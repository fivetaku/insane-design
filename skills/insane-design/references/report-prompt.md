# HTML 리포트 생성 프롬프트 (v2.1)

> Claude Code 에이전트가 `design.md` → `report.ko.html` 을 생성할 때 따르는 규칙.
> 골드 스탠다드: `examples/stripe/report.ko.html`
> v2.1 변경: Input Contract, Typography Normalization, Failure Policy, Batch Isolation, Anti-patterns, Color Brightness 추가

---

## 입출력

- **입력**: `insane-design/<slug>/design.md` (YAML frontmatter + 마크다운 섹션)
- **출력**: `insane-design/<slug>/report.ko.html` (자체 완결 한글 HTML)
- **참조**: `examples/stripe/report.ko.html` 의 HTML/CSS/JS 구조를 그대로 따른다

---

## 1. CSS 공유 원칙

모든 서비스가 **동일한 CSS**를 쓴다. 서비스마다 바뀌는 건 딱 하나:

```css
:root {
  --brand-color: {frontmatter 의 brand_color};  /* 이것만 서비스별로 다름 */
  /* 나머지 zinc palette, font 로딩, layout 전부 동일 */
}
```

Stripe report.ko.html 의 `<style>` 블록을 통째로 복사하고 `--brand-color` 값만 교체.

---

## 2. 섹션 매핑

| design.md 섹션 | HTML | TOC 그룹 | TOC 이름 | 필수 |
|---|---|---|---|---|
| §01 Quick Start | Hero 안 카드 | Overview | 한눈에 보기 | ✅ |
| §02 Provenance | 별도 섹션 | Overview | 출처와 수집 기준 | ✅ |
| §03 Tech Stack | 별도 섹션 | Overview | 테크 스택 | ✅ |
| §04 Font Stack | Typography 안 subsection | Foundations | 타이포그래피 | ✅ |
| §05 Typography Scale | Typography 안 subsection | (위와 합침) | | ✅ |
| §06 Colors | 별도 섹션 | Foundations | 컬러 | ✅ |
| §07 Spacing | 별도 섹션 | Tokens | 스페이싱 | ✅ |
| §08 Radius | 별도 섹션 | Tokens | 라디우스 | ✅ |
| §09 Shadows | 별도 섹션 | Tokens | 섀도우 | ⭕ optional |
| §10 Motion | 별도 섹션 | Tokens | 모션 | ⭕ optional |
| §11 Layout Patterns | 별도 섹션 | Patterns | 레이아웃 패턴 | ⭕ optional |
| §12 Components | 별도 섹션 | Patterns | 컴포넌트 | ✅ |
| §13 Content/Copy Voice | 별도 섹션 | Patterns | 라이팅 원칙 | ⭕ optional |
| §14 Drop-in CSS | Code Export 탭 | Code | CSS · Tailwind | ✅ |
| §15 Tailwind Config | Code Export 탭 | (위와 합침) | | ⭕ optional |
| §16 DO / DON'T | 별도 섹션 | Rules | Do / Don't | ✅ |

### 선택 섹션 처리
- design.md 에 해당 `## NN.` 이 없으면 → **HTML 섹션 AND TOC 항목 둘 다 제거**
- §15 Tailwind 없으면 → Code Export 에서 Tailwind 탭 제거, CSS 만
- §09 Shadows 없는 서비스도 있음 → 같은 처리

---

## 3. 사이드바 TOC — 6그룹

```
── Overview ──
  00  한눈에 보기
  01  출처와 수집 기준
  02  테크 스택

── Foundations ──
  03  타이포그래피
  04  컬러

── Tokens ──
  05  스페이싱
  06  라디우스
  07  섀도우
  08  모션            ← optional

── Patterns ──
  09  레이아웃 패턴   ← optional
  10  컴포넌트
  11  라이팅 원칙     ← optional

── Code ──
  12  CSS · Tailwind

── Rules ──
  13  Do / Don't
```

