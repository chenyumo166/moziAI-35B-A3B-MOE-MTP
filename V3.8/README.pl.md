---
language:
- pl
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

# MoziAI-35B-V3.8 — Kompaktowy, ale potężny multimodalny model AI do darmowego wdrożenia lokalnego

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | Polski | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md)

**Data wydania: 2026-09-01** · **Wersja: V3.8**

---

## 📑 Spis treści

- [1. Przegląd modelu](#1-przegląd-modelu)
- [2. Kluczowe funkcje](#2-kluczowe-funkcje) — Dynamiczne myślenie siedmiowymiarowe / LOOP / MoziSmartBit / Fokus finansowy
- [3. Notatki o aktualizacji wersji](#3-notatki-o-aktualizacji-wersji)
- [4. Kluczowe możliwości](#4-kluczowe-możliwości-w-domenie-finansowej)
- [5. Specyfikacja techniczna](#5-specyfikacja-techniczna)
- [6. Szybki start](#6-szybki-start-3-pliki-100-aktywacji-najlepszych-możliwości-wnioskowania) — **pobierz 3 pliki**
- [7. Pobieranie modelu](#7-pobieranie-modelu)
- [8. Polecenia uruchamiania](#8-polecenia-uruchamiania)
- [9. Zalecane parametry wnioskowania](#9-zalecane-parametry-wnioskowania)
- [10. Porównanie formatów kwantyzacji](#10-porównanie-formatów-kwantyzacji)
- [11. Przyspieszenie dekodowania spekulacyjnego](#11-przyspieszenie-dekodowania-spekulacyjnego-kluczowa-funkcja)
- [12. Zalecenia konfiguracji VRAM](#12-zalecenia-konfiguracji-vram)
- [13. Metody wdrożenia](#13-metody-wdrożenia)
- [14. Benchmarki](#14-benchmarki)
- [15. Optymalizacja Uncensored](#15-optymalizacja-uncensored)
- [16. Licencja](#16-licencja)
- [17. Kontakt](#17-kontakt)

---

## 1. Przegląd modelu

MoziAI-35B-V3.8 to lokalnie wdrażalny, otwartoźródłowy multimodalny model AI opracowany przez zespół Chen Yumo, czołowego chińskiego influencera finansowego. Zbudowany na otwartej bazie **Ornith-1.5-35B-A3B** (architektura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, licencja MIT), integruje własne dane finansowe zespołu + możliwości domeny finansowej + dynamiczny siedmiowymiarowy system myślenia + mechanizm iteracyjnej refleksji LOOP agenta + cechę Uncensored + hybrydowy algorytm kwantyzacji MoziSmartBit.

**💡 Przewaga rozmiaru: tylko 15,9 GB** — model MoE o 35 mld parametrów jest skompresowany do zaledwie **15,9 GB** dzięki autorskiej inteligentnej kwantyzacji MoziSmartBit (około 30% mniejszy niż standardowy Q4_K_M ~22GB). Mieści się w jednym instalatorze, działa na zwykłych kartach konsumenckich (20GB VRAM+), redukuje koszty tokenów chmurowych do **zera**, zapewnia wolność tokenów 7×24 godziny oraz gwarantuje prywatność i bezpieczeństwo danych lokalnych. Licencjonowany do **darmowego użytku komercyjnego** — zero barier dla osób i firm.

---

## 2. Kluczowe funkcje

### 🧠 Dynamiczny siedmiowymiarowy system myślenia

Autorski system wnioskowania MoziAI. Dla dowolnego zadania model najpierw generuje znacznik **moziAI-Think**, a następnie dynamicznie rozwija ustrukturyzowane myślenie w zależności od złożoności zadania:

| Poziom | Scenariusz | Typowe zadania | Rozwijane wymiary |
| --- | --- | --- | --- |
| **Poziom 0** | Proste pytania i odpowiedzi | Wyjaśnianie terminów, wyszukiwanie faktów, tłumaczenie, streszczanie | ①Zrozumienie zadania ⑤Potrzeby zasobów (szybka odpowiedź 2-wymiarowa) |
| **Poziom 1** | Analiza i diagnoza | Badania rynku, copywriting, analiza danych, czytanie raportów, ocena strategii | ①②③⑤⑥ Ocena pięciowymiarowa |
| **Poziom 2** | Złożony rozwój/strategia | Rozwój kodu, projektowanie architektury, rozwój strategii kwant, wieloetapowe przepływy pracy, projektowanie systemów | ①②③④⑤⑥⑦ Pełne siedmiowymiarowe głębokie wnioskowanie |

> Siedem wymiarów: ①Zrozumienie zadania ②Ocena złożoności ③Zależności ④Ocena ryzyka ⑤Potrzeby zasobów ⑥Kryteria akceptacji ⑦Strategia wykonania

### 🔄 Mechanizm iteracji LOOP agenta

Złożone zadania automatycznie wchodzą w tryb iteracji **moziAI-Loop**: **Runda 1 wykonanie + ocena → Runda 2 dostosowanie + weryfikacja**, co zapewnia, że wyniki przechodzą samoweryfikację przed udzieleniem ostatecznej odpowiedzi. Model działa jak doświadczony inżynier: «dekompozycja problemu → ocena rozwiązania → wykonanie → refleksja → optymalizacja», znacząco zwiększając dokładność i wykonalność złożonych zadań. Proste pytania i zadania automatycznie wyłączają Loop.

### 📦 Inteligentna kwantyzacja MoziSmartBit

Autorska warstwowa inteligentna kwantyzacja: model MoE o 35 mld parametrów kompresowany do około **15,9 GB**, około 6,5 GB (~30%) mniejszy niż standardowy Q4_K_M (~22 GB), przy zachowaniu **~99%** dokładności FP16. Tradycyjna kwantyzacja stosuje jednolitą precyzję do wszystkich warstw; MoziSmartBit stosuje inteligentną strategię zróżnicowania dopasowaną do struktury MoE, z dokładnością lepszą niż Q4_K_M. Współczynnik kompresji: **4,5x**.

### 💰 Fokus na pionowej domenie finansowej

Głęboka optymalizacja pod pytania finansowe, programowanie ilościowe i wywoływanie narzędzi. Domena finansowa ma bardzo niską tolerancję na halucynacje modelu, a MoziAI wypada znacznie lepiej niż modele ogólne o podobnym rozmiarze w tej dziedzinie.

### 🛡️ Cecha Uncensored

Brak ograniczeń moderacji treści, swobodne odpowiedzi, kompletne informacje, lokalna prywatność. Odpowiedni do badań akademickich, głębokiej analizy, swobodnej dyskusji itp. (patrz [Sekcja 15](#15-optymalizacja-uncensored)).

### 🌐 Inne funkcje

- **Wsparcie wielojęzyczne**: 201 języków i dialektów, z szczególną optymalizacją chińskiego
- **Programowanie ogólne**: rozwój full-stack, debugowanie kodu, projektowanie architektury, obejmuje Python/JS/TS/Go/Rust
- **Pisanie artykułów**: wysokiej jakości pisanie w wielu gatunkach — raporty, artykuły analityczne, dokumentacja techniczna, treści kreatywne
- **Rozumienie wizualne**: multimodalne widzenie, wsparcie rozumienia obrazów ze zrzutów ekranu lokalnie
- **Wsparcie wielu frameworków**: llama.cpp / Ollama / LM Studio / Jan
- **Wsparcie wielu Agentów**: OpenClaw / Hermes / Cursor / Claude Code / Codex itd., natywne wywoływanie narzędzi i wieloetapowa orkiestracja zadań

---

## 3. Notatki o aktualizacji wersji

Wersja V3.8 została przeszkolona z wykorzystaniem autorskiego systemu zbiorów treningowych tej samej generacji co 27B-V3.8 (tożsamość / dynamiczne siedmiowymiarowe myślenie / iteracja LOOP / pionowa domena finansowa), ze szczególnym naciskiem na wzmocnienie autorskiego trybu wnioskowania «dynamiczne siedmiowymiarowe myślenie + iteracja LOOP», inteligentniejsze rozpoznawanie złożoności zadań, wyższy wskaźnik ukończenia złożonych zadań oraz lepszą zdolność «najpierw pomyśl, potem działaj»; kontynuuje również cechę Uncensored i głęboką optymalizację pionowej domeny finansowej.

moziAI utrzymuje aktywną częstotliwość aktualizacji wersji, aby nadążać za przyszłym rozwojem AI, i nieustannie poprzez własne technologie sprawia, że lokalne modele AI są lżejsze we wdrożeniu i coraz bardziej zdolne.

---

## 4. Kluczowe możliwości w domenie finansowej

| Obszar możliwości | Opis |
| --- | --- |
| Analiza rynku | Interpretacja makro/mikroekonomiczna, analiza rynków A/HK/US/towarów/kryptowalut i ich logiki |
| Finanse i raporty | Interpretacja kluczowych wskaźników raportów finansowych, ekstrakcja streszczeń raportów, wsparcie wyceny i prognoz zysków |
| Ryzyko i zgodność | Ocena ryzyka produktów, przypomnienia o zgodności porad inwestycyjnych, interpretacja polityk regulacji finansowych |
| Kwant i strategia | Projektowanie pomysłów na strategie ilościowe, kwantyzacja Pyramid (PEL), logika backtestów, budowa czynników i wywoływanie narzędzi |
| Wywoływanie narzędzi | Łączenie z danymi rynkowymi w czasie rzeczywistym, bazami danych, wyszukiwaniem raportów finansowych |

---

## 5. Specyfikacja techniczna

| Element | Specyfikacja |
| --- | --- |
| Model bazowy | Ornith-1.5-35B-A3B (architektura Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, licencja MIT) |
| Rozmiar parametrów | 35 mld (35B) architektura MoE, 256 ekspertów routingu + 1 ekspert współdzielony, 8 ekspertów aktywnych na token |
| Metoda kwantyzacji | Autorska inteligentna kwantyzacja MoziSmartBit + standardowy format GGUF |
| Długość kontekstu | 256K (262 144 tokenów) |
| Rozmiar modelu | ~15,9 GB |
| Minimalne VRAM | **20GB+** wdrażalny (offload CPU); **24GB+** płynny długi kontekst; **32GB+** pełne 256K + widzenie |
| Frameworki wnioskowania | llama.cpp / Ollama / LM Studio / Jan |
| Szybkość wnioskowania | Z dekodowaniem spekulacyjnym: GPU AMD R9700 do **140+ tokenów/s** / AMD MAX+395 CPU iGPU do **70+ tokenów/s** |
| Zespół deweloperski | Zespół Chen Yumo |

---

## 6. Szybki start 3 pliki 100 aktywacji najlepszych możliwości wnioskowania

> ⚠️ **Kluczowa uwaga**: Najlepsze możliwości wnioskowania MoziAI wymagają **pobrania 3 plików jednocześnie** — modelu głównego, projektora wizyjnego, szablonu czatu. Brak któregokolwiek spowoduje utratę odpowiednich możliwości.

### 6.1 Pobieranie plików modelu

Pobierz **te 3 pliki** z HuggingFace / ModelScope do tego samego katalogu lokalnego (model główny w **katalogu głównym repozytorium**, projektor wizyjny w `mmproj/35B/`, szablon czatu w `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Model główny (wymagany, 15,9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Projektor wizyjny (wymagany, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Szablon czatu (wymagany, zawiera instrukcje myślenia+Loop)
```

| Plik | Rozmiar | Wymóg | Funkcja |
| --- | --- | --- | --- |
| Model główny `.gguf` | ~15,9 GB | **Wymagany** | Wagi modelu, podstawowe możliwości wnioskowania |
| Projektor wizyjny `mmproj` | ~1 GB | **Wymagany** | Multimodalne rozumienie wizualne, bez niego utrata możliwości obrazowych |
| Szablon czatu `.jinja` | Minimalny | **Wymagany** | Wstrzykuje tożsamość MoziAI + instrukcje siedmiowymiarowego myślenia + mechanizm LOOP |

### 6.2 Uruchamianie i użytkowanie

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Otwórz `http://localhost:8080` w przeglądarce, aby rozpocząć rozmowę. Pełne zalecane parametry w Sekcji 9.

---

## 7. Pobieranie modelu

| Platforma | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Użytkownicy LM Studio**: wyszukaj `moziAI` w [LM Studio](https://lmstudio.ai), aby pobrać jednym kliknięciem, bez ręcznego pobierania plików.

> 💡 **Wskazówka pobierania**: kliknij link powyżej, aby wejść do repozytorium HuggingFace, otwórz zakładkę **"Files and versions"**, pobierz model główny z **katalogu głównego repozytorium**, następnie projektor wizyjny z `mmproj/35B/` i szablon czatu z `V3.8/`, upewniając się, że wszystkie trzy pliki znajdują się w tym samym katalogu.

---

## 8. Polecenia uruchamiania

### Najprostsze uruchomienie (z 3 plikami)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Pełne zalecane uruchomienie

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

> 💡 Jeśli VRAM jest ograniczone: obniż `-c` (np. 131072) lub dodaj `--fit on`, aby llama.cpp automatycznie dopasował VRAM.

---

## 9. Zalecane parametry wnioskowania

Zoptymalizowane na podstawie lokalnych testów (AMD Radeon AI PRO R9700 32GB):

| Parametr | Zadania codzienne / Pisanie | Zadania złożone / Zaawansowane kodowanie | Uwagi |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Codzienna stabilność; umiarkowana eksploracja dla złożonego kodowania |
| top\_p | 0,95 | 0,95 | Próg próbkowania jądrowego |
| top\_k | 20 | 20 | Próbkowanie ucięte |
| min\_p | 0,024 | 0,024 | Filtr minimalnego prawdopodobieństwa |
| repeat\_penalty | 1,05 | 1,05 | Kara za powtarzanie |
| presence\_penalty | 0 | 0 | Brak kary obecności |
| context\_length | 131072 | 262144 | Codziennie 128K / Złożone 256K (domyślnie llama.cpp 128K) |
| reasoning | on | on | Włącz łańcuch wnioskowania (CoT) |
| reasoning\_budget | 400 | 1000 | Budżet tokenów wnioskowania (wyższy dla złożonych zadań) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Wnioskowanie w osobnym polu |
| **spec-type** | **default** | **default** | **Przyspieszenie dekodowania spekulacyjnego (ngram, optymalne dla MoE, patrz Sekcja 11)** |
| Pamięć podręczna KV | q4\_0 | q4\_0 | Skwantyzowana pamięć KV (kv-unified) |

> 💡 **Tryb myślenia**: włączany przez `--reasoning on` — model wnioskuje wewnętrznie przed odpowiedzią. `reasoning_budget` ogranicza maksymalną liczbę tokenów myślenia.

---

## 10. Porównanie formatów kwantyzacji

| Format | Rozmiar | Dokładność | Uwagi |
| --- | --- | --- | --- |
| FP16 oryginalny | ~70 GB | 100% | Bezstratny, wymaga profesjonalnego GPU |
| **MoziSmartBit (ten model)** | **~15,9 GB** | **~99%** | **Autorska inteligentna kwantyzacja, najlepsza dokładność na rozmiar** |
| Q4_K_M | ~22 GB | ~98% | Standardowe GGUF 4-bit |
| Q5_K_M | ~24,7 GB | ~99% | Wyższa dokładność |
| Q6_K | ~28,5 GB | ~99,5% | Prawie bezstratny |
| Q8_0 | ~36,9 GB | ~100% | Bezstratny |

> MoziSmartBit zachowuje ~99% dokładności, kompresując model MoE 35B do 15,9 GB (współczynnik 4,5x), ~30% mniejszy niż Q4_K_M — idealny dla kart konsumenckich.

---

## 11. Przyspieszenie dekodowania spekulacyjnego kluczowa funkcja

Ten model znacząco zwiększa szybkość wnioskowania dzięki **Dekodowaniu Spekulacyjnemu (Speculative Decoding)** — lokalnie zmierzono **~1,5-2x szybciej** niż przy wyłączonym.

- **Konfiguracja optymalna dla MoE**: llama.cpp zaleca **dekodowanie spekulacyjne ngram** (`--spec-default`) dla architektur MoE — najszybsze i najbardziej stabilne w testach lokalnych
- **O \"MTP\" w nazwie**: \"MTP\" odnosi się do wag Multi-Token Prediction modelu bazowego (w pełni zachowane); wsparcie draftu MTP llama.cpp dla MoE jest ograniczone, dlatego MoziAI używa schematu ngram dla najlepszej zmierzonej szybkości

### Parametr aktywacji

```bash
--spec-default
```

### Sugestie dostrajania

| Konfiguracja | Scenariusz |
| --- | --- |
| --spec-default (domyślny) | Zalecany: równowaga szybkości i VRAM |
| Wyłącz (usuń parametr) | Scenariusze niskiego VRAM; nieco wolniej |

---

## 12. Zalecenia konfiguracji VRAM

Zmierzono na wersji MoziSmartBit (model + widzenie łącznie ~16,4 GB):

| VRAM | Zalecana konfiguracja | Uwagi |
| --- | --- | --- |
| 20 GB | Kontekst 150K, pamięć KV q4\_0, wsparcie widzenia | Model+widzenie ~16,4 GB, 256K+widzenie tylko ~19,5 GB VRAM |
| **24 GB** | **Pełne 256K, pamięć KV q4\_0, doskonałe wsparcie widzenia** | **Zalecana konfiguracja**: widzenie+długi kontekst 256K ~20,4 GB, zapas ~3,6 GB |
| 32 GB+ | Pełne 256K, wystarczający zapas VRAM | Jak R9700 32GB: widzenie+długi kontekst 256K, zapas ~10 GB, najsilniejsza konfiguracja |

> 💡 Im dłuższy kontekst, tym więcej VRAM. Przy OOM stopniowo obniżaj `-c`. Użyj `--fit on`, aby llama.cpp automatycznie dostosował liczbę warstw. Wspiera wszystkie karty NVIDIA / AMD.

---

## 13. Metody wdrożenia

### Wdrożenie Ollama

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

Wyszukaj `moziAI` w LM Studio / Jan i wybierz wersję kwantyzacji Q4\_K\_M do pobrania (LM Studio domyślnie czyta model z katalogu głównego repozytorium; dla wersji historycznych użyj \"dodaj z URL\", aby zaimportować pliki z odpowiedniego katalogu wersji, np. `V3.7/`).

> 💡 Wsparcie Ollama dla mmproj i chat\_template jest ograniczone; zaleca się najpierw użycie llama.cpp dla pełnej funkcjonalności.

---

## 14. Benchmarki

MoziAI-35B-V3.8 opiera się na fine-tuningu, destylacji i wtórnym rozwoju bazy deepreinforce-ai/Ornith-1.5-35B-A3B, z pionową domeną finansową jako głównym kierunkiem optymalizacji. Poniżej porównanie wielu modeli (ogólne możliwości MoziAI są takie same jak bazy Ornith-1.5-35B-A3B; dane z pomiarów wersji V3.7, V3.8 i V3.7 mają tę samą bazę i system treningowy):

| Benchmark | moziAI-35B-V3.8<br>(ten model) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Testy programowania** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Testy wnioskowania** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Testy agentów** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> Pionowa domena finansowa MoziAI-35B jest głównym kierunkiem optymalizacji MoziAI, wypadając znacznie lepiej niż modele ogólne w interpretacji raportów finansowych, strategiach ilościowych, zgodności zarządzania ryzykiem i wywoływaniu narzędzi agentów. Dane Gemma-4 / Qwen3.6 to oficjalnie opublikowane wyniki ewaluacji.

---

## 15. Optymalizacja Uncensored

Model dziedziczy cechę Uncensored z bazy Ornith-1.5-35B-A3B, z następującymi zaletami:

| Zaleta | Opis |
| --- | --- |
| Bez ograniczeń moderacji | Nie odrzuca żadnego tematu, w tym treści wrażliwych i kontrowersyjnych |
| Swobodne odpowiedzi | Nie jest ograniczony politykami bezpieczeństwa, może generować dowolne typy odpowiedzi |
| Kompletne informacje | Dostarcza pełnych, niefiltrowanych informacji, odpowiedni do badań i analiz |
| Lokalna prywatność | Lokalne wdrożenie oznacza w pełni prywatne dane, bez moderacji chmurowej |

**Przypadki użycia**: badania akademickie, głęboka analiza, swobodna dyskusja, nieograniczone rozmowy AI.

**Uwaga**: To model wdrożony lokalnie — wyniki są w pełni kontrolowane przez użytkownika; model nie ponosi odpowiedzialności za moderację treści.

---

## 16. Licencja

Model używa **niestandardowej licencji ograniczającej**:

- ✅ **Dozwolone** — darmowe użytkowanie komercyjne, kopiowanie i dystrybucja
- ❌ **Zabronione** — dalszy rozwój, odsprzedaż, sublicencjonowanie
- 📋 **Wymagane** — zachowanie oryginalnego powiadomienia o prawach autorskich, podanie źródła: moziAI-35B

Model jest dostarczany „tak jak jest", bez żadnych gwarancji. Wyniki modelu służą wyłącznie celom informacyjnym i nie stanowią porady inwestycyjnej. Użytkownik ponosi całe ryzyko.

Pełne warunki w pliku [LICENSE](LICENSE).

---

## 17. Kontakt

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
