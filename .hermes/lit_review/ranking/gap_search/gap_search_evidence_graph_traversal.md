# Recursive evidence-chain and claim-evidence graph traversal benchmark search

**Slug:** `evidence_graph_traversal`  
**Search date:** 2026-10-12  
**Scope:** scholarly benchmarks and reusable evaluation resources for recursive evidence chains, explicit claim-evidence graphs, bedrock/source dependency tracking, intermediate-claim construction, and evidence traversal across heterogeneous or scholarly sources.

## Result

- **Records:** 19
- **Direct gap fills:** 13
- **Strong adjacent controls:** 6
- **Artifact URLs verified:** 5
- **Main finding:** No single established benchmark before the 2026 preprint was found that jointly provides authentic scholarly claims, recursively linked intermediate claims, source-level provenance, support/refutation or disagreement, and graph-traversal evaluation. The strongest compositional stack is HiEviDR-Bench (newest end-to-end graph formulation), CLAIM-BENCH, SciCiteVal, and MEVER/AIChartClaim (full-paper scholarly claim→evidence links), EntailmentBank/ProofWriter (explicit recursive support structure), HoVer/EX-FEVER/FEVEROUS (multi-hop retrieval and evidence completeness), SciFact/SciFact-Open/AVeriTeC (scientific or real-world grounding), and WiCE/SciClaimEval (minimal or cross-modal evidence sufficiency).

## Recommended benchmark stack

1. **HiEviDR-Bench** — closest direct end-to-end hierarchical evidence graph and intermediate-claim benchmark; treat as provisional until artifact and license are verified.
2. **CLAIM-BENCH** — primary scholarly-text claim/evidence extraction and link-validation layer.
3. **EntailmentBank + ProofWriter** — recursive bedrock-to-conclusion dependency controls with explicit trees/proofs and depth.
4. **HoVer + EX-FEVER** — multi-hop distributed-evidence chain retrieval and explanation paths.
5. **FEVEROUS + UnifEE + Papelo** — heterogeneous text/table graph traversal, evidence interaction, and iterative next-hop pursuit.
6. **SciFact + SciFact-Open + AVeriTeC** — scientific and open-world evidence grounding, including refutation and evidence sufficiency.
7. **WiCE + SciClaimEval** — subclaim/minimal-evidence and cross-modal evidence diagnostics.
8. **SciVer + MEVER/AIChartClaim + MuSciClaims** — large-scale multimodal scientific claim/evidence retrieval and verification.
9. **SciCiteVal** — cross-document citation-to-source edge correctness and fine-grained citation failure taxonomy.

## Gap assessment

The resources divide into four non-equivalent families:

- **Recursive proof structure:** EntailmentBank and ProofWriter expose intermediate deductions and proof depth, but are textbook/synthetic rather than source-attributed scholarly graphs.
- **Multi-hop fact verification:** HoVer, EX-FEVER, and FEVEROUS expose distributed evidence and evidence-set completeness, but use Wikipedia and generally lack claim ownership or explicit intermediate-claim annotations.
- **Claim-evidence grounding:** SciFact, SciFact-Open, CLAIM-BENCH, WiCE, and SciClaimEval provide scientific or fine-grained claim/evidence links, but mostly stop at one evidence layer or lack recursive traversal.
- **Hierarchical deep-research graphs:** HiEviDR-Bench explicitly models evidence selection, cross-source linking, aggregation to intermediate claims, and final conclusions; it is the closest match but is a very recent preprint with artifact details still unverified.
- **Multimodal scholarly evidence graphs:** SciVer, SciClaimEval, MEVER/AIChartClaim, and MuSciClaims test evidence retrieval/verification over figures and tables; SciCiteVal tests whether a citation edge is actually supported by full-text evidence.

A defensible evaluation should report separate scores for: (a) node/span recovery, (b) edge/link precision and recall, (c) bedrock/source dependency completeness, (d) hop/depth success, (e) intermediate-claim validity, (f) support/refutation/NEI correctness, and (g) final answer correctness. Final-answer accuracy alone is insufficient because it can hide a missing or spurious dependency edge.

## Search and verification notes

Searches covered ACL Anthology, arXiv, official dataset/repository pages, and retained local literature-review evidence. Query families included `multi-hop evidence chain benchmark`, `claim evidence graph`, `entailment tree`, `scientific claim evidence`, `hierarchical evidence aggregation`, `next-hop evidence pursuit`, and `cross-modal claim verification`. Paper identity and task descriptions were verified from scholarly pages or papers; artifact access and licensing were kept separate and marked unverified when not directly checked.

## Limitations and negative results

- No located benchmark simultaneously annotates source/claim ownership, support/attack/disagreement, recursive multi-hop evidence, and expert scholarly provenance.
- Wikipedia fact-verification benchmarks are strong traversal controls but are not substitutes for scholarly source dependency tracking.
- SciFact-family resources provide valuable scientific grounding but generally do not encode recursive claim-to-claim support.
- HiEviDR-Bench is highly relevant but requires artifact, license, and annotation-schema verification before treating it as a stable dependency.
- SciVer, MEVER/AIChartClaim, SciClaimEval, MuSciClaims, and SciCiteVal are strong 2025–2026 additions for multimodal or cross-document scholarly grounding, but their publicly verified artifact access remains incomplete in this pass.
- Method papers evaluated on an existing benchmark are retained only when they expose a reusable traversal protocol or diagnostic signal; they are marked `evaluates_existing_benchmark_only`.

## Primary source URLs

- HoVer: https://aclanthology.org/2020.findings-emnlp.309/
- EX-FEVER: https://aclanthology.org/2024.findings-acl.556/
- FEVEROUS: https://aclanthology.org/2021.fever-1.1/
- UnifEE: https://aclanthology.org/2023.eacl-main.82/
- EntailmentBank: https://aclanthology.org/2021.emnlp-main.585/
- ProofWriter: https://aclanthology.org/2021.findings-acl.317/
- CLAIM-BENCH: https://aclanthology.org/2025.ijcnlp-long.127/
- SciFact: https://aclanthology.org/2020.emnlp-main.609/
- SciFact-Open: https://aclanthology.org/2022.findings-emnlp.347/
- AVeriTeC: https://arxiv.org/abs/2305.13117
- WiCE: https://aclanthology.org/2023.emnlp-main.470/
- SciClaimEval: https://aclanthology.org/2026.lrec-1.864/
- HiEviDR-Bench: https://arxiv.org/abs/2607.25151
- SciVer: https://aclanthology.org/2025.acl-long.420/
- MEVER: https://aclanthology.org/2026.eacl-long.242/
- SciCiteVal: https://aclanthology.org/2026.lrec-1.125/
- MuSciClaims: https://aclanthology.org/2025.ijcnlp-long.175/
- Papelo: https://aclanthology.org/2021.fever-1.5/
