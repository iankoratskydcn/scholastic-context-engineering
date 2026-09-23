# Scholastic Context Engineering — Logical Claims 10-5-3 Wave Plan

> Discussion-only planning artifact. Do not create Kanban cards or implement until owner review approves the shortlist, wave boundaries, and blockers.

**Goal:** Extend the verified standalone evidence-first pipeline with corpus-backed logical-claims capabilities without converting historical material into unreviewed executable semantics.

**Baseline:** `3362eaa`; clean-clone verification reported `209 passed, 0 failed`. Archive: `Logical_Claims_Conversation-2.zip`; 110 records, 50 sources, 8 dimensions.

## 10 candidates

| ID | Capability | Narrow scope | Primary proof |
|---|---|---|---|
| C1 | Standalone release gate | Repeatable schema, contract, security, reproducibility, checkpoint, and clean-clone gate | Fresh clone + full suite + checkpoint audit + independent review |
| C2 | Quarantined historical corpus adapter | Import supplied JSON corpus without flattening caveats or semantics | Exact hash/counts, round-trip fixtures, quarantine accounting |
| C3 | Corpus source/evidence ledger | Hash-bound source inventory and claim/source links | Foreign-key, source-class, stale-hash, and citation omission tests |
| C4 | Taxonomy snapshot/disposition boundary | Versioned leaves, metadata-only headings, unresolved bundles | Snapshot identity, stale rejection, disposition and abstention fixtures |
| C5 | Corpus-aware extraction extension | Support only explicitly authorized record templates | Accepted/abstained/quarantined canaries with span/provenance |
| C6 | Formalization/validation tiers | Separate reviewable sketches from executable semantics | Empty-class, scope, invalid-form, and no-upgrade tests |
| C7 | Corpus retrieval/evaluation fixture | Deterministic retrieval over imported records | Stable IDs/order, budgets, citations, stale/injection refusal |
| C8 | Weight projection/community enrichment | Bounded non-probative graph metadata | Revision binding and no-validation-upgrade proof |
| C9 | Retry/idempotency and partial-run recovery | Deterministic rerun, resume, and duplicate handling at stage boundaries | Interrupted-run fixtures, replay equality, no duplicate records |
| C10 | Deferred Hermes seam | Document future handoff only; no integration code | Versioned boundary contract; owner gate before implementation |

## 5-item shortlist

1. **C2 — Quarantined historical corpus adapter**
2. **C3 — Corpus source/evidence ledger**
3. **C4 — Taxonomy snapshot/disposition boundary**
4. **C7 — Corpus retrieval/evaluation fixture**
5. **C8 — Weight projection/community enrichment, deferred behind evidence**

C1 is already proven by checkpoint 15 and remains a release gate for every future wave, not a new implementation card. Excluded from immediate implementation: broad extraction, executable formal semantics, CLI productization, and Hermes integration.

## 3 implementation waves

### Wave 1 — Import archive as evidence, not semantics

**Cards:** C2, C3, C4. These are serial/partially parallel only after their adapter contracts are frozen. The existing C1 baseline gate must pass before dispatch.

**Baseline gate:** clean-clone verification, canonical envelope/provenance audit, adversarial security suite, checkpoint consistency, independent review, and no unapproved dependency changes.

### Wave 2 — Deterministic retrieval payoff

**Card:** C7. It depends on the archive adapter, source ledger, and taxonomy disposition boundary.

**Required behavior:**

- exact archive checksum;
- 110-record and 50-source accounting;
- source foreign-key integrity;
- preservation of all 8 dimensions;
- historical context, native terminology, evidence basis, and formalization status preserved;
- headings/caveats remain metadata-only;
- unresolved bundles quarantine or abstain;
- no historical record becomes `VALID` merely by parsing;
- no DOCX parsing, OCR, web crawling, LLM tooling, solver, or new runtime dependency.

**Gate:** independent review confirms no schema/provenance loss and no conversion of historical reconstruction into executable semantics.

### Wave 3 — Optional graph enrichment, only after evidence

**Card:** C8, gated behind explicit owner approval and successful Waves 1–2.

**Required behavior:**

- bounded deterministic weight projection and/or community snapshot;
- graph revision binding;
- enrichment status cannot upgrade validation or truth status;
- repeated clean runs are byte-identical.

**Stop condition:** if Waves 1–2 do not demonstrate a concrete navigation need, defer C8. No embeddings, vector search, GraphRAG, broad CLI, Hermes integration, cloud/model retrieval, or learned ranking.

## Blocking owner decisions

- **B1:** Approve lossless archive-to-canonical mapping and quarantine policy.
- **B2:** Keep archive formalizations non-executable unless a named reviewed authority manifest authorizes otherwise.
- **B3:** Accept heterogeneous declared evidence basis with abstention, or require source-by-source verification before import.
- **B4:** Decide whether adapter payloads are separately strict while the current envelope remains extensible, or version/tighten schemas first.
- **B5:** Keep JSON/stdlib/current dependencies only, or authorize a separate dependency/security review.
- **B6:** Maintain Hermes integration deferral until standalone gates pass.

## Card contract for later creation

Every eventual Kanban card must include: source ID, objective, dependencies, exact target files, RED test, GREEN behavior, acceptance proof, non-goals, risks, stop conditions, worktree/branch rule, independent review requirement, checkpoint artifact, and Conventional Commit requirement.

## Current decision request

Approve/revise:

1. the 5-item shortlist;
2. the 3-wave order;
3. the archive mapping/quarantine policy;
4. the evidence-basis policy;
5. whether Wave 3 should be retrieval or retry/idempotency instead.

No Kanban cards have been created from this plan.
