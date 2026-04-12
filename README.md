# Insane Design

> URL 하나로 실제 CSS 기반 디자인 시스템을 추출하는 도구

---

## 이런 분을 위한 도구입니다

- 레퍼런스 사이트의 디자인을 AI에게 시키고 싶지만 "이런 느낌으로" 말고는 전달할 방법이 없는 분
- 디자인 시스템을 직접 만들기엔 시간이 없지만, 프로 수준 결과물이 필요한 분
- Stripe, Linear, Vercel 같은 사이트의 색상/폰트/간격을 정확히 복제하고 싶은 분
- 프론트엔드 작업 시 AI 코딩 에이전트에 디자인 레퍼런스를 첨부하고 싶은 분

---

## 어떻게 작동하나요?

URL을 입력하면 실제 서빙 중인 CSS를 수집하고 분석해서, AI 에이전트가 바로 쓸 수 있는 구조화 문서와 브라우저에서 확인 가능한 인터랙티브 리포트를 생성합니다.

```
URL 입력 → 스크린샷 캡처 → CSS 수집
                                ↓
                         토큰 분석 (색상, 타이포, 간격, 라디우스, 섀도우)
                                ↓
                         design.md + report.html 생성
```

"이 스타일로 만들어줘"에 `design.md`를 첨부하면 AI 에이전트가 실제 디자인 언어로 작업할 수 있습니다.

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

### 3. 업데이트

```
/plugin update
```

> 설치/업데이트 후에는 Claude Code를 **재시작**하세요.

### 사전 요구사항

- Python 3.11+
- Pillow (`pip install Pillow`) — 스크린샷 crop용
- Playwright MCP (권장) — 스크린샷 캡처용

### 처음 시작하기

설치 후 Claude Code를 재시작하고 바로 사용할 수 있습니다.

```
/insane-design https://stripe.com
```

---

## 핵심 기능

### 실제 CSS 기반 분석

피그마 파일이나 스크린샷 추측이 아닌, 실제 서빙되는 CSS를 직접 파싱합니다. 브라우저가 렌더링하는 것과 동일한 스타일 소스를 사용합니다.

### 디자인 토큰 추출

| 토큰 유형 | 추출 항목 |
|-----------|----------|
| 색상 | brand ramp, neutral, accent, semantic |
| 타이포그래피 | heading/text 사이즈, weight, line-height, letter-spacing |
| 스페이싱 | 간격 토큰 시스템 |
| 라디우스 | border-radius 체계 |
| 섀도우 | box-shadow 레이어 |
| 폰트 스택 | 커스텀 폰트 식별 + fallback chain |

### AI 에이전트용 design.md

"이 스타일로 만들어줘"에 첨부할 수 있는 구조화 문서를 생성합니다. AI 코딩 에이전트가 실제 디자인 언어로 작업할 수 있도록 토큰을 정리합니다. Drop-in CSS와 Tailwind Config도 포함됩니다.

### 인터랙티브 HTML 리포트

브라우저에서 열어보는 시각적 리포트로 색상 팔레트, 타이포그래피 스케일, 컴포넌트 클래스를 한눈에 확인할 수 있습니다.

### Quick Start 치트시트

"3가지만 하면 80%"를 재현할 수 있는 핵심 가이드를 포함합니다. 시간이 없을 때 가장 임팩트 큰 부분만 빠르게 적용할 수 있습니다.

### 35개 서비스 검증

Stripe, GitHub, Linear, Notion, Discord, Vercel 등 35개 서비스에서 검증된 파이프라인입니다.

---

## 사용법

| 명령어 | 설명 |
|--------|------|
| `/insane-design [URL]` | URL의 디자인 시스템 추출 |

**자연어 트리거**

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
| 스킬 | `insane-design` — CSS 수집/분석/문서 생성 파이프라인 |

---

## 요구사항

### 필수

- Claude Code
- Python 3.11+
- Pillow (`pip install Pillow`)

### 선택

- Playwright MCP — 스크린샷 캡처 품질 향상 (없으면 curl 기반 fallback 사용)

---

## 라이선스

MIT
