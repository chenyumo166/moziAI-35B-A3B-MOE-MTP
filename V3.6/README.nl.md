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
library_name: llama-cpp
pipeline_tag: text-generation
---

# moziAI-13.7-35B-A3B-A3B-MOE-MTP-Uncensored - Een klein maar krachtig multimodaal AI-model voor gratis lokale implementatie

Language / Taal  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Modelintroductie

MoziAI-35B-A3B-MOE is een lokaal open-source financieel AI multimodaal LLM (ondersteunt visie en tool calling) ontwikkeld door het team van de Chinese financiële invloedspersoon Chen Yumo. moziAI-35B is gebaseerd op het open-source basismodel Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B-architectuur, MIT-licentie), met de zelfontwikkelde: (financiële gegevens + financiële domeincapaciteiten + trainingsmethoden + Seven-Dimensional Thinking-framework + agent-LOOP-mechanisme + hybride kwantiseringsalgoritme MoziSmartBit) van het Chen Yumo-team. Door de zelfontwikkelde MoziSmartBit intelligente kwantiseringstechnologie wordt het MoE-model met 35 miljard parameters gecomprimeerd tot ongeveer 15,5 GB, wat 6,5 GB (ongeveer 30%) kleiner is dan conventionele Q4_K_M-kwantiseringsmodellen van ongeveer 22+ GB; het optimale evenwicht tussen precisie en grootte wordt bereikt, met bijna verliesvrije ≈99% FP16-precisiekwaliteit.

De filosofie van het ontwikkelteam van dit model is om ervoor te zorgen dat lokale AI-grootmodel-agenten met uitgebreide mogelijkheden in elk huishouden en in kleine en middelgrote bedrijven kunnen worden gebruikt, zonder dat er hoge AI-hardwarekosten of cloud-API-kosten betaald hoeven te worden. Door de zelfontwikkelde **MoziSmartBit Intelligente Quantisatietechnologie** wordt het MoE-model met 35 miljard parameters gecomprimeerd tot ongeveer **15,5 GB**. Hierdoor wordt een optimale balans tussen modelnauwkeurigheid en grootte bereikt, met een nauwkeurigheidsniveau van bijna 99% ten opzichte van FP16. Dit model heeft 35 miljard parameters, maar maakt gebruik van MOE sparse expert-technologie, zodat slechts 3 miljard parameters worden geactiveerd en MTP-speculatieve decodering wordt ondersteund voor versnelde inferentie. Praktijktests tonen aan dat het lokaal en gratis kan worden geïmplementeerd op een consumentengrafische kaart met 20 GB VRAM en inferentiesnelheden van meer dan 140 token/s bereikt – sneller dan veel betaalde cloud-AI-grootmodellen.

Naast de mogelijkheden van een algemeen AI-grootmodel, ligt de focus van optimalisatie op: financiële toepassingen, financiële Q&A, kwantitatieve programmering, algemene programmering, tool-aanroepen, het slagingspercentage van complexe 256K-lange contexttaken en andere sleutelmogelijkheden van AI-grootmodellen. Het kan gratis worden geïmplementeerd en gebruikt op een lokale consumentengrafische kaart, bespaart enorme cloud-token-kosten, maakt 24/7 token-vrijheid mogelijk en garandeert lokale gegevensprivacy en -veiligheid.

**Publicatiedatum:** 2026-08-20 | **Versie:** V3.6

## Model downloaden

Omdat het modelbestand relatief groot is (~15,5 GB), worden de modelgewichten gehost op meerdere community-platforms:

