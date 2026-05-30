---
agent: repairer
mode: producer-style-mechanical-fix
scope: cycle-030 D1 lowering-verifier audit Finding B — three off-by-one cross-anchor citation imprecisions in the L1>L0 theme's cross-reference list to the firm L1 leaf `book/src/L1/back_solve.md`
batch: cycle-031 (batch-9 #1)
dispatch_slot: D4
cycle_id: cycle-031
upstream_source: reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md Finding B (lines 325-336)
target_file: book/src/L1-L0/back-solve-mutation-rotation.md (the theme cross-anchor list at lines 685-694 — citations TO the firm L1 leaf)
leaf_unchanged: book/src/L1/back_solve.md (the citation TARGETS; on-disk content is authoritative and unchanged)
emitted_at: 2026-05-30T050100Z
integrated_at: 2026-05-30T051734Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean (cycle-031 D4). Mechanical 2-token cite-precision substitution in back-solve-mutation-rotation.md cross-anchor bullet (:78→:77-78 signature anchor, :218-221→:217-221 law 5 boundary anchor; third anchor :466-540 confirmed correct-as-is no-op). Closes c030 D1 audit Finding B mechanically. Same-file co-edit with D2 (D2 landed first +17 line offset; D4 cross-anchor bullet shifted from pre-D2 :685-694 to post-D2 :702-711 — both [old] strings unique-in-target on post-D2 on-disk state).
---

# repairer — back-solve L1-leaf cross-anchor off-by-one fixes (cycle-031 D4)

## Scope

Cycle-030 D1 lowering-verifier audit
(`reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md`)
Finding B identified three minor 1-line off-by-one cross-anchor imprecisions in
the L1>L0 theme `book/src/L1-L0/back-solve-mutation-rotation.md`'s
"L1 / cross-theme anchors" list (the bullet at line 685-694 that points at the
firm L1 leaf `book/src/L1/back_solve.md`). The leaf itself is firm and unchanged;
this report applies the precision-tightening edits to the THEME file's
cross-anchor citations TO the leaf.

Note on framing: the task description says "off-by-one cross-anchor citation
imprecisions in the firm L1 leaf `book/src/L1/back_solve.md`". The leaf is the
citation **target** (the anchor destinations); the citation **strings** that
need tightening live in the L1>L0 theme's cross-anchor list. The leaf's
own content is on-disk authoritative and is the verification source of truth
(per CLAUDE.md "on-disk is the citation source of truth, NOT codemap
read_range"). Fixes are applied in the theme file; the leaf is read-only.

## Audit Finding B — verbatim summary

Cycle-030 D1 audit Finding B (audit CYCLE.md lines 325-336) cited three
cross-anchors in `book/src/L1-L0/back-solve-mutation-rotation.md` lines
686-694 that are tight-by-one against the most-precise anchors on disk:

1. `:78` (signature) — the `back_solve` operator NAME is on line 77; the
   `::`-arrow is on line 78. The signature spans `:77-78`. Tighten to
   `:77-78`.
2. `:218-221` (law 5 body) — the law 5 header
   `5. **Empty / single-column boundary.**` is on line 217; the body
   spans `:218-221`. Tighten to `:217-221` to include the header.
3. `:466-540` (cycle-028 `verified_against:` block) — the opening
   ` ```yaml ` fence is on `:466`, the `verified_against:` keyword is on
   `:467`, the closing ` ``` ` fence is on `:540`. **Already correct** as
   the full fenced block; the audit included it for completeness so the
   integrator can audit the full triple. **No change to this citation.**

## On-disk verification (citecheck `--anchor` against
`book/src/L1/back_solve.md`)

All three corrected ranges verified mechanically via `tools/citecheck/`
against the on-disk content of `book/src/L1/back_solve.md` (the leaf is the
citation source of truth; codemap `read_range` not used per CLAUDE.md
directive).

### Fix 1: `:78` → `:77-78` (signature)

Original `:78` (alone, with `back_solve` anchor): **DRIFT**
(`citecheck --anchor 'back_solve' book/src/L1/back_solve.md:78`)
→ "anchor at line 77, -1 outside range 78-78; suggested:
book/src/L1/back_solve.md:77".

Corrected `:77-78` (with `back_solve` anchor): **ok**
(`citecheck --anchor 'back_solve' book/src/L1/back_solve.md:77-78`)
→ "anchor at line(s) [77] within range 77-78"; on-disk content:
```
77 |     back_solve
78 |       :: (R: UpperTri[j+1, j+1], s: Tensor[j+1]) -> Tensor[j+1]
```
The corrected range `:77-78` is the precise signature anchor.

### Fix 2: `:218-221` → `:217-221` (law 5)

Original `:218-221` (with `Empty / single-column boundary` anchor):
**DRIFT** (`citecheck --anchor 'Empty / single-column boundary'
book/src/L1/back_solve.md:218-221`) → "anchor at line 217, -1 outside
range 218-221; suggested: book/src/L1/back_solve.md:217-220".

Corrected `:217-221` (with same anchor): **ok**
(`citecheck --anchor 'Empty / single-column boundary'
book/src/L1/back_solve.md:217-221`) → "anchor at line(s) [217] within
range 217-221"; on-disk content:
```
217 | 5. **Empty / single-column boundary.** The empty restart cycle (`j = -1`) yields
218 |    `y = []` (the `for (int i = j; i >= 0; …)` loop body does not execute,
219 |    `iterative.cpp:653`); the downstream correction `V·y` is the zero vector. The
220 |    single column (`j = 0`) is one scalar division `y[0] = s[0] / R[0][0]`
221 |    (`:656` with the inner `k` loop empty). Both are degenerate cases of law 1.
```
The corrected range `:217-221` includes the law 5 header (:217) plus the
full body (:218-221).

### Fix 3: `:466-540` — already correct (no change)

Verification (with `verified_against` anchor): **ok**
(`citecheck --anchor 'verified_against' book/src/L1/back_solve.md:466-540`)
→ "anchor at line(s) [467] within range 466-540"; on-disk content:
```
466 | ```yaml
467 | verified_against:
...
540 | ```
```
The range `:466-540` is the complete fenced YAML block (opening fence at
:466, `verified_against:` keyword at :467, closing fence at :540). No
change needed; the audit's verdict "CORRECT as-is" stands.

## Net edit summary

The L1>L0 theme `book/src/L1-L0/back-solve-mutation-rotation.md` lines
686-694 cross-anchor bullet (one bullet, three inline citations) goes from:

- `back_solve :: (UpperTri[j+1,j+1], Tensor[j+1]) -> Tensor[j+1]`
  (`:78`) → (`:77-78`)
- `the empty-stream / single-column boundary (law 5, :218-221)` →
  (`:217-221`)
- the cycle-028 `verified_against:` block (`:466-540`) → **unchanged**

Two tight-by-one corrections (Fix 1, Fix 2) + one no-op verification
(Fix 3) = three off-by-one imprecisions cleared.

## Proposed changes

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
- [`L1/back_solve`](../L1/back_solve.md) — the firm L1 operator this theme
  lowers; signature `back_solve :: (UpperTri[j+1,j+1], Tensor[j+1]) ->
  Tensor[j+1]` (`:78`), the defining contract `R · back_solve(R, s) = s`
  (law 1, `:187-195`), the back-substitution recurrence (law 4,
  `:207-215`), the empty-stream / single-column boundary (law 5,
  `:218-221`), basis-lift independence (law 6, `:223-230`), the reduction-
  order non-law (`:234-243`), the singular-`R` applicability boundary
  (`:249-254`), the L1 vs L0 distinction section (`:371-390`), the firm-
  on-positive-structure status (`:330-369`), the cycle-028 `verified_against:`
  block (`:466-540`).
---
- [`L1/back_solve`](../L1/back_solve.md) — the firm L1 operator this theme
  lowers; signature `back_solve :: (UpperTri[j+1,j+1], Tensor[j+1]) ->
  Tensor[j+1]` (`:77-78`), the defining contract `R · back_solve(R, s) = s`
  (law 1, `:187-195`), the back-substitution recurrence (law 4,
  `:207-215`), the empty-stream / single-column boundary (law 5,
  `:217-221`), basis-lift independence (law 6, `:223-230`), the reduction-
  order non-law (`:234-243`), the singular-`R` applicability boundary
  (`:249-254`), the L1 vs L0 distinction section (`:371-390`), the firm-
  on-positive-structure status (`:330-369`), the cycle-028 `verified_against:`
  block (`:466-540`).
```

## Verified-against append (back-solve-mutation-rotation.md `verified_against:` block addendum)

The audit's Finding B `verified_against:` rows for the three cross-anchors
already landed in cycle-030 D1 integration (the back-solve-mutation-rotation
audit was integrated end-of-cycle-030 per integrator-finalize). This dispatch
is the **mechanical enactment** of the Finding B repair direction
(audit CYCLE.md line 336: "bulk-edit the L1 cross-anchor list to use
`:77-78`, `:217-221`, `:466-540`"); no further append is needed to the
theme's `verified_against:` block — the existing rows already record the
`partially-supports` verdict for `:78` and `:218-221` and the `supports`
verdict for `:466-540`. Upon integration of THIS report, those two
`partially-supports` rows become satisfied (the off-by-ones cleared); the
integrator MAY append a single addendum row to the theme's `verified_against:`
block recording the cycle-031 repair, or simply note the closure in the
integrator-finalize log entry. The decision is the integrator's; the leaf is
not modified.

```yaml
# Optional addendum row(s) — integrator's discretion.
# - audit_repair: cycle-031-D4-back-solve-l1-leaf-off-by-one-fixes
#   citations_repaired:
#     - was: book/src/L1/back_solve.md:78        # signature
#       now: book/src/L1/back_solve.md:77-78
#       reason: include the `back_solve` operator-name anchor at :77 (was excluded by tight-by-one).
#     - was: book/src/L1/back_solve.md:218-221   # law 5 body
#       now: book/src/L1/back_solve.md:217-221
#       reason: include the law 5 header at :217 (was excluded by tight-by-one).
#     - confirmed_correct: book/src/L1/back_solve.md:466-540   # verified_against block
#       reason: full fenced YAML block (opening fence :466 → closing fence :540), already correct as a range.
#   verification: citecheck --anchor zero-drift on-disk against book/src/L1/back_solve.md.
#   audited_at: 2026-05-30T050100Z
```

## Status

Three off-by-one imprecisions cleared; the leaf is unchanged (citation
target on-disk is authoritative and was the verification source); the
theme's `firm` status is unaffected; the audit's Finding B is closed by
this mechanical repair.

The leaf `book/src/L1/back_solve.md` remains `firm` per its existing status
section and the cycle-030 D1 audit verdict (`partially-supports` overall,
which was driven by Finding A — a narrative-prose error in Sub-pattern B —
NOT by Finding B, which is purely cross-anchor precision and is now
addressed). Finding A is the subject of a parallel dispatch
(`2026-05-30T050100Z-lifter-back-solve-sub-pattern-b-narrative-repair`); it
is independent of this report.

## Open questions / follow-ups

None. The repair is mechanical and self-contained. The leaf's content was
the verification source; no leaf-side edits were proposed or applied. The
theme's three off-by-one cross-anchor imprecisions are surgical 3-token
substitutions in a single bullet (`:78` → `:77-78`; `:218-221` →
`:217-221`; `:466-540` unchanged).

Closes the off-by-one sub-finding of audit Finding B
(`book/src/L1-L0/back-solve-mutation-rotation.md`); leaves Finding A (the
Sub-pattern B narrative repair) to the parallel lifter dispatch noted above.

## Evidence

- `reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md:325-336`
  — Finding B (the three off-by-one cross-anchor imprecisions and the
  repair direction).
- `book/src/L1-L0/back-solve-mutation-rotation.md:685-694` — the
  cross-anchor bullet whose three inline citations are corrected by the
  proposed-changes block above.
- `book/src/L1/back_solve.md:77-78` — the `back_solve` operator name + `::`
  signature arrow (corrected range for Fix 1). Self-verified via citecheck
  `--anchor 'back_solve'` zero-drift on-disk.
- `book/src/L1/back_solve.md:217-221` — the law 5 `Empty / single-column
  boundary` header + body (corrected range for Fix 2). Self-verified via
  citecheck `--anchor 'Empty / single-column boundary'` zero-drift on-disk.
- `book/src/L1/back_solve.md:466-540` — the cycle-028 `verified_against:`
  fenced YAML block (range confirmed correct for Fix 3, no change).
  Self-verified via citecheck `--anchor 'verified_against'` zero-drift
  on-disk.

```yaml
verified_against:
  - citation: book/src/L1/back_solve.md:77-78
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: citecheck --anchor 'back_solve' zero-drift on-disk; the corrected range for Fix 1 (signature); operator-name anchor at :77 within range; original :78 was tight-by-one (DRIFT confirmed via citecheck).
  - citation: book/src/L1/back_solve.md:217-221
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: citecheck --anchor 'Empty / single-column boundary' zero-drift on-disk; the corrected range for Fix 2 (law 5); header anchor at :217 within range; original :218-221 was tight-by-one (DRIFT confirmed via citecheck).
  - citation: book/src/L1/back_solve.md:466-540
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: citecheck --anchor 'verified_against' zero-drift on-disk; the verified-correct range for Fix 3 (cycle-028 `verified_against:` block); opening fence :466, keyword :467, closing fence :540; no change required.
  - citation: book/src/L1-L0/back-solve-mutation-rotation.md:685-694
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: the cross-anchor bullet whose three inline citations are corrected by the proposed-changes block; the surrounding bullet text (defining contract, recurrence, basis-lift, reduction-order non-law, singular-R boundary, L1-vs-L0 section, status range) is unchanged and not audited here (those ranges were audited firm by cycle-030 D1 and are not part of Finding B).
  - citation: reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md:325-336
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: the cycle-030 D1 lowering-verifier audit Finding B (named finding + the repair direction); the upstream authority for this mechanical repair dispatch.
```
