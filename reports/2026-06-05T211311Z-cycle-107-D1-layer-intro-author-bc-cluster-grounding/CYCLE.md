---
agent: layer-intro-author
invoked_at: 2026-06-05T211311Z
scope: cycle-107 D1 — WAVE-3 reachability follow-up; GROUND the firm-but-absorbed BC-elimination + divfree clusters from the feature-spine roots (the dofset / set_subvector_zero rescue)
status: pending
integrated_at: 2026-06-05T223500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row D1). 3 honestly-typed, citation-grounded (critic-verified faithful) grounding depends-on edges landed per the NEW 2026-06-05 grounding directive — fe_assemble->absorbed-post-composition->eliminate_bc; eigenmode.L4->constrains-eigvec->L3/divfree-projector; L3/divfree-projector->uses->{L1/set_subvector_zero, concepts/set_subvector_zero}; all pre-existing reference: entries preserved. reachable 88->95 (+7 nodes rescued), 0 regressions, rank_violations HELD 0, build EXIT 0. Resolved OQs bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue + set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink grounded-and-rescued; the WAVE-3 record-rescue tranche is COMPLETE. The L1/divfree-projector enumeration discrepancy (did NOT flip — pre-scheme L2/divfree-projector dead-ends the L2->L1 mark-sweep) routed to batch-34 OQ lowering-chain-liveness-not-propagated-to-l1-ops; L4-L3/bc-elimination-post-composition-dissolution flipped in its place so the headline +7/-7 is exactly correct. No finalize build-repair."
---

# CYCLE: ground the BC-elimination + divfree absorbed clusters (dofset / set_subvector_zero rescue)

## Summary

The cycle-106 WAVE-3 pass typed `L4/eliminate_bc → uses-record → concepts/dofset`, but `dofset`
stayed GC-garbage because `eliminate_bc` itself had no root-reachable inbound edge. The coupled
`set_subvector_zero` cluster had the same shape (its consumer `L3/divfree-projector` was itself
garbage). Under the **NEW user directive (2026-06-05)** — when the reachability-GC surfaces an
unreachable node that is a genuine (future-or-absorbed) dependency of a goal node, **ground it**
with an honestly-typed `depends-on` edge rather than deleting it or filing it as detritus — I
verified both clusters ARE real absorbed dependencies of reachable feature-spine roots, and
authored **three frontmatter-only grounding edges** (disposition **path (a)**, the PREFERRED option):

1. **BC-elimination leg.** `L4/fe_assemble → depends-on (kind: absorbed-post-composition) →
   L4/eliminate_bc`. The `models/`-level operator construction that `fe_assemble` stands in for at
   the driver-column altitude **interleaves the BC-elimination into the assembled operator** —
   verified at `laplaceoperator.cpp:216-217` (`SetEssentialTrueDofs(...DIAG_ONE)` inside
   `GetStiffnessMatrix`) + `:252` (`EliminateRHS` in `GetExcitationVector`) and
   `modeeigensolver.cpp:571,574,608,611` (`EliminateBC` inside `BuildSystemMatrixA/B`). All 6 driver
   columns reach `fe_assemble`, so this single edge transitively grounds `eliminate_bc` + `dofset`.

2. **Divfree leg.** `feature/eigenmode.L4 → depends-on (kind: constrains-eigvec) →
   L3/divfree-projector`, plus `L3/divfree-projector → depends-on (kind: uses) →
   {L1/set_subvector_zero, concepts/set_subvector_zero}`. The eigenmode driver genuinely wires the
   divergence-free projector into the eigensolver (`eigensolver.cpp:233` `SetDivFreeProjector`,
   `:262` `divfree->Mult(v0)`); the projector's step-2 essential-BC zeroing IS the
   `set_subvector_zero` primitive (`divfree.cpp:171-174`). This grounds the whole divfree chain
   (`L3 → L2 → L1`) + the `set_subvector_zero` cluster.

