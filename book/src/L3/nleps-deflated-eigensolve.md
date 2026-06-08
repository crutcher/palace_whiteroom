---
layer: L3
operator: nleps-deflated-eigensolve
kind: composition-root (deflation-eigensolve consumer)
status: roadmap_goal
rank: roadmap_goal
edges:
  depends-on:
    - target: L3/eigsolve-impl
      kind: composes                    # the constructive Krylov-Schur/Arnoldi linear eigensolve seeding the NLEPS initial guess (nleps.cpp:470-471); roadmap_goal — the BLOCKING dep its §Pulled-by:122-124 names. This edge CAPS the consumer at roadmap_goal (§(h) well-foundedness) AND carries the liveness that grounds eigsolve-impl off RE11.
    - target: L2/deflate
      kind: composes                    # the oblique/Galerkin complementary projector removing span(X) inside the deflated solve (nleps.cpp:505-537); partly-constructive. deflate itself composes L2/gram — so this edge fires RE3 (the deflate→gram faithful edge becomes reachable through a built consumer).
    - target: L2/gram
      kind: composes                    # the all-pairs XᴴX Gram block (nleps.cpp:524-531) the deflated coordinate solve LU-solves; firm. Named directly here as a constituent (the RE3 faithful deflate→gram edge, surfaced on a real consumer).
    - target: L1/nleps_deflated_solve
      kind: composes                    # the per-step deflated linear solve atom (nleps.cpp:505-537, called :542/:682/:735); firm.
    - target: L1/nleps_deflated_residual
      kind: composes                    # the deflated extended-NEP residual evaluation (nleps.cpp:547-576); firm.
    - target: L1/nleps_eigenvalue_correction
      kind: composes                    # the quasi-Newton eigenvalue update from the projected residual; firm.
    - target: L1/nleps_jacobian_action
      kind: composes                    # the Jacobian-action term of the quasi-Newton step (the deflation Jacobian terms, nleps.cpp:664-667); firm.
  reference:
    - target: L3/lanczos_step
      kind: see-also                    # the symmetric/Hermitian three-term-recurrence basis-extension specialization carried INTO this consumer via eigsolve-impl's Hermitian arm (NOT a direct constituent of the NEP outer loop — it is reached through eigsolve-impl). Navigational.
    - target: L3/eigsolve
      kind: see-also                    # the kernel-api eigsolve gate (partial-obstruction) whose direct_newton orchestration variant treats QuasiNewtonSolver as one opaque step — this consumer is the constructive opening of that variant. Navigational.
    - target: feature/eigenmode.L4
      kind: pulled-by-root              # the GC-root the consumer's reachability terminates at (the eigenmode driver composes the NEP/nonlinear eigensolve path).
    - target: concepts/sequential-obstruction
    - target: concepts/constructed-operators
    - target: semantics/index           # §1.2.1–§1.2.2 named-shape-group convention; §3.7 iterate_while — USED + linked, not restated
