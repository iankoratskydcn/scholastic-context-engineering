# Gap search report: scholastic or structured philosophical disputation output evaluation

## Scope and conclusion

Search date: **October 12, 2026 (US/Eastern)**. The target was a benchmark that evaluates a **complete** scholastic or structured philosophical disputation output: question/quaestio, objections, contrary authority or *sed contra*, determination/*respondeo*, distinctions, and objection-specific replies, ideally with citation/faithfulness and structure metrics.

**Conclusion:** No inspected scholarly benchmark evaluates that full typed sequence end-to-end. The strongest resources are complementary rather than complete: LMCA scores conceptual critiques; DebateQA scores perspective coverage and dispute awareness; NoDE/QuAD evaluates non-linear argument acceptability; SocREval evaluates reasoning chains; QT-SCHEMES and Walton-scheme work score argument form; RESEARCHQA scores rubric-item coverage in scholarly answers; and PhilosophyBench is a promising but not yet frozen live study. The gap therefore remains a genuine **integrated-output benchmark gap**, not a lack of adjacent evaluation technology.

## Records

- **Total records:** 14
- **Direct gap fills:** 0
- **Strong adjacent:** 11
- **Control only:** 1
- **False positives / deduplication or protocol-only records:** 2
- **Uncertain watch items:** 0

The CSV preserves the required schema from `gap_benchmark_search_protocol.md`. The false-positive records are retained because the search specifically surfaced formal disputation protocols and duplicate URL families; dropping them would hide the evidence boundary.

## Best candidates for a future complete-output battery

1. **LMCA** — adapt its expert dimensions (centrality, strength, correctness, clarity, single-issue focus, overall) to objection quality and reply adequacy. Pin the dataset version before use because the arXiv abstract and current project page report different corpus totals.
2. **DebateQA** — use Perspective Diversity and Dispute Awareness as answer-level outer-loop metrics, but add typed stage and reply-alignment scoring.
3. **NoDE/QuAD evaluation** — apply graph-level acceptability and attack/support consistency to the extracted disputation graph; do not treat QuAD as philosophical truth.
4. **QT-SCHEMES + Walton scheme evaluation** — provide upstream form labels for objections, distinctions, and replies, with macro-F1 and held-out cross-domain tests.
5. **SocREval** — adapt Socratic evaluator prompts to interrogate each required stage, then validate against independent expert judgments rather than relying on LLM-judge agreement alone.
6. **RESEARCHQA** — borrow rubric-item coverage and citation/limitation/comparison checks for complete rendered answers.
7. **Marji & Licato** — borrow human evaluation of arguments for/against a disputed interpretation and machine-vs-human quality controls.

## Minimum missing benchmark design

A complete benchmark should provide frozen questions and source packets; gold or adjudicated labels for objection relevance/strength, *sed contra* source identity and quotation fidelity, distinction correctness, determination/question fit, one-to-one reply coverage, and citation entailment; plus graph/protocol validity checks. Report stage completion, typed-role F1, reply alignment, citation precision/recall, source/span faithfulness, contradiction/consistency, expert rubric scores, judge reliability, and budget-matched ablations against single completion, CoT, self-consistency, generic debate, and retrieval-augmented debate.

## Search log and failures preserved

### Queries/routes used

- `AI philosopher large language model philosophical arguments`
- `machine generated philosophical arguments LLM debate`
- `LLM objection rebuttal structured reasoning debate`
- `argument scheme classification LLM dialogue 2025`
- `philosophical reasoning benchmark language models dataset`
- `structured philosophical benchmark LLM`
- Official scholarly sources searched: ACL Anthology, arXiv, Springer, SAGE/IOS, OpenReview, and official project pages.

### Retrieval failures / boundaries

- `functions.web_extract` was attempted on ACL, arXiv, and OpenReview URLs but failed because the configured OpenAI-native backend is search-only and has no extraction backend. The search was rerouted to `web.run` official scholarly pages/PDF search results and the repository's already-retained opened source artifacts.
- Search-result snippets were not treated as sole evidence for retained scholarly findings. Rows cite official ACL/arXiv/SAGE/Stanford pages and, where appropriate, local retained review artifacts such as `agents/23_disputatio_dialectical_ai.md`.
- Artifact access and license are marked **not independently verified** whenever the paper page or abstract did not explicitly establish them. Paper access is never treated as proof of dataset access.
- No public, frozen, end-to-end benchmark with all named scholastic stages was found in the inspected corpus. This is a bounded negative result, not a proof of nonexistence.

## Source URLs consulted

- https://arxiv.org/abs/2607.27499
- https://www.andrew.cmu.edu/user/coesterh/LMCA_dataset.pdf
- https://aclanthology.org/2026.findings-eacl.44/
- https://aclanthology.org/2025.findings-emnlp.1159/
- https://aclanthology.org/2024.findings-naacl.175/
- https://arxiv.org/abs/2406.02106
- https://aclanthology.org/2025.acl-long.368/
- https://aclanthology.org/2025.findings-acl.702/
- https://aclanthology.org/2023.eacl-main.12/
- https://journals.sagepub.com/doi/10.3233/AAC-230014
- https://aclanthology.org/2026.tacl-1.62/
- https://aclanthology.org/2026.acl-long.835/
- https://link.springer.com/article/10.1007/s10503-012-9266-7
- https://philosophybench.org/

## Integrity checks

- CSV row count reconciled programmatically: 14 data rows.
- Required CSV columns present: yes.
- Duplicate record IDs: none.
- No production code or repository source files modified; only the requested gap-search artifacts were created.
