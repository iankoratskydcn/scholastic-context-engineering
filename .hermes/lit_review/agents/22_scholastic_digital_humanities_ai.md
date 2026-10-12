# Search angle 2 — AI and computational/digital humanities for medieval scholastic texts

**Research date:** 2026-10-11

## Scope and search record

**Question.** What computational, digital-humanities, NLP/AI, and formalization work directly concerns medieval scholastic texts or adjacent medieval philosophical/theological corpora (quaestiones, disputations, commentaries, sententiae, reportationes, Arabic–Latin transmission), and how much of it performs actual argument reasoning rather than merely digitizing or annotating texts?

**Scholar-oriented query variants used (Google Scholar route plus venue searches):**
1. `scholastic texts digital humanities corpus medieval quaestiones computational analysis`
2. `medieval scholastic disputations NLP AI computational humanities`
3. `medieval philosophy text mining digital humanities commentary sententiae`
4. `formalization scholastic arguments medieval logic AI theorem proving`
5. `Aquinas corpus computational text mining`
6. `Index Thomisticus treebank parsing Universal Dependencies`
7. `medieval Latin HTR transformer OCR`
8. `DEBATE ERC medieval philosophy digital corpus`
9. `Arabic Latin Corpus medieval philosophy digital humanities`
10. `e-Ideas computational history of ideas medieval philosophy topic modeling`

Scholar result pages were not reliably fetchable in this environment. Results were therefore resolved to ACL Anthology, arXiv, DOI/publisher records, official project pages, CORDIS, Universal Dependencies, or institutional repositories. Search snippets were used for discovery only; the retained items below have an inspectable scholarly or primary project landing page. Exact URLs/DOIs are given for reproducibility.

## Verified sources retained (15)

### 1. Langton’s *Quaestiones Theologiae*: HTR + stylometry + authorship/editorial layers

- **Citation.** Anonymous-contribution study on Stephen Langton’s *Quaestiones Theologiae* (2025), *Computational Humanities Research*. DOI: `10.1017/chr.2025.10004`. Publisher: <https://doi.org/10.1017/chr.2025.10004>. Open preprint: <https://arxiv.org/abs/2508.12830>.
- **What it does.** Designs a computational study of reportationes using authorship-attribution/stylometric features (most frequent words, POS n-grams, pseudo-affixes), with transformer-based HTR and alignment of automatically extracted transcriptions. The target is internal editorial/collaborative structure, not theorem proving.
- **Classification.** **AI/computational analysis:** HTR and stylometry; **not AI reasoning**.
- **Relevance.** Closest direct precedent for computationally studying the formation of a scholastic quaestiones collection and the transition from oral teaching records to literary text.
- **Novelty threat.** A claim of being the first computational study of scholastic reportationes/authorship would be vulnerable. The paper already supplies a strong precedent for HTR + stylometry on a scholastic corpus.
- **Limitations.** The article is a study design/proposed workflow; short quaestiones make stylometry unstable, and HTR/transcription noise can be mistaken for authorial signal. It does not recover argumentative roles or validate scholastic inferences.

### 2. CREMMA Medii Aevi: medieval Latin HTR dataset

- **Citation.** Thibault Clérice et al. “CREMMA Medii Aevi: Literary Manuscript Text Recognition in Latin.” *Journal of Open Humanities Data* (2023). DOI: `10.5334/johd.97`. <https://doi.org/10.5334/johd.97>. Dataset: <https://zenodo.org/records/7510411>.
- **What it does.** Provides a segmentation/handwritten-text-recognition dataset for Medieval Latin literary manuscripts, covering approximately the eleventh–sixteenth centuries; the metadata/search record reports 263,000 items/units and a reusable HTR model/data release.
- **Classification.** **Corpus digitization / AI transcription:** HTR; **not AI reasoning**.
- **Relevance.** Establishes a reusable technical layer for opening manuscript scholastic sources before linguistic or argument analysis.
- **Novelty threat.** “Applying transformers to medieval scholastic manuscripts” is not by itself novel; HTR resources and models already exist for Medieval Latin.
- **Limitations.** Literary-manuscript coverage is broader than scholastic disputations; transcription is not normalization, linguistic annotation, or argument segmentation.

### 3. Medieval Latin HTR for the Bavarian Medieval Latin Dictionary

