# Walton-scheme ranking repair

## Scope

Repaired only `review_walton_schemes_category.csv` and `review_walton_schemes_global.csv`. The protocol and all other repository files were left unchanged.

## Corrections

- Replaced generic rationale/evidence with paper-specific distinctions across scheme/CQ, defeasible logic, dialogue/objection-reply, argument extraction, provenance/infrastructure, deductive reasoning, and generic LLM/context work.
- Preserved all 124 literal paper IDs and normalized duplicate-work scores: Lawrence & Reed = 72, Shanahan = 56, and the three Maliszewski records = 41.
- Set `S10P10` confidence to `medium` because the supplied evidence leaves evaluation-data provenance uncertain.
- Kept `S21P01` as a weak false positive with score 15 and medium confidence.
- Recomputed category and global ranks using descending score, then numeric `category_num`, numeric `paper_order`, and literal `paper_id` as the deterministic tie-break.

## Verification

Both CSVs contain 124 rows, identical unique ID sets, integer scores in 0–100, non-empty explanations/evidence, contiguous unique ranks, and ranks consistent with the protocol ordering.
