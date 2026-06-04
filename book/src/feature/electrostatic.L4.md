---
kind: feature-surface
feature: electrostatic
level: L4
status: seed
composes:
  - book/src/L4/fe_assemble.md (firm — assemble K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (firm — fixed-operator per-terminal map)
  - book/src/L4/ksp_solve.md (firm — the per-element solve cap solve_family maps)
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — the operator-weighted symmetric-Gram output-product reduction; capacitance = the w = 1 voltage specialization)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
---

# electrostatic — L4 composition-root

The **electrostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the simplest Palace pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → capacitance matrix), and links DOWN to each composed piece.

The electrostatic pipeline is the cleanest entry point because it is a **fixed-operator** solve: the stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-terminal right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md).

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the capacitance matrix (the physical product)
    electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
    electrostatic cfg =
      let space  = h1_space cfg                       -- the H1 finite-element space (readonly construction stratum)
          terms  = [ diffusion (permittivity cfg) ]   -- the weak-form term list (single ε-weighted ∇ term)
          k      = fe_assemble space terms            -- (1) assemble K ONCE  ── L4/fe_assemble (firm)
          rhss   = [ excitation cfg idx | idx <- terminal_sources cfg ]  -- per-terminal RHS family
          sols   = solve_family k rhss                -- (2) fixed-operator per-terminal map  ── L4/solve_family
      in  capacitance_reduce k sols                   -- (3) Cᵢⱼ = Vⱼᵀ K Vᵢ reduction → capacitance matrix

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble `K` once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds the weak-form term list into the global stiffness operator `K`. For electrostatic the term list is the single ε-weighted diffusion term `[ diffusion(ε) ]` (the single-term reduction, `fe_assemble`'s law 5; the electrostatic specialization is named at `book/src/L4/fe_assemble.md:127`). `space` (the H1 space) is the `readonly` construction stratum captured once. L0: `auto K = laplace_op.GetStiffnessMatrix()` (`palace/drivers/electrostaticsolver.cpp:30`).

2. **Per-terminal map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**firm**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-terminal RHS family, collecting the solution family `[Vᵢ]`. The electrostatic terminal-boundary sweep is `solve_family`'s **witness 1** (named at `book/src/L4/solve_family.md:107`): `op = K`, the family is the terminal-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `electrostaticsolver.cpp:34-36`, the family map at `:59`, the per-element solve `ksp.Mult(RHS, V[step])` at `:69`.

3. **Capacitance-matrix reduction** — [`gram_reduce`](../L4/gram_reduce.md) (**rough-in (test-coverage-bounded)**), the `w = 1` voltage specialization. The capacitance matrix is the operator-weighted symmetric-Gram reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` over the solution family `[Vᵢ]` — the unit-weight (`w i j = 1`) member of the shared L4 reduction `gram_reduce K xs w = Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` (the COMSOL energy formulation: `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ² ≡ ×1`, off-diagonals from the cross energy; named electrostatic specialization at `book/src/L4/gram_reduce.md:167-171`). `gram_reduce` is the **entry** (replace-and-propagate, CLAUDE.md §VOCABULARY-SHIFT redirect); the capacitance reduction re-expresses THROUGH it as the `w = 1` corner, NOT as a hand-rolled fold. The combinator's `map`-then-`reduce` body composes the rough-in L1 building blocks — the diagonal `Vᵢᵀ K Vᵢ` is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) radicand, the off-diagonal `Vⱼᵀ K Vᵢ` is the [`bilinear-form`](../L1/bilinear-form.md) — folded over the upper-triangle family-pair grid with the symmetric mirror; `gram_reduce` is rough-in BECAUSE those folded constituents are. The inverse (`Cinv = C⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root — authored in full as its dedicated output-product feature column [`capacitance`](./capacitance.L4.md), which links back DOWN to this driver as its producing column. L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).

## Inputs / outputs (the feature surface)

- **Input — config.** `ElectrostaticConfig`: the H1 space construction (mesh + order → `h1_space`), the material permittivity ε (→ the diffusion term coefficient), the terminal-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `LaplaceOperator laplace_op(iodata, mesh)` (`electrostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` Maxwell capacitance matrix `C` (and its inverse). This is what the user ran the electrostatic solver to compute. L0 home: the `mfem::DenseMatrix C` written by `PostprocessTerminals` (`electrostaticsolver.cpp:111`).

## Why this is the cleanest exemplar

The electrostatic feature is the cleanest composition root because **every stage composes a firm or rough-in L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the simplest possible use of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the cleanest member; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is a fold of bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: the composition is clean, but under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) the column stays `seed` because the [`gram_reduce`](../L4/gram_reduce.md) capacitance reduction — a **directly-owned** constituent — is `rough-in (test-coverage-bounded)`. The [`solve_family`](../L4/solve_family.md) per-terminal map is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape), so the own-constituent gate has narrowed from two directly-owned rough-in constituents to ONE: firming `gram_reduce` is the remaining promotion route — and that is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), which `gram_reduce` folds.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `electrostaticsolver.cpp:30` |
| per-terminal solve map | [`solve_family`](../L4/solve_family.md) | firm | `electrostaticsolver.cpp:34-36, 59, 68-69, 89` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `electrostaticsolver.cpp:69` |
| capacitance reduction (Vⱼᵀ K Vᵢ) | [`gram_reduce`](../L4/gram_reduce.md) (`w = 1` voltage specialization) — folding L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (diagonal) / [`bilinear-form`](../L1/bilinear-form.md) (off-diagonal) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:95, 100-138` |

## Status

`seed` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. This column **stays `seed`** — not on a sibling-column blocker, but on a genuine **own-constituent gate** that has now NARROWED to a single remaining constituent: the [`gram_reduce`](../L4/gram_reduce.md) `w = 1` voltage-specialization capacitance reduction (`rough-in (test-coverage-bounded)`, which folds the rough-in L1 diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md) over the family-pair grid). The other directly-composed constituent, the [`solve_family`](../L4/solve_family.md) per-terminal solve map, is now **firm** (c086, the firm-on-positive-structure / syntactic-identity escape — its concatenation-homomorphism is `map`'s definitional list-homomorphism, its operator-capture-once hoist is read off the positive `SetOperators`-outside-the-loop source, and its element-independence is a `const`-`BaseKspSolver::Mult`-with-telemetry-only-state read-off). The composition is sound (stage (1) the firm [`fe_assemble`](../L4/fe_assemble.md), the reduction a clean fold of evaluations), but one directly-owned constituent (`gram_reduce`) remaining rough-in is the own-constituent gate; firming `gram_reduce` is the remaining promotion route — and `gram_reduce` is itself convergently blocked on the `matrix-weighted-norm` √-cascade (NO-GO-HELD), so this column does not flip this cycle. This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
