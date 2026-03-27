#!/usr/bin/env python3
"""
Link integrity checker for epla-toc docs.

Checks:
  1. All [text](link) and ![](image) links in every .md file
  2. Resolves each link relative to the file that contains it
  3. If target is missing, searches for a file with the same name elsewhere in docs/
  4. Writes a broken-links.log with details
"""

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

DOCS_ROOT = Path(__file__).parent / "docs"
LOG_FILE = Path(__file__).parent / "broken-links.log"

# Matches both image and regular markdown links
# Captures: (optional !, link text, target)
LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)#\s][^)\s]*?)(?:\s+"[^"]*")?\)')


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "ftp://", "/"))


def find_elsewhere(filename: str, docs_root: Path) -> list[Path]:
    """Search for a file with this name anywhere under docs_root."""
    return list(docs_root.rglob(filename))


def check_links(docs_root: Path) -> dict:
    md_files = list(docs_root.rglob("*.md"))

    broken = []          # (source_file, link_target, is_image, suggestion)
    ok_count = 0
    external_count = 0

    print(f"Scanning {len(md_files)} markdown files under {docs_root}...\n")

    for md_path in sorted(md_files):
        content = md_path.read_text(encoding="utf-8", errors="replace")
        base_dir = md_path.parent

        for m in LINK_RE.finditer(content):
            excl, _text, target = m.group(1), m.group(2), m.group(3)
            is_image = excl == "!"

            # Skip external / absolute links
            if is_external(target):
                external_count += 1
                continue

            # Strip MkDocs attribute suffix e.g. "){ .ui-icon }" is already outside,
            # but sometimes attrs are inside: handle trailing `{ ... }` just in case
            target = re.sub(r'\s*\{[^}]*\}$', '', target).strip()

            resolved = (base_dir / target).resolve()

            if resolved.exists():
                ok_count += 1
            else:
                # Try to find the file somewhere else in docs
                filename = Path(target).name
                candidates = find_elsewhere(filename, docs_root)
                # Exclude the exact missing path
                candidates = [c for c in candidates if c.resolve() != resolved]

                suggestion = None
                if candidates:
                    # Prefer shortest relative path
                    suggestion = min(
                        candidates,
                        key=lambda p: len(p.parts)
                    ).relative_to(docs_root)

                broken.append({
                    "source": md_path.relative_to(docs_root),
                    "target": target,
                    "is_image": is_image,
                    "suggestion": str(suggestion) if suggestion else None,
                })

    return {
        "broken": broken,
        "ok_count": ok_count,
        "external_count": external_count,
        "total_files": len(md_files),
    }


def write_log(result: dict, log_path: Path) -> None:
    broken = result["broken"]

    # Group by whether a suggestion was found
    found_elsewhere = [b for b in broken if b["suggestion"]]
    not_found      = [b for b in broken if not b["suggestion"]]

    with log_path.open("w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("BROKEN LINKS REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Files scanned    : {result['total_files']}\n")
        f.write(f"Links OK         : {result['ok_count']}\n")
        f.write(f"External (skipped): {result['external_count']}\n")
        f.write(f"Broken total     : {len(broken)}\n")
        f.write(f"  → found elsewhere : {len(found_elsewhere)}\n")
        f.write(f"  → completely missing: {len(not_found)}\n\n")

        # --- Section 1: found elsewhere (fixable) ---
        if found_elsewhere:
            f.write("─" * 80 + "\n")
            f.write(f"FOUND ELSEWHERE ({len(found_elsewhere)} links) — wrong path, file exists\n")
            f.write("─" * 80 + "\n\n")
            for b in found_elsewhere:
                kind = "IMAGE" if b["is_image"] else "LINK "
                f.write(f"[{kind}] {b['source']}\n")
                f.write(f"       target    : {b['target']}\n")
                f.write(f"       suggestion: docs/{b['suggestion']}\n\n")

        # --- Section 2: completely missing ---
        if not_found:
            f.write("─" * 80 + "\n")
            f.write(f"COMPLETELY MISSING ({len(not_found)} links) — file not found anywhere\n")
            f.write("─" * 80 + "\n\n")
            for b in not_found:
                kind = "IMAGE" if b["is_image"] else "LINK "
                f.write(f"[{kind}] {b['source']}\n")
                f.write(f"       target    : {b['target']}\n\n")

    print(f"Report written to: {log_path}")


def print_summary(result: dict) -> None:
    broken = result["broken"]
    found  = [b for b in broken if b["suggestion"]]
    missing = [b for b in broken if not b["suggestion"]]

    print(f"Files scanned     : {result['total_files']}")
    print(f"Links OK          : {result['ok_count']}")
    print(f"External (skipped): {result['external_count']}")
    print(f"Broken total      : {len(broken)}")
    print(f"  ✓ found elsewhere : {len(found)}")
    print(f"  ✗ completely missing: {len(missing)}")


if __name__ == "__main__":
    result = check_links(DOCS_ROOT)
    print_summary(result)
    print()
    write_log(result, LOG_FILE)

    sys.exit(1 if result["broken"] else 0)