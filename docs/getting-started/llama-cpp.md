# llama.cpp 使用指南

本文档介绍如何使用 llama.cpp 运行 MoziAI-35B 模型。

---

## 前置条件

- 已安装 [llama.cpp](https://github.com/ggerganov/llama.cpp)
- 下载 MoziAI-35B V3.6 模型文件
- 显卡显存 ≥ 16GB（纯文本），推荐 24GB+

---

## 文件准备

确保以下文件在同一版本目录下：

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf       # 主模型（必选）
├── moziAI-35B-mmproj-BF16-V1.0.gguf   # 视觉投影器（可选，需要视觉时加载）
└── moziAI-V3.6-35B-chat-template.jinja                   # 对话模板（推荐）
```

---

## 基本对话（交互式）

```bash
# 在 V3.6 目录下运行
./main \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  -i
```

参数说明：
- `-m`：模型文件路径
- `--chat-template`：对话模板文件
- `-i`：交互式模式

---

## 多模态对话（带图片）

```bash
./main \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --image path/to/chart.png \
  -p "请分析这张K线图的走势"
```

参数说明：
- `--mmproj`：多模态投影器文件
- `--image`：输入图片路径
- `-p`：提示词

---

## 服务模式（API）

```bash
./server \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --host 0.0.0.0 \
  --port 8080 \
  -c 262144
```

启动后访问 `http://localhost:8080` 即可使用 Web 界面，或通过 API 调用。
