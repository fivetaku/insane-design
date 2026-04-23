---
schema_version: 3.1
slug: microsoft
service_name: Microsoft
site_url: https://www.microsoft.com/en-us
fetched_at: 2026-04-23
default_theme: light
brand_color: "#0067B8"
primary_font: Segoe UI
font_weight_normal: 400
token_prefix: --ds-*

bold_direction: "Modular Fluent"
aesthetic_category: "Refined SaaS"
signature_element: section_transition
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Microsoft (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere

Microsoft의 현재 `https://www.microsoft.com/en-us` 홈은 하나의 단일 디자인 시스템이 아니라, **Reimagine `--ds-*` 토큰 레이어와 UHF(Universal Header Framework) 레거시 크롬이 공존하는 하이브리드 페이지**다. 페이지 본문 모듈은 `reimagine-*` 웹 컴포넌트로 재구성되어 있고, 상단/하단 크롬은 여전히 `uhf-*`와 literal color 중심의 오래된 레이어를 유지한다. 그래서 이 사이트를 Microsoft답게 만드는 핵심은 "깔끔한 Fluent 카드" 자체보다, **두 시스템이 충돌하지 않고 나란히 돌아가는 안정감**이다.

컬러 전략도 이 이중 구조를 그대로 드러낸다. 글로벌 링크와 UHF 크롬은 base/UHF CSS에 박혀 있는 `#0067B8`를 계속 사용한다. 실제로 `base...min.css`의 `a { color: #0067b8 }`와 `uhf...style-*.css`의 `--uhf-header-cart-bg-color ... #0067b8`가 이를 증명한다. 반면 Reimagine 토큰은 `store...min.css`에서 `--ds-color-brilliant-blue-500: #0078d4`를 anchor로 삼고, hover/pressed를 `#006DC1`, `#002948`까지 내려간다. 결과적으로 Microsoft 홈은 "브랜드 블루 하나"가 아니라 **legacy blue `#0067B8` + Fluent accent blue `#0078D4`**의 두 축으로 읽혀야 맞다.

타이포그래피는 여전히 Segoe 중심이다. Reimagine bundle은 `--ds-font-family-segoe-variable-display`, `--ds-font-family-segoe-variable-text`, `--ds-font-family-segoe-variable-small`로 Segoe UI Variable 3축을 선언하고, base bundle은 `@font-face`로 `local("Segoe UI")`와 Microsoft CDN(`c.s-microsoft.com`) 폰트를 함께 로드한다. 헤딩은 `500/600`과 큰 size scale을, body는 `400`과 `-0.03em` letter-spacing을 사용해 **깔끔하지만 지나치게 차갑지 않은 기업형 readable UI**를 만든다.

레이아웃은 카드 중심이지만 단순 카드 나열은 아니다. hero는 `<reimagine-hero-featured-slider>` 안에서 `<reimagine-carousel autoplay-interval="7000">`로 움직이고, 카드 영역은 `<reimagine-card-feature clickable>`와 `<reimagine-carousel-card-grid>`가 반복된다. 여기에 `theme="night"`와 `background="special-color"` 같은 속성이 끼어들어, 라이트 베이스 위에 필요한 순간만 어두운 패널과 그래디언트를 얹는다. 즉 Microsoft의 공간 전략은 미니멀이라기보다 **모듈형 편집 시스템**에 가깝다.

인터랙션도 과장 대신 제어가 핵심이다. UHF와 chat bundle에는 `background-color .2s ease`, `fill .2s ease`, `all .2s` 같은 짧은 transition이 깔려 있고, media player는 `opacity .3s ease-in-out`으로 나타난다. hero의 긴 움직임은 flashy animation이 아니라 7초 autoplay carousel에서 온다. 즉 Microsoft는 motion으로 놀라게 하기보다 **상태 변화가 명확한 제품 문법**을 유지한다.

### Key Characteristics

- Reimagine 본문 `--ds-*` 842개 + UHF 크롬 `--uhf-*` 20개가 공존하는 hybrid stack
- legacy Microsoft blue `#0067B8`와 Reimagine accent blue `#0078D4`의 이중 구조
- `Segoe UI Variable` / `Segoe UI` 기반 3축 폰트 패밀리
- `reimagine-*` custom element + `uhf-*` chrome + `aem-Grid*` layout 혼합
- `--ds-spacing-*` 20개, `--ds-elevation-level-*` 6단 shadow 시스템
- hero slider 7초 autoplay, 일반 hover/focus는 `0.2s` 중심
- 밝은 카드 표면 + 선택적 night theme 패널의 section-by-section 전환

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Modular Fluent
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **Reimagine Fluent 카드와 UHF 레거시 블루 크롬이 한 화면에서 이어지는 모듈 전환감**으로 기억된다.
> **Code Complexity**: high — `--ds-*` 토큰 레이어, custom element, AEM markup, UHF legacy CSS가 동시에 존재한다.

---

## 01. Quick Start

> 5분 안에 Microsoft처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family:
    "Segoe UI Variable Text",
    "Segoe UI",
    SegoeUI,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
  font-weight: 400;
}

