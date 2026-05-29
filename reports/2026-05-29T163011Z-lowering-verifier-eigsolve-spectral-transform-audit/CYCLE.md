---
agent: lowering-verifier
invoked_at: 2026-05-29T16:47:39Z
scope: L2>L1 theme audit — eigsolve-spectral-transform-composition
status: pending
inputs:
  - book/src/L2-L1/eigsolve-spectral-transform-composition.md
  - reference/palace/palace/linalg/arpack.cpp:562-590, 733-799, 191-193, 241-247, 263-358
  - reference/palace/palace/linalg/slepc.cpp:1801-1877, 364-394, 674, 694, 715
  - reference/palace/palace/models/modeeigensolver.cpp:1030-1053
  - book/src/L2/eigsolve.md (LHS, firm cycle-023)
  - book/src/L1/{apply_linop,ksp_solve,scal,apply_nonlinear_pencil}.md (RHS leaves, all firm)
  - book/src/L3/eigsolve.md (partial-obstruction boundary, cycle-024)
integrated_at: 2026-05-29T203000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (cycle-026 dispatch-6c). Additive verified_against: YAML block (15 entries, all verdict:supports) appended at EOF; theme stays firm, ZERO content/status change. COMPLETES the lowering-verifier verified_against: audit cohort for all 3 cycle-025-new firm themes (jacobian-action 24 / eigenvalue-correction 19 / eigsolve-spectral-transform 15). Zero gate hits."

# CYCLE: Audit eigsolve-spectral-transform-composition

## Summary

Audited the firm L2>L1 theme `eigsolve-spectral-transform-composition` (authored firm
cycle-025, not yet audited) against concrete L0 evidence. The theme narrates the forward
(high→low) de-fusion of the L2 named composition
`apply_shift_invert = apply_linop(M) ▷ ksp_solve((K−σM)⁻¹) ▷ scale_untransform` into its
firm L1 leaves (`apply_linop`, `ksp_solve`, `scal`), reading the de-fusion off two positive
backend faces — ARPACK's explicit `ApplyOp` hand-assembly and SLEPc's PETSc-`ST`-shell
decomposition (`__pc_apply_EPS` + `__mat_apply_EPS_A0/A1`). **Verdict: fully-supported.**
Every load-bearing anchor lands against on-disk `reference/palace/`, verified mechanically via
`tools/citecheck/citecheck.py --anchor` AND read for meaning via `read_range`. The decisive
finding: **the cycle-025 +7 anchor repair (`__mat_apply_EPS_A1` matvec/scale `:1817→:1824`,
`:1818→:1825`) is confirmed correct on disk and has NOT regressed** — `opM->Mult` is at
`slepc.cpp:1824` and `*= delta*gamma` is at `:1825`, exactly as the repaired theme states.
The two backend faces genuinely realize the claimed L1 sequence; the rewrite is value-preserving
(structural / syntactic expansion of `▷`); the in-scope (per-step body) vs out-of-scope
(eigen-iteration loop = L3 `partial-obstruction`) boundary is clean and not over-claimed; both
RHS leaves are genuinely firm (no speculative operator). One non-defect citation nuance noted
below (the `:715` `GetEigenvalue` anchor is a *content* citation, not a function-name anchor —
the cited line IS the `return l * gamma;` content the theme describes; no drift). Recommend the
additive `verified_against:` block.

## Per-citation audit

The theme's L0 anchor block (§Verified-against, `:285-333`) and the in-body pinpoints
(`:114-126`, `:141-181`, `:285-333`) were each independently `read_range`-confirmed and
`citecheck --anchor`-confirmed. Mechanical results: every anchor `[ok]` except the one
content-vs-function-name nuance flagged.

