---
agent: layer-intro-author
invoked_at: 2026-06-05T072032Z
scope: P1 typed-edge campaign — type the navigational container pages (layer/lowering indexes + group-intros + feature group pages) + DECIDE the index/intro node-status convention
status: pending
integrated_at: 2026-06-05T085500Z
integration_commit: INTEGRATION_SHA_PLACEHOLDER
integration_notes: >
  Applied clean (cycle-103 D5, staging row 6 — P1 typed-edge campaign container pages).
  35 container pages typed kind: navigational-container (no rank, reference-only): all 8 layer
  indices + 4 lowering indices + feature Part index + 3 feature-group pages + 23 L*/...-intro
  group-intros. The L4/index.md edit is FRONTMATTER ONLY (lines 1-11), byte-disjoint from D8's
  §Vocabulary-cohort prose surface. All-pass clean (critic set ready directly, no repair phase).
  Build green (mdBook strips frontmatter). step-5b rank_violations: 0 (0 of 35 carry rank or
  depends-on, vacuous; untyped 142->107 from this dispatch alone, -35). Opened OQ
  linter-outside-dag-misses-group-intro-container-pages (the 23 group-intros shift to
  detritus_with_typed_edges noise; fix = recognize kind: navigational-container, folds with D4's
  gap; routed to meta-phase/tools) + container node-status closure note for meta ratify.
---

# CYCLE: P1 typed-edge — navigational container pages + node-status convention

## Summary

Cycle-103 D5, graded-stack typed-edge campaign (P1, first tranche). Types **35 navigational
container pages** with `edges:` frontmatter and DECIDES + records the **container node-status
convention** that scheme §4/§5 carved out as an OQ (`graded-stack-index-and-concept-node-status`).

**The convention decision (authoritative — for the scheme page / meta-phase to RATIFY):**

