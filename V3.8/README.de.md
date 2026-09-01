---
language:
- de
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

# MoziAI-35B-V3.8 — Kompaktes, leistungsstarkes multimodales KI-Modell für die kostenlose lokale Bereitstellung

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | Deutsch | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

**Veröffentlichungsdatum: 2026-09-01** · **Version: V3.8**

---

## 📑 Inhaltsverzeichnis

- [1. Modellübersicht](#1-modellübersicht)
- [2. Hauptmerkmale](#2-hauptmerkmale) — Dynamisches 7-Dimensionales Denken / LOOP / MoziSmartBit / Finanzfokus
- [3. Versionshinweise](#3-versionshinweise)
- [4. Kernkompetenzen](#4-kernkompetenzen)
- [5. Technische Spezifikationen](#5-technische-spezifikationen)
- [6. ⚡ Schnellstart](#6--schnellstart3-dateien--100-beste-inferenz-aktivieren) — **3-Dateien-Paket**
- [7. Modell-Downloads](#7-modell-downloads)
- [8. Startbefehle](#8-startbefehle)
- [9. Empfohlene Inferenzparameter](#9-empfohlene-inferenzparameter)
- [10. Quantisierungsformatvergleich](#10-quantisierungsformatvergleich)
- [11. Spekulatives Decoding](#11-spekulatives-decoding-beschleunigungschlüsselfunktion)
- [12. VRAM-Empfehlungen](#12-vram-empfehlungen)
- [13. Bereitstellungsmethoden](#13-bereitstellungsmethoden)
- [14. Benchmarks](#14-benchmarks)
- [15. Uncensored-Optimierung](#15-uncensoredohne-zensur-optimierung)
- [16. Lizenz](#16-lizenz)
- [17. Kontakt](#17-kontakt)

---

## 1. Modellübersicht

MoziAI-35B-V3.8 ist ein lokal bereitstellbares Open-Source-Multimodal-KI-Modell, entwickelt vom Team des chinesischen Finanz-Influencers Chen Yumo. Basierend auf dem Open-Source-Fundament **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B-Architektur, MoE 35B, MIT-Lizenz) integriert es die selbst entwickelten Finanzdaten + Finanzbereichsfähigkeiten + dynamisches 7-dimensionales Denkframework + Agent-LOOP-Reflexionsmechanismus + Uncensored-Eigenschaft + MoziSmartBit-Hybridquantisierungsalgorithmus.

**💡 Größen-Vorteil: nur 15,9 GB** — Das 35B-Parametermodell (MoE) wird durch die eigene MoziSmartBit-Quantisierung auf nur **15,9 GB** komprimiert (ca. 30 % kleiner als Standard-Q4_K_M ~22 GB). Es passt in ein einziges Installationspaket, läuft auf normalen Consumer-GPUs (ab 20 GB VRAM), senkt Cloud-Token-Kosten auf **0**, ermöglicht 7×24 Stunden Token-Freiheit und gewährleistet lokale Datensouveränität. **Kostenlose kommerzielle Nutzung** – null Einstiegshürde.

---

## 2. Hauptmerkmale

### 🧠 Dynamisches 7-Dimensionales Denkframework

Das selbst entwickelte Kerninferenzframework von MoziAI. Für jede Aufgabe gibt das Modell zunächst einen **moziAI-Think**-Marker aus und entfaltet dann dynamisch strukturiertes Denken je nach Aufgabenkomplexität:

| Ebene | Szenario | Typische Aufgaben | Entfaltete Dimensionen |
| --- | --- | --- | --- |
| **Ebene 0** | Einfache Q&A | Begriffserklärung, Faktenabfrage, Übersetzung, Zusammenfassung | ①Aufgabe verstehen ⑤Ressourcenbedarf (2-Dimensionen-Schnellantwort) |
| **Ebene 1** | Analyse/Diagnose | Marktforschung, Textverfassung, Datenanalyse, Berichtsauswertung, Strategiebewertung | ①②③⑤⑥ Fünf-Dimensionen-Bewertung |
| **Ebene 2** | Komplexe Entwicklung/Strategie | Code-Entwicklung, Architekturdesign, Quant-Strategie, Multi-Step-Workflows, Systemdesign | ①②③④⑤⑥⑦ Vollständige 7-Dimensionen-Tiefenanalyse |

> 7 Dimensionen: ①Aufgabe verstehen ②Komplexität bewerten ③Abhängigkeiten ④Risiko bewerten ⑤Ressourcenbedarf ⑥Abnahmekriterien ⑦Ausführungsstrategie

### 🔄 Agent-LOOP-Iterationsmechanismus

Komplexe Aufgaben laufen automatisch in den **moziAI-Loop**-Iterationsmodus: **Runde 1 Ausführen+Bewerten → Runde 2 Anpassen+Verifizieren** — die Ausgabe wird selbst validiert, bevor die endgültige Antwort erfolgt. Wie ein Senior-Engineer arbeitet das Modell „Problem zerlegen → Plan bewerten → ausführen → reflektieren → optimieren" und verbessert so Genauigkeit und Ausführbarkeit komplexer Aufgaben deutlich. Einfache Q&A überspringt den Loop automatisch.

### 📦 MoziSmartBit-Smart-Quantisierung

Selbst entwickelte, geschichtete Smart-Quantisierung komprimiert das 35-Milliarden-Parameter-MoE-Modell auf etwa **15,5 GB** — rund 6,5 GB (~30 %) kleiner als Standard-Q4_K_M (~22 GB) bei **~99 %** FP16-Genauigkeit. Herkömmliche Quantisierung nutzt einheitliche Präzision für alle Schichten; MoziSmartBit nutzt eine intelligente Differenzstrategie für die MoE-Struktur mit besserer Genauigkeit als Q4_K_M. Kompressionsverhältnis: **4,5x**.

### 💰 Finanzbereich-Fokus

Tief optimiert für Finanz-Q&A, Quant-Programmierung und Tool-Aufrufe. Der Finanzbereich toleriert Halluzinationen kaum — MoziAI übertrifft gleich große allgemeine Modelle hier deutlich.

### 🛡️ Uncensored-Eigenschaft

Keine Inhaltsbeschränkungen, freie Ausgabe, vollständige Informationen, lokale Privatsphäre. Geeignet für akademische Forschung, Tiefenanalyse, freie Diskussion (siehe [Abschnitt 15](#15-uncensoredohne-zensur-optimierung)).

### 🌐 Weitere Merkmale

- **Mehrsprachig**: 201 Sprachen und Dialekte, Chinesisch besonders optimiert
- **Allgemeine Programmierung**: Full-Stack, Debugging, Architekturdesign (Python/JS/TS/Go/Rust)
- **Schreiben**: Berichte, Analysen, technische Dokumente, kreative Inhalte
- **Bildverständnis**: Multimodal, versteht lokale Screenshots
- **Multi-Framework**: llama.cpp / Ollama / LM Studio / Jan
- **Multi-Agent**: OpenClaw / Hermes / Cursor / Claude Code / Codex usw., native Tool-Aufrufe und Multi-Round-Orchestrierung

---

## 3. Versionshinweise

V3.8 wurde mit dem gleichaltrigen, selbst entwickelten Trainingsdatensatz-System wie 27B-V3.8 (Identität / dynamisches 7-Dimensionales Denken / LOOP-Iteration / Finanzbereich) neu trainiert — mit verstärktem dynamischem 7-Dimensionalen Denken + LOOP-Inferenzmodus: bessere Komplexitätserkennung, höhere Komplettierungsraten bei komplexen Aufgaben, stärkere „Erst denken, dann handeln"-Fähigkeit. Die Uncensored-Eigenschaft und die Finanzoptimierung bleiben erhalten.

MoziAI hält einen aktiven Upgrade-Rhythmus, bleibt an der Spitze der KI-Entwicklung und macht lokale KI-Modelle durch eigene Technologie ständig leichter und leistungsfähiger.

---

## 4. Kernkompetenzen

| Kompetenz | Beschreibung |
| --- | --- |
| Marktanalyse | Makro/mikroökonomische Einordnung, A-Aktien/HK/US/Commodities/Krypto |
| Finanzen & Berichte | Bilanzkennzahlen, Berichtszusammenfassungen, Bewertung & Prognose |
| Risiko & Compliance | Produktrisiko, Anlage-Compliance, Regulierung |
| Quant & Strategie | Quant-Strategiedesign, Pyramid/PEL, Backtesting, Faktoren, Tool-Aufrufe |
| Tool-Aufrufe | Anbindung an Live-Marktdaten, Datenbanken, Recherche |

---

## 5. Technische Spezifikationen

| Punkt | Spezifikation |
| --- | --- |
| Basismodell | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MIT) |
| Parameter | 35B MoE, 256 Routing-Experten + 1 Shared Expert, 8 Experten pro Token aktiv |
| Quantisierung | MoziSmartBit + GGUF-Standard |
| Kontextlänge | 256K (262.144 Tokens) |
| Modellgröße | ~15,5 GB |
| Mindest-VRAM | **20GB+** bereitstellbar (CPU-Offload); **24GB+** flüssig langer Kontext; **32GB+** voll 256K + Vision |
| Frameworks | llama.cpp / Ollama / LM Studio / Jan |
| Inferenzgeschwindigkeit | Mit spekulativem Decoding: AMD R9700 **140+ tok/s** / AMD MAX+395 **70+ tok/s** |
| Entwickler | Chen Yumo Team |

---

## 6. ⚡ Schnellstart (3 Dateien = 100 % beste Inferenz)

> ⚠️ **Wichtig**: Für die beste Inferenz müssen **3 Dateien zusammen** heruntergeladen werden — Hauptmodell, Vision-Projektor, Chat-Template. Fehlt eine, geht die entsprechende Fähigkeit verloren.

### 6.1 Modell-Dateien herunterladen

Laden Sie diese **3 Dateien** von HuggingFace / ModelScope in denselben lokalen Ordner (Hauptmodell im **Repo-Root**, Vision-Projektor unter `mmproj/35B/`, Chat-Template unter `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Hauptmodell (erforderlich, 15,5 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Vision-Projektor (erforderlich, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Chat-Template (erforderlich, 7-Denken+LOOP)
```

### 6.2 Starten und verwenden

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Öffnen Sie `http://localhost:8080` im Browser. Vollständige Parameter in Abschnitt 9.

---

## 7. Modell-Downloads

| Plattform | Adresse |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/master) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored/tree/main) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM-Studio-Nutzer**: Suchen Sie `moziAI` in [LM Studio](https://lmstudio.ai) und laden Sie mit einem Klick herunter.

---

## 8. Startbefehle

### Minimaler Start (mit 3 Dateien)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Vollständiger empfohlener Start

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

> 💡 Bei wenig VRAM: `-c` verringern (z. B. 131072) oder `--fit on` hinzufügen.

---

## 9. Empfohlene Inferenzparameter

Optimiert durch lokale Tests (AMD Radeon AI PRO R9700 32GB):

| Parameter | Tägliche Aufgaben/Texten | Komplexe Aufgaben/Programmierung | Beschreibung |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Täglich stabil; komplex: moderate Exploration |
| top\_p | 0,95 | 0,95 | Nucleus-Sampling |
| top\_k | 20 | 20 | Truncated Sampling |
| min\_p | 0,024 | 0,024 | Min.-Wahrscheinlichkeitsfilter |
| repeat\_penalty | 1,05 | 1,05 | Wiederholungsstrafe |
| presence\_penalty | 0 | 0 | Keine Präsenzstrafe |
| context\_length | 262144 | 262144 | 256K langer Kontext |
| reasoning | on | on | Reasoning-Kette (CoT) |
| reasoning\_budget | 400 | 1000 | Reasoning-Budget (komplex höher) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Reasoning in separatem Feld |
| **spec-type** | **default** | **default** | **Spekulatives Decoding (ngram, MoE-optimal, Abschnitt 11)** |
| KV-Cache | q4\_0 | q4\_0 | Quantisierter KV-Cache (kv-unified) |

> 💡 **Denkmodus**: Aktivieren mit `--reasoning on` — das Modell denkt intern, bevor es antwortet. `reasoning_budget` begrenzt die Denk-Tokens.

---

## 10. Quantisierungsformatvergleich

| Format | Größe | Genauigkeit | Beschreibung |
| --- | --- | --- | --- |
| FP16 Original | ~70 GB | 100 % | Verlustfrei, Profi-GPU nötig |
| **MoziSmartBit (dieses Modell)** | **~15,5 GB** | **~99 %** | **Selbst entwickelt, beste Genauigkeit/Größe** |
| Q4_K_M | ~22 GB | ~98 % | GGUF-Standard 4-bit |
| Q5_K_M | ~24,7 GB | ~99 % | Höhere Genauigkeit |
| Q6_K | ~28,5 GB | ~99,5 % | Fast verlustfrei |
| Q8_0 | ~36,9 GB | ~100 % | Verlustfrei |

> MoziSmartBit hält ~99 % Genauigkeit und komprimiert 35B MoE auf 15,5 GB (4,5x), ~30 % kleiner als Q4_K_M.

---

## 11. Spekulatives Decoding (Schlüsselfunktion)

Dieses Modell beschleunigt die Inferenz durch **spekulatives Decoding** um **~1,5-2x** (lokal gemessen).

- **MoE-optimal**: llama.cpp empfiehlt **ngram** (`--spec-default`) für MoE — am schnellsten und stabilsten im Test
- **Zum „MTP" im Namen**: stammt von den Multi-Token-Prediction-Gewichten der Basis (vollständig erhalten); llama.cpps MTP-Draft-Unterstützung für MoE ist begrenzt, daher nutzt MoziAI ngram

```bash
--spec-default
```

---

## 12. VRAM-Empfehlungen

Gemessen mit MoziSmartBit-Build (Modell + Vision ~16,4 GB):

| VRAM | Empfehlung | Beschreibung |
| --- | --- | --- |
| 20 GB | 150K Kontext, q4\_0, Vision | ~19,5 GB Nutzung |
| **24 GB** | **Voll 256K, q4\_0, Vision perfekt** | **Empfohlen**: ~20,4 GB, ~3,6 GB Reserve |
| 32 GB+ | Voll 256K, viel Reserve | R9700 32GB: ~10 GB Reserve |

> 💡 Längerer Kontext = mehr VRAM. Bei OOM `-c` reduzieren oder `--fit on`. NVIDIA / AMD unterstützt.

---

## 13. Bereitstellungsmethoden

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

Suchen Sie `moziAI` in LM Studio / Jan und laden Sie die Q4\_K\_M-Version (LM Studio liest Standard-Root-Modelle; für ältere Versionen „aus URL hinzufügen" verwenden).

> 💡 Ollamas mmproj- und chat\_template-Unterstützung ist begrenzt — llama.cpp für volle Funktionen.

---

## 14. Benchmarks

MoziAI-35B-V3.8 basiert auf deepreinforce-ai/Ornith-1.5-35B-A3B (Feinabstimmung/Destillation). Daten aus V3.7-Messungen (V3.8 = gleiche Basis und Trainingssystem):

| Benchmark | moziAI-35B-V3.8<br>(dieses Modell) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmierung** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67,8 | 64,2 | 52,5 | 42,1 | 51,7 | 53,5 |
| Terminal-Bench 2.1 (Claude Code) | 68,5 | 62,8 | 49,2 | - | - | 48,6 |
| SWE-bench Verified | 79 | 75,6 | 73,4 | 52 | 76 | 76,4 |
| SWE-bench Pro | 59,6 | 50,4 | 49,5 | 35,7 | 51,2 | 51,6 |
| SWE-bench Multilingual | 71,4 | 69,3 | 67,2 | 51,7 | - | 69,3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5,1 | 1,4 | 1,4 | - | - | 1,4 |
| NL2Repo | 46,2 | 34,6 | 29,4 | 15,5 | - | 36,8 |
| SWE Atlas - QnA | 39,8 | 37,1 | 15,5 | - | - | 20,4 |
| **Reasoning** |  |  |  |  |  |  |
| HLE (no tools) | 25,6 | 20,8 | 21,4 | 19,5 | 22 | 28,7 |
| HLE (with tools) | 33,4 | 30,1 | 28,9 | 26,5 | - | 48,3 |
| GPQA Diamond | 89,2 | 86,2 | 86 | 84,3 | 83,5 | 88,4 |
| **Agentisch** |  |  |  |  |  |  |
| MCP-Atlas | 70,2 | 64,4 | 62,8 | 55 | 75,5 | 72,3 |
| Toolathlon-Verified | 48,7 | 42,4 | 41,7 | 40,8 | - | 38,3 |
| WideSearch | 67,8 | 63,4 | 60,1 | 54,2 | - | 74 |
| BrowseComp | 67,6 | 63,5 | 62 | - | - | 78,6 |
| ClawEval | 72,5 | 69,8 | 68,7 | 48,5 | - | 70,7 |

> Im Finanzbereich (Bilanzen, Quant, Risiko, Agent-Tools) deutlich besser als allgemeine Modelle. Gemma-4 / Qwen3.6 sind offizielle Ergebnisse.

---

## 15. Uncensored-Optimierung

Dieses Modell erbt die Uncensored-Eigenschaft von Ornith-1.5-35B-A3B:

| Vorteil | Beschreibung |
| --- | --- |
| Keine Einschränkungen | Lehnt kein Thema ab, auch sensible |
| Freie Ausgabe | Keine Sicherheitspolitik-Grenzen |
| Vollständige Infos | Ungefiltert, ideal für Forschung |
| Lokale Privatsphäre | Daten vollständig privat |

**Hinweis**: Lokales Modell — die Ausgabe wird vom Nutzer kontrolliert; das Modell trägt keine Moderatonsverantwortung.

---

## 16. Lizenz

**Benutzerdefinierte restriktive Lizenz**:

- ✅ **Erlaubt** — kostenlose kommerzielle Nutzung, Kopie, Verteilung
- ❌ **Verboten** — Weiterentwicklung, Weiterverkauf, Unterlizenzierung
- 📋 **Erforderlich** — Urheberrechtshinweis, Quelle: moziAI-35B

Modell „wie besehen" ohne Garantien. Ausgabe ist keine Anlageberatung.

---

## 17. Kontakt

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo) · **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen) · **E-Mail**: 263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. Alle Rechte vorbehalten.