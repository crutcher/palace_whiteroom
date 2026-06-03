---
agent: layer-intro-author
invoked_at: 2026-06-03T16:01:06Z
scope: boundary-mode driver-leaf feature column (6th driver; status seed) — feature/boundary-mode.{L4,L1,L0}.md + driver-leaf.md own-bullet
status: pending
integrated_at: 2026-06-03T160000Z
integration_commit: dcfb41e
integration_notes: |
  Applied cycle-078 (batch-24 position 3/3, THIRD/FINAL). The 6th driver-leaf feature column
  boundary-mode (driver cohort 5->6, status seed, alpha-FIRST in the driver-leaf grouping) at
  L4/L1/L0 -- the composition root for BoundaryModeSolver (6th ProblemType branch); a 2D-submesh-
  extraction preface + the SAME opaque-library black-box eigsolve corner as eigenmode (2nd clean
  witness). Added its alpha-FIRST bullet to feature/driver-leaf.md ("5 drivers"->"6 drivers");
  its index/SUMMARY rows were added by D1 (cohort owner) -- dangling-link risk CLOSED at rebuild
  (this report created the 3 files D1's rows point at). Settles boundarymode-is-sixth-problemtype-
  branch by-landing. NO firm-count change (seed column). cargo make book exit 0, linkcheck2 clean,
  zero build-repair. Build-relevant: yes.
---

# CYCLE: boundary-mode driver-leaf feature column

## Summary

Authors the NEW **boundary-mode** driver-leaf feature column (the 6th driver column, alpha-FIRST in the driver-leaf grouping), as 3 new composition-root chapters (`book/src/feature/boundary-mode.{L4,L1,L0}.md`), all `status: seed`. The column is the composition root for `BoundaryModeSolver` (the 6th `ProblemType` dispatch branch, `palace/main.cpp:276-278`): inputs = config (`iodata.solver.boundary_mode` 2D waveguide-mode params); output = the converged propagation modes; body = a 2D-submesh-extraction preface + the **same opaque-library black-box eigen-iteration corner as the [`eigenmode`](book/src/feature/eigenmode.L4.md) driver** (the `ModeEigenSolver` GEP is opaque-library-owned; cross-referenced to `eigenmode`). The distinguishing shape vs the 3D-domain eigenmode driver is the boundary-extracted 2D submesh (`ExtractBoundary2DSubmesh`: `CreateFromBoundary` → 3D→2D projection).

The two solve-side constituents ([`fe_assemble`](book/src/L4/fe_assemble.md), [`eigsolve`](book/src/L4/eigsolve.md)) are **firm at both L4 and L1** (verified on-disk via each chapter's `## Status` line this dispatch). The column stays `seed` because the stage-(3) per-mode readout reduces into a user-facing waveguide-mode product that has NO dedicated output-product column yet (the forward-ref; sibling of the eigenmode→`eigenfrequency-qfactor` pairing that landed c075).

Also converts the line-13 "A 6th co-equal leaf driver column … is planned" prose in the `feature/driver-leaf.md` group-intro into the live **alpha-FIRST** `boundary-mode` bullet (my OWN bullet only).

**Deferred to D1 (cohort owner this cycle):** the `feature/index.md` matrix row + the `SUMMARY.md` `# Feature surfaces` 3-level block entry for `boundary-mode` — NOT touched here (parallel-blind-shared-index guard, c074/c075 precedent). D1 adds those rows.

## Proposed changes

### New file 1 — book/src/feature/boundary-mode.L4.md

Full-file content is the supporting doc `boundary-mode.L4.md` in this report directory.

```new:book/src/feature/boundary-mode.L4.md
---
kind: feature-surface
feature: boundary-mode
level: L4
status: seed
composes:
  - book/src/L4/fe_assemble.md (firm — assemble the 2D-submesh GEP block operators A(ω,σ) / B: the assemble-fold combinator)
  - book/src/L4/eigsolve.md (firm — the opaque black-box eigen-solve cap: one library call, no Palace-authored loop — the SAME corner as the eigenmode driver)
l0_ground_truth:
  - palace/drivers/boundarymodesolver.cpp:201-341 (BoundaryModeSolver::Solve)
  - palace/main.cpp:276-278 (ProblemType::BOUNDARYMODE dispatch)
---

# boundary-mode — L4 composition-root

The **boundary-mode (2D waveguide-mode analysis) simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the `BoundaryModeSolver` driver (the 6th `ProblemType` dispatch branch, `palace/main.cpp:276-278`). This chapter is a **composition root** (a **leaf feature column** in the FEATURE-SURFACE SPINE — a per-driver surface whose stage constituents are *vocabulary ops*, not other feature columns): it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → converged propagation modes), and links DOWN to each composed piece.

Boundary-mode is the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** — it shares the [`eigenmode`](./eigenmode.L4.md) driver's solve corner (the opaque [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap; the eigen-iteration is opaque-library-owned, SLEPc/ARPACK), but over a **boundary-extracted 2D submesh** rather than the 3D problem domain. That submesh-extraction preface is the distinguishing shape: where the 3D-domain eigenmode driver assembles its pencil directly on the problem mesh, boundary-mode first extracts a 2D cross-section from the 3D boundary faces (`CreateFromBoundary` → 3D→2D projection) and assembles the generalized eigenproblem on *that* submesh. The solve corner itself is the same minimal shape: assemble a block operator pencil, hand it to the opaque eigen-solver **once**, read out the converged propagation modes.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the converged propagation-mode set (the physical product)
    boundary_mode :: BoundaryModeConfig -> BoundaryModeResult
    boundary_mode cfg =
      let mesh2d = extract_boundary_2d_submesh (parent_mesh cfg) (surface_attrs cfg)  -- (0) 3D-boundary → 2D submesh (the distinguishing preface)
          space  = mode_space mesh2d cfg                          -- the combined ND ⊕ H1 block FE space on the 2D submesh (readonly construction stratum)
          opA    = fe_assemble space [ block_system (omega cfg) (sigma cfg) ]   -- (1a) assemble the ω/σ-dependent block system A ── L4/fe_assemble (firm)
          opB    = fe_assemble space [ mass_block ]                            -- (1b) assemble the generalized RHS block B ── L4/fe_assemble (firm)
          pencil = eig_pencil opA opB (sigma cfg) (n_modes cfg)   -- the (A, B) GEP pencil + shift-invert σ = -kn_target²
          eigs   = eigsolve pencil (initial_space cfg)            -- (2) ONE opaque black-box eigen-solve ── L4/eigsolve (firm) — SAME corner as eigenmode
      in  map (readout cfg (omega cfg)) eigs                      -- (3) per-mode readout map → kn, n_eff, (Et, En, Bz)

Four composed stages; stages (1)–(3) each a link DOWN to firm L4 vocabulary, stage (0) the boundary-extraction preface:

0. **Extract the 2D submesh from the 3D boundary (the distinguishing preface).** When the config names boundary attributes, the parent 3D mesh's named boundary faces are extracted into a self-contained 2D submesh (`CreateFromBoundary` → attribute remap → internal-boundary-edge add → 3D→2D coordinate projection), and the material tensors + path coordinates are rotated into the submesh's local tangent frame. This is the structural feature that distinguishes boundary-mode from [`eigenmode`](./eigenmode.L4.md): the GEP is posed on a *boundary-extracted 2D cross-section*, not the 3D problem domain. When the config supplies a 2D mesh directly (empty attribute list), this stage is the identity. L0: `ExtractBoundary2DSubmesh` (`palace/drivers/boundarymodesolver.cpp:42-55`), called from `Preprocess` at `:141`; the direct-2D bypass at `:87-92`.

1. **Assemble the GEP block operator pencil** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The combined block FE space is `ND ⊕ H1` (the transverse Nédélec H(curl) field `Et` ⊕ the longitudinal H1 field `En`); the assemble-fold builds the ω/σ-dependent block system `A(ω,σ)` and the generalized RHS block `B`. The `space` (the combined ND ⊕ H1 block space on the 2D submesh) is the `readonly` construction stratum captured once. L0: `BoundaryModeOperator mode_op(iodata, mesh, mat_op)` (`palace/drivers/boundarymodesolver.cpp:216`) builds the operator family from config + the 2D mesh + material operator (`:214`); the ω/σ-dependent block assembly is `ModeEigenSolver::AssembleFrequencyDependent` (`palace/models/modeeigensolver.cpp:395`), and the pencil is captured via `eigen->SetOperators(*opB, *opA, ScaleType::NONE)` (`:470`).

2. **One opaque black-box eigen-solve** — [`eigsolve`](../L4/eigsolve.md) (**firm**). This is the **black-box-kernel constituent**, and it is the **SAME corner as the [`eigenmode`](./eigenmode.L4.md) driver** (per the directive `project_blackbox_vs_accelerated_kernels`: an opaque/special op with a clean surface and non-local iterative behaviour RISES to L4 as an opaque-surface primitive). The `ModeEigenSolver`'s GEP eigen-iteration lives inside the opaque library (SLEPc `EPSSolve` / ARPACK `naupd` RCI) — Palace authors **no** eigen-iteration loop, so the cap names the iteration by role and marks the obstruction rather than rendering a Palace-authored loop (see [`L4/eigsolve`](../L4/eigsolve.md) §Status — the opaque-library constraint). The cap is called **exactly once** with a shift-invert target `σ = -kn_target²`: the whole `(A, B)` pencil is handed to the library, which returns the converged-mode count. There is no `solve_family` map here (no operator/RHS family) and no `fold_solve` state-march (no value-threaded outer iteration the calculus owns) — the single black-box call IS the entire solve, exactly as in eigenmode. L0: `auto result = eig.Solve(omega, sigma)` (`palace/drivers/boundarymodesolver.cpp:268`), whose body is the single `int num_conv = eigen->Solve()` (`palace/models/modeeigensolver.cpp:477`).

3. **Per-mode readout map → the physical product** — a pure `map` over the already-converged eigenpair set, recovering each mode's physical observables: the propagation constant `kn` (from the eigenvalue, via the shift-invert un-transform), the effective index `n_eff = kn / ω`, the transverse + longitudinal mode fields `(Et, En)` (the VD back-transform of the eigenvector), and the longitudinal magnetic field `Bz = curl(Et)/(iω)` (for propagating modes). This is the boundary-mode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (the same non-membership the [`eigenmode`](./eigenmode.L4.md) driver records). L0: the propagation-constant report loop `for (int i = 0; i < num_conv; i++)` (`palace/drivers/boundarymodesolver.cpp:273`), the per-mode readout loop `for (int i = 0; i < n_print; i++)` (`:292`), the VD back-transform `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`), the power-normalization (`:304`), the `Bz` formation for propagating modes (`:316`), and `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`).

## Inputs / outputs (the feature surface)

- **Input — config.** `BoundaryModeConfig` (the `iodata.solver.boundary_mode` surface, `palace/utils/configfile.hpp:856-890`): the operating frequency `freq` [GHz] (→ `ω`), the requested mode count `n`, the modes-to-write count `n_post`, the target effective index `target` (→ the shift-invert spectral transform; zero ⇒ auto-computed from material light speed), the eigenvalue-solver tolerance `tol`, the subspace dimension `max_size`, the eigensolver backend `type`, and the boundary `attributes` selecting the 3D faces to extract (empty ⇒ direct-2D mesh). Plus the mesh + the linear-solver config the inner `ksp_solve` consumes. All `readonly` construction-stratum inputs. L0 home: `const auto &bm = iodata.solver.boundary_mode` (`palace/drivers/boundarymodesolver.cpp:203`).
- **Output — the physical product.** `BoundaryModeResult` — the set of converged propagation modes, each carrying its propagation constant `kn`, effective index `n_eff = kn/ω`, transverse + longitudinal mode fields `(Et, En)`, and (for propagating modes) `Bz`. This is what the user ran the boundary-mode solver to compute (waveguide / wave-port mode characterization). L0 home: the per-mode `kn` / `(et, en)` measured by `post_op.MeasureAndPrintAll(...)` (`palace/drivers/boundarymodesolver.cpp:314`); the driver returns `{indicator, mode_op.GetNDSpace().GlobalTrueVSize() + mode_op.GetH1Space().GlobalTrueVSize()}` (`:339-340`).

## Why this composes (the eigenmode corner + a 2D-submesh preface)

The boundary-mode feature composes the **same minimal solve shape as [`eigenmode`](./eigenmode.L4.md)** — a single opaque black-box eigen-iteration flanked by an assemble-fold and a pure readout-map, with **no outer solve-loop the calculus has to own** — prefixed by the **2D-submesh extraction** that distinguishes it:

- The preface (stage 0) extracts a 2D cross-section from the 3D boundary; this is structure the eigenmode driver does not have, and is the reason boundary-mode is a *co-equal* leaf driver column rather than a variant of eigenmode.
- The assemble (stage 1) is the [`fe_assemble`](../L4/fe_assemble.md) fold building the `(A, B)` GEP block pencil on the combined ND ⊕ H1 submesh space.
- The solve (stage 2) is **one** [`eigsolve`](../L4/eigsolve.md) black-box call — no `solve_family` map (no RHS family), no `fold_solve` (no state-threaded march) — the identical solve corner to eigenmode.
- The readout (stage 3) is a pure `map` over the converged modes.

Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**. As with eigenmode, the solve-side constituents being firm means the only thing keeping this column at `seed` is the readout stage's reduction into the user-facing waveguide-mode product (whose dedicated output-product reduction is not yet a feature column).

## Variant axes

Two axes shape the boundary-mode composition; both are absorbed into the preface / pencil-construction / cap, not into the composition shape:

1. **mesh-source** (`3D-boundary-extracted | direct-2D`) — selects whether stage (0) runs the `CreateFromBoundary` 3D→2D extraction or is the identity. `3D-boundary-extracted` (`attributes ≠ ∅`, the submesh is cut from the named 3D boundary faces); `direct-2D` (`attributes = ∅`, the supplied mesh is already the solve mesh). Absorbed into `extract_boundary_2d_submesh`. L0: the branch at `palace/drivers/boundarymodesolver.cpp:87-92` (direct-2D bypass) vs. `:141` (extraction).
2. **shift-target** (`auto | target-n_eff`) — selects the shift-invert center the eigen-iteration drives toward. `target-n_eff` (`bm.target > 0`, `kn_target = target · ω`, `WhichType::LARGEST_MAGNITUDE`); `auto` (`bm.target = 0`, `kn_target` from the material max light speed, `WhichType::LARGEST_REAL`). Absorbed into `eig_pencil (sigma cfg)` (`σ = -kn_target²`) + the [`eigsolve`](../L4/eigsolve.md) cap's spectral-transform axis; not part of the composition shape. L0: the `kn_target` branch at `palace/drivers/boundarymodesolver.cpp:267` + the `which_eig` selection (`:232-233`).

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| extract 2D submesh from 3D boundary | *(driver-local preface; no standalone combinator yet)* | (preface) | `boundarymodesolver.cpp:42-55, 141` |
| assemble (A, B) GEP block pencil | [`fe_assemble`](../L4/fe_assemble.md) | firm | `boundarymodesolver.cpp:216`; `modeeigensolver.cpp:395, 470` |
| opaque eigen-solve (once; SAME corner as eigenmode) | [`eigsolve`](../L4/eigsolve.md) | firm | `boundarymodesolver.cpp:268`; `modeeigensolver.cpp:477` |
| per-mode readout (kn, n_eff, Et, En, Bz) | *(waveguide-mode product reduction; forward-ref — no output-product column yet)* | (forward-ref) | `boundarymodesolver.cpp:273-334` |

## Status

`seed` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). Both composed combinators are firm: stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble, stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call — with NO `solve_family` map and NO `fold_solve` state-march (the minimal solve shape eigenmode established). Stage (0) is the distinguishing 2D-submesh preface; stage (3) is a pure per-mode readout `map` whose reduction into the user-facing waveguide-mode product is a forward-ref (no dedicated output-product column yet) — the one reason this column stays `seed`. This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm constituent down-links.
```

### New file 2 — book/src/feature/boundary-mode.L1.md

```new:book/src/feature/boundary-mode.L1.md
---
kind: feature-surface
feature: boundary-mode
level: L1
status: seed
composes:
  - book/src/L1/fe_assemble.md (firm — assemble the 2D-submesh GEP block operators)
  - book/src/L1/eigsolve.md (firm — the eigensolver-as-operator collapse: one opaque solve → EigResult — the SAME corner as eigenmode)
l0_ground_truth:
  - palace/drivers/boundarymodesolver.cpp:201-341 (BoundaryModeSolver::Solve)
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

`seed` — the L1 pure-function composition root for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [boundary-mode.L4](./boundary-mode.L4.md) composition root and the L1 sibling of the [eigenmode.L1](./eigenmode.L1.md) driver (the SAME opaque eigensolver-as-operator solve corner, distinguished by the 2D-submesh extraction preface). BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)); the only non-firm element is the stage-3 readout's forward-ref to a not-yet-authored waveguide-mode output-product reduction — which is why the column stays `seed`. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, e0)` destination write, the `bz.Real() *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm L1 constituent down-links.
```

### New file 3 — book/src/feature/boundary-mode.L0.md

```new:book/src/feature/boundary-mode.L0.md
---
kind: feature-surface
feature: boundary-mode
level: L0
status: seed
l0_ground_truth:
  - palace/drivers/boundarymodesolver.cpp:201-341 (BoundaryModeSolver::Solve)
  - palace/drivers/boundarymodesolver.hpp:15-28 (class declaration)
  - palace/main.cpp:276-278 (ProblemType::BOUNDARYMODE dispatch)
lifts_to:
  - book/src/feature/boundary-mode.L1.md (the L1 pure-function composition root)
---

# boundary-mode — L0 ground-truth surface

The **boundary-mode (2D waveguide-mode analysis) simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/boundarymodesolver.cpp` and its operator/eigensolver collaborators.

The driver is `BoundaryModeSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/boundarymodesolver.cpp:201-202`; the function body runs to the closing brace at `:341`). The class is `BoundaryModeSolver : public BaseSolver` with the `Preprocess(...) const override` (the 3D→2D extraction hook) and the `Solve(...) const override` (`palace/drivers/boundarymodesolver.hpp:15-28`; the ctor is `boundarymodesolver.cpp:78-82`). It is the **6th `ProblemType` dispatch branch**: `case ProblemType::BOUNDARYMODE: return std::make_unique<BoundaryModeSolver>(...)` (`palace/main.cpp:276-278`), routed through the same `switch` as the 5 simulation drivers — a co-equal leaf driver.

## The composition, in source

The driver extracts a 2D cross-section from the 3D boundary (in `Preprocess`), assembles the generalized-eigenproblem block operator pencil `(A, B)` on that submesh, hands it to the opaque `ModeEigenSolver` once, and reads out the converged propagation modes. Unlike the 3D-domain [eigenmode](./eigenmode.L0.md) driver, the GEP is posed on a *boundary-extracted 2D submesh*; like eigenmode, the solve is a single opaque eigen-iteration with **no value-threaded outer solve loop** — the only outer loops are the post-processing readouts. The source stages, in order:

0. **Extract the 2D submesh from the 3D boundary (the distinguishing preface).** `BoundaryModeSolver::Preprocess` (`palace/drivers/boundarymodesolver.cpp:84`) reads the config boundary attributes (`:87`); when non-empty it runs the full 3D-boundary → 2D-submesh pipeline `ExtractBoundary2DSubmesh` (`:42-55`: `mfem::SubMesh::CreateFromBoundary` `:46` → `ProjectSubmeshTo2D` 3D→2D coordinate projection `:50` → `RemapSubMeshAttributes` / `RemapSubMeshBdrAttributes` / `AddSubMeshInternalBoundaryElements` `:51-53`), called at `:141`, and rotates material tensors + path coordinates into the submesh's local tangent `SubmeshFrame` (`:29-34`). When the attribute list is empty the driver takes the direct-2D path `BaseSolver::Preprocess(...)` (`:87-92`). This is the L0 site the L1/L4 `extract_boundary_2d_submesh` preface lift — the structural feature distinguishing boundary-mode from eigenmode.

1. **Assemble the GEP block operator pencil.** `MaterialOperator mat_op(iodata, *mesh.back())` (`:214`) builds the material operator from config + the 2D mesh; `BoundaryModeOperator mode_op(iodata, mesh, mat_op)` (`:216`) builds the combined `ND ⊕ H1` block operator family (the transverse Nédélec H(curl) field `Et` ⊕ the longitudinal H1 field `En`); the combined DBC tdof list is assembled from the ND + H1 Dirichlet lists (`:217-225`). The ω/σ-dependent block system `A(ω,σ)` + the generalized RHS block `B` are assembled inside `ModeEigenSolver::AssembleFrequencyDependent(omega, sigma)` (`palace/models/modeeigensolver.cpp:395`, called from `Solve` at `:432`), and the pencil is captured into the opaque solver via `eigen->SetOperators(*opB, *opA, EigenvalueSolver::ScaleType::NONE)` (`:470`). This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift (the block-pencil assemble).

2. **Configure the eigensolver, set the shift target.** `const auto which_eig = (bm.target > 0.0) ? WhichType::LARGEST_MAGNITUDE : WhichType::LARGEST_REAL` (`:232-233`); `ModeEigenSolver eig(mode_op, dbc_tdof_list, num_modes, bm.max_size, bm.tol, which_eig, iodata.solver.linear, bm.type, ...)` (`:234`) constructs the opaque GEP eigen-solver over the block operator. The shift-invert center `kn_target` is computed — `kn_target = bm.target * omega` when a target effective index is given (`:251`), else auto-computed from the material max light speed `kn_target = omega / c_min * sqrt(1.1)` (`:260`) — and the shift is `const double sigma = -kn_target * kn_target` (`:267`). This is the L0 site the [`eigsolve`](../L1/eigsolve.md) operator-setup the L4 [`eigsolve`](../L4/eigsolve.md) cap names.

3. **One opaque eigen-solve.** `auto result = eig.Solve(omega, sigma)` (`:268`) runs the entire GEP eigen-iteration; its body sets the pencil and runs the single `int num_conv = eigen->Solve()` (`palace/models/modeeigensolver.cpp:477`) **inside the opaque library** (SLEPc `EPSSolve` / ARPACK `naupd` RCI), returning the converged-mode count (`result.num_converged`, `:269`). The mode-ordering permutation sorted by proximity to the shift target is built after the solve (`modeeigensolver.cpp:481-491`). **No Palace-authored loop surrounds the eigen-solve** — this is the same load-bearing fact as the [eigenmode](./eigenmode.L0.md) driver (the eigen-iteration is opaque-library-owned; the [`eigsolve`](../L4/eigsolve.md) black-box-kernel constituent). The converged propagation constants are reported in `for (int i = 0; i < num_conv; i++)` (`:273-278`).

4. **Per-mode readout map → the physical product.** `for (int i = 0; i < n_print; i++)` (`:292`, `n_print = min(num_conv, num_modes)`) iterates the converged modes — a pure post-processing readout (NOT a solve-iteration). Per mode: `eig.GetEigenvector(i, e0)` (`:297`) reads the raw eigenvector into the destination buffer (the in-place write the L1 form lifts); `const std::complex<double> kn = eig.GetPropagationConstant(i)` (`:299`); `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`) applies the VD back-transform to recover the physical transverse `et` + longitudinal `en` fields; the mode is power-normalized to `|P| = 1` via `mode_op.ComputePoyntingPower(...)` then `e0 *= 1/sqrt(|P|)` (`:304-307`); the backward + absolute errors are read (`:309-310`); `auto total_domain_energy = post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`) measures + records the per-mode observables; for propagating modes (`ModeEigenSolver::IsPropagating(kn)`, `:316`) the longitudinal magnetic field `Bz = curl(Et)/(iω)` is formed from `CurlOp.Mult(et.Real(), curl_etr)` / `CurlOp.Mult(et.Imag(), curl_eti)` then `bz.Real() *= 1/omega` / `bz.Imag() *= -1/omega` (`:317-333`, the in-place accumulations the L1 form lifts) and fed to the error estimator (`:333`). The readout loop closes at `:334`; `post_op.MeasureFinalize(indicator)` (`:337`) finalizes. This is the L0 site the L1/L4 per-mode readout map lifts — feeding the waveguide-mode **output product** (whose reduction has no dedicated output-product column yet; forward-ref).

