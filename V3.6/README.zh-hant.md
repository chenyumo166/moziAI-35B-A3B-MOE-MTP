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

# moziAI-35B-V3.6-A3B-MOE-MTP-Uncensored - 可免費本地部署的小而強的多模態AI模型

Language / 語言選擇  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## 模型簡介

MoziAI-35B-A3B-MOE 是由中國財經大V陳雨墨團隊開發的本地開源多模態AI大模型（增強金融領域、支持視覺、工具調用、消費級顯卡本地部署），moziAI-35B 基於開源底座 Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MIT 許可），結合陳雨墨團隊自主研發的：（金融數據 + 金融領域能力 + 訓練方法 + 七維思考體系 + 智能體LOOP機制 + 混合量化算法 MoziSmartBit）開發而成。通過自研的 MoziSmartBit 智能量化 技術，將350億參數MoE模型壓縮至約 15.5 GB，比常規Q4_K_M量化約22+GB的模型體積小了6.5G（約30%）；在精度與體積間取得最優平衡，實現幾乎≈FP16 的 99%的精度質量。

本模型研發團隊的理念就是讓綜合能力強大的本地AI大模型智慧體可走入千家萬戶與中小企業，不再需要支付高昂的AI硬體成本或雲端API成本。通過自研的**MoziSmartBit 智慧量化** 技術，將 350 億參數的 MoE 模型壓縮至約 **15.5 GB**，在模型精度與體積間取得最優平衡，實現幾乎≈FP16 的 99% 的精度質量。本模型具有350億參數，但是採用MOE稀疏專家技術而獲得只調用30億參數並支援MTP推測解碼的加速推理能力，實測可在20G顯存的家用消費級顯卡完成本地免費部署也可擁有140+ token/s的推理速度，推理速度優於眾多雲端收費AI大模型。

本模型除了保留通用AI大模型的能力，重點優化：金融垂直領域的應用，金融問答、量化編程、通用編程、工具調用、256K複雜長上下文任務的成功率等AI大模型關鍵能力。可在本地消費級顯卡免費部署使用，節約大量雲端token成本，實現 7X24小時token自由並且確保本地數據隱私與安全。

**發佈日期：** 2026-08-20 | **版本：V3.6**

## 模型下載

由於模型文件較大（~15.5 GB），模型權重託管於多個社區平臺：

