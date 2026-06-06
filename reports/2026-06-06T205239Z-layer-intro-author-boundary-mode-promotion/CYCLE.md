---
agent: layer-intro-author
invoked_at: 2026-06-06T205239Z
scope: feature/boundary-mode column promotion off seed (cycle-117 D2, WAVE-2)
status: integrated
integrated_at: 2026-06-06T214845Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-117 D2 (apply-order 5/5, LAST). boundary-mode driver-leaf column rank rough-in->FIRM across 3 chapter bodies (feature_root: seed KEPT as the permanent GC-root marker, matching the eigenmode.L4 precedent) + live waveguide-mode sibling cross-links. Both-land coupling with D1 RESOLVED (D1's firm index-cell + D2's chapter-body flip now match -- no index-cell drift). All per-report gates PASS; rank firm rests on firm fe_assemble+eigsolve (no violation); the waveguide-mode reference edges are sibling references not blockers (OWN-COMPOSITION). 0 new OQs. Non-blocking citecheck: 3 MISS were cross-report ...-elided provenance prose, not landed citations."
---

# CYCLE: boundary-mode driver-leaf column promotion off `seed`

## Summary

Promote the **`boundary-mode` driver-leaf feature column off `seed`** under the OWN-COMPOSITION rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; user directive 2026-06-03; memory `project_feature_column_promotion_rule`). This is cycle-117 D2 (WAVE-2), depending on D1 (WAVE-1) which authored the `waveguide-mode` 6th output-product column — the home for boundary-mode's stage-(3) readout reduction.

Boundary-mode's directly-owned constituents are all firm on disk:
- `fe_assemble` (×2 — the `(A, B)` GEP block-pencil assemble) — `L4/fe_assemble` **firm**, `L1/fe_assemble` **firm**;
- `eigsolve` (the single opaque black-box eigen-solve) — `L4/eigsolve` **firm**, `L1/eigsolve` **firm**;
- the per-mode readout — its reduction is now homed in D1's `waveguide-mode` output-product column.

Under the OWN-COMPOSITION rule its **own-readout gate is cleared**: the readout reduction is no longer an unhomed directly-owned constituent (D1 homed it in the `waveguide-mode` column). The `waveguide-mode` column is a **cross-linked SIBLING reference, NOT a blocking constituent** (the output-product↔driver reciprocal cross-link drift-guard) — so the fact that `waveguide-mode` itself is `seed` (its own reduce verb `waveguide_mode_reduce` is rough-in) does NOT block boundary-mode. Boundary-mode promotes on its OWN firm composition.