variant_axes:
  - problem-symmetry (Hermitian = eigsolve-impl's lanczos_step arm / non-Hermitian = krylov-step arm — selects the linear-eigensolve seed recurrence; inherited via eigsolve-impl)
  - deflation-cardinality k (variadic — grows by one converged column per eigenpair, nleps.cpp:613-619)
  - block-form (Schur-modified NLEPS S = λI − H / bare Galerkin S = I — inherited from L2/deflate's op.block axis)
  - convergence-target (eigenvalue-in-range vs out-of-range guess-index / nev increment, nleps.cpp:623-630)
---

# nleps-deflated-eigensolve

> **⟢ composition-root (deflation-eigensolve consumer).** This chapter COMPOSES already-firm
> vocabulary — it is the L3 (eigenmode-driver-side) consumer that names the
> NLEPS-deflated-eigensolve loop, wiring the deflation projector, the Gram block, the deflated
> solve/residual atoms, and the linear-eigensolve seed kernel-impl into one named composition. It
> does NOT re-derive the per-op algebra (that lives in the linked constituent chapters); it states
> the **deflation laws at the composition level** and cites the outer-loop source as its own
> evidence. It is the **blocking `depends-on` consumer** the [`eigsolve-impl`](./eigsolve-impl.md)
> §Pulled-by names — wiring it FIRES RE3 and GROUNDS `eigsolve-impl` + `lanczos_step`.

> **⟢ roadmap_goal (rank 0) — capped by the rank-0 eigsolve-impl seed.** The consumer's OWN outer
> NEP loop is **positively sourced** (Palace authors `QuasiNewtonSolver::Solve`,
> `palace/linalg/nleps.cpp:351`, `:590-619`), and its deflation atoms are firm. But the chapter
> composes the rank-0 `roadmap_goal` [`eigsolve-impl`](./eigsolve-impl.md) as the linear-eigensolve
> **seed** of the NEP initial guess (`nleps.cpp:470-471`), so the §(h) well-foundedness cap
> (`rank(u) ≤ min over depends-on of rank(v)`) pins the whole chapter at `roadmap_goal`. This is
> the honest landing, not a failed discharge: the GROUNDING (RE3 fire + the eigsolve-impl /
> lanczos_step liveness flip) lands regardless of this chapter's own rank, because liveness flows
> over `depends-on` independent of rank.

## Context

Palace's eigenmode driver solves the nonlinear eigenvalue problem (NEP) `T(λ)·x = 0` for the
pencil `T(λ) = K + λC + λ²M + A2(λ)` (lossy / dispersive media) via a **deflated quasi-Newton
method** (`QuasiNewtonSolver`, `palace/linalg/nleps.cpp:351`). The method computes eigenpairs
**one at a time**, deflating each converged eigenpair so the next solve cannot re-converge to it.
The deflation scheme is SLEPc-NEP's with **minimality index 1** (Effenberger 2013 robust
successive eigenpair computation; Jarlebring–Koskela–Mele 2018 disguised/quasi-Newton —
`palace/linalg/nleps.cpp:356-362`), which solves an **extended problem of size `n + k`** where `n`
is the original problem size and `k` is the count of converged eigenpairs.

This chapter is the **iteration-rotation view of that outer loop, named by composition**. The L3
layer is where global tensor-field operations and field transitions live; the NLEPS-deflated
eigensolve is a field transition (the outer Newton sweep advancing the eigenpair estimate and
growing the invariant pair) built from already-firm field-vocabulary atoms. The per-step body —
the deflated linear solve, the deflated residual, the eigenvalue correction, the Jacobian action —
is firm L1 vocabulary; the deflation projection is the partly-constructive L2 `deflate`; the Gram
block is the firm L2 `gram`; the **initial guess** is seeded from the linear eigensolver, which is
the constructive [`eigsolve-impl`](./eigsolve-impl.md) kernel-impl (`nleps.cpp:470-471`,
`eig_opInv = eig` at `:474`). The consumer threads these into the outer Newton loop.

The outer loop is itself a **sequential obstruction** — it is a carry-threaded one-at-a-time
deflation sweep (each iteration's deflation basis is the prior iterations' converged columns,
`nleps.cpp:613-619`; the schedule does not commute). But Palace AUTHORS the outer loop
(`nleps.cpp:590-619`), so it RENDERS as an explicit value-threaded tail recursion (the
`ksp_solve` / `chebyshev` / `fold_solve` rendering, NOT `eigsolve`'s un-renderable opaque-library
case). The consumer is therefore the **constructive opening of the `direct_newton` orchestration
variant** the kernel-api [`eigsolve`](./eigsolve.md) gate treats as one opaque step.

## Signature

The composition-root form (positional values; the operator-domain shape group `S` follows the
named-shape-group convention of [`semantics/index`](../semantics/index.md) §1.2.1–§1.2.2;
`complex` is the element type throughout — the NEP pencil is complex; the deflation-cardinality
axis `k` is a genuine small-dense coordinate axis, NOT congruent to the field axis `S`):

    nleps_deflated_eigensolve :: (op, control) -> NepResult
    -- op : the NEP operator-parameters surface
    --      (op.pencil = T(λ) = K + λC + λ²M + A2(λ); op.precond = the lagged (K−σM)-style
    --       preconditioned Krylov solver; op.seed = the linear eigensolver for the initial guess).
    -- control : NepControl (requested eigenvalue count nev, target shift σ, nleps_it max
    --           Newton iterations, rtol residual tolerance, inexact-Newton tolerance schedule).

    type NepResult = { eigs   : Tensor[K, complex]                    -- the K converged eigenvalues
                     , X      : Basis[(S: ...), K, complex]           -- the converged invariant-pair basis (k grows to K)
                     , H      : Matrix[K, K, complex]                 -- the Rayleigh-quotient block of the invariant pair
                     , status : NepStatus }                           -- converged / diverged / max-it per eigenvalue

    nleps_deflated_eigensolve op control =
      let s0 = seed_invariant_pair op control            -- X ← []; eigs ← []; H ← [];  initial guess from eigsolve-impl (op.seed)
      in  iterate_while_L3                                 -- OUTER one-at-a-time deflation sweep (Palace-authored; RENDERS)
            s0
            (\s -> length s.eigs < control.nev)            -- until nev eigenvalues converged
            (\s -> converge_one_eigenpair op control s)    -- ONE deflated quasi-Newton solve to a converged pair (below)

      where
        -- converge ONE eigenpair against the current deflation basis s.X, then DEFLATE it in.
        converge_one_eigenpair op control s =
          let g0 = seed_guess op control s                 -- linear-eigensolve seed (eigsolve-impl), deflated against s.X
          in  let (eig, v, v2) = iterate_while_L3          -- INNER quasi-Newton iteration (Palace-authored, nleps.cpp:590)
                    g0
                    (\g -> g.res >= control.rtol && g.it < control.nleps_it)
                    (\g -> quasi_newton_step op control s g)
              in  extend_invariant_pair s eig v v2          -- DEFLATE: X ← X ++ [v/‖v‖]; H bordered; k++  (nleps.cpp:613-619)

        -- ONE quasi-Newton step: deflated residual ▷ projection-direction solve ▷ eigenvalue
        -- correction ▷ deflated Newton-step solve ▷ Armijo backtrack.
        quasi_newton_step op control s g =
          let (r, r2)   = nleps_deflated_residual op.pencil g.eig s.X s.H g.v g.v2   -- deflated extended residual (nleps.cpp:547-576)
              (w0, w2)  = nleps_deflated_solve op.precond s g.eig (r, r2)            -- projection direction T⁻¹r, deflated (nleps.cpp:542)
              eig'      = nleps_eigenvalue_correction op g w0 w2 r r2                -- quasi-Newton λ update from the projected residual
              (du, du2) = nleps_deflated_solve op.precond s eig' (rhs g)             -- the (damped) Newton step, deflated (nleps.cpp:682)
          in  armijo_backtrack op control g eig' du du2                              -- commit the accepted trial

The deflated solve / residual / correction / Jacobian atoms are the firm L1 vocabulary
([`nleps_deflated_solve`](../L1/nleps_deflated_solve.md),
[`nleps_deflated_residual`](../L1/nleps_deflated_residual.md),
[`nleps_eigenvalue_correction`](../L1/nleps_eigenvalue_correction.md),
[`nleps_jacobian_action`](../L1/nleps_jacobian_action.md)); the deflation projection inside each
is the partly-constructive [`deflate`](../L2/deflate.md) over the firm [`gram`](../L2/gram.md); the
`seed_guess` linear eigensolve is the constructive [`eigsolve-impl`](./eigsolve-impl.md). The
`seed_invariant_pair` / `extend_invariant_pair` / `armijo_backtrack` / `seed_guess` /
`converge_one_eigenpair` are this consumer's own composition scaffolding, named inline (not
separate dep-map rows — single consumer; the harvester may promote one to its own entry if a
second consumer appears).

