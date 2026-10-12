# Adversarial review: implementation-feasibility ranking

**Artifacts reviewed**

- `remaining_nonbenchmark.csv` (124 source rows)
- `review_implementation_feasibility_category.csv` (124 rows)
- `review_implementation_feasibility_global.csv` (124 rows)
- `ranking_protocol.md`
- Sampled source summaries in `.hermes/lit_review/summaries/`, including subtopics 04, 08, and 21.

## Verdict

**CONDITIONAL FAIL — structural completeness passes, but the ranking is not yet sufficiently evidenced as an implementation-feasibility review.** The files contain the required row counts and columns, but the evidence field is largely inherited from benchmark-exclusion screening rather than implementation-feasibility evidence. The global tie-break rule is also not met, and 49 source paper IDs violate the protocol's canonical ID format upstream.

## What passed

- Both review files have exactly 124 rows and exactly the same paper-ID set as `remaining_nonbenchmark.csv`.
- There are no duplicate IDs, missing IDs, extra IDs, empty explanations, or empty `evidence_basis` values.
- Required columns are present; metadata fields (`category_num`, `category`, `paper_order`, and `citation`) match the source file in both outputs.
- Scores are integer values in the required 0–100 range.
- Category ranks are unique and contiguous within every category; global ranks are unique and contiguous from 1 through 124.
- `category_rank`/`global_rank` blanking is correct in the respective files.
- Explanations are consistently two sentences and generally name a feasibility-relevant feature such as an executable algorithm, corpus, parser, formal semantics, or evaluation protocol.
- The sampled source summaries support that several high-ranked items really do expose implementable components. For example, the subtopic-08 summary describes Lean Copilot as a Lean-native framework with proof-step suggestion, proof-goal completion, relevant-premise selection, and local/cloud model support; the subtopic-04 summary describes concrete compression algorithms and baselines.
- I found no explicit prestige, citation-count, recency, or writing-quality language in the explanations.

## Findings

### 1. Blocker: `evidence_basis` does not evidence implementation feasibility (124/124 rows)

Every review row copies the exact `evidence` string from `remaining_nonbenchmark.csv`. That source field was created for benchmark exclusion, not for feasibility ranking. Its dominant value appears on 40 rows:

> `source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact`

That statement establishes only that a paper is not a benchmark-producing study. It does **not** establish whether the paper has runnable code, an algorithm specification, accessible data, a reproducible evaluation recipe, manageable dependencies, licensing/access constraints, hardware requirements, or solo-project implementation effort. The same problem appears in the top-ranked row: `S08P06` receives score 96, while its evidence basis is only `System paper; inspected source establishes no new benchmark.` The sampled subtopic-08 summary contains the actual feasibility evidence, but the ranking row does not point to it.

**Required repair:** replace or augment `evidence_basis` with paper-specific feasibility evidence: artifact type, implementation availability or pseudocode, data/access burden, external-system dependencies, evaluation reproducibility, and expected solo-project effort. Benchmark absence may remain as secondary context but cannot be the primary support.

### 2. Major: global equal-score ties do not follow the protocol's tie-break rule

`ranking_protocol.md` requires equal scores to be broken by canonical `paper_id` order. The global file has **21 adjacent equal-score pairs** whose order is not ascending by literal `paper_id`, including:

- `S04P04` before `18_04` at score 86
- `S04P12` before `18_03` at score 84
- `S10P10` before `18_02` at score 82
- `S02P03` before `13-02` at score 78
- `S01P02` before `16_06` at score 60

This is partly entangled with the source-ID defect below, but the delivered global ranking still does not demonstrate the specified tie-break. Category rankings happen to be score-monotone and have no equal-score ties.

**Required repair:** first resolve the canonical-ID issue in the source artifact or define a deterministic normalized ordering approved by the protocol owner; then regenerate global ranks using that exact order for every score tie.

### 3. Major upstream defect: 49/124 source IDs violate the canonical format

The protocol requires `S<category number, 2 digits>P<paper order, 2 digits>`. The source and both review files contain 49 IDs in noncanonical forms, including `12-01`, `13-02`, `15-07`, `16_07`, `18_04`, and `20_10`. The review correctly preserves source identifiers rather than inventing replacements, so this is not a reviewer mutation; nevertheless, the output cannot fully satisfy the protocol's canonical-ID requirement until the source artifact is repaired or the protocol explicitly permits these legacy IDs.

**Required repair:** repair the source ID artifact with versioned mapping evidence, or amend the protocol to define the accepted legacy forms and their tie-break ordering. Do not silently normalize IDs only in the review files.

### 4. Major: feasibility dimensions are asserted but not scored or evidenced separately

The viewpoint says `implementation feasibility for a solo research/web engineering project`, but the outputs provide only one scalar score and a short explanation. They do not distinguish the main drivers that can reverse feasibility: availability of code, data acquisition/cleaning, model/API cost, formal-system setup, dependency burden, evaluation reproducibility, and licensing. For example, the sampled summaries describe meaningful differences among LLMLingua-2, Lean Copilot, LeanDojo, and Scholastic, but the row evidence does not capture those differences. This makes scores difficult to audit and encourages conflating “has a concrete method” with “is feasible for this project.”

**Required repair:** either add explicit subcriteria columns, or require each explanation/evidence basis to cover at least the decisive artifact, dependency/data burden, and reproducibility/effort tradeoff. Keep the published schema compatible if needed by encoding those items in a structured evidence string.

### 5. Moderate: explanation templates are too coarse for adversarial audit

There are only 20 unique explanations across 124 rows. The most common template is reused 14 times, and other templates are reused 10–13 times. Template reuse is not inherently invalid, but many rows receive the same rationale despite materially different source constraints. The explanations usually identify a broad feature (“explicit compression algorithm,” “formalized domain artifact,” or “taxonomy/metric guidance”) but omit why that feature is easy or difficult for a solo implementation and omit countervailing costs. This weakens rank discrimination and makes the scores look more mechanically assigned than source-audited.

**Required repair:** retain concise explanations but make them paper-specific where feasibility differs; mention the concrete implementation surface and the main cost/risk that affects the score.

## Relevance/prestige check

I found no direct evidence that the scores were assigned for prestige, citation count, recency, or writing quality. The language is predominantly about algorithms, formal semantics, corpora, annotation infrastructure, baselines, and executable workflows. However, the evidence field is too benchmark-centered to independently prove that the score reflects implementation feasibility rather than general relevance or methodological interest. This is a grounding failure, not a confirmed prestige bias.

## Sampled source-evidence assessment

- **Lean Copilot / subtopic 08:** source summary supports high feasibility through native Lean integration, proof-goal completion, relevant-premise selection, and local/cloud model support. The ranking row's `System paper; ... no new benchmark` evidence does not preserve any of those facts.
- **LLMLingua-2 / subtopic 04:** source summary supports a concrete token-classification compressor, strong baselines, and an implementable comparison surface. The row evidence mentions the training dataset and lack of a benchmark, but not the implementation/evaluation details that justify the high score.
- **Scholastic / subtopic 21:** source summary identifies a concrete human–AI interface with clustering, codes, metadata, and visualization, while also warning that it is a false positive for medieval scholastic method. The ranking rationale captures a structured system but does not state the domain mismatch or adaptation cost.

## Acceptance decision

Do not treat the current ranking as fully verified. It is structurally usable as a draft and appears broadly oriented toward implementation features, but it needs evidence-basis repair and deterministic tie-break correction before downstream selection decisions. The upstream ID-format defect must be resolved or explicitly waived by the ranking protocol owner.
