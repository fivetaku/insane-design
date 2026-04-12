---
slug: {SLUG}
service_name: {SERVICE_NAME}
site_url: {SITE_URL}
fetched_at: {FETCHED_AT}
default_theme: {light|dark|mixed}
brand_color: {BRAND_HEX}
primary_font: {PRIMARY_FONT}
font_weight_normal: {WEIGHT_NORMAL}
token_prefix: {TOKEN_PREFIX}
---

<!--
  DesignMD Analyzer — DESIGN.claude.manual.md 템플릿
  버전: 2.0 (2026-04-11)

  섹션 번호: 01~15 (통일)
  Quick Start = 01, Provenance = 02, Tech Stack = 03 ...

  N/A 처리 규칙:
  - 섹션 전체 생략: 해당 ## 블록을 통째로 제거
  - 표 전체 누락:   표 대신 `> N/A — {reason}` 한 줄 작성
  - 필드 단일 누락: `{VAR}` → `N/A` 로 채움
  선택(OPTIONAL) 섹션은 <!-- OPTIONAL --> 주석으로 표시.
  있으면 넣고, 없으면 통째로 제거.

  SOURCE 표기:
  <!-- SOURCE: auto -->  — CSS 파싱으로 추출
  <!-- SOURCE: manual --> — 사람이 직접 관찰·작성
  <!-- SOURCE: auto+manual --> — 자동 추출 후 사람이 보완

  Template ↔ Report 매핑:
  §01 Quick Start    → report hero
  §02 Provenance     → report §01
  §03 Tech Stack     → report §02
  §04 Font+Type      → report §03 (merged)
  §05 Colors         → report §04
  §06 Spacing        → report §05
  §07 Radius         → report §06
  §08 Shadows        → report §07
  §09 Motion         → report §08 (if data exists)
  §10 Layout         → report §09 (if data exists)
  §11 Components     → report §10
  §12 Content Voice  → report §11 (if data exists)
  §13 Drop-in CSS    → report sidebar
  §14 Tailwind       → report sidebar
  §15 DO / DON'T     → report §12
-->

# DESIGN.md — {SERVICE_NAME} (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->
<!--
  {SINGLE_BIGGEST_MISTAKE} 선정 기준:
  실제 CSS와 가장 다른 것 중 "이거 하나 고치면 70% 달라 보이는 것".
  예: Stripe → "body weight 300 (400 아님)"
      Linear → "violet 악센트는 primary에만. 전체에 쓰지 마라"
      Notion  → "배경은 순백이 아니라 warm #F7F7F5"
-->

> 5분 안에 {SERVICE_NAME}처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "{PRIMARY_FONT}", "{FALLBACK_1}", -apple-system, sans-serif;
  font-weight: {WEIGHT_NORMAL};
}

