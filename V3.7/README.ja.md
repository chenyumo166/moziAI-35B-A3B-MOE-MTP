---
language:
- ja
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

# MoziAI-V3.7-35B-A3B-MOE - 無料でローカルデプロイできる小型高性能マルチモーダルAI

[English](README.en.md) | [中文](README.md)

## モデル概�?

MoziAI-35B-A3B-MOEは、中国の金融インフルエンサー陳雨墨（Chen Yumo）のチームが開発した、ローカルオープンソース金融AIマルチモーダルLLM（visionおよびtool callingをサポート）です。Ornith-1.5-35B-A3B�?*Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** アーキテクチャ、MITライセンス）ベースモデルからファインチューニング/蒸留されています。自社開発の**MoziSmartBit Intelligent Quantization**技術により�?5BパラメータのMoEモデルを�?*15.5 GB**に圧縮し、ほぼロスレスな�?9%の精度品質を維持しながら、精度とサイズの最適バランスを実現しています�?

一般的なAI機能を保持するだけでなく、このモデルは金融垂直ドメインアプリケーションの最適化に重点を置いており、金融Q&A、クオンツプログラミング、tool calling、および汎用プログラミングをカバーしています�?

モデル開発者の陳雨墨は、このモデルをローカルの金融データ分析、クオンツ戦略研究開発、市場調査、記事執筆、プロジェクト全体の推進、汎用プログラミング、およびopenclaw/hermes経由�?56Kコンテキストタスクに頻繁に使用しています。コンシューマグレードGPUでローカルデプロイが可能で、クラウドトークンコストを大幅に節約し�?×24のトークン自由を実現するとともに、ローカルデータのプライバシーとセキュリティを確保します�?

llama.cpp、Ollama、LM Studioなど、主要な推論フレームワークをサポートしています�?

**リリース日：2026-08-21** | **バージョン：V3.7**

## モデルの特徴

- **金融垂直ドメイン特化**: 金融Q&A、クオンツプログラミング、tool callingのための深層最適化
- **MoziSmartBit Intelligent Quantization**: 自社開発のスマート量子化、精度とサイズの最適バランス、約**15.5 GB**に圧�?
- **コンシューマグレードデプロイ**: 20GBまた�?4GB以上のVRAMを持つコンシューマGPUでデプロイ可能�?56K長コンテキストをサポート
- **多言語サポー�?*: 201の言語と方言、中国語能力が強化、英�?日本�?韓国�?ドイツ語/フランス�?スペイン�?ポルトガル語などをカバー
- **汎用プログラミン�?*: フルスタック開発、コードデバッグ、アーキテクチャ設計、スクリプト作成、Python/JS/TS/Go/Rustなどの主要言語をカバ�?
- **記事執筆**: リサーチレポート、分析記事、技術ドキュメント、クリエイティブコンテンツなど、ハイクオリティな多ジャンル執筆
- **Vision理解**: マルチモーダルvision、ローカルスクリーンショット入力、画像理解をサポート
- **Uncensored自由出力**: コンテンツ検閲なし、安全制限なしであらゆるトピックを自由に議論
- **推論能力の強�?*: Chain-of-thought訓練による推論品質の向上
- **マルチフレームワークサポート**: llama.cpp、Ollama、LM Studio、Janに対�?
- **マルチエージェントプラットフォームサポー�?*: OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codexなどの主要AI IDEおよびエージェントフレームワークとの深層統合、tool callingおよびマルチターンタスクオーケストレーションをネイティブにサポート、すぐに使用可能

## Uncensoredの利�?

このモデルはOrnith-1.5-35B-A3Bベースモデルから**Uncensored**機能を継承しており、以下の利点があります：

| 利点 | 説明 |
|------|------|
| **検閲なし** | 感惹的または議論の的となるコンテンツを含め、あらゆるトピックを拒否しな�?|
| **自由な出�?* | 安全ポリシーの制限を受けず、あらゆるタイプの応答を生成可能 |
| **完全な情�?* | フィルタリングされていない完全な情報を提供し、研究・分析に適している |
| **ローカルプライバシー** | ローカルデプロイにより、データは完全にプライベートでクラウド検閲の影響を受けな�?|

> **ユースケース**: 学術研究、深層分析、自由な議論、制限のないAI会話�?
> **注意**: これはローカルデプロイされたモデルであり、出力コンテンツはユーザーが完全に管理します。コンテンツモデレーションの責任はありません�?

## コア能力

