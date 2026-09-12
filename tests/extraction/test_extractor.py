import json
from pathlib import Path

from scholastic_pipeline.extraction import extract_argument


FIXTURE = Path(__file__).parents[2] / "fixtures" / "canary" / "argument-cases.json"


def test_canary_modus_ponens_preserves_spans_roles_and_taxonomy_id():
    case = next(c for c in json.loads(FIXTURE.read_text())["cases"] if c["id"] == "modus-ponens")
    result = extract_argument(case["text"], source_id=case["source_id"], run_id="test-run")

    assert result.status == "ACCEPTED"
    assert result.taxonomy.taxonomy_id == "src.core_initial_pass.003.l9"
    assert result.taxonomy.label == "Modus ponens"
    assert [(p.role, p.text) for p in result.argument.premises] == [
        ("premise", "it rains"),
        ("premise", "It rains"),
    ]
    assert result.argument.conclusion.role == "conclusion"
    assert result.argument.conclusion.text == "the ground is wet"
    assert result.argument.relation == "entails"
    for proposition in (*result.argument.premises, result.argument.conclusion):
        assert case["text"][proposition.provenance[0].start:proposition.provenance[0].end] == proposition.text


def test_canary_modus_tollens_preserves_negated_spans_and_taxonomy_id():
    case = next(c for c in json.loads(FIXTURE.read_text())["cases"] if c["id"] == "modus-tollens")
    result = extract_argument(case["text"], source_id=case["source_id"], run_id="test-run")

    assert result.status == "ACCEPTED"
    assert result.taxonomy.taxonomy_id == "src.core_initial_pass.004.l10"
    assert [(p.role, p.text) for p in result.argument.premises] == [
        ("premise", "the alarm is set"),
        ("premise", "The light is not flashing"),
    ]
    assert result.argument.conclusion.text == "the alarm is not set"
    assert result.argument.relation == "entails"


def test_unsupported_text_abstains_with_reason_and_no_argument():
    result = extract_argument("Birds fly. Tweety is a bird.", source_id="unsupported", run_id="test-run")

    assert result.status == "ABSTAINED"
    assert result.argument is None
    assert result.taxonomy is None
    assert result.abstention_reason == "unsupported_argument_form"
