## 2026-05-25 cycle-67 — forward cg [L4→L4] — pass

- Synthesis: Retroactive rotation_claim for the L4 v0.3→v0.4 derived-view-hoisting self-rotation already documented in cg.md's '## L4 v0.4 — derived-view hoisting' section. The slice already carries the v0.4 narrative naming the state-hiding decision; this cycle emits the missing rotation_claim that audits it, plus a lessons line and a dep-map edge connecting cg to the derived-view-hoisting concept. retroactive_claim_evidence below.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L4 v0.4 — derived-view hoisting (self-rotation)
    quoted_lines: |
      Per `book/src/concepts/rotation.md` criterion (a) *state hiding*: the scalar `res = sqrt|beta|` is hoisted from "hypothetical iteration-state field" to "step-output field, demand-pruned per L4 calculus §3.8".

      A candidate v0.2-style schema would include `res: Scalar` in `CgState`/`PCgState` and require the step to maintain the invariant `s.res == sqrt|s.beta|` on every transition. v0.4 (= v0.3 schema, re-justified) eliminates the field:

          // Rejected v0.2-style schema (load-bearing field that defeats §3.8 pruning)
          CgState = { x, r, p, beta, beta_prev, res, it, converged }
                     with invariant res == sqrt|beta|

          // Adopted v0.3/v0.4 schema
          CgState = { x, r, p, beta, beta_prev, it, converged }
          step returns { state: CgState, residual_norm: Scalar }

      The rotation is observable in three places: (1) State schema — `CgState`/`PCgState` carry `beta` only; `res` is not a field. (2) Step body — `let res' = sqrt (abs beta')` is a step-local binding that flows into the step's *return record* (`residual_norm: res'`), not into the next state. (3) Step output record — `{ state, residual_norm }` separates iteration-threaded state from step-observable outputs. The split makes pruning targetable.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s), 1 lesson(s); 1 rotation_claim(s).
