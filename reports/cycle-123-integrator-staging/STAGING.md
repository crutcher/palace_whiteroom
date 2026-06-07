# cycle-123 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative apply-order
record (NOT the `applied_at` timestamps, which are advisory). integrator-finalize reconciles from
this log.

---

## 2026-06-07T083902Z-layer-intro-author-refinement-data-concepts-page (D4)
applied_at: 2026-06-07T085908Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/RefinementData.md (created — firm record-definition page for the AMR config record `RefinementData`)
- book/src/L1/dorfler_mark.md (edited — θ-field reference re-pointed to concepts/RefinementData.md; struct cite :97-119 → :97-154)
- book/src/L1-L0/amr-estimate-mark-refine.md (edited — `RefineConfig` §Record-definition bullet re-pointed to concepts/RefinementData.md; struct cite :96-125 → :97-154)
- book/src/SUMMARY.md (edited — registered concepts/RefinementData.md in the concepts list, alpha position between `rotation` :364 and `scal` :365)
- scaffolding/open-questions.md (append-only — RESOLVED note appended under record-RefinementData-needs-concept-definition-home)

Gate hits:
- citecheck bounds + path-hygiene lint: 0 failing (35 ok, 0 failing — clean; ran `tools/citecheck/citecheck.py --scan` over CYCLE.md; the repairer-corrected ctor extent configfile.cpp:318-359 and box/sphere sub-range :334-357 + the struct extent configfile.hpp:97-154 all verify exact on-disk)
- record-definition discipline: 0 (page defines data-shape only, defers behaviour to consumers; ≥2-consumer bar genuinely met by dorfler_mark + amr-estimate-mark-refine + lifecycle.L4 AMR fold)
- SUMMARY alpha-position insert: 0 (report specified the position; verified case-insensitive alpha correct — `refinementdata` sorts after `rotation`, before `scal`; not discretionary, position was given)
- forward-edge claim without surface: 0
- rank gate (rank(u) ≤ min deps): 0 (page is rank: firm; only blocking edges are cites-evidence depends-on to rank-terminal L0 ground truth — invariant holds vacuously; consumer edges are `reference` (free))
- variant-axis / edge-label / H1-reuse / append-on-missing-slug: 0

Open questions promoted:
- record-RefinementData-needs-concept-definition-home (CLOSED this dispatch — RESOLVED note appended to open-questions.md; meta-phase may formally migrate)

Build-relevant: yes

Notes:
- META overall_status: ready (canonical; set by repairer after fixing citation-validity + cross-reference-integrity warnings). Applied cleanly.
- Repairer's in-place CYCLE.md fixes were already reflected in the report I read: ctor range configfile.cpp:318-377 → :318-359 (the load-bearing depends-on cites-evidence edge target), box/sphere sub-range :334-377 → :334-357, and the spurious `reference: L1/flux_recovery_estimate` frontmatter edge dropped. I applied the corrected forms.
- The repairer left `ParseOptional<RefinementData>` cite at configfile.cpp:378 (deliberate not-needed — critic mis-pinpointed :379; repairer verified :378 is correct on disk via codemap search_text + Read). I did NOT alter it; the page carries :378 as authored. Independent on-disk confirmation not separately re-run by me, but citecheck --scan (bounds-mode) passed all 35 cites including this one's enclosing range.
- This report integrated FIRST in cycle-123 specifically so D1 (AMR group-intro, links to ../concepts/RefinementData.md) resolves once it lands. The new page is on disk; D1's forward link will resolve.
- SUMMARY.md is a shared-file this cycle (D1 nesting block ~:245, D2 feature Part block ~:54). My edit is the disjoint concepts-list region (:364/:365). Subsequent per-report integrators MUST re-read SUMMARY.md off disk before their edits (per role-spec) — my insertion shifts line numbers below :365 by +1.
- I observed only this invocation's on-disk state; no sibling-landing claims made (D1/D2 not yet applied at the time I read SUMMARY.md — the concepts-list region was the pre-cycle baseline plus my insertion).
- Deferred integrated_at to finalize per role-spec.

---

