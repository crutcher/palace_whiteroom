---
agent: layer-intro-author
invoked_at: 2026-06-05T071837Z
scope: graded-stack typed-edge campaign P1 first tranche — concepts/ cluster C (krylov-internals + obstruction/disposition vocabulary)
status: pending
integrated_at: 2026-06-05T085500Z
integration_commit: INTEGRATION_SHA_PLACEHOLDER
integration_notes: >
  Applied clean (cycle-103 D3, staging row 4 — P1 typed-edge campaign concepts cluster C).
  12 concept pages got reference-only typed edges: frontmatter (gmres/givens/obstruction-
  classification/disposition-test meta-pages; no rank tokens — all non-DAG narrative/obstruction
  meta-pages). incremental-least-squares edge typed to the EXISTING concepts/givens (NOT the
  prose's nonexistent givens-rotation slug — prose left untouched, flagged). overall_status: ready
  set by the repairer (accept-and-route on the lone edge-label-fidelity WARNING). Build green.
  step-5b rank_violations: 0 (every edge reference, vacuous). Opened OQ
  incremental-least-squares-prose-names-nonexistent-givens-rotation-slug (non-link drift).
---

# CYCLE: concepts/ cluster C typed-edge frontmatter (12 pages)

## Summary

Cycle-103 D3, first tranche of the graded-stack typed-edge campaign (P1). Authors the canonical
`edges:` frontmatter block onto the 12 concept pages of cluster C: the krylov-internals cluster
(`gmres`, `givens`, `givens_apply`, `givens_generate`, `plane-rotation-stream`, `orthogonalization`,
`incremental-least-squares`, `first-iteration-unrolling`) and the obstruction/disposition vocabulary
cluster (`sequential-obstruction`, `scope-out-obstruction`, `negative-result-slice`,
`black-box-vs-accelerated-kernels`).

**Node-status convention applied (the load-bearing decision, recorded for meta-phase unification
across D1/D2/D4/D5).** Per scheme §2d / §5 and `METHODOLOGY-GRADED-STACK.md` §2d: a concept page
that is a **narrative pointer to an L_n operator / a classification-vocabulary page / a
methodology-pattern page** sits **OUTSIDE the subject DAG** — it documents the construction, it is
not a node in it. **All 12 of these pages are exactly that kind** (narrative pointers + obstruction
classification vocabulary + a disposition-test page). NONE is a record-definition (`record` kind)
page. Therefore:

- **No `rank:` token on any of the 12** (same convention as `graded-stack-scheme.md` itself, scheme
  §2d). A `rank:` would falsely enroll a meta-page as a DAG node and would make the reachability GC
  treat it as live-or-garbage vocabulary, which it is not.
- **Each still gets a typed `edges:` block** (HARD-gate-new: every page is typed even when it is not
  a ranked node). The `edges:` block records the page's outbound links classified `depends-on` vs
  `reference`. For a non-DAG meta-page these are *documentation of the navigation*; the linters will
  see no inbound `depends-on` edge pulling these pages live (they are not roots and not reachable
  vocabulary), which is correct — a concept meta-page is reachable as a `reference` target of the
  entries that cite it, never as a `depends-on` support.

**Edge-typing decision (uniform across the cluster).** Per the typing discipline: a concept page is
a narrative POINTER, not a node that *rests on* its home in the well-foundedness sense. A
narrative-pointer page does not constrain (or get constrained by) the rank of the entry it points at
— so **every outbound edge from these 12 pages is `reference`**. There is **zero `depends-on`** in
this tranche. This is the correct and expected outcome for the obstruction/disposition substrate
(the dispatch note predicted these are `reference`-only substrate nodes) AND for the
krylov-internals narrative pointers (a `concepts/gmres` page does not *depend on* `L2/krylov-step` in
the rank sense — it points the reader at the firm home; the rank flows the other way, and the L2
entry's own `depends-on` block already carries that). Were any of these pages a record-definition
page, its down-edge to the backing L0 struct would be `depends-on (kind: cites-evidence)` — but none
is.

**depends-on vs reference split for the tranche: 0 `depends-on` / 12 pages of `reference`-only edges.**

**Dangling targets: none.** All edge targets verified to exist on disk (see Supporting evidence).

## Proposed changes

Each block prepends a YAML frontmatter `edges:` document to the existing file. The page's current
first line (the `# Title`) is preserved immediately after the closing `---`.

```edit:book/src/concepts/gmres.md
[old]: # GMRES (concept)
[new]: ---
edges:
  reference:
    - L2/krylov-step
    - L2/ksp_solve
    - L1-L0/ksp-solve-mutation-rotation
    - concepts/orthogonalization
    - concepts/apply_linop
    - concepts/variant-absorption
    - concepts/constructed-operators
---

# GMRES (concept)
```

```edit:book/src/concepts/givens.md
[old]: # givens
[new]: ---
edges:
  reference:
    - L2/incremental-least-squares
---

# givens
```

```edit:book/src/concepts/givens_apply.md
[old]: # `givens_apply`
[new]: ---
edges:
  reference:
    - L1/ls-update-column
---

# `givens_apply`
```

```edit:book/src/concepts/givens_generate.md
[old]: # `givens_generate`
[new]: ---
edges:
  reference:
    - L1/ls-update-column
---

# `givens_generate`
```

```edit:book/src/concepts/plane-rotation-stream.md
[old]: # Plane-rotation stream
[new]: ---
edges:
  reference:
    - concepts/givens_apply
    - concepts/givens_generate
    - concepts/sequential-obstruction
    - L2/incremental-least-squares
    - L2/krylov-step
---

# Plane-rotation stream
```

```edit:book/src/concepts/orthogonalization.md
[old]: # concept: orthogonalization
[new]: ---
edges:
  reference:
    - L1/orthogonalize
    - L1-L0/orthogonalize-mutation-rotation
    - L1/dot
    - L1/axpy
    - L2/orthogonalize
    - L3/orthogonalize
    - L2/krylov-step
    - concepts/sequential-obstruction
    - concepts/variant-absorption
---

# concept: orthogonalization
```

```edit:book/src/concepts/incremental-least-squares.md
[old]: # Incremental least-squares update
[new]: ---
edges:
  reference:
    - L1/ls-update-column
    - concepts/givens
    - concepts/orthogonalization
---

# Incremental least-squares update
```

```edit:book/src/concepts/first-iteration-unrolling.md
[old]: # First-iteration unrolling
[new]: ---
edges:
  reference:
    - L2/krylov-step
    - L4/krylov-step
    - concepts/rotation
    - concepts/derived-view-hoisting
    - concepts/variant-absorption
    - concepts/sequential-obstruction
---

# First-iteration unrolling
```

```edit:book/src/concepts/sequential-obstruction.md
[old]: # Concept: sequential-obstruction
[new]: ---
edges:
  reference:
    - concepts/tensor-field-lift
    - concepts/rotation
    - L3/orthogonalize
    - L1-L0/triangular-solve-obstruction
    - L1/ls-update-column
    - concepts/apply_linop
    - concepts/ksp_solve
---

# Concept: sequential-obstruction
```

```edit:book/src/concepts/scope-out-obstruction.md
[old]: # scope-out-obstruction
[new]: ---
edges:
  reference:
    - concepts/sequential-obstruction
    - concepts/apply_linop
    - concepts/ksp_solve
    - concepts/variant-absorption
    - concepts/constructed-operators
    - L1-L0/triangular-solve-obstruction
---

# scope-out-obstruction
```

```edit:book/src/concepts/negative-result-slice.md
[old]: # Negative-result slice
[new]: ---
edges:
  reference:
    - concepts/sequential-obstruction
    - L1-L0/triangular-solve-obstruction
    - L4/chebyshev
---

# Negative-result slice
```

```edit:book/src/concepts/black-box-vs-accelerated-kernels.md
[old]: # black-box vs accelerated kernels
[new]: ---
edges:
  reference:
    - concepts/eigsolve
    - concepts/dot
    - concepts/nrm2
    - concepts/scal
    - concepts/ksp_solve
    - concepts/apply_linop
    - L4/eigsolve
    - L4/ksp_solve
    - L4/fe_assemble
    - L4/fold_solve
    - L3/inner_product
    - L3/linear_combination
    - concepts/sequential-obstruction
    - concepts/scope-out-obstruction
---

# black-box vs accelerated kernels
```

## Supporting evidence

**Pages typed (12):** `gmres`, `givens`, `givens_apply`, `givens_generate`, `plane-rotation-stream`,
`orthogonalization`, `incremental-least-squares`, `first-iteration-unrolling`,
`sequential-obstruction`, `scope-out-obstruction`, `negative-result-slice`,
`black-box-vs-accelerated-kernels`. Disjoint from D1/D2's page sets; does not touch operator entries,
`concepts/index.md`, or `concepts/dependency-map.md` (D4's).

**Edge targets — all verified to exist on disk** (`book/src/<slug>.md`), so no dangling target and
the build stays green (`linkcheck2` would fail on a missing-file link; every `reference` slug here
resolves):

- L_n homes: `L2/krylov-step`, `L2/ksp_solve`, `L2/incremental-least-squares`, `L2/orthogonalize`,
  `L2/inner_product`, `L3/orthogonalize`, `L3/inner_product`, `L3/linear_combination`,
  `L4/krylov-step`, `L4/eigsolve`, `L4/ksp_solve`, `L4/fe_assemble`, `L4/fold_solve`, `L4/chebyshev`.
- L1 / lowering: `L1/orthogonalize`, `L1/ls-update-column`, `L1/dot`, `L1/axpy`, `L1/apply_linop`,
  `L1-L0/orthogonalize-mutation-rotation`, `L1-L0/ksp-solve-mutation-rotation`,
  `L1-L0/triangular-solve-obstruction`.
- concepts/ siblings: `orthogonalization`, `apply_linop`, `ksp_solve`, `variant-absorption`,
  `constructed-operators`, `tensor-field-lift`, `rotation`, `derived-view-hoisting`, `eigsolve`,
  `dot`, `nrm2`, `scal`, `givens`, `givens_apply`, `givens_generate`, `sequential-obstruction`,
  `scope-out-obstruction`.

**Edges read from each page's existing prose** (all outbound markdown links + the cited L_n homes in
the narrative pointer line), then classified. The two `givens_*` pages cite
`palace/linalg/gmres.cpp:GeneratePlaneRotation` / `:ApplyPlaneRotation` as a `reference/` source
pointer (a bare-file pointer, no line range, into `reference/palace/...`); these are L0 source
citations *inside the page body*, not edges to a book DAG node, so they do not become `edges:`
entries (the page is a meta-page, not a record-definition resting on that struct — were it a
record-definition page, the L0 struct would be a `depends-on (kind: cites-evidence)` edge).

**`rank:` decision per page:** none assigned. All 12 are construction-meta / classification-
vocabulary pages outside the subject DAG (scheme §2d). The obstruction/disposition four
(`sequential-obstruction`, `scope-out-obstruction`, `negative-result-slice`,
`black-box-vs-accelerated-kernels`) are heavily `reference`d *by* obstruction-status operator
entries — they are reference TARGETS, never `depends-on` supports, consistent with the dispatch
note's prediction that they are `reference`-only substrate nodes.

## Open questions / caveats

- **`graded-stack-index-and-concept-node-status` (the carved-out OQ) — convention applied here, for
  meta-phase cross-D unification.** I treated ALL 12 cluster-C pages as **non-DAG meta-pages: typed
  `edges:` block, NO `rank:`**, because each is a narrative pointer / classification-vocabulary /
  methodology-pattern page (scheme §2d's "meta page about the construction" case), and none is a
  `record`-kind record-definition page (the only concept-page sub-case that scheme §5 says IS a DAG
  node, ranked by the resolution of the data shape). D1/D2/D4/D5 should apply the same rule and the
  meta-phase should ratify it: **concept page is a DAG node iff it is a record-definition page;
  otherwise it is a typed-but-unranked meta-page.** If a sibling dispatch hits a concept page that
  genuinely defines a data shape (a `{ field: type }` schema with an L0 backing struct), THAT page
  takes `rank:` + a `depends-on (kind: cites-evidence)` edge to its L0 struct — none occurred in
  cluster C.
- **`edges:`-on-a-non-DAG-node ambiguity.** The scheme says a non-DAG meta-page "carries no
  `rank:`/`edges:` frontmatter" for the scheme page *itself* (§2d, top banner). I read the
  HARD-gate-new "any node must be typed" + the dispatch instruction ("type their own down-edges") as
  overriding for the concept *pages* (vs. the methodology scheme/ladder pages): the concept pages get
  a typed `edges:` block (all `reference`) so the reachability GC can follow their see-also links
  without inventing untyped edges, but no `rank:`. If the meta-phase prefers concept meta-pages to
  carry NO frontmatter at all (pure §2d treatment, like the scheme page), these 12 `edges:` blocks
  would be dropped — flagging the choice rather than forcing it. The conservative choice taken (type
  the edges, omit the rank) is reversible and strictly more information than omitting frontmatter.
- **`incremental-least-squares.md` §Dependencies prose names `givens-rotation`** (line 35: "L2
  realisation depends on `givens-rotation` (the scalar kernel pair: generate + apply)"). There is no
  `concepts/givens-rotation.md` file — the kernel pair lives as `concepts/givens.md` (+ the split
  `givens_apply` / `givens_generate`). I typed the edge to the existing `concepts/givens` rather than
  the prose's non-existent `givens-rotation` slug (avoids a dangling target). The prose still reads
  `givens-rotation`; this is a pre-existing prose/naming drift (the page predates the
  `givens`/`givens_apply`/`givens_generate` split) — flagged as `incremental-least-squares-prose-
  names-nonexistent-givens-rotation-slug` for a future harvester/cross-cutter touch, NOT fixed here
  (out of typed-edge scope; the page body is not mine to re-author this dispatch).
- The cluster-C pages reference several other concept pages that are themselves in D1/D2's set or
  not-yet-typed (`apply_linop`, `ksp_solve`, `variant-absorption`, `constructed-operators`,
  `eigsolve`, `dot`, `nrm2`, `scal`, `rotation`, `tensor-field-lift`, `derived-view-hoisting`). These
  are `reference` targets (the files exist; build-safe). Whether THEY get `rank:` is each owner
  dispatch's call under the same node-status convention above; nothing in cluster C constrains them
  (no `depends-on` edges emitted).
