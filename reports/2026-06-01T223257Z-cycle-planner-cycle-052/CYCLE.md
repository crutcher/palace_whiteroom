---
agent: cycle-planner
invoked_at: 2026-06-01T223257Z
scope: cycle-052 dispatch plan
status: pending
---

# Cycle 052 dispatch plan

FIRST primary cycle of meta-batch-16 (cycles 052/053/054; the batch-16 meta-phase fires AFTER cycle-054's finalize). The 2026-06-01 VOCABULARY-SHIFT REDIRECT is in force; the batch-15 meta-phase (commit `45ab935`) RATIFIED `collapsed-leaf-disposition-convention-cohort-wide` → **reduce-to-specialization-stub** (information-non-lossy, NOT full-delete) and reshaped the CYCLE-052 active head. NO session restart needed (no agent-def change).

## Goals selected this cycle

**LEAD (redirect item 2a) — complete the refactor pass by enacting the ratified leaf-chapter reduce-to-stub disposition on the 12 fold-family leaf chapters.** This removes the last rectangular residue (the duplicated semantics in the L2/L3 BLAS-1 leaf chapters) while preserving each operator's unique L0 anchors, its variant-axis row, and all live inbound consumer links (`orthogonalize-variant-split`, `L3/nrm2`, the index dep-map rows). With the refactor pass winding down to one bounded sweep, I ALSO schedule **(2b)** the next in-layer combinator-family mine (replace-and-propagate) and **(3)** a strictly-low-priority single-pipeline solver-test-load probe (electrostatic, clean-describability check), neither of which preempts or distorts the spine. 6 dispatches total, well under the 12-cap.

## Deliverable-presence verification

Per the MANDATORY pre-dispatch deliverable-presence procedure (paste-inline-evidence). The lead is **open by ratification** — the convention `collapsed-leaf-disposition-convention-cohort-wide` was RATIFIED at the batch-15 meta-phase (the structural gate that HELD it through c049–c051 is now PASSED), and all 12 leaf chapters are full-bodied on disk (NOT yet stubs), so the reduce-to-stub deliverable is genuinely open. Items 2b/3 are open by construction (a fresh mine of an unsurveyed family; a fresh solver probe with no prior-cycle history).

**Step 1 — file existence + maturity (the 12 lead targets are FULL bodies, NOT stubs):**
```
OK  book/src/L2/scal.md (365 ln)        ## Status: firm
OK  book/src/L2/axpy.md (406 ln)        ## Status: firm
OK  book/src/L2/axpby.md (437 ln)       ## Status: firm
OK  book/src/L2/axpbypcz.md (449 ln)    ## Status: firm
OK  book/src/L2/dot.md (345 ln)         ## Status: firm
OK  book/src/L2/nrm2.md (160 ln)        ## Status: firm
OK  book/src/L3/scal.md (155 ln)        ## Status: firm
OK  book/src/L3/axpy.md (149 ln)        ## Status: firm
OK  book/src/L3/axpby.md (154 ln)       ## Status: firm
OK  book/src/L3/axpbypcz.md (160 ln)    ## Status: firm
OK  book/src/L3/dot.md (162 ln)         ## Status: firm
OK  book/src/L3/nrm2.md (167 ln)        ## Status: firm
```
The L2 `linear_combination`-family leaves carry the heavy duplicated-semantics bodies (345–449 ln — the bulk of the reduction); the L3 leaves were already re-expressed through the L3 combinators at c051 (149–167 ln, lighter reduction). NONE is yet a stub → the reduce-to-stub deliverable is open.

**Step 1b — combinator link targets (live link-up resolves):**
```
OK book/src/L2/linear_combination.md (## Status: firm)
OK book/src/L2/inner_product.md      (## Status: firm)
OK book/src/L3/linear_combination.md (## Status: firm)
OK book/src/L3/inner_product.md      (## Status: firm)
```
All four `[<combinator>](...)` link-up targets exist firm → the stubs' "specialization of [`<combinator>`]" live links resolve.

**Step 1c — unique L0 anchors that the stub MUST retain (verified-unique example, `L2/scal.md`):**
```
vector.cpp:207-211   vector.hpp:262-270   vector.cpp:203-227   vector.hpp:98-99
```
(per the ratified convention clause (b) — a full-delete would LOSE this L0 grounding; the stub preserves it).

**Step 1d — inbound live links that MUST stay live (the reason reduce-to-stub, not delete):**
```
orthogonalize-variant-split.md:134  [`dot`](../L3/dot.md) ... [`axpy`](../L3/axpy.md)
orthogonalize-variant-split.md:259  [`L3/dot`](../L3/dot.md), [`L3/axpy`](../L3/axpy.md); [`L2/dot`](../L2/dot.md),
orthogonalize-variant-split.md:260  [`L2/axpy`](../L2/axpy.md)
L3/nrm2.md:134                       L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) ...
```
Distinct-inbound-file counts (links resolving to L2/L3 leaf targets, self excluded): `scal` 25, `axpy` 22, `dot` 25, `nrm2` 22, `axpby` 13, `axpbypcz` 11. The stubs persist → these all stay live with no re-pointing required (the link target file is unchanged); only dep-map ROW prose + leaf-body reduction is the work.

**Step 2/3 — OQ-ledger RESOLVED/RATIFIED grep (structural gate now PASSED):**
```
priorities.md:150  `collapsed-leaf-disposition-convention-cohort-wide` RATIFIED — REDUCE-TO-SPECIALIZATION-STUB ... (GO; the ONE decision gating batch-16)
open-questions.md:10 (1) `collapsed-leaf-disposition-convention-cohort-wide` RATIFIED ... → migrated to plan CYCLE-052 #1 (`refactor-pass-leaf-chapter-reduce-to-stub`)
```
The convention is RATIFIED + migrated to the plan as the c052 lead → the lead is open (the structural HOLD that blocked it c049–c051 is lifted). All checks pass.

**Step 4 — STOP-PROPOSING NEGATIVE LIST:** none of the 6 dispatch scopes touches `lu_solve` / `back_solve` / `ls-update-column` / the 4 NLEPS atoms / `apply_nonlinear_pencil` (HELD). The combinator-miner family (item 2b, D5) is constrained to the smoother / projector-gate / Krylov-inner-fold candidates — disjoint from the negative list.

## Dispatches

**D1 — `lifter` — L2 `linear_combination`-family leaf reduce-to-stub (`scal`/`axpy`/`axpby`/`axpbypcz`).**
- **scope:** Reduce `book/src/L2/scal.md` + `book/src/L2/axpy.md` + `book/src/L2/axpby.md` + `book/src/L2/axpbypcz.md` (full firm bodies, 365/406/437/449 ln) to **specialization-stubs** per the ratified convention clause: (a) the one-line "`<op>` is the arity-`N` specialization of [`linear_combination`](./linear_combination.md)" with a LIVE link up to the combinator entry + its §"Arity specializations"/§"Specializations" note (`scal` = arity-1, `axpy` = arity-2 second-coeff-fixed-1, `axpby` = arity-2, `axpbypcz` = arity-3); (b) RETAIN each operator's UNIQUE L0 citation anchors + its one variant-axis row (verified-unique per the deliverable-presence evidence — e.g. `L2/scal.md` keeps `vector.hpp:98-99`/`:262-270`/`vector.cpp:207-211`/`:203-227`; carry forward the per-operator output-aliasing/element-type variant row, noting output-aliasing is the FOLD's axis per OQ `arity-family-leaf-floors-output-aliasing-axis-is-the-folds`); (c) DEFER all semantics / algebraic-laws / fusion prose to `linear_combination` — delete the duplicated body. Keep `## Status: firm` (the stub is a firm specialization pointer). Do NOT touch `L2/index.md` dep-map rows or consolidated narrative (D4 owns those). Invoke the `deleted-slug-inbound-live-link-sweep` skill conceptually — but note NO file is deleted here (reduce-to-stub keeps the file), so the inbound links to `../L2/{scal,axpy,axpby,axpbypcz}.md` stay live by construction; verify zero dangling.
- **deps:** none.
- **rationale:** the LEAD `refactor-pass-leaf-chapter-reduce-to-stub`; the heavy-body half (the 4 large L2 chapters carrying the duplicated rectangular semantics the redirect removes). One dispatch owns one combinator-family at one layer → each leaf chapter touched by exactly one dispatch.

