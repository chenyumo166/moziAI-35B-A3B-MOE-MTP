---
language:
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

# moziAI-35B-V3.6-A3B-MOE-MTP-Uncensored - Free Locally Deployable Small Yet Powerful Multimodal AI Model

Language / Language Selection
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | **English** | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Model Introduction

MoziAI-35B-A3B-MOE is a local open-source financial AI multimodal LLM (supports vision and tool calling) developed by Chinese finance influencer Chen Yumo's team. moziAI-35B is built on the open-source base model Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MIT licensed), incorporating the Chen Yumo team's self-developed: (financial data + financial domain capabilities + training methods + Seven-Dimensional Thinking framework + agent LOOP mechanism + hybrid quantization algorithm MoziSmartBit). Through the self-developed MoziSmartBit intelligent quantization technology, the 35B-parameter MoE model is compressed to approximately 15.5 GB, which is 6.5G (about 30%) smaller than conventional Q4_K_M quantization models of about 22+GB; achieving the optimal balance between precision and size, delivering nearly lossless ≈99% of FP16 precision quality.

The philosophy of our development team is to bring powerful local AI large model agents to every household and small-to-medium enterprise, eliminating the need for expensive AI hardware costs or cloud API fees. Through our proprietary **MoziSmartBit intelligent quantization** technology, the 35-billion-parameter MoE model is compressed to approximately **15.5 GB**, achieving an optimal balance between model accuracy and size while delivering nearly 99% of FP16 precision quality. This model has 35 billion parameters but uses MoE sparse expert technology, activating only 3 billion parameters per token and supporting MTP speculative decoding for accelerated inference. In practice, it can be deployed locally for free on a consumer-grade graphics card with 20GB of VRAM, achieving inference speeds of 140+ tokens/s — faster than many cloud-based paid AI models.

In addition to retaining the capabilities of a general-purpose AI model, this model focuses on optimizing key AI capabilities such as financial vertical domain applications, financial Q&A, quantitative programming, general programming, tool calling, and the success rate of complex long-context tasks at 256K. It can be deployed for free on local consumer-grade graphics cards, saving substantial cloud token costs, enabling 24/7 token freedom, and ensuring local data privacy and security.

**Release Date:** 2026-08-20 | **Version:** V3.6

## Model Download

Due to the large model file size (~15.5 GB), model weights are hosted on multiple community platforms:

