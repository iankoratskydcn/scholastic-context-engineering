# Research subtopic 3: long-context degradation, lost in the middle, and context rot

**Scope.** Evidence on performance degradation as input length grows, positional/attention bias (especially middle-position failures), limits of long-context benchmarks, and the newer “context rot” framing. Search date: 2026-10-11.

## Search route and query variants

Google Scholar was attempted first. The Scholar endpoint returned an anti-bot/interstitial page rather than results, so no Scholar result snippets were treated as evidence. I then used broad web search to locate the corresponding primary publisher, proceedings, arXiv, and paper pages, and opened those pages or their PDFs/metadata.

Queries attempted (8 variants):

1. `Google Scholar lost in the middle long context language models`
2. `Google Scholar long context degradation language models context length`
3. `Google Scholar context rot large language models`
4. `Google Scholar long-context understanding benchmark positional bias`
5. `Google Scholar long range arena language models`
6. `Google Scholar needle in a haystack long context`
7. `Google Scholar transformers effective context length degradation`
8. `Google Scholar long context retrieval augmented generation lost middle`

## Verified papers retained (10)

### 1. Liu et al. (2024), “Lost in the Middle: How Language Models Use Long Contexts”

- **Citation.** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. *Transactions of the Association for Computational Linguistics*, 12, 157–173, 2024. DOI: `10.1162/tacl_a_00638`. Source route: ACL Anthology page and ACL BibTeX: https://aclanthology.org/2024.tacl-1.9/
- **Finding.** On multi-document question answering and key-value retrieval, performance can vary substantially with the position of relevant information; the characteristic pattern is worse use of information in the middle than near the beginning or end of the context.
- **Relation to subtopic.** Foundational direct evidence for “lost in the middle”: a long nominal context window does not imply uniform utilization of the context.
- **Limitation.** The evaluation centers on two controlled information-identification tasks and a set of models available at the time; it does not cover all long-context reasoning, agents, modalities, or current frontier models.

### 2. Sun et al. (2021), “Do Long-Range Language Models Actually Use Long-Range Context?”

- **Citation.** Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, and Mohit Iyyer. *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 807–822, 2021. DOI: `10.18653/v1/2021.emnlp-main.62`. Source route: ACL Anthology page and ACL BibTeX: https://aclanthology.org/2021.emnlp-main.62/
- **Finding.** A fine-grained analysis of long-range Transformer language models reports that models often rely on local context and may fail to exploit discourse-level information farther away, despite accepting longer sequences.
- **Relation to subtopic.** Early foundational evidence that architectural/context-length support and actual long-range use are different properties; it predates the later “lost in the middle” terminology.
- **Limitation.** The study uses earlier long-range language-model architectures and language-modeling analyses, so absolute performance and failure modes may not transfer directly to modern instruction-tuned LLMs.

### 3. Tay et al. (2021), “Long Range Arena: A Benchmark for Efficient Transformers”

- **Citation.** Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. *International Conference on Learning Representations (ICLR 2021)*. Source route: ICLR paper page: https://www.iclr.cc/virtual/2021/poster/3225
- **Finding.** Introduces a unified benchmark for long-context sequence processing with tasks spanning roughly 1K–16K tokens, motivated by the difficulty and quadratic cost of standard self-attention and inconsistent prior evaluation.
- **Relation to subtopic.** Foundational measurement infrastructure: it established that “long context” needs task-based evaluation rather than relying only on advertised sequence length or efficiency claims.
- **Limitation.** LRA is primarily a benchmark for efficient Transformer architectures and synthetic/structured sequence tasks; it is not a direct measure of modern instruction-following LLM context rot or real document workflows.

### 4. Xu et al. (2023), “Retrieval meets Long Context Large Language Models”

