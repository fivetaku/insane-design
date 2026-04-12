# Insane Design

**URL 하나 넣으면 실제 CSS 기반 디자인 시스템이 나옵니다**

"Stripe 느낌으로 해줘"가 잘 안 통하는 이유는 단순합니다.
AI는 느낌을 재현하는 게 아니라, **구체적인 토큰**을 받아야 제대로 만듭니다.

색상, 폰트, 간격, 라디우스, 섀도우 —
이걸 눈대중으로 맞추는 게 아니라 **실제 CSS에서 직접 추출**해야 합니다.

Insane Design은 Stripe부터 Vercel까지 35개 서비스를 분석해 만든 툴이고,
URL 하나만 넣으면 그 사이트의 디자인 시스템을 뽑아줍니다.

---

## 왜 필요한가

- "이런 느낌으로 해줘"가 아니라 실제 디자인 토큰을 AI에게 넘기고 싶을 때
- Stripe, Linear, Vercel 같은 서비스의 스타일을 감이 아니라 정확한 값으로 가져오고 싶을 때
- 디자인 시스템을 처음부터 만들 시간은 없지만 결과물 퀄리티는 포기하고 싶지 않을 때
- AI 코딩 에이전트에게 재현 가능한 디자인 레퍼런스를 함께 주고 싶을 때

---

## 어떻게 작동하나요?

URL 하나만 넣으면 됩니다. 피그마도, 디자이너도 필요 없어요.

```
URL 입력
    ↓
스크린샷 캡처 + 실제 CSS 수집
    ↓
토큰 분석
(색상 ramp, 타이포 스케일, 간격, 라디우스, 섀도우, 폰트 스택)
    ↓
design.md 생성 (AI 에이전트용)
+
report.html 생성 (사람용 인터랙티브 리포트)
```

생성된 `design.md`를 AI 에이전트에 첨부하면, "이 스타일로 만들어줘"가 훨씬 정확하게 동작합니다.

---

## 설치 방법

### 1. 마켓플레이스 등록 (처음 한 번만)

```
/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git
```

### 2. 플러그인 설치

```
/plugin install insane-design
```

> 설치 후에는 Claude Code를 **재시작**하세요.

### 사전 요구사항

**필수**
- Claude Code
- Python 3.11+
- Pillow (`pip install Pillow`)

**선택**
- Playwright MCP — 스크린샷 캡처 품질 향상용. 없으면 curl 기반 fallback으로 동작합니다.

### 빠르게 시작하기

설치 후 Claude Code를 재시작하고 바로 사용할 수 있습니다.

```
/insane-design https://stripe.com
```

---

## 핵심 기능

### 1. 실제 CSS 기반 분석

피그마 파일이나 스크린샷을 보고 추측하지 않습니다.
서비스가 실제로 서빙하는 CSS를 직접 수집하고 파싱합니다.
즉, 브라우저가 렌더링하는 기준과 가장 가깝습니다.

### 2. 디자인 토큰 추출

| 토큰 유형 | 추출 항목 |
|-----------|----------|
| 색상 | brand ramp, neutral, accent, semantic |
| 타이포그래피 | heading/text 사이즈, weight, line-height, letter-spacing |
| 스페이싱 | 간격 토큰 시스템 |
| 라디우스 | border-radius 체계 |
| 섀도우 | box-shadow 레이어 |
| 폰트 스택 | 커스텀 폰트 식별 + fallback chain |

### 3. AI 에이전트용 design.md

"이 스타일로 만들어줘"에 바로 첨부할 수 있는 구조화 문서입니다.
AI가 추상적인 느낌이 아니라 실제 디자인 언어로 작업할 수 있게 정리해줍니다.
Drop-in CSS와 Tailwind Config도 함께 제공합니다.

### 4. 인터랙티브 HTML 리포트

브라우저에서 바로 열어볼 수 있는 시각적 리포트입니다.
색상 팔레트, 타이포 스케일, 컴포넌트 클래스, 섀도우 등을 한눈에 확인할 수 있습니다.

### 5. Quick Start 치트시트

"이 3가지만 적용해도 80%는 닮는다" 수준의 빠른 가이드를 제공합니다.
시간이 없을 때 임팩트가 큰 요소부터 바로 반영할 수 있습니다.

### 6. 35개 서비스 분석 기반

Stripe, GitHub, Linear, Notion, Discord, Vercel 등
35개 서비스를 실제로 분석해 파이프라인을 만들었습니다.
각 서비스의 결과 예시도 함께 포함되어 있어 바로 참고할 수 있습니다.

---

## 사용법

| 명령어 | 설명 |
|--------|------|
| `/insane-design [URL]` | URL의 디자인 시스템 추출 |

**자연어로도 실행 가능**

- "이 사이트 디자인 분석해줘"
- "디자인 시스템 추출해줘"
- "이 URL 디자인 레퍼런스 만들어줘"

---

## 산출물 구조

```
{site-name}/
├── design.md              # AI 에이전트용 디자인 시스템 문서
├── report.ko.html         # 인터랙티브 HTML 리포트
└── screenshots/
    └── hero-cropped.png   # 사이트 스크린샷 (1280×800)
```

---

## 구성요소

| 구성요소 | 설명 |
|----------|------|
| 커맨드 | `/insane-design` — URL 입력 → 디자인 시스템 추출 |
| 스킬 | `insane-design` — CSS 수집, 분석, 문서 생성 파이프라인 |

---

## 요구사항

### 필수

- Claude Code
- Python 3.11+
- Pillow

### 선택

- Playwright MCP — 스크린샷 캡처 품질 향상용

---

## 라이선스

MIT
