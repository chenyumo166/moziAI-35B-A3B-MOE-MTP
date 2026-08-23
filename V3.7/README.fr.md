---
language:
- fr
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

# MoziAI-V3.7-35B-A3B-MOE - IA multimodale puissante et compacte, dÃ©ployable gratuitement en local

FranÃ§ais | [ä¸­æ](README.md) | [English](README.en.md)

## PrÃ©sentation du modÃ¨le

MoziAI-35B-A3B-MOE est un LLM multimodal financier open-source local (supportant la vision et le tool calling), dÃ©veloppÃ© par l'Ã©quipe de l'influenceur financier chinois Chen Yumo, affinÃ©/distillÃ© Ã  partir du modÃ¨le de base Ornith-1.5-35B-A3B (**architectures Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, licence MIT). GrÃ¢ce Ã  la technologie **MoziSmartBit Intelligent Quantization** dÃ©veloppÃ©e en interne, le modÃ¨le MoE Ã  35B de paramÃ¨tres est compressÃ© Ã  environ **15,5 Go**, atteignant un Ã©quilibre optimal entre prÃ©cision et taille avec une qualitÃ© de prÃ©cision quasi intacte de ~99%.

En plus de conserver les capacitÃ©s gÃ©nÃ©rales de l'IA, ce modÃ¨le se concentre sur l'optimisation des applications verticales dans le domaine financier, y compris les questions-rÃ©ponses financiÃ¨res, la programmation quantitative, le tool calling et la programmation gÃ©nÃ©rale.

Le dÃ©veloppeur du modÃ¨le Chen Yumo utilise frÃ©quemment ce modÃ¨le pour l'analyse locale de donnÃ©es financiÃ¨res, le R&D de stratÃ©gies quantitatives, la recherche de marchÃ©, la rÃ©daction d'articles, l'avancement global des projets, la programmation gÃ©nÃ©rale et les tÃ¢ches avec contexte 256K via OpenClaw/Hermes. Il peut Ãªtre dÃ©ployÃ© localement sur des GPUs grand public, gÃ©nÃ©rant des Ã©conomies substantielles de coÃ»ts de tokens cloud, atteignant la libertÃ© de tokens 7j/24h tout en garantissant la confidentialitÃ© et la sÃ©curitÃ© des donnÃ©es locales.

Supporte llama.cpp, Ollama, LM Studio et d'autres frameworks d'infÃ©rence grand public.

**Date de publication : 2026-08-21** | **Version : V3.7**

## CaractÃ©ristiques du modÃ¨le

- **Focus financier vertical** : Optimisation approfondie pour les questions-rÃ©ponses financiÃ¨res, la programmation quantitative et le tool calling
- **MoziSmartBit Intelligent Quantization** : Quantification intelligente dÃ©veloppÃ©e en interne, meilleur Ã©quilibre prÃ©cision/taille, compressÃ© Ã  environ **15,5 Go**
- **DÃ©ploiement grand public** : DÃ©ployable sur des GPUs grand public avec 20 Go ou 24 Go+ de VRAM, supporte les contextes longs de 256K
- **Support multilingue** : 201 langues et dialectes, avec des capacitÃ©s renforcÃ©es en chinois, couvrant l'anglais/japonais/corÃ©en/allemand/franÃ§ais/espagnol/portugais et plus
- **Programmation gÃ©nÃ©rale** : DÃ©veloppement full-stack, dÃ©bogage de code, conception d'architecture, Ã©criture de scripts, couvrant Python/JS/TS/Go/Rust et d'autres langages grand public
- **RÃ©daction d'articles** : RÃ©daction multi-genres de haute qualitÃ© incluant des rapports de recherche, des articles d'analyse, de la documentation technique, du contenu crÃ©atif
- **ComprÃ©hension visuelle** : Supporte la vision multimodale, la capture d'Ã©cran locale, la comprÃ©hension d'images
- **Sortie uncensored libre** : Pas de censure de contenu, discussion libre sur tout sujet sans restrictions
- **Raisonnement amÃ©liorÃ©** : EnchaÃ®nement de raisonnement pour une qualitÃ© de raisonnement amÃ©liorÃ©e
- **Support multi-framework** : Compatible avec llama.cpp, Ollama, LM Studio, Jan
- **Support multi-plateforme Agent** : IntÃ©gration profonde avec OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex et d'autres IDE et frameworks Agent grand public, support natif du tool calling et de l'orchestration multi-tours de tÃ¢ches, prÃªt Ã  l'emploi