- **Citation**: `arpack.cpp:562-590` (`ArpackEPSSolver::ApplyOp`)
  - **Theme claim**: the **decisive positive anchor** — line-for-line the L1 two-stage sequence;
    shift-invert branch `opM->Mult(x1,z1)` (`:579`) ▷ `opInv->Mult(z1,y1)` (`:580`) ▷
    `y1 *= gamma` (`:581`); no-transform dual `opK->Mult` (`:573`) ▷ `opInv->Mult` (`:574`) ▷
    `y1 *= 1/gamma` (`:575`); projector tail `opProj->Mult(y1)` (`:586`).
  - **Found**: `read_range(562-590)` shows EXACTLY this. `if (!sinvert) { opK->Mult; opInv->Mult;
    y1 *= 1.0/gamma; } else { opM->Mult; opInv->Mult; y1 *= gamma; } if (opProj) { opProj->Mult(y1); }`.
    citecheck: `opM->Mult`@579, `opInv->Mult`@580 & @574, `opK->Mult`@573, `gamma`@581 & @575,
    `opProj->Mult`@586 — all `[ok]`.
  - **Verdict**: supports.
  - **Notes**: The body is a flawless witness for the de-fusion. The branch structure (sinvert
    vs no-transform) is the spectral-transformation variant axis the theme records; both branches
    are the same `apply_linop ▷ ksp_solve ▷ scal` shape with operand/multiplier swapped.

- **Citation**: `slepc.cpp:1801-1827` (`__mat_apply_EPS_A0` + `__mat_apply_EPS_A1`)
  — **THE LOAD-BEARING CYCLE-025-REPAIRED ANCHORS**
  - **Theme claim**: `__mat_apply_EPS_A0` is `opK->Mult` (`:1809`) + `*= delta` (`:1810`);
    `__mat_apply_EPS_A1` is `opM->Mult` (`:1824`) + `*= delta*gamma` (`:1825`) — the outer
    shell matvecs that SLEPc's `ST` composes with the inverse-apply (the SLEPc-face of stage-1
    `apply_linop` + the `δ`/`δγ` scaling).
  - **Found**: `read_range(1801-1827)` shows `__mat_apply_EPS_A0` body `ctx->opK->Mult(ctx->x1,
    ctx->y1); ctx->y1 *= ctx->delta;` and `__mat_apply_EPS_A1` body `ctx->opM->Mult(ctx->x1,
    ctx->y1); ctx->y1 *= ctx->delta * ctx->gamma;`. citecheck: `opK->Mult`@1809, `delta`@1810
    (A0), `opM->Mult`@1824, `delta`@1825 (A1) — all `[ok]`.
  - **Verdict**: supports. **The cycle-025 repair (`:1817→:1824`, `:1818→:1825`) holds; NO
    regression.** Independently confirmed the off-by-7 is gone and the A1 matvec/scale land at
    `:1824`/`:1825` on disk. (Per dispatch instruction: verified this is NOT the nleps.cpp +1
    codemap artifact — this is a hand-corrected +7 shell-decomposition drift, and it is now
    correct. `read_range` and `citecheck` agree, which is the cross-role adjudication the
    citecheck-as-shared-line-map wiring is meant to provide.)
  - **Notes**: There is a third shell matvec `__mat_apply_EPS_B` (`:1831-1845`, `opB->Mult` ×2)
    in the same source span — NOT cited by the theme (it is the B-matrix metric for the
    generalized inner product, not part of the shift-invert operand stage). Correctly omitted;
    not a coverage gap.

