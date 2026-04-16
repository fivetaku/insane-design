[English](README.md) | 한국어

# insane-design

> **URL 하나. 실제 CSS. 그게 다입니다.**

"Stripe 느낌으로 해줘"가 잘 안 통하는 이유는 단순합니다. AI는 느낌이 아니라 토큰을 받아야 합니다. insane-design은 어떤 사이트든 CSS를 직접 가져와 실제 디자인 시스템을 추출하고, AI 에이전트가 바로 쓸 수 있는 `design.md`와 브라우저에서 열 수 있는 인터랙티브 HTML 리포트를 만들어줍니다.

[Quick Start](#quick-start) • [왜 insane-design인가](#왜-insane-design인가) • [작동 방식](#작동-방식) • [기능](#기능) • [요구사항](#요구사항)

---

## Quick Start

### 1. 마켓플레이스 등록 (처음 한 번만)

```
/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git
```

### 2. 플러그인 설치

```
/plugin install insane-design
```

### 3. Claude Code 재시작

플러그인이 로드되려면 재시작이 필요합니다.

### 4. 실행

```
/insane-design https://stripe.com
```

자연어도 됩니다. "이 사이트 디자인 분석해줘"처럼 말하면 커맨드가 알아서 처리합니다.

---

## 왜 insane-design인가

- **LLM 추론이 아닙니다** — CSS를 직접 수집하고 파싱합니다. hex 값은 실제 스타일시트에서 나옵니다. 환각 없음.
- **AI 에이전트용 산출물** — `design.md`는 AI 에이전트에게 첨부하도록 구조화되어 있습니다. 프롬프트에 붙이면 감이 아니라 재현 가능한 결과물이 나옵니다.
- **100개 사전 분석 사이트 포함** — Stripe, Apple, Linear, Vercel, 토스, Nike, Figma, Notion 외 92개. 분석 없이 바로 적용 가능.
- **두 가지 모드, 하나의 커맨드** — 새 URL을 분석하거나, 기존 디자인 시스템을 프로젝트에 적용. 같은 커맨드가 둘 다 처리합니다.
- **Drop-in CSS + Tailwind 설정 포함** — 바로 붙여넣을 수 있는 CSS 변수와 Tailwind `theme.extend` 설정이 함께 나옵니다. 수동 번역 불필요.
- **인터랙티브 HTML 리포트** — 클릭하면 복사되는 컬러 스와치, 라이브 타이포 프리뷰, 스페이싱 바, 섀도우 데모 카드. 한 파일에 전부.
- **Quick Start 치트시트** — "이 세 가지만 적용해도 80%는 닮는다." 임팩트 순서로 정리.

---

## 작동 방식

```
URL 입력
  ↓
HTML + CSS 파일 수집 (실제 스타일시트 번들, Chrome UA 사용)
  ↓
CSS 커스텀 프로퍼티 파싱
추출: 컬러 램프 · 타이포그래피 스케일 · 스페이싱 토큰
     라디우스 체계 · 섀도우 레이어 · 폰트 스택
  ↓
스크린샷 기반 시각 검증 (Playwright 또는 curl fallback)
확인: 브랜드 컬러 · light/dark 테마 · 폰트 렌더링
  ↓
design.md 생성               report.html 생성
(AI 에이전트용 레퍼런스)     (인터랙티브 브라우저 리포트)
```

결과물은 `{site-slug}/`에 저장됩니다:

```
stripe/
├── design.md              # AI 에이전트용 — 16섹션 구조화 문서
├── report.ko.html         # 인터랙티브 HTML 리포트
└── screenshots/
    └── hero-cropped.png   # 1280×800 스크린샷
```

---

## 기능

### 커맨드

| 커맨드 | 설명 |
|--------|------|
| `/insane-design [URL]` | 사이트 분석 — 디자인 시스템 추출, `design.md` + HTML 리포트 생성 |
| `/insane-design [slug]` | 사전 분석된 디자인을 내 프로젝트에 적용 |
| `/insane-design:analysis [URL]` | 분석 모드만 실행 |
| `/insane-design:apply [slug]` | 적용 모드만 실행 |

자연어도 인식합니다. "이 사이트 분석해줘"는 analysis 모드, "Stripe 스타일 적용해줘"는 apply 모드로 진입합니다.

### 추출되는 디자인 토큰

| 토큰 유형 | 추출 항목 |
|-----------|----------|
| 색상 | 브랜드 램프, 뉴트럴 램프, 액센트 패밀리, 시맨틱 alias |
| 타이포그래피 | heading/body 스케일 — 사이즈, weight, line-height, letter-spacing |
| 스페이싱 | 전체 간격 토큰 시스템 |
| 라디우스 | border-radius 체계 |
| 섀도우 | box-shadow 레이어 (멀티 레이어 스택 포함) |
| 폰트 스택 | 커스텀 폰트 식별 + fallback chain |

### design.md 구조 (16섹션)

| 섹션 | 내용 |
|------|------|
| 01 Quick Start | 3단계 CSS 스니펫 — "5분 만에 80% 닮게" |
| 02 Provenance | 소스 URL, 수집 날짜, CSS 바이트 수 |
| 03 Tech Stack | 프레임워크 및 DS 네임스페이스 감지 |
| 04–05 Typography | 폰트 스택 + 전체 스케일 |
| 06 Colors | 브랜드 램프 · 뉴트럴 · 액센트 · 시맨틱 레이어 |
| 07–09 Spacing / Radius / Shadows | 전체 토큰 테이블 |
| 12 Components | BEM 클래스 패턴, 컴포넌트 변형 |
| 14 Drop-in CSS | 바로 붙여넣기 가능한 `:root {}` CSS 변수 |
| 15 Tailwind Config | `theme.extend` 설정 |
| 16 DO / DON'T | 이 사이트에서 가장 흔한 실수 하나 |

### Apply 모드 — 프로젝트에 토큰 주입

globals.css, Tailwind 설정, 일반 CSS 파일을 자동 감지하고 기존 설정을 건드리지 않고 디자인 토큰을 주입합니다.

| 대상 | 처리 방식 |
|------|----------|
| `:root {}` 있는 CSS | 기존 블록 내부에 토큰 추가 |
| `:root {}` 없는 CSS | 파일 최상단에 새 `:root {}` 생성 |
| Tailwind 설정 | `theme.extend.colors`, `fontFamily`, `borderRadius` 업데이트 |
| 재적용 | `/* insane-design */` 블록 전체 교체 |

### 100개 사전 분석 사이트

Stripe, Apple, Linear, Vercel, Notion, Figma, GitHub, Discord, Slack, Spotify, 토스, 배민, 당근, 카카오, 네이버, Nike, Gucci, Chanel, Tesla, Ferrari, BMW 외 79개. 분석 없이 바로 적용 가능합니다.

---

## 요구사항

### 필수

- [Claude Code](https://docs.anthropic.com/claude-code)
- Python 3.11+
- Pillow (`pip install Pillow`)

### 선택

- **Playwright MCP** — 스크린샷 캡처 품질 향상용. 없으면 curl 기반 fallback으로 동작합니다.

---

## 라이선스

MIT

---

<div align="center">

**실제 CSS. 느낌이 아닙니다.**

</div>
