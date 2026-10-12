# Expert argument comparison benchmark search

**Slug:** `expert_argument_comparison`  
**Verification date:** 2026-10-12 (US/Eastern)  
**Scope:** benchmarks and evaluation resources that compare competing arguments, rank arguments/passages, or calibrate argument-quality judgments against experienced human or professional experts. Formal argument-strength competitions are retained as controls, not mistaken for expert-natural-language benchmarks.

## Findings

1. **Best direct pairwise resources:** IBM-ArgQ, Webis-ArgQuality-20, UKPConvArg, IBM-EviConv, Passage Convincingness, ClaimRev, and the 2024 end-to-end debate-preparation dataset provide explicit pairwise preferences or ranking targets. IBM-ArgQ is the cleanest controlled pairwise argument-quality benchmark: 6.3k individually annotated arguments plus 14k independently labeled pairs. Webis-ArgQuality-20 is the strongest multi-dimensional pairwise resource, with rhetorical, logical, dialectical, and overall scores inferred from 41,859 pairwise judgments over 1,271 arguments.

2. **Best expert calibration resource:** *This House Debates AI* directly compares an LLM with 20 experienced human debaters across 100 six-turn Oxford-style debates. Five independent raters provide win/loss judgments and 0–100 scores on 11 quality dimensions. It is the closest retained benchmark to expert judgment of competing complete arguments, but its unit is a whole debate and its winner label is not a proposition-level defeat or proof judgment.

3. **Best current judge-calibration paper:** Ocampo, Nyiranziza, and Ceolin (2026) explicitly approximate expert pairwise comparisons across logical, rhetorical, and dialectical dimensions and aggregate them with a Bradley–Terry model. It is highly relevant methodologically, but the retained record is an evaluation study rather than a clearly packaged, independently reusable benchmark artifact.

4. **Best legal/philosophical calibration complements:** PRBench, PLAWBENCH, LEGIT, and GreekBarBench use expert-authored tasks, expert-curated rubrics, or human-expert judge calibration for legal/professional reasoning. They are not pairwise argument-ranking datasets, but they can supply domain-specific criteria for adjudicating whether a preferred argument is legally complete, grounded, transparent, and procedurally adequate. LAR-ECHR provides structured legal-argument-chain reasoning, but not pairwise strength labels.

5. **Best formal controls:** ArgStrength 2021 and ICCMA provide machine-readable argument graphs and explicit ranking/acceptance semantics. They are useful for testing defeat, ranking, and uncertainty implementations, but they do not measure agreement with human or expert judgments over natural-language philosophical/legal arguments.

## Recommended benchmark battery

- **Pairwise quality baseline:** IBM-ArgQ + Webis-ArgQuality-20.
- **Passage/evidence preference:** IBM-EviConv + Passage Convincingness.
- **Structured debate and expert calibration:** This House Debates AI.
- **Argumentation scale and coverage:** ClaimRev + ArgBench.
- **Professional-domain calibration:** PRBench + PLAWBENCH, used as rubric layers rather than pairwise substitutes.
- **Formal semantics control:** ArgStrength 2021 + ICCMA.

## Unfilled target

No retained benchmark combines all of the following in one reusable artifact: (a) proposition-level competing arguments from philosophical or legal sources, (b) independent expert pairwise judgments, (c) explicit winner/loser/tie/incomparable outcomes, (d) reason-coded adjudication such as support, attack, burden, relevance, and validity, and (e) exact source-span provenance. The strongest defensible next step is therefore a hybrid protocol: use IBM-ArgQ/Webis-style pairwise collection, add expert legal/philosophical panels and an explicit incomparable option, and attach PRBench/PLAWBENCH-style criteria plus source spans.

## Record inventory

The companion CSV contains 22 records: 13 direct or direct-suite pairwise/ranking resources, 5 adjacent expert/rubric resources, 3 formal controls, and 1 proposed target-gap row. Each record preserves a source URL, artifact URL where identified, scale information, outcome labels, and an explicit limitation/gap statement.

## Primary sources checked

- Toledo et al., *Automatic Argument Quality Assessment: New Datasets and Methods*: https://aclanthology.org/D19-1564/
- Gienapp et al., *Efficient Pairwise Annotation of Argument Quality*: https://aclanthology.org/2020.acl-main.511/
- Potash et al., *Ranking Passages for Argument Convincingness*: https://aclanthology.org/W19-4517/
- Ocampo et al., *Argument Quality Assessment with Large Language Models: A Pairwise Bradley-Terry Approach*: https://arxiv.org/abs/2605.28313
- Belluzzo et al., *This House Debates AI*: https://aclanthology.org/2026.lrec-1.215/
- Sternlicht et al., *Debatable Intelligence*: https://aclanthology.org/2025.emnlp-main.953/
- Akyürek et al., *PRBench*: https://aclanthology.org/2026.acl-long.1958/
- Shi et al., *PLAWBENCH*: https://aclanthology.org/2026.acl-long.458/
- Li et al., *Which Side Are You On?*: https://aclanthology.org/2024.findings-acl.9/
- Lee et al., *LEGIT*: https://aclanthology.org/2026.acl-long.150/
- *GreekBarBench*: https://aclanthology.org/2025.findings-emnlp.1368/
- Lan et al., *CEDAR*: https://aclanthology.org/2026.acl-long.238/
- ArgStrength 2021: https://argstrength2021.argumentationcompetition.org/
- ICCMA 2021: https://www.argumentationcompetition.org/2021/

## Limitations of the search

Several resources report expert or experienced-human evaluation but do not release all judgments as a standalone benchmark. “Expert-calibrated” is therefore distinguished from “expert-authored/rubric-based” and from ordinary crowd pairwise annotation. Artifact availability and licensing were recorded from the cited paper/repository pages but were not treated as fully verified unless an explicit public artifact URL was present.
