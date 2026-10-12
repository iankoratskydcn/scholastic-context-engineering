# Adversarial relevance review B

**Scope.** Reviewed exactly the 18 identity-passing rows in `finalized_v1_1/aggregate_top20_identity_status.csv`. Excluded identity-failed `18_03` and `18_02`. The review used the strongest locally available evidence under `verification_runs/20261012_shard*/evidence/`, reading full PDFs where present and the complete available landing/abstract artifacts otherwise. No ranking, identity, or source artifacts were edited.

## Adjudication rule

A paper is **retain_high** only when the available evidence demonstrates an exact pipeline stage or a direct novelty threat: source-span/component extraction, typed argument/form classification, prover-backed premise selection, or inspectable argumentative claim verification. **retain_mid** means a useful formal/protocol/proof-skeleton transfer but no demonstrated selection/extraction/compression interface. **demote** means background, pedagogy, survey, or generation work whose mechanism is materially outside this pipeline. **insufficient_evidence** is fail-closed when the local artifact cannot support a mechanism judgment.

Hostile countertests were applied against title/category fit, prestige, benchmark status, and recency. These were never treated as mechanism evidence. Formal argumentation was separated from natural-language extraction; formal premise retrieval was separated from prose context compression; historical/protocol relevance was separated from operational pipeline evidence.

## Results

| verdict | count |
|---|---:|
| retain_high | 7 |
| retain_mid | 8 |
| demote | 2 |
| insufficient_evidence | 1 |
| false_positive | 0 |
| **reviewed** | **18** |

### Retain high

- `S21P02` — argumentative LLMs construct formal, contestable claim-verification frameworks.
- `S21P05` — raw debate text to fuzzy argument knowledge base with typed support/attack relations and queryable semantics.
- `S10P10` — scheme-conditioned LLM translation from natural-language arguments to computational representations; medium confidence because only abstract metadata is locally available.
- `S10P05` — practical scheme annotation assistant for structured span/form labeling.
- `S21P07` — explicit premise/claim/major-claim spans and typed support/attack relations from persuasive text.
- `S08P06` — prover-in-the-loop proof-step and relevant-premise selection with Lean checking; high but stage-bounded to formal premises.
- `S10P04` — scheme-aware scientific-discourse mining that extracts scheme names, premises, and implicit/explicit conclusions; medium confidence because only abstract metadata is locally available.

### Retain mid

`18_04`, `18_05`, `S23P01`, `S21P06`, `18_09`, `18_01`, `18_08`, and `S24P02` are relevant formal, protocol, generation, or cross-tradition precedents, but do not demonstrate the full source-to-selection/compression-to-proof interface. They should not be described as direct context-selector evidence.

### Demote or block

- `18_06` — **insufficient_evidence**: local artifact is only a redirect/locator page; canonical Carneades relevance is plausible, but fail closed without full text.
- `S21P10` — **demote**: Socratic/fallacy tutoring and pedagogy, not source extraction, dependency preservation, or proof validation.
- `18_13` — **demote**: AI-and-law historical/survey lineage, not an operational mechanism.

## Main adversarial findings

1. The strongest exact overlaps are front-end argument mining (`S21P07`, `S10P04`, `S10P05`, `S10P10`), integrated structured claim verification (`S21P02`, `S21P05`), and prover-backed formal premise selection (`S08P06`).
2. Formal defeasible systems (`18_01`, `18_04`, `18_05`) are valuable proof-kernel and defeat-semantics precedents, but they presuppose symbolic inputs and do not mine open text or compress context.
3. Historical/formal dialogue and comparative logic (`S23P01`, `S24P02`) support protocol and proof-skeleton design, not retrieval or context-budget claims.
4. Generation and tutoring systems (`18_09`, `S21P06`, `S21P10`) must not be credited with source-preserving selection merely because outputs are argumentative or Socratic.
5. Abstract-only or landing-only evidence was confidence-capped and stated explicitly in the CSV. `18_06` was blocked rather than inferred from prestige or category placement.

## Evidence and output

The per-paper CSV records pipeline stages, demonstrated mechanism versus inference, exact overlap/threat, missing boundaries, verdict, confidence, and evidence file/page/section for all 18 rows:

`verification_runs/adversarial_relevance_reviewer_B.csv`

Review completed 2026-10-12. External web search was not used; this was an independent read of the repository's retrieved evidence artifacts.
