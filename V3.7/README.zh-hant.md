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

library_name: llama-cpp

pipeline_tag: text-generation

---



# MoziAI-V3.7-35B-A3B-MOE - 可免費本地部署的小而強的多模態AI模型



[English](README.en.md) | [简体中文](README.zh.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)



## 模型簡介



MoziAI-35B-A3B-MOE 是由中國財經大V陳雨墨團隊開發的本地開源多模態AI大模型（增強金融領域、支持視覺、工具調用、消費級顯卡本地部署），moziAI-35B 基於開源底座 Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MIT 許可），結合陳雨墨團隊自主研發的：（金融數據 + 金融領域能力 + 訓練方法 + 七維思考體系 + 智能體LOOP機制 + 混合量化算法 MoziSmartBit）開發而成。通過自研的 MoziSmartBit 智能量化 技術，將350億參數MoE模型壓縮至約 15.5 GB，比常規Q4_K_M量化約22+GB的模型體積小了6.5G（約30%）；在精度與體積間取得最優平衡，實現幾乎≈FP16 的 99%的精度質量。通過自研的 MoziSmartBit 智能量化 技術，將350億參數MoE模型壓縮至約 15.5 GB，比常規Q4_K_M量化約22+GB的模型體積小了6.5G（約30%）；在精度與體積間取得最優平衡，實現幾乎≈FP16 的 99%的精度質量。



本模型除了保留AI大模型的通用能力外，還增強了：金融垂直領域應用，金融問答、量化編程、工具調用和通用編程，模型的七維思考能力、LOOP機制、兼容各種agent平台調用。



模型研發者陳雨墨常把本模型用於本地金融數據分析、量化策略研發、市場調研、任何的文章編寫、整體項目推進、通用程式編寫，openclaw/hermes執行256K上下文的任務。因本地消費級顯卡可部署使用，節約大量雲端token成本，實現X24小時token自由並且確保本地數據隱私與安全策



支持 llama.cpp、Ollama、LM Studio 等主流推理框架構



**發佈日期：2026-08-21** | **版本：V3.7**



## 模型特色



- **金融垂直深度**：深度加強金融問答、量化程式編寫、工具調用能力

- **MoziSmartBit 智能量化**：自研的智能量化技術，精度與體積最佳平衡，模型幾乎無損壓縮至約 **15.5 GB**

- **消費級部署**：20GB / 4GB顯存以上的家用消費級顯卡即可本地部署，支持最優256K 長上下文推理

- **多語言支持**：支援201 種語言和方言，中文能力特別優化，兼顧英語、日語、韓語、德語、法語、西班牙語、葡萄牙語等主流語言

- **通用程式編寫能力**：支持全棧開發、代碼調試、架構設計、腳本編寫，覆蓋 Python/JS/TS/Go/Rust 等主流語言

- **文章寫作能力**：支持多體裁高質量寫作，包括研報、分析文章、技術文檔、創意內容等

- **視覺理解**：支持多模態視覺，可本地截圖進入聊天窗口，模型能夠看懂圖片內資訊

- **去審核自由輸出**：無內容審查限制，可自由討論任何話題，不受安全策略約束

- **推理邏輯增強**：配合推理邏輯（思維鏈）進行訓練，進一步提升推理質量

- **多框架支援**：兼顧llama.cpp、Ollama、LM Studio、Jan 等主流推理框架

- **多 Agent 平台支持**：深度適合OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex 等國內外主流 AI IDE 與 Agent 框架，原生支持工具調用與多輪任務編排，開箱即可



## 去審核（Uncensored）優化



本模型繼承底座Ornith-1.5-35B-A3B 的 Uncensored（去審核）特性，具有以下優勢：

| 優勢    | 說明                    |
| ----- | --------------------- |
| 無審查限制| 不會拒絕任何話題，包括敏感、爭議性內容  |
| 自由輸出  | 不受安全策略約束，可生成任何類型的回復  |
| 完整資訊  | 提供未經過濾的完整資訊，適合研究和分析場景|
| 本地私有  | 本地部署意味著數據完全私有，不受雲端審查  |
**適用場景**：學術研究、深度分析、自由討論、不受限的AI對話格

**注意**：本模型為本地部署模型，輸出內容完全由使用者控制，不承擔內容審核責任務



## 核心能力



