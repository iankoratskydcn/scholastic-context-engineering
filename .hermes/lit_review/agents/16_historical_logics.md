# Subtopic 16 — Computational history of logic and formalizing historical logics

**Research date:** 2026-10-11

**Scope.** Scholar-oriented literature on reconstructing historical logics computationally, with five traditions kept in view: Aristotelian, Latin medieval, Islamic/Arabic, Nyāya/Navya-Nyāya, and Mohist. The target is not to claim that these traditions are instances of one modern calculus. It is to identify formalization strategies that preserve historically load-bearing distinctions while making inference, semantics, provenance, and comparison machine-checkable. Discovery used Google Scholar-oriented web queries and publisher/index pages; title, authorship, year, venue, and major claims were checked against the linked scholarly landing pages, DOI records, books, or primary-text repositories. Search snippets were not treated as sole evidence.

## Query variants used

1. `computational history of logic formalization Aristotle syllogistic`
2. `Aristotelian syllogistic computer program formal system Glashoff`
3. `formalizing medieval logical theories Dutilh Novaes`
4. `medieval logic computational formalization supposition consequence`
5. `Arabic Islamic logic formalization Avicenna syllogism`
6. `history of Arabic logic relational syllogisms El-Rouayheb`
7. `Nyaya logic formalization first order type theory`
8. `Navya-Nyaya formalization computational logic`
9. `Mohist Canons logic formalization computation`
10. `historical logic formal languages cognitive formalization`

## Retained papers/books/primary sources (14)

### 1. Aristotle — *Prior Analytics*

**Citation.** Aristotle. *Prior Analytics*, especially Books I–II, in the standard Greek/English scholarly editions and translations. Primary text route: [Perseus Digital Library](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0053).

**Finding.** The *Prior Analytics* supplies the canonical ancient system of categorical syllogistic: terms, premises, figures, moods, conversion, reduction, and demonstrations. A computational reconstruction must distinguish Aristotle's own vocabulary and proof procedures from later predicate-logical recodings.

**Relation to project.** This is the historical source layer for argument templates and deduction traces. It should be represented as an attributed, versioned rule system rather than silently translated into modern first-order logic.

**Limitation.** The text is not a modern formal specification; quantifier scope, existential import, modality, and the status of examples require philological reconstruction. A theorem prover that validates only a modern translation can miss historically intended constraints.

### 2. Corcoran (1974)

