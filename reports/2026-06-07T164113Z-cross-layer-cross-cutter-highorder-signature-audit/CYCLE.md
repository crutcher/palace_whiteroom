---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T164113Z
scope: L4↔L3 cross-cut — high-order signature closure-grouping compliance audit (cycle-128 D2)
status: pending
integrated_at: 2026-06-07T170138Z
integration_commit: f93eaff
integration_notes: "cycle-128 D2 (batch-41 MIDDLE) read-only compliance audit; NO artifact change (no proposed-changes block); 2 OQs promoted — highorder-signature-noncompliant-cohort-c129-lifter-sweep (4 non-compliant ops -> c129 lifter) + oq-highorder-operator-transformer-codomain-convention (gates eliminate_essential_bc's c129-sweep inclusion); graded-stack no-op, all totals HELD."
---

# CYCLE: Cross-layer observation — high-order signature closure-grouping compliance

## Summary
Per the USER DIRECTIVE (2026-06-07) that the L4 calculus's closure-yielding signatures must make the
closure intent **syntactically explicit** — paren-group the closure sub-signature `foo -> (bar -> baz)`
and/or use the operator-value spelling `Op[τ_in → τ_out]` — I swept every high-order signature across
`book/src/L4/**`, `book/src/L3/**`, `book/src/L4-L3/**`, `book/src/L3-L2/**`, and the L4 feature
surfaces `book/src/feature/*.L4.md`. The discriminator that falls out of the existing semantic surface
(`book/src/semantics/index.md` §"data classification" L46/L91–L95, and the bunsen exemplars L383–L408,
L494): the **bracketed operator-value spelling** `LinOp[(R: ...), (D: ...)]` / `Op[τ_in → τ_out]` ALREADY
carries the in/out and counts as COMPLIANT, as does an explicit paren-grouped trailing closure
`(SimState -> Solve {...})`. The **NON-COMPLIANT** pattern is exactly the trigger shape: an operator/closure
codomain written as the *type-application* form `LinearOperator[N, N]` or `LinearOperator (Tensor[...])`
with a bare trailing arrow — the higher-order intent hidden in a record-applied-to-types. I found
**4 NON-COMPLIANT operator constructors** (a tight, self-consistent cohort — all the FE-assembly /
operator-transformer constructors that still use the rank-1 `LinearOperator[...]` applied spelling),
plus **1 NON-COMPLIANT closure-valued record field**. The `krylov-step` family is the COMPLIANT model.
None is a semantic-ambiguity emergency; the cohort is a clean **lifter follow-up sweep for c129**.

## Observation kind
**Edge-label / surface-fidelity drift (signature-convention non-compliance).** A cross-cutting
consistency observation: a calculus-level notation convention (closure-grouping, owned by the semantic
surface D1 is codifying this cycle) is satisfied by some high-order ops and silently violated by a
coherent cohort of operator-constructor signatures. This is the signature-convention analog of an
edge-label-fidelity mismatch — the *type* says "applied operator value" where the *intent* is "closure /
operator action".

## Specific finding

### Inventory: high-order operations swept

**Total high-order / closure-or-operator-returning ops examined: 17** (excluding the trigger).
Breakdown: **COMPLIANT 11 · NON-COMPLIANT 4 (+1 record field) · N/A (value-returning) — the remainder.**

#### COMPLIANT (closure intent already syntactically explicit)

