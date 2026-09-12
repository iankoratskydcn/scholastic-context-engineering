import pytest

from scholastic_pipeline.assembly import assemble_edge_events
from scholastic_pipeline.formal import Formalization, validate
from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, Proposition, ValidationStatus


def make_argument():
    a = EvidenceSpan("source-1", 0, 1, "A", revision="rev-2")
    c = EvidenceSpan("source-1", 4, 5, "C", revision="rev-2")
    p = Proposition(proposition_id="p", text="A -> C", role="premise", run_id="run-1", provenance=(a,))
    q = Proposition(proposition_id="q", text="A", role="premise", run_id="run-1", provenance=(a,))
    conclusion = Proposition(proposition_id="c", text="C", role="conclusion", run_id="run-1", provenance=(c,))
    return ArgumentUnit(argument_id="arg-1", premises=(p, q), conclusion=conclusion, relation="entails", run_id="run-1", provenance=(a, c))


def test_assembly_emits_provenance_and_validation_status():
    arg = make_argument()
    result = validate(arg, Formalization("A -> C", provenance=(arg.provenance[0],)))
    events = assemble_edge_events(arg, result)
    assert len(events) == 2
    event = events[0]
    assert event.source_node_id == "p"
    assert event.target_node_id == "c"
    assert events[1].source_node_id == "q"
    assert event.validation_status is ValidationStatus.VALID
    assert event.record_id
    assert events[0].edge_instance_id != events[1].edge_instance_id
    assert {(s.source_id, s.revision, s.start, s.end) for s in event.provenance} == {
        ("source-1", "rev-2", 0, 1), ("source-1", "rev-2", 4, 5)
    }


def test_assembly_rejects_missing_provenance():
    arg = make_argument()
    bad = result = validate(arg, Formalization("A -> C", provenance=(arg.provenance[0],)))
    with pytest.raises(ValueError):
        assemble_edge_events(arg, bad, provenance=())


def test_assembly_rejects_mismatched_provenance_and_ids_include_content():
    arg = make_argument()
    result = validate(arg, Formalization("A -> C", provenance=(arg.provenance[0],)))
    with pytest.raises(ValueError):
        assemble_edge_events(arg, result, provenance=(EvidenceSpan("source-1", 0, 1, "A", revision="other"),))
    events = assemble_edge_events(arg, result)
    assert arg.provenance[0].record_id in events[0].edge_instance_id or events[0].edge_instance_id != assemble_edge_events(
        arg, result, provenance=(arg.provenance[0],),
    )[0].edge_instance_id


def test_assembly_does_not_use_taxonomy_or_frequency_as_proof():
    arg = make_argument()
    result = validate(arg, Formalization("A", provenance=(arg.provenance[0],)))
    event = assemble_edge_events(arg, result, taxonomy_label="causal", frequency=99)[0]
    assert event.validation_status is ValidationStatus.UNKNOWN
