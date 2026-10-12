# Repair record — context compression ranking

## Scope

Repaired only `review_context_compression_category.csv`, `review_context_compression_global.csv`, and this file. Paper IDs and source evidence fields were preserved.

## Scoring changes

Scores now distinguish five dimensions: query conditioning, representation quality, fidelity risk/control, reasoning-task relevance, and transferability. The S04 block is no longer a uniform 100: only LLMLingua retains 100 as the broad baseline; LongLLMLingua and RECOMP score 99 for query/task-conditioned selection, LLMLingua-2 and tool-context compression score 98, and latent/opaque or example-set methods are lower where inspectability or within-example retention is limited.

Generic argumentation and formal-logic papers were downgraded when they provide schemas, rules, or dialogue models without an actual compression, selection, or context-budget experiment. Their remaining value is described as representation or evaluation prior art, with the transfer limitation stated explicitly.

## Ranking repair

- Category rows are emitted in numeric `category_num`, numeric `paper_order` order.
- `category_rank` and `global_rank` are unique integers.
- Global ties are resolved by descending numeric score, then ascending numeric `category_num`, numeric `paper_order`, and literal `paper_id`.
- Category ties use descending numeric score, then numeric `paper_order`, and literal `paper_id`.

## Verification

The repaired files contain 124 rows each, preserve the same 124 unique IDs, keep scores in 0–100, use non-empty concrete explanations and evidence fields, and contain no rank ties.
