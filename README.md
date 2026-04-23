English | [한국어](README.ko.md)

# insane-design

> **Rips the design system out of any website. In one command.**

"Make it feel like Stripe" is useless to AI — it needs tokens, not vibes. insane-design doesn't guess. It fetches the real CSS, parses every custom property, extracts typography, spacing, shadows, radii, and gradients, then hands your AI agent a `design.md` it can actually build with. Plus an interactive HTML report with click-to-copy swatches.

100 pre-analyzed sites shipped (Stripe, Apple, Linear, Toss, Notion...) — or point it at any URL and go.

**[See the gallery — 100 design system reports →](https://fivetaku.github.io/insane-design/)**

[Quick Start](#quick-start) • [Why insane-design?](#why-insane-design) • [How it works](#how-it-works) • [Features](#features) • [Requirements](#requirements)

---

## Quick Start

### 1. Add the marketplace (once)

```
/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git
```

### 2. Install

```
/plugin install insane-design
```

### 3. Restart Claude Code

Required for the plugin to load.

### 4. Run it

```
/insane-design https://stripe.com
```

Or use natural language: "analyze this site's design system" — the command figures out what you mean.

---

## Why insane-design?

- **Not LLM guessing** — CSS is fetched and parsed directly. Hex values come from actual stylesheets, not hallucinations.
- **AI-ready output** — `design.md` is structured for AI agents. Attach it to any prompt and get reproducible results instead of vibes.
- **100 pre-analyzed sites included** — Stripe, Apple, Linear, Vercel, Toss, Nike, Figma, Notion, and 92 more. Ready to apply without running analysis.
- **Two modes, one command** — Analyze a new URL, or apply an existing design system to your project. Same command handles both.
- **Drop-in CSS and Tailwind config** — The output includes ready-to-paste CSS variables and a Tailwind theme extension. No manual translation.
- **Interactive HTML report** — Color swatches with click-to-copy, live typography preview, spacing bars, shadow demo cards — everything visual in one file.
- **Quick Start cheat sheet** — "Apply these three things and it's 80% there." Prioritized for maximum impact, minimum effort.

---

## How it works

```
URL
  ↓
Fetch HTML + CSS files (real stylesheet bundles, Chrome UA)
  ↓
Parse CSS custom properties
Extract: color ramps · typography scale · spacing tokens
         radius system · shadow layers · font stack
  ↓
Visual verification via screenshot (Playwright or curl fallback)
Confirm: brand color · light/dark theme · font rendering
  ↓
Generate design.md          Generate report.html
(structured for AI agents)  (interactive browser report)
```

Output lands at `{site-slug}/`:

```
stripe/
├── design.md              # AI agent reference — 16-section structured doc
├── report.ko.html         # interactive HTML report
└── screenshots/
    └── hero-cropped.png   # 1280×800 screenshot
```

---

## Features

### Commands

| Command | What it does |
|---------|-------------|
| `/insane-design [URL]` | Analyze a site — extract design system, generate `design.md` + HTML report |
| `/insane-design [slug]` | Apply a pre-analyzed design to your project |
| `/insane-design:analysis [URL]` | Analysis mode only |
| `/insane-design:apply [slug]` | Apply mode only |
| `/insane-design:build [design.md]` | Scaffold a new page/component from a `design.md` (or synthesize on the fly from a URL) |
| `/insane-design:verify [job_id]` | Poll the async verifier — collects §18 DON'T violations + screenshot diff |

Natural language also works. "Analyze this site" triggers analysis mode, "apply the Stripe style" triggers apply mode.

### Design tokens extracted

| Token type | What's captured |
|------------|----------------|
| Colors | Brand ramp, neutral ramp, accent families, semantic aliases |
| Typography | Heading/body scale — size, weight, line-height, letter-spacing |
| Spacing | Full spacing token system |
| Radius | Border-radius scale |
| Shadows | Box-shadow layers (including multi-layer stacks) |
| Font stack | Custom font identification + fallback chain |

### design.md structure (16 sections)

| Section | Content |
|---------|---------|
| 01 Quick Start | 3-step CSS snippet — "80% there in 5 minutes" |
| 02 Provenance | Source URL, fetch date, CSS byte count |
| 03 Tech Stack | Framework and DS namespace detection |
| 04–05 Typography | Font stack + full scale |
| 06 Colors | Brand ramp · neutral · accents · semantic layer |
| 07–09 Spacing / Radius / Shadows | Full token tables |
| 12 Components | BEM class patterns and component variants |
| 14 Drop-in CSS | Ready-to-paste `:root {}` CSS variables |
| 15 Tailwind Config | `theme.extend` configuration |
| 16 DO / DON'T | Most common mistake to avoid for this site |

### Apply mode — inject tokens into your project

Apply scans your project (globals.css, Tailwind config, or plain CSS) and injects the design tokens without overwriting your existing setup.

| Target | What happens |
|--------|-------------|
| CSS with `:root {}` | Tokens appended inside existing block |
| CSS without `:root {}` | New `:root {}` created at top of file |
| Tailwind config | `theme.extend.colors`, `fontFamily`, `borderRadius` updated |
| Re-apply | `/* insane-design */` block replaced cleanly |

### 100 pre-analyzed sites

Stripe, Apple, Linear, Vercel, Notion, Figma, GitHub, Discord, Slack, Spotify, Toss, Baemin, Daangn, Kakao, Naver, Nike, Gucci, Chanel, Tesla, Ferrari, BMW, and 79 more. Apply any of them directly without running analysis.

---

## Requirements

### Required

- [Claude Code](https://docs.anthropic.com/claude-code)
- Python 3.11+
- Pillow (`pip install Pillow`)

### Optional

- **Playwright MCP** — improves screenshot capture quality. Without it, insane-design falls back to curl-based capture and still works.

---

## License

MIT

---

<div align="center">

**Real CSS. Not feelings.**

</div>
