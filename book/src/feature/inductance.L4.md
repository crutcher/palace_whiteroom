---
kind: feature-surface
feature: inductance
level: L4
status: seed
composes:
  - book/src/feature/magnetostatic.L4.md (seed — the producing driver column: solution family [Aᵢ])
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — the symmetric-Gram reduction combinator; current-normalized specialization)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:110-152 (MagnetostaticSolver::PostprocessTerminals)
---

# inductance — L4 composition-root (output product)

The **Maxwell inductance matrix** output product, presented at L4 as a single composition of firm-track L4 vocabulary — the **outward backend-lowering entry point** for "what the magnetostatic solver computes." This chapter is an **output-product leaf feature column** (a composition root): inputs = config (the surface-current sources + their excitation currents); output = the physical product (the inductance matrix `M` and its inverse `Minv`); body = the composition of the already-firm-track [`gram_reduce`](../L4/gram_reduce.md) reduction over the [`magnetostatic`](./magnetostatic.L4.md) driver column's solution family. It does **not** introduce a new combinator; it wires existing L4 vocabulary into the user-facing output product and links DOWN to each composed piece.

Inductance is the **output-product half** of the magnetostatic composition root — the post-processing stage that the [`magnetostatic.L4`](./magnetostatic.L4.md) driver column flags as its stage (3) and defers to a forward mine. That mine landed: [`gram_reduce`](../L4/gram_reduce.md) is the symmetric-Gram reduction combinator shared with the electrostatic [capacitance](./capacitance.L4.md) output product, and inductance is its **current-normalized specialization** (weight `w = 1/(IᵢIⱼ)`). This column is the feature-surface view of that specialization.

## The composition

At L4 the inductance output product is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the inductance matrix (the physical product)
    inductance :: MagnetostaticConfig -> InductanceMatrix
    inductance cfg =
      let (k, as) = magnetostatic_solution cfg            -- (1) the magnetostatic driver column: assemble K once, solve the surface-current family [Aᵢ]
          is      = currents cfg                           -- the per-source excitation currents Iᵢ
          w i j   = 1 / (is!!i * is!!j)                    -- the current-normalized weight closure (THE specialization)
          m       = gram_reduce k as w                     -- (2) Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ) symmetric-Gram reduction
      in  { matrix: m, inverse: gram_inverse m }           -- (3) M + Minv (the alternate Maxwell form)

Two composed stages (the driver column + the reduction), with an inverse tail:

1. **The magnetostatic driver column produces the solution family** — [`magnetostatic.L4`](./magnetostatic.L4.md) (**seed**). The upstream composition root assembles the curl-curl stiffness `K` once ([`fe_assemble`](../L4/fe_assemble.md)) and maps the per-surface-current solve over the source family ([`solve_family`](../L4/solve_family.md)), collecting the solution family `as = [Aᵢ]`. This output-product column **consumes** that `(k, as)` pair; it does not re-derive it (the driver column owns the solve, this column owns the reduction). L0: the `Solve` body assembles + sweeps (`palace/drivers/magnetostaticsolver.cpp:29`, `:66`, `:77`); the family `A` + currents `I_inc` are handed to `PostprocessTerminals` (`:105`).

2. **The current-normalized symmetric-Gram reduction** — [`gram_reduce`](../L4/gram_reduce.md) (**rough-in (test-coverage-bounded)**). The L4 operator-weighted symmetric-Gram reduction combinator `gram_reduce K xs w` folds each upper-triangle family-pair through the operator-weighted bilinear primitives and mirrors to a symmetric matrix. Inductance is its **current-normalized specialization**: `w i j = 1/(Iᵢ Iⱼ)`, `K = M_mag` (the curl-curl magnetic-energy operator), `xs = [Aᵢ]`. The diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` is the self-bilinear ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) radicand) current-normalized; the off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` is the cross-bilinear ([`bilinear-form`](../L1/bilinear-form.md)) current-normalized. The COMSOL magnetic-energy formulation `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²` is exactly the squared-energy radicand scaled by the current weight (`magnetostaticsolver.cpp:115-121` cites the COMSOL AC/DC Module manual p. 97). This is `gram_reduce`'s second positive witness (the current-normalized one; capacitance is the unit-weight first). L0: the diagonal `:129-131`, the off-diagonal `:138`, the symmetric mirror `:143-149`.

