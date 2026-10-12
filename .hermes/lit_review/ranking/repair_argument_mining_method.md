# Argument-mining methodology ranking repair

Date: 2026-10-12

## Scope

Repaired only `review_argument_mining_method_category.csv`, `review_argument_mining_method_global.csv`, and this log. IDs and source order were preserved.

## Changes

- Replaced generic evidence and explanations with paper-specific component, relation, scheme, structured-representation, or explicitly contextual/indirect assessments grounded in the retained summary for each category.
- Re-scored all 124 rows to separate direct extraction/representation precedents from formal reasoning foundations and contextual work.
- Reassessed `S10P02` as foundational scheme-taxonomy infrastructure, `S10P04` as narrower domain-specific scheme programming, and `S10P10` as a direct scheme-conditioned RAG/computational-argument precedent with medium confidence.
- Reconciled `S09P04`, `18_14`, and `S24P17` as retained IDs for the same/possibly different Lawrence & Reed survey versions; they are not treated as independent methodological contributions.
- Recomputed category ranks by descending score then numeric `paper_order`, and global ranks by descending score then numeric `category_num`, `paper_order`, and literal `paper_id`.
- Calibrated confidence downward for contextual, indirect, duplicate-uncertain, and source-limited records.

Rows changed: 124/124.
