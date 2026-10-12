# Search angle 3 — computational disputation, dialectical dialogue, and objection/reply AI

**Scope.** Search for computational models of disputation, dialectical dialogue, objection/reply structure, debate trees, argumentation frameworks, and AI systems that operationalize some part of the scholastic *quaestio/disputatio* pattern without necessarily using the word “scholastic.” The closest analogues are systems with: (a) a root issue or claim, (b) explicit pro/con attacks or objections, (c) regulated turn-taking or critical questions, (d) tree/graph structure, and/or (e) a final evaluation, explanation, or reconciliation step.

**Verification rule.** I retained only sources whose abstract, article page, or PDF was opened and read. Search-result snippets were used for discovery only, not as evidence. The 12 retained papers below were verified from an opened publisher page, ACL page/PDF, arXiv page/PDF, or proceedings PDF.

## Query variants searched

1. `computational models disputation dialectical dialogue argumentation framework AI`
2. `objection reply structure debate tree computational argumentation`
3. `scholastic quaestio disputatio artificial intelligence dialogue system`
4. `AI law argumentation dialogue protocols rebuttal objection reply`
5. `formal dialogue games argumentation frameworks AI`
6. `persuasion dialogue systems argument trees computational`
7. `argument mining debate graphs rebuttal support tree NLP`
8. `philosophy of AI dialectical reasoning dialogue argumentation`
9. `legal reasoning defeasible argumentation dialogue systems`
10. `LLM debate tree argumentation framework critique rebuttal`

The search covered computational argumentation/MAS, AI & Law, dialogue systems, argument mining, LLM debate, philosophy of AI, and the historical bridge from medieval disputation to formal dialogue systems.

## Retained verified sources

### 1. Uckelman (2013), “Medieval Disputationes de obligationibus as Formal Dialogue Systems”

- **Venue/source:** *Argumentation* 27, 143–166; Springer open article.
- **URL:** https://link.springer.com/article/10.1007/s10503-012-9266-7
- **What it contributes:** The most direct bridge in this set. It models medieval *obligationes* as formal dialogue: an Opponent and Respondent alternate moves under rules, with the Respondent’s actions governed by the protocol and the goal of establishing consistency of a proposition. The paper implements the medieval structure in Prakken’s formal dialogue framework using Dynamic Epistemic Logic.
- **Scholastic relevance:** **Exact conceptual overlap** with regulated objection/reply: opposing move, response constrained by a rule system, and a terminal consistency/evaluation objective. It is not a Thomistic *quaestio* implementation, but it demonstrates that a medieval disputational form can be represented as executable dialogue semantics.
- **Evidence checked:** article title/date and abstract, including alternating Opponent/Respondent moves, rule-governed response, consistency goal, and implementation details.

### 2. Maudet, Parsons & Rahwan (2007), “Argumentation in Multi-Agent Systems: Context and Recent Developments”

- **Venue/source:** ArgMAS 2006 / LNCS 4766, pp. 1–16; MIT-hosted PDF.
- **URL:** https://web.mit.edu/irahwan/www/docs/argmas2006survey.pdf
- **What it contributes:** Survey of argumentation for autonomous-agent reasoning and inter-agent communication. It treats argumentation as principled interaction among conflicting arguments, covering belief revision, deliberation, planning, persuasion, inquiry, negotiation, and dialogue games.
- **Scholastic relevance:** **Near overlap** with the disputation as a protocol. The paper describes dialogue games as rule-governed interactions with locutions, commencement/combination/commitment/termination rules; it also notes that a rigid proponent/opponent proof dialogue can be too constrained and that flexible protocols should permit alternative replies. Argumentation schemes plus critical questions provide a direct computational analogue of objection generation.
- **Evidence checked:** opened PDF sections on argumentation/MAS, dialogue-game protocols, flexible proponent/opponent dialogue, and critical questions.

### 3. Castagna, Kökciyan, Sassoon, Parsons & Sklar (2024), “Computational Argumentation-based Chatbots: a Survey”

