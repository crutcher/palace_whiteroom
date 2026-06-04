# cycle-087 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER (append position) is the authoritative apply-order record; `applied_at` is advisory only. integrator-finalize reads this log to reconcile the cycle (rebuild + commit + cycle-record + log + integrator-signals + roadmap).

---

## 2026-06-04T004404Z-lifter-cycle-087-solve-family-stale-reanchor (D1)
applied_at: 2026-06-04T005358Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/index.md (edit — 4 sub-edits: §1a collapsed the "Rough-in at L4" cohort header `(1 + 1 test-coverage-bounded)` → `(1)` + dropped the duplicate solve_family rough-in bullet at :59 — solve_family now in the firm cohort ONLY; §1b re-anchored the :47 firm-cohort entry status clause `rough-in (test-coverage-bounded)` → `firm`, the DO-NOT-TOUCH-list divergence — see Notes; §1c re-anchored the :122 dep-map status cell → `firm`)
- book/src/L4/frequency_sweep.md (edit — §2a :69 contrast re-narrated "firm solve_family entry records per-element out-of-scope"; §2b :506 firm-vs-rough-in contrast block re-narrated to PRESERVE the operator-capture / fresh-vs-reused axis while dropping the now-false maturity contrast, both entries firm)
- book/src/L4-L3/solve-family-map-dissolution.md (edit — §3a :134 LHS status `firm since c086`; §3b :140 §Verified-against §Status bullet; §3c :187 "On the (former) inherited LHS test-coverage caveat" paragraph re-narrated to "cap firmed c086 exactly as anticipated", firm-on-structure reasoning preserved; theme STAYS firm)
- book/src/feature/index.md (edit — §4 :68 narrowed the electrostatic/magnetostatic own-constituent gate to `gram_reduce` alone, "own solve_family firmed c086"; columns STAY seed)
- book/src/L4/fe_assemble.md (edit — §5 :171 contrast re-narrated; solve_family's independence claim *also* discharged on positive structure c086, two combinators now equal maturity; fe_assemble STAYS firm)
- scaffolding/open-questions.md (append-only — new cycle-087 D1 section: 1 DISCHARGEABLE-AT-NEXT-META flag (`solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage` + its parent fold), 1 NEW drift-pattern signal for batch-27 meta-phase, 1 OUT-OF-SCOPE drive-by observation)

Gate hits:
- exact-match-apply: 0 (all 12 [old] anchors matched on-disk unique; applied cleanly)
- dispatch-phase-book-leak: 0 (all 5 book/src files touched are the report's named targets; working tree carried no pre-existing book mutation from this report)
- citecheck (--scan over CYCLE.md): 16 ok, 3 failing — all 3 are [AMBIG] (NOT MISS/OOB/bounds), the report's OWN internal line-number self-references to its subject file `index.md` (unambiguous in context as book/src/L4/index.md per §1 header + §Discipline notes); basename path-hygiene lint only, non-blocking. The single load-bearing L0 citation `palace/linalg/ksp.cpp:297-310` resolves ([ok], const BaseKspSolver::Mult body) — already critic-verified.
- retroactive-budget: n/a (pure maturity re-anchor, no retroactive-evidence slices)
- feature-column-status-flip: 0 (electrostatic + magnetostatic verified `status: seed` on-disk AFTER edits — NOT flipped; §4 narrates the narrowed gate only)
- other-operator-maturity-change: 0 (domain_energy_reduce verified `firmness: rough-in` unchanged — the sole remaining L4 rough-in, matching the new `(1)` header; no other operator touched)
- count-reconciliation: index.md "Firm at L4 (17 + 4 outer-driver)" header + "Rough-in at L4 (1)" header now consistent with on-disk solve_family.md `firmness: firm` + the c086 cycle-record counts (L4_firm:17, L4_rough_in:1, L4_rough_in_test_coverage_bounded:0). NO new count-owner decision made — pure prose reconciliation against the c086-finalize-authoritative counts.

Open questions promoted:
- solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage (DISCHARGEABLE-AT-NEXT-META; the parent fold `solve-family-firm-on-structure-vs-test-coverage` is now fully dischargeable — both sub-questions resolved. NOT closed here; flagged for batch-27 meta-phase unify-close)
- firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep (NEW drift-pattern signal for batch-27 meta-phase; the FIRM-analog of floor-landing-implies-same-cycle-adjacent-entry-reanchor — strengthened by the c086 sweep having missed sites in the SAME file `index.md` it partially corrected. Integrator-finalize should ALSO route this as an integrator-signal.)
- (drive-by observation, not a durable OQ slug) feature/eigenfrequency-qfactor.L4.md:38 still labels eigenfreq_qfactor_reduce `rough-in (test-coverage-bounded)` despite firm c082 — SEPARATE stale ref, OUT-OF-SCOPE for this solve_family-only report, NOT corrected (no scope creep); reinforces the drift-pattern signal above.

Build-relevant: yes (edits touch 5 book/src/*.md files — book rebuild needed at finalize)

Notes:
- DO-NOT-TOUCH-list divergence APPLIED (correct per report §Discipline notes + critic META): the plan listed `L4/index.md:47` as "correctly-firm → KEEP" on the on-disk-FALSE assumption the firm-cohort entry body already read `*(firm; cycle-086 D1)*`. On-disk the :47 firm-cohort entry BODY still asserted `Status rough-in (test-coverage-bounded)` two lines below the :32 header narrating the c086 firm promotion — a genuine internal contradiction in the SAME maturity-drift class as the 5 plan-named sites, L0-evidenced by solve_family.md:4 `firmness: firm`. Applying the :47 re-anchor is the correct land-clean disposition (declining it would leave a surviving firm-cohort entry asserting rough-in); critic confirmed it is a legitimate stale-correction NOT an out-of-scope leak. Surfaced here so finalize does not treat it as a scope breach.
- deferred integrated_at to finalize per role-spec (this integrator does NOT touch the consumed report's integrated_at / integration_commit frontmatter).
- scaffolding/priorities.md shows as `M` in git status but was NOT touched by this dispatch (cycle-planner write-authority, modified during the planning phase before integration). Left untouched per write-authority partition.
- cycle-record JSONL `counts_after` L4 sub-tally reconciliation (L4_rough_in_test_coverage_bounded 1→0 if solve_family was counted there at c086) is integrator-finalize scope — the on-disk c086 cycle-record already carries L4_rough_in_test_coverage_bounded:0, so finalize likely only confirms no drift. Flagged for finalize.
- First per-report integrator this cycle — created reports/cycle-087-integrator-staging/STAGING.md.

---
