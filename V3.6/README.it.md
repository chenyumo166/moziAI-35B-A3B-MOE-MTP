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
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.6-A3B-MOE-MTP-Uncensored - Un modello AI multimodale piccolo ma potente, distribuibile localmente gratuitamente

Language / Lingua  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## Introduzione al modello

MoziAI-35B-A3B-MOE è un grande modello AI multimodale open-source locale sviluppato dal team di Chen Yumo, influencer finanziario cinese (potenziato nel settore finanziario, supporta la visione, le chiamate di strumenti, le attività lunghe e complesse e la distribuzione locale su schede grafiche consumer). Si basa sul modello base Ornith-1.0-35B-A3B (architettura **Qwen3.5-35B-A3B/Qwen3.6-35B-A3B**) ed è stato ulteriormente sviluppato e affinato/distillato.

La filosofia del team di sviluppo di questo modello è fare in modo che gli agenti di grandi modelli AI locali con capacità complete possano entrare in ogni famiglia e nelle piccole e medie imprese, senza dover pagare costi hardware AI elevati o costi di API cloud. Grazie alla tecnologia di **quantizzazione intelligente MoziSmartBit** sviluppata internamente, il modello MoE da 35 miliardi di parametri viene compresso a circa **15,5 GB**. Ciò consente di raggiungere un equilibrio ottimale tra precisione del modello e dimensione, con una qualità di precisione di quasi il 99% rispetto a FP16. Questo modello ha 35 miliardi di parametri, ma utilizza la tecnologia di esperti sparse MOE, quindi solo 3 miliardi di parametri vengono attivati e la decodifica speculativa MTP è supportata per un'inferenza accelerata. I test pratici dimostrano che può essere distribuito localmente e gratuitamente su una scheda grafica consumer con 20 GB di VRAM e raggiunge velocità di inferenza superiori a 140 token/s – più veloce di molti grandi modelli AI cloud a pagamento.

Oltre alle capacità di un grande modello AI generale, l'ottimizzazione si concentra su: applicazioni finanziarie, domande e risposte finanziarie, programmazione quantitativa, programmazione generale, chiamate di strumenti, il tasso di successo delle attività complesse a contesto lungo 256K e altre capacità chiave dei grandi modelli AI. Può essere distribuito e utilizzato gratuitamente su una scheda grafica consumer locale, risparmia enormi costi di token cloud, consente la libertà dei token 24 ore su 24, 7 giorni su 7, e garantisce la privacy e la sicurezza dei dati locali.

**Data di pubblicazione:** 2026-08-20 | **Versione:** V3.6

## Download del modello

Poiché il file del modello è relativamente grande (~15,5 GB), i pesi del modello sono ospitati su più piattaforme comunitarie:

| Piattaforma | Indirizzo |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

