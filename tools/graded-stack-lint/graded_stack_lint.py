#!/usr/bin/env python3
"""graded_stack_lint — the two graded-stack linters (rank check + reachability GC).

Implements `METHODOLOGY-GRADED-STACK.md` §4 over the machine-readable scheme
defined in `book/src/methodology/graded-stack-scheme.md` (P0-A, the D1 contract).
One pass builds ONE typed dependency graph from `book/src/**/*.md` frontmatter;
two analyses run over it:

  1. RANK LINTER — Axis 1, well-foundedness. For every blocking (`depends-on`)
     edge u -> v, assert rank(u) <= rank(v) ("a node is at most as resolved as
     its least-resolved dependency", §1b). Reports rank VIOLATIONS, and emits the
     PROMOTION FRONTIER for free (nodes all of whose depends-on deps are already
     >= the node's own rank, i.e. nothing below blocks a promotion past that rank).

  2. REACHABILITY GC — Axis 2, liveness. Mark from the feature-root node-set (the
     `feature_root: seed` / legacy `status: seed` feature-spine columns) over
     `depends-on` edges. Unmarked nodes are GARBAGE (detritus / dead intent).
     Emits the detritus list + a per-file inbound-reference report.

Both analyses consume ONLY the blocking bit (`depends-on`); `reference` edges
constrain nothing and carry no liveness (§3). The optional edge `kind:` is
documentation the linter ignores.

INCREMENTAL-SAFE (hard requirement (a)). Most of the tree is not yet typed
(253/357 files pre-P1). A file with no rank/edge frontmatter is counted as an
"untyped" WARNING, never a hard error — the linters run cleanly throughout the
P1 rollout. Only genuine rank violations and (optionally, under --strict)
unresolved edge targets fail.

OUTPUT. Human-readable to stdout; `--json` emits a machine-parseable summary the
integrator-finalize consumes (graded-stack §8). Exit code 1 iff a rank violation
is found (or, with --strict, an unresolved depends-on target); untyped warnings
and detritus alone do NOT set a failing exit (they are informational pre-P1).

See README.md for invocation, the scheme grammar, and the migration-mapping the
edge reader implements.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# The resolution ladder (scheme §1). Numeric ranks; sub-ranks at 2.5.
# ---------------------------------------------------------------------------

RANK_VALUE = {
    "roadmap_goal": 0.0,
    "stub": 1.0,
    "rough-in": 2.0,
    "rough-in (test-coverage-bounded)": 2.5,
    "rough-in-test-coverage-bounded": 2.5,  # frontmatter-safe spelling
    "partly-constructive": 2.5,
    "firm": 3.0,
}

# Obstruction is a SEPARATE kind, itself rankable via obstruction_resolution
# (scheme §1f). These are the kind tokens, not ladder values.
OBSTRUCTION_KINDS = {"obstruction", "partial-obstruction"}

# The feature-root marker. A parallel axis, NOT a ladder rung (scheme §3).
ROOT_MARKER = "seed"


def rank_label(value: float | None) -> str:
    """Best human label for a numeric rank (used in diagnostics)."""
    if value is None:
        return "untyped"
    # exact-match a known token first
    for tok, v in RANK_VALUE.items():
        if v == value and tok not in (
            "rough-in-test-coverage-bounded",
        ):
            return tok
    return f"rank={value}"


# ---------------------------------------------------------------------------
# Minimal YAML-frontmatter reader.
#
# The frontmatter we parse is a small, regular subset: top-level `key: value`
# scalars, and the two block shapes that actually appear on disk —
#   key:
#     - item
#     - item
# and nested two-level blocks (the `edges:` block):
#   edges:
#     depends-on:
#       - target
#     reference:
#       - target
# plus the `{target: X, kind: Y}` inline-mapping list-item form for typed edges.
# We deliberately DON'T pull in PyYAML (the tools/ convention is stdlib-only,
# matching citecheck) — this hand reader covers exactly the scheme grammar and
# the three legacy representations, and nothing else.
# ---------------------------------------------------------------------------


def extract_frontmatter_block(text: str) -> str | None:
    """Return the raw YAML between the leading `---` fences, or None."""
    if not text.startswith("---"):
        return None
    # first line must be exactly --- (allow trailing whitespace)
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def _strip_inline_comment(s: str) -> str:
    """Drop a trailing ` # comment`. We only strip an unquoted ` #`."""
    # Conservative: only strip if there's a space-hash not inside quotes/parens.
    # Frontmatter qualifiers use parens ('(firm — ...)'), not '#', so this is safe.
    in_quote = None
    for i, ch in enumerate(s):
        if ch in ("'", '"'):
            if in_quote == ch:
                in_quote = None
            elif in_quote is None:
                in_quote = ch
        elif ch == "#" and in_quote is None and i > 0 and s[i - 1] == " ":
            return s[:i]
    return s


def _unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def parse_frontmatter(text: str) -> dict:
    """Parse the scheme/legacy frontmatter subset into a dict.

    Scalars -> str. Simple `- item` lists -> list[str]. Nested two-level blocks
    (edges:) -> dict[str, list]. Typed edge list items in BOTH forms ->  dict:
      - the inline-flow form `- {target: X, kind: Y}`, and
      - the multi-line BLOCK-MAPPING form (the shape producers actually author):
            - target: X
              kind: Y
        where the `- target:` line opens a mapping item and subsequent
        more-indented `key: value` lines (`kind:`, etc.) belong to THAT item,
        not to the surrounding block. (Before the batch-33 fix this form was
        mis-read: `- target: X` stored as the bare string `"target: X"` and the
        indented `kind:` line was attached as a stray sub-key of `edges`, so the
        reachability GC never traversed block-mapping `depends-on`/`uses-record`
        edges. See the batch-33 meta-phase report.)
    Indentation drives nesting; we track the indent of the current key/sub-key.
    """
    raw = extract_frontmatter_block(text)
    if raw is None:
        return {}
    out: dict = {}
    cur_key: str | None = None          # top-level key collecting a list/block
    cur_subkey: str | None = None       # second-level key inside a block
    cur_key_indent = 0
    # When the most recent list item is a BLOCK-MAPPING item (`- target: X`
    # followed by indented `kind: Y` continuation lines), we hold it here so the
    # continuation `key: value` lines fold INTO this dict rather than being
    # mistaken for a deeper block sub-key. `cur_item_indent` is the indent of the
    # `- ` marker; a continuation line is any non-list line indented STRICTLY
    # deeper than that marker.
    cur_item_dict: dict | None = None
    cur_item_indent = -1

    def indent_of(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    for raw_line in raw.splitlines():
        line = _strip_inline_comment(raw_line.rstrip())
        if not line.strip():
            continue
        ind = indent_of(line)
        stripped = line.strip()

        # A continuation line of an open block-mapping list item: a `key: value`
        # line indented strictly deeper than the `- ` marker, while we hold an
        # open mapping item. Fold it into that item's dict.
        if (cur_item_dict is not None and not stripped.startswith("- ")
                and ind > cur_item_indent):
            mc = re.match(r"^(\S[^:]*):\s*(.*)$", stripped)
            if mc:
                ck, cv = mc.group(1).strip(), mc.group(2).strip()
                cur_item_dict[ck] = _unquote(cv)
                continue
            # not a key:value continuation -> fall through (close the item)
        # Any line that is NOT a deeper continuation closes the open mapping item.
        if cur_item_dict is not None and not (
                not stripped.startswith("- ") and ind > cur_item_indent):
            cur_item_dict = None
            cur_item_indent = -1

        # List item.
        if stripped.startswith("- "):
            item = stripped[2:].strip()
            parsed_item = _parse_list_item(item)
            if cur_key is None:
                continue  # malformed; ignore
            # If the list item is itself a `key: value` (block-mapping item, e.g.
            # `- target: X`), open it as a dict so trailing indented `kind:` etc.
            # continuation lines fold in.
            bm = re.match(r"^(\S[^:]*):\s*(.+)$", item)
            if bm and not item.startswith("{"):
                parsed_item = {bm.group(1).strip(): _unquote(bm.group(2).strip())}
                cur_item_dict = parsed_item
                cur_item_indent = ind
            else:
                cur_item_dict = None
                cur_item_indent = -1
            # Promote a still-pending top-level opener to a concrete list.
            if isinstance(out.get(cur_key), _Pending):
                out[cur_key] = []
            target_container = out[cur_key]
            if isinstance(target_container, dict):
                # we're inside a nested block (edges:)
                if cur_subkey is None:
                    continue
                target_container.setdefault(cur_subkey, []).append(parsed_item)
            else:
                target_container.append(parsed_item)
            continue

        # key: value  OR  key:  (block opener)
        m = re.match(r"^(\S[^:]*):\s*(.*)$", stripped)
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()

        if ind == 0:
            cur_key = key
            cur_subkey = None
            cur_key_indent = ind
            if val == "" or val == "[]":
                # block or empty list opener; default to list, may become dict
                out[key] = [] if val != "" else _Pending()
            else:
                out[key] = _unquote(val)
                cur_key = None  # scalar, not collecting
        else:
            # nested under the current top-level block key
            if cur_key is None:
                continue
            # Promote the top-level container to a dict on first sub-key.
            if isinstance(out.get(cur_key), _Pending) or isinstance(out.get(cur_key), list):
                if not isinstance(out.get(cur_key), dict):
                    out[cur_key] = {}
            cur_subkey = key
            if val and val != "[]":
                out[cur_key][key] = _unquote(val)
                cur_subkey = None
            else:
                out[cur_key].setdefault(key, [])

    # Resolve any leftover _Pending (an empty block opener never filled) to [].
    for k, v in list(out.items()):
        if isinstance(v, _Pending):
            out[k] = []
    return out


class _Pending:
    """Sentinel: a `key:` opener whose body (list vs nested block) is unknown."""
    pass


def _parse_list_item(item: str):
    """A list item is either a bare string or an inline `{target: X, kind: Y}`.

    Bare strings may carry a trailing free-text qualifier in parens, e.g.
    `book/src/L4/dot.md (firm — ...)` or `palace/...cpp:32-477 (Foo::Bar)`.
    We return the raw string; target extraction (stripping the qualifier) is
    done by the edge reader, which knows whether a target is a slug or a cite.
    """
    item = item.strip()
    if item.startswith("{") and item.endswith("}"):
        inner = item[1:-1]
        d: dict = {}
        for part in inner.split(","):
            if ":" in part:
                k, v = part.split(":", 1)
                d[k.strip()] = _unquote(v.strip())
        return d
    return _unquote(item)


# ---------------------------------------------------------------------------
# Node-id normalization. The graph keys on the repo-relative slug
# (no `book/src/` prefix, no `.md` suffix): `L1/dot`, `feature/eigenmode.L4`,
# `concepts/config-record`, `L1-L0/ksp-solve-mutation-rotation`.
# Edge targets appear in TWO forms on disk:
#   - slug form (depends_on:) -> `L1/dot`
#   - full path form (composes:/lowers_to:) -> `book/src/L4/dot.md`
# Both normalize to the slug.
# ---------------------------------------------------------------------------


def slug_of_path(p: Path, book_src: Path) -> str:
    rel = p.relative_to(book_src)
    return str(rel.with_suffix(""))


def normalize_target(raw: str) -> str | None:
    """Strip a trailing ` (qualifier)`, then normalize a slug or full-path
    target to a slug. Returns None if the token isn't a book target (e.g. an
    L0 source citation `palace/...cpp:..`)."""
    s = raw.strip()
    # drop trailing parenthetical qualifier: `... (firm — ...)`
    paren = s.find(" (")
    if paren != -1:
        s = s[:paren].strip()
    s = s.strip()
    if not s:
        return None
    # an L0 source citation (has a `:lo-hi` line range and is NOT a .md) -> not a book node
    if re.search(r":\d", s) and not s.endswith(".md"):
        return None
    # full-path form
    if s.startswith("book/src/"):
        s = s[len("book/src/"):]
    if s.endswith(".md"):
        s = s[: -len(".md")]
    # bare slug form already (`L1/dot`); leave as-is
    return s or None


# ---------------------------------------------------------------------------
# The graph.
# ---------------------------------------------------------------------------


@dataclass
class Node:
    slug: str
    path: Path
    rank: float | None = None          # numeric ladder rank; None = untyped
    rank_token: str | None = None      # the on-disk maturity word
    is_root: bool = False              # feature_root: seed
    is_obstruction: bool = False
    obstruction_kind: str | None = None
    is_feature: bool = False
    is_lowering_theme: bool = False
    kind: str | None = None            # frontmatter `kind:` (documentation token)
    depends_on: list[str] = field(default_factory=list)   # slugs
    references: list[str] = field(default_factory=list)    # slugs
    untyped: bool = True               # no rank AND no edges read
    notes: list[str] = field(default_factory=list)


# The maturity token always LEADS the first non-empty line after `## Status`,
# as the leading inline-code (`` `firm` ``) or bold (`**firm**`) token — the
# project convention. It may carry a parenthetical qualifier INSIDE the
# decoration (`` `rough-in (test-coverage-bounded)` ``, `` `firm (structural)` ``,
# `` `obstruction (opaque-library-ownership)` ``). We match the leading word,
# preferring the qualified sub-rank spellings over the bare ladder word so that
# `rough-in (test-coverage-bounded)` reads as the 2.5 sub-rank, not bare
# `rough-in`. Tokens are ordered LONGEST-/most-qualified-FIRST for that reason.
_STATUS_TOKENS = (
    "rough-in (test-coverage-bounded)",
    "partly-constructive",
    "partial-obstruction",
    "roadmap_goal",
    "obstruction",
    "rough-in",
    "stub",
    "firm",
    "seed",
)


def read_status_line(text: str) -> str | None:
    """Find the prose `## Status` maturity token.

    Reads the FIRST non-empty line after a `## Status` heading and matches ONLY
    the **leading** maturity token (the project convention: the maturity word is
    the leading inline-code `` `token` `` — or bold `**token**` — of the status
    line). This is deliberately NOT a multi-line blob scan: a firm `## Status`
    paragraph frequently MENTIONS "rough-in"/"stub" in a downstream provenance
    phrase ("promoted from rough-in", "previously the rough-in (…) caveat …"),
    and a blob-scan-in-priority-order mis-reads such a firm node as rough-in/stub
    (the c095 token-priority bug, 12 ledger instances). Anchoring on the LEADING
    token of the first line is exactly the project convention and immune to that
    downstream-mention drift.

    Returns a known ladder/obstruction token (the qualified sub-rank spelling
    when present, e.g. `rough-in (test-coverage-bounded)`), or None.
    """
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"^#{2,3}\s+Status\b", ln.strip()):
            # the first non-empty line after the heading
            first = None
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    first = lines[j].strip()
                    break
            if first is None:
                return None
            # strip a leading blockquote/list marker, then a single leading
            # decoration char (`` ` `` inline-code or `*` bold) so we can read
            # the token whether it is `` `firm` `` or `**firm**` (and tolerate an
            # inline-code span that is left UNTERMINATED on the first line, e.g.
            # a long parenthetical that wraps — the leading word still leads).
            head = first.lstrip("> ").lstrip()
            head = head.lstrip("`*").lower()
            # longest/most-qualified token that PREFIXES the leading text wins.
            for tok in _STATUS_TOKENS:
                if head.startswith(tok):
                    return tok
            return None
    return None


def derive_rank(fm: dict, text: str) -> tuple[float | None, str | None, bool, str | None]:
    """Return (numeric_rank, rank_token, is_obstruction, obstruction_kind).

    Priority (scheme §1, §5): explicit `rank:` > `firmness:` > feature `status:`
    (non-seed) > prose `## Status`. The `seed` token is the root marker, never a
    rank; a feature column with `status: seed` and no other rank is treated as
    UNTYPED for rank (its composition-maturity is unknown until P1 splits it),
    while still contributing its root membership (handled by the caller)."""
    # explicit rank token
    tok = fm.get("rank") or fm.get("firmness") or None
    if tok is None:
        st = fm.get("status")
        if st is not None and st != ROOT_MARKER:
            tok = st
    if tok is None:
        tok = read_status_line(text)

    if tok is None:
        return None, None, False, None

    tok = tok.strip()
    if tok in OBSTRUCTION_KINDS:
        # constructive-resolution rank of the negative result
        res = fm.get("obstruction_resolution")
        res_val = RANK_VALUE.get(res) if res else None
        # use the declared obstruction_resolution rank when present; when no
        # resolution is stated, leave it None (typed-but-rankless) rather than
        # defaulting to firm, so the linter never silently asserts a firm
        # obstruction the author didn't declare. (D1↔D2 sync point: if §1f later
        # prefers obstruction-defaults-to-firm, that is a one-line change here.)
        return res_val, tok, True, fm.get("obstruction_kind")

    val = RANK_VALUE.get(tok)
    return val, tok, False, None


def build_graph(book_src: Path, verbose: bool = False) -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    for p in sorted(book_src.rglob("*.md")):
        text = p.read_text(errors="replace")
        slug = slug_of_path(p, book_src)
        fm = parse_frontmatter(text)
        node = Node(slug=slug, path=p)

        kind = fm.get("kind")
        node.kind = kind
        node.is_feature = (kind == "feature-surface") or slug.startswith("feature/")
        # lowering theme: directory like L4-L3, L3-L2, ... L1-L0
        node.is_lowering_theme = bool(re.match(r"^L\d-L\d/", slug))

        # rank + obstruction
        rank, rtok, is_obs, okind = derive_rank(fm, text)
        node.rank = rank
        node.rank_token = rtok
        node.is_obstruction = is_obs
        node.obstruction_kind = okind

        # ----- root marker (scheme §3) -----
        # Root membership is PERMANENT and CATEGORICAL: a feature-surface COLUMN
        # is a root regardless of its composition-maturity. Three signals, in the
        # transitional dual-form era (D1 OQ graded-stack-feature-root-frontmatter-split):
        #   (1) explicit `feature_root: seed` (the going-forward split form);
        #   (2) legacy `status: seed` (the un-promoted columns still carry it);
        #   (3) a feature-surface COLUMN that PROMOTED off seed to `status: firm`
        #       — it lost the seed token but its root-role never changed. We detect
        #       a column by `kind: feature-surface` (excluding the group-intro pages
        #       driver-leaf / output-product / spine-root / index, which are NOT
        #       columns and NOT roots).
        if fm.get("feature_root") == ROOT_MARKER or fm.get("status") == ROOT_MARKER:
            node.is_root = True
        elif (kind == "feature-surface"
              and slug not in FEATURE_NON_COLUMN):
            # promoted-off-seed column: still a permanent root.
            node.is_root = True
            node.notes.append(
                "root inferred from kind:feature-surface (promoted off seed; "
                "carries no feature_root: marker — transitional dual-form, "
                "OQ graded-stack-feature-root-frontmatter-split)")

        # ----- edges -----
        edges = fm.get("edges")
        read_any_edge = False
        if isinstance(edges, dict):
            for tgt in edges.get("depends-on", []) or []:
                t = _edge_target(tgt)
                nt = normalize_target(t) if t else None
                if nt:
                    node.depends_on.append(nt)
                    read_any_edge = True
            for tgt in edges.get("reference", []) or []:
                t = _edge_target(tgt)
                nt = normalize_target(t) if t else None
                if nt:
                    node.references.append(nt)
                    read_any_edge = True
        else:
            # ---- migration mapping from the three legacy representations ----
            # (a) depends_on: -> depends-on
            for tgt in fm.get("depends_on", []) or []:
                nt = normalize_target(str(tgt))
                if nt:
                    node.depends_on.append(nt)
                    read_any_edge = True
            # (a) lowers_to:/lifts_from:/lifts_to: -> depends-on (lowering edge is
            #     blocking on both endpoints; kind=lowers/lifts is documentation).
            for key in ("lowers_to", "lifts_from", "lifts_to", "consumes"):
                for tgt in fm.get(key, []) or []:
                    nt = normalize_target(str(tgt))
                    if nt:
                        node.depends_on.append(nt)
                        read_any_edge = True
            # (c) composes: -> a vocabulary op is depends-on; a SIBLING feature
            #     column is a reference (the OWN-COMPOSITION rule, scheme §3).
            for tgt in fm.get("composes", []) or []:
                nt = normalize_target(str(tgt))
                if not nt:
                    continue
                read_any_edge = True
                if nt.startswith("feature/"):
                    node.references.append(nt)   # sibling root -> reference
                else:
                    node.depends_on.append(nt)   # vocabulary op -> depends-on
            # (c) l0_ground_truth: source citations are evidence (depends-on,
            #     kind: cites-evidence). They are NOT book nodes (normalize_target
            #     returns None for a `:lo-hi` cite), so they don't add graph edges
            #     — but their presence counts as "typed" for the untyped flag.
            if fm.get("l0_ground_truth"):
                read_any_edge = True

        node.untyped = (node.rank is None and not read_any_edge
                        and not node.is_root and not node.is_obstruction)
        nodes[slug] = node
    return nodes


def _edge_target(item) -> str | None:
    """An edges: list item is a bare string or a {target:, kind:} mapping."""
    if isinstance(item, dict):
        return item.get("target")
    return str(item)


# ---------------------------------------------------------------------------
# Lowering-theme rank derivation: theme rank = min(endpoint ranks) (scheme §5).
# Applied AFTER the base graph is built so endpoint ranks are available.
# ---------------------------------------------------------------------------


def apply_lowering_theme_ranks(nodes: dict[str, Node]) -> None:
    for node in nodes.values():
        if not node.is_lowering_theme:
            continue
        endpoint_ranks = [nodes[d].rank for d in node.depends_on
                          if d in nodes and nodes[d].rank is not None]
        if endpoint_ranks:
            derived = min(endpoint_ranks)
            # a theme's rank is derived from (and bounded by) its endpoints.
            if node.rank is None:
                node.rank = derived
                node.rank_token = f"{rank_label(derived)} (derived: min of endpoints)"
            elif node.rank > derived:
                node.notes.append(
                    f"declared rank {rank_label(node.rank)} exceeds min-of-endpoints "
                    f"{rank_label(derived)} (lowering-theme rule, scheme §5)")


# ---------------------------------------------------------------------------
# Analysis 1 — rank linter.
# ---------------------------------------------------------------------------


@dataclass
class RankViolation:
    src: str
    dep: str
    src_rank: float
    dep_rank: float


def rank_check(nodes: dict[str, Node]) -> tuple[list[RankViolation], list[str], list[str]]:
    """Returns (violations, promotion_frontier, unresolved_targets)."""
    violations: list[RankViolation] = []
    unresolved: list[str] = []
    for node in nodes.values():
        if node.rank is None:
            continue
        # promotion-frontier check accumulates below
        for dep_slug in node.depends_on:
            dep = nodes.get(dep_slug)
            if dep is None:
                unresolved.append(f"{node.slug} -> {dep_slug}")
                continue
            if dep.rank is None:
                continue  # dep untyped: warn-not-fail (incremental)
            if node.rank > dep.rank:
                violations.append(RankViolation(
                    src=node.slug, dep=dep_slug,
                    src_rank=node.rank, dep_rank=dep.rank))

    # Promotion frontier: a node is "at the frontier" iff it is typed and EVERY
    # one of its typed depends-on deps has rank >= the node's own rank (i.e.
    # nothing below blocks it from being where it is — and it could climb as soon
    # as its own evidence supports it, since its supports already do). We report
    # nodes whose deps are all >= rank AND that are below firm (room to climb).
    frontier: list[str] = []
    for node in nodes.values():
        if node.rank is None or node.rank >= 3.0:
            continue
        typed_deps = [nodes[d] for d in node.depends_on
                      if d in nodes and nodes[d].rank is not None]
        if all(d.rank >= node.rank for d in typed_deps):
            # all supports already at-or-above this node's rank -> ready to climb
            # (gated only by the node's own evidence, not by its foundation)
            frontier.append(node.slug)
    return violations, sorted(frontier), sorted(set(unresolved))


# ---------------------------------------------------------------------------
# Analysis 2 — reachability GC.
# ---------------------------------------------------------------------------


def reachability_gc(nodes: dict[str, Node]) -> tuple[set[str], list[str], dict[str, list[str]]]:
    """Mark from feature roots over depends-on edges. Returns
    (reachable, garbage, inbound_map). inbound_map[slug] = list of slugs that
    depends-on it (the per-file inbound-reference report)."""
    roots = [n.slug for n in nodes.values() if n.is_root]
    reachable: set[str] = set()
    stack = list(roots)
    while stack:
        s = stack.pop()
        if s in reachable:
            continue
        reachable.add(s)
        node = nodes.get(s)
        if node is None:
            continue
        for dep in node.depends_on:
            if dep in nodes and dep not in reachable:
                stack.append(dep)

    # inbound depends-on map (over the whole graph, for the per-file report)
    inbound: dict[str, list[str]] = {s: [] for s in nodes}
    for node in nodes.values():
        for dep in node.depends_on:
            if dep in inbound:
                inbound[dep].append(node.slug)

    # garbage = typed/DAG nodes that are NOT reachable and are NOT methodology /
    # outside-DAG pages. We can't perfectly know "outside DAG" without the kind,
    # so we report ALL unreachable nodes but separate the likely-outside-DAG
    # ones (methodology/, design/, concepts/, index.md, group-intro pages) which
    # are expected-unreachable and not detritus.
    garbage = sorted(s for s in nodes if s not in reachable)
    return reachable, garbage, inbound


OUTSIDE_DAG_PREFIXES = ("methodology/", "design/")
OUTSIDE_DAG_SUFFIXES = ("/index", "index")  # index.md pages
# group-intro feature pages (not columns): driver-leaf, output-product, spine-root
FEATURE_NON_COLUMN = {"feature/driver-leaf", "feature/output-product",
                      "feature/spine-root", "feature/index"}
# navigational-container kinds (scheme §6, batch-33-ratified): layer/group/feature
# index + group-intro + dependency-map pages. Reference-only, no rank, not DAG
# nodes — expected-unreachable, never detritus. We accept the canonical token
# plus the descriptive synonyms producers may write.
NAVIGATIONAL_CONTAINER_KINDS = {
    "navigational-container", "navigation-container",
    "group-intro", "index", "dependency-map",
}


def is_likely_outside_dag(slug: str, node: Node) -> bool:
    if slug.startswith(OUTSIDE_DAG_PREFIXES):
        return True
    if slug.endswith("/index") or slug == "index":
        return True
    if slug in FEATURE_NON_COLUMN:
        return True
    # navigational containers (layer-index / group-intro / dependency-map pages):
    # the batch-33-ratified `kind: navigational-container` convention (scheme §6).
    # They emit reference-only edges, carry no rank, and are NOT DAG nodes — so
    # they are expected-unreachable, never detritus. This is the explicit author
    # signal that replaces the heuristic guessing (the 23 group-intro pages +
    # concepts/dependency-map that previously read as detritus_with_typed_edges
    # noise). Recognized regardless of how the navigation links are typed.
    if node.kind is not None:
        # the kind may carry a free-text parenthetical qualifier, e.g.
        # `navigational-container (feature group intro)` — match the leading token.
        kind_head = node.kind.split(" (")[0].strip()
        if kind_head in NAVIGATIONAL_CONTAINER_KINDS:
            return True
    # narrative concept pages are outside-DAG per scheme §5; we can't always tell
    # them from record-definition pages without the `kind`, so we DON'T blanket
    # them here — they show up as unreachable and are flagged for P1 judgment.
    return False


# ---------------------------------------------------------------------------
# Rendering.
# ---------------------------------------------------------------------------


def build_summary(nodes: dict[str, Node]) -> dict:
    apply_lowering_theme_ranks(nodes)
    violations, frontier, unresolved = rank_check(nodes)
    reachable, garbage, inbound = reachability_gc(nodes)

    roots = sorted(n.slug for n in nodes.values() if n.is_root)
    untyped = sorted(n.slug for n in nodes.values() if n.untyped)
    typed = [n for n in nodes.values() if not n.untyped]

    # detritus = unreachable AND not-likely-outside-DAG AND typed-as-a-DAG-node
    detritus = sorted(
        s for s in garbage
        if not is_likely_outside_dag(s, nodes[s]) and not nodes[s].untyped)
    expected_unreachable = sorted(
        s for s in garbage if is_likely_outside_dag(s, nodes[s]))

    # PRE-P1 caveat. Most "detritus" right now is an artifact of edges being
    # untyped: a node carries its deps only in a PROSE dep-map, so the mark can't
    # propagate THROUGH it, and everything below it looks unreachable. We split
    # the detritus into (i) nodes with NO typed outbound depends-on edges (the
    # mark dead-ends here purely because this node's edges aren't typed yet — the
    # dominant pre-P1 cause, NOT genuine garbage) vs (ii) nodes that DO declare
    # typed deps yet are still unreached (a stronger garbage signal). Post-P1
    # (every edge typed) bucket (i) collapses and only true garbage remains.
    detritus_no_typed_edges = sorted(
        s for s in detritus
        if not nodes[s].depends_on)  # no outbound depends-on at all
    detritus_with_typed_edges = sorted(
        s for s in detritus if nodes[s].depends_on)

    rank_hist: dict[str, int] = {}
    for n in typed:
        lbl = (n.rank_token.split(" (")[0] if n.rank_token else
               (rank_label(n.rank) if n.rank is not None else "typed-no-rank"))
        rank_hist[lbl] = rank_hist.get(lbl, 0) + 1

    return {
        "totals": {
            "files": len(nodes),
            "typed": len(typed),
            "untyped": len(untyped),
            "roots": len(roots),
            "rank_violations": len(violations),
            "unresolved_depends_on_targets": len(unresolved),
            "promotion_frontier": len(frontier),
            "reachable": len(reachable),
            "detritus": len(detritus),
            "detritus_no_typed_edges_pre_p1_artifact": len(detritus_no_typed_edges),
            "detritus_with_typed_edges_stronger_signal": len(detritus_with_typed_edges),
            "expected_unreachable_outside_dag": len(expected_unreachable),
        },
        "rank_histogram": rank_hist,
        "roots": roots,
        "rank_violations": [
            {"src": v.src, "src_rank": rank_label(v.src_rank),
             "dep": v.dep, "dep_rank": rank_label(v.dep_rank)}
            for v in violations],
        "unresolved_depends_on_targets": unresolved,
        "promotion_frontier": frontier,
        "detritus": detritus,
        "detritus_no_typed_edges_pre_p1_artifact": detritus_no_typed_edges,
        "detritus_with_typed_edges_stronger_signal": detritus_with_typed_edges,
        "expected_unreachable_outside_dag": expected_unreachable,
        "untyped": untyped,
        "lowering_theme_notes": {
            n.slug: n.notes for n in nodes.values() if n.notes},
        "inbound_reference_report": {
            s: sorted(set(inbound[s])) for s in sorted(inbound) if inbound[s]},
    }


def render_text(summary: dict, show_untyped: bool, show_inbound: bool) -> None:
    t = summary["totals"]
    print("=" * 72)
    print("graded-stack-lint  —  rank check + reachability GC")
    print("=" * 72)
    print(f"files scanned:        {t['files']}")
    print(f"  typed nodes:        {t['typed']}")
    print(f"  untyped (WARNING):  {t['untyped']}   "
          f"(pre-P1 expected; warn-not-fail)")
    print(f"  feature roots:      {t['roots']}")
    print()
    print(f"rank histogram (typed nodes): {summary['rank_histogram']}")
    print()

    # --- rank linter ---
    print("-" * 72)
    print("AXIS 1 — RANK LINTER (well-foundedness: rank(u) <= min deps)")
    print("-" * 72)
    if summary["rank_violations"]:
        print(f"RANK VIOLATIONS ({len(summary['rank_violations'])}):")
        for v in summary["rank_violations"]:
            print(f"  [VIOLATION] {v['src']} ({v['src_rank']}) "
                  f"depends-on {v['dep']} ({v['dep_rank']}) "
                  f"— a {v['src_rank']} node rests on a {v['dep_rank']} dep")
    else:
        print("RANK VIOLATIONS: none.")
    if summary["unresolved_depends_on_targets"]:
        print(f"\nUNRESOLVED depends-on targets "
              f"({len(summary['unresolved_depends_on_targets'])}) "
              f"(edge points at a slug with no file — WARNING unless --strict):")
        for u in summary["unresolved_depends_on_targets"]:
            print(f"  [UNRESOLVED] {u}")
    if summary["lowering_theme_notes"]:
        print("\nLOWERING-THEME rank notes:")
        for slug, notes in summary["lowering_theme_notes"].items():
            for nt in notes:
                print(f"  [{slug}] {nt}")
    print(f"\nPROMOTION FRONTIER ({len(summary['promotion_frontier'])}) "
          f"— typed sub-firm nodes whose every typed dep is at-or-above them "
          f"(ready to climb when their own evidence supports it):")
    for s in summary["promotion_frontier"]:
        print(f"  [FRONTIER] {s}")

    # --- reachability GC ---
    print()
    print("-" * 72)
    print("AXIS 2 — REACHABILITY GC (liveness: mark from feature roots)")
    print("-" * 72)
    print(f"reachable from roots: {t['reachable']}")
    if summary["detritus"]:
        n_pre = t["detritus_no_typed_edges_pre_p1_artifact"]
        n_sig = t["detritus_with_typed_edges_stronger_signal"]
        print(f"\nDETRITUS ({len(summary['detritus'])}) "
              f"— typed DAG nodes unreachable from any feature root.")
        print(f"  PRE-P1 READING: {n_pre} of these have NO typed outbound "
              f"depends-on edges — the mark dead-ends at them ONLY because their\n"
              f"  own edges are still in prose dep-maps (not yet typed). That is an "
              f"edge-untypedness ARTIFACT, not garbage; it collapses as P1 types\n"
              f"  edges. The {n_sig} node(s) that DO declare typed deps yet stay "
              f"unreached are the stronger garbage signal to inspect first.")
        if summary["detritus_with_typed_edges_stronger_signal"]:
            print(f"\n  STRONGER GARBAGE SIGNAL ({n_sig}) — declares typed deps, "
                  f"still unreachable:")
            for s in summary["detritus_with_typed_edges_stronger_signal"]:
                print(f"    [GARBAGE*] {s}")
        print(f"\n  edge-untyped detritus (pre-P1 artifact, {n_pre}):")
        for s in summary["detritus_no_typed_edges_pre_p1_artifact"]:
            print(f"    [garbage?] {s}")
    else:
        print("\nDETRITUS: none (every typed DAG node is reachable from a root).")
    print(f"\nexpected-unreachable (outside-DAG: methodology/design/index/"
          f"group-intro pages): {t['expected_unreachable_outside_dag']}")

    if show_untyped and summary["untyped"]:
        print(f"\nUNTYPED files ({len(summary['untyped'])}) — no rank/edges yet "
              f"(P1 will type these):")
        for s in summary["untyped"]:
            print(f"  [untyped] {s}")

    if show_inbound:
        print("\nINBOUND-REFERENCE REPORT (per file: who depends-on it):")
        for s, srcs in summary["inbound_reference_report"].items():
            print(f"  {s}  <-  {', '.join(srcs)}")

    print()
    print("=" * 72)
    print(f"RESULT: {t['rank_violations']} rank violation(s), "
          f"{t['detritus']} detritus node(s), "
          f"{t['untyped']} untyped (warning).")
    print("=" * 72)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="graded-stack-lint",
        description="Graded-stack rank linter + reachability GC "
                    "(METHODOLOGY-GRADED-STACK.md §4).")
    ap.add_argument("--book-src", default=None,
                    help="path to book/src (default: auto-detect from tool location)")
    ap.add_argument("--json", action="store_true",
                    help="emit the machine-parseable JSON summary (for integrator-finalize)")
    ap.add_argument("--show-untyped", action="store_true",
                    help="list every untyped file (default: just the count)")
    ap.add_argument("--show-inbound", action="store_true",
                    help="print the per-file inbound-reference report")
    ap.add_argument("--strict", action="store_true",
                    help="treat unresolved depends-on targets as failures too")
    args = ap.parse_args(argv)

    if args.book_src:
        book_src = Path(args.book_src).resolve()
    else:
        # tools/graded-stack-lint/graded_stack_lint.py -> repo/book/src
        book_src = Path(__file__).resolve().parents[2] / "book" / "src"

    if not book_src.is_dir():
        print(f"error: book/src not found at {book_src}", file=sys.stderr)
        return 2

    nodes = build_graph(book_src)
    summary = build_summary(nodes)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        render_text(summary, args.show_untyped, args.show_inbound)

    fail = summary["totals"]["rank_violations"] > 0
    if args.strict and summary["totals"]["unresolved_depends_on_targets"] > 0:
        fail = True
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
