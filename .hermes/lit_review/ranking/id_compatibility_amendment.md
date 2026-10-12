# Ranking ID compatibility amendment validation

**Protocol:** `ranking_protocol.md` version 1.1 (compatibility amendment dated 2026-10-12).

## Amendment applied

- Preserves literal `paper_id` values as immutable source identifiers; no CSV was renamed or rewritten.
- Explicitly permits the three existing formats: `S##P##`, `##-##`, and `##_##`.
- Defines deterministic ordering as ascending numeric `category_num`, numeric `paper_order`, then literal `paper_id`.

## Corpus validation

- CSV files scanned: **60**.
- Total CSV rows scanned: **7,324**.
- Invalid/unrecognized IDs: **0**.
- Category/order field mismatches: **0**.
- Reviewer CSVs scanned: **50**.
- Reviewer paper-set failures: **0** (each has the same 124 unique IDs as `remaining_nonbenchmark.csv`).
- Reviewer rank uniqueness failures: **0** (category ranks are checked within category; global ranks across the full file).

### Accepted-format counts (all CSV rows)

| Format | Rows | Distinct IDs |
|---|---:|---:|
| `S##P##` | 4,395 | 219 |
| `##-##` | 713 | 71 |
| `##_##` | 2,216 | 72 |

### `remaining_nonbenchmark.csv`

- Rows / distinct paper IDs: **124 / 124**.
- Format distribution: `S##P##` **74**, `##-##` **10**, `##_##` **40**.
- Legacy IDs affected: **124 distinct immutable source identifiers** (all remaining papers use one of the three permitted legacy forms).

## Existing tie-break observations

- **101** equal-score adjacency pairs in **13** reviewer CSVs do not follow the newly documented deterministic tuple. These are recorded findings only; CSVs were not altered per task scope.
- No tie-break findings were observed in the category-ranking files; the findings are in global-ranking files.

Affected reviewer files and pair counts:
- `review_argument_form_taxonomy_global.csv`: 12
- `review_argument_mining_method_global.csv`: 4
- `review_dialectical_ai_global.csv`: 3
- `review_empirical_rigor_global.csv`: 17
- `review_evaluation_design_global.csv`: 2
- `review_experimental_next_steps_global.csv`: 4
- `review_hallucination_mitigation_global.csv`: 11
- `review_implementation_feasibility_global.csv`: 21
- `review_neurosymbolic_integration_global.csv`: 7
- `review_novelty_threat_global.csv`: 10
- `review_proof_relevance_global.csv`: 2

## Affected source files

The following **56** CSVs contain separator-based legacy IDs (`##-##` or `##_##`); all **60** CSVs were nevertheless scanned and accepted under the versioned rule:

- `all_standardized_records.csv`
- `benchmark_classification_11_15.csv`
- `benchmark_classification_16_20.csv`
- `benchmark_related_but_not_new.csv`
- `benchmark_studies.csv`
- `remaining_nonbenchmark.csv`
- `review_argument_form_taxonomy_category.csv`
- `review_argument_form_taxonomy_global.csv`
- `review_argument_mining_method_category.csv`
- `review_argument_mining_method_global.csv`
- `review_context_compression_category.csv`
- `review_context_compression_global.csv`
- `review_cross_cultural_logic_category.csv`
- `review_cross_cultural_logic_global.csv`
- `review_dialectical_ai_category.csv`
- `review_dialectical_ai_global.csv`
- `review_empirical_rigor_category.csv`
- `review_empirical_rigor_global.csv`
- `review_evaluation_design_category.csv`
- `review_evaluation_design_global.csv`
- `review_experimental_next_steps_category.csv`
- `review_experimental_next_steps_global.csv`
- `review_formal_logic_compatibility_category.csv`
- `review_formal_logic_compatibility_global.csv`
- `review_hallucination_mitigation_category.csv`
- `review_hallucination_mitigation_global.csv`
- `review_historical_fidelity_category.csv`
- `review_historical_fidelity_global.csv`
- `review_implementation_feasibility_category.csv`
- `review_implementation_feasibility_global.csv`
- `review_interdisciplinary_bridge_category.csv`
- `review_interdisciplinary_bridge_global.csv`
- `review_long_context_category.csv`
- `review_long_context_global.csv`
- `review_neurosymbolic_integration_category.csv`
- `review_neurosymbolic_integration_global.csv`
- `review_novelty_threat_category.csv`
- `review_novelty_threat_global.csv`
- `review_philosophical_output_category.csv`
- `review_philosophical_output_global.csv`
- `review_pi_slide_value_category.csv`
- `review_pi_slide_value_global.csv`
- `review_premise_selection_category.csv`
- `review_premise_selection_global.csv`
- `review_proof_relevance_category.csv`
- `review_proof_relevance_global.csv`
- `review_provenance_auditability_category.csv`
- `review_provenance_auditability_global.csv`
- `review_rag_grounding_category.csv`
- `review_rag_grounding_global.csv`
- `review_reusable_resources_category.csv`
- `review_reusable_resources_global.csv`
- `review_scholastic_protocol_category.csv`
- `review_scholastic_protocol_global.csv`
- `review_walton_schemes_category.csv`
- `review_walton_schemes_global.csv`

No CSV files were modified.
