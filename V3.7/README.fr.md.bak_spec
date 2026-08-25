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



# MoziAI-V3.7-35B-A3B-MOE - IA multimodale puissante et compacte, déployable gratuitement en local



[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | Français | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)



## Présentation du modèle



MoziAI-35B-A3B-MOE est un LLM multimodal financier open-source local (supportant la vision et le tool calling), développé par l'équipe de l'influenceur financier chinois Chen Yumo. moziAI-35B est basé sur le modèle de base open-source Ornith-1.5-35B-A3B (architecture Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licence MIT), intégrant les développements propres de l'équipe Chen Yumo : (données financières + capacités du domaine financier + méthodes d'entraînement + cadre de réflexion à sept dimensions + mécanisme LOOP d'agent + algorithme de quantification hybride MoziSmartBit). Grâce à la technologie de quantification intelligente MoziSmartBit développée en interne, le modèle MoE de 35 milliards de paramètres est compressé à environ 15,5 Go, soit 6,5 Go (environ 30%) de moins que les modèles de quantification Q4_K_M conventionnels d'environ 22+ Go ; atteignant l'équilibre optimal entre précision et taille, avec une qualité de précision presque sans perte d'environ 99% de la FP16.



En plus de conserver les capacités générales de l'IA, ce modèle améliore : les applications verticales du domaine financier, les questions-réponses financières, la programmation quantitative, le tool calling et la programmation générale, ainsi que la capacité de réflexion à sept dimensions du modèle, le mécanisme LOOP et la compatibilité avec diverses plateformes d'agents.



Le développeur du modèle Chen Yumo utilise fréquemment ce modèle pour l'analyse locale de données financières, le R&D de stratégies quantitatives, la recherche de marché, la rédaction d'articles, l'avancement global des projets, la programmation générale et les tâches avec contexte 256K via OpenClaw/Hermes. Il peut être déployé localement sur des GPUs grand public, générant des économies substantielles de coûts de tokens cloud, atteignant la liberté de tokens 7j/24h tout en garantissant la confidentialité et la sécurité des données locales.



Supporte llama.cpp, Ollama, LM Studio et d'autres frameworks d'inférence grand public.



**Date de publication : 2026-08-21** | **Version : V3.7**



## Caractéristiques du modèle



- **Focus financier vertical** : Optimisation approfondie pour les questions-réponses financières, la programmation quantitative et le tool calling

- **MoziSmartBit Intelligent Quantization** : Quantification intelligente développée en interne, meilleur équilibre précision/taille, compressé à environ **15,5 Go**

- **Déploiement grand public** : Déployable sur des GPUs grand public avec 20 Go ou 24 Go+ de VRAM, supporte les contextes longs de 256K

- **Support multilingue** : 201 langues et dialectes, avec des capacités renforcées en chinois, couvrant l'anglais/japonais/coréen/allemand/français/espagnol/portugais et plus

- **Programmation générale** : Développement full-stack, débogage de code, conception d'architecture, écriture de scripts, couvrant Python/JS/TS/Go/Rust et d'autres langages grand public

- **Rédaction d'articles** : Rédaction multi-genres de haute qualité incluant des rapports de recherche, des articles d'analyse, de la documentation technique, du contenu créatif

- **Compréhension visuelle** : Supporte la vision multimodale, la capture d'écran locale, la compréhension d'images

- **Sortie uncensored libre** : Pas de censure de contenu, discussion libre sur tout sujet sans restrictions

- **Raisonnement amélioré** : Enchaînement de raisonnement pour une qualité de raisonnement améliorée

- **Support multi-framework** : Compatible avec llama.cpp, Ollama, LM Studio, Jan

- **Support multi-plateforme Agent** : Intégration profonde avec OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex et d'autres IDE et frameworks Agent grand public, support natif du tool calling et de l'orchestration multi-tours de tâches, prêt à l'emploi



## Avantages Uncensored



Ce modèle hérite de la fonctionnalité **Uncensored** du modèle de base Ornith-1.5-35B-A3B, avec les avantages suivants :



| Avantage | Description |
|----------|-------------|
| **Pas de censure** | Ne refusera aucun sujet, y compris les contenus sensibles ou controversés |
| **Sortie libre** | Non soumis aux politiques de sécurité, peut générer n'importe quel type de réponse |
| **Informations complètes** | Fournit des informations complètes non filtrées, adaptées à la recherche et à l'analyse |
| **Confidentialité locale** | Le déploiement local signifie que les données sont totalement privées et à l'abri de la censure cloud |
> **Cas d'utilisation** : Recherche académique, analyse approfondie, discussion libre, conversation IA sans restriction.