## Avantages Uncensored

Ce modÃ¨le hÃ©rite de la fonctionnalitÃ© **Uncensored** du modÃ¨le de base Ornith-1.5-35B-A3B, avec les avantages suivants :

| Avantage | Description |
|----------|-------------|
| **Pas de censure** | Ne refusera aucun sujet, y compris les contenus sensibles ou controversÃ©s |
| **Sortie libre** | Non soumis aux politiques de sÃ©curitÃ©, peut gÃ©nÃ©rer n'importe quel type de rÃ©ponse |
| **Informations complÃ¨tes** | Fournit des informations complÃ¨tes non filtrÃ©es, adaptÃ©es Ã  la recherche et Ã  l'analyse |
| **ConfidentialitÃ© locale** | Le dÃ©ploiement local signifie que les donnÃ©es sont totalement privÃ©es et Ã  l'abri de la censure cloud |

> **Cas d'utilisation** : Recherche acadÃ©mique, analyse approfondie, discussion libre, conversation IA sans restriction.
> **Remarque** : Il s'agit d'un modÃ¨le dÃ©ployÃ© localement, le contenu de sortie est entiÃ¨rement contrÃ´lÃ© par l'utilisateur, aucune responsabilitÃ© de modÃ©ration du contenu.

## CapacitÃ©s principales

| Domaine de capacitÃ© | Description |
|---------------------|-------------|
| Analyse de marchÃ© | InterprÃ©tation macro/microÃ©conomique, logique des marchÃ©s actions A/HK/US/matieres premieres/crypto |
| Rapports financiers | InterprÃ©tation des indicateurs financiers clÃ©s, rÃ©sumÃ© de rapports de recherche, aide Ã  l'Ã©valuation et aux prÃ©visions de rÃ©sultats |
| Risque & ConformitÃ© | Ãvaluation des risques produits, conformitÃ© des conseils d'investissement, interprÃ©tation des politiques de rÃ©glementation financiÃ¨re |
| Quant & StratÃ©gie | Conception de stratÃ©gies quantitatives, quantification Pyramid (PEL), logique de backtesting, construction de facteurs et tool calling |
| Tool Calling | IntÃ©gration avec les cotations en temps rÃ©el, les bases de donnÃ©es, la rÃ©cupÃ©ration de rapports de recherche et d'autres sources de donnÃ©es financiÃ¨res |

## SpÃ©cifications techniques

| ÃlÃ©ment | SpÃ©cification |
|---------|---------------|
| ModÃ¨le de base | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, licence MIT) |
| ParamÃ¨tres | 35B MoE (256 experts routÃ©s + 1 expert partagÃ©, 8 actifs par token) |
| Quantification | MoziSmartBit Intelligent Quantization dÃ©veloppÃ© en interne + format standard GGUF |
| Longueur de contexte | 256K (262 144 tokens) |
| Taille du modÃ¨le | ~15,5 Go (version MoziSmartBit Uncensored) |
| VRAM minimum | GPUs grand public avec 20 Go+ de VRAM (ex. : RTX 4060 Ti 16G avec CPU offload), 24 Go recommandÃ©s (avec vision + long contexte) |
| Framework d'infÃ©rence | llama.cpp / Ollama / LM Studio / Jan |
| Vitesse d'infÃ©rence | Optimisation algorithmique : 140+ tokens/s sur GPU AMD R9700, 70+ tokens/s sur iGPU AMD MAX+395 CPU, libertÃ© de tokens locale |
| Ãquipe | Ãquipe Chen Yumo |

