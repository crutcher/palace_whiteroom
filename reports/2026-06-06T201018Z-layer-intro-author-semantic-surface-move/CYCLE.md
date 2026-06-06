---
agent: layer-intro-author
invoked_at: 2026-06-06T201018Z
scope: semantic-surface PHYSICAL PATH MOVE (design/l4_calculus.md -> semantics/index.md) + cross-reference rewrite
cycle: cycle-116
dispatch: D1 (WAVE-1) of semantic-consolidation-campaign LEAD
status: pending
integrated_at: 2026-06-06T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-116 finalize. VERIFY-NOT-REDO — the dispatch applied all edits directly in book/src;
  the per-report integrator verified the on-disk state. Physical git mv of design/l4_calculus.md
  -> semantics/index.md + ~97-file cross-ref rewrite + new '# Semantic surface' SUMMARY Part
  (after Feature, before L4) + design/index.md reframed to pointer. Reachability/rank-NEUTRAL
  (no frontmatter touched). cargo make book EXIT 0. Graded-stack linter HELD (reachable=133,
  rank_violations=0, detritus=126; files 355->356, expected_unreachable_outside_dag 44->45 —
  the matcher correctly catches semantics/index, NO new orphan). 2 OQs promoted
  (ambiguous-bare-index-md-prose-refs-after-semantic-surface-move,
  l4-entries-section-3.7-line-range-citation-drift). Applied clean, no repair-phase warnings.
---

# CYCLE: semantic-surface path move + 97-file cross-reference rewrite

## Summary

Enacted the cycle-116 LEAD physical path move of the active-management semantic
surface out of `design/` into its own top-level location, and rewrote every
referencing file. The surface content moved **verbatim** (a `git mv`, 0 content
changes — header, §0/§0.1 active-management discipline, §1.2.1/§1.2.2
named-shape-groups, §3.x, §4.1 all intact at the same line numbers). All
referencing files were updated by pure path-prefix substitution that preserves
`:NNN-MMM` line ranges and `§N.N` section refs unchanged (line numbers are stable
because the content moved verbatim).

**Because this is a mechanical file move + bulk link rewrite under a hard build
gate, the edits were performed directly in `book/src/` and the build verified**
(per the dispatch instruction; the integrator should treat these as
already-applied proposed-changes and verify, not re-do).

**Both hard gates PASS:**
- `cargo make book` → **EXIT 0**, "Build Done in 93.00 seconds." linkcheck2 ran
  clean (no broken-link / does-not-exist errors; only pre-existing content-driven
  "Potential incomplete link" warnings on `[...]`/math-bracket prose — see caveat 1).
- `grep -rl 'design/l4_calculus' book/src` → **0** residual.

## What was done (files touched)

### 1. The move
- `git mv book/src/design/l4_calculus.md book/src/semantics/index.md`
  (created `book/src/semantics/`; tracked by git as a pure rename `R`, 0 content
  insertions/deletions).

### 2. Bulk cross-reference rewrite (97 referencing files)
Ordered `sed` substitution across every file in
`grep -rl 'design/l4_calculus' book/src` (most-specific prefix first to avoid the
shared `design/l4_calculus.md` substring collision):
- `book/src/design/l4_calculus.md`  → `book/src/semantics/index.md`  (class (b): prose-text repo-root citations, 99 occurrences; `:NNN-MMM` suffixes preserved automatically since only the path stem is replaced)
- `../design/l4_calculus.md`         → `../semantics/index.md`        (class (a): live markdown links, 87 occurrences; includes inline `` [`l4_calculus`](../semantics/index.md) `` link forms — link TEXT `l4_calculus` left intact, only the target rewritten)
- `./design/l4_calculus.md`          → `./semantics/index.md`         (1 occurrence — SUMMARY.md)

Depth assumption verified: every content file is exactly one level under
`book/src/` (depth 2), so `../design/l4_calculus.md` is uniform; only `SUMMARY.md`
(depth 1) used the `./design/...` form.

### 3. `book/src/SUMMARY.md`
The `# Semantic surface — calculus, rules & abstractions` Part link (line 52)
target `./design/l4_calculus.md` → `./semantics/index.md`. (Picked up by the
`./design/...` substitution above; verified post-edit.)

### 4. `book/src/design/index.md`
DROPPED the hosting bullet (line 9) — the old bullet still carried a same-dir
`(./l4_calculus.md)` link, which is NOT caught by a `design/...`-prefix grep but
would have become a dangling link (the file left `design/`). Replaced with a
one-line "moved to the `# Semantic surface` Part" pointer note:

```edit:book/src/design/index.md
[old]: - [**L4 calculus & spec semantics (active-management surface)**](./l4_calculus.md) — **promoted (2026-06-06, semantic-consolidation directive) out of "design strawman" status into the project's active semantic-management surface** — the single home for the spec's semantic rules / defs / abstractions (shape semantics + named shape groups, the L4/L3 pseudo-language notation invariant, monad / ownership / reduction-rule conventions, the calculus grammar). It now appears in `SUMMARY.md` under the top-level `# Semantic surface` Part placed BEFORE `# L4`, not under Design Artifacts. (Physical path move out of `design/` is the cycle-116 LEAD; the file remains at this path until then.)
[new]: - The **L4 calculus & spec semantics (active-management surface)** has **moved out of Design Artifacts** into its own top-level `# Semantic surface` Part — it now lives at [`book/src/semantics/index.md`](../semantics/index.md) (cycle-116 LEAD, the physical path move enacting the 2026-06-06 semantic-consolidation directive). It is the single home for the spec's semantic rules / defs / abstractions (shape semantics + named shape groups, the L4/L3 pseudo-language notation invariant, monad / ownership / reduction-rule conventions, the calculus grammar).
```

`design/index.md` itself stays in the `# Design Artifacts` SUMMARY Part (unchanged).

