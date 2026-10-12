# PI-slide-value ranking repair

Date: 2026-10-12

## Scope

Repaired only `review_pi_slide_value_category.csv`, `review_pi_slide_value_global.csv`, and this log, using `remaining_nonbenchmark.csv`, the retained agent summaries, and the adversarial review.

## Changes

- Recomputed `category_rank` independently within each populated category, ranking by descending score and then source `paper_order`.
- Recomputed `global_rank` after score changes with the same deterministic source-order tie break.
- Replaced generic ranking-corpus evidence pointers with concrete `.hermes/lit_review/agents/<summary>.md` source-entry pointers plus the retained evidence row.
- Rewrote explanations to name a slide use case: motivation, prior work, gap, or citation-ready. Prestige, recency, and canonicality are not used as standalone reasons.
- Corrected `S21P01` to a low-scoring naming/false-positive contrast citation; it is not treated as a scholastic-method precedent.
- Desaturated the 95+ cluster, distinguishing exact protocol overlap, strong adjacent threats, method precedents, infrastructure, and proposal-level evidence.
- Marked the two low-confidence rows (`S02P08`, `S10P10`) as pending verification and reduced their scores accordingly.

Rows changed: 124/124.
