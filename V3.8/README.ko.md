---
language:
- ko
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

# MoziAI-35B-V3.8 — 무료 로컬 배포 가능한 작지만 강력한 멀티모달 AI 모델

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | 한국어 | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

**출시일: 2026-09-01** · **버전: V3.8**

---

## 📑 목차

- [1. 모델 개요](#1-모델-개요)
- [2. 주요 특징](#2-주요-특징) — 동적 7차원 사고 / LOOP / MoziSmartBit / 금융 특화
- [3. 버전 업그레이드 정보](#3-버전-업그레이드-정보)
- [4. 핵심 역량](#4-핵심-역량)
- [5. 기술 사양](#5-기술-사양)
- [6. ⚡ 빠른 시작](#6--빠른-시작3-파일--100-최적-추론-활성화) — **3파일 세트**
- [7. 모델 다운로드](#7-모델-다운로드)
- [8. 실행 명령](#8-실행-명령)
- [9. 권장 추론 파라미터](#9-권장-추론-파라미터)
- [10. 양자화 형식 비교](#10-양자화-형식-비교)
- [11. 투기적 디코딩 가속](#11-투기적-디코딩-가속주요-기능)
- [12. VRAM 설정 권장](#12-vram-설정-권장)
- [13. 배포 방법](#13-배포-방법)
- [14. 벤치마크](#14-벤치마크)
- [15. Uncensored 최적화](#15-uncensored검열-없음-최적화)
- [16. 라이선스](#16-라이선스)
- [17. 연락처](#17-연락처)

---

## 1. 모델 개요

MoziAI-35B-V3.8은 중국 금융 인플루언서 천위모(陳雨墨) 팀이 개발한 로컬 배포 가능한 오픈소스 멀티모달 AI 대규모 모델입니다. 오픈소스 베이스 **Ornith-1.5-35B-A3B**(Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 아키텍처, MoE 35B, MIT 라이선스)를 기반으로, 팀 자체 개발 금융 데이터 + 금융 영역 역량 + 동적 7차원 사고 체계 + 에이전트 LOOP 반복 메커니즘 + Uncensored 특성 + MoziSmartBit 하이브리드 양자화 알고리즘을 통합했습니다.

**💡 크기 장점: 단 15.9GB** — 350억 파라미터 MoE 모델이 자체 개발 MoziSmartBit 양자화로 **15.9 GB**(표준 Q4_K_M ~22GB보다 약 30% 작음)로 압축되었습니다. 단일 패키지로 이동 가능하며, 일반 소비자용 GPU(20GB VRAM 이상)에서 실행되고, 클라우드 token 비용은 **0**, 7×24시간 token 자유를 실현하며 로컬 데이터 프라이버시를 보장합니다. **상업 무료** 라이선스 — 진입 장벽 제로.

---

## 2. 주요 특징

### 🧠 동적 7차원 사고 체계

MoziAI 자체 개발 핵심 추론 프레임워크. 모든 작업에 대해 모델은 먼저 **moziAI-Think** 마커를 출력하고, 작업 복잡도에 따라 구조화된 사고를 동적으로 전개합니다:

| 레벨 | 적용 시나리오 | 대표 작업 | 전개 차원 |
| --- | --- | --- | --- |
| **Level 0** | 간단 Q&A | 용어 설명, 사실 조회, 번역, 요약 | ①작업 이해 ⑤리소스 요구(2차원 즉답) |
| **Level 1** | 분석·진단 | 시장 조사, 문서 작성, 데이터 분석, 리포트 해석, 전략 평가 | ①②③⑤⑥ 5차원 평가 |
| **Level 2** | 복잡 개발/전략 | 코드 개발, 아키텍처 설계, 퀀트 전략 개발, 다단계 워크플로, 시스템 설계 | ①②③④⑤⑥⑦ 전체 7차원 심층 추론 |

> 7차원: ①작업 이해 ②복잡도 평가 ③의존 관계 ④리스크 평가 ⑤리소스 요구 ⑥수용 기준 ⑦실행 전략

### 🔄 에이전트 LOOP 반복 메커니즘

복잡한 작업은 자동으로 **moziAI-Loop** 반복 모드에 진입합니다: **1라운드 실행+평가 → 2라운드 조정+검증**. 출력은 자체 검증을 거친 후 최종 답변이 반환됩니다. 모델은 시니어 엔지니어처럼「문제 분해 → 플랜 평가 → 실행 → 반성 → 최적화」를 수행하여 복잡 작업의 정확성과 실행 가능성을 크게 향상시킵니다. 간단한 Q&A는 Loop를 자동으로 건너뜁니다.

### 📦 MoziSmartBit 스마트 양자화

자체 개발 계층형 스마트 양자화로 350억 파라미터 MoE 모델을 약 **15.9 GB**로 압축. 일반 Q4_K_M(약 22 GB)보다 약 6.5 GB(약 30%) 작고 FP16의 **약 99%** 정확도를 유지합니다. 기존 양자화는 모든 레이어에 균일 정밀도를 사용하지만, MoziSmartBit은 MoE 구조에 특화된 스마트 차별화 전략으로 Q4_K_M보다 높은 정확도를 제공합니다. 압축비 **4.5x**.

### 💰 금융 수직 영역 집중

금융 Q&A, 퀀트 프로그래밍, 도구 호출에 깊이 최적화. 금융 분야는 환각 허용도가 극히 낮아 MoziAI는 동급 크기의 범용 모델보다 명확히 우수합니다.

### 🛡️ Uncensored 특성

콘텐츠 심사 없음, 자유 출력, 완전한 정보, 로컬 프라이버시. 학술 연구, 심층 분석, 자유 토론 등에 적합합니다([15절](#15-uncensored검열-없음-최적화) 참조).

### 🌐 기타 특징

- **다국어 지원**: 201개 언어·방언, 중국어 능력 특별 최적화
- **일반 프로그래밍**: 풀스택 개발, 디버깅, 아키텍처 설계(Python/JS/TS/Go/Rust)
- **글쓰기**: 리포트, 분석 기사, 기술 문서, 창작 등 다장르 고품질
- **시각 이해**: 멀티모달, 로컬에서 스크린샷 이미지 이해
- **멀티 프레임워크**: llama.cpp / Ollama / LM Studio / Jan
- **멀티 에이전트**: OpenClaw / Hermes / Cursor / Claude Code / Codex 등, 네이티브 도구 호출과 멀티턴 작업 오케스트레이션

---

## 3. 버전 업그레이드 정보

V3.8은 27B-V3.8과 같은 세대의 자체 개발 학습 데이터셋 체계(아이덴티티 / 동적 7차원 사고 / LOOP 반복 / 금융 수직 영역)로 재학습되었으며, 동적 7차원 사고 + LOOP 반복 추론 모드를 중점 강화했습니다. 작업 복잡도 인식이 더 스마트해지고 복잡 작업 완료율이 향상되며「먼저 생각하고 행동」능력이 강화되었습니다. Uncensored 특성과 금융 수직 최적화도 지속됩니다.

moziAI는 활발한 버전 업그레이드를 지속하며 AI 발전에 뒤처지지 않고, 자체 기술로 로컬 AI 모델의 경량화와 역량 강화를 계속합니다.

---

## 4. 핵심 역량

| 역량 영역 | 설명 |
| --- | --- |
| 시장 분석 | 거시/미시 경제 해석, A주/홍콩/미국주/상품/암호화폐 시황과 논리 정리 |
| 재무·리포트 | 실적 지표 해석, 리포트 요약 추출, 밸류에이션·수익 예측 보조 |
| 리스크·컴플라이언스 | 상품 리스크 평가, 투자 조언 컴플라이언스, 금융 규제 정책 해석 |
| 퀀트·전략 | 퀀트 전략 설계, Pyramid/PEL 양자화, 백테스트, 팩터 구축, 도구 호출 |
| 도구 호출 | 실시간 시세, 데이터베이스, 리포트 검색 등 금융 데이터 소스 연결 |

---

## 5. 기술 사양

| 항목 | 사양 |
| --- | --- |
| 베이스 모델 | Ornith-1.5-35B-A3B(Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 아키텍처, MIT 라이선스) |
| 파라미터 수 | 350억(35B) MoE, 256 라우팅 전문가 + 1 공유 전문가, 토큰당 8 전문가 활성 |
| 양자화 | 자체 MoziSmartBit 스마트 양자화 + GGUF 표준 형식 |
| 컨텍스트 길이 | 256K(262,144 tokens) |
| 모델 크기 | ~15.9 GB |
| 최소 VRAM | **20GB+** 배포 가능(CPU 오프로드); **24GB+** 부드러운 장문맥; **32GB+** 완전 256K + 시각 |
| 추론 프레임워크 | llama.cpp / Ollama / LM Studio / Jan |
| 추론 속도 | 투기적 디코딩 시: AMD R9700 GPU **140+ tok/s** / AMD MAX+395 iGPU **70+ tok/s** — 로컬 token 자유 |
| 개발 팀 | 천위모 팀 |

---

## 6. ⚡ 빠른 시작(3파일 = 100% 최적 추론 활성화)

> ⚠️ **핵심 팁**: MoziAI의 최적 추론은 **3개 파일을 동시에 다운로드**해야 합니다 — 메인 모델, 비전 프로젝터, 채팅 템플릿. 하나라도 없으면 해당 능력이 손실됩니다.

### 6.1 모델 파일 다운로드

HuggingFace / ModelScope에서 **이 3개 파일**을 로컬 같은 폴더에 다운로드 (메인 모델은 **리포지토리 루트**, 비전 프로젝터는 `mmproj/35B/`, 채팅 템플릿은 `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← 메인 모델(필수, 15.9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← 비전 프로젝터(필수, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← 채팅 템플릿(필수, 7차원 사고+Loop 지시)
```

| 파일 | 크기 | 필수 | 역할 |
| --- | --- | --- | --- |
| 메인 모델 `.gguf` | ~15.9 GB | **필수** | 모델 가중치, 핵심 추론 |
| 비전 `mmproj` | ~1 GB | **필수** | 멀티모달 시각, 미로드 시 이미지 능력 상실 |
| 채팅 템플릿 `.jinja` | 미세 | **필수** | MoziAI 아이덴티티 + 7차원 사고 + LOOP 지시 주입 |

### 6.2 실행 및 사용

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

브라우저에서 `http://localhost:8080`을 열어 대화 시작. 전체 권장 파라미터는 9절 참조.

---

## 7. 모델 다운로드

| 플랫폼 | 주소 |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP/tree/main) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP/tree/master) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP/tree/main) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio 사용자**: [LM Studio](https://lmstudio.ai)에서 `moziAI` 검색 후 원클릭 다운로드.

> 💡 **다운로드 팁**: HuggingFace 리포지토리 **"Files and versions"** 탭에서 **리포지토리 루트**에서 메인 모델, `mmproj/35B/`에서 비전 프로젝터, `V3.8/`에서 채팅 템플릿을 다운로드해 같은 폴더에 배치하세요.

---

## 8. 실행 명령

### 최소 실행(3파일 포함)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### 전체 권장 실행

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

> 💡 VRAM 부족 시: `-c` 낮추기(예: 131072) 또는 `--fit on` 추가로 자동 적합.

---

## 9. 권장 추론 파라미터

로컬 실측 최적화(AMD Radeon AI PRO R9700 32GB):

| 파라미터 | 일상 작업/문서 작성 | 복잡 작업/고급 코딩 | 설명 |
| --- | --- | --- | --- |
| temperature | 0.6 | 0.8 | 일상은 안정, 복잡 코딩은 적절한 탐색 |
| top\_p | 0.95 | 0.95 | 핵 샘플링 임계값 |
| top\_k | 20 | 20 | 절단 샘플링 |
| min\_p | 0.024 | 0.024 | 최소 확률 필터 |
| repeat\_penalty | 1.05 | 1.05 | 반복 페널티 |
| presence\_penalty | 0 | 0 | 존재 페널티 없음 |
| context\_length | 262144 | 262144 | 256K 장문맥 |
| reasoning | on | on | 추론 체인(CoT) 활성화 |
| reasoning\_budget | 400 | 1000 | 추론 예산 token(복잡 작업 높게) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | 추론을 별도 필드로 출력 |
| **spec-type** | **default** | **default** | **투기적 디코딩(ngram, MoE 최적, 11절 참조)** |
| KV 캐시 | q4\_0 | q4\_0 | 양자화 KV 캐시(kv-unified) |

> 💡 **사고 모드**: `--reasoning on`으로 활성화 — 답변 전 내부 추론. `reasoning_budget`은 최대 사고 token 수 제어.

---

## 10. 양자화 형식 비교

| 형식 | 크기 | 정확도 | 설명 |
| --- | --- | --- | --- |
| FP16 원본 | ~70 GB | 100% | 무손실, 프로 GPU 필요 |
| **MoziSmartBit(본 모델)** | **~15.9 GB** | **~99%** | **자체 스마트 양자화, 최고 정확도/최소 크기** |
| Q4_K_M | ~22 GB | ~98% | GGUF 표준 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 더 높은 정확도 |
| Q6_K | ~28.5 GB | ~99.5% | 거의 무손실 |
| Q8_0 | ~36.9 GB | ~100% | 무손실 |

> MoziSmartBit은 약 99% 정확도를 유지하며 35B MoE를 15.9 GB(4.5x 압축)로. Q4_K_M보다 약 30% 작아 소비자 GPU에 최적.

---

## 11. 투기적 디코딩 가속(주요 기능)

본 모델은 **투기적 디코딩(Speculative Decoding)**으로 추론 속도를 크게 향상. 로컬 실측에서 끄면보다 **약 1.5-2배** 빠릅니다.

- **MoE 최적 설정**: llama.cpp는 MoE 아키텍처에 **ngram 투기적 디코딩**(`--spec-default`)을 권장. 로컬 실측 최고 속도·안정
- **모델명 "MTP" 관해**: 베이스의 Multi-Token Prediction 가중치(완전 보존)에서 유래. llama.cpp의 MoE용 MTP draft 지원이 제한적이라 MoziAI는 ngram 방식으로 최적 실측 속도 구현

### 활성화 파라미터

```bash
--spec-default
```

### 조정 제안

| 설정 | 적용 시나리오 |
| --- | --- |
| --spec-default(기본) | 권장: 속도와 VRAM 균형 |
| 비활성화(플래그 제거) | VRAM 부족 시, 다소 느림 |

---

## 12. VRAM 설정 권장

MoziSmartBit 버전(모델+시각 약 16.4GB) 실측 기준:

| VRAM | 권장 설정 | 설명 |
| --- | --- | --- |
| 20 GB | 150K 문맥, q4\_0 KV, 시각 지원 | 모델+시각 약 16.4GB; 256K+시각 약 19.5GB 사용 |
| **24 GB** | **완전 256K, q4\_0 KV, 시각 완벽** | **권장**: 시각+256K 약 20.4GB, 여유 약 3.6GB |
| 32 GB+ | 완전 256K, 여유 충분 | 예: R9700 32GB: 시각+256K 약 10GB 여유, 최강 구성 |

> 💡 문맥이 길수록 VRAM 사용 증가. OOM 시 `-c` 단계적으로 낮추기. `--fit on` 자동 적합. NVIDIA / AMD 지원.

---

## 13. 배포 방법

### Ollama 배포

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

LM Studio / Jan에서 `moziAI` 검색 후 Q4\_K\_M 양자화 버전 다운로드(LM Studio는 기본적으로 루트 디렉토리 모델을 읽습니다. 이전 버전은 "URL에서 추가"로 해당 버전 디렉토리(예: `V3.7/`)의 파일을 가져오세요).

> 💡 Ollama의 mmproj와 chat\_template 지원은 제한적. 전체 기능은 llama.cpp 권장.

---

## 14. 벤치마크

MoziAI-35B-V3.8은 deepreinforce-ai/Ornith-1.5-35B-A3B 베이스를 미세조정·증류·재개발한 모델로, 금융 수직 영역이 핵심 최적화 방향입니다. 아래는 멀티모델 비교(MoziAI 일반 역량은 베이스 Ornith-1.5-35B-A3B와 일치. 데이터는 V3.7 실측 계승 — V3.8은 V3.7과 동일 베이스·동일 학습 체계):

| Benchmark | moziAI-35B-V3.8<br>(본 모델) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **코딩** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **추론** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **에이전트** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI는 금융 수직 영역(실적 해석, 퀀트 전략, 리스크 관리, 에이전트 도구 호출)에서 동급 범용 모델을 크게 능가합니다. Gemma-4 / Qwen3.6 수치는 공식 공개 평가 결과.

---

## 15. Uncensored(검열 없음) 최적화

본 모델은 Ornith-1.5-35B-A3B 베이스의 Uncensored 특성을 계승:

| 장점 | 설명 |
| --- | --- |
| 검열 없음 | 민감·논쟁적 콘텐츠 포함 어떤 주제도 거부하지 않음 |
| 자유 출력 | 안전 정책에 제약 없이 모든 유형의 답변 생성 |
| 완전한 정보 | 필터링되지 않은 정보 제공, 연구·분석에 최적 |
| 로컬 프라이버시 | 로컬 배포 = 데이터 완전 프라이빗, 클라우드 검열 없음 |

**사용 사례**: 학술 연구, 심층 분석, 자유 토론, 제한 없는 AI 대화.

**주의**: 로컬 배포 모델이므로 출력은 사용자가 완전히 관리합니다. 모델은 콘텐츠 심사 책임을 지지 않습니다.

---

## 16. 라이선스

본 모델은 **사용자 정의 제한 라이선스**를 채택:

- ✅ **허용** — 상업 무료 사용, 복사·배포
- ❌ **금지** — 2차 개발, 재판매, 재라이선스
- 📋 **필수** — 원본 저작권 표시 유지, 출처: moziAI-35B

본 모델은「있는 그대로」제공되며 어떠한 보증도 없습니다. 모델 출력은 참고용이며 투자 조언을 구성하지 않습니다. 사용자는 모든 리스크를 부담합니다.

자세한 내용은 [LICENSE](LICENSE) 파일 참조.

---

## 17. 연락처

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 陳雨墨 / chenyumo166. All rights reserved.