**Promotion mechanics** (matching the promoted-sibling convention — read `feature/eigenmode.L4.md:5-6`): `feature_root: seed` is the **permanent root-set marker** (NOT a maturity), kept unchanged; the maturity is carried by `rank:`, flipped `rough-in` → `firm`; and the body `## Status` token flips `seed` → `firm`. (D1's own note `reports/.../waveguide-mode/CYCLE.md:333` explicitly records "promoted `seed`→`firm` c117" for boundary-mode and "its `feature_root: seed` is the permanent root marker, not a maturity".)

This dispatch edits ONLY the three `boundary-mode.{L4,L1,L0}.md` chapter bodies + frontmatter. **D1 sole-owns `feature/index.md` + `feature/SUMMARY.md`** this cycle (it already applied the boundary-mode index-cell delta — index reflecting 12 firm / 1 seed); per the both-land-or-both-defer flag D1 raised, landing these chapter-body flips this cycle keeps the index cell from leading the chapter `## Status` (the index-cell-drift guard).

Also replaces the boundary-mode L1/L0 plain-text waveguide-mode **forward-ref** ("the reduction into the reported waveguide-mode product is a forward-ref, no dedicated output-product column yet") with a **live cross-link** to D1's `waveguide-mode.{L4,L1,L0}` files (canonical slug `waveguide-mode`), and adds the reciprocal `reference` frontmatter edge to the sibling output-product column.

## Proposed changes

### 1. `book/src/feature/boundary-mode.L4.md`

#### 1a. Frontmatter: rank flip + sibling reference edge

```edit:book/src/feature/boundary-mode.L4.md
[old]: feature_root: seed
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
[new]: feature_root: seed
rank: firm
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
    - feature/waveguide-mode.L4           # SIBLING output-product cross-link (reciprocal drift-guard) — homes this driver's stage-(3) readout reduction; a reference, NOT a blocking constituent (OWN-COMPOSITION rule)
```

#### 1b. Stage-(3) readout: forward-ref → live waveguide-mode cross-link

```edit:book/src/feature/boundary-mode.L4.md
[old]: 3. **Per-mode readout map → the physical product** — a pure `map` over the already-converged eigenpair set, recovering each mode's physical observables: the propagation constant `kn` (from the eigenvalue, via the shift-invert un-transform), the effective index `n_eff = kn / ω`, the transverse + longitudinal mode fields `(Et, En)` (the VD back-transform of the eigenvector), and the longitudinal magnetic field `Bz = curl(Et)/(iω)` (for propagating modes). This is the boundary-mode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (the same non-membership the [`eigenmode`](./eigenmode.L4.md) driver records). L0: the propagation-constant report loop `for (int i = 0; i < num_conv; i++)` (`palace/drivers/boundarymodesolver.cpp:273`), the per-mode readout loop `for (int i = 0; i < n_print; i++)` (`:292`), the VD back-transform `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`), the power-normalization (`:304`), the `Bz` formation for propagating modes (`:316`), and `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`).
[new]: 3. **Per-mode readout map → the physical product** — a pure `map` over the already-converged eigenpair set, recovering each mode's physical observables: the propagation constant `kn` (from the eigenvalue, via the shift-invert un-transform), the effective index `n_eff = kn / ω`, the transverse + longitudinal mode fields `(Et, En)` (the VD back-transform of the eigenvector), and the longitudinal magnetic field `Bz = curl(Et)/(iω)` (for propagating modes). This per-mode reduction is the **stage-(3) post-process homed in the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column** (the `waveguide_mode_reduce` reduce verb) — a SIBLING cross-link (the output-product↔driver reciprocal drift-guard), NOT a blocking constituent. This is the boundary-mode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (the same non-membership the [`eigenmode`](./eigenmode.L4.md) driver records). L0: the propagation-constant report loop `for (int i = 0; i < num_conv; i++)` (`palace/drivers/boundarymodesolver.cpp:273`), the per-mode readout loop `for (int i = 0; i < n_print; i++)` (`:292`), the VD back-transform `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`:300`), the power-normalization (`:304`), the `Bz` formation for propagating modes (`:316`), and `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`).
```

#### 1c. "Why this composes" — the readout-map cross-link

```edit:book/src/feature/boundary-mode.L4.md
[old]: - The readout (stage 3) is a pure `map` over the converged modes.

Both composed solve-side combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**. Under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers), the firm solve corner is not sufficient here: this column stays `seed` on its **own-readout gate** — its directly-owned stage-(3) readout reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). The gate is a directly-owned constituent (the column's own readout reduction), NOT a sibling-column reference; authoring a firm waveguide-mode reduction is the promotion route.
[new]: - The readout (stage 3) is a pure `map` over the converged modes, homed in the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column.

Both composed solve-side combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**, and the stage-(3) readout reduction is now homed in the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column (authored cycle-117). Under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers), **this column is firm**: its directly-owned constituents — the [`fe_assemble`](../L4/fe_assemble.md) block-pencil assemble (firm), the [`eigsolve`](../L4/eigsolve.md) black-box eigen-solve (firm), and its per-mode readout (now homed in the `waveguide-mode` column) — are all firm. The cross-link to the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column is a **SIBLING reference (the reciprocal drift-guard), NOT a blocking constituent** — so the fact that `waveguide-mode` is itself `seed` (its own reduce verb `waveguide_mode_reduce` is rough-in) does NOT block boundary-mode (exactly as the [`eigenmode`](./eigenmode.L4.md) sibling promotes independent of its `eigenfrequency-qfactor` cross-link).
```

#### 1d. Constituent down-link table — readout row

```edit:book/src/feature/boundary-mode.L4.md
[old]: | per-mode readout (kn, n_eff, Et, En, Bz) | *(waveguide-mode product reduction; forward-ref — no output-product column yet)* | (forward-ref) | `boundarymodesolver.cpp:273-334` |
[new]: | per-mode readout (kn, n_eff, Et, En, Bz) | [`waveguide-mode`](./waveguide-mode.L4.md) (`waveguide_mode_reduce`) — SIBLING output-product column | (sibling ref) | `boundarymodesolver.cpp:273-334` |
```

#### 1e. `## Status` — token flip + promotion prose

