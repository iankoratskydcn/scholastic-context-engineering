# Repair report: philosophical-output ranking

- Updated `review_philosophical_output_category.csv` and `review_philosophical_output_global.csv` using paper-specific findings from retained summary files and `remaining_nonbenchmark.csv`.
- Preserved all immutable `paper_id` values, scores, category ranks, and global ranks; no score changes required.
- Replaced category boilerplate explanations with citation-specific explanations tied to each paper’s method, finding, or contribution and its philosophical-output relevance.
- Replaced generic evidence with retained-summary file/item references and concrete source findings; fallback rows cite the retained input evidence explicitly.
- Calibrated confidence downward where retained evidence explicitly signaled uncertainty.
- Rows repaired: 248 output rows (124 category, 124 global).
- Follow-up pass replaced the remaining generic historical-logic and AI-writing evidence with numbered summary findings.
