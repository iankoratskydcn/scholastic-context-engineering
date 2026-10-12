# Neuro-symbolic/formal-proof benchmark review

Perspective: rank the 80 retained benchmark studies for natural-language-to-logic mapping, proof traces, premise selection, Lean/Isabelle compatibility, and executable rules. Penalize generic QA and symbolic-only resources lacking natural-language/project transfer.

Top direct candidates: LeanDojo/ReProver, ProofWriter, FOLIO, MALLS/LogicLLaMA, Magnushammer Isabelle premise pairs, LogicNLI, RuleTaker, PrOntoQA, SMARTYPAT-BENCH. Use ProofWriter/RuleTaker for controlled proof depth and FOLIO/LogicNLI for human-authored NL-to-FOL transfer; use LeanDojo/Magnushammer for actual prover and premise-selection interfaces.

Scores are perspective-specific suitability, not prestige. Existing summary artifacts and benchmark evidence were retained in `benchmark_studies.csv`; no duplicate benchmark records were merged.
