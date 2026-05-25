## 2026-05-25 cycle-35 — forward gmres [L4→L4] — revise

- Synthesis: Cycle on gmres L4→L4: tighten the L4 form by collapsing the over-articulated StopTag/hit_limit_converged plumbing into a single typed Outcome flowed through SimState, removing the calculus-level friction flagged as an open question; preserves variant absorption and sequential-obstruction placement.
- Verdict: revise.
- Friction: The Outcome ADT {Continue, Done Bool} carrying a boolean converged flag is itself slightly labored — Done Bool re-encodes the same information that (K.beta < ε) would expose at the call site. If solve_loop pattern-matches Outcome to decide recursion, the boolean payload is only consumed by the caller's final return shape. Consider whether solve_loop can return the terminal SimState directly and let the caller inspect (s.beta < ε) once, eliminating the boolean payload entirely..
- Structural change: applied: 1 lesson(s); 2 rotation_claim(s).
