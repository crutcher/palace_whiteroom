---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T154500Z
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
repaired_at: 2026-05-29T155500Z
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

# META: verification of "L1>L0 theme sketch — nleps-jacobian-action-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Mechanically backed via `tools/citecheck/citecheck.py` against the on-disk `reference/palace/` checkout. `--scan` over the full CYCLE.md returned **32 ok, 0 failing** (all citation bounds in-range, paths clean). I then `--anchor`-checked every load-bearing pinpoint: Sub-pattern A (`:649` comment, `:650` funcA2, `:651-652` denom, `:653-654` A2', `:655-656` derivative pencil, `:657` opJ->Mult, `:658` k>0 guard), the deflation block (`:660-661` source comment, `:662-663` value pencil, `:664` S, `:665` Sv2, `:666` XSv2, `:667` XSSv2, `:668`/`:669` AddMult), and the supporting sites (`:412` δ=√ε, `:378` w decl, `:329-347` MatVecMult body, `:606-619` deflation growth, `:673`/`:675`/`:676` consumer, `:177-181` SetExtraSystemMatrix). **Every single anchor landed exactly where the report claims** — the report's on-disk line numbers are authoritative and confirmed. A `--show` meaning-read of the `:649-669` block confirms the report's structural reading is faithful (divided-difference A2', `{0,1,2λ,1}` derivative pencil, the `if (k>0)` guard, the double `S⁻¹` solve, the two `AddMult`). **The drift finding is also independently confirmed:** running the L1 operator entry `nleps_jacobian_action.md`'s own deflation-block anchors through citecheck reproduces the report's claim — `:663`/`:664`/`:665`/`:666` (S/Sv2/XSv2/XSSv2) each register `[DRIFT +1]` (on-disk source is at `:664`/`:665`/`:666`/`:667`), and the two-line ranges `:659-660`/`:661-662` are likewise −1 from on-disk `:660-661`/`:662-663`. The report correctly uses the on-disk numbers throughout and correctly partitions the operator-entry re-anchor as a carry-forward to PROPOSE (not apply) under dispatch-phase write-authority — see Issue 1 below, which is a non-blocking integrator-awareness note, not a defect in this report.

**surface-or-evidence — pass.** This is a `new:` L1>L0 theme creating a fresh chapter (`book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md`) with full surface (the firm chapter body) plus a dep-map row and SUMMARY entry. It is not a pure rotation_claim against an existing entry; it authors new surface AND grounds every constituent in positive L0 source. The refinement-shaped failure mode (pure rotation_claim without surface) does not apply.

**rotation-quality — pass.** The theme asserts a structural mutation rotation: the in-place destination-buffer `w = J*v` block (overwrite via `opJ->Mult` + two `AddMult` accumulations, line-search-cached `A2n`, scratch-buffer reuse) rotates to the pure-functional L1 form `nleps_jacobian_action(T, λ, P, v, v₂) -> Tensor[N]` that hides the destination buffer, the `A2n` caching, the value-pencil re-scoping, and the build-form choice. This is genuine state-hiding / threaded-state compression (the L1 form is strictly more equational — buffer mutation and operator caching become a returned value), not a renaming or 1:1 mapping. The big-space-only output and the divided-difference A2' are correctly carried as load-bearing recordings, not smoothed.

**variant-axis-coverage — pass.** All orthogonal axes are covered or explicitly scoped: deflation-present (`k=0` bare derivative-pencil apply vs `k>0` with coupling) handled in Sub-pattern A item 3, Applicability item 3, and the `:658` guard discussion; damping-present (`with-C`/`without-C`) absorbed by the pencil and noted in Applicability item 1; element-type complex-only in Applicability item 2; the δ=√ε step classified as a fixed solver constant (not a structural variant) in Applicability item 5; single-rank scope in Applicability item 6. No hidden branches. Coverage matches the L1 operator entry's own variant-axes section that this theme lowers.