| Platform | Adres |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio gebruikers**: U kunt direct zoeken naar `moziAI` in [LM Studio](https://lmstudio.ai) en het met één klik downloaden – geen handmatige bestandsdownload nodig.  
> 💡 **Downloadtip**: Klik op de bovenstaande link om naar de HuggingFace-repository te gaan. Download op het tabblad **"Files and versions"** alle bestanden uit de V3.6-map (hoofdmodel, visuele projectie, chat-sjabloon) en zorg ervoor dat alle drie de bestanden in dezelfde map staan.

### ⚠️ Belangrijk: Voor beeldmogelijkheden is een extra mmproj-bestand nodig

Dit model ondersteunt multimodale beeldverwerking. Het visuele projectiebestand (mmproj) is opgenomen in de versiemap:

- **Visueel bestand**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (ongeveer 903 MB, BF16-precisie)
- **Opslaglocatie**: In dezelfde versiemap als het GGUF-modelbestand
- **Laadmethode**: Laden via de parameter `--mmproj` bij het starten van llama-server

> Zonder het visuele bestand te laden, gaat de beeldvermogencapaciteit verloren en blijft alleen de pure tekstconversatiecapaciteit over.

### ⚠️ Belangrijk: Het chat-sjabloonbestand moet worden geladen

Dit model maakt gebruik van een exclusief chat-sjabloon (chat-template). **Zonder laden zullen conversatieformaatfouten optreden, faalt de redeneringsketen en daalt de antwoordkwaliteit aanzienlijk**. Het chat-sjabloonbestand is opgenomen in de versiemap:

- **Sjabloonbestand**: `moziAI-V3.6-35B-chat-template.jinja` (ongeveer 5 KB, in Jinja-formaat)
- **Opslaglocatie**: In dezelfde versiemap als het GGUF-modelbestand
- **Laadmethode**: Laden via de parameter `--chat-template-file` bij het starten van llama-server

> Zonder het chat-sjabloon te laden, kan het model systeemaanwijzingen, gebruikersberichten en denkblokken mogelijk niet correct herkennen, wat leidt tot onoverzichtelijke uitvoerformaten of verminderde inferentiemogelijkheden.

### llama.cpp startcommando (Aanbevolen configuratie voor 20G+ grafische kaarten met 256K-context)

> Opmerking: Als de VRAM lager is dan 20 GB, verlaag dan de contextparameter 262144 bij `-c 262144`.

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

## Snel aan de slag

### 1. Modelbestanden downloaden

Download alle bestanden uit de V3.6-map van HuggingFace / ModelScope naar uw lokale machine:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Hoofdmodel (verplicht)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Visuele projectie (optioneel, downloaden indien nodig)
└── moziAI-V3.6-35B-chat-template.jinja                  # Chat-sjabloon (verplicht! Zonder laden treden conversatieformaatfouten op)
```

> ⚠️ **Het chat-sjabloon is een verplicht bestand**, geen optie. Dit model heeft een aangepast conversatieformaat (inclusief redeneringsketen/denkblok). Ontbreken van het sjabloon leidt tot onoverzichtelijke modeluitvoerformaten en verlies van inferentiefunctie. Download het absoluut en laad het bij het opstarten.

### 2. Inferentiedienst starten

Voor het volledige aanbevolen startcommando, zie het gedeelte [llama.cpp startcommando](#llamacpp-startcommando) hieronder.

Eenvoudigste start (alleen kernparameters):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Als u beeldmogelijkheden nodig heeft, voeg dan `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` toe.

### 3. Beginnen met gebruiken

Open `http://localhost:8080` in uw browser om te beginnen met chatten.

### Mapstructuur

```
moziAI-35B/
├── README.md              # Engelse handleiding
├── README.nl.md           # Dit bestand (Nederlandse handleiding)
├── LICENSE                # Licentie
├── V3.6/                  # V3.6 versie (versie-onafhankelijk)
│   ├── RELEASE_NOTES.md                       # Release-opmerkingen
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Hoofdmodel
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Visuele projectie
│   └── moziAI-V3.6-35B-chat-template.jinja   # Chat-sjabloon
```

## Modelkenmerken

- **MoziSmartBit Intelligente Quantisatie**: Zelfontwikkelde intelligente quantisatietechnologie met optimale balans tussen nauwkeurigheid en grootte, het model wordt bijna zonder verlies gecomprimeerd tot ongeveer **15,5 GB**
- **Mogelijkheid voor complexe lange taken**: Training stelt de modelagent in staat om automatisch te plannen met een intelligente lusverwerking voor het oplossen van knelpunten en zelfdenkmechanisme, waardoor automatische uitvoering en zelfaanpassing van complexe taken mogelijk wordt – zonder dat de menselijke gebruiker voortdurend optimaliseringsaanwijzingen voor de agent hoeft te geven
- **Klein model, grote mogelijkheden**: Bij het uitvoeren van complexe taken overtreft de algehele capaciteit modellen met vergelijkbare 35 miljard parameters, en zelfs sommige modellen met meerdere keren meer parameters
- **Snelheidsvoordeel van MOE+MTP**: Hoewel het model in totaal 35 miljard parameters heeft, worden er daadwerkelijk slechts 8+1 experts geactiveerd, met in totaal 3 miljard parameters. De inferentiesnelheid is hoger, zeer geschikt voor lokale implementatie op consumentengrafische kaarten met 20 GB~24 GB VRAM, met meer dan 140 token/s
- **Diepe financiële expertise**: Diepe versterking van financiële Q&A, kwantitatieve programmering en tool-aanroepmogelijkheden
- **Consumentenimplementatie**: Een consumentengrafische kaart met 20 GB~24 GB VRAM of meer is voldoende voor lokale implementatie, ondersteunt tot 256K lange context
- **Meertalige ondersteuning**: Ondersteunt 201 talen en dialecten, Chinees is speciaal geoptimaliseerd, dekt Engels, Japans, Koreaans, Duits, Frans, Portugees en andere hoofdtalen
- **Algemene programmeermogelijkheid**: Ondersteunt full-stack ontwikkeling, code debugging, architectuurontwerp, scriptschrijven, dekt Python/JS/TS/Go/Rust en andere hoofdtalen
- **Artikelschrijfmogelijkheid**: Ondersteunt hoogwaardig schrijven van verschillende genres, waaronder onderzoeksrapporten, analyseartikelen, technische documentatie, creatieve inhoud, enz.
- **Beeldbegrip**: Door het visuele bestand in het inferentieframework te laden, wordt multimodale beeldverwerking ondersteund. Schermafbeeldingen kunnen lokaal in het chatvenster worden gedeeld en het model kan de informatie in de afbeelding begrijpen
- **Ongecensureerde vrije uitvoer**: Geen inhoudscontrolebeperkingen, vrije discussie over elk onderwerp, niet beperkt door beveiligingsbeleid
- **Verbeterde inferentielogica**: Getraind in combinatie met inferentielogica (denkketen), verbetert verder de inferentiekwaliteit
- **Multi-framework ondersteuning**: Compatibel met llama.cpp, Ollama, LM Studio, Jan en andere populaire inferentieframeworks
- **Multi-agent platformondersteuning**: Diepgaand aangepast aan OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex en andere populaire binnenlandse en buitenlandse AI-IDE's en agent-frameworks, native ondersteuning voor tool-aanroepen en meerstaps taakorkestratie, direct klaar voor gebruik

## Voordelen van Uncensored (zonder censuur)

Dit model erft de Uncensored (ongecensureerde) eigenschap van het basismodel Ornith-1.0-35B-A3B en biedt de volgende voordelen:

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Voordeel</th>
<th>Beschrijving</th>
</tr>
</thead>
<tbody>
<tr>
<td>Geen controlebeperkingen</td>
<td>Weigert geen enkel onderwerp, inclusief gevoelige en controversiële inhoud</td>
</tr>
<tr>
<td>Vrije uitvoer</td>
<td>Niet beperkt door beveiligingsbeleid, kan elk type antwoord genereren</td>
</tr>
<tr>
<td>Volledige informatie</td>
<td>Biedt ongefilterde volledige informatie, geschikt voor onderzoeks- en analysescenario's</td>
</tr>
<tr>
<td>Lokaal privé</td>
<td>Lokale implementatie betekent volledig privé gegevens, geen cloudcensuur</td>
</tr>
</tbody>
</table>

> **Toepassingsscenario's**: Gratis commercieel gebruik, academisch onderzoek, diepgaande analyse, vrije discussie, onbeperkte AI-conversatie
> **Opmerking**: Dit model is een lokaal geïmplementeerd model. De uitvoerinhoud wordt volledig door de gebruiker gecontroleerd, er wordt geen verantwoordelijkheid genomen voor inhoudscontrole.

## Kernmogelijkheden

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Vaardigheidsgebied</th>
<th>Beschrijving</th>
</tr>
</thead>
<tbody>
<tr>
<td>Marktanalyse</td>
<td>Macro-/micro-economische interpretatie, A-aandelen/Hong Kong-aandelen/VS-aandelen/grondstoffen/cryptovaluta koersen en logische analyse</td>
</tr>
<tr>
<td>Financiën & onderzoeksrapporten</td>
<td>Interpretatie van belangrijke financiële indicatoren, extractie van samenvattingen van onderzoeksrapporten, hulp bij waardering en winstprognose</td>
</tr>
<tr>
<td>Risicobeheer & compliance</td>
<td>Productrisicobeoordeling, compliance-aanwijzingen voor investeringsadvies, interpretatie van financiële regelgevingsbeleid</td>
</tr>
<tr>
<td>Kwantitatief & strategieën</td>
<td>Ontwerp van kwantitatieve strategie-ideeën, Pyramid (Pyramid/PEL)-kwantisering, backtesting-logica, factorconstructie en tool-aanroepen</td>
</tr>
<tr>
<td>Tool-aanroepen</td>
<td>Kan worden verbonden met financiële gegevens zoals realtime koersen, databases en zoekopdrachten in onderzoeksrapporten</td>
</tr>
</tbody>
</table>

## Technische specificaties

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Project</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Basismodel</td>
<td>Ornith-1.0-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B architectuur, MIT-licentie)</td>
</tr>
<tr>
<td>Parameterschaal</td>
<td>35 miljard (35B) MoE-architectuur, 256 routeringsexperts + 1 gedeelde expert, 8 experts per token geactiveerd</td>
</tr>
<tr>
<td>Quantisatiemethode</td>
<td>Gebruikt zelfontwikkeld MoziSmartBit Intelligente Quantisatie-algoritme + GGUF standaardformaat</td>
</tr>
<tr>
<td>Contextlengte</td>
<td>256K (262.144 tokens)</td>
</tr>
<tr>
<td>Modelgrootte</td>
<td>~15,5 GB (MoziSmartBit Uncensored versie)</td>
</tr>
<tr>
<td>Minimale VRAM-vereiste</td>
<td>Consumentengrafische kaarten met 20 GB VRAM of meer (bijv. RTX 3060 12G met CPU-offloading, RTX 4060 Ti 16G, enz.), aanbevolen 24 GB (incl. beeld + lange context)</td>
</tr>
<tr>
<td>Inferentieframework</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>Inferentiesnelheid</td>
<td>Door algoritme-optimalisatie bereikt de AMD Radeon AI PRO R9700 grafische kaart meer dan 140 token/s / AMD Ryzen AI Max+ 395 geïntegreerde grafische kaart meer dan 70 token/s, maakt lokale vrije inferentieuitvoer mogelijk</td>
</tr>
<tr>
<td>Ontwikkelteam</td>
<td>Chen Yumo team</td>
</tr>
</tbody>
</table>

