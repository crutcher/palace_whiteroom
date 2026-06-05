---
agent: layer-intro-author
invoked_at: 2026-06-05T223620Z
scope: cycle-108 D1 — lowering-chain-liveness grounding pass (BC + divfree chains)
status: pending
integrated_at: 2026-06-05T230500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D1, cycle-108 batch-34 position 3/3, the BATCH-CLOSING cycle). 8 pre-scheme lowering-chain chapters typed with edges: blocks (4 authored from scratch, 4 legacy→scheme), grounding the L1/L0 BC+divfree lowering homes from their already-reachable L4/L3 sources. reachable 95→102 (+7 nodes rescued), 0 regression, rank_violations HELD 0. Faithful — caught the essential_dofs would-be over-edge. cargo make book EXIT 0; no finalize build-repair. Resolved OQ lowering-chain-liveness-not-propagated-to-l1-ops grounded-and-rescued; routed l2-l1-theme-cohort-reachability-gap + lowering-theme-reachability-vs-well-foundedness-scheme-clarification to the batch-34 meta-phase. All per-report safety-net gates PASS/N/A; global retroactive-budget 0."
---

# CYCLE: lowering-chain-liveness grounding — type the missing `edges:` blocks down the BC + divfree chains

## Summary

Discharges the ONE carried follow-up `lowering-chain-liveness-not-propagated-to-l1-ops` (c107 D1
routed OQ) as a systematic **`lowers-to` typed-edge GROUNDING pass** (per the 2026-06-05 grounding
directive). After c107 grounded the BC/divfree clusters at L4/L3, their L1/L0 lowering homes stayed
unreachable because the intervening pre-scheme chapters carried NO machine-readable `edges:` block —
so the reachable L_n op's `lowers-to` edge to its L_{n-1} home was never traversed (the mark-sweep
dead-ended at the untyped intermediate). This pass types the missing `edges:` on 8 chapters down the
two chains so liveness propagates.

**Result (dry-run-validated against the real linter via `--book-src`):**
- `reachable from roots`: **95 → 102** (+7) — all 7 target nodes flipped `[garbage?]`/`[GARBAGE*]` → reachable.
- `detritus`: **163 → 156** (−7).
- `rank_violations`: **HOLDS 0** (every typed `depends-on` edge rests firm-on-firm; well-foundedness holds).
- `unresolved depends-on targets`: **0** (no broken slugs; the `cites-evidence` L0 source paths resolve as rank-terminal ground truth, matching the `set-subvector-zero-mutation-rotation` precedent).
- No regression: no previously-reachable node became garbage.

All 7 rescued nodes: `L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L1/essential_dofs`,
`L1/divfree-projector`, `L2/divfree-projector`, `L1-L0/divfree-projector-mutation-rotation`,
`L1-L0/essential-dofs-construction-rotation` — plus `L2-L1/divfree-projector-leaf-identity`
(the 8th, see "One faithful refinement beyond the planner's literal edge set" below).

**OQ resolution:** `lowering-chain-liveness-not-propagated-to-l1-ops` → **RESOLVED (grounded-and-rescued)**.
Every leg the planner scoped was a REAL, prose-witnessed lowering; none required routing as a finding.

## Faithfulness audit (verify-before-typing — done per leg)

Every edge below was confirmed against the on-disk chapter prose (and L0 anchors spot-verified via
`tools/citecheck/citecheck.py --anchor`, all `[ok]`):

**BC chain (dissolves DIRECTLY L4→L1, no interposed L3/L2 BC entry — warranted at
`bc-elimination-post-composition-dissolution.md:105,:114-121`):**
- `bc-elimination-post-composition-dissolution` `lowers-to` → `eliminate_essential_bc` (operator-side
  deferred-config-then-apply, `:35-57`) + `eliminate_rhs` (RHS-side in-place pooled-scratch loop,
  `:59-81`). **Faithful** — the theme's two §sections ARE these two L1 verbs.
- The theme does **NOT** `lowers-to` `essential_dofs` — the prose explicitly states *"This theme
  consumes `DofSet[N]` as a given operand"* (`:99-101`) and routes its construction to its own
  `essential-dofs-construction-rotation` theme. So `essential_dofs` is a `reference` (consumed
  operand), NOT a dissolution source. This is the faithful-path-or-finding discipline catching a
  would-be over-edge: `essential_dofs` reaches root instead via `eliminate_essential_bc uses
  essential_dofs` (the real consume edge — the `DofSet[N]` `eliminate_essential_bc` consumes,
  `eliminate_essential_bc.md:70-72`).