**Citation.** John Corcoran. 1974. “Aristotle’s Prior Analytics and the Theory of Syllogism.” In *Ancient Logic and Its Modern Interpretations*, edited by John Corcoran, 7–41. Dordrecht: Reidel. Scholarly record route: [Google Books/WorldCat discovery](https://search.worldcat.org/title/ancient-logic-and-its-modern-interpretations/oclc/1020378).

**Finding.** Corcoran treats Aristotelian syllogistic as a deductive system with rules and derivations rather than as an incomplete precursor to modern logic. The distinction between deductional presentation and semantic/model-theoretic presentation is crucial for historical formalization.

**Relation to project.** Provides a model for preserving the internal proof architecture of a historical calculus and for comparing it with, but not reducing it to, modern systems.

**Limitation.** The reconstruction is focused on Aristotelian syllogistic and does not by itself handle medieval semantic theories, Arabic adaptations, Indian inference, or Mohist argument forms.

### 3. Glashoff (2005)

**Citation.** Klaus Glashoff. 2005. “Aristotelian Syntax from a Computational–Combinatorial Point of View.” *Journal of Logic and Computation* 15(6): 949–973. DOI: [10.1093/logcom/exi048](https://doi.org/10.1093/logcom/exi048). Publisher page: [Oxford Academic](https://academic.oup.com/logcom/article/15/6/949/1086849).

**Finding.** Glashoff formalizes Aristotelian logic with rule-based reduction relations and analyzes the resulting structure computationally, including reproduction of Aristotle’s derivations and a programmatic study of syllogistic rules. The paper explicitly argues that Aristotelian syllogistic can be modeled as a formal system independently of predicate logic and set theory.

**Relation to project.** This is the strongest direct precedent for a computational historical-logic module: typed terms, explicit reduction rules, generated derivations, and structural comparison.

**Limitation.** The formal environment targets Aristotelian syntax and syllogistic; it does not solve the semantic and translation problems of medieval supposition, Arabic relational syllogisms, Navya-Nyāya relational depth, or Mohist paronymy/analogy.

### 4. Dutilh Novaes (2007)

**Citation.** Catarina Dutilh Novaes. 2007. *Formalizing Medieval Logical Theories: Suppositio, Consequentiae and Obligations*. Dordrecht: Springer. DOI: [10.1007/978-1-4020-5853-0](https://doi.org/10.1007/978-1-4020-5853-0).

**Finding.** The book develops formal reconstructions of medieval theories including supposition, consequences, and obligationes, while arguing that formalization is an interpretive tool rather than a neutral transcription. It shows how semantic-pragmatic distinctions can be made explicit without assuming that medieval logic is simply a defective version of modern logic.

**Relation to project.** Supplies the main methodological bridge from historical text to executable representation: formalize a local theory, document interpretive choices, and preserve the relation between linguistic form, semantic role, and inference.

**Limitation.** The focus is primarily Latin medieval material. Arabic and Indian traditions require separate source-sensitive ontologies, and a shared schema must not erase language-specific technical distinctions.

### 5. Broadie (1993)

**Citation.** Alexander Broadie. 1993. *Introduction to Medieval Logic*, 2nd ed. Oxford: Oxford University Press. DOI: [10.1093/acprof:oso/9780198240266.001.0001](https://doi.org/10.1093/acprof:oso/9780198240266.001.0001). Publisher page: [Oxford Academic](https://academic.oup.com/book/6319).

**Finding.** Broadie surveys medieval theories of truth, categorical and molecular propositions, validity conditions, supposition, and syllogistic, including authors such as Burley, Ockham, Buridan, Albert of Saxony, and Paul of Venice. The book shows that medieval logical analysis extends beyond the Aristotelian syllogistic core.

**Relation to project.** Useful as a map for selecting formalization targets and for preventing the corpus from being reduced to syllogism-only examples.

**Limitation.** It is a scholarly synthesis rather than an executable specification. Formalization still requires edition-level text alignment, terminology normalization, and explicit rules for context-sensitive interpretation.

### 6. Dutilh Novaes and Read (eds.) (2016)

**Citation.** Catarina Dutilh Novaes and Stephen Read, eds. 2016. *The Cambridge Companion to Medieval Logic*. Cambridge: Cambridge University Press. DOI/landing page: [Cambridge Core](https://www.cambridge.org/core/books/cambridge-companion-to-medieval-logic/).

**Finding.** The volume emphasizes the connected Latin and Arabic medieval traditions and treats logic as a family of linguistic, semantic, epistemological, and inferential practices. Its introduction warns against overly narrow geographical and chronological boundaries.

**Relation to project.** Supports a graph model of transmission: Greek sources, Syriac/Arabic translation, Latin reception, and internal innovations should be linked by provenance rather than placed in isolated national or civilizational buckets.

**Limitation.** A companion volume provides broad scholarly coverage but not a common machine-readable annotation standard. The project must supply the alignment layer and expose where a relation is historical transmission versus structural analogy.

### 7. Mancosu and Mugnai (2023)

**Citation.** Paolo Mancosu and Massimo Mugnai. 2023. *Syllogistic Logic and Mathematical Proof*. Oxford: Oxford University Press. DOI: [10.1093/oso/9780198876922](https://doi.org/10.1093/oso/9780198876922). See especially “Extensions of the Syllogism in Medieval Logic.”

**Finding.** The authors analyze medieval extensions involving oblique terms, relational sentences, and expository syllogism, including work by Ockham, Buridan, and Albert of Saxony. The discussion shows how medieval logicians tried to accommodate relational reasoning while retaining syllogistic resources.

**Relation to project.** Offers concrete candidate variants beyond categorical syllogism: relational/oblique propositions and expository reasoning can be encoded as separate rule families with historical attribution.

**Limitation.** The book’s focus is the relation between syllogistic and mathematical proof; it does not provide a unified computational treatment across Arabic, Nyāya, and Mohist materials.

### 8. El-Rouayheb (2010)

**Citation.** Khaled El-Rouayheb. 2010. *Relational Syllogisms and the History of Arabic Logic, 900–1900*. Leiden: Brill. DOI: [10.1163/ej.9789004180844.i-366](https://doi.org/10.1163/ej.9789004180844.i-366).

**Finding.** El-Rouayheb reconstructs Arabic logical work on relational syllogisms across a long period, challenging the assumption that Arabic logic merely preserved Greek syllogistic. The work is central evidence for treating Islamic logic as a site of original formal development.

**Relation to project.** Supplies a historically grounded Arabic variant in which relation-sensitive inference is primary. It also motivates a provenance graph that records adaptation, criticism, and independent development.

**Limitation.** The historical argument is not itself a machine-checkable calculus. Arabic technical vocabulary, manuscript variation, and the interaction of logic with grammar and theology remain difficult annotation problems.

### 9. Hodges (2024/2025 publication)

**Citation.** Wilfrid Hodges. 2024. “Avicenna’s Logics with Sentence-Type Terms: 1. Wholly *Muttaṣil* Syllogisms.” *Journal of Logic and Computation* 35(7), published online 31 July 2024 / issue 2025, article exae032. DOI: [10.1093/logcom/exae032](https://doi.org/10.1093/logcom/exae032).

**Finding.** Hodges studies Avicenna’s *Short Epitome in Logic* and its hypothetical logic, where sentence-type terms replace ordinary noun terms. The analysis identifies a system structurally related to categorical syllogistic but with a different term domain and quantificational behavior.

**Relation to project.** This is a strong test case for a typed historical formalizer: the same surface word “syllogism” can conceal a change in term ontology, syntax, and semantics.

**Limitation.** The article treats one Avicennian work and one family of syllogisms. It should not be generalized to Islamic logic as a whole without additional Arabic sources and manuscript/context evidence.

### 10. Matilal (1998)

**Citation.** Bimal Krishna Matilal. 1998. *The Character of Logic in India*. Edited by Jonardon Ganeri and Heeraman Tiwari. Albany: State University of New York Press. Publisher route: [SUNY Press](https://sunypress.edu/Books/T/The-Character-of-Logic-in-India).

**Finding.** Matilal presents Indian logic as a philosophically and linguistically sophisticated tradition whose inferential analysis cannot be adequately represented by importing only Aristotelian or Fregean categories. Nyāya inference involves components such as thesis, reason, example, application, and conclusion, with attention to pervasion (*vyāpti*) and defeaters.

**Relation to project.** Provides the scholarly basis for a Nyāya argument schema that records warrant, example, application, and defeater conditions rather than forcing every inference into a three-line syllogism.

**Limitation.** The book is interpretive and comparative, not a formal specification. Its modern analytic vocabulary must be kept distinct from Sanskrit technical terms and from later Navya-Nyāya developments.

### 11. Ganeri (2001)

**Citation.** Jonardon Ganeri. 2001. *Indian Logic: A Reader*. Richmond, Surrey: Curzon. Publisher/discovery route: [Routledge](https://www.routledge.com/Indian-Logic-A-Reader/Ganeri/p/book/9780700712248).

**Finding.** Ganeri’s reader assembles primary and secondary materials across Indian logical traditions and makes visible the diversity of inference, debate, epistemic sources, and semantic analysis. It is useful for separating Nyāya from Buddhist, Jain, and later Navya-Nyāya positions.

**Relation to project.** Supports corpus construction with passage-level source provenance and tradition labels instead of a single “Indian logic” class.

**Limitation.** A reader does not settle competing translations or provide a canonical formal calculus. Formalization must retain alternative translations and disagreement metadata.

### 12. Panday and Ghosh (2026)

**Citation.** Mrityunjoy Panday and Sudipta Ghosh. 2026. “Cubical Type Theoretic Navya-Nyāya.” arXiv:2605.12548. [arXiv record](https://arxiv.org/abs/2605.12548).

**Finding.** The paper proposes a cubical type-theoretic formalization of Navya-Nyāya, encoding constructs including relation, delimitor (*avacchedaka*), absence (*abhāva*), pervasion (*vyāpti*), identity, higher relations, and qualifier–qualificand structure. It reports internal theorems and metatheoretic results, while comparing with first-order, higher-order, and Martin-Löf type-theoretic attempts.

**Relation to project.** This is the clearest current computational precedent for preserving historically load-bearing structure rather than flattening Navya-Nyāya into ordinary first-order predicates. It suggests dependent types or typed relational graphs for the project’s intermediate representation.

**Limitation.** It is a recent preprint and focuses on Navya-Nyāya, not the full Nyāya corpus or cross-tradition evaluation. Its formal choices require independent philological validation against primary Sanskrit commentaries.

### 13. Graham (1978)

**Citation.** A. C. Graham. 1978. *Later Mohist Logic, Ethics and Science*. Hong Kong: Chinese University Press. Bibliographic route: [WorldCat](https://search.worldcat.org/title/later-mohist-logic-ethics-and-science/oclc/4495009).

**Finding.** Graham’s translation and analysis of the Later Mohist Canons reconstructs a Chinese argumentative tradition involving distinctions, definitions, analogy, disputation, names, and empirical/technical reasoning. The material is not naturally identical to Aristotelian syllogistic, even where modern readers can identify inferential regularities.

**Relation to project.** Mohist material should be represented as a family of lexical, analogical, classificatory, and disputational operations, with primary Chinese text, translation alternatives, and commentary linked to each rule.

**Limitation.** The Canons are terse, textually difficult, and dependent on emendation and commentary. A computational model risks encoding Graham’s reconstruction as if it were uncontroversial primary meaning.

### 14. Dutilh Novaes (2012)

**Citation.** Catarina Dutilh Novaes. 2012. *Formal Languages in Logic: A Philosophical and Cognitive Analysis*. Cambridge: Cambridge University Press. DOI/landing page: [Cambridge Core](https://www.cambridge.org/core/books/formal-languages-in-logic/7D1DD805F7B3C70A0C32F2F6A66BE3DD).

**Finding.** Dutilh Novaes argues for a broad conception of formal language and studies the cognitive, historical, and logical functions of formalization. The historical record shows that sophisticated logical practices need not use modern formal languages.

**Relation to project.** Supplies the general methodological guardrail: formalization should be evaluated by what it makes explicit, what it preserves, and what it suppresses. A compact context representation can therefore be formal without pretending to be tradition-neutral.

**Limitation.** The book is methodological rather than a complete computational pipeline. It does not specify data models, theorem-prover interfaces, or evaluation benchmarks for the five traditions.

## Formalization variants to retain (8)

1. **Aristotelian rule-reduction calculus:** typed terms, categorical forms, figures/moods, conversion, and reduction traces; benchmark with generated valid/invalid syllogisms.
2. **Aristotelian modal syllogistic:** add necessity/possibility operators and track whether modal readings are textual, reconstructed, or modernized.
3. **Latin medieval semantic logic:** model supposition, ampliation/restriction, syncategoremata, and context-sensitive reference; retain competing analyses rather than one normalized paraphrase.
4. **Medieval consequence/obligationes:** represent inference under stipulated cases, commitment sets, retraction rules, and paradoxical or insoluble cases.
5. **Arabic/Islamic relational and hypothetical logic:** separate Aristotelian inheritance from Avicennian and later developments; support relational terms, sentence-type terms, and Arabic technical vocabulary.
6. **Nyāya five-member inference:** thesis, reason, example, application, conclusion, with *vyāpti*, defeaters, epistemic source, and debate status explicitly represented.
7. **Navya-Nyāya typed relational language:** dependent delimitation, typed absence, non-extensional identity, qualifier–qualificand structure, and unbounded relational depth; candidate implementation in dependent/cubical type theory.
8. **Mohist Canons/disputation:** lexical distinctions, definition, analogy, classification, counterexample, and disputational moves with primary-text and translation provenance.

## Cross-tradition relation to the project

The shared computational object should be a **provenance-preserving argument record**, not a universal logic. Each record can contain: source passage and edition; language and translation; tradition and date range; premises/claims; inferential operation; semantic commitments; defeaters or exceptions; confidence; formal encoding; proof/check result; and unresolved scholarly alternatives. This supports comparison at several levels: surface argument structure, rule behavior, semantic commitments, and proof-theoretic properties.

The strongest common denominator is not “all traditions are syllogistic.” It is that each tradition provides explicit or reconstructable constraints on acceptable transitions from linguistic material to conclusion. The computational task is therefore to model **historically typed transitions** and to keep the mapping from source text to formal rule inspectable.

## Limitations and thin areas

- **Philology versus executable form.** Most historical-logical scholarship gives arguments for interpretation, not machine-readable corpora. Edition alignment, manuscript variants, translation alternatives, and commentary dependencies are first-class data requirements.
- **Category mismatch.** “Logic,” “inference,” “grammar,” “debate,” and “epistemology” do not divide the five traditions in the same way. A single ontology risks imposing modern boundaries.
- **Uneven computational maturity.** Aristotelian syllogistic has mature rule-based reconstructions; Navya-Nyāya now has ambitious type-theoretic work; Latin medieval semantics has substantial formal scholarship; Arabic and Mohist traditions have much less interoperable executable modeling.
- **Arabic/Islamic undercoverage.** Relational syllogisms and Avicenna are strong anchors, but the field remains too often represented by a few figures. Later Arabic, Persian, Ottoman, and Jewish-Arabic logical work needs broader computational treatment.
- **Nyāya primary-text gap.** Modern formal work often targets Navya-Nyāya technical language, while the historical relation among early Nyāya, Buddhist logic, Jain logic, and later Navya-Nyāya remains underrepresented in executable datasets.
- **Mohist thinness.** The Later Mohist Canons are textually compressed and heavily mediated by reconstruction. There is no widely accepted benchmark suite comparable to syllogistic validity tables.
- **Evaluation gap.** Existing work tends to prove properties of one formalization or explain one historical system. Cross-tradition tests for faithfulness, translation variance, annotator agreement, and resistance to anachronism are largely absent.
- **LLM-specific gap.** Few studies connect historical formalizations to retrieval, context compression, or model evaluation. A promising experiment is to compare modern LLM reasoning over raw translations versus provenance-preserving structured records, while scoring both logical validity and historical fidelity.

## Recommended computational design

Use a layered representation: (1) diplomatic/source text; (2) scholarly translation and segmentation; (3) tradition-specific argument schema; (4) executable rule or type-theoretic encoding; (5) proof/check trace; and (6) uncertainty and disagreement record. Run at least two formal encodings where possible—e.g., Aristotelian reduction rules versus first-order semantics, and Navya-Nyāya dependent types versus a relational graph—to expose what each encoding loses. Do not report a successful proof as proof that the historical author endorsed the modern formalization; report it as a property of the stated reconstruction.

## Sources and verification notes

The 14 retained entries above are scholarly books, journal articles, primary texts, or research preprints with identifiable authorship, title, year/publication status, and publisher/repository route. The strongest directly computational sources are Glashoff (2005), Dutilh Novaes (2007, 2012), Hodges (2024/2025), and Panday & Ghosh (2026). The strongest historical/primary anchors are Aristotle, Graham, Matilal/Ganeri’s source collections, and El-Rouayheb’s Arabic-logical history. The 2026 Navya-Nyāya and 2026 project-adjacent LLM work should be treated as frontier/preprint evidence, not settled consensus.

**Search limitation.** Google Scholar result pages were not reliably directly fetchable in this environment; Scholar-style queries were used for discovery, while publisher pages, DOI records, books, primary-text repositories, and arXiv records were used for verification. No claim above depends solely on a search-result snippet.