```edit:book/src/feature/boundary-mode.L4.md
[old]: `seed` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. The solve corner is firm — stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble, stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (with NO `solve_family` map and NO `fold_solve` state-march, the minimal solve shape eigenmode established), stage (0) is the distinguishing 2D-submesh preface — but this column **stays `seed`** on an **own-readout gate**: its directly-owned stage-(3) readout (a pure per-mode `map`) reduces into a user-facing **waveguide-mode output product that has no firm home** (no dedicated output-product column / no firm reduction verb exists yet; the waveguide-mode product column is demand-gated). This is a directly-owned constituent gate (the column's own readout reduction), NOT a sibling-column reference — so unlike its eigenmode sibling (which promotes because its reduction is owned by a *separate* `eigenfrequency-qfactor` cross-linked column), boundary-mode's readout reduction is its own unhomed constituent; authoring a firm waveguide-mode reduction is the promotion route. This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk, plus the firm constituent down-links.
[new]: `firm` — the **6th per-driver feature-surface composition-root** (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the alpha-first column in the driver-leaf grouping, and the **second clean witness of the composition-root pattern over a single opaque-library black-box eigen-iteration** (the SAME [`eigsolve`](../L4/eigsolve.md) corner as [`eigenmode`](./eigenmode.L4.md), distinguished by the 2D-submesh extraction preface). **Promoted `seed`→`firm` cycle-117 under the OWN-COMPOSITION promotion rule** (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; user directive 2026-06-03; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers. Its directly-owned constituents are all firm — stage (1) is the [`fe_assemble`](../L4/fe_assemble.md) GEP block-pencil assemble (**firm**), stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (**firm**, with NO `solve_family` map and NO `fold_solve` state-march, the minimal solve shape eigenmode established), stage (0) is the distinguishing 2D-submesh preface, and the stage-(3) per-mode readout reduction is now **homed in the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column** (authored cycle-117 by the WAVE-1 dispatch, which fired its demand-gate under the post-consolidation open-all-feature-fronts wave, user directive 2026-06-06). The cycle-085 re-eval held this column at `seed` on an **own-readout gate** (its readout reduction had no firm home — no dedicated output-product column existed); cycle-117 **cleared that gate** by homing the readout reduction in the new `waveguide-mode` column, so the readout is no longer an unhomed directly-owned constituent. The cross-link to the [`waveguide-mode`](./waveguide-mode.L4.md) output-product column is a **SIBLING reference (the reciprocal drift-guard), NOT a blocking constituent** — so the fact that `waveguide-mode` is itself `seed` (its own reduce verb `waveguide_mode_reduce` is rough-in) does NOT block boundary-mode, exactly as the [`eigenmode`](./eigenmode.L4.md) sibling promotes independent of its `eigenfrequency-qfactor` cross-link. (`feature_root: seed` in the frontmatter is the permanent root-set marker, NOT a maturity; the maturity is carried by `rank: firm`.) This chapter carries the *compositional* claim (boundary-mode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). The `BoundaryModeSolver` is a 6th `ProblemType` dispatch branch that routes through the same `switch` as the 5 drivers (`palace/main.cpp:276-278`), so it is a co-equal leaf driver column. Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` (`BoundaryModeSolver::Solve`) realizing the composition, all anchors confirmed on-disk, plus the firm constituent down-links.
```

### 2. `book/src/feature/boundary-mode.L1.md`

#### 2a. Frontmatter: rank flip + sibling reference edge

```edit:book/src/feature/boundary-mode.L1.md
[old]: feature_root: seed
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
[new]: feature_root: seed
rank: firm
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
    - feature/waveguide-mode.L1           # SIBLING output-product cross-link (reciprocal drift-guard) — homes this driver's stage-(3) readout reduction; a reference, NOT a blocking constituent (OWN-COMPOSITION rule)
