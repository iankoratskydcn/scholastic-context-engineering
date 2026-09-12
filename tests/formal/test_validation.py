import pytest

from dataclasses import replace

from scholastic_pipeline.formal import Formalization, validate
from scholastic_pipeline.extraction import ExtractionBundle
from scholastic_pipeline.schema import (
    ArgumentUnit, EvidenceSpan, Proposition, StructuredDocument, TaxonomyMatch, TaxonomySnapshot, ValidationStatus,
)


def span(text="A", start=0):
    return EvidenceSpan("source-1", start, start + len(text), text, revision="rev-2")


def argument(premises, conclusion):
    ps = tuple(Proposition(proposition_id=f"p{i}", text=p, role="premise", run_id="run-1", provenance=(span(p),)) for i, p in enumerate(premises))
    c = Proposition(proposition_id="c", text=conclusion, role="conclusion", run_id="run-1", provenance=(span(conclusion, 20),))
    return ArgumentUnit(argument_id="arg-1", premises=ps, conclusion=c, relation="entails", run_id="run-1", provenance=(span("A"),))


def test_modus_ponens_validates_without_solver():
    result = validate(argument(["A -> B", "A"], "B"), Formalization("A -> B", provenance=(span("A"),)))
    assert result.validation_status is ValidationStatus.VALID
    assert result.normalized_form == "A -> B"


def test_modus_tollens_validates():
    result = validate(argument(["A -> B", "¬B"], "¬A"), Formalization("A → B", provenance=(span("A"),)))
    assert result.validation_status is ValidationStatus.VALID


def test_malformed_supported_form_is_invalid_not_unknown():
    result = validate(argument(["A -> B", "A"], "C"), Formalization("A -> B", provenance=(span("A"),)))
    assert result.validation_status is ValidationStatus.INVALID


@pytest.mark.parametrize("expression", ["A", "A | B", "A -> B -> C", "A & B -> C", ""])
def test_other_forms_are_closed_as_unknown_or_unsupported(expression):
    result = validate(argument(["A"], "C"), Formalization(expression, provenance=(span("A"),)))
    assert result.validation_status in {ValidationStatus.UNKNOWN, ValidationStatus.UNSUPPORTED}




def test_validation_rejects_missing_taxonomy_in_canonical_extraction():
    from scholastic_pipeline.extraction import ExtractionBundle
    bundle = ExtractionBundle("ACCEPTED", argument(["A -> B", "A"], "B"), None, None, 1.0, span("A"))
    with pytest.raises(ValueError):
        validate(bundle, Formalization("A -> B", provenance=(span("A"),)))


def test_bundle_validation_requires_compatible_taxonomy_and_matching_provenance():
    arg = argument(["A -> B", "A"], "B")
    taxonomy = TaxonomyMatch(taxonomy_id="tax", label="modus", run_id="run-1", provenance=(span("A"),))
    bundle = ExtractionBundle("ACCEPTED", arg, taxonomy, None, 1.0, span("A"),
                             Formalization("A -> B", run_id="run-1", provenance=(span("A"),)))
    assert validate(bundle, bundle.formalization).validation_status is ValidationStatus.VALID
    wrong = TaxonomyMatch(taxonomy_id="other", label="modus", run_id="run-1", provenance=(span("A"),))
    with pytest.raises(ValueError):
        validate(bundle, bundle.formalization, wrong)
    wrong_run = Formalization("A -> B", run_id="other", provenance=(span("A"),))
    with pytest.raises(ValueError):
        validate(bundle, wrong_run)


def test_validation_rejects_wrong_canonical_input_type():
    with pytest.raises(TypeError):
        validate({"argument": "not-an-extraction"}, Formalization("A -> B", provenance=(span("A"),)))

    with pytest.raises(ValueError):
        validate(argument(["A -> B", "A"], "B"), Formalization("A -> B", provenance=()))
