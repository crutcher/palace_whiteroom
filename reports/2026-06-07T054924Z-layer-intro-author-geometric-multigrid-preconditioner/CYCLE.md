---
agent: layer-intro-author
invoked_at: 2026-06-07T054924Z
scope: geometric-multigrid-preconditioner feature-surface column (DIRECTIVE-2 grounded consumer-(1), batch-39 LEAD)
status: pending
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied (sanctioned integration-sequencing exception). GMG L4+L1 columns rough-in + NEW Infrastructure feature sub-kind. Grounds RE9/RE1/RE5/RE7."
---

# CYCLE: geometric-multigrid preconditioner feature-surface column

## Summary

Authors the **geometric-multigrid (GMG) preconditioner feature-surface column** — the
DIRECTIVE-2 grounded consumer-(1), the highest-fan-out lift-through lead. It is a
**driver-agnostic infrastructure / shared-substrate feature column** (a *preconditioner
surface*, the thing every Krylov solve in every driver hangs under — NOT a driver-leaf
entry point and NOT an output product). The column is a composition-root that wires BY
NAME, via faithful `depends-on (composes)` edges, the GMG V-cycle's already-firm
constituents:

- the firm [`L4/preconditioning-framework`](../L4/preconditioning-framework.md) (the
  bind-once preconditioner cap GMG plugs into; firm c096),
- the per-level **smoother leg** — the relaxation smoother (D3's kernel-impl, canonical
  slug `book/src/L1/multigrid-relaxation-smoother.md`, forward-referenced) wrapping the
  [`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) / [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) (firm) Chebyshev/Jacobi polynomial smoothers,
- the **level-stack prolongation** — [`L1/fe_space_hierarchy`](../L1/fe_space_hierarchy.md)'s
  `GetProlongationOperators()` (firm; `P[l]` lifts level `l → l+1`) — **the named GMG
  consumer of the prolongation operators, which GROUNDS RE9**,
- the smoother's **diagonal-preconditioner extract/apply + reciprocal/normalize chains** —
  the firm [`L1/reciprocal`](../L1/reciprocal.md) / [`L1/normalize`](../L1/normalize.md) —
  the named consumer that **GROUNDS RE5/RE7** (`chebyshev.cpp:177-178`:
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();`).

**RE-discharge wiring (the c122 re-check target):** building this named consumer composes
RE9 (prolongation), RE1 (chebyshev/jacobi smoother leg), RE5 + RE7 (diagonal-precond
apply/extract + reciprocal/normalize) by name via faithful `depends-on` edges, so the c122
linter re-run can confirm those nodes become reachable through this column's chain.

**Clean-gate landing — `rank: rough-in`, NOT firm.** Well-foundedness
(`rank(u) ≤ min(deps)`) forbids `firm`: the column's smoother leg rests on
[`L3/chebyshev`](../L3/chebyshev.md) (**partial-obstruction**, the witnessed
inner-`k`-recurrence + outer Richardson sweep sequential obstruction — `chebyshev.md`
`## Status`) and on D3's `multigrid-relaxation-smoother` kernel-impl, which is
**forward-referenced this cycle and not yet firm on disk**. The honest status is
**rough-in**; the column promotes when the smoother leg firms (a c122+ re-check). The GC-root
marker `feature_root: seed` is preserved (root-role is permanent + categorical, a separate
axis from the resolution ladder).

Deliverables:
1. `book/src/feature/geometric-multigrid-preconditioner.L4.md` (new) — L4 composition-root.
2. `book/src/feature/geometric-multigrid-preconditioner.L1.md` (new) — L1 pure-function surface.
3. `book/src/feature/infrastructure.md` (new) — the **infrastructure / shared-substrate**
   kind-group intro page (NEW by-kind grouping → its group-intro authored in the SAME
   landing, per the new-summary-kind-grouping rule).
4. `book/src/feature/index.md` — matrix: add the infrastructure grouping + the GMG row.
5. `book/src/SUMMARY.md` — nest the new `Infrastructure / shared-substrate` grouping +
   the GMG column's high→low (L4→L1) levels under the Feature Part.