/* 2. 표면 + 본문 */
:root {
  --bg: #ffffff;
  --surface: #f8f7f8;
  --border: #e7e7e7;
  --fg: #0e1726;
  --fg-subtle: #17253d;
}

/* 3. 블루는 두 축으로 분리 */
:root {
  --brand: #0067b8;         /* legacy header / link blue */
  --brand-accent: #0078d4;  /* Reimagine accent fill */
  --brand-accent-hover: #006dc1;
}
```

**절대 하지 말아야 할 것 하나**: `#0067B8`와 `#0078D4`를 같은 역할로 합쳐 쓰지 마라. live Microsoft 홈은 header/footer/link chrome에는 `#0067B8`, tokenized accent fill에는 `#0078D4` 계열을 쓴다. 둘을 구분하지 않으면 바로 "Fluent를 닮은 아무 사이트"처럼 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.microsoft.com/en-us` |
| Fetched | 2026-04-23 |
| Extractor | `curl_cffi.requests.Session(impersonate="chrome")` + CSS 직접 파싱 |
| HTML size | `214258` bytes |
| CSS files | `11`개 외부 + `1`개 inline, 총 `576134` chars |
| Primary token bundle | `store.ACSHASH94d661eddae45b14c9f57e0b79a7fe67.min.css` (`58773` chars, `--ds-*` 832개) |
| Chrome bundle | `uhf.microsoft.com/.../style-BpAANDpw.css` (`452610` chars, `--uhf-*` 20개 + icon vars 다수) |
| Token prefix | `--ds-*` (본문), `--uhf-*` (header/footer chrome) |
| Method | CSS 커스텀 프로퍼티와 실제 markup 직접 확인 · AI 추측 없음 |

---

## 03. Tech Stack

- **Framework**: Adobe Experience Manager + Cascade Reimagine web components + UHF chrome
- **Design system**: Reimagine theme tokens — prefix `--ds-*`
- **CSS architecture**: palette → semantic theme → component slot의 3층 구조
  ```
  palette   (--ds-color-*)     raw ramps and neutrals
  semantic  (--ds-theme-*)     background / foreground / border aliases
  chrome    (--uhf-* + literals)  header, footer, cart, search chrome
  ```
- **Markup layer**: `reimagine-*` custom element, `uhf-*` shell, `aem-Grid*` layout classes
- **Default theme**: light base, 일부 hero/featured 모듈만 `theme="night"`
- **Font loading**: `local("Segoe UI")` + `c.s-microsoft.com` hosted Segoe files + Segoe UI Variable family tokens
- **Canonical anchor**: `#0067B8` for global chrome, `#0078D4` for tokenized accent fill
- **Animation primitives**: hero carousel `autoplay-interval="7000"`, hover/fill transition `.2s`, media fade `.3s ease-in-out`
- **Fluent audit**: live CSS에는 Fluent Web 공개 토큰명(`--colorBrandBackground`)이 직접 노출되지 않고, 의미상 동등한 내부 alias `--ds-theme-background-accent-strong-normal`이 쓰인다

---

## 04. Font Stack

- **Display**: `--ds-font-family-segoe-variable-display`
- **Body**: `--ds-font-family-segoe-variable-text`
- **Small / label**: `--ds-font-family-segoe-variable-small`
- **Legacy chrome**: `--uhf-font-family`
- **Code**: `SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --ms-font-display:
    "Segoe UI Variable Display",
    "Segoe UI",
    SegoeUI,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
  --ms-font-body:
    "Segoe UI Variable Text",
    "Segoe UI",
    SegoeUI,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
  --ms-font-small:
    "Segoe UI Variable Small",
    "Segoe UI",
    SegoeUI,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
  --ms-font-uhf:
    "Segoe UI",
    SegoeUI,
    "Helvetica Neue",
    Helvetica,
    Arial,
    sans-serif;
}
```

