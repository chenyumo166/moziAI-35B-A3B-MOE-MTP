# MoziAI 模型分发复盘 — 2026-08-21

> **执行者**：mxxx（MoziAI 大模型训练专家）
> **涉及项目**：MoziAI-35B (V3.6)
> **分发平台**：HuggingFace / ModelScope（魔搭）/ GitHub

---

## 一、完成的工作

### 1. HuggingFace 首页英文切换

**背景**：HuggingFace 用户 80%+ 是海外开发者，英文 README 曝光率远高于中文。

**操作**：
- `README.md`（原中文）→ 改为英文版首页
- 新建 `README.zh.md` 保存中文版
- 12 种语言的 README 全部更新语言切换链接（中文→`README.zh.md`）
- V3.6/ 子目录同步执行

**结果**：✅ 24 个文件推送成功

### 2. 三平台 README 标题统一

**操作**：所有语言的 README 标题由 `MoziAI-35B-A3B-MOE - Financial Vertical Domain LLM` 改为 `MoziAI-V3.6-35B-A3B-MOE - Free Locally Deployable Small Yet Powerful Multimodal AI`（及对应语言翻译）。

**结果**：✅ 35 个文件推送成功（HF + GH + MS）

### 3. 模型体积数据修正

**发现**：Q4_K_M 标准体积应为 ~22 GB（非 ~21.2 GB）。

**修改**：
- Q4_K_M 表格体积：~21.2 GB → ~22 GB
- 对比百分比：~27% → ~30%（(22-15.5)/22 ≈ 29.5%）
- 涉及 35 个 README 文件（根 + V3.6 + V3.7）

**结果**：✅ HF + GH 已推送，MS 待补

### 4. LM Studio 兼容性问题解决（踩坑重点）

**问题**：LM Studio 搜索 moziAI 模型后显示 "No compatible options available for this format"。

**原因**：LM Studio 只扫描 HuggingFace 仓库**根目录**下的 `.gguf` 文件。我们的 GGUF 文件放在 `V3.6/` 子目录中，LM Studio 找不到。

**解决方案**：在 HF 仓库根目录同时保存 GGUF 文件（与 V3.6/ 子目录副本并存）。HF 自动去重，不重复占用存储。

**结果**：✅ GGUF + mmproj + chat-template 上传到 HF 根目录，LM Studio 可正常检测下载。

### 5. 所有 README 添加 LM Studio 下载说明

**操作**：在 35 个 README 文件的模型下载章节添加 LM Studio 下载提示。

**结果**：✅ 三平台同步（HF + GH + MS）

### 6. 版本管理策略确立

**原则**：单仓库 + 版本子目录（与 Qwen、LLaMA、Mistral 一致）
- 根目录始终放最新版 GGUF（供 LM Studio 检测）
- 旧版保留在子目录中
- 版本迭代：创建新子目录 → GGUF 放入子目录 → 根目录 → 更新 README → 三平台同步

**记录位置**：`F:/fin_moe/doc/`

---

## 二、踩坑总结

### 1. 多平台同步顺序

**经验**：先本地统一修改，再一次性推送到三个平台，避免各平台内容不一致。

### 2. LM Studio 扫描机制

**教训**：LM Studio 只认 HF 根目录的 GGUF。子目录文件无法被检测到。

### 3. 体积数据来源

**教训**：体积数据要基于 GGUF 文件实际大小，不能凭印象填写。

---

## 三、后续改进

1. 发布新版本时，先本地统一文档再分发
2. 注意 GGUF 文件要同时放在根目录（LM Studio 兼容）
3. 定期检查三平台内容一致性
