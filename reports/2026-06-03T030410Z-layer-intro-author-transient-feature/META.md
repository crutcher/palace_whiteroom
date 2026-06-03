---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T034500Z
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
repaired_at: 2026-06-03T035200Z
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

# META: verification of cycle-073 D3 — transient feature-surface column

## Critique

Report kind: **FEATURE-SURFACE composition-root** (leaf feature column, per-driver sub-kind), three staged chapter files `transient.{L4,L1,L0}.md` destined for `book/src/feature/`. Checks run with the feature-surface adaptations (rotation-quality / variant-axis-coverage no-op; surface-or-evidence and cross-reference-integrity adapted/load-bearing).

### Checks run

**citation-validity — pass.** All three staged files clear `tools/citecheck/citecheck.py --scan` (L4: 15 ok / 0 failing; L1: 8 / 0; L0: 10 / 0), matching the report's self-reported scan counts. I `--anchor`-confirmed the load-bearing L0 pinpoints on disk: `timeoperator.cpp:65/66/67` (`GetStiffnessMatrix`/`GetDampingMatrix`/`GetMassMatrix`), `:407`/`:410`/`:413` (`Step` / `ode->Step` / close brace), `:311-313` (`IMPLICIT` op build); `transientsolver.cpp:77` (`for` loop), `:89` (`Init`), `:93` (`Step`), `:115` (`GlobalTrueVSize`), `:118` (`GetTimeExcitation` def). All resolve in-range. I also confirmed the cross-artifact pinpoint `book/src/L4/fold_solve.md:113` — it is exactly the "Transient fixed-schedule time-march … **default surface**" specialization bullet, so the report's repeated "transient is `fold_solve`'s default/primary witness (`fold_solve.md:113`)" claim is faithfully anchored. The loop-span claim `:77-109` is correct (`for` at 77, closing `}` at 109) and the method-span `:24-116` is correct (24 blank, 116 close brace, accepted by `--scan`). No `verified_against:` block is present, so the YAML round-trip sub-check is not applicable. One sub-pinpoint imprecision noted under Issues (non-blocking).

**surface-or-evidence — pass (feature-surface adaptation).** A composition-root's evidence is the L0 driver-source range + the constituent down-links, not a new per-op algebraic claim. The L0 driver range `transientsolver.cpp:24-116` (`Solve`) is cited and backs the feature; the K/C/M assembly (`timeoperator.cpp:65-67`) and ODE-step (`:407-413`) sites realize the two composed stages; every down-link (`fe_assemble`, `fold_solve`) resolves to a real firm constituent. The chapters explicitly disclaim per-op algebraic claims ("carries the compositional claim only; per-op algebraic claims live in the linked chapters"). The composition is supported — pass.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature chapter rotates nothing; it recomposes already-firm vocabulary outward (`transient = fold_solve ∘ fe_assemble`). No-op per the role-spec adaptation. (The chapters correctly route the substantive L4→L3 rotation OUT to the `fold-solve-time-step-dissolution` theme rather than asserting it here.)

**variant-axis-coverage — pass (not applicable to feature-surface kind).** No variant axes of the column's own; the `schedule-source` (fixed-list vs state-generated) axis lives in the composed `fold_solve` combinator, which the report correctly references (`fold_solve.md:115`) and explicitly scopes the driven/SweepAdaptive generalization out to D2/planner territory. No hidden branch.

