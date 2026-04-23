---
schema_version: 3.1
slug: krafton
service_name: Krafton
site_url: https://www.krafton.com/
fetched_at: 2026-04-23
default_theme: light
brand_color: "#E84847"
primary_font: KRAFTON
font_weight_normal: 400
token_prefix: --wp--preset--color--

bold_direction: "Dark Gaming Corporate"
aesthetic_category: "Gaming/Entertainment"
signature_element: fluid_vw_layout
code_complexity: low

medium: web
medium_confidence: high
---

# DESIGN.md — Krafton (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere

Krafton 웹사이트는 **"게임 회사의 기업 사이트"**다. 화려한 게임 비주얼을 배경으로 기업 정보를 깔끔하게 정리한다. 배경은 기본 흰색(`#fff`)이지만, 히어로 섹션은 풀스크린 비디오/이미지로 덮는다.

색상 전략은 극도로 절제되어 있다. **레드 `#E84847` 한 점**이 전체 브랜드 포인트 역할을 한다. 나머지는 `#000 → #555555 → #777777 → #ddd → #fff`의 5단계 무채색이 모든 것을 처리한다. 링크에만 `#3D7FD9` 블루가 등장한다.

타이포그래피는 **독점 서체 `KRAFTON` + 글로벌 다국어 폰트 시스템**이다. 영문 헤딩에는 KRAFTON 폰트, 본문과 한국어에는 Noto Sans / Noto Sans KR, 영문 대체로 Poppins를 사용한다.

레이아웃은 **vw 기반 유동형**이다. 고정 px 대신 `0 2.607vw`, `0 6.25vw` 등 뷰포트 비율로 여백을 제어한다. 화면 크기에 따라 선형으로 스케일된다.

### Key Characteristics

- 레드 `#E84847` — 브랜드 accent 단일 포인트
- 흰색 배경 위 다크 콘텐츠, 히어로는 풀스크린 비디오
- 독점 KRAFTON 폰트 — 헤딩 전용
- vw 기반 유동 레이아웃 — 고정 그리드 없음
- WordPress 기반 — WP preset color 토큰 사용

---

## 01. Quick Start
<!-- SOURCE: css -->

> 5분 안에 Krafton처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 기본 타이포그래피 */
body {
  font-family: "Noto Sans", "Noto Sans KR", Dotum, Helvetica, sans-serif;
  font-size: 14px;
  line-height: 1.7;
  color: #555555;
  background: #fff;
}

/* 2. KRAFTON 브랜드 폰트 헤딩 */
h1, h2, h3 {
  font-family: "KRAFTON", "Noto Sans", sans-serif;
  font-weight: 400;
  color: #000;
}

