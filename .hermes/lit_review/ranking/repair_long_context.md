# Long-context ranking repair

## Scope

These rankings cover only the 124 rows in `remaining_nonbenchmark.csv`. They intentionally exclude benchmark-producing direct studies, including LongBench, RULER, NoLiMa, LongPiBench, Long Range Arena, and ∞Bench; those remain outside this ranking under `ranking_protocol.md`. Therefore, the top ordering is the ordering of the nonbenchmark subset, not a claim that these are the strongest long-context studies overall.

## Evidence-weighted scoring rubric

Scores use feature-based relevance to the scholastic context-engineering project, in this order: (1) direct diagnostic evidence about context length, positional access, lost-in-the-middle/context rot, or retention under long prompts; (2) tested interventions involving context selection, compression, memory, or positional calibration; (3) structured representations or retrieval infrastructure that can reduce irrelevant-context load; (4) downstream reliability, hallucination, reasoning, or evaluation evidence that transfers only indirectly. Limitations are penalized when a paper lacks a controlled length/position manipulation, uses a narrow or older model setting, is conceptual, or provides infrastructure without LLM evaluation.

Scores were not changed in this repair: the direct top end remains intact, and all rank values remain valid. The 92 boilerplate explanations were replaced with paper-specific feature/limitation statements.

## Low-end floor policy

Some categories are intentionally low-relevance floors because their evidence is historical, conceptual, corpus/infrastructure-oriented, or output-evaluation-oriented rather than long-context evidence: category 16 uses a score floor of 5, category 18 a floor of 8, and category 20 a floor of 6. Equal scores within those categories are policy ties, not claims that the papers are substantively identical; canonical `paper_order` resolves the required rank. The repaired explanations name each paper’s distinct transferable feature and the missing context-length/position/compression evidence.

## Repair record

- `review_long_context_category.csv`: 92 explanations replaced; IDs, scores, and category ranks preserved.
- `review_long_context_global.csv`: 92 explanations replaced; IDs, scores, and global ranks preserved.
- No protocol or source files changed.
