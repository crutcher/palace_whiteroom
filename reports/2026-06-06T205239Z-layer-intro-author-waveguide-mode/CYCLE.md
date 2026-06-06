---
agent: layer-intro-author
invoked_at: 2026-06-06T205239Z
scope: feature/waveguide-mode output-product column (cycle-117 D1, WAVE-1, open-all-feature-fronts front (i))
status: integrated
integrated_at: 2026-06-06T214845Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-117 D1 (apply-order 1/5). New 6th output-product feature column feature/waveguide-mode.{L4,L1,L0}.md (seed/rough-in) + sole-owned feature/index.md + output-product.md + SUMMARY.md (incl boundary-mode firm index-cell on D2's behalf). All per-report gates PASS; rank/reachability re-measured clean by finalize (waveguide-mode chapters reachable as feature-surface roots, roots 36->39). 3 OQs promoted."
---

# CYCLE: waveguide-mode 6th output-product feature column

## Summary

Authors the **`waveguide-mode` output-product feature column** — the 6th output product, the boundary-mode driver's readout reduction homed at last. Three new files (high→low within-column ordering): `book/src/feature/waveguide-mode.{L4,L1,L0}.md`. The column is an **output-product leaf feature column** whose composition root is:

> **input = the `boundary-mode` driver's converged eigenpair family → per-mode reduce verb (`kn` propagation-constant + `n_eff = kn/ω` extraction + `(Et, En, Bz)` field components + power-normalization to `|P| = 1`) → output = the waveguide-mode physical product `{kn, n_eff, (Et, En, Bz)}`.**

It composes the firm [`eigsolve`](../../book/src/L1/eigsolve.md) readout vocabulary (via the producing `boundary-mode` driver column) and a NEW per-mode reduce verb `waveguide_mode_reduce` (the analog of `sparameter_reduce` / `domain_energy_reduce` / `eigenfreq_qfactor_reduce`). Because that reduce verb has **no firm L4 home yet** (no `L4/waveguide_mode_reduce.md`), the column lands `status: seed` / `rank: rough-in` under the OWN-COMPOSITION rule — exactly the state `sparameters` was in when `sparameter_reduce` was rough-in. I flag the verb-home + the `WaveguideModeTable` record-home as Open questions.

As the SOLE owner of the shared `feature/` index this cycle, this report ALSO carries: the `feature/index.md` matrix row (alpha after `sparameters`) + the `feature/output-product.md` group-intro bullet + the `feature/SUMMARY.md` 3 entries, AND (on D2's behalf) the `boundary-mode` index-cell + sibling-status reflection now that its waveguide-mode product has a home (clearing its own-readout `seed` gate — D2 promotes the boundary-mode chapter bodies/frontmatter; I own the index-cell reflection only).

## Clean-gate: on-disk firm-status evidence for `eigsolve` (the readout vocabulary composed)

`book/src/L1/eigsolve.md` `## Status` line (read on-disk this dispatch, lines 178-188):

> `firm` (cycle-022, route-(b) law-confidence re-eval; promoted from `rough-in (test-coverage-bounded)` landed cycle-009, refined cycles 010/011/012) — the structural signature ... is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies; the algebraic laws (1-6) are firm because **each is a syntactic identity on fully-specified positive source** ...

Frontmatter `rank: firm` (`book/src/L1/eigsolve.md:4`). The boundary-mode column composes `eigsolve` via the producing `boundary-mode` driver column (which itself depends-on `L1/eigsolve` + `L4/eigsolve`, both firm — `boundary-mode.L1.md:10` / `boundary-mode.L4.md:11`). The L4 `eigsolve` cap is the black-box-kernel constituent (opaque-library SLEPc/ARPACK eigen-iteration) per `project_blackbox_vs_accelerated_kernels`. The waveguide-mode reduction CONSUMES the `EigResult` that `eigsolve` produces; it does not re-derive the solve.

## Source-range self-verification (on-disk, `reference/palace/palace/drivers/boundarymodesolver.cpp`)

All citation paths are relative to `reference/` per CLAUDE.md (i.e. `palace/drivers/boundarymodesolver.cpp` resolves on-disk to `reference/palace/palace/drivers/boundarymodesolver.cpp`). Confirmed this dispatch:

| Citation | Anchor token confirmed on-disk |
|---|---|
| `palace/drivers/boundarymodesolver.cpp:273` | propagation-constant report loop `for (int i = 0; i < num_conv; i++)` |
| `palace/drivers/boundarymodesolver.cpp:275` | `auto kn = eig.GetPropagationConstant(i)` (+ `n_eff = kn/ω` print `:276-277`) |
| `palace/drivers/boundarymodesolver.cpp:292` | readout loop `for (int i = 0; i < n_print; i++)` (`n_print = min(num_conv, num_modes)`) |
| `palace/drivers/boundarymodesolver.cpp:297` | `eig.GetEigenvector(i, e0)` (the in-place destination write the L1 form lifts) |
| `palace/drivers/boundarymodesolver.cpp:300` | `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (VD back-transform → physical `et`/`en`) |
| `palace/drivers/boundarymodesolver.cpp:304` | `mode_op.ComputePoyntingPower(omega, kn, et, en)` (the power for `|P|=1` normalization) |
| `palace/drivers/boundarymodesolver.cpp:304-307` | power-normalization `e0 *= 1/sqrt(|P|)` |
| `palace/drivers/boundarymodesolver.cpp:310-311` | `error_bkwd` (`:310`) / `error_abs` (`:311`) per-pair error reads |
| `palace/drivers/boundarymodesolver.cpp:314` | `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` |
| `palace/drivers/boundarymodesolver.cpp:316` | `ModeEigenSolver::IsPropagating(kn)` propagating-mode branch + `Bz = curl(Et)/(iω)` block (`:317-333`) |
| `palace/drivers/boundarymodesolver.cpp:339-340` | driver return `{indicator, NDSpace.GlobalTrueVSize() + H1Space.GlobalTrueVSize()}` |

(Note: the prompt's pre-localized `ComputePoyntingPower :304` and the `(Et, En, Bz)` block lines all confirmed; `GetEigenvector` is at `:297` and the report loop at `:273` — used as cited.)

## Proposed changes

### New file 1 of 3 (L4 — high in within-column ordering)

```edit:book/src/feature/waveguide-mode.L4.md
[old]:
[new]:
---
kind: feature-surface
feature: waveguide-mode
level: L4
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: feature/boundary-mode.L4
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
                                                        --     ── the reduce verb (rough-in; no firm L4 home yet)
      in  tbl

Two composed stages, the first a down-link to the producing driver column, the second the per-mode reduce verb:

1. **The producing driver column** — [`boundary-mode.L4`](./boundary-mode.L4.md). The boundary-mode driver extracts a 2D cross-section from the 3D boundary (`CreateFromBoundary` → 3D→2D projection), assembles the `ND ⊕ H1` block GEP pencil `(A, B)` ([`fe_assemble`](../L4/fe_assemble.md), firm), and runs **one** [`eigsolve`](../L4/eigsolve.md) (**firm**) black-box eigen-solve with shift-invert `σ = -kn_target²`, collecting the converged eigenpair family. This output product does NOT re-derive that solve; it consumes the driver column's eigenpair family and reduces it. This is the output-product / driver split the FEATURE-SURFACE SPINE encodes: one driver column (boundary-mode), with the waveguide-mode table the output product hanging off its converged-mode family. L0: the boundary-mode solve in `boundarymodesolver.cpp:201-268`.

2. **The per-mode propagation-mode reduction** — `waveguide_mode_reduce` (**rough-in; no firm L4 home yet**). The per-mode reduce maps each converged eigenpair `(λᵢ, xᵢ)` to its waveguide-mode row:
   - the **propagation constant `kn`** — the shift-invert un-transform of the eigenvalue (`kn = √(-λ)` modulo the spectral-transform convention; `eig.GetPropagationConstant(i)` exposes it un-transformed). L0: `eig.GetPropagationConstant(i)` (`boundarymodesolver.cpp:299`, reported `:275`).
   - the **effective index `n_eff = kn / ω`**. L0: the `kn.real()/omega`, `kn.imag()/omega` formation (`boundarymodesolver.cpp:276-277`).
   - the **mode fields `(Et, En)`** — the VD back-transform of the eigenvector, power-normalized so `|P| = 1` over the Poynting power. L0: `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`boundarymodesolver.cpp:300`), the normalization `e0 *= 1/√|P|` from `mode_op.ComputePoyntingPower(...)` (`:304-307`).
   - the **longitudinal magnetic field `Bz = curl(Et)/(iω)`** for propagating modes (`ModeEigenSolver::IsPropagating(kn)`). L0: the `Bz` formation `bz.Real() = curl_eti; bz.Real() *= 1/ω; bz.Imag() = curl_etr; bz.Imag() *= -1/ω` (`boundarymodesolver.cpp:316-333`).

   This is a pure per-mode `map` — no inter-mode state, no solve-iteration. It is the **per-mode propagation-mode sibling** in the output-product reduce-verb algebra (alongside `eigenfreq_qfactor_reduce` per-mode `(f, Q)`, `sparameter_reduce` port-projection, `gram_reduce` family-Gram, `domain_energy_reduce` per-domain): a reduce-to-mode-TABLE, but carrying mode-FIELDS (not only scalars) — it is NOT a `gram_reduce` family-PAIR grid and NOT a scalar-only table. L0: the readout loop `for (int i = 0; i < n_print; i++)` (`boundarymodesolver.cpp:292`), `post_op.MeasureAndPrintAll(...)` (`:314`).

## Inputs / outputs (the feature surface)

- **Input — config (boundary attributes + operating frequency).** `BoundaryModeConfig` (the `iodata.solver.boundary_mode` surface): the operating frequency `freq` → `ω` (the `n_eff = kn/ω` divisor + the `Bz` `1/ω` scale), the boundary `attributes` → the 2D-submesh the family is solved on, the requested + post-written mode counts → the table rows, and the effective-index `target` → the shift-invert center — inherited from the producing boundary-mode driver column. All `readonly` construction-stratum inputs. L0 home: `const auto &bm = iodata.solver.boundary_mode` (`boundarymodesolver.cpp:203`).
- **Output — the physical product.** `WaveguideModeTable` — one row per converged mode, each `{kn, n_eff, (Et, En, Bz)}` (`Bz` present only for propagating modes). This is what the user runs the boundary-mode solver to compute (waveguide / wave-port mode characterization). L0 home: the per-mode `kn`/`(et, en)`/`Bz` measured by `post_op.MeasureAndPrintAll(...)` (`boundarymodesolver.cpp:314`) + the `Bz` formation (`:316-333`).

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
| per-mode propagation-mode reduction | `waveguide_mode_reduce` *(rough-in; no firm L4 verb chapter yet — OQ `waveguide-mode-reduce-needs-l4-verb-home`)* | rough-in | `boundarymodesolver.cpp:273-333` |
| └ propagation-constant un-transform | `eig.GetPropagationConstant(i)` (L0 site) | (L0 site) | `boundarymodesolver.cpp:299` |
| └ VD back-transform → (Et, En) | `mode_op.ApplyVDBackTransform` (L0 site) | (L0 site) | `boundarymodesolver.cpp:300` |
| └ power-normalize `|P|=1` | `mode_op.ComputePoyntingPower` (L0 site) | (L0 site) | `boundarymodesolver.cpp:304` |
| └ Bz = curl(Et)/(iω) | `IsPropagating` branch (L0 site) | (L0 site) | `boundarymodesolver.cpp:316-333` |

## Status

`rough-in` — the L4 composition root for the waveguide-mode output product (an output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), homing the boundary-mode driver's stage-(3) readout reduction that the [`boundary-mode`](./boundary-mode.L4.md) chapters previously carried as a forward-ref ("the reduction into the reported waveguide-mode product is a forward-ref, no dedicated output-product column yet"). **Held at `rough-in` / `feature_root: seed` under the OWN-COMPOSITION rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; user directive 2026-06-03; memory `project_feature_column_promotion_rule`): an output-product column promotes off `seed` when its OWN reduce verb + directly-owned constituents are firm. This column's directly-owned reduce verb `waveguide_mode_reduce` has **no firm L4 home yet** (no `L4/waveguide_mode_reduce.md` chapter — its per-mode constituents are read at L0 sites but the verb is unhomed), exactly the state [`sparameters`](./sparameters.L4.md) was in when `sparameter_reduce` was rough-in. The cross-link to the [`boundary-mode.L4`](./boundary-mode.L4.md) producing driver column is a **SIBLING reference, NOT a blocker** (the reciprocal drift-guard). The promotion route is a firm `waveguide_mode_reduce` L4 verb chapter (OQ `waveguide-mode-reduce-needs-l4-verb-home`) — once it firms, this column promotes to `firm`, exactly as `sparameters` promoted at c083. This chapter carries the *compositional* claim (waveguide-mode = the per-mode reduce over the boundary-mode driver's converged eigenpair family), not the per-op algebraic claims (those live in the constituent ops + the L0 sites). Evidence: the L0 readout range `boundarymodesolver.cpp:273-340` realizing the reduction, all anchors self-verified on-disk this dispatch, plus the constituent down-links.
```

### New file 2 of 3 (L1 — middle in within-column ordering)

```edit:book/src/feature/waveguide-mode.L1.md
[old]:
[new]:
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
```

### New file 3 of 3 (L0 — low in within-column ordering)

```edit:book/src/feature/waveguide-mode.L0.md
[old]:
[new]:
---
kind: feature-surface
feature: waveguide-mode
level: L0
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: palace/drivers/boundarymodesolver.cpp:273-340
      kind: cites-evidence
  reference:
    - feature/waveguide-mode.L1
    - feature/boundary-mode.L0
---

# waveguide-mode — L0 ground-truth surface (output product)

The **waveguide-mode table** output product at L0: the cited Palace driver source that realizes the per-mode propagation-mode reduction over the boundary-mode driver's converged eigenpair family, with the per-stage source ranges the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/boundarymodesolver.cpp`. The reduction's *producing* driver source (extract → assemble → eigen-solve) is the [`boundary-mode.L0`](./boundary-mode.L0.md) surface; this output-product surface covers the **readout reduction** stage that consumes the converged eigenpair family.

## The reduction, in source

After the boundary-mode driver's single opaque `eig.Solve(omega, sigma)` (`boundarymodesolver.cpp:268`) returns the converged-mode count, the driver runs **two post-processing readout loops** — pure post-processing maps over the converged modes, NOT solve-iterations. These loops ARE the waveguide-mode reduction:

1. **The propagation-constant report loop.** `for (int i = 0; i < num_conv; i++)` (`boundarymodesolver.cpp:273`): per mode, `auto kn = eig.GetPropagationConstant(i)` (`:275`) reads the propagation constant (the shift-invert un-transform of the eigenvalue), and the effective index `n_eff = kn/ω` is formed as `kn.real()/omega`, `kn.imag()/omega` (`:276-277`). This is the L0 site the L1/L4 `kn` / `n_eff` extraction lift.

2. **The mode-field readout loop.** `for (int i = 0; i < n_print; i++)` (`boundarymodesolver.cpp:292`, `n_print = min(num_conv, num_modes)`): per mode —
   - `eig.GetEigenvector(i, e0)` (`:297`) reads the raw eigenvector into the destination buffer (the in-place write the L1 form lifts);
   - `const std::complex<double> kn = eig.GetPropagationConstant(i)` (`:299`);
   - `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`) applies the VD back-transform to recover the physical transverse `et` + longitudinal `en` fields;
   - the mode is **power-normalized to `|P| = 1`**: `const std::complex<double> P_initial = mode_op.ComputePoyntingPower(omega, kn, et, en)` (`:304`) then `e0 *= 1.0/std::sqrt(std::abs(P_initial))` when `|P| > 0` (`:305-307`, the in-place normalization the L1 form lifts);
   - the backward + absolute errors are read (`error_bkwd` `:310`, `error_abs` `:311`);
   - `auto total_domain_energy = post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`) measures + records the per-mode observables;
   - for propagating modes (`ModeEigenSolver::IsPropagating(kn)`, `:316`) the longitudinal magnetic field `Bz = curl(Et)/(iω)` is formed: `CurlOp.Mult(et.Real(), curl_etr)` / `CurlOp.Mult(et.Imag(), curl_eti)` (`:326-327`) then `bz.Real() = curl_eti; bz.Real() *= 1.0/omega` / `bz.Imag() = curl_etr; bz.Imag() *= -1.0/omega` (`:328-331`, the in-place accumulations the L1 form lifts), fed to the error estimator `estimator.AddErrorIndicator(...)` (`:332`).

   The readout loop closes at `:334`; `post_op.MeasureFinalize(indicator)` (`:337`) finalizes. This is the L0 site the L1/L4 per-mode reduce verb lifts.

