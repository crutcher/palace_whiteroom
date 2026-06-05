---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/assemble-diagonal
    - L2/divfree-projector
    - L2/elementwise_product
    - L2/jacobi-smoother
    - L2/normalize
    - L2/reciprocal
---

# L2 elementwise & gate floors

Standalone same-named L2 entries under firm L3 entries with **NO fold combinator** to defer
to: standalone elementwise leaves, a fused norm-then-rescale composite, and constructed-operator
/ operator-to-data gates. Having no fold-parent, each stays a **full standalone entry** (no
specialization-stub reduction applies). Most are thin identity-in-form floors; `divfree-projector`
carries one genuine `AddMult` apply-accumulate de-fusion.

Elementwise leaves / composite (no fold-parent):

- [`reciprocal`](./reciprocal.md) — the nonlinear elementwise multiplicative-inverse
  self-map (`y[i] = 1/x[i]`; `1/(a+b) ≠ 1/a + 1/b`).
- [`elementwise_product`](./elementwise_product.md) — the Hadamard binary field op
  (`a ⊙ b`); the inverse-subsumption generalisation of `scal`.
- [`normalize`](./normalize.md) — the fused norm-then-rescale composite
  `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, returning **both** the norm and the unit
  vector; consumes the `nrm2` + `scal` stubs but is itself fork-independent (no fold-parent).

Constructed-operator / operator-to-data gates:

- [`assemble-diagonal`](./assemble-diagonal.md) — the operator-to-data diagonal-extraction
  primitive (`A → diag(A)`); the operator-to-data sibling of `apply_linop` (NOT a variant);
  the load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law is preserved
  through the floor.
- [`jacobi-smoother`](./jacobi-smoother.md) — the **thinnest** constructed-operator gate
  (apply `op.dinv ⊙ x`, one elementwise product); the fusion rotation is **negative**.
- [`divfree-projector`](./divfree-projector.md) — the divergence-free Helmholtz-projection
  gate (fixed four-step `WeakDiv → Z_{bdr_eff} → ksp_solve → Grad`); the one genuine
  `AddMult` apply-accumulate de-fusion; direct L2 dep `ksp_solve` carrying its
  `sequential-obstruction` by reference.

All six `firm`. Chapters are alphabetical.
