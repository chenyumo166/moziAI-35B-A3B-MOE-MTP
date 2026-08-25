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
library_name: llama-cpp
pipeline_tag: text-generation
---

# moziAI-13.7-35B-A3B-A3B-MOE-MTP-Uncensored - Kleines aber starkes multimodales KI-Modell für kostenlose lokale Bereitstellung

Language / Sprache wählen  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Modellübersicht

MoziAI-35B-A3B-MOE ist ein lokales Open-Source-multimodales KI-Großmodell, das vom Team des chinesischen Finanz-Influencers Chen Yumo entwickelt wurde (stärker im Finanzbereich, unterstützt Vision, Tool Calling, komplexe Langzeitaufgaben und lokale Bereitstellung auf Consumer-GPUs). moziAI-35B basiert auf dem Open-Source-Basismodell Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B-Architektur, MIT-lizenziert) und integriert die selbst entwickelten: (Finanzdaten + Finanzbereichsfähigkeiten + Trainingsmethoden + Seven-Dimensional-Thinking-Framework + Agent-LOOP-Mechanismus + hybriden Quantisierungsalgorithmus MoziSmartBit) des Chen-Yumo-Teams. Durch die selbst entwickelte MoziSmartBit-Intelligent-Quantisierungstechnologie wird das 35B-Parameter-MoE-Modell auf ca. 15,5 GB komprimiert, was 6,5 GB (ca. 30%) kleiner ist als herkömmliche Q4_K_M-Quantisierungsmodelle von ca. 22+ GB; es wird das optimale Gleichgewicht zwischen Präzision und Größe erreicht, mit nahezu verlustfreier ≈99% FP16-Präzisionsqualität.

Die Philosophie des Entwicklungsteams dieses Modells ist es, dass lokale KI-Großmodell-Agenten mit umfassenden Fähigkeiten in jeden Haushalt und in kleine und mittlere Unternehmen Einzug halten, ohne dass hohe KI-Hardwarekosten oder Cloud-API-Kosten anfallen. Durch die selbstentwickelte **MoziSmartBit Intelligente Quantisierungstechnologie** wird das MoE-Modell mit 35 Milliarden Parametern auf ca. **15,5 GB** komprimiert. Dadurch wird ein optimales Gleichgewicht zwischen Modellgenauigkeit und Größe erreicht und eine Genauigkeitsqualität von fast 99% im Vergleich zu FP16 erzielt. Dieses Modell hat 35 Milliarden Parameter, nutzt jedoch die MOE-Sparse-Expertentechnologie, sodass nur 3 Milliarden Parameter aktiviert werden und MTP-Spekulativedekodierung für beschleunigte Inferenz unterstützt wird. Praxistests zeigen, dass es auf Consumer-Grafikkarten mit 20 GB VRAM lokal kostenlos bereitgestellt werden kann und Inferenzgeschwindigkeiten von über 140 Token/s erreicht – schneller als viele kostenpflichtige Cloud-KI-Großmodelle.

Neben den Fähigkeiten eines allgemeinen KI-Großmodells liegt der Fokus der Optimierung auf: Finanzanwendungen, Finanz-Q&A, quantitative Programmierung, allgemeine Programmierung, Tool-Aufrufe, Erfolgsrate komplexer 256K-Langkontextaufgaben und weitere Schlüsselfähigkeiten von KI-Großmodellen. Es kann kostenlos auf lokalen Consumer-Grafikkarten bereitgestellt und verwendet werden, spart enorme Cloud-Token-Kosten, ermöglicht 24/7 Token-Freiheit und gewährleistet lokale Datenprivatsphäre und -sicherheit.

**Veröffentlichungsdatum:** 2026-08-20 | **Version:** V3.6

## Modelldownload

Da die Modelldatei relativ groß ist (~15,5 GB), werden die Modellgewichte auf mehreren Community-Plattformen gehostet:

