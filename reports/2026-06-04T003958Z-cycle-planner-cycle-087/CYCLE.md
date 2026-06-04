---
agent: cycle-planner
invoked_at: 2026-06-04T003958Z
scope: cycle-087 dispatch plan
status: pending
---

# Cycle 087 dispatch plan

## Goals selected this cycle

Cycle-087 is the **THIRD and LAST primary cycle of meta-batch-27** (cycles 085/086/087; the batch-27 meta-phase fires AFTER this cycle's finalize, aggregating 085/086/087). **Land-clean discipline applies** — a small, clean cycle that leaves the tree in good shape for the meta-phase to aggregate, NOT a heavy structural wave or a speculative pull-up.

The single highest-value land-clean item is a **maturity-reference drift-guard pass**: cycle-086 promoted the L4 combinator `solve_family` `rough-in (test-coverage-bounded)` → **firm** (now `firmness: firm` on disk), correcting 5 files, but the c086 grep-sweep was scoped to the L4-operator/feature-driver files and **left a coherent residue of stale `solve_family` `rough-in (test-coverage-bounded)` references across 5 OTHER files** — including a **load-bearing internal inconsistency** in `book/src/L4/index.md` (the now-firm `solve_family` is listed in BOTH the firm cohort `:71` AND the "Rough-in at L4" cohort `:57`/`:59`, with a stale `(1 + 1 test-coverage-bounded)` count header that contradicts the on-disk `L4_rough_in_test_coverage_bounded: 0`). The c086 integrator-signals tail explicitly flagged exactly this as the c087 land-clean candidate ("audit for any remaining stale `solve_family rough-in (test-coverage-bounded)` references outside the 5 files this cycle touched"). This is a textbook `lifter` re-anchor (re-anchor stale maturity references to firmed-up vocabulary) — ONE dispatch, ZERO new files, ZERO status/count change to any operator, and it removes a genuine contradiction the meta-phase would otherwise inherit.

Deliberately a **single-dispatch cycle**: the standing forward frontier is genuinely foundation-gated (the remaining stay-seed columns all converge on the `matrix-weighted-norm` √-cascade, which is NO-GO-HELD and is a **meta-phase re-weigh decision, explicitly forbidden as a c087 land-clean pick**); the in-scope firm-on-positive-structure route is exhausted on the 2 reduce verbs + the solve-family combinator; no feature column qualifies for a flip; 5-driver→L4 is AFFIRMED-COMPLETE. Manufacturing a second dispatch would violate land-clean discipline.

## Dispatches

### D1 — (`lifter`, solve_family-firmed-stale-maturity-reanchor, deps: none)

**scope:** Re-anchor the residual stale `solve_family` `rough-in (test-coverage-bounded)` maturity references that the c086 firm promotion left behind, across the 5 files c086 did NOT touch. `solve_family` is **firm on disk** (`book/src/L4/solve_family.md:4` `firmness: firm`; promoted c086 D1 via the firm-on-positive-structure / syntactic-identity escape). Re-anchor each stale reference to the now-firm maturity, preserving each site's surrounding argument. The genuinely-stale set (triaged on-disk — see §Deliverable-presence verification for the keep/fix triage):

1. **`book/src/L4/index.md`** — THE load-bearing fix (`solve_family` is double-listed across contradictory cohorts):
   - **`:57`** the "**Rough-in at L4 (1 + 1 test-coverage-bounded)**" cohort header — the count is now `(1)` (only `domain_energy_reduce` remains rough-in; `L4_rough_in: 1`, `L4_rough_in_test_coverage_bounded: 0` per the c086 `counts_after`). Drop the "+ 1 test-coverage-bounded" and drop the in-line "plus the fixed-operator family-map combinator `solve_family` (`rough-in (test-coverage-bounded)`)" clause.
   - **`:59`** REMOVE the `- [`solve_family`](./solve_family.md) *(rough-in (test-coverage-bounded))* — ...` bullet from the Rough-in cohort entirely (it is already correctly present in the firm/active-frontier cohort at `:71` as `*(firm; cycle-086 D1)*` — keeping both is the duplicate-listing inconsistency).
   - **`:122`** the dep-map TABLE status cell `| `rough-in (test-coverage-bounded)` (harvested cycle-055 D1; ... promotion = dedicated family-map test OR strawman-derivation pass ...)` → re-anchor to `firm` (cite c086 D1, the firm-on-positive-structure escape, `palace/linalg/ksp.cpp:297-310`), matching the firm-cohort narration at `:71`.
2. **`book/src/L4/frequency_sweep.md`** — the contrast-prose treating `solve_family` as the rough-in sibling:
   - **`:69`** "This is the named `per-element` value that the `solve_family` `rough-in (test-coverage-bounded)` entry records as out-of-scope and batch-17-gated" → the out-of-scope/batch-17-gating is unchanged, but `solve_family` is now firm; re-narrate so the contrast is "the firm `solve_family` entry records `per-element` as out-of-scope".
   - **`:506`** the `(Contrast [`solve_family`], which is `rough-in (test-coverage-bounded)` because its load-bearing claim ... is test-unconfirmed ...)` contrast block — `solve_family`'s independence claim was DISCHARGED c086 (read off the const `BaseKspSolver::Mult` body); re-narrate the contrast (frequency_sweep stays firm for the *fresh-operator-per-member* reason; the historical contrast that `solve_family` was rough-in is now a "was rough-in, firmed c086" or simply drop the now-equal-maturity contrast — lifter judgment, preserve the *fresh-vs-reused-operator* distinction which is the load-bearing point).
3. **`book/src/L4-L3/solve-family-map-dissolution.md`** — the LHS-caveat prose (the theme itself is firm and STAYS firm; only its narration of the now-moot LHS caveat is stale):
   - **`:134`** "lowers an already-authored L4 combinator ([`solve_family`], firm-structure cycle-055 D1, status `rough-in (test-coverage-bounded)`)" → "status `firm` (c086)".
   - **`:140`** the §Verified-against bullet describing `solve_family`'s §Status as carrying "the `rough-in (test-coverage-bounded)` caveat this theme's §Status reasons about" → re-anchor to firm.
   - **`:187`** the "On the inherited LHS test-coverage caveat" reasoning paragraph — this paragraph EXPLICITLY PREDICTED its own resolution ("should a batch-17 lowering-verifier pass confirm the `KspSolver`-reuse carries no cross-element state (promoting the LHS cap to `firm`), this theme is unaffected — it is already firm on structure"). That promotion LANDED (c086). Re-narrate from "the LHS is rough-in, but this theme is firm anyway" to "the LHS firmed c086 exactly as anticipated; this theme was already firm on structure and is unaffected" — PRESERVE the firm-on-structure reasoning (it is load-bearing and still correct), update the LHS-maturity premise.
4. **`book/src/feature/index.md:68`** — "[`electrostatic`] + [`magnetostatic`] — own `solve_family` + own `gram_reduce` are `rough-in (test-coverage-bounded)`" → `solve_family` is firm; the own-constituent gate is now `gram_reduce` ONLY. Re-narrate to "own `gram_reduce` is `rough-in (test-coverage-bounded)` (`solve_family` firmed c086)". This is the c086-grep-sweep MISS (the feature-Part index is a different index than the L4 files c086 corrected).
5. **`book/src/L4/fe_assemble.md:171`** — the contrast-prose "This is distinct from `solve_family`'s `rough-in (test-coverage-bounded)`: `solve_family`'s laws encode an *independence claim* ... that integration-level-only coverage leaves test-unconfirmed" → the `solve_family` independence claim was DISCHARGED c086 (the firm-on-positive-structure escape applied to it too, via the const `BaseKspSolver::Mult` read-off). Re-narrate the contrast: `fe_assemble`'s independence is a positive structural fact (unchanged); `solve_family`'s independence was *also* ultimately discharged on positive structure (c086) — the contrast that `solve_family` was once test-bounded becomes historical. PRESERVE `fe_assemble`'s own firm-on-positive-structure reasoning (the load-bearing point); update the now-equal-maturity sibling reference.

**DO-NOT-TOUCH (triaged NOT-stale — leave exactly as-is):** the 5 files c086 already corrected and any line that already narrates the firm promotion correctly — specifically `book/src/L4/solve_family.md:150,154` (the promotion-narration in the firmed file itself); `book/src/L4/index.md:32,47,71` (the firm-cohort / active-frontier entries already say `*(firm; cycle-086 D1)*`); `book/src/feature/electrostatic.L4.md:56` + `book/src/feature/magnetostatic.L4.md:56` (these correctly say `solve_family` is "now **firm** (c086)" and the `rough-in (test-coverage-bounded)` on those lines refers to `gram_reduce`, NOT `solve_family`).

**rationale:** Drift-guard hygiene flagged directly by the c086 integrator-signals tail (the named c087 land-clean confirm-grep candidate). Removes a load-bearing internal inconsistency (`solve_family` double-listed in contradictory L4/index cohorts + a stale rough-in count header contradicting the on-disk count) so the batch-27 meta-phase inherits a clean, self-consistent tree. ZERO new files, ZERO operator status/count change, ZERO SUMMARY change — pure re-anchor of maturity prose to the firmed-on-disk `solve_family`. Friction `floor-landing-implies-same-cycle-adjacent-entry-reanchor` (the cross-cycle analog: a firm-promotion's adjacent-entry re-anchors that a one-operator-per-dispatch promotion cycle deferred). Serves the c086 integrator-signals §Suggested-next-dispatches land-clean recommendation + the §Standing land-clean discipline.

## Deliverable-presence verification

Per the MANDATORY pre-dispatch four-step check (paste-inline-evidence). D1 is a **hygiene/re-anchor** dispatch (not a new-artifact-slug landing), but its targets are named file paths under `book/src/`, so the check applies to confirm the stale references are genuinely-present-on-disk (the work is open) AND the subject is genuinely firm (the re-anchor target is correct).

**STEP 1 — file existence (all targets present):**
```
book/src/L4/index.md EXISTS 92276b
book/src/L4/frequency_sweep.md EXISTS 43814b
book/src/L4-L3/solve-family-map-dissolution.md EXISTS 35786b
book/src/feature/index.md EXISTS (grep-confirmed line :68)
book/src/L4/fe_assemble.md EXISTS (grep-confirmed line :171)
book/src/L4/solve_family.md EXISTS 40776b  (the re-anchor SUBJECT)
```

**STEP 2 — maturity of the re-anchor subject `solve_family` (confirms the re-anchor TARGET = firm; confirms the work is open because the references still say rough-in):**
```
$ grep -n "^firmness:" book/src/L4/solve_family.md
4:firmness: firm
```
`solve_family` is **firm on disk** (promoted c086 D1). Every reference in D1's stale-set still asserts `rough-in (test-coverage-bounded)` → the re-anchor is genuinely-open work, and the target maturity (`firm`) is confirmed.

**STEP 2b — the stale references are present on disk (exhaustive sweep, triaged):**
```
$ grep -rln "solve_family" book/src/ | <co-occurrence-with-rough-in filter>
### book/src/L4-L3/solve-family-map-dissolution.md   lines 134, 140, 187   [STALE → fix]
### book/src/feature/electrostatic.L4.md   line 56   [NOT stale: refers to gram_reduce; says solve_family "now firm" → KEEP]
### book/src/feature/index.md   line 68   [STALE → fix]
### book/src/feature/magnetostatic.L4.md   line 56   [NOT stale: refers to gram_reduce; says solve_family "now firm" → KEEP]
### book/src/L4/fe_assemble.md   line 171   [STALE → fix]
### book/src/L4/frequency_sweep.md   lines 69, 506   [STALE → fix]
### book/src/L4/index.md   lines 32, 47, 57, 59, 71, 122   [:57/:59/:122 STALE → fix; :32/:47/:71 correctly-firm → KEEP]
### book/src/L4/solve_family.md   lines 150, 154   [NOT stale: the promotion-narration in the firmed file itself → KEEP]
```
Triage confirms exactly **5 files** with genuinely-stale references; the keep/fix split is recorded in D1's scope (DO-NOT-TOUCH list).

**STEP 3 — OQ-ledger RESOLVED-grep (confirm no closed-already item; confirm this is fresh hygiene, not a stale plan line):**
```
$ grep -niE "solve.family.*(RESOLVED|CLOSED|firm.*c086|stale)" scaffolding/open-questions.md
(matches: the batch-26 unify header narrating prior closures + the c086-opened `solve-family-firmed-discharges-one-of-two-electrostatic-magnetostatic-column-gates` (OPEN, a meta-phase column-gate decision — NOT this hygiene item) + `solve-family-md-stale-evidence-provenance-lines-after-firm-promotion` ANSWERED-CLOSED c086 by D2 — that was the INTRA-solve_family.md §Evidence/§Provenance cleanup, a DIFFERENT scope than these 5 cross-file references)
```
No closed-already OQ covers the 5-file cross-reference residue. The c086-closed `solve-family-md-stale-evidence-provenance-lines` was scoped to `solve_family.md`'s own §Evidence/§Provenance lines (already done); the c087 residue is the references in OTHER files. Genuinely-open.

**STEP 4 — structural-block check:** None. The re-anchor target (`solve_family` = firm) is on disk; no methodology gate blocks correcting a stale maturity reference to a firmed operator. (Contrast: the stay-seed feature columns ARE structurally blocked by the `matrix-weighted-norm` √-cascade NO-GO-HELD — but those are NOT in D1's scope; D1 does not touch any `status: seed` token.)

**Verdict: D1 PASSES all four checks. Open, correctly-targeted, structurally-unblocked.**

## Overlap analysis

Single dispatch (D1). No intra-cycle overlap possible. D1 touches 5 distinct files; within `book/src/L4/index.md` it edits the rough-in cohort (`:57`/`:59`), the dep-map cell (`:122`) — all describing the same subject, authored by one owner, so no internal write-conflict. No other dispatch this cycle, so no shared-index / shared-tally / cross-report-forward-reference coordination is needed (the single-index-owner, dual-registration-partition, and canonical-slug guards are all N/A at N=1).

## Sequencing schedule

**Wave 1 (only wave):** D1 (`lifter`). Then the standard post-dispatch pipeline: critic (D1) → repairer (if warn/fail) → `integrator-per-report` (×1, applies D1) → ONE `integrator-finalize` (rebuild book + commit + push + cycle-end housekeeping; the batch-27 meta-phase fires AFTER this finalize as a SEPARATE dispatch).

## Open questions / caveats

- **For the batch-27 meta-phase (drift-pattern signal, NOT actionable this cycle):** the c087 stale-reference residue (5 files) is the **adjacent-entry re-anchor that a firm-promotion cycle deferred** — the same shape as the codified `floor-landing-implies-same-cycle-adjacent-entry-reanchor` friction, but for an L4-operator FIRM-promotion (c086) rather than an L_n-floor landing. The c086 dispatch's stale-ref grep-sweep was scoped to the L4-operator + feature-driver files and **missed `book/src/feature/index.md` and the `L4-L3/` dissolution-theme + `frequency_sweep.md`/`fe_assemble.md` contrast-prose**. The meta-phase may consider whether the firm-promotion dispatch scope should carry a **mandatory whole-`book/src/` cross-reference grep** (not just the operator's own file + immediate consumers) as a coupled same-cycle re-anchor, to avoid the next firm-promotion leaving a similar residue. This is a candidate methodology-tightening for the meta-phase to weigh — surfaced here per the cadence note (the friction-ledger entry would not yet exist).
- **NOT dispatched, confirmed meta-phase-owned (per the task brief + on-disk OQ verification):** the `matrix-weighted-norm` √-cascade re-weigh (NO-GO-HELD; the convergent foundation-blocker now gating 5 of 6 stay-seed columns via `gram_reduce`/`domain_energy_reduce`); the `feature-column-firm-token-choice-batch-27-meta-phase` token convention; the `solve-family-firmed-discharges-one-of-two-...-gates` 1-of-2 column-gate disposition; the `waveguide-mode-output-product-column` demand-gated 6th column; the `electrostatic-magnetostatic-stay-seed-overrides-priorities-1-expectation` priorities.md reconciliation. All five are OPEN OQs explicitly tagged "for the batch-27 meta-phase" on disk (`scaffolding/open-questions.md:1107,1108,1109,1119,1127`) — they are exactly what the meta-phase aggregates, NOT c087 dispatch work.
- **No second dispatch:** the forward frontier is genuinely foundation-gated this cycle (every remaining lever is either the NO-GO-HELD √-cascade or a meta-phase decision), so a second dispatch would either re-propose forbidden/gated work or manufacture a rectangular pull-up (redirect-forbidden). Land-clean discipline ⇒ the single clean hygiene dispatch is the correct and complete plan.
