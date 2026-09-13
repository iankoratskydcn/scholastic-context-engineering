"""Deterministic canary extraction with revision-safe evidence.

The extraction representation is deliberately formal-ready: premise zero is the
normalized implication (``A -> B``), premise one is A (or ¬B), and conclusion is
B (or ¬A). Each proposition retains source-document provenance; callers pass the
bundle's Formalization directly to ``formal.validate`` without reconstruction.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import re
from typing import Any

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, Proposition, StructuredDocument, TaxonomyMatch, TaxonomySnapshot

MAX_SOURCE_CHARS = 1_000_000
_DIAGNOSTIC_RUN_ID = "diagnostic-run"
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
    run_id: str = ""
    uncertainty: tuple[str, ...] = ()
    diagnostics: tuple[str, ...] = ()
    schema_version: str = "0.1"
    producer: str = "scholastic-context-engineering"
    record_id: str = field(init=False)

    def __post_init__(self) -> None:
        if (not isinstance(self.run_id, str) or not self.run_id or
                any(0xD800 <= ord(char) <= 0xDFFF for char in self.run_id)):
            raise ValueError("run_id must be a non-empty string")
        if not isinstance(self.producer, str) or not self.producer:
            raise ValueError("producer must be a non-empty string")
        if self.schema_version != "0.1":
            raise ValueError("unsupported schema version")
        if self.status not in {"ACCEPTED", "ABSTAINED", "REJECTED", "QUARANTINED"}:
            raise ValueError("unknown extraction status")
        if not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        if self.provenance is None and self.status != "ABSTAINED":
            raise ValueError("extraction bundle requires provenance")
        if self.provenance is None:
            reason = self.abstention_reason or "abstained extraction"
            text = f"[diagnostic: {reason}; no source evidence]"
            object.__setattr__(self, "provenance", EvidenceSpan("diagnostic://extraction", 0, len(text), text, "diagnostic"))
        if self.provenance is not None and not isinstance(self.provenance, EvidenceSpan):
            raise ValueError("extraction provenance must be an evidence span")
        payload = self.to_payload()
        object.__setattr__(self, "record_id", "extraction-" + hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        ).hexdigest()[:24])

    def to_payload(self) -> dict[str, Any]:
        """Return the complete stable JSON-safe envelope and result payload."""
        def encode(value: Any) -> Any:
            if hasattr(value, "value") and not isinstance(value, (str, bytes)):
                return value.value
            if hasattr(value, "to_payload"):
                return value.to_payload()
            if hasattr(value, "__dataclass_fields__"):
                result = {name: encode(getattr(value, name))
                          for name in value.__dataclass_fields__ if name != "record_id"}
                if hasattr(value, "record_id"):
                    result["record_id"] = value.record_id
                return result
            if isinstance(value, tuple):
                return [encode(item) for item in value]
            if isinstance(value, list):
                return [encode(item) for item in value]
            if isinstance(value, dict):
                return {str(key): encode(item) for key, item in value.items()}
            return value
        payload = {"kind": "extraction_bundle", "status": self.status, "argument": encode(self.argument),
                "taxonomy": encode(self.taxonomy), "abstention_reason": self.abstention_reason,
                "confidence": self.confidence, "provenance": [encode(self.provenance)],
                "formalization": encode(self.formalization), "run_id": self.run_id,
                "uncertainty": encode(self.uncertainty), "diagnostics": encode(self.diagnostics),
                "schema_version": self.schema_version, "producer": self.producer}
        if hasattr(self, "record_id"):
            payload["record_id"] = self.record_id
        return payload


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


def _abstain(reason: str, run_id: str = "") -> ExtractionBundle:
    safe_run_id = run_id if isinstance(run_id, str) and run_id and not any(0xD800 <= ord(char) <= 0xDFFF for char in run_id) else _DIAGNOSTIC_RUN_ID
    return ExtractionBundle("ABSTAINED", None, None, reason, 0.0, None, run_id=safe_run_id)


def _structured_problem(document: StructuredDocument) -> str | None:
    try:
        if document.status != "ACCEPTED" or not isinstance(document.spans, tuple) or not document.spans:
            return "malformed_source"
        if not isinstance(document.blocks, tuple) or len(document.blocks) != len(document.spans):
            return "malformed_source"
        for block, span in zip(document.blocks, document.spans):
            if not isinstance(block, str) or any(0xD800 <= ord(char) <= 0xDFFF for char in block):
                return "malformed_source"
            if not isinstance(span, EvidenceSpan) or span.revision != document.revision:
                return "malformed_source"
            if not isinstance(span.text, str):
                return "malformed_source"
            if len(span.text.encode("utf-8")) > 65_536:
                return "malformed_source"
            if span.start < 0 or span.end < span.start or span.end - span.start != len(span.text):
                return "malformed_source"
    except (AttributeError, TypeError, UnicodeError):
        return "malformed_source"
    return None


def _provenance_problem(spans: object) -> str | None:
    try:
        if not isinstance(spans, tuple) or not spans:
            return "malformed_taxonomy_provenance"
        for span in spans:
            if not isinstance(span, EvidenceSpan):
                return "malformed_taxonomy_provenance"
            if not isinstance(span.source_id, str) or not span.source_id:
                return "malformed_taxonomy_provenance"
            if not isinstance(span.revision, str) or not span.revision:
                return "malformed_taxonomy_provenance"
            if not isinstance(span.text, str) or any(0xD800 <= ord(char) <= 0xDFFF for char in span.text):
                return "malformed_taxonomy_provenance"
            if len(span.text.encode("utf-8")) > 65_536:
                return "malformed_taxonomy_provenance"
    except (AttributeError, TypeError, UnicodeError):
        return "malformed_taxonomy_provenance"
    return None


def _input_text(source: object, source_id: str, source_revision: str | None, base_offset: int = 0) -> tuple[str, EvidenceSpan] | None:
    if isinstance(source, StructuredDocument):
        if _structured_problem(source):
            return None
        span = source.spans[0]
        return span.text, span
    if not isinstance(source, str) or not isinstance(source_id, str) or not source_id:
        return None
    if not isinstance(source_revision, str) or not source_revision:
        return None
    if len(source) > MAX_SOURCE_CHARS or any(0xD800 <= ord(char) <= 0xDFFF for char in source):
        return None
    try:
        if len(source.encode("utf-8")) > 65_536:
            return None
        return source, EvidenceSpan(source_id=source_id, start=base_offset, end=base_offset + len(source), text=source, revision=source_revision)
    except (TypeError, ValueError, UnicodeError):
        return None


def extract_argument(source: str | StructuredDocument, *, source_id: str = "source",
                     run_id: str = "run", source_revision: str | None = None, base_offset: int = 0) -> ExtractionBundle:
    """Extract one canary argument, abstaining on malformed or revisionless input."""
    if (not isinstance(run_id, str) or not run_id or
            any(0xD800 <= ord(char) <= 0xDFFF for char in run_id)):
        return _abstain("malformed_source", run_id)
    prepared = _input_text(source, source_id, source_revision, base_offset)
    if prepared is None:
        return _abstain("malformed_source", run_id)
    text, document_span = prepared
    conditional = _CONDITIONAL.search(text)
    if conditional is None:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span,
                                run_id=run_id)
    offset = document_span.start
    a_start, a_end = _clean_span(text, conditional.start("antecedent"), conditional.end("antecedent"))
    b_start, b_end = _clean_span(text, conditional.start("consequent"), conditional.end("consequent"))
    tail_start = conditional.end()
    remainder = text[tail_start:]
    premise_match = re.match(r"\s*(?P<premise>[^.!?]+)\.", remainder)
    conclusion_match = re.match(r"\s*Therefore,\s*(?P<conclusion>[^.!?]+)\.",
                                 remainder[premise_match.end():] if premise_match else "", re.IGNORECASE)
    if not premise_match or not conclusion_match:
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span,
                                run_id=run_id)
    p_start = tail_start + premise_match.start("premise")
    p_end = tail_start + premise_match.end("premise")
    c_offset = tail_start + premise_match.end()
    c_start = c_offset + conclusion_match.start("conclusion")
    c_end = c_offset + conclusion_match.end("conclusion")
    c_start, c_end = _clean_span(text, c_start, c_end)
    antecedent, consequent = text[a_start:a_end], text[b_start:b_end]
    premise, conclusion = text[p_start:p_end], text[c_start:c_end]
    conditional_span = EvidenceSpan(document_span.source_id, offset + conditional.start(), offset + conditional.end(),
                                    text[conditional.start():conditional.end()], document_span.revision)
    premise_span = EvidenceSpan(document_span.source_id, offset + p_start, offset + p_end, premise, document_span.revision)
    conclusion_span = EvidenceSpan(document_span.source_id, offset + c_start, offset + c_end, conclusion, document_span.revision)
    is_mp = _same_polarity(antecedent, premise) and _same_polarity(consequent, conclusion) and not _negated_key(premise)[0]
    is_mt = _opposite_polarity(consequent, premise) and _opposite_polarity(antecedent, conclusion)
    if not (is_mp or is_mt):
        return ExtractionBundle("ABSTAINED", None, None, "unsupported_argument_form", 0.0, document_span,
                                run_id=run_id)
    a = _key(antecedent)
    b = _key(consequent)
    normalized = f"{a} -> {b}"
    second_text = a if is_mp else f"¬{b}"
    conclusion_text = b if is_mp else f"¬{a}"
    first = _proposition(normalized, "premise", run_id, conditional_span)
    second = _proposition(second_text, "premise", run_id, premise_span)
    conclusion_prop = _proposition(conclusion_text, "conclusion", run_id, conclusion_span)
    argument = ArgumentUnit(argument_id="arg-" + hashlib.sha256(document_span.record_id.encode()).hexdigest()[:24],
                            premises=(first, second), conclusion=conclusion_prop, relation="entails",
                            provenance=(document_span,), run_id=run_id, confidence=1.0)
    taxonomy_id, label = (_MP_ID, "Modus ponens") if is_mp else (_MT_ID, "Modus tollens")
    taxonomy = TaxonomyMatch(taxonomy_id=taxonomy_id, label=label, provenance=(document_span,), run_id=run_id, confidence=1.0)
    from scholastic_pipeline.formal import Formalization
    formalization = Formalization(normalized, provenance=(document_span,), run_id=run_id)
    return ExtractionBundle("ACCEPTED", argument, taxonomy, None, 1.0, document_span,
                            formalization, run_id=run_id)


def extract_structured_document(document: StructuredDocument, taxonomy_snapshot: TaxonomySnapshot) -> ExtractionBundle:
    """Production extraction port: typed document plus explicit taxonomy authority."""
    if not isinstance(document, StructuredDocument):
        raise TypeError("extraction requires StructuredDocument")
    if not isinstance(taxonomy_snapshot, TaxonomySnapshot):
        raise TypeError("extraction requires TaxonomySnapshot")
    if taxonomy_snapshot.run_id and taxonomy_snapshot.run_id != document.run_id:
        return _abstain("malformed_taxonomy_provenance", document.run_id)
    if (problem := _structured_problem(document)):
        return _abstain(problem, document.run_id)
    if (problem := _provenance_problem(taxonomy_snapshot.provenance)):
        return ExtractionBundle("ABSTAINED", None, None, problem, 0.0,
                                document.spans[0], run_id=document.run_id)
    try:
        taxonomy_scope = {span.record_id for span in taxonomy_snapshot.provenance}
        document_scope = {span.record_id for span in document.spans}
        if not taxonomy_scope <= document_scope:
            return ExtractionBundle("ABSTAINED", None, None, "malformed_taxonomy_provenance", 0.0,
                                    document.spans[0], run_id=document.run_id)
    except (AttributeError, TypeError, UnicodeError):
        return _abstain("malformed_taxonomy_provenance", document.run_id)
    unsupported_taxonomy = False
    for block, span in zip(document.blocks, document.spans):
        result = extract_argument(block, source_id=span.source_id, run_id=document.run_id,
                                  source_revision=document.revision, base_offset=span.start)
        if result.status != "ACCEPTED":
            continue
        if result.taxonomy is None or result.taxonomy.taxonomy_id not in taxonomy_snapshot.supported_taxonomy_ids:
            unsupported_taxonomy = True
            continue
        return result
    return ExtractionBundle("ABSTAINED", None, None,
                            "unsupported_taxonomy" if unsupported_taxonomy else "unsupported_argument_form", 0.0,
                            document.spans[0], run_id=document.run_id,
                            diagnostics=("all structured blocks scanned in source order",))


extract = extract_structured_document
__all__ = ["ExtractionBundle", "MAX_SOURCE_CHARS", "extract", "extract_argument", "extract_structured_document"]
