# Experimental-next-steps ranking repair

- **Scope:** Repaired the 124 retained rows in `review_experimental_next_steps_category.csv` and `review_experimental_next_steps_global.csv`.
- **Evidence repair:** Replaced category-template explanations with paper-specific evidence snippets extracted from the retained summary corresponding to each paper order. Each explanation now states a baseline, intervention/ablation, metrics, falsifiable hypothesis, implementation/data burden, and limitation.
- **Scores:** Preserved all 124 scores because the retained evidence supported the existing relative utility signal but did not justify an unreviewed score change.
- **Ranks:** Recomputed category and global ranks using descending score, then literal `paper_id` order for ties. The global file now follows the protocol's deterministic tie rule without renaming legacy IDs.
- **Known protocol issue retained:** The source still contains 50 legacy noncanonical IDs; this repair does not rename them because the protocol prohibits inventing or renaming paper IDs.

## Verification

- 124 rows in each output; exact ID-set equality preserved.
- Scores remain integers in 0–100.
- Category ranks are contiguous and unique within each category.
- Global ranks are contiguous and unique from 1 through 124.
- Global ordering is exactly `(-score_0_100, paper_id)`.
- Metadata and evidence-basis fields were preserved; only explanations and rank fields were regenerated.
- No files outside the two target CSVs and this repair report were modified.