그룹 라벨: `.toc__group-label` (영어, uppercase, monospace)
항목 번호: `.toc__num` (monospace, 10px)

---

## 4. Hero 구성

순서 (위→아래):
1. **Eyebrow pill**: `Design System Report`
2. **h1**: `{service_name} — {system_name 또는 token_prefix}`
3. **sub**: design.md §01 아래 설명 문장 또는 한 줄 요약
4. **Screenshot** (있으면): `screenshots/hero-cropped.png` — 조건부
5. **Quick Start 카드**: 3칸 dark code cards + 빨간 경고 callout
6. **4-stat 카드**: Source / Fetched / System / 핵심 수치

### Screenshot 조건부 렌더링

스크린샷 파이프라인 (Phase 1 에서 처리):
```
Jina Reader API → jina-hero.png (1280×1280 원본)
                      │
                      └─ PIL crop(0, 0, 1280, 800) → hero-cropped.png (리포트용)
```

Phase 5 에서는 `hero-cropped.png` 이 존재하는지만 확인하고 삽입:
```html
<!-- screenshots/hero-cropped.png 파일이 존재하면 삽입 -->
<div class="hero__screenshot">
  <img src="screenshots/hero-cropped.png" alt="{service_name} — 실제 홈페이지 스크린샷">
</div>
```
파일이 없으면 이 div 자체를 생략. hero-cropped.png 를 직접 생성하거나 crop 하는 건 Phase 5 의 역할이 아님.

CSS:
```css
.hero__screenshot{
  margin-bottom:32px;max-width:880px;
  border-radius:var(--radius-lg);overflow:hidden;border:1px solid var(--border);
}
.hero__screenshot img{width:100%;height:auto;display:block;}
```

### Quick Start 3칸 분리
- design.md §01 의 CSS 코드 블록에서 `/* 1. */` `/* 2. */` `/* 3. */` 주석으로 3개 스텝 분리
- 각 스텝 → `.qs__step` dark card
- "절대 하지 말 것" → `.qs__warn` 빨간 callout
- 주석 구분 안 되면 전체를 1개 스텝에 넣어도 됨

---

## 5. Typography (§04 + §05 통합)

### Font Stack 카드 (§04)
`.fs-card` 안에 `.fs-card__row` 들:
- Display font + 라이선스
- Code font
- Weight normal / bold 값
- Fallback chain

### 타이포 라이브 프리뷰 (§05)

**핵심**: 테이블 컬럼 구조는 서비스마다 다름. **의미로 파악**해서 매핑.

각 행을 `.type-row` 로 렌더:
- 좌측 `.type-row__s`: **실제 inline style 적용** (`font-size`, `font-weight`, `line-height`, `letter-spacing`)
- 우측 `.type-row__spec`: 토큰명 + 스펙 텍스트

font-family 는 `"SF Pro Display", -apple-system, BlinkMacSystemFont, sans-serif`

**주의**:
- 테이블 헤더 행(`| Token | Size | ...`)은 데이터가 아님 → 렌더하지 말 것
- `"400 (3회)"` 같은 주석 포함 값 → 순수 숫자(400) 만 추출
- `.875rem` 같은 소수점 시작 → 앞점 유지
- Weight 컬럼이 없는 서비스 → 해당 서비스의 body weight(frontmatter `font_weight_normal`)를 기본값으로

---

## 6. Colors (§06)

design.md §06 의 서브섹션(06-1 ~ 06-7) 을 순서대로 렌더. 없는 서브섹션은 건너뜀.

### 컬러 램프 스와치
- 각 step → 실제 배경색 div
- 밝은 색 → `.sw--l` (어두운 텍스트), 어두운 색 → `.sw--d` (밝은 텍스트)
  - 판단 기준: hex 값의 밝기. 대략 #808080 이상이면 light
- anchor step(★) → `.is-anchor`
- step 수에 따라 grid columns 동적 조정