```

#### 2b. Output — forward-ref → live waveguide-mode cross-link

```edit:book/src/feature/boundary-mode.L1.md
[old]: - **Output — the physical product.** `BoundaryModeResult` — the set of converged propagation modes, each carrying `kn`, `n_eff`, `(Et, En)`, and (for propagating modes) `Bz`. The reduction into the reported waveguide-mode product is a forward-ref (no dedicated output-product column yet). L0: the per-mode `kn`/`(et, en)` measured by `post_op.MeasureAndPrintAll(...)` (`palace/drivers/boundarymodesolver.cpp:314`).
[new]: - **Output — the physical product.** `BoundaryModeResult` — the set of converged propagation modes, each carrying `kn`, `n_eff`, `(Et, En)`, and (for propagating modes) `Bz`. The reduction into the reported waveguide-mode product is homed in the [`waveguide-mode`](./waveguide-mode.L1.md) output-product column (a SIBLING cross-link, the reciprocal drift-guard). L0: the per-mode `kn`/`(et, en)` measured by `post_op.MeasureAndPrintAll(...)` (`palace/drivers/boundarymodesolver.cpp:314`).
```

#### 2c. Constituent down-link table — readout row

```edit:book/src/feature/boundary-mode.L1.md
[old]: | per-mode readout (kn, n_eff, Et, En, Bz) | *(waveguide-mode product reduction; forward-ref — no output-product column yet)* | (forward-ref) | `boundarymodesolver.cpp:273-334` |
[new]: | per-mode readout (kn, n_eff, Et, En, Bz) | [`waveguide-mode`](./waveguide-mode.L1.md) (`waveguide_mode_reduce`) — SIBLING output-product column | (sibling ref) | `boundarymodesolver.cpp:273-334` |
```

#### 2d. `## Status` — token flip + promotion prose

```edit:book/src/feature/boundary-mode.L1.md
[old]: `seed` — the L1 pure-function composition root for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [boundary-mode.L4](./boundary-mode.L4.md) composition root and the L1 sibling of the [eigenmode.L1](./eigenmode.L1.md) driver (the SAME opaque eigensolver-as-operator solve corner, distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)), but the column **stays `seed`** on an **own-readout gate** — its directly-owned stage-3 readout reduces into a not-yet-authored waveguide-mode output-product reduction (no firm home; the waveguide-mode product column is demand-gated). The gate is the column's own readout constituent, NOT a sibling-column reference — so authoring a firm waveguide-mode reduction is the promotion route. The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, e0)` destination write, the `bz.Real() *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm L1 constituent down-links.
[new]: `firm` — the L1 pure-function composition root for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [boundary-mode.L4](./boundary-mode.L4.md) composition root and the L1 sibling of the [eigenmode.L1](./eigenmode.L1.md) driver (the SAME opaque eigensolver-as-operator solve corner, distinguished by the 2D-submesh extraction preface). **Promoted `seed`→`firm` cycle-117 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): BOTH composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`eigsolve`](../L1/eigsolve.md)), and the stage-3 readout reduction is now **homed in the [`waveguide-mode`](./waveguide-mode.L1.md) output-product column** (authored cycle-117). The cycle-085 re-eval held this column at `seed` on an **own-readout gate** (its readout reduction had no firm home); cycle-117 **cleared that gate** by homing the readout in the new `waveguide-mode` column, so the readout is no longer an unhomed directly-owned constituent. The cross-link to the [`waveguide-mode`](./waveguide-mode.L1.md) output-product column is a **SIBLING reference (the reciprocal drift-guard), NOT a blocking constituent** — so the fact that `waveguide-mode` is itself `seed` (its own reduce verb `waveguide_mode_reduce` is rough-in) does NOT block boundary-mode, exactly as the [eigenmode.L1](./eigenmode.L1.md) sibling promotes independent of its `eigenfrequency-qfactor` cross-link. (`feature_root: seed` in the frontmatter is the permanent root-set marker, NOT a maturity; the maturity is carried by `rank: firm`.) The defining structural fact carried from L4: a single opaque eigensolver-as-operator application, with NO RHS family-map and NO value-threaded outer solve loop. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The L1→L0 direction (how each pure operator lowers to the in-place driver writes — the `GetEigenvector(i, e0)` destination write, the `bz.Real() *= ...` accumulations) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline). Evidence: the L0 driver range `boundarymodesolver.cpp:201-341` realizing the composition, all anchors confirmed on-disk this dispatch, plus the firm L1 constituent down-links.
```

