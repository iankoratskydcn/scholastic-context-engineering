# Adversarial review: interdisciplinary-bridge ranking

**Artifacts reviewed**
- `ranking_protocol.md`
- `remaining_nonbenchmark.csv`
- `review_interdisciplinary_bridge_category.csv`
- `review_interdisciplinary_bridge_global.csv`
- Source summaries for sampled high/low rows, especially subtopics 01, 10, 20, 21, 22, 23, and 24.

## Verdict: REVISE

The two review files pass the basic row/column and rank-integrity checks, but the ranking is not ready to accept as evidence-grounded because several explanations are boilerplate, many evidence fields are non-specific, one evidence claim contradicts the source summary, and a documented false positive is scored as a relatively strong bridge.

## Checks that passed

- Both files contain exactly 124 data rows, matching `remaining_nonbenchmark.csv`.
- Paper-ID sets match exactly; no missing, extra, or duplicate IDs.
- Required columns are present and non-empty where required.
- Category file has blank `global_rank`; global file has blank `category_rank`.
- Scores parse as integers in the 0–100 range.
- Category ranks are contiguous and unique within every category.
- Global ranks are unique and contiguous from 1 through 124.
- Source identity fields (`category_num`, `category`, `paper_order`, `citation`) match the remaining-paper inventory.
- Global ordering and category ordering follow descending score with `paper_id` tie-breaking.
- Explanations are syntactically 1–3 sentences.

## Exact issues requiring revision

### 1. Evidence basis is materially under-grounded for 40 rows

For 40 rows, the `evidence_basis` is the same generic statement: `source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact`. This does not identify the source summary, section, result, method, or paper-level feature that supports the interdisciplinary-bridge score. It is especially inadequate for the complete category-16 set, the category-18 set, and the category-20 set. The protocol requires evidence pointing to source summary or paper evidence, not a generic classification label.

**Required fix:** replace each generic basis with a row-specific source citation and concrete contribution, e.g. summary path plus section/item and the actual formalization, argument representation, corpus resource, or evaluation finding that drives the score.

### 2. `S01P03` contains a source-grounding contradiction

Both ranking files state for Rawte et al. (`S01P03`) that the artifact does not attribute a named dataset, task, benchmark, or formal evaluation suite. The verified source summary for subtopic 01 states that Rawte et al. release the named HILT dataset (75,000 samples) and propose the Hallucination Vulnerability Index. The paper may still be classified as `not_benchmark` under the project’s benchmark definition, but the current evidence sentence is factually false and cannot support the row as written.

**Required fix:** distinguish “introduces a dataset but not a benchmark/formal evaluation suite” from “introduces no named dataset.” Reassess the score if the released dataset materially changes interdisciplinary value.

### 3. Explanations do not satisfy the protocol’s concrete-feature requirement for most rows

There are only 32 unique explanations across 124 rows; 108 rows reuse an explanation shared by at least one other paper. Entire categories receive the same explanation despite large score/rank differences. Examples:

- All 14 category-16 papers use the same sentence, although the source summaries distinguish historical primary text, formal reconstructions, proof-search work, and formalization monographs.
- All 13 category-20 papers use the same sentence, although the evidence ranges from empirical authorship detection and citation fabrication to normative authorship analysis.
- All 12 category-4 compression papers use the same sentence despite different mechanisms (prompt compression, retrieval compression, latent memory, tool-document compression, and example selection).
- Category-18 rows with scores 94, 93, 91, 90, 89, 87, 85, and 84 use essentially the same generic explanation.

The files are mechanically rank-valid, but these explanations do not state the concrete feature that differentiates the ranking. They also make it impossible to audit whether score gaps reflect method transfer, novelty threat, provenance, formal executability, or merely topic membership.

**Required fix:** write row-specific 1–3 sentence explanations naming the decisive feature and why it places the paper above/below nearby items.

### 4. Documented false positive `S21P01` is substantially over-ranked and its explanation contradicts source evidence

The source summary explicitly says that Hong et al.’s *Scholastic* is an HCI/ML system name, not medieval scholastic method; it does not represent a `quaestio`, objections, distinctions, `respondeo`, or replies, and its exact relevance is “low.” Nevertheless, the category file gives it score 87/category rank 5, and the global file gives it score 87/global rank 18. The explanation reframes it as “linking scholastic inquiry with interactive AI methodology,” which is not supported by the source’s false-positive finding and inflates the interdisciplinary bridge.

**Required fix:** either score this row as a low-relevance false positive with an explanation preserving the negative finding, or document a clearly bounded secondary value (human-guided structured context) and reduce the score accordingly. It should not outrank direct formal-argument and disputation precedents without an explicit rationale.

### 5. Baseline identifier format conflicts with the stated canonical-ID rule

The protocol says IDs must match `S<category number, 2 digits>P<paper order, 2 digits>`, but the inventory and both outputs contain IDs such as `12-01`, `16_01`, `17_05`, `18_08`, and `20_01`. The outputs correctly preserve the inventory IDs, so this is not an isolated reviewer-file mismatch; it is an unresolved protocol/source-contract inconsistency. It still prevents strict validation of the stated canonical-ID requirement.

**Required fix:** either correct the upstream inventory and regenerate all dependent artifacts, or amend the protocol to explicitly allow the legacy hyphen/underscore IDs and record that compatibility rule.

## Sampled grounding assessment

- **High end:** `S21P05` (Alfano et al., score 98) and `S21P02` (Freedman et al., score 97) are directionally supported: their summaries describe formal argument extraction/semantics and contestable claim verification as close adjacent technical precedents. Their exact scores are subjective, but the bridge rationale is plausible.
- **Mid/high:** `S10P10` (Trajano et al., score 95, low confidence) is supported as a strong direct novelty threat because the source says it already uses scheme-conditioned context/RAG for translation into computational arguments. The low confidence should remain visible because the evidence does not resolve all evaluation-data provenance.
- **Low end:** hallucination surveys and long-context/compression papers are directionally grounded as general evaluation/context methods rather than direct scholastic-protocol implementations. However, their reused explanations do not make the distinctions among survey, theory, and method contributions auditable.
- **Exception:** `S21P01` fails the sample check because the ranking explanation reverses the source’s explicit false-positive conclusion.

## Required disposition

**REVISE before acceptance.** Preserve the mechanically valid row/rank structure, then repair the five issues above and rerun the exact validation checks. The most important substantive corrections are the Rawte evidence contradiction, the Hong false-positive over-ranking, and row-specific evidence/explanations.