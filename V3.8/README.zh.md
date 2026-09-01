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
- MTP
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.8 — 可免费本地部署的小而强的多模态 AI 模型

[English](README.en.md) | 简体中文 | [繁体中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

**发布日期：2026-09-01** · **版本：V3.8**

---

## 📑 目录

- [1. 模型概述](#1-模型概述)
- [2. 模型特色](#2-模型特色) — 动态七维思考 / LOOP / MoziSmartBit / 金融聚焦
- [3. 版本升级说明](#3-版本升级说明)
- [4. 核心能力](#4-核心能力)
- [5. 技术规格](#5-技术规格)
- [6. ⚡ 快速开始](#6--快速开始3-个文件--100-激活最佳推理能力) — **三件套下载**
- [7. 模型下载](#7-模型下载)
- [8. 启动命令](#8-启动命令)
- [9. 推荐推理参数](#9-推荐推理参数)
- [10. 量化格式对比](#10-量化格式对比)
- [11. 推测解码加速](#11-推测解码加速重要特性)
- [12. 显存配置](#12-显存配置推荐)
- [13. 部署方式](#13-部署方式)
- [14. 基准评测](#14-基准评测)
- [15. 去审核（Uncensored）优化](#15-去审核uncensored优化)
- [16. 许可证](#16-许可证)
- [17. 联系方式](#17-联系方式)

---

## 1. 模型概述

MoziAI-35B-V3.8 是由中国财经大V陈雨墨团队开发的本地开源多模态AI大模型，基于开源底座 **Ornith-1.5-35B-A3B**（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架构，MoE 35B，MIT 许可），结合团队自主研发的金融数据 + 金融领域能力 + 动态七维思考体系 + 智能体LOOP反思迭代机制 + Uncensored 去审核特性 + MoziSmartBit混合量化算法开发而成。

**💡 体积优势：仅 15.9G 小体积** —— 350 亿参数 MoE 模型经自研 MoziSmartBit 智能量化压缩至 **15.9 GB**（比常规 Q4_K_M ~22GB 小约 30%），一个安装包即可带走，普通消费级显卡（20GB 显存起）即可本地部署，云端 token 成本 = 0，实现 7×24 小时 token 自由并确保本地数据隐私与安全。授权**免费商用**，个人与企业零门槛使用。

---

## 2. 模型特色

### 🧠 动态七维思考体系

MoziAI 自研的核心推理框架。面对任何任务，模型先输出 **moziAI-Think** 标记，按任务复杂度动态展开结构化思考：

| 级别 | 适用场景 | 典型任务 | 展开维度 |
| --- | --- | --- | --- |
| **Level 0** | 简单问答 | 术语解释、事实查询、翻译、摘要 | ①理解任务 ⑤资源需求（两维速答） |
| **Level 1** | 分析诊断 | 市场调研、文案编写、数据分析、研报解读、策略评估 | ①②③⑤⑥ 五维评估 |
| **Level 2** | 复杂开发/策略 | 代码开发、架构设计、量化策略开发、多步工作流、系统设计 | ①②③④⑤⑥⑦ 全七维深度推演 |

> 七维：①理解任务 ②复杂度评估 ③依赖关系 ④风险评估 ⑤资源需求 ⑥验收标准 ⑦执行策略

### 🔄 智能体 LOOP 迭代机制

复杂任务自动进入 **moziAI-Loop** 迭代模式：**第 1 轮执行+评估 → 第 2 轮调整+验证**，确保输出经过自我校验后才给出最终答案。模型像资深工程师一样「拆解问题 → 评估方案 → 执行 → 反思 → 优化」，显著提升复杂任务的准确性和可执行性。简单问答和任务则自动关闭 Loop。

### 📦 MoziSmartBit 智能量化

自研分层智能量化，350 亿参数 MoE 模型压缩至约 **15.9 GB**，比常规 Q4_K_M（~22 GB）小约 6.5 GB（~30%），保持 FP16 **~99%** 精度。传统量化对所有层使用统一精度，MoziSmartBit 针对 MoE 模型结构特点采用智能差异化策略，精度优于 Q4_K_M。压缩比达 **4.5x**。

### 💰 金融垂直领域聚焦

针对金融问答、量化编程和工具调用的深度优化。金融领域对模型幻觉容忍度极低，MoziAI 在该领域的表现显著优于同等体积的通用模型。

### 🛡️ Uncensored 去审核特性

无内容审查限制、自由输出、完整资讯、本地私有。适合学术研究、深度分析、自由讨论等场景。（详见 [第 15 节](#15-去审核uncensored优化)）

### 🌐 其他特性

- **多语言支持**：201 种语言和方言，中文能力特别优化
- **通用编程**：全栈开发、代码调试、架构设计，覆盖 Python/JS/TS/Go/Rust
- **文章写作**：研报、分析文章、技术文档、创意内容等多体裁高质量写作
- **视觉理解**：多模态视觉，支持本地截图理解图片内容
- **多框架支持**：llama.cpp / Ollama / LM Studio / Jan
- **多 Agent支持**：OpenClaw / Hermes / Cursor / Claude Code / Codex 等，原生工具调用与多轮任务编排

---

## 3. 版本升级说明

本次 V3.8 版本采用与 27B-V3.8 同代的自研训练数据集体系进行重新训练（身份 / 动态七维思考 / LOOP 迭代 / 金融垂直领域），重点强化了 moziAI 自研的动态七维思考 + LOOP 迭代的推理模式，使其更加智能识别任务复杂度，复杂任务的完成率更高，提高"先想后做"的能力；同时延续 Uncensored 去审核特性与金融垂直领域深度优化。

moziAI 会保持活跃的版本升级迭代更新频率，确保紧随未来人工智能的发展，并且不断通过自研技术，让本地 AI 模型可轻量化部署，能力越来越强。

---

## 4. 金融领域核心能力

| 能力领域 | 说明 |
| --- | --- |
| 市场分析 | 宏观/微观经济解读、A股/港股/美股/商品/加密货币行情与逻辑梳理 |
| 财务与研报 | 财报关键指标解读、研报摘要提取、估值与盈利预测辅助 |
| 风控与合规 | 产品风险评估、投资建议合规提示、金融监管政策解读 |
| 量化与策略 | 量化策略思路设计、金字塔（Pyramid/PEL）量化、回测逻辑、因子构建与工具调用 |
| 工具调用 | 可接入实时行情、数据库、研报检索等金融数据源 |

---

## 5. 技术规格

| 项目 | 参数 |
| --- | --- |
| 底座模型 | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架构，MIT 许可证） |
| 参数规模 | 350 亿（35B）MoE 架构，256 个路由专家 + 1 个共享专家，每 token 激活 8 个专家 |
| 量化方式 | 自研 MoziSmartBit 智能量化 + GGUF 标准格式 |
| 上下文长度 | 256K（262,144 tokens） |
| 模型体积 | ~15.9 GB |
| 最低显存 | **20GB+** 可部署（CPU 卸载）；**24GB+** 流畅长上下文；**32GB+** 完整 256K + 视觉 |
| 推理框架 | llama.cpp / Ollama / LM Studio / Jan |
| 推理速度 | 推测解码下：AMD R9700 显卡可达 **140+ token/s** / AMD MAX+395 CPU 核显可达 **70+ token/s**，实现本地 token 自由输出 |
| 开发团队 | 陈雨墨团队 |

---

## 6. ⚡ 快速开始（3 个文件 = 100% 激活最佳推理能力）

> ⚠️ **核心提示**：MoziAI 的最佳推理能力需要**同时下载 3 个文件**——主模型、视觉投影、聊天模板。缺少任何一个都会损失对应能力。

### 6.1 下载模型文件

在 HuggingFace / ModelScope 下载**这 3 个文件**到本地同一目录（主模型在**仓库根目录**，视觉投影在 `mmproj/35B/`，聊天模板在 `V3.8/`）：

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← 主模型（必选，15.9 GB）
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← 视觉投影（必选，~1 GB）
moziAI-V3.8-35B-chat-template.jinja                                        ← 聊天模板（必选，含七维思考+Loop指令）
```

| 文件 | 大小 | 必要性 | 作用 |
| --- | --- | --- | --- |
| 主模型 `.gguf` | ~15.9 GB | **必选** | 模型权重，核心推理能力 |
| 视觉投影 `mmproj` | ~1 GB | **必选** | 多模态视觉理解，不载入则丧失图像能力 |
| 聊天模板 `.jinja` | 微量 | **必选** | 注入 MoziAI 身份 + 七维思考 + LOOP 机制指令 |

### 6.2 启动并使用

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

浏览器打开 `http://localhost:8080` 即可开始对话。完整推荐参数见第 9 节。

---

## 7. 模型下载

| 平台 | 地址 |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio 用户**：在 [LM Studio](https://lmstudio.ai) 中搜索 `moziAI` 一键下载，无需手动下载文件。

> 💡 **下载提示**：请点击上方链接进入 HuggingFace 仓库，在 **"Files and versions"** 标签页，于**仓库根目录**下载主模型，再从 `mmproj/35B/` 下载视觉投影、从 `V3.8/` 下载聊天模板，确保三个文件放在同一目录下。

---

## 8. 启动命令

### 最简启动（含三件套）

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### 完整推荐启动

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

> 💡 显存不足时：降低 `-c`（如 131072），或加 `--fit on` 让 llama.cpp 自动适配显存。

---

## 9. 推荐推理参数

基于本地实测优化（AMD Radeon AI PRO R9700 32GB）：

| 参数 | 日常任务/文案写作 | 复杂任务/高级编程 | 说明 |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | 日常求稳、复杂编程适度探索 |
| top\_p | 0.95 | 0.95 | 核采样阈值 |
| top\_k | 20 | 20 | 截断采样 |
| min\_p | 0.024 | 0.024 | 最小概率过滤 |
| repeat\_penalty | 1.05 | 1.05 | 重复惩罚 |
| presence\_penalty | 0 | 0 | 无存在惩罚 |
| context\_length | 262144 | 262144 | 256K 长上下文 |
| reasoning | on | on | 开启推理链（思维链） |
| reasoning\_budget | 400 | 1000 | 推理预算 token（复杂任务更高） |
| reasoning\_format | deepseek-legacy | deepseek-legacy | 推理输出到独立字段 |
| **spec-type** | **default** | **default** | **推测解码加速（ngram，MoE 最优，详见第 11 节）** |
| KV 缓存 | q4\_0 | q4\_0 | 量化 KV 缓存（统一 kv-unified） |

> 💡 **思考模式**：通过 `--reasoning on` 开启，模型先进行内部推理再输出答案。`reasoning_budget` 控制最大思考 token 数。

---

## 10. 量化格式对比

| 格式 | 体积 | 精度 | 说明 |
| --- | --- | --- | --- |
| FP16 原始 | ~70 GB | 100% | 无损，需专业显卡 |
| **MoziSmartBit（本模型）** | **~15.9 GB** | **~99%** | **自研智能量化，精度最优、体积最小** |
| Q4_K_M | ~22 GB | ~98% | GGUF 标准 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 更高精度 |
| Q6_K | ~28.5 GB | ~99.5% | 近无损 |
| Q8_0 | ~36.9 GB | ~100% | 无损 |

> MoziSmartBit 在保持约 99% 精度的同时，将 35B MoE 模型压缩至 15.9 GB（压缩比 4.5x），比 Q4_K_M 小约 30%，更适合消费级显卡本地部署。

---

## 11. 推测解码加速（重要特性）

本模型通过**推测解码（Speculative Decoding）**显著提升推理速度，本地实测比关闭时**提升约 1.5-2 倍**。

- **MoE 最优配置**：llama.cpp 对 MoE 架构推荐使用 **ngram 推测解码**（`--spec-default`），本地实测最快且稳定
- **模型命名说明**：模型名中的 "MTP" 表示底座自带的 Multi-Token Prediction 权重（已完整保留），llama.cpp 对 MoE 架构的 MTP draft 支持有限，MoziAI 统一采用 ngram 推测方案获得最佳实测速度

### 开启参数

```bash
--spec-default
```

### 参数调整建议

| 配置 | 适用场景 |
| --- | --- |
| --spec-default（默认） | 推荐：平衡速度与显存 |
| 关闭推测（删除该参数） | 显存紧张场景，速度略降 |

---

## 12. 显存配置推荐

基于 MoziSmartBit 版本（模型 + 视觉共 ~16.4GB）实测：

| 显存 | 推荐配置 | 说明 |
| --- | --- | --- |
| 20 GB | 上下文 150K，q4\_0 KV 缓存，支持视觉 | 模型+视觉共 ~16.4GB，256K+视觉仅占显存 ~19.5GB |
| **24 GB** | **256K 满配，q4\_0 KV 缓存，完美支持视觉** | **推荐配置**：视觉+256K 长上下文仅占显存 ~20.4GB，余量 ~3.6GB |
| 32 GB+ | 256K 满配，显存余量充足 | 如 R9700 32GB：视觉+256K 长上下文，余量 ~10GB，最强配置 |

> 💡 上下文越长，显存占用越多。OOM 时逐步降低 `-c` 参数。使用 `--fit on` 让 llama.cpp 自动调整层数适配显存。支持 NVIDIA / AMD 全品牌显卡。

---

## 13. 部署方式

### Ollama 部署

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

在 LM Studio / Jan 中搜索 `moziAI`，选择 Q4\_K\_M 量化版本下载即可（LM Studio 默认读取仓库根目录模型，历史版本请使用"从 URL 添加"导入对应版本目录文件，如 `V3.7/`）。

> 💡 Ollama 的 mmproj 和 chat\_template 支持有限，建议优先使用 llama.cpp 获得完整功能。

---

## 14. 基准评测

MoziAI-35B-V3.8 基于 deepreinforce-ai/Ornith-1.5-35B-A3B 底座微调、蒸馏与二次开发，金融垂直领域为核心优化方向。以下为多模型对比（MoziAI 通用能力与底座 Ornith-1.5-35B-A3B 一致；数据沿用 V3.7 版本实测，V3.8 与 V3.7 同底座同训练体系）：

| Benchmark | moziAI-35B-V3.8<br>（本模型） | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **编程测试** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **推理测试** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **代理测试** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI-35B 金融垂直领域为 MoziAI 的核心优化方向，在财报解读、量化策略、风控合规、agent 工具调用等场景下表现显著优于通用模型。Gemma-4 / Qwen3.6 数据为官方公开评测结果。

---

## 15. 去审核（Uncensored）优化

本模型继承底座 Ornith-1.5-35B-A3B 的 Uncensored（去审核）特性，具有以下优势：

| 优势 | 说明 |
| --- | --- |
| 无审查限制 | 不会拒绝任何话题，包括敏感、争议性内容 |
| 自由输出 | 不受安全策略约束，可生成任何类型的回复 |
| 完整资讯 | 提供未经过滤的完整资讯，适合研究和分析场景 |
| 本地私有 | 本地部署意味着数据完全私有，不受云端审查 |

**适用场景**：学术研究、深度分析、自由讨论、不受限的 AI 对话格局。

**注意**：本模型为本地部署模型，输出内容完全由使用者控制，不承担内容审核责任。

---

## 16. 许可证

本模型采用**自定义限制性许可证**：

- ✅ **允许** — 免费商业使用、复制和分发
- ❌ **禁止** — 二次开发、转售售卖、再许可
- 📋 **要求** — 保留原始版权声明，注明来源：moziAI-35B

本模型按「原样」提供，不提供任何形式的保证。模型输出仅供参考，不构成投资建议。使用者需自行承担使用风险。

详细条款请参阅 [LICENSE](LICENSE) 文件。

---

## 17. 联系方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.