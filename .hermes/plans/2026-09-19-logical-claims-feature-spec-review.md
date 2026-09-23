# Scholastic Context Engineering — Feature Specification Review

> Draft for owner discussion. This document freezes neither implementation nor Kanban work. No cards should be created until each feature has an accepted scope, contract, and proof gate.

**Baseline:** verified standalone pipeline at `3362eaa`; clean-clone verification reported `209 passed, 0 failed`.

**New source material:** `Logical_Claims_Conversation-2.zip`; corpus contains 110 records, 50 sources, and 8 cross-cutting dimensions. Historical terminology, editorial examples, scholarly references, and modern reconstructions must remain distinguishable.

## Shared specification rules

Every feature must:

- begin with an independent failing test;
- use versioned typed inputs/outputs;
- preserve stable IDs, run IDs, source spans, provenance, status, confidence, uncertainty, and diagnostics;
- reject or abstain on malformed, stale, unsupported, ambiguous, contradictory, uncited, or over-budget input;
- preserve raw evidence and write repairs as new versioned artifacts;
- add no runtime dependency without separate security and owner approval;
- have separate implementation, adversarial review, and final verification workers;
- produce RED, GREEN, review, checkpoint, and commit evidence.

---

## S0 — Baseline release gate

**Status:** Existing capability; not a new feature card.

**Purpose:** Establish the repeatable proof gate before extending the pipeline.

**Inputs:** repository, contracts, fixtures, checkpoints, manifests.

**Outputs:** release verification record and checkpoint.

**Must prove:** clean-clone setup, full suite, canonical envelopes, exact spans, deterministic reruns, hostile-input behavior, dependency scope, checkpoint freshness, intended-only diff.

**Non-goals:** CI migration, deployment, Hermes integration, new runtime behavior.

**Open question:** Should this become a reusable local verification script, or remain a documented gate?

---

## S1 — Historical corpus adapter

**Purpose:** Import the supplied logical-claims JSON as evidence-bearing local data without treating it as executable semantics.

**Inputs:** archive manifest, archive SHA-256, corpus JSON, declared corpus schema.

**Outputs:** versioned `HistoricalCorpusSnapshot` or quarantined-record report.

**Required fields:** corpus ID/version, archive hash, record ID, family, record kind, historical context, native terms, template, formalization status, example status, interpretation note, source refs, related records, evidence basis.

**Invariants:** exactly 110 records and 50 sources for this snapshot; unique IDs; valid foreign keys; all eight dimensions retained; no silent field flattening; unmappable records quarantined.

**Tests:** duplicate/missing IDs, stale archive hash, missing source refs, unsupported record kinds, round-trip payload equality, quarantine counts, representative records across dimensions.

**Non-goals:** DOCX parsing, OCR, web retrieval, LLM extraction, semantic interpretation, source redistribution.

**Decision:** approve exact lossless mapping and quarantine policy.

---

## S2 — Corpus source/evidence ledger

**Purpose:** Make corpus support auditable without overstating source authority.

**Inputs:** source inventory, corpus source references, archive manifest.

**Outputs:** versioned `CorpusEvidenceLedger`.

**Required distinctions:** primary text, primary translation, ancient testimony translation, scholarly reference, editorial composition, unresolved support.

**Invariants:** source identity is separate from authority; a URL does not imply direct inspection; evidence basis cannot be upgraded automatically; every imported record has either valid source links or explicit abstention/quarantine.

**Tests:** forged source IDs, duplicate source keys, stale archive hash, unsupported evidence basis, omitted citations, sampled audit across all eight dimensions.

**Non-goals:** web verification, citation ranking, automatic authority scoring, citation-manager integration.

**Decision:** accept declared evidence basis with abstention, or require source-by-source verification before import.

---

## S3 — Taxonomy snapshot and disposition

**Purpose:** Define which corpus records are executable leaves, metadata-only entries, or unresolved bundles.

**Inputs:** corpus snapshot, approved taxonomy manifest, taxonomy policy.

**Outputs:** versioned `TaxonomySnapshot` and disposition records.

**Disposition values:** executable candidate, enrichment-only, metadata-only, unresolved, rejected.

**Invariants:** snapshot identity and source hash bind to every taxonomy match; headings and caveats cannot become leaves; unresolved bundles cannot be coerced; labels never overwrite native terminology or historical context.

**Tests:** stale snapshot rejection, heading conversion rejection, ambiguous bundle abstention, taxonomy/provenance mismatch, stable ID and hash checks.

**Non-goals:** ontology merger, automatic classification, taxonomy redesign, truth inference.

**Decision:** freeze the supplied taxonomy manifest as authority or create a reviewed vNext manifest.

---

## S4 — Corpus-aware extraction extension

**Purpose:** Extend deterministic extraction only for explicitly authorized logical forms.

**Inputs:** `StructuredDocument`, `TaxonomySnapshot`, corpus disposition.

**Outputs:** multi-annotation `ExtractionBundle` with typed propositions/operators and source spans.

**Invariants:** multiple dimensions may annotate one claim; every annotation links to taxonomy and source evidence; formalization status survives; unsupported forms abstain; no premise reconstruction; no historical label becomes a modern claim by default.

**Initial candidate forms:** A/E/I/O categorical forms, genus/species relation, definition pattern, selected argument schemas.

**Tests:** accepted canaries, unsupported forms, ambiguous forms, exact spans, multiple annotations, provenance mismatch, historical-vs-modern reconstruction separation.

**Non-goals:** full natural-language parsing, universal cross-tradition grammar, LLM extraction, all 110 records in one pass.

