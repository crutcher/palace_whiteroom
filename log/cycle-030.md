## 2026-05-25 cycle-30 — forward gmres [L2→L3] — revise

- Synthesis: GMRES L2→L3: field-side primitives lift to global tensor-field form via the support-operator template; `ls_update_column` and `back_solve` recorded as small-dense-state sequential obstructions (first-class L3 results). Extracted `tensor-field-lift` and `sequential-obstruction` concepts.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `gmres` | L2 | 2026-05-24 | L1 dataflow + L2 primitive composition; variant ab'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
