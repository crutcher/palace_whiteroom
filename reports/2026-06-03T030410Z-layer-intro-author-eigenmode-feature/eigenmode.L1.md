---
kind: feature-surface
feature: eigenmode
level: L1
status: seed
composes:
  - book/src/L1/fe_assemble.md (firm — assemble the K/C/M operator pencil)
  - book/src/L1/eigsolve.md (firm — the eigensolver-as-operator collapse: one opaque solve → EigResult)
l0_ground_truth:
  - palace/drivers/eigensolver.cpp:32-477 (EigenSolver::Solve)
---

# eigenmode — L1 composition-root

The **eigenmode simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface** (a **leaf feature column**): the same composition root as the [L4 chapter](./eigenmode.L4.md), but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the eigenmode feature is a pure function `config → eigenmode result` built from two firm L1 operators plus a pure readout, with the **mutation already lifted** (the L0 in-place `eigen->GetEigenvector(i, E)` destination-buffer write and the `B *= ...` accumulations are lifted to value-returning forms per the L1>L0 mutation rotation; [`L1/eigsolve`](../L1/eigsolve.md) drops the `GetEigenvector(i, x)` out-parameter write and structures the converged-count + per-pair extraction into a single `EigResult` record).

## The composition

    -- inputs = config; output = the eigenfrequency / Q-factor / mode-field set (the physical product)
    eigenmode :: EigenmodeConfig -> EigenmodeResult
    eigenmode cfg =
      let space = nd_space cfg
          k     = fe_assemble space [ curl_curl (reluctivity cfg) ]    -- (1a) assemble K once
          c     = fe_assemble space [ conductivity_term cfg ]          -- (1b) assemble C once (may be empty → linear EVP)
          m     = fe_assemble space [ mass_term (permittivity cfg) ]   -- (1c) assemble M once
          res   = eigsolve (eig_solver k c m (control cfg)) (control cfg)   -- (2) one opaque eigensolver-as-operator → EigResult
      in  [ readout cfg (res.eigenvalues ! i) (res.eigenvectors ! i)   -- (3) per-mode pure readout → ω, Q, B
          | i <- [0 .. res.converged - 1] ]

1. **Assemble the operator pencil once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**), applied three times to build the generalized-eigenproblem matrices `K`, `C`, `M`. The L1 assemble fold `K = Σ_i A(space, termᵢ)` over each operator's term list. Pure: consumes the Nédélec space + term list, produces a fresh operator. The damping matrix `C` may be empty (the linear-EVP branch `K x = ω² M x`); a non-empty `C` is the quadratic EVP `(K + λC + λ²M)x = 0`. L0: `space_op.GetStiffnessMatrix<ComplexOperator>(DIAG_ONE)` / `GetDampingMatrix(DIAG_ZERO)` / `GetMassMatrix(DIAG_ZERO)` (`palace/drivers/eigensolver.cpp:40-42`).

2. **One opaque eigensolver-as-operator** — [`eigsolve`](../L1/eigsolve.md) (**firm**), called once. The L1 form is the **eigensolver-as-operator collapse**: `eigsolve :: (E: EigSolver[problem], control: EigControl) -> EigResult[N, K_max]` — the opaque `EigenvalueSolver` value is treated as a single pure operator that consumes the configured pencil + control and returns an `EigResult` record carrying `eigenvalues : Tensor[K, complex]`, `eigenvectors : Tensor[K, N, complex]`, the `converged` count, and the sum-typed `status` (the four termination modes, including the `0 < converged < requested` partial-success arm that has no `ksp_solve` analog). The whole eigen-iteration (RCI / shell-matrix / Newton orchestration) is *inside* the opaque `EigSolver[...]` value — transparent dispatch, not part of the L1 contract. There is **no RHS family and no value-threaded outer solve loop** at L1: this is a single operator application, the L1 counterpart of the L4 single black-box call. L0: `eigen->SetOperators(...)` (`eigensolver.cpp:172-196`), `int num_conv = eigen->Solve()` (`:367`), the per-pair `GetEigenvalue`/`GetEigenvector`/`GetError` extraction structured into `EigResult`.

