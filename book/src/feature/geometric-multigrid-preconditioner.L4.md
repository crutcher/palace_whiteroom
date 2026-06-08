---
kind: feature-surface
feature: geometric-multigrid-preconditioner
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/preconditioning-framework
      kind: composes                  # the bind-once preconditioner cap GMG plugs into
    - target: L1/fe_space_hierarchy
      kind: composes                  # GetProlongationOperators() — the level-stack P[l] prolongation GMG restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # kernel-impl: the distributive/Hiptmair relaxation smoother — the faithful blocking smoother constituent
    - target: L1/reciprocal
      kind: composes                  # dinv.Reciprocal() — diagonal-preconditioner extract (GROUNDS RE7)
    - target: L1/normalize
      kind: composes                  # the normalize/reciprocal scaling chain in the smoother diagonal-precond apply (GROUNDS RE5)
    - target: palace/linalg/gmg.cpp:126-205
      kind: cites-evidence            # GeometricMultigridSolver::Mult + VCycle (the V-cycle recursion body)
    - target: palace/linalg/ksp.cpp:206-234
      kind: cites-evidence            # GMG construction with the prolongation operators + smoother config
  reference:
    - feature/lifecycle.L4
    - feature/eigenmode.L4
    - L3/chebyshev                     # the L3 ITERATION-VIEW of the smoother leg (partial-obstruction; sibling-view, NOT a blocking constituent — GROUNDS RE1 reachability)
    - L2/jacobi-smoother               # the L2 iteration-view / point-smoother leg (firm; sibling-view)
    - L2/correction_step               # the per-sweep residual-correction COMBINATOR each smooth + coarse-grid-correction leg names (firm; navigational down-link, NOT a blocking dep — reference-only)
---

# geometric-multigrid preconditioner — L4 composition-root

The **geometric-multigrid (GMG) preconditioner**, presented at L4 as a single composition
of firm L4/L3/L2/L1 vocabulary. This chapter is a *composition root* of the
**infrastructure / shared-substrate** sub-kind (the preconditioner surface every Krylov
solve in every driver hangs under) — NOT a driver-leaf entry point and NOT an output
product. It does not introduce a new combinator; it wires the already-firm vocabulary into
the V-cycle preconditioner that [`preconditioning-framework`](../L4/preconditioning-framework.md)
binds, and links DOWN to each composed piece. (Sub-kind: **driver-agnostic infrastructure**
— a shared postprocess-style surface all preconditioned solves point at, analogous to how
[`energy-fields`](./energy-fields.L4.md) is the driver-agnostic output product, but on the
*solve* side rather than the *postprocess* side.)

GMG is a **spine dependency**: the firm [`divfree_projector`](../L1/divfree_projector.md)
builds a `GeometricMultigridSolver` as its preconditioner (`palace/linalg/divfree.cpp:128`),
and every driver's [`ksp_solve`](../L4/ksp_solve.md) selects GMG as the preconditioner when
the FE-space hierarchy has more than one level (`palace/linalg/ksp.cpp:207-234`). Building
this column is the DIRECTIVE-2 grounded consumer that GROUNDS RE9 / RE1 / RE5 / RE7 by
composing those nodes by name.

## The composition

At L4 the preconditioner is the composition (Haskell-style; the strawman
`book/src/semantics/index.md` notation):

    -- input  = the multigrid operator hierarchy (per-level operators + prolongations + smoothers)
    -- output = a preconditioner action B :: applied as one residual-correction sweep
    geometric_multigrid :: MultigridConfig -> Preconditioner
    geometric_multigrid cfg =
      let levels = fe_space_hierarchy cfg          -- (1) coarse→fine FE-space stack  ── L1/fe_space_hierarchy (firm)
          ps     = prolongations levels            --     P[l] : level l → l+1        ── GetProlongationOperators()
          bs     = [ smoother cfg l | l <- levels ] -- (2) per-level relaxation smoother ── L1/multigrid-relaxation-smoother / L3/chebyshev / L2/jacobi-smoother
          b0     = coarse_solver cfg               --     the level-0 coarse solve
      in  bind_preconditioner (vcycle ps bs b0)    -- (3) bind the V-cycle as a preconditioner ── L4/preconditioning-framework (firm)

    -- the V-cycle itself is a level-recursive combinator (NOT a new vocabulary op; the
    -- recursion structure read off gmg.cpp:172-205). Each smooth + the coarse-grid
    -- correction is a `correction_step` (the L2 residual-correction combinator
    -- `y + B·(x − A·y)`, firm) with a different choice of the preconditioner slot B:
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

