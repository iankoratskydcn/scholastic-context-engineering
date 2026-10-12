# Subtopic 8 — LLMs with formal logic, theorem provers, and logic–LM hybrids

- **Research date:** 2026-10-11
- **Scope:** LLM/neuro-symbolic systems that translate, classify, select, construct, verify, or refine logical arguments using formal logic, automated theorem provers, proof assistants, SAT/SMT solvers, or retrieval over formal libraries.
- **Verified paper count:** 11
- **Primary discovery route:** Google Scholar was attempted first; Scholar search results were sparse/noisy and returned an unrelated author profile for broad queries. Fallback routes were ACL Anthology, arXiv, OpenReview/ICLR, and paper PDFs. Every item below was checked against an actual abstract/full-paper page or PDF, not only a search snippet.
- **Key novelty question:** Do prior logic–LM/theorem-prover hybrids perform **argument-form classification/extraction specifically for context selection or context construction**?

## Direct novelty-threat ranking

1. **Quan et al. (2024), Explanation-Refiner — strongest direct overlap.** The paper explicitly asks an LLM to produce a rough inference, identify sufficient/necessary explanatory facts, remove redundant or irrelevant facts, construct a formal theory, and use Isabelle/HOL feedback to refine the explanation. This is an argument-form/context-construction pipeline: natural-language explanatory sentences become axioms, a selected subset becomes proof context, and the prover validates the resulting derivation. It is not merely theorem proving; it operationalizes relevant-vs-irrelevant sentence selection for NLI explanations.
2. **Logic-LM (Pan et al., 2023) — strong adjacent overlap.** The LLM converts a natural-language problem—including premises and conclusion—into a symbolic formulation and iteratively repairs it using solver errors. It constructs formal reasoning context, but the paper does not present a dedicated argument-form classifier or an explicit retrieval/selection stage over candidate context sentences.
3. **LINC (Olausson et al., 2023) — strong adjacent overlap.** The LLM is a semantic parser from natural-language premises/conclusions to FOL, followed by Prover9-style deduction. It extracts argument content into formal premises, but does not specialize in selecting a minimal context or classifying argument forms for context construction.
4. **LeanDojo/ReProver (Yang et al., 2023) — direct on context selection, different input regime.** ReProver retrieves premises from a large formal Lean/mathlib library; fine-grained proof-premise annotations supervise selection. This is a clear context-selection mechanism, but it selects formal lemmas for theorem proving rather than extracting argument forms or relevant natural-language sentences from prose.
5. **Magnushammer (Mikuła et al., 2024) — direct on premise selection, indirect on novelty.** It learns transformer-based retrieval of relevant premises from proof states and combines the retriever with an LLM theorem prover. It is highly relevant if “context construction” includes formal-library retrieval, but not if the novelty requires natural-language argument-form classification.
6. **Logic-LM++ (Kirtania et al., 2024) — refinement overlap.** It improves Logic-LM by comparing candidate symbolic refinements and selecting better formulations. This is selection among formalizations, not explicit argument-form extraction or context retrieval.
7. **LogicLLaMA/MALLS (Yang et al., 2024) — sentence-level extraction/formalization overlap.** MALLS is a large verified collection of sentence-level NL–FOL pairs; LogicLLaMA is fine-tuned to translate and correct formal rules. It supplies the translation component needed for argument extraction, but does not itself build a selected context or prove a target argument.
8. **Automated Theorem Provers Help Improve LLM Reasoning (McGinness & Baumgartner, 2024) — correction overlap.** The LLM translates problems to formal logic, ATPs diagnose syntactic/semantic errors, and ATPs help correct semantic errors. Relevant to proof-relevant context validation, but no dedicated argument-form classifier or context selector is reported.
9. **LeanReasoner (Jiang et al., 2024) — formal-context overlap.** It formalizes FOLIO/ProofWriter tasks as Lean theorems and uses Lean’s symbolic checking/library. The formalization creates a theorem context, but the contribution is theorem proving rather than explicit argument extraction or relevance selection.
10. **Lean Copilot (Song et al., 2024) — premise-selection overlap.** It exposes LLM-based tactic suggestion, proof search, and relevant-premise selection inside Lean. It is relevant as a formal-context selection baseline, but it operates over Lean goals and library premises, not natural-language argument forms.
11. **LoGiPT / Language Models can be Deductive Solvers (Feng et al., 2024) — logic-solver imitation, weak direct overlap.** It trains a language model to emulate deductive solvers with strict syntax/grammar, avoiding an external parsing stage. It addresses logical-form execution but not explicit argument-form classification, extraction, or context selection.

