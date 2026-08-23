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

[English](README.en.md) | [ä¸­æ](README.md)

## Panoramica del Modello

MoziAI-35B-A35B-MOE Ã¨ un LLM multimodale finanziario AI open-source locale (supporta vision e tool calling) sviluppato dal team dell'influencer finanziario cinese Chen Yumo, fine-tuned/distillato dal modello di base Ornith-1.5-35B-A3B (**architettura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, licenza MIT). Grazie alla tecnologia **MoziSmartBit Intelligent Quantization** sviluppata internamente, il modello MoE da 35B parametri Ã¨ compresso a circa **15,5 GB**, raggiungendo un equilibrio ottimale tra precisione e dimensione con qualitÃ  di precisione quasi integra ~99%.

Oltre a mantenere le capacitÃ  AI generali, questo modello si concentra sull'ottimizzazione delle applicazioni verticali nel dominio finanziario, includendo Q&A finanziari, programmazione quantitativa, tool calling e programmazione generale.

Lo sviluppatore Chen Yumo utilizza regolarmente questo modello per l'analisi dati finanziari locali, lo sviluppo e la ricerca di strategie quantitative, la ricerca di mercato, la redazione di articoli, la gestione complessiva dei progetti, la programmazione generale e compiti con contesto di 256K tramite openclaw/hermes. PuÃ² essere distribuito localmente su GPU di fascia consumer, risparmiando costosi token cloud, ottenendo libertÃ  di token 7x24 garantendo al contempo la privacy e la sicurezza dei dati locali.

Supporta llama.cpp, Ollama, LM Studio e altri framework di inferenza mainstream.

**Data di rilascio: 2026-08-21** | **Versione: V3.7**

## Caratteristiche del Modello

- **Focus sul Verticale Finanziario**: Ottimizzazione profonda per Q&A finanziari, programmazione quantitativa e tool calling
- **MoziSmartBit Intelligent Quantization**: Quantizzazione intelligente proprietaria, miglior equilibrio tra precisione e dimensione, compresso a circa **15,5 GB**
- **Distribuzione su Hardware Consumer**: Distribuibile su GPU consumer con 20GB o 24GB+ di VRAM, supporta contesto lungo di 256K
- **Supporto Multilingue**: 201 lingue e dialetti, con capacitÃ  cinesi potenziate, copre inglese/giapponese/tedesco/francese/spagnolo/portoghese e altre
- **Programmazione Generale**: Sviluppo full-stack, debug del codice, architettura, scripting, copre Python/JS/TS/Go/Rust e altre lingue mainstream
- **Redazione Articoli**: Scrittura di alta qualitÃ  in multipli generi inclusi report di ricerca, articoli di analisi, documentazione tecnica, contenuti creativi
- **Comprensione Vision**: Supporta vision multimodale, input da screenshot locali, comprensione di immagini
- **Output Uncensored Libero**: Nessuna censura dei contenuti, discussione libera su qualsiasi argomento senza restrizioni di sicurezza
- **Reasoning Potenziato**: Addestramento a catena del pensiero per una qualitÃ  di reasoning migliorata
- **Supporto Multi-Framework**: Compatibile con llama.cpp, Ollama, LM Studio, Jan
- **Supporto Multi-Piattaforma Agent**: Integrazione profonda con OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex e altri IDE AI mainstream e framework Agent, supporto nativo per tool calling e orchestrazione multi-turn, pronto all'uso

## Vantaggi Uncensored

Questo modello eredita la funzionalitÃ  **Uncensored** dal modello base Ornith-1.5-35B-A3B, con i seguenti vantaggi:

| Vantaggio | Descrizione |
|-----------|-------------|
| **Nessuna Censura** | Non rifiuterÃ  alcun argomento, contenuti sensibili o controversi inclusi |
| **Output Libero** | Non vincolato da politiche di sicurezza, puÃ² generare qualsiasi tipo di risposta |
| **Informazioni Complete** | Fornisce informazioni complete e non filtrate, adatte per ricerca e analisi |
| **Privacy Locale** | La distribuzione locale garantisce che i dati siano completamente privati e liberi dalla censura cloud |

