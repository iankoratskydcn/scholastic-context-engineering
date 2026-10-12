# Empirical-rigor ranking repair

## Rubric

Scores now assess the evidence actually reported by each paper, not whether it released a benchmark. The comparison separates:

- **Empirical design:** sample construction, controls or matched comparisons, blinding/randomization where applicable, and outcome measures.
- **Formal verification:** explicit rules, proofs, termination/correctness arguments, executable implementations, and proof status.
- **Artifact reproducibility:** inspectable data, code, prompts, annotation guidelines, and whether the reported procedure can be rerun.
- **Coverage and external validity:** domains, languages, models, participants, corpus size, and known construct limits.
- **Project transfer:** usefulness for provenance-preserving, source-grounded scholastic reasoning; this is reported separately from empirical strength.

A high score therefore requires strong evidence on the relevant dimensions and a stated limitation. Formal proof is not treated as an empirical experiment; a corpus is not treated as proof; and benchmark exclusion is not itself negative evidence. Confidence describes the stability of the comparative score given the available summary, not merely paper inclusion.

## Repairs

- Replaced generic benchmark-exclusion evidence with paper-specific samples, controls, proofs, annotation agreement, evaluations, and replication limits for categories 16, 17, 18, and 20.
- Added the category-20 identity note: inventory ID `20_11` retains its identifier and inventory citation label, while the verified source is Bhattacharyya, Miller, Bhattacharyya, and Miller (2023), DOI `10.7759/cureus.39238`.
- Recalibrated scores and confidence labels where formal verification, empirical design, coverage, or transfer limitations changed the comparison.
- Recomputed category ranks by descending score with `paper_order` ties, and global ranks by descending score with numeric `category_num` then `paper_order` ties.
