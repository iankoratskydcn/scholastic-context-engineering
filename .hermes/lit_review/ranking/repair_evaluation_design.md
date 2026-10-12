# Evaluation-design ranking repair

## Scope

Repaired `review_evaluation_design_category.csv` and `review_evaluation_design_global.csv` for the 124 rows in `remaining_nonbenchmark.csv`. The ranking measures transferable evaluation-design value, not corpus or dataset presence alone.

## Repair rules

- Replaced repeated generic explanations with paper-specific rationales naming the concrete benchmark condition, metric, ablation/control, human-evaluation protocol, dataset/training-artifact limitation, or conceptual guidance.
- Kept benchmark status conservative: a training corpus, scholarly corpus, or reused task was not promoted to a new benchmark.
- Lowered scores where the retained evidence supported only conceptual guidance, corpus/infrastructure value, or a training artifact; retained the highest scores for controlled perturbations, positional robustness, negation/false-premise controls, evaluator consistency, and repeated human/LLM evaluation protocols.
- Recomputed category and global ranks from numeric `category_num`, numeric `paper_order`, and literal `paper_id` as the final tie-break.

## Verification

Both CSVs contain the same 124 unique paper IDs as the source ranking population, scores are integers in 0–100, category/global ranks are complete and unique, and explanations are non-empty and paper-specific.
