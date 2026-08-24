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







# MoziAI-V3.7-35B-A3B-MOE - 무료 로컬 배포 가능한 소형 고성화멀티모델AI







[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | 한국어 | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md)







## 모델 개요







MoziAI-35B-A3B-MOE는 중국 금융 인플루언서 천위모(Chen Yumo) 팀이 개발한 로컬 오픈소스 금융 AI 멀티모달 LLM(비전 및 도구 호출 지원)입니다. moziAI-35B는 오픈소스 베이스 모델 Ornith-1.5-35B-A3B(Qwen3.5-35B-A3B / Qwen3.6-35B-A3B 아키텍처, MIT 라이선스)를 기반으로, 천위모 팀의 자체 개발:(금융 데이터 + 금융 영역 역량 + 훈련 방법 + 7차원 사고 체계 + 에이전트 LOOP 메커니즘 + 하이브리드 양자화 알고리즘 MoziSmartBit)을 결합하여 개발되었습니다. 자체 개발한 MoziSmartBit 지능형 양자화 기술을 통해 350억 파라미터 MoE 모델을 약 15.5 GB로 압축하여, 기존 Q4_K_M 양자화 모델(약 22+GB)보다 6.5G(약 30%) 작습니다. 정밀도와 크기 사이의 최적 균형을 달성하여 거의 무손실인 ≈FP16의 99% 정밀도 품질을 구현합니다.







범용 AI 대모델의 능력을 유지하는 것 외에도, 이 모델은 다음을 강화합니다: 금융 수직 도메인 애플리케이션, 금융 Q&A, 정량 프로그래밍, 도구 호출 및 일반 프로그래밍, 그리고 모델의 7차원 사고 능력, LOOP 메커니즘, 다양한 에이전트 플랫폼 호환성.







모델 개발한천위모는 이 모델을 로컬 금융 데이전분석, 양적 전략 R&D, 시장 조사, 기사 작성, 전체 프로젝트 진행, 일반 프로그래밍 및 openclaw/hermes를 통한 256K 컨텍스트 작업에자주 사용합니다 소비자등급 GPU에서 로컬 배포 가능하며 상당한 클라우드 토큰 비용자절약하고 로컬 데이전프라이버시와 보안을보장하면서7X24 토큰 자유지달성합니다







llama.cpp, Ollama, LM Studio 등 기타 주류 추론 프레임워크를 지원합니다.







**출시각 2026-08-21** | **버전: V3.7**







## 모델 특징







- **금융 수직 영역 특화**: 금융 Q&A, 양적 프로그래밍 및 도구 호출력대형심층 최적화



- **MoziSmartBit 지원양자화*: 자체 개발 스마크양자화 정밀도와 크기술최적 균형, **15.5 GB**로 압축



- **소비자등급 배포**: 20GB 또는 24GB+ VRAM 소비자 GPU에서 배포 가능 256K 컨텍스트 지원



- **다국어지원*: 201개 언어 및 방언, 향상업중국어능력, 영어/일본어한국어독일을프랑스어/스페인어/포르투갈어등지원



- **일반 프로그래픽*: 풀스택 개발, 코드 디버전 아키텍처 설계, 스크립트 작성, Python/JS/TS/Go/Rust 등 기타 주류 언어 지원



- **기사 작성**: 연구 보고표 분석 기사, 기술 문서, 창의미콘텐츠를 포함되고품질다장문글쓰기



- **비전 이해**: 멀티모델비전 지원 로컬 스크린샷 입력, 이미지 이해



- **검열없는 자유 출력**: 콘텐츠검열없음, 안전 제한 없이 모든 주제한대형자유롭게 논의



- **향상업추론**: 사고표사슬(Chain-of-thought) 훈련으로 추론 품질 향상



- **다중 프레임워크지원*: llama.cpp, Ollama, LM Studio, Jan 호환



- **멀티에이전트플랫폼지원*: OpenClaw, Hermes, OpenCode, Cursor, Windsurf, Claude Code, Codex 등 기타 주류 AI IDE 및 에이전트 프레임워크와 심층 통합, 도구 호출, 멀티턴 작업 오케스트레이션을 네이티브 지원 바로 사용 가능







## 검열없는 출력을장점







이모델은 Ornith-1.5-35B-A3B 기본 모델은**Uncensored** 기능력계승하며, 다음과같은 장점이있습니다:







| 장점 | 설명 |
|------|------|
| **검열없음** | 민감하거의논쟁적인 콘텐츠를 포함되모든 주제한거부하지 않음 |
| **자유 출력** | 안전 정책임제한국받지 않고, 모든 유형식응답도생성화이있음 |
| **완전트정보** | 필터링되지 않은 완전트정보다제공하여, 연구 및 분석에 적합 |
| **로컬 프라이버전* | 로컬 배포함데이터가 완전트비공개이전 클라우드 검열로부도자유로움 |
> **사용 사례**: 학술 연구, 심층 분석, 자유 논의, 제한 없는 AI 대형



