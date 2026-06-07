---
agent: cycle-planner
invoked_at: 2026-06-07T200334Z
scope: cycle-133 dispatch plan
status: pending
---

# Cycle 133 dispatch plan

## Goals selected this cycle

c133 OPENS meta-batch-43 (cycles 133/134/135; batch-43 meta fires after c135 finalize).
The human RESOLVED the §CENTRAL ASK on 2026-06-07, choosing **(C) — OPEN THE DEFERRED
sharding-MATH gate** (over (E) wind-to-maintenance). This FIRES the DIRECTIVE-1
hard-gated door. The §1.2.2 / closure-signature polish pass is COMPLETE end-to-end and
the in-scope FEATURE-SURFACE SPINE is L4-COMPLETE — so the only substantive forward
direction left is the gated sharding-MATH exploration, and it is **GATED-FIRST**: the
LEAD (WAVE-1) is a HARD spine-non-destabilization PROBE that runs BEFORE any lift. Per
the role-spec guidance for a gate whose outcome is not yet known, c133 dispatches the
PROBE as the primary work, bundles 1-2 MAINTENANCE-FLOOR opportunistic hygiene touches,
and **DEFERS WAVE-2's `roadmap_goal` sketch to c134** once the probe verdict is in (no
pre-committing a sketch that depends on an outcome I don't yet have). This keeps the
hard-gate discipline intact: explore whether a non-destabilizing decomposition-abstraction
framing exists, never force one.

## Dispatches

### D1 [LEAD] (`cross-layer-cross-cutter`, WAVE-1) — the sharding-MATH non-destabilization PROBE (audit arm)
- **scope:** `cross-layer audit: sharding-math-non-destabilization-probe`. AUDIT whether the
  **sharding-as-decomposition-abstraction MATH** (domain decomposition / sub-problem
  composition as a *mathematical* abstraction on tensor-field problems — NOT the MPI
  mechanics) can be expressed in the EXISTING L4→L1 spine vocabulary **without
  destabilizing the current abstraction spine.** Deliverable: an audit CYCLE.md (NO book
  mutation — this is a cross-cutter observation report) answering: (a) does a
  *non-destabilizing* decomposition-abstraction framing exist — e.g. a
  tensor-field-restriction / sub-domain-compose combinator that composes EXISTING firm
  vocabulary via `reference`-class edges, leaving every firm node firm and every edge's
  rank/liveness intact? OR (b) would any honest framing require re-rooting/downgrading firm
  spine nodes (→ stays a `roadmap_goal` future-direction note, NOT lifted)? Examine the
  ONE concrete decomposition-math candidate already on file: the Dörfler cross-rank
  threshold-bisection reconciliation (`utils/dorfler.cpp:101-166`, OQ
  `dorfler-cross-rank-bisection-distributed-note-deferred`) — "select a global threshold
  from per-rank local thresholds" is a textbook sub-domain → global reduction; assess
  whether its single-rank-degenerate form (already in the c121 `dorfler_mark` rough-in)
  generalizes to a spine-expressible decomposition-reduce, or whether the generalization
  is purely an MPI-collective concern. **HARD-GATE boundary the audit MUST honor and
  STATE:** MPI/distributed itself stays OUT (`palace/linalg/rap.{cpp,hpp}` `ParOperator`/RAP,
  `palace/utils/geodata.{cpp,hpp}` `Partition`/distribution `:33-41`, the MPI collectives
  — these are NOT lifted; the audit may CITE them as the deferred-future mechanism but
  must NOT propose lifting any as active work). The codemap confirms `linalg/*` carries NO
  Schwarz/domain-decomposition solver primitive — sharding in Palace is purely the
  `Par*`/`Partition` MPI mechanism — so a candidate spine-math framing must come from
  generalizing EXISTING firm tensor-field vocabulary (restriction / extension / partition-
  of-unity / sub-domain reduce composing firm roots BY NAME), not from a Palace source op.
  Verdict format: CLEAR (non-destabilizing framing found, hand to WAVE-2 c134) /
  NO-CLEAR (re-rooting required → record as `roadmap_goal` future note, do NOT lift).
