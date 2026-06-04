---
kind: feature-surface
feature: boundary-mode
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L1/fe_assemble
      kind: composes
    - target: L1/eigsolve
      kind: composes
    - target: palace/drivers/boundarymodesolver.cpp:201-341
      kind: cites-evidence
  reference:
    - feature/eigenmode.L1
---

# boundary-mode — L1 composition-root

The **boundary-mode (2D waveguide-mode analysis) simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface** (a **leaf feature column**): the same composition root as the [L4 chapter](./boundary-mode.L4.md), but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the boundary-mode feature is a pure function `config → propagation-mode result` built from two firm L1 operators plus a 2D-submesh-extraction preface and a pure readout, with the **mutation already lifted** (the L0 in-place `eig.GetEigenvector(i, e0)` destination-buffer write and the `bz.Real() *= ...` accumulations are lifted to value-returning forms per the L1>L0 mutation rotation; [`L1/eigsolve`](../L1/eigsolve.md) drops the `GetEigenvector(i, x)` out-parameter write and structures the converged-count + per-pair extraction into a single `EigResult` record). The solve corner is the **same as the [`eigenmode`](./eigenmode.L1.md) driver** — a single opaque eigensolver-as-operator application — distinguished by the boundary-extracted 2D submesh.

## The composition

    -- inputs = config; output = the converged propagation-mode set (the physical product)
    boundary_mode :: BoundaryModeConfig -> BoundaryModeResult
    boundary_mode cfg =
      let mesh2d = extract_boundary_2d_submesh (parent_mesh cfg) (surface_attrs cfg)  -- (0) 3D-boundary → 2D submesh (the distinguishing preface)
          space  = mode_space mesh2d cfg                            -- the combined ND ⊕ H1 block FE space on the 2D submesh
          opA    = fe_assemble space [ block_system (omega cfg) (sigma cfg) ]   -- (1a) assemble the ω/σ-dependent block system A
          opB    = fe_assemble space [ mass_block ]                            -- (1b) assemble the generalized RHS block B
          res    = eigsolve (eig_solver opA opB (control cfg)) (control cfg)    -- (2) one opaque eigensolver-as-operator → EigResult (SAME corner as eigenmode)
      in  [ readout cfg (omega cfg) (res.eigenvalues ! i) (res.eigenvectors ! i)  -- (3) per-mode pure readout → kn, n_eff, (Et, En, Bz)
          | i <- [0 .. res.converged - 1] ]

0. **Extract the 2D submesh from the 3D boundary (the distinguishing preface).** A pure function from the parent 3D mesh + the named boundary attributes to a self-contained 2D submesh (`CreateFromBoundary` → attribute remap → internal-boundary-edge add → 3D→2D projection) carrying its own node coordinates, plus the local tangent frame used to rotate the material tensors. Identity when the config supplies a 2D mesh directly. This is the structural feature distinguishing boundary-mode from [`eigenmode`](./eigenmode.L1.md). L0: `ExtractBoundary2DSubmesh` (`palace/drivers/boundarymodesolver.cpp:42-55`), called from `Preprocess` at `:141`; direct-2D bypass `:87-92`.

1. **Assemble the GEP block operator pencil** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The combined block FE space is `ND ⊕ H1` (transverse Nédélec H(curl) `Et` ⊕ longitudinal H1 `En`); the L1 assemble fold builds the ω/σ-dependent block system `A(ω,σ)` and the generalized RHS block `B`. Pure: consumes the combined space + the (ω, σ)-parameterized term list, produces fresh block operators. L0: `BoundaryModeOperator mode_op(iodata, mesh, mat_op)` (`palace/drivers/boundarymodesolver.cpp:216`) over the material operator (`:214`); the ω/σ-dependent block assembly `ModeEigenSolver::AssembleFrequencyDependent` (`palace/models/modeeigensolver.cpp:395`); pencil capture `eigen->SetOperators(*opB, *opA, ScaleType::NONE)` (`:470`).

2. **One opaque eigensolver-as-operator** — [`eigsolve`](../L1/eigsolve.md) (**firm**), called once. The L1 form is the **eigensolver-as-operator collapse**: the opaque `EigenvalueSolver` value is treated as a single pure operator that consumes the configured `(A, B)` GEP pencil + control and returns an `EigResult` record (eigenvalues, eigenvectors, the `converged` count, the sum-typed termination `status`). The whole GEP eigen-iteration (RCI / shell-matrix orchestration) is *inside* the opaque solver value — transparent dispatch, not part of the L1 contract — and it is the **SAME corner as the [`eigenmode`](./eigenmode.L1.md) driver** (opaque-library-owned, SLEPc/ARPACK). There is **no RHS family and no value-threaded outer solve loop** at L1: a single operator application with shift-invert `σ = -kn_target²`, the L1 counterpart of the L4 single black-box call. L0: `auto result = eig.Solve(omega, sigma)` (`palace/drivers/boundarymodesolver.cpp:268`), body `int num_conv = eigen->Solve()` (`palace/models/modeeigensolver.cpp:477`).

