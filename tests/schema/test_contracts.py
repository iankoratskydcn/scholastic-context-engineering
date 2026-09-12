import pytest

from scholastic_pipeline.schema import (
    ArgumentUnit,
    EvidenceSpan,
    EnvelopeError,
    IngestedDocument,
    ValidationStatus,
)

def test_envelope_requires_stable_ids_and_provenance():
    span = EvidenceSpan(source_id="source-1", start=0, end=4, text="Prem")
    record = IngestedDocument(document_id="doc-1", revision="r1", bytes_hash="a" * 64, spans=(span,), run_id="run-1")
    assert record.record_id
    assert record.provenance[0].source_id == "source-1"

def test_invalid_span_bounds_are_rejected():
    with pytest.raises(EnvelopeError):
        EvidenceSpan(source_id="source-1", start=4, end=2, text="bad")

def test_validation_statuses_are_closed_and_distinct():
    assert {s.value for s in ValidationStatus} == {"VALID", "INVALID", "UNKNOWN", "UNSUPPORTED", "ILL_POSED"}
    with pytest.raises(ValueError):
        ValidationStatus("maybe")

def test_cross_stage_argument_requires_source_span():
    with pytest.raises(EnvelopeError):
        ArgumentUnit(argument_id="arg-1", premises=(), conclusion="c", relation="entails", provenance=(), run_id="run-1")
