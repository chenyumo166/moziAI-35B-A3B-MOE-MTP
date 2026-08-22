---
language:
- zh
- ko
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

# MoziAI-V3.7-35B-A3B-MOE - 무료 로컬 배포 가능한 소형 고성�?멀티모�?AI

한국�?| [中文](README.md) | [English](README.en.md)

## 모델 개요

MoziAI-35B-A3B-MOE�?중국 금융 인플루언�?천위�?陳雨�? 팀�?개발�?로컬 오픈소스 금융 AI 멀티모�?LLM(비전 �?도구 호출 지�?으로, Ornith-1.5-35B-A3B(**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** 아키텍처, MIT 라이선스) 기반 모델에서 파인튜닝/증류되었습니�? 자체 개발�?**MoziSmartBit 지�?양자�?* 기술�?통해 35B 파라미터 MoE 모델�?�?**15.5 GB**�?압축하여, 손실 수준 ~99% 정밀�?품질�?정밀도와 크기 �?최적�?균형�?달성했습니다.

일반 AI 기능�?유지하는 �?외에�? �?모델은 금융 Q&A, 양적 프로그래�? 도구 호출 �?일반 프로그래밍을 포함�?금융 수직 영역 애플리케이션 최적화에 중점�?둡니�?

모델 개발�?천위모는 �?모델�?로컬 금융 데이�?분석, 양적 전략 R&D, 시장 조사, 기사 작성, 전체 프로젝트 진행, 일반 프로그래�?�?openclaw/hermes�?통한 256K 컨텍스트 작업�?자주 사용합니�? 소비�?등급 GPU에서 로컬 배포 가능하�? 상당�?클라우드 토큰 비용�?절약하고 로컬 데이�?프라이버시와 보안�?보장하면�?7X24 토큰 자유�?달성합니�?

llama.cpp, Ollama, LM Studio �?기타 주류 추론 프레임워크를 지원합니다.

**출시�? 2026-08-21** | **버전: V3.7**

## 모델 특징

- **금융 수직 영역 특화**: 금융 Q&A, 양적 프로그래�?�?도구 호출�?대�?심층 최적�?
- **MoziSmartBit 지�?양자�?*: 자체 개발 스마�?양자�? 정밀도와 크기�?최적 균형, �?**15.5 GB**�?압축
- **소비�?등급 배포**: 20GB 또는 24GB+ VRAM�?소비�?GPU에서 배포 가�? 256K �?컨텍스트 지�?
- **다국�?지�?*: 201�?언어 �?방언, 향상�?중국�?능력, 영어/일본�?한국�?독일�?프랑스어/스페인어/포르투갈�?�?지�?
- **일반 프로그래�?*: 풀스택 개발, 코드 디버�? 아키텍처 설계, 스크립트 작성, Python/JS/TS/Go/Rust �?기타 주류 언어 지�?
- **기사 작성**: 연구 보고�? 분석 기사, 기술 문서, 창의�?콘텐츠를 포함�?고품�?다장�?글쓰기
- **비전 이해**: 멀티모�?비전 지�? 로컬 스크린샷 입력, 이미지 이해
- **검�?없는 자유 출력**: 콘텐�?검�?없음, 안전 제한 없이 모든 주제�?대�?자유롭게 논의
- **향상�?추론**: 사고�?사슬(Chain-of-thought) 훈련으로 추론 품질 향상
- **다중 프레임워�?지�?*: llama.cpp, Ollama, LM Studio, Jan 호환
- **멀티에이전�?플랫�?지�?*: OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex �?기타 주류 AI IDE �?에이전트 프레임워크와 심층 통합, 도구 호출 �?멀티턴 작업 오케스트레이션을 네이티브 지�? 바로 사용 가�?

## 검�?없는 출력�?장점

�?모델은 Ornith-1.5-35B-A3B 기본 모델�?**Uncensored** 기능�?계승하며, 다음�?같은 장점�?있습니다:

| 장점 | 설명 |
|------|------|
| **검�?없음** | 민감하거�?논쟁적인 콘텐츠를 포함�?모든 주제�?거부하지 않음 |
| **자유 출력** | 안전 정책�?제한�?받지 않고, 모든 유형�?응답�?생성�?�?있음 |
| **완전�?정보** | 필터링되지 않은 완전�?정보�?제공하여, 연구 �?분석�?적합 |
| **로컬 프라이버�?* | 로컬 배포�?데이터가 완전�?비공개이�? 클라우드 검열로부�?자유로움 |

> **사용 사례**: 학술 연구, 심층 분석, 자유 논의, 제한 없는 AI 대�?
> **참고**: �?모델은 로컬 배포 모델이며, 출력 콘텐츠는 사용자가 완전�?제어합니�? 콘텐�?관�?책임�?없습니다.

## 핵심 기능

| 기능 영역 | 설명 |
|-----------|------|
| 시장 분석 | 거시/미시경제 해석, A�?HK/미국 주식/원자�?암호화폐 시장 논리 |
| 재무 보고�?| 주요 재무 지�?해석, 리서�?보고�?요약, 밸류에이�?�?실적 전망 지�?|
| 리스�?�?컴플라이언스 | 상품 리스�?평가, 투자 권고 컴플라이언스, 금융 규제 정책 해석 |
| 양적 전략 | 양적 전략 설계, Pyramid(PEL) 양자�? 백테스팅 로직, 팩터 구축 �?도구 호출 |
| 도구 호출 | 실시�?시세, 데이터베이스, 리서�?보고�?검�?�?기타 금융 데이�?소스 통합 |

## 기술 사양

| 항목 | 사양 |
|------|------|
| 기본 모델 | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT 라이선스) |
| 파라미터 | 35B MoE (256�?라우�?전문가 + 1�?공유 전문가, 토큰�?8�?활성) |
| 양자�?| 자체 개발 MoziSmartBit 지�?양자�?+ GGUF 표준 형식 |
| 컨텍스트 길이 | 256K (262,144 토큰) |
| 모델 크기 | ~15.5 GB (MoziSmartBit Uncensored 버전) |
| 최소 VRAM | 20GB+ VRAM 소비�?GPU (�? RTX 4060 Ti 16G CPU 오프로드 사용 �?, 24 GB 권장 (비전 + �?컨텍스트) |
| 추론 프레임워�?| llama.cpp / Ollama / LM Studio / Jan |
| 추론 속도 | 알고리즘 최적�? AMD R700 GPU에서 140+ token/s, AMD MAX+395 CPU iGPU에서 70+ token/s, 로컬 토큰 자유 |
| 팀 | 천위�?팀 |

## 양자�?형식 �?모델 크기 비교

| 양자�?형식 | 모델 크기 | 정밀�?| 비고 |
|------------|-----------|--------|------|
| **FP16 (원본)** | ~70 GB | 100% | 원본 16bit |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **MoziAI가 사용하는 최적�?양자�?방식** |
| Q4_K_M | ~22 GB | ~98% | GGUF 표준 4bit |
| Q5_K_M | ~24.7 GB | ~99% | �?높은 품질 |
| Q6_K | ~28.5 GB | ~99.5% | 거의 무손�?|
| Q8_0 | ~36.9 GB | ~100% | 무손�?|

> MoziAI V3.7은 MoziSmartBit 지�?양자화를 사용하여 ~99% 정밀도를 유지하면�?35B 파라미터 MoE 모델�?~15.5 GB(~4.5�?압축�?�?압축하며, 추론 품질�?소비�?GPU 배포 간소화의 균형�?맞추�?있습니다.

## MoziSmartBit 지�?양자�?

기존 양자화는 모든 레이어에 균일�?정밀도를 적용합니�? **MoziSmartBit 지�?양자�?*�?최적�?크기-정밀�?균형�?위해 차별화된 양자�?전략�?적용합니�?

### 압축 효과

기존 양자화는 모델�?모든 부분을 균일하게 압축하여 종종 상당�?정밀�?손실�?초래합니�? MoziSmartBit 지�?양자화는 자체 개발�?지�?압축 전략�?사용하여 **최소한의 정밀�?손실�?상당�?크기 축소�?달성**합니�?

- **최소 양자�?손실**: 훈련 효과 > 양자�?손실. 훈련�?MoziAI-35B�?금융 영역 텍스트에�?사전 훈련 bf16 기본 모델보다 �?나은 PPL�?달성하며, 유사 AI 모델 대�?환각�?혼란�?perplexity)�?줄입니다
- **~4.5�?크기 축소**: ~70 GB(FP16)에서 ~15.5 GB�?압축, Q4_K_M(~21 GB)보다�?크게 작아 VRAM �?저장소 요구 사항�?크게 낮춤
- **소비�?GPU 친화�?*: 이전�?고급 GPU가 필요했던 35B MoE 모델�?이제 20GB~24GB VRAM에서 원활하게 실행 가�?

### 비교 우위

**Q4_K_M(~22 GB) 대�?*: ~30% �?작음(~15.5 GB), 정밀도는 Q4_K_M보다 **높음**, VRAM 진입 장벽�?�?낮음 �?중급 소비�?GPU(24GB)에서 원활하게 실행 가�?

**FP16 원본(~70 GB) 대�?*: ~4.5�?압축, 훈련 효과 + 최소한의 양자�?손실(훈련 효과 > 양자�?손실), 전문가�?하드웨어 대�?소비�?GPU에서 로컬 256K 컨텍스트 배포 가�?

## 추천 추론 매개변�?

로컬 프로덕션 설정(AMD Radeon AI PRO R9700 32GB) 기반:

| 매개변�?| �?| 설명 |
|----------|------|------|
| temperature | 0.6 | 창의성과 정확�?�?균형 |
| top_p | 0.95 | 뉴클리어�?샘플�?임계�?|
| top_k | 20 | 잘라내기 샘플�?(V3.7 최적�? |
| repeat_penalty | 1.05 | 반복 페널�?|
| presence_penalty | 0 | presence 페널�?없음 |
| context_length | 262144 | 256K �?컨텍스트 |
| batch_size | 2048 | 배치 크기 |
| ubatch_size | 512 | 마이크로 배치 크기 |
| flash_attention | auto | 자동 Flash Attention |
| kv_cache | q4_0 | KV 캐시 양자�?(kv-unified) |
| poll | 0 | 유휴 �?GPU 폴링 없음, 에너지 효율�?|
| reasoning | on | 추론 체인 활성�?(chain of thought) |
| reasoning_budget | 400 | 추론 예산(토큰 단위) |
| reasoning_format | deepseek-legacy | 추론 형식 |
| samplers | top_k;top_p;temperature;typ_p | 샘플�?순서 |

### llama.cpp 실행 명령�?

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 --reasoning on --reasoning-budget 400 \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20
```

### VRAM 구성 권장 사항

사용�?GPU 구성�?각기 다르므�? VRAM 크기�?따른 권장 매개변수를 안내합니�?(모두 MoziSmartBit 버전 기준):

| VRAM | 권장 컨텍스트 | KV 캐시 | 비전 지�?| 비고 |
|------|---------------|---------|-----------|------|
| 20 GB | 150K | q4_0 | 지�?| 모델+비전 ~16.4GB, 실제 테스�?�?200K+비전 사용 �?~19.5GB VRAM 소요 |
| 24 GB | 256K 풀 | q4_0 | 완전 지�?| 비전+256K �?컨텍스트, ~20.4GB VRAM 소요, ~3.6GB 여유 |
| 32 GB+ | 256K 풀 | q4_0 | 완전 지�?| 비전+256K �?컨텍스트, ~10GB 충분�?여유, 최적 구성 |

**NVIDIA**

| VRAM | GPU 모델 |
|------|----------|
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD**

| VRAM | GPU 모델 |
|------|----------|
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel**

| VRAM | GPU 모델 |
|------|----------|
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50 (CPU 오프로드 필요) |

**공유 메모�?iGPU**

| VRAM | 프로세서 |
|------|----------|
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |

> 💡 **�?*: VRAM�?�?요구 사항�?충족하는 �?작동합니�? 브랜드나 모델 제한�?없습니다. NVIDIA / AMD / Intel 독립 GPU �?�?목록�?128GB 통합 메모�?iGPU�?지원합니다.

> 💡 **�?*: �?�?컨텍스트�?�?많은 VRAM�?사용합니�? OOM(메모�?부�?�?발생하면 `-c` 값을 점진적으�?줄이세요. `--fit on`�?사용하면 llama.cpp가 VRAM�?맞게 자동으로 레이어를 조정합니�?

### Ollama 배포

```bash
# Modelfile 생성
FROM ./moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# 빌드 �?실행
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan 배포

LM Studio 또는 Jan에서 `moziAI-35B`�?검색하�? MoziSmartBit 양자�?버전�?다운로드하세�?

## 벤치마크 평가

MoziAI�?**deepreinforce-ai/Ornith-1.5-35B-A3B**에서 파인튜닝되었습니�? MoziAI�?기본 모델 위에�?금융 수직 영역�?최적화되�? 금융 Q&A, 양적 프로그래�?�?도구 호출 시나리오에서 우수�?성능�?제공합니�? MoziAI-35B�?일반 기능은 Ornith-1.5-35B-A3B 기본 모델�?일치합니�?

| 벤치마크 | MoziAI-35B (�?모델) | Qwen3.6-27B | Gemma4-31B | Gemma4-26B | Qwen3.5-35B | 설명 |
|----------|----------------------|-------------|------------|------------|-------------|------|
| Terminal-Bench 2.1 | 64.2 | 59.3 | 42.1 | - | 41.4 | 자율 터미�?코딩 |
| Terminal-Bench (Claude Code) | 62.8 | 59.3 | - | - | 38.9 | Claude Code 코딩 |
| SWE-bench Verified | 75.6 | 77.2 | 52.0 | - | 70.0 | 실제 소프트웨�?엔지니어�?|
| SWE-bench Pro | 50.4 | 53.5 | 35.7 | - | 44.6 | 복잡�?소프트웨�?엔지니어�?|
| SWE-bench Multilingual | 69.3 | 71.3 | - | - | 60.3 | 다국�?코딩 |
| NL2Repo | 34.6 | 36.2 | 15.5 | - | 20.5 | 자연어를 저장소�?변�?|
| LiveCodeBench v6 | 63.3 | 83.9 | 80.0 | 77.1 | - | 경쟁 프로그래�?|
| GPQA Diamond | 88.4 | 87.8 | 84.3 | 82.3 | - | 과학�?추론 |
| AIME 2026 Math | 93.3 | 94.1 | 89.2 | 88.3 | - | 수학 추론 |

> MoziAI-35B�?일반 벤치마크 점수�?Ornith-1.5-35B-A3B 기본 모델�?일치합니�? 금융 수직 영역은 MoziAI�?핵심 최적�?방향으로, 재무제표 분석, 양적 전략, 리스�?�?컴플라이언스, 에이전트 도구 호출 시나리오에서 일반 모델�?크게 능가합니�? Gemma4 �?Qwen3.6 데이터는 공식 공개 결과에서 가져왔습니�?

## 모델 다운로드

모델 크기가 크기(~15.5 GB) 때문�? 가중치�?여러 커뮤니티 플랫폼에 호스팅됩니다:

| 플랫�?| URL |
|--------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |


> 💡 **LM Studio 사용�?*：[LM Studio](https://lmstudio.ai)에서 `moziAI`�?검색하�?원클릭으�?다운로드�?�?있습니다.
> 💡 **다운로드 �?*: �?링크�?클릭하여 HuggingFace 저장소�?이동�?다음, **"Files and versions"** 탭에�?V3.7 디렉토리 아래�?모든 파일(메인 모델, 비전 프로젝션, 채팅 템플�?�?다운로드하세�? �?파일 모두 동일�?디렉토리�?배치해야 합니�?

### ⚠️ 중요: 비전 기능에는 mmproj 파일�?필요합니�?

�?모델은 멀티모�?비전�?지원합니다. **비전 프로젝션 파일(mmproj)**은 버전 디렉토리�?포함되어 있습니다:

- **비전 파일**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16 정밀�?
- **배치 위치**: GGUF 모델 파일�?동일�?버전 디렉토리
- **로딩**: llama-server 시작 �?`--mmproj` 플래그로 로드

```bash
llama-server -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf
```

> 비전 파일 없이�?모델�?**이미지 이해 능력�?손실**되며 텍스�?전용 대화만 유지됩니�?

## 빠른 시작

### 1. 모델 파일 다운로드

HuggingFace / ModelScope에서 V3.7 디렉토리�?모든 파일�?다운로드합니�?

```
V3.7/
├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # 메인 모델 (필수)
├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # 비전 프로젝션 (선택)
└── moziAI-V3.7-35B-chat-template.jinja                  # 채팅 템플�?(권장)
```

### 2. 추론 서버 시작

전체 권장 구성은 위의 [llama.cpp 실행 명령어](#llamacpp-실행-명령�?�?참조하세�?

최소 실행(핵심 매개변수만):

```bash
llama-server \
  -m V3.7/moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 비전 기능�?위해 `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`�?추가하세�?

### 3. 사용 시작

브라우저에서 `http://localhost:8080`�?열고 채팅�?시작하세�?

### 디렉토리 구조

```
moziAI-35B/
├── README.md              # 중국�?버전
├── README.en.md           # �?파일 (영어)
├── LICENSE                # 라이선스
├── V3.7/                  # V3.7 버전 (자체 포함)
�?  ├── RELEASE_NOTES.md                       # 릴리�?노트
�?  ├── moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # 메인 모델
�?  ├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # 비전 프로젝션
�?  └── moziAI-V3.7-35B-chat-template.jinja   # 채팅 템플�?
```

향후 업그레이�?계획은 [未来升级计划.md](未来升级计划.md)�?참조하세�?

## SEO 키워�?

financial AI LLM, 로컬 오픈소스 모델, 엔드사이�?모델, 양적 프로그래�? MoziSmartBit, 지�?양자�? GGUF 양자�? MoE 모델, 로컬 오픈소스 LLM, 로컬 배포, 금융 AI, 도구 호출, Agent, llama.cpp, Ollama, GGUF, Uncensored, 검�?없음, 자유 출력, 제한 없음, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, 금융 수직 영역, 오픈소스 모델

## 라이선스 (중요)

�?모델은 **커스텀 제한 라이선스**�?사용합니�?

### �?허용
- **무료 상업�?사용**: 상업 제품�?자유롭게 통합 가�?
- **복사 �?배포**: 복사, 다운로드, 공유 가�?

### �?금지
- **파생 작품**: 모델 또는 �?일부�?수정, 번역, 적응, 병합 또는 파인튜닝 금지
- **재판�?*: 모델�?단독으로 또는 제품�?일부�?판매 금지
- **재라이선�?*: 서브라이선스 부�?금지

### 📋 요구 사항
- 원본 저작권 고지 유지 필수
- 저작자 표시: moziAI-35B

> 전체 조건은 [LICENSE](./LICENSE)�?참조하세�?

## 면책 조항

있는 그대�?제공되며 보증�?없습니다. 모델 출력은 참고용이�?투자 권유가 아닙니다. 사용자가 모든 리스크를 부담합니다.

## 연락�?

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **이메�?*: 263515@qq.com

---

Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.
