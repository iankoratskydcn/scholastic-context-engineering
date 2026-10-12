# Adversarial review — dialectical-AI ranking

## Verdict

**PASS WITH ISSUES.** The files are structurally valid and the top of the ranking generally captures explicit dialogue protocols, argument structure, critical questions, defeasible defeat, contestability, or objection/reply behavior. The ranking is not yet cleanly adversarial against the key distinction between **regulated disputation** and generic debate/argumentation: several explanations flatten that distinction, and one within-category ordering is debatable under the stated viewpoint.

## Validation performed

- `review_dialectical_ai_category.csv`: 124 rows, 124 unique IDs.
- `review_dialectical_ai_global.csv`: 124 rows, 124 unique IDs.
- `remaining_nonbenchmark.csv`: 124 rows, 124 unique IDs.
- Both review files contain exactly the same IDs as `remaining_nonbenchmark.csv`; no missing or duplicate IDs.
- Scores are integers in 0–100.
- Category ranks are unique within each category; global ranks are unique across all 124 papers.
- Category and global rank orders are consistent with descending score and canonical `paper_id` tie-breaking.
- Global score sequence is monotone descending.

## Findings

### ISSUE-1 — Explanations are too templated to prove dialectical relevance

**Severity: moderate.** The ranking meets the 1–3 sentence length requirement, but many explanations reuse broad templates such as “adjacent evidence for structured reasoning or reliable generation” and then append the same transfer target: “a machine-readable objection/reply pipeline.” This is not enough to show whether a paper contributes an explicit opponent/respondent protocol, a typed objection, a critical question, a reply-to-objection relation, a defeat/acceptance rule, or only generic argument structure. The category file has 36 unique explanation strings across 124 rows; 23 rows share one generic adjacent-reasoning explanation, and 40 evidence fields use the same non-specific source-artifact wording.

Examples: `S21P08`, `S21P09`, `S21P07`, most category-16 rows, and many category-24 rows. For these papers, the score may be defensible, but the explanation does not expose the concrete feature that separates direct disputation precedent from merely structured reasoning.

### ISSUE-2 — Generic debate/argumentation is sometimes presented as direct objection/reply precedent

**Severity: moderate.** The source summaries explicitly distinguish adjacent systems from the scholastic sequence. The category-21 summary says none of the retained papers implements the full *quaestio/disputatio* workflow, and specifically describes Alfano et al. as support/attack debate reasoning without the *quaestio*, enumerated objections, distinctions, determination, or reply ordering; Mitsuda et al. separates an argumentative skeleton from language realization but does not model explicit scholastic stages. Nevertheless, `S21P05` receives 97 and `S21P06` 95, with explanations that end in an unqualified “objection/reply pipeline” transfer target.

This is not necessarily a wrong score—these are strong novelty-threat comparators—but the explanation should label them as **generic support/attack or structured-dialogue analogues**, then state the missing disputational machinery. Otherwise the ranking risks treating “debate reasoning” as equivalent to regulated objection/reply structure.

### ISSUE-3 — `S23P03` versus `S23P02` needs an explicit rationale or rank reversal

**Severity: moderate.** In category 23, `S23P03` (Castagna et al., computational-argumentation chatbots survey) is rank 2 / global rank 6 / score 93, while `S23P02` (Maudet, Parsons & Rahwan, argumentation in multi-agent systems) is rank 3 / global rank 9 / score 89. The source summary characterizes `S23P02` as explicitly covering locutions, commencement, commitments, critical questions, and termination rules—very close to protocol-level disputation. `S23P03` is broader and covers argument extraction, reply structuring, semantics, delivery, and chatbot dialogue types, but does not itself implement a complete disputation engine.

The current ordering can be defended if current-chatbot applicability is weighted above protocol directness, but that weighting is not stated. Under the requested adversarial lens—disputation/objection/reply structure rather than generic debate—`S23P02` is at least a co-equal and plausibly the higher-ranked precedent. Add a directness rationale or swap the two.

### ISSUE-4 — Some high scores overstate the relevance of formal logic/corpus infrastructure to interactive disputation

**Severity: minor-to-moderate.** `S22P13` (UniQ debate database, score 69) and `S24P01` (Avicenna proof-search formalization, score 66) are useful resources, but their evidence supports historical debate retrieval or formal proof structure, not an executable objection/respondent/reply protocol. Likewise, `S10P04` (Green, score 87) is described in its evidence as domain-specific scheme programs, while the explanation generalizes this into an objection/reply pipeline; the source summary presents it as a near miss, not a generic computational disputation engine.

These scores need not be reduced substantially, but the explanations should separate the contribution types: **corpus/provenance**, **formal proof/search**, **scheme extraction**, and **interactive protocol**. Without that separation, the global scale makes heterogeneous forms of relevance look commensurable in a way that obscures the project’s central novelty boundary.

## Sampled explanation verification

- `S23P01` is well supported. The source summary states alternating Opponent/Respondent moves, a positum, constrained admissions/denials, formal dialogue states, and terminal consistency/success conditions. Score 100 and the explicit protocol-focused explanation are justified, with the important limitation that it is not a full Thomistic *quaestio*.
- `S23P02` is well supported and arguably under-ranked relative to `S23P03`: the source states dialogue protocols, locutions, commencement/commitment/termination rules, schemes, and critical questions.
- `S23P03` is supported as a broad computational-argumentation chatbot survey, including reply structuring and protocol-based systems, but its explanation should say “survey-level adjacent substrate,” not imply that it itself supplies a complete objection/reply engine.
- `S21P02` is well supported as contestable claim verification with an explicit argumentation layer; the source summary also clearly says it does not implement the ordered medieval workflow. The 92 score is plausible if the missing scholastic stages are stated in the explanation.
- `S21P05` and `S21P06` are supported as strong adjacent precedents, but their explanations omit the source-verified limitation that they lack the *quaestio*, distinctions, determination, and explicit reply ordering.
- `18_05` and `18_06` are well supported as formal dialectical/defeasible precedents: schemes, critical questions, argument graphs, burdens of proof, and evaluation are concrete features. They should still be distinguished from a full scholastic protocol.
- `S10P04` is supported as scheme-program prior art, but the score-87 explanation overgeneralizes from domain-specific scheme mining to a complete objection/reply pipeline.
- `S22P13` is supported as a structured historical debate corpus, but not as an AI dialogue or response protocol; the explanation correctly identifies retrieval/evaluation value but should keep that resource role explicit.

## Recommended disposition

Keep the file structure and numerical validation as-is. Before treating the ranking as final, revise explanations for the high and mid-ranked rows to include a typed directness label such as:

- `protocol-direct`: explicit regulated moves, roles, commitments, termination, or reply obligations;
- `argumentation-adjacent`: support/attack, schemes, critical questions, defeat, or graph reasoning without scholastic sequencing;
- `infrastructure-adjacent`: corpus, retrieval, proof-search, or formalization resource without interactive disputation;
- `generic`: broad reasoning or reliability relevance only.

Then either justify or reverse `S23P03`/`S23P02`. The ranking is otherwise mechanically sound and broadly points the highest scores toward the correct novelty-threat region.