### Record definition

The `NepResult` / `NepControl` records this signature names are layer-local to this consumer
(used by only this chapter), so they get an in-chapter definition home here:

`NepResult` (the converged-invariant-pair carrier, run-time stratum; mirrors the C++
`QuasiNewtonSolver` members `eigenvalues` / `X` / `H` at `nleps.cpp:397,401` and the readout):

| field | type | meaning | stratum |
|---|---|---|---|
| `eigs`   | `Tensor[K, complex]`             | the `K` converged NEP eigenvalues (`eigs.resize(k+1); eigs[k]=eig`, `nleps.cpp:612-613`) | run-time (accreted) |
| `X`      | `Basis[(S: ...), K, complex]`    | the converged invariant-pair basis, `K` columns each congruent to the field shape `S`; raw normalized eigenvectors, **NOT orthonormalized** (`X.resize(k+1); X[k]=v`, `nleps.cpp:614-615`) | run-time (accreted) |
| `H`      | `Matrix[K, K, complex]`          | the Rayleigh-quotient block of the invariant pair (`H.col(k).head(k)=v2/scale; H(k,k)=eig`, `nleps.cpp:616-618`) | run-time (accreted) |
| `status` | `NepStatus`                      | per-eigenvalue converged / diverged-restart / max-it (the `diverged_it`/`restart` logic, `nleps.cpp:635-...`) | run-time |

`NepControl` (the request/config carrier, construction-time stratum; backed by the `QuasiNewton`
config surface — `nev` requested count, the target shift `σ`, `nleps_it`, `rtol`, the
inexact-Newton tolerance schedule `inexact_tol`):

