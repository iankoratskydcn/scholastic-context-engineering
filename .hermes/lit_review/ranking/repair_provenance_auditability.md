# Repair report: provenance/auditability ranking

## Changes

- Recomputed category and global ranks using descending `score_0_100`, then `(numeric category_num, numeric paper_order, literal paper_id)` for equal scores.
- Replaced generic benchmark-status evidence with row-specific evidence describing source-span limits, linked metadata, formal proof/rule traces, annotation layers, perturbation procedures, or explicit limitations.
- Recalibrated corpus and infrastructure rows so textual/corpus provenance is not treated as complete claim/inference auditability.
- Reassessed the requested cases: Peskov/Hoppe 82, Trajano 84, Freedman 92, Mitsuda 86, and Shi 83.

## Interpretation used

Scores reward auditable mechanisms, not merely the existence or absence of a benchmark. Highest evidence comes from persistent links or explicit stepwise rules/proofs; controlled perturbation and evaluation procedures receive substantial credit but do not imply source-span traceability; corpus infrastructure receives credit for linked textual, witness, and annotation metadata while losing points when premise/conclusion or validity layers are absent.

## Validation

The repaired files retain the original 124 literal paper IDs. Category ranks are contiguous and unique within each category; global ranks are unique 1–124; scores agree between files; and the global ordering applies the numeric category/paper-order tie-break before literal ID.