- **Citation**: `slepc.cpp:1847-1877` (`__pc_apply_EPS`)
  - **Theme claim**: the SLEPc shift-invert inverse-apply `y = (K−σM)⁻¹ x`; inner solve
    `ctx->opInv->Mult(ctx->x1, ctx->y1)` (`:1858`, stage-2 `ksp_solve`); no-transform un-scale
    `y1 *= 1/(δγ)` (`:1861`) vs shift-invert un-scale `y1 *= 1/δ` (`:1865`); projector tail
    `opProj->Mult` (`:1870`).
  - **Found**: `read_range(1847-1877)` shows `ctx->opInv->Mult(ctx->x1, ctx->y1); if
    (!ctx->sinvert) { ctx->y1 *= 1.0/(ctx->delta*ctx->gamma); } else { ctx->y1 *= 1.0/ctx->delta;
    } if (ctx->opProj) { ctx->opProj->Mult(ctx->y1); }`. citecheck `opInv->Mult`@1858,
    `opProj->Mult`@1870 `[ok]`; `--show` confirms `:1861 = *= 1.0/(delta*gamma)` and
    `:1865 = *= 1.0/delta`.
  - **Verdict**: supports.
  - **Notes**: The function header comment (`:1849-1851`) literally states "Solve the linear
    system ... y = M⁻¹ x, or shift-and-invert ... y = (K − σ M)⁻¹ x" — a direct in-source
    confirmation that this IS the inner `ksp_solve` stage. The SLEPc decomposition splits what
    ARPACK assembles in one body: the inverse-apply is in `__pc_apply_EPS` (PC shell) and the
    operand matvec is in `__mat_apply_EPS_A1` (Mat shell), composed by SLEPc's STSINVERT
    machinery. The theme's "two backend assembly faces of the same L1 RHS" framing is precisely
    right.

- **Citation**: `arpack.cpp:733-799` + block comment `:736-743` + `opInv->Mult` `:761, 778`
  (`ArpackPEPSolver::ApplyOp`, quadratic PEP)
  - **Theme claim**: the quadratic-PEP shift-invert composition `(L₀−σL₁)⁻¹ L₁` via block
    linearization `L₀ = [[−K,0],[0,M]]`, `L₁ = [[C,M],[M,0]]`; inner-solve sites `:761, 778`.
  - **Found**: `read_range(733-745)` shows the block-comment `L₀ = [-K 0; 0 M]`, `L₁ = [C M; M 0]`
    exactly. citecheck `opInv->Mult`@761 & @778 `[ok]`.
  - **Verdict**: supports.
  - **Notes**: Correctly recorded as a variant-axis operand selection (problem-type=quadratic),
    lowering the same `apply_linop ▷ ksp_solve` way; not over-derived.

- **Citation**: `arpack.cpp:191-193` / `slepc.cpp:364-366` (`SetLinearSolver`, `opInv = &ksp`)
  - **Theme claim**: the inner-solver binding `op.inv = E.linear`.
  - **Found**: both `read_range` confirm `opInv = &ksp;` inside `SetLinearSolver(ComplexKspSolver
    &ksp)`. (SLEPc body is `:364-367`; the theme cites `:364-366` — both bound the same 3-line
    construct and land. Minor: the L2 entry §Signature `:73` cites `:364-367` for the identical
    construct; the 1-line range difference is a cosmetic inconsistency, not a drift — see Open
    questions.)
  - **Verdict**: supports.

- **Citation**: `arpack.cpp:245-246` (`SetShiftInvert`, `sigma = s; sinvert = true;`; precond
  abort `:243-244`)
  - **Theme claim**: the shift binding; precond aborts via MFEM_VERIFY.
  - **Found**: `read_range(241-247)` shows `MFEM_VERIFY(!precond, ...)` at `:243-244`, `sigma = s;`
    at `:245`, `sinvert = true;` at `:246`. Exact.
  - **Verdict**: supports.

- **Citation**: `slepc.cpp:379-394` (`SetShiftInvert`: `STSINVERT` `:388`, `STSetTransform` `:390`,
  `STSetMatMode(st, ST_MATMODE_SHELL)` `:391`, `sigma = s` `:392`)
  - **Theme claim**: spectral-transformation variant-axis source + explicit-vs-ST-shell assembly
    distinction; STPRECOND `:384` vs STSINVERT `:388`.
  - **Found**: `read_range(379-394)` shows `STSetType(st, STPRECOND)` (`:384`), `STSetType(st,
    STSINVERT)` (`:388`), `STSetTransform(st, PETSC_TRUE)` (`:390`), `STSetMatMode(st,
    ST_MATMODE_SHELL)` (`:391`), `sigma = s;` (`:392`). citecheck `STSINVERT`@388,
    `ST_MATMODE_SHELL`@391 `[ok]`.
  - **Verdict**: supports.
  - **Notes**: `ST_MATMODE_SHELL` (`:391`) is the literal source of the theme's claim that "SLEPc
    delegates the assembly to the PETSc ST layer" — the strongest possible anchor for the
    two-faces framing.

