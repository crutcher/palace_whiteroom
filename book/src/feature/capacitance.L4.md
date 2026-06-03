---
kind: feature-surface
feature: capacitance
level: L4
status: seed
composes:
  - book/src/feature/electrostatic.L4.md (the producing driver column — supplies the per-terminal solution family [Vᵢ])
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — the symmetric-Gram reduction; w = 1 voltage specialization)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:100-140 (ElectrostaticSolver::PostprocessTerminals — the capacitance reduction)
---

# capacitance — L4 composition-root

The **Maxwell capacitance matrix** output product, presented at L4 as a single composition of firm-track L4 combinators. This chapter is a **composition root** of the *output-product* sub-kind (a **leaf feature column**): its constituents at stage (2) are *vocabulary ops* (the [`gram_reduce`](../L4/gram_reduce.md) reduction combinator), and its upstream stage is *another feature column* (the [`electrostatic`](./electrostatic.L4.md) driver, which produces the solution family the reduction consumes). It introduces no new combinator; it wires the already-firm-track L4 vocabulary into the user-facing product (config → capacitance matrix `C`), and links DOWN to each composed piece.

The capacitance matrix is the physical product the user runs the electrostatic solver to obtain: the `n_terminal × n_terminal` symmetric Maxwell capacitance matrix `C` (and its inverse `Cinv`). The **electrostatic driver column** ([`electrostatic.L4`](./electrostatic.L4.md)) produces the per-terminal solution family `[Vᵢ]`; this output-product column reduces that family to `C` via the operator-weighted symmetric-Gram reduction at the **voltage (`w = 1`) specialization**.

## The composition

At L4 the capacitance product is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config (terminal excitations); output = the capacitance matrix (the physical product)
    capacitance :: ElectrostaticConfig -> CapacitanceMatrix
    capacitance cfg =
      let (k, vs) = electrostatic_family cfg     -- (1) the electrostatic driver column: assemble K once,
                                                 --     per-terminal fixed-operator solve → solution family [Vᵢ]
                                                 --     ── feature/electrostatic.L4 (the producing driver column)
          c       = gram_reduce k vs (\i j -> 1) -- (2) symmetric-Gram reduction at w = 1 (voltage)  ── L4/gram_reduce
      in  c                                      --     Cᵢⱼ = Vⱼᵀ K Vᵢ  (Cinv = gram_inverse c, the alternate Maxwell form)

Two composed stages, the first a down-link to the producing driver column, the second a down-link to the firm-track L4 reduction combinator:

1. **The producing driver column** — [`electrostatic.L4`](./electrostatic.L4.md). The electrostatic driver is the fixed-operator solve that assembles the energy operator `K` once and sweeps the terminal-source family with the operator captured once, collecting the per-terminal solution family `[Vᵢ]` (the [`solve_family`](../L4/solve_family.md) output). The capacitance output product does NOT re-derive that solve; it consumes the driver column's `(K, [Vᵢ])` and reduces it. This is the output-product / driver split the FEATURE-SURFACE SPINE encodes: one driver column, possibly several output products hanging off its solution family. L0: the per-terminal solve family is `electrostaticsolver.cpp:59-89` (the loop), reduced after the loop.