- **deps:** none.
- **rationale:** the LEAD WAVE-1 hard gate (priorities.md batch-43 head, LEAD bullet 1).
  Determines whether (C) yields any liftable math at all. Plan-tag `sharding-math-exploration`.

### D2 (`same-layer-cross-cutter`, WAVE-1) — the probe's spine-stability cross-check (within-layer arm)
- **scope:** `same-layer audit: sharding-math-spine-stability-cross-check`. The
  within-spine complement to D1's cross-layer audit: scan the firm L4/L3/L2 combinator
  cohort for which (if any) firm combinators a decomposition-abstraction would have to
  RE-ROOT vs which it can compose UNCHANGED via `reference`-class edges. Specifically:
  does `domain_energy_reduce` (the existing L4 domain-restricted reduce verb,
  `book/src/L4/domain_energy_reduce.md`) already provide a domain-restriction precedent a
  sub-domain-compose could `reference` BY NAME? Are the firm reduce/fold combinators
  (`gram_reduce`, `inner_product`, `linear_combination`) closed under a partition-of-the-
  index-set restriction without re-rooting? Deliverable: an audit CYCLE.md (NO book
  mutation) enumerating the firm-node stability set: GREEN (composable-by-reference,
  no re-root) vs RED (would force a rank/liveness regression on a firm node). This is the
  data D1's CLEAR/NO-CLEAR verdict rests on. **HARD-GATE:** no proposal that downgrades/
  re-roots a firm node; the graded-stack baseline (`rank_violations=0`, reachable held)
  is the invariant the cross-check protects.
- **deps:** none (parallel with D1 — distinct audit arms, no book mutation).
- **rationale:** splits the probe into the cross-layer (D1) and within-layer (D2) audit
  arms per the LEAD's "route `cross-layer-cross-cutter` / `same-layer-cross-cutter` (the
  audit)" instruction, so the gate verdict has both the upward (does it destabilize the
  stack?) and the lateral (does it re-root any firm combinator?) evidence. Plan-tag
  `sharding-math-exploration`.

### D3 (`cross-layer-cross-cutter`, WAVE-1) — MAINTENANCE FLOOR standing hygiene (RE re-check + kernel-API/impl integrity + semantic-surface liveness)
- **scope:** `cross-layer audit: maintenance-floor-standing-hygiene`. The every-cycle
  standing floor, as a single audit CYCLE.md (NO book mutation unless a one-line stale
  token surfaces): (i) **RE-set re-check** — confirm RE4 stays consumer-gated (no
  GMRES-variant column landed/expected c133) and the RE11 deliberate-reference-only-
  reachable cohort premises HOLD (the §2g escalate-guard — flag if any `detritus`/
  `true_detritus`/`reachable` count moves against the held baseline
  `files=385, typed=324, reachable=163, reference_reachable=247, rank_violations=0,
  true_detritus=50`); (ii) **kernel-API/impl integrity** — confirm the three
  `realizes-kernel-api` edges (`libceed-quadrature-kernel-impl` ↔
  `fe-assemble-libceed-boundary-obstruction`; eigsolve-impl ↔ its API; triangular-solve
  impl ↔ its API) stay `reference`-class on disk, NOT mis-typed as `depends-on`; (iii)
  **semantic-surface liveness** — quick scan of `book/src/semantics/index.md` for any
  stale path/anchor drift (the every-batch GC-sweep analog). Deliverable: a clean-bill
  audit OR a flagged-residual list for the batch-43 meta. NOT a forced-vocabulary frontier.
