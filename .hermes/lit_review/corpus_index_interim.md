# Literature-review corpus index (interim)

**Research date:** October 11, 2026

## Verified paper count so far

The first ten subtopic lanes returned **108 verified papers** before deduplication:

| Subtopic | Artifact | Papers |
|---|---|---:|
| LLM hallucination surveys/taxonomies | `agents/01_hallucination_surveys.md` | 9 |
| Hallucination in logical/deductive reasoning | `agents/02_logic_hallucination.md` | 11 |
| Long-context degradation/context rot | `agents/03_context_degradation.md` | 10 |
| Context/prompt compression | `agents/04_context_compression.md` | 12 |
| RAG grounding and limits | `agents/05_rag_grounding.md` | 11 |
| Chain-of-thought faithfulness | `agents/06_cot_faithfulness.md` | 12 |
| Neuro-symbolic reasoning | `agents/07_neurosymbolic.md` | 10 |
| Logic-LM/theorem provers | `agents/08_logic_theorem_provers.md` | 11 |
| Argument mining | `agents/09_argument_mining.md` | 10 |
| Walton schemes in NLP | `agents/10_walton_schemes_nlp.md` | 12 |
| **Subtotal** |  | **108** |

The second ten lanes returned **143 additional verified papers** before deduplication. The total across 20 lanes is therefore **251 verified paper records before deduplication**.

| Subtopic | Artifact | Papers |
|---|---|---:|
| Logical fallacy detection | `agents/11_fallacy_detection.md` | 13 |
| Syllogistic/deductive benchmarks | `agents/12_deductive_benchmarks.md` | 15 |
| Knowledge graphs as LLM scaffolding | `agents/13_knowledge_graphs.md` | 13 |
| Premise/proof-relevant context selection | `agents/14_premise_context_selection.md` | 18 |
| LLMs for philosophy | `agents/15_llm_philosophy.md` | 12 |
| Computational/historical logics | `agents/16_historical_logics.md` | 14 |
| Cross-cultural/non-Western logic | `agents/17_cross_cultural_logic.md` | 15 |
| Toulmin/defeasible/informal logic | `agents/18_toulmin_defeasible.md` | 15 |
| Abductive/analogical reasoning | `agents/19_abduction_analogy.md` | 15 |
| AI-generated academic/philosophical writing | `agents/20_ai_academic_writing.md` | 13 |
| **Second-wave subtotal** |  | **143** |
| **All 20 lanes, pre-deduplication** |  | **251** |

The scholastic-method sweep returned **70 additional verified records** before deduplication. The total corpus is now **321 verified paper records before deduplication**.

| Scholastic-method angle | Artifact | Papers |
|---|---|---:|
| Direct scholastic method + AI | `agents/21_scholastic_method_ai_direct.md` | 10 |
| Scholastic digital humanities + AI | `agents/22_scholastic_digital_humanities_ai.md` | 15 |
| Disputatio/dialectical AI | `agents/23_disputatio_dialectical_ai.md` | 12 |
| Islamic/comparative scholastic AI | `agents/24_islamic_comparative_scholastic_ai.md` | 17 |
| AI philosophy/dialectical methods | `agents/25_ai_philosophy_dialectical_methods.md` | 16 |
| **Scholastic sweep subtotal** |  | **70** |
| **All 25 lanes, pre-deduplication** |  | **321** |

## Highest-priority novelty threats identified so far

1. **Explanation-Refiner (Quan et al., EMNLP 2024):** elicits sufficient/necessary facts, identifies relevant/redundant/unrelated sentences, constructs a formal theory from selected facts, and verifies/refines the proof with Isabelle/HOL. Strongest direct threat to proof-relevant context construction.
2. **Trajano et al. (COMMA 2024):** uses argument-scheme classification to provide scheme-relevant context/examples to an LLM translating natural-language arguments into computational arguments, with RAG and wrong-scheme retrieval discussed. Strongest Walton-specific threat.
3. **FRVA (Findings ACL 2024):** filters irrelevant facts to reduce proof search and constructs verified entailment trees. Strong threat to proof-relevant selection, though not scheme mining.
4. **Feng & Hirst (ACL 2011):** scheme classification followed by enthymeme/missing-premise reconstruction. Foundational threat to argument-form → latent reasoning structure.
5. **Logic-LM/LINC:** natural language to symbolic logic/prover pipelines. Threaten claims about formal argument extraction, but not necessarily selective context construction.
6. **LeanDojo/ReProver, Magnushammer:** explicit premise selection for formal theorem-proving contexts. Threaten formal-premise retrieval claims, not natural-language cross-tradition scheme extraction.
7. **LLMLingua-2, LongLLMLingua, RECOMP, Selective Context:** strong generic compression/selection baselines. If the proposed system only classifies tokens/sentences as useful, novelty is weak.

## Current gap formulation (provisional)

Do not claim novelty for argument-scheme classification, prompt compression, proof-premise retrieval, or LLM-to-formal-logic translation individually. The defensible candidate gap is the **integrated, inspectable, proof-oriented composition**:

> classify natural-language spans across multiple argument/formal reasoning traditions; extract an explicit deductive/argument skeleton with provenance; select or compress only reasoning-critical components under a stated sufficiency/minimality objective; and evaluate the resulting compact context on downstream LLM philosophical reasoning.

This remains provisional until the premise/context-selection lane and the remaining ten lanes are reconciled and deduplicated.
