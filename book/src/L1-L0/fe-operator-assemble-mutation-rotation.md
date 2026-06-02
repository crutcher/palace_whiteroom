---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: rough-in
lowers: L1/fe_assemble (firm — landed cycle-054)
l0_anchor: palace/fem/bilinearform.{hpp,cpp}, palace/fem/libceed/operator.cpp, palace/models/laplaceoperator.cpp, palace/linalg/rap.cpp
justification_kind: structural
---

# fe-operator-assemble-mutation-rotation

**THREAD-OPENER (cycle-053, abstractor D3).** Observation-first sketch of the finite-element
assembly surface — the rewrite that takes a pure "assemble a global FE operator from a list of
weak-form terms" form into Palace's build-up-then-assemble C++ machinery. This theme **maps the
surface and names the speculative abstractions**; it is deliberately `rough-in`, not a firm
landing. FE assembly is the MFEM-equivalent assembly sub-spine (in scope per CLAUDE.md mesh/FE);
this theme opens it, a cohort of follow-on harvester/abstractor passes fills it.

## Status

`rough-in` (thread-opener). The structural decomposition is recognized and L0-anchored, but the
theme is **not promoted** because (a) its LHS operator [`fe_assemble`](../L1/fe_assemble.md) is now
**firm** (landed cycle-054), but the remaining speculative L1 operators it lowers
(`eliminate_essential_bc`, `eliminate_rhs`) are still rough-in placeholders awaiting harvester
promotion, (b) the libCEED matrix-materialization step crosses an **upstream library boundary**
(see §"libCEED boundary" — logged as OQ, not yet classified obstruction vs. transitive-firm), and
(c) the integrator-term vocabulary (the set of weak-form terms — diffusion / mass / curl-curl /
div-div / ...) is only partially witnessed by this single electrostatic probe. Promotion route: a
harvester pass landing `fe_assemble` firm + an abstractor/lowering-verifier pass settling the
libCEED-boundary classification + a sweep enumerating the integrator-term cohort across the 5
solver pipelines.

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

The BC-elimination is a **separable post-composition**, not part of the assembly fold:

    K_bc = eliminate_essential_bc(K, dbc_dofs, DIAG_ONE)
        -- pin the rows/cols of the essential (Dirichlet) dofs; place 1 on the diagonal

    (X, RHS) = eliminate_rhs(K, bc_values, dbc_dofs)
        -- lift the inhomogeneous Dirichlet data into the RHS:
        --   RHS := -K·(BC-extended x), then restore the pinned entries

Of these three pieces, [`fe_assemble`](../L1/fe_assemble.md) is now **firm** (landed cycle-054; its
signature is authoritative there). `eliminate_essential_bc` and `eliminate_rhs` remain **rough-in
placeholders** this thread proposes; their signatures are best-guess pending harvester promotion.

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
   `palace/models/laplaceoperator.cpp:225-253`): project the Dirichlet boundary values into a
   grid function (`x.ProjectBdrCoefficient(one, source_marker)`, `:236`), restrict to true dofs,
   then `PtAP_K->EliminateRHS(X, RHS)` (`:253`). The elimination body
   (`palace/linalg/rap.cpp:56-82`) computes `RHS := RHS − A·(prolongated BC-extended x)` then
   restores the pinned dof entries — the L0 realization of `eliminate_rhs`.

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
it is logged as OQ — see §"libCEED boundary".)

## libCEED boundary

`FullAssemble`'s actual matrix materialization lives in `ceed::CeedOperatorFullAssemble`
(`palace/fem/libceed/operator.cpp:455-490`), which calls libCEED's `CeedOperatorAssembleCOO` to get
the operator in COO format and converts to CSR. The **element-local quadrature kernels** (the
per-integrator `integ->Assemble(...)` that builds each `CeedOperator` sub-operator,
`palace/fem/bilinearform.cpp:75-76`) bottom out in libCEED basis-apply + restriction operations.
This is **upstream library behavior** (libCEED), cited at Palace's call boundary but not itself
Palace source. **Logged as OQ** (see §Open questions): whether the FE-assembly thread treats the
element-local quadrature kernel as (a) a transitive-firm leaf cited at the Palace boundary,
(b) an `obstruction (opaque-library-ownership)` à la the HYPRE relax-type precedent, or
(c) a spine primitive to be re-expressed in tensor-field vocabulary (basis-evaluation +
quadrature-contraction as a tensor contraction). The choice gates how deep this thread goes; it is
a finding for the batch-16 meta-phase, not resolved here.

## Speculative L1 operators (need harvester promotion)

- ~~`fe_assemble`~~ — **PROMOTED firm cycle-054**, see [`L1/fe_assemble`](../L1/fe_assemble.md).
- `eliminate_essential_bc` — pin essential (Dirichlet) dofs into the assembled operator.
- `eliminate_rhs` — lift inhomogeneous Dirichlet data into the RHS vector.
- `weak_form_term` (type) — the `(coefficient, differential-operator)` weak-form contribution; the
  element type of the term list `fe_assemble` folds over (diffusion / mass / curl-curl / div-div /
  ... — the term cohort is only partially witnessed here).

## Verified-against

- `palace/models/laplaceoperator.cpp:184-223` — `GetStiffnessMatrix`: the build-up-then-assemble
  witness (BilinearForm ctor + `AddDomainIntegrator<DiffusionIntegrator>` + `Assemble` + per-level
  `ParOperator` wrap with `SetEssentialTrueDofs`).
- `palace/models/laplaceoperator.cpp:225-253` — `GetExcitationVector`: the BC-elimination witness
  (`ProjectBdrCoefficient` + `ParallelProject` + `EliminateRHS`).
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