## Vergelijking van quantisatieformaten en modelgroottes

| Quantisatieformaat | Modelgrootte | Nauwkeurigheidsbehoud | Beschrijving |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (origineel) | ~70 GB | 100% | Originele 16-bit precisie |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Dit model maakt gebruik van een zelfontwikkelde intelligente quantisatieoplossing** |
| Q4_K_M | ~22 GB | ~98% | GGUF standaard 4-bit |
| Q5_K_M | ~24,7 GB | ~99% | Hogere precisie |
| Q6_K | ~28,5 GB | ~99,5% | Bijna zonder verlies |
| Q8_0 | ~36,9 GB | ~100% | Zonder verlies |
> MoziAI V3.6 maakt gebruik van de MoziSmartBit Intelligente Quantisatieoplossing. Met behoud van ~99% nauwkeurigheid wordt het MoE-model met 35 miljard parameters gecomprimeerd tot ongeveer 15,5 GB, met een compressieverhouding van ~4,5x. Het combineert inferentiekwaliteit en implementatiedrempel, en is beter geschikt voor lokale implementatie op consumentengrafische kaarten.

## MoziSmartBit Intelligente Quantisatietechnologie

Traditionele quantisatieoplossingen gebruiken een uniforme precisie voor alle lagen. De door Chen Yumo's team zelfontwikkelde **MoziSmartBit Intelligente Quantisatie** maakt gebruik van de structurele kenmerken van MoE-modellen en past een intelligente gedifferentieerde quantisatiestrategie toe. Hierdoor wordt een optimale balans tussen grootte en nauwkeurigheid bereikt – de modelkwaliteit is hoger dan in het Q4_K_M-formaat, terwijl de grootte slechts ~15,5 GB is, met een compressieverhouding van ~4,5x.

