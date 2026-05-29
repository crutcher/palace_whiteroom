---
agent: meta-phase
invoked_at: 2026-05-29T063452Z
scope: cycle-021 meta-phase (meta-batch-5; cycles 019/020/021)
status: pending
---

# REPORT: Meta-phase cycle-021 (batch-5)

Fired after cycle-021's integrator-finalize commit `881f200`. Aggregates evidence across the 3-cycle batch (019/020/021) + running history.

## Evidence examined

**Throughput (healthy):** 15 firm landings across 3 cycles (cycle-019: 5 firm + L0 anchor; cycle-020: 6 firm + corrective backfill; cycle-021: 5 firm + 1 BLOCKED-inventory). Counts now L1 firm 13 / L2 firm 6 / L3 firm 9 / L3>L2 firm 2 / L4>L3 firm 3 / L1>L0 themes 16 (BLAS-1 floor 7/8). Seventeenth consecutive clean split-integrator cycle.

**Aggregate tallies (per-cycle / batch-totaled):**
- Open-questions surfaced: large batch (~50+ intake entries across the 3 cycles, most append-only RESOLVED/forward-caveat markers from per-report integrators). ~21 became closure-ready this batch.
- Critic warnings: pervasive `skill-uptake-survey` (all 3 cycles, cycle-wide) + recurring `citation-validity` spot-line warnings (all 3 cycles).
- Critic failures: 0 blocking failures across the batch (zero rejections, zero deferrals batch-wide).
- Unrepairable findings: 0 (`cycle-record.jsonl` shows reports_rejected 0, reports_deferred 0 every cycle — the ledger-update-justification clause is satisfied: friction-ledger updated regardless, see Trends).
- Gate hits: 0 every cycle (retroactive-budget global = 0 all three cycles; build-breakage none; one cycle-021 routed cohort-list consistency-repair, not a content build-repair).
- Deferrals + rejections: 0 / 0 batch-wide. One cycle-021 `partially-applied` (axpbypcz gated by design) + one BLOCKED-inventory (eigsolve, no book change).

**Concentration:** friction is NOT in throughput — it is concentrated in **citation precision** (the recurring inline-anchor drift) and **one fence-discipline defect** (cycle-019, corrected cycle-020). Both are caught downstream; neither reached the artifact.

## Trends recorded

**Escalating (the headline):**
- `producer-citation-drift-verify-not-self-invoked` — **recurrence 3→4, addressed→escalating.** Batch-3 enacted producer self-verify bullets + ASK'd for a mechanical checker (deferred). Batch-4 held clean (defer-confirmed, agreed trigger = "drift returns in batch-5+"). **Batch-5: fresh producer-emit inline-anchor drift in EVERY one of 019/020/021** — a stable 3-cycle pattern (dot/scal/assemble-diagonal/ksp_solve/inner-product-fold/apply_nonlinear_pencil/deflate all 1-2 lines off on pinpoint anchors; wide ranges correct). The recurrence-4 trigger fired. Mechanical-checker tool escalated to ASK (below).
- `skill-uptake-survey-non-invocation-cycle-wide` — recurrence 4→5, stays escalating. Benign telemetry for non-citation skills (no un-classified-axis / missed-refinement-surface reached the artifact); the citation arm is the actionable part, handled by the split-out entry. No-go on recalibrating the check.

**New patterns (both addressed this batch):**
- `firm-chapter-body-authored-outside-proposed-changes-fence` (new, cycle-019) — the batch-5 headline defect: a firm chapter body authored OUTSIDE the `edit:` fence → integrator landed intro-only while dep-map/SUMMARY said firm. Corrected cycle-020; dispatch-prompt guidance held clean cycle-020/021 (zero recurrence). Addressed via the durable critic-side guard.
- `sibling-slice-citation-reanchor-sweep-gap` (new, cycle-020) — a focus-slice re-anchor sweep skipped a sibling slice carrying the same reduction-class drift (`cg.md` vs `gmres.md`). Addressed by a `verify-citation-range` sub-case.

**Validated/extended:**
- `combinator-miner-arity-blind-parametric-family-detection` — validated-by-use (cycle-019 inner_product + cycle-021 deflate/gram live exercises) + extended (the Qualification-B non-fold-family mode-gap closed).

## Plans proposed and judged

