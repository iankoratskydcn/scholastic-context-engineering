"""Small occurrence-preserving SQLite reference backend."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable

from scholastic_pipeline.schema import EvidenceSpan, GraphEdgeEvent, GraphSnapshot


class StorageError(ValueError):
    """Base class for storage boundary failures."""


class IncompleteGenerationError(StorageError):
    pass


class ProvenanceError(StorageError):
    pass


def _span_payload(span: EvidenceSpan) -> dict:
    return {"source_id": span.source_id, "revision": span.revision, "start": span.start,
            "end": span.end, "text": span.text}


def _edge_payload(edge: GraphEdgeEvent) -> dict:
    return {"edge_instance_id": edge.edge_instance_id, "source_node_id": edge.source_node_id,
            "target_node_id": edge.target_node_id, "relation": edge.relation,
            "validation_status": edge.validation_status.value, "run_id": edge.run_id,
            "producer": edge.producer, "provenance": [_span_payload(s) for s in edge.provenance]}


def _edge_from_payload(payload: dict) -> GraphEdgeEvent:
    spans = tuple(EvidenceSpan(**s) for s in payload["provenance"])
    from scholastic_pipeline.schema import ValidationStatus
    return GraphEdgeEvent(edge_instance_id=payload["edge_instance_id"],
        source_node_id=payload["source_node_id"], target_node_id=payload["target_node_id"],
        relation=payload["relation"], validation_status=ValidationStatus(payload["validation_status"]),
        provenance=spans, run_id=payload["run_id"], producer=payload["producer"])


class ReferenceSQLiteBackend:
    """Transactional reference store; each edge ID denotes one occurrence."""

    def __init__(self, path: str | Path = ":memory:", current_revisions: dict[str, str] | None = None):
        self.current_revisions = current_revisions or {}
        self._db = sqlite3.connect(str(path))
        self._db.execute("PRAGMA foreign_keys = ON")
        self._db.executescript("""
            CREATE TABLE IF NOT EXISTS generations (generation_id TEXT PRIMARY KEY, status TEXT NOT NULL);
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
        events = tuple(events)
        for event in events:
            if not event.provenance or not event.edge_instance_id:
                raise ProvenanceError("accepted edge occurrences require provenance and identity")
            for span in event.provenance:
                if not span.source_id or not span.revision:
                    raise ProvenanceError("provenance source and revision are required")
                expected = self.current_revisions.get(span.source_id)
                if expected is not None and expected != span.revision:
                    raise ProvenanceError("stale provenance revision")
        return events

    def begin_generation(self, generation_id: str) -> None:
        if not generation_id:
            raise StorageError("generation ID is required")
        self._db.execute("INSERT OR IGNORE INTO generations VALUES (?, 'writing')", (generation_id,))
        self._db.commit()

    def append(self, generation_id: str, event: GraphEdgeEvent) -> None:
        event = self._validate((event,))[0]
        self.begin_generation(generation_id)
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
        self._db.commit()

    def complete_generation(self, generation_id: str) -> None:
        row = self._db.execute("SELECT status FROM generations WHERE generation_id=?", (generation_id,)).fetchone()
        if row is None:
            raise StorageError("unknown generation")
        self._db.execute("UPDATE generations SET status='complete' WHERE generation_id=?", (generation_id,))
        self._db.commit()

    def write_generation(self, generation_id: str, events: Iterable[GraphEdgeEvent]) -> GraphSnapshot:
        events = self._validate(events)
        self.begin_generation(generation_id)
        for event in events:
            self.append(generation_id, event)
        self.complete_generation(generation_id)
        return self.read_generation(generation_id)

    def read_generation(self, generation_id: str) -> GraphSnapshot:
        row = self._db.execute("SELECT status FROM generations WHERE generation_id=?", (generation_id,)).fetchone()
        if row is None or row[0] != "complete":
            raise IncompleteGenerationError("generation is incomplete or missing")
        rows = self._db.execute("SELECT payload FROM occurrences WHERE generation_id=? ORDER BY ordinal", (generation_id,)).fetchall()
        events = tuple(_edge_from_payload(json.loads(r[0])) for r in rows)
        if not events:
            raise IncompleteGenerationError("empty generation is unreadable")
        return GraphSnapshot(generation_id=generation_id, occurrences=events,
                             provenance=events[0].provenance, run_id=events[0].run_id)


SQLiteReferenceBackend = ReferenceSQLiteBackend
InMemoryReferenceBackend = ReferenceSQLiteBackend
