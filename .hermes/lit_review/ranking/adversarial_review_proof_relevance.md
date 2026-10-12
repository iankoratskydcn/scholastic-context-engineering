# Adversarial review: proof-relevance ranking

## Verdict

**Substantive revision required.** The two CSVs are structurally valid and internally synchronized, but the ranking evidence does not consistently measure proof relevance. It frequently substitutes generic retrieval/compression utility, formalization, or argumentation adjacency for demonstrated proof-relevant context selection and proof-grounded evidence preservation.

## Structural verification

- Both review files contain 124 rows, exactly matching `remaining_nonbenchmark.csv`; no missing, extra, or duplicate `paper_id` values were found.
- Required columns are present; scores are integers in `[0, 100]`.
- Category and global ranks are complete, unique within their required scope, and ordered consistently by descending score with canonical `paper_id` tie-breaking.
- The category and global files agree on all shared metadata, scores, explanations, and evidence fields.
- Category file has blank `global_rank`; global file has blank `category_rank`, as required.

These checks establish formatting correctness only; they do not validate the substantive score model.

## Findings

### 1. Evidence grounding is often benchmark-status evidence, not proof-relevance evidence — **major**

A large fraction of rows use evidence such as “no benchmark artifact,” “no benchmark introduced,” or a generic description of the source type as the main `evidence_basis`. This establishes that a paper is non-benchmark or conceptual, but it does not establish its proof-relevance score, its relation to proof-preserving selection, or its transfer to the project. The boilerplate is especially pervasive for all 14 papers in category 16, all 13 in category 20, and most of category 18.

Examples:

- `18_01`–`18_14` cite only the generic source-artifact description in `review_proof_relevance_category.csv` lines 65–75, while the explanations claim explicit proof/defeat semantics or selector relevance.
- `S23P01` (line 107) cites “Formal dialogue reconstruction; no benchmark artifact” even though its score of 78 depends on regulated dialogue and terminal evaluation, not benchmark status.
- `S24P01` (line 110) cites “Historical formalization of Avicenna proof search; no benchmark” for a 68 score.

**Required correction:** evidence basis should cite the concrete proof-relevance mechanism: premise selection, proof-state retrieval, logical dependency preservation, formal validity checking, critical-question handling, or an explicit absence thereof. Benchmark absence may be a secondary fact only.

### 2. “Direct precedent” is applied to formal or dialectical work that does not select natural-language proof context — **major**

The review repeatedly labels papers as direct proof-relevance precedents when the supplied summaries explicitly describe a different regime:

- `18_01`, `18_02`, `18_03`, `18_04`, `18_05`, `18_06`, and `18_08` are symbolic defeasible-logic or argumentation formalisms. The category-18 summary says these systems presuppose structured arguments and do not extract them from open-domain language or rank passages under a context budget (summary lines 5–19). They are important formal semantics/design baselines, but not direct selectors.
- `S23P01` is a formal reconstruction of medieval obligation dialogue, not a proof-relevant retrieval or sentence-selection system (summary lines 3–4).
- `S24P01` is a historical formalization of Avicenna proof search, not natural-language evidence selection (summary lines 3–4). Its CSV explanation begins “direct premise retrieval” but then concludes “indirect precedent,” an internal semantic mismatch (category CSV line 110).
- `S21P08` is a literature review of argumentation schemes, yet receives 75 and is called a direct precedent (category CSV line 94).

**Required correction:** separate (at minimum) formal proof-context retrieval, formal proof semantics, natural-language proof-relevant selection, and general argument/dialogue structure. Formal semantics can score high for methodological transfer, but should not be described as direct selector precedent without an actual selection interface and proof-validity link.

### 3. Generic context compression/retrieval is over-credited as proof relevance — **major**

`S04P04`–`S04P07` and `S04P10` receive 66, placing them above `S08P06`-adjacent formal/context papers and many explicit argument-structure papers. Yet the category-04 source summary states that RECOMP, AutoCompressors, ICAE, and tool-documentation compression do not identify claims, premises, warrants, proof dependencies, or logical skeletons (summary lines 15–18, 23–29, 39–41). Their contribution is downstream task utility, latent compression, or schema-critical span protection—not proof-relevance.

This is exactly the generic-retrieval failure mode the review was supposed to challenge: a compressor can preserve answer performance while deleting an indispensable premise, and a retriever can be query-relevant without being proof-sufficient. The current explanations acknowledge the missing proof structure (“indirect precedent”) but retain scores of 66, making the ranking numerically inconsistent with the stated viewpoint.

**Required correction:** score generic compression as an adjacent baseline unless the evidence demonstrates proof-relevant selection, sufficiency/minimality, dependency preservation, or formal verification. Add a separate generic retrieval/compression adjacency flag rather than folding it into proof relevance.

### 4. Formal and natural-language regimes are not explicitly calibrated — **major**

The score scale conflates unlike objects:

- Formal defeasible systems: `18_01`–`18_06`, `18_08`, and `18_13` all receive 79; the conceptual/formal survey items `18_07`, `18_09`, and `18_14` still receive 72.
- Formal dialogue and scholastic-method items receive 74–78 (`S23P01`–`S23P03`, `S21P08`).
- Natural-language argument/dialogue systems in category 21 receive mostly 72 despite varying from false-positive HCI infrastructure to structured dialogue generation and claim verification (`S21P01`, `S21P02`, `S21P05`, `S21P06`, `S21P10`; category CSV lines 89–96).
- Generic compression systems receive 58–66, while `S24P01` receives 68 despite having no retrieval stage.

The summaries themselves distinguish these regimes: formal-library premise retrieval is direct for Lean systems, natural-language proof-relevant selection is a separate regime, and formalization/argument extraction are only adjacent (summary 08 lines 49–51). The CSV has no regime field and no consistent penalty for missing the selector-to-proof interface.

**Required correction:** introduce explicit dimensions or labels for (a) formal proof-state/premise retrieval, (b) natural-language proof-relevant sentence selection, (c) formal semantics/verification, (d) argument extraction/dialogue structure, and (e) generic retrieval/compression. Do not compare their raw scores as if they measured one capability without calibration.

### 5. Explanations are highly templated and omit paper-specific discriminators — **moderate**

Only 20 distinct explanation strings are used for 124 papers; one generic “survey, conceptual, or infrastructure” explanation appears 58 times. This satisfies the sentence-count requirement but not the protocol’s demand to name the concrete feature that drove the ranking. The explanation does not distinguish, for example, a defeasible proof engine from a survey, a formal dialogue semantics paper from a chatbot survey, or a latent compressor from sentence-level selection.

The strongest example is category 18: eight distinct formal papers receive the same 79 score and nearly identical explanation, despite their summaries differentiating argument graphs, defeat procedures, proof standards, Toulmin mapping, and limitations. Category 21 similarly assigns 72 to heterogeneous systems without identifying whether the mechanism is argument mining, claim verification, dialogue generation, or tutoring.

**Required correction:** each explanation should name the paper-specific mechanism and its exact proof-relevance limitation, e.g. “formal defeasible warrant evaluation without text extraction,” “natural-language sentence selection with prover feedback,” or “query-aware compression without dependency preservation.”

### 6. Confidence and evidentiary uncertainty do not affect the ranking rationale — **moderate**

`S02P08` and `S10P10` are explicitly low-confidence/uncertain in the source evidence, yet receive scores of 62 and 65 and are ranked alongside higher-confidence items without explaining why uncertainty does not reduce their proof-relevance placement. `S24P14` is medium confidence but receives the same 58 as several high-confidence formalization items. The protocol permits confidence as a separate field, but the explanations should state whether the score is provisional and which claim remains unverified.

**Required correction:** retain the score if justified, but mark uncertain evidence as a bounded provisional estimate and state the missing verification. Do not use “uncertain benchmark status” as if it were evidence of proof relevance.

### 7. The ranking underweights the strongest natural-language proof-selection threat in the source evidence — **major**

The source summary for category 08 identifies Explanation-Refiner as the closest verified prior art: it selects sufficient, necessary, redundant, and unrelated natural-language facts, formalizes selected facts as axioms, and uses Isabelle/HOL feedback (summary 08 lines 13–15). The retained row `S08P06` is Lean Copilot, which is a strong formal premise-retrieval precedent and correctly ranks first at 96, but its evidence basis and explanation do not distinguish formal-library retrieval from natural-language proof-relevant selection (category CSV line 32). The review therefore risks presenting “direct premise retrieval” as one undifferentiated capability and obscuring the natural-language regime’s closest threat.

This is a grounding/comparability issue rather than a claim that `S08P06` is incorrectly included: the row is relevant, but the explanation should explicitly say that Lean Copilot is direct for formal Lean premises and only indirect for natural-language proof-context selection.

**Required correction:** preserve the high score if desired, but split the rationale by regime and add the natural-language/formal boundary to the viewpoint explanation.

## Acceptance recommendation

Do not accept the ranking as substantively validated yet. The structural checks pass, but the following must be repaired before relying on the order:

1. Replace generic benchmark-status evidence with mechanism-level proof-relevance evidence.
2. Reclassify formal semantics, formal dialogue, argument extraction, generic retrieval/compression, and actual proof-context selection into explicit regimes.
3. Re-score or annotate generic compressors and non-selector formalisms so their indirectness is reflected numerically.
4. Rewrite templated explanations with paper-specific discriminators and explicit limitations.
5. Preserve uncertainty where source verification is incomplete.
6. Re-run the category/global rank validation after any score changes.

**Issue count:** 7 substantive issue classes; the most consequential are evidence misgrounding, generic-retrieval conflation, and failure to separate formal from natural-language proof-relevance regimes.
