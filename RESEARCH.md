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
- No named online or Liebefeld winners were established in checked public organizer sources. [Devpost rules](https://hackapertus.devpost.com/rules) estimated the online announcement for October 23 at 12:00 CEST, subject to change. Repositories alone do not establish accepted submissions or awards.

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
