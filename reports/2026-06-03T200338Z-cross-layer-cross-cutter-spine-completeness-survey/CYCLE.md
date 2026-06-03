---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-03T20:11:22Z
scope: full-stack ↔ feature-spine cross-cut — batch-26 spine-completeness survey (the LEAD, D1)
status: pending
integrated_at: 2026-06-03T203730Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied via integrator-per-report (staging row 2, cycle-082). OBSERVATION-ONLY — NO book/ mutation. CONFIRMED 5-driver→L4 completeness (all 5 drivers + boundary-mode + lifecycle reach L4 on both assemble + solve halves; columns sit at seed ONLY because stage-3 output-product reductions are rough-in/seed). Appended 5 survey-conclusion OQs into the cycle-082 resolution-marker subsection (incl. spine-completeness-survey-5-driver-l4-confirmed-batch-26 AFFIRMED-CLOSED + two (D) stale-pointer findings routed to the batch-26 meta-phase). retroactive-budget 0."
---

# CYCLE: Cross-layer observation — batch-26 spine-completeness survey (5-driver→L4 confirmed; ranked A/B/C/D map)

## Summary

I surveyed the full layer stack (L4 / L4-L3 / L3 / L3-L2 / L2 / L2-L1 / L1 / L1-L0)
and all feature-surface columns (`book/src/feature/*`) against the cycle-082 planner's
state-reading that **5-driver→L4 backend-lowering is largely COMPLETE**. The headline
finding: **that claim holds rigorously.** All five solver pipelines (electrostatic /
magnetostatic / eigenmode / driven / transient) reach L4 on **BOTH** the assemble-half
(every column composes the firm `fe_assemble` fold) **AND** the solve-half (each column
composes a firm solve combinator: `solve_family` for the fixed-operator pair,
`frequency_sweep` for driven, `fold_solve` for transient, the firm `eigsolve` black-box
for eigenmode) — plus the 6th `BoundaryModeSolver` driver column and the spine-ROOT
`lifecycle` meta-feature are on disk and compose firm combinators. **There is NO genuine
(A) gap on the solve-side or assemble-side of any of the 5 (+1) drivers.** The genuinely-open
forward-frontier is no longer in the *driver composition shells* — it is in the
**output-product reduction verbs** (the stage-3 reductions every driver feeds into), all four
of which are `rough-in` and gated on **L1-primitive-firmness + dedicated test coverage**, not
on any missing L4 composition. The deliverable's ranked (A)/(B)/(C)/(D) classification below
is the load-bearing output (the planner scoped this to de-risk c083/c084). I also confirm
the planner's caught (D) stale pointer (`orthogonalize-composition-lowering-l2-l1-theme`)
and found a second.

## Observation kind

**Coverage gap survey (the spine-completeness audit)** — a structured cross-layer
classification rather than a single point-observation. Per the dispatch's explicit framing
(the batch-26-framing survey), the deliverable is the ranked (A)/(B)/(C)/(D) map; the ONE
primary observation is: **the 5-driver→L4 picture is complete on the driver-composition axis;
the remaining frontier is the output-product-reduction-verb cohort + a small set of
trigger-gated foundation backfills, with two stale ledger pointers as cheap hygiene.**

## Specific finding

### 5-driver→L4 completeness verification (the core audit)

Both halves of all 5 drivers verified against the on-disk feature columns + their composed
L4 combinator statuses:

| Driver | Assemble-half (→L4) | Solve-half (→L4) | Reaches L4? |
|---|---|---|---|
| electrostatic | `fe_assemble` (firm), single-term ∇ | `solve_family` (rough-in tc) fixed-op, `ksp_solve` (firm) | YES — `feature/electrostatic.L4.md` |
| magnetostatic | `fe_assemble` (firm), single-term ∇× | `solve_family` (rough-in tc) fixed-op, `ksp_solve` (firm) | YES — `feature/magnetostatic.L4.md` |
| eigenmode | `fe_assemble` (firm) ×3 (K/C/M pencil) | `eigsolve` (firm) black-box, ONE call | YES — `feature/eigenmode.L4.md` |
| driven | `fe_assemble` (firm) ×3 fixed basis | `frequency_sweep` (firm) + `assemble_frequency_operator` (firm) + `ksp_solve` (firm) | YES — `feature/driven.L4.md` |
| transient | `fe_assemble` (firm) ×3 (K/C/M) | `fold_solve` (firm) state-march | YES — `feature/transient.L4.md` |
| (boundary-mode) | `fe_assemble` (firm) GEP block-pencil | `eigsolve` (firm) black-box, ONE call | YES — `feature/boundary-mode.L4.md` |
| (lifecycle ROOT) | — (mesh scaffold) | `fold_solve` (firm) state-generated AMR fold + driver dispatch | YES — `feature/lifecycle.L4.md` |

