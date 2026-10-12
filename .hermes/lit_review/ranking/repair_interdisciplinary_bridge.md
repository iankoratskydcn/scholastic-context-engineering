# Interdisciplinary bridge ranking repair

- Rewrote all 124 rows in both review CSVs with row-specific explanations and evidence pointing to `summaries/*.md` item sections.
- Corrected `S01P03` Rawte et al.: retained `not_benchmark` status but recorded the 75,000-sample HILT dataset and Hallucination Vulnerability Index; score changed 60 → 75.
- Corrected `S21P01` Hong et al.: preserved the source’s explicit HCI/ML false-positive finding and low relevance; score changed 87 → 25.
- Recomputed category and global ranks by descending score, then numeric category order and source paper order for deterministic ties; IDs were preserved verbatim.
- Validation target: 124 rows, exact inventory ID set, category ranks populated only in category output, global ranks populated only in global output.
