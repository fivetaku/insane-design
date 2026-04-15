---
slug: baemin
service_name: 배달의민족
site_url: https://www.baemin.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0CEFD3"
primary_font: BAEMINWORK
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — 배달의민족 (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

배달의민족은 친근하고 유머러스한 한국형 서비스 감성의 디자인이다. 순백 `#FFFFFF` 배경 위에 `#222222` 텍스트가 놓이고, 브랜드 민트 `#0CEFD3`(청록)가 CSS frequency 1위 크로마틱 컬러로 CTA와 강조에 사용된다. Styled Components 런타임 CSS-in-JS로 구현되어 있다.

BAEMINWORK(배민 전용 둥근 폰트, 무료 배포)가 전체 UI에 사용되어 친근한 글자 형태를 만든다. 굵은 weight(600~800) 중심의 타이포그래피와 `-webkit-tap-highlight-color: rgba(0,0,0,0)` 터치 최적화가 모바일 우선 설계를 보여준다.

**Key Characteristics:**
- 브랜드 민트 `#0CEFD3` (파란색/초록이 아님)
- BAEMINWORK 둥근 폰트 (무료 배포, 재사용 가능)
- Styled Components 런타임 CSS-in-JS
- 굵은 weight(600~800) 중심 타이포
- 모바일 우선 터치 최적화

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 배달의민족처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'BAEMINWORK', -apple-system, BlinkMacSystemFont,
               'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #222222; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0CEFD3; }
```

**절대 하지 말아야 할 것 하나**: 배민 브랜드 색을 파랑이나 초록으로 기억하는 것. 실제 CSS에서 frequency 10회로 압도적 1위인 크로마틱 색은 `#0CEFD3` — 민트/청록 계열이다. `#181A1C`(9회)는 SVG 패턴으로 UI 색이 아니다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.baemin.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Styled Components (`/*!sc*/` 주석 패턴) |
| Token prefix | N/A (Styled Components, 리터럴 hex) |
| Method | CSS hex frequency 분석 · 셀렉터 역할 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React + Styled Components (`/*!sc*/` 주석으로 확인)
- **Design system**: 배민 내부 커스텀 — `BAEMINWORK` 폰트 중심
- **CSS architecture**: Styled Components 런타임 CSS-in-JS
  ```
  /*!sc*/ 인라인 주입 스타일
  global reset (input, textarea, button 등)
  component-scoped (동적 해시 클래스)
  ```
- **Class naming**: Styled Components 동적 해시 (빌드마다 변경)
- **Default theme**: light (bg = `#FFFFFF`, fg = `#222222`)
- **Font loading**: 자체 호스팅 (`BAEMINWORK` — 배민 전용 둥근 폰트)
- **Canonical anchor**: `#0CEFD3` — CSS frequency 1위 크로마틱, 배민 민트

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `BAEMINWORK` (배달의민족 전용, 무료 배포)
- **Code font**: `source-code-pro`, Menlo, Monaco, Consolas
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --baemin-font-family: 'BAEMINWORK', -apple-system, BlinkMacSystemFont,
                        'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
  --baemin-font-weight-normal: 400;
  --baemin-font-weight-bold: 700;
}
body {
  font-family: var(--baemin-font-family);
  font-weight: var(--baemin-font-weight-normal);
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  color: #222222;
}
```

> `BAEMINWORK`는 배달의민족이 무료 배포하는 폰트로 재사용 가능. 둥글둥글한 친근한 글자 형태.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ Styled Components 런타임 CSS라 토큰 구조 파악 제한. weight 분포: 600(2회), 700(4회), 800(2회) — 굵은 weight 중심.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body-base | N/A | 400 | N/A | N/A |
| ui-medium | N/A | 500 | N/A | N/A |
| ui-semibold | N/A | 600 | N/A | N/A |
| heading | N/A | 700~800 | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (1 step)

| Token | Hex |
|---|---|
| brand-mint | `#0CEFD3` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| black | `#000000` | — |
| text-body | `#222222` | — |
| text-secondary | `#7E8082` | — |
| border-muted | `#B1B3B5` | — |
| bg-muted | `#F6F6F6` | — |
| bg-muted2 | `#F7F7F7` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| brand-mint | `#0CEFD3` | 브랜드 민트 (CTA, 강조) |
| text-base | `#222222` | 버튼, 링크, 기본 텍스트 |
| bg-svg-dark | `#181A1C` | SVG 패턴 전용 (UI 색 아님) |
| text-disabled | `#B1B3B5` | 비활성 상태 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — Styled Components 런타임이라 스페이싱 토큰 파악 제한

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — CSS에서 명시적 radius 토큰 확인 불가

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 모바일 네비게이션, 터치 타겟 44px+ |
| Tablet | 640-1024px | 2컬럼 그리드, 사이드 패딩 증가 |
| Desktop | 1024-1280px | 풀 그리드 레이아웃, 확장 네비게이션 |
| Large | >1280px | max-width 컨테이너, 중앙 정렬 |

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Global Input Reset (`input, textarea, button, select, a`)

```html
<button type="button">주문하기</button>
```

| 속성 | 값 |
|---|---|
| -webkit-tap-highlight-color | rgba(0,0,0,0) |
| color | `#222222` |
| text-decoration | none |
| -webkit-appearance | none |
| outline | none |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 친근하고 유머러스 | "배달이 됩니다" |
| Primary CTA | 단순 명확 | "주문하기" |
| Tone | 활기차고 따뜻 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* 배달의민족 — copy into your root stylesheet */
:root {
  /* Fonts */
  --baemin-font-family: 'BAEMINWORK', -apple-system, BlinkMacSystemFont,
                        'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
  --baemin-font-weight-normal: 400;
  --baemin-font-weight-bold: 700;

  /* Brand */
  --baemin-color-brand: #0CEFD3;

  /* Surfaces */
  --baemin-bg-page: #FFFFFF;
  --baemin-text: #222222;
  --baemin-text-muted: #7E8082;

  /* Border */
  --baemin-border: #B1B3B5;
  --baemin-bg-muted: #F6F6F6;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#0CEFD3` |
| Page BG | `#FFFFFF` |
| Text Primary | `#222222` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "배달의민족 스타일 hero — `BAEMINWORK` 폰트, `#0CEFD3` brand color, light 배경"
>
> **CTA button**: "배달의민족 primary CTA — brand `#0CEFD3` 배경 또는 dark fill, `BAEMINWORK` 폰트"
>
> **Card component**: "배달의민족 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 브랜드 색은 `#0CEFD3` 민트 (청록)
- `BAEMINWORK` 폰트 — 무료 배포, 재사용 가능
- 기본 텍스트 색은 `#222222` (순수 검정 아님)
- `-webkit-tap-highlight-color: rgba(0,0,0,0)` 터치 하이라이트 제거

### ❌ DON'T
- `#181A1C`를 배민 브랜드 색으로 사용 — SVG 패턴 전용
- Styled Components 해시 클래스 직접 복사 — 빌드마다 변경됨
- 배민 색을 파란색이나 초록으로 기억 — 실제는 민트(`#0CEFD3`)
