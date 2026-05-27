# Cycle-005 integrator staging log

Per-cycle staging log for the split integrator (per-report + finalize) introduced cycle-004→005. Each `integrator-per-report` dispatch appends one row (append-only; newest LAST). `integrator-finalize` reads this log at cycle-end to drive the book rebuild, commit, and cycle-end housekeeping.

Format: one section per applied report, ordered by dispatch order (append-only). Each row records files touched, gate-hit counts, open-questions promoted, and a `Build-relevant` flag (`yes` if `book/src/*.md` was touched; consumed by integrator-finalize to decide whether to rebuild).

---

## 2026-05-27T025354Z-harvester-krylov-step-L2
applied_at: 2026-05-27T03:42:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/krylov-step.md (created)
- book/src/L2/index.md (replaced — dep-map row promoted rough-in→firm; Working Notes refreshed)
- book/src/SUMMARY.md (surgical insert — added `- [krylov-step](./L2/krylov-step.md)` under L2 Part)
- scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md (created — speculative-L1-promotion decision artifact)
- scaffolding/open-questions.md (append-only; 7 OQs promoted)

Gate hits:
- retroactive-budget-per-slice: 0
- retroactive-budget-global: 0 (this report only)
- concept_writes-on-existing-slug: 0
- forward-edge-claim-without-surface: 0
- edge-label-prose-mismatch: 0 (no edge-label; intra-L2 firm-up)
- H1-reuses-page-heading: 0
- append-on-missing-slug: 0
- variant-axis-missing-on-multi-variant-operator: 0 (6 axes explicit, all absorbed)
- bookkeeping-incomplete: 0
- SUMMARY-chapter-registration-auto-fix: not-triggered (report proposed the SUMMARY edit explicitly)

Open questions promoted:
- krylov-step-speculative-l1-promotion-decision (status: answered, answered_in: scaffolding/decisions/2026-05-27-krylov-step-speculative-l1-promotion.md)
- orthogonalize-as-future-L2-firstclass-entry
- incremental-least-squares-as-future-L2-firstclass-entry
- L2-layer-intro-refresh-for-named-compositions
- L2-named-compositions-have-no-single-L0-citation
- krylov-step-naming-stretches-to-chebyshev
- gmres-givens-stream-as-step-kernel-borderline

Build-relevant: yes

Notes: First per-report integrator dispatch of cycle-005 and first cycle running the split integrator (per-report + finalize). Created the cycle-005 staging dir and this STAGING.md file. The SUMMARY edit was applied as a surgical 4-line insert rather than a full-file replacement to preserve append-points for subsequent in-cycle integrators (the L0-bootstrap-1 report will also add SUMMARY rows). All 4 proposed-changes blocks applied cleanly; no gate hits; no deferrals.

---

## 2026-05-27T025354Z-abstractor-apply-linop-mutation-rotation
applied_at: 2026-05-27T04:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/apply-linop-mutation-rotation.md (created)
- book/src/SUMMARY.md (surgical insert — added `- [apply-linop-mutation-rotation](./L1-L0/apply-linop-mutation-rotation.md)` between axpby-mutation-rotation and bicgstab-iteration under L1>L0 Part)
- scaffolding/open-questions.md (append-only; 5 OQs promoted)

Gate hits:
- retroactive-budget-per-slice: 0
- retroactive-budget-global: 0 (this report only)
- concept_writes-on-existing-slug: 0
- forward-edge-claim-without-surface: 0
- edge-label-prose-mismatch: 0 (L1>L0 throughout; file lives in L1-L0/)
- H1-reuses-page-heading: 0 (H1 matches sister-theme axpby-mutation-rotation convention)
- append-on-missing-slug: 0
- variant-axis-missing-on-multi-variant-operator: 0 (transpose-mode × accumulate-mode rectangular axes explicit; element-type handled per-sub-pattern)
- bookkeeping-incomplete: 0
- SUMMARY-chapter-registration-auto-fix: not-triggered (report proposed the SUMMARY edit explicitly)

Open questions promoted:
- apply-linop-workspace-tensor-reading-at-L0
- apply-linop-sum-operator-mult-via-addmult-reuse
- apply-linop-preconditioner-application-coverage
- apply-linop-complex-wrapper-operator-lifting
- apply-linop-complex-operator-default-impls-of-hermitian-transpose

Build-relevant: yes

