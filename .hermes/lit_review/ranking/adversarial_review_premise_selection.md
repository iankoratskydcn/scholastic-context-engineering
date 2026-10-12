# Adversarial review: premise-selection ranking

## Verdict

**REVISE_REQUIRED.** The two files cover the correct 124-paper universe and contain valid row schemas, but the global ranking violates the protocol's deterministic tie-break rule. More importantly, several explanations and scores blur formal theorem-prover premise retrieval, formal logical modeling, corpus infrastructure, and natural-language proof-relevant context selection. The ranking is usable as a draft, not as a final auditable review.

## Validation performed

- `remaining_nonbenchmark.csv`: 124 unique paper IDs.
- `review_premise_selection_category.csv`: 124 rows, 124 unique IDs, exact ID-set match, no invariant mismatches against the remaining corpus.
- `review_premise_selection_global.csv`: 124 rows, 124 unique IDs, exact ID-set match, no invariant mismatches.
- Scores are integers in the 0–100 range; global scores are non-increasing by rank.
- Category ranks are contiguous within each category and category ordering is score-descending.
- The category file leaves `global_rank` blank and the global file leaves `category_rank` blank as required.

## Findings

### 1. Global tie-break rule is violated — definite protocol defect

`ranking_protocol.md` requires equal scores to be ordered by canonical `paper_id`. The global file instead preserves a different order for 12 tied-score blocks, affecting 29 rows. Examples:

- score 82: `S04P08` precedes `18_06`, but canonical order requires `18_06` then `S04P08`;
- score 79: `S08P06` precedes `18_05`, but canonical order requires `18_05` then `S08P06`;
- score 76: `S02P09`, `S03P02` precede `13-01`, `18_08`, but canonical order requires the `13-` and `18_` IDs first;
- score 68: `S10P04` precedes `12-01`, but canonical order requires `12-01` first.

This is mechanically reproducible by sorting `review_premise_selection_global.csv` by `(-score_0_100, paper_id)`. The category file does not show the same within-category tie-order defect.

**Required repair:** regenerate `global_rank` using descending score and then literal canonical `paper_id` order; do not normalize or reinterpret the IDs.

### 2. Formal theorem-proving and natural-language context selection are not separated consistently — major conceptual defect

The source summaries explicitly distinguish three regimes: (a) natural-language proof-relevant sentence selection and formalization, with Explanation-Refiner as the closest precedent; (b) whole-problem natural-language-to-logic translation, such as Logic-LM/LINC; and (c) formal-library premise retrieval inside Lean/Isabelle/Coq, such as LeanDojo, Magnushammer, and Lean Copilot. The ranking only partially preserves this distinction.

`S08P06` is comparatively well described: it says Lean Copilot operates with Lean/formal tooling and notes the external checker. However, many category-18 rows receive the generic explanation “Supplies an explicit logical, dialectical, or syllogistic structure that can organize candidate premises and support proof-relevant selection.” That wording presents formal defeasible-logic and argumentation-model papers as if they were natural-language premise selectors. The evidence field for these rows is also only the generic statement that the source is a formal/conceptual study without a benchmark artifact. It does not establish a retrieval system, context selector, natural-language candidate pool, or downstream proof-relevance evaluation.

The same conflation appears in category 24: `S24P01` and `S24P02` are historical formalizations/correctness proofs, `S24P03` and `S24P04` are formalizations, `S24P08` is corpus infrastructure, and `S24P15` is a conceptual KG/LLM framework. Yet all are assigned the same direct-sounding premise-selection explanation. `S24P08` is especially clear: its evidence says “Corpus infrastructure; not presented as a benchmark,” while its explanation claims it supplies a logical structure for candidate-premise selection. Those are different contribution types.

**Required repair:** add an explicit transfer/directness distinction in each explanation, e.g. `formal-proof analogue`, `natural-language selection method`, `argument-schema resource`, `corpus/provenance infrastructure`, or `conceptual background`. Do not treat a formal proof system or a historical logical formalization as evidence that a natural-language context selector exists.

### 3. Evidence basis is frequently non-discriminating and does not support the claimed rank — major auditability defect