- **Citation**: `slepc.cpp:674` (`EPSSetTarget(eps, sigma/gamma)`) and `slepc.cpp:694`
  (`EPSSolve(eps)`)
  - **Theme claim**: `:674` the solve-time deferred target in scaled coords; `:694` the opaque
    library eigen-iteration entry point (boundary reference, NOT lowered).
  - **Found**: citecheck `EPSSetTarget`@674, `EPSSolve`@694 `[ok]`.
  - **Verdict**: supports. Boundary references correctly used as boundary, not re-derived.

- **Citation**: `arpack.cpp:263-358` (`SolveInternal`, `naupd` RCI driver — boundary reference)
  - **Theme claim**: the ARPACK RCI eigen-iteration driver, the opaque library loop NOT lowered.
  - **Found**: range in bounds (`--scan` `[ok]`); the theme correctly references this as the
    out-of-scope loop. (The L3 entry independently pins the RCI callback at `arpack.cpp:318`,
    `:315-339`, consistent with the `:263-358` enclosing range.)
  - **Verdict**: supports.

- **Citation**: `slepc.cpp:715` (`GetEigenvalue` returns `l * γ`)
  - **Theme claim**: the boundary un-scale at extraction restores original-problem coordinates
    (`scale_untransform` tail is informational at the result boundary).
  - **Found**: `--show` confirms `:715 = return l * gamma;`. The `--anchor 'GetEigenvalue'` check
    reports `[DRIFT -1]` (the FUNCTION NAME `GetEigenvalue` is at `:714`). **This is NOT a citation
    drift.** The theme cites `:715` for the *content* "`GetEigenvalue` returns `l * γ`", and
    `:715` IS the `return l * gamma;` statement — the cited line is exactly the described content.
    Citing the return-statement line rather than the function-signature line is correct and
    intentional.
  - **Verdict**: supports.
  - **Notes**: Recorded so the critic does not misread my `--anchor` probe as a regression. The
    correct anchor token for `:715` is `gamma` / `return l`, not the function name. (The L2 entry
    §law 3 cites the same `:715` identically; the L2 §law 2 cites `:711-716` for the broader
    `GetEigenvalue` body — both consistent, no contradiction.)

- **Citation**: `modeeigensolver.cpp:1030-1053` (backend construction: ARPACK
  `SetLinearSolver(*ksp)` `:1037`, SLEPc `SetType(KRYLOVSCHUR)` `:1045` + `SetLinearSolver(*ksp)`
  `:1050`)
  - **Theme claim**: the construction site wiring the inner `ksp_solve` into the eigensolver
    (`op.inv = E.linear`).
  - **Found**: citecheck `SetLinearSolver`@1037, `KRYLOVSCHUR`@1045, `SetLinearSolver`@1050
    `[ok]`; `--scan` confirms `:1030-1053` in bounds.
  - **Verdict**: supports.

- **Citation (L2 LHS)**: `book/src/L2/eigsolve.md:55-77` (§Signature), `:99` (law 1), `:103`
  (law 3), `:105` (law 4), `:163` (§"Lowers from" forward-ref)
  - **Theme claim**: the L2 LHS body + the composition-identity laws this theme lowers.
  - **Found**: `read_range(L2/eigsolve.md 55-77)` shows the `apply_shift_invert` body (`:58-67`)
    inside the `:55-77` range; `:99` IS "Shift-invert composition identity" reading off
    `arpack.cpp:579-581`; `:103` IS "Scaling-coordinate un-transform"; `:105` IS "Inner-solve
    linearity inherited". `:163` IS the §"Lowers from" line literally stating the L2>L1 theme
    "(`L2-L1/eigsolve-spectral-transform-composition`) is pending (a future dispatch)" — this
    theme enacts that forward-reference.
  - **Verdict**: supports. The LHS law citations are precise.

