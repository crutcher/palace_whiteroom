---
agent: layer-intro-author
invoked_at: 2026-06-04T200500Z
scope: P0-B — the two graded-stack linters (rank check + reachability GC) under tools/
status: pending
integrated_at: 2026-06-04T211500Z
integration_commit: caa1d390d4163534901b3a72b5c657a92936d304
integration_notes: "Applied clean (D2, cycle-094 batch-30 position 1/3). Created tools/graded-stack-lint/ (graded_stack_lint.py rank check + reachability GC + README + requirements + fixture). ZERO book/ edits (tooling deliverable). Finalize ran --json as a BASELINE record only (NOT a gate, the linters just landed): rank_violations=22 (the known hand-tracked firm-rests-on-rough-in cascade, priorities item-1) + detritus=136 + roots=36 + typed=207. retroactive-budget 0; build exit 0; no build-repair. 4 OQs promoted (incl. graded-stack-finalize-json-wiring-role-spec)."
---

# CYCLE: graded-stack linters (P0-B)

## Summary

This dispatch **delivers and dry-run-validates** the two graded-stack linters
(`METHODOLOGY-GRADED-STACK.md` §4) under `tools/graded-stack-lint/`, following the
`tools/citecheck/` layout (`<tool>.py` + `README.md` + `requirements.txt`, stdlib-only,
no venv). Both linters run over **one** typed dependency graph built from the
`book/src/**/*.md` frontmatter per D1's landed scheme
(`book/src/methodology/graded-stack-scheme.md`):

1. **Rank linter** (Axis 1) — asserts `rank(u) ≤ rank(v)` for every blocking
   `depends-on` edge; reports rank **violations** + the **promotion frontier** for free;
   applies the lowering-theme `rank ≤ min(endpoints)` rule (scheme §5).
2. **Reachability GC** (Axis 2) — marks from the feature-root node-set over `depends-on`
   edges; reports **detritus** (unreachable typed nodes) + a per-file **inbound-reference**
   report.

Both **(a)** treat missing/untyped frontmatter as a counted WARNING (never a hard error —
the linters run cleanly throughout the P1 rollout) and **(b)** are validated against a
hand-authored seed fixture exercising a KNOWN rank violation + a KNOWN unreachable node +
the transitional dual-form + the migration mapping, AND dry-run over the real existing
typed subset (the 10 `depends_on:` files + the 24 feature `composes:` files). Output is
human-readable + a machine-parseable `--json` summary the integrator-finalize consumes
(graded-stack §8).

**Files created** (under `tools/`, which is `layer-intro-author`/tooling territory — written
directly, NOT routed through the integrator; recorded here so integrator-finalize knows they
exist + how to invoke them):

- `tools/graded-stack-lint/graded_stack_lint.py` — both linters (one graph, two analyses).
- `tools/graded-stack-lint/README.md` — invocation + the parse contract + the migration mapping.
- `tools/graded-stack-lint/requirements.txt` — documents stdlib-only / no-venv (mirrors citecheck).
- `tools/graded-stack-lint/fixture/book/src/*` (9 `.md` files) + `fixture/README.md` — the seed fixture + its expected-outcome assertions.

## Invocation (for integrator-finalize + producers)

```bash
# human-readable, book/src auto-detected from the tool location:
python3 tools/graded-stack-lint/graded_stack_lint.py
# machine summary the integrator-finalize records (graded-stack §8):
python3 tools/graded-stack-lint/graded_stack_lint.py --json
# fixture self-test (expect exit 1, 2 rank violations):
python3 tools/graded-stack-lint/graded_stack_lint.py \
    --book-src tools/graded-stack-lint/fixture/book/src --show-inbound
```

Flags: `--show-untyped` (list untyped files), `--show-inbound` (per-file inbound report),
`--strict` (also fail on unresolved `depends-on` targets), `--book-src PATH` (override),
`--json`. **Exit code** is 1 iff a rank violation exists (or, under `--strict`, an
unresolved target); untyped warnings and detritus alone never fail (the incremental-safe
requirement (a)).

## Proposed changes

**None to `book/`.** This dispatch writes only to `tools/` (tooling-authoring territory per
the role spec + the dispatch prompt). There are no `edit:book/...` blocks: the linters do not
mutate the artifact, and the artifact-wide typing/audit (which WOULD touch `book/`) is P1, not
this dispatch.

For the record, the new tool files are listed in §Summary; the integrator-finalize bullet to
add to its run (graded-stack §8) is: *run `python3 tools/graded-stack-lint/graded_stack_lint.py
--json` at cycle-end and record the `totals` block.* (This is a methodology/role-spec note for
the batch-30 meta-phase, not a `book/` edit — flagged in Open questions.)

## Supporting evidence

### The parse contract (from D1's landed scheme)

