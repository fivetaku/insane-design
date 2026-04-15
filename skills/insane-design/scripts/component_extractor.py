#!/usr/bin/env python3
"""Extract component patterns (§13) from CSS and HTML: buttons, cards, nav, inputs, hero."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def _extract_props(body: str, props: list[str]) -> dict[str, str]:
    """Extract specific CSS properties from a rule body."""
    result = {}
    for prop in props:
        m = re.search(rf'{re.escape(prop)}\s*:\s*([^;]+)', body)
        if m:
            result[prop] = m.group(1).strip()
    return result


COMMON_PROPS = [
    'background', 'background-color', 'color', 'border', 'border-radius',
    'padding', 'margin', 'height', 'min-height', 'width', 'max-width',
    'font-size', 'font-weight', 'font-family', 'line-height', 'letter-spacing',
    'box-shadow', 'text-decoration', 'display', 'gap', 'opacity', 'cursor',
    'transition', 'transform', 'outline',
]


def _extract_hover(selector: str, css: str) -> dict[str, str]:
    """Extract hover/focus/active state properties."""
    states = {}
    for state in ['hover', 'focus', 'active', 'focus-visible']:
        pattern = re.escape(selector.rstrip()) + rf':{state}\s*\{{([^}}]+)\}}'
        m = re.search(pattern, css)
        if m:
            props = _extract_props(m.group(1), COMMON_PROPS)
            if props:
                states[state] = props
    return states


def extract_buttons(css: str, html: str) -> list[dict]:
    """Extract button component styles."""
    results = []
    seen = set()
    pattern = re.compile(r'((?:\.btn|\.button|button|\.cta|a\.primary)[^\s,{]*)\s*\{([^}]+)\}', re.IGNORECASE)
    for match in pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        if selector in seen or len(selector) > 80:
            continue
        seen.add(selector)
        props = _extract_props(match.group(2), COMMON_PROPS)
        if not props:
            continue
        entry = {"selector": selector, "props": props}
        states = _extract_hover(selector, css)
        if states:
            entry["states"] = states
        results.append(entry)
    return results[:10]


def extract_cards(css: str) -> list[dict]:
    """Extract card/container component styles."""
    results = []
    seen = set()
    pattern = re.compile(r'(\.card[^\s,{]*)\s*\{([^}]+)\}', re.IGNORECASE)
    for match in pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        if selector in seen:
            continue
        seen.add(selector)
        props = _extract_props(match.group(2), COMMON_PROPS)
        if not props:
            continue
        entry = {"selector": selector, "props": props}
        states = _extract_hover(selector, css)
        if states:
            entry["states"] = states
        results.append(entry)
    return results[:10]


def extract_inputs(css: str) -> list[dict]:
    """Extract input/form component styles."""
    results = []
    seen = set()
    pattern = re.compile(r'((?:input|textarea|\.input|\.form-control|select)[^\s,{]*)\s*\{([^}]+)\}', re.IGNORECASE)
    for match in pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        if selector in seen or len(selector) > 80:
            continue
        seen.add(selector)
        props = _extract_props(match.group(2), COMMON_PROPS)
        if not props:
            continue
        entry = {"selector": selector, "props": props}
        states = _extract_hover(selector, css)
        if states:
            entry["states"] = states
        results.append(entry)
    return results[:10]


def extract_nav(css: str, html: str) -> list[dict]:
    """Extract navigation component styles."""
    results = []
    seen = set()
    pattern = re.compile(r'((?:nav|\.nav|\.navbar|header|\.header|\.menu)[^\s,{]*)\s*\{([^}]+)\}', re.IGNORECASE)
    for match in pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        if selector in seen or len(selector) > 80:
            continue
        seen.add(selector)
        props = _extract_props(match.group(2), COMMON_PROPS)
        if not props:
            continue
        results.append({"selector": selector, "props": props})
    return results[:10]


def extract_hero(css: str, html: str) -> list[dict]:
    """Extract hero section styles."""
    results = []
    pattern = re.compile(r'(\.hero[^\s,{]*)\s*\{([^}]+)\}', re.IGNORECASE)
    for match in pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        props = _extract_props(match.group(2), COMMON_PROPS)
        if props:
            results.append({"selector": selector, "props": props})
    return results[:10]


def extract_slug(slug: str) -> dict:
    """Read CSS+HTML, extract component patterns, write phase1/components.json."""
    service_dir = Path.cwd() / "insane-design" / slug
    css_dir = service_dir / "css"
    output_path = service_dir / "phase1" / "components.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    css_files = sorted(css_dir.glob("*.css")) if css_dir.is_dir() else []
    if not css_files:
        result = {"slug": slug, "warning": "No CSS files found", "buttons": [], "cards": [], "inputs": [], "nav": [], "hero": [], "stats": {"button_count": 0, "card_count": 0, "input_count": 0, "nav_count": 0, "hero_count": 0}}
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return result

    css = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in css_files)
    html_path = service_dir / "index.html"
    html = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""

    result = {
        "slug": slug,
        "buttons": extract_buttons(css, html),
        "cards": extract_cards(css),
        "inputs": extract_inputs(css),
        "nav": extract_nav(css, html),
        "hero": extract_hero(css, html),
        "stats": {},
    }
    result["stats"] = {
        "button_count": len(result["buttons"]),
        "card_count": len(result["cards"]),
        "input_count": len(result["inputs"]),
        "nav_count": len(result["nav"]),
        "hero_count": len(result["hero"]),
    }

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    result = extract_slug(slug)
    print(json.dumps({"slug": slug, "output": f"insane-design/{slug}/phase1/components.json", "stats": result["stats"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
