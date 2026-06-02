---
agent: abstractor
invoked_at: 2026-06-01T235200Z
scope: L1>L0 theme sketch (THREAD-OPENER, observation-first) — fe-operator-assemble-mutation-rotation
status: pending
inputs:
  - reference/palace/palace/models/laplaceoperator.cpp:183-253 (GetStiffnessMatrix + GetExcitationVector — the electrostatic witness)
  - reference/palace/palace/fem/bilinearform.{hpp,cpp} (the assembly entry-point: integrator-fold + PA/FA dispatch)
  - reference/palace/palace/fem/integrator.hpp:39-130 (BilinearFormIntegrator interface + concrete weak-form terms)
  - reference/palace/palace/fem/libceed/operator.cpp:455-490 (CeedOperatorFullAssemble — the COO→CSR matrix materialization; libCEED boundary)
  - reference/palace/palace/linalg/rap.cpp:56-82 (ParOperator::EliminateRHS — BC-elimination)
  - book/src/L0/fem-bilinearform-file.md (firm L0 navigation for the assembly file — already names the integrator-fold insight)
  - book/src/L1/bilinear-form.md (the slug-collision: existing `bilinear-form` is the BLAS-2 reduction xᴴMy, NOT FE assembly)
integrated_at: 2026-06-02T010500Z
integration_commit: 5e8e7a1
integration_notes: "cycle-053 D3 — APPLIED clean. Opened the MFEM-equivalent FE-assembly sub-spine thread: NEW book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (rough-in BY DESIGN) + L1-L0/index dep-map row + L1/index FE-assembly-sub-spine cohort subsection (3 plain-text speculative-op bullets fe_assemble/eliminate_essential_bc/eliminate_rhs/weak_form_term + slug-collision note vs BLAS-2 bilinear-form) + SUMMARY entry. The BilinearForm-as-fold-over-integrators key insight (K=Sum_i A(term_i)) codemap-verified honest (bilinearform.cpp:28-107 accumulation :73-75, laplaceoperator.cpp:184). 2 live links into the new file resolve at build; speculative ops correctly plain-text (no linkcheck2 hazard). 4 OQs routed to batch-16 meta-phase + 1 RESOLVED-in-report (slug-collision). Build exit 0; new theme renders."
---

# CYCLE: L1>L0 theme sketch (THREAD-OPENER) — fe-operator-assemble-mutation-rotation

## Summary

This is a **thread-opening probe** for the FE-assembly surface (flagged the largest unspined
solver gap by the cycle-052 electrostatic probe D6). It is observation-first: it maps the surface,
sketches the lowering theme, and proposes speculative abstractions as **rough-in placeholders** —
it does NOT force a firm landing.

The motivating L0 pattern is `LaplaceOperator::GetStiffnessMatrix`
(`palace/models/laplaceoperator.cpp:184-223`): build a `BilinearForm` over the H1 space, append a
`DiffusionIntegrator` weak-form term, call `Assemble`, then wrap each multigrid level into a
`ParOperator` carrying its Dirichlet-BC essential-dof list. The companion
`GetExcitationVector` (`:225-253`) sets the Dirichlet boundary values and eliminates the essential
BC into the RHS. Underneath, `BilinearForm::PartialAssemble` (`palace/fem/bilinearform.cpp:28-107`)
is **a fold over an integrator list**: each integrator contributes a libCEED sub-operator that is
accumulated into one composite `ceed::Operator` via `AddSubOperator`; `FullAssemble` then
materializes that into a sparse `HypreCSRMatrix` (`CeedOperatorFullAssemble`,
`palace/fem/libceed/operator.cpp:455-490`).

