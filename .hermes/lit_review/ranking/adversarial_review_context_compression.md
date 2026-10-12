# Adversarial review: context-compression ranking

## Verdict

**BLOCKED.** The files are structurally complete and mostly aligned with the intended topic, but the ranking is not yet defensible as a compression/context-selection ranking. It over-rewards generic reasoning/argumentation relevance, collapses materially different papers into large uniform score blocks, and contains a global tie-break violation required by the protocol.

## Checks performed

- Compared both review CSVs against `remaining_nonbenchmark.csv`.
- Verified 124 rows in each output, matching paper IDs, no duplicate IDs, and unique ranks in the relevant file.
- Checked score/rank ordering, score distributions, explanations, and evidence basis against `ranking_protocol.md`.
- Inspected whether explanations identify compression, selection, context-budget, long-context, or dependency-preservation mechanisms rather than only generic reasoning relevance.

## Findings

### 1. Global ranking violates the prescribed tie-break rule — blocker

`ranking_protocol.md:25` requires equal scores to be ordered by canonical `paper_id`. In `review_context_compression_global.csv`, `S03P02` (score 93) is rank 15, followed by `18_01`–`18_14` (also score 93) at ranks 16–26. Canonical ID ordering requires `18_01`–`18_14` before `S03P02`. The category file does not have this specific global-order defect, but the global output is non-compliant.

**Fix:** Recompute global ranks after sorting by `score_0_100` descending, then canonical `paper_id` ascending; preserve unique ranks.

### 2. Context-compression papers are indistinguishable at the maximum score — major

All twelve `S04P01`–`S04P12` papers receive score 100 in both files (`review_context_compression_category.csv:19-30`; `review_context_compression_global.csv:19-30`). The protocol permits tied scores but requires rankings to express project relevance and concrete ranking drivers. These papers cover extractive, abstractive, latent-memory, token-classification, tool-use, query-aware, and example-selection approaches; assigning every one the same maximum score gives no discrimination on preservation of inferential dependencies, query conditioning, compression representation, or evidence of downstream task fidelity.

**Fix:** Re-score using explicit differentiators: selection/query conditioning, compression representation, preservation/fidelity evaluation, reasoning-task relevance, and transferability to the scholastic setting. Reserve 100 for papers that are strongest across those dimensions, not the whole category.

### 3. Generic reasoning/argumentation relevance is being treated as direct compression evidence — major

The 11 papers in category 18 (`18_01`–`18_09`, `18_13`, `18_14`) all receive score 93 and the same explanation in both files (category CSV lines 65–75; global CSV lines 65–75): “Addresses correctness of inferences…” and “Provides explicit structures for claims, premises, rebuttals, or inferential dependencies.” Their evidence basis explicitly says they are scholarly/formal/conceptual studies without benchmark-producing artifacts. That establishes possible dependency representations, but not context compression, context selection, token-budget behavior, or preservation under lossy transformation. The ranking therefore reflects generic reasoning value rather than the requested compression/context-selection criterion.

**Fix:** Lower or separate these as enabling/background literature unless the source evidence demonstrates a compression or selective-context mechanism and an evaluation of preserved reasoning dependencies.

### 4. Several high-ranked non-compression papers lack a concrete compression pathway — major

The global list places the category-21 argumentation papers at ranks 27–31 with scores 86–89, `S10P10` at rank 32/score 83, and `S09P04`–`S09P05` at ranks 38–40/scores 76–78. Their explanations mainly cite explicit argument structures or generic correctness; they do not state what is selected, compressed, dropped, retained, or evaluated under a context budget. `S21P01` is explicitly called a “False-positive HCI system” yet still receives score 79 (category CSV line 89; global CSV line 89).

**Fix:** Apply a minimum directness gate: high scores should require demonstrated context selection/compression or a direct method for preserving reasoning dependencies during context reduction. Otherwise cap scores and label the contribution as background/transfer evidence.

### 5. Evidence and explanations are too templated to support the fine-grained ranking — risk

The same short explanations recur across many unrelated papers: 28 rows use the exact “correctness of inferences… conceptual distinctions” text, 19 use only “conceptual distinctions,” and 14 use the same generic “explicit structures” formulation. These explanations do not name the concrete feature that drove relative ordering, despite `ranking_protocol.md:25` requiring a concrete ranking driver. The category-16 block is especially revealing: all 14 papers receive score 57 and identical evidence/explanation language, even though they are historical/formal works with no demonstrated compression or context-selection contribution.

**Fix:** Rewrite explanations to identify paper-specific mechanisms and evidence: e.g., query-aware pruning, token-level salience, latent memory, positional robustness, dependency graph retention, or merely conceptual relevance. If no such feature is evidenced, state that limitation and score accordingly.

## What passed

- Both outputs contain exactly 124 data rows, matching `remaining_nonbenchmark.csv` IDs.
- No duplicate paper IDs were found.
- Category ranks and global ranks are unique in their respective files.
- Scores are integer values within 0–100.
- Explanations and evidence fields are non-empty and generally grounded in the supplied artifact summaries.
- Category-file rank ordering is score-consistent; the global file has the tie-break defect described above.

## Required next proof

1. Define and apply a directness rubric distinguishing direct compression/context-selection evidence from generic reasoning or structured-knowledge relevance.
2. Re-score the uniform blocks and high-ranked background papers with paper-specific explanations.
3. Recompute both ranking files and rerun the row/ID/score/rank validation, including canonical tie ordering.
