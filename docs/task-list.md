# Scholastic Context Engineering — Task List

Status snapshot: 2026-10-21

This is an owner-gated implementation backlog. Items remain planning work until explicitly approved and dispatched. No task below authorizes Hermes integration, external runtime dependencies, or destructive cleanup.

## Status legend

- **Done** — verified by existing repository evidence.
- **Blocked** — prerequisite or owner decision is unresolved.
- **Ready after gate** — scope is bounded, but baseline release verification must pass first.
- **Deferred** — intentionally out of the next implementation wave.

## P0 — Close the standalone baseline gate

- [ ] **Repair/recreate the verification environment**
  - Current local `uv run pytest -q`: 208 passed, 1 failed because the Hermes-managed environment cannot import `rpds.rpds`.
  - Acceptance: clean-clone `uv run pytest -q` returns 209 passed, 0 failed; reproducible wheel test passes.

- [ ] **Reconcile current branch evidence**
  - Decide whether `docs/architecture/index.html` and `docs/architecture/workspace.dsl` are intentional tracked artifacts.
  - Re-run checkpoint and full-suite evidence after the current WIP data/docs commit.
  - Acceptance: intended-only working tree and fresh independent verification record.

## P1 — Wave 1: import historical claims as evidence, not semantics

- [ ] **C2 — Historical corpus adapter** — *Ready after gate*
  - Add a versioned, lossless `HistoricalCorpusSnapshot` for the 110-record / 50-source archive.
  - Preserve native terms, historical context, formalization status, examples, related records, and source references.
  - Quarantine unmappable, duplicate, stale, or structurally invalid records.
  - Acceptance: hash/count checks, unique IDs, foreign-key checks, representative fixtures across all 8 dimensions, and round-trip payload equality.

- [ ] **C3 — Corpus source/evidence ledger** — *Ready after gate*
  - Add a hash-bound ledger distinguishing primary text, translation, testimony, scholarly reference, editorial composition, and unresolved support.
  - Do not upgrade evidence basis automatically.
  - Acceptance: forged/stale source IDs, duplicate keys, missing citations, unsupported evidence basis, and sampled all-dimension audit tests.

- [ ] **C4 — Taxonomy snapshot/disposition boundary** — *Ready after gate*
  - Define versioned dispositions: executable candidate, enrichment-only, metadata-only, unresolved, rejected.
  - Keep headings/caveats metadata-only and ambiguous bundles unresolved.
  - Acceptance: stale snapshot refusal, provenance binding, stable IDs, heading-conversion rejection, and ambiguity abstention.

- [ ] **Wave 1 adversarial review and integration gate**
  - Implementers provide RED/GREEN/checkpoint evidence.
  - Independent reviewer verifies schema, provenance, quarantine, and no semantic upgrade.
  - Acceptance: full suite, targeted hostile suite, clean clone, deterministic rerun, and updated evidence artifact.

## P2 — Wave 2: deterministic retrieval payoff

- [ ] **C7 — Corpus retrieval/evaluation fixture** — *Blocked by C2/C3/C4*
  - Add retrieval over imported records and evidence links using the existing bounded deterministic retrieval boundary.
  - Define minimal query vocabulary: text, taxonomy ID, dimension, tradition, source, relation, and combinations as approved.
  - Acceptance: stable ordering, exact citations, hard budgets, stale/forged/unsupported refusal, empty-result behavior, prompt-injection inertness, and repeated-run equality.

- [ ] **Wave 2 independent acceptance gate**
  - Confirm historical metadata survives retrieval and no record becomes `VALID` merely because it parses or ranks highly.

## P3 — Operational hardening choice

- [ ] **Choose one post-retrieval capability**
  - Recommended default: **C9 retry/idempotency and partial-run recovery** before graph enrichment.
  - Alternative: **C8 weight projection/community enrichment** only if Wave 2 demonstrates a concrete navigation need.
  - Acceptance: owner decision records the selected capability and explicit non-goals.

- [ ] **C9 — Retry/idempotency and partial-run recovery** — *Deferred until real artifact boundaries exist*
  - Define authoritative run manifests, stage versions, checkpoint retention, resume behavior, and duplicate handling.
  - Acceptance: interrupted-run, replay-equality, stale-checkpoint, changed-input, missing-artifact, and duplicate-delivery fixtures.

- [ ] **C8 — Weight/community enrichment** — *Deferred unless justified by evidence*
  - Keep graph revision binding and guarantee enrichment cannot upgrade validation, truth, or entailment.
  - Acceptance: deterministic projection, configuration bounds, revision mismatch refusal, and no-validation-upgrade proof.

## Deferred research tracks

- [ ] Candidate-preserving extraction/lattice contract.
- [ ] Attribution, negation, modality, factuality, stance, and speaker/source annotations.
- [ ] Metamorphic transformation relations: equivalent, entails, contradicts, strengthens, weakens, unknown.
- [ ] Multi-frame convergence, calibration, abstention, and out-of-distribution evaluation.
- [ ] Metaphor/narrative evidence frames.
- [ ] Broader corpus acquisition after license and rights review.
- [ ] Hermes handoff documentation and integration seam.

## Explicit non-goals for this plan

- No Hermes-core modification.
- No cloud ingestion or LLM runtime.
- No unapproved NLP dependency.
- No DOCX/OCR pipeline.
- No embeddings, vector database, GraphRAG, or learned ranking.
- No theorem prover or universal historical-logic semantics.
- No automatic truth assessment.

## Owner decisions required before Wave 1 cards

1. Approve lossless archive mapping plus quarantine policy.
2. Keep archive formalizations non-executable by default.
3. Accept declared evidence basis with explicit uncertainty, or require source-by-source verification.
4. Choose strict adapter payloads versus a new schema version.
5. Keep current dependency policy: stdlib/JSON/current local dependencies only.
6. Confirm Hermes integration remains deferred until standalone gates pass.
