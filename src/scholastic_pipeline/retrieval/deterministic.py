"""Dependency-free deterministic retrieval over graph edge occurrences."""
from __future__ import annotations

import re
from collections.abc import Mapping

from scholastic_pipeline.schema import (
    GraphSnapshot, MAX_SPAN_TEXT_BYTES, RecordStatus, RetrievalContext,
    RetrievalRequest,
)


_TOKEN = re.compile(r"[\w]+", re.UNICODE)
MAX_RETRIEVAL_BUDGET = 100
MAX_RETRIEVAL_QUERY_BYTES = 16_384
MAX_RETRIEVAL_INPUT_BYTES = 4_194_304
MAX_RETRIEVAL_OUTPUT_BYTES = 1_048_576


def _tokens(text: str) -> set[str]:
    return {token.casefold() for token in _TOKEN.findall(text)}


def _refusal(request: RetrievalRequest, reason: str) -> RetrievalContext:
    return RetrievalContext(items=(), citations=(), refusal=reason,
                            provenance=request.provenance, run_id=request.run_id)


def _scope(spans) -> frozenset[tuple[str, str]]:
    return frozenset((span.source_id, span.revision) for span in spans)


def _span_bytes(spans) -> int:
    return sum(len(span.text.encode("utf-8")) for span in spans)


def _has_oversized_span(spans) -> bool:
    return any(len(span.text.encode("utf-8")) > MAX_SPAN_TEXT_BYTES for span in spans)


def _input_bytes(request: RetrievalRequest, snapshot: GraphSnapshot) -> int:
    return (len(request.query.encode("utf-8")) + _span_bytes(request.provenance)
            + _span_bytes(snapshot.provenance)
            + sum(_span_bytes(event.provenance) for event in snapshot.occurrences))


def retrieve(request: RetrievalRequest, snapshot: GraphSnapshot,
             current_revisions: Mapping[str, str] | None = None) -> RetrievalContext:
    """Return bounded, admissible matching occurrences in stable order."""
    if request.budget <= 0:
        return _refusal(request, "retrieval budget must be positive")
    if request.budget > MAX_RETRIEVAL_BUDGET:
        return _refusal(request, "retrieval budget exceeds absolute ceiling")
    if not request.query.strip():
        return _refusal(request, "retrieval query is empty")
    if len(request.query.encode("utf-8")) > MAX_RETRIEVAL_QUERY_BYTES:
        return _refusal(request, "retrieval query exceeds absolute byte ceiling")
    if request.status != RecordStatus.ACCEPTED.value or snapshot.status != RecordStatus.ACCEPTED.value:
        return _refusal(request, "retrieval status is not admissible")
    if request.run_id != snapshot.run_id:
        return _refusal(request, "retrieval run ID does not match snapshot")
    if request.schema_version != snapshot.schema_version:
        return _refusal(request, "retrieval schema version does not match snapshot")
    if not request.provenance or not snapshot.provenance:
        return _refusal(request, "retrieval provenance is missing")

    revisions = current_revisions or {}
    request_scope = _scope(request.provenance)
    snapshot_scope = _scope(snapshot.provenance)
    if request_scope != snapshot_scope:
        return _refusal(request, "retrieval provenance scope does not match snapshot")
    all_spans = (*request.provenance, *snapshot.provenance,
                 *(span for event in snapshot.occurrences for span in event.provenance))
    if _has_oversized_span(all_spans):
        return _refusal(request, "retrieval span exceeds absolute byte ceiling")
    if _input_bytes(request, snapshot) > MAX_RETRIEVAL_INPUT_BYTES:
        return _refusal(request, "retrieval input exceeds absolute byte ceiling")
    for span in (*request.provenance, *snapshot.provenance):
        if not span.source_id or not span.revision:
            return _refusal(request, "retrieval provenance is incomplete")
        if revisions.get(span.source_id) not in (None, span.revision):
            return _refusal(request, "retrieval provenance is stale")

    query_tokens = _tokens(request.query)
    ranked = []
    for event in snapshot.occurrences:
        if event.status != RecordStatus.ACCEPTED.value:
            return _refusal(request, "edge status is not admissible")
        if event.run_id != snapshot.run_id or event.schema_version != snapshot.schema_version:
            return _refusal(request, "edge envelope is outside snapshot scope")
        if _scope(event.provenance) != snapshot_scope:
            return _refusal(request, "edge provenance scope does not match snapshot")
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
    output_bytes = sum(len(row[2].encode("utf-8")) for row in selected)
    if output_bytes > MAX_RETRIEVAL_OUTPUT_BYTES:
        return _refusal(request, "retrieval output exceeds absolute byte ceiling")
    return RetrievalContext(items=tuple(row[2] for row in selected),
                            citations=tuple(span for row in selected for span in row[3]),
                            provenance=request.provenance, run_id=request.run_id)


deterministic_retrieve = retrieve
