## 2026-05-25 cycle-56 — forward cg [L3→L4] — pass

- Synthesis: CG L3→L4 rotation_claims emitted retroactively against the on-disk slice (v0.3, L4 against calculus v0.3). Four claims cover: (1) step-body lifting to pure cg_step + iterate_while discharging the L3 sequentiality obstruction; (2) residual-norm logging resolved via L4 v0.3 demand-driven pruning (no Writer effect needed); (3) preconditioner axis absorbed via primary/variant pair with Identity-equivalence; (4) CheckDot guard rotated to an SPD precondition on the operator-instance contract. No new slice content; claims-only cycle. retroactive_claim_evidence below.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L4
    quoted_lines: |
      cg_step
        :: LinOp<S> -> Scalar -> CgState<S>
        -> { state: CgState<S>, residual_norm: Scalar }
      cg_step opA eps s =
        let p'    = if s.it == 0 then s.r
                                 else axpby 1.0 s.r (s.beta / s.beta_prev) s.p in
        let Ap    = apply opA p' in
        let alpha = s.beta / (dot Ap p') in
        ...
        let { final_state, trajectory }
              = iterate_while s0'
                  (\s -> s.it < config.max_it && not s.converged)
                  (\s -> cg_step opA eps s) in
  - claim_index: 1
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L4 (cg_solve return) + ## L3 ↔ L4 correspondence note 6
    quoted_lines: |
      { final_state, residual_history: trajectory.map(\t -> t.residual_norm) }
      Read: cg_solve returns both the converged iterate and the per-iteration residual history. If the caller reads .final_state only, the residual history is pruned — cg_step's residual_norm output is eliminated and the iteration runs without computing per-step residuals.
      6. Palace's print_opts.iterations-conditional residual logging corresponds to L4's residual_history consumption. Palace gates printing by a runtime flag; L4 gates *computation* by consumer demand.
  - claim_index: 2
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L4 Variant: preconditioned CG + Equivalence note
    quoted_lines: |
      pcg_step
        :: LinOp<S> -> LinOp<S> -> Scalar -> PCgState<S>
        -> { state: PCgState<S>, residual_norm: Scalar }
      ...
      Equivalence note. pcg_step opA Identity eps s (where Identity : LinOp<S> returns its argument unchanged) is observably equal to cg_step opA eps s' where s' is s with the z field projected out... Formally: define forget_z : PCgState<S> → CgState<S> as the projection that drops z; then pcg_step opA Identity eps ≡ cg_step opA eps ∘ forget_z modulo the z field's no-op write-back.
  - claim_index: 3
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1 (check_dot note) + ## Working Notes (CheckDot modeling)
    quoted_lines: |
      check_dot (Palace's CheckDot, palace/linalg/iterative.cpp:244-250) is a partial-function guard at each new inner-product site: it aborts execution if the result is non-finite or, on real SPD systems, negative (signalling loss of positive-definiteness). L1 surfaces it as a check_dot β' assertion; at L4 the guard maps to the precondition β > 0 on cg_step's call-site, not a runtime branch in the pure-functional form.
      CheckDot modeling. Palace's CheckDot... Modeled at L1 as check_dot β' partial-function guard; at L4 as a precondition on the SPD assumption (no runtime branch in the pure form).
- Verdict: pass.
- Friction: none.
- Structural change: applied: 3 lesson(s); 4 rotation_claim(s).
