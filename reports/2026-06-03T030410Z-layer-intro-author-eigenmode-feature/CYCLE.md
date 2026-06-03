---
agent: layer-intro-author
invoked_at: 2026-06-03T03:04:10Z
scope: eigenmode feature-surface column (book/src/feature/eigenmode.{L4,L1,L0}.md)
status: pending
integrated_at: 2026-06-03T214500Z
integration_commit: 03d43ae
integration_notes: "cycle-073 D4. Applied clean — new feature/eigenmode.{L4,L1,L0}.md (status seed); the minimal assemble x3 |> eigsolve |> readout-map (single-black-box-kernel shape, no solve_family/fold_solve); eigenfrequency-qfactor output-product down-link stays plain-text (keeps column seed; both solve-side constituents firm). index/SUMMARY rows deferred-to-D2 (resolved same-cycle). Build exit 0, linkcheck2 clean."
---

# CYCLE: eigenmode feature-surface column (L4 + L1 + L0)

## Summary

Authored the **EIGENMODE simulation feature-surface column** — three new composition-root chapters under `book/src/feature/`, one per level (high→low: L4, L1, L0), under the FEATURE-SURFACE SPINE directive (2026-06-02; CLAUDE.md §Extraction-goal; memory `project_feature_surface_spine`). This is a **leaf feature column** (per-driver; uniform `status: seed`), the third driver column after [electrostatic](../../book/src/feature/electrostatic.L4.md) and [magnetostatic](../../book/src/feature/magnetostatic.L4.md).

The eigenmode column is the **cleanest test of the composition-root pattern over a single black-box-kernel constituent + assemble**, because the eigenmode driver has **no operator/RHS family to map and no state-fold** — its body is the minimal shape `assemble (×3) ▷ eigsolve ▷ readout-map`:

- **Stage 1 — assemble the K/C/M operator pencil once**: three single-term [`fe_assemble`](../../book/src/L4/fe_assemble.md) folds (firm).
- **Stage 2 — one opaque black-box eigen-solve**: exactly one [`eigsolve`](../../book/src/L4/eigsolve.md) call (firm; the black-box-kernel constituent per `project_blackbox_vs_accelerated_kernels` — Palace authors no eigen-iteration loop, the iteration is opaque-library-owned inside SLEPc `EPSSolve` / ARPACK `naupd` RCI). NO `solve_family` map, NO `fold_solve` state-march.
- **Stage 3 — per-mode readout map**: a pure post-processing `map` over the converged eigenpair set (ω, Q, `B = -1/(iω)∇×E`); the eigenfrequency/Q reduction into the user-facing product is a **forward-ref** to the not-yet-authored `eigenfrequency-qfactor` output-product column.

The `solve_family`/`fold_solve` **non-membership** is the load-bearing structural fact, explicitly grounded at `book/src/L4/solve_family.md:146` (the cycle-059 eigenmode-outer-machinery probe verdict). Both *solve-side* composed constituents are firm; the only reason the column stays `seed` rather than promoting is the stage-3 forward-ref to the un-authored output-product column.

## Proposed changes

Three NEW files. Each chapter body is staged as a sibling file in this report dir (per the dispatch instruction, to avoid nested-fence truncation); the integrator copies them **verbatim** to the target path.

```edit:book/src/feature/eigenmode.L4.md
[new-file]: copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-eigenmode-feature/eigenmode.L4.md
```

```edit:book/src/feature/eigenmode.L1.md
[new-file]: copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-eigenmode-feature/eigenmode.L1.md
```

```edit:book/src/feature/eigenmode.L0.md
[new-file]: copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-eigenmode-feature/eigenmode.L0.md
```

### Index / SUMMARY rows — DEFERRED to D2 (single-index-owner)

Per the dispatch ownership partition and the role-spec `single-index-owner when ≥2 columns land in one cycle` guard: this dispatch authors **ONLY** its 3 chapter files. The `feature/index.md` matrix row for the eigenmode column **and** the `# Feature surfaces — entry points` SUMMARY.md rows for it are **DEFERRED to D2** (the driven-column layer-intro-author, designated SOLE index/SUMMARY owner for the driver cohort this cycle). This dispatch emits **no** `index.md` or `SUMMARY.md` edit.

For D2's reference, the eigenmode column's three SUMMARY rows should be placed in the `# Feature surfaces` Part with within-column level ordering **high→low (L4→L1→L0), NOT alphabetized** (the deliberate directive-3 exception), nested as a co-equal leaf driver column under the lifecycle ROOT, alongside electrostatic / magnetostatic / driven / transient. Suggested chapter titles (matching the H1s): `eigenmode — L4 composition-root` / `eigenmode — L1 composition-root` / `eigenmode — L0 ground-truth surface`. The `feature/index.md` matrix row: feature `eigenmode`, levels present L4+L1+L0 (no L2/L3 — the decomposition does not meaningfully reshape there: the single opaque solve + assemble carries no intermediate fusion/iteration rotation worth a column), status `seed`, sub-kind `leaf feature column (per-driver)`.

## Supporting evidence

### Composed constituents (all live links; on disk this dispatch)

| Stage | L4 constituent | L1 constituent | Status (read from chapter `## Status`/frontmatter) |
|---|---|---|---|
| assemble K/C/M pencil ×3 | [`fe_assemble`](../../book/src/L4/fe_assemble.md) | [`fe_assemble`](../../book/src/L1/fe_assemble.md) | firm / firm |
| opaque eigen-solve ×1 | [`eigsolve`](../../book/src/L4/eigsolve.md) | [`eigsolve`](../../book/src/L1/eigsolve.md) | firm / firm |
| per-mode readout map | `eigenfrequency-qfactor` (output-product column) | same | forward-ref (un-authored; plain-text) |