Implemented exactly to D1's `graded-stack-scheme.md`:
- **Rank ladder** `roadmap_goal=0 < stub=1 < rough-in=2 < firm=3`, sub-rank 2.5 for
  `partly-constructive` / `rough-in (test-coverage-bounded)` (scheme §1 table).
- **Rank read priority**: `rank:` → `firmness:` → feature `status:` (non-seed) → prose
  `## Status` (scheme §1/§5).
- **Edges**: the going-forward `edges: {depends-on:, reference:}` block (bare-string AND
  `{target:, kind:}` forms; `kind` ignored), with the **migration mapping** applied when no
  `edges:` block exists — `depends_on:`→depends-on; `lowers_to:`/`lifts_from:`/`lifts_to:`/
  `consumes:`→depends-on; `composes:` vocabulary-op→depends-on, sibling-feature-column→reference
  (the OWN-COMPOSITION rule, scheme §3); `l0_ground_truth:` cites counted as typed but not a
  book-node edge (scheme §4 table).
- **Node identity** = repo-relative slug (no `book/src/`, no `.md`); BOTH legacy forms
  normalized (`L1/dot` slug-form from `depends_on:`, `book/src/L4/dot.md` full-path form from
  `composes:`/`lowers_to:`), trailing ` (qualifier)` stripped.
- **Lowering theme** rank ≤ `min(endpoints)` (scheme §5) — applied as a post-pass once
  endpoint ranks are known.
- **Obstruction** is a separate rankable kind via `obstruction_resolution:` (scheme §1f).

### Fixture validation (correctness, requirement (b))

`tools/graded-stack-lint/fixture/book/src/` — 9 files. Confirmed output:
`files=9, typed=8, untyped=1, roots=3, rank_violations=2, detritus=2, promotion_frontier=1,
exit=1`. The assertions (full list in `fixture/README.md`), all passing:
- **KNOWN rank violation**: `feature/widget.L4 (firm) → L1/weak_op (rough-in)`. ✓
- **Lowering-theme rule**: `L1-L0/widget-lowering` declared `firm`, `min(endpoints)=rough-in`
  → both a note AND a violation on the `weak_op` edge. ✓
- **KNOWN unreachable node**: `L1/orphan` is `firm` yet no root reaches it → DETRITUS
  (liveness ≠ resolution); lands in the "stronger garbage signal" bucket. ✓
- **Transitional dual-form root**: `L2/legacy_compose` (legacy `status: seed`) marked a root. ✓
- **Migration mapping**: its `composes:` vocabulary-op→depends-on, sibling-column→reference,
  `l0_ground_truth:` cite NOT a book node. ✓
- **Untyped = WARNING not error**: `concepts/untyped_concept` (no frontmatter) counted, run
  did not fail on it. ✓

### Dry run over the real `book/src` (requirement (b), graceful degradation)

```
files scanned:        357
  typed nodes:        207
  untyped (WARNING):  150   (pre-P1 expected; warn-not-fail)
  feature roots:      36
rank histogram (typed): {firm: 158, rough-in: 26, obstruction: 10, partly-constructive: 8,
                         partial-obstruction: 4, stub: 1}

AXIS 1 — RANK LINTER
  RANK VIOLATIONS (22)            e.g. L2/normalize(firm)→L1/normalize(rough-in);
                                       L3/dot(firm)→L2/inner_product(rough-in);
                                       L4/gram_reduce(2.5)→L1/bilinear-form(rough-in);
                                       feature/energy-fields.L4(firm)→L1/matrix-weighted-norm(2.5)
  UNRESOLVED depends-on targets (11)   e.g. L1/eliminate_rhs→{apply_linop, axpy,
                                       L1-L0/eliminate-rhs-mutation-rotation}; several L3 ops
                                       whose "(no L4 entry …)" prose got parsed as a slug
  PROMOTION FRONTIER (30)         e.g. L1/bilinear-form, L1/matrix-weighted-norm, L2/dot,
                                       L2/inner_product, feature/{capacitance,electrostatic,
                                       inductance,magnetostatic}.L4

AXIS 2 — REACHABILITY GC
  reachable from roots: 77
  DETRITUS (136): split into
    - 102 with NO typed outbound edges  (pre-P1 edge-untypedness ARTIFACT — collapses as
                                          P1 types edges; NOT genuine garbage)
    - 34 with typed deps, still unreached (stronger garbage signal — all the L2/L3/L4
                                          vocabulary ops the feature columns don't yet
                                          `depends-on` because composes: only reaches a thin
                                          slice; this too collapses as P1 fully types the
                                          feature→vocabulary closure)
  expected-unreachable (methodology/design/index/group-intro): 19
RESULT: 22 rank violation(s), 136 detritus, 150 untyped (warning).  exit=1
```