- **Citation.** Peng Xu, Wei Ping, Xianchao Wu, Lawrence McAfee, Chen Zhu, Zihan Liu, Sandeep Subramanian, Evelina Bakhturina, Mohammad Shoeybi, and Bryan Catanzaro. arXiv preprint, arXiv:2310.03025, 2023. DOI route: `10.48550/arXiv.2310.03025`. Source route: arXiv abstract/HTML; OpenReview route was also located but challenged by browser verification: https://arxiv.org/abs/2310.03025
- **Finding.** Compares retrieval augmentation with extended context windows and reports that smaller-context retrieval-augmented systems can be competitive with or better than larger-context systems, while retrieval can improve performance even when the context window is already extended.
- **Relation to subtopic.** Provides a mitigation-oriented counterpoint: context degradation makes indiscriminate context stuffing less attractive, and selective retrieval can reduce the amount of distractor material presented to the model.
- **Limitation.** The experiments use particular pretrained models, task sets, and retrieval configurations; results do not establish that retrieval is universally superior to long context or eliminate retrieval errors.

### 5. Bai et al. (2024), “LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding”

- **Citation.** Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 3119–3137, 2024. DOI: `10.18653/v1/2024.acl-long.172`. Source route: ACL Anthology page and BibTeX: https://aclanthology.org/2024.acl-long.172/
- **Finding.** Introduces a bilingual, multitask benchmark for long-context understanding across tasks such as question answering, summarization, and few-shot learning, addressing the lack of comprehensive evaluation beyond short contexts.
- **Relation to subtopic.** Broadens degradation research from single-needle retrieval to heterogeneous language tasks and makes cross-task/context-length comparisons possible.
- **Limitation.** Benchmark results depend on dataset construction, prompting, scoring, and model versions; aggregate scores can obscure position-specific failure patterns and do not by themselves identify mechanisms.

### 6. Zhang et al. (2024), “∞Bench: Extending Long Context Evaluation Beyond 100K Tokens”

- **Citation.** Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Hao, Xu Han, Zhen Thai, Shuo Wang, Zhiyuan Liu, and Maosong Sun. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 15262–15277, 2024. DOI: `10.18653/v1/2024.acl-long.814`. Source route: ACL Anthology page and BibTeX: https://aclanthology.org/2024.acl-long.814/
- **Finding.** Proposes an evaluation suite aimed at contexts beyond 100K tokens, addressing the gap between very large advertised context windows and the much shorter contexts used by many public benchmarks.
- **Relation to subtopic.** Tests whether degradation appears at extreme lengths where many systems claim support; it pushes the empirical boundary from “long” context to genuinely ultra-long context.
- **Limitation.** Very-long evaluations are expensive and sensitive to inference infrastructure, truncation/tokenization details, and task design; benchmark performance still does not prove robust use of every token in arbitrary real-world inputs.

### 7. Hsieh et al. (2024), “Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization”

- **Citation.** Cheng-Yu Hsieh, Yung-Sung Chuang, Chun-Liang Li, Zifeng Wang, Long Le, Abhishek Kumar, James Glass, Alexander Ratner, Chen-Yu Lee, Ranjay Krishna, and Tomas Pfister. *Findings of the Association for Computational Linguistics: ACL 2024*, 14982–14995, 2024. DOI: `10.18653/v1/2024.findings-acl.890`. Source route: ACL Anthology page and BibTeX: https://aclanthology.org/2024.findings-acl.890/
- **Finding.** Connects lost-in-the-middle behavior to an intrinsic U-shaped positional attention bias, with stronger attention toward the beginning and end than the middle, and proposes calibration methods to improve utilization of middle-position information.
- **Relation to subtopic.** Mechanistic/mitigation follow-up to the original phenomenon: it treats positional bias as an actionable cause rather than only an observed curve.
- **Limitation.** The proposed calibration is evaluated under specific model/task settings and may trade off other behaviors; positional attention patterns are not a complete explanation for all long-context degradation.

### 8. Hsieh et al. (2024), “RULER: What’s the Real Context Size of Your Long-Context Language Models?”

- **Citation.** Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg. arXiv preprint, arXiv:2404.06654, 2024. Source route: arXiv abstract/HTML: https://arxiv.org/abs/2404.06654
- **Finding.** Extends needle-in-a-haystack evaluation with multiple needles, multi-hop tracing, and aggregation tasks. Across 17 long-context LMs and 13 tasks, models can be nearly perfect on simple needle retrieval yet show large performance drops as context length increases; the abstract reports that only about half maintain satisfactory performance at 32K despite claiming at least 32K context.
- **Relation to subtopic.** Direct operationalization of “context rot”: capability degrades with increasing input length and simple NIAH success can substantially overstate general long-context competence.
- **Limitation.** RULER is synthetic and task-family-specific; “satisfactory” is threshold-dependent, and the reported model snapshot is from 2024 rather than current systems.

