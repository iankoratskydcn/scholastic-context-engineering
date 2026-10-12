# Subtopic 5 — Retrieval-Augmented Generation, Grounding, and Limits

## Scope and search record

**Question.** What does primary RAG research establish about retrieval as grounding for structured argument extraction/context engineering, and where does the grounding claim fail?

**Search route.** Google Scholar was used for discovery with the following eight query variants; metadata and source text were then verified from arXiv abstracts/PDFs (the route is recorded per paper). No login, upload, or external write was used.

1. `site:scholar.google.com retrieval augmented generation grounding hallucination`
2. `site:scholar.google.com RAG factuality evidence attribution`
3. `site:scholar.google.com retrieval augmented language models limitations`
4. `site:scholar.google.com retrieval augmentation knowledge intensive NLP`
5. `site:scholar.google.com provenance citation faithfulness retrieval generation`
6. `site:scholar.google.com robustness adversarial retrieval augmented generation`
7. `site:scholar.google.com long context retrieval augmented generation benchmark`
8. `site:scholar.google.com retrieval augmented generation survey evaluation`

## Verified papers

### 1. Guu et al. (2020), “REALM: Retrieval-Augmented Language Model Pre-Training”
- **Citation / route:** Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, Ming-Wei Chang. arXiv:2002.08909 (2020). Route: Google Scholar discovery → arXiv abstract/PDF; first-page metadata and PDF abstract inspected.
- **Finding:** REALM makes a retriever a trainable, latent access path to a large external corpus during pretraining, fine-tuning, and inference. On open-domain QA it reports 4–16 absolute-point gains over prior methods and argues for modularity/interpretability.
- **Relation to structured argument extraction/context engineering:** Establishes the architectural premise that external evidence can be separated from parametric memory and updated independently. This supports an evidence-retrieval layer before claim/argument extraction, but does not itself produce claim-level provenance or argument structure.
- **Limitation:** Retrieval is optimized for task performance, not proof of entailment. A retrieved passage can be relevant yet insufficient, ambiguous, outdated, or contradictory; “interpretable” access is not equivalent to a grounded conclusion.

### 2. Lewis et al. (2020), “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”
- **Citation / route:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela. arXiv:2005.11401 (2020). Route: Google Scholar discovery → arXiv abstract/PDF; first page, abstract, and conclusion/limitations text inspected.
- **Finding:** RAG combines a parametric seq2seq model with a dense-vector Wikipedia index and compares sequence-level versus token-level retrieval conditioning. The paper reports state-of-the-art results on three open-domain QA tasks and explicitly identifies provenance and knowledge updating as open problems.
- **Relation:** Provides the canonical retrieve-then-generate baseline for a context-engineering pipeline: retrieve candidate documents, retain them as explicit context, then generate. It motivates separating retrieval evidence from generated claims.
- **Limitation:** Benchmark gains do not establish that every generated sentence is supported. The paper itself leaves provenance open; retrieval-conditioned generation can still omit, distort, or combine evidence without traceable claim-to-source links.

### 3. Izacard et al. (2022), “Atlas: Few-shot Learning with Retrieval Augmented Language Models”
- **Citation / route:** Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, Edouard Grave. arXiv:2208.03299 (2022). Route: Google Scholar discovery → arXiv PDF; first page and abstract inspected.
- **Finding:** Atlas is a retrieval-augmented model designed for few-shot knowledge-intensive learning; it studies index content and reports strong Natural Questions performance with only 64 examples, while showing that the document index can be updated.
- **Relation:** Supports treating the corpus/index as a replaceable context-engineering component rather than baking all domain knowledge into weights. For argument work, this favors versioned evidence stores and domain-specific retrieval.
- **Limitation:** Few-shot QA accuracy and index updatability do not guarantee source-faithful reasoning. The work is primarily answer-quality oriented, not a test of citation completeness, argumentative validity, or resistance to adversarial/incorrect documents.

### 4. Ma et al. (2023), “Query Rewriting for Retrieval-Augmented Large Language Models”
- **Citation / route:** Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao, Nan Duan. arXiv:2305.14283 (2023). Route: Google Scholar discovery → arXiv PDF; first page, abstract, conclusion, and limitations inspected.
- **Finding:** The Rewrite–Retrieve–Read pipeline inserts a query-rewriting step between the user input and retrieval, using either prompted or trainable rewriting. The paper reports consistent gains on open-domain QA and multiple-choice QA.
- **Relation:** Directly relevant to structured argument extraction: a user question often underspecifies the entities, claims, time range, or relation needed to retrieve evidence. Query planning/reformulation should therefore be an explicit stage, with the original request preserved for audit.
- **Limitation:** Rewriting can specialize toward benchmark/task distributions and can change the question’s scope. The authors note generalization/scalability trade-offs and limitations of web search and one-turn retrieval; a rewritten query is not proof that the retrieved evidence answers the original question.

