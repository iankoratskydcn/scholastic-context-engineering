# Adversarial review — empirical-rigor ranking

## Scope and validation

Reviewed `review_empirical_rigor_category.csv` and `review_empirical_rigor_global.csv` against `remaining_nonbenchmark.csv` and `ranking_protocol.md`, with spot checks against the cited subtopic summaries.

Structural checks passed:

- Both review files contain exactly 124 rows, matching the 124 rows in `remaining_nonbenchmark.csv`.
- Paper-ID sets match exactly; no missing, extra, or duplicate IDs were found.
- Scores are integers in the required 0–100 range.
- Category ranks are contiguous and unique within every category; global ranks are unique 1–124.
- Category and global rows agree on all shared fields, including scores, explanations, and evidence bases.
- Category and global orderings are monotone by score, and equal-score rows follow canonical `paper_id` order.
- Required rank columns are populated in the correct file and blank in the other file.

These checks establish format/rank integrity, not methodological validity.

## Findings

### 1. High-severity — evidence basis is materially non-specific for 40 rows

Rows in categories 16, 17, 18, and 20 use the same generic evidence statement: `source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact`. This occurs for all 14 category-16 rows, both category-17 rows, all 11 category-18 rows, and all 13 category-20 rows. The protocol requires `evidence_basis` to point to source summary or paper evidence, and the review task asks for evidence support; “no benchmark-producing artifact” is not evidence of empirical rigor and does not identify the study design, sample, experiment, theorem, implementation, or validation actually used.

This is especially problematic because the summaries contain concrete evidence that is omitted. For example, the category-20 summary reports 50 generated abstracts, AUROC 0.94, 300 physics essays, five markers, 600 reviewer judgments, 1,000,000 arXiv abstracts, 51 articles evaluated 15 times, and 115 reference checks. Category 18 reports executable argument systems, proofs, annotation studies, 357 relations, 74.6% coverage, 85.9% agreement, and a 26.3K-sample/7-model TRACE evaluation. Category 16 reports a computer program, reduction analysis, theorem results, and an Agda implementation sketch.

### 2. High-severity — the ranking criterion conflates empirical rigor with benchmark/new-artifact status

The evidence repeatedly treats absence of a named benchmark or released dataset as the main reason to lower a paper’s empirical-rigor score. The protocol excludes benchmark-producing studies from the pool, but it does not define benchmark release as the empirical-rigor axis. A controlled experiment, blinded assessment, annotation protocol, formal correctness proof, executable implementation, or reproducible corpus analysis can be methodologically strong without releasing a benchmark.

This conflation is visible in repeated explanations such as “lack of a dedicated reusable benchmark limit[s] reproducibility” for surveys and methods, even when the cited summaries describe controlled evaluations. Conversely, formal/conceptual papers are scored relatively high on the basis of inspectability while their lack of empirical validation is not consistently penalized. The scores therefore mix at least three constructs—empirical design quality, formal verifiability, and reusability of an artifact—without stating weights or applying them consistently.

### 3. High-severity — explanations fail the protocol’s “concrete feature” requirement for 35 rows

The exact generic explanation “Primarily conceptual, survey, or foundational work; it informs the project’s evidence framework but lacks a controlled empirical evaluation of the target behavior.” is used for 35 rows, including every row in categories 16, 17, and 18’s survey entry plus multiple philosophy/argumentation rows. It does not name the concrete feature that drove the rank for an individual paper. The same problem appears in the repeated “concrete evaluation, annotation, corpus, or implementation result” explanation used for 32 rows and the repeated “concrete method or analysis” explanation used for 14 rows.

A valid explanation should distinguish, for example, “formal correctness proof of reconstructed syllogistic diagrams,” “small-domain stylometric PCA protocol,” “blinded five-marker essay grading,” “600 reviewer judgments,” or “annotation agreement on deep argumentative relations,” rather than assigning a template label.

### 4. High-severity — category 20 is under-supported and likely under-differentiated despite unusually rich empirical evidence

