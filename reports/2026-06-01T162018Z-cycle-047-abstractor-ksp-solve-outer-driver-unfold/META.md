---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T16:42:10Z
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
repaired_at: 2026-06-01T16:52:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of L2>L1 theme `ksp-solve-outer-driver-unfold` (cycle-047 D3)

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returns `25 ok, 0 failing (25 citations checked)` — no bounds violations, no path-hygiene issues. I independently spot-verified a sample of load-bearing pinpoints with `--anchor`, all `[ok]` with the claimed token in range: `iterative.cpp:427` (`max_it` loop guard), `:463` (`converged` in-loop test), `:484-485` (`final_res` CG result write), `:703-704` (`final_res` GMRES write — confirmed the GMRES `final_res = beta` LS-residual proxy), `ksp.cpp:53-56` (`MFEM_ABORT`, anchor at :56), `ksp.cpp:296-309` (`GetConverged`, at :301), `divfree.cpp:175` (`Mult` call site). I also read the *semantic* content behind the two structurally load-bearing artifact anchors: `book/src/L2/ksp_solve.md:155-157` §"Lowers from" verbatim asserts the rotation is non-identity, opacity opened at L2, and "the firming evidence for the open are working-notes / OQ-ledger concerns, not chapter content" — exactly the in-line narration this theme firms; and `book/src/L1/ksp_solve.md:93-95` carries the absorbed `krylov-method` axis collapse into the opaque `Solver[A]` exactly as the report's re-absorption claim states. The report's "all 25 pass `--scan` + load-bearing L0 self-verified via `--anchor`" claim holds. No `verified_against:` fenced-YAML block is proposed (the report uses a prose §Verified-against section, not a YAML round-trip payload), so that sub-check is not applicable.

**surface-or-evidence — pass.** This is a NEW L2>L1 theme file (`new:` block), not a refinement of an existing operator/theme surface. It authors fresh surface (the full chapter body) AND it is the dedicated firming-evidence home for a rotation the L2 chapter previously narrated in-line and explicitly deferred. Both the "modifies surface" and "is the deferred firming-evidence backfill" framings are satisfied; not a pure rotation_claim without surface.

**rotation-quality — pass.** The asserted L2→L1 rotation is genuinely non-identity and strictly more compact at L1: the L2 explicit kernel-fold composition (`iterate_while (krylov-step op) …` over a unified `IterState`, plus setup/convergence-init/materialise) re-collapses into the single opaque `(K, b) -> SolveResult` operator application — the kernel, the fold, and the solver-method nesting all vanish into the black-box `Solver[A]`. This is state-hiding / opacity-closing (coarser substitution), not a rename or 1:1 mapping. The forward (high→low) narration as the inverse of the L2 §"Lowers from" *open* is sound — I confirmed against `L2/ksp_solve.md:157` that the L2 entry opens the L1 opacity, so the lowering correctly re-closes it. The rewrite-shape table honestly delimits the substantive lines (kernel-fold + solver-method axis) from the identity lines (boundary `SolveResult`, law-reframing), so the entry does not over-claim. The orthogonal-aspects framing checks out: I read `L3-L2/ksp-solve-outer-driver.md` in full — it rotates the *iteration view* (explicit `iterate_while_L3` tail recursion erased to a role wrap), distinct from this theme's *opacity* axis; the L2 form genuinely sits at the junction (opacity OPEN vs. L1, iteration-view ERASED vs. L3).

**variant-axis-coverage — pass.** The theme's axes are the L2 solver-method loop-shaping axis (CG / GMRES / FGMRES) and the absorbed `krylov-method` opacity-axis at L1; both are explicitly covered — the re-absorption of the composition-granularity solver-method axis into the L1 opacity is the report's re-collapse step (2). The MINRES / BiCGStab arms are explicitly scoped out (Applicability condition 1: obstruction-only, not implementation targets, re-audit deferred). The preconditioner-side axis is addressed as kernel-side (absorbed into `op.T`), not a separate driver axis. No hidden branches.

