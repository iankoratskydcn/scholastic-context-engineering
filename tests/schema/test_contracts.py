import json

import pytest

from scholastic_pipeline.schema import (
    ArgumentUnit,
    EvidenceSpan,
    EnvelopeError,
    GraphEdgeEvent,
    IngestedDocument,
    Proposition,
    TaxonomyMatch,
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


def test_structured_document_rejects_block_span_cardinality_mismatch():
    source = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    with pytest.raises(EnvelopeError, match="blocks and spans"):
        from scholastic_pipeline.schema import StructuredDocument
        StructuredDocument(document_id="doc-1", revision="r1", bytes_hash="a" * 64,
                           spans=(source,), blocks=("A", "extra"), run_id="run-1")


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


def test_graph_edge_event_rejects_empty_required_identity_fields():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    values = {
        "edge_instance_id": "edge-1",
        "source_node_id": "source-1",
        "target_node_id": "target-1",
        "relation": "entails",
    }
    for field_name in values:
        invalid = {**values, field_name: ""}
        with pytest.raises(EnvelopeError, match=field_name):
            GraphEdgeEvent(**invalid, run_id="run-1", provenance=(span,))


def test_graph_edge_event_rejects_empty_provenance():
    with pytest.raises(EnvelopeError, match="provenance"):
        GraphEdgeEvent(edge_instance_id="edge-1", source_node_id="source-1",
                       target_node_id="target-1", relation="entails", run_id="run-1",
                       provenance=())


def test_graph_edge_event_payload_is_json_loadable_with_record_id():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    event = GraphEdgeEvent(edge_instance_id="edge-1", source_node_id="source-1",
                           target_node_id="target-1", relation="entails",
                           run_id="run-1", provenance=(span,))
    payload = json.loads(json.dumps(event.to_payload()))
    assert {"schema_version", "record_id", "run_id", "producer", "status",
            "provenance", "confidence", "uncertainty", "diagnostics"} <= payload.keys()
    assert payload["record_id"] == event.record_id


def test_direct_canonical_records_require_nonempty_domain_fields():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    with pytest.raises(EnvelopeError, match="proposition_id"):
        from scholastic_pipeline.schema import Proposition
        Proposition(text="A", role="premise", run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="text"):
        from scholastic_pipeline.schema import Proposition
        Proposition(proposition_id="p1", text="", role="premise", run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="role"):
        from scholastic_pipeline.schema import Proposition
        Proposition(proposition_id="p1", text="A", role="", run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="conclusion"):
        ArgumentUnit(argument_id="arg-1", premises=(Proposition(proposition_id="p1", text="A", role="premise",
                     run_id="run-1", provenance=(span,)),), conclusion="", relation="entails",
                     run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="taxonomy_id"):
        from scholastic_pipeline.schema import TaxonomyMatch
        TaxonomyMatch(label="label", run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="label"):
        from scholastic_pipeline.schema import TaxonomyMatch
        TaxonomyMatch(taxonomy_id="tax-1", label="", run_id="run-1", provenance=(span,))


def test_snapshot_records_require_generation_fields():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    from scholastic_pipeline.schema import CommunitySnapshot, GraphSnapshot
    with pytest.raises(EnvelopeError, match="generation_id"):
        GraphSnapshot(run_id="run-1", provenance=(span,))
    with pytest.raises(EnvelopeError, match="graph_generation"):
        CommunitySnapshot(run_id="run-1", provenance=(span,))


def test_every_canonical_payload_has_record_id_without_self_hashing():
    span = EvidenceSpan("source-1", 0, 1, "A", revision="r1")
    from scholastic_pipeline.schema import Proposition, TaxonomyMatch, GraphSnapshot, CommunitySnapshot
    records = [
        Proposition(proposition_id="p1", text="A", role="premise", run_id="run-1", provenance=(span,)),
        TaxonomyMatch(taxonomy_id="tax-1", label="label", run_id="run-1", provenance=(span,)),
        GraphSnapshot(generation_id="gen-1", run_id="run-1", provenance=(span,)),
        CommunitySnapshot(graph_generation="gen-1", run_id="run-1", provenance=(span,)),
    ]
    for record in records:
        payload = record.to_payload()
        assert payload["record_id"] == record.record_id
        assert "record_id" not in json.dumps(payload["record_id"])
        assert json.loads(json.dumps(payload))["record_id"] == record.record_id
