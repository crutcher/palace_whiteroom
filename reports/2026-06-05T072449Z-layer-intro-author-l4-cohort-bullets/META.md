---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T073034Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: warning
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T073500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L4 §Vocabulary-cohort missing firm bullets (eliminate_bc + preconditioning-framework)

## Critique

### Checks run

**citation-validity — pass.** The report makes few first-order claims; the load-bearing ones are (i) both target chapters are `firm` on disk, (ii) the new-bullet links resolve, (iii) the `ksp.cpp:276-293` source range backs the `setOperators` framing in the preconditioning-framework bullet. (i) confirmed: `eliminate_bc.md:4` carries `firmness: firm` (and a positive `## Status` at :332 with the firm-on-positive-structure escape), `preconditioning-framework.md:4-5` carries `firmness: firm` / `rank: firm`. (iii) confirmed: `reference/palace/palace/linalg/ksp.cpp:276-293` opens on `BaseKspSolver<OperType>::SetOperators(const OperType &op, const OperType &pc_op)` — the `(op, pc_op)` bind the bullet describes. The two `edit:` blocks themselves are content insertions, not citations, so the citation surface is thin and accurate.

**surface-or-evidence — pass.** This is a layer-intro-author Part-overview prose addition, not a refinement-shaped operator/theme change, so the surface-or-evidence rotation_claim machinery is largely n/a; what matters is whether the two one-line roles faithfully report the chapters they link. They do. `eliminate_bc` = "post-assembly boundary-condition application surface … separable post-composition verb-pair `(eliminate_essential_bc, eliminate_rhs)` … composes AFTER `fe_assemble` … consumes the `DofSet[N]` from `essential_dofs`" — matches `eliminate_bc.md` §Status (:334-349: the post-assembly BC-application verb-pair, the assemble-half-completing companion of `fe_assemble`, the `reference` (not blocking) edge to `fe_assemble`, the `linear_combination` RHS-side fold). `preconditioning-framework` = "composition-and-binding framework one shell outside the `ksp_solve` cap … `buildKspSolver` constructor … `setOperators` bind holding the capability-typed `(op, pc_op)` binding … the three rotations (build/run stratification, capability-typing, `finestLevelUnwrap` derived-view hoist)" — matches `preconditioning-framework.md` §Status (:326-337: the firm-on-positive-structure escape over the positive `BaseKspSolver` source + the firm `ksp_solve` cap; the capability-typing / derived-view-hoist refinements). Both role descriptions are accurate to the chapters and to the firmness on disk. Record-definition sub-check: the bullets name record-ish types (`DofSet[N]`, `DiagPolicy`, `LinearOperator[N,N]`, `(op, pc_op)`/`pcBoundOp`) but only in a Part-overview index bullet that *references* chapters where these are defined (e.g. `eliminate_bc.md` consumes `state-stratification` for `DofSet[N]`/`DiagPolicy`); the index is not the definition home and is not obligated to define them — no missing-home gap.

**rotation-quality — pass (not applicable to this report-kind).** No algebraic/structural rotation is asserted by this dispatch — it adds two prose bullets to an existing Part-overview cohort list. The underlying chapters carry the rotation claims; this report only narrates their roles.

**variant-axis-coverage — pass.** No orthogonal variant axes are introduced by adding two cohort bullets. The variant axes of the underlying operators (e.g. eliminate_bc's `DiagPolicy`, preconditioning-framework's brand role-distinction) live in their own chapters and are summarized, not re-derived, here.

**cross-reference-integrity — pass.** All 13 distinct links across the two new bullets were resolved against disk and every one exists: eliminate_bc bullet → `./eliminate_bc.md`, `./fe_assemble.md`, `../L1/essential_dofs.md`, `./ksp_solve.md`, `./eigsolve.md`, `./linear_combination.md`, `../L4-L3/bc-elimination-post-composition-dissolution.md` (the OQ-flagged "assumed firm/existing" theme — confirmed present on disk, so the defang-fallback caveat in §Open-questions is moot); preconditioning-framework bullet → `./preconditioning-framework.md`, `./ksp_solve.md`, `./krylov-step.md`, `../concepts/state-stratification.md`, `../concepts/capability-typing.md`, `../concepts/derived-view-hoisting.md`. All are firm/existing on-disk targets already linked elsewhere in the same index, so the build-safety (linkcheck2) claim holds. The two `[old]` anchor strings (the `fe_assemble` and `solve_family` bullet openings) match the on-disk text exactly and uniquely, so both insertions apply cleanly with the anchor preserved as the trailing `[new]` line.

