# Grounding / evidence / provenance benchmark ranking notes

Perspective: rank benchmarks for RAG grounding, evidence retrieval, citation support, multi-hop support, and provenance traceability.

## Highest-value direct tests

1. ALCE — direct retrieve-support-generate-with-citations evaluation; separates answer quality from citation quality.
2. MISSCI PLUS — retrieves real biomedical passages and tests whether evidence supports or only appears to support a fallacious claim.
3. MultiHop-RAG — tests recovery of multiple supporting pieces and downstream answer use.
4. RAGTruth — word/case-level unsupported or contradictory span annotations for RAG outputs.
5. LeanDojo/ReProver and LeanDojo — premise retrieval, accessible-premise annotations, hard negatives, and proof verification.
6. MISSCI — cited publication evidence plus reconstruction of the unsupported bridge.

## Required distinctions

- Retrieval/citation benchmarks: ALCE, MISSCI PLUS, MultiHop-RAG, RAGTruth, LeanDojo/ReProver.
- Argument/proof diagnostics: FOLIO, ProofWriter, Magnushammer, fallacy-span/support-attack corpora, scheme corpora, and debate trees.
- Generic QA/corpus resources: cultural-value, multilingual commonsense, Quran/Hadith QA, HTR, POS, and analogy resources; useful stress tests but weak direct provenance coverage.
- Formal proof provenance is not the same as scholarly citation provenance; Lean/Isabelle give stronger correctness oracles but narrower authenticity.

## Main limitations

No benchmark fully covers source-span retrieval, citation completeness, multi-hop dependency preservation, cross-tradition argument forms, and inspectable downstream reasoning in one task. ALCE is citation-focused but mostly QA; MultiHop-RAG is multi-hop but constrained; RAGTruth detects unsupported spans but is not an argument benchmark; LeanDojo provides strict proof provenance but not open scholarly interpretation.

## Validation

- 80 input benchmark rows preserved.
- Category ranks contiguous within each category.
- Global ranks 1–80 and score-sorted with protocol tie-breaks.
- Explanations are 1–3 sentences and identify the concrete benchmark property driving the score.
- Evidence basis retains the supplied benchmark evidence and points to retained category summaries.
