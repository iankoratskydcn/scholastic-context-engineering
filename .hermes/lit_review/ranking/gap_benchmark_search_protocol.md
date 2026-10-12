# Gap-Filling Benchmark Search Protocol

## Goal
Find scholarly benchmark-producing studies or reusable evaluation resources that fill benchmark gaps in the Scholastic Context Engine master plan:

`authentic source text -> attributed claims -> cross-tradition argument form -> proof/dialectical skeleton -> provenance/dependency-preserving selection/compression -> disputation retrieval -> strength evaluation -> inspectable philosophical output`

## Inclusion
- Scholarly paper, dataset, corpus, benchmark, or evaluation task.
- Exact identity verified from an opened scholarly page/PDF or official scholarly repository.
- Benchmark/resource mechanism and task read from retained evidence.
- Prefer resources that expose intermediate artifacts, not only final answer scores.
- Include preprints/workshops when scholarly identity and benchmark artifact are clear; label status.
- Search the exact gap assigned to the worker, plus adjacent terms.

## Exclusion
- Generic QA without argument/provenance/structure relevance.
- Methods-only papers that introduce no benchmark/resource unless they release a reusable evaluation task.
- Paper-only claims with no inspectable benchmark evidence.
- Near matches and duplicate versions: preserve identity, flag family/version.

## Required output
Each worker writes:
- `gap_search_<slug>.csv`
- `gap_search_<slug>.md`

CSV columns:
`record_id,citation,title,authors,year,venue,identifier,scholarly_source_url,artifact_url,benchmark_or_resource_name,benchmark_status,task_description,inputs,outputs_or_labels,pipeline_gap_filled,exact_or_adjacent,authenticity_class,artifact_access_status,license_status,evidence_basis,limitations,why_relevant,confidence`

Use `benchmark_status` values:
`introduces_benchmark`, `introduces_dataset_or_corpus_used_as_benchmark`, `introduces_evaluation_task_or_metric_only`, `evaluates_existing_benchmark_only`, `uncertain`.

Use `exact_or_adjacent` values:
`direct_gap_fill`, `strong_adjacent`, `control_only`, `false_positive`.

## Evidence discipline
- Do not summarize a snippet as a paper finding.
- Preserve failed/blocked searches in the Markdown report.
- Do not infer artifact access or license from paper access.
- Keep duplicate/version families explicit.
- Final counts are reconciled programmatically after all waves.