- **Venue/source:** arXiv:2401.03454v1, cs.AI; HTML paper.
- **URL:** https://arxiv.org/html/2401.03454v1
- **What it contributes:** Taxonomy of chatbots using computational argumentation for extraction, structured reply, reasoning, and reply delivery. It formalizes abstract argumentation frameworks as arguments plus an attack relation, discusses structured argumentation and schemes with critical questions, and classifies argumentation-based dialogues (information-seeking, inquiry, persuasion, negotiation, deliberation, eristic, verification, education, etc.).
- **Scholastic relevance:** **Near overlap** with a machine-readable *objection → reply* pipeline. The paper’s “argumentation-based reply structures,” argument graphs, critical questions, semantics, and dialogue protocols can serve as a general implementation substrate for quaestio-style outputs. It also explicitly positions computational argumentation as a way to improve coherence and explainability in LLM-era chatbots.
- **Evidence checked:** opened HTML abstract, definitions of abstract AFs, argument schemes/critical questions, dialogue types, and computational-argumentation chatbot definition.

### 4. Bolton, Calderwood, Christensen, Kafrouni & Drori (2020), “High Quality Real-Time Structured Debate Generation”

- **Venue/source:** arXiv:2012.00209; PDF.
- **URL:** https://arxiv.org/pdf/2012.00209
- **What it contributes:** Defines debate trees and debate paths for automatically generating debates with high-level structure and grammar; uses a corpus of tree-structured debates with argument metadata and reports real-time generation evaluated on style, content, and strategy.
- **Scholastic relevance:** **Near/exact structural overlap** with a disputation tree. A root topic can branch into supporting and negating moves, and the system can generate paths through that tree. It lacks the named *sed contra/respondeo/replies* stages, but its explicit tree/path representation is a strong computational analogue for nested objections and replies.
- **Evidence checked:** opened PDF abstract/introduction describing debate trees, paths, argument negation/support, and structured debate generation.

### 5. Kargupta, Agarwal, August & Han (2025), “Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis”

- **Venue/source:** ACL 2025 Long Papers; ACL Anthology page and arXiv HTML.
- **URLs:** https://aclanthology.org/2025.acl-long.1422/ ; https://arxiv.org/html/2502.14767v2
- **What it contributes:** Converts scientific papers into LLM personas that debate their respective novelties. The system dynamically constructs a debate tree to analyze independent novelty arguments and evaluates the resulting comparisons with expert researchers.
- **Scholastic relevance:** **Near overlap** with a multi-agent disputation whose root question is decomposed into claims, objections, and counter-objections. The persona specialization resembles assigned disputant roles; dynamic tree growth resembles branching objection/reply analysis. The target is literature comparison rather than truth of a philosophical proposition.
- **Evidence checked:** opened ACL abstract and arXiv HTML abstract/introduction, including persona conversion, dynamic debate-tree construction, and expert evaluation.

### 6. Vasileiou, Kumar, Yeoh, Son & Toni (2024), “Dialectical Reconciliation via Structured Argumentative Dialogues”

- **Venue/source:** KR 2024 proceedings PDF.
- **URL:** https://proceedings.kr.org/2024/73/kr2024-0073-vasileiou-et-al.pdf
- **What it contributes:** Formal framework for human–AI “dialectical reconciliation,” in which an explainer agent and human explainee address knowledge discrepancies through structured argumentation-based dialogue. It gives operational semantics, theoretical guarantees, computational experiments, and a human-subject evaluation.
- **Scholastic relevance:** **Near overlap with respondeo/explanatory reconciliation.** The explainer must present arguments and counterarguments so that the explainee’s knowledge converges toward the explainer’s decision model. This is closer to a dialectical *respondeo* than to open-ended debate: the dialogue is terminated when the relevant understanding/knowledge condition is satisfied.
- **Evidence checked:** opened proceedings PDF abstract and discussion of structured argumentation, internal argument structure, counterarguments, operational semantics, and understanding metric.

### 7. Faugier, Armetta, Bonifati & Yun (2024), “Assisted Debate Builder with Large Language Models”

- **Venue/source:** arXiv:2405.13015; HTML abstract/full paper.
- **URL:** https://arxiv.org/abs/2405.13015
- **What it contributes:** ADBL2 is an open-source debate-builder tool using LLM-based relation-based argument mining to verify pre-existing attack/support relations and assist creation of new arguments. It imports debate trees, exposes relation probabilities, and supports editing/exporting the resulting tree. The paper describes bipolar argumentation trees with support and attack edges.
- **Scholastic relevance:** **Near overlap** with a tool-assisted objection/reply editor. The system does not generate a full *quaestio*, but it provides the missing graph-construction layer: identify whether a proposed move supports or attacks a parent argument and preserve the debate tree as an inspectable artifact.
- **Evidence checked:** opened arXiv page/full HTML, including tool purpose, attack/support relation mining, debate-tree construction, and formal tree representation.