> **Index pages and group-intro pages are navigational CONTAINERS, NOT vocabulary DAG nodes.**
> A container carries:
> - **NO `rank:`** — it makes no resolution claim and is not a member of the resolution total
>   order. (An index's firmness is not a meaningful quantity; its members carry their own ranks.)
> - **`edges: reference:` only** — pointing at the chapters it indexes (its *direct* SUMMARY.md
>   children). **No `depends-on`**: an index neither blocks on nor is blocked by its members, and
>   per scheme §3 a `reference` edge *constrains no rank and carries no liveness* — which is
>   exactly right, because an index must **not** keep dead vocabulary alive (a chapter is live
>   because a *feature root* transitively depends-on it, never because an index lists it).
> - **`kind: navigational-container`** documentation tag (with a parenthetical sub-kind:
>   `layer index` / `lowering index` / `feature Part index` / `group intro` / `feature group
>   intro`) so the page is explicitly self-identifying as outside the subject DAG.

This is the **fully scheme-aligned** reading of §4 ("an `L_n/index.md` is a navigational overview,
not a DAG leaf node carrying claims; its dep-map *table* is a derived view") and §5 (index pages
"methodology/orientation surfaces"). The linter **already anticipates it**: `is_likely_outside_dag()`
(`tools/graded-stack-lint/graded_stack_lint.py:637`) classifies `*/index` and the four
`FEATURE_NON_COLUMN` feature group pages as expected-unreachable. Typing them with `reference`-only
edges flips them from `untyped` (a WARNING) to typed **without** making them rank nodes or
reachability sinks — net measurable P1 progress with zero new rank obligations.

**Member-set derivation.** Each container references its **direct SUMMARY.md children** (the next
navigation level down), so the typed edges exactly mirror the authoritative nav tree:
- layer index (L1/L2/L3/L4) → its kind-group-intro pages;
- flat lowering index (L4-L3/L3-L2/L2-L1) → its theme-leaf chapters directly;
- L1-L0 index → its 3 theme-group-intro pages;
- feature/index → the 3 feature group pages (spine-root, driver-leaf, output-product);
- each group-intro / feature group page → its leaf chapters.

**Verification.** All 35 container files exist; all **230** `reference` edge targets resolve to
real on-disk `.md` files (checked programmatically against SUMMARY.md + the filesystem). A graph
simulation (building the linter's graph in-process with the proposed frontmatter applied) confirms:
**untyped 142 → 107 (−35)**, **0 rank violations** (containers carry no `rank:`), build-safe (YAML
frontmatter mdBook strips; no link or content change). The H1 title line is preserved verbatim in
every block.

**Same-file partition (D8, WAVE 2).** This dispatch touches ONLY the `book/src/L4/index.md`
**frontmatter** (a prepend ABOVE the `# L4 — Top of the stack` H1, top of file). It does **NOT**
touch the mid-file §Vocabulary-cohort bullets / count — that is D8's exclusive surface. The two
edits are at non-overlapping anchors (frontmatter prepend vs. mid-file prose). Same partition holds
for any sibling that touches the body of another index I type here: I write only the top-of-file
`edges:` frontmatter, never the prose body.

**Divergence-risk flag for the batch-close meta-phase unify** (siblings D1/D2/D3 decide concept-page
node-status; D4 decides `concepts/index`): my container convention and D4's `concepts/index` decision
must agree — `concepts/index` is a navigational container by the identical argument (it indexes the
concept library, makes no claim), so it should take the SAME `kind: navigational-container` +
`reference`-only treatment. If D4 instead ranks `concepts/index`, that is a divergence the meta-phase
should reconcile toward the container reading. (I do NOT touch `concepts/index` — D4's surface.) The
record-definition concept pages D1/D2/D3 handle ARE real DAG nodes (scheme §5) — no conflict there;
the only alignment point is the *index/container* pages.

## Proposed changes

```edit:book/src/L1/index.md
[old]:
# L1 — Mutation-lifted forms
[new]:
---
kind: navigational-container (layer index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/blas1-elementwise-intro
    - L1/operator-application-intro
    - L1/constructed-operator-gates-intro
    - L1/krylov-least-squares-intro
    - L1/nep-interior-intro
    - L1/fe-assembly-intro
    - L1/fe-space-intro
---

# L1 — Mutation-lifted forms
```

```edit:book/src/L2/index.md
[old]:
# L2 — Algebraic decompositions
[new]:
---
kind: navigational-container (layer index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/step-kernels-intro
    - L2/folds-intro
    - L2/fold-family-stubs-intro
    - L2/named-compositions-intro
    - L2/elementwise-gate-floors-intro
---

# L2 — Algebraic decompositions
```

```edit:book/src/L3/index.md
[old]:
# L3 — Global tensor-field operations
[new]:
---
kind: navigational-container (layer index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/blas1-intro
    - L3/elementwise-intro
    - L3/operator-apply-intro
    - L3/smoother-intro
    - L3/solver-caps-intro
---

# L3 — Global tensor-field operations
```

```edit:book/src/L4/index.md
[old]:
# L4 — Top of the stack
[new]:
---
kind: navigational-container (layer index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4/iteration-combinators-intro
    - L4/data-algebra-combinators-intro
    - L4/outer-driver-combinators-intro
---

# L4 — Top of the stack
```

```edit:book/src/L1-L0/index.md
[old]:
# L1 > L0 — Lowering layer
[new]:
---
kind: navigational-container (lowering index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1-L0/mutation-rotation-intro
    - L1-L0/construction-rotation-intro
    - L1-L0/obstruction-intro
---

# L1 > L0 — Lowering layer
```

```edit:book/src/L2-L1/index.md
[old]:
# L2 > L1 — Lowering layer
[new]:
---
kind: navigational-container (lowering index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2-L1/chebyshev-iteration-fusion
    - L2-L1/deflate-composition-lowering
    - L2-L1/divfree-projector-leaf-identity
    - L2-L1/eigsolve-spectral-transform-composition
    - L2-L1/gram-fold-specialization
    - L2-L1/incremental-least-squares-composition-lowering
    - L2-L1/inner-product-fold-specialization
    - L2-L1/krylov-step-kernel-defusion
    - L2-L1/ksp-solve-outer-driver-unfold
    - L2-L1/linear-combination-fold-specialization
    - L2-L1/orthogonalize-composition-lowering
---

# L2 > L1 — Lowering layer
```

```edit:book/src/L3-L2/index.md
[old]:
# L3 > L2 — Lowering layer
[new]:
---
kind: navigational-container (lowering index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3-L2/chebyshev-nested-recurrence
    - L3-L2/eigsolve-opaque-eigen-iteration
    - L3-L2/fold-solve-time-step-body
    - L3-L2/krylov-step-body-identity
    - L3-L2/ksp-solve-outer-driver
    - L3-L2/orthogonalize-variant-split
---

# L3 > L2 — Lowering layer
```

```edit:book/src/L4-L3/index.md
[old]:
# L4 > L3 — Lowering layer
[new]:
---
kind: navigational-container (lowering index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4-L3/bc-elimination-post-composition-dissolution
    - L4-L3/fe-assemble-fold-dissolution
    - L4-L3/fgmres-inner-loop-iterate-while-migration
    - L4-L3/fold-solve-time-step-dissolution
    - L4-L3/frequency-sweep-dissolution
    - L4-L3/gmres-inner-loop-iterate-while-migration
    - L4-L3/iterate-while-dissolution
    - L4-L3/iterate-while-with-prev-dissolution
    - L4-L3/krylov-step-typed-wrapper-dissolution
    - L4-L3/ksp-solve-driver-dissolution
    - L4-L3/solve-family-map-dissolution
---

# L4 > L3 — Lowering layer
```

```edit:book/src/feature/index.md
[old]:
# Feature surfaces — entry points
[new]:
---
kind: navigational-container (feature Part index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/spine-root
    - feature/driver-leaf
    - feature/output-product
---

# Feature surfaces — entry points
```

```edit:book/src/feature/spine-root.md
[old]:
# Feature surfaces — spine ROOT (lifecycle)
[new]:
---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/lifecycle.L4
    - feature/lifecycle.L1
    - feature/lifecycle.L0
---

# Feature surfaces — spine ROOT (lifecycle)
```

```edit:book/src/feature/driver-leaf.md
[old]:
# Feature surfaces — driver-leaf columns
[new]:
---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/boundary-mode.L4
    - feature/boundary-mode.L1
    - feature/boundary-mode.L0
    - feature/driven.L4
    - feature/driven.L1
    - feature/driven.L0
    - feature/eigenmode.L4
    - feature/eigenmode.L1
    - feature/eigenmode.L0
    - feature/electrostatic.L4
    - feature/electrostatic.L1
    - feature/electrostatic.L0
    - feature/magnetostatic.L4
    - feature/magnetostatic.L1
    - feature/magnetostatic.L0
    - feature/transient.L4
    - feature/transient.L1
    - feature/transient.L0
---

# Feature surfaces — driver-leaf columns
```

```edit:book/src/feature/output-product.md
[old]:
# Feature surfaces — output-product columns
[new]:
---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/capacitance.L4
    - feature/capacitance.L1
    - feature/capacitance.L0
    - feature/eigenfrequency-qfactor.L4
    - feature/eigenfrequency-qfactor.L1
    - feature/eigenfrequency-qfactor.L0
    - feature/energy-fields.L4
    - feature/energy-fields.L1
    - feature/energy-fields.L0
    - feature/inductance.L4
    - feature/inductance.L1
    - feature/inductance.L0
    - feature/sparameters.L4
    - feature/sparameters.L1
    - feature/sparameters.L0
---

# Feature surfaces — output-product columns
```

```edit:book/src/L1/blas1-elementwise-intro.md
[old]:
# L1 — BLAS-1 & elementwise
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/axpby
    - L1/axpbypcz
    - L1/axpy
    - L1/bilinear-form
    - L1/dot
    - L1/eigenvalue-untransform
    - L1/elementwise_product
    - L1/matrix-weighted-norm
    - L1/normalize
    - L1/nrm2
    - L1/participation_ratio
    - L1/reciprocal
    - L1/scal
---

# L1 — BLAS-1 & elementwise
```

```edit:book/src/L1/operator-application-intro.md
[old]:
# L1 — Operator application & assembly
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/apply_linop
    - L1/assemble-diagonal
    - L1/assemble_frequency_operator
    - L1/port_projection
---

# L1 — Operator application & assembly
```

```edit:book/src/L1/constructed-operator-gates-intro.md
[old]:
# L1 — Constructed-operator gates
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/chebyshev-smoother
    - L1/divfree-projector
    - L1/eigsolve
    - L1/floquet-correction
    - L1/jacobi-smoother
    - L1/ksp_solve
---

# L1 — Constructed-operator gates
```

```edit:book/src/L1/krylov-least-squares-intro.md
[old]:
# L1 — Krylov least-squares leaves
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/back_solve
    - L1/ls-update-column
    - L1/orthogonalize
---

# L1 — Krylov least-squares leaves
```

```edit:book/src/L1/nep-interior-intro.md
[old]:
# L1 — Dense-coordinate & NEP interior atoms
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/apply_nonlinear_pencil
    - L1/lu_solve
    - L1/nleps_deflated_residual
    - L1/nleps_deflated_solve
    - L1/nleps_eigenvalue_correction
    - L1/nleps_jacobian_action
---

# L1 — Dense-coordinate & NEP interior atoms
```

```edit:book/src/L1/fe-assembly-intro.md
[old]:
# L1 — FE-assembly sub-spine
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/fe_assemble
    - L1/weak_form_term
---

# L1 — FE-assembly sub-spine
```

```edit:book/src/L1/fe-space-intro.md
[old]:
# L1 — FE-space sub-spine
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1/essential_dofs
    - L1/fe_collection
    - L1/fe_space
---

# L1 — FE-space sub-spine
```

```edit:book/src/L2/step-kernels-intro.md
[old]:
# L2 step kernels
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/chebyshev-iteration
    - L2/krylov-step
---

# L2 step kernels
```

```edit:book/src/L2/folds-intro.md
[old]:
# L2 fold combinators
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/gram
    - L2/inner_product
    - L2/linear_combination
---

# L2 fold combinators
```

```edit:book/src/L2/fold-family-stubs-intro.md
[old]:
# L2 fold-family specialization / consumer stubs
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/axpby
    - L2/axpbypcz
    - L2/axpy
    - L2/dot
    - L2/nrm2
    - L2/scal
---

# L2 fold-family specialization / consumer stubs
```

```edit:book/src/L2/named-compositions-intro.md
[old]:
# L2 named compositions
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/deflate
    - L2/eigsolve
    - L2/incremental-least-squares
    - L2/ksp_solve
    - L2/orthogonalize
---

# L2 named compositions
```

```edit:book/src/L2/elementwise-gate-floors-intro.md
[old]:
# L2 elementwise & gate floors
[new]:
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
```

```edit:book/src/L3/blas1-intro.md
[old]:
# BLAS-1 vocabulary (L3)
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/axpby
    - L3/axpbypcz
    - L3/axpy
    - L3/dot
    - L3/inner_product
    - L3/linear_combination
    - L3/nrm2
    - L3/scal
---

# BLAS-1 vocabulary (L3)
```

```edit:book/src/L3/elementwise-intro.md
[old]:
# Elementwise field operations (L3)
[new]:
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
```

```edit:book/src/L3/operator-apply-intro.md
[old]:
# Operator application & introspection (L3)
[new]:
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
```

```edit:book/src/L3/smoother-intro.md
[old]:
# Smoothers & projector gates (L3)
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/chebyshev
    - L3/divfree-projector
    - L3/jacobi-smoother
---

# Smoothers & projector gates (L3)
```

```edit:book/src/L3/solver-caps-intro.md
[old]:
# Solver capabilities & field transitions (L3)
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/eigsolve
    - L3/fold_solve
    - L3/krylov-step
    - L3/ksp_solve
    - L3/orthogonalize
---

# Solver capabilities & field transitions (L3)
```

```edit:book/src/L4/iteration-combinators-intro.md
[old]:
# L4 — Iteration & step combinators
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4/chebyshev
    - L4/iterate-while
    - L4/iterate-while-with-prev
    - L4/krylov-step
---

# L4 — Iteration & step combinators
```

```edit:book/src/L4/data-algebra-combinators-intro.md
[old]:
# L4 — Data-algebra combinators & named verbs
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4/assemble_frequency_operator
    - L4/domain_energy_reduce
    - L4/dot
    - L4/eigenfreq_qfactor_reduce
    - L4/eliminate_bc
    - L4/fe_assemble
    - L4/gram_reduce
    - L4/inner_product
    - L4/linear_combination
    - L4/nrm2
    - L4/sparameter_reduce
---

# L4 — Data-algebra combinators & named verbs
```

```edit:book/src/L4/outer-driver-combinators-intro.md
[old]:
# L4 — Outer-driver caps & coordination combinators
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L4/eigsolve
    - L4/fold_solve
    - L4/frequency_sweep
    - L4/ksp_solve
    - L4/preconditioning-framework
    - L4/solve_family
---

# L4 — Outer-driver caps & coordination combinators
```

```edit:book/src/L1-L0/mutation-rotation-intro.md
[old]:
# L1 > L0 — Mutation-rotation themes
[new]:
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
```

```edit:book/src/L1-L0/construction-rotation-intro.md
[old]:
# L1 > L0 — Construction-rotation themes
[new]:
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
```

```edit:book/src/L1-L0/obstruction-intro.md
[old]:
# L1 > L0 — Obstruction themes
[new]:
---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L1-L0/bicgstab-iteration
    - L1-L0/fe-assemble-libceed-boundary-obstruction
    - L1-L0/minres-iteration
    - L1-L0/triangular-solve-obstruction
---

# L1 > L0 — Obstruction themes
```


## Supporting evidence

- **Authoritative scheme**: `book/src/methodology/graded-stack-scheme.md` §4 (index pages are a
  derived navigational view, carved out as a P1 sub-task + OQ), §5 ("Index pages — methodology /
  orientation surfaces … not a DAG leaf node"); `METHODOLOGY-GRADED-STACK.md` §3 (`depends-on` vs
  `reference`: a `reference` edge "constrains nothing; does not carry liveness — a mere mention must
  not keep dead vocabulary alive"), §2d (boundary of the graph; orientation pages document the
  construction, not nodes in it).
- **Linter already anticipates the container convention**: `tools/graded-stack-lint/graded_stack_lint.py`
  `is_likely_outside_dag()` (lines 637–647) treats `*/index` and `FEATURE_NON_COLUMN`
  (`feature/{driver-leaf,output-product,spine-root,index}`) as expected-unreachable, and `untyped`
  (line 502) is false as soon as ANY edge (incl. `reference`) is read. So `reference`-only typing is
  the linter-intended shape for these pages.
- **Member sets derived from SUMMARY.md** (the authoritative nav tree): each container's `reference`
  targets are its direct nav children. 35 containers, 230 reference edges, all targets verified present.
- **Edge-target existence**: programmatic check — 0 missing of 230 targets + 35 container files.
- **Rank/untyped/violation deltas**: in-process linter-graph simulation with the proposed frontmatter
  applied: untyped 142→107 (−35), rank_violations 0→0.

## Open questions / caveats

- **`record-…-needs-definition-home`**: none. Container pages name no records in signatures; this
  tranche introduces no record-definition obligation.

- **FINDING / OQ — linter detritus-classification gap for group-intro container pages** (route to
  meta-phase; `tools/` is meta-phase write-authority, NOT mine). After typing, the **9 layer/lowering
  indexes + 3 feature group pages** correctly land in `expected_unreachable_outside_dag` (covered by
  `is_likely_outside_dag`'s `*/index` + `FEATURE_NON_COLUMN` rules). But the **23 group-intro pages**
  (`L*/...-intro`, `L1-L0/...-intro`) are NOT recognized by `is_likely_outside_dag` — they have no
  `/index` suffix and are not in `FEATURE_NON_COLUMN` — so once typed (not-untyped) and unreachable
  (a `reference` edge propagates no mark) they would be reported as **`detritus`**. This is **lint
  NOISE, not a failure** (the exit code trips only on rank violations; detritus is informational),
  but it is *misleading* — a navigational container is correctly expected-unreachable, not garbage.
  **Recommended linter refinement** (meta-phase): extend `is_likely_outside_dag` to treat any page
  carrying `kind: navigational-container` (the explicit, robust signal I introduce here) — or, less
  robustly, the `-intro` suffix — as outside-DAG / expected-unreachable. Keying off the
  `kind: navigational-container` frontmatter tag is preferred (suffix-matching is brittle; the tag is
  the intended self-identification). This is the natural co-landing follow-up to ratifying the
  container convention. The 23-page detritus listing is cosmetic and self-resolves the moment the
  linter recognizes the tag; my frontmatter needs no change.

- **OQ `graded-stack-index-and-concept-node-status` — DECIDED for the container half** (index/intro
  pages = navigational containers, `reference`-only, no `rank:`, `kind: navigational-container`). The
  **concept-page half** is decided by sibling D1/D2/D3 (record-definition pages are DAG nodes per §5;
  narrative/meta concept pages are outside-DAG) and the `concepts/index` half by D4. Flag for the
  batch-close meta-phase unify: ensure `concepts/index` takes the **same** container treatment as the
  layer indexes (it indexes the concept library and makes no claim) — a divergence to reconcile if D4
  ranks it. No conflict on the record-definition pages.

- **`kind:` value carries a parenthetical sub-kind** (e.g. `navigational-container (layer index)`).
  The linter reads `kind` only to test `== "feature-surface"` (line 418), so the parenthetical is
  harmless today; if a future linter pass wants to switch on the sub-kind it can split on `(`. Flagged
  so the meta-phase can decide whether to normalize the tag to a bare `navigational-container` + a
  separate `container_kind:` field (a cosmetic choice; I kept the inline parenthetical for human
  readability, matching the existing `composes:` free-text-qualifier style).

- **No `depends-on` edges authored on any container** — deliberate, per the convention. If a later
  consumer of the linter wants an index→members *blocking* edge for some traversal, that would be a
  scheme change (it would wrongly make index pages keep vocabulary alive); flagged but not anticipated.

- **L0 lazy tail, `concepts/index`, `design/index`, `meta-reviews/index`, `SUMMARY`, `introduction`,
  `methodology/`, `design/`** were explicitly out of scope this tranche and are untouched.