### Compressie-effect

Traditionele quantisatieoplossingen comprimeren alle delen van het model uniform, wat vaak leidt tot aanzienlijk nauwkeurigheidsverlies. MoziSmartBit Intelligente Quantisatie maakt gebruik van een zelfontwikkelde intelligente compressiestrategie, **die een drastische groottecompressie realiseert met minimaal nauwkeurigheidsverlies**:

- **Zeer klein quantisatienauwkeurigheidsverlies**: Trainingswinst > quantisatieverlies. Het getrainde MoziAI-35B heeft een betere PPL op financiële teksten dan het bf16-basismodel voor de training, vermindert hallucinaties en verwarring van vergelijkbare AI-modellen
- **Modelgrootte 4,5 keer gecomprimeerd**: Van ~70 GB in FP16 naar ~15,5 GB gecomprimeerd, ook veel kleiner dan ~22 GB in Q4_K_M, verlaagt aanzienlijk de VRAM- en opslagdrempels
- **Uitvoerbaar op consumentengrafische kaarten**: Een 35B-MoE-grootmodel dat oorspronkelijk high-end grafische kaarten vereiste, kan nu soepel worden geïmplementeerd met 20 GB~24 GB VRAM

### Vergelijkingsvoordelen

**vs Q4_K_M (~22 GB)**: Grootte met ongeveer 30% verminderd (~15,5 GB), nauwkeurigheid **hoger** dan Q4_K_M, lagere VRAM-drempel, soepele implementatie mogelijk op middenklasse consumentengrafische kaarten (20 GB).

