import pytest

from scholastic_pipeline.backends.reference import (
    IncompleteGenerationError,
    ProvenanceError,
    ReferenceSQLiteBackend,
    StorageError,
    MAX_IDENTIFIER_BYTES,
)
from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, ValidationStatus


def span(source="book", revision="r1", text="alpha", start=0):
    return EvidenceSpan(source_id=source, revision=revision, start=start,
                        end=start + len(text), text=text)


def envelope_edge(edge_id="occ-1", **kwargs):
    values = dict(
        edge_instance_id=edge_id, source_node_id="a", target_node_id="b",
        relation="supports", validation_status=ValidationStatus.VALID,
        provenance=(span(text="alpha"),), run_id="run-1", producer="producer-x",
        confidence=0.37, uncertainty=("u",), diagnostics=("d",),
    )
    values.update(kwargs)
    return GraphEdgeEvent(**values)


def test_sqlite_round_trip_preserves_complete_edge_envelope():
    backend = ReferenceSQLiteBackend()
    event = envelope_edge()
    restored = backend.write_generation("g1", [event]).occurrences[0]
    assert restored == event
    assert restored.record_id == event.record_id


def test_generation_rejects_mixed_run_schema_and_provenance_scope():
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.write_generation("g1", [envelope_edge(), envelope_edge("occ-2", run_id="run-2")])
    with pytest.raises(StorageError):
        backend.write_generation("g2", [envelope_edge(), envelope_edge("occ-2", provenance=(span(source="other"),))])


def test_expected_count_and_manifest_are_required_for_completion():
    backend = ReferenceSQLiteBackend()
    with pytest.raises(IncompleteGenerationError):
        backend.write_generation("g1", [envelope_edge()], expected_count=2)
    with pytest.raises(IncompleteGenerationError):
        backend.write_generation("g2", [envelope_edge()], expected_count=1, manifest=("wrong",))


def test_manifest_rejects_duplicate_ids_before_storage():
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.begin_generation("g1", expected_count=2, manifest=("occ-1", "occ-1"))
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_manifest_matching_preserves_occurrence_order_and_cardinality():
    backend = ReferenceSQLiteBackend()
    events = [envelope_edge("occ-1"), envelope_edge("occ-2")]
    with pytest.raises(IncompleteGenerationError):
        backend.write_generation("g1", events, expected_count=2, manifest=("occ-2", "occ-1"))
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_repeated_begin_rejects_conflicting_options_without_mutating_declaration():
    backend = ReferenceSQLiteBackend()
    backend.begin_generation("g1", expected_count=1, manifest=("occ-1",))
    with pytest.raises(StorageError):
        backend.begin_generation("g1", expected_count=1, manifest=("occ-2",))
    with pytest.raises(StorageError):
        backend.begin_generation("g1", expected_count=2, manifest=("occ-1", "occ-2"))
    backend.append("g1", envelope_edge("occ-1"))
    backend.complete_generation("g1")
    assert backend.read_generation("g1").occurrences[0].edge_instance_id == "occ-1"


def test_repeated_begin_with_same_options_is_idempotent_for_completed_generation():
    backend = ReferenceSQLiteBackend()
    backend.write_generation("g1", [envelope_edge("occ-1")], expected_count=1, manifest=("occ-1",))
    backend.begin_generation("g1", expected_count=1, manifest=("occ-1",))
    assert backend.read_generation("g1").occurrences[0].edge_instance_id == "occ-1"


