"""Deterministic canary argument extraction.

This lane recognizes only the two explicitly supported conditional forms. It
extracts text spans; it does not establish formal validity.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, Proposition, TaxonomyMatch


_MP_ID = "src.core_initial_pass.003.l9"
_MT_ID = "src.core_initial_pass.004.l10"


@dataclass(frozen=True)
class ExtractionBundle:
    status: str
    argument: ArgumentUnit | None
    taxonomy: TaxonomyMatch | None
    abstention_reason: str | None
    confidence: float
    provenance: EvidenceSpan


_SENTENCE = re.compile(r"[^.!?]+(?:[.!?]|$)")
_CONDITIONAL = re.compile(
    r"If\s+(?P<antecedent>[^,.!?]+),\s+(?P<consequent>[^.!?]+)\.", re.IGNORECASE
)


def _span(source_id: str, text: str, start: int, end: int, revision: str = "") -> EvidenceSpan:
    value = text[start:end]
    return EvidenceSpan(source_id=source_id, start=start, end=end, text=value, revision=revision)


def _clean_span(text: str, start: int, end: int) -> tuple[int, int]:
    while start < end and text[start].isspace():
        start += 1
    while end > start and text[end - 1].isspace():
        end -= 1
    return start, end


def _key(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def _negated_key(text: str) -> tuple[bool, str]:
    value = _key(text)
    replacements = (
        (" is not ", " is "), (" are not ", " are "),
        (" was not ", " was "), (" were not ", " were "),
        (" does not ", " does "), (" do not ", " do "),
        (" did not ", " did "), ("not ", ""),
    )
    for marker, replacement in replacements:
        if marker in value:
            return True, value.replace(marker, replacement, 1)
    return False, value


def _same_polarity(left: str, right: str) -> bool:
    left_negated, left_base = _negated_key(left)
    right_negated, right_base = _negated_key(right)
    return left_negated == right_negated and left_base == right_base


def _opposite_polarity(left: str, right: str) -> bool:
    left_negated, left_base = _negated_key(left)
    right_negated, right_base = _negated_key(right)
    return left_negated != right_negated and left_base == right_base


def _proposition(source_id: str, text: str, start: int, end: int, role: str, run_id: str) -> Proposition:
    evidence = _span(source_id, text, start, end)
    proposition_id = "prop-" + hashlib.sha256(evidence.record_id.encode()).hexdigest()[:24]
    return Proposition(
        proposition_id=proposition_id,
        text=evidence.text,
        role=role,
        provenance=(evidence,),
        run_id=run_id,
        confidence=1.0,
    )


def extract_argument(text: str, *, source_id: str = "source", run_id: str = "run") -> ExtractionBundle:
    """Extract one canary argument, or abstain without guessing."""
    document_span = EvidenceSpan(source_id=source_id, start=0, end=len(text), text=text)
    conditional = _CONDITIONAL.search(text)
    if conditional is None:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)

    antecedent_start, antecedent_end = _clean_span(text, conditional.start("antecedent"), conditional.end("antecedent"))
    consequent_start, consequent_end = _clean_span(text, conditional.start("consequent"), conditional.end("consequent"))
    tail_start = conditional.end()
    remainder = text[tail_start:]
    premise_match = re.match(r"\s*(?P<premise>[^.!?]+)\.", remainder)
    conclusion_match = re.match(r"\s*Therefore,\s*(?P<conclusion>[^.!?]+)\.", remainder[premise_match.end():] if premise_match else "", re.IGNORECASE)
    if not premise_match or not conclusion_match:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)

    premise_start = tail_start + premise_match.start("premise")
    premise_end = tail_start + premise_match.end("premise")
    conclusion_offset = tail_start + premise_match.end()
    conclusion_start = conclusion_offset + conclusion_match.start("conclusion")
    conclusion_end = conclusion_offset + conclusion_match.end("conclusion")
    conclusion_start, conclusion_end = _clean_span(text, conclusion_start, conclusion_end)

    antecedent = text[antecedent_start:antecedent_end]
    consequent = text[consequent_start:consequent_end]
    premise = text[premise_start:premise_end]
    conclusion = text[conclusion_start:conclusion_end]

    is_mp = _same_polarity(antecedent, premise) and _same_polarity(consequent, conclusion) and not _negated_key(premise)[0]
    is_mt = _opposite_polarity(consequent, premise) and _opposite_polarity(antecedent, conclusion)
    if not (is_mp or is_mt):
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)

    if is_mp:
        premise_one = _proposition(source_id, text, antecedent_start, antecedent_end, "premise", run_id)
        taxonomy_id, label = _MP_ID, "Modus ponens"
    else:
        premise_one = _proposition(source_id, text, antecedent_start, antecedent_end, "premise", run_id)
        taxonomy_id, label = _MT_ID, "Modus tollens"
    premise_two = _proposition(source_id, text, premise_start, premise_end, "premise", run_id)
    conclusion_prop = _proposition(source_id, text, conclusion_start, conclusion_end, "conclusion", run_id)
    argument = ArgumentUnit(
        argument_id="arg-" + hashlib.sha256(document_span.record_id.encode()).hexdigest()[:24],
        premises=(premise_one, premise_two),
        conclusion=conclusion_prop,
        relation="entails",
        provenance=(document_span,),
        run_id=run_id,
        confidence=1.0,
    )
    taxonomy = TaxonomyMatch(
        taxonomy_id=taxonomy_id,
        label=label,
        provenance=(document_span,),
        run_id=run_id,
        confidence=1.0,
    )
    return ExtractionBundle("ACCEPTED", argument, taxonomy, None, 1.0, document_span)


extract = extract_argument

__all__ = ["ExtractionBundle", "extract", "extract_argument"]
