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

# MoziAI-35B-V3.8 - 可免费本地部署的小而强的多模态 AI

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## 模型概述

MoziAI-35B-V3.8 是由中国财经大V陈雨墨团队开发的本地开源金融AI多模态大语言模型（支持视觉、工具调用与 Uncensored 去审核特性）。基于开源底座 **Ornith-1.5-35B-A3B**（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架构，MoE 35B，MIT 许可），整合团队自主研发的：金融数据 + 金融领域能力 + 训练方法 + 动态七维思考体系 + 智能体 LOOP 机制 + Uncensored 去审核特性 + 混合量化算法 MoziSmartBit。

通过自研 MoziSmartBit 智能量化技术，350 亿参数的 MoE 模型被压缩至约 **15.5 GB**，比常规 Q4_K_M（~22 GB）小约 30%；在精度与体积间取得最优平衡，提供 **~99% 的 FP16 精度质量**。

本模型大幅降低本地部署门槛，授权**免费商用**，消费级显卡即可部署，**云端 token 成本 = 0**，实现 7×24 小时 token 自由，并确保本地数据隐私与安全。

支持 llama.cpp、Ollama、LM Studio、Jan 等主流推理框架，兼容 OpenClaw / Hermes / Cursor / Claude Code / Codex 等主流 Agent 平台。

**发布日期：2026-09-01** | **版本：V3.8**

## 模型特性

- **金融垂直领域聚焦**：金融问答、量化编程、工具调用的深度优化
- **动态七维思考体系**：moziAI-Think 标记按任务复杂度动态展开 0/1/2 级结构化思考
- **智能体 LOOP 机制**：复杂任务自动进入"执行+评估 → 调整+验证"迭代，输出自我校验
- **MoziSmartBit 智能量化**：35B MoE 压缩至 15.5 GB（4.5x 压缩比），精度 ~99%
- **Uncensored 去审核**：无内容审查限制、自由输出、完整资讯、本地私有
- **256K 长上下文**：一次处理超长文档与多轮 Agent 任务
- **多模态视觉**：本地截图理解图片内容
- **多语言支持**：201 种语言和方言，中文能力特别优化
- **推理加速**：推测解码（ngram）实测 R9700 显卡 140+ tok/s / MAX+395 核显 70+ tok/s

## 技术规格

| 项目 | 参数 |
| --- | --- |
| 底座模型 | Ornith-1.5-35B-A3B（Qwen3.5/3.6-35B-A3B 架构，MIT） |
| 参数规模 | 350 亿（35B）MoE，256 路由专家 + 1 共享专家，每 token 激活 8 专家 |
| 量化方式 | MoziSmartBit + GGUF 标准格式 |
| 上下文长度 | 256K（262,144 tokens） |
| 模型体积 | ~15.5 GB |
| 最低显存 | 20GB+ 可部署（CPU 卸载）；24GB+ 流畅长上下文；32GB+ 完整 256K + 视觉 |
| 推理速度 | R9700 **140+ tok/s** / MAX+395 **70+ tok/s**（推测解码下） |

## 下载方式

| 平台 | 地址 |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main/V3.8) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/master/V3.8) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B/tree/master/V3.8) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> ⚠️ **三件套提示**：在 `V3.8/` 目录同时下载主模型（.gguf）、视觉投影（mmproj）、聊天模板（.jinja）三个文件到同一目录，才能 100% 激活最佳推理能力。

## 快速开始（llama.cpp）

```bash
llama-server \
  -m V3.8/moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 --host 0.0.0.0 --port 8080
```

浏览器打开 `http://localhost:8080` 即可开始对话。完整推荐参数与启动命令详见 `V3.8/README.zh.md`。

## 基准速览（编程/推理/代理，与底座同代实测）

| 维度 | 亮点 |
| --- | --- |
| 编程 | SWE-bench Verified **79** / SWE-bench Pro **59.6** / Terminal-Bench 2.1 **67.8-68.5**（显著优于 Ornith-1.0 与 Qwen3.6-35B-A3B） |
| 推理 | GPQA Diamond **89.2** / HLE (tools) **33.4** |
| 代理 | MCP-Atlas **70.2** / ClawEval **72.5** / Toolathlon-Verified **48.7** |

> 金融垂直领域（财报解读、量化策略、风控合规、Agent 工具调用）表现显著优于同等体积通用模型。完整 18 项对比表见 `V3.8/README.zh.md` 第 14 节。

## Uncensored 去审核

无审查限制、自由输出、完整资讯、本地私有。适合学术研究、深度分析、自由讨论等场景。本模型为本地部署模型，输出内容完全由使用者控制，不承担内容审核责任。

## 许可证

本模型采用**自定义限制性许可证**：✅ 免费商业使用 / ❌ 禁止二次开发、转售、再许可 / 📋 使用时保留原始版权声明并注明来源 moziAI-35B。模型输出仅供参考，不构成投资建议。

## 联系方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo) · **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen) · **E-mail**：263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.