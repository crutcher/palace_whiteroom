---
agent: layer-intro-author
invoked_at: 2026-06-05T201831Z
scope: cycle-106 D5 — graded-stack lazy-tail typing; reclassify the 21 unresolved depends-on targets (item-2 sub-target `graded-stack-lazy-tail-typing`)
status: integrated
integrated_at: 2026-06-05T223000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-106 D5, applied clean. 18-host lazy-tail legacy frontmatter reclassified into typed edges: blocks → unresolved_depends_on_targets 21→0 (with D2's solve_family clearing the 21st), --strict EXIT 0; all 21 false-positives from un-migrated legacy frontmatter (36 distinct targets all on-disk). WAVE-3 exclusion honored. Build EXIT 0; rank_violations 0. OQs graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon (latent linter-reader bug) + solve_family-last-unresolved-target-handed-to-d3 (recorded resolved) promoted. Non-blocking report-narration MISS citecheck on graded_stack_lint.py tool line-refs (outside citecheck roots, critic-verified) recorded, not an artifact defect."
---

# CYCLE: unresolved-`depends-on`-target reclassification (21 false-positives)

## Summary

The graded-stack linter reports `unresolved_depends_on_targets: 21` under `--strict`.
**All 21 are false-positives produced by un-migrated LEGACY edge frontmatter**, not
genuine missing targets. 18 host files still carry the pre-scheme `depends_on:` /
`lowers_to:` / `lifts_from:` / `lifts_to:` / `lowers_from:` / `consumes:` keys; the
linter migrates those keys to `depends-on` edges (lint §migration (a)/(b)/(c)) and the
targets fail to resolve for three mechanical reasons:

1. **prose-as-slug (case a)** — a `lowers_to:`/`lifts_from:` item written as pure
   explanatory prose (`(no L4 entry; …)`, `(none) — …`, `the per-mode scalar maps …`,
   `the per-port port-mode linear functional …`). There is no slug; the in-line
   no-theme lowering is annotated in the chapter body, not a frontmatter edge. → **strike**.
2. **mis-parsed `{'book/src/…`** — a legacy item whose trailing prose qualifier
   contains a `:` (e.g. `… (the L1>L0 mutation rotation: …)`). The `:` trips the
   linter's block-mapping branch (`graded_stack_lint.py:211`), so the whole string is
   read as a `{target: …}` dict and stringified into the unresolved list. The slug
   itself is **legitimate and the file EXISTS**; only the encoding is wrong. →
   **re-encode as a clean `edges:` slug**.
3. **missing `L_n/` prefix** — `L1/eliminate_rhs` lists bare `apply_linop` / `axpy`
   (no layer prefix); the real files are `L1/apply_linop` / `L1/axpy`. → **fix prefix**.

**Zero of the 21 are genuine missing targets (case c).** Every clean slug target was
verified to exist on disk (existence sweep below). The fix is the §(e)/scheme-§4
migration: replace each host's legacy edge keys with a single typed `edges:` block,
classifying each edge `depends-on` (blocking vocabulary/lowering-endpoint) vs
`reference` (narrative-concept / navigational-container framing). `firmness: firm`
already supplies each host's `rank: firm` (`derive_rank` reads `firmness:`,
`graded_stack_lint.py:431`), so no `rank:` token is added and no rank claim changes.

**Case (b) of the dispatch (the `cites-evidence` L0-edge exemption) does not arise
here** — none of the 21 unresolved targets is an L0 `path:lo-hi` citation; all are book
slugs. `normalize_target` already returns `None` for `:lo-hi` cites (`:324`), so L0
evidence edges never enter the unresolved list. No linter-code finding is needed.

**Verified result (simulated on a temp copy of `book/src`, then discarded — this is a
DISPATCH-phase report; no `book/` write):**

```
BEFORE:  UNRESOLVED depends-on targets (21)   |  0 rank violation(s)
AFTER :  UNRESOLVED depends-on targets (1)    |  0 rank violation(s)
```

The single residual (`1`) is **`L4/solve_family -> {'book/src/L4-L3/solve-family-map-dissolution`**
— a WAVE-3 file owned by D3 this cycle (EXCLUDED from my scope; deferred, see below).
It resolves when D3 migrates `L4/solve_family` to its `edges:` block.

## WAVE-3 exclusion / deferral

