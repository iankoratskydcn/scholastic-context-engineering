import pytest

from scholastic_pipeline.retrieval.deterministic import retrieve
from scholastic_pipeline.retrieval.deterministic import MAX_RETRIEVAL_OCCURRENCES
from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, GraphSnapshot, RetrievalRequest, ValidationStatus, RecordStatus

MAX_RETRIEVAL_BUDGET = 100


def span(text, source="book", start=0, revision="r1"):
    return EvidenceSpan(source_id=source, revision=revision, start=start, end=start + len(text), text=text)


def edge(edge_id, text, run_id="run-1", status=RecordStatus.ACCEPTED.value, source="book"):
    return GraphEdgeEvent(
        edge_instance_id=edge_id, source_node_id="node-a", target_node_id="node-b",
        relation="supports", validation_status=ValidationStatus.VALID,
        provenance=(span(text, source=source),), run_id=run_id, status=status,
    )


def snapshot(edges, generation="g1", run_id="run-1", status=RecordStatus.ACCEPTED.value):
    return GraphSnapshot(generation_id=generation, occurrences=tuple(edges),
                         provenance=edges[0].provenance, run_id=run_id, status=status)


def request(query="alpha", budget=2, run_id="run-1", provenance=None, status=RecordStatus.ACCEPTED.value):
    return RetrievalRequest(query=query, budget=budget,
                            provenance=provenance or (span("query"),), run_id=run_id, status=status)


def test_retrieval_refuses_budget_above_absolute_ceiling():
    result = retrieve(request(budget=MAX_RETRIEVAL_BUDGET + 1), snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval budget exceeds absolute ceiling"


@pytest.mark.parametrize("run_id", ["wrong"])
def test_retrieval_refuses_mismatched_run_id(run_id):
    assert retrieve(request(run_id=run_id), snapshot([edge("a", "alpha")])).refusal


def test_retrieval_refuses_non_admissible_status_and_mixed_provenance_scope():
    assert retrieve(request(), snapshot([edge("a", "alpha", status=RecordStatus.QUARANTINED.value)])).refusal
    mixed = snapshot([edge("a", "alpha"), edge("b", "alpha", source="other")])
    assert retrieve(request(), mixed).refusal


def test_retrieval_no_match_is_a_valid_empty_context():
    result = retrieve(request(query="absent"), snapshot([edge("a", "alpha")]))
    assert result.refusal is None
    assert result.items == ()
    assert result.citations == ()


def test_retrieval_refuses_missing_snapshot_provenance():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "provenance", ())
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval provenance is missing"


def test_retrieval_refuses_forged_snapshot_missing_generation_id_before_iteration():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "generation_id", "")
    object.__setattr__(snap, "occurrences", object())
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval snapshot generation ID is missing"


def test_retrieval_request_accepts_non_string_query_for_refusal_without_stable_id_error():
    req = RetrievalRequest(query=object(), budget=2, provenance=(span("query"),), run_id="run-1")
    result = retrieve(req, snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query must be a string"


def test_retrieval_refuses_non_string_query_without_string_operations():
    req = request()
    object.__setattr__(req, "query", object())
    result = retrieve(req, snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query must be a string"


def test_retrieval_refuses_lone_surrogate_query_without_encoding():
    req = request()
    object.__setattr__(req, "query", "bad\ud800")
    result = retrieve(req, snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query contains an invalid surrogate"


def test_retrieval_request_accepts_surrogate_query_for_refusal_without_stable_id_error():
    req = RetrievalRequest(query="bad\ud800", budget=2, provenance=(span("query"),), run_id="run-1")
    result = retrieve(req, snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query contains an invalid surrogate"


def test_retrieval_request_accepts_oversized_query_for_refusal_without_stable_id_error():
    req = RetrievalRequest(query="a" * 16_385, budget=2, provenance=(span("query"),), run_id="run-1")
    result = retrieve(req, snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval query exceeds absolute byte ceiling"


def test_retrieval_refuses_malformed_span_before_string_operations():
    evidence = span("alpha")
    object.__setattr__(evidence, "text", object())
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap.occurrences[0], "provenance", (evidence,))
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval provenance span is malformed"


def test_retrieval_refuses_forged_snapshot_before_iterating_occurrences():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "occurrences", object())
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval snapshot occurrences are malformed"


def test_retrieval_refuses_non_snapshot_without_uncaught_exception():
    result = retrieve(request(), object())
    assert result.refusal == "retrieval snapshot is malformed"


def test_retrieval_refuses_forged_occurrence_before_iteration():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "occurrences", (object(),))
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval snapshot occurrences are malformed"


def test_retrieval_refuses_arbitrary_request_without_uncaught_exception():
    result = retrieve(object(), snapshot([edge("a", "alpha")]))
    assert result.refusal == "retrieval request is malformed"


def test_retrieval_refuses_non_mapping_current_revisions_before_lookup():
    result = retrieve(request(), snapshot([edge("a", "alpha")]), current_revisions=[("book", "r1")])
    assert result.refusal == "retrieval current revisions are malformed"


def test_retrieval_refuses_forged_empty_snapshot_before_no_match_result():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "occurrences", ())
    result = retrieve(request(query="absent"), snap)
    assert result.refusal == "retrieval snapshot occurrences are empty"


def test_retrieval_refuses_snapshot_occurrence_count_above_ceiling():
    snap = snapshot([edge("a", "alpha")])
    object.__setattr__(snap, "occurrences", (snap.occurrences[0],) * (MAX_RETRIEVAL_OCCURRENCES + 1))
    result = retrieve(request(), snap)
    assert result.refusal == "retrieval snapshot occurrences exceed absolute ceiling"


def test_retrieval_refuses_hostile_revision_mapping_get():
    class HostileMapping(dict):
        def get(self, *_args, **_kwargs):
            raise RuntimeError("hostile get")

    result = retrieve(request(), snapshot([edge("a", "alpha")]), HostileMapping())
    assert result.refusal == "retrieval current revisions are malformed"
