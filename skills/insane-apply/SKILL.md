---
name: insane-design-apply
description: >
  design.md를 디자인 브리프로 사용하여 기존 프로젝트를 리디자인하는 스킬.
  "디자인 적용해줘", "stripe처럼 만들어줘", "이 스타일로 리디자인",
  "apply design", "레이아웃 바꿔줘", "Tesla 느낌으로".
  design.md v3의 §00 Visual Theme, §11 Layout, §13 Components, §15 Drop-in CSS를
  읽고 기존 코드의 콘텐츠를 유지하면서 HTML + CSS를 재작성한다.
---

# Insane Apply

> design.md = 디자인 브리프. 기존 콘텐츠를 유지하면서 구조와 스타일을 재설계한다.

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
slug가 제공되면 즉시 Step 0부터 실행한다.

---

## 핵심 원칙

1. **콘텐츠는 보존, 디자인만 변경**: 텍스트, 이미지 URL, 링크, 데이터는 그대로 유지
2. **design.md가 디자인 브리프**: §00(분위기) + §11(레이아웃) + §13(컴포넌트) + §15(토큰)이 시공 지시서
3. **CSS Edit가 아니라 코드 재작성**: HTML 구조 + CSS를 design.md 기준으로 다시 쓴다
4. **원본 백업 보장**: 적용 전 git 상태 확인, 롤백 명령어 안내

---

## 워크플로우 — 5 Steps

### Step 0: 소스 확인 + 프로젝트 분석

#### 0-1. design.md 찾기

우선순위 순:
1. `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/{slug}/design.md`
2. `insane-design/{slug}/design.md` (프로젝트 루트)
3. 못 찾으면 → 사용 가능한 slug 목록 출력 후 중단

#### 0-2. design.md에서 디자인 브리프 추출

다음 섹션을 Read:

| 섹션 | 용도 | 추출 내용 |
|------|------|----------|
| §00 Visual Theme | 전체 분위기/철학 | 디자인 방향 (미니멀? 다이내믹? 럭셔리?) |
| §01 Quick Start | 핵심 3가지 | 폰트 + 배경/텍스트 + 브랜드 컬러 |
| §11 Layout Patterns | 구조 설계 | Grid, Hero, Section rhythm, Card, Nav, Content width |
| §12 Responsive | 반응형 전략 | Breakpoints, Touch targets, Collapsing strategy |
| §13 Components | 컴포넌트 패턴 | Button, Card, Input, Nav, Hero 구조 + CSS |
| §14 Content Voice | 카피 톤 | Headline/CTA/Subheading 패턴 |
| §15 Drop-in CSS | 토큰 | CSS 변수 블록 |
| §17 Agent Prompt | 컴포넌트 프롬프트 | 구현 참조 |

#### 0-3. 기존 프로젝트 코드 분석

대상 파일을 Read해서 다음을 파악:

1. **콘텐츠 인벤토리** — 보존해야 할 것:
   - 모든 텍스트 (제목, 본문, CTA 문구)
   - 이미지 URL / 파일 경로
   - 링크 (href, 앵커)
   - 메타데이터 (title, description, og 태그)
   - 외부 스크립트/임베드

2. **현재 구조 파악**:
   - 섹션 목록 (hero, projects, about, contact 등)
   - 컴포넌트 종류 (카드, 버튼, 네비, 폼 등)
   - 기술 스택 (Tailwind? CSS modules? inline?)

3. **스캔 결과 출력**:
   ```
   📁 기존 프로젝트 분석:
   - 파일: portfolio.html (34KB, 단일 HTML)
   - 섹션: nav → hero → project×4 → about → contact → footer
   - 컴포넌트: 카드 4개, CTA 버튼 4개, 네비, 연락 폼
   - 콘텐츠: 텍스트 28개, 이미지 8개, 링크 12개

   🎨 디자인 브리프: Tesla (design.md)
   - §00: 미니멀, 풀스크린 이미지, 수치 중심
   - §11: 100vh hero, 단일 컬럼, 풀블리드 섹션
   - §13: flat black CTA, 이미지 오버레이 hero
   ```

---

### Step 1: 적용 범위 선택

**EXECUTE:** AskUserQuestion 즉시 호출:

```json
{
  "questions": [
    {
      "question": "어떤 수준으로 적용할까요?",
      "header": "적용 범위",
      "options": [
        {
          "label": "전체 리디자인 (추천)",
          "description": "HTML 구조 + CSS를 design.md 기준으로 재작성. 콘텐츠(텍스트/이미지/링크)는 그대로 유지.",
          "preview": "변경 범위:\n✓ HTML 구조 재설계\n✓ CSS 전면 재작성\n✓ 컴포넌트 패턴 변경\n✓ 레이아웃/그리드 변경\n✓ 토큰(색/폰트/라디우스)\n\n보존:\n✓ 모든 텍스트 콘텐츠\n✓ 이미지 URL\n✓ 링크"
        },
        {
          "label": "스타일만 변경",
          "description": "HTML 구조 유지, CSS만 design.md 기준으로 재작성",
          "preview": "변경 범위:\n✓ CSS 전면 재작성\n✓ 토큰(색/폰트/라디우스)\n✗ HTML 구조 유지\n✗ 컴포넌트 마크업 유지\n\n보존:\n✓ 모든 HTML 구조\n✓ 모든 콘텐츠"
        },
        {
          "label": "토큰만 교체",
          "description": "기존 CSS 변수 값만 design.md 값으로 교체. 가장 안전.",
          "preview": "변경 범위:\n✓ CSS 변수 값 교체\n✗ CSS 규칙 유지\n✗ HTML 유지\n\n:root {\n  --brand: {brand_color};\n  --font: {font};\n  --radius: {radius};\n}"
        }
      ],
      "multiSelect": false
    }
  ]
}
```

