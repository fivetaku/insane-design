---
schema_version: 3.1
slug: medium
service_name: Medium
site_url: https://medium.com
fetched_at: 2026-04-23
default_theme: light
brand_color: "#1A8917"
primary_font: Sohne
font_weight_normal: 400
token_prefix: "N/A (hashed utility classes; first-party custom properties 없음)"

bold_direction: "Human Editorial"
aesthetic_category: "Editorial Magazine"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Medium (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

현재 접근 가능한 Medium의 live CSS는 예전의 "노랑 영웅 섹션" 인상이 아니라, **따뜻한 크림 landing hero + 검정 pill + 초록 CTA**의 훨씬 절제된 조합으로 잡힌다. 홈(`/`)의 상단 hero는 `#F7F4ED` 배경 위에 놓이고, 핵심 텍스트는 `#242424` / `#000000`으로 처리된다. 이 조합이 주는 인상은 "신문처럼 무겁지 않은 에디토리얼, 하지만 충분히 인간적인 warmth가 있는 플랫폼"이다.

색상 전략은 면적과 역할이 명확하게 분리된다. 넓은 면은 `#F7F4ED`와 `#FFFFFF`가 맡고, 구조선은 `#242424`, 보조 텍스트는 `#6B6B6B`가 담당한다. 강조는 두 종류뿐이다. 내비게이션의 `Get started` pill은 `rgba(25, 25, 25, 1)` 검정 계열이고, hero의 `Start reading`은 `#1A8917` 초록이다. hover는 각각 `#000000`과 `#156D12`로 한 단계만 더 진해진다. 이 얇은 변화가 Medium 특유의 조용한 상호작용 톤을 만든다.

타이포그래피는 **한 번의 큰 대비**로 정체성을 만든다. UI 전체는 `sohne, "Helvetica Neue", Helvetica, Arial, sans-serif`가 지배하고, 홈 hero만 `gt-super, Georgia, Cambria, "Times New Roman", Times, serif`로 전환된다. 즉, Medium은 모든 레벨에서 폰트를 바꾸지 않는다. 대부분은 Sohne로 유지하고, 단 하나의 거대한 hero headline만 GT Super로 들어간다. 이 한 번의 serif 전환이 "사람이 쓴 이야기"라는 무드를 만든다.

레이아웃 역시 이 톤을 그대로 따른다. 상단 rail은 `75px` 높이로 고정되고, hero는 desktop에서 `460x600` 브랜드 이미지를 오른쪽에 두는 2열 구성이다. headline column은 `max-width: 720px`, horizontal shell은 desktop 기준 `64px`, hero 내부 vertical rhythm은 `48px` 단위가 반복된다. 카드와 리스트는 둥근 panel 대신 **평평한 면 + 1px 경계선**으로 처리된다.

중요한 점은, 이번 수집에서 요청받은 legacy dark/yellow references는 현재 접근 가능한 live CSS(`/`, `/about?autoplay=1`, `/tag/technology`, sign-in flows)에서 재확인되지 않았다는 것이다. 따라서 이 문서의 canonical token 세트는 실제로 확인된 값만 사용한다.

### Key Characteristics

- warm landing hero `#F7F4ED` + white secondary surfaces `#FFFFFF`
- UI 전체를 Sohne로 통일하고, hero headline만 GT Super로 분기
- CTA는 두 축만 사용: green `#1A8917`와 near-black `rgba(25, 25, 25, 1)`
- 본문/구조선은 `#242424`, 보조 정보는 `#6B6B6B`
- pill radius `99em`, 그림자보다 border와 배경 대비로 깊이 표현
- interaction은 `300ms linear` 수준의 조용한 배경색 전환
- first-party custom property 레이어 없음, hashed utility class 중심

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Human Editorial
> **Aesthetic Category**: Editorial Magazine
> **Signature Element**: 이 사이트는 **GT Super hero와 Sohne UI가 만드는 거대한 타이포 대비**로 기억된다.
> **Code Complexity**: medium — semantic token layer는 없지만, runtime-injected hashed utility classes와 여러 route별 스타일셋을 함께 읽어야 한다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Medium처럼 만들기 — 3가지만 하면 80%

```css
/* 1. UI 폰트 */
body {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  color: #242424;
}

/* 2. landing hero 배경 */
.hero {
  background: #F7F4ED;
  border-bottom: 1px solid #242424;
}

/* 3. CTA 축 */
.btn-primary {
  background: #1A8917;
  border: 1px solid #1A8917;
  color: #FFFFFF;
  border-radius: 99em;
}
```

**절대 하지 말아야 할 것 하나**: headline까지 전부 sans-serif로 처리하지 마라. 현재 Medium의 첫인상은 `gt-super` hero headline 하나가 만든다. 이 serif 전환이 빠지면 Medium이 아니라 그냥 깔끔한 블로그 landing이 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://medium.com` |
| Audited routes | `/`, `/about?autoplay=1`, `/tag/technology`, sign-in flows |
| Fetched | 2026-04-23 |
| Extractor | Playwright Chromium (stealth init) + direct CSS download |
| HTML size | `50,095` bytes |
| CSS files | first-party `1`개 외부 (`unbound.css`, `19,440` bytes) + inline `15`개 (`15,603` chars) |
| Third-party CSS | reCAPTCHA + GSI (`84,062` bytes, token extraction 제외) |
| Token prefix | `N/A (hashed utility classes; first-party custom properties 없음)` |
| Method | live DOM 렌더 + CSSOM 추출 + `https://glyph.medium.com/css/unbound.css` 직접 다운로드 |

> 팩트 기준: first-party external CSS는 `unbound.css` 1개, first-party custom property는 확인되지 않았다. inline runtime CSS에 `--reach-menu-button`, `--reach-tabs` 2개만 존재한다.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered shell 위에 hydration 되는 React SPA
- **Design system**: 공개된 token system 없음 — route별 runtime-injected utility class sheet
- **CSS architecture**: hashed utility classes + external font-face sheet
  ```
  external  glyph.medium.com/css/unbound.css   font-face only
  inline    <style> x15                        utility class + route layout
  runtime   --reach-menu-button / --reach-tabs library 변수 2개
  ```
- **Class naming**: `.cl`, `.cm`, `.dx`, `.ao`, `.ep:hover` 식의 1~2자 축약 class
- **Default theme**: light
  `hero = #F7F4ED`, `secondary surface = #FFFFFF`, `text = #242424`
- **Font loading**: `glyph.medium.com`에서 `sohne`, `gt-super`, `charter`, `source-code-pro`, `source-serif-pro`, `fell`, `noe`, `opendyslexic` 선언
- **Canonical anchor**: green hero CTA `#1A8917` + near-black pill `rgba(25, 25, 25, 1)` + GT Super headline

Medium의 핵심은 "토큰이 잘 정리된 DS"가 아니라 **hydrated page가 직접 스타일을 조립하는 구조**에 있다. 즉, class 이름만 보고 의미를 유추하기 어렵고, DOM 위치와 computed style을 같이 봐야 한다. 이는 구현 복잡도가 아주 높지는 않지만, 단순한 CSS 변수 복제만으로는 충분하지 않다는 뜻이다.

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Primary UI**: `"sohne", "Helvetica Neue", Helvetica, Arial, sans-serif`
- **Display / hero**: `"gt-super", Georgia, Cambria, "Times New Roman", Times, serif`
- **Reading serif pool (declared)**: `charter`, `fell`, `source-serif-pro`, `noe`
- **Code**: `source-code-pro`
- **A11y / alternate**: `opendyslexic`
- **Weight normal / bold**: `400` / `700`

```css
/* 실제 first-party font-face 이름 */
body {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

.hero-title {
  font-family: "gt-super", Georgia, Cambria, "Times New Roman", Times, serif;
  font-weight: 400;
}

code,
pre {
  font-family: "source-code-pro", monospace;
}
```

### Loaded vs Declared

- **Loaded on homepage** — `sohne 400 normal`, `gt-super 400 normal`
- **Declared but unloaded on homepage** — `charter 400/700`, `source-serif-pro 400/700`, `fell 400`, `noe 500`, `source-code-pro 400/700`, `opendyslexic 400`

> 핵심 인사이트: Medium은 "여러 글꼴을 다 쓰는 시스템"이 아니라, 필요한 route에서 쓸 수 있도록 font pool을 넓게 선언하고, 현재 route는 극도로 제한된 폰트만 로드하는 구조다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-display / 375w` | `80px` | `400` | `72px` | `-4.4px` |
| `hero-display / 768w` | `106px` | `400` | `95px` | `-5.83px` |
| `hero-display / 1440w` | `120px` | `400` | `100px` | `-6.6px` |
| `hero-subtitle` | `22px` | `400` | `28px` | `normal` |
| `topic-title` | `42px` | `500` | `52px` | `-0.462px` |
| `feed-card-title` | `20px` | `700` | `24px` | `normal` |
| `nav-link` | `14px` | `400` | `20px` | `normal` |
| `meta` | `13px` | `400` | `20px` | `normal` |
| `hero-cta` | `20px` | `400` | `28px` | `normal` |
| `nav-pill` | `14px` | `400` | `20px` | `normal` |

> Medium의 live CSS는 거의 전부 Sohne의 좁은 스케일 위에 놓이고, 단 하나의 GT Super hero만 과감하게 크게 튄다. 즉 "전 레벨 serif"가 아니라 **one-shot display contrast**가 핵심이다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Confirmed Brand / CTA

| Token | Value | Evidence |
|---|---|---|
| `hero-cta-bg` | `#1A8917` | `.em { background: #1A8917 }` |
| `hero-cta-border` | `#1A8917` | `.eo { border-color: #1A8917 }` |
| `hero-cta-hover` | `#156D12` | `.ep:hover { background: #156D12 }` |
| `hero-cta-text` | `#FFFFFF` | `.ej { color: #FFFFFF }` |

### 06-2. Confirmed Neutral / Warm Surfaces

| Token | Value | Usage |
|---|---|---|
| `hero-bg` | `#F7F4ED` | landing hero `.ao`, `.at` |
| `surface` | `#FFFFFF` | about page surface, pill text, neutral panels |
| `surface-muted` | `#F2F2F2` | about / error route muted area |
| `ink` | `#242424` | base text, border-bottom, card titles |
| `text-muted` | `#6B6B6B` | secondary info, disabled text |
| `ink-pure` | `#000000` | hero display text, black-pill hover |
| `pill-bg` | `rgba(25, 25, 25, 1)` | nav `Get started` |

### 06-3. Semantic Roles

| Role | Value | Notes |
|---|---|---|
| `bg/hero` | `#F7F4ED` | first screen tone |
| `bg/default` | `#FFFFFF` | secondary pages / content |
| `text/primary` | `#242424` | 대부분의 UI 텍스트 |
| `text/secondary` | `#6B6B6B` | 부가 정보 |
| `action/primary` | `#1A8917` | hero CTA |
| `action/hover` | `#156D12` | hero CTA hover |
| `action/secondary` | `rgba(25, 25, 25, 1)` | nav pill |
| `action/secondary-hover` | `#000000` | nav pill hover |

> 검증 메모: 요청받은 legacy dark / yellow references는 현재 접근 가능한 live CSS에서 재확인되지 않았다. 그래서 canonical palette는 위 표의 확인값만 사용한다.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Evidence / Usage |
|---|---|---|
| `shell-x-mobile` | `24px` | `.bc { margin: 0 24px }` |
| `shell-x-tablet` | `48px` | `.be { margin: 0 48px }` |
| `shell-x-desktop` | `64px` | `.bg { margin: 0 64px }` |
| `nav-padding-y` | `25px` | `.bj { padding: 25px 0 }` |
| `rail-height` | `75px` | `.bk { height: 75px }` |
| `hero-gap-mobile` | `32px` | `.dq { margin-bottom: 32px }` |
| `hero-gap-desktop` | `48px` | `.du`, `.ec { margin-bottom: 48px }` |
| `nav-pill-x` | `16px` | `.cr { padding: 8px 16px }` |
| `hero-pill-x` | `20px` | `.ek { padding: 8px 20px }` |
| `hero-min-height` | `560px` | `.ap { min-height: 560px }` |

Medium의 공간감은 카드 padding보다 **outer shell 리듬**이 더 중요하다. 좌우 여백이 `24 → 48 → 64`로 커지고, hero 내부 문단/CTA/이미지 간 간격은 `32`와 `48`이 반복된다. 이 때문에 레이아웃이 넓어도 산만하지 않고, 읽기 전에 이미 "조용하다"는 인상을 준다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `pill` | `99em` | nav / hero CTA `.dc` |
| `circle` | `50%` | loading spinner `.l` |

> N/A — 접근 가능한 first-party route에서는 카드/패널용 별도 radius token이 관찰되지 않았다. 현재 Medium은 panel softness보다 flat surface를 우선한다.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `surface-shadow` | `none` | first-party `box-shadow` 미관측 |

Medium의 accessible first-party CSS는 그림자를 거의 쓰지 않는다. depth는 border와 배경 명도 차이로 만든다.

---

## 10. Motion
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `button-bg` | `background-color 300ms linear` | `.ba`, `.bb button` |
| `button-fg` | `color 300ms linear` | `.bb button` |
| `black-pill-hover` | `#000000` | `.cv:hover` |
| `green-pill-hover` | `#156D12` | `.ep:hover`, `.eq:hover` |
| `spinner` | `k1 2s infinite linear` | loading indicator `.p` |

모션은 거의 전부 버튼 hover에만 모인다. translate, blur, spring 같은 효과는 없고, **배경색이 천천히 진해지는 것**만으로 반응성을 준다.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

- **Landing hero** — warm hero `#F7F4ED`, fixed top rail `75px`, 오른쪽 `460x600` brand image, 왼쪽 `max-width: 720px` display headline
- **Top rail** — 1px `#242424` border-bottom + 작은 Sohne link set + 검정 pill `Get started`
- **Topic page** — `42px / 52px` topic headline + 단일 column feed + `20px / 24px` card title
- **Secondary pages** — `/about`는 white surface 비율이 더 높고, 같은 Sohne scale을 유지
- **Visual depth** — 그림자 대신 면의 색 차이와 구조선으로 분리

현재 Medium은 강한 masonry나 복잡한 card grid보다, **headline / subtitle / pill / image** 네 가지 재료를 route마다 조금씩 재배치하는 방식에 가깝다.

---

## 12. Responsive Behavior
<!-- SOURCE: auto -->

### Observed Hero Scaling

| Viewport | Hero size | Line-height | Notes |
|---|---|---|---|
| `375px` | `80px` | `72px` | hero 문구가 가장 먼저 화면을 점유 |
| `768px` | `106px` | `95px` | headline이 2단 사이즈로 확장 |
| `1440px` | `120px` | `100px` | 이미지와 headline이 2열 균형 완성 |

### Responsive Summary

- mobile에서는 nav link 일부가 줄고, hero 메시지가 화면 대부분을 차지한다
- tablet부터 topic/title 폭이 크게 열리며 `42px` headline이 안정적으로 유지된다
- desktop은 `64px` shell과 `720px` headline column이 핵심 구조가 된다

> breakpoint 숫자 자체는 minified CSS에서 semantic하게 노출되지 않았고, 위 표는 실제 viewport 관찰값이다.

---

## 13. Components
<!-- SOURCE: auto -->

### 13-1. Nav Secondary Pill

```css
.btn-nav {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 20px;
  font-weight: 400;
  color: rgba(255, 255, 255, 1);
  background: rgba(25, 25, 25, 1);
  border: 1px solid rgba(25, 25, 25, 1);
  border-radius: 99em;
  padding: 8px 16px;
}
.btn-nav:hover {
  background: #000000;
  border-color: #242424;
}
```

### 13-2. Hero Primary CTA

```css
.btn-hero {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 28px;
  font-weight: 400;
  color: #FFFFFF;
  background: #1A8917;
  border: 1px solid #1A8917;
  border-radius: 99em;
  padding: 8px 20px;
}
.btn-hero:hover {
  background: #156D12;
  border-color: #156D12;
}
```

### 13-3. Topic Feed Card Title

```css
.feed-card__title {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 24px;
  font-weight: 700;
  color: #242424;
}

.feed-card__meta {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 20px;
  font-weight: 400;
  color: #6B6B6B;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

- **Voice** — 직접적이고 짧다. 설명은 차분하지만 감정 과장은 없다.
- **Headline pattern** — `Human stories & ideas`처럼 추상 명사 2~3개로 플랫폼 정체성을 압축한다.
- **Subcopy** — `A place to read, write, and deepen your understanding`처럼 동사 3개를 나열해 효용을 설명한다.
- **CTA** — `Get started`, `Start reading`, `Sign in`처럼 한 문장 대신 한 동사에 가깝다.

Medium의 카피는 "브랜드가 말하는 문장"보다 **행동을 제안하는 짧은 인터페이스 언어**에 가깝다. 레이아웃이 크고 조용하기 때문에 문장도 그만큼 더 짧아진다.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --medium-brand: #1A8917;
  --medium-brand-hover: #156D12;
  --medium-surface-warm: #F7F4ED;
  --medium-surface: #FFFFFF;
  --medium-surface-muted: #F2F2F2;
  --medium-ink: #242424;
  --medium-ink-strong: rgba(25, 25, 25, 1);
  --medium-ink-pure: #000000;
  --medium-text-muted: #6B6B6B;
  --medium-pill-radius: 99em;
}

body {
  font-family: "sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  color: var(--medium-ink);
  background: var(--medium-surface);
}

.medium-hero {
  background: var(--medium-surface-warm);
  border-bottom: 1px solid var(--medium-ink);
  min-height: 560px;
}

.medium-hero__title {
  font-family: "gt-super", Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: clamp(80px, 8vw, 120px);
  line-height: clamp(72px, 7vw, 100px);
  letter-spacing: -0.055em;
  color: var(--medium-ink-pure);
  max-width: 720px;
}

.medium-btn {
  display: inline-block;
  border-radius: var(--medium-pill-radius);
  border: 1px solid transparent;
  text-decoration: none;
  text-align: center;
  transition: background-color 300ms linear, color 300ms linear;
}

.medium-btn--primary {
  padding: 8px 20px;
  background: var(--medium-brand);
  border-color: var(--medium-brand);
  color: #FFFFFF;
}

.medium-btn--primary:hover {
  background: var(--medium-brand-hover);
  border-color: var(--medium-brand-hover);
}

.medium-btn--secondary {
  padding: 8px 16px;
  background: var(--medium-ink-strong);
  border-color: var(--medium-ink-strong);
  color: rgba(255, 255, 255, 1);
}

.medium-btn--secondary:hover {
  background: var(--medium-ink-pure);
  border-color: var(--medium-ink);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        medium: {
          brand: "#1A8917",
          brandHover: "#156D12",
          warm: "#F7F4ED",
          surface: "#FFFFFF",
          surfaceMuted: "#F2F2F2",
          ink: "#242424",
          inkPure: "#000000",
          muted: "#6B6B6B",
        },
      },
      fontFamily: {
        sans: ['"sohne"', '"Helvetica Neue"', "Helvetica", "Arial", "sans-serif"],
        display: ['"gt-super"', "Georgia", "Cambria", '"Times New Roman"', "Times", "serif"],
        mono: ['"source-code-pro"', "monospace"],
      },
      borderRadius: {
        mediumPill: "99em",
      },
      minHeight: {
        mediumHero: "560px",
      },
      maxWidth: {
        mediumHero: "720px",
      },
      transitionDuration: {
        medium: "300ms",
      },
      transitionTimingFunction: {
        medium: "linear",
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Prompt 1 — Landing Hero Recreation

> Create a quiet editorial landing page with a warm cream hero (`#F7F4ED`), a single oversized GT Super display headline, Sohne for all supporting UI, one green primary CTA (`#1A8917`), and one near-black secondary pill. Keep the structure flat, border-led, and human rather than corporate.

### Prompt 2 — Component Guardrails

> Use pill buttons with `99em` radius, 1px borders, and 300ms linear background transitions. Do not introduce gradients, glow, drop shadows, or a visible token-dashboard aesthetic. Treat green as CTA-only, not as a full-page wash.

### Prompt 3 — Tone Guardrails

> Copy should sound like an invitation to read and think, not like aggressive SaaS conversion copy. Prefer short noun-led headlines, short supporting sentences, and one- or two-word CTAs.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- use `gt-super` only for the one oversized hero statement
- keep UI text in Sohne with compact `14px / 20px` and `13px / 20px` scales
- reserve `#1A8917` for primary CTA moments
- use `#F7F4ED` for the first-screen warmth and `#FFFFFF` for follow-up surfaces
- rely on border and tone change instead of shadow for separation

### DON'T

- turn the whole site green
- replace the hero serif with a generic sans display
- add glassmorphism, blur, or oversized shadow cards
- invent a custom-property palette that the current live CSS does not expose
- assume older dark/yellow references are still canonical without current CSS evidence
