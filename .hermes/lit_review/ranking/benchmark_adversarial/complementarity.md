# Adversarial benchmark complementarity review

## Scope and method

Reviewed all **80 benchmark-study rows** in `benchmark_master_matrix.csv` and the selection rules in `benchmark_ranking_protocol.md`. The matrix contains 26 scored perspectives; this review treats `paper_id` and citation as immutable identities and does not merge source records. Duplicate benchmark resources are flagged as duplicate/version families rather than silently collapsed.

The goal was not to choose the seven highest aggregate scores. It was to choose the smallest set that exposes **distinct failure modes** in the target pipeline:

> source text → claims/evidence → argument form → proof/dialectical skeleton → dependency-aware context selection/compression → inspectable reasoning.

Scores below are copied from the matrix and used as evidence, not as a substitute for artifact-access or license verification.

## Minimal complementary battery

| Role | Canonical record | Why it earns a core slot | Main failure exposed |
|---|---|---|---|
| Form/skeleton extraction | `S09P08` — QT-SCHEMES | Highest direct form and argument-mining signal: 24 annotated schemes in dialogue; `argument_form_diagnosticity=98`, `argument_mining_coverage=98`, `battery_complementarity=98`. | Incorrect component boundaries, scheme labels, warrants, and compact argument skeletons. |
| Context stress | `S03P10` — LongPiBench | Tests multiple relevant information pieces separated by distance; `long_context=99`, `diagnosticity=94`, `ablation_intervention=98`. This is more diagnostic for dependency-preserving selection than a generic long-context score. | Lost, displaced, or incompletely retained dependencies under context distance/position changes. |
| Hallucination / invalid inference | `S02P07` — PCBench | Maximum matrix hallucination score (`100`) and `diagnosticity=95`; directly targets premise critique and multiple premise-error types. | Accepting false, defective, or unsupported premises; invalid inference hidden by fluent answers. |
| Grounding / provenance | `S05P05` — ALCE | Maximum grounding and provenance-auditability scores (`98`/`98`); requires support retrieval plus citation-bearing generation. | Unsupported claims, missing source links, citation mismatch, and loss of traceability. |
| Formal proof compatibility | `14-08` — LeanDojo/ReProver | Maximum premise-selection score (`100`), high formal score (`96`), and explicit retrieval-augmented theorem proving. | Whether selected context is formally sufficient, executable, and dependency-preserving at a prover boundary. |
| Authentic scholarly text | `S22P04` — Index Thomisticus Treebank | Maximum scholarly-text fit (`100`), high authenticity (`96`) and cross-tradition score (`93`); real Medieval Latin/Aquinas material prevents an all-synthetic battery. | Failure to parse, preserve, or reason over authentic scholastic language and structure. |
| Dialectical reasoning | `S23P12` — 741-topic argument-tree corpus | Strong tree-level dialectical coverage (`dialectical_argumentation=92`, `argument_form_diagnosticity=89`) over manually curated complex arguments. | Stance, support/attack structure, specificity, and multi-level dialectical relation errors. |

### Why seven is minimal

Each selected row owns a failure mode not adequately owned by another selected row:

1. QT-SCHEMES tests **local argumentative form**.
2. LongPiBench tests **distributed context placement**.
3. PCBench tests **premise validity**.
4. ALCE tests **source attribution**.
5. LeanDojo tests **formal executability and dependency sufficiency**.
6. Index Thomisticus tests **authentic scholarly-language transfer**.
7. The argument-tree corpus tests **dialectical graph structure**.

Removing any row leaves one named mode without a direct primary diagnostic. Some rows have secondary coverage, but that secondary coverage is not enough to justify collapsing the slots: for example, LeanDojo has provenance-like premise annotations but does not replace citation-level grounding; QT-SCHEMES has dialectical schemes but does not replace tree-level stance/support evaluation.

## Duplicate and version findings

### Exact or perspective duplicates

