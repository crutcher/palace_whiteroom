---
rank: firm
kind: primitive
edges:
  depends-on: []
  reference:
    - concepts/state-stratification
    - L4/preconditioning-framework
    - L3/krylov_step
---
# counter-update

A small bookkeeping primitive denoting in-place increment of an integer counter held inside a solver-state bundle. Naming it as a distinct L2 primitive separates *iteration counters* (observability) from *iterates* (the mathematical state) so that the L4 monadic state schema can classify the counter cleanly as ephemeral observability rather than algorithmic state.

## L2 form

```
counter_update(c: &mut int, δ: int):
    c ← c + δ                              // in-place
```

The `&mut` notation marks the in-place mutation explicitly; the caller's surrounding code (e.g. `solver.counters.mult`) makes the storage location unambiguous.

## State classification

Counters tracked by `counter_update` belong to the **observability / diagnostic** stratum of [`state-stratification`](./state-stratification.md): they do not affect convergence or correctness of the iteration. The L4 monadic structure can carry them in a `Writer`-like effect, distinct from the algorithmic-state thread.

## Used by

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `solve` threads `counters.mult` / `counters.mult_it` via `modifyCounters` after the delegated iteration (§Signature body phase; Law 5 counter-monotonicity).
- Per-method slices wherever they track inner-iteration counts at L2.

## See also

- [`state-stratification`](./state-stratification.md) — the classification that justifies separating counter-update from algorithmic-state mutation.
