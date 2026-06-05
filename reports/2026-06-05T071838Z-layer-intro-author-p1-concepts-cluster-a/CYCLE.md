---
agent: layer-intro-author
invoked_at: 2026-06-05T07:18:38Z
scope: graded-stack typed-edge campaign P1 tranche D1 — concepts/ cluster A (BLAS-1 / reduction / operator-application substrate), 16 pages
status: pending
integrated_at: 2026-06-05T085500Z
integration_commit: e9e6556d1fe709b77124731573eafa7a638c7497
integration_notes: >
  Applied clean (cycle-103 D1, staging row 2 — P1 typed-edge campaign concepts cluster A).
  16 concept pages got reference-only typed edges: frontmatter prepended (blas1/reduction/
  operator-application/lift substrate; trsv + set_subvector_zero carry reference: [] empty — no
  L1 home). All-pass clean (critic set ready directly, no repair phase). Build green. step-5b
  rank_violations: 0 (every edge is reference, no rank/liveness claim — vacuous). Opened 2 OQs
  (concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis; the D1/D3-vs-D2
  non-node frontmatter encoding divergence concept-non-node-frontmatter-encoding-reference-only-vs-empty,
  routed for meta unify).
---

# CYCLE: typed `edges:` for concepts/ cluster A (16 pages)

## Summary