| field | type | meaning | stratum |
|---|---|---|---|
| `nev`         | `Int`            | requested eigenvalue count (the loop's termination target; mutated up on out-of-range converged pairs, `nleps.cpp:630`) | construction-time (config) |
| `σ`           | `Complex`        | the target shift / search region (`sigma`, `nleps.cpp:623`) | construction-time |
| `nleps_it`    | `Int`            | max inner quasi-Newton iterations (`while (it < nleps_it)`, `nleps.cpp:590`) | construction-time |
| `rtol`        | `Double`         | inner residual convergence tolerance (`if (res < rtol)`, `nleps.cpp:604`) | construction-time |
| `inexact_tol` | `Double`         | the inexact-Newton solve-tolerance loosening (`std::max(ksp_rel_tol, inexact_tol)`, `nleps.cpp:541`) | construction-time |

`Basis[(S: ...), K, complex]` and `Matrix[K, K, complex]` are the same shape families the L2
[`deflate`](../L2/deflate.md) / [`gram`](../L2/gram.md) signatures use (`Basis[N, k]` /
`Matrix[k, k]`); the field axis `S` is genuine rank-structured, the cardinality axis `K`/`k` is the
small-dense coordinate axis (deflation rank, single to low hundreds).

## Semantics

The consumer runs the **outer one-at-a-time deflation sweep** (`nleps.cpp:590-619`). Each outer
iteration `converge_one_eigenpair` runs an **inner quasi-Newton iteration** to convergence against
the current deflation basis `X`, then **deflates** the converged pair into `X` so the next outer
iteration cannot re-find it. The pipeline, all read from the positive outer-loop source
(`nleps.cpp:590-630`):

1. **Seed** — the inner iteration's initial guess `(eig, v, v2)` is seeded from the **linear
   eigensolver** (the constructive [`eigsolve-impl`](./eigsolve-impl.md) Krylov-Schur/Arnoldi
   loop), giving the eigenvalue estimate `eig` and the lagged preconditioner eigenvalue
   `eig_opInv = eig` (`nleps.cpp:474`). This is the **blocking `depends-on` constituent** — the NEP
   loop genuinely composes the linear eigensolve to seed each new pair.

2. **Inner quasi-Newton iteration** (`while (it < nleps_it)`, `nleps.cpp:590`): each step composes
   the firm L1 atoms — the [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md) evaluates
   the extended deflated residual `r = T(λ)v + T(λ)X(λI−H)⁻¹v2` (`nleps.cpp:547-576`); the
   [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) inverts the extended deflated block
   system for the projection direction `w0` and the Newton step `du` (`nleps.cpp:542,682`);
   [`nleps_eigenvalue_correction`](../L1/nleps_eigenvalue_correction.md) performs the quasi-Newton
   eigenvalue update; [`nleps_jacobian_action`](../L1/nleps_jacobian_action.md) supplies the
   Jacobian term (the deflation Jacobian terms `nleps.cpp:664-667`). The step is Armijo-backtracked
   (standard constants `nleps.cpp:578-580`).

3. **Deflate** — on convergence (`if (res < rtol)`, `nleps.cpp:604`) the converged `v` is
   normalized (`scale = Norml2(v); v *= 1/scale`, `nleps.cpp:610-611`) and the invariant pair is
   extended by one column: `X.resize(k+1); X[k]=v` (`nleps.cpp:614-615`), `H` bordered
   (`H.col(k).head(k)=v2/scale; H(k,k)=eig`, `:616-618`), `k++` (`:619`). This is the
   variadic-in-`k` growth that the deflation projection [`deflate`](../L2/deflate.md) /
   [`gram`](../L2/gram.md) operate over.

The deflation projection appears **inside** each atom: the [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md)
and [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md) each carry the
`coords ▷ schur-solve ▷ back-project` deflation composition the L2 [`deflate`](../L2/deflate.md)
names (over the L2 [`gram`](../L2/gram.md) block) — the Schur-modified NLEPS form
`SS = −S⁻¹(XᴴX)` with `S = λI − H` (`nleps.cpp:532-535`), NOT the bare Galerkin core. So the
consumer composes `deflate` and `gram` transitively through the firm atoms AND names them directly
as the composition's deflation-projection stage.

Two composition-level points are load-bearing and recorded:

**(1) The seed is a genuine blocking constituent — it caps the rank.** The NEP loop cannot start a
new pair without a linear-eigensolve initial guess (`nleps.cpp:470-471`). That guess is the
constructive `eigsolve-impl`. So `eigsolve-impl` is a faithful `depends-on (composes)` constituent,
not a navigational reference — and because it is rank-0 `roadmap_goal`, the §(h) well-foundedness
cap pins this consumer at `roadmap_goal`. The cap is honest: a firm consumer resting on a rank-0
seed would violate the invariant.

**(2) The outer sweep RENDERS but does not LIFT (sequential obstruction).** The one-at-a-time
deflation sweep is a carry-threaded `sequential-obstruction` (`concepts/sequential-obstruction.md`):
iteration `k`'s deflation basis is iterations `0..k−1`'s converged columns, and the schedule does
not commute (the deflation of an earlier pair changes the operator the later pair sees). Unlike
`eigsolve` (whose loop is opaque-library-owned and un-renderable), Palace authors this loop, so it
RENDERS as the explicit `iterate_while_L3` tail recursion above — the `ksp_solve` / `fold_solve`
rendering class, not the `eigsolve` un-renderable class.

## Algebraic laws (composition level)

The laws below are stated at the composition level — facts about the deflation eigensolve the
composition produces — not re-derivations of the constituent atoms' algebra (which lives in the
linked chapters). "Exact" means exact arithmetic.