/* 2. 배경 + 텍스트 */
:root { --bg: {PAGE_BG_HEX}; --fg: {TEXT_HEX}; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: {BRAND_HEX}; }
```

**절대 하지 말아야 할 것 하나**: {SINGLE_BIGGEST_MISTAKE}

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `{SITE_URL}` |
| Fetched | {FETCHED_AT} |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | {HTML_SIZE} bytes ({FRAMEWORK} SSR) |
| CSS files | {CSS_FILE_COUNT}개 외부 + {INLINE_COUNT} 인라인, 총 {CSS_TOTAL_CHARS}자 |
| Token prefix | `{TOKEN_PREFIX}` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: {FRAMEWORK} ({BUILD_DESCRIPTOR})
- **Design system**: {DS_NAME} — prefix `{TOKEN_PREFIX}`
- **CSS architecture**: {CSS_ARCHITECTURE}
  ```
  {TIER_CORE}   (--{PREFIX}-core-*)      raw hex 값
  {TIER_UTIL}   (--{PREFIX}-util-*)      semantic alias, core 참조
  {TIER_COMP}   (--{PREFIX}-{comp}-*)    컴포넌트별 조합
  ```
- **Class naming**: {CLASS_NAMING_PATTERN}
- **Default theme**: {DEFAULT_THEME} (bg = `{DEFAULT_BG_HEX}`)
- **Font loading**: {FONT_LOADING_METHOD}
- **Canonical anchor**: {CANONICAL_ANCHOR_DESC}

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `{PRIMARY_FONT}` ({FONT_LICENSE})
- **Code font**: `{CODE_FONT}` ({CODE_FONT_LICENSE})
- **Weight normal / bold**: `{WEIGHT_NORMAL}` / `{WEIGHT_BOLD}`

```css
:root {
  --{PREFIX}-font-family:       {FONT_FAMILY_CSS_VALUE};
  --{PREFIX}-font-family-code:  {CODE_FONT_CSS_VALUE};
  --{PREFIX}-font-weight-normal: {WEIGHT_NORMAL};
  --{PREFIX}-font-weight-bold:   {WEIGHT_BOLD};
}
body {
  font-family: var(--{PREFIX}-font-family);
  font-weight: var(--{PREFIX}-font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
{TYPOGRAPHY_ROWS}

> ⚠️ {TYPOGRAPHY_KEY_INSIGHT}

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp ({BRAND_RAMP_COUNT} steps)
<!-- {TOKEN_PREFIX}-color-core-{BRAND_FAMILY}-* -->

| Token | Hex |
|---|---|
{BRAND_RAMP_ROWS}

### 06-2. Brand Dark Variant
<!-- OPTIONAL: omit if service uses single-theme ramp -->
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
{BRAND_DARK_ROWS}

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light (`{NEUTRAL_NAME}`) | Dark (`{NEUTRAL_DARK_NAME}`) |
|---|---|---|
{NEUTRAL_PAIR_ROWS}

### 06-4. Accent Families
<!-- OPTIONAL: omit if no accent palette exists -->
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
{ACCENT_ROWS}

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
{SEMANTIC_ROWS}

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->
<!--
  이 tier가 컴포넌트 레벨 API.
  core 토큰보다 alias를 우선 사용.
  {TOKEN_PREFIX}-color-util-* → {TOKEN_PREFIX}-color-core-* → hex
-->

| Alias | Resolves to | Usage |
|---|---|---|
{ALIAS_ROWS}

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->
<!--
  §06-1~06-6 = design time (설계된 토큰 시스템)
  §06-7      = runtime measurement (실제 페이지에 얼마나 쓰이는지)
  중복 있음은 정상 — 역할이 다름.
  자동 추출 전용: CSS 전체 hex 빈도 카운트로 생성, 수동 작성 불가.
-->

| Rank | Hex | Count | Role |
|---|---|---|---|
{DOMINANT_ROWS}

---

## 07. Spacing
<!-- SOURCE: auto -->
<!--
  네이밍 규칙: {SPACING_NAMING_RULE}
  예) stripe: core-200 = 16px = 200 ÷ 12.5
-->

| Token | Value | Use case |
|---|---|---|
{SPACING_ROWS}

**주요 alias**:
- `{SPACE_ALIAS_1}` → {SPACE_ALIAS_1_VALUE} ({SPACE_ALIAS_1_USE})

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
{RADIUS_ROWS}

---

## 09. Shadows
<!-- SOURCE: auto -->
<!--
  패턴: {SHADOW_PATTERN}
  예) stripe: 모든 elevation이 dual-shadow 원자 (top + bottom 레이어)
-->

| Level | Value | Usage |
|---|---|---|
{SHADOW_ROWS}

---

## 10. Motion
<!-- OPTIONAL: omit if no motion tokens found in CSS -->
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
{MOTION_ROWS}

---

## 11. Layout Patterns
<!-- OPTIONAL: omit if insufficient data -->
<!-- SOURCE: manual -->

### Hero
- Layout: {HERO_LAYOUT}
- Background: {HERO_BG}
- H1: `{H1_SIZE}` / weight `{H1_WEIGHT}` / tracking `{H1_TRACKING}`
- Max-width: {HERO_MAX_WIDTH}