## Applicability conditions

The theme states 6 conditions (`:199-241`). Each walked:

1. **Inner-solver operator bound to the shifted system** (`op.inv` = construction-bound
   `ComplexKspSolver` over already-shifted `(K−σM)`; via `SetShiftInvert` `slepc.cpp:379-394` +
   `SetLinearSolver` `slepc.cpp:364-366`/`arpack.cpp:191-193`).
   - **Verifiable**: yes — `read_range` confirms `SetShiftInvert` binds `sigma`/`STSINVERT` and
     `SetLinearSolver` binds `opInv = &ksp`. The shift is construction state; the per-step body
     (`ApplyOp`/`__pc_apply_EPS`) does not re-shift — confirmed by the bodies (no σ appears in the
     per-step matvec/solve, only `opInv` which is the pre-shifted solver).
   - **Found counter-example?**: no.

2. **Operand-stage operator selected by transform × type tag** (`M` linear / `K` no-transform /
   PEP block `L₁` quadratic).
   - **Verifiable**: yes — `ApplyOp` branches on `sinvert` (`opM` vs `opK`); the PEP body uses the
     block `L₁` (`arpack.cpp:733-799`). The selection is value-bearing (a different spectral
     transform), correctly stated.
   - **Found counter-example?**: no.

3. **`scale_untransform` tail matches backend scaling convention** (`γ`/`1/γ` ARPACK; `1/δ`/`1/(δγ)`
   SLEPc).
   - **Verifiable**: yes — confirmed at `arpack.cpp:581`/`:575` and `slepc.cpp:1865`/`:1861`. The
     boundary-un-scale claim (`GetEigenvalue` returns original coords) confirmed at `slepc.cpp:715`.
   - **Found counter-example?**: no.

4. **Inner-solve non-determinism propagates** (bit-sensitive per-step vector; algorithmic-correctness
   unconditional, bit-reproduction tree-matched).
   - **Verifiable**: inherited from the firm `ksp_solve` leaf (its §"Algebraic laws" non-laws); this
     is a correct re-statement of the standard load-bearing-vs-transparent split (CLAUDE.md
     §"Optimization tricks"), not a new claim. Confirmed `ksp_solve` is firm and carries those
     non-laws.
   - **Found counter-example?**: N/A (inherited, not asserted fresh).

5. **Divergence-free projector applied when bound** (`opProj->Mult`, `arpack.cpp:586` /
   `slepc.cpp:1870`).
   - **Verifiable**: yes — both bodies guard the projector on `if (opProj)` / `if (ctx->opProj)`
     and apply `opProj->Mult(y1)`. Omitting it would drop the `∇·E = 0` constraint — correct.
   - **Found counter-example?**: no.

6. **Loop out of scope (boundary condition)** — the de-fusion is per-step value-equality, NOT
   whole-eigensolve equality; the loop is the L3 `partial-obstruction`.
   - **Verifiable**: yes — confirmed the L3 entry IS `partial-obstruction` (cycle-024) and states
     "the body lifts, the loop does not"; the loop is inside `EPSSolve` (`slepc.cpp:694`) / `naupd`
     RCI (`arpack.cpp:263-358`). The boundary is clean: this theme owns the per-step body, the L3
     entry owns the loop obstruction; no content duplication (the L3 entry references the L2 body
     identity-in-form; this theme references the L3 loop obstruction).
   - **Found counter-example?**: no — the boundary is correctly stated at both ends and not
     over-claimed.

## Algebraic laws (the de-fusion as a lowering)

The theme's justification kind is `structural` (`:243-260`) — the de-fusion IS the syntactic
expansion of the L2 `▷` composition operator read line-for-line off positive source. It also
carries an algebraic flavour (the de-fusion = L2 law 1 read as a lowering; the `scale_untransform`
tail = L2 law 3). Both verified:

- **Law (de-fusion = L2 law 1)**: `apply_shift_invert(op,v) = scale_untransform(ksp_solve(op.inv,
  apply_linop(op.M, v)))`.
  - **Holds on operators?**: yes — this is the literal `ApplyOp` body order
    (`opM->Mult ▷ opInv->Mult ▷ y1 *= gamma`, `arpack.cpp:579-581`), and the L2 entry's law 1
    (`L2/eigsolve.md:99`) is itself read off the same source. The `▷` is by-definition the
    left-to-right dataflow the L1 sequence spells out — the rewrite is value-preserving by
    construction (a structural expansion, not an algebraic re-derivation that could fail).

- **Law (scale_untransform tail = L2 law 3)**: the `γ`/`δ` un-scale is a `scal` post-multiply,
  informational at the boundary.
  - **Holds on operators?**: yes — `scal` is firm; the multiplier is read at `arpack.cpp:581`/`:575`
    and `slepc.cpp:1865`/`:1861`; the boundary un-scale at `GetEigenvalue` (`slepc.cpp:715`)
    restores original coordinates. The `scal` signature (scalar × vector) matches the
    `y1 *= gamma` / `y1 *= 1.0/delta` source ops exactly.

- **Law (inner-solve linearity, L2 law 4)**: `apply_shift_invert` linear in `v` (the per-step
  Krylov substrate).
  - **Holds on operators?**: yes as stated — `apply_linop` exactly linear, `ksp_solve`
    linear-in-RHS modulo tolerance (firm L2 `ksp_solve` law 3); correctly recorded as a constituent
    law, not an `eigsolve`-level law (the eigenproblem is nonlinear in `λ`).

The de-fusion does not assert any law that fails on the operator signatures. The `▷` expansion is
syntactic; the leaves' signatures (`apply_linop :: (A,x)->A·x`, `ksp_solve :: (K,b)->SolveResult`,
`scal`) compose exactly to the per-step body type `Tensor[N,complex] -> Tensor[N,complex]`.

## Speculative L1 operators

**None** — confirmed. The theme's §"Speculative L1 operators" (`:262-277`) claims both RHS stages
plus the two tails are firm vocabulary. Verified all four leaf status lines:
- `apply_linop` — `firm` (stage 1).
- `ksp_solve` — `firm` (stage 2; the solver-as-operator leaf).
- `scal` — `firm` (the `scale_untransform` tail).
- `apply_nonlinear_pencil` — `firm` (the NEP operand-stage reference, correctly recorded as a
  variant-axis selection lowered by the separate NLEPS-deflation cohort, NOT folded into this
  theme).
The LHS `L2/eigsolve` is `firm` (cycle-023). The RHS introduces no new vocabulary. This is a clean
firm-on-both-sides lowering edge.

## Proposed changes

The audit found the theme **fully-supported**. No content edits are needed — the theme is already
`firm` and accurately reflects the source (including the cycle-025-repaired SLEPc shell anchors).
The only proposed change is the additive `verified_against:` block the theme's §Status (`:385-388`)
itself anticipates as "the standard follow-up, not a status reduction".

