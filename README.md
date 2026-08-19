# MoziAI-35B-A3B-MOE（墨子AI）AI大模型 V3.6

> 专注金融领域的本地开源 MoE 大模型 | 低显存门槛 | 高专业能力

**发布日期：2026-08-20** | **版本：V3.6**

---

## 模型简介

MoziAI-35B-A3B-MOE 是由中国财经大V陈雨墨团队开发的本地开源多模态AI大模型（强化金融领域、支持视觉、工具调用、消费级显卡本地部署），基于 Ornith-1.0-35B（**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** 架构）底座进行二次开发/微调/蒸馏。通过自研的 **MoziSmartBit 智能量化** 技术，将 350 亿参数 MoE 模型压缩至约 **15.5 GB**，在精度与体积间取得最优平衡，实现几乎≈FP16的99%的精度质量。

---

## 模型矩阵

| 模型 | 总参数 | 激活参数 | 架构 | 多模态 | 工具调用 | 量化方式 | 版本 |
|------|-------|---------|------|--------|---------|---------|------|
| **moziAI-35B** | 35B | ~3B | MoE | ✅ | ✅ | MoziSmartBit | **V3.6** |
| moziAI-27B | 27B | ~3B | MoE | ✅ | ✅ | MoziSmartBit | *coming soon* |

---

## 快速开始

### 模型下载

| 文件 | 大小 | 说明 |
|------|------|------|
| [moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf](./V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf) | ~15.5 GB | 主模型（必选） |
| [moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf](./V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf) | ~903 MB | 视觉投影（可选） |
| [moziAI-V3.6-35B-chat-template.jinja](./V3.6/moziAI-V3.6-35B-chat-template.jinja) | ~9 KB | 聊天模板（推荐） |

### llama.cpp 快速运行

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 更多部署方式详见 [V3.6 完整说明书](./V3.6/README.md)

---

## 核心特点

- **金融垂直深耕**：深度加强金融问答、量化编程、工具调用能力
- **MoziSmartBit 智能量化**：自研智能量化，模型体积压缩至 ~15.5 GB，精度保留约 99%
- **消费级部署**：20GB+ 显存即可本地部署，支持 256K 长上下文
- **多语言支持**：201 种语言，中文特别优化
- **通用编程**：全栈开发、代码调试、架构设计
- **视觉理解**：多模态视觉，截图识别
- **去审核自由输出**：无内容审查限制
- **多 Agent 平台**：适配 OpenClaw、Hermes、Cursor 等主流 AI IDE

---

## 版本导航

- **[V3.6 完整说明书（中文）](./V3.6/README.md)**
- **[V3.6 README (English)](./V3.6/README.en.md)**
- [未来升级计划](./V3.6/未来升级计划.md)

---

## 许可证

本模型采用**自定义限制性许可证**，详见 [LICENSE](./LICENSE)。

✅ 免费商业使用 · ✅ 复制和分发 · ❌ 禁止二次开发 · ❌ 禁止转售

---

## 联系方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

---

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
