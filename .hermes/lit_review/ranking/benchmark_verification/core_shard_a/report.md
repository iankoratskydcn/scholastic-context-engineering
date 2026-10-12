# Core benchmark verification — shard A

Date: 2026-10-12

## Result

| Candidate | Identity | Artifact access | License/access disposition |
|---|---:|---:|---|
| S09P08 — QT-SCHEMES | PASS | BLOCKED | Public author repository contains the released CSV material, but its GitHub metadata reports `license: null` and no repository `LICENSE` file was found. Fail closed. |
| S23P12 — 741-topic argument-tree corpus | FAIL | BLOCKED | The matrix citation is wrong: ACL P19-1456 identifies Durmus, Ladhak & Cardie (2019), not Peldszus & Stede. No downloadable corpus/license was verified; attempted Cornell URLs returned HTTP 404. |
| S03P10 — LongPiBench | PASS | PASS | The arXiv identity matches. The official `thunlp/LongPiBench` repository declares MIT and links its release data archive. `data.zip` downloaded and passed `zipfile.testzip()`; it contains six benchmark JSON files (3,158,570,305 uncompressed bytes). |
| S02P07 — PCBench | PASS | PASS | The arXiv/ACL identity matches. The official project points to the public, non-gated Hugging Face dataset; metadata declares MIT. `dataset.jsonl` downloaded and parsed as 1,200 JSON records. |

## Counts

- Identity passes: **3/4**
- Verified benchmark artifacts: **2/4**
- Blocked items: **2**

## Identity findings

- QT-SCHEMES is exactly the ACL 2025 paper `2025.acl-long.368`, by Ramon Ruiz-Dolz, Zlata Kikteva, and John Lawrence; the paper describes 441 arguments annotated with 24 schemes.
- The 741-topic row has a scholarly identity defect. ACL `P19-1456` is *Determining Relative Argument Specificity and Stance for Complex Argumentative Structures* by Esin Durmus, Faisal Ladhak, and Claire Cardie. Its abstract confirms manually curated trees for 741 controversial topics and 95,312 claims.
- LongPiBench is *Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs* (arXiv:2410.14641), by Runchu Tian et al.; repository and paper names agree.
- PCBench is *Don't Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models* (arXiv:2505.23715 / ACL Findings EMNLP 2025), by Jinzhe Li, Gengxu Li, Yi Chang, and Yuan Wu.

## Artifact evidence

- `artifacts/QT-SCHEMES/`: author repository with five dated QT-Schemes CSV releases and AIF JSON files. Access is reproducible, but license is unresolved.
- `artifacts/LongPiBench_thunlp/`: official MIT repository checkout.
- `artifacts/LongPiBench_data.zip`: official release archive; manifest and response headers are preserved; archive integrity passed.
- `artifacts/PCBench_dataset.jsonl`: public Hugging Face dataset artifact; response headers, dataset API metadata, tree listing, and SHA-256 evidence are preserved.
- No verified 741-topic corpus download was found. The failed Cornell probes are preserved under `raw/cornell_*.html`.

## Evidence files

- `source_resolution.csv`
- `identity_checks.csv`
- `artifact_checks.csv`
- `blocked_items.csv`
- `raw/` — scholarly pages/PDFs, repository metadata, dataset metadata, HTTP headers, manifests, and checksums
- `artifacts/` — downloaded/check-out benchmark artifacts

The master matrix and recommendation files were not edited.
