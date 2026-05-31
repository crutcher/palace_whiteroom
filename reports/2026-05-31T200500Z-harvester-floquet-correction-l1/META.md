---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T20:30:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-31T20:45:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of harvester floquet-correction L1 + L1>L0 theme

## Critique

### Checks run

**citation-validity — pass.** Mechanical: `python3 tools/citecheck/citecheck.py --scan reports/2026-05-31T200500Z-harvester-floquet-correction-l1/CYCLE.md --quiet` reproduces the report's claim of **96 ok, 0 failing**. Independent on-disk spot-check of the load-bearing pinpoints (the codemap can drift ±1; on-disk is the truth):

- `palace/linalg/floquetcorrection.cpp:73-78` — Mult body — VERIFIED on disk: `Cross->Mult(x, rhs); ksp->Mult(rhs, y);` at exactly :76-77 inside the `Mult` body at :74-78 (sig :73-74, brace :75, body :76-77, close :78). The two-step apply claim is exact.
- `palace/linalg/floquetcorrection.cpp:80-86` — AddMult body — VERIFIED: `this->Mult(x, rhs); rhs *= a; y += rhs;` at exactly :83/:84/:85. Lines map exactly to the report's claims (`:83` `this->Mult(x, rhs)`, `:84` `rhs *= a`, `:85` `y += rhs`, `:86` close).
- `palace/linalg/floquetcorrection.cpp:88` — `template class FloquetCorrSolver<ComplexVector>;` — VERIFIED as the sole instantiation; no `<Vector>` line in the file.
- `palace/linalg/floquetcorrection.cpp:20-71` — constructor — VERIFIED: sig :20-23 (4 lines), `M_RT` assembly :26-39 (with `BilinearForm a(rt_fespace)` at :28, `VectorFEMassIntegrator` at :29, `ComplexParOperator` wrap at :33, real-branch dead code at :35-38), `Cross` assembly :41-57 (with `MaterialPropertyCoefficient` at :42, `GetFloquetCross()` at :43, `BilinearForm a(nd_fespace, rt_fespace)` at :45, `VectorFEMassIntegrator(f)` at :46, `ComplexParOperator` wrap at :50-51, real-branch dead code at :53-56), ksp setup :60-67 (with `CgSolver` at :60, `JacobiSmoother` at :65, `SetOperators(*M, *M)` at :67), scratch sizing :69-70, close brace :71. Every sub-range is exact.
- `palace/linalg/floquetcorrection.cpp:35-38, :53-56` — real-branch dead code — VERIFIED: the `else { ... ParOperator ... }` blocks exist at exactly these ranges; dead under the `<ComplexVector>`-only instantiation.
- 4 consumer AddMult sites — all VERIFIED: `drivensolver.cpp:212` (with doc comment at :211), `drivensolver.cpp:336` (with doc comment at :335), `drivensolver.cpp:468` (with doc comment at :467), `eigensolver.cpp:454` (with doc comment at :453). All four bear the inline comment `// B = -1/(iω) ∇ x E + 1/ω kp x E[.]` as claimed.
- 3 construction sites — all VERIFIED: `drivensolver.cpp:138/141` (declaration at :138, `make_unique` at :141), `drivensolver.cpp:289/292`, `eigensolver.cpp:237/240`. All declare `std::unique_ptr<FloquetCorrSolver<ComplexVector>>`.
- `palace/models/materialoperator.hpp:103,128` — per-attribute / all-attributes `GetFloquetCross` accessors — VERIFIED.
- `palace/models/materialoperator.hpp:136` — `HasWaveVector` — VERIFIED.
- `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0, wave_vector_cross);` — VERIFIED.
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult` — VERIFIED.

All 16 anchor-checked claims survive independent on-disk verification; no drift. The 96/96 scan-clean number is reproducible. Pass.

**surface-or-evidence — pass.** This is a refinement-shaped harvester report (new firm L1 operator + new firm L1>L0 theme + dep-map edits + concept-page upgrade). All new content is L1 / L1>L0 surface modification AND every claim has L0 backing citations (16 anchor-checked, 96 total). The L1 floquet-correction body, the L1>L0 4-sub-pattern theme, the L1 index dep-map row, the L1-L0 index dep-map row, the SUMMARY.md registrations, and the concept-page §Firm-instances upgrade 2→3 are all surface; the algebraic laws and structural sub-patterns are all evidence-backed.

**rotation-quality — pass.** Genuine forward L1→L0 narration. The L1 form `y = floquet_correction(F, x) = F.M_RT⁻¹ · F.Cross · x` is defined in L1 vocabulary (closure value F carrying `(M_RT, Cross, ksp)` fields, pure-functional value return) and is genuinely more compact / more equational than the L0 form (the L0 mutates `y` through output arg, threads a construction-bound `mutable rhs` scratch member, sequences `Cross->Mult(x, rhs); ksp->Mult(rhs, y);`, and the construction is 50 lines of `BilinearForm`+`Assemble`+`ComplexParOperator` wrapping). The state hiding is real: destination buffer absorbed into return-value, scratch member erased, construction-time integrator-assembly absorbed into closure `F`. The `AddMult = axpy ∘ floquet_correction` fusion is a sound algebraic identity. The aliased `ksp->Mult(rhs, rhs)` case (when AddMult's inner `this->Mult(x, rhs)` re-binds the `Mult` output arg to the scratch `rhs`, so step 2 inside `Mult` becomes `ksp->Mult(this->rhs, y_arg=this->rhs)`) is correctly identified as a load-bearing applicability condition (sub-pattern B + applicability condition 2), with `palace/linalg/ksp.cpp:297` cited as the inner-ksp site that tolerates the aliasing. Not a 1:1 rename. Not identity. A real rotation.

**variant-axis-coverage — pass.** The element-type axis is exhaustively handled: the report identifies `<ComplexVector>` as the SOLE instantiation at `palace/linalg/floquetcorrection.cpp:88` (independently verified — `grep '^template class' floquetcorrection.cpp` returns only the `<ComplexVector>` line), names the real-branch `if constexpr` dead-code at `:35-38, :53-56` (independently verified), and scopes out `<Vector>` as **non-axis** (the parametric template is dead code in any hypothetical real-only client; no real-typed driver call sites exist). The "first L1 constructed-operator gate with a deliberately-narrowed element-type scope" claim is independently CONFIRMED by cross-check: `divfree.cpp:189-190` carries BOTH `<Vector>` and `<ComplexVector>` template-class lines; `jacobi.cpp:106-107` carries BOTH `<Operator>` and `<ComplexOperator>`; `floquetcorrection.cpp:88` carries ONLY `<ComplexVector>`. The Mult vs AddMult apply-surface axis is handled exhaustively (sub-patterns A and B). The construction site (sub-pattern C) covers the full closure-field materialisation. Sub-pattern D codifies the scope-out as its own sub-pattern. No hidden branches.

**cross-reference-integrity — fail.** All `[link]` references resolve on disk (all L1 targets `apply_linop.md`, `axpy.md`, `chebyshev-smoother.md`, `divfree-projector.md`, `eigsolve.md`, `jacobi-smoother.md`, `ksp_solve.md` exist; all L1-L0 themes `apply-linop-mutation-rotation.md`, `chebyshev-smoother-mutation-rotation.md`, `divfree-projector-mutation-rotation.md`, `eigsolve-mutation-rotation.md`, `jacobi-smoother-mutation-rotation.md`, `ksp-solve-mutation-rotation.md` exist; all concept references `nested-constructed-operator-gate.md`, `solver-as-operator.md`, `constructed-operator-factory.md` exist). All SEARCH blocks for SUMMARY.md (lines 90 + 106-107), L1 index (line 31 + the elementwise_product row at :103 + the §Vocabulary `elementwise_product` paragraph), L1-L0 index (line 43), and `nested-constructed-operator-gate.md` (the firm-instances section + latent-site paragraph + see-also paragraph) match on-disk content exactly.

**HOWEVER**, the **firm-body-inside-fence guard** fails on the FIRST proposed-changes block — the `new:book/src/L1/floquet-correction.md` block at lines 28-433. Mechanical enumeration of top-level fences in CYCLE.md:

    Line 28:  ```new:book/src/L1/floquet-correction.md   ← OPEN (1)
    Line 104: ```text                                     ← (2)
    Line 111: ```                                         ← (3)
    Line 433: ```                                         ← (4)

Per strict CommonMark / mdBook parsing, the ```` ```text ```` at line 104 (same backtick count as the outer fence) **CLOSES** the outer `new:book/src/L1/floquet-correction.md` block, not opens a nested code block. The ```` ``` ```` at line 111 then OPENS a fresh anonymous code fence (its content is the "Shape contract" prose), and the ```` ``` ```` at line 433 closes that. **Net effect**: the firm body for `book/src/L1/floquet-correction.md` includes only lines 29-103 (the intro through the §Context paragraph) — **everything from §Signature onward (lines 112-432) is authored as the report's OWN top-level sections OUTSIDE the proposed-changes fence**. Per friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` (cycle-019; the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill is the codified repair).

