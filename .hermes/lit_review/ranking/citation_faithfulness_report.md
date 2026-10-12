# Citation-faithfulness benchmark sweep

- **Slug:** `citation_faithfulness`
- **Search scope:** scholarly benchmark and evaluation papers for generated-text attribution, citation support, claim/source alignment, and unsupported-claim detection.
- **Source policy:** primary ACL Anthology and arXiv landing pages; every URL in the CSV was HTTP-verified on 2026-10-12.
- **Records:** 12.

## Recommended core battery

1. **CiteEval/CiteBench (2025)** — strongest direct fit. It evaluates citation quality in the full context: user query, retrieval context, generated text, preceding statements, parametric knowledge, and cited sources. This is the best match for claim-to-source alignment after generation.
2. **ALCE (2023)** — end-to-end retrieval plus cited answer generation, with citation correctness/completeness-style signals. Use as the standard cited-answer generation baseline.
3. **Fine-grained citation evaluation framework (2024)** — evaluates statement/citation support with full, partial, and no-support distinctions. Use when binary entailment is too coarse.
4. **AIS (2023)** — statement-level attribution evaluation against cited reference passages. Use as a compact attribution classifier/evaluator.
5. **RAGTruth (2024)** — word/span-level unsupported or contradictory-content annotations for generated RAG responses. Use for unsupported-claim detection even when the system does not emit citations.
6. **VeriScore (2024)** — extracts atomic verifiable claims and checks evidence support in long-form generation. Use for claim-level factuality audits; it is less about citation selection.
7. **MultiHop-RAG (2024)** — evaluates multi-document support chains. Use to stress whether a generated answer preserves all evidence dependencies rather than citing only one supporting document.

## Secondary and protocol resources

- **FaithJudge (2025):** broad RAG faithfulness leaderboard/proxy; useful for model comparison, but citation attribution is not the central annotation.
- **LongEval (2023):** clause-level human faithfulness protocol for long-form summaries; useful for annotation design and long-answer audits.
- **FEQA (2020):** foundational source-document support evaluation for abstractive summaries; useful historical baseline, not citation-aware.
- **CiteBench (2023):** source-conditioned scientific citation-text generation; relevant to citation generation, but not a pure citation-faithfulness benchmark.
- **CiteAudit (2026 preprint):** direct scientific claim-to-reference verification; promising for scientific writing, but too new to treat as an established standard.

## Coverage map

| Benchmark | Generated output | Claim/span labels | Explicit citations | Source passages | Unsupported detection | Multi-hop | Scientific-domain fit |
|---|---:|---:|---:|---:|---:|---:|---:|
| CiteEval/CiteBench | yes | yes | yes | yes | yes | partial | broad |
| ALCE | yes | partial | yes | yes | partial | partial | no |
| Fine-grained citation evaluation | yes | yes | yes | yes | yes | no | no |
| AIS | yes | yes | yes | yes | yes | no | no |
| RAGTruth | yes | yes | no | yes | yes | partial | no |
| VeriScore | yes | yes | no | retrieved evidence | yes | no | partial |
| MultiHop-RAG | yes | answer/evidence set | no | yes | indirect | yes | no |
| FaithJudge | yes | yes | no | yes | yes | partial | no |
| LongEval | yes | clause | no | yes | yes | no | no |
| FEQA | yes | claim via QA | no | yes | yes | no | no |
| CiteBench | yes | citation text | indirect | cited papers | indirect | no | yes |
| CiteAudit | yes | yes | yes | cited papers | yes | partial | yes |

## Evaluation recommendation

For a citation-faithfulness experiment, report at least four separate dimensions rather than one aggregate score:

- **Citation correctness/support:** does the cited source entail the generated claim?
- **Citation completeness:** are all material claims covered by at least one citation?
- **Citation appropriateness:** was the cited source the right source in the full retrieval/query context?
- **Unsupported or contradictory span rate:** what portion of the generated text is not supported by the available evidence?

A practical battery is **CiteEval/CiteBench + ALCE + RAGTruth + VeriScore**, with **MultiHop-RAG** added when claims depend on multiple sources. Use **LongEval** or the fine-grained citation framework for human annotation guidelines and partial-support adjudication.

## Evidence links

The CSV preserves the primary source URL for each record. The strongest direct sources are:

- CiteEval/CiteBench: https://aclanthology.org/2025.acl-long.1574/
- ALCE: https://aclanthology.org/2023.emnlp-main.398/
- Fine-grained citation evaluation: https://aclanthology.org/2024.inlg-main.35/
- AIS: https://aclanthology.org/2023.findings-emnlp.307/
- RAGTruth: https://aclanthology.org/2024.acl-long.585/
- VeriScore: https://aclanthology.org/2024.findings-emnlp.552/
- MultiHop-RAG: https://arxiv.org/abs/2401.15391