### 3. `book/src/feature/boundary-mode.L0.md`

#### 3a. Frontmatter: rank flip + sibling reference edge

```edit:book/src/feature/boundary-mode.L0.md
[old]: feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: palace/drivers/boundarymodesolver.cpp:201-341
      kind: cites-evidence
    - target: palace/drivers/boundarymodesolver.hpp:15-28
      kind: cites-evidence
    - target: palace/main.cpp:276-278
      kind: cites-evidence
  reference:
    - feature/boundary-mode.L1
[new]: feature_root: seed
rank: firm
edges:
  depends-on:
    - target: palace/drivers/boundarymodesolver.cpp:201-341
      kind: cites-evidence
    - target: palace/drivers/boundarymodesolver.hpp:15-28
      kind: cites-evidence
    - target: palace/main.cpp:276-278
      kind: cites-evidence
  reference:
    - feature/boundary-mode.L1
    - feature/waveguide-mode.L0           # SIBLING output-product cross-link (reciprocal drift-guard) — homes this driver's stage-(3) readout reduction; a reference, NOT a blocking constituent (OWN-COMPOSITION rule)
```

#### 3b. Stage-4 readout — forward-ref → live waveguide-mode cross-link

```edit:book/src/feature/boundary-mode.L0.md
[old]: The readout loop closes at `:334`; `post_op.MeasureFinalize(indicator)` (`:337`) finalizes. This is the L0 site the L1/L4 per-mode readout map lifts — feeding the waveguide-mode **output product** (whose reduction has no dedicated output-product column yet; forward-ref).
[new]: The readout loop closes at `:334`; `post_op.MeasureFinalize(indicator)` (`:337`) finalizes. This is the L0 site the L1/L4 per-mode readout map lifts — feeding the waveguide-mode **output product**, whose reduction is homed in the [`waveguide-mode`](./waveguide-mode.L0.md) output-product column (a SIBLING cross-link, the reciprocal drift-guard).
```

#### 3c. Output — forward-ref → live waveguide-mode cross-link

```edit:book/src/feature/boundary-mode.L0.md
[old]: - **Output — the physical product.** The per-mode propagation constant `kn` (`eig.GetPropagationConstant(i)`, `:299`), effective index `n_eff = kn/omega` (`:276-277`), transverse + longitudinal mode fields `(et, en)`, and (propagating modes) `Bz`, measured by `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`). The reduction into the reported waveguide-mode product has no dedicated output-product column yet (forward-ref).
[new]: - **Output — the physical product.** The per-mode propagation constant `kn` (`eig.GetPropagationConstant(i)`, `:299`), effective index `n_eff = kn/omega` (`:276-277`), transverse + longitudinal mode fields `(et, en)`, and (propagating modes) `Bz`, measured by `post_op.MeasureAndPrintAll(i, et, en, kn, omega, error_abs, error_bkwd, n_print)` (`:314`). The reduction into the reported waveguide-mode product is homed in the [`waveguide-mode`](./waveguide-mode.L0.md) output-product column (a SIBLING cross-link, the reciprocal drift-guard).
```

