---
agent: cycle-planner
invoked_at: 2026-06-03T21:33:10Z
scope: cycle-084 dispatch plan (batch-26 position 3/3 — the LAST primary cycle before the batch-26 meta-phase)
status: pending
integrated_at: 2026-06-03T214250Z
integration_commit: 9b9d27d
integration_notes: |
  cycle-084 dispatch plan (the planner report). Consumed at finalize. The plan scheduled ONE small
  lifter hygiene dispatch (land-clean discipline for the last pre-meta cycle); the co-owned
  scaffolding/priorities.md plan write committed atomically. No artifact mutation by the planner.
---

# Cycle 084 dispatch plan

## Goals selected this cycle

**This is an honestly LIGHT, land-clean final cycle: ONE small `lifter` hygiene dispatch.** The
in-scope forward frontier is genuinely thin and the substantive work is meta-phase-reserved, so the
right move is NOT to manufacture work. The state-reading (verified inline below, not asserted):

- **5-driver→L4 is COMPLETE / AFFIRMED-CLOSED** (c082 D1 survey) — do NOT re-open driver-shell /
  driver-composition work, and do NOT re-propose the (B) deliberate absorptions (FE-construction
  inputs absorbed into `fe_assemble` readonly; `weak_form_term` NO-L2; `solve_family` NO-ENTRY).
- **The in-scope reduce-verb law-confidence route is EXHAUSTED** for the two all-primitives-firm
  verbs: A1 `sparameter_reduce` (firm c083) + A2 `eigenfreq_qfactor_reduce` (firm c082). The
  remaining A3 `gram_reduce` + A4 `domain_energy_reduce` are **foundation-gated behind the
  `matrix-weighted-norm` √-entry-point cascade the batch-25 meta-phase NO-GO'd** — NOT cleanly
  promotable this cycle, and NOT to be triggered without an explicit meta-phase go.
- **The highest-priority pending item — the USER DIRECTIVE `feature-column-promotion-break-the-seed-deadlock`
  — is RESERVED for the batch-26 meta-phase** (it edits CLAUDE.md + `layer-intro-author` → session
  restart; the all-13-column re-evaluation is the batch-27 lead). I do NOT enact it or touch any
  column status/promotion prose this cycle.
- **The orthogonalize-family (D) stale pointers + the ledger-unification are meta-phase-reserved** —
  I do NOT pre-empt them.
- **No deferred/contingent OQ trigger has fired** (all are gated on NLEPS, deterministic-reduction
  solver variants, downstream consumers, or specific lowering-verifier passes — none of which fired).

What IS genuinely-open, cheap, NOT meta-phase-reserved, and NOT a near-no-op: **three stale
sibling-verb maturity descriptions inside `book/src/L4/domain_energy_reduce.md`** that still call the
now-firm `eigenfreq_qfactor_reduce` (firm c082) "rough-in" — one of which (line 290) is not merely
stale-wording but **factually misleading about the gating logic** ("also `rough-in` for the same
… reasons" — but A2 promoted firm *because* its primitives all firmed, whereas A4's gate is its own
folded `matrix-weighted-norm` being rough-in; the "same reasons" claim is now false). This is the
chapter the meta-phase will read when it weighs the A3/A4 cascade question, so correcting it de-risks
that read. D1 (`lifter`) takes exactly that fix and nothing else.

**Explicitly NOT planned (and why):**
- An A4 `domain_energy_reduce` deepen-audit (a candidate the dispatch brief flagged) is a **near-no-op
  this cycle** and is SKIPPED: the verb is correctly `rough-in` because its folded `matrix-weighted-norm`
  energy form is itself `rough-in (test-coverage-bounded)` — "a reduction is as firm as its least-firm
  folded primitive." The firm-on-positive-structure law-confidence escape (which promoted A1/A2)
  CANNOT apply while a folded primitive is non-firm, so a deepen-audit would only re-confirm the
  already-recorded double-gate (the `matrix-weighted-norm` √-entry-point cascade [NO-GO] + the
  per-domain test). The honest gate is already recorded in the verb's §Status (verified inline below);
  re-confirming it is busywork. The A3/A4 cascade weigh is correctly routed to the meta-phase.

## Dispatches