All 13 category-20 rows receive the same generic evidence basis even though the summary differentiates experimental designs and limitations in detail. The category contains randomized/blinded or quasi-controlled human studies, large-scale corpus analysis, repeated-measures evaluator validation, citation-integrity audits, and normative analysis. The ranking itself is plausible in broad outline, but the evidence trail cannot justify the fine ordering because it does not say why Yeadon (82) outranks Gao (78), why Levin (76) outranks Sadasivan/Bhattacharyya (74), or why Thelwall (63) outranks Schwitzgebel (55) under the chosen empirical-rigor dimensions.

The category also contains a known citation/identity correction in the summary: the inventory label “Sadasivan et al.” corresponds to the verified Bhattacharyya et al. reference-integrity study. The review preserves the inventory citation but does not flag the mismatch in `evidence_basis`, leaving the source identity ambiguous.

### 5. High-severity — category 16 scores do not reflect the summary’s actual methodological distinctions

All category-16 evidence bases are identical, and the scores appear to be an unsupported ordinal ordering rather than a comparison of methods. The summary distinguishes: Aristotle’s primary historical text; Corcoran’s secondary reconstruction; Glashoff’s executable computational reduction analysis; Dutilh Novaes’s formalization methodology; Panday and Ghosh’s frontier type-theoretic formalization with internal theorems and an Agda sketch; and several broad historical syntheses. Yet the review gives S16_12 57, S16_03 55, S16_07 52, and many lower scores without naming which verification or empirical-rigor dimensions drive those gaps.

For this category, the reviewer should explicitly separate formal proof/verification strength, executable implementation, corpus or textual coverage, independent validation, and historical-source uncertainty. The current ranking is not auditable from its evidence fields.

### 6. Medium-severity — confidence labels are overconfident relative to the evidence quality

The files assign `high` confidence to nearly all rows, including rows whose evidence is explicitly generic, whose summary is conceptual or programmatic, or whose source is a frontier preprint. Examples include S16_12 (the summary calls for independent validation), S24P15 (the summary explicitly reports no benchmark, corpus, ablation, expert agreement, or historical evaluation), and category-20 rows where the inventory citation/source identity is corrected in the summary. Confidence should describe confidence in the comparative score, not merely confidence that the paper belongs in the category.

The `low` labels on S02P08 and S10P10 show that uncertainty can be represented; the same discipline should be applied to unsupported fine-grained comparisons and source-summary limitations elsewhere.

### 7. Medium-severity — formal correctness and empirical evaluation are not calibrated onto a common scale

S24P02 receives 78 based on a symbolic reconstruction and correctness proof, while S21P10 receives 80 for automatic and human evaluation of an LLM tutoring system; S16_12 receives 57 for a formal type-theoretic paper, while S16_03 receives 55 for executable computational analysis. These may be defensible cross-construct judgments, but the files never state whether a formal proof is being treated as equivalent to empirical reproducibility, whether task coverage and external validity matter, or how independent replication is weighted.

Without an explicit rubric, the global ranking’s cross-category comparisons are not reproducible: readers cannot tell whether a theorem, an implementation, a blinded human study, and a corpus-scale observational analysis are being scored on one dimension or on incomparable substitutes.

### 8. Medium-severity — the ranking omits important negative evidence and study limitations when assigning high scores

Several high-scoring rows have limitations that materially affect empirical rigor but are absent from the explanation/evidence basis. The category-20 summary notes one-author convenience samples and self-evaluation for Thelwall, fabricated abstracts for Levin, domain/model/version dependence for Gao and Yeadon, and provenance-vs-truth construct limitations across the category. Category 18 notes that many formal systems presuppose structured inputs and do not validate extraction or LLM performance. Category 24 notes that Hodges’ proof reconstruction is narrow and that formalized fiqh claims are programmatic rather than validated performance.

The current explanations generally state only a positive method label or only “no benchmark,” so they do not support the score’s balance of strengths and threats to validity.

## Overall verdict

**FAIL — structurally valid but methodologically not release-ready.** The two CSVs satisfy the row/ID/rank mechanics, but the empirical-rigor judgment is not sufficiently auditable. The main repair is to replace generic evidence bases and explanations with paper-specific method/validation facts, then re-score using an explicit rubric that separates empirical design, formal verification, reproducibility/artifact availability, coverage/external validity, and project-transfer value. Do not treat the current global order as a defensible evidence-weighted ranking until those fields are repaired.
