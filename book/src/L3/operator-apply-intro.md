---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/apply_linop
    - L3/assemble-diagonal
---

# Operator application & introspection (L3)

The two opaque-operator-gate primitives at L3 — the matvec gate and its operator-to-data sibling. Both are leaf primitives whose L1 form is L3-native by signature shape (identity-in-form across the L3↔L1 edge); both sit at the **obstruction-free end** of the spectrum (apply / introspect is a single field op, no loop of any kind).

- [`apply_linop`](./apply_linop.md) — the linear-operator-application generalisation of "matvec": `(A: LinOp[(R: ...), (D: ...)], x: Tensor[$D]) -> Tensor[$R]` (named shape groups / operator shapes per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; range-first), square (`R ≡ D`) and rectangular, real and complex, all operator representations absorbed. The matvec gate consumed throughout the solver-caps cohort. Lowers L3→L1 directly (no interposed L2 entry — the by-design no-L3-L2-theme case).
- [`assemble-diagonal`](./assemble-diagonal.md) — the operator-to-data introspection primitive `(A: LinOp[(S: ...), $S]) -> Tensor[$S]` (`A -> diag(A)`, square operator — one shape group `S`); the operator-to-data sibling of `apply_linop`. Carries the load-bearing exact-vs-approximate (matrix-free) non-law as a representation-aware non-law.

See `index.md` §"Operator dep-map → Operator application & introspection" for the per-operator detail.
