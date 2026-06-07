---
kind: feature-surface
feature: waveguide-mode
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: feature/boundary-mode.L4
      kind: composes
    - target: L4/waveguide_mode_reduce
      kind: composes
    - target: palace/drivers/boundarymodesolver.cpp:273-340
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable (the IoData surface)
  reference:
    - feature/boundary-mode.L4
---

# waveguide-mode — L4 composition-root (output product)

The **waveguide-mode table** output product — the per-mode propagation-mode characterization `{kn, n_eff, (Et, En, Bz)}` — presented at L4 as a single composition. This chapter is a **composition root** of the *output-product* sub-kind (a **leaf feature column**): its stage-(2) constituent is the per-mode *reduce verb* `waveguide_mode_reduce`, and its upstream stage is *another feature column* (the [`boundary-mode`](./boundary-mode.L4.md) driver, which produces the converged eigenpair family the reduction consumes). It introduces no new combinator-as-feature; it wires the already-decomposed L4 vocabulary into the user-facing product (config → waveguide-mode table), and links DOWN to each composed piece.

The waveguide-mode table is the physical product the user runs the **boundary-mode** (2D waveguide-mode analysis) solver to obtain: for each converged mode, the **propagation constant `kn`** (complex), the **effective index `n_eff = kn/ω`** (complex), and the **mode-field triple `(Et, En, Bz)`** — the transverse H(curl) field `Et`, the longitudinal H1 field `En`, and (for propagating modes) the longitudinal magnetic field `Bz = curl(Et)/(iω)`. The **boundary-mode driver column** ([`boundary-mode.L4`](./boundary-mode.L4.md)) produces the converged eigenpair family (one eigenpair per mode, on the boundary-extracted 2D submesh); this output-product column reduces that family to the waveguide-mode table via the **per-mode propagation-mode reduction** — un-transforming each eigenvalue to `kn`, VD-back-transforming each eigenvector to `(Et, En)`, power-normalizing to `|P| = 1`, and forming `Bz` for propagating modes.

## The composition

At L4 the waveguide-mode product is the composition (Haskell-style; the semantic surface `book/src/semantics/index.md` notation):

    -- inputs = config (boundary attributes + frequency); output = the waveguide-mode table (the physical product)
    waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable
    waveguide_mode cfg =
      let eigs = boundary_mode_eigenpairs cfg          -- (1) the boundary-mode driver column: extract 2D submesh,
                                                        --     assemble (A,B) GEP pencil, ONE eigsolve → converged eigenpair family
                                                        --     ── feature/boundary-mode.L4 (the producing driver column)
          tbl  = waveguide_mode_reduce eigs (omega cfg) -- (2) per-mode propagation-mode reduce → {kn, n_eff, (Et,En,Bz)}
                                                        --     ── the firm L4 reduce verb (../L4/waveguide_mode_reduce.md)
      in  tbl

Two composed stages, the first a down-link to the producing driver column, the second the per-mode reduce verb:

1. **The producing driver column** — [`boundary-mode.L4`](./boundary-mode.L4.md). The boundary-mode driver extracts a 2D cross-section from the 3D boundary (`CreateFromBoundary` → 3D→2D projection), assembles the `ND ⊕ H1` block GEP pencil `(A, B)` ([`fe_assemble`](../L4/fe_assemble.md), firm), and runs **one** [`eigsolve`](../L4/eigsolve.md) (**firm**) black-box eigen-solve with shift-invert `σ = -kn_target²`, collecting the converged eigenpair family. This output product does NOT re-derive that solve; it consumes the driver column's eigenpair family and reduces it. This is the output-product / driver split the FEATURE-SURFACE SPINE encodes: one driver column (boundary-mode), with the waveguide-mode table the output product hanging off its converged-mode family. L0: the boundary-mode solve in `boundarymodesolver.cpp:201-268`.