The second new: block (`new:book/src/L1-L0/floquet-correction-mutation-rotation.md`, lines 435-961) is **clean** — its sub-pattern code uses 4-space indentation (lines 494-499, 558-564, etc.) per the cycle-024 repair pattern, no nested ```text fences.

The four edit: blocks (lines 963, 985, 994, 1016) are also clean.

The defect is **localised to the FIRST proposed-changes block**, and is the canonical firm-body-outside-fence pattern: a `firm`-claimed chapter whose `Signature`, `Semantics`, `Algebraic laws`, `Dependencies`, `Status`, `Evidence` sections — i.e. all of the firm apparatus per the §Status `firm` claim at line 327 — are authored OUTSIDE the fence. Mechanical fix: convert the inner ```text ... ``` fence at lines 104-111 to a 4-space-indented code block (the same approach used in the second `new:` block).

**edge-label-fidelity — pass.** Dep-map row uses `firm` status. L1 count update is 25→26. L1>L0 theme is named `floquet-correction-mutation-rotation` consistent with the L1>L0 directory naming convention (the lowering theme name = `<operator>-mutation-rotation` per the firm cohort: `divfree-projector-mutation-rotation`, `jacobi-smoother-mutation-rotation`, etc.). The narration is L1→L0 forward (LHS L1 form, RHS L0 form, prose narrates the rewrite). The dep-map rows in both L1/index.md and L1-L0/index.md correctly attribute `firm` and cite the harvested-cycle.

**plan-kind-consistency — pass.** Declared `firm` is justified: every step of the apply is read from a positive Palace source site (`floquetcorrection.cpp:73-86`), construction is exhaustively cited (`:20-71`), and the linearity / range / composition / step-ordering / complex-linearity / non-laws follow directly from the source-stated two-step body and the SPD/real properties of the construction. The "firm-on-positive-structure escape" for the missing dedicated unit test is correctly invoked, citing the `divfree-projector` + `jacobi-smoother` + `chebyshev-smoother` + `apply_linop` precedent cohort (where every law is a syntactic identity on fully-specified positive source). The test-absence is acknowledged (`test/unit/test-floquetcorrection.cpp` absent, only `test/unit/test-schema.cpp:340-353` and `test/examples/runtests.jl:289-294` exist) and explicitly does NOT block `firm`. No partly-constructive caveat needed (no constructed-from-negative-anchors sub-part). Not a mis-classification.

**skill-uptake-survey — pass.** `citecheck` invocation is explicit in §"Self-check: `citecheck --scan`" (line 1213-1217) and §"Citation self-verification" (line 1164-1183) — the 16 `--anchor` checks plus the 96/96 `--scan` are the cycle-024 mechanical-realisation pattern. The `proposed-changes-fence-encloses-full-body-guard` skill is the one whose detection was MISSED by the producer (it's a producer-side guard the harvester should have run before emitting; the same skill is the critic-side detection mechanism applied here in this critique).

### Issues found

1. **[CYCLE.md proposed-changes block #1, lines 28-433 — first `new:book/src/L1/floquet-correction.md` block: nested-fence truncation defect.] severity: high.** The block contains a nested ```` ```text ```` fence at line 104 with a matching ```` ``` ```` at line 111. Standard markdown / mdBook parsing closes the outer `new:` fence at line 104 (same delimiter), so the integrator's proposed-changes parser will write `book/src/L1/floquet-correction.md` with content from lines 29-103 only — the intro paragraph + §Context. **The §Signature, §Semantics, §Algebraic laws, §Dependencies, §Status, §Evidence sections (lines 112-432) — i.e. the entire firm apparatus the `## Status: firm` claim depends on — fall OUTSIDE the fence** and are authored as top-level sections of the CYCLE.md report rather than as content of the target chapter. This is friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` (cycle-019); the codified repair is skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` (cycle-024): convert the inner `text`-fenced Signature block at lines 104-111 to a 4-space-indented code block (same pattern the second `new:` block already uses for ITS code excerpts at lines 494-499, 558-564, 617-619, etc.). Without the repair, the integrator would land a defective `floquet-correction.md` containing only the intro + §Context, and the rest of the firm apparatus would be lost. Repairable mechanically.

