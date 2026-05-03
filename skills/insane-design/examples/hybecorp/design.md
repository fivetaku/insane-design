---
schema_version: 3.2
slug: hybecorp
service_name: HYBE
site_url: https://hybecorp.com
fetched_at: 2026-05-03T15:36:13+09:00
default_theme: mixed
brand_color: "#10182F"
primary_font: "Big Hit 201110"
font_weight_normal: 400
token_prefix: "none"

bold_direction: "Monochrome Stage"
aesthetic_category: "editorial-product"
signature_element: "hero_impact"
code_complexity: medium

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS token layer is thin, but navigation, full-screen hero, pagination, mobile drawer, cookie, and corporate subpage components are consistently implemented."

colors:
  primary: "#10182F"
  ink: "#111111"
  paper: "#FFFFFF"
  stage-black: "#000000"
  signal-lime: "#F5FF00"
  muted-line: "#E6E6E6"
  swiper-blue: "#007AFF"

typography:
  display: "Big Hit 201110"
  body: "Noto Sans KR"
  japanese: "Noto Sans JP"
  base:
    html_font_size: "62.5%"
    body_weight: 400
    global_tracking: "-0.01em"
  ladder:
    - { token: nav-large, size: "2.8rem", weight: 700, line_height: "1.07", tracking: "-0.04rem" }
    - { token: nav-mobile, size: "2.8rem", weight: 700, line_height: "4.8rem", tracking: "normal" }
    - { token: menu-link, size: "1.8rem", weight: 400, line_height: "2.06", tracking: "-0.026rem" }
    - { token: ci-title, size: "50px", weight: 500, line_height: "1.44", tracking: "-1.5px" }
    - { token: footer-copy, size: "1.1rem", weight: 400, line_height: "2rem", tracking: "-0.01em" }
  weights_used: [100, 200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  header-fixed: { height: "8rem", bg: "rgba(255,255,255,0.8)", z_index: 9999, transition: "all 0.3s ease-out" }
  hero-stage: { width: "100vw", height: "100vh", bg: "#000000", media_padding: "80px 0" }
  nav-mega-link: { color: "#111111", opacity: ".3", font: "Big Hit 201110 700 2.8rem" }
  nav-dropdown-link: { color: "#FFFFFF", font_size: "1.8rem", underline: "1px hover grow" }
  progress-pagination: { width: "calc(100% - 432px)", height: "2px", active_transition: "5s cubic-bezier(1,1.025,0,0.02)" }
  play-button: { size: "100px", radius: "100px", border: "2px solid #FFFFFF" }
  mobile-drawer: { width: "86.111%", bg: "#111111", transition: "all 0.3s ease-out" }
  cookie-bar: { bg: "#FFFFFF", padding: "34px 40px", button_radius: "45px" }
---

# DESIGN.md - HYBE (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

HYBE의 웹사이트는 기업 소개 페이지라기보다 영상 무대의 프레임에 가깝다. 첫 화면은 정보보다 화면비와 긴장감을 먼저 세운다. 상단 80px 고정 헤더, 좌우 30px 지점의 흰 세로선, 중앙을 가로지르는 2px 슬라이드 진행선이 영상 위에 얇게 얹히면서, 사이트 전체가 "콘텐츠를 재생하는 기업"처럼 보인다.

이 화면은 자정의 공연장에 켜진 안전 조명처럼 움직인다. 영상은 무대이고, UI는 공연을 방해하지 않는 얇은 장비선이다. 좌우 흰 레일은 포스터를 장식하는 border가 아니라 무대 양끝을 표시하는 마킹 테이프처럼 보인다. 중앙 2px 진행선은 뉴스 사이트의 progress bar가 아니라, 조명 콘솔에서 다음 큐를 기다리는 타임코드에 가깝다.

팔레트는 넓지 않다. 실제 CSS에서 가장 많이 반복되는 색은 #111111 (`{colors.ink}`), #FFFFFF (`{colors.paper}`), #000000 (`{colors.stage-black}`)이고, 채도 높은 색은 메뉴 오픈/언어 활성 상태의 #F5FF00 (`{colors.signal-lime}`) 정도다. `--primary`로 #10182F (`{colors.primary}`)가 존재하지만 화면을 지배하는 브랜드 톤은 짙은 네이비보다 거의 흑백에 가까운 무대 대비다. no second brand color: HYBE다움은 색을 늘리는 데서 오지 않고, 영상과 흰 선, 검은 내비게이션 레이어, 그리고 매우 제한적인 형광 라임 포커스에서 온다.

타이포그래피는 커스텀 디스플레이 폰트 `Big Hit 201110`과 본문용 `Noto Sans KR`의 이중 구조다. 내비게이션은 `Big Hit 201110` 700으로 각지고 넓게 서고, 본문과 쿠키/서브 UI는 Noto 계열이 실무적인 가독성을 맡는다. 전역 `letter-spacing: -0.01em`이 깔려 있어 모든 텍스트가 약간 조여진다. 특히 GNB의 `letter-spacing: -0.04rem`은 공연장 후면의 장비 라벨처럼 압축되어 있고, opacity `.3` 상태에서는 아직 켜지지 않은 채널명처럼 뒤로 물러난다.

공간은 카드형으로 쪼개지지 않는다. 첫 화면은 100vw x 100vh를 꽉 쓰고, 콘텐츠는 이미지와 비디오의 면으로 먼저 들어온다. 텍스트나 버튼은 그 위에 떠 있는 얇은 컨트롤이다. HYBE 페이지에는 사이트라는 자의식이 거의 없다. 페이지는 자기 존재를 지우고, 아티스트 영상이 스크린 전체를 차지하도록 비켜선다.

shadow, gradient, blur로 분위기를 꾸미지 않고 영상 자체의 콘트라스트를 믿는다. 쿠키 배너와 서브페이지 UI가 잠깐 흰 사무실 조명으로 돌아오더라도, 첫 인상은 검은 박스 시어터다. chrome에는 그림자가 없고, 드라마는 media에만 있다. 그래서 재현의 핵심은 장식 추가가 아니라 장식 제거다.

비유로 다시 정리하면, hybecorp.com은 회사 소개 책자가 아니라 **박물관 무대 + 갤러리 진열장 + 아티스트 쇼룸**을 한 화면에 묶은 큐레이션이다. 흰 좌우 레일은 진열장의 유리 모서리, 80px 헤더는 박물관 전시실 입구의 안내판, 100px 원형 play 버튼은 갤러리 한가운데에 놓인 단 하나의 작품 캡션이다. 풀스크린 영상은 무대 위 라이브 공연이고, 다크 드로어는 무대 뒤편의 카탈로그 서랍처럼 슬라이드된다. 형광 라임은 전시 안내 라벨에 켜진 LED — "지금 이 부스가 활성"이라는 신호. 모든 UI 요소가 제품사진/영상이라는 전시 객체를 받쳐주는 진열대 구조물로만 존재한다.

### Key Characteristics

- Full-viewport video/image stage: `.hybe_main .swiper-slide`가 `100vw` x `100vh`를 차지한다.
- Fixed corporate header: 상단 8rem 헤더가 무대 위에 항상 고정된다.
- Monochrome operating layer: #111111, #FFFFFF, #000000이 UI 대부분을 구성한다.
- Thin frame geometry: 좌우 2px white rails와 중앙 2px pagination line이 화면을 절단한다.
- Custom nav typography: `Big Hit 201110` 700, uppercase, compressed tracking.
- Single chromatic signal: #F5FF00은 모바일 오픈/언어 활성/hover에만 강하게 쓰인다.
- Long-timed progress: active pagination bar가 5s cubic-bezier로 채워진다.
- Circular video affordance: 100px play button, 2px white stroke, centered transform.
- Component chrome is flat: 버튼, drawer, footer는 shadow 없이 border와 fill로만 구분한다.
- Corporate content stays secondary: 회사/IR/뉴스/커리어 구조는 내비게이션 레이어 안에서 정돈된다.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Stage
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **full-screen artist video framed by fixed black-and-white corporate navigation and a thin timed progress line**으로 기억된다.
> **Code Complexity**: medium — token layer is small, but responsive header states, video hero, Swiper pagination, drawer navigation, and cookie UI require coordinated CSS states.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 HYBE처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
html,
body {
  font-family: "Noto Sans KR", "Big Hit 201110", sans-serif;
  font-size: 62.5%;
  font-weight: 400;
  letter-spacing: -0.01em;
}

/* 2. 무대 배경 + 흰 UI 레일 */
.hero-stage {
  width: 100vw;
  height: 100vh;
  background: #000000;
  color: #FFFFFF;
  position: relative;
}

/* 3. 내비게이션은 커스텀 디스플레이 폰트 */
.gnb-link {
  font-family: "Big Hit 201110", sans-serif;
  font-size: 2.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.04rem;
}
```

**절대 하지 말아야 할 것 하나**: HYBE를 K-pop 사이트라고 해서 보라/핑크 gradient나 팬덤형 장식을 얹지 말 것. 실제 화면은 #000000 무대, #FFFFFF 선, #111111 기업 내비게이션의 절제된 흑백 시스템이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://hybecorp.com` |
| Fetched | 2026-05-03T15:36:13+09:00 |
| Extractor | phase1 재사용: saved HTML/CSS/tokens/screenshot |
| HTML size | 20478 bytes |
| CSS files | 5 files, 243395 bytes total |
| Token prefix | `none` |
| Method | saved CSS custom properties, selector roles, frequency candidates, typography JSON, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered corporate site, not a modern component bundle in the captured HTML.
- **Design system**: thin local CSS system, no broad token namespace. Only `--primary` and Swiper variables are explicit custom properties.
- **CSS architecture**:
  ```css
  core        (--primary, --swiper-*)       raw values only
  selectors   (.header, .hybe_main, .footer) component/state rules
  utilities   (.ver_w, .ver_m, lang/body)    responsive visibility and locale branches
  ```
- **Class naming**: BEM-like Korean corporate CSS, mostly `.header .nav .gnb`, `.hybe_main .swiper-slide`, `.section_box.ci`.
- **Default theme**: mixed. Home hero is dark/video-first; subpage and cookie surfaces are white.
- **Font loading**: CSS references local/custom family names: `Big Hit 201110`, `Noto Sans KR`, `Noto Sans JP`, `NotoSansCJKkr-R`.
- **Canonical anchor**: captured canonical points to `https://hybecorp.com/kor/main`; HTML language in capture is English and navigation paths use `/eng/...`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Big Hit 201110` - used heavily for logo-adjacent navigation, mobile drawer labels, footer copy, and branded headings.
- **Body font**: `Noto Sans KR` - default Korean body stack.
- **Japanese branch**: `Noto Sans JP` is applied through `body:lang(ja)` and locale-specific declarations.
- **Code font**: no product code font; normalize CSS keeps `monospace, monospace` for code elements.
- **Weight normal / bold**: `400` / `700`; captured CSS also uses 100, 200, 300, 500, 600, 800, 900 and `bold`.

```css
html,
body {
  font-family: "Noto Sans KR", "Big Hit 201110", sans-serif;
  font-size: 62.5%;
  font-weight: normal;
}

body:lang(ja) {
  font-family: "Noto Sans JP", "Big Hit 201110", sans-serif !important;
}

.header .nav .gnb > li > a {
  font-family: "Big Hit 201110";
  font-size: 2.8rem;
  font-weight: 700;
  letter-spacing: -0.04rem;
  line-height: 1.07;
}
```

### Note on Font Substitutes

If `Big Hit 201110` is unavailable, use a square, techno-grotesque display face only for navigation and logo-like headings. Do not replace the whole site with Inter. A practical substitute stack is `"Big Hit 201110", "Arial Black", "Helvetica Neue Condensed Bold", sans-serif` for display, while body remains `"Noto Sans KR", system-ui, sans-serif`. The substitute must preserve uppercase width, compact counters, and strong 700-weight nav presence.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. Keep the global text slightly tight: `letter-spacing: -0.01em` is part of the site texture.
2. Reserve `Big Hit 201110` for brand/navigation moments, not long paragraphs.
3. Use uppercase navigation as structural signage, not as decorative labels everywhere.
4. Let video/image carry emotion; type should behave like control-room labels.
5. Use 500/700 weights for corporate titles and nav; avoid soft 300-only editorial styling.
6. Preserve locale branches: Korean and Japanese font stacks are separate, not interchangeable.

### Scale Notes

- **GNB desktop**: `2.8rem`, weight 700, line-height 1.07, uppercase, opacity `.3` until active.
- **GNB compact override**: `2rem`, line-height 1.5 in narrower rules.
- **Dropdown links**: `1.8rem`, line-height 2.06, white text over #111111 nav background.
- **Mobile drawer main links**: `2.8rem`, line-height `4.8rem`, weight 700.
- **CI/subpage large title**: `50px`, weight 500, line-height 1.44, tracking `-1.5px`.
- **Footer copy**: `1.1rem`, line-height `2rem`, `Big Hit 201110`.
- **Cookie text**: `14px`, line-height 1.5714, `NotoSansCJKkr-R`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Token Inventory

```css
:root {
  --primary: #10182F;
  --swiper-theme-color: #007AFF;
  --swiper-navigation-size: 44px;
  --swiper-navigation-color: #000000;
  --swiper-pagination-color: #000000;
  --swiper-preloader-color: #000000;
}
```

### Core Palette

- **Ink**: #111111 - most frequent UI text, nav backgrounds, borders, drawer background.
- **Paper**: #FFFFFF - menu links, hero rails, active progress, cookie surface, button reversals.
- **Stage black**: #000000 - hero slide background, cookie primary buttons, selected Swiper black variant.
- **Signal lime**: #F5FF00 - language active state, mobile menu open hamburger, hover underline.
- **Primary token**: #10182F - exists as `--primary`, used by cookie text via `color: var(--primary)`.
- **Muted line**: #E6E6E6 - frequent neutral divider/support color.
- **Swiper blue**: #007AFF - library default token, not HYBE brand identity.

### Contrast Behavior

HYBE does not use a multi-brand entertainment palette in the chrome. The page keeps UI colors neutral and lets artist imagery supply warmth, skin tones, light leaks, and album graphics. In implementation, any vivid color beyond #F5FF00 should be treated as content media, not as UI token.

### 06-8. Color Stories

- **#111111 Story**: The corporate operating layer. It appears in nav backgrounds, text, borders, drawer panels, and hover reversals, making the site feel institutional rather than fan-decorated.
- **#FFFFFF Story**: The stage instrument color. It draws rails, play borders, menu text, pagination fills, and cookie backgrounds, always clean and flat.
- **#000000 Story**: The video void. It sits behind full-screen slides and primary cookie buttons, allowing media to take over without visible page chrome.
- **#F5FF00 Story**: The only electric accent. It is not a general brand wash; it marks active language/menu states and mobile open controls.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

### Whitespace Philosophy

HYBE uses whitespace less like SaaS padding and more like a stage frame. The first viewport is not a centered content stack; it is a full-bleed media plane held in place by fixed 30px side rails and an 80px header/vertical safety area. The result is dense at the edges and open in the center.

- Header height: `8rem`.
- Header logo position: top `3rem`, left `3rem`.
- Hero video padding: `80px 0`, matching the fixed header band.
- Hero side rails: left/right `30px`, width `2px`, height `calc(100vh - 160px)`.
- Pagination width: `calc(100% - 432px)`, centered both horizontally and vertically.
- Footer padding: `3rem`; footer right nav anchored at `right: 30px`.
- Cookie bar padding: `34px 40px`, with `40px` gap between message and actions.
- Mobile drawer width: `86.111%`, padded `6rem 2rem 7.7rem`.

Spacing should feel measured, not plush. Avoid large card gutters, pill clusters, or stacked marketing sections on the first viewport.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

HYBE is mostly square and flat. Radius appears only where the control is physically circular or pill-like.

- **Play button**: `100px` square with `border-radius: 100px`; this is a true circle.
- **Cookie buttons**: `border-radius: 45px`; service utility, not a brand-wide pill system.
- **Cookie modal buttons**: `border-radius: 30px`.
- **Switch toggle**: `border-radius: 12px`; toggle knob is `100%`.
- **Selectric/dropdown/footer chrome**: `border-radius: 0`.
- **Main surfaces/cards**: no general rounded-card language.

Do not infer a soft rounded design system from the cookie banner. The core site is rectilinear.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

There is no meaningful shadow system in the captured core HYBE page. Depth comes from media contrast, fixed overlays, opacity, and black/white reversal. If a reproduction needs elevation, use stacking and solid fills first.

- Header uses `background-color: rgba(255,255,255,0.8)` and fixed positioning, not drop shadow.
- Nav drawer uses #111111 plus overlay behavior, not shadow.
- Hero controls are white strokes on media, not raised buttons.
- Cookie UI separates by fixed bottom placement and white fill.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is simple but important.

- Header and nav background: `transition: all 0.3s ease-out 0s`.
- Menu underline: width grows from `0` to `100%` over `0.3s ease-out`.
- Mobile drawer: right panel slides from `right: -100%` with `0.3s ease-out`.
- Cookie close: `transform: translateY(100%)` with `transition: transform 0.3s`.
- Hero progress active bar: `transition: all 5s cubic-bezier(1, 1.025, 0, 0.02)`.

The motion vocabulary is not bouncy. It is timed, direct, and control-like.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Full-Screen Stage

The home layout is a Swiper-driven full-screen stage. Each slide is `100vw` x `100vh`, black-backed, and media-first. The play affordance is centered with `transform: translate(-50%, -50%)`.

### Fixed Corporate Header

The header is always present and sits at the top with high z-index. Logo left, GNB centered, language right. On white/header variants it can invert logo/control colors, but its geometry stays fixed.

### Mega Navigation Overlay

Desktop GNB top-level labels are low-opacity until active. Dropdown links sit on #111111 with white text and underline-on-hover. This gives the menu a backstage/control-panel feel rather than a standard white dropdown.

### Mobile Drawer

At max-width 1024px, desktop nav hides and the drawer panel occupies `86.111%` width from the right. The drawer is #111111, links are white, and active language/menu cues use #F5FF00.

### Corporate Subpage Stack

Subpages such as CI/career sections move into conventional corporate layout: large title blocks, white backgrounds, black borders, and rectangular outline buttons. They share the same monochrome grammar but lose the full-viewport hero drama.

### Cookie Utility Layer

The cookie banner is a fixed bottom white utility band with text, underline links, outlined buttons, and black primary action. It is functionally separate from the editorial hero and should not drive the main visual language.

---

## 12. Responsive
<!-- SOURCE: auto+manual -->

- `max-width: 1024px` switches `.ver_w` off and activates mobile navigation patterns.
- Mobile header height becomes `6rem`; hamburger button is `6rem` square.
- Mobile drawer width is `86.111%`, with full viewport height and internal scroll.
- Desktop nav is typographic and horizontal; mobile nav becomes a stacked list with `2.8rem` main labels.
- Mobile open state changes hamburger bars to #F5FF00 and rotates them into a close icon.
- Cookie/modal UI includes viewport-width sizing at smaller widths; the captured CSS uses `vw` in cookie modal media rules.

Responsive behavior prioritizes control access over reflowing content cards. The hero remains media-dominant.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Component Inventory

- **Header**: fixed top, 8rem height, logo left, centered GNB, language switch right.
- **Logo link**: text hidden with SVG background; desktop logo width `11rem`, height `2.2rem`.
- **Desktop GNB**: uppercase `Big Hit 201110`, opacity states, dropdown menu.
- **Dropdown menu links**: white text, 1px underline growth on hover.
- **Mobile hamburger**: two-line icon, transforms into close state, #F5FF00 open color.
- **Mobile drawer**: #111111 right panel, scrollable full-height navigation.
- **Hero slide**: full viewport media container with black background.
- **Hero rails**: left/right 2px white lines from `top: 80px` to bottom safety band.
- **Progress pagination**: 2px center line with timed active fill.
- **Play button**: 100px circular white stroke with centered play asset.
- **Footer**: flex footer, small copy, right-side FNB/select controls.
- **Corporate outline button**: 185px x 60px or 186px x 52px, 1px black border, reversible hover.
- **Cookie bar**: fixed bottom service message with outline/filled pill buttons.

### 13-2. Named Variants

- **`header-fixed-light`**: `height: 8rem`, `background-color: rgba(255,255,255,0.8)`, high z-index, `transition: all 0.3s ease-out`.
- **`header-c-white`**: white logo/control variant for media-backed hero state.
- **`gnb-link-muted`**: #111111 text, opacity `.3`, uppercase, `Big Hit 201110` 700.
- **`gnb-link-active`**: same geometry as muted, opacity `1`.
- **`dropdown-link-white`**: #FFFFFF, `1.8rem`, line-height 2.06, underline grows from 0 to 100%.
- **`drawer-black`**: fixed right panel, width `86.111%`, #111111 background, 0.3s slide.
- **`hero-stage-black`**: `100vw` x `100vh`, #000000 background, media layer z-index 1.
- **`progress-line-timed`**: center 2px pagination, white active fill, 5s cubic-bezier.
- **`play-circle-white`**: 100px circle, 2px #FFFFFF border, transparent center.
- **`outline-corporate-button`**: black 1px border, white fill; hover reverses to #111111/#FFFFFF or keeps white variant depending page context.
- **`cookie-primary-pill`**: #000000 background, #FFFFFF text, radius 45px or 30px depending banner/modal.

### 13-3. Signature Micro-Specs

```yaml
stage-rail-frame:
  description: "full-screen artist media를 공연장 무대처럼 고정하는 좌우 레일"
  technique: ".hybe_main::before/::after; width: 2px; background: #FFFFFF; left/right: 30px; top: 80px; height: calc(100vh - 160px)"
  applied_to: ["{component.hero-stage}", "{component.hero-rails}"]
  visual_signature: "영상 양끝에 흰 마킹 테이프가 서 있는 듯한 HYBE home의 가장 강한 비미디어 시그니처"

timed-centerline-pagination:
  description: "슬라이드 진행을 중앙 타임코드처럼 보이게 하는 2px progress line"
  technique: ".hybe_main .swiper-pagination; top: 50%; left: 50%; width: calc(100% - 432px); height: 2px; active .after_bar transition: all 5s cubic-bezier(1, 1.025, 0, 0.02)"
  applied_to: ["{component.progress-pagination}", "{component.hero-stage}"]
  visual_signature: "페이지 indicator가 아니라 공연 큐시트의 진행선처럼 화면 한가운데를 얇게 절단한다"

compressed-corporate-gnb:
  description: "기업 내비게이션을 로고 장비 라벨처럼 압축하는 display type 운용"
  technique: ".header .nav .gnb > li > a; font-family: Big Hit 201110; font-size: 2.8rem; font-weight: 700; line-height: 1.07; letter-spacing: -0.04rem; text-transform: uppercase; opacity: .3 until active"
  applied_to: ["{component.header-fixed}", "{component.nav-mega-link}"]
  visual_signature: "일반 SaaS nav가 아니라 검은 backstage wall 위의 굵고 낮게 켜진 채널명처럼 보인다"

electric-drawer-close:
  description: "모바일 open 상태를 유일한 chromatic signal로 표시하는 hamburger 변환"
  technique: ".header.open .btn_nav:before/after; color switch to #F5FF00 !important; two-line hamburger rotates into close mark; transition: all 0.3s ease-out"
  applied_to: ["{component.mobile-hamburger}", "{component.mobile-drawer}"]
  visual_signature: "흑백 시스템 안에서 형광 라임이 작은 경고등처럼 켜진다"

video-play-disc:
  description: "artist media 위에 놓이는 원형 재생 affordance"
  technique: "width: 100px; height: 100px; border: 2px solid #FFFFFF; border-radius: 100px; background: transparent; play image sized 98px 98px; transform: translate(-50%, -50%)"
  applied_to: ["{component.play-button}", "{component.hero-stage}"]
  visual_signature: "버튼이라기보다 검은 스크린 중앙에 얹힌 흰 조명 링처럼 읽힌다"
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

HYBE's visible copy is corporate and direct: COMPANY, INVESTORS, NEWSROOM, CAREERS, Company Info., Artist, Business, Ethical Management. The voice does not explain itself with playful microcopy. The home hero relies on artist/content titles and video imagery; navigation uses institutional labels.

Use short noun labels, uppercase section names, and minimal helper text. Avoid chatty UX writing, fan-community tone, or startup-style value propositions.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --hybe-primary: #10182F;
  --hybe-ink: #111111;
  --hybe-paper: #FFFFFF;
  --hybe-stage-black: #000000;
  --hybe-signal-lime: #F5FF00;
  --hybe-muted-line: #E6E6E6;
}

