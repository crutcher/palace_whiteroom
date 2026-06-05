---
agent: layer-intro-author
invoked_at: 2026-06-05T072449Z
scope: L4 index §Vocabulary-cohort — 2 missing firm bullets (preconditioning-framework, eliminate_bc)
status: pending
integrated_at: 2026-06-05T085500Z
integration_commit: e9e6556d1fe709b77124731573eafa7a638c7497
integration_notes: >
  Applied clean (cycle-103 D8, staging row 8 — the FINAL per-report, staging COMPLETE).
  2 §Vocabulary-cohort prose bullets inserted into L4/index.md (eliminate_bc before fe_assemble;
  preconditioning-framework before solve_family) — mid-file prose region, byte-disjoint from D5's
  frontmatter edges: block on lines 1-11. Closes OQ
  vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc (the c102 follow-up).
  overall_status: ready set by the repairer (the lone edge-label-fidelity WARNING was repaired
  in-report — the cosmetic "between A and B" placement gloss rewritten to anchor-based phrasing;
  the two edit: blocks preserved unchanged). Build green; all 13 cross-links resolve; citecheck
  4 ok / 0 failing. step-5b rank_violations: 0 (no rank/depends-on authored, vacuous).
---

# CYCLE: L4 §Vocabulary-cohort missing firm bullets

## Summary

Cycle-103 D8 (WAVE 2, content tail 2c). The L4 firm-count header was corrected c102 (21 + 4
outer-driver), but two firm chapters lack their dedicated §Vocabulary-cohort PROSE bullets — the
count-owner-vs-landing-dispatch split left them lagging:

1. `eliminate_bc` (firmed c101 D1) — the post-assembly boundary-condition application surface.
2. `preconditioning-framework` (firmed c096 D1) — the L4 preconditioning-framework cap (the
   construction-and-binding shell one outside `ksp_solve`).

This report adds both bullets to the **Firm at L4** cohort list in `book/src/L4/index.md`, each in
ALPHA-within-cohort position (directive-3), matching the existing bullets' style (chapter link +
one-line role with the cohort's standard cross-references). Resolves OQ
`vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc`.

**Scope discipline:** edits touch ONLY the mid-file §Vocabulary-cohort PROSE bullets. The frontmatter
`edges:` block (D5, WAVE 1, separate report) and the firm-count header (correct at 21+4 from c102)
are NOT touched — disjoint regions of the same file; the serial integrator applies both.

## Proposed changes

`eliminate_bc` alpha-slot: inserted immediately before the existing `fe_assemble` bullet (line 48),
preserving the alpha relation `eliminate_bc` < `fe_assemble`. Anchored on the unique opening of the
`fe_assemble` bullet. (The cohort list is in the documented transitional mixed alpha/chronological
order, so the on-disk predecessor of the insertion is the `solve_family` bullet at line 47, not the
full-alpha left-neighbor; the anchor-based placement honors `eliminate_bc` < `fe_assemble` locally and
applies unambiguously regardless of the surrounding list order.)

