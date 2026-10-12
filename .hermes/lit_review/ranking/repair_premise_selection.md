# Premise-selection ranking repair

## Scope

Repaired only `review_premise_selection_category.csv`, `review_premise_selection_global.csv`, and this report. Paper IDs, category metadata, citations, reviewer slug, viewpoint, and the required 124-paper universe were preserved.

## Changes

- Rewrote the inherited generic explanations and evidence bases so each row names a mechanism and a transfer boundary.
- Separated five evidence classes: natural-language proof-relevant context selection/compression; formal-library premise retrieval; whole-problem natural-language-to-logic translation; symbolic reasoning substrates; and corpus/provenance infrastructure.
- Lowered scores for survey/background, symbolic-transfer, and corpus/infrastructure rows where the source does not implement a premise selector. Direct context/example selection and compression methods retain the highest scores; formal-library retrieval remains a distinct, formal-proof-state analogue rather than a natural-language selector.
- Recomputed category ranks and global ranks after score changes. Global ties use numeric `category_num`, numeric `paper_order`, then literal `paper_id`; IDs were not normalized or renamed.

## Verification

- Both CSVs contain 124 rows and 124 unique paper IDs.
- The category and global ID sets are identical.
- Scores are integer values in the inclusive range 0–100.
- Category ranks are unique and contiguous within each category; `global_rank` is blank in the category file.
- Global ranks are unique and contiguous from 1 through 124; `category_rank` is blank in the global file.
- Global ordering is descending score, then `(numeric category_num, numeric paper_order, literal paper_id)` for equal scores.
- Explanations and evidence bases are non-empty; no protocol or other files were edited.