3. **Per-mode pure readout** — a pure list comprehension over the `res.converged` converged eigenpairs, recovering each mode's physical observables from the `EigResult`: the propagation constant `kn` (the shift-invert un-transform of the eigenvalue), the effective index `n_eff = kn/ω`, the transverse + longitudinal mode fields `(Et, En)` (the VD back-transform of the eigenvector, power-normalized so `|P| = 1`), and the longitudinal magnetic field `Bz = curl(Et)/(iω)` for propagating modes. This is a pure post-processing map — no solve-iteration, exactly as in eigenmode. L0: the propagation-constant report loop `for (int i = 0; i < num_conv; i++)` (`palace/drivers/boundarymodesolver.cpp:273`), the readout loop `for (int i = 0; i < n_print; i++)` (`:292`), `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`), power-normalization (`:304`), `Bz` formation (`:316`), `post_op.MeasureAndPrintAll(...)` (`:314`).

## Inputs / outputs (the feature surface)

- **Input — config.** `BoundaryModeConfig` (the `iodata.solver.boundary_mode` surface): operating frequency `freq` → `ω`; requested mode count `n`; effective-index target `target` → the shift-invert spectral transform; tolerance `tol`; subspace dimension `max_size`; eigensolver backend `type`; boundary `attributes` → the 2D-submesh extraction; plus mesh + linear-solver config for the inner `ksp_solve`. All read-only.
- **Output — the physical product.** `BoundaryModeResult` — the set of converged propagation modes, each carrying `kn`, `n_eff`, `(Et, En)`, and (for propagating modes) `Bz`. The reduction into the reported waveguide-mode product is a forward-ref (no dedicated output-product column yet). L0: the per-mode `kn`/`(et, en)` measured by `post_op.MeasureAndPrintAll(...)` (`palace/drivers/boundarymodesolver.cpp:314`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): a 2D-submesh-extraction preface, two explicit per-operator pure functions ([`fe_assemble`](../L1/fe_assemble.md) ×2, [`eigsolve`](../L1/eigsolve.md) ×1) wired by a `let`, then a pure readout comprehension over `EigResult`. The single opaque solve is an operator application returning a record.
- **L4** ([`boundary-mode.L4`](./boundary-mode.L4.md)): the same constituents named as L4 combinators (the [`fe_assemble`](../L4/fe_assemble.md) assemble-fold, the [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap), the readout as a pure `map`. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The defining structural fact at both levels: **no `solve_family` map and no `fold_solve`** — boundary-mode composes a single opaque solve (the same eigenmode corner), not an outer-iteration combinator; the distinguishing structure is the 2D-submesh preface.

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| extract 2D submesh from 3D boundary | *(driver-local preface; no standalone op yet)* | (preface) | `boundarymodesolver.cpp:42-55, 141` |
| assemble (A, B) GEP block pencil | [`fe_assemble`](../L1/fe_assemble.md) | firm | `boundarymodesolver.cpp:216`; `modeeigensolver.cpp:395, 470` |
| opaque eigensolver-as-operator (once; SAME corner as eigenmode) | [`eigsolve`](../L1/eigsolve.md) | firm | `boundarymodesolver.cpp:268`; `modeeigensolver.cpp:477` |
| per-mode readout (kn, n_eff, Et, En, Bz) | *(waveguide-mode product reduction; forward-ref — no output-product column yet)* | (forward-ref) | `boundarymodesolver.cpp:273-334` |

## Status

`seed` — the L1 pure-function composition root for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [boundary-mode.L4](./boundary-mode.L4.md) composition root and the L1 sibling of the [eigenmode.L1](./eigenmode.L1.md) driver (the SAME opaque eigensolver-as-operator solve corner, distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)), but the column **stays `seed`** on an **own-readout gate** — its directly-owned stage-3 readout reduces into a not-yet-authored waveguide-mode output-product reduction (no firm home; the waveguide-mode product column is demand-gated). The gate is the column's own readout constituent, NOT a sibling-column reference — so authoring a firm waveguide-mode reduction is the promotion route. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, e0)` destination write, the `bz.Real() *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm L1 constituent down-links.
