# Search angle 4 — AI/NLP/computational work on Islamic, Jewish, Christian, and comparative scholastic traditions

**Scope.** Searches covered Islamic kalām and falsafa, medieval Arabic logic, Islamic legal/theological reasoning, Jewish/Hebrew textual scholarship, Christian medieval scholasticism, computational humanities, argument mining, formalization, knowledge representation, and LLMs. Sources were opened or directly retrieved on 11 October 2026; PDF endpoints were checked for successful retrieval where applicable.

## Bottom line

The **exact intersection of AI/NLP with historical kalām, medieval Arabic logic, or comparative scholastic argument is sparse**. The strongest directly relevant work is computational formalization of medieval Arabic logical procedures and computational work on premodern Arabic corpora; recent LLM work is concentrated on broad Islamic knowledge, Qur’an/Hadith QA, Islamic humanities knowledge graphs, or legal reasoning rather than historically faithful modeling of kalām debates. Christian scholasticism has a small but real computational-humanities literature, mostly stylometry, textual relatedness, authorship, and corpus construction—not argument mining. Jewish scholastic argument is still underrepresented as an explicit computational-AI research area; Hebrew NLP and Biblical-text computation provide enabling infrastructure but are not equivalent to formal analysis of medieval Jewish philosophical disputation.

## Verified sources and relevance

1. **Hodges, “Ibn Sīnā on analysis: 1. Proof search. Or: Abstract State Machines as a tool for history of logic.”** This is the clearest direct bridge between medieval Arabic logic and computer-science formalization: it interprets a passage in Avicenna’s *Qiyās* as a proof-search algorithm for syllogisms and models the procedure with Abstract State Machines. It is historical logic formalization, not machine-learned NLP, but it supplies a concrete representation target for computational studies of Arabic logical texts. [1]

2. **“A Correctness Proof for al-Barakāt’s Logical Diagrams.”** The article reconstructs and proves correct a procedure proposed by Abū al-Barakāt for finding conclusions of premise-pairs and identifying pairs with no conclusion. This is a formal/computationally legible account of a twelfth-century Arabic logical system; it could support executable theorem-prover or symbolic-AI implementations, although the paper itself is not an NLP system. [2]

3. **“The Algorithm of Islamic Jurisprudence (Fiqh) with Validation of an Entscheidungsproblem.”** This preprint translates aspects of fiqh methodology into mathematical-logic and computer-science terms, proposing a logic-query language and discussing decision-problem validation. It is adjacent to kalām rather than a study of kalām proper, but it is directly relevant to formalization of Islamic scholastic reasoning and to rule-based/knowledge-representation approaches. Treat its broad claims cautiously because it is a preprint rather than a mature benchmarked NLP paper. [3]

4. **“Computational Extraction of Legal Causes via al-Ṣabr wa al-Taqsīm: A Set-Theoretic Formalization for Closed Fiqh Chapters.”** This paper formalizes the classical uṣūl al-fiqh method of examination-and-division as a set-theoretic extraction procedure. It demonstrates how a premodern Islamic reasoning technique can be represented algorithmically, while also showing the current literature’s tendency to target jurisprudence rather than theological disputation. [4]

5. **Maliszewski, “It takes a village to write a book: mapping anonymous contributions in Stephen Langton’s *Quaestiones Theologiae*.”** This registered-report/protocol applies stylometry and computational authorship analysis to a Christian scholastic theological corpus produced through reportationes. It is not argument mining, but it is a verified computational study of medieval scholastic theology and a useful model for separating textual layers, contributors, and transmission histories before attempting semantic or argumentative modeling. [5][6]

6. **Text Mining Islamic Law, *Islamic Law and Society* 28(3).** This essay surveys the place of digital humanities and text mining in Islamic legal studies. Its importance for this search is infrastructural: Islamic studies has substantial opportunities for corpus construction, OCR/HTR, metadata, and text mining, but these methods have not yet become mainstream enough to yield a mature computational literature on kalām argument structure. [7]

7. **OpenITI (Open Islamicate Texts Initiative).** OpenITI is a machine-actionable scholarly corpus initiative for premodern Arabic and other Islamicate texts. It is not a single AI paper, but it is a foundational resource for training, retrieval, citation-network analysis, authorship studies, terminology extraction, and future argument-mining work across kalām, falsafa, fiqh, and related traditions. Corpus quality, edition alignment, genre labels, and theological-text coverage remain important research questions. [8]

