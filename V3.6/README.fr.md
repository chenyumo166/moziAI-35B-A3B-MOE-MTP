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
library_name: llama-cpp
pipeline_tag: text-generation
---

# moziAI-13.7-35B-A3B-A3B-MOE-MTP-Uncensored - Un modèle d'IA multimodal petit mais puissant, déployable localement gratuitement

Language / Langue  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Présentation du modèle

MoziAI-35B-A3B-MOE est un grand modèle d'IA multimodal open-source local développé par l'équipe de Chen Yumo, influenceur financier chinois (renforcé dans le domaine financier, support visuel, appels d'outils, capacités de tâches longues et complexes, déploiement local sur carte graphique grand public). Il est basé sur le modèle de base Ornith-1.0-35B-A3B (architecture **Qwen3.5-35B-A3B/Qwen3.6-35B-A3B**) et a été affiné/distillé lors d'un développement secondaire.

La philosophie de l'équipe de développement de ce modèle est de faire en sorte que les agents de grands modèles d'IA locaux aux capacités complètes puissent entrer dans chaque foyer et dans les petites et moyennes entreprises, sans avoir à payer de coûts matériels d'IA élevés ou de coûts d'API cloud. Grâce à la technologie de **quantification intelligente MoziSmartBit** développée en interne, le modèle MoE de 35 milliards de paramètres est compressé à environ **15,5 Go**. Cela permet d'obtenir un équilibre optimal entre la précision du modèle et sa taille, avec une qualité de précision de près de 99 % par rapport à FP16. Ce modèle possède 35 milliards de paramètres, mais utilise la technologie d'expert sparse MOE, de sorte que seuls 3 milliards de paramètres sont activés et que le décodage spéculatif MTP est pris en charge pour une inférence accélérée. Les tests pratiques montrent qu'il peut être déployé localement et gratuitement sur une carte graphique grand public avec 20 Go de VRAM, et qu'il atteint des vitesses d'inférence de plus de 140 token/s – plus rapides que de nombreux grands modèles d'IA cloud payants.

En plus des capacités d'un grand modèle d'IA général, l'optimisation se concentre sur : les applications financières, les questions-réponses financières, la programmation quantitative, la programmation générale, les appels d'outils, le taux de réussite des tâches complexes à long contexte 256K et d'autres capacités clés des grands modèles d'IA. Il peut être déployé et utilisé gratuitement sur une carte graphique grand public locale, économise d'énormes coûts de tokens cloud, permet une liberté de token 24h/24 et 7j/7 et garantit la confidentialité et la sécurité des données locales.

**Date de publication :** 2026-08-20 | **Version :** V3.6

## Téléchargement du modèle

Comme le fichier du modèle est relativement volumineux (~15,5 Go), les poids du modèle sont hébergés sur plusieurs plateformes communautaires :

| Plateforme | Adresse |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

> 💡 **Utilisateurs de LM Studio** : Vous pouvez rechercher directement `moziAI` dans [LM Studio](https://lmstudio.ai) et le télécharger en un clic, sans avoir à télécharger manuellement de fichiers.  
> 💡 **Conseil de téléchargement** : Cliquez sur le lien ci-dessus pour accéder au dépôt HuggingFace. Dans l'onglet **"Files and versions"**, téléchargez tous les fichiers du répertoire V3.6 (modèle principal, projection visuelle, modèle de chat) et assurez-vous que les trois fichiers se trouvent dans le même répertoire.

### ⚠️ Important : La capacité visuelle nécessite un fichier mmproj supplémentaire

Ce modèle prend en charge la vision multimodale. Le fichier de projection visuelle (mmproj) est inclus dans le répertoire de version :

- **Fichier visuel** : `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (environ 903 Mo, précision BF16)
- **Emplacement** : Dans le même répertoire de version que le fichier du modèle GGUF
- **Méthode de chargement** : Charger via le paramètre `--mmproj` lors du démarrage de llama-server

> Sans charger le fichier visuel, la capacité de compréhension d'image est perdue, seule la capacité de conversation en texte pur est conservée.

### ⚠️ Important : Le fichier de modèle de chat doit être chargé

Ce modèle utilise un modèle de chat exclusif (chat-template). **Sans chargement, des erreurs de format de conversation se produiront, la chaîne de raisonnement échouera et la qualité des réponses diminuera considérablement**. Le fichier de modèle de chat est inclus dans le répertoire de version :

- **Fichier de modèle** : `moziAI-V3.6-35B-chat-template.jinja` (environ 5 Ko, format Jinja)
- **Emplacement** : Dans le même répertoire de version que le fichier du modèle GGUF
- **Méthode de chargement** : Charger via le paramètre `--chat-template-file` lors du démarrage de llama-server

> Sans charger le modèle de chat, le modèle risque de ne pas reconnaître correctement les instructions système, les messages utilisateur et les blocs de réflexion, ce qui entraîne des formats de sortie confus ou une diminution des capacités d'inférence.

### Commande de démarrage llama.cpp (configuration recommandée pour carte graphique 20G+ avec contexte 256K)

> Remarque : Si la VRAM est inférieure à 20 Go, réduisez le paramètre de contexte 262144 de `-c 262144`.

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

## Démarrage rapide

### 1. Télécharger les fichiers du modèle

Téléchargez tous les fichiers du répertoire V3.6 depuis HuggingFace / ModelScope sur votre machine locale :

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Modèle principal (obligatoire)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Projection visuelle (optionnel, télécharger si nécessaire)
└── moziAI-V3.6-35B-chat-template.jinja                  # Modèle de chat (obligatoire ! Sans chargement, erreurs de format de conversation)
```

> ⚠️ **Le modèle de chat est un fichier obligatoire**, pas optionnel. Ce modèle a un format de conversation personnalisé (y compris la chaîne de raisonnement/bloc de réflexion). L'absence du modèle entraînera des formats de sortie de modèle confus et une perte de fonction d'inférence. Veuillez absolument le télécharger et le charger au démarrage.

### 2. Démarrer le service d'inférence

Pour la commande de démarrage complète recommandée, reportez-vous à la section [Commande llama.cpp](#commande-llamacpp) ci-dessous.

Démarrage minimal (seulement les paramètres principaux) :

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Si vous avez besoin de capacités visuelles, ajoutez `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`

### 3. Commencer à utiliser

Ouvrez `http://localhost:8080` dans votre navigateur pour commencer la conversation.

### Structure des répertoires

```
moziAI-35B/
├── README.md              # Manuel en anglais
├── README.fr.md           # Ce fichier (manuel en français)
├── LICENSE                # Licence
├── V3.6/                  # Version V3.6 (autonome par version)
│   ├── RELEASE_NOTES.md                       # Notes de mise à jour
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Modèle principal
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Projection visuelle
│   └── moziAI-V3.6-35B-chat-template.jinja   # Modèle de chat
```

## Caractéristiques du modèle

- **Quantification intelligente MoziSmartBit** : Technologie de quantification intelligente développée en interne, équilibre optimal entre précision et taille, le modèle est compressé presque sans perte à environ **15,5 Go**
- **Capacité de tâches longues et complexes** : L'entraînement permet à l'agent du modèle de planifier automatiquement avec un mécanisme de traitement en boucle intelligent pour surmonter les blocages et d'auto-réflexion, permettant l'exécution automatique et l'auto-ajustement des tâches complexes – sans que l'utilisateur humain doive constamment optimiser les instructions de l'agent
- **Petit modèle, grandes capacités** : Pour l'exécution de tâches complexes, la capacité globale dépasse les modèles similaires de moins de 35 milliards de paramètres, et même certains modèles avec plusieurs fois plus de paramètres
- **Avantage de vitesse de MOE+MTP** : Bien que le modèle compte au total 35 milliards de paramètres, seuls 8+1 experts sont réellement activés, soit 3 milliards de paramètres au total. La vitesse d'inférence est plus rapide, idéal pour un déploiement local sur carte graphique grand public avec 20 Go~24 Go de VRAM, avec plus de 140 token/s
- **Expertise financière approfondie** : Renforcement profond des questions-réponses financières, de la programmation quantitative et des capacités d'appel d'outils
- **Déploiement grand public** : Une carte graphique grand public avec 20 Go~24 Go de VRAM ou plus suffit pour un déploiement local, prend en charge un contexte long allant jusqu'à 256K
- **Support multilingue** : Prend en charge 201 langues et dialectes, le chinois est particulièrement optimisé, couvre l'anglais, le japonais, le coréen, l'allemand, le français, le portugais et d'autres langues principales
- **Capacité de programmation générale** : Prend en charge le développement full-stack, le débogage de code, la conception d'architecture, la rédaction de scripts, couvre Python/JS/TS/Go/Rust et d'autres langues principales
- **Capacité de rédaction d'articles** : Prend en charge la rédaction de haute qualité de plusieurs genres, y compris les rapports de recherche, les articles d'analyse, la documentation technique, le contenu créatif, etc.
- **Compréhension visuelle** : En chargeant le fichier visuel dans le framework d'inférence, la vision multimodale est prise en charge. Les captures d'écran peuvent être partagées localement dans la fenêtre de chat et le modèle peut comprendre les informations de l'image
- **Sortie libre non censurée** : Aucune restriction de vérification de contenu, discussion libre sur n'importe quel sujet, pas de contrainte par les politiques de sécurité
- **Logique d'inférence améliorée** : Entraîné en conjonction avec la logique d'inférence (chaîne de pensée), améliore encore la qualité de l'inférence
- **Support multi-frameworks** : Compatible avec llama.cpp, Ollama, LM Studio, Jan et d'autres frameworks d'inférence populaires
- **Support de plateformes multi-agents** : Profondément adapté à OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex et d'autres IDE AI et frameworks agent populaires en Chine et à l'étranger, support natif des appels d'outils et de l'orchestration de tâches multi-tours, prêt à l'emploi

## Avantages d'Uncensored (sans censure)

Ce modèle hérite de la caractéristique Uncensored (sans censure) du modèle de base Ornith-1.0-35B-A3B et offre les avantages suivants :

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Avantage</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Aucune restriction de censure</td>
<td>Ne refuse aucun sujet, y compris le contenu sensible et controversé</td>
</tr>
<tr>
<td>Sortie libre</td>
<td>Pas de contrainte par les politiques de sécurité, peut générer n'importe quel type de réponse</td>
</tr>
<tr>
<td>Informations complètes</td>
<td>Fournit des informations complètes non filtrées, adapté aux scénarios de recherche et d'analyse</td>
</tr>
<tr>
<td>Local et privé</td>
<td>Le déploiement local signifie que les données sont entièrement privées, pas de censure cloud</td>
</tr>
</tbody>
</table>

> **Scénarios d'application** : Utilisation commerciale gratuite, recherche académique, analyse approfondie, discussion libre, conversation IA illimitée
> **Remarque** : Ce modèle est un modèle déployé localement. Le contenu de sortie est entièrement contrôlé par l'utilisateur, aucune responsabilité de censure de contenu n'est assumée.

## Capacités principales

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Domaine de capacité</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Analyse de marché</td>
<td>Interprétation macro/microéconomique, analyse des cours et logique des actions A/actions de Hong Kong/actions américaines/matières premières/cryptomonnaies</td>
</tr>
<tr>
<td>Finance et rapports de recherche</td>
<td>Interprétation des indicateurs clés des résultats financiers, extraction de résumés de rapports de recherche, aide à l'évaluation et aux prévisions de bénéfices</td>
</tr>
<tr>
<td>Gestion des risques et conformité</td>
<td>Évaluation des risques produit, conseils de conformité pour les recommandations d'investissement, interprétation des politiques de réglementation financière</td>
</tr>
<tr>
<td>Quantitatif et stratégies</td>
<td>Conception d'idées de stratégies quantitatives, quantification Pyramid (Pyramid/PEL), logique de backtesting, construction de facteurs et appels d'outils</td>
</tr>
<tr>
<td>Appels d'outils</td>
<td>Peut se connecter à des données financières telles que les cours en temps réel, les bases de données et la recherche de rapports de recherche</td>
</tr>
</tbody>
</table>

## Spécifications techniques

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Projet</th>
<th>Paramètre</th>
</tr>
</thead>
<tbody>
<tr>
<td>Modèle de base</td>
<td>Ornith-1.0-35B-A3B (architecture Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licence MIT)</td>
</tr>
<tr>
<td>Échelle des paramètres</td>
<td>35 milliards (35B) architecture MoE, 256 experts de routage + 1 expert partagé, 8 experts activés par token</td>
</tr>
<tr>
<td>Méthode de quantification</td>
<td>Utilise l'algorithme de quantification intelligente MoziSmartBit développé en interne + format standard GGUF</td>
</tr>
<tr>
<td>Longueur de contexte</td>
<td>256K (262 144 tokens)</td>
</tr>
<tr>
<td>Taille du modèle</td>
<td>~15,5 Go (version MoziSmartBit Uncensored)</td>
</tr>
<tr>
<td>Exigence minimale de VRAM</td>
<td>Carte graphique grand public avec 20 Go de VRAM ou plus (par ex. RTX 3060 12G avec délestage CPU, RTX 4060 Ti 16G, etc.), recommandé 24 Go (incl. visuel + long contexte)</td>
</tr>
<tr>
<td>Framework d'inférence</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>Vitesse d'inférence</td>
<td>Grâce à l'optimisation algorithmique, la carte graphique AMD Radeon AI PRO R9700 atteint plus de 140 token/s / la puce graphique intégrée AMD Ryzen AI Max+ 395 atteint plus de 70 token/s, permettant une sortie d'inférence libre locale</td>
</tr>
<tr>
<td>Équipe de développement</td>
<td>Équipe Chen Yumo</td>
</tr>
</tbody>
</table>

## Comparaison des formats de quantification et des tailles de modèle

| Format de quantification | Taille du modèle | Précision conservée | Description |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (original) | ~70 Go | 100% | Précision 16 bits d'origine |
| **MoziSmartBit** | **~15,5 Go** | **~99%** | **Ce modèle utilise une solution de quantification intelligente développée en interne** |
| Q4_K_M | ~22 Go | ~98% | 4 bits standard GGUF |
| Q5_K_M | ~24,7 Go | ~99% | Plus haute précision |
| Q6_K | ~28,5 Go | ~99,5% | Presque sans perte |
| Q8_0 | ~36,9 Go | ~100% | Sans perte |

> MoziAI V3.6 utilise la solution de quantification intelligente MoziSmartBit. Tout en conservant ~99% de précision, le modèle MoE de 35 milliards de paramètres est compressé à environ 15,5 Go, avec un taux de compression d'environ 4,5x. Il allie qualité d'inférence et seuil de déploiement, et convient mieux au déploiement local sur carte graphique grand public.

## Technologie de quantification intelligente MoziSmartBit

Les solutions de quantification traditionnelles utilisent une précision uniforme pour toutes les couches. La **quantification intelligente MoziSmartBit**, développée en interne par l'équipe de Chen Yumo, tire parti des caractéristiques structurelles des modèles MoE et met en œuvre une stratégie de quantification différenciée intelligente. Cela permet d'obtenir un équilibre optimal entre taille et précision – la qualité du modèle est supérieure à celle du format Q4_K_M, tandis que la taille n'est que d'environ 15,5 Go, avec un taux de compression d'environ 4,5x.

### Effet de compression

Les solutions de quantification traditionnelles compriment uniformément toutes les parties du modèle, ce qui entraîne souvent des pertes de précision importantes. La quantification intelligente MoziSmartBit utilise une stratégie de compression intelligente développée en interne, **qui réalise une compression de taille drastique avec une perte de précision minimale** :

- **Perte de précision de quantification extrêmement faible** : Gain d'entraînement > perte de quantification. Le MoziAI-35B entraîné a un PPL supérieur sur les textes financiers par rapport au modèle de base bf16 avant l'entraînement, réduisant les hallucinations et la confusion des modèles d'IA similaires
- **Taille du modèle compressée de 4,5 fois** : De ~70 Go en FP16 à ~15,5 Go compressé, également beaucoup plus petit que ~22 Go en Q4_K_M, réduisant considérablement les seuils de VRAM et de stockage
- **Exécutable sur carte graphique grand public** : Un grand modèle MoE 35B qui nécessitait à l'origine une carte graphique haut de gamme peut maintenant être déployé en douceur avec 20 Go~24 Go de VRAM

### Avantages comparatifs

**vs Q4_K_M (~22 Go)** : Taille réduite d'environ 30% (~15,5 Go), précision **supérieure** à Q4_K_M, seuil de VRAM plus bas, déploiement fluide possible sur carte graphique grand public milieu de gamme (20 Go).

**vs FP16 original (~70 Go)** : Taille compressée d'environ 4,5 fois, entraînement efficace + perte de précision de quantification extrêmement faible (gain d'entraînement > perte de quantification), passage de cartes graphiques professionnelles (48 Go+) à des cartes graphiques grand public pour une exécution locale avec un long contexte 256K.

## Paramètres d'inférence recommandés

Sur la base de la configuration d'exécution locale (AMD Radeon AI PRO R9700 32 Go), les paramètres suivants sont recommandés :

| Paramètre | Valeur recommandée | Description |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Équilibre entre créativité et précision |
| top_p | 0.95 | Seuil d'échantillonnage par noyau |
| top_k | 20 | Échantillonnage tronqué |
| repeat_penalty | 1.05 | Pénalité de répétition |
| presence_penalty | 0 | Aucune pénalité de présence |
| context_length | 262144 | Long contexte 256K |
| batch_size | 2048 | Taille de lot |
| ubatch_size | 512 | Taille de micro-lot |
| flash_attention | auto | Flash Attention automatique |
| kv_cache | q4_0 | Quantification du cache KV (kv-unified unifié) |
| poll | 0 | Pas de polling GPU en veille, économe en énergie et faible latence |
| reasoning | on | Activer la chaîne de raisonnement |
| reasoning_budget | 400 | Nombre de tokens du budget d'inférence |
| reasoning_format | deepseek-legacy | Format d'inférence |
| samplers | top_k;top_p;temperature;typ_p | Ordre des échantillonneurs |

### Recommandations pour différentes configurations de VRAM

Étant donné que les configurations de carte graphique des utilisateurs varient considérablement, voici les paramètres recommandés pour différentes tailles de VRAM (tous pour la version MoziSmartBit) :

| VRAM | Longueur de contexte recommandée | Cache KV | Support visuel | Description |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 Go | 128K | q4_0 | Pris en charge | Modèle + visuel total ~16,4 Go, test pratique : 128K + visuel n'occupe que ~19,5 Go de VRAM |
| 24 Go | 256K complet | q4_0 | Parfaitement pris en charge | Visuel + contexte long 256K, n'occupe que ~20,4 Go de VRAM, réserve ~3,6 Go de VRAM |
| 32 Go+ | 256K complet | q4_0 | Parfaitement pris en charge | Visuel + contexte long 256K, réserve de VRAM suffisante ~10 Go, configuration la plus puissante |

**Tableau de référence des cartes graphiques NVIDIA**

| VRAM | Modèle de carte graphique |
| ----- | ---------------------- |
| 24 Go | RTX 4090 / RTX 3090 Ti |
| 32 Go | RTX 5090 |

**Tableau de référence des cartes graphiques AMD**

| VRAM | Modèle de carte graphique |
| ----- | ------------------- |
| 20 Go | RX 7900 XT |
| 24 Go | RX 7900 XTX |
| 32 Go | Radeon AI PRO R9700 |

**Tableau de référence des cartes graphiques Intel**

| VRAM | Modèle de carte graphique |
| ----- | ------------------------- |
| 32 Go | Arc Pro B70 / Arc Pro B65 |
| 24 Go | Arc Pro B60 |
| 16 Go | Arc Pro B50 (nécessite un délestage CPU) |

**Tableau de référence des appareils à puce graphique intégrée avec mémoire partagée CPU**

| VRAM | Modèle de processeur |
| ------ | -------------------------------------- |
| 128 Go | AMD Ryzen AI Max+ 395 (puce graphique intégrée Radeon 8060S) |
| 128 Go | NVIDIA RTX Spark (GPU RTX Blackwell) |

> 💡 **Conseil** : Tant que la VRAM répond aux exigences ci-dessus, elle peut être utilisée – aucune restriction de marque ou de modèle. Prend en charge les cartes graphiques dédiées NVIDIA / AMD / Intel, ainsi que les puces graphiques intégrées / CPU avec 128 Go de mémoire unifiée.
>
> 💡 **Conseil** : Plus le contexte est long, plus la VRAM est occupée. Si la VRAM est insuffisante (OOM), réduisez progressivement la valeur du paramètre `-c`. Avec le paramètre `--fit on`, llama.cpp peut ajuster automatiquement le nombre de couches pour s'adapter à la VRAM.

### Déploiement Ollama

```bash
# Créer un Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Construire et exécuter
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### Déploiement LM Studio / Jan

Recherchez directement `moziAI-35B` dans LM Studio ou Jan et sélectionnez la version quantifiée à télécharger.

## Évaluation de référence

moziAI-13.7-35B-A3B est affiné à partir du modèle de base **Ornith-1.0-35B** (deepreinforce-ai). S'appuyant sur les excellentes capacités de codage d'agent du modèle de base, MoziAI a ajouté une **optimisation approfondie du domaine financier**, offrant de meilleures performances dans des scénarios tels que les questions-réponses financières, la programmation quantitative et les appels d'outils. Les capacités générales sont identiques à celles du modèle de base Ornith-1.0-35B.

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
\* **Terminal-Bench 2.1 (Terminus-2)** : Évalué avec le framework Harbor/Terminus-2, configuration `parser=json`, `temperature=1.0`, `top_p=1.0`, fenêtre de contexte 128K. Chaque exécution a un délai d'attente de 4 heures, 32 cœurs, 48 Go de RAM, le résultat est la moyenne de 5 exécutions.  
\* **Terminal-Bench 2.1 (Claude Code)** : Évalué avec Claude Code 2.1.126, configuration `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Le résultat est la moyenne de 5 exécutions.  
\* **SWE-bench Verified, Pro et Multilingual** : Évalués avec le framework OpenHands, configuration `temp=1.0`, `top_p=0.95`, fenêtre de contexte 256K.  
\* **NL2Repo** : Configuration `temperature=1.0`, `top_p=1.0`, contexte 400K, sortie 48K.  

> MoziAI-35B hérite complètement des excellentes capacités de codage d'agent d'Ornith-1.0-35B. La différence clé de MoziAI réside dans l'**optimisation approfondie du domaine financier**. Dans des scénarios tels que l'analyse des rapports financiers, les stratégies quantitatives, la gestion des risques et la conformité, et les appels d'outils d'agent, les performances sont nettement supérieures à celles des modèles généraux.

## Mots-clés SEO

Grand modèle d'IA financière, grand modèle d'IA, modèle open-source local, modèle edge, programmation quantitative, MoziSmartBit, quantification intelligente, quantification GGUF, modèle MoE, grand modèle open-source local, déploiement local, IA financière, appels d'outils, Agent, llama.cpp, Ollama, GGUF, Uncensored (sans censure), pas de censure, sans censure, sortie libre, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B, verticale financière, modèle open-source.

## Licence (important)

Ce modèle utilise une **licence restrictive personnalisée**, les conditions détaillées sont les suivantes :

✅ **Autorisé**

- Utilisation commerciale gratuite : Peut être intégré gratuitement dans vos produits ou services commerciaux
- Copie et distribution : Peut être copié, téléchargé, distribué tel quel

Les conditions de licence détaillées sont disponibles dans le fichier [LICENSE](../LICENSE).

## Clause de non-responsabilité

Ce modèle est fourni "tel quel" sans garantie d'aucune sorte. Les sorties du modèle sont fournies à titre de référence uniquement et ne constituent pas un conseil en investissement. L'utilisateur assume seul les risques liés à son utilisation.

## Contact

- **HuggingFace** : [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub** : [@chenyumo166](https://github.com/chenyumo166)
- **Weibo** : [@rimochen](https://weibo.com/rimochen)
- **E-mail** : 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.