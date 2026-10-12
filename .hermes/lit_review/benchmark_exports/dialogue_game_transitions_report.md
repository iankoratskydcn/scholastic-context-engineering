# Dialogue-game transitions benchmark scan

**Slug:** `dialogue_game_transitions`  
**Research date:** October 12, 2026  
**Artifact:** `dialogue_game_transitions.csv`

## Scope

This scan targets reusable scholarly artifacts for a structured dialogue engine that needs to represent multi-turn argumentation, dialogue-game moves, commitment-like state, objections and replies, response legality, and response quality. The results deliberately separate three kinds of evidence:

1. **Protocol/formalization artifacts** — strongest for legal moves, commitments, terminal conditions, and state transitions.
2. **Argumentative dialogue corpora** — strongest for learning empirical objection/reply and relation transitions.
3. **General dialogue-quality controls** — useful for contextual response appropriateness, but not substitutes for argument-game semantics.

Search and verification relied on the repository's previously verified disputation/dialectical literature lane plus primary publisher or ACL records for benchmark details. Search-result snippets were not treated as evidence. The local disputation lane explicitly identifies the recurring computational primitives as legal moves, commitments, attacks/support, critical questions, dialogue termination, and semantic evaluation.

## Findings

### Best protocol and commitment foundations

- **Uckelman (2013)** is the closest formal analogue to a regulated objection/reply game: alternating Opponent/Respondent moves, a positum, rule-governed responses, and a terminal consistency condition. It is not a released ML benchmark, but it is the best reference for transition legality and state semantics.
- **Maudet, Parsons & Rahwan (2007)** is the best protocol-design source for commitment rules, locutions, critical questions, commencement, combination, and termination. It supplies reusable vocabulary and design constraints rather than a single train/test corpus.
- **CPD/SDA (2026)** is the strongest directly relevant commitment-aware empirical artifact in this scan. Its courtroom move taxonomy treats dialogue moves through commitment effects and evaluates strategic assessment. It should be used as a domain-specific quality/strategy layer, not as the sole legality model.

### Best empirical objection/reply transition corpora

- **SAD (2026)** is the strongest large-scale transition corpus: it contains long ChangeMyView histories, reply chains, stance, and five strategy labels (Question, Causality, Example, Analogy, Statement). It is especially reusable for learning which move follows which history, although its labels are rhetorical rather than formal-game legal.
- **Wikipedia dispute tactics (2022)** is the strongest compact disagreement-resolution corpus for rebuttal, clarification, questioning, and attack tactics. It is useful for objection/reply taxonomy and soft quality priors.
- **ADEA (2024)** is the strongest graph-grounded ethical-dialogue artifact in the set. Its labeled utterances and linked argument graphs can support target selection and graph-consistency checks, but the release is German and does not expose a complete commitment ledger.
- **MAD (2026)** is the best multilingual option. IAT relations plus dialogue acts provide a principled intermediate representation for reconstructing objection/support/reply transitions across languages.
- **ArguNet/Kialo (2024)** is useful as a relation-extraction front end: it predicts argumentative relations with dialogue-act and context features, which can precede typed transition validation.

### Quality and structural backstops

- **MuTual (2020)** provides a strong general next-response appropriateness control with 8,860 multi-turn dialogues, but it is not argumentative and has no explicit commitments or move legality.
- **MT-Bench-101 (2024)** provides turn-level and task-level quality dimensions across 1,388 multi-turn dialogues and 4,208 turns. It is appropriate for general response-quality regression tests, not for proving that an objection or reply is legal in a dialogue game.
- **Dependency Dialogue Acts (2025)** provides linked dialogue-act structure over 33 multi-party sessions and 9,000+ units. It is useful for parsing transition structure and reply targets, but its intent inventory is broader than argumentation.

## Recommended reusable benchmark battery

1. **Protocol legality:** implement a small executable legality suite from Uckelman plus dialogue-game commitment/termination concepts from Maudet et al. Include illegal out-of-turn moves, unsupported commitment withdrawal, invalid reply targets, and premature termination.
2. **Commitment state:** use CPD/SDA move effects to define commitment-aware state updates and strategic-effect labels. Keep formal commitment state separate from courtroom-specific credibility proxies.
3. **Argument transition learning:** train/evaluate on SAD, Wikipedia dispute tactics, ADEA, MAD, and ArguNet/Kialo. Normalize labels into a project taxonomy such as `question`, `challenge`, `support`, `rebuttal`, `undercut`, `clarification`, `concession`, `withdrawal`, and `answer` while preserving original labels.
4. **Graph and provenance checks:** use ADEA argument links and ArguNet/Kialo relations to test that every objection/reply points to an existing claim or move and that support/attack polarity is preserved.
5. **General response quality:** add MuTual and MT-Bench-101 as non-argumentative controls for context use, relevance, and multi-turn response quality. Do not report their scores as dialogue-game legality.
6. **Multilingual robustness:** use MAD for cross-lingual act/relation transfer and retain language-specific performance breakdowns.

## Main gap

No single released benchmark found here jointly provides: (a) explicit commitment-store snapshots, (b) typed objection/reply transitions, (c) a complete legality oracle, and (d) human-validated response quality. The practical design is therefore a **composite battery**: formal protocol tests for legality, argumentative corpora for transition prediction, commitment-aware domain annotations for state effects, and general multi-turn benchmarks for quality controls.

## Source basis

- Uckelman, “Medieval Disputationes de obligationibus as Formal Dialogue Systems.” https://link.springer.com/article/10.1007/s10503-012-9266-7
- Maudet, Parsons & Rahwan, “Argumentation in Multi-Agent Systems: Context and Recent Developments.” https://web.mit.edu/irahwan/www/docs/argmas2006survey.pdf
- ADEA, “An Argumentative Dialogue Dataset on Ethical Issues Concerning Future A.I. Applications.” https://aclanthology.org/2024.lrec-main.38/
- SAD, “A Large-Scale Strategic Argumentative Dialogue Dataset.” https://aclanthology.org/2026.acl-long.1673/
- “How to disagree well: Investigating the dispute tactics used on Wikipedia.” https://aclanthology.org/2022.emnlp-main.252/
- “Exploiting Dialogue Acts and Context to Identify Argumentative Relations in Online Debates.” https://aclanthology.org/2024.argmining-1.4/
- MAD, “A Corpus of Multilingual Argumentative Deliberation.” https://aclanthology.org/2026.lrec-1.554/
- CPD/SDA, “Strategic Dialogue Assessment and the Crooked Path Dataset.” https://aclanthology.org/2026.dnd-17.1/
- MuTual, “A Dataset for Multi-Turn Dialogue Reasoning.” https://aclanthology.org/2020.acl-main.130/
- MT-Bench-101, “A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues.” https://aclanthology.org/2024.acl-long.401/
- “In Search of the Lost Arch in Dialogue: A Dependency Dialogue Acts Corpus for Multi-Party Dialogues.” https://aclanthology.org/2025.findings-acl.1032/

## Validation notes

The CSV contains 11 records with stable IDs, explicit artifact types, fit dimensions, limitations, and source URLs. “Partial” and “near” labels are intentional: they distinguish a reusable component from a benchmark that directly supplies a formal dialogue-game oracle.
