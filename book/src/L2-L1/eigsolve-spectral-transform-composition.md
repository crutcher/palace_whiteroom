# eigsolve-spectral-transform-composition

The per-step pipeline de-fusion for the shift-invert spectral transformation. Lowers the
L2 named composition [`eigsolve`](../L2/eigsolve.md)'s per-step **fold body**
`apply_shift_invert = apply_linop(op.operand) ▷ ksp_solve(op.inv) ▷ scale_untransform`
(`book/src/L2/eigsolve.md`) into its two firm L1 leaves —
[`apply_linop`](../L1/apply_linop.md) (the operator-application stage against `M` / the PEP
block `L₁`) and [`ksp_solve`](../L1/ksp_solve.md) (the inner Krylov solve inverting the shifted
operator `(K − σM)`) — by **expanding the `▷`-composition into the literal Palace per-step
`Mult`-then-inner-solve-then-scale body**. Narrated forward: the one named L2 transformed-operator
application **de-fuses** downward into Palace's two-stage `opM->Mult(x1, z1); opInv->Mult(z1, y1);
y1 *= γ` matvec-then-solve sequence (`palace/linalg/arpack.cpp:579-581`), and this theme records
(a) the **stage de-fusion** — the L2 `▷` becomes the explicit sequencing of `apply_linop` feeding
its result into the inner `ksp_solve`; (b) the **two backend assembly faces** of the same RHS —
ARPACK's explicit hand-assembled `ApplyOp` body vs SLEPc's PETSc-`ST`-shell-decomposed
`__pc_apply_EPS` + `__mat_apply_EPS_A0/A1` triple; (c) the **`scale_untransform` tail** (the
per-backend `γ` / `δ` un-scale) as a `scal` post-multiply that is informational at the result
boundary; and (d) the **divergence-free projector tail** `op.projector->Mult(result)` as an
optional `apply_linop` constituent.

This theme covers the **per-step spectral-transform-apply composition only**. The eigen-iteration
**loop** that folds this composition (Krylov-Schur restart, Arnoldi/Lanczos basis extension,
Rayleigh-Ritz extraction, convergence test) is **out of scope**: it is the witnessed
opaque-library [`sequential-obstruction`](../concepts/sequential-obstruction.md) — SLEPc
`EPSSolve` / ARPACK `naupd` RCI, with **no Palace-authored eigen-step kernel / eigen-iteration
driver pair** analogous to the `(krylov_step, ksp_solve)` pair — documented at L3
[`eigsolve`](../L3/eigsolve.md) (`partial-obstruction`). That obstruction is this
theme's **boundary**, referenced, not re-derived.

It is a sibling of [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md)
and [`gram-fold-specialization`](./gram-fold-specialization.md) (each a
one-named-L2-composition-fans-down-into-firm-L1-leaves theme), with one load-bearing structural
distinction: `eigsolve`'s inner stage is itself the **constructed-solver composition**
[`ksp_solve`](../L1/ksp_solve.md), so this theme is the **first L2>L1 lowering whose RHS composes
a solver-as-operator leaf** (the L2>L1 statement of the L1 observation that `eigsolve` is the first
operator to compose two layers of constructed-operator absorption).

## Slug

`eigsolve-spectral-transform-composition`

## L2 form (LHS)

The L2 form is the named per-step shift-invert spectral-transform application — the **fold body**
the opaque eigen-iteration consumes ([`eigsolve`](../L2/eigsolve.md) §Signature,
`book/src/L2/eigsolve.md:55-77`). It is the only Palace-authored, L2-opened half of the L1
eigsolve opacity; the eigen-iteration fold itself is named by role, not opened:

```text
apply_shift_invert :: (op: SpectralTransformOp, v: Tensor[(S: ...), complex]) -> Tensor[$S, complex]

