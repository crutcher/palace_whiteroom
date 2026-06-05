---
agent: layer-intro-author
invoked_at: 2026-06-05T211311Z
scope: cycle-107 D2 — strict-zero concept pages get ratified non-node reference-only edges blocks (item-3c lazy tail)
status: pending
integrated_at: 2026-06-05T223500Z
integration_commit: 24c3e71
integration_notes: "Applied clean (staging row D2). 15 of the 16 strict-zero non-node concept pages got the batch-33-ratified reference-only edges: block (NO rank:); untyped 76->61 (-15), typed 279->294, reachable HELD 95, rank_violations HELD 0, unresolved_depends_on_targets HELD 0, build EXIT 0. The 16th page concepts/counter-update DELIBERATELY DEFERRED (a node needing rank:, not a non-node) — captured by promoted OQ concepts-counter-update-needs-node-rank-and-depends-on-edges, routed to batch-34; no live rank/liveness impact. The detritus rise 149->163 (+14) is the untyped->typed-non-node reclassification (the 14 newly-typed pages carry no liveness), NOT a regression — 0 nodes lost reachability (verified by git-stash set-diff). No finalize build-repair."
---

# CYCLE: strict-zero concept pages → non-node `reference`-only `edges:` blocks

## Summary

Authors the batch-33-ratified **non-node concept-page encoding** (`graded-stack-scheme.md`
§5/§6, §6 checklist step 4) — a `reference`-only `edges:` block, **NO `rank:`** — onto
**15** of the 16 strict-zero concept pages identified by the cycle-107 planner (D2 section)
that currently carry zero `edges:` frontmatter. These are non-node narrative / layer-pattern
/ concept-framing pages: they assert no blocking dependency, so every see-also link is a
`reference` edge (machine-readable for the reachability-GC author, uniform with the
navigational-container convention, zero linter-invariance cost).

**`counter-update` is DEFERRED from this dispatch** (the 16th page) — see Open questions:
the batch-33 §5 reconciliation ratifies `counter-update` → **node** (sole-definition site of
the L2 `counter_update` primitive), which requires a `rank:` + classified `depends-on` edges,
not the non-node `reference`-only treatment this LOW lazy-tail dispatch authors. On disk it has
no `## Status` line and no firm apparatus, so deriving a `rank:` would be a guess; per the
planner OQ I defer it to a dedicated record/definition-node pass + flag for the batch-34
meta-phase rather than guess.

Pure frontmatter typing — no prose/semantics changes.

## Linter before / after (real run, scratch tree)

Run against a scratch copy of `book/src` (under `/tmp`, NOT `book/`) with the 15 proposed
blocks applied; `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src <scratch>`:

```
BEFORE:  RESULT: 0 rank violation(s), 156 detritus node(s), 76 untyped (warning).
AFTER:   RESULT: 0 rank violation(s), 170 detritus node(s), 61 untyped (warning).
```

- **`untyped`: 76 → 61** — drops by exactly the 15 typed pages (linter line 551:
  `node.untyped = (rank is None and not read_any_edge)`; a `reference`-only block sets
  `read_any_edge=True` → no longer untyped). Toward the planner's ~60 target.
- **`rank_violations`: 0 → 0** (HELD) — no `rank:` and no `depends-on` added, so the
  well-foundedness check is untouched.
- **`--strict` reports NO unresolved reference targets and NO errors** — every `reference`
  slug was verified to resolve on-disk (`book/src/<slug>.md` exists) before emitting.
- **No new *node* orphaned.** The detritus count rises 156 → 170 because 14 of the 15 pages
  move from the *untyped-detritus* bucket into the *typed-but-non-node-detritus* bucket — the
  **identical, expected** disposition the pre-existing `reference`-only concept pages already
  hold: `concepts/{dot,nrm2,scal,apply_linop,axpy}` ALL read `[garbage?]` in the current tree.
  A non-node narrative page carrying only `reference` edges carries no liveness, so it stays
  correctly-unreachable (it is documentation, not a DAG node). This is the convention working
  as designed, not a regression. (1 of the 15 — `concepts/solve-monad` — became fully clean,
  i.e. left both lists, because it has an inbound `L4/eigsolve <- ... -> solve-monad`
  navigational edge the GC now sees; a bonus, not a problem.)

## Proposed changes

Each page currently has NO frontmatter; the proposed change prepends a `reference`-only
`edges:` block immediately before the page's first line (the `# <title>` heading). Slugs use
the on-disk bare-slug convention (`L1/...`, `L2/...`, `concepts/...`, `L4/...`, `L1-L0/...`,
`L3-L2/...`), matching the sibling `concepts/axpy.md` / `concepts/apply_linop.md` blocks. Every
target was existence-verified on-disk.

