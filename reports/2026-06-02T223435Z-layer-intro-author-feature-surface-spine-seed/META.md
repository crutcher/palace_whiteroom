---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T231500Z
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
repaired_at: 2026-06-02T233000Z
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

# META: verification of "Feature surfaces — electrostatic exemplar (composition-root spine seed)"

## Critique

This report is the FIRST exemplar of a NEW chapter kind — the **feature-surface / composition-root** chapter — authored under the FEATURE-SURFACE SPINE user directive (2026-06-02), not yet codified into role-specs. Per the dispatch framing, the surface-or-evidence / rotation-quality / variant-axis checks ADAPT for a composition-root (evidence = L0 driver range + constituent down-links; rotation/variant largely no-op, as on a stub). I applied the adapted forms and did not mis-flag the composition-root shape on those three checks. The one substantive finding is a status-label mismatch on a constituent down-link plus several minor L0 sub-anchor drifts; everything else is sound.

### Checks run

**citation-validity — warning.** All L0 anchors were verified on-disk via palace-codemap `read_range` against `palace/drivers/electrostaticsolver.{cpp,hpp}`. The macro-ranges are correct: `Solve` body `:20-98` (line 20 = `std::pair<...>`, 21 = `ElectrostaticSolver::Solve(...)`, 98 = closing `}`), `PostprocessTerminals` def `:100-160`, `.hpp` class decl. The high-traffic mid-body anchors are exact: `:28` LaplaceOperator, `:30` GetStiffnessMatrix, `:31` GetGradMatrix, `:34` KspSolver / `:36` SetOperators, `:38` PostOperator, `:39` n_step, `:40` MFEM_VERIFY, `:44-45` RHS/V storage, `:59` family loop, `:68` GetExcitationVector, `:69` ksp.Mult, `:75-76` E=-∇V, `:89` step++, `:95` PostprocessTerminals call, `:97` return, `:111` `mfem::DenseMatrix C(...)`. Several **pinpoint sub-anchors in `electrostatic.L0.md` drift by 1–3 lines** (details under Issues): the diagonal `M_elec->Mult`/`Dot` (cited `:115-117`, actually `:118-119`), `MeasureAndPrintAll` (cited `:83`, actually `:82`), the `Cinv(C); Cinv.Invert()` inverse (cited `:137-138`, actually `:139-140`), and the COMSOL-comment range (cited `:103-109`, actually ~`:105-110`). The enclosing ranges (`:100-138`/`:100-160`) still contain all the cited content, so the drift is cosmetic-to-minor, but the named-line pinpoints are off and the `:137-138` / `:115-117` references point at lines that hold something other than the cited statement. The two on-disk constituent-page pinpoints the report re-uses are accurate: `fe_assemble.md:127` (electrostatic diffusion specialization) and `solve_family.md:107` (electrostatic terminal-boundary witness 1) both resolve and say what the report claims. No `verified_against:` YAML block is present, so that sub-check is N/A.

**surface-or-evidence — pass (adapted).** Applying the adapted form: the feature's "surface" IS the feature (the composition root config → fe_assemble → solve_family → capacitance reduction → capacitance-out), evidenced by (a) the L0 driver range `:20-98` + `:100-138` that realizes the composition and (b) the live down-links to the firm/rough-in constituent ops. Both legs are present and faithful. The composition root matches the directive's specified one and is faithfully presented at all three levels in each level's own vocabulary (high→low coherence honored). The fixed-operator characterization is correct against L0: `ksp.SetOperators(*K,*K)` at `:36` sits OUTSIDE the terminal loop (loop opens `:59`), so the operator IS captured once — the "fixed-operator / solve_family fixed-corner" framing is source-faithful. Not flagged.

**rotation-quality — pass (N/A, adapted).** A composition-root rotates nothing — it recomposes already-firm vocabulary outward rather than asserting an L_{n+1}→L_n compaction. Per the dispatch framing this check no-ops on the feature-surface kind (as it does on a stub). The report does NOT over-claim any rotation. Not applicable to the feature-surface kind; pass.

