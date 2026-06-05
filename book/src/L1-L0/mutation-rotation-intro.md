---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1-L0/apply-linop-mutation-rotation
    - L1-L0/apply-nonlinear-pencil-mutation-rotation
    - L1-L0/assemble-diagonal-mutation-rotation
    - L1-L0/assemble-frequency-operator-rotation
    - L1-L0/axpby-mutation-rotation
    - L1-L0/axpbypcz-mutation-rotation
    - L1-L0/back-solve-mutation-rotation
    - L1-L0/bilinear-form-mutation-rotation
    - L1-L0/chebyshev-smoother-mutation-rotation
    - L1-L0/divfree-projector-mutation-rotation
    - L1-L0/dot-mutation-rotation
    - L1-L0/eigsolve-convergence-reason-mapping
    - L1-L0/eigsolve-mutation-rotation
    - L1-L0/floquet-correction-mutation-rotation
    - L1-L0/jacobi-smoother-mutation-rotation
    - L1-L0/ksp-solve-mutation-rotation
    - L1-L0/ls-update-column-mutation-rotation
    - L1-L0/lu-solve-mutation-rotation
    - L1-L0/matrix-weighted-norm-mutation-rotation
    - L1-L0/nleps-deflated-residual-mutation-rotation
    - L1-L0/nleps-deflated-solve-mutation-rotation
    - L1-L0/nleps-eigenvalue-correction-mutation-rotation
    - L1-L0/nleps-jacobian-action-mutation-rotation
    - L1-L0/normalize-mutation-rotation
    - L1-L0/nrm2-mutation-rotation
    - L1-L0/orthogonalize-mutation-rotation
    - L1-L0/reciprocal-elementwise-product-mutation-rotation
    - L1-L0/scal-mutation-rotation
---

# L1 > L0 — Mutation-rotation themes

The bulk of the L1>L0 lowering: themes that rewrite a pure-functional L1 form into its L0 in-place-mutation C++ source pattern. The recurring rewrite shapes are the ones the Part overview names — in-place axpy as `x.Add(α, y)`, operator application as `A.Mult(x, y)` (output-arg convention), workspace-buffer reuse as mention-and-erase, and the constructed-operator absorption rules (timer erase, warning-to-structured-field, counter-to-driver-accumulator, destination-binding). Each theme carries `palace/<file>.cpp:<lines>` evidence and records load-bearing numerical tricks (pinned reduction-tree non-associativity, descending back-substitution order) as explicit non-laws.

Themes are listed alphabetically.