1. **The level-stack + prolongations** — [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
   (**firm**). The coarse-to-fine FE-space hierarchy `fespaces[0..L]` is the firm
   `AddLevel`-fold construction; its **prolongation operators** `P[l]` (each lifting level
   `l → l+1`) are exactly what the V-cycle restricts (`Pᵀ`) and prolongs (`P`) over. GMG
   consumes them by name: `fespaces.GetProlongationOperators()` is passed to the
   `GeometricMultigridSolver` constructor (`palace/linalg/ksp.cpp:221,228`;
   `palace/linalg/gmg.cpp:182-201`). **This is the named GMG consumer of the prolongation
   level-stack that GROUNDS RE9.** L0: `GetProlongationOperators()` consumed at
   `ksp.cpp:221`; the lazy `P[l]` materialization at `fespace.cpp:240`.

2. **The per-level smoother leg** — the relaxation smoother
   [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (the
   kernel-impl) wrapping the
   [`L3/chebyshev`](../L3/chebyshev.md) (**partial-obstruction**) /
   [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) (**firm**) polynomial smoothers. Each
   non-coarse level `l` carries a smoother `B[l]` applied as
   `Y ← Y + B(X − A Y)` (pre-smooth `Mult2`, post-smooth `MultTranspose2`;
   `gmg.cpp:184,202`) — i.e. a [`correction_step`](../L2/correction_step.md) (the L2
   residual-correction combinator, firm) with `B` = the per-level point smoother; the
   coarse-grid correction is the same combinator with the conjugated `B = P·B'·Pᵀ` (law 6).
   When an auxiliary H(curl)/H1 space is supplied the smoother is the
   **distributive-relaxation (Hiptmair)** smoother `DistRelaxationSmoother`
   (`gmg.cpp:42-46`; `distrelaxation.cpp:13-36`, which itself folds two
   `ChebyshevSmoother` instances — one on the primary space, one on the auxiliary space);
   otherwise it is a bare `ChebyshevSmoother` / `ChebyshevSmoother1stKind`
   (`gmg.cpp:50-60`). **This is the named consumer that GROUNDS RE1** (the
   chebyshev/jacobi smoother leg). The Chebyshev smoother's diagonal-preconditioner setup
   `op.AssembleDiagonal(dinv); dinv.Reciprocal();` (`chebyshev.cpp:177-178`) is the named
   consumer of the firm [`reciprocal`](../L1/reciprocal.md) /
   [`normalize`](../L1/normalize.md) elementwise chains — **GROUNDS RE5/RE7**.

3. **Bind the V-cycle as a preconditioner** —
   [`preconditioning-framework`](../L4/preconditioning-framework.md) (**firm**). The
   assembled V-cycle action is bound once as the preconditioner `B` that the Krylov
   [`ksp_solve`](../L4/ksp_solve.md) cap applies per iteration — the bind-once
   construction-stratum capture the preconditioning-framework formalizes (the operator is
   set once via `SetOperators`, then `Mult` is const). L0: GMG constructed +
   `EnableTimer()` + returned as the `pc` plugged into the Krylov solver
   (`ksp.cpp:207-234`).

## Inputs / outputs (the feature surface)

- **Input — config + the operator hierarchy.** `MultigridConfig`: the FE-space hierarchy
  (mesh + order schedule → [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)), the
  per-level operators `A[l]` (the geometrically-coarsened bilinear_form operators, built by
  the spaceoperator), the smoother configuration (`mg_smooth_it` / `mg_smooth_order` /
  `mg_smooth_sf_max` / `mg_smooth_sf_min` / `mg_smooth_cheby_4th`), and the coarse-level
  solver. All `readonly` construction-stratum inputs. L0: the
  `GeometricMultigridSolver` constructor parameter list (`gmg.cpp:16-23`).
- **Output — a preconditioner action.** A `Preconditioner` whose `Mult` applies one (or
  `pc_it`) V-cycle sweep — `B(x) ≈ A⁻¹ x` to preconditioner accuracy — consumed per Krylov
  iteration. L0: `GeometricMultigridSolver::Mult` (`gmg.cpp:126-142`).

## Why this is firm

Under the OWN-COMPOSITION promotion rule (a column promotes off its current rung when its
OWN composition + directly-owned constituents are at-rank; cross-linked sibling columns are
references, NOT blockers) **and** the well-foundedness invariant `rank(u) ≤ min(deps)`, this
column is **firm**:

- **The faithful blocking smoother constituent is
  [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)** (kernel-impl,
  firm).
- **[`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) is NOT a blocking
  `depends-on` of this column — it is the L3 *iteration-view* of the smoother**, typed as a
  `reference` (sibling-view). The firm `multigrid-relaxation-smoother` depends on the firm
  [`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md) (the per-level point smoother
  `B`/`B_G`), NOT on `L3/chebyshev`; and it documents the `pc_it` Richardson sweep as a
  **sequential-obstruction that does not gate its L1 firm status** (the sweep is a pure
  `pc_it`-fold parameter at L1). The column inherits exactly that disposition: its V-cycle
  level recursion + `pc_it` Richardson sweep are documented sequential-obstructions, and they
  do not gate the *compositional* firm claim — the same firm-on-positive-structure +
  documented-sequential-obstruction discipline that holds for the smoother itself. (Forcing a
  `column →depends-on→ L3-iteration-view` edge would be an over-edge — the real relationship
  is a sibling-view, so it is a `reference`.)

So every directly-owned **blocking** constituent is firm
([`preconditioning-framework`](../L4/preconditioning-framework.md),
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md),
[`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md),
[`reciprocal`](../L1/reciprocal.md), [`normalize`](../L1/normalize.md)), and
`rank(geometric-multigrid-preconditioner) = firm ≤ min(deps) = firm` holds. The
chebyshev/jacobi iteration-views remain `reference` cross-links (the drift-guard sibling
pointers; they still GROUND RE1's reachability via this live column). The substrate is
cleanly composable BY NAME and the compositional V-cycle algebra is exhaustively cited
(`gmg.cpp:126-205`).

## Single-machine reading (DIRECTIVE-1)

The V-cycle's `Par*`/RAP dependencies (`gmg.cpp` `ParOperator`/`ComplexParOperator` casts at
`:67-93`; the `RealMult`/`RealMultTranspose` over the parallel prolongations) are read
**single-rank** — the multigrid level-recursion + smoother sweep is identical at single
rank; the parallelism is **by composition** (the prolongation `P[l]` and operator `A[l]` are
the single-rank operators, the MPI collectives inside HYPRE/RAP are the deferred MPI layer
DIRECTIVE-1 keeps OUT). No MPI-associated version is lifted here.

## Constituent down-links

| Stage | Constituent | Status | L0 site |
|---|---|---|---|
| level-stack + prolongations | [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) `GetProlongationOperators()` (GROUNDS RE9) | firm | `ksp.cpp:221,228`; `gmg.cpp:182-201`; `fespace.cpp:240` |
| per-level relaxation smoother (blocking dep) | [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (kernel-impl) | firm | `distrelaxation.cpp:13-36`; `gmg.cpp:42-60` |
| Chebyshev polynomial smoother leg — L3 iteration-VIEW (reference; GROUNDS RE1) | [`L3/chebyshev`](../L3/chebyshev.md) | partial-obstruction | `chebyshev.cpp:160-220`; `gmg.cpp:50-60` |
| Jacobi (point) smoother / diagonal gate — L2 iteration-view (reference) | [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) | firm | `chebyshev.cpp:177` (`AssembleDiagonal`) |
| diagonal-precond extract + reciprocal/normalize (GROUNDS RE5/RE7) | [`L1/reciprocal`](../L1/reciprocal.md) / [`L1/normalize`](../L1/normalize.md) | firm | `chebyshev.cpp:177-178` (`AssembleDiagonal(dinv); dinv.Reciprocal()`) |
| bind V-cycle as preconditioner | [`preconditioning-framework`](../L4/preconditioning-framework.md) | firm | `ksp.cpp:207-234` |

## Role

The first **infrastructure / shared-substrate** feature-surface composition-root (DIRECTIVE-2
grounded consumer-(1)). The GC-root marker `feature_root: seed` is preserved (root-role is
permanent/categorical, a separate axis from the resolution ladder). This chapter carries the
*compositional* claim (the GMG preconditioner = this V-cycle composition of these constituent
pieces, GROUNDING RE9/RE1/RE5/RE7 by name), not the constituents' per-op algebraic claims (those
live in the linked chapters). Evidence: `gmg.cpp:126-205` (Mult + VCycle) + `ksp.cpp:206-234`
(construction with the prolongation operators + smoother config) realizing the composition, plus
the firm constituent down-links.
