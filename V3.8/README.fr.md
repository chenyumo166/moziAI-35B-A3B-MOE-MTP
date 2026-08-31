---
language:
- fr
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

# MoziAI-35B-V3.8 — Un modèle IA multimodal compact et puissant, déployable localement gratuitement

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | Français | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

**Date de sortie : 2026-09-01** · **Version : V3.8**

---

## 📑 Table des matières

- [1. Présentation du modèle](#1-présentation-du-modèle)
- [2. Caractéristiques principales](#2-caractéristiques-principales) — Pensée dynamique à 7 dimensions / LOOP / MoziSmartBit / Focus finance
- [3. Notes de mise à jour](#3-notes-de-mise-à-jour)
- [4. Compétences de base](#4-compétences-de-base)
- [5. Spécifications techniques](#5-spécifications-techniques)
- [6. ⚡ Démarrage rapide](#6--démarrage-rapide3-fichiers--100-inférence-optimale) — **Pack 3 fichiers**
- [7. Téléchargement du modèle](#7-téléchargement-du-modèle)
- [8. Commandes de lancement](#8-commandes-de-lancement)
- [9. Paramètres d'inférence recommandés](#9-paramètres-dinférence-recommandés)
- [10. Comparaison des formats de quantification](#10-comparaison-des-formats-de-quantification)
- [11. Décodage spéculatif accéléré](#11-décodage-spéculatif-accéléréfonction-clé)
- [12. Recommandations VRAM](#12-recommandations-vram)
- [13. Méthodes de déploiement](#13-méthodes-de-déploiement)
- [14. Benchmarks](#14-benchmarks)
- [15. Optimisation Uncensored](#15-optimisation-uncensoredsans-censure)
- [16. Licence](#16-licence)
- [17. Contact](#17-contact)

---

## 1. Présentation du modèle

MoziAI-35B-V3.8 est un grand modèle IA multimodal open-source déployable localement, développé par l'équipe de Chen Yumo, influenceur financier chinois. Basé sur le modèle de base open-source **Ornith-1.5-35B-A3B** (architecture Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, licence MIT), il intègre les données financières auto-développées + capacités financières + cadre de pensée dynamique à 7 dimensions + mécanisme itératif LOOP d'agent + caractéristique Uncensored + algorithme de quantification hybride MoziSmartBit.

Ce modèle abaisse la barrière du déploiement local pour les particuliers et les entreprises, est autorisé pour **usage commercial gratuit**, fonctionne sur GPU grand public, réduit les coûts cloud à **0**, offre une liberté de tokens 7×24 et garantit la confidentialité et la sécurité des données locales.

---

## 2. Caractéristiques principales

### 🧠 Cadre de pensée dynamique à 7 dimensions

Cadre d'inférence principal développé par MoziAI. Pour toute tâche, le modèle émet d'abord un marqueur **moziAI-Think**, puis déploie dynamiquement une réflexion structurée selon la complexité :

| Niveau | Scénario | Tâches typiques | Dimensions déployées |
| --- | --- | --- | --- |
| **Niveau 0** | Q&A simple | Explication, recherche, traduction, résumé | ①Comprendre ⑤Ressources (réponse rapide 2D) |
| **Niveau 1** | Analyse/diagnostic | Étude de marché, rédaction, analyse de données, rapports, évaluation | ①②③⑤⑥ Évaluation 5D |
| **Niveau 2** | Développement/stratégie complexe | Code, architecture, stratégie quant, workflows, système | ①②③④⑤⑥⑦ Analyse profonde 7D |

> 7 dimensions : ①Comprendre la tâche ②Évaluer la complexité ③Dépendances ④Évaluer les risques ⑤Ressources ⑥Critères d'acceptation ⑦Stratégie d'exécution

### 🔄 Mécanisme itératif LOOP d'agent

Les tâches complexes entrent automatiquement en **moziAI-Loop** : **Tour 1 exécution+évaluation → Tour 2 ajustement+vérification**. La sortie est auto-validée avant la réponse finale. Comme un ingénieur senior — « décomposer → évaluer → exécuter → réfléchir → optimiser » — améliorant nettement la précision. Les Q&A simples sautent le Loop.

### 📦 Quantification intelligente MoziSmartBit

Quantification intelligente en couches développée en interne : compresse le modèle MoE de 35 milliards de paramètres à environ **15,5 Go** — ~6,5 Go (~30 %) de moins que Q4_K_M (~22 Go) avec **~99 %** de la précision FP16. Ratio de compression **4,5x**.

### 💰 Focus finance

Optimisé en profondeur pour Q&A financière, programmation quant et appels d'outils. La finance tolère très mal les hallucinations — MoziAI surpasse nettement les modèles généraux de même taille.

### 🛡️ Caractéristique Uncensored

Aucune restriction de contenu, sortie libre, information complète, confidentialité locale (voir [Section 15](#15-optimisation-uncensoredsans-censure)).

### 🌐 Autres caractéristiques

- **Multilingue** : 201 langues et dialectes, chinois optimisé
- **Programmation** : full-stack, Python/JS/TS/Go/Rust
- **Rédaction** : rapports, articles, documents techniques, création
- **Vision** : multimodale, comprend les captures d'écran
- **Multi-frameworks** : llama.cpp / Ollama / LM Studio / Jan
- **Multi-agents** : OpenClaw / Hermes / Cursor / Claude Code / Codex, appels d'outils natifs

---

## 3. Notes de mise à jour

V3.8 a été ré-entraîné avec le même système de jeu de données auto-développé de génération que 27B-V3.8 (identité / pensée 7D / LOOP / finance), renforçant la pensée dynamique 7D + mode inférence LOOP : meilleure reconnaissance de complexité, taux de réussite plus élevé, capacité « réfléchir avant d'agir » plus forte. L'Uncensored et l'optimisation finance perdurent.

MoziAI maintient un rythme de mises à jour actif et rend les modèles locaux plus légers et plus performants.

---

## 4. Compétences de base

| Domaine | Description |
| --- | --- |
| Analyse marché | Macro/microéconomie, actions A/HK/US, matières premières, crypto |
| Finance & rapports | Indicateurs de bilan, résumés, évaluation et prévisions |
| Risque & conformité | Risque produit, conformité des conseils, réglementation |
| Quant & stratégie | Stratégies quant, Pyramid/PEL, backtest, facteurs, appels d'outils |
| Appels d'outils | Données de marché temps réel, bases de données, recherche |

---

## 5. Spécifications techniques

| Point | Spécification |
| --- | --- |
| Modèle de base | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT) |
| Paramètres | 35B MoE, 256 experts de routage + 1 expert partagé, 8 experts actifs par token |
| Quantification | MoziSmartBit + format GGUF standard |
| Longueur de contexte | 256K (262 144 tokens) |
| Taille | ~15,5 Go |
| VRAM minimale | **20 Go+** déployable (offload CPU) ; **24 Go+** contexte long fluide ; **32 Go+** 256K complet + vision |
| Frameworks | llama.cpp / Ollama / LM Studio / Jan |
| Vitesse | Décodage spéculatif : AMD R9700 **140+ tok/s** / AMD MAX+395 **70+ tok/s** |
| Développeur | Équipe Chen Yumo |

---

## 6. ⚡ Démarrage rapide (3 fichiers = 100 % d'inférence optimale)

> ⚠️ **Important** : l'inférence optimale nécessite de **télécharger 3 fichiers ensemble** — modèle principal, projecteur de vision, modèle de chat. S'il en manque un, la capacité correspondante est perdue.

### 6.1 Télécharger les fichiers

Téléchargez **tous les fichiers du répertoire V3.8** depuis HuggingFace / ModelScope dans le même dossier :

```
V3.8/
├── moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Modèle principal (requis, 15,5 Go)
├── moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Projecteur vision (requis, ~1 Go)
└── moziAI-V3.8-35B-chat-template.jinja                                        ← Modèle de chat (requis, pensée 7D+LOOP)
```

### 6.2 Lancer et utiliser

```bash
llama-server \
  -m V3.8/moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Ouvrez `http://localhost:8080` dans le navigateur. Paramètres complets en Section 9.

---

## 7. Téléchargement du modèle

| Plateforme | Adresse |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith/tree/main/V3.8) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/master/V3.8) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main/V3.8) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Utilisateurs LM Studio** : cherchez `moziAI` dans [LM Studio](https://lmstudio.ai) et téléchargez en un clic.

---

## 8. Commandes de lancement

### Lancement minimal (3 fichiers)

```bash
llama-server \
  -m V3.8/moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Lancement recommandé complet

```bash
llama-server \
  -m V3.8/moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
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

> 💡 VRAM limitée : réduisez `-c` (ex. 131072) ou ajoutez `--fit on`.

---

## 9. Paramètres d'inférence recommandés

Optimisé par tests locaux (AMD Radeon AI PRO R9700 32 Go) :

| Paramètre | Tâches quotidiennes/Rédaction | Tâches complexes/Programmation | Description |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Stabilité quotidienne ; exploration modérée pour code complexe |
| top\_p | 0,95 | 0,95 | Seuil d'échantillonnage noyau |
| top\_k | 20 | 20 | Échantillonnage tronqué |
| min\_p | 0,024 | 0,024 | Filtre de probabilité min |
| repeat\_penalty | 1,05 | 1,05 | Pénalité de répétition |
| presence\_penalty | 0 | 0 | Aucune pénalité de présence |
| context\_length | 262144 | 262144 | Contexte long 256K |
| reasoning | on | on | Chaîne de raisonnement (CoT) |
| reasoning\_budget | 400 | 1000 | Budget de raisonnement (plus élevé pour tâches complexes) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Raisonnement dans un champ séparé |
| **spec-type** | **default** | **default** | **Décodage spéculatif (ngram, optimal MoE, Section 11)** |
| Cache KV | q4\_0 | q4\_0 | Cache KV quantifié (kv-unified) |

> 💡 **Mode pensée** : activé via `--reasoning on`. `reasoning_budget` limite les tokens de réflexion.

---

## 10. Comparaison des formats de quantification

| Format | Taille | Précision | Description |
| --- | --- | --- | --- |
| FP16 original | ~70 Go | 100 % | Sans perte, GPU pro requis |
| **MoziSmartBit (ce modèle)** | **~15,5 Go** | **~99 %** | **Développé en interne, meilleur précision/taille** |
| Q4_K_M | ~22 Go | ~98 % | GGUF standard 4 bits |
| Q5_K_M | ~24,7 Go | ~99 % | Plus précise |
| Q6_K | ~28,5 Go | ~99,5 % | Quasi sans perte |
| Q8_0 | ~36,9 Go | ~100 % | Sans perte |

> MoziSmartBit maintient ~99 % et compresse 35B MoE à 15,5 Go (4,5x), ~30 % plus petit que Q4_K_M.

---

## 11. Décodage spéculatif accéléré (fonction clé)

Ce modèle accélère nettement l'inférence via le **décodage spéculatif** — **~1,5-2x** plus rapide (mesures locales).

- **Optimal MoE** : llama.cpp recommande le **ngram** (`--spec-default`) pour MoE — le plus rapide et stable
- **À propos du « MTP »** : vient des poids Multi-Token Prediction de la base (conservés) ; le support MTP draft de llama.cpp pour MoE est limité, MoziAI utilise donc ngram

```bash
--spec-default
```

---

## 12. Recommandations VRAM

Mesuré avec la version MoziSmartBit (modèle + vision ~16,4 Go) :

| VRAM | Recommandation | Description |
| --- | --- | --- |
| 20 Go | 150K contexte, q4\_0, vision | ~19,5 Go utilisés |
| **24 Go** | **256K complet, q4\_0, vision parfaite** | **Recommandé** : ~20,4 Go, ~3,6 Go de marge |
| 32 Go+ | 256K complet, large marge | R9700 32 Go : ~10 Go de marge |

> 💡 Contexte plus long = plus de VRAM. En cas d'OOM, réduisez `-c` ou utilisez `--fit on`. NVIDIA / AMD pris en charge.

---

## 13. Méthodes de déploiement

### Ollama

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

Cherchez `moziAI` dans LM Studio / Jan et téléchargez la version Q4\_K\_M (LM Studio lit les modèles racine par défaut ; pour les anciennes versions, utilisez « Ajouter depuis une URL »).

> 💡 Le support mmproj et chat\_template d'Ollama est limité — préférez llama.cpp.

---

## 14. Benchmarks

MoziAI-35B-V3.8 est affiné/distillé depuis deepreinforce-ai/Ornith-1.5-35B-A3B. Données issues des mesures V3.7 (V3.8 = même base et même système d'entraînement) :

| Benchmark | moziAI-35B-V3.8<br>(ce modèle) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmation** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67,8 | 64,2 | 52,5 | 42,1 | 51,7 | 53,5 |
| Terminal-Bench 2.1 (Claude Code) | 68,5 | 62,8 | 49,2 | - | - | 48,6 |
| SWE-bench Verified | 79 | 75,6 | 73,4 | 52 | 76 | 76,4 |
| SWE-bench Pro | 59,6 | 50,4 | 49,5 | 35,7 | 51,2 | 51,6 |
| SWE-bench Multilingual | 71,4 | 69,3 | 67,2 | 51,7 | - | 69,3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5,1 | 1,4 | 1,4 | - | - | 1,4 |
| NL2Repo | 46,2 | 34,6 | 29,4 | 15,5 | - | 36,8 |
| SWE Atlas - QnA | 39,8 | 37,1 | 15,5 | - | - | 20,4 |
| **Raisonnement** |  |  |  |  |  |  |
| HLE (no tools) | 25,6 | 20,8 | 21,4 | 19,5 | 22 | 28,7 |
| HLE (with tools) | 33,4 | 30,1 | 28,9 | 26,5 | - | 48,3 |
| GPQA Diamond | 89,2 | 86,2 | 86 | 84,3 | 83,5 | 88,4 |
| **Agentique** |  |  |  |  |  |  |
| MCP-Atlas | 70,2 | 64,4 | 62,8 | 55 | 75,5 | 72,3 |
| Toolathlon-Verified | 48,7 | 42,4 | 41,7 | 40,8 | - | 38,3 |
| WideSearch | 67,8 | 63,4 | 60,1 | 54,2 | - | 74 |
| BrowseComp | 67,6 | 63,5 | 62 | - | - | 78,6 |
| ClawEval | 72,5 | 69,8 | 68,7 | 48,5 | - | 70,7 |

> Dans la finance (bilans, quant, risque, outils d'agent), nettement meilleur que les modèles généraux. Gemma-4 / Qwen3.6 : résultats officiels.

---

## 15. Optimisation Uncensored

Ce modèle hérite de l'Uncensored d'Ornith-1.5-35B-A3B :

| Avantage | Description |
| --- | --- |
| Aucune restriction | Ne refuse aucun sujet, y compris sensible |
| Sortie libre | Non contrainte par les politiques de sécurité |
| Infos complètes | Non filtrées, idéal pour la recherche |
| Confidentialité | Données entièrement privées |

**Note** : modèle local — la sortie est contrôlée par l'utilisateur ; le modèle ne porte pas de responsabilité de modération.

---

## 16. Licence

**Licence restrictive personnalisée** :

- ✅ **Autorisé** — usage commercial gratuit, copie, distribution
- ❌ **Interdit** — développement secondaire, revente, sous-licence
- 📋 **Requis** — conserver le copyright, source : moziAI-35B

Modèle fourni « en l'état », sans garantie. Sortie non constitutive de conseil en investissement.

---

## 17. Contact

- **HuggingFace** : [@chenyumo](https://huggingface.co/chenyumo) · **GitHub** : [@chenyumo166](https://github.com/chenyumo166)
- **Weibo** : [@rimochen](https://weibo.com/rimochen) · **E-mail** : 263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. Tous droits réservés.