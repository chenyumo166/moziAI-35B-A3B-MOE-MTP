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



[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | 日本語 | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)



## モデル概要



MoziAI-35B-A3B-MOEは、中国の金融インフルエンサー陳雨墨（Chen Yumo）のチームが開発した、ローカルオープンソース金融AIマルチモーダルLLM（visionおよびtool callingをサポート）です。moziAI-35Bはオープンソース基盤モデル Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B アーキテクチャ、MITライセンス）に基づき、陳雨墨チームの自社開発：（金融データ + 金融領域能力 + トレーニング手法 + 七次元思考体系 + エージェントLOOPメカニズム + ハイブリッド量子化アルゴリズム MoziSmartBit）を組み合わせて開発されています。自社開発のMoziSmartBit インテリジェント量子化技術により、350億パラメータのMoEモデルは約15.5 GBに圧縮され、従来のQ4_K_M量子化モデル（約22+GB）より6.5G（約30%）小さくなっています。精度とサイズの最適なバランスを実現し、ほぼロスレスな≈FP16の99%の精度品質を実現しています。



一般的なAI機能を保持するだけでなく、このモデルは金融垂直ドメインアプリケーションの最適化に重点を置いており、金融Q&A、クオンツプログラミング、tool calling、および汎用プログラミングをカバーしています。



モデル開発者の陳雨墨は、このモデルをローカルの金融データ分析、クオンツ戦略研究開発、市場調査、記事執筆、プロジェクト全体の推進、汎用プログラミング、およびopenclaw/hermes経由な56Kコンテキストタスクに頻繁に使用しています。コンシューマグレードGPUでローカルデプロイが可能で、クラウドトークンコストを大幅に節約して×24のトークン自由を実現するとともに、ローカルデータのプライバシーとセキュリティを確保します。



llama.cpp、Ollama、LM Studioなど、主要な推論フレームワークをサポートしています。



**リリース日：2026-08-21** | **バージョン：V3.7**



## モデルの特徴



- **金融垂直ドメイン特化**: 金融Q&A、クオンツプログラミング、tool callingのための深層最適化

- **MoziSmartBit Intelligent Quantization**: 自社開発のスマート量子化、精度とサイズの最適バランス、約**15.5 GB**に圧縮

- **コンシューマグレードデプロイ**: 20GBまため4GB以上のVRAMを持つコンシューマGPUでデプロイ可能力56K長コンテキストをサポート

- **多言語サポーマ*: 201の言語と方言、中国語能力が強化、英語日本モ韓国語ドイツ語/フランストスペインテポルトガル語などをカバー

- **汎用プログラミンテ*: フルスタック開発、コードデバッグ、アーキテクチャ設計、スクリプト作成、Python/JS/TS/Go/Rustなどの主要言語をカバー

- **記事執筆**: リサーチレポート、分析記事、技術ドキュメント、クリエイティブコンテンツなど、ハイクオリティな多ジャンル執筆

- **Vision理解**: マルチモーダルvision、ローカルスクリーンショット入力、画像理解をサポート

- **Uncensored自由出力**: コンテンツ検閲なし、安全制限なしであらゆるトピックを自由に議論

- **推論能力の強化*: Chain-of-thought訓練による推論品質の向上

- **マルチフレームワークサポート**: llama.cpp、Ollama、LM Studio、Janに対応

- **マルチエージェントプラットフォームサポーマ*: OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codexなどの主要AI IDEおよびエージェントフレームワークとの深層統合、tool callingおよびマルチターンタスクオーケストレーションをネイティブにサポート、すぐに使用可能



## Uncensoredの利用



このモデルはOrnith-1.5-35B-A3Bベースモデルから**Uncensored**機能を継承しており、以下の利点があります：



| 利点 | 説明 |
|------|------|
| **検閲なし** | 感惹的または議論の的となるコンテンツを含め、あらゆるトピックを拒否しなど|
| **自由な出し* | 安全ポリシーの制限を受けず、あらゆるタイプの応答を生成可能 |
| **完全な情報* | フィルタリングされていない完全な情報を提供し、研究・分析に適している |
| **ローカルプライバシー** | ローカルデプロイにより、データは完全にプライベートでクラウド検閲の影響を受けなど|
> **ユースケース**: 学術研究、深層分析、自由な議論、制限のないAI会話フ