- **deps:** none (parallel — pure audit, disjoint from D1/D2's sharding focus).
- **rationale:** the MAINTENANCE FLOOR surround (priorities.md batch-43 head, FLOOR item 1
  + the standing gates). Keeps the health signals clean while the gated exploration runs.
  Plan-tag `graded-stack-hygiene`.

## Overlap analysis

Three dispatches, ALL audit-class (NO book mutation in any — cross-cutter / same-layer-
cross-cutter / maintenance-audit all produce observation CYCLE.md reports, not
proposed-changes to book chapters). Pairwise:

- **D1 ↔ D2:** both audit the sharding-MATH question, but DISTINCT arms — D1 is the
  cross-LAYER (vertical: does the stack destabilize?) arm, D2 is the same-LAYER
  (lateral: does any firm combinator re-root?) arm. They share the SUBJECT (sharding-math
  non-destabilization) but write DISJOINT report files and mutate NO shared artifact
  region. Per the conflict-tolerance philosophy (when in doubt, PARALLEL; two reports are
  non-overlapping at the operational level) → **PARALLEL.** Their findings COMPOSE into
  the gate verdict; minor framing overlap is useful corroboration, not conflict.
- **D1 ↔ D3:** disjoint subjects (D1 = sharding-math probe; D3 = RE/kernel/liveness
  hygiene). No shared file region, no shared operator name. → **PARALLEL.**
- **D2 ↔ D3:** disjoint subjects (D2 = firm-combinator stability set; D3 = RE/kernel/
  liveness hygiene). No overlap. → **PARALLEL.**

No consolidated-tally collision (no firm-count moves — all audit-class, no node maturity
changes). No floor-landing → adjacent-entry re-anchor coupling (no floor lands this cycle).
No cross-report forward-reference to a not-yet-existing slug (WAVE-2's sketch slug
`sharding-math-decomposition-abstraction-sketch` is DEFERRED to c134 and is NOT referenced
by any c133 dispatch). The DIRECTIVE-1 OUT-of-scope paths (`linalg/rap.*`,
`utils/geodata.*`, MPI collectives) are CITED-as-deferred-mechanism by D1, never lifted —
no boundary violation.

## Sequencing schedule

**ONE wave (all parallel):** D1 + D2 + D3.

All three are audit-class with no book mutation and no inter-dispatch dependency. WAVE-2
(the `sharding-math-decomposition-abstraction-sketch`, route `abstractor`/
`layer-intro-author`, dep the probe) is **DEFERRED to cycle-134** — it lands ONLY if the
c133 probe (D1+D2) returns CLEAR. Not dispatched this cycle (no pre-committing a sketch
that depends on a verdict not yet in hand).

ONE `integrator-finalize` at cycle end (reports → STAGING → rebuild → commit/push), as
always. The audit reports' findings (gate verdict + hygiene bill) flow to the c134 planner
via `integrator-signals.md` and to the batch-43 meta.

## RE-recheck (batch-43, c133)

NO RE fires this cycle — all three dispatches are audit-class (NO node maturity / rank /
edge change → the graded-stack baseline is HELD BY DESIGN). The live re-check (D3's
explicit job): **RE4** stays consumer-gated (no GMRES-variant driven-solver column c133);
the **RE11** deliberate-reference-only-reachable cohort premises HOLD (the §2g
escalate-guard fires only if a `detritus`/`reachable` count moves against the held
baseline). **DIRECTIVE-1 boundary** is ACTIVELY GUARDED this cycle (the sharding probe is
the LEAD): the MPI-associated version (`linalg/rap.*` `ParOperator`/RAP, `utils/geodata.*`
`Partition`/distribution, MPI collectives) stays OUT — D1 may CITE these as the deferred
mechanism, must NOT propose lifting them; a sketch that re-roots a firm node is REJECTED,
recorded as a `roadmap_goal` future note. **Kernel-API/impl integrity**: the three
`realizes-kernel-api` edges stay `reference`-class (D3 confirms on disk).

## Standing-gate confirmations (pre-dispatch, paste-inline evidence)

**Linter baseline (run at c133 dispatch time — HELD vs c132 finalize):**
```
$ python3 tools/graded-stack-lint/graded_stack_lint.py --json
rank_violations: []            (0 — HELD)
unresolved_depends_on_targets: []   (0 — HELD)
roots: 45                      (HELD)
detritus / true_detritus: 122 / 50  (HELD)
promotion_frontier: 10         (HELD)
```
The HARD-GATE invariant the probe must preserve (`rank_violations=0`, reachable held) is
CONFIRMED clean at dispatch. The exception ledger
(`scaffolding/graded-stack-baseline-exceptions.md`) is CLOSED (0 tracked open — burned
down c096).

**MPI-boundary paths (codemap-verified, marked OUT-of-scope in D1):**
```
$ list_files palace/linalg/rap.*   → palace/linalg/rap.cpp, palace/linalg/rap.hpp   (ParOperator class @ rap.hpp:24-121) — OUT
$ list_files palace/utils/geodata.* → palace/utils/geodata.cpp, palace/utils/geodata.hpp (Partition @ geodata.hpp:35; distribution pipeline :319) — OUT
$ search_text "domain decomposition|Schwarz" palace/linalg/*.hpp → no hits  (NO single-machine decomposition-math primitive in linalg)
```
The codemap confirms the spine-math candidate must come from generalizing EXISTING firm
vocabulary, not from a Palace solver op — a load-bearing input to the probe verdict.

## Deliverable-presence verification

All three c133 dispatches are **audit-class observation reports** (cross-cutter /
same-layer-cross-cutter / maintenance-audit) producing a CYCLE.md, not a named-book-slug
chapter — **open by construction** (no prior-cycle history; the four-step deliverable-
presence check applies to named `book/src/<layer>/<slug>.md` producer scopes, which none
of these are). The WAVE-2 sketch slugs (`sharding-math-decomposition-abstraction-sketch`)
are DEFERRED to c134 and not dispatched. For completeness, the verbatim no-prior-landing
check on the probe-adjacent slugs:
```
$ ls book/src/L4/sharding* book/src/L3/sharding* book/src/L4/decomposition*  → No such file or directory (none exist — open by construction)
$ grep -i "sharding-math|decomposition-abstraction" scaffolding/open-questions.md  → no sharding-math/decomposition-abstraction slug closed (the related deferred OQ `dorfler-cross-rank-bisection-distributed-note-deferred` is OPEN — a probe input, not a discharged deliverable)
```
SKIP-justification: all three dispatches are open by construction (fresh audits, no
prior-cycle history). The STOP-PROPOSING negative-list (lu_solve/back_solve/… L3
backfills) is not matched by any dispatch.

## Open questions / caveats

- **Probe verdict expectation (my recommendation to the human, for lining up WAVE-2):**
  I expect the probe to lean **NO-CLEAR / heavily-qualified** — i.e. the honest framing is
  likely a `roadmap_goal` future-direction note rather than a non-destabilizing spine lift.
  Evidence: (1) the codemap shows Palace has NO single-machine domain-decomposition math
  primitive in `linalg/*` — sharding is purely the `Par*`/`Partition` MPI mechanism in
  `geodata`, so there is no source op to lift, only a generalization of existing firm
  vocabulary; (2) the spine was deliberately re-written under a lifetime structure the MPI
  sharding theory does NOT assume (`project_sharding_mpi_deferred`), so a faithful
  decomposition-abstraction risks re-rooting firm reduce/fold combinators — exactly the
  HARD-GATE-prohibited move; (3) the ONE concrete on-file candidate (the Dörfler cross-rank
  threshold bisection) is already documented as an MPI-collective concern folded into a
  *future distributed note*, not a single-rank spine op. The most-likely good outcome is a
  THIN, non-destabilizing `roadmap_goal` sketch (sub-domain restriction/compose composing
  firm roots BY NAME via `reference`-class edges) that records the direction WITHOUT
  touching any firm node — which is a legitimate WAVE-2 landing under the gate. So: **line
  up WAVE-2 for c134 as a `roadmap_goal`-class sketch, NOT a spine lift** — the probe is
  more likely to clear for a reference-only `roadmap_goal` note than for an in-spine
  combinator. If the probe returns a hard NO-CLEAR (re-rooting required even for a
  reference-only note), WAVE-2 collapses to a recorded-deferred future-direction note and
  the batch-43 head reverts to the MAINTENANCE FLOOR — flag for the batch-43 meta either way.
- The `dorfler-cross-rank-bisection-distributed-note-deferred` OQ is the cleanest concrete
  anchor for the probe; if D1 finds it generalizes spine-expressibly (unlikely per above),
  that is the strongest CLEAR signal.
- No friction-ledger escalating pattern bears on this cycle (batch-42 was clean; the
  `§1.2.2:NN` citecheck false-positive is benign and unrelated to audit-class work).