| 能力領域  | 說明                                         |
| ----- | ------------------------------------------ |
| 市場分析  | 宏觀/微觀經濟解讀、A 股/港股/美股/商品/加密貨幣行情與邏輯梳理         |
| 財務與研的| 財報關鍵指標解讀、研報摘要提取、估值與盈利預測輔助                  |
| 風控與合規| 產品風險評估、投資建議合規提示、金融監管政策解讀                   |
| 量化與策略| 量化策略思路設計、金字塔（Pyramid/PEL）量化、回測邏輯、因子構建與工具調用 |
| 工具調用  | 可接入實時行情、數據庫、研報檢索等金融數據隱                    |
## 技術規劃



| 項目     | 參數                                                                                 |
| ------ | ---------------------------------------------------------------------------------- |
| 底座模型   | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MIT 許可證                       |
| 參數規模   | 350億（35B）MoE 架構建56 個路由專家+ 1 個共享專家，不token 激活 8 個專家                              |
| 量化方式   | 採用自研 MoziSmartBit 智能量化算法 + GGUF 標準格式                                               |
| 上下文長上 | 256K（262,144 tokens）                                                             |
| 模型體積   | \~15.5 GB（MoziSmartBit Uncensored 版本地                                             |
| 最低顯存要求| 20GB顯存以上的家用消費級顯卡（如 RTX 3060 12G 需搭配 CPU 卸載，RTX 4060 Ti 16G 等），推理24 GB（含視覺 + 長上下文件|
| 推理框架   | llama.cpp / Ollama / LM Studio / Jan                                               |
| 推理速度   | 透過算法優化，AMD R9700顯卡可達140+token/s / AMD MAX+395CPU核顯可達70+token/s ,實現本地token自由輸出       |
| 開發團隊   | 陳雨墨團隊                                                                             |
## 量化格式與模型體積對話



| 量化格式             | 模型體積          | 精度保持      | 說明                |
| ---------------- | ------------- | --------- | ----------------- |
| FP16（原始）         | \~70 GB       | 100%      | 原始 16bit 精度       |
| **MoziSmartBit** | **\~15.5 GB** | **\~99%** | **本模型採用自研智能量化方式** |
| Q4\_K\_M         | \~22 GB     | \~98%     | GGUF 標準 4bit      |
| Q5\_K\_M         | \~24.7 GB     | \~99%     | 更高精度              |
| Q6\_K            | \~28.5 GB     | \~99.5%   | 近無損              |
| Q8\_0            | \~36.9 GB     | \~100%    | 無損失              |
> MoziAI V3.7 採用 MoziSmartBit 智能量化方案，在保持约99% 精度的同時，将350亿参数MoE模型压缩至约 15.5 GB，压缩比达4.5x，兼顧推理質量與部署門檻，更適合消費級顯卡本地部署的



## MoziSmartBit 智能量化技術



傳統量化方案對所有層使用統一精度，而陳雨墨團隊自研的**MoziSmartBit 智能量化** 針對 MoE 模型的結構特點，採用智能差異化量化策略，在體積與精度間取得最優平衡，模型質量高於 Q4\_K\_M 格式，同時體積僅占15.5 GB，壓縮比達 4.5x。



### 壓縮效果



傳統量化方案對模型所有部分統一壓縮，往往導致精度損失明顯。MoziSmartBit 智能量化採用自研的智能壓縮策略，**在極小的精度損失下實現大幅體積縮小**。- **量化精度損失極小**：訓練增益> 量化損失，訓練後的MoziAI-35B 在金融領域文本上下PPL 優於訓練前的 bf16 底座，降低了同類 AI 模型的幻覺與困惑。- **模型體積壓縮至 4.5 倍**：從 FP16（~70 GB 壓縮至\~15.5 GB，也大幅小於Q4\_K\_M的\~21 GB，大幅降低顯存與存儲門檻

- **消費級顯卡可部署**：原本需要高端顯卡的 35B MoE 大模型，現在 20GB\~24GB 顯存即可流暢部署



### 對比優勢



**vs Q4\_K\_M（~22 GB）**：體積減少約 30%（\~15.5 GB），精度優Q4\_K\_M **更高**，顯存門檻更低，中端消費級顯卡（24GB）即可流暢部署的



