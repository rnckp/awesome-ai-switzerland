# Research notes

Dated selection decisions and open checks for maintainers. Earlier audits are preserved in Git history; maintenance instructions live in [CONTRIBUTING.md](CONTRIBUTING.md).

## Review snapshot

- **Full ecosystem review:** September 26, 2026. **Targeted additions and list audit:** October 20, 2026.
- Evidence came from primary documentation, repository files and model/dataset cards. The October audit read all 141 retained Hack Apertus project READMEs. Applications, deployments, model inference and benchmark results were not independently exercised or reproduced.
- The latest full README link check covered **424 distinct HTTP(S) destinations: 422 reachable, one 404 and one 429**, detailed below. Local links, anchors and tables passed validation. Raw reports and source snapshots were not committed; HTTP success alone does not verify content or functionality.

## Open checks

Observations below are from **October 20, 2026**; recheck before changing an entry.

- [ETH AI Center](https://ai.ethz.ch/) returned a 404 with “Cache Server Error: Not found UA”, while primary-site search still identified it as the homepage. Retained pending resolution of that discrepancy.
- [Apertus 1.5 70B discussions](https://huggingface.co/swiss-ai/Apertus-v1.5-70B/discussions) returned 429 in the crawl and a targeted retry, but were readable through the browser. Retained as a rate-limit issue.
- Fresh content reads remained unavailable for Swisscom/KVANT details, the stepping stone wiki, Apertus Decide and the Kaggle fine-tuning notebook. Their descriptions still depend on earlier dated reviews.
- **Updated October 21:** ArchAI is the organizer-confirmed Liebefeld winner. Stregoni/B2Bern's reported third place has a source discrepancy, detailed below. No named online winners were established; [Devpost rules](https://hackapertus.devpost.com/rules) estimate October 23 at 12:00 CEST, subject to change.

## Selection decisions

- Independent implementations of the same hackathon challenge remain separate. Team copies and mirrors are not additional resources: use the listed [Fact Attack](https://github.com/JJukic/Apertus-Team-Fact-Attack-2026) and [B2Bern](https://github.com/Spaghetti-Overflow/hack-apertus-stregoni) repositories rather than the Felipe3052 and RenatoMignone copies.
- Read the linked branch and nested project documentation before rejecting a template root. [ApertusVote](https://github.com/CraigChiambiro/hackapertus-ost) uses the default `submission-only` branch; `main` retains an old template. Klartext and MergeProof document their implementations below the root.
- The [1.5 release overview](https://apertus-ai.org/articles/2026-07-apertus-1-5/) identifies 70B DPO as the final 70B model; it is not listed twice. The final 8B adds charter alignment. Experimental Apertus 2 infrastructure does not establish a released model.
- Authored model-card runtime instructions take precedence over generated launch snippets. Mock/replay results do not establish live inference, and matching quotations do not prove semantic correctness. Code licences do not automatically cover datasets, model heads, assets or dependencies; relevant exceptions remain beside entries in the README.

## Deferred resources

Selected candidates worth revisiting, based on the October 20 review and earlier unresolved findings. These are dated evidence gaps, not permanent assessments; older scaffold and unrelated-project exclusions remain in Git history.

| Candidate | Evidence needed before inclusion |
| --- | --- |
| [Bern Match](https://github.com/AnAsteria/Apertus_Hack) | An explicit project-code licence; its [attribution audit](https://github.com/AnAsteria/Apertus_Hack/blob/main/docs/attribution.md#repository-licence) states that no reuse grant was chosen. |
| [Apertus Nash](https://github.com/moncifem/apertus-nash), [Sovra Verify](https://github.com/yablokolabs/sovra-verify) | Explicit project-code licence grants; base-model licensing is insufficient. |
| [Bern Expertise Navigator](https://github.com/prachi-kedar/bern-expertise-navigator-final) | Apertus evaluation: reported results used the rules baseline despite an implemented model path. |
| [BernMiner](https://github.com/Trista1208/bernminer_lifescience) | Demonstrated Apertus-specific results and a substantive report; crawling is deterministic and matching can select other providers. The Coupur copy is not a separate candidate. |
| [FormRehearsal](https://github.com/sumit1717/formrehearsal-hack-apertus) | Useful live Apertus interpretation and qualifying deployment; the authored example makes no provider calls. |
| [Forester](https://github.com/bennyfathurr/Forester-Tower-Defense) | Documented fresh inference and completion of the pending asset audit. |
| [Apertus StressLab](https://github.com/Alextsvr/apertus-stresslab) | Restored public source or a confirmed replacement. Removed after repository/README 404s and an unsuccessful replacement search; deletion versus private visibility was not established. |


## Hack Apertus follow-up — October 21, 2026

Targeted GitHub discovery and awards correction; earlier full-review and full-link-audit dates/totals are unchanged. Public API searches returned 200 repositories for `"Hack Apertus" in:readme` (both 100-result pages), 91 for `hackapertus in:name,description,readme`, 22 for `apertus bern in:readme created:>=2026-10-17`, 20 for `apertus Liebefeld in:readme`, and one for `hackpertus in:name,description,readme`. All responses reported `incomplete_results: false`. The broad four-query set contained 218 distinct repositories; the separate recent-update/Liebefeld/alternate-spelling pass contained 27, with overlap. These are discovery results, not accepted submissions. Compared repository identities with the current list and screened unlisted documentation; selected additions received licence, report, inventory and source checks. New discovery does not imply recent creation.

### Awards

The [organizer's spotlight](https://www.linkedin.com/posts/hack-apertus_spotlight-on-for-the-winner-of-the-first-activity-7518206147535896576-Kmml) explicitly identifies **ArchAI, team EDUCATION, as the Liebefeld winner**, qualified for the Grand Finals.

The [jury member Susie Xi Rao's post](https://www.linkedin.com/posts/susie-xi-rao-a0199b15b_apertus-siliconlovefield-activity-7518031548185493504-F0oP) has an indexed excerpt naming EDUCATION first, Swiss-SDI runner-up and Stregoni third. Its accessible edited body names only EDUCATION. **Stregoni/B2Bern's third place is therefore reported with an explicit qualification**, rather than treated as independently corroborated. B2Bern's README identifies Stregoni and its members, but does not itself claim an award. No separate project was confidently mapped to the Swiss-SDI runner-up name. The eliainnocenti and RenatoMignone repositories are B2Bern team copies. No named online winners were established; October 23 remains the estimated announcement date.

### Additions

All seven additions have full Apache-2.0 code licence texts. Documentation, source data, datasets and auxiliary models retain their own terms. Paths below are relative to the linked repositories; files and reported results were inspected, not executed or independently reproduced.

| Project | Evidence and limits |
| --- | --- |
| [Gied voting-booklet NLI](https://github.com/pgied/apertushack-fact-checking-pub) | `track_2a/src/llm.py`, model configurations and report: sentence retrieval, translation, vote scoping and Apertus 1.5 NLI. Scores use the public challenge cases; processing times exclude inference latency. |
| [VoteLens](https://github.com/greateden/Hackathon26) | `track_2a/src/nli_judge.py`, report and `docs/evidence/release_smoke_20261014.json`: real 70B requests, quotation/vote-identity gates and negative coverage results. Development exposure and unpublished raw records limit reproduction. Bundled SentenceSwissBERT encoder is CC-BY-NC-4.0. |
| [SwissDoc Q&A](https://github.com/MrFreemanO/swissdoc-qa-apertus) | `track_2b/src/llm_server.py`, report and `eval/results_apertus-0.5b.json`: Mini 0.5B/1.5B generation and recorded answers. The 1.5 8B path is recommended, not the measured default. Twelve team-written summaries are illustrative; thresholds were tuned on the same small set. |
| [RelayZero](https://github.com/abhijeetnardele24-hash/relayzero) | `track_2b/src/backend/apertus_adapter.py`, report and `data/live_smoke_evidence.json`: three retained real-model incident extractions. The 24-incident comparison uses fixtures; operational safety and deployment isolation are not independently established. |
| [StudyBridge](https://github.com/dukeoghenefejiroduke/studybridge-apertus/tree/main/track_2b) | Report, ingestion/retrieval/tutoring modules and `src/app/llm_client.py`. One reported live request establishes basic integration only. No demonstrated learning benefit, broad accuracy or phone-local inference. Substantive nested project documentation qualifies despite the template root. |
| [Apertus Lightpath](https://github.com/theBlackfish01/ApertusNetworkGym) | Report, model cards, `track_2b/src/readers3.py`, decoding/training/simulation code and model-answer caches. Apertus 1.5 adaptations translate policies and compare readings. AI-written instructions, single training runs and simulated operators limit claims; no physical controller was exercised. |
| [Canis Apertus Lab](https://github.com/UrsushoribilisMusic/canis-hackapertus-track2b) | Report, `track_2b/src/backend/runtime.py` and `model_probe.py`: local generation and hidden-state/logit access, with distinct mock and lexical fallbacks. The small-model disposition study does not validate a general emotional state or correctness probability; iOS reference and Docker implementation are distinct. |

### Deferrals and exclusions

- Existing Bern Match, Apertus Nash and Sovra Verify still lack explicit project-code licences. Earlier unresolved candidates remain deferred; no later update resolving their gaps was established.
- Ari Widget Translator, Briefklar Desk, Scythe, Multilingual Review-Reply Triage, Polyglot Explainer and Nearby Stars have substantive code/reports, but their reports leave actual Apertus runs unmeasured or failed. Fixture/stub results are not successful model integration evidence. Template roots alone were not grounds for rejection.
- [PolisProof](https://github.com/chapaevv123/PolisProof) has an Apache notice and real original-2509 trivial smoke prompts, but `evidence/live/results.md` records zero successful application runs for every route. Minimal `POLISPROOF_OK` replies do not establish document-auditing behavior.
- Thalabus leaves component/data licensing unsettled; Sentinel x Apertus requires confirmation of pre-existing CORE rights. ChronoMine's report supplies no measured result supporting its broad deployment/compliance claims. Garden Oracle documents a client and licence notice, but no successful-run artifact or substantive technical report was established here.
- Omitted duplicate team copies, profile/event indexes, unrelated Apertus names and unfinished templates. Coverage remains selective.


### Verification

The prepared update adds seven resource bullets: 148 Hack Apertus entries and 262 overall (141 and 255 before this pass). The existing link helper checked all nine new README destinations: nine reachable, no likely broken links and no inconclusive results. Patch applicability, entry uniqueness, local document targets, follow-up heading and whitespace checks passed. No applications, model inference or benchmarks were run. This was a targeted link check; the October 20 full-crawl totals remain historical. The update was prepared as a patch because the renamed checkout was readable but outside the session's writable paths; the changes are now present in this checkout (confirmed October 22).


## New-contribution follow-up — October 22, 2026

Targeted discovery of new-to-list GitHub contributions, emphasizing the online and Liebefeld Hack Apertus rounds. This is not a new full ecosystem audit. The September 26 full-review date and October 20 full-link-check totals remain unchanged. A newly discovered entry need not be a newly created repository.

### Discovery and selection

Public GitHub repository searches returned 197 matches for `"Hack Apertus" in:readme` (both pages read), 88 for `hackapertus in:name,description,readme`, 17 for `apertus Liebefeld in:readme`, 16 for `apertus created:>=2026-10-17`, and one for `hackpertus in:name,description,readme`. Together these yielded 218 distinct repositories, 76 not linked under the same repository identity in the README. All search responses reported `incomplete_results: false`; search coverage is still selective. Read the available unlisted root READMEs, then inspected selected nested reports, file inventories, licences and implementation files.

Additional searches covered `apertus in:readme created:>=2026-10-17` (34 matches), `"Hack Apertus" in:readme pushed:>=2026-10-21` (four), and `apertus liebefeld in:readme fork:true` (20). A name/description search for Apertus repositories pushed since October 20 found nine, including the speculative-decoding study updated October 22. These searches helped find contributions outside the event-specific keywords; totals overlap and are not submission counts.

### Additions and refreshed entry

Added booklet-nli and llm-public-ai; refreshed the existing speculative-decoding entry in place.

| Project | Evidence and limits |
| --- | --- |
| [Large Canelé Model — booklet-nli](https://github.com/MidsummerYU/large-canele-model-2a) | Online OST challenge. Full Apache-2.0 code licence; documentation/report CC-BY-4.0 and OST data MIT. Read `track_2a/technical_report.md`, `src/booklet_nli/client.py`, `predict.py` and `evidence.py` under `track_2a/`, and retained advanced 8B test scores. The inventory includes CSCS 8B/70B response recordings and predictions. Recorded-call replay is distinct from fresh inference. Its test split comes from public data and shares booklets/votes with development; source-span matching retains the model quotation when no close match exists. No official hidden-test result is established. |
| [llm-public-ai](https://github.com/simonw/llm-public-ai) | Created October 20. Full Apache-2.0 licence; read README, `pyproject.toml` and `llm_public_ai.py`. Registers Public AI models with the LLM library and handles streaming and Apertus inline thinking markers. Author documentation describes recorded API tests and model-specific capabilities; this review did not run the plugin or verify a live endpoint. |
| [Apertus speculative decoding](https://github.com/swiss-ai/apertus-speculative-decoding) | Updated October 22. README and `pyproject.toml` identify a semester research project, an Apache-2.0 metadata declaration, streaming measurements, deployment controls and pinned runtime requirements. The tree exposes methods, results and research reports; organization ownership does not make these experiments a supported serving release. No bundled root `LICENSE` was available at the checked path. No speedup or correctness result was independently reproduced. |

### Liebefeld and other exclusions

- [fra-itc Bern Expertise Navigator](https://github.com/fra-itc/bern-expertise-navigator) was updated October 22 and has an Apache-2.0 licence and substantive implementation. Its current report still says all measured results are from the rules baseline, with Apertus evaluation and live figures pending. Deferred on the same evidence basis as the previously noted Bern Expertise Navigator; a reachable model-list endpoint does not establish successful application inference.
- The eliainnocenti and RenatoMignone B2Bern repositories remain team copies of the listed Stregoni project. The Coupur repository repeats the BernMiner team work. No additional distinct Liebefeld project meeting the current inclusion criteria was established in this pass; existing entries remain.
- The alternate Belegt repository (`chessoren/swiss`) and CLAUSESHIFT experiment repository (`guelmbaye/clauseshift_track2a`) are not additional independent projects alongside their already listed author repositories.
- Rütli explicitly leaves live Eunomia/Apertus integration unverified; BhashaCut reports API testing blocked. Apertus Lab reports narrow live experiments but its checked licence files cover a nested submission and vendored assets, without an established project-wide code grant. Kept out pending the missing evidence. Profile pages, event trackers, mock-only landing pages and unmodified templates are not project additions.

### Verification

The resource-count helper reports **264 resource-bullet entries overall, including 149 Hack Apertus entries** (262 and 148 before this pass). The targeted link helper checked the two added README destinations, the refreshed research entry and the newly linked deferred candidate: four reachable, no likely broken links and no inconclusive results. Entry uniqueness, local document targets, README contents anchors, table structure and `git diff --check` passed. Applications, model inference and benchmark reproduction were not run; no GitHub publication was requested.
