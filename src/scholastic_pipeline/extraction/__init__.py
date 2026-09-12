"""Deterministic canary extraction with revision-safe evidence.

The extraction representation is deliberately formal-ready: premise zero is the
normalized implication (``A -> B``), premise one is A (or ¬B), and conclusion is
B (or ¬A). Each proposition retains source-document provenance; callers pass the
bundle's Formalization directly to ``formal.validate`` without reconstruction.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re
from typing import Any

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, Proposition, StructuredDocument, TaxonomyMatch

MAX_SOURCE_CHARS = 1_000_000
_MP_ID = "src.core_initial_pass.003.l9"
_MT_ID = "src.core_initial_pass.004.l10"


@dataclass(frozen=True)
class ExtractionBundle:
    status: str
    argument: ArgumentUnit | None
    taxonomy: TaxonomyMatch | None
    abstention_reason: str | None
    confidence: float
    provenance: EvidenceSpan | None
    formalization: Any = None


_CONDITIONAL = re.compile(
    r"If\s+(?P<antecedent>[^,.!?]+),\s+(?P<consequent>[^.!?]+)\.", re.IGNORECASE
)


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
    for marker, replacement in ((" is not ", " is "), (" are not ", " are "),
                                (" was not ", " was "), (" were not ", " were "),
                                (" does not ", " does "), (" do not ", " do "),
                                (" did not ", " did "), ("not ", "")):
        if marker in value:
            return True, value.replace(marker, replacement, 1)
    return False, value


def _same_polarity(left: str, right: str) -> bool:
    a, b = _negated_key(left), _negated_key(right)
    return a == b


def _opposite_polarity(left: str, right: str) -> bool:
    a, b = _negated_key(left), _negated_key(right)
    return a[0] != b[0] and a[1] == b[1]


def _proposition(text: str, role: str, run_id: str, evidence: EvidenceSpan) -> Proposition:
    proposition_id = "prop-" + hashlib.sha256((evidence.record_id + "\0" + text + "\0" + role).encode()).hexdigest()[:24]
    return Proposition(proposition_id=proposition_id, text=text, role=role,
                       provenance=(evidence,), run_id=run_id, confidence=1.0)


def _abstain(reason: str) -> ExtractionBundle:
    return ExtractionBundle("ABSTAINED", None, None, reason, 0.0, None)


def _input_text(source: object, source_id: str, source_revision: str | None) -> tuple[str, EvidenceSpan] | None:
    if isinstance(source, StructuredDocument):
        if not source.spans or any(span.revision != source.revision for span in source.spans):
            return None
        span = source.spans[0]
        return span.text, EvidenceSpan(source_id=span.source_id, start=span.start, end=span.end,
                                       text=span.text, revision=source.revision)
    if not isinstance(source, str) or not isinstance(source_id, str) or not source_id:
        return None
    if not isinstance(source_revision, str) or not source_revision:
        return None
    if len(source) > MAX_SOURCE_CHARS or any(0xD800 <= ord(char) <= 0xDFFF for char in source):
        return None
    return source, EvidenceSpan(source_id=source_id, start=0, end=len(source), text=source, revision=source_revision)


def extract_argument(source: str | StructuredDocument, *, source_id: str = "source",
                     run_id: str = "run", source_revision: str | None = None) -> ExtractionBundle:
    """Extract one canary argument, abstaining on malformed or revisionless input."""
    if not isinstance(run_id, str) or not run_id:
        return _abstain("malformed_source")
    prepared = _input_text(source, source_id, source_revision)
    if prepared is None:
        return _abstain("malformed_source")
    text, document_span = prepared
    conditional = _CONDITIONAL.search(text)
    if conditional is None:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)
    a_start, a_end = _clean_span(text, conditional.start("antecedent"), conditional.end("antecedent"))
    b_start, b_end = _clean_span(text, conditional.start("consequent"), conditional.end("consequent"))
    tail_start = conditional.end()
    remainder = text[tail_start:]
    premise_match = re.match(r"\s*(?P<premise>[^.!?]+)\.", remainder)
    conclusion_match = re.match(r"\s*Therefore,\s*(?P<conclusion>[^.!?]+)\.",
                                 remainder[premise_match.end():] if premise_match else "", re.IGNORECASE)
    if not premise_match or not conclusion_match:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)
    p_start = tail_start + premise_match.start("premise")
    p_end = tail_start + premise_match.end("premise")
    c_offset = tail_start + premise_match.end()
    c_start = c_offset + conclusion_match.start("conclusion")
    c_end = c_offset + conclusion_match.end("conclusion")
    c_start, c_end = _clean_span(text, c_start, c_end)
    antecedent, consequent = text[a_start:a_end], text[b_start:b_end]
    premise, conclusion = text[p_start:p_end], text[c_start:c_end]
    is_mp = _same_polarity(antecedent, premise) and _same_polarity(consequent, conclusion) and not _negated_key(premise)[0]
    is_mt = _opposite_polarity(consequent, premise) and _opposite_polarity(antecedent, conclusion)
    if not (is_mp or is_mt):
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span)
    a = _key(antecedent)
    b = _key(consequent)
    normalized = f"{a} -> {b}"
    second_text = a if is_mp else f"¬{b}"
    conclusion_text = b if is_mp else f"¬{a}"
    first = _proposition(normalized, "premise", run_id, document_span)
    second = _proposition(second_text, "premise", run_id, document_span)
    conclusion_prop = _proposition(conclusion_text, "conclusion", run_id, document_span)
    argument = ArgumentUnit(argument_id="arg-" + hashlib.sha256(document_span.record_id.encode()).hexdigest()[:24],
                            premises=(first, second), conclusion=conclusion_prop, relation="entails",
                            provenance=(document_span,), run_id=run_id, confidence=1.0)
    taxonomy_id, label = (_MP_ID, "Modus ponens") if is_mp else (_MT_ID, "Modus tollens")
    taxonomy = TaxonomyMatch(taxonomy_id=taxonomy_id, label=label, provenance=(document_span,), run_id=run_id, confidence=1.0)
    from scholastic_pipeline.formal import Formalization
    formalization = Formalization(normalized, provenance=(document_span,))
    return ExtractionBundle("ACCEPTED", argument, taxonomy, None, 1.0, document_span, formalization)


extract = extract_argument
__all__ = ["ExtractionBundle", "MAX_SOURCE_CHARS", "extract", "extract_argument"]
