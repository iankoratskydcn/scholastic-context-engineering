import pytest

from scholastic_pipeline.backends.reference import ReferenceSQLiteBackend, StorageError
from scholastic_pipeline.schema import GraphEdgeEvent, EvidenceSpan, ValidationStatus


def span(source="book", revision="r1", text="alpha"):
    return EvidenceSpan(source_id=source, revision=revision, start=0, end=len(text), text=text)


def edge(edge_id, run_id="run-1", source="book"):
    return GraphEdgeEvent(edge_instance_id=edge_id, source_node_id="a", target_node_id="b",
                          relation="supports", validation_status=ValidationStatus.VALID,
                          provenance=(span(source=source),), run_id=run_id)


def test_append_rejects_mixed_envelopes_in_one_generation():
    backend = ReferenceSQLiteBackend()
    backend.begin_generation("g1")
    backend.append("g1", edge("a"))
    with pytest.raises(StorageError):
        backend.append("g1", edge("b", run_id="run-2"))


def test_retry_cannot_mutate_completed_generation():
    backend = ReferenceSQLiteBackend()
    backend.write_generation("g1", [edge("a")])
    with pytest.raises(StorageError):
        backend.write_generation("g1", [edge("a", source="other")])
