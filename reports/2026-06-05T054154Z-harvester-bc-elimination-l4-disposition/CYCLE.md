---
agent: harvester
invoked_at: 2026-06-05T054154Z
scope: L4 operator: eliminate_bc (BC-elimination cohort L4 disposition)
status: integrated
integrated_at: 2026-06-05T070000Z
integration_commit: f7f6e58
integration_notes: "Applied clean (staging row 1, cycle-101). eliminate_bc PROMOTED FIRM L4 + bc-elimination-post-composition-dissolution LANDED FIRM L4>L3 (tally 10->11); essential_dofs mis-attribution at L4/fe_assemble.md:69/status/147/175 corrected; c069 BC-deferral re-anchored to the firm cap; 2 SUMMARY entries + 4 discretionary alpha-position-insert corrections (append-after-sibling -> alpha-within-cohort per directive-3) + a tally full-paragraph replace. Step-5b rank_violations 0 (both new firm nodes rest on firm deps); cargo make book EXIT 0; citecheck on touched files clean except 2 PRE-EXISTING out-of-scope basename flags on untouched lines. 2 OQs opened (record-DofSet-needs-definition-home, eliminate-rhs-mutation-rotation L1>L0 leg). Closes the BC-elimination cohort L4 hole; the in-scope stack is now substantially L4-complete for backend-lowering."
inputs:
  - book/src/L1/eliminate_essential_bc.md (firm L1; the operator-side BC pin)
  - book/src/L1/eliminate_rhs.md (firm L1; the RHS-side Dirichlet-data lift)
  - book/src/L1/essential_dofs.md (firm L1; produces DofSet[N], the post-assembly BC cohort feeder)
  - book/src/L4/fe_assemble.md:69,119,147,175 (c069 deferral + essential_dofs mis-attribution sites)
  - book/src/L4-L3/fe-assemble-fold-dissolution.md:127 (c069 deferral site)
  - book/src/L4/index.md:48,100 (c100 partial fix — re-verified clean)
  - OQ bc-elimination-cohort-l4-disposition
  - reference/palace/palace/linalg/rap.cpp:36-47,56-83,139-148 (EliminateBC / SetEssentialTrueDofs / EliminateRHS, codemap-verified this dispatch)
---

# CYCLE: Formalize eliminate_bc at L4 (BC-elimination cohort L4 disposition)

## Summary

Warrant-first L4 disposition of the BC-elimination cohort — the one genuine in-scope L4 hole
from the cycle-100 completeness survey. The cohort is the two firm-L1 **separable post-compositions**
[`eliminate_essential_bc`](../../book/src/L1/eliminate_essential_bc.md) (operator-side BC pin) and
[`eliminate_rhs`](../../book/src/L1/eliminate_rhs.md) (RHS-side inhomogeneous-Dirichlet lift), fed by
the firm-L1 [`essential_dofs`](../../book/src/L1/essential_dofs.md) (produces `DofSet[N]`). All three
are firm at L1; none had an L2/L3/L4 entry; the L4 disposition was deferred-but-undecided per the c069
sibling-deferral (`L4/fe_assemble.md:119`, `L4-L3/fe-assemble-fold-dissolution.md:127`).

**VERDICT: Route (a) — the cohort lifts cleanly to L4 as a small post-assembly combinator pair.**
The two L1 entries both positively establish (with full source) that BC elimination is a *separable
post-composition on the assembled operator value* — defined purely on `(K, dofs, policy)` / `(K, x_bc,
b, policy)`, independent of HOW `K` was assembled, with read-off syntactic-identity laws (idempotence,
free-block preservation, DIAG_ZERO-distribution-over-the-assembly-fold for the operator-side; affine-
on-interior, homogeneous-BC-identity for the RHS-side). That is exactly the `fe_assemble`/`solve_family`
shape: an abstraction the backend wants as a clean BC-application verb-pair, with no irreducible in-place
index-masking that resists post-composition. I author **one L4 chapter** `eliminate_bc.md` homing BOTH
verbs as the two co-equal halves of the post-assembly BC-application surface (the way `fe_assemble`
homes the assemble fold), plus the L4>L3 dissolution theme `bc-elimination-post-composition-dissolution`.

Coupled fixes (consistent with route (a)): the three `essential_dofs` mis-attribution sites in
`L4/fe_assemble.md` (`:69,:147,:175` — `essential_dofs` was wrongly listed inside `fe_assemble`'s
absorbed *construction* stratum; it actually produces the `DofSet[N]` that feeds THIS post-assembly
cohort) are corrected; the c069 deferral prose at `L4/fe_assemble.md:119` +
`L4-L3/fe-assemble-fold-dissolution.md:127` is re-anchored from "deferred to c069 / open" to the now-firm
`eliminate_bc` cap. The `L4/index.md:48,:100` parentheticals (already corrected c100 — `essential_dofs`
NOT a `fe_assemble` input) are re-read and confirmed clean (no edit owed there beyond the OQ-pointer
update from "open" to the firm cap).

`DofSet[N]` has ≥2 consumers (`eliminate_essential_bc`, `eliminate_rhs`, now the L4 `eliminate_bc` cap)
and no definition home → flagged `record-DofSet-needs-definition-home` in Open questions (judge: flag,
do not author the concept page this cycle).

## Disposition reasoning (warrant-first; route (a) vs route (b))

Route (b) — no-L4-by-design — would be warranted only if BC elimination were an irreducible in-place
index-masking op with no abstraction value at L4 (the FE-space-constituent disposition at
`L4/index.md:48`). It is NOT:

1. **It is a clean separable post-composition, positively established at L1.** Both L1 entries are firm
   and both state the post-composition framing as a load-bearing law:
   `eliminate_essential_bc(fe_assemble(space, terms), E, policy)` is a well-formed composition for ANY
   assembled `K` (`L1/eliminate_essential_bc.md:99-109`); `eliminate_rhs` "consumes the *already-
   assembled* operator `K` and is independent of HOW `K` was assembled" (`L1/eliminate_rhs.md:142-150`).
   It composes AFTER the `fe_assemble` fold, not inside it (`L1/fe_assemble.md` law-list "BC-elimination
   is NOT part of the fold", cited at `L1/eliminate_rhs.md:262-264`).

2. **The laws are read-off syntactic identities** (the firm-on-positive-structure escape, the
   `fe_assemble`/`apply_linop` precedent): operator-side idempotence, free-block preservation,
   policy-determines-only-the-essential-diagonal, and DIAG_ZERO-distribution (the elimination is the
   linear free-block projection `K ↦ P_F K P_F` under DIAG_ZERO — `L1/eliminate_essential_bc.md:148-159`);
   RHS-side affine-on-interior linearity, linearity-in-boundary-data, homogeneous-BC interior identity
   (`L1/eliminate_rhs.md:120-150`). These lift to L4 vocabulary unchanged.

3. **Abstraction value at L4 = a backend-lowering verb the backend wants.** L4 is the outward backend-
   lowering target (directive-1, `project_l4_is_backend_lowering_target`); a backend assembling FE
   operators wants the BC-application surface as a clean verb-pair `(eliminate_essential_bc,
   eliminate_rhs)` it can place AFTER its assemble engine, not the unfolded `SetEssentialTrueDofs`-record-
   then-`EliminateBC`-apply two-step / the pooled-scratch in-place `EliminateRHS` loop. This is the same
   warrant that rose `fe_assemble`, `linear_combination`, `inner_product` — the FE/BLAS-1 verbs the
   backend wants — to L4 regardless.

4. **Cross-pipeline recurrence** (the disciplined-cross-pipeline-combinator-mining-gate bar): ≥2 positive
   witnesses, structurally identical — electrostatic (`laplaceoperator.cpp:217` SetEssentialTrueDofs +
   `:252` EliminateRHS) and the eigen pipeline (`modeeigensolver.cpp:571,574,608,611` EliminateBC across
   the A/B blocks, exercising BOTH diagonal policies). No break-witness. The verb-pair is the entry; the
   per-pipeline call-sites are specialization notes.

**One chapter, two verbs (not two thin mirror chapters, not a single merged combinator).** The two
operators are genuinely distinct algebraically — `eliminate_essential_bc :: ... -> LinearOperator[N,N]`
(operator-side) vs `eliminate_rhs :: ... -> Tensor[N]` (RHS-side) — so they are NOT one combinator with
one as a specialization. But they are a *coherent post-composition pair* sharing the same `DofSet[N]` /
`DiagPolicy` vocabulary and the same "apply Dirichlet BC after assembly" surface; Palace applies them
together as the two halves of one BC treatment (operator pin + RHS lift). Homing both in one L4 chapter
`eliminate_bc` (the BC-application post-composition surface), with each verb as a co-equal half, is the
right granularity — it presents the surface coherently and avoids two near-duplicate thin chapters
(the anti-mirror principle). The canonical dispatch slug `book/src/L4/eliminate_bc.md` matches.

**Definition is in L4 vocabulary** (high→low discipline): the chapter defines the two verbs in terms of
operator block-decomposition on the free/essential dof partition, the free-block projection `P_F`, the
`apply_linop`/`linear_combination` data-algebra verbs (for the RHS-side `b − K·x_bc`), and the post-
composition-with-`fe_assemble` framing — NOT in terms of L3 value-threading. The L4>L3 dissolution theme
narrates the rewrite into the L3 deferred-config-then-apply / in-place-RHS-mutation forms.

## Proposed changes

```new:book/src/L4/eliminate_bc.md
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

# eliminate_bc

The L4 **post-assembly boundary-condition application surface**: the pair of separable
post-compositions that pin essential (Dirichlet) dofs into an assembled operator and lift the
inhomogeneous Dirichlet data into the right-hand side. Two co-equal verbs over the same
`(DofSet[N], DiagPolicy)` vocabulary:

- `eliminate_essential_bc` — the **operator-side** pin: `LinearOperator[N,N] -> LinearOperator[N,N]`,
  zero the essential rows/cols of `K` and set the eliminated diagonal per policy.
- `eliminate_rhs` — the **RHS-side** lift: `... -> Tensor[N]`, subtract the boundary-data forcing
  `K·x_bc` from `b` and pin the essential rows per policy.

Both compose **AFTER** the [`fe_assemble`](./fe_assemble.md) fold — they consume the *already-assembled*
operator value and are independent of HOW it was assembled (the **separable post-composition** framing
that is explicitly NOT a law of `fe_assemble`, `fe_assemble.md` §Algebraic-laws "BC-elimination is NOT
part of the fold"). They consume the `DofSet[N]` produced by [`essential_dofs`](../L1/essential_dofs.md)
— the post-assembly cohort feeder, NOT a `fe_assemble` construction input. This chapter is the
**assemble-half-completing companion** to `fe_assemble`: where `fe_assemble` builds `K`, `eliminate_bc`
applies the Dirichlet boundary condition to the `(K, b)` pair before the
[`ksp_solve`](./ksp_solve.md) / [`eigsolve`](./eigsolve.md) solve-coordination shells drive it.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch sites,
and effect placement structural (`L4/index.md:7-13`). `eliminate_bc` is the **BC-application half** of
the deliverable's L4 assemble surface — the verb-pair every conforming-FE solver pipeline calls after
[`fe_assemble`](./fe_assemble.md) builds the system operator and before the solve. It is the L4 lift of
the two firm L1 separable post-compositions [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
and [`eliminate_rhs`](../L1/eliminate_rhs.md) (both firm, cycle-053/firm-on-positive-structure), pulled
up as the answer to the cycle-100 completeness survey's one genuine in-scope L4 hole (OQ
`bc-elimination-cohort-l4-disposition`).

The combinator is defined **in L4 vocabulary** (high→low discipline, CLAUDE.md §Methodology invariants):
its semantics, signatures, and laws are stated in terms of the free/essential dof partition block-
decomposition, the free-block projection `P_F`, the data-algebra verbs ([`linear_combination`](./linear_combination.md)
for the RHS-side `b − K·x_bc`), the post-composition-with-`fe_assemble` framing, and the
[`state-stratification`](../concepts/state-stratification.md) `readonly` BC stratum (`DofSet[N]` +
`DiagPolicy` captured at construction) — NOT in terms of L3 value-threading or L0 in-place mutation.
The L4>L3 dissolution (the post-composition pair collapsing to Palace's deferred-config-then-apply
operator pin + the in-place pooled-scratch RHS mutation) is the substantive
[`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)
theme, narrated forward L4→L3; it is **not** authored here.