**edge-label-fidelity — warning.** Not an L_{n+1}→L_n edge-label question (no lowering edge is authored here), but the report's *placement-justification prose* asserts an alpha-neighbor framing that does not match the on-disk cohort order, and that mismatch is the closest analog to an edge-label/prose-fidelity discrepancy. The report states `eliminate_bc` lands "between `eigenfreq_qfactor_reduce` and `fe_assemble`" and `preconditioning-framework` "between `nrm2` and `solve_family`". On disk the firm cohort is NOT alpha-sorted (it is the documented transitional mixed alpha/chronological state): `eigenfreq_qfactor_reduce` (line 49) actually sits AFTER `fe_assemble` (line 48), not before it; and between `nrm2` (line 43) and `solve_family` (line 47) sit `eigsolve`/`fold_solve`/`frequency_sweep`. So the literal "between X and Y" narration does not describe the realized neighbors. This is cosmetic, not structurally wrong: the actual insertion is anchor-defined ("immediately before the on-disk `fe_assemble` bullet" / "before the on-disk `solve_family` bullet"), which is unambiguous and applies cleanly, and the report explicitly acknowledges the list is "NOT yet fully alpha-sorted (transitional)" with insertions placed "alpha-LOCALLY against their named on-disk neighbors". The two alpha relations the prompt asked to confirm (`eliminate_bc < fe_assemble`; `nrm2 < preconditioning-framework < solve_family`) ARE alphabetically true and the chosen anchors honor them locally. The warning is only that the "between A and B" gloss names a non-adjacent member (`eigenfreq_qfactor_reduce`) as the upper neighbor when the realized predecessor of the insertion is `frequency_sweep`/`solve_family` etc. — a reader following the prose to audit placement would find the named left-neighbor in the wrong position.

**plan-kind-consistency — pass.** Declared shape is a layer-intro-author Part-overview prose addition (two cohort bullets), and the content is exactly that — chapter link + one-line role + standard cross-references, matching the existing bullet style (the inserted bullets carry the same `[`slug`](./slug.md) — **bold role**: prose … Status `firm` (…). Harvested + firmed cycle-NNN` shape as their neighbors). No rough-in placeholders, no mis-classified firm/stub content. The same-file partition with D5 is respected: both edits anchor on mid-file §Vocabulary-cohort prose bullets (lines 47-48 region), disjoint from the frontmatter `edges:` block (D5) and the firm-count header at line 32. The header already reads "Firm at L4 (21 + 4 outer-driver)" and its prose already narrates both eliminate_bc (c101) and preconditioning-framework (c096) as landed firm, so the count is consistent with these two as firm members and needs no mutation — the bullets bring the enumerated list into line with the already-correct count.

**skill-uptake-survey — pass.** The report cites the c057-meta guard ("read the file, not the index cell") and confirms firmness from on-disk `## Status` / frontmatter for both chapters, which is the relevant procedural discipline for this dispatch. No dedicated skill is strongly implied for "add a cohort bullet in alpha-local position"; the directive-3 insertion rule is followed and named. Telemetry only — non-blocking.

### Issues found

1. **Placement-justification prose names a non-adjacent left-neighbor (`book/src/L4/index.md` §Vocabulary-cohort, via CYCLE.md "Proposed changes" line 31 + §Supporting-evidence line 73) — severity: low (cosmetic).** The report says `eliminate_bc` lands "between `eigenfreq_qfactor_reduce` and `fe_assemble`", but on disk `eigenfreq_qfactor_reduce` (line 49) follows `fe_assemble` (line 48), so the realized predecessor of the insertion is `frequency_sweep`/`solve_family`, not `eigenfreq_qfactor_reduce`. The full-alpha order listed in §Supporting-evidence (lines 71-74) is a *hypothetical* fully-sorted sequence, not the on-disk order; the report does flag the list as "transitional mixed alpha/chronological" (§Open-questions), so the discrepancy is disclosed, but the "between A and B" gloss is misleading on its own. Does not affect the applied edit (anchor-based insertion is unambiguous and correct).