Notes: Three proposed-changes blocks in the report. Block 1 (create L1-L0/apply-linop-mutation-rotation.md) applied as Write — file did not previously exist. Block 2 (L1/index.md) is an explicit no-op stanza by the abstractor (no speculative L1 operators emitted, so no L1 dep-map edit); no action taken, matches the abstractor's deliberate documentation. Block 3 (SUMMARY.md) applied as surgical insert between axpby-mutation-rotation and bicgstab-iteration to preserve append-points for the 4 remaining in-cycle integrators. Five forward-looking caveats (workspace tensor reading, Mult-via-AddMult reuse, preconditioner coverage, ComplexWrapperOperator lifting, hermitian-transpose default impls) promoted to open-questions.md; caveat #5 (no speculative L1 operators emitted) is a meta-summary not a tracking item, not promoted. No gate hits; no deferrals; all per-report safety-net checks clean.

---

## 2026-05-27T025354Z-abstractor-axpbypcz-mutation-rotation
applied_at: 2026-05-27T04:28:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/axpbypcz-mutation-rotation.md (created)
- book/src/SUMMARY.md (surgical insert — added `- [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)` between axpby-mutation-rotation and apply-linop-mutation-rotation under L1>L0 Part)
- scaffolding/open-questions.md (append-only; 6 OQs promoted)

