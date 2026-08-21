# Release Notes - MoziAI-35B V3.7

**发布日期**: 2026-08-21

---

## V3.7 版本亮点

### 核心升级

- **MoziSmartBit 智能量化算法（Q4_K_M）**：从三值量化升级为MoziSmartBit 智能量化（Q4_K_M），专家层 Q4_K_M 均匀量化 + MoziSmartBit 智能比特分配，精度 ~99%，模型体积 ~15.5 GB
- **256K 超长上下文**：支持 262,144 tokens 长上下文，适合研报、财报、长文档分析
- **Uncensored 去审核**：继承底座 Ornith-1.5-35B-A3B 的 Uncensored 特性，无内容审查限制
- **多模态视觉**：支持图片输入与理解，适配金融图表、K线图、财报识别
- **工具调用**：原生支持 Function Calling / Tool Use，可接入实时行情等金融数据源

### 金融垂直优化

- 深度优化金融专业知识问答
- 金字塔（Pyramid/PEL）量化策略编写能力加强
- Python 编程与量化代码生成优化
- K线图、财报图表识别与分析
- 研报摘要与要点提取
- 风控合规与金融监管政策解读

### 性能与部署

| 指标 | V3.7 |
|------|------|
| 模型体积 | ~15.5 GB |
| 推理速度 | AMD R700 显卡可达 140+ token/s |
| 最低显存 | 16 GB（纯文本）/ 24 GB（视觉+中长上下文） |
| 推荐显存 | 32 GB（256K 满配 + 视觉） |
| 量化方式 | MoziSmartBit 智能量化（Q4_K_M） |
| 文件格式 | GGUF |

### 版本规格

| 项目 | 规格 |
|------|------|
| 底座模型 | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B，MIT 许可） |
| 总参数量 | 35B |
| 架构 | MoE (256 路由专家 + 1 共享专家，激活 8 个/token) |
| 量化方式 | MoziSmartBit 智能量化（Q4_K_M） |
| 上下文长度 | 256K（262,144 tokens） |
| 多模态 | ✅ Vision（mmproj） |
| 工具调用 | ✅ Function Calling |
| 去审核 | ✅ Uncensored |
| 文件格式 | GGUF |
| 模型大小 | ~15.5 GB |

---

## 文件说明

V3.7 版本目录包含以下文件（版本自包含）：

| 文件 | 说明 | 大小 |
|------|------|------|
| `moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf` | 主模型文件（必选） | ~15.5 GB |
| `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` | 视觉投影文件（可选，需要视觉能力时加载） | ~903 MB |
| `moziAI-V3.7-35B-chat-template.jinja` | 聊天模板（推荐配合使用） | ~9 KB |
| `RELEASE_NOTES.md` | 本文件（版本更新说明） | - |

---

*详细评测数据请参考 [Evaluation Report](../docs/evaluation.md)*
*快速开始请参考 [README.md](README.md)*
