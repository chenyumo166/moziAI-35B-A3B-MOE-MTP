---
language:
- en
- zh
license: other
tasks:
- text-generation
tags:
- gguf
- MoE
- financial-llm
- MoziSmartBit
- qwen3.5
- qwen3.6
- ornith
- MoziAI
- tool-calling
- uncensored
- vision
- MTP
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.8 — A Compact Yet Powerful Multimodal AI Model for Free Local Deployment

[English](V3.8/README.en.md) | [简体中文](V3.8/README.zh.md) | [繁體中文](V3.8/README.zh-hant.md) | [日本語](V3.8/README.ja.md) | [한국어](V3.8/README.ko.md) | [हिन्दी](V3.8/README.hi.md) | [Deutsch](V3.8/README.de.md) | [Français](V3.8/README.fr.md) | [Nederlands](V3.8/README.nl.md) | [Italiano](V3.8/README.it.md) | [Русский](V3.8/README.ru.md) | [Español](V3.8/README.es.md) | [Português](V3.8/README.pt.md) | [العربية](V3.8/README.ar.md) | [Bahasa Indonesia](V3.8/README.id.md) | [Türkçe](V3.8/README.tr.md) | [Tiếng Việt](V3.8/README.vi.md) | [Polski](V3.8/README.pl.md)

**Release Date: 2026-09-01** · **Version: V3.8**

---

## 📑 Table of Contents

