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

# eliminate_bc

The L4 **post-assembly boundary-condition application surface**: the pair of separable
post-compositions that pin essential (Dirichlet) dofs into an assembled operator and lift the
inhomogeneous Dirichlet data into the right-hand side. Two co-equal verbs over the same
`(DofSet[N], DiagPolicy)` vocabulary:

- `eliminate_essential_bc` — the **operator-side** pin: `LinOp[(S: ...), $S] -> LinOp[$S, $S]`,
  zero the essential rows/cols of `K` and set the eliminated diagonal per policy.
- `eliminate_rhs` — the **RHS-side** lift: `... -> Tensor[$S]`, subtract the boundary-data forcing
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

```text
-- operator-side: pin the essential dofs into the assembled square operator
eliminate_essential_bc :: LinOp[(S: ...), $S] -> DofSet[N] -> DiagPolicy
                          -> LinOp[$S, $S]

-- RHS-side: lift the inhomogeneous Dirichlet data into the right-hand side
eliminate_rhs :: LinOp[(S: ...), $S] -> Tensor[$S] -> Tensor[$S] -> DiagPolicy
                 -> Tensor[$S]
eliminate_rhs K x_bc b policy =
  let y    = apply_linop K (restrict_essential x_bc)          -- K · Eₑ(x_bc)
      b'   = linear_combination [(1, b), (-1, y)]             -- b − K·x_bc
      pin  = case policy of DIAG_ONE -> x_bc ; DIAG_ZERO -> zeros
  in  set_essential b' pin                                    -- BC rows ← pin
```

Shape contract (named shape groups / operator shapes per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; the system operator is square, so domain and range are one shape group `S` and the BC-side vectors are congruent to it; the essential-dof index set keeps its genuine flat-index spelling; the BC stratum per [`state-stratification`](../concepts/state-stratification.md)):

- `K` — `LinOp[(S: ...), $S]` — the assembled **square** operator over the true-dof shape group `S`, the
  output of [`fe_assemble`](./fe_assemble.md). `readonly`; squareness is required (BC elimination is
  defined only when domain group ≡ range group, i.e. `height == width`; the rectangular case is a hard L0 reject — the
  `trial-test-coincidence` variant axis). The operator-side result decomposes block-wise on the
  free/essential partition `F = 0..N \ E`, `E = dofs` (a partition of the flat true-dof index set `0..N` underlying `S`):

      eliminate_essential_bc K E policy =
        [ K[F,F]   0   ]      D = I_E   (policy = DIAG_ONE)
        [ 0        D   ]      D = 0_E   (policy = DIAG_ZERO)

- `dofs : DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` (a **genuine
  index set** over the flat true-dof index space underlying `S`, NOT a tensor shape — kept in its
  flat-index spelling); the
  `DofSet[N]` produced by [`essential_dofs`](../L1/essential_dofs.md) (the firm boundary-attribute →
  essential-true-dof construction). Part of the `readonly` BC stratum captured at construction.
- `policy : DiagPolicy` — `DIAG_ONE | DIAG_ZERO` (the diagonal-policy variant axis). The only two
  admissible values; MFEM's third policy `DIAG_KEEP` is out-of-axis (excluded at the `ParOperator`
  boundary).
- `x_bc : Tensor[(S: ...)]` — (RHS-side only) the essential boundary data; a vector congruent to the operator's shape group `S` prescribing the
  Dirichlet value on essential dofs, masked-out elsewhere. Only the essential entries are read
  (`restrict_essential`). `readonly`.
- `b : Tensor[(S: ...)]` — (RHS-side only) the right-hand-side vector to adjust, congruent to `S`. `readonly` at L4 (the L4 form
  returns a fresh value; the in-place `b.Add` is an L3-and-below concern).
- result — operator-side `LinOp[(S: ...), $S]` (the eliminated operator); RHS-side `Tensor[$S]` (the
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
`concepts/<record>.md` page, not an in-chapter section). That cross-cutting home is the concept page
[`DofSet`](../concepts/dofset.md) (`book/src/concepts/dofset.md`, `rank: firm`), which defines the
record schema — the `indices : Set<TrueDofIndex>` field, its construction-time readonly stratum, and
its L0 backing. See that page for the full record definition; the working description here:
`DofSet[N]` is an immutable index set over the
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
  blocking fold dependency: `eliminate_bc` consumes `K` as an opaque assembled `LinOp[(S: ...), $S]`,
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

**Strawman reference**: `book/src/semantics/index.md` §3.5 (operator application, `:138-145`) is the
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
high→low discipline; it does **not** author the theme. The L1>L0 mutation rotation
(`fe-operator-assemble-mutation-rotation` for the operator pin, and the `eliminate_rhs` leg folded
into that same theme — §"The `eliminate_rhs` leg (folded here)" — for the RHS lift; there is no
separate `eliminate-rhs-mutation-rotation` theme, disposition FOLD c103) carries the L1→L0 half;
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
`LinOp[(S: ...), $S]` vs RHS-side `Tensor[$S]` — homed as a co-equal PAIR, not merged into one
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
