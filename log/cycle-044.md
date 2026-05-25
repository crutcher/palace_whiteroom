## 2026-05-25 cycle-44 — forward chebyshev [L1→L2] — pass

- Synthesis: Chebyshev L1→L2 rotation_claims retroactive on the already-present `## L2 — primitive composition` section of `book/src/spec/slices/chebyshev.md`. The L2 section unfolds the L1 Richardson-like sweep into a sequence of named base primitives (`copy`, `zero`, `apply_linop(A,·)`, `axpy`, `elementwise_product`, `scal`) while preserving constructed-operator variant absorption: 4th-kind and 1st-kind share the same primitive sequence, differing only in the scalar generator `scalars(op, k)`. Per-edge rotation_claims cover (1) the residual unfold `r := x - A*y` → `copy`+`apply_linop`+`axpy`, (2) the initial-direction unfold `d := alpha_0 * dinv .* r` → `elementwise_product`+`scal`, (3) the inner-recurrence direction update `d := sd_k * d + sr_k * dinv .* r` → `elementwise_product`+`scal`+`axpy`, (4) the scalar-coefficient resolution from variant tag to closed-form (4th-kind) / three-term recurrence (1st-kind) `(alpha_0, sd_k, sr_k)`, and (5) the variant-absorption preservation at the primitive-sequence axis.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/chebyshev.md
    section: ## L2 — primitive composition / Apply primitives
    quoted_lines: |
      # 1. residual r = x - A y  (or r = x if !initial_guess on first sweep)
      if it == 1 and not initial_guess:
        r ← copy(x)
        zero(y)
      else:
        r ← copy(x)
        Ay ← apply_linop(op.A, y)
        axpy(-1, Ay, r)                         # r ← r - A y
  - claim_index: 1
    on_disk_path: book/src/spec/slices/chebyshev.md
    section: ## L2 — primitive composition / Apply primitives
    quoted_lines: |
      # 2. initial direction:  d = alpha_0 * dinv .* r
      a0 = scalars(op, 0).alpha_0
      d  ← elementwise_product(dinv, r)
      scal(a0, d)
  - claim_index: 2
    on_disk_path: book/src/spec/slices/chebyshev.md
    section: ## L2 — primitive composition / Apply primitives
    quoted_lines: |
      (sd, sr) = scalars(op, k)
      # d ← sd * d + sr * (dinv .* r)
      t ← elementwise_product(dinv, r)
      scal(sd, d)
      axpy(sr, t, d)
  - claim_index: 3
    on_disk_path: book/src/spec/slices/chebyshev.md
    section: ## L2 — primitive composition / Apply primitives
    quoted_lines: |
      scalars(op, k):
        if op.variant == 4th-kind:
          alpha_0 = 4/3 / op.lam_max
          sd_k    = (2k - 1) / (2k + 3)
          sr_k    = (8k + 4) / ((2k + 3) * op.lam_max)
        else:  # 1st-kind, three-term Chebyshev recurrence centered at theta
          alpha_0 = 1 / op.theta
          rho_k tracked across k: rho_0 = delta / (2*theta), then
            rho_k = 1 / (2*theta/delta - rho_{k-1}) for k >= 1
          sd_k    = rho_k * rho_{k-1}
          sr_k    = 2 * rho_k / op.delta
  - claim_index: 4
    on_disk_path: book/src/spec/slices/chebyshev.md
    section: ## L2 — primitive composition / Variant absorption at L2
    quoted_lines: |
      The primitive *sequence* in `apply_linop` is identical across variants. Only the scalar-generator `scalars(op, k)` branches on variant. This is the (c) primitive-sequence axis of variant absorption per `concepts/variant-absorption.md`, achieved here because both polynomial families admit a uniform `(alpha_0, sd_k, sr_k)` recurrence parameterization — 4th-kind via closed-form, 1st-kind via a `rho_k` scalar carried across `k`.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s); 5 rotation_claim(s).
