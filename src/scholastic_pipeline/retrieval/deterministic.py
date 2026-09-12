"""Dependency-free deterministic retrieval over graph edge occurrences."""
from __future__ import annotations

import re
from collections.abc import Mapping

from scholastic_pipeline.schema import GraphSnapshot, RetrievalContext, RetrievalRequest


_TOKEN = re.compile(r"[\w]+", re.UNICODE)


def _tokens(text: str) -> set[str]:
    return {token.casefold() for token in _TOKEN.findall(text)}


def _refusal(request: RetrievalRequest, reason: str) -> RetrievalContext:
    return RetrievalContext(items=(), citations=(), refusal=reason,
                            provenance=request.provenance, run_id=request.run_id)


def retrieve(request: RetrievalRequest, snapshot: GraphSnapshot,
             current_revisions: Mapping[str, str] | None = None) -> RetrievalContext:
    """Return at most ``request.budget`` matching occurrences in stable order.

    Refusal is represented in the contract rather than silently returning partial
    or unverifiable context.
    """
    if request.budget <= 0:
        return _refusal(request, "retrieval budget must be positive")
    if not request.query.strip():
        return _refusal(request, "retrieval query is empty")
    if not request.provenance or not snapshot.provenance:
        return _refusal(request, "retrieval provenance is missing")

    revisions = current_revisions or {}
    for span in (*request.provenance, *snapshot.provenance):
        if not span.source_id or not span.revision:
            return _refusal(request, "retrieval provenance is incomplete")
        if revisions.get(span.source_id) not in (None, span.revision):
            return _refusal(request, "retrieval provenance is stale")

    query_tokens = _tokens(request.query)
    ranked = []
    for event in snapshot.occurrences:
        if not event.provenance:
            return _refusal(request, "edge occurrence provenance is missing")
        for span in event.provenance:
            if not span.source_id or not span.revision:
                return _refusal(request, "edge occurrence provenance is incomplete")
            if revisions.get(span.source_id) not in (None, span.revision):
                return _refusal(request, "edge occurrence provenance is stale")
        text = " ".join(span.text for span in event.provenance)
        score = len(query_tokens & _tokens(text))
        if score:
            ranked.append((-score, event.edge_instance_id, text, event.provenance))

    ranked.sort(key=lambda row: (row[0], row[1]))
    selected = ranked[:request.budget]
    return RetrievalContext(items=tuple(row[2] for row in selected),
                            citations=tuple(span for row in selected for span in row[3]),
                            provenance=request.provenance, run_id=request.run_id)


deterministic_retrieve = retrieve