The driver returns `{indicator, mode_op.GetNDSpace().GlobalTrueVSize() + mode_op.GetH1Space().GlobalTrueVSize()}` (`:339-340`).

## Inputs / outputs (the feature surface, in source)

- **Input — the converged eigenpair family + config.** The `result` of `eig.Solve(omega, sigma)` (`:268`, `result.num_converged` at `:269`) — the converged eigenpair family the producing [`boundary-mode.L0`](./boundary-mode.L0.md) driver computes; plus `const auto &bm = iodata.solver.boundary_mode` (`:203`) and `omega` (`:206-207`).
- **Output — the physical product.** The per-mode propagation constant `kn` (`eig.GetPropagationConstant(i)`, `:299`), effective index `n_eff = kn/omega` (`:276-277`), transverse + longitudinal mode fields `(et, en)` (`:300`), and (propagating modes) `Bz` (`:316-333`), measured by `post_op.MeasureAndPrintAll(...)` (`:314`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`waveguide-mode.L1`](./waveguide-mode.L1.md) (the `GetEigenvector(i, e0)` destination write → a value-returning eigenpair-field read; the `e0 *= 1/√|P|` normalization → a pure `power_normalize`; the in-place `bz.Real() *= 1/ω` accumulations → a pure `Bz = curl(Et)/(iω)` value) and the L4 reduce-verb composition root [`waveguide-mode.L4`](./waveguide-mode.L4.md) (the two readout `for` loops → the `waveguide_mode_reduce` per-mode `map`). The per-operator L1>L0 mutation-rotation themes of the constituent reads carry the per-write lifts; this feature surface records the reduction-stage *site map*.

