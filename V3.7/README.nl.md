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



# MoziAI-V3.7-35B-A3B-MOE - Gratis lokaal deploybaar compact krachtig multimodaal AI



[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | Nederlands | [Italiano](README.it.md) | [Русский](README.ru.md)



## Modeloverzicht



MoziAI-35B-A3B-MOE is een lokaal open-source financieel AI multimodaal LLM (ondersteunt visie en tool calling) ontwikkeld door het team van de Chinese financiële invloedspersoon Chen Yumo. moziAI-35B is gebaseerd op het open-source basismodel Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B-architectuur, MIT-licentie), met de zelfontwikkelde: (financiële gegevens + financiële domeincapaciteiten + trainingsmethoden + Seven-Dimensional Thinking-framework + agent-LOOP-mechanisme + hybride kwantiseringsalgoritme MoziSmartBit) van het Chen Yumo-team. Door de zelfontwikkelde MoziSmartBit intelligente kwantiseringstechnologie wordt het MoE-model met 35 miljard parameters gecomprimeerd tot ongeveer 15,5 GB, wat 6,5 GB (ongeveer 30%) kleiner is dan conventionele Q4_K_M-kwantiseringsmodellen van ongeveer 22+ GB; het optimale evenwicht tussen precisie en grootte wordt bereikt, met bijna verliesvrije ≈99% FP16-precisiekwaliteit.



Naast het behouden van de algemene AI-mogelijkheden, verbetert dit model: financiële verticale domeintoepassingen, financiële Q&A, kwantitatieve programmering, tool calling en algemene programmering, evenals de zeven-dimensionale denkvaardigheid van het model, het LOOP-mechanisme en compatibiliteit met verschillende agentplatforms.



De modelontwikkelaar Chen Yumo gebruikt dit model regelmatig voor lokale financiële gegevensanalyse, kwantitatieve strategie-ontwikkeling, marktonderzoek, artikelen schrijven, algemene projectvoortgang, algemene programmering en 128K context-taken via openclaw/hermes. Het kan lokaal worden gedeployeerd op consumentengrade GPUs, waardoor aanzienlijke cloud-tokenkosten worden bespaard en 7X24 token-vrijheid wordt gerealiseerd terwijl de lokale gegevensprivacy en -beveiliging worden gewaarborgd.



Ondersteunt llama.cpp, Ollama, LM Studio en andere mainstream inferentieframeworks.



**Releasedatum: 2026-08-21** | **Versie: V3.7**



## Modelfuncties



- **Financieel Vertaaldomein Focus**: Diepe optimalisatie voor financiële Q&A, kwantitatieve programmering en tool calling

- **MoziSmartBit Intelligente Kwantisatie**: Zelf ontwikkelde slimme kwantisatie, beste balans tussen precisie en grootte, gecomprimeerd tot ongeveer **15,5 GB**

- **Consumentengrade Deployment**: Deployable op consumenten-GPU's met 20GB of 24GB+ VRAM, ondersteunt 256K lange context

- **Meertalige Ondersteuning**: 201 talen en dialecten, met verbeterde Chinese vaardigheden, dekkend Engels/Japans/Koreaans/Duits/Frans/Spaans/Portugees en meer

- **Algemene Programmering**: Full-stack ontwikkeling, code debugging, architectuurontwerp, scriptwriting, dekkend Python/JS/TS/Go/Rust en andere mainstream talen

- **Artikelenschrijven**: Hoogwaardig meergenre schrijven inclusief onderzoeksrapporten, analyseartikelen, technische documentatie, creatieve content

- **Visiebegrip**: Ondersteunt multimodale visie, lokale screenshot-invoer, afbeeldingsbegrip

- **Ongecensureerde Vrije Output**: Geen inhoudscensuur, vrij discussiëren over elk onderwerp zonder beveiligingsbeperkingen

- **Verbeten Redeneren**: Chain-of-thought training voor verbeterde redeneerkwaliteit

- **Multi-Framework Ondersteuning**: Compatibel met llama.cpp, Ollama, LM Studio, Jan

- **Multi-Agent Platform Ondersteuning**: Diepe integratie met OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex en andere mainstream AI IDE's en Agent-frameworks, ondersteunt native tool calling en multi-turn taakorkestratie, direct gebruiksklaar



## Ongecensureerde Voordelen



