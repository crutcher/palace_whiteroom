# graded-stack-lint

The two **graded-stack linters** (`METHODOLOGY-GRADED-STACK.md` §4) in one tool:
a **rank linter** (Axis 1, well-foundedness) and a **reachability GC** (Axis 2,
liveness). Both run over **one** typed dependency graph built from the
`book/src/**/*.md` frontmatter, per the machine-readable scheme defined in
`book/src/methodology/graded-stack-scheme.md` (the P0-A authoring contract).

No third-party dependencies — Python 3.10+ stdlib only, **no venv required**
(mirrors `tools/citecheck`).

## What it checks

### Axis 1 — rank linter (well-foundedness)
For every blocking `depends-on` edge `u → v`, asserts `rank(u) ≤ rank(v)` — "a
node is at most as resolved as its least-resolved dependency" (scheme §1b). On
the ladder `roadmap_goal=0 < stub=1 < rough-in=2 < firm=3` (with
`partly-constructive` / `rough-in (test-coverage-bounded)` at sub-rank 2.5).

- **Rank violations** — a `firm` entry resting on a `rough-in` dep, etc.
- **Promotion frontier** (free) — typed sub-`firm` nodes whose every typed
  `depends-on` dep is already at-or-above the node's own rank (so the foundation
  no longer blocks a promotion; the node climbs as soon as its OWN evidence
  supports it). This is the rank-discontinuity surface (scheme §1c).
- **Lowering-theme rule** — a lowering theme's rank is bounded by `min` of its
  endpoints (scheme §5); a declared rank above that is flagged.

### Axis 2 — reachability GC (liveness)
Marks from the **feature-root** node-set (the FEATURE-SURFACE SPINE columns)
over `depends-on` edges (scheme §3). Unmarked nodes are **garbage** (detritus /
dead intent). Also emits a **per-file inbound-reference report** (who
`depends-on` each node).

**Reference-reachable reporting tier** (batch-39 meta-phase, ASK-1; scheme §2g).
A *second*, non-gating mark runs from the same roots over BOTH `depends-on` AND
`reference` edges, splitting the `detritus` set:

- **reference-reachable detritus** — depends-on-unreachable but reachable once
  `reference` edges are followed: the §2g / **RE11** DELIBERATE reference-only-
  reachable cohort (combinator-primary leaves back-linked by their combinator's
  `reference`; DIRECTIVE-3 kernel-impls linked to their kernel-api surface by a
  `reference`-class `realizes-kernel-api` edge; feature-root→node `reference`
  under OWN-COMPOSITION). These are firm-and-faithful-but-correctly-off-the
  -`depends-on`-spine — `detritus` over-counts them by ~design under the post-§3
  structural models.
- **true-detritus** — unreachable EVEN under the reference-augmented mark:
  genuine dead intent / orphaned vocabulary. **This is the clean health signal**
  (the §2g escalate-guard watches `true_detritus`, not the raw `detritus`).

A reporting/classification refinement ONLY — it changes **no gate**. `reference`
still constrains nothing and carries no liveness (§3); the gating depends-on-only
GC still marks both sub-buckets `[GARBAGE*]`; the tier merely *separates* them.
The split counts always print (text + JSON); the per-node listing + the back-link
attribution are gated behind `--reference-reachable`.

## The graph it builds (the parse contract)

**Node identity** is the repo-relative slug — no `book/src/` prefix, no `.md`
suffix: `L1/dot`, `feature/eigenmode.L4`, `concepts/config-record`,
`L1-L0/ksp-solve-mutation-rotation`.

**Rank** is read in priority order (scheme §1, §5):
`rank:` frontmatter → `firmness:` → feature `status:` (when not `seed`) → the
prose `## Status` line. `seed` is the **root marker**, never a rank.
An `obstruction` / `partial-obstruction` is a separate *kind*; its constructive
rank is read from `obstruction_resolution:` (scheme §1f).