-- spectral-transformation = none (no transform):        apply M⁻¹ K   (or M⁻¹ alone, per backend)
-- spectral-transformation = shift-invert (linear):      (K − σM)⁻¹ M
-- spectral-transformation = shift-invert (quadratic):   (L₀ − σL₁)⁻¹ L₁   -- PEP block linearization

apply_shift_invert op v =
  let w  = apply_linop op.operand v        -- apply_linop against M (linear) / the PEP block L₁ (quadratic)
  let y  = ksp_solve op.inv w              -- inner ksp_solve inverting the shifted (K − σM) (or (L₀ − σL₁))
  in scale_untransform op y                -- the per-backend γ / δ un-scale (informational coordinate bookkeeping)
```

where the composition operator `▷` denotes left-to-right dataflow: the `apply_linop` result feeds
the inner `ksp_solve`, whose result feeds the `scale_untransform` tail. The composition is
**pure / value-producing** at L2 (it consumes `op` and `v`, produces the transformed vector;
there is no destination buffer in the L2 surface). The shift `σ` and spectral-transform mode
(STSINVERT exact-inverse vs STPRECOND approximate-inverse) are bound into `op.inv`'s operator at
construction (`book/src/L2/eigsolve.md` §Signature `op.inv`; the L0 `SetShiftInvert`,
`palace/linalg/slepc.cpp:379-394`); the inner solve sees an already-shifted system operator.

The L2 composition-identity laws this theme lowers (read off the positive `ApplyOp` body) are
[`eigsolve`](../L2/eigsolve.md) law 1 (shift-invert composition identity:
`apply_shift_invert(op, v) = scale_untransform(ksp_solve(op.inv, apply_linop(op.M, v)))`,
`book/src/L2/eigsolve.md:99`) and law 3 (the scaling-coordinate un-transform tail,
`book/src/L2/eigsolve.md:103`). Law 4 (inner-solve linearity inherited by the per-step
application, `book/src/L2/eigsolve.md:105`) is the algebraic substrate that makes the de-fused
sequence a Krylov per-step body.


## L1 form (RHS)

The L1 form is the two-stage pipeline spelled out in firm L1 primitives: an
[`apply_linop`](../L1/apply_linop.md) feeding an inner [`ksp_solve`](../L1/ksp_solve.md), followed
by the `scale_untransform` `scal` tail and the optional divergence-free-projector `apply_linop`
tail ([`L1/apply_linop`](../L1/apply_linop.md) §Signature; [`L1/ksp_solve`](../L1/ksp_solve.md)
§Signature). At this RHS the operands are the **concrete Palace `Vector`s** — genuinely flat
rank-1 dof-vectors of length `N`, and the operators flat square `LinearOperator[N, N]` — so the
`Tensor[N]` / `LinearOperator[N, N]` rendering here is the literal L0/L1 leaf-call shape, NOT the
shape-generic `(S: ...)` of the L2 composition above (the rank-1-ness is real at the lowered leaf
call; the complex element-type axis lives at the L2 surface above and in the leaves' own overloads):

    apply_linop :: (A: LinearOperator[N, N], x: Tensor[N])      -> Tensor[N]     -- A · x
    ksp_solve   :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]
                                                                   -- (K bound to the shifted (K − σM))

    -- the per-step body is the explicit two-stage sequence:
    apply_shift_invert op v
      ⇒  let w        = apply_linop op.operand v               -- stage 1: M·v (linear) / L₁·v (quadratic)
             result   = ksp_solve op.inv w                     -- stage 2: (K − σM)⁻¹ w via the inner Krylov solve
             scaled   = scal op.scale result.x                 -- tail 1: × γ (ARPACK) / × 1/δ (SLEPc) un-scale
         in maybe_project op.projector scaled                  -- tail 2: optional opProj->Mult divergence-free constraint

At L1 the inner-solve stage takes the **`.x` field** of the `ksp_solve` result `SolveResult[N]`
(the approximate solution to `(K − σM)·w' = w`; [`L1/ksp_solve`](../L1/ksp_solve.md) §Signature) —
the eigen-iteration consumes only the transformed vector, discarding the per-solve statistics
(`converged`, `iterations`, residuals) at the per-step boundary (they propagate to the outer
eigensolve's load-bearing non-determinism but are not part of the transformed vector). The L2
`op.inv` is exactly the construction-bound `ComplexKspSolver` value the L1 `ksp_solve` takes as
`K` (`op.inv = E.linear`; the L0 binding `opInv = &ksp`, `palace/linalg/slepc.cpp:364-366` /
`palace/linalg/arpack.cpp:191-193`). The two L1 leaves are firm: `apply_linop` (firm) and
`ksp_solve` (firm); the RHS introduces no new vocabulary.

## The de-fusion rewrite (L2 → L1)

The lowering reads the spectral-transformation tag (`none | shift-invert | shift-invert-precond`)
and the problem-type tag (`linear | quadratic | nonlinear`) and emits the matching two-stage L1
sequence — the L2 `▷` composition operator becomes the **explicit dataflow sequencing** of the two
firm leaves. This is [`eigsolve`](../L2/eigsolve.md) law 1 (the shift-invert composition identity)
read as a lowering:

    apply_shift_invert { transform = shift-invert, type = linear } op v          -- the canonical case
      =  let w = apply_linop op.M v                              -- opM->Mult(x1, z1)   arpack.cpp:579
             y = ksp_solve op.inv w                              -- opInv->Mult(z1, y1) arpack.cpp:580
         in scal op.gamma y.x                                    -- y1 *= gamma         arpack.cpp:581

    apply_shift_invert { transform = none, type = linear } op v                  -- the no-transform dual
      =  let w = apply_linop op.K v                              -- opK->Mult(x1, z1)   arpack.cpp:573
             y = ksp_solve op.inv w                              -- opInv->Mult(z1, y1) arpack.cpp:574
         in scal (1/op.gamma) y.x                                -- y1 *= 1/gamma       arpack.cpp:575

    apply_shift_invert { transform = shift-invert, type = quadratic } op v       -- the PEP block linearization
      =  let w = apply_linop op.L1 v                             -- L₁ = [[C, M],[M, 0]] block matvec
             y = ksp_solve op.inv w                              -- opInv->Mult(z1, y2/y1) arpack.cpp:761,778
         in scale_untransform op y.x                             -- P(σ) = (L₀ − σL₁) block solve

The **dispatch rule** is: *the L2 `apply_linop op.operand v ▷ ksp_solve op.inv` composition lowers
to the explicit two-stage `apply_linop`-then-`ksp_solve` sequence, with `op.operand` and the
inner-solve operator selected by the spectral-transformation × problem-type tag pair*. The de-fusion
is **structural** (a syntactic expansion of the `▷` operator) — the L1 sequence computes the same
transformed vector the L2 composition denotes, because the L2 form's `▷` is by definition the
left-to-right dataflow the L1 sequence spells out.

### Two backend assembly faces of the same L1 RHS

The same `apply_linop ▷ ksp_solve` RHS materializes at two distinct L0 sites — this is the
**backend-orchestration** variant axis ([`eigsolve`](../L2/eigsolve.md) §Variant axes, collapsed at
L2 to the single named composition). The lowering recognizes both as the same L1 sequence:

- **ARPACK (explicit hand-assembly).** `ArpackEPSSolver::ApplyOp`
  (`palace/linalg/arpack.cpp:562-590`) is, line-for-line, the L1 sequence: stage 1 `apply_linop`
  is `opM->Mult(x1, z1)` (`:579`), stage 2 inner `ksp_solve` is `opInv->Mult(z1, y1)` (`:580`),
  the `scale_untransform` tail is `y1 *= gamma` (`:581`), the divergence-free projector tail is
  `opProj->Mult(y1)` (`:586`). The no-transform branch is the dual `opK->Mult` (`:573`) ▷
  `opInv->Mult` (`:574`) ▷ `y1 *= 1/gamma` (`:575`). This is the **decisive positive anchor** for
  the de-fusion — the L1 two-stage sequence is the literal Palace body.

- **SLEPc (PETSc-ST-shell-decomposed).** The same action `y = (K − σM)⁻¹ x` is decomposed across
  the PETSc `ST` shell: the inner-solve stage is `__pc_apply_EPS`'s
  `ctx->opInv->Mult(ctx->x1, ctx->y1)` (`palace/linalg/slepc.cpp:1858`) — the inner `ksp_solve` —
  with the `scale_untransform` tail `y1 *= 1/(δγ)` (no-transform, `:1861`) / `y1 *= 1/δ`
  (shift-invert, `:1865`) and the projector tail `opProj->Mult` (`:1870`); the `apply_linop`
  operator-stage surfaces as the **outer shell matvecs** `__mat_apply_EPS_A0` (`y = δ·opK·x`,
  `opK->Mult` at `:1809`, `*= delta` at `:1810`) and `__mat_apply_EPS_A1` (`y = δγ·opM·x`,
  `opM->Mult` at `:1824`, `*= delta*gamma` at `:1825`), which SLEPc's `STSINVERT` machinery composes
  with the `__pc_apply_EPS` inverse-apply. ARPACK assembles the `apply_linop ▷ ksp_solve` sequence
  by hand; SLEPc delegates the assembly to the PETSc `ST` layer
  (`STSetMatMode(st, ST_MATMODE_SHELL)`, `palace/linalg/slepc.cpp:391`). **The L1 RHS is the same
  sequence either way** — `(K − σM)⁻¹ M v`; the assembly site is the collapsed backend-orchestration
  axis, invariant on the lowered L1 sequence.

### The scale_untransform tail (a coordinate-bookkeeping `scal`, informational at the boundary)

The per-step body's final stage is the Higham `γ` / `δ` un-scale — a `scal` (scalar-times-vector)
post-multiply: ARPACK `y1 *= gamma` (`:581`) / `y1 *= 1/gamma` (`:575`); SLEPc `y1 *= 1/δ` (`:1865`)
/ `y1 *= 1/(δγ)` (`:1861`). This is the `scale_untransform op y` tail of the L2 composition
([`eigsolve`](../L2/eigsolve.md) law 3, `book/src/L2/eigsolve.md:103`); it lowers to a `scal`
applied to the inner-solve result. It is **informational at the result boundary** — the eigen-iteration
runs in scaled `θ`-coordinates, and the boundary un-scale at extraction (`GetEigenvalue` returns
`l * γ`, `palace/linalg/slepc.cpp:715`, referenced from the firm L1 eigsolve law 5) restores
original-problem coordinates. The scaling axis (`NONE | NORM_2`) shapes only this tail's multiplier,
not the de-fusion structure.

### The divergence-free projector tail (an optional `apply_linop` constituent)

When a divergence-free projector `op.projector` is bound, the per-step body applies it after the
inner solve: `opProj->Mult(y1)` (ARPACK `:586`; SLEPc `:1870`). This is an additional
`apply_linop` stage at L1 (`maybe_project`), enforcing the `∇·E = 0` constraint per step inside the
eigen-iteration. It is part of the named composition's tail at L2 ([`eigsolve`](../L2/eigsolve.md)
§Semantics), and lowers to a guarded `apply_linop op.projector` when the projector is non-null.

