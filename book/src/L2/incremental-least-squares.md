# incremental-least-squares

> **Status: `stub`** — claim-free placeholder materialized 2026-05-28 (CLAUDE.md §Methodology invariants "Integration may materialize implied components as stubs"). Exists so converging forward-references resolve to a live home and the plan points at a real file. **No citations or semantic claims yet** — the next `harvester` refines it in place (`stub` → `rough-in` → `firm`).

## What this will be

The L2 composition consumed by GMRES's outer driver: the running-QR / Givens-rotation-stream small-dense **incremental least-squares** update (the Hessenberg-column LS solve threaded across iterations). Currently lives only as the concept page [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md); this entry lifts it to a first-class L2 composition (sibling to the [`orthogonalize`](./orthogonalize.md) L2 lift), naming variant axes (real / complex Givens) and the composition-level invariant `‖R·y − s‖² + |s[j+1]|² = ‖H̄·y − βe₁‖²`.

## Implied by

- [`L2/krylov-step`](./krylov-step.md) (names `incremental-least-squares` as a future L2 composition candidate) + [`L2/index`](./index.md) Working Notes.
- Plan (`scaffolding/priorities.md`) Backlog High-fan-out item **l2-named-composition-lifts**.
- OQ `incremental-least-squares-as-future-L2-firstclass-entry`; concept [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md).

## Refinement pending

- **Owner:** `harvester`.
- **Plan:** Backlog High-fan-out `l2-named-composition-lifts`.
- **OQs:** `incremental-least-squares-as-future-L2-firstclass-entry`, `gmres-givens-stream-as-step-kernel-borderline` (whether the Givens-stream is a `krylov-step` instance is decided here).