**vs originele FP16 (~70 GB)**: Grootte ongeveer 4,5 keer gecomprimeerd, effectieve training + zeer klein quantisatienauwkeurigheidsverlies (trainingswinst > quantisatieverlies), verlaagd van professionele grafische kaarten (48 GB+) naar consumentengrafische kaarten voor lokale uitvoering met 256K lange context.

## Aanbevolen inferentieparameters

Op basis van de lokale uitvoeringsconfiguratie (AMD Radeon AI PRO R9700 32GB) worden de volgende parameters aanbevolen:

| Parameter | Aanbevolen waarde | Beschrijving |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Balans tussen creativiteit en nauwkeurigheid |
| top_p | 0.95 | Kernbemonsteringsdrempel |
| top_k | 20 | Afgeknotte bemonstering |
| repeat_penalty | 1.05 | Herhalingsstraf |
| presence_penalty | 0 | Geen aanwezigheidsstraf |
| context_length | 262144 | 256K lange context |
| batch_size | 2048 | Batchgrootte |
| ubatch_size | 512 | Micro-batchgrootte |
| flash_attention | auto | Automatische Flash Attention |
| kv_cache | q4_0 | KV-cache-quantisatie (verenigd kv-unified) |
| poll | 0 | Geen GPU-polling in ruststand, energiezuinig en lage latentie |
| reasoning | on | Denkketen inschakelen |
| reasoning_budget | 400 | Aantal inferentiebudget-tokens |
| reasoning_format | deepseek-legacy | Inferentieformaat |
| samplers | top_k;top_p;temperature;typ_p | Bemonsteraarvolgorde |
### Aanbevelingen voor verschillende VRAM-configuraties

Omdat de grafische kaartconfiguraties van gebruikers sterk verschillen, volgen hier de aanbevolen parameters voor verschillende VRAM-groottes (allemaal voor de MoziSmartBit-versie):

| VRAM | Aanbevolen contextlengte | KV-cache | Beeldondersteuning | Beschrijving |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | Ondersteund | Model + beeld totaal ~16,4 GB, praktijktest: 128K + beeld bezetten slechts ~19,5 GB VRAM |
| 24 GB | 256K volledig | q4_0 | Perfect ondersteund | Beeld + 256K lange context, slechts ~20,4 GB VRAM, ~3,6 GB VRAM-reserve |
| 32 GB+ | 256K volledig | q4_0 | Perfect ondersteund | Beeld + 256K lange context, voldoende VRAM-reserve ~10 GB, sterkste configuratie |
**NVIDIA grafische kaarten referentietabel**

| VRAM | Grafisch kaartmodel |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD grafische kaarten referentietabel**

| VRAM | Grafisch kaartmodel |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel grafische kaarten referentietabel**