**vs 原始 FP16（~70 GB）**：體積壓縮約 4.5 倍，訓練有效 + 量化精度損失極小（訓練增益> 量化損失），從需要專業級顯卡即4GB+）降低到消費級顯卡即可本地運行256K 長上下文件



## 推薦推理參數



基於本地運行配置（AMD Radeon AI PRO R9700 32GB），推薦參數如下文



| 參數                | 推薦配                             | 說明                     |
| ----------------- | -------------------------------- | ---------------------- |
| temperature       | 0.6                              | 平衡創意與準確保              |
| top\_p            | 0.95                             | 核採樣閾值                 |
| top\_k            | 20                               | 截斷採樣          |
| repeat\_penalty   | 1.05                             | 重複懲罰                   |
| presence\_penalty | 0                                | 無存在懲罰                 |
| context\_length   | 262144                           | 256K 長上下文              |
| batch\_size       | 2048                             | 批處理大模                 |
| ubatch\_size      | 512                              | 微批次大模                 |
| flash\_attention  | auto                             | 自動 Flash Attention     |
| kv\_cache         | q4\_0                            | KV 緩存量化（統一 kv-unified）|
| poll              | 0                                | 閒置不輪任GPU，節能低延遲        |
| reasoning         | on                               | 開啟推理鏈（思維鏈）             |
| reasoning\_budget | 400                              | 推理預算 token |          |
| reasoning\_format | deepseek-legacy                  | 推理格式                   |
| samplers          | top\_k;top\_p;temperature;typ\_p | 採樣器順序                 |
### llama.cpp 啟動命令



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

  --host 0.0.0.0 --port 8080 \

  --temp 0.6 --top-p 0.95 --top-k 20

```



### 不同顯存配置推薦



由於使用者顯卡配置差異較大，以下為不同顯存下的推薦參數（均為 MoziSmartBit 版本）：



| 顯存     | 推薦上下文長上| KV 緩存 | 視覺支持 | 說明                                   |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB  | 150K    | q4\_0 | 支持   | 模型+視覺共\~16.4GB，實現00K+視覺僅佔顯存\~19.5GB |
| 24 GB  | 256K 滿配 | q4\_0 | 完美支持 | 視覺+256K長上下文,僅佔顯存\~20.4GB，顯存餘量\~3.6GB |
| 32 GB+ | 256K 滿配 | q4\_0 | 完美支持 | 視覺+256K長上下文，顯存餘量充足\~10GB，最強配置       |
**NVIDIA 顯卡參考表**



| 顯存    | 顯卡型號                   |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090               |
**AMD 顯卡參考表**



| 顯存    | 顯卡型號                |
| ----- | ------------------- |
| 20 GB | RX 7900 XT          |
| 24 GB | RX 7900 XTX         |
| 32 GB | Radeon AI PRO R9700 |
**Intel 顯卡參考表**



| 顯存    | 顯卡型號                      |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60               |
| 16 GB | Arc Pro B50（需搭配 CPU 卸載入  |
**CPU共享記憶體核顯設備參考表**



| 顯存     | 處理器型號                                 |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S 核顯存|
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU）   |
> 💡 **提示**：只要顯存滿足以上要求即可使用，不限品牌型號，支援NVIDIA / AMD / Intel 各品牌獨立顯卡，也支持上下128GB 統一記憶體的核顯 CPU。> 💡 **提示**：上下文越長，佔用顯存越多。如果出現顯存不足（OOM），請逐步降低 `-c` 參數值。使用`--fit on` 參數可讓 llama.cpp 自動調整層數適配顯存的



### Ollama 部署



```bash

# 建立 Modelfile

FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf



PARAMETER temperature 0.6

PARAMETER top_p 0.95

PARAMETER top_k 20

PARAMETER num_ctx 262144

PARAMETER num_gpu 99



# 建置並運行

ollama create moziAI-35B -f Modelfile

ollama run moziAI-35B