> **Remarque** : Il s'agit d'un modèle déployé localement, le contenu de sortie est entièrement contrôlé par l'utilisateur, aucune responsabilité de modération du contenu.



## Capacités principales



| Domaine de capacité | Description |
|---------------------|-------------|
| Analyse de marché | Interprétation macro/microéconomique, logique des marchés actions A/HK/US/matieres premieres/crypto |
| Rapports financiers | Interprétation des indicateurs financiers clés, résumé de rapports de recherche, aide à l'évaluation et aux prévisions de résultats |
| Risque & Conformité | Évaluation des risques produits, conformité des conseils d'investissement, interprétation des politiques de réglementation financière |
| Quant & Stratégie | Conception de stratégies quantitatives, quantification Pyramid (PEL), logique de backtesting, construction de facteurs et tool calling |
| Tool Calling | Intégration avec les cotations en temps réel, les bases de données, la récupération de rapports de recherche et d'autres sources de données financières |
## Spécifications techniques



| Élément | Spécification |
|---------|---------------|
| Modèle de base | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, licence MIT) |
| Paramètres | 35B MoE (256 experts routés + 1 expert partagé, 8 actifs par token) |
| Quantification | MoziSmartBit Intelligent Quantization développé en interne + format standard GGUF |
| Longueur de contexte | 256K (262 144 tokens) |
| Taille du modèle | ~15,5 Go (version MoziSmartBit Uncensored) |
| VRAM minimum | GPUs grand public avec 20 Go+ de VRAM (ex. : RTX 4060 Ti 16G avec CPU offload), 24 Go recommandés (avec vision + long contexte) |
| Framework d'inférence | llama.cpp / Ollama / LM Studio / Jan |
| Vitesse d'inférence | Optimisation algorithmique : 140+ tokens/s sur GPU AMD R9700, 70+ tokens/s sur iGPU AMD MAX+395 CPU, liberté de tokens locale |
| Équipe | Équipe Chen Yumo |
## Comparaison des formats de quantification et tailles de modèle



| Format de quantification | Taille du modèle | Précision | Notes |
|--------------------------|-------------------|-----------|-------|
| **FP16 (original)** | ~70 Go | 100% | Original 16bit |
| **MoziSmartBit** | **~15,5 Go** | **~99%** | **Utilisé par MoziAI, schéma de quantification optimal** |
| Q4_K_M | ~21,2 Go | ~98% | Standard GGUF 4bit |
| Q5_K_M | ~24,7 Go | ~99% | Qualité supérieure |
| Q6_K | ~28,5 Go | ~99,5% | Quasi sans perte |
| Q8_0 | ~36,9 Go | ~100% | Sans perte |
> MoziAI V3.7 utilise MoziSmartBit Intelligent Quantization, maintenant ~99% de précision tout en compressant le modèle MoE à 35B paramètres à ~15,5 Go (~4,5x ratio de compression), équilibrant la qualité d'inférence et l'accessibilité du déploiement pour les GPUs grand public.



## MoziSmartBit Intelligent Quantization



La quantification traditionnelle utilise une précision uniforme sur toutes les couches. **MoziSmartBit Intelligent Quantization** applique des stratégies de quantification différenciées pour un équilibre optimal taille-précision.



### Effet de compression



La quantification traditionnelle comprime toutes les parties du modèle de manière uniforme, entraînant souvent une perte significative de précision. MoziSmartBit Intelligent Quantization utilise une stratégie de compression intelligente développée en interne qui **réduit considérablement la taille avec une perte de précision minimale** :



- **Perte de quantification minimale** : Gain d'entraînement > perte de quantification. Le MoziAI-35B entraîné atteint un meilleur PPL sur les textes du domaine financier que le modèle de base bf16 pré-entraîné, réduisant les hallucinations et la perplexité par rapport aux modèles d'IA similaires

- **Réduction de taille ~4,5x** : Compressé de ~70 Go (FP16) à ~15,5 Go, également nettement plus petit que Q4_K_M (~21 Go), réduisant considérablement les exigences de VRAM et de stockage

- **Compatible GPU grand public** : Un modèle MoE à 35B qui nécessitait auparavant des GPU haut de gamme peut désormais fonctionner fluide sur 20 Go~24 Go de VRAM



### Avantages comparatifs



**vs Q4_K_M (~21,2 Go)** : ~30% plus petit (~15,5 Go), avec une précision **supérieure** à Q4_K_M, seuil de VRAM plus bas → fonctionne fluide sur GPU grand public 20 Go, économise ~55% de VRAM vs Q4_K_M



