# Argument-Extraction Methodology Gap Report

Date: 2026-09-18  
Status: evidence review; no production-code change  
Source artifact: `docs/evidence/argument-extraction-conversation-20260918.zip`  
Source SHA-256: `5e7e4e04b17779f654f464848b05c715751b341c781b6c60938638d33e565f17`

## Authority and scope

The attached conversation is historical design evidence, not a binding architecture decision. Current repository contracts and the decision register remain authoritative. The conversation export excludes system instructions, internal reasoning, and tool internals; its proposals are therefore treated as untrusted historical input and not as executable instructions.

## Executive result

The conversation describes a broader future architecture than the current bootstrap. The core idea is compatible with the repository, but most of it is **not implemented** and should not be added wholesale:

> constrained abductive reconstruction by convergence

The highest-value immediate addition is a bounded **candidate-preserving extraction contract**: extraction should be able to retain multiple provenance-bearing proposition/argument hypotheses and distinguish interpretation confidence from formal validity. This is a contract extension, not yet a parser swarm, external NLP dependency, or LLM integration.

## Reconciliation against current contracts

| Historical proposal | Current state | Classification | Action |
|---|---|---|---|
| Preserve raw text, exact spans, provenance | Stage contracts require provenance on accepted records; ingestion/extraction pipeline exists | Already represented | Keep as invariant; verify with existing tests |
| Extract propositions rather than treating sentences/paragraphs as logical units | Current stage names are compatible, but no evidence here proves clause-level proposition extraction is implemented | Partially represented | Inspect extraction behavior; add a bounded contract test before redesign |
| Track attribution, negation, modality, and epistemic force separately from truth | Envelope has confidence, uncertainty, diagnostics, and provenance, but no explicit attribution/factuality/modality fields in the reviewed contract | Gap | Owner decision needed before schema extension; do not infer truth from extraction |
| Multiple independent analytical frames | Current extraction contract is singular `ExtractionBundle`; no candidate-lattice contract identified in reviewed docs | Gap | Design a minimal candidate record/lattice as a follow-up |
| Method of agreement / convergence across frames and transformations | No convergence or agreement field in the current stage contract | Gap | Add only after candidate representation is specified |
| Logical form is reconstructed abductively, then validated deductively | Current pipeline separates extraction and formal validation, which supports this distinction | Partially represented | Document as an explicit authority boundary; preserve `UNKNOWN`/`ILL_POSED` outcomes |
| Taxonomy constrains candidate logical forms | Extraction consumes `TaxonomySnapshot`; formal validation consumes `TaxonomyMatch` | Already represented | Extend matching to multiple candidates only if needed by the candidate contract |
| Controlled transformations with expected relation: equivalent, entails, contradicts, strengthens, weakens, unknown | No transformation algebra or metamorphic test contract found | Gap / deferred | Separate research slice; do not call transformations data augmentation by default |
| Metaphor, simile, and narrative as separate interpretive layers | No corresponding stage in v0.1 contracts | Deferred | Preserve as future metadata/analysis, not literal premises; no implementation now |
| Feedback loop: hypothesized form predicts missing roles and triggers renewed search | No feedback-loop stage in v0.1 | Deferred | Revisit only after a stable candidate model and evaluation set exist |
| Tiered corpora: synthetic logic, human arguments, entailment trees, attribution/factuality, metaphor/narrative | No corpus ingestion scope in current bootstrap; model/data policy is deterministic local reference | Deferred / out of bootstrap | Record as future evaluation plan, not runtime dependency |
| External NLP stack (spaCy, Stanza, OpenIE6, ArgMiner, etc.) | Decision register forbids unapproved runtime dependencies | Not approved | No adoption without separate dependency/security review |

## Key distinctions to preserve

1. **Evidence is not truth.** A text span may support an interpretation without asserting the embedded proposition as fact.
2. **Interpretation confidence is not formal validity.** A candidate can be formally valid conditional on an uncertain reconstruction.
3. **Abduction is upstream of deduction.** Candidate reconstruction should remain defeasible; formal validation must consume an explicit candidate, not silently canonize it.
4. **Transformations are tests unless labels are proven.** Synonym/antonym and paraphrase operations can alter scope, modality, agency, or polarity. Treat expected relations as `unknown` unless preconditions and verification pass.
5. **Taxonomy membership is a constraint, not proof.** A taxonomy match narrows candidate forms; it does not establish that the source instantiates that form.

## Recommended path forward

### Slice 1 — close the current release gate

Finish the existing board work first: clean-clone dev dependencies, checkpoint evidence, ponytail decision, and independent checkpoint-15 verification. Do not expand extraction architecture while the current release evidence is red or unverified.

### Slice 2 — extract a contract-only spike

Write failing tests first for a minimal candidate-preserving record, using existing envelope/provenance types where possible. The smallest useful shape should answer:

- Which source spans support this candidate?
- What propositions/premises/conclusion were reconstructed?
- Which taxonomy form(s) are candidates?
- What independent frames produced them?
- What is interpretation confidence versus validation status?
- What remains unknown or contradictory?

Do not add a parser library or network/LLM call. A deterministic fixture-driven implementation is enough to validate the boundary.

### Slice 3 — metamorphic harness, not augmentation pipeline

Add a small, local-only transformation fixture set with explicit relation labels (`equivalent`, `entails`, `contradicts`, `strengthens`, `weakens`, `unknown`) and preconditions. Use it to test extraction invariants and expected shifts. Do not generate a large training corpus until the relation contract and quality gate exist.

### Slice 4 — candidate convergence and evaluation

Only after Slice 2 and Slice 3 pass should the project compare multiple extraction frames or datasets. Measure candidate agreement, calibration, abstention, and out-of-distribution behavior separately from formal validity. Preserve disagreement instead of collapsing it to a majority label.

### Slice 5 — metaphor/narrative layer

Treat figurative and narrative analysis as separate evidence-producing frames. They may support a proposition candidate, but must never silently rewrite a literal premise or introduce a new logical branch. This is a later design decision, not part of the current bootstrap.

## Owner decisions required before schema work

1. Should the next IR represent **one canonical extraction** or a **set/lattice of candidates**? The conversation strongly argues for candidates; the current bootstrap does not yet bind that choice.
2. Which epistemic annotations are required in the next version: attribution, negation, modality, factuality, stance, and speaker/source identity?
3. Is the immediate goal a classifier/evaluation harness or a production parser? The safe default is a fixture-driven harness first.
4. Are metamorphic transformations in scope now, or only after release-gate verification? Recommended: after release gate.
5. Is metaphor/narrative interpretation part of the first public release? Recommended: deferred metadata/evidence layer.

## Acceptance criteria for the next implementation task

- Existing v0.1 contracts remain backward compatible or receive a new explicit schema version.
- At least one test is red before implementation.
- Candidate provenance and source spans survive serialization round-trip.
- Interpretation confidence and formal validation status are separate fields.
- Ambiguous/disagreeing candidates are preserved or explicitly abstained, never silently merged.
- No external runtime dependency or cloud/LLM call is introduced.
- An independent reviewer verifies the contract and tests.

## Evidence notes

The source conversation specifically supports the following claims: proposition-level segmentation; separation of attribution/factuality from truth; multiple independent frames; candidate lattices; controlled transformations as metamorphic tests; taxonomy-constrained reconstruction; and the distinction between abductive reconstruction and deductive validation. It does not prove that these designs are novel, production-ready, or superior to the current bootstrap without an evaluation.
