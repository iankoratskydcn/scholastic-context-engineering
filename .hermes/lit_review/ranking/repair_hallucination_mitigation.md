# Hallucination-mitigation ranking repair

## Scope

Repaired only `review_hallucination_mitigation_category.csv` and `review_hallucination_mitigation_global.csv`; created this repair record. Preserved every paper ID, citation, category, paper order, reviewer slug, viewpoint, and CSV schema. Did not edit the protocol or other ranking files.

## Changes

- Added an explicit directness class to every explanation: demonstrated hallucination mitigation/detection; factuality/citation reliability; formal verifier/argument representation; context/retrieval risk factor; corpus/infrastructure; or generic quality.
- Kept category 2 as the highest-directness evidence and at the top of the global ranking; reduced formal/corpus/infrastructure scores where the retained evidence does not report an LLM hallucination outcome.
- Split category 20 by mechanism: fabricated references/data and research-quality screening are factuality/citation reliability; authorship, style, genre, and normative accountability are generic quality.
- Replaced generic benchmark-screening evidence with paper/category-specific mechanisms and explicit negative evidence, including proxy-task, structured-input, transfer, and no-hallucination-outcome limitations.
- Calibrated confidence to comparative hallucination-mitigation relevance rather than citation inclusion.
- Recomputed category ranks and global ranks after score changes using descending score, with numeric `category_num` then `paper_order` for ties.

## Verification

Both CSVs contain 124 rows with the same 124 unique paper IDs; category/global shared fields agree; scores are integers in 0–100; category ranks are contiguous and unique per category; global ranks are unique and contiguous 1–124; category 2 occupies global ranks 1–5; all explanations/evidence are non-empty and include one allowed directness class.