> **注意**: これはローカルデプロイされたモデルであり、出力コンテンツはユーザーが完全に管理します。コンテンツモデレーションの責任はありません。



## コア能力



| 能力分野 | 説明 |
|----------|------|
| 市場分析 | マクトミクロ経済解説、A/香港/米国語商品/暗号通貨市場のロジット|
| 財務報告 | 主要財務指標の解標の解説、リサーチレポートの要約、バリュエーション＆業績予測のサポーマ|
| リスク＆コンプライアンス | 製品リスク評価、投資助言のコンプライアンス、金融規制ポリシーの解説 |
| クオンツ＆戦略| クオンツ戦略設計、Pyramid（PEL）クオンツ化、バックテストロジック、ファクター構築およびtool calling |
| Tool Calling | リアルタイム配信、データベース、リサーチレポート検索などの金融データソースとの統合 |
## 技術仕様



| 項目 | 仕様 |
|------|------|
| ベースモデル | Ornith-1.5-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**、MITライセンス） |
| パラメータ数 | 35B MoE（256個のルーティングエキスパート + 1個の共有エキスパート、トークンあたり8個がアクティブ） |
| 量子化| 自社開発MoziSmartBit Intelligent Quantization + GGUF標準フォーマット |
| コンテキストを| 256K（262,144トークンテ|
| モデルサイズ | 約15.5 GB（MoziSmartBit Uncensored版） |
| 最小VRAM | 20GB以上のVRAMを持つコンシューマGPU（例：RTX 4060 Ti 16G + CPUオフロード）を4 GB推奨（vision + 長コンテキスト使用時に|
| 推論フレームワーマ| llama.cpp / Ollama / LM Studio / Jan |
| 推論速度 | アルゴリズム最適化：AMD R9700 GPUで140+ token/s、AMD MAX+395 CPU iGPUで70+ token/s、ローカルトークン自開|
| 開発チーマ| 陳雨墨チーム |
## 量子化フォーマット＆モデルサイズ比較



| 量子化フォーマット| モデルサイズ | 精度 | 備考|
|-------------------|-------------|------|------|
| **FP16（オリジナルの* | 約70 GB | 100% | オリジナル6bit |
| **MoziSmartBit** | **約15.5 GB** | **約99%** | **MoziAIが採用、最適な量子化スキーマ* |
| Q4_K_M | 約22 GB | 約98% | GGUF標準4bit |
| Q5_K_M | 約24.7 GB | 約99% | 高品質|
| Q6_K | 約18.5 GB | 約99.5% | 近似ロスレス |
| Q8_0 | 約16.9 GB | 約100% | ロスレス |
> MoziAI V3.7はMoziSmartBit Intelligent Quantizationを採用し、約99%の精度を維持しながら35BパラメータのMoEモデルを実5.5 GB（約4.5倍の圧縮率）に圧縮し、推論品質とコンシューマGPU向けデプロイ可能性のバランスを実現しています。



## MoziSmartBit Intelligent Quantization



従来の量子化は全レイヤーに均一な精度を適用します。*MoziSmartBit Intelligent Quantization**は、サイズと精度の最適バランスのために差別化された量子化戦略を適用します。



### 圧縮効果



従来の量子化はモデルの全部分を均一に圧縮し、しばしば著しい精度損失を引き起こします。MoziSmartBit Intelligent Quantizationは自社開発のインテリジェント圧縮戦略を使用して*最小限の精度損失で大幅なサイズ削減を実現*します：



- **最小限の量子化損失**: 訓練効果 > 量子化損失。訓練されたMoziAI-35Bは金融ドメインテキストにおいて、事前学習bf16ベースモデルよりも良好なPPLを達成し、類似AIモデルと比較してハルシネーションとパープレキシティを削減

- **約4.5倍のサイズ削減*: 約70 GB（FP16）から約15.5 GBに圧縮、Q4_K_M（約21 GB）よりも大幅に小さく、VRAMとストレージ要件を著しく削減

- **コンシューマGPUフレンドリー**: 以前はハイエンドGPUが必要だった35B MoEモデルが20GB/24GB VRAMでスムーズに動作



