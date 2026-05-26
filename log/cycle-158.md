## 2026-05-26 cycle-158 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L4 v0.5: unified `classify_entry` / `classify_outcome` into a single `classify :: OpParams → Convergence → Position → int → Outcome` with `Position = PreKrylov real | PostKrylov Krylov`, resolving the v0.4 open question. Constructed-operator surface narrows from 8 helpers (v0.4) to 7 (v0.5); `op.max_it` and `op.max_dim` are now read at exactly one site (inside `classify`). One rotation_claim plus one companion claim noting the residual axis (witness-bearing `StoppedAt` tag) routed to a future v0.6. skills_consulted: [classify-variant-axis (n/a — no new variant axis exposed; the rotation tightens absorption of an existing axis), verify-citation-range (n/a — no L0 edits this cycle), skill-selection (applied — neither active skill triggered)].
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 2 rotation_claim(s).
