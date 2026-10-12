# Next-seven identity retry report

- Run date: 2026-10-12.
- Scope: `18_07` and `S24P01` only.
- Rankings/master files were not edited.
- Identity pass: 1; blocked: 1.

## 18_07 — blocked

The retained citation is Walton & Gordon (2011), “Formalizing Informal Logic,” *Informal Logic* 31(1). Bounded retrieval found the exact title and authors at the Informal Logic landing page and PDF, and Crossref returned DOI `10.22329/il.v35i4.4335`. The downloaded PDF states *Informal Logic*, volume 35, number 4 (2015), pages 508–538. Therefore the title/authors/identifier match, but the retained year and issue metadata do not. The 2015 work was not substituted.

Attempts and raw responses are preserved under `raw/`: Informal Logic landing page, PDF, Crossref title search, plus initial Python TLS failures.

## S24P01 — identity pass

Crossref exact-DOI metadata identifies Wilfrid Hodges, the exact retained title, year 2010, DOI `10.1007/978-3-642-15025-8_18`, and *Fields of Logic and Computation* / LNCS 6300. A Shelah-hosted repository PDF downloaded successfully and its extracted text contains the exact title, author, and page-354 table-of-contents entry. Springer DOI/landing, DBLP, Crossref, and repository PDF attempts are preserved under `raw/`.

## Retrieval limitation

The local Python HTTPS client failed certificate verification for all tested hosts. Retry retrieval used `curl -k -L`; this is recorded in `raw/curl_metadata.json` and the manifest. Raw headers and bodies are retained for audit.

## Artifacts

- `source_resolution.csv`
- `download_manifest.json`
- `identity_checks.csv`
- `blocked_items.csv`
- `raw/` and `evidence/`
