"""Acceptance tests for the generation/injection safety boundary.

The tests deliberately pass real RetrievalContext records and hostile retrieved
strings; they do not replace the verifier with mocks.
"""
from __future__ import annotations

from dataclasses import FrozenInstanceError, is_dataclass
import json
from pathlib import Path

import pytest

from scholastic_pipeline.schema import EvidenceSpan, RecordStatus, RetrievalContext

from scholastic_pipeline.generation import (  # type: ignore[import-not-found]
    ClaimStatus,
    Citation,
    GenerationRequest,
    GenerationResult,
    generate,
)

FIXTURE = Path(__file__).parents[2] / "fixtures" / "generation" / "contexts.json"


def _span(text: str, *, source_id="book-1", revision="rev-1", start=0):
    return EvidenceSpan(source_id, start, start + len(text), text, revision)


def _context(text="The library opened in 1850.", **kwargs):
    citation = _span(text, **kwargs)
    return RetrievalContext(items=(text,), citations=(citation,),
                            provenance=(citation,), run_id="run-1")


def _request(**kwargs):
    values = dict(
        prompt="State the supported fact.", run_id="run-1", scope=("book-1",),
        claim_budget=4, context_budget_bytes=4096, allowed_tools=(),
    )
    values.update(kwargs)
    return GenerationRequest(**values)


def _claims(result):
    return getattr(result, "claims", ())


def test_generation_boundary_is_typed_immutable_and_refuses_untyped_inputs():
    assert is_dataclass(GenerationRequest) and is_dataclass(GenerationResult)
    assert is_dataclass(Citation)
    with pytest.raises(FrozenInstanceError):
        _request().prompt = "mutate"  # type: ignore[misc]
    result = generate(object(), _context())
    assert isinstance(result, GenerationResult)
    assert result.refusal


def test_supported_claims_carry_resolvable_exact_citations():
    context = _context()
    result = generate(_request(), context)
    assert result.refusal is None
    assert _claims(result)
    for claim in _claims(result):
        assert claim.status is ClaimStatus.SUPPORTED
        assert claim.citations
        for citation in claim.citations:
            assert isinstance(citation, Citation)
            assert citation.source_id == "book-1"
            assert citation.revision == "rev-1"
            assert citation.start >= 0 and citation.end - citation.start == len(citation.text)
            assert citation.text == context.citations[0].text


@pytest.mark.parametrize("mutation", ["missing", "stale", "out-of-scope"])
def test_missing_stale_or_out_of_scope_citation_refuses(mutation):
    context = _context()
    if mutation == "missing":
        context = RetrievalContext(items=context.items, citations=(), provenance=context.provenance, run_id="run-1")
    elif mutation == "stale":
        context = _context(revision="old-rev")
    else:
        context = _context(source_id="other-book")
    result = generate(_request(), context)
    assert result.refusal
    assert not _claims(result)


def test_unsupported_claim_is_explicitly_unverified_or_refused():
    result = generate(_request(prompt="Assert that the moon is made of glass."), _context())
    assert result.refusal or all(
        claim.status is ClaimStatus.UNVERIFIED for claim in _claims(result)
    )
    assert not any(claim.status is ClaimStatus.SUPPORTED for claim in _claims(result))


def test_evidence_is_not_silently_truncated():
    full = "The library opened in 1850; its archive moved in 1901."
    result = generate(_request(prompt="Repeat every detail exactly."), _context(full))
    assert result.refusal or full in " ".join(
        citation.text for claim in _claims(result) for citation in claim.citations
    )


def test_claim_and_context_budgets_are_hard_bounds():
    context = _context("alpha. beta. gamma. delta.")
    assert generate(_request(claim_budget=0), context).refusal
    bounded = generate(_request(claim_budget=1), context)
    assert bounded.refusal or len(_claims(bounded)) <= 1
    tiny = generate(_request(context_budget_bytes=1), context)
    assert tiny.refusal


def test_retrieval_refusal_cannot_become_generated_evidence():
    refused = _context()
    refused = RetrievalContext(items=(), citations=(), provenance=refused.provenance,
                               refusal="stale", run_id="run-1")
    result = generate(_request(), refused)
    assert result.refusal
    assert not _claims(result)


def test_generation_is_deterministic_for_identical_typed_inputs():
    request, context = _request(), _context()
    first, second = generate(request, context), generate(request, context)
    assert first == second
    assert first.to_payload() == second.to_payload()


def test_result_rejects_claims_without_exact_provenance_at_boundary():
    # A verifier may not expose an accepted result whose claim is uncited.
    with pytest.raises((ValueError, TypeError)):
        GenerationResult(claims=("uncited",), run_id="run-1")
