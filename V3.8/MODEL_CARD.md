---
language:
- en
- zh
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
- MTP
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.8 - A Compact Yet Powerful Multimodal AI for Free Local Deployment

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Model Overview

MoziAI-35B-V3.8 is a locally deployable open-source financial AI multimodal large language model (vision, tool calling and Uncensored support), developed by the team of Chen Yumo, a leading Chinese finance influencer. Built on the open-source base **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MoE 35B, MIT license), it integrates the team's self-developed: financial data + financial domain capabilities + training methods + dynamic seven-dimensional thinking system + agent LOOP mechanism + Uncensored characteristic + MoziSmartBit hybrid quantization algorithm.

With the self-developed MoziSmartBit smart quantization technology, the 35B-parameter MoE model is compressed to just **15.9 GB** — around 30% smaller than standard Q4_K_M (~22 GB) — achieving an optimal balance between accuracy and size with **~99% FP16 accuracy quality**.

This model significantly lowers the barrier to local deployment, is licensed for **free commercial use**, runs on consumer-grade GPUs with **zero cloud token cost**, enables 7×24 token freedom, and ensures local data privacy and security.

Supports llama.cpp, Ollama, LM Studio, Jan and other mainstream inference frameworks, and is compatible with OpenClaw / Hermes / Cursor / Claude Code / Codex agent platforms.

**Release Date: 2026-09-01** | **Version: V3.8**

## Key Features

- **Financial vertical focus**: deep optimization for financial Q&A, quantitative programming and tool calling
- **Dynamic 7-Dimensional Thinking**: moziAI-Think marker with Level 0/1/2 structured thinking by task complexity
- **Agent LOOP mechanism**: complex tasks auto-iterate "execute+assess → adjust+verify" with self-validation
- **MoziSmartBit smart quantization**: 35B MoE compressed to 15.9 GB (4.5x ratio), ~99% accuracy
- **Uncensored**: no content restrictions, free output, complete information, local privacy
- **256K long context**: handles huge documents and multi-turn agent tasks
- **Multimodal vision**: understands screenshots locally
- **Multilingual**: 201 languages and dialects, optimized Chinese
- **Inference acceleration**: ngram speculative decoding — 140+ tok/s on R9700 GPU / 70+ tok/s on MAX+395 iGPU (measured)

## Technical Specifications

| Item | Specification |
| --- | --- |
| Base Model | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT) |
| Parameters | 35B MoE, 256 routing experts + 1 shared expert, 8 experts active per token |
| Quantization | MoziSmartBit + GGUF standard |
| Context Length | 256K (262,144 tokens) |
| Model Size | ~15.9 GB |
| Min VRAM | 20GB+ deployable (CPU offload); 24GB+ smooth long context; 32GB+ full 256K + vision |
| Inference Speed | R9700 **140+ tok/s** / MAX+395 **70+ tok/s** (speculative decoding) |

## Downloads

| Platform | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP/tree/main) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP/tree/master) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP/tree/main) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> ⚠️ **3-file tip**: download all files in the `V3.8/` directory — main model (.gguf), vision projector (mmproj), chat template (.jinja) — into the same folder for 100% best inference.

## Quick Start (llama.cpp)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 --host 0.0.0.0 --port 8080
```

Open `http://localhost:8080` to start chatting. Full recommended parameters and launch commands: see `V3.8/README.en.md`.

## Benchmark Snapshot (Coding / Reasoning / Agentic, same-generation measurements)

| Domain | Highlights |
| --- | --- |
| Coding | SWE-bench Verified **79** / SWE-bench Pro **59.6** / Terminal-Bench 2.1 **67.8-68.5** (clearly above Ornith-1.0 and Qwen3.6-35B-A3B) |
| Reasoning | GPQA Diamond **89.2** / HLE (tools) **33.4** |
| Agentic | MCP-Atlas **70.2** / ClawEval **72.5** / Toolathlon-Verified **48.7** |

> In the financial vertical (earnings interpretation, quant strategy, risk & compliance, agent tool calling) it significantly outperforms same-size general models. Full 18-item comparison table: section 14 of `V3.8/README.en.md`.

## Uncensored

No content moderation restrictions, free output, complete information, local privacy. Suitable for academic research, deep analysis and free discussion. This is a locally deployed model — output is fully controlled by the user; the model bears no content-moderation responsibility.

## License

**Custom restrictive license**: ✅ free commercial use / ❌ no secondary development, resale or sub-licensing / 📋 retain the original copyright notice and credit moziAI-35B. Model output is for reference only and does not constitute investment advice.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo) · **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen) · **E-mail**: 263515@qq.com

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.