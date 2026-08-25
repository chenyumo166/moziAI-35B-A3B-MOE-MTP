---

language:

- it

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



# MoziAI-V3.7-35B-A3B-MOE - IA multimodale compatta e potente, distribuibile gratuitamente in locale



[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | Italiano | [Русский](README.ru.md)



## Panoramica del Modello



MoziAI-35B-A3B-MOE è un LLM multimodale finanziario AI open-source locale (supporta vision e tool calling) sviluppato dal team dell'influencer finanziario cinese Chen Yumo. moziAI-35B è basato sul modello base open-source Ornith-1.5-35B-A3B (architettura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licenza MIT), integrando lo sviluppo autonomo del team Chen Yumo: (dati finanziari + capacità del dominio finanziario + metodi di addestramento + framework di pensiero a sette dimensioni + meccanismo LOOP dell'agente + algoritmo di quantizzazione ibrido MoziSmartBit). Attraverso la tecnologia di quantizzazione intelligente MoziSmartBit sviluppata internamente, il modello MoE da 35 miliardi di parametri viene compresso a circa 15,5 GB, ovvero 6,5 GB (circa 30%) in meno rispetto ai modelli di quantizzazione Q4_K_M convenzionali di circa 22+ GB; raggiungendo l'equilibrio ottimale tra precisione e dimensioni, con qualità di precisione quasi senza perdite di circa il 99% della FP16.



Oltre a mantenere le capacità AI generali, questo modello si concentra sull'ottimizzazione delle applicazioni verticali nel dominio finanziario, includendo Q&A finanziari, programmazione quantitativa, tool calling e programmazione generale.



Lo sviluppatore Chen Yumo utilizza regolarmente questo modello per l'analisi dati finanziari locali, lo sviluppo e la ricerca di strategie quantitative, la ricerca di mercato, la redazione di articoli, la gestione complessiva dei progetti, la programmazione generale e compiti con contesto di 256K tramite openclaw/hermes. Può essere distribuito localmente su GPU di fascia consumer, risparmiando costosi token cloud, ottenendo libertà di token 7x24 garantendo al contempo la privacy e la sicurezza dei dati locali.



Supporta llama.cpp, Ollama, LM Studio e altri framework di inferenza mainstream.



**Data di rilascio: 2026-08-21** | **Versione: V3.7**



## Caratteristiche del Modello



- **Focus sul Verticale Finanziario**: Ottimizzazione profonda per Q&A finanziari, programmazione quantitativa e tool calling

- **MoziSmartBit Intelligent Quantization**: Quantizzazione intelligente proprietaria, miglior equilibrio tra precisione e dimensione, compresso a circa **15,5 GB**

- **Distribuzione su Hardware Consumer**: Distribuibile su GPU consumer con 20GB o 24GB+ di VRAM, supporta contesto lungo di 256K

- **Supporto Multilingue**: 201 lingue e dialetti, con capacità cinesi potenziate, copre inglese/giapponese/tedesco/francese/spagnolo/portoghese e altre

- **Programmazione Generale**: Sviluppo full-stack, debug del codice, architettura, scripting, copre Python/JS/TS/Go/Rust e altre lingue mainstream

- **Redazione Articoli**: Scrittura di alta qualità in multipli generi inclusi report di ricerca, articoli di analisi, documentazione tecnica, contenuti creativi

- **Comprensione Vision**: Supporta vision multimodale, input da screenshot locali, comprensione di immagini

- **Output Uncensored Libero**: Nessuna censura dei contenuti, discussione libera su qualsiasi argomento senza restrizioni di sicurezza

- **Reasoning Potenziato**: Addestramento a catena del pensiero per una qualità di reasoning migliorata

- **Supporto Multi-Framework**: Compatibile con llama.cpp, Ollama, LM Studio, Jan

- **Supporto Multi-Piattaforma Agent**: Integrazione profonda con OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex e altri IDE AI mainstream e framework Agent, supporto nativo per tool calling e orchestrazione multi-turn, pronto all'uso



## Vantaggi Uncensored



Questo modello eredita la funzionalità **Uncensored** dal modello base Ornith-1.5-35B-A3B, con i seguenti vantaggi:



| Vantaggio | Descrizione |
|-----------|-------------|
| **Nessuna Censura** | Non rifiuterà alcun argomento, contenuti sensibili o controversi inclusi |
| **Output Libero** | Non vincolato da politiche di sicurezza, può generare qualsiasi tipo di risposta |
| **Informazioni Complete** | Fornisce informazioni complete e non filtrate, adatte per ricerca e analisi |
| **Privacy Locale** | La distribuzione locale garantisce che i dati siano completamente privati e liberi dalla censura cloud |
> **Casi d'uso**: Ricerca accademica, analisi approfondita, discussione libera, conversazione AI senza restrizioni.

