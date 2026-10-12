# Continuation retry report

- Run date: 2026-10-12
- Scope: rank 28 `S21P09` and rank 36 `S03P01` only.
- Policy: bounded exact scholarly alternatives; fail closed on inaccessible or identity-mismatched sources; no ranking/master edits.

## Results

- `S21P09` — identity pass. Exact Walton paper recovered from the University of Windsor institutional repository. Springer DOI landing metadata independently confirms title, author, journal, volume 30, publication date August 2016, pages 317–340, and DOI `10.1007/s10503-015-9387-x`. Crossref raw metadata is preserved; its 2015 online-publication date is recorded as a metadata nuance, not treated as a mismatch with the retained 2016 issue citation.
- `S03P01` — identity pass. Exact Liu et al. paper recovered from ACL Anthology, with ACL landing metadata and PDF; arXiv `2307.03172` is preserved as a corroborating scholarly record. ACL metadata confirms TACL volume 12 (2024), pages 157–173, DOI `10.1162/tacl_a_00638`, and all seven authors.

## Verification artifacts

- `source_resolution.csv`
- `download_manifest.json`
- `identity_checks.csv`
- `blocked_items.csv` (header only; no blocked items)
- `retrieval_trail.json`
- `evidence/` raw PDFs, landing pages, arXiv page, and Crossref JSON

Identity passes: 2
Blocked: 0