`L4/solve_family` appears among the unresolved-target hosts but is one of the 5 WAVE-3
chapters owned by D1/D2/D3 this cycle (`L4/ksp_solve`, `L4/krylov-step`,
**`L4/solve_family`**, `L4/fold_solve`, `L4/eliminate_bc`). **I did NOT touch it.** Its
one unresolved target is the same legacy-`lowers_to:`-with-`:`-in-qualifier mis-parse
class: the item `- book/src/L4-L3/solve-family-map-dissolution.md (… NO standalone
L3/solve_family entry …)` — the slug `L4-L3/solve-family-map-dissolution` EXISTS
(verified). **For the owning dispatch (D3):** when you author `L4/solve_family`'s
`edges:` block per the prompt (`uses-record` → `op-params`,`sim-state`), also encode
`depends-on: [L4/ksp_solve, L4/iterate-while, L4-L3/solve-family-map-dissolution]` and
`reference: [concepts/state-stratification]` (migrating its current `consumes:` /
`lowers_to:`), which clears this last unresolved target → `0`.

## Proposed changes

Each block strips the host's legacy edge keys (`depends_on:` / `lowers_to:` /
`lifts_from:` / `lifts_to:` / `lowers_from:` / `consumes:`) and adds a typed `edges:`
block. All other frontmatter keys (`layer`, `operator`, `firmness`, `variant_axes`,
`consumes`-derived references) are preserved. Free-text dependency qualifiers are
dropped from the edges per scheme §4 row (c) (the dep's rank is read from the dep's own
frontmatter, never restated on the edge); the prose rationale already lives in each
chapter's body (`## Downward to …` / `## Lowers to` / `## Consumes`) and is untouched.

### (1) L1/assemble_frequency_operator — mis-parse(b)×2 + clean(b)×1

```edit:book/src/L1/assemble_frequency_operator.md
[old]:
depends_on:
  - book/src/L2/linear_combination.md (the firm scalar-weighted-sum fold this operator is the operator-operand specialization of — re-expressed THROUGH it via the operand-category variant axis; NOT a new mirrored fold)
  - book/src/L1/apply_linop.md (the opaque-operator gate — the fixed-basis operators {K, C, M, A2} are apply_linop-shaped opaque LinearOperator values; the assembled A is itself apply_linop-applicable)
lowers_to:
  - book/src/L1-L0/assemble-frequency-operator-rotation.md (the L1>L0 mutation rotation: the pure affine-operator-family value → the BuildParSumOperator / GetSystemMatrix imperative SumOperator assembly)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L2/linear_combination
      kind: folds
    - L1/apply_linop
    - target: L1-L0/assemble-frequency-operator-rotation
      kind: lowers-to
variant_axes:
```

### (2) L1/eliminate_rhs — missing-prefix(c-style→fixed) + clean

```edit:book/src/L1/eliminate_rhs.md
[old]:
lowers_to:
  - L1-L0/fe-operator-assemble-mutation-rotation
lifts_from: []
depends_on:
  - apply_linop
  - axpy
variant_axes:
[new]:
edges:
  depends-on:
    - L1/apply_linop
    - L1/axpy
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to
variant_axes:
```

### (3) L2/ksp_solve — mis-parse(b)×2 (`lifts_to:`/`lowers_from:`)

```edit:book/src/L2/ksp_solve.md
[old]:
lifts_to:
  - book/src/L3/ksp_solve.md (the L3 iteration-rotation un-erasure: L2's outer-driver-by-role wrap becomes the explicit iterate_while_L3 fold; theme L3-L2/ksp-solve-outer-driver pending — NOT identity-in-form)
lowers_from:
  - book/src/L1/ksp_solve.md (the opaque solver-as-operator collapse; this L2 entry opens that collapse into the kernel-fold composition while keeping the iteration view erased)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L3/ksp_solve
      kind: lifts-to
    - target: L1/ksp_solve
      kind: lowers-from
variant_axes:
```

### (4) L3/apply_linop — strike prose `lifts_from:` (a) + clean `lowers_to:`

```edit:book/src/L3/apply_linop.md
[old]:
lowers_to:
  - book/src/L1/apply_linop.md (directly; identity-in-form on the primitive's signature; no L3-L2 theme — apply_linop is a leaf primitive whose L1 form is L3-native by signature shape, and L2 hosts no standalone apply_linop entry)
lifts_from:
  - (no L4 entry; apply_linop appears inside book/src/L4/krylov-step.md as a let-binding per book/src/L4/krylov-step.md §Semantics body; the L4 candidate was confirmed-not-needed by cycle-010 cross-layer-cross-cutter audit — leaf primitives carry no L4 calculus content)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L1/apply_linop
      kind: lowers-to
variant_axes:
```

