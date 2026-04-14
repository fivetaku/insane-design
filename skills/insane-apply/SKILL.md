---
name: insane-design-apply
description: >
  분석된 design.md의 디자인 토큰을 내 프로젝트에 적용하는 스킬.
  "디자인 적용해줘", "design.md 적용", "토큰 주입", "CSS 변수 적용",
  "이 사이트 스타일로", "stripe처럼 만들어줘", "apply design".
  design.md의 §14 Drop-in CSS와 §15 Tailwind Config를 파싱하여
  카테고리별 선택 후 프로젝트 파일에 주입한다.
---

# Insane Apply

> design.md → 카테고리별 선택 → 내 프로젝트에 디자인 토큰 주입

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
slug가 제공되면 즉시 Step 0부터 실행한다.

---

## 워크플로우 — 5 Steps

### Step 0: 소스 확인 + 프로젝트 스캔

1. **design.md 찾기** (우선순위 순):
   - `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/{slug}/design.md`
   - `insane-design/{slug}/design.md` (프로젝트 루트)
   - 못 찾으면 사용자에게 "이 slug의 design.md를 찾을 수 없습니다" + 사용 가능한 slug 목록 출력 후 중단

2. **slug 검증**:
   - 공백, 특수문자 포함 시 거부
   - 대소문자 무시 (모두 소문자로 정규화)

3. **design.md 파싱**:
   - YAML frontmatter 추출: `brand_color`, `primary_font`, `font_weight_normal`, `default_theme`
   - §14 Drop-in CSS: `## 14.` 헤더 다음의 ` ```css ` 블록 추출
   - §15 Tailwind Config: `## 15.` 헤더 다음의 ` ```js ` 블록 추출 (없으면 skip)
   - §01 Quick Start: 3줄 CSS 스니펫 추출
   - §08 Radius: 라디우스 토큰 테이블 추출
   - §09 Shadows: 그림자 값 추출

4. **내 프로젝트 스캔** (Glob으로 자동 감지):

   ```
   스택 감지 우선순위:
   1. tailwind.config.{js,ts,mjs,cjs} → Tailwind 프로젝트
   2. package.json의 dependencies에 tailwindcss → Tailwind 프로젝트
   3. globals.css / global.css / app.css 발견 → Plain CSS 프로젝트
   4. 위 모두 없음 → AskUserQuestion으로 파일 경로 직접 입력
   ```

   CSS 파일 탐색 경로 (순서대로):
   - `src/app/globals.css`
   - `app/globals.css`
   - `src/styles/globals.css`
   - `styles/global.css`
   - `src/index.css`
   - `app.css`

5. **현재 토큰 추출**:
   - 발견된 CSS 파일에서 `:root { }` 블록의 기존 변수 추출
   - tailwind.config에서 기존 theme.extend 추출
   - 충돌 변수 목록 준비 (design.md 토큰과 이름이 겹치는 것)

6. **스캔 결과 출력** (텍스트):
   ```
   📁 프로젝트 감지 결과:
   - 스택: Tailwind v3 + Next.js
   - CSS 파일: src/app/globals.css
   - Tailwind: tailwind.config.ts
   - 기존 토큰: 12개 (--brand, --bg, --text 등)
   - 충돌: 3개 (--brand, --radius-md, --font-sans)
   
   🎨 적용할 레퍼런스: Stripe (design.md)
   - 브랜드: #533AFD
   - 폰트: sohne-var, weight 300
   - 테마: mixed
   ```

---

### Step 1: 폰트 + 브랜드 컬러 선택

**EXECUTE:** AskUserQuestion 즉시 호출:

design.md frontmatter에서 `primary_font`, `font_weight_normal`, `brand_color`를 읽고,
내 프로젝트의 현재 값과 비교하여 **동적으로** 옵션을 생성한다.

```json
{
  "questions": [
    {
      "question": "폰트를 어떻게 할까요?",
      "header": "폰트",
      "options": [
        {
          "label": "현재 유지",
          "description": "지금 쓰고 있는 {현재폰트}, weight {현재weight} 유지",
          "preview": "body {\n  font-family: \"{현재폰트}\", sans-serif;\n  font-weight: {현재weight};\n}"
        },
        {
          "label": "{레퍼런스} 적용",
          "description": "{서비스명}의 {레퍼런스폰트}, weight {레퍼런스weight}로 변경",
          "preview": "body {\n  font-family: \"{레퍼런스폰트}\", sans-serif;\n  font-weight: {레퍼런스weight};\n}"
        },
        {
          "label": "weight만 변경",
          "description": "현재 폰트 유지, weight만 {레퍼런스weight}로",
          "preview": "body {\n  font-family: \"{현재폰트}\", sans-serif;\n  font-weight: {레퍼런스weight};\n}"
        }
      ],
      "multiSelect": false
    },
    {
      "question": "브랜드 컬러는?",
      "header": "브랜드",
      "options": [
        {
          "label": "현재 유지 ({현재brand})",
          "description": "지금 쓰고 있는 브랜드 컬러 유지",
          "preview": ":root {\n  --brand: {현재brand};\n}"
        },
        {
          "label": "{레퍼런스brand} 적용",
          "description": "{서비스명}의 브랜드 컬러로 변경",
          "preview": ":root {\n  --brand: {레퍼런스brand};\n}"
        }
      ],
      "multiSelect": false
    }
  ]
}
```

