# Adversarial review: formal-logic compatibility ranking

## Verdict

**Conditionally usable, but not decision-grade without a semantic re-ranking pass.** The two CSVs are structurally compliant with the ranking protocol and agree with `remaining_nonbenchmark.csv`, but the ranking construct is under-specified and the evidence frequently proves only benchmark status, not formal-logic compatibility.

## Verification performed

- `remaining_nonbenchmark.csv`: 124 rows / 124 unique paper IDs.
- Category review: 124 rows / 124 unique IDs; all IDs match the remaining set; category ranks are unique within every category and follow descending score with canonical-order tie breaks.
- Global review: 124 rows / 124 unique IDs; all IDs match the remaining set; global ranks are unique and follow descending score with canonical-order tie breaks.
- Metadata (`category_num`, `category`, `paper_order`, `citation`) matches the source in both outputs.
- Scores are integers in the required 0–100 range.
- Explanations and evidence fields are populated.

No mechanical schema, coverage, duplicate, or rank-order defect was found.

## Findings

### 1. The viewpoint collapses distinct compatibility targets into one score — **high severity**

“Formal logic and theorem-prover compatibility” is being used for at least four different properties:

1. executable proof search / theorem-prover integration;
2. formal reconstruction or correctness proofs of historical logic;
3. defeasible, dialectical, or argumentation semantics;
4. natural-language argument mining, scheme extraction, or debate generation.

These are not interchangeable. `S08P06` (*Lean Copilot*) is direct Lean/theorem-prover integration; `S24P02` is a symbolic reconstruction and correctness proof; `18_02` and `18_04` are defeasible logic formalisms; `S21P05` extracts arguments from debate text into argumentation and description logics. They can all be relevant, but the current single 0–100 scale does not state whether direct prover interoperability outranks formal semantics, or whether extraction systems are being judged as upstream input to a prover rather than as provers themselves.

**Required repair:** add explicit subdimensions or a reviewer rubric, at minimum: `prover_integration`, `formal_semantics`, `extraction_to_formal_structure`, and `scholastic_project_transfer`. Recompute the aggregate score from those dimensions or state an explicit precedence rule.

### 2. Evidence often supports “not a benchmark,” not the claimed ranking rationale — **high severity**

Many rows use evidence such as “source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact.” That is sufficient to justify inclusion in `remaining_nonbenchmark.csv`, but it does not establish the concrete feature driving a compatibility score. The protocol requires evidence for the ranking rationale, not merely evidence that the paper is non-benchmark.

This is especially weak across the 16-series historical-logic rows, where identical evidence is paired with scores of 62, and across the 18-series formal argumentation rows, where identical evidence is paired with scores from 70 to 100. The score differences are therefore not auditable from the CSV evidence.

**Required repair:** cite the summary/paper passage establishing the actual mechanism: a Lean/ prover interface, executable state machine, proof procedure, typed logic, argument graph, extraction task, or merely conceptual discussion. Do not reuse benchmark-status boilerplate as compatibility evidence.

### 3. Formalization is repeatedly treated as theorem-prover compatibility without an implementation gate — **high severity**

The source summaries explicitly distinguish symbolic formalization from NLP or validated implementation. For example, the summary for `S24P02` describes a narrow symbolic reconstruction and correctness proof, while `S24P03` is a conceptual formal account with no released implementation or empirical evaluation. The review nonetheless gives `S24P02` and several `S24` items scores near or above direct computational argumentation systems.

A proof in a paper, a mathematical formalization, and a theorem-prover-compatible artifact are different evidence classes. The current ranking gives no penalty for absent executable representation, machine-readable formal language, prover export, or reproducible implementation.

**Required repair:** distinguish `formalizable_in_principle` from `executable/prover_compatible`; require an implementation/prover artifact before assigning the top band (for example, 90–100).

### 4. Natural-language argument extraction is not separated from formal reasoning — **high severity**

