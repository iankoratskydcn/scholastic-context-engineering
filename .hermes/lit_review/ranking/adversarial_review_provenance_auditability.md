# Adversarial review: provenance/auditability ranking

## Scope and method

Reviewed:

- `review_provenance_auditability_category.csv`
- `review_provenance_auditability_global.csv`
- `remaining_nonbenchmark.csv`
- `ranking_protocol.md`
- sampled source summaries in `summaries/02_logic_hallucination_summaries.md`, `summaries/21_scholastic_method_ai_direct_summaries.md`, `summaries/22_scholastic_digital_humanities_ai_summaries.md`, `summaries/23_disputatio_dialectical_ai_summaries.md`, and `summaries/25_ai_philosophy_dialectical_methods_summaries.md`.

The review checked row/ID/rank integrity, score ordering, whether explanations identify row-specific auditable features, and whether `evidence_basis` supports the claimed source-span/citation trace rather than merely naming a venue, artifact class, or absence of a benchmark.

## Structural validation

- All three CSVs contain 124 data rows; category/global outputs contain exactly the 124 IDs in `remaining_nonbenchmark.csv`, with no missing, extra, or duplicate IDs.
- Scores are within 0–100 and category ranks are contiguous and unique within each category.
- Global ranks are unique and cover 1–124.
- Category and global scores agree for every paper.
- **Failure:** the global file violates the protocol's explicit equal-score tie-break rule at ranks 107–110. The protocol requires canonical `paper_id` order for equal scores, but the file orders `S01P07` and `S09P04` before `15-04` and `15-11` despite all four scoring 70. Correct lexical paper-ID order is `15-04`, `15-11`, `S01P07`, `S09P04`.

## Findings

### 1. Global tie-break is not reproducible (severity: high)

Evidence: `review_provenance_auditability_global.csv:108-111` (global ranks 107–110). All four rows have score 70, but the order is `S01P07`, `S09P04`, `15-04`, `15-11`, not canonical `paper_id` order. This means an independent implementation of `ranking_protocol.md` produces a different global ranking even though the scores match.

**Required correction:** reorder those four rows/ranks, then revalidate all global ranks.

### 2. Evidence basis frequently does not identify auditable source evidence (severity: high)

At least 40 of 124 global rows use the identical generic evidence string:

> `Source evidence: source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact`

This occurs throughout the historical-logic, Toulmin/defeasible-logic, and AI-generated-writing groups. It does not identify a paper section, passage, result, dataset record, formal rule, URL, or source-summary location. It supports only the negative claim “not a benchmark,” not the positive provenance/auditability score. The same generic wording is also present in the category file for those rows.

Other rows cite an artifact section or summary file, but most still provide no concrete source span. For example, the high-ranked rows in `review_provenance_auditability_global.csv:2-10` cite summary-level descriptions rather than a claim-bearing passage or explicit citation target. This is insufficient for a reviewer whose stated viewpoint is source-span-to-claim/inference traceability.

**Required correction:** replace generic evidence with row-specific references: summary path plus section/line, paper page/figure/table, or a stable URL/identifier and the exact claim supported. Separate “source is citable” from “the paper exposes a traceable claim-to-span/inference mapping.”

### 3. Explanations are repeated templates rather than row-specific reasoning (severity: medium-high)

The global file reuses only five explanation templates; the “strong provenance” template appears for 51 rows, and the “controlled empirical evidence” template appears for 23 rows. Template reuse is not itself invalid, but here it often substitutes for the required concrete feature that drove each ranking. The wording does not distinguish a linked-data corpus, a formal proof, a controlled human experiment, a benchmark, a model architecture, or a survey citation map.

This is especially problematic for the 100-point block: `S22P07`, `S22P09`, `S22P10`, `S22P11`, `S22P12`, `S22P13`, `S22P14`, and `S24P03` all receive 100 with essentially the same explanation despite materially different evidence types.

**Required correction:** state the auditable mechanism per row—for example, persistent token IDs and linked annotation layers; explicit formal rules and proof obligations; citable manuscript/witness metadata; or a controlled experimental protocol—and state what remains unauditable.

### 4. Perfect scores conflate corpus provenance with claim/inference auditability (severity: high)

The top-ranked rows are mostly infrastructure or formalization sources, but their own summaries explicitly limit the claims they support:

