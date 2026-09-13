"""Small occurrence-preserving SQLite reference backend."""
from __future__ import annotations

import json
import sqlite3
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Iterable

from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, GraphSnapshot, RecordStatus


class StorageError(ValueError):
    """Base class for storage boundary failures."""


class IncompleteGenerationError(StorageError):
    pass


class ProvenanceError(StorageError):
    pass


MAX_MANIFEST_ENTRIES = 100_000


def _span_payload(span: EvidenceSpan) -> dict:
    return {"source_id": span.source_id, "revision": span.revision, "start": span.start,
            "end": span.end, "text": span.text}


def _edge_payload(edge: GraphEdgeEvent) -> dict:
    return {
        "edge_instance_id": edge.edge_instance_id, "source_node_id": edge.source_node_id,
        "target_node_id": edge.target_node_id, "relation": edge.relation,
        "validation_status": edge.validation_status.value, "producer": edge.producer,
        "run_id": edge.run_id, "status": edge.status, "confidence": edge.confidence,
        "uncertainty": list(edge.uncertainty), "diagnostics": list(edge.diagnostics),
        "schema_version": edge.schema_version,
        "provenance": [_span_payload(s) for s in edge.provenance],
    }


def _edge_from_payload(payload: dict) -> GraphEdgeEvent:
    from scholastic_pipeline.schema import ValidationStatus
    try:
        spans = tuple(EvidenceSpan(**s) for s in payload["provenance"])
        return GraphEdgeEvent(
            edge_instance_id=payload["edge_instance_id"], source_node_id=payload["source_node_id"],
            target_node_id=payload["target_node_id"], relation=payload["relation"],
            validation_status=ValidationStatus(payload["validation_status"]),
            provenance=spans, run_id=payload["run_id"], producer=payload["producer"],
            status=payload["status"], confidence=payload["confidence"],
            uncertainty=tuple(payload["uncertainty"]), diagnostics=tuple(payload["diagnostics"]),
            schema_version=payload["schema_version"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise StorageError("stored edge envelope is invalid") from exc


def _scope(event: GraphEdgeEvent) -> frozenset[tuple[str, str]]:
    return frozenset((span.source_id, span.revision) for span in event.provenance)


def _validate_generation_id(generation_id: object) -> str:
    if not isinstance(generation_id, str) or not generation_id:
        raise StorageError("generation ID is required")
    return generation_id


def _validate_generation_options(expected_count: object, manifest: object) -> tuple[int | None, tuple[str, ...] | None]:
    if expected_count is not None and (not isinstance(expected_count, int) or isinstance(expected_count, bool)):
        raise StorageError("expected count must be an integer")
    if expected_count is not None and expected_count < 0:
        raise StorageError("expected count must not be negative")
    if manifest is None:
        return expected_count, None
    if isinstance(manifest, (str, bytes, bytearray)) or not isinstance(manifest, Sequence):
        raise StorageError("manifest must be a bounded sequence of strings")
    try:
        if len(manifest) > MAX_MANIFEST_ENTRIES:
            raise StorageError("manifest exceeds absolute entry ceiling")
        manifest = tuple(manifest)
    except StorageError:
        raise
    except (TypeError, ValueError, OverflowError) as exc:
        raise StorageError("manifest must be a bounded sequence of strings") from exc
    if any(not isinstance(edge_id, str) or not edge_id
           or any(0xD800 <= ord(char) <= 0xDFFF for char in edge_id)
           for edge_id in manifest):
        raise StorageError("manifest must contain valid strings")
    if expected_count is not None and len(manifest) != expected_count:
        raise StorageError("manifest and expected count disagree")
    return expected_count, manifest


class ReferenceSQLiteBackend:
    """Transactional reference store; each edge ID denotes one occurrence."""

    def __init__(self, path: str | Path = ":memory:", current_revisions: Mapping[str, str] | None = None):
        if current_revisions is not None and not isinstance(current_revisions, Mapping):
            raise StorageError("current revisions must be a mapping")
        self.current_revisions = current_revisions or {}
        self._db = sqlite3.connect(str(path))
        self._db.execute("PRAGMA foreign_keys = ON")
        self._db.executescript("""
            CREATE TABLE IF NOT EXISTS generations (
                generation_id TEXT PRIMARY KEY, status TEXT NOT NULL,
                expected_count INTEGER, manifest TEXT
            );
            CREATE TABLE IF NOT EXISTS occurrences (
                generation_id TEXT NOT NULL REFERENCES generations(generation_id),
                edge_instance_id TEXT NOT NULL, ordinal INTEGER NOT NULL, payload TEXT NOT NULL,
                PRIMARY KEY (generation_id, edge_instance_id), UNIQUE (generation_id, ordinal)
            );
        """)
        self._db.commit()

    def close(self) -> None:
        self._db.close()

    def _validate(self, events: Iterable[GraphEdgeEvent]) -> tuple[GraphEdgeEvent, ...]:
        try:
            events = tuple(events)
            if not events:
                raise IncompleteGenerationError("empty generation is unreadable")
            if any(not isinstance(event, GraphEdgeEvent) for event in events):
                raise StorageError("event is invalid")
            first = events[0]
            expected_scope = _scope(first)
            for event in events:
                if not event.provenance or not event.edge_instance_id:
                    raise ProvenanceError("accepted edge occurrences require provenance and identity")
                if event.run_id != first.run_id:
                    raise StorageError("mixed run IDs are not admissible")
                if event.schema_version != first.schema_version:
                    raise StorageError("mixed schema versions are not admissible")
                if _scope(event) != expected_scope:
                    raise ProvenanceError("mixed provenance scopes are not admissible")
                for span in event.provenance:
                    if not span.source_id or not span.revision:
                        raise ProvenanceError("provenance source and revision are required")
                    expected = self.current_revisions.get(span.source_id)
                    if expected is not None and expected != span.revision:
                        raise ProvenanceError("stale provenance revision")
            return events
        except StorageError:
            raise
        except Exception as exc:
            raise StorageError("events are invalid") from exc

    def begin_generation(self, generation_id: str, expected_count: int | None = None,
                         manifest: Sequence[str] | None = None) -> None:
        generation_id = _validate_generation_id(generation_id)
        expected_count, manifest = _validate_generation_options(expected_count, manifest)
        self._db.execute(
            "INSERT OR IGNORE INTO generations VALUES (?, 'writing', ?, ?)",
            (generation_id, expected_count, json.dumps(list(manifest)) if manifest is not None else None),
        )
        self._db.commit()

    def _append(self, generation_id: str, event: GraphEdgeEvent) -> None:
        status = self._db.execute("SELECT status FROM generations WHERE generation_id=?", (generation_id,)).fetchone()[0]
        row = self._db.execute("SELECT payload FROM occurrences WHERE generation_id=? AND edge_instance_id=?",
                               (generation_id, event.edge_instance_id)).fetchone()
        encoded = json.dumps(_edge_payload(event), sort_keys=True, separators=(",", ":"))
        if row is not None:
            if row[0] != encoded:
                raise StorageError("edge identity collision with different payload")
            return
        if status == "complete":
            raise StorageError("completed generation is immutable")
        ordinal = self._db.execute("SELECT COALESCE(MAX(ordinal), -1)+1 FROM occurrences WHERE generation_id=?",
                                   (generation_id,)).fetchone()[0]
        self._db.execute("INSERT INTO occurrences VALUES (?, ?, ?, ?)",
                         (generation_id, event.edge_instance_id, ordinal, encoded))

    def append(self, generation_id: str, event: GraphEdgeEvent) -> None:
        generation_id = _validate_generation_id(generation_id)
        self._validate((event,))
        self.begin_generation(generation_id)
        existing = tuple(_edge_from_payload(json.loads(row[0])) for row in self._db.execute(
            "SELECT payload FROM occurrences WHERE generation_id=? ORDER BY ordinal", (generation_id,)))
        self._validate((*existing, event))
        self._append(generation_id, event)
        self._db.commit()

    def complete_generation(self, generation_id: str) -> None:
        generation_id = _validate_generation_id(generation_id)
        row = self._db.execute("SELECT status, expected_count, manifest FROM generations WHERE generation_id=?", (generation_id,)).fetchone()
        if row is None:
            raise StorageError("unknown generation")
        if row[0] == "complete":
            return
        ids = [r[0] for r in self._db.execute("SELECT edge_instance_id FROM occurrences WHERE generation_id=?", (generation_id,))]
        if row[1] is not None and len(ids) != row[1]:
            raise IncompleteGenerationError("generation does not meet expected count")
        if row[2] is not None and set(ids) != set(json.loads(row[2])):
            raise IncompleteGenerationError("generation does not match manifest")
        if not ids:
            raise IncompleteGenerationError("empty generation is unreadable")
        self._db.execute("UPDATE generations SET status='complete' WHERE generation_id=?", (generation_id,))
        self._db.commit()

    def write_generation(self, generation_id: str, events: Iterable[GraphEdgeEvent],
                         expected_count: int | None = None, manifest: Sequence[str] | None = None) -> GraphSnapshot:
        generation_id = _validate_generation_id(generation_id)
        expected_count, manifest = _validate_generation_options(expected_count, manifest)
        events = self._validate(events)
        existing = self._db.execute("SELECT status FROM generations WHERE generation_id=?", (generation_id,)).fetchone()
        if existing is not None and existing[0] == "complete":
            current = self.read_generation(generation_id).occurrences
            if current == events:
                return self.read_generation(generation_id)
            raise StorageError("completed generation is immutable")
        if expected_count is not None and len(events) != expected_count:
            raise IncompleteGenerationError("generation does not meet expected count")
        if manifest is not None and set(event.edge_instance_id for event in events) != set(manifest):
            raise IncompleteGenerationError("generation does not match manifest")
        try:
            self._db.execute("BEGIN")
            self._db.execute("DELETE FROM occurrences WHERE generation_id=?", (generation_id,))
            self._db.execute("DELETE FROM generations WHERE generation_id=?", (generation_id,))
            self._db.execute("INSERT INTO generations VALUES (?, 'writing', ?, ?)",
                              (generation_id, expected_count, json.dumps(list(manifest)) if manifest is not None else None))
            for event in events:
                self._append(generation_id, event)
            self.complete_generation(generation_id)
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise
        return self.read_generation(generation_id)

    def read_generation(self, generation_id: str) -> GraphSnapshot:
        generation_id = _validate_generation_id(generation_id)
        row = self._db.execute("SELECT status FROM generations WHERE generation_id=?", (generation_id,)).fetchone()
        if row is None or row[0] != "complete":
            raise IncompleteGenerationError("generation is incomplete or missing")
        rows = self._db.execute("SELECT payload FROM occurrences WHERE generation_id=? ORDER BY ordinal", (generation_id,)).fetchall()
        events = self._validate(_edge_from_payload(json.loads(r[0])) for r in rows)
        return GraphSnapshot(generation_id=generation_id, occurrences=events,
                             provenance=events[0].provenance, run_id=events[0].run_id)


SQLiteReferenceBackend = ReferenceSQLiteBackend
InMemoryReferenceBackend = ReferenceSQLiteBackend