## Verified papers

### 1. Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning
- **Authors:** Liangming Pan, Alon Albalak, Xinyi Wang, William Yang Wang
- **Year/venue:** 2023, Findings of EMNLP
- **Links:** https://aclanthology.org/2023.findings-emnlp.248/ ; https://arxiv.org/abs/2305.12295
- **What was verified:** The abstract states that an LLM translates a natural-language problem into a symbolic formulation; a deterministic symbolic solver performs inference; solver error messages drive self-refinement. Evaluated on ProofWriter, PrOntoQA, FOLIO, LogicalDeduction, and AR-LSAT.
- **Relevance:** Formal context construction and solver-validated logical reasoning.
- **Novelty assessment:** Strong adjacent threat; no dedicated relevance classifier/minimal-context selector identified in the verified paper description.

### 2. LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers
- **Authors:** Theo Olausson, Alex Gu, Ben Lipkin, Cedegao Zhang, Armando Solar-Lezama, Joshua Tenenbaum, Roger Levy
- **Year/venue:** 2023, EMNLP
- **Links:** https://aclanthology.org/2023.emnlp-main.313/ ; https://arxiv.org/abs/2310.15164
- **What was verified:** The LLM acts as a semantic parser translating natural-language premises and conclusions into FOL; the expressions are passed to an external theorem prover. Experiments cover FOLIO and ProofWriter.
- **Relevance:** Natural-language argument extraction into formal premises and conclusions.
- **Novelty assessment:** Strong adjacent threat; extraction is central, but explicit context selection/classification is not the main contribution.

### 3. Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving (Explanation-Refiner)
- **Authors:** Xin Quan, Marco Valentino, Louise A. Dennis, André Freitas
- **Year/venue:** 2024, EMNLP
- **Links:** https://aclanthology.org/2024.emnlp-main.172/ ; https://arxiv.org/abs/2405.01379 ; PDF: https://aclanthology.org/2024.emnlp-main.172.pdf
- **What was verified:** The paper’s full PDF describes a pipeline where the LLM generates a rough inference and elicits sufficient/necessary facts; it identifies relevant, redundant, and unrelated explanatory sentences; selected facts become axioms; Isabelle/HOL verifies the constructed proof and returns feedback for iterative refinement. The framework uses Neo-Davidsonian event semantics plus FOL and evaluates e-SNLI, QASC, and WorldTree.
- **Relevance:** Exact prior art for argument-form extraction and proof-relevant context construction.
- **Novelty assessment:** Highest direct overlap. Any proposed system claiming to classify/extract argument forms for selecting or constructing context must clearly distinguish its task, representation, selection objective, and evaluation from Explanation-Refiner.

### 4. LeanDojo: Theorem Proving with Retrieval-Augmented Language Models
- **Authors:** Kaiyu Yang, Aidan M. Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan Prenger, Anima Anandkumar
- **Year/venue:** 2023, arXiv/preprint and later research ecosystem
- **Link:** https://arxiv.org/abs/2306.15626
- **What was verified:** LeanDojo extracts proof data from Lean, provides fine-grained premise annotations, and introduces ReProver, an LLM-based prover with retrieval for selecting premises from a large math library. The benchmark contains 98,734 theorems/proofs.
- **Relevance:** Formal premise retrieval and construction of compact proof context.
- **Novelty assessment:** Direct context-selection threat in formal mathematics; not a natural-language argument-form extractor.

### 5. Magnushammer: A Transformer-Based Approach to Premise Selection
- **Authors:** Maciej Mikuła, Szymon Tworkowski, Szymon Antoniak, Bartosz Piotrowski, Albert Qiaochu Jiang, Jin Peng Zhou, Christian Szegedy, Łukasz Kuciński, Piotr Miłoś, Yuhuai Wu
- **Year/venue:** 2024, ICLR
- **Links:** https://proceedings.iclr.cc/paper_files/paper/2024/hash/ab5f5f22e3e09f4424592ffb06840ab0-Abstract-Conference.html ; https://arxiv.org/abs/2303.04488
- **What was verified:** The paper presents contrastively trained transformer retrieval for premise selection in automated theorem proving, compares against Sledgehammer, and combines Magnushammer with a language-model prover. It releases proof-state/relevant-premise pairs for Isabelle.
- **Relevance:** Explicit proof-context/premise selection.
- **Novelty assessment:** Direct if the target contribution is formal-premise retrieval; indirect if the target is natural-language argument-form extraction.

