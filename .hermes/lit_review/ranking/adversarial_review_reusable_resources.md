# Adversarial review: reusable-resources ranking

**Reviewed:** 2026-10-12
**Inputs:** `review_reusable_resources_category.csv`, `review_reusable_resources_global.csv`, `remaining_nonbenchmark.csv`, `ranking_protocol.md`, and the cited subtopic summary artifacts.

## Verdict

**CONDITIONAL FAIL — structural validation passes, but the ranking is not yet a reliable ranking of reusable, accessible resources.** The files contain the required 124 papers and their ranks are internally consistent, but the scoring frequently treats conceptual papers and reimplementable methods as resources, does not consistently verify access or release status, and contains several evidence/explanation contradictions.

## Validation results

- `remaining_nonbenchmark.csv`: 124 unique paper IDs.
- Category review: 124 unique IDs; exact ID set match; scores 25–96; category ranks are unique within every category and reproduce descending score/canonical-ID ordering.
- Global review: 124 unique IDs; exact ID set match; scores 25–96; global ranks are unique and reproduce descending score/canonical-ID ordering.
- Required blank-rank convention is satisfied: category file has blank `global_rank`; global file has blank `category_rank`.
- No duplicate IDs or out-of-range scores were found.
- Therefore the defects below are semantic/evidentiary rather than CSV mechanics.

## Findings

### 1. The ranking conflates “reusable resource” with “method that could be reimplemented” — **high severity**

Many explanations award substantial scores for papers that the evidence explicitly says do not release a dataset, codebase, benchmark, or formal suite. Examples include S04P01–S04P02, S04P04–S04P12, S13P01–S13P03, and S21P02/S21P05/S21P06/S21P07. “Concrete method or architecture that can be reimplemented” is a valid novelty/usefulness dimension, but it is not proof that a reusable resource is available or accessible. The protocol asks this reviewer to judge reusable data, code, and resources; the score rubric needs separate artifact-type and access evidence rather than treating reimplementation possibility as resource availability.

### 2. S21P01 is materially over-ranked despite being a verified false positive — **high severity**

`S21P01` receives 92 and rank 1 in category 21, but the cited summary states that *Scholastic* is an HCI/ML system unrelated to medieval scholastic method and that its exact project relevance is low. It is a potentially reusable HCI workflow, but the evidence does not establish a corpus, annotation tool release, code availability, or direct scholastic-method relevance. The summary supports an adjacent, moderate score at most, not the category’s top resource score.

### 3. Corpus/infrastructure entries are not scored with an explicit access test — **high severity**

The strongest-looking resource scores are S22P07, S22P09, S22P11–S22P13, and S24P08, but the ranking evidence only says “named scholarly corpus/database/infrastructure.” The summaries do provide stronger evidence: *Corpus Thomisticum* has an official searchable infrastructure; OpenITI is machine-actionable corpus infrastructure; UniQ and the Arabic–Latin Corpus are named databases/corpora; ERC-DEBATE has a corpus page. The CSV should record whether access is open, searchable-only, downloadable, API/metadata available, license known, and whether the resource is directly relevant to the project. A name alone is insufficient for the requested accessibility check.

### 4. S22P11’s explanation contradicts its own high score and source evidence — **high severity**

`S22P11` is scored 94, but its explanation says “empirical findings without a clearly reusable released dataset, codebase, or formal resource.” Its evidence basis identifies ERC-DEBATE as a corpus-oriented project, and the summary confirms a project site and corpus page. Either the score must be reduced to reflect unverified access, or the explanation must explicitly identify the corpus and its access status. The current row cannot simultaneously claim no reusable resource and justify a top-tier resource score.

### 5. S24P14’s explanation understates the verified reusable implementation — **medium severity**

`S24P14` is scored 78 with the explanation “empirical findings without a clearly reusable released dataset, codebase, or formal resource,” while the summary explicitly identifies ONLP/YAP, an open implementation, output layers, and an accessible source record. This is a direct evidence/explanation mismatch. It should be classified as reusable open software/infrastructure, with the domain-transfer penalty (Modern Hebrew versus historical Jewish scholastic texts) stated separately.

### 6. S04P03 is the only row that explicitly acknowledges a released dataset, but access is still unverified in the ranking — **medium severity**

`S04P03` says it offers a released compression dataset, yet the evidence basis only points to Artifact 04 and does not identify a repository, license, download, or version. The summary confirms the dataset contribution but not the access terms in this CSV. This is a good candidate for high resource value, but its confidence should be reduced or access evidence added until the release is directly verified.

### 7. Peskov and Trajano remain uncertain but receive scores that imply established reusability — **medium severity**

`S02P08` is explicitly `uncertain` with low confidence because the underlying modular benchmark is unnamed and the paper’s release status is unclear, yet it receives 68. `S10P10` is also `uncertain`/low confidence although the summary identifies scheme-conditioned RAG/translation as a strong direct prior-art threat. The ranking should distinguish “important prior art” from “accessible reusable resource”; uncertainty should materially cap resource scores unless the artifact/repository is verified.

### 8. Category 10 contains a direct annotation resource but the ranking does not distinguish resource forms — **medium severity**