## 2026-06-07T083902Z-layer-intro-author-amr-estimate-mark-group-intro (D1)
applied_at: 2026-06-07T090125Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/amr-estimate-mark-intro.md (created — navigational-container by-kind group-intro for the AMR estimate/mark vocabulary; `kind: navigational-container (group intro)`, NO `rank:`, `reference`-only edges to L1/dorfler_mark + L1/flux_recovery_estimate)
- book/src/SUMMARY.md (edited — re-nested the 2 flat AMR verbs under the new `AMR estimate / mark vocabulary` grouping, placed after the FE-space sub-spine grouping; anchor was the FE-space-sub-spine→flat-AMR span, on-disk lines 239-246 after D4's +1 shift)
- book/src/L1/index.md (edited — dep-map TABLE group-header de-stale `**Rough-in (AMR estimate/mark vocabulary)**` → `**AMR estimate/mark vocabulary**` at on-disk line 208; both verb rows 209-210 already read `firm`)

Gate hits:
- cross-reference-integrity resolution (the needs-revision driver): RESOLVED. `../concepts/RefinementData.md` confirmed on-disk (created by D4, prior staging row); all four outbound links from the intro resolve relative to book/src/L1/ (flux_recovery_estimate.md, dorfler_mark.md, ../L1-L0/amr-estimate-mark-refine.md, ../concepts/RefinementData.md — all OK). Producer's defang fallback NOT needed (D4 landed). No content edit made.
- new-summary-kind-grouping GATE (group-intro exists before SUMMARY nests it): 0 (satisfied — created amr-estimate-mark-intro.md FIRST, then nested; grouping link points at the freshly-created file, no duplicate-file / placeholder reuse)
- both AMR verbs firm: 0 (confirmed on-disk: index.md rows 209-210 both read `firm`; verbs' frontmatter rank: firm)
- navigational-container reference-only edges: 0 (no `rank:`, `reference:`-only to the 2 members; matches fe-space-intro.md / mesh-construction-intro.md precedent)
- citecheck bounds + path-hygiene lint: 0 failing (6 ok, 0 failing — ran `tools/citecheck/citecheck.py --scan` over CYCLE.md)
- forward-edge claim without surface / edge-label mismatch / H1-reuse / variant-axis / rank gate: 0 (navigational container makes no rank/depends-on claim; rank gate vacuous — only reference edges)

Open questions promoted:
- (none new) — the report's `## Open questions / caveats` are all integrator-coordination notes (D4 ordering, SUMMARY shared-file coupling, two-headers analysis, no-new-claims), not fresh cross-cycle questions. No new OQ ledger section appended.

Build-relevant: yes

Notes:
- META overall_status: needs-revision with follow_up_agent: integrator-per-report — the SOLE issue was the cross-dispatch integration-ordering coupling on `../concepts/RefinementData.md` (D4's page). The repairer marked it `unrepairable` and explicitly routed it here with "no content work; apply D4 BEFORE D1". D4 landed first (its staging row precedes this one), so the link resolves. Per the role-spec apply-without-content-revision path for an integration-ordering-only needs-revision routed to integrator-per-report, I applied D1 unchanged. Treated as ready-to-apply (no synonym normalization — the status genuinely was needs-revision, but the finding was integration-sequencing, fully discharged by the D4-before-D1 ordering the parent dispatched).
- I observed the D4 landing both via its staging row (above) AND by directly stat-ing book/src/concepts/RefinementData.md on disk this invocation (exists, 13249 bytes) — not assumed.
- The report Summary's member-link prose used wrong relative depth `../book/src/L1/...`, but that is report narrative only; the actual proposed-changes file content uses correct `./flux_recovery_estimate.md` / `./dorfler_mark.md` (critic Notes confirmed). No artifact impact.
- This report's Summary CLOSES OQ `amr-estimate-mark-group-intro-needs-authoring` (open-questions.md line 1812). I did NOT edit that OQ — closing/migrating is meta-phase unify authority; flagging for finalize/meta to formally close. The deferred c122 navigational hygiene is now landed: AMR verbs re-nested, intro authored, index header de-staled.
- SUMMARY.md shared-file this cycle (D4 concepts list :364/:365, D1 L1-chapters block, D2 feature Part). I re-read SUMMARY off disk before editing; D1's anchor (FE-space sub-spine → flat AMR, on-disk 239-246) matched exactly and uniquely after D4's +1 shift. My nesting edit shifts lines below ~246 by +1 — any subsequent per-report integrator (e.g. D2) MUST re-read SUMMARY off disk.
- Deferred integrated_at to finalize per role-spec.

---
## 2026-06-07T083902Z-layer-intro-author-krylov-iteration-column (D2)
applied_at: 2026-06-07T093500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/krylov-iteration.L4.md (created — infrastructure feature-surface composition-root, the L3 iteration-rotation spine; `feature_root: seed`, `rank: rough-in`; blocking `depends-on (composes)` → L3/krylov-step + L3/fold_solve + L3/orthogonalize + L4/iterate-while + L4/ksp_solve; `reference` → eigsolve-impl/lanczos_step + sibling feature columns + concepts + semantics/index)
- book/src/feature/krylov-iteration.L1.md (created — L1 pure-function surface; `rank: rough-in`; blocking `depends-on (composes)` → L1 orthogonalize/apply_linop/axpy/axpby/dot/nrm2/scal; `reference` → krylov-iteration.L4 + the 3 L3 views + sequential-obstruction)
- book/src/feature/index.md (edited — added the `krylov-iteration (rough-in)` row under the Infrastructure grouping, alpha-after geometric-multigrid-preconditioner)
- book/src/feature/infrastructure.md (edited — added krylov-iteration.{L4,L1} to the `reference` frontmatter; added the member-list bullet; KEPT the GMG member-status `(rough-in.)`→`(firm.)` honest reconciliation per repairer's on-disk confirmation that GMG is firm)
- book/src/SUMMARY.md (edited — nested `krylov-iteration — L4/L1 composition-root` under the Infrastructure grouping, high→low within-column order, after the GMG entries)

Gate hits:
- citecheck bounds + path-hygiene lint: 0 failing (21 ok, 0 failing — ran `tools/citecheck/citecheck.py --scan` over CYCLE.md; the repairer's 6+1 iterative.cpp pinpoint-drift corrections are reflected in the applied report)
- graded-stack rank well-foundedness (rank(u) ≤ min deps): 0 violations (lint `rank_violations: 0`; rough-in over min(firm, partial-obstruction, partial-obstruction)≈2.5 is permissible — firm would have violated it, which is exactly why the column lands rough-in and the firm-vs-rough-in question is an OQ for the meta, NOT silently resolved)
- unresolved depends-on targets: 0 (all 7 L4 + 7 L1 blocking depends-on edges resolve on disk)
- RE2/RE8 reachability discharge (the load-bearing confirmation): CONFIRMED as a GENUINE depends-on root→node flip. Post-apply lint: `L3/orthogonalize` (RE2), `L3/krylov-step` + `L3/fold_solve` (RE8) ALL flip to REACHABLE (out of the STRONGER/detritus lists) via the new feature_root column's `depends-on (composes)` edges. Mechanically distinct from the c122 reference-only-reachable cohort.
- eigsolve-impl/lanczos_step reference-not-depends-on correctness: CONFIRMED — both stayed DETRITUS/STRONGER (gained NO liveness from the column's `reference` edges, exactly as the report predicted; a depends-on there would have been a §2g over-edge + a rank violation rough-in→roadmap_goal). The reference-only-reachable behavior is the correct second data class for the meta.
- new column files register as GC roots: 0 (both `feature/krylov-iteration.{L4,L1}` appear as roots, `feature_root: seed`; 43 roots total)
- alpha-within-kind insert: 0 discretionary (krylov-iteration sorts after geometric-multigrid-preconditioner — alpha-correct append within the Infrastructure kind grouping; report specified the position)
- SUMMARY new-grouping / group-intro: not-applicable (Infrastructure grouping + its intro `feature/infrastructure.md` already exist from the GMG column; this is a 2nd member nested under the existing grouping, no new grouping opened)
- forward-edge claim without surface / variant-axis / edge-label / H1-reuse / append-on-missing-slug: 0

Open questions promoted:
- krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views (for the batch-39 meta — the well-foundedness rough-in vs GMG-precedent firm adjudication)
- eigsolve-impl-reference-uplink-to-krylov-iteration-column (optional cosmetic reference-uplink for a future lifter)

Build-relevant: yes

Notes:
- META overall_status: ready (canonical; set by repairer after fixing the citation-validity warning — 6 per-line +1 pinpoint drifts in iterative.cpp decremented; the enclosing ranges were always correct so no claim was ever unsupported). Applied cleanly.
- HEADLINE — RE2/RE8 DISCHARGE CONFIRMED AS A REACHABILITY FLIP (not a reference-only-reachable artifact). I re-ran `graded_stack_lint.py --book-src book/src --json` AFTER applying the edits and directly observed: L3/krylov-step, L3/fold_solve, L3/orthogonalize all moved to REACHABLE; L3/eigsolve-impl + L3/lanczos_step stayed STRONGER (reference-only, unchanged). This is the clean second data class the planner wanted for the batch-39 meta reference-edge-liveness adjudication: a depends-on RE-discharge (reachable-flip) mechanically distinct from the c122 reference-only-reachable kernel-impl/combinator cohort.
- KEPT the GMG member-status `(rough-in.)`→`(firm.)` normalization in feature/infrastructure.md (the side-edit the critic flagged informational): the repairer confirmed on disk that GMG is firm (`geometric-multigrid-preconditioner.L4.md` frontmatter `rank: firm` + `## Status: firm` post-c122-D7; `.L1.md rank: firm`) and that `infrastructure.md:39` carried a stale c122 `(rough-in.)` drift while `index.md:59` already read `(firm)`. The normalization is an honest reconciliation, KEEP-confirmed.
- SHARED-FILE coordination (SUMMARY.md): D4 (concepts list ~:364) + D1 (L1 AMR group ~:239-246) edited SUMMARY earlier this cycle, both BELOW the feature Part region. I re-read SUMMARY off disk before editing; the feature Infrastructure anchor (on-disk lines 54-56) matched D2's `[old]` block verbatim and uniquely (unshifted by D4/D1, which were below line 246). feature/index.md (also touched by D9 in c121): the `[old]` anchor at lines 58-59 matched current on-disk verbatim. I observed only this invocation's on-disk file state for all anchors; no sibling-landing assumptions.
- Deferred integrated_at to finalize per role-spec.

---
## 2026-06-07T083902Z-same-layer-cross-cutter-correction-step-wider-propagate (D3)
applied_at: 2026-06-07T094800Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only — 3 sections appended: RESOLVED note for `correction-step-wider-replace-and-propagate-set-l1-and-feature-column` (c122-opened), RESOLVED note for `correction-step-replace-and-propagate-scope` (c121-opened, transitive close), and new OQ `correction-step-l4-reference-edge-adds-to-reference-only-reachable-liveness-evidence` promoting the report's caveat-1 meta-evidence)

Gate hits:
- (no book/ edits — pure observation report; no book safety gates apply): 0
- citecheck bounds + path-hygiene lint: 0 failing (9 ok, 0 failing — ran `tools/citecheck/citecheck.py --scan` over CYCLE.md; the two load-bearing source ranges `distrelaxation.cpp:101-119` + `gmg.cpp:172-205` both verify in bounds; matches the critic's independent on-disk read)
- reference-edge-class confirmation: N/A this dispatch (no L4 reference down-link landed — the report SURFACES it as a follow-up candidate, does NOT enact it; the candidate edge IS confirmed `reference`-class in the report's verdict + the promoted OQ, for the future enacting agent)
- forward-edge claim without surface / edge-label / variant-axis / rank gate / H1-reuse / append-on-missing-slug / SUMMARY-registration: 0 (no book mutation)

Open questions promoted:
- correction-step-wider-replace-and-propagate-set-l1-and-feature-column (CLOSED — RESOLVED note appended; c122-D3 harvester-opened; meta-phase may formally migrate)
- correction-step-replace-and-propagate-scope (CLOSED transitively — RESOLVED note appended; c121-combinator-miner-opened; the L1-gate-keeps-closure layer-placement refinement is now settled)
- correction-step-l4-reference-edge-adds-to-reference-only-reachable-liveness-evidence (NEW — promotes the report's caveat-1; intentional reference-edge-liveness meta-evidence for the batch-39 meta-phase adjudication)

Build-relevant: no

Notes:
- META overall_status: ready (canonical; all 8 checks pass — set directly by the critic on an all-pass clean report, no repairer ran). Applied cleanly.
- PURE OBSERVATION REPORT — NO `## Proposed changes` section, NO `edit:` blocks (confirmed by grep over CYCLE.md). A same-layer-cross-cutter surfaces a verdict + flags follow-up candidates; it does NOT mutate book/. The report explicitly states "none enacted here — I surface; harvester / combinator-miner / layer-intro-author enact". So this dispatch promotes OQs only; no book edit was authored to apply, by design (the dispatch prompt anticipated this path).
- The report's follow-up candidates are NOT enacted (they require a producer dispatch, out of integrator scope): (1) combinator-miner/layer-intro-author add the L4 `reference` down-link `feature/geometric-multigrid-preconditioner.L4 → L2/correction_step` + reword the L4 vcycle prose to NAME correction_step; (2) harvester/layer-intro-author add 2 L1 downward annotations (prose + reference link, NOT depends-on edges) to `L1/multigrid-relaxation-smoother` + `feature/geometric-multigrid-preconditioner.L1`. These are recorded in the promoted OQ `correction-step-wider-...` RESOLVED note for the planner to route to a future cycle. NOTHING in the corpus changed re: the L4 reference-only-reachable status this cycle (no edge landed).
- The reference-edge-liveness meta-evidence (caveat 1) is COMPLEMENTARY to the c123-D2 RE2/RE8 depends-on reachability FLIP (this staging log, D2 row): D2 = depends-on flip (krylov-step/fold_solve/orthogonalize → REACHABLE); this report's candidate = reference-only-reachable (correction_step stays STRONGER even if the L4 ref edge lands). Together = the two data classes the batch-39 meta wants for the reference-edge-liveness adjudication. Surfaced via the new OQ; meta-phase folds it in.
- Deferred integrated_at to finalize per role-spec.

---
