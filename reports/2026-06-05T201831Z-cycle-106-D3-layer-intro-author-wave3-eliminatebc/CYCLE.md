---
agent: layer-intro-author
invoked_at: 2026-06-05T20:18:31Z
scope: cycle-106 D3 — WAVE-3 op-chapter typed-edge migration (eliminate_bc) + item-3b stale-prose fix (same file)
status: integrated
integrated_at: 2026-06-05T223000Z
integration_commit: 7592988
integration_notes: "cycle-106 D3, applied clean. L4/eliminate_bc migrated to typed edges + DofSet record-home prose retargeted concepts/DofSet.md→concepts/dofset.md (stale record-DofSet-needs-definition-home flag dropped). FAITHFUL-PATH-OR-FINDING: dofset STAYS unreachable (no feature column links to eliminate_bc); D3 declined to force an unfaithful column→eliminate_bc edge, routed OQ bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue (THE ONE CARRIED FOLLOW-UP). Build EXIT 0; rank_violations 0; full frontmatter parses clean under strict YAML (no variant_axes colon artifact)."
---

# CYCLE: L4/eliminate_bc — WAVE-3 typed-edge migration + DofSet record-page prose retarget

## Summary

Two coupled edits to `book/src/L4/eliminate_bc.md` (single file; no new operator algebra — `eliminate_bc` is already `firm`):

1. **Typed-edge migration (§(f) WAVE-3).** Fold the chapter's pre-scheme frontmatter — `consumes:` + `lowers_to:` + the partial pre-scheme `depends_on:` list — into ONE scheme `edges:` block (block-mapping form, §(e)/scheme §2/§6), and ADD the `uses-record` `depends-on` → `concepts/dofset`. Add the matching `rank: firm` token.
2. **Item-3b stale-prose fix (COUPLED, same file).** The §Record-definition prose (line 126) says the concept page `book/src/concepts/DofSet.md` "does **not yet exist**" and flags `record-DofSet-needs-definition-home`. The page DOES exist now — `book/src/concepts/dofset.md`, `rank: firm` (read on-disk; defines the record schema). Retarget the prose to point at the existing page and drop the stale not-yet-exist / needs-dispatch flag.

**Faithful-path-or-finding outcome (the c104-D2 discipline):** the `uses-record`→`dofset` edge is now correctly typed and **IS GC-traversed** by the linter (it appears in `--show-inbound` for `concepts/dofset`), but it does **NOT** rescue `dofset` standalone — because `eliminate_bc` is itself `[GARBAGE*]` (no feature column links to it). §(f) adds NO column→eliminate_bc edge, and I did **not** force an unfaithful one. The BC-driver-column→eliminate_bc edge gap is routed as a **FINDING** in §Open questions below (a producer/meta judgment, not a forced edge).

## Proposed changes

### Edit 1 — frontmatter: fold pre-scheme blocks into one typed `edges:` block + `rank:` + `uses-record`→dofset

```edit:book/src/L4/eliminate_bc.md
[old]:
---
layer: L4
operator: eliminate_bc
firmness: firm
consumes:
  - book/src/L4/fe_assemble.md (the assemble-fold combinator this post-composes AFTER)
  - book/src/L4/linear_combination.md (the RHS-side b − K·x_bc data-algebra verb)
  - book/src/concepts/state-stratification.md (DofSet[N] / DiagPolicy the readonly BC stratum)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (the post-composition verb-pair rises regardless)
lowers_to:
  - book/src/L4-L3/bc-elimination-post-composition-dissolution.md
depends_on:
  - book/src/L4/fe_assemble.md (reference — post-composes after; an edge to the assemble combinator it sits beside, not a blocking fold dependency)
  - book/src/L4/linear_combination.md (depends-on — the RHS-side b − K·x_bc is one linear_combination)
variant_axes:
  - diagonal-policy
  - trial-test-coincidence
  - bc-data-homogeneity
---

[new]:
---
layer: L4
operator: eliminate_bc
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/linear_combination
      kind: folds                 # the RHS-side b − K·x_bc is one linear_combination [(1,b),(-1,y)] (firm c068)
    - target: L1/apply_linop
      kind: folds                 # the operator action K·x_bc = apply_linop K (restrict_essential x_bc) in the RHS lift
    - target: concepts/dofset
      kind: uses-record           # the DofSet[N] essential-true-dof index set the verb-pair consumes (the readonly BC stratum)
    - target: L4-L3/bc-elimination-post-composition-dissolution
      kind: lowers-to             # the substantive L4>L3 dissolution theme this surface lowers through
  reference:
    - L4/fe_assemble              # post-composes AFTER the assemble fold (pipeline-position see-also), NOT a blocking fold dependency — separability law 8
    - L1/essential_dofs           # cross-ref: the producer of the DofSet[N] operand (post-assembly cohort feeder, NOT a construction input)
    - concepts/state-stratification              # the (DofSet[N], DiagPolicy) readonly BC stratum
    - concepts/black-box-vs-accelerated-kernels  # the BC-application verb-pair rises as a feature-surface verb regardless
    - concepts/constructed-operators             # the eliminated K is a constructed operator
variant_axes:
  - diagonal-policy
  - trial-test-coincidence
  - bc-data-homogeneity
---
```

