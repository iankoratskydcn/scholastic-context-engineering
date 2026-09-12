# Canonical Stage Contracts v0.1

All stages exchange immutable records carrying `schema_version`, stable `record_id`, `run_id`, producer, status, provenance/source spans, confidence, uncertainty, and diagnostics. Unknown or incompatible versions fail closed.

| Stage | Input | Output | Owner |
|---|---|---|---|
| Ingestion | SourceArtifact | IngestedDocument | ingestion lane |
| Structuring | IngestedDocument | StructuredDocument | ingestion lane |
| Extraction | StructuredDocument + TaxonomySnapshot | ExtractionBundle | extraction lane |
| Formal validation | ArgumentUnit + TaxonomyMatch + Formalization | ValidationResult | formal lane |
| Assembly | ExtractionBundle + ValidationResult | GraphEdgeEvent | assembly lane |
| Storage/indexing | GraphEdgeEvent collection | GraphSnapshot | storage lane |
| Weight projection | GraphSnapshot | WeightProjection | graph lane |
| Community detection | GraphSnapshot + WeightProjection + config | CommunitySnapshot | community lane |
| Retrieval | RetrievalRequest + snapshots | RetrievalContext | retrieval lane |
| Generation/injection | RetrievalContext + request | GenerationResult | generation lane |

## Frozen invariants

- IDs are deterministic over canonical payloads and never caller-repaired.
- A source span is half-open `[start, end)` and its length equals its text length.
- Provenance is required for every accepted record.
- `VALID`, `INVALID`, `UNKNOWN`, `UNSUPPORTED`, and `ILL_POSED` are distinct validation outcomes.
- Unsupported, stale, malformed, uncited, contradictory, or over-budget data is rejected or abstained.
- Frequency and community membership are enrichment only; neither proves entailment or truth.
- Retrieved text is untrusted data and cannot alter policy, tools, instructions, or scope.
- Contract changes require a new version and compatibility fixtures.
