# Scholastic Context Engineering

Standalone, evidence-first pipeline for provenance-bearing argument extraction and retrieval.

- Canonical schema authority: `schemas/` (to be frozen before implementation)
- Source-of-truth: versioned artifacts under `docs/evidence/` and `fixtures/`
- Setup: `uv sync --extra dev` (installs pytest, jsonschema, pip into the venv)
- Supported execution command: `uv run pytest -q` (reconnaissance/bootstrap only until contracts are frozen)

The first slice is intentionally small: frozen local text → exact spans → typed premise/conclusion extraction → taxonomy match → formal validation result → provenance-bearing edge occurrence → deterministic local retrieval.

No cloud ingestion, full GraphRAG fork, Hermes-core modifications, or unapproved runtime dependency is part of the bootstrap.