| 能力分野 | 説明 |
|----------|------|
| 市場分析 | マク�?ミクロ経済解説、A�?香港/米国�?商品/暗号通貨市場のロジッ�?|
| 財務報告 | 主要財務指標の解標の解説、リサーチレポートの要約、バリュエーション＆業績予測のサポー�?|
| リスク＆コンプライアンス | 製品リスク評価、投資助言のコンプライアンス、金融規制ポリシーの解説 |
| クオンツ＆戦�?| クオンツ戦略設計、Pyramid（PEL）クオンツ化、バックテストロジック、ファクター構築およびtool calling |
| Tool Calling | リアルタイム配信、データベース、リサーチレポート検索などの金融データソースとの統合 |

## 技術仕�?

| 項目 | 仕様 |
|------|------|
| ベースモデル | Ornith-1.5-35B-A3B�?*Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**、MITライセンス） |
| パラメータ数 | 35B MoE�?56個のルーティングエキスパート + 1個の共有エキスパート、トークンあたり8個がアクティブ） |
| 量子�?| 自社開発MoziSmartBit Intelligent Quantization + GGUF標準フォーマット |
| コンテキスト�?| 256K�?62,144トークン�?|
| モデルサイズ | �?5.5 GB（MoziSmartBit Uncensored版） |
| 最小VRAM | 20GB以上のVRAMを持つコンシューマGPU（例：RTX 4060 Ti 16G + CPUオフロード）�?4 GB推奨（vision + 長コンテキスト使用時�?|
| 推論フレームワー�?| llama.cpp / Ollama / LM Studio / Jan |
| 推論速度 | アルゴリズム最適化：AMD R700 GPU�?40+ token/s、AMD MAX+395 CPU iGPU�?0+ token/s、ローカルトークン自�?|
| 開発チー�?| 陳雨墨チーム |

## 量子化フォーマット＆モデルサイズ比較

| 量子化フォーマッ�?| モデルサイズ | 精度 | 備�?|
|-------------------|-------------|------|------|
| **FP16（オリジナル�?* | �?0 GB | 100% | オリジナ�?6bit |
| **MoziSmartBit** | **�?5.5 GB** | **�?9%** | **MoziAIが採用、最適な量子化スキー�?* |
| Q4_K_M | �?2 GB | �?8% | GGUF標準4bit |
| Q5_K_M | �?4.7 GB | �?9% | 高品�?|
| Q6_K | �?8.5 GB | �?9.5% | 近似ロスレス |
| Q8_0 | �?6.9 GB | �?00% | ロスレス |

> MoziAI V3.7はMoziSmartBit Intelligent Quantizationを採用し、約99%の精度を維持しながら35BパラメータのMoEモデルを�?5.5 GB（約4.5倍の圧縮率）に圧縮し、推論品質とコンシューマGPU向けデプロイ可能性のバランスを実現しています�?

## MoziSmartBit Intelligent Quantization

従来の量子化は全レイヤーに均一な精度を適用します�?*MoziSmartBit Intelligent Quantization**は、サイズと精度の最適バランスのために差別化された量子化戦略を適用します�?

### 圧縮効果

従来の量子化はモデルの全部分を均一に圧縮し、しばしば著しい精度損失を引き起こします。MoziSmartBit Intelligent Quantizationは自社開発のインテリジェント圧縮戦略を使用し�?*最小限の精度損失で大幅なサイズ削減を実�?*します：

- **最小限の量子化損失**: 訓練効果 > 量子化損失。訓練されたMoziAI-35Bは金融ドメインテキストにおいて、事前学習bf16ベースモデルよりも良好なPPLを達成し、類似AIモデルと比較してハルシネーションとパープレキシティを削減
- **�?.5倍のサイズ削�?*: �?0 GB（FP16）から約15.5 GBに圧縮、Q4_K_M（約21 GB）よりも大幅に小さく、VRAMとストレージ要件を著しく削減
- **コンシューマGPUフレンドリー**: 以前はハイエンドGPUが必要だった35B MoEモデルが�?0GB�?4GB VRAMでスムーズに動作

### 比較優位�?

**Q4_K_M（約22 GB）と比較**: �?0%小型化（�?5.5 GB）、精度はQ4_K_M**より高く**、VRAM障壁が低�?�?ミドルレンジコンシューマGPU�?4GB）でスムーズに動作�?

**FP16オリジナル（�?0 GB）と比較**: �?.5倍の圧縮、訓練有�?+ 最小限の量子化損失（訓練効�?> 量子化損失）、プロフェッショナルグレードのハードウェアではなくコンシューマGPUでローカ�?56Kコンテキストデプロイが可能�?

## 推奨推論パラメー�?

ローカル本番環境の設定に基づく（AMD Radeon AI PRO R9700 32GB）：

