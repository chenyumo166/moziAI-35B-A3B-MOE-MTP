---
language:
- zh
- en
license: other
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
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-A3B-MOE - Financial Vertical Domain LLM - V3.7

English | [中文](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md) | [繁體中文](README.zh-hant.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md)

## Model Overview

MoziAI-35B-A3B-MOE is a local open-source financial AI multimodal LLM (supports vision and tool calling) developed by Chinese finance influencer Chen Yumo's team, fine-tuned/distilled from the Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** architecture, MIT licensed) foundation model. Through the self-developed **MoziSmartBit Intelligent Quantization** technology, the 35B-parameter MoE model is compressed to approximately **15.5 GB**, achieving an optimal balance between precision and size with near-lossless ~99% precision quality.

In addition to retaining general AI capabilities, this model focuses on optimizing financial vertical domain applications, including financial Q&A, quantitative programming, tool calling, and general programming.

The model developer Chen Yumo frequently uses this model for local financial data analysis, quantitative strategy R&D, market research, article writing, overall project advancement, general programming, and 256K context tasks via openclaw/hermes. It can be deployed locally on consumer-grade GPUs, saving substantial cloud token costs, achieving 7X24 token freedom while ensuring local data privacy and security.

Supports llama.cpp, Ollama, LM Studio and other mainstream inference frameworks.

**Release Date: 2026-08-21** | **Version: V3.7**

## Model Features

- **Financial Vertical Focus**: Deep optimization for financial Q&A, quantitative programming, and tool calling
- **MoziSmartBit Intelligent Quantization**: Self-developed smart quantization, best balance of precision and size, compressed to approximately **15.5 GB**
- **Consumer-grade Deployment**: Deployable on consumer GPUs with 20GB or 24GB+ VRAM, supports 256K long context
- **Multilingual Support**: 201 languages and dialects, with enhanced Chinese capabilities, covering English/Japanese/Korean/German/French/Spanish/Portuguese and more
- **General Programming**: Full-stack development, code debugging, architecture design, script writing, covering Python/JS/TS/Go/Rust and other mainstream languages
- **Article Writing**: High-quality multi-genre writing including research reports, analysis articles, technical documentation, creative content
- **Vision Understanding**: Supports multimodal vision, local screenshot input, image comprehension
- **Uncensored Free Output**: No content censorship, free discussion on any topic without safety restrictions
- **Enhanced Reasoning**: Chain-of-thought training for improved reasoning quality
- **Multi-Framework Support**: Compatible with llama.cpp, Ollama, LM Studio, Jan
- **Multi-Agent Platform Support**: Deep integration with OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex and other mainstream AI IDEs and Agent frameworks, natively supports tool calling and multi-turn task orchestration, ready to use out of the box

## Uncensored Advantages

This model inherits the **Uncensored** feature from the Ornith-1.5-35B-A3B base model, with the following advantages:

| Advantage | Description |
|-----------|-------------|
| **No Censorship** | Will not refuse any topic, including sensitive or controversial content |
| **Free Output** | Unrestricted by safety policies, can generate any type of response |
| **Complete Information** | Provides unfiltered complete information, suitable for research and analysis |
| **Local Privacy** | Local deployment means data is fully private and free from cloud censorship |

> **Use Cases**: Academic research, deep analysis, free discussion, unrestricted AI conversation.
> **Note**: This is a locally deployed model, output content is fully controlled by the user, no content moderation responsibility.

## Core Capabilities

| Capability Area | Description |
|----------------|-------------|
| Market Analysis | Macro/microeconomic interpretation, A-share/HK/US stock/commodity/crypto market logic |
| Financial Reports | Key financial indicator interpretation, research report summary, valuation & earnings forecast assistance |
| Risk & Compliance | Product risk assessment, investment advice compliance, financial regulation policy interpretation |
| Quant & Strategy | Quant strategy design, Pyramid (PEL) quantization, backtesting logic, factor construction and tool calling |
| Tool Calling | Integration with real-time quotes, databases, research report retrieval and other financial data sources |

## Technical Specifications

| Item | Specification |
|------|---------------|
| Base Model | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT licensed) |
| Parameters | 35B MoE (256 routed experts + 1 shared expert, 8 active per token) |
| Quantization | Self-developed MoziSmartBit Intelligent Quantization + GGUF standard format |
| Context Length | 256K (262,144 tokens) |
| Model Size | ~15.5 GB (MoziSmartBit Uncensored version) |
| Min VRAM | Consumer GPUs with 20GB+ VRAM (e.g., RTX 4060 Ti 16G with CPU offload), 24 GB recommended (with vision + long context) |
| Inference Framework | llama.cpp / Ollama / LM Studio / Jan |
| Inference Speed | Algorithm-optimized: 140+ token/s on AMD R700 GPUs, 70+ token/s on AMD MAX+395 CPU iGPU, local token freedom |
| Team | Chen Yumo Team |

