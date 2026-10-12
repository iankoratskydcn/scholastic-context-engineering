# Gap search: argument-form-conditioned context selection/compression

**Search date:** 2026-10-12 (US/Eastern)

## Scope and conclusion

This search targeted benchmarks or reusable evaluation resources that combine (1) argument-form, argumentation-scheme, or structured reasoning classification with (2) context retrieval, selection, compression, or proof-relevant context construction.

**Result:** one close scheme-conditioned context precedent was verified: Trajano et al. (COMMA 2024) classifies natural-language arguments by scheme and supplies scheme-relevant descriptions/examples to an LLM through retrieval-augmented context for translation into computational arguments. Its paper identity and mechanism are verified, but a separately released benchmark artifact could not be confirmed from the inspected evidence, so its `benchmark_status` is `uncertain` rather than `introduces_benchmark`.

No benchmark was verified that evaluates the full target combination as a reusable task: predicted argument form -> adaptive retrieval/selection or compression -> proof/dependency-preserving compact context -> downstream reasoning quality. The remaining records are component controls or strong adjacent precedents.

## Records retained

- **FCS01 — Trajano et al. (2024), “Translating Natural Language Arguments to Computational Arguments Using LLMs.”** Closest direct hit. Scheme classification conditions context/examples for an LLM translation pipeline; the inspected local evidence also records RAG, short-versus-larger context, and wrong-scheme retrieval concerns. Artifact/benchmark release status remains uncertain.
- **FCS02 — Explanation-Refiner (Quan et al., 2024).** Strong proof-context precedent: selects relevant, redundant, unrelated, sufficient, and necessary facts, formalizes selected facts, and checks them with Isabelle/HOL. It lacks argument-form classification.
- **FCS03 — FRVA (Fan et al., 2024).** Filters irrelevant facts before entailment-tree generation and verification. It evaluates proof-relevant selection but starts with fact/entailment data rather than mined argument forms.
- **FCS04 — QT-SCHEMES (Ruiz-Dolz et al., 2025).** Current fine-grained dialogue argument-scheme benchmark with 24 labels. It supplies the form-classification side only; no selector/compressor or downstream proof-context task.
- **FCS05 — EthiX (Bezou-Vrakatseli et al., 2024).** Human-authored ethical-debate scheme dataset with eight Walton-based classes. It is a naturalistic form-label control, not a context-selection benchmark.
- **FCS06 — RECOMP (Xu et al., 2024).** Selective extractive/abstractive retrieval-context compression with empty-context decisions. It is a generic compression control with no argument-form representation.
- **FCS07 — LLMLingua-2 (Pan et al., 2024).** Token keep/drop compression and faithfulness evaluation across multiple tasks. It is a generic compression control and does not preserve argument roles or proof dependencies.
- **FCS08 — LeanDojo/ReProver (Yang et al., 2023).** Mature proof-relevant premise-selection benchmark and codebase. It supplies the downstream retrieval/proving control, but its representations are formal proof states rather than natural-language argument forms.

## Recommended benchmark construction from the gap

A new combined benchmark should cross the form resources (QT-SCHEMES/EthiX or a broader multi-form corpus) with a selector/compressor intervention and a structured downstream target. Minimum fields should include:

1. source argument/document and provenance;
2. gold form/scheme label plus confidence or ambiguity;
3. candidate context units with argument roles and dependency links;
4. gold sufficient/necessary or proof-relevant subset where available;
5. selection/compression budget and retained-context faithfulness;
6. downstream structured reasoning/proof score; and
7. ablations for flat semantic retrieval, generic compression, and form-conditioned selection.

The key novelty boundary is therefore not argument-form classification or compression alone, but an inspectable evaluation of whether form labels improve retrieval precision, dependency recall, compact-context faithfulness, and downstream reasoning.

## Search coverage and failed/blocked searches

Scholar-oriented and exact-title searches were attempted for:

- `argument scheme classification context selection`
- `argument scheme classification retrieval ranking`
- `argument mining proof relevant retrieval`
- `argument structure context compression LLM`
- `premise selection argument mining LLM`
- `scheme-conditioned retrieval benchmark`
- `argument form prompt compression`

Google Scholar result pages were not reliably fetchable in the environment; Scholar-style queries were used for discovery only. Claims were retained only when a primary/official scholarly page, PDF, ACL Anthology record, arXiv record, DOI/publisher record, or official artifact page was available in the local corpus or source manifest.

The configured `web_extract` route was also unavailable for the searched URLs because its backend reported: “OpenAI Native Web Search (Codex Responses) is a search-only backend and cannot extract URL content.” This did not block the search because the repository already contained checked ACL/arXiv/publisher evidence and retained summaries for the included records.

No exact hit was retained when it only described generic argument mining, generic long-context compression, or scheme classification without an inspectable selection/compression or downstream reasoning task. Such near misses were preserved as controls only where they materially support benchmark design.

## Provenance

Primary/local evidence used:

- `.hermes/lit_review/agents/10_walton_schemes_nlp.md`
- `.hermes/lit_review/summaries/09_argument_mining_summaries.md`
- `.hermes/lit_review/agents/08_logic_theorem_provers.md`
- `.hermes/lit_review/agents/14_premise_context_selection.md`
- `.hermes/lit_review/summaries/04_context_compression_summaries.md`
- `.hermes/lit_review/summaries/08_logic_theorem_provers_summaries.md`
- `.hermes/lit_review/corpus_index_interim.md`

The machine-readable records are in `gap_search_form_conditioned_selection.csv` in this directory. Counts were reconciled programmatically after writing.