**Prose `## Status` parse rule — the leading inline-code token.** When the
fallback reaches the prose `## Status` line, it reads the **first non-empty line
after the heading** and matches ONLY its **leading** maturity token — the
project convention that the maturity word is the leading inline-code
(`` `firm` ``) or bold (`**firm**`) token of the status line. The qualified
sub-rank spellings (`` `rough-in (test-coverage-bounded)` ``, `` `firm
(structural)` ``, `` `obstruction (opaque-library-ownership)` ``) are matched
ahead of their bare ladder word, so a sub-rank reads as 2.5, not bare rough-in.
This is **not** a multi-line blob scan: a firm `## Status` paragraph routinely
*mentions* "rough-in"/"stub" downstream in a provenance phrase ("promoted from
rough-in", "previously the rough-in (…) caveat"), and a blob-scan in
priority-order (rough-in/stub before firm) mis-read such firm nodes as
rough-in/stub (the c095 token-priority bug — 12 ledger instances incl. the lone
residual O1 rank violation, all untyped-tail nodes). Anchoring on the leading
token is immune to that downstream-mention drift; typed `rank:` nodes never
reach this path. The `fixture/book/src/L1/prose_firm_provenance.md` case
regression-guards it (a firm node whose `## Status` mentions "rough-in" and
"stub" in provenance phrases).

**Edges** are read from the going-forward `edges:` block when present:

```yaml
edges:
  depends-on:        # blocking: constrains rank AND carries liveness
    - L1/dot
    - target: L2/linear_combination
      kind: folds    # documentation; the linter ignores `kind`
  reference:         # navigational see-also: constrains nothing, no liveness
    - feature/eigenmode.L4
```

When no `edges:` block exists, the linter applies the **migration mapping**
(scheme §4) to the three legacy representations so it runs TODAY, pre-P1:

| legacy frontmatter | mapped to |
|---|---|
| `depends_on:` | `depends-on` |
| `lowers_to:` / `lifts_from:` / `lifts_to:` / `consumes:` | `depends-on` (the lowering edge is blocking on both endpoints) |
| `composes:` → a **vocabulary op** | `depends-on` |
| `composes:` → a **sibling feature column** (`feature/…`) | `reference` (the OWN-COMPOSITION rule, scheme §3) |
| `l0_ground_truth:` source cites (`palace/…:lo-hi`) | counted as "typed" but not a book-node edge |

Trailing free-text qualifiers in legacy lists (`… (firm — …)`,
`… (EigenSolver::Solve)`) are stripped; an L0 source citation (`…:lo-hi`, not
`.md`) is correctly NOT treated as a book node.

**Feature roots** are permanent and categorical (scheme §3). The linter marks a
node a root if it carries `feature_root: seed` (the split form) OR legacy
`status: seed` OR is a `kind: feature-surface` **column** that promoted off seed
to `status: firm` (it lost the `seed` token but its root-role never changed —
the transitional dual-form, D1 OQ `graded-stack-feature-root-frontmatter-split`).
The feature group-intro pages (`driver-leaf`, `output-product`, `spine-root`,
`index`) are NOT columns and NOT roots.

## Incremental-safe (the hard requirement)

Most of the tree is not yet typed (P1 does the artifact-wide typing pass in
c095+). **A file with no rank/edge frontmatter is a counted WARNING, never a
hard error.** Exit code is non-zero ONLY when there is a rank violation (or,
under `--strict`, an unresolved `depends-on` target). Untyped warnings and
detritus alone never fail the run — the linters are runnable throughout the P1
rollout.

**Pre-P1 detritus reading.** Before edges are typed, "detritus" is dominated by
an *edge-untypedness artifact*: a node carries its deps only in a prose dep-map,
so the mark can't propagate through it and everything below looks unreachable.
The report splits detritus into (i) nodes with NO typed outbound `depends-on`
(the mark dead-ends purely because this node's edges aren't typed yet — collapses
as P1 types edges) vs (ii) nodes that DO declare typed deps yet stay unreached
(the stronger garbage signal). Post-P1, bucket (i) collapses and only genuine
garbage remains.

## Usage

```bash
# Run from anywhere; book/src is auto-detected from the tool location.
python3 tools/graded-stack-lint/graded_stack_lint.py            # human-readable
python3 tools/graded-stack-lint/graded_stack_lint.py --json     # machine summary
```

Flags:

| flag | effect |
|---|---|
| `--book-src PATH` | point at a different `book/src` (used for the fixture) |
| `--json` | emit the machine-parseable JSON summary (for integrator-finalize) |
| `--show-untyped` | list every untyped file (default: just the count) |
| `--show-inbound` | print the per-file inbound-reference report |
| `--reference-reachable` | list the §2g reference-reachable / true-detritus split node-by-node, with the back-link that keeps each reference-reachable node alive (the split COUNTS always print regardless) |
| `--strict` | treat unresolved `depends-on` targets as failures too |

### JSON summary (for integrator-finalize, graded-stack §8)

`--json` emits a single object: `totals` (file/typed/untyped/root counts,
`rank_violations`, `promotion_frontier`, `reachable`, `detritus` +
the pre-P1 `detritus_no_typed_edges_pre_p1_artifact` /
`detritus_with_typed_edges_stronger_signal` split + the §2g reference-reachable
split `reference_reachable` / `detritus_reference_reachable_re11_cohort` /
`true_detritus` / `stronger_signal_reference_reachable` /
`stronger_signal_true_detritus`), `rank_histogram`, `roots`,
`rank_violations` (each `{src, src_rank, dep, dep_rank}`),
`unresolved_depends_on_targets`, `promotion_frontier`, `detritus`,
`detritus_reference_reachable_re11_cohort`, `true_detritus`,
`stronger_signal_reference_reachable`, `stronger_signal_true_detritus`,
`reference_reachable_inbound` (per reference-reachable-detritus node: who
back-links it), `expected_unreachable_outside_dag`, `untyped`,
`lowering_theme_notes`, and the `inbound_reference_report`.
`integrator-finalize` runs `--json` at cycle-end and records the `totals` block
(the graded-stack §8 "run the linters at finalize" bullet) — and should now
track **`true_detritus`** (the clean health number) alongside the raw
`detritus`, since the latter over-counts the deliberate RE11 cohort by ~design.

## Fixture (correctness validation)

`fixture/book/src/` is a small hand-authored typed graph that exercises a KNOWN
rank violation + a KNOWN unreachable node + the transitional dual-form + the
migration mapping + the prose-`## Status` leading-token rule (see
`fixture/README.md` for the expected outcomes):

```bash
python3 tools/graded-stack-lint/graded_stack_lint.py \
    --book-src tools/graded-stack-lint/fixture/book/src \
    --show-inbound --reference-reachable
# Expect: 2 rank violations (widget.L4→weak_op, widget-lowering→weak_op),
#         detritus=3 split into true_detritus=2 (L1/orphan, L1-L0/widget-lowering)
#         + reference_reachable=1 (L1/ref_only_leaf, kept reachable only by
#         feature/widget.L4's reference edge — the §2g/RE11 cohort guard),
#         1 untyped concept page, L1/prose_firm_provenance read as FIRM via its
#         prose ## Status line (despite the body mentioning "rough-in"/"stub" —
#         the token-priority bug guard), exit code 1.
```

## Adoption note

This dispatch (cycle-094 P0-B) DELIVERS + dry-run-validates the tooling. The
artifact-wide audit (running the linters over a fully-typed tree and acting on
the results) is **P1** (c095+), AFTER the typing pass populates the scheme.
Pre-P1, expect mostly warnings + artifact-detritus — that is the correct,
graceful-degradation state.
