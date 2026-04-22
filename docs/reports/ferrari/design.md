---
slug: ferrari
service_name: Ferrari
site_url: https://ferrari.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#DA0000"
primary_font: N/A
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Ferrari (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Ferrari처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Neue Haas Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1A1A; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #DA0000; }
```

**절대 하지 말아야 할 것 하나**: Ferrari 레드를 UI 전반에 과용하는 것. Ferrari 마케팅 사이트는 극도로 절제된 레이아웃을 사용하며 레드는 로고와 핵심 accent에만 나타난다. CSS 파싱에서 어떤 chromatic 컬러도 감지되지 않을 만큼 레드는 절제되어 있다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://ferrari.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

> **참고**: Ferrari 사이트의 CSS 파싱 결과 어떤 chromatic 후보도, font-family도 감지되지 않음. 사이트가 고도로 인라인화 또는 JS 렌더링 방식이라 정적 CSS 파싱이 제한됨.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼)
- **Design system**: Ferrari 내부 디자인 시스템 (미공개)
- **CSS architecture**: N/A (토큰 시스템 미노출)
- **Class naming**: N/A
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: N/A (CSS에서 미감지)
- **Canonical anchor**: N/A (CSS 데이터 없음)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: N/A (CSS에서 미감지)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

> **참고**: CSS 파싱에서 font-family가 전혀 감지되지 않음. 시각적으로 Ferrari 사이트는 sans-serif 계열을 사용하는 것으로 관찰되나 CSS 데이터 기반 확인 불가.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

> N/A — CSS 파싱에서 어떤 color 후보도 감지되지 않음.

> **참고**: Ferrari 마케팅 사이트의 CSS는 정적 파싱으로 컬러 정보를 추출할 수 없었음. 브랜드 레드는 Rosso Corsa(`#DA0000`)로 알려져 있으나 이는 CSS 데이터가 아닌 공개 브랜드 정보.

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: manual -->

### Hero Section

```html
<section class="hero">
  <div class="hero__media">
    <!-- 차량 전체 폭 영상 또는 사진 -->
  </div>
  <div class="hero__overlay">
    <h1>Ferrari SF90 Stradale</h1>
    <a href="#" class="cta">Discover</a>
  </div>
</section>
```

| 속성 | 값 |
|---|---|
| hero 배경 | 차량 전체 폭 영상/사진 |
| 오버레이 | 그라디언트 (어두운 → 투명) |
| H1 색상 | `#FFFFFF` |
| CTA 배경 | `#DA0000` 또는 `transparent + white border` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명 전체, 이탤릭 없이 | "Ferrari SF90 Stradale" |
| Primary CTA | 발견 유도 | "Discover" / "Configure" |
| Secondary CTA | 탐색 | "Find a Dealer" |
| Subheading | 퍼포먼스 수치 | "1000 hp · V8 hybrid" |
| Tone | 열정적이나 절제됨, 이탈리안 프리미엄 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Ferrari — copy into your root stylesheet */
/* ⚠️ CSS 파싱 데이터 없음. 브랜드 가이드라인 기반 추정값 */
:root {
  /* Fonts (CSS 미감지 — 시각 관찰 기반) */
  --ferrari-font-family: "Neue Haas Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --ferrari-font-weight-normal: 400;
  --ferrari-font-weight-bold: 700;

  /* Brand (공개 브랜드 가이드 — CSS 미확인) */
  --ferrari-color-rosso-corsa: #DA0000;

  /* Surfaces */
  --ferrari-bg-page: #FFFFFF;
  --ferrari-bg-dark: #1A1A1A;
  --ferrari-text: #1A1A1A;
  --ferrari-text-on-dark: #FFFFFF;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- Ferrari 레드를 로고, 주요 CTA에만 절제적으로 사용
- Hero는 차량 전체 폭 고화질 사진/영상으로 채우기
- 레이아웃 최대한 여백 넓게, 그리드 정교하게
- 모델명을 그대로 headline으로 사용

### ❌ DON'T
- Ferrari 레드를 배경 전체에 쓰지 말 것
- 과장된 마케팅 문구 쓰지 말 것
- CSS 데이터 없는 값을 확정적으로 사용하지 말 것
- 레이아웃을 복잡하게 만들지 말 것 — 미니멀이 핵심