**옵션 동적 생성 규칙:**
- `{현재폰트}`, `{현재weight}` → Step 0에서 스캔한 프로젝트 현재 값
- `{레퍼런스폰트}`, `{레퍼런스weight}` → design.md frontmatter 값
- `{현재brand}`, `{레퍼런스brand}` → 프로젝트 vs design.md 값
- 현재 값을 감지 못했으면 "현재 유지" 대신 "설정 없음 (새로 추가)"로 표시

---

### Step 2: Neutral + Shape 선택

design.md §01 Quick Start에서 `--bg`, `--fg` 값을, §08에서 라디우스, §09에서 그림자를 읽어온다.

```json
{
  "questions": [
    {
      "question": "배경/텍스트 톤과 모서리를 어떻게 할까요?",
      "header": "톤+Shape",
      "multiSelect": true,
      "options": [
        {
          "label": "배경/텍스트 톤 적용",
          "description": "{서비스명}의 배경({bg_hex})과 텍스트({fg_hex}) 톤으로 변경",
          "preview": ":root {\n  --bg: {bg_hex};\n  --fg: {fg_hex};\n}"
        },
        {
          "label": "라디우스 적용",
          "description": "{서비스명}의 모서리 둥글기로 변경 (sm: {r_sm}, md: {r_md})",
          "preview": ":root {\n  --radius-sm: {r_sm};\n  --radius-md: {r_md};\n  --radius-lg: {r_lg};\n}"
        },
        {
          "label": "그림자 적용",
          "description": "{서비스명}의 그림자 스타일로 변경",
          "preview": ":root {\n  --shadow-sm: {shadow_sm};\n  --shadow-md: {shadow_md};\n}"
        }
      ]
    }
  ]
}
```

**multiSelect**: 원하는 것만 골라서 적용 가능.

---

### Step 3: 최종 확인 + 적용

선택 결과를 요약하고 확인받는다.

```json
{
  "questions": [
    {
      "question": "이렇게 적용할까요?",
      "header": "확인",
      "options": [
        {
          "label": "적용하기 (추천)",
          "description": "선택한 토큰을 프로젝트 파일에 주입합니다",
          "preview": "{선택된 모든 CSS 변수 변경 요약}"
        },
        {
          "label": "다시 선택",
          "description": "Step 1부터 다시 선택합니다"
        }
      ],
      "multiSelect": false
    }
  ]
}
```

**preview에 들어갈 내용 (동적 생성)**:
```
=== 변경 사항 ===
✓ 폰트: Inter 400 → sohne-var 300
✓ 브랜드: #3B82F6 → #533AFD
✗ 배경/텍스트: 현재 유지
✓ 라디우스: 6px → 12px
✗ 그림자: 현재 유지

수정 파일: src/app/globals.css (4줄 추가)
롤백: git restore src/app/globals.css
```

"다시 선택" 시 Step 1로 돌아간다.

---

### Step 4: 파일 수정

**적용 전 안전 조치**:
1. `git status` 실행 → uncommitted changes 경고
2. 적용할 파일 목록 출력

**CSS 파일 수정 (Edit 도구 사용)**:

케이스 A: 기존 `:root { }` 블록이 있는 경우
→ Edit으로 블록 내부에 선택된 토큰 추가/교체

케이스 B: `:root { }` 블록이 없는 경우
→ 파일 최상단에 새 `:root { }` 블록 추가

케이스 C: Tailwind 프로젝트 + §15 있는 경우
→ tailwind.config의 `theme.extend`에 토큰 병합

**충돌 처리**:
- 동일 이름 변수가 이미 있으면 → 새 값으로 교체 (Edit의 old_string → new_string)
- 새 변수면 → 블록에 append

**주입 코드 형식**:
```css
/* ===== insane-design: {slug} ({date}) ===== */
:root {
  /* Fonts */
  --font-sans: "{primary_font}", sans-serif;
  --font-weight-normal: {weight};
  
  /* Brand */
  --brand: {brand_color};
  
  /* Surfaces */
  --bg: {bg_hex};
  --fg: {fg_hex};
  
  /* Shape */
  --radius-sm: {r_sm};
  --radius-md: {r_md};
}
/* ===== /insane-design ===== */
```

**"현재 유지" 선택된 카테고리는 주입하지 않는다.**
모든 카테고리가 "현재 유지"면 파일 수정 없이 완료 메시지만 출력.

---

### Step 5: 완료 보고

```
✅ {서비스명} 디자인 토큰 적용 완료!

📝 수정된 파일:
  - src/app/globals.css (4줄 추가)

🔄 적용된 항목:
  - 폰트: sohne-var, weight 300
  - 브랜드: #533AFD

↩️ 되돌리기:
  git restore src/app/globals.css

📖 전체 레퍼런스:
  design.md: examples/stripe/design.md
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| slug에 해당하는 design.md 없음 | 사용 가능한 slug 목록 (카테고리별) 출력 후 중단 |
| §14 Drop-in CSS 섹션 없음 | frontmatter + §01 Quick Start로 최소 토큰 추출 |
| 프로젝트 CSS 파일 없음 | AskUserQuestion으로 파일 경로 입력받기 |
| Tailwind v4 프로젝트 | `@theme` 블록 방식으로 분기 (v3과 다름) |
| 모든 선택이 "현재 유지" | 파일 수정 없이 "변경 사항 없음" 메시지 출력 |
| uncommitted changes 존재 | 경고 출력 + "계속하시겠습니까?" 확인 |
