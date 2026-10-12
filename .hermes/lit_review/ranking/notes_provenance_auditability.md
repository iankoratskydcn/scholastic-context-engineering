# Provenance / claim-evidence auditability benchmark ranking notes

Perspective: rank benchmarks by source provenance, claim/evidence alignment, citation support, source-span traceability, attribution, and inspectable inference dependencies.

## Highest-value direct tests

1. ALCE — retrieve support, generate answer, attach citations; separates answer quality from citation quality.
2. MISSCI PLUS — retrieves real biomedical passages and checks whether evidence supports or merely appears to support a fallacious claim.
3. MultiHop-RAG — tests recovery and use of multiple supporting pieces.
4. RAGTruth — word/case-level unsupported or contradictory span annotations for RAG outputs.
5. LeanDojo/ReProver and LeanDojo — premise retrieval, accessible-premise annotations, hard negatives, and proof verification.
6. MISSCI — cited publication evidence plus reconstruction of unsupported bridges.

## Required distinctions

- Citation/source-span benchmarks: ALCE, MISSCI PLUS, MultiHop-RAG, RAGTruth, LeanDojo/ReProver.
- Claim/argument/proof audit diagnostics: FOLIO, ProofWriter, Magnushammer, fallacy span/support-attack corpora, scheme corpora, debate trees.
- Generic QA/corpus resources: useful stress tests, weak direct claim-evidence provenance.
- Formal proof provenance is not same as scholarly citation provenance; Lean/Isabelle provide stronger correctness oracles but narrower authenticity.

## Main limitation

No benchmark fully covers source-span retrieval, citation completeness, multi-hop dependency preservation, cross-tradition argument forms, and inspectable downstream reasoning in one task. Top suite should combine citation-grounded, span-annotated, multi-hop, and proof-oracle resources.

## Validation

- 80 input benchmark rows preserved.
- Category ranks contiguous within each category.
- Global ranks 1–80, sorted by protocol tie-break.
- Scores agree across category/global outputs.
- Explanations 1–3 sentences; evidence basis preserves supplied evidence and retained summary pointer.
