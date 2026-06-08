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

# eliminate_essential_bc

Pin the essential (Dirichlet) true dofs into an assembled square operator: produce a fresh operator
in which the rows and columns at the essential-dof set are zeroed and each eliminated diagonal entry
is set per a **diagonal policy** (`DIAG_ONE` / `DIAG_ZERO`). A **separable post-composition** on the
assembled operator — it composes AFTER [`fe_assemble`](./fe_assemble.md) and is NOT part of the
assembly fold. The pure-functional lift of Palace's `ParOperator` essential-BC elimination
(`SetEssentialTrueDofs` recording the dof-set + policy; `mfem::HypreParMatrix::EliminateBC` applying
it on the assembled square matrix).

## Context

`eliminate_essential_bc` lifts the BC-elimination step that Palace applies to an assembled operator
**after** the FE-assembly fold. In Palace the elimination is split across two L0 sites that together
realize one L1 operation:

- `ParOperator::SetEssentialTrueDofs(tdof_list, policy)` (`palace/linalg/rap.cpp:36-47`) records the
  essential-true-dof list and the diagonal policy on the operator wrapper (it verifies the operator
  is square — `height == width` — and that the policy is one of `DIAG_ONE` / `DIAG_ZERO`). It is a
  *deferred* configuration: it stores the dof-set + policy but does not yet alter the matrix.
- `RAP->EliminateBC(dbc_tdof_list, diag_policy)` (`palace/linalg/rap.cpp:141-143`) applies the
  recorded elimination on the assembled (square) `HypreParMatrix` at parallel-assemble time: it
  zeros the rows and columns at `dbc_tdof_list` and sets each eliminated diagonal per `diag_policy`.

At L1 these two L0 sites collapse into a single pure operation `eliminate_essential_bc(K, dofs,
policy)` that consumes the assembled operator and produces the eliminated operator value. The
deferred-config / apply-at-assemble-time split, the `ParOperator` wrapper state, and the
square-operator `MFEM_VERIFY` guards are L0 concerns reintroduced by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 lowering theme, not by the L1 signature.

The witness is the electrostatic stiffness build: `LaplaceOperator::GetStiffnessMatrix`
(`palace/models/laplaceoperator.cpp:184-219`) assembles the diffusion operator via `fe_assemble`,
wraps each multigrid level in a `ParOperator`, and calls
`SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE)`
(`palace/models/laplaceoperator.cpp:216-217`) — the separable `eliminate_essential_bc` post-comp on
the freshly-assembled `K`. The eigen pipeline applies the same elimination on its assembled real /
imaginary stiffness and mass blocks (`palace/models/modeeigensolver.cpp:571,574,608,611`).

## Signature

```text
eliminate_essential_bc :: (K: LinearOperator[N, N], dofs: DofSet[N], policy: DiagPolicy)
                          -> LinearOperator[N, N]
```

Shape contract (bunsen-style, named axes):

- `K` — `LinearOperator[N, N]` — an assembled **square** operator over the true-dof axis `N`
  (`N = space.GetTrueVSize()`, `palace/fem/fespace.hpp:96`); the output of
  [`fe_assemble`](./fe_assemble.md). The axis `N` is defined by the finite-element space
  [`fe_space`](./fe_space.md) constructs. Read-only; squareness is required (essential-BC elimination
  is defined only for `height == width` — the L0 guard `palace/linalg/rap.cpp:42-43`, and the
  rectangular-reject branch `palace/linalg/rap.cpp:145-148`).
- `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` over the
  true-dof axis [`fe_space`](./fe_space.md) defines; the `DofSet[N]` constructed by
  [`essential_dofs`](./essential_dofs.md) (the firm `(space, bdr_attrs, bdr_attr_max) → DofSet[N]`
  boundary-attribute → essential-true-dof-set construction). At L0 the `mfem::Array<int> dbc_tdof_list`
  recorded by `SetEssentialTrueDofs` (`palace/linalg/rap.cpp:45-46`).
