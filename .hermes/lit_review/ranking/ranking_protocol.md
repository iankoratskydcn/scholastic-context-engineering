# Ranking protocol

**Protocol version: 1.1**  
**Compatibility amendment: 2026-10-12**

## Scope

Rank only rows in `remaining_nonbenchmark.csv`. Benchmark-producing studies are excluded from ranking and remain in `benchmark_studies.csv`; benchmark-related but non-new studies remain in `benchmark_related_but_not_new.csv`.

## Canonical order

- Category order is numeric ascending.
- Paper order is the source-artifact order.
- Do not rename, merge, or invent paper IDs.

## Versioned ID compatibility rule (v1.1)

The following three formats are valid immutable `paper_id` source identifiers:

- `S##P##` — legacy source form with `S`/`P` markers;
- `##-##` — legacy source form with a hyphen separator;
- `##_##` — legacy source form with an underscore separator.

Here `##` means exactly two decimal digits. These forms are equivalent only for locating the numeric category and paper order; the literal source identifier remains the authoritative value in every CSV. IDs are immutable: do not rename, normalize separators, reformat, merge, or invent IDs, even when producing derived ranking files. Consumers must preserve the literal `paper_id` and use `category_num` and `paper_order` as the numeric ordering fields.

For deterministic ordering, sort by the tuple `(numeric category_num, numeric paper_order, literal paper_id)`. When equal scores require a tie-break, apply that tuple in ascending order; the literal `paper_id` is the final tie-break and is compared exactly as stored, not after normalization.

## Required outputs per reviewer

For reviewer slug `<slug>`:

- `review_<slug>_category.csv`: one row for every remaining paper, with `category_rank` ranking within its category.
- `review_<slug>_global.csv`: one row for every remaining paper, with `global_rank` ranking across all remaining papers.

Required columns in both files:

`paper_id,category_num,category,paper_order,citation,reviewer_slug,viewpoint,category_rank,global_rank,score_0_100,confidence,explanation,evidence_basis`

`category_rank` is populated in the category file and blank in the global file. `global_rank` is populated in the global file and blank in the category file. Scores are integers 0–100. Ranks are unique integers with no ties; break equal scores by ascending `(numeric category_num, numeric paper_order, literal paper_id)` order. Explanations must be 1–3 sentences and name the concrete feature that drove the ranking. `evidence_basis` must point to the source summary or paper evidence, not reviewer intuition alone.

## Judging rule

Rank germane value to the scholastic context-engineering project, not prestige, citation count, recency, or writing quality. The perspective controls weighting; all reviewers still score project relevance, novelty threat, methodological transfer, and likely usefulness.

## Validation

Every output must have exactly 124 rows, exactly the same paper IDs as `remaining_nonbenchmark.csv`, no duplicate IDs, scores in range, unique ranks in the relevant ranking file, and non-empty explanations/evidence.