```edit:book/src/L2-L1/eigsolve-spectral-transform-composition.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/arpack.cpp:562-590
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: ArpackEPSSolver::ApplyOp is line-for-line the L1 sequence — opM->Mult@579 ▷ opInv->Mult@580 ▷ y1*=gamma@581 (shift-invert); opK->Mult@573 ▷ opInv->Mult@574 ▷ y1*=1/gamma@575 (no-transform); opProj->Mult@586 (projector tail). read_range + citecheck all [ok].
  - citation: palace/linalg/slepc.cpp:1801-1827
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: cycle-025 +7 repair CONFIRMED on disk, no regression — __mat_apply_EPS_A0 opK->Mult@1809 *=delta@1810; __mat_apply_EPS_A1 opM->Mult@1824 *=delta*gamma@1825. read_range + citecheck all [ok].
  - citation: palace/linalg/slepc.cpp:1847-1877
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: __pc_apply_EPS inner solve opInv->Mult@1858; un-scale *=1/(delta*gamma)@1861 (no-transform) / *=1/delta@1865 (shift-invert); opProj->Mult@1870. read_range + citecheck all [ok]. Header comment @1849-1851 names it the (K-sigmaM)^-1 x inverse-apply.
  - citation: palace/linalg/arpack.cpp:733-799
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: ArpackPEPSolver::ApplyOp quadratic-PEP operand variant — block comment L0=[[-K,0],[0,M]] L1=[[C,M],[M,0]] @736-743; opInv->Mult@761,778. read_range + citecheck [ok].
  - citation: palace/linalg/arpack.cpp:191-193
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: SetLinearSolver opInv=&ksp (the inner-solver binding op.inv=E.linear). read_range [ok].
  - citation: palace/linalg/arpack.cpp:245-246
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: SetShiftInvert sigma=s@245 sinvert=true@246 (precond MFEM_VERIFY abort @243-244). read_range [ok].
  - citation: palace/linalg/arpack.cpp:263-358
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: SolveInternal naupd RCI driver — the opaque eigen-iteration loop, correctly referenced as the out-of-scope boundary, not lowered. --scan in-bounds [ok].
  - citation: palace/linalg/slepc.cpp:364-366
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: SlepcEigenvalueSolver::SetLinearSolver opInv=&ksp. read_range [ok]. (Body is 364-367; cited 364-366 bounds the same construct — cosmetic 1-line span diff vs L2 entry, not a drift.)
  - citation: palace/linalg/slepc.cpp:379-394
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: SetShiftInvert STPRECOND@384 / STSINVERT@388 / STSetTransform@390 / STSetMatMode ST_MATMODE_SHELL@391 (the ST-shell delegation) / sigma=s@392. read_range + citecheck [ok].
  - citation: palace/linalg/slepc.cpp:674
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: EPSSetTarget(eps, sigma/gamma) deferred scaled-coordinate target. citecheck [ok].
  - citation: palace/linalg/slepc.cpp:694
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: EPSSolve(eps) — the opaque library eigen-iteration entry, correctly referenced as the L3 partial-obstruction boundary, not lowered. citecheck [ok].
  - citation: palace/linalg/slepc.cpp:715
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: GetEigenvalue boundary un-scale — line 715 IS "return l * gamma;" (the content cited). NOT a drift; the function-name token is at 714 but the cited line is the described return content.
  - citation: palace/models/modeeigensolver.cpp:1030-1053
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: backend construction wiring inner ksp into eigensolver — ARPACK SetLinearSolver@1037; SLEPc SetType(KRYLOVSCHUR)@1045 + SetLinearSolver@1050. read_range + citecheck [ok].
  - citation: book/src/L2/eigsolve.md:55-77,99,103,105,163
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: L2 LHS — Signature apply_shift_invert body (58-67 within 55-77); law 1 (composition identity)@99; law 3 (scaling un-transform)@103; law 4 (inner-solve linearity)@105; Lowers-from forward-ref@163 (this theme enacts it). read_range [ok].
  - citation: book/src/L3/eigsolve.md
    verdict: supports
    audited_at: 2026-05-29T16:47:39Z
    note: L3 partial-obstruction boundary (cycle-024) — "body lifts, loop does not"; this theme owns the per-step body, the L3 entry owns the loop sequential-obstruction. Boundary clean, no content duplication.
~~~
```

(No status reduction. The theme remains `firm`. This block is the additive audit-trail the §Status
section anticipated.)

## Supporting evidence

Files consulted:
- `reference/palace/palace/linalg/arpack.cpp` — `:562-590` (EPS ApplyOp), `:733-745` (PEP block
  comment), `:191-193` (SetLinearSolver), `:241-247` (SetShiftInvert).
