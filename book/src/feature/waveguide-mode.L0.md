---
kind: feature-surface
feature: waveguide-mode
level: L0
feature_root: seed
rank: firm
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

`firm` — the L0 ground-truth surface for the waveguide-mode output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L0 surface of the readout reduction that the [`boundary-mode.L0`](./boundary-mode.L0.md) driver carries as a forward-ref. **Promoted `rough-in` → `firm` (reconciled to the cycle-118 D5 column flip):** the column's own reduce verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firmed c118 D5 (OQ `waveguide-mode-reduce-needs-l4-verb-home` RESOLVED), so the OWN-COMPOSITION promotion gate cleared and the [waveguide-mode.L4](./waveguide-mode.L4.md) + [waveguide-mode.L1](./waveguide-mode.L1.md) chapters promoted `rough-in` → `firm`; this L0 ground-truth surface is reconciled to that firm reality. **`feature_root: seed` is KEPT** (the permanent GC-root marker, NOT a maturity rung — the column is a reachability root). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`, self-verified on-disk (the propagation-constant report loop `:273-277`, the mode-field readout loop `:292-334` with `GetEigenvector` `:297`, `ApplyVDBackTransform` `:300`, `ComputePoyntingPower` `:304`, the power-normalization `:305-307`, `MeasureAndPrintAll` `:314`, the `IsPropagating` branch + `Bz` formation `:316-333`, the return `:339-340`). The load-bearing structural fact at L0: the waveguide-mode product is a pair of **pure post-processing readout loops** over the converged eigenpair family — NOT a solve-iteration (the driver's only outer loops). The chapter's evidence IS the driver-source range + the per-stage site map (the adapted surface-or-evidence form for the feature-surface kind).
