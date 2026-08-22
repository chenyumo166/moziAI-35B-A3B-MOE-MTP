---
language:
- nl
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

# MoziAI-V3.6-35B-A3B-MOE - Gratis lokaal deploybaar compact krachtig multimodaal AI

Language / Taalkeuze  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | Nederlands | [Italiano](README.it.md) | [Русский](README.ru.md)

## Modeloverzicht

MoziAI-35B-A3B-MOE is een groot lokaal open-source multimodaal AI-taalmodel ontwikkeld door het team van de Chinese financiële invloedspersoon Chen Yumo (geoptimaliseerd voor de financiële sector, ondersteunt visie, tool calling, complexe lange taken, lokale implementatie op consumenten-GPU's). Het is fijn-afgestemd/gedistilleerd vanuit het basismodel Ornith-1.0-35B-A3B (**Qwen3.5-35B-A3B/Qwen3.6-35B-A3B** architectuur, MIT-licentie).

De missie van ons team is om krachtige lokale AI-grote modellen toegankelijk te maken voor huishoudens en het MKB, waardoor de noodzaak van dure AI-hardwarekosten of cloud API-kosten wordt geëlimineerd. Door middel van de zelf ontwikkelde **MoziSmartBit Intelligente Kwantisatie**-techniek wordt het 350 miljard parameter MoE-model gecomprimeerd tot ongeveer **15,5 GB**, waarbij een optimaal evenwicht tussen modelprecisie en grootte wordt bereikt, met ~99% van de FP16-precisiekwaliteit. Hoewel het model in totaal 350 miljard parameters heeft, gebruikt het MOE sparse expert-technologie die slechts 3 miljard parameters per token activeert en ondersteunt MTP speculatieve decodering voor versnelde inferentie. Praktische tests tonen aan dat het lokaal kan worden geïmplementeerd op een consumenten-GPU met 20 GB VRAM en een inferentiesnelheid van 140+ tokens/s behaalt, waardoor veel betaalde cloud AI-grote modellen worden overtroffen.

Naast het behouden van algemene AI-mogelijkheden, richt dit model zich op de optimalisatie van kernmogelijkheden van grote AI-modellen in het financiële verticale domein, inclusief financiële Q&A, kwantitatieve programmering, algemene programmering, tool calling, en het succespercentage van 256K complexe lange context taken. Het kan gratis lokaal worden geïmplementeerd op consumenten-GPU's, bespaart aanzienlijke cloud-tokenkosten, bereikt 7X24 token-vrijheid waarborgt lokale gegevensprivacy en -beveiliging.

**Releasedatum: 2026-08-20** | **Versie: V3.6**

## Model download

Vanwege de grote modelgrootte (~15,5 GB) worden de gewichten op verschillende communityplatforms gehost:

| Platform | URL |
|----------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |


> 💡 **LM Studio**: U kunt het model ook direct zoeken en downloaden in [LM Studio](https://lmstudio.ai). Zoek naar `moziAI` en klik op Download.
> 💡 **Downloadtip**: Klik op de link hierboven om naar de HuggingFace-repository te gaan, ga vervolgens naar het tabblad **"Files and versions"** om alle bestanden in de V3.6-map te downloaden (hoofdmodel, visieprojectie, chat-sjabloon). Zorg ervoor dat alle drie de bestanden in dezelfde map staan.

### ⚠️ Belangrijk: voor visie is een mmproj-bestand vereist

Dit model ondersteunt multimodale visie. Het **visieprojectiebestand (mmproj)** is opgenomen in de versiemap:

- **Visiebestand**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16-precisie)
- **Locatie**: Plaats het in dezelfde versiemap als het GGUF-modelbestand
- **Laden**: Gebruik de vlag `--mmproj` bij het starten van llama-server

> Zonder het visiebestand verliest het model **beeldvermogend vermogen** en behoudt het alleen tekstuele conversatie.

### ⚠️ Belangrijk: chat-sjabloonbestand moet worden geladen

Dit model gebruikt een aangepast chatsjabloon. **Zonder dit treden dialoogopmaakfouten, verbroken redeneringsketens en verminderde antwoordkwaliteit op.** Het sjabloonbestand is opgenomen in de versiemap:

- **Sjabloonbestand**: `moziAI-V3.6-35B-chat-template.jinja` (enkele KB, jinja-formaat)
- **Locatie**: Plaats het in dezelfde versiemap als het GGUF-modelbestand
- **Laden**: Gebruik de parameter `--chat-template-file` bij het starten van llama-server

> Zonder het chatsjabloon herkent het model mogelijk systeemprompts, gebruikersberichten en denkblokken niet correct, wat resulteert in onleesbare uitvoer of verminderd redeneervermogen.

### llama.cpp opstartopdracht (Aanbevolen configuratie voor 20GB+ GPU's met 256K context)

> Opmerking: Als de VRAM onder de 20 GB ligt, verlaag dan de contextgrootteparameter `-c 262144`.

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

## Snelle Start

### 1. Modelbestanden downloaden

Download alle bestanden in de V3.6-map van HuggingFace / ModelScope:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Hoofdmodel (vereist)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Visieprojectie (optioneel)
└── moziAI-V3.6-35B-chat-template.jinja                  # Chat-sjabloon (VEREIST! Zonder dit treden dialoogopmaakfouten op)
```

> ⚠️ **Het chatsjabloon is een verplicht bestand**, niet optioneel. Dit model heeft een aangepast dialoogformaat (inclusief redeneringsketen / denkblokken). Zonder het sjabloon is de modeluitvoer onleesbaar en werkt het redeneren niet. Download het en laad het bij opstarten.

### 2. Inferentieservice starten

Voor de volledige opstartopdracht met aanbevolen configuratie, zie de sectie **llama.cpp opstartopdracht** hierboven.

Minimale opstart (alleen kernparameters):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Voeg `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` toe voor visie.

### 3. Gebruik starten

Open `http://localhost:8080` in uw browser om te beginnen met chatten.

### Directorystructuur

```
moziAI-35B/
├── README.md              # Chinese versie
├── README.nl.md           # Dit bestand (Nederlands)
├── LICENSE                # Licentie
├── V3.6/                  # V3.6-versie (zelfstandig)
�?  ├── RELEASE_NOTES.md                       # Release-opmerkingen
�?  ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Hoofdmodel
�?  ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Visieprojectie
�?  └── moziAI-V3.6-35B-chat-template.jinja   # Chat-sjabloon
```

## Modelfuncties

<br />

- **MoziSmartBit Intelligente Kwantisatie**: Zelf ontwikkelde slimme kwantisatie, beste balans tussen precisie en grootte, bijna verliesloos gecomprimeerd tot ongeveer **15,5 GB**
- **Complexe Lange Taken Capaciteit**: Getraind met een intelligent cyclisch mechanisme waarmee de agent automatisch taken plant, vastgelopen punten verwerkt en zelfreflecteert, waardoor automatische uitvoering en zelfaanpassing voor complexe taken mogelijk wordt, waardoor gebruikers worden verlost van de moeite om constant prompts te optimaliseren.
- **Klein Model, Groot Vermogen**: Overtreft andere modellen met minder dan 350 miljard parameters op complexe taken, overtreft zelfs sommige grotere modellen met meerdere keren meer parameters.
- **MOE+MTP Snelheidsvoordeel**: Hoewel het model in totaal 350 miljard parameters heeft, worden slechts 3 miljard parameters (8+1 experts) per token geactiveerd, wat resulteert in een snellere inferentiesnelheid. Perfect voor lokale implementatie op consumenten-GPU's met 20 GB of 24 GB VRAM, levert een inferentiesnelheid van 140+ tokens/s.
- **Financieel Vertaaldomein Focus**: Diepe optimalisatie voor financiële Q&A, kwantitatieve programmering en tool calling
- **Consumentengrade Implementatie**: Implementeerbaar op consumenten-GPU's met 20GB of 24GB+ VRAM, ondersteunt 256K lange context
- **Meertalige Ondersteuning**: 201 talen en dialecten, met verbeterde Chinese vaardigheden, dekkend Chinees/Engels/Japans/Koreaans/Duits/Frans/Spaans/Portugees en meer
- **Algemene Programmering**: Full-stack ontwikkeling, code debugging, architectuurontwerp, scriptwriting, dekkend Python/JS/TS/Go/Rust en andere mainstream talen
- **Artikelschrijven**: Hoogwaardig meergenre schrijven inclusief onderzoeksrapp

## Ongecensureerde Voordelen

Dit model erft de **Uncensored**-functie van het Ornith-1.0-35B basismodel, met de volgende voordelen:

| Voordeel | Beschrijving |
|----------|-------------|
| **Geen Censuur** | Weigert geen enkel onderwerp, inclusief gevoelige of controversiële inhoud |
| **Vrije Output** | Niet beperkt door beveiligingsbeleid, kan elk type respons genereren |
| **Volledige Informatie** | Biedt ongefilterde volledige informatie, geschikt voor onderzoek en analyse |
| **Lokale Privacy** | Lokale deployment betekent dat gegevens volledig privé zijn en vrij van cloud-censuur |

> **Gebruiksscenarios**: Academisch onderzoek, diepe analyse, vrije discussie, onbeperkte AI-gesprekken.
> **Opmerking**: Dit is een lokaal gedeployeerd model, de outputinhoud wordt volledig beheerd door de gebruiker, geen inhoudsmoderatieverantwoordelijkheid.

## Kernmogelijkheden

| Vaardigheidsgebied | Beschrijving |
|-------------------|-------------|
| Marktanalyse | Macro-/micro-economische interpretatie, A-share/HK/US-aandelen/grondstoffen/crypto-marktlogica |
| Financiële Rapporten | Interpretatie van belangrijke financiële indicatoren, samenvatting van onderzoeksrapporten, waardering & winstprognose-assistentie |
| Risico & Compliance | Productrisicobeoordeling, investeringsadvies-compliance, interpretatie van financiële regelgevingsbeleid |
| Kwant & Strategie | Kwantitatieve strategieontwerp, Pyramid (PEL) kwantisatie, backtesting-logica, factorconstructie en tool calling |
| Tool Calling | Integratie met realtime koersen, databases, onderzoeksrapportenophaling en andere financiële gegevensbronnen |

## Technische Specificaties

| Item | Specificatie |
|------|-------------|
| Basismodel | Ornith-1.0-35B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT-licentie) |
| Parameters | 35B MoE (256 gerouteerde experts + 1 gedeelde expert, 8 actief per token) |
| Kwantisatie | Zelf ontwikkelde MoziSmartBit Intelligente Kwantisatie + GGUF standaardformaat |
| Contextlengte | 256K (262.144 tokens) |
| Modelgrootte | ~15,5 GB (MoziSmartBit Uncensored versie) |
| Min. VRAM | Consumenten-GPU's met 20GB+ VRAM (bijv. RTX 4060 Ti 16G met CPU offload), 24 GB aanbevolen (met visie + lange context) |
| Inferentieframework | llama.cpp / Ollama / LM Studio / Jan |
| Inferencesnelheid | Algoritme-geoptimaliseerd: 140+ token/s op AMD R700 GPU's, 70+ token/s op AMD MAX+395 CPU iGPU, lokale token-vrijheid |
| Team | Chen Yumo Team |

