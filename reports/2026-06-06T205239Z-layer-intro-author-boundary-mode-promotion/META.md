---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T211500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of boundary-mode driver-leaf column promotion off `seed`

## Critique

This is a **feature-surface composition-root** report (driver-leaf column, `boundary-mode`), so the adapted feature-surface checklist applies (rotation-quality and variant-axis-coverage are formal no-ops; surface-or-evidence adapts to driver-range + constituent down-links; cross-reference-integrity is load-bearing). The report is a **column promotion off `seed`** (`rank: rough-in → firm`, `feature_root: seed` retained) — directive-B front (ii). 13 edit blocks across the three `boundary-mode.{L4,L1,L0}.md` bodies + frontmatter; no index/SUMMARY writes (D1-owned).

### Checks run

**citation-validity — pass.** Every `[old]` edit anchor was located verbatim on disk: the three frontmatter blocks (`boundary-mode.L4.md:5-20`, `.L1.md:5-16`, `.L0.md:5-16`), the three `## Status` blocks, and the forward-ref / down-link-table anchors all match. The load-bearing L0 source pinpoints were content-confirmed against `reference/palace/palace/drivers/boundarymodesolver.cpp` (343 lines, so `:201-341`, `:273-334`, `:314`, `:337` are all in range): `:273` = `for (int i = 0; i < num_conv; i++)`, `:292` = `for (int i = 0; i < n_print; i++)`, `:300` = `mode_op.ApplyVDBackTransform(e0, kn, et, en)`, `:314` = `post_op.MeasureAndPrintAll(...)`, `:337` = `post_op.MeasureFinalize(indicator)`. `palace/main.cpp:276-278` confirmed as the `case ProblemType::BOUNDARYMODE` dispatch branch. The constituent-firmness clean-gate citations were all confirmed (next check). No `verified_against:` block in this report, so that sub-check no-ops.

**surface-or-evidence — pass (feature-surface adaptation).** A composition-root's evidence is the L0 driver range + the constituent down-links, and this report's value is the OWN-COMPOSITION promotion, so I verified the directly-owned constituents are genuinely firm on disk: `book/src/L4/fe_assemble.md:173` reads `` `firm` `` (firm-on-positive-structure escape); `book/src/L4/eigsolve.md:178` reads `` `firm` `` (firm as a cap, carrying the L3 obstruction); `book/src/L1/fe_assemble.md:15` carries `rank: firm`; `book/src/L1/eigsolve.md:4` carries `rank: firm`. The 4th directly-owned constituent (the per-mode readout reduction) is homed by D1's `waveguide-mode` column, clearing the cycle-085 own-readout gate. The L0 driver range `boundarymodesolver.cpp:201-341` is cited and backs the composition. The `feature_root: seed` is NOT itself an unfilled record; no signature-named record lacks a home (`BoundaryModeConfig`/`BoundaryModeResult` are carried via the `uses-record` edge to the existing `concepts/config-record.md`, confirmed present on disk).

**rotation-quality — pass (not applicable to feature-surface kind).** A feature chapter rotates nothing; it recomposes already-firm vocabulary outward. No-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The column has no variant axes of its own; the axes live in the composed constituent ops (`fe_assemble` carries its assembly-representation/term-position/trial-test axes in its own chapter). No-op.

**cross-reference-integrity — pass (load-bearing for this kind).** The promotion's value is its down-links and the forward-ref → live-link swap. All same-file/intra-feature links resolve on disk (`./eigenmode.{L4,L1,L0}.md`, `../L4/fe_assemble.md`, `../L4/eigsolve.md`, `../L1/...`). The three NEW cross-link targets — `./waveguide-mode.{L4,L1,L0}.md` — do NOT yet exist on disk; they are created by D1 (WAVE-1) this cycle. I confirmed D1's report proposes exactly those three files under the canonical slug `waveguide-mode` (`reports/.../waveguide-mode/CYCLE.md:52,150,237`). Critically, I also confirmed the **maturity-overclaim guard**: D1 holds `waveguide-mode` at `status: seed` / `rank: rough-in` (its own reduce verb `waveguide_mode_reduce` is unhomed), and this report's prose correctly treats `waveguide-mode` as a `seed` SIBLING reference (NOT a blocker) — a `firm` driver column composing a `seed` sibling output-product column is the correct OWN-COMPOSITION state (exactly the `eigenmode` ↔ `eigenfrequency-qfactor` precedent). The integration-ordering caveat (D2 cross-links point at files D1 creates; finalize must apply D1's file-creation before/with D2's edits or the `linkcheck2` rebuild fails on the missing anchor) is correctly identified and flagged in §Cross-link resolution. This is an integration-sequencing constraint for finalize, not a defect in the report. No stale sibling-status mention was found: `grep` over `book/src/feature` for `boundary-mode` `(seed)` outside the three chapter bodies returns nothing (D1 owns the index + its new chapters, which already describe the gate as cleared).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is a same-column promotion across the three level chapters, not a lowering theme). The `composes` / `reference` / `cites-evidence` / `uses-record` edge kinds in the frontmatter each match the prose discussion of the corresponding target.

