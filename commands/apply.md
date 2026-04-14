---
name: apply
description: "분석된 design.md를 내 프로젝트에 적용 — 카테고리별 선택 후 CSS/Tailwind 주입"
argument-hint: "[slug]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# /insane-design:apply Command

분석된 design.md의 디자인 토큰을 내 프로젝트에 적용한다.

## Parse Arguments

Inspect `$ARGUMENTS` to determine the action:

| Argument Pattern | Action |
|-----------------|--------|
| `[slug]` | 해당 design.md로 적용 시작 |
| (no argument) | slug 선택 요청 |

## No Argument Provided

**EXECUTE:** 아래 JSON으로 AskUserQuestion 도구를 즉시 호출한다:

```json
{
  "questions": [
    {
      "question": "어떤 사이트의 디자인을 적용할까요?",
      "header": "레퍼런스",
      "options": [
        {"label": "stripe", "description": "보라 브랜드, sohne 폰트, weight 300 — SaaS 대표"},
        {"label": "apple", "description": "모노크롬, SF Pro, 미니멀 — 프리미엄"},
        {"label": "toss", "description": "Toss Blue, 깔끔한 핀테크 UI"},
        {"label": "nike", "description": "Futura/Helvetica, 스포티한 느낌"}
      ],
      "multiSelect": false
    }
  ]
}
```

사용자가 "Other"로 slug를 직접 입력하면 그것을 사용한다.

## Execute

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/SKILL.md`
2. Follow SKILL.md's workflow with the provided slug: `$ARGUMENTS`
3. Every question MUST use the AskUserQuestion tool