**Decision:** approve the first explicitly executable record kinds.

---

## S5 — Formalization and validation tiers

**Purpose:** Separate reviewable formal sketches from executable semantics.

**Inputs:** argument unit, taxonomy match, formalization metadata, semantic authority manifest.

**Outputs:** `ValidationResult` with status, assumptions, proof obligations, and diagnostics.

**Status values:** `VALID`, `INVALID`, `UNKNOWN`, `UNSUPPORTED`, `ILL_POSED`.

**Invariants:** historical or disputed reconstructions remain `UNKNOWN`/`UNSUPPORTED` unless explicitly authorized; empty-class, scope, modality, and existence assumptions are explicit; enrichment never upgrades validation.

**Tests:** empty-class assumptions, modal-scope ambiguity, invalid formalization, missing authority, accidental enrichment-to-proof upgrade.

**Non-goals:** theorem prover, modal logic engine, historical semantics simulator, automatic truth assessment.

**Decision:** keep all archive formalizations non-executable by default or approve named semantic authorities.

---

## S6 — Deterministic corpus retrieval/evaluation

**Purpose:** Make imported logical-claim records discoverable through the existing bounded retrieval boundary.

**Inputs:** corpus/taxonomy/evidence snapshots, retrieval request, graph snapshot.

**Outputs:** deterministic `RetrievalContext` with record/source citations.

**Invariants:** stable IDs/order; exact source and revision citations; hard input/output budgets; stale/forged/unsupported records refuse; prompt-like corpus text remains inert; frequency is not truth or entailment.

**Tests:** labeled query fixtures, stable tie ordering, stale records, forged snapshots, budget overflow, empty results, prompt injection, repeated clean runs.

**Non-goals:** embeddings, vector DB, GraphRAG, learned ranking, generation-quality claims, cloud retrieval.

**Decision:** define the minimal retrieval query vocabulary: text, taxonomy ID, dimension, tradition, source, relation, or combinations.

---

## S7 — Weight projection and community enrichment

**Purpose:** Provide optional navigation metadata over accepted edge occurrences.

**Inputs:** `GraphSnapshot`, projection configuration.

**Outputs:** versioned `WeightProjection` and/or `CommunitySnapshot`.

**Invariants:** deterministic; graph-revision bound; source occurrences remain unchanged; community/weight metadata cannot upgrade validation, truth, historical influence, or entailment status.

**Tests:** duplicate occurrence behavior, deterministic projection, revision mismatch, configuration bounds, no-validation-upgrade property.

**Non-goals:** learned ranking, centrality-as-truth, historical influence inference, graph database migration, probabilistic semantics.

**Decision:** defer until corpus retrieval demonstrates a concrete navigation need.

---

## S8 — Retry, idempotency, and partial-run recovery

**Purpose:** Make stage execution safe to retry or resume without duplicate or missing records.

**Inputs:** run manifest, stage input/output manifests, checkpoint, prior partial artifacts.

**Outputs:** deterministic stage artifacts, resume report, idempotency record.

**Invariants:** same input manifest and stage version produce the same output; retries do not duplicate records; partial outputs are explicit; incompatible artifacts fail closed; no silent recovery or coercion.

**Tests:** interrupted ingestion, repeated extraction, duplicate delivery, missing artifact, stale checkpoint, changed input hash, resumed run equality, no missing/duplicate records.

**Non-goals:** distributed queue, cloud orchestration, exactly-once claims outside the local artifact boundary.

**Decision:** define the authoritative run-manifest location and whether artifact retention is append-only or replace-by-version.

---

## S9 — Benchmark and evaluation leakage controls

**Purpose:** Ensure evaluation measures generalization rather than fixture memorization or source leakage.

**Inputs:** benchmark manifest, source IDs, train/evaluation partitions, retrieval/generation outputs.

**Outputs:** leakage report and benchmark result manifest.

**Invariants:** source and near-duplicate separation; no evaluation record appears in retrieval context unless policy allows it; benchmark versions and hashes are bound; unsupported cases are scored as abstention, not failure-free omission.

**Tests:** duplicate-source detection, near-duplicate fixture, contaminated retrieval snapshot, benchmark version mismatch, missing-result accounting.

**Non-goals:** model leaderboard, external benchmark downloads, statistical claims before corpus policy is frozen.

**Decision:** choose source-level, record-level, or temporal split policy.

---

## S10 — Hermes integration seam

**Purpose:** Define a future adapter without changing Hermes core or moving canonical ownership.

**Inputs:** standalone versioned IR and provenance contract.

**Outputs:** documentation-only handoff contract initially.

**Invariants:** standalone repository remains authority; no duplicate IR; retrieved text remains untrusted; no credentials/tools/policy mutation; integration cannot bypass standalone release gates.

**Tests before implementation:** immutable handoff, provenance preservation, schema mismatch refusal, prompt-injection isolation.

**Non-goals:** MCP tool, plugin, scheduler, browser surface, Hermes-core modification, cross-repository storage.

**Decision:** keep deferred until standalone corpus and retrieval gates pass.

---

## Proposed discussion order

1. Approve shared rules and S0 baseline assumption.
2. Decide S1–S3 data authority and quarantine policy.
3. Decide whether S4/S5 are in the next release or remain deferred.
4. Define S6 retrieval query vocabulary.
5. Decide whether S7 or S8 is the first post-corpus operational wave.
6. Decide benchmark split policy before any benchmark card is created.
7. Keep S10 deferred.

## Current status

- This is a specification review artifact only.
- No Kanban cards created.
- No production code changed.
- No commit or push performed for these specs.