3. **The inverse tail** — `gram_inverse m = inv m` (LAPACK). The alternate Maxwell form `Minv = M⁻¹` is a downstream matrix map on the produced `M` — a **consumer** of the reduction, kept OUT of the reduction combinator (the `nrm2`-style consumer split, `gram_reduce` law "the inverse is NOT part of the reduction"). L0: `mfem::DenseMatrix Minv(M); Minv.Invert()` (`magnetostaticsolver.cpp:151-152`).

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig`: the surface-current-boundary source set (→ the solution-family index domain) and, distinctively for this output product, the **per-source excitation currents** `Iᵢ` (→ the normalization weight closure `w i j = 1/(IᵢIⱼ)`). The current set is what distinguishes the inductance reduction from the capacitance reduction at the config surface. L0 home: `data.GetExcitationCurrent()` collected into `I_inc` (`magnetostaticsolver.cpp:48`, populated in the `Solve` sweep), passed to `PostprocessTerminals` as the `I_inc` argument (`:105`, `:112`).
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` symmetric Maxwell inductance matrix `M` (and its inverse `Minv`). This IS what the user ran the magnetostatic solver to compute — the output product the driver column produces a solution family *for*. L0 home: `mfem::DenseMatrix M(A.size())` (`magnetostaticsolver.cpp:122`), `Minv` (`:151-152`).

## Why this composes cleanly (the current-normalized Gram specialization)

The inductance output product composes cleanly because it is a **pure specialization of an existing L4 combinator** — no new vocabulary, only a weight closure:

- The reduction is [`gram_reduce`](../L4/gram_reduce.md) with `w i j = 1/(IᵢIⱼ)`; the unit-weight sibling is the [capacitance](./capacitance.L4.md) output product (`w ≡ 1`). ONE symmetric-Gram reduction across the two output products; **the weight is the only difference** (`gram_reduce` §Specialization).
- The solution family is supplied by the [`magnetostatic`](./magnetostatic.L4.md) driver column — the output-product column links UP to its producing driver rather than re-deriving the solve.
- The inverse is a downstream consumer, not part of the reduction — the clean consumer split.

The whole output product therefore lowers cleanly outward: `inductance = gram_inverse-tail ∘ gram_reduce(w=current-normalized) ∘ magnetostatic_solution`. This is the FEATURE-SURFACE test for pulling an output product up: it advances because the constituent vocabulary (`gram_reduce` + the magnetostatic driver column) exists and composes without forcing the spine — the current normalization is a scalar weight absorbed into the combinator's `w` argument, not a new shape.

## Constituent down-links

| Stage | L4 vocabulary | Status | L0 site |
|---|---|---|---|
| solution family [Aᵢ] | [`magnetostatic.L4`](./magnetostatic.L4.md) (driver column) | seed | `magnetostaticsolver.cpp:29, 66, 77` |
| current-normalized Gram reduction | [`gram_reduce`](../L4/gram_reduce.md) (`w = 1/(IᵢIⱼ)`) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:122, 129-138, 143-149` |
| inverse tail (Minv) | `gram_inverse` (the LAPACK `Invert()` consumer) | — | `magnetostaticsolver.cpp:151-152` |

## Status

`seed` — an output-product leaf feature column under the FEATURE-SURFACE SPINE directive (2026-06-02), the current-normalized sibling of the [capacitance](./capacitance.L4.md) unit-weight output product. The composition is sound: the reduction is the [`gram_reduce`](../L4/gram_reduce.md) combinator's current-normalized specialization (`w = 1/(IᵢIⱼ)`), consuming the [`magnetostatic`](./magnetostatic.L4.md) driver column's solution family `[Aᵢ]`, with the inverse a downstream consumer. The column stays `seed` because `gram_reduce` is itself `rough-in (test-coverage-bounded)` (its folded L1 bilinear primitives are rough-in, and no dedicated test exercises the Gram reduction) — a feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (the inductance output product = this current-normalized specialization of `gram_reduce` over the magnetostatic family), NOT the combinator's per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md)). Evidence: `PostprocessTerminals` realizing the current-normalized reduction (`magnetostaticsolver.cpp:110-152`, on-disk-verified this dispatch), plus the `gram_reduce` + magnetostatic-column down-links.