- `policy` — `DiagPolicy` — `DIAG_ONE | DIAG_ZERO` (the diagonal-policy variant axis; see
  *Variant axes*). The only two admissible values (L0 guard `palace/linalg/rap.cpp:39-41`).
- result — `LinearOperator[N, N]` — a fresh square operator equal to `K` with rows and columns at
  `dofs` zeroed and the eliminated diagonal set per `policy`.

The result operator's action decomposes block-wise on the free/essential dof partition. Writing
`F = 0..N \ dofs` (free dofs) and `E = dofs` (essential dofs):

```text
eliminate_essential_bc(K, E, policy) =
  [ K[F,F]   0      ]
  [ 0        D       ]   where   D = I_E   (policy = DIAG_ONE)
                                D = 0_E   (policy = DIAG_ZERO)
```

i.e. the off-diagonal coupling blocks `K[F,E]` and `K[E,F]` are zeroed, the free–free block `K[F,F]`
is preserved, and the essential–essential block becomes the identity (`DIAG_ONE`) or zero
(`DIAG_ZERO`) on `E`.

## Semantics

`eliminate_essential_bc(K, E, policy)` returns the operator obtained from `K` by **decoupling the
essential dofs**: every matrix entry in an essential row or essential column is set to zero, then
each essential diagonal entry `(i, i)` for `i ∈ E` is set to `1` (`DIAG_ONE`) or left `0`
(`DIAG_ZERO`). Free–free entries `K[i,j]` with `i, j ∉ E` are unchanged.

The operation is **separable from assembly**: it is defined purely on the operator value, the dof
set, and the policy — it does not inspect how `K` was assembled (which weak-form terms, which
representation). This is what makes it a **post-composition** rather than a fold step: for any
assembled `K = fe_assemble(space, terms)`,

```text
eliminate_essential_bc(fe_assemble(space, terms), E, policy)
```

is a well-formed composition, and the elimination commutes with the assembly fold's term-additivity
in the precise sense given by the *distribution-over-assembly* law below.

The `DIAG_ONE` policy is the **solve-side** convention: it makes the eliminated operator
non-singular on the essential block (the essential dofs become trivial `x_i = b_i` equations), so the
operator can be inverted by `ksp_solve` with the essential values supplied through the RHS (the
companion `eliminate_rhs` operator, sibling rough-in). The `DIAG_ZERO` policy is the
**energy / mass-block** convention used where the essential block must contribute no spurious unit
eigenvalues (e.g. assembling sub-blocks of a generalized eigenvalue problem — the eigen pipeline
`palace/models/modeeigensolver.cpp:571-611` uses both policies across its `A`/`B` blocks).

`eliminate_essential_bc` is **pure at L1**: there is no in-place mutation of the operator, no
deferred-config wrapper, no apply-at-assemble-time staging. The L0 `SetEssentialTrueDofs`
record-then-`EliminateBC`-apply split (`palace/linalg/rap.cpp:36-47` record;
`palace/linalg/rap.cpp:141-143` apply) and the `ParOperator` mutable wrapper are L1>L0 lowering
concerns.

## Algebraic laws

The laws below hold treating `K` as an opaque assembled square operator and `EliminateBC` as the
zero-rows-cols-then-set-diagonal map it positively is (`palace/linalg/rap.cpp:143`). Absences are
deliberate.

1. **Idempotence**: `eliminate_essential_bc(eliminate_essential_bc(K, E, policy), E, policy) =
   eliminate_essential_bc(K, E, policy)`. After elimination the essential rows/cols are already zero
   and the diagonal already equals the policy value; re-eliminating the same `(E, policy)` is the
   identity. The eliminated operator is a fixed point of the elimination with the same dof-set and
   policy.

2. **Free-block preservation**: the free–free sub-block is unchanged —
   `eliminate_essential_bc(K, E, policy)[F, F] = K[F, F]` for `F = 0..N \ E`. The elimination
   touches only essential rows and columns; the interior (free) physics is preserved exactly. This
   is what licenses solving the reduced free-dof system.

