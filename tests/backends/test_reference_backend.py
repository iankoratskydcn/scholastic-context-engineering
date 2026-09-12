import pytest

from scholastic_pipeline.backends.reference import (
    IncompleteGenerationError,
    ProvenanceError,
    ReferenceSQLiteBackend,
)
from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, ValidationStatus


def span(source="book", revision="r1", text="alpha", start=0):
    return EvidenceSpan(source_id=source, revision=revision, start=start, end=start + len(text), text=text)


def edge(edge_id, source_node="a", target_node="b", evidence=None):
    return GraphEdgeEvent(
        edge_instance_id=edge_id,
        source_node_id=source_node,
        target_node_id=target_node,
        relation="supports",
        validation_status=ValidationStatus.VALID,
        provenance=(evidence or span(),),
        run_id="run-1",
    )


def test_retry_is_idempotent_and_distinct_occurrences_are_preserved():
    backend = ReferenceSQLiteBackend()
    first = edge("occ-1", evidence=span(text="same", start=0))
    second = edge("occ-2", evidence=span(text="same", start=10))

    backend.write_generation("g1", [first, second])
    backend.write_generation("g1", [first, second])

    snapshot = backend.read_generation("g1")
    assert [item.edge_instance_id for item in snapshot.occurrences] == ["occ-1", "occ-2"]
    assert [item.provenance[0].start for item in snapshot.occurrences] == [0, 10]


def test_incomplete_generation_is_not_readable():
    backend = ReferenceSQLiteBackend()
    backend.begin_generation("g1")
    backend.append("g1", edge("occ-1"))

    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_stale_or_missing_provenance_is_rejected():
    backend = ReferenceSQLiteBackend(current_revisions={"book": "r2"})
    with pytest.raises(ProvenanceError):
        backend.write_generation("g1", [edge("occ-1", evidence=span(revision="r1"))])

    # The canonical schema itself fails closed before storage can accept it.
    with pytest.raises(ValueError):
        GraphEdgeEvent(
            edge_instance_id="occ-2", source_node_id="a", target_node_id="b", relation="supports",
            validation_status=ValidationStatus.VALID, provenance=(), run_id="run-1",
        )
