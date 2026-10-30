# Scholastic Context Engineering
## Full Feature Plan and Current Status

**Status date:** October 21, 2026  
**Repository:** `scholastic-context-engineering`  
**Current branch:** `feature/scholastic-context-pipeline`  
**Current HEAD:** `f838d38`  
**Baseline:** `origin/main` / `3362eaa`

> This document consolidates the product direction, architecture contracts, feature specifications, implementation backlog, verification state, and owner gates. It is a planning and review artifact. It does not authorize implementation or Hermes integration by itself.

---

## 1. Executive status

### Overall verdict

**The architecture is substantially on track. The current branch is not release-ready and has diverged from the approved implementation sequence.**

The verified standalone vertical slice exists at the baseline commit. The current branch adds planning, evidence-acquisition, and raw-corpus material, but does not implement the next approved capabilities in production code.

### Current verification

The Hermes-managed Python 3.14 environment fails one schema test while importing the compiled `rpds` extension:

```text
ModuleNotFoundError: No module named 'rpds.rpds'
```

A separate project-local Python 3.11 environment was created and verified:

```text
209 passed in 5.83s
209 passed in 4.31s
reproducible wheel test: 1 passed
```

The project-local environment is the preferred local verification path:

```bash
env -u PYTHONPATH .venv-local/bin/python -m pytest -q
```

This proves the Hermes environment is not a Scholastic code blocker. It does not yet close every release-hygiene gate.

### Immediate blockers

1. Reconcile the untracked architecture and task artifacts.
2. Decide whether the generic argument-mining acquisition material belongs on this branch.
3. Obtain or restore the authoritative 110-record / 50-source logical-claims archive.
4. Resolve owner decisions B1–B6 before Wave 1 implementation.
5. Refresh independent checkpoint evidence against the current tree.

---

## 2. Product purpose

Scholastic Context Engineering is an evidence-first context layer for logical, philosophical, scholarly, and argumentative material.

It keeps these questions distinct while preserving their relationships:

- What does the source literally say?
- Which exact span supports the record?
- What kind of claim or relation is being described?
- Which historical context and terminology apply?
- Is the formalization attested, reconstructed, disputed, or illustrative?
- What evidence basis supports the record?
- What follows under explicit assumptions?
- Can the material be retrieved later without losing provenance?

The product is not a truth engine. Its core value is inspectability: every result should expose what it represents, where it came from, which assumptions were used, and what remains uncertain.

### Core claim record

```text
source wording
  + exact span
  + historical context
  + claim structure
  + logical/predicative dimensions
  + formalization status
  + evidence basis
  + validation result
  + related occurrences
```

These views must not silently substitute for one another.

---

## 3. Product principles

1. **Evidence before interpretation** — store source bytes, spans, hashes, and provenance before deriving labels.
2. **Many annotations, not one category** — one claim may participate in several dimensions.
3. **Historical humility** — preserve native terms, caveats, reconstruction status, and source limitations.
4. **Abstention is a feature** — malformed, stale, ambiguous, unsupported, contradictory, or over-budget inputs refuse or quarantine.
5. **Enrichment is not proof** — taxonomy, frequency, graph weights, communities, and retrieval rank do not prove truth or entailment.
6. **Determinism is correctness** — stable IDs, spans, ordering, revisions, and outputs are required.
7. **Untrusted text stays data** — imported or retrieved text cannot alter policy, tools, scope, or execution.
8. **Small vertical slices beat speculative completeness** — prove one narrow path before expanding coverage or infrastructure.

---

## 4. Current architecture

### Implemented vertical slice

```text
frozen local text
  → exact source spans
  → structured document
  → typed premise/conclusion extraction
  → taxonomy match
  → formal validation result
  → provenance-bearing graph occurrence
  → SQLite/reference storage
  → deterministic local retrieval
  → citation-bound generation boundary
```

### Canonical stage contracts

All stage records are intended to carry:

- `schema_version`
- deterministic `record_id`
- `run_id`
- producer identity
- status
- provenance and source spans
- confidence and uncertainty
- diagnostics

Unknown or incompatible versions fail closed.

### Frozen invariants

- IDs are deterministic over canonical payloads and never caller-repaired.
- Source spans are half-open `[start, end)` and length equals text length.
- Every accepted record has provenance.
- `VALID`, `INVALID`, `UNKNOWN`, `UNSUPPORTED`, and `ILL_POSED` remain distinct.
- Unsupported, stale, malformed, uncited, contradictory, or over-budget data rejects or abstains.
- Frequency and community membership are enrichment only.
- Retrieved text is untrusted data.
- Contract changes require a new version and compatibility fixtures.