3. **Policy determines only the essential diagonal**:
   `eliminate_essential_bc(K, E, DIAG_ONE)` and `eliminate_essential_bc(K, E, DIAG_ZERO)` differ
   *only* on the essential–essential diagonal entries `(i, i), i ∈ E` (identity vs. zero on `E`);
   all other entries (free–free, and the zeroed coupling/off-diagonal-essential entries) are
   identical. The policy is a per-diagonal-entry choice on the eliminated block, nothing more.

4. **Distribution over the assembly fold (separable post-composition)**:
   `eliminate_essential_bc(K₁ + K₂, E, DIAG_ZERO) = eliminate_essential_bc(K₁, E, DIAG_ZERO) +
   eliminate_essential_bc(K₂, E, DIAG_ZERO)`. With the `DIAG_ZERO` policy the elimination is a
   **linear** map on operators (zeroing rows/cols + zero diagonal is the linear projection
   `K ↦ P_F K P_F` onto the free block, with `P_F` the diagonal 0/1 free-dof projector), so it
   distributes over operator addition — hence over the `fe_assemble` term-sum (law 2 of
   [`fe_assemble`](./fe_assemble.md)). The `DIAG_ONE` policy is the same projection **plus** the
   constant `I_E` on the essential block, an affine (not linear) map, so it distributes up to that
   constant: `eliminate_essential_bc(K₁ + K₂, E, DIAG_ONE) = eliminate_essential_bc(K₁, E, DIAG_ONE)
   + eliminate_essential_bc(K₂, E, DIAG_ZERO)` (the `I_E` is added once, not per-term). This is the
   precise sense in which the elimination is *separable* from assembly: it factors through the
   free-block projection regardless of the term decomposition.

Laws that explicitly **do not** hold:

- **Not the identity** (for non-empty `E`): elimination changes `K` whenever any essential row/col
  has a nonzero entry. The empty-dof-set case is the only identity: `eliminate_essential_bc(K, ∅,
  policy) = K`.
- **No SPD / invertibility guarantee under `DIAG_ZERO`**: `DIAG_ZERO` leaves a zero block on `E`,
  so the result is singular by construction (rank ≤ `|F|`). Only `DIAG_ONE` makes the essential
  block non-singular. `eliminate_essential_bc` carries no SPD/invertibility postcondition; that is a
  policy- and `K`-dependent property, not a law.
- **Policy-commutativity does NOT hold**: `eliminate_essential_bc(·, E, DIAG_ONE)` and
  `eliminate_essential_bc(·, E, DIAG_ZERO)` are distinct maps (law 3); there is no policy under
  which they coincide for non-empty `E`.

## Applicability

`eliminate_essential_bc` is a **separable post-composition** on an assembled **square** operator: it
composes AFTER [`fe_assemble`](./fe_assemble.md) on the assembly axis and BEFORE the linear/eigen
solve. The standard electrostatic pipeline is
`eliminate_essential_bc(fe_assemble(h1_space, [diffusion(ε)]), E, DIAG_ONE)` then `ksp_solve`
(`palace/models/laplaceoperator.cpp:184-217`). It is defined only when:

- `K` is **square** (`height == width`) — the L0 guards reject the rectangular case
  (`palace/linalg/rap.cpp:42-43` set-time; `:145-148` assemble-time
  `"Essential BC elimination is only available for square ParOperator!"`). The
  `trial-test-coincidence` variant axis records this (the witnessed case is `square`).
- `policy ∈ {DIAG_ONE, DIAG_ZERO}` — no other diagonal policy is admissible at this boundary
  (`palace/linalg/rap.cpp:39-41`); MFEM's third policy `DIAG_KEEP` is explicitly excluded by the
  `ParOperator` guard.