`eliminate_bc` at L4 is a **methodology-level surface** distilled from the BC-application machinery
Palace shares across the conforming-FE pipelines (electrostatic + eigenmode witnesses), not a single
Palace-source artefact — there is no single L0 range that "is" the L4 `eliminate_bc`. The Palace
evidence is the two firm L1 operators + the `ParOperator` BC L0 home (`palace/linalg/rap.cpp:36-83`,
`:139-148`) + the witness call-sites (§Specializations); L4 names the post-composition verb-pair and
the `readonly` BC-stratum the call-sites share.

## Signature

The pair, both post-composing after `fe_assemble` on the assembled `K`:

    -- operator-side: pin the essential dofs into the assembled square operator
    eliminate_essential_bc :: LinearOperator[N, N] -> DofSet[N] -> DiagPolicy
                              -> LinearOperator[N, N]

    -- RHS-side: lift the inhomogeneous Dirichlet data into the right-hand side
    eliminate_rhs :: LinearOperator[N, N] -> Tensor[N] -> Tensor[N] -> DiagPolicy
                     -> Tensor[N]
    eliminate_rhs K x_bc b policy =
      let y    = apply_linop K (restrict_essential x_bc)          -- K · Eₑ(x_bc)
          b'   = linear_combination [(1, b), (-1, y)]             -- b − K·x_bc
          pin  = case policy of DIAG_ONE -> x_bc ; DIAG_ZERO -> zeros
      in  set_essential b' pin                                    -- BC rows ← pin

Shape contract (bunsen-style; named axes; the BC stratum per [`state-stratification`](../concepts/state-stratification.md)):

- `K` — `LinearOperator[N, N]` — the assembled **square** operator over the true-dof axis `N`, the
  output of [`fe_assemble`](./fe_assemble.md). `readonly`; squareness is required (BC elimination is
  defined only for `height == width`; the rectangular case is a hard L0 reject — the
  `trial-test-coincidence` variant axis). The operator-side result decomposes block-wise on the
  free/essential partition `F = 0..N \ E`, `E = dofs`:

      eliminate_essential_bc K E policy =
        [ K[F,F]   0   ]      D = I_E   (policy = DIAG_ONE)
        [ 0        D   ]      D = 0_E   (policy = DIAG_ZERO)

- `dofs : DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N`; the
  `DofSet[N]` produced by [`essential_dofs`](../L1/essential_dofs.md) (the firm boundary-attribute →
  essential-true-dof construction). Part of the `readonly` BC stratum captured at construction.
- `policy : DiagPolicy` — `DIAG_ONE | DIAG_ZERO` (the diagonal-policy variant axis). The only two
  admissible values; MFEM's third policy `DIAG_KEEP` is out-of-axis (excluded at the `ParOperator`
  boundary).
- `x_bc : Tensor[N]` — (RHS-side only) the essential boundary data; a true-dof vector prescribing the
  Dirichlet value on essential dofs, masked-out elsewhere. Only the essential entries are read
  (`restrict_essential`). `readonly`.
- `b : Tensor[N]` — (RHS-side only) the right-hand-side vector to adjust. `readonly` at L4 (the L4 form
  returns a fresh value; the in-place `b.Add` is an L3-and-below concern).
- result — operator-side `LinearOperator[N, N]` (the eliminated operator); RHS-side `Tensor[N]` (the
  adjusted RHS `b − K·x_bc` with essential rows pinned per policy).

`restrict_essential` / `set_essential` are the essential-dof gather/scatter masking projections onto
the essential-dof subspace (the general `set_subvector` write-mask, whose zeroing arm is the
`set_subvector_zero` [`divfree-projector`](../L1/divfree-projector.md) §Dependencies names); they are
masking projections over `DofSet[N]`, not separate spine verbs.

## Record definition

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
`DiagPolicy` is the two-valued `DIAG_ONE | DIAG_ZERO` enum (L0 `Operator::DiagonalPolicy`, guarded to
exactly these two at the `ParOperator` boundary, `palace/linalg/rap.cpp:39-41`); single-use-shaped here
(named by both verbs in THIS chapter), it is defined inline as that two-valued enum.

## Semantics

`eliminate_bc` is the **post-assembly Dirichlet BC application**, the two halves of which act on the
assembled `(K, b)` pair:

1. **`eliminate_essential_bc K E policy`** — decouple the essential dofs in the operator: zero every
   matrix entry in an essential row or column, then set each essential diagonal `(i,i), i ∈ E` to `1`
   (`DIAG_ONE`) or `0` (`DIAG_ZERO`). Free–free entries are unchanged. Under `DIAG_ZERO` this is the
   linear free-block projection `K ↦ P_F K P_F` (`P_F` the diagonal 0/1 free-dof projector); under
   `DIAG_ONE` it is that projection plus the constant `I_E` on the essential block (affine).

2. **`eliminate_rhs K x_bc b policy`** — lift the inhomogeneous Dirichlet forcing into the RHS in three
   data-algebra steps: apply the unconstrained operator to the boundary-data extension
   (`y = K · Eₑ(x_bc)`, one [`apply_linop`](../L1/apply_linop.md)); subtract it from `b`
   (`b − y`, one [`linear_combination`](./linear_combination.md) `[(1,b),(-1,y)]`); pin the essential
   rows to the boundary data (`DIAG_ONE`) or zero (`DIAG_ZERO`). The pinned system is consistent: the
   essential equations become `1·xᵢ = (x_bc)ᵢ` / `1·xᵢ = 0`, matching the essential-row diagonal the
   operator-side pin installed.