| Op | File:line | Form | Why compliant |
|---|---|---|---|
| `krylov-step` | `book/src/L4/krylov-step.md:63` | `OpParams -> Krylov -> (SimState -> Solve {…})` | trailing closure **paren-grouped** — the canonical model |
| `first_step` / `steady_step` | `book/src/L4/krylov-step.md:69-70` | `… -> (SimState -> Solve {…})` / `… -> (PrevCarry -> SimState -> Solve {…})` | paren-grouped closure |
| `krylov-step` (theme) | `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:29,49,50` | mirrors the L4 entry | paren-grouped, faithful to the L4 surface |
| `chebyshev setup` | `book/src/L4/chebyshev.md:74` | `LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)` | constructed `ChebOp` returned inside `Solve s (…)` — explicit monadic wrap (but see borderline note + record-field non-compliance below) |
| `chebyshev apply` | `book/src/L4/chebyshev.md:75` | `ChebOp E S -> Bool -> Solve (ChebSim E) ()` | monadic action, explicit `Solve` wrap |
| `iterate_while_pure` | `book/src/L4/iterate-while.md:22` | `α -> (α -> Bool) -> (α -> α) -> α` | higher-order **arguments paren-grouped** |
| `iterate_while_with_prev` | `book/src/L4/iterate-while-with-prev.md:23,34,45` | `(α -> { state, prev })` etc. | function args paren-grouped |
| `apply_linop` | `book/src/L3/apply_linop.md:37` | `LinOp[(R: ...), (D: ...)] -> Tensor[$D] -> Tensor[$R]` | bracketed operator-value spelling in domain position; value-returning otherwise |
| `inner_product_M` | `book/src/L4/inner_product.md:85`, `book/src/L3/inner_product.md:95` | `… -> LinOp[$S, $S] -> …` | operator arg in bracketed spelling |
| `fgmres_inner_loop` / `inner_loop` | `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md:48`, `…/gmres-inner-loop-…:36` | `… -> Solve (Krylov, StopReason)` | monadic value-action, explicit `Solve` wrap |
| `preconditioning-framework` run-time prims (`solve`, `applyPreconditioner`) | `book/src/L4/preconditioning-framework.md:159-160` | `… -> Solve E (Vec E)` | monadic value-action, explicit wrap |

#### NON-COMPLIANT (operator/closure codomain in bare type-application form — hides the higher-order intent)

These are the c129 lifter-sweep targets. All four are operator **constructors / transformers** whose
codomain is an operator value but written with the rank-1 `LinearOperator[…]` applied spelling and a
bare trailing arrow — the **identical shape as the `mk_matrix_free_operator` trigger**.

| # | Op | File:line | Current signature | Recommended fix |
|---|---|---|---|---|
| 1 | `assemble_frequency_operator` | `book/src/L4/assemble_frequency_operator.md:98-99` (also restated `:293`) | `FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]` | `FrequencyOperatorFamily[N] -> Scalar -> Op[Tensor[$N] → Tensor[$N]]` (or the bracketed `LinOp[(N: ...), $N]` square-operator spelling). The op CONSTRUCTS the per-ω system operator `A(ω)` — codomain is an operator value, not a tensor. |
| 2 | `fe_assemble` | `book/src/L4/fe_assemble.md:60` | `FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]` | `FiniteElementSpace[N] -> [WeakFormTerm] -> Op[Tensor[$N] → Tensor[$N]]` / `LinOp[(N: ...), $N]`. The assemble-fold's product IS the assembled operator. |
| 3 | `assemble_term` (the libCEED black-box leaf, named in `fe_assemble`) | `book/src/L4/fe_assemble.md:35,71` | `FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N,N]` | `… -> Op[Tensor[$N] → Tensor[$N]]`. Even as an opaque-surface input it is an operator-VALUED leaf — the closure spelling makes the opacity-as-operator explicit. |
| 4 | `eliminate_essential_bc` | `book/src/L4/eliminate_bc.md:83-84` | `LinOp[(S: ...), $S] -> DofSet[N] -> DiagPolicy -> LinOp[$S, $S]` | **Borderline-compliant** — the codomain `LinOp[$S, $S]` IS the bracketed operator-value spelling, so by the strict discriminator this is already COMPLIANT. Flagged here only because it is an operator-TRANSFORMER (operator-in → operator-out) and the convention author may want operator-transformer codomains explicitly `Op[…]`-or-paren-grouped for symmetry with `mk_matrix_free_operator`. **Adjudication call (see Open questions).** |

#### NON-COMPLIANT record field (closure-valued field in bare-arrow form)

| Op | File:line | Field | Note |
|---|---|---|---|
| `FrequencyOperatorFamily.A2` | `book/src/L4/assemble_frequency_operator.md:106` | `A2 : Scalar -> LinearOperator[N, N]` | A genuinely closure-valued record field (the prose even calls it "closure over ω"). Same applied-spelling issue: recommend `A2 : Scalar -> Op[Tensor[$N] → Tensor[$N]]`. Bundles naturally with fix #1 (same chapter). |
| `ChebOp.scalars` | `book/src/L4/chebyshev.md:70` | `scalars: (Int, S) -> { … }` | Already paren-tupled arg + record return — **COMPLIANT** as a closure field (listed for completeness; no fix). |

