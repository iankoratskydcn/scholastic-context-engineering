# Adversarial benchmark review — semantic and exact pipeline fit

## Scope and verdict

Reviewed the 20 highest aggregate candidates in `benchmark_master_matrix.csv`, ordered by `aggregate_mean_global_rank`. The proposed pipeline is **source text → argument/form classification → deductive/proof/dialectical skeleton → provenance/dependency-preserving selection/compression → inspectable reasoning**.

**Overall verdict: REVISE / suite, not standalone benchmark.** No single top-20 candidate tests the complete pipeline. The strongest candidates are complementary component benchmarks: QT-SCHEMES, Walton/EthiX, MISSCI/MISSCI PLUS, FOLIO, LeanDojo/Magnushammer, and deep argument-structure resources. ProofWriter and RuleTaker are useful controlled baselines but are synthetic; LeanDojo and Magnushammer are strong selection controls but formal-only. Duplicate records materially inflate apparent coverage: ProofWriter appears as `S07P01` and `12-04`, QT-SCHEMES as `S09P08` and `S25P13`, and LeanDojo as `14-08`, `S07P08`, and `S08P04`.

## Coverage counts

- Reviewed: **20** unique matrix rows.
- Direct component/subpipeline candidates: **10**.
- Adjacent diagnostic/control candidates: **9**.
- Synthetic/formal-only controls: **1**.
- No candidate received a complete-pipeline verdict.

## Main adversarial findings

1. **Aggregate rank overstates exact fit.** High scores mostly reward one strong layer—formal deduction, scheme classification, evidence retrieval, or premise selection—without requiring the same item to expose all five pipeline stages.
2. **Generic QA and formal-only false positives must be demoted.** RuleTaker, LogicNLI, ProofWriter, LeanDojo, Magnushammer, and SMARTYPAT-BENCH provide valuable controls, but their task interfaces bypass or simplify source interpretation, broad argument forms, provenance, or dialectical reasoning.
3. **Synthetic resources must not stand in for scholarly authenticity.** ProofWriter and RuleTaker offer deterministic proof/depth stress; they do not test ambiguous, historically situated, cross-tradition text. Synthetic oracles in SMARTYPAT-BENCH validate intended generated patterns, not complete pragmatic adequacy.
4. **Argument-mining resources stop before selection/compression.** QT-SCHEMES, US2016G1tvWALTON, EthiX, ElecDeb60To16, the 741-topic trees, and the causal/deep-structure corpora make extraction and form/skeleton errors visible, but none evaluates whether a provenance-linked minimal context preserves downstream reasoning.
5. **Selection resources stop before semantic interpretation.** LeanDojo/ReProver and Magnushammer prove that proof-state-aware retrieval matters, yet exact formal proof success cannot substitute for natural-language provenance, implicit warrants, or cross-tradition adequacy.
6. **Evidence-grounded fallacy resources are closest to an inspectable subpipeline.** MISSCI and MISSCI PLUS connect claims to source passages and require reconstruction/verbalization, but remain biomedical fallacy tasks without general scheme coverage or dependency-aware compression.

## Recommended suite composition

- **Form/scheme layer:** QT-SCHEMES plus US2016G1tvWALTON and EthiX; retain both natural dialogue and human ethical debate, and report ambiguity/multilabel behavior.
- **Structure/skeleton layer:** 741-topic argument trees, deep argumentative structures, and implicit causal-link materials.
- **Evidence/provenance layer:** MISSCI PLUS and MISSCI.
- **Deductive/verification controls:** FOLIO and one ProofWriter family record; use RuleTaker as a synthetic negative/control condition.
- **Selection/dependency controls:** one LeanDojo/ReProver record and Magnushammer; report them as formal controls, not scholarly-text evidence.
- **End-to-end gap:** add a project-owned paired evaluation with raw source text, extracted form/skeleton, provenance-linked selected context, compressed context, and downstream inspectable reasoning. Score each artifact separately and include adversarial distractors, omitted dependencies, alternative valid parses, and cross-tradition examples.

## Candidate-level notes

The accompanying `semantic_fit.csv` contains one paper-specific row for each reviewed candidate, with explicit caveats, stage coverage, evidence basis, and recommended use. Scores are semantic-fit scores for the exact pipeline, not prestige or aggregate benchmark quality; duplicate benchmark families should be collapsed before suite-level aggregation.

## Evidence basis

All judgments are grounded in the retained local evidence files cited per row in `semantic_fit.csv`, chiefly:

- `.hermes/lit_review/summaries/12_deductive_benchmarks_summaries.md`
- `.hermes/lit_review/summaries/07_neurosymbolic_summaries.md`
- `.hermes/lit_review/summaries/09_argument_mining_summaries.md`
- `.hermes/lit_review/summaries/10_walton_schemes_nlp_summaries.md`
- `.hermes/lit_review/summaries/11_fallacy_detection_summaries.md`
- `.hermes/lit_review/summaries/14_premise_context_selection_summaries.md`
- `.hermes/lit_review/summaries/18_toulmin_defeasible_summaries.md`
- `.hermes/lit_review/summaries/23_disputatio_dialectical_ai_summaries.md`
- `benchmark_studies.csv` and `benchmark_ranking_protocol.md`.