/* 3. 레드 accent */
.brand-red { color: #E84847; }
.btn-primary {
  background: #E84847;
  color: #fff;
  border-radius: 10px;
  padding: 12px 32px;
}
```

---

## 02. Provenance
<!-- SOURCE: auto -->

| 항목 | 값 |
|------|-----|
| Source URL | `https://www.krafton.com/` |
| CSS 파일 | `krafton/style.css`, `krafton/assets/css/fonts.css`, `krafton/assets/css/lang-ko.css` |
| CSS 바이트 | ~22,004 chars total |
| 수집일 | 2026-04-23 |
| 수집 방법 | curl_cffi (chrome impersonation) |

---

## 03. Tech Stack
<!-- SOURCE: html -->

| 항목 | 감지 값 |
|------|---------|
| CMS | WordPress |
| CSS 방식 | WordPress preset CSS variables + hardcoded values |
| 토큰 네임스페이스 | `--wp--preset--color--*`, `--wp--preset--gradient--*` |
| 레이아웃 | vw 기반 유동형 |

---

## 04. Font Stack
<!-- SOURCE: css -->

| 역할 | 폰트 | 폴백 |
|------|------|------|
| Brand Heading | `KRAFTON` | `Noto Sans`, sans-serif |
| Body / Korean | `Noto Sans`, `Noto Sans KR` | Dotum, 돋움, Helvetica, `Apple SD Gothic Neo`, sans-serif |
| English Alt | `Poppins` | sans-serif |
| Chinese | `Noto Sans SC` | sans-serif |
| Japanese | `Noto Sans JP` | sans-serif |

```css
h1, h2, h3 {
  font-family: "KRAFTON", "Noto Sans", sans-serif;
}
body {
  font-family: "Noto Sans", "Noto Sans KR", Dotum, 돋움, Helvetica, "Apple SD Gothic Neo", sans-serif;
}
```

---

## 05. Typography Scale
<!-- SOURCE: css -->

| 레벨 | Size | Line Height | 용도 |
|------|------|-------------|------|
| Base | 14px | 1.7 | 본문 |
| Small | 0.75em | — | sup / sub |
| Default | 1em | — | 인풋, 버튼 |

타이포그래피 스케일은 minimal하다. 대부분의 크기는 vw 또는 em으로 유동 처리된다.

---

## 06. Colors
<!-- SOURCE: css -->

### Brand (Theme CSS)

| 이름 | 값 | 용도 |
|------|-----|------|
| brand-red | `#E84847` | 브랜드 레드 — 강조 텍스트, CTA |
| brand-blue | `#3D7FD9` | 링크 색상 |

### Neutral

| 이름 | 값 | 용도 |
|------|-----|------|
| black | `#000000` | 다크 섹션 배경, 헤딩 |
| text-body | `#555555` | 본문 텍스트 |
| text-muted | `#777777` | 보조 텍스트 |
| border | `#dddddd` | 구분선, 테두리 |
| white | `#ffffff` | 기본 배경 |

### WordPress Preset Colors

| 토큰 | 값 |
|------|-----|
| `--wp--preset--color--black` | `#000000` |
| `--wp--preset--color--white` | `#FFF` |
| `--wp--preset--color--cyan-bluish-gray` | `#abb8c3` |
| `--wp--preset--color--dark-gray` | `#111` |
| `--wp--preset--color--light-gray` | `#767676` |
| `--wp--preset--color--primary` | `#0073a8` |
| `--wp--preset--color--secondary` | `#005075` |
| `--wp--preset--color--vivid-red` | `#cf2e2e` |
| `--wp--preset--color--luminous-vivid-orange` | `#ff6900` |
| `--wp--preset--color--luminous-vivid-amber` | `#fcb900` |
| `--wp--preset--color--vivid-green-cyan` | `#00d084` |
| `--wp--preset--color--pale-cyan-blue` | `#8ed1fc` |
| `--wp--preset--color--vivid-cyan-blue` | `#0693e3` |
| `--wp--preset--color--vivid-purple` | `#9b51e0` |

---

## 07. Spacing
<!-- SOURCE: css -->

Krafton은 고정 spacing 토큰이 없다. vw 기반 유동형 패딩을 사용한다.

| 패턴 | 값 | 용도 |
|------|-----|------|
| 컨텐츠 사이드 여백 (소) | `0 2.607vw` | 모바일 근접 |
| 컨텐츠 사이드 여백 (중) | `0 4.11458vw` | 태블릿 |
| 컨텐츠 사이드 여백 (대) | `0 6.25vw` | 데스크탑 |
| 히어로 패딩 탑 | `220px` | 데스크탑 header 오프셋 |
| 히어로 패딩 탑 (반응형) | `16.923vw` | 태블릿 이하 |
| 공통 여백 | `40px` | 섹션 내부 |

---

## 08. Border Radius
<!-- SOURCE: css -->

| 값 | 용도 |
|-----|------|
| `0` | 카드, 이미지, 기본 요소 |
| `10px` | 버튼, 강조 요소 |

---

## 09. Shadows
<!-- SOURCE: css -->

Krafton theme CSS에는 box-shadow 토큰이 없다. 풀스크린 비디오 위 텍스트 가독성은 gradient overlay로 처리한다.

---

## 10. Animation
<!-- SOURCE: css -->

CSS 테마에 명시적 transition 토큰 없음. 기본 브라우저 전환 사용.

---

## 11. Grid / Layout
<!-- SOURCE: css -->

- Full-viewport hero (100vw × 100vh) — 비디오/이미지 배경
- vw 기반 유동 레이아웃 — 고정 컬럼 그리드 없음
- 반응형 breakpoints: 1300px, 1024px, 767px

---

## 12. Components
<!-- SOURCE: css -->

**버튼**
- 기본 radius: `10px`
- 레드 배경 CTA: `background: #E84847`

**@font-face 목록**
- KRAFTON — woff (weight 400, 헤딩 전용)
- Noto Sans KR — woff2 + woff + otf (300/400/500/700)
- Noto Sans SC — woff2 + otf (300/400/500/700)
- Noto Sans JP — woff2 + otf (400/500/700)
- Poppins — woff2 + woff (multiple weights)

---

## 13. Dark/Light Mode
<!-- SOURCE: manual -->

Krafton은 **라이트 모드** 기본 사이트다. 히어로와 일부 섹션은 풀스크린 이미지/비디오로 다크하게 처리되지만, CSS 레벨 다크 모드 토글은 없다.

---

## 14. Drop-in CSS
<!-- SOURCE: css -->

```css
/* Krafton Design System — insane-design */
:root {
  /* Brand */
  --krafton-red: #E84847;
  --krafton-blue: #3D7FD9;

  /* Neutral */
  --krafton-black: #000000;
  --krafton-text: #555555;
  --krafton-muted: #777777;
  --krafton-border: #dddddd;
  --krafton-white: #ffffff;

  /* WordPress Preset */
  --wp--preset--color--black: #000000;
  --wp--preset--color--white: #FFF;
  --wp--preset--color--cyan-bluish-gray: #abb8c3;
  --wp--preset--color--dark-gray: #111;
  --wp--preset--color--light-gray: #767676;
  --wp--preset--color--primary: #0073a8;
  --wp--preset--color--secondary: #005075;
  --wp--preset--color--vivid-red: #cf2e2e;
  --wp--preset--color--luminous-vivid-orange: #ff6900;
  --wp--preset--color--luminous-vivid-amber: #fcb900;
  --wp--preset--color--vivid-cyan-blue: #0693e3;
  --wp--preset--color--vivid-purple: #9b51e0;

  /* Typography */
  --krafton-font-brand: "KRAFTON", "Noto Sans", sans-serif;
  --krafton-font-body: "Noto Sans", "Noto Sans KR", Dotum, 돋움, Helvetica, "Apple SD Gothic Neo", sans-serif;
  --krafton-font-size-base: 14px;
  --krafton-line-height: 1.7;

  /* Radius */
  --krafton-radius-sm: 0;
  --krafton-radius-md: 10px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: css -->

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        krafton: {
          red: '#E84847',
          blue: '#3D7FD9',
          black: '#000000',
          text: '#555555',
          muted: '#777777',
          border: '#dddddd',
          white: '#ffffff',
        },
      },
      fontFamily: {
        krafton: ['"KRAFTON"', '"Noto Sans"', 'sans-serif'],
        body: ['"Noto Sans"', '"Noto Sans KR"', 'Dotum', '돋움', 'Helvetica', '"Apple SD Gothic Neo"', 'sans-serif'],
      },
      borderRadius: {
        brand: '10px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

**이 사이트에서 가장 흔한 실수 하나:**

> **DON'T**: KRAFTON 폰트를 본문에 사용하는 것.
>
> KRAFTON 폰트는 weight 400 단 하나만 있고 한국어를 포함하지 않는다. 본문에 쓰면 한글이 깨진다.
>
> **DO**: KRAFTON 폰트는 헤딩과 영문 로고타입에만. 본문 전체는 Noto Sans / Noto Sans KR 스택. 빨간 포인트는 `#E84847` 하나만 — 배경색으로 쓰지 않는다.