**cross-reference-integrity — pass (load-bearing for this kind).** All constituent down-links resolve on disk: `book/src/L4/{fold_solve,fe_assemble,solve_family}.md`, `book/src/L1/{fe_assemble,ksp_solve}.md`, `book/src/L3/fold_solve.md`, `book/src/L4-L3/fold-solve-time-step-dissolution.md`, `book/src/concepts/sequential-obstruction.md`, and all sibling feature columns `electrostatic.{L4,L1,L0}.md` / `magnetostatic.{L4,L1,L0}.md` / the in-column siblings `transient.{L4,L1,L0}.md`. Relative-link depth is correct from `book/src/feature/` (`../L4/`, `../concepts/`, `./<sibling>`). Maturity claims match on-disk `## Status`: `fold_solve` firm (frontmatter `firmness: firm`), `fe_assemble` L4 firm / L1 firm (`## Status: firm` line 200), `L3/fold_solve` `partial-obstruction` (line 152) — all as the chapters assert. The two forward-referenced un-authored siblings `driven`/`eigenmode` appear ONLY as plain-text prose (no markdown link) — the rough-in plain-text-when-anchor-missing discipline is honored, no dead live link. **Deferral confirmed honored:** the proposed-changes block contains exactly three `edit:` fences, all `book/src/feature/transient.{L4,L1,L0}.md`; `SUMMARY.md` / `index.md` appear only in deferral prose (§Ownership), NOT as emitted edits — the D2 deferral is real, not silently emitted. Fence parity in CYCLE.md is balanced (6 backtick-fences, 3 open + 3 close); no firm-body-outside-fence concern (the bodies are sibling files, not inline). Within-column ordering high→low (L4→L1→L0) is honored in prose and the deferral instruction to D2.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this composition-root (it is a same-level surface at each of L4/L1/L0, linking DOWN to constituents, not a lowering theme). The cross-layer "L1 vs L4" and "Lifts to" prose discuss the correct adjacent relationships. No mismatch.

**plan-kind-consistency — pass.** Declared kind is feature-surface / leaf feature column with `status: seed`; content shape matches (composition-root: inputs=config, outputs=field trajectory, body=composition, links DOWN). All three files carry bare `status: seed` per the batch-22-codified uniform token (no `(exemplar)`/`(composition-root)` qualifier), with the leaf-driver sub-kind named in prose — exactly the role-spec rule. No rough-in placeholders masquerading as firm.

**skill-uptake-survey — pass (telemetry only).** The report invokes `tools/citecheck/citecheck.py --scan` and palace-codemap `read_range` with close-brace discipline — the expected localization/citation tooling for this shape. No skill omission implied by the shape.

### Issues found

1. **(minor, citation precision) `transient.L0.md:19` + L4/L1 supporting-evidence: `Solve` signature cited as `:24-25`.** The `TransientSolver::Solve` signature actually spans source lines **25-27** (return type `std::pair<...>` at 25, `TransientSolver::Solve(...)` name+params at 26, opening `{` at 27); line 24 is blank. `--anchor 'TransientSolver::Solve'` resolves at line 26, outside the cited `:24-25`. The whole-method range `:24-116` used everywhere else is fine (24 = blank line immediately preceding, 116 = close brace, accepted by `--scan`), and the L0 chapter's narrative text at `:19` correctly writes the broader `:24-25`/`:26-27` pair in context. This is a sub-line imprecision on the signature-only pinpoint, not a bounds failure — every `--scan` passed. Severity: low. Location: `transient.L0.md:19` ("`transientsolver.cpp:24-25`"), echoed in CYCLE.md §Supporting-evidence line for the signature.

2. **(observation, non-blocking) status-token form diverges from the on-disk exemplars it claims to "mirror."** The three transient files carry bare `status: seed`, which is **correct** per the batch-22-codified uniform-token rule (no qualifier; sub-kind in prose). However the chapters' own prose says they "mirror the electrostatic / magnetostatic exemplars," and those on-disk exemplars still carry the older qualifier form (`status: seed (exemplar)`, and `lifecycle.L4.md` carries `seed (composition-root)`). The transient column is the correctly-codified form; the divergence is in the *older exemplars*, not this report. Flagged only so the integrator/repairer is aware the "mirror" prose is form-accurate in structure but not in the literal status token (the exemplars are the ones now non-conforming). No change required in this report. Location: `transient.{L4,L1,L0}.md` Status sections; cross-ref `book/src/feature/electrostatic.L4.md:5`, `lifecycle.L4.md:5`.

3. **(observation, non-blocking, already self-flagged) three-operator `fe_assemble` down-link reads as one matrix row.** The author's own §Open-questions caveat notes the single `fe_assemble` constituent stands for three assemble-folds (K/C/M) for the second-order-in-time system, and asks D2 not to read the matrix row as a single-operator assemble like the map drivers. This is faithfully a single `fe_assemble` *combinator* applied thrice (not a defect); recorded here only to carry the author's hand-off note forward to the cohort-owner (D2) who authors the index row. Location: `transient.L4.md:38`, `transient.L1.md:34`; CYCLE.md §Open-questions bullet 1.