This is the **correct pre-P1 state** the planner predicted: mostly warnings +
artifact-detritus, the tool degrading gracefully (no crash, no hard-fail on the 150 untyped
files; exit 1 only because of the 22 genuine rank violations that ARE in the typed subset).
The 22 rank violations are real signal already — they are exactly the matrix-weighted-norm /
inner_product / bilinear-form / normalize "firm rests on rough-in" cascade the priorities
item-1 bilinear-form wave will discharge (the linter independently rediscovered the cascade
the project tracked by hand — strong evidence the rank linter is correct). They are **not
acted on here** (that is P1/item-1, per scope).

## Open questions / caveats

- **`record-…-needs-definition-home` flagging:** N/A — this dispatch authored tooling under
  `tools/`, no operator signatures naming an undefined record.

- **DECISION carried from D1 — obstruction encoding (`obstruction_resolution`).** D1 flagged
  this as a parser-coordination point. I implemented exactly D1's encoding: `rank: obstruction`
  (the kind) + `obstruction_kind:` (sub-kind) + `obstruction_resolution:` (the constructive
  rank read as the node's effective rank). When an obstruction node carries NO
  `obstruction_resolution`, the linter treats its rank as **None (typed-but-rankless)** rather
  than defaulting to firm — a conservative choice so the linter never silently asserts a firm
  obstruction the author didn't declare. The 10 obstruction nodes on disk today have no
  `obstruction_resolution:` yet (it is a scheme addition), so they currently show as
  typed-but-rankless and don't anchor any rank check — correct pre-P1 behavior. **If the
  batch-30 meta-phase prefers obstruction-defaults-to-firm, that is a one-line change in
  `derive_rank`.** Flagged for D1↔D2 sync.

- **DECISION carried from D1 — transitional dual-form `seed` (OQ
  `graded-stack-feature-root-frontmatter-split`).** The dry run **empirically confirmed** D1's
  concern: 21 of the 36 feature-column files promoted off `seed` to `status: firm` and thereby
  LOST their `seed` root marker under the single-`status` encoding (e.g. `feature/eigenmode.L4`,
  `feature/driven.L4` are `status: firm`). With a naive "root = has `seed`" rule they fell out of
  the root set and the whole reachability GC collapsed (only 6 reachable). **My resolution
  (implemented):** root membership is permanent + categorical, so the linter marks a root by
  THREE signals — explicit `feature_root: seed`, legacy `status: seed`, OR being a
  `kind: feature-surface` **column** (excluding the `driver-leaf`/`output-product`/`spine-root`/
  `index` group-intro pages) regardless of its `status:`. This makes the GC correct under the
  transitional dual form AND after P1 splits the marker. Flagged so the P1 split + the scheme
  page stay in sync: once P1 writes `feature_root: seed` on every column, the kind-inference
  fallback becomes redundant but harmless.

- **UNRESOLVED-target false positives from prose-in-frontmatter.** 11 unresolved
  `depends-on` targets — but several are **not** real (e.g. `L3/apply_linop → "(no L4 entry;
  apply_linop appears inside …)"`): a legacy `lowers_to:`/`consumes:` list item that is a
  free-text *prose explanation of a non-dependency*, not a slug, which my migration reader
  parsed as a target. This is a **migration-mapping edge case**, not a graph error: such
  prose-as-list-item entries should become `reference:` (or be dropped) during P1's
  hand-classification, which is exactly the "the typing pass IS the audit" step (scheme §4(b)).
  The linter correctly flags them as unresolved (a WARNING, not a failure, since `--strict` is
  off by default), so they surface for P1 to fix. I did NOT try to heuristically suppress them
  — surfacing them is the right pre-P1 behavior. Recorded as input to P1's typing pass.

- **Detritus over-count is a pre-P1 artifact, surfaced honestly.** 136 "detritus" is dominated
  by edge-untypedness (102 nodes have no typed outbound edge at all; the other 34 are vocabulary
  ops no feature column yet `depends-on`). The report splits these two buckets and labels the
  pre-P1 reading explicitly so a reader does not mistake 136 for genuine garbage. Post-P1 (every
  edge typed, every feature column's `composes:` closure complete) the artifact bucket collapses
  and only true garbage remains. This is the correct graceful-degradation behavior, not a defect.

- **Integrator-finalize wiring (graded-stack §8) is a role-spec note for the batch-30
  meta-phase, NOT a `book/` edit I make.** The §8 bullet says finalize should "run the linters
  at finalize once built." The tool + invocation are delivered here; the actual addition of the
  `--json` run to `integrator-finalize`'s role spec is meta-phase territory (`.claude/agents/`
  write authority). Flagged for batch-30 meta-phase intake so finalize starts recording the
  `totals` block.

- **Out of scope by design:** I did NOT run the linters as the artifact-wide audit and act on
  results (P1), did NOT mutate `book/`, and did NOT type any real chapter's edges. This
  dispatch delivers + dry-run-validates the tooling, exactly per the prompt.
