"""Assembly of validation results into provenance-bearing edge occurrences."""
from __future__ import annotations

import hashlib
import json
from typing import Iterable

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, GraphEdgeEvent, ValidationResult, RecordStatus


def _node_id(value: object) -> str:
    return value.proposition_id if hasattr(value, "proposition_id") else str(value)


def _unique(spans: Iterable[EvidenceSpan]) -> tuple[EvidenceSpan, ...]:
    result: list[EvidenceSpan] = []
    seen: set[str] = set()
    for span in spans:
        if span.record_id not in seen:
            seen.add(span.record_id)
            result.append(span)
    return tuple(result)


def _edge_id(argument_id: str, source: str, target: str, result: ValidationResult) -> str:
    payload = [argument_id, source, target, result.record_id, result.validation_status.value]
    digest = hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()[:24]
    return f"edge-{digest}"


def assemble_edge_events(
    argument: ArgumentUnit,
    validation: ValidationResult,
    *,
    provenance: tuple[EvidenceSpan, ...] | None = None,
    taxonomy_label: str | None = None,
    frequency: int | None = None,
) -> tuple[GraphEdgeEvent, ...]:
    """Emit one edge per premise, carrying status but never upgrading it with enrichment."""
    if not argument.provenance or not validation.provenance:
        raise ValueError("assembly requires argument and validation provenance")
    spans = _unique(provenance if provenance is not None else argument.provenance + validation.provenance)
    if not spans:
        raise ValueError("assembly requires provenance")
    if argument.run_id != validation.run_id:
        raise ValueError("argument and validation run IDs must match")
    record_status = {
        "VALID": RecordStatus.ACCEPTED.value,
        "INVALID": RecordStatus.REJECTED.value,
        "UNKNOWN": RecordStatus.ABSTAINED.value,
        "UNSUPPORTED": RecordStatus.ABSTAINED.value,
        "ILL_POSED": RecordStatus.ABSTAINED.value,
    }[validation.validation_status.value]
    target = _node_id(argument.conclusion)
    return tuple(
        GraphEdgeEvent(
            run_id=argument.run_id,
            status=record_status,
            provenance=spans,
            edge_instance_id=_edge_id(argument.argument_id, premise.proposition_id, target, validation),
            source_node_id=premise.proposition_id,
            target_node_id=target,
            relation=argument.relation,
            validation_status=validation.validation_status,
            diagnostics=validation.diagnostics,
        )
        for premise in argument.premises
    )

assemble = assemble_edge_events

__all__ = ["assemble", "assemble_edge_events"]