| Platform | URL |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio Users**: You can directly search for `moziAI` in [LM Studio](https://lmstudio.ai) and download with one click, no manual file download required.
> 💡 **Download Tip**: Click the link above to enter the HuggingFace repository, and download all files in the **V3.6** directory from the **"Files and versions"** tab (main model, vision projection, chat template). Ensure all three files are placed in the same directory.

### ⚠️ Important: Vision Capability Requires Additional mmproj File

This model supports multimodal vision. The vision projection file (mmproj) is included in the version directory:

- **Vision File**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (approx. 903 MB, BF16 precision)
- **Placement**: Place in the same version directory as the GGUF model file
- **Loading Method**: Load via the `--mmproj` parameter when starting llama-server

> Without loading the vision file, image understanding capability will be lost, and only pure text dialogue capability will remain.

### ⚠️ Important: Chat Template File Must Be Loaded

This model uses a custom chat template. **Failing to load it will cause dialogue format errors, broken reasoning chains, and significantly reduced response quality**. The chat template file is included in the version directory:

- **Template File**: `moziAI-V3.6-35B-chat-template.jinja` (approx. 5 KB, jinja format)
- **Placement**: Place in the same version directory as the GGUF model file
- **Loading Method**: Load via the `--chat-template-file` parameter when starting llama-server

> Without loading the chat template, the model may not correctly recognize system prompts, user messages, and thinking blocks, leading to chaotic output formatting or degraded reasoning capabilities.

### llama.cpp Startup Command (Recommended Config for 20G+ Graphics Card with 256K Context)

> Note: If your VRAM is below 20G, reduce the context setting value of 262144 in the `-c 262144` parameter.

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --spec-default \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

## Quick Start

### 1. Download Model Files

Download all files in the V3.6 directory from HuggingFace / ModelScope to your local machine:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Main model (required)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision projection (optional, download for vision capability)
└── moziAI-V3.6-35B-chat-template.jinja                  # Chat template (required! Not loading will cause dialogue format errors)
```

> ⚠️ **The chat template is a required file**, not optional. This model has a custom dialogue format (including reasoning chains / thinking blocks). Missing the template will cause chaotic model output formatting and failed reasoning capabilities. Please be sure to download it and load it at startup.

### 2. Start the Inference Service

For the complete recommended configuration startup command, please refer to the [llama.cpp Startup Command](#llamacpp-startup-command) section below.

Minimal startup (core parameters only):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Add `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` when vision capability is needed.

### 3. Start Using

Open `http://localhost:8080` in your browser to start chatting.

### Directory Structure

```
moziAI-35B/
├── README.md              # English documentation
├── README.zh.md           # Chinese documentation
├── LICENSE                # License
├── V3.6/                  # V3.6 version (self-contained)
│   ├── RELEASE_NOTES.md                       # Version release notes
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Main model
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Vision projection
│   └── moziAI-V3.6-35B-chat-template.jinja   # Chat template
```

## Model Features

- **MoziSmartBit Intelligent Quantization**: Proprietary intelligent quantization technology, optimal balance between precision and size, model compressed to approximately **15.5 GB** with near-zero quality loss
- **Complex Long-Task Capability**: Trained with an intelligent loop processing mechanism that allows the model agent to automatically plan tasks, handle bottlenecks, and engage in self-reflection, enabling automatic execution and self-adjustment of complex tasks, eliminating the need for users to continuously optimize prompts
- **Small Model, Big Capability**: In executing complex tasks, comprehensive capabilities outperform models within the same 35-billion-parameter class, and even outperform some models with several times more parameters
- **Speed Advantage of MOE+MTP**: Although the model has 35 billion parameters in total, only 8+1 experts are actually activated per token, totaling 3 billion parameters, resulting in faster inference speeds. Ideal for local deployment on consumer-grade graphics cards with 20GB~24GB VRAM, enjoying 140+ tokens/s inference speed
- **Deep Financial Vertical Focus**: Deeply enhanced financial Q&A, quantitative programming, and tool calling capabilities
- **Consumer-Grade Deployment**: Can be deployed locally on consumer-grade graphics cards with 20GB~24GB+ VRAM, supporting up to 256K long context inference
- **Multilingual Support**: Supports 201 languages and dialects, with specially optimized Chinese capability, while also supporting major languages including English, Japanese, Korean, German, French, Portuguese, and more
- **General Programming Capability**: Supports full-stack development, code debugging, architecture design, and script writing, covering mainstream languages such as Python/JS/TS/Go/Rust
- **Article Writing Capability**: Supports high-quality writing in multiple genres, including research reports, analytical articles, technical documentation, and creative content
- **Vision Understanding**: Load the vision file with the inference framework to support multimodal vision. You can take local screenshots and paste them into the chat window, and the model can understand the information in the images
- **Uncensored Free Output**: No content review restrictions, free to discuss any topic, not constrained by safety policies
- **Enhanced Reasoning Logic**: Trained with reasoning logic (chain of thought) to further improve reasoning quality
- **Multi-Framework Support**: Compatible with mainstream inference frameworks such as llama.cpp, Ollama, LM Studio, and Jan
- **Multi-Agent Platform Support**: Deeply adapted to mainstream domestic and international AI IDEs and Agent frameworks such as OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, and Codex, with native support for tool calling and multi-round task orchestration, ready to use out of the box

## Uncensored Advantages

This model inherits the Uncensored characteristics of the Ornith-1.0-35B-A3B base model, with the following advantages:

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Advantage</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>No Censorship Restrictions</td>
<td>Will not refuse any topic, including sensitive and controversial content</td>
</tr>
<tr>
<td>Free Output</td>
<td>Not constrained by safety policies, can generate any type of response</td>
</tr>
<tr>
<td>Complete Information</td>
<td>Provides unfiltered complete information, suitable for research and analysis scenarios</td>
</tr>
<tr>
<td>Local & Private</td>
<td>Local deployment means data is completely private, not subject to cloud review</td>
</tr>
</tbody>
</table>

> **Applicable Scenarios**: Free commercial use, academic research, in-depth analysis, free discussion, unrestricted AI dialogue
> **Note**: This model is for local deployment; output content is entirely controlled by the user, and we assume no responsibility for content review.

## Core Capabilities

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Capability Domain</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Market Analysis</td>
<td>Macro/microeconomic interpretation, A-share/HK stock/US stock/commodities/cryptocurrency market trends and logical analysis</td>
</tr>
<tr>
<td>Finance & Research Reports</td>
<td>Financial report key indicator interpretation, research report summary extraction, valuation and earnings forecast assistance</td>
</tr>
<tr>
<td>Risk Control & Compliance</td>
<td>Product risk assessment, investment advice compliance reminders, financial regulatory policy interpretation</td>
</tr>
<tr>
<td>Quantitative & Strategies</td>
<td>Quantitative strategy design, Pyramid (PEL) quantitative analysis, backtesting logic, factor construction, and tool calling</td>
</tr>
<tr>
<td>Tool Calling</td>
<td>Can integrate with real-time market data, databases, research report retrieval, and other financial data</td>
</tr>
</tbody>
</table>

## Technical Specifications

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Item</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Base Model</td>
<td>Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MIT license)</td>
</tr>
<tr>
<td>Parameter Scale</td>
<td>35 billion (35B) MoE architecture, 256 routing experts + 1 shared expert, 8 experts activated per token</td>
</tr>
<tr>
<td>Quantization Method</td>
<td>Proprietary MoziSmartBit intelligent quantization algorithm + GGUF standard format</td>
</tr>
<tr>
<td>Context Length</td>
<td>256K (262,144 tokens)</td>
</tr>
<tr>
<td>Model Size</td>
<td>~15.5 GB (MoziSmartBit Uncensored version)</td>
</tr>
<tr>
<td>Minimum VRAM Requirement</td>
<td>Consumer-grade graphics card with 20GB+ VRAM (e.g., RTX 3060 12G requires CPU offloading, RTX 4060 Ti 16G, etc.), recommended 24 GB (including vision + long context)</td>
</tr>
<tr>
<td>Inference Framework</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>Inference Speed</td>
<td>Through algorithm optimization, AMD Radeon AI PRO R9700 graphics card can reach 140+ tokens/s / AMD Ryzen AI Max+ 395 integrated GPU can reach 70+ tokens/s, enabling free local inference output</td>
</tr>
<tr>
<td>Development Team</td>
<td>Chen Yumo Team</td>
</tr>
</tbody>
</table>