### 6. Towards Large Language Models as Copilots for Theorem Proving in Lean (Lean Copilot)
- **Authors:** Peiyang Song, Kaiyu Yang, Anima Anandkumar
- **Year/venue:** 2024, arXiv/preprint
- **Link:** https://arxiv.org/abs/2404.12534
- **What was verified:** The abstract states that Lean Copilot supports tactic suggestion, proof search, and relevant-premise selection using LLMs integrated into Lean.
- **Relevance:** Interactive formal context selection and proof assistance.
- **Novelty assessment:** Direct formal-premise baseline; no natural-language argument-form classifier is the paper’s central mechanism.

### 7. Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation (MALLS/LogicLLaMA)
- **Authors:** Yuan Yang, Siheng Xiong, Ali Payani, Ehsan Shareghi, Faramarz Fekri
- **Year/venue:** 2024, ACL
- **Link:** https://aclanthology.org/2024.acl-long.375/
- **What was verified:** The ACL page reports MALLS, a 28K sentence-level NL–FOL dataset with human/automatic filtering, and LogicLLaMA models fine-tuned for NL–FOL translation and correction of generated rules.
- **Relevance:** Sentence-level logical-form extraction, a component of argument-form classification/construction.
- **Novelty assessment:** Moderate adjacent threat; no dedicated proof-relevant sentence selection or end-to-end context construction is established in the verified abstract.

### 8. LOGIC-LM++: Multi-Step Refinement for Symbolic Formulations
- **Authors:** Shashank Kirtania, Priyanshu Gupta, Arjun Radhakrishnan
- **Year/venue:** 2024, arXiv/preprint
- **Link:** https://arxiv.org/abs/2407.02514
- **What was verified:** The abstract describes multi-step refinement of formal specifications, using LLM pairwise comparisons to evaluate candidate refinements, with gains over Logic-LM on FOLIO, ProofWriter, and AR-LSAT.
- **Relevance:** Selection/refinement among competing symbolic formulations.
- **Novelty assessment:** Moderate adjacent threat; closer to formalization refinement than argument-form extraction or context retrieval.

### 9. Automated Theorem Provers Help Improve Large Language Model Reasoning
- **Authors:** Lachlan McGinness, Peter Baumgartner
- **Year/venue:** 2024, arXiv; also published in LPAR 2024 proceedings
- **Link:** https://arxiv.org/abs/2408.03492
- **What was verified:** The paper uses an LLM as a front-end translating problems into formal logic, then applies logic programming/first-order ATPs. It defines syntactic and semantic translation-error categories and uses ATPs for semantic error correction on PRONTOQA steamroller problems.
- **Relevance:** Formalization, error diagnosis, and prover-guided repair.
- **Novelty assessment:** Moderate adjacent threat; not an explicit argument-form/context selector.

### 10. LeanReasoner: Boosting Complex Logical Reasoning with Lean
- **Authors:** Dongwei Jiang, Marcio Fonseca, Shay B. Cohen
- **Year/venue:** 2024, NAACL
- **Link:** https://aclanthology.org/2024.naacl-long.416/
- **What was verified:** The ACL abstract states that logical reasoning problems are formalized as Lean theorems and solved by proving/disproving them, leveraging Lean’s symbolic solver and theorem library; results are reported on FOLIO and ProofWriter with fewer than 100 in-domain samples per dataset.
- **Relevance:** LLM-to-proof-assistant formalization and proof-library use.
- **Novelty assessment:** Moderate/weak direct threat; no dedicated argument-form classification or context-selection mechanism identified in the abstract.

### 11. Language Models can be Deductive Solvers (LoGiPT)
- **Authors:** Jiazhan Feng, Ruochen Xu, Junheng Hao, Hiteshi Sharma, Yelong Shen, Dongyan Zhao, Weizhu Chen
- **Year/venue:** 2024, Findings of NAACL
- **Links:** https://aclanthology.org/2024.findings-naacl.254/ ; https://arxiv.org/abs/2311.06158
- **What was verified:** The ACL page states that LoGiPT directly internalizes/emulates logical-solver reasoning, learns strict solver syntax/grammar, and avoids the parsing failures of solver-augmented pipelines. It is trained from revealed/refined deductive-solver reasoning and evaluated on two deductive benchmarks.
- **Relevance:** Logic–LM hybrid architecture and formal-syntax adherence.
- **Novelty assessment:** Weak direct threat for context construction; it intentionally removes the explicit parser/selector stage.

