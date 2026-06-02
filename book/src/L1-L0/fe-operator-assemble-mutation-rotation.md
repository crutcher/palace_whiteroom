---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: firm
lowers: L1/fe_assemble (firm c054), L1/eliminate_essential_bc (firm c055), L1/eliminate_rhs (firm c055)
l0_anchor: palace/fem/bilinearform.{hpp,cpp}, palace/fem/libceed/operator.cpp, palace/models/laplaceoperator.cpp, palace/linalg/rap.cpp
justification_kind: structural
---

# fe-operator-assemble-mutation-rotation

**FIRM (promoted cycle-057, lifter D2; opened cycle-053, abstractor D3).** The rewrite that
takes a pure "assemble a global FE operator from a list of weak-form terms" form into Palace's
build-up-then-assemble C++ machinery, plus the two separable BC-elimination post-compositions. FE
assembly is the MFEM-equivalent assembly sub-spine (in scope per CLAUDE.md mesh/FE). Opened as a
thread-opener mapping the surface; promoted to `firm` once all three LHS operators landed firm
([`fe_assemble`](../L1/fe_assemble.md) c054, [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
+ [`eliminate_rhs`](../L1/eliminate_rhs.md) c055) and the libCEED leaf-kernel boundary was settled as
[`opaque-library-ownership`](./fe-assemble-libceed-boundary-obstruction.md) (c055).

## Status

`firm`. **Clean-gate call: PROMOTE — clean.** The three gates that held this theme `rough-in` at
authoring time are all closed:

- **(a) all three LHS operators are firm** — [`fe_assemble`](../L1/fe_assemble.md) (c054, the
  integrator-fold `K = Σ_i A(term_i)`), [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md)
  (c055, the operator-side essential-dof pin), and [`eliminate_rhs`](../L1/eliminate_rhs.md) (c055,
  the inhomogeneous-Dirichlet RHS lift). The two elimination legs are no longer rough-in
  placeholders; they are firm separable post-compositions.
- **(b) the libCEED boundary is settled** — the per-term leaf `A(·)` is documented as
  [`obstruction (opaque-library-ownership)`](./fe-assemble-libceed-boundary-obstruction.md) (c055).
  The opaque leaf does **not** gate the theme's firmness: the firm `fe_assemble` fold quantifies
  over `A(term_i)` opaquely, exactly as `ksp_solve` stays firm while its inner MINRES/BiCGStab
  Krylov kernels are obstruction-documented (the same structural relationship — a firm
  outer form over an obstruction-tier inner leaf; see §"libCEED boundary").
- **(c) the term-cohort enumeration does not gate this theme** — the `weak_form_term` type stays a
  deferred rough-in input the assembly fold quantifies over **opaquely** (the fold never cracks open
  a term's `(coefficient, differential-operator)` internals; see `fe_assemble` §Status clean-gate).
  Enumerating the full term cohort across the 5 solver pipelines is follow-on width work, not a
  firmness gate on the rotation theme.

The rewrite's structural decomposition (build-up-then-assemble object protocol → integrator-fold +
PA/FA variant axis + separable BC-elimination post-compositions) is recognized and exhaustively
L0-anchored; the rotation is fully cited (the accumulation `AddSubOperator`
`palace/fem/bilinearform.cpp:77`/`:97` + `Finalize` `:104`, the BC legs
`palace/linalg/rap.cpp:56-82` + `palace/models/laplaceoperator.cpp:216-217`/`:252`). This is the
**firm-on-positive-structure** situation inherited from the three firm LHS operators: each leg's L0
form is read, not constructed.

## L1 form (LHS)

The LHS is the now-firm L1 operator [`fe_assemble`](../L1/fe_assemble.md) (landed cycle-054). It
consumes a finite-element space and an **immutable list of weak-form terms** (each term a
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

All three pieces are **firm**: [`fe_assemble`](../L1/fe_assemble.md) (c054, the assembly fold),
[`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) (c055, the operator-side essential-dof
pin), and [`eliminate_rhs`](../L1/eliminate_rhs.md) (c055, the inhomogeneous-Dirichlet RHS lift).
Their signatures are authoritative there; this theme narrates how each lowers into Palace's L0
imperative protocol.

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
Palace source. The classification OQ logged by the thread-opener — (a) transitive-firm leaf,
(b) `obstruction (opaque-library-ownership)`, or (c) tensor-contraction respine — was **settled as
(b)** by the batch-16 meta-phase: see the sibling annotation
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md)
(c055, opaque-library-ownership, deeper-boundary sibling of `triangular-solve-obstruction`). The
opaque leaf sits **strictly below** the firm `fe_assemble` fold — the fold quantifies over
`A(term_i)` opaquely — so the boundary does NOT downgrade the fold or gate this theme's firmness
(the `ksp_solve` / inner-Krylov-kernel structural relationship).

## Vocabulary status (all LHS operators promoted)

All three L1 operators this theme lowers are now **firm** — no speculative LHS remains:

- [`fe_assemble`](../L1/fe_assemble.md) — **firm c054** (the assembly fold `K = Σ_i A(term_i)`).
- [`eliminate_essential_bc`](../L1/eliminate_essential_bc.md) — **firm c055** (operator-side
  essential-dof pin).
- [`eliminate_rhs`](../L1/eliminate_rhs.md) — **firm c055** (inhomogeneous-Dirichlet RHS lift).

One deferred rough-in **input** remains (it does NOT gate this theme — the fold quantifies over it
opaquely, per §Status (c)):

- `weak_form_term` (type) — the `(coefficient, differential-operator)` weak-form contribution; the
  element type of the term list `fe_assemble` folds over (diffusion / mass / curl-curl / div-div /
  ... — the term cohort is only partially witnessed by this electrostatic probe). Enumerating the
  full cohort across the 5 solver pipelines is follow-on width work tracked in the OQ ledger.

## Verified-against

- `palace/models/laplaceoperator.cpp:184-223` — `GetStiffnessMatrix`: the build-up-then-assemble
  witness (BilinearForm ctor + `AddDomainIntegrator<DiffusionIntegrator>` + `Assemble` + per-level
  `ParOperator` wrap with `SetEssentialTrueDofs`).
- `palace/models/laplaceoperator.cpp:225-252` — `GetExcitationVector`: the BC-elimination witness
  (`ProjectBdrCoefficient` `:238` + `ParallelProject` `:247` + `EliminateRHS` `:252`).
- `palace/fem/bilinearform.hpp:25-91` — `class BilinearForm`: the integrator-list container + the
  templated `AddDomainIntegrator` / `AddBoundaryIntegrator` append surface (`:53-63`).
- `palace/fem/bilinearform.cpp:28-107` — `PartialAssemble`: the integrator-fold core
  (`AddSubOperator` accumulation at `:77` domain / `:97` boundary; `Finalize` at `:104`).
- `palace/fem/bilinearform.cpp:141-151` — `Assemble(bool)`: the PA/FA policy dispatch.
- `palace/fem/integrator.hpp:39-130` — `BilinearFormIntegrator` interface + concrete weak-form
  terms (`MassIntegrator`, `DiffusionIntegrator`, `CurlCurlIntegrator`, `DivDivIntegrator`, ...).
- `palace/fem/libceed/operator.cpp:455-490` — `CeedOperatorFullAssemble`: COO→CSR materialization
  (the libCEED boundary).
- `palace/linalg/rap.cpp:56-82` — `ParOperator::EliminateRHS`: the `eliminate_rhs` L0 realization.
- `book/src/L0/fem-bilinearform-file.md` — firm L0 navigation already naming the integrator-fold
  insight (§"Notes for higher layers": "BilinearForm is fundamentally a fold over integrators").

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
- The **FE space** itself (`FiniteElementSpace`) — the dof-numbering / mesh-topology object — is a
  whole sub-thread (`book/src/L0/fespace-file.md` exists at L0; no L1 form yet).
