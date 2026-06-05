---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T01:10:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T01:40:00Z
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

# META: verification of "polynomial_recurrence_step slice deletion (graded-stack P2, batch-31 tranche-2, Wave 2 / D2)"

## Critique

### Checks run

**citation-validity — pass (one informational note).** The absorb-no-op evidence (§1) was sample-checked on disk: every cited line in `concepts/negative-result-slice.md` resolves and supports its claim — `:46` (4-site catalog: Chebyshev-4th, Chebyshev-1st, GMRES-Givens, eigentracking out-of-scope branch), `:61` (five-axis difference table named as the cross-family evidence), `:66` (four-of-five-axes within-Chebyshev partial-positive + `ChebyshevSmootherBase<ScalarGenerator>` refactor), `:62`/`:66`/`:75-84` (dual falsification surfaces; the page mandates `### Falsification criterion` and names the slice as the canonical worked example at `:86`). The absorb-verified-no-op verdict is well-supported: every load-bearing catalog datum is present in the firm page. One note: the report repeatedly cites the substitute firm home as "`book/src/L4/chebyshev.md` §Semantics `innerStep`" (R1, R2, R3, R5, and supporting-evidence "`:134` … `innerStep` confirmed present"). The token `innerStep` does **not** appear as a literal identifier anywhere in `book/src/L4/chebyshev.md` — the §Semantics inner k-recurrence fold (`chebyshev.md:172-185`) is an anonymous `iterate_while_pure` step closure, not a named `innerStep` binding, so an `--anchor 'innerStep'` probe would not resolve. This is **not** charged against the report because `§Semantics innerStep` is an established project-wide labeling convention already used identically in ≥6 firm chapters (`L2/krylov-step.md:7,79,85,140`, `L2/chebyshev-iteration.md:30,266`, `L2/index.md:133`, `L3/apply_linop.md:188`, `L3/krylov-step.md:198`, `L3-L2/krylov-step-body-identity.md:127`); the report introduces no new drift and the §Semantics section + its inner k-recurrence fold genuinely exist. The supporting-evidence phrasing "`innerStep` confirmed present" is mildly overstated (the *section* is present; `innerStep` is a convention-label denoting the inner fold, not a literal token), but it resolves to a real firm home consistent with the corpus.

**surface-or-evidence — pass.** This is a `Redundancy` observation / reachability-GC audit, not a refinement of an operator/theme surface. The repoints (R1–R5) re-anchor evidence pointers off a to-be-deleted duplicate onto the firm absorbing home; no new algebraic/rotation claim is asserted. No record is named in a signature here, so the record-definition sub-check does not apply. The absorb-evidence framing is exactly the allowed "verify-the-absorb" shape.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is claimed; this is a deletion/repoint sweep. The check no-ops as it does for stub/roadmap_goal/audit-shaped reports.

**variant-axis-coverage — pass (not applicable).** No operator with orthogonal variant axes is introduced; the report is a corpus-hygiene deletion. Inapplicable to this report kind.

**cross-reference-integrity — warning.** I independently grepped the corpus for every surviving inbound reference. The **live markdown-link** set (the `[...](...polynomial_recurrence_step.md)` form that hard-fails `linkcheck2` on deletion) is exactly four — `SUMMARY.md:296` (R7), `spec/index.md:19` (R8), `negative-result-slice.md:46` (R5), `negative-result-slice.md:66` (R5) — and **all four are covered**; the report's R5 co-landing-blocker catch (outside the planner's enumerated 4-site list) is correct and load-bearing. The `L4/krylov-step.md:126` and `L4/index.md:28` hits link only to `../L2/krylov-step.md` and mention the slice filename in prose, correctly classified no-edit. **However**, the report's §(2) sweep ("Full corpus-wide inbound-reference sweep … classifies every inbound edge") is **incomplete**: it missed `book/src/L3/krylov-step.md:200`, a plain-text slice-anchor `book/src/spec/slices/polynomial_recurrence_step.md:119-160` (parallel to the R1/R2/R3 anchors at `L2/krylov-step.md:7,142` and `L2/index.md:135`, which the report DID catch and repoint). Because it is a plain-text path, not a markdown link, it will **not** trigger a `linkcheck2` hard-fail, so R6 deletion does not break the build — but it leaves a **stale dangling text pointer to a non-existent file** in a firm L3 chapter (a citation-integrity defect), and it **falsifies the report's "every inbound edge" completeness claim**. The prompt's explicit instruction was to confirm R1–R5 cover every surviving markdown link AND slice-anchor; the markdown-link set is fully covered, the slice-anchor set is not (3 of 4 anchors repointed; `L3/krylov-step.md:200` omitted). Warning, not fail: build-safe, but a real missed site and a false sweep-completeness claim.

