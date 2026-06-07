---
agent: harvester
invoked_at: 2026-06-07T071941Z
scope: L1 operator: flux_recovery_estimate
status: pending
inputs:
  - reports/2026-06-07T071941Z-cycle-planner-cycle-122/CYCLE.md (D1 row)
  - book/src/L1/index.md:195 (rough-in dep-map row)
  - book/src/L1-L0/amr-estimate-mark-refine.md (the c121 theme naming this verb)
  - palace/linalg/errorestimator.cpp (ComputeErrorEstimates / FluxProjector / Grad+Curl estimators)
  - palace/linalg/errorestimator.hpp (class structure)
  - palace/fem/errorindicator.cpp:11-47 (ErrorIndicator::AddIndicator running-average fold)
integrated_at: 2026-06-07T071941Z
integration_commit: 17cdafe9d9515c72045691b07420fbdfa25af81a
integration_notes: "cycle-122 D1. Applied clean. L1/flux_recovery_estimate landed FIRM (the ZZ flux-recovery AMR estimate verb; depends-on ksp_solve/apply_linop/nrm2); unresolved_depends_on_targets 2→1. Flat SUMMARY entry (AMR group-intro deferred to c123). 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: Formalize flux_recovery_estimate at L1

## Summary

`flux_recovery_estimate` is the Zienkiewicz–Zhu (ZZ) flux-recovery a-posteriori error
estimate verb, declared as a rough-in row by c121's D7 AMR dispatch and named by the c121
`amr-estimate-mark-refine` L1>L0 theme. It is the **estimate** stage of the AMR
estimate→mark→refine loop. Given a discrete field `F` (the electric field `E` or magnetic
flux density `B`) it (1) recovers a **smooth** flux `G` by an L2 mass-matrix projection of
the *discontinuous* material flux (`εE` for the Grad channel, `μ⁻¹B` for the Curl channel)
onto a smooth conforming FE space, and (2) returns the **per-element squared L2 norm of the
flux difference** `η²_K = ‖flux(F) − G‖²_K`, a vector indexed by mesh element. The recovery
projection `G = M⁻¹·(Flux·F)` is the `FluxProjector::Mult` body
(`palace/linalg/errorestimator.cpp:170-178`); the per-element difference reduction is the
`ComputeErrorEstimates` body (`:184-268`), whose element-local quadrature is performed by a
libCEED integrator that is the **kernel-api leaf** below the verb (referenced, not
re-derived). The current rough-in row carries no signature/laws/applicability — this dispatch
firms all three and resolves the two c121 OQs (flux-channel-axis collapse; FluxProjector
gate-vs-absorbed).

