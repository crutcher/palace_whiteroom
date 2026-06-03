---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T16:40:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T17:10:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "boundary-mode driver-leaf feature column"

## Critique

This is a FEATURE-SURFACE composition-root report (leaf feature column, `status: seed`), so the adapted checklist applies: rotation-quality and variant-axis-coverage are formal no-ops for the kind; surface-or-evidence is adapted to L0-driver-range + constituent down-links; cross-reference-integrity is load-bearing.

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` on CYCLE.md (28 ok / 0 failing on bounds + path-hygiene) and spot-verified the load-bearing anchors both on-disk (direct `sed`/`awk` against `reference/palace`) and via `palace-codemap read_range`. The bulk of the citations are correct on-disk: `eigen->Solve()` = `modeeigensolver.cpp:477` (CONFIRMED on-disk AND via codemap — see drift note below), `main.cpp:276-278` BOUNDARYMODE dispatch (confirmed), `BoundaryModeSolver::Solve` body `boundarymodesolver.cpp:201-341` (confirmed, file is 343 lines, body close at `:341`), `ExtractBoundary2DSubmesh` `:42-55` (confirmed), `Preprocess` `:84` (confirmed), direct-2D bypass `:87-92` (confirmed), extraction call `:141` (confirmed), `which_eig` `:232-233` + `eig(...)` ctor `:234` (confirmed), `sigma = -kn_target²` `:267` (confirmed), `eig.Solve(omega, sigma)` `:268` (confirmed), `eig.GetPropagationConstant(i)` `:299` (confirmed), readout loops `:273` / `:292` (confirmed), `ApplyVDBackTransform` `:300` / `MeasureAndPrintAll` `:314` / `MeasureFinalize` `:337` / return `:339-340` (confirmed), config struct `configfile.hpp:856-890` + parse `configfile.cpp:1390` (confirmed), hpp class `:15-28` / ctor `:78-82` (confirmed), `modeeigensolver.cpp` `:395`/`:432`/`:470`/`:481` and `modeeigensolver.hpp:96-270` (all confirmed). HOWEVER, two `kn_target` citations in the L0 chapter (stage 2) DRIFT: see Issues #1.

**surface-or-evidence — pass.** Adapted feature-surface form. The composition is supported: the L0 driver range `boundarymodesolver.cpp:201-341` is cited and backs the feature, and the two solve-side constituent down-links resolve. Verified on-disk that all four constituents are `firm`: `book/src/L4/eigsolve.md` (`firm` — opaque-library cap), `book/src/L1/eigsolve.md` (`firm`, cycle-022 route-(b)), `book/src/L4/fe_assemble.md` (`firm`), `book/src/L1/fe_assemble.md` (`firm`) — the report's firmness claim is accurate. The opaque-library eigen-iteration cross-reference to `eigenmode` is accurate: `eigenmode.L4.md` describes itself as "the cleanest test of the composition-root pattern over a single black-box-kernel constituent" with no `solve_family`/`fold_solve`, the same `eigsolve` opaque corner — so boundary-mode's "2nd clean witness, distinguished by the 2D-submesh preface" framing is faithful. The 2D-submesh distinguishing shape is real: `ExtractBoundary2DSubmesh` (`CreateFromBoundary` → `ProjectSubmeshTo2D` 3D→2D → attribute remaps) at `:42-55` is genuine structure absent from eigenmode. The `seed` status is justified (stage-3 readout reduces into a not-yet-authored waveguide-mode output-product column; all composed constituents firm — exactly the documented seed-retention rule). Record-definition sub-check: signatures name `BoundaryModeConfig` / `BoundaryModeResult` / `EigResult`. The report addresses this explicitly in its closing caveat — `BoundaryModeConfig` is given an in-chapter definition home (Inputs section + `configfile.hpp:856-890`), single-consumer; `EigResult` is defined at the constituent `L1/eigsolve`; no flag needed. Defensible.

**rotation-quality — pass (not applicable to feature-surface kind).** A composition-root rotates nothing; it recomposes already-firm vocabulary outward. Formal no-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind, but the report exceeds the bar anyway).** Formal no-op for the kind. The report nonetheless documents two variant axes (mesh-source `3D-boundary-extracted | direct-2D`; shift-target `auto | target-n_eff`) and shows where each is absorbed — both covered, no hidden branch.

**cross-reference-integrity — pass.** Load-bearing for this kind. All constituent down-links resolve on disk (`book/src/L4/fe_assemble.md`, `book/src/L4/eigsolve.md`, `book/src/L1/fe_assemble.md`, `book/src/L1/eigsolve.md`); the sibling cross-links resolve (`eigenmode.{L4,L1,L0}.md`, `driven.L4.md`, `frequency_sweep.md`, `design/l4_calculus.md`). Maturity claims match on-disk Status (all four constituents `firm`; a `seed` feature column composing firm constituents is correct — the column stays `seed` for the readout-product forward-ref, not a constituent gap). The D1 deferral is correctly executed: the report touches ONLY its 3 chapter files + its own `driver-leaf.md` bullet; it does NOT touch `feature/index.md` matrix or the `SUMMARY.md` feature block (those are explicitly deferred to D1 with the c074/c075 parallel-blind-shared-index precedent). The `driver-leaf.md` edit anchors both match the on-disk file exactly; the `boundary-mode` bullet is inserted before `driven` = alpha-FIRST (boundary < driven < eigenmode < electrostatic < magnetostatic < transient), correct; the "5 drivers"→"6 drivers" count update and the line-13 "planned" de-stale are both applied.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a composition-root, not a lowering theme). The "Lifts to" / "L1 vs L4" prose discusses the correct direction (L0 lifts up to L1/L4; high→low chapter discipline preserved — the L1>L0 mutation lifts are correctly delegated to the constituent ops' themes, not authored here).

**plan-kind-consistency — pass.** The content shape matches a `seed` driver-leaf feature column: composition-root prose, constituent down-link tables, no new per-op algebraic claim, links DOWN. The `kind: feature-surface` frontmatter + uniform `status: seed` token (no `(exemplar)`/`(composition-root)` qualifier) are correct for the kind. Lands in the driver-leaf by-kind grouping alpha-FIRST, consistent with the FEATURE-SURFACE SPINE driver-leaf sub-kind.

**skill-uptake-survey — pass.** The report references its localization procedure (palace-codemap `read_range` → `citecheck --anchor` + direct END-line reads) and the on-disk-authoritative re-anchoring practice. Pure telemetry; no blocking concern.

### Issues found

**Issue #1 — kn_target citation drift in `boundary-mode.L0.md` stage 2 (citation-validity, warning).** In the `new:book/src/feature/boundary-mode.L0.md` block, stage 2 (CYCLE.md line 207) cites:
- "`kn_target = bm.target * omega` when a target effective index is given (`:262`)" — on-disk, line `:262` is a bare `}`; the actual `kn_target = bm.target * omega;` is at **`:251`**.
- "auto-computed ... `kn_target = omega / c_min * sqrt(1.1)` (`:265`)" — on-disk, line `:265` is `BlockTimer bt1(Timer::EPS);`; the actual `kn_target = omega / c_min * std::sqrt(1.1);` is at **`:260`**.

Both are in-range (so `citecheck --scan` bounds-pass) but point at the wrong content — confirmed via `citecheck --anchor 'kn_target'` (`:262` → DRIFT, nearest token at 261; `:265` → DRIFT, nearest token at 267) and direct `grep -n kn_target` (true sites 251 / 260). The same wrong pair (`:262`/`:265`) is repeated in the Supporting-evidence bullet (CYCLE.md line 258, "`kn_target` branch `:262`/`:265`"). Note: the `kn_target` block is bracketed by an `if (bm.target > 0.0)` / `else` (lines ~250–261) — the correct cite for the *branch* selection would be the `if` at ~`:250`, and the two assignment lines are `:251` (target) and `:260` (auto). The drift is localized to the L0 chapter + supporting evidence; the L4/L1 chapters do not cite these specific lines (their variant-axis section cites `:267` for the sigma line, which is correct). Suggested corrections: `:262`→`:251`, `:265`→`:260`.

**Issue #2 — informational, not a defect (codemap drift OQ may not reproduce).** The report's OQ `modeeigensolver-readrange-minus-one-drift-witness` claims `palace-codemap read_range` reported `eigen->Solve()` at `:476` (a -1 drift) vs on-disk `:477`. On THIS critique's `read_range` query (`modeeigensolver.cpp:475-478`), the codemap returned content byte-identical to the on-disk `sed` read — `int num_conv = eigen->Solve();` at line 477 — i.e. no drift reproduced here. The report's emitted citation (`:477`) is correct on-disk either way, so this does not affect citation-validity; flagging only that the OQ's drift-witness claim is not reproducible from this seat (the OQ is informational, so harmless, but the repairer/integrator should not treat the -1-drift claim as a settled finding).

## Repair

### Fixes attempted

- **Finding (Issue #1)**: `kn_target` citation drift in `boundary-mode.L0.md` stage 2 — `:262` cited for `kn_target = bm.target * omega` (actual `:251`; `:262` is a bare `}`); `:265` cited for the auto-compute `kn_target = omega / c_min * sqrt(1.1)` (actual `:260`; `:265` is `BlockTimer bt1(Timer::EPS);`). Same wrong pair recurs in the Supporting-evidence bullet.
  - **Decision**: repaired.
  - **Action**: re-anchored `:262`→`:251` and `:265`→`:260` at BOTH sites — (i) the `new:book/src/feature/boundary-mode.L0.md` stage-2 chapter content (CYCLE.md §"The composition, in source" stage 2) and (ii) the Supporting-evidence bullet ("`kn_target` branch `:251`/`:260`"). Line numbers verified on-disk first via direct Read of `reference/palace/palace/drivers/boundarymodesolver.cpp:245-269`: line 251 = `kn_target = bm.target * omega;`, line 260 = `kn_target = omega / c_min * std::sqrt(1.1);` — matching the critic's `:251`/`:260` exactly. This is a small content/anchor-drift offset fix (a few lines slip within the `if`/`else` block), squarely in repair scope. The `:267` sigma cite and all other anchors were already correct (critic confirmed) and were not touched.

- **Finding (Issue #2)**: codemap `-1`-drift OQ on `modeeigensolver.cpp` (`eigen->Solve()` at `:476` claimed vs on-disk `:477`) did not reproduce from the critic's seat.
  - **Decision**: not-needed (informational; no defect). The emitted `:477` citation is correct on-disk; the OQ is a not-settled drift-witness left as-is per the critic's note. No edit.

### Unrepairable findings

None. The single warning was a mechanical citation re-anchor, applied.

## Suggested resolution

`ready` — the lone citation-validity warning (the `kn_target` `:262`/`:265` → `:251`/`:260` drift) is repaired at both sites, with the corrected line numbers verified on-disk. All other checks passed at critique. Integrator note: the `modeeigensolver-readrange-minus-one-drift-witness` OQ is an informational not-settled witness (the `-1` drift did not reproduce from the critic's seat); promote it as an OQ but do not treat the drift claim as a confirmed finding. D1 (cohort owner) still owns the `feature/index.md` matrix row + the `SUMMARY.md` feature-block entry for `boundary-mode` (correctly deferred here per the parallel-blind-shared-index guard).
