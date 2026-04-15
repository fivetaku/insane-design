---
name: insane-design-apply
description: >
  design.md를 디자인 브리프로 사용하여 내 프로젝트를 리디자인하는 스킬.
  "디자인 적용해줘", "stripe처럼 만들어줘", "이 스타일로 리디자인",
  "design.md 기반으로 바꿔줘", "apply design", "레퍼런스 적용".
  단순 토큰 교체가 아니라, design.md의 분위기(§00), 레이아웃(§11),
  컴포넌트(§13), 토큰(§15)을 종합하여 코드를 실제로 재작성한다.
---

# Insane Apply — 리디자인 워크플로우

> design.md = 디자인 브리프. 이걸 읽고 내 프로젝트를 해당 스타일로 리디자인한다.

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
slug가 제공되면 즉시 Step 0부터 실행한다.

---

## 핵심 원칙

**이 스킬은 토큰 교체가 아니라 리디자인이다.**

| 레벨 | 뭘 하는지 | 이 스킬의 범위 |
|------|----------|--------------|
| 리스킨 | CSS 변수만 교체 | 포함 |
| 리스타일 | + 컴포넌트 CSS 변경 | 포함 |
| **리디자인** | + 레이아웃/구조/배치 변경 | **이것이 목표** |

design.md는 "이 사이트는 이런 느낌, 이런 레이아웃, 이런 컴포넌트를 쓴다"를 알려주는 **디자인 브리프**다.
이걸 읽고 내 프로젝트 코드를 해당 스타일로 재작성한다.

---

## 워크플로우 — 5 Steps

### Step 0: 소스 + 타겟 분석

#### 0-A. design.md 찾기 (레퍼런스)

우선순위 순:
1. `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/{slug}/design.md`
2. `insane-design/{slug}/design.md` (프로젝트 루트)
3. 못 찾으면 → 사용 가능한 slug 목록 출력 후 중단

#### 0-B. design.md 읽기 (디자인 브리프)

**반드시 읽어야 하는 섹션:**

| 섹션 | 용도 | 읽는 이유 |
|------|------|----------|
| §00 Visual Theme | 전체 분위기와 철학 | 리디자인 방향 결정 |
| §01 Quick Start | 핵심 3가지 CSS | 최소 적용 기준 |
| §04 Font Stack | 폰트 + weight | 타이포그래피 변경 |
| §06 Colors | 브랜드 + neutral + semantic | 컬러 시스템 교체 |
| §08 Radius | 모서리 둥글기 | Shape 변경 |
| §09 Shadows | 그림자 패턴 | Elevation 변경 |
| §11 Layout Patterns | Grid, Hero, Section, Card, Nav 구조 | **레이아웃 재설계** |
| §13 Components | 버튼, 카드, 인풋, 네비, 히어로 CSS | **컴포넌트 재설계** |
| §15 Drop-in CSS | 복붙용 CSS 변수 블록 | 토큰 주입 |
| §18 DO/DON'T | 이 서비스에서 절대 하면 안 되는 것 | 실수 방지 |

#### 0-C. 내 프로젝트 코드 읽기 (타겟)

사용자가 지정한 파일 또는 자동 감지된 파일을 읽는다:
- HTML 파일 전체 구조 (어떤 섹션이 있는지, 컴포넌트가 뭔지)
- CSS/스타일 블록 (현재 토큰, 레이아웃 패턴, 컴포넌트 스타일)
- 프레임워크 감지 (Tailwind? Plain CSS? CSS Modules?)

#### 0-D. 분석 결과 출력 (텍스트)

```
📁 현재 프로젝트:
  - 파일: portfolio-final.html
  - 구조: Hero → About → Projects → Contact
  - 스타일: Toss 디자인 (인라인 CSS, CSS 변수 사용)
  - 컴포넌트: 카드 4개, CTA 버튼 2개, 네비게이션 1개

🎨 적용할 레퍼런스: Tesla
  - 분위기: 미니멀 모노크롬, 풀블리드 이미지, 큰 타이포
  - 레이아웃: 수직 스택, 풀스크린 섹션, 중앙 정렬
  - 컬러: #CC0000 (Red) + #F4F4F4 (라이트 그레이) + #000000 (순검정)
  - 폰트: Gotham SSm / Helvetica Neue, weight 400
```

---

### Step 1: 리디자인 범위 선택

**EXECUTE:** AskUserQuestion 즉시 호출:

```json
{
  "questions": [
    {
      "question": "어느 수준으로 적용할까요?",
      "header": "리디자인 범위",
      "options": [
        {
          "label": "전체 리디자인 (추천)",
          "description": "레이아웃 + 컴포넌트 + 토큰 전부 변경. design.md의 분위기대로 코드를 재작성합니다.",
          "preview": "변경 내용:\n- 레이아웃 구조 재배치\n- 컴포넌트(버튼/카드/네비) 스타일 재설계\n- 폰트, 컬러, 스페이싱, 라디우스, 그림자 교체\n- §00 Visual Theme의 분위기 반영"
        },
        {
          "label": "컴포넌트 + 토큰",
          "description": "레이아웃 구조는 유지. 컴포넌트 스타일과 디자인 토큰만 변경.",
          "preview": "변경 내용:\n- 버튼/카드/네비 스타일 교체\n- 폰트, 컬러, 라디우스, 그림자 교체\n- 섹션 배치/순서는 그대로"
        },
        {
          "label": "토큰만",
          "description": "CSS 변수(색/폰트/그림자)만 교체. 구조와 컴포넌트는 그대로.",
          "preview": "변경 내용:\n- :root { } 블록의 CSS 변수 교체\n- 레이아웃/컴포넌트 코드 변경 없음"
        }
      ],
      "multiSelect": false
    }
  ]
}
```

