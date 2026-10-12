# Literature source download bundle

Generated from the 25 agent artifacts under `../agents/`.

- Raw URL occurrences: 492
- Deduplicated URL records: 472
- Non-Scholar source URLs attempted: 405
- Successfully downloaded: 354
- Unique downloaded content hashes: 319
- PDF files: 169
- HTML/XHTML landing pages: 185
- Failed downloads: 51

## Files

- `../url_manifest.json` — URL-level deduplication manifest, including agent provenance.
- `../download_manifest.json` — every attempted source URL, fetched URL, status, content type, byte count, and local path.
- `../content_dedup_manifest.json` — content-hash groups for identifying duplicate downloads.
- `./` — downloaded PDFs and landing pages, named by SHA-256 prefix of the source URL.

## Failure policy

Scholar discovery URLs were excluded from download attempts. DOI, publisher, and book pages that returned 403/404, TLS failures, or connection failures remain listed in `download_manifest.json`; they were not replaced with guessed or fabricated copies. The agent artifacts retain the original verified source URLs and fallback routes.
