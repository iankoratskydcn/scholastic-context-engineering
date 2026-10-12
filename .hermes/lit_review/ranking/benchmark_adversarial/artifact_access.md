# Adversarial benchmark review: artifact access, reproducibility, and solo-project feasibility

**Scope.** Reviewed the top 10 rows by `aggregate_mean_score` in `benchmark_master_matrix.csv` (80-study universe), preserving their literal matrix identities. The review checks exact paper identity, benchmark artifact existence, access/license/tooling evidence, reproducibility burden, and whether a solo project can run the benchmark without inventing missing infrastructure.

## Adjudication

| Rank by aggregate | Paper ID | Benchmark | Mean | Verdict |
|---:|---|---|---:|---|
| 1 | 12-06 | FOLIO | 86.64 | **RETAIN** — verified repository/Hugging Face artifact; CC-BY-SA-4.0; low setup burden. |
| 2 | S07P01 | ProofWriter | 85.04 | **RETAIN with pinned archive** — paper and direct S3 ZIP verified; license and checksum still need project-level pinning. |
| 3 | 12-04 | ProofWriter | 84.96 | **Same benchmark family as S07P01** — do not count as an independent artifact; consolidate at suite-design time while preserving both matrix records. |
| 4 | 14-08 | LeanDojo/ReProver | 83.28 | **RETAIN as heavy formal control** — Zenodo benchmark and tooling exist, but Lean/elan/GitHub-token setup is not solo-light. |
| 5 | S09P08 | QT-SCHEMES | 81.32 | **FAIL CLOSED pending artifact proof** — paper identity verified; no verified downloadable dataset/license found in the checked official sources. |
| 6 | S25P13 | QT-SCHEMES | 80.88 | **Same benchmark family as S09P08** — preserve duplicate matrix record; one artifact/access adjudication is sufficient. |
| 7 | 11-08 | MISSCI PLUS | 79.20 | **RETAIN with caveat** — repository contains dataset splits and Apache-2.0 repo metadata; README says code is still coming soon, so full paper reproduction is not proven. |
| 8 | S08P05 | Isabelle proof-state/relevant-premise pairs | 78.72 | **RETAIN as formal control** — dataset and generator are linked; no machine-readable license was found; Isabelle setup adds burden. |
| 9 | 12-05 | LogicNLI | 78.12 | **RETAIN** — paper, GitHub repository, and ZIP dataset are directly linked; artifact is easy to run, but reuse license is not verified. |
| 10 | S23P12 | 741-topic argument-tree corpus | 77.28 | **EXCLUDE until identity correction** — matrix citation is mismatched: ACL metadata identifies Durmus, Ladhak, and Cardie, not Peldszus & Stede. |

## Key findings

1. **Best solo-ready candidates:** FOLIO, LogicNLI, and ProofWriter (if the versioned archive is pinned). They have concrete machine-readable artifacts and comparatively conventional evaluation paths.
2. **Best integrated grounding candidate:** MISSCI/MISSCI PLUS. The artifacts are unusually close to the target evidence-grounded fallacy pipeline, but MISSCI PLUS is not yet a fully reproducible code release according to its README.
3. **Formal controls are real but expensive:** LeanDojo/ReProver and Magnushammer are artifact-backed, but theorem-prover environments, version pinning, and proof execution make them poor first benchmarks for a solo implementation.
4. **Fail closed on paper-only evidence:** QT-SCHEMES and US2016G1tvWALTON should not be described as available benchmark artifacts until a downloadable corpus and reuse terms are independently verified.
5. **Correct identity before ranking:** the 741-topic argument-tree row currently conflates a 2019 ACL paper by Durmus, Ladhak, and Cardie with Peldszus & Stede. This is a scholarly-identity defect, not merely an access gap.
6. **Duplicate-family handling:** ProofWriter, QT-SCHEMES, and LeanDojo appear in multiple matrix perspectives. The CSV preserves each top-row paper ID, while the report flags that artifact readiness should be adjudicated once per benchmark family to avoid false suite breadth.

## Reproducibility recommendations

- Pin exact artifact URLs, archive versions, and checksums for ProofWriter and FOLIO before experimental reporting.
- Separate `paper accessible`, `artifact downloadable`, `license verified`, and `full pipeline reproducible`; none implies the others.
- For MISSCI PLUS, report dataset-only replication separately from full method replication until the missing/unfinished code path is resolved.
- Treat missing license metadata as an unresolved reuse condition, not as permission to redistribute.
- Keep LeanDojo/Magnushammer in a secondary formal-control tier rather than making them prerequisites for the first solo benchmark battery.

## Sources checked

- FOLIO repository and release: https://github.com/Yale-LILY/FOLIO; https://huggingface.co/datasets/yale-nlp/FOLIO; https://aclanthology.org/2024.emnlp-main.1229.pdf
- ProofWriter paper and archive: https://aclanthology.org/2021.findings-acl.317/; https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip
- LeanDojo tooling and benchmark: https://github.com/lean-dojo/LeanDojo; https://doi.org/10.5281/zenodo.8016385; https://leandojo.readthedocs.io/en/latest/user-guide.html
- QT-SCHEMES paper: https://aclanthology.org/2025.acl-long.368/
- MISSCI PLUS repository and paper: https://github.com/UKPLab/naacl2025-missciplus; https://aclanthology.org/2025.naacl-long.491
- Magnushammer artifact and paper: https://github.com/Simontwice/MagnusData; https://huggingface.co/datasets/Simontwice/premise_selection_in_isabelle; https://arxiv.org/abs/2303.04488
- LogicNLI repository and paper: https://github.com/omnilabNLP/LogicNLI; https://aclanthology.org/2021.emnlp-main.303/
- Identity check for the 741-topic row: https://aclanthology.org/P19-1456/; https://arxiv.org/abs/1906.11313
- Walton annotation paper/corpus context: https://pmc.ncbi.nlm.nih.gov/articles/PMC7888437; https://link.springer.com/article/10.1007/s10503-020-09519-x

**Files created:** `benchmark_adversarial/artifact_access.csv` and this report. The benchmark master matrix was not edited.
