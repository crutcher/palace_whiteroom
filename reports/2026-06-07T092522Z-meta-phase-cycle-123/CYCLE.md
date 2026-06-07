---
agent: meta-phase
invoked_at: 2026-06-07T092522Z
scope: cycle-123 meta-phase (batch-39; aggregates cycles 121/122/123)
status: pending
---

# REPORT: Meta-phase cycle-123 (batch-39)

The batch-39 meta-phase, firing after the cycle-123 BATCH-CLOSING finalize (`e79fb8c`). Aggregates the 2026-06-07 RE-SCOPE's **lift-through + constructive-kernels campaign** (cycles 121/122/123) and adjudicates the two headline scheme questions the c122/c123 finalizes flagged.

## Evidence examined

- **3 integrator-finalize batch CYCLE.md** (c121 `ae2e2f4` OPENER / c122 `17cdafe` / c123 `e79fb8c` BATCH-CLOSING): 9 + 7 + 4 = 20 dispatches, ALL applied clean (102nd/103rd/104th consecutive clean staging); 0 deferrals, 0 rejections, 0 gate-hits; 1 finalize build-repair total (c121 README de-link).
- **Linter trend:** `reachable` 139 → 156 (+17, plateau BROKEN) → 150 → 158; `rank_violations` HELD 0 throughout; `unresolved_depends_on_targets` 6 → 0; `detritus` 123 → 136 → 132 (the climb ENTIRELY reference-edge-liveness accounting, NOT new defects); final `files=389, reachable=158, roots=43, rank_violations=0, unresolved=0, promotion_frontier=14`.
- **OQ ledger:** ~40 new OQs promoted across the batch (the c121 wide-wave's per-report OQs + the c122/c123 follow-ups). The two scheme questions surfaced as the c122/c123 finalize headlines.
- **friction-ledger / problems/:** no new problems/ filings; the reference-edge-liveness detritus-overcounting is the one new friction pattern (2-of-3-cycle persistence: c122 surfaced, c123 confirmed with the contrast).

## Trends recorded

- **NEW friction entry `reference-only-reachable-firm-nodes-over-counted-as-detritus`** (first_observed c122, last_observed c123, recurrence 2, status `addressed`). The combinator-primary + DIRECTIVE-3 dual-surface models systematically produce firm/roadmap_goal nodes reachable only via `reference` edges; the depends-on-only GC marks them `[GARBAGE*]`, so `detritus` climbs as a function of correct modeling. Addressed by §2g + RE11 (below).
- **`plateau-as-scope-boundary-not-project-boundary` (existing, recurrence 3, status `addressed`):** the lift-through campaign confirms the addressed-by-rescope disposition held — the plateau was a scope boundary, and naming the consumers (GMG, krylov-iteration) discharged 8/10 REs cleanly. No status change.
- No other friction patterns escalated; no `tools/`-unrepairable findings carried (unrepairable count was 0 across the batch).

## Plans proposed and judged

1. **Adjudicate scheme-Q (a) reference-edge-liveness** — scheme/linter-semantics decision. Evidence: c122/c123 finalize headlines + the clean contrasting data class (c123-D2 depends-on flip vs the reference-only cohort). Cascade: Medium (scheme-doc + role-spec). KEEP.
2. **Adjudicate scheme-Q (b) rough-in-vs-firm-over-partial-obstruction** — scheme clarification. Evidence: OQ `krylov-iteration-rough-in-vs-firm...` + the GMG-vs-krylov-iteration precedent contrast. Cascade: Low (scheme-doc clarification). KEEP.
3. **§Intake→plan migration + OQ unification** — standing every-batch duty. KEEP.
4. **RE-discharge tracking + RE11 ratification** — standing graded-stack duty. KEEP.
5. **Reshape priorities.md → CYCLE-124/batch-40 head** — standing duty. KEEP.
6. **Refresh reader mirrors (resolution-ladder.md, goal-flow.md)** — standing duty. KEEP.
7. **kernel-API/impl integrity + DIRECTIVE-1 boundary guard** — standing duties. KEEP (both clean this batch — confirmed below).

No speculative plans dropped; all kept plans were actionable this batch.

## Decisions

### go (enacted this cycle)

- **GO — scheme-Q (a) §2g + RE11.** `METHODOLOGY-GRADED-STACK.md` §2g codified: deliberate-reference-only-reachable structural nodes (combinator-primary leaves, DIRECTIVE-3 kernel-impls via `realizes-kernel-api`, root-sibling references) are the Axis-2 baseline-exception pattern, NOT decay-detritus — ratified as **RE11** in `scaffolding/graded-stack-baseline-exceptions.md`. The §3 "reference carries no liveness" rule is UNCHANGED (its load-bearing purpose holds; these nodes are not dead). This is a reporting/classification refinement — no gate-behavior change. An impl mis-typing its `realizes-kernel-api` as `depends-on` is a DEFECT, not RE11. (The NO-GO half is recorded below.)
- **GO — scheme-Q (b) §1g.** `METHODOLOGY-GRADED-STACK.md` §1g codified: well-foundedness CAPS a composition-root at its least-resolved blocking dep; firm-on-positive-structure escapes the test-coverage law-confidence gate ONLY, not the cap. krylov-iteration correctly rough-in; GMG firm because its deps were firm. Codified into `layer-intro-author` §(h).
- **GO — RE-discharge disposition + RE11 ratification.** `scaffolding/graded-stack-baseline-exceptions.md` batch-39 section: RE1/RE2/RE5/RE7/RE8/RE9/RE10 discharged/grounded; RE3/RE4/RE6 residual with promotion conditions re-checked; RE11 ratified. The RE set is a discharge target (DIRECTIVE 2), not a floor.
- **GO — role-spec edits.** `layer-intro-author.md` §(h) + §(i); `lowering-verifier.md` kernel-api/impl integrity bullet. → SESSION RESTART required (`scaffolding/cycle-124-resume-notes.md`).
- **GO — reader mirrors + plan reshape + OQ unification.** `book/src/methodology/resolution-ladder.md` (the cap + RE11) + `goal-flow.md` (the batch-39 arc); `scaffolding/priorities.md` CYCLE-124/batch-40 head; `scaffolding/open-questions.md` unified (closed ~30 / migrated ~6 / kept-deferred ~12).

### no-go (declined)

- **NO-GO — making `reference` edges carry liveness.** Reason: would break the graded-stack §3 rule's load-bearing purpose ("a mere mention must not keep dead vocabulary alive") AND the combinator-primary model (RE6/RE8 leaf→combinator `depends-on` with combinator→leaf `reference`). The correct disposition is RE11 tracking (the GO above), not changing the liveness semantics. Recorded against friction `reference-only-reachable-firm-nodes-over-counted-as-detritus` (addressed: NO-GO on reference-carries-liveness, GO on §2g/RE11).

### ask (surfaced to human)

- **ASK-1 — optional `tools/` `--reference-reachable` reporting tier.** Separate `reference-reachable` from `true-detritus` so the headline `detritus` number is a clean health signal (it systematically over-counts by ~design under the combinator-primary + DIRECTIVE-3 models). Ask-class (`tools/`-code change, outside meta-phase write authority). The most-valuable linter-maintenance candidate now; bundle with the carried `--show-stronger`/`--end-anchor`/`prose-status-inference` items.
- **ASK-2 — the residual-RE disposition + the batch-40+ forward direction.** The lift-through has substantially landed (8/10 REs discharged). RE3 (deflate/NLEPS) discharges in batch-40 item-1; RE6 (axpy-arity) in item-3; RE4 is consumer-gated with no batch-40 consumer. Once the residual burns down + the constructive-kernel substrate firms, the in-scope RE set is fully closed — the next forward direction is the human's call (continue firming the constructive kernels? a new in-scope front? the natural completion plateau again?).

## Standing-duty checks

- **kernel-API/impl integrity — CLEAN.** All 3 spine-dependency kernels (libceed-quadrature, eigsolve, triangular-solve relaxation) kept BOTH surfaces (kernel-api obstruction theme + kernel-impl node); the `realizes-kernel-api` links held `reference`-class; BOTH c122 correspondence audits FAITHFUL (smoother↔triangular-solve faithful with correctly-scoped Hiptmair-distributive coverage; libceed-impl + eigsolve-impl structural-correspondence faithful). No impl downgraded/deleted its API surface; no realizes edge mis-typed as depends-on.
- **DIRECTIVE-1 (MPI/sharding) boundary — CLEAN.** Confirmed via git diff + grep: no MPI-associated book files touched; the GMG/relaxation/AMR chapters read RAP / Dörfler single-rank (no `ParOperator`/`HypreParVector`/`MPI_` lift in the new chapters). No MPI work leaked into active scope.
- **SEMANTIC SURFACE liveness — no new restatement cohort this batch** (the kernel-impl/AMR/krylov vocabulary did not restate a general semantic rule at functional-unit scope; the element-local-rank-tensor front is the next candidate cohort, flagged in the batch-40 head item-2).
- **Graded-stack GC sweep — the reference-edge-liveness adjudication IS this batch's GC headline** (the §2g/RE11 disposition); no orphaned-intent / detritus delete needed (the climb was fully accounted by deliberate-reference-only-reachable firm nodes).

## Enacted changes summary

- `METHODOLOGY-GRADED-STACK.md` — §1g (well-foundedness cap, scheme-Q (b)) + §2g (deliberate-reference-only-reachable, scheme-Q (a)).
- `scaffolding/graded-stack-baseline-exceptions.md` — batch-39 RE disposition (8 discharged/grounded) + RE11 ratification.
- `book/src/methodology/resolution-ladder.md` — the well-foundedness cap mirror + the RE11/lift-through reachability mirror.
- `book/src/methodology/goal-flow.md` — the batch-39 GOAL arc (lift-through landed + two scheme adjudications).
- `.claude/agents/layer-intro-author.md` — §(h) well-foundedness cap; §(i) RE11 deliberate-reference-only-reachable.
- `.claude/agents/lowering-verifier.md` — kernel-api/impl correspondence integrity bullet (RE11 intended-disposition + mis-typed-edge-is-a-defect + scoped-coverage/sibling-edge).
- `scaffolding/priorities.md` — CYCLE-124/batch-40 active head (discharge RE3/RE6 + firm the constructive-kernel substrate + cheap hygiene).
- `scaffolding/open-questions.md` — batch-39 unification (header + Closed-index/migrated/kept-deferred section; closed ~30 / migrated ~6 / kept-deferred ~12).
- `scaffolding/friction-ledger.md` — new entry `reference-only-reachable-firm-nodes-over-counted-as-detritus` (addressed).
- `scaffolding/cycle-124-resume-notes.md` — SESSION RESTART notice (2 role-spec edits) + the 2 ASKs.
- `scaffolding/cycle-record.jsonl` — meta-phase row appended.

## Open ask items

1. **ASK-1** — optional `tools/` `--reference-reachable` reporting tier (ask-class `tools/`-code change).
2. **ASK-2** — the residual-RE (RE3/RE4/RE6) disposition + the batch-40+ forward direction now the lift-through has substantially landed.

## Cycle-record append

`{"cycle_id": "cycle-123", "kind": "meta-phase", "timestamp": "2026-06-07T092522Z", "batch": "batch-39", "batch_cycle_ids": ["cycle-121","cycle-122","cycle-123"], "meta_phase_decision_counts": {"go": 5, "no-go": 1, "ask": 2}, "ledger_updates_count": 1, "skill_promotions_count": 0, "skill_retirements_count": 0, "oq_unification": {"closed": 30, "migrated": 6, "kept_deferred": 12}, "session_restart_required": true, ...}` (full row in `scaffolding/cycle-record.jsonl`).
