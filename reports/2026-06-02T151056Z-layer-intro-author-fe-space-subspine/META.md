---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T16:05:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T16:20:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "L1 intro — FE-space sub-spine framing + consolidated count" (cycle-064 D4)

## Critique

### Checks run

**citation-validity — warning.** The report's load-bearing claim is arithmetic, not a source pinpoint, and the arithmetic is correct: I counted the firm rows in the on-disk `book/src/L1/index.md` dep-map table (lines 86-118) and found exactly **31** `firm` rows (axpy, dot, nrm2, axpby, scal, normalize, apply_linop, axpbypcz, ksp_solve, eigsolve, orthogonalize, chebyshev-smoother, divfree-projector, assemble-diagonal, apply_nonlinear_pencil, nleps_deflated_residual, lu_solve, nleps_deflated_solve, nleps_jacobian_action, nleps_eigenvalue_correction, back_solve, ls_update_column, jacobi-smoother, reciprocal, elementwise_product, floquet-correction, assemble_frequency_operator, fe_assemble, eliminate_rhs, eliminate_essential_bc, weak_form_term); the rough-in `matrix-weighted-norm`/`bilinear-form` rows and the 6 obstruction rows are correctly excluded. 27 main + 4 FE-assembly (`fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs`) = 31 pre-c064; `fe_space` is +1 → 32. The header pre-edit (line 31) reads `31`, matching. Edit 1 `[old]` block reproduces the on-disk header verbatim. The count-owner guard (chapter-`## Status`-sourced, not index cells) is honored and explicitly narrated. The arithmetic and the "cycle-063 added no firm operator (NO-ENTRY warrant cycle)" premise both check out (the L1 §Working-Notes cycle-063 bullet at lines 137-140 confirms three NO-ENTRY warrants, zero new firm operators). **Warning** is for a minor citation drift in the co-authored framing prose: Edit 2 cites the variadic ctor as `palace/fem/fespace.hpp:67-75`, but the constructor block is at **66-74** (read-range confirmed: `template<...>` at 66, ctor signature 67, forwarding-init `fespace(&mesh.Get(), ...)` 68, body 69-73, close 74) — and the D1 survey it forwards from uses `:66-74` (survey line 200). A 1-line down-shift; the anchor still lands on the ctor but does not match the cited source's first line and is inconsistent with its own evidence source. The `:93-103` dof-accessor span is acceptable (accessors 91-100, prolongation/restriction forwarders 101-102).

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme; this is a new framing subsection (front-shell) plus a count-line refresh. No rotation_claim obligation. Edit 2 establishes new index prose; Edit 1 updates a tally. Both are additive index surface, appropriately evidenced against the D1 survey.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted in this report — it is a layer-intro framing + count consolidation. The actual L1>L0 rotation lives in D3's theme, which this report correctly does not author.

**variant-axis-coverage — pass.** The de-Rham family variant axis (H1/H(curl)/H(div)/L2 ↔ collection type) is named in-scope; the MFEM-owned axes (dof numbering, ordering, conformity, prolongation) are explicitly scoped out as read-as-given; MPI/`Par*`/partitioning are scoped out per CLAUDE.md §Scope. The 3-way boundary is a clean variant-axis disposition with no hidden branches. The "do NOT split into `fe_space`+`dof_map`" note correctly forecloses the identity-in-named-terms mirror.

