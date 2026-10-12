# Scholarly/philosophical text fit review

- Viewpoint: authentic philosophical, historical, legal, dialectical, argument-mining, or academic text fit.
- Highest scores: authentic Medieval Latin, Classical Arabic, Quran/Hadith, philosophical intertextuality, and manually annotated argument corpora.
- Middle scores: real debate/science/fallacy corpora and natural-language logic with useful structure but weaker tradition provenance.
- Lower scores: formal theorem/rule worlds, generated analogy/scheme tasks, generic cultural QA, RAG/long-context controls, and premise/factuality tests.
- Adaptation rule: do not erase source language, genre, citation chain, or tradition-specific distinctions when projecting into claim/evidence/argument schemas.
- Validation: 80 input rows, 25 categories, contiguous category ranks, unique global ranks 1-80, deterministic tie-break `(category_num, paper_order, paper_id)`.