### Dominant Colors (§06-7)
- 있으면: `.dom-chart` 가로 누적 막대 + `.dom-list` 그리드
- 없으면: 생략

### Alias layer (§06-6)
- `.alias-table` 안에 `.row` 들 (key → value 매핑)

---

## 7. Spacing (§07)

- `.space-row` 들: 토큰명 | px 값 | **실제 폭 bar** (`width` 를 px 값으로 설정)
- 네이밍 규칙 callout 있으면 `.space-note` 로

---

## 8. Radius (§08)

- `.rad-card` 들: 실제 `border-radius` 가 적용된 `.rad-box` + 이름 + 값 + 용도
- step 수에 따라 grid columns 조정 (7개면 7열, 6개면 6열)

---

## 9. Shadows (§09)

- `.sh-card` 들: 실제 `box-shadow` CSS 적용된 카드
- level 이름 + 설명 + shadow 값

---

## 10. Components (§12)

각 컴포넌트 → `.cmp-block`:
- `.cmp-block__head`: 클래스명 + variant 설명
- `.cmp-demo`: 데모 영역 (가능하면 실제 스타일 적용된 버튼/링크 등)
- `.cmp-spec`: 스펙 상세 (monospace)
- `.cmp-code`: **HTML 마크업 코드 블록** + Copy 버튼

design.md 에 ```html 블록이 있으면 그대로 사용.

---

## 11. Code Export (§14 + §15)

- `.code-export` 컨테이너
- `.code-tabs`: "CSS 스니펫" | "Tailwind 설정" 탭 버튼 + "Copy" 버튼
- `.code-pane[data-pane="css"]`: §14 코드 블록
- `.code-pane[data-pane="tw"]`: §15 코드 블록 (없으면 탭 자체 제거)
- 탭 전환 + 클립보드 복사 JS 포함

---

## 12. Do / Don't (§16)

- `.dd-grid` 2열
- `.dd-card--do` (녹색 배지) + `.dd-card--dont` (빨간 배지)
- 교정표/Myth 테이블 있으면 `.myth-table` 렌더

---

## 13. 한글 톤 규칙

| 영역 | 처리 |
|---|---|
| CSS 속성·토큰명·클래스·hex | 영어 유지 |
| 섹션명 | 혼용 외래어 (스페이싱, 라디우스, 섀도우) |
| 본문 | 한국어, 과장 금지 |
| 첫 등장 용어 | 하이브리드: `라디우스(모서리 반경)` |
| Do / Don't | 영어 유지 |

### 섹션 타이틀 작성법
- 정보 서술형. 직역 금지.
- 각 서비스의 핵심 특징을 반영 (예: Stripe "본문 굵기는 300이다", Linear "Marketing vs App 이중 팔레트")
- ❌ "일곱 개의 모서리" → ✅ "라디우스 7단"
- ❌ "가짜 데이터의 함정" → ✅ "자주 틀리는 것들"
- ❌ "그림자는 쌍으로 온다" → ✅ "섀도우는 항상 두 겹"

---

## 14. JS (파일 하단)

Stripe report.ko.html 하단의 `<script>` 블록을 그대로 복사:
- Code Export 탭 전환
- `.copy[data-copy]` 버튼 → 클립보드 복사
- `[data-copy-active]` → 활성 탭 코드 복사

---

## 15. 반응형

Stripe 의 `@media (max-width:1024px)` 블록 그대로 복사:
- sidebar → 상단 고정 해제
- grid 2열 → 1열
- padding 축소

---

## 16. 소스 파일명

- **기존**: `DESIGN.claude.manual.md`
- **신규**: `design.md`
- 두 이름 다 지원. 폴더 안에 `design.md` 가 있으면 그것을, 없으면 `DESIGN.claude.manual.md` 를 읽는다.

---

## 17. Input Contract (v2.1 추가)

frontmatter 필드의 필수/선택/fallback:

| 필드 | 필수 | fallback (없을 때) |
|---|---|---|
| `slug` | ✅ | 폴더명 사용 |
| `service_name` | ✅ | slug 를 capitalize |
| `brand_color` | ✅ | `#18181b` (zinc-900) |
| `primary_font` | ✅ | `system-ui` |
| `site_url` | ✅ | `https://{slug}.com` |
| `fetched_at` | ⭕ | 파일 수정일 |
| `font_weight_normal` | ⭕ | `400` |
| `token_prefix` | ⭕ | 생략 (Hero 에서도 표시 안 함) |
| `default_theme` | ⭕ | `light` |

