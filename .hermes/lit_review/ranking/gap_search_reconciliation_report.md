# Gap-search reconciliation report

## Scope

- Agent lanes expected: **25**
- Manifested lanes: **25**
- Valid or schema-drift lanes retained: **24**
- Invalid lanes excluded: **1**
- Missing lanes: **0**
- Retained raw records: **287**

## Fail-closed findings

- `premise_equivalence` is excluded from the reconciled corpus: the delivered file is an 80-row prior benchmark-ranking matrix, not the requested premise-equivalence gap search output. The raw artifact is preserved unchanged.
- `dependency_preserving_compression`, `argument_strength`, and `dialogue_game_transitions` are retained but flagged for schema/path drift; their fields were mapped into the common reconciliation schema without overwriting raw evidence.
- All raw agent CSV/Markdown outputs remain preserved at their original paths.

## Lane manifest

| Lane | Records | Status | Raw path |
|---|---:|---|---|
| cross_source_synthesis | 11 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_cross_source_synthesis.csv` |
| common_ground_detection | 8 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_common_ground_detection.csv` |
| form_conditioned_selection | 8 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_form_conditioned_selection.csv` |
| dependency_preserving_compression | 13 | schema_drift | `.hermes/lit_review/ranking/gap_search/dependency_compression/dependency_compression.csv` |
| provenance_transformation | 11 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_provenance_transformation.csv` |
| disputation_retrieval | 10 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_disputation_retrieval.csv` |
| scholastic_output_faithfulness | 14 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_scholastic_output.csv` |
| argument_strength | 20 | schema_drift | `.hermes/lit_review/ranking/gap_search/argument_strength.csv` |
| cross_tradition_forms | 13 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_cross_tradition_forms.csv` |
| attribution_recursive_grounding | 12 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_attribution_recursive_grounding.csv` |
| alternative_valid_parses | 6 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_alternative_valid_parses.csv` |
| implicit_premise_reconstruction | 7 | valid | `.hermes/lit_review/ranking/gap_search/implicit_premise_reconstruction.csv` |
| citation_faithfulness | 12 | valid | `.hermes/lit_review/ranking/citation_faithfulness_benchmarks.csv` |
| multi_document_evidence | 11 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_multi_document_evidence.csv` |
| counterargument_generation | 17 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_counterargument_generation.csv` |
| philosophical_reasoning_eval | 11 | valid | `.hermes/lit_review/ranking/benchmark_review_philosophical_reasoning_eval_global.csv` |
| scholastic_protocol_annotation | 5 | valid | `.hermes/lit_review/ranking/gap_search_scholastic_protocol_annotation.csv` |
| premise_equivalence | 80 | invalid_wrong_artifact_excluded | `.hermes/lit_review/ranking/benchmark_review_premise_equivalence_global.csv` |
| evidence_graph_traversal | 19 | valid | `.hermes/lit_review/ranking/gap_search/gap_search_evidence_graph_traversal.csv` |
| expert_argument_comparison | 22 | valid | `.hermes/lit_review/ranking/gap_search/expert_argument_comparison.csv` |
| claim_ownership_attribution | 9 | valid | `.hermes/lit_review/ranking/gap_search_claim_ownership_attribution.csv` |
| intermediate_artifact_eval | 10 | valid | `.hermes/lit_review/ranking/intermediate_artifact_eval.csv` |
| dialogue_game_transitions | 11 | schema_drift_path_drift | `.hermes/lit_review/benchmark_exports/dialogue_game_transitions.csv` |
| multilingual_cross_cultural_reasoning | 13 | valid | `.hermes/lit_review/ranking/gap_search/multilingual_cross_cultural_reasoning.csv` |
| pipeline_composition_ablation | 14 | valid | `.hermes/lit_review/ranking/gap_search/pipeline_composition_ablation/gap_search_pipeline_composition_ablation.csv` |

## Outputs

- `.hermes/lit_review/ranking/gap_search_reconciliation_manifest.csv` — lane-level manifest and status.
- `.hermes/lit_review/ranking/gap_search_reconciled.csv` — normalized retained records with raw-path provenance.
- `.hermes/lit_review/ranking/gap_search_reconciliation_report.md` — this report.