- `summaries/22_scholastic_digital_humanities_ai_summaries.md:29` says the LiLa/Index Thomisticus contribution is linked-data interoperability and “should not be mistaken for an argument graph or reasoning engine.”
- `:37` describes *Corpus Thomisticum* as searchable corpus/retrieval infrastructure, not argument-aware retrieval or reasoning validation.
- `:45`, `:49`, and `:53` describe ERC-DEBATE, the Arabic–Latin Corpus, and UniQ as corpus/transmission or bibliographic infrastructure, not premise/objection/reply or validity annotations.
- `:57` says Dutilh Novaes is a formal, interpretive reconstruction whose alignment with manuscript passages and competing readings remains open.
- `summaries/24_islamic_comparative_scholastic_ai_summaries.md:10-13` describes the Abdelwahab papers as conceptual formalizations without released benchmarks or empirical validation.

These resources can be highly valuable upstream provenance assets, but a score of 100 implies maximal auditability for the project's stated source-span-to-claim/inference criterion. The evidence supports “excellent citable source/corpus infrastructure” more strongly than “complete claim-level audit trail.” The ranking needs a distinction between bibliographic/textual provenance, annotation provenance, formal proof traceability, and empirical claim verification.

**Required correction:** either lower/calibrate these scores or add a decomposed rationale showing which auditability dimension earns the score and which dimensions are absent.

### 5. Low score for Peskov/Hoppe is driven by benchmark-release status, not auditability evidence (severity: medium-high)

`S02P08` is global rank 119 with score 67 and low confidence. Its evidence basis (`review_provenance_auditability_global.csv:120`) emphasizes that the underlying benchmark is unnamed and that no formal suite release is established. The source summary gives stronger auditability evidence: `summaries/02_logic_hallucination_summaries.md:33-35` identifies seven perturbed datasets, two intervention families (adversarial noise and counterfactual statements), the reasoner/formalization/error-recovery dimensions, and reported findings, with a stable arXiv source.

The absence of a named released benchmark weakens reuse and replication, but it is not equivalent to weak claim-level provenance. The ranking currently appears to penalize “not a benchmark artifact” more heavily than the protocol's provenance/auditability criterion warrants.

**Required correction:** score separately for reproducible source citation, explicit perturbation/procedure description, released artifacts, and span-level traceability. Reassess `S02P08` and similar rows under that decomposition.

### 6. Strong adjacent argumentation systems are not evaluated on their actual span/citation trace (severity: medium)

The rank for `S21P02` (Freedman et al.) is high at 95, while `S21P06` (Mitsuda et al.) is also 95 and `S21P10` (Shi et al.) is 94. Their summaries show meaningful structured evidence, but different auditability properties:

- `summaries/21_scholastic_method_ai_direct_summaries.md:13` says Freedman constructs argumentation frameworks and applies formal reasoning to claims, but does not implement the scholastic sequence.
- `:29` says Mitsuda preserves a hand-crafted argumentative skeleton and evaluates naturalness/consistency, but does not model explicit scholastic stages.
- `:45` says Shi reports automatic and human evaluation gains, while the opened record does not define scholastic data structures.

The CSV explanations collapse these distinctions into “inspectable computational structures.” They do not state whether source spans are preserved, whether generated claims link back to evidence, whether annotations are human-verifiable, or whether evaluation checks provenance versus only output quality. The ranks may be directionally plausible, but the evidence reasoning is under-specified and cannot justify fine ordering among these rows.

**Required correction:** add the actual traceability property for each system and avoid treating formal structure alone as citation/provenance auditability.

## Sampled low-end rows

- `S10P10` (Trajano et al.) is rank 123/124 with score 66 and low confidence. The source summary `summaries/10_walton_schemes_nlp_summaries.md:23` identifies scheme-conditioned context, RAG, and translation into computational arguments, making it a direct structured-representation precedent. Its evidence basis correctly notes uncertainty about whether evaluation data are new or reused, but the score appears to conflate uncertain dataset provenance with weak method-level auditability. This should be split into separate dimensions.
- `S06P03` (Shanahan) is last at 62. The summary `summaries/25_ai_philosophy_dialectical_methods_summaries.md:3` supports low empirical reproducibility but gives a clearly citable conceptual argument and explicit evaluation warnings. A low score is defensible only if the rubric explicitly prioritizes empirical/source-span traceability over conceptual citation auditability; that weighting is not stated in the CSV.
- `S01P01` and other survey rows are generally clustered at 67–71, but the evidence often only says “survey” and “no benchmark.” Surveys can be strong provenance maps when their cited taxonomy and definitions are directly traceable; the ranking does not distinguish a well-indexed citation map from an uncited conceptual overview.

## Verdict

The files are structurally close to valid, but the provenance/auditability judgment is not yet auditable enough for acceptance. The principal defect is not missing rows; it is criterion drift: benchmark-release status and broad source type are repeatedly used as proxies for source-span-to-claim traceability. Fix the global tie-break, replace generic evidence with row-specific source spans, and recalibrate the top/bottom samples using separate provenance dimensions before treating the ranking as final.
