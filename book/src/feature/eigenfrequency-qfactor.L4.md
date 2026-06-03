---
kind: feature-surface
feature: eigenfrequency-qfactor
level: L4
status: seed
composes:
  - book/src/feature/eigenmode.L4.md (seed — the producing driver column: supplies the converged eigenpair family)
  - book/src/L4/eigenfreq_qfactor_reduce.md (rough-in — the per-mode scalar-ratio reduction combinator)
l0_ground_truth:
  - palace/drivers/eigensolver.cpp:424-439 (the eigenvalue→ω un-transform in the readout loop)
  - palace/models/postoperator.cpp:1171-1203 (MeasureLumpedPortsEig — the Q-factor computation)
---

# eigenfrequency-qfactor — L4 composition-root (output product)

The **eigenfrequency + quality-factor table** output product, presented at L4 as a single composition of L4 vocabulary — the **outward backend-lowering entry point** for "what the eigenmode solver computes." This chapter is an **output-product leaf feature column** (a composition root): inputs = config (the eigenmode problem); output = the physical product (the per-mode `(f, Q)` table); body = the composition of the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction over the [`eigenmode`](./eigenmode.L4.md) driver column's converged eigenpair family. It does **not** introduce a new combinator; it wires existing L4 vocabulary into the user-facing output product and links DOWN to each composed piece.

The eigenfrequency / Q-factor table is the **output-product half** of the eigenmode composition root — the post-processing stage that the [`eigenmode.L4`](./eigenmode.L4.md) driver column flags as its stage (3) and defers to a forward mine. That mine landed: [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is the eigenmode **per-mode scalar-ratio reduction** verb — the reduce-to-scalar-table member of the L4 algebra-of-folds. Unlike the [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md) output products (which both reduce a solution family to a symmetric-Gram matrix via [`gram_reduce`](../L4/gram_reduce.md)), this product is a **rank-1 per-mode table**, not a rank-2 family-PAIR grid — the c074 D6 closed-negative non-subsume (the eigenmode Q-factor is a per-mode scalar ratio, the wrong rank for a Gram reduction). This column is the feature-surface view of that distinct reduction.

## The composition

At L4 the eigenfrequency / Q-factor product is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config (the eigenmode problem); output = the (f, Q) table (the physical product)
    eigenfrequency_qfactor :: EigenmodeConfig -> [(Scalar, Scalar)]
    eigenfrequency_qfactor cfg =
      let eigs  = eigenmode_eigenpairs cfg                  -- (1) the eigenmode driver column: assemble the K/C/M
                                                            --     pencil once, ONE opaque eigsolve → converged [(λᵢ, Eᵢ)]
                                                            --     ── feature/eigenmode.L4 (the producing driver column)
          ptype = problem_type cfg                          -- the eigenvalue→ω un-transform selector (the variant axis)
          kappa = loss_rate cfg                             -- the per-mode loss-rate closure κₘ = ½R|Iₘⱼ|²/Eₘ
      in  eigenfreq_qfactor_reduce ptype kappa eigs         -- (2) per mode: (fₘ = Re ωₘ, Qₘ = ωₘ/κₘ)  ── L4/eigenfreq_qfactor_reduce

Two composed stages — the driver column produces the family, the reduction maps it to the table:

1. **The eigenmode driver column produces the converged eigenpair family** — [`eigenmode.L4`](./eigenmode.L4.md) (**seed**). The upstream composition root assembles the generalized-eigenproblem operator pencil `(K, C, M)` once ([`fe_assemble`](../L4/fe_assemble.md) ×3) and hands it to the opaque [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap **once**, collecting the converged eigenpair set `[(λᵢ, Eᵢ)]`. This output-product column **consumes** that family; it does not re-derive the solve (the driver column owns the solve, this column owns the reduction — the output-product / driver split the FEATURE-SURFACE SPINE encodes). L0: the `EigenSolver::Solve` body assembles the pencil (`eigensolver.cpp:40-42`) and runs the single `eigen->Solve()` (`:367`); the readout loop `for (int i = 0; i < num_conv; i++)` (`:424`) iterates the already-converged family.

2. **The per-mode scalar-ratio reduction** — [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) (**rough-in (test-coverage-bounded)**). The L4 per-mode scalar-ratio reduction combinator `eigenfreq_qfactor_reduce ptype κ eigs` maps each converged eigenpair to its `(f, Q)` table row: the eigenfrequency `fₘ = Re ωₘ` is the problem-type un-transform of the eigenvalue (`ω = √μ` for the linear EVP `μ = -λ² = ω²`; `ω = λ/i` for the quadratic EVP `λ = iω`), and the quality factor `Qₘ = ωₘ/κₘ` is the energy/loss ratio (`κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ`, the resistive-lumped-port participation; `κ = 0 ⇒ Q = ∞` lossless-mode guard). Both folded per-mode scalar maps are now **firm L1**: the eigenvalue un-transform is firm L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), the κ-participation half is firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077). The reduction is a pure per-mode `map`-then-collect over the eigenpair family — **no inter-mode state, no `Solve` effect** (the eigenmode driver's readout loop is explicitly NOT a solve-iteration, [`solve_family`](../L4/solve_family.md):146). The **problem-type** un-transform (`√μ` vs `λ/i`) is the load-bearing variant axis, absorbed into the reduction's `untransform` dispatch. L0: the eigenvalue→ω un-transform `eigensolver.cpp:430-439`, the Q-factor body (`κₘ = ½R|I|²/E`, `Qₘ = ωₘ/κₘ`, the `κ=0 ⇒ Q=∞` guard) `postoperator.cpp:1188-1203`.

The mode-field recovery (`Eᵢ`, the magnetic field `B = -1/(iω)∇×E`) is the eigenmode driver column's separate stage-3 field readout (`eigensolver.cpp:443-455`), NOT part of this `(f, Q)` scalar reduction — this output product is the eigenfrequency + Q-factor scalar table specifically.

## Inputs / outputs (the feature surface)

- **Input — config (the eigenmode problem).** `EigenmodeConfig`: the problem-type selector (`linear-EVP | quadratic-EVP | nonlinear-EVP` → the eigenvalue→ω un-transform), the requested mode count (→ how many table rows), and the resistive-lumped-port boundary data (`R`, the port currents → the loss-rate κ closure), all inherited from the producing driver column. All `readonly` construction-stratum inputs. L0 home: `iodata.solver.eigenmode.{n, ...}` (`eigensolver.cpp:32-46`), the lumped-port resistances `data.R` (`postoperator.cpp:1192`).
- **Output — the physical product.** The per-mode `(f, Q)` table — one row per converged mode, each carrying the eigenfrequency `fₘ = Re ωₘ` and the quality factor `Qₘ = ωₘ/κₘ`. This is what the user runs the eigenmode solver to compute. L0 home: the per-mode `omega` un-transformed at `eigensolver.cpp:430-439`, the `quality_factor` at `postoperator.cpp:1201-1203`, recorded by `post_op.MeasureAndPrintAll(...)` (`eigensolver.cpp:458`).

## Why this is a distinct output-product column (rank-1, not Gram)

The eigenfrequency / Q-factor product is the **rank-1 sibling** of the capacitance / inductance output products: where those reduce a solution family to a symmetric-Gram **matrix** (a rank-2 family-PAIR grid via [`gram_reduce`](../L4/gram_reduce.md)), this product reduces the eigenpair family to a per-mode scalar **table** (rank-1, one `(f, Q)` row per mode).

- The upstream family is supplied whole by the [`eigenmode.L4`](./eigenmode.L4.md) driver column — no re-derivation, just consumption of the converged eigenpair set.
- The reduction is [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md), a **per-mode scalar-ratio map** — there is no `symmetric_from_upper`, no family-PAIR `xⱼᵀ K xᵢ` bilinear (the load-bearing distinction from `gram_reduce`; the c074 D6 closed-negative non-subsume, OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess`).
- The reduction folds two scalar projections per mode: the eigenvalue un-transform (`f = Re ω`) and the energy/loss ratio (`Q = ω/κ`), with the lossless `κ=0 ⇒ Q=∞` total handled in the scalar map.

The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The column is `seed` (not promoted past it) because [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `rough-in (test-coverage-bounded)`. Both of its folded per-mode primitives are now firm L1 — the κ-participation-ratio half is firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half is firm L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), so the verb's structure-side gate-(a) is fully discharged. The SOLE remaining gate is **(b)** the eigenpair→`(f, Q)` **assembly test**: the existing postprocess test asserts reduction-OUTPUT invariance over the measurement cache rather than the eigenpair→`(f, Q)` assembly map itself, so the assembly-level laws are still test-unconfirmed (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`; the assembly test is integration-level under the eigenmode `Solve(mesh)` driver with no `test/unit/` home, hence out of write-scope). A feature column may promote past `seed` only once ALL its composed constituents are firm; the verb stays `rough-in (test-coverage-bounded)` on gate-(b) alone, so the column stays `seed`.

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column | [`eigenmode.L4`](./eigenmode.L4.md) (driver feature column) | seed | `eigensolver.cpp:32-477` |
| per-mode scalar-ratio reduction | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) | rough-in (test-coverage-bounded) | `eigensolver.cpp:424-439`, `postoperator.cpp:1171-1203`, `test/unit/test-postoperator.cpp:216,259,160-188` (reduction-output cache round-trip: mode_port_kappa, participation_ratio) |
| eigenfrequency un-transform (folded) | [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `eigensolver.cpp:430-439` |
| Q-factor κ participation (folded) | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) §Semantics | rough-in | `postoperator.cpp:1188-1203` |