```edit:book/src/concepts/build-time-vs-run-time-stratification.md
[old]: # build-time-vs-run-time-stratification
[new]: ---
edges:
  reference:
    - concepts/constructed-operator-factory
    - concepts/finest-level-unwrap
    - concepts/apply_linop
    - concepts/axpy
    - concepts/dot
    - concepts/solve-monad
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/sequential-obstruction
    - L4/preconditioning-framework
---
# build-time-vs-run-time-stratification
```

```edit:book/src/concepts/capability-typing.md
[old]: # capability-typing
[new]: ---
edges:
  reference:
    - concepts/state-stratification
    - concepts/variant-absorption
    - concepts/solve-monad
    - L4/preconditioning-framework
---
# capability-typing
```

```edit:book/src/concepts/chebyshev-iteration.md
[old]: # Chebyshev iteration
[new]: ---
edges:
  reference:
    - concepts/apply_linop
    - concepts/axpy
    - concepts/scal
    - concepts/nrm2
    - concepts/dot
---
# Chebyshev iteration
```

```edit:book/src/concepts/constructed-operator-factory.md
[old]: # constructed-operator-factory
[new]: ---
edges:
  reference:
    - concepts/apply_linop
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/solver-as-operator
    - concepts/rotation
    - L4/preconditioning-framework
---
# constructed-operator-factory
```

```edit:book/src/concepts/constructed-operators.md
[old]: # constructed operators
[new]: ---
edges:
  reference:
    - concepts/rotation
    - concepts/variant-absorption
    - concepts/apply_BA
    - L2/krylov-step
---
# constructed operators
```

```edit:book/src/concepts/convergence-test.md
[old]: # convergence-test
[new]: ---
edges:
  reference:
    - concepts/variant-absorption
    - concepts/constructed-operators
    - concepts/solve-monad
---
# convergence-test
```

```edit:book/src/concepts/derived-view-hoisting.md
[old]: # Derived-view hoisting
[new]: ---
edges:
  reference:
    - L2/krylov-step
    - concepts/variant-absorption
    - concepts/rotation
    - concepts/tensor-field-lift
    - concepts/sequential-obstruction
---
# Derived-view hoisting
```

```edit:book/src/concepts/eigsolve.md
[old]: # eigsolve
[new]: ---
edges:
  reference:
    - L1/eigsolve
    - L2/eigsolve
    - L3/eigsolve
    - L0/eigensolver-wrapper
    - concepts/ksp_solve
    - concepts/solver-as-operator
    - concepts/sequential-obstruction
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/solve-monad
    - concepts/apply_linop
    - L1/apply_nonlinear_pencil
    - L1/nleps_jacobian_action
    - L1/nleps_eigenvalue_correction
    - L1/nleps_deflated_residual
    - L1/nleps_deflated_solve
    - L1-L0/eigsolve-mutation-rotation
    - L1-L0/eigsolve-convergence-reason-mapping
---
# eigsolve
```

```edit:book/src/concepts/erasure-scope.md
[old]: # Concept: erasure-scope
[new]: ---
edges:
  reference:
    - concepts/sequential-obstruction
    - concepts/tensor-field-lift
    - L3-L2/ksp-solve-outer-driver
    - L3/ksp_solve
    - L2/ksp_solve
    - L3-L2/orthogonalize-variant-split
    - L3/orthogonalize
    - L2/orthogonalize
    - L3-L2/chebyshev-nested-recurrence
    - L3/chebyshev
    - L2/chebyshev-iteration
    - L3-L2/eigsolve-opaque-eigen-iteration
    - L3/eigsolve
    - L2/eigsolve
---
# Concept: erasure-scope
```

```edit:book/src/concepts/ksp_solve.md
[old]: # ksp_solve
[new]: ---
edges:
  reference:
    - L1/ksp_solve
    - concepts/apply_linop
    - concepts/constructed-operators
---
# ksp_solve
```

```edit:book/src/concepts/nested-constructed-operator-gate.md
[old]: # nested-constructed-operator-gate
[new]: ---
edges:
  reference:
    - concepts/constructed-operators
    - concepts/constructed-operator-factory
    - concepts/solver-as-operator
    - concepts/ksp_solve
    - concepts/variant-absorption
    - L1/eigsolve
    - L1/divfree-projector
    - L1/floquet-correction
    - L1/jacobi-smoother
    - L1/chebyshev-smoother
    - L1/ksp_solve
    - L1-L0/eigsolve-mutation-rotation
---
# nested-constructed-operator-gate
```

```edit:book/src/concepts/rotation.md
[old]: # rotation
[new]: ---
edges:
  reference:
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/apply_BA
---
# rotation
```

```edit:book/src/concepts/solve-monad.md
[old]: # solve-monad
[new]: ---
edges:
  reference:
    - concepts/state-stratification
    - concepts/constructed-operators
    - concepts/sequential-obstruction
    - L2/krylov-step
---
# solve-monad
```

```edit:book/src/concepts/solver-as-operator.md
[old]: # solver-as-operator
[new]: ---
edges:
  reference:
    - concepts/apply_linop
    - concepts/constructed-operators
    - concepts/constructed-operator-factory
    - concepts/variant-absorption
    - concepts/rotation
    - L4/preconditioning-framework
---
# solver-as-operator
```