The protocol requires evidence that points to source evidence rather than reviewer intuition. For all category-18 rows and most category-16 rows, the evidence basis repeats the same generic phrase: “source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact.” That phrase supports only benchmark exclusion; it does not support the premise-selection score or category rank.

The generic explanations likewise repeat across unrelated papers. For example, formal argumentation systems, human reasoning studies, corpus infrastructure, and historical formalizations all receive the same “explicit logical ... structure” rationale. A reviewer cannot reconstruct why `18_06` scored 82, `18_07` scored 70, or why those papers outrank direct natural-language argument-mining and context-selection precedents from the cited evidence.

**Required repair:** for every high or medium score, cite the concrete transferable mechanism and its boundary: candidate type, selection/retrieval operation, query/proof-state conditioning, formal checker, argument representation, or provenance function. If the paper has no such mechanism, lower the score or classify it as background rather than direct method evidence.

### 4. Corpus and digital-humanities infrastructure is over-promoted relative to direct selection methods — ranking validity concern

Several category-22/24 items are ranked as strong premise-selection evidence despite being resources rather than selection algorithms. Examples include:

- `S22P07` (Index Thomisticus as linked data), global rank 17, score 80;
- `S22P09` (*Corpus Thomisticum* infrastructure), global rank 25, score 77;
- `S24P08` (OpenITI corpus infrastructure), global rank 23, score 78;
- `S22P10` (DH infrastructure history), global rank 44, score 72.

Their evidence fields explicitly say linked-data publication, search/retrieval infrastructure, corpus infrastructure, or DH history, not a premise-selection model or proof-relevance evaluation. By comparison, direct context-compression and selection methods occupy ranks 1–13, which is appropriate, but the infrastructure scores remain high enough to compete with formal premise-selection analogues and argumentation systems. This makes the global ordering difficult to interpret as “germane value” rather than general usefulness to the larger project.

**Required repair:** either introduce a clearly named infrastructure/provenance-transfer tier with lower ceiling scores, or revise scores so corpus availability is not treated as evidence for the selection algorithm itself. Preserve high scores only when the resource contributes a concrete retrieval, indexing, annotation, or provenance mechanism relevant to the proposed context selector.

### 5. The ranking has no explicit penalty for duplicate/near-duplicate or survey-only evidence — moderate methodological concern

The output includes many surveys, conceptual papers, historical works, and repeated infrastructure records. This is not automatically invalid because the protocol ranks all remaining nonbenchmark papers, but the explanation and score policy do not distinguish direct methods from background or synthesis. For example, multiple category-1 hallucination surveys receive scores 30–34 with nearly identical rationales, while category-18 formal systems receive 66–82 despite similarly lacking a natural-language selector. The scale therefore appears inconsistent across evidence classes.

**Required repair:** keep every required row, but calibrate scores against a common rubric: direct selection/compression method; direct formal premise retrieval; natural-language reasoning/argument structure; infrastructure/provenance support; conceptual/background relevance. State the rubric in the report or reviewer artifact so identical generic evidence cannot produce materially different score bands without a stated reason.

## Positive findings

- The reviewer did not accidentally rank benchmark-producing rows: every output ID is present in `remaining_nonbenchmark.csv`, and no extra IDs were introduced.
- The files preserve the source-artifact IDs and metadata exactly.
- The top of the ranking correctly prioritizes context/example selection and compression methods (`S04P12`, `RECOMP`, `LongLLMLingua`, `LLMLingua`), which are closer to natural-language context construction than formal theorem-prover systems.
- The formal-prover item `S08P06` is not ranked above the strongest natural-language compression/selection papers and its explanation at least names Lean/formal checking; this is the right direction, but the distinction must be applied consistently.

## Recommended disposition

1. Repair global tie ordering first.
2. Re-score or relabel formal-logic, theorem-proving, corpus, and historical items using explicit directness/transfer categories.
3. Replace generic evidence strings with paper-specific mechanism-plus-boundary evidence for all rows above the reviewer’s medium threshold.
4. Re-run the protocol checks: 124 rows, exact ID set, unique ranks, score range, non-empty explanations/evidence, canonical tie ordering, and no claim that formal proof validity equals natural-language premise/context adequacy.