| Plattform | Adresse |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio Benutzer**: Suchen Sie direkt in [LM Studio](https://lmstudio.ai) nach `moziAI` und laden Sie es mit einem Klick herunter – kein manueller Dateidownload erforderlich.  
> 💡 **Download-Hinweis**: Klicken Sie auf den obigen Link, um zum HuggingFace-Repository zu gelangen. Laden Sie im Tab **"Files and versions"** alle Dateien aus dem V3.6-Verzeichnis herunter (Hauptmodell, visuelle Projektion, Chat-Vorlage) und stellen Sie sicher, dass sich alle drei Dateien im selben Verzeichnis befinden.

### ⚠️ Wichtig: Für Bildfähigkeiten ist eine zusätzliche mmproj-Datei erforderlich

Dieses Modell unterstützt multimodale Bildverarbeitung. Die visuelle Projektionsdatei (mmproj) ist im Versionsverzeichnis enthalten:

- **Visuelle Datei**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (ca. 903 MB, BF16-Genauigkeit)
- **Speicherort**: Im selben Versionsverzeichnis wie die GGUF-Modelldatei
- **Lademethode**: Beim Start von llama-server über den Parameter `--mmproj` laden

> Ohne Laden der visuellen Datei geht die Bildverständnisfähigkeit verloren, es bleibt nur die reine Textkonversationsfähigkeit erhalten.

### ⚠️ Wichtig: Die Chat-Vorlagendatei muss geladen werden

Dieses Modell verwendet eine exklusive Chat-Vorlage (chat-template). **Ohne Laden kommt es zu Konversationsformatfehlern, die Denkkette funktioniert nicht und die Antwortqualität sinkt drastisch**. Die Chat-Vorlagendatei ist im Versionsverzeichnis enthalten:

- **Vorlagendatei**: `moziAI-V3.6-35B-chat-template.jinja` (ca. 5 KB, im Jinja-Format)
- **Speicherort**: Im selben Versionsverzeichnis wie die GGUF-Modelldatei
- **Lademethode**: Beim Start von llama-server über den Parameter `--chat-template-file` laden

> Ohne Laden der Chat-Vorlage kann das Modell Systemhinweise, Benutzernachrichten und Denkblöcke möglicherweise nicht korrekt erkennen, was zu unübersichtlichen Ausgabeformaten oder verminderter Inferenzfähigkeit führt.

### llama.cpp Startbefehl (Empfohlene Konfiguration für 20G+ Grafikkarten mit 256K-Kontext)

> Hinweis: Wenn der VRAM unter 20 GB liegt, reduzieren Sie den Kontextparameter 262144 bei `-c 262144`.

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --spec-default \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

## Schnellstart

### 1. Modelldateien herunterladen

Laden Sie alle Dateien aus dem V3.6-Verzeichnis von HuggingFace / ModelScope auf Ihren lokalen Rechner herunter:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Hauptmodell (erforderlich)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Visuelle Projektion (optional, bei Bedarf herunterladen)
└── moziAI-V3.6-35B-chat-template.jinja                  # Chat-Vorlage (erforderlich! Ohne Laden treten Konversationsformatfehler auf)
```

> ⚠️ **Die Chat-Vorlage ist eine Pflichtdatei**, keine Option. Dieses Modell verfügt über ein benutzerdefiniertes Konversationsformat (einschließlich Denkkette/Denkblock). Fehlt die Vorlage, führt dies zu unübersichtlichen Modellausgabeformaten und Funktionsverlust der Inferenz. Bitte unbedingt herunterladen und beim Start laden.

### 2. Inferenzdienst starten

Den vollständigen empfohlenen Startbefehl finden Sie im Abschnitt [llama.cpp Startbefehl](#llamacpp-startbefehl) unten.

Einfachster Start (nur Kernparameter):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Wenn Sie Bildfähigkeiten benötigen, fügen Sie `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` hinzu.

### 3. Nutzung beginnen

Öffnen Sie `http://localhost:8080` im Browser, um mit dem Chat zu beginnen.

### Verzeichnisstruktur

```
moziAI-35B/
├── README.md              # Englische Anleitung
├── README.de.md           # Diese Datei (Deutsche Anleitung)
├── LICENSE                # Lizenz
├── V3.6/                  # V3.6 Version (versionsunabhängig)
│   ├── RELEASE_NOTES.md                       # Versionsaktualisierungen
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Hauptmodell
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Visuelle Projektion
│   └── moziAI-V3.6-35B-chat-template.jinja   # Chat-Vorlage
```

## Modellmerkmale

- **MoziSmartBit Intelligente Quantisierung**: Selbstentwickelte intelligente Quantisierungstechnologie mit optimalem Gleichgewicht zwischen Genauigkeit und Größe, das Modell wird nahezu verlustfrei auf ca. **15,5 GB** komprimiert
- **Fähigkeit für komplexe Langzeitaufgaben**: Training ermöglicht dem Modell-Agenten eine selbstständige Planung mit intelligentem Schleifenprozess zur Bewältigung von Engpässen und Selbstdenkmechanismus, ermöglicht automatische Ausführung und Selbstanpassung komplexer Aufgaben – ohne dass der menschliche Benutzer ständig Optimierungshinweise für den Agenten geben muss
- **Kleines Modell, große Fähigkeiten**: Bei komplexen Aufgaben übertrifft die Gesamtfähigkeit Modelle mit vergleichbaren 35 Milliarden Parametern und sogar einige Modelle mit mehrfach höheren Parameterzahlen
- **Geschwindigkeitsvorteil von MOE+MTP**: Obwohl das Modell insgesamt 35 Milliarden Parameter hat, werden tatsächlich nur 8+1 Experten mit insgesamt 3 Milliarden Parametern aktiviert. Die Inferenzgeschwindigkeit ist höher, ideal für Consumer-Grafikkarten mit 20 GB~24 GB VRAM für lokale Bereitstellung mit über 140 Token/s
- **Tiefe Finanzexpertise**: Tiefgehende Stärkung von Finanz-Q&A, quantitativer Programmierung und Tool-Aufruf-Fähigkeiten
- **Consumer-Bereitstellung**: Consumer-Grafikkarten mit 20 GB~24 GB VRAM oder mehr reichen für lokale Bereitstellung, unterstützt bis zu 256K langen Kontext
- **Mehrsprachige Unterstützung**: Unterstützt 201 Sprachen und Dialekte, Chinesisch besonders optimiert, deckt Englisch, Japanisch, Koreanisch, Deutsch, Französisch, Portugiesisch und andere Hauptsprachen ab
- **Allgemeine Programmierfähigkeit**: Unterstützt Full-Stack-Entwicklung, Code-Debugging, Architekturdesign, Skripterstellung, deckt Python/JS/TS/Go/Rust und andere Hauptsprachen ab
- **Artikelschreibfähigkeit**: Unterstützt hochwertiges Schreiben verschiedener Genres, einschließlich Forschungsberichte, Analyseartikel, technische Dokumentation, kreative Inhalte usw.
- **Bildverständnis**: Durch Laden der visuellen Datei im Inferenzframework wird multimodale Bildverarbeitung unterstützt. Screenshots können lokal im Chat-Fenster geteilt werden und das Modell kann die Informationen im Bild verstehen
- **Unzensierte freie Ausgabe**: Keine Inhaltsüberprüfungsbeschränkungen, freie Diskussion zu jedem Thema, nicht durch Sicherheitsrichtlinien beschränkt
- **Verbesserte Inferenzlogik**: Trainiert in Verbindung mit Inferenzlogik (Denkkette), zur weiteren Steigerung der Inferenzqualität
- **Multi-Framework-Unterstützung**: Kompatibel mit llama.cpp、Ollama、LM Studio、Jan und anderen gängigen Inferenzframeworks
- **Multi-Agent-Plattformunterstützung**: Tiefgehend angepasst an OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex und andere gängige in- und ausländische AI-IDEs und Agent-Frameworks, native Unterstützung für Tool-Aufrufe und mehrstufige Aufgabenorchestrierung, sofort einsatzbereit

## Vorteile von Uncensored (ohne Zensur)

Dieses Modell erbt die Uncensored-Eigenschaft des Basismodells Ornith-1.0-35B-A3B und bietet folgende Vorteile:

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Vorteil</th>
<th>Beschreibung</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keine Überprüfungsbeschränkungen</td>
<td>Lehnt kein Thema ab, einschließlich sensibler und kontroverser Inhalte</td>
</tr>
<tr>
<td>Freie Ausgabe</td>
<td>Nicht durch Sicherheitsrichtlinien beschränkt, kann jede Art von Antwort generieren</td>
</tr>
<tr>
<td>Vollständige Informationen</td>
<td>Bietet ungefilterte vollständige Informationen, geeignet für Forschungs- und Analyseszenarien</td>
</tr>
<tr>
<td>Lokal privat</td>
<td>Lokale Bereitstellung bedeutet vollständig private Daten, keine Cloud-Überprüfung</td>
</tr>
</tbody>
</table>

> **Anwendungsbereiche**: Kostenlose kommerzielle Nutzung, akademische Forschung, Tiefenanalyse, freie Diskussion, uneingeschränkte KI-Konversation
> **Hinweis**: Dieses Modell ist ein lokal bereitgestelltes Modell. Die Ausgaben werden vollständig vom Benutzer gesteuert, es wird keine Verantwortung für die Inhaltsüberprüfung übernommen.

## Kernfähigkeiten

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Fähigkeitsbereich</th>
<th>Beschreibung</th>
</tr>
</thead>
<tbody>
<tr>
<td>Marktanalyse</td>
<td>Makro-/Mikroökonomie-Interpretation, A-Aktien/Hongkong-Aktien/US-Aktien/Rohstoffe/Kryptowährung Kurse und logische Aufbereitung</td>
</tr>
<tr>
<td>Finanzen & Forschungsberichte</td>
<td>Interpretation wichtiger Finanzkennzahlen, Extraktion von Forschungsberichtszusammenfassungen, Unterstützung bei Bewertung und Gewinnprognose</td>
</tr>
<tr>
<td>Risikomanagement & Compliance</td>
<td>Produktrisikobewertung, Compliance-Hinweise für Anlageberatung, Interpretation von Finanzaufsichtsrichtlinien</td>
</tr>
<tr>
<td>Quantitativ & Strategien</td>
<td>Design quantitativer Strategiekonzepte, Pyramid (Pyramid/PEL)-Quantifizierung, Backtesting-Logik, Faktorkonstruktion und Tool-Aufrufe</td>
</tr>
<tr>
<td>Tool-Aufrufe</td>
<td>Kann mit Finanzdaten wie Echtzeitkursen, Datenbanken und Forschungsberichtssuche verbunden werden</td>
</tr>
</tbody>
</table>

## Technische Spezifikationen

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Projekt</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Basismodell</td>
<td>Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B Architektur, MIT-Lizenz)</td>
</tr>
<tr>
<td>Parameterumfang</td>
<td>35 Milliarden (35B) MoE-Architektur, 256 Routing-Experten + 1 gemeinsam genutzter Experte, 8 Experten pro Token aktiviert</td>
</tr>
<tr>
<td>Quantisierungsmethode</td>
<td>Verwendet selbstentwickelten MoziSmartBit Intelligent Quantisierungsalgorithmus + GGUF-Standardformat</td>
</tr>
<tr>
<td>Kontextlänge</td>
<td>256K (262.144 Tokens)</td>
</tr>
<tr>
<td>Modellgröße</td>
<td>~15,5 GB (MoziSmartBit Uncensored Version)</td>
</tr>
<tr>
<td>Mindest-VRAM-Anforderung</td>
<td>Consumer-Grafikkarten mit 20 GB VRAM oder mehr (z. B. RTX 3060 12G mit CPU-Offloading, RTX 4060 Ti 16G usw.), empfohlen 24 GB (inkl. Bild + langer Kontext)</td>
</tr>
<tr>
<td>Inferenzframework</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>Inferenzgeschwindigkeit</td>
<td>Durch Algorithmusoptimierung erreicht die AMD Radeon AI PRO R9700 Grafikkarte über 140 Token/s / AMD Ryzen AI Max+ 395 integrierte Grafik über 70 Token/s, ermöglicht lokale freie Inferenzausgabe</td>
</tr>
<tr>
<td>Entwicklungsteam</td>
<td>Chen Yumo Team</td>
</tr>
</tbody>
</table>

