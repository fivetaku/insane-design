---
name: insane-design
description: "URL 하나로 실제 CSS 기반 디자인 시스템 분석 — design.md + HTML 리포트 생성"
argument-hint: "[URL]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---

# /insane-design Command

URL을 입력받아 해당 웹사이트의 실제 CSS를 분석하고 design.md + report.ko.html을 생성한다.

## Parse Arguments

Inspect `$ARGUMENTS` to determine the action:

| Argument Pattern | Action |
|-----------------|--------|
| `[URL]` | 해당 URL 분석 시작 |
| (no argument) | URL 입력 요청 |

## No Argument Provided

**EXECUTE:** 아래 JSON으로 AskUserQuestion 도구를 즉시 호출한다:

```json
{
  "questions": [
    {
      "question": "어떤 사이트의 디자인을 분석할까요? URL을 입력해주세요.",
      "header": "URL 입력",
      "options": [
        {"label": "https://stripe.com (예시)", "description": "Stripe 홈페이지를 분석해서 디자인 토큰, 폰트, 색상 램프를 추출해요."},
        {"label": "https://linear.app (예시)", "description": "Linear 홈페이지를 분석해요."},
        {"label": "https://vercel.com (예시)", "description": "Vercel 홈페이지를 분석해요."}
      ],
      "multiSelect": false
    }
  ]
}
```

사용자가 "Other"로 URL을 직접 입력하면 그것을 사용한다.

## Execute

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/SKILL.md`
2. Follow SKILL.md's 7-Step workflow with the provided URL: `$ARGUMENTS`
3. Every question MUST use the AskUserQuestion tool
