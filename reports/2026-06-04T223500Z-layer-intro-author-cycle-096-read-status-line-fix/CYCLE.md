---
agent: layer-intro-author
invoked_at: 2026-06-04T223500Z
scope: tools/ only — fix read_status_line token-priority parse bug in graded_stack_lint.py (D4)
status: integrated
integrated_at: 2026-06-05T001500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean (D4, cycle-096 batch-30 position 3/3). tools/-ONLY deliverable (no book/ edits — artifact-mutation step a confirmation no-op). read_status_line rewritten to the leading-inline-code-token rule (blob-scan removed; _STATUS_TOKENS longest-/most-qualified-first; derive_rank frontmatter-precedence preserved) + NEW regression fixture (fixture/.../prose_firm_provenance.md + widget.L4.md wiring) + README parse-rule paragraph. py_compile clean. Retires the prose-fallback FALSE-POSITIVE class (~20 untyped-node maturity mis-reads). Landed-tree linter: rank_violations 0, histogram now ACCURATE {firm:192, rough-in:7, partly-constructive:3, obstruction:2, partial-obstruction:4}. NOT build-relevant (no book rebuild needed for D4). citecheck 1 "MISS" is a benign tools/-self-reference (graded_stack_lint.py:319-324), not a real artifact-citation defect. OQ graded-stack-lint-read-status-line-token-priority-bug CLOSEABLE at meta unify.
---

# CYCLE: D4 — `read_status_line` token-priority parse-bug fix (`tools/graded-stack-lint/`)

## Summary

`tools/`-ONLY deliverable (NOT a book change; written directly to `tools/` per the
dispatch scope — this report records the writes, it does not propose them through the
integrator's `book/` channel). Fixes the `read_status_line` token-priority parse bug
root-caused by c095 D6/D7 (12 ledger instances, OQ
`graded-stack-lint-read-status-line-token-priority-bug`).

**The bug:** `read_status_line` joined the ~5 lines following a `## Status` heading into
one lowercased blob and scanned for maturity tokens in priority order with
`rough-in`/`stub` BEFORE `firm`. Any genuinely-firm `## Status` whose paragraph merely
*mentions* "rough-in"/"stub" in a downstream provenance phrase (e.g. "promoted from
rough-in", "previously the rough-in (…) caveat", "specialization-stub") was mis-read as
rough-in/stub. This bit ONLY the untyped tail (typed `rank:`/`firmness:`/`status:`
frontmatter nodes never reach the prose fallback).

**The fix:** replaced the 5-line blob-scan-in-priority-order with the
**leading-inline-code-token rule** — read the FIRST non-empty line after the `## Status`
heading and match ONLY its leading `` `token` `` (or `**token**`) decoration, the project
convention that the maturity word is the leading inline-code token. Qualified sub-rank
spellings (`rough-in (test-coverage-bounded)`, `firm (structural)`,
`obstruction (opaque-library-ownership)`) are matched ahead of their bare ladder word so a
sub-rank reads as 2.5, not bare rough-in. `derive_rank`'s precedence is untouched (explicit
`rank:`/`firmness:`/feature-`status:` still win over the prose fallback). The typed-edge
contract and all `book/` content are unchanged.

## Files written (tools/ only — direct writes, recorded not proposed)

- `tools/graded-stack-lint/graded_stack_lint.py` — rewrote `read_status_line` (was lines
  ~310-326); added a module-level `_STATUS_TOKENS` tuple ordered most-qualified-first.
- `tools/graded-stack-lint/fixture/book/src/L1/prose_firm_provenance.md` — NEW regression
  fixture node: a firm node with NO rank frontmatter whose `## Status` leads with
  `` `firm` `` but mentions "rough-in" and "stub" in provenance phrases.
- `tools/graded-stack-lint/fixture/book/src/feature/widget.L4.md` — wired the new node in as
  a `depends-on` of the `widget.L4` root (firm→firm, reachable, no violation).
- `tools/graded-stack-lint/README.md` — documented the leading-inline-code-token parse rule
  (new "Prose `## Status` parse rule" paragraph) + the new fixture-case expectation.
- `tools/graded-stack-lint/fixture/README.md` — added the new node to the graph diagram,
  added assertion #9, updated the confirmed-outputs counts (9→10 files / 8→9 typed /
  reachable 6→7).

## Verification

### Real tree (`python3 tools/graded-stack-lint/graded_stack_lint.py --json`)

| metric | before fix | after fix | note |
|---|---|---|---|
| `rank_violations` | **1** | **0** | the lone residual O1 (`L4/solve_family → solve-family-map-dissolution`) was a prose-fallback FALSE POSITIVE — the dep leads with `` `firm` `` but the blob-scan mis-read `rough-in (test-coverage-bounded)`. Cleared by the parse fix. |
| histogram `firm` | 171 | **191** | +20: the mis-derived untyped-tail nodes now read firm |
| histogram `rough-in` | 13 | 7 | false positives reclassified |
| histogram `partly-constructive` | 8 | 3 | ditto |
| histogram `obstruction` | 10 | 2 | ditto (firm "both endpoints are firm" lowering themes that *mention* obstruction were mis-read) |
| histogram `partial-obstruction` | 4 | 4 | unchanged (genuine `L3/{chebyshev,eigsolve,fold_solve,orthogonalize}`) |
| `promotion_frontier` | 22 | 10 | fewer sub-firm nodes once false rough-ins read firm |
| `typed` / `untyped` / `roots` / `reachable` / `detritus` | unchanged | unchanged | the fix touches only the rank TOKEN of untyped-tail nodes, not graph membership/edges |