html,
body {
  margin: 0;
  font-family: "Noto Sans KR", "Big Hit 201110", sans-serif;
  font-size: 62.5%;
  font-weight: 400;
  color: var(--hybe-ink);
  background: var(--hybe-paper);
  letter-spacing: -0.01em;
}

.hybe-header {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  width: 100%;
  height: 8rem;
  background: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease-out 0s;
}

.hybe-gnb-link {
  display: block;
  font-family: "Big Hit 201110", sans-serif;
  font-size: 2.8rem;
  font-weight: 700;
  line-height: 1.07;
  letter-spacing: -0.04rem;
  text-transform: uppercase;
  color: var(--hybe-ink);
  opacity: .3;
}

.hybe-gnb-link.is-active {
  opacity: 1;
}

.hybe-stage {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: var(--hybe-stage-black);
  color: var(--hybe-paper);
}

.hybe-stage::before,
.hybe-stage::after {
  position: absolute;
  top: 80px;
  z-index: 10;
  display: block;
  width: 2px;
  height: calc(100vh - 160px);
  background: var(--hybe-paper);
  content: "";
}

.hybe-stage::before {
  left: 30px;
}

.hybe-stage::after {
  right: 30px;
}

.hybe-progress {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 20;
  width: calc(100% - 432px);
  height: 2px;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, .3);
}