- **Citation.** “A Tailored Handwritten-Text-Recognition System for Medieval Latin.” *Ancient Language Processing* (2023). ACL Anthology: <https://aclanthology.org/2023.alp-1.12/>. arXiv HTML: <https://arxiv.org/html/2308.09368>.
- **What it does.** Builds an end-to-end pipeline for locating, extracting, and transcribing handwritten Medieval Latin dictionary record cards, using image segmentation and transformer-based HTR.
- **Classification.** **AI transcription / digitization:** HTR; **not AI reasoning**.
- **Relevance.** Demonstrates domain-tailored modeling for low-resource Medieval Latin and highlights the separation between visual transcription and downstream historical interpretation.
- **Novelty threat.** A project using transformer HTR as its main technical contribution would enter an established line of work.
- **Limitations.** Dictionary cards are not quaestiones or commentaries; no scholastic argument representation or inference evaluation.

### 4. The Index Thomisticus Treebank project

- **Citation.** Federica Gamba, Marco Passarotti, and Paolo Ruffolo. “The Index Thomisticus Treebank Project: Annotation, Parsing and Valency Lexicon.” *Traitement Automatique des Langues* 50(2) (2009): 103–127. ACL/venue record: <https://aclanthology.org/2009.tal-2.5/>. Related DOI-bearing chapter record: `10.1515/9783110599572-017`, <https://doi.org/10.1515/9783110599572-017>.
- **What it does.** Introduces a dependency-based treebank derived from the roughly 11-million-word *Index Thomisticus* of Aquinas, with Medieval Latin syntactic annotation, parsing experiments, and a valency lexicon.
- **Classification.** **Corpus infrastructure + NLP parsing:** linguistic annotation and supervised parsing; **not AI reasoning**.
- **Relevance.** The central machine-readable resource for Aquinas, including material relevant to *Summa*, *Summa contra Gentiles*, and *Scriptum super Sententiis*.
- **Novelty threat.** A claim that scholastic Latin lacks treebanked data or that Aquinas has no computational syntax resource is false.
- **Limitations.** Dependency syntax is not a theory of scholastic disputation; parsing a sentence does not identify objections, sed contra, respondeo, authorities, or inferential warrants.

### 5. Converting the Index Thomisticus Treebank into Universal Dependencies

- **Citation.** Flavio M. Cecchini, Marco Passarotti, and Dan Zeman. “Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies.” *Universal Dependencies / W18 workshop* (2018). ACL record: <https://aclanthology.org/W18-6004/>. Repository record: <https://zenodo.org/records/2552203>.
- **What it does.** Revises and harmonizes the Medieval Latin Aquinas treebank for Universal Dependencies, addressing POS, lemmatization, dependency relations, errors, and inconsistencies, with evaluation against a gold standard.
- **Classification.** **Corpus normalization/interoperability:** NLP annotation; **not AI reasoning**.
- **Relevance.** Makes scholastic Latin more interoperable with cross-linguistic NLP tooling and exposes the nontrivial choices hidden in “standardized” annotation.
- **Novelty threat.** A new project that simply converts Aquinas into UD would be incremental unless it adds argument-level or historically explicit annotation.
- **Limitations.** UD harmonization can aid comparison but cannot be treated as a neutral representation of medieval semantics or disputational function.

### 6. Parsing advances on the Index Thomisticus Treebank

- **Citation.** Federica Gamba, Marco Passarotti, and Paolo Ruffolo. “More Data and New Tools. Advances in Parsing the Index Thomisticus Treebank.” *Computational Humanities Research 2021*, CEUR-WS 2021: 108–122. DOI: `10.5281/zenodo.5599095`. <https://doi.org/10.5281/zenodo.5599095>. Full paper: <https://ceur-ws.org/Vol-2989/long_paper20.pdf>.
- **What it does.** Tests the effects of larger training data and newer parser/tool combinations on Medieval Latin Aquinas dependency parsing.
- **Classification.** **AI/NLP:** supervised parsing; **not AI reasoning**.
- **Relevance.** Gives a concrete benchmark family for evaluating whether modern parsers improve on scholastic Latin, rather than assuming contemporary-language performance transfers.
- **Novelty threat.** “Using a modern transformer/parser on Aquinas” is not sufficient novelty; the treebank and comparative parsing literature already establish the task.
- **Limitations.** Parsing scores do not measure argument reconstruction, historical adequacy, or whether a model distinguishes authorities from an author’s own claims.

### 7. Index Thomisticus Treebank as linked data in LiLa

