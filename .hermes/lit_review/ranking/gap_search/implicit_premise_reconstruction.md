# Implicit-premise, enthymeme, and warrant reconstruction benchmarks

**Search scope/date:** Scholarly sources and primary artifacts available in the repository plus targeted ACL Anthology/arXiv discovery; checked October 12, 2026. The CSV preserves direct versus adjacent fit, artifact-access uncertainty, license uncertainty, and evidence basis rather than treating paper access as dataset access.

## Recommended benchmark battery

1. **ARCT / SemEval-2018 Task 12** — strongest established exact benchmark. It provides authentic debate/news-comment arguments, a premise/reason and claim, two plausible opposing warrants, binary labels, and a public repository with data and annotation exports. Use for contrastive warrant identification; add generation evaluation only with care because the official task is selection.
2. **Implicit Knowledge in Argumentative Texts / Microtexts extension** — strongest direct free-form bridge reconstruction resource. It contains human-written sentences inserted between argumentative units and semantic-clause/ConceptNet relation labels. Use for generation plus typed error analysis, pending artifact URL/license verification.
3. **Mind the Gap** — complementary learner-essay resource for enthymeme detection and reconstruction, including implicit premises and conclusions. Treat as a corpus-creation benchmark until the released artifact, split, and validation protocol are independently verified.
4. **Pastor & Oostdijk (2026)** — most direct recent candidate for joint enthymeme detection, implicit-premise/implicit-conclusion labeling, structural slot annotation, and reconstruction. It is a preprint; pin the version and verify the dataset/repository and social-media access constraints before operational use.
5. **6,000-warrant preliminary corpus** — scale and annotation-method comparator. Useful for studying warrant-quality collection and expert validation, but not yet a stable benchmark without artifact/split/license confirmation.
6. **Implicit reasoning causal-link annotations** — intermediate structured task. Use to evaluate bridge recovery before unconstrained natural-language warrant generation.

## Evidence and caveats

- The **ARCT** paper reports 1,970 high-quality warrant instances; its official repository documents train/dev/test files, correct-warrant labels, swapped training data, and broader annotation exports. Source: https://aclanthology.org/N18-1175/ and https://github.com/UKPLab/argument-reasoning-comprehension-task
- **Implicit Knowledge in Argumentative Texts** explicitly annotates inserted information between Microtexts argumentative units and adds semantic-clause and ConceptNet labels. Source: https://aclanthology.org/2020.lrec-1.282/
- **Implicit Premise Generation** is retained as a strong adjacent evaluation paper, not a new benchmark: it evaluates generation on three datasets and reports discourse-aware commonsense gains. Source: https://aclanthology.org/2021.emnlp-main.504/
- **Mind the Gap** targets learner-argument enthymeme detection/reconstruction and contrasts the setting with earlier warrant-only work. Source: https://aclanthology.org/2023.findings-emnlp.312/
- The **6,000-warrant** study reports 6,000 warrants over 600 claim-premise pairs and compares collection methodologies with expert quality assessment. Source: https://arxiv.org/abs/2104.07924
- **Pastor & Oostdijk (2026)** reports 1,482 annotated political tweets and a formal reconstruction setup covering implicit premises, implicit conclusions, and no-enthymeme cases. Source: https://arxiv.org/abs/2606.12186
- **Causal-link annotations** are included as an adjacent bridge-extraction resource; the retained evidence does not establish a separately accessible artifact, exact split, or license. Source: https://arxiv.org/abs/2110.13692

## Selection guidance

For a minimal reproducible suite, run **ARCT + Microtexts implicit-knowledge annotations + one reconstruction corpus** (Mind the Gap or the 2026 political-discourse resource). Report separate metrics for: (a) enthymeme detection, (b) premise versus conclusion role, (c) bridge/warrant selection, (d) free-form reconstruction, (e) structural/entailment validity, and (f) human agreement or acceptable-answer sets. Do not pool labels across resources without preserving task provenance and annotation granularity.

## Known gaps

No inspected resource simultaneously provides large-scale authentic arguments, multiple independently valid reconstructed premises, formal entailment checks, stable public artifacts, and a common evaluation protocol. ARCT is strongest for contrastive warrant choice; Microtexts and newer enthymeme resources are stronger for free-form reconstruction but have smaller or less independently verified artifacts.
