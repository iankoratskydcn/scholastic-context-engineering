# Implementation-feasibility ranking repair

## Scope

Repaired only `review_implementation_feasibility_category.csv` and `review_implementation_feasibility_global.csv`; preserved paper IDs, scores, metadata, and `ranking_protocol.md`. Created this log as the repair record.

## Changes

- Replaced every inherited benchmark-screening `evidence_basis` with paper-specific feasibility evidence grounded in the retained subtopic summary, covering artifact/code surface, data/access burden, dependencies, reproducibility, and solo effort.
- Rewrote every explanation to name the decisive implementation surface and the principal cost or risk.
- Recomputed category ranks and global ranks using descending score and literal `paper_id` order for equal scores, without renaming legacy IDs.
- Preserved all 124 scores because the retained evidence supports the existing broad ordering and no score change was necessary to repair the evidence basis.

## Verification

Validation was run after writing: both files contain 124 rows with the same ID set as `remaining_nonbenchmark.csv`; no duplicate IDs; scores remain integers in 0–100; category ranks are unique and contiguous per category; global ranks are unique and contiguous 1–124; rank tie ordering follows `(score descending, paper_id ascending)`; explanations and evidence are non-empty and 1–3 sentences.

## Known constraint

The upstream source contains legacy/noncanonical paper IDs. This repair preserves them exactly, as required by the task, and does not edit `ranking_protocol.md` or other ranking files.
