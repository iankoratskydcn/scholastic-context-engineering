# Gap search: pipeline composition ablation and dependency-removal evaluation

**Slug:** `pipeline_composition_ablation`  
**Search date:** 2026-10-12 (US/Eastern)  
**Scope:** Scholarly benchmark methodologies for evaluating the full Scholastic Context Engine composition—extraction → selection → compression → reasoning/output—through component ablations, controlled perturbations, dependency removal/substitution, and faithfulness checks.

## Result

The search retained **14 records**. The strongest direct methodologies are: **AbGen** for specifying and judging ablation designs; **ERASER** for retained-context sufficiency and removed-context comprehensiveness; **FACT-E** and **Interventional Grounding Audits** for step/dependency interventions; **Meadows et al.** for graded premise-removal curves with manual adjudication; and **MoPS** for explicit module-dependency ablation. **MuFaSSa**, **GRACE**, **FUR**, **LeanDojo**, **ProofWriter**, and **LongPiBench** provide complementary faithfulness, formal sufficiency, and placement controls.

## Recommended composition-level protocol

1. **Define a typed pipeline graph.** Treat extraction, attribution, form classification, selection, compression, dependency repair, and reasoning/rendering as named modules with declared inputs/outputs and provenance IDs.
2. **Run a full system and single-removal matrix.** For each module, compare full composition, module removed, module bypassed with a strong baseline, and a randomized/negative control. Report both end-task score and intermediate artifact quality.
3. **Use graded dependency interventions.** For each retained claim/premise/edge, run: (a) deletion, (b) semantic substitution with a fresh symbol, (c) qualifier/negation reversal, and (d) source-span masking. Preserve paired raw/intervened contexts.
4. **Measure more than final accuracy.** Include extraction/attribution precision-recall, dependency-edge recall/precision, proof validity, answer correctness, provenance recovery, compression ratio, latency/cost, and failure class. ERASER-style sufficiency/comprehensiveness should be reported alongside distribution-preserving controls.
5. **Separate failure causes.** Use LongPiBench-like distance/placement controls to distinguish missing dependencies from positional context failure; use LeanDojo/ProofWriter-like executable or enumerated proof controls to distinguish invalid reasoning from parser/selection failure.
6. **Add hostile metric validation.** Apply Goodhart-style adversarial tests and random-removal baselines; do not interpret a score as causal dependence unless the intervention changes only the claimed dependency and keeps the input in support.
7. **Adjudicate alternate valid paths.** As in the physics premise-removal study, manual review or proof checking is needed when removal causes a model to choose a different valid derivation rather than fail.

## Gap finding

No retained work combines all target properties in one benchmark: authentic scholarly arguments, typed extraction/attribution artifacts, an explicit dependency graph, controlled extraction-to-compression interventions, downstream dialectical reasoning, provenance audits, and adversarial negation/qualifier/source-reversal tests. The contribution opportunity is a paired, graph-aware benchmark rather than a single aggregate compression score.

## Search coverage and limitations

Primary/official scholarly pages were consulted for the ACL/EMNLP/EACL records and arXiv record listed in the CSV. Existing repository evidence was used for LeanDojo, ProofWriter, LongPiBench, GRACE, and the dependency-compression comparison. Generic component ablation tables without a reusable evaluation methodology were excluded. Artifact access and licenses were not inferred from paper access; each row states the inspected status.

## Provenance

- Web/primary sources: ACL Anthology pages and PDFs for AbGen, ERASER, MuFaSSa, FUR, FACT-E, MoPS, Madaan et al., Meadows et al., and Goodhart’s Law.
- arXiv primary record: Interventional Grounding Audits (arXiv:2607.13069).
- Local retained evidence: `.hermes/lit_review/ranking/gap_search/dependency_compression/dependency_compression.csv`, `.hermes/lit_review/ranking/benchmark_review_ablation_intervention_notes.md`, `.hermes/lit_review/ranking/notes_downstream_reasoning_eval.md`.

The CSV was written with the repository protocol schema and reconciled programmatically: expected records = 14, actual records = 14, unique record IDs = 14.