## Kwantisatieformaat & Modelgrootte Vergelijking

| Kwant-formaat | Modelgrootte | Precisie | Opmerkingen |
|---------------|-------------|----------|-------------|
| **FP16 (origineel)** | ~70 GB | 100% | Origineel 16bit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Gebruikt door MoziAI, optimale kwantisatieoplossing** |
| Q4_K_M | ~22 GB | ~98% | GGUF standaard 4bit |
| Q5_K_M | ~24,7 GB | ~99% | Hogere kwaliteit |
| Q6_K | ~28,5 GB | ~99,5% | Bijna verliesvrij |
| Q8_0 | ~36,9 GB | ~100% | Verliesvrij |

> MoziAI V3.6 gebruikt MoziSmartBit Intelligente Kwantisatie, handhaaft ~99% precisie terwijl het 35B-parameter MoE-model wordt gecomprimeerd tot ~15,5 GB (~4,5x compressieverhouding), waarbij inferentiekwaliteit en deployment-toegankelijkheid voor consumenten-GPU's in evenwicht worden gebracht.

## MoziSmartBit Intelligente Kwantisatie

Traditionele kwantisatie gebruikt uniforme precisie voor alle lagen. **MoziSmartBit Intelligente Kwantisatie** past gedifferentieerde kwantiseringsstrategieën toe voor optimale grootte-precisiebalans.