### 5. Gao et al. (2023), “Enabling Large Language Models to Generate Text with Citations” (ALCE)
- **Citation / route:** Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen. arXiv:2305.14627 (2023). Route: Google Scholar discovery → arXiv PDF; first page, abstract, conclusion, and limitations inspected.
- **Finding:** ALCE is an end-to-end benchmark for retrieving support and generating answers with citations, with automatic metrics for fluency, correctness, and citation quality validated against human judgments. The paper reports substantial remaining room for improvement; on ELI5, even the best systems lacked complete citation support 50% of the time.
- **Relation:** This is the clearest bridge from RAG to evidence-grounded argument extraction: evaluation must distinguish answer correctness from citation correctness/completeness. A structured argument artifact should preserve claim-level support links, not merely append a bibliography.
- **Limitation:** Metrics depend partly on NLI and automatic claim generation; the authors flag sensitivity to output length, partial-support detection problems, and limited coverage of multi-hop, math, and code scenarios. Citation presence is therefore not sufficient evidence of entailment.

### 6. Liu et al. (2023), “Lost in the Middle: How Language Models Use Long Contexts”
- **Citation / route:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang. arXiv:2307.03172 (2023). Route: Google Scholar discovery → arXiv PDF; first page, abstract, discussion, and experimental text inspected.
- **Finding:** In multi-document QA and key-value retrieval, performance can degrade substantially when relevant information is placed in the middle of a long context; performance is often better when evidence appears at the beginning or end. The effect persists for models advertised as long-context models.
- **Relation:** More retrieved context is not automatically better context engineering. Argument extraction should rank, segment, and organize evidence, and should test position sensitivity rather than assuming that placing all sources in a prompt grounds the answer.
- **Limitation:** The tasks are controlled QA/key-value settings rather than full argument extraction, and the paper does not directly measure citation faithfulness. The result establishes a context-use failure mode, not a universal quantitative law for every model or prompt layout.

### 7. Asai et al. (2023), “SELF-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection”
- **Citation / route:** Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi. arXiv:2310.11511 (2023). Route: Google Scholar discovery → arXiv PDF; first page, abstract, and results/conclusion text inspected.
- **Finding:** SELF-RAG trains a model to retrieve on demand and to generate/critique using reflection tokens, rather than always adding a fixed number of passages. It reports gains over ChatGPT and retrieval-augmented Llama2-chat on open-domain QA, reasoning, and fact verification tasks.
- **Relation:** Supports adaptive evidence acquisition and an explicit critique/verification phase in a structured argument workflow. Retrieval should be conditional on information need, and generated claims should be checked against retrieved passages before acceptance.
- **Limitation:** Self-reflection is still a model-generated control signal; it can fail to retrieve, misjudge relevance, or critique its own unsupported claim incorrectly. Reported gains do not make self-critique an independent verifier.

### 8. Niu et al. (2024), “RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models”
- **Citation / route:** Cheng Niu, Yuanhao Wu, Juno Zhu, Siliang Xu, Kashun Shum, Randy Zhong, Juntong Song, Tong Zhang. arXiv:2401.00396 (2024). Route: Google Scholar discovery → arXiv PDF; first page, abstract, conclusion, and limitations inspected.
- **Finding:** RAGTruth provides nearly 18,000 naturally generated RAG responses with case- and word-level hallucination annotations and benchmarks detection methods. Fine-tuning a smaller model on the corpus can be competitive with prompt-based GPT-4 detection, but span-level hallucination detection remains difficult.
- **Relation:** Supplies an operational definition/evaluation resource for unsupported or contradictory spans, useful for auditing extracted premises, claims, warrants, and conclusions separately.
- **Limitation:** The corpus covers selected tasks/models and cannot represent every deployment context; the authors explicitly note unaddressed application scenarios. Detection performance on a corpus is not proof that a production argument is grounded.

### 9. Tang and Yang (2024), “MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries”
- **Citation / route:** Yixuan Tang, Yi Yang. arXiv:2401.15391 (2024). Route: Google Scholar discovery → arXiv PDF; first page, abstract, conclusion, and limitations inspected.
- **Finding:** MultiHop-RAG introduces a dataset with a knowledge base, multi-hop queries, answers, and supporting evidence. Experiments report that existing RAG systems perform unsatisfactorily both at retrieving multiple supporting pieces and at answering multi-hop questions given evidence.
- **Relation:** Structured arguments often require chaining several sources or premises. This paper supports evaluating retrieval recall over the full support set and testing whether the generator preserves the chain, rather than scoring only final-answer similarity.
- **Limitation:** Ground-truth answers are restricted to simple forms and evidence is capped at four pieces; the experiments use a basic RAG framework. Results therefore understate or omit more complex argumentative synthesis.

