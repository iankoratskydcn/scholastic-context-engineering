# Repair report: neuro-symbolic integration ranking

## Scope

Recalibrated the two neuro-symbolic integration CSVs using a mechanism gate. IDs were preserved exactly; no rows were removed.

## Mechanism gate

- **90–100:** demonstrated neural-to-symbolic interface, formal constraint applied to neural output, solver/theorem-prover interaction, or inspectable symbolic state.
- **70–89:** symbolic-only formal substrate with explicit rules, semantics, proof states, dialogue states, or formal relations, but no demonstrated neural coupling.
- **40–69:** indirect transfer such as structured-knowledge scaffolding, argument mining, context/tool methods, or reasoning-task analysis without a verified solver/state interface.
- **0–39:** generic/background, conceptual work, corpus/HTR infrastructure, writing-quality studies, or surveys without the target mechanism.

Every row now states concrete mechanism evidence and explicitly records absent interface/solver/state evidence where applicable. Confidence was lowered to medium for most transfer/substrate rows and retained high only where the mechanism classification is directly evidenced or exclusion is clear.

## Specific recalibrations

Historical formalizations and category-18 logic papers were moved to the symbolic-only 70–89 tier; human syllogistic studies were treated as indirect transfer; category-22 HTR/corpus infrastructure, generic hallucination/context work, and category-20 writing studies were downgraded to their respective indirect or generic bands. Direct neural-symbolic rows remain concentrated in Lean Copilot and implemented LLM/argumentation pipelines.

`S24P05` and `S24P06` remain separate immutable IDs and are explicitly flagged as duplicate publication versions of the same Maliszewski HTR/stylometry study in both CSVs.

## Ranking integrity

Category ranks were recomputed within category. Global ranks were recomputed by descending numeric score, then numeric `category_num`, numeric `paper_order`, and literal `paper_id` for ties. The output retains 124 rows in each CSV and the required column schema.