**cross-reference-integrity — pass.** Every `[link]` resolves: I confirmed all referenced targets exist on disk (`L1/nleps_jacobian_action.md`, `L1/apply_nonlinear_pencil.md`, `L1/lu_solve.md`, `L1/apply_linop.md`, `L1/ksp_solve.md`, `L2/linear_combination.md`, `L0/eigensolver-wrapper.md`, the residual/solve/pencil/lu-solve/dot L1>L0 siblings, and `L2-L1/linear-combination-fold-specialization.md`). The only "missing" target is the new file itself (`L1-L0/nleps-jacobian-action-mutation-rotation.md`), whose self-reference live link is correct-by-creation (the report's `edit:` block note explicitly states this). **Build-readiness fence guard passes:** the CYCLE.md has 6 fence lines (even parity, 3 balanced proposed-changes blocks); the `new:` block (lines 46–577) ENCLOSES the full firm body — `## Status` (76), Signature/`## L1 form (LHS)` (105), `## L0 form (RHS)` (136), the rewrite with sub-patterns, and `## Verified-against` (Evidence, 480) all sit INSIDE the fence. No bare ` ``` ` is nested inside the proposed-changes fence; the L1/L0 code forms use 4-space-indented code blocks. The cycle-019 fence-truncation defect (firm body authored as the report's own top-level sections outside the fence) is absent. The dep-map insertion point (after line 34 / adjacent line 31) and the SUMMARY insertion point (after line 105) were verified accurate against the live files.

**edge-label-fidelity — pass.** The edge label is L1>L0. The frontmatter declares `layer: L1>L0`, `l1_anchor: book/src/L1/nleps_jacobian_action.md`, `l0_anchor: palace/linalg/nleps.cpp:649-669`. The section structure (`## L1 form (LHS)` / `## L0 form (RHS)` / `## Rewrite — forward (L1 → L0)`) and the prose narrate exactly the L1→L0 edge in the correct high→low direction (LHS = L1 pure form, RHS = L0 source, prose narrating the lowering forward). The reverse-direction lift notes are kept out of the formal body, consistent with the "layers defined high→low; lifting notes in working notes" invariant.

