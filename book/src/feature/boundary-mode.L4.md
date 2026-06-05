---
kind: feature-surface
feature: boundary-mode
level: L4
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L4/fe_assemble
      kind: composes
    - target: L4/eigsolve
      kind: composes
    - target: palace/drivers/boundarymodesolver.cpp:201-341
      kind: cites-evidence
    - target: palace/main.cpp:276-278
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: boundary_mode :: BoundaryModeConfig -> BoundaryModeResult (the IoData surface)
  reference:
    - feature/eigenmode.L4
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

Both composed solve-side combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**. Under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers), the firm solve corner is not sufficient here: this column stays `seed` on its **own-readout gate** — its directly-owned stage-(3) readout reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). The gate is a directly-owned constituent (the column's own readout reduction), NOT a sibling-column reference; authoring a firm waveguide-mode reduction is the promotion route.

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

`seed` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. The solve corner is firm — stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble, stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (with NO `solve_family` map and NO `fold_solve` state-march, the minimal solve shape eigenmode established), stage (0) is the distinguishing 2D-submesh preface — but this column **stays `seed`** on an **own-readout gate**: its directly-owned stage-(3) readout (a pure per-mode `map`) reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). This is a directly-owned constituent gate (the column's own readout reduction), NOT a sibling-column reference — so unlike its eigenmode sibling (which promotes because its reduction is owned by a *separate* `eigenfrequency-qfactor` cross-linked column), boundary-mode's readout reduction is its own unhomed constituent; authoring a firm waveguide-mode reduction is the promotion route. This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk, plus the firm constituent down-links.
