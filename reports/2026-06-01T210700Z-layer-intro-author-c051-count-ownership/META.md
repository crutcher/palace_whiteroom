---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T21:31:39Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T22:05:00Z
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

# META: verification of D5 cycle-051 consolidated count-ownership (L3>L2 + L2>L1 firm tallies + degenerate-cohort discharge)

## Critique

### Checks run

**citation-validity — pass.** This is a count/narrative report, not a source-claim report; the load-bearing "citations" are the on-disk index lines the four `edit:` blocks anchor against, plus the provenance pointers to D1–D4 and the D8 audit. I verified every anchor against the actual on-disk state:
- A.1 `[old]` (L3-L2/index.md:34, the BLAS-1-leaf cohort-header italic intro) matches the on-disk text **byte-for-byte**.
- A.2 `[old]` is asserted to be D4's change-#6 `[new]` verbatim — confirmed **IDENTICAL** via diff of CYCLE.md:48 against D4 report line 242 (D4's `[new]` payload). The current on-disk L3-L2/index.md:61 is still D4's `[old]` (the c050 `17→13` form), so A.2's anchor matches the *post-D4* state, exactly as D5 documents.
- B `[old]` (L2-L1/index.md:73 head bracket + first c050 sentence) is a **substring match** of on-disk line 73, occupying positions 0–954.
- C `[old]` (L3/index.md:65, the "NOT yet re-expressed through" cycle-050 combinator bullet tail) matches on-disk **byte-for-byte**.
- Provenance pointers (D1–D4 reports, the D8 verify-body audit `reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`) all resolve. No off-bounds or stale citation. No `verified_against:` block in this report, so that sub-check no-ops.

**surface-or-evidence — pass.** Not a refinement of operator/theme surface; this is a consolidated count + narrative reconciliation across three Part-index files (a layer-intro-author count-ownership dispatch). The closest analogue to "evidence" is the survivor enumeration, which is backed by direct on-disk file counting (see rotation-quality / cross-reference notes). Not applicable in the refinement-surface sense; marked pass.

**rotation-quality — pass.** No algebraic/structural rotation is asserted by this report — it tallies the *result* of D1–D4's demotions (which removed degenerate identity-in-named-terms themes). The substantive judgement that `divfree-projector-leaf-identity` is a genuine rotation (KEEP) vs. the demoted degenerates is inherited from D4/D8, not re-derived here. I spot-confirmed the KEEP rationale is real: `book/src/L2-L1/divfree-projector-leaf-identity.md` states it carries "exactly one genuine fusion rotation — the L2 form's single `Grad->AddMult(ψ, y, 1.0)` apply-and-accumulate idiom," consistent with D5's characterization. Not applicable as a rotation-authoring check; marked pass.

**variant-axis-coverage — pass.** No operator/theme with orthogonal variant axes is authored here. Not applicable to a count-ownership report.

**cross-reference-integrity — pass.** I verified the survivor enumerations against the actual on-disk theme files:
- **L3>L2: 13 → 5 CONFIRMED.** `ls book/src/L3-L2/*.md` (minus index) = 13 themes. The 8 planned deletions (D1: scal/axpy/axpby/axpbypcz-body; D2: dot-body; D3: nrm2-body; D4: jacobi-smoother-body + divfree-projector-body) are all present on-disk now (deletion happens at integration). 13 − 8 = 5. The named survivors (krylov-step-body-identity, ksp-solve-outer-driver, orthogonalize-variant-split, eigsolve-opaque-eigen-iteration, chebyshev-nested-recurrence) are **exactly** the 5 remaining files. ✓
- **L2>L1: 17 firm → 10 firm (+1 partly-constructive UNCHANGED) CONFIRMED.** `ls book/src/L2-L1/*.md` (minus index) = 18 themes; `deflate-composition-lowering.md` confirmed `partly-constructive` (status line read), so 17 firm + 1 partly-constructive. The 7 planned firm deletions (D1: 4 leaf; D2: dot-leaf; D3: nrm2-leaf; D4: jacobi-smoother-leaf) with `divfree-projector-leaf-identity` SURVIVING gives 17 − 7 = 10 firm + 1 partly-constructive. The named 10 survivors all exist on-disk. ✓
- **L3 firm UNCHANGED at 17 CONFIRMED** — C does not touch the authoritative tally (L3/index.md:63); it appends only to the discharge note. Consistent.
- **All cross-reference links resolve** from their writing-file directories: A.2's `../L3/linear_combination.md` / `../L3/inner_product.md` (from L3-L2/), C's `./linear_combination.md` / `./inner_product.md` and `../L2-L1/linear-combination-fold-specialization.md` (from L3/), plus `book/src/L2/nrm2.md` / `book/src/L2/jacobi-smoother.md` referenced in the narrative — all exist on disk. No build-breaking dead link introduced.

