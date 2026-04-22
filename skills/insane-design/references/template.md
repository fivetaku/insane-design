---
schema_version: 3.1                           # 🆕 v3.1 — medium 분기 + apply/build 계약 필드
slug: {SLUG}
service_name: {SERVICE_NAME}
site_url: {SITE_URL}
fetched_at: {FETCHED_AT}
default_theme: {light|dark|mixed}
brand_color: {BRAND_HEX}
primary_font: {PRIMARY_FONT}
font_weight_normal: {WEIGHT_NORMAL}
token_prefix: {TOKEN_PREFIX}

# apply Lv3 BOLD 리디자인 지원 필드 (v3.0에서 추가, v3.1에서 유지)
bold_direction: {BOLD_DIRECTION}              # 1~2 단어 (예: "Industrial Minimalism")
aesthetic_category: {AESTHETIC_CATEGORY}      # redesign-aesthetics.md §3 12가지 중 1개
signature_element: {SIGNATURE_ELEMENT}        # hero_impact / typo_contrast / section_transition / minimal_extreme
code_complexity: {CODE_COMPLEXITY}            # low / medium / high / very_high

# 🆕 v3.1 — 매체 분기 (build 스킬이 starter-components 로드 시 사용)
medium: {MEDIUM}                              # web | slide | design-system | card-news | motion | print
medium_confidence: {MEDIUM_CONFIDENCE}        # high | medium | low
---

<!--
  DesignMD Analyzer — design.md 템플릿
  버전: 3.1 (2026-04-19)

  v3.1 변경: frontmatter 최상단 `schema_version: 3.1` 추가,
             `medium` + `medium_confidence` 필드 추가 (build 스킬 매체 분기용).

  섹션 번호: 00~18 (통일)
  Visual Theme = 00, Quick Start = 01, Provenance = 02, Tech Stack = 03 ...

  N/A 처리 규칙:
  - 섹션 전체 생략: 해당 ## 블록을 통째로 제거
  - 표 전체 누락:   표 대신 `> N/A — {reason}` 한 줄 작성
  - 필드 단일 누락: `{VAR}` → `N/A` 로 채움

  SOURCE 표기:
  <!-- SOURCE: auto -->  — CSS 파싱으로 추출
  <!-- SOURCE: manual --> — 사람이 직접 관찰·작성
  <!-- SOURCE: auto+manual --> — 자동 추출 후 사람이 보완

  Template ↔ Report 매핑:
  §00 Visual Theme     → report mood section
  §01 Quick Start      → report hero
  §02 Provenance       → report §01
  §03 Tech Stack       → report §02
  §04 Font Stack       → report §03 (merged)
  §05 Typography Scale → report §03
  §06 Colors           → report §04
  §07 Spacing          → report §05
  §08 Radius           → report §06
  §09 Shadows          → report §07
  §10 Motion           → report §08 (if data exists)
  §11 Layout Patterns  → report §09
  §12 Responsive       → report §09-resp
  §13 Components       → report §10
  §14 Content Voice    → report §11 (if data exists)
  §15 Drop-in CSS      → report sidebar
  §16 Tailwind         → report sidebar
  §17 Agent Prompt     → report §agent
  §18 DO / DON'T       → report §12
-->

# DESIGN.md — {SERVICE_NAME} (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->
<!--
  스크린샷 + 추출된 토큰(색상, 폰트, 여백)을 종합해 AI가 서술형으로 작성.
  3~5문단으로 브랜드의 시각적 정체성·핵심 특징·분위기를 설명.
  구현자가 코드를 작성하기 전에 "이 서비스는 이런 느낌이다"를 잡게 해주는 섹션.
-->

{VISUAL_THEME_DESCRIPTION}

<!--
  작성 가이드:
  - 1문단: 전반적 분위기와 디자인 철학 (예: "차갑고 기술적이면서도 친근한 fintech 톤")
  - 2문단: 색상 사용 전략 (브랜드 컬러 역할, 배경/전경 대비, 뉴트럴 활용)
  - 3문단: 타이포그래피 성격 (폰트 선택 이유, weight 활용, 계층 표현)
  - 4문단: 여백/공간 활용과 레이아웃 철학 (밀도 vs 여유, 리듬감)
  - 5문단 (선택): 인터랙션/모션 성격 (정적 vs 다이내믹, 전환 속도)
-->

### 🆕 BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: {BOLD_DIRECTION}
> **Aesthetic Category**: {AESTHETIC_CATEGORY}
> **Signature Element**: 이 사이트는 **{SIGNATURE_DESCRIPTION}**으로 기억된다.
> **Code Complexity**: {CODE_COMPLEXITY} — {COMPLEXITY_REASON}

