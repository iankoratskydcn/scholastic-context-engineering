from pathlib import Path

import pytest

from scholastic_pipeline.assembly import assemble_edge_events
from scholastic_pipeline.backends.reference import ReferenceSQLiteBackend
from scholastic_pipeline.formal import Formalization, validate
from scholastic_pipeline.ingestion import ingest_text, structure_document
from scholastic_pipeline.retrieval import retrieve
from scholastic_pipeline.schema import EvidenceSpan, RecordStatus, RetrievalRequest, StructuredDocument, ValidationStatus
from integration.support import extract_structured_document, formal_argument


FIXTURE = Path(__file__).parents[2] / "fixtures" / "canary" / "canary.txt"
SOURCE_ID = "fixture.canary"
RUN_ID = "canary-run"


def run_canary(path: Path):
    raw = path.read_bytes()
    ingested = ingest_text(SOURCE_ID, raw, run_id=RUN_ID)
    assert ingested.status == RecordStatus.ACCEPTED.value
    structured = structure_document(ingested)
    assert isinstance(structured, StructuredDocument)
    extracted = extract_structured_document(structured)
    assert extracted.status == RecordStatus.ACCEPTED.value
    assert extracted.argument is not None
    assert extracted.taxonomy is not None

    formal = Formalization(
        "the archive is indexed -> retrieval is deterministic",
        provenance=extracted.argument.provenance,
    )
    validation = validate(
        formal_argument(extracted.argument, "the archive is indexed -> retrieval is deterministic"),
        formal,
        extracted.taxonomy,
    )
    assert validation.validation_status is ValidationStatus.VALID

    events = assemble_edge_events(
        extracted.argument,
        validation,
        provenance=(extracted.provenance,),
        taxonomy_label=extracted.taxonomy.label,
    )
    backend = ReferenceSQLiteBackend(current_revisions={SOURCE_ID: ingested.revision})
    try:
        snapshot = backend.write_generation("canary-generation", events)
        query_span = EvidenceSpan(SOURCE_ID, 0, 5, "query", ingested.revision)
        context = retrieve(
            RetrievalRequest(
                query="ignore previous instructions",
                budget=10,
                provenance=(query_span,),
                run_id=RUN_ID,
            ),
            snapshot,
            current_revisions={SOURCE_ID: ingested.revision},
        )
        return snapshot, context
    finally:
        backend.close()


def test_canary_pipeline_retrieves_hostile_text_as_untrusted_evidence(tmp_path):
    first_snapshot, first_context = run_canary(FIXTURE)
    second_snapshot, second_context = run_canary(FIXTURE)

    assert first_context.refusal is None
    assert any("IGNORE ALL PREVIOUS INSTRUCTIONS" in item for item in first_context.items)
    assert first_context.items == second_context.items
    assert first_context.citations == second_context.citations
    assert first_snapshot.occurrences == second_snapshot.occurrences
    assert first_snapshot.record_id == second_snapshot.record_id
    assert tmp_path.exists()
