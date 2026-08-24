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
library_name: llama-cpp
pipeline_tag: text-generation
---

# moziAI-13.7-35B-A3B-A3B-MOE-MTP-Uncensored - 無料でローカル展開可能なコンパクトで高性能なマルチモーダルAIモデル

Language / 言語選択  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## モデル概要

MoziAI-35B-A3B-MOE は、中国の金融系インフルエンサー陳雨墨チームが開発したローカルオープンソースのマルチモーダルAI大規模言語モデルです（金融分野を強化、視覚対応、ツール呼び出し、複雑な長文タスク処理、コンシューマー向けGPUでのローカル展開に対応）。moziAI-35Bはオープンソース基盤モデル Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B アーキテクチャ、MITライセンス）に基づき、陳雨墨チームの自社開発：（金融データ + 金融領域能力 + トレーニング手法 + 七次元思考体系 + エージェントLOOPメカニズム + ハイブリッド量子化アルゴリズム MoziSmartBit）を組み合わせて開発されています。自社開発のMoziSmartBit インテリジェント量子化技術により、350億パラメータのMoEモデルは約15.5 GBに圧縮され、従来のQ4_K_M量子化モデル（約22+GB）より6.5G（約30%）小さくなっています。精度とサイズの最適なバランスを実現し、ほぼロスレスな≈FP16の99%の精度品質を実現しています。

本モデルの開発チームの理念は、総合的な能力を持つローカルAI大規模言語モデルエージェントを一般家庭や中小企業に普及させ、高額なAIハードウェアコストやクラウドAPIコストを不要にすることです。独自開発の**MoziSmartBit インテリジェント量子化**技術により、350億パラメータのMoEモデルを約 **15.5 GB** に圧縮し、モデル精度とサイズの最適なバランスを実現し、FP16の約99%の精度品質を達成しています。本モデルは350億パラメータを持ちますが、MOEスパースエキスパート技術により実際に起動するのは30億パラメータのみで、MTP投機的デコードによる推論の高速化も可能です。実測では、20GB VRAMの家庭用コンシューマーGPUでローカル無料展開が可能で、140+ token/sの推論速度を実現しており、多くのクラウド有料AIモデルよりも高速です。

本モデルは、汎用AI大規模言語モデルの機能を維持しつつ、金融垂直分野の応用、金融Q&A、定量プログラミング、汎用プログラミング、ツール呼び出し、256Kの複雑な長文コンテキストタスクの成功率など、AI大規模言語モデルの重要な機能を重点的に最適化しています。ローカルのコンシューマー向けGPUで無料展開して使用でき、クラウドのトークンコストを大幅に節約し、7X24時間のトークンフリーを実現するとともに、ローカルデータのプライバシーとセキュリティを確保します。

**リリース日：** 2026-08-20 | **バージョン：V3.6**

## モデルのダウンロード

モデルファイルが大きい（~15.5 GB）ため、モデルの重みは複数のコミュニティプラットフォームでホスティングされています：