## What this theme does NOT cover — the eigen-iteration loop obstruction (boundary reference)

The eigen-iteration **loop** that folds `apply_shift_invert` is **out of scope for this theme** and
is the boundary of what an L2>L1 spectral-transform-apply lowering can express. The loop is a
witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in
**opaque-library-ownership**: it is entirely inside SLEPc `EPSSolve(eps)`
(`palace/linalg/slepc.cpp:694`) / ARPACK `naupd`/`neupd` RCI (`palace/linalg/arpack.cpp:263-358`),
with **no Palace-authored eigen-step kernel / eigen-iteration driver pair** analogous to the
`(krylov_step, ksp_solve)` pair. This theme lowers only the **fold body** (the per-step composition
Palace DOES author, in `ApplyOp` / `__pc_apply_EPS`); the fold itself is named by role at L2 and is
the load-bearing obstruction documented at L3 [`eigsolve`](../L3/eigsolve.md) (`partial-obstruction`
— the per-step body lifts identity-in-form, the loop does not lift). **This theme references
that L3 obstruction as its boundary; it does NOT re-derive it.** The distinction from the sibling
[`ksp_solve`](../L1/ksp_solve.md) L2 entry — whose loop IS Palace-authored (`iterative.cpp`) and so
IS opened — is the load-bearing structural fact that makes `eigsolve` the partial-opening case.