## Vergleich von Quantisierungsformaten und Modellgrößen

| Quantisierungsformat | Modellgröße | Genauigkeitserhaltung | Beschreibung |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (Original) | ~70 GB | 100% | Originale 16-Bit-Genauigkeit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Dieses Modell verwendet eine selbstentwickelte intelligente Quantisierungslösung** |
| Q4_K_M | ~22 GB | ~98% | GGUF-Standard 4-Bit |
| Q5_K_M | ~24,7 GB | ~99% | Höhere Genauigkeit |
| Q6_K | ~28,5 GB | ~99,5% | Fast verlustfrei |
| Q8_0 | ~36,9 GB | ~100% | Verlustfrei |
> MoziAI V3.6 verwendet die MoziSmartBit Intelligente Quantisierungslösung. Bei Erhaltung von ~99% Genauigkeit wird das MoE-Modell mit 35 Milliarden Parametern auf ca. 15,5 GB komprimiert, mit einem Kompressionsverhältnis von ~4,5x. Es vereint Inferenzqualität und Bereitstellungshürde und eignet sich besser für lokale Bereitstellung auf Consumer-Grafikkarten.

## MoziSmartBit Intelligente Quantisierungstechnologie

Traditionelle Quantisierungslösungen verwenden eine einheitliche Genauigkeit für alle Schichten. Die von Chen Yumos Team selbstentwickelte **MoziSmartBit Intelligente Quantisierung** nutzt die strukturellen Merkmale von MoE-Modellen und setzt eine intelligente differenzierte Quantisierungsstrategie ein. Dadurch wird ein optimales Gleichgewicht zwischen Größe und Genauigkeit erreicht – die Modellqualität ist höher als im Q4_K_M-Format, während die Größe nur ~15,5 GB beträgt, mit einem Kompressionsverhältnis von ~4,5x.