> **Casi d'uso**: Ricerca accademica, analisi approfondita, discussione libera, conversazione AI senza restrizioni.
> **Nota**: Questo Ã¨ un modello distribuito localmente, il contenuto dell'output Ã¨ completamente controllato dall'utente, senza responsabilitÃ  di moderazione dei contenuti.

## CapacitÃ  Principali

| Area di CapacitÃ  | Descrizione |
|------------------|-------------|
| Analisi di Mercato | Interpretazione macro/microeconomica, logica dei mercati azionari (A-share/HK/US), commodities, crypto |
| Report Finanziari | Interpretazione degli indicatori finanziari chiave, sintesi dei report di ricerca, assistenza a valutazioni e previsioni di utili |
| Rischio e ConformitÃ  | Valutazione del rischio dei prodotti, conformitÃ  dei consigli di investimento, interpretazione delle normative finanziarie |
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
| VelocitÃ  di Inferenza | Ottimizzazione algoritmica: 140+ token/s su GPU AMD R9700, 70+ token/s su CPU AMD MAX+395 iGPU, libertÃ  di token locale |
| Team | Team Chen Yumo |

## Confronto Formati di Quantizzazione e Dimensione Modello

| Formato di Quant | Dimensione Modello | Precisione | Note |
|------------------|--------------------|------------|------|
| **FP16 (originale)** | ~70 GB | 100% | Originale 16bit |
| **MoziSmartBit** | **~15,5 GB** | **~99%** | **Usato da MoziAI, schema di quantizzazione ottimale** |
| Q4_K_M | ~22 GB | ~98% | Standard GGUF 4bit |
| Q5_K_M | ~24,7 GB | ~99% | QualitÃ  superiore |
| Q6_K | ~28,5 GB | ~99,5% | Quasi senza perdita |
| Q8_0 | ~36,9 GB | ~100% | Senza perdita |

> MoziAI V3.7 utilizza MoziSmartBit Intelligent Quantization, mantenendo ~99% di precisione comprimendo il modello MoE da 35B parametri a ~15,5 GB (~4,5x rapporto di compressione), bilanciando qualitÃ  di inferenza e accessibilitÃ  di distribuzione per GPU consumer.

## MoziSmartBit Intelligent Quantization

La quantizzazione tradizionale utilizza una precisione uniforme su tutti i livelli. **MoziSmartBit Intelligent Quantization** applica strategie di quantizzazione differenziate per il miglior equilibrio dimensione-precisione.

### Effetto di Compressione

La quantizzazione tradizionale comprime tutte le parti del modello in modo uniforme, portando spesso a una significativa perdita di precisione. MoziSmartBit Intelligent Quantization utilizza una strategia di compressione intelligente proprietaria che **raggiunge una significativa riduzione dimensionale con perdita di precisione minima**:

- **Perdita di Quantizzazione Minima**: Guadagni dell'addestramento > perdita di quantizzazione. Il modello MoziAI-35B addestrato raggiunge un PPL migliore sul testo del dominio finanziario rispetto al modello base bf16 pre-addestrato, riducendo allucinazioni e perplessitÃ  rispetto a modelli AI simili
- **~4,5x Riduzione Dimensionale**: Compresso da ~70 GB (FP16) a ~15,5 GB, anche significativamente piÃ¹ piccolo di Q4_K_M (~21 GB), riducendo notevolmente i requisiti di VRAM e spazio di archiviazione
- **Compatibile con GPU Consumer**: Un modello MoE da 35B che in precedenza richiedeva GPU di fascia alta ora puÃ² funzionare fluidamente su 20GB~24GB di VRAM

### Vantaggi Comparativi

