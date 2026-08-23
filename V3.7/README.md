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

# MoziAI-35B-V3.7-A3B-MOE-MTP-Uncensored - Free Locally Deployable Small Yet Powerful Multimodal AI

Language / 语言选择  
[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Model Introduction

MoziAI-35B-A3B-MOE is a locally deployable open-source multimodal large language model developed by the Chen Yumo team (a Chinese financial KOL), focusing on financial domain enhancement, supporting vision, tool calling, complex long-task capabilities, and consumer GPU deployment. It is fine-tuned based on the Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B/Qwen3.6-35B-A3B** architecture) base model.

The R&D team's philosophy is to enable powerful local AI large models and agents to enter thousands of households and small and medium-sized enterprises, eliminating the need for expensive AI hardware costs or cloud API costs. Through our self-developed **MoziSmartBit intelligent quantization** technology, we compress the 35B parameter MoE model to approximately **15.5 GB**, achieving an optimal balance between model accuracy and size, with almost 99% accuracy compared to FP16. Although the model has 35 billion parameters overall, it actually only activates 30 billion parameters via MoE sparse expert technology and supports MTP speculative decoding for accelerated inference. Testing shows it can complete local free deployment on a consumer GPU with 20GB VRAM and achieve 140+ tokens/s inference speed, outperforming many cloud-charged AI large models in speed.

In addition to retaining the capabilities of general large AI models, we focus on optimizing: financial vertical domain applications, financial Q&A, quantitative programming, general programming, tool calling, and success rate of 256K complex long context tasks. It can be deployed for free on consumer-grade graphics cards locally, saving a lot of cloud token costs, enabling 7X24 hours token freedom and ensuring local data privacy and security.

**Release Date:** 2026-08-22 | **Version:** V3.7

## Model Download

Due to the large model size (~15.5 GB), model weights are hosted on multiple community platforms:

| Platform | URL |
| -------------- | ----------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

> 💡 **LM Studio Users**: Search for `moziAI` directly in [LM Studio](https://lmstudio.ai) and download with one click, no manual file download required.  
> 💡 **Download Tip**: Please click the link above to enter the HuggingFace repository, download all files under the V3.7 directory in the **"Files and versions"** tab (main model, vision projection, chat template), ensure all three files are placed in the same directory.

⚠️ **Important: Vision capability requires an additional mmproj file**

This model supports multimodal vision, and the vision projection file (mmproj) is already included in the version directory:

- **Vision File**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16 precision)
- **Placement**: Place in the same version directory as the GGUF model file
- **Loading**: Load via the `--mmproj` parameter when starting llama-server

> Without loading the vision file, you will lose image understanding capability and only retain pure text conversation capability.

⚠️ **Important: You must load the chat template file**

This model uses a dedicated chat template, **failure to load will result in incorrect dialogue format, broken reasoning chain, and significantly reduced reply quality**. The chat template file is already included in the version directory:

- **Template File**: `moziAI-V3.7-35B-chat-template.jinja` (~5 KB, jinja format)
- **Placement**: Place in the same version directory as the GGUF model file
- **Loading**: Load via the `--chat-template-file` parameter when starting llama-server

> Without loading the chat template, the model may not correctly identify system prompts, user messages, and thinking blocks, resulting in messy output format or degraded reasoning ability.

### llama.cpp Launch Command (Recommended configuration for 20G+ GPU with 256K context)

> Note: If VRAM is below 20G, reduce the context parameter 262144 for `-c`.

```bash
llama-server \
  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 1000 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

## Quick Start

### 1. Download Model Files

Download all files from the V3.7 directory to your local machine from HuggingFace / ModelScope:

```
V3.7/
├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # Main model (required)
├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision projection (optional, download if you need vision)
└── moziAI-V3.7-35B-chat-template.jinja                  # Chat template (required! Missing template causes format errors)
```

> ⚠️ **Chat template is a required file**, not optional. This model has a custom dialogue format (including reasoning chain/thinking blocks), missing the template will cause messy model output format and degraded reasoning ability. Please be sure to download and load it at startup.

### 2. Start Inference Service

For the complete recommended configuration startup command, please refer to the [llama.cpp Launch Command](#llamacpp-launch-command) section above.

Minimal startup (core parameters only):

```bash
llama-server \
  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Add `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` if you need vision capability.

### 3. Start Using

Open `http://localhost:8080` in your browser to start chatting.

### Directory Structure

```
moziAI-35B-A3B-MOE-MTP-Uncensored/
├── README.md              # This file (Chinese documentation)
├── README.en.md           # English version of the documentation
├── LICENSE                # License
├── V3.7/                  # V3.7 version (self-contained)
│   ├── RELEASE_NOTES.md                       # Release notes
│   ├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # Main model
│   ├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision projection
│   └── moziAI-V3.7-35B-chat-template.jinja   # Chat template
```


