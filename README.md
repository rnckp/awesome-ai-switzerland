# Awesome AI Switzerland

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Suggestions welcome](https://img.shields.io/badge/suggestions-welcome-brightgreen)](https://github.com/rnckp/awesome-ai-switzerland/issues/new)
[![License: CC0](https://img.shields.io/badge/license-CC0-blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-ai-switzerland.svg)](https://github.com/rnckp/awesome-ai-switzerland)
[![Last commit](https://img.shields.io/github/last-commit/rnckp/awesome-ai-switzerland)](https://github.com/rnckp/awesome-ai-switzerland/commits/main/)

A curated guide to [Apertus](https://www.apertus-ai.org/), the open multilingual model family from the [Swiss AI Initiative](https://www.swiss-ai.org/), developed by EPFL, ETH Zurich, and CSCS. Official models, reproducibility resources, tools, integrations, and community projects.

> Independent, community-maintained list; not affiliated with, sponsored by, or endorsed by Apertus or its institutions. “Official” denotes resources from the Apertus team or Swiss AI.

**List audit: October 20, 2026.** Last full ecosystem review: September 26, 2026; targeted additions through October 22.

<details>
<summary><strong>Table of Contents</strong></summary>

<ul>
  <li><a href="#start-here">Start here</a></li>
  <li><a href="#official-sites-and-documentation">Official sites and documentation</a></li>
  <li><a href="#official-models">Official models</a></li>
  <li><a href="#official-code-and-training-infrastructure">Official code and training infrastructure</a></li>
  <li><a href="#datasets-and-transparency">Datasets and transparency</a></li>
  <li><a href="#research-and-evaluation">Research and evaluation</a></li>
  <li><a href="#local-inference-and-serving">Local inference and serving</a></li>
  <li><a href="#community-quantizations-and-derivatives">Community quantizations and derivatives</a></li>
  <li><a href="#hosted-apis-and-cloud-deployment">Hosted APIs and cloud deployment</a></li>
  <li><a href="#applications-and-integrations">Applications and integrations</a></li>
  <li><a href="#hack-apertus-projects">Hack Apertus projects</a>
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
  </li>
  <li><a href="#community-and-contributing">Community and contributing</a></li>
</ul>

</details>

## Start here

- **Try chat:** [Public AI](https://publicai.co/) or the official [Apertus Mini WebGPU demo](https://huggingface.co/spaces/swiss-ai/apertus-mini-webgpu).
- **Download models:** [Swiss AI on Hugging Face](https://huggingface.co/swiss-ai) and the [model guide below](#official-models).
- **Run locally:** [Quickstart](https://apertus-ai.org/docs/quickstart/) and [local inference options](#local-inference-and-serving).
- **Build an application:** [Hosted APIs](#hosted-apis-and-cloud-deployment), [integration examples](#applications-and-integrations), and [fine-tuning recipes](https://github.com/swiss-ai/apertus-finetuning-recipes).
- **Study or reproduce:** [1.5 technical report](https://arxiv.org/abs/2610.15542), [training code](https://github.com/swiss-ai/pretrain-code), and [data reconstruction](https://github.com/swiss-ai/pretrain-data).

## Official sites and documentation

- [Apertus website](https://www.apertus-ai.org/) — Project home; [about and roadmap](https://apertus-ai.org/pages/about/) cover its mission, background, and plans.
- [Swiss AI Initiative](https://www.swiss-ai.org/) — Parent initiative; [ETH AI Center](https://ai.ethz.ch/), [EPFL AI Center](https://ai.epfl.ch/), and [CSCS](https://www.cscs.ch/) are the institutional homes.
- [Documentation hub](https://apertus-ai.org/pages/documentation/) — Downloads, technical resources, and policies; start with the [overview](https://apertus-ai.org/docs/overview/) and [FAQ](https://apertus-ai.org/docs/faq/).
- [Provider directory](https://apertus-ai.org/pages/get-started/) and [community showcase](https://apertus-ai.org/pages/get-showcase/) — Officially listed services and applications.
- [GitHub organization](https://github.com/swiss-ai) — Authoritative code index; includes other Swiss AI research alongside Apertus.
- [Hugging Face organization](https://huggingface.co/swiss-ai) — Authoritative models, datasets, collections, and demos.
- [News](https://apertus-ai.org/news/) and [newsletter](https://apertus-ai.org/subscribe/) — Updates, including [Apertus 1.5](https://apertus-ai.org/articles/2026-07-apertus-1-5/) and the [September 2026 ecosystem review](https://apertus-ai.org/articles/2026-09-apertus-1-5-ga/).
- [Apertus Charter](https://apertus-ai.org/pages/charter/) — Published behavioral principles.
- [Legal documentation](https://github.com/swiss-ai/apertus-legal) — Versioned licenses, usage and privacy policies, EU public summaries, and codes of practice; companion [licensing](https://apertus-ai.org/docs/tech/licensing/) and [safety](https://apertus-ai.org/docs/tech/safety/) guides.
- [Website source](https://github.com/swiss-ai/www-apertus) — Contribute fixes to the website and documentation.

## Official models

Use each model card for capabilities, access conditions, and installation instructions. Base checkpoints are intended for completion or further training; Instruct checkpoints are adapted for conversation.

| Family                               | Official weights                                                                                                                                                                                                                                                                                                              | Purpose                                                                                                |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Apertus 1.5**                      | [8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B) · [70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B) · [collection](https://huggingface.co/collections/swiss-ai/apertus-v15)                                                                                                                                       | Text and image input, experimental audio input, optional thinking; up to 262,144 tokens. Text output.  |
| **1.5 — long-context base**          | [8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B-base) · [70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B-base)                                                                                                                                                                                                     | Pretraining checkpoints for completion or further training; no chat template.                          |
| **1.5 — intermediate post-training** | [8B SFT](https://huggingface.co/swiss-ai/Apertus-v1.5-8B-SFT) · [70B SFT](https://huggingface.co/swiss-ai/Apertus-v1.5-70B-SFT) · [8B RL](https://huggingface.co/swiss-ai/Apertus-v1.5-8B-RL) · [70B RL](https://huggingface.co/swiss-ai/Apertus-v1.5-70B-RL) · [8B DPO](https://huggingface.co/swiss-ai/Apertus-v1.5-8B-DPO) | Training-stage checkpoints for studying behavior changes; access conditions and pinned runtimes apply. |
| **1.1 Mini — base**                  | [0.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B) · [1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B) · [4B](https://huggingface.co/swiss-ai/Apertus-v1.1-4B)                                                                                                                                                 | Smaller distilled text models.                                                                         |
| **1.1 Mini — Instruct**              | [0.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B-Instruct) · [1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B-Instruct) · [4B](https://huggingface.co/swiss-ai/Apertus-v1.1-4B-Instruct)                                                                                                                      | Compact conversational models.                                                                         |
| **1.1 Mini — quantized**             | [Collection](https://huggingface.co/collections/swiss-ai/apertus-mini) · [vLLM NVFP4A16 1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B-Instruct-vLLM-NVFP4A16)                                                                                                                                                       | Official MLX INT3/INT4/INT6 variants at all three sizes, plus the vLLM build.                          |
| **1.0 — base**                       | [8B](https://huggingface.co/swiss-ai/Apertus-8B-2509) · [70B](https://huggingface.co/swiss-ai/Apertus-70B-2509)                                                                                                                                                                                                               | Original September 2025 text checkpoints.                                                              |
| **1.0 — Instruct**                   | [8B](https://huggingface.co/swiss-ai/Apertus-8B-Instruct-2509) · [70B](https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509) · [collection](https://huggingface.co/collections/swiss-ai/apertus-v1)                                                                                                                      | Original chat models; 65,536-token context.                                                            |

Supporting models: [pretraining toxicity classifier](https://huggingface.co/swiss-ai/apertus-pretrain-toxicity) and [WavTokenizer checkpoint](https://huggingface.co/swiss-ai/wavtokenizer-large-unify-40token).

**Version matters:** 1.5 requires accepting access conditions and using custom Transformers/vLLM builds; tool calling is unsupported in thinking mode. Follow the authored [1.5 usage instructions](https://huggingface.co/swiss-ai/Apertus-v1.5-8B#how-to-use), checked October 20, 2026. Support for 1.0 does not imply support for 1.5.

## Official code and training infrastructure

### Training and data preparation

- [pretrain-code](https://github.com/swiss-ai/pretrain-code) and [Megatron-LM](https://github.com/swiss-ai/Megatron-LM) — 1.5 pretraining, context-extension and SFT launch scripts, and the underlying distributed training fork.
- [pretrain-data](https://github.com/swiss-ai/pretrain-data) — Reconstruct the pretraining corpus from its sources.
- [posttraining](https://github.com/swiss-ai/posttraining) — Supervised fine-tuning and alignment experiments.
- [LongContextQA](https://github.com/swiss-ai/LongContextQA) — Synthetic long-context retrieval, word-counting and document-ordering tasks used in Apertus 1.5 training.
- [verl](https://github.com/swiss-ai/verl) and [verl-recipe](https://github.com/swiss-ai/verl-recipe) — Swiss AI forks used for Apertus 1.5 reinforcement learning with verifiable rewards.
- [self-distillation](https://github.com/swiss-ai/self-distillation) — Self-distillation policy optimization code used for the 1.5 8B charter-alignment stage.
- [posttraining-data](https://github.com/swiss-ai/posttraining-data) — Download, standardize, filter, decontaminate, and mix post-training data.
- [apertus-finetuning-recipes](https://github.com/swiss-ai/apertus-finetuning-recipes) — Full-parameter and LoRA recipes using Transformers, TRL, and Accelerate; [walkthrough](https://apertus-ai.org/docs/tech/fine-tuning/) targets the original 8B/70B models.
- [multimodal-data](https://github.com/swiss-ai/multimodal-data) — Apertus 1.5 image/audio preparation, including a [dataset inventory](https://github.com/swiss-ai/multimodal-data/blob/main/datasets/DATASETS.md).
- [robots-txt-compliance](https://github.com/swiss-ai/robots-txt-compliance) — Web-data filtering and URL-checking tooling; [research site](https://data-compliance.github.io/).
- [llm-pretrain-data-toxicity-removal](https://github.com/swiss-ai/llm-pretrain-data-toxicity-removal) — Pretraining toxicity filtering.
- [pretraining-safety-annotation](https://github.com/swiss-ai/pretraining-safety-annotation) — Charter-guided data annotation pipeline.
- [audio-preprocessing](https://github.com/swiss-ai/audio-preprocessing) and [data-PDF-pipeline](https://github.com/swiss-ai/data-PDF-pipeline) — Speech processing and PDF corpus extraction tools.
- [Swiss-AI-Romansh-Scripts](https://github.com/swiss-ai/Swiss-AI-Romansh-Scripts) — Romansh pretraining and SFT corpus preparation for Apertus v1.
- [qat-suite](https://github.com/swiss-ai/qat-suite) — Distillation and quantization-aware training associated with Apertus Mini.

### Tokenization, conversion, and deployment

- [apertus-format](https://github.com/swiss-ai/apertus-format) — Chat-format library, [specification](https://github.com/swiss-ai/apertus-format/blob/main/docs/format.md), and examples.
- [apertus-omni-tokenizer](https://github.com/swiss-ai/apertus-omni-tokenizer) — Canonical 1.5 tokenizer construction and chat templates.
- [apertus-audio-tokenizer](https://github.com/swiss-ai/apertus-audio-tokenizer) and [WavTokenizer](https://github.com/swiss-ai/WavTokenizer) — Audio-tokenizer wrapper and underlying fork.
- [hfconverter](https://github.com/swiss-ai/hfconverter) — Megatron-to-Hugging-Face checkpoint conversion and consistency checks.
- [model-launch](https://github.com/swiss-ai/model-launch) — Alps model-launch CLI and official [1.5 inference Dockerfile](https://github.com/swiss-ai/model-launch/blob/main/images/vllm_apertus_1.5_release/Dockerfile).
- [serving-api](https://github.com/swiss-ai/serving-api) and [llm-proxy](https://github.com/swiss-ai/llm-proxy) — Swiss AI serving frontend, API proxy, and access-control infrastructure.
- [OpenTela](https://github.com/swiss-ai/OpenTela) — Distributed compute orchestration used by Swiss AI serving; [upstream project](https://github.com/eth-easl/OpenTela).
- [gh200-wheels](https://github.com/swiss-ai/gh200-wheels) — Wheels and images for NVIDIA Grace Hopper hardware.
- [model-compatibility-suite](https://github.com/swiss-ai/model-compatibility-suite) — Endpoint conformance and capability checks.

## Datasets and transparency

[All Swiss AI datasets](https://huggingface.co/swiss-ai/datasets) is the live catalog. Dataset licenses and access conditions vary; model licensing does not replace them.

- [Data transparency archive](https://github.com/swiss-ai/apertus-data-transparency) — Versioned training-dataset catalog with modalities, licenses, versions and processing metadata.
- **Web filtering:** [FineWeb tags](https://huggingface.co/datasets/swiss-ai/fineweb-compliant-tag), [FineWeb-2 tags](https://huggingface.co/datasets/swiss-ai/fineweb-2-compliant-tag), and [FineWeb-Edu tags](https://huggingface.co/datasets/swiss-ai/fineweb-edu-compliant-tag).
- **Robots.txt artifacts:** [English blocked domains](https://huggingface.co/datasets/swiss-ai/robots-txt-blocked-domains-english), [multilingual blocked domains](https://huggingface.co/datasets/swiss-ai/robots-txt-blocked-domains-multilingual), and [compressed files](https://huggingface.co/datasets/swiss-ai/fineweb-robots-txt-files-compressed).
- **Swiss language corpora:** [Swiss pretraining](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-swiss), [Romansh pretraining](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-romansh), [Romansh post-training](https://huggingface.co/datasets/swiss-ai/apertus-posttrain-romansh), and [backtranslated Romansh SFT](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-romansh-backtranslated-sft).
- **Text pretraining research:** [processed Project Gutenberg](https://huggingface.co/datasets/swiss-ai/project_gutenberg_preprocessed) and [poison/canary data](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-poisonandcanaries).
- **Post-training:** [SFT mixture](https://huggingface.co/datasets/swiss-ai/apertus-sft-mixture), [Africa SFT](https://huggingface.co/datasets/swiss-ai/africa-sft), and [Africa preferences](https://huggingface.co/datasets/swiss-ai/africa-preferences).
- **1.5 post-training releases:** [Text SFT mix](https://huggingface.co/datasets/swiss-ai/Apertus-v1.5-SFT-mix), [annotated preference pool](https://huggingface.co/datasets/swiss-ai/Apertus-v1.5-Preference-Pool), and [DPO training pairs](https://huggingface.co/datasets/swiss-ai/Apertus-v1.5-Preference-Data).
- **Instruction following:** [verified SFT](https://huggingface.co/datasets/swiss-ai/if-sft-verified-singleturn-all), [RL prompts](https://huggingface.co/datasets/swiss-ai/if-rl-singleturn-prompts), and [hard RL prompts](https://huggingface.co/datasets/swiss-ai/if-rl-singleturn-hard-prompts).
- **Multimodal source collections:** [NASA](https://huggingface.co/datasets/swiss-ai/nasa), [Our World in Data](https://huggingface.co/datasets/swiss-ai/owid), [Smithsonian](https://huggingface.co/datasets/swiss-ai/smithsonian), and [swisstopo](https://huggingface.co/datasets/swiss-ai/swisstopo).
- **Evaluation datasets:** [mLogiQA](https://huggingface.co/datasets/swiss-ai/mlogiqa), [MathQA](https://huggingface.co/datasets/swiss-ai/math_qa), [BLEnD sample](https://huggingface.co/datasets/swiss-ai/blend-sample), and [HalluLens](https://huggingface.co/datasets/swiss-ai/hallulens).
- **Safety evaluation artifacts:** [HarmBench](https://huggingface.co/datasets/swiss-ai/harmbench), [copyright classifier hashes](https://huggingface.co/datasets/swiss-ai/harmbench_copyright_classifier_hashes), [RealToxicityPrompts](https://huggingface.co/datasets/swiss-ai/realtoxicityprompts), and [PolygloToxicityPrompts](https://huggingface.co/datasets/swiss-ai/polyglotoxicityprompts).

### Corpus inspection tools

- [data-indexing](https://github.com/swiss-ai/data-indexing) and [dataset-browser](https://github.com/swiss-ai/dataset-browser) — Corpus search and local data inspection; infrastructure access may be required.
- [HEVS pretraining-data indexing](https://github.com/Reliable-Information-Lab-HEVS/apertus-pretraining-data-indexing) — Community detokenization, Elasticsearch indexing, and corpus inspection tools.

## Research and evaluation

### Papers and technical sources

- [Apertus technical report](https://arxiv.org/abs/2509.14233) — Original architecture, training, data, and evaluations; [report repository](https://github.com/swiss-ai/apertus-tech-report).
- [Apertus 1.5 technical report](https://arxiv.org/abs/2610.15542) — Multimodal continued pretraining, reasoning, post-training stages, ablations and evaluations; companion [release overview](https://apertus-ai.org/articles/2026-07-apertus-1-5/).
- [Apertus Mini: distillation and quantization](https://arxiv.org/abs/2605.29128) — Smaller-model family and compression methods.
- [Training Apertus on Alps](https://arxiv.org/abs/2604.12973) — HPC engineering and distributed-training lessons.
- [Web crawling opt-outs](https://arxiv.org/abs/2504.06219) — Measuring the effect of respecting data-source exclusions.
- [Positional fragility and memorization](https://arxiv.org/abs/2505.13171) — Memorization analysis; [Apertus reproduction code](https://github.com/swiss-ai/apertus-memorization).
- [xIELU activation](https://arxiv.org/abs/2411.13010) and [AdEMAMix optimizer](https://arxiv.org/abs/2409.03137) — Core architectural and optimization ingredients.
- [INCLUDE](https://arxiv.org/abs/2411.19799) and [Global MMLU](https://arxiv.org/abs/2412.03304) — Multilingual evaluation references.
- [Parity-aware BPE](https://arxiv.org/abs/2508.04796) — Cross-language tokenization research; [code](https://github.com/swiss-ai/parity-aware-bpe).
- [Research library](https://apertus-ai.org/pages/research/) and [Zotero group](https://www.zotero.org/groups/6385576/apertus) — Papers and supporting literature on data, optimization, safety, and serving.

### Research projects

- [ONWARD degeneration probes](https://github.com/swiss-ai/degeneration-probe) — Degeneration-onset datasets, hidden-state probes and false-alarm evaluation for original Apertus 8B Instruct and comparison models; [released probes](https://huggingface.co/collections/marcodene/onward-degeneration-probes). Research tooling, not a validated deployment safeguard.
- [SFT Data Scorer](https://github.com/aebelge/sftdashboard) — Dataset inspection, annotation and score-based selection dashboard with Apertus 1.5 dataset/scoring adapters. Research prototype; default scores are synthetic fixtures. MIT.
- [apertus-probes](https://github.com/swiss-ai/apertus-probes) — Hallucination probes and activation analysis.
- [apertus-translate](https://github.com/swiss-ai/apertus-translate) — Translation experiments and human-evaluation annotations.
- [vocab-reduction](https://github.com/swiss-ai/vocab-reduction) — Vocabulary-size optimization for training and inference.
- [prune-apertus-lm-head](https://github.com/swiss-ai/prune-apertus-lm-head) — 1.5 output-head conversion while retaining multimodal input token IDs.
- [Apertus RAG evaluation](https://github.com/swiss-ai/ml4science-apertus-rag-evaluation) — Research comparing retrieval, chunking, and reranking strategies.
- [Apertus speculative decoding](https://github.com/swiss-ai/apertus-speculative-decoding) — Swiss AI semester research project comparing Apertus 1.5 draft-model, n-gram and EAGLE decoding on CSCS Clariden, with streaming benchmarks and correctness controls; experimental, with pinned runtimes and target-specific heads. Apache-2.0 declared in package metadata.
- [apertus-tokenizer-development](https://github.com/swiss-ai/apertus-tokenizer-development) — Preliminary next-generation tokenizer research; not a released Apertus 2 model.

### Evaluation tools and results

- [Official evaluation guide](https://apertus-ai.org/docs/tech/evaluation/) — Benchmark entry point.
- [evals](https://github.com/swiss-ai/evals) and [evals-post-train](https://github.com/swiss-ai/evals-post-train) — Evaluation launchers and 1.5 post-training benchmark pipeline.
- [lm-evaluation-harness](https://github.com/swiss-ai/lm-evaluation-harness), [lighteval](https://github.com/swiss-ai/lighteval), and [MLLM-eval-suite](https://github.com/swiss-ai/MLLM-eval-suite) — Swiss AI evaluation forks and multimodal orchestration.
- [Evaluation dashboard source](https://github.com/swiss-ai/apertus-eval-dashboard) — Visualize results from Weights & Biases.
- [Charter alignment benchmark](https://github.com/swiss-ai/swiss-ai-charter-alignment-benchmark) — Research scaffold for measuring adherence to charter articles.
- [SwissLegalEvals](https://github.com/JoelNiklaus/SwissLegalEvals) — Independent Swiss legal benchmarks and [2026 Apertus comparison](https://github.com/JoelNiklaus/SwissLegalEvals/blob/main/blog/swiss-legal-evals-2026.md).
- [DS-NLP Lab: Apertus 1.5 8B evaluation](https://blog.nlp-lab.ai/2026/07/29/Apertus15Bench.html) — Independent write-up; [earlier 8B result files](https://github.com/unisg-ics-dsnlp/Apertus8B-Instruct-Benchmark-Results).
- [GuideLLM](https://vllm-project.github.io/guidellm/main/) — Serving-load benchmarking tool used in the official ecosystem review.

## Local inference and serving

| Tool                     | Apertus resources                                                                                                                                                                                                                                                           | Notes                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Transformers             | [Official guide](https://apertus-ai.org/docs/guides/transformers/) · [upstream model docs](https://huggingface.co/docs/transformers/model_doc/apertus) · [Swiss AI fork](https://github.com/swiss-ai/transformers)                                                          | Python loading; full multimodal 1.5 requires the model card's pinned fork.           |
| vLLM                     | [Official guide](https://apertus-ai.org/docs/guides/vllm/) · [1.5 instructions](https://huggingface.co/swiss-ai/Apertus-v1.5-70B#how-to-use) · [Swiss AI fork](https://github.com/swiss-ai/vllm) · [integration work](https://github.com/swiss-ai/vllm-apertus-integration) | GPU serving; use the prescribed revisions, parsers and containers.                   |
| SGLang                   | [Official guide](https://apertus-ai.org/docs/guides/sglang/) · [Swiss AI fork](https://github.com/swiss-ai/sglang) · [sglang-apertus](https://github.com/swiss-ai/sglang-apertus) · [Scratchpad](https://github.com/swiss-ai/Scratchpad)                                    | Original-model examples; 1.5 integration remains work in progress.                   |
| llama.cpp                | [Upstream](https://github.com/ggml-org/llama.cpp) · [experimental 1.5 branch](https://github.com/MichelRosselli/llama.cpp/tree/model/apertus-v1.5) · [maintainer discussion](https://huggingface.co/swiss-ai/Apertus-v1.5-8B/discussions/6)                                 | Experimental full 1.5 support: author-tested 8B; 70B unvalidated.                    |
| Ollama                   | [Official guide](https://apertus-ai.org/docs/user/ollama/) · [1.0 package](https://ollama.com/MichelRosselli/apertus) · [Mini package](https://ollama.com/MichelRosselli/apertus-v1.1)                                                                                      | Community-maintained packages.                                                       |
| LM Studio                | [Official guide](https://apertus-ai.org/docs/user/lmstudio/)                                                                                                                                                                                                                | Desktop UI for compatible local builds.                                              |
| Llamafile                | [Official guide](https://apertus-ai.org/docs/user/llamafile/)                                                                                                                                                                                                               | Package compatible GGUF models as executables.                                       |
| Open WebUI               | [Official guide](https://apertus-ai.org/docs/user/openwebui/)                                                                                                                                                                                                               | Chat frontend for local or hosted inference.                                         |
| MLX                      | [Official Mini collection](https://huggingface.co/collections/swiss-ai/apertus-mini) · [community 1.0 8B BF16](https://huggingface.co/mlx-community/Apertus-8B-Instruct-2509-bf16) · [1.5 builds below](#alternative-formats)                                               | Apple Silicon inference; full multimodal 1.5 requires an experimental mlx-vlm build. |
| Transformers.js / WebGPU | [Mini demo and source](https://huggingface.co/spaces/swiss-ai/apertus-mini-webgpu)                                                                                                                                                                                          | Browser-local inference with converted Mini weights.                                 |

## Community quantizations and derivatives

### Alternative formats

- **1.5 text-only 8B:** [Andreas Martin's Transformers conversion](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text), [Q8_0 GGUF](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text-Q8_0-GGUF), [Colby Q4_K_M GGUF](https://huggingface.co/Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF), and [m1rkocasu 4-bit DWQ MLX](https://huggingface.co/m1rkocasu/Apertus-v1.5-8B-text-MLX-4bit-DWQ) — Omit image/audio input. The Transformers conversion needs 4.56+ without a custom fork or remote code; access conditions apply.
- **OnPrem AI 1.5:** [8B FP8](https://huggingface.co/onprem-ai/Apertus-v1.5-8B-FP8), [70B FP8](https://huggingface.co/onprem-ai/Apertus-v1.5-70B-FP8), and [70B NVFP4](https://huggingface.co/onprem-ai/Apertus-v1.5-70B-NVFP4) — GPU quantizations with a [temporary vLLM build](https://github.com/onprem-ai/vllm-apertus-1p5).
- **Simon Bächler's 1.5 70B MLX:** [6-bit](https://huggingface.co/sbaechler/Apertus-v1.5-70B-FP6-mlx) and [8-bit](https://huggingface.co/sbaechler/Apertus-v1.5-70B-FP8-mlx) — Apple Silicon quantizations retaining image/audio input and text output; author-tested on an M5 Max with 128 GB unified memory. Gated downloads; follow the cards' pinned experimental mlx-vlm branch. Released mlx-vlm and mlx-lm do not support these builds.
- **Mini ONNX:** [0.5B](https://huggingface.co/onnx-community/Apertus-v1.1-0.5B-Instruct-QAD-INT4-ONNX), [1.5B](https://huggingface.co/onnx-community/Apertus-v1.1-1.5B-Instruct-QAD-INT4-ONNX), and [4B](https://huggingface.co/onnx-community/Apertus-v1.1-4B-Instruct-QAD-INT4-ONNX) — INT4 browser/runtime conversions.
- **Red Hat AI 1.0 FP8:** [8B Instruct](https://huggingface.co/RedHatAI/Apertus-8B-Instruct-2509-FP8-dynamic) — Dynamic FP8 conversion for compatible GPU serving.

**1.0 Instruct GGUF conversions:**

| Maintainer | 8B                                                                              | 70B                                                                              | Notes                                                                                                   |
| ---------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Unsloth    | [GGUF](https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF)            | [GGUF](https://huggingface.co/unsloth/Apertus-70B-Instruct-2509-GGUF)            | Also [8B bitsandbytes 4-bit](https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-unsloth-bnb-4bit). |
| Bartowski  | [GGUF](https://huggingface.co/bartowski/swiss-ai_Apertus-8B-Instruct-2509-GGUF) | [GGUF](https://huggingface.co/bartowski/swiss-ai_Apertus-70B-Instruct-2509-GGUF) | Alternative quantizations.                                                                              |
| redponike  | [GGUF](https://huggingface.co/redponike/Apertus-8B-Instruct-2509-GGUF)          | [GGUF](https://huggingface.co/redponike/Apertus-70B-Instruct-2509-GGUF)          | Linked by the official Ollama guide.                                                                    |

### Fine-tunes and adaptations

- [Apertus SEA-LION v4 8B](https://huggingface.co/aisingapore/Apertus-SEA-LION-v4-8B-IT) — AI Singapore's Southeast Asian language adaptation; [GGUF](https://huggingface.co/aisingapore/Apertus-SEA-LION-v4-8B-IT-GGUF) and [release collection](https://huggingface.co/collections/aisingapore/sea-lion-v4).
- [Apertus EstLLM](https://huggingface.co/tartuNLP/Apertus-EstLLM-8B-Instruct-0326) — TartuNLP's Estonian adaptation; [base checkpoint](https://huggingface.co/tartuNLP/Apertus-EstLLM-8B-1125) and [paper](https://arxiv.org/abs/2603.02041).
- **Apertus MeditronFO:** [8B](https://huggingface.co/EPFLiGHT/Apertus-8B-MeditronFO) and [70B](https://huggingface.co/EPFLiGHT/Apertus-70B-MeditronFO) — Medical research models; [training pipeline](https://github.com/EPFLiGHT/FullyOpenMeditron) and [paper](https://arxiv.org/abs/2605.16215).
- [Greek Apertus](https://github.com/eellak/greek-apertus) — Greek adaptation of original Apertus 8B; [continued-pretraining weights](https://huggingface.co/glossAPI/apertus-8b-greek-cpt) and [instruction-tuned v0.5 preview](https://huggingface.co/glossAPI/greek-apertus-8b-instruct). Apache-2.0 weights; gated downloads.
- [Apertus Decide](https://huggingface.co/andreasmartin/apertus-v1.1-swiss-decide-0.4b-bidir) — Experimental Mini-derived bidirectional encoder for runtime-defined choices, ordered scores and boolean decisions; [playground/API](https://huggingface.co/spaces/andreasmartin/apertus-decide). Non-generative; confidence is not probability of correctness. Apache-2.0.
- [Andreas Martin's Apertus collection](https://huggingface.co/collections/andreasmartin/apertus) — Experimental and educational 1.1 Mini and 1.5 embedding conversions, text-only formats and a biomedical fine-tune.

### Community fine-tuning tutorials

- [Hack Apertus SFT notebook](https://www.kaggle.com/code/andreasmartinch/sft-apertus-v1-5-8b-hack-apertus-template) — Andreas Martin's 1.5 8B fine-tuning template for FHNW Business students in Hack Apertus; author-tested on Kaggle and CSCS JupyterLab (Clariden).

## Hosted APIs and cloud deployment

### Providers and managed deployment

Sources: official [directory](https://apertus-ai.org/pages/get-started/), [ecosystem review](https://apertus-ai.org/articles/2026-09-apertus-1-5-ga/) and provider catalogs. Check each provider for current versions, modalities, context limits and pricing.

| Provider         | Resources                                                                                                                                                                                                                               | Access                                        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Swisscom         | [Apertus 1.5 70B docs](https://docs.cloud.swisscom.ch/guide/cloud-services/aip/models/apertus-1_5_70B)                                                                                                                                  | Swiss AI Platform API.                        |
| Infomaniak       | [AI Services catalog](https://www.infomaniak.com/en/hosting/ai-services/open-source-models)                                                                                                                                             | Swiss-hosted API; lists 1.5 70B as beta.      |
| PHOENIQS / KVANT | [Active models](https://documentation.kvant.cloud/maas/active-models/)                                                                                                                                                                  | Enterprise model service.                     |
| Safe Swiss Cloud | [Private AI](https://safeswisscloud.com/en/private-ai/)                                                                                                                                                                                 | Managed private AI; lists 1.5 70B.            |
| stepping stone   | [AI on demand](https://www.stepping-stone.ch/en/products/artificial-intelligence/ai-on-demand-powered-by-swiss-ai-initiative) · [deployment notes](https://wiki.stoney-cloud.com/wiki/AI_on_demand:_apertus-ai/Apertus-v1.5-8B)         | Managed 1.5 8B service.                       |
| Public AI        | [Chat](https://publicai.co/) · [developer platform](https://platform.publicai.co/) · [API reference](https://platform.publicai.co/api) · [Hugging Face integration](https://huggingface.co/docs/inference-providers/providers/publicai) | Hosted chat and API.                          |
| Featherless      | [Apertus catalog](https://featherless.ai/models?families=apertus) · [deployment guide](https://apertus-ai.org/docs/deploy/featherless/)                                                                                                 | Serverless inference.                         |
| Regolo           | [Apertus model page](https://regolo.ai/models-archive/apertus-70b-2509/)                                                                                                                                                                | Original 70B via `apertus-70b`.               |
| OnPrem AI        | [Model catalog](https://www.onprem.ai/en/ai-llm-models/)                                                                                                                                                                                | On-premise enterprise deployment and support. |

### Deploy on your own cloud infrastructure

- [Exoscale](https://apertus-ai.org/docs/deploy/exoscale/) — Official guide and [dedicated inference offering](https://www.exoscale.com/ai-cloud-infrastructure/dedicated-inference/).
- [AWS SageMaker AI](https://apertus-ai.org/docs/deploy/sagemaker/) — Draft official guide and [AWS walkthrough](https://aws.amazon.com/blogs/alps/switzerlands-open-source-apertus-llms-now-available-on-amazon-sagemaker-ai/).
- [Microsoft Azure](https://apertus-ai.org/docs/deploy/azure/) — Draft official guide and [Azure Samples quickstart](https://github.com/Azure-Samples/swiss-llm-quickstart).
- [Google Vertex AI](https://apertus-ai.org/docs/deploy/vertex/) — Draft official guide; requires a custom vLLM container.
- [Community SageMaker Terraform](https://github.com/hueper/apertus-70b-infra) — Original 70B Instruct deployment with scheduled endpoint lifecycle management.

## Applications and integrations

### Chat, translation, and data tools

- [Lumo by Proton](https://proton.me/blog/lumo-apertus-partnership) — Assistant with Apertus 1.5 selection.
- [Euria](https://www.infomaniak.com/en/euria) — Infomaniak assistant with Apertus selection; [setup and kSuite integration](https://www.infomaniak.com/en/support/faq/2924/discover-euria-and-the-apertus-model).
- [Helvetra](https://helvetra.ch/) — Swiss-language translation; [backend source](https://github.com/Helvetra/backend).
- [AI Potluck](https://www.aipotluck.org/chat) — Alpha chat with inference traces; the [project](https://www.aipotluck.org/) names Apertus as its foundation, while the example trace uses Mistral.
- [Open Data Editor](https://opendataeditor.okfn.org/) — Tabular-data editor with local AI; [source](https://github.com/okfn/opendataeditor) defaults to original Apertus 8B GGUF.
- [ZüriCityGPT OSS](https://oss.zuericitygpt.ch/) — Liip's Apertus-backed RAG demo over Zurich city website content.

### SDKs, automation, and application examples

- [LiteLLM PublicAI provider](https://docs.litellm.ai/docs/providers/publicai) — Apertus routes for the Python SDK and proxy.
- [llm-public-ai](https://github.com/simonw/llm-public-ai) — Public AI provider plugin for Simon Willison’s LLM CLI/Python library, with Apertus model discovery, streaming and separation of 1.5 thinking output; endpoint capabilities vary by model.
- [Laravel Apertus](https://github.com/mmorand/laravel-apertus) — PHP/Laravel client with streaming and model listing.
- [ApertusSharp](https://github.com/bhrnjica/ApertusSharp) — .NET client using Microsoft.Extensions.AI, with Semantic Kernel integration.
- [Apertus n8n starter kit](https://github.com/aai-institute/apertus-n8n) — Python/curl extraction examples, three n8n workflows and local Ollama support; local tool calling is unsupported by the packaged model.
- [Apertus AI workshop](https://github.com/blancsw/apertus-ai-workshop) — Infomaniak RAG using original Apertus 70B generation with separate embedding and reranking models.
- [Emilie](https://github.com/veronica-builds/emilie) — Legal-document assistant with Apertus support and MCP case-law lookup.
- [CertusAI](https://github.com/saurluca/CertusAI) — Swiss AI Weeks 2025 legal assistant using Apertus.
- [Farmly](https://github.com/Kirchenfeldrobotics/Farmly-Swiss-AI-Weeks) — Liebefeld Swiss AI Weeks **2025** parcel-sharing prototype: original Apertus 70B request extraction, Flutter client and route-matching backend. PolyForm Noncommercial 1.0.0; external service credentials required.

## Hack Apertus projects

Selected projects from [Hack Apertus](https://hackapertus.ch/), reviewed October 9–22, 2026. Inclusion requires an explicit code licence, project-specific documentation, substantive implementation and concrete Apertus use. These are community prototypes and research tools; software and reported results were not independently tested.

**Code is Apache-2.0 unless stated otherwise.** Datasets, models, dependencies and source materials retain their own terms; licence notices without bundled licence text are identified separately.

The online round closed on **October 16, 2026**; the separate [Liebefeld on-site event](https://hackapertus.ch/regions/bern-liebefeld) ran on **October 18–19**. The organizer [confirms ArchAI (team EDUCATION) as the Liebefeld winner](https://www.linkedin.com/posts/hack-apertus_spotlight-on-for-the-winner-of-the-first-activity-7518206147535896576-Kmml). A [jury announcement](https://www.linkedin.com/posts/susie-xi-rao-a0199b15b_apertus-siliconlovefield-activity-7518031548185493504-F0oP) has an indexed excerpt reporting Stregoni/B2Bern in third place; its current body omits the runners-up, so that placing remains qualified. Checked **October 21**. [Devpost rules](https://hackapertus.devpost.com/rules) estimate the online winners announcement at **12:00 CEST on October 23, 2026**, subject to change. Note that this list is independent and community-run and in no way associated with the offical organisations. Directory inclusion therefore does not establish anything (e.g. submission acceptance, award etc).

### Liebefeld on-site projects

#### Archives

- [ArchAI](https://github.com/kirtanp/hackpertus-archives) — **Liebefeld winner, team EDUCATION.** Swiss archive preparation and cited Q&A with Apertus 1.5, provenance-preserving exports, historical maps and evaluation tools. MIT code; archive data retain their terms, and citation checks do not establish answer correctness.
- [CORA](https://github.com/Anakalypto/CORA-Apertus) — Archive-metadata classification and enrichment with Apertus 1.5, provenance, retrieval and an exploration interface; extracted entities and summaries need review.
- [Stapfer evidence explorer](https://github.com/jean3P/bern-archives-apertus) — 1799 school-survey exploration with preserved transcriptions, retrieval, cited Apertus answers and separate saved-run review. MIT code; historical data retain their terms.

#### Bern research and expertise matching

- [B2Bern](https://github.com/Spaghetti-Overflow/hack-apertus-stregoni) — **Reported Liebefeld third place, team Stregoni** (see award notes above). Apertus-assisted investment/expertise briefs with source-backed claims, review and export; combined end-to-end acceptance checks remain incomplete.
- [Bern Fit](https://github.com/Grozby/kinder-bueno) — Company-to-Bern research matching with Apertus analysis, semantic search and source-quote checks. MIT; evaluation uses a small team-authored query set.
- [Bern Innovation Engine](https://github.com/davidbonaccorsi/hackapertusBern) — Bern research navigator with Apertus extraction/query expansion, vector retrieval and model-assisted filtering; traceability does not guarantee correct claims.
- [Bern Life](https://github.com/CPD9/bern-life) — Walkable Bern research navigator; Apertus expands queries and helps match institutional pages with quoted evidence.
- [mutz](https://github.com/beSaif/mutz) — Company one-pager to Bern expertise leads, using Apertus 1.5 and source quotations in a review interface. MIT.
- [RAGlette](https://github.com/Najahiri/mylife-with-tokens) — Apertus research agent over Bern institutional pages, with source-backed matches and editable slide/PDF export. GPL-3.0; the configured API receives prompts and retrieved text.
- [Saarlanders Research & Expertise Navigator](https://github.com/ksjayasankar/liebefeld-saarlanders) — Apertus-assisted needs extraction, Bern expertise retrieval and source-quoted explanations with a separate model check.

#### Parliamentary topics

- [aperTOPic](https://github.com/matthvalette/aperTOPic) — Parliamentary search and APS topic classification with Apertus, a web service and local client; the technical report remains a template.
- [Dreamers ParlTopics](https://github.com/edu008/Dreamers4OpenParl) — OpenParlData classification with Apertus 1.5, APS/custom labels and evaluation tools; partial corpus labelling and coarse reference labels limit validation.
- [Parlamentsthemen](https://github.com/prakash-aryan/parlamentsthemen) — Parliamentary topic monitoring with an Apertus-derived [LoRA adapter and classification head](https://huggingface.co/merabro/Apertus-ParlTopics-8B), review UI and chat-model explanations.
- [ParlaRadar](https://github.com/sagnikdas-ml/Parliament_Classifier_Bern_Hackathon) — APS/custom-topic classification and news-claim review against parliamentary archives with Apertus 1.5, quote checks, abstention and human review. MIT; the earlier 8B benchmark was not rerun for the current 70B configuration and does not validate news checking.
- [ParlTopic](https://github.com/Felipe3052/hackapertus-openparldata) — Apertus topic-card classification with quoted evidence, batch/API workflows and a Streamlit review interface; offline replay and live inference are separate modes.
- [Querschnitt](https://github.com/mi11ione/querschnitt) — OpenParlData topic classification with APS/custom schemes, source-sentence evidence, review lanes and evaluation artifacts. The measured method requires endpoint log-probabilities and assistant prefill.
- [Unisono](https://github.com/Dinesh18S/parltopics) — Swiss parliamentary-topic classification with supporting sentences, search and human review; disclosed recall and long-document failures limit completeness.

### Evaluation

#### Swiss factuality and legal benchmarks

- [Apertus-Recht](https://github.com/mi11ione/apertus-recht) — German/French/Italian minimal-pair evaluation of Art. 261bis StGB, with code-computed labels, recorded Apertus responses and a reusable scoring harness.
- [Inkraft](https://github.com/NWichter/Hack_Apertus_1B_Inkraft) — Trilingual Swiss social/health-insurance law benchmark with dated Fedlex evidence, earlier-law answer pairs and Apertus evaluation tools. Dataset: CDLA-Permissive-2.0.
- [leGML domain transfer](https://github.com/legml-ai/apertus-domain-transfer) — Swiss private-insurance law adaptation of original Apertus 8B, with published weights, German/French evaluation data and a web-search harness. Dataset: CDLA-Permissive-2.0; human accuracy audit remains pending.
- [Scrutineer](https://github.com/winsznx/scrutineer/tree/main/track_1b) — Multilingual Swiss federal-vote outcome benchmark with recorded Apertus responses, replayable scoring and a reported failed initial hypothesis.
- [Swiss Heritage Factuality](https://github.com/ChristoYusj/apertus-swiss-landmarks) — Four-language Swiss landmark benchmark with photo, text-only and trap questions, recorded responses and deterministic regrading.
- [Swiss HVET Eval](https://github.com/wortgefecht/apertus-swiss-hvet-eval) — Swiss vocational-education factuality benchmark for Apertus 1.5 8B, with cited answers, human validation and automated judging.
- [Swiss Newcomer QA](https://github.com/MidsummerYU/large-canele-model-1b) — Four-language Swiss administrative-procedure benchmark for Apertus 1.5 8B/70B, with ch.ch sources, recorded answers and replay scoring.
- [Swiss Reality Check](https://github.com/bhuwanb23/apertus) — Swiss knowledge, values and Alemannic-dialect evaluation with source-backed items and Apertus 1.5 8B artifacts; no 70B comparison is published.
- [Swiss Statute QA](https://github.com/bisale24-ops/swiss-statute-qa) — Multilingual Swiss federal-law benchmark with cited answers, historical statute versions and recorded Apertus 1.5 responses. Dataset: CDLA-Permissive-2.0.
- [SwissCivicQA-4L](https://github.com/Jann08/swisscivicqa/tree/main/track_1b) — Swiss constitutional factuality benchmark in German, French, Italian and Romansh, with source-backed answers, recorded Apertus 1.5 8B responses and cross-language consistency scoring.

#### Safety, culture and reliability probes

- [AirPatch](https://github.com/AhaWissenschaft/airpatch) — Tests Apertus code proposals in offline containers against hidden programming tests, with recorded responses, replay tools and negative results.
- [Apertus Red-Team Harness](https://github.com/devilking7x/apertus-redteam) — Seeded multilingual, prompt-injection and tool-use probes with response logs and heuristic scoring for human review.
- [EpiTrace](https://github.com/wanshuzhang-story/epitrace-apertus) — Tests whether Apertus treats repeated claims as independent evidence, using synthetic dossiers, recorded 8B/70B responses and offline scoring.
- [K-Probe](https://github.com/iamhuman-cheolheelee/k-probe) — Korean factuality, cultural and safety probes with sourced cases, regex scoring, recorded Apertus 1.0/1.5 responses and a results dashboard. MIT.
- [Spoken-request refusal study](https://github.com/nourseen6/hack-apertus-redteam) — Text versus synthetic-speech safety responses from Apertus 1.5 8B/70B, with collection, judging and audit tools; harmful raw answers are withheld.
- [Vipunen](https://github.com/apn201/Vipunen-2B) — Apertus-driven red-teaming pipeline exploring Finnish poetic framing, with neutral public seeds and an operator console; original attack payloads are withheld.

### Document understanding and grounded answers

#### Voting-booklet claims

- [Gied voting-booklet NLI](https://github.com/pgied/apertushack-fact-checking-pub) — Apertus 1.5 translation and claim classification over retrieved booklet sentences, with vote-scoped BM25 retrieval and verbatim evidence. Reported scores use the public challenge data.
- [VoteLens](https://github.com/greateden/Hackathon26) — Apertus 1.5 voting-booklet NLI with retrieval, vote-identity/citation checks and failure-analysis artifacts; stricter output gates can reject correct labels. Bundled SentenceSwissBERT weights are CC-BY-NC-4.0.
- [Apertus Evidence Lab](https://github.com/hallzyx/apertus) — Multilingual voting-booklet classification with hybrid retrieval and a trained decision head over frozen Apertus 1.5; requires its specialized backend.
- [ApertusVote](https://github.com/CraigChiambiro/hackapertus-ost) — Voting-booklet text/PDF claim classification with Apertus 1.5 8B, retrieved passages and usage records; official held-out evaluation remains pending.
- [booklet-check](https://github.com/StuartYo/hack-apertus) — Voting-booklet NLI with local lexical/embedding retrieval, Apertus classification and evidence restored from PDF text.
- [Büchli](https://github.com/kaiser-data/hack-apertus-booklet-nli) — Multilingual voting-booklet claim checking with hybrid retrieval, Apertus decisions, page citations and visual evidence review.
- [ClaimLens](https://github.com/Xa4-wi/HackApertus) — Voting-booklet claim checking with Apertus 1.5, source-relative labels, quotations and PDF pages in German, French and Italian.
- [Fact Attack](https://github.com/JJukic/Apertus-Team-Fact-Attack-2026) — Multilingual voting-booklet claim verification with Apertus 1.5, hybrid page retrieval and cited evidence. The report identifies AGPL obligations for the PyMuPDF-based image.
- [GeaNaVid](https://github.com/NWichter/Hack_Apertus_2A_GeaNaVid) — Voting-booklet claim classification with Apertus 1.5, vote-scoped retrieval, cross-language translation, sentence/page evidence and recorded evaluation runs.
- [kanhe](https://github.com/hoongyu/kanhe) — Multilingual voting-booklet classification with Apertus 1.5, BM25 retrieval, checked quotations and cached evaluation responses.
- [Large Canelé Model — booklet-nli](https://github.com/MidsummerYU/large-canele-model-2a) — Apertus 1.5 8B/70B voting-booklet NLI with translated BM25 retrieval, source-span matching and recorded-call replay. Evaluation uses a split of the public dataset; unmatched model quotations can remain in the output.
- [OpenAlps](https://github.com/rohIta-k/OpenAlps) — Multilingual voting-booklet NLI with Apertus 1.5 8B/70B, hybrid retrieval and evidence-selection experiments.
- [yasuhito's voting-booklet NLI](https://github.com/yasuhito/hackapertus-ost) — Apertus 1.5 pipeline with retrieved source spans, native tool-call output and verbatim evidence restoration.

#### Cross-language differences

- [Apertus Difference Ranker](https://github.com/ChenfWen/Apertus-Difference-Ranker/tree/main/track_2a) — Token-level semantic-difference ranking with frozen Apertus representations, DiffAlign and lightweight supervised models; default execution replays results.
- [CLAUSESHIFT](https://github.com/guelmbaye/clauseshift) — Cross-language difference scoring with a multilingual encoder, bounded Apertus judgments, conservative fallback and retained execution artifacts; no held-out final quality score is published.
- [Concordance](https://github.com/Ali-Aoun5/concordance-hackapertus) — Trilingual Swiss-law divergence review with rules, an Apertus 8B/70B cascade, quotation checks and recorded-response replay; findings need legal review.
- [Gleichlaut](https://github.com/mi11ione/gleichlaut) — Multilingual drug-reimbursement audit with Apertus-drafted French/Italian amendments and code-preserved numeric values; drafts need review.
- [Macagni/Kessler RSD adaptation](https://github.com/g1anci/hackapertus_submission_track_2_uzh_tk_gm_clean) — Apertus 1.5 8B adaptation for cross-language token-level differences, with synthetic-data, QLoRA/full-training and evaluation notebooks; teacher errors and development-set exposure limit conclusions.
- [PolyJudge](https://github.com/hasanssr/polyjudge-swissgov-rsd/tree/main/track_2a) — Swiss government-page semantic-difference detection with sentence alignment, Apertus verification and offline replay.
- [Reading semantic differences from Apertus](https://github.com/amunozo/apertus-swissgov-rsd) — SwissGov-RSD experiments with Apertus 1.5 8B hidden states, fitted prediction heads, token heatmaps and CPU replay of saved features.
- [RöstiBridge](https://github.com/ChristoYusj/RoestiBridge) — Firefox extension highlighting possible cross-language differences with Apertus explanations and SwissGov-RSD evaluation/replay tools.
- [SpanDiff](https://github.com/moscraciunxxx/SpanDiff-HackApertus) — Token-level semantic-drift scoring with Apertus 1.5 8B hidden states, a fitted ridge model, development predictions and layer ablations; generates no text.
- [SplitAlign](https://github.com/sharonbasovich/splitalign) — Token-level differences between English and German/French/Italian Swiss government documents using hosted Apertus.
- [Tse-min](https://github.com/YinZhengxun/hack-apertus-tsemin/tree/main/track_2a) — Word-level semantic-difference scoring with Apertus judgments and token surprisal; requires endpoint support for prompt log-probabilities.

#### Parliamentary and court records

- [Apertus Court Decisions](https://github.com/beyondExp/apertus-court-decisions) — Frozen Apertus 1.5 8B reader with a published Swiss court-ruling classification head; default execution checks the head and replays predictions.
- [Docket](https://github.com/owldevltd/docket-apertus) — Parliamentary PDF/scan extraction into source-linked affair records, with Apertus, field review and correction tools.
- [Gegenprobe](https://github.com/mi11ione/gegenprobe) — Swiss parliamentary-data census, repair plans and schema conversion, with optional Apertus review of difficult layouts and replayable evaluation artifacts.
- [ParliParla](https://github.com/Avonik/ParliParla) — Apertus 1.5 8B parliamentary-affair extraction into a common schema, with quote/span provenance and cross-parliament evaluation artifacts.
- [ParlPDFeCH](https://github.com/jkovatsch/ParlPDFeCH) — Parliamentary PDFs to eCH-0295/RDF with rules and published heads over Apertus 1.5 8B hidden states; model extraction needs its specialized backend. Heads: CC-BY-4.0.
- [SEVERIN](https://github.com/vero-code/severin) — Parliamentary-affair extraction with Apertus, typed schemas, PDF-page quotation checks and a source/extraction viewer.
- [Skony](https://github.com/ahmarkhhan/sfedly) — Parliamentary-document extraction with an Apertus client, source-linked field proposals and human-reviewed export; evaluation coverage is limited.
- [William](https://github.com/ChristoYusj/William) — Parliamentary-PDF extraction with Apertus 1.5 70B, page evidence, a Firefox extension, batch interface and API.

#### Legal, administrative and document Q&A

- [SwissDoc Q&A](https://github.com/MrFreemanO/swissdoc-qa-apertus) — Local public-service Q&A with Apertus 1.1 Mini, BM25 retrieval, citations and extractive fallback. Small team-written corpus/evaluation; wrong source-present numbers can pass its guard.
- [Alpenrecht AI](https://github.com/Anakalypto/AlpenRecht) — Swiss legal Q&A with federal, cantonal and communal retrieval and citation checks; the author reports substantial factual errors.
- [Apertus Evidence Ledger](https://github.com/sgagestudio/apertus-evidence-ledger) — SQLite document retrieval with Apertus synthesis, exact-quote checks and a hash-based evidence ledger.
- [Apertus QA](https://github.com/ventolabs-hq/apertus-qa) — Spanish Q&A over local Argentine official-statistics snapshots; Apertus plans and phrases answers while code supplies numeric values.
- [Belegt](https://github.com/chessoren/Belegt) — Local Swiss Federal Constitution Q&A with Apertus, retrieval, exact-quotation checks, abstention and recorded evaluations. Apache-2.0 grant by notice.
- [ClearDesk](https://github.com/m7mdd77/cleardesk-apertus) — Local Apertus 1.5 CLI selecting a verified verbatim passage from four synthetic IT procedures, with abstention for unsupported questions.
- [Fedlex Answer](https://github.com/bisale24-ops/fedlex-answer) — German/French/Italian federal-law Q&A with local statutory retrieval, Apertus 1.5 generation and deterministic quotation/number checks.
- [Guichet](https://github.com/MidsummerYU/large-canele-model-2b) — Swiss administrative-procedure Q&A with Apertus 1.5 8B, ch.ch retrieval, per-sentence quotation checks and abstention.

#### Letters and accessible language

- [BriefKlar](https://github.com/kiky97/briefklar) — Swiss administrative-letter explanations with Apertus, source-grounded extraction, calendar output and low-resource-language experiments.
- [Folio](https://github.com/ksmostofa/folio) — Source-document checklist workbench with Apertus extraction, exact quotation/page checks, preserved conditional wording and human review.
- [Klarbrief](https://github.com/JannetEkka/klarbrief) — Swiss-letter explanations with Apertus, quotation/date/amount checks, flagged unsupported points and recorded evaluation responses.
- [Klartext](https://github.com/LeFlegm/Klartext/tree/main/track_2b) — Swiss official-letter triage with source-span checks, deadline extraction and an Apertus 8B-to-70B cascade; evaluated on synthetic letters.
- [Leicht·Facile](https://github.com/bobrovsky420/leicht-facile) — Easy-language drafting of Swiss official texts with Apertus, sentence provenance, deterministic fact checks and human review.
- [Passerelle](https://github.com/Thanatos9404/passerelle) — Swiss-letter explanations with Apertus fact cards, back-translation checks and caseworker review indicators; language checks do not guarantee faithful translation.
- [QuietLetter](https://github.com/jacman1988-super/quietletter) — Local Apertus selection of requests and unclear passages from plain-text letters, with exact quotes and a separate literal-date scanner; it does not calculate legal deadlines.

#### Privacy and redaction

- [Clausus](https://github.com/jou2512/clausus) — Confidential-content masking for text, slides and Swiss German audio, with Apertus detection, reversible placeholders and request receipts; evaluation reports residual leaks.
- [Redacta](https://github.com/kangraemin/redacta-apertus/tree/main/track_2b) — Swiss court-decision redaction proposals with rules, Apertus, clerk review and synthetic-name evaluation; identities can be missed.
- [Riserbo](https://github.com/AliceMessi/riserbo) — Reversible Swiss/Italian personal-data redaction with rules and local Apertus 1.5, including indirect identifiers; synthetic evaluation reports residual leaks.
- [Schild](https://github.com/ShenJun93/hack-apertus-schild/tree/main/track_2b) — Swiss personal-data redaction gateway with identifier rules, Apertus 1.5 detection and reversible placeholders; reported evaluations retain residual leaks.
- [Treuhand Shield](https://github.com/ctmakc/treuhand-shield) — Swiss fiduciary-document proxy with identifier rules, Apertus entity detection, reversible placeholders and audit records; detection is probabilistic.
- [Velum](https://github.com/calderbuild/velum) — Swiss court-decision anonymisation with Apertus entity detection, court-specific rules, deterministic edits and human review.

#### Other evidence and extraction workflows

- [CiteOps](https://github.com/sidsri14/citeops) — Incident briefs from bounded, redacted log bundles with Apertus; checks reject invented event IDs and uncited hypotheses/actions.
- [ClearConsent](https://github.com/sese0318/clearconsent) — Research consent-form explanations with Apertus, quotation/number checks, missing-information questions and teach-back quizzes.
- [KMU-Compliance-Check](https://github.com/alexsuter16/kmu-compliance-check) — Swiss online-shop pre-check against selected legal requirements, with Apertus judgments, source evidence and draft corrections; limited page coverage and model errors require legal review.
- [LaporSiap](https://github.com/fadillaoegi/laporsiap-hacketon) — Indonesian scam-report preparation with Apertus, source-linked chronologies, mandatory review and export; it does not file reports.
- [Papertus](https://github.com/igorjovicic/papertus) — Swiss document assistant with Apertus extraction, QR decoding, checksum/arithmetic checks, cited reports and document Q&A.
- [TenderProof](https://github.com/Vishwa-docs/TenderProof) — Equipment-procurement review with Apertus extraction, encoded constraint checks and human evidence approval; solver results cover only encoded obligations.
- [Trace](https://github.com/owldevltd/trace-apertus) — Form-image geometry with Apertus interpretation of fields and spoken answers, source-linked values and human review; signature integration is mocked.

### Robotics and mission planning

- [RelayZero](https://github.com/abhijeetnardele24-hash/relayzero) — Apertus 1.5 incident-report extraction with source-linked claim reconciliation and reviewable briefings. Three-report live smoke evidence is separate from its fixture-based comparative benchmark; operational reliability is unestablished.
- [Checked rescue briefings](https://github.com/prakash-aryan/rescue-briefings-apertus) — Apertus 1.5 turns multilingual briefings into typed drone/ground-robot missions checked by deterministic rules. Simulated terrain and assumed operating limits; no physical or physics-engine validation.
- [Grounded Intent](https://github.com/AS8148/grounded-intent) — Local workcell-image interpretation with open vision models, Apertus reasoning, checked pick/place plans and a browser review interface; does not control a robot.
- [See It, Say It, Pick It — Asian Prompters](https://github.com/azamafridi23/see-it-say-it-pick-it-hack-apertus) — Object segmentation, scene graphs and Apertus planning/safety agents produce pick/place plans, clarification questions or refusals for the robotics challenge.
- [See It, Say It, Pick It — Gude2Learn](https://github.com/jdawnduan/Gude2Learn) — Local Ollama pipeline separating open-model perception from text-only Apertus planning, with geometric hints and saved response traces; held-out wording informed later rules.
- [See It, Say It, Pick It — Nightcats](https://github.com/u826318/see-it-say-it-pick-it) — Local Apertus reasoning with open vision models, staged caches, action compilation and submitted development/held-out artifacts.
- [See It, Say It, Pick It — Zemljic/Ryser](https://github.com/NoahZemljic/hack-apertus) — Apertus instruction parsing and planning with Qwen visual grounding, SAM segmentation and geometric scene graphs.
- [SwarmOps vision-language grounding](https://github.com/prakash-aryan/see-it-say-it-pick-it-apertus) — Separates perception, Apertus instruction parsing and deterministic pick/place planning for the ZHAW workcell challenge; single-view occlusion and object-identification errors remain.

### Education, interviews and language

- [StudyBridge](https://github.com/dukeoghenefejiroduke/studybridge-apertus/tree/main/track_2b) — Apertus study-material Q&A with retrieval, citations, quizzes and learner-progress tracking. One reported live request verifies basic integration, not tutoring effectiveness or answer accuracy.
- [Bewerbär](https://github.com/iatee/Hack-Apertus/tree/main/track_2a) — Apertus apprenticeship-interview practice in German, French, Italian and Swiss German, with voice integration and criteria-based feedback; dialect feedback is less reliable.
- [Interview Coach — Next Question](https://github.com/aliskin/apertus-interview-coach) — Apertus interview practice with a deterministic controller, multilingual feedback and development simulations; official benchmark and consumer-GPU validation remain outstanding.
- [Los emal!](https://github.com/Alise441/los-emal) — Zurich German listening practice with Apertus dialogue, comprehension feedback, speech tools and everyday scenarios; generated dialect lacks native-speaker evaluation.
- [Meditations RAG](https://github.com/YingzhiVA/meditations-Apertus-RAG) — Retrieves Marcus Aurelius passages through Apertus query transformation and safety routing, with source text and an evaluation workflow; English-only, small single-rater evaluation.
- [PrepTalk](https://github.com/ghwiegand/PrepTalk) — Apertus apprenticeship-interview coach in German, French and Italian, with rubric-based feedback, a terminal UI and evaluation tooling.
- [SmartStart](https://github.com/Henryhuangsice/smartstart-hackapertus) — Apertus interview coach with adaptive follow-ups, FHGR rubric retrieval, a web UI and separate assessment/consistency evaluations.
- [SONA Isochron](https://github.com/SONALAB-EU/sona-isochron) — Apertus translates and shortens dubbing lines into German/French, with length budgets, meaning checks and repair-loop experiments.
- [Zusage](https://github.com/shi1720/zusage) — Apertus 1.5 8B interview coach for Swiss apprenticeships, with a web interface and separate offline-demo and real-inference modes.

### Creative tools and simulations

- [Apertus Mundus](https://github.com/zRICGao/Apertus-Mundus) — Apertus narrative-roleplaying workbench with branching proposals, deterministic world-state updates, scoped memories and versioned saves; concurrent deployment remains unvalidated.
- [FRACTRA](https://github.com/sharmainelerato-glitch/FRACTRA) — Organisational dependency/failure simulation with a deterministic engine and Apertus-assisted interpretation and scenario proposals; repeatability does not establish simulation validity.
- [GemeindeSim](https://github.com/hatif03/gemeindesim) — Apertus 1.5 generative-agent town exploring responses to municipal policies and budgets; exploratory simulation, not a validated policy forecast.
- [Kampung Sambau — Of the Dark](https://github.com/ratafani/Scary-Gate-Keeper) — Browser night-watch mystery with Apertus 1.5 visitor dialogue in English/German; live Docker launch and aggregate model evaluation remain unverified by the author.
- [pAperSim](https://github.com/MykiellDeovennPagayonan/apertus-hackathon) — Apertus-assisted educational simulation authoring from registered components, with recipe validation and an editable browser workspace; rendering does not establish scientific validity.
- [PoesIA on Apertus](https://github.com/OomAngel/poesia-apertus) — Poetry workbench combining optional Apertus suggestions with deterministic metre/rhyme tools and human authorship. Apache-2.0 wrapper; MIT engine.
- [Sturmglocke](https://github.com/TusharTechs/sturmglocke) — Crisis-staff training game with Apertus multilingual alerts, calls and debriefs, plus deterministic hazard-value checks; resident behaviour is illustrative.

### Health, food and personal administration

- [AI Fridge Chef](https://github.com/williamcheung/aifridgechef) — Apertus food-image inventory and recipe suggestions with editable voice/text drafts; food recognition, nutrition and dietary claims require user review.
- [Alpenstroke](https://github.com/nikitojik/Alpenstroke) — Multilingual Apertus swimming-workout logging and planning, with deterministic training-load calculations and user-confirmed parsed workouts.
- [Bon·Appétit](https://github.com/kinnuworks/bon-appetit) — Maps Swiss receipt lines to food-composition data with Apertus, review queues and household purchase summaries; purchases are not dietary intake.
- [Comfort](https://github.com/sambutracy/Hospital-Records) — Patient-record workspace with local Apertus evidence retrieval and reviewed summaries; live visit-brief validation is pending and earlier journal outputs failed validation.
- [Inbrev](https://github.com/NWichter/Hack_Apertus_2B_Inbrev) — Apertus administrative inbox review for medical practices, with source quotations and human handling of symptom messages; synthetic evaluation does not establish clinical correctness.
- [LAMal Navigator](https://github.com/sachacoemelck/Health_Insurance_Apertus) — Swiss basic-insurance premium comparison with Apertus explanations, statutory retrieval and application/cancellation drafts; legal answers require review.
- [Ordner](https://github.com/Simlowker/ordner) — Swiss paperwork assistant combining rules, document extraction and local Apertus tools; prepares material without filing it. Synthetic-document and explanation errors are disclosed.
- [Referto Sovrano](https://github.com/nicholasbuenger/referto-sovrano) — Synthetic clinical-note structuring demo with local Apertus, de-identification, FHIR export and a hash-chain audit log; clinical validity and data residency are unverified. MIT.
- [SafeSignal](https://github.com/iancuileana83-lab/safesignal-apertus) — Apertus extracts suspected medicine side-effect reports with quotations, completeness rules and human-edited export; fictional-data demo, not medical advice or automated submission.

### Business and administrative workflows

- [Apertus Draft Gate](https://github.com/ratchetcode/hermes-apertus-email/tree/main/track_2b) — Hermes email/newsletter drafting framework configured for Apertus, with minimised fictional contact context and local review/export commands; implements no mail sender.
- [Beneficia](https://github.com/Chinorab/beneficia/tree/main/track_2b) — Local beneficial-owner declaration drafts with Apertus extraction, line citations, deterministic ownership calculations and human-review queues.
- [HausPost](https://github.com/blucca/hauspost) — Multilingual Apertus tenant-update processing with source-linked repair briefs, follow-up drafts and coordinator review.
- [Mandate Desk](https://github.com/gracelee087/hack-apertus/tree/main/track_2b) — Apertus invoice processing bounded by client mandates, deterministic payment checks, approval queues and signed audit records; evaluation moves no money.
- [MergeProof](https://github.com/williamleewilliam1-star/mergeproof-hack-apertus/tree/main/track_2b/src/mergeproof) — Evidence-linked multilingual contributor summaries from public GitHub pull requests, with Apertus synthesis and deterministic fallback.
- [Mirror AI](https://github.com/13512716817qq-creator/MirrorAI-HackApertus) — Business-inquiry routing with deterministic field/resource matching, Apertus responses and human follow-up; offline demo mode is separate.
- [OriginPass CH–CN](https://github.com/sora200419/Hack-Apertus) — Swiss–China rules-of-origin decision support with Apertus classification/dossier drafting, deterministic rule traces and replay mode.
- [Quotelet Aperto](https://github.com/vickhunter/quotelet) — Apertus turns multilingual price lists into validated calculator configurations and quote wording; code computes amounts. Published comparison is replay-only. MIT.
- [REDRESS × Apertus](https://github.com/Mah-ux-dotcom/redress-ai) — Rule-based review of automated-decision notices, with Apertus translation/explanation drafts and lexical evidence checks; live and mock modes are separate.
- [Sovereign Market Brief](https://github.com/simonlin1212/sovereign-market-brief) — Multilingual Apertus market commentary from code-computed facts, with deterministic checks and retained blocked drafts; supports local inference.
- [Sovereign Trade Copilot](https://github.com/quaner1234-cmd/sovereign-trade-copilot) — Garment-trade inquiry analysis and reply drafting with Apertus, per-fact source spans and human approval checks.

### Auditing, action controls and adaptation

- [Apertus Lightpath](https://github.com/theBlackfish01/ApertusNetworkGym) — Fine-tuned Apertus 1.5 readers translate routing instructions into enforceable policies for an optical-network simulator, with disagreement review and recorded experiments. Synthetic instructions; no physical network controller was exercised.
- [Canis Apertus Lab](https://github.com/UrsushoribilisMusic/canis-hackapertus-track2b) — Local Apertus chat and document retrieval with an experimental hidden-state/logit disposition readout. Lexical fallback and mock mode are separate; the readout is not a calibrated correctness score.
- [Apertus Gate](https://github.com/ondmindmanagement-hub/apertus-gate) — Structured Apertus 1.5 risk review of proposed AI actions, producing allow, human-review or block decisions without executing actions.
- [Apertus Sovereign Operations Bridge](https://github.com/ambrosinistefan8-stack/apertus-sovereign-operations-bridge) — Apertus 1.5 fact extraction with deterministic conflict checks and human gates for proposed actions. Apache-2.0 notice; full licence text is linked, not bundled.
- [Bundesbrief](https://github.com/Powerworks-Global/bundesbrief) — Deterministic parliamentary-PDF extraction with optional local Apertus cross-checks, weighted review gates and a hash-chained ledger; default checks use a labelled stub.
- [FEDERAI](https://github.com/HesamSalehpour/federai-policy-assurance) — Apertus policy-document analysis with quotation matching, structured findings, hypothetical scenarios and human review; no expert-validated accuracy benchmark is published.
- [LoRaclette](https://github.com/bdravec/loraclette) — Experimental Apertus bottleneck-adapter training and position sweeps; tested only on a small random model, not real 8B weights or the 4-bit path.
- [rosetta-flow](https://github.com/anesask/rosetta-flow) — Two-tier Apertus audit of agent traces, with checked source-step quotations, adaptation/evaluation artifacts and human-readable findings.
- [SafeRouter ReplayLab](https://github.com/sumplus-real/saferouter-replaylab) — Local Apertus proposals for bounded retry/cancellation scenarios, checked against a synthetic reference protocol and exported as replayable counterexamples.
- [ScopeLock Verify](https://github.com/agent3-666/scopelock-verify) — Creative-brief review with local Apertus suggestions, source links, human approval and bounded media-file checks; repaired-protocol results are small and separate from earlier evaluations.
- [Sigillum](https://github.com/chessoren/sigillum) — Static AI-project audit with Apertus evidence interpretation, rule-assigned grades, source references and review reports; grades do not certify residency or compliance.
- [Systemic Resilience Copilot](https://github.com/rostys-fintech/systemic-resilience-copilot) — Apertus structuring/explanation for rule-based banking ICT recovery scenarios, with explicit missing-evidence states; not a validated incident predictor. Apache-2.0 notice.

## Community and contributing

- **Discuss models:** official Hugging Face discussions for [1.5 8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B/discussions) and [70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B/discussions).
- **Contact the team:** [contact page](https://apertus-ai.org/contact/), including showcase requests.
- **Meet the community:** [Discord](https://discord.gg/t9TY8FsJd), linked in the official ecosystem post; [Swiss AI events](https://www.swiss-ai.org/events) and [Swiss AI Weeks](https://ai-weeks.ch/).
- **Follow updates:** [Mastodon](https://fosstodon.org/@apertus), [LinkedIn](https://www.linkedin.com/company/apertus/), [X](https://x.com/apertusllm) and [Bluesky](https://bsky.app/profile/did:plc:ytwqtr3ykzq6nzr7kg2465ca).

Read [CONTRIBUTING.md](CONTRIBUTING.md), then suggest a resource with a primary source, short description and Apertus version. This list is [CC0 1.0](LICENSE); linked projects retain their own licenses. See the [helper documentation](https://github.com/rnckp/awesome-ai-switzerland/blob/main/src/README.md) for maintenance commands.
