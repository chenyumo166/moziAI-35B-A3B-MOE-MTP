---
language:
- ja
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

# MoziAI-35B-V3.8 — 無料でローカル導入できる小型・高能力のマルチモーダル AI モデル

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | 日本語 | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

**公開日：2026-09-01** · **バージョン：V3.8**

---

## 📑 目次

- [1. モデル概要](#1-モデル概要)
- [2. 特徴](#2-特徴) — 動的7次元思考 / LOOP / MoziSmartBit / 金融特化
- [3. バージョンアップ情報](#3-バージョンアップ情報)
- [4. コア能力](#4-コア能力)
- [5. 技術仕様](#5-技術仕様)
- [6. ⚡ クイックスタート](#6--クイックスタート3ファイル--100-最適な推論を有効化) — **3ファイル一式**
- [7. モデルダウンロード](#7-モデルダウンロード)
- [8. 起動コマンド](#8-起動コマンド)
- [9. 推奨推論パラメータ](#9-推奨推論パラメータ)
- [10. 量子化形式比較](#10-量子化形式比較)
- [11. 投機的デコード高速化](#11-投機的デコード高速化重要機能)
- [12. VRAM設定推奨](#12-vram設定推奨)
- [13. 導入方法](#13-導入方法)
- [14. ベンチマーク](#14-ベンチマーク)
- [15. Uncensored（検閲なし）最適化](#15-uncensored検閲なし最適化)
- [16. ライセンス](#16-ライセンス)
- [17. 連絡先](#17-連絡先)

---

## 1. モデル概要

MoziAI-35B-V3.8 は、中国の金融インフルエンサー陳雨墨（チェン・ユーモー）チームが開発したローカル導入可能なオープンソース・マルチモーダル AI 大規模モデルです。オープンソース基盤 **Ornith-1.5-35B-A3B**（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B アーキテクチャ、MoE 35B、MIT ライセンス）をベースに、チーム独自開発の金融データ + 金融領域能力 + 動的7次元思考体系 + エージェント LOOP 反復メカニズム + Uncensored 特性 + MoziSmartBit ハイブリッド量子化アルゴリズムを統合しています。

**💡 サイズ優位性：わずか 15.9GB** — 350億パラメータの MoE モデルを自社開発 MoziSmartBit 量子化により **15.9 GB**（標準 Q4_K_M 約22GB より約30%小）まで圧縮。単一パッケージで持ち運べ、一般向け GPU（20GB VRAM 以上）で動作し、クラウド token コストは **0**、7×24 時間 token 自由を実現、ローカルデータのプライバシーを確保。**商用無料**ライセンス — 導入ハードルゼロ。

---

## 2. 特徴

### 🧠 動的7次元思考体系

MoziAI 独自開発のコア推論フレームワーク。あらゆるタスクに対し、まず **moziAI-Think** マーカーを出力し、タスクの複雑さに応じて構造化思考を動的に展開します：

| レベル | 適用シーン | 典型的なタスク | 展開する次元 |
| --- | --- | --- | --- |
| **Level 0** | 簡単なQ&A | 用語解説、事実検索、翻訳、要約 | ①タスク理解 ⑤リソース要件（2次元で即答） |
| **Level 1** | 分析・診断 | 市場調査、文書作成、データ分析、レポート解読、戦略評価 | ①②③⑤⑥ 5次元評価 |
| **Level 2** | 複雑な開発/戦略 | コード開発、アーキテクチャ設計、クオンツ戦略開発、マルチステップ業務、システム設計 | ①②③④⑤⑥⑦ 全7次元の深い推論 |

> 7次元：①タスク理解 ②複雑さ評価 ③依存関係 ④リスク評価 ⑤リソース要件 ⑥受入基準 ⑦実行戦略

### 🔄 エージェント LOOP 反復メカニズム

複雑なタスクは自動的に **moziAI-Loop** 反復モードに入ります：**第1ラウンド実行+評価 → 第2ラウンド調整+検証**。出力は自己検証を経てから最終回答が返されます。モデルはシニアエンジニアのように「問題分解 → プラン評価 → 実行 → 振り返り → 最適化」を行い、複雑タスクの正確性と実行可能性を大幅に向上させます。簡単なQ&Aでは Loop は自動的にスキップされます。

### 📦 MoziSmartBit スマート量子化

独自開発の階層型スマート量子化により、350億パラメータの MoE モデルを約 **15.9 GB** に圧縮。通常の Q4_K_M（約22 GB）より約6.5 GB（約30%）小さく、FP16 の **約99%** 精度を維持します。従来の量子化は全レイヤーに統一精度を使用しますが、MoziSmartBit は MoE 構造に特化したスマート差別化戦略を採用し、Q4_K_M より高精度です。圧縮比 **4.5x**。

### 💰 金融垂直領域への特化

金融Q&A、クオンツプログラミング、ツール呼び出しに深く最適化。金融分野は幻覚への許容度が極めて低く、MoziAI は同サイズの汎用モデルより明確に優れています。

### 🛡️ Uncensored 特性

コンテンツ規制なし・自由出力・完全な情報・ローカルプライバシー。学術研究、深い分析、自由な議論などのシーンに最適です（[第15節](#15-uncensored検閲なし最適化)参照）。

### 🌐 その他の特徴

- **多言語対応**：201の言語・方言、中国語能力を特に最適化
- **一般プログラミング**：フルスタック開発、デバッグ、アーキテクチャ設計（Python/JS/TS/Go/Rust）
- **文章作成**：レポート、分析記事、技術文書、クリエイティブなど多ジャンル高品質
- **視覚理解**：マルチモーダル、ローカルでスクリーンショット画像を理解
- **マルチフレームワーク**：llama.cpp / Ollama / LM Studio / Jan
- **マルチエージェント対応**：OpenClaw / Hermes / Cursor / Claude Code / Codex など、ネイティブなツール呼び出しとマルチターンタスク編成

---

## 3. バージョンアップ情報

V3.8 は 27B-V3.8 と同じ世代の独自開発トレーニングデータセット体系（アイデンティティ / 動的7次元思考 / LOOP 反復 / 金融垂直領域）で再トレーニングされ、動的7次元思考 + LOOP 反復の推論モードを重点強化。タスク複雑さの認識がより賢くなり、複雑タスクの完遂率が向上、「先に考えてから実行」の能力が強化されました。Uncensored 特性と金融垂直領域の最適化も継続しています。

moziAI は活発なバージョンアップを継続し、AI の発展に追随するとともに、独自技術によるローカル AI モデルの軽量化と能力強化を続けます。

---

## 4. コア能力

| 能力領域 | 説明 |
| --- | --- |
| 市場分析 | マクロ/ミクロ経済解説、A株/香港/米国株/商品/仮想通貨の相場とロジック整理 |
| 財務とレポート | 決算指標の解説、レポート要約抽出、評価・収益予測の補助 |
| リスクとコンプライアンス | 商品リスク評価、投資助言のコンプライアンス、金融規制政策の解説 |
| クオンツと戦略 | クオンツ戦略設計、Pyramid/PEL 量化、バックテスト、ファクター構築、ツール呼び出し |
| ツール呼び出し | リアルタイム相場、データベース、レポート検索などの金融データソースに接続可能 |

---

## 5. 技術仕様

| 項目 | 仕様 |
| --- | --- |
| ベースモデル | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B アーキテクチャ、MIT ライセンス） |
| パラメータ数 | 350億（35B）MoE、256ルーティング専門家 + 1共有専門家、トークン毎に8専門家がアクティブ |
| 量子化 | 独自 MoziSmartBit スマート量子化 + GGUF 標準形式 |
| コンテキスト長 | 256K（262,144 tokens） |
| モデルサイズ | ~15.9 GB |
| 最小 VRAM | **20GB+** 導入可（CPUオフロード）；**24GB+** 快適な長文脈；**32GB+** 完全 256K + 視覚 |
| 推論フレームワーク | llama.cpp / Ollama / LM Studio / Jan |
| 推論速度 | 投機的デコード時：AMD R9700 GPU で **140+ tok/s** / AMD MAX+395 iGPU で **70+ tok/s** — ローカルで token 自由 |
| 開発チーム | 陳雨墨チーム |

---

## 6. ⚡ クイックスタート（3ファイル = 100% 最適な推論を有効化）

> ⚠️ **重要**：MoziAI の最適な推論には**3ファイルを同時にダウンロード**してください——メインモデル、ビジョンプロジェクター、チャットテンプレート。1つ欠けると対応する能力が失われます。

### 6.1 モデルファイルのダウンロード

HuggingFace / ModelScope で**この 3 ファイル**をローカルの同一フォルダにダウンロード（メインモデルは**リポジトリルート**、ビジョンプロジェクターは `mmproj/35B/`、チャットテンプレートは `V3.8/`）：

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← メインモデル（必須、15.9 GB）
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← ビジョンプロジェクター（必須、~1 GB）
moziAI-V3.8-35B-chat-template.jinja                                        ← チャットテンプレート（必須、7次元思考+Loop指令）
```

| ファイル | サイズ | 必須 | 役割 |
| --- | --- | --- | --- |
| メインモデル `.gguf` | ~15.9 GB | **必須** | モデル重み、コア推論 |
| ビジョン `mmproj` | ~1 GB | **必須** | マルチモーダル視覚、未ロードなら画像能力喪失 |
| チャットテンプレート `.jinja` | 微小 | **必須** | MoziAI アイデンティティ + 7次元思考 + LOOP 指令を注入 |

### 6.2 起動して使用

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

ブラウザで `http://localhost:8080` を開いて会話を開始。完全な推奨パラメータは第9節を参照。

---

## 7. モデルダウンロード

| プラットフォーム | アドレス |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/master) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio ユーザー**：[LM Studio](https://lmstudio.ai) で `moziAI` を検索すればワンクリックダウンロード。

> 💡 **ダウンロードのコツ**：HuggingFace リポジトリの **"Files and versions"** タブから **リポジトリルート**でメインモデル、`mmproj/35B/` からビジョンプロジェクター、`V3.8/` からチャットテンプレートをダウンロードし、3つを同じフォルダに配置してください。

---

## 8. 起動コマンド

### 最小起動（3ファイル含む）

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### 完全推奨起動

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

> 💡 VRAM 不足時：`-c` を下げる（例：131072）、または `--fit on` を追加して llama.cpp に VRAM 適合させる。

---

## 9. 推奨推論パラメータ

ローカル実測に基づく最適化（AMD Radeon AI PRO R9700 32GB）：

| パラメータ | 日常タスク/文書作成 | 複雑タスク/高度コーディング | 説明 |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | 日常は安定、複雑コーディングは適度に探索 |
| top\_p | 0.95 | 0.95 | 核サンプリング閾値 |
| top\_k | 20 | 20 | トランケーションサンプリング |
| min\_p | 0.024 | 0.024 | 最小確率フィルタ |
| repeat\_penalty | 1.05 | 1.05 | 繰り返しペナルティ |
| presence\_penalty | 0 | 0 | 存在ペナルティなし |
| context\_length | 262144 | 262144 | 256K 長文脈 |
| reasoning | on | on | 推論チェーン（CoT）有効 |
| reasoning\_budget | 400 | 1000 | 推論予算 token（複雑タスクは高め） |
| reasoning\_format | deepseek-legacy | deepseek-legacy | 推論を別フィールドに出力 |
| **spec-type** | **default** | **default** | **投機的デコード（ngram、MoE最適、第11節参照）** |
| KV キャッシュ | q4\_0 | q4\_0 | 量子化 KV キャッシュ（kv-unified） |

> 💡 **思考モード**：`--reasoning on` で有効化。回答前に内部推論します。`reasoning_budget` は最大思考トークン数を制御。

---

## 10. 量子化形式比較

| 形式 | サイズ | 精度 | 説明 |
| --- | --- | --- | --- |
| FP16 オリジナル | ~70 GB | 100% | ロスレス、プロ GPU 必要 |
| **MoziSmartBit（本モデル）** | **~15.9 GB** | **~99%** | **独自スマート量子化、精度最良・最小サイズ** |
| Q4_K_M | ~22 GB | ~98% | GGUF 標準 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 高精度 |
| Q6_K | ~28.5 GB | ~99.5% | ほぼロスレス |
| Q8_0 | ~36.9 GB | ~100% | ロスレス |

> MoziSmartBit は約99%精度を維持しつつ 35B MoE を 15.9 GB（4.5x 圧縮）に。Q4_K_M より約30%小さく、コンシューマー GPU に最適。

---

## 11. 投機的デコード高速化（重要機能）

本モデルは**投機的デコード（Speculative Decoding）**で推論速度を大幅向上。ローカル実測でオフ時より**約1.5-2倍**速くなります。

- **MoE 最適設定**：llama.cpp は MoE アーキテクチャに **ngram 投機的デコード**（`--spec-default`）を推奨。ローカル実測で最速かつ安定
- **モデル名の "MTP" について**：基盤の Multi-Token Prediction 重み（完全保持）に由来。llama.cpp の MoE 向け MTP draft サポートは限定的なため、MoziAI は ngram 方式で最良の実測速度を実現

### 有効化パラメータ

```bash
--spec-default
```

### 調整提案

| 設定 | 適用シーン |
| --- | --- |
| --spec-default（デフォルト） | 推奨：速度と VRAM のバランス |
| 無効化（フラグ削除） | VRAM 逼迫時、やや低速 |

---

## 12. VRAM設定推奨

MoziSmartBit 版（モデル+視覚 約16.4GB）実測ベース：

| VRAM | 推奨設定 | 説明 |
| --- | --- | --- |
| 20 GB | 150K 文脈、q4\_0 KV、視覚対応 | モデル+視覚約16.4GB；256K+視覚で約19.5GB使用 |
| **24 GB** | **完全 256K、q4\_0 KV、視覚完璧** | **推奨**：視覚+256K で約20.4GB、余裕約3.6GB |
| 32 GB+ | 完全 256K、余裕十分 | 例：R9700 32GB：視覚+256K で約10GB 余裕、最強構成 |

> 💡 文脈が長いほど VRAM 消費増。OOM 時は `-c` を段階的に下げる。`--fit on` で自動適合。NVIDIA / AMD 対応。

---

## 13. 導入方法

### Ollama 導入

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

LM Studio / Jan で `moziAI` を検索し、Q4\_K\_M 量子化版をダウンロード（LM Studio はデフォルトでルートディレクトリのモデルを読み込みます。以前のバージョンは「URLから追加」で対応するバージョンディレクトリ（例：`V3.7/`）のファイルをインポートしてください）。

> 💡 Ollama の mmproj と chat\_template サポートは限定的。フル機能には llama.cpp を推奨。

---

## 14. ベンチマーク

MoziAI-35B-V3.8 は deepreinforce-ai/Ornith-1.5-35B-A3B ベースを微調整・蒸留・再開発したモデルで、金融垂直領域が中核の最適化方向です。以下はマルチモデル比較（MoziAI の汎用能力はベース Ornith-1.5-35B-A3B と一致。データは V3.7 実測を踏襲——V3.8 は V3.7 と同一ベース・同一トレーニング体系）：

| Benchmark | moziAI-35B-V3.8<br>（本モデル） | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **コーディング** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **推論** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **エージェント** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI は金融垂直領域（決算解読、クオンツ戦略、リスク管理、エージェントツール呼び出し）で同サイズ汎用モデルを大幅に上回ります。Gemma-4 / Qwen3.6 の数値は公式公開評価結果。

---

## 15. Uncensored（検閲なし）最適化

本モデルは Ornith-1.5-35B-A3B ベースの Uncensored 特性を継承：

| 利点 | 説明 |
| --- | --- |
| 検閲なし | センシティブ・論争的コンテンツを含め、いかなる話題も拒否しない |
| 自由出力 | 安全ポリシーに制約されず、あらゆるタイプの返答を生成 |
| 完全な情報 | フィルタリングされていない情報を提供、研究・分析に最適 |
| ローカルプライバシー | ローカル導入 = データ完全プライベート、クラウド検閲なし |

**ユースケース**：学術研究、深い分析、自由な議論、制限のない AI 会話。

**注意**：ローカル導入モデルのため、出力はユーザーが完全に管理します。モデルはコンテンツモデレーションの責任を負いません。

---

## 16. ライセンス

本モデルは**カスタム制限ライセンス**を採用：

- ✅ **許可** — 商用無料利用、コピー・配布
- ❌ **禁止** — 二次開発、転売、再ライセンス
- 📋 **必須** — 元の著作権表示を保持、出典：moziAI-35B

本モデルは「現状有姿」で提供され、いかなる保証もありません。モデル出力は参考情報であり、投資助言を構成するものではありません。利用者はすべてのリスクを自己負担します。

詳細は [LICENSE](LICENSE) ファイルを参照。

---

## 17. 連絡先

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **Weibo**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. All rights reserved.