## Quantization Formats and Model Size Comparison

| Quantization Format | Model Size | Precision Retention | Description |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (Original) | ~70 GB | 100% | Original 16-bit precision |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **This model uses proprietary intelligent quantization** |
| Q4_K_M | ~22 GB | ~98% | GGUF standard 4-bit |
| Q5_K_M | ~24.7 GB | ~99% | Higher precision |
| Q6_K | ~28.5 GB | ~99.5% | Near lossless |
| Q8_0 | ~36.9 GB | ~100% | Lossless |
> MoziAI V3.6 uses MoziSmartBit intelligent quantization, maintaining ~99% precision while compressing the 35-billion-parameter MoE model to approximately 15.5 GB, with a compression ratio of ~4.5x. This balances inference quality and deployment threshold, making it more suitable for local deployment on consumer-grade graphics cards.

## MoziSmartBit Intelligent Quantization Technology

Traditional quantization schemes use uniform precision across all layers. However, Chen Yumo's team's proprietary **MoziSmartBit intelligent quantization** targets the structural characteristics of MoE models, adopting an intelligent differentiated quantization strategy to achieve the optimal balance between size and precision. Model quality is higher than the Q4_K_M format, while the size is only ~15.5 GB, with a compression ratio of ~4.5x.

### Compression Effect

Traditional quantization schemes uniformly compress all parts of the model, often resulting in significant precision loss. MoziSmartBit intelligent quantization uses a proprietary intelligent compression strategy, **achieving substantial size compression with minimal precision loss**:

- **Minimal Quantization Precision Loss**: Training gain > quantization loss. The trained MoziAI-35B has better PPL on financial domain text than the pre-training bf16 base model, reducing hallucination and perplexity of similar AI models
- **Model Size Compressed 4.5x**: Compressed from ~70 GB in FP16 to ~15.5 GB, also significantly smaller than Q4_K_M's ~22 GB, greatly reducing VRAM and storage thresholds
- **Runnable on Consumer-Grade Graphics Cards**: The 35B MoE large model that originally required high-end graphics cards can now be smoothly deployed with 20GB~24GB VRAM

### Comparative Advantages

**vs Q4_K_M (~22 GB)**: Size reduced by approximately 30% (~15.5 GB), precision is **higher** than Q4_K_M, lower VRAM threshold, and mid-range consumer-grade graphics cards (20GB) can run it smoothly.

**vs Original FP16 (~70 GB)**: Size compressed by approximately 4.5x, effective training + minimal quantization precision loss (training gain > quantization loss), reduced from requiring professional-grade graphics cards (48GB+) to consumer-grade graphics cards for local 256K long context operation.

## Recommended Inference Parameters

Based on local running configuration (AMD Radeon AI PRO R9700 32GB), the recommended parameters are as follows:

