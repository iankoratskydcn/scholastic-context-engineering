# Direct-acquisition wave — download manifest

All files below were fetched on 2026-09-20 into `raw_data/`. Total size: ~36 MB, 1,270 files. No credentials or requests were used; all URLs were public at fetch time. Licenses/rights still apply — see `argument_mining_clean_access_inventory.csv` before any redistribution.

| Dataset | Local path | Verified contents |
|---|---|---|
| GDN-CC | `raw_data/gdn_cc/` | train/valid/test JSONL (1,601 train lines) + README |
| PERSPECTRUM | `raw_data/perspectrum/` | `perspectrum_with_answers_v1.0.json` (907 claims) + license.txt |
| KPA / ArgKP | `raw_data/kpa_argkp/` | arguments/key_points/labels CSVs, train+dev (5,584 arguments train) |
| SciARK | `raw_data/sciark/` | `SciARK.json`, keyed by source document filename |
| ECHR Argument Corpus | `raw_data/echr/echr_corpus.zip` | `ECHR_Corpus.json` (2.69 MB uncompressed), verified zip listing |
| CDCP | `raw_data/cdcp/cdcp_acl17.zip` | 2,928 files, train/test .json+.pipe annotations, verified zip listing |
| Argumentative Microtext Part 1 | `raw_data/argmicro_part1/repo/` | git clone; `corpus/en/` txt+xml+pdf per text |
| Argumentative Microtexts Part 2 | `raw_data/argmicro_part2/repo/` | git clone; `corpus/` txt+xml+pdf per text |
| ArgUNSC | `raw_data/argunsc/` | 4 CSVs incl. `base.csv` (13,868 lines) |

## Not yet fetched (license/rights review needed first)

- **AAEC v2** — open ZIP at TU Darmstadt, but academic/research-only license and third-party essay copyright; fetch after explicit scope confirmation.
- **AbstRCT** — open GitLab archive, CC BY-NC-SA 4.0 plus MEDLINE/PubMed source-text caveats.
- **IAM** — public GitHub repo, but license field is empty/null; hold until author clarifies reuse rights.
- **PERSUADE 2.0** — public but hosted on Google Drive with a password-protected test set; CC BY-NC-SA 4.0.
- **M-Arg** — public Zenodo archive (435 MB) with research/education/evaluation-only license.
- **CasiMedicos-Arg** — public Hugging Face dataset, but CC BY 4.0 vs CC0 license conflict must be resolved first.
- **CEDAR** — public 21 MB GitHub ZIP, Apache-2.0 repo license but no separate data license confirmed.
- **DebateSum** — public but ~1.25 GB Hugging Face CSV; pin a revision before fetching.
- **ARCT** — public GitHub repo; Room for Debate source-text rights belong to individual authors.
- **GerCCT** — public annotation/ID CSV only; tweet text explicitly not distributable.
- **ImageArg** — public annotation JSON; tweet/image content must be re-fetched via Twitter API and may be incomplete.
- **DialAM-2024** — public Hugging Face loader/source; no explicit dataset license found.
- **ArgSciChat** — public GitHub files, Apache-2.0 repo, but paper-excerpt content rights are separate.

See `argument_mining_request_packets.md` for the resources that require an author/provider request rather than direct fetch.
