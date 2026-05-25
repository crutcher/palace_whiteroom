#!/usr/bin/env python3
"""One-shot migration: split LOG.md into per-cycle / per-meta entries
under log/, and emit log/README.md as the index.

Usage:  python3 tools/migrate-log/migrate.py

Idempotent if the log/ directory already exists — overwrites entries.
After migration, the orchestrator writes new entries directly into
log/<entry>.md via state.write_log_entry() (added 2026-05-26).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_MD = REPO_ROOT / "LOG.md"
LOG_DIR = REPO_ROOT / "log"


def main() -> int:
    if not LOG_MD.exists():
        print(f"LOG.md not at {LOG_MD}; nothing to migrate.")
        return 1
    text = LOG_MD.read_text()

    # Preserve the header up to the first '---' separator as log/README.md's
    # preface (about the format and convention).
    header_match = re.search(r"\A(.*?)\n---\n", text, re.DOTALL)
    if header_match:
        header = header_match.group(1).strip()
        rest = text[header_match.end():]
    else:
        header = "# Cycle log\n\nPer-cycle and meta-review entries, one file each. Indexed newest-first below."
        rest = text

    # Split on `^## ` lines into entries. The first chunk before any `## `
    # is preamble (kept in header).
    chunks = re.split(r"(?=^## )", rest, flags=re.MULTILINE)
    entries: list[dict] = []  # {filename, title, body, cycle_id_for_sort}

    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or not chunk.startswith("## "):
            continue
        # Parse the heading
        m = re.match(r"## (.+)", chunk.splitlines()[0])
        if not m:
            continue
        title = m.group(1).strip()

        # Determine filename: cycles get cycle-NNN.md; meta-reviews get meta-NN.md.
        cycle_match = re.search(r"cycle-(\d+)\b", title)
        meta_match = re.search(r"meta-review \(cycles (\d+)[–-](\d+)\)", title)
        meta_n: int | None = None
        cycle_id_for_sort: int | None = None
        if cycle_match:
            cycle_id = int(cycle_match.group(1))
            filename = f"cycle-{cycle_id:03d}.md"
            cycle_id_for_sort = cycle_id * 10  # cycles before meta-of-same-window
        elif meta_match:
            # We need to derive meta_n from the entry's position in the LOG.
            # The original LOG.md is in newest-first order; we'll count
            # meta entries by scanning AFTER the loop. For now use a
            # placeholder.
            cycle_end = int(meta_match.group(2))
            cycle_id_for_sort = cycle_end * 10 + 1  # meta after last cycle of window
            filename = f"meta-{cycle_end:03d}-cycles-{meta_match.group(1)}-{meta_match.group(2)}.md"
        else:
            # Fallback: kebab-case the title for the filename
            slug = re.sub(r"[^\w\s-]", "", title).strip().lower()
            slug = re.sub(r"[-\s]+", "-", slug)[:80]
            filename = f"misc-{slug}.md"
            cycle_id_for_sort = 0

        entries.append({
            "filename": filename,
            "title": title,
            "body": chunk + "\n",
            "sort_key": cycle_id_for_sort or 0,
        })

    # Number the meta entries by their position in the project history.
    # Meta entries are processed in newest-first order; reverse so they
    # number from oldest first.
    meta_entries_oldest_first = [e for e in reversed(entries) if e["filename"].startswith("meta-")]
    for n, e in enumerate(meta_entries_oldest_first, start=1):
        # Rename meta-XXX-cycles-...md to meta-NN.md (preserve cycle range)
        old_name = e["filename"]
        m = re.match(r"meta-\d+-cycles-(\d+)-(\d+)\.md", old_name)
        if m:
            new_name = f"meta-{n:02d}-cycles-{m.group(1)}-{m.group(2)}.md"
        else:
            new_name = f"meta-{n:02d}.md"
        e["filename"] = new_name

    LOG_DIR.mkdir(exist_ok=True)

    # Write entries to disk
    for e in entries:
        path = LOG_DIR / e["filename"]
        path.write_text(e["body"])

    # Build README.md index, newest-first.
    # Sort by sort_key descending (which is cycle * 10 for cycles,
    # cycle * 10 + 1 for meta — so meta-after-cycle-window comes
    # after the last cycle of that window in newest-first order).
    entries_newest_first = sorted(entries, key=lambda e: e["sort_key"], reverse=True)

    readme_lines = [
        header,
        "",
        "## Index (newest first)",
        "",
    ]
    for e in entries_newest_first:
        readme_lines.append(f"- [{e['title']}]({e['filename']})")

    (LOG_DIR / "README.md").write_text("\n".join(readme_lines) + "\n")

    print(f"Migrated {len(entries)} entries into {LOG_DIR}/")
    print(f"  Cycles: {sum(1 for e in entries if e['filename'].startswith('cycle-'))}")
    print(f"  Meta-reviews: {sum(1 for e in entries if e['filename'].startswith('meta-'))}")
    print(f"  Misc: {sum(1 for e in entries if e['filename'].startswith('misc-'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