The strongest extraction precedents (`S21P02`, `S21P05`, `S10P10`, and the argument-mining items) identify spans, support/attack relations, schemes, or debate structure. That is valuable upstream infrastructure, but it does not establish soundness, completeness, proof checking, or theorem-prover interoperability. The summaries themselves state these limits: `S21P05` models debate support/attack networks rather than the scholastic sequence, and `S24` formalization papers generally do not perform argument identification from prose.

The ranking explanation often calls both groups “formal argumentation” or “formalizable inference structure,” which obscures whether the paper contributes a parser, an intermediate representation, or a reasoning engine. This can cause extraction papers to be over- or under-ranked depending on an unstated assumption about the intended architecture.

**Required repair:** label each paper by pipeline role: `text_to_structure`, `structure_to_inference`, `prover_integration`, or `conceptual/background`; score transfer to the project separately from logical validity.

### 5. A verified false positive remains materially over-ranked — **medium severity**

`S21P01` (*Scholastic: Graphical Human–AI Collaboration for Inductive and Interpretive Text Analysis*) is ranked `category_rank=6`, `global_rank=61`, score 61. The source summary explicitly calls it a false positive: “Scholastic” is an HCI system and it does not represent a quaestio, objections, distinctions, determination, replies, or formal logic. Its only stated transfer is generic human-guided structured context over a corpus.

That may justify a low adjacent-relevance score, but a score of 61 places it above multiple actual argument-mining, formalization, and logic-adjacent items with scores in the 40s–50s. Under a formal-logic compatibility lens, the false-positive status should trigger a substantial penalty or an explicit `not_formal_logic` flag.

**Required repair:** move it to the bottom of the relevant category or mark it as excluded from formal-logic compatibility while retaining it for HCI/context-engineering review.

### 6. The ranking contains no explicit novelty-threat or evidence-confidence adjustment — **medium severity**

The protocol says all reviewers should weigh project relevance, novelty threat, methodological transfer, and likely usefulness, but the output has only one score and a generic confidence field. A high-confidence historical formalization, a high-confidence theorem-prover system, and a low-confidence recent extraction paper can receive comparable scores without showing how uncertainty or novelty threat affected the result. `S10P10` is marked low confidence while receiving score 68; `S24P04` is high confidence with score 87 despite being described as a closed-domain formalization with no benchmark dataset.

**Required repair:** add explicit columns for at least `relevance`, `novelty_threat`, `transfer`, and `evidence_confidence`, or document a deterministic mapping from those factors to `score_0_100`.

## Sample evidence-based adjudications

- **Keep at/near the top:** `S08P06` because the supplied evidence identifies direct Lean/theorem-prover integration; this is the cleanest match to the literal viewpoint.
- **Keep high but classify differently:** `S24P01` and `S24P02` because they provide executable or correctness-oriented symbolic reconstructions, but they should be labeled historical formalization rather than theorem-prover integration unless a prover artifact is verified.
- **Keep as adjacent upstream work:** `S21P02` and `S21P05` because they connect natural-language argument extraction to formal argumentation; do not treat them as proof-library or theorem-prover results.
- **Downgrade or separate:** `S21P01`, HTR/stylometry infrastructure in `S22P01`/`S22P03`, and generic long-context/compression/philosophy papers. Their evidence supports corpus/HCI/context relevance, not formal-logic compatibility.
- **Reassess:** `S24P03` and `S24P04`; the summaries describe conceptual or closed-domain set-theoretic formalization without validated implementation, so their scores should be determined by formal-semantic transfer rather than inferred prover compatibility.

## Conclusion

The files pass the ranking protocol mechanically, but the ranking is not yet semantically calibrated. The principal adversarial risk is construct leakage: proof libraries, historical formalization, computational argumentation, and natural-language argument extraction are all being placed on one scale while the evidence does not identify the transfer mechanism or implementation level. Re-rank only after adding the compatibility-axis rubric and replacing benchmark-status boilerplate with claim-specific evidence.
