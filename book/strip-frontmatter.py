#!/usr/bin/env python3
"""mdBook preprocessor: strip a leading YAML frontmatter block from each chapter.

The whiteroom `.md` chapters carry a `---` ... `---` YAML frontmatter block read by
the graded-stack linter (`tools/graded-stack-lint`). mdBook has no native frontmatter
support, so without this preprocessor the YAML renders into every page — the `key: value`
lines as body text and, worse, the `# comment` lines as `<h1>` section headers (a `#`
line is a YAML comment but a Markdown ATX heading). This strips the leading frontmatter
block for RENDERING only; the source files (and their frontmatter) are untouched.

Protocol (mdBook preprocessor):
  - `strip-frontmatter.py supports <renderer>`  -> exit 0 (supported for all renderers)
  - otherwise: read `[context, book]` JSON on stdin, emit the transformed `book` on stdout.
"""
import sys
import json


def strip_frontmatter(content: str) -> str:
    """Remove a leading `---` ... `---` YAML block, if present."""
    if not content.startswith("---"):
        return content
    lines = content.split("\n")
    if lines[0].strip() != "---":
        return content
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1:]).lstrip("\n")
    return content


def process(items) -> None:
    for item in items:
        chapter = item.get("Chapter") if isinstance(item, dict) else None
        if chapter is None:
            continue
        if chapter.get("content"):
            chapter["content"] = strip_frontmatter(chapter["content"])
        if chapter.get("sub_items"):
            process(chapter["sub_items"])


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)
    context, book = json.load(sys.stdin)
    # mdBook >=0.5 names the top-level list `items`; older versions used `sections`.
    process(book.get("items") or book.get("sections") or [])
    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