**Measured rescue (transient apply → linter → revert; book/ left pristine):** `reachable from roots
88 → 95` (+7), `detritus 156 → 149` (−7), `rank_violations 0 → 0` (HELD), `untyped 76 → 76` (HELD;
frontmatter-only, no new untyped nodes). The 7 rescued nodes: `L4/eliminate_bc`, `concepts/dofset`,
`L3/divfree-projector`, `L2/divfree-projector`, `L1/divfree-projector`, `L1/set_subvector_zero`,
`concepts/set_subvector_zero`. Both carried OQs resolve **grounded-and-rescued**.

This is NOT a false `composes` edge and NOT a reversal of the separability law: the book's claim is
"BC-elimination is NOT part of the *fold*" (the algebraic term-fold), and that stands — the grounding
edge `kind: absorbed-post-composition` honestly names the *separate post-composition* the
operator-construction absorbs, NOT a fold step. The `reference` edge `eliminate_bc → fe_assemble`
(post-composition pipeline-position) stays as-is; the new grounding edge runs the other direction
(`fe_assemble → eliminate_bc`) and carries liveness, which is the faithful reading: the column that
depends on `fe_assemble`'s constructed operator ALSO depends on the BC-elimination baked into that
construction.

## Verification — the absorbed-construction relationship is REAL (not fabricated)

**BC leg — `laplaceoperator.cpp` (`GetStiffnessMatrix` + `GetExcitationVector`, read this dispatch):**
- `:216` `auto K_l = std::make_unique<ParOperator>(std::move(k_vec[l]), h1_fespace_l);`
- `:217` `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE);` —
  the operator-side BC pin recorded INSIDE the stiffness-matrix construction, per multigrid level.
- `:252` `PtAP_K->EliminateRHS(X, RHS);` — the RHS-side lift, inside `GetExcitationVector`.
  The electrostatic column's stage-1 down-link is `electrostaticsolver.cpp:30 GetStiffnessMatrix()` —
  i.e. it composes exactly the construction that absorbs the pin.

**BC leg — `modeeigensolver.cpp` (`BuildSystemMatrixA/B`, read this dispatch):**
- `:571` `Ar->EliminateBC(dbc_tdof_list, Operator::DIAG_ONE);` and `:574`
  `Ai->EliminateBC(dbc_tdof_list, Operator::DIAG_ZERO);` — inside `BuildSystemMatrixA`.
- `:608` `Br->EliminateBC(dbc_tdof_list, Operator::DIAG_ZERO);` and `:611`
  `Bi->EliminateBC(...DIAG_ZERO);` — inside `BuildSystemMatrixB`.
  The eigenmode column's stage-1 assembles the `(K,C,M)` pencil — exactly these constructions.

