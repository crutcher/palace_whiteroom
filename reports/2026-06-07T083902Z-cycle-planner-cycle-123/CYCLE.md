---
agent: cycle-planner
invoked_at: 2026-06-07T083902Z
scope: cycle-123 dispatch plan (batch-39 position 3/3 — THE BATCH-CLOSING primary cycle; batch-39 meta fires AFTER this finalize)
status: pending
---

# Cycle 123 dispatch plan

## Goals selected this cycle

c123 is the **batch-closing** cycle of meta-batch-39 (121/122/123). The c122 finalize flagged the
**reference-edge-liveness scheme question** as the headline batch-39-meta adjudication — and confirmed it
is NOT a defect but a systematic artifact of the combinator-primary + DIRECTIVE-3 dual-surface models. With
a wide new-vocabulary wave therefore *less* valuable than consolidation+hygiene before the meta, c123 favors
**(a) the deferred AMR navigational hygiene** the c122 wave left, **(b) the ONE highest-fan-out residual-RE
discharge** (the L3-iteration-view feature column, DIRECTIVE-2 item-4b, discharging RE2/RE8), **(c) the wider
correction_step replace-and-propagate** routed to the same-layer-cross-cutter, and **(d) one cheap honesty
record-definition pick** (`concepts/RefinementData.md`, ≥2-consumer bar now fired). Four dispatches, ONE wave
(all parallel — disjoint file regions). The RE-recheck (below) confirms c121/c122's discharges HELD on the
landed tree; the residual STRONGER set decomposes cleanly into the ratified RE cohorts + exactly the 7
c121/c122-new reference-only-reachable firm nodes — which IS the scheme-question evidence the meta needs.

## RE-premise re-check (run on the LANDED tree — `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src --json`)

Live linter (on disk this cycle, exactly matching the c122 finalize): `files=385, typed=324, untyped=61,
roots=41, reachable=150, detritus=136 (no_typed=108, STRONGER=28), rank_violations=0, unresolved_depends_on_targets=0,
promotion_frontier=12, rank_histogram={firm:224, roadmap_goal:7, typed-no-rank:82, rough-in:2, partly-constructive:3, obstruction:2, partial-obstruction:4}`.

**c121/c122 discharges HELD ✓:** RE10 DISCHARGED (`L1/interpolator` off STRONGER ✓ — not in the list); RE9
GROUNDED (`fe_space_hierarchy` reachable ✓); `unresolved_depends_on_targets` 6→0 HELD ✓; `rank_violations` HELD 0 ✓.

**STRONGER (28) decomposition — 21 RE-accounted + 7 reference-only-reachable c121/c122-new nodes:**

| RE | members in STRONGER | verdict |
|---|---|---|
| RE1 | `L3/chebyshev`, `L2/jacobi-smoother` (2/5) | HELD — re-stated by c122 (GMG firm re-type; L2/L3 iteration-VIEWS absorbed-below-spine like RE5/RE7; L1 chebyshev-smoother GROUNDED via the smoother chain). OQ `gmg-firm-flip-re1-reachability-l2l3-iteration-views-absorbed-below-spine`. |
| RE2 | `L3/orthogonalize` (1/2) | HELD — **the D2 target** (L3-iteration-view feature column discharges it). |
| RE5 | `L3/normalize`, `L3/reciprocal`, `L2/normalize`, `L2/reciprocal` (4/5) | HELD (absorbed normalize/reciprocal chain). |
| RE6 | all 8 axpy/scal arity leaves | HELD (combinator-primary; combinator-arity-notes refactor still pending, item-4c). |
| RE7 | `L2/elementwise_product`, `L3/elementwise_product`, `L3/assemble-diagonal`, `L3/jacobi-smoother` (4/4) | HELD (diagonal-apply chain absorbed below RE1 leg). |
| RE8 | `L3/fold_solve`, `L3/krylov-step` (2/2) | HELD — **the D2 target** (L3-iteration-view feature column discharges it). |

RE3 (`L2/gram`)/RE4 (`L2/incremental-least-squares`) remain in the demand-gated / edge-untyped buckets, NOT
the STRONGER subset at this snapshot (unchanged; RE3 gated on `deflate`/NLEPS item-4a).