## Quantization Format & Model Size Comparison

| Quant Format | Model Size | Precision | Notes |
|--------------|------------|-----------|-------|
| **FP16 (original)** | ~70 GB | 100% | Original 16bit |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **Used by MoziAI, optimal quantization scheme** |
| Q4_K_M | ~21.2 GB | ~98% | GGUF standard 4bit |
| Q5_K_M | ~24.7 GB | ~99% | Higher quality |
| Q6_K | ~28.5 GB | ~99.5% | Near lossless |
| Q8_0 | ~36.9 GB | ~100% | Lossless |

> MoziAI V3.7 uses MoziSmartBit Intelligent Quantization, maintaining ~99% precision while compressing the 35B parameter MoE model to ~15.5 GB (~4.5x compression ratio), balancing inference quality with deployment accessibility for consumer GPUs.

## MoziSmartBit Intelligent Quantization

Traditional quantization uses uniform precision across all layers. **MoziSmartBit Intelligent Quantization** applies differentiated quantization strategies for optimal size-precision balance.

### Compression Effect

Traditional quantization compresses all parts of the model uniformly, often leading to significant precision loss. MoziSmartBit Intelligent Quantization uses a self-developed intelligent compression strategy that **achieves substantial size reduction with minimal precision loss**:

- **Minimal Quantization Loss**: Training gains > quantization loss. The trained MoziAI-35B achieves better PPL on financial domain text than the pre-training bf16 base model, reducing hallucination and perplexity compared to similar AI models
- **~4.5x Size Reduction**: Compressed from ~70 GB (FP16) to ~15.5 GB, also significantly smaller than Q4_K_M (~21 GB), significantly lowering VRAM and storage requirements
- **Consumer GPU Friendly**: A 35B MoE model that previously required high-end GPUs can now run smoothly on 20GB~24GB VRAM

### Comparative Advantages

**vs Q4_K_M (~21.2 GB)**: ~27% smaller (~15.5 GB), with precision **higher** than Q4_K_M, lower VRAM barrier — runs smoothly on mid-range consumer GPUs (24GB).

**vs FP16 original (~70 GB)**: ~4.5x compression, training effective + minimal quantization loss (training gains > quantization loss), enabling local 256K context deployment on consumer GPUs instead of professional-grade hardware.

## Recommended Inference Parameters

Based on local production config (AMD Radeon AI PRO R9700 32GB):

| Parameter | Value | Description |
|-----------|-------|-------------|
| temperature | 0.6 | Balance creativity vs accuracy |
| top_p | 0.95 | Nucleus sampling threshold |
| top_k | 20 | Truncation sampling (V3.7 optimized) |
| repeat_penalty | 1.05 | Repetition penalty |
| presence_penalty | 0 | No presence penalty |
| context_length | 262144 | 256K long context |
| batch_size | 2048 | Batch size |
| ubatch_size | 512 | Micro-batch size |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | KV cache quantization (kv-unified) |
| poll | 0 | No GPU polling when idle, energy efficient |
| reasoning | on | Enable reasoning chain (chain of thought) |
| reasoning_budget | 400 | Reasoning budget in tokens |
| reasoning_format | deepseek-legacy | Reasoning format |
| samplers | top_k;top_p;temperature;typ_p | Sampler order |

### llama.cpp Launch Command

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

### VRAM Configuration Recommendations

Since user GPU configurations vary widely, here are recommended parameters for different VRAM sizes (all for MoziSmartBit version):

| VRAM | Recommended Context | KV Cache | Vision Support | Notes |
|------|---------------------|----------|----------------|-------|
| 20 GB | 150K | q4_0 | Supported | Model+vision ~16.4GB, actual test shows 200K+vision uses ~19.5GB VRAM |
| 24 GB | 256K full | q4_0 | Full support | Vision+256K long context, uses ~20.4GB VRAM, ~3.6GB headroom |
| 32 GB+ | 256K full | q4_0 | Full support | Vision+256K long context, sufficient headroom ~10GB, best config |

**NVIDIA**

| VRAM | GPU Model |
|------|-----------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD**

| VRAM | GPU Model |
|------|-----------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel**

| VRAM | GPU Model |
|------|-----------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (requires CPU offload) |

**Shared Memory iGPUs**

| VRAM | Processor |
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |

> 💡 **Tip**: As long as your VRAM meets the above requirements, it works. No brand or model restrictions. Supports NVIDIA / AMD / Intel discrete GPUs, and also 128GB unified memory iGPUs listed above.

> 💡 **Tip**: Longer context uses more VRAM. If you encounter OOM (out of memory), gradually reduce the `-c` value. Use `--fit on` to let llama.cpp auto-adjust layers to fit your VRAM.

### Ollama Deployment

