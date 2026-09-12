"""Local, deterministic text ingestion and paragraph structuring."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import re
from typing import Any

from scholastic_pipeline.schema import (
    EvidenceSpan, IngestedDocument, MAX_SOURCE_TEXT_BYTES, MAX_SPAN_TEXT_BYTES,
    RecordStatus, StructuredDocument,
)


@dataclass(frozen=True)
class QuarantinedDocument:
    """A source that cannot be represented without loss in the contract."""

    source_id: str
    run_id: str
    status: str
    diagnostics: tuple[str, ...]
    document_id: str
    revision: str
    bytes_hash: str
    spans: tuple[EvidenceSpan, ...] = ()
    record_id: str = field(init=False)

    def __post_init__(self) -> None:
        payload = {
            "kind": "quarantined_document", "source_id": self.source_id, "run_id": self.run_id,
            "status": self.status, "diagnostics": list(self.diagnostics), "document_id": self.document_id,
            "revision": self.revision, "bytes_hash": self.bytes_hash,
            "spans": [s.record_id for s in self.spans],
        }
        object.__setattr__(self, "record_id", "quarantine-" + _digest("quarantined_document", payload))


def _digest(kind: str, payload: dict[str, Any]) -> str:
    canonical = json.dumps({"kind": kind, **payload}, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:24]


def _source_bytes(source: str | bytes) -> tuple[bytes, str | None]:
    if isinstance(source, bytes):
        raw = source
    elif isinstance(source, str):
        try:
            raw = source.encode("utf-8", errors="strict")
        except UnicodeEncodeError:
            return b"", "source text cannot be encoded as strict UTF-8"
    else:
        return b"", "source must be str or bytes"
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return raw, "source is not valid UTF-8"
    if "\ufffd" in text:
        return raw, "source contains a replacement character and may be lossy"
    return raw, None


def _quarantine(source_id: object, run_id: object, reason: str) -> QuarantinedDocument:
    """Build a safe quarantine record without interpreting hostile identity data."""
    safe_source_id = source_id if isinstance(source_id, str) and not any(
        0xD800 <= ord(char) <= 0xDFFF for char in source_id
    ) else ""
    safe_run_id = run_id if isinstance(run_id, str) and not any(
        0xD800 <= ord(char) <= 0xDFFF for char in run_id
    ) else ""
    return QuarantinedDocument(
        safe_source_id, safe_run_id, RecordStatus.QUARANTINED.value, (reason,),
        "doc-quarantined", "rev-quarantined", "0" * 64,
    )


def ingest_text(source_id: str, source: str | bytes, *, run_id: str) -> IngestedDocument | QuarantinedDocument:
    """Decode local text strictly and emit one exact source span."""
    if (not isinstance(source_id, str) or not source_id
            or any(0xD800 <= ord(char) <= 0xDFFF for char in source_id)):
        return _quarantine(source_id, run_id, "source_id is malformed")
    if not isinstance(run_id, str) or not run_id or any(0xD800 <= ord(char) <= 0xDFFF for char in run_id):
        return _quarantine(source_id, run_id, "run_id is malformed")
    raw, problem = _source_bytes(source)
    if not raw:
        problem = problem or "empty source is not admissible"
    elif len(raw) > MAX_SOURCE_TEXT_BYTES:
        problem = problem or "source text exceeds absolute byte ceiling"
    elif len(raw) > MAX_SPAN_TEXT_BYTES:
        problem = problem or "source span exceeds absolute byte ceiling"
    if not source_id:
        problem = problem or "source_id is required"
    if not run_id:
        problem = problem or "run_id is required"
    bytes_hash = hashlib.sha256(raw).hexdigest()
    document_id = "doc-" + _digest("document", {"source_id": source_id})
    revision = "rev-" + _digest("revision", {"document_id": document_id, "bytes_hash": bytes_hash})
    if problem:
        return QuarantinedDocument(source_id, run_id, RecordStatus.QUARANTINED.value, (problem,), document_id, revision, bytes_hash)
    text = raw.decode("utf-8")
    span = EvidenceSpan(source_id=source_id, start=0, end=len(text), text=text, revision=revision)
    return IngestedDocument(document_id=document_id, revision=revision, bytes_hash=bytes_hash, spans=(span,), run_id=run_id)


def structure_document(document: IngestedDocument | QuarantinedDocument) -> StructuredDocument | QuarantinedDocument:
    """Split accepted text on blank lines, retaining exact source offsets."""
    if isinstance(document, QuarantinedDocument):
        return document
    if not isinstance(document, IngestedDocument):
        return _quarantine("", "", "document is malformed")
    if document.status != RecordStatus.ACCEPTED.value:
        return document
    if not isinstance(document.spans, tuple) or len(document.spans) != 1:
        return _quarantine(getattr(document, "document_id", ""), document.run_id, "document spans are malformed")
    source = document.spans[0]
    if not isinstance(source, EvidenceSpan) or not isinstance(source.text, str):
        return _quarantine(getattr(source, "source_id", ""), document.run_id, "document span is malformed")
    blocks: list[str] = []
    spans: list[EvidenceSpan] = []
    for match in re.finditer(r"[^\n](?:.*?[^\n])?(?=(?:\n[ \t]*\n)|$)", source.text, re.DOTALL):
        text = match.group(0)
        start = source.start + match.start()
        end = start + len(text)
        blocks.append(text)
        spans.append(EvidenceSpan(source_id=source.source_id, start=start, end=end, text=text, revision=document.revision))
    if not spans and source.text == "":
        return QuarantinedDocument(document.source_id if hasattr(document, "source_id") else source.source_id, "", RecordStatus.QUARANTINED.value, ("empty source is malformed",), document.document_id, document.revision, document.bytes_hash)
    return StructuredDocument(
        document_id=document.document_id, revision=document.revision, bytes_hash=document.bytes_hash,
        spans=tuple(spans), blocks=tuple(blocks), run_id=document.run_id,
    )


def to_payload(record: IngestedDocument | StructuredDocument | QuarantinedDocument) -> dict[str, Any]:
    """Return a complete JSON-safe canonical envelope payload."""
    if isinstance(record, (IngestedDocument, StructuredDocument)):
        result = record.to_payload()
        if hasattr(record, "blocks"):
            result["blocks"] = list(record.blocks)
        return result
    result = {
        "kind": "quarantined_document", "schema_version": "0.1", "record_id": record.record_id,
        "run_id": record.run_id, "producer": "scholastic-context-engineering", "status": record.status,
        "provenance": [
            {"source_id": s.source_id, "start": s.start, "end": s.end,
             "text": s.text, "revision": s.revision, "record_id": s.record_id}
            for s in record.spans
        ],
        "confidence": None, "uncertainty": [], "diagnostics": list(record.diagnostics),
        "document_id": record.document_id, "revision": record.revision, "bytes_hash": record.bytes_hash,
        "spans": [
            {"source_id": s.source_id, "start": s.start, "end": s.end,
             "text": s.text, "revision": s.revision, "record_id": s.record_id}
            for s in record.spans
        ],
    }
    return result
