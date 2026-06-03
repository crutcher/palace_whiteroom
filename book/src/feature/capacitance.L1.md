---
kind: feature-surface
feature: capacitance
level: L1
status: seed
composes:
  - book/src/feature/electrostatic.L1.md (the producing driver column — supplies the per-terminal solution family [Vᵢ])
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — diagonal Vᵢᵀ K Vᵢ)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Vⱼᵀ K Vᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:100-140 (ElectrostaticSolver::PostprocessTerminals — the capacitance reduction)
---

# capacitance — L1 composition-root

The **Maxwell capacitance matrix** output product, presented at L1 as a pure-function composition of L1 operators. This is the **pure-function feature surface** of the output-product sub-kind: the same composition root as the L4 chapter, but expressed in L1 vocabulary (explicit per-operator bilinear-form evaluations, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole product do these L1 bilinear operators add up to?"

At L1 the capacitance product is a pure function `config → capacitance matrix`: it consumes the per-terminal solution family `[Vᵢ]` produced by the [`electrostatic.L1`](./electrostatic.L1.md) driver column, then folds a grid of L1 bilinear-form evaluations into the symmetric matrix `C` (the **mutation already lifted** — the L0 in-place `M_elec->Mult(V_gf, D_gf)` / `Cinv.Invert()` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config (terminal excitations); output = the capacitance matrix (the physical product)
    capacitance :: ElectrostaticConfig -> CapacitanceMatrix
    capacitance cfg =
      let (k, vs) = electrostatic_family cfg               -- (1) the electrostatic driver column → (K, [Vᵢ])
          m       = length vs
          c i j   | i == j     = matrix_weighted_norm (vs!!i) k ^ 2  -- diagonal  Vᵢᵀ K Vᵢ
                  | otherwise  = bilinear_form (vs!!j) k (vs!!i)      -- off-diag  Vⱼᵀ K Vᵢ
      in  symmetric_matrix m c                             -- (2) symmetric fold over the family-pair grid → C

1. **The producing driver column** — [`electrostatic.L1`](./electrostatic.L1.md). The electrostatic driver assembles `K` once (the [`fe_assemble`](../L1/fe_assemble.md) fold) and maps the per-terminal pure solve [`ksp_solve`](../L1/ksp_solve.md) over the terminal-source family, collecting the solution family `[Vᵢ]`. The capacitance output product consumes that `(K, [Vᵢ])`; it does not re-derive the solve. L0: the per-terminal loop `electrostaticsolver.cpp:59-89`.

2. **Capacitance-matrix reduction** — the symmetric matrix `Cᵢⱼ = Vⱼᵀ K Vᵢ`, built from L1 bilinear-form evaluations over the solution-family pair grid (rough-in diagonal + rough-in off-diagonal):
   - diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` — the operator-weighted self-form, the rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Vᵢ, K)² = Vᵢᵀ K Vᵢ`; L0 builds it as `M_elec->Mult(V_gf, D_gf)` then `linalg::Dot(V_gf, D_gf)`, `:118-119`).
   - off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` — the operator-weighted cross-pairing, the rough-in [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Vⱼ, K Vᵢ⟩` (L0 `:122-127`, the same energy-form `Mult`/`Dot` with the `j` grid function, `:126`).
   The result is the symmetric `C` (and its LAPACK inverse `Cinv`, `:139-140`). This stage is a pure fold of bilinear-form evaluations over the family-pair grid — no L1 operator is *new* here; the reduction composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in). At L4 this exact fold is named the [`gram_reduce`](../L4/gram_reduce.md) combinator (voltage `w = 1` specialization); L1 sees the unfolded grid.

## Inputs / outputs (the feature surface)

- **Input — config (terminal excitations).** `ElectrostaticConfig` (terminal-source set → family-index domain + unit-voltage excitations; H1 space + ε → energy operator `K`), inherited from the producing driver column. All read-only.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` symmetric Maxwell capacitance matrix `C` (+ inverse `Cinv`). L0: `mfem::DenseMatrix C` (`electrostaticsolver.cpp:111`).

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit symmetric fold over the family-pair grid, each entry a per-operator bilinear-form pure function ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) on the diagonal, [`bilinear-form`](../L1/bilinear-form.md) off-diagonal).
- **L4** ([`capacitance.L4`](./capacitance.L4.md)): the whole reduction is the [`gram_reduce`](../L4/gram_reduce.md) combinator at the voltage `w = 1` specialization (the grid fold + symmetric mirror + weight made *structural*). The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinator names.

The L1→L0 direction (how the bilinear-form pure functions lower to the in-place `Mult`/`Dot` driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column | [`electrostatic.L1`](./electrostatic.L1.md) (driver feature column) | seed | `electrostaticsolver.cpp:21-98` |
| diagonal Vᵢᵀ K Vᵢ | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:118-119` |
| off-diagonal Vⱼᵀ K Vᵢ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `electrostaticsolver.cpp:122-127` |

## Status

`seed` — the L1 pure-function composition root for the capacitance output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`electrostatic.L1`](./electrostatic.L1.md) driver column's solution family, then folds the two rough-in L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `rough-in (test-coverage-bounded)`, [`bilinear-form`](../L1/bilinear-form.md) rough-in) over the family-pair grid. The reduction therefore rests on rough-in L1 primitives — consistent with the column being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` realizing the composition, plus the constituent down-links.
