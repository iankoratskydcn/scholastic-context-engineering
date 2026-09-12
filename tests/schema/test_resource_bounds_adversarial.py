import pytest

from scholastic_pipeline.schema import EvidenceSpan, EnvelopeError, IngestedDocument

MAX_SOURCE_TEXT_BYTES = 1_048_576
MAX_SPAN_TEXT_BYTES = 65_536


def test_evidence_span_accepts_exact_utf8_byte_boundary():
    text = "é" * (MAX_SPAN_TEXT_BYTES // 2)
    span = EvidenceSpan("source-1", 0, len(text), text, revision="r1")
    assert len(span.text.encode("utf-8")) == MAX_SPAN_TEXT_BYTES


def test_evidence_span_rejects_one_byte_overflow():
    text = "é" * ((MAX_SPAN_TEXT_BYTES // 2) + 1)
    with pytest.raises(EnvelopeError, match="text exceeds absolute byte ceiling"):
        EvidenceSpan("source-1", 0, len(text), text, revision="r1")


def test_document_rejects_aggregate_source_text_overflow():
    text = "A" * MAX_SPAN_TEXT_BYTES
    spans = tuple(
        EvidenceSpan("source-1", index * len(text), (index + 1) * len(text), text, revision="r1")
        for index in range((MAX_SOURCE_TEXT_BYTES // MAX_SPAN_TEXT_BYTES) + 1)
    )
    with pytest.raises(EnvelopeError, match="source text exceeds absolute byte ceiling"):
        IngestedDocument(
            document_id="doc-1", revision="r1", bytes_hash="a" * 64,
            spans=spans, run_id="run-1",
        )


def test_document_source_ceiling_is_canonical_and_nonzero():
    assert MAX_SOURCE_TEXT_BYTES >= MAX_SPAN_TEXT_BYTES