Dit model erft de **Uncensored**-functie van het Ornith-1.5-35B-A3B basismodel, met de volgende voordelen:



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
| Basismodel | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT-licentie) |
| Parameters | 35B MoE (256 gerouteerde experts + 1 gedeelde expert, 8 actief per token) |
| Kwantisatie | Zelf ontwikkelde MoziSmartBit Intelligente Kwantisatie + GGUF standaardformaat |
| Contextlengte | 256K (262.144 tokens) |
| Modelgrootte | ~15,5 GB (MoziSmartBit Uncensored versie) |
| Min. VRAM | Consumenten-GPU's met 20GB+ VRAM (bijv. RTX 4060 Ti 16G met CPU offload), 24 GB aanbevolen (met visie + lange context) |
| Inferentieframework | llama.cpp / Ollama / LM Studio / Jan |
| Inferencesnelheid | Algoritme-geoptimaliseerd: 140+ token/s op AMD R9700 GPU's, 70+ token/s op AMD MAX+395 CPU iGPU, lokale token-vrijheid |
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
> MoziAI V3.7 gebruikt MoziSmartBit Intelligente Kwantisatie, handhaaft ~99% precisie terwijl het 35B-parameter MoE-model wordt gecomprimeerd tot ~15,5 GB (~4,5x compressieverhouding), waarbij inferentiekwaliteit en deployment-toegankelijkheid voor consumenten-GPU's in evenwicht worden gebracht.



## MoziSmartBit Intelligente Kwantisatie



Traditionele kwantisatie gebruikt uniforme precisie voor alle lagen. **MoziSmartBit Intelligente Kwantisatie** past gedifferentieerde kwantiseringsstrategieën toe voor optimale grootte-precisiebalans.



### Compressie-effect



Traditionele kwantisatie comprimeert alle delen van het model uniform, wat vaak leidt tot aanzienlijk precisieverlies. MoziSmartBit Intelligente Kwantisatie gebruikt een zelf ontwikkelde intelligente compressiestrategie die **aanzienlijke groottereductie bereikt met minimaal precisieverlies**:



- **Minimaal Kwantisatieverlies**: Trainingswinst > kwantisatieverlies. Het getrainde MoziAI-35B bereikt betere PPL op financieel domeintekst dan het pre-training bf16 basismodel, waardoor hallucinatie en perplexiteit worden verminderd in vergelijking met vergelijkbare AI-modellen

- **~4,5x Groottereductie**: Gecomprimeerd van ~70 GB (FP16) tot ~15,5 GB, ook aanzienlijk kleiner dan Q4_K_M (~21 GB), waardoor VRAM- en opslagvereisten aanzienlijk worden verlaagd

- **Consumenten-GPU Vriendelijk**: Een 35B MoE-model dat voorheen durend GPU's vereiste, kan nu soepel draaien op 20GB~24GB VRAM



### Vergelijkende Voordelen



**vs Q4_K_M (~22 GB)**: ~30% kleiner (~15,5 GB), met precisie **hoger** dan Q4_K_M, lagere VRAM-drempel — draait soepel op mid-range consumenten-GPU's (24GB).



**vs FP16 origineel (~70 GB)**: ~4,5x compressie, trainings-effectief + minimaal kwantisatieverlies (trainingswinst > kwantisatieverlies), waardoor lokale 128K context-deployment op consumenten-GPU's mogelijk wordt in plaats van professioneel materiaal.



## Aanbevolen Inferentieparameters



Gebaseerd op lokale productieconfiguratie (AMD Radeon AI PRO R9700 32GB):



| Parameter | Waarde | Beschrijving |
|-----------|--------|-------------|
| temperature | 0,6 | Balans creativiteit vs nauwkeurigheid |
| top_p | 0,95 | Nucleus sampling drempel |
| top_k | 20 | Truncatie sampling (V3.7 geoptimaliseerd) |
| repeat_penalty | 1,05 | Herhalingsstraf |
| presence_penalty | 0 | Geen aanwezigheidsstraf |
| context_length | 131072 | 256K lange context |
| batch_size | 2048 | Batchgrootte |
| ubatch_size | 512 | Micro-batchgrootte |
| flash_attention | auto | Automatische Flash Attention |
| kv_cache | q4_0 | KV cache-kwantisatie (kv-unified) |
| poll | 0 | Geen GPU-polling bij inactiviteit, energiezuinig |
| reasoning | on | Redeneerketens inschakelen (chain of thought) |
| reasoning_budget | 400 | Redeneerbudget in tokens |
| reasoning_format | deepseek-legacy | Redeneerformaat |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | Sampler-volgorde |
### llama.cpp Startcommando



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 131072 -ngl 99 -t 28 \

  --batch-size 2048 --ubatch-size 512 \

  --flash-attn auto \

  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \

  --spec-default \
  --poll 0 --reasoning on --reasoning-budget 1000 \

  --host 0.0.0.0 --port 8080 \

  --temp 0.6 --top-p 0.95 --top-k 20

```



### VRAM-configuratieaanbevelingen



Aangezien de GPU-configuraties van gebruikers sterk uiteenlopen, volgen hier aanbevolen parameters voor verschillende VRAM-groottes (allemaal voor de MoziSmartBit-versie):



| VRAM | Aanbevolen Context | KV Cache | Visieondersteuning | Opmerkingen |
|------|-------------------|----------|-------------------|-------------|
| 20 GB | 150K | q4_0 | Ondersteund | Model+visie ~16,4GB, praktijktest toont 200K+visie gebruikt ~19,5GB VRAM |
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

FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf



PARAMETER temperature 0.6

PARAMETER top_p 0.95

PARAMETER top_k 20

PARAMETER num_ctx 131072

PARAMETER num_gpu 99



# Bouw en start

ollama create moziAI-35B -f Modelfile

ollama run moziAI-35B

```