## Applicability conditions

The de-fusion lowering preserves the L2 per-step value when:

1. **Inner-solver operator bound to the shifted system.** `op.inv` is the construction-bound
   `ComplexKspSolver` whose system operator is the *already-shifted* `(K − σM)` (linear) / `(L₀ − σL₁)`
   (quadratic) — bound at construction via `SetShiftInvert(σ, mode)`
   (`palace/linalg/slepc.cpp:379-394`) + `SetLinearSolver(ksp)`
   (`palace/linalg/slepc.cpp:364-366` / `palace/linalg/arpack.cpp:191-193`); the per-step inner
   `ksp_solve` sees the shift baked in. The lowering does NOT re-shift; the shift is `op.inv`'s
   construction state.

2. **Operand-stage operator selected by the transform × type tag.** Stage-1 `apply_linop` is against
   `M` (linear shift-invert), `K` (no-transform), or the PEP block `L₁ = [[C, M], [M, 0]]` (quadratic;
   `palace/linalg/arpack.cpp:733-799`). Selecting the wrong operand is value-bearing (a different
   spectral transform). The tag pair is part of `EigSolver[problem]`'s phantom (inherited from L1).

3. **`scale_untransform` tail matches the backend's scaling convention.** The `scal` multiplier is
   `γ` / `1/γ` (ARPACK, `:581`/`:575`) or `1/δ` / `1/(δγ)` (SLEPc, `:1865`/`:1861`); reproducing a
   specific Palace per-step value requires the matching multiplier. The un-scale is informational at
   the result boundary (the eigenvalue accessor undoes it; firm L1 law 5) — value-preservation of the
   *transformed vector* requires the tail, but the *returned eigenvalues* are in original coordinates
   uniformly across backends.

