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
        "LOG.md",
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