2. **[CYCLE.md §Dependencies (theme), line 651 — slug mismatch on cross-reference.] severity: low.** The theme's §Justification kind paragraph at line 648-659 cross-references `[ksp-solve](./ksp-solve-mutation-rotation.md)` but the path is correct; the issue is that the L1-L0 directory uses `ksp-solve-mutation-rotation.md` (verified — exists), so this link DOES resolve. Not a defect; recording as a no-op verification note (originally suspected, retracted on inspection). Skip.

3. **[CYCLE.md L1-L0 theme §Justification kind, line 813 — `algebraic` rule scope.] severity: low / note.** The justification for sub-pattern B reads "`algebraic` (the AddMult-into-axpy unfolding is the `axpy(α, a, b) = a·α + b` definition with `a = floquet_correction(F, x)` and `α = a` *plus* the structural buffer-economy claim …)" — the variable-name collision between the L1 algebraic `axpy` argument `a` and the L0 scalar argument `a` is confusing but not wrong. Worth a tiny rename pass for prose clarity (e.g. rename the L0 scalar to `α` in the prose for consistency). Not a check failure.

4. **[CYCLE.md §"Self-check: `citecheck --scan`" line 1215 — self-check is reproducible.] note.** Independently reproduced the 96/96 number via `python3 tools/citecheck/citecheck.py --scan reports/2026-05-31T200500Z-harvester-floquet-correction-l1/CYCLE.md --quiet`. Not an issue.

