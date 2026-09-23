# Argument-mining clean access inventory

Generated from the 10-agent identity audit and 10-agent acquisition audit. No large datasets were downloaded. Statuses are acquisition classifications, not permission to redistribute.

## Status meanings

- **direct** — files/annotations were observed at a public URL without a request gate.
- **direct-with-conditions** — public access exists, but license, source-text, social-media, commercial-use, or version constraints require review.
- **request-required** — author/provider request or approval is the documented route.
- **unavailable** — no usable public corpus files were found at the current canonical release.
- **conditional-follow-up** — a public route exists, but part of the resource could not be verified or retrieved reliably.
- **fragmented** — benchmark code is public, but data must be assembled from upstream corpora.

## Recommended first acquisition wave

Start with the lowest-friction, highest-value resources:

1. GDN-CC
2. PERSPECTRUM
3. KPA / ArgKP
4. Argumentative Microtext Corpus Parts 1 and 2
5. ArgUNSC
6. CasiMedicos-Arg, after resolving its CC BY/CC0 conflict
7. CEDAR, after pinning a repository commit
8. ECHR Argument Corpus, after confirming dataset redistribution terms
9. ARCT, retaining source-text rights caveat
10. SciARK, after author license clarification

## Explicitly request or recover

- UKP Sentential Argument Mining Corpus — current repository exposes request-a-copy.
- DARIUS — OSF currently exposes the paper, not corpus files.
- Twitter Arguments Facts and Sources — paper says annotated data are available upon request.
- QuoraAM real-world undercut corpus — no public data package found.
- PerspectiveArg2024 — request requires intended use and safeguards.
- GAQCorpus — request underlying corpora and then Grammarly access.
- Planned Parenthood Twitter — recover the historical ID/label release or contact authors.

## Important rights blockers

- IAM, SciARK, CDCP, DialAM, CEAMC, and parts of ArgUNSC have unclear or missing dataset-license statements.
- AAEC, UKP, AbstRCT, DARIUS, ARCT, ECHR, and ArgSciChat contain source-text or third-party-content rights that are not automatically cleared by repository/code licenses.
- Twitter/ImageArg/GerCCT resources generally require ID hydration and cannot guarantee recovery of deleted, protected, suspended, or unavailable content.
- DebateSum is directly accessible but large (~1.25 GB) and includes upstream evidence whose rights should be treated separately.

## Provenance spot-checks

- IAM: https://aclanthology.org/2022.acl-long.162/
- ARIES: https://aclanthology.org/2024.argmining-1.1/
- AMResources correction: https://aclanthology.org/2026.argmining-1.5/
- Actual AMResources catalog target: http://purl.archive.org/amresources
- M-Arg: https://zenodo.org/records/5653504
- GDN-CC: https://huggingface.co/datasets/LequeuISIR/GDN-CC