#### 3d. `## Status` — token flip + promotion prose

```edit:book/src/feature/boundary-mode.L0.md
[old]: `seed` — the L0 ground-truth surface for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the 6th driver-leaf column and the L0 sibling of the [eigenmode.L0](./eigenmode.L0.md) driver (the SAME opaque-library black-box eigen-iteration corner, distinguished by the 2D-submesh extraction preface). **Re-evaluated cycle-085 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): the solve corner is firm (`fe_assemble`, `eigsolve`), but the column stays `seed` on an own-readout gate — its directly-owned readout reduces into a waveguide-mode output product with no firm home yet (the waveguide-mode product column is demand-gated; unlike eigenmode, this driver's reduction is its OWN unhomed constituent, not a separate cross-linked output-product column). Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`
[new]: `firm` — the L0 ground-truth surface for the boundary-mode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the 6th driver-leaf column and the L0 sibling of the [eigenmode.L0](./eigenmode.L0.md) driver (the SAME opaque-library black-box eigen-iteration corner, distinguished by the 2D-submesh extraction preface). **Promoted `seed`→`firm` cycle-117 under the OWN-COMPOSITION promotion rule** (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers): the solve corner is firm (`fe_assemble`, `eigsolve`), and the stage-(3) readout reduction is now **homed in the [`waveguide-mode`](./waveguide-mode.L0.md) output-product column** (authored cycle-117) — the cycle-085 own-readout gate (the readout reduction had no firm home) is **cleared**, so the readout is no longer an unhomed directly-owned constituent. The cross-link to the [`waveguide-mode`](./waveguide-mode.L0.md) output-product column is a SIBLING reference (the reciprocal drift-guard), NOT a blocking constituent — so the fact that `waveguide-mode` is itself `seed` (its own reduce verb is rough-in) does NOT block boundary-mode. (`feature_root: seed` in the frontmatter is the permanent root-set marker, NOT a maturity; the maturity is carried by `rank: firm`.) Every stage is a cited range into `palace/drivers/boundarymodesolver.cpp`
```

## Supporting evidence

### Clean-gate: on-disk firm-status of boundary-mode's OWN directly-owned constituents

All four constituents read directly from their `## Status` lines / `rank:` frontmatter on disk this dispatch (per the survey-firmness-from-on-disk-status discipline):

- **`book/src/L4/fe_assemble.md:171-173`** — `## Status` line reads: ``` `firm` — the `foldr`-producing-a-sum combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` ... ``` (the firm-on-positive-structure escape; all five combinator laws are read-off syntactic identities). **firm.**
- **`book/src/L4/eigsolve.md:176-178`** — `## Status` line reads: ``` `firm` — the `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_state` ... (the cap is firm *as a cap*; the obstruction it carries is the same one L3 carries) ```. **firm.**
- **`book/src/L1/fe_assemble.md:15`** — frontmatter `rank: firm`. **firm.**
- **`book/src/L1/eigsolve.md:4`** — frontmatter `rank: firm`. **firm.**

The stage-(3) per-mode readout — the 4th directly-owned constituent — is homed in D1's `waveguide-mode` output-product column (cycle-117). It is no longer an unhomed directly-owned constituent (the cycle-085 own-readout gate is cleared). The `waveguide-mode` column is a cross-linked SIBLING reference (the reciprocal output-product↔driver drift-guard), NOT a blocking constituent — so its own `seed` status (its reduce verb `waveguide_mode_reduce` rough-in) does NOT gate boundary-mode (OWN-COMPOSITION rule; CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; the exact analog of `eigenmode` promoting independent of its `eigenfrequency-qfactor` sibling cross-link).