#### Excluded
- **`mk_matrix_free_operator`** (`book/src/L4/mk_matrix_free_operator.md:60`) — the named trigger
  (`… -> LinearOperator (Tensor[(N: ...)])`), **fixed by D1 this cycle**. Its sibling feature surface
  `book/src/feature/matrix-free-operator.L4.md:54` carries the identical signature and should be fixed
  **in lockstep with D1's chapter fix** (it is the same op's feature-surface mirror, not a fresh finding —
  flagging it so D1/integrator keeps the two in sync).

#### N/A (genuinely value-returning at their layer — no closure/operator codomain)
`ksp_solve` / `eigsolve` / `fold_solve` / `solve_family` (all `… -> SimState`/`EigState`/`[SimState]` — value-returning solve drivers; the opaque per-step *bodies* `eigen_iterate`/`time_step_op`/`apply_shift_invert` are role-named function args, already bare-but-positional and not closure-CONSTRUCTORS); `domain_energy_reduce` / `gram_reduce` / `eigenfreq_qfactor_reduce` / `sparameter_reduce` / `waveguide_mode_reduce` / `inner_product` / `nrm2` / `dot` (reduce-to-value); `frequency_sweep` (`… -> [SimState]`); `buildKspSolver` / `setOperators` (`… -> BaseKspSolver E` — return a **record handle**, not a closure); all L3 `(args) -> result` positional-value forms (`chebyshev`, `eigsolve`, `krylov-step`, `ksp_solve`, `linear_combination`).

