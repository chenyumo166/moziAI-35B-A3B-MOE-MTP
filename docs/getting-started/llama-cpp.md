# llama.cpp 使用指南

本文档介绍如何使�?llama.cpp 运行 MoziAI-35B 模型�?

---

## 前置条件

- 已安�?[llama.cpp](https://github.com/ggerganov/llama.cpp)
- 下载 MoziAI-35B V3.6 模型文件
- 显卡显存 �?16GB（纯文本），推荐 24GB+

---

## 文件准备

确保以下文件在同一版本目录下：

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf       # 主模型（必选）
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf   # 视觉投影器（可选，需要视觉时加载�?
└── moziAI-V3.6-35B-chat-template.jinja                   # 对话模板（推荐）
```

---

## 基本对话（交互式�?

```bash
# �?V3.6 目录下运�?
./main \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  -i
```

参数说明�?
- `-m`：模型文件路�?
- `--chat-template`：对话模板文�?
- `-i`：交互式模式

---

## 多模态对话（带图片）

```bash
./main \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --image path/to/chart.png \
  -p "请分析这张K线图的走�?
```

参数说明�?
- `--mmproj`：多模态投影器文件
- `--image`：输入图片路�?
- `-p`：提示词

---

## 服务模式（API�?

```bash
./server \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --host 0.0.0.0 \
  --port 8080 \
  -c 262144
```

启动后访�?`http://localhost:8080` 即可使用 Web 界面，或通过 API 调用�?

常用参数�?
- `--host`：监听地址
- `--port`：监听端�?
- `-c`：上下文长度（最�?262144 / 256K�?

---

## 推荐配置（基�?32GB 显存�?

以下�?V3.6 推荐推理参数（基�?AMD Radeon AI PRO R9700 32GB 验证）：

```bash
llama-server \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

| 参数 | 推荐�?| 说明 |
|------|-------|------|
| temperature | 0.6 | 平衡创意与准确�?|
| top_p | 0.95 | 核采样阈�?|
| top_k | 20 | 截断采样（V3.6 优化�?|
| context_length | 262144 | 256K 长上下文 |
| batch_size | 2048 | 批处理大�?|
| flash_attn | auto | 自动 Flash Attention |
| kv_cache | q4_0 | KV 缓存量化 |
| reasoning | on | 开启推理链 |

---

## 不同显存配置推荐

| 显存 | 推荐上下文长�?| KV 缓存 | 视觉支持 | 说明 |
|------|--------------|---------|---------|------|
| 16 GB | 32K ~ 64K | q4_0 | 不推�?| 仅纯文本推理，建议关闭视�?|
| 20 GB | 64K ~ 128K | q4_0 | 有限支持 | 视觉+短上下文可用，长上下文需关闭视觉 |
| 24 GB | 128K ~ 256K | q4_0 | 支持 | 视觉+中长上下文流畅运�?|
| 32 GB+ | 256K 满配 | q4_0 | 完美支持 | 视觉+256K长上下文，推荐配�?|

> 💡 **提示**：上下文越长，占用显存越多。如果出现显存不足（OOM），请逐步降低 `-c` 参数值。使�?`--fit on` 参数可让 llama.cpp 自动调整层数适配显存�?

---

## 常见问题

### Q: 显存不足怎么办？
A: 可以�?
1. 减少 `-ngl` 层数，部分层�?CPU
2. 降低上下文长�?`-c`
3. 使用 `--fit on` 自动适配
4. 使用 q4_0 KV 缓存（已默认启用�?

### Q: 对话模板不生效？
A: 确认 `--chat-template` 路径正确，且文件�?jinja 格式�?

### Q: 工具调用怎么用？
A: 参�?[工具调用指南](../features/tool-calling.md)�?

### Q: 推理速度慢？
A: 检查：
1. `-ngl 99` 是否全部层加载到 GPU
2. `--flash-attn auto` 是否已开�?
3. `--batch-size` 是否设置合理�?048 推荐�?
4. 确认使用 GPU 版本�?llama.cpp
