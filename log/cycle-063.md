## 2026-05-25 cycle-63 — forward cg [L4→L4] — pass

- Synthesis: CG L4→L4 self-rotation: emit rotation_claim for the v0.4 state-schema tightening (derived-view hoisting of `res = sqrt|beta|` from CgState/PCgState to step-output `residual_norm`), already landed on-disk in the slice's `## L4 v0.4 — state-schema tightening` section. retroactive_claim_evidence quotes the on-disk prose; no new content writes this cycle.

retroactive_claim_evidence:
  - claim_index: 0
    on_disk_path: book/src/spec/slices/cg.md
    section: ## L4 v0.4 — state-schema tightening
    quoted_lines: |
      **v0.4 vs. v0.3 (this revision).** The L4 v0.3 form (above) stores `res` neither in `CgState` nor `PCgState` — it is computed inside `cg_step` / `pcg_step` and returned as the step-output `residual_norm`. **v0.4 is a no-op on the state schema** (the v0.3 form was already correct on this axis) and adds an explicit comment to that effect: `res` is a *derived view* of `beta` (specifically `sqrt|beta|`); storing it in the iteration state would duplicate `beta`'s information and create a redundant invariant the step must maintain (`s.res == sqrt|s.beta|`) on every transition.

      1. **State schema** — `CgState`/`PCgState` carry `beta` only; `res` is not a field. Saved: 1 scalar per state record × 2 schemas.
      2. **Step body** — `let res' = sqrt (abs beta')` is a step-local binding; it flows into the step's return record (`residual_norm: res'`), not into the next state's `res` field.
      3. **Step output record** — `{ state: CgState<S>, residual_norm: Scalar }` separates iteration-threaded state from step-observable outputs. The split makes pruning targetable.

      A reader looking at `CgState<S>` v0.4 cannot tell — and **does not need to know** — whether downstream consumers will read the residual history.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 2 lesson(s); 1 rotation_claim(s).
