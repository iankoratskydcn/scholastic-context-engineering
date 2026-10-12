# Attribution-aware recursive grounding benchmark search

**Slug:** `attribution_recursive_grounding`  
**Search date:** 2026-10-12  
**Scope:** scholarly benchmark-producing studies and reusable evaluation resources for reported speech, claim ownership, source attribution, disagreement, recursive evidence chains, bedrock claims, and claim-to-source traversal.

## Result

- **Records:** 12
- **Direct gap fills:** 5
- **Strong adjacent controls:** 7
- **Artifact URLs verified:** 3
- **Main finding:** no single located benchmark jointly annotates claim ownership/epistemic attribution, disagreement, and multi-hop recursive evidence chains. The best coverage is compositional: FactAppeal/quote-attribution resources for ownership, HoVer/EX-FEVER for recursive chains, WiCE/FEVEROUS/AVeriTeC for evidence sufficiency, and CLAIM-BENCH for scholarly claim→evidence links.

## Recommended benchmark stack

1. **FactAppeal** — direct attribution-aware anchor: source spans, source type, role/credentials, and direct/indirect quotation.
2. **HoVer + EX-FEVER** — recursive chain and explanation-path stress tests.
3. **WiCE** — minimal evidence and subclaim-level sufficiency.
4. **AVeriTeC** — real-world open-web evidence quality and verdict coupling.
5. **CLAIM-BENCH** — scientific-paper claim→evidence reasoning.
6. **Who Said What / QuoteLi3** — reported-speech attribution controls, not evidence-grounding benchmarks.

## Evidence notes

- **FactAppeal:** ACL Anthology record says the dataset contains 3,226 English news sentences with span-level factual statements and source mentions, plus source type, namedness, role/credentials, and direct/indirect quotation features.
- **Who Said What:** ACL record formalizes quote attribution as pairing utterances with speakers and benchmarks available English and Chinese datasets.
- **QuoteLi3:** ACL record reports more than 6,000 quote-to-mention and quote-to-entity annotations.
- **HoVer:** ACL record identifies a many-hop evidence extraction and claim verification dataset; later scholarly evidence describes 2–6 hop chains and complementary evidence.
- **EX-FEVER:** ACL abstract reports more than 60,000 2-hop/3-hop claims with veracity labels and reasoning-path explanations.
- **WiCE:** ACL abstract reports sub-sentence entailment judgments and minimal supporting evidence subsets.
- **AVeriTeC:** ACL shared-task abstract states that systems retrieve evidence for real-world fact-checker claims and are scored only when both verdict and evidence quality are correct; its paper links the official dataset page and reports CC-BY-NC-4.0.
- **FEVEROUS / UnifEE:** ACL records describe mixed sentence/table-cell evidence, graph interactions, and multi-hop reasoning; the FEVEROUS paper defines scoring around complete gold evidence sets plus correct labels.
- **CLAIM-BENCH:** ACL abstract describes a benchmark for scientific claim-evidence extraction and validation focused on logical links in AI papers.

## Search log and failures

- Queried ACL Anthology for attribution benchmarks, quote attribution, multi-hop fact verification, evidence chains, claim-evidence entailment, FEVEROUS, HoVer, WiCE, EX-FEVER, AVeriTeC, FactAppeal, and scientific claim-evidence validation.
- Search results were dominated by benchmark evaluations and method papers; these were retained only when they documented a reusable benchmark or a concrete evaluation resource.
- No exact unified resource was found that simultaneously provides: (a) claim ownership/source identity, (b) support/attack/disagreement, and (c) recursively linked multi-hop evidence paths. This is recorded as a gap, not inferred away.
- Separate artifact access and licensing were not inferred from paper access. Rows marked **not verified** require a follow-up download/license check.
- Quote attribution resources were retained as strong adjacent controls because they isolate the reported-speech/ownership subproblem but do not establish epistemic truth.

## Source URLs

- Mor-Lan, Sheafer, & Shenhav (2026) — https://aclanthology.org/2026.findings-eacl.344/
- Zhong et al. (2024) — https://aclanthology.org/2024.lrec-main.1530/
- Muzny et al. (2017) — https://aclanthology.org/E17-1044/
- Jiang et al. (2020) — https://aclanthology.org/2020.findings-emnlp.309/
- Ma et al. (2024) — https://aclanthology.org/2024.findings-acl.556/
- Kamoi, Goyal, Rodriguez, & Durrett (2023) — https://aclanthology.org/2023.emnlp-main.470/
- Schlichtkrull et al. (2024) — https://aclanthology.org/2024.fever-1.1/
- Hu et al. (2026) — https://aclanthology.org/2026.acl-long.119/
- Wu, Hu, & Feng (2023) — https://aclanthology.org/2023.emnlp-main.409/
- Aharoni et al. (2014) — https://aclanthology.org/W14-2109/
- Hu et al. (2023) — https://aclanthology.org/2023.eacl-main.82/
- Javaji et al. (2025) — https://aclanthology.org/2025.ijcnlp-long.127/