**The OWN-COMPOSITION promotion is licensed:** every directly-owned constituent is firm (`fe_assemble`×2 firm, `eigsolve` firm) or homed (the readout, in the `waveguide-mode` sibling column).

### Promoted-sibling convention (the `feature_root:` / `rank:` split)

Read `book/src/feature/eigenmode.L4.md:5-6`: `feature_root: seed` (line 5) co-exists with `rank: firm` (line 6) on a promoted driver-leaf column. So `feature_root: seed` is the **permanent root-set marker** (kept unchanged), and the maturity is carried by `rank:`. The promotion flips `rank: rough-in` → `rank: firm` and the body `## Status` token `seed` → `firm`, keeping `feature_root: seed`. D1's report (`reports/.../waveguide-mode/CYCLE.md:333`) independently records this for boundary-mode ("promoted `seed`→`firm` c117" / "its `feature_root: seed` is the permanent root marker, not a maturity").

### Cross-link resolution (forward-ref → live)

D1 (WAVE-1, this cycle) proposes `book/src/feature/waveguide-mode.{L4,L1,L0}.md` (canonical slug `waveguide-mode`, confirmed `reports/.../waveguide-mode/CYCLE.md:52,150,237` — the three `edit:book/src/feature/waveguide-mode.<level>.md` proposed-changes blocks). The boundary-mode cross-links I add (`./waveguide-mode.L4.md`, `./waveguide-mode.L1.md`, `./waveguide-mode.L0.md`) resolve to those D1 files once both reports integrate this cycle.

**Integration-ordering note:** these `boundary-mode` cross-links to `waveguide-mode.*` are live `linkcheck2` links to files that D1 (not yet integrated at the time this report is read) creates. The integrator must apply D1's `waveguide-mode.*` file-creation BEFORE (or in the same finalize-rebuild as) these boundary-mode edits, else `cargo make book` fails the `linkcheck2` rebuild on the missing anchor. WAVE-2-depends-on-WAVE-1 ordering already encodes this; flagging it explicitly for finalize.

## Open questions / caveats

- **`waveguide-mode-reduce-needs-l4-verb-home`** (raised by D1) — the `waveguide-mode` output-product column itself stays `seed` because its own reduce verb `waveguide_mode_reduce` has no firm `L4/waveguide_mode_reduce.md` chapter yet. This does NOT affect boundary-mode's promotion (sibling reference, not a blocker), but it is the standing promotion route for the `waveguide-mode` column (exactly as `sparameter_reduce` was the route for `sparameters`, firm c083). Carried here as a caveat for visibility; D1 owns the OQ.
- **Index/SUMMARY ownership.** D1 sole-owns `feature/index.md` + `feature/SUMMARY.md` this cycle and has already applied the boundary-mode index-cell delta (index reflecting 12 firm / 1 seed) + the sibling-status reflection. This dispatch does NOT edit those files (the single-index-owner coordination). These chapter-body flips + D1's index-cell delta are the both-land-or-both-defer pair D1 flagged (`reports/.../waveguide-mode/CYCLE.md:421`); landing both this cycle keeps the index cell from leading the chapter `## Status` (the index-cell-drift guard).
- **Whole-`feature/` sibling-status grep** (the column-flip drift-guard): a `seed`→`firm` boundary-mode flip can stale sibling-column prose that still calls `boundary-mode` `(seed)`/`(**seed**)`. D1's `waveguide-mode.*` chapters reference `boundary-mode` as a sibling; D1 authored them THIS cycle already describing boundary-mode's gate as cleared / promoted (`reports/.../waveguide-mode/CYCLE.md:333,346` — "promoted `seed`→`firm` c117"), so D1's new chapters are NOT stale. No other on-disk `feature/` file calls `boundary-mode` `(seed)` outside the index (D1-owned) and these three chapter bodies (this dispatch). `grep -rn 'boundary-mode' book/src/feature | grep -E '\(\*?\*?seed\*?\*?\)'` should be re-run by finalize after both reports integrate to confirm zero residual stale sibling-status mentions.