### 9. Modarressi et al. (2025), “NoLiMa: Long-Context Evaluation Beyond Literal Matching”

- **Citation.** Ali Modarressi, Hanieh Deilamsalehy, Franck Dernoncourt, Trung Bui, Ryan A. Rossi, Seunghyun Yoon, and Hinrich Schuetze. *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267:44554–44570, 2025. Source route: PMLR paper page and BibTeX: https://proceedings.mlr.press/v267/modarressi25a.html
- **Finding.** Shows that standard needle-in-a-haystack tests can be made too easy by lexical overlap between the query and the inserted needle. NoLiMa minimizes literal overlap and requires latent association; 13 evaluated LLMs perform well at short contexts but degrade sharply as context grows.
- **Relation to subtopic.** Refines the context-rot measurement problem: apparent long-context robustness can be an artifact of lexical matching, while harder semantic retrieval exposes degradation more clearly.
- **Limitation.** The benchmark’s controlled needle design is still not equivalent to open-ended document reasoning, and its results reflect the evaluated 2025 model set and task construction.

### 10. Tian et al. (2025), “Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs”

- **Citation.** Runchu Tian, Yanghao Li, Yuepeng Fu, Siyang Deng, Qinyu Luo, Cheng Qian, Shuo Wang, Xin Cong, Zhong Zhang, Yesai Wu, Yankai Lin, Huadong Wang, and Xiaojiang Liu. *Findings of the Association for Computational Linguistics: ACL 2025*, 521–533, 2025. DOI: `10.18653/v1/2025.findings-acl.28`. Source route: ACL Anthology page, PDF, and BibTeX: https://aclanthology.org/2025.findings-acl.28/
- **Finding.** Introduces LongPiBench for multiple relevant information pieces and studies positional bias when those pieces are separated by different distances, extending lost-in-the-middle analysis beyond a single relevant span.
- **Relation to subtopic.** Important real-world extension: multi-document answers often require combining dispersed evidence, so degradation depends not only on absolute position but also on the distance and arrangement among relevant pieces.
- **Limitation.** The benchmark remains controlled and focused on positional/multi-piece effects; it does not fully cover noisy conversational histories, tool traces, multimodal context, or agent state.

## Synthesis

The evidence supports three separable claims. First, long input acceptance is not equivalent to uniform information use: this is established by the early long-range analysis and the later lost-in-the-middle results. Second, evaluation design strongly affects measured capability: LRA, LongBench, ∞Bench, RULER, and NoLiMa progressively broaden task coverage, length, and semantic difficulty, while showing that simple retrieval tests can overestimate competence. Third, “context rot” is a useful umbrella label for performance degradation as irrelevant or difficult-to-use tokens accumulate, but the retained scholarly literature more often operationalizes it as positional bias, distractor sensitivity, long-range dependency failure, or length-dependent task degradation rather than using the exact phrase.

## Search failures and exclusions

- **Google Scholar:** direct Scholar requests for the eight variants above returned an anti-bot/interstitial page (“Why did this happen?”) rather than result pages. Scholar snippets were therefore not used as evidence.
- **OpenReview:** the page for “Retrieval meets Long Context Large Language Models” returned a browser-verification challenge. The paper was verified through its arXiv abstract/HTML and retained as an arXiv preprint, without asserting an unverified venue.
- **Context Rot exact phrase:** searches located Chroma’s technical report, repository, and secondary commentary, but no arXiv/ACM/ACL/ICLR/ICML paper page with a verified scholarly venue was found in the attempted routes. The report was not counted among the 10 papers; its concept is represented through the verified RULER, NoLiMa, Lost in the Middle, and related benchmark papers.
- **No unsupported venue claims:** RULER and Retrieval Meets Long Context are labeled arXiv preprints because a peer-reviewed venue was not verified from an opened primary venue page.