4. **Inner-solve non-determinism propagates (the standard load-bearing-vs-transparent split).** The
   inner `ksp_solve` is non-deterministic at the bit level (inherited from `apply_linop` / `dot`
   reduction-tree non-associativity + orthogonalisation-method bit-determinism;
   [`L1/ksp_solve`](../L1/ksp_solve.md) §"Algebraic laws" non-laws), so the per-step transformed
   vector — and hence the Krylov basis the (opaque) eigen-iteration extends — is bit-sensitive to the
   inner-solve tolerance and reduction tree. The de-fusion is valid under **algorithmic-correctness**
   unconditionally (the L1 sequence computes `(K − σM)⁻¹ M v` to the inner-solve tolerance); under
   **bit-reproduction** only when the inner-solve reduction tree and tolerance are matched (CLAUDE.md
   §"Optimization tricks vs. base algebra").

5. **Divergence-free projector applied when bound.** If `op.projector` is non-null, the
   `maybe_project` tail MUST emit the `apply_linop op.projector` stage (`opProj->Mult`, ARPACK `:586`
   / SLEPc `:1870`); omitting it drops the per-step `∇·E = 0` constraint enforcement and changes the
   converged eigenvectors.

6. **Loop out of scope (the boundary condition).** The de-fusion lowers the per-step body ONLY; the
   eigen-iteration loop folding it is the opaque-library `sequential-obstruction` (L3
   `partial-obstruction`, `book/src/L3/eigsolve.md`). The lowering is a per-step value-equality, NOT a
   whole-eigensolve equality — the latter additionally depends on the (un-lowered) library loop.