```



### LM Studio / Jan 部署



直接在LM Studio / Jan 中搜索`moziAI-35B`，選擇MoziSmartBit 量化版本下載即可證



## 基準評測



MoziAI 基於 deepreinforce-ai/Ornith-1.5-35B-A3B 底座微調、蒸餾與二次開發。MoziAI 在底座基礎上針對金融垂直領域優化，在金融問答、量化程式編寫、工具調用等場景下表現更出色。以下為多模型對比（MoziAI-35B 通用能力與底座Ornith-1.5-35B-A3B 一致）底



| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **程式設計** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **推理** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **代理式** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |
> MoziAI-35B 通用能力基準分數與底座Ornith-1.5-35B-A3B 一致。金融垂直領域為 MoziAI 的核心優化方向，在財報解讀、量化策略、風控合規、agent管理工具調用等場景下表現顯著優於通用模型。Gemma4 / Qwen3.6 數據為官方公開評測結果取



## 模型下載



由於模型文件較大（\~15.5 GB），模型權重託管於多個社群平台：



| 平台             | 地址                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| HuggingFace    | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub         | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio 用戶**：可直接在[LM Studio](https://lmstudio.ai) 中搜索`moziAI` 並一鍵下載，無需手動下載檔案對

> 💡 **下載提示**：請點擊上方連結進入 HuggingFace 倉庫，在 **"Files and versions"** 標籤頁下文V3.7 目錄下的所有文件（主模型、視覺投影、聊天模板），確保三個文件放在同一目錄下



⚠️ **重要：視覺能力需要額外載入mmproj 文件**



本模型支持多模態視覺，視覺投影文件（mmproj）已包含在版本目錄中文



- **視覺文件**：`moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`（約 903 MB，BF16 精度優

- **放置位置**：與 GGUF 模型文件放在同一版本目錄下

- **載入方式**：啟動llama-server 時透過 `--mmproj` 參數載入



```bash

llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf

```



> 不載入視覺文件將喪失圖像理解能力，僅保留純文本對話能力時



## 快速開發



### 1. 下載模型文件



在 HuggingFace / ModelScope 下載 V3.7 目錄下的所有文件到本地部



```

V3.7/

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # 主模型（必選擇

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # 視覺投影（可選）

└── moziAI-V3.7-35B-chat-template.jinja                  # 聊天模板（推薦）

```



### 2. 啟動推理服務



完整的推薦配置啟動命令請參考上下[llama.cpp 啟動命令](#llamacpp-啟動命令) 章節約



最簡啟動（僅核心參數）底



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 262144 -ngl 99

```



> 需要視覺能力時加上 `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`



### 3. 開始使用



瀏覽器打開`http://localhost:8080` 即可開始對話格



### 目錄結構



```

moziAI-35B/

├── README.md              # 本文件（中文說明書）

├── README.en.md           # 說明書的英文版本

├── LICENSE                # 許可證

├── V3.7/                  # V3.7 版本（版本自包含在

├  ├── RELEASE_NOTES.md                       # 版本更新說明

├  ├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # 主模型

├  ├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # 視覺投影

├  └── moziAI-V3.7-35B-chat-template.jinja   # 聊天模板

```



未來升級計劃詳見 [未來升級計劃.md](未來升級計劃.md）。



## SEO 關鍵能



金融AI大模型、AI大模型、本地開源模型、端側模型、量化程式編寫、MoziSmartBit、智能量化、GGUF量化、MoE模型、本地開源大模型、本地部署、金融AI、工具調用、Agent、llama.cpp、Ollama、GGUF、Uncensored（去審核）、無審查、免審核、自由輸出、Q3\_K\_M、Q4\_K\_M、Q5\_K\_M、Q6\_K、Q8\_0、Ornith-1.5-35B-A3B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、金融垂直領域、開源模型



## 許可證（重要事項



本模型採用**自定義限制性許可證**，具體條款如下：



✅**允許**



- 免費商業使用：可免費整合到您的商業產品或服務能

- 複製和分發：可原樣複製、下載、分析



❌**禁止**



- 二次開發：不得修改、翻譯、改編、合併、微調本模型或其任何部分

- 轉售售賣：不得將本模型單獨或作為產品組成部分進行售賣

- 再許可：不得就本模型授予任何從屬許可



📋 **要求**



- 使用時必須保留原始版權聲明

- 註明來源：moziAI-35B



詳細許可證條款請參閱 [LICENSE](LICENSE) 文件放



## 免責聲明



本模型按「原樣」提供，不提供任何形式的保證。模型輸出僅供參考，不構成投資建議。使用者需自行承擔使用風險評



## 聯絡方式



- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)

- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)

- **微博**：[@rimochen](https://weibo.com/rimochen)

- **E-mail**：263515@qq.com>






Copyright (c) 2026 陳雨墨/ chenyumo166. All rights reserved.