**variant-axis-coverage — pass (N/A, adapted).** A feature chapter has no variant axes of its own; the variant axes live in the constituent ops it composes (e.g. `solve_family`'s fixed-vs-per-element axis, which the report correctly attributes to `solve_family` and notes the electrostatic feature is the fixed-operator corner, NOT the driven per-element superset). No hidden branch is suppressed at the composition level. Not applicable to the feature-surface kind; pass.

**cross-reference-integrity — pass.** All down-link targets resolve on-disk: `L4/{fe_assemble,solve_family,ksp_solve}.md`, `L1/{fe_assemble,ksp_solve,matrix-weighted-norm,bilinear-form}.md` all exist. Relative paths are correct from `book/src/feature/` (`../L4/...`, `../L1/...`, inter-feature `./electrostatic.L4.md`). The SUMMARY.md `[old]` anchor matches the live file exactly (Introduction → Methodology block → `# L4` header), and the new `# Feature surfaces — entry points` Part is inserted between Methodology and L4 with all four new files wired. The `feature/` directory does not pre-exist (integration creates it). No dead links; no dangling slug.

**edge-label-fidelity — pass (N/A).** No L_{n+1}→L_n edge label is carried (this is a composition-root, not a lowering theme). The `lifts_to` / `lifts` prose in `electrostatic.L0.md` correctly describes L0→L1/L4 lifting as cross-references, consistent with the high→low discipline (the actual per-write lowering is delegated to the constituents' L1>L0 themes, not authored here). Not applicable.

**plan-kind-consistency — pass.** Declared kind `feature-surface` with status `seed (exemplar)` matches the content shape: a composition root with no new per-op algebraic claim, an "Implied-by / under-directive" provenance, and a compositional-only claim. The `seed (exemplar)` tier is correctly used (first-exemplar, ahead of role-spec codification) and the report is explicit that the column as a whole is a seed, not a firm composition (correct, since stage 3 leans on rough-in L1 primitives). Consistent.

**skill-uptake-survey — pass.** The report references the count-from-Status / survey-chapter-firmness-from-on-disk-`## Status` discipline and applied it (it surveyed each constituent's on-disk `## Status` line). The `proposed-changes-fence-encloses-full-body-guard` shape is satisfied (verified below). No missing skill invocation implied by the shape. Telemetry only; pass.

### Issues found

1. **[citation-validity / count-from-Status — primary] `matrix-weighted-norm` firmness MISLABELED as `firm`; on-disk `## Status` is `rough-in (test-coverage-bounded)`.** The report labels the diagonal capacitance primitive `L1/matrix-weighted-norm` as **firm** in five places: `electrostatic.L4.md` frontmatter prose ("firm diagonal"), the L4 §"Constituent down-links" table row ("firm / rough-in (L1)"), `electrostatic.L1.md` `composes:` frontmatter ("firm — diagonal Vᵢᵀ K Vᵢ"), the L1 down-links table row (Status "firm"), and Open-question 4 ("is **firm** (`√(xᴴ B x)`...)"). The on-disk `book/src/L1/matrix-weighted-norm.md` `## Status` line reads `rough-in (test-coverage-bounded)` (no dedicated Palace test exercises the SPD-weighted overload at the exact entry point; cycle-009 precedent). This is a count-from-Status-guard violation: a constituent down-link carrying an inaccurate firmness label. Severity: **medium** — it does not break the link (the target is correct) but it overstates the composition's firmness floor. Consequence cascade: the report's own conclusion ("Three of the four composed L1 operators are firm ... the off-diagonal `bilinear-form` is rough-in" in `electrostatic.L1.md` §Status) is wrong — only TWO of the four are firm (`fe_assemble`, `ksp_solve`); BOTH bilinear primitives (`matrix-weighted-norm` diagonal AND `bilinear-form` off-diagonal) are rough-in. The "Why this is the cleanest exemplar" / firmness narrative should be corrected to reflect that the entire stage-3 reduction rests on rough-in L1 primitives. Locations: `electrostatic.L4.md` (composes-prose + §down-links table + §Status), `electrostatic.L1.md` (`composes:` frontmatter + §3 prose "firm diagonal" + §down-links table + §Status), CYCLE.md Open-question 4.

2. **[citation-validity — minor] L0 pinpoint sub-anchor drift in `electrostatic.L0.md`.** Four named-line citations are off by 1–3 lines from the on-disk source:
   - Diagonal energy-form `M_elec->Mult(V_gf, D_gf)` then `linalg::Dot` cited `:115-117` — actual `Mult` is line **118**, `Dot` line **119**; `:115-117` covers only the `V_gf`/`D_gf` decls + `SetFromTrueDofs`. (`electrostatic.L0.md` §"composition in source" stage 5, and `electrostatic.L1.md` §3 reuses `:115-117`.)
   - `PostprocessTerminals` inverse `mfem::DenseMatrix Cinv(C); Cinv.Invert()` cited `:137-138` — actual is **`:139-140`**; lines 137-138 are closing `}` braces. (`electrostatic.L0.md` §stage 5 + §I/O; also the L4/L1 chapters reference `:137-138`.)
   - `MeasureAndPrintAll(step, V[step], E, idx)` cited `:83` — actual line **82** (`:83` is blank). (`electrostatic.L0.md` §I/O.)
   - COMSOL p.97 comment cited `:103-109` — the manual reference actually sits ~`:105-110`. (`electrostatic.L0.md` §stage 5.)
   The enclosing macro-ranges (`:100-138` / `:100-160`) remain correct and contain all cited content, so this is minor, but the pinpoints should be nudged to the exact lines. Severity: **low**.

3. **[framing finding → route to batch-22 meta-phase, NOT a hard fail] adapted-check no-op needs codification.** Per the dispatch framing and CYCLE.md Open-question 1, the feature-surface kind needs its surface-or-evidence check formally adapted (evidence = driver range + down-links) and its rotation-quality / variant-axis-coverage checks formally no-op'd (analogous to the `stub` tier). I applied these adaptations by hand for this critique; absent codification, a future critic without the dispatch framing would likely mis-flag rotation-quality and variant-axis-coverage as failing on the composition-root shape. This is a real friction with the current 8-check checklist vs. the new kind — recorded here as a meta-phase-routed finding (it is the report's own Open-question 1, confirmed from the critic side). Severity: **methodology (non-blocking)**.

4. **[observation, non-blocking] level-ordering and path-layout are deliberate exceptions awaiting meta-phase ratification.** The column orders levels L4→L1→L0 (high→low reading) NOT alpha-by-filename, and uses flat `feature/electrostatic.<level>.md` naming. The report flags both as deliberate exceptions for the batch-22 meta-phase to ratify or correct (CYCLE.md Open-question 2). I concur these are sane seed choices (high→low matches the spine reading order; flat naming avoids over-structuring a 1-column Part) and surface no integrity problem now; noting them so the meta-phase decision is on record. Severity: **none (forward note)**.

Fence/build-readiness note (cross-reference-integrity sub-check): the proposed-changes block carries 5 `edit:` fences, each opening and closing cleanly (63→79, 81→115, 117→187, 189→256, 258→307), with every full chapter body (frontmatter, `## Status`, composition, tables) INSIDE its fence. The in-chapter code blocks use 4-space-indented code rather than nested ```` ``` ```` fences, sidestepping the nested-fence truncation hazard. No firm-body-outside-fence defect.

## Repair

### Fixes attempted

- **Finding 1 — `matrix-weighted-norm` firmness MISLABELED `firm`; on-disk `## Status` is `rough-in (test-coverage-bounded)` (citation-validity / count-from-Status, MEDIUM).**
  - **Decision**: repaired.
  - **Action**: Confirmed on-disk via grep of each constituent's `## Status` line: `L1/matrix-weighted-norm.md` → `rough-in (test-coverage-bounded)`; `L1/bilinear-form.md` → `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`; `L1/fe_assemble.md` → `firm`; `L1/ksp_solve.md` → `firm`. So exactly **two of four** L1 constituents firm (`fe_assemble`, `ksp_solve`); BOTH capacitance-reduction primitives rough-in. Corrected the `firm` → `rough-in (test-coverage-bounded)` label for `matrix-weighted-norm` in all flagged proposed-changes locations:
    - `electrostatic.L4.md`: stage-(3) prose ("the rough-in L1 matrix-weighted-norm"), §"Why this is the cleanest exemplar" ("rough-in diagonal + rough-in off-diagonal"), §Constituent-down-links table row (`rough-in / rough-in (L1)`), §Status ("rough-in diagonal matrix-weighted-norm").
    - `electrostatic.L1.md`: `composes:` frontmatter row, §3 reduction prose ("the rough-in matrix-weighted-norm"), §down-links table row (Status → `rough-in (test-coverage-bounded)`), and §Status narrative rewritten from "Three of the four composed L1 operators are firm (…matrix-weighted-norm)" → "Two … firm (fe_assemble, ksp_solve); BOTH capacitance-reduction primitives are rough-in … the entire stage-3 reduction rests on rough-in L1 primitives".
    - CYCLE.md Open-question 4 rewritten: both reduction primitives stated rough-in with the correct on-disk `## Status` strings; OQ3 "firm matrix-weighted-norm diagonal" → "rough-in"; the two report-internal mentions (L0-anchors-confirmed list + Supporting-evidence list) corrected from `(firm)` → `(rough-in (test-coverage-bounded))`.
  - This is the count-from-on-disk-`## Status` guard (c057-meta): the corrected firmness floor is now consistent across frontmatter + both tables + prose + OQ.

- **Finding 2 — L0 pinpoint sub-anchor drift in `electrostatic.L0.md` (citation-validity, LOW).**
  - **Decision**: repaired.
  - **Action**: Re-confirmed each via palace-codemap `read_range` on `palace/drivers/electrostaticsolver.cpp` and corrected the pinpoints in the proposed-changes (and the matching report-internal anchor-list entries):
    - diagonal `M_elec->Mult`/`linalg::Dot`: `:115-117` → **`:118-119`** (118 = `M_elec->Mult(V_gf, D_gf)`, 119 = `C(i,i) = … linalg::Dot`; 115–117 are the `V_gf`/`D_gf` decls + `SetFromTrueDofs`). Corrected in `electrostatic.L0.md` §"composition in source" stage 5, `electrostatic.L1.md` §3 + §down-links table, and the CYCLE.md anchor-list.
    - inverse `Cinv(C); Cinv.Invert()`: `:137-138` → **`:139-140`** (137–138 are `}` braces; 139 = `mfem::DenseMatrix Cinv(C)`, 140 = `Cinv.Invert()`). Corrected in `electrostatic.L0.md` stage 5 + §I/O, `electrostatic.L1.md` §3, `electrostatic.L4.md` stage-(3) prose, and the anchor-list.
    - `MeasureAndPrintAll(...)`: `:83` → **`:82`** (82 = the `auto total_domain_energy = post_op.MeasureAndPrintAll(...)` call; 81 = comment, 83 = blank). Corrected in `electrostatic.L0.md` §I/O.
    - COMSOL p. 97 comment: `:103-109` → **`:105-110`** ("See p. 97 of the COMSOL AC/DC Module manual" begins line 105; the comment block runs 105–110; 104 = `{` brace, 111 = `mfem::DenseMatrix C`). Corrected in `electrostatic.L0.md` stage 5.
  - The macro-ranges (`:20-98` / `:100-160`, `:100-138`) were verified correct and left unchanged; `:111` (`mfem::DenseMatrix C`) and `:122-127` (off-diagonal loop) confirmed correct and left unchanged.

### Unrepairable findings

None. Both substantive findings were surgical (firmness-label corrections + citation-line corrections) and applied in place.

The critic's framing findings (Issue 3 — feature-surface-kind adapted-check codification; Issue 4 — level-ordering L4→L1→L0 + flat `feature/<feature>.<level>.md` path-layout ratification) are **correctly routed to the batch-22 meta-phase**, not defects to repair. They remain as CYCLE.md Open-questions 1 and 2, untouched — they are methodology-level decisions outside repair authority (and the report itself surfaces them as meta-phase ASKs).

## Suggested resolution

`ready` — all critic findings are `pass` (from critic) or `repaired`. Integrator notes:
- The new `feature/` Part directory does not pre-exist; integration creates `book/src/feature/{index,electrostatic.L4,electrostatic.L1,electrostatic.L0}.md` and inserts the `# Feature surfaces — entry points` Part into `SUMMARY.md` between Methodology and L4 per the report's `edit:book/src/SUMMARY.md` `[old]` anchor.
- This is the FIRST exemplar of the feature-surface chapter kind (seed, ahead of role-spec codification). The two open meta-phase questions (adapted-check codification; level-ordering / path-layout ratification) should be carried into the batch-22 meta-phase — they are on record in both the critique (Issues 3/4) and the report's Open-questions.
- The firmness floor now correctly reads "two of four L1 constituents firm" with the whole stage-3 reduction resting on rough-in primitives, consistent with the column's `seed (exemplar)` maturity.
