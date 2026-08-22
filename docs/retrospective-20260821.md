# MoziAI 模型分发复盘 �?2026-08-21

> **执行�?*：mxxx（MoziAI 大模型训练专家）
> **涉及项目**：MoziAI-35B (V3.6)
> **分发平台**：HuggingFace / ModelScope（魔搭）/ GitHub

---

## 一、完成的工作

### 1. HuggingFace 首页英文切换

**背景**：HuggingFace 用户 80%+ 是海外开发者，英文 README 曝光率远高于中文�?
**操作**�?- `README.md`（原中文）→ 改为英文版首�?- 新建 `README.zh.md` 保存中文�?- 12 种语言�?README 全部更新语言切换链接（中文→`README.zh.md`�?- V3.6/ 子目录同步执�?
**结果**：✅ 24 个文件推送成�?
### 2. 三平�?README 标题统一

**操作**：所有语言�?README 标题�?`MoziAI-35B-A3B-MOE - Financial Vertical Domain LLM` 改为 `MoziAI-V3.6-35B-A3B-MOE - Free Locally Deployable Small Yet Powerful Multimodal AI`（及对应语言翻译）�?
**结果**：✅ 35 个文件推送成功（HF + GH + MS�?
### 3. 模型体积数据修正

**发现**：Q4_K_M 标准体积应为 ~22 GB（非 ~21.2 GB）�?
**修改**�?- Q4_K_M 表格体积：~21.2 GB �?~22 GB
- 对比百分比：~27% �?~30%�?22-15.5)/22 �?29.5%�?- 涉及 35 �?README 文件（根 + V3.6 + V3.7�?
**结果**：✅ HF + GH 已推送，MS 待补

### 4. LM Studio 兼容性问题解决（踩坑重点�?
**问题**：LM Studio 搜索 moziAI 模型后显�?"No compatible options available for this format"�?
**原因**：LM Studio 只扫�?HuggingFace 仓库**根目�?*下的 `.gguf` 文件。我们的 GGUF 文件放在 `V3.6/` 子目录中，LM Studio 找不到�?
**解决方案**：在 HF 仓库根目录同时保�?GGUF 文件（与 V3.6/ 子目录副本并存）。HF 自动去重，不重复占用存储�?
**结果**：✅ GGUF + mmproj + chat-template 上传�?HF 根目录，LM Studio 可正常检测下�?
### 5. 所�?README 添加 LM Studio 下载说明

**操作**：在 35 �?README 文件的模型下载章节添�?LM Studio 下载提示�?
**结果**：✅ 三平台同步（HF + GH + MS�?
### 6. 版本管理策略确立

**原则**：单仓库 + 版本子目录（�?Qwen、LLaMA、Mistral 一致）
- 根目录始终放最新版 GGUF（供 LM Studio 检测）
- 旧版保留在子目录�?- 版本迭代：创建新子目�?�?GGUF 放入子目�?根目�?�?更新 README �?三平台同�?
**记录位置**：AGENTS.md（七.5 模型发布策略�? 模型分发操作说明书（十、版本管理策略）

### 7. 安全排除规则

**发现**：`debug.log` �?`模型分发操作说明�?md` 不应推送到公开平台�?
**确认**：三大平台均无这两个文件（从未被推送过）�?
**防护**�?- 创建 `dist/moziAI-35B/.gitignore` 排除内部文件
- AGENTS.md 和分发操作说明书记录禁止公开的文件清�?- 上传脚本必须使用白名单模式（`allow_patterns`�?
---

## 二、踩坑记�?
### �?1：ModelScope Token 频繁过期

**现象**：ModelScope session token 有效期极短，每次推送都可能过期�?
**解决**：用户手动到魔搭用户中心获取�?Token，更新到 `~/.modelscope/credentials/session`�?
**教训**：ModelScope SDK �?`api.login()` 会写 `~/.modelscope/credentials/user` 文件，sandbox 环境下可能报权限错误（但不影响实际上传）�?
### �?2：HF 推送限�?
**现象**：每小时 128 �?commit 限制，频繁推送单文件会快速耗尽�?
**解决**：使�?`upload_folder()` 批量上传替代逐文�?`upload_file()`，一�?commit 提交所有变更�?
**教训**：README 更新等批量操作应合并为一�?commit�?
### �?3：ModelScope `delete_repo_file` 不存�?
**现象**：`HubApi` 没有 `delete_repo_file` 方法�?
**结论**：ModelScope SDK 不支持通过 Python 删除单个文件，需要通过网页手动操作或使�?REST API�?
### �?4：PowerShell 执行策略拦截

**现象**：脚本执行时出现 `about_Execution_Policies` 错误�?
**影响**：不影响 Python 脚本执行，仅 PowerShell 原生命令受影响。可通过 `Set-ExecutionPolicy` 解决�?
---

## 三、三平台最终状�?
| 平台 | README | GGUF | 语言�?| LM Studio |
|------|--------|------|--------|-----------|
| HuggingFace | �?英文首页 + 11 语言 | �?根目录（主模�?视觉+模板�? V3.6/ | 12 | �?可搜索下�?|
| ModelScope | �?三平台同�?| �?待上�?| 12 | �?|
| GitHub | �?三平台同�?| �?不放大文�?| 12 | �?|

---

## 四、待办事�?
| 优先�?| 事项 | 说明 |
|--------|------|------|
| �?| ModelScope 上传 GGUF | 主模�?14.4GB + 视觉投影 903MB，需�?Token |
| �?| ModelScope 补推 Q4_K_M 修复 | 体积 21.2�?2GB，百分比 27%�?0% |
| �?| 清理 HF 仓库中的测试文件 | `tmp_ms_test.txt`（可能已自动清理�?|
| �?| 生成广告横幅图片 | 科技感横幅，用于 README 顶部 |

---

## 五、关键经验总结

1. **LM Studio 兼容�?*：GGUF 必须�?HF 仓库根目录才能被检测到
2. **批量推�?*：用 `upload_folder()` 替代逐文�?`upload_file()` 避免限�?3. **版本管理**：单仓库 + 版本子目录是主流做法，不要每版一个仓�?4. **安全红线**：内部文档（操作说明书、调试日志）绝不推送到公开平台
5. **Token 管理**：ModelScope Token 有效期短，推送前先验证有效�?6. **体积数据**：上传前确认实际文件大小，文档数据必须与实际一�?