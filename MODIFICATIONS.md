# Modifications Notice / 修改声明

本文件依据 **Apache License, Version 2.0 第 4(b) 条** 的要求发布：
分发衍生作品时，必须使任何被修改的文件带有显著声明，说明该文件已被修改。

This file is published to satisfy **Apache License, Version 2.0,
Section 4(b)**, which requires that any modified files carry prominent
notices stating that they were changed.

---

## 1. 原始作品 / Original work

| 项目 | 内容 |
|---|---|
| 上游基底模型 | Ornith-1.5-35B-A3B |
| 上游仓库 | `ornith-ai/Ornith-1.5-35B-A3B`（https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B） |
| 上游自研增量的许可 | MIT License（上游模型卡声明；截至 2026-09-13 上游仓库未随附 LICENSE 文件） |
| 上游自身继承的预训练基底 | Qwen3.5-35B-A3B / Qwen3.6-35B-A3B（Apache License 2.0） |
| 上游经 Ornith-1.0 血统继承的组件 | Gemma 4（Apache License 2.0，见 https://ai.google.dev/gemma/apache_2） |
| 本作品 | MoziAI-35B-A3B-MOE-MTP（moziAI-35B-V3.8） |
| 修改人 | Chen Yumo / 陈雨墨 / chenyumo166 |
| 修改时间 | 2026-08-10 ~ 2026-09-01 |

---

## 2. 修改内容 / What was changed

MoziAI 团队对原始作品进行了以下修改：

The MoziAI team made the following changes to the original work:

1. **继续训练 / 微调** — 在金融领域数据上进行继续预训练与监督微调
   **Continued training / fine-tuning** — continued pre-training and
   supervised fine-tuning on financial-domain data.
2. **蒸馏与二次开发** — 对上游模型进行蒸馏与进一步开发
   **Distillation and further development** of the upstream model.
3. **重新量化** — 使用自研 MoziSmartBit 混合量化算法对权重重新量化
   （Q4_K_M 级别，GGUF 格式）
   **Requantization** of the weights with the MoziAI-developed
   MoziSmartBit hybrid quantization algorithm (Q4_K_M class, GGUF).
4. **对话模板** — 新增自定义 chat template，注入 MoziAI 身份标识、
   动态七维思考指令与 LOOP 迭代指令
   **Chat template** — added a custom chat template injecting the MoziAI
   identity marker, seven-dimensional thinking instructions and LOOP
   iteration instructions.
5. **视觉投影器** — 新增 mmproj 视觉投影器文件
   **Vision projector** — added mmproj projector artifacts.
6. **文档与脚手架** — 新增/改写 README、MODEL_CARD、docs、发布脚本
   **Documentation and scaffolding** — added/rewrote README, MODEL_CARD,
   docs and release scripts.

---

## 3. 被修改 / 新增的文件清单 / Modified & added files

### 权重与推理产物 / Weights and inference artifacts

| 文件 | 状态 |
|---|---|
| `moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf` | 由上游权重**修改**（继续训练 + 重新量化） |
| `mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf` | **新增** |
| `V3.8/moziAI-V3.8-35B-chat-template.jinja` | **新增** |
| 历史版本 `V3.6/`、`V3.7/` 下的权重与模板 | 同样为对上游的**修改** |

### 文档 / Documentation

| 文件 | 状态 |
|---|---|
| `README.md`、`README.modelscope.md` | **新增/改写** |
| `MODEL_CARD.md`、`MODEL_CARD.zh.md` | **新增/改写** |
| `V3.8/README.*.md`（18 种语言） | **新增/改写** |
| `docs/**` | **新增** |
| `LICENSE`（Apache 2.0 全文）、`NOTICE`、`LICENSE.zh-CN.md` | **新增/改写** |

---

## 4. 未修改的上游权利 / Upstream rights not modified

本声明仅记录 MoziAI 团队的修改行为，**不改变**任何上游组件的许可状态。

This statement only records the MoziAI team's modifications. It does
**not** alter the license status of any upstream component.

- 继承自上游（Qwen3.5/3.6 与 Gemma 4）的组件持续受 **Apache License, Version 2.0**
  约束，见 `LICENSE`。
- Ornith 自研增量适用上游声明的 **MIT License**，不受本仓库许可条件影响。
- 上游版权、商标与归属声明见 `NOTICE`。
- 详细许可分层见 `NOTICE` 第 5 节。

---

## 5. 上游文件名的保留 / Retention of upstream notices

原始上游作品中的版权、专利、商标与归属声明（Apache License 2.0
第 4(c) 条要求保留的部分）均未被移除或隐藏。

No copyright, patent, trademark or attribution notice from the
original upstream work (as required to be retained by Apache License
2.0, Section 4(c)) has been removed or obscured.

---

*本文件最后更新：2026-09-13 / Last updated: 2026-09-13*

---


<!-- UPSTREAM-LICENSE-NOTICE:BEGIN -->
## License

License: **Apache License 2.0** — authoritative text: [`LICENSE`](LICENSE) (Chinese note: [`LICENSE.zh-CN.md`](LICENSE.zh-CN.md)).
This model is distributed as a whole under Apache-2.0; upstream components (Qwen3.5/3.6 and Gemma 4) are Apache-2.0 and the Ornith increment is MIT as declared upstream (notices retained). Attribution: [`NOTICE`](NOTICE); modifications: [`MODIFICATIONS.md`](MODIFICATIONS.md).
<!-- UPSTREAM-LICENSE-NOTICE:END -->


