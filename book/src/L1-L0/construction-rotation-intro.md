---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1-L0/essential-dofs-construction-rotation
    - L1-L0/fe-collection-construction-rotation
    - L1-L0/fe-operator-assemble-mutation-rotation
    - L1-L0/fe-space-construction-rotation
    - L1-L0/weak-form-term-rotation
---

# L1 > L0 — Construction-rotation themes

The FE-construction lowerings: themes that rewrite a pure declarative L1 construction value (a space, a collection schedule, an assembled operator, a weak-form term, an essential-dof set) into the imperative MFEM/Palace build sequence at L0. Each carries a **construction-lowers / bookkeeping-read-as-given split** — the Palace-side pairing / case-selection / schedule lowers here, while the MFEM-owned dof bookkeeping (numbering, ordering, conformity, prolongation/restriction) or the libCEED-owned per-term quadrature kernel is read-as-given at its boundary (the analogue of the libCEED-leaf boundary). These are genuine vocabulary translations — declarative value → imperative build loop — not 1:1 named-term renames.

Themes are listed alphabetically.
