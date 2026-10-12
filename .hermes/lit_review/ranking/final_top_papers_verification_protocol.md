# Final top-paper download and adversarial-relevance acceptance protocol

**Status:** procedure only; not executed against the repaired rankings.  
**Scope:** final acceptance of the nonbenchmark literature ranking after all reviewer repairs and the master matrix are complete.  
**Corpus boundary:** `remaining_nonbenchmark.csv` only. Do not add benchmark-producing studies, benchmark-related-but-not-new studies, invented records, or renamed paper IDs.

## 1. Preconditions and immutable inputs

Run this protocol only after the repaired reviewer CSVs are frozen and a master matrix/aggregate has been generated.

1. Preserve the literal `paper_id` exactly as stored. Accept the three protocol forms (`S##P##`, `##-##`, `##_##`) without normalizing separators.
2. Assert that `remaining_nonbenchmark.csv` contains 124 unique records and that every reviewer category/global file contains exactly those same 124 IDs, with scores in 0–100, required columns present, and unique ranks in the applicable file.
3. Require one completed category and one completed global file for each of the 25 reviewer slugs. Do not select papers from an individual reviewer file as if it were the final aggregate.
4. Confirm the repaired files and master matrix are the inputs used for selection. Keep all source CSVs immutable; write selection, resolution, download, and adjudication artifacts as new files.
5. Record the exact input paths, file hashes, generation timestamp, protocol version, and row/ID validation result in the final run manifest.

Existing source artifacts are evidence, not acceptance proof: `ranking_protocol.md`, `remaining_nonbenchmark.csv`, reviewer CSVs, the retained-paper summaries, URL/source manifests, and prior adversarial reviews must be preserved and cited by path in the run manifest.

## 2. Select the papers to verify

### 2.1 Per-perspective selection

After the master matrix is complete, select the top set **separately for each reviewer perspective**, using that perspective's final category/global score and rank. The selection rule must be declared before looking at downloads. Recommended default:

- select the top **10 global papers** for every perspective;
- also include the top **3 papers in every category** for that perspective when they are not already in its global top 10;
- include every paper explicitly marked as a high-priority novelty threat in the corpus/summary artifacts, even if it falls outside those cutoffs;
- include every low-confidence (`low`) paper that enters a selected set, because uncertainty is itself an acceptance risk.

If the owner chooses different cutoffs, record them verbatim in the run manifest and apply them uniformly. Deduplicate by literal `paper_id`, while retaining all perspectives and selection reasons for each selected record.

For each selected record retain:

- `paper_id`, category number/name, paper order, and citation from the master matrix;
- perspective, category rank, global rank, score, confidence, explanation, and evidence basis;
- every perspective in which the paper was selected and the selection reason;
- the source summary path(s) and source-manifest URL candidates.

### 2.2 Aggregate selection

Build the aggregate only from the frozen master matrix, never by averaging already-ranked positions without documenting the rule. The aggregate must expose the component scores and ranks for all perspectives, not just a final number.

Use a declared, reproducible aggregation rule. The default is:

1. join all perspective rows on literal `paper_id`;
2. verify one row per paper per perspective and no missing perspective score;
3. compute the predeclared aggregate score (prefer a transparent mean or weighted mean whose weights are recorded);
4. preserve per-perspective scores, ranks, confidence, and evidence in the master matrix;
5. sort aggregate ties by `(numeric category_num, numeric paper_order, literal paper_id)` ascending, exactly as required by `ranking_protocol.md`;
6. select the aggregate top **20** papers, plus any paper appearing in at least two perspective top-10 sets, any high-priority novelty threat, and any low-confidence paper in the aggregate top 20.

The aggregate output must distinguish “high across perspectives” from “high in one perspective but specialized.” Do not allow prestige, citation count, publication recency, venue, or writing quality to enter the score.

## 3. Resolve each selected citation to a stable scholarly source

Resolve citations before downloading. Use the retained citation, `standardized_papers.csv`, the relevant summary/agent artifact, `url_manifest.json`, `scholarly_url_manifest.json`, and existing source links as candidate evidence. Preserve every candidate and its resolution outcome.

Resolution priority:

1. DOI URL (`https://doi.org/<literal DOI>`) when a DOI is established by the paper record or publisher metadata.
2. A stable publisher or proceedings landing page with bibliographic metadata and a downloadable full text.
3. A stable scholarly repository record such as ACL Anthology, arXiv, an institutional repository, Crossref-linked record, or a library/catalog record for books and primary texts.
4. A stable official resource page for a corpus or infrastructure item only when the ranking record identifies the resource itself rather than a paper.

Do not silently substitute a near match, later survey, preprint for a different work, conference version for a distinct journal article, or a duplicate edition. If multiple versions exist, record the relation (`preprint`, `accepted manuscript`, `published version`, `chapter`, `book`, `resource`) and choose the version that best matches the paper record. DOI resolution is an identity aid, not proof that the resolved object matches.

