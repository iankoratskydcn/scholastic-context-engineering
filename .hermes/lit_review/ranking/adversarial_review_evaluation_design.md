# Adversarial review: evaluation-design ranking

## Verdict

**FAIL / revise before use.** The files are structurally complete, but the ranking is not evidentially auditable as a ranking of useful benchmark, metric, or ablation design. It mostly supplies scores plus a repeated generic disclaimer that the papers have no reusable benchmark/metric, while still assigning many of those papers very high scores.

## Scope and checks

Reviewed:

- `review_evaluation_design_category.csv`
- `review_evaluation_design_global.csv`
- `remaining_nonbenchmark.csv`
- `ranking_protocol.md`
- sampled source summaries in `summaries/02_logic_hallucination_summaries.md`, `03_context_degradation_summaries.md`, `04_context_compression_summaries.md`, and `20_ai_academic_writing_summaries.md`

Structural checks passed:

- 124 rows in each review file, matching the 124 rows in `remaining_nonbenchmark.csv`.
- No missing or duplicate paper IDs.
- Scores are integer-valued and within 0–100.
- Global ranks are unique and complete; category ranks are complete within each category.
- Global scores are monotonically non-increasing by rank.

These checks do not rescue the substantive ranking defects below.

## Findings

### 1. Critical: explanations are non-discriminative and violate the protocol

**Evidence:** 119/124 rows in both review files use the exact same explanation:

> Offers domain-relevant concepts that may inform benchmark construction, but transfer is indirect because no reusable task or metric is evidenced.

This does not name the concrete feature that drove each ranking, as required by `ranking_protocol.md`. It also cannot explain why one paper received 98, another 86, another 82, or another 44. The five customized global explanations are S03P01, S02P08, S02P03, S02P02, and S02P09; all other rows are effectively unaudited.

**Impact:** The output cannot distinguish benchmark design, metric design, ablation/control design, evaluation protocol, or merely topical relevance. Category and global rankings are therefore not independently reviewable.

### 2. Critical: high scores are assigned despite evidence explicitly denying reusable evaluation artifacts

The ranking's highest tier is dominated by papers whose evidence says no benchmark release is attributed:

- S03P02 and S03P07: global ranks 2–3, score 98, but evidence only describes long-range analysis or positional-bias calibration; their explanations are generic.
- S04P01–S04P12: global ranks 20–30, score 82, while the evidence repeatedly says no named benchmark release is attributed. The summaries show useful compression methods, but the ranking does not identify which paper contributes a metric, controlled condition, protected-span rule, or ablation that transfers to the project.
- 20_01, 20_03, 20_06, 20_10, and 20_11: global ranks 7–11, score 86, despite `remaining_nonbenchmark.csv` providing only the generic description “scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact.”
- 20_02 and 20_04–20_09: global ranks 14–19, score 84 with the same generic evidence limitation.

A paper can reasonably score well without releasing a benchmark, but then the explanation must identify a transferable evaluation construct or design (for example, blinded agreement, criterion decomposition, repeated-run stability, perturbation control, or reference-integrity checking). The present rows do not do that.

### 3. High: the ranking conflates dataset/corpus presence with evaluation-design value

S04P03 (LLMLingua-2) is global rank 13 with score 85. Its evidence specifically mentions a “compression dataset for training,” not a benchmark, metric, or formal evaluation suite. The source summary describes token-retention classification and task-agnostic compression, which could support an ablation or baseline, but the row's generic explanation does not say that. This is exactly the failure mode the review was meant to catch: a dataset or training artifact is not automatically useful benchmark design.

The same ambiguity affects the category-20 corpus studies. Their summaries contain potentially useful controls—matched prompts, blinded human judgments, repeated evaluator runs, criterion-level scoring, and reference verification—but the ranking treats them all as nearly interchangeable 84–86-point items and does not state which design element is transferable.

### 4. High: genuine evaluation-design exemplars are present but not consistently recognized

The strongest evidence-backed rows are the five customized entries:

- S03P01, rank 1/score 98: controlled positional placement, multi-document QA, and key-value retrieval.
- S02P08, rank 4/score 94: adversarial noise and counterfactual perturbation families.
- S02P03, rank 5/score 90: negation-sensitive task conditions and error-stratified evaluation.
- S02P02, rank 6/score 89: false-premise handling and premise validation.
- S02P09, rank 12/score 86: consistency constraints between response labels and self-judgments.

These are materially different design contributions, and the source summaries support them. However, the immediately adjacent papers in the ranking often have only generic explanations, so the ranking does not establish whether they deserve comparable scores. For example, the long-context summary also identifies RULER, NoLiMa, LongBench, and LongPiBench as explicit evaluation designs, yet the reviewed rows for S03P02 and S03P07 do not expose a comparable benchmark/metric/ablation rationale.

### 5. Medium: canonical tie-breaking is violated in the global file

`ranking_protocol.md` requires equal-score ties to be broken by canonical `paper_id` order, with category order numeric ascending and paper order from the source artifact. Three equal-score groups violate that order:

- Score 86: S02P09 (category 2) is rank 12 after category-20 papers at ranks 7–11; category 2 should precede category 20.
- Score 65: `12-02` is placed after S23P01 despite category 12 preceding category 23.
- Score 74: S25P02 is placed before category-20 rows 20_12 and 20_13 despite category 20 preceding category 25.

This is independently verifiable from the global CSV and is a mechanical protocol defect.

### 6. Medium: confidence is not reflected in the ranking rationale

S02P08 is rank 4 with score 94 but confidence `low`; S03P01 is rank 1 with confidence `medium`. Low confidence is allowed by the protocol, but the explanations do not expose uncertainty or explain why a low-confidence score outranks high-confidence alternatives. Given that most rows are marked high confidence while carrying only generic evidence, confidence appears decorative rather than calibrated to evidence quality.

## Recommended repair

1. Replace every generic explanation with a paper-specific 1–3 sentence rationale naming the concrete transferable feature: benchmark task family, perturbation/control, metric, annotation scheme, evaluator agreement/stability procedure, ablation, or protected-span criterion.
2. Add an explicit design-type field or encode it consistently in `explanation`/`evidence_basis`: `benchmark`, `metric`, `ablation/control`, `human-evaluation protocol`, `dataset/training artifact only`, or `conceptual guidance`.
3. Cap or separately label papers whose evidence supports only a dataset/corpus or topical relevance; do not let them occupy the same score band as controlled evaluation protocols without justification.
4. Re-rank using the protocol's canonical tie-break order and verify equal-score groups programmatically.
5. Re-run the 124-row validation after revision, including a uniqueness test for explanations or at minimum a check that each explanation contains a paper-specific design feature.

## Bottom line

The ranking has a plausible top signal around controlled robustness and long-context evaluation, but 119 repeated explanations and unsupported high scores make the full ordering unreliable. It should not be used to select benchmark, metric, or ablation prior art until the rows are rewritten and the tie-break defects are corrected.