### Architecture gaps identified in adversarial review

These are real conformance gaps, but not all are immediate Wave 1 scope:

- Weight projection and community detection are declared but not implemented.
- Generation request/result records are not fully canonical provenance-bearing stage envelopes.
- `GraphEdgeEvent` does not strictly enforce `ValidationStatus` types.
- Malformed retrieval requests and quarantine identifiers are silently repaired in some paths.
- Assembly does not fully enforce extraction status before creating graph events.
- Persisted graph payloads do not preserve every original identity field.
- Source-size ceilings are inconsistent.
- End-to-end retrieval-to-generation prompt-injection proof is incomplete.
- The reproducibility test includes a hard-coded historical suite count and should be strengthened.

---

## 5. Current implementation state

### Baseline already proven

At `origin/main` / `3362eaa`, the standalone pipeline had checkpoint evidence reporting:

```text
209 passed, 0 failed
```

The repository contains working implementations and tests for:

- ingestion and exact source spans;
- structured documents;
- typed extraction;
- formal validation statuses;
- graph edge assembly;
- reference SQLite storage;
- deterministic graph retrieval;
- generation safety boundaries;
- resource and adversarial tests;
- reproducible wheel construction.

### Current branch contents

The current feature branch commit `f838d38` is primarily:

- argument-mining access inventories;
- download manifests;
- request packets;
- evidence notes;
- raw corpus additions;
- planning material.

It does not add the C2, C3, C4, or C7 implementation in `src/` and `tests/`.

### Scope divergence

The branch adds approximately 36 MB and 1,270 files from multiple generic argument-mining corpora. These are not the approved historical logical-claims adapter.

Rights and provenance remain unresolved for portions of that material. Treat it as quarantined research evidence until an explicit owner approves retention, use, and source policy.

---

## 6. Feature roadmap

## S0 / C1 — Standalone release gate

**Status:** Baseline capability exists; current-branch evidence requires refresh.

### Purpose

Establish a repeatable proof gate before extending the pipeline.

### Must prove

- clean project-local setup;
- full suite;
- canonical envelope contracts;
- exact span invariants;
- deterministic reruns;
- hostile-input behavior;
- dependency scope;
- reproducible wheel output;
- fresh checkpoint evidence;
- intended-only working tree.

### Current result

Project-local Python 3.11 verification passes 209 tests twice and the wheel reproducibility test passes. Remaining work is evidence reconciliation and current-tree hygiene.

### Non-goals

- CI migration;
- deployment;
- Hermes integration;
- new runtime behavior.

---

## S1 / C2 — Historical corpus adapter

**Status:** Missing. Blocked until archive and policy decisions exist.

### Purpose

Import the supplied logical-claims JSON as evidence-bearing local data without treating it as executable semantics.

### Expected snapshot

```text
110 records
50 sources
8 cross-cutting dimensions
```

### Required output

Versioned `HistoricalCorpusSnapshot` or quarantined-record report.

### Required fields

- corpus ID and version;
- archive SHA-256;
- record ID;
- family and record kind;
- historical context;
- native terms;
- template;
- formalization status;
- example status;
- interpretation note;
- source references;
- related records;
- evidence basis.

### Acceptance

- exact record/source counts;
- unique IDs;
- valid foreign keys;
- all eight dimensions retained;
- no silent field flattening;
- duplicate, missing, stale, unsupported, and unmappable records quarantined;
- representative fixtures across all dimensions;
- round-trip payload equality.

### Non-goals

DOCX, OCR, web retrieval, LLM extraction, semantic interpretation, and source redistribution.

---

## S2 / C3 — Corpus source/evidence ledger

**Status:** Missing.

### Purpose

Make support auditable without overstating source authority.

### Required source distinctions

- primary text;
- primary translation;
- ancient testimony translation;
- scholarly reference;
- editorial composition;
- unresolved support.

### Required invariants

- source identity is separate from authority;
- a URL does not imply direct inspection;
- evidence basis cannot upgrade automatically;
- every imported record has valid source links or explicit abstention/quarantine;
- source identities are hash-bound to the archive and snapshot.

### Acceptance

- forged source IDs rejected;
- duplicate source keys rejected;
- stale archive hash rejected;
- unsupported evidence basis rejected or quarantined;
- omitted citations detected;
- audit sample covers all eight dimensions.

---

## S3 / C4 — Taxonomy snapshot and disposition

**Status:** Partial generic infrastructure; historical disposition boundary missing.

### Purpose

