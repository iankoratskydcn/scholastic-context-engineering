# Adversarial relevance review A

**Scope.** Independent review of the 20 aggregate-top identities, restricted to the 18 rows with `identity_pass=True` in `finalized_v1_1/aggregate_top20_identity_status.csv`. Identity-failed `18_03` and `18_02` were excluded. The master matrix, aggregate identity status, rankings, and identity artifacts were not edited.

**Question applied.** Does the paper demonstrate a concrete mechanism for one or more stages of the target pipeline: source/span and claim extraction; cross-tradition argument/form classification; deductive or proof skeleton recovery; dependency/provenance-preserving context selection/compression; or downstream inspectable philosophical reasoning?

**Evidence rule.** Full text was preferred. Where only a scholarly landing page, abstract, or metadata capture was preserved, the verdict was bounded to that evidence and the item was demoted or marked `insufficient_evidence` when a positive judgment would require unavailable details. The CSV records exact evidence paths and page/section locations.

## Counts

| Metric | Count |
|---|---:|
| Identity-pass papers reviewed | 18 |
| `retain_high` | 6 |
| `retain_mid` | 6 |
| `demote` | 4 |
| `false_positive` | 0 |
| `insufficient_evidence` | 2 |
| `demote_or_block` (`demote` + `false_positive` + `insufficient_evidence`) | 6 |

## Retain high

- **S21P02 Freedman et al.** — direct argumentative-LLM/argumentation-framework and contestable claim-verification mechanism; strongest overlap is verification and attack/support structure, not compression or scholastic order.
- **S21P05 Alfano et al.** — raw-debate argument mining into fuzzy support/attack knowledge bases with quantitative semantics and logical querying; direct structured-reasoning threat, bounded away from provenance/compression.
- **S10P10 Trajano et al.** — abstract-level evidence supports scheme-conditioned LLM translation from natural-language arguments to computational arguments; direct novelty threat, but confidence is medium because only metadata/abstract was preserved.
- **S23P01 Uckelman** — full article provides an implementable formal dialogue account of medieval obligationes with alternating roles, rule-governed moves, and consistency goals; strong protocol precedent, not extraction/compression.
- **S21P07 Sazid et al.** — full paper explicitly labels spans/components and support/attack/for/against relations with evaluated unified and decoupled architectures; direct extraction-stage precedent.
- **S10P04 Green** — abstract-level evidence states logic-program argumentation schemes can extract scheme names, premises, and explicit/implicit conclusions from biomedical discourse; direct extraction/form-classification threat, bounded by narrow domain and medium confidence.

## Retain mid

- **18_04 Garcia & Simari** — DeLP dialectical defeat and warrant computation; strong formal reasoning substrate, no natural-language extraction or context engineering.
- **18_05 Verheij (2003)** — formal argumentation schemes embedded in dialectical legal logic; scheme/protocol semantics, no learned extraction or compression.
- **S21P06 Mitsuda et al.** — supplied argument structures condition dialogue generation; useful structure-to-language baseline, not source mining or proof validation.
- **18_01 Simari & Loui** — formal defeasible reasoning, specificity, warrant, termination, and implementation; foundational proof skeleton, not evidence-grounded NLP.
- **18_08 Verheij (2009)** — Toulmin/defeasible-scheme-to-AI conceptual bridge; useful taxonomy and boundary source, not an evaluated pipeline.
- **S10P05 Lawrence et al.** — annotation-assistant mechanism for scheme corpora; useful annotation/resource precedent, with abstract-only local evidence.

## Demote or block

- **18_06 Gordon, Prakken & Walton** — `insufficient_evidence`: preserved landing capture confirms title only; full model mechanism was not independently available.
- **S21P10 Shi et al.** — `demote`: Socratic fallacy tutoring is a neighboring pedagogical dialogue intervention, not extraction, proof, provenance, or compression.
- **18_09 Reisert et al.** — `insufficient_evidence`: ACL landing capture has an empty abstract and no preserved paper text; relevance depends on unavailable ranking-summary claims.
- **S08P06 Lean Copilot** — `demote`: formal proof-assistant integration is concrete but does not address natural-language evidence, argument forms, provenance, or context selection.
- **18_13 Atkinson & Bench-Capon** — `demote`: preserved abstract supports a historical/taxonomic contribution, not a demonstrated extractor or formal engine.
- **S24P02 Hodges** — `demote`: concrete and historically valuable correctness proof for al-Barakāt’s syllogistic diagrams, but narrow, landing-page-only evidence and no NLP/context-engineering mechanism.

## Hostile countertest result

The high verdicts were not assigned from title, category, venue, prestige, benchmark status, or recency alone. Each high item has a concrete mechanism tied to a named pipeline stage. Formal logic, theorem proving, generic tutoring, historical relevance, and generic scheme discussion were explicitly separated from direct extraction/protocol evidence. The main remaining uncertainty is full-text availability for `18_06`, `18_09`, and several abstract-only records; these were not promoted to high.

## Artifact verification

- Detailed judgments: `.hermes/lit_review/ranking/verification_runs/adversarial_relevance_reviewer_A.csv`
- Input identity status: `.hermes/lit_review/ranking/finalized_v1_1/aggregate_top20_identity_status.csv`
- Evidence roots: `.hermes/lit_review/ranking/verification_runs/20261012_shard1` through `20261012_shard4`
- Reviewed IDs: exactly 18 unique identity-pass IDs; no duplicates or omissions.
- Ranking and identity artifacts: unchanged by this review.