Confirmed: no `Eliminate*` call sits in `drivers/` directly (the planner's audit); the elimination is
buried inside the `models/`-level operator construction the L4 `fe_assemble` represents. So
`fe_assemble → eliminate_bc` is the faithful grounding host (the columns abstract over `fe_assemble`'s
constructed operator, which carries the absorbed BC-elimination), NOT a column→eliminate_bc edge (which
the planner correctly rejected as a non-existent column-visible composition stage).

**Divfree leg — `eigensolver.cpp` (read via codemap this dispatch):**
- `:222-233` `std::unique_ptr<DivFreeSolver<ComplexVector>> divfree; … divfree = make_unique<…>(…);
  eigen->SetDivFreeProjector(*divfree);` — the eigenmode driver builds + wires the divfree projector
  into the eigensolver.
- `:262` `divfree->Mult(v0);` — the projector applied to the initial starting vector `v0` to keep it divergence-free.
  The eigenmode column already names this in prose (`eigenmode.L4.md:52`: "the … divergence-free-projector
  configuration (→ … the `SetDivFreeProjector`)") and its evidence range `eigensolver.cpp:32-477`
  contains the setup+apply sites. So the divfree projector is a genuine directly-wired absorbed
  constituent of the eigenmode pipeline (highest entry L3; no L4 entry by the constructed-operator-gate
  verdict — `L3/divfree-projector.md` §"Upward to L4").

**Divfree step-2 zeroing — `divfree.cpp` (the set_subvector_zero use):**
- `:171-174` `SetSubVector(rhs, …, 0.0)` — the step-2 essential-BC zeroing, which `L3/divfree-projector`
  §Semantics step 2 + §Dependencies already name as the `set_subvector_zero` primitive (prose links to
  `concepts/set_subvector_zero`). The new `depends-on` to `L1/set_subvector_zero` (the firm authoritative
  operator) + `concepts/set_subvector_zero` (the cross-cutting page) types those genuine prose
  dependencies as liveness edges.

## Rank/well-foundedness check (rank_violations HELD 0)

- `L4/fe_assemble` reads rank `firm` (via `firmness: firm`); `L4/eliminate_bc` is `rank: firm`. The new
  edge is `firm → firm` → well-founded.
- `feature/eigenmode.L4` is `rank: firm`; `L3/divfree-projector` is `firmness: firm`. `firm → firm`.
- `L3/divfree-projector` (firm) → `L1/set_subvector_zero` (`rank: firm`) → `firm → firm`. → `concepts/
  set_subvector_zero` (non-node, no rank) → `firm → untyped`, tolerated exactly as the pre-existing
  `L3/divfree-projector → L2/divfree-projector` (untyped) edge is (0 violations before and after).

Linter rank source confirmed `rank:` > `firmness:` > prose `## Status` (`tools/graded-stack-lint/graded_stack_lint.py:431`).

## Before / after — `graded_stack_lint.py --show-inbound` (the MEASURABLE rescue)

**BEFORE (clean baseline, this invocation):**
```
reachable from roots: 88
RESULT: 0 rank violation(s), 156 detritus node(s), 76 untyped (warning).

  [GARBAGE*] L4/eliminate_bc            (inbound: L4-L3/bc-elimination-post-composition-dissolution only → itself garbage)
  [garbage?] concepts/dofset           (inbound: L4/eliminate_bc only → itself garbage)
  [GARBAGE*] L3/divfree-projector      (no root-reachable inbound; L2/divfree-projector <- L3 only)
  [garbage?] concepts/set_subvector_zero
  [garbage?] L1/set_subvector_zero     (inbound: L1-L0/set-subvector-zero-mutation-rotation only → garbage)
  L4/fe_assemble  <-  feature/boundary-mode.L4, feature/driven.L4, feature/eigenmode.L4,
                      feature/electrostatic.L4, feature/magnetostatic.L4, feature/transient.L4   (root-reachable)
```

**AFTER (transient apply of the 3 grounding edges):**
```
reachable from roots: 95
RESULT: 0 rank violation(s), 149 detritus node(s), 76 untyped (warning).

  L4/eliminate_bc           <-  L4/fe_assemble                       (RESCUED → reachable)
  concepts/dofset           <-  L4/eliminate_bc                      (RESCUED → reachable)
  L3/divfree-projector      <-  feature/eigenmode.L4                 (RESCUED → reachable)
  L2/divfree-projector      <-  L3/divfree-projector                 (RESCUED → reachable, transitive)
  L1/divfree-projector      <-  L2/divfree-projector                 (RESCUED → reachable, transitive)
  L1/set_subvector_zero     <-  L1-L0/set-subvector-zero-mutation-rotation, L3/divfree-projector  (RESCUED)
  concepts/set_subvector_zero  <-  L3/divfree-projector              (RESCUED → reachable)
```

Deltas: `reachable 88 → 95` (+7), `detritus 156 → 149` (−7), `rank_violations 0` (held), `untyped 76`
(held). book/ reverted to pristine after measurement (`git status --short book/` → 0 modified; the
proposed-changes blocks below are the integrator's to apply in Phase 5).

## Proposed changes

```edit:book/src/L4/fe_assemble.md
[old]:
edges:
  depends-on:
    - target: L4-L3/fe-assemble-fold-dissolution
      kind: lowers-to
  reference:
    - L4/index
    - concepts/black-box-vs-accelerated-kernels
    - concepts/state-stratification
[new]:
edges:
  depends-on:
    - target: L4-L3/fe-assemble-fold-dissolution
      kind: lowers-to
    - target: L4/eliminate_bc
      kind: absorbed-post-composition   # GROUNDING edge (c107): the models/-level operator construction `fe_assemble` stands in for INTERLEAVES the BC-elimination post-composition into the assembled operator (laplaceoperator.cpp:216-217,252; modeeigensolver.cpp:571,574,608,611). NOT a fold step (separability law 8 stands — eliminate_bc is post-composition, not part of the term fold); this edge records the genuine pipeline-altitude dependency (every driver column reaching fe_assemble's construction also reaches the absorbed BC-elimination), giving the firm-but-absorbed eliminate_bc/dofset cluster root-reachability.
  reference:
    - L4/index
    - concepts/black-box-vs-accelerated-kernels
    - concepts/state-stratification
```

```edit:book/src/feature/eigenmode.L4.md
[old]:
    - target: L4/eigsolve
      kind: composes
    - target: palace/drivers/eigensolver.cpp:32-477
      kind: cites-evidence
[new]:
    - target: L4/eigsolve
      kind: composes
    - target: L3/divfree-projector
      kind: constrains-eigvec           # GROUNDING edge (c107): the eigenmode driver wires the divergence-free projector into the eigensolver (`eigen->SetDivFreeProjector(*divfree)` eigensolver.cpp:233; the initial starting vector projected `divfree->Mult(v0)` :262) to keep eigenvectors in the divergence-free subspace — a genuine directly-wired absorbed constituent of this pipeline (highest entry L3; no L4 entry by the constructed-operator-gate verdict). Grounds the firm-but-absorbed divfree-projector cluster (and its step-2 set_subvector_zero) from this root.
    - target: palace/drivers/eigensolver.cpp:32-477
      kind: cites-evidence
```

```edit:book/src/L3/divfree-projector.md
[old]:
edges:
  depends-on:
    - target: L2/divfree-projector
      kind: lowers-to
  reference:
    - L2-L1/divfree-projector-leaf-identity
[new]:
edges:
  depends-on:
    - target: L2/divfree-projector
      kind: lowers-to
    - target: L1/set_subvector_zero
      kind: uses                        # GROUNDING edge (c107): step-2 essential-BC zeroing `Z_{bdr_eff}(rhs)` IS the set_subvector_zero primitive (divfree.cpp:171-174; §Semantics step 2). The firm L1 operator is the authoritative home; this depends-on gives the firm-but-absorbed set_subvector_zero cluster root-reachability via this (now-grounded) projector.
    - target: concepts/set_subvector_zero
      kind: uses                        # the cross-cutting concept page for the same step-2 primitive (the §Dependencies prose pointer, now a typed liveness edge).
  reference:
    - L2-L1/divfree-projector-leaf-identity
```

## Supporting evidence

- **Linter:** `tools/graded-stack-lint/graded_stack_lint.py` (rank check + reachability GC). Before/after
  pasted above; transient apply→measure→`git checkout` revert, book/ confirmed pristine.
- **BC-leg absorbed-construction sites** (read this dispatch): `palace/models/laplaceoperator.cpp:216-217,252`,
  `palace/models/modeeigensolver.cpp:571,574,608,611`. The book's own framing
  (`L4/fe_assemble.md:71,121`, `L4/eliminate_bc.md:40-47,163-168` separability law 8) confirms BC-elimination
  is a *separable post-composition* — which the `kind: absorbed-post-composition` edge honors (it is NOT a
  fold step; it is the post-composition the operator construction absorbs).
- **Divfree-leg wiring sites** (read this dispatch via codemap): `palace/drivers/eigensolver.cpp:222-233,262`
  (`SetDivFreeProjector` + `divfree->Mult`); `palace/linalg/divfree.cpp:171-174` (the step-2
  `SetSubVector(rhs,…,0.0)` zeroing = `set_subvector_zero`). The L3 chapter already names these in prose
  (`L3/divfree-projector.md` §Semantics step 2, §Dependencies).
- **Rank source:** `tools/graded-stack-lint/graded_stack_lint.py:431` (`rank:` > `firmness:` > prose `## Status`). All three new
  edges are firm→firm (or firm→untyped, tolerated as the pre-existing pattern).

## Open questions / caveats

- **RESOLVED `bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue`** — grounded-and-rescued via
  `fe_assemble → eliminate_bc` (absorbed-post-composition). `eliminate_bc` + `dofset` flip
  `[garbage?]`→reachable. NOT the column→eliminate_bc edge the c106 finalize first suggested (the planner
  correctly rejected that as a non-existent column-visible stage); the faithful host is `fe_assemble`,
  whose construction absorbs the BC-elimination.
- **RESOLVED `set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink`** —
  grounded-and-rescued via the divfree leg: `feature/eigenmode.L4 → L3/divfree-projector →
  {L1/set_subvector_zero, concepts/set_subvector_zero}`. The c106 D4 reference-backlink did not carry
  liveness (reference edges don't); these `depends-on` edges do. `L1/set_subvector_zero` +
  `concepts/set_subvector_zero` + the whole divfree `L3→L2→L1` chain flip reachable.
- **FOLLOW-UP (NOT rescued this dispatch; routed to batch-34 meta-phase) — the L1 BC-op tail
  (`L1/eliminate_essential_bc`, `L1/eliminate_rhs`, `L1/essential_dofs`) stays `[GARBAGE*]`.** They are
  reached by NEITHER a `depends-on` from `L4/eliminate_bc` (which only `reference`s them — correctly, since
  the L4 surface is the LIFT of them, and they are what it *lowers to*, not constituents it composes) NOR
  by their own lowering-theme inbounds (the L1>L0 BC mutation themes are themselves garbage). This is the
  **lowering-chain-incompleteness** pattern affecting nearly the whole L1/L2/L3 vocabulary in the pre-P1
  state (most L1-L0 themes are `[garbage?]` — they depend-on their endpoints but nothing depends-on them
  with liveness). Forcing `eliminate_bc → depends-on → L1 BC ops` would MISCLASSIFY a lowering relationship
  (L4-surface lowers-to L1-form) as a blocking constituent dependency — the wrong fix. The right fix is the
  systematic lowering-edge liveness typing (the WAVE-tail / P1 lowering-theme `lowers-to` depends-on pass,
  graded-stack-scheme §5 lowering rule: a theme's higher endpoint should carry a `lowers-to` depends-on TO
  the theme). Flagged for the batch-34 meta-phase as `lowering-chain-liveness-not-propagated-to-l1-ops`
  (the BC-op tail is one instance of the broad pre-P1 lowering-theme garbage cohort).
- **FOLLOW-UP (noted, not this dispatch) — `L1-L0/set-subvector-zero-mutation-rotation` stays garbage.** Its
  inbound is only from `L1/set_subvector_zero` as a `reference` edge (not `depends-on`), so the rescue of
  `L1/set_subvector_zero` does not propagate to it. Same lowering-chain-liveness pattern as the BC-op tail
  above; same batch-34 follow-up.
- **`L4/eigsolve` / `L3/eigsolve` remain pre-scheme** (`consumes:`/`lowers_to:`/`lifts_from:`, no `edges:`
  block). I deliberately did NOT migrate them this dispatch (out-of-scope WAVE-tail op-chapter migration);
  the divfree grounding routed through the eigenmode COLUMN + the L3 projector entry (both of which already
  carry `edges:` blocks) to avoid an unscoped migration. When the eigsolve chapters are migrated, the
  divfree projector edge could ALTERNATIVELY/ADDITIONALLY live on `L3/eigsolve` (the per-step `[▷ project]`
  optional projection step) — a finer-grained home; the column-level grounding here is the faithful,
  minimal version that the OWN-COMPOSITION reading already supports (the eigenmode driver genuinely owns the
  `SetDivFreeProjector` wiring). Noted for the eigsolve migration so the grounding is not duplicated.
