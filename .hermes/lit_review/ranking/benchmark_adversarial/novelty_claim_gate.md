# Adversarial benchmark review: novelty-threat and claim-validation gate

## Gate result
**REVISE BEFORE CLAIMING NOVELTY.** The top aggregate candidates contain strong prior art for argument-form classification, proof/dependency selection, evidence grounding, hallucination resistance, and abductive reasoning. No reviewed benchmark alone falsifies the entire integrated claim (source text → cross-tradition form → proof/dialectical skeleton → provenance/dependency-safe compression → downstream philosophical reasoning), but several falsify component-level “first” or “no prior benchmark” claims.

## Scope and method
- Reviewed the top **25 literal rows** sorted by `aggregate_mean_score` from `benchmark_master_matrix.csv`; duplicate/version rows were retained exactly and flagged rather than merged.
- Penalized prestige, recency, dataset size, and generic reasoning relevance. A benchmark received a threat only when its task design exposes an observable failure mode relevant to one of the six named claims.
- `direct` means the benchmark natively evaluates the claim or a close operationalization; `strong_adjacent` means it is a hard comparator but needs adaptation; `partial` means a narrow control; `none` means no meaningful test.
- Artifact access, license, exact version, and reproducibility were not inferred from paper-level evidence. The gate fails closed on those items until verified.

## Findings by claim
### Argument-form classification
QT-SCHEMES, the Walton corpus, EthiX, ElecDeb60To16, the complex argument-tree corpus, enthymeme materials, FOLIO, and the abductive syllogism dataset are direct or strong-adjacent threats. A claim that argument-form classification is unprecedented is not defensible. The remaining gap is cross-tradition scholastic coverage and preservation of distinctions such as objections, replies, and determinations—not classification in the abstract.

### Proof-skeleton extraction
FOLIO, both ProofWriter rows, LogicNLI, LeanDojo/ReProver, Isabelle premise pairs, causal-link materials, deep argumentative structures, RuleTaker, and PrOntoQA establish substantial prior art. Formal and synthetic benchmarks leave an authenticity gap, but they still falsify any unqualified claim that proof/dependency skeleton recovery has no benchmark precedent.

### Dependency-safe context compression
LeanDojo/ReProver and Isabelle premise selection are the strongest hostile controls; MultiHop-RAG tests support-chain retention. FOLIO and ProofWriter can be adapted to raw/reduced/distractor conditions, but the reviewed set contains no benchmark that natively scores compression while preserving argument dependencies, provenance, and downstream validity together. This is the most defensible remaining novelty claim, but it is currently an unverified gap rather than a demonstrated absence.

### Provenance
MISSCI PLUS, MISSCI, and MultiHop-RAG directly threaten provenance/grounding novelty through source passages, cited publications, support evidence, retrieval, fact-checking, or unsupported-claim labels. Scheme and proof corpora generally expose structural identity rather than bibliographic/source-span provenance. A provenance claim must therefore be scoped to dependency-preserving provenance across transformation, not citation grounding generally.

### Hallucination resistance
MISSCI/MISSCI PLUS, SMARTYPAT-BENCH, RuleTaker, PrOntoQA, and FOLIO provide strong hallucination or logical-consistency controls; the reviewed top-25 set also includes evidence-grounded multi-hop evaluation. “No existing benchmark tests hallucination resistance” is falsified. The defensible gap is hallucination resistance after provenance-preserving compression in authentic scholastic material.

### Downstream philosophical reasoning
The abductive syllogism dataset is the strongest direct reasoning threat; QT-SCHEMES, Walton/EthiX, argument trees, and debate materials are adjacent. None of the reviewed top candidates directly evaluates the complete scholastic downstream task over authentic, cross-tradition source material with inspectable provenance and proof/dialectical skeletons. Do not convert generic metaphysical, debate, or syllogistic reasoning into evidence of that full capability.

## Top hostile threats
1. **QT-SCHEMES / Walton / EthiX / ElecDeb** — invalidate novelty claims for scheme/form classification and structured argument mining.
2. **ProofWriter / FOLIO / LogicNLI** — invalidate unqualified novelty claims for natural-language proof/form recovery, while leaving scholarly authenticity and cross-tradition transfer open.
3. **LeanDojo/ReProver / Isabelle premise pairs / MultiHop-RAG** — invalidate claims that dependency-aware evidence selection has no prior benchmark analogue.
4. **MISSCI PLUS / MISSCI / SMARTYPAT-BENCH** — invalidate claims that evidence-grounded hallucination or symbolic consistency lacks benchmark precedent.
5. **Abductive syllogism dataset** — invalidates a broad “downstream abductive reasoning is unbenchmarked” claim, but not the integrated scholastic claim.

## Required claim repairs
- Replace “novel benchmark/task” with **integrated, cross-tradition, provenance-preserving compression and downstream scholastic reasoning** where that is the actual gap.
- Report benchmark-family deduplication in synthesis: ProofWriter, QT-SCHEMES, and LeanDojo appear multiple times in the input matrix.
- Add paired raw/reduced/distractor conditions, dependency-preservation checks, source-span/provenance retention, and downstream answer/form invariance. Without these, a benchmark comparison cannot validate the central architecture.
- Verify exact artifact access, license, version, split, and evaluator before claiming reproducibility.
- Treat the six claim columns in `novelty_claim_gate.csv` as gate outcomes, not aggregate relevance scores.

## Audit counts
- Reviewed rows: **25**
- Gate-status counts: `{'strong_component_threat': 22, 'control_not_integrated_threat': 2, 'component_control': 1}`
- Novelty-threat counts: `{'high_component': 21, 'medium_component': 4}`
- Source matrix rows: **80**; matrix file was not edited.

## Files
- `.hermes/lit_review/ranking/benchmark_adversarial/novelty_claim_gate.csv` — row-level hostile judgments.
- `.hermes/lit_review/ranking/benchmark_adversarial/novelty_claim_gate.md` — this report.
