---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: firm
lowers: L1/fe_assemble, L1/eliminate_essential_bc, L1/eliminate_rhs
l0_anchor: palace/fem/bilinearform.{hpp,cpp}, palace/fem/libceed/operator.cpp, palace/models/laplaceoperator.cpp, palace/linalg/rap.cpp
justification_kind: structural
---

# fe-operator-assemble-mutation-rotation

The rewrite that takes a pure "assemble a global FE operator from a list of weak-form terms" form into
Palace's build-up-then-assemble C++ machinery, plus the two separable BC-elimination post-compositions.
FE assembly is the MFEM-equivalent assembly sub-spine (in scope per CLAUDE.md mesh/FE). The three LHS
operators are firm — [`fe_assemble`](../L1/fe_assemble.md),
[`eliminate_essential_bc`](../L1/eliminate_essential_bc.md), [`eliminate_rhs`](../L1/eliminate_rhs.md)
— and the libCEED leaf-kernel boundary is settled as
[`opaque-library-ownership`](./fe-assemble-libceed-boundary-obstruction.md). The opaque leaf does
**not** gate the theme's firmness: the firm `fe_assemble` fold quantifies over `A(term_i)` opaquely,
exactly as `ksp_solve` stays firm while its inner MINRES/BiCGStab Krylov kernels are
obstruction-documented (a firm outer form over an obstruction-tier inner leaf; see §"libCEED
boundary"). The `weak_form_term` type stays a deferred rough-in input the assembly fold quantifies over
**opaquely** (the fold never cracks open a term's `(coefficient, differential-operator)` internals);
enumerating the full term cohort across the 5 solver pipelines is follow-on width work.

**The `eliminate_rhs` L1>L0 leg FOLDS here — no dedicated `eliminate-rhs-mutation-rotation` sibling
theme.** The RHS-side BC-elimination rotation is the same FE-BC-elimination rotation as its
operator-side partner `eliminate_essential_bc`, on the same L0 witness
(`GetExcitationVector`/`GetStiffnessMatrix`) and the same L0 file (`palace/linalg/rap.cpp`); it is
narrated as **step 5** of the L0-form protocol below and is folded here exactly as the operator-side
leg is. A dedicated sibling theme would be a degenerate identity-in-named-terms split (anti-mirror
smell, CLAUDE.md §VOCABULARY-SHIFT REDIRECT). The anchor for cross-references is §"The `eliminate_rhs`
leg (folded here)" below.

## L1 form (LHS)

The LHS is the firm L1 operator [`fe_assemble`](../L1/fe_assemble.md). It
consumes a finite-element space — the firm [`fe_space`](../L1/fe_space.md) value
`fe_space(mesh, collection) :: FiniteElementSpace[N]` (the substrate that *defines* the true-dof axis
`N`) — and an **immutable list of weak-form terms** (each term a
`(coefficient, differential-operator)` pair naming a bilinear weak-form contribution `a_i(u, v)`),
and produces a fresh global linear operator. Nothing is mutated; there is no container built up in
place, no sub-operator accumulator, no finalize step.

    K = fe_assemble(space, [term_0, term_1, ...])
        -- K :: LinearOperator[N, N]   (N = space.GetTrueVSize())
        -- term_i :: WeakFormTerm       (a coefficient-weighted differential bilinear form)
        -- the assembled operator's action is  K = Σ_i A(term_i)
        --   where A(·) is the element-local→global assembly of one weak-form term

The shared-spine reading is a **fold over the term list**: the global operator is the sum of the
per-term assembled contributions. For the electrostatic witness the single term is the
permittivity-weighted diffusion form `a(u, v) = (ε ∇u, ∇v)`; the L1 form is
`fe_assemble(h1_space, [diffusion(ε)])`.

The BC-elimination is a **separable post-composition**, not part of the assembly fold. Both
legs are now firm L1 operators (signatures authoritative in their entries):

    K_bc = eliminate_essential_bc(K, dbc_dofs, DIAG_ONE)
        -- pin the rows/cols of the essential (Dirichlet) dofs; place 1 on the diagonal

    RHS = eliminate_rhs(K, x_bc, b, policy)
        -- lift the inhomogeneous Dirichlet data into the RHS:
        --   b' := b - K·(BC-extended x_bc), then pin the essential rows per policy

All three pieces are **firm**: [`fe_assemble`](../L1/fe_assemble.md) (the assembly fold),
[`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) (the operator-side essential-dof pin), and
[`eliminate_rhs`](../L1/eliminate_rhs.md) (the inhomogeneous-Dirichlet RHS lift). Their signatures are
authoritative there; this theme narrates how each lowers into Palace's L0 imperative protocol.

## L0 form (RHS)

The Palace L0 form is an imperative **build-up-then-assemble** object protocol. For the
electrostatic witness (`palace/models/laplaceoperator.cpp:184-223`):

1. **Construct an empty form container** over the trial/test space:
   `BilinearForm k(GetH1Space());` (`bilinearform.cpp` ctor; the single-space ctor delegates
   trial = test, `palace/fem/bilinearform.hpp:48`).

2. **Push weak-form terms onto an owned list** by templated append:
   `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func);`
   (`palace/fem/bilinearform.hpp:53-57` — `make_unique<T>` then `push_back` onto `domain_integs`).
   This is the imperative form of building the term list; multiple `AddDomainIntegrator` /
   `AddBoundaryIntegrator` calls accumulate the list before any assembly runs.

3. **Assemble** — `k.Assemble(GetH1Spaces(), skip_zeros)`. The public dispatch
   (`palace/fem/bilinearform.cpp:141-151`) picks **partial** (matrix-free libCEED `ceed::Operator`)
   vs. **full** (assembled `HypreCSRMatrix`) by polynomial order via the anonymous-namespace
   `UseFullAssembly` helper. The assembly core `PartialAssemble`
   (`palace/fem/bilinearform.cpp:28-107`) is the **integrator-fold**: over each mesh geometry, for
   each integrator in `domain_integs` (and `boundary_integs` at dimension−1), call
   `integ->Assemble(...)` to build a libCEED sub-operator and `op->AddSubOperator(sub_op)` to
   accumulate it into the composite operator (`palace/fem/bilinearform.cpp:77` domain branch;
   `:97` boundary branch), then `op->Finalize()` (`:104`). `FullAssemble`
   (`palace/fem/bilinearform.cpp:109-113`) forwards to `ceed::CeedOperatorFullAssemble`
   (`palace/fem/libceed/operator.cpp:455-490`), which assembles each sub-operator in COO format
   (`CeedOperatorAssembleCOO`) and converts to CSR — the **libCEED boundary**.

4. **Wrap + attach essential dofs** per multigrid level:
   `ParOperator K_l(std::move(k_vec[l]), h1_fespace_l);`
   `K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], DiagonalPolicy::DIAG_ONE);`
   (`palace/models/laplaceoperator.cpp:215-217`). This is the L0 realization of
   `eliminate_essential_bc`.

5. **BC-elimination into the RHS** (`GetExcitationVector`,
   `palace/models/laplaceoperator.cpp:225-252`): project the Dirichlet boundary values into a
   grid function (`x.ProjectBdrCoefficient(one, source_marker)`, `:238`), restrict to true dofs
   (`x.ParallelProject(X)`, `:247`), then `PtAP_K->EliminateRHS(X, RHS)` (`:252`). The elimination
   body (`palace/linalg/rap.cpp:56-82`) computes `RHS := RHS − A·(prolongated BC-extended x)` then
   restores the pinned dof entries — the L0 realization of the firm
   [`eliminate_rhs`](../L1/eliminate_rhs.md).

## Applicability conditions

- The L1 `fe_assemble` form is valid when the global operator is **the sum of element-local
  weak-form contributions** with no inter-element coupling beyond the shared-dof assembly (the
  standard conforming-FE assembly model). This holds for all of Palace's `AddDomainIntegrator` /
  `AddBoundaryIntegrator` terms (each is a per-element quadrature contribution).
- **PA/FA is a variant axis, absorbed at L1** (`book/src/L0/fem-bilinearform-file.md` §"The PA/FA
  dual collapses at L1"): partial and full assembly compute the same operator *action*; the L1
  form is representation-agnostic. The `pa_order_threshold` dispatch is a performance selector, not
  an algebraic distinction.
- **BC-elimination is separable**: `eliminate_essential_bc` / `eliminate_rhs` are post-compositions
  on the assembled operator, valid independently of how the operator was assembled.
- **Single-rank reading**: the OMP-parallel composite build
  (`palace/fem/bilinearform.cpp:51-101` — `PalacePragmaOmp(parallel ...)`, one `Ceed` per thread)
  is a transparent CPU-threading trick that collapses at L1; `ParOperator` / `HypreParMatrix` are
  read single-rank (per `book/src/L0/par-types-single-rank-reading.md`). The MPI `GlobalSum` over
  NNZ in the print path is diagnostic-only.

## Justification kind

**Structural** — the rewrite is shape-driven: it recognizes the build-up-then-assemble object
protocol as a fold over an immutable term list plus separable BC post-compositions, and the
matrix-materialization as the fold's action. (The libCEED boundary is the one non-structural seam;
it is settled as `obstruction (opaque-library-ownership)` — see
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) and
§"libCEED boundary".)

## libCEED boundary

`FullAssemble`'s actual matrix materialization lives in `ceed::CeedOperatorFullAssemble`
(`palace/fem/libceed/operator.cpp:455-490`), which calls libCEED's `CeedOperatorAssembleCOO` to get
the operator in COO format and converts to CSR. The **element-local quadrature kernels** (the
per-integrator `integ->Assemble(...)` that builds each `CeedOperator` sub-operator,
`palace/fem/bilinearform.cpp:75-76`) bottom out in libCEED basis-apply + restriction operations.
This is **upstream library behavior** (libCEED), cited at Palace's call boundary but not itself
Palace source. The libCEED leaf is settled as `obstruction (opaque-library-ownership)`: see the
sibling annotation
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
(deeper-boundary sibling of `triangular-solve-obstruction`). The
opaque leaf sits **strictly below** the firm `fe_assemble` fold — the fold quantifies over
`A(term_i)` opaquely — so the boundary does NOT downgrade the fold or gate this theme's firmness
(the `ksp_solve` / inner-Krylov-kernel structural relationship).

## Vocabulary status

All three L1 operators this theme lowers are **firm** — no speculative LHS remains:

- [`fe_assemble`](../L1/fe_assemble.md) — the assembly fold `K = Σ_i A(term_i)`.
- [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) — operator-side essential-dof pin.
- [`eliminate_rhs`](../L1/eliminate_rhs.md) — inhomogeneous-Dirichlet RHS lift.

One deferred rough-in **input** remains (it does NOT gate this theme — the fold quantifies over it
opaquely):

- `weak_form_term` (type) — the `(coefficient, differential-operator)` weak-form contribution; the
  element type of the term list `fe_assemble` folds over (diffusion / mass / curl-curl / div-div /
  ... — the term cohort is only partially witnessed by this electrostatic probe). Enumerating the
  full cohort across the 5 solver pipelines is follow-on width work tracked in the OQ ledger.

## Evidence

The L0 witnesses are cited inline in the §L0 form and §"The `eliminate_rhs` leg" sections. Two
additional surface anchors:

- `palace/fem/bilinearform.hpp:25-91` — `class BilinearForm`: the integrator-list container + the
  templated `AddDomainIntegrator` / `AddBoundaryIntegrator` append surface (`:53-63`).
- `palace/fem/integrator.hpp:39-130` — `BilinearFormIntegrator` interface + concrete weak-form
  terms (`MassIntegrator`, `DiffusionIntegrator`, `CurlCurlIntegrator`, `DivDivIntegrator`, ...).
- `book/src/L0/fem-bilinearform-file.md` — the L0 navigation naming the integrator-fold insight
  (§"Notes for higher layers": "BilinearForm is fundamentally a fold over integrators").

## What lifts cleanly vs. what needs new vocabulary

**Lifts cleanly** (existing spine vocabulary suffices):
- The integrator-fold → an L2 `fold`/`sum` over a term list. The "sum of weak-form terms" algebra is
  exactly the `linear_combination` / fold shape already present at L2/L3.
- The PA/FA dual → a variant axis (matrix-free vs. sparse representation of the same operator action).
- BC-elimination → a separable post-composition; `eliminate_rhs`'s body is an `apply_linop` + `axpy`
  composition over the assembled operator (`RHS −= A·x_bc`), already firm spine vocabulary.

**Needs new vocabulary** (findings about the spine):
- The **weak-form term** itself — `(coefficient, differential-operator)` — has no spine vocabulary
  yet. The differential operators (∇ for diffusion, curl for curl-curl, div for div-div, identity
  for mass) are the FE-specific primitives. This is the core new vocabulary the FE-assembly
  sub-spine introduces.
- The **element-local→global assembly** map `A(·)` — how a per-element quadrature contribution
  becomes a global-dof operator (the libCEED restriction + basis-apply). This is the libCEED
  boundary; whether it gets re-expressed as a tensor contraction or stays library-owned is the
  thread's central open decision.
- The **FE space** itself (`FiniteElementSpace`) — the dof-numbering / mesh-topology object — now
  has its firm L1 home [`fe_space`](../L1/fe_space.md) (the `(mesh, collection) →
  FiniteElementSpace[N]` construction that defines the true-dof axis `N` every `[N]`-indexed operand
  shares), lowering to L0 via the `fe-space-construction-rotation` L1>L0 theme. The dof-numbering /
  ordering / conformity internals stay MFEM-owned-read-as-given (see `fe_space` §"MFEM-owned");
  `book/src/L0/fespace-file.md` is the L0 localization.

## The `eliminate_rhs` leg (folded here)

This section is the explicit home of the `eliminate_rhs` L1>L0 lowering (the target of the
cross-references from [`eliminate_rhs`](../L1/eliminate_rhs.md), [`eliminate_bc`](../L4/eliminate_bc.md),
and [`bc-elimination-post-composition-dissolution`](../L4-L3/bc-elimination-post-composition-dissolution.md)).
There is **no** separate `eliminate-rhs-mutation-rotation.md` theme — the rotation lives here.

**L1 form (LHS).** [`eliminate_rhs`](../L1/eliminate_rhs.md) `(K, x_bc, b, policy)` — the
mutation-free inhomogeneous-Dirichlet lift `b' = b − K·x_bc` with essential rows pinned per diagonal
policy; a separable post-composition on the assembled `K` (signature authoritative in the L1 entry).