- **Citation.** Federica Gamba et al. “The Index Thomisticus Treebank as Linked Data in the LiLa Knowledge Base.” *LREC 2022*. <https://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.428.pdf>.
- **What it does.** Publishes the Thomistic dependency treebank as Linguistic Linked Open Data and links corpus tokens/dependencies to interoperable Latin lexical resources in the LiLa knowledge base.
- **Classification.** **Corpus interoperability / knowledge representation:** linked data; **not AI reasoning**.
- **Relevance.** A model for connecting scholastic text, morphology, syntax, and lexical resources while preserving identifiers and provenance.
- **Novelty threat.** A new “knowledge graph for scholastic texts” needs to distinguish corpus/lexical linking from argument reasoning; LiLa already demonstrates substantial infrastructure.
- **Limitations.** Linked-data connectivity does not entail an argument graph. The resource remains primarily linguistic and lexical.

### 8. eFontes models for Medieval Latin annotation

- **Citation.** “eFontes. Part of Speech Tagging and Lemmatization of Medieval Latin Texts. A Cross-Genre Survey” (2024). arXiv: `2407.00418`. <https://arxiv.org/abs/2407.00418>.
- **What it does.** Trains/evaluates transformer-based models for Medieval Latin lemmatization, POS tagging, and morphological features using UD resources and a Polish Medieval Latin corpus; reports accuracy under orthographic and lexical variation.
- **Classification.** **AI/NLP annotation:** sequence labeling/lemmatization; **not AI reasoning**.
- **Relevance.** Shows the importance of genre and orthographic variation for any downstream retrieval or argument mining over scholastic Latin.
- **Novelty threat.** A claim that Medieval Latin lacks neural linguistic annotation models is untenable.
- **Limitations.** The evaluated tasks stop below discourse structure; high token-level accuracy cannot establish correct interpretation of quaestio architecture or inferential force.

### 9. *Corpus Thomisticum* official research infrastructure

- **Citation.** *Corpus Thomisticum*, official project introduction: <https://corpusthomisticum.org/wintroen.html>.
- **What it does.** Provides searchable editions of Aquinas, bibliography, research tools, manuscript material, and database functions for words, phrases, quotations, similarities, correlations, and statistics. The project descends from Busa’s *Index Thomisticus* work.
- **Classification.** **Corpus digitization/search infrastructure:** not AI reasoning.
- **Relevance.** A foundational primary corpus for Thomistic commentaries, disputed questions, *Sentences* material, and theological/philosophical prose.
- **Novelty threat.** “Building the first searchable digital Aquinas corpus” is not novel; the resource is mature and historically central to DH.
- **Limitations.** Search, concordance, and similarity functions are not argument-aware retrieval or validity checking. Editions and metadata must still be audited at passage level.

### 10. The *Index Thomisticus* as a Big Data project

- **Citation.** Geoffrey Rockwell and Marco Passarotti. “The Index Thomisticus as a Big Data Project.” *Umanistica Digitale* 3(5) (2019). DOI: `10.6092/issn.2532-8816/8575`. <https://doi.org/10.6092/issn.2532-8816/8575>.
- **What it does.** Histories and analyzes the *Index Thomisticus* as DH infrastructure, emphasizing data representation, scale, concordance, and project management/media archaeology.
- **Classification.** **DH history/infrastructure:** not AI reasoning.
- **Relevance.** Prevents anachronistic claims that computational work on scholastic texts begins with current LLMs; Aquinas has been a computational corpus case since the mid-twentieth century.
- **Novelty threat.** “First computational treatment of Aquinas” claims are especially vulnerable because the *Index* is an iconic early large-scale humanities-computing project.
- **Limitations.** Historical infrastructure analysis does not itself provide modern argument mining or semantic formalization.

### 11. DEBATE: Innovation as Performance in Late-Medieval Universities

- **Citation.** ERC-DEBATE project, official site: <https://debate-erc.com/>; corpus page: <https://debate-erc.com/corpus/>; European Commission CORDIS fact sheet, grant 771589, DOI `10.3030/771589`: <https://cordis.europa.eu/project/id/771589>.
- **What it does.** Builds a corpus of late-medieval university *principia* across cultural contexts, with goals including authorship attribution, neglected-text recovery, manuscript/text transmission, and study of academic innovation/debate.
- **Classification.** **Corpus construction, digital editions, authorship/transmission research:** computational/DH-adjacent; **not AI reasoning**.
- **Relevance.** Directly targets university debate practice and a corpus type adjacent to scholastic disputations, with manuscript-aware provenance.
- **Novelty threat.** A claim that no structured digital corpus exists for late-medieval university debate or authorship/transmission work would overlook DEBATE.
- **Limitations.** The project’s corpus and scholarly tools are not an evaluated LLM argument-reasoning benchmark; authorship attribution is not reconstruction of argument validity.