No fail- or warning-severity issues. The column is citation-clean, deferral-honored, cross-reference-intact, and correctly shaped for the feature-surface composition-root kind.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity)**: `TransientSolver::Solve` signature-only pinpoint cited `transientsolver.cpp:24-25`, but the signature actually spans `:25-27` (return type `std::pair<...>` at `:25`, name+params `TransientSolver::Solve(...)` at `:26`, opening `{` at `:27`; line `:24` is blank; `--anchor 'TransientSolver::Solve'` resolves at `:26`, outside `:24-25`).
  - **Decision**: repaired.
  - **Action**: Hand-verified on disk via palace-codemap `read_range` (`transientsolver.cpp:22-30` → return type `:25`, name+params `:26`, `{` `:27`, `:24` blank). Corrected the signature pinpoint `:24-25` → `:25-27` in `transient.L0.md:19` (the narrative signature sentence) and echoed the fix in `CYCLE.md:59` (§Supporting-evidence) with an inline line-by-line note. The whole-method range `:24-116` used everywhere else is correct and was left untouched; the adjacent `.hpp:26-27` declaration pinpoint was independently re-verified on disk and is correct (left untouched). The L4/L1 staged chapter files carry only the correct `:24-116` whole-method range (no `:24-25` pinpoint), so no change was needed there. Re-ran `tools/citecheck/citecheck.py --scan` on the edited `transient.L0.md` — full scan still `ok`, new `:25-27` in-bounds.

- **Finding 2 (status-token form diverges from on-disk exemplars)**: the transient files carry bare `status: seed` (correct per batch-22 uniform-token rule), while the older on-disk `electrostatic`/`magnetostatic`/`lifecycle` exemplars still carry the deprecated `seed (exemplar)` / `seed (composition-root)` qualifiers.
  - **Decision**: not-needed (acknowledged-not-repaired).
  - **Rationale**: This report is the correctly-codified form; the divergence is in OTHER files (`book/src/feature/electrostatic.L4.md`, `lifecycle.L4.md`, etc.), which are out of repair scope (the artifact `book/` is not repairer-writable, and modifying other reports is out of scope). The "mirror" prose in the transient chapters is structurally accurate. The exemplar back-fill (normalizing the older columns to the bare token) is a separate artifact-edit for a future dispatch / the integrator's awareness — not a defect in this report.

- **Finding 3 (single `fe_assemble` down-link stands for 3 K/C/M assemble-folds)**: the matrix-row down-link is one `fe_assemble` constituent representing three assemble-folds (the second-order-in-time wave system).
  - **Decision**: not-needed (informational hand-off).
  - **Rationale**: Not a defect — faithfully a single `fe_assemble` *combinator* applied thrice. Already self-flagged in the report's §Open-questions bullet 1 as a hand-off note to D2 (the cohort index/SUMMARY owner) so the matrix row is not read as a single-operator assemble like the map drivers. Carried forward to the integrator/D2; no edit in this report.

### Unrepairable findings

None. The sole concrete defect (signature-pinpoint imprecision) was mechanical and repaired; the other two observations are out-of-report-scope (Finding 2) or informational (Finding 3).

## Suggested resolution

`integrate` — all 8 critic checks pass, the one repairable citation-precision defect is fixed and re-verified clean by `citecheck --scan`. Integrator notes: (a) copy the three staged sibling files (`transient.{L4,L1,L0}.md`) verbatim to `book/src/feature/` as the CYCLE.md proposed-changes instructs; (b) SUMMARY.md / `feature/index.md` wiring is DEFERRED to D2 — if D2 does not land this cycle, integrator-finalize should wire the three transient chapters into the `# Feature surfaces — entry points` Part (high→low within column) to keep them reachable; (c) Finding 3's three-operator `fe_assemble` note should reach D2 (the matrix-row author) so the row is annotated as a thrice-applied combinator; (d) Finding 2's exemplar status-token divergence (`electrostatic`/`magnetostatic`/`lifecycle` still carrying `seed (exemplar)` / `seed (composition-root)`) is a standing artifact-normalization item for a future dispatch — not blocking.
