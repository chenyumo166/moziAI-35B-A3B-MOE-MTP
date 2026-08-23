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
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.6-A3B-MOE-MTP-Uncensored - 무료 로컬 배포 가능한 작고 강력한 멀티모달 AI 모델

Language / 언어 선택  
[简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [English](README.en.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)

## 모델 소개

MoziAI-35B-A3B-MOE는 중국의 금융 분야 인플루언서 천위모(陳雨墨) 팀이 개발한 로컬 오픈소스 멀티모달 대형 언어 모델입니다(금융 분야 강화, 시각 지원, 도구 호출, 복잡한 장문 태스크 처리, 소비자용 그래픽카드 로컬 배포 지원). Ornith-1.0-35B-A3B(**Qwen3.5-35B-A3B/Qwen3.6-35B-A3B** 아키텍처) 기반으로 2차 개발 파인튜닝/증류를 진행했습니다.

본 모델 개발팀의 철학은 종합적인 능력을 갖춘 로컬 AI 대형 언어 모델 에이전트를 일반 가정과 중소기업에 보급하여 고가의 AI 하드웨어 비용이나 클라우드 API 비용을 들이지 않아도 되게 하는 것입니다. 자체 개발한 **MoziSmartBit 인텔리전트 양자화** 기술로 350억 파라미터의 MoE 모델을 약 **15.5 GB**로 압축하여 모델 정밀도와 크기의 최적 균형을 이루었으며, FP16의 약 99% 수준의 정밀도 품질을 달성했습니다. 본 모델은 350억 파라미터를 가지고 있지만 MOE 희소 전문가 기술로 실제 호출되는 파라미터는 30억에 불과하며 MTP 추측 디코딩을 통한 추론 가속도 가능합니다. 실측 결과 20GB VRAM의 가정용 소비자 그래픽카드로 로컬 무료 배포가 가능하며 140+ token/s의 추론 속도를 자랑해 많은 클라우드 유료 AI 모델보다 빠릅니다.

본 모델은 범용 AI 대형 언어 모델의 능력을 유지하면서 금융 수직 분야 응용, 금융 Q&A, 퀀트 프로그래밍, 범용 프로그래밍, 도구 호출, 256K 복잡한 장문 컨텍스트 태스크 성공률 등 AI 대형 언어 모델의 핵심 능력을 집중 최적화했습니다. 로컬 소비자용 그래픽카드에 무료로 배포해 사용할 수 있어 클라우드 토큰 비용을 크게 절약하고 7X24시간 토큰 프리를 실현하며 로컬 데이터 프라이버시와 보안을 보장합니다.

**발매일：** 2026-08-20 | **버전：V3.6**

## 모델 다운로드

모델 파일이 크기 때문에(~15.5 GB) 모델 가중치는 여러 커뮤니티 플랫폼에 호스팅되어 있습니다：

| 플랫폼 | 주소 |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope（魔搭） | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |

> 💡 **LM Studio 사용자**：[LM Studio](https://lmstudio.ai)에서 `moziAI`를 직접 검색하여 원클릭으로 다운로드할 수 있습니다. 수동으로 파일을 다운로드할 필요가 없습니다.  
> 💡 **다운로드 팁**：위 링크를 클릭해 HuggingFace 리포지토리로 이동한 후 **"Files and versions"** 탭에서 V3.6 디렉토리 내 모든 파일(메인 모델, 시각 프로젝션, 채팅 템플릿)을 다운로드하세요. 세 파일이 같은 디렉토리에 위치하도록 하십시오.

### ⚠️ 중요：시각 기능에는 mmproj 파일 추가가 필요합니다

본 모델은 멀티모달 시각을 지원하며, 시각 프로젝션 파일(mmproj)이 버전 디렉토리에 포함되어 있습니다：

- **시각 파일**：`moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`（약 903 MB, BF16 정밀도）
- **배치 위치**：GGUF 모델 파일과 같은 버전 디렉토리
- **로드 방법**：llama-server 시작 시 `--mmproj` 파라미터로 로드

> 시각 파일을 로드하지 않으면 이미지 이해 기능이 상실되고 순수 텍스트 대화 기능만 남습니다.

### ⚠️ 중요：채팅 템플릿 파일 로드는 필수입니다

본 모델은 전용 채팅 템플릿(chat-template)을 사용하며, **로드하지 않으면 대화 형식 오류, 추론 체인 실패, 응답 품질 대폭 저하의 원인이 됩니다**. 채팅 템플릿 파일은 버전 디렉토리에 포함되어 있습니다：

- **템플릿 파일**：`moziAI-V3.6-35B-chat-template.jinja`（약 5 KB, jinja 형식）
- **배치 위치**：GGUF 모델 파일과 같은 버전 디렉토리
- **로드 방법**：llama-server 시작 시 `--chat-template-file` 파라미터로 로드

> 채팅 템플릿을 로드하지 않으면 모델이 시스템 프롬프트, 사용자 메시지, 사고 블록을 올바르게 인식하지 못해 출력 형식이 혼란스러워지거나 추론 능력이 저하될 수 있습니다.

### llama.cpp 시작 명령（20G+ 그래픽카드 256K 컨텍스트 권장 설정）

> 비고：VRAM이 20G 미만이면 `-c 262144`의 컨텍스트 설정 파라미터 262144를 줄이십시오.

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

## 빠른 시작

### 1. 모델 파일 다운로드

HuggingFace / ModelScope에서 V3.6 디렉토리 내 모든 파일을 로컬로 다운로드합니다：

```
V3.6/
├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf      # 메인 모델（필수）
├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf  # 시각 프로젝션（선택, 시각 기능 필요시 다운로드）
└── moziAI-V3.6-35B-chat-template.jinja                  # 채팅 템플릿（필수! 로드하지 않으면 대화 형식 오류 발생）
```

> ⚠️ **채팅 템플릿은 필수 파일**이며 선택 사항이 아닙니다. 본 모델에는 커스텀 대화 형식(추론 체인/사고 블록 포함)이 있어 템플릿이 없으면 모델 출력 형식이 혼란스러워지고 추론 능력이 상실됩니다. 반드시 다운로드하여 시작 시 로드하십시오.

### 2. 추론 서비스 시작

전체 권장 설정 시작 명령은 아래 [llama.cpp 시작 명령](#llamacpp-시작-명령) 장을 참고하십시오.

최소 시작（핵심 파라미터만）：

```bash
llama-server \
  -m V3.6/moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --chat-template-file V3.6/moziAI-V3.6-35B-chat-template.jinja \
  -c 262144 -ngl 99
```

> 시각 기능이 필요하면 `--mmproj V3.6/moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`를 추가하십시오

### 3. 사용 시작

브라우저에서 `http://localhost:8080`을 열면 대화를 시작할 수 있습니다.

### 디렉토리 구조

```
moziAI-35B/
├── README.md              # 영어 설명서
├── README.ko.md           # 본 파일（한국어 설명서）
├── LICENSE                # 라이선스
├── V3.6/                  # V3.6 버전（버전 자체 포함）
│   ├── RELEASE_NOTES.md                       # 버전 업데이트 설명
│   ├── moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf    # 메인 모델
│   ├── moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf # 시각 프로젝션
│   └── moziAI-V3.6-35B-chat-template.jinja   # 채팅 템플릿
```

## 모델 특징

- **MoziSmartBit 인텔리전트 양자화**：자체 개발한 인텔리전트 양자화 기술로 정밀도와 크기의 최적 균형 실현, 모델을 거의 무손실로 약 **15.5 GB**에 압축
- **복잡한 장문 태스크 처리 능력**：모델 에이전트가 태스크를 자동 계획하는 지능형 루프 처리 난점 대응과 자기 사고 메커니즘을 학습시켜 복잡한 태스크의 자동 실행과 자기 조정 실현, 사용자가 에이전트에 계속 프롬프트를 최적화하는 수고를 덜어줌
- **작은 모델, 큰 능력**：복잡한 태스크 수행에서 동급 350억 파라미터 이내 모델보다 종합 능력이 우수하며, 파라미터 수가 몇 배 더 큰 모델 일부도 능가함
- **MOE+MTP 속도 우위**：모델 전체는 350억 파라미터이지만 실제 호출되는 전문가는 8+1개, 총 30억 파라미터에 불과해 추론 속도가 더 빠름. 20GB~24GB VRAM의 가정용 소비자 그래픽카드로 로컬 배포 가능하며 140+ token/s의 추론 속도를 누릴 수 있음
- **금융 수직 분야 심층 투자**：금융 Q&A, 퀀트 프로그래밍, 도구 호출 능력 강화
- **소비자용 배포**：20GB~24GB VRAM 이상의 가정용 소비자 그래픽카드로 로컬 배포 가능, 최대 256K 장문 컨텍스트 추론 지원
- **다국어 지원**：201개 언어와 방언 지원, 중국어 능력 특별 최적화, 영어, 일본어, 한국어, 독일어, 프랑스어, 포르투갈어 등 주요 언어 지원
- **범용 프로그래밍 능력**：풀스택 개발, 코드 디버깅, 아키텍처 설계, 스크립트 작성 지원, Python/JS/TS/Go/Rust 등 주요 언어 커버
- **문서 작성 능력**：리서치 리포트, 분석 기사, 기술 문서, 크리에이티브 콘텐츠 등 다양한 장르의 고품질 라이팅 지원
- **시각 이해**：추론 프레임워크에 시각 파일을 로드하면 멀티모달 시각 지원, 로컬 스크린샷을 채팅 창에 올리면 모델이 이미지 속 정보를 이해 가능
- **검열 없이 자유로운 출력**：콘텐츠 검열 제한이 없어 어떤 주제든 자유롭게 토론 가능, 보안 정책 제약 받지 않음
- **추론 논리 강화**：추론 논리（사고 연쇄）를 결합해 학습시켜 추론 품질을 더욱 향상
- **멀티 프레임워크 지원**：llama.cpp、Ollama、LM Studio、Jan 등 주요 추론 프레임워크와 호환
- **멀티 Agent 플랫폼 지원**：OpenClaw、Hermes、OpenCode、Cursor、Windsurf、Claude Code、Codex 등 국내외 주요 AI IDE와 Agent 프레임워크에 심층 대응, 도구 호출과 다중 라운드 태스크 오케스트레이션을 네이티브 지원하여 바로 사용 가능

## Uncensored（무검열）의 이점

본 모델은 베이스 모델 Ornith-1.0-35B-A3B의 Uncensored（무검열）특성을 계승하며 다음과 같은 이점이 있습니다：

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>이점</th>
<th>설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>검열 제한 없음</td>
<td>민감하고 논란의 여지가 있는 콘텐츠를 포함해 어떤 주제도 거부하지 않음</td>
</tr>
<tr>
<td>자유로운 출력</td>
<td>보안 정책 제약을 받지 않아 어떤 유형의 응답도 생성 가능</td>
</tr>
<tr>
<td>완전한 정보</td>
<td>필터링되지 않은 완전한 정보를 제공, 연구와 분석 시나리오에 적합</td>
</tr>
<tr>
<td>로컬 프라이빗</td>
<td>로컬 배포는 데이터가 완전히 비공개임을 의미, 클라우드 검열의 영향을 받지 않음</td>
</tr>
</tbody>
</table>

> **적용 시나리오**：무료 상업 이용, 학술 연구, 심층 분석, 자유 토론, 제한 없는 AI 대화
> **주의**：본 모델은 로컬 배포 모델로 출력 내용은 전적으로 사용자가 제어하며 콘텐츠 검열 책임을 지지 않습니다.

## 핵심 능력

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>능력 분야</th>
<th>설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>시장 분석</td>
<td>거시/미시 경제 해석, A주/홍콩주/미국주/상품/암호화폐 시세와 논리 정리</td>
</tr>
<tr>
<td>재무와 리서치 리포트</td>
<td>결산보고서 핵심 지표 해석, 리서치 리포트 요약 추출, 밸류에이션과 수익 예측 보조</td>
</tr>
<tr>
<td>리스크 관리와 컴플라이언스</td>
<td>상품 리스크 평가, 투자 조언 컴플라이언스 안내, 금융 규제 정책 해석</td>
</tr>
<tr>
<td>퀀트와 전략</td>
<td>퀀트 전략 아이디어 설계, 피라미드（Pyramid/PEL）퀀트, 백테스트 로직, 팩터 구축과 도구 호출</td>
</tr>
<tr>
<td>도구 호출</td>
<td>실시간 시세, 데이터베이스, 리서치 리포트 검색 등 금융 데이터에 연결 가능</td>
</tr>
</tbody>
</table>

## 기술 사양

<table>
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr>
<th>항목</th>
<th>파라미터</th>
</tr>
</thead>
<tbody>
<tr>
<td>베이스 모델</td>
<td>Ornith-1.0-35B-A3B（Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 아키텍처, MIT 라이선스）</td>
</tr>
<tr>
<td>파라미터 규모</td>
<td>350억（35B）MoE 아키텍처, 256개 라우팅 전문가 + 1개 공유 전문가, 토큰당 8개 전문가 활성화</td>
</tr>
<tr>
<td>양자화 방식</td>
<td>자체 개발 MoziSmartBit 인텔리전트 양자화 알고리즘 + GGUF 표준 형식 채용</td>
</tr>
<tr>
<td>컨텍스트 길이</td>
<td>256K (262,144 tokens)</td>
</tr>
<tr>
<td>모델 크기</td>
<td>~15.5 GB（MoziSmartBit Uncensored 버전）</td>
</tr>
<tr>
<td>최저 VRAM 요구사항</td>
<td>20GB VRAM 이상의 가정용 소비자 그래픽카드（RTX 3060 12G는 CPU 오프로드 병용 필요, RTX 4060 Ti 16G 등）, 권장 24 GB（시각 + 장문 컨텍스트 포함）</td>
</tr>
<tr>
<td>추론 프레임워크</td>
<td>llama.cpp / Ollama / LM Studio / Jan</td>
</tr>
<tr>
<td>추론 속도</td>
<td>알고리즘 최적화로 AMD Radeon AI PRO R9700 그래픽카드에서 140+token/s / AMD Ryzen AI Max+ 395 내장그래픽에서 70+token/s 달성, 로컬 자유 추론 출력 실현</td>
</tr>
<tr>
<td>개발 팀</td>
<td>천위모 팀</td>
</tr>
</tbody>
</table>

## 양자화 형식과 모델 크기 비교

| 양자화 형식 | 모델 크기 | 정밀도 유지율 | 설명 |
| ---------------- | ------------- | --------- | ----------------- |
| FP16（원본） | ~70 GB | 100% | 원본 16bit 정밀도 |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **본 모델이 채용한 자체 개발 인텔리전트 양자화 솔루션** |
| Q4_K_M | ~22 GB | ~98% | GGUF 표준 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 더 높은 정밀도 |
| Q6_K | ~28.5 GB | ~99.5% | 거의 무손실 |
| Q8_0 | ~36.9 GB | ~100% | 무손실 |

> MoziAI V3.6은 MoziSmartBit 인텔리전트 양자화 솔루션을 채택하여 약 99%의 정밀도를 유지하면서 350억 파라미터의 MoE 모델을 약 15.5 GB로 압축, 압축비 약 4.5x로 추론 품질과 배포 장벽의 균형을 맞춰 소비자용 그래픽카드 로컬 배포에 더 적합합니다.

## MoziSmartBit 인텔리전트 양자화 기술

전통적인 양자화 솔루션은 모든 레이어에 통일된 정밀도를 사용하지만, 천위모 팀이 자체 개발한 **MoziSmartBit 인텔리전트 양자화**는 MoE 모델의 구조적 특징에 대해 지능형 차별화 양자화 전략을 채택하여 크기와 정밀도의 최적 균형을 이룹니다. 모델 품질은 Q4_K_M 형식보다 높으면서 크기는 ~15.5 GB에 불과하며 압축비는 ~4.5x입니다.

### 압축 효과

전통적인 양자화 솔루션은 모델의 모든 부분을 일률적으로 압축해 정밀도 손실이 두드러지는 경우가 많습니다. MoziSmartBit 인텔리전트 양자화는 자체 개발한 지능형 압축 전략을 채택해 **극소의 정밀도 손실로 대폭적인 크기 압축을 실현**합니다：

- **양자화 정밀도 손실 극소**：학습 이득 > 양자화 손실. 학습 후 MoziAI-35B는 금융 분야 텍스트에서 PPL이 학습 전 bf16 베이스 모델보다 우수하며, 유사 AI 모델의 환각과 혼란을 감소
- **모델 크기 4.5배 압축**：FP16의 ~70 GB에서 ~15.5 GB로 압축. Q4_K_M의 ~22 GB보다도 훨씬 작아 VRAM과 스토리지 장벽을 대폭 낮춤
- **소비자용 그래픽카드로 실행 가능**：원래 고급 그래픽카드가 필요했던 35B MoE 대형 모델이 이제 20GB~24GB VRAM으로 원활하게 배포 가능

### 비교 우위

**vs Q4_K_M（~22 GB）**：크기가 약 30% 감소（~15.5 GB）, 정밀도는 Q4_K_M보다 **더 높음**, VRAM 장벽이 더 낮아 중급 소비자용 그래픽카드（20GB）로 원활히 배포 가능.

**vs 원본 FP16（~70 GB）**：크기가 약 4.5배 압축, 학습 효과 + 양자화 정밀도 손실 극소（학습 이득 > 양자화 손실）. 전문가용 그래픽카드（48GB+）가 필요했던 것이 소비자용 그래픽카드로 256K 장문 컨텍스트를 로컬에서 실행 가능해짐.

## 권장 추론 파라미터

로컬 실행 구성（AMD Radeon AI PRO R9700 32GB）을 기준으로 권장 파라미터는 다음과 같습니다：

| 파라미터 | 권장값 | 설명 |
| ----------------- | -------------------------------- | ---------------------- |
| temperature | 0.6 | 창의성과 정확성의 균형 |
| top_p | 0.95 | 핵 샘플링 임계값 |
| top_k | 20 | 절단 샘플링 |
| repeat_penalty | 1.05 | 반복 페널티 |
| presence_penalty | 0 | 존재 페널티 없음 |
| context_length | 262144 | 256K 장문 컨텍스트 |
| batch_size | 2048 | 배치 처리 크기 |
| ubatch_size | 512 | 마이크로 배치 크기 |
| flash_attention | auto | 자동 Flash Attention |
| kv_cache | q4_0 | KV 캐시 양자화（통합 kv-unified） |
| poll | 0 | 유휴 시 GPU 폴링 안 함, 절전·저지연 |
| reasoning | on | 추론 체인（사고 연쇄）활성화 |
| reasoning_budget | 400 | 추론 예산 토큰 수 |
| reasoning_format | deepseek-legacy | 추론 형식 |
| samplers | top_k;top_p;temperature;typ_p | 샘플러 순서 |

### 다른 VRAM 구성 권장

사용자 그래픽카드 구성이 다양하므로, 아래에 다른 VRAM에서의 권장 파라미터를 제시합니다（모두 MoziSmartBit 버전）：

| VRAM | 권장 컨텍스트 길이 | KV 캐시 | 시각 지원 | 설명 |
| ------ | ------- | ----- | ---- | ------------------------------------ |
| 20 GB | 128K | q4_0 | 지원 | 모델+시각 합쳐 ~16.4GB, 실측 128K+시각에 VRAM ~19.5GB만 사용 |
| 24 GB | 256K 풀설정 | q4_0 | 완벽 지원 | 시각+256K장문 컨텍스트, VRAM ~20.4GB 사용, 여유 ~3.6GB |
| 32 GB+ | 256K 풀설정 | q4_0 | 완벽 지원 | 시각+256K장문 컨텍스트, VRAM 여유 ~10GB로 충분, 최강 구성 |

**NVIDIA 그래픽카드 참고표**

| VRAM | 그래픽카드 모델 |
| ----- | ---------------------- |
| 24 GB | RTX 4090 / RTX 3090 Ti |
| 32 GB | RTX 5090 |

**AMD 그래픽카드 참고표**

| VRAM | 그래픽카드 모델 |
| ----- | ------------------- |
| 20 GB | RX 7900 XT |
| 24 GB | RX 7900 XTX |
| 32 GB | Radeon AI PRO R9700 |

**Intel 그래픽카드 참고표**

| VRAM | 그래픽카드 모델 |
| ----- | ------------------------- |
| 32 GB | Arc Pro B70 / Arc Pro B65 |
| 24 GB | Arc Pro B60 |
| 16 GB | Arc Pro B50（CPU 오프로드 병용 필요） |

**CPU 공유 메모리 내장그래픽 장치 참고표**

| VRAM | 프로세서 모델 |
| ------ | -------------------------------------- |
| 128 GB | AMD Ryzen AI Max+ 395（Radeon 8060S 내장그래픽） |
| 128 GB | NVIDIA RTX Spark（Blackwell RTX GPU） |

> 💡 **팁**：VRAM이 위 요건을 만족하면 사용 가능하며 브랜드나 모델은 상관없습니다. NVIDIA / AMD / Intel 각 브랜드의 독립 그래픽카드를 지원할 뿐 아니라 128GB 통합 메모리를 탑재한 내장그래픽/CPU도 지원합니다.
>
> 💡 **팁**：컨텍스트가 길수록 VRAM 사용량이 많아집니다. VRAM 부족（OOM）이 발생하면 `-c` 파라미터 값을 단계적으로 낮추십시오. `--fit on` 파라미터를 사용하면 llama.cpp가 자동으로 레이어 수를 조정해 VRAM에 적응시킵니다.

### Ollama 배포

```bash
# Modelfile 생성
FROM ./moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf

PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 262144
PARAMETER num_gpu 99

# 빌드하고 실행
ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan 배포

LM Studio 또는 Jan에서 `moziAI-35B`를 직접 검색하고 양자화 버전을 선택해 다운로드하면 됩니다.

## 벤치마크 평가

MoziAI-35B-V3.6은 **Ornith-1.0-35B**（deepreinforce-ai）기반으로 파인튜닝되었습니다. MoziAI는 베이스 모델의 뛰어난 에이전트 코딩 능력에 더해 **금융 수직 분야 심층 최적화**를 새롭게 추가하여 금융 Q&A, 퀀트 프로그래밍, 도구 호출 등 시나리오에서 더 뛰어난 성능을 발휘합니다. 범용 능력은 Ornith-1.0-35B 베이스 모델과 동일합니다.

| 벤치마크/Benchmark                         | MoziAI-35B-V3.6（본 모델） | Qwen3.5-35B | Qwen3.6-35B | Gemma4-31B | Qwen3.5-397B | 설명             |
| -------------------------------- | ------------------------- | ----------- | ----------- | ---------- | ------------ | ---------------- |
| **에이전트 코딩**                   |                           |             |             |            |              |                  |
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
| AIME 2026 수학                   | -                         | -           | 94.1        | 89.2       | -            |                  |

\* **Terminal-Bench 2.1 (Terminus-2)**：Harbor/Terminus-2 프레임워크로 평가, 설정 `parser=json`, `temperature=1.0`, `top_p=1.0`, 128K 컨텍스트 윈도우. 실행당 4시간 타임아웃, 32코어 48GB 메모리, 결과는 5회 평균.  
\* **Terminal-Bench 2.1 (Claude Code)**：Claude Code 2.1.126으로 평가, 설정 `parser=json`, `temperature=1.0`, `top_p=1.0`, `max_new_tokens=131072`. 결과는 5회 평균.  
\* **SWE-bench Verified, Pro and Multilingual**：OpenHands 프레임워크로 평가, 설정 `temp=1.0`, `top_p=0.95`, 256K 컨텍스트 윈도우.  
\* **NL2Repo**：설정 `temperature=1.0`, `top_p=1.0`, 400K 컨텍스트, 48K 출력.  

> MoziAI-35B는 Ornith-1.0-35B의 뛰어난 에이전트 코딩 능력을 완전히 계승하고 있습니다. MoziAI의 핵심 차별화는 **금융 수직 분야 심층 최적화**에 있으며, 재무 분석, 퀀트 전략, 리스크 관리·컴플라이언스, 에이전트 도구 호출 등 시나리오에서 범용 모델보다 성능이 현저히 우수합니다.

## SEO 키워드

금융AI 대형언어모델、AI 대형언어모델、로컬 오픈소스 모델、엣지 디바이스 모델、퀀트 프로그래밍、MoziSmartBit、인텔리전트 양자화、GGUF 양자화、MoE 모델、로컬 오픈소스 대형언어모델、로컬 배포、금융AI、도구 호출、Agent、llama.cpp、Ollama、GGUF、Uncensored（무검열）、무심사、면심사、자유 출력、Q3_K_M、Q4_K_M、Q5_K_M、Q6_K、Q8_0、Ornith-1.0-35B、Qwen3.5-35B-A3B、Qwen3.6-35B-A3B、금융 수직 분야、오픈소스 모델.

## 라이선스（중요）

본 모델은 **커스텀 제한적 라이선스**를 채택하고 있으며 구체적인 조항은 다음과 같습니다：

✅ **허용**

- 무료 상업 이용：상업 제품이나 서비스에 무료로 통합 가능
- 복제와 배포：그대로 복제, 다운로드, 배포 가능

상세한 라이선스 조항은 [LICENSE](../LICENSE) 파일을 참고하십시오.

## 면책 조항

본 모델은 "있는 그대로" 제공되며 어떠한 형태의 보증도 하지 않습니다. 모델 출력은 참고용일 뿐 투자 조언을 구성하지 않습니다. 사용자는 스스로 사용 위험을 부담해야 합니다.

## 연락처

- **HuggingFace**：[@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**：[@chenyumo166](https://github.com/chenyumo166)
- **微博**：[@rimochen](https://weibo.com/rimochen)
- **E-mail**：263515@qq.com

***

Copyright (c) 2026 천위모 / chenyumo166. All rights reserved.