**L0 form (RHS).** `ParOperator::EliminateRHS` (`palace/linalg/rap.cpp:56-82`), reached from the
electrostatic witness `LaplaceOperator::GetExcitationVector` at `:252`
(`palace/models/laplaceoperator.cpp:252`). The in-place RHS-mutation protocol the L1 form lowers
into, line-by-line:

- **Gather the essential boundary values onto pooled true-dof scratch** — `tx = 0.0` then
  `linalg::SetSubVector(tx, dbc_tdof_list, x)` (`palace/linalg/rap.cpp:62-63`): scatter the Dirichlet
  data `x` (= `x_bc`) into a zeroed true-dof vector.
- **Prolong to the local (l-)vector** — `trial_fespace.GetProlongationMatrix()->Mult(tx, lx)`
  (`palace/linalg/rap.cpp:64`): the true→local prolongation `P·x_bc`.
- **Apply the unconstrained local operator** — `A->Mult(lx, ly)` (`palace/linalg/rap.cpp:69`): the
  local-matrix action `A·(P·x_bc)` (the single `apply_linop` of the L1 form, realized as the
  prolong/local-apply/restrict round-trip).
- **Restrict back to true dofs** — `RestrictionMatrixMult(ly, ty)` (`palace/linalg/rap.cpp:72`):
  `ty = Rᵀ·(A·P·x_bc)`, i.e. the assembled `K·x_bc` in true-dof space.