**cross-reference-integrity — pass (build-readiness verified).** Fence enumeration: `grep -nE '^\`\`\`'` on CYCLE.md returns exactly 10 fences forming 5 balanced blocks (1 `new:` + 3 `edit:index.md` + 1 `edit:SUMMARY.md`), matching the report's claim. The `new:` block body spans lines 26–185 with `## Status` (line 181) INSIDE the fence — the firm-body-inside-fence guard passes (no cycle-019 fence-truncation defect). No nested ` ``` ` fences inside any block (code samples are 4-space-indented). The four `edit:` anchors all match disk byte-exactly: the `incremental-least-squares-composition-lowering` table row (index.md:32), the §Vocabulary-cohort `running-QR / Givens-stream` bullet (index.md:44), the Cohort-growth-log line (index.md:71), and the SUMMARY `divfree-projector-leaf-identity` line (SUMMARY.md:106). All live links resolve on disk: `L3-L2/ksp-solve-outer-driver.md`, `L2/krylov-step.md`, `L4/iterate-while.md`, `L1-L0/{minres,bicgstab}-iteration.md`, `L1-L0/ksp-solve-mutation-rotation.md`, all six cited `concepts/*.md`. The sibling D4 `krylov-step-kernel-defusion.md` is confirmed ABSENT on disk and is referenced ONLY by plain-text slug (never as a `[live](link)`) — correct per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention; not a dead live-link. The target `ksp-solve-outer-driver-unfold.md` is absent (genuine create).

**edge-label-fidelity — pass.** The edge label is consistently L2>L1 throughout (slug, theme-table row, cohort bullet, SUMMARY, §Justification, §Status). The prose discusses exactly the L2→L1 edge; the L3>L2 references are explicitly labeled as the *sibling upward complement* (not conflated with this edge), and the L1>L0 `ksp-solve-mutation-rotation` is correctly labeled as the next edge down, out of scope. No L2/L3 mislabel anywhere.

**plan-kind-consistency — pass (count-ownership arithmetic verified).** Declared kind is `firm` L2>L1 theme; content shape matches (both endpoints firm; substantive structurally-grounded non-identity rotation; no rough-in placeholders; no speculative L1 operators). I independently verified the consolidated-tally arithmetic against disk: the current `L2-L1/index.md` Cohort-growth-log head (line 71) reads "firm **15 → 19** = 19 firm + 1 partly-constructive", and the themes-table has 20 rows (19 firm + 1 partly-constructive `deflate-composition-lowering`) — so the report's pre-bump baseline of 19 firm + 1 partly-constructive is correct, and the 19→21 bump for two landings (D3 + D4) is the correct arithmetic. The dual-registration partition is correctly applied: this report owns the consolidated tally + its own table row + its own cohort bullet + its own SUMMARY line; D4 defers its tally to this report. The D4-non-landing contingency (reconcile to 20 firm + 1) is flagged for the integrator (§Open-questions count-ownership note). The OQ closures are accurate: `ksp-solve-l2-l1-theme-gap` (OQ ledger :182) and the joint `residual-l2-l1-gap-audit` closure with D4 both match the on-disk ledger framing, including the slug suggestion, the driver-tier RANK-1 fan-out, and the route.