2. **Same observation for `preconditioning-framework` (CYCLE.md "Proposed changes" line 41) — severity: low (cosmetic).** "Between `nrm2` and `solve_family`" is alphabetically true but the realized predecessor on disk is `frequency_sweep` (line 46), with `eigsolve`/`fold_solve`/`frequency_sweep` intervening between `nrm2` (line 43) and the `solve_family` anchor (line 47). The anchor-based insertion is correct; only the neighbor-naming prose overstates adjacency.

No structural, link, firmness, partition, or build-safety defects found. Both target chapters are firm on disk, all links resolve, the anchors match uniquely, the partition with D5 is clean, and the firm-count header is already consistent with both members.

## Repair

### Fixes attempted

- **Finding**: edge-label-fidelity WARNING (low/cosmetic) — the placement-justification PROSE names a non-adjacent left-neighbor. CYCLE.md asserts `eliminate_bc` lands "between `eigenfreq_qfactor_reduce` and `fe_assemble`" and `preconditioning-framework` "between `nrm2` and `solve_family`", but the on-disk §Vocabulary-cohort list is in the documented transitional mixed alpha/chronological order, so the realized on-disk predecessors are `solve_family` (line 47, before `fe_assemble`) and `frequency_sweep` (line 46, before `solve_family`) — NOT the full-alpha left-neighbors named in the gloss.
  - **Decision**: repaired
  - **Action**: rewrote the three "between A and B" prose glosses in CYCLE.md to anchor-based, list-order-agnostic phrasing:
    - "Proposed changes" `eliminate_bc` placement justification (was line 31-33): now "inserted immediately before the existing `fe_assemble` bullet (line 48), preserving the alpha relation `eliminate_bc` < `fe_assemble`", with a parenthetical noting the on-disk predecessor is the `solve_family` bullet (line 47) under the transitional order.
    - "Proposed changes" `preconditioning-framework` placement justification (was line 41-43): now "inserted immediately before the existing `solve_family` bullet (line 47), preserving the alpha relation `nrm2` < `preconditioning-framework` < `solve_family`", with a parenthetical noting the on-disk predecessor is the `frequency_sweep` bullet (line 46).
    - §Supporting-evidence alpha-placement bullet (was line 69-78): re-labeled the listed full-alpha sequence as HYPOTHETICAL (not the on-disk order), kept the two honored local alpha relations explicit, and corrected the realized on-disk predecessors to `solve_family` / `frequency_sweep`.
  - **Rationale**: The actual artifact edit (the two `edit:book/src/L4/index.md` blocks) is anchor-defined and correct — the `[old]` anchors match the on-disk `fe_assemble` / `solve_family` bullet openings uniquely, and the alpha relations honored are alphabetically true. The defect was purely in the justification prose's neighbor-naming gloss. Mechanical prose correction within repair authority (edge-label/prose-fidelity fix where the prose names a non-adjacent neighbor); the proposed-changes `edit:` blocks were preserved UNCHANGED.

### Unrepairable findings

None.

## Suggested resolution

`overall_status: ready`. The single non-pass finding (edge-label-fidelity warning, low/cosmetic) is repaired in-report; the applied artifact edit was already correct and is untouched. Notes for the integrator/meta-phase:

- The two `edit:book/src/L4/index.md` proposed-changes blocks are sound and apply cleanly on their unique anchors; integrate as-is.
- Out-of-scope-here observation for the meta-phase: the L4 §Vocabulary-cohort list is in the documented transitional mixed alpha/chronological order (not yet fully alpha-sorted). The directive-3 one-time alpha reorg of the L4 firm cohort (meta-phase-owned) would resolve this pre-existing condition and make future "alpha-slot" placement glosses match the realized neighbors. This repair did NOT reorder the list (out of repair scope).
