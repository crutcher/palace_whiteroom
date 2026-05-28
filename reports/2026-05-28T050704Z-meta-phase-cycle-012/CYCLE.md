---
agent: meta-phase
invoked_at: 2026-05-28T05:07:04Z
scope: cycle-012 meta-phase (batch-2 closure; cycles 010/011/012)
status: pending
---

# REPORT: Meta-phase cycle-012 (meta-batch-2 closure)

Second meta-phase under the 3:1 cadence. Aggregates evidence across primary cycles 010/011/012. Primary evidence source: the cycle-012 integrator-signals section's 10 curated forward signals + the cycle-010/011 signals for the 3-cycle aggregation. Fires after the cycle-012 finalize commit `5964cb4` (+ SHA-patch `8d01b2f`).

## Evidence examined

**Aggregate, batch-2 (cycles 010/011/012):**
- **Productivity (healthy batch):** L3 1→8 firm (BLAS-1 cohort closed cycle-011), L1 8→10 (orthogonalize + chebyshev-smoother cycle-012), L2 1→2 (chebyshev-iteration cycle-012 — first L2 growth since cycle-005), 8/10 slices reduced (cumulative), eigsolve cycle-009 OQ cluster fully closed across the batch, MCP codemap operational.
- **Critic warnings/failures:** cycle-012 — 2 gate hits (citation-carry-forward-correction ×2); 1 HIGH critic finding (write-authority phase-boundary violation, report #6) caught + repaired pre-integration. Batch clean-integration streak preserved (8 consecutive clean integration cycles 005–012).
- **Unrepairable findings:** 0 across the batch (cycle-record `repair_outcomes.unrepairable` 0; all reports applied as-is, no deferrals/rejections/rework loops cycle-012).
- **Integrator gate hits:** cycle-012 = 2 (both citation carry-forward corrections, applied). No deferrals, no rejections.
- **Open-questions:** cycle-012 promoted 17, closed 8; cycle-011 +7 net (12 new, 4 resolved + 1 partial); batch closure-heavy. OQ ledger health: 129 open / 31 answered + 3 resolved + 5 partially-answered + 2 answered-by-rough-in. Closing meaningfully (8 closed cycle-012 alone); NOT monotonic-with-zero-closure — well clear of the 20-cycle-zero-closure escalation trigger.
- **Problems filings:** 0 across the layered era (0/11).

**The 10 enumerated forward signals (cycle-012 integrator-signals §Integration-tooling friction)** are the primary aggregation input and are addressed one-to-one in §Decisions.

## Trends recorded

Friction-ledger updates this meta-phase (per signal):

| Pattern slug | before → after | status |
|---|---|---|
| `mcp-codemap-permission-denied-across-batch-1` | recurrence-3 ask | → **resolved** (user enabled option (a) `ceb87da`; cycles 011/012 zero permission-denied) |
| `specialized-agent-direct-write-to-book-during-dispatch` | (generalizes cycle-008 `abstractor-direct-write…` recurrence-1) | **NEW recurrence-2** → addressed (layer-intro-author prompt-guard + skill) |
| `skill-uptake-survey-non-invocation-cycle-wide` | (new) | **NEW recurrence-3** → recurring (judged telemetry-noise; recalibration deferred) |
| `partly-constructive-lowering-theme-status` | (new) | **NEW recurrence-3** → addressed (CLAUDE.md invariant + 2 role-spec touches) |
| `negative-anchor-citation-pattern` | (new) | **NEW recurrence-3** → addressed (folded into partly-constructive invariant) |
| `lifter-scope-content-correction-boundary` | (new) | **NEW recurrence-3** → addressed (lifter + lowering-verifier Discipline touches) |
| `cycle-planner-dispatch-prompt-framing-drift` | (new) | **NEW recurrence-3** → addressed (cycle-planner MCP-path-verify Discipline touch) |
| `per-report-integrator-cycle-mislabeling` | (new) | **NEW recurrence-1** → addressed (integrator-per-report cycle-id-from-parent-path Discipline touch) |
| `l3-l1-inline-identity-rotation-convention` | (new) | **NEW recurrence-9** → addressed (DECISION: codify in-line; no `L3-L1/` dir) |
| `mcp-first-localization-codified` | (new) | **NEW recurrence-1** → addressed (CLAUDE.md §Target system soft note) |

10 ledger updates total (1 resolution flip + 9 new/generalized entries). Cycle-record shows `unrepairable: 0` for the batch, so no "unrepairable > 0 but no ledger entry" gap.

## Plans proposed and judged

| # | Plan kind | Target | Motivation (evidence) | Cascade | Judgment |
|---|---|---|---|---|---|
| P1 | Prompt edit | `layer-intro-author.md` write-authority prompt-guard | signal 1; recurrence-2 generalized | Medium | **keep / go** |
| P2 | Skill promotion | `skills/phase-1-slice-reduction-audit/SKILL.md` | signal 2; recurrence-3 + severity | Medium | **keep / go** |
| P3 | Recalibration | `skill-uptake-survey` check | signal 3; recurrence-3 cycle-wide | Medium | **drop now / no-go** (telemetry-noise) |
| P4 | Methodology invariant | `partly-constructive` status (CLAUDE.md + abstractor/lowering-verifier) | signal 4; recurrence-3 | Medium | **keep / go** |
| P5 | Methodology invariant | negative-anchor codification | signal 5; recurrence-3 | Low | **keep / go** (folded into P4) |
| P6 | Scope clarification | lifter / lowering-verifier content-correction boundary | signal 6; recurrence-3 | Medium | **keep / go** |
| P7 | Prompt edit | `cycle-planner.md` MCP path-verify | signal 7; recurrence-3 | Low | **keep / go** |
| P8 | Prompt edit | `integrator-per-report.md` cycle-id-from-parent-path | signal 8; recurrence-1 | Low | **keep / go** |
| P9 | DECISION + invariant | L3-L1 in-line convention (codify, no dir) | signal 9; recurrence-9 | Medium | **keep / go** (option a) |
| P10 | Methodology note + ledger | MCP-first localization codification + resolve MCP ledger | signal 10 | Low | **keep / go** (soft codify) |
| P11 | Skill promotion | `revert-dispatch-phase-book-mutation` | signal 1 companion (repairer recovery) | Low | **keep / go** (safety-net) |
| P12 | Skill extension | `verify-citation-range` audit-report sub-case | skill-candidate `audit-report-inherited-miscitation-lint` | Low | **keep / go** (extend, not new) |
| P13 | Calibration | `problems-sensitivity.md` | scheduled cycle-006-meta follow-up; 0/11 filings | Low | **keep / go** (hold at 3, standing-finding) |
| P14 | Tooling gate | integrator-per-report pre-dispatch clean-tree gate | signal 1 cycle-008 watch option (b) | High (code/tooling) | **drop / no-go** (ask-class; repairer suffices) |

Sharpened during judging: P5 folded into P4 (they co-occur — a partly-constructive sub-part is justified by negative anchors). P12 enacted as an extension of an existing firm skill rather than a new skill (per the candidate's own recommendation). P14 dropped as a no-go (it is a tooling/code change = ask-class, and the repairer already catches the leak reliably).

## Decisions

### go (enacted this cycle)

1. **P1 — layer-intro-author write-authority prompt-guard.** Added a prominent top-level Discipline bullet to `.claude/agents/layer-intro-author.md`: do NOT write to `book/` yourself; emit proposed-changes blocks; concept-page corrections feel like edits but are changes to propose. Rationale: signal 1, recurrence-2 of the generalized leak pattern (abstractor cycle-008 + layer-intro-author cycle-012). The cycle-009 "treat as one-off" decision held for the abstractor specifically but the pattern recurred for a different agent — per the cycle-008 watch clause, enact the guard on the agent that leaked.

2. **P2 — promote `phase-1-slice-reduction-audit` skill.** Wrote `skills/phase-1-slice-reduction-audit/SKILL.md` (four-part template + the START+END boundary-verification + unique-text-anchor refinement that the recurrence-3 HIGH-severity line-map defect made necessary). Rationale: signal 2; recurrence-3 + severity escalation; concrete shape; skill-candidate + priority entries exist. Updated skill-candidates.md status → promoted.

3. **P4+P5 — codify `partly-constructive` theme-status as first-class + negative-anchor distinction.** New CLAUDE.md §Methodology invariants bullet "Theme/operator status `partly-constructive` is first-class" (defines the status, its caveat-with-citation + promotion-condition requirement, and the negative-anchor distinction from obstruction-theme negative anchors). Discipline touches: `abstractor.md` (author with the status + caveat + promotion condition; don't over/under-state) + `lowering-verifier.md` (audit may UNBLOCK a partly-constructive promotion without ENACTING it; gate it). Rationale: signals 4+5; recurrence-3; eigsolve-mutation-rotation precedent (gated to cycle-013). Friction-ledger entries `partly-constructive-lowering-theme-status` + `negative-anchor-citation-pattern`.

4. **P6 — codify lifter/lowering-verifier content-correction boundary.** Discipline touches: `lifter.md` + `lowering-verifier.md` — L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded; re-architecting re-routes to abstractor/harvester. Rationale: signal 6; recurrence-3; all three instances (cycle-010/011/012) were sound L0-evidence-driven fixes; forcing a re-route for every prose correction adds a full round-trip. Friction-ledger `lifter-scope-content-correction-boundary`.

5. **P7 — cycle-planner MCP path-verification.** Discipline bullet on `.claude/agents/cycle-planner.md`: verify Palace source file paths / symbol locations via the MCP codemap before citing them in a dispatch scope; don't cite from memory/inference. Rationale: signal 7; recurrence-3 (cycles 010/011/012 all drifted on `linalg/*` paths); the enabling fix (MCP access) is now available. Friction-ledger `cycle-planner-dispatch-prompt-framing-drift`.

6. **P8 — integrator-per-report cycle-id discipline.** Process step 7 + Discipline touch on `.claude/agents/integrator-per-report.md`: the staging-dir path (and cycle-id) comes from the parent's dispatch; never infer it from report content (forward-references to future cycles are content, not the filing target); if no path supplied, stop. Rationale: signal 8; recurrence-1 (report #3 mis-filed to a cycle-013 staging dir). Friction-ledger `per-report-integrator-cycle-mislabeling`.

7. **P9 — L3-L1-directory-naming-structure-policy DECISION: codify in-line (option a). Do NOT introduce `book/src/L3-L1/`.** New CLAUDE.md §Methodology invariants bullet "Identity rotations across non-adjacent layers are annotated in-line" + `harvester.md` Discipline touch. Rationale (signal 9; recurrence-9): lowering directories are per-adjacent-edge by design; non-adjacent identity is the transitive consequence of the adjacent-edge themes (L3>L2 ∘ L2>L1 ⟹ L3>L1); ~9+ instances already annotate in-line cleanly (`book/src/L3/krylov-step.md:28-31` precedent); a `L3-L1/` dir would break the adjacent-edge invariant, duplicate the chain, and require a non-trivial migration for zero coherence gain. Friction-ledger `l3-l1-inline-identity-rotation-convention`.

8. **P10 — MCP-first localization codification + resolve MCP ledger.** CLAUDE.md §Target system soft note (preferred localization path; agent judgment retained) + flipped `mcp-codemap-permission-denied-across-batch-1` ledger entry to `resolved`. Did NOT add a hard per-role mandate (the MCP server's own instructions already advise the pattern to every tool-holding agent; per-role mandate would be redundant + over-constraining). Friction-ledger `mcp-first-localization-codified`.

9. **P11 — promote `revert-dispatch-phase-book-mutation` skill.** Wrote `skills/revert-dispatch-phase-book-mutation/SKILL.md` (deterministic seven-step repairer git procedure). Companion safety-net to the P1 prompt-guard (primary mitigation). Updated skill-candidates.md status → promoted.

10. **P12 — extend `verify-citation-range` with audit-report sub-case.** Added an "Audit-report / inherited-citation sub-case" section to `skills/verify-citation-range/SKILL.md` (independently `read_range`-confirm every asserted-verified anchor; don't transcribe from the audited artifact; internal-consistency reconcile) + a lint bullet on `lowering-verifier.md`. Enacted per the candidate's recommendation (a). Updated skill-candidates.md status → promoted-as-skill-extension.

11. **P13 — problems-sensitivity calibration: hold at 3 (standing structural-absorption finding).** Updated `scaffolding/problems-sensitivity.md`: hold sensitivity at 3 despite 0/11 filings; the scaffolding channels have structurally absorbed the `problems/` channel (the cycle-006-meta hypothesis (c) is now the standing finding, not a deferral). Did not escalate sensitivity (would pressure filing into a correctly-dormant channel) and did not surface as HIGH (the channels work). Next calibration cycle-018.

### no-go (declined)

1. **P3 — recalibrate the `skill-uptake-survey` critic check.** Declined this cycle. The check fires cycle-wide (all 8 cycle-012 reports lacked explicit skill invocation), but the agents ARE doing the skill-described work (citation-range checks, variant-axis classification happen) — they just don't write the invocation string. For opus-tier agents the skill knowledge is internalized; explicit invocation is telemetry, not a quality signal. The one place it mattered (the `:387` drift) is better addressed by the P12 `verify-citation-range` audit-report extension than by forcing invocation telemetry. Recalibrating now is premature. Friction-ledger `skill-uptake-survey-non-invocation-cycle-wide` status `recurring` (NOT escalating — benign telemetry). Watch: if a future cycle shows a *quality defect* an explicitly-invoked skill would have caught, escalate to recurrence-4 and narrow the check to flag missing *outcomes*, not missing invocation *strings*.

2. **P14 — integrator-per-report pre-dispatch clean-tree gate.** Declined. This is the cycle-008 watch-clause option (b) — a gate that detects whether a dispatch wrote outside its proposed-changes channel and refuses to apply. It is a tooling/code change (ask-class per CLAUDE.md "Edit code ... are ask-decisions"), and the repairer already catches the leak reliably pre-apply (skill `revert-dispatch-phase-book-mutation`). The prompt-guard (P1) + repairer-safety-net (P11) cover the pattern at recurrence-2 without a tooling change. Re-weigh only at recurrence-3 (a third leaking agent).

### ask (surfaced to human)

**None.** Per the cycle-009-meta one ASK (MCP rollout) being now resolved, and the "don't over-ask / incremental refinement is default-accepted" project memory, this meta-phase enacted all kept plans as `go` (all Low/Medium cascade) and declined the two no-gos with reasons. No High-cascade items (no new agent roles, no cycle-structure changes, no layer-count changes) arose. The L3-L1 decision (signal 9) was the one explicit DECISION item and it was default-accept-able (option a, the recommended default per the cohort's empirical convergence) — not an ASK.

## Enacted changes summary

Files written/edited this invocation:
- `scaffolding/friction-ledger.md` — flipped `mcp-codemap-permission-denied-across-batch-1` to resolved; appended 9 entries (`specialized-agent-direct-write-to-book-during-dispatch`, `skill-uptake-survey-non-invocation-cycle-wide`, `partly-constructive-lowering-theme-status`, `negative-anchor-citation-pattern`, `lifter-scope-content-correction-boundary`, `cycle-planner-dispatch-prompt-framing-drift`, `per-report-integrator-cycle-mislabeling`, `l3-l1-inline-identity-rotation-convention`, `mcp-first-localization-codified`).
- `skills/phase-1-slice-reduction-audit/SKILL.md` — NEW (promoted).
- `skills/revert-dispatch-phase-book-mutation/SKILL.md` — NEW (promoted).
- `skills/verify-citation-range/SKILL.md` — extended with audit-report / inherited-citation sub-case.
- `scaffolding/skill-candidates.md` — status updates: phase-1-slice-reduction-audit → promoted; revert-dispatch-phase-book-mutation → promoted; audit-report-inherited-miscitation-lint → promoted-as-skill-extension.
- `.claude/agents/layer-intro-author.md` — write-authority prompt-guard Discipline bullet.
- `.claude/agents/cycle-planner.md` — MCP path-verification Discipline bullet.
- `.claude/agents/integrator-per-report.md` — cycle-id-from-parent-path discipline (Process step 7 + Discipline bullet).
- `.claude/agents/harvester.md` — in-line non-adjacent identity-rotation convention bullet.
- `.claude/agents/abstractor.md` — partly-constructive authoring Discipline bullet.
- `.claude/agents/lifter.md` — content-correction-boundary Discipline bullet.
- `.claude/agents/lowering-verifier.md` — partly-constructive-audit-gate + independent-anchor-confirmation Discipline bullets.
- `CLAUDE.md` — §Methodology invariants: 2 new bullets (partly-constructive first-class; non-adjacent identity in-line). §Target system: MCP-first localization note. §Skills: refreshed skills list (+2 promotions + verify-citation-range extension note).
- `scaffolding/priorities.md` — rewrote §Now (active) for cycle-013+ (6 items); compressed batch-1/pre-batch-2 landed items; §Methodology priorities reference section.
- `scaffolding/problems-sensitivity.md` — calibration: hold at 3 + standing structural-absorption finding.
- `scaffolding/cycle-013-resume-notes.md` — NEW (cycle-013 handoff).
- `scaffolding/cycle-record.jsonl` — appended meta-phase record (see below).
- `reports/2026-05-28T050704Z-meta-phase-cycle-012/CYCLE.md` — this report.

Agent-defs changed (7): layer-intro-author, cycle-planner, integrator-per-report, harvester, abstractor, lifter, lowering-verifier. **Session restart required before cycle-013** per friction-ledger `new-agent-defs-need-session-restart`.

## Open ask items

None. (All kept plans enacted as `go`; two no-gos declined with reasons; no High-cascade items arose.)

## Cycle-record append

```json
{"cycle_id": "cycle-012", "timestamp": "2026-05-28T05:07:04Z", "kind": "meta-phase", "phases_fired": ["meta-phase"], "batch_cycle_ids": ["cycle-010", "cycle-011", "cycle-012"], "meta_batch": "batch-2", "meta_batch_position": "closure", "meta_phase_decision_counts": {"go": 11, "no-go": 2, "ask": 0}, "ledger_updates_count": 10, "ledger_status_flips": ["mcp-codemap-permission-denied-across-batch-1 ask -> resolved"], "ledger_new_entries": ["specialized-agent-direct-write-to-book-during-dispatch", "skill-uptake-survey-non-invocation-cycle-wide", "partly-constructive-lowering-theme-status", "negative-anchor-citation-pattern", "lifter-scope-content-correction-boundary", "cycle-planner-dispatch-prompt-framing-drift", "per-report-integrator-cycle-mislabeling", "l3-l1-inline-identity-rotation-convention", "mcp-first-localization-codified"], "skill_promotions_count": 2, "skill_promotions_detail": ["phase-1-slice-reduction-audit", "revert-dispatch-phase-book-mutation"], "skill_extensions_count": 1, "skill_extensions_detail": ["verify-citation-range: audit-report / inherited-citation sub-case"], "skill_retirements_count": 0, "role_spec_touches_count": 7, "role_spec_touches_detail": ["layer-intro-author.md write-authority prompt-guard", "cycle-planner.md MCP path-verify", "integrator-per-report.md cycle-id-from-parent-path", "harvester.md non-adjacent in-line identity convention", "abstractor.md partly-constructive authoring", "lifter.md content-correction boundary", "lowering-verifier.md partly-constructive-audit-gate + anchor-confirm"], "claude_md_invariants_added": 2, "claude_md_invariants_added_detail": ["Theme/operator status partly-constructive is first-class", "Identity rotations across non-adjacent layers are annotated in-line"], "claude_md_other_edits": ["Target system MCP-first localization note", "Skills list refresh"], "priorities_rewritten": true, "decisions_enacted": ["L3-L1-directory-naming-structure-policy: codify in-line (option a); no L3-L1/ directory"], "problems_sensitivity_change": "hold-at-3 (standing structural-absorption finding; 0/11 layered-era filings)", "ask_items": [], "session_restart_required": true, "session_restart_reason": "7 agent-defs changed; cycle-013 needs reloaded definitions", "resume_notes_written": "scaffolding/cycle-013-resume-notes.md"}
```