1. **Deflation complementarity (oblique-projection, inherited from `deflate`).** At each outer
   iteration the deflated solve/residual operate on the **complement of `span(X)`**: the deflation
   projection annihilates the already-converged basis (`deflate op X X[i] = 0` in the Galerkin
   exact case; the Schur-modified NLEPS form is the corresponding extended-block annihilation —
   [`deflate`](../L2/deflate.md) laws 3–4). This is the defining "deflation" contract: the next
   eigenpair solve **cannot re-converge** to an already-converged eigenvector because that direction
   is projected out of the deflated operator. (Inherited from the firm
   [`nleps_deflated_solve`](../L1/nleps_deflated_solve.md) / `deflate` constituents — stated here as
   the composition-level consequence, not re-derived.)

2. **Locked-vector invariance.** Once a pair `(eig[i], X[i])` is converged and deflated in
   (`nleps.cpp:614-619`), it is **not revisited** — the outer loop only appends columns to `X`
   (`X.resize(k+1)`), never modifies or removes a locked column, and `H` is bordered (the existing
   block is preserved, `H.col(k).head(k)` writes only the new column, `:616-617`). So the converged
   eigenpairs are invariant under subsequent outer iterations (the invariant-pair `(X, H)` is
   monotone-growing). This is the structural guarantee that makes one-at-a-time deflation correct.

3. **Variadic-in-`k` deflation cardinality.** The composition is parameterized by the deflation
   basis size `k`, which grows by exactly one per converged eigenpair (`k++`, `nleps.cpp:619`); it
   is NOT a family of fixed-`k` specializations. The `k = 0` outer iteration is the un-deflated case
   (the first eigenpair) — the deflated solve/residual reduce to their bare big-space forms
   (`nleps_deflated_solve` law 1: `k=0` is the plain `ksp_solve`).

4. **Seed-then-correct decomposition.** Each outer iteration is `seed ▷ quasi-Newton-correct ▷
   deflate`: the linear-eigensolve seed provides the initial estimate; the inner quasi-Newton
   iteration corrects it to a converged NEP eigenpair; the deflation locks it. The seed need not be
   accurate (the inner iteration converges it) — recorded so a caller does not assume the seed IS
   the answer.

Laws that explicitly **do NOT** hold:

- **No whole-loop lift.** The outer one-at-a-time sweep does NOT lift to a global tensor-field
  expression — it is a carry-threaded `sequential-obstruction` (semantics point 2). It RENDERS as a
  tail recursion (Palace-authored), but the un-liftability is the load-bearing non-law. Distinct
  from the BLAS-1 cohort (no obstruction) and from `eigsolve` (opaque-library un-renderable loop).
- **No simultaneous / block convergence.** The method converges eigenpairs **one at a time**, not
  as a block — the deflation depends on the prior pair being fully converged before the next is
  sought. A block reformulation would change the algorithm (it is not the SLEPc-NEP minimality-1
  scheme Palace implements).
