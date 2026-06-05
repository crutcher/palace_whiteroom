# cycle-098 — integrator-per-report staging log

Append-only. Newest row LAST. The **row ORDER** (append position) is the authoritative
apply-order record — NOT the `applied_at` timestamps (advisory only). integrator-finalize
reads this log to reconcile the cycle (book rebuild, roadmap, cycle-record, log,
integrator-signals, commit). Per-report integrators do NOT rebuild/commit/housekeep.

---

## 2026-06-05T002531Z-same-layer-cross-cutter-orthog-slice-delete (D1)
applied_at: 2026-06-05T00:46:43Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/gemv_basis.md (edit — PC-1: slice-link `slices/orthog.md` → `[orthogonalization](./orthogonalization.md)`)
- book/src/L1/orthogonalize.md (edit — PC-2: pending-lift anchor :299-304 → claim-free Provenance prose; arnoldi bullet :305-308 left UNTOUCHED per boundary caution)
- book/src/L0/mpi-globalsum-and-collectives.md (edit — PC-4a :69, PC-4b :105 → `[orthogonalization](../concepts/orthogonalization.md)`)
- book/src/concepts/orthogonalization.md (edit — PC-4c :77 self-page slice link → `[L2/orthogonalize]` + `[L3/orthogonalize]`)
- book/src/concepts/gmres.md (edit — PC-4d :23 dropped slice link; firm orthogonalization concept link retained)
- book/src/concepts/sequential-obstruction.md (edit — PC-4e :48 → `[L3/orthogonalize](../L3/orthogonalize.md)`)
- book/src/spec/slices/arnoldi_step.md (edit — PC-4f :67,:95,:115,:144 — 4 dangling `./orthog.md` sibling links → `[orthogonalization](../../concepts/orthogonalization.md)`; arnoldi_step slice SURVIVES, c099 scope)
- book/src/spec/slices/orthog.md (DELETE — PC-3, via `git rm`; reachability-GC detritus, no inbound depends-on edge)
- scaffolding/open-questions.md (append — `orthog-slice-substantive-absorb-framing-was-a-verified-no-op` record)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- bookkeeping-incomplete: 0
- SUMMARY/index chapter-registration auto-fix: 0 (deletion, not creation; SUMMARY:295 + spec/index:17 row removals are D2 single-owner scope — NOT touched here per dispatch)
- graded-stack rank-gate: 0 violations (PC-3 deletes detritus with no inbound `depends-on` edge — producer+critic independently confirmed `grep depends-on | grep orthog` empty; no rank-gate flip in this report)
- citecheck (--scan): 38 ok, 1 failing (39 checked). The single MISS is `slices/arnoldi_step.md:5` — a bare path-form citation inside a PC-2 OQ-caveat prose note; the file EXISTS at `book/src/spec/slices/arnoldi_step.md` (citecheck couldn't resolve the `spec/`-less bare basename relative to reference/ + book/src). Benign path-prefix artifact in a caveat note, NOT a load-bearing proposed-change anchor. Non-blocking (not a MISS on any applied edit's target).

Open questions promoted:
- orthog-slice-substantive-absorb-framing-was-a-verified-no-op (records the stale "substantive MPI-collective-shape absorb" tranche framing as a VERIFIED NO-OP for the c099 planner / batch-31 meta-phase)

Build-relevant: yes

