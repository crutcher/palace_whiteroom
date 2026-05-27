---
agent: meta-phase
invoked_at: 2026-05-27T012648Z
scope: cycle-004 meta-phase
status: pending
---

# CYCLE: Meta-phase cycle-004

## Evidence examined

- **Cycle plan**: `reports/2026-05-27T004411Z-cycle-planner-cycle-004/CYCLE.md` — 8 dispatches planned, main session dropped `krylov-step` to wave-2 cycle-005 (integrator is once-per-cycle; krylov-step depended on apply_linop firmness). Ran 7 wave-1.
- **Wave-1 CYCLE.md reports**: 7 dispatches, all `ready` post-repair (2 layer-intro-author, 3 harvester, 2 abstractor).
- **Critic findings**: 53 pass / 3 warning / 0 fail (per cycle-record cycle-004 row).
- **Repair outcomes**: 3 repaired / 0 unrepairable / 53 not-needed.
- **Integrator batch**: commits b8332b9 + ed50d6e + 8ac1f37 (filter-repair rename). 0 gate hits. 7 reports applied, 0 deferred, 0 rejected. 25 open questions promoted + 9 answered. 4 wave-conflict observations (all positive — see `integrator-signals.md` cycle-004).
- **Mid-cycle user escalation**: content-pattern Write filter recharacterised from `addressed-by-design` (workaround active) to **bug to repair**. Project-wide rename `REPORT.md → CYCLE.md` landed (commit 8ac1f37); skill `embed-and-persist-subagent-dispatch` retired; user-memory `escalate-process-issues` saved.
- **Running history**: friction-ledger (14 patterns + this cycle's adds), priorities.md, cycle-record.jsonl tail (cycle-003-meta most recent), prior meta-phase reports.

## Trends recorded

### Updates to existing friction-ledger entries

- **`content-pattern-write-filter-on-report-keywords`** — already updated mid-cycle (recurrence-count now 4, status `resolved-by-rename`, `addressed_by: 8ac1f37`).
- **`integrator-signals-channel-working-as-designed`** — recurrence 1→2; `last_observed: cycle-004`. Cycle-004 confirmation: 5 of 7 dispatches were sourced verbatim from cycle-003's Suggested next dispatches. Channel is load-bearing carrier between cycles.

### New friction-ledger entries (this cycle)

1. **`addressed-by-design-misuse-as-workaround-silting`** — status `escalated-by-user`, recurrence 1, `addressed_by: 8ac1f37 + user-memory escalate-process-issues`. The pattern: `addressed-by-design` was used as a category for "we have a workaround; no further action" when the workaround was load-bearing. New discipline: counterfactual test before filing under `addressed-by-design`; meta-phase audit each cycle. The audit was enacted this cycle on the one remaining surviving entry (`integrator-signals-channel-working-as-designed`); it passes the counterfactual (the channel IS the design).
2. **`subagent-skips-edit-on-explicit-instruction`** — status `resolved-by-rename`, recurrence 2, `addressed_by: 8ac1f37`. The pattern crossed model tiers (cycle-002 haiku cycle-planner, cycle-004 opus BiCGStab abstractor). Root cause: default subagent system-prompt instruction ("don't write reports, return text"). Rename obviates the pattern (no skeleton + Edit dance needed; subagents Write CYCLE.md directly).
3. **`advertised-but-unimplemented-krylov-solvers`** — status `new`, recurrence 2 (in one cycle), `addressed_by: null`. Palace ships enum + JSON-parser entries for `MINRES` + `BICGSTAB` that route to a single `MFEM_ABORT` (`palace/linalg/ksp.cpp:53-56`). Mitigation = mfem-as-l0-substrate policy decision (the ASK item below). Pre-decision, additional themes can land for known enum-only solvers. Post-decision, themes either gain MFEM L0 anchors or are explicitly out-of-scope.
4. **`wave-conflict-philosophy-scales`** — status `addressed-by-design`, recurrence 2 (passes counterfactual — the philosophy IS the design, not a workaround). Cycle-003 (2 wave-mates) → cycle-004 (5 wave-mates on `book/src/L1/index.md`), zero structural conflicts. New high-water-mark; cycle-005 can mark same-file row-level edits PARALLEL at wave-size up to ~8.

## Plans proposed and judged

| # | Plan kind | Target | Motivation | Cascade | Judgment |
|---|---|---|---|---|---|
| 1 | Friction-ledger update | 3 new + 1 existing entries | items 1–3 + 5 in the directive | Low | keep — go |
| 2 | Role-spec update | `.claude/agents/layer-intro-author.md` (Vocabulary-cohort template) | item 6: transferable pattern from cycle-004 L1 intro refresh | Medium | keep — go |
| 3 | Skill-candidate update | `cycle-planner-discipline-read-role-spec-first` → deferred; new `vocabulary-cohort-subsection-template` promoted-as-role-spec-template | items above | Low | keep — go |
| 4 | Skill retirement | `embed-and-persist-subagent-dispatch` (already enacted mid-cycle via commit 8ac1f37) | no-longer-applicable post-rename | Low | already enacted — record only |
| 5 | Priorities update | `scaffolding/priorities.md` Now / Near / Watch list / Recently landed | item 7: full reshuffle for cycle-005 | Low | keep — go |
| 6 | ASK item | `mfem-as-l0-substrate-policy` to user | item 4: 2 obstruction themes flag the policy gap | High (user-decision) | keep — ask |
| 7 | Channel-format spec | obstruction-theme treatment for cross-layer-cross-cutter | Watch-list note in priorities; defer until first cross-layer-cross-cutter encounter | Medium | drop for now — premature; add to watch list |
| 8 | Tooling — enum-only Krylov grep skill | candidate skill: "grep labels.hpp + ksp.cpp for MFEM_ABORT-routed enums before harvester dispatch" | item 4 mitigation procedure | Medium | drop as standalone skill; subsumed into priority #13 + #6/#7 pre-grep notes |
| 9 | High cascade | swap cycle-planner to opus | preempt friction recurrence | High | drop — cycle-004 ran 7 dispatches cleanly with haiku; not needed |

## Decisions

### go (enacted this cycle)

- **Friction-ledger update** — appended 3 new entries (`addressed-by-design-misuse-as-workaround-silting`, `subagent-skips-edit-on-explicit-instruction`, `advertised-but-unimplemented-krylov-solvers`, `wave-conflict-philosophy-scales`) and bumped `integrator-signals-channel-working-as-designed` to recurrence-2. File: `scaffolding/friction-ledger.md`.
- **Role-spec update** — added §Vocabulary-cohort subsection template to `.claude/agents/layer-intro-author.md`. Pattern documented as role-spec template (not standalone skill) since it is intrinsic to the role and not cross-role invocable.
- **Skill-candidate updates** — marked `cycle-planner-discipline-read-role-spec-first` as `deferred` with cycle-004 rationale; added new entry `vocabulary-cohort-subsection-template` as `promoted-as-role-spec-template`. File: `scaffolding/skill-candidates.md`.
- **Priorities update** — full reshuffle of Now/Near/Watch/Recently-landed sections; cycle-005 Now list is 9 items reflecting integrator-signals.md cycle-004 suggestions + Shared Infrastructure follow-ups + scalar-promotion-typing-rule lift (promoted from watch). File: `scaffolding/priorities.md`.

### no-go (declined)

- **Channel-format spec for obstruction themes** — premature without a downstream consumer encounter. Recorded as watch-list note in priorities.md; will be authored in the meta-phase that follows the first cross-layer-cross-cutter dispatch over an obstruction theme.
- **Standalone skill for enum-only Krylov grep** — folded into priority #13 (`enum-only-krylov-discovery-grep`) + pre-grep notes on priorities #6/#7 (Householder QR, Jacobi smoother). Friction-ledger entry `advertised-but-unimplemented-krylov-solvers` carries the operational recommendation.
- **Cycle-planner swap to opus** — not needed; cycle-004 ran 7 dispatches cleanly under haiku with no over-scoping or over-cautious overlap classification. The 8fc3a07 user directive (parallel-when-in-doubt) and role-spec Discipline updates appear to have absorbed the previous friction. Demote `haiku-cycle-planner-cascade-pattern` to monitoring-only on watch list.

### ask (surfaced to human)

- **`mfem-as-l0-substrate-policy`** — Cycle-004 landed two L1>L0 obstruction themes (MINRES + BiCGStab) for Krylov solvers that Palace advertises via enum but does not implement (route to a single `MFEM_ABORT`). Implementations live in MFEM (`mfem::MINRESSolver`, `mfem::BiCGSTABSolver`). The CLAUDE.md scope section does not cleanly answer: when Palace ships an enum-only Krylov solver but MFEM provides the implementation, should the L0 substrate include MFEM headers for that algorithm? Decision affects MINRES, BiCGStab, possibly Householder QR + Jacobi smoother + others (recommend grepping `palace/utils/labels.hpp` + `palace/linalg/ksp.cpp` for other `MFEM_ABORT`-routed enums before scoping). Currently captured as obstruction themes; pre-decision, additional themes can land; post-decision, themes either get retroactively rewritten with MFEM L0 anchors or are re-categorised out-of-scope. Friction-ledger entry: `advertised-but-unimplemented-krylov-solvers`. Priority #4 in cycle-005 priorities.

## Enacted changes summary

Files written / edited this invocation:

- `/home/crutcher/git/palace_whiteroom/scaffolding/friction-ledger.md` — 4 new entries + 1 update to recurrence-count.
- `/home/crutcher/git/palace_whiteroom/.claude/agents/layer-intro-author.md` — added §Vocabulary-cohort subsection template.
- `/home/crutcher/git/palace_whiteroom/scaffolding/skill-candidates.md` — `cycle-planner-discipline-read-role-spec-first` → deferred; new `vocabulary-cohort-subsection-template` → promoted-as-role-spec-template.
- `/home/crutcher/git/palace_whiteroom/scaffolding/priorities.md` — full reshuffle (Now / Near / Watch list / Methodology guidance / Recently landed).
- `/home/crutcher/git/palace_whiteroom/scaffolding/cycle-record.jsonl` — append cycle-004-meta row.

Files NOT edited (intentional):

- `scaffolding/problems-sensitivity.md` — no problems/ filings cycle-004; sensitivity recalibration not warranted by a clean cycle.
- `.claude/agents/` other than layer-intro-author — no role changes warranted; all 13 roles performed as designed.
- `skills/` — no new skill promotions (vocabulary-cohort went to role spec instead); the cycle-004 retirement of `embed-and-persist-subagent-dispatch` was enacted mid-cycle via commit 8ac1f37.

## Open ask items

- **`mfem-as-l0-substrate-policy`** — see ask section above. **User decision required** before Shared Infrastructure items #6 / #7 (Householder QR, Jacobi smoother) are reliably scopable. Pre-decision workaround: file as obstruction themes when the implementation routes to MFEM. Post-decision: decide retroactive scope.

## Cycle-record append

```json
{"cycle_id": "cycle-004-meta", "timestamp": "2026-05-27T01:26:48Z", "kind": "meta-phase", "decisions": {"go": 4, "no_go": 3, "ask": 1}, "ledger_updates_count": 5, "skill_promotions_count": 0, "skill_promotions_as_role_template_count": 1, "skill_retirements_count": 1, "skill_retirements_note": "embed-and-persist-subagent-dispatch retired mid-cycle via commit 8ac1f37, not by this meta-phase", "skill_candidate_appends": 1, "priorities_updates_count": 1, "role_spec_updates_count": 1, "ask_items": ["mfem-as-l0-substrate-policy"], "filter_repair_landed": true, "filter_repair_commit": "8ac1f37"}
```