### Summary of severity

- **One high-severity issue**: the L1 `floquet-correction.md` proposed-changes block has the nested-`text`-fence truncation defect (cycle-019 / cycle-024 lineage; canonical mechanical repair exists).
- **No other issues** beyond the prose-clarity note in (3).
- All 16 representative on-disk anchors verify exactly; the 96/96 citecheck scan is reproducible; the element-type scope-out claim is independently confirmed by direct grep against `divfree.cpp` / `jacobi.cpp` / `floquetcorrection.cpp` template-instantiation lines. The defect is **mechanical and surgical** (convert lines 104-111 from ```text``` fence to 4-space indent), well within repair authority.

## Repair

### Fixes attempted

- **Finding**: cross-reference-integrity — first `new:book/src/L1/floquet-correction.md` proposed-changes block (lines 28-433) contains a nested ```` ```text ... ``` ```` fence at lines 104-111 that, under strict CommonMark / mdBook parsing, closes the outer same-delimiter `new:` fence at line 104. Net effect: §Signature through §Evidence (lines 112-432, the entire firm apparatus the `## Status: firm` claim depends on) authored OUTSIDE the proposed-changes fence; integrator would land a defective `floquet-correction.md` containing only intro + §Context. Recurrence-3 of friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` (cycle-019); detection by skill `proposed-changes-fence-encloses-full-body-guard` (cycle-021); mechanical repair by skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` (cycle-024).
  - **Decision**: repaired.
  - **Action**: applied `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill — converted the nested ```` ```text ```` fence at CYCLE.md:104-111 (the §Signature pseudo-code block: `floquet_correction :: ...` plus the 3-line equational rewrite) to a 4-space-indented code block. The outer surrounding text ("## Signature" header above, "Shape contract (bunsen-style; named axes):" prose below) is preserved verbatim. No content was added, removed, or reworded — purely a fence→indent structural rewrite of the same 7 code lines.
  - **Verification**:
    - Top-level fence enumeration via `grep -n '^```' CYCLE.md` now shows: line 28 (`new:` opens) → line 431 (closes) → line 433 (second `new:` opens) → line 959 (closes) → 4 `edit:` blocks each paired (961/981, 983/990, 992/1012, 1014/1149). The first `new:` block opens once and closes once, enclosing the FULL firm body (intro through §Evidence at line 430). No inner ```` ``` ```` delimiter remains inside it.
    - The second `new:` block (the L1>L0 theme, lines 433-959) is UNCHANGED — still uses 4-space indentation for its sub-pattern code per the cycle-024 repair pattern.
    - The four `edit:` blocks (SUMMARY.md, L1/index.md, L1-L0/index.md, concepts/nested-constructed-operator-gate.md) are UNCHANGED.
    - `python3 tools/citecheck/citecheck.py --scan reports/2026-05-31T200500Z-harvester-floquet-correction-l1/CYCLE.md --quiet` reports **96 ok, 0 failing (96 citations checked)** — identical to the pre-repair number; no citation drift.
    - The `## Status: firm` declaration (now at CYCLE.md:323-325) and all subsequent §Status / §Evidence content are now correctly enclosed within the first `new:` proposed-changes fence; integrator will land the full firm chapter body.