---

### Step 2: 리디자인 실행

선택된 범위에 따라 실행:

#### 모드 A: 전체 리디자인

1. **콘텐츠 추출**: Step 0에서 파악한 텍스트/이미지/링크를 변수로 정리
2. **design.md 브리프 적용**:
   - §00 Visual Theme → 전체 분위기/톤 설정
   - §11 Layout Patterns → 섹션 구조, 그리드, Hero 패턴 재설계
   - §13 Components → 버튼/카드/네비/히어로 마크업 + CSS 재작성
   - §12 Responsive → 미디어 쿼리, 브레이크포인트 적용
   - §15 Drop-in CSS → :root 토큰 블록
   - §14 Content Voice → CTA 문구 톤 조정 (선택적)
3. **코드 재작성**: Write 도구로 파일 전체를 새로 작성
   - 기존 콘텐츠(텍스트/이미지/링크)를 새 구조에 채워넣기
   - `<!-- insane-design: {slug} -->` 주석 삽입
4. **기존 파일 대체**: 원본 파일을 새 코드로 Write

**재작성 시 참조 순서**:
```
1. §00 → "이 사이트는 어떤 느낌이어야 하는가?"
2. §11 → "섹션 배치, 그리드, Hero를 어떻게?"
3. §13 → "버튼/카드/네비를 어떻게 만드는가?"
4. §15 → ":root { } 토큰 블록 삽입"
5. §12 → "@media 쿼리 추가"
6. §17 → "컴포넌트별 구체 스펙 확인"
```

#### 모드 B: 스타일만 변경

1. HTML 구조 유지
2. `<style>` 블록 또는 CSS 파일만 재작성
3. design.md §15 토큰 + §13 컴포넌트 CSS 적용
4. Edit 도구로 CSS 부분만 교체

#### 모드 C: 토큰만 교체

1. 기존 `:root { }` 또는 `insane-design` 블록 찾기
2. design.md §15 Drop-in CSS의 값으로 교체
3. Edit 도구로 변수 값만 swap

---

### Step 3: 검증 + 확인

리디자인 완료 후:

1. **콘텐츠 보존 검증**: 기존 텍스트/이미지/링크가 모두 새 코드에 존재하는지 확인
   ```
   ✓ 텍스트 28개 중 28개 보존
   ✓ 이미지 8개 중 8개 보존
   ✓ 링크 12개 중 12개 보존
   ✗ 누락: 없음
   ```

2. **design.md 반영 검증**: 주요 토큰이 적용되었는지 확인
   ```
   ✓ brand_color: #CC0000
   ✓ primary_font: Gotham SSm
   ✓ bg: #F4F4F4
   ✓ Hero: 풀스크린 이미지 오버레이
   ✓ CTA: flat black 버튼
   ```

3. **AskUserQuestion으로 확인**:

```json
{
  "questions": [
    {
      "question": "리디자인 결과를 확인해주세요. 브라우저에서 열어보셨나요?",
      "header": "확인",
      "options": [
        {
          "label": "좋아요, 완료",
          "description": "리디자인 결과가 만족스럽습니다"
        },
        {
          "label": "수정할 부분 있어요",
          "description": "어떤 부분을 바꾸고 싶은지 알려주세요"
        },
        {
          "label": "되돌리기",
          "description": "git restore로 원래 상태로 돌립니다"
        }
      ],
      "multiSelect": false
    }
  ]
}
```

- "수정할 부분 있어요" → 사용자 피드백 받고 해당 부분만 수정
- "되돌리기" → `git restore {파일}` 실행

---

### Step 4: 완료 보고

```
✅ {서비스명} 스타일 리디자인 완료!

📝 변경 파일: {파일 목록}
🎨 적용 범위: {전체 리디자인 / 스타일만 / 토큰만}

🔄 적용된 디자인:
  - §00: {분위기 한줄 요약}
  - §11: {레이아웃 변경 요약}
  - §13: {컴포넌트 변경 요약}
  - §15: {토큰 요약}

📋 콘텐츠 보존: {N}개 텍스트, {N}개 이미지, {N}개 링크 — 모두 유지

↩️ 되돌리기: git restore {파일 목록}
📖 레퍼런스: {design.md 경로}
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| slug에 해당하는 design.md 없음 | 사용 가능한 slug 목록 출력 후 중단 |
| design.md에 §11/§13 없음 | "스타일만 변경" 모드로 자동 전환 (구조 리디자인 불가) |
| design.md에 §15도 없음 | §01 Quick Start + frontmatter로 최소 토큰 추출 |
| 대상 파일이 너무 큼 (>100KB) | 파일 단위로 분할 처리 제안 |
| 콘텐츠 누락 감지 | 누락 항목 경고 + 수동 확인 요청 |
| uncommitted changes 존재 | 경고 + "계속하시겠습니까?" 확인 |
| 대상이 여러 파일 프로젝트 | 파일별로 처리할지, 전체 한번에 할지 선택 |

---

## 적용 레벨 요약

| 레벨 | 변경 범위 | 도구 | design.md 섹션 |
|------|----------|------|---------------|
| **Lv3 전체 리디자인** | HTML + CSS 재작성 | Write | §00 + §11 + §12 + §13 + §15 |
| **Lv2 스타일 변경** | CSS만 재작성 | Write/Edit | §13 + §15 |
| **Lv1 토큰 교체** | CSS 변수 값만 swap | Edit | §15 |

---

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/references/apply-workflow.md` — 파싱/스캔/주입 규칙
