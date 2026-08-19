# MoziAI-35B-A3B-MOE - Financial Vertical Domain LLM - V3.6

> Local open-source MoE LLM for financial domain | Low VRAM requirement | High professional capability

**Release Date: 2026-08-20** | **Version: V3.6**

---

## Model Overview

MoziAI-35B-A3B-MOE is a local open-source financial AI multimodal LLM (supports vision and tool calling) developed by Chinese finance influencer Chen Yumo's team, fine-tuned/distilled from the Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** architecture, MIT licensed) foundation model. Through the self-developed **MoziSmartBit Intelligent Quantization** technology, the 35B-parameter MoE model is compressed to approximately **15.5 GB**, achieving an optimal balance between precision and size with near-lossless ~99% precision quality.

---

## Model Matrix

| Model | Total Params | Active Params | Architecture | Multimodal | Tool Calling | Quantization | Version |
|-------|-------------|---------------|-------------|-----------|-------------|-------------|---------|
| **moziAI-35B** | 35B | ~3B | MoE | ✅ | ✅ | MoziSmartBit | **V3.6** |
| moziAI-27B | 27B | ~3B | MoE | ✅ | ✅ | MoziSmartBit | *coming soon* |

---

## Quick Start

### Model Downloads

| File | Size | Description |
|------|------|-------------|
| [moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf](./V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf) | ~15.5 GB | Main model (required) |
| [moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf](./V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf) | ~903 MB | Vision projection (optional) |
| [moziAI-V3.6-35B-chat-template.jinja](./V3.6/moziAI-V3.6-35B-chat-template.jinja) | ~9 KB | Chat template (recommended) |

### llama.cpp Quick Start

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> For more deployment options, see [V3.6 Full Documentation (English)](./V3.6/README.en.md)

---

## Key Features

- **Financial Vertical Focus**: Deep optimization for financial Q&A, quantitative programming, tool calling
- **MoziSmartBit Intelligent Quantization**: Compressed to ~15.5 GB, ~99% precision retained
- **Consumer-grade Deployment**: 20GB+ VRAM, supports 256K long context
- **Multilingual Support**: 201 languages, enhanced Chinese capabilities
- **General Programming**: Full-stack development, code debugging, architecture design
- **Vision Understanding**: Multimodal vision, screenshot recognition
- **Uncensored Free Output**: No content censorship
- **Multi-Agent Platform**: OpenClaw, Hermes, Cursor and other AI IDEs

---

## Version Navigation

- **[V3.6 Full Documentation (Chinese)](./V3.6/README.md)**
- **[V3.6 README (English)](./V3.6/README.en.md)**
- [Future Upgrade Plan](./V3.6/未来升级计划.md)

---

## License

Custom Restrictive License. See [LICENSE](./LICENSE) for details.

✅ Free commercial use · ✅ Copy & distribute · ❌ No derivative works · ❌ No resale

---

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.
