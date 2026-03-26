#!/usr/bin/env python3
"""Clean up markdown files in docs/new/:
1. Reformat 'См. также' section (bold, colon, list, no blank lines between links)
2. Collapse multiple blank lines into one
3. Remove leading whitespace from list items (* and 1., 2., etc.)
4. Delete everything before the first ## heading
5. Change .htm to .md in markdown links
6. Convert javascript: links to plain text
"""

import re
import glob

def fix_see_also(content):
    """Reformat 'См. также' sections."""
    pattern = re.compile(
        r'^См\. также\s*\n'
        r'((?:\s*\n)*'
        r'(?:\[.+?\]\(.+?\)\s*\n(?:\s*\n)*)+)',
        re.MULTILINE
    )
    def reformat(match):
        block = match.group(1)
        links = re.findall(r'(\[.+?\]\(.+?\))', block)
        result = '**См. также:**\n\n'
        result += '\n'.join(f'* {link}' for link in links) + '\n'
        return result
    return pattern.sub(reformat, content)

def collapse_blank_lines(content):
    """Replace multiple consecutive blank lines (including whitespace-only lines) with a single blank line."""
    # First, strip trailing whitespace from every line so whitespace-only lines become truly empty
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    # Then collapse runs of 2+ empty lines into one
    return re.sub(r'\n{3,}', '\n\n', content)

def strip_list_indent(content):
    """Remove leading whitespace from list items (* and numbered)."""
    content = re.sub(r'^[ \t]+\* ', '* ', content, flags=re.MULTILINE)
    content = re.sub(r'^[ \t]+(\d+\.) ', r'\1 ', content, flags=re.MULTILINE)
    return content

def delete_before_first_heading(content):
    """Delete everything before the first ## heading."""
    match = re.search(r'^## ', content, re.MULTILINE)
    if match:
        content = content[match.start():]
    return content

def fix_javascript_links(content):
    """Convert [text](javascript:...) links to plain text, remove empty ones."""
    content = re.sub(r'\[([^\]]+)\]\(javascript:[^)]*\);?\)?', r'\1', content)
    content = re.sub(r'\[\]\(javascript:[^)]*\);?\)?', '', content)
    return content

def fix_stray_semicolon_paren(content):
    """Remove leftover ;) artifacts from escaped javascript links."""
    return re.sub(r';\)', '', content)

def fix_htm_links(content):
    """Change .htm to .md in markdown links."""
    return re.sub(r'(\[[^\]]+\]\([^)]+)\.htm(\))', r'\1.md\2', content)

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = delete_before_first_heading(content)
    content = fix_see_also(content)
    content = strip_list_indent(content)
    content = fix_javascript_links(content)
    content = fix_stray_semicolon_paren(content)
    content = fix_htm_links(content)
    content = collapse_blank_lines(content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for path in sorted(glob.glob('docs/new/*.md')):
    if process_file(path):
        count += 1

print(f'Updated {count} files')
