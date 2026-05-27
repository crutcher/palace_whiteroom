# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:
- `x.Add(α, y)` → `x_{k+1} = x_k + α·y`
- `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention)
- Iterative loop mutating iterate in place → functional unfold `state_{k+1} = step(state_k)`
- Reused workspace `tmp` → omitted (the COW backend handles allocation)

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style).

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |

## Working Notes

- L1 is what `abstractor` produces in early bottom-up sweeps (L0 → L1).
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content.
