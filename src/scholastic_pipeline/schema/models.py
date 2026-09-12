"""Canonical, dependency-free records shared by all pipeline stages."""
from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from enum import Enum
import hashlib
import json
from typing import Any, ClassVar

SCHEMA_VERSION = "0.1"
MAX_SOURCE_TEXT_BYTES = 1_048_576
MAX_SPAN_TEXT_BYTES = 65_536
MAX_RETRIEVAL_QUERY_BYTES = 16_384


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


def _canonical(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {item.name: _canonical(getattr(value, item.name))
                for item in fields(value) if item.name != "record_id"}
    if isinstance(value, tuple):
        return [_canonical(item) for item in value]
    if isinstance(value, list):
        return [_canonical(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _canonical(item) for key, item in value.items()}
    return value


def _stable_id(kind: str, payload: Any) -> str:
    encoded = json.dumps({"kind": kind, "payload": _canonical(payload)},
                         sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return f"{kind}-{hashlib.sha256(encoded.encode('utf-8')).hexdigest()[:24]}"


def _valid_text(value: object, label: str, *, required: bool = True) -> None:
    if not isinstance(value, str) or (required and not value):
        raise EnvelopeError(f"{label} must be a non-empty string")
    if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
        raise EnvelopeError(f"{label} contains an invalid surrogate")


@dataclass(frozen=True)
class EvidenceSpan:
    source_id: str
    start: int
    end: int
    text: str
    revision: str
    record_id: str = field(init=False)

    def __post_init__(self) -> None:
        _valid_text(self.source_id, "source_id")
        _valid_text(self.revision, "revision")
        _valid_text(self.text, "text", required=False)
        if len(self.text.encode("utf-8")) > MAX_SPAN_TEXT_BYTES:
            raise EnvelopeError("text exceeds absolute byte ceiling")
        if not isinstance(self.start, int) or not isinstance(self.end, int):
            raise EnvelopeError("source span bounds must be integers")
        if self.start < 0 or self.end < self.start:
            raise EnvelopeError("source span bounds are invalid")
        if self.end - self.start != len(self.text):
            raise EnvelopeError("source span length must equal text length")
        object.__setattr__(self, "record_id", _stable_id("span", self))


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
        _valid_text(self.producer, "producer")
        _valid_text(self.run_id, "run_id")
        if self.schema_version != SCHEMA_VERSION:
            raise EnvelopeError(f"unsupported schema version: {self.schema_version}")
        if self.status not in {s.value for s in RecordStatus}:
            raise EnvelopeError(f"unknown record status: {self.status}")
        if self.confidence is not None and not isinstance(self.confidence, (int, float)):
            raise EnvelopeError("confidence must be numeric or null")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            raise EnvelopeError("confidence must be between 0 and 1")
        if not self.provenance:
            raise EnvelopeError("at least one provenance span is required")
        if any(not isinstance(span, EvidenceSpan) for span in self.provenance):
            raise EnvelopeError("provenance must contain evidence spans")
        object.__setattr__(self, "record_id", _stable_id(self.kind, self.to_payload()))

    def to_payload(self) -> dict[str, Any]:
        """Return the complete JSON-safe canonical payload, excluding derived ID."""
        payload = _canonical(self)
        payload["kind"] = self.kind
        return payload


@dataclass(frozen=True)
class IngestedDocument(Envelope):
    document_id: str = ""
    revision: str = ""
    bytes_hash: str = ""
    spans: tuple[EvidenceSpan, ...] = ()
    kind: ClassVar[str] = "ingested_document"

    def __post_init__(self) -> None:
        _valid_text(self.document_id, "document_id")
        _valid_text(self.revision, "revision")
        if not isinstance(self.bytes_hash, str) or len(self.bytes_hash) != 64:
            raise EnvelopeError("document identity, revision, and SHA-256 hash are required")
        if not self.spans:
            raise EnvelopeError("ingested document requires ordered spans")
        if sum(len(span.text.encode("utf-8")) for span in self.spans) > MAX_SOURCE_TEXT_BYTES:
            raise EnvelopeError("source text exceeds absolute byte ceiling")
        if not self.provenance:
            object.__setattr__(self, "provenance", self.spans)
        if any(span.revision != self.revision for span in self.spans):
            raise EnvelopeError("document spans must use document revision")
        super().__post_init__()


@dataclass(frozen=True)
class StructuredDocument(IngestedDocument):
    blocks: tuple[str, ...] = ()
    kind: ClassVar[str] = "structured_document"

    def __post_init__(self) -> None:
        if len(self.blocks) != len(self.spans):
            raise EnvelopeError("structured document blocks and spans must have matching cardinality")
        if any(not isinstance(block, str) for block in self.blocks):
            raise EnvelopeError("structured document blocks must be strings")
        super().__post_init__()


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
class TaxonomySnapshot(Envelope):
    """Immutable taxonomy authority supplied to production extraction."""
    snapshot_id: str = ""
    supported_taxonomy_ids: tuple[str, ...] = ()
    kind: ClassVar[str] = "taxonomy_snapshot"

    def __post_init__(self) -> None:
        _valid_text(self.snapshot_id, "snapshot_id")
        if not self.supported_taxonomy_ids or any(
            not isinstance(value, str) or not value for value in self.supported_taxonomy_ids
        ):
            raise EnvelopeError("taxonomy snapshot requires supported taxonomy IDs")
        super().__post_init__()


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

    def __post_init__(self) -> None:
        # Preserve hostile query data for retrieve() to refuse, while keeping
        # construction and stable-ID derivation exception-free.
        invalid = (
            not isinstance(self.query, str)
            or any(0xD800 <= ord(char) <= 0xDFFF for char in self.query)
            or not self.query.strip()
            or len(self.query.encode("utf-8")) > MAX_RETRIEVAL_QUERY_BYTES
        )
        if not invalid:
            super().__post_init__()
            return
        original = self.query
        object.__setattr__(self, "query", "<invalid retrieval query>")
        try:
            super().__post_init__()
        finally:
            object.__setattr__(self, "query", original)


@dataclass(frozen=True)
class RetrievalContext(Envelope):
    items: tuple[str, ...] = ()
    citations: tuple[EvidenceSpan, ...] = ()
    refusal: str | None = None
    kind: ClassVar[str] = "retrieval_context"
