---
language:
- de
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

# MoziAI-35B-A3B-MOE - Finanzieller vertikaler Domänen-LLM - V3.6

[中文](README.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Deutsch | [Français](README.fr.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md) | [繁體中文](README.zh-hant.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md)

## Modellübersicht

MoziAI-35B-A3B-MOE ist ein lokales Open-Source-finanzielles KI-Multimodal-LLM (unterstützt Vision und Tool Calling), entwickelt vom Team des chinesischen Finanz-Influencers Chen Yumo, feinabgestimmt/distilliert aus dem Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**-Architektur, MIT-lizenziert) Basismodell. Durch die selbst entwickelte **MoziSmartBit Intelligent Quantization**-Technologie wird das 35B-Parameter-MoE-Modell auf ca. **15,5 GB** komprimiert und erreicht eine optimale Balance zwischen Präzision und Größe mit nahezu verlustfreier ~99% Präzisionsqualität.

Neben der Beibehaltung allgemeiner KI-Fähigkeiten konzentriert sich dieses Modell auf die Optimierung vertikaler Finanzdomänen-Anwendungen, einschließlich Finanz-Q&A, quantitativer Programmierung, Tool Calling und allgemeiner Programmierung.

Der Modellentwickler Chen Yumo verwendet dieses Modell häufig für lokale Finanzdatenanalyse, Quantitative-Strategie-Entwicklung, Marktforschung, Artikelschreibung, Gesamtprojektvorantreiben, allgemeine Programmierung und 256K-Kontext-Aufgaben über OpenClaw/Hermes. Es kann auf verbrauchertauglichen GPUs lokal bereitgestellt werden und spart erhebliche Cloud-Token-Kosten und erreicht 7×24 Token-Freiheit bei gleichzeitiger Gewährleistung der lokalen Datendatenprivacy und -sicherheit.

Unterstützt llama.cpp, Ollama, LM Studio und andere Mainstream-Inferenzframeworks.

**Veröffentlichungsdatum: 2026-08-20** | **Version: V3.6**

## Modellfunktionen

- **Finanzieller vertikaler Fokus**: Tiefgehende Optimierung für Finanz-Q&A, Quantitative Programmierung und Tool Calling
- **MoziSmartBit Intelligent Quantization**: Selbst entwickelte intelligente Quantisierung, optimale Balance von Präzision und Größe, komprimiert auf ca. **15,5 GB**
- **Verbrauchertaugliche Bereitstellung**: Auf verbrauchertauglichen GPUs mit 20 GB oder 24 GB+ VRAM deploybar, unterstützt 256K-lange Kontexte
- **Mehrsprachige Unterstützung**: 201 Sprachen und Dialekte, mit erweiterten Chinesisch-Fähigkeiten, Abdeckung von Englisch/Japanisch/Koreanisch/Deutsch/Französisch/Spanisch/Portugiesisch und mehr
- **Allgemeine Programmierung**: Full-Stack-Entwicklung, Code-Debugging, Architekturdesign, Skripterstellung, Abdeckung von Python/JS/TS/Go/Rust und anderen Mainstream-Sprachen
- **Artikelschreibung**: Hochwertiges Multi-Genre-Schreiben einschließlich Forschungsberichte, Analyseartikel, technische Dokumentation, kreative Inhalte
- **Vision-Verständnis**: Unterstützt multimodale Vision, lokale Screenshot-Eingabe, Bildverständnis
- **Uncensored freie Ausgabe**: Keine Inhaltszensur, freie Diskussion über jedes Thema ohne Einschränkungen
- **Erweiterte Reasoning**: Chain-of-Training für verbesserte Reasoning-Qualität
- **Multi-Framework-Unterstützung**: Kompatibel mit llama.cpp, Ollama, LM Studio, Jan
- **Multi-Agent-Plattformunterstützung**: Tiefe Integration mit OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex und anderen Mainstream-AI-IDEs und Agent-Frameworks, nativer Support für Tool Calling und Multi-Turn-Task-Orchestrierung, sofort einsetzbar

## Uncensored-Vorteile

Dieses Modell erbt die **Uncensored**-Funktion des Ornith-1.0-35B-Basismodells mit folgenden Vorteilen:

