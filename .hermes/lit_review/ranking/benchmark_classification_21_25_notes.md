# Benchmark classification notes: categories 21–25

Classification is based on the supplied category agent files and summary artifacts; source URLs were retained in those artifacts and were not treated as instructions. “Benchmark-producing” includes explicit benchmark introductions, reusable datasets/corpora used for model evaluation, and newly specified evaluation tasks/metrics. Existing-benchmark evaluations are separated.

## Counts

- `introduces_benchmark`: 1
- `introduces_dataset_or_corpus_used_as_benchmark`: 12
- `introduces_evaluation_task_or_metric_only`: 3
- `evaluates_existing_benchmark_only`: 17
- `not_benchmark`: 38
- `uncertain`: 0
- **Total rows:** 71
- **Benchmark-producing rows (first three statuses):** 16

## Boundary decisions

- Corpus or infrastructure papers were marked `not_benchmark` unless the artifact was explicitly introduced and used for model/task evaluation.
- Parser/annotation papers using an existing treebank were marked `evaluates_existing_benchmark_only`; papers introducing a reusable annotated resource used for evaluation were marked `introduces_dataset_or_corpus_used_as_benchmark`.
- Surveys, conceptual frameworks, formal reconstructions, and manual/human evaluations without a reusable benchmark artifact were marked `not_benchmark` or `introduces_evaluation_task_or_metric_only` where a new evaluative protocol/metric was the contribution.
- Category 24 entries P05/P06 are the same Langton study in preprint/published form; both are preserved in source order and classified independently as non-benchmark.
- Category 25 was reconstructed from its supplied summary artifact because `standardized_papers.csv` contains no category-25 rows; order follows the 16 numbered entries in that artifact.
