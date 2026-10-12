# Continuation-candidate relevance review

## Scope and decision rule

Reviewed exactly the eight identity-passed continuation candidates in aggregate ranks 29–35 and 37:
`S04P03`, `S02P02`, `S04P02`, `18_14`, `S02P03`, `S02P04`, `S04P01`, and `S04P04`.

The project pipeline used for the hostile test is the integrated composition described in the corpus review: **cross-tradition argument/form classification; explicit deductive or argument skeleton extraction with provenance; selection or compression of reasoning-critical components under a sufficiency/minimality objective; and downstream LLM philosophical reasoning evaluation**. A paper was not treated as a full-pipeline duplicate merely because it addressed one component.

For every row, the review separately checked:

- exact project-pipeline stage(s) actually demonstrated;
- mechanism evidenced by the strongest local full text or landing record;
- transfer that is only inferred rather than demonstrated;
- novelty overlap or threat;
- missing boundaries;
- a hostile countertest removing title/venue/category prestige and testing whether a concrete mechanism remains.

Identity files and ranking files were not edited.

## Verdict distribution

| Verdict | Count |
|---|---:|
| retain_high | 4 |
| retain_mid | 4 |
| demote | 0 |
| false_positive | 0 |
| insufficient_evidence | 0 |
| **Reviewed** | **8** |

`retain_high` means a strong component-level novelty threat with a demonstrated mechanism, not exact duplication of the integrated scholastic pipeline. `retain_mid` means the evidence is useful for a bounded evaluation, taxonomy, or robustness threat but does not materially cover the core context-engineering composition.

## Candidate findings

### S04P03 — retain_high

LLMLingua-2 demonstrates learned extractive prompt compression as token classification, with distilled supervision, an explicit faithfulness objective, out-of-domain evaluation, compression ratios, and latency measurements. This is a direct threat to generic reasoning-context compression and token-retention novelty. It does **not** identify argument forms, preserve proof dependencies, track source spans, or test sufficiency/minimality for scholastic reasoning. The hostile countertest leaves a concrete compression mechanism, so the candidate remains high for the compression stage only.

Evidence: `20261012_shard1/evidence/S04P03.html`, especially lines 6, 32, and 43–69.

### S02P02 — retain_mid

The paper provides a concrete false-premise evaluation pipeline: factual-triple selection, corruption, templated question construction, internal attention-head analysis, and FAITH mitigation. It is valuable for adversarial evaluation of premise acceptance and hallucination, but its intervention is model-internal attention control rather than source-grounded argument extraction or context construction. It has no provenance, proof skeleton, scholastic protocol, or compression objective. The mechanism survives the hostile countertest, but only as a robustness/evaluation precedent.

Evidence: `20261012_shard2/evidence/S02P02_88f4f5f0ab0b15af.pdf`, pp. 1–3, especially the abstract, contributions, and §3.

### S04P02 — retain_high

LongLLMLingua demonstrates query-aware compression for long contexts, using key-information density/position considerations and reporting measurable quality, token, cost, and latency effects. This directly threatens broad novelty claims around query-conditioned selection and compression. The paper does not show argument-form classification, proof-aware dependency preservation, source-span lineage, or a sufficiency/minimality criterion. After stripping venue and branding, the mechanism remains concrete; retain high as a context-engineering comparator, not as an integrated scholastic system.

Evidence: `20261012_shard3/evidence/S04P02.html`, lines 6, 26–28, 37–57, and 152–187.

### 18_14 — retain_mid

The survey defines argument mining as automatic identification and extraction of inferential structure and surveys components, relations, data, and evaluation. Its important project-level contribution is boundary-setting: argument analysis is a structured, interdependent task, not merely sentence classification. It is not itself a new extractor, compressor, provenance system, or downstream LLM experiment, and it does not implement the cross-tradition scholastic pipeline. The hostile countertest leaves a strong taxonomy and decomposition precedent but not a direct system mechanism.

Evidence: `20261012_shard4/evidence/18_14.pdf`, pp. 1–3 and the sections covering argument components, relations, and the shift from a simple pipeline to an interconnected network view.

### S02P03 — retain_mid

This paper demonstrates a negation-sensitive robustness matrix across false-premise completion, constrained fact generation, multiple-choice QA, and fact generation, together with mitigation comparisons. It is directly useful for hostile evaluation of polarity, negation, and premise handling. It does not build source-grounded argument structures, preserve proof dependencies, compress evidence, or model scholastic forms. The task matrix remains concrete after removing the broad hallucination framing, so it is retained as a bounded evaluation precedent.

Evidence: `20261012_shard1/evidence/S02P03.html`, lines 6, 26, 39, and 48–78.

### S02P04 — retain_mid

McKenna et al. use controlled NLI transformations across several LLM families to isolate attestation/memorization and corpus-frequency biases, with adversarial controls that expose misleadingly high baseline performance. This is strong methodology for counterfactual and bias-isolating evaluation. It does not construct argument representations, select or compress evidence, preserve provenance, or intervene on a proof-oriented context. The controlled transformations remain substantive without title/venue prestige; retain mid as evaluation-design prior art only.

Evidence: `20261012_shard2/evidence/S02P04_bb046e1619932ab1.pdf`, pp. 1–3, especially the abstract, contributions, §3, and dataset-transformation discussion.

### S04P01 — retain_high

LLMLingua demonstrates coarse-to-fine prompt compression with a budget controller, token-level iterative compression that models interdependence, distribution alignment, and large compression-ratio evaluations. It is foundational direct prior art against generic prompt-compression and budget-control novelty. It does not define argument semantics, protect premises/warrants/replies, preserve provenance, or optimize logical sufficiency. The mechanism remains concrete under the hostile countertest, warranting high retention for the compression stage but not for the full project pipeline.

Evidence: `20261012_shard3/evidence/S04P01.html`, lines 6, 24–26, 36–53, and 134–167.

### S04P04 — retain_high

RECOMP is direct prior art for retrieval-conditioned compression and selective augmentation: retrieved documents are compressed before generation while answer quality and context reduction are evaluated. This threatens broad novelty claims about compact evidence contexts for RAG. It does not expose argument forms, proof dependencies, scholastic sequencing, source-span-to-output lineage, or a formal sufficiency/minimality objective. The compression/selective-augmentation mechanism survives the hostile countertest, so it remains high as a retrieval/context comparator rather than a proof-aware scholastic duplicate.

Evidence: `20261012_shard1/evidence/S04P04.html`, lines 4–6 and the preserved arXiv abstract/full-text landing capture.

## Overall adjudication

The four `retain_high` papers are strong, demonstrated threats to the project’s generic compression, query-aware selection, and retrieval-conditioned context-construction claims. They do not establish the project’s integrated gap because none demonstrates the complete chain of cross-tradition form classification, provenance-bearing argument/proof skeleton extraction, proof-critical sufficiency/minimality selection, and downstream philosophical reasoning evaluation.

The four `retain_mid` papers should remain visible as bounded precedents: `18_14` for argument-mining task decomposition and dependency-aware scope, and `S02P02`, `S02P03`, and `S02P04` for hostile evaluation of false premises, negation, and inference biases. None should be described as a direct implementation of the project pipeline.

No candidate was a false positive or evidence-blocked. No ranking or identity artifact was changed.