### LM Studio / Jan Deployment



Zoek `moziAI-35B` in LM Studio of Jan, download de MoziSmartBit-kwantversie.



## Benchmarkbeoordeling



MoziAI is fijn-afgestemd vanuit **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI is geoptimaliseerd voor financiële vertaaldomeinen bovenop het basismodel en levert uitstekende prestaties in financiële Q&A, kwantitatieve programmering en tool calling-scenario's. MoziAI-35B algemene mogelijkheden komen overeen met het Ornith-1.5-35B-A3B basismodel.



| Benchmark | moziAI-35B-V3.7 | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmeren** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Redeneren** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Agentisch** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |
> MoziAI-35B algemene benchmarkscores komen overeen met het Ornith-1.5-35B-A3B basismodel. Het financiële vertaaldomein is de kernoptimalisatierichting van MoziAI, met aanzienlijk betere prestaties dan algemene modellen in scenario's zoals financiële rapportanalyse, kwantitatieve strategie, risico & compliance en agent-tool calling. Gemma4- en Qwen3.6-gegevens afkomstig van officiële openbare resultaten.



## Model Download



Vanwege de grote modelgrootte (~15,5 GB) worden gewichten gehost op meerdere gemeenschapsplatforms:



| Platform | URL |
|----------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
> 💡 **LM Studio**: U kunt het model ook direct zoeken en downloaden in [LM Studio](https://lmstudio.ai). Zoek naar `moziAI` en klik op Download.

> 💡 **Downloadtip**: Klik op de bovenstaande link naar de HuggingFace-repository, ga vervolgens naar het tabblad **"Files and versions"** om alle bestanden onder de V3.7-map te downloaden (hoofdmodel, visieprojectie, chatsjabloon). Zorg ervoor dat alle drie de bestanden in dezelfde map worden geplaatst.



### ⚠️ Belangrijk: Visiemogelijkheid Vereist mmproj-bestand



Dit model ondersteunt multimodale visie. Het **visieprojectiebestand (mmproj)** is opgenomen in de versiemap:



- **Visiebestand**: `mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf` (~903 MB, BF16-precisie)

- **Plaatsing**: Dezelfde versiemap als het GGUF-modelfbestand

- **Laden**: Laad met de `--mmproj`-vlag bij het starten van llama-server



```bash

llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf

```



> Zonder het visiebestand verliest het model de **afbeeldingsbegripsmogelijkheid** en behoudt het alleen tekstgebaseerde gesprekken.



## Snelle Start



### 1. Download Modelfbestanden



Download alle bestanden onder de V3.7-map van HuggingFace / ModelScope:



```

V3.7/

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # Hoofdmodel (vereist)

├── moziAI-35B-mmproj-BF16-V1.0.gguf  # Visieprojectie (optioneel)

└── moziAI-V3.7-35B-chat-template.jinja                  # Chatsjabloon (aanbevolen)

```



### 2. Start Inferentieserver



Voor de volledige aanbevolen configuratie, zie [llama.cpp Startcommando](#llamacpp-startcommando) hierboven.



Minimale start (alleen kerndata):



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 131072 -ngl 99

```



> Voeg `--mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf` toe voor visiemogelijkheden.



### 3. Begin met Gebruiken



Open `http://localhost:8080` in uw browser om te beginnen met chatten.



### Mapstructuur



```

moziAI-35B/

├── README.md              # Chinese versie

├── README.en.md           # Engelse versie

├── README.nl.md           # Dit bestand (Nederlands)

├── LICENSE                # Licentie

├── V3.7/                  # V3.7 versie (zelfstandig)

├── RELEASE_NOTES.md                       # Releasenotities

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # Hoofdmodel

├── moziAI-35B-mmproj-BF16-V1.0.gguf # Visieprojectie

└── moziAI-V3.7-35B-chat-template.jinja   # Chatsjabloon

```



Voor het toekomstige upgradeplan, zie [未来升级计划.md](未来升级计划.md).



## SEO Trefwoorden



financieel AI LLM, lokaal open-source model, eindapparaatmodel, kwant programmering, MoziSmartBit, intelligente kwantisatie, GGUF kwantisatie, MoE-model, lokaal open-source LLM, lokale deployment, financieel AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, geen censuur, vrije output, onbeperkt, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, financieel vertaaldomein, open-source model



## Licentie (Belangrijk)



Dit model gebruikt een **Aangepaste Beperkte Licentie**:



### ✅ Toegestaan

- **Vrij Commercieel Gebruik**: Vrij te integreren in commerciële producten

- **Kopiëren & Verspreiden**: Kan gekopieerd, gedownload en gedeeld worden



### ❌ Verboden

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