### Section Rhythm
```css
section {
  padding: {SECTION_PADDING_V} {SECTION_PADDING_H};
  max-width: {SECTION_MAX_WIDTH};
}
```

### Breakpoints
<!-- OPTIONAL -->

| Breakpoint | Value | Changes |
|---|---|---|
{BREAKPOINT_ROWS}

---

## 12. Components
<!-- SOURCE: auto+manual -->
<!--
  {COMPONENTS_BLOCK} = 아래 패턴을 서비스별로 반복한 마크다운 블록을 주입.
  자동 생성 또는 수동 작성 후 단일 블록으로 삽입.
  각 컴포넌트: BEM 클래스 + HTML 마크업 + spec 표
-->

{COMPONENTS_BLOCK}

---

## 13. Content / Copy Voice
<!-- OPTIONAL: omit if insufficient data -->
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | {HEADLINE_RULE} | "{HEADLINE_EXAMPLE}" |
| Primary CTA | {CTA_RULE} | "{CTA_EXAMPLE}" |
| Secondary CTA | {SECONDARY_CTA_RULE} | "{SECONDARY_CTA_EXAMPLE}" |
| Subheading | {SUBHEADING_RULE} | |
| Tone | {TONE_DESC} | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->
<!--
  핵심 토큰 5개만 (brand: 25/300/500/600anchor/900).
  전체 ramp는 §06 참조.
-->

```css
/* {SERVICE_NAME} — copy into your root stylesheet */
:root {
  /* Fonts */
  --{PREFIX}-font-family:       {FONT_FAMILY_CSS_VALUE};
  --{PREFIX}-font-family-code:  {CODE_FONT_CSS_VALUE};
  --{PREFIX}-font-weight-normal: {WEIGHT_NORMAL};
  --{PREFIX}-font-weight-bold:   {WEIGHT_BOLD};

  /* Brand (anchor + 4 steps) */
  --{PREFIX}-color-brand-25:  {BRAND_25};
  --{PREFIX}-color-brand-300: {BRAND_300};
  --{PREFIX}-color-brand-500: {BRAND_500};
  --{PREFIX}-color-brand-600: {BRAND_600};   /* ← canonical */
  --{PREFIX}-color-brand-900: {BRAND_900};

  /* Surfaces */
  --{PREFIX}-bg-page:   {PAGE_BG_HEX};
  --{PREFIX}-bg-dark:   {DARK_BG_HEX};
  --{PREFIX}-text:      {TEXT_HEX};
  --{PREFIX}-text-muted:{TEXT_MUTED_HEX};

  /* Key spacing */
  --{PREFIX}-space-sm:  {SPACE_SM};
  --{PREFIX}-space-md:  {SPACE_MD};
  --{PREFIX}-space-lg:  {SPACE_LG};

  /* Radius */
  --{PREFIX}-radius-sm: {RADIUS_SM};
  --{PREFIX}-radius-md: {RADIUS_MD};
}
```

---

## 15. Tailwind Config
<!-- OPTIONAL: omit if service doesn't use Tailwind or config not derivable -->
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — {SERVICE_NAME}
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '{BRAND_25}',
          300: '{BRAND_300}',
          500: '{BRAND_500}',
          600: '{BRAND_600}',
          900: '{BRAND_900}',
        },
        neutral: {
{TAILWIND_NEUTRAL_TOKENS}
        },
      },
      fontFamily: {
        sans: ['{PRIMARY_FONT}', '{FALLBACK_1}', 'system-ui'],
        mono: ['{CODE_FONT}', 'ui-monospace'],
      },
      fontWeight: {
        normal: '{WEIGHT_NORMAL}',
        bold:   '{WEIGHT_BOLD}',
      },
      borderRadius: {
{TAILWIND_RADIUS_TOKENS}
      },
      boxShadow: {
{TAILWIND_SHADOW_TOKENS}
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->
<!--
  실제 CSS에서 검증된 규칙만 작성.
  이 서비스 디자인을 구현할 때 흔히 틀리는 것들.
-->

### ✅ DO
{DO_ITEMS}

### ❌ DON'T
{DONT_ITEMS}
