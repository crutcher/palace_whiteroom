# problems/ filing sensitivity

A self-tuning knob that adjusts how readily per-cycle agents file `problems/` entries. The target is **1 problem filed per 15 agent runs**. The Meta-Critic recalibrates at each meta-cycle based on the actual rate over the last 2 meta-cycle windows.

## Current state

```yaml
sensitivity: 3
target_rate: 0.0667  # 1 / 15
last_calibrated: 2026-05-28  # cycle-012 meta-phase (batch-2 closure). HOLD at 3. 0/11 layered-era filings, but the structural-absorption interpretation is now the standing finding: the scaffolding/ channels (friction-ledger, open-questions, integrator-signals) absorb what would have been problems/ filings in the slice era. Do NOT escalate sensitivity (would pressure filing into a superseded channel). See Calibration history.
```

## Sensitivity scale

Integer 1-5. Default 3.

- **1 — Very conservative.** File only egregious, immediate-blocker problems where the current cycle cannot proceed at all without human intervention. Speculative concerns and out-of-role observations are suppressed.
- **2 — Conservative.** File when the agent has concrete evidence the right answer requires authority it doesn't have (the original `problems/README.md` bar). Speculative concerns are suppressed.
- **3 — Default (current).** Standard bar per `problems/README.md`: out-of-role conflicts, in-line framing concerns exceeding agent responsibility, tooling/infrastructure gaps. Per-cycle judgment.
- **4 — Eager.** Lower the bar: cross-cutting observations the agent isn't sure about are worth surfacing. Reasonable speculative concerns file.
- **5 — Very eager.** File even speculative, weakly-evidenced concerns when the agent suspects a pattern. Used when the loop is in an exploration phase or when the problem-filing rate has been too low.

## Calibration rule

At each meta-cycle, the Meta-Critic runs:

1. Count problem files created in the last 2 meta-cycle windows (combined). Use `git log` or file mtimes; the orchestrator helper `state.count_recent_problem_filings(window=2_meta_cycles)` returns this.
2. Count cycles in the same window (read from `episodic.jsonl` or count meta-cycle window sizes).
3. Compute `actual_rate = problems / cycles`.
4. Compare to `target_rate = 0.0667` (1/15):
   - `actual > 1.5 × target` → decrease `sensitivity` by 1 (floor at 1). The agents are filing too readily; raise the bar.
   - `actual < 0.5 × target` → increase `sensitivity` by 1 (cap at 5). The agents are filing too rarely; lower the bar.
   - Otherwise → hold.
5. Update the `sensitivity:` value and `last_calibrated:` field above. Record the count and rate in *Calibration history* below.

The calibration is a LOW direct action in the meta-review plan: it edits this file in place.

## Agent invocation

The orchestrator reads the current `sensitivity:` value at each cycle and injects it into the per-cycle agent prompts (Critic, Synthesizer, Explorer) via a short context line: `problems_sensitivity: <N>`. Each agent's prompt describes the meaning of each level and acts accordingly when considering whether to file a problem.

## Saturation (added meta-22 after 0/24 over two consecutive windows at cap=5)

When sensitivity has been at cap (5) AND filing rate has been 0 for ≥2 consecutive 12-cycle windows, the calibration knob has saturated. Two interpretations:

1. **Genuine** — the loop is producing no filing-worthy friction. Target rate (1/15) needs revising downward.
2. **Mis-calibrated bar** — agents have an internalized definition of "filing-worthy" that excludes things the project considers filing-worthy.

To distinguish, the meta-review surfaces the saturation as a LOW direct action and the human reviews the worked examples below. If a fraction of these examples should have been problems/ filings, the bar is mis-calibrated; if none should have been, the target rate needs revising.

### Worked examples of borderline-friction (could have been problems/ filings)

These are concrete cases from recent meta-reviews where an agent caught friction in-role but the situation arguably exceeded that role's authority — candidates for problems/ filings rather than in-role workarounds:

- **Meta-21 cycle 115**: Critic explicitly told the Synthesizer "consider filing a problems/ entry" about the rotation_claim schema gap for self-edges. The Critic surfaced the schema-gap concern *in its verdict* rather than filing. A higher-sensitivity Critic should have filed.
- **Meta-20 cycles 98-102**: 5 consecutive bookkeeping_incomplete signals on arnoldi_step due to `slice_index_updates` lacking append-by-slug. The orchestrator carried this for 5 cycles before meta-review surfaced it. An Explorer/Synthesizer noticing the recurring `bookkeeping_incomplete` could have filed.
- **Meta-19 cycles 86-89**: 4-cycle escalate-storm from the retroactive hard gate. The Planner kept proposing cg cycles knowing they would escalate. A higher-sensitivity Planner — or Critic observing the pattern — could have filed.
- **User directives 2026-05-25 and 2026-05-26**: skill-priority +60%, intermediate-tier prioritization, dep-map future markers, refinement push kind, log/ restructure, problems-sensitivity, push-after-commit. All of these landed as human-direct prompts. A higher-sensitivity meta-cycle could have surfaced some of these as problems/ filings rather than waiting for the human to notice.