3. **Per-mode pure readout** — a pure list comprehension over the `res.converged` converged eigenpairs, recovering each mode's physical observables from the `EigResult`: the eigenfrequency `ω` (the problem-type un-transform of the eigenvalue — `ω = √μ` for the linear EVP, `ω = λ/i` for the quadratic EVP), the quality factor `Q` (from the complex `ω`), the electric mode field `E = res.eigenvectors ! i` (phase-normalized), and the magnetic field `B = -1/(iω) ∇×E` (the curl of the electric eigenvector, scaled). This is a pure post-processing map — no solve-iteration. The eigenfrequency / Q reduction into the user-facing **output product** is a forward-ref to the `eigenfrequency-qfactor` output-product column (plain-text — not authored here); this stage records only that eigenmode feeds it the per-mode `(ω, E, B)`. L0: the readout loop `for (int i = 0; i < num_conv; i++)` (`eigensolver.cpp:424`), the eigenvalue → ω recovery (`:427-439`), `eigen->GetEigenvector(i, E)` (`:443`), the `B = -1/(iω)∇×E` field readout (`:445-455`), `post_op.MeasureAndPrintAll(...)` (`:458`).

## Inputs / outputs (the feature surface)

- **Input — config.** `EigenmodeConfig` (mesh + order → Nédélec H(curl) space; material coefficients → K/C/M weak-form terms; requested mode count + spectral target → the `EigControl`; linear-solver + divergence-free-projector config → the inner `ksp_solve` the eigensolver calls). All read-only.
- **Output — the physical product.** `EigenmodeResult` — the set of converged modes, each carrying its eigenfrequency `ω`, quality factor `Q`, and mode fields `(E, B)`. The eigenfrequency/Q reduction into the reported product is owned by the `eigenfrequency-qfactor` output-product column (forward-ref). L0: the per-mode `omega`/`E`/`B` measured by `post_op.MeasureAndPrintAll` (`eigensolver.cpp:458`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): two explicit per-operator pure functions ([`fe_assemble`](../L1/fe_assemble.md) ×3, [`eigsolve`](../L1/eigsolve.md) ×1) wired by a `let`, then a pure readout comprehension over `EigResult`. The single opaque solve is an operator application returning a record.
- **L4** ([`eigenmode.L4`](./eigenmode.L4.md)): the same two constituents named as L4 combinators (the [`fe_assemble`](../L4/fe_assemble.md) assemble-fold, the [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap), the readout as a pure `map`. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The defining structural fact at both levels: **no `solve_family` map and no `fold_solve`** — the eigenmode driver composes a single opaque solve, not an outer-iteration combinator (`book/src/L4/solve_family.md:146`).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K/C/M pencil once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `eigensolver.cpp:40-42` |
| opaque eigensolver-as-operator (once) | [`eigsolve`](../L1/eigsolve.md) | firm | `eigensolver.cpp:172-196, 367` |
| per-mode readout (ω, Q, B=-1/(iω)∇×E) | `eigenfrequency-qfactor` *(output-product column; forward-ref — not authored here)* | (forward-ref) | `eigensolver.cpp:424-458` |

## Status

`seed` — the L1 pure-function composition root for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenmode.L4](./eigenmode.L4.md) minimal composition root. BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)); the only non-firm element is the stage-3 readout's forward-ref to the not-yet-authored `eigenfrequency-qfactor` output-product column — which is why the column stays `seed`. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop (the `solve_family`/`fold_solve` non-membership at `book/src/L4/solve_family.md:146`). The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, E)` destination write, the `B *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `eigensolver.cpp:32-477` realizing the composition, plus the firm L1 constituent down-links.