`S10P05` (Online Annotation Assistant) receives 91, which is plausible, but its explanation says only “annotation infrastructure.” The summary says it integrates the Argument Scheme Key with OVA to assist annotators and construct labeled corpora. The row should state whether OVA/code, annotation schema, and resulting data are actually available, because annotation software, annotation protocol, and released corpus have different reuse profiles. The current score is not falsified, but the evidence is underspecified.

### 9. The 38-point block is a low-information default, not an adversarial ranking — **medium severity**

All S16P01–S16P14, S17P05–S17P06, S20P01–S20P13, and several other rows receive exactly 38 with near-identical explanations and generic evidence (“scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact”). This satisfies numeric uniqueness only through canonical ID order; it does not name a concrete feature driving each ranking as required by the protocol. These rows need differentiated scores or an explicit rationale that they are intentionally tied on the same measured dimensions (with artifact/access/relevance fields supporting that claim).

### 10. Category 18’s uniform 70 scores erase meaningful resource differences — **medium severity**

S18P01–S18P08 and S18P13 all receive 70 despite different contributions: formal reasoning calculi, argumentation schemes, legal-logic models, and surveys. The summaries support varying degrees of executable formalization, implementation evidence, and direct transfer to the project. Uniform scoring is especially weak here because the viewpoint should favor reusable formal representations; the rows need differentiation by executable specification, available implementation, corpus/annotation support, and project fit.

### 11. Some high scores are based on project relevance rather than resource accessibility — **medium severity**

S13P01 (`ERNIE`) and S13P03 (`KEPLER`) score 79 as structured-knowledge designs, and S24P15 scores 79 as a conceptual knowledge-graph/LLM framework. Their summaries describe methods/frameworks, but not released project-specific resources; S24P15 explicitly lacks a public benchmark, corpus, ablation, or validated implementation. These may be useful design precedents, but they should not rank alongside OpenITI, *Corpus Thomisticum*, or a released treebank without an explicit “method precedent” category or access penalty.

### 12. Duplicate-study rows inflate apparent resource coverage in category 24 — **medium severity**

`S24P05` and `S24P06` are two records for the same Maliszewski study (preprint/registered protocol and Cambridge publication). The protocol forbids merging or renaming IDs, so retaining both is correct for this ranking pass, but the review should flag that they are not independent reusable resources or independent evidence. Their current equal low scores avoid major distortion, yet aggregate counts and resource coverage must not treat them as two distinct contributions.

### 13. Evidence bases are generally summaries, not direct access verification — **medium severity**

The CSV evidence bases mostly cite “Artifact N § …” or a summary filename. The summary files often contain URLs and verification statements, but the ranking rows do not identify the actual resource URL, release artifact, license, or access result. This is adequate for traceability to a source summary, but not adequate to claim that resources are accessible. At minimum, top-ranked rows should carry a direct URL and an access label such as `open_download`, `open_search_only`, `code_open`, `metadata_only`, `restricted`, or `not_verified`.

### 14. Confidence is too high for several claims that the evidence explicitly leaves open — **medium severity**

Examples include high confidence for S04P03 despite the dataset/release details not being named in the row, high confidence for S22P11 despite corpus accessibility not being stated in the ranking row, and high confidence for S24P14 despite a domain-transfer caveat. Confidence should reflect evidence for the resource itself, not merely confidence in the paper summary.

## Sample evidence verification

- **S21P01:** summary explicitly calls it a false positive and says exact relevance is low; this conflicts with category rank 1/score 92.
- **S22P07/S22P09:** summaries identify the Index Thomisticus linked-data resource and official *Corpus Thomisticum* infrastructure; these are genuine resource candidates, but the CSV should retain direct access/licensing evidence.
- **S22P11–S22P13:** summaries identify ERC-DEBATE, the Arabic–Latin Corpus, and UniQ as corpus/database infrastructure; S22P11’s current explanation is contradictory.
- **S24P08:** summary identifies OpenITI as machine-actionable corpus infrastructure but warns about uneven edition alignment, OCR/transcription noise, and incomplete metadata; a 96 score needs an explicit accessibility/quality caveat.
- **S24P14:** summary identifies the open ONLP/YAP implementation; the CSV explanation incorrectly says no clearly reusable codebase is established.
- **S04P01–S04P12:** summaries describe methods and benchmarks used, but generally not released reusable artifacts; the repeated “can be reimplemented” rationale overstates resource status.
- **S10P05:** summary supports genuine annotation infrastructure and direct usefulness for constructing project data; access details remain absent from the ranking row.

## Recommended disposition

Keep the CSV structure and rank mechanics, but revise the semantic rubric before accepting the ranking:

1. Add explicit evidence dimensions for `artifact_type`, `access_status`, `license_or_restriction`, `direct_project_relevance`, and `verification_confidence`.
2. Cap or separately label papers that only provide methods/frameworks without an identified release.
3. Re-score S21P01 downward; repair S22P11 and S24P14 explanations; reassess S02P08 and S10P10 under uncertainty.
4. Replace boilerplate 38/70 blocks with concrete differentiating features, or document an intentional tie policy beyond canonical tie-breaking.
5. Preserve S24P05/S24P06 IDs but mark them as one underlying study for aggregation.
6. Re-run the protocol’s exact-ID/rank checks after semantic edits.

**Issue count:** 14 distinct semantic/evidentiary issues (including the access-verification gap as a recurring cross-row issue).