### Kompressionseffekt

Traditionelle Quantisierungslösungen komprimieren alle Teile des Modells einheitlich, was oft zu deutlichen Genauigkeitsverlusten führt. MoziSmartBit Intelligente Quantisierung verwendet eine selbstentwickelte intelligente Kompressionsstrategie, **die bei minimalem Genauigkeitsverlust eine drastische Größenkompression erreicht**:

- **Minimaler Quantisierungsgenauigkeitsverlust**: Trainingsgewinn > Quantisierungsverlust. Das trainierte MoziAI-35B hat im Finanzbereich einen besseren PPL als das bf16-Basismodell vor dem Training, reduziert Halluzinationen und Verwirrung ähnlicher KI-Modelle
- **Modellgröße um 4,5-fache komprimiert**: Von ~70 GB bei FP16 auf ~15,5 GB komprimiert, auch deutlich kleiner als ~22 GB bei Q4_K_M, senkt drastisch die VRAM- und Speicherhürden
- **Auf Consumer-Grafikkarten ausführbar**: Ein 35B-MoE-Großmodell, das ursprünglich High-End-Grafikkarten erforderte, kann jetzt mit 20 GB~24 GB VRAM flüssig bereitgestellt werden

### Vergleichsvorteile

**vs Q4_K_M (~22 GB)**: Größe um ca. 30% reduziert (~15,5 GB), Genauigkeit **höher** als Q4_K_M, niedrigere VRAM-Hürde, flüssige Bereitstellung auf Mittelklasse-Consumer-Grafikkarten (20 GB) möglich.