It is **not** part of the `fe_assemble` fold (law 2 of `fe_assemble` explicitly excludes
BC-elimination) and is independent of the assembly representation (PA/FA): the elimination acts on
the assembled square matrix's true-dof structure, which both representations share. Its sibling
post-composition is [`eliminate_rhs`](./eliminate_rhs.md) (lift inhomogeneous Dirichlet data into the
RHS, L0 `ParOperator::EliminateRHS` `palace/linalg/rap.cpp:60-83`); the two together realize the full
Dirichlet-BC application on the operator+RHS pair.

## Variant axes

- **diagonal-policy**: `DIAG_ONE` (eliminated diagonal set to `1` — the solve-side convention,
  makes the essential block trivially invertible) | `DIAG_ZERO` (eliminated diagonal left `0` — the
  energy/mass-block convention, the linear free-block projection). The L0 selector is the
  `diag_policy` member (`palace/linalg/rap.cpp:18` default `DIAG_ONE`; set by
  `SetEssentialTrueDofs` `:46`; consumed at `:143`). Both policies share the row/col-zeroing
  behavior; they differ only on the essential diagonal (law 3). The witnessed electrostatic case is
  `DIAG_ONE` (`palace/models/laplaceoperator.cpp:217`); the eigen pipeline exercises both across its
  `A`/`B` blocks (`palace/models/modeeigensolver.cpp:571-611`). MFEM's third policy `DIAG_KEEP` is
  **out of axis** — the `ParOperator` boundary admits only the two above
  (`palace/linalg/rap.cpp:39-41`).
- **trial-test-coincidence**: `square` (trial = test space — the only admissible case;
  `height == width` guard `palace/linalg/rap.cpp:42-43`) | `rectangular` (rejected —
  `palace/linalg/rap.cpp:145-148` requires `dbc_tdof_list.Size() == 0` for non-square operators).
  The signature above is the square case; the rectangular case is a hard reject at L0, not a
  variant the L1 operator carries.

## Clean post-composition

`eliminate_essential_bc`'s definition, signature, and all four algebraic laws are stated entirely in
**existing shared vocabulary** (operator block-decomposition on the free/essential dof partition; the
free-block projection `K ↦ P_F K P_F`; operator addition) treating `K` as an **opaque assembled square
operator** and the diagonal policy as a two-valued variant axis. The `EliminateBC` diagonal-policy
does **not** resist clean post-composition: the elimination is defined purely on `(K, dofs, policy)`
and does not inspect how `K` was assembled; it factors through the free-block projection regardless of
the term decomposition (law 4). The diagonal policy is a per-essential-diagonal choice (law 3) — it
does not couple to the free-block physics and does not require cracking open `K`. Defining
`eliminate_essential_bc` therefore does NOT require formalizing `fe_assemble`'s internals; the two
compose as post-composition.

This is the **firm-on-positive-structure** situation (the `apply_linop` / `fe_assemble` precedent):
the four laws are syntactic identities on the positive `EliminateBC` zero-rows-cols-then-set-diagonal
operation (`palace/linalg/rap.cpp:143`) + the recorded `(dofs, policy)`
(`palace/linalg/rap.cpp:36-47`). No dedicated unit test exercises essential-BC elimination at this
entry point, but the missing test does not gate syntactic-identity laws on fully-specified positive
source (the `eliminate`-as-block-projection structure is read, not constructed).

## L1 vs L0 distinction

- **L0**: a deferred-config-then-apply two-step on a mutable `ParOperator` wrapper.
  `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], DIAG_ONE)` (`palace/models/laplaceoperator.cpp:217`)
  records the dof-set + policy on the wrapper (`palace/linalg/rap.cpp:45-46`, mutating
  `dbc_tdof_list` and `diag_policy`); later, at `ParallelAssemble` time,
  `RAP->EliminateBC(dbc_tdof_list, diag_policy)` (`palace/linalg/rap.cpp:143`) mutates the assembled
  `HypreParMatrix` in place (zero rows/cols + set diagonal). State is threaded through the mutable
  `ParOperator` and the mutable assembled matrix.
