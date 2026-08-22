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

# MoziAI-35B-A3B-MOE-MTP-Uncensored - 可免费本地部署的小而强的多模态AI模型

Language / 语言选择  
[English](README.md) | 简体中�?| [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## 模型简�?

MoziAI-35B-A3B-MOE 是由中国财经大V陈雨墨团队开发的本地开源多模态AI大模型（强化金融领域、支持视觉、工具调用、复杂长任务能力、消费级显卡本地部署），基于 Ornith-1.0-35B-A3B�?*Qwen3.5-35B-A3B/Qwen3.6-35B-A3B** 架构）底座进行二次开�?微调/蒸馏�?

本模型研发团队的理念就是让综合能力强大的本地AI大模型智能体可走入千家万户与中小企业，不再需要支付高昂的AI硬件成本或云端API成本。通过自研�?**MoziSmartBit 智能量化** 技术，�?350 亿参�?MoE 模型压缩至约 **15.5 GB**，在模型精度与体积间取得最优平衡，实现几乎≈FP16�?9%的精度质量。本模型具有350亿参数，但是采用MOE稀疏专家技术而获得只调用30亿参数并支持MTP推测解码的加速推理能力，实测可在20G显存的家用消费级显卡完成本地免费部署也可拥有140+ token/s的推理速度，推理速度优于众多云端收费AI大模型�?

本模型除了保留通用AI大模型的能力，重点优化：金融垂直领域的应用，金融问答、量化编程、通用编程、工具调用�?56K复杂长上下文任务的成功率等AI大模型关键能力。可在本地消费级显卡免费部署使用，节约大量云端token成本，实�?X24小时token自由并且确保本地数据隐私与安全�?

**发布日期�?026-08-20** | **版本：V3.6**

## 模型特色

- **MoziSmartBit 智能量化**：自研的智能量化技术，精度与体积最佳平衡，模型几乎无损压缩至约 **15.5 GB**
- **复杂长任务能�?*：训练让模型智能体为任务自动规划的智能循环处理卡点与自我思考机制，实现复杂任务的自动执行与自我调整，摆脱人类用户不断给智能体优化提示词的麻烦�?
- **小模型大能力**：在执行复杂任务上，综合能力跑赢同类350亿参数以内的模型，甚至跑赢部分比自己参数大几倍的模型�?
- **MOE+MTP的速度优势**：虽然模型整体是350亿参数，但实际只调用8+1专家�?0亿参数，推理速度更快，很适合20GB�?4GB显存的家用消费级显卡即可本地部署并享�?40+ token/s的推理速度�?
- **金融垂直深�?*：深度加强金融问答、量化编程、工具调用能�?
- **消费级部�?*�?0GB�?4GB显存以上的家用消费级显卡即可本地部署，支持最�?256K 长上下文推理
- **多语言支持**：支�?201 种语言和方言，中文能力特别优化，兼顾�?�?�?�?�?�?�?葡等主流语言
- **通用编程能力**：支持全栈开发、代码调试、架构设计、脚本编写，覆盖 Python/JS/TS/Go/Rust 等主流语言
- **文章写作能力**：支持多体裁高质量写作，包括研报、分析文章、技术文档、创意内容等
- **视觉理解**：推理框架加载视觉文件即可支持多模态视觉，可本地截图进入聊天窗口，模型能够看懂图片内信�?
- **去审核自由输�?*：无内容审查限制，可自由讨论任何话题，不受安全策略约�?
- **推理逻辑增强**：配合推理逻辑（思维链）进行训练，进一步提升推理质�?
- **多框架支�?*：兼�?llama.cpp、Ollama、LM Studio、Jan 等主流推理框�?
- **多Agent 平台支持**：深度适配 OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex 等国内外主流 AI IDE �?Agent 框架，原生支持工具调用与多轮任务编排，开箱即�?

## 去审核（Uncensored）优�?

本模型继承底�?Ornith-1.0-35B-A3B �?Uncensored（去审核）特性，具有以下优势�?

| 优势    | 说明                    |
| ----- | --------------------- |
| 无审查限�?| 不会拒绝任何话题，包括敏感、争议性内�?  |
| 自由输出  | 不受安全策略约束，可生成任何类型的回�?  |
| 完整信息  | 提供未经过滤的完整信息，适合研究和分析场�?|
| 本地私有  | 本地部署意味着数据完全私有，不受云端审�? |

**适用场景**：免费商用、学术研究、深度分析、自由讨论、不受限的AI对话�?
**注意**：本模型为本地部署模型，输出内容完全由用户控制，不承担内容审核责任�?

## 核心能力

| 能力领域  | 说明                                         |
| ----- | ------------------------------------------ |
| 市场分析  | 宏观/微观经济解读、A�?港股/美股/商品/加密货币行情与逻辑梳理          |
| 财务与研�?| 财报关键指标解读、研报摘要提取、估值与盈利预测辅助                  |
| 风控与合�?| 产品风险评估、投资建议合规提示、金融监管政策解�?                  |
| 量化与策�?| 量化策略思路设计、金字塔（Pyramid/PEL）量化、回测逻辑、因子构建与工具调用 |
| 工具调用  | 可接入实时行情、数据库、研报检索等金融数据�?                    |

## 技术规�?

| 项目     | 参数                                                                                 |
| ------ | ---------------------------------------------------------------------------------- |
| 底座模型   | Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架构，MIT 许可�?                   |
| 参数规模   | 350亿（35B）MoE 架构�?56 个路由专�?+ 1 个共享专家，�?token 激�?8 个专�?                              |
| 量化方式   | 采用自研 MoziSmartBit 智能量化算法 + GGUF 标准格式                                               |
| 上下文长�? | 256K�?62,144 tokens�?                                                              |
| 模型体积   | \~15.5 GB（MoziSmartBit Uncensored 版本�?                                             |
| 最低显存要�?| 20GB显存以上的家用消费级显卡（如 RTX 3060 12G 需搭配 CPU 卸载，RTX 4060 Ti 16G 等），推�?24 GB（含视觉 + 长上下文�?|
| 推理框架   | llama.cpp / Ollama / LM Studio / Jan                                               |
| 推理速度   | 通过算法优化，AMD R700显卡可达140+token/s / AMD MAX+395CPU核显可达70+token/s ,实现本地token自由输出       |
| 开发团�?  | 陈雨墨团�?                                                                             |

## 量化格式与模型体积对�?

| 量化格式             | 模型体积          | 精度保持      | 说明                |
| ---------------- | ------------- | --------- | ----------------- |
| FP16（原始）         | \~70 GB       | 100%      | 原始 16bit 精度       |
| **MoziSmartBit** | **\~15.5 GB** | **\~99%** | **本模型采用自研智能量化方�?* |
| Q4\_K\_M         | \~22 GB     | \~98%     | GGUF 标准 4bit      |
| Q5\_K\_M         | \~24.7 GB     | \~99%     | 更高精度              |
| Q6\_K            | \~28.5 GB     | \~99.5%   | 近无�?              |
| Q8\_0            | \~36.9 GB     | \~100%    | 无损�?              |

> MoziAI V3.6 采用 MoziSmartBit 智能量化方案，在保持�?99% 精度的同时，�?350 亿参�?MoE 模型压缩至约 15.5 GB，压缩比�?4.5x，兼顾推理质量与部署门槛，更适合消费级显卡本地部署�?

## MoziSmartBit 智能量化技�?

传统量化方案对所有层使用统一精度，而陈雨墨团队自研�?**MoziSmartBit 智能量化** 针对 MoE 模型的结构特点，采用智能差异化量化策略，在体积与精度间取得最优平衡，模型质量高于 Q4\_K\_M 格式，同时体积仅�?15.5 GB，压缩比�?4.5x�?

### 压缩效果

传统量化方案对模型所有部分统一压缩，往往导致精度损失明显。MoziSmartBit 智能量化采用自研的智能压缩策略，**在极小的精度损失下实现大幅体积缩�?*�?

- **量化精度损失极小**：训练增�?> 量化损失，训练后�?MoziAI-35B 在金融领域文本上�?PPL 优于训练前的 bf16 底座，降低了同类 AI 模型的幻觉与困惑�?
- **模型体积压缩�?4.5 �?*：从 FP16 �?\~70 GB 压缩�?\~15.5 GB，也大幅小于Q4\_K\_M的\~21 GB，大幅降低显存与存储门槛
- **消费级显卡可�?*：原本需要高端显卡的 35B MoE 大模型，现在 20GB\~24GB 显存即可流畅部署

### 对比优势

**vs Q4\_K\_M（\~22 GB�?*：体积减少约 30%（\~15.5 GB），精度�?Q4\_K\_M **更高**，显存门槛更低，中端消费级显卡（20GB）即可流畅部署�?

**vs 原始 FP16（\~70 GB�?*：体积压缩约 4.5 倍，训练有效 + 量化精度损失极小（训练增�?> 量化损失），从需要专业级显卡�?4GB+）降低到消费级显卡即可本地运�?256K 长上下文�?

## 推荐推理参数

基于本地运行配置（AMD Radeon AI PRO R9700 32GB），推荐参数如下�?

| 参数                | 推荐�?                             | 说明                     |
| ----------------- | -------------------------------- | ---------------------- |
| temperature       | 0.6                              | 平衡创意与准确�?              |
| top\_p            | 0.95                             | 核采样阈�?                 |
| top\_k            | 20                               | 截断采样                   |
| repeat\_penalty   | 1.05                             | 重复惩罚                   |
| presence\_penalty | 0                                | 无存在惩�?                 |
| context\_length   | 262144                           | 256K 长上下文              |
| batch\_size       | 2048                             | 批处理大�?                 |
| ubatch\_size      | 512                              | 微批次大�?                 |
| flash\_attention  | auto                             | 自动 Flash Attention     |
| kv\_cache         | q4\_0                            | KV 缓存量化（统一 kv-unified�?|
| poll              | 0                                | 空闲不轮�?GPU，节能低延迟        |
| reasoning         | on                               | 开启推理链（思维链）             |
| reasoning\_budget | 400                              | 推理预算 token �?          |
| reasoning\_format | deepseek-legacy                  | 推理格式                   |
| samplers          | top\_k;top\_p;temperature;typ\_p | 采样器顺�?                 |

### llama.cpp 启动命令

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

### 不同显存配置推荐

由于用户显卡配置差异较大，以下为不同显存下的推荐参数（均�?MoziSmartBit 版本）：

| 显存     | 推荐上下文长�?| KV 缓存 | 视觉支持 | 说明                                   |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB  | 128K    | q4\_0 | 支持   | 模型+视觉共\~16.4GB，实�?00K+视觉仅占显存\~19.5GB |
| 24 GB  | 256K 满配 | q4\_0 | 完美支持 | 视觉+256K长上下文,仅占显存\~20.4GB，显存余量\~3.6GB |
| 32 GB+ | 256K 满配 | q4\_0 | 完美支持 | 视觉+256K长上下文，显存余量充足\~10GB，最强配�?       |

**NVIDIA 显卡参考表**

| 显存    | 显卡型号                   |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090               |

**AMD 显卡参考表**

| 显存    | 显卡型号                |
| ----- | ------------------- |
| 20 GB | RX 7900 XT          |
| 24 GB | RX 7900 XTX         |
| 32 GB | Radeon AI PRO R9700 |

**Intel 显卡参考表**

| 显存    | 显卡型号                      |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60               |
| 16 GB | Arc Pro B50（需搭配 CPU 卸载�?  |

**CPU共享内存核显 设备参考表**

| 显存     | 处理器型�?                                 |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S 核显�?|
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU�?   |

> 💡 **提示**：只要显存满足以上要求即可使用，不限品牌型号，支�?NVIDIA / AMD / Intel 各品牌独立显卡，也支持上�?128GB 统一内存的核�?CPU�?

> 💡 **提示**：上下文越长，占用显存越多。如果出现显存不足（OOM），请逐步降低 `-c` 参数值。使�?`--fit on` 参数可让 llama.cpp 自动调整层数适配显存�?

### Ollama 部署

```bash
# 创建 Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# 构建并运�?
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan 部署

直接�?LM Studio �?Jan 中搜�?`moziAI-35B`，选择 MoziSmartBit 量化版本下载即可�?

## 基准评测

MoziAI 基于 deepreinforce-ai/Ornith-1.0-35B 底座微调、蒸馏与二次开发。MoziAI 在底座基础上针对金融垂直领域优化，在金融问答、量化编程、工具调用等场景下表现更出色。以下为多模型对比（MoziAI-35B 通用能力与底�?Ornith-1.0-35B 一致）�?

| 基准测试                         | MoziAI-35B (本模�? | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | 说明             |
| ---------------------------- | ---------------- | ----------- | ---------- | ---------- | ----------- | -------------- |
| Terminal-Bench 2.1           | 64.2             | 59.3        | 42.1       | -          | 41.4        | 自主终端编码         |
| Terminal-Bench (Claude Code) | 62.8             | 59.3        | -          | -          | 38.9        | Claude Code 编码 |
| SWE-bench Verified           | 75.6             | 77.2        | 52.0       | -          | 70.0        | 真实软件工程         |
| SWE-bench Pro                | 50.4             | 53.5        | 35.7       | -          | 44.6        | 复杂软件工程         |
| SWE-bench Multilingual       | 69.3             | 71.3        | -          | -          | 60.3        | 多语言编码          |
| NL2Repo                      | 34.6             | 36.2        | 15.5       | -          | 20.5        | 自然语言到仓�?       |
| LiveCodeBench v6             | 63.3             | 83.9        | 80.0       | 77.1       | -           | 竞赛编程           |
| GPQA Diamond                 | 88.4             | 87.8        | 84.3       | 82.3       | -           | 科学推理           |
| AIME 2026 数学                 | 93.3             | 94.1        | 89.2       | 88.3       | -           | 数学推理           |

> MoziAI-35B 通用能力基准分数与底�?Ornith-1.0-35B 一致。金融垂直领域为 MoziAI 的核心优化方向，在财报解读、量化策略、风控合规、agent管理工具调用等场景下表现显著优于通用模型。Gemma4 �?Qwen3.6 数据为官方公开评测结果�?

## 模型下载

由于模型文件较大（\~15.5 GB），模型权重托管于多个社区平台：

| 平台             | 地址                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| HuggingFace    | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub         | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |


> 💡 **LM Studio 用户**：可直接�?[LM Studio](https://lmstudio.ai) 中搜�?`moziAI` 并一键下载，无需手动下载文件�?
> 💡 **下载提示**：请点击上方链接进入 HuggingFace 仓库，在 **"Files and versions"** 标签页下�?V3.6 目录下的所有文件（主模型、视觉投影、聊天模板），确保三个文件放在同一目录下�?

⚠️ **重要：视觉能力需要额外加�?mmproj 文件**

本模型支持多模态视觉，视觉投影文件（mmproj）已包含在版本目录中�?

- **视觉文件**：`moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`（约 903 MB，BF16 精度�?
- **放置位置**：与 GGUF 模型文件放在同一版本目录�?
- **加载方式**：启�?llama-server 时通过 `--mmproj` 参数加载

```bash
llama-server -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf
```

> 不加载视觉文件将丧失图像理解能力，仅保留纯文本对话能力�?

## 快速开�?

### 1. 下载模型文件

�?HuggingFace / ModelScope 下载 V3.6 目录下的所有文件到本地�?

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # 主模型（必选）
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # 视觉投影（可选）
└── moziAI-V3.6-35B-chat-template.jinja                  # 聊天模板（推荐）
```

### 2. 启动推理服务

完整的推荐配置启动命令请参考上�?[llama.cpp 启动命令](#llamacpp-启动命令) 章节�?

最简启动（仅核心参数）：

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 需要视觉能力时加上 `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`

### 3. 开始使�?

浏览器打开 `http://localhost:8080` 即可开始对话�?

### 目录结构

```
moziAI-35B/
├── README.md              # 本文件（中文说明书）
├── README.en.md           # 说明书的英文版本
├── LICENSE                # 许可�?
├── V3.6/                  # V3.6 版本（版本自包含�?
�?  ├── RELEASE_NOTES.md                       # 版本更新说明
�?  ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # 主模�?
�?  ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # 视觉投影
�?  └── moziAI-V3.6-35B-chat-template.jinja   # 聊天模板
```

未来升级计划详见 [未来升级计划.md](未来升级计划.md)�?

## SEO 关键�?

金融AI大模型、AI大模型、本地开源模型、端侧模型、量化编程、MoziSmartBit、智能量化、GGUF量化、MoE模型、本地开源大模型、本地部署、金融AI、工具调用、Agent、llama.cpp、Ollama、GGUF、Uncensored（去审核）、无审查、免审核、自由输出、Q3\_K\_M、Q4\_K\_M、Q5\_K\_M、Q6\_K、Q8\_0、Ornith-1.0-35B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、金融垂直领域、开源模�?

## 许可证（重要�?

本模型采�?*自定义限制性许可证**，具体条款如下：

�?**允许**

- 免费商业使用：可免费集成到您的商业产品或服务�?
- 复制和分发：可原样复制、下载、分�?

�?**禁止**

- 二次开发：不得修改、翻译、改编、合并、微调本模型或其任何部分
- 转售售卖：不得将本模型单独或作为产品组成部分进行售卖
- 再许可：不得就本模型授予任何从属许可

📋 **要求**

- 使用时必须保留原始版权声�?
- 注明来源：moziAI-35B

详细许可证条款请参阅 [LICENSE](LICENSE) 文件�?

## 免责声明

本模型按"原样"提供，不提供任何形式的保证。模型输出仅供参考，不构成投资建议。使用者需自行承担使用风险�?

## 联系方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**�?263515@qq.com>

***

Copyright (c) 2026 陈雨�?/ chenyumo166. All rights reserved.
