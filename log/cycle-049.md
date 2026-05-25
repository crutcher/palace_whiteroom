## 2026-05-25 cycle-49 — back cg — pass

- Synthesis: Retroactive L0→L1 rotation_claims for the cg slice (slice already complete through L4 on disk). Quoted prose blocks from the existing ## L1 section support each claim; no new structural writes. retroactive_claim_evidence:
  - claim_index: 0 (mutation-erasure for x.Add/r.Add)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "let x' = x + alpha · p'                      // x.Add(alpha, p)
       let r' = r - alpha · z'_pre                  // r.Add(-alpha, z)"
      "The MFEM `Vector::Add(α, y)` mutates `x` in place; L1 names the resulting value `x'` and rebinds."
  - claim_index: 1 (AXPBY destination-erasure)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "let p' = if it == 0 then z else axpby 1.0 z (beta/beta_prev) p"
      "`linalg::AXPBY(α, x, β, y)` mutates `y` in place; L1 makes the destination explicit as the result of the call."
  - claim_index: 2 (operator output-buffer erasure)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "let z'_pre = apply A p'                      // A->Mult(p, z)"
      "let z' = apply B r'                          // ApplyB(B, r, z); or z = r if !B"
      "The L3 calls to `A->Mult` and `B->Mult` write into pre-allocated output buffers (`z`, `r`). In L1 those are erased — the calls become pure `apply A p → tensor` and `apply B r → tensor`."
  - claim_index: 3 (loop-as-iterate state-threading)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "iterate from (x = x₀, r = r₀, z = z₀, p = ⊥, beta = beta₀, beta_prev = 0, res = sqrt |beta₀|, it = 0):
         while it < max_it && !converged:
           ...
           continue with (x = x', r = r', z = z', p = p', beta = beta', beta_prev = beta, res = res', it = it')"
  - claim_index: 4 (CheckDot lifted to partial-function guard)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "check_dot beta'                                // partial-function guard; aborts on non-finite"
      "`check_dot` (Palace's `CheckDot`, …) is a partial-function guard at each new inner-product site: it aborts execution if the result is non-finite or, on real SPD systems, negative (signalling loss of positive-definiteness). L1 surfaces it as a `check_dot β'` assertion"
  - claim_index: 5 (initial-residual quirk preserved verbatim)
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L1
    quoted_lines:
      "Palace computes `beta_rhs = Norml2(b) = sqrt|(b,b)|` then sets `initial_res = sqrt|beta_rhs|`, yielding `initial_res = (b·b)^{1/4}` — not `‖b‖₂`. … L1 preserves Palace's source behavior"
- Verdict: pass.
- Friction: none.
- Structural change: none.