**plan-kind-consistency — pass.** Declared kind is a `firm` L1>L0 theme. The content shape matches: every constituent is read from a positive source site, the two non-laws (divided-difference A2', big-space-only output) are recorded as explicit load-bearing recordings (not rough-in placeholders), and zero speculative operators are proposed. There are no `partly-constructive` constructive sub-parts (nothing is materialized from negative anchors), so `firm` (not `partly-constructive`) is the correct status — matching the firm-on-positive-structure escape the residual/solve/pencil siblings use. The "Speculative L1 operators: None" and "Speculative operators proposed: None" sections are consistent with the compose-existing-firm-leaves shape.

**skill-uptake-survey — pass.** The report's citation-verification shape implies `verify-citation-range`, and the report explicitly invokes it: §Verified-against names the `verify-citation-range` discipline and documents the mechanical `tools/citecheck/citecheck.py --anchor`/`--scan`/`--show` self-verify per the cycle-024 meta-phase wiring, with per-anchor `citecheck --anchor ... → line N` telemetry. This is strong, current skill uptake. (Pure presence check — non-blocking.)

### Issues found

No blocking issues. Two non-blocking notes for the integrator/repairer:

1. **(informational, correctly self-partitioned) Theme/operator-entry citation disagreement on six anchors.** `reports/.../CYCLE.md` §Open questions item 1 and §Verified-against record that the firm L1 operator entry `book/src/L1/nleps_jacobian_action.md` carries a −1 line drift on six deflation-block anchors (comment `:659-660`→on-disk `:660-661`; value pencil `:661-662`→`:662-663`; S `:663`→`:664`; Sv2 `:664`→`:665`; XSv2 `:665`→`:666`; XSSv2 `:666`→`:667`). I independently confirmed all six via citecheck `[DRIFT +1]` / range analysis. This report is the citecheck-verified-correct one; the operator entry is the drifted one. The report correctly partitions the operator-entry re-anchor as a change to PROPOSE (a follow-up lifter/repairer pass), not to apply here, per dispatch-phase write-authority. **No defect in this report** — flagged only so the integrator is aware the theme and the operator entry will disagree on these six anchors until the operator entry is re-anchored (the OQ should be promoted at integration).

2. **(observation) Shared `:673-676` citation range with dispatch-2 sibling.** §Open questions item 3 notes the consumer lines `:673`/`:675`/`:676` are cited here as downstream context (the big-space-only confirmation) and will be the primary subject of dispatch 2's `nleps_eigenvalue_correction` theme. No conflict — different roles (context here, subject there). Flagged only as integrator awareness for the shared citation range across the two NEP-interior themes; not a defect.

---

## Repair

### Fixes attempted

The critic graded **all 8 checks `pass`** — a clean report with no warning/fail findings. There are no in-report defects to repair. The two items the critic recorded under "Issues found" are both explicitly non-blocking integrator-awareness notes (the critic so labels them), not defects in this report. Per-check accountability:

- **citation-validity** — `pass` (critic) → **not-needed**. The critic mechanically re-verified all 32 citations via `tools/citecheck/citecheck.py --scan` (32 ok, 0 failing) and per-anchor `--anchor`. The report's on-disk line numbers are authoritative and confirmed. Nothing to repair.
- **surface-or-evidence** — `pass` → **not-needed**. The `new:` L1>L0 theme authors full firm-chapter surface plus dep-map row and SUMMARY entry; not a bare rotation_claim.
- **rotation-quality** — `pass` → **not-needed**. Genuine state-hiding rotation (destination-buffer / `A2n`-cache / value-pencil re-scoping → returned value).
- **variant-axis-coverage** — `pass` → **not-needed**. All orthogonal axes (deflation-present `k=0`/`k>0`, damping `with-C`/`without-C`, complex-only element type, `δ=√ε` solver constant, single-rank) covered or explicitly scoped.
- **cross-reference-integrity** — `pass` → **not-needed**. Every `[link]` resolves on disk; the self-reference is correct-by-creation; the build-readiness fence guard passes (even parity, firm body fully enclosed by the `new:` fence, no nested bare fences).
- **edge-label-fidelity** — `pass` → **not-needed**. L1>L0 edge label, high→low direction, frontmatter anchors consistent.
- **plan-kind-consistency** — `pass` → **not-needed**. `firm` L1>L0 theme; every constituent read from a positive site; firm-on-positive-structure status correct (no `partly-constructive` sub-part); zero speculative operators.
- **skill-uptake-survey** — `pass` → **not-needed**. Strong current uptake of `verify-citation-range` via the cycle-024 `citecheck` wiring.

**Frontmatter check (per dispatch instruction).** The `verifies:` frontmatter is already `../CYCLE.md` (META.md line 2) — not the stale `../REPORT.md` form. No fix needed.

### Unrepairable findings

None. No findings were flagged `warning`/`fail` by the critic, so there is nothing that exceeds repair authority.

### Carry-forward (for the integrator / a follow-up dispatch — NOT repaired here)

The two critic notes are deliberately **out of this report's scope** and are NOT touched by this repair pass:

1. **L1 operator-entry six-anchor drift (carry-forward to PROPOSE).** The firm L1 entry `book/src/L1/nleps_jacobian_action.md` carries a −1 line drift on six deflation-block anchors (comment `:659-660`→on-disk `:660-661`; value pencil `:661-662`→`:662-663`; `S` `:663`→`:664`; `Sv2` `:664`→`:665`; `XSv2` `:665`→`:666`; `XSSv2` `:666`→`:667`), independently confirmed by the critic via citecheck `[DRIFT +1]`. **This report is the citecheck-verified-correct one** and uses the corrected on-disk numbers throughout. Re-anchoring the L1 ENTRY is a change to the artifact (`book/src/L1/`), which is out of scope for this repair pass (the repairer does not modify the artifact, and the dispatch-phase write-authority partition keeps the producer from applying it). The CYCLE.md §Open questions item 1 already records this as a change to PROPOSE; the integrator should promote that OQ at integration, and a follow-up **lifter or repairer pass on the L1 entry** should re-anchor the Semantics-point-2 trace (`:46-69`), Dependencies (`:108-111`), L1-vs-L0 (`:140`), and Evidence (`:152-158`) citations by `+1` for the six drifted anchors. Until then the theme and the operator entry will disagree on these six anchors (the theme is correct).

2. **Shared `:673-676` range with dispatch-2 sibling.** No conflict — context here, subject in dispatch 2's `nleps_eigenvalue_correction` theme. Integrator awareness only; nothing to repair.

## Suggested resolution

`ready`. The report is clean (8/8 `pass`); no repairs were required and the `verifies:` frontmatter was already correct. Notes for the integrator:

- Promote CYCLE.md §Open questions item 1 (the L1-entry six-anchor re-anchor) to the OQ ledger / plan as a follow-up lifter/repairer pass on `book/src/L1/nleps_jacobian_action.md` — do not block this report on it. The theme being applied is the citecheck-verified-correct one.
- Expect the `:673-676` citation range to be shared with the dispatch-2 `nleps_eigenvalue_correction` theme (context-vs-subject; no conflict).
- CYCLE.md §Open questions item 2 (codemap `read_range` +1 drift as a methodology signal) is surfaced for the meta-phase's batch view; it is an observation below the problems/ bar, appropriately left as an OQ.