## Status

`rough-in` — the L0 ground-truth surface for the waveguide-mode output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L0 surface of the readout reduction that the [`boundary-mode.L0`](./boundary-mode.L0.md) driver carries as a forward-ref. **Held at `rough-in` / `feature_root: seed` under the OWN-COMPOSITION rule:** the reduction's L4 verb home `waveguide_mode_reduce` has no firm chapter yet (OQ `waveguide-mode-reduce-needs-l4-verb-home`). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`, self-verified on-disk this dispatch (the propagation-constant report loop `:273-277`, the mode-field readout loop `:292-334` with `GetEigenvector` `:297`, `ApplyVDBackTransform` `:300`, `ComputePoyntingPower` `:304`, the power-normalization `:305-307`, `MeasureAndPrintAll` `:314`, the `IsPropagating` branch + `Bz` formation `:316-333`, the return `:339-340`). The load-bearing structural fact at L0: the waveguide-mode product is a pair of **pure post-processing readout loops** over the converged eigenpair family — NOT a solve-iteration (the driver's only outer loops). The chapter's evidence IS the driver-source range + the per-stage site map (the adapted surface-or-evidence form for the feature-surface kind).
```

### Index edit 1 — `feature/index.md` matrix row (alpha after `sparameters`, last output-product row)

```edit:book/src/feature/index.md
[old]:
| [sparameters](./sparameters.L4.md) | [L4 root](./sparameters.L4.md) | [L1 root](./sparameters.L1.md) | [L0 surface](./sparameters.L0.md) |