- `eliminate_essential_bc` `lowers-to` → `L1-L0/fe-operator-assemble-mutation-rotation` (already in
  legacy `lowers_to:`; preserved as a typed edge). `essential_dofs` `lowers-to` →
  `L1-L0/essential-dofs-construction-rotation` (already legacy; preserved).
- `eliminate_rhs` already carried a scheme-conformant `edges:` block with its `lowers-to →
  L1-L0/fe-operator-assemble-mutation-rotation` — **confirmed, left untouched** (the planner's
  "confirm/leave").

**divfree chain:**
- `L2/divfree-projector` (the c107 dead-end, NO frontmatter today) → authored `edges:` from scratch:
  `lowers-to → L1/divfree-projector` + `depends-on → L2/ksp_solve` (the inner projected-H1 solve,
  step 3) + references. **Faithful** — the L2 §Dependencies names `ksp_solve` as the direct
  load-bearing inner gate and the L1 entry as the lowering target.
- `L1/divfree-projector` (NO frontmatter today) → authored `edges:`: `lowers-to →
  L1-L0/divfree-projector-mutation-rotation` + `depends-on → {ksp_solve, apply_linop, axpy}` (the
  four-step constituents named in its §Semantics/§Dependencies). **Faithful.**
- `L2-L1/divfree-projector-leaf-identity` + `L1-L0/divfree-projector-mutation-rotation` +
  `L1-L0/essential-dofs-construction-rotation` → authored `edges:` from scratch as lowering-theme
  leaves (`lifts-from`/`lowers-to` endpoints + `cites-evidence` L0). **Faithful** — endpoints are the
  themes' own stated LHS/RHS; L0 anchors are the themes' own Evidence sections.

## One faithful refinement beyond the planner's literal edge set

The planner's edge set typed the divfree operator spine `L2/divfree → L1/divfree` (operator→operator).
That alone left `L2-L1/divfree-projector-leaf-identity` STILL garbage — and the diagnosis is a real
**convention asymmetry worth flagging**:

- **L1 ops reach their L1>L0 theme** because their `lowers_to:` points operator→**theme** (e.g.
  `eliminate_essential_bc lowers_to L1-L0/fe-operator-assemble-mutation-rotation`). So typing the L1
  op rescues its L1-L0 theme automatically.
- **L2/L3 ops reach the next operator** because their `lowers-to` points operator→**operator** (e.g.
  the already-scheme-typed `L3/divfree lowers-to L2/divfree`). The L2-L1 *theme* is only ever a
  `reference` target — so **ALL 11 L2-L1 themes are uniformly `[garbage?]`** today, not just this one.

To rescue `L2-L1/divfree-projector-leaf-identity` faithfully I added **`L2/divfree-projector lowers-to
L2-L1/divfree-projector-leaf-identity`** (operator→theme), mirroring exactly how L1 ops reach their
L1-L0 themes. This is faithful (the L2 floor genuinely lowers to L1 *via* that theme) and is the
in-spirit completion of the grounding directive for the divfree chain. It is the +1 that takes the
delta from +6 to +7.