### (5) L3/assemble-diagonal — strike prose `lifts_from:` (a) + clean `lowers_to:`

```edit:book/src/L3/assemble-diagonal.md
[old]:
lowers_to:
  - book/src/L2/assemble-diagonal.md (identity-in-form on the primitive's signature; the L3>L2 edge is a degenerate identity-in-named-terms lowering recorded as an in-line note here — see Lowers-to — not a dedicated theme, per the 2026-06-01 vocabulary-shift redirect)
lifts_from:
  - (none) — `assemble_diagonal` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict; the operator-to-data sibling of `apply_linop`, which is likewise L4-row-free)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L2/assemble-diagonal
      kind: lowers-to
variant_axes:
```

### (6) L3/divfree-projector — mis-parse(b) `lowers_to:` + strike prose `lifts_from:` (a); kept theme → reference

```edit:book/src/L3/divfree-projector.md
[old]:
lowers_to:
  - book/src/L2/divfree-projector.md (identity-in-form on the constructed-operator-gate apply; lowers through the present adjacent L2 floor — the L3>L2 rotation is a degenerate identity-in-named-terms lowering annotated in-line in §"Lowers to" as of cycle-051 demotion, no dedicated L3>L2 theme file; the four-step apply WeakDiv→Z→ksp_solve→Grad is a fixed straight-line composition whose L2 floor form is value-thread-isomorphic by signature shape. The ONE genuine fusion rotation in the chain lives on the L2>L1 edge: the step-4 Grad->AddMult re-fusion, captured by the KEPT firm theme book/src/L2-L1/divfree-projector-leaf-identity.md — reachable onward from the L2 floor, not orphaned. The substantive leaf-mutation rotation lives at L1>L0 divfree-projector-mutation-rotation; the inner-solve obstruction is carried BY REFERENCE through the firm-L3 ksp_solve dependency, never introduced or erased here)
lifts_from:
  - (no L4 entry; divfree-projector carries no monadic effect / state-stratification typing / outer-driver structure at L4 of its own — the apply is a fixed four-step composition delegating its only iteration to the inner ksp_solve gate; same confirmed-not-needed L4 verdict as the firm apply_linop / ksp_solve / jacobi-smoother constructed-operator gates)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L2/divfree-projector
      kind: lowers-to
  reference:
    - L2-L1/divfree-projector-leaf-identity
variant_axes:
```

### (7) L3/elementwise_product — mis-parse(b) `lowers_to:` + strike prose `lifts_from:` (a)

```edit:book/src/L3/elementwise_product.md
[old]:
lowers_to:
  - book/src/L2/elementwise_product.md (identity-in-form on the primitive's signature; degenerate identity-in-named-terms edge — recorded in-line at "Lowers to" per the 2026-06-01 vocabulary-shift redirect, no dedicated L3>L2 theme; substantive rotation deferred to the L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B)
lifts_from:
  - (none) — `elementwise_product` is a leaf binary field operation; no L4 entry exists (leaf primitives don't get L4 rows per the cycle-010 audit verdict; the Hadamard sibling of the BLAS-1 / `scal` leaf cohort, which is likewise L4-row-free)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L2/elementwise_product
      kind: lowers-to
variant_axes:
```

### (8) L3/jacobi-smoother — mis-parse(b) `lowers_to:` + strike prose `lifts_from:` (a)

```edit:book/src/L3/jacobi-smoother.md
[old]:
lowers_to:
  - book/src/L1/jacobi-smoother.md (identity-in-form on the constructed-operator-gate apply; no L3-L2 theme — the apply is a single elementwise-product whose L1 form is L3-native by signature shape; the substantive leaf-mutation rotation lives at L1>L0 reciprocal-elementwise-product-mutation-rotation)
lifts_from:
  - (no L4 entry; jacobi-smoother carries no monadic effect / state-stratification typing / outer-driver structure at L4 — the apply is one elementwise product, a leaf-shaped constructed-operator gate; same confirmed-not-needed L4 verdict as the firm apply_linop / ksp_solve constructed-operator gates)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L1/jacobi-smoother
      kind: lowers-to
variant_axes:
```