D1↔D3 forward-reference: the canonical slug `book/src/L1/multigrid-relaxation-smoother.md`
is stated in BOTH scopes; the per-report integrator wires the live link when D3 lands. The
`realizes-kernel-api` edge mechanics are D3's job, not mine.

## Proposed changes

```new-file:book/src/feature/geometric-multigrid-preconditioner.L4.md
---
kind: feature-surface
feature: geometric-multigrid-preconditioner
level: L4
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L4/preconditioning-framework
      kind: composes                  # the bind-once preconditioner cap GMG plugs into (firm c096)
    - target: L1/fe_space_hierarchy
      kind: composes                  # GetProlongationOperators() — the level-stack P[l] prolongation GMG restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # D3 kernel-impl: the distributive/Hiptmair relaxation smoother (forward-ref, lands same cycle)
    - target: L3/chebyshev
      kind: composes                  # the per-level Chebyshev polynomial smoother leg (partial-obstruction; GROUNDS RE1)
    - target: L2/jacobi-smoother
      kind: composes                  # the Jacobi (point) smoother leg / diagonal-preconditioner gate (firm)
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

GMG is a **spine dependency**: the firm [`divfree-projector`](../L1/divfree-projector.md)
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

1. **The level-stack + prolongations** — [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
   (**firm**, c117). The coarse-to-fine FE-space hierarchy `fespaces[0..L]` is the firm
   `AddLevel`-fold construction; its **prolongation operators** `P[l]` (each lifting level
   `l → l+1`) are exactly what the V-cycle restricts (`Pᵀ`) and prolongs (`P`) over. GMG
   consumes them by name: `fespaces.GetProlongationOperators()` is passed to the
   `GeometricMultigridSolver` constructor (`palace/linalg/ksp.cpp:221,228`;
   `palace/linalg/gmg.cpp:182-201`). **This is the named GMG consumer of the prolongation
   level-stack that GROUNDS RE9.** L0: `GetProlongationOperators()` consumed at
   `ksp.cpp:221`; the lazy `P[l]` materialization at `fespace.cpp:240`.

2. **The per-level smoother leg** — the relaxation smoother
   [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (D3's
   kernel-impl, forward-referenced this cycle) wrapping the
   [`L3/chebyshev`](../L3/chebyshev.md) (**partial-obstruction**) /
   [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) (**firm**) polynomial smoothers. Each
   non-coarse level `l` carries a smoother `B[l]` applied as
   `Y ← Y + B(X − A Y)` (pre-smooth `Mult2`, post-smooth `MultTranspose2`;
   `gmg.cpp:178,202`). When an auxiliary H(curl)/H1 space is supplied the smoother is the
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
   [`preconditioning-framework`](../L4/preconditioning-framework.md) (**firm**, c096). The
   assembled V-cycle action is bound once as the preconditioner `B` that the Krylov
   [`ksp_solve`](../L4/ksp_solve.md) cap applies per iteration — the bind-once
   construction-stratum capture the preconditioning-framework formalizes (the operator is
   set once via `SetOperators`, then `Mult` is const). L0: GMG constructed +
   `EnableTimer()` + returned as the `pc` plugged into the Krylov solver
   (`ksp.cpp:207-234`).

## Inputs / outputs (the feature surface)

- **Input — config + the operator hierarchy.** `MultigridConfig`: the FE-space hierarchy
  (mesh + order schedule → [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)), the
  per-level operators `A[l]` (the geometrically-coarsened bilinear-form operators, built by
  the spaceoperator), the smoother configuration (`mg_smooth_it` / `mg_smooth_order` /
  `mg_smooth_sf_max` / `mg_smooth_sf_min` / `mg_smooth_cheby_4th`), and the coarse-level
  solver. All `readonly` construction-stratum inputs. L0: the
  `GeometricMultigridSolver` constructor parameter list (`gmg.cpp:16-23`).
- **Output — a preconditioner action.** A `Preconditioner` whose `Mult` applies one (or
  `pc_it`) V-cycle sweep — `B(x) ≈ A⁻¹ x` to preconditioner accuracy — consumed per Krylov
  iteration. L0: `GeometricMultigridSolver::Mult` (`gmg.cpp:126-142`).

## Why this is rough-in (not firm)

Under the OWN-COMPOSITION promotion rule (a column promotes off its current rung when its
OWN composition + directly-owned constituents are at-rank; cross-linked sibling columns are
references, NOT blockers) **and** the well-foundedness invariant `rank(u) ≤ min(deps)`, this
column is **rough-in**, not firm:

- Its directly-owned **smoother leg** rests on [`L3/chebyshev`](../L3/chebyshev.md), which
  is **partial-obstruction** (`chebyshev.md` `## Status`: the per-step body lifts cleanly
  to a whole-tensor expression, but the inner `k`-recurrence and the outer `pc_it`
  Richardson sweep are *witnessed sequential obstructions* — the V-cycle inherits this
  un-liftable iteration in the same way).
