"""Explicit bridges for incompatible stage contracts used by the canary."""
from dataclasses import replace

from scholastic_pipeline.extraction import ExtractionBundle, extract_argument
from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, Proposition, StructuredDocument


def _with_revision(span: EvidenceSpan, revision: str) -> EvidenceSpan:
    return replace(span, revision=revision)


def extract_structured_document(document: StructuredDocument) -> ExtractionBundle:
    """Adapt a structured document to extraction's text API without coercion."""
    if not isinstance(document, StructuredDocument):
        raise TypeError("canary extraction adapter requires StructuredDocument")
    source = document.spans[0]
    bundle = extract_argument(
        "\n\n".join(document.blocks),
        source_id=source.source_id,
        run_id=document.run_id,
    )
    argument = bundle.argument
    if argument is not None:
        conclusion = argument.conclusion
        if not isinstance(conclusion, Proposition):
            raise TypeError("extraction returned a non-proposition conclusion")
        argument = replace(
            argument,
            provenance=tuple(_with_revision(s, source.revision) for s in argument.provenance),
            premises=tuple(
                replace(p, provenance=tuple(_with_revision(s, source.revision) for s in p.provenance))
                for p in argument.premises
            ),
            conclusion=replace(
                conclusion,
                provenance=tuple(_with_revision(s, source.revision) for s in conclusion.provenance),
            ),
        )
    taxonomy = bundle.taxonomy
    if taxonomy is not None:
        taxonomy = replace(taxonomy, provenance=tuple(_with_revision(s, source.revision) for s in taxonomy.provenance))
    return replace(
        bundle,
        provenance=_with_revision(bundle.provenance, source.revision),
        argument=argument,
        taxonomy=taxonomy,
    )


def formal_argument(argument: ArgumentUnit, normalized_form: str) -> ArgumentUnit:
    """Translate extraction's antecedent-first premises for formal validation."""
    if len(argument.premises) != 2:
        raise TypeError("canary formal adapter requires exactly two premises")
    return replace(argument, premises=(replace(argument.premises[0], text=normalized_form), argument.premises[1]))