**D2 — `lifter` — L3 `linear_combination`-family leaf reduce-to-stub (`scal`/`axpy`/`axpby`/`axpbypcz`).**
- **scope:** Reduce `book/src/L3/scal.md` + `book/src/L3/axpy.md` + `book/src/L3/axpby.md` + `book/src/L3/axpbypcz.md` (149–160 ln; already re-expressed through `L3/linear_combination` at c051, so lighter) to specialization-stubs: (a) one-line "`<op>` is the arity-`N` specialization of [`linear_combination`](./linear_combination.md)" LIVE link up to `book/src/L3/linear_combination.md` + its specializations note; (b) RETAIN each L3 leaf's unique L0 anchors + variant-axis row; (c) DEFER semantics to `L3/linear_combination` (the c051 in-line §"Downward to L2" combinator note is the home — delete the duplicated body). Keep `## Status: firm`. Do NOT touch `L3/index.md` rows/narrative (D4). Reduce-to-stub keeps the files → inbound links (incl. `orthogonalize-variant-split.md:259-260,293` → `../L3/axpy.md`) stay live; verify zero dangling.
- **deps:** none.
- **rationale:** the L3 half of the `linear_combination` family. Disjoint files from D1 → parallel-safe.

**D3 — `lifter` — `inner_product`-family leaf reduce-to-stub, BOTH layers (`dot` specialization-stub + `nrm2` consumer-stub).**
- **scope:** FOUR chapters, two distinct stub kinds (the member/consumer distinction must be applied consistently → one owner): **(i) `dot` specialization-stubs** — reduce `book/src/L2/dot.md` (345 ln) + `book/src/L3/dot.md` (162 ln) to "`dot` is the `M=I` Hermitian/symmetric specialization of [`inner_product`](./inner_product.md)" LIVE link up (to `L2/inner_product.md` / `L3/inner_product.md` respectively) + retain unique L0 anchors + the conjugation variant-axis row + defer semantics. **(ii) `nrm2` consumer-stubs** — reduce `book/src/L2/nrm2.md` (160 ln) + `book/src/L3/nrm2.md` (167 ln) to **consumer-stubs** (the do-NOT-merge carve-out): "`nrm2` is a CONSUMER of [`inner_product`](...) (`√ ∘ abs ∘ inner_product` at `y=x`); see the in-line §Downward consumer note" — NOT "specialization of" (it is not a fold member). RETAIN the load-bearing `std::abs` defensive-guard claim + the `vector.hpp:255-260` Norml2 anchor (preserved at c051; do NOT drop). The `L3/nrm2.md:134` in-line consumer note → `../L2/nrm2.md` stays live by construction. Keep `## Status: firm` on all four. Do NOT touch index rows/narrative (D4). Verify zero dangling after reduction.
- **deps:** none.
- **rationale:** the `inner_product` family. Bundling `dot`+`nrm2` across both layers in ONE dispatch ensures the member-vs-consumer distinction (the `:595` carve-out) is applied uniformly by a single author; disjoint files from D1/D2 → parallel-safe.