> **라이브 근거**: base bundle의 `@font-face`는 `local("Segoe UI")`를 우선 사용하고, store bundle은 Segoe UI Variable 3패밀리를 토큰으로 선언한다.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--ds-label-eyebrow-*` | `0.75rem` | `600` | `1rem` | `0.08em` |
| `--ds-body-xs-*` | `0.75rem` | `400` | `1rem` | `-0.03em` |
| `--ds-body-s-*` | `0.875rem` | `400` | `1.25rem` | `-0.03em` |
| `--ds-body-m-*` | `1rem` | `400` | `1.5rem` | `-0.03em` |
| `--ds-body-l-*` | `1.125rem` | `400` | `1.75rem` | `-0.03em` |
| `--ds-heading-3xs-*` | `1rem` | `600` | `1.5rem` | `normal` |
| `--ds-heading-2xs-*` | `1.125rem` | `600` | `1.5rem` | `normal` |
| `--ds-heading-xs-*` | `1.25rem` | `500` | `1.75rem` | `-0.01em` |
| `--ds-heading-s-*` | `1.5rem` | `500` | `2rem` | `-0.015em` |
| `--ds-heading-m-*` | `2rem` | `500` | `2.5rem` | `-0.025em` |
| `--ds-heading-l-*` | `2.5rem` | `500` | `3rem` | `-0.025em` |
| `--ds-heading-xl-*` | `3rem` | `500` | `3.5rem` | `-0.025em` |
| `--ds-heading-2xl-*` | `3.5rem` | `400` | `3.875rem` | `-0.025em` |
| `--ds-heading-3xl-*` | `4.75rem` | `400` | `5.125rem` | `-0.025em` |

> **핵심 인사이트**: mid heading(`xs~xl`)은 `500`, giant display(`2xl/3xl`)는 오히려 `400`으로 내려간다. Microsoft는 거대한 헤드를 굵게 누르기보다, **Segoe UI Variable의 넓은 면적과 긴 line-height**로 기업형 임팩트를 만든다.

---

## 06. Colors

### 06-1. Brand Split: Legacy Blue + Reimagine Accent

| Source | Token / literal | Hex | Usage |
|---|---|---|---|
| Base / UHF | literal `#0067B8` ★ | `#0067B8` | global links, cart badge, chrome accent |
| Reimagine | `--ds-color-brilliant-blue-500` | `#0078D4` | semantic accent fill |
| Reimagine | `--ds-color-brilliant-blue-600` | `#006DC1` | accent hover |
| Reimagine | `--ds-color-brilliant-blue-700` | `#005597` | accent selected |
| Reimagine | `--ds-color-brilliant-blue-900` | `#002948` | accent pressed / deepest blue |

### 06-2. Reimagine Brand Ramp

| Token | Hex |
|---|---|
| `--ds-color-brilliant-blue-50` | `#E6F2FB` |
| `--ds-color-brilliant-blue-100` | `#B0D5F2` |
| `--ds-color-brilliant-blue-300` | `#54A5E2` |
| `--ds-color-brilliant-blue-500` | `#0078D4` |
| `--ds-color-brilliant-blue-600` | `#006DC1` |
| `--ds-color-brilliant-blue-700` | `#005597` |
| `--ds-color-brilliant-blue-800` | `#004275` |
| `--ds-color-brilliant-blue-900` | `#002948` |

### 06-3. Neutral Ramp

| Role | Token | Hex |
|---|---|---|
| page white | `--ds-color-neutral-white` | `#FFFFFF` |
| card hover white | `--ds-color-off-white-300` | `#F8F7F8` |
| surface alt | `--ds-color-off-white-500` | `#F4F3F5` |
| border fade | `--ds-color-vapor-gray-100` | `#E7E7E7` |
| border / icon neutral | `--ds-color-vapor-gray-500` | `#B1B3B3` |
| tertiary text | `--ds-color-vapor-gray-800` | `#616262` |
| deep neutral | `--ds-color-vapor-gray-900` | `#3C3D3D` |
| dark ink | `--ds-color-dark-blue-900` | `#0E1726` |
| dark text secondary | `--ds-color-dark-blue-800` | `#17253D` |
| dark panel accent | `--ds-color-dark-blue-500` | `#2A446F` |

