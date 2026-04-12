# Insane Design

> URL 하나 → 실제 CSS 기반 design.md + 인터랙티브 HTML 리포트

웹사이트 URL을 입력하면 실제 서빙 중인 CSS를 분석해서 디자인 시스템 레퍼런스 문서와 인터랙티브 리포트를 자동 생성합니다.

## 사용법

```
/insane-design https://stripe.com
```

또는 자연어로:
```
이 사이트 디자인 분석해줘 https://linear.app
```

## 결과물

| 파일 | 용도 |
|------|------|
| `design.md` | AI 코딩 에이전트에 첨부 → "이 스타일로 만들어줘" |
| `report.ko.html` | 브라우저에서 열어보는 인터랙티브 디자인 리포트 |
| `screenshots/hero-cropped.png` | 실제 사이트 스크린샷 (1280×800) |

## 분석 범위

- 색상 토큰 (brand ramp, neutral, accent, semantic)
- 타이포그래피 스케일 (heading/text sizes, weights, line-height, letter-spacing)
- 스페이싱 토큰
- 라디우스 / 섀도우 시스템
- 폰트 스택 (커스텀 폰트 식별 + fallback chain)
- BEM 컴포넌트 클래스
- Quick Start 치트시트 ("3가지만 하면 80%")
- Drop-in CSS + Tailwind Config

## 검증 이력

35개 서비스(Stripe, GitHub, Linear, Notion, Discord, Vercel 등)에서 검증된 파이프라인.

## 의존성

- Python 3.11+
- PIL/Pillow (`pip install Pillow`) — 스크린샷 crop용
- curl — 기본 데이터 수집