For every selected record write a resolution row containing:

- literal `paper_id` and citation as stored;
- candidate URLs and source-manifest provenance;
- chosen URL, URL type, DOI if any, and resolution date;
- title/authors/year/venue metadata returned by the chosen source;
- match status for each field and any version/edition note;
- resolver status: `resolved`, `ambiguous`, or `unresolved`.

A citation that names only a book, ancient work, project, database, or infrastructure resource may not have a DOI. Resolve it to the authoritative scholarly edition or official research-resource page and explicitly record the edition/resource identity. Do not fabricate missing author, year, venue, DOI, or publisher data.

## 4. Download and preserve raw evidence

Do not use a search snippet as the downloaded evidence. Download from the resolved scholarly URL, following redirects and recording each attempted URL, HTTP status, content type, byte count, and final URL.

For each selected paper:

1. Prefer the publisher/proceedings PDF or the stable repository PDF. If no PDF is legitimately available, preserve the scholarly landing-page HTML and any permitted full-text HTML/XML.
2. Store the raw response byte-for-byte under a new verification run directory; never overwrite prior downloads.
3. Compute a cryptographic hash (SHA-256) of every raw file and record it with size, media type, final URL, retrieval timestamp, and tool/version.
4. Save a normalized text extraction separately from the raw file. Never treat extracted text as a replacement for the raw artifact.
5. Save the landing page/metadata response separately when it is needed to establish title, authors, year, venue, DOI, or version identity.
6. Preserve license/access notes and the exact failure trail for blocked, paywalled, rate-limited, malformed, or empty responses.

Existing files in `.hermes/lit_review/downloads/` and `scholarly_download_manifest.json` may be reused only after hash and identity verification. A prior `downloaded` status is not acceptance proof. Existing failed entries are not automatically permanent failures: retry only during the final run when a stable scholarly alternative is available, and preserve both the old and new outcomes.

Do not download the entire corpus during this acceptance test. Download only the declared per-perspective and aggregate selected sets, plus explicitly required tie/novelty-threat additions.

## 5. Confirm bibliographic identity against the paper record

A selected item passes identity verification only when the downloaded scholarly evidence matches the retained paper record on all applicable fields:

- **Title:** exact after harmless whitespace, punctuation, capitalization, and Unicode normalization; substantive wording changes require adjudication.
- **Authors:** all record authors must be present in the same work; abbreviated “et al.” is acceptable only when the full author list is confirmed by the source. Do not accept a different first author, a different work with a similar title, or an unrelated resource page.
- **Year:** publication year must match the record's stated version. If the record intentionally states `2023/ACL 2024` or online-first versus issue year, record both and explain the match; do not silently choose one.
- **Venue/type:** journal, conference/proceedings, workshop, book, chapter, repository preprint, primary text, or official resource must match the record's work type. A repository mirror is acceptable only as a host for the same work.
- **DOI/stable identifier:** if present, DOI or stable identifier must resolve to the same work; if absent, state `no DOI located` rather than inventing one.

Use a field-level identity table with values from (a) the retained paper record, (b) the scholarly metadata source, and (c) the downloaded full text where available. Require a human-readable match rationale for any normalized or versioned field. `identity_status` is one of `pass`, `pass_with_version_note`, `fail`, or `unresolved`.

## 6. Adversarial high-relevance judgment

Bibliographic identity and download success do not establish relevance. Every selected paper receives an independent hostile review against the project's exact pipeline:

> retrieve or receive source material; identify claims and evidence spans; classify argument/formal-reasoning structure across relevant traditions; recover premises, warrants, conclusions, support/attack or dialectical relations; preserve polarity, qualifiers, dependencies, and provenance; select/compress reasoning-critical context under a stated sufficiency/minimality objective; and evaluate downstream LLM reasoning with inspectable, reproducible checks.

The adversarial reviewer must read the downloaded paper or the strongest available full text, not only the abstract or ranking explanation, and answer:

1. **Pipeline location:** Which exact stage(s) does the paper implement, evaluate, or directly constrain? Mark `retrieval`, `span/claim extraction`, `argument/form classification`, `formalization/proof structure`, `dependency-aware selection/compression`, `provenance/auditability`, `downstream reasoning evaluation`, or `none`.
2. **Demonstrated versus inferred relevance:** What does the paper actually demonstrate? Separate implemented/evaluated behavior from a plausible future adaptation.
3. **Mechanism transfer:** Name the concrete transferable artifact: algorithm, representation, schema, annotation protocol, dataset/resource, verifier, baseline, metric, ablation, or failure mode. “Related to reasoning/AI/logic” is not sufficient.
4. **Exact-project fit:** Does it address natural-language, evidence-grounded, inspectable, proof-oriented context engineering for scholastic/philosophical reasoning, or only a neighboring problem such as generic compression, QA, debate, style, corpus infrastructure, or formal theorem proving?
5. **Threat/overlap:** Does it threaten a novelty claim, and if so, which narrowly stated claim? Do not inflate a generic component into a threat to the full integrated pipeline.
6. **Boundary conditions:** What does it not cover—tradition, argument form, implicit premises, negation, defeasible defeat, provenance, long-context position effects, compression fidelity, or downstream reasoning? Record limitations rather than smoothing them away.
7. **Acceptance verdict:** `retain_high`, `retain_mid`, `demote`, `false_positive`, or `insufficient_evidence`.