## Comparaison des formats de quantification et tailles de modÃ¨le

| Format de quantification | Taille du modÃ¨le | PrÃ©cision | Notes |
|--------------------------|-------------------|-----------|-------|
| **FP16 (original)** | ~70 Go | 100% | Original 16bit |
| **MoziSmartBit** | **~15,5 Go** | **~99%** | **UtilisÃ© par MoziAI, schÃ©ma de quantification optimal** |
| Q4_K_M | ~21,2 Go | ~98% | Standard GGUF 4bit |
| Q5_K_M | ~24,7 Go | ~99% | QualitÃ© supÃ©rieure |
| Q6_K | ~28,5 Go | ~99,5% | Quasi sans perte |
| Q8_0 | ~36,9 Go | ~100% | Sans perte |

> MoziAI V3.7 utilise MoziSmartBit Intelligent Quantization, maintenant ~99% de prÃ©cision tout en compressant le modÃ¨le MoE Ã  35B paramÃ¨tres Ã  ~15,5 Go (~4,5x ratio de compression), Ã©quilibrant la qualitÃ© d'infÃ©rence et l'accessibilitÃ© du dÃ©ploiement pour les GPUs grand public.

## MoziSmartBit Intelligent Quantization

La quantification traditionnelle utilise une prÃ©cision uniforme sur toutes les couches. **MoziSmartBit Intelligent Quantization** applique des stratÃ©gies de quantification diffÃ©renciÃ©es pour un Ã©quilibre optimal taille-prÃ©cision.

### Effet de compression

La quantification traditionnelle comprime toutes les parties du modÃ¨le de maniÃ¨re uniforme, entraÃ®nant souvent une perte significative de prÃ©cision. MoziSmartBit Intelligent Quantization utilise une stratÃ©gie de compression intelligente dÃ©veloppÃ©e en interne qui **rÃ©duit considÃ©rablement la taille avec une perte de prÃ©cision minimale** :

- **Perte de quantification minimale** : Gain d'entraÃ®nement > perte de quantification. Le MoziAI-35B entraÃ®nÃ© atteint un meilleur PPL sur les textes du domaine financier que le modÃ¨le de base bf16 prÃ©-entraÃ®nÃ©, rÃ©duisant les hallucinations et la perplexitÃ© par rapport aux modÃ¨les d'IA similaires
- **RÃ©duction de taille ~4,5x** : CompressÃ© de ~70 Go (FP16) Ã  ~15,5 Go, Ã©galement nettement plus petit que Q4_K_M (~21 Go), rÃ©duisant considÃ©rablement les exigences de VRAM et de stockage
- **Compatible GPU grand public** : Un modÃ¨le MoE Ã  35B qui nÃ©cessitait auparavant des GPU haut de gamme peut dÃ©sormais fonctionner fluide sur 20 Go~24 Go de VRAM

### Avantages comparatifs

**vs Q4_K_M (~21,2 Go)** : ~30% plus petit (~15,5 Go), avec une prÃ©cision **supÃ©rieure** Ã  Q4_K_M, seuil de VRAM plus bas â?fonctionne de maniÃ¨re fluide sur des GPUs grand public milieu de gamme (24 Go).

**vs FP16 original (~70 Go)** : ~4,5x compression, efficacitÃ© d'entraÃ®nement + perte de quantification minimale (gain d'entraÃ®nement > perte de quantification), permettant le dÃ©ploiement local de contexte 256K sur des GPUs grand public au lieu de matÃ©riel haut de gamme professionnel.

## ParamÃ¨tres d'infÃ©rence recommandÃ©s

BasÃ©s sur la configuration de production locale (AMD Radeon AI PRO R9700 32GB) :