8. **Yousef et al., “Enhancing State-of-the-Art NLP Models for Classical Arabic.”** This paper evaluates and improves NLP models for Classical Arabic, directly relevant to historical Islamic texts. It addresses the domain shift between modern/news Arabic and premodern/classical material; the work is language technology rather than theology, but it provides the modeling baseline needed before extracting premises, objections, replies, and authorities from kalām texts. [9]

9. **“A Pilot PropBank Annotation for Quranic Arabic.”** This ACL workshop paper creates predicate-argument annotations for Qur’anic Arabic. It is not a study of kalām, but semantic-role resources of this kind are a prerequisite for argument mining and knowledge representation in Arabic religious texts, especially where syntactic and semantic relations must be distinguished from later theological interpretation. [10]

10. **“Challenging the Transformer-based models with a Classical Arabic dataset: Quran and Hadith.”** This LREC paper tests transformer models on Classical Arabic Qur’an and Hadith data and documents the difficulty of transferring modern-Arabic performance to religious/classical genres. It offers a relevant warning for LLM prompting and evaluation: high scores on contemporary Arabic tasks do not establish competence with premodern religious language or scholastic reasoning. [11]

11. **“HAQA and QUQA: Constructing Two Arabic Question-Answering Corpora for the Quran and Hadith.”** This paper constructs Arabic QA resources for Qur’an and Hadith. These datasets are not argument-mining corpora and do not encode kalām debates, but they are among the closest established resources for testing retrieval, answer extraction, faithfulness, and domain-specific LLM behavior on Islamic textual traditions. [12]

12. **“Computational Linguistic Analysis of the Biblical Text,” in *The Digital Bible: A Practical Guide to Digital Humanities and Biblical Studies*.** This chapter surveys computational approaches to Biblical Hebrew and related textual analysis, including rule-based and corpus methods. It represents enabling infrastructure for computational Jewish and Christian textual scholarship, but it should not be misread as evidence that medieval Jewish scholastic argument has already been computationally modeled. [13]

13. **“What’s Wrong with Hebrew NLP? And How to Make it Right.”** This paper diagnoses Hebrew NLP limitations and presents a formal framework and computational machinery for Hebrew linguistic analysis. It is relevant to Jewish scholastic research because medieval Jewish philosophical and theological sources require historically and morphologically aware Hebrew processing; however, the paper is language-infrastructure work, not argument mining of rabbinic or scholastic disputation. [14]

14. **“Explainable Large Language Model for Islamic and Humanities Sciences Based on Knowledge Graphs.”** The article explicitly proposes combining knowledge graphs and LLMs for Islamic studies and humanities, with keywords including logic, conceptual inference, and explainability. It is one of the closest matches to the requested knowledge-representation/LLM angle, but its evidentiary value is primarily as a design proposal; the report should distinguish conceptual architecture from a validated benchmark on historical kalām. [15]

15. **“Islamic Large Language Models: From Knowledge Acquisition to Trustworthy and Hallucination-Resistant AI.”** This recent survey organizes work around Arabic NLP/LLMs, Islamic NLP resources, Qur’anic QA, Islamic knowledge benchmarks, retrieval-augmented generation, Islamic legal reasoning, and hallucination evaluation. It confirms that current AI work is growing around Islamic knowledge broadly, while also reinforcing the gap in historically grounded, argument-structured modeling of kalām, falsafa, and cross-tradition scholastic debate. [16]

16. **Argument-mining methodology: Lawrence and Reed, “Argument Mining: A Survey.”** This is a general computational-argumentation survey rather than a religious-studies paper. It is retained as a methodological anchor because it defines the task family—identifying argumentative components and relations—and clarifies what would be required to move from OCR/semantic retrieval to formal extraction of scholastic objections, premises, rebuttals, distinctions, and conclusions. It should be paired with domain-specific corpora rather than treated as evidence of existing kalām systems. [17]

## Evidence assessment by requested angle