**Does the fix change `rank_violations`/histogram?** YES, as expected: it removes the
residual prose-fallback false positives for untyped tail nodes — `rank_violations 1→0` and
+20 firm in the histogram. This is the intended effect (the spec's "removes residual
prose-fallback false positives for untyped tail nodes").

**Note on the typed subset:** the per-node rank of any node carrying explicit
`rank:`/`firmness:`/feature-`status:` frontmatter is UNCHANGED (those bypass the prose
fallback). All deltas above are on UNTYPED-tail nodes that fall through to the prose reader.

**Cross-check of the 13 mismatch nodes** (the 12 ledger instances + O1): every node whose
classification changed was verified to genuinely LEAD with its corrected token:
`L1/{apply_nonlinear_pencil,lu_solve,nleps_*}`, `L2/dot`,
`L3-L2/krylov-step-body-identity`, `L4-L3/{fgmres,gmres}-inner-loop-iterate-while-migration`,
`L4-L3/solve-family-map-dissolution` all lead with `` `firm` `` → now read firm.
`L1-L0/triangular-solve-obstruction` (leads `` `obstruction` ``) was previously mis-read
`rough-in` by the blob-scan and now reads `obstruction` correctly; `L1-L0/bicgstab-iteration`
(leads `` `rough-in (obstruction)` ``) reads `rough-in` correctly. The 9 lowering themes that
left the `obstruction` count (`L1/ksp_solve`, `L2/krylov-step`, the `L3-L2/*` family, the
`L4-L3/{fe-assemble-fold,fold-solve-time-step}-dissolution` pair) all lead with `` `firm` ``
and were mis-classified as obstruction by the blob-scan finding "obstruction" downstream —
these are real corrections, not regressions.

### Fixture (`--book-src tools/graded-stack-lint/fixture/book/src`)

`files=10 typed=9 untyped=1 roots=3 rank_violations=2 reachable=7 detritus=2
promotion_frontier=1 exit=1` — the two pre-existing rank violations (both `→ L1/weak_op`)
and the `L1/orphan` detritus are unchanged; the new `L1/prose_firm_provenance` reads
`firm` (rank 3.0) via the prose `## Status` leading token and adds NO violation.

The new fixture is a genuine guard: re-running the OLD blob-scan logic on
`prose_firm_provenance.md` returns `rough-in (test-coverage-bounded)` (would manufacture a
spurious violation), while the new leading-token rule returns `firm`. Asserted in the
report's verification script.

`python3 -m py_compile` clean.

## Supporting evidence

- Bug location confirmed at the dispatch-cited `graded_stack_lint.py:319-324` (the
  `blob = " ".join(lines[i+1:i+6]).lower()` + priority-ordered token loop).
- The leading-token convention is the dominant on-disk form: a tree-wide survey of the
  first non-empty line after every `## Status` found leading inline-code tokens
  `` `firm` `` (188), `` `partial-obstruction` `` (4), `` `seed` `` (3), `` `rough-in` ``
  (3), `` `partly-constructive` `` (2), plus the qualified forms `` `rough-in (obstruction)` ``,
  `` `obstruction (opaque-library-ownership)` ``, `` `obstruction` ``, `` `firm (structural)` ``.
- Two files lead with a `**bold**` (not inline-code) token (`L1/fe_collection.md`,
  `L1/fe_space.md`); both carry `status: firm` frontmatter so they never reach the prose
  fallback, but the fix accepts the bold form too for robustness.
- One file (`L1-L0/eigsolve-convergence-reason-mapping.md`) leads with an inline-code span
  whose closing backtick wraps to a later line (`` `partly-constructive (structural … ``);
  the fix tolerates the unterminated span by matching the leading WORD, returning
  `partly-constructive` correctly.

## Open questions / caveats

- **Soft interaction with D3 (O1 typing), as the planner flagged (benign).** D3/the lifter
  independently types `L4-L3/solve-family-map-dissolution` with `rank: firm` frontmatter
  this cycle. My fix clears the SAME O1 violation from the prose-fallback side (the dep now
  reads firm without frontmatter). Both independently drive `rank_violations → 0`; they do
  not conflict (different files: the tool vs the theme). At finalize, whichever lands, the
  result is `rank_violations = 0`. If ONLY my fix lands (D3 deferred), O1 is still cleared by
  the parse fix; if ONLY D3 lands (my fix deferred), O1 is cleared by the typed frontmatter —
  but the OTHER 12 untyped-tail mis-classifications would persist, so my fix is the broader
  resolution.
- **The `obstruction` histogram drop (10→2) is large** — verified above that all 8 departing
  nodes are firm lowering themes that merely mention "obstruction" downstream, not genuine
  obstructions losing their kind. The 6 surviving obstruction/partial-obstruction nodes are
  exactly the genuine ones (`L1-L0/{fe-assemble-libceed-boundary,triangular-solve}-obstruction`
  + `L3/{chebyshev,eigsolve,fold_solve,orthogonalize}`). No genuine obstruction was lost.
- **No `book/` content touched**; `scaffolding/priorities.md` shows as modified in
  `git status` but was NOT touched by this dispatch (concurrent/pre-existing change, likely
  the planner's). My writes are confined to `tools/graded-stack-lint/`.
- Resolves OQ `graded-stack-lint-read-status-line-token-priority-bug`. The batch-30
  meta-phase now inherits a linter with `rank_violations = 0` on the real tree and a correct
  prose-fallback parser for its own audit.