### Edit 2 — §Record-definition prose: retarget to the existing `concepts/dofset.md`, drop the stale not-yet-exist / needs-dispatch flag

```edit:book/src/L4/eliminate_bc.md
[old]:
`DofSet[N]` — the essential (Dirichlet) true-dof index set the BC verb-pair consumes — has **≥2
consumers** (`eliminate_essential_bc`, `eliminate_rhs`, and the upstream firm-L1
[`essential_dofs`](../L1/essential_dofs.md) producer) and so is a **cross-cutting record**: its
definition home is NOT this chapter (per the record-definition obligation, ≥2 consumers ⇒ a
`concepts/<record>.md` page, not an in-chapter section). `DofSet[N]` is currently described only by use
across the three L1/L4 entries; the concept page `book/src/concepts/DofSet.md` does **not yet exist**.
Flagged for dispatch as `record-DofSet-needs-definition-home` (see §Open questions in the dispatch
report). Pending that page, the working description: `DofSet[N]` is an immutable index set over the
true-dof axis `N` of a finite-element [`fe_space`](../L1/fe_space.md), a subset of `0..N`; its L0
backing is the `mfem::Array<int> dbc_tdof_list` recorded by `SetEssentialTrueDofs`
(`palace/linalg/rap.cpp:45-46`) and built by `essential_dofs` (`palace/fem/multigrid.hpp:99-100`).

[new]:
`DofSet[N]` — the essential (Dirichlet) true-dof index set the BC verb-pair consumes — has **≥2
consumers** (`eliminate_essential_bc`, `eliminate_rhs`, and the upstream firm-L1
[`essential_dofs`](../L1/essential_dofs.md) producer) and so is a **cross-cutting record**: its
definition home is NOT this chapter (per the record-definition obligation, ≥2 consumers ⇒ a
`concepts/<record>.md` page, not an in-chapter section). That cross-cutting home is the concept page
[`DofSet`](../concepts/dofset.md) (`book/src/concepts/dofset.md`, `rank: firm`), which defines the
record schema — the `indices : Set<TrueDofIndex>` field, its construction-time readonly stratum, and
its L0 backing. See that page for the full record definition; the working description here:
`DofSet[N]` is an immutable index set over the
true-dof axis `N` of a finite-element [`fe_space`](../L1/fe_space.md), a subset of `0..N`; its L0
backing is the `mfem::Array<int> dbc_tdof_list` recorded by `SetEssentialTrueDofs`
(`palace/linalg/rap.cpp:45-46`) and built by `essential_dofs` (`palace/fem/multigrid.hpp:99-100`).
```

## Supporting evidence

### Scheme conformance (§(e) / graded-stack-scheme.md §2/§6)