### 06-4. Accent Families

| Family | Key token | Hex |
|---|---|---|
| sky blue highlight | `--ds-color-sky-blue-100` | `#DCEEF8` |
| sky blue strong | `--ds-color-sky-blue-300` | `#B3DAF0` |
| sky blue tint | `--ds-color-sky-blue-500` | `#8DC8E8` |
| lavender supportive | `--ds-color-lavender-500` | `#C5B4E3` |
| lavender tint | `--ds-color-lavender-300` | `#D8CDEC` |
| lavender fade | `--ds-color-lavender-100` | `#EDE8F6` |
| twilight purple | `--ds-color-twilight-purple-500` | `#463668` |
| twilight purple dark | `--ds-color-twilight-purple-900` | `#181223` |
| yellow alert | `--ds-color-golden-yellow-500` | `#FFB900` |
| magenta accent | `--ds-color-red-violet-500` | `#C03BC4` |

### 06-5. Semantic

| Alias | Resolves to | Usage |
|---|---|---|
| `--ds-theme-background-accent-strong-normal` | `#0078D4` | primary accent background |
| `--ds-theme-background-accent-strong-hover` | `#006DC1` | accent hover |
| `--ds-theme-background-accent-strong-pressed` | `#002948` | accent pressed |
| `--ds-theme-border-accent-strong-normal` | `#0078D4` | accent stroke |
| `--ds-theme-foreground-accent-strong-normal` | `#FFFFFF` | text/icon on accent fill |
| `--ds-theme-background-card-normal` | `#FFFFFF` | card default surface |
| `--ds-theme-background-card-hover` | `#F8F7F8` | card hover surface |
| `--ds-theme-background-highlight-normal` | `#DCEEF8` | soft highlight block |
| `--ds-theme-foreground-base-strong` | `#0E1726` | primary text |
| `--ds-theme-foreground-base-subtle` | `#17253D` | secondary text |
| `--ds-theme-border-neutral-fade` | `#E7E7E7` | light divider |
| `--ds-theme-border-neutral-pure` | `#B1B3B3` | harder neutral border |
| `--ds-theme-background-supportive-color` | `#C5B4E3` | supportive / secondary panel |
| `--ds-theme-foreground-supportive-icon-dark` | `#181223` | supportive icon on lavender |

### 06-6. Fluent Token Audit

| Status | Token |
|---|---|
| live CSS에서 직접 발견 안 됨 | `--colorBrandBackground` |
| live CSS에서 직접 발견 안 됨 | `--colorBrandForeground1` |
| live CSS에서 직접 발견 안 됨 | `--colorNeutralForeground1` |
| closest live background alias | `--ds-theme-background-accent-strong-normal` |
| closest live border alias | `--ds-theme-border-accent-strong-normal` |
| closest live foreground alias | `--ds-theme-foreground-accent-strong-normal` |

> **중요**: Microsoft 홈은 Fluent Web 공개 변수명을 그대로 노출하지 않는다. 실제 페이지는 같은 의미층을 내부 `--ds-theme-*` alias로 운용한다.

### 06-7. Dominant Colors (실제 CSS 빈도, normalized)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 38 | base surface / card |
| 2 | `#0078D4` | 19 | Reimagine accent |
| 3 | `#F4FAFD` | 11 | highlight surface |
| 4 | `#000000` | 10 | icons / base text |
| 5 | `#E6F2FB` | 9 | brilliant blue 50 |
| 6 | `#2A446F` | 8 | dark blue panel |
| 7 | `#0067B8` | 7 | legacy Microsoft blue |
| 8 | `#B3DAF0` | 7 | sky blue strong |
| 9 | `#005A9E` | 7 | legacy dark blue |
| 10 | `#106EBE` | 7 | legacy hover blue |

---

## 07. Spacing

