# Adversarial review — `walton_schemes`

## Verdict

**FAIL — revise before acceptance.** The two CSVs are structurally valid and internally rank-consistent, but the review is not yet a defensible Walton-scheme/critical-question ranking because relevance evidence is frequently generic or absent, generic argumentation is repeatedly scored with the same boilerplate rationale, and duplicate works receive materially different scores.

## Checks performed

- Compared both review files with `remaining_nonbenchmark.csv` and `ranking_protocol.md`.
- Confirmed 124 data rows in each review file.
- Confirmed exact paper-ID equality, no duplicate IDs, and no missing IDs in either file.
- Confirmed category ranks and global ranks are unique, contiguous, and ordered by descending score with `paper_id` tie-breaking.
- Confirmed scores are integers in the permitted 0–100 range and explanations/evidence fields are non-empty.
- Spot-checked the supplied subtopic summaries for direct, adjacent, and weakly related items, including Subtopics 21, 23, 24, and 25.

## Findings

### 1. Blocker: `evidence_basis` often proves only non-benchmark status, not ranking relevance

The protocol requires evidence that supports the ranking, not merely evidence that a paper is allowed into the nonbenchmark pool. In the global file, 56/124 rows use evidence that is primarily a benchmark-exclusion statement; 33 of those also use the identical generic explanation that no explicit Walton scheme or critical-question mechanism was identified. Examples include:

- `S04P01`–`S04P12`: the evidence says each paper introduces a prompt/context-compression method, but does not support the claimed relative relevance to Walton schemes, critical questions, or defeasible argument context.
- `16_01`–`16_14`: every row cites the same generic “scholarly, formal, conceptual...” benchmark-status text, with no paper-specific reasoning evidence.
- `S01P01`–`S01P08`, `S02P02`–`S02P09`, and several philosophy/evaluation rows have the same problem.

A non-benchmark determination is necessary for scope, but it cannot substantiate a score such as 40–49 for transfer to scheme-aware context. Replace or supplement these entries with source-summary/paper evidence describing the actual transferable mechanism and why it is weaker or stronger than neighboring items.

### 2. Major: generic argumentation is not consistently separated from Walton-scheme/CQ relevance

Seventy category rows reuse the same explanation: “indirect transfer to scheme-conditioned context, but no explicit Walton scheme or critical-question mechanism is identified.” This collapses materially different cases:

- prompt compression and long-context utilization;
- deductive reasoning and syllogistic psychology;
- knowledge-graph scaffolding;
- philosophical LLM surveys;
- formal historical logic;
- corpus/HTR infrastructure.

These are not one relevance class. At minimum, the review needs explicit labels or paper-specific explanations distinguishing: (a) direct Walton scheme/CQ work; (b) computational argumentation/defeasible logic; (c) dialogue/objection/reply analogues; (d) upstream extraction or provenance infrastructure; and (e) generic LLM/context work. Without that separation, scores are not auditable and the lower half of the ranking is largely a template artifact.

### 3. Major: duplicate or near-duplicate works receive inconsistent scores

The input IDs must not be merged, but the ranking protocol does not justify assigning different relevance scores to the same work without an explicit version distinction.

- Lawrence & Reed argument-mining survey: `S18_14` = 80, `S09P04` = 72, `S24P17` = 68.
- Shanahan, “Talking About Large Language Models”: `S06P03` = 57 and `S25P01` = 55.
- Maliszewski, “It Takes a Village...” / published version: `S22P01` = 43, `S24P05` = 40, `S24P06` = 39; the Subtopic 24 summary explicitly says the latter two are the same study and should not be treated as independent corroboration.

Preserve all required rows and IDs, but normalize scores/explanations for duplicates or state a documented version-specific reason for each difference. Otherwise the global ranking double-counts some literature while penalizing/rewarding versions arbitrarily.

### 4. Major: low-confidence evidence is placed near the top without an uncertainty penalty or caveat

`S10P10` (Trajano et al.) is global rank 3 with score 94 and confidence `high` in the review, while the evidence basis says it is “unclear whether evaluation data are newly introduced or reused.” That unresolved fact directly affects novelty-threat and methodological-transfer assessment. The supplied evidence supports direct topical relevance, but not a high-confidence novelty score. Either lower confidence to `low`/`medium`, separate relevance from novelty certainty, or explain why the uncertainty does not affect the score.

Similarly, papers such as `S21P05` and `S21P10` are given high confidence despite source-summary evidence describing adjacent systems rather than Walton/CQ implementations. Confidence should track evidence for the ranking claim, not merely confidence that the paper exists or is nonbenchmark.

### 5. Major: category and global rankings are mechanically consistent but not independently justified

The rank arithmetic passes, but the score pattern reveals coarse batching rather than discriminative review. For example, all twelve Subtopic 4 compression papers receive score 44, all fourteen Subtopic 16 historical-logic items receive score 37, and many unrelated hallucination/philosophy rows receive the same score. Equal scores are permitted, but here the repeated boilerplate explanations and identical evidence-basis style provide no paper-specific reason that these works are tied. The ranking should either document the deliberate tie or assign differentiated scores based on concrete transfer features.

### 6. Moderate: the ranking under-specifies the project’s critical-question target

The direct high-ranked items correctly identify foundational schemes, argument mining, defeasible reasoning, and computational argumentation. However, the explanations rarely state which project capability is transferred: scheme identification, CQ generation, burden shifting, objection typing, reply discharge, authority/provenance handling, or dialectical protocol control. The Subtopic 21 summary explicitly distinguishes generic argument graphs, contestability, debate, and Socratic questioning from the full scholastic sequence. The review should use that distinction rather than treating all “structured reasoning” as equivalent Walton/CQ value.

## Evidence spot-check

- `S10P02`, `S10P04`, `S10P05`, and `S10P10` are plausibly in the top tier because the retained evidence describes argumentation schemes, scientific-discourse mining, scheme annotation, and scheme-conditioned computational arguments respectively.
- `S21P08`, `S21P09`, `S21P05`, and `S23P01` are strong adjacent/direct candidates; the supplied summaries support scheme/CQ literature, AI argument evaluation, formal argumentation/logic, and regulated dialogue. Their explanations are substantially better than the generic lower-half entries.
- `S21P01` is correctly treated as a false-positive/weak relevance item: the summary explicitly says “Scholastic” is an HCI system, not medieval scholastic method, and it lacks quaestio/objection/determination/reply structure.
- `S24P15` is correctly marked as a design proposal without validated benchmark evidence, but its score should be supported by that proposal’s concrete knowledge-graph/explainability mechanism rather than only its benchmark absence.
- `S24P05`/`S24P06` are explicitly identified by the source summary as the same HTR/stylometry study; their inconsistent scores are therefore not defensible without a version-specific rationale.

## Required corrections

1. Rewrite `evidence_basis` for every row so it supports relevance/transfer, not only benchmark exclusion.
2. Replace the 70-row generic explanation block with paper-specific explanations or explicit relevance classes.
3. Reconcile scores for duplicate works while preserving every required input row and ID.
4. Correct confidence for `S10P10` and any other row whose source evidence leaves novelty or mechanism uncertain.
5. Re-run the protocol validator after edits and retain the structural checks above.

## Structural result

**PASS:** row count, ID coverage, rank uniqueness/contiguity, score range, and score-to-rank ordering.

**FAIL:** evidentiary sufficiency, direct-versus-generic relevance discrimination, duplicate consistency, and confidence calibration.
