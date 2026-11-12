# Hack Apertus projects

[Back to Awesome AI Switzerland](README.md#hack-apertus-projects).

Selected projects from [Hack Apertus](https://hackapertus.ch/), reviewed October 9–November 12, 2026. Inclusion requires an explicit code licence, project-specific documentation, substantive implementation and concrete Apertus use. These are community prototypes and research tools; software and reported results were not independently tested.

The [official Hack Apertus project overview](https://hackapertus.ch/projects/overview) is the companion catalog maintained by the organizers. All 224 online-project records in its November 8 data snapshot were compared with this list on November 12. Projects without public reusable code, a clear code licence, substantive documentation or demonstrated Apertus use are omitted here; this list also retains qualifying projects found outside that catalog.

**Code is Apache-2.0 unless stated otherwise.** Datasets, models, dependencies and source materials retain their own terms; licence notices without bundled licence text are identified separately.

The online round closed on **October 16, 2026**; the separate [Liebefeld on-site event](https://hackapertus.ch/regions/bern-liebefeld) ran on **October 18–19**. The [published Liebefeld results](https://app.sprintd.org/events/hack-apertus-liebefeld) identify **ArchAI / EDUCATION first, B2Bern / Stregoni second, and Parlamentsthemen / Invincibles third**. Online awards were [announced on October 23](https://hackapertus.ch/online-hack); verified placements are noted beside the mapped projects. Checked **October 24, 2026**. Note that this list is independent and community-run and in no way associated with the official organisations. Directory inclusion therefore does not establish anything (e.g. submission acceptance, award etc).

<details>
<summary><strong>Table of Contents</strong></summary>

<ul>
  <li><a href="#liebefeld-on-site-projects">Liebefeld on-site projects</a></li>
  <li><a href="#evaluation">Evaluation</a></li>
  <li><a href="#document-understanding-and-grounded-answers">Document understanding and grounded answers</a></li>
  <li><a href="#robotics-and-mission-planning">Robotics and mission planning</a></li>
  <li><a href="#education-interviews-and-language">Education, interviews and language</a></li>
  <li><a href="#creative-tools-and-simulations">Creative tools and simulations</a></li>
  <li><a href="#health-food-and-personal-administration">Health, food and personal administration</a></li>
  <li><a href="#business-and-administrative-workflows">Business and administrative workflows</a></li>
  <li><a href="#auditing-action-controls-and-adaptation">Auditing, action controls and adaptation</a></li>
</ul>

</details>

## Liebefeld on-site projects

### Archives

- [ArchAI](https://github.com/kirtanp/hackpertus-archives) — **Liebefeld winner, team EDUCATION.** Swiss archive preparation and cited Q&A with Apertus 1.5, provenance-preserving exports, historical maps and evaluation tools. MIT code; archive data retain their terms, and citation checks do not establish answer correctness.
- [CORA](https://github.com/Anakalypto/CORA-Apertus) — Archive-metadata classification and enrichment with Apertus 1.5, provenance, retrieval and an exploration interface; extracted entities and summaries need review.
- [Stapfer evidence explorer](https://github.com/jean3P/bern-archives-apertus) — 1799 school-survey exploration with preserved transcriptions, retrieval, cited Apertus answers and separate saved-run review. MIT code; historical data retain their terms.

### Bern research and expertise matching

- [B2Bern](https://github.com/Spaghetti-Overflow/hack-apertus-stregoni) — **Liebefeld second place, team Stregoni.** Apertus-assisted investment/expertise briefs with source-backed claims, review and export; combined end-to-end acceptance checks remain incomplete.
- [Bern Fit](https://github.com/Grozby/kinder-bueno) — Company-to-Bern research matching with Apertus analysis, semantic search and source-quote checks. MIT; evaluation uses a small team-authored query set.
- [Bern Innovation Engine](https://github.com/davidbonaccorsi/hackapertusBern) — Bern research navigator with Apertus extraction/query expansion, vector retrieval and model-assisted filtering; traceability does not guarantee correct claims.
- [Bern Life](https://github.com/CPD9/bern-life) — Walkable Bern research navigator; Apertus expands queries and helps match institutional pages with quoted evidence.
- [mutz](https://github.com/beSaif/mutz) — Company one-pager to Bern expertise leads, using Apertus 1.5 and source quotations in a review interface. MIT.
- [RAGlette](https://github.com/Najahiri/mylife-with-tokens) — Apertus research agent over Bern institutional pages, with source-backed matches and editable slide/PDF export. GPL-3.0; the configured API receives prompts and retrieved text.
- [Saarlanders Research & Expertise Navigator](https://github.com/ksjayasankar/liebefeld-saarlanders) — Apertus-assisted needs extraction, Bern expertise retrieval and source-quoted explanations with a separate model check.

### Parliamentary topics

- [aperTOPic](https://github.com/matthvalette/aperTOPic) — Parliamentary search and APS topic classification with Apertus, a web service and local client; the technical report remains a template.
- [Dreamers ParlTopics](https://github.com/edu008/Dreamers4OpenParl) — OpenParlData classification with Apertus 1.5, APS/custom labels and evaluation tools; partial corpus labelling and coarse reference labels limit validation.
- [Parlamentsthemen](https://github.com/prakash-aryan/parlamentsthemen) — **Liebefeld third place, team Invincibles.** Parliamentary topic monitoring with an Apertus-derived [LoRA adapter and classification head](https://huggingface.co/merabro/Apertus-ParlTopics-8B), review UI and chat-model explanations.
- [ParlaRadar](https://github.com/sagnikdas-ml/Parliament_Classifier_Bern_Hackathon) — APS/custom-topic classification and news-claim review against parliamentary archives with Apertus 1.5, quote checks, abstention and human review. MIT; the earlier 8B benchmark was not rerun for the current 70B configuration and does not validate news checking.
- [ParlTopic](https://github.com/Felipe3052/hackapertus-openparldata) — Apertus topic-card classification with quoted evidence, batch/API workflows and a Streamlit review interface; offline replay and live inference are separate modes.
- [Querschnitt](https://github.com/mi11ione/querschnitt) — OpenParlData topic classification with APS/custom schemes, source-sentence evidence, review lanes and evaluation artifacts. The measured method requires endpoint log-probabilities and assistant prefill.
- [Unisono](https://github.com/Dinesh18S/parltopics) — Swiss parliamentary-topic classification with supporting sentences, search and human review; disclosed recall and long-document failures limit completeness.

## Evaluation

### Swiss factuality and legal benchmarks

- [Apertus-Recht](https://github.com/mi11ione/apertus-recht) — German/French/Italian minimal-pair evaluation of Art. 261bis StGB, with code-computed labels, recorded Apertus responses and a reusable scoring harness.
- [Inkraft](https://github.com/NWichter/Hack_Apertus_1B_Inkraft) — Trilingual Swiss social/health-insurance law benchmark with dated Fedlex evidence, earlier-law answer pairs and Apertus evaluation tools. Dataset: CDLA-Permissive-2.0.
- [leGML domain transfer](https://github.com/legml-ai/apertus-domain-transfer) — Swiss private-insurance law adaptation of original Apertus 8B, with published weights, German/French evaluation data and a web-search harness. Dataset: CDLA-Permissive-2.0; human accuracy audit remains pending.
- [Scrutineer](https://github.com/winsznx/scrutineer/tree/main/track_1b) — **Online Track 1B winner.** Multilingual Swiss federal-vote outcome benchmark with recorded Apertus responses, replayable scoring and a reported failed initial hypothesis.
- [Swiss Heritage Factuality](https://github.com/ChristoYusj/apertus-swiss-landmarks) — **Online Track 1B third place, team Red Pandas.** Four-language Swiss landmark benchmark with photo, text-only and trap questions, recorded responses and deterministic regrading.
- [Swiss HVET Eval](https://github.com/wortgefecht/apertus-swiss-hvet-eval) — Swiss vocational-education factuality benchmark for Apertus 1.5 8B, with cited answers, human validation and automated judging.
- [Swiss Reality Check](https://github.com/bhuwanb23/apertus) — Swiss knowledge, values and Alemannic-dialect evaluation with source-backed items and Apertus 1.5 8B artifacts; no 70B comparison is published.
- [Swiss Aargau Lucerne Legal QA](https://github.com/DanielaFshr/swiss-legal-ag-lu-qa) — Apertus 1.5 70B evaluation on German federal, Aargau and Lucerne law questions, with cited references, frozen responses and replayable scoring. Dataset: CDLA-Permissive-2.0. Single-curator and model-assisted adjudication limit ground-truth confidence.
- [Swiss Statute QA](https://github.com/bisale24-ops/swiss-statute-qa) — Multilingual Swiss federal-law benchmark with cited answers, historical statute versions and recorded Apertus 1.5 responses. Dataset: CDLA-Permissive-2.0.
- [SwissCivicQA-4L](https://github.com/Jann08/swisscivicqa/tree/main/track_1b) — **Online Track 1B runner-up, team Jann.** Swiss constitutional factuality benchmark in German, French, Italian and Romansh, with source-backed answers, recorded Apertus 1.5 8B responses and cross-language consistency scoring.

### Safety, culture and reliability probes

- [AirPatch](https://github.com/AhaWissenschaft/airpatch) — Tests Apertus code proposals in offline containers against hidden programming tests, with recorded responses, replay tools and negative results.
- [Apertus Red-Team Harness](https://github.com/devilking7x/apertus-redteam) — Seeded multilingual, prompt-injection and tool-use probes with response logs and heuristic scoring for human review.
- [EpiTrace](https://github.com/wanshuzhang-story/epitrace-apertus) — Tests whether Apertus treats repeated claims as independent evidence, using synthetic dossiers, recorded 8B/70B responses and offline scoring.
- [Apertus Choice Audit](https://github.com/ElmekaouiHaitham/apertus-track1a) — English/French/Arabic identity-cue and reasoning audit of Apertus 1.5 70B, with recorded responses, human review, CPU replay and a white-box supplement. Findings/data: CDLA-Permissive-2.0. Localised stimuli and corpus-tuned parsers limit comparisons.
- [Arifi multilingual factuality probes](https://github.com/arifiarber-sYn/hackapertus-1a) — Apertus 1.5 8B cultural, historical, legal and synthetic-persona probes across Albanian, German, French, Italian and English, with recorded-response replay and a fingerprint-checked live mode; narrow cases and string-based scoring limit generalisation.
- [K-Probe](https://github.com/iamhuman-cheolheelee/k-probe) — Korean factuality, cultural and safety probes with sourced cases, regex scoring, recorded Apertus 1.0/1.5 responses and a results dashboard. MIT.
- [Spoken-request refusal study](https://github.com/nourseen6/hack-apertus-redteam) — Text versus synthetic-speech safety responses from Apertus 1.5 8B/70B, with collection, judging and audit tools; harmful raw answers are withheld.
- [Vipunen](https://github.com/apn201/Vipunen-2B) — Apertus-driven red-teaming pipeline exploring Finnish poetic framing, with neutral public seeds and an operator console; original attack payloads are withheld.

## Document understanding and grounded answers

### Voting-booklet claims

- [Gied voting-booklet NLI](https://github.com/pgied/apertushack-fact-checking-pub) — Apertus 1.5 translation and claim classification over retrieved booklet sentences, with vote-scoped BM25 retrieval and verbatim evidence. Reported scores use the public challenge data.
- [Abstimmungsbüchlein Check](https://github.com/Rashad18236/hackapertus-voting-nli/tree/main/track_2a) — German/French/Italian voting-booklet claim checking with Apertus 1.5 8B, vote-scoped retrieval, page evidence and recorded evaluation runs; reported combined scores use estimated organizer reference values.
- [VoteLens](https://github.com/greateden/Hackathon26) — Apertus 1.5 voting-booklet NLI with retrieval, vote-identity/citation checks and failure-analysis artifacts; stricter output gates can reject correct labels. Bundled SentenceSwissBERT weights are CC-BY-NC-4.0.
- [Apertus Evidence Lab](https://github.com/hallzyx/apertus) — Multilingual voting-booklet classification with hybrid retrieval and a trained decision head over frozen Apertus 1.5; requires its specialized backend.
- [ApertusVote](https://github.com/CraigChiambiro/hackapertus-ost) — Voting-booklet text/PDF claim classification with Apertus 1.5 8B, retrieved passages and usage records; official held-out evaluation remains pending.
- [booklet-check](https://github.com/StuartYo/hack-apertus) — Voting-booklet NLI with local lexical/embedding retrieval, Apertus classification and evidence restored from PDF text.
- [Büchli](https://github.com/kaiser-data/hack-apertus-booklet-nli) — Multilingual voting-booklet claim checking with hybrid retrieval, Apertus decisions, page citations and visual evidence review.
- [ClaimLens](https://github.com/Xa4-wi/HackApertus) — Voting-booklet claim checking with Apertus 1.5, source-relative labels, quotations and PDF pages in German, French and Italian.
- [Fact Attack](https://github.com/JJukic/Apertus-Team-Fact-Attack-2026) — **Online Track 2A runner-up.** Multilingual voting-booklet claim verification with Apertus 1.5, hybrid page retrieval and cited evidence. The report identifies AGPL obligations for the PyMuPDF-based image.
- [GeaNaVid](https://github.com/NWichter/Hack_Apertus_2A_GeaNaVid) — Voting-booklet claim classification with Apertus 1.5, vote-scoped retrieval, cross-language translation, sentence/page evidence and recorded evaluation runs.
- [kanhe](https://github.com/hoongyu/kanhe) — Multilingual voting-booklet classification with Apertus 1.5, BM25 retrieval, checked quotations and cached evaluation responses.
- [Large Canelé Model — booklet-nli](https://github.com/MidsummerYU/large-canele-model-2a) — Apertus 1.5 8B/70B voting-booklet NLI with translated BM25 retrieval, source-span matching and recorded-call replay. Evaluation uses a split of the public dataset; unmatched model quotations can remain in the output.
- [OpenAlps](https://github.com/rohIta-k/OpenAlps) — Multilingual voting-booklet NLI with Apertus 1.5 8B/70B, hybrid retrieval and evidence-selection experiments.
- [yasuhito's voting-booklet NLI](https://github.com/yasuhito/hackapertus-ost) — Apertus 1.5 pipeline with retrieved source spans, native tool-call output and verbatim evidence restoration.

### Cross-language differences

- [Apertus Difference Ranker](https://github.com/ChenfWen/Apertus-Difference-Ranker/tree/main/track_2a) — Token-level semantic-difference ranking with frozen Apertus representations, DiffAlign and lightweight supervised models; default execution replays results.
- [CLAUSESHIFT](https://github.com/guelmbaye/clauseshift) — Cross-language difference scoring with a multilingual encoder, bounded Apertus judgments, conservative fallback and retained execution artifacts; no held-out final quality score is published.
- [Concordance](https://github.com/Ali-Aoun5/concordance-hackapertus) — Trilingual Swiss-law divergence review with rules, an Apertus 8B/70B cascade, quotation checks and recorded-response replay; findings need legal review.
- [Gleichlaut](https://github.com/mi11ione/gleichlaut) — Multilingual drug-reimbursement audit with Apertus-drafted French/Italian amendments and code-preserved numeric values; drafts need review.
- [Macagni/Kessler RSD adaptation](https://github.com/g1anci/hackapertus_submission_track_2_uzh_tk_gm_clean) — Apertus 1.5 8B adaptation for cross-language token-level differences, with synthetic-data, QLoRA/full-training and evaluation notebooks; teacher errors and development-set exposure limit conclusions.
- [PolyJudge](https://github.com/hasanssr/polyjudge-swissgov-rsd/tree/main/track_2a) — Swiss government-page semantic-difference detection with sentence alignment, Apertus verification and offline replay.
- [Reading semantic differences from Apertus](https://github.com/amunozo/apertus-swissgov-rsd) — **Online Track 2A winner, Alberto Muñoz Ortiz.** SwissGov-RSD experiments with Apertus 1.5 8B hidden states, fitted prediction heads, token heatmaps and CPU replay of saved features.
- [RöstiBridge](https://github.com/ChristoYusj/RoestiBridge) — Firefox extension highlighting possible cross-language differences with Apertus explanations and SwissGov-RSD evaluation/replay tools.
- [SpanDiff](https://github.com/moscraciunxxx/SpanDiff-HackApertus) — Token-level semantic-drift scoring with Apertus 1.5 8B hidden states, a fitted ridge model, development predictions and layer ablations; generates no text.
- [SplitAlign](https://github.com/sharonbasovich/splitalign) — Token-level differences between English and German/French/Italian Swiss government documents using hosted Apertus.
- [Tse-min](https://github.com/YinZhengxun/hack-apertus-tsemin/tree/main/track_2a) — Word-level semantic-difference scoring with Apertus judgments and token surprisal; requires endpoint support for prompt log-probabilities.
- [YT-APERTUS-RSD](https://github.com/tumatuma2/yt-uzh/tree/main/track_2a) — Experimental cross-language semantic-difference scoring using Apertus 1.5 70B prompt log-probabilities and linguistic segmentation; the report evaluates Fedlex samples, not the SwissGov-RSD challenge. Requires a compatible vLLM endpoint.

### Parliamentary and court records

- [Apertus Court Decisions](https://github.com/beyondExp/apertus-court-decisions) — Frozen Apertus 1.5 8B reader with a published Swiss court-ruling classification head; default execution checks the head and replays predictions.
- [Docket](https://github.com/owldevltd/docket-apertus) — Parliamentary PDF/scan extraction into source-linked affair records, with Apertus, field review and correction tools.
- [Gegenprobe](https://github.com/mi11ione/gegenprobe) — Swiss parliamentary-data census, repair plans and schema conversion, with optional Apertus review of difficult layouts and replayable evaluation artifacts.
- [ParliParla](https://github.com/Avonik/ParliParla) — Apertus 1.5 8B parliamentary-affair extraction into a common schema, with quote/span provenance and cross-parliament evaluation artifacts.
- [ParlPDFeCH](https://github.com/jkovatsch/ParlPDFeCH) — Parliamentary PDFs to eCH-0295/RDF with rules and published heads over Apertus 1.5 8B hidden states; model extraction needs its specialized backend. Heads: CC-BY-4.0.
- [SEVERIN](https://github.com/vero-code/severin) — Parliamentary-affair extraction with Apertus, typed schemas, PDF-page quotation checks and a source/extraction viewer.
- [Skony](https://github.com/ahmarkhhan/sfedly) — Parliamentary-document extraction with an Apertus client, source-linked field proposals and human-reviewed export; evaluation coverage is limited.
- [William](https://github.com/ChristoYusj/William) — Parliamentary-PDF extraction with Apertus 1.5 70B, page evidence, a Firefox extension, batch interface and API.

### Legal, administrative and document Q&A

- [SwissDoc Q&A](https://github.com/MrFreemanO/swissdoc-qa-apertus) — Local public-service Q&A with Apertus 1.1 Mini, BM25 retrieval, citations and extractive fallback. Small team-written corpus/evaluation; wrong source-present numbers can pass its guard.
- [Alpenrecht AI](https://github.com/Anakalypto/AlpenRecht) — Swiss legal Q&A with federal, cantonal and communal retrieval and citation checks; the author reports substantial factual errors.
- [Apertus Evidence Ledger](https://github.com/sgagestudio/apertus-evidence-ledger) — SQLite document retrieval with Apertus synthesis, exact-quote checks and a hash-based evidence ledger.
- [Apertus QA](https://github.com/ventolabs-hq/apertus-qa) — Spanish Q&A over local Argentine official-statistics snapshots; Apertus plans and phrases answers while code supplies numeric values.
- [Belegt](https://github.com/chessoren/Belegt) — Local Swiss Federal Constitution Q&A with Apertus, retrieval, exact-quotation checks, abstention and recorded evaluations. Apache-2.0 grant by notice.
- [ClearDesk](https://github.com/m7mdd77/cleardesk-apertus) — Local Apertus 1.5 CLI selecting a verified verbatim passage from four synthetic IT procedures, with abstention for unsupported questions.
- [Fedlex Answer](https://github.com/bisale24-ops/fedlex-answer) — German/French/Italian federal-law Q&A with local statutory retrieval, Apertus 1.5 generation and deterministic quotation/number checks.
- [Guichet](https://github.com/MidsummerYU/large-canele-model-2b) — Swiss administrative-procedure Q&A with Apertus 1.5 8B, ch.ch retrieval, per-sentence quotation checks and abstention.

### Letters and accessible language

- [BriefKlar](https://github.com/kiky97/briefklar) — Swiss administrative-letter explanations with Apertus, source-grounded extraction, calendar output and low-resource-language experiments.
- [Folio](https://github.com/ksmostofa/folio) — Source-document checklist workbench with Apertus extraction, exact quotation/page checks, preserved conditional wording and human review.
- [Klarbrief](https://github.com/JannetEkka/klarbrief) — Swiss-letter explanations with Apertus, quotation/date/amount checks, flagged unsupported points and recorded evaluation responses.
- [Klartext](https://github.com/LeFlegm/Klartext/tree/main/track_2b) — Swiss official-letter triage with source-span checks, deadline extraction and an Apertus 8B-to-70B cascade; evaluated on synthetic letters.
- [Leicht·Facile](https://github.com/bobrovsky420/leicht-facile) — Easy-language drafting of Swiss official texts with Apertus, sentence provenance, deterministic fact checks and human review.
- [Passerelle](https://github.com/Thanatos9404/passerelle) — Swiss-letter explanations with Apertus fact cards, back-translation checks and caseworker review indicators; language checks do not guarantee faithful translation.
- [QuietLetter](https://github.com/jacman1988-super/quietletter) — Local Apertus selection of requests and unclear passages from plain-text letters, with exact quotes and a separate literal-date scanner; it does not calculate legal deadlines.

### Privacy and redaction

- [Clausus](https://github.com/jou2512/clausus) — Confidential-content masking for text, slides and Swiss German audio, with Apertus detection, reversible placeholders and request receipts; evaluation reports residual leaks.
- [Redacta](https://github.com/kangraemin/redacta-apertus/tree/main/track_2b) — Swiss court-decision redaction proposals with rules, Apertus, clerk review and synthetic-name evaluation; identities can be missed.
- [Riserbo](https://github.com/AliceMessi/riserbo) — Reversible Swiss/Italian personal-data redaction with rules and local Apertus 1.5, including indirect identifiers; synthetic evaluation reports residual leaks.
- [Schild](https://github.com/ShenJun93/hack-apertus-schild/tree/main/track_2b) — Swiss personal-data redaction gateway with identifier rules, Apertus 1.5 detection and reversible placeholders; reported evaluations retain residual leaks.
- [Treuhand Shield](https://github.com/ctmakc/treuhand-shield) — Swiss fiduciary-document proxy with identifier rules, Apertus entity detection, reversible placeholders and audit records; detection is probabilistic.
- [Velum](https://github.com/calderbuild/velum) — Swiss court-decision anonymisation with Apertus entity detection, court-specific rules, deterministic edits and human review.

### Other evidence and extraction workflows

- [CiteOps](https://github.com/sidsri14/citeops) — Incident briefs from bounded, redacted log bundles with Apertus; checks reject invented event IDs and uncited hypotheses/actions.
- [ClearConsent](https://github.com/sese0318/clearconsent) — Research consent-form explanations with Apertus, quotation/number checks, missing-information questions and teach-back quizzes.
- [KMU-Compliance-Check](https://github.com/alexsuter16/kmu-compliance-check) — Swiss online-shop pre-check against selected legal requirements, with Apertus judgments, source evidence and draft corrections; limited page coverage and model errors require legal review.
- [LaporSiap](https://github.com/fadillaoegi/laporsiap-hacketon) — Indonesian scam-report preparation with Apertus, source-linked chronologies, mandatory review and export; it does not file reports.
- [Papertus](https://github.com/igorjovicic/papertus) — Swiss document assistant with Apertus extraction, QR decoding, checksum/arithmetic checks, cited reports and document Q&A.
- [StimmFolgen](https://github.com/Devpen787/stimmfolgen/tree/9e1c60845c64bbe2b810a08be67fe39d47e96904) — Swiss-vote evidence reader with Apertus 1.5 8B question interpretation, reviewed source wording and private local notes. One published AHV analysis; local inference uses a text-only MLX conversion, while the hosted demo sends public questions to Public AI.
- [TenderProof](https://github.com/Vishwa-docs/TenderProof) — Equipment-procurement review with Apertus extraction, encoded constraint checks and human evidence approval; solver results cover only encoded obligations.
- [Trace](https://github.com/owldevltd/trace-apertus) — Form-image geometry with Apertus interpretation of fields and spoken answers, source-linked values and human review; signature integration is mocked.

## Robotics and mission planning

- [Aperceptia](https://github.com/Gianl-cyber/Apertus2Track/tree/main/track_2a) — Local Qwen perception with Apertus 1.5 8B pick/place decisions, constrained output and rule-based refusal checks; missing objects and spatial reasoning errors limit plans. Challenge data: CC-BY-4.0.
- [RelayZero](https://github.com/abhijeetnardele24-hash/relayzero) — Apertus 1.5 incident-report extraction with source-linked claim reconciliation and reviewable briefings. Three-report live smoke evidence is separate from its fixture-based comparative benchmark; operational reliability is unestablished.
- [Checked rescue briefings](https://github.com/prakash-aryan/rescue-briefings-apertus) — Apertus 1.5 turns multilingual briefings into typed drone/ground-robot missions checked by deterministic rules. Simulated terrain and assumed operating limits; no physical or physics-engine validation.
- [Grounded Intent](https://github.com/AS8148/grounded-intent) — Local workcell-image interpretation with open vision models, Apertus reasoning, checked pick/place plans and a browser review interface; does not control a robot.
- [See It, Say It, Pick It — Asian Prompters](https://github.com/azamafridi23/see-it-say-it-pick-it-hack-apertus) — **Online Track 2A third place.** Object segmentation, scene graphs and Apertus planning/safety agents produce pick/place plans, clarification questions or refusals for the robotics challenge.
- [See It, Say It, Pick It — Claw & Order](https://github.com/d-er/see-it-say-it-pick-it) — Open-model perception and scene geometry feed Apertus 1.5 8B pick/place reasoning, checked by rules and a bounded correction loop. Single-image geometry and development-set tuning limit validation. Challenge data: CC-BY-4.0.
- [See It, Say It, Pick It — Gude2Learn](https://github.com/jdawnduan/Gude2Learn) — Local Ollama pipeline separating open-model perception from text-only Apertus planning, with geometric hints and saved response traces; held-out wording informed later rules.
- [See It, Say It, Pick It — Nightcats](https://github.com/u826318/see-it-say-it-pick-it) — Local Apertus reasoning with open vision models, staged caches, action compilation and submitted development/held-out artifacts.
- [See It, Say It, Pick It — Zemljic/Ryser](https://github.com/NoahZemljic/hack-apertus) — Apertus instruction parsing and planning with Qwen visual grounding, SAM segmentation and geometric scene graphs.
- [SwarmOps vision-language grounding](https://github.com/prakash-aryan/see-it-say-it-pick-it-apertus) — Separates perception, Apertus instruction parsing and deterministic pick/place planning for the ZHAW workcell challenge; single-view occlusion and object-identification errors remain.

## Education, interviews and language

- [StudyBridge](https://github.com/dukeoghenefejiroduke/studybridge-apertus/tree/main/track_2b) — Apertus study-material Q&A with retrieval, citations, quizzes and learner-progress tracking. One reported live request verifies basic integration, not tutoring effectiveness or answer accuracy.
- [Bewerbär](https://github.com/iatee/Hack-Apertus/tree/main/track_2a) — Apertus apprenticeship-interview practice in German, French, Italian and Swiss German, with voice integration and criteria-based feedback; dialect feedback is less reliable.
- [Interview Coach — Next Question](https://github.com/aliskin/apertus-interview-coach) — Apertus interview practice with a deterministic controller, multilingual feedback and development simulations; official benchmark and consumer-GPU validation remain outstanding.
- [Los emal!](https://github.com/Alise441/los-emal) — Zurich German listening practice with Apertus dialogue, comprehension feedback, speech tools and everyday scenarios; generated dialect lacks native-speaker evaluation.
- [Meditations RAG](https://github.com/YingzhiVA/meditations-Apertus-RAG) — Retrieves Marcus Aurelius passages through Apertus query transformation and safety routing, with source text and an evaluation workflow; English-only, small single-rater evaluation.
- [PrepTalk](https://github.com/ghwiegand/PrepTalk) — Apertus apprenticeship-interview coach in German, French and Italian, with rubric-based feedback, a terminal UI and evaluation tooling.
- [SmartStart Coach — AI-Powerd job interview](https://github.com/bouchnafoumayma-gif/SmartStart-Coach/tree/main/track_2a) — Apprenticeship-interview practice with Apertus 1.5 8B, deterministic question flow and rubric-based feedback. Recorded live checks cover French; German/Italian validation and exclusion of distress answers from scoring remain outstanding.
- [SmartStart](https://github.com/Henryhuangsice/smartstart-hackapertus) — Apertus interview coach with adaptive follow-ups, FHGR rubric retrieval, a web UI and separate assessment/consistency evaluations.
- [SONA Isochron](https://github.com/SONALAB-EU/sona-isochron) — **Online Track 2B third place, team SONALAB.** Apertus translates and shortens dubbing lines into German/French, with length budgets, meaning checks and repair-loop experiments.
- [Zusage](https://github.com/shi1720/zusage) — Apertus 1.5 8B interview coach for Swiss apprenticeships, with a web interface and separate offline-demo and real-inference modes.

## Creative tools and simulations

- [Apertus Mundus](https://github.com/zRICGao/Apertus-Mundus) — Apertus narrative-roleplaying workbench with branching proposals, deterministic world-state updates, scoped memories and versioned saves; concurrent deployment remains unvalidated.
- [FRACTRA](https://github.com/sharmainelerato-glitch/FRACTRA) — Organisational dependency/failure simulation with a deterministic engine and Apertus-assisted interpretation and scenario proposals; repeatability does not establish simulation validity.
- [GemeindeSim](https://github.com/hatif03/gemeindesim) — Apertus 1.5 generative-agent town exploring responses to municipal policies and budgets; exploratory simulation, not a validated policy forecast.
- [Kampung Sambau — Of the Dark](https://github.com/ratafani/Scary-Gate-Keeper) — Browser night-watch mystery with Apertus 1.5 visitor dialogue in English/German; live Docker launch and aggregate model evaluation remain unverified by the author.
- [pAperSim](https://github.com/MykiellDeovennPagayonan/apertus-hackathon) — Apertus-assisted educational simulation authoring from registered components, with recipe validation and an editable browser workspace; rendering does not establish scientific validity.
- [PoesIA on Apertus](https://github.com/OomAngel/poesia-apertus) — Poetry workbench combining optional Apertus suggestions with deterministic metre/rhyme tools and human authorship. Apache-2.0 wrapper; MIT engine.
- [Sturmglocke](https://github.com/TusharTechs/sturmglocke) — **Online Track 2B winner, team Barry.** Crisis-staff training game with Apertus multilingual alerts, calls and debriefs, plus deterministic hazard-value checks; resident behaviour is illustrative.

## Health, food and personal administration

- [AI Fridge Chef](https://github.com/williamcheung/aifridgechef) — Apertus food-image inventory and recipe suggestions with editable voice/text drafts; food recognition, nutrition and dietary claims require user review.
- [Alpenstroke](https://github.com/nikitojik/Alpenstroke) — Multilingual Apertus swimming-workout logging and planning, with deterministic training-load calculations and user-confirmed parsed workouts.
- [Bon·Appétit](https://github.com/kinnuworks/bon-appetit) — Maps Swiss receipt lines to food-composition data with Apertus, review queues and household purchase summaries; purchases are not dietary intake.
- [Comfort](https://github.com/sambutracy/Hospital-Records) — Patient-record workspace with local Apertus evidence retrieval and reviewed summaries; live visit-brief validation is pending and earlier journal outputs failed validation.
- [Inbrev](https://github.com/NWichter/Hack_Apertus_2B_Inbrev) — Apertus administrative inbox review for medical practices, with source quotations and human handling of symptom messages; synthetic evaluation does not establish clinical correctness.
- [LAMal Navigator](https://github.com/sachacoemelck/Health_Insurance_Apertus) — Swiss basic-insurance premium comparison with Apertus explanations, statutory retrieval and application/cancellation drafts; legal answers require review.
- [Ordner](https://github.com/Simlowker/ordner) — Swiss paperwork assistant combining rules, document extraction and local Apertus tools; prepares material without filing it. Synthetic-document and explanation errors are disclosed.
- [Referto Sovrano](https://github.com/nicholasbuenger/referto-sovrano) — Synthetic clinical-note structuring demo with local Apertus, de-identification, FHIR export and a hash-chain audit log; clinical validity and data residency are unverified. MIT.
- [SafeSignal](https://github.com/iancuileana83-lab/safesignal-apertus) — Apertus extracts suspected medicine side-effect reports with quotations, completeness rules and human-edited export; fictional-data demo, not medical advice or automated submission.

## Business and administrative workflows

- [APatent](https://git.rgross.ch/RGross/HackApertus) — EPO patent search, multilingual readings and drawing analysis with Apertus 1.5 8B/70B, source references and human review. Patentability and market estimates are unvalidated; PyMuPDF licensing obligations remain a release review item.
- [Apertus Draft Gate](https://github.com/ratchetcode/hermes-apertus-email/tree/main/track_2b) — Hermes email/newsletter drafting framework configured for Apertus, with minimised fictional contact context and local review/export commands; implements no mail sender.
- [Beneficia](https://github.com/Chinorab/beneficia/tree/main/track_2b) — Local beneficial-owner declaration drafts with Apertus extraction, line citations, deterministic ownership calculations and human-review queues.
- [HausPost](https://github.com/blucca/hauspost) — Multilingual Apertus tenant-update processing with source-linked repair briefs, follow-up drafts and coordinator review.
- [Mandate Desk](https://github.com/gracelee087/hack-apertus/tree/main/track_2b) — Apertus invoice processing bounded by client mandates, deterministic payment checks, approval queues and signed audit records; evaluation moves no money.
- [MergeProof](https://github.com/williamleewilliam1-star/mergeproof-hack-apertus/tree/main/track_2b/src/mergeproof) — Evidence-linked multilingual contributor summaries from public GitHub pull requests, with Apertus synthesis and deterministic fallback.
- [Mirror AI](https://github.com/13512716817qq-creator/MirrorAI-HackApertus) — Business-inquiry routing with deterministic field/resource matching, Apertus responses and human follow-up; offline demo mode is separate.
- [Quotelet Aperto](https://github.com/vickhunter/quotelet) — Apertus turns multilingual price lists into validated calculator configurations and quote wording; code computes amounts. Published comparison is replay-only. MIT.
- [REDRESS × Apertus](https://github.com/Mah-ux-dotcom/redress-ai) — Rule-based review of automated-decision notices, with Apertus translation/explanation drafts and lexical evidence checks; live and mock modes are separate.
- [Sovereign Market Brief](https://github.com/simonlin1212/sovereign-market-brief) — Multilingual Apertus market commentary from code-computed facts, with deterministic checks and retained blocked drafts; supports local inference.
- [Sovereign Trade Copilot](https://github.com/quaner1234-cmd/sovereign-trade-copilot) — Garment-trade inquiry analysis and reply drafting with Apertus, per-fact source spans and human approval checks.

## Auditing, action controls and adaptation

- [Apertus Lightpath](https://github.com/theBlackfish01/ApertusNetworkGym) — Fine-tuned Apertus 1.5 readers translate routing instructions into enforceable policies for an optical-network simulator, with disagreement review and recorded experiments. Synthetic instructions; no physical network controller was exercised.
- [Canis Apertus Lab](https://github.com/UrsushoribilisMusic/canis-hackapertus-track2b) — Local Apertus chat and document retrieval with an experimental hidden-state/logit disposition readout. Lexical fallback and mock mode are separate; the readout is not a calibrated correctness score.
- [Klar](https://github.com/0uternet/klar) — **Online Track 2B runner-up.** Web-accessibility pre-checks combining axe-core, Apertus 1.5 interpretation, source-quotation guards and human review. Recorded local runs and replay are available; live-page false positives remain a limitation and findings do not certify conformance.
- [Apertus Gate](https://github.com/ondmindmanagement-hub/apertus-gate) — Structured Apertus 1.5 risk review of proposed AI actions, producing allow, human-review or block decisions without executing actions.
- [Apertus Sovereign Operations Bridge](https://github.com/ambrosinistefan8-stack/apertus-sovereign-operations-bridge) — Apertus 1.5 fact extraction with deterministic conflict checks and human gates for proposed actions. Apache-2.0 notice; full licence text is linked, not bundled.
- [Bundesbrief](https://github.com/Powerworks-Global/bundesbrief) — Deterministic parliamentary-PDF extraction with optional local Apertus cross-checks, weighted review gates and a hash-chained ledger; default checks use a labelled stub.
- [FEDERAI](https://github.com/HesamSalehpour/federai-policy-assurance) — Apertus policy-document analysis with quotation matching, structured findings, hypothetical scenarios and human review; no expert-validated accuracy benchmark is published.
- [Lain ZIP](https://github.com/epsilon-lain/lain-brain/tree/codex/hack-apertus-model-training-20261015) — Checkable memory revision with Apertus 1.5 70B, recorded-response replay and separate Mini 0.5B adapter experiments. MIT; small mathematical pilots include false withdrawals and do not establish a general learning benefit.
- [LoRaclette](https://github.com/bdravec/loraclette) — Experimental Apertus bottleneck-adapter training and position sweeps; tested only on a small random model, not real 8B weights or the 4-bit path.
- [rosetta-flow](https://github.com/anesask/rosetta-flow) — Two-tier Apertus audit of agent traces, with checked source-step quotations, adaptation/evaluation artifacts and human-readable findings.
- [SafeRouter ReplayLab](https://github.com/sumplus-real/saferouter-replaylab) — Local Apertus proposals for bounded retry/cancellation scenarios, checked against a synthetic reference protocol and exported as replayable counterexamples.
- [ScopeLock Verify](https://github.com/agent3-666/scopelock-verify) — Creative-brief review with local Apertus suggestions, source links, human approval and bounded media-file checks; repaired-protocol results are small and separate from earlier evaluations.
- [Sigillum](https://github.com/chessoren/sigillum) — Static AI-project audit with Apertus evidence interpretation, rule-assigned grades, source references and review reports; grades do not certify residency or compliance.
- [Systemic Resilience Copilot](https://github.com/rostys-fintech/systemic-resilience-copilot) — Apertus structuring/explanation for rule-based banking ICT recovery scenarios, with explicit missing-evidence states; not a validated incident predictor. Apache-2.0 notice.

## Contributing and licence

Follow [CONTRIBUTING.md](CONTRIBUTING.md) to suggest a project or correction. This list is [CC0 1.0](LICENSE); linked projects and materials retain their own licences and terms.