| 平台 | 位址 |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio 使用者**：可直接在 [LM Studio](https://lmstudio.ai) 中搜索 `moziAI` 並一鍵下載，無需手動下載文件。  
> 💡 **下載提示**：請點擊上方連結進入 HuggingFace 倉庫，在 **"Files and versions"** 標籤頁下載 V3.6 目錄下的所有文件（主模型、視覺投影、聊天範本），確保三個文件放在同一目錄下。

### ⚠️ 重要：視覺能力需要額外添加 mmproj 文件

本模型支援多模態視覺，視覺投影文件（mmproj）已包含在版本目錄中：

- **視覺文件**：`mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf`（約 903 MB，BF16 精度）
- **放置位置**：與 GGUF 模型文件放在同一版本目錄
- **載入方式**：啟動 llama-server 時通過 `--mmproj` 參數載入

> 不載入視覺文件將喪失圖像理解能力，僅保留純文字對話能力。

### ⚠️ 重要：必須載入聊天範本文件

本模型使用專屬的聊天範本（chat-template），**不載入將導致對話格式錯誤、推理鏈失效、回復品質大幅下降**。聊天範本文件已包含在版本目錄中：

- **範本文件**：`moziAI-V3.6-35B-chat-template.jinja`（約 5 KB，jinja 格式）
- **放置位置**：與 GGUF 模型文件放在同一版本目錄
- **載入方式**：啟動 llama-server 時通過 `--chat-template-file` 參數載入

> 不載入聊天範本，模型可能無法正確識別系統提示、用戶消息和思考區塊，導致輸出格式混亂或推理能力下降。

### llama.cpp 啟動命令（20G+顯卡開256K上下文的推薦配置）

> 備註：如顯存低於 20G，則減少 `-c 262144` 的上下文設置參數 262144。

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --spec-default \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

## 快速開始

### 1. 下載模型文件

從 HuggingFace / ModelScope 下載 V3.6 目錄下的所有文件到本地：

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # 主模型（必選）
├── moziAI-35B-mmproj-BF16-V1.0.gguf  # 視覺投影（可選，需視覺能力時下載）
└── moziAI-V3.6-35B-chat-template.jinja                  # 聊天範本（必選！不載入會導致對話格式錯誤）
```

> ⚠️ **聊天範本是必選文件**，不是可選。本模型有自訂的對話格式（含推理鏈/思考區塊），缺失範本將導致模型輸出格式混亂、推理能力失效。請務必下載並在啟動時載入。

### 2. 啟動推理服務

完整的推薦配置啟動命令請參考下文 [llama.cpp 啟動命令](#llamacpp-啟動命令) 章節。

最簡啟動（僅核心參數）：

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 需要視覺能力時加上 `--mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf`

### 3. 開始使用

瀏覽器打開 `http://localhost:8080` 即可開始對話。

### 目錄結構

```
moziAI-35B/
├── README.md              # 英文說明書
├── README.zh.md           # 簡體中文說明書
├── README.zh-hant.md      # 本文件（繁體中文說明書）
├── LICENSE                # 許可證
├── V3.6/                  # V3.6 版本（版本自包含）
│   ├── RELEASE_NOTES.md                       # 版本更新說明
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # 主模型
│   ├── moziAI-35B-mmproj-BF16-V1.0.gguf # 視覺投影
│   └── moziAI-V3.6-35B-chat-template.jinja   # 聊天範本
```

## 模型特色

- **MoziSmartBit 智慧量化**：自研的智慧量化技術，精度與體積最佳平衡，模型幾乎無損壓縮至約 **15.5 GB**
- **複雜長任務能力**：訓練讓模型智慧體為任務自動規劃的智慧循環處理卡點與自我思考機制，實現複雜任務的自動執行與自我調整，擺脫人類用戶不斷給智慧體優化提示詞的麻煩
- **小模型大能力**：在執行複雜任務上，綜合能力跑贏同類350億參數以內的模型，甚至跑贏部分比自己參數大幾倍的模型
- **MOE+MTP的速度優勢**：雖然模型整體是350億參數，但實際只調用8+1專家，共30億參數，推理速度更快，很適合20GB~24GB顯存的家用消費級顯卡即可本地部署並享受 140+ token/s的推理速度
- **金融垂直深耕**：深度加強金融問答、量化編程、工具調用能力
- **消費級部署**：20GB~24GB顯存以上的家用消費級顯卡即可本地部署，支援最大 256K 長上下文推理
- **多語言支援**：支援 201 種語言和方言，中文能力特別優化，兼顧英、日、韓、德、法、葡等主流語言
- **通用編程能力**：支援全棧開發、代碼調試、架構設計、腳本編寫，覆蓋 Python/JS/TS/Go/Rust 等主流語言
- **文章寫作能力**：支援多體裁高品質寫作，包括研報、分析文章、技術文檔、創意內容等
- **視覺理解**：推理框架載入視覺文件即可支援多模態視覺，可本地截圖進入聊天視窗，模型能夠看懂圖片內資訊
- **去審核自由輸出**：無內容審查限制，可自由討論任何話題，不受安全策略約束
- **推理邏輯增強**：配合推理邏輯（思維鏈）進行訓練，進一步提升推理品質
- **多框架支援**：相容 llama.cpp、Ollama、LM Studio、Jan 等主流推理框架
- **多Agent 平台支援**：深度適配 OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex 等國內外主流 AI IDE 與 Agent 框架，原生支援工具調用與多輪任務編排，開箱即用

## 去審核（Uncensored）優勢

本模型繼承底座 Ornith-1.0-35B-A3B 的 Uncensored（去審核）特性，具有以下優勢：

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>優勢</th>
<th>說明</th>
</tr>
</thead>
<tbody>
<tr>
<td>無審查限制</td>
<td>不會拒絕任何話題，包括敏感、爭議性內容</td>
</tr>
<tr>
<td>自由輸出</td>
<td>不受安全策略約束，可生成任何類型的回復</td>
</tr>
<tr>
<td>完整資訊</td>
<td>提供未經過濾的完整資訊，適合研究和分析場景</td>
</tr>
<tr>
<td>本地私有</td>
<td>本地部署意味著數據完全私有，不受雲端審核</td>
</tr>
</tbody>
</table>

> **適用場景**：免費商用、學術研究、深度分析、自由討論、不受限的AI對話
> **注意**：本模型為本地部署模型，輸出內容完全由用戶控制，不承擔內容審核責任。

## 核心能力

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>能力領域</th>
<th>說明</th>
</tr>
</thead>
<tbody>
<tr>
<td>市場分析</td>
<td>宏觀/微觀經濟解讀、A 股/港股/美股/商品/加密貨幣行情與邏輯梳理</td>
</tr>
<tr>
<td>財務與研報</td>
<td>財報關鍵指標解讀、研報摘要提取、估值與盈利預測輔助</td>
</tr>
<tr>
<td>風控與合規</td>
<td>產品風險評估、投資建議合規提示、金融監管政策解讀</td>
</tr>
<tr>
<td>量化與策略</td>
<td>量化策略思路設計、金字塔（Pyramid/PEL）量化、回測邏輯、因子構建與工具調用</td>
</tr>
<tr>
<td>工具調用</td>
<td>可接入即時行情、數據庫、研報檢索等金融數據</td>
</tr>
</tbody>
</table>

## 技術規格

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>項目</th>
<th>參數</th>
</tr>
</thead>
<tbody>
<tr>
<td>底座模型</td>
<td>Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 架構，MIT 許可證）</td>
</tr>
<tr>
<td>參數規模</td>
<td>350億（35B）MoE 架構，256 個路由專家 + 1 個共享專家，每個 token 啟用 8 個專家</td>
</tr>
<tr>
<td>量化方式</td>
<td>採用自研 MoziSmartBit 智慧量化演算法 + GGUF 標準格式</td>
</tr>
<tr>
<td>上下文長度</td>
<td>256K (262,144 tokens)</td>
</tr>
<tr>
<td>模型體積</td>
<td>~15.5 GB（MoziSmartBit Uncensored 版本）</td>
</tr>
<tr>
<td>最低顯存要求</td>
<td>20GB顯存以上的家用消費級顯卡（如 RTX 3060 12G 需搭配 CPU 卸載，RTX 4060 Ti 16G 等），推薦 24 GB（含視覺 + 長上下文）</td>
</tr>
<tr>
<td>推理框架</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>推理速度</td>
<td>通過演算法優化，AMD Radeon AI PRO R9700 顯卡可達 140+token/s / AMD Ryzen AI Max+ 395 核顯可達 70+token/s，實現本地自由推理輸出</td>
</tr>
<tr>
<td>開發團隊</td>
<td>陳雨墨團隊</td>
</tr>
</tbody>
</table>

## 量化格式與模型體積對比

| 量化格式 | 模型體積 | 精度保持 | 說明 |
| ---------------- | ------------- | --------- | ----------------- |
| FP16（原始） | ~70 GB | 100% | 原始 16bit 精度 |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **本模型採用自研智慧量化方案** |
| Q4_K_M | ~22 GB | ~98% | GGUF 標準 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 更高精度 |
| Q6_K | ~28.5 GB | ~99.5% | 近無損 |
| Q8_0 | ~36.9 GB | ~100% | 無損 |
> MoziAI V3.6 採用 MoziSmartBit 智慧量化方案，在保持 ~99% 精度的同時，將 350 億參數的 MoE 模型壓縮至約 15.5 GB，壓縮比 ~4.5x，兼顧推理品質與部署門檻，更適合消費級顯卡本地部署。

## MoziSmartBit 智慧量化技術

傳統量化方案對所有層使用統一精度，而陳雨墨團隊自研的**MoziSmartBit 智慧量化** 針對 MoE 模型的結構特點，採用智慧差異化量化策略，在體積與精度間取得最優平衡，模型品質高於 Q4_K_M 格式，同時體積僅 ~15.5 GB，壓縮比 ~4.5x。

### 壓縮效果

傳統量化方案對模型所有部分統一壓縮，往往導致精度損失明顯。MoziSmartBit 智慧量化採用自研的智慧壓縮策略，**在極小的精度損失下實現大幅體積壓縮**：

- **量化精度損失極小**：訓練增益 > 量化損失，訓練後的 MoziAI-35B 在金融領域文字上的 PPL 優於訓練前的 bf16 底座，降低了同類 AI 模型的幻覺與困惑
- **模型體積壓縮 4.5 倍**：從 FP16 的 ~70 GB 壓縮到 ~15.5 GB，也大幅小於Q4_K_M的~22 GB，大幅降低顯存與存儲門檻
- **消費級顯卡可運行**：原本需要高端顯卡的 35B MoE 大模型，現在 20GB~24GB 顯存即可流暢部署

### 對比優勢

**vs Q4_K_M（~22 GB）**：體積減少約 30%（~15.5 GB），精度比 Q4_K_M **更高**，顯存門檻更低，中端消費級顯卡（20GB）即可流暢部署。

**vs 原始 FP16（~70 GB）**：體積壓縮約 4.5 倍，訓練有效 + 量化精度損失極小（訓練增益 > 量化損失），從需要專業級顯卡（48GB+）降低到消費級顯卡即可本地運行 256K 長上下文。

## 推薦推理參數

基於本地運行配置（AMD Radeon AI PRO R9700 32GB），推薦參數如下：

| 參數 | 推薦值 | 說明 |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | 平衡創意與準確性 |
| top_p | 0.95 | 核採樣閾值 |
| top_k | 20 | 截斷採樣 |
| repeat_penalty | 1.05 | 重複懲罰 |
| presence_penalty | 0 | 無存在懲罰 |
| context_length | 262144 | 256K 長上下文 |
| batch_size | 2048 | 批次處理大小 |
| ubatch_size | 512 | 微批次大小 |
| flash_attention | auto | 自動 Flash Attention |
| kv_cache | q4_0 | KV 快取量化（統一 kv-unified） |
| poll | 0 | 空閒不輪詢 GPU，節能低延遲 |
| reasoning | on | 開啟推理鏈（思維鏈） |
| reasoning_budget | 400 | 推理預算 token 數量 |
| reasoning_format | deepseek-legacy | 推理格式 |
| samplers | top_k;top_p;temperature;typ_p | 採樣器順序 |
### 不同顯存配置推薦

由於用戶顯卡配置差異較大，以下為不同顯存下的推薦參數（均為 MoziSmartBit 版本）：

| 顯存 | 推薦上下文長度 | KV 快取 | 視覺支援 | 說明 |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | 支援 | 模型+視覺共~16.4GB，實測 128K+視覺僅占顯存~19.5GB |
| 24 GB | 256K 滿配 | q4_0 | 完美支援 | 視覺+256K長上下文,僅占顯存~20.4GB，顯存餘量~3.6GB |
| 32 GB+ | 256K 滿配 | q4_0 | 完美支援 | 視覺+256K長上下文，顯存餘量充足~10GB，最強配置 |
**NVIDIA 顯卡參考表**

| 顯存 | 顯卡型號 |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD 顯卡參考表**

| 顯存 | 顯卡型號 |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel 顯卡參考表**

| 顯存 | 顯卡型號 |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50（需搭配 CPU 卸載） |
**CPU共用記憶體核顯 設備參考表**

| 顯存 | 處理器型號 |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S 核顯） |
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU） |
> 💡 **提示**：只要顯存滿足以上要求即可使用，不限品牌型號，支援 NVIDIA / AMD / Intel 各品牌獨立顯卡，也支援帶有 128GB 統一記憶體的核顯/CPU。
>
> 💡 **提示**：上下文越長，佔用顯存越多。如果出現顯存不足（OOM），請逐步降低 `-c` 參數值。使用 `--fit on` 參數可讓 llama.cpp 自動調整層數適配顯存。

### Ollama 部署

```bash
# 建立 Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# 構建並運行
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan 部署

直接在 LM Studio 或 Jan 中搜索 `moziAI-35B`，選擇量化版本下載即可。

## 基準評測

moziAI-35B-V3.6 基於 **Ornith-1.0-35B**（deepreinforce-ai）底座微調。MoziAI 在底座優秀的智慧體編碼能力基礎上，新增**金融垂直領域深度優化**，在金融問答、量化編程、工具調用等場景下表現更出色。通用能力與 Ornith-1.0-35B 底座保持一致。

| Benchmark | moziAI-35B-V3.6 | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
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
**Terminal-Bench 2.1 (Terminus-2)**：使用 Harbor/Terminus-2 框架評測，配置 `parser=json`，`temperature=1.0`，`top_p=1.0`，128K 上下文視窗。每次運行 4 小時超時，32 核 48GB 記憶體，結果取 5 次平均。  
**Terminal-Bench 2.1 (Claude Code)**：使用 Claude Code 2.1.126 評測，配置 `parser=json`，`temperature=1.0`，`top_p=1.0`，`max_new_tokens=131072`。結果取 5 次平均。  
**SWE-bench Verified, Pro and Multilingual**：使用 OpenHands 框架評測，配置 `temp=1.0`，`top_p=0.95`，256K 上下文視窗。  
**NL2Repo**：配置 `temperature=1.0`，`top_p=1.0`，400K 上下文，48K 輸出。  

> MoziAI-35B 完整繼承了 Ornith-1.0-35B 優秀的智慧體編碼能力。MoziAI 的核心差異化在於**金融垂直領域深度優化**，在財報分析、量化策略、風控合規、智慧體工具調用等場景下，表現顯著優於通用模型。

## SEO 關鍵字

金融AI大模型、AI大模型、本地開源模型、端側模型、量化編程、MoziSmartBit、智慧量化、GGUF量化、MoE模型、本地開源大模型、本地部署、金融AI、工具調用、Agent、llama.cpp、Ollama、GGUF、Uncensored（去審核）、無審查、免審核、自由輸出、Q3_K_M、Q4_K_M、Q5_K_M、Q6_K、Q8_0、Ornith-1.0-35B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、金融垂直領域、開源模型。

## 許可證（重要）

本模型採用 **自訂限制性許可證**，具體條款如下：

✅ **允許**

- 免費商業使用：可免費整合到您的商業產品或服務
- 複製和分發：可原样複製、下載、分發

詳細許可證條款請參閱 [LICENSE](../LICENSE) 文件。

## 免責聲明

本模型按"原样"提供，不提供任何形式的保證。模型輸出僅供參考，不構成投資建議。使用者需自行承擔使用風險。

## 聯繫方式

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com


Copyright (c) 2026 陳雨墨 / chenyumo166. All rights reserved.