- **No λ-linearity / λ-polynomiality.** The inner solve, residual, and Schur block `S = λI − H` are
  rational (not polynomial) in `λ` (inherited from the firm atoms' λ-nonlinearity non-laws). The
  outer correction is quasi-Newton, not a polynomial root-find.
- **Firm rank (capped).** The consumer is NOT firm despite its positively-sourced outer loop,
  because it composes the rank-0 `eigsolve-impl` seed (the §(h) cap). Recorded so the integrator
  does not read the `roadmap_goal` rank as a failed discharge.

## Dependencies

`depends-on (composes)` — blocking constituents (constrain rank, carry liveness):

- [`L3/eigsolve-impl`](./eigsolve-impl.md) (roadmap_goal, kernel-impl) — the constructive
  Krylov-Schur/Arnoldi linear eigensolve seeding the NEP initial guess (`nleps.cpp:470-471`). The
  **rank-capping** dep (§(h)) AND the liveness edge that grounds `eigsolve-impl` off RE11. Its
  §Pulled-by:122-124 names THIS consumer as the blocking edge.
- [`L2/deflate`](../L2/deflate.md) (partly-constructive) — the oblique/Galerkin complementary
  projector removing `span(X)` inside the deflated solve/residual. `deflate` itself composes
  `L2/gram` — so this edge makes the faithful `deflate → gram` constituent edge reachable through a
  built consumer, **firing RE3**.
- [`L2/gram`](../L2/gram.md) (firm) — the all-pairs `XᴴX` Gram block (`nleps.cpp:524-531`) the
  deflated coordinate solve LU-solves. Named directly as a constituent (the RE3 faithful
  `deflate → gram` edge, surfaced on a real consumer).
- [`L1/nleps_deflated_solve`](../L1/nleps_deflated_solve.md) (firm) — the per-step deflated linear
  solve atom.
- [`L1/nleps_deflated_residual`](../L1/nleps_deflated_residual.md) (firm) — the deflated extended-NEP
  residual.
- [`L1/nleps_eigenvalue_correction`](../L1/nleps_eigenvalue_correction.md) (firm) — the quasi-Newton
  eigenvalue update.
- [`L1/nleps_jacobian_action`](../L1/nleps_jacobian_action.md) (firm) — the Jacobian-action term of
  the quasi-Newton step.

`reference` (navigational, free — constrain nothing):

- [`L3/lanczos_step`](./lanczos_step.md) (roadmap_goal, kernel-impl-constituent) — the
  symmetric/Hermitian three-term-recurrence basis-extension specialization. It is reached INTO this
  consumer **via `eigsolve-impl`'s Hermitian arm** (the symmetric-pencil seed recurrence), NOT as a
  direct constituent of the NEP outer loop — so it is a `reference` here, and its grounding comes
  from `eigsolve-impl` being grounded (the liveness reaches `lanczos_step` transitively over
  `eigsolve-impl`'s own `folds` edge). It is the symmetric-pencil basis-extension constituent
  carried via `eigsolve-impl`.
- [`L3/eigsolve`](./eigsolve.md) (partial-obstruction, kernel-api) — the eigsolve gate whose
  `direct_newton` orchestration variant treats `QuasiNewtonSolver` as one opaque step; this consumer
  is the constructive opening of that variant.

The `seed_invariant_pair` / `extend_invariant_pair` / `quasi_newton_step` / `armijo_backtrack` /
`converge_one_eigenpair` / `seed_guess` are this consumer's own composition scaffolding (named
inline, single-consumer — not separate dep-map rows).

## Pulled-by (reachability provenance)

Reachable from a feature root (the liveness guard, [`resolution-ladder`](../methodology/resolution-ladder.md)):

- **Root chain:** [`feature/eigenmode.L4`](../feature/eigenmode.L4.md) (`feature_root: seed`, the
  GC-root) composes the eigenmode/NEP eigensolve path → **this consumer** `depends-on (composes)` →
  `L3/eigsolve-impl` + `L2/deflate` + `L2/gram` + the four firm L1 NLEPS atoms.
- **What this consumer grounds:** it is the **first faithful `depends-on` consumer** of
  `eigsolve-impl` and (transitively, via `eigsolve-impl`) of `lanczos_step` — moving both off the
  RE11 deliberate-reference-only-reachable cohort into ordinary depends-on-reachable liveness. And
  it makes the `deflate → gram` faithful constituent edge reachable through a built consumer,
  **firing RE3** (`graded-stack-baseline-exceptions.md:199`).

## Status

`roadmap_goal` (rank 0) — **composition-root, capped by the §(h) well-foundedness invariant.** The
consumer's OWN outer NEP loop is positively sourced (`QuasiNewtonSolver::Solve`, `nleps.cpp:351`,
`:590-619`) and its deflation atoms are firm L1 vocabulary, BUT it composes the rank-0
`roadmap_goal` [`eigsolve-impl`](./eigsolve-impl.md) as the linear-eigensolve seed
(`nleps.cpp:470-471`), so `rank(consumer) ≤ min over depends-on of rank(v) = rank(eigsolve-impl) =
roadmap_goal`. Promotion route: `roadmap_goal → rough-in → firm` rises in lockstep with
`eigsolve-impl` — when `eigsolve-impl` promotes (its `lanczos_step` constituent firms against the
symmetric-Lanczos L0 + the lowering-verifier audits the impl↔api eigenpair correspondence), this
consumer's cap lifts and it promotes on its own positively-sourced outer-loop structure (the
outer-loop laws are syntactic identities on the positive `nleps.cpp` sweep — the
firm-on-positive-structure escape applies to the consumer's OWN structure once the seed cap clears).