**vs Original FP16 (~70 GB)**: Größe um ca. 4,5-fache komprimiert, effektives Training + minimaler Quantisierungsgenauigkeitsverlust (Trainingsgewinn > Quantisierungsverlust), von professionellen Grafikkarten (48 GB+) auf Consumer-Grafikkarten für lokale Ausführung mit 256K langem Kontext gesenkt.

## Empfohlene Inferenzparameter

Basierend auf lokaler Laufzeitkonfiguration (AMD Radeon AI PRO R9700 32GB) sind folgende Parameter empfehlenswert:

| Parameter | Empfohlener Wert | Beschreibung |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Gleichgewicht zwischen Kreativität und Genauigkeit |
| top_p | 0.95 | Nukleus-Sampling-Schwellenwert |
| top_k | 20 | Trunkiertes Sampling |
| repeat_penalty | 1.05 | Wiederholungsbestrafung |
| presence_penalty | 0 | Keine Präsenzbestrafung |
| context_length | 262144 | 256K langer Kontext |
| batch_size | 2048 | Batch-Größe |
| ubatch_size | 512 | Mikro-Batch-Größe |
| flash_attention | auto | Automatische Flash Attention |
| kv_cache | q4_0 | KV-Cache-Quantisierung (vereinheitlicht kv-unified) |
| poll | 0 | Kein GPU-Polling im Leerlauf, energiesparend und niedrige Latenz |
| reasoning | on | Denkkette aktivieren |
| reasoning_budget | 400 | Anzahl der Inferenzbudget-Token |
| reasoning_format | deepseek-legacy | Inferenzformat |
| samplers | top_k;top_p;temperature;typ_p | Sampler-Reihenfolge |
### Empfehlungen für verschiedene VRAM-Konfigurationen