**edge-label-fidelity — pass.** The load-bearing R1 surgical clause-drop at `L2/krylov-step.md:7` was verified byte-exactly against current disk: the `old` block matches line 7 verbatim; the `new` removes ONLY the `the three polynomial-recurrence sites cataloged at \`polynomial_recurrence_step.md:119-160\`` clause and re-anchors it, while the CG, GMRES (`gmres.md:459-471`), Chebyshev (`§Semantics innerStep`), and Arnoldi (`arnoldi_step.md:99-105, :285-298`) clauses are preserved character-for-character — no trio/chebyshev anchor is collaterally dropped, leaving the c099 krylov-trio sub-campaign material intact. R2 (`:142`), R3 (`L2/index.md:135`) are confirmed polynomial-only lines; their sibling cg/gmres/chebyshev/arnoldi lines (`:138-141`, `:131-134`) are untouched. R4's `old` matches `dependency-map.md:169-172` exactly and removes only the three underscore `polynomial_recurrence_step` slice-node edges, preserving the distinct hyphenated `polynomial-recurrence-step:::planned` planned-node at `:77-79,:98`. All edge-scoping claims hold.

**plan-kind-consistency — pass.** Declared an `observation` (Redundancy) with a mechanical reachability-GC disposition; content shape matches — a verified-absorb no-op plus surgical repoints/delink/deletion/row-removal, with explicit deferral of the krylov-trio to c099. No firm-operator content masquerading as rough-in or vice versa.

**plan / row-anchor verification (R7/R8) — confirmed against current disk.** `SUMMARY.md:295` orthog / `:296` polynomial (trio `:292` arnoldi, `:293` cg, `:294` gmres PRESERVED); `spec/index.md:17` orthog / `:19` polynomial (trio `:15` cg, `:16` gmres, `:18` arnoldi PRESERVED). Both R7 and R8 `old` blocks match the on-disk lines byte-exactly; the c097 line-shift re-verification claim holds. `orthog.md` is still present on disk (D1 not yet applied) — consistent with the report's serialization caveat #3; the integrator must sequence D1's orthog-file deletion before R7/R8's orthog-row removal as the report flags. Removing the orthog rows here is correct given D1 owns the orthog file this same cycle.

**skill-uptake-survey — pass.** The report's shape (slice reduction/deletion) implies the `phase-1-slice-reduction-audit` skill; OQ #5 explicitly applies its canonical-instance carve-out (concept-page-grep: the slice is named by one page, but its L0 navigation is fully absorbed, so "unique L0 navigation not covered elsewhere" FAILS and the carve-out does not retain it). Skill uptake is surfaced.

### Issues found

1. **`L3/krylov-step.md:200` — missed inbound slice-anchor; stale dangling text pointer post-deletion + falsified sweep-completeness claim** (severity: warning; `cross-reference-integrity`). CYCLE.md §(2) "Full corpus-wide inbound-reference sweep" omits `book/src/L3/krylov-step.md:200`, which carries the plain-text anchor `book/src/spec/slices/polynomial_recurrence_step.md:119-160` — the exact sibling of the R1/R2/R3 anchors that WERE repointed (`L2/krylov-step.md:7,142`, `L2/index.md:135`). After R6 deletes the slice, this line is a stale text pointer to a non-existent file inside a firm L3 chapter. It is NOT a `linkcheck2` hard-fail (plain text, not a markdown link), so the build survives — but it is a genuine citation-integrity defect and it makes the report's "classifies every inbound edge" / "every load-bearing catalog datum … no unique datum missing" completeness framing false for the anchor set. Repair candidate: add an R9 repoint of `L3/krylov-step.md:200` parallel to R2/R3 (re-anchor the catalog claim to `concepts/negative-result-slice.md` §Partial-positive + the `L4/chebyshev.md` §Semantics Chebyshev-pair home), and correct the §(2) sweep table to include the row.

