#!/usr/bin/env python3
"""Extract layout patterns (§11) from CSS and HTML: grid, hero, section rhythm, card, nav, content width."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def extract_max_widths(css: str) -> list[dict]:
    """Find all max-width declarations with their selectors."""
    results = []
    for match in re.finditer(r'([^{}]+)\{([^{}]*max-width\s*:\s*([^;}\s]+)[^{}]*)\}', css):
        selector = ' '.join(match.group(1).split()).strip()
        value = match.group(3).strip()
        if selector and not selector.startswith('@'):
            results.append({"selector": selector, "value": value})
    return results


def extract_grid_patterns(css: str) -> list[dict]:
    """Find grid and flex layout declarations."""
    results = []
    for match in re.finditer(r'([^{}]+)\{([^{}]*(?:display\s*:\s*(?:grid|flex)|grid-template-columns)[^{}]*)\}', css):
        selector = ' '.join(match.group(1).split()).strip()
        body = match.group(2)
        if selector.startswith('@'):
            continue
        entry = {"selector": selector}
        display = re.search(r'display\s*:\s*(grid|flex|inline-grid|inline-flex)', body)
        if display:
            entry["display"] = display.group(1)
        cols = re.search(r'grid-template-columns\s*:\s*([^;]+)', body)
        if cols:
            entry["grid_columns"] = cols.group(1).strip()
        gap = re.search(r'(?:gap|grid-gap|column-gap|row-gap)\s*:\s*([^;]+)', body)
        if gap:
            entry["gap"] = gap.group(1).strip()
        results.append(entry)
    return results


def extract_section_rhythm(css: str) -> list[dict]:
    """Extract padding patterns from section/container selectors."""
    results = []
    section_pattern = re.compile(
        r'((?:section|\.section|\.container|\.wrapper|main|\.hero|\.content)[^{]*)\{([^}]+)\}',
        re.IGNORECASE
    )
    for match in section_pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        body = match.group(2)
        entry = {"selector": selector}
        padding = re.search(r'padding\s*:\s*([^;]+)', body)
        if padding:
            entry["padding"] = padding.group(1).strip()
        margin = re.search(r'margin\s*:\s*([^;]+)', body)
        if margin:
            entry["margin"] = margin.group(1).strip()
        mw = re.search(r'max-width\s*:\s*([^;]+)', body)
        if mw:
            entry["max_width"] = mw.group(1).strip()
        if len(entry) > 1:
            results.append(entry)
    return results


def extract_nav_patterns(css: str, html: str) -> dict:
    """Extract navigation structure from CSS and HTML."""
    nav_info = {"type": "unknown", "position": "unknown", "height": None, "bg": None}
    nav_css = re.search(r'(nav|\.nav|\.navbar|header|\.header)[^{]*\{([^}]+)\}', css, re.IGNORECASE)
    if nav_css:
        body = nav_css.group(2)
        pos = re.search(r'position\s*:\s*(fixed|sticky|absolute|relative|static)', body)
        if pos:
            nav_info["position"] = pos.group(1)
        h = re.search(r'height\s*:\s*([^;]+)', body)
        if h:
            nav_info["height"] = h.group(1).strip()
        bg = re.search(r'background(?:-color)?\s*:\s*([^;]+)', body)
        if bg:
            nav_info["bg"] = bg.group(1).strip()
    if re.search(r'<nav\b', html, re.IGNORECASE):
        nav_info["type"] = "semantic_nav"
    if re.search(r'hamburger|menu-toggle|mobile-menu', html + css, re.IGNORECASE):
        nav_info["has_hamburger"] = True
    return nav_info


def extract_card_patterns(css: str) -> list[dict]:
    """Extract card component patterns."""
    results = []
    card_pattern = re.compile(r'(\.card[^{]*)\{([^}]+)\}', re.IGNORECASE)
    for match in card_pattern.finditer(css):
        selector = ' '.join(match.group(1).split()).strip()
        body = match.group(2)
        entry = {"selector": selector}
        for prop in ['background', 'background-color', 'border', 'border-radius', 'padding', 'box-shadow']:
            m = re.search(rf'{prop}\s*:\s*([^;]+)', body)
            if m:
                entry[prop.replace('-', '_')] = m.group(1).strip()
        hover_match = re.search(rf'{re.escape(selector)}:hover\s*\{{([^}}]+)\}}', css)
        if hover_match:
            entry["hover"] = {}
            hbody = hover_match.group(1)
            for prop in ['box-shadow', 'transform', 'border-color', 'background']:
                hm = re.search(rf'{prop}\s*:\s*([^;]+)', hbody)
                if hm:
                    entry["hover"][prop.replace('-', '_')] = hm.group(1).strip()
        if len(entry) > 1:
            results.append(entry)
    return results


def extract_slug(slug: str) -> dict:
    """Read CSS+HTML, extract layout patterns, write phase1/layout.json."""
    service_dir = Path.cwd() / "insane-design" / slug
    css_dir = service_dir / "css"
    output_path = service_dir / "phase1" / "layout.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    css_files = sorted(css_dir.glob("*.css")) if css_dir.is_dir() else []
    if not css_files:
        result = {"slug": slug, "warning": "No CSS files found", "max_widths": [], "grids": [], "sections": [], "nav": {}, "cards": [], "stats": {"max_width_count": 0, "grid_count": 0, "section_count": 0, "card_count": 0}}
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return result

    css = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in css_files)
    html_path = service_dir / "index.html"
    html = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""

    result = {
        "slug": slug,
        "max_widths": extract_max_widths(css),
        "grids": extract_grid_patterns(css),
        "sections": extract_section_rhythm(css),
        "nav": extract_nav_patterns(css, html),
        "cards": extract_card_patterns(css),
        "stats": {}
    }
    result["stats"] = {
        "max_width_count": len(result["max_widths"]),
        "grid_count": len(result["grids"]),
        "section_count": len(result["sections"]),
        "card_count": len(result["cards"]),
    }

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    result = extract_slug(slug)
    print(json.dumps({"slug": slug, "output": f"insane-design/{slug}/phase1/layout.json", "stats": result["stats"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