### 比較優位性



**Q4_K_M（約22 GB）と比較**: 約30%小型化（検5.5 GB）、精度はQ4_K_M**より高く**、VRAM障壁が低下→ミドルレンジコンシューマGPU（24GB）でスムーズに動作成



**FP16オリジナル（検0 GB）と比較**: 約4.5倍の圧縮、訓練有効+ 最小限の量子化損失（訓練効果> 量子化損失）、プロフェッショナルグレードのハードウェアではなくコンシューマGPUでローカル56Kコンテキストデプロイが可能力



## 推奨推論パラメーマ



ローカル本番環境の設定に基づく（AMD Radeon AI PRO R9700 32GB）：



| パラメータ | 値 | 説明 |
|-----------|-----|------|
| temperature | 0.6 | 創造性と正確性のバランス |
| top_p | 0.95 | ニュークルサムプリングしきいま|
| top_k | 20 | トランケーションサプリング（V3.7最適化ソ|
| repeat_penalty | 1.05 | 繰り返しペナルテキ|
| presence_penalty | 0 | presenceペナルティなど|
| context_length | 262144 | 256K長コンテキスト|
| batch_size | 2048 | バッチサイズ |
| ubatch_size | 512 | マイクロバッチサイズ |
| flash_attention | auto | 自動Flash Attention |
| kv_cache | q4_0 | KVキャッシュ量子化（kv-unified）|
| poll | 0 | アイドル時GPUポーリングなし、省エネ |
| reasoning | on | 推論チェーン（chain of thought）を有効果|
| reasoning_budget | 400 | 推論予算（トークン数の|
| reasoning_format | deepseek-legacy | 推論フォーマット |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | サンプラー順序|
### llama.cpp起動コマンド



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



### VRAM設定の推論



ユーザーのGPU構成は大きく異なるため、異なるVRAMサイズの推奨パラメータを以下に示します（すべてMoziSmartBit版用）：



| VRAM | 推奨コンテキスト | KVキャッショ| Visionサポート | 備考|
|------|-----------------|-------------|---------------|------|
| 20 GB | 150K | q4_0 | サポートあり | モデルvision 約16.4GB、実測で200K+vision使用時のVRAM消費は約19.5GB |
| 24 GB | 256Kフル | q4_0 | 完全サポート | Vision+256K長コンテキスト、VRAM消費約20.4GB、ヘッドルーム約3.6GB |
| 32 GB+ | 256Kフル | q4_0 | 完全サポート | Vision+256K長コンテキスト、十分なヘッドルームワ0GB、最適構成|
**NVIDIA**



| VRAM | GPUモデル|
|------|-----------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD**



| VRAM | GPUモデル|
|------|-----------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel**



| VRAM | GPUモデル|
|------|-----------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50（CPUオフロードが必要な|
**共有メモリiGPU**



| VRAM | プロセット|
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S iGPU）|
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU）|
> 💡 **ヒンテ*: 上記のVRAM要件を満たしていれば動作します。ブランドやモデルの制限はありません。NVIDIA / AMD / IntelのディスクリートGPU、および上記の28GB統合メモリiGPUをサポートしています。



> 💡 **ヒンテ*: コンテキストが長くなるほどVRAMを多く使用します。OOM（メモリ不足）が発生した場合は、`-c`の値を段階的に減らしてください。`--fit on`を使用すると、llama.cppがVRAMに合わせて自動的にレイヤーを調整します。



### Ollamaデプロイ



