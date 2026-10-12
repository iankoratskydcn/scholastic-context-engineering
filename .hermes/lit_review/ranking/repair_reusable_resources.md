# Repair record: reusable-resources ranking

- Scope: `review_reusable_resources_category.csv` and `review_reusable_resources_global.csv` only.
- The existing 13-column CSV schema is preserved. Resource metadata is embedded in `explanation` and `evidence_basis` as explicit `artifact_type`, `access_status`, `license_or_not_verified`, and `direct_project_relevance` statements.
- Reusable artifacts are separated from methods that are merely reimplementable. Unverified release/access claims are scored conservatively.
- `S21P01` is treated as a false-positive name match with low direct relevance; `S22P11` is described as ERC-DEBATE corpus infrastructure rather than an unsupported empirical study; `S24P14` is recognized as open ONLP/YAP software with a Modern-Hebrew transfer penalty. `S02P08` and `S10P10` remain low-confidence/uncertain.
- Corpus/infrastructure entries are distinguished by access evidence and direct relevance. Category 18 scores are differentiated by formal executability, implementation/resource support, and project fit rather than tied at 70.
- Ranks were recomputed descending by score, with ties broken by numeric `category_num`, numeric `paper_order`, then literal `paper_id`. IDs and row membership were preserved.