### Unrepairable findings

None. The single cross-reference-integrity FAIL was the canonical fence-truncation defect with a codified mechanical repair (skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`). All 7 other checks were PASS → not-needed.

### Recurrence note for batch-10 meta-phase

This is **recurrence-3** of the friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` pattern (originally codified cycle-019; the cycle-021 detection guard `proposed-changes-fence-encloses-full-body-guard` and the cycle-024 mechanical repair `convert-nested-fences-to-indented-code-in-proposed-changes-block` are both already in the skills library). The critic's detection guard caught the defect cleanly; the repairer's mechanical fix applied without complication. Surfacing for the batch-10 meta-phase (which fires after cycle-036's integrator-finalize) as evidence that despite two codified skills, **producer-side prevention has not landed** — the harvester wrote the same defect that has now surfaced 3 times (cycle-019, prior recurrence, this one). Meta-phase consideration: is a producer-side pre-emission guard warranted (e.g. a producer-checklist bullet "verify no nested ```` ``` ```` delimiters inside `new:` blocks; if needed, use 4-space indent") or is post-hoc critic-detection + repairer-fix the steady-state regime?

## Suggested resolution

`ready` — the integrator can apply this report as-is. The first `new:book/src/L1/floquet-correction.md` proposed-changes block now encloses the full firm body (intro through §Evidence). The second `new:book/src/L1-L0/floquet-correction-mutation-rotation.md` block, plus the four `edit:` blocks for SUMMARY.md, L1/index.md, L1-L0/index.md, and concepts/nested-constructed-operator-gate.md, are unchanged and ready to apply. The critic's prose-clarity note (item 3, the `axpy` argument-name collision in the L1>L0 theme's §Justification kind paragraph) is informational only, not a check failure, and the repairer leaves it for an eventual prose-polish pass — repair authority does not extend to renaming variables in claim text.
