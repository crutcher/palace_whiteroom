---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/elementwise_product
    - L3/normalize
    - L3/reciprocal
---

# Elementwise field operations (L3)

Whole-tensor element-local self-maps and the one fused composite — all at the **obstruction-free end** of the L3 obstruction-profile spectrum (`index.md` §Semantics): embarrassingly parallel, no loop-recurrence introduced at L3.

- [`elementwise_product`](./elementwise_product.md) — the whole-tensor Hadamard binary product `a ⊙ b`; the Hadamard floor of the cohort, the operator-action realisation of a diagonal operator; sibling-subsumes `scal`. Firm-on-positive-structure, carries NO obstruction.
- [`reciprocal`](./reciprocal.md) — the whole-tensor multiplicative-inverse self-map `x -> (1/x[i])ᵢ`; the `D⁻¹`-forming step of the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner-apply chain. **Nonlinear**, **partial** at `x[i]=0`.
- [`normalize`](./normalize.md) — the fused norm-then-rescale `x -> (β, x/β)` with `β = nrm2(x)`; the only **fused composite** of the cohort (genuine same-layer `nrm2`/`scal` deps), exemplifying the **fused-composite-obstruction-free** profile — both constituents are individually obstruction-free, so the composite authors no loop. The returned norm is load-bearing (Arnoldi sub-diagonal / eigenvalue estimate / NEP deflation companion-scale); **partial** at `x=0`.

Each operator's substantive rotation lives at L1>L0; the L3>L2 edge is an in-line identity-in-form §"Downward to L2" note (no theme file).

See `index.md` §"Operator dep-map → Elementwise field operations" for the per-operator detail.
