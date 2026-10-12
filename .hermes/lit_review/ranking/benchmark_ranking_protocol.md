# Benchmark selection and validation protocol

**Protocol version:** 1.0
**Scope:** `benchmark_studies.csv` only; 80 studies classified as introducing a new benchmark, dataset/corpus used as a benchmark, or benchmark artifact.

## Goal

Identify the best existing benchmarks for evaluating the scholastic context-engineering system:

> source text → claim/evidence spans → cross-tradition argument-form classification → deductive/proof/dialectical skeleton → provenance/dependency-preserving context selection/compression → inspectable philosophical/LLM reasoning.

The benchmark must test one or more project capabilities, not merely generic language-model quality.

## Immutable identity

Preserve literal `paper_id`, citation, category number, paper order, benchmark name, benchmark type, evidence, and confidence exactly as supplied. Do not merge duplicate benchmark records; flag shared benchmark families or versions in explanations.

## Reviewer outputs

Each of 25 benchmark perspectives produces:

- `benchmark_review_<slug>_category.csv`
- `benchmark_review_<slug>_global.csv`

Each file contains all 80 benchmark studies and columns:

`paper_id,category_num,category,paper_order,citation,benchmark_status,benchmark_name,benchmark_type,reviewer_slug,viewpoint,category_rank,global_rank,score_0_100,confidence,explanation,evidence_basis`

Category ranks are contiguous within each category. Global ranks are 1–80. Sort scores descending; equal-score ties use `(numeric category_num, numeric paper_order, literal paper_id)`.

Explanations must be 1–3 sentences and name the concrete benchmark property driving the score. Evidence must point to the retained summary/paper evidence, not benchmark status alone.

## Benchmark suitability dimensions

Reviewers must distinguish:

1. **Exact task fit:** tests natural-language philosophical reasoning, argument forms, proof/dialectical structure, or context selection.
2. **Pipeline coverage:** span/claim extraction, argument-form classification, skeleton/proof recovery, dependency-aware selection/compression, provenance, downstream reasoning.
3. **Diagnosticity:** isolates failure modes rather than collapsing into one end score.
4. **Data authenticity:** real scholarly/philosophical text versus synthetic/rule-generated or generic QA.
5. **Cross-tradition coverage:** supports Aristotelian, medieval, Islamic, Jewish, Nyaya, Mohist, or other explicit traditions, or is adaptable without erasing distinctions.
6. **Reasoning depth:** multi-step inference, implicit premises, defeasible/analogical/abductive/dialectical structure, proof validity, or only surface classification.
7. **Context stress:** long context, distractors, position effects, compression, minimal sufficient context, evidence selection.
8. **Grounding/provenance:** cited evidence, source spans, attribution, entailment, support/attack, traceability.
9. **Evaluation quality:** splits, leakage controls, annotations, agreement, metrics, baselines, reproducibility, adversarial controls.
10. **Implementation feasibility:** access, licensing, format, tooling, annotation cost, and ability to run as a solo project.
11. **Novelty coverage:** whether the benchmark threatens or validates the proposed integrated architecture.
12. **Composite suite value:** whether it should be combined with other benchmarks rather than treated as a standalone test.

## Required distinctions

- benchmark-producing study versus existing benchmark evaluation;
- direct project test versus adjacent diagnostic;
- synthetic logical benchmark versus authentic scholarly-text benchmark;
- benchmark resource versus paper method;
- dataset availability versus verified access/license;
- high relevance versus high prestige/recency.

## Final verification gate

After aggregation, select the top candidates, resolve and download the exact scholarly paper and benchmark artifact where available, verify identity and artifact access, then have independent adversarial reviewers judge whether each benchmark genuinely tests the stated project pipeline. Fail closed on mismatches, inaccessible artifacts, duplicate/version confusion, or generic relevance unsupported by task design.