### 12. Arabic and Latin Corpus

- **Citation.** University of Würzburg, *Arabic and Latin Corpus*: <https://www.arabic-latin-corpus.philosophie.uni-wuerzburg.de/>.
- **What it does.** Provides a digital collection of Arabic–Latin translations from the tenth–fourteenth centuries, aiming to document Arabic influence in Europe and supply citable digital editions of texts, translators, authors, and witnesses.
- **Classification.** **Corpus digitization and transmission infrastructure:** not AI reasoning.
- **Relevance.** Essential adjacent resource for Islamic/Arabic–Latin philosophical and scientific transmission, terminology, and translation comparison around scholastic traditions.
- **Novelty threat.** A project claiming to be the first computational corpus for Arabic–Latin medieval philosophical transmission would face a direct prior-art challenge.
- **Limitations.** A bilingual digital corpus enables retrieval and alignment but does not by itself identify argument schemes, theological commitments, or cross-language inferential equivalence.

### 13. UniQ: Prague debate on universals

- **Citation.** Institute of Philosophy of the Czech Academy of Sciences, UniQ database: <https://digitalhumanities.cz/en/db/uniq-2/>.
- **What it does.** Interlinks texts, authors, manuscripts, and bibliography for the medieval debate on universals at Prague (1348–1500), supporting analysis of relationships and transmission.
- **Classification.** **Scholastic corpus/bibliographic graph:** not AI reasoning.
- **Relevance.** A concrete debate-centered data model, useful for linking philosophical positions, authorship, manuscript witnesses, and university intellectual history.
- **Novelty threat.** A new project centered on a structured database of a medieval philosophical debate would not be unprecedented; its novelty must lie in argument-level annotation or model evaluation.
- **Limitations.** Relation graphs and metadata are not the same as extracted premises, objections, replies, or formal validity judgments.

### 14. Formalizing Medieval Logical Theories

- **Citation.** Catarina Dutilh Novaes. *Formalizing Medieval Logical Theories: Suppositio, Consequentiae and Obligationes* (2007). DOI: `10.1007/978-1-4020-5853-0`. <https://doi.org/10.1007/978-1-4020-5853-0>.
- **What it does.** Develops formal reconstructions of medieval theories of supposition, consequences, and obligationes, treating formalization as an interpretive and philosophical instrument rather than a neutral transcription.
- **Classification.** **Actual formalization of historical reasoning:** closest retained precedent to scholastic argument modeling; not an LLM paper.
- **Relevance.** Supplies the conceptual guardrail for encoding historically specific logical/semantic practices without reducing them to modern predicate logic.
- **Novelty threat.** “First formalization of medieval scholastic logic” is false. The project’s novelty must be corpus-scale, provenance-aware, computationally executable, or comparative across traditions.
- **Limitations.** Formal reconstructions are theory-level and local; they do not automatically align manuscript passages, identify argument roles in large corpora, or evaluate LLM outputs.

### 15. Digital history of ideas / e-Ideas

- **Citation.** Arianna Betti and Hein van den Berg (eds.), *Data-Driven History of Ideas* collection, *Open Library of Humanities Data*: <https://openhumanitiesdata.metajnl.com/collections/historyofideas>. Project site: <https://conceptsinmotion.org/e-ideas/>.
- **What it does.** Develops a computational history-of-ideas program using qualitative, quantitative, and text-mining methods to study the development and spread of concepts; related work includes topic modeling and concept modeling over historical philosophical corpora.
- **Classification.** **Computational intellectual history:** AI/statistical text analysis; generally **not argument reasoning**.
- **Relevance.** Provides methodological precedent for concept trajectories and corpus-scale comparison around philosophical terminology, including ancient/medieval material, while warning that topic/concept models are not substitutes for interpretation.
- **Novelty threat.** “First computational history-of-ideas treatment of philosophical concepts” is too broad; the field is established.
- **Limitations.** Concept frequency/topic proximity does not recover the argumentative function of a term inside a quaestio, commentary, or theological disputation.

## Corpus digitization vs. actual AI/formal reasoning

### Corpus/digitization/annotation infrastructure (dominant majority)

The strongest and most mature layer is infrastructure: *Corpus Thomisticum*; the *Index Thomisticus* and its treebank/UD/LiLa derivatives; CREMMA and other Medieval Latin HTR resources; DEBATE; the Arabic and Latin Corpus; and UniQ. These works solve access, transcription, editions, metadata, morphology, syntax, linking, authorship, or transmission. They are indispensable prerequisites, but they do not normally infer a scholastic conclusion, validate a disputed-question argument, or reconstruct the semantics of an objection/reply structure.