**The 7 STRONGER members NOT in any ratified RE** — `L1-L0/amr-estimate-mark-refine`, `L1/dorfler_mark`,
`L1/flux_recovery_estimate`, `L1/libceed-quadrature-kernel-impl`, `L2/correction_step`, `L3/eigsolve-impl`,
`L3/lanczos_step`. These are **exactly** the c121/c122-new firm + roadmap_goal nodes that reach the feature roots
ONLY via `reference`-class edges (combinator-primary specialization-notes, `realizes-kernel-api`, kernel-impl
`folds`). This is the c122-finalize headline: NOT new garbage, NOT new RE candidates, NOT a rank violation —
the systematic artifact of correct modelling under the depends-on-only GC. **Do NOT ratify these as new REs**
(that is the meta's scheme call, not the planner's); they are the evidence corpus for the batch-39-meta adjudication.

**RE-recheck conclusion:** the ratified RE set holds; no RE auto-discharged this cycle by c123's slate
(consolidation+hygiene, not new consumers). **D2 (the L3-iteration-view column) is the one slate item that
FIRES an RE promotion condition** — it is the "future faithful feature column composing the L3 iteration-rotation
form by name" that both RE2 and RE8 name as their discharge trigger. Re-check RE2/RE8 on the landed tree at the
c123 finalize; the batch-39 meta ratifies the discharged set + adjudicates the reference-edge-liveness scheme.

## Deliverable-presence verification (paste-inline evidence per dispatch)