> **Nota**: Questo è un modello distribuito localmente, il contenuto dell'output è completamente controllato dall'utente, senza responsabilità di moderazione dei contenuti.



## Capacità Principali



| Area di Capacità | Descrizione |
|------------------|-------------|
| Analisi di Mercato | Interpretazione macro/microeconomica, logica dei mercati azionari (A-share/HK/US), commodities, crypto |
| Report Finanziari | Interpretazione degli indicatori finanziari chiave, sintesi dei report di ricerca, assistenza a valutazioni e previsioni di utili |
| Rischio e Conformità | Valutazione del rischio dei prodotti, conformità dei consigli di investimento, interpretazione delle normative finanziarie |
| Quant e Strategia | Progettazione di strategie quantitative, quantizzazione Pyramid (PEL), logica di backtesting, costruzione di fattori e tool calling |
| Tool Calling | Integrazione con quotazioni in tempo reale, database, recupero report di ricerca e altre fonti dati finanziarie |
## Specifiche Tecniche



| Elemento | Specifica |
|----------|-----------|
| Modello Base | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, licenza MIT) |
| Parametri | 35B MoE (256 esperti instradati + 1 esperto condiviso, 8 attivi per token) |
| Quantizzazione | MoziSmartBit Intelligent Quantization proprietaria + formato standard GGUF |
| Lunghezza Contesto | 256K (262.144 token) |
| Dimensione Modello | ~15,5 GB (versione MoziSmartBit Uncensored) |
| VRAM Minima | GPU consumer con 20GB+ di VRAM (es. RTX 4060 Ti 16G con CPU offload), 24 GB consigliati (con vision + contesto lungo) |
| Framework di Inferenza | llama.cpp / Ollama / LM Studio / Jan |
| Velocità di Inferenza | Ottimizzazione algoritmica: 140+ token/s su GPU AMD R9700, 70+ token/s su CPU AMD MAX+395 iGPU, libertà di token locale |
| Team | Team Chen Yumo |
## Confronto Formati di Quantizzazione e Dimensione Modello



| Formato di Quant | Dimensione Modello | Precisione | Note |
|------------------|--------------------|------------|------|
| **FP16 (originale)** | ~70 GB | 100% | Originale 16bit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Usato da MoziAI, schema di quantizzazione ottimale** |
| Q4_K_M | ~22 GB | ~98% | Standard GGUF 4bit |
| Q5_K_M | ~24,7 GB | ~99% | Qualità superiore |
| Q6_K | ~28,5 GB | ~99,5% | Quasi senza perdita |
| Q8_0 | ~36,9 GB | ~100% | Senza perdita |
> MoziAI V3.7 utilizza MoziSmartBit Intelligent Quantization, mantenendo ~99% di precisione comprimendo il modello MoE da 35B parametri a ~15,5 GB (~4,5x rapporto di compressione), bilanciando qualità di inferenza e accessibilità di distribuzione per GPU consumer.



## MoziSmartBit Intelligent Quantization



La quantizzazione tradizionale utilizza una precisione uniforme su tutti i livelli. **MoziSmartBit Intelligent Quantization** applica strategie di quantizzazione differenziate per il miglior equilibrio dimensione-precisione.



### Effetto di Compressione



La quantizzazione tradizionale comprime tutte le parti del modello in modo uniforme, portando spesso a una significativa perdita di precisione. MoziSmartBit Intelligent Quantization utilizza una strategia di compressione intelligente proprietaria che **raggiunge una significativa riduzione dimensionale con perdita di precisione minima**:



- **Perdita di Quantizzazione Minima**: Guadagni dell'addestramento > perdita di quantizzazione. Il modello MoziAI-35B addestrato raggiunge un PPL migliore sul testo del dominio finanziario rispetto al modello base bf16 pre-addestrato, riducendo allucinazioni e perplessità rispetto a modelli AI simili

- **~4,5x Riduzione Dimensionale**: Compresso da ~70 GB (FP16) a ~15,5 GB, anche significativamente più piccolo di Q4_K_M (~21 GB), riducendo notevolmente i requisiti di VRAM e spazio di archiviazione

- **Compatibile con GPU Consumer**: Un modello MoE da 35B che in precedenza richiedeva GPU di fascia alta ora può funzionare fluidamente su 20GB~24GB di VRAM



### Vantaggi Comparativi



**vs Q4_K_M (~21,2 GB)** : ~30% più piccolo (~15,5 GB), con precisione **superiore** a Q4_K_M, soglia VRAM più bassa → funziona fluidamente su GPU consumer 20 GB, risparmia ~55% VRAM vs Q4_K_M



