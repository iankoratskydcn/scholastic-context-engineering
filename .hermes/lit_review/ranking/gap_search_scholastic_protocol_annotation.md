# Gap search: scholastic disputation-role annotation

**Slug:** `scholastic_protocol_annotation`  
**Search date:** 2026-10-12 (US/Eastern)  
**Question:** Find benchmark-producing studies or reusable resources with explicit annotations for scholastic disputation roles such as *quaestio*, objections, *sed contra*, *respondeo*/determination, and replies, including Latin and Arabic scholastic materials.

## Result

The search found **one strong direct gap-fill candidate** and **four adjacent/control resources**:

1. **Argumentation Theory TEI-XML Pilot Corpus** — closest match. The repository describes Arabic/Ottoman debate-theory witnesses, TEI-XML records, annotated TSV companions, and role vocabulary centered on the inquirer (*al-sā'il*), justifier (*al-mu'allil*), and objection order. It is the only located resource whose artifact description explicitly combines a scholastic-adjacent debate tradition with role-aware annotations. It is not yet a conventional benchmark: no verified train/dev/test split, adjudicated label inventory, or published task metrics were found.
2. **Arabic Argumentative Debate Corpus / hybrid annotation model** — strong annotation comparator. It explicitly labels position, super claim, claim, ground, warrant, backing, and rhetorical/recurrence categories, with double annotation and trained annotators. It is Arabic competitive debate, not medieval scholastic disputation, so it should not be counted as a direct scholastic benchmark.
3. **US2016G1tvWALTON** — strong generic argument-form control. It has AIF graphs and 60 Walton scheme labels on 491 of 505 inference relations, but its English political-debate domain and scheme ontology do not encode *quaestio* stages or objection/reply roles.
4. **SCTA/LombardPress** — best Latin source layer. It provides machine-readable scholastic editions, stable identifiers, witnesses, TEI/XML, and explicit *Quaestio* textual structures, but no verified gold labels for objections, *sed contra*, *respondeo*, determinations, or replies.
5. **Munazarat 1.0** — negative control. It is a substantial Arabic competitive-debate transcription corpus, but the corpus paper and later Arabic NLP evidence do not establish explicit argumentative-role gold labels.

**Bottom line:** No verified Latin benchmark with explicit, adjudicated labels for the full sequence *quaestio → objections → sed contra → respondeo/determination → replies* was located. The practical benchmark path is to use the Argumentation Theory corpus as the closest Arabic role-annotation seed, SCTA/LombardPress as the Latin source layer, and add a new expert annotation layer with span-level role labels, links from each objection to its reply, authority/source provenance, and adjudication statistics.

## Search and evidence scope

Local repository evidence was checked first, including the existing scholastic digital-humanities and scholastic-method sweeps. Those records explicitly report that the direct AI/LLM area is thin and that no verified system operationalizes the complete medieval sequence. Web/search verification then targeted:

- `quaestio objection sed contra respondeo dataset annotation`
- `scholastic disputation corpus TEI XML annotation`
- `Arabic debate corpus argumentative annotation roles`
- `munazarat corpus annotation argument scheme`
- `al-sail al-muallil annotated corpus`
- `opponens respondens medieval disputation dataset`

Primary/official routes retained in the CSV:

- Argumentation Theory repository: https://github.com/Sserhatt/Argumentation-Theory
- Arabic Argumentative Debate Corpus publication record: https://squ.elsevierpure.com/en/publications/a-hybrid-annotation-model-forarabic-argumentative-debate-corpus/
- Arabic Argumentative Debate Corpus DOI: https://doi.org/10.1007/978-3-031-79164-2_9
- US2016G1tvWALTON annotation paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC7888437/
- SCTA research infrastructure: https://community.scta.info/
- SCTA repositories: https://github.com/scta-texts/
- Munazarat 1.0 ACL record: https://aclanthology.org/2024.osact-1.3/
- Munazarat 1.0 repository: https://github.com/moh72y/Munazarat1.0

## Inclusion/exclusion decisions

- Included resources expose reusable text, corpus, annotation, graph, or benchmark artifacts rather than only historical discussion.
- `direct_gap_fill` is reserved for an artifact whose evidence explicitly combines a scholastic-adjacent disputation tradition with role-aware annotation. Only SPA-01 meets that threshold, and even it is marked as a resource/seed rather than a validated benchmark.
- `strong_adjacent` covers explicit argument-role or scheme annotation that can transfer to scholastic annotation but does not encode medieval disputation roles.
- `control_only` covers scholastic source infrastructure without role labels.
- `false_positive` covers debate/transcription resources that lack explicit role annotations.
- Paper access was not treated as proof of artifact access or licensing. Unknown license/access states remain explicit in the CSV.

## Limitations and unresolved verification

- The Argumentation Theory repository needs a direct clone/file inspection to confirm the exact label strings, file counts, annotation granularity, and any README claims against the stored TSV/TEI files.
- No peer-reviewed paper establishing a benchmark protocol, split policy, inter-annotator agreement, or baseline results for the Argumentation Theory corpus was located.
- SCTA/LombardPress record structures are not equivalent to adjudicated semantic role annotations; a future annotation pass is still required.
- The search did not establish a public, licensed Latin gold corpus for the full role sequence.
- Search engines returned noisy historical scholarship and generic argument-mining resources; those were excluded when they lacked an inspectable benchmark/resource artifact.

## Programmatic reconciliation

- CSV schema: exact `gap_benchmark_search_protocol.md` columns.
- Records written: 5.
- Duplicate record IDs: none.
- Missing required fields: none.
- Direct gap-fill records: 1.
- Strong adjacent records: 2.
- Control-only records: 1.
- False positives/negative controls: 1.
