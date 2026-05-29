#!/usr/bin/env python3
"""citecheck — mechanical citation-range checker for the Palace dissection.

Validates `path:lo-hi` (or `path:N`) citations against the local `reference/`
source checkout. Two complementary checks:

  1. BOUNDS lint (always): does the file resolve, and is the line range
     in-bounds (1 <= lo <= hi <= file_length)? Catches mis-paths, off-the-end
     ranges, and inverted ranges.

  2. ANCHOR drift (opt-in, per citation): given an expected anchor string the
     citation is supposed to point at, find where it actually is. If it falls
     outside [lo, hi], report DRIFT(+/-N) with the nearest actual line and a
     suggested corrected range. This is the mechanical catch for the recurring
     "pinpoint citation off by +/-1-2 lines while the wide range stays correct"
     friction (friction-ledger `producer-citation-drift-verify-not-self-invoked`).

Citation paths are resolved relative to the target repo roots (in order):
`reference/palace`, `reference/bunsen`, `reference/burn`, then `reference`
itself. The first root under which the file exists wins. Palace citations
(`palace/linalg/foo.cpp`, `test/unit/bar.cpp`) resolve under `reference/palace/`.

This is a LINT, not a semantic checker: it confirms a citation points where it
claims to (and, with an anchor, at what it claims to) — it cannot confirm the
cited lines *mean* what the prose says. Pair it with human/agent reading.

Exit code: 0 if every citation is OK, 1 if any citation fails (use as a
pre-integration gate). See README.md for invocation patterns.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Citation token: PATH:LO-HI or PATH:N. PATH has no whitespace and must contain
# a dotted extension so we don't match bare `word:123` prose (e.g. "line:5").
CITATION_RE = re.compile(
    r"(?P<path>[\w./+-]+\.[A-Za-z0-9_+]+):(?P<lo>\d+)(?:-(?P<hi>\d+))?"
)

# Source roots (reference/ checkouts) + the book artifact root, in resolution
# order. `book/src` lets the lint also validate intra-book cross-reference line
# targets (e.g. `dot.md:34`, `book/src/L2/index.md:26`).
DEFAULT_ROOTS = ("reference/palace", "reference/bunsen", "reference/burn",
                 "reference", "book/src")

# Extensions we index for basename-shorthand resolution. Agents routinely write
# `vector.cpp:263` in prose after giving the full path once; bare basenames are
# resolved by unique-match search under the roots.
INDEX_EXTS = {".cpp", ".hpp", ".h", ".cc", ".c", ".cu", ".rs", ".md"}

# Status values, ordered worst-to-best for summary purposes.
ST_FILE_MISSING = "FILE_MISSING"
ST_AMBIGUOUS = "AMBIGUOUS"
ST_OOB = "OOB"
ST_ANCHOR_NOT_FOUND = "ANCHOR_NOT_FOUND"
ST_DRIFT = "DRIFT"
ST_OK = "OK"

FAIL_STATUSES = {ST_FILE_MISSING, ST_AMBIGUOUS, ST_OOB, ST_ANCHOR_NOT_FOUND, ST_DRIFT}


@dataclass
class Citation:
    raw: str
    path: str
    lo: int
    hi: int
    anchor: str | None = None
    anchor_is_regex: bool = False


@dataclass
class Result:
    citation: Citation
    status: str
    resolved: str | None = None  # repo-relative resolved path (root + path)
    file_lines: int | None = None
    detail: str = ""
    anchor_lines: list[int] = field(default_factory=list)
    suggested: str | None = None  # suggested corrected `path:lo-hi`

    @property
    def ok(self) -> bool:
        return self.status == ST_OK


class Resolver:
    """Resolves a citation path to a file under the candidate roots.

    Full paths (`palace/linalg/vector.cpp`) resolve directly. Bare basenames
    (`vector.cpp`) — the shorthand agents use in prose — resolve by unique-match
    search over a lazily-built basename index; multiple matches are AMBIGUOUS.
    """

    def __init__(self, project_root: Path, roots: tuple[str, ...]):
        self.project_root = project_root
        self.roots = roots
        self._index: dict[str, list[Path]] | None = None

    def _build_index(self) -> dict[str, list[Path]]:
        # De-dupe by real path: the roots overlap (reference/palace is under
        # reference), so the same physical file is reachable via several roots.
        index: dict[str, dict[Path, Path]] = {}
        for root in self.roots:
            base = self.project_root / root
            if not base.is_dir():
                continue
            for f in base.rglob("*"):
                if f.is_file() and f.suffix in INDEX_EXTS:
                    index.setdefault(f.name, {})[f.resolve()] = f
        # Collapse each basename's de-duped real-path set to a path list.
        return {name: list(by_real.values()) for name, by_real in index.items()}

    def resolve(self, path: str) -> tuple[Path | None, list[Path]]:
        """Return (resolved_file_or_None, candidates). `candidates` is non-empty
        only for an ambiguous bare-basename match."""
        # Fast path: full path relative to the project root, then under each root.
        direct = self.project_root / path
        if direct.is_file():
            return direct, []
        for root in self.roots:
            candidate = self.project_root / root / path
            if candidate.is_file():
                return candidate, []
        # Fallback: bare basename (no directory component) → unique-match search.
        if "/" not in path:
            if self._index is None:
                self._index = self._build_index()
            hits = self._index.get(path, [])
            if len(hits) == 1:
                return hits[0], []
            if len(hits) > 1:
                return None, hits
        return None, []


def find_anchor(lines: list[str], anchor: str, is_regex: bool) -> list[int]:
    """Return 1-based line numbers where `anchor` occurs."""
    if is_regex:
        pat = re.compile(anchor)
        return [i for i, ln in enumerate(lines, 1) if pat.search(ln)]
    return [i for i, ln in enumerate(lines, 1) if anchor in ln]


def nearest(hits: list[int], lo: int, hi: int) -> tuple[int, int]:
    """Nearest hit to the range [lo, hi] and its signed distance from the
    nearest boundary (0 if a hit is inside the range)."""
    best_line = hits[0]
    best_delta = None
    for h in hits:
        if lo <= h <= hi:
            return h, 0
        delta = h - lo if h < lo else h - hi  # signed: negative = before range
        if best_delta is None or abs(delta) < abs(best_delta):
            best_delta, best_line = delta, h
    return best_line, best_delta or 0


def check(cit: Citation, resolver: Resolver) -> Result:
    resolved, candidates = resolver.resolve(cit.path)
    if resolved is None:
        if candidates:
            rels = [str(c.relative_to(resolver.project_root)) for c in candidates]
            return Result(cit, ST_AMBIGUOUS,
                          detail=f"basename `{cit.path}` matches {len(rels)} files; "
                                 f"use a full path. candidates: {', '.join(rels)}")
        return Result(cit, ST_FILE_MISSING,
                      detail=f"no file `{cit.path}` under {', '.join(resolver.roots)}")

    rel = str(resolved.relative_to(resolver.project_root))
    lines = resolved.read_text(errors="replace").splitlines()
    n = len(lines)

    # Bounds check.
    if cit.lo < 1 or cit.hi < cit.lo or cit.hi > n:
        return Result(cit, ST_OOB, resolved=rel, file_lines=n,
                      detail=f"range {cit.lo}-{cit.hi} out of bounds (file has {n} lines)")

    if cit.anchor is None:
        return Result(cit, ST_OK, resolved=rel, file_lines=n,
                      detail=f"range in bounds (file has {n} lines)")

    # Anchor drift check.
    hits = find_anchor(lines, cit.anchor, cit.anchor_is_regex)
    if not hits:
        return Result(cit, ST_ANCHOR_NOT_FOUND, resolved=rel, file_lines=n,
                      detail=f"anchor {cit.anchor!r} not found in file")
    if any(cit.lo <= h <= cit.hi for h in hits):
        inside = [h for h in hits if cit.lo <= h <= cit.hi]
        return Result(cit, ST_OK, resolved=rel, file_lines=n, anchor_lines=hits,
                      detail=f"anchor at line(s) {inside} within range {cit.lo}-{cit.hi}")
    line, delta = nearest(hits, cit.lo, cit.hi)
    sign = f"{'+' if delta > 0 else ''}{delta}"
    span = cit.hi - cit.lo
    sug_lo = line
    sug_hi = line + span
    return Result(cit, ST_DRIFT, resolved=rel, file_lines=n, anchor_lines=hits,
                  detail=f"anchor at line {line}, {sign} outside range {cit.lo}-{cit.hi}",
                  suggested=f"{cit.path}:{sug_lo}" + (f"-{sug_hi}" if span else ""))


def parse_citation(token: str) -> Citation | None:
    m = CITATION_RE.fullmatch(token.strip())
    if not m:
        return None
    lo = int(m["lo"])
    hi = int(m["hi"]) if m["hi"] else lo
    return Citation(raw=token.strip(), path=m["path"], lo=lo, hi=hi)


def scan_markdown(text: str) -> list[Citation]:
    """Extract every citation token from free text (e.g. a CYCLE.md)."""
    seen: dict[str, Citation] = {}
    for m in CITATION_RE.finditer(text):
        lo = int(m["lo"])
        hi = int(m["hi"]) if m["hi"] else lo
        raw = m.group(0)
        # de-dupe identical tokens; keep first occurrence
        seen.setdefault(raw, Citation(raw=raw, path=m["path"], lo=lo, hi=hi))
    return list(seen.values())


def parse_batch(text: str) -> list[Citation]:
    """One citation per line: `PATH:LO-HI` optionally `<TAB>ANCHOR`.
    A leading `re:` on the anchor marks it as a regex. Blank/`#` lines skipped."""
    cits: list[Citation] = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t", 1)
        cit = parse_citation(parts[0])
        if cit is None:
            print(f"warning: unparseable citation line: {line!r}", file=sys.stderr)
            continue
        if len(parts) == 2 and parts[1].strip():
            anchor = parts[1].strip()
            if anchor.startswith("re:"):
                cit.anchor = anchor[3:]
                cit.anchor_is_regex = True
            else:
                cit.anchor = anchor
        cits.append(cit)
    return cits


SYMBOLS = {
    ST_OK: "ok  ",
    ST_DRIFT: "DRIFT",
    ST_OOB: "OOB ",
    ST_FILE_MISSING: "MISS",
    ST_AMBIGUOUS: "AMBIG",
    ST_ANCHOR_NOT_FOUND: "NOANC",
}


def render_text(results: list[Result], show: bool, resolver: Resolver,
                quiet: bool) -> None:
    for r in results:
        if quiet and r.ok:
            continue
        sym = SYMBOLS.get(r.status, r.status)
        line = f"[{sym}] {r.citation.raw}"
        if r.citation.anchor:
            kind = "re" if r.citation.anchor_is_regex else "lit"
            line += f"  (anchor {kind}: {r.citation.anchor!r})"
        line += f"\n       {r.detail}"
        if r.resolved and r.resolved != r.citation.path:
            line += f"\n       resolved: {r.resolved}"
        if r.suggested:
            line += f"\n       suggested: {r.suggested}"
        print(line)
        if show and r.resolved and r.status in (ST_OK, ST_DRIFT, ST_ANCHOR_NOT_FOUND):
            _show_lines(r, resolver)


def _show_lines(r: Result, resolver: Resolver) -> None:
    resolved, _ = resolver.resolve(r.citation.path)
    if resolved is None:
        return
    lines = resolved.read_text(errors="replace").splitlines()
    lo, hi = r.citation.lo, r.citation.hi
    for i in range(max(1, lo), min(len(lines), hi) + 1):
        print(f"       {i:>6} | {lines[i - 1]}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="citecheck",
        description="Mechanical citation-range checker against reference/ source.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("citations", nargs="*", default=[],
                     help="inline citation tokens, e.g. palace/linalg/vector.cpp:258-260")
    src.add_argument("--scan", metavar="FILE",
                     help="extract & bounds-check every citation in a markdown/CYCLE.md file")
    src.add_argument("--batch", metavar="FILE",
                     help="one `PATH:LO-HI[<TAB>ANCHOR]` per line ('-' for stdin)")
    ap.add_argument("--anchor", help="expected anchor for inline citations (drift check)")
    ap.add_argument("--regex", action="store_true",
                    help="treat --anchor as a regex")
    ap.add_argument("--show", action="store_true",
                    help="print the cited source lines for eyeball verification")
    ap.add_argument("--quiet", action="store_true", help="print only failing citations")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    ap.add_argument("--ref-root", default=None,
                    help="primary source root (default: reference/palace)")
    ap.add_argument("--project-root", default=None,
                    help="repo root holding reference/ (default: auto-detect)")
    args = ap.parse_args(argv)

    # Locate the project root (the dir containing reference/).
    if args.project_root:
        project_root = Path(args.project_root).resolve()
    else:
        project_root = Path(__file__).resolve().parents[2]  # tools/citecheck/.. -> repo

    roots: tuple[str, ...] = DEFAULT_ROOTS
    if args.ref_root:
        roots = (args.ref_root,) + tuple(r for r in DEFAULT_ROOTS if r != args.ref_root)

    # Gather citations.
    cits: list[Citation] = []
    if args.scan:
        cits = scan_markdown(Path(args.scan).read_text(errors="replace"))
        if not cits:
            print(f"no citations found in {args.scan}", file=sys.stderr)
    elif args.batch:
        text = sys.stdin.read() if args.batch == "-" else Path(args.batch).read_text()
        cits = parse_batch(text)
    else:
        for tok in args.citations:
            cit = parse_citation(tok)
            if cit is None:
                print(f"error: unparseable citation: {tok!r}", file=sys.stderr)
                return 2
            if args.anchor:
                cit.anchor = args.anchor
                cit.anchor_is_regex = args.regex
            cits.append(cit)

    if not cits:
        return 0

    resolver = Resolver(project_root, roots)
    results = [check(c, resolver) for c in cits]

    if args.json:
        payload = [{
            "raw": r.citation.raw, "path": r.citation.path,
            "lo": r.citation.lo, "hi": r.citation.hi,
            "anchor": r.citation.anchor, "status": r.status,
            "resolved": r.resolved, "file_lines": r.file_lines,
            "detail": r.detail, "anchor_lines": r.anchor_lines,
            "suggested": r.suggested,
        } for r in results]
        print(json.dumps(payload, indent=2))
    else:
        render_text(results, args.show, resolver, args.quiet)
        n_fail = sum(1 for r in results if not r.ok)
        n_ok = len(results) - n_fail
        print(f"\n{n_ok} ok, {n_fail} failing ({len(results)} citations checked).",
              file=sys.stderr)

    return 1 if any(not r.ok for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
