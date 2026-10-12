# Intermediate-artifact / downstream-outcome benchmark shortlist

**Slug:** `intermediate_artifact_eval`  
**Research date:** 2026-10-12  
**Scope:** Benchmarks or reusable benchmark artifacts that expose, annotate, or mechanically check an intermediate reasoning object and also measure a downstream outcome. The target is component-wise evaluation rather than answer accuracy alone.

## Selection rule

A resource is **Exact** when the same benchmark protocol can score both (1) an intermediate object such as a proof chain, entailment tree, formalization, tactic/premise dependency, or evidence citation and (2) a downstream conclusion, QA, theorem-proving, or fact-verification outcome. **Strong** resources meet the same condition with a narrower domain or less natural language. **Moderate** resources jointly score grounding/evidence artifacts and final outputs but do not provide full logical proofs. **Adjacent** resources expose intermediate traces and diagnose their faithfulness, but downstream correctness is not the primary benchmark target.

## Recommended core battery

1. **P-FOLIO** — closest direct match for human-authored reasoning chains: step-level inference-rule labels plus pass@k evaluation of generated chains and final logical conclusions.
2. **ProofWriter** — checker-backed proof certificates, depth control, True/False/Unknown, implication enumeration, and abduction.
3. **EntailmentBank** — evidence selection and multi-step entailment trees evaluated alongside question-answer hypotheses; particularly useful for proof-relevant context selection.
4. **FOLIO** — natural-language reasoning plus NL-to-FOL formalization and automated theorem-prover verification; pair with P-FOLIO for finer step-level scoring.
5. **LeanDojo/ReProver** — kernel-accepted proofs, theorem dependencies, and premise retrieval; strongest machine-checkable dependency benchmark, but least linguistically similar to scholarly prose.
6. **PRover** — generated proof trees and downstream rule-question answers, including depth and paraphrase stress.
7. **ProoFVer** — natural-logic proof sequences determine fact-verification labels, including counterfactual robustness.

## Grounding and scholarly-text complements

- **ALCE:** citation/evidence spans plus answer quality; good for provenance and source attribution, but citations are not complete proofs.
- **MISSCI PLUS:** retrieval of real scientific passages, verbalized fallacious reasoning, and downstream fact-checking; useful for authentic evidence-grounded reasoning and hallucination-sensitive evaluation.

## Faithfulness diagnostic

- **FAITHCOT-BENCH/FINE-COT:** expert-annotated trajectories with step-level evidence and unfaithfulness causes. Include as a trace-faithfulness diagnostic, not as a substitute for proof validity or final-answer evaluation.

## Implementation implication

Report separate columns or metrics for: artifact validity, artifact grounding/provenance, artifact completeness, final outcome correctness, and consistency between artifact and outcome. For proof resources, accept multiple valid derivations where possible; exact string matching against one reference chain is too strict. For the core suite, combine P-FOLIO/ProofWriter/EntailmentBank/FOLIO with ALCE or MISSCI PLUS to cover formal proof, natural-language evidence, and source attribution.

## Evidence and source verification

The shortlist was derived from the repository's benchmark-ranking protocol and retained scholarly summaries, then checked against primary ACL/PMLR/arXiv records. Primary records explicitly describe P-FOLIO's human-written chains and pass@k evaluation, EntailmentBank's multistep entailment trees and answer hypotheses, ProoFVer's natural-logic proofs determining claim veracity, and MISSCI PLUS's retrieval, verbalization, and fact-checking tasks.

Primary sources:

- P-FOLIO: https://aclanthology.org/2024.findings-emnlp.966/
- ProofWriter: https://aclanthology.org/2021.findings-acl.317/
- EntailmentBank: https://aclanthology.org/2021.emnlp-main.585/
- FOLIO: https://aclanthology.org/2024.emnlp-main.1229/
- LeanDojo: https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html
- PRover: https://aclanthology.org/2020.emnlp-main.9/
- ProoFVer: https://aclanthology.org/2022.tacl-1.59/
- ALCE: https://aclanthology.org/2023.emnlp-main.155/
- MISSCI PLUS: https://aclanthology.org/2025.naacl-long.491/
- FAITHCOT-BENCH: https://arxiv.org/abs/2510.04040

The companion CSV contains one record per shortlisted benchmark and preserves the distinction between exact, strong, moderate, and adjacent jointness.