### Compressie-effect

Traditionele kwantisatie comprimeert alle delen van het model uniform, wat vaak leidt tot aanzienlijk precisieverlies. MoziSmartBit Intelligente Kwantisatie gebruikt een zelf ontwikkelde intelligente compressiestrategie die **aanzienlijke groottereductie bereikt met minimaal precisieverlies**:

- **Minimaal Kwantisatieverlies**: Trainingswinst > kwantisatieverlies. Het getrainde MoziAI-35B bereikt betere PPL op financieel domeintekst dan het pre-training bf16 basismodel, waardoor hallucinatie en perplexiteit worden verminderd in vergelijking met vergelijkbare AI-modellen
- **~4,5x Groottereductie**: Gecomprimeerd van ~70 GB (FP16) tot ~15,5 GB, ook aanzienlijk kleiner dan Q4_K_M (~21 GB), waardoor VRAM- en opslagvereisten aanzienlijk worden verlaagd
- **Consumenten-GPU Vriendelijk**: Een 35B MoE-model dat voorheen�?end GPU's vereiste, kan nu soepel draaien op 20GB~24GB VRAM

### Vergelijkende Voordelen

**vs Q4_K_M (~22 GB)**: ~30% kleiner (~15,5 GB), met precisie **hoger** dan Q4_K_M, lagere VRAM-drempel �?draait soepel op mid-range consumenten-GPU's (24GB).

