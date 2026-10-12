# Premise equivalence and cross-source claim matching

## Result

The retained 80-study benchmark inventory contains no purpose-built benchmark whose primary task is pairwise matching of claims that can be resolved by the same fact-check or premise. The strongest retained proxies are PCBench, MISSCI PLUS, RAGTruth, ALCE, LogicNLI, FOLIO, FalseQA, and ProofWriter; they cover premise critique, source grounding, entailment/contradiction, and proof traces but not the full cross-source equivalence decision.

The recommended common-ground battery should therefore combine a direct claim-matching resource with proposition-level NLI and source-grounding diagnostics. Treat semantic similarity alone as insufficient: matching claims may have low surface similarity, while high lexical overlap can conceal polarity, quantifier, temporal, or entity changes.

## External benchmarks found

| Benchmark/resource | What it tests | Fit for common ground | Main caveat | Scholarly source |
|---|---|---|---|---|
| Claim Matching Beyond English (Kazemi et al., ACL 2021) | Whether two textual messages containing claims can be served by one fact-check; multilingual WhatsApp tipline/public-group messages paired with fact-checked claims | **Direct** cross-source claim matching; best starting point for “same premise” clustering | Fact-check serviceability is broader than strict truth-conditional equivalence; social-media domain | https://aclanthology.org/2021.acl-long.347/ |
| MultiClaim (Shaar et al., 2023) | Multilingual previously fact-checked claim retrieval | **Direct/near-direct** retrieval of paraphrased or reformulated claims across languages | Retrieval relevance is not an explicit equivalence label; inspect split and cluster construction | https://arxiv.org/abs/2305.07991 |
| SciFact (Wadden et al., EMNLP 2020) | Select scientific abstracts that support/refute a claim and identify rationale sentences | **Direct for scholarly common ground**; source selection plus support/refute and rationale spans | Claim-to-evidence verification, not claim-pair matching; scientific abstracts only | https://aclanthology.org/2020.emnlp-main.609/ |
| AVeriTeC (Schlichtkrull et al., NeurIPS 2023) | Real-world claim verification using web evidence and structured evidence annotations | **Direct for web-scale source alignment** and evidence provenance | Verdict/evidence task rather than premise identity; web snapshot and licensing details matter | https://proceedings.neurips.cc/paper_files/paper/2023/hash/cd86a30526cd1aff61d6f89f107634e4-Abstract.html |
| FEVER (Thorne et al., NAACL 2018) | SUPPORTS/REFUTES/NOT ENOUGH INFO with Wikipedia evidence retrieval | Strong baseline for evidence selection and polarity checks | Claims are largely constructed from Wikipedia sentences; limited paraphrase diversity | https://aclanthology.org/N18-1074/ |
| VitaminC (Schuster et al., NAACL 2021) | Contrastive fact verification over changed Wikipedia revisions | **High diagnostic value** for minimal edits, negation, and subtle premise changes | Revision-based Wikipedia setting; not independent scholarly sources | https://aclanthology.org/2021.naacl-main.52/ |
| SciNLI (Sadat & Caragea, ACL 2022) | Entailment, contradiction, and neutral relations in scientific text | **High proposition-level calibration** for scholarly paraphrase and polarity | NLI pairs are not necessarily cross-source claims or evidence chains | https://aclanthology.org/2022.acl-long.511/ |
| PAWS / PAWS-X (Zhang et al., NAACL/EMNLP 2019) | Adversarial paraphrase identification with high lexical-overlap non-paraphrases; PAWS-X adds cross-lingual coverage | **High adversarial control** for false matches and multilingual paraphrase | Sentence paraphrase, not factual/source-grounded claim equivalence | https://aclanthology.org/N19-1131/ |
| STS Benchmark (SemEval 2017 Task 1) | Graded semantic similarity for sentence pairs | Useful weak baseline and retrieval prefilter | Similarity is not entailment; cannot decide contradiction or changed quantification | https://aclanthology.org/S17-2001/ |
| MultiNLI (Williams et al., ACL 2018) | Broad-genre entailment, contradiction, and neutral classification | Robust general NLI calibration and genre transfer | Premise/hypothesis relation is not the same as same-source claim matching | https://aclanthology.org/N18-1101/ |

## Recommended evaluation stack

1. **Candidate generation:** STS-B or a dense retriever, measured by Recall@k against claim clusters.
2. **Equivalence decision:** Claim Matching Beyond English and MultiClaim, scored with pair F1/AUROC and cluster purity; include hard negatives with changed polarity, entity, time, quantity, and modality.
3. **Scholarly grounding:** SciFact and SciNLI, scored for evidence retrieval, rationale span F1, and entailment/contradiction/neutral accuracy.
4. **Adversarial robustness:** VitaminC and PAWS/PAWS-X for minimal edits and lexical-overlap traps.
5. **Web provenance:** AVeriTeC and FEVER for source selection, citation support, and auditable evidence chains.

## Scope and limitations

The two CSVs rank the existing 80 benchmark studies from `benchmark_studies.csv`; they do not silently add external resources to the immutable inventory. External resources above were separately searched and recorded because the retained inventory lacks a direct claim-matching benchmark. Scores are suitability scores for this narrow viewpoint, not overall benchmark quality.

## Sources consulted

- ACL Anthology records for SciFact, Claim Matching Beyond English, VitaminC, SciNLI, PAWS, and MultiNLI.
- NeurIPS proceedings record for AVeriTeC.
- arXiv record for MultiClaim.
- SemEval 2017 Task 1 record for STS Benchmark.
