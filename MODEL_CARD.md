# Model Card: MoziAI-35B

## Model Details

- **Model Name**: MoziAI-35B
- **Model Type**: Mixture of Experts (MoE) Large Language Model with Vision
- **Total Parameters**: 35B
- **Active Parameters**: ~3B
- **Version**: V3.6
- **Release Date**: 2026-08
- **Developed by**: 陈雨墨团队
- **License**: Apache License 2.0
- **Format**: GGUF (quantized)

### Model Architecture
- MoE (Mixture of Experts) decoder-only transformer
- Multimodal support (text + image) via separate vision projector (mmproj)
- Native function calling / tool use capability
- Q4Q3 Hybrid quantized version (main release)

---

## Model Description

MoziAI-35B is a financial-domain specialized MoE large language model. It is designed to provide professional financial knowledge, quantitative programming capabilities, and general AI assistance while maintaining a low memory footprint through its MoE architecture.

The model excels at:
- Financial knowledge Q&A and analysis
- Quantitative trading strategy development (Pyramid / PEL format)
- Python programming and tool development
- Financial chart and image understanding (multimodal)
- Tool use and function calling
- General purpose knowledge and coding

---

## Intended Uses

### Primary Intended Use
- Financial analysis assistance
- Quantitative strategy prototyping
- Programming and code generation
- Financial document analysis and summarization
- Multimodal chart interpretation
- General AI assistant tasks

### Target Users
- Financial professionals
- Quantitative traders
- Software developers
- Researchers
- Hobbyists and enthusiasts

### Out-of-Scope Use Cases
- Use that violates any laws or regulations
- Providing financial advice or investment recommendations (for informational purposes only)
- Any use that bypasses safety guardrails for harmful purposes
- Automated trading without human supervision

---

## Bias, Risks, and Limitations

### Known Limitations
1. **Hallucinations**: Like all LLMs, the model may generate incorrect or fabricated information, especially in niche financial topics. Always verify critical facts.

2. **Financial Disclaimer**: The model's outputs are for informational and educational purposes only. They do not constitute financial advice.

3. **Knowledge Cutoff**: The model's training data has a cutoff date. It may not have the most recent market events or regulatory changes.

4. **Quantization Artifacts**: Quantized versions may have slightly reduced output quality compared to full precision. Q4Q3 hybrid is optimized for a balance of quality and size.

5. **Vision Capability**: Vision understanding is supplementary. It should not be relied upon for precise numerical extraction from charts or documents.

### Ethical Considerations
- Do not use this model for market manipulation or misleading financial information dissemination.
- Do not use to generate harmful, illegal, or deceptive content.
- Users are responsible for complying with local laws and regulations regarding AI usage in financial contexts.

---

## Evaluation

### Quantitative Performance

*Detailed evaluation results and benchmark comparisons are available in the [Evaluation Report](./docs/evaluation.md).*

### Key Capabilities Tested
- Financial domain knowledge
- Code generation (Python, PEL/Pyramid)
- General reasoning
- Multimodal understanding
- Tool calling accuracy

---

## How to Use

### Quick Start with llama.cpp

```bash
# Text only
./main -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template V3.6/chat-template/chat-template.jinja \
  -i

# With vision (multimodal)
./main -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template V3.6/chat-template/chat-template.jinja \
  --image path/to/chart.png
```

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| GPU VRAM | 8 GB | 12 GB+ |
| RAM | 16 GB | 32 GB |
| Disk Space | 7 GB | 10 GB |
| GPU | NVIDIA RTX 3060+ / AMD RX 6800+ / Apple M2+ | NVIDIA RTX 4070+ |

---

## Citation

```bibtex
@misc{moziAI-35B-2026,
  title={MoziAI-35B: A Financial Domain MoE Large Language Model},
  author={陈雨墨团队},
  year={2026},
  howpublished={\url{https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored}}
}
```

---

## Model Card Contact

For questions about this model card or the model, please open an issue on the project repository.

---

*Last updated: 2026-08*