Apply a hostile countertest: try to reject the paper as high relevance using only its title, category label, citation prestige, benchmark status, recency, or generic topic overlap. If the paper fails once those proxies are removed, it cannot pass as high relevance. A paper may remain useful as adjacent prior art, historical grounding, or a negative/contrast case without being accepted as a top direct comparator.

Require two independent judgments for every aggregate-top paper and every item marked `retain_high`; disagreements must be adjudicated with the full-text evidence. A single judgment is acceptable for lower-ranked per-perspective additions only if the reviewer records the reason and confidence.

## 7. Fail-closed criteria

Mark the item `blocked` and exclude it from any final accepted-top list when any of the following holds:

- no stable scholarly URL or DOI can be resolved after bounded alternatives;
- the source is inaccessible, paywalled without an authorized accessible copy, blocked, empty, malformed, or only a search snippet;
- the downloaded object is not the cited work or its declared version/edition;
- title, author identity, year, venue/type, or DOI has a substantive mismatch;
- the paper is only an abstract, slide deck, citation entry, secondary summary, or unrelated resource page when full text is required for the judgment;
- the raw file, metadata response, hash, retrieval trail, or text extraction cannot be preserved;
- the item is a duplicate/version collision and the relationship cannot be established;
- high relevance depends only on the category label, reviewer intuition, benchmark status, prestige, recency, or a generic “could inform” claim;
- the adversarial reviewer cannot identify a concrete pipeline stage and transferable mechanism from the evidence;
- the paper's strongest evidence contradicts the ranking's claimed relevance or the selected score band;
- confidence is low and the unresolved uncertainty could change top-paper membership or novelty interpretation.

Fail closed means do not replace the paper with a convenient near neighbor and do not silently lower the evidence bar. Keep the item in a blocked ledger with the exact reason, attempted alternatives, and whether it may be reconsidered after a new source or an explicit owner decision.

## 8. Required outputs

Create a new run directory under `.hermes/lit_review/ranking/verification_runs/<run_id>/` containing at least:

- `run_manifest.json`: protocol version, input paths/hashes, selection cutoffs, aggregation rule, selected IDs, counts, timestamps, and tool versions;
- `selected_per_perspective.csv`: all perspective selections and reasons;
- `selected_aggregate.csv`: aggregate scores/ranks and selection reasons;
- `source_resolution.csv`: candidate/chosen URLs, DOI/stable IDs, metadata, and resolution status;
- `download_manifest.json`: every attempt, final URL, HTTP status, media type, byte count, raw path, text path, SHA-256, and failure details;
- `identity_checks.csv`: record metadata versus downloaded scholarly metadata/full text, field-level statuses, and version notes;
- `relevance_adjudications.csv`: pipeline stages, demonstrated mechanism, exact-project fit, overlap/threat, limitations, verdict, confidence, reviewer IDs, and evidence locations;
- `blocked_items.csv`: every fail-closed item and its complete failure trail;
- `evidence/`: immutable raw downloads, metadata/landing-page captures, extracted text, and reviewer evidence excerpts or page/section references;
- `final_acceptance_report.md`: accepted per-perspective and aggregate lists, demotions/false positives, blocked items, unresolved risks, and explicit statement of what was not verified.

The final report may claim acceptance only if every selected accepted item has a resolved scholarly source, preserved raw evidence, passing identity check, and completed adversarial relevance judgment. Report counts from parsed artifacts, including selected, downloaded, identity-pass, relevance-pass, blocked, failed, and unresolved totals; never infer totals from filenames or partial logs.

## 9. Final gate

The final gate is **PASS** only when:

1. the master matrix and all selections are complete and reproducible;
2. every selected accepted paper is traceable from literal `paper_id` → paper record → stable scholarly URL/DOI → hashed raw artifact → identity table → full-text relevance judgment;
3. all blocked or mismatched items are excluded from accepted-top claims and listed with reasons;
4. no ranking CSV was modified during verification;
5. independent count/duplicate/missing-ID checks pass for every generated table;
6. the acceptance report distinguishes direct high relevance, adjacent usefulness, contrast/false-positive cases, and unverified items;
7. any remaining ambiguity is explicitly labeled, not converted into a positive acceptance claim.

Until this gate passes, describe the rankings as repaired or provisional—not finally verified.