| Token / observation | Value | Use case |
|---|---|---|
| `--ds-spacing-1` | `0.125rem` (`2px`) | micro nudge |
| `--ds-spacing-2` | `0.25rem` (`4px`) | icon / eyebrow gaps |
| `--ds-spacing-3` | `0.5rem` (`8px`) | chip / small stack |
| `--ds-spacing-4` | `0.75rem` (`12px`) | compact padding |
| `--ds-spacing-6` | `1rem` (`16px`) | standard inner padding |
| `--ds-spacing-7` | `1.5rem` (`24px`) | card / row gap |
| `--ds-spacing-8` | `2rem` (`32px`) | section block spacing |
| `--ds-spacing-9` | `3rem` (`48px`) | generous section spacing |
| `--ds-spacing-10` | `3.5rem` (`56px`) | hero / large offset |
| `--ds-card-padding-default` | `1rem` | default card padding |
| `--ds-card-padding-comfortable` | `1.5rem` | comfortable card padding |
| `--ds-card-padding-relaxed` | `2rem` | relaxed / featured card padding |
| UHF desktop shell | `padding-left/right: 5%` | wide header/footer chrome |
| UHF tablet shell | `padding-left/right: 24px` | mid viewport chrome |

---

## 08. Radius

> live Microsoft CSS에는 통일된 `--ds-radius-*` 토큰군이 없고, radius가 컴포넌트별 literal 값으로 흩어져 있다.

| Literal | Context |
|---|---|
| `0` | media edges, reset, square shells |
| `4px` | chat input shell |
| `8px` | compact prompt/input state |
| `10px` | UHF cart count badge |
| `16px` | prompt pill / rounded chip |
| `24px` | desktop chat container |
| `25px` | contained chat hero capsule |
| `50% / 100px` | spinners and circular affordances |

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| `--ds-elevation-level-1` | `0 0 .125rem rgba(0,0,0,.12), 0 .063rem .125rem rgba(0,0,0,.14)` | subtle surface lift |
| `--ds-elevation-level-2` | `0 0 .125rem rgba(0,0,0,.12), 0 .125rem .25rem rgba(0,0,0,.14)` | light card |
| `--ds-elevation-level-3` | `0 0 .125rem rgba(0,0,0,.12), 0 .25rem .5rem rgba(0,0,0,.14)` | floating card |
| `--ds-elevation-level-4` | `0 0 .125rem rgba(0,0,0,.12), 0 .5rem 1rem rgba(0,0,0,.14)` | popover / deeper tray |
| `--ds-elevation-level-5` | `0 0 .5rem rgba(0,0,0,.12), 0 .875rem 1.75rem rgba(0,0,0,.14)` | modal-like shell |
| `--ds-elevation-level-6` | `0 0 .5rem rgba(0,0,0,.12), 0 2rem 4rem rgba(0,0,0,.14)` | hero / high emphasis |
| chat input observed | `0 0 2px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.14)` | actual chat input container |

---

## 10. Motion

| Pattern | Value | Source |
|---|---|---|
| hero carousel autoplay | `7000ms` | `<reimagine-carousel autoplay-interval="7000">` |
| primary hover transitions | `.2s` | UHF / chat / icon fill transitions |
| background-color transition | `.2s ease` | UHF / chat interactive shells |
| media reveal | `opacity .3s ease-in-out` | `reimagine-media universal-media-player.ump-visible` |
| chat pill hover | `transition: all .2s` | `.msstore-chatonpage__prompt-pill` |

> Microsoft의 motion은 "기능적 이동"에 가깝다. 긴 인상을 만드는 건 hero carousel의 7초 리듬이고, 나머지는 거의 전부 `.2s` 안쪽의 상태 변화다.

---

## 11. Layout Patterns

### Grid System

- **Shell**: `aem-Grid`, `aem-GridColumn`, `reimagine-layout`, `reimagine-layout-column`
- **Chrome**: `uhf-header`, `uhf-footer-nav-group`
- **Section mode**: card grid + featured slider + editorial text block의 반복

### Hero

```html
<reimagine-hero-featured-slider>
  <reimagine-carousel autoplay="true" autoplay-interval="7000">
    <reimagine-hero-featured-slider-item
      theme="night"
      header-layout-configuration="2-col-even"
      background="special-color">
      <reimagine-media aspect-ratio="16-9" slot="ui-shell-media"></reimagine-media>
    </reimagine-hero-featured-slider-item>
  </reimagine-carousel>
</reimagine-hero-featured-slider>
```

- Hero는 **2-column even split + 16:9 media + optional night theme**가 기본
- 첫 화면이 곧 브랜드가 아니라, 여러 corporate/editorial 메시지를 캐러셀로 순환

