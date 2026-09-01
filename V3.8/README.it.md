---
language:
- it
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

# MoziAI-35B-V3.8 — Un modello IA multimodale compatto e potente, deployabile localmente gratuitamente

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | Italiano | [Русский](README.ru.md)

**Data di rilascio: 2026-09-01** · **Versione: V3.8**

---

## 📑 Indice

- [1. Panoramica del modello](#1-panoramica-del-modello)
- [2. Caratteristiche principali](#2-caratteristiche-principali) — Pensiero dinamico a 7 dimensioni / LOOP / MoziSmartBit / Focus finanza
- [3. Note di aggiornamento](#3-note-di-aggiornamento)
- [4. Competenze principali](#4-competenze-principali)
- [5. Specifiche tecniche](#5-specifiche-tecniche)
- [6. ⚡ Avvio rapido](#6--avvio-rapido3-file--100-inferenza-ottimale) — **Pacchetto 3 file**
- [7. Download del modello](#7-download-del-modello)
- [8. Comandi di avvio](#8-comandi-di-avvio)
- [9. Parametri di inferenza consigliati](#9-parametri-di-inferenza-consigliati)
- [10. Confronto formati di quantizzazione](#10-confronto-formati-di-quantizzazione)
- [11. Decodifica speculativa accelerata](#11-decodifica-speculativa-acceleratafunzione-chiave)
- [12. Raccomandazioni VRAM](#12-raccomandazioni-vram)
- [13. Metodi di deployment](#13-metodi-di-deployment)
- [14. Benchmark](#14-benchmark)
- [15. Ottimizzazione Uncensored](#15-ottimizzazione-uncensoredsenza-censura)
- [16. Licenza](#16-licenza)
- [17. Contatti](#17-contatti)

---

## 1. Panoramica del modello

MoziAI-35B-V3.8 è un modello IA multimodale open-source deployabile localmente, sviluppato dal team di Chen Yumo, influencer finanziario cinese. Basato sul modello base open-source **Ornith-1.5-35B-A3B** (architettura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, licenza MIT), integra dati finanziari autosviluppati + capacità del dominio finanziario + framework di pensiero dinamico a 7 dimensioni + meccanismo iterativo LOOP dell'agente + caratteristica Uncensored + algoritmo di quantizzazione ibrido MoziSmartBit.

**💡 Vantaggio di dimensione: solo 15,9 GB** — Il modello MoE da 35 miliardi di parametri viene compresso a soli **15,9 GB** grazie alla quantizzazione MoziSmartBit proprietaria (circa il 30% più piccolo del Q4_K_M standard ~22 GB). Sta in un singolo installer, funziona su GPU consumer (20 GB di VRAM+), riduce i costi cloud a **0**, offre libertà di token 7×24 e garantisce privacy dei dati locali. **Uso commerciale gratuito** — zero barriere.

---

## 2. Caratteristiche principali

### 🧠 Framework di pensiero dinamico a 7 dimensioni

Framework di inferenza principale sviluppato da MoziAI. Per ogni attività, il modello emette prima un marcatore **moziAI-Think**, poi dispiega dinamicamente un pensiero strutturato in base alla complessità:

| Livello | Scenario | Attività tipiche | Dimensioni dispiegate |
| --- | --- | --- | --- |
| **Livello 0** | Q&A semplice | Spiegazione, ricerca, traduzione, riassunto | ①Comprendere ⑤Risorse (risposta rapida 2D) |
| **Livello 1** | Analisi/diagnosi | Ricerca di mercato, scrittura, analisi dati, report, valutazione | ①②③⑤⑥ Valutazione 5D |
| **Livello 2** | Sviluppo/strategia complesso | Codice, architettura, strategia quant, workflow, sistema | ①②③④⑤⑥⑦ Analisi profonda 7D |

> 7 dimensioni: ①Comprendere l'attività ②Valutare complessità ③Dipendenza ④Rischi ⑤Risorse ⑥Criteri di accettazione ⑦Strategia di esecuzione

### 🔄 Meccanismo iterativo LOOP dell'agente

Le attività complesse entrano automaticamente in **moziAI-Loop**: **Round 1 esecuzione+valutazione → Round 2 aggiustamento+verifica**. L'output è auto-validato prima della risposta finale. Come un ingegnere senior — «scomporre → valutare → eseguire → riflettere → ottimizzare» — migliorando nettamente la precisione. Le Q&A semplici saltano il Loop.

### 📦 Quantizzazione intelligente MoziSmartBit

Quantizzazione intelligente a strati sviluppata internamente: comprime il modello MoE da 35 miliardi di parametri a circa **15,5 GB** — ~6,5 GB (~30%) in meno rispetto a Q4_K_M (~22 GB) con **~99%** della precisione FP16. Rapporto di compressione **4,5x**.

### 💰 Focus sul settore finanziario

Ottimizzato in profondità per Q&A finanziaria, programmazione quant e tool-call. La finanza tollera pochissimo le allucinazioni — MoziAI supera nettamente i modelli generali di pari dimensioni.

### 🛡️ Caratteristica Uncensored

Nessuna restrizione sui contenuti, output libero, informazioni complete, privacy locale (vedi [Sezione 15](#15-ottimizzazione-uncensoredsenza-censura)).

### 🌐 Altre caratteristiche

- **Multilingue**: 201 lingue e dialetti, cinese ottimizzato
- **Programmazione**: full-stack, Python/JS/TS/Go/Rust
- **Scrittura**: report, articoli, documenti tecnici, creatività
- **Visione**: multimodale, comprende gli screenshot
- **Multi-framework**: llama.cpp / Ollama / LM Studio / Jan
- **Multi-agente**: OpenClaw / Hermes / Cursor / Claude Code / Codex, tool-call nativi

---

## 3. Note di aggiornamento

V3.8 è stato ri-addestrato con lo stesso sistema di dataset autosviluppato di generazione di 27B-V3.8 (identità / pensiero 7D / iterazione LOOP / finanza), rafforzando il pensiero dinamico 7D + modalità inferenza LOOP: migliore riconoscimento della complessità, tassi di completamento più alti, capacità «pensa prima di agire» più forte. Uncensored e ottimizzazione finanziaria persistono.

MoziAI mantiene un ritmo attivo di aggiornamenti e rende i modelli IA locali più leggeri e capaci.

---

## 4. Competenze principali

| Dominio | Descrizione |
| --- | --- |
| Analisi di mercato | Macro/microeconomia, azioni A/HK/US, materie prime, crypto |
| Finanza & report | Indicatori di bilancio, riassunti, valutazione e previsioni |
| Rischio & conformità | Rischio prodotto, conformità dei consigli, regolamentazione |
| Quant & strategia | Strategie quant, Pyramid/PEL, backtest, fattori, tool-call |
| Tool-call | Dati di mercato in tempo reale, database, ricerca |

---

## 5. Specifiche tecniche

| Punto | Specifica |
| --- | --- |
| Modello base | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT) |
| Parametri | 35B MoE, 256 esperti di routing + 1 esperto condiviso, 8 esperti attivi per token |
| Quantizzazione | MoziSmartBit + formato GGUF standard |
| Lunghezza contesto | 256K (262.144 token) |
| Dimensione | ~15,5 GB |
| VRAM minima | **20GB+** deployabile (offload CPU); **24GB+** contesto lungo fluido; **32GB+** 256K completo + visione |
| Framework | llama.cpp / Ollama / LM Studio / Jan |
| Velocità | Decodifica speculativa: AMD R9700 **140+ tok/s** / AMD MAX+395 **70+ tok/s** |
| Sviluppatore | Team Chen Yumo |

---

## 6. ⚡ Avvio rapido (3 file = 100% inferenza ottimale)

> ⚠️ **Importante**: l'inferenza ottimale richiede il **download di 3 file insieme** — modello principale, proiettore di visione, template di chat. Se manca uno, la capacità corrispondente è persa.

### 6.1 Scaricare i file

Scarica questi **3 file** da HuggingFace / ModelScope nella stessa cartella locale (modello principale alla **radice del repository**, proiettore visione sotto `mmproj/35B/`, template di chat sotto `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Modello principale (richiesto, 15,5 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Proiettore visione (richiesto, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Template di chat (richiesto, pensiero 7D+LOOP)
```

### 6.2 Avviare e usare

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Apri `http://localhost:8080` nel browser. Parametri completi nella Sezione 9.

---

## 7. Download del modello

| Piattaforma | Indirizzo |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/master) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Utenti LM Studio**: cerca `moziAI` in [LM Studio](https://lmstudio.ai) e scarica con un clic.

---

## 8. Comandi di avvio

### Avvio minimo (3 file)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Avvio raccomandato completo

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

> 💡 VRAM limitata: riduci `-c` (es. 131072) o aggiungi `--fit on`.

---

## 9. Parametri di inferenza consigliati

Ottimizzato con test locali (AMD Radeon AI PRO R9700 32GB):

| Parametro | Attività quotidiane/Scrittura | Attività complesse/Programmazione | Descrizione |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Stabilità quotidiana; esplorazione moderata per codice complesso |
| top\_p | 0,95 | 0,95 | Soglia di campionamento nucleo |
| top\_k | 20 | 20 | Campionamento troncato |
| min\_p | 0,024 | 0,024 | Filtro probabilità minima |
| repeat\_penalty | 1,05 | 1,05 | Penalità di ripetizione |
| presence\_penalty | 0 | 0 | Nessuna penalità di presenza |
| context\_length | 262144 | 262144 | Contesto lungo 256K |
| reasoning | on | on | Catena di ragionamento (CoT) |
| reasoning\_budget | 400 | 1000 | Budget di ragionamento (più alto per attività complesse) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Ragionamento in campo separato |
| **spec-type** | **default** | **default** | **Decodifica speculativa (ngram, ottimale MoE, Sezione 11)** |
| Cache KV | q4\_0 | q4\_0 | Cache KV quantizzata (kv-unified) |

> 💡 **Modalità pensiero**: attivata con `--reasoning on`. `reasoning_budget` limita i token di riflessione.

---

## 10. Confronto formati di quantizzazione

| Formato | Dimensione | Precisione | Descrizione |
| --- | --- | --- | --- |
| FP16 originale | ~70 GB | 100% | Senza perdite, GPU pro richiesta |
| **MoziSmartBit (questo modello)** | **~15,5 GB** | **~99%** | **Sviluppato internamente, migliore precisione/dimensione** |
| Q4_K_M | ~22 GB | ~98% | GGUF standard 4 bit |
| Q5_K_M | ~24,7 GB | ~99% | Più precisa |
| Q6_K | ~28,5 GB | ~99,5% | Quasi senza perdite |
| Q8_0 | ~36,9 GB | ~100% | Senza perdite |

> MoziSmartBit mantiene ~99% e comprime 35B MoE a 15,5 GB (4,5x), ~30% più piccolo di Q4_K_M.

---

## 11. Decodifica speculativa accelerata (funzione chiave)

Questo modello accelera l'inferenza con la **decodifica speculativa** — **~1,5-2x** più veloce (misure locali).

- **Ottimale MoE**: llama.cpp raccomanda il **ngram** (`--spec-default`) per MoE — il più veloce e stabile
- **Sul "MTP"**: deriva dai pesi Multi-Token Prediction della base (conservati); il supporto MTP draft di llama.cpp per MoE è limitato, quindi MoziAI usa ngram

```bash
--spec-default
```

---

## 12. Raccomandazioni VRAM

Misurato con la versione MoziSmartBit (modello + visione ~16,4 GB):

| VRAM | Raccomandazione | Descrizione |
| --- | --- | --- |
| 20 GB | 150K contesto, q4\_0, visione | ~19,5 GB usati |
| **24 GB** | **256K completo, q4\_0, visione perfetta** | **Raccomandato**: ~20,4 GB, ~3,6 GB di margine |
| 32 GB+ | 256K completo, ampio margine | R9700 32GB: ~10 GB di margine |

> 💡 Contesto più lungo = più VRAM. In caso di OOM riduci `-c` o usa `--fit on`. NVIDIA / AMD supportati.

---

## 13. Metodi di deployment

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

Cerca `moziAI` in LM Studio / Jan e scarica la versione Q4\_K\_M (LM Studio legge i modelli root di default; per le versioni precedenti usa "Aggiungi da URL").

> 💡 Il supporto mmproj e chat\_template di Ollama è limitato — preferisci llama.cpp.

---

## 14. Benchmark

MoziAI-35B-V3.8 è affinato/distillato da deepreinforce-ai/Ornith-1.5-35B-A3B. Dati dalle misure V3.7 (V3.8 = stessa base e sistema di addestramento):

| Benchmark | moziAI-35B-V3.8<br>(questo modello) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmazione** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67,8 | 64,2 | 52,5 | 42,1 | 51,7 | 53,5 |
| Terminal-Bench 2.1 (Claude Code) | 68,5 | 62,8 | 49,2 | - | - | 48,6 |
| SWE-bench Verified | 79 | 75,6 | 73,4 | 52 | 76 | 76,4 |
| SWE-bench Pro | 59,6 | 50,4 | 49,5 | 35,7 | 51,2 | 51,6 |
| SWE-bench Multilingual | 71,4 | 69,3 | 67,2 | 51,7 | - | 69,3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5,1 | 1,4 | 1,4 | - | - | 1,4 |
| NL2Repo | 46,2 | 34,6 | 29,4 | 15,5 | - | 36,8 |
| SWE Atlas - QnA | 39,8 | 37,1 | 15,5 | - | - | 20,4 |
| **Ragionamento** |  |  |  |  |  |  |
| HLE (no tools) | 25,6 | 20,8 | 21,4 | 19,5 | 22 | 28,7 |
| HLE (with tools) | 33,4 | 30,1 | 28,9 | 26,5 | - | 48,3 |
| GPQA Diamond | 89,2 | 86,2 | 86 | 84,3 | 83,5 | 88,4 |
| **Agentico** |  |  |  |  |  |  |
| MCP-Atlas | 70,2 | 64,4 | 62,8 | 55 | 75,5 | 72,3 |
| Toolathlon-Verified | 48,7 | 42,4 | 41,7 | 40,8 | - | 38,3 |
| WideSearch | 67,8 | 63,4 | 60,1 | 54,2 | - | 74 |
| BrowseComp | 67,6 | 63,5 | 62 | - | - | 78,6 |
| ClawEval | 72,5 | 69,8 | 68,7 | 48,5 | - | 70,7 |

> Nel settore finanziario (bilanci, quant, rischio, tool dell'agente) nettamente migliore dei modelli generali. Gemma-4 / Qwen3.6: risultati ufficiali.

---

## 15. Ottimizzazione Uncensored

Questo modello eredita l'Uncensored da Ornith-1.5-35B-A3B:

| Vantaggio | Descrizione |
| --- | --- |
| Nessuna restrizione | Non rifiuta alcun tema, anche sensibile |
| Output libero | Non vincolato dalle policy di sicurezza |
| Info complete | Non filtrate, ideali per la ricerca |
| Privacy | Dati completamente privati |

**Nota**: modello locale — l'output è controllato dall'utente; il modello non ha responsabilità di moderazione.

---

## 16. Licenza

**Licenza restrittiva personalizzata**:

- ✅ **Consentito** — uso commerciale gratuito, copia, distribuzione
- ❌ **Vietato** — sviluppo secondario, rivendita, sub-licenza
- 📋 **Richiesto** — mantenere il copyright, fonte: moziAI-35B

Modello fornito «così com'è», senza garanzie. L'output non costituisce consulenza finanziaria.

---

## 17. Contatti

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo) · **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen) · **E-mail**: 263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. Tutti i diritti riservati.