### 8. Du, Li, Torralba, Tenenbaum & Mordatch (2023), “Improving Factuality and Reasoning in Language Models through Multiagent Debate”

- **Venue/source:** arXiv:2305.14325; abstract page.
- **URL:** https://arxiv.org/abs/2305.14325
- **What it contributes:** Multiple LLM instances propose and debate answers/reasoning over multiple rounds before reaching a common final answer; the paper reports improvements in mathematical/strategic reasoning and factual validity, with reduced fallacious answers/hallucinations.
- **Scholastic relevance:** **Near overlap** with multi-round objections and replies followed by a judgment/synthesis stage. It is not a formal argumentation framework: the debate protocol is largely prompt-defined and the paper’s target is answer quality rather than explicit proof of each objection. It is nevertheless relevant as an AI implementation pattern for staged dialectical generation.
- **Evidence checked:** opened arXiv abstract page with authors, protocol description, multiple rounds, common final answer, and reported outcomes.

### 9. Khan et al. (2024), “Debating with More Persuasive LLMs Leads to More Truthful Answers”

- **Venue/source:** arXiv:2402.06782; abstract page.
- **URL:** https://arxiv.org/abs/2402.06782
- **What it contributes:** Studies two LLM debaters arguing opposite answers before a weaker model or human selects the answer. The paper reports improved answer selection and examines optimizing debaters for persuasiveness without direct ground-truth labels.
- **Scholastic relevance:** **Near overlap** with disputation as adversarial testing before judgment. It operationalizes the “opposition exposes error” intuition, but differs from scholastic form in having fixed opposing sides and a judge rather than a Respondent who integrates objections into a principled final answer.
- **Evidence checked:** opened arXiv abstract page and revised-version metadata.

### Lineage note (not an additional paper)

- **Status:** This item is intentionally **not counted separately** as a paper. It records the recurring lineage found in the opened sources: Hamblin formal dialogue → Walton/Krabbe dialogue types → Prakken-style protocols → Dung-style argumentation frameworks → contemporary argumentation-based chatbots and LLM debate trees.
- **Reason for inclusion in the synthesis:** The sources repeatedly converge on the same computational primitives: legal moves, commitments, attacks/support, critical questions, dialogue termination, and semantic evaluation. This lineage matters more for the project than any one implementation label.

### 10. Hadoux & Hunter (2017), “Strategic Sequences of Arguments for Persuasion Using Decision Trees”

- **Venue/source:** AAAI proceedings PDF.
- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/10673/10532
- **What it contributes:** Uses decision trees to select strategic sequences of arguments for persuasion, treating argument choice as a planning problem over a dialogue.
- **Scholastic relevance:** **Near overlap** with selecting which objection/reply to present next. It is useful for a disputation engine that must prioritize objections, critical questions, or replies under cost/utility constraints rather than enumerate every possible branch.
- **Evidence checked:** opened AAAI PDF.

### 11. Gorur et al. (2024), “Can Large Language Models perform Relation-based Argument Mining?”

- **Venue/source:** arXiv:2402.11243; HTML paper.
- **URL:** https://arxiv.org/html/2402.11243
- **What it contributes:** Evaluates LLMs for relation-based argument mining, i.e., identifying relations among argument components rather than only detecting isolated claims.
- **Scholastic relevance:** **Supporting infrastructure overlap.** A scholastic parser needs to distinguish objection, support, rebuttal, undercutting, and reply relations; this paper addresses the relation-extraction problem needed before a disputation tree can be built or checked.
- **Evidence checked:** opened arXiv HTML paper.

### 12. Peldszus & Stede (2019), “Determining Relative Argument Specificity and Stance for Complex Argumentative Structures”

- **Venue/source:** ACL 2019 PDF.
- **URL:** https://aclanthology.org/P19-1456.pdf
- **What it contributes:** Addresses stance and relative specificity in complex argumentative structures, both of which are needed when arguments do not form a simple linear pro/con pair.
- **Scholastic relevance:** **Supporting infrastructure overlap.** Scholastic objections often target a specific premise, distinction, or inference rather than the whole conclusion. Specificity and stance modeling can help classify whether a reply defeats the objection, narrows it, or merely shifts the target.
- **Evidence checked:** opened ACL PDF.

## Exact/near-overlap flags

