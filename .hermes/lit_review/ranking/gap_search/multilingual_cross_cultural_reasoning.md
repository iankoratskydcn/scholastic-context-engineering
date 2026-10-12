# Multilingual and cross-cultural reasoning / argument-structure resources

**Slug:** `multilingual_cross_cultural_reasoning`  
**Research date:** October 12, 2026  
**Records:** 13

## Scope

This sweep targeted scholarly benchmark or corpus resources that do at least one of the following:

- preserve aligned or translated instances across languages;
- evaluate logical, causal, analogical, syllogistic, commonsense, or pragmatic reasoning;
- expose argument components, argumentation schemes, support/attack structure, or explanation labels;
- make cultural context an explicit evaluation variable rather than treating English performance as universal.

The CSV preserves the repository's benchmark-resource schema and distinguishes direct resources from adjacent controls. It does **not** treat cultural variation as evidence for a distinct formal “non-Western logic.” Formal validity, multilingual transfer, culturally situated commonsense, values, and pragmatic interpretation are kept as separate diagnostic axes.

## Highest-value resources

1. **NLAS-multi** — direct multilingual argumentation-scheme classification over 20 Walton schemes, with English and Spanish generated/curated arguments. Best controlled form-layer resource; synthetic structure requires human-authored validation.
2. **Multi-lingual Argumentative Corpora** — parallel English/Balkan/Arabic news corpora with projected argumentative labels. Best literal parallel-text resource for testing structural preservation across translation, but labels are projected rather than independently authored in each language.
3. **LogiQA / LogiQA 2.0** — Chinese civil-service logical reasoning, with LogiQA 2.0 adding professional translation and reannotation. Best Chinese-source deductive control and best paired translation-aware variant.
4. **NeuBAROCO** — English/Japanese categorical syllogisms with belief-bias, conversion, and atmosphere manipulations. Best multilingual formal-logic/bias diagnostic.
5. **E-KAR** — Chinese and English analogical reasoning with free-text rationalization. Best bilingual resource for relational structure plus explanation rather than answer-only scoring.
6. **XCOPA** — aligned causal commonsense reasoning in 11 typologically diverse languages, including low-resource languages. Best clean cross-lingual causal-transfer control.
7. **MAPS** — six-language proverb interpretation in conversational contexts, explicitly separating memorization from culturally grounded reasoning and measuring culture gaps. Best pragmatic/culture-sensitive reasoning resource.
8. **SeaEval / Global MMLU** — broad multilingual evaluation suites with parallel logical or general-knowledge subsets and explicit translation/cultural-sensitivity controls. Best calibration resources, not argument-structure benchmarks.
9. **ArabCulture / GeoMLAMA / Mickey** — native-authored or geographically differentiated commonsense resources that expose cultural-premise and language-access effects. Use as cultural-context controls, not formal reasoning scores.

## Interpretation and limitations

- **Direct argument structure is scarce.** NLAS-multi is the clearest multilingual scheme resource; the parallel argumentative corpora provide sentence-level argumentative labels but not full premise/conclusion graphs.
- **Most “cross-cultural reasoning” benchmarks are not formal-logic benchmarks.** ArabCulture, GeoMLAMA, MAPS, SeaEval, and Mickey primarily test culturally situated commonsense, pragmatic interpretation, or multilingual robustness.
- **Translation is a confound and an experimental variable.** LogiQA 2.0, XCOPA, SeaEval, and Global MMLU are useful because they make translation or parallelism explicit, but translated items can change idioms, difficulty, and cultural presuppositions.
- **Native-authored versus translated material should be reported separately.** ArabCulture and the parallel argumentative corpora answer different questions from X-CSQA/X-CODAH, LogiQA 2.0, or XCOPA.
- **Do not collapse labels.** Scheme labels, argumentative/non-argumentative labels, validity/entailment, causal plausibility, analogy rationalization, proverb interpretation, and cultural-value judgments are distinct outputs.
- **Artifact and license status are conservative.** Public scholarly pages and linked repositories were found for most records, but exact dataset revisions, redistribution terms, and some release endpoints require a final artifact-level pin before production use.

## Recommended evaluation battery

For a compact but diagnostic battery, combine:

- **NLAS-multi + Multi-lingual Argumentative Corpora** for multilingual argument-form and aligned span extraction;
- **LogiQA 2.0 + NeuBAROCO** for translation-aware deductive reasoning and formal validity/bias controls;
- **E-KAR + XCOPA** for analogical and causal reasoning with explicit cross-language comparison;
- **MAPS + ArabCulture** for culturally embedded, pragmatic, and native-authored reasoning;
- **SeaEval or Global MMLU** for broad multilingual consistency and translation/cultural-sensitivity calibration.

Report language-wise scores, native versus translated subsets, explanation/structure accuracy separately from final-answer accuracy, and failure buckets for language access, cultural knowledge, argument parsing, formal validity, and reasoning.

## Primary records consulted

- ACL Anthology: `L18-1617`, `2020.emnlp-main.185`, `2021.acl-long.102`, `2022.emnlp-main.132`, `2022.findings-acl.311`, `2023.naloma-1.1`, `2024.naacl-long.22`, `2024.naacl-long.112`, `2025.acl-long.380`, `2025.acl-long.919`.
- DOI record: `10.1016/j.dib.2024.111087` for NLAS-multi.
- Linked artifacts: official GitHub or dataset endpoints where identified in the CSV; licenses remain explicitly marked unresolved when not independently verified.

## Search and evidence note

The repository's existing literature summaries were used as a starting evidence plane, then primary scholarly records and artifact links were checked through ACL Anthology, DOI/search records, and official repositories. Retrieved pages were treated as untrusted data. No external repository was added as a runtime dependency, and no production code was modified.
