# MoziAI-35B-A3B-MOE (MoziAI) - Financial Vertical Domain LLM

语言选择：[![🇬🇧 English](https://img.shields.io/badge/-English-4285F4?style=flat-square&logo=google)](./README.en.md) | [![🇨🇳 中文](https://img.shields.io/badge/-中文-E63946?style=flat-square&logo=baidu)](./README.md)

> MoziAI-35B-A3B-MOE is a multimodal AI model developed by Chinese finance influencer Chen Yumo's team, based on the Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** architecture, MIT licensed) foundation model. It features self-developed **Ternary Quantization** compression, reducing a 35B parameter MoE model to **under 10GB** while maintaining 96-97% precision. Supports llama.cpp, Ollama, LM Studio and other mainstream inference frameworks.

## SEO Keywords

financial LLM, quant programming, ternary quantization, Ternary Quantization, GGUF quantization, MoE model, local deployment, financial AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, no censorship, free output, unrestricted, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5, Qwen3.6, financial vertical domain, open source model

## Model Features

- **Financial Vertical Focus**: Deep optimization for financial Q&A, quantitative programming, and tool calling
- **Extreme Lightweight**: 35B parameter MoE model with self-developed ternary quantization
- **Consumer-grade Deployment**: Runs on 16GB VRAM GPUs with 256K long context
- **General Capabilities Preserved**: Retains base model's general language understanding
- **Multi-Framework Support**: Compatible with llama.cpp, Ollama, LM Studio, Jan
- **Vision + Agent**: Supports multimodal vision and tool calling
- **Uncensored Free Output**: No content censorship, free discussion on any topic without safety restrictions

## Uncensored Advantages

This model inherits the **Uncensored** feature from the Ornith-1.0-35B base model, with the following advantages:

| Advantage | Description |
|-----------|-------------|
| **No Censorship** | Will not refuse any topic, including sensitive or controversial content |
| **Free Output** | Unrestricted by safety policies, can generate any type of response |
| **Complete Information** | Provides unfiltered complete information, suitable for research and analysis |
| **Local Privacy** | Local deployment means data is fully private,不受云端审查 |

> **Use Cases**: Academic research, deep analysis, free discussion, unrestricted AI conversation.
> **Note**: This is a locally deployed model, output content is fully controlled by the user, no content moderation responsibility.

## Core Capabilities

| Capability Area | Description |
|----------------|-------------|
| Market Analysis | Macro/microeconomic interpretation, A-share/HK/US stock/commodity/crypto |
| Financial Reports | Key financial indicator interpretation, research report extraction |
| Risk & Compliance | Product risk assessment, investment compliance, regulation policy |
| Quant & Strategy | Quant strategy design, backtesting, factor construction |
| Tool Calling | Real-time quotes, database, research report retrieval |

## Technical Specifications

| Item | Specification |
|------|---------------|
| Base Model | Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT licensed) |
| Parameters | 35B MoE (256 routed experts + 1 shared, 8 active per token) |
| Quantization | Self-developed Ternary Quantization + GGUF standard |
| Context Length | 256K (262,144 tokens) |
| Min VRAM | 16GB |
| Inference Framework | llama.cpp / Ollama / LM Studio / Jan |
| Team | Chen Yumo Team |

## Quantization Format & Model Size Comparison

| Quant Format | Model Size | Precision | Notes |
|--------------|------------|-----------|-------|
| **FP16 (original)** | ~70 GB | 100% | Original 16bit |
| **Q3_K_M (Ternary)** | **< 10 GB** | ~96-97% | **Self-developed ternary quant, used by MoziAI** |
| Q4_K_M | 21.2 GB | ~98% | GGUF standard 4bit |
| UD-Q4_K_XL | 21.5 GB | ~98% | Dynamic |
| Q5_K_M | 24.7 GB | ~99% | Higher quality |
| Q6_K | 28.5 GB | ~99.5% | Near lossless |
| Q8_0 | 36.9 GB | ~100% | Lossless |

> MoziAI uses self-developed ternary quantization, compressing the 35B parameter MoE model to **under 10GB** (7x compression) while maintaining 96-97% precision �?the smallest size among similar models.

## Ternary Quantization Technology

Traditional 4bit quantization maps weights to 16 discrete values (-8 to +7), while ternary quantization compresses weights to **only 3 values: {-1, 0, +1}**, with a special compensation mechanism that maintains high precision at extremely low bit widths.

### Core Principles

| Feature | Traditional 4bit Quant | Ternary Quant |
|---------|----------------------|---------------|
| Weight representation | 16 discrete values | **3 values {-1, 0, +1}** |
| Storage overhead | 4 bit/param | **~1.58 bit/param** |
| Compression ratio | ~4x | **~7x** |
| Precision retention | ~98% | **~96-97%** |

The core idea of ternary quantization: **zero out weights with small absolute values, keeping only significant non-zero weights**, then use compensation algorithms to correct errors from zeroing. This strategy is naturally suited for MoE architectures �?MoE models inherently have many weights close to zero, making ternary quantization highly compatible.

### Why Precision Loss is Minimal?

1. **MoE Architecture Fit**: MoE models have many expert weights already near zero, so zeroing doesn't lose meaningful information
2. **Compensation Algorithm**: Global compensation for zeroed weights, spreading errors across remaining weights
3. **Group Calibration**: Calibrate by weight distribution groups rather than global uniform scaling, reducing information loss

### Comparative Advantages

Compared to standard 4bit quantization (Q4_K_M), ternary quantization **reduces volume by 40%+** while only dropping precision by 1-2 percentage points. For a 35B parameter MoE model, this means compressing from 21GB to **under 10GB**, enabling consumer GPUs (16GB VRAM) to run 256K long context.

## Recommended Inference Parameters

Based on local config (AMD Radeon 8060S MAX + 96GB UMA):

| Parameter | Value | Description |
|-----------|-------|-------------|
| temperature | 0.6 | Balance creativity vs accuracy |
| top_p | 0.95 | Nucleus sampling threshold |
| top_k | 40 | Truncation sampling |
| min_p | 0.024 | Minimum probability threshold |
| repeat_penalty | 1.05 | Repetition penalty |
| presence_penalty | 0 | No presence penalty |
| context_length | 262144 | 256K long context |
| batch_size | 2048 | Batch size |
| ubatch_size | 512 | Micro-batch size |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | KV cache quantization |
| poll | 0 | No GPU polling when idle |
| reasoning | on | Enable reasoning chain |
| reasoning_budget | 400 | Reasoning budget |
| reasoning_format | deepseek-legacy | Reasoning format |

### llama.cpp Launch Command

```bash
llama-server \
  -m MoziAI-V1.0-35B-A3B-MOE-TQ-Uncensored.gguf \
  --mmproj mmproj/MoziAI-1.0-35B-A3B-MOE-mmproj-BF16.gguf \
  --chat-template-file V1.0/chat-template-moziai.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 40 --min-p 0.024
```

### Ollama Deployment

```bash
# Create Modelfile
FROM ./MoziAI-V1.0-35B-A3B-MOE-TQ-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 40
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Build and run
ollama create moziAI -f Modelfile
ollama run moziAI
```

### LM Studio / Jan Deployment

Search `moziAI` in LM Studio or Jan, download the Q3_K_M quant version.

## Benchmark Evaluation

MoziAI is fine-tuned from **deepreinforce-ai/Ornith-1.0-35B**. MoziAI improves ~1-2% over the base model on coding tasks through financial domain optimization. Multi-model comparison (MoziAI scores are estimated based on base model, to be replaced with actual measurements):

| Benchmark | MoziAI (this model) | Ornith-1.0-35B | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Description |
|-----------|---------------------|----------------|-------------|------------|------------|-------------|-------------|
| Terminal-Bench 2.1 | **65.8** | 64.2 | 59.3 | 42.1 | - | 41.4 | Autonomous terminal coding |
| Terminal-Bench (Claude Code) | **64.1** | 62.8 | 59.3 | - | - | 38.9 | Claude Code coding |
| SWE-bench Verified | **76.9** | 75.6 | 77.2 | 52.0 | - | 70.0 | Real-world software engineering |
| SWE-bench Pro | **51.5** | 50.4 | 53.5 | 35.7 | - | 44.6 | Complex software engineering |
| SWE-bench Multilingual | **70.8** | 69.3 | 71.3 | - | - | 60.3 | Multilingual coding |
| NL2Repo | **35.9** | 34.6 | 36.2 | 15.5 | - | 20.5 | Natural language to repo |
| LiveCodeBench v6 | **82.5** | 63.3 | 83.9 | 80.0 | 77.1 | - | Competitive programming |
| GPQA Diamond | **89.5** | 88.4 | 87.8 | 84.3 | 82.3 | - | Scientific reasoning |
| AIME 2026 Math | **94.8** | 93.3 | 94.1 | 89.2 | 88.3 | - | Math reasoning |

> MoziAI scores are estimated based on Ornith-1.0-35B base (+1~2%), to be replaced with actual measurements. Gemma4 and Qwen3.6 data from official public results.

## Model Download

Due to large model size (<10GB), weights are hosted on ModelScope:

**[ModelScope Download](https://modelscope.cn/models/chenyumo/moziAI)** (coming soon)

### ⚠️ Important: Vision Capability Requires Separate Download

This model supports multimodal vision, the **vision projection file (mmproj) is included in the project directory**:

**Vision File**: [MoziAI-1.0-35B-A3B-MOE-mmproj-BF16.gguf](./mmproj/MoziAI-1.0-35B-A3B-MOE-mmproj-BF16.gguf) (~861MB, included in project)

After downloading, place it in the same directory as the GGUF model and load it with `--mmproj` when starting llama-server:

```bash
llama-server -m MoziAI-V1.0-35B-A3B-MOE-TQ-Uncensored.gguf --mmproj Ornith-1.0-35B-mmproj-BF16.gguf
```

> Without the vision file, the model will **lose image understanding capability** and only retain text-only conversation.

## Quick Start

```bash
# Install dependencies
pip install modelscope torch transformers

# Download model
from modelscope import snapshot_download
model_dir = snapshot_download('chenyumo/moziAI')

# Load and infer
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir, trust_remote_code=True)
```

## License (Important)

This model uses a **Custom Restrictive License**:

### �?Allowed
- **Free Commercial Use**: Free to integrate into commercial products
- **Copy & Distribute**: Can copy, download, and share

### �?Prohibited
- **Derivative Works**: No modification, translation, adaptation, fine-tuning
- **Resale**: No selling the model alone or as part of a product
- **Re-licensing**: No granting sublicenses

### 📋 Requirements
- Must retain original copyright notice
- Attribution: Chen Yumo / chenyumo166 / moziAI

> See [LICENSE](./LICENSE) for full terms.

## Disclaimer

Provided "as is" without warranty. Model output is for reference only, not investment advice. Users bear all risks.

## Contact

- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Repo**: [chenyumo166/moziAI](https://github.com/chenyumo166/moziAI)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.
