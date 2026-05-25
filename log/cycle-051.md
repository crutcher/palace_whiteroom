## 2026-05-25 cycle-51 — back cg — pass

- Synthesis: Retroactive L0→L1 rotation_claims for cg.md v0.3: emitted 4 per-substitution claims (mutation-erasure with destination-renaming for AXPBY/Add/A->Mult/ApplyB; workspace-aliasing rename of p→p_tmp; CheckDot partial-function guard surfacing; faithful rendering of the !B-branch initial-residual quirk). retroactive_claim_evidence: 
  - claim_index: 0 (mutation-erasure)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines: |
      let r₀ = b - apply A x_in                    // A->Mult(x, r); AXPBY(1, b, -1, r)
      ...
      let p' = if it == 0 then z else axpby 1.0 z (beta/beta_prev) p
      let z'_pre = apply A p'                      // A->Mult(p, z)
      let x' = x + alpha · p'                      // x.Add(alpha, p)
      let r' = r - alpha · z'_pre                  // r.Add(-alpha, z)
      let z' = apply B r'                          // ApplyB(B, r, z); or z = r if !B
  - claim_index: 1 (workspace-aliasing rename)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1 (setup block) and Notes
    quoted_lines: |
      let p_tmp = apply B b                        // tmp use of p as Bb workspace
      sqrt |dot p_tmp b|                           // or Norml2(b) if !B
      ...
      - The `initial_guess` branch reuses `p` as scratch for computing `(Bb, b)`; L1 binds it to a local `p_tmp` since it is not the iteration's search direction.
  - claim_index: 2 (CheckDot guard surfacing)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1 Notes
    quoted_lines: |
      - `check_dot` (Palace's `CheckDot`, [palace/linalg/iterative.cpp:244-250](../../../../reference/palace/linalg/iterative.cpp#L244-L250)) is a partial-function guard at each new inner-product site: it aborts execution if the result is non-finite or, on real SPD systems, negative (signalling loss of positive-definiteness). L1 surfaces it as a `check_dot β'` assertion;
  - claim_index: 3 (initial-residual quirk faithful rendering)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1 Notes
    quoted_lines: |
      - **Initial-residual quirk in the no-preconditioner branch (`!B && initial_guess`).** Palace computes `beta_rhs = Norml2(b) = sqrt|(b,b)|` then sets `initial_res = sqrt|beta_rhs|`, yielding `initial_res = (b·b)^{1/4}` — not `‖b‖₂`. The preconditioned branch computes the correct `sqrt|(Bb, b)|`. L1 preserves Palace's source behavior; the L4 modeling and Working Notes flag this as a likely Palace bug.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 4 rotation_claim(s).