---

### Step 2: 리디자인 실행

선택된 범위에 따라 코드를 재작성한다.

#### 토큰만 선택 시

design.md §15 Drop-in CSS의 `:root { }` 블록으로 기존 CSS 변수를 교체한다.
- 기존 `/* insane-design: */` 블록이 있으면 → 해당 블록 전체 교체
- 없으면 → 새 블록 추가
- Edit 도구로 pinpoint 수정

#### 컴포넌트 + 토큰 선택 시

위 토큰 교체 + design.md §13 Components를 참조하여:
- 버튼: background, border, radius, padding, hover 상태 변경
- 카드: bg, border, shadow, padding, hover 효과 변경
- 네비게이션: bg, height, 링크 스타일 변경
- 인풋: border, focus ring, height 변경

**기존 HTML 구조는 유지**하고 CSS만 변경한다.

#### 전체 리디자인 선택 시

design.md §00 Visual Theme + §11 Layout + §13 Components를 종합하여:

1. **분위기 설정**: §00을 읽고 전체적인 톤/방향 결정
2. **레이아웃 재설계**: §11을 참조하여
   - Hero 영역 재배치 (풀블리드? 2-column? 중앙정렬?)
   - 섹션 리듬 변경 (padding, max-width, 여백)
   - 카드 그리드 변경 (열 수, gap, 배치)
   - 네비게이션 스타일 변경
3. **컴포넌트 재설계**: §13을 참조하여 각 컴포넌트 CSS 재작성
4. **토큰 교체**: §15의 CSS 변수 블록 주입
5. **DO/DON'T 확인**: §18을 읽고 금지사항 체크

**HTML 구조 변경도 포함**될 수 있다:
- 섹션 순서 재배치
- 그리드 컬럼 변경
- Hero 영역 구조 변경
- 하지만 **콘텐츠(텍스트, 이미지)는 보존**한다

---

### Step 3: 적용 전 확인

**EXECUTE:** AskUserQuestion 즉시 호출:

변경 사항을 요약하고 확인받는다.

```json
{
  "questions": [
    {
      "question": "이렇게 리디자인할까요?",
      "header": "확인",
      "options": [
        {
          "label": "적용하기 (추천)",
          "description": "위 변경 사항을 프로젝트 파일에 적용합니다.",
          "preview": "{변경 사항 동적 요약}"
        },
        {
          "label": "범위 다시 선택",
          "description": "Step 1로 돌아갑니다."
        }
      ],
      "multiSelect": false
    }
  ]
}
```

preview에 들어갈 동적 내용:
```
=== {서비스명} 스타일 리디자인 ===

분위기: {§00에서 핵심 1줄}

변경될 항목:
✓ 폰트: {현재} → {레퍼런스}
✓ 컬러: {현재 brand} → {레퍼런스 brand}
✓ 레이아웃: {변경 요약}
✓ 컴포넌트: {변경 요약}

수정 파일: {파일 목록}
롤백: git restore {파일}
```

---

### Step 4: 코드 재작성

**적용 전 안전 조치**:
1. `git status` 실행 → uncommitted changes 경고

**파일 수정**: Edit/Write 도구 사용
- 작은 변경 (토큰 교체) → Edit
- 큰 변경 (레이아웃 재설계) → Write (전체 재작성)

**insane-design 출처 표시**:
```css
/* ===== insane-design: {slug} ({date}) ===== */
```

**콘텐츠 보존 규칙**:
- 텍스트 내용 변경 금지 (이름, 설명, 프로젝트 목록 등)
- 이미지 경로 유지
- 링크 URL 유지
- 폼 action/method 유지

---

### Step 5: 완료 보고

```
✅ {서비스명} 스타일 리디자인 완료!

📝 수정된 파일:
  - {파일명} ({변경 라인 수})

🎨 적용된 디자인:
  - 분위기: {§00 핵심}
  - 레이아웃: {변경 요약}
  - 컴포넌트: {변경 요약}
  - 토큰: {변경 요약}

↩️ 되돌리기:
  git restore {파일명}

📖 레퍼런스:
  design.md: {경로}
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| slug에 해당하는 design.md 없음 | 사용 가능한 slug 목록 출력 후 중단 |
| design.md에 §11/§13 없음 | 토큰만 교체 (리디자인 범위 축소 안내) |
| 타겟 파일을 찾을 수 없음 | 사용자에게 파일 경로 입력 요청 |
| uncommitted changes 존재 | 경고 + "계속하시겠습니까?" 확인 |
| 전체 리디자인 후 깨진 부분 | 사용자에게 알리고 추가 수정 제안 |

---

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/references/apply-workflow.md` — 파싱/스캔/주입 상세 규칙