def test_manifest_entry_identifier_obeys_canonical_byte_ceiling():
    backend = ReferenceSQLiteBackend()
    oversized_id = "é" * (MAX_IDENTIFIER_BYTES // 2 + 1)
    with pytest.raises(StorageError):
        backend.begin_generation("g1", expected_count=1, manifest=(oversized_id,))
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_duplicate_event_ids_are_rejected_without_partial_generation():
    backend = ReferenceSQLiteBackend()
    events = [envelope_edge("occ-1"), envelope_edge("occ-1")]
    with pytest.raises(StorageError):
        backend.write_generation("g1", events, expected_count=2)
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_failed_generation_is_atomic_and_retry_can_start_clean():
    backend = ReferenceSQLiteBackend(current_revisions={"book": "r1"})
    with pytest.raises(ProvenanceError):
        backend.write_generation("g1", [envelope_edge(), envelope_edge("bad", provenance=(span(revision="r2"),))])
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")
    assert backend.write_generation("g1", [envelope_edge()]).occurrences[0].edge_instance_id == "occ-1"


def test_completed_generation_cannot_accept_new_occurrence():
    backend = ReferenceSQLiteBackend()
    backend.write_generation("g1", [envelope_edge()])
    with pytest.raises(StorageError):
        backend.append("g1", envelope_edge("occ-2"))


@pytest.mark.parametrize("generation_id", [None, 42, object(), ""])
def test_public_methods_reject_malformed_generation_ids_with_storage_error(generation_id):
    backend = ReferenceSQLiteBackend()
    event = envelope_edge()
    for operation in (
        lambda: backend.begin_generation(generation_id),
        lambda: backend.append(generation_id, event),
        lambda: backend.complete_generation(generation_id),
        lambda: backend.write_generation(generation_id, [event]),
        lambda: backend.read_generation(generation_id),
    ):
        with pytest.raises(StorageError):
            operation()


@pytest.mark.parametrize("events", [None, 42])
def test_write_generation_rejects_non_iterable_events_with_storage_error(events):
    with pytest.raises(StorageError):
        ReferenceSQLiteBackend().write_generation("g1", events)


@pytest.mark.parametrize("event", [None, object(), {"edge_instance_id": "occ-1"}])
def test_append_rejects_malformed_events_with_storage_error(event):
    with pytest.raises(StorageError):
        ReferenceSQLiteBackend().append("g1", event)


def test_write_generation_wraps_generator_failures_and_rolls_back():
    backend = ReferenceSQLiteBackend()

    def failing_events():
        yield envelope_edge()
        raise RuntimeError("boom")

    with pytest.raises(StorageError):
        backend.write_generation("g1", failing_events())
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_write_generation_wraps_malformed_event_attributes_with_storage_error():
    class BrokenEvent:
        edge_instance_id = "occ-1"

    with pytest.raises(StorageError):
        ReferenceSQLiteBackend().write_generation("g1", [BrokenEvent()])


@pytest.mark.parametrize("revisions", [[], object(), "book:r1"])
def test_backend_rejects_non_mapping_current_revisions(revisions):
    with pytest.raises(StorageError):
        ReferenceSQLiteBackend(current_revisions=revisions)


@pytest.mark.parametrize("expected_count", [True, False, 1.0, "1", object()])
def test_generation_options_reject_non_integer_expected_count_before_storage(expected_count):
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.begin_generation("g1", expected_count=expected_count)
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


@pytest.mark.parametrize("manifest", ["occ-1", ["occ-1", 2], [""], object()])
def test_generation_options_reject_malformed_manifest_before_storage(manifest):
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.begin_generation("g1", manifest=manifest)
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_generation_options_reject_manifest_over_bound_before_storage():
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.begin_generation("g1", manifest=["occ"] * 100_001)
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_append_validates_event_before_creating_generation():
    backend = ReferenceSQLiteBackend()
    with pytest.raises(StorageError):
        backend.append("g1", None)
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_storage_rejects_huge_generation_and_occurrence_identifiers():
    backend = ReferenceSQLiteBackend()
    event = envelope_edge()
    object.__setattr__(event, "edge_instance_id", "x" * (MAX_IDENTIFIER_BYTES + 1))
    with pytest.raises(StorageError):
        backend.begin_generation("g" * (MAX_IDENTIFIER_BYTES + 1))
    with pytest.raises(StorageError):
        backend.write_generation("g1", [event])


def test_append_rolls_back_when_internal_storage_step_fails(monkeypatch):
    backend = ReferenceSQLiteBackend()
    monkeypatch.setattr(backend, "_append", lambda *_: (_ for _ in ()).throw(RuntimeError("boom")))
    with pytest.raises(RuntimeError, match="boom"):
        backend.append("g1", envelope_edge())
    with pytest.raises(IncompleteGenerationError):
        backend.read_generation("g1")


def test_append_rolls_back_when_existing_scope_rejects_event():
    backend = ReferenceSQLiteBackend()
    backend.begin_generation("g1")
    backend.append("g1", envelope_edge())
    with pytest.raises(StorageError):
        backend.append("g1", envelope_edge("occ-2", run_id="other"))
    assert backend._db.execute("SELECT COUNT(*) FROM occurrences WHERE generation_id='g1'").fetchone()[0] == 1
