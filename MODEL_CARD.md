# Model Card: MoziAI-35B V3.7

## Model Details

- **Model Name**: MoziAI-35B-A3B-MOE
- **Model Type**: Mixture of Experts (MoE) Large Language Model with Vision
- **Total Parameters**: 35B (MoE: 256 routed experts + 1 shared expert, 8 active per token)
- **Active Parameters**: ~3B
- **Version**: V3.7
- **Release Date**: 2026-08-21
- **Developed by**: Chen Yumo Team (陈雨墨团队)
- **License**: Custom Restrictive License (free commercial use, no modification/resale)
- **Format**: GGUF (quantized with MoziSmartBit Intelligent Quantization)

---

## Model Description

MoziAI-35B-A3B-MOE is a financial-domain specialized MoE large language model developed by Chinese finance influencer Chen Yumo's team. Built on the open-source Ornith-1.5-35B-A3B base (Qwen3.5/Qwen3.6 architecture, MIT licensed), incorporating:

- Financial vertical domain data and capabilities
- Seven-Dimensional Thinking framework (七维思考体系)
- Agent LOOP mechanism
- **MoziSmartBit Intelligent Quantization** (self-developed)

Through MoziSmartBit, the 35B MoE model is compressed to **~15.5 GB** (~30% smaller than Q4_K_M), achieving **~99% of FP16 precision**.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Financial Focus** | Deep optimization for financial Q&A, quantitative programming, tool calling |
| **MoziSmartBit Quantization** | Self-developed smart quantization, ~15.5 GB with ~99% precision |
| **Consumer GPU Deploy** | 20GB+ VRAM (e.g., RTX 4060 Ti 16G with CPU offload), 24GB recommended |
| **256K Context** | Supports long context for complex financial analysis |
| **Vision Multimodal** | Supports image understanding via mmproj file |
| **Tool Calling** | Native function calling / agent support |
| **Uncensored** | Free output without content restrictions |
| **Multi-Language** | 201 languages, enhanced Chinese capabilities |

---

## Quantization Comparison

| Format | Size | Precision | Notes |
|--------|------|-----------|-------|
| FP16 (original) | ~70 GB | 100% | Original 16bit |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **Used by MoziAI, optimal scheme** |
| Q4_K_M | ~22 GB | ~98% | GGUF standard 4bit |
| Q5_K_M | ~24.7 GB | ~99% | Higher quality |
| Q6_K | ~28.5 GB | ~99.5% | Near lossless |
| Q8_0 | ~36.9 GB | ~100% | Lossless |

---

## Hardware Requirements

| VRAM | Context | Vision | Recommended GPUs |
|------|---------|--------|------------------|
| 20 GB | 150K | Supported | RX 7900 XT |
| 24 GB | 256K full | Full support | RTX 4090, RX 7900 XTX |
| 32 GB+ | 256K full | Full support | RTX 5090, R9700 |
| 128 GB | 256K full | Full support | AMD Ryzen AI Max+ 395 |

---

## Quick Start

### llama.cpp

```bash
llama-server \
  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 1000 \
  --host 0.0.0.0 --port 8080
```

### Ollama

```bash
# Create Modelfile
FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144

# Build and run
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

---

## Intended Uses

- Financial analysis and market research
- Quantitative strategy development (Pyramid/PEL)
- Code generation and debugging
- Document analysis and summarization
- Multimodal chart interpretation
- General AI assistant tasks

## Out-of-Scope Uses

- Providing financial advice or investment recommendations
- Automated trading without human supervision
- Use that violates laws or regulations
- Generating harmful, illegal, or deceptive content

---

## Limitations

1. **Hallucinations**: May generate incorrect information in niche financial topics
2. **Financial Disclaimer**: Outputs are for informational purposes only, not investment advice
3. **Knowledge Cutoff**: May not have most recent market events
4. **Quantization Artifacts**: Slightly reduced quality vs full precision

---

## Model Download

| Platform | Link |
|----------|------|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

---

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

*Last updated: 2026-08-21*