```bash

# Modelfileを作成

FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf



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



LM StudioまたはJanで`moziAI-35B`を検索し、MoziSmartBit量子化版をダウンロードしてくださいま



## ベンチマーク評価



MoziAIは**deepreinforce-ai/Ornith-1.5-35B-A3B**からファインチューニングされています。MoziAIはベースモデルの上で金融垂直ドメインの最適化が施されており、金融Q&A、クオンツプログラミング、tool callingシナリオにおいて優れた性能を発揮します。MoziAI-35Bの汎用能力はOrnith-1.5-35B-A3Bベースモデルと一致しています。



| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
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
> MoziAI-35Bの汎用ベンチマークスコアはOrnith-1.5-35B-A3Bベースモデルと一致しています。金融垂直ドメインはMoziAIのコア最適化方向であり、財務報告分析、クオンツ戦略、リスク＆コンプライアンス、エージェントtool callingなどのシナリオで汎用モデルを大幅に上回ります。Gemma4およびQwen3.6のデータは公式公開結果からの引用です。



## モデルダウンローマ



モデルサイズが大きく（約15.5 GB）、複数のコミュニティプラットフォームでホストされています。



| プラットフォーム | URL |
|----------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio ユーザー**：[LM Studio](https://lmstudio.ai) で`moziAI` を検索し、ワンクリックでダウンロードできます。

> 💡 **ダウンロードのヒンテ*: 上記リンクをクリックしてHuggingFaceリポジトリに移動して*「Files and versions）**タブでV3.7ディレクトリ配下のすべてのファイルをダウンロードしてください（メインモデル、vision射影、チャットテンプレート）をつのファイルすべてを同じディレクトリに配置してくださいま



### ⚠️ 重要：Vision機能にはmmprojファイルが必要です



このモデルはマルチモーダルvisionをサポートしています。*vision射影ファイル（mmproj）**はバージョンディレクトリに含まれています。



- **Visionファイル**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`（約903 MB、BF16精度を

- **配置場所**: GGUFモデルファイルと同じバージョンディレクトを

- **読み込み**: llama-server起動時に`--mmproj`フラグを使用して読み込み



```bash

llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf

```



> visionファイルがない場合、モデルの*画像理解機能を失が*、テキストのみの会話のみが可能になります。



## クイックスタート



### 1. モデルファイルをダウンローマ



HuggingFace / ModelScopeからV3.7ディレクトリ配下のすべてのファイルをダウンロード：



```

V3.7/

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # メインモデル（必須）

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision射影（オプションテ

└── moziAI-V3.7-35B-chat-template.jinja                  # チャットテンプレート（推奨）

```



### 2. 推論サーバーを起動



完全な推奨設定については、上記の[llama.cpp起動コマンド](#llamacpp起動コマンド)を参照してくださいま



最小限の起動（コアパラメータのみ）を



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 262144 -ngl 99

```



> vision機能を追加するには`--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`を追加してくださいま



### 3. 使用開始



ブラウザで`http://localhost:8080`を開いてチャットを開始します。



### ディレクトリ構成



```

moziAI-35B/

├── README.md              # 中文コ

├── README.en.md           # 英語モ

├── README.ja.md           # このファイル（日本語モ

├── LICENSE                # ライセンテ

├── V3.7/                  # V3.7バージョン（自己完結型）

├── RELEASE_NOTES.md                       # リリースノーマ

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # メインモデル

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision射影

└── moziAI-V3.7-35B-chat-template.jinja   # チャットテンプレート

```



将来のアップグレード計画については、[未来升级计划.md](未来升级计划.md)を参照してくださいま



## SEOキーワーマ



financial AI LLM, ローカルオープンソースモデル, エッジサイドモデル クオンツプログラミンテ MoziSmartBit, インテリジェント量子化 GGUF量子化 MoEモデル ローカルオープンソースLLM, ローカルデプロイ, 金融AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, 検閲なし, 自由出力, 制限なし, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, 金融垂直ドメイン, オープンソースモデル



## ライセンス（重要な



このモデルは**カスタム制限付きライセンテ*を使用しています。



### ✅ 許可事項

- **無料商用利用**: 商製品に統合自由

- **複製＆配置*: コピー、ダウンロード、共有が可能



### ❌ 禁止事項

- **派生作品**: モデルまたはその一部の修正、翻訳、適応、統合、ファインチューニング禁止。

- **再販**： モデル単体または製品の一部としての販売禁止。

- **再ライセンス**: サブライセンスの付与禁止



### 📋 要件

- 元の著作権表示を保持すること

- 表記: moziAI-35B



> 完全な条款については[LICENSE](./LICENSE)を参照してくださいま



## 免責事項



現状有姿で保証なしに提供されます。モデル出力は参考情報であり、投資助言ではありません。ユーザーはすべてのリスクを負います。



## お問い合わせ



- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)

- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)

- **Weibo**: [@rimochen](https://weibo.com/rimochen)

- **E-mail**: 263515@qq.com



---



Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.