### (9) L3/reciprocal — mis-parse(b) `lowers_to:` + clean `lifts_from:`

```edit:book/src/L3/reciprocal.md
[old]:
lowers_to:
  - book/src/L2/reciprocal.md (identity-in-form on the primitive's signature; lowers to the present adjacent L2 floor — the degenerate L3>L2 identity is recorded in-line at §"Downward to L2" / §"Lowers to", no dedicated theme file: the vocabulary does not shift across this edge)
lifts_from:
  - book/src/L1/reciprocal.md (value-thread-isomorphic; same signature shape; whole-tensor by construction — no L4 entry, leaf elementwise primitive)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L2/reciprocal
      kind: lowers-to
    - target: L1/reciprocal
      kind: lifts-from
variant_axes:
```

### (10) L4/assemble_frequency_operator — `consumes:` → depends-on/reference; mis-parse(b) `lowers_to:`

```edit:book/src/L4/assemble_frequency_operator.md
[old]:
consumes:
  - book/src/L4/linear_combination.md (the firm L4 scalar-weighted-sum combinator this entry is the OPERATOR-OPERAND specialization of — re-expressed THROUGH its operand-category variant axis at the operator-operand corner; NOT a mirrored operator_linear_combination fold; replace-and-propagate)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§"The combinators rise regardless" — linear_combination rises to L4 regardless as a feature-surface verb; this driven specialization rides that rise)
  - book/src/L1/assemble_frequency_operator.md (the firm L1 source — the warrant + the affine-modulo-A2 + single-pipeline-by-design caveats + the positive L0 structure are read off it; this is the upward in-layer rendering of that firm cap)
lowers_to:
  - book/src/L1/assemble_frequency_operator.md (DOWNWARD: identity-in-form on the body — the L4 operator-operand linear_combination specialization is value-thread-isomorphic to the firm L1 affine-operator-family form; NO dedicated L4>L3 / L4>L1 theme file, in-line §"Downward to L1" — the transitive consequence of L4/linear_combination's in-line L4>L3 identity composed with the L1 cap's L1>L0 rotation; the non-adjacent-identity in-line-marker convention)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L4/linear_combination
      kind: specializes
    - L1/assemble_frequency_operator
  reference:
    - concepts/black-box-vs-accelerated-kernels
variant_axes:
```

### (11) L4/dot — `consumes:` → depends-on/reference; mis-parse(b) `lowers_to:`

```edit:book/src/L4/dot.md
[old]:
consumes:
  - book/src/L4/inner_product.md (the firm L4 reduce-to-scalar inner-product combinator this named verb re-expresses THROUGH; dot IS inner_product at M = I with the Hermitian/symmetric kernel — replace-and-propagate, NOT a re-derived fold)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§2 "Kept named abstraction — rises": dot is a confirmed keep — the literature-standard named unit downstream algorithms reference by name, rising to L4 as a named verb alongside the general combinator, a permitted dual)
  - book/src/L3/dot.md (the firm L3 named abstraction below; the value-thread-isomorphic image — identity-in-form on the body)
  - book/src/concepts/dot.md (the BLAS-1-heritage / element-type cross-cutting framing)
lowers_to:
  - book/src/L3/dot.md (identity-in-form on the body — the L4 named verb is value-thread-isomorphic to the firm L3 specialization-stub; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the inner_product/eigsolve/chebyshev in-line-marker route — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L4/inner_product
      kind: specializes
    - L3/dot
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/dot
variant_axes:
```

### (12) L4/eigenfreq_qfactor_reduce — strike prose `lowers_to:` (a); named L1 homes → reference

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
[old]:
consumes:
  - book/src/L4/eigsolve.md (firm — the opaque eigen-solve cap producing the converged eigenpair family this reduction maps over; the upstream composition-root stage)
lowers_to:
  - the per-mode scalar maps (eigenvalue un-transform + κ participation ratio + f/κ quotient); identity-in-form on the body, no dedicated L4>L3 theme — in-line §"Lowers to". The two scalar-map halves now have firm L1 homes: the eigenvalue un-transform → book/src/L1/eigenvalue-untransform.md (firm, c080); the κ participation ratio → book/src/L1/participation_ratio.md (firm, c077)
variant_axes:
[new]:
edges:
  depends-on:
    - L4/eigsolve
  reference:
    - L1/eigenvalue-untransform
    - L1/participation_ratio