- **L1**: a pure post-composition. `K' = eliminate_essential_bc(K, dofs, policy)`. No deferred
  config, no wrapper state, no in-place matrix mutation. The eliminated operator is the value
  `P_F K P_F (+ I_E for DIAG_ONE)`. The deferred-config split, the wrapper mutation, the assemble-
  time staging, and the square-operator guards are L1>L0 lowering concerns.

## Evidence

- `palace/linalg/rap.cpp:36-47` — `ParOperator::SetEssentialTrueDofs(tdof_list, policy)`: records
  the essential-true-dof list (`dbc_tdof_list.MakeRef(tdof_list)`, `:45`) and the diagonal policy
  (`diag_policy = policy`, `:46`); guards `policy ∈ {DIAG_ONE, DIAG_ZERO}` (`:39-41`) and squareness
  (`height == width`, `:42-43`). The deferred-config half of the L0 operation.
- `palace/linalg/rap.cpp:141-143` — `RAP->EliminateBC(dbc_tdof_list, diag_policy)`: applies the
  elimination on the assembled square `HypreParMatrix` (zero rows/cols + set diagonal per policy) —
  the apply half. Guarded by `&trial_fespace == &test_fespace` (square-only).
- `palace/linalg/rap.cpp:145-148` — the rectangular-reject branch
  (`MFEM_VERIFY(dbc_tdof_list.Size() == 0, "Essential BC elimination is only available for square
  ParOperator!")`) — the `trial-test-coincidence` variant-axis L0 anchor.
- `palace/linalg/rap.cpp:18` — `diag_policy(DiagonalPolicy::DIAG_ONE)` ctor default: the
  diagonal-policy variant-axis default value.
- `palace/linalg/rap.hpp:84` — `void SetEssentialTrueDofs(const mfem::Array<int> &tdof_list,
  DiagonalPolicy policy)` declaration ("Set essential boundary condition true dofs for square
  operators", `:82-84`).
- `palace/models/laplaceoperator.cpp:216-217` — the electrostatic witness consumer:
  `auto K_l = std::make_unique<ParOperator>(std::move(k_vec[l]), h1_fespace_l)` (`:216`) +
  `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE)` (`:217`) — the
  separable `eliminate_essential_bc(K, E, DIAG_ONE)` post-comp on each multigrid-level stiffness
  operator.
- `palace/models/laplaceoperator.cpp:184-219` — `LaplaceOperator::GetStiffnessMatrix`: the full
  witness — `fe_assemble` the diffusion operator, per-level `ParOperator` wrap, essential-BC
  elimination. The `eliminate_essential_bc ∘ fe_assemble` pipeline.
- `palace/models/modeeigensolver.cpp:571,574,608,611` — the eigen-pipeline consumers:
  `Ar->EliminateBC` / `Ai->EliminateBC` (real/imag stiffness blocks) + `Br->EliminateBC` /
  `Bi->EliminateBC` (real/imag mass blocks) — additional witnesses exercising both diagonal
  policies across the generalized-EVP `A`/`B` blocks.
- `book/src/L1/fe_assemble.md` — the sibling firm operator; §"Algebraic laws" law 5
  explicitly names BC-elimination (`eliminate_essential_bc`) as a separable post-composition NOT
  part of the assembly fold — the upstream framing this entry realizes.

## Downward to L0

The lowering is folded into the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 theme, which narrates the FE-assembly sub-spine's build-up-then-assemble protocol and the
separable BC-elimination post-compositions: how this L1 pure post-composition lowers into Palace's
deferred-config-then-apply two-step (record `(dofs, policy)` on the `ParOperator` wrapper via
`SetEssentialTrueDofs`, then mutate the assembled `HypreParMatrix` in place via `EliminateBC` at
parallel-assemble time), plus the square-operator guards and the rectangular reject.