- `reference/palace/palace/linalg/slepc.cpp` — `:1801-1877` (A0/A1/B shell matvecs +
  `__pc_apply_EPS`), `:364-394` (SetLinearSolver + SetShiftInvert), `:715` (GetEigenvalue return).
- `tools/citecheck/citecheck.py --anchor` / `--show` / `--scan` — mechanical line-map adjudication
  for every anchor (the shared deterministic line-map per the cycle-024 wiring).
- `book/src/L2/eigsolve.md` (LHS, firm cycle-023) — §Signature, laws 1/3/4, §"Lowers from".
- `book/src/L1/{apply_linop,ksp_solve,scal,apply_nonlinear_pencil}.md` — RHS leaf firmness lines
  (all `firm`).
- `book/src/L3/eigsolve.md` (cycle-024 `partial-obstruction`) — the loop-obstruction boundary
  counterpart.

## Open questions / caveats

- **`citecheck --scan` on this CYCLE.md**: run (see below); the audit's own anchors are all in
  bounds / land. The `--scan` over the theme file itself returned all `[ok]` (no out-of-range, no
  bounds failures) across all 14 distinct L0 citations.

- **Cosmetic span inconsistency (NOT a defect, NOT actioned)**: this theme cites
  `slepc.cpp:364-366` for `SetLinearSolver` (`opInv = &ksp`), while the L2 entry §Signature
  (`book/src/L2/eigsolve.md:73`) cites `:364-367` for the identical construct. Both ranges bound
  the same 3–4 line `SetLinearSolver` body and both land; the `:715`-vs-`:711-716` GetEigenvalue
  span is similarly consistent-but-differently-bounded across the two files. These are not drifts
  (the construct is at the cited location in every case) — just non-uniform range widths for the
  same construct across sibling chapters. Left as-is; flagged only so a future lifter/cross-cutter
  doing a uniformity pass is aware. Not in this audit's edit scope.

- **`:715` GetEigenvalue anchor-token nuance (resolved, recorded for the critic)**: a naive
  `citecheck --anchor 'GetEigenvalue' :715` reports `[DRIFT -1]` because the function *name* is at
  `:714`. The theme cites `:715` for the *content* "returns `l * γ`", and `:715` IS
  `return l * gamma;`. This is a correct content-citation, not a drift. The critic should use
  `gamma` (or `return l`) as the `:715` anchor token, not the function name, when re-verifying.

- **Directionality (high→low) — clean**: the formal chapter body narrates the rewrite forward
  (L2 → L1: the named composition de-fuses downward into the per-step body). The single
  reverse-direction note (how an L1 sequence lifts up to the L2 composition) is correctly quarantined
  in §"Open questions / caveats" (`:392-401`) as a working-note, explicitly marked "NOT in the
  high→low chapter body". No direction-of-definition violation.

- **Boundary (per-step body vs eigen-iteration loop) — clean, not over-claiming**: the theme owns
  ONLY the per-step `apply_linop ▷ ksp_solve ▷ scal` de-fusion; the eigen-iteration loop is
  delegated to the L3 `eigsolve` `partial-obstruction` (cycle-024) and referenced, not re-derived.
  Confirmed no content duplication between this theme and the L3 entry. The applicability condition 6
  correctly frames the lowering as a per-step value-equality, NOT a whole-eigensolve equality.

- **OQ disposition** — appended to `scaffolding/open-questions.md`:
  `eigsolve-spectral-transform-composition-lowering-verifier-audit-followup` → **CLOSED /
  fully-supported**. The theme is `firm`, every L0 anchor lands (including the cycle-025-repaired
  SLEPc shell anchors, which did NOT regress), both RHS leaves are firm, the boundary is clean. The
  only follow-up is the integrator attaching the additive `verified_against:` block above. Two
  cosmetic, non-blocking carry-notes (the `:364-366`/`:364-367` span uniformity and the `:715`
  content-vs-function-name anchor token) are recorded for an optional future uniformity pass — neither
  gates anything.