## Model Features

- **MoziSmartBit Intelligent Quantization**: Self-developed intelligent quantization technology, optimal balance between accuracy and size, almost lossless compression of the model to ~15.5 GB
- **Complex Long Task Capability**: Training enables the model agent to automatically plan intelligent loop processing of stuck points and self-thinking mechanism, realizing automatic execution and self-adjustment of complex tasks, eliminating the trouble of human users constantly optimizing prompts for agents
- **Small Model, Great Capability**: On complex tasks, comprehensive performance outperforms similar models within 35 billion parameters, even outperforming some models several times larger in parameters
- **MOE+MTP Speed Advantage**: Although the model has 35 billion parameters overall, it actually only calls 8+1 experts, totaling 3 billion parameters, inference is faster, very suitable for consumer GPUs with 20GB~24GB VRAM for local deployment, enjoying 140+ tokens/s inference speed
- **Financial Vertical Deep Cultivation**: Deeply strengthened financial Q&A, quantitative programming, tool calling capabilities
- **Consumer-Grade Deployment**: Consumer GPUs with 20GB~24GB VRAM or more can be deployed locally, supporting up to 256K long context inference
- **Multilingual Support**: Supports 201 languages and dialects, with special optimization for Chinese, 同时支持 English, Japanese, Korean, German, French, Portuguese and other mainstream languages
- **General Programming Capability**: Supports full-stack development, code debugging, architecture design, script writing, covering mainstream languages such as Python/JS/TS/Go/Rust
- **Article Writing Capability**: Supports high-quality writing in multiple genres, including research reports, analysis articles, technical documents, creative content, etc.
- **Visual Understanding**: Load the vision file in the inference framework to support multimodal vision, you can locally paste screenshots into the chat window, the model can understand the information in the image
- **Uncensored Free Output**: No content censorship restrictions, freely discuss any topic, not constrained by security policies
- **Reasoning Logic Enhancement**: Trained with reasoning logic (chain-of-thought), further improving reasoning quality
- **Multi-framework Support**: Compatible with mainstream inference frameworks such as llama.cpp, Ollama, LM Studio, Jan
- **Multi-agent Platform Support**: Deeply adapted to domestic and foreign mainstream AI IDEs and Agent frameworks such as OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex, native support for tool calling and multi-round task orchestration, ready to use out of the box

## Uncensored Advantages

This model inherits the Uncensored characteristics from the base model Ornith-1.5-35B-A3B, with the following advantages:

| Advantage | Description |
| ----- | --------------------- |
| No censorship restrictions | Will not refuse any topic, including sensitive and controversial content |
| Free output | Not constrained by security policies, can generate any type of reply |
| Complete information | Provides unfiltered complete information, suitable for research and analysis scenarios |
| Local privacy | Local deployment means data is completely private, not subject to cloud review |

**Application Scenarios**: Free commercial use, academic research, in-depth analysis, open discussion, unrestricted AI dialogue  
**Note**: This model is for local deployment, output content is completely controlled by the user, we do not bear content review responsibility.

## Core Capabilities

| Capability Area | Description |
| ----- | ------------------------------------------ |
| Market Analysis | Macro/microeconomic interpretation, A-share/HK stock/US stock/commodity/cryptocurrency market analysis and logic sorting |
| Financial Research Report | Interpretation of key indicators in financial reports, extraction of research summary, valuation and earnings forecast assistance |
| Risk Control & Compliance | Product risk assessment, investment advice compliance tips, interpretation of financial regulatory policies |
| Quantitative Strategy | Quantitative strategy idea design, Pyramid (PEL) quantification, backtesting logic, factor construction and tool calling |
| Tool Calling | Can access real-time market data, databases, research retrieval and other financial data |

## Technical Specifications

| Item | Parameters |
| ------ | ---------------------------------------------------------------------------------- |
| Base Model | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MIT license) |
| Parameter Size | 35 billion (35B) MoE architecture, 256 routed experts + 1 shared expert, 8 active per token |
| Quantization Method | Self-developed MoziSmartBit intelligent quantization algorithm + GGUF standard format |
| Context Length | 256K (262,144 tokens) |
| Model Size | ~15.5 GB (MoziSmartBit Uncensored version) |
| Minimum VRAM Requirement | Consumer GPU with 20GB VRAM or more (e.g., RTX 3060 12G requires CPU offloading, RTX 4060 Ti 16G, etc.), recommended 24 GB (including vision + long context) |
| Inference Framework | llama.cpp / Ollama / LM Studio / Jan |
| Inference Speed | Through algorithm optimization, AMD R9700 GPU can reach 140+ tokens/s / AMD MAX+395 CPU iGPU can reach 70+ tokens/s, enabling local token free output |
| Development Team | Chen Yumo Team |