> 💡 **Utenti di LM Studio**: Puoi cercare direttamente `moziAI` in [LM Studio](https://lmstudio.ai) e scaricarlo con un clic – nessun download manuale di file necessario.  
> 💡 **Suggerimento per il download**: Clicca sul link sopra per accedere alla repository HuggingFace. Nella scheda **"Files and versions"**, scarica tutti i file dalla directory V3.6 (modello principale, proiezione visiva, modello di chat) e assicurati che tutti e tre i file si trovino nella stessa directory.

### ⚠️ Importante: La capacità visiva richiede un file mmproj aggiuntivo

Questo modello supporta la visione multimodale. Il file di proiezione visiva (mmproj) è incluso nella directory della versione:

- **File visivo**: `moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf` (circa 903 MB, precisione BF16)
- **Posizione**: Nella stessa directory della versione del file del modello GGUF
- **Metodo di caricamento**: Caricare tramite il parametro `--mmproj` all'avvio di llama-server

> Senza caricare il file visivo, la capacità di comprensione delle immagini viene persa, rimane solo la capacità di conversazione di testo puro.

### ⚠️ Importante: Il file del modello di chat deve essere caricato

Questo modello utilizza un modello di chat esclusivo (chat-template). **Senza caricamento si verificheranno errori di formato della conversazione, la catena di ragionamento fallirà e la qualità delle risposte diminuirà drasticamente**. Il file del modello di chat è incluso nella directory della versione:

- **File modello**: `moziAI-V3.6-35B-chat-template.jinja` (circa 5 KB, in formato Jinja)
- **Posizione**: Nella stessa directory della versione del file del modello GGUF
- **Metodo di caricamento**: Caricare tramite il parametro `--chat-template-file` all'avvio di llama-server

> Senza caricare il modello di chat, il modello potrebbe non riconoscere correttamente i prompt di sistema, i messaggi utente e i blocchi di pensiero, causando formati di output confusi o capacità di inferenza ridotte.

### Comando di avvio llama.cpp (Configurazione consigliata per schede grafiche 20G+ con contesto 256K)

> Nota: Se la VRAM è inferiore a 20 GB, ridurre il parametro di contesto 262144 di `-c 262144`.

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

## Guida rapida

### 1. Scaricare i file del modello

Scarica tutti i file dalla directory V3.6 da HuggingFace / ModelScope sulla tua macchina locale:

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # Modello principale (obbligatorio)
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # Proiezione visiva (opzionale, scaricare se necessario)
└── moziAI-V3.6-35B-chat-template.jinja                  # Modello di chat (obbligatorio! Senza caricamento, errori di formato della conversazione)
```

> ⚠️ **Il modello di chat è un file obbligatorio**, non opzionale. Questo modello ha un formato di conversazione personalizzato (inclusa catena di ragionamento/blocco di pensiero). L'assenza del modello causerà formati di output del modello confusi e perdita della funzione di inferenza. Si prega di scaricarlo assolutamente e caricarlo all'avvio.

### 2. Avviare il servizio di inferenza

Per il comando di avvio completo consigliato, fare riferimento alla sezione [Comando llama.cpp](#comando-llamacpp) di seguito.

Avvio minimo (solo parametri principali):

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> Se hai bisogno di capacità visive, aggiungi `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`

### 3. Iniziare a usare

Apri `http://localhost:8080` nel tuo browser per iniziare la conversazione.

### Struttura delle directory

```
moziAI-35B/
├── README.md              # Manuale in inglese
├── README.it.md           # Questo file (manuale in italiano)
├── LICENSE                # Licenza
├── V3.6/                  # Versione V3.6 (autonoma per versione)
│   ├── RELEASE_NOTES.md                       # Note di rilascio
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # Modello principale
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # Proiezione visiva
│   └── moziAI-V3.6-35B-chat-template.jinja   # Modello di chat
```

## Caratteristiche del modello

- **Quantizzazione intelligente MoziSmartBit**: Tecnologia di quantizzazione intelligente sviluppata internamente, equilibrio ottimale tra precisione e dimensione, il modello viene compresso quasi senza perdite a circa **15,5 GB**
- **Capacità per attività lunghe e complesse**: L'addestramento consente all'agente del modello di pianificare automaticamente con un meccanismo di elaborazione a ciclo intelligente per superare gli ostacoli e di auto-pensiero, consentendo l'esecuzione automatica e l'auto-adeguamento di attività complesse – senza che l'utente umano debba costantemente ottimizzare i prompt per l'agente
- **Modello piccolo, grandi capacità**: Nell'esecuzione di attività complesse, la capacità globale supera i modelli simili con meno di 35 miliardi di parametri, e anche alcuni modelli con diverse volte più parametri
- **Vantaggio di velocità di MOE+MTP**: Sebbene il modello abbia in totale 35 miliardi di parametri, vengono effettivamente attivati solo 8+1 esperti, per un totale di 3 miliardi di parametri. La velocità di inferenza è maggiore, molto adatta per la distribuzione locale su schede grafiche consumer con 20 GB~24 GB di VRAM, con oltre 140 token/s
- **Esperienza finanziaria approfondita**: Potenziamento profondo di domande e risposte finanziarie, programmazione quantitativa e capacità di chiamata di strumenti
- **Distribuzione consumer**: Una scheda grafica consumer con 20 GB~24 GB di VRAM o più è sufficiente per la distribuzione locale, supporta contesti lunghi fino a 256K
- **Supporto multilingue**: Supporta 201 lingue e dialetti, il cinese è particolarmente ottimizzato, copre inglese, giapponese, coreano, tedesco, francese, portoghese e altre lingue principali
- **Capacità di programmazione generale**: Supporta lo sviluppo full-stack, il debug del codice, la progettazione dell'architettura, la scrittura di script, copre Python/JS/TS/Go/Rust e altre lingue principali
- **Capacità di scrittura di articoli**: Supporta la scrittura di alta qualità di vari generi, inclusi rapporti di ricerca, articoli di analisi, documentazione tecnica, contenuti creativi, ecc.
- **Comprensione visiva**: Caricando il file visivo nel framework di inferenza, la visione multimodale è supportata. Le schermate possono essere condivise localmente nella finestra di chat e il modello può comprendere le informazioni nell'immagine
- **Output libero non censurato**: Nessuna restrizione di controllo del contenuto, discussione libera su qualsiasi argomento, non limitato dalle politiche di sicurezza
- **Logica di inferenza migliorata**: Addestrato in congiunzione con la logica di inferenza (catena di pensiero), migliora ulteriormente la qualità dell'inferenza
- **Supporto multi-framework**: Compatibile con llama.cpp, Ollama, LM Studio, Jan e altri framework di inferenza popolari
- **Supporto piattaforma multi-agente**: Profondamente adattato a OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex e altri IDE AI e framework agent popolari cinesi e stranieri, supporto nativo per chiamate di strumenti e orchestrazione di attività multi-turno, pronto all'uso

## Vantaggi di Uncensored (senza censura)

Questo modello eredita la caratteristica Uncensored (senza censura) del modello base Ornith-1.0-35B-A3B e offre i seguenti vantaggi:

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Vantaggio</th>
<th>Descrizione</th>
</tr>
</thead>
<tbody>
<tr>
<td>Nessuna restrizione di censura</td>
<td>Non rifiuta nessun argomento, inclusi contenuti sensibili e controversi</td>
</tr>
<tr>
<td>Output libero</td>
<td>Non limitato dalle politiche di sicurezza, può generare qualsiasi tipo di risposta</td>
</tr>
<tr>
<td>Informazioni complete</td>
<td>Fornisce informazioni complete non filtrate, adatto a scenari di ricerca e analisi</td>
</tr>
<tr>
<td>Locale e privato</td>
<td>La distribuzione locale significa dati completamente privati, nessuna censura cloud</td>
</tr>
</tbody>
</table>

> **Scenari di applicazione**: Uso commerciale gratuito, ricerca accademica, analisi approfondita, discussione libera, conversazione AI illimitata
> **Nota**: Questo modello è un modello distribuito localmente. Il contenuto di output è completamente controllato dall'utente, non si assume alcuna responsabilità per il controllo del contenuto.

## Capacità principali

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Area di capacità</th>
<th>Descrizione</th>
</tr>
</thead>
<tbody>
<tr>
<td>Analisi di mercato</td>
<td>Interpretazione macro/microeconomica, analisi dei corsi e logica di azioni A/azioni di Hong Kong/azioni statunitensi/materie prime/criptovalute</td>
</tr>
<tr>
<td>Finanza e rapporti di ricerca</td>
<td>Interpretazione dei principali indicatori finanziari, estrazione di riassunti di rapporti di ricerca, supporto per valutazione e previsione degli utili</td>
</tr>
<tr>
<td>Gestione del rischio e conformità</td>
<td>Valutazione del rischio prodotto, suggerimenti di conformità per consulenze di investimento, interpretazione delle politiche di regolamentazione finanziaria</td>
</tr>
<tr>
<td>Quantitativo e strategie</td>
<td>Progettazione di idee di strategie quantitative, quantizzazione Pyramid (Pyramid/PEL), logica di backtesting, costruzione di fattori e chiamate di strumenti</td>
</tr>
<tr>
<td>Chiamate di strumenti</td>
<td>Può essere collegato a dati finanziari come corsi in tempo reale, database e ricerca di rapporti di ricerca</td>
</tr>
</tbody>
</table>

## Specifiche tecniche

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>Progetto</th>
<th>Parametro</th>
</tr>
</thead>
<tbody>
<tr>
<td>Modello base</td>
<td>Ornith-1.0-35B-A3B (architettura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licenza MIT)</td>
</tr>
<tr>
<td>Scala dei parametri</td>
<td>35 miliardi (35B) architettura MoE, 256 esperti di routing + 1 esperto condiviso, 8 esperti attivati per token</td>
</tr>
<tr>
<td>Metodo di quantizzazione</td>
<td>Utilizza l'algoritmo di quantizzazione intelligente MoziSmartBit sviluppato internamente + formato standard GGUF</td>
</tr>
<tr>
<td>Lunghezza del contesto</td>
<td>256K (262.144 token)</td>
</tr>
<tr>
<td>Dimensione del modello</td>
<td>~15,5 GB (versione MoziSmartBit Uncensored)</td>
</tr>
<tr>
<td>Requisito minimo di VRAM</td>
<td>Schede grafiche consumer con 20 GB di VRAM o più (es. RTX 3060 12G con offloading CPU, RTX 4060 Ti 16G, ecc.), consigliati 24 GB (incl. visivo + contesto lungo)</td>
</tr>
<tr>
<td>Framework di inferenza</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>Velocità di inferenza</td>
<td>Grazie all'ottimizzazione degli algoritmi, la scheda grafica AMD Radeon AI PRO R9700 raggiunge oltre 140 token/s / la GPU integrata AMD Ryzen AI Max+ 395 raggiunge oltre 70 token/s, consentendo output di inferenza libero locale</td>
</tr>
<tr>
<td>Team di sviluppo</td>
<td>Team Chen Yumo</td>
</tr>
</tbody>
</table>

## Confronto tra formati di quantizzazione e dimensioni del modello

| Formato di quantizzazione | Dimensione del modello | Precisione mantenuta | Descrizione |
| ---------------- | ------------- | --------- | ----------------- |
| FP16 (originale) | ~70 GB | 100% | Precisione originale a 16 bit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Questo modello utilizza una soluzione di quantizzazione intelligente sviluppata internamente** |
| Q4_K_M | ~22 GB | ~98% | 4 bit standard GGUF |
| Q5_K_M | ~24,7 GB | ~99% | Maggiore precisione |
| Q6_K | ~28,5 GB | ~99,5% | Quasi senza perdite |
| Q8_0 | ~36,9 GB | ~100% | Senza perdite |

> MoziAI V3.6 utilizza la soluzione di quantizzazione intelligente MoziSmartBit. Mantenendo ~99% di precisione, il modello MoE da 35 miliardi di parametri viene compresso a circa 15,5 GB, con un rapporto di compressione di ~4,5x. Combina qualità di inferenza e soglia di distribuzione, ed è più adatto per la distribuzione locale su schede grafiche consumer.

## Tecnologia di quantizzazione intelligente MoziSmartBit

Le soluzioni di quantizzazione tradizionali utilizzano una precisione uniforme per tutti i livelli. La **quantizzazione intelligente MoziSmartBit**, sviluppata internamente dal team di Chen Yumo, sfrutta le caratteristiche strutturali dei modelli MoE e implementa una strategia di quantizzazione differenziata intelligente. Ciò consente di raggiungere un equilibrio ottimale tra dimensione e precisione – la qualità del modello è superiore a quella del formato Q4_K_M, mentre la dimensione è solo di ~15,5 GB, con un rapporto di compressione di ~4,5x.

### Effetto di compressione

Le soluzioni di quantizzazione tradizionali comprimono uniformemente tutte le parti del modello, il che spesso porta a perdite di precisione significative. La quantizzazione intelligente MoziSmartBit utilizza una strategia di compressione intelligente sviluppata internamente, **che realizza una compressione delle dimensioni drastica con una perdita di precisione minima**:

- **Perdita di precisione di quantizzazione estremamente bassa**: Guadagno di addestramento > perdita di quantizzazione. Il MoziAI-35B addestrato ha un PPL migliore sui testi finanziari rispetto al modello base bf16 prima dell'addestramento, riduce allucinazioni e confusione di modelli AI simili
- **Dimensione del modello compressa di 4,5 volte**: Da ~70 GB in FP16 a ~15,5 GB compresso, anche molto più piccolo di ~22 GB in Q4_K_M, riduce drasticamente le soglie di VRAM e archiviazione
- **Eseguibile su schede grafiche consumer**: Un grande modello MoE 35B che originariamente richiedeva schede grafiche di fascia alta, ora può essere distribuito senza problemi con 20 GB~24 GB di VRAM

### Vantaggi comparativi

**vs Q4_K_M (~22 GB)**: Dimensione ridotta di circa il 30% (~15,5 GB), precisione **maggiore** di Q4_K_M, soglia di VRAM più bassa, distribuzione fluida possibile su schede grafiche consumer di fascia media (20 GB).

**vs FP16 originale (~70 GB)**: Dimensione compressa di circa 4,5 volte, addestramento efficace + perdita di precisione di quantizzazione estremamente bassa (guadagno di addestramento > perdita di quantizzazione), passaggio da schede grafiche professionali (48 GB+) a schede grafiche consumer per l'esecuzione locale con contesto lungo 256K.

## Parametri di inferenza consigliati

Basandosi sulla configurazione di esecuzione locale (AMD Radeon AI PRO R9700 32GB), sono consigliati i seguenti parametri:

| Parametro | Valore consigliato | Descrizione |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | Equilibrio tra creatività e precisione |
| top_p | 0.95 | Soglia di campionamento nucleare |
| top_k | 20 | Campionamento troncato |
| repeat_penalty | 1.05 | Penalità di ripetizione |
| presence_penalty | 0 | Nessuna penalità di presenza |
| context_length | 262144 | Contesto lungo 256K |
| batch_size | 2048 | Dimensione del batch |
| ubatch_size | 512 | Dimensione del micro-batch |
| flash_attention | auto | Flash Attention automatica |
| kv_cache | q4_0 | Quantizzazione della cache KV (kv-unified unificato) |
| poll | 0 | Nessun polling GPU in idle, efficiente dal punto di vista energetico e bassa latenza |
| reasoning | on | Abilita catena di ragionamento |
| reasoning_budget | 400 | Numero di token del budget di inferenza |
| reasoning_format | deepseek-legacy | Formato di inferenza |
| samplers | top_k;top_p;temperature;typ_p | Ordine dei campionatori |

### Consigli per diverse configurazioni di VRAM

Poiché le configurazioni delle schede grafiche degli utenti variano notevolmente, ecco i parametri consigliati per diverse dimensioni di VRAM (tutti per la versione MoziSmartBit):

| VRAM | Lunghezza del contesto consigliata | Cache KV | Supporto visivo | Descrizione |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | Supportato | Modello + visivo totale ~16,4 GB, test pratico: 128K + visivo occupano solo ~19,5 GB di VRAM |
| 24 GB | 256K completo | q4_0 | Perfettamente supportato | Visivo + contesto lungo 256K, occupa solo ~20,4 GB di VRAM, ~3,6 GB di riserva VRAM |
| 32 GB+ | 256K completo | q4_0 | Perfettamente supportato | Visivo + contesto lungo 256K, riserva VRAM sufficiente ~10 GB, configurazione più potente |

**Tabella di riferimento schede grafiche NVIDIA**

| VRAM | Modello scheda grafica |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**Tabella di riferimento schede grafiche AMD**

| VRAM | Modello scheda grafica |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Tabella di riferimento schede grafiche Intel**

| VRAM | Modello scheda grafica |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (richiede offloading CPU) |

**Tabella di riferimento dispositivi con GPU integrata e memoria condivisa CPU**

| VRAM | Modello processore |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395 (GPU integrata Radeon 8060S) |
| 128 GB | NVIDIA RTX Spark (GPU RTX Blackwell) |

> 💡 **Suggerimento**: Finché la VRAM soddisfa i requisiti di cui sopra, può essere utilizzato – nessuna restrizione su marca o modello. Supporta schede grafiche dedicate NVIDIA / AMD / Intel, nonché GPU integrate / CPU con 128 GB di memoria unificata.
>
> 💡 **Suggerimento**: Più lungo è il contesto, più VRAM viene occupata. Se la VRAM è insufficiente (OOM), ridurre gradualmente il valore del parametro `-c`. Con il parametro `--fit on`, llama.cpp può regolare automaticamente il numero di livelli per adattarsi alla VRAM.

### Distribuzione Ollama

```bash
# Crea un Modelfile
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# Crea ed esegui
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### Distribuzione LM Studio / Jan

Cerca direttamente `moziAI-35B` in LM Studio o Jan e seleziona la versione quantizzata per il download.

## Valutazione di riferimento

MoziAI-35B-V3.6 è basato sul modello base **Ornith-1.0-35B** (deepreinforce-ai) ed è stato affinato. Basandosi sulle eccellenti capacità di codifica degli agenti del modello base, MoziAI ha aggiunto un'**ottimizzazione approfondita del settore finanziario**, offrendo prestazioni migliori in scenari come domande e risposte finanziarie, programmazione quantitativa e chiamate di strumenti. Le capacità generali sono coerenti con quelle del modello base Ornith-1.0-35B.

| Benchmark                         | MoziAI-35B-V3.6 (questo modello) | Qwen3.5-35B | Qwen3.6-35B | Gemma4-31B | Qwen3.5-397B | Descrizione             |
| -------------------------------- | ------------------------- | ----------- | ----------- | ---------- | ------------ | ---------------- |
| **Codifica agente**                   |                           |             |             |            |              |                  |
| Terminal-Bench 2.1 (Terminus-2)  | 64.2                      | 41.4        | 52.5        | 42.1       | 53.5         |                  |
| Terminal-Bench 2.1 (Claude Code) | 62.8                      | 38.9        | 49.2        | -          | 48.6         |                  |
| SWE-bench Verified               | 75.6                      | 70          | 73.4        | 52         | 76.4         |                  |
| SWE-bench Pro                    | 50.4                      | 44.6        | 49.5        | 35.7       | 51.6         |                  |
| SWE-bench Multilingual           | 69.3                      | 60.3        | 67.2        | 51.7       | 69.3         |                  |
| NL2Repo                          | 34.6                      | 20.5        | 29.4        | 15.5       | 36.8         |                  |
| Claw-eval Avg                    | 69.8                      | 65.4        | 68.7        | 48.5       | 70.7         |                  |
| SWE Atlas - QnA                  | 37.1                      | 13.2        | 15.5        | -          | 20.4         |                  |
| SWE Atlas - RF                   | 29.7                      | 10.2        | 11.4        | -          | 18.4         |                  |
| SWE Atlas - TW                   | 27.8                      | 9.8         | 13.3        | -          | 18.5         |                  |
| LiveCodeBench v6                 | -                         | -           | 83.9        | 80.0       | -            |                  |
| GPQA Diamond                     | -                         | -           | 87.8        | 84.3       | -            |                  |
| AIME 2026 Matematica             | -                         | -           | 94.1        | 89.2       | -            |                  |

\* **Terminal-Bench 2.1 (Terminus-2)**: Valutato con il framework Harbor/Terminus-2, configurazione `parser=json`, `temperature=1.0`, `top_p=1.0`, finestra di contesto 128K. Ogni esecuzione ha un timeout di 4 ore, 32 core, 48 GB di RAM, il risultato è la media di 5 esecuzioni.  
\* **Terminal-Bench 2.1 (Claude Code)**: Valutato con Claude Code 2.1.126, configurazione `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. Il risultato è la media di 5 esecuzioni.  
\* **SWE-bench Verified, Pro e Multilingual**: Valutati con il framework OpenHands, configurazione `temp=1.0`, `top_p=0.95`, finestra di contesto 256K.  
\* **NL2Repo**: Configurazione `temperature=1.0`, `top_p=1.0`, contesto 400K, output 48K.  

> MoziAI-35B eredita completamente le eccellenti capacità di codifica degli agenti di Ornith-1.0-35B. La differenza chiave di MoziAI risiede nell'**ottimizzazione approfondita del settore finanziario**. In scenari come l'analisi dei rapporti finanziari, le strategie quantitative, la gestione del rischio e la conformità e le chiamate di strumenti per agenti, le prestazioni sono nettamente migliori rispetto ai modelli generali.

## Parole chiave SEO

Grande modello AI finanziario, grande modello AI, modello open-source locale, modello edge, programmazione quantitativa, MoziSmartBit, quantizzazione intelligente, quantizzazione GGUF, modello MoE, grande modello open-source locale, distribuzione locale, AI finanziaria, chiamate di strumenti, Agent, llama.cpp, Ollama, GGUF, Uncensored (senza censura), nessuna censura, senza censura, output libero, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.0-35B, Qwen3.5-35B-A3B, Qwen3.6-35B-A3B, verticale finanziaria, modello open-source.

## Licenza (importante)

Questo modello utilizza una **licenza restrittiva personalizzata**, i termini dettagliati sono i seguenti:

✅ **Consentito**

- Uso commerciale gratuito: Può essere integrato gratuitamente nei tuoi prodotti o servizi commerciali
- Copia e distribuzione: Può essere copiato, scaricato, distribuito così com'è

I termini di licenza dettagliati sono disponibili nel file [LICENSE](../LICENSE).

## Dichiarazione di non responsabilità

Questo modello è fornito "così com'è", senza garanzie di alcun tipo. L'output del modello è solo di riferimento e non costituisce un consiglio di investimento. L'utente si assume il rischio di utilizzo.

## Contatti

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

***

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