| Vorteil | Beschreibung |
|---------|--------------|
| **Keine Zensur** | Weigert sich nicht, jedes Thema zu behandeln, einschließlich sensibler oder kontroverser Inhalte |
| **Freie Ausgabe** | Nicht durch Sicherheitsrichtlinien eingeschränkt, kann jeden Typ von Antwort generieren |
| **Vollständige Informationen** | Stellt ungefilterte vollständige Informationen bereit, geeignet für Forschung und Analyse |
| **Lokale Datenschutz** | Lokale Bereitstellung bedeutet vollständige Datenprivacy und Freiheit von Cloud-Zensur |

> **Anwendungsfälle**: Wissenschaftliche Forschung, Tiefenanalyse, freie Diskussion, uneingeschränktes KI-Gespräch.
> **Hinweis**: Dies ist ein lokal bereitgestelltes Modell, der Ausgabevollinhalt wird vollständig vom Benutzer kontrolliert, keine Inhaltsmoderationsverantwortung.

## Kerndefinitionen

| Fähigkeitsbereich | Beschreibung |
|-------------------|--------------|
| Marktanalyse | Makro-/Mikroökonomische Interpretation, A-Aktien/HK/US-Aktien/Rohstoffe/Krypto-Marktlogik |
| Finanzberichte | Wichtige finanzielle Indikator-Interpretation, Forschungsbericht-Zusammenfassung, Bewertungs- & Ertragsprognose-Unterstützung |
| Risiko & Compliance | Produktrisikobewertung, Anlageberatungs-Compliance, finanzielle Regulierungsrichtlinien-Interpretation |
| Quant & Strategie | Quant-Strategie-Design, Pyramid (PEL) Quantisierung, Backtesting-Logik, Faktorkonstruktion und Tool Calling |
| Tool Calling | Integration mit Echtzeitkursen, Datenbanken, Forschungsbericht-Abruf und anderen finanziellen Datenquellen |

## Technische Spezifikationen

| Punkt | Spezifikation |
|-------|---------------|
| Basismodell | Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT-lizenziert) |
| Parameter | 35B MoE (256 geroutete Experten + 1 geteilter Experte, 8 aktive pro Token) |
| Quantisierung | Selbst entwickelte MoziSmartBit Intelligent Quantization + GGUF-Standardformat |
| Kontextlänge | 256K (262.144 Tokens) |
| Modellgröße | ~15,5 GB (MoziSmartBit Uncensored-Version) |
| Min. VRAM | Verbrauchertaugliche GPUs mit 20 GB+ VRAM (z. B. RTX 4060 Ti 16G mit CPU-Offload), 24 GB empfohlen (mit Vision + langer Kontext) |
| Inferenzframework | llama.cpp / Ollama / LM Studio / Jan |
| Inferenzgeschwindigkeit | Algorithmusoptimiert: 140+ Token/s auf AMD R700 GPUs, 70+ Token/s auf AMD MAX+395 CPU iGPU, lokaler Token-Freiheit |
| Team | Chen Yumo Team |

## Quantisierungsformat & Modellgrößenvergleich

| Quant-Format | Modellgröße | Präzision | Hinweise |
|--------------|-------------|-----------|----------|
| **FP16 (Original)** | ~70 GB | 100% | Original 16bit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Von MoziAI verwendet, optimales Quantisierungsschema** |
| Q4_K_M | ~21,2 GB | ~98% | GGUF-Standard 4bit |
| Q5_K_M | ~24,7 GB | ~99% | Höhere Qualität |
| Q6_K | ~28,5 GB | ~99,5% | Nahezu verlustfrei |
| Q8_0 | ~36,9 GB | ~100% | Verlustfrei |

> MoziAI V3.6 verwendet MoziSmartBit Intelligent Quantization und erhält ~99% Präzision bei Komprimierung des 35B-Parameter-MoE-Modells auf ~15,5 GB (~4,5x Komprimierungsrate), Balance zwischen Inferenzqualität und Bereitstellungsmöglichkeiten für verbrauchertaugliche GPUs.

## MoziSmartBit Intelligent Quantization

