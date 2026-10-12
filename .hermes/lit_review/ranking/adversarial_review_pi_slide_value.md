# Adversarial review: PI-slide-value ranking

**Reviewed artifacts**

- `review_pi_slide_value_category.csv`
- `review_pi_slide_value_global.csv`
- `remaining_nonbenchmark.csv`
- `ranking_protocol.md`
- sampled source artifacts under `.hermes/lit_review/agents/` and `.hermes/lit_review/summaries/`

## Verdict

**FAIL — the global file is structurally usable but the category file is invalid, and the ranking rationale is not sufficiently evidence-grounded for PI slides.** Do not use the category ranking in slides until ranks are recomputed within each category. The global ordering is mechanically coherent by descending score with source-order tie-breaking, but several high scores contradict the sampled source evidence or rely on generic relevance/prestige language.

## What passed

A programmatic validation found:

- Both review files contain exactly 124 rows.
- Both contain exactly the 124 `paper_id` values in `remaining_nonbenchmark.csv`; no missing, extra, or duplicate IDs.
- Required columns are present; category/global rank blanks are in the correct opposite files.
- Scores are integer values in the required 0–100 range.
- Global ranks are unique integers 1–124 and are sorted by descending score; equal-score ties follow the source-artifact order.
- Category-file and global-file metadata agree with `remaining_nonbenchmark.csv` for category, paper order, citation, and category number.
- Explanations and evidence fields are non-empty and are one sentence each, within the protocol's 1–3 sentence limit.

These checks establish coverage/schema hygiene, not substantive validity.

## Findings

### F1 — Critical: `category_rank` is not ranked within category

`ranking_protocol.md:18–25` requires `category_rank` to rank papers **within their category**. Instead, `review_pi_slide_value_category.csv` assigns the same global sequence 1–124 used by the category-grouped rows. For example:

- Category 1 has ranks 1–9 (`.../review_pi_slide_value_category.csv:2–10`).
- Category 2 starts at rank 10 rather than 1 (`.../review_pi_slide_value_category.csv:11–15`).
- Category 21 has ranks 88–95 (`.../review_pi_slide_value_category.csv:89–96`).
- Category 24 has ranks 109–121 (`.../review_pi_slide_value_category.csv:110–122`).

Thus every category after the first has invalid local ranks, even though ranks are globally unique. Recompute category ranks from 1 to the number of rows in each category, preserving score order and canonical source-order tie breaks.

### F2 — High: the strongest sampled source contradiction is ranked at the very top

`S21P01` (Hong et al., *Scholastic*) is assigned global rank 1 and score 100 (`review_pi_slide_value_global.csv:2`). Its explanation calls it the project's “closest human-in-the-loop precedent.” The source review explicitly says the paper is a **low / false positive**, uses “scholastic” as a project name, and has no objections, replies, quaestiones, distinctions, disputation protocol, or formal argument evaluation (`agents/21_scholastic_method_ai_direct.md:14–20`). The retained-paper evidence also labels it a “False-positive HCI system” (`remaining_nonbenchmark.csv:89`).

This is not merely a calibration disagreement: the ranking rationale reverses the source's central relevance judgment. It should be demoted substantially or explicitly labeled as a naming/false-positive contrast citation, not a top PI-slide precedent.

### F3 — High: score saturation collapses distinct evidence levels

Six papers receive score 100 (`review_pi_slide_value_global.csv:2–7`), despite materially different source classifications:

- `S21P01`: source says low/false positive (`agents/21_scholastic_method_ai_direct.md:14–20`).
- `S21P02`: high adjacent threat (`agents/21_scholastic_method_ai_direct.md:22–28`).
- `S21P05`: very high adjacent threat (`agents/21_scholastic_method_ai_direct.md:46–52`).
- `S21P06`: medium-high adjacent threat (`agents/21_scholastic_method_ai_direct.md:54–60`).
- `S21P10`: medium adjacent threat (`agents/21_scholastic_method_ai_direct.md:86–92`).
- `S23P01`: exact conceptual/protocol overlap (`agents/23_disputatio_dialectical_ai.md:24–30`).

The ranking provides no visible rubric that explains why a false positive, medium adjacent threat, high threat, and exact protocol overlap all deserve the same maximum score. This weakens the claimed 0–100 precision and makes “global citation value” difficult to defend.

### F4 — High: evidence basis is frequently a pointer to the ranking corpus, not paper evidence

In 87 of 124 rows, `evidence_basis` only says that the claim comes from the `remaining_nonbenchmark.csv` evidence field plus the retained citation/category (`review_pi_slide_value_global.csv`; same pattern in the category file). Only 37 rows point to an agent summary containing source-level findings.

The generic pointer can support a basic inclusion/status statement, but it does not substantiate stronger claims such as “direct methodological precedent,” “strong novelty comparison,” “useful for persistent scholarly interaction,” or “directly informing structured scholastic knowledge representation.” The protocol requires evidence pointing to source summary or paper evidence, not reviewer intuition. Evidence bases should name the specific summary section, source-artifact statement, or paper finding used for the score.

### F5 — High: explanations do not consistently cover the stated PI-slide decision dimensions