| Computational pattern | Closest retained sources | Overlap assessment | What is still missing for a scholastic *quaestio* |
|---|---|---|---|
| Alternating opponent/respondent under explicit rules | Uckelman 2013; Maudet et al. 2007 | **Exact protocol-level overlap** with formal disputation/obligationes | Named stages (*quaestio*, objections, *sed contra*, *respondeo*, replies) and a canonical final answer schema |
| Argument graph with attacks/supports | Castagna et al. 2024; Faugier et al. 2024; Gorur et al. 2024 | **Near structural overlap** | Distinguish objection types: direct rebuttal, undercutter, distinction, qualification, and reply-to-reply |
| Tree/path generation for debate | Bolton et al. 2020; Kargupta et al. 2025 | **Near structural overlap** | Role semantics and stage ordering; current systems are generic debate trees, not question-centered disputations |
| Critical questions attached to argument schemes | Maudet et al. 2007; Castagna et al. 2024 | **Near functional overlap** with objections | A controlled library of scholastic objection templates and rules for when each question is discharged |
| Explainer presents reasons and answers counterarguments | Vasileiou et al. 2024 | **Near overlap** with *respondeo* and explanatory replies | A stable distinction between the main answer, objections, and replies; explicit handling of contrary authority (*sed contra*) |
| Multi-agent LLM debate with final judge/synthesis | Du et al. 2023; Khan et al. 2024 | **Near procedural overlap** | Formal argument semantics, provenance, non-hallucinatory citations, and a reasoned synthesis rather than winner selection |
| Strategic next-move selection | Hunter / AAAI decision-tree paper | **Near planning overlap** | Scholastic relevance ordering: prioritize objections that threaten the main inference, not merely persuasive utility |
| Legal/defeasible reasoning | Maudet et al. 2007 survey; Castagna et al. 2024; the AI & Law query family | **Near domain overlap** | Explicit mapping from authority/case distinctions to *sed contra*, objections, and replies |

## Synthesis for the project

1. **The closest formal ancestor is not generic LLM debate; it is rule-governed dialogue.** Uckelman’s reconstruction of *obligationes* gives the clearest executable template: two roles, alternating moves, legal-response constraints, and a terminal consistency question. A scholastic parser should therefore represent a disputation as a protocol/state machine in addition to a text tree.
2. **A useful intermediate representation is a typed argument graph.** The contemporary literature converges on nodes plus attack/support relations, often enriched with internal premises/rules and critical questions. For the project, the graph should retain the original text span, role, target node, relation type, and whether a reply defeats, limits, or reframes the objection.
3. **Tree structure alone is insufficient.** Debate-tree systems provide branching and path generation, but scholastic structure requires typed slots and stage semantics. A root “question” should have an objection set, a contrary authority or counter-consideration, a main determination, and replies linked to individual objections.
4. **Critical questions are a strong computational analogue of objections.** Argumentation schemes turn a claim into a finite set of pressure points. This is close to scholastic objection generation, provided the system distinguishes a challenge to a premise from a challenge to the inference or to the scope of the conclusion.
5. **LLM debate systems supply generation and evaluation patterns, not sufficient semantics.** Multi-round debate can improve factuality or answer selection, but without explicit provenance and typed relations it can collapse into persuasive performance. A scholastic pipeline should use LLMs for candidate extraction/generation while delegating acceptance, linkage, and termination to inspectable rules or argumentation semantics.
6. **The most promising architecture is hybrid:** argument mining → typed disputation graph → protocol-constrained reply generation → semantic/consistency checks → rendered *quaestio* output. The retained literature supports each stage, but no single paper implements the whole Thomistic sequence.

## Gaps and cautions

- I found no verified paper in this sweep that implements the full Thomistic sequence *quaestio → objections → sed contra → respondeo → replies* as a general computational model. The closest exact bridge is Uckelman’s formalization of medieval *obligationes*, while the closest modern AI systems are generic argumentation chatbots, debate-tree generators, and structured explanation dialogues.
- “Debate” is overloaded. Some systems generate persuasive two-sided text; others compute accepted arguments under formal semantics; others mine relations from existing debate graphs. These should not be merged as if they had the same notion of correctness.
- Search results surfaced product pages and GitHub projects explicitly calling themselves scholastic or Thomistic, but they were not retained as research sources because this review prioritized opened scholarly papers/PDFs and reproducible computational models.
- Exact overlap claims above refer to structural or protocol similarity, not historical identity. “Near overlap” means useful design correspondence, not evidence that the cited authors intended to model scholastic disputation.

## Source count

**12 verified scholarly sources/papers retained** (the lineage note is not an additional paper).