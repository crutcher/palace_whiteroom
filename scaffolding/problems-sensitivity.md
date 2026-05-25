# problems/ filing sensitivity

A self-tuning knob that adjusts how readily per-cycle agents file `problems/` entries. The target is **1 problem filed per 15 agent runs**. The Meta-Critic recalibrates at each meta-cycle based on the actual rate over the last 2 meta-cycle windows.

## Current state

```yaml
sensitivity: 3
target_rate: 0.0667  # 1 / 15
last_calibrated: 2026-05-26  # meta-N — set on each Meta-Critic calibration
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

## Calibration history

| Date | Meta | Window cycles | Problems filed | Rate | Sensitivity (after) | Notes |
|------|------|---------------|----------------|------|---------------------|-------|
| 2026-05-26 | (initial) | — | — | — | 3 | Initial setting. |
