---
kind: feature-surface
feature: waveguide-mode
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: feature/boundary-mode.L1
      kind: composes
    - target: palace/drivers/boundarymodesolver.cpp:273-340
      kind: cites-evidence
  reference:
    - feature/boundary-mode.L1
---

# waveguide-mode — L1 composition-root (output product)

The **waveguide-mode table** output product, presented at L1 as a pure-function composition of L1 operations. This is the **pure-function feature surface** of the output-product sub-kind: the same composition root as the [L4 chapter](./waveguide-mode.L4.md), but expressed in L1 vocabulary (an explicit per-mode pure readout, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole product does this per-mode readout add up to?"

At L1 the waveguide-mode product is a pure function `config → mode table`: it consumes the converged eigenpair set (the `EigResult`) produced by the [`boundary-mode.L1`](./boundary-mode.L1.md) driver column, then maps each mode to its `{kn, n_eff, (Et, En, Bz)}` row (the **mutation already lifted** — the L0 in-place `eig.GetEigenvector(i, e0)` destination write, the `e0 *= 1/√|P|` normalization, and the `bz.Real() *= 1/ω` accumulations are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config (boundary attributes + frequency); output = the waveguide-mode table (the physical product)
    waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable
    waveguide_mode cfg =
      let res = boundary_mode_eigenpairs cfg               -- (1) the boundary-mode driver column → EigResult (converged eigenpairs)
          w   = omega cfg
      in  [ let kn    = propagation_constant (res.eigenvalues ! i)  -- kn = shift-invert un-transform of eigenvalue
                n_eff = kn / w                                       -- effective index n_eff = kn/ω
                (et, en) = vd_back_transform (res.eigenvectors ! i) kn  -- VD back-transform → physical (Et, En)
                (et', en') = power_normalize (et, en) w kn          -- normalize so |P| = 1 (Poynting power)
                bz    = if is_propagating kn                        -- longitudinal B for propagating modes
                          then Just (curl et' / (1i * w))
                          else Nothing
            in  { kn, n_eff, et = et', en = en', bz }               -- (2) per-mode waveguide-mode row
          | i <- [0 .. res.converged - 1] ]                          -- map over converged modes (no inter-mode state)

1. **The boundary-mode driver column produces the converged eigenpair set** — [`boundary-mode.L1`](./boundary-mode.L1.md). The upstream composition root extracts the 2D submesh from the 3D boundary, assembles the `ND ⊕ H1` block GEP pencil ([`fe_assemble`](../L1/fe_assemble.md) ×2) and applies the single opaque [`eigsolve`](../L1/eigsolve.md) (**firm**) eigensolver-as-operator **once**, returning an `EigResult` record. This output-product column **consumes** that record; it does not re-derive the solve. L0: the `EigResult`-equivalent extraction `eig.GetEigenvector(i, e0)` (`boundarymodesolver.cpp:297`) + `eig.GetPropagationConstant(i)` (`:299`).

2. **The per-mode pure readout → the waveguide-mode table** — a pure list comprehension over the `res.converged` converged eigenpairs, mapping each mode to its `{kn, n_eff, (Et, En, Bz)}` row:
   - the **propagation constant `kn`** — the shift-invert un-transform of the eigenvalue. L0: `eig.GetPropagationConstant(i)` (`boundarymodesolver.cpp:299`).
   - the **effective index `n_eff = kn/ω`**. L0: `kn.real()/omega` / `kn.imag()/omega` (`boundarymodesolver.cpp:276-277`).
   - the **mode fields `(Et, En)`** — the VD back-transform of the eigenvector, then power-normalized so `|P| = 1`. L0: `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`boundarymodesolver.cpp:300`), `e0 *= 1/√|P|` from `mode_op.ComputePoyntingPower(...)` (`:304-307`).
   - the **longitudinal magnetic field `Bz = curl(Et)/(iω)`** for propagating modes (`is_propagating kn`). L0: the `Bz` formation `bz.Real() = curl_eti; bz.Real() *= 1/ω; bz.Imag() = curl_etr; bz.Imag() *= -1/ω` (`boundarymodesolver.cpp:316-333`).
   This stage is a pure per-mode map — no inter-mode state, no solve-iteration. At L4 this exact per-mode reduction is named the `waveguide_mode_reduce` reduce verb (the propagation-mode member of the L4 output-product reduce-verb algebra); L1 sees the unfolded per-mode comprehension.

## Inputs / outputs (the feature surface)

- **Input — config (boundary attributes + operating frequency).** `BoundaryModeConfig` (operating frequency `freq` → `ω`; boundary `attributes` → the 2D submesh; mode counts → table rows; effective-index `target` → the shift-invert center), inherited from the producing driver column. All read-only.
- **Output — the physical product.** The per-mode `WaveguideModeTable` — one row per converged mode, each `{kn, n_eff, (Et, En, Bz)}` (`Bz` present only for propagating modes). L0: the per-mode observables measured by `post_op.MeasureAndPrintAll(...)` (`boundarymodesolver.cpp:314`) + the `Bz` formation (`:316-333`).

Shape contract (the mode fields are genuine flat rank-1 dof-vectors on the 2D-submesh ND / H1 / curl spaces — `Tensor[N]` is correct per the semantic surface §1.2.1, NOT a named shape group; `kn`/`n_eff` are complex scalars):

```text
-- per converged mode i:
--   kn_i : Complex; n_eff_i : Complex
--   Et_i : Tensor[N_nd, complex]; En_i : Tensor[N_h1, complex]
--   Bz_i : Maybe (Tensor[N_curl, complex])   -- propagating modes only
```

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit per-mode pure list comprehension — the eigenvalue un-transform + the VD back-transform + the power-normalization + the conditional `Bz` formation, written out per mode.
- **L4** ([`waveguide-mode.L4`](./waveguide-mode.L4.md)): the whole per-mode reduction is the `waveguide_mode_reduce` reduce verb (the per-mode map made *structural*). The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 verb names.

The defining structural fact at both levels: a **per-mode mode-TABLE carrying mode-FIELDS** (not only scalars) — distinct from the scalar-only per-element tables (`eigenfreq_qfactor_reduce` / `domain_energy_reduce`) and the rank-2 Gram / port-projection products. The L1→L0 direction (how the per-mode readout lowers to the in-place `GetEigenvector(i, e0)` destination write + the `bz.Real() *= 1/ω` accumulations) is the per-operator L1>L0 mutation-rotation of the readout; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column (sibling reference, not a blocker) | [`boundary-mode.L1`](./boundary-mode.L1.md) (driver feature column) | seed → promotable (own-readout gate cleared by this column) | `boundarymodesolver.cpp:201-268` |
| per-mode propagation-mode readout | *(`waveguide_mode_reduce` reduce verb; rough-in — no firm L4 verb home yet)* | rough-in | `boundarymodesolver.cpp:273-333` |

## Status

`rough-in` — the L1 pure-function composition root for the waveguide-mode output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [waveguide-mode.L4](./waveguide-mode.L4.md) composition root. It consumes the [`boundary-mode.L1`](./boundary-mode.L1.md) driver column's converged eigenpair set, then maps each mode to its `{kn, n_eff, (Et, En, Bz)}` row (the eigenvalue un-transform + the VD back-transform + the power-normalization + the conditional `Bz`). **Held at `rough-in` / `feature_root: seed` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent — the reduction's L4 home `waveguide_mode_reduce` — has no firm L4 verb chapter yet (OQ `waveguide-mode-reduce-needs-l4-verb-home`), exactly the state the L1 `sparameters` column was in when `sparameter_reduce` was rough-in. The cross-link to the [`boundary-mode.L1`](./boundary-mode.L1.md) driver column (itself a firm-once-promoted composition; its `feature_root: seed` is the permanent root marker, not a maturity) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters + the L0 sites. Evidence: the L0 readout range `boundarymodesolver.cpp:273-340` realizing the reduction, all anchors self-verified on-disk this dispatch, plus the constituent down-links.
