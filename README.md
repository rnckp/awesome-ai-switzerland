# Awesome Apertus

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Suggestions welcome](https://img.shields.io/badge/suggestions-welcome-brightgreen)](https://github.com/rnckp/awesome-apertus/issues/new)
[![License: CC0](https://img.shields.io/badge/license-CC0-blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-apertus.svg)](https://github.com/rnckp/awesome-apertus)
[![Last commit](https://img.shields.io/github/last-commit/rnckp/awesome-apertus)](https://github.com/rnckp/awesome-apertus/commits/main/)

A curated guide to [Apertus](https://www.apertus-ai.org/), the open multilingual model family from the [Swiss AI Initiative](https://www.swiss-ai.org/), developed by EPFL, ETH Zurich, and CSCS. Official models, reproducibility resources, tools, integrations, and community projects.

**Last full ecosystem review: September 26, 2026; latest targeted Hack Apertus review: October 16, 2026.** Independent community list; “official” denotes Apertus team or Swiss AI resources. External-resource descriptions reflect their dated reviews, not continuous verification. See [research notes](RESEARCH.md) for scope and verification limits.

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
  <li><a href="#hack-apertus-projects">Hack Apertus projects</a></li>
  <li><a href="#community-and-contributing">Community and contributing</a></li>
</ul>

</details>

## Start here

- **Try chat:** [Public AI](https://publicai.co/) or the official [Apertus Mini WebGPU demo](https://huggingface.co/spaces/swiss-ai/apertus-mini-webgpu).
- **Download models:** [Swiss AI on Hugging Face](https://huggingface.co/swiss-ai) and the [model guide below](#official-models).
- **Run locally:** [Quickstart](https://apertus-ai.org/docs/quickstart/) and [local inference options](#local-inference-and-serving).
- **Build an application:** [Hosted APIs](#hosted-apis-and-cloud-deployment), [integration examples](#applications-and-integrations), and [fine-tuning recipes](https://github.com/swiss-ai/apertus-finetuning-recipes).
- **Study or reproduce:** [Technical report](https://arxiv.org/abs/2509.14233), [training code](https://github.com/swiss-ai/pretrain-code), and [data reconstruction](https://github.com/swiss-ai/pretrain-data).

## Official sites and documentation

- [Apertus website](https://www.apertus-ai.org/) — Project home.
- [About and roadmap](https://apertus-ai.org/pages/about/) — Mission, background, and planned development.
- [Swiss AI Initiative](https://www.swiss-ai.org/) — Parent initiative; [ETH AI Center](https://ai.ethz.ch/), [EPFL AI Center](https://ai.epfl.ch/), and [CSCS](https://www.cscs.ch/) are the institutional homes.
- [Documentation hub](https://apertus-ai.org/pages/documentation/) — Downloads, technical resources, and policy documents.
- [Technical overview](https://apertus-ai.org/docs/overview/) and [FAQ](https://apertus-ai.org/docs/faq/) — Orientation and common questions.
- [Provider directory](https://apertus-ai.org/pages/get-started/) and [community showcase](https://apertus-ai.org/pages/get-showcase/) — Officially listed services and applications.
- [GitHub organization](https://github.com/swiss-ai) — Authoritative code index; includes other Swiss AI research alongside Apertus.
- [Hugging Face organization](https://huggingface.co/swiss-ai) — Authoritative models, datasets, collections, and demos.
- [News](https://apertus-ai.org/news/) and [newsletter](https://apertus-ai.org/subscribe/) — Updates, including [Apertus 1.5](https://apertus-ai.org/articles/2026-07-apertus-1-5/) and the [September 2026 ecosystem review](https://apertus-ai.org/articles/2026-09-apertus-1-5-ga/).
- [Apertus Charter](https://apertus-ai.org/pages/charter/) — Published behavioral principles.
- [Legal documentation](https://github.com/swiss-ai/apertus-legal) — Versioned licenses, usage and privacy policies, EU public summaries, and codes of practice; companion [licensing](https://apertus-ai.org/docs/tech/licensing/) and [safety](https://apertus-ai.org/docs/tech/safety/) guides.
- [Website source](https://github.com/swiss-ai/www-apertus) — Contribute fixes to the website and documentation.

## Official models

Use each model card for capabilities, access conditions, and installation instructions. Base checkpoints are intended for completion or further training; Instruct checkpoints are adapted for conversation.

| Family                   | Official weights                                                                                                                                                                                         | Purpose                                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Apertus 1.5**          | [8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B) · [70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B) · [collection](https://huggingface.co/collections/swiss-ai/apertus-v15)                  | Text and image input, experimental audio input, optional thinking; up to 262,144 tokens. Text output. |
| **1.1 Mini — base**      | [0.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B) · [1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B) · [4B](https://huggingface.co/swiss-ai/Apertus-v1.1-4B)                            | Smaller distilled text models.                                                                        |
| **1.1 Mini — Instruct**  | [0.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B-Instruct) · [1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B-Instruct) · [4B](https://huggingface.co/swiss-ai/Apertus-v1.1-4B-Instruct) | Compact conversational models.                                                                        |
| **1.1 Mini — quantized** | [Collection](https://huggingface.co/collections/swiss-ai/apertus-mini) · [vLLM NVFP4A16 1.5B](https://huggingface.co/swiss-ai/Apertus-v1.1-1.5B-Instruct-vLLM-NVFP4A16)                                  | Official MLX INT3/INT4/INT6 variants at all three sizes, plus the vLLM build.                         |
| **1.0 — base**           | [8B](https://huggingface.co/swiss-ai/Apertus-8B-2509) · [70B](https://huggingface.co/swiss-ai/Apertus-70B-2509)                                                                                          | Original September 2025 text checkpoints.                                                             |
| **1.0 — Instruct**       | [8B](https://huggingface.co/swiss-ai/Apertus-8B-Instruct-2509) · [70B](https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509) · [collection](https://huggingface.co/collections/swiss-ai/apertus-v1) | Original chat models; 65,536-token context.                                                           |

Supporting models: [pretraining toxicity classifier](https://huggingface.co/swiss-ai/apertus-pretrain-toxicity) and [WavTokenizer checkpoint](https://huggingface.co/swiss-ai/wavtokenizer-large-unify-40token).

**Version matters:** at the full ecosystem review, the 1.5 cards required acceptance of access conditions and documented custom Transformers/vLLM builds. They also stated that tool calling was unsupported in thinking mode. Follow the authored [1.5 usage instructions](https://huggingface.co/swiss-ai/Apertus-v1.5-8B#how-to-use); a runtime supporting 1.0 does not automatically support 1.5.

## Official code and training infrastructure

### Training and data preparation

- [pretrain-code](https://github.com/swiss-ai/pretrain-code) and [Megatron-LM](https://github.com/swiss-ai/Megatron-LM) — Apertus pretraining entry point and underlying distributed training fork.
- [pretrain-data](https://github.com/swiss-ai/pretrain-data) — Reconstruct the pretraining corpus from its sources.
- [posttraining](https://github.com/swiss-ai/posttraining) — Supervised fine-tuning and alignment experiments.
- [posttraining-data](https://github.com/swiss-ai/posttraining-data) — Download, standardize, filter, decontaminate, and mix post-training data.
- [apertus-finetuning-recipes](https://github.com/swiss-ai/apertus-finetuning-recipes) — Full-parameter and LoRA recipes using Transformers, TRL, and Accelerate; [walkthrough](https://apertus-ai.org/docs/tech/fine-tuning/) targets the original 8B/70B models.
- [multimodal-data](https://github.com/swiss-ai/multimodal-data) — Apertus 1.5 image/audio preparation, including a [dataset inventory](https://github.com/swiss-ai/multimodal-data/blob/main/datasets/DATASETS.md).
- [robots-txt-compliance](https://github.com/swiss-ai/robots-txt-compliance) — Web-data filtering and URL-checking tooling; [research site](https://data-compliance.github.io/).
- [llm-pretrain-data-toxicity-removal](https://github.com/swiss-ai/llm-pretrain-data-toxicity-removal) — Pretraining toxicity filtering.
- [pretraining-safety-annotation](https://github.com/swiss-ai/pretraining-safety-annotation) — Charter-guided data annotation pipeline.
- [audio-preprocessing](https://github.com/swiss-ai/audio-preprocessing) and [data-PDF-pipeline](https://github.com/swiss-ai/data-PDF-pipeline) — Speech processing and PDF corpus extraction tools.
- [Swiss-AI-Romansh-Scripts](https://github.com/swiss-ai/Swiss-AI-Romansh-Scripts) — Romansh corpus preparation for Apertus v1.
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

- [Data transparency archive](https://github.com/swiss-ai/apertus-data-transparency) — Versioned dataset and release documentation.
- **Web filtering:** [FineWeb tags](https://huggingface.co/datasets/swiss-ai/fineweb-compliant-tag), [FineWeb-2 tags](https://huggingface.co/datasets/swiss-ai/fineweb-2-compliant-tag), and [FineWeb-Edu tags](https://huggingface.co/datasets/swiss-ai/fineweb-edu-compliant-tag).
- **Robots.txt artifacts:** [English blocked domains](https://huggingface.co/datasets/swiss-ai/robots-txt-blocked-domains-english), [multilingual blocked domains](https://huggingface.co/datasets/swiss-ai/robots-txt-blocked-domains-multilingual), and [compressed files](https://huggingface.co/datasets/swiss-ai/fineweb-robots-txt-files-compressed).
- **Swiss language corpora:** [Swiss pretraining](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-swiss), [Romansh pretraining](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-romansh), and [Romansh post-training](https://huggingface.co/datasets/swiss-ai/apertus-posttrain-romansh).
- **Text pretraining research:** [processed Project Gutenberg](https://huggingface.co/datasets/swiss-ai/project_gutenberg_preprocessed) and [poison/canary data](https://huggingface.co/datasets/swiss-ai/apertus-pretrain-poisonandcanaries).
- **Post-training:** [SFT mixture](https://huggingface.co/datasets/swiss-ai/apertus-sft-mixture), [Africa SFT](https://huggingface.co/datasets/swiss-ai/africa-sft), [Africa preferences](https://huggingface.co/datasets/swiss-ai/africa-preferences), and [1.5 preference data](https://huggingface.co/datasets/swiss-ai/Apertus_v1.5_Preference_Data).
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
- [Apertus Mini: distillation and quantization](https://arxiv.org/abs/2605.29128) — Smaller-model family and compression methods.
- [Training Apertus on Alps](https://arxiv.org/abs/2604.12973) — HPC engineering and distributed-training lessons.
- [Web crawling opt-outs](https://arxiv.org/abs/2504.06219) — Measuring the effect of respecting data-source exclusions.
- [Positional fragility and memorization](https://arxiv.org/abs/2505.13171) — Memorization analysis; [Apertus reproduction code](https://github.com/swiss-ai/apertus-memorization).
- [xIELU activation](https://arxiv.org/abs/2411.13010) and [AdEMAMix optimizer](https://arxiv.org/abs/2409.03137) — Core architectural and optimization ingredients.
- [INCLUDE](https://arxiv.org/abs/2411.19799) and [Global MMLU](https://arxiv.org/abs/2412.03304) — Multilingual evaluation references.
- [Parity-aware BPE](https://arxiv.org/abs/2508.04796) — Cross-language tokenization research; [code](https://github.com/swiss-ai/parity-aware-bpe).
- [Research library](https://apertus-ai.org/pages/research/) and [Zotero group](https://www.zotero.org/groups/6385576/apertus) — Papers and supporting literature on data, optimization, safety, and serving. The page still lists the 1.5 technical report as forthcoming at the research date.

### Research projects

- [apertus-probes](https://github.com/swiss-ai/apertus-probes) — Hallucination probes and activation analysis.
- [apertus-translate](https://github.com/swiss-ai/apertus-translate) — Translation experiments and human-evaluation annotations.
- [vocab-reduction](https://github.com/swiss-ai/vocab-reduction) — Vocabulary-size optimization for training and inference.
- [prune-apertus-lm-head](https://github.com/swiss-ai/prune-apertus-lm-head) — 1.5 output-head conversion while retaining multimodal input token IDs.
- [Apertus RAG evaluation](https://github.com/swiss-ai/ml4science-apertus-rag-evaluation) — Research comparing retrieval, chunking, and reranking strategies.
- [apertus-speculative-decoding](https://github.com/swiss-ai/apertus-speculative-decoding) — Reproducible 1.5 serving-performance study.
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

| Tool                     | Apertus resource                                                                                                                                                                                | Notes                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Transformers             | [Official guide](https://apertus-ai.org/docs/guides/transformers/) · [upstream model docs](https://huggingface.co/docs/transformers/model_doc/apertus) · [Swiss AI fork](https://github.com/swiss-ai/transformers)                                          | Python model loading; use the 1.5 card's pinned fork for multimodal support.                                        |
| vLLM                     | [Official guide](https://apertus-ai.org/docs/guides/vllm/) · [1.5 model card](https://huggingface.co/swiss-ai/Apertus-v1.5-70B#how-to-use) · [Swiss AI fork](https://github.com/swiss-ai/vllm) · [integration work](https://github.com/swiss-ai/vllm-apertus-integration)                                                      | GPU serving; use model-card-pinned revisions, parsers, and containers.                                                               |
| SGLang                   | [Official guide](https://apertus-ai.org/docs/guides/sglang/) · [Swiss AI fork](https://github.com/swiss-ai/sglang) · [sglang-apertus](https://github.com/swiss-ai/sglang-apertus) · [Scratchpad](https://github.com/swiss-ai/Scratchpad)                                                                                                                                    | Original-model examples; 1.5 integration is work in progress.                                                       |
| llama.cpp                | [Upstream](https://github.com/ggml-org/llama.cpp) · [experimental 1.5 branch](https://github.com/MichelRosselli/llama.cpp/tree/model/apertus-v1.5)                                              | Follow the [maintainer's discussion](https://huggingface.co/swiss-ai/Apertus-v1.5-8B/discussions/6) for 1.5 status. |
| Ollama                   | [Official guide](https://apertus-ai.org/docs/user/ollama/) · [v1 community package](https://ollama.com/MichelRosselli/apertus) · [Mini package](https://ollama.com/MichelRosselli/apertus-v1.1) | Community-maintained model packages.                                                                                |
| LM Studio                | [Official guide](https://apertus-ai.org/docs/user/lmstudio/)                                                                                                                                    | Desktop UI for compatible local model builds.                                                                       |
| Llamafile                | [Official guide](https://apertus-ai.org/docs/user/llamafile/)                                                                                                                                   | Package compatible GGUF models as executables.                                                                      |
| Open WebUI               | [Official guide](https://apertus-ai.org/docs/user/openwebui/)                                                                                                                                   | Chat frontend for local or hosted inference.                                                                        |
| MLX                      | [Official Mini collection](https://huggingface.co/collections/swiss-ai/apertus-mini) · [mlx-community 8B BF16](https://huggingface.co/mlx-community/Apertus-8B-Instruct-2509-bf16) · [community 1.5 70B requirements](https://huggingface.co/sbaechler/Apertus-v1.5-70B-FP8-mlx#requirements) | Apple Silicon builds; the multimodal 1.5 70B conversions require a pinned experimental mlx-vlm branch, not released mlx-vlm or mlx-lm. |
| Transformers.js / WebGPU | [Mini demo and source files](https://huggingface.co/spaces/swiss-ai/apertus-mini-webgpu)                                                                                                        | Browser-local inference using converted Mini weights.                                                               |

## Community quantizations and derivatives

### Alternative formats

**Apertus 1.0 Instruct GGUF conversions:**

| Maintainer | 8B | 70B | Notes |
| ---------- | -- | --- | ----- |
| Unsloth | [GGUF](https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF) | [GGUF](https://huggingface.co/unsloth/Apertus-70B-Instruct-2509-GGUF) | Also offers [8B bitsandbytes 4-bit](https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-unsloth-bnb-4bit). |
| Bartowski | [GGUF](https://huggingface.co/bartowski/swiss-ai_Apertus-8B-Instruct-2509-GGUF) | [GGUF](https://huggingface.co/bartowski/swiss-ai_Apertus-70B-Instruct-2509-GGUF) | Alternative quantizations. |
| redponike | [GGUF](https://huggingface.co/redponike/Apertus-8B-Instruct-2509-GGUF) | [GGUF](https://huggingface.co/redponike/Apertus-70B-Instruct-2509-GGUF) | Linked by the official Ollama guide. |

- **Red Hat AI FP8:** [8B Instruct](https://huggingface.co/RedHatAI/Apertus-8B-Instruct-2509-FP8-dynamic) — Dynamic FP8 conversion for compatible GPU serving.
- **OnPrem AI 1.5:** [8B FP8](https://huggingface.co/onprem-ai/Apertus-v1.5-8B-FP8), [70B FP8](https://huggingface.co/onprem-ai/Apertus-v1.5-70B-FP8), and [70B NVFP4](https://huggingface.co/onprem-ai/Apertus-v1.5-70B-NVFP4) — Quantized checkpoints with a [temporary vLLM build](https://github.com/onprem-ai/vllm-apertus-1p5).
- [Andreas Martin's Apertus 1.5 8B text-only conversion](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text) — Text backbone repackaged for standard Transformers (4.56+), without a custom fork or remote code; omits image/audio input and requires accepting the model's access conditions.
- **1.5 text-only GGUF:** [Andreas Martin Q8_0](https://huggingface.co/andreasmartin/apertus-v1.5-8b-text-Q8_0-GGUF) and [Colby Q4_K_M](https://huggingface.co/Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF) — 8B conversions that omit multimodal capabilities.
- **1.5 text-only MLX:** [m1rkocasu 4-bit DWQ](https://huggingface.co/m1rkocasu/Apertus-v1.5-8B-text-MLX-4bit-DWQ) — Community Apple Silicon conversion.
- **Simon Bächler's 1.5 70B MLX:** [6-bit](https://huggingface.co/sbaechler/Apertus-v1.5-70B-FP6-mlx) and [8-bit](https://huggingface.co/sbaechler/Apertus-v1.5-70B-FP8-mlx) — Community Apple Silicon quantizations retaining image/audio input and text output; author reports testing on an M5 Max with 128 GB unified memory. Gated downloads; follow the cards' pinned experimental mlx-vlm setup.
- **Mini ONNX:** [0.5B](https://huggingface.co/onnx-community/Apertus-v1.1-0.5B-Instruct-QAD-INT4-ONNX), [1.5B](https://huggingface.co/onnx-community/Apertus-v1.1-1.5B-Instruct-QAD-INT4-ONNX), and [4B](https://huggingface.co/onnx-community/Apertus-v1.1-4B-Instruct-QAD-INT4-ONNX) — INT4 browser/runtime conversions.

### Fine-tunes and adaptations

- [Apertus SEA-LION v4 8B](https://huggingface.co/aisingapore/Apertus-SEA-LION-v4-8B-IT) — AI Singapore's Southeast Asian language adaptation; [GGUF](https://huggingface.co/aisingapore/Apertus-SEA-LION-v4-8B-IT-GGUF) and [release collection](https://huggingface.co/collections/aisingapore/sea-lion-v4).
- [Apertus EstLLM](https://huggingface.co/tartuNLP/Apertus-EstLLM-8B-Instruct-0326) — TartuNLP's Estonian adaptation; [base checkpoint](https://huggingface.co/tartuNLP/Apertus-EstLLM-8B-1125) and [paper](https://arxiv.org/abs/2603.02041).
- **Apertus MeditronFO:** [8B](https://huggingface.co/EPFLiGHT/Apertus-8B-MeditronFO) and [70B](https://huggingface.co/EPFLiGHT/Apertus-70B-MeditronFO) — Medical-domain research models; [training pipeline](https://github.com/EPFLiGHT/FullyOpenMeditron) and [paper](https://arxiv.org/abs/2605.16215).
- [Greek Apertus](https://github.com/eellak/greek-apertus) — Ongoing Greek continued-pretraining and tokenizer project using GlossAPI data; tooling, not a finished model release.
- [Andreas Martin's Apertus collection](https://huggingface.co/collections/andreasmartin/apertus) — Experimental and educational adaptations, including Apertus 1.1 Mini and 1.5 embedding conversions, text-only formats, and a biomedical fine-tune.

### Community fine-tuning tutorials

- [Hack Apertus SFT notebook](https://www.kaggle.com/code/andreasmartinch/sft-apertus-v1-5-8b-hack-apertus-template) — Andreas Martin's Jupyter template for fine-tuning Apertus 1.5 8B, designed for FHNW Business students contributing to Hack Apertus; author reports testing on Kaggle and CSCS JupyterLab (Clariden).

## Hosted APIs and cloud deployment

### Providers and managed deployment

Entries were found through the official [directory](https://apertus-ai.org/pages/get-started/), [September 2026 ecosystem review](https://apertus-ai.org/articles/2026-09-apertus-1-5-ga/), and providers' own catalogs. Check providers for available versions, modalities, context limits, and pricing.

| Provider                         | Resource                                                                                                                                                                                                                        | Access                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Swisscom                         | [Apertus 1.5 70B docs](https://docs.cloud.swisscom.ch/guide/cloud-services/aip/models/apertus-1_5_70B)                                                                                                                          | Swiss AI Platform API.                           |
| Infomaniak                       | [AI Services catalog](https://www.infomaniak.com/en/hosting/ai-services/open-source-models)                                                                                                                                     | Swiss-hosted inference API.                      |
| PHOENIQS / KVANT                 | [Active models](https://documentation.kvant.cloud/maas/active-models/)                                                                                                                                                          | Enterprise model service.                        |
| Safe Swiss Cloud                 | [Private AI](https://safeswisscloud.com/en/private-ai/)                                                                                                                                                                         | Managed private AI offering.                     |
| stepping stone                   | [AI on demand](https://www.stepping-stone.ch/en/products/artificial-intelligence/ai-on-demand-powered-by-swiss-ai-initiative) · [deployment notes](https://wiki.stoney-cloud.com/wiki/AI_on_demand:_apertus-ai/Apertus-v1.5-8B) | Managed 8B service.                              |
| Public AI                        | [Developer platform](https://platform.publicai.co/) · [API reference](https://platform.publicai.co/api) · [Hugging Face integration](https://huggingface.co/docs/inference-providers/providers/publicai)                                                                                                                         | Chat and API access.                             |
| Featherless                      | [Apertus catalog](https://featherless.ai/models?families=apertus) · [deployment guide](https://apertus-ai.org/docs/deploy/featherless/)                                                                                         | Serverless inference.                            |
| Regolo                           | [Model catalog](https://regolo.ai/models/)                                                                                                                                                                                      | Additional provider listing `apertus-70b`.       |
| OnPrem AI                        | [Model catalog](https://www.onprem.ai/en/ai-llm-models/)                                                                                                                                                                        | Local enterprise deployment and support.         |

### Deploy on your own cloud infrastructure

- [Exoscale](https://apertus-ai.org/docs/deploy/exoscale/) — Official guide and [dedicated inference offering](https://www.exoscale.com/ai-cloud-infrastructure/dedicated-inference/).
- [AWS SageMaker AI](https://apertus-ai.org/docs/deploy/sagemaker/) — Official guide; [AWS walkthrough](https://aws.amazon.com/blogs/alps/switzerlands-open-source-apertus-llms-now-available-on-amazon-sagemaker-ai/).
- [Microsoft Azure](https://apertus-ai.org/docs/deploy/azure/) — Official guide; [Azure Samples quickstart](https://github.com/Azure-Samples/swiss-llm-quickstart).
- [Google Vertex AI](https://apertus-ai.org/docs/deploy/vertex/) — Official cloud deployment guide.
- [Community SageMaker Terraform](https://github.com/hueper/apertus-70b-infra) — Original 70B Instruct deployment with scheduled endpoint lifecycle management.

## Applications and integrations

### Chat, translation, and data tools

- [Public AI chat](https://publicai.co/) — Hosted Apertus chat interface.
- [Lumo by Proton](https://proton.me/blog/lumo-apertus-partnership) — Apertus integration in Proton's assistant.
- [Euria](https://www.infomaniak.com/en/euria) — Infomaniak assistant with Apertus selection; [setup and kSuite integration](https://www.infomaniak.com/en/support/faq/2924/discover-euria-and-the-apertus-model).
- [Helvetra](https://helvetra.ch/) — Swiss-language translation application; [backend source](https://github.com/Helvetra/backend).
- [AI Potluck](https://www.aipotluck.org/chat) — Chat interface exposing aspects of the inference process.
- [Open Data Editor](https://opendataeditor.okfn.org/) — Tabular-data tool with an Apertus Mini component; [source](https://github.com/okfn/opendataeditor).
- [ZüriCityGPT OSS](https://oss.zuericitygpt.ch/) — Liip's municipal-law RAG demonstration.

### SDKs, automation, and application examples

- [LiteLLM PublicAI provider](https://docs.litellm.ai/docs/providers/publicai) — Documented Apertus routes for the Python SDK and proxy.
- [Laravel Apertus](https://github.com/mmorand/laravel-apertus) — Community PHP/Laravel client with streaming and model listing.
- [ApertusSharp](https://github.com/bhrnjica/ApertusSharp) — Community .NET client built on Microsoft.Extensions.AI, with Semantic Kernel integration.
- [Apertus n8n starter kit](https://github.com/aai-institute/apertus-n8n) — Python/curl examples, structured extraction, three workflows, and a local Ollama path.
- [Apertus AI workshop](https://github.com/blancsw/apertus-ai-workshop) — Infomaniak-backed RAG combining Apertus generation with separate embedding and reranking models.
- [Emilie](https://github.com/veronica-builds/emilie) — Community legal-document assistant with Apertus support and MCP-based case-law lookup.
- [CertusAI](https://github.com/saurluca/CertusAI) — Swiss AI Weeks legal-assistant project using Apertus.

## Hack Apertus projects

Selected community projects from [Hack Apertus](https://hackapertus.ch/), reviewed on **October 9, 13 and 16, 2026**, covering the online hackathon and emerging on-site projects. These are experimental prototypes and research tools, not official Apertus releases. Selection requires an explicit code licence, project-specific documentation, a concrete Apertus use, and substantive implementation. See the [closing-day review](RESEARCH.md#hack-apertus-closing-day-discovery--october-16-2026) and earlier notes for decisions and limitations; software and reported results were not independently tested.

Online submissions closed on **October 16, 2026 at 12:00 CEST**. No named winners were found in the checked public organizer sources that evening. The [official schedule](https://hackapertus.ch/online-hack) puts the jury decision by **October 23**; [Devpost rules](https://hackapertus.devpost.com/rules) estimate the announcement at **12:00 CEST on October 23, 2026**, subject to change. Directory inclusion does not establish submission acceptance or an award.

### Red-teaming and evaluation

- [SwissCivicQA-4L](https://github.com/Jann08/swisscivicqa/tree/main/track_1b) — Swiss constitutional factuality benchmark in German, French, Italian and Romansh, with source-backed answers, recorded Apertus 1.5 8B responses and cross-language consistency scoring. Apache-2.0 code.
- [Inkraft](https://github.com/NWichter/Hack_Apertus_1B_Inkraft) — Trilingual Swiss social/health-insurance law benchmark with dated Fedlex evidence, earlier-law answer pairs and Apertus evaluation tooling. Apache-2.0 code; dataset CDLA-Permissive-2.0.
- [Swiss Newcomer QA](https://github.com/MidsummerYU/large-canele-model-1b) — Four-language factuality evaluation of Apertus 1.5 8B/70B on Swiss administrative procedures, with ch.ch sources, recorded answers and replay scoring. Apache-2.0.
- [Swiss Reality Check](https://github.com/bhuwanb23/apertus) — Swiss knowledge, values and Alemannic-dialect evaluation with source-backed items and Apertus 1.5 8B artifacts; no 70B comparison is published. Apache-2.0.
- [leGML domain transfer](https://github.com/legml-ai/apertus-domain-transfer) — Swiss private-insurance law adaptation of original Apertus 8B, with published weights, German/French evaluation data and a web-search evaluation harness. Apache-2.0 code; legal accuracy is not independently validated.
- [Spoken-request refusal study](https://github.com/nourseen6/hack-apertus-redteam) — Compares text and synthetic-speech safety responses from Apertus 1.5 8B/70B, with collection, judging and audit tooling; harmful raw answers are withheld. Apache-2.0.
- [Scrutineer](https://github.com/winsznx/scrutineer/tree/main/track_1b) — Multilingual Swiss federal-vote outcome benchmark with recorded Apertus responses, reproducible scoring and explicit reporting of a failed initial hypothesis. Apache-2.0.
- [EpiTrace](https://github.com/wanshuzhang-story/epitrace-apertus) — Tests whether Apertus treats repeated claims as independent evidence, with synthetic dossiers, recorded 8B/70B responses and offline scoring. Apache-2.0.
- [Swiss HVET Eval](https://github.com/wortgefecht/apertus-swiss-hvet-eval) — Swiss vocational-education factuality benchmark for Apertus 1.5 8B, with cited reference answers and human validation alongside automated judging. Apache-2.0.
- [Swiss Heritage Factuality](https://github.com/ChristoYusj/apertus-swiss-landmarks) — Four-language Swiss landmark benchmark with photo, text-only and trap questions, recorded responses and deterministic regrading. Apache-2.0.
- [Apertus-Recht](https://github.com/mi11ione/apertus-recht) — German, French and Italian minimal-pair evaluation of Art. 261bis StGB, with code-computed labels, recorded Apertus responses and a reusable scoring harness. Apache-2.0.
- [Swiss Statute QA](https://github.com/bisale24-ops/swiss-statute-qa) — Multilingual Swiss federal-law evaluation dataset with cited statutory answers, historical statute versions and recorded Apertus 1.5 responses. Apache-2.0 code; dataset CDLA-Permissive-2.0.
- [Apertus StressLab](https://github.com/Alextsvr/apertus-stresslab) — False-premise acceptance experiments on Apertus 1.5 with preregistered evaluation, raw responses and provenance checks; small synthetic studies with quantization caveats. Apache-2.0.
- [AirPatch](https://github.com/AhaWissenschaft/airpatch) — Evaluates Apertus code proposals in offline containers against hidden programming tests, with recorded responses, replay tooling and negative results. Apache-2.0.
- [Vipunen](https://github.com/apn201/Vipunen-2B) — Apertus-driven red-teaming pipeline exploring Finnish poetic framing, with neutral public seeds and an operator console; original attack payloads are withheld. Apache-2.0.
- [K-Probe](https://github.com/iamhuman-cheolheelee/k-probe) — Korean factuality, cultural and safety probes with source-backed cases, regex scoring, recorded Apertus 1.0/1.5 responses and a results dashboard. MIT.
- [Apertus Red-Team Harness](https://github.com/devilking7x/apertus-redteam) — Seeded multilingual, prompt-injection and tool-use probes with response logs and heuristic scoring for human review. Apache-2.0.

### Document understanding and grounded answers

- [Concordance](https://github.com/Ali-Aoun5/concordance-hackapertus) — Trilingual Swiss-law divergence review combining rules, an Apertus 8B/70B cascade, source-quotation checks and recorded-response replay. Apache-2.0; findings require legal review.
- [Alpenrecht AI](https://github.com/Anakalypto/AlpenRecht) — Apertus legal Q&A retrieving federal, cantonal and communal sources with citation checks; the author's evaluation reports substantial factual errors. Apache-2.0.
- [ParliParla](https://github.com/Avonik/ParliParla) — Apertus 1.5 8B extraction of parliamentary affairs into a common schema, with quote/span provenance and cross-parliament evaluation artifacts. Apache-2.0.
- [William](https://github.com/ChristoYusj/William) — Parliamentary-PDF extraction using Apertus 1.5 70B, source-page evidence, a Firefox extension, batch interface and API. Apache-2.0.
- [RöstiBridge](https://github.com/ChristoYusj/RoestiBridge) — Firefox extension highlighting possible cross-language differences with Apertus explanations and SwissGov-RSD evaluation/replay tooling. Apache-2.0.
- [Apertus Difference Ranker](https://github.com/ChenfWen/Apertus-Difference-Ranker/tree/main/track_2a) — Token-level semantic-difference ranking using frozen Apertus representations, DiffAlign and lightweight supervised models; default execution replays results. Apache-2.0.
- [Reading semantic differences from Apertus](https://github.com/amunozo/apertus-swissgov-rsd) — SwissGov-RSD experiments using Apertus 1.5 8B hidden states, fitted prediction heads, token heatmaps and CPU replay of saved features. Apache-2.0.
- [CLAUSESHIFT](https://github.com/guelmbaye/clauseshift) — Cross-language semantic-difference scoring combining a multilingual encoder, bounded Apertus judgments and conservative fallback, with retained execution artifacts. Apache-2.0; no independent final quality estimate is established.
- [GeaNaVid](https://github.com/NWichter/Hack_Apertus_2A_GeaNaVid) — Apertus 1.5 voting-booklet claim classification with vote-scoped retrieval, cross-language translation, sentence/page evidence and recorded evaluation runs. Apache-2.0.
- [Büchli](https://github.com/kaiser-data/hack-apertus-booklet-nli) — Multilingual voting-booklet claim checking with hybrid retrieval, Apertus decisions, page citations and visual evidence review. Apache-2.0.
- [booklet-check](https://github.com/StuartYo/hack-apertus) — Swiss voting-booklet NLI with local lexical/embedding retrieval, Apertus classification and evidence restored from PDF text. Apache-2.0.
- [yasuhito's voting-booklet NLI](https://github.com/yasuhito/hackapertus-ost) — Apertus 1.5 pipeline using retrieved source spans, native tool-call output and verbatim evidence restoration. Apache-2.0.
- [Guichet](https://github.com/MidsummerYU/large-canele-model-2b) — Apertus 1.5 8B answers about Swiss administrative procedures, grounded in ch.ch passages with per-sentence quotation checks and abstention. Apache-2.0.
- [Skony](https://github.com/ahmarkhhan/sfedly) — Parliamentary-document extraction with an Apertus client, source-linked field proposals and a human-reviewed export workflow. Apache-2.0; evaluation coverage is limited.
- [Docket](https://github.com/owldevltd/docket-apertus) — Apertus extraction of parliamentary PDFs and scans into source-linked affair records, with field review and correction tooling. Apache-2.0.
- [Trace](https://github.com/owldevltd/trace-apertus) — Form-image geometry plus Apertus interpretation of fields and spoken answers, with source-linked values and human review; signature integration is mocked. Apache-2.0.
- [SEVERIN](https://github.com/vero-code/severin) — Parliamentary-affair extraction using Apertus, typed schemas, PDF-page quotation checks and an interactive source/extraction viewer. Apache-2.0.
- [ParlPDFeCH](https://github.com/jkovatsch/ParlPDFeCH) — Parliamentary PDFs to eCH-0295/RDF using rules and published heads over Apertus 1.5 8B hidden states; model-assisted extraction needs its specialized backend. Apache-2.0 code; heads CC-BY-4.0.
- [Passerelle](https://github.com/Thanatos9404/passerelle) — Apertus explanations of Swiss official letters with extracted fact cards, back-translation checks and caseworker review indicators. Apache-2.0; language checks do not guarantee faithful translation.
- [BriefKlar](https://github.com/kiky97/briefklar) — Swiss administrative-letter explanations with Apertus, source-grounded extraction, calendar output and low-resource-language experiments. Apache-2.0.
- [Klarbrief](https://github.com/JannetEkka/klarbrief) — Apertus explanations of Swiss letters with quotation/date/amount checks, separately flagged unsupported points and recorded evaluation responses. Apache-2.0.
- [QuietLetter](https://github.com/jacman1988-super/quietletter) — Local Apertus selection of requests and unclear passages from plain-text letters, with exact quotes and a separate literal-date scanner. Apache-2.0; it does not calculate legal deadlines.
- [Redacta](https://github.com/kangraemin/redacta-apertus/tree/main/track_2b) — Swiss court-decision redaction proposals using rules and Apertus, with clerk review and synthetic-name evaluation. Apache-2.0; missed identities remain possible.
- [Clausus](https://github.com/jou2512/clausus) — Confidential-content masking for text, slides and Swiss German audio, with an Apertus detection layer, reversible placeholders and request receipts. Apache-2.0; evaluation reports residual leaks.
- [Treuhand Shield](https://github.com/ctmakc/treuhand-shield) — Swiss fiduciary-document proxy combining identifier rules, Apertus entity detection, reversible placeholders and audit records. Apache-2.0; entity detection is probabilistic.
- [LaporSiap](https://github.com/fadillaoegi/laporsiap-hacketon) — Apertus-assisted scam-report preparation for Indonesia, with source-linked chronologies, mandatory review and export; it does not file reports. Apache-2.0.
- [Belegt](https://github.com/chessoren/Belegt) — Local Apertus Q&A over the Swiss Federal Constitution with retrieval, exact-quotation checks, abstention and recorded evaluation runs. Apache-2.0 notice.
- [ClearConsent](https://github.com/sese0318/clearconsent) — Apertus research consent-form explanations with source-quotation and number checks, missing-information questions and teach-back quizzes. Apache-2.0.
- [Leicht·Facile](https://github.com/bobrovsky420/leicht-facile) — Easy-language drafting for Swiss official texts with Apertus, sentence provenance, deterministic fact checks and human review. Apache-2.0.
- [Papertus](https://github.com/igorjovicic/papertus) — Swiss document assistant combining Apertus extraction with QR decoding, checksum and arithmetic checks, cited reports and document Q&A. Apache-2.0.
- [Querschnitt](https://github.com/mi11ione/querschnitt) — Apertus topic classification for OpenParlData affairs using configurable taxonomies, review lanes and quoted evidence; targets the October 18–19, 2026 Liebefeld hackathon. Apache-2.0.
- [Gegenprobe](https://github.com/mi11ione/gegenprobe) — Swiss parliamentary-data census, repair plans and schema conversion, with optional Apertus review of difficult layouts and replayable evaluation artifacts. Apache-2.0.
- [Gleichlaut](https://github.com/mi11ione/gleichlaut) — Audits multilingual drug-reimbursement conditions and uses Apertus to draft French/Italian amendments while deterministic code preserves numeric values; drafts require review. Apache-2.0.
- [Riserbo](https://github.com/AliceMessi/riserbo) — Reversible Swiss/Italian personal-data redaction with rules and local Apertus 1.5 detection, including indirect identifiers; synthetic evaluation reports residual leaks. Apache-2.0.
- [kanhe](https://github.com/hoongyu/kanhe) — Multilingual voting-booklet claim classification with Apertus 1.5, BM25 retrieval, checked quotations and cached evaluation responses. Apache-2.0.
- [PolyJudge](https://github.com/hasanssr/polyjudge-swissgov-rsd/tree/main/track_2a) — Cross-language semantic-difference detection in Swiss government pages, combining sentence alignment with Apertus verification and offline replay. Apache-2.0.
- [Tse-min](https://github.com/YinZhengxun/hack-apertus-tsemin/tree/main/track_2a) — Word-level semantic-difference scoring combining Apertus judgments and token surprisal; requires an endpoint supporting prompt log probabilities. Apache-2.0.
- [CiteOps](https://github.com/sidsri14/citeops) — Apertus incident-brief generation from bounded, redacted log bundles, with checks rejecting invented event IDs and uncited hypotheses or actions. Apache-2.0.
- [Fedlex Answer](https://github.com/bisale24-ops/fedlex-answer) — Swiss federal-law Q&A using local statutory retrieval, Apertus 1.5 generation and deterministic quotation/number checks in German, French and Italian. Apache-2.0.
- [Apertus Evidence Lab](https://github.com/hallzyx/apertus) — Multilingual voting-booklet claim classification with hybrid retrieval and a trained decision head over frozen Apertus 1.5; requires its specialized model backend. Apache-2.0.
- [Schild](https://github.com/ShenJun93/hack-apertus-schild/tree/main/track_2b) — Swiss personal-data redaction gateway combining deterministic identifier rules with Apertus 1.5 entity detection and reversible placeholders. Apache-2.0.
- [Apertus Court Decisions](https://github.com/beyondExp/apertus-court-decisions) — Frozen Apertus 1.5 8B reader with a published classification head for Swiss court rulings; default execution checks the head and replays saved predictions. Apache-2.0.
- [Folio](https://github.com/ksmostofa/folio) — Source-document checklist workbench with Apertus extraction, exact quotation/page checks, preserved conditional wording and human review. Apache-2.0.
- [SplitAlign](https://github.com/sharonbasovich/splitalign) — Token-level semantic-difference detection between English and German, French or Italian Swiss government documents using hosted Apertus. Apache-2.0.
- [SpanDiff](https://github.com/moscraciunxxx/SpanDiff-HackApertus) — Cross-language semantic-drift scoring using Apertus 1.5 8B hidden states, with development predictions and layer ablations; generates no text. Apache-2.0.
- [ClaimLens](https://github.com/Xa4-wi/HackApertus) — Checks claims against Swiss voting booklets with Apertus 1.5, returning source-relative labels, quotations and PDF pages in German, French and Italian. Apache-2.0.
- [Apertus QA](https://github.com/ventolabs-hq/apertus-qa) — Spanish Q&A over local snapshots of Argentine official statistics; Apertus plans and phrases answers while code supplies the numeric values. Apache-2.0.
- [Apertus Evidence Ledger](https://github.com/sgagestudio/apertus-evidence-ledger) — SQLite-based document retrieval with Apertus synthesis, exact-quote citation checks and a hash-based evidence ledger. Apache-2.0.
- [Velum](https://github.com/calderbuild/velum) — Swiss court-decision anonymisation combining Apertus entity detection with court-specific rule packs, deterministic edits and a human review interface. Apache-2.0.
- [Klartext](https://github.com/LeFlegm/Klartext/tree/main/track_2b) — Swiss official-letter triage with source-span checks, deadline extraction and an Apertus 8B-to-70B cascade; evaluated on synthetic letters. Apache-2.0.
- [ClearDesk](https://github.com/m7mdd77/cleardesk-apertus) — Local Apertus 1.5 CLI selecting a verified verbatim passage from four synthetic IT procedures, with abstention for unsupported questions. Apache-2.0.

### Applications, workflow controls and adaptation

- [Grounded Intent](https://github.com/AS8148/grounded-intent) — Local workcell-image interpretation with open vision models, Apertus language reasoning and checked pick/place plans; includes a browser review interface. Apache-2.0; it does not control a robot.
- [See It, Say It, Pick It — Zemljic/Ryser](https://github.com/NoahZemljic/hack-apertus) — Apertus instruction/planning pipeline with Qwen visual grounding, SAM segmentation and geometric scene graphs. Apache-2.0.
- [See It, Say It, Pick It — Gude2Learn](https://github.com/jdawnduan/Gude2Learn) — Local Ollama pipeline separating open-model perception from text-only Apertus planning, with geometric hints and saved response traces. Apache-2.0.
- [See It, Say It, Pick It — Nightcats](https://github.com/u826318/see-it-say-it-pick-it) — Local Apertus language reasoning with open vision models, staged caches, action compilation and submitted development/held-out artifacts. Apache-2.0.
- [pAperSim](https://github.com/MykiellDeovennPagayonan/apertus-hackathon) — Apertus-assisted educational simulation authoring from registered components, with recipe validation and an editable browser workspace. Apache-2.0.
- [PrepTalk](https://github.com/ghwiegand/PrepTalk) — Apertus apprenticeship-interview coach in German, French and Italian, with rubric-based feedback, terminal UI and evaluation tooling. Apache-2.0.
- [SmartStart](https://github.com/Henryhuangsice/smartstart-hackapertus) — Apertus interview coach with adaptive follow-ups, FHGR rubric retrieval, web UI and separate assessment/consistency evaluations. Apache-2.0.
- [Bewerbär](https://github.com/iatee/Hack-Apertus/tree/main/track_2a) — Apertus apprenticeship-interview practice with German/French/Italian/Swiss German support, voice integration and criteria-based feedback. Apache-2.0; dialect feedback remains less reliable.
- [Interview Coach — Next Question](https://github.com/aliskin/apertus-interview-coach) — Apertus interview practice combining a deterministic interview controller, multilingual feedback and development simulations. Apache-2.0; official benchmark and consumer-GPU validation remain outstanding.
- [Los emal!](https://github.com/Alise441/los-emal) — Zurich German listening practice with Apertus dialogue and comprehension feedback, speech tools and everyday scenarios. Apache-2.0; dialect quality has not received native-speaker evaluation.
- [SONA Isochron](https://github.com/SONALAB-EU/sona-isochron) — Apertus translation and shortening of dubbing lines into German/French, with length budgets, meaning checks and repair-loop experiments. Apache-2.0.
- [Bon·Appétit](https://github.com/kinnuworks/bon-appetit) — Apertus mapping of Swiss receipt lines to food-composition data, with review queues and household purchase summaries; purchases are not dietary intake. Apache-2.0.
- [PoesIA on Apertus](https://github.com/OomAngel/poesia-apertus) — Poetry-writing workbench configured for Apertus, combining optional model suggestions with deterministic metre/rhyme tools and human authorship. Apache-2.0 wrapper; MIT engine.
- [Apertus Mundus](https://github.com/zRICGao/Apertus-Mundus) — Apertus narrative-roleplaying workbench with branching proposals, deterministic world-state updates, scoped memories and versioned saves. Apache-2.0; concurrent deployment remains unvalidated.
- [rosetta-flow](https://github.com/anesask/rosetta-flow) — Two-tier Apertus audit of agent traces, with checked source-step quotations, adaptation/evaluation artifacts and human-readable findings. Apache-2.0.
- [Bundesbrief](https://github.com/Powerworks-Global/bundesbrief) — Deterministic parliamentary-PDF extraction with optional local Apertus cross-checks, weighted review gates and a hash-chained ledger. Apache-2.0; default checks use a labelled stub.
- [Sigillum](https://github.com/chessoren/sigillum) — Static AI-project audit using Apertus to interpret evidence while rules assign grades; includes source references and review reports. Apache-2.0; grades do not certify residency or compliance.
- [SafeRouter ReplayLab](https://github.com/sumplus-real/saferouter-replaylab) — Local Apertus proposals for bounded retry/cancellation scenarios, checked against a synthetic reference protocol and exported as replayable counterexamples. Apache-2.0.
- [ScopeLock Verify](https://github.com/agent3-666/scopelock-verify) — Creative-brief requirement review combining local Apertus suggestions, source links, human approval and bounded media-file checks. Apache-2.0; model/runtime revisions have separate evaluation records.
- [FEDERAI](https://github.com/HesamSalehpour/federai-policy-assurance) — Apertus policy-document analysis with quotation matching, structured findings, hypothetical scenarios and human review. Apache-2.0; no expert-validated accuracy benchmark is published.
- [FRACTRA](https://github.com/sharmainelerato-glitch/FRACTRA) — Organisational dependency/failure simulation with a deterministic engine and Apertus-assisted interpretation and scenario proposals. Apache-2.0; simulation validity is not established by repeatability.
- [Systemic Resilience Copilot](https://github.com/rostys-fintech/systemic-resilience-copilot) — Apertus structuring and explanation around rule-based banking ICT recovery scenarios, with explicit missing-evidence states. Apache-2.0 notice; not a validated incident predictor.
- [Sturmglocke](https://github.com/TusharTechs/sturmglocke) — Crisis-staff training game using Apertus for multilingual alerts, calls and debriefs, with deterministic hazard-value checks. Apache-2.0; resident behaviour is illustrative.
- [LAMal Navigator](https://github.com/sachacoemelck/Health_Insurance_Apertus) — Swiss basic-insurance premium comparison with Apertus explanations, statutory retrieval and application/cancellation drafts. Apache-2.0; legal answers require review.
- [SafeSignal](https://github.com/iancuileana83-lab/safesignal-apertus) — Apertus extraction of suspected medicine side-effect reports with source quotations, completeness rules and human-edited export. Apache-2.0; fictional-data demo, not medical advice or automated submission.
- [Comfort](https://github.com/sambutracy/Hospital-Records) — Patient-record workspace with local Apertus evidence retrieval and reviewed summaries; newer visit-brief and journal features have unresolved model-validation limits. Apache-2.0.
- [Quotelet Aperto](https://github.com/vickhunter/quotelet) — Apertus converts multilingual price-list descriptions into validated calculator configurations and quote wording; deterministic code computes amounts. MIT.
- [Mirror AI](https://github.com/13512716817qq-creator/MirrorAI-HackApertus) — Business-inquiry routing with deterministic field/resource matching, an Apertus response layer and human follow-up; offline demo mode is separate. Apache-2.0.
- [See It, Say It, Pick It — Asian Prompters](https://github.com/azamafridi23/see-it-say-it-pick-it-hack-apertus) — Robotics challenge submission combining object segmentation, scene graphs and Apertus planning/safety agents to produce pick-and-place plans, clarification questions or refusals. Apache-2.0.
- [Sovereign Market Brief](https://github.com/simonlin1212/sovereign-market-brief) — Multilingual Apertus market commentary from code-computed facts, with deterministic checks and retained blocked drafts; supports local inference. Apache-2.0.
- [Apertus Draft Gate](https://github.com/ratchetcode/hermes-apertus-email/tree/main/track_2b) — Hermes-based email/newsletter drafting framework configured for Apertus, with minimised fictional contact context and local review/export commands; implements no mail sender. Apache-2.0.
- [HausPost](https://github.com/blucca/hauspost) — Multilingual tenant-update processing with Apertus, source-linked repair briefs, follow-up drafts and coordinator review. Apache-2.0.
- [Beneficia](https://github.com/Chinorab/beneficia/tree/main/track_2b) — Local beneficial-owner declaration drafting with Apertus extraction, line citations, deterministic ownership calculations and human-review queues. Apache-2.0.
- [Mandate Desk](https://github.com/gracelee087/hack-apertus/tree/main/track_2b) — Apertus invoice processing bounded by client mandates, deterministic payment checks, approval queues and signed audit records. Apache-2.0.
- [OriginPass CH–CN](https://github.com/sora200419/Hack-Apertus) — Swiss–China rules-of-origin decision-support prototype with Apertus classification and dossier drafting, deterministic rule traces and replay mode. Apache-2.0.
- [Alpenstroke](https://github.com/nikitojik/Alpenstroke) — Multilingual swimming-workout logging and planning with Apertus, deterministic training-load calculations and user-confirmed parsed workouts. Apache-2.0.
- [Zusage](https://github.com/shi1720/zusage) — Apertus 1.5 8B interview coach for Swiss apprenticeships, with a web interface and documented offline-demo and real-inference modes. Apache-2.0.
- [GemeindeSim](https://github.com/hatif03/gemeindesim) — Apertus 1.5 generative-agent town exploring responses to municipal policies and budgets; an exploratory simulation, not a validated policy forecast. Apache-2.0.
- [Kampung Sambau — Of the Dark](https://github.com/ratafani/Scary-Gate-Keeper) — Browser night-watch mystery with Apertus 1.5 visitor dialogue in English and German; Docker launch and aggregate live-model evaluation remain unverified by the author. Apache-2.0.
- [Sovereign Trade Copilot](https://github.com/quaner1234-cmd/sovereign-trade-copilot) — Garment-trade inquiry analysis and reply drafting with Apertus, per-fact source spans and human approval checks. Apache-2.0.
- [Apertus Sovereign Operations Bridge](https://github.com/ambrosinistefan8-stack/apertus-sovereign-operations-bridge) — Apertus 1.5 structured-fact extraction with deterministic conflict checks and human gates for proposed actions. Apache-2.0 notice; full licence text is linked rather than bundled.
- [Apertus Gate](https://github.com/ondmindmanagement-hub/apertus-gate) — Structured Apertus 1.5 risk review of proposed AI actions; produces allow, human-review or block decisions without executing actions. Apache-2.0.
- [MergeProof](https://github.com/williamleewilliam1-star/mergeproof-hack-apertus/tree/main/track_2b/src/mergeproof) — Evidence-linked, multilingual contributor summaries from public GitHub pull requests, with Apertus synthesis and deterministic fallback. Apache-2.0.
- [Referto Sovrano](https://github.com/nicholasbuenger/referto-sovrano) — Synthetic clinical-note structuring demo with a local Apertus client, de-identification, FHIR export and a hash-chain audit log; clinical validity and data-residency claims are unverified. MIT.
- [LoRaclette](https://github.com/bdravec/loraclette) — Experimental bottleneck-adapter training and position sweeps for Apertus; tested only on a small random model, not real 8B weights or the 4-bit path. Apache-2.0.

## Community and contributing

- **Discuss models:** official [8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B/discussions) and [70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B/discussions) Hugging Face discussions.
- **Contact the team:** [official contact page](https://apertus-ai.org/contact/); submit projects for the showcase through these channels.
- **Meet the community:** [Discord](https://discord.gg/t9TY8FsJd), linked by the official ecosystem post; [Swiss AI events](https://www.swiss-ai.org/events) and [Swiss AI Weeks](https://ai-weeks.ch/).
- **Follow updates:** [Mastodon](https://fosstodon.org/@apertus), [LinkedIn](https://www.linkedin.com/company/apertus/), [X](https://x.com/apertusllm), and [Bluesky](https://bsky.app/profile/did:plc:ytwqtr3ykzq6nzr7kg2465ca).

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), then suggest a resource with a primary source, a short description, and the relevant Apertus version. This list is released under [CC0 1.0](LICENSE); linked projects retain their own licenses.

For maintenance scripts and development commands, see the [helper documentation](https://github.com/rnckp/awesome-apertus/blob/main/src/README.md).