The viewpoint is “principal-investigator motivation, prior-work, gap-slide, and overall citation value,” but most explanations name only one generic relevance feature. A keyword audit found approximately:

- motivation/problem language: 18/124;
- prior-work/precedent language: 40/124;
- gap/novelty language: 11/124;
- citation/canonical/standard language: 12/124.

Many high-scoring rows provide no motivation, gap, or citation-use rationale at all. Examples include `S21P08` (99), `18_02` (98), `18_05` (97), `S24P02` (97), and `S24P04` (96), whose one-sentence explanations describe a method but do not say whether the item belongs on a motivation, prior-work, gap, or citation slide (`review_pi_slide_value_global.csv:9–11,13,18,21`).

A defensible PI-slide score should either separate the four use cases or explicitly state which use case drives the score and why the paper is preferable to nearby alternatives.

### F6 — Medium-high: prestige/recency/citation-value language leaks into a protocol that forbids it

`ranking_protocol.md:28–29` says to rank project relevance, novelty threat, methodological transfer, and usefulness—not prestige, citation count, recency, or writing quality. The explanations nevertheless use citation/prestige proxies, including:

- `S24P16` (score 94): “Useful overview citation ... and benchmark context” (`review_pi_slide_value_global.csv:28`).
- `S24P17` (score 92): “broad argument-mining synthesis” with no concrete transfer or gap claim (`review_pi_slide_value_global.csv:35`).
- `S24P08` (score 92): corpus infrastructure is elevated as a high-value PI citation without specifying a project-relevant method or gap (`review_pi_slide_value_global.csv:34`).
- The ranking corpus contains repeated “foundational,” “canonical,” “recent,” “standard,” and “overview citation” reasoning; these are not valid substitutes for evidence of project relevance.

Foundational status can be relevant when tied to a concrete construct the project needs, but the rationale must name that construct and avoid treating canonicality or recency as value by itself.

### F7 — Medium: low-confidence and uncertain source items are not handled conservatively

The files assign `low` confidence to only two rows, including `S10P10` and `S02P08`, but still give them high scores 92 and 81 (`review_pi_slide_value_global.csv:33` and category/global corresponding rows). `remaining_nonbenchmark.csv` marks both as `uncertain` benchmark-status evidence, with low confidence (`remaining_nonbenchmark.csv:14,38`). This does not automatically exclude them from PI slides, but the ranking should distinguish “potentially important pending verification” from “safe citation for a slide.” The current score/confidence combination can overstate citation readiness.

## Sample source-evidence adjudication

| Paper | Ranking claim | Source evidence | Adversarial judgment |
|---|---|---|---|
| `S21P01` | “closest human-in-the-loop precedent,” score 100 | HCI clustering/coding interface; explicitly not scholastic disputation; low/false positive | Unsupported and contradicted; major demotion required. |
| `S21P05` | Integrated argument-mining, description-logic, debate-reasoning novelty threat, score 100 | Source reports fuzzy argumentative KB, support/attack, quantitative semantics, and description-logic query answering; no scholastic stages | Supported as a high adjacent threat, but “direct” should be qualified as adjacent rather than direct duplicate. |
| `S23P01` | Medieval disputation as formal dialogue, score 100 | Source reports alternating Opponent/Respondent moves, rule-governed responses, consistency goal, and implementation in formal dialogue semantics | Strongly supported and plausibly top-tier, but should be distinguished from generic LLM debate. |
| `S21P10` | Socratic/fallacy-aware intervention, score 100 | Source classifies it as a medium adjacent threat; no explicit quaestio/objection/respondeo data structure | Relevant motivation/application citation, but maximum score is not supported. |
| `S24P08` | Corpus infrastructure precedent, score 92 | OpenITI is a machine-actionable corpus resource, not an argument-reasoning system or benchmark | Useful infrastructure citation, but score should reflect enabling-resource value rather than direct method threat. |
| `S24P15` | Strong novelty-threat and motivation citation, score 96 | Source describes a conceptual Islamic-humanities KG/LLM proposal and explicitly cautions that it lacks a validated benchmark | Should be labeled proposal-level adjacent evidence; “strong novelty threat” is overstated without validated system evidence. |
| `S01P01` | Foundational factuality/faithfulness distinction, score 63 | Source summary supports factuality vs. faithfulness and source-grounded error distinctions | Explanation is supported, but the slide use case should be explicit: motivation/definition, not method or direct scholastic precedent. |

## Recommended repair gate

1. Recompute `category_rank` independently within each `category_num`; validate each category has ranks `1..N`.
2. Replace generic evidence pointers with source-specific evidence locations for every row, especially all rows above score 90.
3. Re-score using explicit dimensions or tags: motivation, prior-work, novelty/gap, methodological transfer, and citation-readiness. Keep “citation value” separate from canonicality/recency.
4. Re-review all score-95+ rows against source classifications; in particular correct `S21P01`, calibrate `S21P06`/`S21P10`, and qualify `S24P15`/`S24P08`.
5. Preserve the global file only after confirming the revised scores and tie breaks; regenerate it if any score changes.

**No production code or external systems were changed. This report is the only created artifact.**
