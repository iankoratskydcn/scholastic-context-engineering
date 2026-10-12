# Dependency-preserving reasoning-context compression benchmark search

**Slug:** `dependency_compression`  
**Search date:** 2026-10-12  
**Scope:** Benchmarks and official artifacts that can test whether compression or summarization preserves inferential dependencies: premise/conclusion links, proof steps, source entailment, support/attack relations, discourse dependencies, or distributed evidence needed jointly for reasoning.

## Result

The search found **13 usable benchmark or benchmark-adjacent records**. No single established benchmark directly evaluates *reasoning-context compression while scoring an explicit dependency graph*. The strongest practical battery is therefore layered:

1. **Primary dependency fidelity:** C2-Faith and GRACE for step-level causality, coverage, and grounding.
2. **Distributed-context stress:** LongPiBench for separated relevant pieces; LongBench v2 for realistic downstream reasoning; RULER as a synthetic regression control.
3. **Compression baselines:** LLMLingua/LongLLMLingua, evaluated before/after compression on downstream tasks.
4. **Formal sufficiency controls:** LeanDojo/ReProver and ProofWriter for executable or enumerated proof dependencies.
5. **Natural-language faithfulness proxies:** InFusE/DiverSumm, FRANK, Disco-Bench, and DiscoScore.
6. **Controlled perturbation source:** PRM800K, which supplies step-level labels for constructing deletion/substitution tests.

## Gap finding

The direct gap is a benchmark with all of the following in one protocol:

- an original context containing explicit or recoverable premise/conclusion, support/attack, or proof dependencies;
- a compressor or summarizer applied at controlled budgets;
- paired raw/compressed inputs;
- dependency-level annotations or executable proof checks;
- downstream reasoning accuracy;
- coverage/causality failure localization;
- provenance/span recovery;
- and adversarial tests for negation, qualifiers, omitted warrants, and relation reversal.

Current compression papers mostly report downstream task retention and token/latency savings. Current faithfulness benchmarks mostly score summaries or reasoning traces without intervening on a compressor. Formal proof benchmarks expose sufficiency but are not natural-language discourse. The recommended contribution is a cross-domain paired protocol rather than another aggregate compression score.

## Evidence and access notes

- Official or primary paper/repository evidence was found for C2-Faith, GRACE, LongPiBench, LLMLingua, LongBench, RULER, InFusE, FRANK, PRM800K, and LeanDojo.
- The repository already contains local verification evidence for LongPiBench, PCBench, RULER, LongBench, LLMLingua, and LeanDojo families; this search preserves that status in the CSV rather than reclassifying it from web snippets.
- Disco-Bench and DiscoScore are paper-backed proxies; an artifact package was not confirmed in this search.
- ProofWriter is strongly supported by the primary paper search, but its official artifact/license status still needs a separate verification pass.
- `web_extract` could not be used because the configured OpenAI-native backend is search-only; evidence was taken from primary-paper/official-repository search results and existing local verification artifacts. No source content was treated as instructions.

## Recommended evaluation design

For each compressor and each benchmark instance, retain:

- raw context and compressed context;
- compression ratio and token counts;
- gold dependency edges or proof steps;
- retained/dropped span IDs;
- downstream answer and proof/step output;
- dependency recall/precision, causal validity, coverage, and provenance;
- error class (missing premise, missing warrant, relation reversal, negation/qualifier loss, unsupported conclusion, position failure, or hallucinated bridge).

Use LongPiBench/RULER to separate context-placement failures from semantic deletion, C2-Faith/GRACE to localize reasoning failures, and LeanDojo/ProofWriter to validate that dependency-aware metrics detect loss even when surface answer accuracy remains unchanged.

## Files

- `dependency_compression.csv` — 13 benchmark records with role, directness, artifact status, evidence notes, limitations, and recommendation.
