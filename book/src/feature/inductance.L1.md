---
kind: feature-surface
feature: inductance
level: L1
status: seed
composes:
  - book/src/feature/magnetostatic.L1.md (seed — the producing driver column: solution family [Aᵢ])
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — diagonal Aᵢᵀ K Aᵢ)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Aⱼᵀ K Aᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:110-152 (MagnetostaticSolver::PostprocessTerminals)
---

# inductance — L1 composition-root (output product)

The **Maxwell inductance matrix** output product, presented at L1 as a pure-function composition of L1 operators. This is the **pure-function feature surface** of the output product: the same composition root as the [L4 chapter](./inductance.L4.md), but in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole output product do these L1 bilinear operators add up to?"

At L1 the inductance output product is a pure function `(solution family, currents) → inductance matrix` built from the magnetostatic driver column's solution family `[Aᵢ]` reduced through two rough-in L1 bilinear operators, with the **mutation already lifted** (the L0 in-place `M_mag->Mult(A_gf, H_gf)` / `linalg::Dot(...)` energy-form writes are lifted to value-returning bilinear evaluations per the constituent ops' L1>L0 mutation rotations).

## The composition

    -- inputs = the magnetostatic solution family + currents; output = the inductance matrix
    inductance :: MagnetostaticConfig -> InductanceMatrix
    inductance cfg =
      let (k, as) = magnetostatic_solution cfg                       -- (1) the magnetostatic driver column: K + family [Aᵢ]
          is      = currents cfg                                      -- the per-source excitation currents Iᵢ
          m       = symmetric                                        -- (3) symmetric M from the upper triangle
                      [ [ entry k as is i j | j <- [i .. n-1] ]      -- (2) per-pair current-normalized bilinear
                        | i <- [0 .. n-1] ]
      in  { matrix: m, inverse: invert m }                            -- Minv (LAPACK)
      where
        n            = length as
        entry k as is i j
          | i == j   = matrix_weighted_norm (as!!i) k ^ 2 / (is!!i * is!!i)   -- diagonal: (Aᵢᵀ K Aᵢ)/Iᵢ²
          | otherwise = bilinear_form (as!!j) k (as!!i) / (is!!i * is!!j)     -- off-diag: (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)

1. **The magnetostatic driver column produces the solution family** — [`magnetostatic.L1`](./magnetostatic.L1.md) (**seed**). The upstream pure-function composition root assembles `K` once and solves the per-source family `as = [Aᵢ]`. This output-product column consumes that `(k, as)` pair. L0: the `Solve` body (`palace/drivers/magnetostaticsolver.cpp:29`, `:66`, `:77`); the family + currents handed to `PostprocessTerminals` (`:105`).

2. **The current-normalized bilinear reduction** — built from two rough-in L1 operators, each normalized by the excitation currents:
   - diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` — the operator-weighted self-form normalized by the squared current, the rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Aᵢ, K)² = Aᵢᵀ K Aᵢ`; L0 builds it as `post_op.GetDomainPostOp().M_mag->Mult(A_gf, H_gf)` then `linalg::Dot<Vector>(..., A_gf, H_gf) / (I_inc[i]*I_inc[i])`, `magnetostaticsolver.cpp:129-131`).
   - off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` — the operator-weighted cross-pairing normalized by the current product, the rough-in [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Aⱼ, K Aᵢ⟩` (L0 the same energy-form `Mult`/`Dot` against the `j` grid function then `/ (I_inc[i]*I_inc[j])`, `:135-138`).
   The result is the symmetric `M` (upper triangle computed, lower mirrored, `:140-149`) and its LAPACK inverse `Minv` (`:151-152`). This stage is a pure fold of current-normalized bilinear-form evaluations over the solution-family pair grid — no L1 operator is *new* here; it composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in), with the current normalization a scalar weight on each entry.

## Inputs / outputs (the feature surface)

- **Input.** The magnetostatic solution family `[Aᵢ]` + the magnetic-energy operator `K = M_mag` (from the [`magnetostatic.L1`](./magnetostatic.L1.md) driver column) + the per-source excitation currents `Iᵢ` (the normalization that distinguishes the inductance reduction from the capacitance reduction). All read-only. L0: `I_inc` argument to `PostprocessTerminals` (`magnetostaticsolver.cpp:112`).
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` symmetric Maxwell inductance matrix `M` (+ inverse). L0: `mfem::DenseMatrix M(A.size())` (`magnetostaticsolver.cpp:122`), `Minv` (`:151-152`).

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): an explicit upper-triangle comprehension over per-pair pure bilinear evaluations (`matrix_weighted_norm` on the diagonal, `bilinear_form` off-diagonal), each scaled by an inline current weight, mirrored to symmetric.
- **L4** ([`inductance.L4`](./inductance.L4.md)): the per-pair bilinear grid is the [`gram_reduce`](../L4/gram_reduce.md) combinator (the symmetric-Gram reduction made *structural*), and the current normalization is the combinator's `w = 1/(IᵢIⱼ)` weight closure — the current-normalized specialization, the sibling of capacitance's unit weight. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the `gram_reduce` combinator names.

The L1→L0 direction (how each bilinear evaluation lowers to the in-place energy-form driver writes) is the per-operator L1>L0 mutation-rotation themes of [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md); this output-product column records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| solution family [Aᵢ] | [`magnetostatic.L1`](./magnetostatic.L1.md) (driver column) | seed | `magnetostaticsolver.cpp:29, 66, 77` |
| diagonal Aᵢᵀ K Aᵢ / Iᵢ² | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:129-131` |
| off-diagonal Aⱼᵀ K Aᵢ / Iᵢ Iⱼ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `magnetostaticsolver.cpp:135-138` |

## Status

`seed` — the L1 pure-function output-product composition root for the inductance matrix, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance.L1](./capacitance.L1.md) unit-weight output product. BOTH directly-owned bilinear primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing). **Under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03) a column promotes off `seed` when its OWN directly-owned constituents are firm; this column STAYS `seed` because its OWN reduce primitives are rough-in** (the reduction rests on the rough-in L1 bilinear primitives, whose L4 home `gram_reduce` is `rough-in (test-coverage-bounded)`). This is an OWN-constituent gate, NOT a cross-linked-sibling blocker: the [`magnetostatic.L1`](./magnetostatic.L1.md) producing driver column is a SIBLING reference, not the gate. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the L1 constituent down-links.