**Conclusion: the 5-driver→L4 claim is CONFIRMED.** Every driver's assemble-half and
solve-half composes a firm (or firm-structure rough-in-tc) L4 combinator. The columns sit at
`status: seed` NOT because any solve/assemble piece is missing, but because their stage-3
**output-product reduction** is itself `seed`/`rough-in` (a column promotes past `seed` only
once ALL composed constituents are firm). This is the load-bearing reframe for batch-26: the
driver-composition spine is done; the frontier moved down into the reduction verbs and their
L1 primitives.

### (A) — Genuinely-open, cleanly-describable pull-ups (the batch-26 forward-frontier, fan-out-ranked)

These are real, cleanly-describable-in-existing-vocabulary candidates with downstream fan-out.
ALL of them are in the **output-product-reduction-verb cohort** (NOT the driver shells):

**A1 (HIGHEST fan-out) — `sparameter_reduce` promotion (`L4/sparameter_reduce.md`, rough-in → firm).**
Gate-b (the per-port projection needs a firm L1 home) was **DISCHARGED c077** by the firm L1
`port_projection` entry (the `verified_against` block records `port_projection.md:1-354` verdict
`supports`, "the former Status gate-2 is resolved"). The ONLY remaining gate is **gate-a:
test-coverage of the assembly fold** — the existing `test/unit/test-postoperator.cpp:188-271`
idempotency test witnesses the reduction OUTPUT invariant but does NOT call `MeasureSParameter`,
so the fold itself is test-coverage-bounded. Fan-out: HIGH — `sparameter_reduce` is the driven
column's stage-3 (the S-parameters output product); promoting it promotes the driven column's
last non-firm constituent. **Candidate follow-up: a `lowering-verifier` deepen-audit (already
has a rich `verified_against` block) OR a harvester pass IF a `MeasureSParameter`-entry-point
test materializes (out of write-scope; the gate is honestly bounded).**

**A2 (HIGH fan-out) — `eigenfreq_qfactor_reduce` promotion (`L4/eigenfreq_qfactor_reduce.md`, rough-in → firm).**
Gate-(a) (both folded scalar-map building blocks need firm L1 homes) is **DISCHARGED**: the
eigenvalue un-transform → firm L1 `eigenvalue-untransform` (c080); the κ-participation half →
firm L1 `participation_ratio` (c077). The ONLY remaining gate is **gate-(b): the eigenpair→(f,Q)
ASSEMBLY map is test-output-asserted but the assembly itself is not CHECK-asserted** (the
idempotency test populates `cache.freq`/`cache.eigenmode_Q` but does not assert the assembly).
Fan-out: HIGH — this is the eigenmode + boundary-mode columns' stage-3 (the two black-box-eigen
drivers' shared output product). **Candidate follow-up: lowering-verifier deepen-audit; the
structure is firm-on-positive-structure, the gate is test-bounded (honestly out of write-scope
absent a dedicated assembly-map test).**

**A3 (MEDIUM-HIGH fan-out) — `gram_reduce` promotion (`L4/gram_reduce.md`, rough-in-tc → firm).**
`gram_reduce` is rough-in BECAUSE its folded L1 constituents are: the diagonal
`matrix-weighted-norm` radicand (rough-in-tc, see C1) + the off-diagonal `bilinear-form`.
Fan-out: MEDIUM-HIGH — it is the SHARED reduction for BOTH electrostatic (capacitance, `w=1`)
AND magnetostatic (inductance, `w=1/IᵢIⱼ`) columns' stage-3. Its promotion is **downstream of**
the `matrix-weighted-norm` √-entry-point trigger (C1) + `bilinear-form` firming — i.e. it is a
foundation-gated pull-up, not independently cleanly-describable-to-firm yet. **Candidate
follow-up: gated behind C1; recommend tracking, not dispatching ahead of the L1 floor.**