2. **The per-mode propagation-mode reduction** — the firm L4 reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) (**firm**). The per-mode reduce maps each converged eigenpair `(λᵢ, xᵢ)` to its waveguide-mode row:
   - the **propagation constant `kn`** — the shift-invert un-transform of the eigenvalue (`kn = √(-λ)` modulo the spectral-transform convention; `eig.GetPropagationConstant(i)` exposes it un-transformed). L0: `eig.GetPropagationConstant(i)` (`boundarymodesolver.cpp:299`, reported `:275`).
   - the **effective index `n_eff = kn / ω`**. L0: the `kn.real()/omega`, `kn.imag()/omega` formation (`boundarymodesolver.cpp:276-277`).
   - the **mode fields `(Et, En)`** — the VD back-transform of the eigenvector, power-normalized so `|P| = 1` over the Poynting power. L0: `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`boundarymodesolver.cpp:300`), the normalization `e0 *= 1/√|P|` from `mode_op.ComputePoyntingPower(...)` (`:304-307`).
   - the **longitudinal magnetic field `Bz = curl(Et)/(iω)`** for propagating modes (`ModeEigenSolver::IsPropagating(kn)`). L0: the `Bz` formation `bz.Real() = curl_eti; bz.Real() *= 1/ω; bz.Imag() = curl_etr; bz.Imag() *= -1/ω` (`boundarymodesolver.cpp:316-333`).

   This is a pure per-mode `map` — no inter-mode state, no solve-iteration. It is the **per-mode propagation-mode sibling** in the output-product reduce-verb algebra (alongside `eigenfreq_qfactor_reduce` per-mode `(f, Q)`, `sparameter_reduce` port-projection, `gram_reduce` family-Gram, `domain_energy_reduce` per-domain): a reduce-to-mode-TABLE, but carrying mode-FIELDS (not only scalars) — it is NOT a `gram_reduce` family-PAIR grid and NOT a scalar-only table. L0: the readout loop `for (int i = 0; i < n_print; i++)` (`boundarymodesolver.cpp:292`), `post_op.MeasureAndPrintAll(...)` (`:314`).

## Inputs / outputs (the feature surface)

- **Input — config (boundary attributes + operating frequency).** `BoundaryModeConfig` (the `iodata.solver.boundary_mode` surface): the operating frequency `freq` → `ω` (the `n_eff = kn/ω` divisor + the `Bz` `1/ω` scale), the boundary `attributes` → the 2D-submesh the family is solved on, the requested + post-written mode counts → the table rows, and the effective-index `target` → the shift-invert center — inherited from the producing boundary-mode driver column. All `readonly` construction-stratum inputs. L0 home: `const auto &bm = iodata.solver.boundary_mode` (`boundarymodesolver.cpp:203`).
- **Output — the physical product.** `WaveguideModeTable` — one row per converged mode, each `{kn, n_eff, (Et, En, Bz)}` (`Bz` present only for propagating modes). The record's data shape (row schema, per-field types/strata, the L0 readout home) is defined in its cross-cutting home [`concepts/WaveguideModeTable.md`](../concepts/WaveguideModeTable.md) (promoted c118 D6 — ≥2 signature consumers: the [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) verb + this L4 column + the L1 column). This is what the user runs the boundary-mode solver to compute (waveguide / wave-port mode characterization). L0 home: the per-mode `kn`/`(et, en)`/`Bz` measured by `post_op.MeasureAndPrintAll(...)` (`boundarymodesolver.cpp:314`) + the `Bz` formation (`:316-333`).

Shape contract (the per-mode reduce, using the semantic surface §1.2.1 named-shape-groups notation for the rank-generic mode field-vectors; `book/src/semantics/index.md`):

```text
waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable
-- per converged mode i:
--   kn_i   : Complex                       -- propagation constant
--   n_eff_i: Complex                       -- = kn_i / ω
--   Et_i   : Tensor[N_nd,  complex]        -- transverse H(curl) mode field (flat ND dof-vector)
--   En_i   : Tensor[N_h1,  complex]        -- longitudinal H1 mode field (flat H1 dof-vector)
--   Bz_i   : Maybe (Tensor[N_curl, complex]) -- longitudinal B (propagating modes only)
```

(The mode fields are genuine **flat rank-1 dof-vectors** on the 2D submesh ND / H1 / curl spaces — `Tensor[N]` is correct here per §1.2.1, NOT a named shape group; `kn`/`n_eff` are complex scalars.)

## Why this is an output-product column

- The upstream family is supplied whole by the [`boundary-mode.L4`](./boundary-mode.L4.md) driver column — no re-derivation, just consumption of the converged eigenpair family.
- The reduction `waveguide_mode_reduce` is a **per-mode map** carrying mode FIELDS + propagation scalars — the propagation-mode member of the output-product reduce-verb algebra, distinct from the rank-2 Gram (`gram_reduce`), the rank-2 port-projection (`sparameter_reduce`), and the scalar-only per-element tables (`eigenfreq_qfactor_reduce` / `domain_energy_reduce`).
- It shares the **`eigsolve` solve corner** with `eigenfrequency-qfactor` (both reduce an eigenpair family) but over the **boundary-mode** driver (the 2D-submesh-extracted GEP), not the 3D-domain eigenmode driver — the same driver-distinction boundary-mode carries against eigenmode.

The whole output product lowers cleanly outward to the L4 backend surface: `waveguide_mode = waveguide_mode_reduce (ω) ∘ boundary_mode_eigenpairs` — a one-reduction tail on the boundary-mode driver column.

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column (sibling reference, not a blocker) | [`boundary-mode.L4`](./boundary-mode.L4.md) (driver feature column) | seed → promotable (own-readout gate cleared by this column) | `boundarymodesolver.cpp:201-268` |
| per-mode propagation-mode reduction | [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) (firm L4 reduce verb, c118 D5) | firm | `boundarymodesolver.cpp:273-333` |
| └ propagation-constant un-transform | `eig.GetPropagationConstant(i)` (L0 site) | (L0 site) | `boundarymodesolver.cpp:299` |
| └ VD back-transform → (Et, En) | `mode_op.ApplyVDBackTransform` (L0 site) | (L0 site) | `boundarymodesolver.cpp:300` |
| └ power-normalize `|P|=1` | `mode_op.ComputePoyntingPower` (L0 site) | (L0 site) | `boundarymodesolver.cpp:304` |
| └ Bz = curl(Et)/(iω) | `IsPropagating` branch (L0 site) | (L0 site) | `boundarymodesolver.cpp:316-333` |

## Status

`firm` — the L4 composition root for the waveguide-mode output product (an output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), homing the boundary-mode driver's stage-(3) readout reduction that the [`boundary-mode`](./boundary-mode.L4.md) chapters previously carried as a forward-ref ("the reduction into the reported waveguide-mode product is a forward-ref, no dedicated output-product column yet"). **Promoted `rough-in` → `firm` (cycle-118 D5) under the OWN-COMPOSITION rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; user directive 2026-06-03; memory `project_feature_column_promotion_rule`): an output-product column promotes off `seed`/`rough-in` when its OWN reduce verb + directly-owned constituents are firm. This column's directly-owned reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) is now **firm** (its dedicated L4 verb chapter landed c118 D5, OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED), so the OWN-COMPOSITION promotion gate clears — exactly as [`sparameters`](./sparameters.L4.md) promoted when `sparameter_reduce` firmed at c083. **`feature_root: seed` is KEPT** (the permanent GC-root marker, NOT a ladder rung — the column is a reachability root, not a maturity tier). The cross-link to the [`boundary-mode.L4`](./boundary-mode.L4.md) producing driver column is a **SIBLING reference, NOT a blocker** (the reciprocal drift-guard). This chapter carries the *compositional* claim (waveguide-mode = the per-mode reduce over the boundary-mode driver's converged eigenpair family), not the per-op algebraic claims (those live in the constituent ops + the L0 sites). Evidence: the L0 readout range `boundarymodesolver.cpp:273-340` realizing the reduction, all anchors self-verified on-disk, plus the constituent down-links + the now-firm `waveguide_mode_reduce` verb.