- **ProofWriter:** `S07P01` and `12-04` refer to the same ProofWriter benchmark family. Do not count them as two independent tests. If a synthetic proof control is desired, retain one canonical record only.
- **LeanDojo:** `S07P08`, `S08P04`, and `14-08` are perspective/category records for the same underlying LeanDojo resource. The core battery uses `14-08` because it is the most specific to LeanDojo/ReProver premise selection.
- **QT-SCHEMES:** `S09P08` and `S25P13` are duplicate records for the same benchmark/citation. The core battery uses `S09P08`, which has the stronger matrix complementarity/diagnosticity profile.

### Version or family redundancy

- **MISSCI → MISSCI PLUS:** `11-06` and `11-08` are a version family, not independent failure modes. MISSCI PLUS is the stronger grounding/fact-checking option, but ALCE is retained in the minimal core because it adds citation-generation/provenance behavior rather than another fallacy-reconstruction test. MISSCI PLUS is the preferred optional scholarly-grounding extension.
- **Long-context family:** LRA, LongBench, ∞Bench, RULER, NoLiMa, and LongPiBench largely compete for one context-stress slot. LongPiBench is selected because separated relevant pieces and distance-dependent bias most directly threaten dependency-preserving context selection. RULER is a broad optional regression suite; NoLiMa is an optional low-overlap semantic-retrieval control.
- **Walton/scheme family:** US2016G1tvWALTON, EthiX, and the annotated/generated Walton sets overlap heavily with QT-SCHEMES on scheme extraction. They are useful for cross-corpus robustness, not for the minimal battery.
- **Formal proof family:** ProofWriter, LeanDojo, and Isabelle/Magnushammer are complementary at the ecosystem level but redundant for a seven-slot battery's single formal-compatibility slot. LeanDojo is preferred because it combines a real prover boundary with retrieval and premise annotations. ProofWriter remains the best low-cost synthetic sanity control.

## Recommended execution design

Use each core benchmark in paired conditions where the artifact permits it:

1. **Raw context:** original supplied input and evidence.
2. **Selected context:** system-selected claims/spans with provenance links.
3. **Compressed context:** system compression under a fixed token budget.
4. **Distractor context:** irrelevant or adversarially positioned material.
5. **Ablated context:** remove one proof/evidence dependency at a time.

Record separate metrics rather than one pooled score:

- span/component F1 and scheme/skeleton exactness;
- dependency retention and answer degradation after removal;
- premise-critique accuracy and invalid-inference rate;
- citation precision/recall and source-span attribution;
- prover acceptance and proof-relevant premise recall;
- scholarly-text parsing/structure retention by genre/tradition;
- stance/support/attack and tree-relation accuracy.

A benchmark should be marked **not comparable** when its native task does not expose the requested intermediate artifact. In particular, do not infer provenance quality from final answer accuracy, or proof compatibility from a text-only logical label.

## Non-core alternates

- **FOLIO (`12-06`)** is the strongest aggregate candidate (`aggregate_mean=86.64`, `battery_complementarity=97`) and should be the first fallback if LeanDojo cannot be executed. It is also a strong human-authored logical-form control.
- **ProofWriter (`S07P01` or `12-04`, one only)** is the preferred inexpensive synthetic proof/abduction control.
- **MISSCI PLUS (`11-08`)** is the preferred optional extension when grounding must use real scientific passages and fact-checking rather than citation generation.
- **FalseQA (`S02P05`)** is a human-written premise-critique transfer check for PCBench.
- **RULER (`S03P08`)** is a broad context-capacity regression suite after LongPiBench, not a second core context test.
- **US2016G1tvWALTON (`S10P07`)** is the best alternate if QT-SCHEMES access or annotation format is unavailable.

## Evidence and limitations

- This was a local artifact review only; no external web search, download, license check, or benchmark execution was performed.
- The review relies on the retained benchmark evidence and matrix scores. The protocol's final verification gate still requires exact paper/artifact identity and access verification before production use.
- `Index Thomisticus Treebank` is deliberately included for authenticity, but its native task is linguistic annotation/parsing. It is a transfer gate, not a complete reasoning benchmark.
- The battery is minimal for **failure-mode coverage**, not for statistical power. Each slot may later need multiple seeds, held-out splits, or an alternate corpus once the harness is stable.

## Files

- `complementarity.csv` — machine-readable selected battery, duplicate/version groups, and non-core alternates.
- `complementarity.md` — this report.

The source matrix was not edited.