Gate hits:
- retroactive-budget-per-slice: 0
- retroactive-budget-global: 0 (this report only — aggregate across cycle staging deferred to integrator-finalize)
- concept_writes-on-existing-slug: 0
- forward-edge-claim-without-surface: 0 (uses firm L1 vocabulary `axpbypcz`, `axpby`, `axpy` exclusively; no speculative operators emitted)
- edge-label-prose-mismatch: 0 (L1>L0 throughout; file lives in L1-L0/)
- H1-reuses-page-heading: 0 (H1 `axpbypcz-mutation-rotation` matches the file slug and the sister-theme `axpby-mutation-rotation` convention)
- append-on-missing-slug: 0
- variant-axis-missing-on-multi-variant-operator: 0 (4 sub-patterns A/B/C/D explicit covering scalar-element-type × free-vs-member axes; γ==0 algebraic sub-rule scoped to sub-patterns A and C; α==0/β==0 explicitly scoped out as L1-level recognition-only per Applicability condition #5)
- bookkeeping-incomplete: 0 (repairer added `skill_uptake:` block to CYCLE.md frontmatter)
- SUMMARY-chapter-registration-auto-fix: not-triggered (report proposed the SUMMARY edit explicitly)

Open questions promoted:
- mfem-add-alias-safety
- mixed-justification-sub-rule-methodology
- axpbypcz-gamma-asymmetric-branching-rationale
- axpbypcz-sub-pattern-B-defined-not-used-corpus-audit
- scalar-promotion-mutation-rotation-cross-family-theme
- axpbypcz-gamma-recognition-is-syntactic-not-semantic

Build-relevant: yes

Notes: Three proposed-changes blocks in the report. Block 1 (create L1-L0/axpbypcz-mutation-rotation.md) applied as Write — file did not previously exist. Block 2 (L1/index.md) is an explicit no-op stanza by the abstractor (axpbypcz, axpby, axpy are all firm L1 operators — no dep-map row to add); the abstractor flagged an optional "forward link from axpbypcz row's status cell to the new theme file" as integrator's discretion — not applied this dispatch to keep the per-report scope minimal (can be added by a later refresh report if helpful). Block 3 (SUMMARY.md) applied as surgical insert between `axpby-mutation-rotation` and `apply-linop-mutation-rotation` under L1>L0 Part, following the abstractor's literal placement ("after the axpby-mutation-rotation line") — preserves append-points for the 3 remaining in-cycle integrators. **Methodology-novelty advisory survives apply**: critic finding #3 (non-blocking) flagged this as the project's **first mixed-justification sub-rule** (γ==0 sub-rule labelled both `algebraic` and `structural`); the open-question `mixed-justification-sub-rule-methodology` was promoted to make this visible to a future `cross-layer-cross-cutter` review. Scope-confidence on sub-pattern B (critic finding #4) is empirically confirmed defined-not-used by `grep -rn AXPBYPCZ` audit — corresponding OQ `axpbypcz-sub-pattern-B-defined-not-used-corpus-audit` promoted for full-tree exhaustive audit. No gate hits; no deferrals; all per-report safety-net checks clean. Repairer's `not-needed` resolution of the citation-validity warning (citation ranges already include the `template <>` markers per critic's mistaken off-by-one claim) accepted as-is — the source ranges in the L1>L0 file match the report's verified ranges.

---

## 2026-05-27T025354Z-layer-intro-author-L0-reference-bootstrap-1
applied_at: 2026-05-27T04:52:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L0/output-arg-vs-receiver.md (created)
- book/src/L0/mfem-vector-types.md (created)
- book/src/L0/linalg-free-functions.md (created)
- book/src/L0/transparent-vs-load-bearing-tricks.md (created)
- book/src/L0/linalg-vector-file.md (created)
- book/src/L0/ksp-factory-file.md (created)
- book/src/L0/index.md (replaced — re-framed L0 as citations + reference-note overlay; added Reference-note cohort split into Conventions / File overviews; preserved Citation format rule + Working Notes; updated heading to include "+ reference notes")
- book/src/SUMMARY.md (surgical insert — replaced `# L0 — Cited Palace Source` heading with `# L0 — Cited Palace Source + Reference Notes` and added 6 chapter rows under the L0 Part)
- book/src/L1-L0/bicgstab-iteration.md (cross-reference fix — reconciled `ksp.cpp:53-56` → `:53-57` at 2 locations: prose at line 39 and verified_against citation block at line 68; matches sibling minres-iteration.md and the new ksp-factory-file.md chapter; per resume-notes mention and META.md repair section unrepairable-finding #1)

Gate hits:
- retroactive-budget-per-slice: 0
- retroactive-budget-global: 0 (this report only)
- concept_writes-on-existing-slug: 0 (6 new L0 slugs created; L0/index.md full replacement is the L0-overview page, not a concept page)
- forward-edge-claim-without-surface: 0 (all referenced L1 slugs exist — axpy / axpby / axpbypcz / scal / dot / nrm2 / apply_linop; L1-L0/minres-iteration and L1-L0/bicgstab-iteration exist; spec/slices/cg and spec/slices/gmres exist; backlinks marked aspirational with explicit "Forward-declared" disclaimer in the 4 conventions chapters)
- edge-label-prose-mismatch: 0 (no L_{n+1}→L_n edge labels in L0 reference notes; chapters are L0-only with backward-pointing "Referenced from" annotations)
- H1-reuses-page-heading: 0 (each H1 is distinct from the SUMMARY-row link text; chapter slug ≠ H1)
- append-on-missing-slug: 0
- variant-axis-missing-on-multi-variant-operator: 0 (mfem-vector-types explicitly enumerates element-type axis × Par* axis as orthogonal; transparent-vs-load-bearing classification explicit)
- bookkeeping-incomplete: 0 (META frontmatter has skill_uptake block per repair)
- SUMMARY-chapter-registration-auto-fix: not-triggered (report proposed the SUMMARY edit explicitly for all 6 new chapters)

Open questions promoted:
- (none — report explicitly states "No new entries in `scaffolding/open-questions.md` are proposed"; the 5 caveats are forward-notes / scope-limitations / dependency advisories, not new tracking items)

Build-relevant: yes

Notes: Largest report this cycle — 8 proposed-changes blocks (6 new L0 chapters + L0/index.md replacement + SUMMARY.md surgical insert). All 8 applied cleanly. **Cross-reference fix applied as part of this dispatch per integrator dispatch instructions**: `book/src/L1-L0/bicgstab-iteration.md` reconciled from `ksp.cpp:53-56` → `:53-57` at 2 locations (prose at :39 and verified_against citation at :68). Source range verified directly against `reference/palace/palace/linalg/ksp.cpp` — the three-case fall-through is lines 53–55 (case labels), 56 (MFEM_ABORT), 57 (break); the full block is `:53-57`. This fix surfaced from this report's META.md "Unrepairable findings #1" and the cycle-005-resume-notes.md note ("L0 bundle repair surfaced one cross-reference issue to fix"). Resume notes had originally flagged this for integrator-finalize but the dispatch instructions explicitly routed it to this per-report dispatch since it's directly relevant to L0 bootstrap consistency. Sibling page `minres-iteration.md` already uses `:53-57` (verified at lines 47, 131); the bicgstab-iteration page was the outlier; now all three sources (`minres-iteration.md`, `bicgstab-iteration.md`, new `ksp-factory-file.md`) cite the consistent `:53-57` range. SUMMARY.md edit applied as targeted heading-line replacement + 6-row insert; the L0 Part is the last named Part in the layered stack before the Phase 1 slices, so no append-point preservation concern for sibling layers (subsequent dispatches edit other Parts). Five forward-notes caveats from the report (retroactive L1 thinning is separate dispatch; mfem-vector-types scope; transparent-vs-load-bearing depends on CLAUDE.md; linalg-vector-file representative-not-exhaustive; ksp-factory-file stops short of ConfigurePreconditionerSolver) recorded by the report's "Open questions / caveats" section but explicitly NOT promoted to open-questions.md per report's own decision. No gate hits; no deferrals; all per-report safety-net checks clean. Critic findings 1-2 already resolved by repair (skill_uptake block added; `four real LocalDot calls` phrasing replaced with explicit `mfem::Vector::operator*` enumeration); critic findings 3-5 explicitly classified by critic as non-blocking presentational notes (no repair attempted; no follow-up needed); critic finding 6 resolved by repair (Forward-declared disclaimer prepended to all 4 conventions-chapter Referenced-from sections); critic finding 7 (skill-uptake) telemetry only; critic finding 8 (CYCLE.md vs REPORT.md naming) correctly marked not-needed by repairer as stale-info.

---

## 2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement
applied_at: 2026-05-27T05:08:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only; 4 OQs promoted)

Gate hits:
- retroactive-budget-per-slice: 0
- retroactive-budget-global: 0 (this report only; observation-only, no surface diff)
- concept_writes-on-existing-slug: 0 (no artifact writes)
- forward-edge-claim-without-surface: 0 (no proposed-changes; recommendation routes to next-cycle dispatches)
- edge-label-prose-mismatch: 0 (no edges authored; L4>L3>L2 lowering is recommended-only, not authored)
- H1-reuses-page-heading: 0 (no artifact pages created)
- append-on-missing-slug: 0 (no appends; pure observation report)
- variant-axis-missing-on-multi-variant-operator: 0 (no operator authored; variant absorption noted by reference to L2 rough-in)
- bookkeeping-incomplete: 0 (META frontmatter has skill_uptake block per repair)
- SUMMARY-chapter-registration-auto-fix: not-triggered (no chapters created)

Open questions promoted:
- krylov-step-dual-placement-l2-l4-routing
- krylov-step-naming-reuse-vs-disambiguation
- krylov-step-l3-identity-in-form-audit
- state-stratification-as-l4-concept-or-l4-row

Build-relevant: no

Notes: Observation-only cross-cutter report — no `## Proposed changes` section, no artifact edits. Recommendation is **dual-placement** for `krylov-step` (both L2 and L4 with L4>L3>L2 lowering edge) with three concrete cycle-006 follow-up dispatches named (primary: harvester on `krylov-step @ L4`; secondary: abstractor on L4>L3 lowering theme; tertiary deferrable: layer-intro-author on L4 dep-map). The primary recommendation (L4 dual-placement entry) requires the cycle-005 L2 firm-up to land first (which it did this cycle in dispatch #1 of this staging log: `2026-05-27T025354Z-harvester-krylov-step-L2`), so the routing is sequence-correct: L2 firm landed cycle-005, L4 dual lands cycle-006+. Four OQs promoted: (1) the dual-placement routing itself (load-bearing recommendation, names the three follow-up dispatches for cycle-planner consumption); (2) naming-reuse-vs-disambiguation (whether to use `krylov-step` at both layers or disambiguate); (3) L3 identity-in-form audit (whether the L4→L2 lowering can skip an explicit L3 row, deferred to abstractor); (4) state-stratification L4 concept-or-row coordination (whether the L4 harvester needs to batch state-stratification + iterate_while + solve-monad as L4 dep-map rows alongside the krylov-step entry). Two of the report's five caveats were NOT promoted as OQs by the report itself (caveat #4 promotion-timing is process-routing not tracking, and caveat #5 single-observation-discipline is meta-summary not tracking) — matching the abstractor-apply-linop dispatch's discipline of not promoting meta-summary caveats. Critic findings 1-3 are all severity-low informational (skill-uptake repaired by adding skill_uptake block; caveats #2 and #3 in CYCLE.md are non-blocking and explicitly classified `not-needed` by repairer per role authority). No gate hits; no deferrals; no artifact touched (Build-relevant: no — integrator-finalize can skip the book rebuild on the basis of this row alone, but other in-cycle rows still require rebuild).

---

## 2026-05-27T025354Z-layer-intro-author-scalar-promotion-concept
applied_at: 2026-05-27T05:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/scalar-promotion.md (created)
- book/src/concepts/index.md (anchor-and-insert — added `| [scalar-promotion](./scalar-promotion.md) | methodology |` after `| [scal](./scal.md) | primitive |`)
- book/src/SUMMARY.md (discretionary auto-fix — appended `  - [scalar-promotion](./concepts/scalar-promotion.md)` at end of Concepts section before Design Artifacts; report did NOT propose this edit but existing pattern registers nearly all concept pages in SUMMARY.md)
- scaffolding/open-questions.md (append-only; 2 OQs promoted)

Gate hits:
- retroactive-budget-per-slice: 0 (purely additive concept page; no retroactive L1 edits)
- retroactive-budget-global: 0 (this report only; aggregate across cycle staging deferred to integrator-finalize)
- concept_writes-on-existing-slug: 0 (new slug `scalar-promotion`; verified no pre-existing `book/src/concepts/scalar-promotion.md`)
- forward-edge-claim-without-surface: 0 (all four L1 backlinks resolve — axpy.md / axpby.md / axpbypcz.md / scal.md all exist; `complex-from-real-lift.md` exists; open-question backlink `scalar-promotion-typing-rule` exists in open-questions.md line 53)
- edge-label-prose-mismatch: 0 (concept page, no layer edge)
- H1-reuses-page-heading: 0 (H1 `scalar-promotion` matches sister-concept convention `complex-from-real-lift`, `state-stratification`, `tensor-field-lift` etc. — slug-equals-H1 is the established norm for concepts/ pages)
- append-on-missing-slug: 0
- variant-axis-missing-on-multi-variant-operator: 0 (not an operator entry)
- bookkeeping-incomplete: 0 (META has `skill_uptake:` block; `overall_status: ready`)
- SUMMARY-chapter-registration-auto-fix: applied-discretionarily (gate text targets `book/src/L<n>/<slug>.md` chapters; concepts/ is technically outside the literal gate; however, the existing SUMMARY.md pattern registers nearly all concept pages, so registering preserves book-build consistency — see Notes)

Open questions promoted:
- scalar-promotion-retroactive-l1-thinning
- scalar-promotion-l4-calculus-formalisation

Build-relevant: yes

Notes: Two proposed-changes blocks in the report; both applied cleanly. Block 1 (create `book/src/concepts/scalar-promotion.md`) applied as Write — file did not pre-exist. Block 2 (anchor-and-insert into `book/src/concepts/index.md` after the `| [scal](./scal.md) | primitive |` row) applied as Edit. Anchor was unique. **Taxonomy classification decision**: report deferred `methodology` vs `layer-pattern` to integrator; selected `methodology` per the report's own rationale (the rule transcends a single layer — it's a general principle of the `real ⊑ complex` promotion lattice on scalars, applicable wherever real-scalar overloads are sibling to complex-scalar overloads in any layer's operator surface, not specifically L1). `layer-pattern` was the defensible alternative cited by critic; either is correct; `methodology` chosen to match the report's stated preference. **SUMMARY.md discretionary auto-fix**: report did NOT propose a SUMMARY.md edit (concept pages are a look-aside library per `concepts/index.md` § "Why this exists"; not all are SUMMARY-registered). However, the existing SUMMARY.md pattern registers nearly all concept pages (verified: ~35 concept rows in SUMMARY.md between lines 64-104), so I added `  - [scalar-promotion](./concepts/scalar-promotion.md)` at the end of the Concepts section (after `scope-out-obstruction`, before `# Design Artifacts`) to preserve discoverability via the sidebar. This is a discretionary auto-fix; integrator-finalize's book rebuild will catch any SUMMARY.md issues. Two OQs promoted: `scalar-promotion-retroactive-l1-thinning` (load-bearing cycle-006+ retroactive-thinning todo to backlink the four L1 entries to this concept page; estimated ~600 words savings) and `scalar-promotion-l4-calculus-formalisation` (forward-looking dependency on L4 typing-judgement adoption to close the pre-existing `scalar-promotion-typing-rule` OQ). The report's caveats #1 (task-brief-vs-evidence correction: `dot` does not scalar-promote — verified; the report correctly scoped to four operators, not five) and #3 (taxonomy classification — now decided) are not promoted as tracking items per cycle-005 staging precedent (process-correction and decision-made caveats are not OQ-tracked). **Adjacent pre-existing breakage NOT addressed**: `book/src/concepts/index.md` has duplicate `complex-from-real-lift` rows at lines 70-71 (and duplicate `solver-as-operator` rows at lines 98-99; both predate this report). Critic finding #2 (META.md:55) and repairer's unrepairable finding flag this for cycle-006 housekeeping; out-of-scope for this per-report dispatch's edit set; routes to cycle-006 cycle-planner as a drive-by fix or to problems/. No gate hits requiring deferral; no rejections; report applied fully as `applied`. Sixth and final per-report integrator dispatch of cycle-005 — integrator-finalize is now ready to run.

---
