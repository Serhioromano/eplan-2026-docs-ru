#!/usr/bin/env python3
"""
Generate book/tree.md from mkdocs.yml nav structure.
For each nav entry with a file, also extracts H2 headings from that file.
"""

import os
import re
import yaml

MKDOCS_YML = "mkdocs.yml"
DOCS_DIR = "docs"
OUTPUT_FILE = "book/tree.md"


def load_nav():
    with open(MKDOCS_YML, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("nav", [])


def get_h2_headings(filepath):
    """Extract H2 headings from a markdown file."""
    headings = []
    try:
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                m = re.match(r'^##\s+(.+)', line)
                if m:
                    headings.append(m.group(1).strip())
    except FileNotFoundError:
        pass
    return headings


def render_nav(nav_items, out_lines, depth=0):
    indent = "  " * depth
    for item in nav_items:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    # Leaf node with a file
                    filepath = os.path.join(DOCS_DIR, value)
                    out_lines.append(f"{indent}- **{title}** — [{value}]({filepath})")
                    h2s = get_h2_headings(filepath)
                    for h2 in h2s:
                        out_lines.append(f"{indent}  - {h2}")
                elif isinstance(value, list):
                    # Section with children
                    out_lines.append(f"{indent}- **{title}**")
                    render_nav(value, out_lines, depth + 1)
        elif isinstance(item, str):
            out_lines.append(f"{indent}- {item}")


def main():
    nav = load_nav()

    lines = [
        "# Структура книги",
        "",
        "Многоуровневое дерево разделов на основе навигации mkdocs.yml.",
        "Для каждого файла перечислены заголовки второго уровня (##).",
        "",
    ]

    render_nav(nav, lines, depth=0)

    os.makedirs("book", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Готово: {OUTPUT_FILE}")
    # Count stats
    file_count = sum(1 for l in lines if " — [" in l)
    h2_count = sum(1 for l in lines if l.strip().startswith("- ") and " — [" not in l and "**" not in l)
    print(f"  Файлов: {file_count}, H2-заголовков: {h2_count}")


if __name__ == "__main__":
    main()