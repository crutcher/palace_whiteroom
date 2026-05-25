## 2026-05-25 meta-review (cycles 80–85) — enacted — forward-frontier + intermediate-tier prioritization

- Window: 6 cycles. **Six clean passes, zero new layer prose.** All 6 were retroactive_claims (meta-13 2/6 → meta-17 5/6 → meta-18 6/6). The loop reached a fixed point on cg/gmres/orthog/chebyshev at L4 and switched to backfill mode; meta-17 budget rule was guidance, not enforcement.
- Cascade: 1 LOW; 4 MEDIUM plan items enacted (2 user-directed during enactment); 0 HIGH.
- Plan items enacted: (1) **Retroactive-budget HARD GATE** — Planner MUST-NOT + orchestrator-side `consecutive_retroactive_on_slice ≥ 3` auto-escalates; (2) **Forward-frontier criterion** — when ≥3 of last 6 cycles produced 0 forward-edge landings AND most slices at L4, next push MUST be forward on missing-L4 OR new roadmap slice OR explicit justification; (3) **Skill-uptake structured field** — `critic_verdict.skill_uptake` array surfaces uptake to episodic on every verdict; (4) **Intermediate-tier algorithms** (user directive) — roadmap section with 7 candidates ranked by `|concepts| × |slices_reusing| × (1/cycles_to_extract)`; Planner prefers intermediates over new roots.
- README regenerated with intermediate-tier roadmap reflected.
- Full record: `book/src/meta-reviews/2026-05-25-cycles-80-85.md`.
