import json
from pathlib import Path

import pytest

from scholastic_pipeline.extraction import ExtractionBundle, extract_argument, extract_structured_document
from scholastic_pipeline.formal import validate
from scholastic_pipeline.schema import EnvelopeError, EvidenceSpan, StructuredDocument, TaxonomySnapshot


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


def test_malformed_structured_span_abstains_without_constructing_evidence_span():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-13")
    document = StructuredDocument(document_id="doc", revision="rev-13", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="test-run")
    object.__setattr__(source, "text", object())
    result = extract_argument(document)
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_source"


def test_structured_block_span_cardinality_rejected_at_construction():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-14")
    with pytest.raises(EnvelopeError, match="cardinality"):
        StructuredDocument(document_id="doc", revision="rev-14", bytes_hash="a" * 64,
                           spans=(source,), blocks=(), run_id="test-run")


def test_taxonomy_provenance_scope_mismatch_abstains():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-15")
    taxonomy_source = EvidenceSpan("other-source", 0, 1, "T", revision="rev-15")
    document = StructuredDocument(document_id="doc", revision="rev-15", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="test-run")
    result = extract_structured_document(document, TaxonomySnapshot(
        snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
        run_id="test-run", provenance=(taxonomy_source,)))
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_taxonomy_provenance"


def test_taxonomy_run_mismatch_abstains_fail_closed():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-16")
    document = StructuredDocument(document_id="doc", revision="rev-16", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="test-run")
    result = extract_structured_document(document, TaxonomySnapshot(
        snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
        run_id="other-run", provenance=(source,)))
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_taxonomy_provenance"


def test_taxonomy_provenance_requires_exact_span_identity_not_just_scope():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-exact")
    same_scope_different_span = EvidenceSpan("source", 0, 1, "I", revision="rev-exact")
    document = StructuredDocument(document_id="doc", revision="rev-exact", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="run-exact")
    result = extract_structured_document(document, TaxonomySnapshot(
        snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
        run_id="run-exact", provenance=(same_scope_different_span,)))
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_taxonomy_provenance"


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


def test_canonical_bundle_and_formalization_expose_complete_stable_envelopes():
    result = extract_argument("If it rains, the ground is wet. It rains. Therefore, the ground is wet.",
                              source_id="source", source_revision="rev-envelope", run_id="run-envelope")
    assert result.to_payload()["schema_version"] == "0.1"
    assert result.to_payload()["producer"] == "scholastic-context-engineering"
    assert result.record_id
    assert result.formalization.record_id
    bundle_payload = json.loads(json.dumps(result.to_payload()))
    formal_payload = json.loads(json.dumps(result.formalization.to_payload()))
    required = {"producer", "run_id", "status", "confidence", "uncertainty", "diagnostics",
                "schema_version", "provenance", "record_id"}
    assert required <= bundle_payload.keys()
    assert required <= formal_payload.keys()
    assert bundle_payload["record_id"] == result.record_id
    assert formal_payload["record_id"] == result.formalization.record_id
    assert formal_payload["expression"] == "it rains -> the ground is wet"
    assert bundle_payload["argument"]["record_id"] == result.argument.record_id
    assert bundle_payload["provenance"]["record_id"] == result.provenance.record_id
    assert formal_payload["provenance"][0]["record_id"] == result.formalization.provenance[0].record_id


def test_structured_extraction_rejects_taxonomy_provenance_outside_document():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    source = EvidenceSpan("source", 0, len(text), text, revision="rev-tax")
    foreign = EvidenceSpan("foreign", 0, 1, "I", revision="rev-tax")
    document = StructuredDocument(document_id="doc", revision="rev-tax", bytes_hash="a" * 64,
                                  spans=(source,), blocks=(text,), run_id="run-tax")
    taxonomy = TaxonomySnapshot(snapshot_id="taxonomy", supported_taxonomy_ids=("src.core_initial_pass.003.l9",),
                                run_id="run-tax", provenance=(foreign,))
    result = extract_structured_document(document, taxonomy)
    assert result.status == "ABSTAINED"
    assert result.abstention_reason == "malformed_taxonomy_provenance"


def test_propositions_keep_exact_source_spans_and_stable_identity():
    text = "If it rains, the ground is wet. It rains. Therefore, the ground is wet."
    first = extract_argument(text, source_id="source", source_revision="rev-id", run_id="run-id")
    second = extract_argument(text, source_id="source", source_revision="rev-id", run_id="run-id")
    assert first.record_id == second.record_id
    assert [p.provenance[0].record_id for p in first.argument.premises] == [
        p.provenance[0].record_id for p in second.argument.premises]


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


def test_extraction_bundle_rejects_missing_run_id_instead_of_using_unknown():
    with pytest.raises(ValueError, match="run_id"):
        from scholastic_pipeline.extraction import ExtractionBundle
        ExtractionBundle("ABSTAINED", None, None, "unsupported", 0.0, None)


def test_extraction_bundle_does_not_infer_missing_run_id_from_nested_records():
    source = EvidenceSpan("source", 0, 1, "A", revision="rev-1")
    with pytest.raises(ValueError, match="run_id"):
        ExtractionBundle("ABSTAINED", None, None, "unsupported", 0.0, source,
                         formalization=type("FormalizationStub", (), {"run_id": "nested-run"})())


def test_malformed_run_id_abstains_fail_closed():
    with pytest.raises(ValueError, match="run_id"):
        extract_argument("Birds fly.", source_id="source", source_revision="rev-1", run_id="bad\ud800")