**FINDING (flagged, not actioned — out of this dispatch's BC+divfree scope):** the other **10 L2-L1
themes remain `[garbage?]`** for the identical reason (their L2 op points operator→operator at the L1
op, never operator→theme at the L2-L1 theme). This is a **systematic L2-L1-theme-cohort reachability
gap** — the L2-L1 analog of the lowering-chain-liveness pattern this dispatch closed for the BC/L1-L0
legs. A bounded one-edge-per-theme follow-up (add an `L2/<op> lowers-to L2-L1/<op>-theme` edge to each
L2 op that already carries scheme frontmatter) would rescue all 10. Recommend routing to the batch-34
meta-phase as a sibling of the carried `set_subvector_zero` L1-L0 leg note (planner OQ caveat). I did
NOT scope it here to keep this batch-closing dispatch bounded to the BC+divfree chains.

## Verification evidence (dry-run against the real linter)

Validated by copying `book/src` to a temp tree, applying every proposed edit, and running
`graded_stack_lint.py --book-src <temp>`. Before = real tree; after = temp tree with all edits.

```
BEFORE (real tree)                          AFTER (temp tree, all edits applied)
  RESULT: 0 rank, 163 detritus, 61 untyped    RESULT: 0 rank, 156 detritus, 61 untyped
  reachable from roots: 95                     reachable from roots: 102

  [GARBAGE*] L1/eliminate_essential_bc    →   L1/eliminate_essential_bc  <-  L4-L3/bc-elimination-post-composition-dissolution
  [GARBAGE*] L1/eliminate_rhs             →   L1/eliminate_rhs           <-  L4-L3/bc-elimination-post-composition-dissolution
  [GARBAGE*] L1/essential_dofs            →   L1/essential_dofs          <-  L1-L0/essential-dofs-construction-rotation, L1/eliminate_essential_bc
  [garbage?] L1/divfree-projector         →   L1/divfree-projector       <-  L1-L0/divfree-projector-mutation-rotation, L2-L1/divfree-projector-leaf-identity, L2/divfree-projector
  [garbage?] L1-L0/divfree-projector-...  →   L1-L0/divfree-projector-mutation-rotation  <-  L1/divfree-projector
  [garbage?] L1-L0/essential-dofs-...     →   L1-L0/essential-dofs-construction-rotation <-  L1/essential_dofs
  [garbage?] L2-L1/divfree-projector-...  →   L2-L1/divfree-projector-leaf-identity      <-  L2/divfree-projector
  (L2/divfree-projector reachable, no out)→   L2/divfree-projector       <-  L2-L1/divfree-projector-leaf-identity, L3/divfree-projector
```

`RANK VIOLATIONS: none.` and zero unresolved depends-on targets in the after-tree.

L0 anchors spot-verified (`citecheck --anchor`, all `[ok]`):
`palace/linalg/divfree.cpp:155-187` (anchor `Mult`), `palace/fem/multigrid.hpp:92-101` (anchor
`dbc`), `palace/utils/geodata.hpp:75-96` (anchor `AttrToMarker`), `palace/linalg/rap.cpp:56-83`
(anchor `EliminateRHS`).

## Proposed changes

### 1. `book/src/L4-L3/bc-elimination-post-composition-dissolution.md` — replace legacy `lhs:/rhs:` with `edges:`

```edit:book/src/L4-L3/bc-elimination-post-composition-dissolution.md
[old]:
---
layer: L4-L3
theme: bc-elimination-post-composition-dissolution
firmness: firm
lhs: book/src/L4/eliminate_bc.md
rhs:
  - book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (operator-side deferred-config-then-apply)
  - book/src/L1/eliminate_rhs.md (RHS-side in-place pooled-scratch loop)
justification_kind: structural
---
[new]:
---
layer: L4-L3
theme: bc-elimination-post-composition-dissolution
firmness: firm
justification_kind: structural
# Graded-stack scheme: lowering theme. This theme dissolves the L4 eliminate_bc
# verb-pair DIRECTLY to its two L1 sources (no interposed L3/eliminate_bc entry —
# warranted on-disk at :105,:114-121). rank = min(endpoints); both endpoints firm
# (rank 3) and the L4 source is firm, so the theme is firm. rank(theme) <= min holds.
rank: firm
edges:
  depends-on:
    - target: L4/eliminate_bc
      kind: lifts-from            # the L4 source verb-pair this theme lowers (the LHS)
    - target: L1/eliminate_essential_bc
      kind: lowers-to             # operator-side: deferred-config-then-apply (:35)
    - target: L1/eliminate_rhs
      kind: lowers-to             # RHS-side: in-place pooled-scratch loop (:59-61)
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to             # the operator-pin L1>L0 half this L4>L3 half composes with
  reference:
    - L4/eliminate_bc
    - L1/essential_dofs           # the DofSet[N] consumed as a given operand (:99-101; own construction theme)
    - L4-L3/fe-assemble-fold-dissolution   # the assemble-fold sibling theme
---
```

### 2. `book/src/L1/eliminate_essential_bc.md` — replace legacy frontmatter with `edges:` block

```edit:book/src/L1/eliminate_essential_bc.md
[old]:
---
layer: L1
operator: eliminate_essential_bc
firmness: firm
lowers_to:
  - L1-L0/fe-operator-assemble-mutation-rotation
lifts_from: []
depends_on: []
variant_axes:
  - diagonal-policy
  - trial-test-coincidence
---
[new]:
---
layer: L1
operator: eliminate_essential_bc
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L1/essential_dofs
      kind: uses                  # consumes the DofSet[N] essential_dofs constructs (:70-72)
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation home
  reference:
    - L1/fe_assemble              # composes AFTER fe_assemble (separable post-composition)
    - L1/eliminate_rhs            # sibling BC verb (the RHS-lift half of the pair)
variant_axes:
  - diagonal-policy
  - trial-test-coincidence
---
```

### 3. `book/src/L1/essential_dofs.md` — replace legacy frontmatter with `edges:` block

```edit:book/src/L1/essential_dofs.md
[old]:
---
status: firm
harvested_by: harvester:2026-06-02T164202Z-harvester-essential-dofs
cycle: cycle-066
layer: L1
operator: essential_dofs
firmness: firm
lowers_to:
  - L1-L0/essential-dofs-construction-rotation
lifts_from: []
depends_on: []
variant_axes:
  - attribute-wildcard
  - per-level-hierarchy-application
---
[new]:
---
status: firm
harvested_by: harvester:2026-06-02T164202Z-harvester-essential-dofs
cycle: cycle-066
layer: L1
operator: essential_dofs
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L1-L0/essential-dofs-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation home
  reference:
    - L1/fe_space                 # the FiniteElementSpace[N] the DofSet is built over
    - L1/eliminate_essential_bc   # consumer of the DofSet[N]
    - L1/eliminate_rhs            # consumer of the DofSet[N]
variant_axes:
  - attribute-wildcard
  - per-level-hierarchy-application
---
```

### 4. `book/src/L1-L0/essential-dofs-construction-rotation.md` — prepend `edges:` frontmatter (no frontmatter today)

```edit:book/src/L1-L0/essential-dofs-construction-rotation.md
[old]:
# essential-dofs-construction-rotation

**Slug:** `essential-dofs-construction-rotation`
[new]:
---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (essential_dofs) is firm (rank 3); the L0 endpoint is rank-terminal ground
# truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/essential_dofs
      kind: lowers-to             # the L1 source construction this theme lowers
    - target: palace/fem/multigrid.hpp:92-101
      kind: cites-evidence        # the dbc block in ConstructFiniteElementSpaceHierarchy
    - target: palace/utils/geodata.hpp:75-96
      kind: cites-evidence        # mesh::AttrToMarker (Palace-authored marker constructor)
    - target: palace/fem/multigrid.hpp:99-100
      kind: cites-evidence        # GetEssentialTrueDofs (MFEM-owned-read-as-given tail)
  reference:
    - L1-L0/fe-space-construction-rotation        # sibling construction-lowers/bookkeeping-MFEM-owned split
    - L1-L0/fe-operator-assemble-mutation-rotation # the BC-elimination consumer theme
---

# essential-dofs-construction-rotation

**Slug:** `essential-dofs-construction-rotation`
```

### 5. `book/src/L2/divfree-projector.md` — author `edges:` frontmatter from scratch (the c107 dead-end; NO frontmatter today)

```edit:book/src/L2/divfree-projector.md
[old]:
# divfree-projector

The divergence-free Helmholtz-projection **constructed-operator gate** at the fusion-rotation
[new]:
---
layer: L2
operator: divfree-projector
firmness: firm
# Graded-stack scheme: this L2 fusion-rotation floor lowers to the L1 divfree-projector
# gate (lowers-to depends-on) AND through the L2>L1 lowering theme (mirrors how L1 ops reach
# their L1>L0 theme). Its inner gate is the firm L2 ksp_solve (depends-on). Edges to the L3
# consumer + L1 step-anchors + concepts are navigational references. All depends-on targets
# firm (rank 3); this node firm (rank 3); well-foundedness holds.
rank: firm
edges:
  depends-on:
    - target: L1/divfree-projector
      kind: lowers-to             # the L1 mutation-rotation gate this L2 floor lowers to
    - target: L2-L1/divfree-projector-leaf-identity
      kind: lowers-to             # the L2>L1 lowering theme this floor lowers through (mirrors how L1 ops reach their L1>L0 theme)
    - L2/ksp_solve                # the inner projected-H1 solve (step 3); nested-gate inner gate
  reference:
    - L3/divfree-projector        # the L3 consumer this floor parents
    - L1/apply_linop              # step-1 / step-4 apply (L1 anchor; no L2 chapter)
    - L1/axpy                     # step-4 accumulate (L1 anchor; no L2 chapter)
    - concepts/set_subvector_zero
    - concepts/nested-constructed-operator-gate
    - concepts/sequential-obstruction
---

# divfree-projector

The divergence-free Helmholtz-projection **constructed-operator gate** at the fusion-rotation
```

### 6. `book/src/L1/divfree-projector.md` — author `edges:` frontmatter from scratch (NO frontmatter today)

```edit:book/src/L1/divfree-projector.md
[old]:
# divfree-projector

Mutation-lifted divergence-free projector: a pure-functional linear projection
[new]:
---
layer: L1
operator: divfree-projector
firmness: firm
# Graded-stack scheme: this L1 mutation-rotation gate lowers to its L1>L0 mutation-rotation
# theme (lowers-to depends-on). Its inner gate is the firm L1 ksp_solve (depends-on). The
# step constituents (apply_linop, axpy) are depends-on. All firm (rank 3); this node firm
# (rank 3); well-foundedness holds.
rank: firm
edges:
  depends-on:
    - target: L1-L0/divfree-projector-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation home
    - L1/ksp_solve                # the inner projected-H1 solve (step 3)
    - L1/apply_linop              # step-1 WeakDiv apply + step-4 Grad apply
    - L1/axpy                     # step-4 additive gradient correction
  reference:
    - L2/divfree-projector        # the L2 fusion-rotation floor above
    - concepts/set_subvector_zero # the Z_{bdr_eff} essential-BC zeroing (step 2)
    - concepts/nested-constructed-operator-gate
    - concepts/constructed-operators
---

# divfree-projector

Mutation-lifted divergence-free projector: a pure-functional linear projection
```

### 7. `book/src/L2-L1/divfree-projector-leaf-identity.md` — prepend `edges:` frontmatter (no frontmatter today)

```edit:book/src/L2-L1/divfree-projector-leaf-identity.md
[old]:
# divfree-projector-leaf-identity

The L2>L1 lowering theme for the `divfree-projector` constructed-operator gate. The rewrite is
[new]:
---
# Lowering theme (L2>L1). Per graded-stack scheme §5: rank = min(endpoint ranks). Both
# endpoints (L2 + L1 divfree-projector) are firm (rank 3); so the theme is firm and
# rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L2/divfree-projector
      kind: lifts-from            # the L2 fusion-rotation floor (LHS)
    - target: L1/divfree-projector
      kind: lowers-to             # the L1 mutation-rotation gate (RHS)
  reference:
    - L2/ksp_solve                # the inner-solve obstruction carried by reference
    - L1-L0/divfree-projector-mutation-rotation  # the L1>L0 sibling leg
---

# divfree-projector-leaf-identity

The L2>L1 lowering theme for the `divfree-projector` constructed-operator gate. The rewrite is
```

### 8. `book/src/L1-L0/divfree-projector-mutation-rotation.md` — prepend `edges:` frontmatter (no frontmatter today)

```edit:book/src/L1-L0/divfree-projector-mutation-rotation.md
[old]:
# divfree-projector-mutation-rotation

The mutation rotation for the divergence-free projector apply. Lowers the pure
[new]:
---
# Lowering theme (L1>L0). Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (divfree-projector) is firm (rank 3); the L0 endpoint is rank-terminal ground
# truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/divfree-projector
      kind: lowers-to             # the L1 source gate this theme lowers
    - target: palace/linalg/divfree.cpp:155-187
      kind: cites-evidence        # DivFreeSolver<VecType>::Mult — the in-place four-step apply
    - target: palace/linalg/divfree.cpp:43-152
      kind: cites-evidence        # the constructor materialising the L1 closure fields
    - target: palace/linalg/divfree.hpp:55
      kind: cites-evidence        # `mutable VecType psi, rhs;` — the construction-bound scratch
  reference:
    - L1-L0/set-subvector-zero-mutation-rotation  # the step-2 zeroing leaf
    - L2-L1/divfree-projector-leaf-identity       # the L2>L1 sibling leg
---

# divfree-projector-mutation-rotation

The mutation rotation for the divergence-free projector apply. Lowers the pure
```

## Supporting evidence

- The two chains' lowering relationships are documented in the chapter prose (not invented):
  - BC: `bc-elimination-post-composition-dissolution.md:35-57` (operator-side → `eliminate_essential_bc`),
    `:59-81` (RHS-side → `eliminate_rhs`), `:99-101` (`essential_dofs` consumed as operand, NOT
    dissolved), `:105,:114-121` (DISSOLUTION-HOME warrant: no interposed L3/eliminate_bc).
  - divfree: `L2/divfree-projector.md:114-135` (four-step apply), §Dependencies `:264-309` (inner
    `ksp_solve`; `apply_linop`/`axpy` step constituents; L1 lowering target); `L1/divfree-projector.md`
    §Semantics/§Dependencies; the two divfree theme leaves' own §"L0 form"/§Evidence sections.
- Scheme conventions followed: `book/src/methodology/graded-stack-scheme.md` §2 (block-mapping edge
  form `- target:/  kind:`), §5 (lowering-theme rank = min(endpoints); `cites-evidence` to L0 source).
  Precedent pattern: `book/src/L1-L0/set-subvector-zero-mutation-rotation.md` (firm L1-L0 theme with
  `lowers-to` L1 endpoint + `cites-evidence` L0 source paths + `reference` siblings).
- All depends-on edges rest firm-on-firm (every endpoint surveyed from its on-disk `## Status` /
  `firmness:` line = firm): `eliminate_essential_bc`, `eliminate_rhs`, `essential_dofs`,
  `L1/divfree-projector`, `L2/divfree-projector`, `L3/divfree-projector`, `L2/ksp_solve`,
  `L1/ksp_solve`, `L1/apply_linop`, `L1/axpy`, `fe-operator-assemble-mutation-rotation`,
  `essential-dofs-construction-rotation`, `divfree-projector-mutation-rotation`,
  `divfree-projector-leaf-identity` — all firm. L0 source paths are rank-terminal ground truth.

## Open questions / caveats

- **RESOLVED:** `lowering-chain-liveness-not-propagated-to-l1-ops` → grounded-and-rescued for ALL
  scoped legs (BC + divfree). +7 reachable, −7 detritus, 0 rank violations. No leg needed routing as a
  finding — every scoped lowering was real.

- **FINDING (flag for batch-34 meta-phase — systematic L2-L1-theme-cohort reachability gap):** the
  other **10 L2-L1 lowering themes** (`chebyshev-iteration-fusion`, `deflate-composition-lowering`,
  `eigsolve-spectral-transform-composition`, `gram-fold-specialization`,
  `incremental-least-squares-composition-lowering`, `inner-product-fold-specialization`,
  `krylov-step-kernel-defusion`, `ksp-solve-outer-driver-unfold`,
  `linear-combination-fold-specialization`, `orthogonalize-composition-lowering`) are ALL still
  `[garbage?]` for the IDENTICAL reason this dispatch fixed for `divfree-projector-leaf-identity`: the
  established L2/L3 `lowers-to` convention points operator→operator (L2 op → L1 op), never
  operator→theme — so the L2-L1 theme is only ever a `reference` target and never on the `depends-on`
  spine. (Contrast L1 ops, whose `lowers_to:` points operator→theme, so typing the L1 op rescues its
  L1-L0 theme automatically.) The bounded fix is one edge per theme: add `L2/<op> lowers-to
  L2-L1/<op>-theme` to each L2 op that already carries scheme frontmatter (mirroring edit #5 here).
  This rescues ~10 nodes. I did NOT scope it (out of the BC+divfree chains; batch-closing-bounded
  discipline) — recommend a dedicated bounded follow-up, a sibling of the planner-flagged
  `set_subvector_zero` L1-L0 leg note.

- **Convention observation (for the scheme doc / meta-phase):** the asymmetry above — L1-op
  `lowers_to` targets the L1-L0 *theme*; L2/L3-op `lowers-to` targets the next *operator* — means the
  reachability of a lowering theme depends on whether its UPPER-endpoint operator points at the theme
  vs. at the lower operator. The graded-stack-scheme §5 lowering-theme rule (theme `edges:` lists both
  endpoints + rank = min) makes the theme well-founded, but does NOT itself make the theme reachable
  unless a reachable node `depends-on` it. Worth a one-line note in `graded-stack-scheme.md` §5: a
  lowering theme is reachable iff its upper endpoint carries a `lowers-to` edge AT the theme (not only
  at the lower operator). The BC + L1-L0 legs satisfy this natively (L1 ops point at their theme); the
  L2-L1 cohort does not (the finding above).