<!--
  이 4줄 블록은 apply 스킬이 정규식으로 파싱하여 Lv3 BOLD 리디자인 시 사용함.
  반드시 위 형식 그대로 작성. frontmatter 필드와 정확히 일치해야 함.

  - BOLD_DIRECTION: 1~2 단어 레이블 (Step 4 판정 #13)
  - AESTHETIC_CATEGORY: redesign-aesthetics.md §3의 12가지 중 1개
  - SIGNATURE_DESCRIPTION: hero 임팩트 / 타이포 대비 / 섹션 전환 / 미니멀 극단 등
  - CODE_COMPLEXITY: low / medium / high / very_high + 근거 한줄
-->

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
| Extractor | curl + Chrome UA (5-tier fallback) |
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
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: {CONTENT_MAX_WIDTH}
- **Grid type**: {GRID_TYPE}
- **Column count**: {GRID_COLUMNS}
- **Gutter**: {GRID_GUTTER}

### Hero
- **🆕 Pattern Summary**: {HERO_PATTERN_SUMMARY}
  <!-- 한줄 요약: "{height}vh + {bg 처리} + {H1 정렬} + {CTA 배치}"
       예: "100vh + 풀스크린 차량 사진 + 중앙 H1 + dual CTA 아래"
       예: "70vh + gradient flame bg + 좌측 H1 + 우측 제품 mockup" -->
- Layout: {HERO_LAYOUT}
- Background: {HERO_BG}
- **🆕 Background Treatment**: {HERO_BG_TREATMENT}
  <!-- atmospheric 효과 명시: solid / gradient mesh / noise texture / image overlay / video / dot pattern / grain
       예: "image-overlay (vehicle.jpg + linear-gradient(180deg, rgba(0,0,0,0.3), rgba(0,0,0,0.6)))"
       예: "gradient-mesh (radial 2-layer)"
       예: "solid #F5F5F7" — 단색이면 단색이라고 명시 -->
- H1: `{H1_SIZE}` / weight `{H1_WEIGHT}` / tracking `{H1_TRACKING}`
- Max-width: {HERO_MAX_WIDTH}

### Section Rhythm
```css
section {
  padding: {SECTION_PADDING_V} {SECTION_PADDING_H};
  max-width: {SECTION_MAX_WIDTH};
}
```

### Card Patterns
- **Card background**: {CARD_BG}
- **Card border**: {CARD_BORDER}
- **Card radius**: {CARD_RADIUS}
- **Card padding**: {CARD_PADDING}
- **Card shadow**: {CARD_SHADOW}

### Navigation Structure
- **Type**: {NAV_TYPE}
- **Position**: {NAV_POSITION}
- **Height**: {NAV_HEIGHT}
- **Background**: {NAV_BG}
- **Border**: {NAV_BORDER}

### Content Width
- **Prose max-width**: {PROSE_MAX_WIDTH}
- **Container max-width**: {CONTAINER_MAX_WIDTH}
- **Sidebar width**: {SIDEBAR_WIDTH}

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->
<!--
  자동 추출된 미디어 쿼리 + 수동 관찰 보완.
  모바일 퍼스트/데스크톱 퍼스트 여부도 명시.
-->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | {BP_MOBILE} | {BP_MOBILE_DESC} |
| Tablet | {BP_TABLET} | {BP_TABLET_DESC} |
| Desktop | {BP_DESKTOP} | {BP_DESKTOP_DESC} |
| Large | {BP_LARGE} | {BP_LARGE_DESC} |

### Touch Targets
- **Minimum tap size**: {TOUCH_MIN_SIZE}
- **Button height (mobile)**: {TOUCH_BUTTON_HEIGHT}
- **Input height (mobile)**: {TOUCH_INPUT_HEIGHT}

### Collapsing Strategy
- **Navigation**: {COLLAPSE_NAV}
- **Grid columns**: {COLLAPSE_GRID}
- **Sidebar**: {COLLAPSE_SIDEBAR}
- **Hero layout**: {COLLAPSE_HERO}

### Image Behavior
- **Strategy**: {IMAGE_STRATEGY}
- **Max-width**: {IMAGE_MAX_WIDTH}
- **Aspect ratio handling**: {IMAGE_ASPECT_RATIO}

---

## 13. Components
<!-- SOURCE: auto+manual -->
<!--
  {COMPONENTS_BLOCK} = 아래 패턴을 서비스별로 반복한 마크다운 블록을 주입.
  자동 생성 또는 수동 작성 후 단일 블록으로 삽입.
  각 컴포넌트: BEM 클래스 + HTML 마크업 + spec 표 + 상태별(hover/active) 값
-->

### Buttons
{BUTTONS_BLOCK}

### Badges
{BADGES_BLOCK}

### Cards & Containers
<!--
  카드/컨테이너 패턴: bg, border, radius, padding, shadow
  hover 상태: shadow 변화, border-color 변화, transform 등
-->
{CARDS_BLOCK}

### Navigation
<!--
  네비게이션 컴포넌트: 링크 스타일, active 상태, 모바일 메뉴
-->
{NAVIGATION_BLOCK}

### Inputs & Forms
<!--
  입력 필드: height, padding, border, focus 스타일, error 스타일
-->
{INPUTS_BLOCK}

### Hero Section
<!--
  히어로 영역: 배경, 텍스트 크기/weight, CTA 배치, 이미지/일러스트
-->
{HERO_SECTION_BLOCK}

---

## 14. Content / Copy Voice
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

## 15. Drop-in CSS
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

## 16. Tailwind Config
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

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->
<!--
  AI 에이전트(Claude, GPT 등)가 이 디자인 시스템으로 구현할 때 참조하는 섹션.
  design.md의 토큰을 실전 프롬프트에서 어떻게 활용하는지 빠른 레퍼런스 제공.
-->

### Quick Color Reference
<!--
  역할별로 hex 값을 한눈에 볼 수 있는 요약 테이블.
  §06의 전체 토큰 중 실전에서 가장 자주 쓰이는 것만 추출.
-->

| Role | Token | Hex |
|---|---|---|
| Brand primary | {AGENT_BRAND_TOKEN} | {AGENT_BRAND_HEX} |
| Background | {AGENT_BG_TOKEN} | {AGENT_BG_HEX} |
| Text primary | {AGENT_TEXT_TOKEN} | {AGENT_TEXT_HEX} |
| Text muted | {AGENT_MUTED_TOKEN} | {AGENT_MUTED_HEX} |
| Border | {AGENT_BORDER_TOKEN} | {AGENT_BORDER_HEX} |
| Success | {AGENT_SUCCESS_TOKEN} | {AGENT_SUCCESS_HEX} |
| Error | {AGENT_ERROR_TOKEN} | {AGENT_ERROR_HEX} |

### Example Component Prompts
<!--
  "이 프롬프트를 복사해서 AI에게 주면 이 서비스 스타일의 컴포넌트가 나온다."
-->

#### Hero Section
```
{SERVICE_NAME} 스타일 히어로 섹션을 만들어줘.
- 배경: {PAGE_BG_HEX}
- H1: {PRIMARY_FONT}, {H1_SIZE}, weight {H1_WEIGHT}, tracking {H1_TRACKING}
- 서브텍스트: {TEXT_MUTED_HEX}, 16px
- CTA 버튼: 배경 {BRAND_HEX}, 텍스트 white, radius {RADIUS_MD}, padding 12px 24px
- 최대 너비: {HERO_MAX_WIDTH}
```

#### Card Component
```
{SERVICE_NAME} 스타일 카드 컴포넌트를 만들어줘.
- 배경: {CARD_BG}, border: 1px solid {AGENT_BORDER_HEX}, radius: {CARD_RADIUS}
- padding: {CARD_PADDING}
- shadow: {CARD_SHADOW}
- hover 시: {CARD_HOVER_EFFECT}
- 제목: {PRIMARY_FONT}, 16px, weight {WEIGHT_BOLD}
- 본문: 14px, color {AGENT_TEXT_HEX}, line-height 1.6
```

#### Badge
```
{SERVICE_NAME} 스타일 배지를 만들어줘.
- font: {PRIMARY_FONT}, 12px, weight 500
- padding: 2px 8px, radius: 999px
- 기본: bg {AGENT_BG_HEX}, border 1px solid {AGENT_BORDER_HEX}
- 브랜드: bg {BRAND_HEX}20, color {BRAND_HEX}, border 없음
```

#### Navigation
```
{SERVICE_NAME} 스타일 상단 네비게이션을 만들어줘.
- 높이: {NAV_HEIGHT}, 배경: {NAV_BG}, 하단 border: 1px solid {AGENT_BORDER_HEX}
- 로고: 좌측, 14px, weight 600
- 링크: {PRIMARY_FONT}, 14px, weight 400, color {AGENT_MUTED_HEX}
- 활성 링크: color {AGENT_TEXT_HEX}, weight 500
- CTA 버튼: 우측, 브랜드 컬러
```

### Iteration Guide
<!--
  반복 작업·수정 요청 시 주의사항.
  "이거만 주의하면 일관성이 유지된다"는 실전 팁.
-->

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight {WEIGHT_NORMAL}이 기본. {WEIGHT_BOLD}는 제목/강조에만.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **다크 모드**: §06-2의 dark variant 토큰을 사용. light 토큰에 opacity 적용하지 말 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->
<!--
  실제 CSS에서 검증된 규칙만 작성.
  이 서비스 디자인을 구현할 때 흔히 틀리는 것들.
-->

### ✅ DO
{DO_ITEMS}

### ❌ DON'T
{DONT_ITEMS}
