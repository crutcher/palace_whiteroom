## 2026-05-25 cycle-26 — forward divfree [L1→L2] — revise

- Synthesis: divfree L1→L2: composed apply as apply_linop(WeakDiv) → set_subvector_zero → ksp_solve → apply_linop(Grad) + axpy. Extracted set_subvector_zero and ksp_solve as new concept entries; appended divfree-use section to apply_linop. Sign convention and BC ordering preserved as load-bearing L2 claims; MG-vs-AMG preconditioner choice and partial-vs-full assembly recorded as transparent optimizations.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `divfree` | L1 | C-7 | Divergence-free projector. Constructed-operator absorpt'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
