# Ablation/intervention ranking notes

Perspective: benchmark usefulness for controlled context interventions, not prestige.

Prioritize benchmarks that expose paired conditions: raw context, classified/skeletonized context, compressed context, distractor-augmented context, and proof-/evidence-relevant selection, with measurable downstream outcomes.

Top signal: LongPiBench/RULER/NoLiMa for context-position and semantic-retrieval stress; LeanDojo/ReProver and Isabelle/Magnushammer for dependency-aware premise selection; ALCE/MultiHop-RAG for support retention and answer outcomes; ProofWriter/RuleTaker/FOLIO for controlled reasoning ablations.

Important limits: generic long-context suites need task adaptation; formal proof benchmarks do not preserve scholarly prose; citation/RAG benchmarks do not by themselves test argument skeleton fidelity; authentic corpora often lack counterfactual intervention labels.

Duplicate benchmark families retained per protocol. Scores rank intervention diagnosticity and adaptation value, not paper quality.