## Justification kind

`structural` — the de-fusion rule **is** the syntactic expansion of the L2 `▷` composition operator
into its explicit two-stage dataflow, read **line-for-line** off two positive Palace per-step bodies:
the ARPACK `ApplyOp` explicit assembly (`palace/linalg/arpack.cpp:562-590`, the canonical
`opM->Mult ▷ opInv->Mult ▷ scal` sequence at `:579-581`) and the SLEPc ST-shell-decomposed
`__pc_apply_EPS` + `__mat_apply_EPS_A0/A1` triple (`palace/linalg/slepc.cpp:1801-1827, 1847-1877`).
The L1 RHS is the literal source. An **algebraic** flavour is present (the de-fusion is also the L2
[`eigsolve`](../L2/eigsolve.md) law 1 read as a lowering, and the `scale_untransform` tail is law 3),
matching the sibling [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) /
[`gram-fold-specialization`](./gram-fold-specialization.md) `algebraic` classification — but the
governing fact here is that the composition is **read off positive source as a literal two-stage body**
(the firm-on-positive-structure basis the L2 entry rests on, per the
[`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md) / [`ksp_solve`](../L1/ksp_solve.md)
precedents), so the theme is classified `structural`. The backend-orchestration variant (explicit vs
ST-shell assembly) is a collapsed axis invariant on the lowered sequence; the `scale_untransform`
multiplier is the load-bearing-numerical coordinate residue; the inner-solve non-determinism is
inherited through the firm `ksp_solve` leaf.

## Speculative L1 operators

**None.** Both stages of the L1 RHS are firm vocabulary:

- Stage 1 — [`apply_linop`](../L1/apply_linop.md) (firm): the operator-application against `M`
  (linear) / `K` (no-transform) / the PEP block `L₁` (quadratic).
- Stage 2 — [`ksp_solve`](../L1/ksp_solve.md) (firm): the inner Krylov solve inverting the shifted
  `(K − σM)`. The `scale_untransform` tail is a [`scal`](../L1/scal.md) (firm) post-multiply; the
  divergence-free-projector tail is an [`apply_linop`](../L1/apply_linop.md) (firm) constituent.

The LHS [`eigsolve`](../L2/eigsolve.md) is firm. This theme proposes no new operators —
it is the lowering edge between firm vocabulary on both sides. The **nonlinear (NEP)** problem-type's
per-`λ` operand `A(λ) = K + λC + λ²M + A2(λ)` is the [`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md)
leaf (firm); the NEP per-step body is its own composition (the NLEPS deflation cohort), not re-derived
here — this theme's canonical case is the linear EPS shift-invert; the quadratic PEP and nonlinear NEP
are recorded as variant-axis selections of the operand stage, lowering the same way.

## Evidence

L0 evidence ranges (paths relative to `reference/`):

- `palace/linalg/arpack.cpp:562-590` — `ArpackEPSSolver::ApplyOp`: the **explicit Palace-owned
  shift-invert composition** — the decisive positive anchor for the de-fusion. Shift-invert branch
  `opM->Mult(x1, z1)` (`:579`, stage-1 `apply_linop`), `opInv->Mult(z1, y1)` (`:580`, stage-2 inner
  `ksp_solve`), `y1 *= gamma` (`:581`, `scale_untransform` tail); no-transform branch `opK->Mult`
  (`:573`) / `opInv->Mult` (`:574`) / `y1 *= 1/gamma` (`:575`); divergence-free projector tail
  `opProj->Mult(y1)` (`:586`).
- `palace/linalg/arpack.cpp:733-799` — `ArpackPEPSolver::ApplyOp`: the quadratic-PEP shift-invert
  composition `(L₀ − σL₁)⁻¹ L₁` via the block linearization `L₀ = [[−K, 0], [0, M]]`,
  `L₁ = [[C, M], [M, 0]]` (block comment `:736-743`); the `opInv->Mult` inner-solve sites
  (`:761, 778`). The problem-type=quadratic operand-stage variant.
- `palace/linalg/arpack.cpp:191-193` — `ArpackEigenvalueSolver::SetLinearSolver`: `opInv = &ksp`. The
  inner-solver binding (`op.inv = E.linear`).
- `palace/linalg/arpack.cpp:245-246` — `ArpackEigenvalueSolver::SetShiftInvert`: `sigma = s;
  sinvert = true;` (precond aborts at `:243-244`, MFEM_VERIFY). The shift binding.
- `palace/linalg/arpack.cpp:263-358` — `ArpackEigenvalueSolver::SolveInternal`: the **ARPACK RCI
  eigen-iteration** driver (`naupd` RCI loop). The opaque library loop NOT lowered by this theme — the
  boundary reference.
- `palace/linalg/slepc.cpp:1847-1877` — `__pc_apply_EPS`: the **SLEPc shift-invert inverse-apply**
  `y = (K − σM)⁻¹ x`. Inner solve `ctx->opInv->Mult(ctx->x1, ctx->y1)` (`:1858`, stage-2
  `ksp_solve`); no-transform un-scale `y1 *= 1/(δγ)` (`:1861`) vs shift-invert un-scale `y1 *= 1/δ`
  (`:1865`); divergence-free projector tail `ctx->opProj->Mult(ctx->y1)` (`:1870`). The SLEPc-face
  anchor that the inner solve is the same `ksp_solve`.
- `palace/linalg/slepc.cpp:1801-1827` — `__mat_apply_EPS_A0` (`opK->Mult` `:1809`, `*= delta` `:1810`)
  and `__mat_apply_EPS_A1` (`opM->Mult` `:1824`, `*= delta*gamma` `:1825`): the original-problem
  operator shell matvecs SLEPc's `ST` composes with the inverse-apply (the SLEPc-face of the stage-1
  `apply_linop` + the `δ`/`δγ` scaling).