variant_axes:
```

### (13) L4/fe_assemble — `consumes:` → depends-on/reference (container + concepts → reference)

```edit:book/src/L4/fe_assemble.md
[old]:
consumes:
  - book/src/L4/index.md (the OpParams / readonly state-stratification rows — the construction-input absorption home, L4/index.md:24)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (the assemble-fold = combinator-rises / libCEED-leaf = black-box-kernel-rises-as-input disposition, case 1)
  - book/src/concepts/state-stratification.md (OpParams readonly captured once; the family/term-list the per-call input)
lowers_to:
  - book/src/L4-L3/fe-assemble-fold-dissolution.md (the substantive L4>L3 dissolution to the L3 global tensor-field assembly view; D2 of this cycle authors it)
variant_axes:
[new]:
edges:
  depends-on:
    - target: L4-L3/fe-assemble-fold-dissolution
      kind: lowers-to
  reference:
    - L4/index
    - concepts/black-box-vs-accelerated-kernels
    - concepts/state-stratification
variant_axes:
```

### (14) L4/frequency_sweep — `consumes:` → depends-on; mis-parse(b) `lowers_to:`; concept → reference

```edit:book/src/L4/frequency_sweep.md
[old]:
consumes:
  - book/src/L4/assemble_frequency_operator.md (the per-ω operand A(ω)=K+iωC−ω²M+A2(ω) each member rebuilds before solving — the operator-VARYING map's per-element operator; the driven assemble half this solve half maps over)
  - book/src/L4/ksp_solve.md (the per-member solve cap mapped — one (rebuilt op_ω, rhs_ω) → one SimState)
  - book/src/L4/iterate-while.md (the strawman §3.7 family whose pure-map degenerate this map IS — each member independent, no carry; the trajectory IS the collected solution family; the solve_family / chebyshev route)
  - book/src/concepts/state-stratification.md (the operator stratum is REBUILT per member — the load-bearing contrast with solve_family's captured-once readonly op; each member's SimState independent)
lowers_to:
  - book/src/L4-L3/frequency-sweep-dissolution.md (DOWNWARD, substantive: the map collapses to the L3 explicit per-ω for-loop with the operator REBUILD + SetOperators INSIDE the loop body; authored by cycle-070 D2 abstractor this same cycle — canonical slug frequency-sweep-dissolution; NOT authored here)
variant_axes:
[new]:
edges:
  depends-on:
    - L4/assemble_frequency_operator
    - L4/ksp_solve
    - L4/iterate-while
    - target: L4-L3/frequency-sweep-dissolution
      kind: lowers-to
  reference:
    - concepts/state-stratification
variant_axes:
```

### (15) L4/inner_product — `consumes:` → depends-on/reference; mis-parse(b) `lowers_to:`

```edit:book/src/L4/inner_product.md
[old]:
consumes:
  - book/src/L3/inner_product.md (the firm L3 whole-tensor reduce-to-scalar combinator this L4 entry re-expresses THROUGH; the L4 form is the calculus-level combinator, the L3 reduction the value-thread-isomorphic image — replace-and-propagate, NOT a rectangular mirror)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (the three-way disposition: inner_product is the general combinator that RISES to L4 regardless — case 2 + §"The combinators rise regardless"; the kept named abstractions dot/nrm2 rise ALONGSIDE it as named verbs, a permitted dual)
  - book/src/concepts/dot.md (the BLAS-1-heritage / element-type cross-cutting framing for the inner-product reduction)
lowers_to:
  - book/src/L3/inner_product.md (identity-in-form on the body — the L4 calculus combinator is value-thread-isomorphic to the firm L3 reduction; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the eigsolve/chebyshev in-line-marker precedent — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
variant_axes:
[new]:
edges:
  depends-on:
    - L3/inner_product
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/dot
variant_axes:
```

### (16) L4/linear_combination — `consumes:` → depends-on/reference; mis-parse(b) `lowers_to:`

```edit:book/src/L4/linear_combination.md
[old]:
consumes:
  - book/src/L3/linear_combination.md (the firm L3 whole-tensor variadic-fold combinator this L4 entry re-expresses THROUGH; the L4 form is the calculus-level combinator, the L3 fold the value-thread-isomorphic image — replace-and-propagate, NOT a rectangular mirror)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (the three-way disposition: linear_combination is the general combinator that RISES to L4 regardless — case 3 "the combinators rise regardless"; the scal/axpy/axpby/axpbypcz fused leaves are stopped-low accelerated-kernel candidates, the combinator rises in their place)
  - book/src/concepts/scalar-promotion.md (the real ⊑ complex element-type lattice on the scalar list; carried up unchanged)
lowers_to:
  - book/src/L3/linear_combination.md (identity-in-form on the body — the L4 calculus combinator is value-thread-isomorphic to the firm L3 fold; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the eigsolve/chebyshev in-line-marker precedent — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
variant_axes:
[new]:
edges:
  depends-on:
    - L3/linear_combination
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/scalar-promotion
variant_axes:
```

### (17) L4/nrm2 — `consumes:` → depends-on/reference; mis-parse(b) `lowers_to:`

```edit:book/src/L4/nrm2.md
[old]:
consumes:
  - book/src/L4/inner_product.md (the firm L4 reduce-to-scalar inner-product combinator nrm2 CONSUMES at the diagonal y = x; nrm2 = √ ∘ abs ∘ inner_product — a CONSUMER of the fold's output, NOT a fold member, the do-NOT-merge over-unification guard)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§2 "Kept named abstraction — rises": nrm2 is a confirmed keep — the 2-norm, the named unit downstream algorithms reference by name as residual nrm2(r), rising to L4 as a named verb)
  - book/src/L3/nrm2.md (the firm L3 named abstraction below; the value-thread-isomorphic image — identity-in-form on the body)
  - book/src/concepts/nrm2.md (the BLAS-1-heritage cross-cutting framing)
lowers_to:
  - book/src/L3/nrm2.md (identity-in-form on the body — the L4 named verb is value-thread-isomorphic to the firm L3 consumer-stub; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the inner_product/eigsolve/chebyshev in-line-marker route — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
variant_axes:
[new]:
edges:
  depends-on:
    - L4/inner_product
    - L3/nrm2
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/nrm2
variant_axes:
```

### (18) L4/sparameter_reduce — strike prose `lowers_to:` (a)

```edit:book/src/L4/sparameter_reduce.md
[old]:
consumes:
  - book/src/L4/frequency_sweep.md (firm — the driven solve-half map producing the per-ω solution family [E_ω] this reduction reduces over; the upstream composition-root stage)
lowers_to:
  - the per-port port-mode linear functional sᵢ·E (lumped (*s)·E / wave (E×H⋆)·n) by identity-in-form on the body; the per-entry self-term/scale is a scalar map. No dedicated L4>L3 theme — the in-line-marker route (the gram_reduce / inner_product / linear_combination pattern); in-line §"Lowers to"
variant_axes:
[new]:
edges:
  depends-on:
    - L4/frequency_sweep
variant_axes:
```

## Supporting evidence

**Linter mechanics:**
- Legacy keys migrated to `depends-on`: `graded_stack_lint.py:519-543` (`depends_on` / `lowers_to` / `lifts_from` / `lifts_to` / `consumes`). When an `edges:` dict is present it is read INSTEAD (`:502-516`), so the migration is the canonical fix.
- The `{'book/src/…` mis-parse: a list item containing `:` is read as a block-mapping `{target: …}` item (`:208-218`, `:211` `bm` regex), so a legacy item with a `:`-bearing prose qualifier stringifies to a dict in the unresolved list.
- `firmness:` already supplies `rank: firm` (`derive_rank`, `:431`), so removing legacy keys / adding `edges:` does not change any rank; `rank: None` deps (the concept pages) are warn-not-fail (`:614-615`), and I route them `reference` anyway.
- L0 `:lo-hi` cites are excluded from edges (`normalize_target` returns None, `:324`) — dispatch case (b) does not arise.

**Existence sweep (all clean slug targets EXIST on disk):** `L2/linear_combination`,
`L1/apply_linop`, `L1-L0/assemble-frequency-operator-rotation`, `L1/axpy`,
`L1-L0/fe-operator-assemble-mutation-rotation`, `L3/ksp_solve`, `L1/ksp_solve`,
`L2/assemble-diagonal`, `L2/divfree-projector`, `L2-L1/divfree-projector-leaf-identity`,
`L2/elementwise_product`, `L1/jacobi-smoother`, `L2/reciprocal`, `L1/reciprocal`,
`L4/linear_combination`, `concepts/black-box-vs-accelerated-kernels`,
`L1/assemble_frequency_operator`, `L4/inner_product`, `L3/dot`, `concepts/dot`,
`L4/eigsolve`, `L1/eigenvalue-untransform`, `L1/participation_ratio`, `L4/index`,
`concepts/state-stratification`, `L4-L3/fe-assemble-fold-dissolution`,
`L4/assemble_frequency_operator`, `L4/ksp_solve`, `L4/iterate-while`,
`L4-L3/frequency-sweep-dissolution`, `L3/inner_product`, `L3/linear_combination`,
`concepts/scalar-promotion`, `L3/nrm2`, `concepts/nrm2`, `L4/frequency_sweep`.

**Classification rationale (`depends-on` vs `reference`), per scheme §2/§5 / §(e):**
- `depends-on` (blocking; constrains rank + liveness): the firm vocabulary op/combinator
  the entry folds-through / specializes / consumes-as-a-constituent; the lowering-theme
  endpoints (`lowers_to`/`lifts_from`/`lifts_to`/`lowers_from` — a lowering edge IS a
  `depends-on` on both endpoints, §4 (a)). All such targets verified `rank: firm`.
- `reference` (navigational; constrains nothing): the **narrative-concept non-node
  pages** (`concepts/black-box-vs-accelerated-kernels`, `concepts/dot`, `concepts/nrm2`,
  `concepts/scalar-promotion`, `concepts/state-stratification` — disposition/framing
  pages, NOT data-shape record-definitions, so §5 non-node ⇒ `reference`), the
  **navigational-container** `L4/index` (§5 ratified container ⇒ never a blocking dep),
  and the kept-but-non-blocking sibling lowering theme `L2-L1/divfree-projector-leaf-identity`
  (a downstream-reachable see-also, not a constituent of the L3 entry's own composition).
  These also carry `rank: None` and so could never legitimately be `depends-on` blocking
  supports of a firm node.

**Before/after (simulated on a discarded temp copy of `book/src`; the report is
dispatch-phase, no `book/` write):**

```
BEFORE:  RESULT: 0 rank violation(s) ; UNRESOLVED depends-on targets (21)
AFTER :  RESULT: 0 rank violation(s) ; UNRESOLVED depends-on targets (1)
```

The residual `1` = `L4/solve_family` (WAVE-3, D3-owned, deferred — clears when D3 lands
its `edges:` block).

## Open questions / caveats

- **`graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon`** (linter
  observation, routed as a finding — I author frontmatter, not tool code). The 21→
  false-positive count is inflated by the linter mis-reading a *legacy* edge item whose
  prose qualifier contains `:` as a `{target: …}` block-mapping dict (`:208-218`). My
  migration removes the trigger for these 18 files, but **any remaining un-migrated file
  with a `:`-bearing legacy-edge qualifier will reproduce the artifact**. Two non-blocking
  options for a future tool pass: (i) have the legacy-key reader strip the trailing
  ` (…)` qualifier BEFORE the block-mapping test (mirror `normalize_target`'s paren-strip
  at `:317`), or (ii) skip the block-mapping branch for items under the legacy keys
  (block-mapping is a scheme-`edges:`-only surface form). Not actioned here (out of
  frontmatter scope); flagged so the P1 typed-edge campaign can decide whether to fix the
  reader or rely on migration-eliminates-the-trigger.
- **`L4/solve_family` last unresolved target — handed to D3** (see §WAVE-3 exclusion).
  Suggested `edges:` for D3: `depends-on: [L4/ksp_solve, L4/iterate-while,
  L4-L3/solve-family-map-dissolution]` (+ the prompt's `uses-record` → `op-params`,
  `sim-state`); `reference: [concepts/state-stratification]`. Drives unresolved → `0`.
- **`kind:` annotations are documentation only** (scheme §2; linters ignore them). I added
  `kind: folds`/`lowers-to`/`lifts-from`/`lifts-to`/`lowers-from`/`specializes` where the
  legacy key name carried that semantics, to preserve the human-readable edge-type that
  the legacy key encoded. If the integrator prefers bare-string edges, dropping every
  `kind:` is linter-equivalent (the bare-string and `{target:,kind:}` forms are
  interchangeable, §2).
- **No rank token added.** These 18 hosts remain rank-typed via `firmness: firm` (the
  §1 mapping `firmness → rank`). I deliberately did not add a redundant `rank: firm`
  line — it would be belt-and-suspenders and outside the "edges-correction-only" scope;
  the lazy-tail P1 campaign can normalize `firmness:` → `rank:` later if desired.
```