Herkömmliche Quantisierung verwendet einheitliche Präzision über alle Schichten. **MoziSmartBit Intelligent Quantization** wendet differenzierte Quantisierungsstrategien für optimale Größe-Präzisions-Balance an.

### Kompressionseffekt

Herkömmliche Quantisierung komprimiert alle Teile des Modells gleichmäßig, was häufig zu erheblichen Präzisionsverlusten führt. MoziSmartBit Intelligent Quantization verwendet eine selbst entwickelte intelligente Kompressionsstrategie, die **erhebliche Größenreduzierung mit minimalem Präzisionsverlust** erreicht:

- **Minimaler Quantisierungsverlust**: Trainingsergebnis > Quantisierungsverlust. Das trainierte MoziAI-35B erreicht bessere PPL auf finanziellen Domänentexten als das Vor-Training bf16-Basismodell, Reduzierung von Halluzinationen und Perplexität im Vergleich zu ähnlichen KI-Modellen
- **~4,5x Größenreduzierung**: Komprimiert von ~70 GB (FP16) auf ~15,5 GB, auch deutlich kleiner als Q4_K_M (~21 GB), erhebliche Reduzierung der VRAM- und Speicheranforderungen
- **Verbraucher-GPU-freundlich**: Ein 35B-MoE-Modell, das zuvor High-End-GPU erforderte, kann jetzt reibungslos auf 20 GB~24 GB VRAM laufen

### Vergleichsvorteile

**vs Q4_K_M (~21,2 GB)**: ~27% kleiner (~15,5 GB), mit **höherer** Präzision als Q4_K_M, niedrigere VRAM-Hürde — läuft reibungslos auf mittelklasse verbrauchertauglichen GPUs (24 GB).

**vs FP16-Original (~70 GB)**: ~4,5x Komprimierung, Trainingseffektivität + minimaler Quantisierungsverlust (Trainingsergebnis > Quantisierungsverlust), Ermöglichung lokaler 256K-Kontextbereitstellung auf verbrauchertauglichen GPUs statt High-End-Hardware.

## Empfohlene Inferenzparameter

Basierend auf lokaler Produktionskonfiguration (AMD Radeon AI PRO R9700 32GB):

| Parameter | Wert | Beschreibung |
|-----------|------|--------------|
| temperature | 0,6 | Balance zwischen Kreativität und Genauigkeit |
| top_p | 0,95 | Nucleus-Sampling-Schwelle |
| top_k | 20 | Trunkations-Sampling (V3.6 optimiert) |
| repeat_penalty | 1,05 | Wiederholungsstrafe |
| presence_penalty | 0 | Keine Anwesenheitsstrafe |
| context_length | 262144 | 256K langer Kontext |
| batch_size | 2048 | Stapelgröße |
| ubatch_size | 512 | Mikro-Stapelgröße |
| flash_attention | auto | Auto Flash Attention |
| kv_cache | q4_0 | KV-Cache-Quantisierung (kv-unified) |
| poll | 0 | Kein GPU-Polling im Leerlauf, energiesparend |
| reasoning | on | Reasoning-Chain aktivieren (Chain of Thought) |
| reasoning_budget | 400 | Reasoning-Budget in Tokens |
| reasoning_format | deepseek-legacy | Reasoning-Format |
| samplers | top_k;top_p;temperature;typ_p | Sampler-Reihenfolge |

### llama.cpp Startbefehl

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
  --temp 0,6 --top-p 0,95 --top-k 20