**The GROUNDING is independent of this rank:** wiring the
blocking `depends-on` edges FIRES RE3 (the `deflate → L2/gram` faithful edge is now reachable
through a built consumer) and GROUNDS `L3/eigsolve-impl` + `L3/lanczos_step` off RE11 — liveness
flows over `depends-on` regardless of rank. So even at `roadmap_goal` this consumer discharges RE3
and grounds the two RE11 kernel-impl nodes.

**Single-algorithm concentration** (noted, acceptable): the consumer's only L0 anchor is
`QuasiNewtonSolver` (one solver) — the same concentration accepted for the firm
`nleps_deflated_solve` / `nleps_deflated_residual` atoms. The composition's value is naming the
deflation-eigensolve loop as a coherent field transition and wiring the grounding edges.

**Test-coverage caveat** (inherited, non-gating): NLEPS has zero dedicated unit tests (the same
absence recorded for `eigsolve` / the NLEPS atoms). The outer-loop structure laws are syntactic
identities on the positive sweep; the missing convergence test does not gate them.

## L3 vs lower-layer distinction

- **L0**: `QuasiNewtonSolver::Solve` (`nleps.cpp:351-...`): the outer `while`/`for` deflation sweep
  (`:590-619`), the `deflated_solve` / `compute_residual` lambdas (`:505-537`, `:550-576`), the
  in-place destination buffers, the Armijo backtrack, the `eig_opInv` lag, the restart/divergence
  logic.
- **L3**: the *named composition* `nleps_deflated_eigensolve op control → NepResult` — the outer
  deflation sweep rendered as an `iterate_while_L3` tail recursion, the inner quasi-Newton iteration
  as a second `iterate_while_L3`, the per-step atoms named as firm L1 vocabulary, the deflation
  projection named via `deflate`/`gram`, the seed named via `eigsolve-impl`. L3's role is to name
  the loop as a field transition and surface the deflation laws + the sequential-obstruction at the
  composition level, where at L0 they were a hand-written nested loop of `linalg`/Eigen calls.

## Evidence

Palace ranges (paths relative to `reference/`):