**vs FP16 originale (~70 GB)**: ~4,5x compressione, addestramento efficace + perdita di quantizzazione minima (guadagni dell'addestramento > perdita di quantizzazione), abilitando la distribuzione locale con contesto di 256K su GPU consumer anziché hardware di livello professionale.



## Parametri di Inferenza Consigliati



Basati sulla configurazione di produzione locale (AMD Radeon AI PRO R9700 32GB):



| Parametro | Valore | Descrizione |
|-----------|--------|-------------|
| temperature | 0.6 | Bilanciamento tra creatività e accuratezza |
| top_p | 0.95 | Soglia di nucleus sampling |
| top_k | 20 | Truncation sampling (ottimizzato in V3.7) |
| repeat_penalty | 1.05 | Penalità per ripetizione |
| presence_penalty | 0 | Nessuna penalità di presenza |
| context_length | 262144 | Contesto lungo 256K |
| batch_size | 2048 | Dimensione del batch |
| ubatch_size | 512 | Dimensione del micro-batch |
| flash_attention | auto | Flash Attention automatico |
| kv_cache | q4_0 | Quantizzazione del KV cache (kv-unified) |
| poll | 0 | Nessun polling GPU a riposo, efficiente energeticamente |
| reasoning | on | Abilita catena del reasoning (chain of thought) |
| reasoning_budget | 4096 | Budget di reasoning in token |
| reasoning_format | deepseek-legacy | Formato di reasoning |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | Ordine dei sampler |
### Comando di Avvio llama.cpp



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 262144 -ngl 99 -t 28 \

  --batch-size 2048 --ubatch-size 512 \

  --flash-attn auto \

  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \

  --poll 0 --reasoning on --reasoning-budget 1000 \

  --host 0.0.0.0 --port 8080 \

  --temp 0.6 --top-p 0.95 --top-k 20

```



### Raccomandazioni Configurazione VRAM



Dato che le configurazioni GPU degli utenti variano ampiamente, ecco i parametri consigliati per diverse dimensioni di VRAM (tutti per la versione MoziSmartBit):



| VRAM | Contesto Consigliato | KV Cache | Supporto Vision | Note |
|------|---------------------|----------|-----------------|------|
| 20 GB | 150K | q4_0 | Supportato | Modello+vision ~16,4GB, test effettivo mostra 200K+vision utilizza ~19,5GB VRAM |
| 24 GB | 256K completo | q4_0 | Supporto completo | Vision+contesto lungo 256K, utilizza ~20,4GB VRAM, ~3,6GB di margine |
| 32 GB+ | 256K completo | q4_0 | Supporto completo | Vision+contesto lungo 256K, margine sufficiente ~10GB, configurazione migliore |
**NVIDIA**



| VRAM | Modello GPU |
|------|-------------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |
**AMD**



| VRAM | Modello GPU |
|------|-------------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |
**Intel**



| VRAM | Modello GPU |
|------|-------------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (richiede CPU offload) |
**iGPU con Memoria Condivisa**



| VRAM | Processore |
|------|-----------|
| 128 GB | AMD Ryzen AI Max+ 395 (iGPU Radeon 8060S) |
| 128 GB | NVIDIA RTX Spark (GPU Blackwell RTX) |
> 💡 **Suggerimento**: Purché la vostra VRAM soddisfi i requisiti sopra indicati, funziona. Nessuna restrizione di marca o modello. Supporta GPU discrete NVIDIA / AMD / Intel, e anche le iGPU a memoria unificata da 128GB sopra elencate.



> 💡 **Suggerimento**: Un contesto più lungo utilizza più VRAM. Se riscontrate OOM (out of memory), riducete gradualmente il valore di `-c`. Usate `--fit on` per far aggiustare automaticamente i livelli da llama.cpp in base alla vostra VRAM.



### Distribuzione con Ollama



```bash

# Crea il Modelfile

FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf



PARAMETER temperature 0.6

PARAMETER top_p 0.95

PARAMETER top_k 20

PARAMETER num_ctx 262144

PARAMETER num_gpu 99



# Costruisci ed esegui

ollama create moziAI-35B -f Modelfile

ollama run moziAI-35B

```



### Distribuzione con LM Studio / Jan



Cercate `moziAI-35B` in LM Studio o Jan, scaricate la versione quant MoziSmartBit.



## Valutazione Benchmark



MoziAI è fine-tuned da **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI è ottimizzato per i domini verticali finanziari sul modello base, offrendo prestazioni superiori negli scenari di Q&A finanziari, programmazione quantitativa e tool calling. Le capacità generali di MoziAI-35B sono coerenti con il modello base Ornith-1.5-35B-A3B.



| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programmazione** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Ragionamento** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Agentico** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |
> I punteggi generali dei benchmark di MoziAI-35B sono coerenti con il modello base Ornith-1.5-35B-A3B. Il dominio verticale finanziario è la direzione di ottimizzazione principale di MoziAI, superando significativamente i modelli generali in scenari come l'analisi di report finanziari, le strategie quantitative, rischio e conformità e tool calling degli agent. I dati di Gemma4 e Qwen3.6 provengono da risultati pubblici ufficiali.



## Download del Modello



A causa della grande dimensione del modello (~15,5 GB), i pesi sono ospitati su piattaforme community multiple:



| Piattaforma | URL |
|-------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio**: Puoi cercare e scaricare direttamente in [LM Studio](https://lmstudio.ai). Cerca `moziAI` e clicca Download.

> 💡 **Suggerimento per il download**: Cliccate sul link sopra per andare al repository HuggingFace, poi andate alla scheda **"Files and versions"** per scaricare tutti i file nella directory V3.7 (modello principale, vision projection, chat template). Assicuratevi che tutti e tre i file siano nella stessa directory.



### ⚠️ Importante: La Capacità Vision Richiede il File mmproj



Questo modello supporta la vision multimodale. Il **file di vision projection (mmproj)** è incluso nella directory della versione:



- **File vision**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, precisione BF16)

- **Posizionamento**: Nella stessa directory della versione del file modello GGUF

- **Caricamento**: Caricate con il flag `--mmproj` all'avvio di llama-server



```bash

llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf

```



> Senza il file vision, il modello **perderà la capacità di comprensione delle immagini** e manterrà solo la conversazione testuale.



## Avvio Rapido



### 1. Scarica i File del Modello



Scaricate tutti i file nella directory V3.7 da HuggingFace / ModelScope:



```

V3.7/

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # Modello principale (obbligatorio)

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision projection (opzionale)

└── moziAI-V3.7-35B-chat-template.jinja                  # Chat template (consigliato)

```



### 2. Avvia il Server di Inferenza



Per la configurazione completa consigliata, consultate il [Comando di Avvio llama.cpp](#comando-di-avvio-llamacpp) sopra.



Avvio minimo (solo parametri fondamentali):



```bash

llama-server \

  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \

  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \

  -c 262144 -ngl 99

```



> Aggiungete `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` per la capacità vision.



### 3. Inizia a Utilizzare



Aprite `http://localhost:8080` nel browser per iniziare a chattare.



### Struttura Directory



```

moziAI-35B/

├── README.md              # Versione cinese

├── README.en.md           # Questo file (inglese)

├── LICENSE                # Licenza

├── V3.7/                  # Versione V3.7 (autonoma)

├── RELEASE_NOTES.md                       # Note di rilascio

├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # Modello principale

├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision projection

└── moziAI-V3.7-35B-chat-template.jinja   # Chat template

```



Per il piano di aggiornamento futuro, consultate [未来升级计划.md](未来升级计划.md).



## Parole Chiave SEO



financial AI LLM, local open source model, end-side model, quant programming, MoziSmartBit, intelligent quantization, GGUF quantization, MoE model, local open source LLM, local deployment, financial AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, no censorship, free output, unrestricted, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, financial vertical domain, open source model



## Licenza (Importante)



Questo modello utilizza una **Licenza Personalizzata Restrittiva**:



### ✅ Consentito

- **Uso Commerciale Libero**: Libero di integrare in prodotti commerciali

- **Copia e Distribuzione**: È possibile copiare, scaricare e condividere



### ✅ Vietato

- **Opere Derivate**: Nessuna modifica, traduzione, adattamento, unione o fine-tuning del modello o di qualsiasi sua parte

- **Rivendita**: Nessuna vendita del modello da solo o come parte di un prodotto

- **Ri-licenza**: Nessuna concessione di sublicenze



### 📋 Requisiti

- Deve essere mantenuto l'avviso di copyright originale

- Attribuzione: moziAI-35B



> Consultate [LICENSE](./LICENSE) per i termini completi.



## Disclaimer



Fornito "così com'è" senza garanzia. L'output del modello è solo a scopo informativo, non costituisce consulenza finanziaria. Gli utenti assumono tutti i rischi.



## Contatti



- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)

- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)

- **Weibo**: [@rimochen](https://weibo.com/rimochen)

- **E-mail**: 263515@qq.com



---



Copyright (c) 2026 Chen Yumo / chenyumo166. Tutti i diritti riservati.