The driver returns `{indicator, mode_op.GetNDSpace().GlobalTrueVSize() + mode_op.GetH1Space().GlobalTrueVSize()}` (`:339-340`) — the error indicator + the combined ND + H1 global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `const auto &bm = iodata.solver.boundary_mode` (`:203`), the `BoundaryModeSolverData` struct (`palace/utils/configfile.hpp:856-890`, parsed at `palace/utils/configfile.cpp:1390`): `freq` [GHz] → `omega` (`:206-207`), `n` (mode count, `:204`), `n_post`, `target` (effective-index shift), `tol`, `max_size`, `type` (eigensolver backend), `attributes` (the 3D faces to extract). Plus `mesh` and `iodata.solver.linear` (the inner `ksp_solve` config).
- **Output — the physical product.** The per-mode propagation constant `kn` (`eig.GetPropagationConstant(i)`, `:299`), effective index `n_eff = kn/omega` (`:276-277`), transverse + longitudinal mode fields `(et, en)`, and (propagating modes) `Bz`, measured by `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`). The reduction into the reported waveguide-mode product has no dedicated output-product column yet (forward-ref).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`boundary-mode.L1`](./boundary-mode.L1.md) (the `GetEigenvector(i, e0)` destination write → a value-returning `EigResult` field; the in-place `bz.Real() *= ...` accumulations → pure field-readout values; the `ExtractBoundary2DSubmesh` mutation pipeline → a pure submesh-from-boundary function) and the L4 combinator composition root [`boundary-mode.L4`](./boundary-mode.L4.md) (the block-pencil `SetOperators` assemble → the [`fe_assemble`](../L4/fe_assemble.md) fold; the single `eigen->Solve()` → the [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap, the SAME corner as eigenmode; the readout `for` → a pure `map`). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).

