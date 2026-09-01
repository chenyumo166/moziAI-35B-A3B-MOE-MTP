---
language:
- nl
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

# MoziAI-35B-V3.8 — Compact en krachtig multimodaal AI-model voor gratis lokale implementatie

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | Nederlands | [Italiano](README.it.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**Releasedatum: 2026-09-01** · **Versie: V3.8**

---

## 📑 Inhoudsopgave

- [1. Modeloverzicht](#1-modeloverzicht)
- [2. Belangrijkste kenmerken](#2-belangrijkste-kenmerken) — Dynamisch 7-dimensionaal denken / LOOP / MoziSmartBit / Financieel focus
- [3. Versie-updates](#3-versie-updates)
- [4. Kerncompetenties](#4-kerncompetenties)
- [5. Technische specificaties](#5-technische-specificaties)
- [6. ⚡ Snelstart](#6--snelstart3-bestanden--100-beste-inferentie) — **3-bestandenpakket**
- [7. Modeldownloads](#7-modeldownloads)
- [8. Startopdrachten](#8-startopdrachten)
- [9. Aanbevolen inferentieparameters](#9-aanbevolen-inferentieparameters)
- [10. Kwantisatieformaatvergelijking](#10-kwantisatieformaatvergelijking)
- [11. Speculatief decoderen versneld](#11-speculatief-decoderen-versneldbelangrijke-functie)
- [12. VRAM-aanbevelingen](#12-vram-aanbevelingen)
- [13. Implementatiemethoden](#13-implementatiemethoden)
- [14. Benchmarks](#14-benchmarks)
- [15. Uncensored-optimalisatie](#15-uncensoredzonder-censuur-optimalisatie)
- [16. Licentie](#16-licentie)
- [17. Contact](#17-contact)

---

## 1. Modeloverzicht

MoziAI-35B-V3.8 is een lokaal implementeerbaar open-source multimodaal AI-model, ontwikkeld door het team van de Chinese financiële influencer Chen Yumo. Gebaseerd op de open-source basis **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B-architectuur, MoE 35B, MIT-licentie), integreert het zelf ontwikkelde financiële data + financiële domeincapaciteiten + dynamisch 7-dimensionaal denkkader + agent-LOOP-reflectiemechanisme + Uncensored-eigenschap + MoziSmartBit-hybridekwantisatiealgoritme.

**💡 Formaatvoordeel: slechts 15,9 GB** — Het MoE-model met 35 miljard parameters wordt door de eigen MoziSmartBit-kwantificatie gecomprimeerd tot slechts **15,9 GB** (ongeveer 30% kleiner dan standaard Q4_K_M ~22 GB). Past in één installatiepakket, draait op gewone consumenten-GPU's (20GB VRAM+), verlaagt cloud-tokenkosten naar **0**, biedt 7×24 uur token-vrijheid en garandeert lokale dataprivacy. **Gratis commercieel gebruik** — nul drempel.

---

## 2. Belangrijkste kenmerken

### 🧠 Dynamisch 7-dimensionaal denkkader

Het zelf ontwikkelde kerninferentiekader van MoziAI. Voor elke taak geeft het model eerst een **moziAI-Think**-marker uit en ontvouwt dan dynamisch gestructureerd denken op basis van taakcomplexiteit:

| Niveau | Scenario | Typische taken | Ontvouwen dimensies |
| --- | --- | --- | --- |
| **Niveau 0** | Eenvoudige Q&A | Termuitleg, feiten, vertaling, samenvatting | ①Taak begrijpen ⑤Middelen (2D-snelantwoord) |
| **Niveau 1** | Analyse/diagnose | Marktonderzoek, schrijven, data-analyse, rapporten, strategie | ①②③⑤⑥ Vijf-dimensie-evaluatie |
| **Niveau 2** | Complexe ontwikkeling/strategie | Code, architectuur, kwantstrategie, workflows, systeem | ①②③④⑤⑥⑦ Volledige 7D-analyse |

> 7 dimensies: ①Taak begrijpen ②Complexiteit ③Afhankelijkheden ④Risico ⑤Middelen ⑥Acceptatiecriteria ⑦Uitvoeringsstrategie

### 🔄 Agent-LOOP-iteratiemechanisme

Complexe taken gaan automatisch in **moziAI-Loop**: **Ronde 1 uitvoeren+evalueren → Ronde 2 aanpassen+verifiëren**. De output wordt zelf gevalideerd vóór het definitieve antwoord. Zoals een senior ingenieur — «probleem ontleden → plan evalueren → uitvoeren → reflecteren → optimaliseren» — verbetert het de nauwkeurigheid aanzienlijk. Eenvoudige Q&A slaat de Loop over.

### 📦 MoziSmartBit slimme kwantisering

Zelf ontwikkelde gelaagde slimme kwantisering comprimeert het 35-miljard-parameter MoE-model naar ongeveer **15,5 GB** — circa 6,5 GB (~30%) kleiner dan Q4_K_M (~22 GB) met **~99%** FP16-nauwkeurigheid. Compressieverhouding **4,5x**.

### 💰 Financiële focus

Diep geoptimaliseerd voor financiële Q&A, kwantprogrammering en tool-calls. Financiën tolereert hallucinaties nauwelijks — MoziAI presteert duidelijk beter dan vergelijkbare algemene modellen.

### 🛡️ Uncensored-eigenschap

Geen inhoudsbeperkingen, vrije output, volledige informatie, lokale privacy (zie [Sectie 15](#15-uncensoredzonder-censuur-optimalisatie)).

### 🌐 Andere kenmerken

- **Meertalig**: 201 talen en dialecten, Chinees geoptimaliseerd
- **Programmeren**: full-stack, Python/JS/TS/Go/Rust
- **Schrijven**: rapporten, analyses, technische documenten, creatief
- **Visie**: multimodaal, begrijpt screenshots
- **Multi-framework**: llama.cpp / Ollama / LM Studio / Jan
- **Multi-agent**: OpenClaw / Hermes / Cursor / Claude Code / Codex, native tool-calls

---

## 3. Versie-updates

V3.8 is opnieuw getraind met hetzelfde zelf ontwikkelde trainingdata-systeem van dezelfde generatie als 27B-V3.8 (identiteit / dynamisch 7D-denken / LOOP-iteratie / financieel domein), met versterkt dynamisch 7D-denken + LOOP-modus: betere complexiteitherkenning, hogere voltooiingspercentages, sterkere «eerst denken, dan doen»-capaciteit. Uncensored en financiële optimalisatie blijven behouden.

MoziAI houdt een actief update-tempo aan en maakt lokale AI-modellen lichter en capabeler via eigen technologie.

---

## 4. Kerncompetenties

| Domein | Beschrijving |
| --- | --- |
| Marktanalyse | Macro/micro-economie, A/HK/US-aandelen, grondstoffen, crypto |
| Financiën & rapporten | Balansindicatoren, rapporten, waardering & prognoses |
| Risico & compliance | Productrisico, adviescompliance, regelgeving |
| Kwant & strategie | Kwantstrategie, Pyramid/PEL, backtest, factoren, tool-calls |
| Tool-calls | Live marktdata, databases, research |

---

## 5. Technische specificaties

| Punt | Specificatie |
| --- | --- |
| Basismodel | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT) |
| Parameters | 35B MoE, 256 routing-experts + 1 gedeelde expert, 8 experts actief per token |
| Kwantisering | MoziSmartBit + GGUF-standaard |
| Contextlengte | 256K (262.144 tokens) |
| Modelgrootte | ~15,5 GB |
| Minimale VRAM | **20GB+** implementeerbaar (CPU-offload); **24GB+** vloeiend lange context; **32GB+** volledig 256K + visie |
| Frameworks | llama.cpp / Ollama / LM Studio / Jan |
| Inferentiesnelheid | Speculatief decoderen: AMD R9700 **140+ tok/s** / AMD MAX+395 **70+ tok/s** |
| Ontwikkelaar | Chen Yumo Team |

---

## 6. ⚡ Snelstart (3 bestanden = 100% beste inferentie)

> ⚠️ **Belangrijk**: voor de beste inferentie moeten **3 bestanden samen** worden gedownload — hoofdmodel, visieprojector, chat-template. Ontbreekt er één, gaat de bijbehorende capaciteit verloren.

### 6.1 Modelbestanden downloaden

Download deze **3 bestanden** van HuggingFace / ModelScope naar dezelfde lokale map (hoofdmodel in de **repo-root**, visieprojector onder `mmproj/35B/`, chat-template onder `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Hoofdmodel (vereist, 15,5 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Visieprojector (vereist, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Chat-template (vereist, 7D-denken+LOOP)
```

### 6.2 Starten en gebruiken

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Open `http://localhost:8080` in de browser. Volledige parameters in Sectie 9.

---

## 7. Modeldownloads

| Platform | Adres |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio-gebruikers**: zoek `moziAI` in [LM Studio](https://lmstudio.ai) en download met één klik.

---

## 8. Startopdrachten

### Minimaal starten (3 bestanden)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Volledige aanbevolen start

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

> 💡 Weinig VRAM: verlaag `-c` (bijv. 131072) of voeg `--fit on` toe.

---

## 9. Aanbevolen inferentieparameters

Geoptimaliseerd door lokale tests (AMD Radeon AI PRO R9700 32GB):

| Parameter | Dagelijkse taken/Schrijven | Complexe taken/Programmeren | Beschrijving |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Dagelijks stabiel; complex: gematigde verkenning |
| top\_p | 0,95 | 0,95 | Kern-samplingdrempel |
| top\_k | 20 | 20 | Afgekapte sampling |
| min\_p | 0,024 | 0,024 | Minimumkansfilter |
| repeat\_penalty | 1,05 | 1,05 | Herhalingsstraf |
| presence\_penalty | 0 | 0 | Geen aanwezigheidsstraf |
| context\_length | 262144 | 262144 | 256K lange context |
| reasoning | on | on | Redeneringsketen (CoT) |
| reasoning\_budget | 400 | 1000 | Redeneringsbudget (hoger bij complexe taken) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Redenering in apart veld |
| **spec-type** | **default** | **default** | **Speculatief decoderen (ngram, MoE-optimaal, Sectie 11)** |
| KV-cache | q4\_0 | q4\_0 | Gekwantiseerde KV-cache (kv-unified) |

> 💡 **Denkmodus**: activeer met `--reasoning on`. `reasoning_budget` begrenst denk-tokens.

---

## 10. Kwantisatieformaatvergelijking

| Formaat | Grootte | Nauwkeurigheid | Beschrijving |
| --- | --- | --- | --- |
| FP16 origineel | ~70 GB | 100% | Verliesloos, pro-GPU nodig |
| **MoziSmartBit (dit model)** | **~15,5 GB** | **~99%** | **Zelf ontwikkeld, beste nauwkeurigheid/grootte** |
| Q4_K_M | ~22 GB | ~98% | GGUF-standaard 4-bit |
| Q5_K_M | ~24,7 GB | ~99% | Hoger |
| Q6_K | ~28,5 GB | ~99,5% | Bijna verliesloos |
| Q8_0 | ~36,9 GB | ~100% | Verliesloos |

> MoziSmartBit behoudt ~99% en comprimeert 35B MoE naar 15,5 GB (4,5x), ~30% kleiner dan Q4_K_M.

---

## 11. Speculatief decoderen versneld (belangrijke functie)

Dit model versnelt inferentie via **speculatief decoderen** — **~1,5-2x** sneller (lokaal gemeten).

- **MoE-optimaal**: llama.cpp beveelt **ngram** (`--spec-default`) aan voor MoE — snelst en stabielst
- **Over "MTP"**: komt van de Multi-Token-Prediction-gewichten van de basis (behouden); llama.cpp's MTP-draft voor MoE is beperkt, dus gebruikt MoziAI ngram

```bash
--spec-default
```

---

## 12. VRAM-aanbevelingen

Gemeten met MoziSmartBit-versie (model + visie ~16,4 GB):

| VRAM | Aanbeveling | Beschrijving |
| --- | --- | --- |
| 20 GB | 150K context, q4\_0, visie | ~19,5 GB gebruik |
| **24 GB** | **Volledig 256K, q4\_0, visie perfect** | **Aanbevolen**: ~20,4 GB, ~3,6 GB marge |
| 32 GB+ | Volledig 256K, ruime marge | R9700 32GB: ~10 GB marge |

> 💡 Langere context = meer VRAM. Bij OOM verlaag `-c` of gebruik `--fit on`. NVIDIA / AMD ondersteund.

---

## 13. Implementatiemethoden

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

Zoek `moziAI` in LM Studio / Jan en download de Q4\_K\_M-versie (LM Studio leest standaard root-modellen; voor oudere versies "van URL toevoegen" gebruiken).

> 💡 Ollama's mmproj- en chat\_template-ondersteuning is beperkt — gebruik llama.cpp voor volledige functionaliteit.

---

## 14. Benchmarks

MoziAI-35B-V3.8 is verfijnd/gedistilleerd van deepreinforce-ai/Ornith-1.5-35B-A3B. Gegevens uit V3.7-metingen (V3.8 = zelfde basis en trainingssysteem):

| Benchmark | moziAI-35B-V3.8<br>(dit model) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmeren** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67,8 | 64,2 | 52,5 | 42,1 | 51,7 | 53,5 |
| Terminal-Bench 2.1 (Claude Code) | 68,5 | 62,8 | 49,2 | - | - | 48,6 |
| SWE-bench Verified | 79 | 75,6 | 73,4 | 52 | 76 | 76,4 |
| SWE-bench Pro | 59,6 | 50,4 | 49,5 | 35,7 | 51,2 | 51,6 |
| SWE-bench Multilingual | 71,4 | 69,3 | 67,2 | 51,7 | - | 69,3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5,1 | 1,4 | 1,4 | - | - | 1,4 |
| NL2Repo | 46,2 | 34,6 | 29,4 | 15,5 | - | 36,8 |
| SWE Atlas - QnA | 39,8 | 37,1 | 15,5 | - | - | 20,4 |
| **Redeneren** |  |  |  |  |  |  |
| HLE (no tools) | 25,6 | 20,8 | 21,4 | 19,5 | 22 | 28,7 |
| HLE (with tools) | 33,4 | 30,1 | 28,9 | 26,5 | - | 48,3 |
| GPQA Diamond | 89,2 | 86,2 | 86 | 84,3 | 83,5 | 88,4 |
| **Agentisch** |  |  |  |  |  |  |
| MCP-Atlas | 70,2 | 64,4 | 62,8 | 55 | 75,5 | 72,3 |
| Toolathlon-Verified | 48,7 | 42,4 | 41,7 | 40,8 | - | 38,3 |
| WideSearch | 67,8 | 63,4 | 60,1 | 54,2 | - | 74 |
| BrowseComp | 67,6 | 63,5 | 62 | - | - | 78,6 |
| ClawEval | 72,5 | 69,8 | 68,7 | 48,5 | - | 70,7 |

> In de financiële sector (balansen, kwant, risico, agent-tools) duidelijk beter dan algemene modellen. Gemma-4 / Qwen3.6: officiële resultaten.

---

## 15. Uncensored-optimalisatie

Dit model erft de Uncensored-eigenschap van Ornith-1.5-35B-A3B:

| Voordeel | Beschrijving |
| --- | --- |
| Geen beperkingen | Weigert geen onderwerp, ook gevoelige |
| Vrije output | Niet beperkt door veiligheidsbeleid |
| Volledige info | Ongefilterd, ideaal voor onderzoek |
| Lokale privacy | Gegevens volledig privé |

**Let op**: lokaal model — output wordt door de gebruiker gecontroleerd; het model draagt geen moderatieverantwoordelijkheid.

---

## 16. Licentie

**Aangepaste restrictieve licentie**:

- ✅ **Toegestaan** — gratis commercieel gebruik, kopiëren, verspreiden
- ❌ **Verboden** — secundaire ontwikkeling, doorverkoop, sublicentie
- 📋 **Vereist** — auteursrecht behouden, bron: moziAI-35B

Model «zoals het is» zonder garanties. Output is geen beleggingsadvies.

---

## 17. Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo) · **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen) · **E-mail**: 263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. Alle rechten voorbehouden.