Constituent statuses confirmed by reading each chapter's authoritative declaration: `L4/eigsolve.md` frontmatter `firmness: firm`; `L4/fe_assemble.md` frontmatter `firmness: firm`; `L1/eigsolve.md` / `L1/fe_assemble.md` `firmness: firm`. The non-membership grounding is `book/src/L4/solve_family.md:146` (read this dispatch — the eigenmode driver calls `eigen->Solve()` once, no operator/RHS family, only a readout map).

### L0 ground-truth (all anchors confirmed on-disk via palace-codemap + `tools/citecheck/citecheck.py --anchor`)

Driver: `EigenSolver::Solve` — `palace/drivers/eigensolver.cpp:32-477` (decl `:32-33`); class `palace/drivers/eigensolver.hpp:20-28` (`Solve` decl `:23-24`).

- K/C/M assembly: `:40` (`GetStiffnessMatrix`, DIAG_ONE) / `:41` (`GetDampingMatrix`, may be nullptr → linear EVP) / `:42` (`GetMassMatrix`); `SpaceOperator space_op` `:39`; nonlinear `funcA2` lambda `:45-46`.
- Pencil capture / per-solve control: `SetOperators` dispatch `:172-196` (SLP `:177`, quadratic `:189`, linear `:193`); `SetNumModes` `:196`, `SetTol` `:200`, `SetMaxIter` `:201`; M-inner-product orthog `:209-218`; divergence-free projector `:220-235`.
- The single opaque solve: `int num_conv = eigen->Solve()` `:367` (print block `:368-375`; optional quasi-Newton refinement re-run `:405`).
- Per-mode readout loop `:424-471`: `for` `:424`, `GetEigenvalue(i)` `:427`, error reads `:428-429`, ω un-transform (linear `:430-434`, quadratic `:435-439`), `GetEigenvector(i, E)` `:443`, `NormalizePhase` `:445`, `B = -1/(iω)∇×E` `:447-449`, Floquet correction `:450-455`, `MeasureAndPrintAll` `:458`; `MFEM_VERIFY` `:472-475`, `return` `:476`.

**Citation-drift note (role-spec `codemap-read-range-plus-one-drift-on-brace-boundary`).** The palace-codemap `read_range` indexing drifted **+1** in the early region of `eigensolver.cpp` (the multi-line-comment + opening-brace boundary at the top of `Solve`): codemap showed `GetStiffnessMatrix` at `:39`, `SpaceOperator` at `:38`, `GetEigenvalue` at `:426`, `SetOperators(linear)` at `:194`, etc. `citecheck --anchor` (on-disk authoritative) caught the drift; **all citations corrected to on-disk line numbers** (K=40, SpaceOp=39, GetEigenvalue=427, SetOperators-linear=193, …). The drift CLOSED mid-file — the solve / readout region (`:367`, `:424`, `:443`, `:458`) matched on-disk under codemap. Final `citecheck --scan` of all three chapters: L4 11/11 ok, L1 9/9 ok, L0 4/4 ok; spot anchor-checks on the corrected lines all `[ok]`.

### Sibling forward-refs

`driven` / `transient` sibling driver columns are **not yet authored** → referenced **plain-text by slug** (NOT live-link), per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention (live links to missing anchors fail mdbook `linkcheck2`). `electrostatic` / `magnetostatic` columns exist on disk → live-linked. The eigenmode chapters cross-link each other (`./eigenmode.L1.md` ↔ `./eigenmode.L4.md` ↔ `./eigenmode.L0.md`); these resolve once the integrator places all three files in `book/src/feature/`.

## Open questions / caveats

- **`eigenfrequency-qfactor` output-product column not yet authored.** The stage-3 per-mode readout reduction (ω → reported eigenfrequency; complex ω → Q-factor) is forward-ref'd plain-text in all three eigenmode chapters. When that output-product column lands, its authoring dispatch should (a) author the physical reduction (eigenfrequency extraction + Q = ... from the complex ω), and (b) the eigenmode column's stage-3 forward-refs can be upgraded plain-text → live-link (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). This is the one element keeping the eigenmode column at `seed` rather than a clean firm-constituent promotion candidate.
- **eigenmode column has NO L2/L3 chapters.** Per the FEATURE-SURFACE directive ("L2/L3 feature chapters ONLY where the decomposition meaningfully reshapes"), the eigenmode decomposition does not reshape at L2 (fusion) or L3 (iteration): the single opaque `eigsolve` + the assemble carry no intermediate fusion or removable-iteration rotation worth a feature column (the L3 iteration view of `eigsolve` is the canonical `partial-obstruction` — the loop is opaque-library-owned, body lifts; `book/src/L3/eigsolve.md`). Recorded here so a future planner does not read the L2/L3 absence as a coverage gap.
- **No 2nd-witness in-column edits made.** Per the down-links-are-read-only guard, this dispatch made no edits to any constituent op chapter (`fe_assemble`, `eigsolve`, `solve_family`). The `solve_family.md:146` non-membership grounding was *read*, not edited.
- **Promotion-past-seed test (role-spec note).** The role-spec names the eigenmode column as "the first clean test" of a column whose composed constituents could all be firm. As authored, the two solve-side constituents ARE firm — but the stage-3 output-product forward-ref blocks a clean all-firm composition, so it correctly stays `seed`. The clean all-firm test arrives when `eigenfrequency-qfactor` is authored AND firm.
