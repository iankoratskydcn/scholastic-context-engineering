# Adversarial review: `scholastic_protocol` ranking

## Verdict

**FAIL — revise before treating the ranking as evidence of scholastic-protocol fit.** The files satisfy most mechanical output requirements, but the semantic ranking substantially conflates generic argumentation, formal logic, debate, and infrastructure with an explicit `quaestio → objections → sed contra → respondeo → distinctions → replies` protocol.

## Scope and checks

Reviewed:

- `.hermes/lit_review/ranking/review_scholastic_protocol_category.csv`
- `.hermes/lit_review/ranking/review_scholastic_protocol_global.csv`
- `.hermes/lit_review/ranking/remaining_nonbenchmark.csv`
- `.hermes/lit_review/ranking/ranking_protocol.md`
- sampled source summaries for subtopics 18, 21, 22, 23, and 24.

Mechanical validation:

- Both review files contain exactly 124 rows.
- Both contain exactly the 124 IDs in `remaining_nonbenchmark.csv`; no missing, extra, or duplicate IDs were found.
- Scores are integers in the required 0–100 range.
- Category ranks are unique within each category, and global ranks are unique from 1–124.
- Category ranks are score-consistent.
- Category/global non-ranking fields match exactly.
- One global ranking tie-break violation exists: the protocol requires equal scores to break by canonical `paper_id` order, but the 74-point block ranks `S09P04`, `S09P05` before `12-01`, `12-02`; canonical ID order places `12-01`, `12-02` first. Evidence: `review_scholastic_protocol_global.csv:57-61`.

## Findings

### 1. Critical false positive is ranked far too highly: `S21P01` / *Scholastic*

`S21P01` receives score **93**, category rank **8/10**, and global rank **22/124** (`review_scholastic_protocol_category.csv:96`; `review_scholastic_protocol_global.csv:96`). The sampled source summary explicitly identifies this as a likely false positive: *Scholastic* is an HCI text-analysis interface and “does not represent a `quaestio`, objections, distinctions, a `respondeo`, or replies” (`summaries/21_scholastic_method_ai_direct_summaries.md:7-9`).

This is not merely an adjacent-but-weaker item; it lacks the target protocol entirely. The ranking explanation (“Direct medieval scholastic textual or procedural alignment”) contradicts the source evidence. It should be sharply down-ranked or explicitly marked as a false-positive exclusion candidate.

### 2. Perfect scores collapse generic argumentation into the scholastic protocol

Fourteen papers receive score **100**, including six generic Toulmin/defeasible-logic items (`18_04`, `18_05`, `18_08`, `18_09`, `18_13`, `18_14`), seven adjacent argumentation/debate items from subtopic 21, and three subtopic-23 debate surveys/systems (`review_scholastic_protocol_global.csv:2-15`, especially rows 2–15 after sorting by rank).

The source evidence for subtopic 18 repeatedly describes formal defeasible reasoning, argument schemes, and legal/informal logic, while explicitly noting missing natural-language extraction, scholastic roles, or modern dialogue protocol. For example, the DeLP summary calls it a symbolic dialectical warrant procedure but says it does not extract Toulmin roles or natural-language argumentative structure (`summaries/18_toulmin_defeasible_summaries.md:9-11`). The ranking therefore treats “formal argument structure” as equivalent to the named medieval sequence, contrary to the requested adversarial criterion.

`S23P01` is described as the closest protocol-level analogue, but it also lacks named `sed contra`, `respondeo`, and reply-to-objection stages (`summaries/23_disputatio_dialectical_ai_summaries.md:2-4`). Giving it the same 100 as generic defeasible-logic and debate items removes the distinction the ranking is supposed to expose.

### 3. The ranking does not separate direct protocol coverage from adjacent support layers

The top 20 global positions are dominated by subtopics 18, 21, and 23: ten subtopic-18 items, seven subtopic-21 items, and three subtopic-23 items. Meanwhile, direct historical/formalization resources are lower: `S22P14` (Dutilh Novaes) scores 91/global rank 25, and `S24P01`/`S24P02` score 92/global ranks 23–24 (`review_scholastic_protocol_global.csv:23-25`).

