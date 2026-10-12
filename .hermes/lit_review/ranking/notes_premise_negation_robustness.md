# Premise, negation, contradiction, logical-error robustness

Ranking rule: reward benchmarks that manipulate premise truth, expose explicit negation/quantifier structure, label contradiction/unknown, provide proof or attack traces, or isolate fallacy/logical-error types. Penalize generic QA, retrieval, cultural knowledge, long-context, OCR, and language resources when premise robustness is incidental.

Top direct diagnostics: PCBench, FalseQA, KG-FPQ, FOLIO, LogicNLI, ProofWriter, SMARTYPAT-BENCH, RuleTaker, SylloBase, and the abductive syllogism dataset. FalseQA and KG-FPQ test rejection/correction of false premises; PCBench adds typed premise errors; FOLIO/LogicNLI/ProofWriter provide structured contradiction and derivation checks.

Limits: synthetic rule/proof benchmarks maximize diagnostic control but underrepresent authentic philosophical prose; argument/fallacy corpora improve implicit-premise realism but often lack exhaustive negation counterfactuals. Use this perspective with argument-form, grounding, and scholarly-text-fit reviews rather than alone.
