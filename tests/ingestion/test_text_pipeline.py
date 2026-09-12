import hashlib

import pytest

from scholastic_pipeline.ingestion import ingest_text, structure_document
from scholastic_pipeline.schema import MAX_SOURCE_TEXT_BYTES, RecordStatus


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
