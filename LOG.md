# Cycle log

Per-cycle human-readable summaries, newest first. Full structured detail in `episodic.jsonl`; full meta-review records in `book/src/meta-reviews/`.

Per-cycle entry format:

```
## YYYY-MM-DD cycle-<N> — <push-kind> <slice> [<edge>] — <verdict>

- Synthesis: <one-line summary of what the cycle produced>.
- Verdict: <pass | revise | reject>. <Brief issues if not pass.>
- Friction: <none | one-line>.
- Structural change: <none | one-line>.
```

Meta-review entry format:

```
## YYYY-MM-DD meta-review (cycles <N>–<M>) — <enacted | partial | deferred>

- Window: <N> cycles. Push breakdown: <X FORWARD, Y BACK, Z SIDEWAYS>.
- Cascade: <a> LOW applied; <b> MEDIUM plan items <approved|deferred>; <c> HIGH escalated.
- Plan items enacted: <one-line summaries, or "none">.
- Recurring patterns: <none | one-line description>.
- Full record: `book/src/meta-reviews/YYYY-MM-DD.md`.
```

New entries are **prepended** immediately below the `---` separator, above prior entries.

---

## 2026-05-24 cycle-1 — forward cg_solver_integration [L0→L1] — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The slice mixes three distinct concerns at L1: (a) top-level ProblemType dispatch to BaseSolver subclasses, (b) IoData DEFAULT→CG resolution, (c) ConfigureKrylovSolver/BaseKspSolver composition. The fact that the middle link (driver Solve() → BaseKspSolver construction) is unverified and left as an open question suggests this slice is trying to span too much. The 'end-to-end linkage' diagram has a '(per driver) constructs BaseKspSolver' step that is hand-waved..
- Structural change: none.