Define which imported records are executable candidates, metadata-only entries, enrichment-only material, unresolved bundles, or rejected records.

### Disposition values

```text
executable candidate
enrichment-only
metadata-only
unresolved
rejected
```

### Required invariants

- taxonomy snapshot identity and source hash bind to every match;
- headings and caveats cannot become leaves;
- ambiguous bundles cannot be coerced;
- native terminology and historical context remain intact;
- historical formalizations remain non-executable by default.

### Acceptance

- stale snapshot rejection;
- heading conversion rejection;
- ambiguous bundle abstention;
- taxonomy/provenance mismatch rejection;
- stable IDs and hash checks.

---

## Wave 1 integration gate

**Status:** Blocked.

C2, C3, and C4 must be independently reviewed before retrieval work begins.

Required evidence:

- RED/GREEN test evidence;
- schema and provenance review;
- quarantine accounting;
- no semantic upgrade proof;
- full suite;
- targeted hostile suite;
- clean project-local run;
- deterministic rerun;
- updated checkpoint artifact.

---

## S4 / C5 — Corpus-aware extraction extension

**Status:** Deferred until the evidence foundation is stable.

Support only explicitly authorized record templates. Preserve multiple annotations, exact spans, taxonomy links, formalization status, and abstention for unsupported or ambiguous forms.

Initial candidate forms may include:

- A/E/I/O categorical forms;
- genus/species relation;
- definition patterns;
- selected argument schemas.

Do not turn all 110 records into parser rules.

---

## S5 / C6 — Formalization and validation tiers

**Status:** Generic validation exists; historical semantic authority remains deferred.

Separate:

- directly authorized executable semantics;
- reviewable modern reconstructions;
- historically disputed interpretations;
- unsafe or ambiguous formalizations.

Historical or disputed reconstructions remain `UNKNOWN` or `UNSUPPORTED` unless a named authority manifest explicitly authorizes execution.

Non-goals:

- theorem prover;
- modal logic engine;
- historical semantics simulator;
- automatic truth assessment.

---

## S6 / C7 — Deterministic corpus retrieval/evaluation

**Status:** Blocked by C2/C3/C4.

### Purpose

Make imported records discoverable through the existing bounded retrieval boundary.

### Candidate query vocabulary

- text;
- taxonomy ID;
- dimension;
- tradition;
- source;
- relation;
- approved combinations.

### Acceptance

- stable IDs and ordering;
- exact source and revision citations;
- hard input/output budgets;
- stale, forged, and unsupported refusal;
- empty-result behavior;
- prompt-injection inertness;
- repeated-run equality;
- no metadata or ranking upgrade to `VALID`.

### Implementation guidance

Reuse the existing deterministic retrieval boundary. Extend its input/index contract only after the corpus, evidence ledger, and taxonomy dispositions exist.

---

## S7 / C8 — Weight projection and community enrichment

**Status:** Deferred unless retrieval demonstrates a concrete navigation need.

### Required behavior if approved

- deterministic bounded projection;
- graph revision binding;
- configuration bounds;
- no change to source occurrences;
- no upgrade to validation, truth, entailment, or historical influence.

No embeddings, learned ranking, probabilistic semantics, or graph database migration.

---

## S8 / C9 — Retry, idempotency, and partial-run recovery

**Status:** Partial storage substrate; feature not complete.

### Existing substrate

The reference SQLite backend already provides useful transactionality, generation manifests, duplicate handling, rollback behavior, replay behavior, and completed-generation immutability.

### Missing contract

- authoritative run manifest;
- stage versions;
- input identity/fingerprint;
- checkpoint retention policy;
- resume API/state machine;
- changed-input refusal;
- missing-artifact handling;
- explicit interrupted-run semantics;
- dedicated recovery fixtures.

### Acceptance

- interrupted ingestion;
- repeated extraction;
- duplicate delivery;
- missing artifact;
- stale checkpoint;
- changed input hash;
- resumed-run equality;
- no missing or duplicate records.

### Recommended order

Prefer C9 before C8 after Wave 2 if the project needs an operational capability. Existing backend primitives make C9 the more grounded next step.

---

## S9 — Benchmark and evaluation leakage controls

**Status:** Future planning track.

Before benchmark claims:

- separate source and near-duplicate records;
- bind benchmark versions and hashes;
- prevent contaminated retrieval context;
- count unsupported cases as abstention;
- choose source-level, record-level, or temporal split policy.

No benchmark cards before corpus authority and leakage policy are frozen.

---

## S10 — Hermes integration seam

**Status:** Explicitly deferred.