## Novelty synthesis

The most important prior-art distinction is between three kinds of “context”:

1. **Natural-language argument context:** candidate sentences/facts/explanations are classified as relevant, redundant, unrelated, sufficient, or necessary for a target conclusion. **Explanation-Refiner is the closest verified precedent**, because it explicitly elicits relevant facts, drops redundant/irrelevant facts, constructs axioms, and validates the selected proof context.
2. **Formalized problem context:** all or most natural-language premises/conclusions are converted into FOL/Lean/solver syntax. Logic-LM and LINC are the principal precedents. They threaten claims about LLM-to-formal-argument extraction, but not necessarily claims about selective context construction.
3. **Formal-library context:** a retriever selects relevant lemmas/premises from a theorem-prover library. LeanDojo/ReProver, Magnushammer, and Lean Copilot are the principal precedents. They threaten claims about proof-premise retrieval, but their inputs are formal proof states/library declarations rather than unstructured natural-language arguments.

A genuinely differentiated contribution should therefore specify whether it introduces: (a) a new argument-form taxonomy/classifier; (b) extraction of argumentative relations rather than sentence-level FOL translation; (c) selection of proof-relevant context under a stated objective such as sufficiency, minimality, coverage, or faithfulness; (d) a cross-domain or long-context setting; or (e) a new interface between selected natural-language context and a prover. The paper must compare directly against Explanation-Refiner, Logic-LM/LINC, and at least one formal-premise retriever (LeanDojo/ReProver or Magnushammer).

## Search log and failed searches

- **Google Scholar, query:** `site:scholar.google.com "logic" "theorem prover" large language models` — did not yield a usable paper-result list; surfaced an unrelated Google Scholar author profile and unrelated theorem-prover citations.
- **Google Scholar, query:** `site:scholar.google.com "Logic-LM"` — no directly usable Scholar result was returned by the search backend.
- **Google Scholar, query:** `site:scholar.google.com "premise selection" theorem proving language model` — no stable paper-result page was returned; fallback used OpenReview/ICLR and arXiv.
- **Google Scholar, query:** `site:scholar.google.com "argument extraction" logic language model` — no usable result list; fallback broadened to ACL Anthology and general web search.
- **Fallback query variants used:** `Logic-LM language models formal logic theorem prover`; `LINC language models theorem proving natural language inference`; `LeanDojo theorem proving premise selection language models`; `argument extraction context construction theorem proving language model`; `LLM formal theorem proving premise selection context retrieval`; `natural language theorem proving first-order logic semantic parsing`; `LLM symbolic theorem prover explanation refinement`.
- **Retrieval issue:** the configured `web_extract` backend could not extract arXiv URLs and returned an explicit backend error. This was bypassed by using the web search/open route for ACL, arXiv, OpenReview, and PDF pages; the Explanation-Refiner full PDF was successfully inspected through the open-PDF route.
- **Stopping rule:** stopped at 11 verified papers after coverage of (i) LLM→FOL/prover translation, (ii) prover-guided refinement, (iii) natural-language explanation/context selection, and (iv) formal-premise retrieval.

## Source list

1. Pan et al. (2023), ACL Anthology: https://aclanthology.org/2023.findings-emnlp.248/
2. Olausson et al. (2023), ACL Anthology: https://aclanthology.org/2023.emnlp-main.313/
3. Quan et al. (2024), ACL Anthology/PDF: https://aclanthology.org/2024.emnlp-main.172/
4. Yang et al. (2023), arXiv: https://arxiv.org/abs/2306.15626
5. Mikuła et al. (2024), ICLR: https://proceedings.iclr.cc/paper_files/paper/2024/hash/ab5f5f22e3e09f4424592ffb06840ab0-Abstract-Conference.html
6. Song et al. (2024), arXiv: https://arxiv.org/abs/2404.12534
7. Yang et al. (2024), ACL Anthology: https://aclanthology.org/2024.acl-long.375/
8. Kirtania et al. (2024), arXiv: https://arxiv.org/abs/2407.02514
9. McGinness & Baumgartner (2024), arXiv: https://arxiv.org/abs/2408.03492
10. Jiang et al. (2024), ACL Anthology: https://aclanthology.org/2024.naacl-long.416/
11. Feng et al. (2024), ACL Anthology: https://aclanthology.org/2024.findings-naacl.254/