The **driven**, **transient**, and **eigenmode** driver columns (cycle-073)
[new]:
| [sparameters](./sparameters.L4.md) | [L4 root](./sparameters.L4.md) | [L1 root](./sparameters.L1.md) | [L0 surface](./sparameters.L0.md) |
| [waveguide-mode](./waveguide-mode.L4.md) | [L4 root](./waveguide-mode.L4.md) | [L1 root](./waveguide-mode.L1.md) | [L0 surface](./waveguide-mode.L0.md) |

The **driven**, **transient**, and **eigenmode** driver columns (cycle-073)
```

### Index edit 2 — `feature/index.md` output-product cohort prose (add the 6th product + the per-mode mode-table shape)

```edit:book/src/feature/index.md
[old]:
- **Per-domain scalar-table (rank-1)** — cycle-078: [`energy-fields`](./energy-fields.L4.md), over a *single solution field* (not a family) from any field-bearing driver. It composes the `domain_energy_reduce` reduction (minted c078, **firm c091** — promoted by the batch-29 firm-flip-and-cascade wave once both its folded primitives firmed) — a per-domain `(energyᵢ, pᵢ)` map folding the domain-restricted SPD energy form `½⟨field, M_i field⟩` (**firm** [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared, firm c091) and the **firm** [`participation_ratio`](../L1/participation_ratio.md). It is the **per-domain** sibling of the per-mode `eigenfreq_qfactor_reduce` table (both reduce-to-scalar-TABLE, rank-1) — NOT a `gram_reduce` family-PAIR grid (the c074 D6 do-NOT-over-unify guard, honored).
[new]:
- **Per-domain scalar-table (rank-1)** — cycle-078: [`energy-fields`](./energy-fields.L4.md), over a *single solution field* (not a family) from any field-bearing driver. It composes the `domain_energy_reduce` reduction (minted c078, **firm c091** — promoted by the batch-29 firm-flip-and-cascade wave once both its folded primitives firmed) — a per-domain `(energyᵢ, pᵢ)` map folding the domain-restricted SPD energy form `½⟨field, M_i field⟩` (**firm** [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared, firm c091) and the **firm** [`participation_ratio`](../L1/participation_ratio.md). It is the **per-domain** sibling of the per-mode `eigenfreq_qfactor_reduce` table (both reduce-to-scalar-TABLE, rank-1) — NOT a `gram_reduce` family-PAIR grid (the c074 D6 do-NOT-over-unify guard, honored).
- **Per-mode mode-table (carrying mode-FIELDS)** — cycle-117: [`waveguide-mode`](./waveguide-mode.L4.md), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family. It composes the new `waveguide_mode_reduce` reduce verb (**rough-in** — no firm L4 verb chapter yet, OQ `waveguide-mode-reduce-needs-l4-verb-home`) — a per-mode map to `{kn, n_eff, (Et, En, Bz)}` (the propagation constant `kn` un-transformed from the eigenvalue, `n_eff = kn/ω`, the VD-back-transformed power-normalized mode fields `(Et, En)`, and `Bz = curl(Et)/(iω)` for propagating modes). It is the **propagation-mode** member of the output-product reduce-verb algebra: a reduce-to-mode-TABLE, but carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref ("no dedicated output-product column yet").
```

### Index edit 3 — `feature/index.md` directive-scope line (waveguide-mode lands; boundary-mode gate cleared)

```edit:book/src/feature/index.md
[old]:
The FEATURE-SURFACE SPINE directive scope is fully authored (cycle-078 landed the last output product [`energy-fields`](./energy-fields.L4.md) and the 6th-`ProblemType` wave-port / [`boundary-mode`](./boundary-mode.L4.md) driver column, a co-equal leaf driver column under the lifecycle ROOT). Cycle-085 ran the all-12-column re-evaluation under the OWN-COMPOSITION promotion rule, and cycle-091 + cycle-095 closed the gram-Gram cascade; after cycle-095 only [`boundary-mode`](./boundary-mode.L4.md) remains `seed` (its stage-(3) readout reduces into a waveguide-mode output product with no firm home — an own-readout gate, the waveguide-mode product column being demand-gated). A column that cannot yet be cleanly composed — i.e. one of its directly-owned constituents is still rough-in or unhomed — stays `seed` as a *finding about the spine* (surfaced as an open question, the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]:
The FEATURE-SURFACE SPINE directive scope is authored across 13 columns (cycle-078 landed the last 1:1 output product [`energy-fields`](./energy-fields.L4.md) and the 6th-`ProblemType` wave-port / [`boundary-mode`](./boundary-mode.L4.md) driver column; cycle-117 opened the 6th output product [`waveguide-mode`](./waveguide-mode.L4.md) — the boundary-mode driver's readout reduction, demand-gate fired by the post-consolidation open-all-feature-fronts wave, user directive 2026-06-06). Cycle-085 ran the all-12-column re-evaluation under the OWN-COMPOSITION promotion rule, cycle-091 + cycle-095 closed the gram-Gram cascade, and cycle-117 cleared boundary-mode's own-readout gate (homing its readout in the new waveguide-mode output-product column — a SIBLING cross-link, not a blocker), promoting boundary-mode to `firm`. After cycle-117 only [`waveguide-mode`](./waveguide-mode.L4.md) remains `seed` (its own reduce verb `waveguide_mode_reduce` has no firm L4 verb home yet — an own-reduce-verb gate; promotes once that verb firms, exactly as `sparameters` promoted at c083). A column that cannot yet be cleanly composed — i.e. one of its directly-owned constituents is still rough-in or unhomed — stays `seed` as a *finding about the spine* (surfaced as an open question, the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

### Index edit 4 — `feature/index.md` Chapter-kind status `firm`/`seed` split (boundary-mode → firm; waveguide-mode → seed)

```edit:book/src/feature/index.md
[old]:
- **`firm` (11 columns)** — own composition + directly-owned constituents all firm; cross-linked sibling columns are references, not blockers:
  - driver-leaf: [`eigenmode`](./eigenmode.L4.md) (own `fe_assemble`×3 + `eigsolve` firm; `eigenfrequency-qfactor` is a sibling cross-link), [`driven`](./driven.L4.md) (own `fe_assemble` + `assemble_frequency_operator` + `frequency_sweep` + `ksp_solve` firm; `sparameters` is a sibling cross-link), [`transient`](./transient.L4.md) (own `fe_assemble` + `fold_solve` firm; no output-product sibling), [`electrostatic`](./electrostatic.L4.md) (own `fe_assemble` + `solve_family` c086 + `ksp_solve` + stage-(3) `gram_reduce` firm c095; `capacitance` is a sibling cross-link — promoted `seed`→`firm` c095 by the cascade), [`magnetostatic`](./magnetostatic.L4.md) (own `fe_assemble` + `solve_family` c086 + `ksp_solve` + stage-(3) `gram_reduce` firm c095; `inductance` is a sibling cross-link — promoted `seed`→`firm` c095 by the cascade).
[new]:
- **`firm` (12 columns)** — own composition + directly-owned constituents all firm; cross-linked sibling columns are references, not blockers:
  - driver-leaf: [`boundary-mode`](./boundary-mode.L4.md) (own `fe_assemble` + `eigsolve` firm; its own-readout gate cleared cycle-117 — its readout reduction is now homed in the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column, a sibling cross-link, NOT a blocker — promoted `seed`→`firm` c117), [`eigenmode`](./eigenmode.L4.md) (own `fe_assemble`×3 + `eigsolve` firm; `eigenfrequency-qfactor` is a sibling cross-link), [`driven`](./driven.L4.md) (own `fe_assemble` + `assemble_frequency_operator` + `frequency_sweep` + `ksp_solve` firm; `sparameters` is a sibling cross-link), [`transient`](./transient.L4.md) (own `fe_assemble` + `fold_solve` firm; no output-product sibling), [`electrostatic`](./electrostatic.L4.md) (own `fe_assemble` + `solve_family` c086 + `ksp_solve` + stage-(3) `gram_reduce` firm c095; `capacitance` is a sibling cross-link — promoted `seed`→`firm` c095 by the cascade), [`magnetostatic`](./magnetostatic.L4.md) (own `fe_assemble` + `solve_family` c086 + `ksp_solve` + stage-(3) `gram_reduce` firm c095; `inductance` is a sibling cross-link — promoted `seed`→`firm` c095 by the cascade).
```

### Index edit 5 — `feature/index.md` `seed`-block in Chapter-kind status (waveguide-mode is now the held column)

```edit:book/src/feature/index.md
[old]:
- **`seed` (1 column)** — held on a genuine **own-constituent gate** (a directly-owned constituent is rough-in or unhomed), NOT a sibling-column blocker:
  - [`boundary-mode`](./boundary-mode.L4.md) — own stage-(3) readout reduces into a waveguide-mode output product with no firm home (own-readout gate; the waveguide-mode product column is demand-gated).

The critic's surface-or-evidence check
[new]:
- **`seed` (1 column)** — held on a genuine **own-constituent gate** (a directly-owned constituent is rough-in or unhomed), NOT a sibling-column blocker:
  - [`waveguide-mode`](./waveguide-mode.L4.md) (cycle-117, output-product) — its own reduce verb `waveguide_mode_reduce` has no firm L4 verb home yet (own-reduce-verb gate; OQ `waveguide-mode-reduce-needs-l4-verb-home`). Promotes to `firm` once that verb firms, exactly as `sparameters` promoted at c083.

The critic's surface-or-evidence check
```

(Note: index edits 3 (directive-scope paragraph) and 4/5 (Chapter-kind status `firm`/`seed` split) both mention boundary-mode's now-cleared `seed` gate but at distinct locations; each old-string is unique to its location by the distinct surrounding context lines included. The single structured `seed (1 column)` bullet at `feature/index.md:79-80` is replaced by edit 5.)

### Group-intro edit — `feature/output-product.md` (add the 6th product bullet + edge + complete-cohort prose)

```edit:book/src/feature/output-product.md
[old]:
    - feature/sparameters.L4
    - feature/sparameters.L1
    - feature/sparameters.L0
---
[new]:
    - feature/sparameters.L4
    - feature/sparameters.L1
    - feature/sparameters.L0
    - feature/waveguide-mode.L4
    - feature/waveguide-mode.L1
    - feature/waveguide-mode.L0
---
```

```edit:book/src/feature/output-product.md
[old]:
- [`sparameters`](./sparameters.L4.md) — **port-projection (rank-2 matrix, a LINEAR projection — NOT a Gram)**, the [`sparameter_reduce`](../L4/sparameter_reduce.md) reduction, over the [`driven`](./driven.L4.md) driver's per-ω family. Levels: [L4](./sparameters.L4.md) · [L1](./sparameters.L1.md) · [L0](./sparameters.L0.md).

Columns are alpha-ordered within this grouping.
[new]:
- [`sparameters`](./sparameters.L4.md) — **port-projection (rank-2 matrix, a LINEAR projection — NOT a Gram)**, the [`sparameter_reduce`](../L4/sparameter_reduce.md) reduction, over the [`driven`](./driven.L4.md) driver's per-ω family. Levels: [L4](./sparameters.L4.md) · [L1](./sparameters.L1.md) · [L0](./sparameters.L0.md).
- [`waveguide-mode`](./waveguide-mode.L4.md) — **per-mode mode-table (carrying mode-FIELDS)**, the `waveguide_mode_reduce` reduction (**rough-in** — no firm L4 verb chapter yet, OQ `waveguide-mode-reduce-needs-l4-verb-home`), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family — a per-mode map to `{kn, n_eff, (Et, En, Bz)}`. The propagation-mode member of the reduce-verb algebra: a reduce-to-mode-TABLE carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout that was previously a forward-ref. **The column is `seed`** (own reduce verb rough-in). Levels: [L4](./waveguide-mode.L4.md) · [L1](./waveguide-mode.L1.md) · [L0](./waveguide-mode.L0.md).

Columns are alpha-ordered within this grouping.
```

```edit:book/src/feature/output-product.md
[old]:
Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. With [`energy-fields`](./energy-fields.L4.md) (cycle-078) the output-product cohort is complete (5 columns), and after the cycle-091 + cycle-095 energy-Gram cascade **all 5 output-product columns are `firm`** under the OWN-COMPOSITION rule (a column promotes off `seed` when its OWN reduce verb + directly-owned constituents are firm; cross-linked sibling driver columns are references, NOT blockers): [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb firm c082), [`sparameters`](./sparameters.L4.md) (own verb firm c083), [`energy-fields`](./energy-fields.L4.md) (own verb firm c091), and [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) (own verb [`gram_reduce`](../L4/gram_reduce.md) firm c095, once its off-diagonal `bilinear-form` folded primitive firmed).
[new]:
Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. The cohort holds **6 columns**: with [`energy-fields`](./energy-fields.L4.md) (cycle-078) the five 1:1 + driver-agnostic products landed, and [`waveguide-mode`](./waveguide-mode.L4.md) (cycle-117) added the 6th (the boundary-mode driver's readout product, demand-gate fired by the post-consolidation open-all-feature-fronts wave). After the cycle-091 + cycle-095 energy-Gram cascade **the five reduce-verb-firm columns are `firm`** under the OWN-COMPOSITION rule (a column promotes off `seed` when its OWN reduce verb + directly-owned constituents are firm; cross-linked sibling driver columns are references, NOT blockers): [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb firm c082), [`sparameters`](./sparameters.L4.md) (own verb firm c083), [`energy-fields`](./energy-fields.L4.md) (own verb firm c091), and [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) (own verb [`gram_reduce`](../L4/gram_reduce.md) firm c095, once its off-diagonal `bilinear-form` folded primitive firmed). [`waveguide-mode`](./waveguide-mode.L4.md) is the sole **`seed`** output-product column — its own reduce verb `waveguide_mode_reduce` is rough-in (no firm L4 verb home yet), the promotion route being a firm `waveguide_mode_reduce` verb chapter.
```

### SUMMARY edit — `book/src/SUMMARY.md` (3 entries, after the `sparameters` block, last in output-product)

```edit:book/src/SUMMARY.md
[old]:
  - [sparameters — L4 composition-root](./feature/sparameters.L4.md)
  - [sparameters — L1 composition-root](./feature/sparameters.L1.md)
  - [sparameters — L0 ground-truth surface](./feature/sparameters.L0.md)
# Semantic surface — calculus, rules & abstractions
[new]:
  - [sparameters — L4 composition-root](./feature/sparameters.L4.md)
  - [sparameters — L1 composition-root](./feature/sparameters.L1.md)
  - [sparameters — L0 ground-truth surface](./feature/sparameters.L0.md)
  - [waveguide-mode — L4 composition-root](./feature/waveguide-mode.L4.md)
  - [waveguide-mode — L1 composition-root](./feature/waveguide-mode.L1.md)
  - [waveguide-mode — L0 ground-truth surface](./feature/waveguide-mode.L0.md)
# Semantic surface — calculus, rules & abstractions
```

## Supporting evidence

- **`eigsolve` firm** — `book/src/L1/eigsolve.md:4` (`rank: firm`), `## Status` lines 178-188 (firm cycle-022, route-(b)). Composed via the producing boundary-mode driver column.
- **Boundary-mode driver chapters** (the producing driver this output product reduces) — `book/src/feature/boundary-mode.{L4,L1,L0}.md`, all carrying the forward-ref "the reduction into the reported waveguide-mode product is a forward-ref (no dedicated output-product column yet)" that this column homes.
- **Substrate** — `palace/drivers/boundarymodesolver.cpp:273-340` (the two readout loops), all anchors self-verified on-disk this dispatch (table in §Source-range self-verification above). The producing solve (`:201-268`) is the boundary-mode.L0 surface.
- **Pattern precedent** — `sparameters` (output-product, own reduce verb `sparameter_reduce` rough-in→firm c083) for the seed-until-own-verb-firms judgment; `eigenfrequency-qfactor` (output-product over an eigenpair family) for the per-mode reduce shape.
- **Semantic surface** — `book/src/semantics/index.md` §1.2.1 named shape groups (USE+LINK: linked, not restated; `Tensor[N]` correct for the flat dof-vector mode fields).

## Open questions / caveats

- **`waveguide-mode-reduce-needs-l4-verb-home`** (record/verb-home obligation) — the per-mode reduce verb `waveguide_mode_reduce` has no firm L4 verb chapter (`L4/waveguide_mode_reduce.md`). Its per-mode constituents (`GetPropagationConstant` un-transform, `ApplyVDBackTransform`, `ComputePoyntingPower` normalization, `Bz = curl/(iω)`) are read at L0 sites and could be mined into a firm verb (analogous to `sparameter_reduce` / `eigenfreq_qfactor_reduce`). This is the promotion gate: once `waveguide_mode_reduce` firms, the `waveguide-mode` column promotes `seed`→`firm` (and the index-cell + group-intro flip in the same dispatch, per the index-cell-drift guard). DISPATCH a combinator-miner / harvester pass for the verb.
- **`record-WaveguideModeTable-needs-definition-home`** (record-definition obligation, ≥2-consumer bar) — the output record, named **`WaveguideModeTable`** consistently across all 3 waveguide-mode chapters (the canonical reduced-product record name, settled this dispatch over the earlier dual `WaveguideModeResult`), is named in signatures across the 3 waveguide-mode chapters (and cross-named `BoundaryModeResult` in the 3 boundary-mode chapters owned by D2), so it clears the ≥2-consumer bar for a `book/src/concepts/<record>.md` record-definition page. Its fields: `kn : Complex`, `n_eff : Complex`, `Et : Tensor[N_nd, complex]`, `En : Tensor[N_h1, complex]`, `Bz : Maybe (Tensor[N_curl, complex])`. The L0 backing is the per-mode observables `MeasureAndPrintAll` records (`postoperator` measurement cache) + the raw `et`/`en`/`bz` ComplexVectors on the 2D-submesh spaces. FLAG for a record-definition concept page (note: the boundary-mode chapters currently use the name `BoundaryModeResult` — the record-definition page should reconcile that cross-name to the canonical `WaveguideModeTable` for the reduced product, distinct from the raw `EigResult` the driver returns).
- **`waveguide-mode-vs-eigenfreq-qfactor-shared-eigsolve-corner`** (non-blocking observation) — both `waveguide-mode` and `eigenfrequency-qfactor` reduce an eigenpair family produced via the `eigsolve` corner; `waveguide-mode` over the boundary-mode (2D-submesh) driver, `eigenfreq-qfactor` over the eigenmode (3D-domain) driver. The reduce verbs differ in OUTPUT shape (mode-fields-table vs scalar-`(f,Q)`-table) — they are sibling reduce verbs, NOT a single shared verb (the same do-NOT-over-unify discipline the c074 D6 Gram-vs-projection guard applies). No merge proposed; recorded so a future combinator-miner does not force-unify them.
- **Boundary-mode chapter-body promotion is owned by D2** (the co-dispatched boundary-mode dispatch this cycle), per the single-index-owner coordination: I own the `feature/index.md` cell + the sibling-status reflection (index edits 3/4/5) reflecting boundary-mode's now-cleared gate; D2 owns the boundary-mode `## Status` + frontmatter `rank:`/`feature_root:` flips in the 3 boundary-mode chapter bodies. If D2 does NOT land this cycle, the index-cell calling boundary-mode `firm` will lead its chapter `## Status` (the index-cell-drift the guard warns of) — flag for finalize to reconcile (either both land or both defer).