### Card Patterns

- `<reimagine-card-feature clickable>` + `<reimagine-media aspect-ratio="16-9" slot="card-feature__media">`
- 이미지 비율은 16:9를 강하게 유지
- CTA는 카드 내부 button group으로 붙는다

### Navigation Structure

- UHF 데스크톱은 `min-width: 1084px`에서 `padding-left/right: 5%`
- `860px` 기준으로 desktop/mobile chrome가 갈린다
- 링크 구조는 제품 허브 + support + deals를 수평으로 유지

---

## 12. Responsive Behavior

### Breakpoints

| Layer | Breakpoint | Purpose |
|---|---|---|
| Reimagine content | `480px` | content scale start |
| Reimagine content | `640px` | tablet-ish spacing/type growth |
| Reimagine content | `1024px` | desktop content layout |
| Reimagine content | `1366px` | wide content |
| Reimagine content | `1920px` | ultra-wide scale |
| Chat module | `479px / 767px` | pill/input layout switch |
| UHF chrome | `860px` | mobile vs desktop header |
| UHF chrome | `1084px` | wide desktop header padding |

### Collapsing Strategy

- hero media는 `<picture><source media="..."></picture>`로 자산 자체를 갈아낀다
- chrome은 `860px` 아래에서 모바일 header 패턴으로 전환
- chat/prompt pills는 `479px` 이하에서 더 조밀한 chip 레이아웃으로 압축
- card 영역은 carousel/card-grid 중심이라 column collapse보다 **component-level swap**이 많다

### Touch Targets

- prompt pill observed height: `32px`
- chat input shell observed height: `66px`
- UHF cart/count badge는 compact하지만 text/icon gap을 `4px`로 유지

---

## 13. Components

### Primary CTA (Reimagine)

```html
<reimagine-button
  shape="rounded"
  appearance="button--primary"
  button-label="Learn more">
  <a href="https://unlocked.microsoft.com/sustainability?icid=mscom_marcom_H1a_Sustainability2026">
    Learn more
  </a>
</reimagine-button>
```

| Spec | Value |
|---|---|
| accent fill | `--ds-theme-background-accent-strong-normal` → `#0078D4` |
| hover | `--ds-theme-background-accent-strong-hover` → `#006DC1` |
| pressed | `--ds-theme-background-accent-strong-pressed` → `#002948` |
| foreground | `--ds-theme-foreground-accent-strong-normal` → `#FFFFFF` |
| shape signal | `shape="rounded"` |

> **근거 범위**: 실제 component module styling은 custom element 내부에서 처리되지만, live CSS가 accent semantic token chain을 명확히 제공한다.

### Feature Card

```html
<reimagine-card-feature clickable>
  <reimagine-media aspect-ratio="16-9" slot="card-feature__media"></reimagine-media>
</reimagine-card-feature>
```

- media ratio: `16:9`
- default surface: `--ds-theme-background-card-normal` → `#FFFFFF`
- hover surface: `--ds-theme-background-card-hover` → `#F8F7F8`

### Header / Chrome

```html
<uhf-header></uhf-header>
```

- font: `--uhf-font-family`
- cart badge bg: `#0067B8`
- cart badge radius: `10px`
- shell padding: desktop `5%`, tablet `24px`

### Copilot Chat Prompt Pill

```css
.msstore-chatonpage__prompt-pill {
  background: linear-gradient(92deg, #0a6bba .48%, #003966 48.85%, #1f5188 99.78%);
  border: 1px solid #b3daf0;
  border-radius: 16px;
  transition: all .2s;
}
```

- 이 모듈은 Microsoft 홈에서 가장 "marketing-plus-product"하게 보이는 실제 CSS 컴포넌트다
- blue gradient, Segoe UI Variable, 16px pill radius가 동시에 드러난다

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Hero headline | 짧은 2절 병치 문장 | `Less plastic, more planet` |
| Offer headline | 숫자/혜택을 앞에 둠 | `10% off Microsoft Surface Certified Refurbished` |
| CTA | 설명보다 행동을 먼저 | `Learn more` |
| Product copy | 한 문장에 benefit 하나 | `Save on refurbished devices—more sustainable than new.` |
| Editorial / mission copy | 기술보다 결과를 앞세움 | `Protecting biodiversity with AI` |
| Tone | 차갑지 않은 기업 톤, 제품/사회 메시지 병치 | — |

