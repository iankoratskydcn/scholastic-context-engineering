# RAG-grounding ranking repair

Repaired the category and global RAG-grounding rankings using the retained paper summaries and the adversarial review.

## Corrections

- Reclassified `S10P10` (Trajano et al.) as a strong direct scheme-conditioned RAG/context prior-art threat: scheme descriptions/examples are supplied to an LLM, retrieval-augmented translation is used, and wrong-scheme retrieval is discussed. Score: `85`, confidence: `high`.
- Removed unsupported retrieval/context-selection claims from `S23P02`, `S25P02`, `15-10`, and `S24P01`. Their revised explanations identify indirect dialogue/protocol, metric-methodology, conceptual application, and historical-formalization relevance respectively.
- Split category 20 into direct citation/fabrication evidence (`20_10`, `20_11`, with `20_01` as weaker evidence-integrity work) versus adjacent essay, authorship, style, evaluation, and normative-generation studies.
- Replaced generic evidence strings for categories 16–18 with paper-specific findings covering historical proof formalization, culture-conditioned evaluation, defeasible verification, argument graphs, scheme/critical-question machinery, and document-grounded Toulmin argument generation.
- Kept the distinctions explicit among retrieval architecture, evidence/citation verification, context selection/compression, corpus/provenance infrastructure, formal verification, and adjacent generation-quality work.

## Rank recomputation

Both CSVs retain all 124 original paper IDs. Category ranks were recomputed within each category; global ranks were recomputed by descending score with numeric `category_num`, then `paper_order` as tie-breakers.

Changed substantive rows: 45. Only the two RAG-grounding CSVs and this repair note were modified.