### Actual computational/AI analysis

There is meaningful AI/ML work for HTR, lemmatization, POS tagging, dependency parsing, stylometry, and authorship attribution. The Langton study is the most direct scholastic example because it combines HTR with stylometric analysis of reportationes. These systems operate mainly below the level of argument reasoning.

### Actual formal reasoning

Dutilh Novaes is the strongest direct precedent for formalized medieval reasoning, especially supposition, consequences, and obligationes. The formalization is historically sensitive but not a trained AI system or corpus-scale argument miner. The retained literature contains almost no evaluated LLM system that takes a medieval quaestio/commentary/disputation as input and outputs a provenance-preserving, historically validated argument graph plus a checked inference. Existing scholastic computational work should therefore not be described as “AI reasoning over scholastic texts” without qualification.

## Thin areas and open novelty space

- **Argument-level annotation is sparse.** Existing resources usually stop at text, token, morphology, syntax, lexical links, authorship, or manuscript/transmission metadata. There is little gold data for `quaestio → objections → authorities → sed contra → respondeo → replies`, commentary layers, *sententiae* distinctions, or disputational moves.
- **Reasoning benchmarks are almost absent.** I found no established benchmark that tests an LLM on medieval scholastic arguments with separate scores for textual fidelity, historical interpretation, argument-form recognition, inference validity, and provenance.
- **Formalization is not corpus-scale.** Historical formal logic is comparatively rich at the theory/book level, but formal reconstructions are rarely linked systematically to the exact Latin/Arabic passages, variant editions, manuscript witnesses, and competing scholarly readings.
- **Translation and transmission are under-modeled.** Arabic–Latin and Greek–Latin relations are searchable and digitized in important projects, but computational evaluation of whether a translated argument preserves premise roles, modality, quantification, or warrant is thin.
- **Scholastic genre is underrepresented in NLP.** Aquinas treebanks are valuable, but dependency syntax does not encode the rhetorical/disputational architecture of *quaestiones*, commentaries, quodlibets, or reportationes.
- **LLM work is mostly adjacent, not direct.** General LLM theorem-proving, argument mining, and formalization systems exist, but the retained scholastic/DH sources do not establish reliable transfer to long, multilingual, authority-heavy medieval texts.
- **Provenance and uncertainty need first-class treatment.** HTR errors, editorial normalization, manuscript variants, attribution hypotheses, translation alternatives, and modern formalization choices can all alter the apparent argument. A compact LLM context should preserve these layers rather than collapse them.
- **Novelty should be framed narrowly.** The defensible gap is not “digitize scholastic texts” or “use AI on Aquinas.” It is a provenance-preserving, genre-aware argument representation and evaluation pipeline that connects source passages to alternative argument parses/formalizations and distinguishes historical adequacy from modern logical validity.

## Synthesis for the project

The literature supports a layered architecture:

1. diplomatic image/manuscript and edition witness;
2. HTR/OCR transcription with confidence and correction provenance;
3. normalized/lemmatized Medieval Latin or Arabic–Latin text;
4. syntactic/lexical annotations and cross-resource identifiers;
5. genre-aware segmentation of quaestio/commentary/disputation structure;
6. argument-role and authority-link annotations with alternatives;
7. tradition-specific formalization (where justified), preserving the original passage;
8. executable checks or theorem-prover traces only for the encoded fragment;
9. LLM context assembly that exposes provenance, uncertainty, and rival interpretations.

The strongest evidence level is **probable methodological precedent for the infrastructure and formal layers; unproven for end-to-end AI reasoning over scholastic debate corpora**. The project’s most credible contribution would be the missing middle: argument-form-aware, provenance-preserving context construction connecting medieval source corpora to formal or semi-formal reasoning without treating digitization, parsing, or stylistometry as reasoning.

## Verification and search limitations

- Verified URLs/DOIs were resolved to publisher, ACL Anthology, arXiv, CORDIS, official institutional project, Universal Dependencies, Zenodo, or institutional repository pages.
- Google Scholar pages were used as discovery routes but were not treated as sole evidence because direct Scholar retrieval was unreliable in this environment.
- No claim here should be read as exhaustive: relevant work may be indexed under “Medieval Latin,” “historical NLP,” “digital medieval studies,” “Latin treebanks,” “textual scholarship,” “history of ideas,” or “Arabic–Latin translation” rather than “scholastic AI.”
