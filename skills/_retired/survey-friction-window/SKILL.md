---
name: survey-friction-window
description: Scan recent cycles' episodic.jsonl and lessons.md to identify unresolved push-back signals, friction clusters, and unification opportunities; output candidate pushes for the next cycle. Invoke at the start of each Planner cycle.
status: retired
---

> **RETIRED (batch-32 meta-phase, 2026-06-05).** Pre-redirect orchestrator-era skill: it scans `episodic.jsonl` / `lessons.md` for the old Planner role. Those ledgers + the prompted Planner role were deleted (batch-31 non-book orphan-review); this skill is read by NO live `.claude/agents/*` definition. The live replacement is `cycle-planner` reading `friction-ledger.md` + `integrator-signals.md` + the plan. Kept under `_retired/` as historical record (recoverable from git).

# survey-friction-window

The Planner's job is to pick the **next push** (forward / back / sideways / escalate), driven by friction rather than enumeration. This skill is the workflow for surveying the friction window.

## When to invoke

- **Planner**, at the start of every cycle before emitting a `push:` directive.
- Optionally **Meta-Critic** during meta-review, as a preliminary to `cluster-friction-patterns` (which operates over a larger window).

## Procedure

1. **Define the window.** Default: last 5 cycles. Wider (10–15) when push-back density is high; narrower (3) when the loop is in steady forward motion.

2. **Pull push-back signals.** Filter `episodic.jsonl` entries within the window where `push_back_signals` is non-empty OR `friction_observed` names a specific lower-layer issue. List each with its (cycle, slice, edge, signal text).

3. **Cluster by lower-layer target.** Group signals by the layer they implicate: signals about L1 → cluster A; about L2 → cluster B; etc. A cluster with ≥2 signals is a strong BACK candidate. A single signal that's been sitting for ≥3 cycles is also a BACK candidate (per the "resolve within 3 cycles" closure criterion).

4. **Scan `lessons.md` for cross-cycle patterns** in the same window. A lesson that matches a current push-back cluster reinforces the BACK push; a lesson that points at a methodology issue rather than a slice issue is an escalation candidate (file under `problems/`).

5. **Check unification opportunities** (SIDEWAYS candidates). Look at the slice index: any two slices at the same layer with similar concepts cited? Any push in the window that noted "this looks like <other slice's> L2"? Those are SIDEWAYS push seeds.

6. **Emit the directive.** Decide on FORWARD / BACK / SIDEWAYS / ESCALATE per `prompts/planner.md`'s ordering criteria:
   - Unanswered question blocking the highest-value push → Explorer cycle (FORWARD to L1).
   - Recent push-back signals naming specific lower-layer change → BACK.
   - High-Li slice with friction remaining → FORWARD.
   - Multiple slices at the same layer with no friction → SIDEWAYS.
   - No clear next step → ESCALATE.

## Heuristics

- **Don't let push-back signals accumulate.** If the window has ≥3 unresolved signals on different layers, the next 2–3 cycles should all be BACK pushes. Forward motion can wait.
- **Sideways is undervalued.** When in doubt between FORWARD and SIDEWAYS, prefer SIDEWAYS — unification driven by cross-slice pressure is a project-level multiplier.
- **ESCALATE is rare but real.** If three cycles' worth of survey produce no productive next push, the methodology has a gap. Emit ESCALATE rather than picking a low-value FORWARD.

## Output

A single `push:` directive per `prompts/planner.md`'s output format. The skill produces the inputs to that directive (the cluster analysis), not extra prose.

## Friction → `problems/`

If running this skill produces persistent ambiguity (e.g., signals routinely cluster around an issue no BACK push resolves; the `episodic.jsonl` schema doesn't capture friction in a clusterable form; the window-size heuristic is consistently wrong), file under `problems/`.