```bash
# Create Modelfile
FROM ./moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Build and run
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan Deployment

Search `moziAI-35B` in LM Studio or Jan, download the MoziSmartBit quant version.

## Benchmark Evaluation

MoziAI is fine-tuned from **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI is optimized for financial vertical domains on top of the base model, delivering superior performance in financial Q&A, quantitative programming, and tool calling scenarios. MoziAI-35B general capabilities are consistent with the Ornith-1.5-35B-A3B base model.

| Benchmark | MoziAI-35B (this model) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Description |
|-----------|-------------------------|-------------|------------|------------|-------------|-------------|
| Terminal-Bench 2.1 | 64.2 | 59.3 | 42.1 | - | 41.4 | Autonomous terminal coding |
| Terminal-Bench (Claude Code) | 62.8 | 59.3 | - | - | 38.9 | Claude Code coding |
| SWE-bench Verified | 75.6 | 77.2 | 52.0 | - | 70.0 | Real-world software engineering |
| SWE-bench Pro | 50.4 | 53.5 | 35.7 | - | 44.6 | Complex software engineering |
| SWE-bench Multilingual | 69.3 | 71.3 | - | - | 60.3 | Multilingual coding |
| NL2Repo | 34.6 | 36.2 | 15.5 | - | 20.5 | Natural language to repo |
| LiveCodeBench v6 | 63.3 | 83.9 | 80.0 | 77.1 | - | Competitive programming |
| GPQA Diamond | 88.4 | 87.8 | 84.3 | 82.3 | - | Scientific reasoning |
| AIME 2026 Math | 93.3 | 94.1 | 89.2 | 88.3 | - | Math reasoning |

> MoziAI-35B general benchmark scores are consistent with the Ornith-1.5-35B-A3B base model. Financial vertical domain is MoziAI's core optimization direction, significantly outperforming general models in scenarios like financial report analysis, quantitative strategy, risk & compliance, and agent tool calling. Gemma4 and Qwen3.6 data from official public results.

## Model Download

Due to the large model size (~15.5 GB), weights are hosted on multiple community platforms:

| Platform | URL |
|----------|-----|
| HuggingFace | [chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://huggingface.co/chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |
| ModelScope | [chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://modelscope.cn/models/chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |
| GitHub | [chenyumo166/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://github.com/chenyumo166/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |

> 💡 **Download Tip**: Click the link above to go to the HuggingFace repository, then go to the **"Files and versions"** tab to download all files under the V3.7 directory (main model, vision projection, chat template). Make sure all three files are placed in the same directory.

### ⚠️ Important: Vision Capability Requires mmproj File

This model supports multimodal vision. The **vision projection file (mmproj)** is included in the version directory:

- **Vision file**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16 precision)
- **Placement**: Same version directory as the GGUF model file
- **Loading**: Load with `--mmproj` flag when starting llama-server

```bash
llama-server -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf
```

> Without the vision file, the model will **lose image understanding capability** and only retain text-only conversation.

## Quick Start

### 1. Download Model Files

Download all files under the V3.7 directory from HuggingFace / ModelScope:

```
V3.7/
├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Main model (required)
├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision projection (optional)
└── moziAI-V3.7-35B-chat-template.jinja                  # Chat template (recommended)
```

### 2. Start Inference Server

For the full recommended configuration, see [llama.cpp Launch Command](#llamacpp-launch-command) above.

Minimal launch (core params only):

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Add `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` for vision capability.

### 3. Start Using

Open `http://localhost:8080` in your browser to start chatting.

### Directory Structure

```
moziAI-35B/
├── README.md              # Chinese version
├── README.en.md           # This file (English)
├── LICENSE                # License
├── V3.7/                  # V3.7 version (self-contained)
│   ├── RELEASE_NOTES.md                       # Release notes
│   ├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Main model
│   ├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision projection
│   └── moziAI-V3.7-35B-chat-template.jinja   # Chat template
```

For the future upgrade plan, see [未来升级计划.md](未来升级计划.md).

## SEO Keywords

financial AI LLM, local open source model, end-side model, quant programming, MoziSmartBit, intelligent quantization, GGUF quantization, MoE model, local open source LLM, local deployment, financial AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, no censorship, free output, unrestricted, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, financial vertical domain, open source model

## License (Important)

This model uses a **Custom Restrictive License**:

### ✅ Allowed
- **Free Commercial Use**: Free to integrate into commercial products
- **Copy & Distribute**: Can copy, download, and share

### ❌ Prohibited
- **Derivative Works**: No modification, translation, adaptation, merging, or fine-tuning of the model or any part of it
- **Resale**: No selling the model alone or as part of a product
- **Re-licensing**: No granting sublicenses

### 📋 Requirements
- Must retain original copyright notice
- Attribution: moziAI-35B

> See [LICENSE](./LICENSE) for full terms.

## Disclaimer

Provided "as is" without warranty. Model output is for reference only, not investment advice. Users bear all risks.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.