Authors the canonical graded-stack `edges:` frontmatter onto the 16 cluster-A
concept pages (BLAS-1 / reduction / operator-application substrate). Per the
typed-edge scheme (`book/src/methodology/graded-stack-scheme.md` §2/§5 +
`METHODOLOGY-GRADED-STACK.md` §2d/§3), **every one of these 16 pages is a
narrative-pointer / methodology concept page** — the §5 category whose named
example is `concepts/dot.md`, which "sits **outside the subject DAG**
(`METHODOLOGY-GRADED-STACK.md` §2d) — no `rank:`". **None** is a
record-definition page (the only concept sub-case that IS a DAG node). So the
**node-status convention I apply uniformly**: each page is a **non-node**,
carries **NO `rank:`**, and its `edges:` block is **`reference`-only** (every
outbound book link is navigational — it constrains no rank and carries no
liveness, exactly per §2's rule that "a mere mention must not keep dead
vocabulary alive"). This realizes the dispatch's "a pure pointer page may be
marked a non-node / `reference`-only" path and OQ
`graded-stack-index-and-concept-node-status`.

**Why every down-edge to the authoritative L1 entry is `reference`, not
`depends-on`:** the L1 entry is the *definition*; the concept page is a pointer
*to* it. The blocking direction (if any) runs the other way and is already
typed on-disk — e.g. `L1/dot` (rank: firm) carries `edges: reference:
- concepts/dot` (a `reference` back-pointer), and crucially does NOT list
`concepts/dot` as a `depends-on`. A firm operator entry does not block on its
narrative-pointer concept page. So the concept→L1 edge is symmetric navigational
`reference`. **No page in this cluster is a load-bearing substrate that an
operator genuinely `depends-on`** (I judged each per the dispatch instruction):
they are all either pointer-to-definition pages (dot/nrm2/scal/axpy/apply_linop/
elementwise-product) or methodology/primitive-narrative pages
(variant-absorption / tensor-field-lift / the constructed-operator family).
Hence **zero `depends-on` edges, 100% `reference`** across the tranche — which
is the correct and expected outcome for a pure-pointer cluster, not an omission.

Down-pointers that target **L0 source ranges in `reference/`** (the BLAS
mappings, `iterative.cpp:669-706`, `orthog.hpp:51-53`, etc.) are NOT book nodes
and get NO edge — they remain prose citations. Three pages (`trsv`,
`set_subvector_zero`, `gemv_basis`) have **no L1 entry home** in the book at all
(`L1/trsv`, `L1/set_subvector_zero`, `L1/gemv_basis` do not exist); their
`edges:` therefore reference only sibling concepts / L2 / L3 nodes that DO
exist — no dangling `depends-on` is created (verified, see Supporting evidence).

## Node-status convention applied (recorded for batch-close unification with D4/D5)

- **Convention C-A:** a cluster-A concept page is a **non-node** — narrative
  pointer or methodology page, `METHODOLOGY-GRADED-STACK.md` §2d. It carries no
  `rank:`. It DOES carry an `edges:` block, but **`reference`-only** (the
  scheme's "no rank:/edges:" phrasing for the scheme page itself is the
  strictest reading; the operative `linkcheck`-relevant fact is that a non-node
  must not emit any `depends-on` edge, because a `depends-on` from a non-live
  non-node would either (a) be ignored by the GC anyway or (b) wrongly keep its
  target's liveness accounting confused. A `reference`-only block is the safe,
  informative encoding: it records the navigational wiring for the linters
  without asserting any blocking/liveness claim). If the batch-close meta-phase
  prefers **zero frontmatter** on non-node concept pages (strict §5 reading),
  these 16 blocks are trivially droppable — they assert nothing. I chose
  `reference`-only over empty because the dispatch explicitly asked for `edges:`
  typing and because it documents the see-also graph for the reachability-GC
  author without lying about liveness.
- **No page promoted to node status.** I found **no record-definition page** in
  the cluster (the one sub-case that would force `rank:` + node status). If
  D4/D5 conclude index/container pages ARE nodes, that does not retro-actively
  make these pointer pages nodes — they remain non-nodes by kind.

## Proposed changes

Each block prepends a `reference`-only `edges:` frontmatter to the page. `[old]`
is the verbatim current first line (the H1); `[new]` is the frontmatter + that
same H1.

```edit:book/src/concepts/dot.md
[old]: # dot
[new]: ---
edges:
  reference:
    - L1/dot                       # authoritative operator entry (definition); pointer-to, not blocking
    - L2/krylov-step               # use-site cross-link (CG/GMRES inner-product role)
---

# dot
```

```edit:book/src/concepts/nrm2.md
[old]: # nrm2
[new]: ---
edges:
  reference:
    - L1/nrm2                      # authoritative operator entry (definition)
    - L2/krylov-step               # use-site cross-link (residual norm / Arnoldi sub-diagonal)
---

# nrm2
```

```edit:book/src/concepts/scal.md
[old]: # scal
[new]: ---
edges:
  reference:
    - L1/scal                      # authoritative operator entry (definition)
    - L2/krylov-step               # use-site cross-link (basis normalization / search-dir rescale)
---

# scal
```

```edit:book/src/concepts/axpy.md
[old]: # axpy
[new]: ---
edges:
  reference:
    - L1/axpy                      # authoritative operator entry (definition)
    - L2/krylov-step               # use-site cross-link (Krylov update axpy chains)
---

# axpy
```

```edit:book/src/concepts/apply_linop.md
[old]: # apply_linop
[new]: ---
edges:
  reference:
    - L1/apply_linop               # authoritative operator entry (definition)
    - concepts/constructed-operators  # sibling concept (constructed-operator unfolding)
    - L2/krylov-step               # use-site cross-link (matvec count / per-step apply)
---

# apply_linop
```

```edit:book/src/concepts/apply_BA.md
[old]: # Concept: `apply_BA` (preconditioner-side constructed operator)
[new]: ---
edges:
  reference:
    - concepts/constructed-operators  # parent concept (apply_BA IS a constructed operator)
    - L2/krylov-step               # use-site (per-Arnoldi-step operator, absorbs side/flexible)
---

# Concept: `apply_BA` (preconditioner-side constructed operator)
```

```edit:book/src/concepts/gemv_basis.md
[old]: # gemv_basis
[new]: ---
edges:
  reference:
    - concepts/orthogonalization   # primary use-site (CGS/CGS2 basis correction)
---

# gemv_basis
```

```edit:book/src/concepts/elementwise-product.md
[old]: # elementwise_product
[new]: ---
edges:
  reference:
    - L1/elementwise_product       # authoritative operator entry (definition)
---

# elementwise_product
```

```edit:book/src/concepts/trsv.md
[old]: # trsv
[new]: ---
edges:
  reference: []                    # no book home: L1/trsv does not exist; the back-solve loop
                                   # (iterative.cpp:669-706) is an L0 source citation, not a book node.
                                   # Non-node pointer page; no outbound book edges.
---

# trsv
```

```edit:book/src/concepts/two_operator_split.md
[old]: # two_operator_split
[new]: ---
edges:
  reference:
    - L4/preconditioning-framework   # firm L4 home of the (op, pc_op) binding
    - concepts/complex-from-real-lift  # the real-pc-on-complex-operand path
    - concepts/constructed-operators   # variant-absorption-behind-uniform-interface pattern
    - concepts/solver-as-operator      # type-level statement making the split uniform
---

# two_operator_split
```

```edit:book/src/concepts/set_subvector_zero.md
[old]: # set_subvector_zero
[new]: ---
edges:
  reference: []                    # no book home: L1/set_subvector_zero does not exist; the
                                   # divfree use-site and the L3 mask-multiply lift are described
                                   # in-page. Non-node pointer page; no outbound book edges.
---

# set_subvector_zero
```

```edit:book/src/concepts/scalar-promotion.md
[old]: # scalar-promotion
[new]: ---
edges:
  reference:
    - L1/axpy                      # operator where the rule applies
    - L1/axpby                     # operator where the rule applies
    - L1/axpbypcz                  # operator where the rule applies
    - L1/scal                      # operator where the rule applies (internal imag==0 branch)
    - concepts/complex-from-real-lift  # the distinct operator-level real->complex lift
---

# scalar-promotion
```

```edit:book/src/concepts/complex-from-real-lift.md
[old]: # complex-from-real-lift
[new]: ---
edges:
  reference:
    - L4/preconditioning-framework   # names this primitive as the complex-pc unfolding
    - concepts/apply_linop           # the wrapped primitive
    - concepts/scal                  # the in-place sign-flip primitive
    - concepts/constructed-operators # the lift as a constructed-operator route
---

# complex-from-real-lift
```

```edit:book/src/concepts/tensor-field-lift.md
[old]: # Concept: tensor-field-lift
[new]: ---
edges:
  reference:
    - concepts/axpy                  # L2 form being lifted
    - concepts/dot                   # L2 form being lifted
    - concepts/nrm2                  # L2 form being lifted
    - concepts/scal                  # L2 form being lifted
    - concepts/apply_linop           # L2 form being lifted
    - concepts/sequential-obstruction  # when the lift fails
    - concepts/rotation              # underlying rotation methodology
---

# Concept: tensor-field-lift
```

```edit:book/src/concepts/variant-absorption.md
[old]: # variant absorption
[new]: ---
edges:
  reference:
    - concepts/rotation              # peer methodology concept
    - concepts/constructed-operators # canonical full-absorption route
    - L2/krylov-step                 # worked example slices (CG / GMRES variant axes)
---

# variant absorption
```

```edit:book/src/concepts/finest-level-unwrap.md
[old]: # finest-level-unwrap
[new]: ---
edges:
  reference:
    - L4/preconditioning-framework      # firm L4 home (structural adapter in pcBoundOp)
    - concepts/constructed-operator-factory  # the factory creating the unwrap condition
---

# finest-level-unwrap
```

## Supporting evidence

- **Scheme authority for the non-node call:** `book/src/methodology/graded-stack-scheme.md:244-252`
  (§5 concept-page two-sub-cases: "narrative pointer to an L_n operator, e.g.
  `concepts/dot.md` ... sits **outside the subject DAG** ... no `rank:`"); the
  scheme-page self-exclusion banner at `:13-17`; the `depends-on`/`reference`
  binary + feature-root rule at `:101-115`.
- **On-disk convention precedent** (the symmetric-`reference` finding):
  `book/src/L1/dot.md:1-9` — `rank: firm` + `edges: reference: [L1-L0/dot-mutation-rotation,
  concepts/dot]`; `concepts/dot` is a `reference` back-pointer, NOT a
  `depends-on`. This is the load-bearing precedent that the concept→L1 down-edge
  is `reference`.
- **Home-target assertions cited per page** (where each page states its
  authoritative home):
  - `concepts/dot.md:4-6` + `:81-84` ("authoritative operator entry ... lives at `L1/dot`").
  - `concepts/nrm2.md:9` ("See `L1/nrm2` (authoritative)").
  - `concepts/scal.md` / `axpy.md` — BLAS-1 in-place primitives; L1 homes `L1/scal`, `L1/axpy` (both exist).
  - `concepts/apply_linop.md:79-92` (concept body) — home `L1/apply_linop`.
  - `concepts/elementwise-product.md` — home `L1/elementwise_product` (file H1 is `# elementwise_product`).
  - `concepts/two_operator_split.md:24-32` ("Used by `preconditioning-framework` — the firm L4 home"; see-also constructed-operators + solver-as-operator).
  - `concepts/complex-from-real-lift.md:24-38` ("`preconditioning-framework` names this primitive"; see-also apply_linop/scal/constructed-operators).
  - `concepts/scalar-promotion.md:32-38` (operators where it applies: axpy/axpby/axpbypcz/scal) + `:46-48` (see-also complex-from-real-lift).
  - `concepts/tensor-field-lift.md:28-32` (see-also: the five L2 forms + sequential-obstruction + rotation).
  - `concepts/variant-absorption.md` — peer to `rotation.md` (`:3`), routes to `constructed-operators` (`:95`), worked-example slices `L2/krylov-step` (`:202-205`).
  - `concepts/finest-level-unwrap.md:20-26` ("Used by `preconditioning-framework`"; see-also constructed-operator-factory).
  - `concepts/apply_BA.md:9` ("This is a constructed operator") + `:38-40` (use-site krylov-step).
  - `concepts/gemv_basis.md:21` (use-site `orthogonalization`).
- **Dangling-target audit (no broken `depends-on`, no dangling `reference`):**
  all edge targets verified present on disk —
  `L1/{dot,nrm2,scal,axpy,apply_linop,axpby,axpbypcz,elementwise_product}.md`,
  `L2/{krylov-step,inner_product,elementwise_product}.md`,
  `L4/preconditioning-framework.md`,
  `concepts/{constructed-operators,orthogonalization,solver-as-operator,complex-from-real-lift,apply_linop,scal,dot,nrm2,axpy,sequential-obstruction,rotation,constructed-operator-factory}.md`.
  Confirmed-ABSENT (so deliberately NOT referenced — would have dangled):
  `L1/trsv`, `L1/set_subvector_zero`, `L1/gemv_basis` do not exist; hence
  `trsv` and `set_subvector_zero` carry empty `reference: []`, and `gemv_basis`
  points only at the existing `concepts/orthogonalization`.
- **Build-safety:** edits are pure frontmatter prepends (a `--- ... ---` block
  before the existing H1) + one preserved blank line; no prose mutated, no link
  added or removed in body text, so `linkcheck2` surface is unchanged. The
  `reference: []` empty-list form is valid YAML.

## Open questions / caveats

- **`graded-stack-index-and-concept-node-status` (the shared OQ with D4/D5):**
  I applied convention **C-A = non-node, `reference`-only, no `rank:`** to all 16
  pages. D4 (concepts/index, concepts/dependency-map) and D5 (layer index/
  container pages) are deciding the SAME node-vs-not question for index/container
  surfaces. **Flag for batch-close meta-phase unification:** (a) confirm
  `reference`-only-with-no-`rank:` is the agreed encoding for non-node concept
  pages (vs strict §5 "zero frontmatter"); if zero-frontmatter wins, these 16
  blocks drop cleanly (they assert nothing blocking). (b) The three homeless
  primitives (`trsv`, `set_subvector_zero`, `gemv_basis`) suggest a latent gap —
  they are real L1-grade vector/BLAS primitives with NO `L1/<name>.md` entry.
  This is not a typing defect but a **coverage gap**: flag
  `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` so a
  harvester pass can decide whether each warrants a promoted L1 entry (gemv_basis
  self-describes as "a derived L2 primitive", so it may legitimately live only as
  a concept; trsv/set_subvector_zero are more clearly L1-shaped). Routed as OQ,
  not an in-cluster edit (concept pages are read-only toward their would-be homes).
- **No `kind:` annotations emitted.** All edges are `reference`, and the scheme
  states the linters ignore `kind:` (documentation only); for a pure-pointer
  cluster the bare-string `reference` form is the cleanest. A future analysis
  wanting to distinguish "pointer-to-definition" vs "see-also sibling" vs
  "use-site" could add `kind:` later without changing linter behavior.
- **`apply_BA` / `two_operator_split` / `complex-from-real-lift` /
  `finest-level-unwrap` border on "load-bearing substrate."** I judged each
  `reference` (not `depends-on`) because: the FIRM home that an operator/feature
  genuinely depends on is the L4 `preconditioning-framework` chapter (and the
  constructed-operator framework), and those chapters carry their OWN typed
  `depends-on` edges to their constituents — the concept page is the narrative
  mirror, not the blocking node. If a future audit finds an operator entry whose
  rank genuinely rests on one of these concept pages (rather than on the L4/L2
  chapter), that edge would be re-typed `depends-on` ON THE OPERATOR ENTRY, not
  here.