### Change accounting
- git status: 99 modified files + 1 tracked rename (`R book/src/design/l4_calculus.md -> book/src/semantics/index.md`, 0 content diff).
- Frontmatter (`edges:` / `rank:`) on the surface and on all referencing files was
  NOT touched — this move is reachability/rank-neutral (the linters key off
  frontmatter + relative-path resolution; relative paths still resolve).

## Supporting evidence
- `grep -rl 'design/l4_calculus' book/src | wc -l` → 0 (post-rewrite gate).
- `cargo make book` → EXIT 0, "Build Done in 93.00 seconds."; linkcheck2 backend
  ran with no broken-link errors.
- `git status --short | grep -E 'semantics/index|design/l4'` →
  `R  book/src/design/l4_calculus.md -> book/src/semantics/index.md`.
- `git diff --cached --stat` for the rename → `1 file changed, 0 insertions(+), 0 deletions(-)`.

## Open questions / caveats

1. **The bare-basename prose references were rewritten to `index.md:NNN`; the
   genuine residual is now an AMBIGUOUS bare-basename `index.md:NNN` prose form
   (non-breaking, build-neutral).** *(Caveat corrected by the cycle-116 D1 repairer
   — the original text claimed bare-basename `l4_calculus.md:NNN-MMM` refs "remain"
   in 4 files; that is NOT the on-disk state. `grep -rn 'l4_calculus\.md' book/src`
   returns **zero** — the bulk `l4_calculus.md` → `index.md` substring substitution
   in fact reached these informal inline-code prose citations too (and D2's
   folded-in cleanup confirmed zero `l4_calculus.md` basename refs remain). The
   class-(b) rewrite ran as a bare-substring rewrite, so e.g.
   `l4_calculus.md:164-171` → `index.md:164-171`, `l4_calculus.md:418` →
   `index.md:418` in `book/src/L4/iterate-while.md`, `book/src/L4/chebyshev.md`,
   `book/src/L4/ksp_solve.md`, `book/src/L4/index.md`.)*

   The real residual: those surviving inline-code prose citations now name the bare
   basename `index.md:NNN` — and `index.md` is the basename of **every** Part
   overview in the book, so as a prose referent it is **ambiguous** (the old
   `l4_calculus.md` was at least unique). They are NOT in markdown link `]()`
   position (inline-code only), so they do NOT break linkcheck2 (build clean, gate
   = 0 holds), and their `:NNN` line ranges remain valid against the verbatim move.
   This is the genuine item for a follow-up sweep to normalize the ambiguous prose
   form (e.g. to `the semantic surface §N.N` / `book/src/semantics/index.md:NNN`).
   Suggested follow-up OQ: `ambiguous-bare-index-md-prose-refs-after-semantic-surface-move`.

2. **Linter `expected-unreachable` outside-DAG set.** Per dispatch note: if the
   reachability linter's `expected-unreachable` matcher keys on
   `methodology/design/index/group-intro` path fragments, the surface's new
   `semantics/index.md` path may flip its membership in that outside-DAG set.
   `index` is a substring of `semantics/index.md`, so it likely still matches an
   `index`-keyed matcher — but the `design`-keyed clause no longer applies. This is
   a benign note for the batch-37 meta to confirm the matcher still classifies the
   surface as expected-unreachable (it is a navigational/semantic non-DAG-node
   surface, `reference`-only inbound). **Not fixed by forcing** — flagging only.

3. **Pre-existing "Potential incomplete link" warnings (135 total, 6 inside the
   moved file).** These are mdbook flagging `[...]` bracket patterns in prose/math
   (`[cycle-051 DEMOTION ...]`, `H[0..k,0..k]`, `Tensor[N]`, etc.) that resemble
   incomplete markdown links. They are content-driven, pre-existed the move (the 6
   inside `semantics/index.md` existed identically when the file was
   `design/l4_calculus.md` — same content, only the warning's path label changed),
   are warnings (not errors), and do not affect EXIT 0. No action.

4. **Pre-existing §3.7 (`iterate_while`) line-range citation drift in several L4
   entries — NOT a D1 defect, tracked for a downstream citation-drift sweep.**
   *(Recorded by the cycle-116 D1 repairer per critic Issue 3.)* Several L4 entries
   cite §3.7 / its small-step rule at `index.md:151-184` / `:164-171` (e.g.
   `book/src/L4/iterate-while.md:211`, `:222`; `book/src/L4/ksp_solve.md:117`,
   `:194`), but on disk §3.7 (`### 3.7 Loops (\`iterate_while\`)`) is at lines
   **190-225** in the moved surface (lines 151-184 are §3.5/§3.6; 164-171 fall in
   §3.3/§3.4). This is a genuine citation-content drift, but it is **pre-existing
   and NOT introduced by D1**: HEAD's `design/l4_calculus.md` had §3.7 at the
   identical line 190 (byte-identical, 513 lines) and the move was a verified
   0-content-diff `git mv`. D1 faithfully preserved the drift; correcting the L4
   citations is **out of D1 scope** (NOT attempted here). Flagged only so it is not
   lost — a candidate for the same downstream citation-drift / prose-ref-normalize
   sweep as caveat 1's ambiguous-basename residual. Suggested follow-up OQ:
   `l4-entries-section-3.7-line-range-citation-drift`.
