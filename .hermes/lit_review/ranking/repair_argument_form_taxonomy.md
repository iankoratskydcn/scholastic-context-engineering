# Repair — argument-form taxonomy ranking

## Scope

Repaired `review_argument_form_taxonomy_category.csv` and `review_argument_form_taxonomy_global.csv` without changing protocol files or paper IDs. Every row now distinguishes the transferable object, skeleton explicitness, operational extraction/validation, transfer distance, novelty threat, and limitation in paper-specific language.

## Adjudication rules

- Treat a scheme taxonomy as conceptual groundwork unless the paper classifies text, annotates scheme instances, or operationalizes a downstream system.
- Treat generic component/relation mining as an extraction precursor, not as a deductive skeleton or validity result.
- Treat KG, corpus, transcription, parsing, and compression work as indirect scaffolding unless the source exposes an argument-form object or proof trace.
- Treat formal historical logic and defeasible systems as direct representation/validation precedents only when they expose rules, derivations, attacks, defeaters, burdens, or proof procedures; preserve their lack of NLP extraction where applicable.
- Reassess `S10P02` Walton & Macagno as a high-value conceptual taxonomy/boundary source, not a learned context-router precedent.
- Reassess `S10P10` Trajano et al. as the strongest direct scheme-conditioned RAG/translation novelty threat; retain its uncertainty limitation rather than treating it as weak relevance.
- Recompute category and global ranks after score changes using descending numeric score, then `(numeric category_num, numeric paper_order, literal paper_id)` for ties.

## Verification

The repaired outputs contain 124 rows, preserve the same 124 literal paper IDs, keep scores in 0–100, and have unique category/global ranks.