**plan-kind-consistency — pass.** The declared kind is a feature-column promotion (directive-B front (ii)); the content shape matches — frontmatter `rank` flip + body `## Status` token flip + forward-ref→live-link swaps + reciprocal `reference` edge. The `feature_root: seed`-stays / `rank: rough-in→firm` split is the correct reading of the graded-stack directive (seed = permanent GC-root marker, NOT a maturity rung), verified against the promoted sibling `book/src/feature/eigenmode.L4.md:5-6` where `feature_root: seed` co-exists with `rank: firm`. No mis-classification.

**Graded-stack rank-invariant (check 9) — pass.** For the promoted `firm` (rank 3) entry, the rank-constraining edges are the `composes`-to-vocabulary `depends-on` edges only. Per the rank linter (`tools/graded-stack-lint/graded_stack_lint.py:544-549`), `cites-evidence` L0 source-range citations normalize to non-nodes (they do not add rank-constraining edges), and a `composes` edge to a SIBLING feature column is demoted to a `reference` (line 533-543, the OWN-COMPOSITION rule); only `composes`-to-vocabulary-op edges are blocking `depends-on`. So boundary-mode's blocking deps are `{L4/fe_assemble (3), L4/eigsolve (3)}` (L4 chapter) and `{L1/fe_assemble (3), L1/eigsolve (3)}` (L1 chapter); `rank(node)=3 ≤ min(deps)=3` holds. The L0 chapter carries only `cites-evidence` + `reference` edges (no blocking vocabulary deps), so its `firm` is unconstrained-from-below. The `waveguide-mode` sibling `reference` edges constrain nothing — correct that a `firm` column references a `seed` sibling.

**Graded-stack reachability (check 10) — pass.** `boundary-mode` is a feature-surface column (`kind: feature-surface`), i.e. itself a GC root — trivially reachable/live. The promotion does not orphan anything; it adds reachability (the new `reference` edges to `waveguide-mode`, plus `waveguide-mode`'s own inbound edge from `boundary-mode`, increase liveness of the new column).

**skill-uptake-survey — pass.** The promotion shape implies the `survey-firmness-from-on-disk-status` and `partly-constructive-promotion-checklist`-adjacent disciplines; the report explicitly applies the on-disk-status survey discipline (§Clean-gate, naming each constituent's exact `## Status`/`rank` line). Telemetry only; non-blocking.

### Issues found

None blocking. All 8 checks plus the two graded-stack checks pass. Two non-blocking notes recorded for the integrator (already correctly surfaced by the report, not defects):

1. **Integration-ordering (finalize coordination, NOT a report defect).** D2's three `./waveguide-mode.{L4,L1,L0}.md` cross-links are live `linkcheck2` links to files D1 creates this cycle. `integrator-finalize` must apply D1 (WAVE-1) before/with D2 (WAVE-2) in the same `cargo make book` rebuild, else the build fails on the missing anchors. The report flags this explicitly (§Cross-link resolution, Integration-ordering note); WAVE-2-depends-on-WAVE-1 ordering already encodes it. Flagging here so the per-report integrator does not apply D2 in isolation.

2. **Both-land-or-both-defer pairing with D1's index-cell delta.** D1 sole-owns `feature/index.md` + `feature/SUMMARY.md` and has already staged the boundary-mode index-cell flip (index reflecting 12 firm / 1 seed). These chapter-body `## Status` flips must land in the same cycle as D1's index-cell delta to avoid the index-cell-drift guard (index cell leading the chapter `## Status`). Correctly flagged in §Open questions; an integration-coordination constraint, not a content issue.

All file paths verified on disk this critique. The report is clean — `overall_status: ready`.