- `palace/linalg/slepc.cpp:379-394` — `SlepcEigenvalueSolver::SetShiftInvert`: `STSetType(st,
  STPRECOND)` (precond, `:384`) vs `STSetType(st, STSINVERT)` (exact-inverse, `:388`);
  `STSetTransform(st, PETSC_TRUE)` (`:390`); `STSetMatMode(st, ST_MATMODE_SHELL)` (`:391`, the ST-shell
  delegation); `sigma = s` (`:392`). The spectral-transformation variant-axis source + the
  explicit-vs-ST-shell assembly distinction.
- `palace/linalg/slepc.cpp:364-366` — `SlepcEigenvalueSolver::SetLinearSolver`: `opInv = &ksp`. The
  SLEPc inner-solver binding (the SLEPc `op.inv`).
- `palace/linalg/slepc.cpp:674` — `SlepcEPSSolverBase::Customize`: `EPSSetTarget(eps, sigma / gamma)`
  — the solve-time deferred target in scaled coordinates (the `σ/γ` form).
- `palace/linalg/slepc.cpp:694` — `EPSSolve(eps)` inside `SlepcEPSSolverBase::Solve` (`:687`): the
  **opaque library eigen-iteration** entry point — the fold NOT lowered by this theme (boundary
  reference, the L3 `partial-obstruction`).
- `palace/models/modeeigensolver.cpp:1030-1053` — eigensolver-backend construction: ARPACK branch
  `arpack->SetLinearSolver(*ksp)` (`:1037`), SLEPc branch `slepc->SetType(KRYLOVSCHUR)` (`:1045`) +
  `slepc->SetLinearSolver(*ksp)` (`:1050`). The construction site wiring the inner `ksp_solve` into
  the eigensolver (`op.inv = E.linear`).

L2 / L1 / cross-theme anchors:

- `book/src/L2/eigsolve.md` — the firm L2 named composition (LHS). §Signature
  (`apply_shift_invert` body, `:55-77`), law 1 (shift-invert composition identity, `:99`), law 3
  (scaling-coordinate un-transform, `:103`), law 4 (inner-solve linearity, `:105`), the
  backend-orchestration collapsed axis (`:148-151`), the §"Lowers from" forward-reference to this theme
  (`:163`). This theme is that forward-reference enacted.
- `book/src/L1/apply_linop.md` — the firm L1 stage-1 leaf (RHS): `apply_linop :: (A, x) -> A·x`
  (§Signature), the composition law 4 witnessed at `BaseProductOperator::Mult`.
- `book/src/L1/ksp_solve.md` — the firm L1 stage-2 leaf (RHS): `ksp_solve :: (K, b) -> SolveResult`
  (§Signature), the soft-fail / solver-as-operator semantics, the reduction-tree + orthogonalisation
  bit-determinism non-laws inherited by the per-step body.
- `book/src/L3/eigsolve.md` — the L3 `partial-obstruction`: the per-step body lifts
  identity-in-form (this composition); the eigen-iteration loop does not lift (opaque-library
  `sequential-obstruction`). **The boundary reference — this theme covers the body, that entry covers
  the loop obstruction.**
- `book/src/L1/eigsolve.md` — the firm L1 anchor: the opaque eigensolver-as-operator the
  L2 composition unfolds the per-step half of; laws 4/5 (shift-invariance, scaling un-transform)
  restate as this theme's `scale_untransform` boundary + composition identity.
- `book/src/L2-L1/orthogonalize-composition-lowering.md`,
  `book/src/L2-L1/gram-fold-specialization.md` — the sibling L2>L1 themes (structural precedent for a
  one-named-L2-composition-fans-down-into-firm-L1-leaves theme).
- `book/src/concepts/sequential-obstruction.md`, `concepts/solver-as-operator.md`,
  `concepts/constructed-operators.md`, `concepts/variant-absorption.md` — cross-cutting concept anchors
  (the library-owned loop obstruction; the inner solver consumed as an operator; the shifted constructed
  operator; the backend-orchestration absorption).

## Status

`firm` — the L2 LHS and both L1 RHS leaves ([`apply_linop`](../L1/apply_linop.md),
[`ksp_solve`](../L1/ksp_solve.md)) are firm; the de-fusion rule IS the syntactic expansion of the
L2 `▷` composition operator read line-for-line off two positive Palace per-step bodies — the ARPACK
`ApplyOp` explicit assembly (`palace/linalg/arpack.cpp:562-590`, the canonical
`opM->Mult ▷ opInv->Mult ▷ scal` at `:579-581`) and the SLEPc ST-shell-decomposed `__pc_apply_EPS` +
`__mat_apply_EPS_A0/A1` triple (`palace/linalg/slepc.cpp:1801-1827, 1847-1877`). Operator-algebra on
read closures (firm-on-positive-structure), not test-gated.

The theme covers the **per-step spectral-transform-apply composition only**; the eigen-iteration loop
is the opaque-library `sequential-obstruction` documented at L3 [`eigsolve`](../L3/eigsolve.md)
(`partial-obstruction`), referenced as the boundary, not re-derived.

## Open questions / caveats

- **NEP per-step body is a separate composition (out of scope).** The nonlinear (NEP)
  problem-type's per-`λ` operand is the [`apply_nonlinear_pencil`](../L1/apply_nonlinear_pencil.md) leaf;
  the NEP per-step body (the NLEPS quasi-Newton / deflation cohort) is its own composition, lowered by the
  NLEPS-deflation L2>L1 cohort (`deflate-composition-lowering` et al.), not this theme. This theme's
  canonical case is the linear EPS shift-invert; the quadratic PEP is a clean operand-stage variant
  (the block `L₁`), but the NEP body is genuinely distinct and not folded in here.
