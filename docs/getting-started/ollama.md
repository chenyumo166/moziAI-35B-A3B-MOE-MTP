# Ollama 使用指南

本文档介绍如何在 Ollama 中使用 MoziAI-35B 模型。

---

## 步骤

### 1. 安装 Ollama

从 [Ollama 官网](https://ollama.com/) 下载并安装。

### 2. 准备模型文件

下载模型文件到本地：
- `moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf`

### 3. 创建 Modelfile

创建一个名为 `Modelfile` 的文件，内容如下：

```dockerfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

TEMPLATE """{{- range .Messages }}
{{- if eq .Role "system" }}<|im_start|>system
{{ .Content }}<|im_end|>
{{- else if eq .Role "user" }}<|im_start|>user
{{ .Content }}<|im_end|>
{{- else if eq .Role "assistant" }}<|im_start|>assistant
{{ .Content }}<|im_end|>
{{- end }}
{{- end }}
{{- if . }}
<|im_start|>assistant
{{- end }}
"""

PARAMETER stop "<|im_end|>"
PARAMETER stop "<|im_start|>"
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99
```

> 注：Ollama 的 TEMPLATE 为示例，推荐使用模型自带的 jinja 模板以获得最佳效果。

### 4. 导入模型

```bash
ollama create moziAI-35B -f Modelfile
```

### 5. 运行模型

```bash
ollama run moziAI-35B
```

---

## API 调用

Ollama 提供 REST API：

```bash
# 生成对话
curl http://localhost:11434/api/chat -d '{
  "model": "moziAI-35B",
  "messages": [
    {
      "role": "user",
      "content": "介绍一下MACD指标"
    }
  ]
}'
```

---

## 推荐参数

| 参数 | 推荐值 | 说明 |
|------|-------|------|
| temperature | 0.6 | 平衡创意与准确性 |
| top_p | 0.95 | 核采样阈值 |
| top_k | 20 | 截断采样（V3.6 优化） |
| num_ctx | 262144 | 256K 长上下文（根据显存调整） |
| num_gpu | 99 | 全部层加载到 GPU |

---

## 显存配置建议

| 显存 | 推荐 num_ctx | 说明 |
|------|-------------|------|
| 16 GB | 32768 (32K) | 纯文本推理 |
| 20 GB | 65536 (64K) | 可尝试视觉 |
| 24 GB | 131072 (128K) | 视觉+中长上下文 |
| 32 GB+ | 262144 (256K) | 满配推荐 |

---

## 注意事项

- 多模态和工具调用功能在 Ollama 中可能有限制
- 如需完整功能（视觉、工具调用、推理链等），推荐使用 llama.cpp
- 首次运行会将模型加载到内存，后续调用更快
