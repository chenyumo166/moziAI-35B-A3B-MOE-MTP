---
language:
- zh-hant
- en
license: other
tags:
- gguf
- MoE
- financial-llm
- MoziSmartBit
- qwen3.5
- qwen3.6
- ornith
- MoziAI
- tool-calling
- uncensored
- vision
- MTP
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.8 — 可免費本地部署的小而強的多模態 AI 模型

[English](README.en.md) | [简体中文](README.zh.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**發佈日期：2026-09-01** · **版本：V3.8**

---

## 📑 目錄

- [1. 模型概述](#1-模型概述)
- [2. 模型特色](#2-模型特色) — 動態七維思考 / LOOP / MoziSmartBit / 金融聚焦
- [3. 版本升級說明](#3-版本升級說明)
- [4. 核心能力](#4-核心能力)
- [5. 技術規格](#5-技術規格)
- [6. ⚡ 快速開始](#6--快速開始-3-個文件--100-啟動最佳推理能力) — **三件套下載**
- [7. 模型下載](#7-模型下載)
- [8. 啟動命令](#8-啟動命令)
- [9. 推薦推理參數](#9-推薦推理參數)
- [10. 量化格式對比](#10-量化格式對比)
- [11. 推測解碼加速](#11-推測解碼加速-重要特性)
- [12. 顯存配置](#12-顯存配置推薦)
- [13. 部署方式](#13-部署方式)
- [14. 基準評測](#14-基準評測)
- [15. 去審核（Uncensored）優化](#15-去審核-uncensored-優化)
- [16. 許可證](#16-許可證)
- [17. 聯絡方式](#17-聯絡方式)

---

## 1. 模型概述

MoziAI-35B-V3.8 是由中國財經大V陳雨墨團隊開發的本地開源多模態AI大模型，基於開源底座 **Ornith-1.5-35B-A3B**（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MoE 35B，MIT 許可），結合團隊自主研發的金融數據 + 金融領域能力 + 動態七維思考體系 + 智慧體LOOP反思迭代機制 + Uncensored 去審核特性 + MoziSmartBit混合量化演算法開發而成。

**💡 體積優勢：僅 15.9G 小體積** —— 350 億參數 MoE 模型經自研 MoziSmartBit 智能量化壓縮至 **15.9 GB**（比常規 Q4_K_M ~22GB 小約 30%），一個安裝包即可帶走，普通消費級顯示卡（20GB 顯存起）即可本地部署，雲端 token 成本 = 0，實現 7×24 小時 token 自由並確保本地數據隱私與安全。授權**免費商用**，個人與企業零門檻使用。

---

## 2. 模型特色

### 🧠 動態七維思考體系

MoziAI 自研的核心推理框架。面對任何任務，模型先輸出 **moziAI-Think** 標記，按任務複雜度動態展開結構化思考：

| 級別 | 適用場景 | 典型任務 | 展開維度 |
| --- | --- | --- | --- |
| **Level 0** | 簡單問答 | 術語解釋、事實查詢、翻譯、摘要 | ①理解任務 ⑤資源需求（兩維速答） |
| **Level 1** | 分析診斷 | 市場調研、文案編寫、數據分析、研報解讀、策略評估 | ①②③⑤⑥ 五維評估 |
| **Level 2** | 複雜開發/策略 | 程式開發、架構設計、量化策略開發、多步工作流、系統設計 | ①②③④⑤⑥⑦ 全七維深度推演 |

> 七維：①理解任務 ②複雜度評估 ③依賴關係 ④風險評估 ⑤資源需求 ⑥驗收標準 ⑦執行策略

### 🔄 智慧體 LOOP 迭代機制

複雜任務自動進入 **moziAI-Loop** 迭代模式：**第 1 輪執行+評估 → 第 2 輪調整+驗證**，確保輸出經過自我校驗後才給出最終答案。模型像資深工程師一樣「拆解問題 → 評估方案 → 執行 → 反思 → 優化」，顯著提升複雜任務的準確性和可執行性。簡單問答和任務則自動關閉 Loop。

### 📦 MoziSmartBit 智慧量化

自研分層智慧量化，350 億參數 MoE 模型壓縮至約 **15.9 GB**，比常規 Q4_K_M（~22 GB）小約 6.5 GB（~30%），保持 FP16 **~99%** 精度。傳統量化對所有層使用統一精度，MoziSmartBit 針對 MoE 模型結構特點採用智慧差異化策略，精度優於 Q4_K_M。壓縮比達 **4.5x**。

### 💰 金融垂直領域聚焦

針對金融問答、量化程式設計和工具呼叫的深度優化。金融領域對模型幻覺容忍度極低，MoziAI 在該領域的表現顯著優於同等體積的通用模型。

### 🛡️ Uncensored 去審核特性

無內容審查限制、自由輸出、完整資訊、本地私有。適合學術研究、深度分析、自由討論等場景。（詳見 [第 15 節](#15-去審核-uncensored-優化)）

### 🌐 其他特性

- **多語言支援**：201 種語言和方言，中文能力特別優化
- **通用程式設計**：全棧開發、程式除錯、架構設計，覆蓋 Python/JS/TS/Go/Rust
- **文章寫作**：研報、分析文章、技術文件、創意內容等多體裁高品質寫作
- **視覺理解**：多模態視覺，支援本地截圖理解圖片內容
- **多框架支援**：llama.cpp / Ollama / LM Studio / Jan
- **多 Agent支援**：OpenClaw / Hermes / Cursor / Claude Code / Codex 等，原生工具呼叫與多輪任務編排

---

## 3. 版本升級說明

本次 V3.8 版本採用與 27B-V3.8 同代的自研訓練資料集體系進行重新訓練（身份 / 動態七維思考 / LOOP 迭代 / 金融垂直領域），重點強化了 moziAI 自研的動態七維思考 + LOOP 迭代的推理模式，使其更加智慧識別任務複雜度，複雜任務的完成率更高，提高"先想後做"的能力；同時延續 Uncensored 去審核特性與金融垂直領域深度優化。

moziAI 會保持活躍的版本升級迭代更新頻率，確保緊隨未來人工智慧的發展，並且不斷透過自研技術，讓本地 AI 模型可輕量化部署，能力越來越強。

---

## 4. 核心能力

| 能力領域 | 說明 |
| --- | --- |
| 市場分析 | 宏觀/微觀經濟解讀、A股/港股/美股/商品/加密貨幣行情與邏輯梳理 |
| 財務與研報 | 財報關鍵指標解讀、研報摘要提取、估值與盈利預測輔助 |
| 風控與合規 | 產品風險評估、投資建議合規提示、金融監管政策解讀 |
| 量化與策略 | 量化策略思路設計、金字塔（Pyramid/PEL）量化、回測邏輯、因子構建與工具呼叫 |
| 工具呼叫 | 可接入即時行情、資料庫、研報檢索等金融資料源 |

---

## 5. 技術規格

| 項目 | 參數 |
| --- | --- |
| 底座模型 | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MIT 許可證） |
| 參數規模 | 350 億（35B）MoE 架構，256 個路由專家 + 1 個共享專家，每 token 啟動 8 個專家 |
| 量化方式 | 自研 MoziSmartBit 智慧量化 + GGUF 標準格式 |
| 上下文長度 | 256K（262,144 tokens） |
| 模型體積 | ~15.9 GB |
| 最低顯存 | **20GB+** 可部署（CPU 卸載）；**24GB+** 流暢長上下文；**32GB+** 完整 256K + 視覺 |
| 推理框架 | llama.cpp / Ollama / LM Studio / Jan |
| 推理速度 | 推測解碼下：AMD R9700 顯示卡可達 **140+ token/s** / AMD MAX+395 CPU 內顯可達 **70+ token/s**，實現本地 token 自由輸出 |
| 開發團隊 | 陳雨墨團隊 |

---

## 6. ⚡ 快速開始 3 個文件 = 100% 啟動最佳推理能力

> ⚠️ **核心提示**：MoziAI 的最佳推理能力需要**同時下載 3 個文件**——主模型、視覺投影、聊天模板。缺少任何一個都會損失對應能力。

### 6.1 下載模型文件

在 HuggingFace / ModelScope 下載**這 3 個檔案**到本地同一目錄（主模型在**倉庫根目錄**，視覺投影在 `mmproj/35B/`，聊天模板在 `V3.8/`）：

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← 主模型（必選，15.9 GB）
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← 視覺投影（必選，~1 GB）
moziAI-V3.8-35B-chat-template.jinja                                        ← 聊天模板（必選，含七維思考+Loop指令）
```

| 文件 | 大小 | 必要性 | 作用 |
| --- | --- | --- | --- |
| 主模型 `.gguf` | ~15.9 GB | **必選** | 模型權重，核心推理能力 |
| 視覺投影 `mmproj` | ~1 GB | **必選** | 多模態視覺理解，不載入則喪失圖像能力 |
| 聊天模板 `.jinja` | 微量 | **必選** | 注入 MoziAI 身份 + 七維思考 + LOOP 機制指令 |

### 6.2 啟動並使用

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

瀏覽器開啟 `http://localhost:8080` 即可開始對話。完整推薦參數見第 9 節。

---

## 7. 模型下載

| 平台 | 地址 |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio 使用者**：在 [LM Studio](https://lmstudio.ai) 中搜尋 `moziAI` 一鍵下載，無需手動下載文件。

> 💡 **下載提示**：請點擊上方連結進入 HuggingFace 倉庫，在 **"Files and versions"** 標籤頁，於**倉庫根目錄**下載主模型，再從 `mmproj/35B/` 下載視覺投影、從 `V3.8/` 下載聊天模板，確保三個檔案放在同一目錄下。

---

## 8. 啟動命令

### 最簡啟動（含三件套）

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### 完整推薦啟動

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 \
  --reasoning on --reasoning-format deepseek-legacy \
  --spec-default \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.024 \
  --repeat-penalty 1.05 --presence-penalty 0
```

> 💡 顯存不足時：降低 `-c`（如 131072），或加 `--fit on` 讓 llama.cpp 自動適配顯存。

---

## 9. 推薦推理參數

基於本地實測優化（AMD Radeon AI PRO R9700 32GB）：

| 參數 | 日常任務/文案寫作 | 複雜任務/高級程式設計 | 說明 |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | 日常求穩、複雜程式設計適度探索 |
| top\_p | 0.95 | 0.95 | 核採樣閾值 |
| top\_k | 20 | 20 | 截斷採樣 |
| min\_p | 0.024 | 0.024 | 最小概率過濾 |
| repeat\_penalty | 1.05 | 1.05 | 重複懲罰 |
| presence\_penalty | 0 | 0 | 無存在懲罰 |
| context\_length | 131072 | 262144 | 日常 128K / 複雜 256K（llama.cpp 預設 128K） |
| reasoning | on | on | 開啟推理鏈（思維鏈） |
| reasoning\_budget | 400 | 1000 | 推理預算 token（複雜任務更高） |
| reasoning\_format | deepseek-legacy | deepseek-legacy | 推理輸出到獨立欄位 |
| **spec-type** | **default** | **default** | **推測解碼加速（ngram，MoE 最優，詳見第 11 節）** |
| KV 快取 | q4\_0 | q4\_0 | 量化 KV 快取（統一 kv-unified） |

> 💡 **思考模式**：透過 `--reasoning on` 開啟，模型先進行內部推理再輸出答案。`reasoning_budget` 控制最大思考 token 數。

---

## 10. 量化格式對比

| 格式 | 體積 | 精度 | 說明 |
| --- | --- | --- | --- |
| FP16 原始 | ~70 GB | 100% | 無損，需專業顯示卡 |
| **MoziSmartBit（本模型）** | **~15.9 GB** | **~99%** | **自研智慧量化，精度最優、體積最小** |
| Q4_K_M | ~22 GB | ~98% | GGUF 標準 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 更高精度 |
| Q6_K | ~28.5 GB | ~99.5% | 近無損 |
| Q8_0 | ~36.9 GB | ~100% | 無損 |

> MoziSmartBit 在保持約 99% 精度的同時，將 35B MoE 模型壓縮至 15.9 GB（壓縮比 4.5x），比 Q4_K_M 小約 30%，更適合消費級顯示卡本地部署。

---

## 11. 推測解碼加速 重要特性

本模型透過**推測解碼（Speculative Decoding）**顯著提升推理速度，本地實測比關閉時**提升約 1.5-2 倍**。

- **MoE 最優配置**：llama.cpp 對 MoE 架構推薦使用 **ngram 推測解碼**（`--spec-default`），本地實測最快且穩定
- **模型命名說明**：模型名中的 "MTP" 表示底座自帶的 Multi-Token Prediction 權重（已完整保留），llama.cpp 對 MoE 架構的 MTP draft 支援有限，MoziAI 統一採用 ngram 推測方案獲得最佳實測速度

### 開啟參數

```bash
--spec-default
```

### 參數調整建議

| 配置 | 適用場景 |
| --- | --- |
| --spec-default（預設） | 推薦：平衡速度與顯存 |
| 關閉推測（刪除該參數） | 顯存緊張場景，速度略降 |

---

## 12. 顯存配置推薦

基於 MoziSmartBit 版本（模型 + 視覺共 ~16.4GB）實測：

| 顯存 | 推薦配置 | 說明 |
| --- | --- | --- |
| 20 GB | 上下文 150K，q4\_0 KV 快取，支援視覺 | 模型+視覺共 ~16.4GB，256K+視覺僅佔顯存 ~19.5GB |
| **24 GB** | **256K 滿配，q4\_0 KV 快取，完美支援視覺** | **推薦配置**：視覺+256K 長上下文僅佔顯存 ~20.4GB，餘量 ~3.6GB |
| 32 GB+ | 256K 滿配，顯存餘量充足 | 如 R9700 32GB：視覺+256K 長上下文，餘量 ~10GB，最強配置 |

> 💡 上下文越長，顯存佔用越多。OOM 時逐步降低 `-c` 參數。使用 `--fit on` 讓 llama.cpp 自動調整層數適配顯存。支援 NVIDIA / AMD 全品牌顯示卡。

---

## 13. 部署方式

### Ollama 部署

```bash
cat > Modelfile << 'EOF'
FROM ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 131072
PARAMETER num_gpu 99
EOF

ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan

在 LM Studio / Jan 中搜尋 `moziAI`，選擇 Q4\_K\_M 量化版本下載即可（LM Studio 預設讀取倉庫根目錄模型，歷史版本請使用"從 URL 新增"匯入對應版本目錄檔案，如 `V3.7/`）。

> 💡 Ollama 的 mmproj 和 chat\_template 支援有限，建議優先使用 llama.cpp 獲得完整功能。

---

## 14. 基準評測

MoziAI-35B-V3.8 基於 deepreinforce-ai/Ornith-1.5-35B-A3B 底座微調、蒸餾與二次開發，金融垂直領域為核心優化方向。以下為多模型對比（MoziAI 通用能力與底座 Ornith-1.5-35B-A3B 一致；數據沿用 V3.7 版本實測，V3.8 與 V3.7 同底座同訓練體系）：

| Benchmark | moziAI-35B-V3.8<br>（本模型） | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **程式設計測試** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **推理測試** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **代理測試** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI-35B 金融垂直領域為 MoziAI 的核心優化方向，在財報解讀、量化策略、風控合規、agent 工具呼叫等場景下表現顯著優於通用模型。Gemma-4 / Qwen3.6 數據為官方公開評測結果。

---

## 15. 去審核 Uncensored 優化

本模型繼承底座 Ornith-1.5-35B-A3B 的 Uncensored（去審核）特性，具有以下優勢：

| 優勢 | 說明 |
| --- | --- |
| 無審查限制 | 不會拒絕任何話題，包括敏感、爭議性內容 |
| 自由輸出 | 不受安全策略約束，可生成任何類型的回覆 |
| 完整資訊 | 提供未經過濾的完整資訊，適合研究和分析場景 |
| 本地私有 | 本地部署意味著數據完全私有，不受雲端審查 |

**適用場景**：學術研究、深度分析、自由討論、不受限的 AI 對話格局。

**注意**：本模型為本地部署模型，輸出內容完全由使用者控制，不承擔內容審核責任。

---

## 16. 許可證

本模型採用**自定義限制性許可證**：

- ✅ **允許** — 免費商業使用、複製和分發
- ❌ **禁止** — 二次開發、轉售販賣、再許可
- 📋 **要求** — 保留原始版權聲明，註明來源：moziAI-35B

本模型按「原樣」提供，不提供任何形式的保證。模型輸出僅供參考，不構成投資建議。使用者需自行承擔使用風險。

詳細條款請參閱 [LICENSE](LICENSE) 文件。

---

## 17. 聯絡方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. All rights reserved.