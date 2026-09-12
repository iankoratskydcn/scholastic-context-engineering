import json
from pathlib import Path

import pytest

from scholastic_pipeline.extraction import extract_argument, extract_structured_document
from scholastic_pipeline.formal import validate
from scholastic_pipeline.schema import EvidenceSpan, StructuredDocument, TaxonomySnapshot


FIXTURE = Path(__file__).parents[2] / "fixtures" / "canary" / "argument-cases.json"


def test_production_extraction_requires_structured_document_and_snapshot():
    with pytest.raises(TypeError):
        extract_structured_document("text", None)


def test_production_extraction_abstains_for_unsupported_taxonomy_and_preserves_identity():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-9")
    document = StructuredDocument(document_id="doc", revision="rev-9", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="test-run")
    taxonomy = TaxonomySnapshot(snapshot_id="taxonomy", supported_taxonomy_ids=("unknown",),
                                run_id="test-run", provenance=(source,))
    result = extract_structured_document(document, taxonomy)
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "unsupported_taxonomy"
    assert result.provenance == source


def test_production_extraction_preserves_exact_document_span_and_revision():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-10")
    document = StructuredDocument(document_id="doc", revision="rev-10", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="test-run")
    taxonomy = TaxonomySnapshot(snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
                                run_id="test-run", provenance=(source,))
    result = extract_structured_document(document, taxonomy)
    assert result.status == "ACCEPTED"
    assert result.provenance == source
    assert result.argument.provenance == (source,)
    assert result.taxonomy.provenance == (source,)



def test_canary_modus_ponens_preserves_spans_roles_and_taxonomy_id():
    case = next(c for c in json.loads(FIXTURE.read_text())["cases"] if c["id"] == "modus-ponens")
    result = extract_argument(case["text"], source_id=case["source_id"], source_revision="rev-1", run_id="test-run")

    assert result.status == "ACCEPTED"
    assert result.taxonomy.taxonomy_id == "src.core_initial_pass.003.l9"
    assert result.taxonomy.label == "Modus ponens"
    assert [(p.role, p.text) for p in result.argument.premises] == [
        ("premise", "it rains -> the ground is wet"),
        ("premise", "it rains"),
    ]
    assert result.argument.conclusion.role == "conclusion"
    assert result.argument.conclusion.text == "the ground is wet"
    assert result.argument.relation == "entails"
    assert all(span.revision == "rev-1" for span in result.argument.provenance)


def test_canary_modus_tollens_preserves_negated_spans_and_taxonomy_id():
    case = next(c for c in json.loads(FIXTURE.read_text())["cases"] if c["id"] == "modus-tollens")
    result = extract_argument(case["text"], source_id=case["source_id"], source_revision="rev-1", run_id="test-run")

    assert result.status == "ACCEPTED"
    assert result.taxonomy.taxonomy_id == "src.core_initial_pass.004.l10"
    assert [(p.role, p.text) for p in result.argument.premises] == [
        ("premise", "the alarm is set -> the light is flashing"),
        ("premise", "¬the light is flashing"),
    ]
    assert result.argument.conclusion.text == "¬the alarm is set"
    assert result.argument.relation == "entails"


def test_unsupported_text_abstains_with_reason_and_no_argument():
    result = extract_argument("Birds fly. Tweety is a bird.", source_id="unsupported", source_revision="rev-1", run_id="test-run")

    assert result.status == "ABSTAINED"
    assert result.argument is None
    assert result.taxonomy is None
    assert result.abstention_reason == "unsupported_argument_form"


def test_extraction_propagates_explicit_revision_to_every_evidence_span():
    result = extract_argument("If it rains, the ground is wet. It rains. Therefore, the ground is wet.",
                              source_id="source", source_revision="rev-7", run_id="test-run")
    assert result.status == "ACCEPTED"
    groups = [result.argument.provenance, result.taxonomy.provenance]
    groups.extend(p.provenance for p in result.argument.premises)
    groups.append(result.argument.conclusion.provenance)
    groups.append((result.provenance,))
    assert all(span.revision == "rev-7" for group in groups for span in group)


def test_structured_input_is_accepted_and_formalization_is_directly_consumable():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-8")
    structured = StructuredDocument(document_id="doc", revision="rev-8", bytes_hash="a" * 64,
                                    spans=(source,), blocks=(text,), run_id="test-run")
    result = extract_argument(structured)
    assert result.status == "ACCEPTED"
    assert result.formalization.expression == "it rains -> the ground is wet"
    assert validate(result.argument, result.formalization).validation_status.value == "VALID"


@pytest.mark.parametrize("bad", [None, 123, "bad\ud800"])
def test_malformed_source_abstains_fail_closed(bad):
    result = extract_argument(bad, source_id="source", source_revision="rev-1", run_id="test-run")
    assert result.status == "ABSTAINED"
    assert result.argument is None
    assert result.abstention_reason == "malformed_source"


def test_oversized_source_abstains_fail_closed():
    result = extract_argument("x" * 1_000_001, source_id="source", source_revision="rev-1", run_id="test-run")
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_source"


def test_propositions_have_exact_substring_spans_and_bundle_is_canonical():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    result = extract_argument(text, source_id="source", source_revision="rev-11", run_id="test-run")
    assert result.record_id
    assert result.schema_version
    assert result.run_id == "test-run"
    for proposition in (*result.argument.premises, result.argument.conclusion):
        span = proposition.provenance[0]
        assert text[span.start:span.end] == span.text
        assert span.text != text
        assert span.revision == "rev-11"


def test_structured_extraction_scans_all_blocks_in_order():
    first = "Background only."
    second = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    text = first + "\\n\\n" + second
    spans = (EvidenceSpan("source", 0, len(text), text, revision="rev-12"),
             EvidenceSpan("source", len(first) + 2, len(first) + 2 + len(second), second, revision="rev-12"))
    document = StructuredDocument(document_id="doc", revision="rev-12", bytes_hash="a" * 64,
                                  spans=spans, blocks=(first, second), run_id="test-run")
    taxonomy = TaxonomySnapshot(snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
                                run_id="test-run", provenance=(spans[0],))
    result = extract_structured_document(document, taxonomy)
    assert result.status == "ACCEPTED"
    assert result.provenance.start == spans[1].start