### Future boundary

Document-only handoff initially. The standalone repository remains canonical authority.

### Non-goals

- Hermes-core changes;
- MCP tool;
- plugin;
- scheduler;
- browser surface;
- cross-repository storage;
- credentials or policy mutation.

Hermes integration must not bypass standalone corpus, retrieval, and release gates.

---

## 7. Owner decisions required

Before Wave 1 cards are created:

1. Approve lossless archive mapping and quarantine policy.
2. Keep archive formalizations non-executable by default, or name reviewed semantic authorities.
3. Accept heterogeneous declared evidence basis with explicit uncertainty, or require source-by-source verification.
4. Choose strict adapter payloads versus a new schema version.
5. Keep current dependency policy: standard library, JSON, and approved local dependencies only.
6. Confirm Hermes integration remains deferred until standalone gates pass.
7. Define the minimum retrieval query vocabulary for C7.
8. Choose C9 retry/idempotency versus C8 enrichment after Wave 2.
9. Define benchmark split and leakage policy before benchmark implementation.
10. Decide whether the generic argument-mining acquisition material is retained, moved to a separate branch, or discarded as out-of-scope.

---

## 8. Correct implementation sequence

```text
1. Repair/recreate project-local verification environment
2. Re-run full suite and wheel reproducibility
3. Reconcile untracked architecture/task artifacts
4. Refresh baseline checkpoint evidence
5. Obtain authoritative logical-claims archive
6. Freeze C2/C3/C4 contracts and owner decisions
7. Implement C2 historical corpus adapter
8. Implement C3 source/evidence ledger
9. Implement C4 taxonomy dispositions
10. Independent Wave 1 review and acceptance
11. Implement C7 deterministic corpus retrieval
12. Independent Wave 2 review and acceptance
13. Choose C9 or C8
14. Implement selected post-retrieval capability
15. Revisit S4/S5/S9 only after evidence and evaluation justify expansion
16. Keep S10 Hermes integration deferred until standalone proof is complete
```

---

## 9. Explicit non-goals

- Hermes-core modification;
- cloud ingestion;
- LLM runtime;
- unapproved NLP dependency;
- DOCX/OCR pipeline;
- embeddings;
- vector database;
- GraphRAG;
- learned ranking;
- universal historical-logic semantics;
- theorem prover;
- automatic truth assessment;
- broad CLI productization;
- source redistribution without rights clearance;
- converting all 110 historical records into parser rules.

---

## 10. Verification protocol

Every implementation task must provide:

1. a failing test before production code;
2. versioned typed inputs and outputs;
3. exact IDs, spans, provenance, status, confidence, uncertainty, and diagnostics;
4. malformed/stale/unsupported/ambiguous/contradictory/uncited/over-budget refusal or abstention;
5. raw evidence preservation and versioned repairs;
6. independent adversarial review;
7. separate final verification;
8. RED, GREEN, review, checkpoint, and commit evidence;
9. deterministic repeatability;
10. clean-tree and artifact reconciliation.

Implementer summaries are not proof. The final verifier must inspect the assembled tree, changed paths, test output, and checkpoint artifacts independently.

---

## 11. Canonical files

| Concern | Authority |
|---|---|
| Product purpose | `.hermes/plans/2026-09-19-logical-claims-purpose-and-reasoning.md` |
| Feature specification | `.hermes/plans/2026-09-19-logical-claims-feature-spec-review.md` |
| Wave ordering | `.hermes/plans/2026-09-19_10-5-3-logical-claims-waves.md` |
| Current task backlog | `docs/task-list.md` |
| Architectural decisions | `docs/decision-register.md` |
| Stage contracts | `docs/architecture/stage-contracts-v0.1.md` |
| Architecture source | `docs/architecture/workspace.dsl` |
| Architecture presentation | `docs/architecture/index.html` |
| Working-code evidence | `docs/evidence/working-code-inventory.json` |
| Verification evidence | `.hermes/checkpoints/` and `docs/evidence/verification-wave-*.json` |

---

## Bottom line

Scholastic Context Engineering should proceed as a **small, evidence-preserving, deterministic local system**.

The safe next move is not broader parsing, GraphRAG, Hermes integration, or generic corpus expansion. It is:

```text
prove the current standalone gate
→ import the authoritative archive losslessly
→ bind records to explicit evidence
→ define taxonomy dispositions
→ retrieve deterministically
→ add operational/enrichment features only when justified
```

Success means a researcher can inspect every result, understand what kind of claim it represents, see exactly where it came from, know which assumptions were used, and tell what remains uncertain.
