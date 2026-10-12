# Repair report: formal-logic compatibility ranking

## Changes

- Reclassified every row by pipeline role: `prover_integration`, `formal_historical_reconstruction`, `defeasible_dialectical_semantics`, `text_to_structure`, or `conceptual_background`.
- Reserved scores 90–100 for a verified executable/prover artifact; `S08P06` (*Lean Copilot*) remains 100 as the direct Lean integration. Formal reconstructions and argumentation semantics remain below 90 unless executable/prover evidence is explicit.
- Downgraded `S21P01` to 5 as a verified HCI naming false positive. Downgraded HTR, corpus, transmission, generic context/compression, and broad conceptual papers to reflect their upstream or background role.
- Replaced benchmark-status boilerplate in every `explanation` and `evidence_basis` with mechanism-focused descriptions tied to the retained source summary. Confidence now reflects evidence for the compatibility mechanism, with low confidence retained for ambiguous `S10P10` and `S02P08`.
- Preserved all literal paper IDs and metadata. Recomputed category and global ranks using descending score, then numeric `category_num`, numeric `paper_order`, and literal `paper_id` ties.

## Calibration rubric

| Role | Compatibility interpretation | Score ceiling without executable/prover evidence |
|---|---|---:|
| `prover_integration` | Native theorem-prover interface, proof-state interaction, or verified solver artifact | 100 |
| `formal_historical_reconstruction` | Explicit states, predicates, algorithms, symbolic reconstruction, or correctness proof grounded in historical logic | 89 |
| `defeasible_dialectical_semantics` | Rule/argument graphs, attack/defeat, burden, acceptance, or formal dialogue semantics | 89 |
| `text_to_structure` | Argument components, schemes, support/attack extraction, or formal intermediate representations | 89 |
| `conceptual_background` | Context, corpus, HTR, survey, philosophical, or task-level evidence without a formal compatibility mechanism | 60 |

The score is a project-transfer judgment, not a benchmark-status judgment. Formalization, extraction, and dialectical semantics remain valuable but are not conflated with theorem-prover interoperability.

## Verification targets

- Both CSVs retain 124 rows and the original literal IDs.
- Category ranks are contiguous and unique within each numeric category; global ranks are contiguous and unique across all rows.
- Scores are integer values in 0–100.
- No row uses benchmark-only language as its sole evidence basis; each row names a mechanism class and source summary.