### Decision protocol

If 3 consecutive 12-cycle windows show 0 filings at cap, the Meta-Critic should escalate to HIGH (it's a methodology gap) and the human revisits the problems/ definition.

## Calibration history

| Date | Meta | Window cycles | Problems filed | Rate | Sensitivity (after) | Notes |
|------|------|---------------|----------------|------|---------------------|-------|
| 2026-05-26 | (initial) | — | — | — | 3 | Initial setting. |
| 2026-05-26 | meta-20 | 92–103 (12) | 0 | 0.000 | 4 | Below 0.5× target → +1; encourage more surfacing. |
| 2026-05-26 | meta-21 | 104–115 (12) | 0 | 0.000 | 5 | Still below 0.5× target → +1 (now at cap). If next window is also 0, the bar may be structurally too high — surface for review. |
| 2026-05-26 | meta-22 | 116–127 (12) | 0 | 0.000 | 5 | **At cap; 0/24 across two consecutive windows.** Calibration knob has saturated. Surfacing for human review per *Saturation* section below. |
| 2026-05-26 | meta-23 | 128–139 (12) | 0 | 0.000 | 5 | **THIRD consecutive cap-zero window. 0/36 total.** Per Saturation decision protocol, this is the HIGH-escalation threshold — surface for human review of the problems/ definition itself. The worked examples in this file are the candidate filings; review which (if any) should have been filed under the current bar. |
| 2026-05-26 | (user reset) | — | — | — | 3 | **User relaxed the filing bar**: `problems/` now permits "observed-but-not-in-focus" drive-by observations (problems noticed in reference work consulted for context, not in the cycle's focused work). Sensitivity reset from cap=5 to default 3 to recalibrate against the new bar. See `problems/README.md` *(B) Observed-but-not-in-focus*. |
| 2026-05-26 | meta-25 | 152–166 (15) | 0 | 0.000 | 3 | First window under relaxed bar produced 0 filings. Hold at 3 — the bar relaxation only landed mid-window (commit 9f05b54) so most cycles ran with the prior prompt context. Next window will be the clean first-relaxed-bar measurement. |
| 2026-05-27 | cycle-006-meta | pilot-1, cycles 002–006 (6 cycles, post-layered-era) | 0 | 0.000 | 3 | **Layered-era flow first calibration.** No `problems/` filings across the 6 layered-era cycles to date. Filing rate is 0/6 ≈ 0.000 — well below 0.5× target (0.033). Calibration rule would advise +1 → sensitivity 4. **Hold at 3** this cycle for three reasons: (a) cycle count (6) is below the standard 15-cycle window used by prior meta-25 measurement — too few samples; (b) the layered-era flow is structurally different from the slice-era flow (per-dispatch agents have narrower scope; many would-be "problems" are now naturally Open questions instead); (c) the system has been actively producing healthy out-of-band signals via the `scaffolding/` channels (friction-ledger, open-questions, integrator-signals) which arguably absorb what would have been `problems/` filings in the slice era. **Next calibration**: at cycle-012 (after 12 layered cycles, comparable to a prior window). If filing rate is still 0 then, escalate to sensitivity 4 or surface for human review whether the layered-era flow has structurally absorbed the `problems/` channel. |
| 2026-05-28 | cycle-012-meta (batch-2 closure) | cycles 007–012 (6 cycles); layered-era total 002–012 (11 cycles) | 0 | 0.000 | 3 | **Scheduled cycle-006-meta follow-up calibration. HOLD at 3 — do NOT escalate to 4.** Filing rate is 0/11 layered-era. The calibration rule's mechanical advice is +1, but the cycle-006-meta hypothesis (c) is now the **standing finding**, not a deferral: the layered-era `scaffolding/` channels have **structurally absorbed** the `problems/` channel. Evidence — across batches 1 and 2 the system surfaced abundant friction through the richer channels: friction-ledger grew to ~30 named patterns, open-questions to 129 open / 31+ answered with healthy closure (8 closed cycle-012 alone), integrator-signals carries 10 curated forward signals per cycle. None of these would have been better-served as a `problems/` filing; the drive-by-observation category (the 2026-05-26 bar relaxation) is what these channels already do, with better routing. Escalating sensitivity to 4 would pressure agents to file into a channel that is correctly dormant. The `problems/` channel remains available for genuine out-of-role / immediate-blocker concerns (its narrowest correct use), but the 1/15 target_rate is a **slice-era artifact** that does not fit the layered flow. **Not surfacing as a HIGH escalation / not asking the user** per "don't over-ask" — the channels are working; the dormant `problems/` channel is a feature of the layered flow, not a methodology gap. **Next calibration**: cycle-018 (batch-4 closure). Only escalate or surface if a concrete case arises where an agent SHOULD have filed a `problems/` entry but routed it to a scaffolding channel that handled it poorly. |
