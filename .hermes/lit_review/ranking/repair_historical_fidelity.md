# Historical-fidelity ranking repair

- Replaced all 40 generic `evidence_basis` values with summary-file paths, section/item references, and paper-specific findings.
- Rewrote 45 boilerplate explanations in categories 1, 4, 18, and 20; each now names the paper-specific contribution and its historical-fidelity limitation in 1–2 sentences.
- Preserved all paper IDs, metadata, row counts, scores, ranks, confidence values, and tie ordering; no score changes required, so ranks were not recomputed.
- Updated only `review_historical_fidelity_category.csv`, `review_historical_fidelity_global.csv`, and this repair log.