Notes:
- All 11 `[old]` anchors (PC-1, PC-2, PC-4a–f across 8 link repoints) were re-read against disk THIS invocation before each Edit; every one matched verbatim. The repairer-added PC-4 was present in the CYCLE.md I read.
- **CO-APPLICATION CONSTRAINT for integrator-finalize (load-bearing).** PC-3 deleted `book/src/spec/slices/orthog.md` in THIS report (D1), but the two surviving live markdown links to it — `book/src/SUMMARY.md:295` (TOC row) + `book/src/spec/index.md:17` (dep-map table row) — are **D2's single-owner row-removal scope** (D2 removes orthog's AND polynomial's rows, applied NEXT). Post-D1, those are the ONLY two live links pointing at the deleted file (verified by `grep -rnE '\]\([^)]*orthog\.md' book/src` — exactly SUMMARY:295 + spec/index:17, nothing else). The book is link-clean ONLY after D2 lands. Do NOT run `cargo make book` / linkcheck2 between D1 and D2; finalize builds once after BOTH land. (Per the repairer's "Co-application constraint" note in META Suggested-resolution.)
- §1 absorb is a critic-verified NO-OP (the slice's MPI-collective-shape + L1-invariant content is fully firm-homed). No content claim was added or altered by this report — it is repoint + delete only.
- The `meta-reviews/*` hits for `orthog.md` are historical prose/path mentions in frozen historical records, NOT live `[..](..)` markdown links to the deleted slice (verified) — they leave no dangling link.
- I did NOT touch the consumed report's `integrated_at:` / `integration_commit:` frontmatter — deferred to finalize per role-spec.

---
## 2026-06-05T002531Z-same-layer-cross-cutter-polynomial-slice-delete (D2)
applied_at: 2026-06-05T01:55:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/krylov-step.md (edit — R1: SURGICAL polynomial-clause drop at line 7, cg/gmres/chebyshev/arnoldi clauses PRESERVED byte-exact; R2: line 142 polynomial-only §Evidence bullet → `concepts/negative-result-slice.md` + `L4/chebyshev.md` §Semantics `innerStep`)
- book/src/L2/index.md (edit — R3: line 135 polynomial dep-map evidence line → `concepts/negative-result-slice.md`; :131-134 cg/gmres/chebyshev/arnoldi trio PRESERVED)
- book/src/concepts/dependency-map.md (edit — R4: removed 3 underscore `polynomial_recurrence_step` slice-node mermaid edges at :169-171; hyphenated `polynomial-recurrence-step:::planned` planned-node at :77-79,:98 PRESERVED; `plane-rotation-stream --> givens_generate`/`givens_apply` untouched)
- book/src/concepts/negative-result-slice.md (edit — R5: delinked the 2 LIVE markdown links at :46 + :66 — the co-landing blocker outside the planner's 4-site list; prose preserved, `(../spec/slices/...)` targets removed)
- book/src/L3/krylov-step.md (edit — R9 [repair-added]: line 200 plain-text slice-anchor `polynomial_recurrence_step.md:119-160` → `concepts/negative-result-slice.md` + `L4/chebyshev.md` §Semantics `innerStep`, parallel to R2/R3)
- book/src/SUMMARY.md (edit — R7: removed BOTH orthog row (:295) AND polynomial row (:296); trio rows Arnoldi:292/CG:293/GMRES:294 PRESERVED)
- book/src/spec/index.md (edit — R8: removed BOTH orthog status row (:17) AND polynomial status row (:19); trio rows CG:15/GMRES:16/arnoldi:18 PRESERVED)
- book/src/spec/slices/polynomial_recurrence_step.md (DELETE — R6, via `git rm`; reachability-GC detritus, no inbound `depends-on` edge, content fully firm-homed in `concepts/negative-result-slice.md`)
- scaffolding/open-questions.md (append — `polynomial-recurrence-step-slice-absorb-verified-no-op-and-campaign-state-5to3-slices`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate to finalize — finalize sees full staging log)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- bookkeeping-incomplete: 0
- SUMMARY/index chapter-registration auto-fix: 0 (deletion, not creation — R7/R8 are deliberate dual-slice ROW removals for BOTH orthog + polynomial)
- graded-stack rank-gate: 0 violations (`grep -rniE depends-on | grep polynomial_recurrence_step` empty — slice is detritus, no firm rank rests on it; reachability-GC 5→3 slices)
- citecheck (--scan): 35 ok, 5 failing (40 checked). ALL 5 failures are EXPECTED deletion-report artifacts on the report's `old:`/supporting-evidence text, NOT on any applied `new:` target: 3× MISS on `polynomial_recurrence_step.md:119-160`/`:70-119` (the slice this report DELETES — the `old:` anchors being removed), 1× AMBIG on bare `gmres.md:459-471` (prose; basename matches concepts/+spec/slices/ — a path-hygiene note on surviving cg/gmres clause prose, not an applied-edit anchor). Every applied `new:` repoint target (`concepts/negative-result-slice.md`, `book/src/L4/chebyshev.md`) was independently verified to resolve + carry its cited §Partial-positive/§Falsification/§Semantics sections. Non-blocking — no MISS/AMBIG/OOB on a landed edit's resolved target.

Open questions promoted:
- polynomial-recurrence-step-slice-absorb-verified-no-op-and-campaign-state-5to3-slices

Build-relevant: yes

Notes:
- All 9 `[old]` anchors (R1, R2, R3, R4, R5×2, R9, R7, R8×2) were re-read against disk THIS invocation before each Edit; every one matched verbatim. The repairer-added R9 was present in the CYCLE.md I read.
- POST-APPLY VERIFICATION (clean): `grep -rnE '\]\([^)]*polynomial_recurrence_step\.md' book/src/ | grep -v meta-reviews` → NONE (no surviving markdown link); `grep -rnE 'polynomial_recurrence_step\.md:[0-9]' book/src/ | grep -v meta-reviews` → NONE (no surviving plain-text anchor, incl. R9's L3 site); `grep '\](.*spec/slices/orthog\.md' book/src/ | grep -v meta-reviews` → NONE; SUMMARY+spec/index rows for both deleted slices → NONE. The 3 surviving krylov-trio rows (cg/gmres/arnoldi_step) confirmed intact in BOTH SUMMARY (292-294) and spec/index (15-17). R1's cg/gmres/chebyshev/arnoldi clauses confirmed intact on line 7 (c099 krylov-trio material preserved). The `meta-reviews/*` hits are frozen historical prose mentions (NOT live links), no dangling link.
- ORTHOG ROW REMOVAL (R7/R8 orthog half) is CORRECT + REQUIRED: I re-read disk this invocation and DIRECTLY OBSERVED `book/src/spec/slices/orthog.md` is ALREADY DELETED (D1's row is present in this STAGING.md AND `test -f` confirmed the file gone on disk). Removing its now-orphaned SUMMARY/spec-index nav rows here resolves the D1↔D2 serialization caveat (#3) the report flagged. The book is link-clean for both slices only after D2 (this report) lands.
- Reachability-GC: orthog (D1) + polynomial (D2) now both fully unreachable; Phase-1 slice corpus 5→3. Krylov trio (cg/gmres/arnoldi_step) deferred to c099 per OQ.
- I did NOT touch the consumed report's `integrated_at:` / `integration_commit:` frontmatter — deferred integrated_at to finalize per role-spec.
- Did NOT run `cargo make book` / commit / housekeeping — all integrator-finalize scope. Co-application complete: D1 + D2 together leave the book link-clean for both deleted slices; finalize builds once after this row.

---
## 2026-06-05T002531Z-lifter-domain-energy-reduce-313-gram-reduce-landclean (D3)
applied_at: 2026-06-05T00:52:05Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/domain_energy_reduce.md (edit — single PC: re-anchored the :313-316 §Status closing parenthetical; dropped the falsified "gram_reduce STAYS rough-in because bilinear-form is still rough-in" maturity assertion; recast as the post-c095 firm-cascade-complete + permanent rank-1-vs-rank-2 / single-field-vs-family-PAIR SHAPE distinction. Both links [gram_reduce](./gram_reduce.md) + [bilinear-form](../L1/bilinear-form.md) retained; no frontmatter touched)
- scaffolding/open-questions.md (append — RESOLVED record for `domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate to finalize)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- bookkeeping-incomplete: 0
- SUMMARY/index chapter-registration auto-fix: 0 (prose-only within-file edit; no new file/chapter)
- index-placeholder-displacement: 0
- implied-component-stub: 0
- graded-stack rank-gate: 0 violations (NO node status flip — pure prose re-anchor; `domain_energy_reduce` already `rank: firm` resting on `depends-on: L1/participation_ratio` + `L1/matrix-weighted-norm` both firm on disk → `rank(u) ≤ min(deps)` holds unchanged; no new edge, no firm-flip authored here)
- citecheck (--scan): 5 ok, 0 failing (5 citations checked) — clean.

Open questions promoted:
- domain_energy_reduce-313-gram_reduce-bilinear-form-c095-stale-rough-in-narration (RESOLVED-by-re-anchor record appended; the original `new`/`opened` entry at open-questions.md:1517 left intact per append-only; meta-phase does the close/unify)

Build-relevant: yes

Notes:
- The single `[old]` anchor (the :313-316 parenthetical) was re-read against disk THIS invocation before the Edit and matched verbatim. This file (`book/src/L4/domain_energy_reduce.md`) is DISJOINT from D1's and D2's touched-file sets — I re-read the staging log and confirmed neither D1 nor D2 lists this file; I did not assume any sibling landing affected it.
- Load-bearing premise re-verified on disk THIS invocation (not trusted from the report): `book/src/L4/gram_reduce.md:4-5` = `firmness: firm` / `rank: firm` AND `book/src/L1/bilinear-form.md:4-5` = `firmness: firm` / `rank: firm` (the cycle-095 firm-flip). The parenthetical's "STAYS rough-in" / "is still rough-in" premise is FALSIFIED on disk; the re-anchor is correct.
- The c097-D6 matrix-weighted-norm residues at :268/:374/:377 were NOT touched (already fixed by c097-D6, out of this cohort's scope, confirmed by the report's self-consistency sweep + not in my single PC).
- No `rank:`/`edges:`/frontmatter flip needed or made (prose-only); no new rank-gate violation introduced; baseline violations unchanged.
- The whole-book `bilinear-form`-c095-firm-flip residue-class sweep (other files co-mentioning gram_reduce+rough-in) is a SEPARATE cross-file land-clean for the c095 gram_reduce flip's lineage — out of this within-file dispatch's scope; flagged in the OQ resolution record for the batch-31 §Intake→plan migration. Not actioned here.
- I did NOT touch the consumed report's `integrated_at:` / `integration_commit:` frontmatter — deferred integrated_at to finalize per role-spec.
- Did NOT run `cargo make book` / commit / housekeeping — all integrator-finalize scope. (Note: D1+D2 left the book link-clean for the two deleted slices per D2's verification; this D3 prose-only edit introduces no link change. Finalize builds once after this row.)

---