**skill-uptake-survey — pass.** The report references the relevant procedural skills appropriately: `tools/citecheck/citecheck.py --anchor`/`--scan` for the L0 self-verification (the citation-validity mechanical procedure), and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` for the D4 forward-reference contingency. The proposed-changes-fence guard's discipline is honored (Provenance bullet on the write-guard). Telemetry only; non-blocking.

### Issues found

No issues found. All eight checks pass. Specific verifications that could have surfaced defects but did not:

- **Count-ownership arithmetic is correct** — on-disk baseline (19 firm + 1 partly-constructive, index.md:71 + 20 table rows) confirms 19→21 for the two landings; the D4-contingency reconciliation (→20 firm) is correctly flagged for the integrator.
- **Plain-text D4 reference is correct, not a build defect** — `krylov-step-kernel-defusion.md` is absent on disk and is referenced only as plain-text slug, never as a live link; this is the required convention for a same-cycle parallel-dispatch sibling.
- **Fence parity is clean** — 10 fences / 5 blocks, `## Status` inside the `new:` fence, no nested fences; no cycle-019-style firm-body-outside-fence truncation risk.
- **Orthogonal-aspects framing is sound** — independently confirmed `L3-L2/ksp-solve-outer-driver.md` rotates the iteration-view axis (distinct from this theme's opacity axis), so the "both edges of the L2 driver, orthogonal aspects" claim is not an over-statement.

Note for the repairer/integrator (not a defect): the `new:` block's first `## Status` (line 181) and the §Status frontmatter consistency are fine; the only downstream contingency is the D4-non-landing tally reconciliation, already self-flagged in the report.

---

## Repair

### Fixes attempted

No warning/fail findings were flagged by the critic. All eight checks pass. This is the confirm + set-`overall_status` pass (the established convention that every report — even an all-pass one — receives a repairer pass that sets `overall_status`). No content was modified.

Per-check disposition: all eight → `not-needed` (nothing to repair). I independently re-ran the two specific sanity checks the dispatch asked me to confirm against `CYCLE.md`:

- **Finding**: Consolidated-tally edit (19→21) present and correctly accounting for both D3 (this theme) + D4 (`krylov-step-kernel-defusion`).
  - **Decision**: not-needed (confirmed sound).
  - **Confirmation**: The CONSOLIDATED tally `edit:` block (CYCLE.md Cohort-growth-log, `book/src/L2-L1/index.md`) reads "firm **19 → 21** = 21 firm + 1 partly-constructive" and explicitly attributes the +2 bump to the D3+D4 driver+kernel edge-pair. The pre-bump on-disk baseline (19 firm + 1 partly-constructive, the cycle-043 head + 20 themes-table rows) is confirmed by the critic (META plan-kind-consistency check). The §Count-ownership note self-flags the D4-non-landing contingency. Arithmetic is correct.

- **Finding**: D4 sibling reference (`krylov-step-kernel-defusion.md`) is plain-text, not a dead live-link.
  - **Decision**: not-needed (confirmed sound).
  - **Confirmation**: `krylov-step-kernel-defusion` appears only as plain-text slug in CYCLE.md — applicability condition 4, the cohort growth-log line, and the §Forward-reference-hygiene note — never as a `[live](link)`. The critic independently verified (META cross-reference-integrity check) the file is ABSENT on disk and referenced only by plain-text slug, correct per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention. No de-linking or plain-text-downgrade repair is required.

### Unrepairable findings

None. No findings were flagged.

## Suggested resolution

`ready` — clean report, no repairs applied, no deferrals.

**Integrator contingency note (carried from the report's own §Count-ownership self-flag, not a defect):** this report is the SOLE `book/src/L2-L1/index.md` consolidated-tally owner and bumps **19 firm + 1 partly-constructive → 21 firm + 1 partly-constructive**, accounting for BOTH D3 (this theme) and the parallel-dispatch sibling D4 (`krylov-step-kernel-defusion`, which defers its tally to this report per the dual-registration partition). D4 IS landing this cycle, so 19→21 is the correct arithmetic. **If D4 does not land**, the integrator should reconcile the tally to **20 firm + 1 partly-constructive** (D3 only) and, per the report's §Forward-reference-hygiene note, leave the D4 plain-text slug references as-is (they remain correct plain-text forward-refs). **If D4 lands** (the expected case), the integrator may optionally upgrade the plain-text `krylov-step-kernel-defusion` references to live links per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` once the anchor file is on disk.