**cross-reference-integrity — warning (the load-bearing finding; see Issues #1).** I verified D4's 3-way boundary against the D1 survey (`...-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` §1, lines 34-82): in-scope construction+typed-identity+de-Rham-family, MFEM-owned dof/ordering/conformity/prolongation-read-as-given, out-of-scope MPI/`Par*`/partitioning — D4's framing is **faithful** to the survey. The deferred siblings (`fe_collection`, `essential_dofs`, `fe_space_hierarchy`, `BuildDiscreteInterpolator`, `BuildProlongationAtLevel`) are correctly rendered **plain-text** with `*(rough-in; no anchor yet)*` (no live links to non-existent files — `rough-in-forward-reference-must-be-plain-text` honored). The two co-landing live links (`./fe_space.md`, `../L1-L0/fe-space-construction-rotation.md`) follow the `weak_form_term` c061 co-landed-row precedent and resolve at rebuild time. **The warning is the cohort-placement conflict with wave-mate D2** — see Issue #1.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried in this report; the L1>L0 edge belongs to D3.

**plan-kind-consistency — pass.** The report's shape (intro/framing + count-owner consolidation) matches its declared scope. D4 correctly scopes itself to (1) the FE-space sub-spine framing prose and (2) the consolidated grand-total, and explicitly does NOT author D2's dep-map row / cohort bullet nor D3's theme row (lines 35-38) — the dual-registration partition is respected. No mis-classification.

**skill-uptake-survey — warning.** No skill is referenced. The `summary-md-surgical-insert` skill is not invoked, but Edit 2 is an `index.md` subsection insert, not a `SUMMARY.md` edit, so that skill does not strictly apply. There is no count-owner-specific skill to cite. This is a pure telemetry surface, non-blocking — flagged only because count-discipline is a recurrent c057-meta concern that might warrant a procedure the report could have referenced.

### Issues found

**Issue #1 (cross-reference-integrity; HIGH — the key reconciliation finding) — D2/D4 cohort-placement conflict that the integrator MUST reconcile.** `CYCLE.md` Edit 2 (the new "Firm (FE-space sub-spine — 1; opened cycle-064)" subsection) places `fe_space` as its **own** FE-space sub-spine, distinct from FE-assembly, and keeps the FE-assembly sub-spine at **4**. The wave-mate D2 harvester (`reports/2026-06-02T151056Z-harvester-fe-space/CYCLE.md`) instead places its `fe_space` member bullet **under the FE-assembly sub-spine subsection** (D2 line 253, bulleted alongside the four FE-assembly members) and asserts (D2 lines 256, 335) "the FE-assembly sub-spine is **5** members (was 4)" / "the FE-assembly sub-spine grows 4→5". **Both agree the grand total is 32**, but they disagree on the sub-spine partition. **Assessment: D4's framing is the correct cohort structure.** `fe_space` *constructs* the space (`(mesh, FECollection) → FiniteElementSpace[N]`); `fe_assemble`/`weak_form_term`/`eliminate_*` *fold over / post-compose on* an already-constructed space — they are distinct vocabulary fronts (the D1 survey §4 itself frames `fe_space` as the upstream substrate the assembly front takes opaquely, and D4's "this sub-spine is upstream of the FE-assembly sub-spine" prose captures this correctly). Folding `fe_space` into the FE-assembly count conflates a construction primitive with the assembly fold. **Integrator action required:** apply D4's separate "FE-space sub-spine" subsection; do NOT also apply D2's `fe_space` bullet under the FE-assembly subsection (that would create a duplicate/conflicting member bullet); ensure the FE-assembly sub-spine header stays "**4**" (NOT 5 — D2's "grows 4→5" line must not be carried into the FE-assembly subsection header); D2's cohort bullet content is otherwise sound and should be relocated into D4's FE-space sub-spine subsection (or D4's subsection prose used in its place). The grand total (32) is consistent across both regardless, so the reconciliation is purely partition placement, not arithmetic.

**Issue #2 (citation-validity; LOW) — 1-line ctor citation drift in Edit 2 framing prose.** `palace/fem/fespace.hpp:67-75` (cited for "the Palace-side pairing of a mesh with an FE collection" / variadic ctor) should be `:66-74` to match the actual constructor block (template line 66 through close-brace 74) and to be consistent with the D1 survey (line 200) and D2 (dep-map row, `:66-74`) it forwards from. The anchor still lands on the ctor; this is a cosmetic off-by-one + inter-report inconsistency, not a wrong target. Repairer may align to `:66-74`.

**Issue #3 (LOW; informational, not a defect) — integrator-contingency self-flag is appropriate.** The report's own Open-questions (lines 128-134) correctly flag that if D2's `fe_space` lands at a maturity other than firm, the 32/1 counts must drop. Verified against D2's actual proposed `## Status`: D2 lands `fe_space` **firm** (clean-gate PROMOTE, D2 line 253/262), so the contingency does not fire — the 32 grand total holds. No action; noting that the self-flag was correct and is now resolved by the on-disk D2 status.

## Repair

### Fixes attempted

- **Finding (Issue #2, citation-validity, LOW)**: Edit 2 framing prose cited the FiniteElementSpace variadic ctor as `palace/fem/fespace.hpp:67-75`; the canonical ctor block (verified by critic via read-range: template line 66, signature 67, close-brace 74) is `:66-74`, also matching the D1 survey (line 200) and D2's dep-map row.
  - **Decision**: repaired.
  - **Action**: corrected `:67-75` → `:66-74` in two places in `CYCLE.md` — (1) the in-scope bullet of Edit 2's framing prose ("the Palace-side pairing of a mesh with an FE collection"), and (2) the §Supporting-evidence "Palace source" line (same anchor, same off-by-one), for inter-report consistency. Small-offset citation slip, squarely in repair authority.

- **Finding (Issue #1, cross-reference-integrity, HIGH — the key reconciliation)**: D2/D4 cohort-placement conflict. D4 places `fe_space` as its own "FE-space sub-spine — 1" subsection (FE-assembly stays 4); D2 placed its `fe_space` bullet under FE-assembly + asserted "FE-assembly grows 4→5". Critic's assessment: D4's framing is the correct/authoritative cohort structure (`fe_space` *constructs* the space; `fe_assemble`/`weak_form_term`/`eliminate_*` fold over an already-constructed space — distinct vocabulary fronts). The D2-side bullet is what gets fixed (by the D2 repairer), not D4.
  - **Decision**: repaired (no D4 content change — D4's framing stands; recorded as an integrator-ordering note).
  - **Action**: No edit to D4's CYCLE.md content — D4's framing is authoritative. Confirmed D4's count arithmetic is correct: Edit 1 computes `27 main + 4 FE-assembly + 1 FE-space = 32` (firm 31→32); the critic independently counted 31 firm dep-map rows pre-c064, and `fe_space` is +1. The FE-assembly sub-spine count stays **4**, the FE-space sub-spine is **1**, grand total **32** — consistent with D2's grand total (32). See integrator-note below.

- **Finding (skill-uptake-survey, warning)**: telemetry-only.
  - **Decision**: not-needed. No skill applies (Edit 2 is an `index.md` subsection insert, not a `SUMMARY.md` edit; no count-owner-specific skill exists). Non-blocking telemetry surface; no fix.

- **Finding (Issue #3, info)**: D4's firm-contingency self-flag (if D2 lands `fe_space` at a maturity other than firm, the 32/1 counts must drop) resolves clean — D2 lands `fe_space` **firm** (clean-gate PROMOTE), so the contingency does not fire and the 32 grand total holds.
  - **Decision**: not-needed (informational, resolved).

### Unrepairable findings

None. All flagged findings are either repaired (the ctor-range slip) or resolve on D4's authoritative framing with no content change required (the cohort-placement reconciliation is an integrator-ordering note, not a D4 defect).

## Suggested resolution

`overall_status: ready`. Integrator notes:

1. **Ordering constraint (load-bearing).** Apply D4's Edit 2 (which CREATES the new "Firm (FE-space sub-spine — 1; opened cycle-064)" subsection in `book/src/L1/index.md`) **before** D2's cohort-bullet edit, so D2's `fe_space` member bullet can anchor into D4's FE-space sub-spine subsection. Do NOT also apply D2's `fe_space` bullet under the FE-assembly subsection (would create a duplicate/conflicting member bullet). The FE-assembly sub-spine header stays **4** (NOT 5 — D2's "grows 4→5" framing must not land in the FE-assembly subsection header). D2's bullet content is otherwise sound; relocate it into D4's FE-space sub-spine subsection (or use D4's subsection prose in its place). The D2 repairer is fixing the D2 side; this note records the cross-report dependency for the integrator.
2. **Count arithmetic confirmed:** L1 firm 31→32 (`27 main + 4 FE-assembly + 1 FE-space`); grand total 32 is consistent across D2 and D4. Edit 1's header refresh is correct.
3. Both ctor-range citations now read `:66-74` (canonical, matching D1/D2).
