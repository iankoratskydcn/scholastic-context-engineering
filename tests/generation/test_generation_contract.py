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
    Claim,
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


def _malformed_context(*, items, citations, provenance):
    """Make a boundary-shaped record without constructor normalization."""
    context = object.__new__(RetrievalContext)
    for name, value in {
        "items": items,
        "citations": citations,
        "provenance": provenance,
        "refusal": None,
        "run_id": "run-1",
    }.items():
        object.__setattr__(context, name, value)
    return context


def _forged_span(**values):
    """Forge a boundary-shaped span to exercise nested validation."""
    span = object.__new__(EvidenceSpan)
    for name, value in values.items():
        object.__setattr__(span, name, value)
    return span


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


def test_unrelated_citation_refuses_instead_of_becoming_claim_provenance():
    context = _context()
    unrelated = _span("An unrelated claim.", source_id="book-1", start=100)
    context = RetrievalContext(items=context.items,
                               citations=(context.citations[0], unrelated),
                               provenance=(context.provenance[0],), run_id="run-1")

    result = generate(_request(), context)

    assert result.refusal == "citation is missing, stale, or out of scope"
    assert result.claims == ()


def test_extra_provenance_with_non_sentinel_revision_mismatch_refuses():
    context = _context()
    extra = _span(context.citations[0].text, source_id="book-1", revision="rev-2")
    context = RetrievalContext(
        items=context.items,
        citations=context.citations,
        provenance=(context.provenance[0], extra),
        run_id="run-1",
    )

    result = generate(_request(), context)

    assert result.refusal == "retrieval provenance is stale or mismatched"
    assert result.claims == ()


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
    assert result.refusal == "claim is unsupported by retrieval evidence"
    assert result.claims == ()


def test_evidence_is_not_silently_truncated():
    full = "The library opened in 1850; its archive moved in 1901."
    result = generate(_request(prompt="State the library archive details."), _context(full))
    assert result.refusal is None
    assert full in " ".join(
        citation.text for claim in _claims(result) for citation in claim.citations
    )


def test_misaligned_citation_offsets_refuse_even_when_text_matches_claim():
    text = "The library opened in 1850."
    misaligned = _span(text, start=1)
    context = RetrievalContext(
        items=(text,), citations=(misaligned,), provenance=(misaligned,), run_id="run-1"
    )

    result = generate(_request(), context)

    assert result.refusal == "citation span does not align to retrieved text"
    assert result.claims == ()


def test_multiple_supported_evidence_items_are_preserved_in_one_claim():
    text = "The library opened in 1850."
    first = _span(text, source_id="book-1")
    second = _span(text, source_id="book-2")
    context = RetrievalContext(
        items=(text, text),
        citations=(first, second),
        provenance=(first, second),
        run_id="run-1",
    )
    result = generate(_request(scope=("book-1", "book-2")), context)

    assert result.refusal is None
    assert len(result.claims) == 1
    assert result.claims[0].text == text
    assert len(result.claims[0].citations) == 2
    assert {citation.source_id for citation in result.claims[0].citations} == {
        "book-1", "book-2"
    }


def test_claim_and_context_budgets_are_hard_bounds():
    context = _context("The library supports alpha facts.")
    assert generate(_request(claim_budget=0), context).refusal
    bounded = generate(_request(claim_budget=1), context)
    assert bounded.refusal is None
    assert len(_claims(bounded)) == 1
    tiny = generate(_request(context_budget_bytes=1), context)
    assert tiny.refusal


def test_nonempty_allowed_tools_are_rejected_at_generation_boundary():
    result = generate(_request(allowed_tools=("shell",)), _context())

    assert result.refusal == "generation request is malformed"
    assert result.claims == ()
    assert result.tools_used == ()


def test_provenance_text_bytes_count_toward_context_budget():
    context = _context("The library opened in 1850.")
    provenance = _span("P" * 200, source_id="book-1")
    context = RetrievalContext(items=context.items, citations=context.citations,
                               provenance=(provenance,), run_id="run-1")
    item_and_citation_bytes = sum(len(value.text.encode("utf-8"))
                                  for value in context.citations) + sum(
                                      len(item.encode("utf-8")) for item in context.items
                                  )

    result = generate(_request(context_budget_bytes=item_and_citation_bytes), context)

    assert result.refusal == "context budget exceeded"
    assert result.claims == ()


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


def test_unverified_claim_semantics_are_explicit_and_uncited():
    result = GenerationResult(
        claims=(Claim("not established", ClaimStatus.UNVERIFIED, ()),),
        run_id="run-1",
    )

    assert result.refusal is None
    assert len(result.claims) == 1
    assert result.claims[0].status is ClaimStatus.UNVERIFIED
    assert result.claims[0].citations == ()


def test_refusal_results_cannot_expose_claims():
    citation = Citation("book-1", 0, 5, "alpha", "rev-1")
    claim = Claim("alpha", ClaimStatus.SUPPORTED, (citation,))

    with pytest.raises(ValueError):
        GenerationResult(claims=(claim,), run_id="run-1", refusal="unsupported")


def test_nested_claims_and_citations_are_immutable():
    result = generate(_request(), _context())
    claim = result.claims[0]
    citation = claim.citations[0]

    with pytest.raises(FrozenInstanceError):
        claim.text = "changed"  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        citation.text = "changed"  # type: ignore[misc]
    with pytest.raises(TypeError):
        claim.citations[0] = citation  # type: ignore[index]


def test_claim_citations_require_a_typed_immutable_tuple():
    citation = Citation("book-1", 0, 5, "alpha", "rev-1")

    with pytest.raises(TypeError):
        Claim("alpha", ClaimStatus.SUPPORTED, [citation])  # type: ignore[arg-type]

    claim = Claim("alpha", ClaimStatus.SUPPORTED, (citation,))
    assert type(claim.citations) is tuple
    with pytest.raises(FrozenInstanceError):
        claim.citations = ()  # type: ignore[misc]


@pytest.mark.parametrize("field", ["items", "citations", "provenance"])
def test_malformed_context_members_refuse_without_exceptions(field):
    valid = _context()
    values = {
        "items": valid.items,
        "citations": valid.citations,
        "provenance": valid.provenance,
    }
    values[field] = (object(),)

    result = generate(_request(), _malformed_context(**values))

    assert result.refusal == "retrieval context is malformed"
    assert result.claims == ()


@pytest.mark.parametrize("member", ["citations", "provenance"])
def test_malformed_nested_span_members_refuse_without_exceptions(member):
    valid = _context()
    malformed = _forged_span(
        source_id="book-1",
        start=0,
        end=len(valid.citations[0].text),
        text=valid.citations[0].text,
        revision=object(),
    )
    values = {
        "items": valid.items,
        "citations": valid.citations,
        "provenance": valid.provenance,
    }
    values[member] = (malformed,)

    result = generate(_request(), _malformed_context(**values))

    assert result.refusal == "retrieval context is malformed"
    assert result.claims == ()