---

## 15. Drop-in CSS

```css
/* Microsoft — derived from live microsoft.com CSS */
:root {
  --ms-font-display:
    "Segoe UI Variable Display","Segoe UI",SegoeUI,
    "Helvetica Neue",Helvetica,Arial,sans-serif;
  --ms-font-body:
    "Segoe UI Variable Text","Segoe UI",SegoeUI,
    "Helvetica Neue",Helvetica,Arial,sans-serif;
  --ms-font-small:
    "Segoe UI Variable Small","Segoe UI",SegoeUI,
    "Helvetica Neue",Helvetica,Arial,sans-serif;

  --ms-brand-legacy: #0067B8;
  --ms-brand-accent: #0078D4;
  --ms-brand-accent-hover: #006DC1;
  --ms-brand-accent-pressed: #002948;

  --ms-bg: #FFFFFF;
  --ms-surface: #F8F7F8;
  --ms-surface-alt: #F4F3F5;
  --ms-border: #E7E7E7;
  --ms-border-strong: #B1B3B3;
  --ms-fg: #0E1726;
  --ms-fg-subtle: #17253D;

  --ms-highlight: #DCEEF8;
  --ms-supportive: #C5B4E3;
  --ms-supportive-ink: #181223;

  --ms-space-1: 2px;
  --ms-space-2: 4px;
  --ms-space-3: 8px;
  --ms-space-4: 12px;
  --ms-space-6: 16px;
  --ms-space-7: 24px;
  --ms-space-8: 32px;
  --ms-space-9: 48px;
  --ms-space-10: 56px;

  --ms-radius-sm: 4px;
  --ms-radius-md: 8px;
  --ms-radius-lg: 16px;
  --ms-radius-xl: 24px;
  --ms-radius-pill: 999px;

  --ms-shadow-1:
    0 0 2px rgba(0,0,0,0.12),
    0 1px 2px rgba(0,0,0,0.14);
  --ms-shadow-3:
    0 0 2px rgba(0,0,0,0.12),
    0 4px 8px rgba(0,0,0,0.14);
}

body {
  font-family: var(--ms-font-body);
  color: var(--ms-fg);
  background: var(--ms-bg);
}

.ms-cta {
  display: inline-flex;
  align-items: center;
  gap: var(--ms-space-2);
  min-height: 44px;
  padding: var(--ms-space-3) var(--ms-space-7);
  border-radius: var(--ms-radius-pill);
  background: var(--ms-brand-accent);
  color: #fff;
  box-shadow: var(--ms-shadow-1);
}

.ms-card {
  background: var(--ms-bg);
  border: 1px solid var(--ms-border);
  border-radius: var(--ms-radius-lg);
  padding: var(--ms-space-8);
  box-shadow: var(--ms-shadow-3);
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Microsoft
module.exports = {
  theme: {
    extend: {
      colors: {
        ms: {
          legacy: '#0067B8',
          accent: '#0078D4',
          accentHover: '#006DC1',
          accentPressed: '#002948',
          surface: '#F8F7F8',
          surfaceAlt: '#F4F3F5',
          border: '#E7E7E7',
          borderStrong: '#B1B3B3',
          ink: '#0E1726',
          inkSubtle: '#17253D',
          highlight: '#DCEEF8',
          supportive: '#C5B4E3',
          supportiveInk: '#181223',
        },
        fluentBlue: {
          50: '#E6F2FB',
          100: '#B0D5F2',
          300: '#54A5E2',
          500: '#0078D4',
          600: '#006DC1',
          700: '#005597',
          800: '#004275',
          900: '#002948',
        },
      },
      fontFamily: {
        sans: [
          'Segoe UI Variable Text',
          'Segoe UI',
          'SegoeUI',
          'Helvetica Neue',
          'Helvetica',
          'Arial',
          'sans-serif',
        ],
        display: [
          'Segoe UI Variable Display',
          'Segoe UI',
          'SegoeUI',
          'Helvetica Neue',
          'Helvetica',
          'Arial',
          'sans-serif',
        ],
      },
      spacing: {
        1: '2px',
        2: '4px',
        3: '8px',
        4: '12px',
        6: '16px',
        7: '24px',
        8: '32px',
        9: '48px',
        10: '56px',
      },
      borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '16px',
        xl: '24px',
        pill: '999px',
      },
      boxShadow: {
        ms1: '0 0 2px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.14)',
        ms3: '0 0 2px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.14)',
        ms6: '0 0 8px rgba(0,0,0,0.12), 0 32px 64px rgba(0,0,0,0.14)',
      },
      screens: {
        chrome: '860px',
        desktop: '1084px',
        contentSm: '480px',
        contentMd: '640px',
        contentLg: '1024px',
        contentXl: '1366px',
        content2xl: '1920px',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Legacy brand blue | `--ms-brand-legacy` | `#0067B8` |
