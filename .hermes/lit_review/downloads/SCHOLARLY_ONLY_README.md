# Scholarly-resource subset

This subset filters the 25 agent URL manifests to scholarly publisher pages, proceedings, preprints, institutional repositories, scholarly corpora, and primary-text resources.

- Candidate scholarly URLs: **394**
- Successfully downloaded: **346**
- Failed scholarly downloads: **48**
- Excluded discovery/non-scholarly URLs: **77**
- Manual-review URL excluded: **1**

Manifests:

- `../scholarly_url_manifest.json` — classification and provenance for every deduplicated URL.
- `../scholarly_download_manifest.json` — scholarly-only download status and local paths.
- `../download_manifest.json` — complete attempted-download record.

The scholarly subset includes ACL Anthology, arXiv, DOI/publisher pages, conference proceedings, OpenReview, journal platforms, PhilPapers, institutional repositories, and identified scholarly corpus/primary-text resources. Google Scholar discovery links, GitHub/project pages, product pages, and unrelated non-scholarly URLs are excluded from the subset.
