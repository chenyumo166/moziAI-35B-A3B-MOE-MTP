---
language:
- es
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

# MoziAI-35B-V3.8 — Un modelo de IA multimodal compacto pero potente, de despliegue local gratuito

[English](README.en.md) | Español | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**Fecha de publicación: 2026-09-01** · **Versión: V3.8**

---

## 📑 Índice

- [1. Resumen del modelo](#1-resumen-del-modelo)
- [2. Características del modelo](#2-caracteristicas-del-modelo) — Pensamiento dinámico de siete dimensiones / LOOP / MoziSmartBit / Enfoque financiero
- [3. Notas de la actualización de versión](#3-notas-de-la-actualizacion-de-version)
- [4. Capacidades principales](#4-capacidades-principales-del-sector-financiero)
- [5. Especificaciones técnicas](#5-especificaciones-tecnicas)
- [6. ⚡ Inicio rápido](#6--inicio-rapido3-archivos--100-de-activacion-del-mejor-razonamiento) — **Descarga de los 3 archivos**
- [7. Descarga del modelo](#7-descarga-del-modelo)
- [8. Comandos de inicio](#8-comandos-de-inicio)
- [9. Parámetros de inferencia recomendados](#9-parametros-de-inferencia-recomendados)
- [10. Comparativa de formatos de cuantización](#10-comparativa-de-formatos-de-cuantizacion)
- [11. Aceleración por decodificación especulativa](#11-aceleracion-por-decodificacion-especulativa-caracteristica-importante)
- [12. Configuración de VRAM](#12-configuracion-de-vram-recomendada)
- [13. Métodos de despliegue](#13-metodos-de-despliegue)
- [14. Evaluaciones comparativas](#14-evaluaciones-comparativas)
- [15. Optimización Uncensored (sin moderación)](#15-optimizacion-uncensored-sin-moderacion)
- [16. Licencia](#16-licencia)
- [17. Contacto](#17-contacto)

---

## 1. Resumen del modelo

MoziAI-35B-V3.8 es un gran modelo de IA multimodal de código abierto y despliegue local, desarrollado por el equipo de Chen Yumo, destacada figura del sector financiero chino. Se basa en el modelo base de código abierto **Ornith-1.5-35B-A3B** (arquitectura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, licencia MIT) y combina los datos financieros desarrollados por el propio equipo, las capacidades del ámbito financiero, el sistema de pensamiento dinámico de siete dimensiones, el mecanismo iterativo de reflexión LOOP de agentes, la característica Uncensored (sin moderación) y el algoritmo de cuantización híbrida MoziSmartBit.

**💡 Ventaja de tamaño: solo 15.9 GB** — el modelo MoE de 35 000 millones de parámetros se comprime mediante la cuantización inteligente patentada MoziSmartBit hasta **15.9 GB** (aproximadamente un 30 % más pequeño que el Q4_K_M convencional de ~22 GB). Cabe en un único paquete de instalación, puede desplegarse localmente en tarjetas gráficas de consumo general (a partir de 20 GB de VRAM), el coste de tokens en la nube es 0, lo que garantiza tokens ilimitados 7×24 horas y asegura la privacidad y seguridad de los datos locales. Con licencia de **uso comercial gratuito**, tanto particulares como empresas pueden utilizarlo sin ninguna barrera de entrada.

---

## 2. Características del modelo

### 🧠 Sistema de pensamiento dinámico de siete dimensiones

Es el marco de razonamiento central desarrollado por MoziAI. Ante cualquier tarea, el modelo emite primero la marca **moziAI-Think** y despliega dinámicamente un razonamiento estructurado según la complejidad de la tarea:

| Nivel | Escenario de uso | Tareas típicas | Dimensiones desplegadas |
| --- | --- | --- | --- |
| **Level 0** | Preguntas y respuestas sencillas | Explicación de términos, consultas de datos, traducción, resúmenes | ① Comprender la tarea ⑤ Requisitos de recursos (respuesta rápida en dos dimensiones) |
| **Level 1** | Análisis y diagnóstico | Investigación de mercado, redacción de textos, análisis de datos, interpretación de informes de investigación, evaluación de estrategias | ①②③⑤⑥ Evaluación de cinco dimensiones |
| **Level 2** | Desarrollo/estrategias complejos | Desarrollo de código, diseño de arquitectura, desarrollo de estrategias cuantitativas, flujos de trabajo de varios pasos, diseño de sistemas | ①②③④⑤⑥⑦ Razonamiento profundo completo de las siete dimensiones |

> Las siete dimensiones: ① comprender la tarea ② evaluar la complejidad ③ dependencias ④ evaluación de riesgos ⑤ requisitos de recursos ⑥ criterios de aceptación ⑦ estrategia de ejecución

### 🔄 Mecanismo de iteración LOOP de agentes

Las tareas complejas entran automáticamente en el modo de iteración **moziAI-Loop**: **ronda 1: ejecución + evaluación → ronda 2: ajuste + verificación**, lo que garantiza que la salida se somete a una autoverificación antes de ofrecer la respuesta final. El modelo, como un ingeniero senior, «descompone el problema → evalúa el enfoque → ejecuta → reflexiona → optimiza», mejorando notablemente la precisión y la ejecutabilidad en las tareas complejas. En las preguntas y tareas sencillas, el Loop se desactiva automáticamente.

### 📦 Cuantización inteligente MoziSmartBit

Cuantización inteligente jerárquica patentada: comprime el modelo MoE de 35 000 millones de parámetros hasta unos **15.9 GB**, aproximadamente 6.5 GB (~30 %) menos que el Q4_K_M convencional (~22 GB), manteniendo cerca del **99 %** de la precisión FP16. Mientras que la cuantización tradicional aplica una precisión uniforme a todas las capas, MoziSmartBit adopta una estrategia inteligente y diferenciada acorde con las características estructurales del modelo MoE, superando al Q4_K_M en precisión. La tasa de compresión alcanza **4.5x**.

### 💰 Enfoque en el sector financiero vertical

Optimización profunda orientada a las preguntas y respuestas financieras, la programación cuantitativa y la llamada de herramientas. El sector financiero tiene una tolerancia extremadamente baja a las alucinaciones del modelo, y MoziAI rinde significativamente mejor que los modelos generales de tamaño comparable en este ámbito.

### 🛡️ Característica Uncensored (sin moderación)

Sin restricciones de moderación de contenido, salida libre, información completa y privacidad local. Adecuado para escenarios como la investigación académica, el análisis en profundidad y el debate libre. (Consulte la [sección 15](#15-optimizacion-uncensored-sin-moderacion)).

### 🌐 Otras características

- **Soporte multilingüe**: 201 idiomas y dialectos, con capacidades optimizadas especialmente para el chino
- **Programación general**: desarrollo full-stack, depuración de código y diseño de arquitectura, con cobertura de Python/JS/TS/Go/Rust
- **Redacción de artículos**: escritura de alta calidad en múltiples géneros: informes de investigación, artículos de análisis, documentación técnica y contenido creativo
- **Comprensión visual**: visión multimodal que permite comprender el contenido de las imágenes a partir de capturas de pantalla locales
- **Compatibilidad con múltiples frameworks**: llama.cpp / Ollama / LM Studio / Jan
- **Compatibilidad con múltiples agentes**: OpenClaw / Hermes / Cursor / Claude Code / Codex, entre otros, con llamada de herramientas nativa y orquestación de tareas de varios turnos

---

## 3. Notas de la actualización de versión

Esta versión V3.8 se ha reentrenado con el mismo sistema de conjuntos de datos de entrenamiento propio que la 27B-V3.8 (identidad / pensamiento dinámico de siete dimensiones / iteración LOOP / sector financiero vertical), con un énfasis especial en reforzar el modo de razonamiento de pensamiento dinámico de siete dimensiones + iteración LOOP desarrollado por moziAI, de modo que reconozca la complejidad de las tareas de forma más inteligente, consiga una mayor tasa de finalización en las tareas complejas y mejore la capacidad de «pensar antes de actuar»; al mismo tiempo, se mantienen la característica Uncensored (sin moderación) y la optimización profunda del sector financiero vertical.

moziAI mantendrá un ritmo activo de actualizaciones de versión, asegurándose de seguir de cerca la evolución futura de la inteligencia artificial, y seguirá desarrollando tecnología propia para que los modelos de IA locales puedan desplegarse de forma ligera y con capacidades cada vez mayores.

---

## 4. Capacidades principales del sector financiero

| Ámbito de capacidad | Descripción |
| --- | --- |
| Análisis de mercado | Interpretación macro/microeconómica, análisis de las cotizaciones y la lógica de los mercados A, de Hong Kong, de EE. UU., de materias primas y de criptomonedas |
| Finanzas e informes | Interpretación de los indicadores clave de los informes financieros, extracción de resúmenes de informes de investigación, asistencia en la valoración y la previsión de beneficios |
| Gestión de riesgos y cumplimiento | Evaluación de riesgos de productos, avisos de cumplimiento para las recomendaciones de inversión, interpretación de las políticas de regulación financiera |
| Cuantitativo y estrategias | Diseño de ideas de estrategias cuantitativas, cuantificación con Pyramid (PEL), lógica de backtesting, construcción de factores y llamada de herramientas |
| Llamada de herramientas | Integración de fuentes de datos financieros como cotizaciones en tiempo real, bases de datos y búsqueda de informes de investigación |

---

## 5. Especificaciones técnicas

| Elemento | Parámetro |
| --- | --- |
| Modelo base | Ornith-1.5-35B-A3B (arquitectura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licencia MIT) |
| Tamaño de parámetros | 35 000 millones (35B), arquitectura MoE, 256 expertos de enrutamiento + 1 experto compartido, 8 expertos activados por token |
| Método de cuantización | Cuantización inteligente patentada MoziSmartBit + formato estándar GGUF |
| Longitud de contexto | 256K (262,144 tokens) |
| Tamaño del modelo | ~15.9 GB |
| VRAM mínima | **20 GB+** desplegable (descarga a CPU); **24 GB+** contexto largo fluido; **32 GB+** 256K completo + visión |
| Framework de inferencia | llama.cpp / Ollama / LM Studio / Jan |
| Velocidad de inferencia | Con decodificación especulativa: hasta **140+ token/s** con la GPU AMD R9700 / hasta **70+ token/s** con los gráficos integrados de la CPU AMD MAX+395, logrando una salida de tokens ilimitada en local |
| Equipo de desarrollo | Equipo de Chen Yumo |

---

## 6. ⚡ Inicio rápido (3 archivos = 100 % de activación del mejor razonamiento)

> ⚠️ **Aviso clave**: la mejor capacidad de razonamiento de MoziAI requiere **descargar 3 archivos a la vez** — el modelo principal, la proyección de visión y la plantilla de chat. Si falta cualquiera de ellos, se pierde la capacidad correspondiente.

### 6.1 Descarga de los archivos del modelo

Descargue **estos 3 archivos** de HuggingFace / ModelScope a un mismo directorio local (el modelo principal está en la **raíz del repositorio**, la proyección de visión en `mmproj/35B/` y la plantilla de chat en `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Modelo principal (obligatorio, 15.9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Proyección de visión (obligatorio, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Plantilla de chat (obligatoria, incluye las instrucciones de pensamiento de siete dimensiones + Loop)
```

| Archivo | Tamaño | Necesidad | Función |
| --- | --- | --- | --- |
| Modelo principal `.gguf` | ~15.9 GB | **Obligatorio** | Pesos del modelo, capacidad de razonamiento central |
| Proyección de visión `mmproj` | ~1 GB | **Obligatorio** | Comprensión visual multimodal; sin cargarla se pierde la capacidad de imagen |
| Plantilla de chat `.jinja` | Mínimo | **Obligatorio** | Inyecta las instrucciones de identidad de MoziAI + pensamiento de siete dimensiones + mecanismo LOOP |

### 6.2 Inicio y uso

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Abra `http://localhost:8080` en el navegador para comenzar la conversación. Consulte la sección 9 para ver los parámetros recomendados completos.

---

## 7. Descarga del modelo

| Plataforma | Dirección |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Usuarios de LM Studio**: busque `moziAI` en [LM Studio](https://lmstudio.ai) y descárguelo con un solo clic, sin necesidad de descargar archivos manualmente.

> 💡 **Consejo de descarga**: haga clic en los enlaces anteriores para entrar en el repositorio de HuggingFace; en la pestaña **"Files and versions"**, descargue el modelo principal desde la **raíz del repositorio**, la proyección de visión desde `mmproj/35B/` y la plantilla de chat desde `V3.8/`, asegurándose de que los tres archivos queden en el mismo directorio.

---

## 8. Comandos de inicio

### Inicio mínimo (con los 3 archivos)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Inicio recomendado completo

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

> 💡 Si la VRAM es insuficiente: reduzca `-c` (p. ej., 131072) o añada `--fit on` para que llama.cpp adapte la VRAM automáticamente.

---

## 9. Parámetros de inferencia recomendados

Optimizados según pruebas locales reales (AMD Radeon AI PRO R9700 32GB):

| Parámetro | Tareas cotidianas / redacción | Tareas complejas / programación avanzada | Descripción |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | Estabilidad en las tareas cotidianas, exploración moderada en la programación compleja |
| top\_p | 0.95 | 0.95 | Umbral de muestreo nucleico (nucleus sampling) |
| top\_k | 20 | 20 | Muestreo por truncamiento |
| min\_p | 0.024 | 0.024 | Filtrado por probabilidad mínima |
| repeat\_penalty | 1.05 | 1.05 | Penalización por repetición |
| presence\_penalty | 0 | 0 | Sin penalización por presencia |
| context\_length | 262144 | 262144 | Contexto largo de 256K |
| reasoning | on | on | Activa la cadena de razonamiento (chain of thought) |
| reasoning\_budget | 400 | 1000 | Presupuesto de tokens de razonamiento (mayor en tareas complejas) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Salida del razonamiento en un campo independiente |
| **spec-type** | **default** | **default** | **Aceleración por decodificación especulativa (ngram, óptimo para MoE; consulte la sección 11)** |
| Caché KV | q4\_0 | q4\_0 | Caché KV cuantizada (unificada con kv-unified) |

> 💡 **Modo de razonamiento**: se activa con `--reasoning on`; el modelo realiza primero el razonamiento interno y después emite la respuesta. `reasoning_budget` controla el número máximo de tokens de razonamiento.

---

## 10. Comparativa de formatos de cuantización

| Formato | Tamaño | Precisión | Descripción |
| --- | --- | --- | --- |
| FP16 original | ~70 GB | 100 % | Sin pérdidas, requiere una tarjeta gráfica profesional |
| **MoziSmartBit (este modelo)** | **~15.9 GB** | **~99 %** | **Cuantización inteligente patentada: mejor precisión y menor tamaño** |
| Q4_K_M | ~22 GB | ~98 % | 4 bits estándar GGUF |
| Q5_K_M | ~24.7 GB | ~99 % | Mayor precisión |
| Q6_K | ~28.5 GB | ~99.5 % | Casi sin pérdidas |
| Q8_0 | ~36.9 GB | ~100 % | Sin pérdidas |

> MoziSmartBit comprime el modelo MoE de 35B a 15.9 GB (tasa de compresión 4.5x) manteniendo alrededor del 99 % de precisión, un ~30 % más pequeño que el Q4_K_M, por lo que resulta más adecuado para el despliegue local en tarjetas gráficas de consumo.

---

## 11. Aceleración por decodificación especulativa (característica importante)

Este modelo mejora notablemente la velocidad de inferencia mediante la **decodificación especulativa (Speculative Decoding)**, con un **aumento de aproximadamente 1.5-2 veces** frente a tenerla desactivada, según las pruebas locales reales.

- **Configuración óptima para MoE**: llama.cpp recomienda la **decodificación especulativa ngram** (`--spec-default`) para arquitecturas MoE; en las pruebas locales es la más rápida y estable
- **Nota sobre el nombre del modelo**: el "MTP" del nombre indica los pesos de Multi-Token Prediction incluidos en el modelo base (conservados íntegramente); llama.cpp ofrece un soporte limitado para el draft MTP en arquitecturas MoE, por lo que MoziAI adopta de forma uniforme el esquema especulativo ngram para obtener la mejor velocidad verificada en la práctica

### Parámetro de activación

```bash
--spec-default
```

### Recomendaciones de ajuste de parámetros

| Configuración | Escenario de uso |
| --- | --- |
| --spec-default (por defecto) | Recomendado: equilibra la velocidad y la VRAM |
| Especulación desactivada (eliminar el parámetro) | Escenarios con VRAM limitada; la velocidad baja ligeramente |

---

## 12. Configuración de VRAM recomendada

Según las pruebas del modelo MoziSmartBit (modelo + visión: ~16.4 GB en total):

| VRAM | Configuración recomendada | Descripción |
| --- | --- | --- |
| 20 GB | Contexto 150K, caché KV q4\_0, con soporte de visión | Modelo + visión: ~16.4 GB en total; 256K + visión ocupan solo ~19.5 GB de VRAM |
| **24 GB** | **256K completo, caché KV q4\_0, soporte de visión perfecto** | **Configuración recomendada**: la visión + el contexto largo de 256K ocupan solo ~20.4 GB de VRAM, con ~3.6 GB de margen |
| 32 GB+ | 256K completo, amplio margen de VRAM | Por ejemplo, R9700 32GB: visión + contexto largo de 256K, ~10 GB de margen, la configuración más potente |

> 💡 Cuanto más largo sea el contexto, mayor será el consumo de VRAM. En caso de OOM, reduzca gradualmente el parámetro `-c`. Use `--fit on` para que llama.cpp ajuste automáticamente el número de capas según la VRAM disponible. Compatible con tarjetas gráficas de todas las marcas NVIDIA / AMD.

---

## 13. Métodos de despliegue

### Despliegue con Ollama

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

Busque `moziAI` en LM Studio / Jan y descargue la versión cuantizada Q4\_K\_M (LM Studio lee por defecto los modelos de la raíz del repositorio; para las versiones anteriores, use «Agregar desde URL» para importar los archivos del directorio de la versión correspondiente, como `V3.7/`).

> 💡 Ollama ofrece un soporte limitado para mmproj y chat\_template; se recomienda usar preferentemente llama.cpp para obtener la funcionalidad completa.

---

## 14. Evaluaciones comparativas

MoziAI-35B-V3.8 se desarrolló mediante fine-tuning, destilación y desarrollo secundario sobre el modelo base deepreinforce-ai/Ornith-1.5-35B-A3B, con el sector financiero vertical como principal dirección de optimización. A continuación se presenta la comparación entre varios modelos (las capacidades generales de MoziAI coinciden con las del modelo base Ornith-1.5-35B-A3B; los datos proceden de las pruebas reales de la versión V3.7, ya que V3.8 y V3.7 comparten el mismo modelo base y el mismo sistema de entrenamiento):

| Benchmark | moziAI-35B-V3.8<br>(este modelo) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Pruebas de programación** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Pruebas de razonamiento** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Pruebas de agente** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> El sector financiero vertical es la dirección de optimización central de MoziAI-35B: en escenarios como la interpretación de informes financieros, las estrategias cuantitativas, la gestión de riesgos y el cumplimiento, y la llamada de herramientas de agentes, rinde significativamente mejor que los modelos generales. Los datos de Gemma-4 / Qwen3.6 corresponden a los resultados de las evaluaciones oficiales publicadas.

---

## 15. Optimización Uncensored (sin moderación)

Este modelo hereda la característica Uncensored (sin moderación) del modelo base Ornith-1.5-35B-A3B, con las siguientes ventajas:

| Ventaja | Descripción |
| --- | --- |
| Sin restricciones de moderación | No rechaza ningún tema, incluidos los contenidos sensibles o controvertidos |
| Salida libre | No está sujeta a políticas de seguridad; puede generar cualquier tipo de respuesta |
| Información completa | Proporciona información completa y sin filtrar, adecuada para los escenarios de investigación y análisis |
| Privacidad local | El despliegue local implica que los datos son totalmente privados y no están sujetos a la moderación en la nube |

**Escenarios de uso**: investigación académica, análisis en profundidad, debate libre y un panorama de conversación con IA sin restricciones.

**Nota**: este modelo está pensado para el despliegue local; el contenido de salida está totalmente bajo el control del usuario y el modelo no asume responsabilidad alguna de moderación de contenido.

---

## 16. Licencia

Este modelo se distribuye bajo una **licencia restrictiva personalizada**:

- ✅ **Permitido** — uso comercial gratuito, copia y distribución
- ❌ **Prohibido** — desarrollo secundario, reventa y sublicencia
- 📋 **Requerido** — conservar el aviso de copyright original e indicar la fuente: moziAI-35B

Este modelo se proporciona «tal cual», sin garantías de ningún tipo. La salida del modelo tiene fines meramente informativos y no constituye asesoramiento de inversión. El usuario asume el riesgo de su uso por su cuenta.

Consulte el archivo [LICENSE](LICENSE) para conocer los términos completos.

---

## 17. Contacto

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **Correo electrónico**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