- **`rank: firm`** matches the on-disk `firmness: firm` + the chapter's `## Status` line `firm` (read directly; the firm-on-positive-structure escape, lines 333–363). Scheme §1 maps `firm → rank: firm`.
- **Block-mapping edge form** (`- target: …` / `  kind: …`) used per §(e) — the batch-33 linter fix GC-traverses it (confirmed below: `concepts/dofset <- L4/eliminate_bc` now appears in `--show-inbound`).
- **Edge classification (deliberate, the typing pass IS the audit):**
  - `L4/linear_combination` → **depends-on** (`folds`). Prose §Dependencies (line 270–271) + the RHS-side signature body (line 84) confirm the blocking data-algebra dependency. firm c068 — rank invariant holds (firm rests on firm).
  - `L1/apply_linop` → **depends-on** (`folds`). The operator action `K·x_bc = apply_linop K (restrict_essential x_bc)` in the RHS lift (signature body line 83; prose §Dependencies line 272–273 lists it as a consumed verb, NOT flagged reference). firm L1 — rank invariant holds.
  - `concepts/dofset` → **depends-on** (`uses-record`). The NEW §(f) edge: the `DofSet[N]` essential-true-dof index set the verb-pair consumes opaquely. firm record node — rank invariant holds.
  - `L4-L3/bc-elimination-post-composition-dissolution` → **depends-on** (`lowers-to`). Subsumes the pre-scheme `lowers_to:` per scheme §4(a)/§5: a lowering edge is a `depends-on` on both endpoints. The theme's own rank is `min(endpoints)` (the lowering-verifier rule); both endpoints firm.
  - `L4/fe_assemble` → **reference**. The pre-scheme `depends_on:` block already classified it `reference` (line 13: "post-composes after; not a blocking fold dependency"); the prose §Dependencies (line 266–269) + separability law 8 confirm `eliminate_bc` consumes `K` as an opaque assembled `LinearOperator[N,N]`, not `fe_assemble`'s term-list machinery. Correctly `reference`.
  - `L1/essential_dofs` → **reference**. The §Dependencies "Cross-refs (produces/operates-on, NOT dependencies)" block (line 288–292): `essential_dofs` PRODUCES the `DofSet[N]` operand; it is the post-assembly cohort feeder, NOT a construction input `eliminate_bc` blocks on. Correctly `reference`.
  - `concepts/state-stratification`, `concepts/black-box-vs-accelerated-kernels`, `concepts/constructed-operators` → **reference** (the three "L4 concept references" in §Dependencies, lines 278–286 — navigational concept pointers, not blocking).

### Pre/post-edit linter run (`tools/graded-stack-lint/graded_stack_lint.py --show-inbound`)

Edit applied to disk, linter run, then **reverted** (dispatch-phase write-authority: `book/` mutation belongs to integrator-per-report, not this dispatch; the edit is emitted only as the proposed-changes blocks above — `git checkout -- book/src/L4/eliminate_bc.md` confirmed clean).

**Post-edit `--show-inbound` for the two nodes in scope (verbatim):**

```
    [GARBAGE*] L4/eliminate_bc
    [garbage?] concepts/dofset
  L1/apply_linop  <-  L1/assemble_frequency_operator, L1/bilinear-form, L1/eigsolve, L1/matrix-weighted-norm, L2/eigsolve, L2/inner_product, L3/apply_linop, L4/eliminate_bc
  L4-L3/bc-elimination-post-composition-dissolution  <-  L4/eliminate_bc
  L4/linear_combination  <-  L3/linear_combination, L4/assemble_frequency_operator, L4/eliminate_bc
  concepts/dofset  <-  L4/eliminate_bc
```

**The `dofset` inbound line (the requested paste):**

```
  concepts/dofset  <-  L4/eliminate_bc
```

- The `uses-record`→`dofset` edge **IS** now traversed (it appears as an inbound edge — the batch-33 linter block-mapping-edge fix works). All four `depends-on` edges from `eliminate_bc` show as inbound on their targets (`linear_combination`, `apply_linop`, `dofset`, the dissolution theme).
- `RANK VIOLATIONS: none` (firm rests on firm for all four `depends-on` edges).
- **`reachable from roots: 81` — UNCHANGED from pre-edit (was 81).** `concepts/dofset` stays `[garbage?]` and `L4/eliminate_bc` stays `[GARBAGE*]`. This is the expected faithful-path-or-finding outcome (see §Open questions): the rescue is blocked upstream by the absence of a column→eliminate_bc edge, which §(f) deliberately did NOT add.