**A4 (MEDIUM fan-out) — `domain_energy_reduce` promotion (`L4/domain_energy_reduce.md`, rough-in → firm).**
The energy-fields output product (the 5th output-product column, driver-agnostic). Rough-in with
a test-gate (§Status point 2). Fan-out: MEDIUM — it is the energy-fields output-product column's
verb; cross-driver but a measurement-output product rather than a primary matrix product.
**Candidate follow-up: lowering-verifier or harvester per its own test-gate; lower-priority than
A1/A2.**

**Net (A) read:** the batch-26 forward-frontier is the **output-product-reduction-verb cohort**
(`sparameter_reduce` > `eigenfreq_qfactor_reduce` > `gram_reduce` > `domain_energy_reduce`), all
`rough-in`, all gated on **test-coverage** (A1/A2/A4) or **L1-primitive-firmness** (A3) — NOT on
any missing L4 composition. Two of the four (A1, A2) have ALREADY had their structural/L1-home
gates discharged this batch (c077/c080) and now stand ONLY on test-coverage gates that are
honestly out of project write-scope (no `MeasureSParameter`/assembly-map entry-point test exists).
This is the load-bearing finding: **the "remaining work" is largely test-coverage-bounded
promotion, not new authoring.** c083/c084 should weigh whether a lowering-verifier deepen-audit
can raise law-confidence to the `ksp_solve`-equivalent literature-anchor bar (the documented
alternate promotion route) rather than waiting on tests that may never be in scope.

### (B) — Deliberate absorptions / NO-FLOOR-by-warrant (CONFIRMED not gaps — do NOT re-propose)

Verified each of these IS a correct deliberate disposition, so c083/c084 do not re-propose them:

- **FE-construction inputs (`fe_space` / `fe_collection` / `essential_dofs`) absorbed into
  `L4/fe_assemble.md` readonly stratum.** CONFIRMED at `L4/fe_assemble.md:69, 147, 174`: the three
  are "absorbed into this `FiniteElementSpace[N]` readonly construction stratum … none shape the
  fold, so none gets a standalone thin chapter (the combinator-as-entry default)." All three have
  firm L1 entries (`fe_space`/`fe_collection`/`essential_dofs` all `status: firm`). **NOT a gap** —
  they are firm at L1 and correctly absorbed (not stranded) at L4. The FE-construction cohort is
  absorbed-by-design, exactly as the planner's state-reading said.
- **`weak_form_term` NO-L2-by-warrant.** CONFIRMED `L1/weak_form_term.md` firm (c061);
  `L1-L0/weak-form-term-rotation.md` firm; the §Status (`:325`) records "No new theme is warranted
  — the term is a strict sub-component of the already-firm" assemble cohort. **NOT a gap.**
- **`solve_family` NO-ENTRY warrant (no standalone `L3/solve_family`).** CONFIRMED
  `L4/solve_family.md:10, 131` (cycle-057 D1 NO-ENTRY warrant): the family loop carries no
  sequential-obstruction, so the L4>L3 dissolution theme's §"L3 form (RHS)" IS the authoritative
  L3-form home; a separate L3 chapter would mirror it (anti-mirror principle). **NOT a gap.**
- **`fold_solve` L3-ENTRY (the CONTRAST case — correctly DOES have an L3 entry).** CONFIRMED
  `L4/fold_solve.md:146`: `L3/fold_solve` IS warranted (`partial-obstruction`) because its loop
  carries BOTH a carry-threading sequential-obstruction AND an opaque-library per-step body. This
  is the correct asymmetry vs `solve_family` — **NOT a gap; the division of labor is recorded and
  resolved** (OQ `fold-solve-l3-entry-vs-dissolution-home` resolved c059).