**vs FP16 origineel (~70 GB)**: ~4,5x compressie, trainings-effectief + minimaal kwantisatieverlies (trainingswinst > kwantisatieverlies), waardoor lokale 256K context-deployment op consumenten-GPU's mogelijk wordt in plaats van professioneel materiaal.

## Aanbevolen Inferentieparameters

Gebaseerd op lokale productieconfiguratie (AMD Radeon AI PRO R9700 32GB):

| Parameter | Waarde | Beschrijving |
|-----------|--------|-------------|
| temperature | 0,6 | Balans creativiteit vs nauwkeurigheid |
| top_p | 0,95 | Nucleus sampling drempel |
| top_k | 20 | Truncatie sampling (V3.6 geoptimaliseerd) |
| repeat_penalty | 1,05 | Herhalingsstraf |
| presence_penalty | 0 | Geen aanwezigheidsstraf |
| context_length | 262144 | 256K lange context |
| batch_size | 2048 | Batchgrootte |
| ubatch_size | 512 | Micro-batchgrootte |
| flash_attention | auto | Automatische Flash Attention |
| kv_cache | q4_0 | KV cache-kwantisatie (kv-unified) |
| poll | 0 | Geen GPU-polling bij inactiviteit, energiezuinig |
| reasoning | on | Redeneerketens inschakelen (chain of thought) |
| reasoning_budget | 400 | Redeneerbudget in tokens |
| reasoning_format | deepseek-legacy | Redeneerformaat |
| samplers | top_k;top_p;temperature;typ_p | Sampler-volgorde |

### VRAM-configuratieaanbevelingen

Aangezien de GPU-configuraties van gebruikers sterk uiteenlopen, volgen hier aanbevolen parameters voor verschillende VRAM-groottes (allemaal voor de MoziSmartBit-versie):

| VRAM | Aanbevolen Context | KV Cache | Visieondersteuning | Opmerkingen |
|------|-------------------|----------|-------------------|-------------|
| 20 GB | 128K | q4_0 | Ondersteund | Model+visie ~16,4GB, praktijktest toont 200K+visie gebruikt ~19,5GB VRAM |
| 24 GB | 256K volledig | q4_0 | Volledige ondersteuning | Visie+256K lange context, gebruikt ~20,4GB VRAM, ~3,6GB marge |
| 32 GB+ | 256K volledig | q4_0 | Volledige ondersteuning | Visie+256K lange context, voldoende marge ~10GB, beste configuratie |

**NVIDIA**

| VRAM | GPU-model |
|------|-----------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD**

| VRAM | GPU-model |
|------|-----------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel**

| VRAM | GPU-model |
|------|-----------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (vereist CPU offload) |

**Gedeeld Geheugen iGPU's**

| VRAM | Processor |
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |

