import hashlib
import json

import pytest

from scholastic_pipeline.ingestion import ingest_text, structure_document
from scholastic_pipeline.schema import MAX_IDENTIFIER_BYTES, MAX_SOURCE_TEXT_BYTES, RecordStatus


def test_ingest_uses_exact_utf8_bytes_and_deterministic_identity():
    text = "Alpha\nBeta"
    first = ingest_text("source-01", text, run_id="run-1")
    second = ingest_text("source-01", text, run_id="run-2")

    assert first.status == RecordStatus.ACCEPTED.value
    assert first.bytes_hash == hashlib.sha256(text.encode("utf-8")).hexdigest()
    assert first.document_id == second.document_id
    assert first.revision == second.revision
    assert first.spans[0].start == 0
    assert first.spans[0].end == len(text)
    assert first.spans[0].text == text


def test_structuring_preserves_order_and_exact_half_open_paragraph_spans():
    document = ingest_text("source-01", " First\n\nSecond line\nThird", run_id="run-1")

    structured = structure_document(document)

    assert structured.blocks == (" First", "Second line\nThird")
    assert [(span.start, span.end, span.text) for span in structured.spans] == [
        (0, 6, " First"),
        (8, 25, "Second line\nThird"),
    ]


def test_invalid_or_lossy_utf8_is_quarantined_without_decoding_replacement():
    invalid = ingest_text("source-01", b"good\xffbad", run_id="run-1")
    lossy = ingest_text("source-01", "good\ufffdbad", run_id="run-1")

    assert invalid.status == RecordStatus.QUARANTINED.value
    assert lossy.status == RecordStatus.QUARANTINED.value
    assert invalid.spans == ()
    assert lossy.spans == ()
    assert "utf-8" in " ".join(invalid.diagnostics).lower()


def test_malformed_identity_is_quarantined():
    result = ingest_text("", "text", run_id="run-1")

    assert result.status == RecordStatus.QUARANTINED.value
    assert result.spans == ()


def test_malformed_source_id_is_quarantined_before_identity_hashing():
    for source_id in (object(), "bad\ud800"):
        result = ingest_text(source_id, "text", run_id="run-1")
        assert result.status == RecordStatus.QUARANTINED.value
        assert result.spans == ()
        assert "source_id" in " ".join(result.diagnostics)


def test_oversized_source_id_or_run_id_is_quarantined_without_exception():
    oversized = "x" * (MAX_IDENTIFIER_BYTES + 1)
    for source_id, run_id in ((oversized, "run-1"), ("source", oversized)):
        result = ingest_text(source_id, "text", run_id=run_id)
        assert result.status == RecordStatus.QUARANTINED.value
        assert result.spans == ()


def test_structure_document_refuses_none_and_malformed_inputs():
    for document in (None, object()):
        result = structure_document(document)
        assert result.status == RecordStatus.QUARANTINED.value
        assert result.spans == ()
        assert "document" in " ".join(result.diagnostics).lower()


def test_empty_source_is_quarantined():
    for source in ("", b""):
        result = ingest_text("source-01", source, run_id="run-1")
        assert result.status == RecordStatus.QUARANTINED.value
        assert result.spans == ()
        assert "empty source" in " ".join(result.diagnostics).lower()


def test_oversized_source_is_quarantined_without_constructing_span():
    result = ingest_text("source-01", b"x" * (MAX_SOURCE_TEXT_BYTES + 1), run_id="run-1")
    assert result.status == RecordStatus.QUARANTINED.value
    assert result.spans == ()
    assert "source text exceeds" in " ".join(result.diagnostics).lower()


def test_source_that_exceeds_span_ceiling_is_quarantined_before_span_construction():
    result = ingest_text("source-01", b"x" * 65_537, run_id="run-1")
    assert result.status == RecordStatus.QUARANTINED.value
    assert result.spans == ()
    assert "span" in " ".join(result.diagnostics).lower()


def test_imported_text_is_data_not_code(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    document = ingest_text("source-01", "__import__('os').system('touch SHOULD_NOT_EXIST')", run_id="run-1")

    assert structure_document(document).blocks == ("__import__('os').system('touch SHOULD_NOT_EXIST')",)
    assert not (tmp_path / "SHOULD_NOT_EXIST").exists()


def test_ingestion_payload_contains_complete_envelope_fields():
    document = ingest_text("source-01", "Alpha", run_id="run-1")
    payload = __import__("scholastic_pipeline.ingestion", fromlist=["to_payload"]).to_payload(document)
    assert {"kind", "schema_version", "record_id", "run_id", "producer", "status",
            "provenance", "confidence", "uncertainty", "diagnostics"} <= payload.keys()
    assert payload["record_id"] == document.record_id
    assert payload["run_id"] == "run-1"


def test_ingestion_quarantine_payload_contains_complete_envelope_fields():
    document = ingest_text("", "text", run_id="run-1")
    payload = __import__("scholastic_pipeline.ingestion", fromlist=["to_payload"]).to_payload(document)
    assert {"kind", "schema_version", "record_id", "run_id", "producer", "status",
            "provenance", "confidence", "uncertainty", "diagnostics"} <= payload.keys()
    assert payload["record_id"]


def test_quarantine_payload_has_non_source_diagnostic_provenance():
    document = ingest_text("", "text", run_id="run-1")
    payload = __import__("scholastic_pipeline.ingestion", fromlist=["to_payload"]).to_payload(document)
    assert payload["provenance"]
    diagnostic = payload["provenance"][0]
    assert diagnostic["source_id"].startswith("diagnostic://")
    assert diagnostic["revision"] == "diagnostic"
    assert "no source evidence" in diagnostic["text"]
    assert diagnostic["end"] - diagnostic["start"] == len(diagnostic["text"])
    assert payload["run_id"] == "run-1"
    assert payload["status"] == "QUARANTINED"


def test_quarantine_with_malformed_run_id_is_serializable_and_nonempty_envelope():
    document = ingest_text("source", "text", run_id="bad\ud800")
    payload = __import__("scholastic_pipeline.ingestion", fromlist=["to_payload"]).to_payload(document)
    assert payload["status"] == "QUARANTINED"
    assert payload["run_id"]
    assert json.loads(json.dumps(payload))["provenance"]


def test_quarantine_bounds_identity_fields_but_keeps_diagnostic():
    result = ingest_text("é" * (MAX_IDENTIFIER_BYTES + 1), "text", run_id="bad\ud800")
    payload = __import__("scholastic_pipeline.ingestion", fromlist=["to_payload"]).to_payload(result)
    assert result.status == RecordStatus.QUARANTINED.value
    assert payload["diagnostics"] == ["source_id is malformed"]
    for field in ("source_id", "run_id", "producer", "document_id", "revision"):
        value = payload.get(field)
        assert isinstance(value, str)
        assert not any(0xD800 <= ord(char) <= 0xDFFF for char in value)
        assert len(value.encode("utf-8")) <= MAX_IDENTIFIER_BYTES
    assert json.loads(json.dumps(payload))["diagnostics"] == ["source_id is malformed"]
