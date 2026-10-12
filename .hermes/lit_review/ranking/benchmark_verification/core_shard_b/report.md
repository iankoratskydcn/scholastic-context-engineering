# Benchmark verification — core shard B

Date: 2026-10-12

## Outcome

- Identity checks: **3 PASS / 3 checked**.
- Verified artifacts: **2** — Index Thomisticus Treebank and FOLIO.
- Blocked items: **1** — ALCE is access-reachable but license provenance is unresolved, so it is fail-closed rather than promoted.
- No master matrix or recommendation files were edited.

## S05P05 — ALCE

**Identity: PASS.** The ACL Anthology paper at https://aclanthology.org/2023.emnlp-main.398/ matches the claimed title, authors, and EMNLP 2023 venue. The downloaded first-page evidence is preserved at `papers/alce_acl.pdf`. The official repository README identifies ALCE as the Automatic LLMs' Citation Evaluation benchmark and names ASQA, QAMPARI, and ELI5 as its three datasets.

**Artifact access: PASS; promotion: BLOCKED.** The official repository download script points to the Princeton-NLP Hugging Face artifact. The 451,297,280-byte tarball was downloaded successfully, SHA-256 `eda837bf659a91b3648dc6e7ab6b17197664d93593857e8fdf3800b6aa6a98f0`, extracted, and all eight JSON files parsed successfully. The shipped files contain 948 examples for ASQA variants and 1,000 for QAMPARI/ELI5 variants. The repository's MIT license covers the code, but neither the official repository distribution nor the Hugging Face dataset page provided an explicit license covering the bundled data and its mixed upstream corpora. Under the requested fail-closed rule, ALCE remains blocked pending data-component licensing confirmation.

## S22P04 — Index Thomisticus Treebank

**Identity: PASS.** The ACL Anthology paper at https://aclanthology.org/2009.tal-2.5/ matches the claimed title, authors, and 2009 TAL venue (50(2), 103–127). The downloaded paper evidence is preserved at `papers/ittb_acl.pdf`.

**Artifact and license: VERIFIED.** The official Universal Dependencies repository identifies `UD_Latin-ITTB` as Latin data from the Index Thomisticus Treebank and states the source corpus and Medieval Latin scope. The train/dev/test CoNLL-U files were downloaded and structurally counted successfully: 22,775 / 2,101 / 2,101 sentences and 390,787 / 29,888 / 29,842 token rows. The repository license states CC BY-NC-SA 3.0. Raw source files, license, README, copied artifacts, paper, and SHA-256 values are preserved under this shard.

## Optional fallback 12-06 — FOLIO

**Identity: PASS.** The ACL Anthology paper at https://aclanthology.org/2024.emnlp-main.1229/ matches the current 2024 EMNLP paper title and author list. The Yale-LILY README preserves the 2022 arXiv lineage and exact benchmark identity. Paper evidence is preserved at `papers/folio_acl.pdf`.

**Artifact and license: VERIFIED as optional fallback.** The official Yale-LILY v0.0 repository train and validation JSONL files were downloaded and parsed successfully: 1,004 and 204 records, respectively. The repository license is Creative Commons Attribution-ShareAlike 4.0 International. The README points users to a newer Hugging Face release; this verification uses the directly accessible, versioned v0.0 repository artifact and should not be treated as verification of the newer release.

## Preserved evidence

- `raw/` — fetched READMEs, licenses, download script, FOLIO API listings, and raw data files.
- `papers/` — ACL Anthology PDFs for all three identities.
- `artifacts/alce/` — extracted ALCE evaluation/retrieval JSON files.
- `artifacts/ittb/` — UD ITTB train/dev/test CoNLL-U files.
- `artifacts/folio/` — Yale-LILY FOLIO v0.0 train/validation JSONL files.
- `source_resolution.csv`, `identity_checks.csv`, `artifact_checks.csv`, `blocked_items.csv` — machine-readable verification ledgers.

## Source URLs

1. ALCE paper: https://aclanthology.org/2023.emnlp-main.398/
2. ALCE official repository: https://github.com/princeton-nlp/ALCE
3. ALCE data artifact: https://huggingface.co/datasets/princeton-nlp/ALCE-data
4. ITTB paper: https://aclanthology.org/2009.tal-2.5/
5. UD_Latin-ITTB repository: https://github.com/UniversalDependencies/UD_Latin-ITTB
6. ITTB project site: https://itreebank.marginalia.it/
7. FOLIO paper: https://aclanthology.org/2024.emnlp-main.1229/
8. FOLIO official repository: https://github.com/Yale-LILY/FOLIO
9. FOLIO v0.0 artifact directory: https://github.com/Yale-LILY/FOLIO/tree/main/data/v0.0
