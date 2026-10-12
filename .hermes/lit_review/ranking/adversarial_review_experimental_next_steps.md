# Adversarial review: experimental-next-steps ranking

## Verdict

**BLOCKED / revise before acceptance.** The two outputs cover the correct 124-paper universe and satisfy most structural checks, but the global ranking violates the protocol's deterministic tie-break rule, 50 inherited paper IDs violate the protocol's canonical ID format, and the rationale/score design is too category-templated to prove that the ranking measures experimental utility rather than broad project importance.

## Checks passed

- `remaining_nonbenchmark.csv` contains 124 unique paper IDs.
- Both review files contain exactly 124 rows, with exact ID-set equality to `remaining_nonbenchmark.csv`; no missing, extra, or duplicate IDs.
- Category-file ranks are complete and unique within every category. Each category rank is the contiguous range `1..N`.
- Global ranks are unique and contiguous `1..124`.
- Scores are integer values in `0..100`.
- Required metadata matches the source for every row: category number, category, paper order, and citation.
- Reviewer slug, viewpoint, confidence, explanation, and evidence basis are non-empty for all rows.
- Explanations satisfy the mechanical 1–3 sentence check for all 248 reviewed rows.
- Evidence-basis paths resolve to the retained summary corpus when interpreted relative to `.hermes/lit_review/`; all 124 rows have distinct evidence-basis strings.
- Category and global files agree on all non-rank fields.

## Issues

### 1. Global tie-break order is not protocol-compliant — blocker

`ranking_protocol.md` requires equal scores to be ordered by canonical `paper_id`. The global file instead preserves a different order for several tied-score groups. There are 21 affected rank positions (10 adjacent swaps/rotations plus related displaced positions), including:

- global ranks 35–36: `S01P01` before `12-02`, but canonical lexical order requires `12-02` before `S01P01`;
- ranks 38–41: `S10P02`, `S10P04`, `S10P10`, `12-01`, but canonical lexical order requires `12-01` first;
- ranks 79–89: the score-58 group is not in canonical paper-ID order;
- ranks 91–98: the score-56 group is not in canonical paper-ID order.

The category file does pass the same score/tie ordering check within categories. The global file must be regenerated or corrected using descending score, then canonical paper ID.

### 2. Fifty IDs violate the protocol's required canonical format — blocker/source-data defect

The protocol specifies `S<category number, 2 digits>P<paper order, 2 digits>`. The source and both outputs preserve 50 nonconforming IDs, including hyphenated IDs such as `12-01`, `13-01`, and `15-03`, and underscored IDs such as `16_01`, `17_05`, `18_01`, and `20_01`.

This does not create coverage loss because both review files exactly mirror the source ID set, and the protocol also says not to invent or rename IDs. It is nevertheless an unresolved protocol conflict: either the source IDs need a versioned canonicalization upstream, or the protocol must explicitly permit the legacy forms. Do not silently rename IDs in only these review files.

### 3. Explanations are mostly category templates, not paper-level ranking evidence — major

Only 2 of 124 explanations are unique singletons; 122 rows reuse one of 16 category-level templates. Examples include all 14 category-16 papers receiving the exact same explanation and score 41, all 3 category-13 papers receiving the same explanation and score 61, and all 11 category-18 papers receiving the same explanation text. The templates do name useful experimental operations (ablation, controls, metrics, annotation, proof traces), so the mechanical explanation check passes, but they generally do not identify the specific feature of the cited paper that justifies its position relative to neighboring papers.

This weakens the required claim that the concrete feature drove the ranking. Evidence strings are paper-specific, but the explanation field does not connect that evidence to the score or rank. A valid revision should retain the category-level next-step pattern while adding a paper-specific differentiator: e.g., released code/data, controlled factor, intervention, measurable outcome, solver/proof artifact, annotation resource, or explicit limitation that determines rank.

### 4. Experimental usability is only partially identified by the scores — major

The top of the global ranking does contain clearly usable experimental material: `S04P03` (96) names compression-ratio/selection-signal ablations against an uncompressed baseline, and `S03P01` (93) names position-by-depth curves, distractor load, and robustness testing. However, the scoring scheme does not consistently distinguish baselines, ablations, metrics, and falsifiable hypotheses from general relevance:

- `S23P01` receives 83 while its explanation only says to operationalize dialogue states and test violations, consistency, and terminal outcomes; it does not specify a baseline, comparison, or intervention.
- `S02P03` receives 81 with a stronger metric list, but still has no explicit baseline or hypothesis.
- The 14 category-16 historical-logic papers all receive exactly 41 under one generic formalization explanation despite differing source artifacts.
- Categories 13 and 17 likewise collapse all papers to one score, and the category-level template provides no paper-specific experimental discriminator.

Therefore the ranking is usable as a rough prioritization of promising topics, but not yet as an auditable experimental-next-steps ranking. A revision should make the score dimensions explicit (at minimum: baseline availability, manipulable factor/ablation, measurable metric, falsifiable hypothesis, and implementation/data feasibility) or add those fields to the review artifact.

## Required disposition

1. Correct global tie ordering without changing the paper universe.
2. Resolve the source/protocol conflict over the 50 noncanonical IDs in a versioned upstream artifact or an explicit protocol amendment.
3. Rewrite explanations for at least the tied/template-heavy groups so each paper's rank has paper-specific experimental evidence.
4. Re-score or annotate rows where the current score reflects general importance but lacks an identifiable baseline, ablation, metric, or falsifiable hypothesis.