```

### VRAM-Konfigurationsempfehlungen

Da sich die GPU-Konfigurationen der Benutzer stark unterscheiden, hier empfohlene Parameter für verschiedene VRAM-Größen (alle für MoziSmartBit-Version):

| VRAM | Empfohlener Kontext | KV Cache | Vision-Unterstützung | Hinweise |
|------|---------------------|----------|----------------------|----------|
| 20 GB | 150K | q4_0 | Unterstützt | Modell+Vision ~16,4GB, Test zeigt 200K+Vision verwendet ~19,5GB VRAM |
| 24 GB | 256K voll | q4_0 | Vollständig | Vision+256K langer Kontext, verwendet ~20,4GB VRAM, ~3,6GB Spielraum |
| 32 GB+ | 256K voll | q4_0 | Vollständig | Vision+256K langer Kontext, ausreichender Spielraum ~10GB, beste Konfiguration |

**NVIDIA**

| VRAM | GPU-Modell |
|------|------------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD**

| VRAM | GPU-Modell |
|------|------------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel**

| VRAM | GPU-Modell |
|------|------------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (erfordert CPU-Offload) |

**Gemeinsamer Speicher iGPUs**

| VRAM | Prozessor |
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |

> 💡 **Hinweis**: Solange Ihre VRAM den obigen Anforderungen entspricht, funktioniert es. Keine Marken- oder Modellbeschränkungen. Unterstützt NVIDIA / AMD / Intel Dedizierte GPUs und auch die oben aufgeführten 128GB Unified Memory iGPUs.

> 💡 **Hinweis**: Längere Kontexte verwenden mehr VRAM. Wenn Sie auf OOM (Out of Memory) stoßen, reduzieren Sie schrittweise den `-c`-Wert. Verwenden Sie `--fit on`, damit llama.cpp die Schichten automatisch an Ihre VRAM anpasst.

### Ollama-Bereitstellung

```bash
# Modelfile erstellen
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0,6
PARAMETER top_p 0,95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Erstellen und ausführen
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan Bereitstellung

Suchen Sie in LM Studio oder Jan nach `moziAI-35B` und laden Sie die MoziSmartBit-Quant-Version herunter.

## Benchmark-Bewertung

MoziAI ist feinabgestimmt von **deepreinforce-ai/Ornith-1.0-35B**. MoziAI ist auf dem Basismodell für finanzielle vertikale Domänen optimiert und liefert überlegene Leistung in Finanz-Q&A, Quantitativer Programmierung und Tool-Calling-Szenarien. Die allgemeinen Fähigkeiten von MoziAI-35B stimmen mit dem Ornith-1.0-35B-Basismodell überein.

| Benchmark | MoziAI-35B (dieses Modell) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Beschreibung |
|-----------|---------------------------|-------------|------------|------------|-------------|--------------|
| Terminal-Bench 2.1 | 64,2 | 59,3 | 42,1 | - | 41,4 | Autonomes Terminal-Coding |
| Terminal-Bench (Claude Code) | 62,8 | 59,3 | - | - | 38,9 | Claude-Code-Coding |
| SWE-bench Verified | 75,6 | 77,2 | 52,0 | - | 70,0 | Software-Engineering in der Praxis |
| SWE-bench Pro | 50,4 | 53,5 | 35,7 | - | 44,6 | Komplexes Software-Engineering |
| SWE-bench Multilingual | 69,3 | 71,3 | - | - | 60,3 | Mehrsprachiges Coding |
| NL2Repo | 34,6 | 36,2 | 15,5 | - | 20,5 | Natürliche Sprache zu Repo |
| LiveCodeBench v6 | 63,3 | 83,9 | 80,0 | 77,1 | - | Wettbewerbsprogrammierung |
| GPQA Diamond | 88,4 | 87,8 | 84,3 | 82,3 | - | Wissenschaftliches Reasoning |
| AIME 2026 Math | 93,3 | 94,1 | 89,2 | 88,3 | - | Mathematisches Reasoning |

> Die allgemeinen Benchmark-Ergebnisse von MoziAI-35B stimmen mit dem Ornith-1.0-35B-Basismodell überein. Die finanzielle vertikale Domäne ist MoziAI's Hauptoptimierungsrichtung, die in Szenarien wie Finanzberichtsanalyse, Quantitative Strategie, Risiko & Compliance und Agent-Tool-Calling deutlich überlegen gegenüber allgemeinen Modellen abschneidet. Gemma4- und Qwen3.6-Daten aus offiziellen öffentlichen Ergebnissen.

## Modell-Download

Aufgrund der großen Modellgröße (~15,5 GB) werden die Gewichte auf mehreren Community-Plattformen gehostet:

| Plattform | URL |
|-----------|-----|
| HuggingFace | [chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://huggingface.co/chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |
| ModelScope | [chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://modelscope.cn/models/chenyumo/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |
| GitHub | [chenyumo166/moziAI-35B-Qwen3.6-35B-A3B-Ornith](https://github.com/chenyumo166/moziAI-35B-Qwen3.6-35B-A3B-Ornith) |

> 💡 **Download-Hinweis**: Klicken Sie auf den obigen Link, um zum HuggingFace-Repository zu gelangen, und navigieren Sie dann zum Tab **„Files and versions"**, um alle Dateien im V3.6-Verzeichnis herunterzuladen (Hauptmodell, Vision-Projektion, Chat-Template). Stellen Sie sicher, dass sich alle drei Dateien im selben Verzeichnis befinden.

### ⚠️ Wichtig: Vision-Fähigkeit erfordert mmproj-Datei

Dieses Modell unterstützt multimodale Vision. Die **Vision-Projektionsdatei (mmproj)** ist im Versionsverzeichnis enthalten:

- **Vision-Datei**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16-Präzision)
- **Ablage**: Im selben Versionsverzeichnis wie die GGUF-Modelldatei
- **Laden**: Mit `--mmproj`-Flag beim Starten von llama-server laden

```bash
llama-server -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf
```

> Ohne die Vision-Datei verliert das Modell die **Bildverständnisfähigkeit** und behält nur textbasierte Konversation bei.

## Schnellstart

### 1. Modelldateien herunterladen

Laden Sie alle Dateien im V3.6-Verzeichnis von HuggingFace / ModelScope herunter:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Hauptmodell (erforderlich)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision-Projektion (optional)
└── moziAI-V3.6-35B-chat-template.jinja                  # Chat-Template (empfohlen)
```

### 2. Inferenzserver starten

Für die vollständige empfohlene Konfiguration siehe [llama.cpp Startbefehl](#llamacpp-startbefehl) oben.

Minimaler Start (nur Kernparameter):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Fügen Sie `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` für Vision-Fähigkeit hinzu.

### 3. Nutzung starten

Öffnen Sie `http://localhost:8080` in Ihrem Browser, um zu chatten.

### Verzeichnisstruktur

```
moziAI-35B/
├── README.md              # Chinesische Version
├── README.en.md           # Englische Version
├── README.de.md           # Deutsche Version (diese Datei)
├── LICENSE                # Lizenz
├── V3.6/                  # V3.6-Version (eigenständig)
│   ├── RELEASE_NOTES.md                       # Veröffentlichungshinweise
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Hauptmodell
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Vision-Projektion
│   └── moziAI-V3.6-35B-chat-template.jinja   # Chat-Template
```

Zukünftige Upgrade-Pläne siehe [未来升级计划.md](未来升级计划.md).

## SEO-Stichwörter

Finanzielle KI LLM, lokales Open-Source-Modell, Endgerät-Modell, Quantitative Programmierung, MoziSmartBit, intelligente Quantisierung, GGUF-Quantisierung, MoE-Modell, lokales Open-Source-LLM, lokale Bereitstellung, finanzielle KI, Tool Calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, keine Zensur, freie Ausgabe, uneingeschränkt, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5, Qwen3.6, finanzielle vertikale Domäne, Open-Source-Modell

## Lizenz (Wichtig)

Dieses Modell verwendet eine **Eingeschränkte benutzerdefinierte Lizenz**:

### ✅ Erlaubt
- **Freie kommerzielle Nutzung**: Frei integrierbar in kommerzielle Produkte
- **Kopieren & Verteilen**: Kann kopiert, heruntergeladen und geteilt werden

### ❌ Verboten
- **Derivative Werke**: Keine Modifikation, Übersetzung, Anpassung, Zusammenführung oder Feinabstimmung des Modells oder eines Teils davon
- **Weiterverkauf**: Kein Verkauf des Modells allein oder als Teil eines Produkts
- **Weiterlizensierung**: Keine Erteilung von Unterlizenzen

### 📋 Anforderungen
- Muss ursprünglichen Copyright-Hinweis beibehalten
- Nennung: moziAI-35B

> Vollständige Bedingungen siehe [LICENSE](./LICENSE).

## Haftungsausschluss

Wird „wie es ist" ohne Gewähr bereitgestellt. Modellausgabe dient nur als Referenz, keine Anlageberatung. Benutzer tragen alle Risiken.

## Kontakt

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-Mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. Alle Rechte vorbehalten.