- Its [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) constituent
  is D3's kernel-impl, **forward-referenced this cycle and not yet firm on disk**; the
  well-foundedness invariant caps this column at no more resolved than that constituent.

So `rank(geometric-multigrid-preconditioner) ≤ min(rank(chebyshev), rank(relaxation-smoother))`
holds only at rough-in. The other directly-owned constituents ARE firm
([`preconditioning-framework`](../L4/preconditioning-framework.md),
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md),
[`jacobi-smoother`](../L2/jacobi-smoother.md), [`reciprocal`](../L1/reciprocal.md),
[`normalize`](../L1/normalize.md)); the column is held at rough-in only by the smoother leg.
**Promotion condition:** the smoother leg firms (D3's `multigrid-relaxation-smoother`
promotes to firm AND the chebyshev partial-obstruction's V-cycle recursion is either lifted
or accepted as a documented sequential-obstruction at the column level) — a c122+ re-check.

This is the clean-gate landing (the redirect's verify-present discipline): the substrate is
cleanly composable BY NAME, but its smoother leg is not yet firm, so the column lands
rough-in rather than forcing a firm claim.

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
| level-stack + prolongations | [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) `GetProlongationOperators()` (GROUNDS RE9) | firm (c117) | `ksp.cpp:221,228`; `gmg.cpp:182-201`; `fespace.cpp:240` |
| per-level relaxation smoother | [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (D3 kernel-impl, forward-ref) | rough-in (D3) | `distrelaxation.cpp:13-36`; `gmg.cpp:42-60` |
| Chebyshev polynomial smoother leg (GROUNDS RE1) | [`L3/chebyshev`](../L3/chebyshev.md) | partial-obstruction | `chebyshev.cpp:160-220`; `gmg.cpp:50-60` |
| Jacobi (point) smoother / diagonal gate | [`L2/jacobi-smoother`](../L2/jacobi-smoother.md) | firm | `chebyshev.cpp:177` (`AssembleDiagonal`) |
| diagonal-precond extract + reciprocal/normalize (GROUNDS RE5/RE7) | [`L1/reciprocal`](../L1/reciprocal.md) / [`L1/normalize`](../L1/normalize.md) | firm | `chebyshev.cpp:177-178` (`AssembleDiagonal(dinv); dinv.Reciprocal()`) |
| bind V-cycle as preconditioner | [`preconditioning-framework`](../L4/preconditioning-framework.md) | firm (c096) | `ksp.cpp:207-234` |

## Status

`rough-in` — the first **infrastructure / shared-substrate** feature-surface
composition-root (DIRECTIVE-2 grounded consumer-(1), batch-39 LEAD). The GC-root marker
`feature_root: seed` is preserved (root-role is permanent/categorical, a separate axis from
the resolution ladder). Held at rough-in by the well-foundedness invariant: its smoother leg
rests on [`L3/chebyshev`](../L3/chebyshev.md) (partial-obstruction) + D3's
forward-referenced [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
(not yet firm on disk). All other directly-owned constituents are firm. **Promotion
condition:** the smoother leg firms (c122+ re-check). This chapter carries the
*compositional* claim (the GMG preconditioner = this V-cycle composition of these constituent
pieces, GROUNDING RE9/RE1/RE5/RE7 by name), not the constituents' per-op algebraic claims
(those live in the linked chapters). Evidence: `gmg.cpp:126-205` (Mult + VCycle) +
`ksp.cpp:206-234` (construction with the prolongation operators + smoother config) realizing
the composition, plus the firm constituent down-links.
```

```new-file:book/src/feature/geometric-multigrid-preconditioner.L1.md
---
kind: feature-surface
feature: geometric-multigrid-preconditioner
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L1/fe_space_hierarchy
      kind: composes                  # the prolongation level-stack the V-cycle restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # D3 kernel-impl: the per-level relaxation smoother (forward-ref)
    - target: L1/reciprocal
      kind: composes                  # diagonal-preconditioner extract dinv.Reciprocal() (GROUNDS RE7)
    - target: L1/normalize
      kind: composes                  # the diagonal-precond scaling chain (GROUNDS RE5)
    - target: palace/linalg/gmg.cpp:126-205
      kind: cites-evidence            # the pure V-cycle recursion (Mult + VCycle) read as nested pure functions
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - L3/chebyshev
    - L2/jacobi-smoother
---

# geometric-multigrid preconditioner — L1 composition-root

The **GMG preconditioner** presented at L1 as the pure-function rendering of the V-cycle —
the mutation-rotated form of `GeometricMultigridSolver::Mult` / `VCycle`
(`palace/linalg/gmg.cpp:126-205`), where the in-place vector mutations (`X.back() = x`,
`Y[l] += R[l]`, the `Mult2`/`MultTranspose2` residual-correction sweeps) are re-expressed as
pure tensor-in / tensor-out functions threaded through the level recursion. This is the
infrastructure / shared-substrate column at L1; it composes the firm L1 vocabulary into the
recursive preconditioner action and links DOWN to each piece. The L4 surface
([`geometric-multigrid-preconditioner.L4`](./geometric-multigrid-preconditioner.L4.md))
carries the full composition narrative; this L1 surface is the pure-function shape the L4
combinator composition lowers onto.

## The pure V-cycle

The V-cycle is a **level-recursive pure function** over flat dof-vectors (`Vector` is rank-1
at L1, so the shapes here are genuinely flat `Tensor[N]`):

    -- one V-cycle sweep at level l, pure (no in-place mutation)
    vcycle :: [LinOp[(S: ...), $S]]   -- A[l]  per-level operators (square)
           -> [Smoother]              -- B[l]  per-level smoothers
           -> [LinOp[(C: ...), (F: ...)]] -- P[l]  prolongations  (coarse → fine)
           -> Solver                  -- b0    coarse solve
           -> Int -> Tensor[N] -> Tensor[N]
    vcycle as bs ps b0 0 x = b0 x                                   -- coarse solve
    vcycle as bs ps b0 l x =
      let y   = presmooth (bs!l) x                                  -- Y ← B(X − A·0)   gmg.cpp:184
          r   = axpby 1.0 x (-1.0) (apply (as!l) y)                -- R ← X − A Y       gmg.cpp:187-188
          rc  = apply_transpose (ps!(l-1)) r                       -- Pᵀ R (restrict)  gmg.cpp:191
          ec  = vcycle as bs ps b0 (l-1) rc                        -- recurse coarser   gmg.cpp:196
          y'  = y `vadd` apply (ps!(l-1)) ec                       -- Y += P E (prolong) gmg.cpp:199-200
      in  postsmooth (bs!l) x y'                                   -- MultTranspose2    gmg.cpp:204

    -- the outer driver: pc_it Richardson sweeps over the finest level
    geometric_multigrid as bs ps b0 pc_it x =
      iterate pc_it (vcycle as bs ps b0 (length as - 1)) x         -- gmg.cpp:135-141

Three composed pieces, each a firm L1 link:

1. **Prolongation level-stack** — [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
   (firm). The per-level prolongations `P[l]` are the firm hierarchy's
   `GetProlongationOperators()`; the V-cycle's `restrict = apply_transpose (P[l])` and
   `prolong = apply (P[l])` are the only inter-level transfers. **GROUNDS RE9.** L0:
   `gmg.cpp:191` (restrict), `:199` (prolong).
2. **Per-level smoother** — [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
   (D3 kernel-impl, forward-ref) / the Chebyshev/Jacobi polynomial smoothers
   ([`L3/chebyshev`](../L3/chebyshev.md) / [`L2/jacobi-smoother`](../L2/jacobi-smoother.md),
   cross-linked as references). The smoother's diagonal-preconditioner setup
   (`dinv = reciprocal(assemble_diagonal A)`) composes the firm
   [`reciprocal`](../L1/reciprocal.md)/[`normalize`](../L1/normalize.md) chains. **GROUNDS
   RE1/RE5/RE7.** L0: `chebyshev.cpp:177-178`.
3. **Coarse solve** — the level-0 base case `b0` (the supplied coarse solver, opaque at this
   surface). L0: `gmg.cpp:178-183` (the `l==0` base case, `B[l]->Mult(X[l], Y[l])` at `:181`).

The residual / update steps (`axpby`, `vadd`) are the firm whole-vector primitives; the body
is whole-tensor by signature shape at each step (the L1 mutation-rotation of the in-place
`R[l]`/`Y[l]` scratch vectors), but the **level recursion and the `pc_it` Richardson sweep
are sequential obstructions** inherited from [`L3/chebyshev`](../L3/chebyshev.md) — see the
L4 surface's §"Why this is rough-in".

## Status

`rough-in` — the L1 pure-function surface of the infrastructure / shared-substrate GMG
preconditioner column. `feature_root: seed` preserved. Held at rough-in by the same
well-foundedness gate as the [L4 surface](./geometric-multigrid-preconditioner.L4.md): the
smoother leg rests on the partial-obstruction [`L3/chebyshev`](../L3/chebyshev.md) + D3's
forward-referenced [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md).
The V-cycle body is the mutation-rotated pure rendering of `gmg.cpp:126-205`; the level
recursion + Richardson sweep are the documented sequential obstructions. Evidence:
`gmg.cpp:126-205`.
```

```new-file:book/src/feature/infrastructure.md
---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
---

# Infrastructure / shared-substrate columns

The fourth feature sub-kind, alongside the [Spine ROOT (lifecycle)](./spine-root.md),
[Driver-leaf columns](./driver-leaf.md), and [Output-product columns](./output-product.md).
An **infrastructure / shared-substrate** column is a composition-root for a feature surface
that is **driver-agnostic** — not an entry-point a user invokes directly, but a shared
substrate that *every* driver's solve composes. It is the *solve-side* analog of the
driver-agnostic [`energy-fields`](./energy-fields.L4.md) output product (a shared postprocess
all field-bearing drivers point at): here the shared surface sits under the Krylov solve
rather than over the solution field.

These columns follow the same composition-root discipline as the other sub-kinds —
inputs = config + the operator/space hierarchy; output = the infrastructure action (e.g. a
preconditioner); body = the composition of already-firm decomposed vocabulary at that level;
they link DOWN to constituent ops/combinators. They are **not** reciprocal-cross-linked to a
single producing/consuming driver (the driver-agnostic exception): a shared-substrate column
links generically to the set of drivers that compose it, and the drivers are not edited to
add an UP-link. The within-column level ordering stays **high→low (L4→L1→L0)**, the deliberate
FEATURE-SURFACE exception; columns sort **alpha-within-this-kind** in the matrix and in
`SUMMARY.md`.

Current member:

- [**geometric-multigrid preconditioner**](./geometric-multigrid-preconditioner.L4.md) — the
  V-cycle preconditioner every multi-level Krylov solve (and the firm
  [`divfree-projector`](../L1/divfree-projector.md)) hangs under; the DIRECTIVE-2 grounded
  consumer-(1) that GROUNDS RE9/RE1/RE5/RE7 by composing the prolongation level-stack +
  smoother leg + diagonal-preconditioner chains by name. (rough-in.)
```

```edit:book/src/feature/index.md
[old]: | [waveguide-mode](./waveguide-mode.L4.md) | [L4 root](./waveguide-mode.L4.md) | [L1 root](./waveguide-mode.L1.md) | [L0 surface](./waveguide-mode.L0.md) |
[new]: | [waveguide-mode](./waveguide-mode.L4.md) | [L4 root](./waveguide-mode.L4.md) | [L1 root](./waveguide-mode.L1.md) | [L0 surface](./waveguide-mode.L0.md) |
| **[Infrastructure / shared-substrate columns](./infrastructure.md)** | | | |
| [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (rough-in) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
```

```edit:book/src/SUMMARY.md
[old]:   - [waveguide-mode — L4 composition-root](./feature/waveguide-mode.L4.md)
  - [waveguide-mode — L1 composition-root](./feature/waveguide-mode.L1.md)
  - [waveguide-mode — L0 ground-truth surface](./feature/waveguide-mode.L0.md)
[new]:   - [waveguide-mode — L4 composition-root](./feature/waveguide-mode.L4.md)
  - [waveguide-mode — L1 composition-root](./feature/waveguide-mode.L1.md)
  - [waveguide-mode — L0 ground-truth surface](./feature/waveguide-mode.L0.md)
- [Infrastructure / shared-substrate columns](./feature/infrastructure.md)
  - [geometric-multigrid-preconditioner — L4 composition-root](./feature/geometric-multigrid-preconditioner.L4.md)
  - [geometric-multigrid-preconditioner — L1 composition-root](./feature/geometric-multigrid-preconditioner.L1.md)
```

## Supporting evidence

### Source citations (verified on disk this cycle via palace-codemap `read_range`)

- `palace/linalg/gmg.cpp:126-142` — `GeometricMultigridSolver::Mult`: `X.back() = x;` then
  `for (it<pc_it) VCycle(n_levels-1, it>0); y = Y.back();` (the outer Richardson driver).
- `palace/linalg/gmg.cpp:172-205` — `VCycle(l, initial_guess)`: coarse-solve base case at
  `l==0` (`:178-183`); pre-smooth `B[l]->Mult2` (`:184`); residual `A[l]->Mult` (`:187`) +
  `linalg::AXPBY(1.0, X, -1.0, R)` (`:188`); restrict `RealMultTranspose(*P[l-1], R, X[l-1])`
  (`:191`); recurse `VCycle(l-1, false)` (`:196`); prolong-add `RealMult(*P[l-1], Y[l-1], R)` (`:199`) +
  `Y[l] += R[l]` (`:200`); post-smooth `B[l]->MultTranspose2` (`:204`).
- `palace/linalg/gmg.cpp:16-63` — constructor: configures level smoothers; uses
  `DistRelaxationSmoother` when an auxiliary space `G` is supplied (`:42-46`), else
  `ChebyshevSmoother`/`ChebyshevSmoother1stKind` (`:50-60`).
- `palace/linalg/ksp.cpp:207-234` — GMG construction: when `fespaces.GetNumLevels() > 1`,
  `std::make_unique<GeometricMultigridSolver<OperType>>(comm, std::move(pc),
  fespaces.GetProlongationOperators(), &G | nullptr, ...)` — the prolongation operators +
  smoother config passed in; returned as the Krylov preconditioner `pc`.
- `palace/linalg/distrelaxation.cpp:13-36` — `DistRelaxationSmoother` ctor folds two
  `ChebyshevSmoother`/`ChebyshevSmoother1stKind` (primary `B` + auxiliary `B_G`).
- `palace/linalg/chebyshev.cpp:177-178` — `op.AssembleDiagonal(dinv); dinv.Reciprocal();`
  (the diagonal-preconditioner extract + reciprocal — the RE5/RE7 grounding site;
  also `:241` in the 1st-kind ctor).
- `palace/linalg/divfree.cpp:128` — the firm `divfree-projector` builds a
  `GeometricMultigridSolver` as its preconditioner (the spine-dependency confirmation).
- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy` (the
  `fe_space_hierarchy` `AddLevel`-fold whose prolongations GMG consumes).
- `palace/fem/fespace.cpp:240` — `FiniteElementSpaceHierarchy::BuildProlongationAtLevel`
  (lazy `P[l]` materialization).

### On-disk constituent `## Status` lines surveyed (NOT the index cells)

- `L4/preconditioning-framework.md` `## Status`: **firm** (c096, firm-on-positive-structure).
- `L1/fe_space_hierarchy.md` `## Status`: **firm** (c117, firm-on-positive-structure).
- `L3/chebyshev.md` `## Status`: **partial-obstruction** (witnessed sequential obstruction).
- `L2/jacobi-smoother.md` frontmatter `firmness: firm`.
- `L1/reciprocal.md` `## Status`: **firm**.
- `L1/normalize.md` `## Status`: **firm**.
- `L1/divfree-projector.md` `## Status`: **firm**.
- `L1/multigrid-relaxation-smoother.md`: **NOT yet on disk** (D3 lands it this cycle;
  forward-referenced, canonical slug stated in both D1+D3 scopes).

### RE-grounding map (the c122 re-check target)

| RE | grounding edge authored by this column | constituent |
|---|---|---|
| RE9 (fe_space_hierarchy prolongation) | `GMG.L4 → L1/fe_space_hierarchy` (composes) | firm; `GetProlongationOperators()` |
| RE1 (chebyshev/jacobi smoother leg) | `GMG.L4 → L3/chebyshev` + `→ L2/jacobi-smoother` (composes) | partial-obstruction / firm |
| RE5 (normalize chain) | `GMG.L4 → L1/normalize` (composes) | firm |
| RE7 (reciprocal — diagonal-precond extract) | `GMG.L4 → L1/reciprocal` (composes) | firm |

## Open questions / caveats

- **`record-MultigridConfig-needs-definition-home` (flag).** The L4 column's input signature
  names `MultigridConfig` (the `mg_cycle_it` / `mg_smooth_it` / `mg_smooth_order` /
  `mg_smooth_sf_max` / `mg_smooth_sf_min` / `mg_smooth_cheby_4th` linear-solver config slice,
  L0 home `palace/linalg/ksp.cpp` `LinearSolverData` / the `IoData` `Solver.Linear` surface).
  It is currently defined only by its USE in this column. If a 2nd consumer surfaces it
  warrants a `concepts/MultigridConfig.md` record-definition page; for now it is a
  single-consumer record (this column) and would take an in-chapter §Record-definition
  section — deferred, flagged for the record-definition dispatcher. NOT authored this cycle to
  keep the landing to the composition-root scope.
- **Column rough-in promotion is consumer-gated on the smoother leg (c122+).** This column
  promotes off rough-in when D3's `multigrid-relaxation-smoother` firms AND the
  `L3/chebyshev` partial-obstruction's V-cycle recursion is resolved-or-documented at the
  column level. The c122 RE re-check should re-survey the smoother leg's on-disk `## Status`
  and re-evaluate. Do NOT flip this column firm before the smoother leg firms (well-foundedness).
- **V-cycle recursion as a vocabulary candidate (combinator-miner handoff).** The V-cycle is
  a level-recursive combinator (`vcycle ps bs b0 l` recursing to `l-1`) that does NOT yet
  exist as named L4 vocabulary — it is presented in this column as an in-line recursion, not
  a firm combinator. If the level-recursive restrict→recurse→prolong pattern recurs (it also
  appears in the AMG/auxiliary-space transfers), it is a combinator-miner candidate. Flagged
  for D6 (the shared-substrate probe) — NOT mined here (a column composes, it does not mine).
- **GMG is also constructed in `hcurl.cpp:101` and `errorestimator.cpp:86`** (the H(curl)
  mass-matrix solver + the flux-recovery error estimator). These are additional
  driver-agnostic consumers of this infrastructure column — consistent with the
  driver-agnostic sub-kind (no single producing driver to reciprocal-link). The AMR
  errorestimator consumer (D7 this cycle) composes this column; a navigational cross-link
  from the AMR column to this one is the correct wiring (NOT a depends-on from this column to
  AMR). Noted for D7 / the c122 planner.
- **`L4/chebyshev` vs `L3/chebyshev` smoother-leg edge target.** I targeted the
  `depends-on (composes)` smoother-leg edge at `L3/chebyshev` (the iteration-rotation form
  closest to the V-cycle's smoother sweep) rather than `L4/chebyshev` (the typed-wrapper
  form). The V-cycle is an L4 composition but its smoother sweep is the L3 partial-obstruction
  body; if the linter / reviewer prefers the L4-level edge for an L4 column, this is a cheap
  re-target. Flagged as a deliberate choice, not an oversight.
