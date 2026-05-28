# L2 > L1 — Lowering layer

The transformation from L2 (algebraic decompositions) to L1 (mutation-lifted forms). Batched by **themes**.

## Context

L1 forms are pure-functional but **structurally close to the source loop** — explicit input/output sets, in-place mutation patterns either erased (workspace) or preserved (semantically-meaningful aliasing). L2 unfolds these into composition of base primitives. The lowering captures the formal correspondence.

## Theme list

| theme | L2 anchor | L1 anchor | status |
|---|---|---|---|
| [chebyshev-iteration-fusion](./chebyshev-iteration-fusion.md) | `L2/chebyshev-iteration` (firm) | `L1/chebyshev-smoother` (firm) | firm *(algebraic; recurrence↔polynomial fusion)* |

## Working Notes

- Themes here are heavy with optimization-trick unfolding (transparent performance tricks like fusion, tiling, packing; load-bearing numerical tricks preserved).
