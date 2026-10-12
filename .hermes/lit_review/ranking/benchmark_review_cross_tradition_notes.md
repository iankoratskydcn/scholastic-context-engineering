# Cross-tradition / historical-logical ranking notes

## Rubric

Reward explicit preservation of historical or culturally situated source material, named philosophical/metaphysical reasoning, comparative/multilingual coverage, and provenance that lets evaluator distinguish traditions. Reward argument/proof structure only when it remains interpretable as a cross-tradition diagnostic. Penalize synthetic FOL, theorem-proving, syllogism, generic Walton/Toulmin, generic debate, and context-only benchmarks when they collapse distinct traditions into one universal logic.

## Findings

- Highest direct coverage: MARS; Index Thomisticus Treebank; Classical Arabic/Quran/Hadith resources; Indian/Arab culture benchmarks; InterIDEAS.
- Medieval/Islamic source coverage exists, but mostly through language, parsing, QA, or semantic tasks—not explicit scholastic logic.
- Aristotelian material appears indirectly through syllogism/formal logic and is heavily penalized when synthetic or decontextualized.
- No supplied benchmark directly evaluates Jewish, Nyaya, or Mohist logical systems as named, historically grounded reasoning traditions. Indian culture resources are not equivalent to Nyaya logic.
- QT-SCHEMES, Walton/Toulmin, debate, proof, and analogy resources are useful adapters/controls, not substitutes for tradition-specific annotation.
- Long-context and RAG resources test preservation/retrieval support only; they do not provide cross-tradition content.

## Validation

80 input rows retained exactly. Category ranks contiguous per category. Global ranks 1-80. Tie order: numeric category, paper order, literal paper ID.