## Status

`seed` — the L0 ground-truth surface for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the 6th driver-leaf column and the L0 sibling of the [eigenmode.L0](./eigenmode.L0.md) driver (the SAME opaque-library black-box eigen-iteration corner, distinguished by the 2D-submesh extraction preface). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp` (+ its `ModeEigenSolver` / `BoundaryModeOperator` collaborators), confirmed on-disk this dispatch (the `BoundaryModeSolver::Solve` decl `:201-202`, the `Preprocess` extraction `:84-141` + `ExtractBoundary2DSubmesh` `:42-55`, the `BoundaryModeOperator` assemble `:216`, the `ModeEigenSolver eig(...)` setup `:234`, the shift `sigma` `:267`, the single `eig.Solve(omega, sigma)` `:268` whose body is the opaque `eigen->Solve()` `modeeigensolver.cpp:477`, the readout loops `:273` / `:292-334`, the `MeasureAndPrintAll` `:314`, the return `:339-340`; the dispatch `palace/main.cpp:276-278`). The load-bearing structural fact at L0: a single opaque `eigen->Solve()` with NO surrounding Palace-authored loop and NO per-source RHS family — the driver's only loops are the post-processing readouts (the same `solve_family`/`fold_solve` non-membership as eigenmode) — prefixed by the boundary-extraction 2D-submesh preface that distinguishes the driver. The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

### Edit — book/src/feature/driver-leaf.md (my OWN bullet: insert alpha-FIRST + de-stale line-13 prose)

Insert the `boundary-mode` bullet alpha-FIRST (before the `driven` bullet) and rewrite the line-13 "planned" sentence to reflect the landed column.

```edit:book/src/feature/driver-leaf.md
[old]:
The 5 drivers span the solve-shape corners the vocabulary spine has to cover:

- [`driven`](./driven.L4.md) — the **operator-VARYING** corner: a per-ω rebuild with `SetOperators` *inside* the loop, composing the [`frequency_sweep`](../L4/frequency_sweep.md) map. Levels: [L4](./driven.L4.md) · [L1](./driven.L1.md) · [L0](./driven.L0.md).
[new]:
The 6 drivers span the solve-shape corners the vocabulary spine has to cover:

- [`boundary-mode`](./boundary-mode.L4.md) — the **opaque-library black-box on a boundary-extracted 2D submesh** corner: the `ModeEigenSolver` GEP eigen-iteration (the SAME opaque corner as `eigenmode`), prefixed by a 3D-boundary → 2D-submesh extraction (the distinguishing shape). Levels: [L4](./boundary-mode.L4.md) · [L1](./boundary-mode.L1.md) · [L0](./boundary-mode.L0.md).
- [`driven`](./driven.L4.md) — the **operator-VARYING** corner: a per-ω rebuild with `SetOperators` *inside* the loop, composing the [`frequency_sweep`](../L4/frequency_sweep.md) map. Levels: [L4](./driven.L4.md) · [L1](./driven.L1.md) · [L0](./driven.L0.md).
```

```edit:book/src/feature/driver-leaf.md
[old]:
Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. A 6th co-equal leaf driver column — wave-port / boundary-mode (the 6th `ProblemType` dispatch branch) — is planned and lands here when its constituent vocabulary composes cleanly. All columns stay `seed` until every composed constituent is firm.
[new]:
Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. The `boundary-mode` column is the 6th co-equal leaf driver — the `BoundaryModeSolver` `ProblemType` dispatch branch (`palace/main.cpp:276-278`), routed through the same `switch` as the other 5; it composes the same opaque-library [`eigsolve`](../L4/eigsolve.md) corner as `eigenmode`, distinguished by its 3D-boundary → 2D-submesh extraction preface. All columns stay `seed` until every composed constituent is firm.
```

## Supporting evidence

- **L0 driver source, verified on-disk this dispatch** (palace-codemap `read_range` to localize, then `citecheck --anchor` + direct `sed` END-line reads against `reference/palace` — the codemap `read_range` showed a -1 drift on the `eigen->Solve()` line, re-anchored on-disk):
  - `BoundaryModeSolver::Solve` `palace/drivers/boundarymodesolver.cpp:201-341` (decl `:201-202`, body close `:341`).
  - `Preprocess` 3D→2D extraction hook `:84-141`; `ExtractBoundary2DSubmesh` helper `:42-55` (`SubmeshFrame` `:29-34`); direct-2D bypass `:87-92`.
  - `MaterialOperator mat_op` `:214`; `BoundaryModeOperator mode_op` `:216`; combined DBC list `:217-225`.
  - `ModeEigenSolver eig(...)` `:234`; `kn_target` branch `:251`/`:260`; shift `sigma = -kn_target²` `:267`.
  - `eig.Solve(omega, sigma)` `:268` → body `int num_conv = eigen->Solve()` `palace/models/modeeigensolver.cpp:477` (the opaque SLEPc/ARPACK call); `eigen->SetOperators(*opB, *opA, ...)` `:470`; `AssembleFrequencyDependent` `:395`; `ModeEigenSolver` class `palace/models/modeeigensolver.hpp:96-270`.
  - kn report loop `:273-278`; readout loop `:292-334`; `ApplyVDBackTransform` `:300`; power-norm `:304-307`; `MeasureAndPrintAll` `:314`; Bz block `:317-333`; `MeasureFinalize` `:337`; return `:339-340`.
  - dispatch `case ProblemType::BOUNDARYMODE` `palace/main.cpp:276-278`; class decl `palace/drivers/boundarymodesolver.hpp:15-28`; ctor `:78-82`.
  - config struct `BoundaryModeSolverData` `palace/utils/configfile.hpp:856-890` (parsed `palace/utils/configfile.cpp:1390`).
- **Constituent firmness, read from each chapter's on-disk `## Status` line this dispatch** (NOT trusting cycle record / index cells): `book/src/L4/eigsolve.md` = `firm`; `book/src/L1/eigsolve.md` = `firm` (cycle-022 route-(b)); `book/src/L4/fe_assemble.md` = `firm`; `book/src/L1/fe_assemble.md` = `firm`. All four composed constituents firm at both levels — so the only thing holding the column at `seed` is the stage-3 readout's forward-ref to a not-yet-authored waveguide-mode output-product column.
- **Slug absence confirmed**: `book/src/feature/boundary-mode.*` did not exist pre-dispatch (planner-confirmed; re-checked on disk).
- **Cross-reference to the sibling solve corner**: the [`eigenmode`](book/src/feature/eigenmode.L4.md) driver column (the SAME opaque `eigsolve` black-box corner; boundary-mode is the 2nd clean witness, distinguished by the 2D-submesh preface). Read `eigenmode.{L4,L1,L0}.md` + `driver-leaf.md` to match the column shape/conventions.