| パラメー�?| �?| 説明 |
|-----------|-----|------|
| temperature | 0.6 | 創造性と正確性のバランス |
| top_p | 0.95 | ニュークルサムプリングしきい�?|
| top_k | 20 | トランケーションサプリング（V3.7最適化�?|
| repeat_penalty | 1.05 | 繰り返しペナルテ�?|
| presence_penalty | 0 | presenceペナルティな�?|
| context_length | 262144 | 256K長コンテキス�?|
| batch_size | 2048 | バッチサイズ |
| ubatch_size | 512 | マイクロバッチサイズ |
| flash_attention | auto | 自動Flash Attention |
| kv_cache | q4_0 | KVキャッシュ量子化（kv-unified�?|
| poll | 0 | アイドル時GPUポーリングなし、省エネ |
| reasoning | on | 推論チェーン（chain of thought）を有効�?|
| reasoning_budget | 400 | 推論予算（トークン数�?|
| reasoning_format | deepseek-legacy | 推論フォーマット |
| samplers | top_k;top_p;temperature;typ_p | サンプラー順�?|

### llama.cpp起動コマンド

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

### VRAM設定の推�?

ユーザーのGPU構成は大きく異なるため、異なるVRAMサイズの推奨パラメータを以下に示します（すべてMoziSmartBit版用）：

| VRAM | 推奨コンテキスト | KVキャッシ�?| Visionサポート | 備�?|
|------|-----------------|-------------|---------------|------|
| 20 GB | 150K | q4_0 | サポートあり | モデ�?vision �?6.4GB、実測で200K+vision使用時のVRAM消費は約19.5GB |
| 24 GB | 256Kフル | q4_0 | 完全サポート | Vision+256K長コンテキスト、VRAM消費�?0.4GB、ヘッドルーム約3.6GB |
| 32 GB+ | 256Kフル | q4_0 | 完全サポート | Vision+256K長コンテキスト、十分なヘッドルーム�?0GB、最適構�?|

**NVIDIA**

| VRAM | GPUモデ�?|
|------|-----------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD**

| VRAM | GPUモデ�?|
|------|-----------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel**

| VRAM | GPUモデ�?|
|------|-----------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50（CPUオフロードが必要�?|

**共有メモリiGPU**

| VRAM | プロセッ�?|
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S iGPU�?|
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU�?|

> 💡 **ヒン�?*: 上記のVRAM要件を満たしていれば動作します。ブランドやモデルの制限はありません。NVIDIA / AMD / IntelのディスクリートGPU、および上記�?28GB統合メモリiGPUをサポートしています�?

> 💡 **ヒン�?*: コンテキストが長くなるほどVRAMを多く使用します。OOM（メモリ不足）が発生した場合は、`-c`の値を段階的に減らしてください。`--fit on`を使用すると、llama.cppがVRAMに合わせて自動的にレイヤーを調整します�?

### Ollamaデプロイ

