# Alternative valid parses, ambiguous argument structures, and disagreement-aware interpretation benchmark search

**Search date:** 2026-10-12

**Scope.** Searched scholarly benchmark and evaluation resources for: (1) alternative valid parses or graph structures, (2) ambiguity-aware logical/semantic interpretations, (3) multi-label entailment or other set-valued outputs, and (4) evaluation that preserves annotator disagreement instead of forcing a single majority gold. Argument mining was prioritized; semantic parsing, NLI, discourse parsing, and perspectivist annotation were retained as strong adjacent controls when they expose reusable mechanisms.

**Outcome.** Six records are retained in `gap_search_alternative_valid_parses.csv`.

## Strongest direct gap fills

1. **QT30nonaggr / Disagreement Space in Argument Analysis (Hautli-Janisz, Schad, and Reed, 2022).** The closest direct argument-mining resource. It preserves non-aggregated annotations as 134 argument graphs over 67 BBC Question Time excerpts, with 1,817 propositions and disagreement labels separating annotation errors, fuzziness, and ambiguity. The ambiguity categories cover alternative segmentation and relation decisions, so multiple graph readings remain inspectable.
2. **Parallel RST analyses disagreement dataset (Hewett and Stede, 2025).** A direct precedent for treating multiple analyses as legitimate alternatives. Each text receives two RST analyses; the paper enumerates disagreement types and distinguishes linguistic ambiguity from scheme/specification ambiguity. It is discourse rather than argument mining, but the set-valued parse design is directly reusable.
3. **AmbiEnt (Liu et al., 2023).** A benchmark for multiple valid NLI labels with label-specific disambiguating rewrites. It operationalizes ambiguity as interpretation-conditioned entailment and gives a concrete multilabel evaluation design that can be transferred to argument claims and relation judgments.

## Strong adjacent controls

- **UNIMER (Guo et al., 2020)** evaluates semantic equivalence across four meaning representations and reports execution-match in addition to exact-match. This is useful when two argument skeletons differ in surface formalism but preserve the same logical content.
- **Justified and informative disagreement (Sommerauer, Fokkens, and Vossen, 2020)** retains worker distributions and expert judgments to distinguish meaningful disagreement from annotation noise. It is not argument-specific, but it supplies a practical disagreement-quality evaluation pattern.
- **From Disagreement to Understanding (Jayaweera and Dorr, 2025)** is a framework/position paper rather than a released benchmark. It is retained as a design control because it makes ambiguity detection a separate stage before NLI inference and gives a taxonomy of ambiguity-related disagreement.

## Record-level notes

- **AVP-01 — Hewett and Stede.** ACL landing page and PDF were accessible. The retained evidence supports two parallel RST analyses and disagreement typology. A separate stable data-download URL was not confirmed; artifact access is therefore not inferred from paper access.
- **AVP-02 — QT30nonaggr.** ACL PDF evidence supports the corpus size, graph counts, proposition counts, and disagreement categories. The paper indicates open availability, but a current standalone artifact URL/license was not independently verified.
- **AVP-03 — AmbiEnt.** The official GitHub repository was located and retained. The paper/repository evidence supports 1,645 examples, multiple entailment labels, disambiguating rewrites, and multilabel evaluation. The dataset is NLI rather than argument mining, so it is classified `strong_adjacent`.
- **AVP-04 — SPT diagnostic annotation.** The official repository URL is given in the paper. The task preserves annotation distributions and evaluates justified disagreement, but the data are semantic-property judgments rather than argument structures.
- **AVP-05 — UNIMER.** The paper exposes four logical-form representations and exact/execution-match evaluation. This is a semantics-preserving equivalence control, not a human disagreement benchmark.
- **AVP-06 — Ambiguity-aware NLI framework.** The ACL paper is accessible, but no released dataset or repository artifact was verified. It is retained as a task-design resource only and marked `introduces_evaluation_task_or_metric_only` with medium confidence.

## Failed, blocked, or negative searches preserved

- Tried `web_extract` on ACL Anthology and arXiv URLs for candidate papers. The configured extraction backend rejected URL extraction (`OpenAI Native Web Search ... search-only backend ... extraction backend unavailable`), so no extracted-page evidence was used.
- Searched for a dedicated benchmark named around “alternative valid parses” and “argument interpretation disagreement.” No additional exact argument benchmark with a stable artifact and explicit set-valued gold was verified beyond QT30nonaggr and the parallel RST dataset.
- Searched for argument-mining datasets with majority-vote-free graph evaluation and explicit ambiguity labels. Results mostly described annotation studies or methods without a reusable benchmark artifact; these were excluded under the protocol’s requirement for inspectable benchmark evidence.
- Searched for multi-label logical-form argument benchmarks. The strongest verified hit was AmbiEnt (NLI) and UNIMER (semantic parsing); no direct argument-mining equivalent with multiple gold logical forms was confirmed.
- Searched for licenses separately from paper access. No license was inferred where the retained paper/repository evidence did not state one; those fields remain “Not stated” or “not verified.”

## Gap assessment

No retained resource directly evaluates a system against multiple human-valid **argument** parses while also preserving proposition-level disagreement and measuring downstream reasoning quality. QT30nonaggr is the closest argument benchmark; the parallel RST dataset provides the clearest alternative-parse evaluation pattern; AmbiEnt provides the clearest multi-label interpretation mechanism.

A new benchmark could combine these mechanisms: annotate pro/con debate excerpts with non-aggregated argument graphs; store ambiguity tags and label-specific rewrites; score against a set of valid graphs or interpretations; and report both exact/structural agreement and disagreement-aware soft or distributional metrics. Add an execution- or entailment-equivalence check inspired by UNIMER so semantically equivalent argument skeletons are not penalized solely for representation choice.

## Retained scholarly and artifact URLs

- https://aclanthology.org/2025.law-1.3/
- https://aclanthology.org/2022.nlperspectives-1.1/
- https://aclanthology.org/2023.emnlp-main.51/
- https://github.com/alisawuffles/ambient
- https://aclanthology.org/2020.coling-main.422/
- https://github.com/cltl/SPT_annotation
- https://aclanthology.org/2020.emnlp-main.118/
- https://taoxiease.github.io/publications/emnlp20-meaningrep.pdf
- https://aclanthology.org/2025.nlperspectives-1.4/
