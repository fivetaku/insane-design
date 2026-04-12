---
slug: github
service_name: GitHub
site_url: https://github.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#1f6feb"
primary_font: Mona Sans
font_weight_normal: 400
token_prefix: Primer
---

# DESIGN.md — GitHub (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 GitHub처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight — Mona Sans Variable + metric fallback */
body {
  font-family: "Mona Sans", "Mona Sans Fallback", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
h1, h2, h3 {
  font-family: "Mona Sans", "Mona Sans Header Fallback", -apple-system, sans-serif;
  font-weight: 800;  /* variable font supports 200, 450, 550, 800 */
}

/* 2. 배경 + 텍스트 — 다크 모드 Primer */
:root[data-color-mode="dark"] {
  --bgColor-default: #0d1117;
  --bgColor-inset:   #010409;
  --fgColor-default: #f0f6fc;
  --fgColor-muted:   #9198a1;
}
body { background: var(--bgColor-default); color: var(--fgColor-default); }

/* 3. 브랜드 — 다크 모드 accent */
:root { --accent: #1f6feb; }
```

**절대 하지 말아야 할 것 하나**: `#0969DA` (Primer v1 라이트 모드 accent)와 `#24292F`를 GitHub 브랜드 색으로 사용하지 말 것. GitHub.com의 현재 상태는 다크 테마가 기본이며, 다크 모드에서 accent는 `#1f6feb` (emphasis) / `#4493f8` (fg) / `#388bfd1a` (muted)의 **3단계 semantic scale**이다. 단일 hex로 "GitHub blue"를 표현하면 Primer의 핵심 컨셉을 놓친다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://github.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | Primer SSR + MVC + Rails ERB |
| CSS files | 21개 외부, 총 2,701,381자 |
| Custom props | 2,196 (color: 1,380 · spacing: 276 · shadow: 31) |
| Token prefix | `--bgColor-*`, `--fgColor-*`, `--borderColor-*`, `--base-size-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · Primer 공식 규약 기반 |

---

## 03. Tech Stack

- **Framework**: Rails + ERB + Web Components. Turbo/Hotwire + Stimulus.
- **Design system**: **Primer** — GitHub 공식 디자인 시스템. W3C Design Tokens 가장 근접.
- **CSS architecture**: 대규모 CSS 커스텀 프로퍼티 시스템 (2,196개) + 테마 스위치
  ```
  --{category}-{role}-{state}       base-size-4, bgColor-accent-emphasis
  --{component}-{property}-{state}  button-primary-bgColor-hover
  :root[data-color-mode="dark"]     다크 모드 스코프
  :root[data-color-mode="light"]    라이트 모드 스코프
  ```
- **Class naming**: Primer 유틸리티 (`Box`, `Label`, `Button`) + 자체 시맨틱 클래스 (`js-*`, `Header-*`, `repository-content`) 혼합
- **Default theme**: **Dark** (현재 크롤링된 페이지 기준). `data-color-mode="dark"` 플래그로 라이트/다크 스위치.
- **Font loading**: `Mona Sans` (variable 웹폰트) + `Mona Sans Fallback` / `Mona Sans Header Fallback` — metric-matched fallback으로 layout shift 방지
- **Canonical anchor**: `--bgColor-default: #0d1117` (dark) / `#ffffff` (light), `--fgColor-default: #f0f6fc` (dark)

---

## 04. Font Stack

- **Display font**: `Mona Sans` (variable, GitHub 2024 리브랜드 자체 폰트)
- **Display alternative**: `Hubot Sans` — 브랜드 페이지 전용
- **Body font**: `Mona Sans`
- **Code font**: `ui-monospace`, `SFMono-Regular`, `SF Mono`, `Menlo`, `Consolas`, `Liberation Mono`
- **Metric fallback**: `Mona Sans Fallback` (body) / `Mona Sans Header Fallback` (heading) — 두 가지 별도 운용
- **Weight range**: 200, 450, 550, 800, 900 (variable font non-standard weights + 400/500/600/700)

```css
:root {
  --brand-body-fontFamily:         "Mona Sans", "Mona Sans Fallback", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  --brand-heading-fontFamily:      "Mona Sans", "Mona Sans Header Fallback", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --brand-fontStack-monospace:     ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  --brand-fontStack-sansSerif:     "Mona Sans", "Mona Sans Fallback", -apple-system, sans-serif;
  --fontStack-monospace:           ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}
body    { font-family: var(--brand-body-fontFamily); }
h1,h2,h3,h4 { font-family: var(--brand-heading-fontFamily); }
code, pre   { font-family: var(--brand-fontStack-monospace); }
```

> ⚠️ **Metric fallback이 핵심**. `Mona Sans Fallback`/`Mona Sans Header Fallback`은 브라우저 내장 폰트 메트릭을 Mona Sans 치수에 맞춰 조정한 가상 폰트다. 웹폰트 로딩 중 layout shift를 방지하며, GitHub 같은 정보 밀도 사이트에서는 필수다.

---

## 05. Typography Scale

Primer는 컴포넌트별 `fontSize-*` 토큰을 사용. 기본 스케일:

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display        | 48px  | 800 | 1.15 | -0.02em |
| h00            | 40px  | 800 | 1.2  | -0.02em |
| h0             | 32px  | 800 | 1.25 | -0.01em |
| h1             | 26px  | 800 | 1.25 | -0.01em |
| h2             | 22px  | 700 | 1.25 | -0.01em |
| h3             | 20px  | 700 | 1.25 | 0em |
| h4             | 16px  | 700 | 1.5  | 0em |
| h5             | 14px  | 600 | 1.5  | 0em |
| h6             | 12px  | 600 | 1.5  | 0em |
| body-normal    | 14px  | 400 | 1.5  | 0em |
| body-small     | 12px  | 400 | 1.5  | 0em |
| caption        | 12px  | 400 | 1.4  | 0em |
| code           | 12px  | 400 | 1.45 | 0em |

> ⚠️ Mona Sans는 variable font여서 `550`, `450`, `200` 같은 비표준 weight가 실제 CSS에 존재한다. 특히 `550`은 label/button에 미묘한 강조를 주는 Primer의 시그너처.

---

## 06. Colors

### 06-1. Dark Mode (default — `data-color-mode="dark"`)

#### Canvas & Background

| Token | Hex |
|---|---|
| `--bgColor-default`        | `#0d1117` |
| `--bgColor-inset`          | `#010409` |
| `--bgColor-muted`          | `#151b23` |
| `--bgColor-subtle`         | `#212830` |
| `--bgColor-emphasis`       | `#3d444d` |
| `--bgColor-neutral-muted`  | `#656c7633` |

#### Foreground (text)

| Token | Hex |
|---|---|
| `--fgColor-default`  | `#f0f6fc` |
| `--fgColor-muted`    | `#9198a1` |
| `--fgColor-onEmphasis`| `#ffffff` |
| `--fgColor-disabled` | `#656c76` |

#### Border

| Token | Hex |
|---|---|
| `--borderColor-default`  | `#3d444d` |
| `--borderColor-muted`    | `#3d444db3` |
| `--borderColor-emphasis` | `#656c76` |

### 06-2. Light Mode (`data-color-mode="light"`)

| Token | Hex |
|---|---|
| `--bgColor-default` | `#ffffff` |
| `--bgColor-inset`   | `#f6f8fa` |
| `--fgColor-default` | `#1f2328` |
| `--fgColor-muted`   | `#59636e` |
| `--borderColor-default` | `#d1d9e0` |

### 06-3. Semantic Scale — emphasis / muted / fg (Dark)

Primer의 핵심 컨셉: 모든 상태 색은 **emphasis** (강조 fill), **muted** (배경 tint, 알파 포함), **fg** (텍스트 전용) 3단계로 구성된다.

| Role | emphasis (fill) | muted (tint) | fg (text) |
|---|---|---|---|
| accent     | `#1f6feb` | `#388bfd1a` | `#4493f8` |
| success    | `#238636` | `#2ea04326` | `#3fb950` |
| attention  | `#9e6a03` | `#bb800926` | `#d29922` |
| danger     | `#da3633` | `#f851491a` | `#f85149` |
| done       | `#8957e5` | `#ab7df826` | `#a371f7` |
| severe     | `#bd561d` | `#db6d2826` | `#db6d28` |
| sponsors   | `#bf4b8a` | —           | `#db61a2` |

**`done`** 은 merged PR 전용 보라. **`sponsors`** 는 GitHub Sponsors 분홍색.

### 06-4. Button Primary (interactive states)

| State | bgColor | borderColor |
|---|---|---|
| rest     | `#238636` | `#238636` |
| hover    | `#29903b` | `#29903b` |
| active   | `#2e9a40` | `#2e9a40` |
| disabled | `#105823` | `#105823` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--fgColor-link`              | `#4493f8` | 링크 기본 |
| `--fgColor-link-hover`        | `#79c0ff` | 링크 호버 |
| `--borderColor-accent-emphasis`| `#1f6feb` | focus ring |
| `--bgColor-accent-emphasis`   | `#1f6feb` | CTA primary |
| `--color-prettylights-syntax-keyword`| `#ff7b72` | 코드 keyword |
| `--color-prettylights-syntax-string`| `#a5d6ff` | 코드 string |

### 06-6. Semantic Alias Layer

Primer는 alias를 변수 체인으로 구성. 예시:

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-primary-bgColor-rest`     | `#238636`  | 녹색 CTA (e.g. "New repository") |
| `--button-primary-bgColor-hover`    | `#29903b`  | 호버 상태 |
| `--button-primary-fgColor-rest`     | `#ffffff`  | 버튼 텍스트 |
| `--label-success-bgColor`           | `#238636`  | green "merged" label |
| `--label-done-bgColor`              | `#8957e5`  | purple "done" label |
| `--label-attention-fgColor-rest`    | `#d29922`  | yellow warning text |

### 06-7. Dominant Colors (실제 DOM 빈도 순 — 다크 모드 크롤)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 592 | transparent 슬롯 |
| 2 | `#FFFFFF`   | 454 | onEmphasis text |
| 3 | `#FFFFFF00` | 267 | transparent white |
| 4 | `#010409`   | 204 | canvas-inset (deep bg) |
| 5 | `#01040966` | 166 | shadow α40 |
| 6 | `#F0F6FC`   | 157 | fgColor-default (다크) |
| 7 | `#656C76`   | 138 | neutral |
| 8 | `#59636E`   | 138 | muted-fg |
| 9 | `#3D444D`   | 128 | border-default |
| 10| `#B7BDC8`   | 122 | text variant |
| 11| `#2A313C`   | 102 | canvas-subtle |
| 12| `#2F3742`   |  82 | surface-2 |

---

## 07. Spacing

Primer는 rem 기반 8pt 그리드. `--base-size-*` 접두사 사용.

| Token | Value | Use case |
|---|---|---|
| `--base-size-2`   | 2px   | micro gap |
| `--base-size-4`   | 4px   | tight gap |
| `--base-size-6`   | 6px   | icon-text gap |
| `--base-size-8`   | 8px   | component padding |
| `--base-size-12`  | 12px  | button padding |
| `--base-size-16`  | 16px  | card padding |
| `--base-size-20`  | 20px  | section inner |
| `--base-size-24`  | 24px  | section gap |
| `--base-size-28`  | 28px  | list gap |
| `--base-size-32`  | 32px  | major section gap |
| `--base-size-36`  | 36px  | — |
| `--base-size-40`  | 40px  | block gap |
| `--base-size-44`  | 44px  | touch target |
| `--base-size-48`  | 48px  | — |
| `--base-size-64`  | 64px  | layout gutter |
| `--base-size-80`  | 80px  | hero padding |
| `--base-size-96`  | 96px  | major page gutter |
| `--base-size-112` | 112px | — |
| `--base-size-128` | 128px | page outer |

**Naming convention**: 토큰 숫자 = px 값 (`base-size-16 = 16px`). 8pt 그리드 기반이지만 4pt 단위도 포함.

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--borderRadius-small`  | 4px   | input, label |
| `--borderRadius-medium` | 6px   | button, card (**가장 많음** — 30회) |
| `--borderRadius-large`  | 8px   | dialog, popover |
| `--borderRadius-xlarge` | 12px  | hero card |
| `--borderRadius-full`   | 100px | pill badge, avatar |

---

## 09. Shadows

Primer는 **2축 shadow 체계**: `resting` (정적 카드) vs `floating` (팝오버/모달) × size 단계.

| Level | Value | Usage |
|---|---|---|
| `--shadow-resting-xsmall` | `0 1px 1px 0 #010409cc` | 얇은 카드 |
| `--shadow-resting-small`  | `0 1px 1px 0 #01040999, 0 1px 3px 0 #01040999` | 기본 카드 |
| `--shadow-resting-medium` | `0 1px 1px 0 #01040966, 0 3px 6px 0 #010409cc` | 강조 카드 |
| `--shadow-floating-small` | `0 0 0 1px #3d444d, 0 6px 12px -3px #01040966, 0 6px 18px 0 #01040966` | 드롭다운 |
| `--shadow-floating-medium`| `0 0 0 1px #3d444d, 0 8px 16px -4px #01040966, 0 4px 32px 0 #010409` | 팝오버 |
| `--shadow-floating-large` | `0 0 0 1px #3d444d, 0 24px 48px 0 #010409` | 모달 |

> ⚠️ 모든 `floating-*` shadow는 `0 0 0 1px #3d444d` hairline ring이 **첫 레이어**로 들어간다. 이 1px 링이 빠지면 GitHub 팝오버/모달이 "배경과 섞이는" 느낌이 난다.

---

## 11. Layout Patterns

### Hero (marketing)
- Layout: 중앙 정렬 단일 컬럼 또는 2-column 스플릿
- Background: `#0d1117` + SVG 그라디언트 오비트
- H1: `48-64px` / weight `800` / tracking `-0.02em`
- Max-width: 1280px

### Repository page (product UI)
- Layout: 좌측 파일 트리 + 중앙 컨텐츠 + 우측 메타 패널
- Container max-width: 1280px (`--pageLayout-contentWidth-xxlarge`)
- Gutter: `--base-size-24`

### Section Rhythm
```css
section { padding: var(--base-size-64) var(--base-size-24); }
.Box    { border-radius: 6px; border: 1px solid var(--borderColor-default); }
```

---

## 12. Components

### 12.1 Button Primary

```html
<button class="Button Button--primary Button--medium">
  <span class="Button-content">
    <span class="Button-label">New repository</span>
  </span>
</button>
```

| Spec | Value |
|---|---|
| Background  | `#238636` (`--button-primary-bgColor-rest`) |
| Hover       | `#29903b` |
| Active      | `#2e9a40` |
| Text        | `#ffffff` |
| Border      | `1px solid #238636` |
| Padding     | `5px 16px` |
| Radius      | `6px` |
| Font weight | `500` |

### 12.2 Button Default

| Spec | Value |
|---|---|
| Background | `#212830` (`--button-default-bgColor-rest`) |
| Hover      | `#2a313c` |
| Text       | `#f0f6fc` |
| Border     | `1px solid #3d444d` |

### 12.3 Label

```html
<span class="Label Label--accent">enhancement</span>
<span class="Label Label--success">merged</span>
<span class="Label Label--done">done</span>
```

| Variant | bgColor | borderColor | fgColor |
|---|---|---|---|
| accent   | `#388bfd1a` | `#1f6feb` | `#4493f8` |
| success  | `#2ea04326` | `#238636` | `#3fb950` |
| attention| `#bb800926` | `#9e6a03` | `#d29922` |
| danger   | `#f851491a` | `#da3633` | `#f85149` |
| done     | `#ab7df826` | `#8957e5` | `#a371f7` |

### 12.4 Box (generic card)

```html
<div class="Box">
  <div class="Box-header">
    <h3 class="Box-title">Pinned</h3>
  </div>
  <div class="Box-body">…</div>
</div>
```

| Spec | Value |
|---|---|
| Background | `#151b23` (`--bgColor-muted`) |
| Border     | `1px solid #3d444d` |
| Radius     | `6px` |
| Header padding | `16px` |

---

## 14. Drop-in CSS

```css
/* GitHub — copy into your root stylesheet */
:root[data-color-mode="dark"] {
  /* Fonts */
  --brand-body-fontFamily:    "Mona Sans", "Mona Sans Fallback", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --brand-heading-fontFamily: "Mona Sans", "Mona Sans Header Fallback", -apple-system, sans-serif;
  --fontStack-monospace:      ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;

  /* Canvas */
  --bgColor-default: #0d1117;
  --bgColor-inset:   #010409;
  --bgColor-muted:   #151b23;
  --bgColor-subtle:  #212830;

  /* Text */
  --fgColor-default: #f0f6fc;
  --fgColor-muted:   #9198a1;
  --fgColor-onEmphasis: #ffffff;

  /* Border */
  --borderColor-default:  #3d444d;
  --borderColor-muted:    #3d444db3;
  --borderColor-emphasis: #656c76;

  /* Semantic (emphasis) */
  --bgColor-accent-emphasis:    #1f6feb;
  --bgColor-success-emphasis:   #238636;
  --bgColor-attention-emphasis: #9e6a03;
  --bgColor-danger-emphasis:    #da3633;
  --bgColor-done-emphasis:      #8957e5;

  /* Semantic (fg) */
  --fgColor-accent:    #4493f8;
  --fgColor-success:   #3fb950;
  --fgColor-attention: #d29922;
  --fgColor-danger:    #f85149;

  /* Radius */
  --borderRadius-small:  4px;
  --borderRadius-medium: 6px;
  --borderRadius-large:  8px;

  /* Shadow */
  --shadow-resting-small:  0 1px 1px 0 #01040999, 0 1px 3px 0 #01040999;
  --shadow-floating-small: 0 0 0 1px #3d444d, 0 6px 12px -3px #01040966, 0 6px 18px 0 #01040966;

  /* Spacing */
  --base-size-4:  4px;
  --base-size-8:  8px;
  --base-size-16: 16px;
  --base-size-24: 24px;
  --base-size-32: 32px;
  --base-size-48: 48px;
  --base-size-64: 64px;
}

body {
  background: var(--bgColor-default);
  color: var(--fgColor-default);
  font-family: var(--brand-body-fontFamily);
  font-size: 14px;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  font-family: var(--brand-heading-fontFamily);
  font-weight: 800;
  letter-spacing: -0.01em;
}

code, pre { font-family: var(--fontStack-monospace); }
a { color: var(--fgColor-accent); }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — GitHub (Primer dark)
module.exports = {
  darkMode: ['class', '[data-color-mode="dark"]'],
  theme: {
    extend: {
      colors: {
        canvas: {
          default: '#0d1117',
          inset:   '#010409',
          muted:   '#151b23',
          subtle:  '#212830',
        },
        fg: {
          default:     '#f0f6fc',
          muted:       '#9198a1',
          onEmphasis:  '#ffffff',
          accent:      '#4493f8',
          success:     '#3fb950',
          attention:   '#d29922',
          danger:      '#f85149',
          done:        '#a371f7',
        },
        accent:   { emphasis: '#1f6feb', muted: '#388bfd1a' },
        success:  { emphasis: '#238636', muted: '#2ea04326' },
        attention:{ emphasis: '#9e6a03', muted: '#bb800926' },
        danger:   { emphasis: '#da3633', muted: '#f851491a' },
        done:     { emphasis: '#8957e5', muted: '#ab7df826' },
        border:   { default: '#3d444d', muted: '#3d444db3' },
      },
      fontFamily: {
        sans: ['Mona Sans', 'Mona Sans Fallback', '-apple-system', 'sans-serif'],
        heading: ['Mona Sans', 'Mona Sans Header Fallback', '-apple-system', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'SF Mono', 'Menlo', 'Consolas', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        'semi':   '550',   // Mona Sans variable
        heading:  '800',
      },
      borderRadius: {
        sm: '4px', md: '6px', lg: '8px', xl: '12px', full: '100px',
      },
      boxShadow: {
        'resting-sm':  '0 1px 1px 0 #01040999, 0 1px 3px 0 #01040999',
        'resting-md':  '0 1px 1px 0 #01040966, 0 3px 6px 0 #010409cc',
        'floating-sm': '0 0 0 1px #3d444d, 0 6px 12px -3px #01040966, 0 6px 18px 0 #01040966',
        'floating-md': '0 0 0 1px #3d444d, 0 8px 16px -4px #01040966, 0 4px 32px 0 #010409',
        'floating-lg': '0 0 0 1px #3d444d, 0 24px 48px 0 #010409',
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- `--bgColor-default: #0d1117` (다크) / `#ffffff` (라이트) 두 모드 모두 문서화. `data-color-mode` 속성 기반 스위치.
- Semantic color는 **3단계** (`emphasis` / `muted` / `fg`)로 구성. 단일 hex로 끝내지 말 것.
- Heading 폰트에 **`Mona Sans Header Fallback`** 별도 지정. Body는 `Mona Sans Fallback`. 두 폴백은 다르다.
- Primary 버튼은 **녹색** (`#238636`), 파란색 아님. 파란색은 accent/link 역할.
- `done` purple (`#8957e5`)을 merged PR 전용으로 사용.
- Shadow는 2축 체계 (`resting` / `floating`). `floating-*`에는 `0 0 0 1px #3d444d` hairline ring 필수 첫 레이어.
- Spacing은 `--base-size-{N}` 포맷, 숫자가 곧 px 값.
- Variable weight 활용: `550` (label), `800` (heading), `200` (thin accent).

### ❌ DON'T
- ❌ `#0969DA` (라이트 v1 accent)를 다크 사이트에 쓰지 말 것 → 실제는 `#1f6feb`.
- ❌ `#24292F`를 body text color로 쓰지 말 것 → 다크 모드는 `#f0f6fc`.
- ❌ `#2DA44E` (라이트 success)를 다크에 쓰지 말 것 → 다크 success emphasis는 `#238636`.
- ❌ Primary 버튼을 파란색으로 만들지 말 것 — GitHub primary CTA는 녹색.
- ❌ Semantic color를 단일 hex로 표현하지 말 것 → `emphasis`/`muted`/`fg` 튜플 필수.
- ❌ 단일 `box-shadow` 사용 금지 → `floating-*`는 최소 2-3 레이어 합성.
- ❌ `font-weight: 700`만 쓰지 말 것 → Mona Sans variable의 200/450/550/800이 실제 시그너처.
- ❌ `#0d1117` 대신 `#0a0a0a` / `#000` 같은 순 검정 사용 금지 — Primer canvas는 살짝 파란 기가 있는 `#0d1117`.