**D4 — `layer-intro-author` — SOLE index-owner + count-owner + co-scheduled bounded narrative micro-sweep.**
- **scope:** Owns ALL `book/src/L2/index.md` + `book/src/L3/index.md` consolidated edits this cycle: (i) update the dep-map ROWS for the 12 reduced leaves to reflect their new specialization-stub/consumer-stub status (the row text that described the now-deleted leaf bodies → "specialization-stub of `linear_combination`/`inner_product`" / "consumer-stub of `inner_product`"); (ii) reconcile the consolidated cohort narrative (the §Vocabulary-cohort / fold-cohort prose) to state the leaves are now reduced specialization-stubs under the combinator-as-entry model (the rectangular-floor framing the redirect retires); (iii) the co-scheduled **bounded narrative micro-sweep** (`l2-index-and-operator-chapter-historical-narrative-and-stale-future-tense-micro-sweep` + `linear-combination-home-residual-future-tense-sweep`): the non-build-breaking stale-future-tense / demoted-slug code-spans in `L2/index.md` (≈`:118`/`:121`/`:123` cohort-history prose), `book/src/L3/linear_combination.md` (§Arity-specializations/§Status/§Dependencies/§Evidence residual future-tense), and the `book/src/L3-L2/index.md` cohort bullets — cosmetic, non-blocking. Expect benign OOB `citecheck` warnings on append-only index prose as the leaf bodies shrink (NO-GO on a re-pin convention per the batch-15 meta-phase — non-load-bearing; do NOT chase them).
- **deps:** D1, D2, D3 (the index rows/narrative reconcile what those three landed).
- **rationale:** the count-ownership convention applied tactically (the ONE place ≥2 dispatches' output converges into a shared consolidated index region). D1/D2/D3 author disjoint leaf bodies; D4 sole-owns the two index files so the consolidated narrative is authored once, not three-ways-blind. Completes the refactor pass.

**D5 — `combinator-miner` — `next-in-layer-combinator-family` (redirect item 2b; replace-and-propagate).**
- **scope:** Mine the NEXT in-layer utility combinator family under the replace-and-propagate model (conciseness-driven INWARD mining to simplify a layer — NOT a cross-layer theme, NOT mine-and-strand). Survey the firm L2/L3 surface for a recurrent base-form pattern a combinator would simplify; the candidate families (planner's deliverable-presence survey picks ONE): **(a) the smoother family** — `jacobi-smoother` (`op.dinv ⊙ x`, one elementwise product) + `chebyshev`/`chebyshev-iteration` apply-shape (degree-zero member of the recurrence) — is there a `polynomial-smoother`-shaped apply combinator? (NOTE: `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` was CLOSED-BLOCKED-RETIRED at batch-10 — richardson-as-third-sibling doesn't exist in Palace; the miner must re-confirm or pick a different family, NOT re-propose the retired one); **(b) the projector/gate family** — `divfree-projector` + the deflation projectors (`deflate`); **(c) the Krylov inner-fold.** If a genuine family is found: author the replace-and-propagate map (the combinator is the entry, the members become specialization notes, propagate upward), ENACT the L2-entry inversion if cheap, sequence the propagation. If NO genuine family is found (e.g. (a) re-confirms the retired richardson gap): record the negative finding as a spine-coverage result — do NOT force a combinator. The low-priority `l4-propagation-depth-linear-combination` "flag, don't force" flag rides here.
- **deps:** none (surveys/authors files disjoint from the leaf reductions — `linear_combination`/`inner_product` are settled; the candidate families are smoother/projector/Krylov, untouched by D1–D4).
- **rationale:** redirect program item 2b; the continued shared-spine abstraction. Independent of the leaf sweep → parallel-safe.

**D6 — `harvester`/`cross-layer-cross-cutter` — `solver-test-load-first-probe` (redirect item 3; LOW priority, clean-describability probe).**
- **scope:** Probe the SIMPLEST pipeline — the **electrostatic solver** (`ElectrostaticSolver::Solve`, `palace/drivers/electrostaticsolver.cpp:22`; a single linear solve over a set of terminal boundary conditions, the simplest of the 5 pipelines) — for whether its top-level shape is **cleanly describable in the existing shared vocabulary** (`ksp_solve` cap + `apply_linop` + the BLAS-1 combinators `linear_combination`/`inner_product` + the FE-assembly primitives `assemble-diagonal` etc.). Localize the driver loop (codemap-first; the entry point `electrostaticsolver.cpp:22` + `PostprocessTerminals` `:100` are pre-anchored). If the top-level solve loop maps cleanly to existing vocabulary → propose a layer entry (the appropriate L_n for the solver step). If it does NOT map cleanly → the gap is a **finding ABOUT the spine** (a missing combinator / a vocabulary the shared spine lacks), recorded as a spine work-item feeding item 2b — do NOT force the spine to fit the solver, do NOT distort/preempt the lead. Observation-first: the value is the spine-coverage finding as much as any landed entry.
- **deps:** none (probes Palace source + reads firm vocabulary; authors nothing that overlaps D1–D5).
- **rationale:** redirect program item 3, strictly low-priority test-load. Begins pulling a solver up the layers per the redirect; never preempts the spine. Independent → parallel-safe. NOTE: `drivers/electrostaticsolver.cpp` is NOT on the dispatch-resilience known-heavy watch-list (it is a driver, not the template-dense `iterative.cpp` running-QR region), so no pre-supplied anchor ranges beyond the two entry points are needed; the probe localizes its own loop.

## Overlap analysis

Pairwise, by artifact region + operator names:

- **D1 ↔ D2:** D1 touches `L2/{scal,axpy,axpby,axpbypcz}.md`; D2 touches `L3/{scal,axpy,axpby,axpbypcz}.md`. Disjoint files, same operator NAMES but different layer entries (different files). NOT overlapping → PARALLEL.
- **D1/D2 ↔ D3:** D3 touches `L2/dot.md`, `L3/dot.md`, `L2/nrm2.md`, `L3/nrm2.md` — disjoint from the `linear_combination`-family files. NOT overlapping → PARALLEL.
- **D1/D2/D3 ↔ D4:** D1/D2/D3 author leaf-chapter BODIES; D4 owns the `L2/index.md` + `L3/index.md` consolidated rows + narrative. The dep-map ROWS are anchor-distinct per leaf (parallel-safe in principle), but the **consolidated cohort narrative + any running tally** is a single shared mutable region → assigned to ONE owner (D4) per the count-ownership convention, AND D4 must read what D1/D2/D3 landed to reconcile the row text. Therefore D4 is SEQUENCED after D1/D2/D3 (wave-2). D1/D2/D3 do NOT touch the index files (stated explicitly in their scopes) → no two-writer.
- **D4 ↔ D5:** D5 (combinator-miner) surveys/authors the smoother/projector/Krylov family files + possibly `L2/<family-combinator>.md`; it does NOT touch `L2/index.md`/`L3/index.md` narrative for the BLAS-1 leaves (different cohort). If D5 lands a new combinator it adds its OWN dep-map row (anchor-distinct, parallel-safe per the distinct-rows convention) — but to be safe under the conflict-tolerance philosophy, mark PARALLEL (a mild index-row co-edit is corrected cheaply by the integrator's merge handling and surfaces as an integrator-signals data point). NOT a genuine same-region overlap → PARALLEL.
- **D5 ↔ D6:** D5 mines the spine (smoother/projector/Krylov); D6 probes the electrostatic driver. D6 may PRODUCE a finding that feeds D5's family choice, but within this cycle they are independent (D6's finding lands as an OQ/spine work-item for a FUTURE cycle's miner, not D5's input). Disjoint files → PARALLEL.
- **D6 ↔ D1/D2/D3/D4:** D6 reads Palace source + firm vocabulary, authors a solver-step entry (a NEW file in a solver-step layer location, or nothing if it records a finding). Disjoint from the leaf chapters + indexes → PARALLEL.

**No two dispatches modify the same operator entry or rewrite the same theme body. The only shared consolidated region (the L2/L3 index narrative) is sole-owned by D4 and sequenced.**

## Sequencing schedule

- **Wave 1 (parallel):** D1, D2, D3, D5, D6.
  - D1/D2/D3 = the 12 leaf-chapter reductions (disjoint files).
  - D5 = the combinator-miner family mine (independent spine work).
  - D6 = the low-priority electrostatic solver probe (independent).
- **Wave 2 (after D1/D2/D3 reports land):** D4 — the `layer-intro-author` index-owner reconciles the `L2/index.md` + `L3/index.md` dep-map rows + consolidated narrative to what D1/D2/D3 landed + runs the co-scheduled bounded narrative micro-sweep. D4 is wave-2 because it must read the three leaf-reduction reports to author the row text correctly.

(Per the cycle-record-keeping note: the book is NOT rebuilt between waves; there is exactly ONE `integrator-finalize` at cycle end. The waves order DISPATCHES by the D4-reads-D1/D2/D3 dependency, not multiple finalizes.)

## What lands c052 vs sequences to c053/c054

- **c052 (this cycle):** the refactor pass COMPLETES — all 12 fold-family leaf chapters reduced to specialization-stubs (D1/D2/D3) + the index reconciliation + micro-sweep (D4). This is the priority and it closes `refactor-pass-leaf-chapter-reduce-to-stub` / `collapsed-leaf-disposition-convention-cohort-wide` / `leaf-chapter-disposition-remains-meta-gated-after-cycle-051-theme-demotion`. PLUS the first `next-in-layer-combinator-family` mine (D5) + the first `solver-test-load-first-probe` (D6).
- **c053/c054 (sequenced):** if D5 finds a genuine family, its full propagation (L3/L4 re-expression + any leaf-as-specialization-note collapse) sequences to c053 (mirroring the c049→c050/c051 `linear_combination`/`inner_product` propagation pattern). If D6 surfaces a spine-coverage gap, that becomes a c053+ spine work-item (a missing combinator feeding D5's successor). The solver test-load continues pipeline-by-pipeline (magnetostatic/eigenmode/driven/transient + FE assembly) across c053/c054 at LOW priority, never preempting the spine.

## Open questions / caveats

- **Items #2/#3 SCHEDULED this cycle (not held for c053).** The lead is only 4 dispatches; with the 12-cap there is ample budget, and items 2b (D5) + 3 (D6) are independent of the leaf sweep (no overlap) so they do not risk the lead. The redirect explicitly sequences 2b + 3 to fill the rest of the frontier after 2a, with 3 strictly low-priority — D6 is observation-first (its value is the spine-coverage finding, so it cannot "fail" expensively or distort the spine). This is the redirect-faithful read of the active head.
- **D5 family choice is the miner's, not pre-fixed.** I list candidates (smoother / projector-gate / Krylov-inner-fold) but the miner picks by its own deliverable-presence survey. I flag the batch-10 `polynomial-smoother-l2-combinator-from-jacobi-and-chebyshev` CLOSED-BLOCKED-RETIRED verdict (richardson-as-third-sibling absent in Palace) so the miner does NOT re-propose it — if the smoother family is chosen, it must find a DIFFERENT shared shape or record the negative finding.
- **Benign OOB citecheck warnings are EXPECTED (D4) and accepted.** The mass leaf-body reduction shrinks files, drifting append-only index-prose line-references (recurrence-2 across c050/c051; the batch-15 meta-phase voted NO-GO on a re-pin convention — non-load-bearing). D4 should NOT chase them; the integrator will note them in signals if any surface.
- **Reduce-to-stub keeps every file → the `deleted-slug-inbound-live-link-sweep` skill is a VERIFICATION gate here, not a de-link sweep.** Unlike c050/c051 (which physically deleted theme files and required de-linking), this cycle DELETES NO file (reduce-to-stub retains the chapter). So the inbound consumer links stay live by construction; D1/D2/D3 invoke the skill only to CONFIRM zero dangling after reducing the bodies (no inbound re-pointing is actually required). This is the lower-risk variant of the multi-deletion convention — flagging it so the producers don't over-engineer a de-link sweep that isn't needed.
- **For the batch-16 meta-phase (fires after c054):** if c052 completes the refactor pass cleanly, the batch-16 frontier is purely items 2b + 3 (shared-spine combinator mining + solver test-load). The strategic-pivot question (continue spine vs. pivot to downstream burn effort) was answered by the redirect (continue spine, solvers as test-load, no pivot yet) — no fresh ASK from this cycle.