| ParamÃ¨tre | Valeur | Description |
|-----------|--------|-------------|
| temperature | 0,6 | Ãquilibre crÃ©ativitÃ© vs prÃ©cision |
| top_p | 0,95 | Seuil d'Ã©chantillonnage nucleus |
| top_k | 20 | Ãchantillonnage de troncature (optimisÃ© V3.7) |
| repeat_penalty | 1,05 | PÃ©nalitÃ© de rÃ©pÃ©tition |
| presence_penalty | 0 | Pas de pÃ©nalitÃ© de prÃ©sence |
| context_length | 262144 | Contexte long 256K |
| batch_size | 2048 | Taille de lot |
| ubatch_size | 512 | Taille de micro-lot |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | Quantification du cache KV (kv-unified) |
| poll | 0 | Pas de polling GPU au ralenti, Ã©conome en Ã©nergie |
| reasoning | on | Activer la chaÃ®ne de raisonnement (chain of thought) |
| reasoning_budget | 400 | Budget de raisonnement en tokens |
| reasoning_format | deepseek-legacy | Format de raisonnement |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | Ordre des Ã©chantillonneurs |

### Commande de lancement llama.cpp

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
  --temp 0,6 --top-p 0,95 --top-k 20
```

### Recommandations de configuration VRAM

Ãtant donnÃ© que les configurations GPU des utilisateurs varient considÃ©rablement, voici les paramÃ¨tres recommandÃ©s pour diffÃ©rentes tailles de VRAM (tous pour la version MoziSmartBit) :

| VRAM | Contexte recommandÃ© | KV Cache | Support de la vision | Notes |
|------|---------------------|----------|----------------------|-------|
| 20 Go | 150K | q4_0 | SupportÃ© | ModÃ¨le+vision ~16,4 Go, tests montrent 200K+vision utilise ~19,5 Go de VRAM |
| 24 Go | 256K complet | q4_0 | Support total | Vision+contexte long 256K, utilise ~20,4 Go de VRAM, ~3,6 Go de marge |
| 32 Go+ | 256K complet | q4_0 | Support total | Vision+contexte long 256K, marge suffisante ~10 Go, meilleure configuration |

**NVIDIA**

| VRAM | ModÃ¨le GPU |
|------|------------|
| 24 Go | RTX 4090 / RTX 3090 Ti |
| 32 Go | RTX 5090 |

**AMD**

| VRAM | ModÃ¨le GPU |
|------|------------|
| 20 Go | RX 7900 XT |
| 24 Go | RX 7900 XTX |
| 32 Go | Radeon AI PRO R9700 |

**Intel**

| VRAM | ModÃ¨le GPU |
|------|------------|
| 32 Go | Arc Pro B70 / Arc Pro B65 |
| 24 Go | Arc Pro B60 |
| 16 Go | Arc Pro B50 (nÃ©cessite CPU offload) |

**MÃ©moire partagÃ©e iGPUs**

| VRAM | Processeur |
|------|------------|
| 128 Go | AMD Ryzen AI Max+ 395 (iGPU Radeon 8060S) |
| 128 Go | NVIDIA RTX Spark (GPU Blackwell RTX) |

> ð¡ **Astuce** : Tant que votre VRAM satisfait les exigences ci-dessus, cela fonctionne. Aucune restriction de marque ou de modÃ¨le. Supporte les GPUs dÃ©diÃ©s NVIDIA / AMD / Intel, ainsi que les iGPUs Ã  mÃ©moire unifiÃ©e 128 Go listÃ©s ci-dessus.

> ð¡ **Astuce** : Un contexte plus long utilise plus de VRAM. Si vous rencontrez un OOM (out of memory), rÃ©duisez progressivement la valeur `-c`. Utilisez `--fit on` pour que llama.cpp ajuste automatiquement les couches Ã  votre VRAM.

### DÃ©ploiement Ollama

```bash
# CrÃ©er le Modelfile
FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf

PARAMETER temperature 0,6
PARAMETER top_p 0,95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Construire et exÃ©cuter
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### DÃ©ploiement LM Studio / Jan

