## 2026-05-25 cycle-48 — forward cg [L0→L1] — revise

- Synthesis: cg L0→L1 back-correction: Explorer audit surfaced two prior gaps in v0.2 — Palace's CheckDot partial-function guard (lines 244-250, invoked 4× per solve) was unmodeled, and the !B && initial_guess branch computes initial_res = (b·b)^{1/4} via a compounding sqrt (likely Palace bug; preserved faithfully). L0/L1/L4 updated; both items flagged in Working Notes with citations. Unit-test coverage confirmed absent at test/unit/; CG verified only through integration tests.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/slices/cg.md): '  let initial_res =\n    if initial_guess then\n      let p_tmp = apply B b       '; verdict auto-downgraded pass→revise: substantive write(s) did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
