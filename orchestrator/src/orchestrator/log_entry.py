"""LOG.md prepend logic and entry formatters.

LOG.md structure (per Phase 2 spec):

    # Cycle log

    <header text>

    ---

    ## newest entry

    ...

    ## older entry

    ...

New entries go IMMEDIATELY BELOW the `---` separator, above prior entries.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

LOG_SEPARATOR = "\n---\n"


def prepend_log_entry(repo_root: Path, entry_md: str) -> None:
    """Insert `entry_md` immediately below the `---` separator in LOG.md.

    `entry_md` should be a complete entry (H2 header + body), without a
    leading or trailing blank line — this function handles spacing.
    """
    path = repo_root / "LOG.md"
    text = path.read_text()
    if LOG_SEPARATOR not in text:
        raise RuntimeError(
            "LOG.md is missing the `---` separator that anchors entries. "
            "The file may have been edited by hand in a way that broke the "
            "prepend protocol — restore the separator or recreate LOG.md "
            "from the Phase 2 seed."
        )
    before, after = text.split(LOG_SEPARATOR, 1)
    # `after` starts with a newline; "(no entries yet)" placeholder lives there
    # initially. We strip the placeholder if present.
    if after.strip() == "(no entries yet)":
        after = ""
    new = f"{before}{LOG_SEPARATOR}\n{entry_md.rstrip()}\n{after.lstrip(chr(10)) if after else ''}"
    path.write_text(new)


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
    """Build a per-cycle LOG.md entry."""
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
    """Build a meta-review LOG.md entry."""
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