| プラットフォーム | アドレス |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio ユーザー**：[LM Studio](https://lmstudio.ai) で `moziAI` を直接検索してワンクリックでダウンロードできます。手動でファイルをダウンロードする必要はありません。  
> 💡 **ダウンロードのヒント**：上記のリンクをクリックして HuggingFace リポジトリに入り、**"Files and versions"** タブから V3.6 ディレクトリ内のすべてのファイル（メインモデル、視覚プロジェクション、チャットテンプレート）をダウンロードしてください。3つのファイルが同じディレクトリに配置されるようにしてください。

### ⚠️ 重要：視覚機能には mmproj ファイルの追加が必要です

本モデルはマルチモーダル視覚に対応しており、視覚プロジェクションファイル（mmproj）はバージョンディレクトリに含まれています：

- **視覚ファイル**：`moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`（約 903 MB、BF16 精度）
- **配置場所**：GGUF モデルファイルと同じバージョンディレクトリ
- **読み込み方法**：llama-server 起動時に `--mmproj` パラメータで読み込み

> 視覚ファイルを読み込まないと画像理解機能が失われ、純テキストの対話機能のみになります。

### ⚠️ 重要：チャットテンプレートファイルの読み込みは必須です

本モデルは専用のチャットテンプレート（chat-template）を使用しており、**読み込まないと対話フォーマットエラー、推論チェーンの失敗、応答品質の大幅な低下の原因となります**。チャットテンプレートファイルはバージョンディレクトリに含まれています：

- **テンプレートファイル**：`moziAI-V3.6-35B-chat-template.jinja`（約 5 KB、jinja フォーマット）
- **配置場所**：GGUF モデルファイルと同じバージョンディレクトリ
- **読み込み方法**：llama-server 起動時に `--chat-template-file` パラメータで読み込み

> チャットテンプレートを読み込まないと、モデルがシステムプロンプト、ユーザーメッセージ、思考ブロックを正しく認識できず、出力フォーマットの混乱や推論能力の低下を引き起こす可能性があります。

### llama.cpp 起動コマンド（20G+ GPUで256Kコンテキストを有効にする推奨設定）

> 備考：VRAM が 20G 未満の場合は、`-c 262144` のコンテキスト設定パラメータ 262144 を減らしてください。

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

## クイックスタート

### 1. モデルファイルのダウンロード

HuggingFace / ModelScope から V3.6 ディレクトリ内のすべてのファイルをローカルにダウンロードします：

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # メインモデル（必須）
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # 視覚プロジェクション（オプション、視覚機能が必要な場合にダウンロード）
└── moziAI-V3.6-35B-chat-template.jinja                  # チャットテンプレート（必須！読み込まないと対話フォーマットエラーが発生）
```

> ⚠️ **チャットテンプレートは必須ファイル**であり、オプションではありません。本モデルにはカスタムの対話フォーマット（推論チェーン/思考ブロックを含む）があり、テンプレートが欠けているとモデルの出力フォーマットが混乱し、推論能力が失われます。必ずダウンロードして起動時に読み込んでください。

### 2. 推論サービスの起動

完全な推奨設定の起動コマンドについては、以下の [llama.cpp 起動コマンド](#llamacpp-起動コマンド) の章を参照してください。

最も簡単な起動（コアパラメータのみ）：

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 視覚機能が必要な場合は `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` を追加してください

### 3. 使用開始

ブラウザで `http://localhost:8080` を開くと対話を開始できます。

### ディレクトリ構成

```
moziAI-35B/
├── README.md              # 英語マニュアル
├── README.ja.md           # 本ファイル（日本語マニュアル）
├── LICENSE                # ライセンス
├── V3.6/                  # V3.6 バージョン（バージョン自己完結型）
│   ├── RELEASE_NOTES.md                       # バージョン更新情報
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # メインモデル
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # 視覚プロジェクション
│   └── moziAI-V3.6-35B-chat-template.jinja   # チャットテンプレート
```

## モデルの特長

- **MoziSmartBit インテリジェント量子化**：独自開発のインテリジェント量子化技術により、精度とサイズの最適なバランスを実現。モデルをほぼ無劣化で約 **15.5 GB** に圧縮
- **複雑な長文タスク処理能力**：モデルエージェントがタスクを自動計画するインテリジェントループ処理の障害点対応と自己思考メカニズムをトレーニングし、複雑なタスクの自動実行と自己調整を実現。ユーザーがエージェントにプロンプトを最適化し続ける手間を削減
- **小規模モデル・高性能**：複雑なタスクの実行において、同クラスの350億パラメータ以内のモデルより総合能力が優れており、パラメータ数が数倍大きいモデルの一部をも上回る
- **MOE+MTPの速度優位性**：モデル全体は350億パラメータですが、実際に起動するのは8+1エキスパートの計30億パラメータのみで、推論速度がより高速。20GB~24GB VRAMの家庭用コンシューマーGPUでローカル展開可能で、140+ token/sの推論速度を享受可能
- **金融垂直分野の深耕**：金融Q&A、定量プログラミング、ツール呼び出し機能を強化
- **コンシューマー向け展開**：20GB~24GB VRAM以上の家庭用コンシューマーGPUでローカル展開可能。最大 256K の長文コンテキスト推論に対応
- **多言語対応**：201 の言語と方言に対応。中国語能力を特別に最適化し、英語、日本語、韓国語、ドイツ語、フランス語、ポルトガル語などの主要言語にも対応
- **汎用プログラミング能力**：フルスタック開発、コードデバッグ、アーキテクチャ設計、スクリプト作成に対応。Python/JS/TS/Go/Rust などの主要言語をカバー
- **文章作成能力**：研究レポート、分析記事、技術文書、クリエイティブコンテンツなど、多ジャンルの高品質なライティングに対応
- **視覚理解**：推論フレームワークに視覚ファイルを読み込むことでマルチモーダル視覚に対応。ローカルでスクリーンショットをチャットウィンドウに貼り付けると、モデルが画像内の情報を理解可能
- **検閲なしの自由な出力**：コンテンツ検閲の制限がなく、あらゆるトピックを自由に議論可能。セキュリティポリシーによる制約を受けない
- **推論論理の強化**：推論論理（思考連鎖）を組み合わせてトレーニングし、推論品質をさらに向上
- **マルチフレームワーク対応**：llama.cpp、Ollama、LM Studio、Jan などの主要な推論フレームワークと互換性あり
- **マルチAgentプラットフォーム対応**：OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex など、国内外の主要な AI IDE と Agent フレームワークに深く対応。ツール呼び出しとマルチラウンドタスクオーケストレーションをネイティブにサポートし、すぐに使用可能

## Uncensored（検閲なし）のメリット

本モデルは、ベースモデル Ornith-1.0-35B-A3B の Uncensored（検閲なし）特性を継承しており、以下のメリットがあります：

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>メリット</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr>
<td>検閲制限なし</td>
<td>センシティブで物議を醸すコンテンツを含め、いかなるトピックも拒否しない</td>
</tr>
<tr>
<td>自由な出力</td>
<td>セキュリティポリシーによる制約を受けず、あらゆる種類の応答を生成可能</td>
</tr>
<tr>
<td>完全な情報</td>
<td>フィルタリングされていない完全な情報を提供。研究や分析シーンに適している</td>
</tr>
<tr>
<td>ローカルプライベート</td>
<td>ローカル展開はデータが完全にプライベートであることを意味し、クラウド検閲の影響を受けない</td>
</tr>
</tbody>
</table>

> **適用シーン**：無料商用、学術研究、深度分析、自由な議論、制限のないAI対話
> **注意**：本モデルはローカル展開モデルであり、出力内容は完全にユーザーが制御します。コンテンツ検閲の責任は負いかねます。

## コア機能

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>機能領域</th>
<th>説明</th>
</tr>
</thead>
<tbody>
<tr>
<td>市場分析</td>
<td>マクロ/ミクロ経済の解釈、A 株/香港株/米国株/商品/暗号資産の相場と論理の整理</td>
</tr>
<tr>
<td>財務と研究レポート</td>
<td>決算報告書の主要指標の解釈、研究レポートの要約抽出、バリュエーションと収益予測の支援</td>
</tr>
<tr>
<td>リスク管理とコンプライアンス</td>
<td>商品のリスク評価、投資助言のコンプライアンス提示、金融規制政策の解釈</td>
</tr>
<tr>
<td>定量とストラテジー</td>
<td>定量ストラテジーのアイデア設計、ピラミッド（Pyramid/PEL）定量、バックテストロジック、ファクター構築とツール呼び出し</td>
</tr>
<tr>
<td>ツール呼び出し</td>
<td>リアルタイム相場、データベース、研究レポート検索などの金融データに接続可能</td>
</tr>
</tbody>
</table>

## 技術仕様

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>項目</th>
<th>パラメータ</th>
</tr>
</thead>
<tbody>
<tr>
<td>ベースモデル</td>
<td>Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B アーキテクチャ、MIT ライセンス）</td>
</tr>
<tr>
<td>パラメータ規模</td>
<td>350億（35B）MoE アーキテクチャ、256 個のルーティングエキスパート + 1 個の共有エキスパート、各トークンで 8 個のエキスパートを起動</td>
</tr>
<tr>
<td>量子化方式</td>
<td>独自開発の MoziSmartBit インテリジェント量子化アルゴリズム + GGUF 標準フォーマットを採用</td>
</tr>
<tr>
<td>コンテキスト長</td>
<td>256K (262,144 tokens)</td>
</tr>
<tr>
<td>モデルサイズ</td>
<td>~15.5 GB（MoziSmartBit Uncensored バージョン）</td>
</tr>
<tr>
<td>最低VRAM要件</td>
<td>20GB VRAM以上の家庭用コンシューマーGPU（RTX 3060 12G はCPUオフロードとの併用が必要、RTX 4060 Ti 16G など）。推奨は 24 GB（視覚 + 長文コンテキストを含む）</td>
</tr>
<tr>
<td>推論フレームワーク</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>推論速度</td>
<td>アルゴリズム最適化により、AMD Radeon AI PRO R9700 GPUで 140+token/s / AMD Ryzen AI Max+ 395 内蔵GPUで 70+token/s を達成。ローカルで自由な推論出力を実現</td>
</tr>
<tr>
<td>開発チーム</td>
<td>陳雨墨チーム</td>
</tr>
</tbody>
</table>

## 量子化フォーマットとモデルサイズの比較

| 量子化フォーマット | モデルサイズ | 精度保持率 | 説明 |
| ---------------- | ------------- | --------- | ----------------- |
| FP16（オリジナル） | ~70 GB | 100% | オリジナル 16bit 精度 |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **本モデルが採用する独自開発のインテリジェント量子化ソリューション** |
| Q4_K_M | ~22 GB | ~98% | GGUF 標準 4bit |
| Q5_K_M | ~24.7 GB | ~99% | より高い精度 |
| Q6_K | ~28.5 GB | ~99.5% | ほぼ無劣化 |
| Q8_0 | ~36.9 GB | ~100% | 無劣化 |
> MoziAI V3.6 は MoziSmartBit インテリジェント量子化ソリューションを採用し、約99%の精度を維持しつつ、350億パラメータのMoEモデルを約15.5 GBに圧縮。圧縮比は約4.5xで、推論品質と展開のハードルのバランスを取り、コンシューマー向けGPUでのローカル展開により適しています。

## MoziSmartBit インテリジェント量子化技術

従来の量子化ソリューションはすべてのレイヤーに統一された精度を使用しますが、陳雨墨チームが独自開発した**MoziSmartBit インテリジェント量子化**は、MoEモデルの構造的特徴に対してインテリジェントな差別化量子化戦略を採用し、サイズと精度の最適なバランスを実現しています。モデル品質は Q4_K_M フォーマットより高く、サイズはわずか ~15.5 GB、圧縮比は ~4.5x です。

### 圧縮効果

従来の量子化ソリューションはモデルのすべての部分を統一的に圧縮するため、精度の損失が顕著になることがよくあります。MoziSmartBit インテリジェント量子化は独自開発のインテリジェント圧縮戦略を採用し、**ごくわずかな精度損失で大幅なサイズ圧縮を実現**します：

- **量子化精度の損失が極小**：トレーニングゲイン > 量子化損失。トレーニング後の MoziAI-35B は金融分野のテキストにおける PPL がトレーニング前の bf16 ベースモデルより優れており、同様の AI モデルの幻覚と困惑を低減
- **モデルサイズが 4.5 倍に圧縮**：FP16 の ~70 GB から ~15.5 GB に圧縮。Q4_K_M の ~22 GB よりも大幅に小さく、VRAM とストレージのハードルを大幅に引き下げ
- **コンシューマー向けGPUで実行可能**：従来はハイエンドGPUが必要だった 35B MoE 大規模モデルが、20GB~24GB VRAM でスムーズに展開可能に

### 比較優位

**vs Q4_K_M（~22 GB）**：サイズが約 30% 削減（~15.5 GB）、精度は Q4_K_M より**高く**、VRAM のハードルが低く、ミッドレンジのコンシューマー向けGPU（20GB）でスムーズに展開可能。

**vs オリジナル FP16（~70 GB）**：サイズが約 4.5 倍に圧縮、トレーニングの効果 + 量子化精度の損失が極小（トレーニングゲイン > 量子化損失）。プロフェッショナル向けGPU（48GB+）が必要だったものが、コンシューマー向けGPUで 256K の長文コンテキストをローカル実行可能に。

## 推奨推論パラメータ

ローカル実行構成（AMD Radeon AI PRO R9700 32GB）に基づき、推奨パラメータは以下の通りです：

| パラメータ | 推奨値 | 説明 |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | 創造性と正確性のバランス |
| top_p | 0.95 | 核サンプリングの閾値 |
| top_k | 20 | 打ち切りサンプリング |
| repeat_penalty | 1.05 | 繰り返しペナルティ |
| presence_penalty | 0 | 存在ペナルティなし |
| context_length | 262144 | 256K 長文コンテキスト |
| batch_size | 2048 | バッチ処理サイズ |
| ubatch_size | 512 | マイクロバッチサイズ |
| flash_attention | auto | 自動 Flash Attention |
| kv_cache | q4_0 | KV キャッシュ量子化（統一 kv-unified） |
| poll | 0 | アイドル時にGPUをポーリングしない、省電力・低遅延 |
| reasoning | on | 推論チェーン（思考連鎖）を有効化 |
| reasoning_budget | 400 | 推論予算のトークン数 |
| reasoning_format | deepseek-legacy | 推論フォーマット |
| samplers | top_k;top_p;temperature;typ_p | サンプラーの順序 |
### 異なるVRAM構成の推奨

ユーザーのGPU構成は多様であるため、以下に異なるVRAMでの推奨パラメータを示します（いずれも MoziSmartBit バージョン）：

| VRAM | 推奨コンテキスト長 | KV キャッシュ | 視覚サポート | 説明 |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | 対応 | モデル+視覚で計~16.4GB、実測で 128K+視覚でVRAM使用量は~19.5GB |
| 24 GB | 256K フル設定 | q4_0 | 完全対応 | 視覚+256K長文コンテキスト、VRAM使用量は~20.4GB、VRAM余量は~3.6GB |
| 32 GB+ | 256K フル設定 | q4_0 | 完全対応 | 視覚+256K長文コンテキスト、VRAM余量は約10GBと十分、最強構成 |
**NVIDIA GPU 参考表**

| VRAM | GPU モデル |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD GPU 参考表**

| VRAM | GPU モデル |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel GPU 参考表**

| VRAM | GPU モデル |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50（CPUオフロードとの併用が必要） |
**CPU共有メモリ内蔵GPU デバイス参考表**

| VRAM | プロセッサモデル |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S 内蔵GPU） |
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU） |
> 💡 **ヒント**：VRAM が上記の要件を満たしていれば使用可能です。ブランドやモデルは問わず、NVIDIA / AMD / Intel 各ブランドの独立GPUに対応するほか、128GBの統一メモリを搭載した内蔵GPU/CPUにも対応しています。
>
> 💡 **ヒント**：コンテキストが長いほど、VRAMの使用量が多くなります。VRAM不足（OOM）が発生した場合は、`-c` パラメータの値を段階的に下げてください。`--fit on` パラメータを使用すると、llama.cpp が自動的にレイヤー数を調整してVRAMに適合させます。

### Ollama での展開

```bash
# Modelfile を作成
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# ビルドして実行
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan での展開

LM Studio または Jan で `moziAI-35B` を直接検索し、量子化バージョンを選択してダウンロードするだけです。

## ベンチマーク評価

moziAI-13.7-35B-A3B は **Ornith-1.0-35B**（deepreinforce-ai）をベースにファインチューニングされています。MoziAI は、ベースモデルの優れたエージェントコーディング能力に加え、**金融垂直分野の深度ある最適化**を新たに実装し、金融Q&A、定量プログラミング、ツール呼び出しなどのシーンでより優れたパフォーマンスを発揮します。汎用的な能力は Ornith-1.0-35B ベースモデルと同じです。

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
**Terminal-Bench 2.1 (Terminus-2)**：Harbor/Terminus-2 フレームワークを使用して評価。設定 `parser=json`、`temperature=1.0`、`top_p=1.0`、128K コンテキストウィンドウ。実行ごとに 4 時間のタイムアウト、32 コア 48GB メモリ、結果は 5 回の平均値。  
**Terminal-Bench 2.1 (Claude Code)**：Claude Code 2.1.126 を使用して評価。設定 `parser=json`、`temperature=1.0`、`top_p=1.0`、`max_new_tokens=131072`。結果は 5 回の平均値。  
**SWE-bench Verified, Pro and Multilingual**：OpenHands フレームワークを使用して評価。設定 `temp=1.0`、`top_p=0.95`、256K コンテキストウィンドウ。  
**NL2Repo**：設定 `temperature=1.0`、`top_p=1.0`、400K コンテキスト、48K 出力。  

> MoziAI-35B は、Ornith-1.0-35B の優れたエージェントコーディング能力を完全に継承しています。MoziAI の中核的な差別化は**金融垂直分野の深度ある最適化**にあり、財務分析、定量ストラテジー、リスク管理・コンプライアンス、エージェントツール呼び出しなどのシーンにおいて、汎用モデルよりもパフォーマンスが大幅に優れています。

## SEO キーワード

金融AI大規模言語モデル、AI大規模言語モデル、ローカルオープンソースモデル、エッジデバイスモデル、定量プログラミング、MoziSmartBit、インテリジェント量子化、GGUF量子化、MoEモデル、ローカルオープンソース大規模言語モデル、ローカル展開、金融AI、ツール呼び出し、Agent、llama.cpp、Ollama、GGUF、Uncensored（検閲なし）、無審査、免審査、自由出力、Q3_K_M、Q4_K_M、Q5_K_M、Q6_K、Q8_0、Ornith-1.0-35B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、金融垂直分野、オープンソースモデル。

## ライセンス（重要）

本モデルは**カスタム制限的ライセンス**を採用しており、具体的な条項は以下の通りです：

✅ **許可**

- 無料商用利用：商業製品やサービスに無料で統合可能
- 複製と配布：そのまま複製、ダウンロード、配布が可能

詳細なライセンス条項については [LICENSE](../LICENSE) ファイルを参照してください。

## 免責事項

本モデルは「現状有姿」で提供され、いかなる形式の保証もいたしません。モデルの出力は参考用であり、投資助言を構成するものではありません。使用者は自身の責任で使用してください。

## お問い合わせ

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

***

Copyright (c) 2026 陳雨墨 / chenyumo166. All rights reserved.