> **참고**: 이 모델은 로컬 배포 모델이며, 출력 콘텐츠는 사용자가 완전트제어합니다 콘텐츠관리책임워없습니다.







## 핵심 기능







| 기능 영역 | 설명 |
|-----------|------|
| 시장 분석 | 거시/미시경제 해석, A/HK/미국 주식/원자화암호화폐 시장 논리 |
| 재무 보고표| 주요 재무 지원해석, 리서치보고표요약, 밸류에이전및실적 전망 지원|
| 리스트및컴플라이언스 | 상품 리스트평가, 투자 권고 컴플라이언스, 금융 규제 정책 해석 |
| 양적 전략 | 양적 전략 설계, Pyramid(PEL) 양자화 백테스팅 로직, 팩터 구축 및 도구 호출 |
| 도구 호출 | 실시각시세, 데이터베이스, 리서치보고표검열및기타 금융 데이전소스 통합 |
## 기술 사양







| 항목 | 사양 |
|------|------|
| 기본 모델 | Ornith-1.5-35B-A3B (**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B**, MIT 라이선스) |
| 파라미터 | 35B MoE (256개 라우팅전문가 + 1개 공유 전문가, 토큰당 8개 활성) |
| 양자화| 자체 개발 MoziSmartBit 지원양자화+ GGUF 표준 형식 |
| 컨텍스트 길이 | 256K (262,144 토큰) |
| 모델 크기 | ~15.5 GB (MoziSmartBit Uncensored 버전) |
| 최소 VRAM | 20GB+ VRAM 소비자GPU (예: RTX 4060 Ti 16G CPU 오프로드 사용 시, 24 GB 권장 (비전 + 긴 컨텍스트) |
| 추론 프레임워크| llama.cpp / Ollama / LM Studio / Jan |
| 추론 속도 | 알고리즘 최적화 AMD R9700 GPU에서 140+ token/s, AMD MAX+395 CPU iGPU에서 70+ token/s, 로컬 토큰 자유 |
| 팀 | 천위모팀 |
## 양자화형식 및 모델 크기 비교







| 양자화형식 | 모델 크기 | 정밀도| 비고 |
|------------|-----------|--------|------|
| **FP16 (원본)** | ~70 GB | 100% | 원본 16bit |
| **MoziSmartBit** | **~15.5 GB** | **~99%** | **MoziAI가 사용하는 최적화양자화방식** |
| Q4_K_M | ~22 GB | ~98% | GGUF 표준 4bit |
| Q5_K_M | ~24.7 GB | ~99% | 높은 품질 |
| Q6_K | ~28.5 GB | ~99.5% | 거의 무손실|
| Q8_0 | ~36.9 GB | ~100% | 무손실|
> MoziAI V3.7은 MoziSmartBit 지원양자화를 사용하여 ~99% 정밀도를 유지하면서35B 파라미터 MoE 모델은~15.5 GB(~4.5x 압축비로 압축하며, 추론 품질을소비자GPU 배포 간소화의 균형식맞추론있습니다.







## MoziSmartBit 지원양자화







기존 양자화는 모든 레이어에 균일을정밀도를 적용합니다 **MoziSmartBit 지원 양자화**의 최적화 크기-정밀도균형식위해 차별화된 양자화전략을적용합니다







### 압축 효과







기존 양자화는 모델은모든 부분을 균일하게 압축하여 종종 상당한 정밀도 손실행초래합니다 MoziSmartBit 지원양자화는 자체 개발한지원압축 전략을사용하여 **최소한의 정밀도손실행상당한 크기 축소비달성**합니다







- **최소 양자화손실**: 훈련 효과 > 양자화손실. 훈련된 MoziAI-35B가 금융 영역 텍스트에서사전 훈련 bf16 기본 모델보다 더 나은 PPL을 달성하며, 유사 AI 모델 대형 환각을 혼란스perplexity)를 줄입니다



- **~4.5x 크기 축소**: ~70 GB(FP16)에서 ~15.5 GB로 압축, Q4_K_M(~21 GB)보다운크게 작아 VRAM 및 저장소 요구 사항은크게 낮춤



- **소비자GPU 친화는*: 이전트고급 GPU가 필요했던 35B MoE 모델은이제 20GB~24GB VRAM에서 원활하게 실행 가능







### 비교 우위







**Q4_K_M(~22 GB) 대비**: ~30% 더 작음(~15.5 GB), 정밀도는 Q4_K_M보다 **높음**, VRAM 진입 장벽이 낮음 한 중급 소비자GPU(24GB)에서 원활하게 실행 가능







**FP16 원본(~70 GB) 대형*: ~4.5x 압축, 훈련 효과 + 최소한의 양자화손실(훈련 효과 > 양자화손실), 전문가능하드웨어 대형소비자GPU에서 로컬 256K 컨텍스트 배포 가능







## 추천 추론 매개변수







로컬 프로덕션 설정(AMD Radeon AI PRO R9700 32GB) 기반:







| 매개변수 | 값 | 설명 |
|----------|------|------|
| temperature | 0.6 | 창의성과 정확성의 균형 |
| top_p | 0.95 | 뉴클리어떤샘플릿임계승|
| top_k | 20 | 잘라내기 샘플릿(V3.7 최적화 |
| repeat_penalty | 1.05 | 반복 페널티|
| presence_penalty | 0 | presence 페널티없음 |
| context_length | 262144 | 256K 컨텍스트 |
| batch_size | 2048 | 배치 크기 |
| ubatch_size | 512 | 마이크로 배치 크기 |
| flash_attention | auto | 자동 Flash Attention |
| kv_cache | q4_0 | KV 캐시 양자화(kv-unified) |
| poll | 0 | 유휴 시 GPU 폴링 없음, 에너지 효율적 |
| reasoning | on | 추론 체인 활성화(chain of thought) |
| reasoning_budget | 400 | 추론 예산(토큰 단위) |
| reasoning_format | deepseek-legacy | 추론 형식 |
| samplers | top_k;top_p;min_p;temperature;dry;typ_p | 샘플릿순서 |
### llama.cpp 실행 명령（







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







### VRAM 구성 권장 사항







사용자GPU 구성화각기 다르므로 VRAM 크기술따른 권장 매개변수를 안내합니다(모두 MoziSmartBit 버전 기준):







| VRAM | 권장 컨텍스트 | KV 캐시 | 비전 지원| 비고 |
|------|---------------|---------|-----------|------|
| 20 GB | 150K | q4_0 | 지원| 모델+비전 ~16.4GB, 실제 테스트에서200K+비전 사용 시 ~19.5GB VRAM 소요 |
| 24 GB | 256K 풀 | q4_0 | 완전 지원| 비전+256K 컨텍스트, ~20.4GB VRAM 소요, ~3.6GB 여유 |
| 32 GB+ | 256K 풀 | q4_0 | 완전 지원| 비전+256K 컨텍스트, ~10GB 충분야여유, 최적 구성 |
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
**공유 메모델iGPU**







| VRAM | 프로세서 |
|------|----------|
| 128 GB | AMD Ryzen AI Max+ 395 (Radeon 8060S iGPU) |
| 128 GB | NVIDIA RTX Spark (Blackwell RTX GPU) |
> 💡 **팁**: VRAM이 요구 사항을 충족하면 작동합니다 브랜드나 모델 제한 없습니다. NVIDIA / AMD / Intel 독립 GPU 목록을 128GB 통합 메모리 iGPU를 지원합니다.







> 💡 **팁**: 더 긴 컨텍스트를 더 많은 VRAM을 사용합니다 OOM(메모델부도이발생하면 `-c` 값을 점진적으로줄이세요. `--fit on`을 사용하면 llama.cpp가 VRAM에 맞게 자동으로 레이어를 조정합니다







### Ollama 배포







```bash



# Modelfile 생성



FROM ./moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf







PARAMETER temperature 0.6



PARAMETER top_p 0.95



PARAMETER top_k 20



PARAMETER num_ctx 262144



PARAMETER num_gpu 99







# 빌드 및 실행



ollama create moziAI-35B -f Modelfile



ollama run moziAI-35B



```







### LM Studio / Jan 배포







LM Studio 또는 Jan에서 `moziAI-35B`를 검색하며 MoziSmartBit 양자화버전트다운로드하세요







## 벤치마크 평가







MoziAI는 **deepreinforce-ai/Ornith-1.5-35B-A3B**에서 파인튜닝되었습니다 MoziAI는 기본 모델 위에서금융 수직 영역에 최적화되어 금융 Q&A, 양적 프로그래밍 및 도구 호출 시나리오에서 우수직성능력제공합니다 MoziAI-35B의 일반 기능은 Ornith-1.5-35B-A3B 기본 모델은일치합니다







| Benchmark | moziAI-13.7-35B-A3B | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
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
> MoziAI-35B의 일반 벤치마크 점수직Ornith-1.5-35B-A3B 기본 모델은일치합니다 금융 수직 영역은 MoziAI의 핵심 최적화방향으로, 재무제표 분석, 양적 전략, 리스트및컴플라이언스, 에이전트 도구 호출 시나리오에서 일반 모델은크게 능가합니다 Gemma4 / Qwen3.6 데이터는 공식 공개 결과에서 가져왔습니다







## 모델 다운로드







모델 크기가 크기(~15.5 GB) 때문가 가중치마여러 커뮤니티 플랫폼에 호스팅됩니다:







| 플랫폼| URL |
|--------|-----|
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP-Uncensored) |
| GitHub | [chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP-Uncensored) |
> 💡 **LM Studio 사용자*：[LM Studio](https://lmstudio.ai)에서 `moziAI`를 검색하며원클릭으로다운로드하이있습니다.



> 💡 **다운로드 팁**: 이 링크기클릭하여 HuggingFace 저장소비이동으다음, **"Files and versions"** 탭에서V3.7 디렉토리 아래픽모든 파일(메인 모델, 비전 프로젝션, 채팅 템플릿이다운로드하세요. 모든 파일 모두 동일을디렉토리전배치해야 합니다







### ⚠️ 중요: 비전 기능에는 mmproj 파일을필요합니다







이모델은 멀티모델비전트지원합니다. **비전 프로젝션 파일(mmproj)**은 버전 디렉토리전포함되어 있습니다:







- **비전 파일**: `moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf` (~903 MB, BF16 정밀도



- **배치 위치**: GGUF 모델 파일을동일을버전 디렉토리



- **로딩**: llama-server 시작 시 `--mmproj` 플래그로 로드







```bash



llama-server -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \



  --mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf



```







> 비전 파일 없이전모델은**이미지 이해 능력을손실**되며 텍스트전용 대화만 유지됩니다







## 빠른 시작







### 1. 모델 파일 다운로드







HuggingFace / ModelScope에서 V3.7 디렉토리전모든 파일을다운로드합니다







```



V3.7/



├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf      # 메인 모델 (필수)



├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf  # 비전 프로젝션 (선택)



└── moziAI-V3.7-35B-chat-template.jinja                  # 채팅 템플릿(권장)



```







### 2. 추론 서버 시작







전체 권장 구성은 위의 [llama.cpp 실행 명령어](#llamacpp-실행-명령（을 참조하세요







최소 실행(핵심 매개변수만):







```bash



llama-server \



  -m V3.7/moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \



  --chat-template-file V3.7/moziAI-V3.7-35B-chat-template.jinja \



  -c 262144 -ngl 99



```







> 비전 기능력위해 `--mmproj V3.7/moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf`를 추가하세요







### 3. 사용 시작







브라우저에서 `http://localhost:8080`를 열고 채팅되시작하세요







### 디렉토리 구조







```



moziAI-35B/



├── README.md              # 중국어버전



├── README.en.md           # README 파일 (영어)



├── LICENSE                # 라이선스



├── V3.7/                  # V3.7 버전 (자체 포함)



├── RELEASE_NOTES.md                       # 릴리전노트



├── moziAI-35B-V3.7-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf    # 메인 모델



├── moziAI-V3.7-35B-uncensored-heretic-mmproj-BF16.gguf # 비전 프로젝션



└── moziAI-V3.7-35B-chat-template.jinja   # 채팅 템플릿



```







향후 업그레이전계획은 [未来升级计划.md](未来升级计划.md)를 참조하세요







## SEO 키워크







financial AI LLM, 로컬 오픈소스 모델, 엔드사이전모델, 양적 프로그래픽 MoziSmartBit, 지원양자화 GGUF 양자화 MoE 모델, 로컬 오픈소스 LLM, 로컬 배포, 금융 AI, 도구 호출, Agent, llama.cpp, Ollama, GGUF, Uncensored, 검열없음, 자유 출력, 제한 없음, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, Ornith-1.5-35B-A3B, Qwen3.5, Qwen3.6, 금융 수직 영역, 오픈소스 모델







## 라이선스 (중요)







이모델은 **커스텀 제한 라이선스**를 사용합니다







### ✅ 허용



- **무료 상업에사용**: 상업 제품질자유롭게 통합 가능



- **복사 및 배포**: 복사, 다운로드, 공유 가능







### ❌ 금지



- **파생 작품**: 모델 또는 그 일부를수정, 번역, 적응, 병합 또는 파인튜닝 금지



- **재판매**： 모델은단독으로 또는 제품질일부도판매 금지



- **재라이선스*: 서브라이선스 부도금지







### 📋 요구 사항



- 원본 저작권 고지 유지 필수



- 저작자 표시: moziAI-35B







> 전체 조건은 [LICENSE](./LICENSE)를 참조하세요







## 면책 조항







있는 그대형제공되며 보증류없습니다. 모델 출력은 참고용이전투자 권유가 아닙니다. 사용자가 모든 리스크를 부담합니다.







## 연락처







- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)



- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)



- **Weibo**: [@rimochen](https://weibo.com/rimochen)



- **이메인*: 263515@qq.com







---







Copyright (c) 2026 Chen Yumo / chenyumo166. All rights reserved.