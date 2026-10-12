# Proof-relevance ranking repair

Date: 2026-10-12

## Scope

Repaired only `review_proof_relevance_category.csv`, `review_proof_relevance_global.csv`, and this log. Source IDs and the 124-row non-benchmark ranking scope were preserved.

## Changes

- Replaced benchmark-status boilerplate with mechanism-level evidence: proof-state/premise retrieval, natural-language proof-relevant selection, formal semantics/verification, argument extraction/dialogue structure, or generic retrieval/compression.
- Separated Lean Copilot’s direct formal-library premise retrieval from the natural-language regime; recorded Explanation-Refiner as the closest natural-language prior-art boundary in the ranking rationale.
- Reclassified formal defeasible logic, formal dialogue, historical proof formalization, argument mining, and scholastic-method papers as adjacent regimes unless the evidence showed an actual selector-to-proof interface.
- Downgraded generic compressors and retrieval systems where the evidence lacks explicit claim/premise representation, dependency preservation, sufficiency/minimality, provenance, or formal validation.
- Rewrote explanations to name paper-specific mechanisms and limitations rather than using category boilerplate.
- Preserved low confidence and unresolved evidence for `S02P08` and `S10P10`; their provisional status is stated explicitly rather than treated as proof-relevance evidence.
- Recomputed category ranks and global ranks after score changes using descending score, then numeric `category_num`, numeric `paper_order`, and literal `paper_id` ties.

## Verification

Both CSVs contain 124 unique IDs, required columns, integer scores in `[0,100]`, complete unique ranks in their populated rank column, blank rank values in the other rank column, and matching row metadata across category/global outputs. Only the two CSVs and this repair log were modified.

Rows changed: 124/124.