- **In-place RHS subtraction** — `b.Add(-1.0, ty)` (`palace/linalg/rap.cpp:73`): the in-place
  realization of `b' = b − K·x_bc` (the L1 `axpy`).
- **In-place essential-row pin per diagonal policy** — `DIAG_ONE` →
  `linalg::SetSubVector(b, dbc_tdof_list, x)` (`palace/linalg/rap.cpp:76`, pin essential rows to the
  boundary data); `DIAG_ZERO` → `linalg::SetSubVector(b, dbc_tdof_list, 0.0)`
  (`palace/linalg/rap.cpp:80`, pin to zero). This is the `policy`-selected essential-row overwrite of
  the L1 form (the non-law that makes `eliminate_rhs` not linear-in-`b`-as-a-whole).

**The mutation rotation.** The L0 form mutates the caller's `b` in place (`b.Add`, `SetSubVector`
both write `b`) using a pooled-scratch round-trip (`tx`/`lx`/`ly`/`ty` are reused per-solver buffers,
not fresh allocations — the transparent pooling trick). The L1 `eliminate_rhs` is the pure-function
rotation: it consumes `(K, x_bc, b, policy)` and returns a fresh `b'`, with the
prolong/apply/restrict round-trip absorbed into the single `K·x_bc` operator action and the in-place
`b.Add` + `SetSubVector` absorbed into the value-returning `b − K·x_bc` + pin. This is the same
in-place-vector → pure-function rotation as the operator-side leg, on the same witness — hence the
fold.

**Justification:** structural (shape-driven, the same as the parent theme) — read directly off the
positive `EliminateRHS` body, not constructed.