The proposed L1>L0 theme **`fe-operator-assemble-mutation-rotation`** lowers a pure-functional
"assemble a global FE operator from a list of weak-form terms" form into Palace's
build-up-then-assemble C++ shape. The shared-spine reading is a **fold/reduction**: the global
operator is `Σ_i integ_i` over domain + boundary terms, the assembled matrix is the materialization
of that fold's action, and BC-elimination is a separable post-composition. **This is a genuine
vocabulary shift, not a rename**: the L0 form is imperative object-mutation (construct empty
container, push integrators, mutate into a sub-operator-accumulating composite, finalize); the L1
form is a single applicative `fe_assemble(space, [terms])` over an immutable term list. The theme
lands **`rough-in`** by design — it is a thread-opener, and the surface is large (MFEM-equivalent
assembly is its own sub-spine). The speculative L1 operators (`fe_assemble`,
`eliminate_essential_bc`, `eliminate_rhs`) are rough-in placeholders for a later harvester.

**Key disambiguation finding** (surfaced as OQ): the slug `bilinear-form` is already taken at L1 by
the BLAS-2 matrix-weighted inner product `xᴴ M y` (`book/src/L1/bilinear-form.md`). That is a
**different object** from `BilinearForm` the C++ assembly class. This thread must NOT reuse the
`bilinear-form` slug; the proposed operator is named `fe_assemble` to avoid the collision.

## Proposed changes

```new:book/src/L1-L0/fe-operator-assemble-mutation-rotation.md
---
layer: L1-L0
theme: fe-operator-assemble-mutation-rotation
status: rough-in
lowers: L1/fe_assemble (speculative rough-in)
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
theme is **not promoted** because (a) the speculative L1 operators it lowers (`fe_assemble`,
`eliminate_essential_bc`, `eliminate_rhs`) are themselves rough-in placeholders awaiting harvester
promotion, (b) the libCEED matrix-materialization step crosses an **upstream library boundary**
(see §"libCEED boundary" — logged as OQ, not yet classified obstruction vs. transitive-firm), and
(c) the integrator-term vocabulary (the set of weak-form terms — diffusion / mass / curl-curl /
div-div / ...) is only partially witnessed by this single electrostatic probe. Promotion route: a
harvester pass landing `fe_assemble` firm + an abstractor/lowering-verifier pass settling the
libCEED-boundary classification + a sweep enumerating the integrator-term cohort across the 5
solver pipelines.

## L1 form (LHS)

The pure-functional FE-assembly form consumes a finite-element space and an **immutable list of
weak-form terms** (each term a `(coefficient, differential-operator)` pair naming a bilinear
weak-form contribution `a_i(u, v)`), and produces a fresh global linear operator. Nothing is
mutated; there is no container built up in place, no sub-operator accumulator, no finalize step.

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

These three pieces — `fe_assemble`, `eliminate_essential_bc`, `eliminate_rhs` — are the speculative
L1 vocabulary this thread proposes. They are **rough-in placeholders**; signatures are best-guess.

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
   accumulate it into the composite operator (`palace/fem/bilinearform.cpp:73-75` domain branch;
   `:93-95` boundary branch), then `op->Finalize()` (`:104`). `FullAssemble`
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
`palace/fem/bilinearform.cpp:73-75`) bottom out in libCEED basis-apply + restriction operations.
This is **upstream library behavior** (libCEED), cited at Palace's call boundary but not itself
Palace source. **Logged as OQ** (see §Open questions): whether the FE-assembly thread treats the
element-local quadrature kernel as (a) a transitive-firm leaf cited at the Palace boundary,
(b) an `obstruction (opaque-library-ownership)` à la the HYPRE relax-type precedent, or
(c) a spine primitive to be re-expressed in tensor-field vocabulary (basis-evaluation +
quadrature-contraction as a tensor contraction). The choice gates how deep this thread goes; it is
a finding for the batch-16 meta-phase, not resolved here.

## Speculative L1 operators (need harvester promotion)

- `fe_assemble` — assemble a global FE operator from a space + immutable weak-form term list.
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
  (`AddSubOperator` accumulation at `:73-75` domain / `:93-95` boundary; `Finalize` at `:104`).
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
```