| Parameter | Recommended Value | Description |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Balance creativity and accuracy |
| top_p | 0.95 | Nucleus sampling threshold |
| top_k | 20 | Truncated sampling |
| repeat_penalty | 1.05 | Repetition penalty |
| presence_penalty | 0 | No presence penalty |
| context_length | 262144 | 256K long context |
| batch_size | 2048 | Batch size |
| ubatch_size | 512 | Micro-batch size |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | KV cache quantization (unified kv-unified) |
| poll | 0 | No GPU polling when idle, energy-saving and low latency |
| reasoning | on | Enable reasoning chain (chain of thought) |
| reasoning_budget | 400 | Reasoning budget token count |
| reasoning_format | deepseek-legacy | Reasoning format |
| samplers | top_k;top_p;temperature;typ_p | Sampler order |
### Recommendations for Different VRAM Configurations

Due to significant variations in user graphics card configurations, the following are recommended parameters for different VRAM amounts (all for the MoziSmartBit version):

| VRAM | Recommended Context Length | KV Cache | Vision Support | Description |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | Supported | Model + vision total ~16.4GB, measured 128K+vision uses only ~19.5GB VRAM |
| 24 GB | 256K Full | q4_0 | Fully Supported | Vision + 256K long context uses only ~20.4GB VRAM, with ~3.6GB VRAM remaining |
| 32 GB+ | 256K Full | q4_0 | Fully Supported | Vision + 256K long context, ample ~10GB VRAM remaining, strongest configuration |
**NVIDIA Graphics Card Reference Table**

| VRAM | Graphics Card Models |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD Graphics Card Reference Table**

| VRAM | Graphics Card Models |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel Graphics Card Reference Table**

| VRAM | Graphics Card Models |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (requires CPU offloading) |
**CPU Shared Memory Integrated GPU Device Reference Table**

| VRAM | Processor Models |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |
> 💡 **Tip**: As long as the VRAM meets the above requirements, you can use it regardless of brand or model. It supports NVIDIA / AMD / Intel discrete graphics cards, as well as integrated GPUs/CPUs with 128GB unified memory.
>
> 💡 **Tip**: Longer context uses more VRAM. If you encounter out-of-memory (OOM) issues, please gradually reduce the `-c` parameter value. Using the `--fit on` parameter allows llama.cpp to automatically adjust the number of layers to fit your VRAM.

### Ollama Deployment

```bash
# Create Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

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

Simply search for `moziAI-35B` in LM Studio or Jan, and select the quantization version to download.

## Benchmark Evaluation

moziAI-35B-V3.6 is fine-tuned based on the **Ornith-1.0-35B** (deepreinforce-ai) base model. Building on the base model's excellent agent coding capabilities, MoziAI adds **deep optimization for the financial vertical domain**, performing better in scenarios such as financial Q&A, quantitative programming, and tool calling. General capabilities remain consistent with the Ornith-1.0-35B base model.

| Benchmark | moziAI-35B-V3.6 | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
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
**Terminal-Bench 2.1 (Terminus-2)**: Evaluated using the Harbor/Terminus-2 framework, configured with `parser=json`, `temperature=1.0`, `top_p=1.0`, 128K context window. Each run has a 4-hour timeout, 32 cores 48GB RAM, results are the average of 5 runs.
**Terminal-Bench 2.1 (Claude Code)**: Evaluated using Claude Code 2.1.126, configured with `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Results are the average of 5 runs.
**SWE-bench Verified, Pro and Multilingual**: Evaluated using the OpenHands framework, configured with `temp=1.0`, `top_p=0.95`, 256K context window.
**NL2Repo**: Configured with `temperature=1.0`, `top_p=1.0`, 400K context, 48K output.

> MoziAI-35B fully inherits the excellent agent coding capabilities of Ornith-1.0-35B. MoziAI's core differentiation lies in **deep optimization for the financial vertical domain**, significantly outperforming general-purpose models in scenarios such as financial report analysis, quantitative strategies, risk control compliance, and agent tool calling.

## SEO Keywords

Financial AI large model, AI large model, local open-source model, on-device model, quantitative programming, MoziSmartBit, intelligent quantization, GGUF quantization, MoE model, local open-source large model, local deployment, financial AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, no censorship, free output, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B, financial vertical domain, open-source model.

## License (Important)

This model uses a **custom restrictive license**, with the following key terms:

✅ **Allowed**

- Free commercial use: Can be freely integrated into your commercial products or services
- Copying and distribution: Can be copied, downloaded, and distributed as-is

For detailed license terms, please refer to the [LICENSE](../LICENSE) file.

## Disclaimer

This model is provided "as-is" without any form of warranty. Model output is for reference only and does not constitute investment advice. Users assume all risks associated with use.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.