## Recommendation
**Dispatch a `lifter` follow-up sweep in c129** to re-write the NON-COMPLIANT cohort (#1 `assemble_frequency_operator`
incl. the `A2` field, #2 `fe_assemble`, #3 `assemble_term`) into the paren-grouped / `Op[…]` form, once D1's
`book/src/semantics/index.md` convention text lands and `mk_matrix_free_operator` is fixed (so the sweep can
cite the now-authoritative convention + the fixed exemplar as the template). The cohort is tight (3 ops + 1
field, 2 chapters: `assemble_frequency_operator.md`, `fe_assemble.md`) and mechanically uniform — a single
lifter dispatch covers it. Keep the `feature/matrix-free-operator.L4.md:54` mirror in sync with D1's
`mk_matrix_free_operator` fix (route that to D1/integrator, NOT the c129 sweep — it's the trigger's mirror).

**Sweep-scope EXTENSION — the `L4/index.md` dep-map MIRROR rows + the in-chapter prose instance (added post-critique).**
The chapter signature blocks are NOT the only carrier of the non-compliant applied-spelling: the
`book/src/L4/index.md` dep-map mirrors the same cohort ops, and `assemble_frequency_operator.md` restates the
`A2` field in prose. A c129 sweep that rewrites only the chapter signature lines would leave the dep-map drifted
(and would leave `eliminate_bc` internally inconsistent between chapter and index). The c129 lifter MUST therefore
ALSO sweep these surfaces, in the SAME cohort:
- **`book/src/L4/index.md:61`** — the `eliminate_essential_bc :: LinearOperator[N,N] -> LinearOperator[N,N]` dep-map
  MIRROR row. This is the **internal-inconsistency reconcile**: the chapter (`eliminate_bc.md:83-84`) uses the
  bracketed `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]` form (adjudicated borderline-COMPLIANT, #4), but the index
  row uses the bare applied-spelling — so the SAME op is spelled compliantly in its chapter and non-compliantly in
  its index. The sweep must bring the index row into agreement with whatever form #4's adjudication settles on
  (the operator-transformer-codomain convention call, `oq-highorder-operator-transformer-codomain-convention`).
- **`book/src/L4/index.md:62`** — the `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N,N]`
  dep-map MIRROR row (the index mirror of finding #3 / the `fe_assemble` chapter row).
- **`book/src/L4/index.md:119`** — the `mk_matrix_free_operator :: ... -> LinearOperator (Tensor[(N: ...)])` dep-map
  MIRROR row of the trigger. Like the `feature/matrix-free-operator.L4.md:54` mirror, this one rides with D1's
  `mk_matrix_free_operator` fix (route to D1/integrator, NOT the c129 cohort sweep — it's the trigger's index mirror).
- **`book/src/L4/assemble_frequency_operator.md:127`** — `fam.A2 — Scalar -> LinearOperator[N, N]`, a THIRD in-chapter
  instance of the `A2` closure field, this one in the shape-contract PROSE (beyond the `:106` record-field finding
  and the `:293` signature restatement). Folds into the "rewrite all instances in the chapter" guidance for fix #1.

**No same-cycle surgical fix warranted.** None of the non-compliances is a semantic-ambiguity emergency —
each codomain unambiguously denotes an operator value in context (the prose says so); the defect is purely
that the *type spelling* under-advertises the higher-order intent. Style/fidelity, not correctness — the
c129 batched sweep is the right cadence.

**Defer one item to the convention author/human:** the operator-transformer adjudication (#4
`eliminate_essential_bc` + the general question of whether bracketed `LinOp[d, r]` codomains count as
"already compliant" or should additionally be `Op[…]`-spelled). See Open questions.

## Supporting evidence
- Convention home (D1's target + the discriminator source): `book/src/semantics/index.md:46` (`Op[τ_in → τ_out]` spelling), `:91-95` (`LinOp[(R: ...), (D: ...)]` operator-value spelling + the rank-1 `LinearOperator[M,N]` faithful-at-L1/L0 carve-out), `:383-408` + `:494` (bunsen operator-constructor exemplars `Bgk :: !LbmTables → Scalar → Op[…]`, `lbm_step :: Op[…] -> Op[…] -> Op[…]`).
- Trigger (fixed by D1): `book/src/L4/mk_matrix_free_operator.md:60`; mirror `book/src/feature/matrix-free-operator.L4.md:54`.
- COMPLIANT model: `book/src/L4/krylov-step.md:63,69-70`; mirrored `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:29,49,50`.
- NON-COMPLIANT cohort: `book/src/L4/assemble_frequency_operator.md:98-99,106,293`; `book/src/L4/fe_assemble.md:35,60,71`; `book/src/L4/eliminate_bc.md:83-84` (borderline).

## Open questions / caveats
- **`oq-highorder-operator-transformer-codomain-convention` (adjudication for the convention author / human):**
  Does a codomain written in the bracketed operator-value spelling `LinOp[(S: ...), $S]` / `Op[τ_in → τ_out]`
  ALREADY satisfy the closure-grouping convention (my working assumption — it carries the in/out, so YES),
  or does the directive want operator-CONSTRUCTOR / operator-TRANSFORMER codomains *additionally* paren-grouped
  for emphasis even when bracketed? The answer decides whether `eliminate_essential_bc` (#4) is in-scope for the
  c129 sweep and whether the recommended fixes #1–#3 should target `Op[Tensor[$N] → Tensor[$N]]` (explicit
  arrow inside brackets) vs. the square-operator `LinOp[(N: ...), $N]` spelling. D1 (the convention author)
  should pin this in `semantics/index.md`; I have assumed bracketed-is-compliant + recommended the explicit
  `Op[… → …]` arrow form as the clearer fix.
- **Borderline — opaque-leaf `assemble_term` (#3):** it is an *opaque black-box-kernel input* (libCEED-owned),
  not a Palace-authored constructor. The closure-spelling fix still applies (it is operator-VALUED), but a
  reviewer may judge the bare-arrow form acceptable for an explicitly-opaque leaf. Low-stakes; bundle with the
  sweep, let the lifter/critic confirm.
- **Sync risk:** `feature/matrix-free-operator.L4.md:54` duplicates the trigger signature. If D1 fixes only
  the L4 chapter, the feature mirror drifts. Verify both land in the same cycle.
- I did NOT re-verify the underlying Palace constructs via codemap — the audit is purely about the *book's*
  signature spelling against the convention, which is a within-artifact notation question (the L0 anchors are
  already cited in the chapters and out of scope for a closure-spelling audit).