.hybe-progress__bar {
  display: block;
  width: 100%;
  height: 2px;
  background: var(--hybe-paper);
  transition: all 5s cubic-bezier(1, 1.025, 0, 0.02);
}

.hybe-play {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 100;
  width: 100px;
  height: 100px;
  border: 2px solid var(--hybe-paper);
  border-radius: 100px;
  background: transparent;
  transform: translate(-50%, -50%);
}

.hybe-drawer {
  position: fixed;
  top: 0;
  right: -100%;
  z-index: 10001;
  width: 86.111%;
  height: 100vh;
  padding: 6rem 2rem 7.7rem;
  overflow-y: auto;
  background: var(--hybe-ink);
  transition: all 0.3s ease-out 0s;
}

.hybe-drawer.is-open {
  right: 0;
}

.hybe-drawer a {
  font-family: "Big Hit 201110", sans-serif;
  font-size: 2.8rem;
  font-weight: 700;
  line-height: 4.8rem;
  color: var(--hybe-paper);
}

.hybe-drawer .is-active {
  color: var(--hybe-signal-lime);
}
```

---

## 16. Tailwind
<!-- SOURCE: manual -->

HYBE's captured CSS is not Tailwind-generated. If translating into Tailwind, keep custom tokens rather than using default palette names as brand identity.

```js
export default {
  theme: {
    extend: {
      colors: {
        hybe: {
          primary: "#10182F",
          ink: "#111111",
          paper: "#FFFFFF",
          stage: "#000000",
          signal: "#F5FF00",
          line: "#E6E6E6"
        }
      },
      fontFamily: {
        display: ["Big Hit 201110", "Arial Black", "sans-serif"],
        body: ["Noto Sans KR", "system-ui", "sans-serif"]
      },
      letterSpacing: {
        hybe: "-0.01em",
        "hybe-nav": "-0.04rem"
      }
    }
  }
}
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a HYBE-inspired editorial corporate homepage. Use a full-viewport black media stage, fixed 8rem header, uppercase display navigation, thin white side rails, a centered 2px timed progress line, and a 100px circular white-stroked play control. The UI chrome must be almost entirely #111111, #FFFFFF, and #000000, with #F5FF00 used only for active language/menu or mobile open states. Use `Big Hit 201110` style display typography for navigation and `Noto Sans KR` style body typography. Avoid gradients, shadows, rounded cards, colorful fan visuals, and SaaS-like feature-card layouts. The first viewport should feel like a controlled video stage for an entertainment company, not a marketing landing page.