**edge-label-fidelity — pass.** Every edge label is discussed at the matching edge: A targets L3>L2 themes, B targets L2>L1 themes, C targets the L3 operator index. The "consolidated 5 / 10 / 17" counts are each attributed to the correct edge. The serial-ordering note correctly identifies A.2 as the L3>L2 cohort-growth bullet and B as the L2>L1 cohort-growth-log head. No edge mislabel.

**plan-kind-consistency — pass.** Declared shape is a consolidated count-ownership / index-reconciliation dispatch (layer-intro-author, sole count-owner). The content (three Part-index `edit:` blocks updating tallies + discharge narrative, no operator/theme authoring) matches. Fence parity verified: 8 ``` markers = 4 balanced `edit:` blocks, no nested fences inside any block (the firm-body-inside-fence guard is N/A — no firm chapter body is authored here). No mis-classification.

**skill-uptake-survey — warning.** This report's shape (count arithmetic + collision/serial-ordering discipline + cross-file anchor reconciliation) is exactly the situation a count-reconciliation or anchor-disjointness procedure would serve, but no skill is referenced. Two skills are arguably relevant and uninvoked: `verify-citation-range` / `tools/citecheck` for the anchor-substring confirmation (the A.2-equals-D4-`[new]` byte-identity claim and the B/D4 disjoint-substring claim are precisely mechanical line-map checks), and the `proposed-changes-fence-encloses-full-body-guard` (no-op here but unmentioned). Pure telemetry, non-blocking — the report did the verification carefully *by hand and by enumeration*, it just didn't cite a procedure. Surfaces a candidate gap: there is no skill for "consolidated cross-dispatch count reconciliation against on-disk survivor enumeration," which this report executes well and which recurs across count-owner dispatches.

### Issues found

1. **[LOW — narrative-arithmetic inconsistency, NOT a tally error] Summary §"Degenerate-cohort discharge" (CYCLE.md:28) and the C-change discharge note (CYCLE.md:67) — "16 demoted + 1 KEPT = 17" does not reconcile with the unit used in the same sentence's breakdown.** The Summary asserts a 17-member cohort = "16 demoted ... + 1 KEPT-substantive," but the parenthetical breakdown inside the *same sentence* enumerates **themes**: c050 "both edges = 8 themes" + c051 "8 + 2 + 2 + 2 + 1" = 23 themes demoted, not 16. Counting by **operator** instead: c050 = 4 ops (assemble-diagonal/elementwise-product/reciprocal/normalize) + c051 = 7 fully-demoted ops (scal/axpy/axpby/axpbypcz/dot/nrm2/jacobi-smoother) = 11 ops, not 16 either. The D8 denominator "17 (not 18)" is defined upstream (cycle-049 audit §1c, `reports/2026-06-01T190900Z-...-degenerate-lowering-audit/CYCLE.md:80-93`) as a count of degenerate **{body-identity, leaf-identity} PAIRS** (18 pairs → 17 after divfree-projector is reclassified because its leaf edge is substantive). Under that pair-unit, "16 demoted + 1 KEPT = 17" still does not match the demotion set (11 fully-demoted operators this refactor pass; the original 18-pair cohort included survivors like `krylov-step` that this pass does not demote). The "16" is unreconcilable with any single consistent unit (themes=23, operators=11, pairs=11-of-17-demoted). **Scope of harm is contained:** this is prose in the discharge narrative only; the three load-bearing count EDITS — A.2 L3>L2 13→5, B L2>L1 17→10 (+1 pc), C L3 unchanged 17 — are each independently verified correct against on-disk survivor enumeration. The defect is the discharge-narrative tally framing, not the firm-count tallies. Location: CYCLE.md:28 (Summary) and the parallel phrase "16 demoted across c050+c051, 1 KEPT-substantive" in the C `[new]` block (CYCLE.md:67).

2. **[INFO — verified-correct, flagged for integrator attention] Serial-ordering dependency A.2 is real and load-bearing.** D5's A.2 `[old]` is byte-identical to D4's change-#6 `[new]` (confirmed by diff). The current on-disk L3-L2/index.md:61 is D4's `[old]` (`17→13`), so **A.2 will fail to match unless D4 is applied first.** D5 flags this prominently (Summary, A.2 preamble, and Open-questions). The integrator-per-report serial order (D1→D2→D3→D4→D5, D5 in the last wave-2 slot) honors it. Not a defect — D5's handling is exemplary — but the integrator must not reorder D5 ahead of D4. Note for contrast: change B has **no** such dependency — its `[old]` matches the *current* on-disk line 73 at position 0 (verified) and D4's line-73 edit is a disjoint substring starting at position 955 ("**NOTE the cycle-050-vs-051 split"), so B applies cleanly regardless of D4 ordering. D5's disjointness claim for line 73 is **confirmed correct** (the two `[old]` substrings are exactly adjacent, non-overlapping).

3. **[INFO — correct as stated] divfree-projector-leaf-identity KEEP and the c050-vs-c051 split are accurate.** Confirmed `divfree-projector-leaf-identity.md` carries one genuine `Grad->AddMult` fusion rotation (KEEP-substantive), and the D8 audit (`...verify-divfree-jacobi/CYCLE.md`) verdicts match D5's narrative (jacobi body+leaf DEMOTE-OK, divfree body DEMOTE-OK, divfree leaf KEEP). The "leaf-CHAPTER deletions remain HELD/meta-gated; only THEME files deleted this cohort" framing is consistent with the producer reports. No issue.

## Repair

### Fixes attempted

- **Finding**: [LOW issue #1] Discharge-narrative phrase "16 demoted + 1 KEPT = 17" (Summary CYCLE.md:28, echoed in change-C `[new]` ~:67) is internally unreconcilable — "16" matches no consistent counting unit, and the same-sentence parenthetical enumerates a different number.
  - **Decision**: repaired
  - **Action**: Reconciled both occurrences to a single consistent counting unit.
    - **Summary (CYCLE.md:28)** — rewrote the discharge sentence to count at the **theme** unit (the unit the parenthetical breakdown actually enumerates): **23 themes demoted + 1 KEPT = 24 themes across both edges**, with the parenthetical now summing correctly (c050 = 8 themes; c051 = 8 + 2 + 2 + 2 + 1 = 15 themes; 8 + 15 = 23). Added the explicit pair-unit cross-check tying back to the orphaned D8 denominator: of the **17 degenerate {body,leaf} pairs** (D8 −1-corrected after `divfree-projector`'s leaf edge was reclassified substantive), all 16 fully-degenerate pairs demoted both edges and the 17th (`divfree-projector`) demoted body-only with its leaf edge KEPT. Both units now agree with the enumeration.
    - **change-C `[new]` (CYCLE.md:67)** — replaced the parallel "16 demoted across c050+c051, 1 KEPT-substantive" phrase with the same reconciled framing (23 themes demoted + 1 KEPT; equivalently 16 fully-degenerate pairs + the 17th split body-demote/leaf-keep).
  - This is narrative-prose-only. The three load-bearing firm-count EDITS (A.2 L3>L2 13→5, B L2>L1 17→10 +1 partly-constructive, C L3 unchanged 17) and the A.2 serial-ordering flag (issue #2) were NOT touched.

- **Finding**: [INFO issue #2] Serial-ordering dependency A.2 (D4 before D5) — verified-correct, flagged for integrator.
  - **Decision**: not-needed (verified-correct; flag is exemplary and must stand for the integrator). No repair.

- **Finding**: [INFO issue #3] divfree-projector-leaf-identity KEEP + c050/c051 split accurate.
  - **Decision**: not-needed (correct as stated).

- **Finding**: [skill-uptake-survey — warning] No skill cited for the count-reconciliation / anchor-disjointness verification.
  - **Decision**: not-needed (pure telemetry, non-blocking; the verification was done correctly by hand). No content change in scope; the surfaced candidate gap ("consolidated cross-dispatch count reconciliation against on-disk survivor enumeration") is left for meta-phase to weigh.

### Unrepairable findings

None. The sole actionable finding (issue #1) was a contained narrative-arithmetic reconciliation — mechanical and surgical, within repair authority (made the prose self-consistent against the already-verified dispositions; authored no new substantive content and changed no verified count).

## Suggested resolution

`ready`. Integrator notes:
- **Honor the serial order**: D5's change A.2 `[old]` is byte-identical to D4's change-#6 `[new]`, so D4 MUST be applied before D5 or the A.2 anchor will not match (issue #2). Change B is a disjoint substring on L2-L1/index.md:73 (no collision, applies cleanly regardless of D4 ordering) — confirmed by the critic.
- The verified-correct firm counts stand: L3>L2 13→5, L2>L1 17→10 (+1 partly-constructive), L3 unchanged at 17 firm + 3 partial-obstruction.
- The discharge narrative now reconciles at theme-unit (23 demoted + 1 KEPT = 24) with a pair-unit cross-check (17 degenerate pairs; 16 fully demoted + 1 split).
