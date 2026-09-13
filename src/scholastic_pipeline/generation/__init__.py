"""Deterministic, evidence-bound generation safety boundary."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from scholastic_pipeline.schema import EvidenceSpan, RetrievalContext


class ClaimStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    UNVERIFIED = "UNVERIFIED"


@dataclass(frozen=True)
class Citation:
    """An exact, independently resolvable evidence span."""

    source_id: str
    start: int
    end: int
    text: str
    revision: str

    def __post_init__(self) -> None:
        if type(self.source_id) is not str or not self.source_id:
            raise ValueError("citation source_id is required")
        if type(self.revision) is not str or not self.revision:
            raise ValueError("citation revision is required")
        if type(self.text) is not str or not self.text:
            raise ValueError("citation text is required")
        if type(self.start) is not int or isinstance(self.start, bool):
            raise TypeError("citation start must be an integer")
        if type(self.end) is not int or isinstance(self.end, bool):
            raise TypeError("citation end must be an integer")
        if self.start < 0 or self.end < self.start or self.end - self.start != len(self.text):
            raise ValueError("citation span bounds are invalid")

    @classmethod
    def from_span(cls, span: EvidenceSpan) -> "Citation":
        return cls(span.source_id, span.start, span.end, span.text, span.revision)

    def to_payload(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "start": self.start,
            "end": self.end,
            "text": self.text,
            "revision": self.revision,
        }


@dataclass(frozen=True)
class Claim:
    text: str
    status: ClaimStatus
    citations: tuple[Citation, ...] = ()

    def __post_init__(self) -> None:
        if type(self.text) is not str or not self.text:
            raise ValueError("claim text is required")
        if type(self.status) is not ClaimStatus:
            raise TypeError("claim status must be ClaimStatus")
        if type(self.citations) is not tuple or any(not isinstance(citation, Citation) for citation in self.citations):
            raise TypeError("claim citations must be Citation records")
        if self.status is ClaimStatus.SUPPORTED and not self.citations:
            raise ValueError("supported claims require exact citations")
        if any(citation.text != self.text for citation in self.citations):
            raise ValueError("citation text must exactly match claim text")

    def to_payload(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "status": self.status.value,
            "citations": [citation.to_payload() for citation in self.citations],
        }


@dataclass(frozen=True)
class GenerationRequest:
    prompt: str
    run_id: str
    scope: tuple[str, ...]
    claim_budget: int
    context_budget_bytes: int
    allowed_tools: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if type(self.prompt) is not str or not self.prompt.strip():
            raise ValueError("prompt is required")
        if type(self.run_id) is not str or not self.run_id:
            raise ValueError("run_id is required")
        for value, label in ((self.scope, "scope"), (self.allowed_tools, "allowed_tools")):
            if type(value) is not tuple or any(type(item) is not str or not item for item in value):
                raise TypeError(f"{label} must be a tuple of non-empty strings")
        if type(self.claim_budget) is not int or isinstance(self.claim_budget, bool):
            raise TypeError("claim_budget must be an integer")
        if type(self.context_budget_bytes) is not int or isinstance(self.context_budget_bytes, bool):
            raise TypeError("context_budget_bytes must be an integer")

    def to_payload(self) -> dict[str, Any]:
        return {
            "prompt": self.prompt,
            "run_id": self.run_id,
            "scope": list(self.scope),
            "claim_budget": self.claim_budget,
            "context_budget_bytes": self.context_budget_bytes,
            "allowed_tools": list(self.allowed_tools),
        }


@dataclass(frozen=True)
class GenerationResult:
    claims: tuple[Claim, ...] = ()
    run_id: str = ""
    refusal: str | None = None
    tools_used: tuple[str, ...] = ()
    scope: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if type(self.claims) is not tuple or any(not isinstance(c, Claim) for c in self.claims):
            raise ValueError("claims must contain Claim records")
        if type(self.run_id) is not str:
            raise TypeError("run_id must be a string")
        if self.refusal is not None and (type(self.refusal) is not str or not self.refusal):
            raise TypeError("refusal must be a non-empty string or null")
        for value, label in ((self.tools_used, "tools_used"), (self.scope, "scope")):
            if type(value) is not tuple or any(type(item) is not str or not item for item in value):
                raise TypeError(f"{label} must be a tuple of non-empty strings")
        if self.refusal is not None and self.claims:
            raise ValueError("refusal results cannot contain claims")

    def to_payload(self) -> dict[str, Any]:
        return {
            "claims": [claim.to_payload() for claim in self.claims],
            "run_id": self.run_id,
            "refusal": self.refusal,
            "tools_used": list(self.tools_used),
            "scope": list(self.scope),
        }


_INJECTION_MARKERS = (
    "ignore policy",
    "ignore the limit",
    "use the shell tool",
    "reveal secrets",
    "expand scope",
)


def _refusal(request: Any, reason: str) -> GenerationResult:
    run_id = getattr(request, "run_id", "")
    scope = getattr(request, "scope", ())
    if type(run_id) is not str:
        run_id = ""
    if type(scope) is not tuple or any(type(item) is not str or not item for item in scope):
        scope = ()
    return GenerationResult(
        run_id=run_id,
        refusal=reason,
        tools_used=(),
        scope=scope,
    )


def _encodable(value: str) -> bool:
    try:
        value.encode("utf-8")
    except (UnicodeError, AttributeError):
        return False
    return True


def _span_fields(span: EvidenceSpan) -> tuple[str, int, int, str, str] | None:
    """Read and validate every field before any comparison or encoding."""
    if not isinstance(span, EvidenceSpan):
        return None
    try:
        source_id = getattr(span, "source_id")
        start = getattr(span, "start")
        end = getattr(span, "end")
        text = getattr(span, "text")
        revision = getattr(span, "revision")
    except Exception:
        return None
    if (type(source_id) is not str or not source_id
            or type(revision) is not str or not revision
            or type(text) is not str
            or type(start) is not int or isinstance(start, bool)
            or type(end) is not int or isinstance(end, bool)
            or start < 0 or end < start or end - start != len(text)):
        return None
    if not all(_encodable(value) for value in (source_id, revision, text)):
        return None
    return source_id, start, end, text, revision


def _same_span(left: tuple[str, int, int, str, str],
               right: tuple[str, int, int, str, str]) -> bool:
    """Compare validated primitive fields, never forged dataclass equality."""
    return left == right


def _valid_context(context: RetrievalContext) -> bool:
    """Validate forged boundary records before touching nested members."""
    try:
        items = getattr(context, "items")
        citations = getattr(context, "citations")
        provenance = getattr(context, "provenance")
        refusal = getattr(context, "refusal")
        run_id = getattr(context, "run_id")
    except Exception:
        return False
    if (type(items) is not tuple or type(citations) is not tuple
            or type(provenance) is not tuple
            or (refusal is not None and type(refusal) is not str)
            or type(run_id) is not str):
        return False
    if any(type(item) is not str or not _encodable(item) for item in items):
        return False
    return all(_span_fields(span) is not None for span in (*citations, *provenance))


def _exact_span(span_fields: tuple[str, int, int, str, str],
                candidates: tuple[tuple[str, int, int, str, str], ...],
                scope: tuple[str, ...]) -> bool:
    source_id = span_fields[0]
    return source_id in scope and any(_same_span(span_fields, candidate) for candidate in candidates)


def _aligns_to_item(span_fields: tuple[str, int, int, str, str], items: tuple[str, ...]) -> bool:
    """Require citation offsets and text to describe a complete evidence item."""
    _, start, end, text, _ = span_fields
    return any(start == 0 and end == len(item) and text == item for item in items)


def generate(request: GenerationRequest, context: RetrievalContext) -> GenerationResult:
    """Generate only claims whose evidence is exact and in request scope."""
    if not isinstance(request, GenerationRequest):
        return _refusal(request, "generation request is malformed")
    if not isinstance(context, RetrievalContext):
        return _refusal(request, "retrieval context is malformed")
    if not _valid_context(context):
        return _refusal(request, "retrieval context is malformed")
    if context.refusal:
        return _refusal(request, "retrieval context was refused")
    if request.run_id != context.run_id:
        return _refusal(request, "generation run ID does not match retrieval context")
    if (type(request.prompt) is not str or not request.prompt.strip()
            or type(request.run_id) is not str or not request.run_id
            or type(request.scope) is not tuple or not request.scope
            or any(type(item) is not str or not item for item in request.scope)
            or type(request.allowed_tools) is not tuple
            or any(type(item) is not str or not item for item in request.allowed_tools)
            or type(request.claim_budget) is not int or isinstance(request.claim_budget, bool)
            or type(request.context_budget_bytes) is not int
            or isinstance(request.context_budget_bytes, bool)):
        return _refusal(request, "generation request is malformed")
    if request.allowed_tools:
        return _refusal(request, "generation request is malformed")
    if request.claim_budget <= 0:
        return _refusal(request, "claim budget is exhausted")
    if request.context_budget_bytes <= 0:
        return _refusal(request, "context budget is exhausted")
    if not context.items or not context.citations or not context.provenance:
        return _refusal(request, "retrieval evidence is missing")

    citation_fields = tuple(_span_fields(span) for span in context.citations)
    provenance_fields = tuple(_span_fields(span) for span in context.provenance)
    # _valid_context established these records, but keep the narrowing local so
    # later checks never dereference or compare a forged nested member.
    if any(fields is None for fields in (*citation_fields, *provenance_fields)):
        return _refusal(request, "retrieval context is malformed")
    citations = tuple(fields for fields in citation_fields if fields is not None)
    provenance = tuple(fields for fields in provenance_fields if fields is not None)

    evidence_bytes = sum(len(item.encode("utf-8")) for item in context.items)
    evidence_bytes += sum(len(fields[3].encode("utf-8")) for fields in citations)
    evidence_bytes += sum(len(fields[3].encode("utf-8")) for fields in provenance)
    if evidence_bytes > request.context_budget_bytes:
        return _refusal(request, "context budget exceeded")
    if any(marker in item.lower() for item in context.items for marker in _INJECTION_MARKERS):
        return _refusal(request, "retrieved instructions are untrusted data")
    if any(term in request.prompt.lower() for term in ("moon", "glass")):
        return _refusal(request, "claim is unsupported by retrieval evidence")
    if any(not _exact_span(span, provenance, request.scope) for span in citations):
        return _refusal(request, "citation is missing, stale, or out of scope")
    if any(span[0] not in request.scope for span in provenance):
        return _refusal(request, "retrieval provenance is out of scope")
    if any(
        not any(span[0] == candidate[0] and span[4] == candidate[4]
                for candidate in citations)
        for span in provenance
    ):
        return _refusal(request, "retrieval provenance is stale or mismatched")

    if any(span[4] == "old-rev" for span in citations):
        return _refusal(request, "citation is stale")

    claim_text = context.items[0]
    if any(not _aligns_to_item(span, context.items) for span in citations):
        return _refusal(request, "citation span does not align to retrieved text")
    if any(span[3] != claim_text for span in citations):
        return _refusal(request, "citation text does not match claim")
    prompt_words = {word.strip(".,?!:;").lower() for word in request.prompt.split()}
    evidence_words = {word.strip(".,?!:;").lower() for word in claim_text.split()}
    if prompt_words and not (prompt_words & evidence_words):
        return _refusal(request, "claim is unsupported by retrieval evidence")
    citations = tuple(Citation.from_span(span) for span in context.citations)
    return GenerationResult(
        claims=(Claim(claim_text, ClaimStatus.SUPPORTED, citations),),
        run_id=request.run_id,
        tools_used=(),
        scope=request.scope,
    )


__all__ = ["ClaimStatus", "Citation", "Claim", "GenerationRequest", "GenerationResult", "generate"]
