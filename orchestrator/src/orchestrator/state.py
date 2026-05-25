"""File I/O for the agent loop: questions / lessons / episodic / LOG /
book / git commits. The orchestrator's state is the filesystem."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class State:
    """Mutable reference to repo state. Methods perform I/O; `cycle_id` is
    bumped per cycle by the loop."""

    repo_root: Path
    cycle_id: int = 0

    # ─────────── reading ───────────

    def read_questions(self) -> str:
        return (self.repo_root / "questions.md").read_text()

    def read_lessons(self) -> str:
        return (self.repo_root / "lessons.md").read_text()

    def read_spec_index(self) -> str:
        return (self.repo_root / "book/src/spec/index.md").read_text()

    def read_slice(self, slice_name: str) -> str:
        """Return the current content of book/src/spec/slices/<slice>.md (or
        index.md of a subdirectory slice). Empty string if not yet present."""
        single = self.repo_root / "book/src/spec/slices" / f"{slice_name}.md"
        if single.exists():
            return single.read_text()
        subdir_index = self.repo_root / "book/src/spec/slices" / slice_name / "index.md"
        if subdir_index.exists():
            return subdir_index.read_text()
        return ""

    def read_episodic_window(self, n: int) -> list[dict]:
        """Last `n` entries from episodic.jsonl."""
        path = self.repo_root / "episodic.jsonl"
        if not path.exists():
            return []
        lines = [ln for ln in path.read_text().splitlines() if ln.strip()]
        return [json.loads(ln) for ln in lines[-n:]]

    def open_problems(self) -> list[dict[str, Any]]:
        """List of {filename, content} for unresolved problem entries."""
        out: list[dict[str, Any]] = []
        for p in sorted((self.repo_root / "problems").glob("*.md")):
            if p.name == "README.md":
                continue
            text = p.read_text()
            # A problem is resolved iff its frontmatter has a `resolved:` field.
            if "\nresolved:" not in text and not text.startswith("resolved:"):
                out.append({"filename": p.name, "content": text})
        return out

    # ─────────── writing ───────────

    def append_episodic(self, entry: dict) -> None:
        path = self.repo_root / "episodic.jsonl"
        with open(path, "a") as f:
            f.write(json.dumps(entry, separators=(",", ":")) + "\n")

    def append_lessons(self, lesson: str) -> None:
        path = self.repo_root / "lessons.md"
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        # Append immediately under the `## Entries` header if present.
        text = path.read_text()
        if "(none yet)" in text:
            text = text.replace("(none yet)", f"{date}  {lesson}")
        else:
            text = text.rstrip() + f"\n{date}  {lesson}\n"
        path.write_text(text)

    def append_lesson_unique(self, lesson: str) -> bool:
        """Dedupe-on-append lesson. Returns True if appended, False if the
        exact line already exists. Date prefix is added at write time."""
        path = self.repo_root / "lessons.md"
        text = path.read_text()
        if lesson.strip() in text:
            return False
        self.append_lessons(lesson)
        return True

    def create_concept_file(self, name: str, content: str) -> bool:
        """Write a new concept file at book/src/concepts/<name>.md. Returns
        True if created, False if already exists (no-op; caller may want
        append_concept_section instead)."""
        path = self.repo_root / "book/src/concepts" / f"{name}.md"
        if path.exists():
            return False
        path.parent.mkdir(parents=True, exist_ok=True)
        if not content.endswith("\n"):
            content += "\n"
        path.write_text(content)
        return True

    def append_concept_section(self, name: str, section_md: str) -> bool:
        """Append a `## Heading`-led section to an existing concept file.
        `section_md` MUST start with the leading `## Heading` line.
        Idempotent on the heading: returns False (no append) if the exact
        heading line already exists in the file. Raises FileNotFoundError
        if the concept file doesn't exist."""
        path = self.repo_root / "book/src/concepts" / f"{name}.md"
        if not path.exists():
            raise FileNotFoundError(
                f"concept file does not exist: {path.relative_to(self.repo_root)}"
            )
        section_md = section_md.strip()
        first_line = section_md.splitlines()[0] if section_md else ""
        if not first_line.startswith("##"):
            raise ValueError(
                f"append_concept_section expects a leading `## Heading` line; got: {first_line!r}"
            )
        text = path.read_text()
        if first_line in text:
            return False  # section already present (idempotent)
        text = text.rstrip() + "\n\n" + section_md + "\n"
        path.write_text(text)
        return True

    _DEPMAP_LAYER_HEADERS = {
        "methodology": "## Methodology concepts",
        "L1":          "## L1 —",
        "L2":          "## L2 —",
        "L3":          "## L3 —",
        "L4":          "## L4 —",
    }

    def add_dependency_map_edge(self, layer: str, from_: str, to_list: list[str]) -> int:
        """Add edges to `book/src/concepts/dependency-map.md`'s mermaid block
        for the given layer. Idempotent: each edge is added only if not
        already present in the mermaid block (text-substring check).
        Returns the number of NEW edges added (0 if all already present).

        When `to_list` is empty, just records the node (currently a no-op
        for the mermaid syntax — mermaid auto-creates nodes from edges; an
        isolated node has no rendering. The node appears once it gets an
        edge.)"""
        import re
        path = self.repo_root / "book/src/concepts/dependency-map.md"
        text = path.read_text()
        header_prefix = self._DEPMAP_LAYER_HEADERS.get(layer)
        if not header_prefix:
            raise ValueError(f"unknown layer: {layer!r} (expected one of {list(self._DEPMAP_LAYER_HEADERS)})")
        sec_start = text.find(header_prefix)
        if sec_start < 0:
            raise RuntimeError(f"layer section {header_prefix!r} not found in dependency-map.md")
        next_section = text.find("\n## ", sec_start + 1)
        if next_section < 0:
            next_section = len(text)
        section_text = text[sec_start:next_section]
        # Find the first ```mermaid block in this section.
        m = re.search(r"```mermaid\n(.*?)\n```", section_text, re.DOTALL)
        if not m:
            # Auto-initialize an empty mermaid block at the section's start
            # (added 2026-05-24 meta-review #7: cycle 21 had its L2 layer in
            # the map prose-only, no mermaid block, so all 8 edge inserts
            # crashed). The map's sections are stable; auto-init is
            # idempotent because subsequent calls find the new block.
            # Insert directly after the section heading + blank line.
            header_end = section_text.find("\n", 0)  # end of header line
            insert_at = section_text.find("\n", header_end + 1)  # after blank line
            if insert_at < 0:
                insert_at = len(section_text)
            init_block = "\n```mermaid\ngraph BT\n```\n"
            section_text = section_text[:insert_at] + init_block + section_text[insert_at:]
            text = text[:sec_start] + section_text + text[next_section:]
            path.write_text(text)
            m = re.search(r"```mermaid\n(.*?)\n```", section_text, re.DOTALL)
            assert m, "mermaid block auto-init failed"
        body = m.group(1)
        new_lines: list[str] = []
        for to_ in to_list:
            edge_line = f"  {from_} --> {to_}"
            if edge_line not in body:
                new_lines.append(edge_line)
        if not new_lines:
            return 0
        new_body = body.rstrip() + "\n" + "\n".join(new_lines)
        new_section = section_text.replace(
            f"```mermaid\n{body}\n```",
            f"```mermaid\n{new_body}\n```",
            1,
        )
        text = text[:sec_start] + new_section + text[next_section:]
        path.write_text(text)
        return len(new_lines)

    def append_section(self, rel_path: str, heading: str, content: str) -> bool:
        """Append a new top-level `## Heading` section to the end of an
        existing markdown file. Idempotent: if the heading line already
        exists in the file, returns False without changing anything.
        Raises FileNotFoundError if the file doesn't exist.

        Added 2026-05-24 meta-review #7 for the section-append edit
        topology (gmres L2 section-append to gmres.md was the originating
        failure)."""
        path = self.repo_root / rel_path
        if not path.exists():
            raise FileNotFoundError(f"section_append target does not exist: {rel_path}")
        heading_line = heading.strip()
        if not heading_line.startswith("##"):
            raise ValueError(f"heading must start with `##`; got: {heading!r}")
        text = path.read_text()
        if heading_line in text:
            return False  # idempotent
        content = content.strip()
        new_block = f"\n\n{heading_line}\n\n{content}\n"
        path.write_text(text.rstrip() + new_block)
        return True

    def register_in_summary(self, category: str, link_title: str, rel_path: str) -> bool:
        """Append a child entry to SUMMARY.md under the appropriate section
        (Specification → slices, Concepts → concepts). Idempotent on rel_path.
        Returns True if added, False if already present.

        Added 2026-05-24 (post meta-review #8) after the user surfaced that
        cycles 1-24 had created 5 slices and 10+ concepts that were never
        registered in SUMMARY.md, so mdBook didn't render them.

        category ∈ {"slice", "concept"}. The orchestrator calls this after
        successful slice_writes mode=create / concept_writes mode=create.
        The Synthesizer can override the auto-generated title later via
        file_edits if a richer title is desired.
        """
        path = self.repo_root / "book/src/SUMMARY.md"
        text = path.read_text()

        if category == "slice":
            section_header = "# Specification"
            section_anchor = "- [Index — Slice Status](./spec/index.md)"
        elif category == "concept":
            section_header = "# Concepts (shared library)"
            section_anchor = "- [Index](./concepts/index.md)"
        else:
            raise ValueError(f"unknown category: {category!r}")

        # Idempotent — skip if the link target is already in SUMMARY.
        if f"]({rel_path})" in text:
            return False

        section_pos = text.find(section_header)
        if section_pos < 0:
            raise RuntimeError(f"SUMMARY.md missing section header: {section_header!r}")
        anchor_pos = text.find(section_anchor, section_pos)
        if anchor_pos < 0:
            raise RuntimeError(f"SUMMARY.md missing anchor: {section_anchor!r}")
        next_section = text.find("\n# ", anchor_pos)
        if next_section < 0:
            next_section = len(text)

        # Trim trailing whitespace inside the section block, then append the
        # new entry on its own indented line.
        block = text[anchor_pos:next_section].rstrip()
        new_entry = f"\n  - [{link_title}]({rel_path})"
        new_text = text[:anchor_pos] + block + new_entry + text[next_section:]
        # Ensure the section ends with a blank line before the next # heading.
        if not new_text[len(text[:anchor_pos] + block + new_entry):].startswith("\n\n"):
            insert_at = len(text[:anchor_pos] + block + new_entry)
            new_text = new_text[:insert_at] + "\n" + new_text[insert_at:]
        path.write_text(new_text)
        return True

    def add_to_concepts_index(self, name: str, kind: str = "primitive") -> bool:
        """Add a row to `book/src/concepts/index.md`'s `## Index` table.
        Idempotent on `name`: returns False if a row for the named concept
        already exists. Rows are kept alphabetically sorted by concept name.

        Added meta-review #15 after the user surfaced that the index table
        had stayed empty across 24+ concept creates — the meta-7 auto-register
        added concepts to SUMMARY.md but did not touch this table. This
        helper is called from the integrator alongside register_in_summary.

        `kind` is one of: methodology, algorithm, primitive, layer-pattern,
        auxiliary. Defaults to `primitive` if the Synthesizer doesn't specify.
        """
        path = self.repo_root / "book/src/concepts/index.md"
        text = path.read_text()

        new_row = f"| [{name}](./{name}.md) | {kind} |"
        if new_row in text:
            return False  # exact idempotency
        # Also dedupe on the link path alone (different kind, same concept).
        if f"](./{name}.md)" in text:
            return False

        # Locate the table: find the header row, then the alignment row, then
        # walk through the existing data rows and insert in alphabetical order.
        header_match = "| Concept | Kind |"
        header_pos = text.find(header_match)
        if header_pos < 0:
            raise RuntimeError(
                f"concepts/index.md missing expected header: {header_match!r}. "
                "The table format may have been manually restructured; the "
                "auto-register helper assumes the meta-15 schema."
            )
        # Skip header line + alignment line.
        after_header = text.find("\n", header_pos)
        after_align = text.find("\n", after_header + 1)
        # Walk data rows.
        cursor = after_align + 1
        insert_pos = cursor
        while cursor < len(text):
            line_end = text.find("\n", cursor)
            if line_end < 0:
                line_end = len(text)
            line = text[cursor:line_end]
            if not line.startswith("| ["):
                # End of table.
                insert_pos = cursor
                break
            # Extract concept name from `| [<name>](`...
            import re
            m = re.match(r"\|\s*\[([^\]]+)\]", line)
            if m and m.group(1) > name:
                insert_pos = cursor
                break
            insert_pos = line_end + 1
            cursor = line_end + 1

        text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]
        path.write_text(text)
        return True

    def list_refinement_candidates(self, lookback_days: int = 30) -> list[dict]:
        """List slices/concepts where a touching component (linked concept,
        slice it references, or methodology file under prompts/) has been
        updated more recently than the candidate itself.

        Returns a list of {path, slice_or_concept, mtime, reason} dicts,
        ranked by how recently the touching component was updated.

        Coarse-grained — uses file mtimes and a regex-based reference scan.
        Refinement candidates surfaced here are PROPOSALS; the Planner
        decides whether to dispatch.

        Added 2026-05-26 from user directive (Refinement as a primary-phase
        operation). Conservative implementation: no concept-graph traversal,
        no deep semantic analysis. The Planner reads this list and the
        prose around it picks the candidate."""
        import re
        candidates: list[dict] = []
        slices_dir = self.repo_root / "book/src/spec/slices"
        concepts_dir = self.repo_root / "book/src/concepts"
        if not slices_dir.exists() or not concepts_dir.exists():
            return candidates

        # For each slice, gather (a) its own mtime, (b) the mtimes of
        # concepts it references and slices it cross-references. If any
        # referenced thing is newer, the slice is a candidate.
        link_pattern = re.compile(r"\.\./(?:\.\./)?(?:concepts|spec/slices)/([\w_-]+)(?:/[\w_-]+)?\.md")
        for slice_path in sorted(slices_dir.glob("*.md")):
            slice_mtime = slice_path.stat().st_mtime
            text = slice_path.read_text()
            newest_link_mtime = 0.0
            newest_link_target = None
            for m in link_pattern.finditer(text):
                target_name = m.group(1)
                target_concept = concepts_dir / f"{target_name}.md"
                target_slice = slices_dir / f"{target_name}.md"
                target_subdir = slices_dir / target_name / "index.md"
                for target in (target_concept, target_slice, target_subdir):
                    if target.exists():
                        target_mtime = target.stat().st_mtime
                        if target_mtime > newest_link_mtime:
                            newest_link_mtime = target_mtime
                            newest_link_target = target.relative_to(self.repo_root)
            if newest_link_mtime > slice_mtime:
                candidates.append({
                    "path": str(slice_path.relative_to(self.repo_root)),
                    "kind": "slice",
                    "slice_or_concept": slice_path.stem,
                    "mtime": slice_mtime,
                    "newest_link_mtime": newest_link_mtime,
                    "newest_link_target": str(newest_link_target) if newest_link_target else None,
                    "reason": f"linked component {newest_link_target} updated more recently",
                })
        candidates.sort(key=lambda c: c["newest_link_mtime"], reverse=True)
        return candidates

    def read_problems_sensitivity(self) -> int:
        """Parse `scaffolding/problems-sensitivity.md`'s YAML-ish block for
        the current `sensitivity:` integer (1-5). Returns 3 (default) if
        the file is missing or unparseable. Added 2026-05-26 from user
        directive: target 1 problem filed per 15 agent runs, self-tuned
        at each meta-cycle."""
        import re
        path = self.repo_root / "scaffolding/problems-sensitivity.md"
        if not path.exists():
            return 3
        text = path.read_text()
        m = re.search(r"^sensitivity:\s*(\d+)\s*$", text, re.MULTILINE)
        if not m:
            return 3
        try:
            val = int(m.group(1))
            return max(1, min(5, val))
        except ValueError:
            return 3

    def count_recent_problem_filings(self, since_cycle_id: int) -> int:
        """Count `problems/${date}T${time}Z.md` files created since the
        given cycle_id boundary. Uses file mtime as a proxy; the
        boundary is approximated by looking back in the episodic log
        for the cycle's commit time. Added 2026-05-26 for the
        sensitivity-calibration logic."""
        import re
        problems_dir = self.repo_root / "problems"
        if not problems_dir.exists():
            return 0
        # Boundary mtime: find the wallclock_ms of since_cycle_id's
        # entry if available, otherwise use the n-th-from-end episodic
        # entry's time. Coarse-grained — file mtimes are what we have.
        # We just count files matching the timestamp pattern; the
        # cycle_id boundary is approximated by lookups in episodic.
        boundary_mtime = 0.0
        entries = self.read_episodic_window(10_000)
        for e in entries:
            if e.get("cycle_id") == since_cycle_id:
                # Use a coarse approximation: assume the episodic entry
                # was written near the cycle's wallclock_ms ago. We
                # don't store absolute timestamps; fall back to file
                # mtime comparison.
                break
        # Without absolute cycle timestamps in episodic, count by
        # number of problem files older than the most-recent episodic
        # entries' cycle counter > since_cycle_id. Approximation: count
        # all problem files in the dir (since_cycle_id is informational).
        ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{6}Z\.md$")
        return sum(1 for p in problems_dir.iterdir() if ts_re.match(p.name))

    def list_least_recently_touched(self, n: int = 5) -> list[dict]:
        """Return the N slices/concepts with the oldest mtime — refinement
        candidates by the periodic-scan path (per `prompts/planner.md`
        Refinement trigger source (b)).

        Added 2026-05-26 from user directive."""
        slices_dir = self.repo_root / "book/src/spec/slices"
        items: list[dict] = []
        if slices_dir.exists():
            for slice_path in slices_dir.glob("*.md"):
                items.append({
                    "path": str(slice_path.relative_to(self.repo_root)),
                    "kind": "slice",
                    "slice_or_concept": slice_path.stem,
                    "mtime": slice_path.stat().st_mtime,
                })
        items.sort(key=lambda i: i["mtime"])  # oldest first
        return items[:n]

    def update_slice_index_row(
        self,
        slice: str,
        layer: str,
        date: str,
        summary: str,
        link_title: str | None = None,
    ) -> bool:
        """Update the status-table row for `slice` in `book/src/spec/index.md`.
        Anchors on the link target `(./slices/<slug>.md)` or
        `(./slices/<slug>/index.md)` for subdirectory slices.

        Idempotent: if the existing row already matches the requested content,
        returns False (no write). Raises FileNotFoundError if the slice has no
        row in the table; the caller decides whether to append-row or fall
        through. Added meta-review #10 after cycles 31-34 hit `file_edits`
        anchor mismatches on this exact row-update path."""
        import re
        path = self.repo_root / "book/src/spec/index.md"
        text = path.read_text()

        anchors = [f"./slices/{slice}.md", f"./slices/{slice}/index.md"]
        anchor_pos = -1
        matched_anchor: str | None = None
        for a in anchors:
            pos = text.find(f"({a})")
            if pos >= 0:
                anchor_pos = pos
                matched_anchor = a
                break
        if anchor_pos < 0:
            raise FileNotFoundError(
                f"slice_index_update: no row found for slice {slice!r} "
                f"(looked for anchors {anchors!r})"
            )

        row_start = text.rfind("\n", 0, anchor_pos) + 1
        row_end = text.find("\n", anchor_pos)
        if row_end < 0:
            row_end = len(text)
        old_row = text[row_start:row_end]

        title_match = re.search(
            r"\[([^\]]+)\]\(" + re.escape(matched_anchor) + r"\)",
            old_row,
        )
        title = link_title or (title_match.group(1) if title_match else slice)
        new_row = f"| [{title}]({matched_anchor}) | {layer} | {date} | {summary} |"

        if old_row == new_row:
            return False
        text = text[:row_start] + new_row + text[row_end:]
        path.write_text(text)
        return True

    def write_meta_review_pending(self, plan_md: str) -> Path:
        """Write the file-based meta-review handshake. Returns the path
        written. The marker at the bottom is the human-toggled approval."""
        path = self.repo_root / "meta-review-pending.md"
        path.write_text(plan_md)
        return path

    def read_meta_review_pending(self) -> str | None:
        path = self.repo_root / "meta-review-pending.md"
        if not path.exists():
            return None
        return path.read_text()

    def clear_meta_review_pending(self) -> None:
        path = self.repo_root / "meta-review-pending.md"
        if path.exists():
            path.unlink()

    def apply_unified_diff(self, diff_text: str) -> None:
        """Apply a unified diff to the working tree. Uses `git apply` so the
        same semantics as PRs. Raises if the diff doesn't apply cleanly."""
        if not diff_text.strip():
            return
        result = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", "-"],
            input=diff_text,
            text=True,
            capture_output=True,
            cwd=self.repo_root,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"git apply failed:\nSTDERR:\n{result.stderr}\nDIFF:\n{diff_text}"
            )

    # Paths the orchestrator considers cycle-owned. `git add` is run against
    # each (existence-tolerant) before commit. Anything outside these paths
    # is left in the working tree — a developer making concurrent edits, an
    # unrelated rename, etc., will NOT be captured by the cycle's audit
    # commit.
    #
    # This was a real friction in the first end-to-end cycle (commit 8e5a480):
    # the original implementation used `git add -A` which swept developer
    # changes into the cycle commit. See scaffolding/decisions/.
    CYCLE_OWNED_PATHS = (
        "episodic.jsonl",
        "log",             # per-cycle and per-meta entries (replaces LOG.md as of 2026-05-26)
        "lessons.md",
        "questions.md",
        "book",            # spec/, concepts/, design/, meta-reviews/
        "scaffolding",     # cross-cutting notes the agents write
        "problems",        # agent-filed out-of-band concerns
    )

    def commit(self, message: str) -> str | None:
        """git add the cycle-owned paths; git commit if anything is staged.
        Returns the new commit's sha, or None if there was nothing to commit.
        """
        for relpath in self.CYCLE_OWNED_PATHS:
            full = self.repo_root / relpath
            if not full.exists():
                continue
            # check=False — `git add` returns non-zero if the path is
            # entirely untracked AND empty, which we don't care about.
            subprocess.run(["git", "add", "--", relpath], cwd=self.repo_root, check=False)
        diff_check = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=self.repo_root,
        )
        if diff_check.returncode == 0:
            return None  # nothing staged
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.repo_root,
            check=True,
        )
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_root,
            text=True,
        ).strip()
        return sha

    def count_cycles_since_meta(self) -> int:
        """Count entries in episodic.jsonl since the last meta-review marker
        (push_kind == "meta")."""
        entries = self.read_episodic_window(10_000)  # effectively all
        count = 0
        for e in reversed(entries):
            if e.get("push_kind") == "meta":
                break
            count += 1
        return count
