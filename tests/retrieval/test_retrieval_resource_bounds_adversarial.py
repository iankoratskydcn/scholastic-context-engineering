import pytest

from scholastic_pipeline.retrieval.deterministic import retrieve
from scholastic_pipeline.schema import (
    EvidenceSpan, GraphEdgeEvent, GraphSnapshot, MAX_SPAN_TEXT_BYTES, RecordStatus,
    RetrievalRequest, ValidationStatus,
)

MAX_RETRIEVAL_QUERY_BYTES = 16_384
MAX_RETRIEVAL_INPUT_BYTES = 4_194_304
MAX_RETRIEVAL_OUTPUT_BYTES = 1_048_576


def span(text, source="book", start=0, revision="r1"):
    return EvidenceSpan(source, start, start + len(text), text, revision)


def edge(edge_id, text):
    return GraphEdgeEvent(
        edge_instance_id=edge_id, source_node_id="node-a", target_node_id="node-b",
        relation="supports", validation_status=ValidationStatus.VALID,
        provenance=(span(text),), run_id="run-1",
    )


def snapshot(edges):
    return GraphSnapshot(
        generation_id="g1", occurrences=tuple(edges),
        provenance=edges[0].provenance, run_id="run-1",
    )


def request(query="alpha", budget=100):
    return RetrievalRequest(
        query=query, budget=budget, provenance=(span("query"),), run_id="run-1",
    )


def test_retrieval_rejects_query_one_utf8_byte_over_ceiling():
    query = "é" * ((MAX_RETRIEVAL_QUERY_BYTES // 2) + 1)
    result = retrieve(request(query), snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query exceeds absolute byte ceiling"


def test_retrieval_accepts_query_at_exact_byte_ceiling():
    query = "a" * MAX_RETRIEVAL_QUERY_BYTES
    result = retrieve(request(query), snapshot([edge("a", "alpha")]))
    assert result.refusal is None
    assert result.items == ()


def test_retrieval_rejects_forged_oversized_span():
    evidence = span("alpha")
    object.__setattr__(evidence, "text", "x" * (MAX_SPAN_TEXT_BYTES + 1))
    event = GraphEdgeEvent(
        edge_instance_id="a", source_node_id="node-a", target_node_id="node-b",
        relation="supports", validation_status=ValidationStatus.VALID,
        provenance=(evidence,), run_id="run-1",
    )
    result = retrieve(request(), snapshot([event]))
    assert result.refusal == "retrieval span exceeds absolute byte ceiling"


def test_retrieval_rejects_input_bytes_before_ranking():
    text = "alpha " + "x" * (MAX_SPAN_TEXT_BYTES // 2)
    edges = [edge(str(index), text) for index in range(
        (MAX_RETRIEVAL_INPUT_BYTES // len(text.encode("utf-8"))) + 1
    )]
    result = retrieve(request(), snapshot(edges))
    assert result.refusal == "retrieval input exceeds absolute byte ceiling"


def test_retrieval_rejects_output_bytes_before_returning_context():
    text = "alpha " + "x" * (MAX_RETRIEVAL_OUTPUT_BYTES // 20)
    edges = [edge(str(index), text) for index in range(25)]
    result = retrieve(request(), snapshot(edges))
    assert result.refusal == "retrieval output exceeds absolute byte ceiling"


def test_retrieval_input_and_output_ceiling_constants_are_positive():
    assert 0 < MAX_RETRIEVAL_QUERY_BYTES < MAX_RETRIEVAL_INPUT_BYTES
    assert 0 < MAX_RETRIEVAL_OUTPUT_BYTES <= MAX_RETRIEVAL_INPUT_BYTES