```edit:book/src/L1-L0/index.md
| [bilinear-form-mutation-rotation](./bilinear-form-mutation-rotation.md) | `L1/bilinear-form` (rough-in test-coverage-bounded) | `palace/linalg/operator.{hpp,cpp}`, `palace/models/boundarymodeoperator.cpp` | firm *(structural; 2 element-type sub-patterns A real-`A`/B complex-`A` + callsite cohort C; reuses apply_linop A `A.Mult(x,Ax)` (×2 lane-split for real-`A`; ×1 direct for complex-`A`) + dot A `Dot(comm,Ax,y)`; internally-allocated workspace `Ax` (Category-4 — distinct from `matrix-weighted-norm`'s caller-supplied `Bx`); L1/L0 conjugation-asymmetry reconciliation via argument-position swap; no SPD/Hermitian precondition; both M-symmetry witnesses Hermitian `Bttr`(:85) + non-Hermitian `Atn`(:90))* |
| fe-operator-assemble-mutation-rotation *(rough-in; THREAD-OPENER cycle-053)* | `L1/fe_assemble` *(speculative rough-in; no anchor yet)* | `palace/fem/bilinearform.{hpp,cpp}`, `palace/fem/libceed/operator.cpp`, `palace/models/laplaceoperator.cpp:184-253`, `palace/linalg/rap.cpp:56-82` | rough-in *(structural; integrator-fold + PA/FA variant axis + separable BC-elimination (`eliminate_essential_bc`/`eliminate_rhs`); slug-collision noted — distinct from BLAS-2 `bilinear-form` `xᴴMy`; libCEED matrix-materialization boundary logged OQ (transitive-firm vs opaque-library-ownership vs tensor-contraction-respine); opens the MFEM-equivalent FE-assembly sub-spine — cohort follow-on)* |
```

```edit:book/src/L1/index.md
**Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)** — speculative L1 operators opening the finite-element assembly surface (the MFEM-equivalent assembly sub-spine, in scope per CLAUDE.md mesh/FE). Proposed by the [`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) L1>L0 thread-opener; await harvester promotion + integrator-term-cohort enumeration:

- `fe_assemble` *(rough-in; no anchor yet)* — assemble a global FE operator from a space + immutable weak-form term list; the integrator-fold `K = Σ_i A(term_i)` (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener). **Slug-collision note**: NOT the existing [`bilinear-form`](./bilinear-form.md) (which is the BLAS-2 reduction `xᴴ M y`); `fe_assemble` is the C++ `BilinearForm`-*class* assembler.
- `eliminate_essential_bc` *(rough-in; no anchor yet)* — pin essential (Dirichlet) dofs into the assembled operator (L0: `ParOperator::SetEssentialTrueDofs`, `palace/models/laplaceoperator.cpp:215-217`) (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener).
- `eliminate_rhs` *(rough-in; no anchor yet)* — lift inhomogeneous Dirichlet data into the RHS (L0: `ParOperator::EliminateRHS`, `palace/linalg/rap.cpp:56-82`) (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener).
```

```edit:book/src/SUMMARY.md
- [bilinear-form-mutation-rotation](./L1-L0/bilinear-form-mutation-rotation.md)
- [fe-operator-assemble-mutation-rotation](./L1-L0/fe-operator-assemble-mutation-rotation.md)
```

## Speculative operators proposed

- **`fe_assemble`** — signature (best guess):
  `fe_assemble :: (space: FiniteElementSpace[N], terms: [WeakFormTerm]) -> LinearOperator[N, N]`.
  Assemble a global FE operator as the fold `K = Σ_i A(term_i)` over an immutable weak-form term
  list. This is the L1 lift of `BilinearForm::Assemble`. Motivation: the integrator-fold is the
  central FE-assembly abstraction (the L0 file note already names it: "BilinearForm is
  fundamentally a fold over integrators"); lifting it gives the spine a clean "assemble operator from
  weak-form terms" primitive that all 5 solver pipelines consume. Harvester should land it firm once
  the weak-form-term cohort is enumerated and the libCEED boundary is classified.

- **`eliminate_essential_bc`** — signature (best guess):
  `eliminate_essential_bc :: (K: LinearOperator[N,N], dofs: DofSet, policy: DiagPolicy) -> LinearOperator[N,N]`.
  Pin the rows/cols of essential (Dirichlet) dofs, placing 1 (DIAG_ONE) or 0 (DIAG_ZERO) on the
  diagonal. L0: `ParOperator::SetEssentialTrueDofs`. Motivation: BC-elimination is a separable
  post-composition shared across all solver pipelines (every Dirichlet-constrained problem needs it);
  factoring it from the assembly fold keeps both clean.

- **`eliminate_rhs`** — signature (best guess):
  `eliminate_rhs :: (K: LinearOperator[N,N], bc_values: Tensor[N], dofs: DofSet) -> (Tensor[N], Tensor[N])`.
  Lift inhomogeneous Dirichlet data into the RHS: `RHS := −K·x_bc` on free dofs, restore pinned
  entries. Returns `(X, RHS)`. L0: `ParOperator::EliminateRHS` (`palace/linalg/rap.cpp:56-82`).
  Motivation: the body is already an `apply_linop` + `axpy` composition over the assembled operator
  (firm spine vocabulary); naming it makes the inhomogeneous-BC pattern reusable.

- **`weak_form_term`** (type, not operator) — the element type of `fe_assemble`'s fold:
  a `(coefficient, differential-operator)` pair naming a bilinear weak-form contribution. The
  differential-operator cohort witnessed so far: ∇ (diffusion), identity (mass), curl (curl-curl),
  div (div-div) (`palace/fem/integrator.hpp:67-130`). This is the FE-specific new vocabulary the
  sub-spine introduces; full cohort enumeration is follow-on work.

## Supporting evidence

- `palace/models/laplaceoperator.cpp:184-223` — `GetStiffnessMatrix` (the electrostatic witness;
  BilinearForm + DiffusionIntegrator + Assemble + per-level ParOperator wrap). Anchor verified:
  `GetStiffnessMatrix` at line 184 (citecheck `--anchor`).
- `palace/models/laplaceoperator.cpp:225-253` — `GetExcitationVector` (BC-elimination into RHS).
- `palace/fem/bilinearform.hpp:25-91` — `class BilinearForm`; `:53-63` templated integrator-append.
- `palace/fem/bilinearform.cpp:28-107` — `PartialAssemble` (the integrator-fold; `AddSubOperator`
  accumulation at `:73-75`/`:93-95`, `Finalize` at `:104`).
- `palace/fem/bilinearform.cpp:141-151` — `Assemble(bool)` PA/FA dispatch.
- `palace/fem/integrator.hpp:39-130` — `BilinearFormIntegrator` interface + concrete terms.
- `palace/fem/libceed/operator.cpp:455-490` — `CeedOperatorFullAssemble` (COO→CSR; libCEED boundary).
- `palace/linalg/rap.cpp:56-82` — `ParOperator::EliminateRHS`.
- `book/src/L0/fem-bilinearform-file.md` — firm L0 navigation (already names the integrator-fold
  insight + the PA/FA-collapses-at-L1 + DiscreteLinearOperator interpolation sibling).
- `book/src/L1/bilinear-form.md` — the slug-collision source (BLAS-2 `xᴴMy`, NOT FE assembly).
- `test/unit/test-libceed.cpp:284-325` — `TestCeedOperatorFullAssemble` (L0-equivalent semantic
  evidence: asserts the assembled matrix matches an MFEM reference to 1e-12 — direct test coverage
  of the FullAssemble materialization, useful for a future `empirical-match` justification on
  `fe_assemble`).

All citations verified against source via `tools/citecheck/citecheck.py` (`--anchor` on
`GetStiffnessMatrix`/`GetExcitationVector`; bounds-check pass on the batch — all in-bounds).

## Open questions / caveats

1. **`fe-assembly-thread-scope-and-sequencing`** (FOR BATCH-16 META-PHASE) — FE assembly is the
   largest unspined solver surface and is its own sub-spine (FE space construction + weak-form-term
   vocabulary + element-local→global assembly + BC-elimination + multigrid-hierarchy assembly +
   DiscreteLinearOperator interpolation). This thread-opener maps the entry point; the meta-phase
   should decide the **sequencing**: (a) land `fe_assemble` + the 3 BC operators firm next, then
   enumerate the weak-form-term cohort, vs. (b) settle the libCEED-boundary classification first
   (it gates how deep the thread goes), vs. (c) treat FE assembly as low-priority test-load that
   advances only when cleanly describable (per the 2026-06-01 redirect: solvers pulled up only when
   cleanly describable, never forcing the spine). The redirect leans toward (c). Recommendation:
   land `fe_assemble` + `eliminate_rhs` (both cleanly describable in existing fold + apply_linop +
   axpy vocabulary) as the next firm step; defer the weak-form-term differential-operator cohort
   (the genuinely-new FE vocabulary) until a solver actually needs more than diffusion.

2. **`fe-assembly-libceed-boundary-classification`** — the element-local quadrature kernel
   (`integ->Assemble` building a `CeedOperator` sub-operator) + the COO→CSR materialization
   (`CeedOperatorFullAssemble`) bottom out in libCEED (upstream). Three routes (see theme §"libCEED
   boundary"): transitive-firm-leaf-at-boundary / `obstruction (opaque-library-ownership)` /
   tensor-contraction-respine. This is distinct from the HYPRE/SLEPc opaque-library precedents
   because Palace DOES own the orchestration (the fold, the PA/FA dispatch) — only the innermost
   quadrature kernel is library-owned. Likely outcome: the fold + dispatch + BC-elimination lift
   cleanly (Palace-owned), and the quadrature kernel is the opaque leaf. Needs a lowering-verifier
   or harvester pass to settle.

3. **`fe-assemble-slug-collision-with-bilinear-form`** (RESOLVED in this report by naming) — the
   slug `bilinear-form` is taken at L1 by the BLAS-2 reduction `xᴴ M y`
   (`book/src/L1/bilinear-form.md`), which is a *different object* from the C++ `BilinearForm`
   assembly class. This thread uses `fe_assemble` to avoid the collision. Flagging so downstream
   producers do NOT conflate the two and do NOT route FE-assembly work to the `bilinear-form` slug.
   (The two are related only by name — both derive from "bilinear form" the math concept — but the
   L1 objects are unrelated: a scalar reduction vs. a global operator constructor.)

4. **`fe-space-l1-form-untouched`** — `FiniteElementSpace` (the dof-numbering / mesh-topology
   object) has an L0 chapter (`book/src/L0/fespace-file.md`) but no L1 form. `fe_assemble` takes a
   space as an opaque parameter here; a full FE-assembly spine eventually needs an L1 FE-space form
   (mesh + element-collection + dof-map). This is a sibling sub-thread, not opened here.

5. **`discrete-linear-operator-interpolation-sibling`** — `DiscreteLinearOperator`
   (`palace/fem/bilinearform.cpp:203-282`) is the interpolation variant of the same assembly fold
   (interpolator basis instead of quadrature, transpose-also production, dof-multiplicity
   averaging). It shares the assembly skeleton with `BilinearForm` but adds the multiplicity-scaling
   load-bearing numerical content. A future abstractor pass should sketch it as a sibling of
   `fe_assemble` (likely `fe_interpolate`), reusing this thread's fold structure. Not opened here.