**D1 — `L1/amr-estimate-mark-intro.md` group-intro authoring + re-nest + index header rename.** OPEN.
- File existence: `ls book/src/L1/amr-estimate-mark-intro.md` → **No such file or directory** (the intro page is absent).
- Maturity: both verbs FIRM on disk (`flux_recovery_estimate.md` `rank: firm`; `dorfler_mark.md` `rank: firm`) — so the "Rough-in" group header is now stale.
- L1/index.md state: line 208 dep-map TABLE header still reads `**Rough-in (AMR estimate/mark vocabulary)**` (verbs marked firm in rows — header lags). (Line 134 narrative cohort header already says "Firm" — a SECOND, separate header; the dep-map TABLE header at :208 is what's stale.)
- SUMMARY state: lines 245-246 are the FLAT fallback (`- [dorfler_mark](./L1/dorfler_mark.md)` / `- [flux_recovery_estimate](...)`), NOT yet a nested grouping.
- OQ-ledger grep: `amr-estimate-mark-group-intro-needs-authoring` is OPEN (no RESOLVED/CLOSED match).
- Structural block: NONE — straight navigational follow-up (the new-SUMMARY-kind-grouping group-intro-stub discipline, friction `new-summary-kind-grouping-placeholder-link-duplicate-file-build-break` GO-codified).

**D2 — L3-iteration-view feature column (Krylov-iteration infrastructure column).** OPEN by construction (new column).
- File existence: `ls book/src/feature/krylov* book/src/feature/*iteration*` → **NONE** (no such column exists).
- Substrate firmness (the BY-NAME constituents): `L3/krylov-step` `firmness: firm`; `L3/fold_solve` `firmness: partial-obstruction` (rankable kind ~2, faithful); `L3/orthogonalize` `rank: partial-obstruction`; `L3/eigsolve-impl`/`L3/lanczos_step` roadmap_goal (referenced, not blocking).
- OQ-ledger grep: no `krylov-iteration`/`L3-iteration-view` RESOLVED match (item-4b is OPEN; RE2/RE8 name this exact discharge trigger).
- Structural block: NONE — DIRECTIVE-2 item-4b explicitly LIFTS this (the L3 iteration-views need a feature column composing the iteration-rotation form BY NAME). A composition-root links DOWN via `reference` (root→node, OWN-COMPOSITION carries liveness).

**D3 — correction_step wider replace-and-propagate (same-layer-cross-cutter).** OPEN.
- Target-state: `grep -c correction_step book/src/L1/multigrid-relaxation-smoother.md` → **0**; `grep -c correction_step book/src/feature/geometric-multigrid-preconditioner.L1.md` → **0** (neither expresses its per-sweep body through the combinator yet).
- No L1 distrelaxation chapter exists (`ls book/src/L1/*distrelax*` → not found); distributive relaxation lives inside `multigrid-relaxation-smoother`.
- OQ-ledger grep: `correction-step-wider-replace-and-propagate-set-l1-and-feature-column` OPEN (the c122-D3 harvester explicitly ROUTED confirmation to the c123 same-layer-cross-cutter).
- Structural block: NONE — audit/observation dispatch; the c121 miner's read (L1 gates keep closure, L2 unfoldings + V-cycle body use the combinator) is the hypothesis to confirm-or-record-why-not.

**D4 — `concepts/RefinementData.md` record-definition page + re-point.** OPEN.
- File existence: `ls book/src/concepts/RefinementData.md` → **ABSENT**.
- ≥2-consumer bar: `RefinementData`/`RefineConfig`/`update_fraction` named by `L1/dorfler_mark.md` (θ field) + `L1-L0/amr-estimate-mark-refine.md` (inline single-consumer `RefineConfig` §Record-definition) + the lifecycle column — ≥2 consumers → `concepts/<record>.md` page warranted.
- OQ-ledger grep: `record-RefinementData-needs-concept-definition-home` OPEN.
- Structural block: NONE — the record-definition obligation (≥2 consumers); cheap honesty pick.

ALL FOUR open. None on the STOP-PROPOSING negative list (`lu_solve`/`back_solve`/… L3-backfill cohort — N/A).
Framing: D1/D2/D4 are layer-intro-author composition/navigation (correct routing); D3 is audit-first
(same-layer-cross-cutter — confirm-the-propagation-reached-all-consumers, the correct framing for a cross-cutting
replace-and-propagate question per the c036 audit-first precedent).

## Dispatches

- **D1 (`layer-intro-author`, MEDIUM-HIGH, WAVE-1) — `amr-estimate-mark-group-intro` (the deferred c122 AMR navigational hygiene).**
  Author `book/src/L1/amr-estimate-mark-intro.md` as a navigational-container by-kind group intro (`kind: navigational-container (group intro)`, NO `rank:`, a one-line orientation + `reference` edges to the two members `L1/flux_recovery_estimate` + `L1/dorfler_mark` — the `fe-space-intro.md` / `mesh-construction-intro.md` format precedent). Then convert the two FLAT `SUMMARY.md` entries (lines ~245-246) into a nested `AMR estimate / mark` grouping under the intro (placed after `Mesh & FE-space construction` / `FE-space sub-spine`, or wherever the AMR group files). Then RENAME the `book/src/L1/index.md` dep-map TABLE group header `**Rough-in (AMR estimate/mark vocabulary)**` (line ~208) → drop "Rough-in" (both verbs firm). GATE: `cargo make book` EXIT 0 + linkcheck2 clean (the group-intro-stub-in-the-same-landing discipline avoids the duplicate-file break). **fan-out: MEDIUM-HIGH** (one coordinated navigational follow-up; closes OQ `amr-estimate-mark-group-intro-needs-authoring`). Plan-tag `amr-estimate-mark-refine`.

- **D2 (`layer-intro-author`, HIGH, WAVE-1) — the L3-iteration-view feature column (Krylov-iteration infrastructure column; DIRECTIVE-2 item-4b; discharges RE2/RE8).**
  Author a new **infrastructure / shared-substrate feature column** (the 4th sub-kind, alongside `feature/infrastructure.md`'s GMG — read that group-intro for the precedent) — slug `feature/krylov-iteration.{L4,L1}` (canonical slug; the planner's working name — the author may refine to e.g. `feature/krylov-iteration-spine` if cleaner, STATE the chosen slug in the report) — that explains the **Krylov / Arnoldi iteration spine** as a composition root and COMPOSES the L3 **iteration-rotation form BY NAME**: `L3/krylov-step` (firm), `L3/fold_solve` (partial-obstruction), `L3/orthogonalize` (partial-obstruction), referencing `L3/eigsolve-impl` + `L3/lanczos_step` (roadmap_goal constituents). This is the "future faithful feature column composing the L3 iteration-rotation form by name" that RE2 (`L3/orthogonalize`) and RE8 (`L3/krylov-step`, `L3/fold_solve`) name as their EXACT discharge trigger — grounding them as a reachable feature-root's composed constituents (root→node `reference` edges carry liveness under OWN-COMPOSITION; the column is itself a `feature_root`). Clean-gate: compose only on-disk firm/rankable substrate (verify-present, paste-inline-evidence); the column is composition, not new operator algebra. Single-machine-valid. NOTE the reference-edge-liveness scheme caveat: the column reaches its L3 constituents via composition/`reference` edges (same shape as GMG) — STATE in the report that this is the faithful RE2/RE8-discharge route AND that it adds to the reference-edge-liveness evidence corpus for the batch-39 meta. **fan-out: HIGH** (the highest-fan-out residual-RE discharge; grounds the L3 iteration-rotation spine; couples to the c121 eigsolve-impl). Plan-tag `re-discharge-tail`.

- **D3 (`same-layer-cross-cutter`, MEDIUM, WAVE-1) — `correction-step-wider-propagate` (confirm the replace-and-propagate reached all consumers).**
  Confirm the wider `correction_step` replace-and-propagate set the c122-D3 harvester ROUTED here: does the **L1 `multigrid-relaxation-smoother`**, the **GMG V-cycle feature column** (`feature/geometric-multigrid-preconditioner.L1.md`), and the **distributive-relaxation L1 form** (inside `multigrid-relaxation-smoother`) express the per-sweep body THROUGH `correction_step` (link DOWN to the combinator) — OR record WHY the L1 gate keeps its closure form (the c121 miner's read: L1 gates keep the closure, L2 unfoldings + the V-cycle body use the combinator). One observation: confirm-propagation-or-record-the-closure-rationale. This is the replace-and-propagate (NOT mine-and-strand) integrity check on the firm `L2/correction_step` combinator. AUDIT-first framing (cross-cutting consumer-completeness question). **fan-out: MEDIUM** (combinator-integrity; closes OQ `correction-step-wider-replace-and-propagate-set-l1-and-feature-column`). Plan-tag `constructive-spine-kernels`.

- **D4 (`layer-intro-author`, LOW-MEDIUM, WAVE-1) — `RefinementData` record-definition concepts-page (cheap honesty pick; AMR record obligation).**
  Author `book/src/concepts/RefinementData.md` defining the AMR refinement config record (≥2-consumer bar fired: `dorfler_mark` θ field + the `amr-estimate-mark-refine` theme's inline `RefineConfig` + the lifecycle column) — all fields (`tol`/`max_it`/`max_size`/`max_nc_levels`/`nonconformal`/`update_fraction`/…) + each field's construction-vs-run-time stratum + the L0 home of the backing C++ struct (`palace/utils/configfile.hpp:97-119`, field `update_fraction` default 0.7) + the `refinement.*` IoData surface. Re-point the theme's inline §Record-definition + `dorfler_mark`/`flux_recovery_estimate` θ references to the concept page (back-link). Define the data shape (NOT operator algebra). **fan-out: LOW-MEDIUM** (record-definition obligation; closes OQ `record-RefinementData-needs-concept-definition-home`). Plan-tag `amr-estimate-mark-refine`.

## Overlap analysis

- **D1 ↔ D2**: BOTH touch `book/src/SUMMARY.md` but in **disjoint regions** — D1 edits the L1-chapters block (lines ~245-246, AMR fallback → nested AMR grouping); D2 appends to the feature Part block (the `# Feature surfaces` region near line 54, the Infrastructure grouping). Disjoint anchors, parallel-safe (the c121/c122 finalizes confirmed multiple disjoint SUMMARY touches integrate clean via per-report on-disk re-read). D1 creates `L1/amr-estimate-mark-intro.md` + edits `L1/index.md`; D2 creates `feature/krylov-iteration.{L4,L1}.md` + edits `feature/index.md` (+ possibly `feature/infrastructure.md` if it co-files under the same infra grouping). **No shared file region.** PARALLEL.
- **D1 ↔ D3**: D3 is observation-only on `L1/multigrid-relaxation-smoother.md` + `feature/geometric-multigrid-preconditioner.L1.md` (it may propose link-DOWN edits to those, OR record the closure rationale). D1 touches AMR files + SUMMARY/index. **Disjoint.** PARALLEL.
- **D1 ↔ D4**: BOTH are AMR-cohort, but **disjoint files** — D1 touches the intro + SUMMARY + `L1/index.md` AMR table header; D4 touches `concepts/RefinementData.md` (new) + the theme `L1-L0/amr-estimate-mark-refine.md` + the verb θ refs in `L1/dorfler_mark.md`/`L1/flux_recovery_estimate.md`. D1 does NOT edit the verb files (only the intro/SUMMARY/index); D4 does NOT edit the index AMR-table-header line or the SUMMARY AMR block. **No shared region.** PARALLEL.
- **D2 ↔ D3**: D2 creates the new krylov-iteration column (composes `L3/krylov-step`/`L3/fold_solve`/`L3/orthogonalize`); D3 observes/edits the GMG column + `multigrid-relaxation-smoother` (correction_step propagation). Different feature columns, different L3 op set. **Disjoint.** PARALLEL.
- **D2 ↔ D4**, **D3 ↔ D4**: fully disjoint (krylov-iteration column / GMG-smoother vs AMR record page). PARALLEL.
- **Consolidated-tally / shared-index:** D2 is the ONLY dispatch touching `feature/index.md` this cycle (its matrix + any Infrastructure-grouping count) → sole-owner, no parallel-blind divergence. D1 is the ONLY dispatch touching the `L1/index.md` AMR dep-map header. No ≥2-parallel-into-one-consolidated-count situation arises. No dual-registration partition needed (each dispatch owns its own distinct rows/page).

## Sequencing schedule

**ONE wave (all parallel):** D1, D2, D3, D4. No forward-reference dependency among them (D2's new column does not reference D1's AMR intro; D4's record page does not block on D1/D2). No same-file overlap. The four touch disjoint file regions; SUMMARY co-touches (D1 L1-block / D2 feature-block) are disjoint-region and parallel-safe by the conflict-tolerance philosophy. ONE `integrator-finalize` at cycle end (rebuild + commit + push + the batch-39-meta-feeding housekeeping).

## Open questions / caveats

- **The reference-edge-liveness scheme question is the batch-39-meta headline — c123 surfaces MORE evidence for it, deliberately.** D2 (the L3-iteration-view column) grounds RE2/RE8 via composition/`reference` edges (root→node, OWN-COMPOSITION) — the SAME edge shape that the GMG column / combinator-primary / DIRECTIVE-3 models use, and the same shape the depends-on-only GC does not traverse. So D2's landing will (a) faithfully discharge RE2/RE8 under the OWN-COMPOSITION liveness rule, but (b) under the *current* depends-on-only GC, the newly-composed L3 views may stay `[GARBAGE*]` (reference-only-reachable) — adding `L3/krylov-step`/`L3/fold_solve`/`L3/orthogonalize` to the reference-only-reachable corpus. **This is intentional evidence-gathering:** it shows the scheme question is not confined to the c122 kernel-impl/combinator cohort but extends to the RE-discharge mechanism itself (a faithful RE discharge produces reference-only-reachable firm nodes). The batch-39 meta should weigh this when adjudicating (e.g. a `reference`-to-reachable-node liveness rule would make D2's discharge show up as `reachable`; the current GC will keep it STRONGER). The D2 author MUST state this explicitly in the report so the meta has the per-node attribution.
- **My read on whether c123 should surface more reference-edge-liveness evidence: YES, and D2 does so by construction.** The cheapest highest-value RE-discharge available (RE2/RE8 via the L3-iteration-view column, item-4b, the c122-planner-flagged highest-fan-out residual) HAPPENS to be the exact mechanism that produces reference-only-reachable nodes — so dispatching it both advances the lift-through campaign AND hands the meta a clean second data class (RE-discharge-produced reference-only nodes, distinct from the c122 kernel-impl/combinator class). No separate evidence-only dispatch is warranted (a plateau-probe-style observation-only dispatch would duplicate what the linter already shows on disk + what this plan's RE-recheck already enumerates).
- **D2 slug coordination:** the canonical working slug is `feature/krylov-iteration.{L4,L1}` (stated in BOTH the D2 scope and here). No sibling dispatch forward-references it this cycle (D1/D3/D4 do not link to the new column), so no cross-report forward-reference slug-divergence risk. The author may refine the slug if a cleaner name surfaces — must STATE the chosen slug in the report for the integrator.
- **The L3-iteration-view column vs the DIRECTIVE-2 item-4b framing:** item-4b says "the L3 iteration-views (RE2 orthogonalize, RE8 fold_solve/krylov-step) need a feature column composing the iteration-rotation form BY NAME." D2 is precisely that. It is the LEAD residual-RE discharge; if the author finds the composition CANNOT be cleanly stated in existing shared vocabulary (the solver-as-low-priority-test-load gate), that is itself a spine finding — land it as a `roadmap_goal` column with the obstruction recorded, NOT a forced firm claim. (The substrate is firm/partial-obstruction on disk, so a clean composition is expected, but the clean-gate governs.)
- **No methodology-adjustment pattern warrants a fresh friction-ledger entry mid-batch beyond the already-flagged reference-edge-liveness scheme question** (which the c122 finalize + this plan both route to the batch-39 meta). The carried linter-maintenance ask-class items (`--show-stronger` per-node attribution especially — it would make THIS plan's manual STRONGER-decomposition automatic) are re-evaluable as GO-candidates at the batch-39 meta now that the project is in forward-build posture.