Hero 4-stat 카드 값 선정 기준:
- **Source**: `site_url` 에서 도메인만
- **Fetched**: `fetched_at`
- **System**: `token_prefix` 또는 디자인 시스템 이름 (없으면 "Custom")
- **4번째**: 해당 서비스의 가장 특징적인 수치 (body weight, 토큰 수, 브랜드 컬러 등 — design.md §01 의 핵심 포인트에서 선택)

---

## 18. Typography Normalization (v2.1 추가)

design.md 의 타이포 테이블은 서비스마다 컬럼 구조가 다름. 의미 기반으로 매핑:

### 컬럼 동의어 테이블

| 속성 | 동의어 (어느 것이든 매칭) |
|---|---|
| **size** | Size, rem, px, font-size, 크기 |
| **weight** | Weight, font-weight, bold, 굵기 |
| **line-height** | Line-height, lh, 줄높이, leading |
| **letter-spacing** | Letter-spacing, tracking, 자간, ls |
| **token** | Token, Class, Name, 토큰 |
| **usage** | Usage, Use, Context, 용도 |

### 매핑 우선순위
1. 테이블 헤더 행의 컬럼명을 위 동의어로 매칭
2. 매칭 안 되는 컬럼 → 해당 속성은 inline style 에서 생략
3. Weight 컬럼이 없으면 → frontmatter `font_weight_normal` 값을 기본값으로
4. 숫자 뒤 주석 처리: `"400 (3회)"` → 순수 숫자 `400` 만 추출 (첫 번째 숫자)
5. `.875rem` 같은 소수점 시작 → **앞점 반드시 유지**
6. 테이블 헤더 행 (`| Token | Size | ...`)과 구분자 행 (`|---|---|...`) 은 데이터가 아님 → 렌더하지 않음

---

## 19. Failure Policy (v2.1 추가)

| 상황 | 처리 |
|---|---|
| YAML frontmatter 파싱 실패 | 폴더명을 slug 로, 나머지 §17 의 fallback 적용 |
| 섹션 내용이 비어있거나 N/A 만 | 해당 섹션 건너뜀 (TOC 에서도 제거) |
| 코드블록 없음 (§14/§15) | Code Export 섹션 전체 생략 |
| hex 값 비표준 형식 | 문자열 그대로 표시 (변환 시도 안 함) |
| 컴포넌트 데모 재현 불가 | 코드 블록만 표시, 데모 영역은 muted placeholder |
| 스크린샷 파일 없음 | Hero screenshot div 전체 생략 |
| 테이블 파싱 불가 | 원문 마크다운 그대로 `<pre>` 블록에 삽입 |

**절대 금지**: design.md 에 없는 값을 **지어내지 말 것**. hex, 토큰명, font name, 스펙 수치 — 전부 design.md 에 적힌 것만 사용.

---

## 20. Batch Isolation (v2.1 추가)

한 에이전트가 여러 서비스를 연속 처리할 때:

1. **각 서비스는 독립적.** 이전 서비스의 값/구조를 다음 서비스에 carry-over 금지.
2. **TOC 번호 재계산**: optional 섹션 제거 후 빈 번호 없이 연속 번호 부여 (00, 01, 02, 03...).
3. **상태 리셋**: 각 서비스 생성 시작 전, 이전 서비스의 brand_color, font, theme 등을 완전히 잊고 새 frontmatter 에서만 읽는다.
4. **파일 격리**: 출력은 반드시 해당 서비스 폴더 안에만 (`insane-design/{slug}/report.ko.html`).

