# Evaluation-quality ranking notes

- Perspective: evaluation quality and diagnostic rigor. Scores reward diagnostic task design, annotation/label validity, split and leakage controls, perturbation coverage, baselines, objective metrics, reproducibility, and statistical usefulness. Dataset size or release status alone does not raise score.
- Strongest candidates: formal checker-backed proof suites (LeanDojo, ProofWriter, FOLIO/LogicNLI), controlled long-context suites (RULER/LongPiBench), and grounded argument corpora with explicit spans/relations (QT-SCHEMES, Walton, argument-tree resources).
- Caveat: many records are adjacent resources, not direct tests of full source-to-proof scholastic context engineering. Synthetic suites score for control and repeatability but lose authenticity; small expert corpora score for structural labels but lose statistical power.
- Tie rule: global ranks sorted by score descending, then numeric category number, numeric paper order, literal paper_id.
- Evidence basis preserves supplied benchmark evidence and points to retained category summaries.
