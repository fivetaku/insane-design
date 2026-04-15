#!/usr/bin/env python3
"""Extract responsive behavior (§12) from CSS: @media queries, breakpoints, touch targets."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


def extract_breakpoints(css: str) -> list[dict]:
    """Extract all @media breakpoints with their widths and content summary."""
    breakpoints: list[dict] = []
    seen: set[str] = set()

    for match in re.finditer(r'@media\s*\(([^)]+)\)\s*\{', css):
        condition = match.group(1).strip()
        width_match = re.search(r'(min|max)-width\s*:\s*([\d.]+(?:px|em|rem))', condition)
        if not width_match:
            continue
        direction = width_match.group(1)
        value = width_match.group(2)
        key = f"{direction}-{value}"
        if key in seen:
            continue
        seen.add(key)
        breakpoints.append({
            "condition": condition,
            "direction": direction,
            "value": value,
        })

    breakpoints.sort(key=lambda b: _to_px(b["value"]))
    return breakpoints


def _to_px(value: str) -> float:
    """Convert CSS length to px for sorting."""
    num = re.match(r'([\d.]+)', value)
    if not num:
        return 0
    n = float(num.group(1))
    if 'em' in value or 'rem' in value:
        return n * 16
    return n


def detect_mobile_first(breakpoints: list[dict]) -> str:
    """Determine if the CSS is mobile-first or desktop-first."""
    min_count = sum(1 for b in breakpoints if b["direction"] == "min")
    max_count = sum(1 for b in breakpoints if b["direction"] == "max")
    if min_count > max_count:
        return "mobile-first"
    elif max_count > min_count:
        return "desktop-first"
    return "mixed"


def extract_touch_targets(css: str) -> dict:
    """Look for touch-friendly sizing patterns."""
    targets = {"min_height_44px": False, "button_heights": [], "input_heights": []}

    for match in re.finditer(r'(?:button|\.btn|\.button|input|\.input)[^{]*\{([^}]+)\}', css, re.IGNORECASE):
        body = match.group(1)
        h = re.search(r'(?:min-)?height\s*:\s*([\d.]+(?:px|rem|em))', body)
        if h:
            val = h.group(1)
            px = _to_px(val)
            if 'button' in match.group(0).lower() or 'btn' in match.group(0).lower():
                targets["button_heights"].append(val)
            else:
                targets["input_heights"].append(val)
            if px >= 44:
                targets["min_height_44px"] = True

    targets["button_heights"] = list(set(targets["button_heights"]))
    targets["input_heights"] = list(set(targets["input_heights"]))
    return targets


def extract_collapsing_strategy(css: str) -> dict:
    """Detect how layout collapses at smaller breakpoints."""
    strategy = {"nav_collapse": None, "grid_collapse": None, "sidebar_collapse": None}

    if re.search(r'@media[^{]*\{[^}]*(?:display\s*:\s*none|visibility\s*:\s*hidden)[^}]*(?:nav|menu)', css, re.IGNORECASE):
        strategy["nav_collapse"] = "hidden_at_mobile"
    if re.search(r'hamburger|menu-toggle|mobile-menu', css, re.IGNORECASE):
        strategy["nav_collapse"] = "hamburger"

    if re.search(r'@media[^{]*\{[^}]*grid-template-columns\s*:\s*1fr\s*[;}]', css, re.IGNORECASE):
        strategy["grid_collapse"] = "single_column"

    if re.search(r'@media[^{]*\{[^}]*(?:sidebar|aside)[^}]*display\s*:\s*none', css, re.IGNORECASE):
        strategy["sidebar_collapse"] = "hidden_at_mobile"

    return strategy


def extract_slug(slug: str) -> dict:
    """Read CSS, extract responsive patterns, write phase1/responsive.json."""
    service_dir = Path.cwd() / "insane-design" / slug
    css_dir = service_dir / "css"
    output_path = service_dir / "phase1" / "responsive.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    css_files = sorted(css_dir.glob("*.css")) if css_dir.is_dir() else []
    if not css_files:
        result = {"slug": slug, "warning": "No CSS files found", "breakpoints": [], "approach": "unknown", "touch": {}, "collapsing": {}, "stats": {"breakpoint_count": 0, "approach": "unknown"}}
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return result

    css = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in css_files)

    breakpoints = extract_breakpoints(css)
    approach = detect_mobile_first(breakpoints)
    touch = extract_touch_targets(css)
    collapsing = extract_collapsing_strategy(css)

    result = {
        "slug": slug,
        "breakpoints": breakpoints,
        "approach": approach,
        "touch": touch,
        "collapsing": collapsing,
        "stats": {
            "breakpoint_count": len(breakpoints),
            "approach": approach,
        }
    }

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    result = extract_slug(slug)
    print(json.dumps({"slug": slug, "output": f"insane-design/{slug}/phase1/responsive.json", "stats": result["stats"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