This firms one of the two verbs (with D2's `dorfler_mark`) gating the
`amr-estimate-mark-refine` theme firm-flip, and discharges 1 of the 6
`unresolved_depends_on_targets`.

## Proposed changes

```new:book/src/L1/flux_recovery_estimate.md
---
rank: firm
status: firm
edges:
  depends-on:
    - target: L1/apply_linop
      kind: uses              # the Flux·F discontinuous-flux apply and M·(·) mass apply (operator-domain)
    - target: L1/ksp_solve
      kind: uses              # the M⁻¹ smooth-recovery L2 projection solve (FluxProjector closure)
    - target: L1/nrm2
      kind: uses              # the per-element L2 norm shape of the flux difference (element-local reduction)
  reference:
    - L1-L0/fe-assemble-libceed-boundary-obstruction   # the libCEED element-quadrature kernel-api below the per-element integral
    - L1-L0/amr-estimate-mark-refine                   # the estimate→mark→refine theme this verb is the estimate stage of
    - L1/fe_space                                       # operates-on: the trial + smooth FE spaces (not a dep)
    - L1/interpolator                                   # sibling FE-space de-Rham operator (the flux maps live on the same de-Rham complex)
---

# flux_recovery_estimate

**Slug:** `flux_recovery_estimate`

The Zienkiewicz–Zhu **flux-recovery a-posteriori error estimate** verb — the *estimate* stage
of the AMR estimate→mark→refine loop. It maps a discrete field `F` to a **per-element error
indicator** by comparing the (cheap, discontinuous) material flux of `F` against a (smooth,
recovered) projection of that same flux onto a conforming FE space. Where the two disagree, the
discretization is under-resolved.

## Signature

    type FluxChannel = Grad | Curl   -- selects the flux map and the (trial, smooth) FE-space pair

    flux_recovery_estimate
      :: FluxEstimator   -- closure: flux map + smooth-recovery projector + element integrator
      -> Tensor[N]       -- F : the field true-dof vector (E for Grad, B for Curl)
      -> Tensor[E]       -- η² : per-element SQUARED error indicator, one entry per mesh element

`F : Tensor[N]` is a flat true-dof vector (rank-1; Palace `Vector`), and the result
`Tensor[E]` is a flat rank-1 vector of length `E = #elements` — a genuine per-element list,
**not** a field-space tensor. (Per the semantic surface, `Tensor[N]`/`Tensor[E]` are faithful
rank-1 spellings at L1; see `book/src/semantics/index.md` §1.2.1.)

The primary argument is a **constructed-operator** value `FluxEstimator` (the closure built by
the `GradFluxErrorEstimator` / `CurlFluxErrorEstimator` constructor), structured-opaque about
its flux map, its recovery solver, and its element integrator — the same
**constructed-operator absorption** motif as `ksp_solve` / `eigsolve` / `chebyshev-smoother`
(L1 §Semantics motif 4). See `## Record definition` for its fields.

The verb returns the **squared** per-element indicator. The √ and energy
nondimensionalization — `η_K ← √(η²_K · (Et>0 ? 0.5/Et : 1))` — is a thin epilogue applied by
the caller `AddErrorIndicator` (`palace/linalg/errorestimator.cpp:386` for Grad,
`:508` for Curl), not part of the verb; it is recorded as a §Law (law 5).

## Semantics

Let `flux(F)` be the **discontinuous material flux** of the field — `εE` for the Grad
(electric) channel, `μ⁻¹B` for the Curl (magnetic) channel — and let `G` be its **smooth
recovery**, the L2 projection of `flux(F)` onto a conforming smooth FE space. The estimate is
the per-element squared L2 norm of their difference:

$$ \eta^2_K \;=\; \int_K \bigl\lVert \mathrm{flux}(F) - G \bigr\rVert^2 \, dx, \qquad K \in \text{elements}. $$

The verb is a two-step pipeline over the closure:

1. **Smooth recovery (the projection).** `G = M⁻¹·(Flux·F)`, the body of `FluxProjector::Mult`
   (`palace/linalg/errorestimator.cpp:170-178`): `Flux·F` assembles the RHS of the L2
   projection (`Flux` is the partially-assembled `coeff`-weighted mass cross-operator from the
   field space to the smooth space, `:151-162`), and `M⁻¹·(·)` solves the smooth-space mass
   system `M G = Flux F` (`ksp->Mult(rhs, y)`, `:177`). `M` and `Flux` are assembled **once**
   in the `FluxProjector` constructor (`:109-167`) and the Krylov solver `ksp` is configured
   there (`:163`); the projection at estimate time is a single `apply_linop` + `ksp_solve`.

2. **Per-element difference reduction.** `ComputeErrorEstimates`
   (`palace/linalg/errorestimator.cpp:184-268`) prolongates `F` and `G` to L-dofs
   (`:202-204`), then runs a **libCEED element integrator** (`CeedOperatorApplyAdd`,
   `:251-253`) that, per element, integrates `‖flux(F) − G‖²` over the element and writes the
   scalar into `estimates[K]` (the per-element vector, allocated `:209-210` and initialized to zero at `:211`). The
   element-local quadrature is the libCEED kernel — see `## libCEED kernel-api leaf`.

**Complex fields.** For `ComplexVector` the integrator runs twice (real then imag part) and
**adds** the two squared contributions into `estimates` before the (later) √
(`palace/linalg/errorestimator.cpp:254-260`) — i.e. `η²_K = ‖flux(Fʳ)−Gʳ‖²_K +
‖flux(Fⁱ)−Gⁱ‖²_K`. This is the element-type variant axis; it changes only the per-element
accumulation count, not the verb's shape or laws.

## Flux-channel variant axis

The verb has ONE material variant axis, **flux-channel**, selecting the flux map and the
(trial, smooth) FE-space pair:

| channel | field `F` | discontinuous flux | trial space | smooth space | L0 ctor |
|---|---|---|---|---|---|
| **Grad** (electric) | `E` | `εE` | ND (`nd_fespace`) | RT (`rt_fespace`) | `GradFluxErrorEstimator` `palace/linalg/errorestimator.cpp:273-378` |
| **Curl** (magnetic) | `B` | `μ⁻¹B` | RT (`rt_fespace`) | ND (`nd_fespace`) | `CurlFluxErrorEstimator` `:391-500` |

The two channels are **structurally identical** — both build a `FluxProjector` with a
material-property `coeff` (`ε` resp. `μ⁻¹`) and the matching mass integrator, both run the same
`ComputeErrorEstimates` pipeline; they differ only in the `coeff` and the (trial, smooth)
space pair (which are mirror-swapped: ND→RT for Grad, RT→ND for Curl). So flux-channel is a
**closure-absorbed parametric axis**, not a structural branch in the verb body.

**The composite is NOT a third estimate verb (OQ resolved).** The "Grad+Curl composite" used
by the 3D drivers (`TimeDependentFluxErrorEstimator`, `BoundaryModeFluxErrorEstimator`)
computes the two channels **separately** and combines them by the elementwise vector add
`grad_estimates += curl_estimates` over the **squared** indicators
(`palace/linalg/errorestimator.cpp:536`, `:566`):

$$ \eta^2_K \;=\; \lVert \varepsilon E - D\rVert^2_K + \lVert \mu^{-1}B - H\rVert^2_K. $$

This is an `axpy(1, curl_estimates, grad_estimates)` / `linear_combination`-over-indicators
shape on the per-element indicator vectors — it composes two `flux_recovery_estimate` results,
it does **not** introduce a new estimate kernel. (OQ
`flux-recovery-estimate-flux-channel-axis-vs-separate-verbs` resolves: flux-channel is a
single parametric axis on one verb; the composite is an L2-level `linear_combination` over
indicator vectors, NOT a 3rd verb. The over-mark factor `0.5/Et` √-scaling is the same shared
epilogue regardless of channel.)

## libCEED kernel-api leaf

The per-element integral `∫_K ‖flux(F) − G‖² dx` is performed by a **libCEED composite
operator** (`integ_op`), assembled per element-geometry in the channel constructor
(`AssembleCeedElementErrorIntegrator` + `info.apply_qf = f_apply_hcurlhdiv_error_*`,
`palace/linalg/errorestimator.cpp:340-371`) and applied via `CeedOperatorApplyAdd`
(`:251-253`). This element-quadrature kernel is the on-disk **kernel-api leaf**
[`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
(`obstruction (opaque-library-ownership)`); its from-our-primitives realization is
[`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). This verb **references**
that contract and does not re-derive the quadrature — the verb's own content is the
recovery-projection + difference-reduction *composition*, with the element integral as an
opaque leaf.

## Record definition

`FluxEstimator` is the constructed-operator closure consumed by `flux_recovery_estimate`. It
is used by **only this operator** (the AMR estimate verb), so it is defined in-chapter (the
record-definition obligation, single-consumer case). It mirrors the C++
`GradFluxErrorEstimator` / `CurlFluxErrorEstimator` private members
(`palace/linalg/errorestimator.hpp:65-92` for Grad, `:98-125` for Curl).

    type FluxEstimator = {
      channel    : FluxChannel,                 -- Grad | Curl (selects flux map + space pair)
      projector  : FluxProjector,               -- the smooth-recovery L2 projection closure
      integ_op   : ceed.Operator,               -- libCEED per-element difference integrator (kernel-api leaf)
      trial_fespace  : FiniteElementSpace,      -- space F lives in (ND for Grad, RT for Curl)
      smooth_fespace : FiniteElementSpace,      -- conforming recovery space (RT for Grad, ND for Curl)
    }

    type FluxProjector = {
      Flux : LinearOperator[Ns, N],   -- coeff-weighted mass cross-operator (field space → smooth space)
      M    : LinearOperator[Ns, Ns],  -- smooth-space FE mass operator (SPD)
      ksp  : Solver[M],               -- Krylov solver for the M G = Flux F projection (closed-over)
    }

| field | type | stratum | meaning / L0 home |
|---|---|---|---|
| `channel` | `FluxChannel` | construction | electric (Grad) vs magnetic (Curl); fixes `coeff` + space pair. `errorestimator.cpp:273` / `:391` |
| `projector` | `FluxProjector` | construction | the recovery projection closure; built once in ctor (`:283-285` Grad). |
| `integ_op` | `ceed.Operator` | construction | per-element difference integrator; assembled per geometry (`:340-371`); the kernel-api leaf. |
| `trial_fespace` / `smooth_fespace` | `FiniteElementSpace` | construction | the operated-on FE spaces (`errorestimator.hpp:71` / `:108`). |
| `Flux` | `LinearOperator[Ns, N]` | construction | partial-assembled coeff-mass cross-operator (`errorestimator.cpp:151-162`). |
| `M` | `LinearOperator[Ns, Ns]` | construction | smooth-space SPD mass operator (`:124-148`). |
| `ksp` | `Solver[M]` | construction | configured projection solver (`:163`). |

All fields are **construction-time** — the verb's run-time input is only `F : Tensor[N]`. This
resolves the OQ `flux-projector-constructed-operator-gate-vs-absorbed`: `FluxProjector` is a
**construction-time member absorbed into the `FluxEstimator` closure**, not a separate run-time
gate argument (the same absorption as `ksp_solve`'s closed-over preconditioner). It is recorded
as a nested record here for definition-home completeness, not surfaced as a verb operand.

## Algebraic laws

Let `fre = flux_recovery_estimate(est, ·)`. The following hold:

1. **Per-element locality (no cross-element coupling in the reduction).** `η²_K` depends only on
   `flux(F)` and `G` restricted to element `K` — the libCEED integrator writes
   non-overlapping entries (`palace/linalg/errorestimator.cpp:245`, "Each thread writes to
   non-overlapping entries"). The *recovery* step `G = M⁻¹·Flux·F` is global (the projection
   couples elements through `M⁻¹`), but the *difference reduction* is element-local. So the
   verb is **not** a fully element-local map — locality holds for the reduction only, and is the
   reason the channels can be composed by an elementwise vector add (law 4).

2. **Non-negativity.** `η²_K ≥ 0` for every `K` — each entry is an integral of a squared norm
   (`∫_K ‖·‖² ≥ 0`); `estimates` is zero-initialized and only `ApplyAdd`-accumulated
   (`:211`, `:251-253`). (This is the squared indicator; the caller's √ is well-defined.)

3. **Exactness vanishing (recovery fixed point).** If `flux(F)` already lies in the smooth
   recovery space, then `G = flux(F)` (the L2 projection of a member of the space is itself) and
   `η²_K = 0` for all `K`. The estimate detects exactly the *non-conformity* of the
   discontinuous flux — the ZZ premise. (Structural consequence of `G = M⁻¹·Flux·F` being the
   L2 projection; not separately Palace-tested, recorded as a definitional property of the ZZ
   construction.)

4. **Channel-additivity over squared indicators (composite law).** The 3D composite is the
   elementwise sum of the per-channel squared indicators:
   `composite(E, B)_K = fre(grad_est, E)_K + fre(curl_est, B)_K`
   (`palace/linalg/errorestimator.cpp:536`, `:566`). This is `axpy(1, ·, ·)` /
   `linear_combination` over indicator vectors — the composite is **not** a new verb (the OQ
   resolution). Composing in the **squared** domain is load-bearing: the global error
   `E² = (1/N)Σ Eₙ²` decomposition requires squared accumulation (see law 5 / the
   `ErrorIndicator` averaging note `palace/fem/errorindicator.cpp:27-43`).

5. **Caller epilogue (√ + energy nondimensionalization).** The indicator consumed by the AMR
   loop is `η_K = √(η²_K · s)` with `s = (Et > 0 ? 0.5/Et : 1)` — the `linalg::Sqrt` epilogue
   (`palace/linalg/errorestimator.cpp:386`, factor-of-½ energy correction). This is applied
   **after** the verb (in `AddErrorIndicator`), is shared across channels, and commutes with
   the per-element structure (an elementwise scale-then-√). Recorded as a caller law because the
   verb's natural codomain is the squared indicator; the √-domain identity
   `√(a²+b²) = nrm2([a,b])` is the connection to `nrm2` in §Dependencies.

**Non-laws.**

- **No linearity in `F`.** `fre(est, F)` is **quadratic** in `F` (it is `‖affine(F)‖²` per
  element, where `affine(F) = flux(F) − M⁻¹·Flux·F` is linear in `F`). `fre(est, αF) =
  |α|² · fre(est, F)` (homogeneity of degree 2), but `fre(est, F+F') ≠ fre(est, F) +
  fre(est, F')`. The verb is therefore NOT an `apply_linop` variant.

- **No reduction-order non-associativity claim across elements.** The per-element entries are
  independent writes (law 1); there is no cross-element summation in the verb (the
  cross-element global-error √-sum is the `ErrorIndicator` running average,
  `palace/fem/errorindicator.cpp:11-47`, outside this verb). Inside a single element the
  quadrature sum is the libCEED kernel's (kernel-api leaf), not this verb's algebra.

## Dependencies

L1-internal `depends-on (uses)`:

- [`ksp_solve`](./ksp_solve.md) — the `M⁻¹·(·)` smooth-recovery L2 projection solve
  (`FluxProjector::Mult`, `palace/linalg/errorestimator.cpp:177`); closed over by the
  `FluxProjector` field of the closure.
- [`apply_linop`](./apply_linop.md) — the `Flux·F` discontinuous-flux RHS assembly
  (`:176`), operator-domain application of the coeff-mass cross-operator.
- [`nrm2`](./nrm2.md) — the per-element L2 norm shape of the flux difference; the squared
  per-element entry is `nrm2(flux(F)−G | K)²` and the caller √-epilogue (law 5) realizes the
  outer `nrm2` over the element. (The element-local integral itself is the libCEED kernel-api
  leaf, referenced not depended-on.)

`reference` (navigational, non-blocking):

- [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
  — the libCEED element-quadrature **kernel-api** below the per-element integral; its impl is
  [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). Referenced, not
  re-derived (DIRECTIVE-3: this verb is a *consumer* of the kernel-api, not its realization).
- [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) — the estimate→mark→refine
  theme; this verb is its **estimate** stage (`dorfler_mark` is the mark stage).
- [`fe_space`](./fe_space.md) — operates-on the trial + smooth FE spaces (a consumed-by/
  operates-on relation, not a blocking dependency).

## Status

`firm` (AMR estimate verb; flux-channel variant axis Grad/Curl, composite an L2
`linear_combination` over indicators NOT a 3rd verb).

Promoted rough-in→**firm** on the **firm-on-positive-structure escape** (the `apply_linop` /
`jacobi-smoother` / `reciprocal` no-dedicated-test precedent): every law is a syntactic
identity / structural-property read-off on **fully-specified positive source** — the recovery
projection `M⁻¹·Flux·F` is read in full at `FluxProjector::Mult`
(`palace/linalg/errorestimator.cpp:170-178`), the per-element difference reduction in full at
`ComputeErrorEstimates` (`:184-268`), both channel constructors in full
(`:273-378` Grad, `:391-500` Curl), and the composite `+=` at `:536`/`:566`. The
quadratic-in-`F` non-law and the non-negativity / per-element-locality / channel-additivity
laws are operator-algebra / squared-norm facts, not convergence facts — the absence of a
dedicated error-estimator unit test (AMR is integration-covered only, exercised through the
adaptive driver) does not gate syntactic-identity laws. The two constructive sub-parts that
ride opaque leaves — the libCEED element integral and the `ksp_solve` projection convergence —
are referenced kernel-api / firm-constituent boundaries, not reconstructed claims, so they do
not force `partly-constructive`.

**Single-rank reading (DIRECTIVE-1).** `ComputeErrorEstimates` is read single-rank: the
per-element `estimates` vector is local-element-indexed; the cross-rank reductions in the
*surrounding* AMR loop (global-error averaging, Dörfler threshold bisection — D2's territory)
are out of this verb's body. The L1 signature carries no communicator.

## Evidence

- `palace/linalg/errorestimator.cpp:184-268` — `ComputeErrorEstimates`: the verb core
  (recovery via `projector.Mult` at `:193`, prolongation `:202-204`, per-element libCEED
  difference integration `:251-253`, complex two-pass accumulation `:254-260`, return
  `estimates` `:267`).
- `palace/linalg/errorestimator.cpp:170-178` — `FluxProjector::Mult`: `G = M⁻¹·(Flux·F)`
  (`Flux->Mult(x, rhs)` `:176`, `ksp->Mult(rhs, y)` `:177`).
- `palace/linalg/errorestimator.cpp:109-167` — `FluxProjector` ctor: `M` (smooth-space mass,
  `:124-148`), `Flux` (coeff-weighted cross-mass, `:151-162`), `ksp` (`:163`) — the
  construction-stratum absorption.
- `palace/linalg/errorestimator.cpp:273-378` — `GradFluxErrorEstimator` ctor: `coeff = ε`
  (`:279`), ND→RT spaces (`:277`), libCEED integrator assembly (`:340-371`).
- `palace/linalg/errorestimator.cpp:391-500` — `CurlFluxErrorEstimator` ctor: the `coeff =
  μ⁻¹` magnetic mirror (RT→ND).
- `palace/linalg/errorestimator.cpp:380-388`, `:502-510` — per-channel `AddErrorIndicator`:
  the `linalg::Sqrt((Et>0)?0.5/Et:1)` epilogue (`:386` Grad, `:508` Curl) + `indicator.AddIndicator`.
- `palace/linalg/errorestimator.cpp:525-538`, `:555-567` — the 3D composite
  `grad_estimates += curl_estimates` (`:536`, `:566`): the channel-additivity law over squared
  indicators (NOT a 3rd verb).
- `palace/linalg/errorestimator.hpp:34-125` — `FluxProjector` (`:34-56`), `GradFluxErrorEstimator`
  (`:65-92`), `CurlFluxErrorEstimator` (`:98-125`) class structure (the record-definition home).
- `palace/fem/errorindicator.cpp:11-47` — `ErrorIndicator::AddIndicator`: the squared-then-√
  running-average fold that consumes the verb output (the reason laws 4/5 compose in the
  squared domain) — outside the verb, cited for the epilogue/composition rationale.
```

Replace the rough-in dep-map row at `book/src/L1/index.md:195` (the `Rough-in (AMR estimate/mark
vocabulary)` group) with the firm row below. The OLD row is:

```text
| `flux_recovery_estimate` *(rough-in; no anchor yet; proposed-by: abstractor:2026-06-07T054924Z-amr-estimate-mark-refine)* | ZZ flux-recovery a-posteriori error estimate `est ▷ field → per-element-indicator`; recover smooth flux by projecting the discontinuous material flux (εE / μ⁻¹B) onto a smooth FE space, return per-element L2 norm of the difference. The AMR estimate verb; flux-channel variant axis (Grad / Curl / Grad+Curl composite). libCEED quadrature integrator is a kernel-api leaf below. | `palace/linalg/errorestimator.cpp:184-268`, `:273-378`, `:391-500` | rough-in |
```

The NEW row (firm; the dep-map cell uses L1-internal `depends-on` only, per the §Working-Notes
convention):

```edit:book/src/L1/index.md
| [`flux_recovery_estimate`](./flux_recovery_estimate.md) | `FluxEstimator → Tensor[N] → Tensor[E]` (ZZ flux-recovery a-posteriori error estimate: recover the smooth flux `G = M⁻¹·Flux·F` by L2 projection of the discontinuous material flux `εE`/`μ⁻¹B` onto a smooth FE space, return the per-element SQUARED L2 difference `η²_K = ‖flux(F)−G‖²_K`, one entry per mesh element) | `ksp_solve`, `apply_linop`, `nrm2` | `firm` (AMR estimate verb; **flux-channel variant axis** Grad (εE, ND→RT, `errorestimator.cpp:273-378`) / Curl (μ⁻¹B, RT→ND, `:391-500`); the 3D Grad+Curl composite is an elementwise `linear_combination`/`axpy(1,·)` over squared indicators `:536`/`:566`, NOT a 3rd verb (OQ resolved); `FluxProjector` is a construction-absorbed closure member NOT a run-time gate (OQ resolved); libCEED element-quadrature integrator below is the `kernel-api` leaf `fe-assemble-libceed-boundary-obstruction`, referenced not re-derived; verb core `ComputeErrorEstimates` `palace/linalg/errorestimator.cpp:184-268` + projection `FluxProjector::Mult` `:170-178`; firm-on-positive-structure, no-dedicated-test caveat non-gating per `jacobi-smoother`/`reciprocal`; laws: per-element-locality (reduction-only), non-negativity, exactness-vanishing, channel-additivity-over-squared-indicators, caller-√-epilogue; NON-laws: quadratic-in-F (homogeneity deg-2, NOT `apply_linop`), no-cross-element-reduction; read single-rank (DIRECTIVE-1); harvested cycle-122; L1>L0: estimate stage of `amr-estimate-mark-refine`) |
```

**§Vocabulary-cohort registration (D1's OWN cohort bullet — appended to the
`Rough-in (AMR estimate/mark vocabulary)` sub-list, flipped to firm).** Add this bullet under the
AMR vocabulary cohort (do NOT touch the main-cohort firm count/tally — `flux_recovery_estimate`
is a NEW AMR-vocabulary-group member, distinct from the 43-member L1 firm grand total which is
the main + FE-assembly + FE-space + Mesh-construction sub-spines; the AMR group carries no
consolidated running count per the overlap analysis):

```text
- [`flux_recovery_estimate`](./flux_recovery_estimate.md) — ZZ flux-recovery a-posteriori error estimate; the **estimate** stage of the AMR estimate→mark→refine loop. Recovers the smooth flux `G = M⁻¹·Flux·F` (L2 mass projection of the discontinuous material flux `εE`/`μ⁻¹B`, `FluxProjector::Mult`) then returns the per-element squared L2 difference `η²_K = ‖flux(F)−G‖²_K`. Flux-channel variant axis (Grad electric / Curl magnetic); the 3D composite is an elementwise `linear_combination`/`axpy(1,·)` over squared indicators (`errorestimator.cpp:536`/`:566`), NOT a 3rd verb. `FluxProjector` construction-absorbed (closure member, not a run-time gate). libCEED element-quadrature integrator below is the `kernel-api` leaf (`fe-assemble-libceed-boundary-obstruction`), referenced not re-derived. Firm-on-positive-structure (no-dedicated-test caveat non-gating). Quadratic-in-`F` (NOT an `apply_linop` variant). Read single-rank. Harvested cycle-122; one of the two verbs gating the `amr-estimate-mark-refine` theme firm-flip (with `dorfler_mark`).
```

```edit:book/src/SUMMARY.md
- [AMR estimate / mark](./L1/amr-estimate-mark-intro.md)
  - [flux_recovery_estimate](./L1/flux_recovery_estimate.md)
```

**SUMMARY note for the integrator.** `flux_recovery_estimate` (D1) and `dorfler_mark` (D2) are
the first two members of a NEW L1 sub-chapter group `AMR estimate / mark`, parallel to the
index's existing `Rough-in (AMR estimate/mark vocabulary)` dep-map group. The group intro page
`./L1/amr-estimate-mark-intro.md` does **not** yet exist — it is the `layer-intro-author`'s
artifact (a by-kind group intro per `feedback_mdbook_subchapter_grouping_and_alpha_api`). Insert
the `flux_recovery_estimate` chapter entry alphabetically within the group; place the group AFTER
`Mesh & FE-space construction` / `FE-space sub-spine` (or wherever the layer-intro-author files
the AMR group). If the group intro does not land this cycle, register `flux_recovery_estimate`
as a flat chapter under the existing L1 Part rather than a live-linked group header pointing at a
missing intro file (a link to a missing file is a hard `linkcheck2` error). See Open questions
(`amr-estimate-mark-group-intro-needs-authoring`).

## Supporting evidence

- **Source self-verification (citecheck, on-disk `--anchor` pass).** Every load-bearing
  pinpoint confirmed against `reference/palace/palace/linalg/errorestimator.cpp`:
  `ComputeErrorEstimates` `:184` [ok], `projector.Mult` `:193` [ok], `GradFluxErrorEstimator`
  `:273` [ok], `CurlFluxErrorEstimator` `:391` [ok], `FluxProjector` ctor `:109` [ok],
  `FluxProjector::Mult` `:170` [ok], Grad `AddErrorIndicator` `:381` [ok], Curl
  `AddErrorIndicator` `:503` [ok], composite `grad_estimates += curl_estimates` `:536` [ok] +
  `:566` [ok], `linalg::Sqrt` epilogue `:386` [ok], `errorestimator.hpp:34` `FluxProjector`
  [ok], `errorindicator.cpp:11` `AddIndicator` [ok]. **Drift correction applied at emit time:**
  the planner's `:529-566` composite range and the codemap's first-look line numbers drifted
  +3 on the `+=` site — the actual elementwise-add composite is at `:536` (TimeDependent) and
  `:566` (BoundaryMode), and the √ epilogue at `:386` (Grad)/`:508` (Curl); cited the corrected lines.
- **The c121 `amr-estimate-mark-refine` theme** (`book/src/L1-L0/amr-estimate-mark-refine.md`)
  names this verb as its estimate stage and cites the same `:184-268` / `:273-378` / `:391-500`
  ranges as `cites-evidence`; firming this verb (with `dorfler_mark`) fires the theme's
  rough-in→firm gate (OQ `amr-estimate-mark-refine-theme-firmness-gate`).
- **Kernel-api leaf** `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` + impl
  `book/src/L1/libceed-quadrature-kernel-impl.md` both on disk — referenced, not re-derived.

## Open questions / caveats

- **`flux-recovery-estimate-flux-channel-axis-vs-separate-verbs` — RESOLVED.** Flux-channel
  (Grad/Curl) is a single closure-absorbed parametric axis on ONE verb; the 3D Grad+Curl
  composite is an elementwise `linear_combination`/`axpy(1, curl, grad)` over the **squared**
  per-element indicator vectors (`errorestimator.cpp:536`/`:566`), NOT a third estimate kernel.
  The composite belongs at L2 as a `linear_combination` over indicators, not as a new L1 verb.
- **`flux-projector-constructed-operator-gate-vs-absorbed` — RESOLVED.** `FluxProjector` is a
  **construction-time member absorbed into the `FluxEstimator` closure** (built once in the
  channel ctor, `errorestimator.cpp:283-285`; called by `Mult`), not a run-time gate argument.
  The verb's only run-time operand is `F : Tensor[N]`. (Same absorption as `ksp_solve`'s
  closed-over preconditioner.) `FluxProjector` is documented as a nested record in the
  `## Record definition` section for definition-home completeness.
- **`amr-estimate-mark-group-intro-needs-authoring` — NEW, flagged for `layer-intro-author`.**
  The new L1 SUMMARY sub-chapter group `AMR estimate / mark` (members `flux_recovery_estimate`
  D1 + `dorfler_mark` D2) needs a by-kind group intro page `book/src/L1/amr-estimate-mark-intro.md`.
  Until it exists, register the two chapters flat (a live link to a missing intro is a hard
  `linkcheck2` error). The index already carries the matching dep-map group header
  `Rough-in (AMR estimate/mark vocabulary)` (now misnamed once both verbs are firm — the
  layer-intro-author should rename it to drop "Rough-in").
- **Composite-as-L2-`linear_combination` is a deferred abstractor pick.** The Grad+Curl
  composite (`TimeDependentFluxErrorEstimator` / `BoundaryModeFluxErrorEstimator`) is an
  elementwise sum over squared indicators — a clean operator-operand-free `linear_combination`
  over `Tensor[E]` indicator vectors. It is NOT authored here (one operator per invocation; the
  composite composes two `flux_recovery_estimate` results). Flag for a future abstractor/
  combinator-miner pick if a 2nd indicator-combining site surfaces; for now the composite law
  (law 4) records the shape in-chapter without minting a new entry (avoiding the
  mine-and-strand / identity-in-named-terms smell — it is `axpy(1,·)` already firm).
- **`ksp_solve` projection convergence + libCEED integral are referenced opaque boundaries,
  not reconstructed.** The recovery `M⁻¹·Flux·F` rests on the firm `ksp_solve` (convergence is
  its concern), and the per-element integral rests on the libCEED kernel-api. Neither is a
  constructive sub-part materialized from negative anchors, so the verb is `firm`, not
  `partly-constructive`. If a future scope widens to reconstruct the libCEED error-integrand
  QFunction (`f_apply_hcurlhdiv_error_*`), that lands in the `libceed-quadrature-kernel-impl`
  node, not here.
- **Single-rank (DIRECTIVE-1).** The verb is read single-rank; the cross-rank global-error
  averaging (`ErrorIndicator::AddIndicator` MPI reduction) and the Dörfler threshold bisection
  (D2's `dorfler_mark`) are out of this verb's body. No communicator in the L1 signature.
