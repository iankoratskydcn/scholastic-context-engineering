import pytest

from scholastic_pipeline.schema import (
    ArgumentUnit,
    EvidenceSpan,
    EnvelopeError,
    IngestedDocument,
    ValidationStatus,
    TaxonomySnapshot,
)

def test_envelope_requires_stable_ids_and_provenance():
    span = EvidenceSpan(source_id="source-1", start=0, end=4, text="Prem", revision="r1")
    record = IngestedDocument(document_id="doc-1", revision="r1", bytes_hash="a" * 64, spans=(span,), run_id="run-1")
    assert record.record_id
    assert record.provenance[0].source_id == "source-1"

def test_invalid_span_bounds_are_rejected():
    with pytest.raises(EnvelopeError):
        EvidenceSpan(source_id="source-1", start=4, end=2, text="bad", revision="r1")

def test_validation_statuses_are_closed_and_distinct():
    assert {s.value for s in ValidationStatus} == {"VALID", "INVALID", "UNKNOWN", "UNSUPPORTED", "ILL_POSED"}
    with pytest.raises(ValueError):
        ValidationStatus("maybe")

def test_cross_stage_argument_requires_source_span():
    with pytest.raises(EnvelopeError):
        ArgumentUnit(argument_id="arg-1", premises=(), conclusion="c", relation="entails", provenance=(), run_id="run-1")


def test_evidence_span_requires_non_empty_string_revision():
    for revision in ("", None, 42):
        with pytest.raises(EnvelopeError):
            EvidenceSpan("source-1", 0, 1, "A", revision=revision)


def test_taxonomy_snapshot_is_canonical_and_requires_supported_ids():
    snapshot = TaxonomySnapshot(snapshot_id="taxonomy-1", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
                                run_id="run-1", provenance=(EvidenceSpan("taxonomy", 0, 1, "T", "rev-1"),))
    assert snapshot.record_id
    assert snapshot.supported_taxonomy_ids == ("src.core_initial_pass.003.l9",)


def test_record_id_changes_with_subclass_content_and_identity():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    first = IngestedDocument(document_id="doc-1", revision="r1", bytes_hash="a" * 64, spans=(span,), run_id="run-1")
    second = IngestedDocument(document_id="doc-2", revision="r1", bytes_hash="a" * 64, spans=(span,), run_id="run-1")
    assert first.record_id != second.record_id


def test_canonical_payload_preserves_envelope_and_subclass_fields():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    record = IngestedDocument(document_id="doc-1", revision="r1", bytes_hash="a" * 64,
                              spans=(span,), run_id="run-1", producer="custom",
                              confidence=0.75, uncertainty=("u",), diagnostics=("d",))
    payload = record.to_payload()
    assert payload["producer"] == "custom"
    assert payload["confidence"] == 0.75
    assert payload["uncertainty"] == ["u"]
    assert payload["diagnostics"] == ["d"]
    assert payload["document_id"] == "doc-1"
    assert payload["revision"] == "r1"
    assert payload["bytes_hash"] == "a" * 64
    assert payload["spans"][0]["revision"] == "r1"