- `palace/linalg/nleps.cpp:351` — `int QuasiNewtonSolver::Solve()`: the outer NEP driver function
  (the consumer's outer-loop home).
- `palace/linalg/nleps.cpp:356-359` — the deflation-scheme comment: "Using the deflation scheme used
  by SLEPc's NEP solver with minimality index set to 1" (`:356`), Effenberger 2013 ref (`:357-358`),
  "the deflation scheme solves an extended problem of size n + k" (`:359`). The SLEPc-NEP
  minimality-index-1 anchor.
- `palace/linalg/nleps.cpp:470-474` — the initial-guess seed: the eigenvector averaging seed
  (`:471` `v.AXPBYPCZ(0.5, eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)`) from the linear
  eigensolver and `eig_opInv = eig` (`:474`, the lagged preconditioner eigenvalue) — the
  `eigsolve-impl` blocking-seed constituent.
- `palace/linalg/nleps.cpp:505-537` — the `deflated_solve` lambda: the deflated extended linear
  solve (`auto deflated_solve =` at `:505`, closing `};` at `:537`). The deflation-projection
  positive site (`coords ▷ schur-solve ▷ back-project`, the `S = λI − H` Schur form).
- `palace/linalg/nleps.cpp:524-531` — the Gram double-loop `SS(i,j) = linalg::Dot(GetComm(), X[i],
  X[j])` (`:529`) = `XᴴX` — the L2 `gram` positive site the deflated solve LU-solves (the RE3
  faithful `deflate → gram` constituent).
- `palace/linalg/nleps.cpp:532-535` — the Schur-modified NLEPS coordinate solve: `S = λI − H`
  (`:532`), `SS = −S⁻¹(XᴴX)` (`:533`), `SS⁻¹·c` (`:534`), `X·(S⁻¹·)` back-projection (`:535`) — the
  `deflate` Schur form.
- `palace/linalg/nleps.cpp:547-576` — the deflated-residual purpose comment (`:547-549`) + the
  `compute_residual` lambda (`auto compute_residual = [this, &k, &H,` at `:550`, closing `};` at
  `:576`): `r = T(λ)v + T(λ)X(λI−H)⁻¹v2`, `r2 = Xᴴv`. The `nleps_deflated_residual` site.
- `palace/linalg/nleps.cpp:578-580` — the Armijo backtrack constants (`armijo_c`,
  `backtrack_factor`, `max_backtrack`) — the inner-step damping.
- `palace/linalg/nleps.cpp:590` — `while (it < nleps_it)`: the inner quasi-Newton iteration loop
  (within `:590-619`).
- `palace/linalg/nleps.cpp:604` — `if (res < rtol)`: the inner convergence test (the deflate-trigger
  branch).
- `palace/linalg/nleps.cpp:610-619` — the converged-pair deflation/basis-extension: normalize
  (`scale = Norml2(v); v *= 1/scale`, `:610-611`), `eigs.resize(k+1); eigs[k]=eig` (`:612-613`),
  `X.resize(k+1)` (`:614`), `X[k]=v` (`:615`), `H` bordered (`:616-618`), `k++` (`:619`). The
  variadic-in-`k` growth + locked-vector invariance (laws 2, 3).
- `palace/linalg/nleps.cpp:623-630` — the in-range / out-of-range guess-index vs `nev` increment
  (`if (eig.imag() > sigma.imag()) guess_idx++ else nev++`) — the convergence-target variant axis.
- `palace/linalg/nleps.cpp:664-667` — the Jacobian deflation terms (`S = eig·I − H` `:664`,
  `XSv2 = MatVecMult(X, S⁻¹v2)` `:666`, nested `S⁻¹(S⁻¹·)` `:667`) — the `nleps_jacobian_action`
  deflation site (back-projection reused with carried coordinates).
- `palace/linalg/nleps.cpp:542,682,735` — the three `deflated_solve` call sites (projection-direction
  setup `:542`, Newton-step solve `:682`, restart projection-direction setup `:735`) — the
  consumer's per-step composition of `nleps_deflated_solve`.

Constituent chapters (firm/roadmap_goal vocabulary this consumer composes):

- `book/src/L3/eigsolve-impl.md` (roadmap_goal, kernel-impl) — the linear-eigensolve seed; this
  consumer is the blocking `depends-on` edge its §Pulled-by:122-124 names.
- `book/src/L3/lanczos_step.md` (roadmap_goal, kernel-impl-constituent) — the symmetric-pencil
  basis-extension carried via `eigsolve-impl` (reference).
- `book/src/L2/deflate.md` (partly-constructive) — the oblique projector; composes `gram` (the RE3
  edge). §Status (firm Schur-form pipeline `nleps.cpp:505-537`; constructive bare-Galerkin core).
- `book/src/L2/gram.md` (firm) — the all-pairs `XᴴX` Gram block.
- `book/src/L1/nleps_deflated_solve.md` (firm) — the per-step deflated linear solve atom.
- `book/src/L1/nleps_deflated_residual.md` (firm) — the deflated extended-NEP residual.
- `book/src/L1/nleps_eigenvalue_correction.md` (firm) — the quasi-Newton eigenvalue update.
- `book/src/L1/nleps_jacobian_action.md` (firm) — the Jacobian-action term.
- `book/src/feature/eigenmode.L4.md` (seed root) — the GC-root the pulled-by chain terminates at.
- `book/src/L3/eigsolve.md` (partial-obstruction, kernel-api) — the `direct_newton` orchestration
  variant this consumer constructively opens (reference).
- `scaffolding/graded-stack-baseline-exceptions.md:199` (RE3 promotion condition — fired here), `:209`
  (RE11 cohort — `eigsolve-impl` + `lanczos_step` grounded here).
- `book/src/methodology/resolution-ladder.md` — the `roadmap_goal` rank-0 discipline + the §(h)
  well-foundedness cap this consumer's rank satisfies.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits; the outer-loop structure laws are
  syntactic identities on the positive sweep, not test-gated.