### 10. Yan et al. (2024), “Corrective Retrieval Augmented Generation” (CRAG)
- **Citation / route:** Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling. arXiv:2401.15884 (2024). Route: Google Scholar discovery → arXiv PDF; first page, abstract, discussion, and conclusion/limitation text inspected.
- **Finding:** CRAG adds a lightweight retrieval evaluator that assigns confidence and triggers different actions, including web search and document decomposition/recomposition to filter irrelevant content. Experiments across four datasets report improved short- and long-form generation; the authors identify retrieval evaluation as central when retrieval goes wrong.
- **Relation:** Supports a retrieval-quality gate before argument extraction: evidence can be accepted, refined, expanded, or rejected. This maps naturally to provenance states such as supported, weakly supported, conflicting, and unresolved.
- **Limitation:** CRAG depends on an external retrieval evaluator whose errors can route the system incorrectly; web search adds source-quality, temporal, and adversarial-content risks. “Correction” is not independent truth verification.

### 11. Jiang et al. (2024), “LongRAG: Enhancing Retrieval-Augmented Generation with Long-context LLMs”
- **Citation / route:** Ziyan Jiang, Xueguang Ma, Wenhu Chen. arXiv:2406.15319 (2024). Route: Google Scholar discovery → arXiv PDF; first page, abstract, and conclusion inspected.
- **Finding:** LongRAG groups documents into roughly 4K-token retrieval units, reducing the corpus from 22M to 600K units in its Wikipedia experiments and using fewer long units to preserve document semantics and improve retrieval recall. It reports strong results on four QA tasks without training.
- **Relation:** Relevant to argument extraction where local chunks lose definitions, exceptions, or cross-sentence relations. Longer units can preserve context, but should be paired with evidence localization so the final argument points to exact support spans.
- **Limitation:** Larger units increase prompt load and can reintroduce irrelevant material; the approach is evaluated mainly on Wikipedia QA. The paper does not establish that long units improve claim-level grounding or resist long-context position effects.

## Synthesis for structured argument extraction

1. **Retrieval is an evidence-access mechanism, not a grounding guarantee.** REALM, RAG, and Atlas show that external memory can improve knowledge-intensive performance and updateability, but Lewis et al. explicitly leave provenance open. Treat retrieval relevance, source reliability, entailment, and argumentative sufficiency as separate checks.
2. **Query and context construction are first-class reasoning stages.** Query Rewriting shows that the initial request may not be retrieval-ready; LongRAG and Lost in the Middle show that chunk size, ordering, and context length affect what the model can use. Preserve the original query, rewritten query, retrieved IDs, rank, and selected spans.
3. **Argument-level support must be evaluated per claim and per link.** ALCE separates correctness from citation quality; RAGTruth shows that unsupported spans persist inside RAG outputs. A useful extraction schema should represent premises/claims/conclusions with support edges, exact evidence spans, contradiction status, and unresolved gaps.
4. **Multi-hop and bad-retrieval cases are the decisive limits.** MultiHop-RAG shows failures when support is distributed across documents; CRAG shows that retrieval errors require explicit detection and repair. Do not report “grounded” when only one relevant-looking passage was retrieved or when the model’s conclusion was not entailed by the full support set.
5. **Self-critique is a control aid, not an oracle.** SELF-RAG and CRAG motivate adaptive retrieval and critique, but both retain model/evaluator failure modes. Independent checks—source metadata, claim-to-span entailment, contradiction search, and abstention—remain necessary.

## Failed or thin searches

- Scholar query variants for `RAG factuality evidence attribution`, `provenance citation faithfulness retrieval generation`, and `robustness adversarial retrieval augmented generation` returned noisy author/profile pages and snippets rather than consistently accessible paper records. These were used for discovery only, not as evidence.
- Direct `web_extract` of arXiv/ACL URLs was unavailable in this environment because the configured native backend is search-only. PDFs were instead fetched read-only from arXiv and text-inspected locally with `pypdf`; no paper was retained without a readable PDF/metadata header.
- A direct arXiv API metadata batch was rate-limited once (HTTP 429). Metadata was verified from the downloaded PDF first pages and previously successful arXiv API responses; no unverified venue or citation-count claims are included.
- Searches for a single canonical “grounding” metric were thin: the retained primary papers operationalize different targets—QA accuracy, citation quality, hallucination spans, retrieval recall, multi-hop answer accuracy, or long-context use. These are related but not interchangeable evidence of grounding.

## Bottom line

The primary literature supports a restrained claim: RAG can improve access to external evidence and often improves knowledge-intensive task performance, but retrieval alone does not ensure factuality, entailment, citation completeness, or valid argumentative structure. For scholastic context engineering, grounding should be implemented as a traceable pipeline—query formulation → ranked evidence → exact spans → claim extraction → entailment/contradiction checks → calibrated abstention—with benchmark coverage for long contexts, multi-hop support, bad retrieval, and unsupported spans.