---

## 18. 🚫 What This Site Doesn't Use
<!-- SOURCE: auto+manual -->

- 배경을 전역 `#F8FAFC`나 `#F5F5F5`로 두지 말 것 — 홈 무대는 `#000000`, 일반 표면은 `#FFFFFF`를 사용.
- 본문/내비 텍스트를 순수 `#222222` 중심으로 완화하지 말 것 — 실제 핵심 잉크는 `#111111`.
- 브랜드 악센트를 보라 `#7C3AED`, 핑크 `#FF3B8A`, 파랑 `#007AFF`로 확장하지 말 것 — UI 악센트는 #F5FF00만 제한적으로 사용하고 #007AFF는 Swiper 기본값으로 취급.
- 영상 위 UI 선을 회색 `#E6E6E6`으로 낮추지 말 것 — hero rails와 active progress는 `#FFFFFF`.
- 헤더를 투명 glass/blur로 만들지 말 것 — captured header는 `rgba(255,255,255,0.8)` 또는 media-state white logo 변형, blur/shadow가 핵심이 아니다.
- GNB를 Inter 500, 16px 같은 SaaS 내비로 만들지 말 것 — `Big Hit 201110`, 700, `2.8rem`, uppercase 압축감이 필요하다.
- 카드 grid와 12px radius 컴포넌트로 첫 화면을 채우지 말 것 — home은 full-screen media stage이며 일반 radius 시스템이 없다.
- 버튼 shadow나 multi-layer elevation을 추가하지 말 것 — HYBE chrome은 border/fill/position으로 구분한다.
- 형광 #F5FF00을 배경 섹션이나 CTA 대면적으로 쓰지 말 것 — active language, hover underline, mobile open state처럼 작은 신호에만 사용.
- 쿠키 배너의 pill radius를 전체 디자인 규칙으로 확대하지 말 것 — cookie utility만 `45px`/`30px`이고 핵심 사이트는 rectilinear하다.

