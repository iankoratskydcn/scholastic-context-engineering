# Shard 2 scholarly verification report

- Run directory: `/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering/.hermes/lit_review/ranking/verification_runs/20261012_shard2`
- Selection input: `.hermes/lit_review/ranking/finalized_v1_1/final_verification_selection_shard_2.csv`
- Selected records: **22**
- Identity checks passed: **21**
- Blocked / fail-closed: **1**
- Raw evidence artifacts: preserved under `evidence/`; SHA-256, byte size, content type, final URL, and retrieval trail are recorded in `download_manifest.json` and `source_resolution.csv`.

## Verification result

21 records matched the retained title/author/year/venue-or-identifier fields against retrieved scholarly full text or scholarly landing metadata. Four records whose publisher pages were inaccessible were resolved through Crossref DOI landing metadata and preserved as raw JSON evidence: Trajano et al., Green, Macagno, and Millière. One downloaded item remains blocked: Abdelwahab et al. (`S24P04`). Its repository PDF is encrypted/unextractable by the available verifier, so exact identity could not be independently confirmed; no near-match substitution was made.

## Fail-closed policy

The ranking inputs and master matrix were not edited. The blocked item remains excluded from the identity-pass count until an independently extractable scholarly full text or landing metadata can confirm its identity.

## Artifacts

- `source_resolution.csv`
- `download_manifest.json`
- `identity_checks.csv`
- `blocked_items.csv`
- `evidence/`
