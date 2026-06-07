---
agent: layer-intro-author
invoked_at: 2026-06-07T112037Z
scope: cycle-124 D7 — bundled cheap-hygiene (correction_step back-links + eigsolve arpack-ido99 citation nit)
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: 331a5ed
integration_notes: "cycle-124 (batch-40 opener) D7. Applied clean. Cheap-hygiene bundle, zero maturity/GC/rank impact: 4 new reference-class L2/correction_step down-links (2 as explicit downward-annotation NON-edges) on the GMG L4/L1 + multigrid-relaxation-smoother + 3 stale ido==99 citation corrections :330-333->:331-334. 2 OQs promoted (interpolator-backward-reference-note-trim-target-unidentified [actionable, next planner]; d7-ido99-citation-plan-path-correction-disposition [informational/resolved])."
---

# CYCLE: D7 — correction_step navigational back-links + the arpack ido-99 citation drift

## Summary

Two cheap-hygiene sub-tasks, all `reference`-class navigational / citation hygiene (no
`depends-on` edges, no maturity changes):

**(a) correction_step back-links (item-4 — the c123-D3-flagged inbound navigational
propagation).** The L2 `correction_step` combinator (firm, c122) names all four call sites on
its OUTWARD face, but the INBOUND back-links from the GMG column + the L1 smoother were
unwritten (c123-D3 verdict; OQ `correction-step-wider-replace-and-propagate-set-l1-and-feature-column`).
This dispatch authors them, respecting the layer direction (CLAUDE.md §"Layers are defined
high→low"):
- **1 L4 `reference` down-link** `feature/geometric-multigrid-preconditioner.L4 → L2/correction_step`
  + reword the L4 `vcycle` recursion prose so pre-smooth / coarse-grid-correction / post-smooth
  each NAME `correction_step` (the conjugated `B = P·B'·Pᵀ` for the coarse-grid leg). This is
  the one site where the layer direction PERMITS a reference edge (L4 *may* reference an L2
  combinator) — the combinator-primary conciseness payoff. (RE11-clean per the c123-meta
  adjudication of OQ `correction-step-l4-reference-edge-adds-to-reference-only-reachable-liveness-evidence`:
  the edge is `reference`-class, carries NO liveness — `correction_step` reaches a root via its
  specialization `reference` edges, NOT via this one; this is navigability completion, not a
  reachability flip.)
- **2 L1 downward annotations** (prose + `reference`-class navigational link, NOT a `depends-on`
  edge — an L1 form cannot depend UP on an L2 abstraction) in
  `L1/multigrid-relaxation-smoother.md` + `feature/geometric-multigrid-preconditioner.L1.md`,
  each naming its per-sweep leg as the L1 realization of `L2/correction_step` with its `B`-slot,
  and EXPLICITLY recording that no `depends-on` edge is created (the relationship is downward).

**(b) eigsolve arpack-ido99 citation nit (item-5).** Correct the carried `:330-333`→`:331-334`
ARPACK ido-99 break-clause citation drift. **PLAN-PATH CORRECTION (flagged below):** the drift
is NOT in `book/src/L1/eigsolve.md` (that file has NO ido-99 citation — verified by full read +
grep). The stale `:330-333` actually lives in `book/src/L3/eigsolve.md` (lines 94, 221) and
`book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (line 188). On-disk verified: `else if (ido
== 99)` is at `arpack.cpp:331`, the break clause spans `:331-334` (`:331` `else if`, `:332` `{`,
`:333` `break;`, `:334` `}`); `:330` is the `ido == 2` close-brace (the off-by-one the
`L3/eigsolve-impl.md:186` carry-forward note already diagnosed). Corrections proposed at the
real homes.

## On-disk citation verification (the ido-99 nit)

`reference/palace/palace/linalg/arpack.cpp` (on-disk grep — the citation source of truth, NOT
codemap; both agreed here):

```
327:    else if (ido == 2)
328:    {
329:      ApplyOpB(&workd.get()[ipntr[0] - 1], &workd.get()[ipntr[1] - 1]);
330:    }
331:    else if (ido == 99)
332:    {
333:      break;
334:    }
335:    else
```

So the `ido == 99` break clause = `:331-334`; `:330` = the `ido == 2` close-brace (NOT part of
the ido-99 clause). The carried `:330-333` is off-by-one on the start. `:331-334` confirmed
correct. (`grep -n "ido == 99" arpack.cpp` → `331:    else if (ido == 99)`.)

## Proposed changes

### (a1) GMG L4 column — add the `L2/correction_step` reference edge

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]:  reference:
    - feature/lifecycle.L4
    - feature/eigenmode.L4
    - L3/chebyshev                     # the L3 ITERATION-VIEW of the smoother leg (partial-obstruction; sibling-view, NOT a blocking constituent — GROUNDS RE1 reachability)
    - L2/jacobi-smoother               # the L2 iteration-view / point-smoother leg (firm; sibling-view)
[new]:  reference:
    - feature/lifecycle.L4
    - feature/eigenmode.L4
    - L3/chebyshev                     # the L3 ITERATION-VIEW of the smoother leg (partial-obstruction; sibling-view, NOT a blocking constituent — GROUNDS RE1 reachability)
    - L2/jacobi-smoother               # the L2 iteration-view / point-smoother leg (firm; sibling-view)
    - L2/correction_step               # the per-sweep residual-correction COMBINATOR each smooth + coarse-grid-correction leg names (firm c122; navigational down-link, NOT a blocking dep — RE11-clean reference-only)
```

### (a2) GMG L4 column — reword the `vcycle` recursion prose to NAME correction_step

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]:    -- the V-cycle itself is a level-recursive combinator (NOT a new vocabulary op; the
    -- recursion structure read off gmg.cpp:172-205):
    vcycle ps bs b0 l x =
      if l == 0
        then b0 x                                       -- coarse solve
        else do { y  <- presmooth  (bs!l) x             -- B[l]->Mult2  (Y ← B(X − A Y))
                ; r  <- residual   (a!l) x y            -- R ← X − A Y         (linalg::AXPBY)
                ; rc <- restrict   (ps!(l-1)) r         -- Pᵀ R              (RealMultTranspose)
                ; ec <- vcycle ps bs b0 (l-1) rc        -- recurse to coarser level
                ; y' <- prolong_add (ps!(l-1)) ec y     -- Y += P E          (RealMult)
                ; postsmooth (bs!l) x y' }              -- B[l]->MultTranspose2

Three composed stages, each a link DOWN to firm vocabulary:
[new]:    -- the V-cycle itself is a level-recursive combinator (NOT a new vocabulary op; the
    -- recursion structure read off gmg.cpp:172-205). Each smooth + the coarse-grid
    -- correction is a `correction_step` (the L2 residual-correction combinator
    -- `y + B·(x − A·y)`, firm c122) with a different choice of the preconditioner slot B:
    -- pre/post-smooth use B = the per-level point smoother; the coarse-grid leg uses the
    -- conjugated B = P·(recursive V-cycle solve)·Pᵀ (correction_step law 6, T = P):
    vcycle ps bs b0 l x =
      if l == 0
        then b0 x                                       -- coarse solve
        else do { y  <- presmooth  (bs!l) x             -- correction_step (B = B[l]); gmg.cpp:184  (Y ← Y + B(X − A Y))
                ; r  <- residual   (a!l) x y            -- R ← X − A Y         (linalg::AXPBY)  ── the correction_step residual stage
                ; rc <- restrict   (ps!(l-1)) r         -- Pᵀ R              (RealMultTranspose)
                ; ec <- vcycle ps bs b0 (l-1) rc        -- recurse to coarser level
                ; y' <- prolong_add (ps!(l-1)) ec y     -- Y += P E          (RealMult)
                ; postsmooth (bs!l) x y' }              -- correction_step (B = B[l]ᵀ); gmg.cpp:204

    -- The pre-smooth → restrict → recurse → prolong-add chain (R ← X − A Y, Pᵀ R, recurse,
    -- Y += P E) is exactly `correction_step A (P·B'·Pᵀ) x y` — the coarse-grid correction as
    -- the conjugated-B specialization of the per-sweep combinator (see
    -- [`correction_step`](../L2/correction_step.md) §"Conjugated preconditioner" + law 6).

Three composed stages, each a link DOWN to firm vocabulary:
```

### (a3) GMG L4 column — name correction_step in the per-level smoother stage prose

```edit:book/src/feature/geometric-multigrid-preconditioner.L4.md
[old]:   non-coarse level `l` carries a smoother `B[l]` applied as
   `Y ← Y + B(X − A Y)` (pre-smooth `Mult2`, post-smooth `MultTranspose2`;
   `gmg.cpp:184,202`). When an auxiliary H(curl)/H1 space is supplied the smoother is the
[new]:   non-coarse level `l` carries a smoother `B[l]` applied as
   `Y ← Y + B(X − A Y)` (pre-smooth `Mult2`, post-smooth `MultTranspose2`;
   `gmg.cpp:184,202`) — i.e. a [`correction_step`](../L2/correction_step.md) (the L2
   residual-correction combinator, firm c122) with `B` = the per-level point smoother; the
   coarse-grid correction is the same combinator with the conjugated `B = P·B'·Pᵀ` (law 6).
   When an auxiliary H(curl)/H1 space is supplied the smoother is the
```

### (a4) GMG L1 column — add the `L2/correction_step` reference edge

```edit:book/src/feature/geometric-multigrid-preconditioner.L1.md
[old]:  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - L3/chebyshev
    - L2/jacobi-smoother
[new]:  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - L3/chebyshev
    - L2/jacobi-smoother
    - L2/correction_step               # DOWNWARD annotation: each pure V-cycle per-sweep leg is the L1 realization of the L2 correction_step combinator (firm c122). NOT a depends-on — an L1 form cannot depend UP on an L2 abstraction (CLAUDE.md §"Layers are defined high→low"); reference-class navigational only.
```

### (a5) GMG L1 column — downward annotation in the per-level smoother prose

```edit:book/src/feature/geometric-multigrid-preconditioner.L1.md
[old]:The residual / update steps (`axpby`, `vadd`) are the firm whole-vector primitives; the body
is whole-tensor by signature shape at each step (the L1 mutation-rotation of the in-place
`R[l]`/`Y[l]` scratch vectors), but the **level recursion and the `pc_it` Richardson sweep
are sequential obstructions** inherited from [`L3/chebyshev`](../L3/chebyshev.md) — see the
L4 surface's §"Why this is rough-in".
[new]:The residual / update steps (`axpby`, `vadd`) are the firm whole-vector primitives; the body
is whole-tensor by signature shape at each step (the L1 mutation-rotation of the in-place
`R[l]`/`Y[l]` scratch vectors), but the **level recursion and the `pc_it` Richardson sweep
are sequential obstructions** inherited from [`L3/chebyshev`](../L3/chebyshev.md) — see the
L4 surface's §"Why this is rough-in".

**Downward annotation (L1 → L2 navigational, NOT a dependency).** Each per-sweep V-cycle leg
(pre-smooth `presmooth (bs!l) x`, the residual+prolong-add coarse-grid correction, post-smooth)
is the L1 pure-function realization of the L2 [`correction_step`](../L2/correction_step.md)
combinator `y + B·(x − A·y)` (firm c122): the smooth legs with `B` = the per-level point
smoother, the coarse-grid leg with the conjugated `B = P·B'·Pᵀ` (correction_step law 6, T = P).
This is a **downward annotation only** — NO `depends-on` edge is created (an L1 form is defined
in L1 vocabulary and cannot depend UP on an L2 abstraction, CLAUDE.md §"Layers are defined
high→low"); the L1 body is already well-grounded in the firm L1 primitives `axpby`/`apply_linop`
that `correction_step` itself decomposes into. The reference is the combinator-primary
navigational link.
```

### (a6) L1/multigrid-relaxation-smoother — add the `L2/correction_step` reference edge

```edit:book/src/L1/multigrid-relaxation-smoother.md
[old]:  reference:
    - target: L1-L0/triangular-solve-obstruction
      kind: realizes-kernel-api        # DIRECTIVE-3: the kept opaque GS-SSOR kernel-api this impl realizes (free, NOT depends-on)
    - L1/set_subvector_zero            # the essential-dof pin on the auxiliary residual x_G (consumed-by, not a spine dep)
    - concepts/sequential-obstruction  # the outer pc_it relaxation-sweep recurrence (documented non-law)
    - L4/preconditioning-framework     # the multigrid V-cycle consumer that installs this as per-level smoother
[new]:  reference:
    - target: L1-L0/triangular-solve-obstruction
      kind: realizes-kernel-api        # DIRECTIVE-3: the kept opaque GS-SSOR kernel-api this impl realizes (free, NOT depends-on)
    - L1/set_subvector_zero            # the essential-dof pin on the auxiliary residual x_G (consumed-by, not a spine dep)
    - concepts/sequential-obstruction  # the outer pc_it relaxation-sweep recurrence (documented non-law)
    - L4/preconditioning-framework     # the multigrid V-cycle consumer that installs this as per-level smoother
    - L2/correction_step               # DOWNWARD annotation: each per-sweep leg (primary B; auxiliary conjugated G·B_G·Gᵀ) is the L1 realization of the L2 correction_step combinator (firm c122). NOT a depends-on (L1 cannot depend UP on L2); reference-class navigational.
```

### (a7) L1/multigrid-relaxation-smoother — downward annotation prose

```edit:book/src/L1/multigrid-relaxation-smoother.md
[old]:1. **Primary leg** (`:104-106`): `y := y + B (x − A·y)`. The point smoother `B`
   is applied to the primary operator `A`; with the input-guess flag set to
   `op.initial_guess || it > 0` (`:105`) so only the very first sweep may skip
   the leading residual.
2. **Auxiliary leg** (`:108-117`): form the primary residual `r = x − A·y`
   (`A->Mult(y, r)` `:109`, then `linalg::AXPBY(1.0, x, -1.0, r)` `:110`);
   restrict it to the auxiliary space `x_G = Gᵀ r` (`:111`); pin the auxiliary
   essential dofs to zero (`:112-115`); relax in the auxiliary space
   `y_G = B_G x_G` (`:116`); prolong the correction back and add
   `y := y + G y_G` (`:117`).
[new]:1. **Primary leg** (`:104-106`): `y := y + B (x − A·y)`. The point smoother `B`
   is applied to the primary operator `A`; with the input-guess flag set to
   `op.initial_guess || it > 0` (`:105`) so only the very first sweep may skip
   the leading residual.
2. **Auxiliary leg** (`:108-117`): form the primary residual `r = x − A·y`
   (`A->Mult(y, r)` `:109`, then `linalg::AXPBY(1.0, x, -1.0, r)` `:110`);
   restrict it to the auxiliary space `x_G = Gᵀ r` (`:111`); pin the auxiliary
   essential dofs to zero (`:112-115`); relax in the auxiliary space
   `y_G = B_G x_G` (`:116`); prolong the correction back and add
   `y := y + G y_G` (`:117`).

**Downward annotation (L1 → L2 navigational, NOT a dependency).** Both legs are
the L1 realization of the L2 [`correction_step`](../L2/correction_step.md)
combinator `y + B·(x − A·y)` (firm c122) with a different `B`-slot: the primary
leg is `correction_step A B x y` (B = the primary point smoother); the auxiliary
leg is `correction_step A (G·B_G·Gᵀ) x y` — the **conjugated** preconditioner
`B = T·B'·Tᵀ` with `T = G` (correction_step law 6, the de-Rham auxiliary-space
specialization). The two-leg sequence is multiplicative (the auxiliary leg reads
the post-primary residual; law 1 above). This is a **downward annotation only** —
NO `depends-on` edge to `correction_step` is created (an L1 form cannot depend UP
on an L2 abstraction, CLAUDE.md §"Layers are defined high→low"); this smoother is
already correctly grounded in the firm L1 primitives `apply_linop` + `axpby` that
`correction_step` itself decomposes into. The link is the combinator-primary
navigational back-reference.
```

### (b1) L3/eigsolve.md:94 — ido-99 citation `:330-333` → `:331-334`

```edit:book/src/L3/eigsolve.md
[old]:   - **ARPACK**: the iteration is a reverse-communication-interface (RCI) loop. Palace's `while(true)` loop (`palace/linalg/arpack.cpp:315-339`) calls the ARPACK driver `naupd` (`palace/linalg/arpack.cpp:318`) and dispatches the per-step matvec `ApplyOp(&workd[ipntr[0]-1], &workd[ipntr[1]-1])` only when `naupd` returns the reverse-communication tag `ido == 1 || ido == -1` (`palace/linalg/arpack.cpp:323-326`), breaking when `ido == 99` (`palace/linalg/arpack.cpp:330-333`). **The loop body is a callback dispatcher, not an algorithm** — all eigen-iteration logic (basis extension, restart, convergence) is inside `naupd`. The `iparam[2] = arpack_it` max-iteration bound (`palace/linalg/arpack.cpp:270`) is an ARPACK parameter, not a Palace-rendered convergence predicate.
[new]:   - **ARPACK**: the iteration is a reverse-communication-interface (RCI) loop. Palace's `while(true)` loop (`palace/linalg/arpack.cpp:315-339`) calls the ARPACK driver `naupd` (`palace/linalg/arpack.cpp:318`) and dispatches the per-step matvec `ApplyOp(&workd[ipntr[0]-1], &workd[ipntr[1]-1])` only when `naupd` returns the reverse-communication tag `ido == 1 || ido == -1` (`palace/linalg/arpack.cpp:323-326`), breaking when `ido == 99` (`palace/linalg/arpack.cpp:331-334`). **The loop body is a callback dispatcher, not an algorithm** — all eigen-iteration logic (basis extension, restart, convergence) is inside `naupd`. The `iparam[2] = arpack_it` max-iteration bound (`palace/linalg/arpack.cpp:270`) is an ARPACK parameter, not a Palace-rendered convergence predicate.
```

### (b2) L3/eigsolve.md:221 — ido-99 citation `:330-333` → `:331-334`

```edit:book/src/L3/eigsolve.md
[old]:- `palace/linalg/arpack.cpp:263-402` — `ArpackEigenvalueSolver::SolveInternal`: the **ARPACK RCI eigen-iteration loop that does NOT lift**. Problem-mode `iparam[6] = sinvert ? 3 : 1` (`:273`, mode-3 shift-invert); max-iteration `iparam[2] = arpack_it` (`:270`); `which::largest_magnitude` (`:278`); the RCI `while(true)` loop (`:315-339`) calling the opaque ARPACK driver `naupd` (`:318`), dispatching `ApplyOp(&workd[ipntr[0]-1], &workd[ipntr[1]-1])` only on `ido == 1 || ido == -1` (`:323-326`), breaking on `ido == 99` (`:330-333`). The decisive negative anchor: Palace's loop body is a callback dispatcher, not an algorithm — the eigen-iteration logic is inside `naupd`. No Palace-authored eigen-step kernel / eigen-iteration driver pair.
[new]:- `palace/linalg/arpack.cpp:263-402` — `ArpackEigenvalueSolver::SolveInternal`: the **ARPACK RCI eigen-iteration loop that does NOT lift**. Problem-mode `iparam[6] = sinvert ? 3 : 1` (`:273`, mode-3 shift-invert); max-iteration `iparam[2] = arpack_it` (`:270`); `which::largest_magnitude` (`:278`); the RCI `while(true)` loop (`:315-339`) calling the opaque ARPACK driver `naupd` (`:318`), dispatching `ApplyOp(&workd[ipntr[0]-1], &workd[ipntr[1]-1])` only on `ido == 1 || ido == -1` (`:323-326`), breaking on `ido == 99` (`:331-334`). The decisive negative anchor: Palace's loop body is a callback dispatcher, not an algorithm — the eigen-iteration logic is inside `naupd`. No Palace-authored eigen-step kernel / eigen-iteration driver pair.
```

### (b3) L3-L2/eigsolve-opaque-eigen-iteration.md:188 — ido-99 citation `:330-333` → `:331-334`

```edit:book/src/L3-L2/eigsolve-opaque-eigen-iteration.md
[old]:breaking on `ido == 99` (`arpack.cpp:330-333`). All eigen-iteration *logic* (basis extension, restart,
[new]:breaking on `ido == 99` (`arpack.cpp:331-334`). All eigen-iteration *logic* (basis extension, restart,
```

## Supporting evidence

- `book/src/L2/correction_step.md` (firm, c122) — the combinator each GMG/smoother per-sweep leg
  names; §"Conjugated preconditioner" + law 6 (`B = T·B'·Tᵀ`, T = P coarse-grid / T = G de-Rham);
  §Specializations (Jacobi / Chebyshev / Distributive-coarse-grid). Outward roster already complete
  (names `gmg.cpp:176/184-188/189-200`, `distrelaxation.cpp:104/108-117`, `chebyshev.cpp:193/264`).
  Already carries `reference: L1/divfree-projector` (borderline) — adding the inbound back-links from
  GMG/smoother completes the bidirectional navigability.
- `reports/2026-06-07T083902Z-same-layer-cross-cutter-correction-step-wider-propagate/CYCLE.md`
  (c123-D3) — the verdict: propagation reaches all consumers; the wiring is **1 L4 reference edge +
  2 L1 downward annotations**, constrained by the L1-can't-depend-up-on-L2 layer direction. Items 1-2
  of its recommendation are exactly (a1)-(a7) here.
- OQ `correction-step-l4-reference-edge-adds-to-reference-only-reachable-liveness-evidence`
  (`scaffolding/open-questions.md:1856,1870`) — CLOSED-adjudicated: the L4→L2 `correction_step`
  reference down-link is a clean RE11 deliberate-reference-only instance; NO-GO on
  reference-carries-liveness. Confirms (a1)/(a4)/(a6) are navigability completion, NOT a
  reachability flip — no GC/rank impact.
- `reference/palace/palace/linalg/arpack.cpp` (on-disk grep, citation source of truth):
  `327: else if (ido == 2)` … `330: }` (ido==2 close-brace) … `331: else if (ido == 99)` … `333:
  break;` … `334: }`. The `ido == 99` break clause = `:331-334`; `:330-333` was off-by-one on the
  start. Matches the `L3/eigsolve-impl.md:186` carry-forward diagnosis verbatim.
- `book/src/L3/eigsolve-impl.md:186` — the `verified_against:` audit note that diagnosed the
  `:330-333`→`:331-334` drift and flagged the "carry-forward to :331-334 for a future lifter." This
  dispatch IS that carry-forward discharge (at the two L3/L3-L2 homes where the stale cite lives).
  The audit record itself is left untouched (append-only-after-integration discipline; its note
  correctly documents the now-discharged carry-forward).

## Open questions / caveats

- **PLAN-PATH CORRECTION — the ido-99 nit is NOT in `book/src/L1/eigsolve.md`.** The D7 scope
  named `book/src/L1/eigsolve.md` for the `:330-333`→`:331-334` correction, but that file has NO
  ido-99 / `:330-333` citation (verified by full 320-line read + `grep -n "330\|331\|ido\|99"`).
  The stale citation actually lives in `book/src/L3/eigsolve.md` (lines 94, 221) +
  `book/src/L3-L2/eigsolve-opaque-eigen-iteration.md` (line 188) — the L3 opaque-eigen-iteration
  obstruction homes where the ARPACK RCI loop is the negative anchor. Proposed corrections at the
  real homes (b1/b2/b3). NOT force-fit onto `L1/eigsolve.md`. (The plan-path error is harmless —
  the integrator applies from this proposed-changes channel at the correct paths.)
- **The "interpolator backward-reference-note trim" (item-5) could not be resolved in scope — no
  specific note identified.** The plan's D7 scope lists "+ the interpolator backward-reference-note
  trim (item-5)" but neither priorities.md item-5 (line 96/112) nor the c123-D3 report names a
  SPECIFIC backward-reference note in `L1/interpolator.md` to trim. The interpolator file's
  references are all faithful forward-consumer notes (`divfree-projector`, `apply_linop`, `fe_space`,
  the GSLIB obstruction sub-note) — none reads as a stale "backward-reference note" needing trimming;
  the c123 re10-interpolator-ground dispatch GROUNDED two inbound `depends-on` edges (divfree /
  waveguide_mode_reduce → interpolator), which is the opposite of a trim. FLAGGED, not force-fit:
  `interpolator-backward-reference-note-trim-target-unidentified` — the next planner / meta should
  specify the exact `file:line` (or confirm it is stale/moot) before re-dispatching. Leaving it
  unauthored is the correct disposition over inventing a trim.
- **No maturity / GC / rank impact.** Every edge added is `reference`-class; no `depends-on` edge,
  no `## Status` flip, no index-table cell change, no consolidated-tally touch. The two L1 sites get
  DOWNWARD annotations explicitly recorded as non-edges (L1-can't-depend-up-on-L2). The citation
  corrections are pure line-number hygiene. `linkcheck2`-safe: all four `correction_step` reference
  links point at the existing `book/src/L2/correction_step.md` (firm, on disk).
- **All files touched are disjoint from the other c124 dispatches** (per the plan overlap analysis:
  D1 touches `L3/eigsolve-impl.md` — a DIFFERENT file from this dispatch's `L3/eigsolve.md`; D3/D4
  the L1 substrate ops; D5 concepts + L1/index; D6 the linear_combination chapters). No shared
  region; PARALLEL-safe.