Da sich die Grafikkartenkonfigurationen der Benutzer stark unterscheiden, finden Sie hier empfohlene Parameter für verschiedene VRAM-Größen (alle für die MoziSmartBit-Version):

| VRAM | Empfohlene Kontextlänge | KV-Cache | Bildunterstützung | Beschreibung |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | Unterstützt | Modell + Bild insgesamt ~16,4 GB, Praxistest: 128K + Bild belegen nur ~19,5 GB VRAM |
| 24 GB | 256K Vollausstattung | q4_0 | Perfekt unterstützt | Bild + 256K langer Kontext, nur ~20,4 GB VRAM, ~3,6 GB VRAM-Reserve |
| 32 GB+ | 256K Vollausstattung | q4_0 | Perfekt unterstützt | Bild + 256K langer Kontext, ausreichend VRAM-Reserve ~10 GB, stärkste Konfiguration |
**NVIDIA-Grafikkarten Referenztabelle**

| VRAM | Grafikkartenmodell |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD-Grafikkarten Referenztabelle**

| VRAM | Grafikkartenmodell |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel-Grafikkarten Referenztabelle**

| VRAM | Grafikkartenmodell |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (erfordert CPU-Offloading) |
**Integrierte Grafik mit gemeinsamem CPU-Speicher Referenztabelle**

| VRAM | Prozessormodell |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S integrierte Grafik) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |
> 💡 **Hinweis**: Solange der VRAM die oben genannten Anforderungen erfüllt, kann es verwendet werden – keine Beschränkung auf Marke oder Modell. Unterstützt NVIDIA / AMD / Intel dedizierte Grafikkarten sowie integrierte Grafik/CPU mit 128 GB einheitlichem Speicher.
>
> 💡 **Hinweis**: Je länger der Kontext, desto mehr VRAM wird belegt. Wenn der VRAM nicht ausreicht (OOM), reduzieren Sie schrittweise den Wert des Parameters `-c`. Mit dem Parameter `--fit on` kann llama.cpp die Anzahl der Schichten automatisch an den VRAM anpassen.