The source summaries characterize Dutilh Novaes as the strongest retained precedent for formalized historical reasoning (`summaries/22_scholastic_digital_humanities_ai_summaries.md:55-57`) and Hodges as the strongest direct precedent for executable medieval reasoning reconstruction (`summaries/24_islamic_comparative_scholastic_ai_summaries.md:3-7`). Those items need not automatically outrank every adjacent argumentation paper, but the current scores provide no explicit dimensions for: (a) medieval/historical fidelity, (b) explicit stage coverage, (c) typed objection/reply structure, and (d) executable or evaluable protocol. Without those dimensions, generic argumentation vocabulary dominates the ranking.

### 4. Explanations are boilerplate and often fail the protocol’s “concrete feature” requirement

The protocol requires explanations to name the concrete feature driving each rank (`ranking_protocol.md:25`). Instead, the same viewpoint is repeated for all 124 rows, and only 11 explanation templates are used. Many explanations end with the same generic claim that the paper is useful for “modeling or testing ordered objections, determinate resolution, distinctions, and replies,” even where the evidence says the paper is a survey, corpus, parser, HTR pipeline, or generic formal logic system.

Examples include all 14 subtopic-16 historical-logic rows, whose `evidence_basis` is only “source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact” (`review_scholastic_protocol_category.csv:49-62`). That establishes non-benchmark status, not scholastic-protocol fit. Similarly, subtopic-22 corpus and infrastructure rows receive “Direct medieval scholastic textual or procedural alignment” even though the source summary says linked data and corpus infrastructure do not encode premises, objections, replies, or validity (`summaries/22_scholastic_digital_humanities_ai_summaries.md:27-29`, `35-37`).

### 5. Confidence is overstated where the source explicitly limits the claim

Several rows have **high** confidence despite source summaries identifying only indirect relevance or major scope limitations. `S21P01` is high confidence despite the explicit false-positive diagnosis. `S22P09` (*Corpus Thomisticum*) is high confidence despite being search/retrieval infrastructure that does not perform argument-aware retrieval or reasoning (`summaries/22_scholastic_digital_humanities_ai_summaries.md:35-37`; `review_scholastic_protocol_category.csv:98`). `S24P15` is high confidence despite its source being a conceptual framework with no benchmark, corpus, ablation, expert agreement, or historical evaluation (`summaries/24_islamic_comparative_scholastic_ai_summaries.md:45-46`).

High confidence should be reserved for the narrower claim actually supported by the evidence—for example, “is useful upstream corpus infrastructure”—not for the stronger claim that the paper fits the explicit scholastic protocol.

### 6. Global tie-breaking is mechanically non-compliant

The global file violates the explicit tie rule for equal scores. At score 74, the file orders `S09P04` and `S09P05` at global ranks 56–57, then `12-01` and `12-02` at ranks 58–59 (`review_scholastic_protocol_global.csv:57-61`). Under `ranking_protocol.md:25`, equal scores must be ordered by canonical `paper_id`; therefore `12-01`, `12-02` must precede the `S09...` IDs. This is a small mechanical defect, but it means the global output is not fully protocol-valid even apart from the semantic concerns.

## Recommended remediation

1. Re-score with explicit dimensions rather than one undifferentiated relevance score:
   - named scholastic-stage coverage;
   - objection/reply typing and linkage;
   - determination/respondeo representation;
   - historical or medieval source fidelity;
   - executable/evaluable protocol;
   - adjacent enabling value.
2. Apply a hard penalty or exclusion label to false positives such as `S21P01`.
3. Separate direct protocol precedents, formal historical reconstructions, generic argumentation substrates, corpus/infrastructure resources, and merely thematic philosophy.
4. Rewrite explanations so each identifies the actual structural feature present and the missing scholastic stages; do not infer protocol fit from benchmark status or broad argument relevance.
5. Lower confidence where the source summary itself says “adjacent,” “conceptual,” “infrastructure,” “not a full `quaestio`,” or “does not model objections/replies.”
6. Re-sort all equal-score global ties by canonical `paper_id` and rerun the mechanical validator.

## Files changed

Created only:

- `.hermes/lit_review/ranking/adversarial_review_scholastic_protocol.md`

No CSV, source summary, external system, or Git history was modified.
