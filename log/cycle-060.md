## 2026-05-25 cycle-60 — back divfree — pass

- Synthesis: Retroactive L0→L1 rotation_claim for divfree slice. The slice already has L1, L2, L3, L4 content on disk (cycles prior to this audit); the producer-side claim for the L0→L1 edge was missing. Plan_kind=retroactive_claims with retroactive_claim_evidence below.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/divfree.md
    section: ## L1
    quoted_lines: |
      ### Defining condition
      A `DivFreeSolver` represents the discrete projector `P` onto the
      divergence-free subspace of an Nedelec field, defined by
          Gᵀ M (P x) = 0
      where
      - `G : H1 → Nedelec` is the discrete gradient (the H1→Nedelec interpolator),
      - `M : H1 → H1` is the ε-weighted H1 mass-like operator

      ### Apply (`P x → y`)
      1. Form the H1 residual:        `rhs ← WeakDiv · y`.
      2. Impose essential BC on rhs:  zero entries of `rhs` on `bdr_tdof_list_M`.
      3. Solve the projected system:  `M · ψ = rhs`         via `ksp`.
      4. Apply the gradient correction: `y ← y + Grad · ψ`.

      ## Variant axes (absorption status)
      - **VecType ∈ {Vector, ComplexVector}.** Parametric absorption.
      - **H1 hierarchy depth = 1 vs > 1.** Constructed-operator absorption.
      - **Boundary-dof list empty vs non-empty.** Absorbed at construction.

The quoted prose supports the claim: it names the defining condition (state-hiding via the Gᵀ M P = 0 mathematical identity), surfaces the four role-named steps (the procedural form hides the BilinearForm machinery), preserves the sign convention as an explicit L1 invariant (+Grad·ψ), and explicitly catalogs the three variant absorptions matching the rotation criteria.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 lesson(s); 1 rotation_claim(s).
