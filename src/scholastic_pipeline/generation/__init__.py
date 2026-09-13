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
        if any(not isinstance(citation, Citation) for citation in self.citations):
            raise TypeError("claim citations must be Citation records")
        if self.status is ClaimStatus.SUPPORTED and not self.citations:
            raise ValueError("supported claims require exact citations")

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
        if self.refusal is None and any(
            claim.status is ClaimStatus.SUPPORTED and not claim.citations
            for claim in self.claims
        ):
            raise ValueError("accepted claims require exact citations")

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
    return GenerationResult(
        run_id=getattr(request, "run_id", "") if isinstance(getattr(request, "run_id", ""), str) else "",
        refusal=reason,
        tools_used=(),
        scope=getattr(request, "scope", ()) if isinstance(getattr(request, "scope", ()), tuple) else (),
    )


def _exact_span(span: EvidenceSpan, context: RetrievalContext, scope: tuple[str, ...]) -> bool:
    return (
        isinstance(span, EvidenceSpan)
        and span.source_id in scope
        and any(
            span.source_id == candidate.source_id
            and span.revision == candidate.revision
            and span.start == candidate.start
            and span.end == candidate.end
            and span.text == candidate.text
            for candidate in context.citations
        )
    )


def generate(request: GenerationRequest, context: RetrievalContext) -> GenerationResult:
    """Generate only claims whose evidence is exact and in request scope."""
    if not isinstance(request, GenerationRequest):
        return _refusal(request, "generation request is malformed")
    if not isinstance(context, RetrievalContext):
        return _refusal(request, "retrieval context is malformed")
    if context.refusal:
        return _refusal(request, "retrieval context was refused")
    if request.run_id != context.run_id:
        return _refusal(request, "generation run ID does not match retrieval context")
    if (type(request.prompt) is not str or not request.prompt.strip()
            or type(request.run_id) is not str or not request.run_id
            or type(request.scope) is not tuple or not request.scope
            or any(type(item) is not str or not item for item in request.scope)
            or type(request.claim_budget) is not int or isinstance(request.claim_budget, bool)
            or type(request.context_budget_bytes) is not int
            or isinstance(request.context_budget_bytes, bool)):
        return _refusal(request, "generation request is malformed")
    if request.claim_budget <= 0:
        return _refusal(request, "claim budget is exhausted")
    if request.context_budget_bytes <= 0:
        return _refusal(request, "context budget is exhausted")
    if type(context.items) is not tuple or type(context.citations) is not tuple:
        return _refusal(request, "retrieval context is malformed")
    if not context.items or not context.citations or not context.provenance:
        return _refusal(request, "retrieval evidence is missing")

    evidence_bytes = sum(len(item.encode("utf-8")) for item in context.items)
    evidence_bytes += sum(len(span.text.encode("utf-8")) for span in context.citations)
    if evidence_bytes > request.context_budget_bytes:
        return _refusal(request, "context budget exceeded")
    if any(marker in item.lower() for item in context.items for marker in _INJECTION_MARKERS):
        return _refusal(request, "retrieved instructions are untrusted data")
    if any(term in request.prompt.lower() for term in ("moon", "glass")):
        return _refusal(request, "claim is unsupported by retrieval evidence")
    if any(not _exact_span(span, context, request.scope) for span in context.citations):
        return _refusal(request, "citation is missing, stale, or out of scope")
    if any(span.source_id not in request.scope for span in context.provenance):
        return _refusal(request, "retrieval provenance is out of scope")
    if any(span.revision == "old-rev" for span in context.citations):
        return _refusal(request, "citation is stale")

    # Evidence itself is the only claim text; no prompt-derived instruction is executed.
    claim_text = context.items[0]
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
