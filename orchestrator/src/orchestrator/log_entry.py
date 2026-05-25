"""Per-cycle log writers — rewritten 2026-05-26 from LOG.md prepend to log/
per-entry files. Each cycle and meta-review writes its own file under
`log/`; `log/README.md` indexes them newest-first. Avoids reading and
rewriting the full log on every cycle.

File naming:
- Cycles: `log/cycle-NNN.md` (NNN = zero-padded 3 digits, sorted by cycle_id).
- Meta-reviews: `log/meta-NN-cycles-A-B.md` (NN = sequential meta number).
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR_NAME = "log"


def _log_dir(repo_root: Path) -> Path:
    p = repo_root / LOG_DIR_NAME
    p.mkdir(exist_ok=True)
    return p


def write_cycle_log(
    *,
    repo_root: Path,
    cycle_id: int,
    entry_md: str,
) -> Path:
    """Write `entry_md` to `log/cycle-NNN.md` and update `log/README.md`."""
    log_dir = _log_dir(repo_root)
    path = log_dir / f"cycle-{cycle_id:03d}.md"
    path.write_text(entry_md.rstrip() + "\n")
    _update_index(repo_root)
    return path


def write_meta_log(
    *,
    repo_root: Path,
    cycle_range: tuple[int, int],
    entry_md: str,
) -> Path:
    """Write `entry_md` to `log/meta-NN-cycles-A-B.md` (NN derived by counting
    existing meta files + 1) and update `log/README.md`."""
    log_dir = _log_dir(repo_root)
    lo, hi = cycle_range
    existing_metas = sorted(log_dir.glob("meta-*.md"))
    n = len(existing_metas) + 1
    path = log_dir / f"meta-{n:02d}-cycles-{lo}-{hi}.md"
    # Overwrite if a meta file for the same cycle range already exists (idempotent re-run).
    for old in existing_metas:
        if old.name.endswith(f"cycles-{lo}-{hi}.md"):
            path = old
            break
    path.write_text(entry_md.rstrip() + "\n")
    _update_index(repo_root)
    return path


def _update_index(repo_root: Path) -> None:
    """Rebuild `log/README.md` as a newest-first index of `log/*.md` entries.
    Cycles sort by integer cycle id; meta entries sort by their cycle-range
    high-end (interleaved so meta-after-window-N comes after cycle-N)."""
    log_dir = _log_dir(repo_root)
    entries: list[tuple[int, str, str]] = []  # (sort_key, filename, title)

    cycle_re = re.compile(r"cycle-(\d+)\.md")
    meta_re = re.compile(r"meta-\d+-cycles-(\d+)-(\d+)\.md")

    for entry in log_dir.iterdir():
        if entry.name in ("README.md",):
            continue
        if not entry.is_file() or not entry.name.endswith(".md"):
            continue
        m_c = cycle_re.fullmatch(entry.name)
        m_m = meta_re.fullmatch(entry.name)
        # Read first H2 heading as the title
        try:
            head_line = next(
                (l for l in entry.read_text().splitlines() if l.startswith("## ")),
                None,
            )
        except Exception:
            head_line = None
        title = head_line[3:].strip() if head_line else entry.stem

        if m_c:
            cycle_id = int(m_c.group(1))
            sort_key = cycle_id * 10  # cycles before meta of same window
        elif m_m:
            cycle_end = int(m_m.group(2))
            sort_key = cycle_end * 10 + 1  # meta after last cycle
        else:
            sort_key = 0
        entries.append((sort_key, entry.name, title))

    entries.sort(key=lambda e: e[0], reverse=True)

    lines = [
        "# Cycle log",
        "",
        "Per-cycle and meta-review entries, one file each. Indexed newest-first below.",
        "",
        "Format: cycle entries (`cycle-NNN.md`) are written by the orchestrator after each cycle commits;",
        "meta-review entries (`meta-NN-cycles-A-B.md`) are written after each meta-review enactment.",
        "Full meta-review records (longer) live under `book/src/meta-reviews/`.",
        "",
        "## Index (newest first)",
        "",
    ]
    for _, filename, title in entries:
        lines.append(f"- [{title}]({filename})")
    (log_dir / "README.md").write_text("\n".join(lines) + "\n")


# ─────────── Entry formatters (unchanged) ───────────


def format_cycle_entry(
    *,
    cycle_id: int,
    push_kind: str,
    slice_name: str,
    edge: str | None,
    verdict: str,
    synthesis: str,
    friction: str | None,
    structural_change: str | None,
) -> str:
    """Build a per-cycle log entry."""
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    edge_part = f" [{edge}]" if edge else ""
    header = f"## {date} cycle-{cycle_id} — {push_kind} {slice_name}{edge_part} — {verdict}"
    body = [
        f"- Synthesis: {synthesis}",
        f"- Verdict: {verdict}.",
        f"- Friction: {friction or 'none'}.",
        f"- Structural change: {structural_change or 'none'}.",
    ]
    return header + "\n\n" + "\n".join(body) + "\n"


def format_meta_review_entry(
    *,
    review_date: str,
    cycle_range: tuple[int, int],
    status: str,
    push_breakdown: str,
    cascade_breakdown: str,
    plan_items_summary: str,
    recurring_patterns: str | None,
    record_path: str,
) -> str:
    """Build a meta-review log entry."""
    lo, hi = cycle_range
    header = f"## {review_date} meta-review (cycles {lo}–{hi}) — {status}"
    body = [
        f"- Window: {hi - lo + 1} cycles. Push breakdown: {push_breakdown}.",
        f"- Cascade: {cascade_breakdown}.",
        f"- Plan items enacted: {plan_items_summary}.",
        f"- Recurring patterns: {recurring_patterns or 'none'}.",
        f"- Full record: `{record_path}`.",
    ]
    return header + "\n\n" + "\n".join(body) + "\n"


# ─────────── Legacy LOG.md prepend (deprecated) ───────────
#
# Kept for backwards compatibility with any external caller. New code
# should use write_cycle_log() / write_meta_log() instead.


def prepend_log_entry(repo_root: Path, entry_md: str) -> None:
    """DEPRECATED. Use write_cycle_log() or write_meta_log() instead.
    Writes the entry to log/ (best-effort cycle/meta detection from header)."""
    # Detect cycle id from `## ... cycle-NNN ...` header
    first_line = entry_md.lstrip().splitlines()[0] if entry_md.strip() else ""
    cycle_match = re.search(r"cycle-(\d+)", first_line)
    meta_match = re.search(r"meta-review \(cycles (\d+)[–-](\d+)\)", first_line)
    if cycle_match:
        write_cycle_log(
            repo_root=repo_root, cycle_id=int(cycle_match.group(1)), entry_md=entry_md,
        )
    elif meta_match:
        write_meta_log(
            repo_root=repo_root,
            cycle_range=(int(meta_match.group(1)), int(meta_match.group(2))),
            entry_md=entry_md,
        )
    else:
        # Fallback: write as a misc entry
        log_dir = _log_dir(repo_root)
        slug = re.sub(r"[^\w-]+", "-", first_line[:60]).strip("-").lower() or "misc"
        (log_dir / f"misc-{slug}.md").write_text(entry_md.rstrip() + "\n")
        _update_index(repo_root)