## Quantization Format and Model Size Comparison

| Quantization Format | Model Size | Accuracy Retention | Description |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (original) | ~70 GB | 100% | Original 16-bit precision |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **Self-developed intelligent quantization scheme used by this model** |
| Q4_K_M | ~22 GB | ~98% | GGUF standard 4bit |
| Q5_K_M | ~24.7 GB | ~99% | Higher accuracy |
| Q6_K | ~28.5 GB | ~99.5% | Near-lossless |
| Q8_0 | ~36.9 GB | ~100% | Lossless |

> MoziAI V3.7 uses the MoziSmartBit intelligent quantization scheme, while maintaining ~99% accuracy, compressing the 35B parameter MoE model to about 15.5 GB, with a compression ratio of ~4.5x, balancing inference quality and deployment threshold, more suitable for local deployment on consumer graphics cards.

## MoziSmartBit Intelligent Quantization Technology

Traditional quantization schemes use uniform precision for all layers, but the self-developed **MoziSmartBit intelligent quantization** by the Chen Yumo team targets the structural characteristics of MoE models, adopting intelligent differentiated quantization strategy, achieving optimal balance between volume and accuracy, model quality is higher than Q4_K_M format, while the volume is only ~15.5 GB, compression ratio ~4.5x.

### Compression Effect

Traditional quantization schemes uniformly compress all parts of the model, which often leads to obvious accuracy loss. MoziSmartBit intelligent quantization uses self-developed intelligent compression strategy, **achieving large volume compression with minimal accuracy loss**:

- **Minimal quantization accuracy loss**: Training gain > quantization loss, after training, MoziAI-35B has better PPL on financial domain text than the bf16 base before training, reducing hallucinations and confusion in similar AI models
- **4.5x model volume compression**: Compressed from ~70 GB FP16 to ~15.5 GB, also significantly smaller than ~22 GB of Q4_K_M, greatly reducing VRAM and storage thresholds
- **Runnable on consumer graphics cards**: The 35B MoE large model that originally required high-end graphics cards can now be smoothly deployed with 20GB~24GB VRAM

### Comparative Advantages

**vs Q4_K_M (~22 GB)**: Volume reduced by about 30% (~15.5 GB), accuracy is **higher** than Q4_K_M, lower VRAM threshold, can be smoothly deployed on mid-range consumer graphics cards (20GB).

**vs original FP16 (~70 GB)**: Volume compressed about 4.5 times, training effective + minimal quantization accuracy loss (training gain > quantization loss), from requiring professional graphics cards (48GB+) to consumer graphics cards (20GB+) can locally run 256K long context.

## Recommended Inference Parameters

Based on local operation configuration (AMD Radeon AI PRO R9700 32GB), the following parameters are recommended:

| Parameter | Recommended Value | Description |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Balance creativity and accuracy |
| top_p | 0.95 | Nucleus sampling threshold |
| top_k | 20 | Truncated sampling |
| repeat_penalty | 1.05 | Repetition penalty |
| presence_penalty | 0 | No presence penalty |
| context_length | 262144 | 256K long context |
| batch_size | 2048 | Batch size |
| ubatch_size | 512 | Micro batch size |
| flash_attention | auto | Automatic Flash Attention |
| kv_cache | q4_0 | KV cache quantization (unified kv-unified) |
| poll | 0 | Idle does not poll GPU, energy saving low latency |
| reasoning | on | Enable reasoning chain (chain-of-thought) |
| reasoning_budget | 400 | Reasoning budget token count |
| reasoning_format | deepseek-legacy | Reasoning format |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | Sampler order |

### Recommended Configuration for Different VRAM

Due to differences in user graphics card configurations, the following are recommended parameters for different VRAM (all for MoziSmartBit version):

| VRAM | Recommended Context Length | KV Cache | Vision Support | Description |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | Supported | Model + vision total ~16.4GB,实测 128K+vision only takes ~19.5GB VRAM |
| 24 GB | 256K full | q4_0 | Perfect support | Vision + 256K long context, only takes ~20.4GB VRAM, ~3.6GB VRAM remaining |
| 32 GB+ | 256K full | q4_0 | Perfect support | Vision + 256K long context, ~10GB VRAM remaining, strongest configuration |

**NVIDIA Graphics Card Reference Table**

| VRAM | Graphics Card Model |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD Graphics Card Reference Table**

| VRAM | Graphics Card Model |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel Graphics Card Reference Table**

| VRAM | Graphics Card Model |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (requires CPU offloading) |

**CPU Shared Memory iGPU Device Reference Table**

| VRAM | Processor Model |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |

> 💡 **Tip**: As long as the VRAM meets the above requirements, it can be used, regardless of brand or model, supports NVIDIA / AMD / Intel independent graphics cards, also supports iGPU/CPU with 128GB unified memory.
>
> 💡 **Tip**: The longer the context, the more VRAM it occupies. If you run out of VRAM (OOM), please gradually decrease the `-c` parameter value. Use the `--fit on` parameter to let llama.cpp automatically adjust the number of layers to fit VRAM.

### Ollama Deployment

```bash
# Create Modelfile
FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf

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

Search for `moziAI-35B` directly in LM Studio or Jan, select the MoziSmartBit quantization version to download.

## Benchmarks

MoziAI-35B-V3.7 is fine-tuned from **Ornith-1.5-35B-A3B** (deepreinforce-ai). MoziAI adds **financial vertical domain optimization** on top of the excellent agentic coding capabilities of the base model, delivering superior performance in financial Q&A, quantitative programming, and tool calling scenarios. General capabilities remain consistent with the Ornith-1.5-35B-A3B base model.

| Benchmark                        | MoziAI-35B-V3.7 (this model) | Qwen3.5-35B | Qwen3.6-35B | Gemma4-31B | Qwen3.5-397B | Description |
| -------------------------------- | ---------------------------- | ----------- | ----------- | ---------- | ------------ | ----------- |
| **Agentic Coding**               |                              |             |             |            |              |             |
| Terminal-Bench 2.1 (Terminus-2)  | 64.2                         | 41.4        | 52.5        | 42.1       | 53.5         |             |
| Terminal-Bench 2.1 (Claude Code) | 62.8                         | 38.9        | 49.2        | -          | 48.6         |             |
| SWE-bench Verified               | 75.6                         | 70          | 73.4        | 52         | 76.4         |             |
| SWE-bench Pro                    | 50.4                         | 44.6        | 49.5        | 35.7       | 51.6         |             |
| SWE-bench Multilingual           | 69.3                         | 60.3        | 67.2        | 51.7       | 69.3         |             |
| NL2Repo                          | 34.6                         | 20.5        | 29.4        | 15.5       | 36.8         |             |
| Claw-eval Avg                    | 69.8                         | 65.4        | 68.7        | 48.5       | 70.7         |             |
| SWE Atlas - QnA                  | 37.1                         | 13.2        | 15.5        | -          | 20.4         |             |
| SWE Atlas - RF                   | 29.7                         | 10.2        | 11.4        | -          | 18.4         |             |
| SWE Atlas - TW                   | 27.8                         | 9.8         | 13.3        | -          | 18.5         |             |
| LiveCodeBench v6                 | -                            | -           | 83.9        | 80.0       | -            |             |
| GPQA Diamond                     | -                            | -           | 87.8        | 84.3       | -            |             |
| AIME 2026 Math                   | -                            | -           | 94.1        | 89.2       | -            |             |

\* **Terminal-Bench 2.1 (Terminus-2)**: Evaluated using the Harbor/Terminus-2 framework with `parser=json`, `temperature=1.0`, `top_p=1.0`, and a 128K context window. Each run uses a 4-hour timeout with 32 CPU cores and 48GB RAM, results averaged over 5 runs.  
\* **Terminal-Bench 2.1 (Claude Code)**: Evaluated using Claude Code 2.1.126 with `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Results averaged over 5 runs.  
\* **SWE-bench Verified, Pro and Multilingual**: Evaluated using OpenHands harness with `temp=1.0`, `top_p=0.95`, 256K context window.  
\* **NL2Repo**: Evaluated with `temperature=1.0`, `top_p=1.0`, 400K context, 48K output.  

> MoziAI-35B fully inherits the excellent agentic coding capabilities from Ornith-1.5-35B-A3B. MoziAI's core differentiation is **deep optimization for financial vertical domains**, significantly outperforming general models in scenarios like financial report analysis, quantitative strategy, risk & compliance, and agent tool calling.

## SEO Keywords

金融AI大模型、AI大模型、本地开源模型、端侧模型、量化编程、MoziSmartBit、智能量化、GGUF量化、MoE模型、本地开源大模型、本地部署、金融AI、工具调用、Agent、llama.cpp、Ollama、GGUF、Uncensored（去审核）、无审查、免审核、自由输出、Q3_K_M、Q4_K_M、Q5_K_M、Q6_K、Q8_0、Ornith-1.5-35B-A3B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、金融垂直领域、开源模型。

## License (Important)

This model uses a **Custom Restrictive License**:

✅ **Allowed**

- Free commercial use: Free to integrate into your commercial products or services
- Copy and distribute: Can be copied, downloaded, and distributed as-is

> See [LICENSE](../LICENSE) for full terms.

## Disclaimer

This model is provided "as is" without any warranties of any kind. Model output is for reference only and does not constitute investment advice. Users bear their own risk of use.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