## Status

`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. The verb is `rough-in (test-coverage-bounded)` (cycle-079 lowering-verifier audit; gate-(a) discharged cycle-080). The column stays `seed` (does not promote) because the verb is still not `firm` — but its structure-side gate is now fully discharged: BOTH folded per-mode primitives are firm L1, the κ-participation-ratio half via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080). The SOLE remaining gate is **(b)** the eigenpair→`(f, Q)` **assembly test** (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`): the existing postprocess test asserts reduction-OUTPUT invariance over the measurement cache rather than the eigenpair→`(f, Q)` assembly map itself, so the assembly-level laws are still test-unconfirmed; the assembly test is integration-level under the eigenmode `Solve(mesh)` driver with no `test/unit/` home, hence out of write-scope (a lowering-verifier law-confidence pass on the verb is the in-scope promotion route). A feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` this dispatch, plus the constituent down-links.

The verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) was raised to `rough-in
(test-coverage-bounded)` (cycle-079 lowering-verifier audit: the PostOperator `[idempotent]`
postprocess test `test/unit/test-postoperator.cpp` CHECK-asserts the κ loss-rate `mode_port_kappa`
and the participation-ratio output fields as round-trip-invariant L0-equivalent semantics). The
column nonetheless stays `seed`: the verb is still not `firm`, gated SOLELY on gate-(b) (the
eigenpair→`(f,Q)` assembly test asserts the eigenpair→`(f,Q)` assembly map, distinct from the
existing reduction-OUTPUT invariance test; out of write-scope, a lowering-verifier law-confidence
pass is the in-scope route). Its structure-side gate-(a) is fully discharged — both folded per-mode
primitives are firm L1, the eigenvalue un-transform via
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ-participation half
via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077). A feature column may promote
past `seed` only once ALL its composed constituents are firm.
