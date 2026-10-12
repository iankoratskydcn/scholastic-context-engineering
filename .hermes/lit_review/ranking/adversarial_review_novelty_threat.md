# Adversarial Review — Novelty-Threat Ranking

**Reviewed artifacts**

- `review_novelty_threat_category.csv`
- `review_novelty_threat_global.csv`
- `remaining_nonbenchmark.csv`
- `ranking_protocol.md`
- Referenced source summaries under `.hermes/lit_review/summaries/`

## Verdict: REVISE

The files pass the mechanical coverage and rank-integrity checks, but the novelty-threat semantics are not sufficiently adversarial. The review labels every item `direct novelty threat`, including papers whose cited summaries explicitly describe them as conceptual, infrastructural, foundational, background, false-positive, or otherwise adjacent. Scores also frequently represent threat to one component rather than direct duplication of the proposed integrated architecture. The artifacts should be revised before being treated as a reliable direct-vs-adjacent novelty ranking.

## Mechanical validation — PASS

- Both CSVs contain exactly **124 data rows**.
- Each contains exactly the same 124 IDs as `remaining_nonbenchmark.csv`; no missing, extra, or duplicate IDs were found.
- Category ranks are complete and unique within every category, from 1 through the category size.
- Global ranks are unique and complete from 1 through 124.
- Category and global rows agree on all shared fields, including citation, score, confidence, explanation, and evidence basis.
- Scores are integer values in the required 0–100 range.
- Category ranks and global ranks are consistent with descending score; equal-score ordering follows canonical `paper_id` order. No rank/score ordering violation was found.
- All 124 explanation and evidence fields are non-empty; explanations satisfy the 1–3 sentence constraint.
- All referenced summary paths exist.

## Findings requiring revision

### 1. Systematic direct/adjacent misclassification — HIGH

Every one of the 124 rows uses `viewpoint=direct novelty threat`, but the evidence base repeatedly distinguishes direct overlap from adjacent relevance. This is not a harmless label choice because the task specifically requires distinguishing direct overlap from adjacent relevance.

Concrete contradictions include:

- `S21P05` (score 97): its source summary calls Alfano et al. the “closest recent technical comparator” but explicitly says the novelty threat is **adjacent rather than direct** because it models generic debate graphs rather than the scholastic sequence.
- `S23P01` (score 88): Uckelman is the closest protocol-level analogue, but the summary says it lacks `sed contra`, `respondeo`, and reply-to-objection stages; this is adjacent protocol overlap, not direct duplication.
- `S22P03` (score 55): the summary describes Medieval Latin HTR and explicitly says it does not interpret propositions, represent disputational roles, or test inferences. It is upstream infrastructure, not a direct novelty threat to the reasoning architecture.
- `16_01`–`16_14` (all score 8): the summary describes historical/formal background and repeatedly says the works do not provide an LLM context-engineering system. Calling all of them direct threats is inconsistent with the evidence.
- `S21P01` (score 35): the summary identifies “Scholastic” as an HCI/ML false positive unrelated to medieval scholastic method and says exact relevance is low, yet the row is still labeled direct.
- Categories 12, 15, 16, 17, 20, 22, and 25 contain broad groups whose explanations characterize relevance as limited, conceptual, methodological, background, or infrastructural while retaining the direct label.

**Required correction:** add an explicit direct/adjacent/background classification (or encode it in `viewpoint`) and reserve `direct` for a paper that implements or operationalizes the same claimed mechanism/system boundary. Keep component-level threats such as compression, argument mining, or debate graphs as adjacent unless the proposed novelty claim is explicitly limited to that component.

### 2. Scores conflate component threat with integrated-architecture threat — HIGH

The ranking is mechanically ordered correctly, but the score meaning is unstable. The highest scores are assigned to papers that threaten only one layer while their own evidence records major architectural gaps:

- `S04P03` LLMLingua-2 — score **98**: direct token-retention classification overlap, but the summary says it does not identify argument components, logical relations, proof dependencies, or provenance.
- `S21P05` Alfano et al. — score **97**: formal argument graph and support/attack overlap, but no scholastic stages or proof-relevant context construction.
- `S04P01` and `S04P02` — scores **96** and **95**: strong compression/query-selection prior art, but no explicit argument representation or inferential-dependency protection.
- `S23P01` — score **88**: executable formal dialogue analogue, but not the claimed scholastic workflow.

These can reasonably be high **adjacent-component** threats, but the current `direct novelty threat` viewpoint makes the scores read as threats to the complete proposed machine. The report should either (a) separate component-threat and integrated-system-threat scores, or (b) lower/annotate scores when the source only covers an adjacent layer.

### 3. Evidence is category-summary grounded but often not paper-specific enough — MEDIUM

All evidence paths exist and are valid, so the evidence-basis field passes the protocol’s non-empty/path requirement. However, many explanations are copied verbatim across an entire category and do not name the concrete feature of the individual paper that drove its rank. Examples include all nine category-1 rows, all fourteen category-16 rows, all ten category-22 rows, and most category-20 rows.

This weakens confidence in within-category distinctions. For example, category 16 assigns identical score 8 to every paper, which is defensible as a low-threat floor, but the explanation does not identify the paper-specific formal or historical feature that justified its placement. Category 22 similarly uses one infrastructure-level explanation for HTR, linked data, corpus search, debate projects, and formalization work with materially different relationships to the proposed system.

**Required correction:** make each explanation paper-specific, naming the actual method, representation, evaluation target, or infrastructure feature and stating whether the overlap is direct, component-level adjacent, or merely enabling/background.

## Sample-extreme assessment

- **Top of global ranking:** `S04P03` 98, `S21P05` 97, `S04P01` 96, `S04P02` 95, `S21P02` 92. These are sensible candidates for the strongest component-level novelty threats, especially compression/classification and formal argumentation. They should not all be presented as direct duplication of the integrated scholastic pipeline.
- **Middle:** `S23P01` 88, `18_09` 89, `S03P01` 82, and `S21P10` 81 cover formal dialogue, Toulmin argument generation, long-context degradation, and Socratic tutoring respectively. They are meaningful adjacent threats with distinct mechanisms; the shared direct label hides those distinctions.
- **Bottom:** `16_01`–`16_14` all score 8 and are correctly last under the current score policy, but their direct label and high confidence are semantically wrong for background historical/formal sources. `12-01` and `12-02` are similarly benchmark/foundational reasoning precedents rather than direct architecture threats.

## Final disposition

**REVISE.** Mechanical completeness, exact ID coverage, rank uniqueness, score range, tie-breaking, and evidence-path existence pass. The ranking should not be accepted as final until the direct-versus-adjacent distinction is represented explicitly, component-threat scores are separated from integrated-system threat, and repeated category boilerplate is replaced with paper-specific evidence-grounded explanations.