```bash
# Modelfileを作�?
FROM ./moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# ビルド＆実行
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Janデプロイ

LM StudioまたはJanで`moziAI-35B`を検索し、MoziSmartBit量子化版をダウンロードしてください�?

## ベンチマーク評価

MoziAI�?*deepreinforce-ai/Ornith-1.5-35B-A3B**からファインチューニングされています。MoziAIはベースモデルの上で金融垂直ドメインの最適化が施されており、金融Q&A、クオンツプログラミング、tool callingシナリオにおいて優れた性能を発揮します。MoziAI-35Bの汎用能力はOrnith-1.5-35B-A3Bベースモデルと一致しています�?

| ベンチマーク | MoziAI-35B（本モデル） | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | 説明 |
|-------------|------------------------|-------------|------------|------------|-------------|------|
| Terminal-Bench 2.1 | 64.2 | 59.3 | 42.1 | - | 41.4 | 自律ターミナルコーディン�?|
| Terminal-Bench（Claude Code�?| 62.8 | 59.3 | - | - | 38.9 | Claude Codeコーディング |
| SWE-bench Verified | 75.6 | 77.2 | 52.0 | - | 70.0 | 実世界ソフトウェアエンジニアリン�?|
| SWE-bench Pro | 50.4 | 53.5 | 35.7 | - | 44.6 | 複雑なソフトウェアエンジニアリン�?|
| SWE-bench Multilingual | 69.3 | 71.3 | - | - | 60.3 | 多言語コーディン�?|
| NL2Repo | 34.6 | 36.2 | 15.5 | - | 20.5 | 自然言語からリポジトリ生成 |
| LiveCodeBench v6 | 63.3 | 83.9 | 80.0 | 77.1 | - | 競プロプログラミング |
| GPQA Diamond | 88.4 | 87.8 | 84.3 | 82.3 | - | 科学的推�?|
| AIME 2026 Math | 93.3 | 94.1 | 89.2 | 88.3 | - | 数学的推�?|

> MoziAI-35Bの汎用ベンチマークスコアはOrnith-1.5-35B-A3Bベースモデルと一致しています。金融垂直ドメインはMoziAIのコア最適化方向であり、財務報告分析、クオンツ戦略、リスク＆コンプライアンス、エージェントtool callingなどのシナリオで汎用モデルを大幅に上回ります。Gemma4およびQwen3.6のデータは公式公開結果からの引用です�?

## モデルダウンロー�?

モデルサイズが大きく（約15.5 GB）、複数のコミュニティプラットフォームでホストされています�?

| プラットフォーム | URL |
|----------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |


> 💡 **LM Studio ユーザー**：[LM Studio](https://lmstudio.ai) �?`moziAI` を検索し、ワンクリックでダウンロードできます�?
> 💡 **ダウンロードのヒン�?*: 上記リンクをクリックしてHuggingFaceリポジトリに移動し�?*「Files and versions�?*タブでV3.7ディレクトリ配下のすべてのファイルをダウンロードしてください（メインモデル、vision射影、チャットテンプレート）�?つのファイルすべてを同じディレクトリに配置してください�?

### ⚠️ 重要：Vision機能にはmmprojファイルが必要で�?

このモデルはマルチモーダルvisionをサポートしています�?*vision射影ファイル（mmproj�?*はバージョンディレクトリに含まれています�?

- **Visionファイル**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`（約903 MB、BF16精度�?
- **配置場所**: GGUFモデルファイルと同じバージョンディレクト�?
- **読み込み**: llama-server起動時に`--mmproj`フラグを使用して読み込み

```bash
llama-server -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf
```

> visionファイルがない場合、モデル�?*画像理解機能を失�?*、テキストのみの会話のみが可能になります�?

## クイックスタート

### 1. モデルファイルをダウンロー�?

HuggingFace / ModelScopeからV3.7ディレクトリ配下のすべてのファイルをダウンロード：

```
V3.7/
├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # メインモデル（必須）
├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision射影（オプション�?
└── moziAI-V3.7-35B-chat-template.jinja                  # チャットテンプレート（推奨）
```

### 2. 推論サーバーを起�?

完全な推奨設定については、上記の[llama.cpp起動コマンド](#llamacpp起動コマンド)を参照してください�?

最小限の起動（コアパラメータのみ）�?

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> vision機能を追加するには`--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`を追加してください�?

### 3. 使用開始

ブラウザで`http://localhost:8080`を開いてチャットを開始します�?

### ディレクトリ構成

```
moziAI-35B/
├── README.md              # 中文�?
├── README.en.md           # 英語�?
├── README.ja.md           # このファイル（日本語�?
├── LICENSE                # ライセン�?
├── V3.7/                  # V3.7バージョン（自己完結型）
�?  ├── RELEASE_NOTES.md                       # リリースノー�?
�?  ├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # メインモデル
�?  ├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision射影
�?  └── moziAI-V3.7-35B-chat-template.jinja   # チャットテンプレート
```

将来のアップグレード計画については、[未来升级计划.md](未来升级计划.md)を参照してください�?

## SEOキーワー�?

financial AI LLM, ローカルオープンソースモデル, エッジサイドモデ�? クオンツプログラミン�? MoziSmartBit, インテリジェント量子�? GGUF量子�? MoEモデ�? ローカルオープンソースLLM, ローカルデプロイ, 金融AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, 検閲なし, 自由出力, 制限なし, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, 金融垂直ドメイン, オープンソースモデル

## ライセンス（重要�?

このモデルは**カスタム制限付きライセン�?*を使用しています�?

### �?許可事項
- **無料商用利用**: 商製品に統合自由
- **複製＆配�?*: コピー、ダウンロード、共有が可能

### �?禁止事項
- **派生作品**: モデルまたはその一部の修正、翻訳、適応、統合、ファインチューニング禁�?
- **再販�?*: モデル単体または製品の一部としての販売禁�?
- **再ライセンス**: サブライセンスの付与禁止

### 📋 要件
- 元の著作権表示を保持すること
- 表記: moziAI-35B

> 完全な条款については[LICENSE](./LICENSE)を参照してください�?

## 免責事項

現状有姿で保証なしに提供されます。モデル出力は参考情報であり、投資助言ではありません。ユーザーはすべてのリスクを負います�?

## お問い合わせ

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.
