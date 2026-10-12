# Benchmark gap search: claim ownership, reported speech, and attribution-aware argument extraction

## Scope and result

This search targeted scholarly benchmarks and reusable corpora for:

- claim ownership / author-versus-quoted-claim separation;
- reported speech and quotation extraction with speaker/addressee attribution;
- attribution relations exposing source, cue, and content;
- adjacent claim/evidence or argument-mining benchmarks that can be paired with ownership labels.

**Records:** 9. The strongest direct gap fills are **PARC 3.0**, **PolNeAR**, and **DirectQuote**. **PDNC**, **QuoteLi3**, and the **Who Said What** benchmark are strong reported-speech/ownership resources, while **Aharoni et al. (2014)** is an adjacent argument-extraction control without source-ownership labels.

## Ranked findings

1. **PolNeAR (Newell, Margolin & Ruths, 2018)** — political-news attribution with source, cue, and content labels; about 24,000 attributions over 1,008 articles; official GitHub artifact. Best direct fit for author-vs-quoted claim separation in authentic news.
2. **PARC 3.0 (Pareti, 2016)** — approximately 20,000 fully annotated attribution relations, including source/cue/content, direct/indirect/mixed quotation, opinion, fact, belief, and nested attribution. Best broad relation inventory.
3. **DirectQuote (Zhang & Liu, 2022)** — 19,706 news paragraphs and 10,279 manually annotated direct quotations, with speakers linked to Wikidata. Best large direct-quote extraction plus entity-linked ownership resource.
4. **PDNC (Vishnubhotla, Hammond & Hirst, 2022)** — 35,978 quotations in 22 novels with speaker, addressee, quotation type, referring expression, and character mentions. Best difficult implicit/anaphoric ownership control, but literary rather than argumentative.
5. **Who Said What (Zhong et al., 2024)** — formalized bilingual quote-attribution evaluation over seven existing datasets. Best comparative evaluation harness, not a new unified corpus.
6. **QuoteLi3 (Muzny et al., 2017)** — quote-to-mention and quote-to-entity labels for 3,103 quotes across three novels. Useful for separating mention ownership from resolved speaker identity.
7. **RiQuA (LREC 2020)** — rich reported-speech annotation with quotation type, cues, speakers, and addressees/listeners. Promising direct fit, but artifact details and full metadata were not fully verified in this run.
8. **PARC3–PolNeAR family comparison** — not a new dataset, but a useful schema benchmark: PARC3 supports nested/overlapping attribution; PolNeAR supplies a larger political-news corpus with high-completeness annotations and a simpler univocal scheme.
9. **Aharoni et al. (2014)** — claims/evidence benchmark for controversial topics. Strong adjacent argument-mining control, but it does not encode source ownership or author-versus-quoted disagreement.

## Coverage mapping

| Resource | Claim ownership | Reported speech | Source/cue/content | Argument/evidence | Fit |
|---|---:|---:|---:|---:|---|
| PARC 3.0 | Yes | Yes | Yes | Indirect | direct gap fill |
| PolNeAR | Yes | Yes | Yes | Indirect | direct gap fill |
| DirectQuote | Yes | Yes, direct only | Partial | Indirect | direct gap fill |
| PDNC | Yes | Yes | Partial | No | direct gap fill for ownership control |
| Who Said What | Yes | Yes | Evaluation-level | No | strong adjacent |
| QuoteLi3 | Yes | Yes | Partial | No | strong adjacent |
| RiQuA | Yes | Yes | Likely yes | No | direct gap fill, confidence limited |
| PARC3–PolNeAR family | Yes | Yes | Yes | Indirect | direct gap fill |
| Aharoni et al. | No | No | No | Yes | strong adjacent control |

## Evidence and access notes

- Exact scholarly identity was verified from ACL Anthology pages/PDF search results for all ACL records.
- The PolNeAR official repository was identified as `https://github.com/networkdynamics/PolNeAR`; it documents the corpus composition, annotation structure, and train/dev/test organization.
- The DirectQuote official repository was identified as `https://github.com/THUNLP-MT/DirectQuote`; the paper/search evidence gives corpus counts and Wikidata-linked speakers.
- The PDNC official repository was identified as `https://github.com/Priya22/project-dialogism-novel-corpus`; the scholarly evidence gives the 22-novel and 35,978-quotation figures.
- Artifact access and license were not inferred from paper access. Where the exact artifact license or download endpoint was not visible in retained evidence, the CSV says `not verified`.
- The RiQuA record is intentionally retained with lower confidence because the search result exposed task/schema details but did not fully recover authors, counts, artifact endpoint, or license.

## Failed or blocked searches

- Search backend returned a usable scholarly search result for the requested terms, but the configured `web_extract` backend refused URL extraction because the active backend was search-only (`OpenAI Native Web Search (Codex Responses) is a search-only backend and cannot extract URL content`).
- Several searches returned truncated result payloads because the search response exceeded the output budget. Records were retained only where the returned scholarly page/PDF snippets exposed enough identity and benchmark details; otherwise fields are explicitly marked `not verified` or the item is labeled adjacent.
- Searches for a benchmark explicitly named “claim ownership” did not surface a canonical resource under that exact name. The operationally closest scholarly resources use **attribution relations**, **quote attribution**, **reported speech**, or **source/cue/content** terminology.
- No claim-ownership benchmark was found that simultaneously combines source ownership, disagreement stance, and full argument graph extraction in one artifact. The likely construction path is to align PolNeAR/PARC3-style attribution with an argument-mining benchmark such as Aharoni et al.

## Duplicate/version handling

- PARC3 and PolNeAR are retained as separate resources and also represented once as a family-comparison record because they are distinct corpora with materially different annotation completeness and nesting policies.
- The “Who Said What” record is an evaluation benchmark over existing datasets, not a duplicate corpus release.
- ACL Anthology page and PDF URLs are treated as scholarly-source variants of the same paper; only one record is used per paper except where a family comparison is analytically necessary.

## Search provenance

Queries used included:

- `scholarly benchmark source attribution reported speech quotation attribution dataset argumentative text`
- `benchmark claim ownership author quoted claim separation stance attribution corpus`
- `site:aclanthology.org reported speech extraction corpus benchmark source cue content news`
- `site:aclanthology.org attribution relations benchmark argumentative text speaker source content`
- `claim attribution benchmark fact checking source ownership dataset`

All external facts in the CSV are tied to a scholarly source URL or official artifact URL; uncertain access/license claims are preserved as uncertainty rather than inferred.