- [1. Model Overview](#1-model-overview)
- [2. Key Features](#2-key-features) — Dynamic 7-Dimensional Thinking / LOOP / MoziSmartBit / Finance Focus
- [3. Version Upgrade Notes](#3-version-upgrade-notes)
- [4. Core Capabilities](#4-core-capabilities)
- [5. Technical Specifications](#5-technical-specifications)
- [6. ⚡ Quick Start](#6--quick-start-3-files--100-best-inference) — **3-file download**
- [7. Model Downloads](#7-model-downloads)
- [8. Launch Commands](#8-launch-commands)
- [9. Recommended Inference Parameters](#9-recommended-inference-parameters)
- [10. Quantization Format Comparison](#10-quantization-format-comparison)
- [11. Speculative Decoding Acceleration](#11-speculative-decoding-acceleration-key-feature)
- [12. VRAM Configuration Recommendations](#12-vram-configuration-recommendations)
- [13. Deployment Methods](#13-deployment-methods)
- [14. Benchmarks](#14-benchmarks)
- [15. Uncensored Optimization](#15-uncensored-optimization)
- [16. License](#16-license)
- [17. Contact](#17-contact)

---

## 1. Model Overview

MoziAI-35B-V3.8 is a locally deployable open-source multimodal AI large model developed by the team of Chen Yumo, a leading Chinese finance influencer. Built on the open-source base **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MoE 35B, MIT license), it integrates the team's self-developed financial data + financial domain capabilities + dynamic seven-dimensional thinking framework + agent LOOP reflection and iteration mechanism + Uncensored characteristic + MoziSmartBit hybrid quantization algorithm.

**💡 Size Advantage: only 15.9 GB** — the 35B-parameter MoE model is compressed to just **15.9 GB** via the self-developed MoziSmartBit quantization (about 30% smaller than standard Q4_K_M ~22GB). It fits in a single installer, runs on ordinary consumer GPUs (20GB VRAM+), reduces cloud token costs to **zero**, enables 7×24 hour token freedom, and ensures local data privacy and security. Licensed for **free commercial use** — zero barrier for individuals and enterprises.

---

## 2. Key Features

### 🧠 Dynamic Seven-Dimensional Thinking Framework

MoziAI's self-developed core reasoning framework. For any task, the model first outputs a **moziAI-Think** marker, then dynamically unfolds structured thinking based on task complexity:

| Level | Scenario | Typical Tasks | Dimensions Expanded |
| --- | --- | --- | --- |
| **Level 0** | Simple Q&A | Term explanation, fact lookup, translation, summarization | ①Understand task ⑤Resource needs (2-dimension quick answer) |
| **Level 1** | Analysis & Diagnosis | Market research, copywriting, data analysis, report reading, strategy evaluation | ①②③⑤⑥ Five-dimension evaluation |
| **Level 2** | Complex Dev/Strategy | Code development, architecture design, quant strategy development, multi-step workflows, system design | ①②③④⑤⑥⑦ Full 7-dimension deep reasoning |

> Seven dimensions: ①Understand task ②Complexity assessment ③Dependencies ④Risk assessment ⑤Resource needs ⑥Acceptance criteria ⑦Execution strategy

### 🔄 Agent LOOP Iteration Mechanism

Complex tasks automatically enter **moziAI-Loop** iteration mode: **Round 1 execute+assess → Round 2 adjust+verify**, ensuring output undergoes self-validation before the final answer. The model works like a senior engineer — "decompose problem → evaluate plan → execute → reflect → optimize" — significantly improving accuracy and executability of complex tasks. Simple Q&A automatically skips the Loop.

### 📦 MoziSmartBit Smart Quantization

Self-developed layered smart quantization compresses the 35B-parameter MoE model to about **15.9 GB** — about 6.5 GB (~30%) smaller than standard Q4_K_M (~22 GB) while maintaining **~99%** of FP16 accuracy. Traditional quantization applies uniform precision to all layers; MoziSmartBit adopts a smart differentiated strategy for MoE structure, delivering accuracy better than Q4_K_M. Compression ratio: **4.5x**.

### 💰 Financial Vertical Focus

Deeply optimized for financial Q&A, quantitative programming, and tool calling. Finance has extremely low tolerance for hallucination — MoziAI significantly outperforms general models of the same size in this domain.

### 🛡️ Uncensored Feature

No content moderation restrictions, free output, complete information, local privacy. Suitable for academic research, deep analysis, free discussion and more. (See [Section 15](#15-uncensored-optimization))

### 🌐 Other Features

- **Multilingual support**: 201 languages and dialects, with specially optimized Chinese
- **General programming**: Full-stack development, debugging, architecture design, covering Python/JS/TS/Go/Rust
- **Writing**: High-quality multi-genre writing — research reports, analysis articles, technical docs, creative content
- **Vision understanding**: Multimodal vision, understands screenshots locally
- **Multi-framework support**: llama.cpp / Ollama / LM Studio / Jan
- **Multi-Agent support**: OpenClaw / Hermes / Cursor / Claude Code / Codex etc., native tool calling and multi-turn task orchestration

---

## 3. Version Upgrade Notes

V3.8 is retrained on the same-generation self-developed training dataset system as 27B-V3.8 (identity / dynamic seven-dimensional thinking / LOOP iteration / financial vertical domain), with key enhancements to the dynamic seven-dimensional thinking + LOOP reasoning mode — smarter complexity recognition, higher complex-task completion rates, stronger "think before act" ability. The Uncensored characteristic and financial vertical optimization are carried forward.

MoziAI maintains an active upgrade cadence, staying at the forefront of AI development while continuously making local AI models lighter and more capable through self-developed technology.

---

## 4. Core Capabilities

| Capability | Description |
| --- | --- |
| Market Analysis | Macro/micro economic interpretation, A-share/HK/US/commodity/crypto market logic |
| Finance & Research | Earnings report interpretation, research summary extraction, valuation & earnings forecasting |
| Risk & Compliance | Product risk assessment, investment advice compliance, regulatory policy interpretation |
| Quant & Strategy | Quant strategy design, Pyramid (PEL) quantitative programming, backtest logic, factor construction, tool calling |
| Tool Calling | Pluggable into live market data, databases, research retrieval and other financial data sources |

---

## 5. Technical Specifications

| Item | Specification |
| --- | --- |
| Base Model | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MIT license) |
| Parameter Count | 35B MoE architecture, 256 routing experts + 1 shared expert, 8 experts active per token |
| Quantization | Self-developed MoziSmartBit smart quantization + GGUF standard format |
| Context Length | 256K (262,144 tokens) |
| Model Size | ~15.9 GB |
| Minimum VRAM | **20GB+** deployable (CPU offload); **24GB+** smooth long context; **32GB+** full 256K + vision |
| Inference Frameworks | llama.cpp / Ollama / LM Studio / Jan |
| Inference Speed | With speculative decoding: **140+ tok/s** on AMD R9700 GPU / **70+ tok/s** on AMD MAX+395 iGPU — token freedom locally |
| Developer | Chen Yumo Team |

---

## 6. ⚡ Quick Start 3 Files = 100% Best Inference

> ⚠️ **Key tip**: Best inference requires downloading **3 files at once** — main model, vision projector, chat template. Missing any one loses the corresponding capability.

### 6.1 Download Model Files

Download these **3 files** from HuggingFace / ModelScope to one local folder (main model at **repo root**, vision projector under `mmproj/35B/`, chat template under `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Main model (required, 15.9 GB, repo root)
mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf                                 ← Vision projector (required, ~1 GB)
V3.8/moziAI-V3.8-35B-chat-template.jinja                                    ← Chat template (required, 7-dim thinking + Loop)
```

| File | Size | Required | Purpose |
| --- | --- | --- | --- |
| Main model `.gguf` | ~15.9 GB | **Yes** | Model weights, core reasoning |
| Vision `mmproj` | ~1 GB | **Yes** | Multimodal vision; without it image capability is lost |
| Chat template `.jinja` | tiny | **Yes** | Injects MoziAI identity + 7-dim thinking + LOOP instructions |

### 6.2 Launch and Use

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Open `http://localhost:8080` in your browser to start chatting. See Section 9 for full recommended parameters.

---

## 7. Model Downloads

| Platform | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio users**: search `moziAI` in [LM Studio](https://lmstudio.ai) to download with one click.

> 💡 **Download tip**: go to the HuggingFace repo above, open the **"Files and versions"** tab, download the main model at the **repo root**, then the vision projector from `mmproj/35B/` and the chat template from `V3.8/`, keeping all three in the same folder.

---

## 8. Launch Commands

### Minimal Launch (with 3 files)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Full Recommended Launch

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 \
  --reasoning on --reasoning-format deepseek-legacy \
  --spec-default \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.024 \
  --repeat-penalty 1.05 --presence-penalty 0
```

> 💡 If VRAM is limited: lower `-c` (e.g. 131072), or add `--fit on` to let llama.cpp auto-fit VRAM.

---

## 9. Recommended Inference Parameters

Optimized from local testing (AMD Radeon AI PRO R9700 32GB):

| Parameter | Daily Tasks / Copywriting | Complex Tasks / Advanced Coding | Notes |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | Daily stability; moderate exploration for complex coding |
| top\_p | 0.95 | 0.95 | Nucleus sampling threshold |
| top\_k | 20 | 20 | Truncated sampling |
| min\_p | 0.024 | 0.024 | Minimum probability filter |
| repeat\_penalty | 1.05 | 1.05 | Repetition penalty |
| presence\_penalty | 0 | 0 | No presence penalty |
| context\_length | 131072 | 262144 | Daily 128K / Complex 256K (llama.cpp default 128K) |
| reasoning | on | on | Enable reasoning chain (CoT) |
| reasoning\_budget | 400 | 1000 | Reasoning budget tokens (higher for complex tasks) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Reasoning in separate field |
| **spec-type** | **default** | **default** | **Speculative decoding (ngram, MoE-optimal, see Section 11)** |
| KV cache | q4\_0 | q4\_0 | Quantized KV cache (unified kv-unified) |

> 💡 **Thinking mode**: enabled via `--reasoning on` — the model reasons internally before answering. `reasoning_budget` caps the max thinking tokens.

---

## 10. Quantization Format Comparison

| Format | Size | Accuracy | Notes |
| --- | --- | --- | --- |
| FP16 original | ~70 GB | 100% | Lossless, needs pro GPU |
| **MoziSmartBit (this model)** | **~15.9 GB** | **~99%** | **Self-developed smart quantization, best accuracy per size** |
| Q4_K_M | ~22 GB | ~98% | Standard GGUF 4-bit |
| Q5_K_M | ~24.7 GB | ~99% | Higher accuracy |
| Q6_K | ~28.5 GB | ~99.5% | Near-lossless |
| Q8_0 | ~36.9 GB | ~100% | Lossless |

> MoziSmartBit keeps ~99% accuracy while compressing the 35B MoE model to 15.9 GB (4.5x compression), ~30% smaller than Q4_K_M — ideal for consumer GPUs.

---

## 11. Speculative Decoding Acceleration Key Feature

This model significantly boosts inference speed via **Speculative Decoding** — locally measured **~1.5-2x faster** than disabled.

- **MoE-optimal config**: llama.cpp recommends **ngram speculative decoding** (`--spec-default`) for MoE architectures — fastest and most stable in local testing
- **About the "MTP" in the name**: "MTP" refers to the base model's Multi-Token Prediction weights (fully preserved); llama.cpp's MTP draft support for MoE is limited, so MoziAI uses the ngram scheme for the best measured speed

### Enable Parameter

```bash
--spec-default
```

### Tuning Suggestions

| Config | Scenario |
| --- | --- |
| --spec-default (default) | Recommended: balanced speed & VRAM |
| Disable (remove the flag) | Low-VRAM scenarios; slightly slower |

---

## 12. VRAM Configuration Recommendations

Measured with the MoziSmartBit build (model + vision ~16.4GB total):

| VRAM | Recommended Config | Notes |
| --- | --- | --- |
| 20 GB | 150K context, q4\_0 KV cache, vision supported | Model+vision ~16.4GB; 256K+vision uses ~19.5GB |
| **24 GB** | **Full 256K, q4\_0 KV cache, perfect vision** | **Recommended**: vision+256K uses ~20.4GB, ~3.6GB headroom |
| 32 GB+ | Full 256K, ample headroom | e.g. R9700 32GB: vision+256K with ~10GB headroom, max config |

> 💡 Longer context = more VRAM. On OOM, lower `-c` step by step. Use `--fit on` to auto-fit VRAM. Supports NVIDIA / AMD GPUs.

---

## 13. Deployment Methods

### Ollama Deployment

```bash
cat > Modelfile << 'EOF'
FROM ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 131072
PARAMETER num_gpu 99
EOF

ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan

Search `moziAI` in LM Studio / Jan and download the Q4\_K\_M quantized version (LM Studio reads root-dir models by default; for legacy versions use "Add from URL" to import files from their version directory, e.g. `V3.7/`).

> 💡 Ollama's support for mmproj and chat\_template is limited — prefer llama.cpp for the full feature set.

---

## 14. Benchmarks

MoziAI-35B-V3.8 is fine-tuned, distilled and further developed from the deepreinforce-ai/Ornith-1.5-35B-A3B base, with financial vertical as the core optimization direction. Multi-model comparison (MoziAI general capabilities match base Ornith-1.5-35B-A3B; data carried from V3.7 measurements — V3.8 shares the same base and training system):

| Benchmark | moziAI-35B-V3.8<br>(This model) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Coding** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Reasoning** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Agentic** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI's financial vertical — earnings interpretation, quant strategy, risk & compliance, agent tool calling — significantly outperforms general models. Gemma-4 / Qwen3.6 numbers are official public results.

---

## 15. Uncensored Optimization

This model inherits the Uncensored characteristic of the Ornith-1.5-35B-A3B base:

| Advantage | Description |
| --- | --- |
| No restrictions | Refuses no topics, including sensitive or controversial content |
| Free output | Not constrained by safety policies, generates any type of reply |
| Complete information | Provides unfiltered information, ideal for research and analysis |
| Local privacy | Local deployment means fully private data, no cloud review |

**Use cases**: academic research, deep analysis, free discussion, unrestricted AI conversation.

**Note**: This is a locally deployed model — output is entirely controlled by the user; the model bears no content-moderation responsibility.

---

## 16. License

This model uses a **custom restrictive license**:

- ✅ **Allowed** — free commercial use, copying and distribution
- ❌ **Forbidden** — further development, resale, sub-licensing
- 📋 **Required** — retain original copyright notice, credit: moziAI-35B

The model is provided "as is" without warranties of any kind. Model output is for reference only and does not constitute investment advice. Users assume all risk.

See the [LICENSE](LICENSE) file for full terms.

---

## 17. Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.