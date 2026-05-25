## 2026-05-25 cycle-70 — forward gmres [L0→L1] — pass

- Synthesis: GMRES L0 citation tightening: re-anchored 12 cited regions per Explorer audit. Split L0.3 → L0.3a/L0.3b (real/complex `GeneratePlaneRotation`) since prose claimed both specialisations but cited only the real. Split L0.8/L0.9 into Initialize/Update sub-entries (a/b). Tightened L0.10/L0.11 boundary at the inner-loop init line (`int j = 0;` at 613). Tightened L0.13 from cited 733-875 (spilled into template-instantiation block) to 734-871 — the audit-failing function-boundary case. Tightened L0.11a to 592-600 so the 10%-threshold comparison line falls inside the cited range. Added clickable source-citation links throughout the L0 section per the 2026-05-25 citation-format rule (existing L0 used bare symbolic citations). Added a note that FGMRES inherits but never uses the `r` workspace field. No L1/L2/L3/L4 prose changes — this is a citation-only tightening pass; the dataflow/primitive/global/calculus forms are unaffected.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 1 rotation_claim(s).
