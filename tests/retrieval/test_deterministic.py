from scholastic_pipeline.retrieval.deterministic import retrieve
from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, GraphSnapshot, RetrievalRequest, ValidationStatus


def span(text, start=0, revision="r1"):
    return EvidenceSpan(source_id="book", revision=revision, start=start, end=start + len(text), text=text)


def edge(edge_id, text, start=0, revision="r1"):
    evidence = span(text, start, revision)
    return GraphEdgeEvent(
        edge_instance_id=edge_id, source_node_id="node-a", target_node_id="node-b",
        relation="supports", validation_status=ValidationStatus.VALID,
        provenance=(evidence,), run_id="run-1",
    )


def snapshot(edges, generation="g1"):
    return GraphSnapshot(generation_id=generation, occurrences=tuple(edges), provenance=edges[0].provenance, run_id="run-1")


def test_retrieval_is_bounded_and_deterministically_ranked():
    result = retrieve(
        RetrievalRequest(query="alpha", budget=2, provenance=(span("query"),), run_id="run-1"),
        snapshot([edge("z", "alpha beta"), edge("a", "alpha"), edge("x", "gamma")]),
    )
    assert result.refusal is None
    assert result.items == ("alpha", "alpha beta")
    assert tuple(c.record_id for c in result.citations) == (snapshot([edge("a", "alpha")]).occurrences[0].provenance[0].record_id, snapshot([edge("z", "alpha beta")]).occurrences[0].provenance[0].record_id)


def test_retrieval_refuses_missing_or_stale_provenance_and_budget_overflow():
    request = RetrievalRequest(query="alpha", budget=10, provenance=(span("query"),), run_id="run-1")
    stale = snapshot([edge("a", "alpha", revision="r2")])
    assert retrieve(request, stale, current_revisions={"book": "r1"}).refusal

    over = retrieve(RetrievalRequest(query="alpha", budget=0, provenance=(span("query"),), run_id="run-1"), snapshot([edge("a", "alpha")]))
    assert over.refusal
