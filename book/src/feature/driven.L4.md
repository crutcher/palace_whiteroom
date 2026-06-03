---
kind: feature-surface
feature: driven
level: L4
status: firm
composes:
  - book/src/L4/fe_assemble.md (firm — assemble the fixed operator basis {K, C, M} once: the assemble-fold combinator)
  - book/src/L4/assemble_frequency_operator.md (firm — the per-ω operand A(ω) = K + iωC − ω²M + A2(ω); the operator-operand linear_combination specialization, rebuilt per member)
  - book/src/L4/frequency_sweep.md (firm — the operator-VARYING per-ω solve map; SetOperators INSIDE the loop)
  - book/src/L4/ksp_solve.md (firm — the per-ω solve cap frequency_sweep maps)
l0_ground_truth:
  - palace/drivers/drivensolver.cpp:37-75 (DrivenSolver::Solve — dispatch to SweepUniform/SweepAdaptive)
  - palace/drivers/drivensolver.cpp:77-229 (DrivenSolver::SweepUniform — the uniform frequency sweep)
---

# driven — L4 composition-root

The **driven (frequency-domain) simulation feature**, presented at L4 as a single
composition of firm L4 combinators — the **outward backend-lowering entry point**
for the frequency-response pipeline. This chapter is a *composition root* (a **leaf
feature column** in the FEATURE-SURFACE SPINE — its stage-2 constituents are
vocabulary ops, not other feature columns): it does not introduce a new combinator;
it wires the already-firm L4 vocabulary into the user-facing feature (config →
frequency response / S-parameters), and links DOWN to each composed piece.