> 💡 **Tip**: Zolang uw VRAM aan de bovenstaande vereisten voldoet, werkt het. Geen merk- of modelbeperkingen. Ondersteunt NVIDIA / AMD / Intel discrete GPU's, en ook 128GB unified memory iGPU's zoals hierboven vermeld.

> 💡 **Tip**: Langere context gebruikt meer VRAM. Als u OOM (out of memory) tegenkomt, verlaag dan geleidelijk de `-c`-waarde. Gebruik `--fit on` zodat llama.cpp automatisch lagen aanpast om bij uw VRAM te passen.

### Ollama Deployment

```bash
# Maak Modelfile aan
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Bouw en start
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan Deployment

Zoek `moziAI-35B` in LM Studio of Jan, download de MoziSmartBit-kwantversie.

## Benchmarkbeoordeling

MoziAI is fijn-afgestemd vanuit **deepreinforce-ai/Ornith-1.0-35B**. MoziAI is geoptimaliseerd voor financiële vertaaldomeinen bovenop het basismodel en levert uitstekende prestaties in financiële Q&A, kwantitatieve programmering en tool calling-scenario's. MoziAI-35B algemene mogelijkheden komen overeen met het Ornith-1.0-35B basismodel.

| Benchmark | MoziAI-35B (dit model) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Beschrijving |
|-----------|----------------------|-------------|------------|------------|-------------|-------------|
| Terminal-Bench 2.1 | 64,2 | 59,3 | 42,1 | - | 41,4 | Autonome terminal-coding |
| Terminal-Bench (Claude Code) | 62,8 | 59,3 | - | - | 38,9 | Claude Code-coding |
| SWE-bench Verified | 75,6 | 77,2 | 52,0 | - | 70,0 | Software engineering in de praktijk |
| SWE-bench Pro | 50,4 | 53,5 | 35,7 | - | 44,6 | Complexe software engineering |
| SWE-bench Multilingual | 69,3 | 71,3 | - | - | 60,3 | Meertalige codering |
| NL2Repo | 34,6 | 36,2 | 15,5 | - | 20,5 | Natuurlijke taal naar repository |
| LiveCodeBench v6 | 63,3 | 83,9 | 80,0 | 77,1 | - | Competitief programmeren |
| GPQA Diamond | 88,4 | 87,8 | 84,3 | 82,3 | - | Wetenschappelijk redeneren |
| AIME 2026 Math | 93,3 | 94,1 | 89,2 | 88,3 | - | Wiskundig redeneren |

> MoziAI-35B algemene benchmarkscores komen overeen met het Ornith-1.0-35B basismodel. Het financiële vertaaldomein is de kernoptimalisatierichting van MoziAI, met aanzienlijk betere prestaties dan algemene modellen in scenario's zoals financiële rapportanalyse, kwantitatieve strategie, risico & compliance en agent-tool calling. Gemma4- en Qwen3.6-gegevens afkomstig van officiële openbare resultaten.

## SEO Trefwoorden

financieel AI LLM, lokaal open-source model, eindapparaatmodel, kwant programmering, MoziSmartBit, intelligente kwantisatie, GGUF kwantisatie, MoE-model, lokaal open-source LLM, lokale deployment, financieel AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, geen censuur, vrije output, onbeperkt, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5, Qwen3.6, financieel vertaaldomein, open-source model

## Licentie (Belangrijk)

Dit model gebruikt een **Aangepaste Beperkte Licentie**:

### �?Toegestaan
- **Vrij Commercieel Gebruik**: Vrij te integreren in commerciële producten
- **Kopiëren & Verspreiden**: Kan gekopieerd, gedownload en gedeeld worden

### �?Verboden
- **Afgeleide Werken**: Geen modificatie, vertaling, aanpassing, samenvoeging of fijne afstemming van het model of enig deel ervan
- **Doorverkoop**: Geen verkoop van het model alleen of als onderdeel van een product
- **Herlicentiëring**: Geen sublicenties verlenen

### 📋 Vereisten
- Origineel copyrightbericht behouden moet worden
- Naamsvermelding: moziAI-35B

> Zie [LICENSE](./LICENSE) voor de volledige voorwaarden.

## Disclaimer

Geleverd "zoals het is" zonder garantie. Modeloutput is uitsluitend ter referentie, geen investeringsadvies. Gebruikers dragen alle risico's.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. Alle rechten voorbehouden.