**D1 — `lifter` — `domain_energy_reduce` stale sibling-verb maturity-word hygiene (single-file, build-relevant, LOW fan-out).**
- **scope:** In `book/src/L4/domain_energy_reduce.md` ONLY, correct the three references that describe
  the now-**firm** sibling reduce verb `eigenfreq_qfactor_reduce` (promoted firm cycle-082) — and the
  closely-coupled comparison to `sparameter_reduce` (firm cycle-083) — as if they were still `rough-in`:
  - `:212` — "`(rough-in)`" parenthetical on the `eigenfreq_qfactor_reduce` reduce-family-member bullet → re-token to `(firm, c082)`.
  - `:290` — "(Contrast the per-mode sibling `eigenfreq_qfactor_reduce`, **also `rough-in` for the same
    primitive-maturity + no-dedicated-test reasons**.)" → this is the LOAD-BEARING correction: it is now
    factually wrong. `eigenfreq_qfactor_reduce` is firm (c082) **precisely because** both its folded
    primitives (`participation_ratio` c077 + `eigenvalue-untransform` c080) firmed and the
    firm-on-positive-structure law-confidence escape then applied. A4 `domain_energy_reduce` stays
    `rough-in` for a DIFFERENT reason — its folded `matrix-weighted-norm` energy form is itself
    `rough-in (test-coverage-bounded)` (gated on the √-entry-point cascade), so the escape cannot apply.
    Re-narrate the contrast to state this correctly (the per-mode sibling is now firm; this per-domain
    verb stays rough-in because its folded energy-form primitive is not yet firm — the asymmetry IS the
    point).
  - `:354` — the §"Sibling-combinator grounding" bullet naming `eigenfreq_qfactor_reduce` "(the per-MODE
    rank-1 scalar-table sibling)" — verify whether it carries a stale rough-in qualifier; if so, sync to
    firm; if it is a pure structural-shape reference (no maturity word), leave it.
  - `:32` / `:298` — the `sparameter_reduce` references are scope/shape comparisons ("single-witness-driven-by-design
    scope"), NOT maturity claims — verify and leave unless a stale rough-in qualifier is attached.
- **deps:** none.
- **rationale:** Pure drift-guard / factual-correctness hygiene on a single chapter body. The verb's
  OWN status stays `rough-in` (untouched — its double-gate is real and correctly recorded). This is
  NOT a column promotion (meta-phase-reserved), NOT the orthogonalize family (meta-phase-reserved),
  NOT a ledger-unification (meta-phase-reserved), NOT triggering the `matrix-weighted-norm` cascade.
  It corrects stale sibling-maturity prose in the exact chapter the batch-26 meta-phase will read when
  it weighs the A3/A4 foundation-gate question — so it removes a misleading "same reasons" framing
  before that read. Serves: land-clean discipline for the final batch-26 cycle; the c082 survey's (D)
  cheap-hygiene class (this is the in-chapter analog of the eigenmode.L4 sync c083 D2 already did for
  the sibling driver column); friction-ledger drift-guard.

## Overlap analysis

Single dispatch — no pairs to analyze. D1 touches exactly one file (`book/src/L4/domain_energy_reduce.md`),
edits only prose maturity-word references, touches NO shared index / consolidated tally / SUMMARY entry /
frontmatter status token / count line. No parallel-blind-shared-index concern (the parallel-blind guard is
N/A with one dispatch). No forward-reference / cross-report slug coordination (no sibling dispatch). No
floor-landing / adjacent-entry re-anchor coupling (no floor lands). The verb's own `## Status: rough-in`
and `firmness: rough-in` frontmatter are left UNCHANGED (the fix is sibling-maturity-word only).

## Sequencing schedule

**One wave (purely parallel — trivially, a single dispatch):**
- Wave 1: D1.

Pipeline reminder (per role-spec): D1 → critic(D1) → repairer(D1, if needed) → `integrator-per-report` ×1
→ ONE `integrator-finalize` (rebuild book + commit + push + cycle-end housekeeping). The batch-26
META-PHASE fires AFTER this finalize as a SEPARATE dispatch, aggregating cycles 082/083/084.

## Deliverable-presence verification

Four-step check per role-spec, with pasted inline evidence. D1's scope resolves to the named file
`book/src/L4/domain_energy_reduce.md` — the check applies.

**D1 — `book/src/L4/domain_energy_reduce.md`:**

1. **File existence** — `ls -la book/src/L4/domain_energy_reduce.md`:
   ```
   -rw-rw-r-- 1 crutcher crutcher 29681 Jun  3 12:16 book/src/L4/domain_energy_reduce.md
   EXIT=0
   ```
   PRESENT.

2. **Maturity / already-discharged check** — `## Status` line read from disk (`sed -n '266,269p'`):
   ```
   ## Status

   `rough-in`. **Reasoning (warrant-first):** the combinator's **structure** is read directly off the
   positive `MeasureDomainFieldEnergy` per-domain loop (`postoperator.cpp:1021-1099`) — the per-domain map,
   ```
   The verb is `rough-in` — and STAYS rough-in (its double-gate is real). The dispatch is NOT a no-op:
   it corrects stale *sibling*-verb maturity refs, not the verb's own status. Confirmed the two sibling
   verbs the stale refs describe ARE firm on disk:
   ```
   book/src/L4/eigenfreq_qfactor_reduce.md  →  ## Status\n\n`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):**
   book/src/L4/sparameter_reduce.md         →  ## Status\n\n`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):**
   ```
   So `domain_energy_reduce.md:212` "(rough-in)" + `:290` "also `rough-in` for the same … reasons" are
   genuinely stale (eigenfreq_qfactor_reduce is firm c082). NOT a no-op.

3. **OQ-ledger RESOLVED-grep** — `grep -n "domain_energy_reduce.*RESOLVED\|domain_energy_reduce.*CLOSED"
   scaffolding/open-questions.md`: no RESOLVED/CLOSED match for the verb's own promotion. The OQ
   `domain_energy_reduce-promotion-double-gated` is OPEN (the verb correctly stays rough-in). The
   hygiene fix does NOT touch that OQ or the verb status — it touches only sibling-maturity prose, so
   there is no stale-vs-closed conflict. (The c079/c080 `domain_energy_reduce` authoring + distinct-verb
   confirm-probe OQs were closed by the batch-25 meta-phase unify-pass; those are the authoring OQs, not
   the promotion gate.)

4. **Structural-block check** — no methodology gate blocks this fix. It is NOT a promotion of
   `domain_energy_reduce` (its `matrix-weighted-norm` √-entry-point cascade gate + per-domain test gate
   both stand — NO-GO this batch, untouched). It is NOT a feature-column promotion (the
   `feature-column-promotion-break-the-seed-deadlock` directive is meta-phase-reserved — D1 touches an L4
   verb chapter, NOT any `feature/*` column file or status token). It is NOT the orthogonalize-family
   stale pointers (meta-phase-reserved ledger-unification). It is a pure sibling-maturity-word
   correction in a single L4 verb chapter — a legitimate `lifter` drift-guard fix. ALL FOUR CHECKS PASS.

**STOP-PROPOSING negative-list cross-check:** D1's scope (a prose hygiene fix on an existing L4 verb
chapter) does not match any disqualified slug (`lu_solve`, `back_solve`, `ls-update-column`,
`nleps_*`) — those are L3-backfill disqualifications; this is not an L3 backfill.

## Open questions / caveats

- **The in-scope frontier is genuinely thin this cycle — this is reported honestly, not manufactured.**
  The batch-26 substantive work (the column-promotion deadlock-break enactment; the A3/A4
  `matrix-weighted-norm` √-entry-point cascade weigh; the orthogonalize-family + scope-limit
  ledger-unification) is ALL correctly routed to the batch-26 meta-phase, which fires immediately after
  this cycle's finalize. A single clean hygiene dispatch is the appropriate land-clean close.

- **Meta-phase agenda (surfacing for the batch-26 meta-phase, which I do NOT enact):** the three
  highest-priority meta-phase items are already well-wired in the ledger/signals and need no new plan
  candidate from me — (1) `feature-column-promotion-break-the-seed-deadlock` (USER DIRECTIVE, HIGHEST
  PRIORITY; with TWO output-product verbs now firm [`sparameter_reduce` c083, `eigenfreq_qfactor_reduce`
  c082] and their columns STILL `seed` purely on the sibling-blocks-promotion rule, the deadlock is now
  concretely demonstrated — the enactment is overdue and the all-13-column re-evaluation is the natural
  batch-27 lead); (2) the A3/A4 foundation-gate weigh (the in-scope law-confidence route is EXHAUSTED;
  A3 `gram_reduce` + A4 `domain_energy_reduce` need the `matrix-weighted-norm` √-entry-point cascade —
  "dedicate a cascade cycle" vs "leave at sharpened rough-in" recurs batch-25/26); (3) the
  orthogonalize-family (D) stale-pointer ledger-unification (`orthogonalize-composition-lowering-l2-l1-theme`
  OQ says "not yet authored" but the theme is FIRM on disk since c022; `L2-layer-intro-refresh-for-named-compositions`
  actionable ~60 cycles without migration) + the c082 survey's residual scope-limits (no `L2/index.md`
  Working-Notes line-read; no full record-definition ≥2-consumer coverage audit).

- **Possible meta-phase plan-candidate (NOT a fired trigger; flagged for meta-phase judgment, not
  appended to the plan by me):** the `matrix-weighted-norm` √-entry-point full-firm cascade is now the
  SOLE shared blocker for BOTH remaining reduce verbs (A3 `gram_reduce` AND A4 `domain_energy_reduce`)
  AND for the `capacitance`/`inductance`/`energy-fields` output-product columns' eventual full firm.
  The batch-25 meta-phase NO-GO'd it on "no downstream consumer needs it now." That premise is now
  WEAKER (it is the convergent blocker for the entire remaining reduce-verb tail). I am NOT proposing
  to trigger it (it remains a ~30-file own-cycle structural wave, correctly meta-phase-gated) — but the
  batch-26 meta-phase should re-weigh whether the consumer-demand premise still holds, given the A3/A4
  exhaustion finding. This is a re-weigh input, not a dispatch.

- **Cadence note:** if the meta-phase concludes (as the signals suggest) that the in-scope seed-surface
  is at its firming ceiling AND the column-promotion deadlock-break is the only thing that moves the 13
  `seed` columns, then batch-27 will be substantively driven by the deadlock-break enactment +
  column re-evaluation — i.e. the next-batch frontier is the column re-evaluation, not new bottom-up
  vocabulary. Flagging so the meta-phase sets batch-27's lead accordingly.