- **`eigsolve` / `assemble_term` / `time_step_op` black-box-kernel leaves rise as opaque-surface
  inputs.** CONFIRMED (the `black-box-vs-accelerated-kernels` case-1 disposition, `fe_assemble.md`
  §Status). The opaque-library per-step / per-term / eigen-iteration leaves are correctly
  positively-reframed at L4 (not stranded obstructions). **NOT gaps.**
- **Transient per-step `ksp_solve` NOT exposed as a column cap.** CONFIRMED
  `feature/transient.L4.md:42`: the implicit solve is inside the opaque MFEM integrator step, not
  a user-visible map element. Correct absorption — **NOT a gap.**

### (C) — Trigger-gated items (trigger-firing status checked)

- **C1 — `matrix-weighted-norm` √-entry-point cascade (trigger NOT fully fired).**
  `L1/matrix-weighted-norm.md` is `rough-in (test-coverage-bounded)`. Gate (a) (direct test of the
  `Norml2(comm,x,B,Bx)` √-overload entry point) is **PARTIALLY ADVANCED c080** — the new
  `test/unit/test-domainpostoperator.cpp:75-93` covers the SPD-weighted **radicand** `⟨E, M_elec E⟩`
  (the squared self-bilinear of law 8) + the `½` energy scaling, discharging the
  radicand-constituent half — but **does NOT discharge the gate**: the energy form returns `0.5*dot`
  with NO `√` and never routes through `Norml2`, so the outer `√` at the named entry point remains
  test-uncovered. **Trigger: PARTIALLY fired (radicand half), NOT fully fired (√ entry point).**
  This cascade gates A3 (`gram_reduce` diagonal). **Status: standing gate, advanced-not-discharged.**
- **C2 — record-definition ≥2-consumer promote-watches.** The record-definition obligation (config
  records, `OpParams`/`SimState`/`StepOutputs`/`PrevCarry` L4 records, etc.) — I did not find a
  fired ≥2-consumer trigger requiring a new cross-cutting `concepts/<record>.md` page this batch;
  the existing concept pages (`op-params`, `sim-state`, `step-outputs`, `prev-carry`, `config-record`,
  `solve-result`, `solve-monad`) cover the L4 record cohort. **Status: no new trigger fired; watch
  continues.** (Note: a fuller record-definition-coverage audit is its own scope; flagged as OQ.)