Both are **separable post-compositions**: defined purely on the assembled-operator value (plus the BC
stratum / boundary data), they do not inspect how `K` was assembled. For any
`K = fe_assemble space terms`, both `eliminate_essential_bc K E policy` and `eliminate_rhs K x_bc b
policy` are well-formed compositions valid after the fold — this is the framing that makes them
*post-compositions* rather than fold steps (the `fe_assemble` §Algebraic-laws "BC-elimination is NOT
part of the fold").

The verbs are **pure** at L4: no deferred-config wrapper, no apply-at-assemble-time staging, no in-place
operator/RHS mutation, no pooled scratch. The L0 `SetEssentialTrueDofs`-record-then-`EliminateBC`-apply
two-step (`palace/linalg/rap.cpp:36-47` record; `:139-148` apply), the `ParOperator` mutable wrapper,
and the in-place pooled-scratch `EliminateRHS` loop (`:56-83`) are all L4>L3 lowering concerns.

Per [`state-stratification`](../concepts/state-stratification.md), the `(DofSet[N], DiagPolicy)` pair is
the **`readonly` BC stratum** captured once at construction (the L4 typing of the `ParOperator`'s
recorded `dbc_tdof_list` + `diag_policy`); the assembled `K`, the boundary data `x_bc`, and the RHS `b`
are the per-call operands. The verbs introduce no monadic effect — they are plain value-producing
functions (the `apply_linop` / `linear_combination` data-algebra, not a `Solve` action).

## Algebraic laws

The laws are the L4-vocabulary statements of the firm L1 laws
(`L1/eliminate_essential_bc.md:126-172`, `L1/eliminate_rhs.md:112-162`), lifted to the L4 surface. They
hold treating `K` as an opaque assembled square operator and the masks as fixed projections over
`DofSet[N]`. Absences are catalogued to prevent decoration drift.

**Operator-side (`eliminate_essential_bc`):**

1. **Idempotence.** `eliminate_essential_bc (eliminate_essential_bc K E policy) E policy =
   eliminate_essential_bc K E policy`. After elimination the essential rows/cols are already zero and
   the diagonal already equals the policy value; re-eliminating the same `(E, policy)` is the identity.
2. **Free-block preservation.** `(eliminate_essential_bc K E policy)[F,F] = K[F,F]` for `F = 0..N \ E`.
   The elimination touches only essential rows/cols; the interior physics is preserved exactly — what
   licenses solving the reduced free-dof system.
3. **Policy determines only the essential diagonal.** `eliminate_essential_bc K E DIAG_ONE` and
   `eliminate_essential_bc K E DIAG_ZERO` differ *only* on the essential–essential diagonal (identity
   vs zero on `E`); all other entries are identical.
4. **DIAG_ZERO distribution over the assembly fold (the separability law).**
   `eliminate_essential_bc (K₁ + K₂) E DIAG_ZERO = eliminate_essential_bc K₁ E DIAG_ZERO +
   eliminate_essential_bc K₂ E DIAG_ZERO`. With `DIAG_ZERO` the elimination is the **linear** free-block
   projection `K ↦ P_F K P_F`, so it distributes over operator addition — hence over the `fe_assemble`
   term-sum (`fe_assemble` law 1, the concatenation-homomorphism). Under `DIAG_ONE` the `I_E` is added
   once (affine, not linear): `eliminate_essential_bc (K₁ + K₂) E DIAG_ONE = eliminate_essential_bc K₁
   E DIAG_ONE + eliminate_essential_bc K₂ E DIAG_ZERO`. This is the precise sense in which the
   elimination factors through the free-block projection regardless of the term decomposition — the
   post-composition is separable from assembly.

**RHS-side (`eliminate_rhs`):**

5. **Affine-on-interior linearity in `b`** (homogeneous BC fixed). On the interior dofs the map is
   affine in `b` with unit gradient — `Iₑ̄ · eliminate_rhs K x_bc b policy = Iₑ̄·b − Iₑ̄·K·Eₑ(x_bc)`;
   the essential block is constant in `b` (overwritten by the pin), so the full map is affine-on-
   interior + constant-on-essential, **not** linear as a whole.
6. **Linearity in the boundary data** (interior block). The forcing correction `−K·Eₑ(x_bc)` is
   `apply_linop ∘ Eₑ` applied to `x_bc`, both linear, so the interior correction is linear in `x_bc`.
7. **Homogeneous-BC interior identity.** When `x_bc = 0` on essential dofs, `K·Eₑ(0) = 0`, so
   `eliminate_rhs K 0 b policy = b` on the interior (and pinned on essential) — a no-op on the interior
   for homogeneous Dirichlet data (the `bc-data-homogeneity` variant axis).

**Cohort-level (the load-bearing post-composition framing):**

8. **Separable post-composition with `fe_assemble`.** Both verbs consume the *already-assembled* `K`
   and are valid for any `K`, post-composing AFTER the [`fe_assemble`](./fe_assemble.md) fold — NOT
   inside it. The standard electrostatic pipeline is
   `eliminate_rhs (eliminate_essential_bc (fe_assemble h1_space [diffusion ε]) E DIAG_ONE) x_bc 0
   DIAG_ONE` then `ksp_solve`. This is the cohort-side statement of `fe_assemble` §Algebraic-laws
   "BC-elimination is NOT part of the fold".

Laws that explicitly **do not** hold:

- **Operator-side not the identity** (non-empty `E`): elimination changes `K` whenever an essential
  row/col has a nonzero entry. The empty-dof-set case is the only identity
  (`eliminate_essential_bc K ∅ policy = K`).
- **No SPD / invertibility guarantee.** `DIAG_ZERO` leaves a zero block on `E` (singular by
  construction, rank ≤ `|F|`); only `DIAG_ONE` makes the essential block non-singular. Neither verb
  carries an SPD/invertibility postcondition. `eliminate_rhs` applies `K` opaquely — no symmetry or
  definiteness requirement.
- **RHS-side not linear in `b` as a whole map** (the essential-row pin overwrites, breaking linearity;
  recovered only on the interior, law 5) and **not idempotent** (applying `eliminate_rhs` twice
  subtracts `K·x_bc` twice on the interior — a one-shot RHS preparation, not a projector).
- **`eliminate_rhs` does NOT distribute over the assembly fold.** Unlike the operator-side DIAG_ZERO
  law 4, `eliminate_rhs (K₁ + K₂) ...` is NOT `eliminate_rhs K₁ ... + eliminate_rhs K₂ ...` (the pin
  and `b` would be applied/carried twice). The correct statement is law 8 — a post-composition valid
  for any `K`, not a per-term distribution.
- **Policy-commutativity does NOT hold** for either verb (the two policies are distinct maps for
  non-empty `E`).

## Specializations

Per replace-and-propagate, `eliminate_bc` is the **entry**; the Palace witness call-sites are
**specialization notes re-expressing THROUGH it**, not separate rectangular leaf chapters:

- **Electrostatic** (`palace/models/laplaceoperator.cpp`). Operator-side: per multigrid level,
  `K_l = ParOperator(...)` (`:216`) + `SetEssentialTrueDofs(dbc_tdof_lists[l], DIAG_ONE)` (`:217`) —
  `eliminate_essential_bc K E DIAG_ONE` on each level's stiffness. RHS-side:
  `GetExcitationVector` projects a unit Dirichlet value to the terminal boundary, restricts to true
  dofs `X`, then `PtAP_K->EliminateRHS(X, RHS)` (`:252`) — `eliminate_rhs K x_bc=X b=0 DIAG_ONE`, the
  inhomogeneous lift.
- **Eigenmode** (`palace/models/modeeigensolver.cpp`). `Ar->EliminateBC` / `Ai->EliminateBC` (real/imag
  stiffness blocks) + `Br->EliminateBC` / `Bi->EliminateBC` (real/imag mass blocks) at `:571,574,608,
  611` — `eliminate_essential_bc` across the generalized-EVP A/B blocks, exercising **both** diagonal
  policies: the real-stiffness block `Ar` (`:571`) uses the solve-side `DIAG_ONE`; the imaginary-stiffness
  block `Ai` (`:574`) and both mass blocks `Br`/`Bi` (`:608,611`) use the energy-block `DIAG_ZERO`.

Both witnesses instantiate the same `(K, DofSet[N], DiagPolicy)` post-composition shape; they differ
only in the diagonal policy and which assembled operator they post-compose, which is absorbed into the
operands — they do not shape the verb-pair.

## Dependencies

L4 rows / vocabulary this surface consumes:

- [`fe_assemble`](./fe_assemble.md) (**reference**) — the assemble-fold combinator `eliminate_bc`
  post-composes AFTER. This is a navigational see-also (the pipeline-position relationship), NOT a
  blocking fold dependency: `eliminate_bc` consumes `K` as an opaque assembled `LinearOperator[N,N]`,
  not `fe_assemble`'s term-list machinery (the separability law 8). Edge classified `reference`.
- [`linear_combination`](./linear_combination.md) (**depends-on**) — the RHS-side `b − K·x_bc` is one
  `linear_combination [(1,b),(-1,y)]` (firm c068; the rank invariant holds — firm rests on firm).
- [`apply_linop`](../L1/apply_linop.md) — the operator action `K·x_bc` in the RHS-side lift (the firm
  L1 operator-action verb; the assembled operator applied opaquely).
- `set_subvector` / essential-dof mask (concept, NOT a spine verb) — `restrict_essential` /
  `set_essential` over `DofSet[N]`; the general `set_subvector` write-mask whose zeroing arm is
  [`set_subvector_zero`](../concepts/set_subvector_zero.md).

L4 concept references:

- [`state-stratification`](../concepts/state-stratification.md) — the `(DofSet[N], DiagPolicy)` BC
  stratum captured `readonly` at construction; the assembled `K` / `x_bc` / `b` the per-call operands.
- [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) — the BC-
  application verb-pair rises as a feature-surface verb the backend wants (§"the combinators rise
  regardless"), the disposition that warrants the L4 lift over no-L4-by-design.
- [`constructed-operators`](../concepts/constructed-operators.md) — the eliminated `K` is a constructed
  operator; the BC stratum + the assembled `K` is its construction.

**Cross-refs (produces/operates-on, NOT dependencies):** the `DofSet[N]` operand is produced by the
firm L1 [`essential_dofs`](../L1/essential_dofs.md) (`essential_dofs (space, bdr_attrs, bdr_attr_max)
-> DofSet[N]`) — the post-assembly cohort feeder. This is the same `DofSet[N]` that `fe_assemble`'s
dep-map correctly excludes from its construction stratum (`L4/index.md:100` — `essential_dofs` feeds
THIS cohort, not the assemble fold).

**Strawman reference**: `book/src/design/l4_calculus.md` §3.5 (operator application, `:138-145`) is the
convention for the `K · x_bc` operator-action form; §3.3–3.4 (record/state conventions) for the
`(DofSet[N], DiagPolicy)` BC stratum.

## Lowers to

L4 `eliminate_bc` lowers to the L3 forms via the substantive L4>L3 dissolution theme
[`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)
(this cycle; canonical slug `bc-elimination-post-composition-dissolution`). The rotation is
**substantive** (not identity-in-form): the operator-side pure post-composition collapses to Palace's
**deferred-config-then-apply** two-step (record `(dofs, policy)` on the `ParOperator` wrapper via
`SetEssentialTrueDofs`, then mutate the assembled `HypreParMatrix` in place via `EliminateBC` at
parallel-assemble time — `palace/linalg/rap.cpp:36-47` record, `:139-148` apply); the RHS-side pure
`b − K·x_bc + pin` collapses to the **in-place pooled-scratch** loop (gather essential values onto a
pooled true-dof vector → prolong → local apply → restrict → in-place `b.Add(-1.0, ·)` → in-place
essential-row `SetSubVector` pin — `palace/linalg/rap.cpp:56-83`), with the prolongation/restriction
round-trip realizing the single `apply_linop`. This entry records the rotation *direction* in-line per
high→low discipline; it does **not** author the theme. The two L1>L0 mutation rotations
(`fe-operator-assemble-mutation-rotation` for the operator pin, `eliminate-rhs-mutation-rotation` for
the RHS lift — the latter forthcoming per `L1/eliminate_rhs.md` §"Downward to L0") carry the L1→L0 half;
the L4>L3 theme carries the L4→L3 post-composition-to-imperative-staging half.

## Variant axes

- **diagonal-policy**: `DIAG_ONE` (eliminated diagonal set to `1` — the solve-side convention, makes the
  essential block trivially invertible; the witnessed electrostatic case) | `DIAG_ZERO` (eliminated
  diagonal left `0` — the energy/mass-block convention, the linear free-block projection; the eigen B
  blocks). Both share the row/col-zeroing behavior; they differ only on the essential diagonal (law 3).
  MFEM's third policy `DIAG_KEEP` is out-of-axis (the `ParOperator` boundary admits only the two).
  Absorbed into the `readonly` BC stratum.
- **trial-test-coincidence**: `square` (trial = test space — the only admissible case; `height ==
  width`) | `rectangular` (rejected — a hard L0 reject, `dbc_tdof_list.Size() == 0` required for
  non-square operators). The signature is the square case; the rectangular case is not a variant the
  verb-pair carries.
- **bc-data-homogeneity** (RHS-side only): `homogeneous` (`x_bc = 0` on essential dofs — the interior
  correction vanishes, law 7; the verb collapses to the essential-row pin) | `inhomogeneous` (`x_bc ≠
  0` — the full `b − K·x_bc` lift fires; the electrostatic witness, a unit terminal value).

## Status

`firm` — the post-assembly BC-application verb-pair `(eliminate_essential_bc, eliminate_rhs)` is the
canonical L4 BC-application surface, the assemble-half-completing companion of
[`fe_assemble`](./fe_assemble.md). The promotion is the **firm-on-positive-structure escape** (the
`fe_assemble` / `solve_family` / `apply_linop` precedent): every law (operator-side idempotence, free-
block preservation, policy-determines-only-the-diagonal, DIAG_ZERO-distribution; RHS-side affine-on-
interior linearity, linearity-in-boundary-data, homogeneous-BC identity; the cohort separable-post-
composition framing) is a **read-off syntactic identity** on the positive `EliminateBC` zero-rows-cols-
then-set-diagonal operation (`palace/linalg/rap.cpp:139-148`) + the recorded `(dofs, policy)`
(`:36-47`) + the positive `EliminateRHS` body (`:56-83`), and the laws are the direct L4-vocabulary lift
of the two firm L1 law-sets (`L1/eliminate_essential_bc.md:126-172`, `L1/eliminate_rhs.md:112-162`,
both firm on the same firm-on-positive-structure clean-gate).

The well-foundedness rank invariant holds: the one blocking `depends-on` edge is to
[`linear_combination`](./linear_combination.md) (firm c068, the RHS-side `b − K·x_bc`); the edge to
[`fe_assemble`](./fe_assemble.md) is `reference` (post-composition position, not a blocking fold
dependency — the separability law 8). `firm` therefore rests only on `firm`.

The verb-pair meets the disciplined-cross-pipeline-combinator-mining-gate bar: ≥2 positive witnesses
structurally identical at the load-bearing post-composition shape (electrostatic
`laplaceoperator.cpp:217,252` — `DIAG_ONE` + eigenmode `modeeigensolver.cpp:571,574,608,611` — the
real-stiffness `Ar` block `DIAG_ONE` `:571`, the imaginary-stiffness `Ai` + both mass blocks
`DIAG_ZERO` `:574,608,611`, both policies exercised), no break-witness, and
the over-unification guard honored (the two verbs are genuinely distinct — operator-side
`LinearOperator[N,N]` vs RHS-side `Tensor[N]` — homed as a co-equal PAIR, not merged into one
combinator; the diagonal-policy split is a variant axis, not a 2nd pipeline). No dedicated unit test
exercises BC elimination at this entry point (codemap search of `test/unit/**` for `EliminateBC` /
`SetEssentialTrueDofs` returns no hits), but the missing test does not gate syntactic-identity laws on
fully-specified positive source — the firm-on-positive-structure escape exactly as for `fe_assemble`
and the two firm L1 sources.

This dispatch (cycle-101 D1) closes OQ `bc-elimination-cohort-l4-disposition` (the one genuine in-scope
L4 hole from the cycle-100 completeness survey) on **route (a)** — the cohort lifts cleanly to L4 as a
small post-assembly combinator pair. The coupled L4>L3 dissolution theme
[`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)
lands this same cycle (the cap/theme pair together, avoiding the cross-cycle stale-assertion window).

## L4 vs L3 distinction

- **L3**: the imperative BC-application staging. Operator-side: a deferred-config-then-apply two-step on
  a mutable `ParOperator` wrapper — record `(dofs, policy)` (`SetEssentialTrueDofs`), then mutate the
  assembled `HypreParMatrix` in place (`EliminateBC`) at parallel-assemble time. RHS-side: an in-place
  RHS mutation with pooled scratch — gather/prolong/apply/restrict/in-place-`Add`/in-place-pin. State
  threads through the mutable wrapper + the mutated matrix/RHS.
- **L4**: the pure post-composition verb-pair. `K' = eliminate_essential_bc K dofs policy`,
  `b' = eliminate_rhs K x_bc b policy` — no deferred config, no wrapper state, no in-place mutation, no
  pooled scratch. The `(dofs, policy)` BC stratum is `readonly`, captured once. The deferred-config
  split, the wrapper mutation, the assemble-time staging, the pooled scratch, and the square-operator
  guards are all L4>L3 lowering concerns
  ([`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)).

## Evidence

`eliminate_bc` at L4 is a methodology-level surface distilled from the BC-application machinery Palace
shares across the conforming-FE pipelines; Palace's C++ does not realise the L4 verb-pair form (it
writes the deferred-config-then-apply operator pin + the in-place pooled-scratch RHS loop). All L0
citations self-verified against on-disk source this dispatch via codemap `read_range`.

- `palace/linalg/rap.cpp:36-47` — `ParOperator::SetEssentialTrueDofs(tdof_list, policy)`: records the
  essential-true-dof list (`dbc_tdof_list.MakeRef(tdof_list)`, `:45`) and the diagonal policy
  (`diag_policy = policy`, `:46`); guards `policy ∈ {DIAG_ONE, DIAG_ZERO}` (`:39-41`) and squareness
  (`height == width`, `:42-43`). The deferred-config half of the operator-side L0 operation.
- `palace/linalg/rap.cpp:139-148` — the `EliminateBC` apply block: `RAP->EliminateBC(dbc_tdof_list,
  diag_policy)` (`:143`, guarded by `&trial_fespace == &test_fespace`, `:141`) applies the elimination
  on the assembled square `HypreParMatrix`; the rectangular-reject branch (`:145-148`,
  `MFEM_VERIFY(dbc_tdof_list.Size() == 0, "...only available for square ParOperator!")`) is the
  `trial-test-coincidence` variant-axis L0 anchor.
- `palace/linalg/rap.cpp:56-83` — `ParOperator::EliminateRHS(x, b)`: the full RHS-side L0 body —
  essential gather `linalg::SetSubVector(tx, dbc_tdof_list, x)` (`:64`), prolongation (`:65`),
  unconstrained operator apply `A->Mult(lx, ly)` (`:69`, the `apply_linop`), restriction (`:72`), RHS
  subtraction `b.Add(-1.0, ty)` (`:73`, the `linear_combination`/axpy with `α = −1`), diagonal-policy
  essential-row pin `SetSubVector(b, dbc_tdof_list, x | 0.0)` (`:74-81`).
- `palace/linalg/rap.cpp:18` — `diag_policy(DiagonalPolicy::DIAG_ONE)` ctor default: the diagonal-policy
  variant-axis default value.
- `palace/models/laplaceoperator.cpp:216-217` — the electrostatic operator-side witness:
  `K_l = std::make_unique<ParOperator>(...)` (`:216`) + `SetEssentialTrueDofs(dbc_tdof_lists[l],
  DIAG_ONE)` (`:217`).
- `palace/models/laplaceoperator.cpp:252` — the electrostatic RHS-side witness:
  `PtAP_K->EliminateRHS(X, RHS)` — `eliminate_rhs K x_bc=X b=0 DIAG_ONE`.
- `palace/models/modeeigensolver.cpp:571,574,608,611` — the eigenmode operator-side witnesses:
  `Ar->EliminateBC` / `Ai->EliminateBC` (stiffness A blocks) + `Br->EliminateBC` / `Bi->EliminateBC`
  (mass B blocks), exercising both diagonal policies across the generalized-EVP A/B blocks.
- `book/src/L1/eliminate_essential_bc.md` — the firm L1 operator-side source (the four laws this entry
  lifts, `:126-172`; the separable-post-composition framing, `:99-109,176-195`).
- `book/src/L1/eliminate_rhs.md` — the firm L1 RHS-side source (the four laws `:112-162`; the
  `apply_linop`+`axpy`/`linear_combination` body `:48-58,84-110`).
- `book/src/L1/essential_dofs.md` — the firm L1 `DofSet[N]` producer (`:19,62`); the post-assembly
  cohort feeder (`:22-23,139-140`).
- `book/src/L4/fe_assemble.md` — the assemble-fold combinator this post-composes after; its
  §Algebraic-laws "BC-elimination is NOT part of the fold" is the upstream framing this surface
  realizes.
- **No dedicated test** exercises BC elimination at this entry point (codemap `test/unit/**` search for
  `EliminateBC` / `SetEssentialTrueDofs` / `EliminateRHS` returns no hits); the laws are firm-on-
  positive-structure (read-off syntactic identities), so no test gates them — the same status as the
  two firm L1 sources and `fe_assemble`.
- **Provenance**: harvested cycle-101 D1 from OQ `bc-elimination-cohort-l4-disposition` (the cycle-100
  completeness-survey hole); the two firm L1 sources (cycle-053) + the firm L1 `essential_dofs`
  (cycle-066) + the firm L4 `fe_assemble` (cycle-068) + `linear_combination` (cycle-068) are the direct
  inputs.
```

```new:book/src/L4-L3/bc-elimination-post-composition-dissolution.md
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

# bc-elimination-post-composition-dissolution

The L4>L3 dissolution of the [`eliminate_bc`](../L4/eliminate_bc.md) post-assembly BC-application
verb-pair into Palace's imperative BC staging. **Substantive** (not identity-in-form): the two pure
post-compositions collapse to a **deferred-config-then-apply** operator pin and an **in-place pooled-
scratch** RHS-mutation loop.

## Context

A lowering theme rewrites an L4 form of shape A into an L3 form of shape B. The
[`eliminate_bc`](../L4/eliminate_bc.md) L4 surface is the pure post-assembly Dirichlet-BC verb-pair
`(eliminate_essential_bc, eliminate_rhs)` over the `readonly` `(DofSet[N], DiagPolicy)` BC stratum;
this theme narrates how it lowers (L4→L3 direction, per high→low discipline) into the L3 imperative
staging Palace actually writes.

This is the **post-composition sibling** of the [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
theme: where `fe-assemble-fold-dissolution` lowers the assemble FOLD that builds `K`, this theme lowers
the BC verb-pair that post-composes on the assembled `K` (the operator pin) and the `(K, b)` pair (the
RHS lift). The two themes together cover the assemble + BC-application halves of the FE-operator
construction surface.

## LHS (L4) → RHS (L3)

### Operator-side: `eliminate_essential_bc` → deferred-config-then-apply

The L4 pure post-composition `K' = eliminate_essential_bc K dofs policy` (zero essential rows/cols, set
the eliminated diagonal per policy; the linear free-block projection `K ↦ P_F K P_F` under DIAG_ZERO)
dissolves to the L3 **two-step on a mutable `ParOperator` wrapper**:

1. **Record** the `(dofs, policy)` BC stratum on the wrapper — `SetEssentialTrueDofs(tdof_list, policy)`
   stores `dbc_tdof_list` + `diag_policy` (`palace/linalg/rap.cpp:36-47`, the `:45-46` writes; guards
   `policy ∈ {DIAG_ONE, DIAG_ZERO}` `:39-41` and squareness `:42-43`). The L4 `readonly` BC stratum
   captured once dissolves to this deferred mutation of the wrapper's `dbc_tdof_list`/`diag_policy`
   members.
2. **Apply** at parallel-assemble time — `RAP->EliminateBC(dbc_tdof_list, diag_policy)`
   (`palace/linalg/rap.cpp:139-148`, the call at `:143` guarded square `:141`) mutates the assembled
   `HypreParMatrix` **in place** (zero rows/cols + set diagonal per policy). The L4 fresh-value-returning
   post-composition dissolves to this destructive matrix mutation; the rectangular case is a hard L0
   reject (`:145-148`).

Substantive: the pure value-returning post-composition → a deferred-config record + an in-place matrix
mutation, the `readonly` BC stratum → mutable wrapper state, the squareness precondition → an
`MFEM_VERIFY` guard + a rectangular-reject branch. The operator-pin L1→L0 half is carried by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) theme
(which narrates the FE-assembly build-up-then-assemble protocol + the separable BC-elimination
post-compositions).

### RHS-side: `eliminate_rhs` → in-place pooled-scratch loop

The L4 pure post-composition `b' = eliminate_rhs K x_bc b policy` (`b − K·x_bc` then pin the essential
rows; one `apply_linop` + one `linear_combination` + one essential-row scatter) dissolves to the L3
**in-place RHS mutation with pooled scratch** (`palace/linalg/rap.cpp:56-83`):

- gather essential values onto a zeroed pooled true-dof vector `tx` (`SetSubVector(tx, dbc_tdof_list,
  x)`, `:62-64`) → prolong to a pooled local vector `lx` (`:65`) → apply the local matrix into a pooled
  local output `ly` (`A->Mult(lx, ly)`, `:69`, the `apply_linop`) → restrict to a pooled true-dof
  vector `ty` (`:71-72`);
- mutate `b` **in place** by `b.Add(-1.0, ty)` (`:73`, the `linear_combination [(1,b),(-1,y)]` / axpy
  with `α = −1`);
- overwrite `b`'s essential rows **in place** by `SetSubVector` (`:74-81`, the diagonal-policy pin —
  `x` for DIAG_ONE `:76`, `0.0` for DIAG_ZERO `:80`).

Substantive: the pure value-returning post-composition → an in-place `b` mutation threaded through five
pooled MFEM vectors, the single logical `apply_linop` → the prolongation→local-apply→restriction
round-trip (the assembled operator's galerkin true-dof action realized on the fly), the
`linear_combination` → the in-place `b.Add`, the essential-row pin → an in-place `SetSubVector`. The
RHS-side L1→L0 half is carried by the (forthcoming) `eliminate-rhs-mutation-rotation` theme (referenced
in plain text per the missing-anchor convention — no
`book/src/L1-L0/eliminate-rhs-mutation-rotation.md` exists yet; see `L1/eliminate_rhs.md` §"Downward to
L0").

## What does NOT change in the rotation

The **separable post-composition position** survives the rotation unchanged — both verbs still consume
the *already-assembled* operator value and run AFTER the assemble fold, never inside it (the L4 cap's
law 8; the L3 staging is likewise applied after assembly, at parallel-assemble time for the operator
pin, at excitation-vector-build time for the RHS lift). The **free/essential block structure** survives
(the operator pin still touches only essential rows/cols; the RHS lift still affects the interior block
by `b − K·x_bc` and the essential block by the pin). The **diagonal-policy semantics** survive
(DIAG_ONE solve-side, DIAG_ZERO energy-block; identical row/col-zeroing). The verbs carry **NO
`sequential-obstruction`** — they are one-shot post-compositions, not iterations (the contrast with
`fold_solve`'s carry-threaded sweep).

## What this lowering does NOT cover

- **The assemble fold that builds `K`** — that is the [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
  theme. This theme lowers only the BC post-compositions ON the assembled `K`.
- **The `DofSet[N]` construction** — the boundary-attribute → essential-true-dof-set build is the firm
  L1 [`essential_dofs`](../L1/essential_dofs.md), lowered by its own
  `essential-dofs-construction-rotation` L1>L0 theme. This theme consumes `DofSet[N]` as a given operand.
- **The libCEED/MFEM kernel interiors** — the `EliminateBC` HYPRE matrix mutation and the prolongation/
  restriction MFEM operators are library-owned (out of scope per CLAUDE.md §Target-system — "cite
  Palace source, not vendored upstream"); the theme records Palace's CALLs, not the library bodies.
- **The L3>L2 hop.** There is **no standalone `L3/eliminate_bc` entry warranted** — the BC verb-pair
  carries no `sequential-obstruction` (one-shot post-compositions; nothing to iterate-rotate), so its
  L3 image is the imperative staging described above, homed here. This matches the
  `solve-family-map-dissolution` / `fe-assemble-fold-dissolution` NO-ENTRY pattern: a standalone L3
  chapter would mirror this theme's RHS (the §1d anti-mirror smell). This L4>L3 theme is the
  **authoritative downward home** for the BC-application post-composition pair.

## L3-entry-vs-dissolution-home verdict

**WARRANT-FIRST: DISSOLUTION-HOME (no interposed `L3/eliminate_bc` entry).** The decision criterion (per
the `fold_solve` c059 L3-ENTRY vs `solve_family` c057 / `fe_assemble` c068 NO-ENTRY precedents): does the
L3 image carry a `sequential-obstruction` or `partial-obstruction` warranting a standing iteration-
rotation chapter? **No** — the BC verb-pair lowers to two one-shot imperative stagings (a deferred-
config-then-apply operator mutation + an in-place pooled-scratch RHS mutation), neither an iteration.
There is no loop to rotate, no carry to thread, no obstruction to render. A standalone `L3/eliminate_bc`
would be a degenerate identity-in-named-terms restatement of this theme's RHS — the vocabulary-shift-
redirect anti-mirror smell. This theme is the authoritative L3-form home.

## Evidence

- `palace/linalg/rap.cpp:36-47` — `SetEssentialTrueDofs` (the operator-side deferred-config record;
  `:45-46` writes, `:39-43` guards). Codemap-verified this dispatch.
- `palace/linalg/rap.cpp:139-148` — the `EliminateBC` in-place apply (`:143` call, `:141` square guard,
  `:145-148` rectangular reject). Codemap-verified this dispatch.
- `palace/linalg/rap.cpp:56-83` — `EliminateRHS` (the RHS-side in-place pooled-scratch loop: gather
  `:64`, prolong `:65`, apply `:69`, restrict `:72`, in-place `b.Add(-1.0,·)` `:73`, in-place pin
  `:74-81`). Codemap-verified this dispatch.
- `book/src/L4/eliminate_bc.md` — the LHS L4 verb-pair (the eight laws this theme's RHS realizes; the
  in-line §"Lowers to" rotation direction).
- `book/src/L1/eliminate_essential_bc.md` / `book/src/L1/eliminate_rhs.md` — the firm L1 sources; their
  §"L1 vs L0 distinction" + §"Downward to L0" prose is the L1→L0 half this theme's L4→L3 half composes
  with.
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` — the operator-side L1>L0 theme (the
  build-up-then-assemble protocol + the separable BC-elimination post-compositions).
- **Provenance**: cycle-101 D1, the coupled L4>L3 theme for the `eliminate_bc` cap landed this same
  cycle; closes OQ `bc-elimination-cohort-l4-disposition` (route (a)) jointly with the cap.
```

```edit:book/src/L4/fe_assemble.md
- `space` — `FiniteElementSpace[N]` — the trial/test finite-element space, **captured once at assembly construction; `readonly`** per [`state-stratification`](../concepts/state-stratification.md). `N = space.GetTrueVSize()` is the global true-dof count (the operator's square dimension). This is the load-bearing typing: `space` is bound *once, outside the fold*, and threaded *unchanged* into every `assemble_term` call — the L4 typing of the single `BilinearForm k(GetH1Space())` construction the term-appends share. The **three FE construction inputs** (`fe_space` / `fe_collection` / `essential_dofs`) are **absorbed into this `FiniteElementSpace[N]` `readonly` construction stratum** (the `OpParams`/`readonly` state-stratification home, `L4/index.md:24`): `fe_collection` is the basis the space is built over, `fe_space` the construction itself, `essential_dofs` the BC dof-set carried for the separable post-composition — none shape the fold, so none gets a standalone thin chapter (the combinator-as-entry default; re-open per downstream-consumer demand, see §Open questions).
- `space` — `FiniteElementSpace[N]` — the trial/test finite-element space, **captured once at assembly construction; `readonly`** per [`state-stratification`](../concepts/state-stratification.md). `N = space.GetTrueVSize()` is the global true-dof count (the operator's square dimension). This is the load-bearing typing: `space` is bound *once, outside the fold*, and threaded *unchanged* into every `assemble_term` call — the L4 typing of the single `BilinearForm k(GetH1Space())` construction the term-appends share. The **two FE construction inputs** (`fe_space` / `fe_collection`) are **absorbed into this `FiniteElementSpace[N]` `readonly` construction stratum** (the `OpParams`/`readonly` state-stratification home, `L4/index.md:24`): `fe_collection` is the basis the space is built over, `fe_space` the construction itself — neither shapes the fold, so neither gets a standalone thin chapter (the combinator-as-entry default; re-open per downstream-consumer demand, see §Open questions). `essential_dofs` is **NOT** a `fe_assemble` construction input: it produces the `DofSet[N]` consumed by the *post-assembly* BC cohort [`eliminate_bc`](./eliminate_bc.md) (`eliminate_essential_bc`/`eliminate_rhs`, `L1/essential_dofs.md:22-23,139-140`), a separable post-composition that runs AFTER this fold — see §"Algebraic laws" "BC-elimination is NOT part of the fold".
```

```edit:book/src/L4/fe_assemble.md
- **BC-elimination is NOT part of the fold.** Pinning essential (Dirichlet) dofs (`eliminate_essential_bc`) and lifting inhomogeneous Dirichlet data into the RHS (`eliminate_rhs`) are **separable post-compositions** on the assembled operator, valid independently of how it was assembled — not laws of `fe_assemble`. They consume `essential_dofs` (absorbed into the `readonly` construction stratum) but compose *after* the fold. Inherited from `L1/fe_assemble.md:150-155`; they are sibling deferred operators (the rank-3/4 c069 candidates, gated on primitive-L4-presence per the planner OQ).
- **BC-elimination is NOT part of the fold.** Pinning essential (Dirichlet) dofs (`eliminate_essential_bc`) and lifting inhomogeneous Dirichlet data into the RHS (`eliminate_rhs`) are **separable post-compositions** on the assembled operator, valid independently of how it was assembled — not laws of `fe_assemble`. They consume the `DofSet[N]` that [`essential_dofs`](../L1/essential_dofs.md) produces (NOT a `fe_assemble` construction input — it feeds the post-assembly cohort) but compose *after* the fold. Inherited from `L1/fe_assemble.md:150-155`; they are the firm L4 post-assembly BC-application verb-pair [`eliminate_bc`](./eliminate_bc.md) (cycle-101 D1 — the cohort lifted cleanly to L4 as a separable post-composition pair, route (a); closed OQ `bc-elimination-cohort-l4-disposition`).
```

```edit:book/src/L4/fe_assemble.md
The variant-axis profile is closed at four axes, all absorbed (none coordination-shaping). The three construction inputs (`fe_space` / `fe_collection` / `essential_dofs`) are absorbed into the `readonly` `FiniteElementSpace[N]` construction stratum (no standalone thin chapters; re-open per downstream-consumer demand). This dispatch (cycle-068 D1) is the **rank-1 FE-cohort→L4 lift** opening the assemble-half of the deliverable's L4 surface (directive 1); the coupled L4>L3 dissolution theme [`fe-assemble-fold-dissolution`](../L4-L3/fe-assemble-fold-dissolution.md) is D2's job this same cycle (the cap/theme pair lands together, avoiding the cross-cycle stale-assertion window).
The variant-axis profile is closed at four axes, all absorbed (none coordination-shaping). The two construction inputs (`fe_space` / `fe_collection`) are absorbed into the `readonly` `FiniteElementSpace[N]` construction stratum (no standalone thin chapters; re-open per downstream-consumer demand). `essential_dofs` is NOT among them — it produces the `DofSet[N]` consumed by the *post-assembly* BC-application cohort [`eliminate_bc`](./eliminate_bc.md), a separable post-composition that runs AFTER this fold (cycle-101 D1; OQ `bc-elimination-cohort-l4-disposition` closed on route (a)). This dispatch (cycle-068 D1) is the **rank-1 FE-cohort→L4 lift** opening the assemble-half of the deliverable's L4 surface (directive 1); the coupled L4>L3 dissolution theme [`fe-assemble-fold-dissolution`](../L4-L3/fe-assemble-fold-dissolution.md) is D2's job this same cycle (the cap/theme pair lands together, avoiding the cross-cycle stale-assertion window).
```

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
- **BC-elimination.** Pinning essential dofs (`eliminate_essential_bc`) and lifting Dirichlet data into the RHS (`eliminate_rhs`) are **separable post-compositions** on the assembled operator (the L1 cap §"Algebraic laws" — explicitly NOT laws of `fe_assemble`), valid independently of how it was assembled. They are sibling speculative operators (the planner's ranks 3-4, deferred to c069), NOT part of this assemble-fold dissolution.
- **BC-elimination.** Pinning essential dofs (`eliminate_essential_bc`) and lifting Dirichlet data into the RHS (`eliminate_rhs`) are **separable post-compositions** on the assembled operator (the L1 cap §"Algebraic laws" — explicitly NOT laws of `fe_assemble`), valid independently of how it was assembled. They are the firm L4 post-assembly BC-application verb-pair [`eliminate_bc`](../L4/eliminate_bc.md) (cycle-101 D1 — lifted cleanly to L4 as a separable post-composition pair, route (a)), lowered by the sibling [`bc-elimination-post-composition-dissolution`](./bc-elimination-post-composition-dissolution.md) theme, NOT part of this assemble-fold dissolution.
```

```edit:book/src/L4/index.md
| [`fe_assemble`](./fe_assemble.md) | `fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]`; entry `fe_assemble space terms = foldr (\t acc -> assemble_term space t + acc) zero terms = sum (map (assemble_term space) terms)`. The **assemble-fold combinator**: capture the FE space once (`readonly`), fold an immutable weak-form-term list by the opaque per-term leaf `assemble_term`, and **sum** the contributions into a global operator `K`. The **concatenation-homomorphism `foldr` producing a sum** — the homomorphic sibling of [`solve_family`](./solve_family.md)'s map (both fold independent per-element work; `solve_family` reduces by list-collect, `fe_assemble` by operator-`+`), distinct from [`fold_solve`](./fold_solve.md)'s carry-threaded sequential fold (homomorphism does NOT hold there; HOLDS here). The opaque per-term libCEED quadrature leaf `assemble_term` rises as a **black-box-kernel `readonly` input** (the `eigsolve`/`fold_solve` opaque-leaf pattern). | Concepts: `black-box-vs-accelerated-kernels` (the assemble-fold = combinator-rises / libCEED-leaf = black-box-kernel-rises-as-input disposition, case 1), `state-stratification` (`space` the shared `readonly` construction stratum captured once — the two construction inputs `fe_space`/`fe_collection` absorbed; `essential_dofs` is NOT a `fe_assemble` input, it feeds the *post-assembly* BC cohort `eliminate_essential_bc`/`eliminate_rhs`, `L1/essential_dofs.md:22-23,72`, L4 disposition open — OQ `bc-elimination-cohort-l4-disposition`), `variant-absorption`, `derived-view-hoisting`, `constructed-operators`, `solver-as-operator`. L4 rows: [`weak_form_term`](../L1/weak_form_term.md) (the list element-type, folded opaquely); homomorphic-sibling [`solve_family`](./solve_family.md); contrast-sibling [`fold_solve`](./fold_solve.md). Black-box-kernel input: `assemble_term` (libCEED-owned, lifts the `L1-L0/fe-assemble-libceed-boundary-obstruction`). | L3 the global tensor-field assembly view (explicit composite-operator accumulation, the per-term leaf bottoming out in the libCEED boundary) via the **substantive** L4>L3 theme [`fe-assemble-fold-dissolution`](../L4-L3/fe-assemble-fold-dissolution.md) (cycle-068 D2; this same cycle): the `foldr`/sum collapses to the explicit accumulating build, the space-capture-once hoist becomes `BilinearForm space(...)`-outside-the-loop, the leaf bottoms out in `obstruction (opaque-library-ownership)`. L3-entry-vs-dissolution-home verdict is D2's (likely the `solve_family` NO-ENTRY shape — the term fold lifts, no `sequential-obstruction`). | `firm` (harvested cycle-068 D1; firm-on-positive-structure escape — every fold law is a read-off syntactic identity on the positive integrator-fold structure `palace/fem/bilinearform.cpp:71-104` + the firm L1 `fe_assemble`, lifting its four laws; ≥2-witness mining-gate met (3 witnesses: electrostatic ∇ `laplaceoperator.cpp:191-194`, magnetostatic ∇× `curlcurloperator.cpp:178-181`, mass I `spaceoperator.cpp:278`), no break-witness, map-not-fold guard honored. Rank-1 FE-cohort→L4 lift, plan-tag `fe-cohort-l4-lift`) |
| [`eliminate_bc`](./eliminate_bc.md) | `eliminate_essential_bc :: LinearOperator[N,N] -> DofSet[N] -> DiagPolicy -> LinearOperator[N,N]`; `eliminate_rhs :: LinearOperator[N,N] -> Tensor[N] -> Tensor[N] -> DiagPolicy -> Tensor[N]` (`= set_essential (linear_combination [(1,b),(-1, apply_linop K (restrict_essential x_bc))]) pin`). The **post-assembly boundary-condition application surface**: the two co-equal separable-post-composition verbs that pin essential (Dirichlet) dofs into an assembled operator (operator-side, the linear free-block projection `P_F K P_F` under DIAG_ZERO) and lift the inhomogeneous Dirichlet data into the RHS (RHS-side, `b − K·x_bc` + essential-row pin). Both compose AFTER [`fe_assemble`](./fe_assemble.md) on the assembled `K` value — independent of HOW `K` was assembled (the separability law; explicitly NOT a `fe_assemble` fold law). The assemble-half-completing companion of `fe_assemble`. Consumes the `DofSet[N]` produced by [`essential_dofs`](../L1/essential_dofs.md) (the post-assembly cohort feeder, NOT a `fe_assemble` input). Pure value-producing — no `Solve` monad / carry / predicate. | Reference (post-composes after, NOT a blocking fold dep): [`fe_assemble`](./fe_assemble.md). Depends-on: [`linear_combination`](./linear_combination.md) (firm c068 — the RHS-side `b − K·x_bc`). Folds/uses: [`apply_linop`](../L1/apply_linop.md) (the RHS-side `K·x_bc`), `set_subvector` essential-dof mask ([`set_subvector_zero`](../concepts/set_subvector_zero.md) the DIAG_ZERO arm). Concepts: `state-stratification` (the `(DofSet[N], DiagPolicy)` `readonly` BC stratum), `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"), `constructed-operators`. Produces-input: [`essential_dofs`](../L1/essential_dofs.md) (the `DofSet[N]`). Record `DofSet[N]` cross-cutting — needs concept home (OQ `record-DofSet-needs-definition-home`). | L3 the imperative BC staging (operator-side deferred-config-then-apply on a mutable `ParOperator`; RHS-side in-place pooled-scratch loop) via the **substantive** L4>L3 theme [`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md) (cycle-101 D1; this same cycle). DISSOLUTION-HOME verdict — no interposed `L3/eliminate_bc` (the verbs carry no `sequential-obstruction`; one-shot post-compositions, nothing to iterate-rotate; the `solve_family`/`fe_assemble` NO-ENTRY shape). | `firm` (harvested cycle-101 D1 from OQ `bc-elimination-cohort-l4-disposition` — the one genuine in-scope L4 hole from the c100 completeness survey, resolved on route (a): the cohort lifts cleanly to L4 as a separable post-composition pair. Firm-on-positive-structure / syntactic-identity escape — every law a read-off syntactic identity on the positive `EliminateBC`/`EliminateRHS` source (`palace/linalg/rap.cpp:36-47,56-83,139-148`) + the two firm L1 sources `eliminate_essential_bc`/`eliminate_rhs` (cycle-053), lifting their law-sets unchanged. ≥2-witness mining-gate met (electrostatic `laplaceoperator.cpp:217,252` + eigenmode `modeeigensolver.cpp:571,574,608,611`, both policies), no break-witness, over-unification guard honored (two distinct verbs homed as a co-equal PAIR, not merged). `depends-on: linear_combination` firm so the rank invariant holds; the `fe_assemble` edge is `reference`, no rank constraint. No dedicated test gates the syntactic-identity laws) |
```

```edit:book/src/SUMMARY.md
  - [eigenfreq_qfactor_reduce](./L4/eigenfreq_qfactor_reduce.md)
  - [eliminate_bc](./L4/eliminate_bc.md)
  - [fe_assemble](./L4/fe_assemble.md)
```

```edit:book/src/SUMMARY.md
- [Overview](./L4-L3/index.md)
- [bc-elimination-post-composition-dissolution](./L4-L3/bc-elimination-post-composition-dissolution.md)
- [fe-assemble-fold-dissolution](./L4-L3/fe-assemble-fold-dissolution.md)
```

```edit:book/src/L4-L3/index.md
| [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md) | L4 [`fe_assemble`](../L4/fe_assemble.md) **assemble-fold combinator** — the concatenation-homomorphism `foldr (\t acc -> assemble_term space t + acc) zero terms = Σ assemble_term space t`: the once-captured `readonly` `space` stratum, the **homomorphic map-then-reduce** over the independent weak-form **term** family, the opaque quantified-over per-term `assemble_term` leaf, the single logical `[WeakFormTerm]` list. The **homomorphic sibling** of `solve-family-map-dissolution`'s map shell (same NO-carry family-loop; different reduction + leaf). | L3 explicit **imperative integrator-fold**: the once-captured `readonly` `space` stratum dissolves to the `CeedElemRestriction`/`CeedBasis` FE context hoisted by hand outside the loops (`bilinearform.cpp:64-70`); the homomorphic map-then-reduce dissolves to **two** positional `for` loops over `domain_integs`/`boundary_integs` accumulating each per-term sub-operator into a mutable composite by `op->AddSubOperator(sub_op)` (`:77`/`:97`) then `Finalize()` (`:104`); the opaque per-term leaf resolves to the **opaque libCEED element-local quadrature kernel** (`integ->Assemble`, `:75` → `palace/fem/integrator.hpp:58-61`; `obstruction (opaque-library-ownership)` per-term sub-leaf, already recorded by `L1-L0/fe-assemble-libceed-boundary-obstruction.md`, negative anchor Palace's CALL `:75`, NOT libCEED internals); the single list splits into the domain/boundary two-container split (re-unified by the homomorphism). Substantive (a homomorphic-`foldr` → imperative-integrator-fold translation: operator-`+` sum → `AddSubOperator` accumulation, single list → two-container split, opaque `assemble_term` → `integ->Assemble` libCEED boundary). The integrator-fold carries **NO `sequential-obstruction`** (term-position commutativity; the reduction is embarrassingly parallel, exploited one-`Ceed`-per-thread) — the homomorphic-sibling alignment with the map theme, the contrast with `fold_solve`'s carry-threaded sweep. | `structural` + secondary `reduction-chain` | `firm` (cycle-068 D2 abstractor; the assemble-fold-shell rotation for the `L4/fe_assemble` combinator D1 firmed this cycle; **homomorphic sibling** of `solve-family-map-dissolution` (firm c055) — same NO-carry family-loop, differing in reduction (reduce-by-`+` vs collect-into-vector) + leaf (libCEED-opaque vs lowers); firm on the outer-fold structural rotation — read directly off positive source (`bilinearform.cpp:28-107`, L0 nav `fem-bilinearform-file.md`); per-term `integ->Assemble` libCEED body the `obstruction (opaque-library-ownership)` sub-leaf (recorded via `L1-L0/fe-assemble-libceed-boundary-obstruction.md`, not lowered); DISSOLUTION-HOME verdict — no interposed `L3/fe_assemble` (matches the map sibling's c057 NO-ENTRY); covers the single FE-assembly machinery all 5 pipelines share) |
| [`bc-elimination-post-composition-dissolution`](./bc-elimination-post-composition-dissolution.md) | L4 [`eliminate_bc`](../L4/eliminate_bc.md) **post-assembly BC-application verb-pair** — the two pure separable post-compositions `eliminate_essential_bc K dofs policy` (operator-side pin) + `eliminate_rhs K x_bc b policy` (RHS-side `b − K·x_bc` + essential-row pin) over the `readonly` `(DofSet[N], DiagPolicy)` BC stratum; both post-compose AFTER the `fe_assemble` fold on the assembled `K` value. | L3 the **imperative BC staging**: operator-side → a **deferred-config-then-apply** two-step on a mutable `ParOperator` (record `(dofs, policy)` via `SetEssentialTrueDofs` `rap.cpp:36-47`, then mutate the assembled `HypreParMatrix` IN PLACE via `EliminateBC` `:139-148` at parallel-assemble time); RHS-side → an **in-place pooled-scratch** loop (gather `:64` → prolong `:65` → local apply `A->Mult` `:69` → restrict `:72` → in-place `b.Add(-1.0,·)` `:73` → in-place essential-row `SetSubVector` pin `:74-81`). Substantive (pure value-returning post-composition → deferred-config record + in-place matrix/RHS mutation; `readonly` BC stratum → mutable wrapper state; the single `apply_linop` → the prolong/local-apply/restrict round-trip; the `linear_combination` → in-place `b.Add`). The verbs carry **NO `sequential-obstruction`** (one-shot post-compositions, not iterations — the contrast with `fold_solve`'s carry-threaded sweep). The L1→L0 halves are the operator-side [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) + the RHS-side `eliminate-rhs-mutation-rotation` (forthcoming). | `structural` | `firm` (cycle-101 D1; the coupled L4>L3 theme for the `L4/eliminate_bc` cap landed this same cycle; the **post-composition sibling** of `fe-assemble-fold-dissolution` (firm c068) — that theme lowers the assemble FOLD that builds `K`, this lowers the BC verb-pair that post-composes on the assembled `K`/`(K,b)`; firm on the structural rotation — read directly off positive source (`rap.cpp:36-47,56-83,139-148`) + the two firm L1 sources; **DISSOLUTION-HOME verdict** — no interposed `L3/eliminate_bc` (the verbs carry no `sequential-obstruction`; one-shot post-compositions, nothing to iterate-rotate; the `solve_family`/`fe_assemble` NO-ENTRY shape); closes OQ `bc-elimination-cohort-l4-disposition` (route (a)) jointly with the cap) |
```

```edit:book/src/L4-L3/index.md
**Substantive themes (firm):**

- [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md) — the L4 `fe_assemble` **assemble-fold combinator** → L3 explicit imperative **integrator-fold**. A genuine homomorphic-`foldr` → imperative-integrator-fold translation: the **operator-`+` sum → `AddSubOperator` accumulation into a mutable composite**, the single logical `[WeakFormTerm]` list → the domain/boundary two-container split (`for` over `domain_integs`/`boundary_integs`, re-unified by the concatenation homomorphism), the opaque quantified-over per-term `assemble_term` → the `integ->Assemble` **libCEED element-local quadrature kernel** (`obstruction (opaque-library-ownership)` per-term sub-leaf — negative anchor Palace's CALL `bilinearform.cpp:75`, recorded via [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) NOT lowered). The **homomorphic SIBLING** of [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) (NOT the carry-threaded `fold_solve` — the map-not-fold guard): same NO-carry family-loop semantics; the load-bearing differences are the **reduction shape** (reduce-by-operator-`+` vs the map's collect-into-`std::vector` slot) and the **leaf** (libCEED-opaque vs the map's per-member solve that lowers). The integrator-fold carries **NO `sequential-obstruction`** (term-position commutativity; the reduction is embarrassingly parallel, here exploited one-`Ceed`-per-OMP-thread). Firm on the outer-fold structural rotation; **DISSOLUTION-HOME verdict** — no interposed `L3/fe_assemble` (matches the map sibling's c057 NO-ENTRY); covers the single FE-assembly machinery all 5 pipelines share. Cycle-068 D2.
- [`bc-elimination-post-composition-dissolution`](./bc-elimination-post-composition-dissolution.md) — the L4 `eliminate_bc` **post-assembly BC-application verb-pair** → L3 the imperative BC staging. A genuine pure-post-composition → imperative-staging translation: the operator-side pin → a **deferred-config-then-apply** two-step on a mutable `ParOperator` (record `(dofs, policy)` then mutate the assembled `HypreParMatrix` IN PLACE at parallel-assemble time, `rap.cpp:36-47`/`:139-148`); the RHS-side `b − K·x_bc` + pin → an **in-place pooled-scratch** loop (`rap.cpp:56-83`, the in-place `b.Add(-1.0,·)` + essential-row `SetSubVector`). The **post-composition sibling** of [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md): that theme lowers the assemble FOLD that builds `K`, this lowers the BC verb-pair that post-composes on the assembled `K` (operator pin) and `(K, b)` pair (RHS lift) — together the assemble + BC-application halves of the FE-operator construction surface. The verbs carry **NO `sequential-obstruction`** (one-shot post-compositions, not iterations — the contrast with `fold_solve`'s carry-threaded sweep). Firm on the structural rotation; **DISSOLUTION-HOME verdict** — no interposed `L3/eliminate_bc` (nothing to iterate-rotate; the `solve_family`/`fe_assemble` NO-ENTRY shape). The L1→L0 halves are the operator-side `fe-operator-assemble-mutation-rotation` + the RHS-side `eliminate-rhs-mutation-rotation` (forthcoming). Cycle-101 D1.
```

```edit:book/src/L4-L3/index.md
**Consolidated tally (firm L4>L3 themes: 10 → 11 this cycle).** Counted from the on-disk theme-list table above: **11 firm** themes — `krylov-step-typed-wrapper-dissolution` (c006 abstractor, firm c008 lifter), `gmres-inner-loop-iterate-while-migration` (c008 abstractor, firm c020 lifter), `fgmres-inner-loop-iterate-while-migration` (c011 lifter, firm c021), `iterate-while-dissolution` (c047), `iterate-while-with-prev-dissolution` (c047), `ksp-solve-driver-dissolution` (c048), `solve-family-map-dissolution` (cycle-055 D2), `fold-solve-time-step-dissolution` (cycle-058 D2), `fe-assemble-fold-dissolution` (cycle-068 D2), `frequency-sweep-dissolution` (cycle-070 D2), and `bc-elimination-post-composition-dissolution` (cycle-101 D1, this cohort); **0 rough-in**. The cycle-101 D1 landing is **substantive** (a pure-post-composition → imperative-staging translation: the operator-side pin dissolving to a deferred-config-then-apply two-step on a mutable `ParOperator` + an in-place `HypreParMatrix` mutation, the RHS-side `b − K·x_bc` + pin dissolving to an in-place pooled-scratch loop — honoring the vocabulary-shift redirect). It is the **post-composition sibling** of the cycle-068 `fe-assemble-fold-dissolution` assemble-fold rotation (that theme lowers the assemble FOLD that builds `K`; this lowers the BC verb-pair that post-composes on the assembled `K`/`(K,b)` pair) — together they cover the assemble + BC-application halves of the FE-operator construction surface. With the `solve_family` fixed-operator map, the `fold_solve` carry-threaded fold, the `frequency_sweep` operator-varying map, the `fe_assemble` assemble-fold, and now the `eliminate_bc` BC-application post-composition all landed, the L4>L3 hop covers the operator-capture axis (fixed vs per-element) and the carry axis (map vs fold) across the solver half AND the assemble + BC-application halves of the FE-assembly stack. **This cycle's L4>L3 row+bullet+tally are all D1-authored** (sole index toucher; no separate count-owner named — D1 also owns the distinct `L4/index.md` tally).
```

## Operator content

The full firm `eliminate_bc` L4 chapter body is authored inside the `new:book/src/L4/eliminate_bc.md`
proposed-changes fence above (Status `firm`; Signature with the two-verb shape contract + the `DofSet[N]`
/ `DiagPolicy` BC stratum; Record-definition section flagging `DofSet[N]` as the cross-cutting record
needing a concept home; eight Algebraic laws split operator-side / RHS-side / cohort-level with the
non-laws catalogued; Dependencies with the `reference` vs `depends-on` edge classification; Evidence
with all L0 citations self-verified via codemap `read_range` this dispatch). The coupled L4>L3 theme is
the `new:book/src/L4-L3/bc-elimination-post-composition-dissolution.md` fence.

## Supporting evidence

- L0 source self-verified via codemap `read_range` this dispatch: `palace/linalg/rap.cpp:16-20` (ctor
  `diag_policy` default `:18`), `:36-47` (`SetEssentialTrueDofs` record), `:56-83` (`EliminateRHS`
  body), `:139-148` (`EliminateBC` apply block + rectangular reject). Witness sites
  `palace/models/laplaceoperator.cpp:214-218` (`SetEssentialTrueDofs` `:217`, construction `:216`),
  `:248-253` (`EliminateRHS(X, RHS)` `:252`). The eigenmode witnesses
  `modeeigensolver.cpp:571,574,608,611` were re-read via codemap `read_range` during the cycle-101
  repair pass to confirm the exact per-block policy split: `Ar`→`DIAG_ONE` (`:571`), `Ai`→`DIAG_ZERO`
  (`:574`), `Br`→`DIAG_ZERO` (`:608`), `Bi`→`DIAG_ZERO` (`:611`).
- Firm L1 sources: `book/src/L1/eliminate_essential_bc.md` (laws `:126-172`, post-composition framing
  `:99-109`), `book/src/L1/eliminate_rhs.md` (laws `:112-162`, body `:48-58,84-110`),
  `book/src/L1/essential_dofs.md` (`DofSet[N]` producer `:19,62`; post-assembly-cohort-feeder
  `:22-23,139-140`).
- Firm L4 inputs: `book/src/L4/fe_assemble.md` (the assemble-half companion + the "BC-elimination is NOT
  part of the fold" framing), `book/src/L4/linear_combination.md` (the RHS-side `b − K·x_bc`
  depends-on, firm c068).
- c069 deferral sites resolved: `L4/fe_assemble.md:119` (now points to the firm `eliminate_bc`),
  `L4-L3/fe-assemble-fold-dissolution.md:127` (now points to the firm cap + sibling theme).

## Open questions / caveats

- **`record-DofSet-needs-definition-home`** (FLAG, not authored this cycle — judge-on-touch per dispatch).
  `DofSet[N]` (the essential-true-dof index set) has ≥2 consumers (`eliminate_essential_bc`,
  `eliminate_rhs`, the L4 `eliminate_bc` cap) + the `essential_dofs` producer, and is described only by
  use across the L1/L4 entries — no `book/src/concepts/DofSet.md` page exists. Per the record-definition
  obligation (≥2 consumers ⇒ concept page, layer-intro-author's domain), this needs a definition home
  defining the data shape (immutable index set over the true-dof axis `N`, subset of `0..N`; L0 backing
  `mfem::Array<int> dbc_tdof_list`, `palace/linalg/rap.cpp:45-46`; built by `essential_dofs`,
  `palace/fem/multigrid.hpp:99-100`). The `eliminate_bc` §"Record definition" section carries the working
  description + the cross-reference pointer pending the page.
- **`eliminate-rhs-mutation-rotation` L1>L0 theme still forthcoming** (no
  `book/src/L1-L0/eliminate-rhs-mutation-rotation.md` exists; referenced in plain text per the
  missing-anchor convention in both the L4 cap §"Lowers to" and the L4>L3 theme). The RHS-side L1→L0
  half is not yet authored; the L4>L3 theme this dispatch lands carries only the L4→L3 half. An
  abstractor/lifter pass should author the L1>L0 RHS-side rotation (the operator-side L1>L0 half is the
  existing `fe-operator-assemble-mutation-rotation`). Not in scope this dispatch.
- **Intro refresh** (layer-intro-author's domain, noted not actioned): `L4/index.md` §Vocabulary-cohort
  firm-count narration ("Firm at L4 (19 + 4 outer-driver)") should increment for the new `eliminate_bc`
  chapter; the §"Cycle-068 (batch-21)" narrative block could gain a cycle-101 BC-application-half entry.
  I added the dep-map row + the L4>L3 tally I own; the prose firm-count + the cohort-bullet sub-list
  narration are the layer-intro-author's to refresh (flagged, not edited — out of harvester scope).
- **`L4/index.md:48,:100` re-read clean** — both parentheticals were corrected c100 (essential_dofs NOT
  a fe_assemble input; feeds the post-assembly BC cohort). The only residual was the "L4 disposition
  open — OQ ..." pointer at `:100`, now updated by the dep-map row edit to reflect the firm `eliminate_bc`
  cap. No other stale `essential_dofs`-as-fe_assemble-input site found in `L4/index.md`.