```edit:book/src/L4/index.md
[old]: - [`fe_assemble`](./fe_assemble.md) — the **assemble-fold combinator**: capture the FE space once (`readonly`), fold an immutable weak-form-term list `[WeakFormTerm]` by the opaque per-term leaf `assemble_term`, and **sum** the contributions into the global operator `K = Σ_t assemble_term(space, t)`.
[new]: - [`eliminate_bc`](./eliminate_bc.md) — the **post-assembly boundary-condition application surface**: the separable post-composition verb-pair `(eliminate_essential_bc, eliminate_rhs)` over a shared `(DofSet[N], DiagPolicy)` vocabulary that pins essential (Dirichlet) dofs into an assembled operator (`eliminate_essential_bc :: LinearOperator[N,N] -> LinearOperator[N,N]`, zero the essential rows/cols + set the eliminated diagonal per policy) and lifts the inhomogeneous Dirichlet data into the RHS (`eliminate_rhs :: ... -> Tensor[N]`, subtract `K·x_bc` from `b` + pin the essential rows). Both compose **AFTER** the [`fe_assemble`](./fe_assemble.md) fold on the *already-assembled* operator value — the **separable post-composition** framing that is explicitly NOT a law of `fe_assemble` (`fe_assemble.md` §Algebraic-laws "BC-elimination is NOT part of the fold"); they consume the `DofSet[N]` produced by [`essential_dofs`](../L1/essential_dofs.md) (the post-assembly cohort feeder, NOT a `fe_assemble` construction input). The **assemble-half-completing companion** of [`fe_assemble`](./fe_assemble.md): where `fe_assemble` builds `K`, `eliminate_bc` applies the Dirichlet BC to the `(K, b)` pair before the [`ksp_solve`](./ksp_solve.md) / [`eigsolve`](./eigsolve.md) solve-coordination shells drive it. The RHS-side `b − K·x_bc` is one [`linear_combination`](./linear_combination.md). Status `firm` (firm-on-positive-structure escape — lifts the two firm L1 law-sets unchanged; closed the one genuine in-scope L4 hole from the c100 completeness survey, OQ `bc-elimination-cohort-l4-disposition` resolved on route (a)). Lowers to the L3 global tensor-field view via [`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md). Harvested + firmed cycle-101 D1 — the BC-elimination cohort cap.
[new]: - [`fe_assemble`](./fe_assemble.md) — the **assemble-fold combinator**: capture the FE space once (`readonly`), fold an immutable weak-form-term list `[WeakFormTerm]` by the opaque per-term leaf `assemble_term`, and **sum** the contributions into the global operator `K = Σ_t assemble_term(space, t)`.
```

`preconditioning-framework` alpha-slot: inserted immediately before the existing `solve_family` bullet
(line 47), preserving the alpha relation `nrm2` < `preconditioning-framework` < `solve_family`.
Anchored on the unique opening of the `solve_family` bullet. (The cohort list is in the documented
transitional mixed alpha/chronological order, so the on-disk predecessor of the insertion is the
`frequency_sweep` bullet at line 46, not the full-alpha left-neighbor `nrm2`; the anchor-based
placement honors `preconditioning-framework` < `solve_family` locally and applies unambiguously
regardless of the surrounding list order.)

```edit:book/src/L4/index.md
[old]: - [`solve_family`](./solve_family.md) — the fixed-operator **map-over-RHS-family outer-driver combinator**: capture the system operator once (`SetOperators(*K,*K)` hoisted outside the loop), build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over a family of right-hand sides `[rhs_i]`, collect the solution family `[x_i]`.
[new]: - [`preconditioning-framework`](./preconditioning-framework.md) — the L4 **composition-and-binding framework** one shell outside the [`ksp_solve`](./ksp_solve.md) cap: the `buildKspSolver` constructor that assembles the `(ksp, pc)` pair via constructed-operator factories and the `setOperators` bind that holds the capability-typed two-operator `(op, pc_op)` binding the cap iterates against. The L4 home of Palace's `BaseKspSolver` framework — the type at which build-time composition and run-time iteration are **stratified** ([`state-stratification`](../concepts/state-stratification.md): `buildKspSolver`/`setOperators` cannot appear inside the monadic body), the `(op, pc_op)` role distinction is **capability-typed** (`TrueOp<E>` / `PcAssemblyOp<E>` brands — this chapter is [`capability-typing`](../concepts/capability-typing.md)'s canonical L4 use site), and the `finestLevelUnwrap` structural adapter is hoisted into a `pcBoundOp` **derived view** ([`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). Where `ksp_solve` is the outer-driver *coordination* that folds [`krylov-step`](./krylov-step.md) to convergence, `preconditioning-framework` is the **non-iteration construction surface** that builds and binds the operator graph the solve runs against. Status `firm` (firm-on-positive-structure escape over the positive `BaseKspSolver` source `palace/linalg/ksp.cpp:276-293` + the firm `ksp_solve` cap). Harvested + firmed cycle-096 D1 — the framework one shell outside the cap.
[new]: - [`solve_family`](./solve_family.md) — the fixed-operator **map-over-RHS-family outer-driver combinator**: capture the system operator once (`SetOperators(*K,*K)` hoisted outside the loop), build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over a family of right-hand sides `[rhs_i]`, collect the solution family `[x_i]`.
```

## Supporting evidence

- Firm chapters surveyed at their on-disk `## Status` / frontmatter (c057-meta guard — read the file,
  not the index cell):
  - `book/src/L4/eliminate_bc.md` — frontmatter `firmness: firm`; body §intro confirms the
    `(eliminate_essential_bc, eliminate_rhs)` verb-pair, the separable-post-composition framing, the
    `essential_dofs` feeder, the `fe_assemble` assemble-half-completing companion role, and the
    `bc-elimination-post-composition-dissolution` L4>L3 lowering (`eliminate_bc.md:1-40`).
  - `book/src/L4/preconditioning-framework.md` — frontmatter `firmness: firm` / `rank: firm`; body
    §intro + §Context confirm the `buildKspSolver`/`setOperators` construction-and-binding surface,
    the three rotations (build/run stratification, capability-typed `(op, pc_op)`, `finestLevelUnwrap`
    derived-view hoist), and the `ksp.cpp:276-293` evidence cite
    (`preconditioning-framework.md:1-69`).
- Both bullet links resolve to existing chapters (`./eliminate_bc.md`, `./preconditioning-framework.md`)
  and the cross-referenced anchors (`./fe_assemble.md`, `./ksp_solve.md`, `./eigsolve.md`,
  `./krylov-step.md`, `../L1/essential_dofs.md`, `../L1/linear_combination.md` via `./linear_combination.md`,
  `../L4-L3/bc-elimination-post-composition-dissolution.md`, the four concept pages) — all are firm
  on-disk targets already linked elsewhere in this same index, so `linkcheck2` build-safe.
- Alpha-within-cohort placement (directive-3): full alpha order of the firm set with the two new
  members is `assemble_frequency_operator, chebyshev, dot, domain_energy_reduce,
  eigenfreq_qfactor_reduce, eigsolve, eliminate_bc, fe_assemble, fold_solve, frequency_sweep,
  inner_product, iterate-while, iterate-while-with-prev, krylov-step, ksp_solve, linear_combination,
  nrm2, preconditioning-framework, solve_family` (a HYPOTHETICAL fully-sorted sequence, NOT the on-disk
  order). In that full-alpha order `eliminate_bc` would sit immediately before `fe_assemble` and
  `preconditioning-framework` immediately before `solve_family` — and the insertions DO honor exactly
  those two local alpha relations (`eliminate_bc` < `fe_assemble`; `nrm2` < `preconditioning-framework`
  < `solve_family`). But the on-disk cohort list is in the documented transitional mixed
  alpha/chronological state pending the one-time reorg, so the REALIZED on-disk predecessors of the two
  insertions are `solve_family` (line 47, before `fe_assemble`) and `frequency_sweep` (line 46, before
  `solve_family`) respectively — NOT the full-alpha left-neighbors. The insertions are anchor-defined
  (immediately before the named on-disk bullet) and apply unambiguously regardless of the surrounding
  list order; new rows go in alpha-local position per the directive-3 insertion rule.

## Open questions / caveats

- The cohort list as a whole is NOT yet fully alpha-sorted (transitional mixed alpha/chronological
  state — the one-time directive-3 reorg of the L4 firm cohort into alpha order is meta-phase-owned
  and not in this dispatch's scope). These two insertions are placed alpha-LOCALLY against their named
  on-disk neighbors, consistent with the "new entry goes in alpha position within its cohort" rule;
  they do not attempt the global re-sort.
- `book/src/L4-L3/bc-elimination-post-composition-dissolution.md` is referenced in the `eliminate_bc`
  bullet (and in `eliminate_bc.md`'s own `lowers_to:` frontmatter). It is assumed firm/existing on
  disk (the `eliminate_bc` chapter firmed c101 with its lowering); if the integrator finds it
  missing-on-disk, defang that single link to plain text per the rough-in-link convention. (Not
  expected — it is a c101-landed companion theme.)