- **C3 — boundary-mode ↔ waveguide-mode output-product gate.** CONFIRMED NOT fired:
  `feature/boundary-mode.L4.md:59, 75, 79` — the per-mode readout reduction into the user-facing
  waveguide-mode product is a **forward-ref with NO dedicated output-product column yet** ("no
  output-product column yet"). This is the ONE reason boundary-mode stays `seed`. **Trigger: NOT
  fired — a waveguide-mode output-product column (paralleling the 5 existing output-product columns)
  is a genuine LOW-MEDIUM-fan-out (A)-adjacent candidate IF a downstream consumer demands it.**
  Recommend recording as a gated candidate, not dispatching ahead of demand (the output-product
  spine is otherwise complete at 5 columns; a 6th waveguide-mode column is demand-gated).

### (D) — Closed-but-stale-pointer items (cheap hygiene; meta-phase ledger-unification inputs)

- **D1 (planner-caught, CONFIRMED) — `orthogonalize-composition-lowering-l2-l1-theme` OQ is stale.**
  `scaffolding/open-questions.md` (the `### orthogonalize L2 composition family` section) still
  states: "the `L2-L1/orthogonalize-composition-lowering` theme is **not yet authored** (abstractor)
  … Referenced as plain text in the firm L2 entry (the chapter does not yet exist…)." **This is
  STALE:** the file `book/src/L2-L1/orthogonalize-composition-lowering.md` EXISTS on disk, is a full
  firm theme (carries a `## Status` section at `:359`, a `verified_against`-style audit, and the
  three-way-delegation-boundary content). Planner says FIRM since c022. **Disposition: meta-phase
  unify-pass — close this OQ sub-item + the sibling `L2-layer-intro-refresh-for-named-compositions`
  sub-item (which references the same now-landed work) to the Closed index.**

- **D2 (NEWLY found) — the same `### orthogonalize L2 composition family` block contains a SECOND
  stale sub-item: `L2-layer-intro-refresh-for-named-compositions`.** It says the L2 `index.md`
  Working Notes "state the cycle-005 firm-up did not introduce a new L2 entry for `orthogonalize`…
  that remains a candidate" and "that note is now stale and the dep-map row has flipped stub→firm …
  flagging for a refresh." Given the L2 `orthogonalize` entry has been firm since c019 and the
  L2-L1 theme firm since c022, this refresh-flag has been actionable for ~60 cycles without
  migration — it is exactly the "lingering in intake without a plan item" defect the CLAUDE.md
  intake→plan invariant warns about. **Disposition: meta-phase — either migrate to the plan as a
  one-touch `layer-intro-author` L2-index Working-Notes refresh, OR (if already refreshed on disk)
  close to the Closed index.** (I did not read `L2/index.md` Working Notes line-by-line this
  dispatch to confirm whether the on-disk note is itself already updated — flagged as a verify-first
  caveat below.)

## Recommendation

1. **De-risk c083/c084 with this map.** The driver-composition spine is COMPLETE (5+1 drivers reach
   L4 both halves); c083/c084 should NOT re-open driver-shell work and should NOT re-propose the (B)
   absorptions. The forward-frontier is the (A) output-product-reduction-verb cohort.
2. **Highest-fan-out (A) follow-up candidates for `priorities.md` / lowering-verifier:** `sparameter_reduce`
   (A1, gate-b discharged c077, only test-bounded gate-a remains) and `eigenfreq_qfactor_reduce`
   (A2, gate-a discharged c077/c080, only test-bounded gate-b remains) — both stand ONLY on
   test-coverage gates that are honestly out of project write-scope. **Recommend a `lowering-verifier`
   deepen-audit on each to test whether the literature-anchor / law-completeness promotion route can
   raise them to firm without the (unavailable) entry-point tests** — this is the cheapest path to
   promoting the driven + eigenmode/boundary-mode columns past `seed`.
3. **A3 (`gram_reduce`) is foundation-gated behind C1** (`matrix-weighted-norm` √-entry-point) — do
   NOT dispatch ahead of the L1 floor; track it.
4. **(D) stale pointers → meta-phase ledger-unification inputs.** Close D1 + D2 (the whole
   `### orthogonalize L2 composition family` block is now largely landed-work residue) at the next
   meta-phase unify-pass. Cheap hygiene; prevents re-proposal.
5. **C3 (waveguide-mode output-product column)** — record as a demand-gated candidate, not a
   dispatched item.

## Supporting evidence

- 5-driver L4 columns (all read this dispatch): `book/src/feature/electrostatic.L4.md`,
  `magnetostatic.L4.md`, `eigenmode.L4.md`, `driven.L4.md`, `transient.L4.md`, plus
  `boundary-mode.L4.md` and `lifecycle.L4.md`.
- Firm solve/assemble combinators: `book/src/L4/fe_assemble.md` (firm; §Status, the
  fe_space/fe_collection/essential_dofs absorption at `:69, 147, 174`), `solve_family.md`
  (NO-ENTRY warrant `:10, 131`), `fold_solve.md` (L3-ENTRY contrast `:146`), `frequency_sweep.md`,
  `assemble_frequency_operator.md`, `eigsolve.md`, `ksp_solve.md`.
- Output-product reduce verbs (the (A) frontier): `book/src/L4/sparameter_reduce.md` (`firmness:
  rough-in`; `verified_against` block records gate-b discharged by firm L1 `port_projection`
  c077, gate-a test-coverage-bounded), `eigenfreq_qfactor_reduce.md` (`rough-in`; §Status gate-a
  DISCHARGED c080, gate-b test-open at `:198-210`), `gram_reduce.md` (`rough-in (test-coverage-bounded)`;
  §Status "primitives are rough-in" at `:247`), `domain_energy_reduce.md` (`rough-in`).
- Firm L1 primitives that discharged reduce-verb gates: `book/src/L1/port_projection.md` (firm c077),
  `participation_ratio.md` (firm c077), `eigenvalue-untransform.md` (firm c080).
- C1 trigger: `book/src/L1/matrix-weighted-norm.md:108-115` (`rough-in (test-coverage-bounded)`;
  gate-a partially advanced c080 via `test-domainpostoperator.cpp:75-93`, √-entry-point still open).
- (B) absorption warrants: `book/src/L1/weak_form_term.md:325`, the firm `fe_space`/`fe_collection`/
  `essential_dofs` L1 entries.
- (D) stale pointers: `scaffolding/open-questions.md` `### orthogonalize L2 composition family`
  block (sub-items `orthogonalize-composition-lowering-l2-l1-theme` and
  `L2-layer-intro-refresh-for-named-compositions`), vs the on-disk firm
  `book/src/L2-L1/orthogonalize-composition-lowering.md` (`## Status` at `:359`).

## Open questions / caveats

- `spine-completeness-survey-5-driver-l4-confirmed-batch-26` (this dispatch) — RECORD: the
  5-driver→L4 backend-lowering claim is verified COMPLETE on both the assemble-half and solve-half
  of all 5 (+boundary-mode +lifecycle) columns; the remaining frontier is the output-product-reduction
  -verb cohort (`sparameter_reduce` / `eigenfreq_qfactor_reduce` / `gram_reduce` / `domain_energy_reduce`),
  all rough-in and gated on test-coverage (A1/A2/A4) or L1-primitive-firmness (A3), NOT on missing L4
  composition. *Trigger:* the c083/c084 planner consumes this as the batch-26 frontier shape.
- `output-product-reduce-verb-test-coverage-bounded-promotion-route` (this dispatch) — A1
  (`sparameter_reduce`) and A2 (`eigenfreq_qfactor_reduce`) have had their structural/L1-home gates
  discharged (c077/c080) and now stand ONLY on test-coverage gates that appear out of project
  write-scope (no `MeasureSParameter`-entry-point / eigenpair→(f,Q)-assembly-map test exists). Open
  question for c083/c084: can a `lowering-verifier` law-completeness / literature-anchor deepen-audit
  raise these to firm via the documented alternate route (the `ksp_solve`-equivalent
  literature-anchor bar) rather than waiting on tests? *Trigger:* a lowering-verifier deepen-audit
  dispatch on either verb.
- `orthogonalize-l2-composition-family-oq-block-stale-landed-work` (this dispatch) — the whole
  `### orthogonalize L2 composition family` OQ block in `open-questions.md` is largely
  landed-work residue: `orthogonalize-composition-lowering-l2-l1-theme` (theme FIRM on disk since
  c022) and `L2-layer-intro-refresh-for-named-compositions` (the L2 entry firm since c019) are both
  stale "not yet authored" / "candidate for future" pointers. *Trigger:* meta-phase unify-pass —
  close both to the Closed index. *Caveat:* I did not line-read `L2/index.md` Working Notes this
  dispatch to confirm whether the on-disk Working-Notes prose D2 references is itself already
  refreshed; verify before closing D2 (the OQ pointer is stale regardless of the on-disk note state).
- `waveguide-mode-output-product-column-demand-gated` (this dispatch) — boundary-mode's stage-3
  readout reduction has NO dedicated output-product column (the only one of the driver columns
  lacking one; the other 5 drivers feed capacitance/inductance/sparameters/eigenfreq-qfactor/
  energy-fields). A 6th waveguide-mode output-product column is a genuine but demand-gated (A)-adjacent
  candidate. *Trigger:* a downstream consumer of the waveguide-mode product, OR an output-product
  spine-completion size-judgment dispatch.
- `record-definition-coverage-audit-not-performed-this-dispatch` (this dispatch, caveat) — I did
  NOT perform a full record-definition ≥2-consumer coverage audit (it is its own scope); I confirmed
  the existing L4 record concept-page cohort covers the named L4 records but did not exhaustively
  cross-check every signature-named record against a definition home. *Trigger:* a dedicated
  record-definition-coverage cross-cut, IF the meta-phase wants the C2 watch closed rather than
  carried.