Recherchez `moziAI-35B` dans LM Studio ou Jan, tÃ©lÃ©chargez la version quant MoziSmartBit.

## Ãvaluation Benchmark

MoziAI est affinÃ© Ã  partir de **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI est optimisÃ© pour les domaines financiers verticaux au-dessus du modÃ¨le de base, offrant des performances supÃ©rieures dans les scÃ©narios de questions-rÃ©ponses financiÃ¨res, de programmation quantitative et de tool calling. Les capacitÃ©s gÃ©nÃ©rales de MoziAI-35B sont cohÃ©rentes avec le modÃ¨le de base Ornith-1.5-35B-A3B.

| Benchmark | MoziAI-35B (ce modÃ¨le) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Description |
|-----------|------------------------|-------------|------------|------------|-------------|-------------|
| Terminal-Bench 2.1 | 64,2 | 59,3 | 42,1 | - | 41,4 | Codage terminal autonome |
| Terminal-Bench (Claude Code) | 62,8 | 59,3 | - | - | 38,9 | Codage Claude Code |
| SWE-bench Verified | 75,6 | 77,2 | 52,0 | - | 70,0 | IngÃ©nierie logicielle en conditions rÃ©elles |
| SWE-bench Pro | 50,4 | 53,5 | 35,7 | - | 44,6 | IngÃ©nierie logicielle complexe |
| SWE-bench Multilingual | 69,3 | 71,3 | - | - | 60,3 | Codage multilingue |
| NL2Repo | 34,6 | 36,2 | 15,5 | - | 20,5 | Langage naturel vers dÃ©pÃ´t |
| LiveCodeBench v6 | 63,3 | 83,9 | 80,0 | 77,1 | - | Programmation compÃ©titive |
| GPQA Diamond | 88,4 | 87,8 | 84,3 | 82,3 | - | Raisonnement scientifique |
| AIME 2026 Math | 93,3 | 94,1 | 89,2 | 88,3 | - | Raisonnement mathÃ©matique |

> Les scores benchmarks gÃ©nÃ©raux de MoziAI-35B sont cohÃ©rents avec le modÃ¨le de base Ornith-1.5-35B-A3B. Le domaine financier vertical est la principale direction d'optimisation de MoziAI, surpassant significativement les modÃ¨les gÃ©nÃ©raux dans des scÃ©narios tels que l'analyse de rapports financiers, la stratÃ©gie quantitative, le risque & conformitÃ© et le tool calling d'agents. DonnÃ©es Gemma4 et Qwen3.6 issues de rÃ©sultats publics officiels.

## TÃ©lÃ©chargement du modÃ¨le

En raison de la grande taille du modÃ¨le (~15,5 Go), les poids sont hÃ©bergÃ©s sur plusieurs plateformes communautaires :

| Plateforme | URL |
|------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