### 🚫 Negative-Space Identity

- Second brand color: **none** — 갤러리 진열장은 흑백 + 형광 라임 신호 단 하나로 운영된다.
- Brand gradient/glass blur chrome: **absent** — 무대 chrome에 gradient/blur 장식은 zero이고, 깊이는 영상 콘트라스트가 만든다.
- Card grid lifestyle hero: **never** — 첫 화면은 박물관 전시 무대 한 장이지 쇼룸 카드 컬렉션이 아니다.
- Box-shadow elevation system: **zero** — 진열장 모서리는 line/border/position만으로 분리된다.
- Fan-community pink/purple palette: **absent** — K-pop이라는 이유로 보라/핑크를 얹는 순간 박물관 전시 톤이 무너진다.
- SaaS-style 16px Inter nav: **never** — 전시실 입구의 안내판은 `Big Hit 201110` 700, 2.8rem, 압축감 그대로다.
- Pill radius as global rule: **absent** — 쿠키 utility만 예외이고 진열대 본체는 전부 직각이다.
- Multi-color decorative dots: **none** — chromatic signal은 #F5FF00 단 하나, 다른 신호등은 부재.

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Phase1 자료에 `scale` 객체가 비어 있어 전체 폰트 사이즈 래더는 CSS selector samples와 typography family/weight counts를 결합해 수동 해석했다.
- `--primary: #10182F`는 명시 토큰이지만 captured home visual에서는 #111111/#000000/#FFFFFF의 영향이 훨씬 크다. 따라서 `brand_color`는 토큰 값을 유지하되 direction은 monochrome stage로 판정했다.
- Screenshot은 `hero-cropped.png` 한 장을 기준으로 관찰했다. 슬라이드 16개 전체의 이미지 톤, 영상 썸네일, artist title 처리는 phase1 화면 밖일 수 있다.
- HTML capture는 canonical이 `/kor/main`이지만 문서 `lang="en"`과 `/eng/...` 내비게이션이 함께 보인다. 언어별 서체/카피 차이는 CSS와 captured nav만 기준으로 정리했다.
- CSS에는 cookie preference UI, Selectric, Swiper 등 외부/유틸리티 스타일이 섞여 있다. 브랜드 핵심 판정에서는 customer/logo-wall 오염과 라이브러리 기본값을 분리했다.
- `design_system_level`은 lv2로 판정했다. 명명된 디자인 토큰 체계는 얇지만, 실제 컴포넌트 상태와 반응형 패턴은 운영 가능한 수준으로 일관되어 있기 때문이다.
- Step 6 RENDER-HTML은 사용자 지시에 따라 생략했다. 이 문서는 `design.md` 산출물만을 대상으로 한다.
