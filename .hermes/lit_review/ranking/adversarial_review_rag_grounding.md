# Adversarial review — RAG-grounding ranking

## Verdict

**CONDITIONAL FAIL — structurally valid, but the ranking contains several grounding-specific reasoning errors and evidence-quality weaknesses that should be corrected before treating it as an authoritative RAG ranking.**

## Verification performed

- Compared both reviewer files against `remaining_nonbenchmark.csv` and `ranking_protocol.md`.
- Confirmed both outputs contain exactly 124 data rows, the exact 124 expected paper IDs, no duplicate IDs, integer scores in `0–100`, and non-empty explanations/evidence.
- Confirmed `review_rag_grounding_category.csv` has contiguous unique `category_rank` values within every category.
- Confirmed `review_rag_grounding_global.csv` has contiguous unique `global_rank` values `1–124`.
- Confirmed category/global files agree on all shared metadata, scores, explanations, and evidence fields; only the rank-specific columns differ as required.
- Confirmed global ordering follows descending score with ties resolved by canonical `(category_num, paper_order)` order.
- Confirmed explanations are within the protocol's 1–3 sentence limit.

No structural/schema defect was found in the two ranking CSVs. The problems below are substantive ranking/evidence defects.

## Findings

### 1. `S23P02` is assigned an unsupported retrieval/context-selection rationale — major

`review_rag_grounding_category.csv:107` and `review_rag_grounding_global.csv:79` describe Maudet, Parsons & Rahwan's survey as a “concrete context-selection or long-context failure mechanism.” The corresponding source summary characterizes it as a survey of argumentation in multi-agent systems, not a retrieval, context-window, or long-context study (`summaries/23_disputatio_dialectical_ai_summaries.md:1–5`). The explanation does not name a concrete feature supported by the evidence and should be rewritten as indirect transferable argument-structure background or ranked lower.

### 2. `S25P02` is misclassified as a concrete retrieval/evidence-selection contribution — major

`review_rag_grounding_category.csv:123` and `review_rag_grounding_global.csv:82` give Schaeffer, Miranda & Koyejo 35 points while saying it offers a “concrete retrieval, evidence-selection, corpus, or knowledge-grounding mechanism.” The evidence basis says it is scaling/metric analysis of existing reported tasks and introduces no benchmark artifact. That is not a retrieval or grounding mechanism. The paper may be a methodological caution about apparent capability thresholds, but the explanation and viewpoint application are not source-supported.

### 3. `15-10` is overclaimed as a retrieval/evidence-selection paper — major

`review_rag_grounding_category.csv:45` and `review_rag_grounding_global.csv:90` classify *Leveraging LLMs to Assist Philosophical Counseling* as a concrete retrieval/evidence-selection contribution. The source evidence identifies it as an application/critical-analysis paper with no benchmark (`remaining_nonbenchmark.csv:47`; `summaries/15_llm_philosophy_summaries.md`, the corresponding counseling entry). This should be an indirect, low-priority transfer item unless the source explicitly demonstrates a retrieval-grounding mechanism.

### 4. `S24P01` receives a concrete retrieval-grounding rationale despite being historical formalization — major

`review_rag_grounding_category.csv:112` and `review_rag_grounding_global.csv:67` assign 45 points and the concrete retrieval/evidence-selection rationale to Hodges's historical formalization of Avicenna proof search. The source evidence explicitly says “Historical formalization ...; no benchmark” (`remaining_nonbenchmark.csv:110`; `summaries/24_islamic_comparative_scholastic_ai_summaries.md:55–57` for the formalization distinction). The paper may transfer to proof representation, but it is not direct RAG grounding prior art and should not use the retrieval-mechanism explanation.

### 5. `S10P10` is materially under-ranked and under-confident relative to the available evidence — major

Trajano et al. is ranked only 35 globally with score 61 and **low** confidence (`review_rag_grounding_global.csv:36`). Its explanation calls it merely transferable argument-scheme structure with limited direct RAG evidence. The retained source summary identifies it as the **strongest direct novelty threat**: scheme-conditioned context supplied to an LLM, retrieval-augmented translation, and explicit discussion of wrong-scheme retrieval (`summaries/10_walton_schemes_nlp_summaries.md:23–27`). This is directly relevant to the stated RAG-grounding viewpoint and should be near the top of the non-compression direct-grounding items, with confidence at least medium/high if the summary is accepted as evidence.

### 6. The category-20 cluster is inflated and insufficiently differentiated — major

`20_10` and `20_11` receive 74 and 72, while ten other academic/philosophical-writing papers receive identical 57 scores (`review_rag_grounding_global.csv:19–21, 34, 38, 43–51`). Their evidence bases are the same generic sentence — “source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact” — rather than paper-specific grounding evidence. Fabricated-reference studies can have indirect relevance to citation reliability, but essay-style comparison, authorship, stylistic convergence, and philosophical ethics papers do not all provide a concrete retrieval/grounding mechanism. The cluster needs explicit separation of direct citation/fabrication evidence from weakly related generation-quality work.

### 7. Generic evidence strings weaken auditability for multiple low-ranked categories — moderate

For categories 16, 17, and 18, nearly every `evidence_basis` repeats the same generic template instead of identifying the paper's actual contribution or limitation (`review_rag_grounding_category.csv:49–75`). This technically satisfies non-empty evidence, but not the protocol's requirement that evidence point to source summary or paper evidence rather than reviewer intuition. The repeated text cannot justify fine-grained score differences such as 18 versus 15 or 11 versus 3. Replace it with summary-specific evidence or mark the ranking as low-confidence/underdetermined.

### 8. Some high scores conflate “useful upstream corpus infrastructure” with direct RAG grounding — moderate

The high placement of `S22P09` (70), `S22P07` (66), `S24P15` (67), and `S24P08` (64) is defensible only if the ranking explicitly rewards upstream evidence infrastructure. Their summaries stress that searchable corpora, linked data, and a conceptual KG/LLM framework are prerequisites, not argument-level grounding or validated retrieval systems (`summaries/22_scholastic_digital_humanities_ai_summaries.md:27–37, 51–57`; `summaries/24_islamic_comparative_scholastic_ai_summaries.md`, corresponding entries). The current explanations alternate between “concrete retrieval mechanism” and generic infrastructure language without distinguishing corpus availability, provenance, retrieval quality, entailment, and claim-level support. Re-score or rewrite explanations to make that weighting explicit; otherwise these papers outrank more direct grounding/verification evidence without a reproducible basis.

## Recommended disposition

- Preserve the CSV structure and rank arithmetic.
- Correct findings 1–5 before downstream synthesis; they are direct explanation/ranking mismatches.
- Rework the category-20 cluster and generic evidence strings before using score differences quantitatively.
- Add an explicit scoring distinction between: (a) retrieval architecture, (b) evidence/citation verification, (c) context-selection/compression, (d) upstream corpus/provenance infrastructure, and (e) merely adjacent text-generation or philosophical work.