| Plan | Kind | Target | Evidence | Cascade | Judgment |
|---|---|---|---|---|---|
| Critic build-readiness guard (firm-body-inside-fence) | prompt edit | `critic.md` `cross-reference-integrity` | cycle-019 fence defect; cost a corrective cycle | Medium | keep (go) |
| Promote `proposed-changes-fence-encloses-full-body-guard` | skill promotion | new SKILL | bar met (friction-ledger entry exists; concrete) | Low | keep (go) |
| Producer fence-reinforcement bullet | prompt edit | harvester/abstractor/lifter/lowering-verifier | same defect; producer-side | Low | keep (go) |
| Fold `verify-intro-firmness` into role-spec | prompt edit | `layer-intro-author.md` | downstream symptom of fence defect | Low | keep (go); no-go on standalone skill |
| Extend `verify-citation-range` sibling-slice sub-case | skill refinement | existing SKILL | candidate's own recommendation | Low | keep (go) |
| Correct gs_orthog worked example | skill refinement | `classify-variant-axis` SKILL | cycle-019 critic flagged stale-vs-L0 | Low | keep (go) |
| Codify `rough-in (test-coverage-bounded)` + `partial-obstruction` | CLAUDE.md invariant | §Methodology invariants | both in live use since cycles 009/013 | Low | keep (go) |
| Combinator-miner non-fold family class | prompt edit | `combinator-miner.md` | cycle-019 Qualification-B mode-gap | Medium | keep (go) |
| Intake→plan migration (standing pass) | priority update | `priorities.md` + `open-questions.md` | every-batch standing duty | Medium | keep (go) |
| Mechanical citation-checker tool | tooling (code) | `tools/` | recurrence-4 fired | Medium | **ask** (code change) |
| Recalibrate skill-uptake-survey check | prompt edit | `critic.md` 8th check | benign telemetry | Low | drop (no-go) |
| Pre-dispatch clean-tree gate | tooling | `integrator-per-report.md` | no batch-5 book-leak | — | held (carried; not re-escalated) |

## Decisions

### go (enacted this cycle)

