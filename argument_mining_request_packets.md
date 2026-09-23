# Request packets — gated / unavailable argument-mining resources

Each packet is ready to send with minimal edits (fill in your name/affiliation/intended use). None of these have been contacted yet.

---

## 1. UKP Sentential Argument Mining Corpus

- **Status:** request-required (repository exposes a "Request a copy" workflow)
- **Action:** Submit the request via the TU Darmstadt DSpace item page.
- **URL:** https://tudatalib.ulb.tu-darmstadt.de/items/18c6544d-fa61-4505-ae8f-1304352c06e6/request-a-copy?bitstream=90a1de18-7a2e-4706-89e6-cf8108cfd3e9
- **Note in request:** State research/testing use for argument-mining system evaluation; ask whether annotations (CC BY-NC) can be separated from source sentences for redistribution-safe use.

## 2. DARIUS (German learner-essay argumentation)

- **Status:** unavailable — OSF record currently shows only the paper PDF
- **Action:** Email the corresponding author of the LREC-COLING 2024 paper (https://aclanthology.org/2024.lrec-main.389/) asking whether/when the corpus will be released, and whether a pre-release copy is available for research testing.
- **OSF record to monitor:** https://osf.io/3t2w8/files/

## 3. Twitter Arguments, Facts and Sources (AFS)

- **Status:** request-required (paper states "available upon request to the authors")
- **Paper:** https://aclanthology.org/D17-1245/
- **Action:** Email the paper's authors requesting the annotated Grexit/Brexit tweet dataset. Ask specifically whether they can provide (1) tweet IDs, (2) annotations, (3) any legally redistributable text, (4) preprocessing/version details.
- **Caveat to note in reply:** hydration of any provided tweet IDs will be incomplete due to deletions/suspensions.

## 4. Real-world undercut corpus / QuoraAM

- **Status:** request-required — no public data or code package found
- **Paper:** https://aclanthology.org/2024.argmining-1.6/
- **Action:** Email the paper's authors requesting the 400-document / 326-undercut QuoraAM dataset for research testing use.

## 5. PerspectiveArg2024

- **Status:** request-required — explicit email-request workflow documented in the repository README
- **Contacts:** andreas.waldis@live.com or neele.falk@ims.uni-stuttgart.de
- **Repo:** https://github.com/Blubberli/perspective-argument-retrieval
- **Required in request:** intended use, and confirmation of safeguards against negative impact (data is anonymized, research/non-commercial only, must not be used for identity inference or vote manipulation, copyright attributed to SmartVote, CC BY-NC 4.0).

## 6. GAQCorpus

- **Status:** request-required — multi-step: request 3 of 4 underlying corpora from their original providers first, then forward confirmations to Grammarly
- **Underlying corpora to request first:** Yahoo L6, IAC v2, Yelp Open Dataset (obtain from their respective providers)
- **Then email:** peng.wang@grammarly.com with affiliation and intended use, plus proof of access to the above three corpora
- **Repo:** https://github.com/grammarly/gaqcorpus

## 7. Twitter Planned Parenthood Corpus (recovery, not a formal request)

- **Status:** request-or-recovery — paper says IDs/labels were hosted at joonsuk.org, but the live site no longer exposes the file
- **Action A (recovery):** Check the Wayback Machine for an archived copy of https://joonsuk.org/ around the 2021 ArgMining publication date.
- **Action B (request):** If not recoverable, email the paper's corresponding author (https://aclanthology.org/2021.argmining-1.1/) asking for the tweet-ID/label file.

---

## Tracking

| # | Resource | Contact/route | Sent? | Response |
|---|---|---|---|---|
| 1 | UKP Sentential Argument Mining Corpus | DSpace request-a-copy | no | — |
| 2 | DARIUS | author email | no | — |
| 3 | Twitter AFS | author email | no | — |
| 4 | QuoraAM undercut corpus | author email | no | — |
| 5 | PerspectiveArg2024 | andreas.waldis@live.com / neele.falk@ims.uni-stuttgart.de | no | — |
| 6 | GAQCorpus | peng.wang@grammarly.com (after 3 upstream requests) | no | — |
| 7 | Planned Parenthood Twitter | Wayback Machine, then author email | no | — |

Update this table as requests go out and responses arrive. Do not mark "done" until the actual data file is in hand and its license is recorded in `argument_mining_clean_access_inventory.csv`.