2. **"`innerStep` confirmed present" is mildly overstated** (severity: informational; `citation-validity`). Supporting-evidence bullet "`book/src/L4/chebyshev.md:134` (§Semantics; `innerStep` confirmed present)" — the §Semantics section is present, but `innerStep` is not a literal identifier in the file (the inner k-recurrence fold at `chebyshev.md:172-185` is an anonymous `iterate_while_pure` closure). `§Semantics innerStep` is an established corpus-wide convention-label (≥6 firm chapters use it identically), so this introduces no new drift and resolves to a real firm home; flagged only so a downstream reader does not expect a literal `innerStep` anchor. No repair required.

---

## Repair

### Fixes attempted

- **Finding**: `L3/krylov-step.md:200` — missed inbound slice-anchor; stale dangling text pointer post-deletion + falsified §(2) sweep-completeness claim (critic warning, `cross-reference-integrity`).
  - **Decision**: repaired.
  - **Action**: Added proposed-change **R9** to D2's CYCLE.md (`reports/2026-06-05T002531Z-same-layer-cross-cutter-polynomial-slice-delete/CYCLE.md` §Proposed changes) re-anchoring the plain-text `book/src/spec/slices/polynomial_recurrence_step.md:119-160` pointer at `book/src/L3/krylov-step.md:200` onto the firm home — parallel to R2/R3. The catalog claim moves to `book/src/concepts/negative-result-slice.md` §Partial-positive sub-pattern + §Falsification criterion; the Chebyshev-pair firm home stays `book/src/L4/chebyshev.md` §Semantics `innerStep`. Target selection verified by reading `L3/krylov-step.md:194-200` in context: line 200 is the polynomial entry of the L3 "Five Phase-1 slice instances" list whose immediate sibling (`:198`, the Chebyshev entry) is already anchored to `L4/chebyshev.md` §Semantics `innerStep`, so the R2/R3 firm-home pair is the contextually-correct repoint. The R9 `edit` `old` block was verified byte-exactly against current disk (line 200 matches verbatim). Also corrected CYCLE.md §(2) "Full corpus-wide inbound-reference sweep" table to add the `L3/krylov-step.md:200` row (classified `reference` / plain-text / no-linkcheck-hard-fail / repoint R9), updated the §(2) detritus-confirmation co-landing list to `R1–R5, R7, R8, R9`, and updated the Summary / Recommendation / Supporting-evidence counts (4→4+R9 repoint sites; 8→9 proposed-changes).
  - **Scope note**: Surgical and mechanical — a parallel re-anchor of an evidence pointer already established by the verified-clean R2/R3, with no new algebraic/rotation claim authored. R1's krylov-trio cg/gmres/arnoldi clauses, R1–R8, and the `L2/krylov-step.md:7` surgical clause-drop were left untouched.

- **Finding**: "`innerStep` confirmed present" mildly overstated (critic informational, `citation-validity`).
  - **Decision**: not-needed (critic flagged informational only, "No repair required" — resolves to a real firm home via an established ≥6-chapter convention-label; no drift introduced).

### Unrepairable findings

None. The single warning was a missed-site / surgical-repoint defect squarely inside repair authority (forgotten anchor whose firm target is the same one R2/R3 already used, with the source range and contextually-correct home trivially supported).

## Suggested resolution

`ready`. Notes for the integrator: R9 must land in the same cycle (c098) as R6 (slice deletion) alongside R1–R5 and R7–R8 — it is build-safe to omit (plain text, not a `linkcheck2` hard-fail) but omitting it leaves a stale dangling text pointer in a firm L3 chapter, which is exactly the citation-integrity defect this repair closes. R9 touches a fourth file (`book/src/L3/krylov-step.md`) not in the original CYCLE.md edit set; the on-disk `old` block was re-verified verbatim at repair time. The D1-serialization caveat (#3) for R7/R8's orthog-row half is unchanged and still applies.