2. **The symmetric-Gram reduction at `w = 1`** — [`gram_reduce`](../L4/gram_reduce.md) (**rough-in (test-coverage-bounded)**). The L4 operator-weighted symmetric-Gram reduction `gram_reduce k xs w` folds each upper-triangle family pair through the operator-weighted bilinear primitives and mirrors to a symmetric matrix. The capacitance matrix is its **voltage / unit-weight specialization** (`gram_reduce`'s §Specialization "Electrostatic capacitance" bullet, `book/src/L4/gram_reduce.md:167-171`; the literal "positive witness 1" label is at `:255`): `w i j = 1` (the unit-voltage excitation `/Vᵢ² ≡ ×1`), `K = M_elec` (the diffusion-energy operator), `xs = [Vᵢ]` (the per-terminal solution family). The diagonal is `Cᵢᵢ = Vᵢᵀ K Vᵢ`, the off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ`; `gram_inverse` then produces `Cinv = C⁻¹` (LAPACK) for the alternate Maxwell form. The `w = 1` weight is the multiplicative-identity specialization on `gram_reduce`'s load-bearing normalization-weight axis (the magnetostatic inductance product is the `w = 1/(Iᵢ Iⱼ)` sibling specialization of the SAME combinator — see [`inductance.L4`](./inductance.L4.md)). L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`), `mfem::DenseMatrix C(V.size())` (`:111`), the energy-form `Mult`/`Dot` (`:118-127`), the inverse (`:139-140`).

## Inputs / outputs (the feature surface)

- **Input — config (terminal excitations).** `ElectrostaticConfig`: the terminal-boundary source set (the unit-voltage excitations, → the family-index domain `i`), the H1 space + material permittivity ε (→ the energy operator `K = M_elec`), inherited from the producing driver column. All `readonly` construction-stratum inputs. L0 home: `laplace_op.GetSources()` (`electrostaticsolver.cpp:95`) — the terminal-source map driving the reduction.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` symmetric Maxwell capacitance matrix `C` and its inverse `Cinv`. This is what the electrostatic simulation is run to compute. L0 home: `mfem::DenseMatrix C` (`electrostaticsolver.cpp:111`), `Cinv` (`:139-140`).

## Why this is a clean output-product column

The capacitance product is the cleanest output-product composition root because **its single reduction stage is exactly one firm-track L4 combinator at its simplest weight**:

- The upstream family is supplied whole by the [`electrostatic.L4`](./electrostatic.L4.md) driver column — no re-derivation, just consumption of `(K, [Vᵢ])`.
- The reduction is [`gram_reduce`](../L4/gram_reduce.md) at the **multiplicative-identity weight** `w = 1` (the simplest member of the normalization-weight axis; the magnetostatic inductance product is the non-trivial `w = 1/(Iᵢ Iⱼ)` sibling).
- The inverse `Cinv` is the `gram_inverse` consumer, kept OUT of the reduction (the `nrm2`-style consumer split, `gram_reduce` §Algebraic-laws).

The whole output product therefore lowers cleanly outward to the L4 backend surface: `capacitance = gram_reduce (w ≡ 1) ∘ electrostatic_family` — a one-reduction tail on the electrostatic driver column. The column is `seed` (not promoted past it) because `gram_reduce` is itself `rough-in (test-coverage-bounded)` — its folded L1 primitives are rough-in and there is no dedicated Gram-reduction test.

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column | [`electrostatic.L4`](./electrostatic.L4.md) (driver feature column) | seed | `electrostaticsolver.cpp:21-98` |
| symmetric-Gram reduction (w = 1) | [`gram_reduce`](../L4/gram_reduce.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:100-140` |
| diagonal Vᵢᵀ K Vᵢ (folded) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:118-119` |
| off-diagonal Vⱼᵀ K Vᵢ (folded) | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `electrostaticsolver.cpp:126` |

## Status

`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`electrostatic.L4`](./electrostatic.L4.md) driver column's solution family; stage (2) composes the [`gram_reduce`](../L4/gram_reduce.md) reduction at the voltage `w = 1` specialization. The column stays `seed` (does not promote) because `gram_reduce` is `rough-in (test-coverage-bounded)` — its folded L1 bilinear primitives ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), [`bilinear-form`](../L1/bilinear-form.md)) are rough-in and no dedicated Gram-reduction test exists; a feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (capacitance = the `w = 1` Gram reduction over the electrostatic driver's solution family), not the constituents' per-op algebraic claims (those live in [`gram_reduce`](../L4/gram_reduce.md) and the linked L1 primitives). Evidence: the L0 reduction range `electrostaticsolver.cpp:100-140` (`PostprocessTerminals`) realizing the reduction, plus the firm-track constituent down-links.