**vs Q4_K_M (~22 GB)**: ~30% piÃ¹ piccolo (~15,5 GB), con precisione **superiore** a Q4_K_M, soglia VRAM piÃ¹ bassa â?funziona fluidamente su GPU consumer di fascia media (24GB).

**vs FP16 originale (~70 GB)**: ~4,5x compressione, addestramento efficace + perdita di quantizzazione minima (guadagni dell'addestramento > perdita di quantizzazione), abilitando la distribuzione locale con contesto di 256K su GPU consumer anzichÃ© hardware di livello professionale.

## Parametri di Inferenza Consigliati

Basati sulla configurazione di produzione locale (AMD Radeon AI PRO R9700 32GB):

| Parametro | Valore | Descrizione |
|-----------|--------|-------------|
| temperature | 0.6 | Bilanciamento tra creativitÃ  e accuratezza |
| top_p | 0.95 | Soglia di nucleus sampling |
| top_k | 20 | Truncation sampling (ottimizzato in V3.7) |
| repeat_penalty | 1.05 | PenalitÃ  per ripetizione |
| presence_penalty | 0 | Nessuna penalitÃ  di presenza |
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

> ð¡ **Suggerimento**: PurchÃ© la vostra VRAM soddisfi i requisiti sopra indicati, funziona. Nessuna restrizione di marca o modello. Supporta GPU discrete NVIDIA / AMD / Intel, e anche le iGPU a memoria unificata da 128GB sopra elencate.

> ð¡ **Suggerimento**: Un contesto piÃ¹ lungo utilizza piÃ¹ VRAM. Se riscontrate OOM (out of memory), riducete gradualmente il valore di `-c`. Usate `--fit on` per far aggiustare automaticamente i livelli da llama.cpp in base alla vostra VRAM.

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

MoziAI Ã¨ fine-tuned da **deepreinforce-ai/Ornith-1.5-35B-A3B**. MoziAI Ã¨ ottimizzato per i domini verticali finanziari sul modello base, offrendo prestazioni superiori negli scenari di Q&A finanziari, programmazione quantitativa e tool calling. Le capacitÃ  generali di MoziAI-35B sono coerenti con il modello base Ornith-1.5-35B-A3B.

| Benchmark | MoziAI-35B (questo modello) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | Descrizione |
|-----------|--------------------------|-------------|------------|------------|-------------|-------------|
| Terminal-Bench 2.1 | 64,2 | 59,3 | 42,1 | - | 41,4 | Programmazione terminale autonoma |
| Terminal-Bench (Claude Code) | 62,8 | 59,3 | - | - | 38,9 | Programmazione Claude Code |
| SWE-bench Verified | 75,6 | 77,2 | 52,0 | - | 70,0 | Ingegneria del software reale |
| SWE-bench Pro | 50,4 | 53,5 | 35,7 | - | 44,6 | Ingegneria del software complessa |
| SWE-bench Multilingual | 69,3 | 71,3 | - | - | 60,3 | Programmazione multilingue |
| NL2Repo | 34,6 | 36,2 | 15,5 | - | 20,5 | Linguaggio naturale a repo |
| LiveCodeBench v6 | 63,3 | 83,9 | 80,0 | 77,1 | - | Programmazione competitiva |
| GPQA Diamond | 88,4 | 87,8 | 84,3 | 82,3 | - | Reasoning scientifico |
| AIME 2026 Math | 93,3 | 94,1 | 89,2 | 88,3 | - | Reasoning matematico |

> I punteggi generali dei benchmark di MoziAI-35B sono coerenti con il modello base Ornith-1.5-35B-A3B. Il dominio verticale finanziario Ã¨ la direzione di ottimizzazione principale di MoziAI, superando significativamente i modelli generali in scenari come l'analisi di report finanziari, le strategie quantitative, rischio e conformitÃ  e tool calling degli agent. I dati di Gemma4 e Qwen3.6 provengono da risultati pubblici ufficiali.

## Download del Modello

A causa della grande dimensione del modello (~15,5 GB), i pesi sono ospitati su piattaforme community multiple:

| Piattaforma | URL |
|-------------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |


> ð¡ **LM Studio**: Puoi cercare e scaricare direttamente in [LM Studio](https://lmstudio.ai). Cerca `moziAI` e clicca Download.
> ð¡ **Suggerimento per il download**: Cliccate sul link sopra per andare al repository HuggingFace, poi andate alla scheda **"Files and versions"** per scaricare tutti i file nella directory V3.7 (modello principale, vision projection, chat template). Assicuratevi che tutti e tre i file siano nella stessa directory.

### â ï¸ Importante: La CapacitÃ  Vision Richiede il File mmproj

Questo modello supporta la vision multimodale. Il **file di vision projection (mmproj)** Ã¨ incluso nella directory della versione:

- **File vision**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, precisione BF16)
- **Posizionamento**: Nella stessa directory della versione del file modello GGUF
- **Caricamento**: Caricate con il flag `--mmproj` all'avvio di llama-server

```bash
llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf
```

> Senza il file vision, il modello **perderÃ  la capacitÃ  di comprensione delle immagini** e manterrÃ  solo la conversazione testuale.

## Avvio Rapido

### 1. Scarica i File del Modello

Scaricate tutti i file nella directory V3.7 da HuggingFace / ModelScope:

```
V3.7/
âââ moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # Modello principale (obbligatorio)
âââ moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # Vision projection (opzionale)
âââ moziAI-V3.7-35B-chat-template.jinja                  # Chat template (consigliato)
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

> Aggiungete `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` per la capacitÃ  vision.

### 3. Inizia a Utilizzare

Aprite `http://localhost:8080` nel browser per iniziare a chattare.

### Struttura Directory

```
moziAI-35B/
âââ README.md              # Versione cinese
âââ README.en.md           # Questo file (inglese)
âââ LICENSE                # Licenza
âââ V3.7/                  # Versione V3.7 (autonoma)
â?  âââ RELEASE_NOTES.md                       # Note di rilascio
â?  âââ moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # Modello principale
â?  âââ moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # Vision projection
â?  âââ moziAI-V3.7-35B-chat-template.jinja   # Chat template
```

Per il piano di aggiornamento futuro, consultate [æªæ¥åçº§è®¡å.md](æªæ¥åçº§è®¡å.md).

## Parole Chiave SEO

financial AI LLM, local open source model, end-side model, quant programming, MoziSmartBit, intelligent quantization, GGUF quantization, MoE model, local open source LLM, local deployment, financial AI, tool calling, Agent, llama.cpp, Ollama, GGUF, Uncensored, no censorship, free output, unrestricted, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, financial vertical domain, open source model

## Licenza (Importante)

Questo modello utilizza una **Licenza Personalizzata Restrittiva**:

### â?Consentito
- **Uso Commerciale Libero**: Libero di integrare in prodotti commerciali
- **Copia e Distribuzione**: Ã possibile copiare, scaricare e condividere

### â?Proibito
- **Opere Derivate**: Nessuna modifica, traduzione, adattamento, unione o fine-tuning del modello o di qualsiasi sua parte
- **Rivendita**: Nessuna vendita del modello da solo o come parte di un prodotto
- **Ri-licenza**: Nessuna concessione di sublicenze

### ð Requisiti
- Deve essere mantenuto l'avviso di copyright originale
- Attribuzione: moziAI-35B

> Consultate [LICENSE](./LICENSE) per i termini completi.

## Disclaimer

Fornito "cosÃ¬ com'Ã¨" senza garanzia. L'output del modello Ã¨ solo a scopo informativo, non costituisce consulenza finanziaria. Gli utenti assumono tutti i rischi.

## Contatti

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. Tutti i diritti riservati.