## Open questions / caveats

### FINDING (routed, not forced): the BC-driver-column → `eliminate_bc` edge gap blocks the `dofset` rescue

`oq: bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue`

`concepts/dofset` is named in NO feature-column signature; it is the internal record shape of the L4 BC-application operator `eliminate_bc`. The faithful reachability path is therefore `column →(composes) eliminate_bc →(uses-record) dofset` — exactly the WAVE-3 `column → op → record` shape. This dispatch installed the **second half** of that path (`eliminate_bc →(uses-record) dofset`, now GC-traversed). But the **first half** (`column →(composes) eliminate_bc`) does not exist: `eliminate_bc` is `[GARBAGE*]` — no feature column links to it. So `dofset` is NOT rescued this cycle, and `reachable from roots` holds at 81.

Per §(f)'s explicit instruction, I did **not** force an unfaithful `column→eliminate_bc` edge. The plausibility call (which column, and whether faithful) belongs to a producer/meta judgment:

- **The plausibly-faithful candidates are the electrostatic + magnetostatic driver columns** (and, where applicable, eigenmode — the eigenmode witness `modeeigensolver.cpp:571,574,608,611` and the electrostatic witness `laplaceoperator.cpp:217,252` are exactly `eliminate_bc`'s two cited specialization call-sites). These conforming-FE driver columns DO eliminate-then-solve: they call `eliminate_essential_bc` / `eliminate_rhs` on the assembled `(K, b)` AFTER `fe_assemble` and BEFORE the solve (the standard pipeline `eliminate_rhs (eliminate_essential_bc (fe_assemble …) …) …` then `ksp_solve`, law 8 / electrostatic specialization). A `feature/electrostatic.L4 →(composes) L4/eliminate_bc` `depends-on` edge (and the magnetostatic/eigenmode analogs) is therefore plausibly faithful — and would simultaneously rescue `eliminate_bc`, `dofset`, AND (transitively) the firm L1 `eliminate_essential_bc` / `eliminate_rhs` / `essential_dofs` (all currently `[GARBAGE*]`), since they hang below `eliminate_bc`.
- **But that call is a producer/meta judgment, not a forced edge from this dispatch.** The driver columns are feature-surface chapters whose `composes:`/`edges:` blocks list their stage-(2) constituents; whether `eliminate_bc` belongs in that list (vs. being absorbed into the assemble/solve stage as an implementation detail of those columns) is a column-authoring decision. The down-link is also read-only from a feature chapter's side. **Recommend dispatching a WAVE-3-followup that adds the `feature/{electrostatic,magnetostatic,eigenmode}.L4 →(composes/depends-on) L4/eliminate_bc` edges** (the driver columns already carry `→ fe_assemble` depends-on edges per the pre-edit `--show-inbound`: `L4/fe_assemble <- … feature/electrostatic.L4, feature/magnetostatic.L4, feature/eigenmode.L4 …`, so adding the sibling `→ eliminate_bc` edge is the natural same-shape completion). That followup would make the rescue MEASURABLE (`reachable from roots` rises; `eliminate_bc` + `dofset` + the three firm L1 BC entries flip off `[GARBAGE*]`).

### Caveats

- The `## Open questions` cross-reference in the OLD §Record-definition prose ("see §Open questions in the dispatch report" + the `record-DofSet-needs-definition-home` flag) is removed by Edit 2 because the obligation is now MET (the page exists, `rank: firm`). No residual dangling flag remains in the chapter.
- I did not touch `fe_assemble.md` (still pre-scheme `consumes:`/`lowers_to:` — out of this dispatch's single-file scope; a future WAVE-3 tranche migrates it). The `L4/fe_assemble` reference edge in `eliminate_bc`'s new block resolves to the existing file regardless of `fe_assemble`'s own frontmatter state.
- Single-file scope honored: both edits are to `book/src/L4/eliminate_bc.md`; no other chapter touched (the `concepts/dofset.md` page is only READ, to confirm it exists at `rank: firm` and to cite its schema in the retargeted prose — not edited).