## Deferred to D1 (cohort owner) — NOT in this report's proposed changes

- **`feature/index.md` matrix row** for `boundary-mode` — DEFERRED to D1 (parallel-blind-shared-index guard, c074/c075 precedent). D1 adds the alpha-first driver-leaf matrix row (3 levels, high→low within-column).
- **`SUMMARY.md` `# Feature surfaces` block** — DEFERRED to D1. The new `boundary-mode` 3-level entry goes in the `Driver-leaf columns` grouping, alpha-FIRST (before the `driven` block, current lines 14-16). D1 inserts:
  ```
  - [boundary-mode — L4 composition-root](./feature/boundary-mode.L4.md)
  - [boundary-mode — L1 composition-root](./feature/boundary-mode.L1.md)
  - [boundary-mode — L0 ground-truth surface](./feature/boundary-mode.L0.md)
  ```
  (high→low within-column, the deliberate FEATURE-SURFACE exception; placed before the `driven` 3-level block.)

## Open questions / caveats

Appended to `scaffolding/open-questions.md` (cycle-078 D2 intake block):
- `boundary-mode-2d-submesh-extraction-preface-vocabulary-home` — stage (0) `ExtractBoundary2DSubmesh` is authored as a driver-local preface (no standalone L4/L1 combinator); promote to a real vocabulary op + an L1>L0 mutation-rotation theme only if a 2nd boundary-submesh-extraction consumer surfaces. Below the ≥2-consumer bar now.
- `boundary-mode-waveguide-output-product-column-needs-home` — the stage-(3) readout reduces into a user-facing waveguide-mode product (`kn` / `n_eff` / impedance) with no dedicated output-product feature column yet (the forward-ref keeping the column at `seed`). Sibling of the eigenmode→`eigenfrequency-qfactor` pairing (landed c075). Candidate slug `waveguide-mode` / `propagation-modes`.
- `modeeigensolver-readrange-minus-one-drift-witness` — palace-codemap `read_range` reported `eigen->Solve()` at `:476`; on-disk it is `:477` (a -1 drift; the standing `codemap-read-range-plus-one-drift-on-brace-boundary` friction extends to the eigensolver-models sources). All emitted citations re-anchored on-disk via `citecheck --anchor` + direct END-line reads. Informational.

Caveat — record-definition obligation: the signatures name `BoundaryModeConfig` / `BoundaryModeResult` / `EigResult`. `BoundaryModeConfig` is the feature-surface naming for the L0 `BoundaryModeSolverData` struct (defined in-line in each chapter's Inputs section + cited to `configfile.hpp:856-890`); it is single-consumer (this column) so it does not yet cross the ≥2-consumer bar for a `concepts/` record page — left as an in-chapter definition. `EigResult` is the shared eigensolver record already defined at [`L1/eigsolve`](book/src/L1/eigsolve.md) (boundary-mode reuses it via the cross-referenced `eigsolve` constituent, not a new definition). No `record-<name>-needs-definition-home` flag raised — the records have homes (in-chapter / the constituent's chapter).