**vs FP16 original (~70 Go)** : ~4,5x compression, efficacité d'entraînement + perte de quantification minimale (gain d'entraînement > perte de quantification), permettant le déploiement local de contexte 256K sur des GPUs grand public au lieu de matériel haut de gamme professionnel.



## Paramètres d'inférence recommandés



Basés sur la configuration de production locale (AMD Radeon AI PRO R9700 32GB) :



| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| temperature | 0,6 | Équilibre créativité vs précision |
| top_p | 0,95 | Seuil d'échantillonnage nucleus |
| top_k | 20 | Échantillonnage de troncature (optimisé V3.7) |
| repeat_penalty | 1,05 | Pénalité de répétition |
| presence_penalty | 0 | Pas de pénalité de présence |
| context_length | 262144 | Contexte long 256K |
| batch_size | 2048 | Taille de lot |
| ubatch_size | 512 | Taille de micro-lot |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | Quantification du cache KV (kv-unified) |
| poll | 0 | Pas de polling GPU au ralenti, économe en énergie |
| reasoning | on | Activer la chaîne de raisonnement (chain of thought) |
| reasoning_budget | 400 | Budget de raisonnement en tokens |
| reasoning_format | deepseek-legacy | Format de raisonnement |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | Ordre des échantillonneurs |
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



Étant donné que les configurations GPU des utilisateurs varient considérablement, voici les paramètres recommandés pour différentes tailles de VRAM (tous pour la version MoziSmartBit) :



| VRAM | Contexte recommandé | KV Cache | Support de la vision | Notes |
|------|---------------------|----------|----------------------|-------|
| 20 Go | 150K | q4_0 | Supporté | Modèle+vision ~16,4 Go, tests montrent 200K+vision utilise ~19,5 Go de VRAM |
| 24 Go | 256K complet | q4_0 | Support total | Vision+contexte long 256K, utilise ~20,4 Go de VRAM, ~3,6 Go de marge |
| 32 Go+ | 256K complet | q4_0 | Support total | Vision+contexte long 256K, marge suffisante ~10 Go, meilleure configuration |
**NVIDIA**



| VRAM | Modèle GPU |
|------|------------|
| 24 Go | RTX 4090 / RTX 3090 Ti |
| 32 Go | RTX 5090 |
**AMD**



| VRAM | Modèle GPU |
|------|------------|
| 20 Go | RX 7900 XT |
| 24 Go | RX 7900 XTX |
| 32 Go | Radeon AI PRO R9700 |
**Intel**



| VRAM | Modèle GPU |
|------|------------|
| 32 Go | Arc Pro B70 / Arc Pro B65 |
| 24 Go | Arc Pro B60 |
| 16 Go | Arc Pro B50 (nécessite CPU offload) |
**Mémoire partagée iGPUs**



| VRAM | Processeur |
|------|------------|
| 128 Go | AMD Ryzen AI Max+ 395 (iGPU Radeon 8060S) |
| 128 Go | NVIDIA RTX Spark (GPU Blackwell RTX) |
> 💡 **Astuce** : Tant que votre VRAM satisfait les exigences ci-dessus, cela fonctionne. Aucune restriction de marque ou de modèle. Supporte les GPUs dédiés NVIDIA / AMD / Intel, ainsi que les iGPUs à mémoire unifiée 128 Go listés ci-dessus.



> 💡 **Astuce** : Un contexte plus long utilise plus de VRAM. Si vous rencontrez un OOM (out of memory), réduisez progressivement la valeur `-c`. Utilisez `--fit on` pour que llama.cpp ajuste automatiquement les couches à votre VRAM.



### Déploiement Ollama



```bash

# Créer le Modelfile

FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf



PARAMETER temperature 0,6

PARAMETER top_p 0,95

PARAMETER top_k 20

PARAMETER num_ctx 262144

PARAMETER num_gpu 99



# Construire et exécuter

ollama create moziAI-35B -f Modelfile

ollama run moziAI-35B

```



### Déploiement LM Studio / Jan



Recherchez `moziAI-35B` dans LM Studio ou Jan, téléchargez la version quant MoziSmartBit.



## Évaluation Benchmark



MoziAI est affiné à partir de **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI est optimisé pour les domaines financiers verticaux au-dessus du modèle de base, offrant des performances supérieures dans les scénarios de questions-réponses financières, de programmation quantitative et de tool calling. Les capacités générales de MoziAI-35B sont cohérentes avec le modèle de base Ornith-1.5-35B-A3B.



| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmation** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Raisonnement** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Agentique** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |
> Les scores benchmarks généraux de MoziAI-35B sont cohérents avec le modèle de base Ornith-1.5-35B-A3B. Le domaine financier vertical est la principale direction d'optimisation de MoziAI, surpassant significativement les modèles généraux dans des scénarios tels que l'analyse de rapports financiers, la stratégie quantitative, le risque & conformité et le tool calling d'agents. Données Gemma4 et Qwen3.6 issues de résultats publics officiels.



## Téléchargement du modèle



En raison de la grande taille du modèle (~15,5 Go), les poids sont hébergés sur plusieurs plateformes communautaires :



| Plateforme | URL |
|------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio** : Vous pouvez rechercher et télécharger directement dans [LM Studio](https://lmstudio.ai). Recherchez `moziAI` et cliquez sur Télécharger.



> 💡 **Astuce de téléchargement** : Cliquez sur le lien ci-dessus pour accéder au dépôt HuggingFace, puis naviguez vers l'onglet **« Files and versions »** pour télécharger tous les fichiers sous le répertoire V3.7 (modèle principal, projection visuelle, modèle de chat). Assurez-vous que les trois fichiers se trouvent dans le même répertoire.



### ⚠️ Important : La capacité visuelle nécessite le fichier mmproj



Ce modèle supporte la vision multimodale. Le **fichier de projection visuelle (mmproj)** est inclus dans le répertoire de version :



- **Fichier vision** : `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 Mo, précision BF16)

- **Placement** : Dans le même répertoire de version que le fichier modèle GGUF

- **Chargement** : Charger avec le drapeau `--mmproj` lors du démarrage de llama-server



```bash

llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf

```



> Sans le fichier vision, le modèle **perdra la capacité de compréhension d'images** et ne conservera que la conversation textuelle.



## Démarrage rapide



### 1. Télécharger les fichiers du modèle



Téléchargez tous les fichiers du répertoire V3.7 depuis HuggingFace / ModelScope :



```

V3.7/

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # Modèle principal (requis)

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Projection visuelle (optionnel)

└── moziAI-V3.7-35B-chat-template.jinja                  # Modèle de chat (recommandé)

```



### 2. Démarrer le serveur d'inférence



Pour la configuration complète recommandée, voir [Commande de lancement llama.cpp](#commande-de-lancement-llamacpp) ci-dessus.



Lancement minimal (paramètres principaux uniquement) :



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 262144 -ngl 99

```



> Ajoutez `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` pour la capacité visuelle.



### 3. Commencer à utiliser



Ouvrez `http://localhost:8080` dans votre navigateur pour commencer à discuter.



### Structure du répertoire



```

moziAI-35B/

├── README.md              # Version chinoise

├── README.en.md           # Version anglaise

├── README.fr.md           # Version française (ce fichier)

├── LICENSE                # Licence

├── V3.7/                  # Version V3.7 (autonome)

├── RELEASE_NOTES.md                       # Notes de version

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # Modèle principal

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Projection visuelle

└── moziAI-V3.7-35B-chat-template.jinja   # Modèle de chat

```



Pour le plan de mise à jour futur, voir [未来升级计划.md](未来升级计划.md).



## Mots-clés SEO



LLM IA financière, modèle open-source local, modèle de bord, programmation quantitative, MoziSmartBit, quantification intelligente, quantification GGUF, modèle MoE, LLM open-source local, déploiement local, IA financière, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, pas de censure, sortie libre, sans restriction, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, domaine financier vertical, modèle open-source



## Licence (Important)



Ce modèle utilise une **Licence restrictive personnalisée** :



### ✅ Autorisé

- **Utilisation commerciale libre** : Libre d'intégrer dans des produits commerciaux

- **Copie & Distribution** : Peut être copié, téléchargé et partagé



### ✅ Interdit

- **Œuvres dérivées** : Aucune modification, traduction, adaptation, fusion ou affinage du modèle ou d'une partie de celui-ci

- **Revente** : Pas de vente du modèle seul ou dans le cadre d'un produit

- **Relicenciement** : Pas de concession de sous-licences



### 📋 Exigences

- Doit conserver la mention de copyright originale

- Attribution : moziAI-35B



> Voir [LICENSE](./LICENSE) pour les conditions complètes.



## Avertissement



Fourni « en l'état » sans garantie. La sortie du modèle est uniquement à titre indicatif, pas un conseil en investissement. Les utilisateurs assument tous les risques.



## Contact



- **HuggingFace** : [@chenyumo](https://huggingface.co/chenyumo)

- **GitHub** : [@chenyumo166](https://github.com/chenyumo166)

- **Weibo** : [@rimochen](https://weibo.com/rimochen)

- **E-mail** : 263515@qq.com



---



Copyright (c) 2026 Chen Yumo / chenyumo166. Tous droits réservés.