"""Canonical, dependency-free records shared by all pipeline stages."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import hashlib
import json
from typing import Any, ClassVar

SCHEMA_VERSION = "0.1"


class EnvelopeError(ValueError):
    """Raised when a canonical record violates its boundary contract."""


class RecordStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    QUARANTINED = "QUARANTINED"
    REJECTED = "REJECTED"
    ABSTAINED = "ABSTAINED"


class ValidationStatus(str, Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"
    UNSUPPORTED = "UNSUPPORTED"
    ILL_POSED = "ILL_POSED"


def _stable_id(kind: str, payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return f"{kind}-{hashlib.sha256(encoded.encode('utf-8')).hexdigest()[:24]}"


@dataclass(frozen=True)
class EvidenceSpan:
    source_id: str
    start: int
    end: int
    text: str
    revision: str = ""
    record_id: str = field(init=False)

    def __post_init__(self) -> None:
        if not self.source_id or not self.revision and self.revision is None:
            raise EnvelopeError("source_id and revision identity are required")
        if self.start < 0 or self.end < self.start:
            raise EnvelopeError("source span bounds are invalid")
        if self.end - self.start != len(self.text):
            raise EnvelopeError("source span length must equal text length")
        object.__setattr__(self, "record_id", _stable_id("span", {
            "source_id": self.source_id, "revision": self.revision,
            "start": self.start, "end": self.end, "text": self.text,
        }))


@dataclass(frozen=True)
class Envelope:
    producer: str = "scholastic-context-engineering"
    run_id: str = ""
    status: str = RecordStatus.ACCEPTED.value
    confidence: float | None = None
    uncertainty: tuple[str, ...] = ()
    diagnostics: tuple[str, ...] = ()
    schema_version: str = SCHEMA_VERSION
    record_id: str = field(init=False)
    provenance: tuple[EvidenceSpan, ...] = ()

    kind: ClassVar[str] = "record"

    def __post_init__(self) -> None:
        if self.schema_version != SCHEMA_VERSION:
            raise EnvelopeError(f"unsupported schema version: {self.schema_version}")
        if not self.producer or not self.run_id:
            raise EnvelopeError("producer and run_id are required")
        if self.status not in {s.value for s in RecordStatus}:
            raise EnvelopeError(f"unknown record status: {self.status}")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            raise EnvelopeError("confidence must be between 0 and 1")
        if not self.provenance:
            raise EnvelopeError("at least one provenance span is required")
        object.__setattr__(self, "record_id", _stable_id(self.kind, self.to_payload()))

    def to_payload(self) -> dict[str, Any]:
        return {"kind": self.kind, "schema_version": self.schema_version,
                "run_id": self.run_id, "status": self.status,
                "provenance": [s.record_id for s in self.provenance]}


@dataclass(frozen=True)
class IngestedDocument(Envelope):
    document_id: str = ""
    revision: str = ""
    bytes_hash: str = ""
    spans: tuple[EvidenceSpan, ...] = ()
    kind: ClassVar[str] = "ingested_document"

    def __post_init__(self) -> None:
        if not self.document_id or not self.revision or len(self.bytes_hash) != 64:
            raise EnvelopeError("document identity, revision, and SHA-256 hash are required")
        if not self.spans:
            raise EnvelopeError("ingested document requires ordered spans")
        if not self.provenance:
            object.__setattr__(self, "provenance", self.spans)
        super().__post_init__()


@dataclass(frozen=True)
class StructuredDocument(IngestedDocument):
    blocks: tuple[str, ...] = ()
    kind: ClassVar[str] = "structured_document"


@dataclass(frozen=True)
class Proposition(Envelope):
    proposition_id: str = ""
    text: str = ""
    role: str = ""
    kind: ClassVar[str] = "proposition"


@dataclass(frozen=True)
class ArgumentUnit(Envelope):
    argument_id: str = ""
    premises: tuple[Proposition, ...] = ()
    conclusion: Proposition | str = ""
    relation: str = ""
    kind: ClassVar[str] = "argument_unit"

    def __post_init__(self) -> None:
        if not self.argument_id or not self.premises or not self.relation:
            raise EnvelopeError("argument requires ID, premise(s), relation, and provenance")
        super().__post_init__()


@dataclass(frozen=True)
class TaxonomyMatch(Envelope):
    taxonomy_id: str = ""
    label: str = ""
    kind: ClassVar[str] = "taxonomy_match"


@dataclass(frozen=True)
class ValidationResult(Envelope):
    validation_status: ValidationStatus = ValidationStatus.UNKNOWN
    normalized_form: str = ""
    proof_obligations: tuple[str, ...] = ()
    kind: ClassVar[str] = "validation_result"


@dataclass(frozen=True)
class GraphEdgeEvent(Envelope):
    edge_instance_id: str = ""
    source_node_id: str = ""
    target_node_id: str = ""
    relation: str = ""
    validation_status: ValidationStatus = ValidationStatus.UNKNOWN
    kind: ClassVar[str] = "graph_edge_event"


@dataclass(frozen=True)
class GraphSnapshot(Envelope):
    generation_id: str = ""
    occurrences: tuple[GraphEdgeEvent, ...] = ()
    kind: ClassVar[str] = "graph_snapshot"


@dataclass(frozen=True)
class CommunitySnapshot(Envelope):
    graph_generation: str = ""
    communities: tuple[tuple[str, ...], ...] = ()
    kind: ClassVar[str] = "community_snapshot"


@dataclass(frozen=True)
class RetrievalRequest(Envelope):
    query: str = ""
    budget: int = 0
    kind: ClassVar[str] = "retrieval_request"


@dataclass(frozen=True)
class RetrievalContext(Envelope):
    items: tuple[str, ...] = ()
    citations: tuple[EvidenceSpan, ...] = ()
    refusal: str | None = None
    kind: ClassVar[str] = "retrieval_context"