1. **Critic build-readiness guard (firm-body-inside-fence)** — `.claude/agents/critic.md` `cross-reference-integrity` check gains a fence-enumeration + apparatus-inside-block scan that fails a `firm`-claimed chapter whose body sits outside the proposed-changes fence. The durable structural fix for the cycle-019 defect (the dispatch-prompt reminder held clean but per-dispatch reminders are not durable — friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`).
2. **Skill `proposed-changes-fence-encloses-full-body-guard` promoted** — `skills/proposed-changes-fence-encloses-full-body-guard/SKILL.md` (the deterministic checklist backing the guard).
3. **Producer fence-reinforcement bullets** — `.claude/agents/{harvester,abstractor,lifter,lowering-verifier}.md` each gain a tailored "author the FULL firm body INSIDE the fence" Discipline bullet.
4. **`verify-intro-firmness` folded into role-spec** — `.claude/agents/layer-intro-author.md` Discipline bullet "survey chapter firmness from the on-disk `## Status`, NOT the cycle record" (the downstream symptom of the fence defect).
5. **`verify-citation-range` sibling-slice sub-case** — `skills/verify-citation-range/SKILL.md` gains a third sub-case (sibling/inherited-precedent re-anchor: enumerate ALL distinct cited slices). Friction-ledger `sibling-slice-citation-reanchor-sweep-gap`.
6. **gs_orthog worked-example correction** — `skills/classify-variant-axis/SKILL.md:64-68` corrected to the verified L0 shape (CGS = `[dot×m, allreduce, axpy×m]` plain `w.Add`, not fused `gemv_basis`; CGS2 second pass unconditional, no `refine_threshold`). Closes the cycle-019 skill-friction item.
7. **Codify two rough-in qualifiers** — `CLAUDE.md` §Methodology invariants: `rough-in (test-coverage-bounded)` (structure firm, laws test/literature-gated) + `partial-obstruction` (body lifts, loop is a witnessed sequential-obstruction) as first-class status tiers. Both in live use; canonicalized per the 2 next-meta-phase agenda items.
8. **Combinator-miner non-fold family class** — `.claude/agents/combinator-miner.md` gains a "Constructed-operator-action family" reportable class (unified by a shared `Solver<OperType>::Mult` contract, not a fold-law). Closes the cycle-019 Qualification-B mode-gap.
9. **Standing intake→plan migration** — `priorities.md` re-ranked: cycle-021 active head replaced with a cycle-022 fan-out-ranked slate (axpbypcz floor-close 8/8, lu_solve HIGH-fan-out blocker, eigsolve prerequisite chain reframed, NLEPS pieces, deflate/gram firm, citation-drift sweep). The friction resolutions migrated into the §Methodology priorities (addressed) section.

### no-go (declined)

1. **Recalibrate the `skill-uptake-survey` check** — declined (continued from cycles 012/015/018). The non-citation skills' outcomes stay clean (no un-classified variant axis / missed refinement-surface reached the artifact); the warnings are benign slug-naming telemetry for opus-tier agents. The citation arm is the actionable part and is handled by the split-out `producer-citation-drift` entry's mechanical-checker ASK (which, if built, would also relieve the citation arm of this telemetry warning). Friction-ledger `skill-uptake-survey-non-invocation-cycle-wide` (recurrence 4→5, no-go recorded).
2. **`verify-intro-firmness-survey-against-on-disk-status-lines` as a standalone skill** — declined as standalone; folded into the layer-intro-author Discipline instead. Reason: it is the *downstream* symptom of the cycle-019 fence-truncation defect, whose *upstream* cause is now critic-guarded; the high-leverage fix is the upstream guard, and the downstream survey-check is a one-line role-spec rule, not a procedure needing a skill. Recorded `promoted-as-role-spec` in skill-candidates.

### ask (surfaced to human)

1. **Mechanical codemap-backed citation-range checker tool under `tools/` — ESCALATED from defer to go-recommended.** This is the agreed recurrence-4 escalation of `producer-citation-drift-verify-not-self-invoked`: the batch-3 meta-phase ASK'd for the tool and deferred it; batch-4 held clean (defer-confirmed, trigger = "drift returns in batch-5+"); **batch-5 shows the drift returned as a stable 3-cycle pattern despite the producer self-verify bullets.** The tool validates every `path:lo-hi` in a CYCLE.md's proposed-changes against `reference/` source via the codemap (`get_symbol_def`/`search_text`/`read_range`) as a pre-integration lint, emitting a per-citation OK/DRIFT(±N) report. **Ask-class** (requires code under `tools/`, outside meta-phase write-authority). Enabling conditions all met: recurrence-4 fired; the codemap MCP is in routine zero-permission-denied use; the drift is mechanical (a lint catches it, a prose bullet does not). **What the human should consider:** build it (the role-spec bullets have reached their ceiling — they are necessary but not sufficient against pinpoint drift across a heavy-citation batch; the cross-check by three independent re-reads works but does not scale and occasionally produces critic↔repairer↔verifier disagreement). If declined, the drift-repair-round cost is accepted as standing overhead (the drift is always-caught, never reaching the artifact — so this is a cost-efficiency decision, not a correctness one).

## Enacted changes summary

- `.claude/agents/critic.md` — build-readiness guard (firm-body-inside-fence) in `cross-reference-integrity`.
- `.claude/agents/harvester.md` — fence-encloses-full-body Discipline bullet.
- `.claude/agents/abstractor.md` — fence-encloses-full-body Discipline bullet.
- `.claude/agents/lifter.md` — fence-encloses-full-body bullet (rough-in→firm flip shape).
- `.claude/agents/lowering-verifier.md` — fence-encloses-full-body bullet (status-flip shape).
- `.claude/agents/layer-intro-author.md` — survey-firmness-from-on-disk-status bullet.
- `.claude/agents/combinator-miner.md` — non-fold constructed-operator-action family class.
- `CLAUDE.md` — §Methodology invariants: codify `rough-in (test-coverage-bounded)` + `partial-obstruction`.
- `skills/proposed-changes-fence-encloses-full-body-guard/SKILL.md` — NEW skill.
- `skills/verify-citation-range/SKILL.md` — third sub-case (sibling-slice/inherited-precedent re-anchor).
- `skills/classify-variant-axis/SKILL.md` — gs_orthog worked-example correction.
- `scaffolding/friction-ledger.md` — 5 updates (2 new entries + 3 status flips).
- `scaffolding/skill-candidates.md` — status updates (2 promoted, 1 promoted-as-role-spec, 1 resolved).
- `scaffolding/open-questions.md` — OQ unification: closed 21 / migrated 8 / kept-deferred ~40; maintenance-note header updated.
- `scaffolding/priorities.md` — cycle-022 fan-out-ranked active head + backlog re-rank + methodology-priorities batch-5 additions.
- `scaffolding/cycle-record.jsonl` — meta-phase row appended.
- `scaffolding/cycle-022-resume-notes.md` — NEW (parent orchestrator handoff).

## Open ask items

1. **Mechanical codemap-backed citation-range checker tool** (`tools/`) — recurrence-4 of producer-citation-drift fired in batch-5; ESCALATED from defer to go-recommended. Ask-class (code). Awaiting user decision. (The integrator-per-report pre-dispatch clean-tree gate remains HELD, not re-escalated — no batch-5 book-leak.)

## Cycle-record append

```json
{"cycle_id": "cycle-021", "kind": "meta-phase", "timestamp": "2026-05-29T063452Z", "batch_cycle_ids": ["cycle-019", "cycle-020", "cycle-021"], "meta_batch": "batch-5", "meta_phase_decision_counts": {"go": 8, "no-go": 2, "ask": 1}, "ledger_updates_count": 5, "skill_promotions_count": 2, "skill_retirements_count": 0, "oq_unification": {"closed": 21, "migrated": 8, "kept_deferred": 40}, "session_restart_required": true}
```

(Full row in `scaffolding/cycle-record.jsonl`; go-decisions counted as 8 distinct enactments — the standing intake→plan migration is counted as one go even though it touches both `priorities.md` and `open-questions.md`.)