---

## 21. Anti-patterns (v2.1 추가)

생성 시 절대 하지 말 것:

| # | 안티패턴 | 올바른 처리 |
|---|---|---|
| 1 | design.md 에 없는 hex 값 / 토큰명 / 폰트명 지어내기 | design.md 에 적힌 것만 사용 |
| 2 | 다른 서비스의 값을 이 서비스에 복사 | 각 서비스는 자기 design.md 만 참조 |
| 3 | 마크다운 테이블 헤더 행을 데이터로 렌더 | `\| Token \| Size \|` 는 헤더 → 스킵 |
| 4 | font-weight 에 font-size px 값 넣기 | weight 와 size 컬럼 구분 (§18 참조) |
| 5 | `"400 (3회)"` → `4003` 으로 파싱 | 첫 번째 정수만 추출 → `400` |
| 6 | `.875rem` → `875rem` 앞점 탈락 | 소수점 유지 → `.875rem` |
| 7 | 섹션 타이틀 1:1 직역 ("일곱 개의 모서리") | 정보 서술형 ("라디우스 7단") |
| 8 | 과장 부사 ("충격적", "놀라운", "혁신적") | 사실 서술만 |
| 9 | Quick Start 3칸을 1칸으로 합치기 | `/* 1. */` `/* 2. */` `/* 3. */` 주석 기준 분리 |
| 10 | Stripe 의 데이터를 다른 서비스에 사용 | 절대 금지 — Stripe report 는 구조 참조만 |

---

## 22. Color Brightness (v2.1 추가)

스와치 텍스트 색상(`.sw--l` vs `.sw--d`) 결정 기준:

```
hex → RGB 변환 (0~255)
R' = R/255, G' = G/255, B' = B/255

각 채널 선형화:
  c ≤ 0.04045 → c/12.92
  c > 0.04045 → ((c + 0.055)/1.055)^2.4

상대 휘도 L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin

L > 0.179 → 밝은 배경 → 어두운 텍스트 (.sw--l)
L ≤ 0.179 → 어두운 배경 → 밝은 텍스트 (.sw--d)
```

> 간이 판단: hex 의 6자리 중 R+G+B 합이 384 (=128×3) 이상이면 `.sw--l`, 미만이면 `.sw--d`. 정확도는 WCAG 공식보다 떨어지지만 대부분 맞음.

---

## 체크리스트 (생성 후 자체 검증 — v2.1 강화)

### 필수 PASS (하나라도 실패하면 재생성)

- [ ] `<!doctype html>` 로 시작, `</html>` 로 끝남
- [ ] `--brand-color` 가 frontmatter 의 `brand_color` 와 일치
- [ ] TOC 6그룹 존재, 한글 라벨 정확
- [ ] Quick Start: dark card + 빨간 경고 존재
- [ ] Typography: 실제 font-size/weight 로 inline style 렌더, **헤더 행 없음**
- [ ] Colors: hex 값이 design.md 와 일치, 스와치 배경색 적용됨
- [ ] Code Export: 탭 전환 JS 존재, Copy 버튼 존재
- [ ] Do / Don't: 녹색/빨간 카드
- [ ] 선택 섹션: design.md 에 없는 섹션은 HTML + TOC 둘 다 없음
- [ ] 한글 네이밍: 스페이싱/라디우스/섀도우/Do·Don't

### 권장 PASS

- [ ] Screenshot: `screenshots/hero-cropped.png` 있으면 Hero 에 삽입, 없으면 생략
- [ ] Spacing: bar 의 width 가 실제 px 값
- [ ] design.md 에 없는 값이 HTML 에 나타나지 않음 (지어낸 값 없음)
- [ ] TOC 번호가 연속 (빈 번호 없음)