> ð¡ **LM Studio** : Vous pouvez rechercher et tÃ©lÃ©charger directement dans [LM Studio](https://lmstudio.ai). Recherchez `moziAI` et cliquez sur TÃ©lÃ©charger.

> ð¡ **Astuce de tÃ©lÃ©chargement** : Cliquez sur le lien ci-dessus pour accÃ©der au dÃ©pÃ´t HuggingFace, puis naviguez vers l'onglet **Â« Files and versions Â»** pour tÃ©lÃ©charger tous les fichiers sous le rÃ©pertoire V3.7 (modÃ¨le principal, projection visuelle, modÃ¨le de chat). Assurez-vous que les trois fichiers se trouvent dans le mÃªme rÃ©pertoire.

### â ï¸ Important : La capacitÃ© visuelle nÃ©cessite le fichier mmproj

Ce modÃ¨le supporte la vision multimodale. Le **fichier de projection visuelle (mmproj)** est inclus dans le rÃ©pertoire de version :

- **Fichier vision** : `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 Mo, prÃ©cision BF16)
- **Placement** : Dans le mÃªme rÃ©pertoire de version que le fichier modÃ¨le GGUF
- **Chargement** : Charger avec le drapeau `--mmproj` lors du dÃ©marrage de llama-server

```bash
llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf
```

> Sans le fichier vision, le modÃ¨le **perdra la capacitÃ© de comprÃ©hension d'images** et ne conservera que la conversation textuelle.

## DÃ©marrage rapide

### 1. TÃ©lÃ©charger les fichiers du modÃ¨le

TÃ©lÃ©chargez tous les fichiers du rÃ©pertoire V3.7 depuis HuggingFace / ModelScope :

```
V3.7/
âââ moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # ModÃ¨le principal (requis)
âââ moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Projection visuelle (optionnel)
âââ moziAI-V3.7-35B-chat-template.jinja                  # ModÃ¨le de chat (recommandÃ©)
```

### 2. DÃ©marrer le serveur d'infÃ©rence

Pour la configuration complÃ¨te recommandÃ©e, voir [Commande de lancement llama.cpp](#commande-de-lancement-llamacpp) ci-dessus.

Lancement minimal (paramÃ¨tres principaux uniquement) :

```bash
llama-server \
  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Ajoutez `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` pour la capacitÃ© visuelle.

### 3. Commencer Ã  utiliser

Ouvrez `http://localhost:8080` dans votre navigateur pour commencer Ã  discuter.

### Structure du rÃ©pertoire

```
moziAI-35B/
âââ README.md              # Version chinoise
âââ README.en.md           # Version anglaise
âââ README.fr.md           # Version franÃ§aise (ce fichier)
âââ LICENSE                # Licence
âââ V3.7/                  # Version V3.7 (autonome)
â?  âââ RELEASE_NOTES.md                       # Notes de version
â?  âââ moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # ModÃ¨le principal
â?  âââ moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Projection visuelle
â?  âââ moziAI-V3.7-35B-chat-template.jinja   # ModÃ¨le de chat
```

Pour le plan de mise Ã  jour futur, voir [æªæ¥åçº§è®¡å.md](æªæ¥åçº§è®¡å.md).

## Mots-clÃ©s SEO

LLM IA financiÃ¨re, modÃ¨le open-source local, modÃ¨le de bord, programmation quantitative, MoziSmartBit, quantification intelligente, quantification GGUF, modÃ¨le MoE, LLM open-source local, dÃ©ploiement local, IA financiÃ¨re, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, pas de censure, sortie libre, sans restriction, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, domaine financier vertical, modÃ¨le open-source

## Licence (Important)

Ce modÃ¨le utilise une **Licence restrictive personnalisÃ©e** :

### â?AutorisÃ©
- **Utilisation commerciale libre** : Libre d'intÃ©grer dans des produits commerciaux
- **Copie & Distribution** : Peut Ãªtre copiÃ©, tÃ©lÃ©chargÃ© et partagÃ©

### â?Interdit
- **Åuvres dÃ©rivÃ©es** : Aucune modification, traduction, adaptation, fusion ou affinage du modÃ¨le ou d'une partie de celui-ci
- **Revente** : Pas de vente du modÃ¨le seul ou dans le cadre d'un produit
- **Relicenciement** : Pas de concession de sous-licences

### ð Exigences
- Doit conserver la mention de copyright originale
- Attribution : moziAI-35B

> Voir [LICENSE](./LICENSE) pour les conditions complÃ¨tes.

## Avertissement

Fourni Â« en l'Ã©tat Â» sans garantie. La sortie du modÃ¨le est uniquement Ã  titre indicatif, pas un conseil en investissement. Les utilisateurs assument tous les risques.

## Contact

- **HuggingFace** : [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub** : [@chenyumo166](https://github.com/chenyumo166)
- **Weibo** : [@rimochen](https://weibo.com/rimochen)
- **E-mail** : 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. Tous droits rÃ©servÃ©s.