### Ollama-Bereitstellung

```bash
# Modelfile erstellen
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Erstellen und ausführen
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan Bereitstellung

Suchen Sie direkt in LM Studio oder Jan nach `moziAI-35B` und wählen Sie die Quantisierungsversion zum Download aus.

## Benchmark-Bewertung

moziAI-13.7-35B-A3B basiert auf dem **Ornith-1.0-35B** (deepreinforce-ai)-Basismodell und wurde feinabgestimmt. Aufbauend auf den exzellenten Agent-Coding-Fähigkeiten des Basismodells hat MoziAI eine **tiefe Optimierung im Finanzbereich** hinzugefügt und zeigt bessere Leistung in Szenarien wie Finanz-Q&A, quantitative Programmierung und Tool-Aufrufe. Die allgemeinen Fähigkeiten stimmen mit dem Ornith-1.0-35B-Basismodell überein.

| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmierung** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Denken** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Agentisch** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |
**Terminal-Bench 2.1 (Terminus-2)**: Bewertet mit dem Harbor/Terminus-2-Framework, Konfiguration `parser=json`, `temperature=1.0`, `top_p=1.0`, 128K-Kontextfenster. Jeder Lauf hat ein Timeout von 4 Stunden, 32 Kerne, 48 GB RAM, Ergebnis ist der Durchschnitt von 5 Läufen.  
**Terminal-Bench 2.1 (Claude Code)**: Bewertet mit Claude Code 2.1.126, Konfiguration `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Ergebnis ist der Durchschnitt von 5 Läufen.  
**SWE-bench Verified, Pro und Multilingual**: Bewertet mit dem OpenHands-Framework, Konfiguration `temp=1.0`, `top_p=0.95`, 256K-Kontextfenster.  
**NL2Repo**: Konfiguration `temperature=1.0`, `top_p=1.0`, 400K-Kontext, 48K-Ausgabe.  

> MoziAI-35B erbt vollständig die exzellenten Agent-Coding-Fähigkeiten von Ornith-1.0-35B. Der Kernunterschied von MoziAI liegt in der **tiefen Optimierung im Finanzbereich**. In Szenarien wie Finanzberichtsanalyse, quantitativen Strategien, Risikomanagement & Compliance und Agent-Tool-Aufrufen ist die Leistung deutlich besser als bei allgemeinen Modellen.

## SEO-Schlüsselwörter

Finanz-KI-Großmodell, KI-Großmodell, lokales Open-Source-Modell, Edge-Modell, quantitative Programmierung, MoziSmartBit, intelligente Quantisierung, GGUF-Quantisierung, MoE-Modell, lokales Open-Source-Großmodell, lokale Bereitstellung, Finanz-KI, Tool-Aufrufe, Agent, llama.cpp, Ollama, GGUF, Uncensored (ohne Zensur), keine Überprüfung, Überprüfungsfrei, freie Ausgabe, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B, Finanzvertikale, Open-Source-Modell.

## Lizenz (wichtig)

Dieses Modell verwendet eine **benutzerdefinierte restriktive Lizenz**, die genauen Bedingungen lauten wie folgt:

✅ **Erlaubt**

- Kostenlose kommerzielle Nutzung: Kann kostenlos in Ihre kommerziellen Produkte oder Dienstleistungen integriert werden
- Kopieren und Verteilen: Kann unverändert kopiert, heruntergeladen und verteilt werden

Die detaillierten Lizenzbestimmungen finden Sie in der Datei [LICENSE](../LICENSE).

## Haftungsausschluss

Dieses Modell wird "wie besehen" bereitgestellt, ohne jegliche Garantie. Modellausgaben dienen nur als Referenz und stellen keine Anlageberatung dar. Der Nutzer trägt das Risiko der Nutzung selbst.

## Kontakt

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.