- **Formalization:** strongest evidence exists for Avicenna’s proof-search procedure, al-Barakāt’s logical diagrams, and formalized uṣūl al-fiqh methods. These are symbolic or mathematical reconstructions, not end-to-end AI systems. [1][2][3][4]
- **Argument mining:** general argument-mining methods are mature enough to transfer in principle, but I found no well-established, openly benchmarked corpus specifically annotated for kalām, medieval Arabic disputation, medieval Jewish scholastic argument, or Christian *quaestiones*. The Langton work demonstrates computational analysis of a Christian scholastic corpus, but primarily authorship/textual transmission. [5][6]
- **Knowledge representation:** OpenITI supplies corpus infrastructure, while the Islamic-humanities knowledge-graph/LLM article supplies an explicit architecture proposal. A validated ontology of theological positions, authorities, objections, modal qualifiers, and dialectical relations remains an open gap. [8][15]
- **LLM prompting/evaluation:** Islamic LLM and Qur’an/Hadith QA work is expanding, but most evaluated tasks are QA, retrieval, morphology, semantic parsing, or broad cultural/religious knowledge. These should not be equated with historically faithful reasoning over kalām arguments. [9][10][11][12][15][16]
- **Comparative traditions:** Christian computational scholasticism and Hebrew/Biblical NLP offer transferable methods, but there is little direct comparative AI work aligning Islamic kalām, Jewish scholasticism, and Christian scholastic *quaestiones* in one representation or benchmark. [5][6][13][14]

## Research gap / recommended next step

The exact AI literature is **sparse and fragmented**. A feasible research program would begin with a small, expert-annotated multilingual corpus of parallel argumentative units from kalām, Arabic falsafa, Jewish philosophy, and Latin scholastic *quaestiones*. Annotation should separate: (1) issue/question, (2) thesis, (3) objection, (4) premise or authority, (5) inference rule, (6) reply/rebuttal, (7) distinction/qualification, and (8) citation or intertextual link. A hybrid pipeline—HTR/OCR and normalization, retrieval over OpenITI-like corpora, symbolic argument graphs, and LLM extraction constrained by the schema—would be more defensible than prompting an LLM to “reason like” a historical theologian. Evaluation should include expert agreement, source-grounded citation accuracy, cross-lingual entity alignment, and adversarial tests for anachronism and fabricated authorities.

## Sources

The numbered citations above map to the following verified URLs:

[1] https://wilfridhodges.co.uk/arabic05.pdf  
[2] https://www.cambridge.org/core/journals/review-of-symbolic-logic/article/abs/correctness-proof-for-albarakats-logical-diagrams/6345C259CB7CD88CF9753FF26001FB61  
[3] https://arxiv.org/abs/1604.00266  
[4] https://jacad.eth.limo/rc_images/abdelwahab_3_18_15_1.pdf  
[5] https://arxiv.org/html/2508.12830v1  
[6] https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9A1A9C2B789EC1AD7A876F65F5D90CCC/S2977815825100043a.pdf/it_takes_a_village_to_write_a_book_mapping_anonymous_contributions_in_stephen_langtons_quaestiones_theologiae.pdf  
[7] https://brill.com/view/journals/ils/28/3/article-p234_234.xml?language=en  
[8] https://alraqmiyyat.github.io/OpenITI  
[9] https://aclanthology.org/2023.alp-1.19.pdf  
[10] https://aclanthology.org/W12-2511.pdf  
[11] https://aclanthology.org/2022.lrec-1.157.pdf  
[12] https://aclanthology.org/2023.ranlp-1.10.pdf  
[13] https://books.openbookpublishers.com/10.11647/obp.0358.05.pdf  
[14] https://ar5iv.labs.arxiv.org/html/1908.05453  
[15] https://stim.qom.ac.ir/article_3085.html?lang=en  
[16] https://arxiv.org/abs/2606.16629  
[17] https://aclanthology.org/J19-4006.pdf

## Verification notes

- 17 sources were registered in the citation ledger; direct retrieval succeeded for the arXiv/ACL/Cambridge/HTML endpoints used above, while one Brill page was access-restricted during automated retrieval but its bibliographic landing page and search result were verified.
- The sources deliberately mix direct matches, adjacent computational humanities, and enabling NLP infrastructure. The report labels these differences rather than presenting all 17 as direct kalām-AI studies.
- No claim is made that the listed papers establish a mature field; the principal finding is the opposite: relevant work exists, but it is mostly foundational, adjacent, or symbolic rather than benchmarked AI for comparative scholastic argument.

