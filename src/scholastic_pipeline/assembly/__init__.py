"""Assembly of validation results into provenance-bearing edge occurrences."""
from __future__ import annotations

import hashlib
import json
from typing import Iterable

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, GraphEdgeEvent, ValidationResult, RecordStatus


def assemble_extraction(extraction: object, validation: ValidationResult) -> tuple[GraphEdgeEvent, ...]:
    """Production assembly port consuming the canonical extraction bundle."""
    from scholastic_pipeline.extraction import ExtractionBundle
    if not isinstance(extraction, ExtractionBundle):
        raise TypeError("assembly requires ExtractionBundle")
    if not isinstance(validation, ValidationResult):
        raise TypeError("assembly requires ValidationResult")
    if extraction.argument is None or extraction.taxonomy is None or extraction.provenance is None:
        raise ValueError("assembly requires an accepted extraction with taxonomy")
    return assemble_edge_events(extraction.argument, validation, provenance=(extraction.provenance,))


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


def _edge_id(argument_id: str, source: str, target: str, result: ValidationResult,
             provenance: tuple[EvidenceSpan, ...]) -> str:
    payload = [argument_id, source, target, result.record_id, result.validation_status.value,
               [(s.source_id, s.revision, s.start, s.end, s.text) for s in provenance]]
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
    expected = {s.record_id for s in argument.provenance + validation.provenance}
    if any(s.record_id not in expected for s in spans):
        raise ValueError("assembly provenance does not match argument and validation")
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
            edge_instance_id=_edge_id(argument.argument_id, premise.proposition_id, target, validation, spans),
            source_node_id=premise.proposition_id,
            target_node_id=target,
            relation=argument.relation,
            validation_status=validation.validation_status,
            diagnostics=validation.diagnostics,
        )
        for premise in argument.premises
    )

assemble = assemble_extraction

__all__ = ["assemble", "assemble_edge_events", "assemble_extraction"]
