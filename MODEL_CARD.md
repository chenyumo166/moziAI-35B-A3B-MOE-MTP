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

MoziAI-35B-V3.8 is a locally deployable open-source financial AI multimodal large language model (vision, tool calling and Uncensored support), developed by the team of Chen Yumo, a leading Chinese finance influencer. Built on the open-source base **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architecture, MoE 35B, MIT/Apache-2.0 license), it integrates the team's self-developed: financial data + financial domain capabilities + training methods + dynamic seven-dimensional thinking system + agent LOOP mechanism + Uncensored characteristic + MoziSmartBit hybrid quantization algorithm.

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
| Base Model | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT/Apache-2.0) |
| Parameters | 35B MoE, 256 routing experts + 1 shared expert, 8 experts active per token |
| Quantization | MoziSmartBit + GGUF standard |
| Context Length | 256K (262,144 tokens) |
| Model Size | ~15.9 GB |
| Min VRAM | 20GB+ deployable (CPU offload); 24GB+ smooth long context; 32GB+ full 256K + vision |
| Inference Speed | R9700 **140+ tok/s** / MAX+395 **70+ tok/s** (speculative decoding) |

## Downloads

| Platform | URL |
| --- | --- |
| HuggingFace | [https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| GitCode | [https://ai.gitcode.com/chenyumo166/moziAI-35B-A3B-MOE-MTP](https://ai.gitcode.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |
| LM Studio | Search `moziAI` in LM Studio → Download |

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

**Layered licensing**: ✅ free commercial use, copying and distribution / ❌ secondary development, resale, or sub-licensing **of MoziAI's original additions only** (upstream components retain their original Apache 2.0 / MIT licenses) / 📋 retain all upstream copyright notices ([`NOTICE`](NOTICE)) and this license. See [`LICENSE`](LICENSE), [`LICENSE-APACHE`](LICENSE-APACHE), [`NOTICE`](NOTICE), and [`MODIFICATIONS.md`](MODIFICATIONS.md). Model output is for reference only and does not constitute investment advice.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo) · **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen) · **E-mail**: 263515@qq.com

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.

---
<!-- UPSTREAM-LICENSE-NOTICE:BEGIN -->
## 上游许可与归属声明 / Upstream License & Attribution Notice

本模型是**组合作品**，采用分层许可。This model is a **combined work** distributed under layered licensing.

| 组成部分 / Component | 许可 / License |
|---|---|
| Ornith 自研增量 / Ornith increment | 以上游仓库实际随附的许可文件为准 / per the upstream repository |
| 继承的上游 Qwen 组件 / Inherited Qwen components | **Apache License 2.0** |
| MoziAI 原创增量 / MoziAI additions | **MoziAI Custom Restricted License** |

- 继承的 Qwen 组件在任何时候均持续受 **Apache License 2.0** 约束；本仓库的限制性许可、以及适用于 Ornith 增量的宽松许可，均不构成对该等组件的重新授权、再许可或变更。许可全文见 [`LICENSE-APACHE`](LICENSE-APACHE)。
  The inherited Qwen components remain governed by the **Apache License, Version 2.0** at all times. Neither this repository's restrictive license nor any permissive license applied to the Ornith increment relicenses, sublicenses or otherwise modifies them. Full text: [`LICENSE-APACHE`](LICENSE-APACHE).
- 上游版权、商标与归属声明见 [`NOTICE`](NOTICE)。
  Upstream copyright, trademark and attribution notices: [`NOTICE`](NOTICE).
- 本团队对上游作品所做的修改见 [`MODIFICATIONS.md`](MODIFICATIONS.md)。
  Modifications made by this team to the upstream work: [`MODIFICATIONS.md`](MODIFICATIONS.md).
- 本仓库的限制性条款**仅适用于 MoziAI 原创增量部分**。若与上游许可冲突，就上游组件而言以上游许可为准（见 `LICENSE` 第 11 条）。
  This repository's restrictive terms apply **only to MoziAI's original additions**. Where they conflict with an upstream license, the upstream license prevails for the upstream components (see `LICENSE`, Section 11).
- "Qwen"、"通义千问" 是阿里巴巴集团的商标。本项目与阿里巴巴集团、Qwen 团队及 Ornith 作者无隶属、赞助或背书关系。
  "Qwen" and "Tongyi Qianwen" are trademarks of Alibaba Group. This project is not affiliated with, endorsed by or sponsored by Alibaba Group, the Qwen team or the Ornith authors.
<!-- UPSTREAM-LICENSE-NOTICE:END -->