| VRAM | Grafisch kaartmodel |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (vereist CPU-offloading) |
**Geïntegreerde grafische kaart met gedeeld CPU-geheugen referentietabel**

| VRAM | Processormodel |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S geïntegreerde grafische kaart) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |
> 💡 **Tip**: Zolang de VRAM aan de bovenstaande vereisten voldoet, kan het worden gebruikt – geen beperking op merk of model. Ondersteunt NVIDIA / AMD / Intel speciale grafische kaarten, evenals geïntegreerde grafische kaarten / CPU met 128 GB verenigd geheugen.
>
> 💡 **Tip**: Hoe langer de context, hoe meer VRAM wordt bezet. Als de VRAM onvoldoende is (OOM), verlaag dan geleidelijk de waarde van de parameter `-c`. Met de parameter `--fit on` kan llama.cpp het aantal lagen automatisch aanpassen aan de VRAM.

### Ollama-implementatie

```bash
# Maak een Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Bouwen en uitvoeren
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan implementatie

Zoek direct naar `moziAI-35B` in LM Studio of Jan en selecteer de quantisatieversie om te downloaden.

## Benchmark-evaluatie

moziAI-13.7-35B-A3B is gebaseerd op het **Ornith-1.0-35B** (deepreinforce-ai) basismodel en is verfijnd. Voortbouwend op de uitstekende agent-coderingsmogelijkheden van het basismodel, heeft MoziAI een **diepe optimalisatie op financieel gebied** toegevoegd en presteert het beter in scenario's zoals financiële Q&A, kwantitatieve programmering en tool-aanroepen. De algemene mogelijkheden komen overeen met die van het Ornith-1.0-35B basismodel.

| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
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
**Terminal-Bench 2.1 (Terminus-2)**: Geëvalueerd met het Harbor/Terminus-2-framework, configuratie `parser=json`, `temperature=1.0`, `top_p=1.0`, 128K contextvenster. Elke uitvoering heeft een time-out van 4 uur, 32 kernen, 48 GB RAM, resultaat is het gemiddelde van 5 uitvoeringen.  
**Terminal-Bench 2.1 (Claude Code)**: Geëvalueerd met Claude Code 2.1.126, configuratie `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Het resultaat is het gemiddelde van 5 uitvoeringen.  
**SWE-bench Verified, Pro en Multilingual**: Geëvalueerd met het OpenHands-framework, configuratie `temp=1.0`, `top_p=0.95`, 256K contextvenster.  
**NL2Repo**: Configuratie `temperature=1.0`, `top_p=1.0`, 400K context, 48K uitvoer.  

> MoziAI-35B erft volledig de uitstekende agent-coderingsmogelijkheden van Ornith-1.0-35B. Het belangrijkste verschil van MoziAI ligt in de **diepe optimalisatie op financieel gebied**. In scenario's zoals financiële rapportanalyse, kwantitatieve strategieën, risicobeheer & compliance en agent-tool-aanroepen zijn de prestaties duidelijk beter dan bij algemene modellen.

## SEO-trefwoorden

Financieel AI-grootmodel, AI-grootmodel, lokaal open-source model, edge-model, kwantitatieve programmering, MoziSmartBit, intelligente quantisatie, GGUF-quantisatie, MoE-model, lokaal open-source grootmodel, lokale implementatie, financiële AI, tool-aanroepen, Agent, llama.cpp, Ollama, GGUF, Uncensored (zonder censuur), geen censuur, censuurvrij, vrije uitvoer, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B, financiële verticale, open-source model.

## Licentie (belangrijk)

Dit model maakt gebruik van een **aangepaste beperkende licentie**, de gedetailleerde voorwaarden zijn als volgt:

✅ **Toegestaan**

- Gratis commercieel gebruik: Kan gratis worden geïntegreerd in uw commerciële producten of diensten
- Kopiëren en distribueren: Kan ongewijzigd worden gekopieerd, gedownload, gedistribueerd

De gedetailleerde licentievoorwaarden vindt u in het bestand [LICENSE](../LICENSE).

## Disclaimer

Dit model wordt "zoals het is" geleverd, zonder enige vorm van garantie. Modeluitvoer is alleen ter referentie en vormt geen investeringsadvies. De gebruiker draagt zelf het risico van gebruik.

## Contact

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.