---
language:
- pt
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

# MoziAI-35B-V3.8 — Um modelo de IA multimodal compacto e poderoso, gratuito para implantação local

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | Português | [Русский](README.ru.md) | [Español](README.es.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**Data de lançamento: 2026-09-01** · **Versão: V3.8**

---

## 📑 Índice

- [1. Visão geral do modelo](#1-visão-geral-do-modelo)
- [2. Características principais](#2-características-principais) — Pensamento dinâmico de sete dimensões / LOOP / MoziSmartBit / Foco em finanças
- [3. Notas de atualização](#3-notas-de-atualização)
- [4. Capacidades principais no domínio financeiro](#4-capacidades-principais-no-domínio-financeiro)
- [5. Especificações técnicas](#5-especificações-técnicas)
- [6. Início rápido](#6-início-rápido-3-arquivos-100-da-melhor-capacidade-de-inferência) — **Download dos 3 arquivos**
- [7. Download do modelo](#7-download-do-modelo)
- [8. Comandos de inicialização](#8-comandos-de-inicialização)
- [9. Parâmetros de inferência recomendados](#9-parâmetros-de-inferência-recomendados)
- [10. Comparação de formatos de quantização](#10-comparação-de-formatos-de-quantização)
- [11. Aceleração por decodificação especulativa](#11-aceleração-por-decodificação-especulativa-função-importante)
- [12. Recomendações de configuração de VRAM](#12-recomendações-de-configuração-de-vram)
- [13. Métodos de implantação](#13-métodos-de-implantação)
- [14. Benchmarks](#14-benchmarks)
- [15. Otimização Uncensored (sem censura)](#15-otimização-uncensored-sem-censura)
- [16. Licença](#16-licença)
- [17. Contatos](#17-contatos)

---

## 1. Visão geral do modelo

MoziAI-35B-V3.8 é um grande modelo de IA multimodal open-source para implantação local gratuita, desenvolvido pela equipe de Chen Yumo, influenciador financeiro chinês. Construído sobre o modelo base open-source **Ornith-1.5-35B-A3B** (arquitetura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, licença MIT), integra dados financeiros desenvolvidos internamente + capacidades do domínio financeiro + sistema de pensamento dinâmico de sete dimensões + mecanismo de iteração reflexiva LOOP do agente + característica Uncensored (sem censura) + algoritmo de quantização híbrida MoziSmartBit.

**💡 Vantagem de tamanho: apenas 15,9 GB** — O modelo MoE de 35 bilhões de parâmetros é comprimido para **15,9 GB** pela quantização inteligente MoziSmartBit (cerca de 30% menor que o Q4_K_M convencional de ~22 GB). Cabe em um único pacote de instalação: GPUs de consumo (a partir de 20 GB de VRAM) são suficientes para a implantação local, o custo de tokens em nuvem = 0, garantindo 7×24 horas de liberdade de tokens e a privacidade e a segurança dos dados locais. **Uso comercial gratuito** — acesso sem barreiras para pessoas físicas e empresas.

---

## 2. Características principais

### 🧠 Sistema de pensamento dinâmico de sete dimensões

O framework de raciocínio central desenvolvido internamente pela MoziAI. Diante de qualquer tarefa, o modelo primeiro emite o marcador **moziAI-Think** e, em seguida, expande dinamicamente o pensamento estruturado conforme a complexidade da tarefa:

| Nível | Cenário de uso | Tarefas típicas | Dimensões ativadas |
| --- | --- | --- | --- |
| **Nível 0** | Perguntas e respostas simples | Explicação de termos, consulta de fatos, tradução, resumo | ①Entender a tarefa ⑤Recursos necessários (resposta rápida em duas dimensões) |
| **Nível 1** | Análise e diagnóstico | Pesquisa de mercado, redação de textos, análise de dados, interpretação de relatórios, avaliação de estratégias | ①②③⑤⑥ Avaliação em cinco dimensões |
| **Nível 2** | Desenvolvimento/estratégia complexos | Desenvolvimento de código, design de arquitetura, desenvolvimento de estratégias quantitativas, fluxos de trabalho em várias etapas, design de sistemas | ①②③④⑤⑥⑦ Raciocínio profundo completo nas sete dimensões |

> Sete dimensões: ①Entender a tarefa ②Avaliar a complexidade ③Relações de dependência ④Avaliar riscos ⑤Recursos necessários ⑥Critérios de aceitação ⑦Estratégia de execução

### 🔄 Mecanismo de iteração LOOP do agente

Tarefas complexas entram automaticamente no modo de iteração **moziAI-Loop**: **1ª rodada de execução + avaliação → 2ª rodada de ajuste + validação**, garantindo que a saída passe por autocorreção antes de ser apresentada como resposta final. Como um engenheiro sênior, o modelo "decompõe o problema → avalia a solução → executa → reflete → otimiza", aumentando significativamente a precisão e a executabilidade de tarefas complexas. Para perguntas simples e tarefas rotineiras, o Loop é desativado automaticamente.

### 📦 Quantização inteligente MoziSmartBit

Quantização hierárquica inteligente desenvolvida internamente: o modelo MoE de 35 bilhões de parâmetros é comprimido para cerca de **15,9 GB** — aproximadamente 6,5 GB (~30%) menor que o Q4_K_M convencional (~22 GB) — mantendo **~99%** da precisão FP16. Enquanto a quantização tradicional aplica precisão uniforme a todas as camadas, a MoziSmartBit adota uma estratégia inteligente e diferenciada, com base nas características estruturais dos modelos MoE, alcançando precisão superior ao Q4_K_M. Taxa de compressão de **4,5x**.

### 💰 Foco no domínio financeiro vertical

Otimização profunda para perguntas e respostas financeiras, programação quantitativa e chamada de ferramentas. O setor financeiro tem tolerância extremamente baixa a alucinações de modelos; a MoziAI apresenta desempenho significativamente superior ao de modelos gerais de mesmo porte nesse domínio.

### 🛡️ Característica Uncensored (sem censura)

Sem restrições de moderação de conteúdo, saída livre, informações completas e privacidade local. Adequado para pesquisa acadêmica, análise aprofundada, discussão livre e outros cenários. (Consulte a [Seção 15](#15-otimização-uncensored-sem-censura))

### 🌐 Outras características

- **Suporte multilíngue**: 201 idiomas e dialetos, com capacidade em chinês especialmente otimizada
- **Programação geral**: desenvolvimento full-stack, depuração de código e design de arquitetura, cobrindo Python/JS/TS/Go/Rust
- **Redação de artigos**: produção de alta qualidade em múltiplos gêneros — relatórios de pesquisa, artigos de análise, documentação técnica, conteúdo criativo etc.
- **Compreensão visual**: visão multimodal, com suporte a capturas de tela locais para entender o conteúdo de imagens
- **Suporte a múltiplos frameworks**: llama.cpp / Ollama / LM Studio / Jan
- **Suporte a múltiplos agentes**: OpenClaw / Hermes / Cursor / Claude Code / Codex etc., com chamada nativa de ferramentas e orquestração de tarefas em várias etapas

---

## 3. Notas de atualização

Esta versão V3.8 foi retreinada com o mesmo sistema de datasets de treinamento de última geração usado no 27B-V3.8 (identidade / pensamento dinâmico de sete dimensões / iteração LOOP / domínio financeiro vertical), com foco em reforçar o modo de raciocínio proprietário da moziAI — pensamento dinâmico de sete dimensões + iteração LOOP — tornando o reconhecimento da complexidade das tarefas mais inteligente, elevando a taxa de conclusão de tarefas complexas e fortalecendo a capacidade de "pensar antes de agir"; ao mesmo tempo, mantém a característica Uncensored (sem censura) e a otimização profunda no domínio financeiro vertical.

A moziAI mantém um ritmo ativo de atualizações e iterações de versão, garantindo o acompanhamento próximo da evolução futura da inteligência artificial e, continuamente, por meio de tecnologia proprietária, tornando os modelos de IA locais mais leves de implantar e cada vez mais capazes.

---

## 4. Capacidades principais no domínio financeiro

| Área de capacidade | Descrição |
| --- | --- |
| Análise de mercado | Interpretação macroeconômica e microeconômica, análise de mercado e lógica de movimentação de ações chinesas (A-shares), de Hong Kong e dos EUA, commodities e criptomoedas |
| Finanças e relatórios | Interpretação dos principais indicadores de demonstrações financeiras, extração de resumos de relatórios de pesquisa, suporte a valuation e projeção de lucros |
| Gestão de risco e compliance | Avaliação de risco de produtos, alertas de conformidade para recomendações de investimento, interpretação de políticas regulatórias financeiras |
| Quant e estratégias | Concepção de ideias de estratégias quantitativas, quantificação Pyramid (Pyramid/PEL), lógica de backtest, construção de fatores e chamada de ferramentas |
| Chamada de ferramentas | Integração de fontes de dados financeiros, como cotações em tempo real, bancos de dados e busca de relatórios de pesquisa |

---

## 5. Especificações técnicas

| Item | Parâmetro |
| --- | --- |
| Modelo base | Ornith-1.5-35B-A3B (arquitetura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licença MIT) |
| Escala de parâmetros | 35 bilhões (35B) em arquitetura MoE, 256 especialistas roteados + 1 especialista compartilhado, 8 especialistas ativados por token |
| Quantização | Quantização inteligente MoziSmartBit proprietária + formato padrão GGUF |
| Comprimento do contexto | 256K (262.144 tokens) |
| Tamanho do modelo | ~15,9 GB |
| VRAM mínima | **20GB+** implantável (offload de CPU); **24GB+** contexto longo fluido; **32GB+** 256K completo + visão |
| Frameworks de inferência | llama.cpp / Ollama / LM Studio / Jan |
| Velocidade de inferência | Com decodificação especulativa: **140+ token/s** na GPU AMD R9700 / **70+ token/s** na iGPU da CPU AMD MAX+395, garantindo liberdade total de tokens com saída local |
| Equipe de desenvolvimento | Equipe Chen Yumo |

---

## 6. Início rápido 3 arquivos 100 da melhor capacidade de inferência

> ⚠️ **Dica essencial**: a melhor capacidade de inferência da MoziAI exige o download **simultâneo dos 3 arquivos** — modelo principal, projeção visual e template de chat. A ausência de qualquer um deles compromete a capacidade correspondente.

### 6.1 Baixar os arquivos do modelo

Baixe **estes 3 arquivos** no HuggingFace / ModelScope para o mesmo diretório local (o modelo principal fica na **raiz do repositório**, a projeção visual em `mmproj/35B/` e o template de chat em `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Modelo principal (obrigatório, 15,9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Projeção visual (obrigatório, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Template de chat (obrigatório, contém instruções de pensamento 7D + Loop)
```

| Arquivo | Tamanho | Necessidade | Função |
| --- | --- | --- | --- |
| Modelo principal `.gguf` | ~15,9 GB | **Obrigatório** | Pesos do modelo; capacidade central de inferência |
| Projeção visual `mmproj` | ~1 GB | **Obrigatório** | Compreensão visual multimodal; sem ele, a capacidade de imagem é perdida |
| Template de chat `.jinja` | Mínimo | **Obrigatório** | Injeta a identidade da MoziAI + instruções do mecanismo de pensamento 7D + LOOP |

### 6.2 Iniciar e usar

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Abra `http://localhost:8080` no navegador para começar a conversar. Veja os parâmetros completos recomendados na Seção 9.

---

## 7. Download do modelo

| Plataforma | Endereço |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Usuários do LM Studio**: pesquise `moziAI` no [LM Studio](https://lmstudio.ai) e baixe com um clique, sem precisar baixar os arquivos manualmente.

> 💡 **Dica de download**: clique no link acima para acessar o repositório do HuggingFace; na aba **"Files and versions"**, baixe o modelo principal na **raiz do repositório**, a projeção visual na pasta `mmproj/35B/` e o template de chat na pasta `V3.8/`, garantindo que os três arquivos fiquem no mesmo diretório.

---

## 8. Comandos de inicialização

### Inicialização mínima (com os 3 arquivos)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Inicialização completa recomendada

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

> 💡 Se a VRAM for insuficiente: reduza `-c` (ex.: 131072) ou adicione `--fit on` para que o llama.cpp ajuste automaticamente o uso de VRAM.

---

## 9. Parâmetros de inferência recomendados

Otimizados com base em testes locais reais (AMD Radeon AI PRO R9700 32GB):

| Parâmetro | Tarefas do dia a dia / Redação | Tarefas complexas / Programação avançada | Descrição |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Estabilidade no dia a dia; exploração moderada em programação complexa |
| top\_p | 0,95 | 0,95 | Limiar do núcleo de amostragem (nucleus sampling) |
| top\_k | 20 | 20 | Amostragem truncada |
| min\_p | 0,024 | 0,024 | Filtro de probabilidade mínima |
| repeat\_penalty | 1,05 | 1,05 | Penalidade de repetição |
| presence\_penalty | 0 | 0 | Sem penalidade de presença |
| context\_length | 131072 | 262144 | Diário 128K / Complexo 256K (padrão llama.cpp 128K) |
| reasoning | on | on | Ativa a cadeia de raciocínio (chain-of-thought) |
| reasoning\_budget | 400 | 1000 | Orçamento de raciocínio em tokens (maior para tarefas complexas) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Raciocínio emitido em campo separado |
| **spec-type** | **default** | **default** | **Aceleração por decodificação especulativa (ngram, ideal para MoE — veja a Seção 11)** |
| Cache KV | q4\_0 | q4\_0 | Cache KV quantizado (unificado com kv-unified) |

> 💡 **Modo de pensamento**: ative com `--reasoning on`; o modelo raciocina internamente antes de emitir a resposta. `reasoning_budget` controla o número máximo de tokens de raciocínio.

---

## 10. Comparação de formatos de quantização

| Formato | Tamanho | Precisão | Descrição |
| --- | --- | --- | --- |
| FP16 original | ~70 GB | 100% | Sem perdas; requer GPU profissional |
| **MoziSmartBit (este modelo)** | **~15,9 GB** | **~99%** | **Quantização inteligente proprietária: melhor precisão e menor tamanho** |
| Q4_K_M | ~22 GB | ~98% | GGUF padrão de 4 bits |
| Q5_K_M | ~24,7 GB | ~99% | Precisão ainda maior |
| Q6_K | ~28,5 GB | ~99,5% | Quase sem perdas |
| Q8_0 | ~36,9 GB | ~100% | Sem perdas |

> A MoziSmartBit mantém cerca de 99% de precisão e, ao mesmo tempo, comprime o modelo MoE de 35B para 15,9 GB (taxa de compressão de 4,5x), cerca de 30% menor que o Q4_K_M — mais adequada para implantação local em GPUs de consumo.

---

## 11. Aceleração por decodificação especulativa função importante

Este modelo acelera significativamente a inferência por meio da **decodificação especulativa (Speculative Decoding)** — em testes locais, a velocidade é **cerca de 1,5–2x maior** do que com a função desativada.

- **Configuração ideal para MoE**: o llama.cpp recomenda a decodificação especulativa **ngram** (`--spec-default`) para arquiteturas MoE — a mais rápida e estável em testes locais
- **Sobre o nome do modelo**: "MTP" no nome indica os pesos de Multi-Token Prediction do modelo base (totalmente preservados). Como o suporte do llama.cpp a drafts MTP para arquiteturas MoE é limitado, a MoziAI adota uniformemente a decodificação especulativa ngram para obter a melhor velocidade medida em testes

### Parâmetros para ativar

```bash
--spec-default
```

### Sugestões de ajuste dos parâmetros

| Configuração | Cenário de uso |
| --- | --- |
| --spec-default (padrão) | Recomendado: equilibra velocidade e VRAM |
| Desativar a decodificação (remova o parâmetro) | Cenários com VRAM limitada; velocidade ligeiramente menor |

---

## 12. Recomendações de configuração de VRAM

Com base em testes reais da versão MoziSmartBit (modelo + visão totalizando ~16,4 GB):

| VRAM | Configuração recomendada | Descrição |
| --- | --- | --- |
| 20 GB | Contexto de 150K, cache KV q4\_0, com suporte a visão | Modelo + visão ~16,4 GB; 256K + visão ocupam apenas ~19,5 GB de VRAM |
| **24 GB** | **256K completo, cache KV q4\_0, visão perfeitamente suportada** | **Configuração recomendada**: visão + contexto longo de 256K ocupam ~20,4 GB, com margem de ~3,6 GB |
| 32 GB+ | 256K completo, margem de VRAM generosa | Ex.: R9700 32GB: visão + contexto longo de 256K com margem de ~10 GB — a configuração mais potente |

> 💡 Quanto mais longo o contexto, maior o consumo de VRAM. Em caso de OOM, reduza gradualmente o parâmetro `-c`. Use `--fit on` para que o llama.cpp ajuste automaticamente o número de camadas à VRAM disponível. Suporta GPUs NVIDIA / AMD de todas as marcas.

---

## 13. Métodos de implantação

### Implantação com Ollama

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

Pesquise `moziAI` no LM Studio / Jan e baixe a versão quantizada Q4\_K\_M (o LM Studio lê por padrão o modelo na raiz do repositório; para versões anteriores, use "Adicionar a partir de URL" para importar os arquivos do diretório da versão correspondente, ex.: `V3.7/`).

> 💡 O suporte do Ollama a mmproj e chat\_template é limitado; recomendamos priorizar o llama.cpp para obter todas as funcionalidades.

---

## 14. Benchmarks

O MoziAI-35B-V3.8 foi desenvolvido por meio de fine-tuning, destilação e aprimoramento sobre o modelo base deepreinforce-ai/Ornith-1.5-35B-A3B, tendo o domínio financeiro vertical como direção central de otimização. Segue a comparação entre modelos (as capacidades gerais do MoziAI são equivalentes às do modelo base Ornith-1.5-35B-A3B; os dados são dos testes reais da versão V3.7, já que V3.8 e V3.7 compartilham a mesma base e o mesmo sistema de treinamento):

| Benchmark | moziAI-35B-V3.8<br>(este modelo) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Testes de programação** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67,8 | 64,2 | 52,5 | 42,1 | 51,7 | 53,5 |
| Terminal-Bench 2.1 (Claude Code) | 68,5 | 62,8 | 49,2 | - | - | 48,6 |
| SWE-bench Verified | 79 | 75,6 | 73,4 | 52 | 76 | 76,4 |
| SWE-bench Pro | 59,6 | 50,4 | 49,5 | 35,7 | 51,2 | 51,6 |
| SWE-bench Multilingual | 71,4 | 69,3 | 67,2 | 51,7 | - | 69,3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5,1 | 1,4 | 1,4 | - | - | 1,4 |
| NL2Repo | 46,2 | 34,6 | 29,4 | 15,5 | - | 36,8 |
| SWE Atlas - QnA | 39,8 | 37,1 | 15,5 | - | - | 20,4 |
| **Testes de raciocínio** |  |  |  |  |  |  |
| HLE (no tools) | 25,6 | 20,8 | 21,4 | 19,5 | 22 | 28,7 |
| HLE (with tools) | 33,4 | 30,1 | 28,9 | 26,5 | - | 48,3 |
| GPQA Diamond | 89,2 | 86,2 | 86 | 84,3 | 83,5 | 88,4 |
| **Testes de agente** |  |  |  |  |  |  |
| MCP-Atlas | 70,2 | 64,4 | 62,8 | 55 | 75,5 | 72,3 |
| Toolathlon-Verified | 48,7 | 42,4 | 41,7 | 40,8 | - | 38,3 |
| WideSearch | 67,8 | 63,4 | 60,1 | 54,2 | - | 74 |
| BrowseComp | 67,6 | 63,5 | 62 | - | - | 78,6 |
| ClawEval | 72,5 | 69,8 | 68,7 | 48,5 | - | 70,7 |

> O domínio financeiro vertical é a direção central de otimização da MoziAI-35B: em cenários como interpretação de demonstrações financeiras, estratégias quantitativas, gestão de risco e compliance e chamada de ferramentas de agentes, o desempenho é significativamente superior ao dos modelos gerais. Os dados de Gemma-4 / Qwen3.6 são resultados oficiais publicados.

---

## 15. Otimização Uncensored sem censura

Este modelo herda a característica Uncensored (sem censura) do modelo base Ornith-1.5-35B-A3B, com as seguintes vantagens:

| Vantagem | Descrição |
| --- | --- |
| Sem restrições de censura | Não recusa nenhum tópico, incluindo conteúdos sensíveis ou controversos |
| Saída livre | Não sujeito a políticas de segurança; pode gerar qualquer tipo de resposta |
| Informações completas | Fornece informações completas e sem filtros, adequado para cenários de pesquisa e análise |
| Privacidade local | A implantação local garante dados totalmente privados, livres de censura na nuvem |

**Cenários de uso**: pesquisa acadêmica, análise aprofundada, discussão livre e um panorama de conversas com IA sem limitações.

**Aviso**: este é um modelo de implantação local; o conteúdo gerado é inteiramente controlado pelo usuário, e o modelo não assume responsabilidade pela moderação de conteúdo.

---

## 16. Licença

Este modelo utiliza uma **licença restritiva personalizada**:

- ✅ **Permitido** — uso comercial gratuito, cópia e distribuição
- ❌ **Proibido** — desenvolvimento secundário, revenda e sublicenciamento
- 📋 **Exigido** — preservar o aviso de copyright original e indicar a fonte: moziAI-35B

Este modelo é fornecido "no estado em que se encontra" (as is), sem garantias de qualquer tipo. As saídas do modelo têm caráter apenas informativo e não constituem recomendação de investimento. O usuário assume integralmente os riscos decorrentes do uso.

Para os termos detalhados, consulte o arquivo [LICENSE](LICENSE).

---

## 17. Contatos

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