```edit:book/src/concepts/state-stratification.md
[old]: # state-stratification
[new]: ---
edges:
  reference:
    - concepts/solve-monad
    - concepts/constructed-operators
    - concepts/sequential-obstruction
    - L2/krylov-step
---
# state-stratification
```

## Supporting evidence

- **Reference material read:** `.claude/agents/layer-intro-author.md` §(e); `book/src/methodology/graded-stack-scheme.md`
  §5 (non-node concept-page encoding — UNIFIED) + §6 checklist step 4; cycle-107 planner
  `reports/2026-06-05T211311Z-cycle-planner-cycle-107/CYCLE.md` D2 section.
- **Slug convention** confirmed against the two sibling pages D4 last cycle cited
  (`concepts/axpy.md`, `concepts/apply_linop.md`) — bare slugs `L1/...`, `L2/...`, `concepts/...`,
  no `book/src/` prefix, no `.md` suffix.
- **On-disk no-`edges:` confirmation** (`grep -L '^edges:' book/src/concepts/*.md`): all 16 planner
  pages genuinely lack `edges:` frontmatter.
- **Every `reference` target existence-verified** on-disk (`book/src/<slug>.md` exists) — full check
  passed for all ~45 distinct targets across the 15 blocks; `--strict` linter run reports zero
  unresolved targets.
- **Target selection** = each page's in-body markdown links (its authoritative L_n operator home(s) +
  the sibling concepts / themes / use-sites it narrates) — faithfully "the pages it points-at," no
  invented edges. Prose `see the cg slice` style mentions with NO live link target (`L2/cg`,
  `L2/gmres` do not exist) were NOT manufactured into edges.
- **D1/D2 disjointness re-confirmed:** D1 touches `concepts/{dofset,set_subvector_zero}`, feature
  columns, `L4/{fe_assemble,eliminate_bc}`, `L3/divfree-projector`, `L1/set_subvector_zero` — NONE of
  which appear in this dispatch's 15 (or the deferred `counter-update`). The `concepts/{eigsolve,ksp_solve}`
  pages typed here are distinct files from the `L4/{eigsolve,ksp_solve}` op-chapters; D1 touches neither
  `concepts/` page. Write-sets are disjoint.

## Open questions / caveats

- **`counter-update` DEFERRED (the 16th planner page) — node-vs-non-node, ratified→node but rank
  unguessable here.** The batch-33 §5 reconciliation ratifies `counter-update` → **node**
  ("sole-definition site of an L2 primitive a real node `depends-on`"), confirmed on-disk: there is
  no `L1/counter-update` / `L2/counter-update` operator chapter — `concepts/counter-update.md` IS the
  sole home defining the L2 `counter_update` primitive, and it is referenced as a primitive by
  `L3/krylov-step`, `L4/preconditioning-framework`, and `L1-L0/ksp-solve-mutation-rotation`. BUT:
  (i) making it a node requires a `rank:` + classified `depends-on` edges, which is NOT the non-node
  `reference`-only treatment this LOW lazy-tail dispatch authors; (ii) the page has no `## Status`
  line and no firm apparatus (no Signature/Algebraic-laws/Evidence section), so deriving its `rank:`
  would be a guess — and the project rule is to survey firmness from the on-disk `## Status`, never
  invent it. Per the planner OQ ("default the most-conservative reading and flag for the next
  meta-phase rather than guess a `rank:`"), I author NO edges on `counter-update` this cycle and
  **flag `concepts-counter-update-needs-node-rank-and-depends-on-edges`** for a dedicated
  record/definition-node pass (the batch-34 meta-phase or a follow-up harvester/layer-intro dispatch):
  it should get `rank:` + a `depends-on` edge to its `state-stratification` classification basis and
  `reference` edges to its use-sites, with the rank judged against its consumers. (No DAG node
  currently carries a typed `depends-on: concepts/counter-update` edge in an `edges:` block, so the
  deferral introduces no live rank-violation or orphaning meanwhile.)
- **`chebyshev-iteration` confirmed non-node** (matches the §5 borderline ratification:
  pre-redirect literature-background page with no authoritative L_n forward — `L2/chebyshev-iteration`
  and `L3/chebyshev` are the *operator* homes; this concept page is the literature-background narrative,
  not their definition home). Authored as non-node `reference`-only. Its in-body `cg slice` /
  `multigrid slice` / `lanczos-spectral-estimate` mentions are forward-looking prose with no live
  target, correctly omitted from edges.
- **Detritus-count rise (156→170) is expected, not a regression** (detailed under "Linter before/after"):
  the 14 newly-typed non-node pages join the same `[garbage?]` disposition the existing
  `concepts/{dot,nrm2,scal,apply_linop,axpy}` reference-only pages already hold — a non-node carries no
  liveness by construction. Flagging so the critic/integrator does not read the detritus delta as
  newly-orphaned nodes.