The driven pipeline is the **operator-VARYING** sibling of the fixed-operator
[electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md)
columns. Where those assemble a single stiffness operator `K` **once** and reuse it
unchanged across a fixed-operator [`solve_family`](../L4/solve_family.md) map (the
operator captured once, `SetOperators` hoisted outside the loop), the driven sweep
**rebuilds the system operator `A(ω)` at every swept frequency** before solving —
the [`frequency_sweep`](../L4/frequency_sweep.md) combinator (`SetOperators` *inside*
the loop). That operator-varying shape is exactly what scopes driven *out* of
`solve_family` and into `frequency_sweep`'s `operator-capture = per-element` axis
value. This is the **first feature column all three of whose composition stages
compose FIRM L4 combinators** (the assemble basis, the per-ω rebuild verb, and the
operator-varying solve map are each firm) — the driven solve+assemble halves both
reached L4 in cycles 069/070.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman
`book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the frequency response / S-parameters (the physical product)
    driven :: DrivenConfig -> FrequencyResponse
    driven cfg =
      let space  = nd_space cfg                                   -- the Nédélec H(curl) finite-element space (readonly construction stratum)
          fam    = { K  = fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1a) stiffness, assembled ONCE
                   , C  = fe_assemble space [ damping cfg ]                    -- (1b) damping, assembled ONCE
                   , M  = fe_assemble space [ mass (permittivity cfg) ]        -- (1c) mass, assembled ONCE
                   , A2 = \omega -> extra_system_matrix space cfg omega }      --      ω-dependent extra term (closure)
          omegas = sample_frequencies cfg                          -- the swept ω family (the [Scalar] the map ranges over)
          es     = frequency_sweep fam omegas                      -- (2) operator-VARYING per-ω solve map  ── L4/frequency_sweep
      in  sparameter_reduce es (ports cfg)                         -- (3) per-ω S-parameter / energy reduction → frequency response

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble the fixed operator basis `{K, C, M}` ONCE** —
   [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator
   `fe_assemble space terms = sum (map (assemble_term space) terms)` folds each
   weak-form term list into one of the three fixed basis operators. The basis is the
   `FrequencyOperatorFamily[N]` record `{K, C, M, A2}` captured ONCE before the sweep
   (the `readonly` construction stratum); `K`/`C`/`M` are genuine assemble-folds,
   `A2` is the ω-dependent extra-term closure. L0: `K =
   GetStiffnessMatrix<ComplexOperator>(...)` (`drivensolver.cpp:91`), `C =
   GetDampingMatrix<ComplexOperator>(...)` (`:92`), `M =
   GetMassMatrix<ComplexOperator>(...)` (`:93`), all *before* the sweep loop.

2. **Operator-VARYING per-ω solve map** —
   [`frequency_sweep`](../L4/frequency_sweep.md) (**firm**), which itself composes the
   per-ω operand verb [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md)
   (**firm**) with the per-member [`ksp_solve`](../L4/ksp_solve.md) (**firm**). The
   L4 operator-varying map `frequency_sweep fam omegas = map (\w -> ksp_solve
   (assemble_frequency_operator fam w) (rhs_at fam w)) omegas` captures the **basis**
   `fam` once but **rebuilds the operator `A(ω) = K + iω·C − ω²·M + A2(ω)` inside the
   map** at each ω (the [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md)
   operator-operand `linear_combination` specialization), then runs one
   [`ksp_solve`](../L4/ksp_solve.md) against the rebuilt operator, collecting the per-ω
   solution family `[Eᵢ]`. The load-bearing structural fact — the **non**-hoist — is
   that `SetOperators` sits *inside* the loop because the operator is a function of
   the map index (`frequency_sweep` law 2), the exact negation of `solve_family`'s
   operator-capture-once hoist. This is why driven cannot reuse the fixed-operator
   columns' [`solve_family`](../L4/solve_family.md). L0: per-ω rebuild `A =
   GetSystemMatrix(1.0+0.0i, 1i*ω, −ω²+0.0i, K, C, M, A2)` (`drivensolver.cpp:176-177`),
   the per-ω capture `ksp.SetOperators(*A, *P)` *inside* the loop (`:180`), the per-ω
   RHS `GetExcitationVector(excitation_idx, ω, RHS)` (`:194`), the per-ω solve
   `ksp.Mult(RHS, E)` (`:196`).

3. **S-parameter / frequency-response reduction** — the per-ω reduction of the
   solution family `[Eᵢ]` to the user-facing frequency response (S-parameters,
   per-frequency energy / field measurements). This stage is the **output-product**
   half of the composition root; it is the per-ω post-process measurement
   `MeasureAndPrintAll(...)` (`drivensolver.cpp:216`) plus the B-field recovery `B =
   −1/(iω) ∇×E` (`:205-207`). There is no *new* L4 combinator authored here — the
   driven S-parameter reduction is the **driven output-product surface**, authored as
   its own dedicated output-product feature column [`sparameters`](./sparameters.L4.md)
   (the scattering-matrix `S` column, which links back DOWN to this driver as its
   producing column; its stage-(2) verb [`sparameter_reduce`](../L4/sparameter_reduce.md)
   *(rough-in)* is the port-projection reduction). This mirrors how the
   electrostatic/magnetostatic drivers feed their [`capacitance`](./capacitance.L4.md) /
   [`inductance`](./inductance.L4.md) output-product columns. The shared
   operator-weighted-Gram energy-form reduction combinator
   ([`gram_reduce`](../L4/gram_reduce.md), the capacitance/inductance reductions) does
   NOT subsume the S-parameter reduction (it is a port-projection, not a Gram-weight
   specialization — the c074 D6 / c075 closed-negative distinction); see Open questions.

## Inputs / outputs (the feature surface)

- **Input — config.** `DrivenConfig`: the Nédélec H(curl) space construction (mesh +
  order → `nd_space`), the material coefficients (reluctivity/permittivity/conductivity
  → the `K`/`C`/`M` term coefficients + the ω-dependent `A2`), the swept frequency
  family (the `omega_sample` list → the `[Scalar]` the sweep map ranges over), the
  port-excitation set (→ the per-ω RHS), and the linear-solver configuration (→ the
  per-member `ksp_solve` solver build). All `readonly` construction-stratum inputs.
  L0 home: `SpaceOperator space_op(iodata, mesh)` (`drivensolver.cpp:41`) — `iodata`
  is the config surface; the swept family is `iodata.solver.driven.sample_f`
  (`:45`, `:80`).
- **Output — the physical product.** `FrequencyResponse` — the per-ω frequency
  response: S-parameters and the per-frequency field / energy measurements. This is
  what the user ran the driven solver to compute. L0 home: the per-ω
  `MeasureAndPrintAll(excitation_idx, omega_i, E, B, omega)` measurements
  (`drivensolver.cpp:216`) and the finalize `MeasureFinalize(indicator)` (`:227`).

## Why this composes cleanly (the all-firm operator-varying column)

The driven feature composes cleanly because **every composition stage composes a
firm L4 combinator with no obstruction at the composition level**:

- The basis assemble is three single-term `fe_assemble` folds (the `K`/`C`/`M`
  fixed basis), assembled once before the sweep — the `readonly` construction stratum.
- The per-ω solve is the firm [`frequency_sweep`](../L4/frequency_sweep.md) map,
  itself a clean composition of the firm per-ω operand verb
  [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) and the firm
  per-member [`ksp_solve`](../L4/ksp_solve.md) cap — the operator-VARYING corner,
  with `SetOperators` inside the loop (the non-hoist) the load-bearing structural
  contrast with the fixed-operator columns.
- The reduction is the driven output-product surface (the S-parameter reduction),
  forward-ref'd to its own column — a fold of per-ω measurements, no iterative
  obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface:
`driven = sparameter_reduce ∘ frequency_sweep ∘ fe_assemble(×3)`, an
operator-varying three-stage pipeline of firm combinators with a once-captured
fixed basis and a per-member operator rebuild. This is the test the FEATURE-SURFACE
SPINE directive sets for pulling a feature up: it advances cleanly because the
constituent vocabulary is firm and composes without forcing the spine. (The driven
column is also the spine's clean confirmation that the operator-varying shape — the
harder per-element corner — composes as cleanly as the fixed-operator shape once the
constituent `frequency_sweep` / `assemble_frequency_operator` vocabulary is firm.)

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble basis {K, C, M} once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `drivensolver.cpp:91-93` |
| per-ω operator rebuild A(ω) | [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) | firm | `drivensolver.cpp:175-177` |
| operator-varying per-ω solve map | [`frequency_sweep`](../L4/frequency_sweep.md) | firm | `drivensolver.cpp:168-196` |
| per-ω solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `drivensolver.cpp:196` |
| S-parameter reduction (output product) | [`sparameters`](./sparameters.L4.md) output-product column (verb [`sparameter_reduce`](../L4/sparameter_reduce.md), *rough-in*) | seed (column) | `drivensolver.cpp:205-216` |

## Status

`firm` — the driven feature-surface composition-root, a **leaf feature column**
(per-driver; stage-2 constituents are vocabulary ops) authored under the
FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the
[electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md)
exemplars but at the operator-VARYING corner. **Promoted `seed → firm` cycle-085**
under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE
SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed`
when its OWN composition + directly-owned constituents are firm; cross-linked sibling
columns are references, NOT blockers. The composition is sound and every
directly-owned constituent is firm: stage (1) is three firm
[`fe_assemble`](../L4/fe_assemble.md) folds (the fixed basis captured once); stage (2)
is the firm [`frequency_sweep`](../L4/frequency_sweep.md) map composing the firm per-ω
operand verb [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) with
the firm per-member [`ksp_solve`](../L4/ksp_solve.md) (the operator-varying corner,
`SetOperators` inside the loop). All three directly-owned composition-stage L4
combinators are **firm** — the cleanest operator-varying composition the spine
carries. Stage (3), the S-parameter reduction, is presented as the dedicated
output-product feature column [`sparameters`](./sparameters.L4.md): that is a
**sibling cross-link (a reference / drift-guard), NOT a directly-owned constituent**,
so it does NOT gate this driver column's promotion (the `sparameters` column itself
promotes independently on its own firm reduce verb
[`sparameter_reduce`](../L4/sparameter_reduce.md), firm cycle-083). This chapter
carries the *compositional* claim (driven = this composition of these constituent
pieces), not the constituents' per-op algebraic claims (those live in the linked
chapters). Evidence: the L0 driver range `drivensolver.cpp:37-75` (`Solve` dispatch) +
`:77-229` (`SweepUniform`) realizing the composition, plus the firm constituent
down-links (all line ranges self-verified on-disk via palace-codemap).