| Reimagine accent fill | `--ms-brand-accent` | `#0078D4` |
| Accent hover | `--ms-brand-accent-hover` | `#006DC1` |
| Background | `--ms-bg` | `#FFFFFF` |
| Card surface | `--ms-surface` | `#F8F7F8` |
| Border | `--ms-border` | `#E7E7E7` |
| Ink | `--ms-fg` | `#0E1726` |
| Ink subtle | `--ms-fg-subtle` | `#17253D` |
| Highlight | `--ms-highlight` | `#DCEEF8` |
| Supportive | `--ms-supportive` | `#C5B4E3` |

### Example Component Prompts

#### Hero

```
Microsoft 홈 스타일 hero.
- 구조: featured slider 느낌의 2-column even split
- 배경: white base + 필요한 경우 night panel
- 타이포: Segoe UI Variable Display 48~76px, weight 400~500
- CTA: rounded, accent fill #0078D4, text #FFFFFF
- 보조 chrome: link / shell accent는 #0067B8
- media ratio는 16:9
- 과장된 motion 대신 7초 autoplay 느낌의 조용한 이동
```

#### Feature Card

```
Microsoft Reimagine 카드.
- surface #FFFFFF
- hover surface #F8F7F8
- border 1px solid #E7E7E7
- radius 16px
- padding 24~32px
- media 16:9
- body font Segoe UI Variable Text 16px weight 400
```

#### Chrome / Header

```
Microsoft UHF 스타일 header.
- font "Segoe UI"
- background white
- desktop shell padding 5%
- tablet shell padding 24px
- link accent #0067B8
- cart/count badge radius 10px
```

### Iteration Guide

- `#0067B8`는 chrome / link blue, `#0078D4`는 accent fill로 분리해서 쓸 것
- body는 `Segoe UI Variable Text` 또는 `Segoe UI`, heading은 display family를 우선
- spacing은 `2 / 4 / 8 / 12 / 16 / 24 / 32 / 48 / 56` 그리드만 사용할 것
- radius는 token이 아니라 literal이므로 `4 / 8 / 16 / 24 / pill` 범위에 묶을 것
- hero, card, nav를 각각 다른 subsystem으로 보고 조합할 것

---

## 18. DO / DON'T

### ✅ DO

- 링크 / header chrome에는 `#0067B8`를 사용한다.
- primary accent fill에는 `#0078D4`와 hover `#006DC1`를 사용한다.
- 본문은 Segoe UI 계열 `400`, heading은 `500` 또는 giant display에서 `400`을 유지한다.
- 표면은 `#FFFFFF`와 `#F8F7F8`로 깔고 border는 `#E7E7E7`를 쓴다.
- hero는 2-column media + text split, card는 16:9 media 중심으로 설계한다.
- shadow는 단층보다 `ds-elevation`식 2-layer 조합을 따른다.
- night variant는 전체 사이트가 아니라 특정 featured module에만 제한한다.

### ❌ DON'T

- `#0067B8`와 `#0078D4`를 아무 구분 없이 하나의 primary color처럼 섞지 말 것.
- Inter, Roboto 같은 generic SaaS 폰트로 바꾸지 말 것.
- card를 모두 같은 흰 박스로만 반복하지 말 것 — hero/feature/supportive block의 톤 차이를 유지할 것.
- radius를 12px 단일값으로 고정하지 말 것 — live site는 4/8/10/16/24/25 계층을 가진다.
- hover를 400ms 이상 길게 끌지 말 것 — 실제 사이트는 `.2s` 중심이다.
- `--colorBrandBackground` 같은 공개 Fluent 토큰명이 live page에 있다고 가정하지 말 것.
- purple-heavy gradient나 glass morphism으로 Microsoft 톤을 덮어쓰지 말 것.
