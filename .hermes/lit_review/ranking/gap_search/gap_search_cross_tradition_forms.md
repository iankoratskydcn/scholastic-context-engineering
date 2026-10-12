# Cross-tradition argument-form benchmark gap search

**Scope.** Search for scholarly benchmark, corpus, or executable-evaluation resources covering qiyas/Islamic legal reasoning, Nyaya/Navya-Nyaya, Mohist or Chinese argumentation, medieval Latin scholastic logic, Jewish/Hebrew/Talmudic disputation, and Aristotelian reasoning. Search emphasized resources with inspectable artifacts, intermediate labels, proof traces, argument graphs, or provenance metadata.

**Result.** 13 records were retained in `gap_search_cross_tradition_forms.csv`.

## Main findings

- **Islamic / Arabic:** ALARB is the strongest Arabic legal argument benchmark located: it exposes multistep reasoning chains, verdicts, and cited regulations. QIAS/MAWARITH is the closest explicitly Islamic executable reasoning task, with intermediate inheritance stages and final distributions. Munazarat 1.0 supplies authentic Arabic debate audio/transcripts and metadata, but not tradition-specific logical labels.
- **Jewish / Hebrew / Aramaic:** MishnaBase is the clearest direct resource: every Mishnah argument is manually coded with participants, positions, dispute direction, and outcome fields. Waxman’s Talmud graph adds typed inquiry, objection, retort, support, and disagreement edges with page-level provenance.
- **Medieval Latin / Aristotelian:** The Index Thomisticus Treebank is a usable medieval Latin syntactic substrate, not an argument benchmark. Glashoff’s Aristotelian reduction system is an executable formalization/proof-trace precedent, not a natural-language dataset.
- **Nyaya:** Pramana is the only directly named benchmark-like Nyaya task found, but it is a small 55-problem preprint and its artifact/provenance claims require verification. Panday and Ghosh provide a stronger typed-formalization precedent for Navya-Nyaya relations and proof checks, but not a standardized benchmark.
- **Mohist:** No verified scholarly benchmark or released executable corpus directly annotating Later Mohist *bian* / Canons as a named reasoning tradition was found. Chinese argument corpora ORCHID and the Chinese hotel-review corpus are retained only as adjacent/control resources and must not be labeled Mohist.
- **Cross-tradition gap:** No single resource combines historically faithful source text, named tradition-specific argument forms, intermediate proof/dialectical structure, and reproducible evaluation across qiyas, Nyaya, Mohist, Latin scholastic, and Jewish/Hebrew traditions.

## Recommended use

1. Use **QIAS/MAWARITH + ALARB** for Islamic-law reasoning and staged evaluation.
2. Use **MishnaBase + Talmud graph** for Jewish/Hebrew/Aramaic dispute structure and provenance.
3. Use **Index Thomisticus Treebank + Glashoff** as the medieval Latin/Aristotelian source-and-formalization pair.
4. Treat **Pramana** as a provisional Nyaya challenge set pending artifact, license, and historical-fidelity audit; use the Navya-Nyaya type-theoretic work to design a tradition-specific IR.
5. Use **Munazarat, ORCHID, and Chinese argument mining** as language/dialogue controls, not as historical-logic substitutes.
6. Build a Mohist benchmark from primary-text editions and expert annotation rather than repurposing generic Chinese debate data.

## Evidence and limitations

- Exact identity was checked against ACL Anthology, Oxford Academic, arXiv, university project pages, GitHub/repository pages, and retained local scholarly summaries.
- “Paper accessible” is not treated as proof that a dataset, code release, or license is accessible. Rows explicitly distinguish paper access from artifact/license verification.
- Several promising items are preprints or infrastructure projects rather than mature benchmarks. Their confidence is reduced where the artifact URL, license, or historical provenance was not independently resolved.
- Formalizations of Aristotle or Navya-Nyaya establish properties of the reconstruction, not that the reconstructed calculus exhausts the historical tradition.

## Failed / blocked / negative searches preserved

- **Mohist bian / Later Mohist Canons:** Searches combining `Mohist logic`, `bian`, `Canons`, `argument mining`, `dataset`, `benchmark`, `corpus`, and `executable` found scholarly translations and historical studies but no verified benchmark with released argument labels or evaluation splits. Generic Chinese argument corpora were downgraded to `control_only` or `strong_adjacent`.
- **Named qiyas benchmark:** No standalone benchmark explicitly titled for classical *qiyas* argument forms was verified. The QIAS shared task is an Arabic Islamic inheritance-reasoning benchmark and is therefore recorded as a direct adjacent operationalization, not as proof of broad qiyas coverage.
- **Nyaya artifact verification:** The Pramana preprint claims model/data release, but the exact Hugging Face collection was not independently resolved during this pass; row CTF-10 remains medium confidence.
- **Universal cross-tradition benchmark:** No resource was found that jointly evaluates Islamic, Nyaya, Mohist, medieval Latin, and Jewish/Hebrew argument forms while preserving distinct vocabularies and provenance.
- **Artifact extraction limitation:** The configured native web extractor could not open URLs in this environment, so evidence was triangulated from search results, official bibliographic/project pages, accessible ACL/arXiv metadata, and the repository’s retained scholarly summaries. Claims marked as requiring artifact verification were left explicitly unresolved rather than inferred.

## Sources consulted

- ACL Anthology records for ALARB, QIAS shared tasks, Munazarat 1.0, ArabLegalEval, and related Arabic resources.
- Oxford Academic records for the Talmud graph and medieval logic sources.
- University project/repository pages for the Index Thomisticus Treebank.
- OpenITI project documentation and repository.
- arXiv records for Pramana, Navya-Nyaya formalization, ORCHID, and Chinese argumentation.
- JSIJ article and MishnaBase repository for Mishnaic disputes.

The CSV is the machine-readable evidence ledger; unresolved access, licensing, and historical-fidelity questions are retained in each row rather than silently upgraded.
