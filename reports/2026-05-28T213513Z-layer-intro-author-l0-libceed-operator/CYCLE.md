---
agent: layer-intro-author
invoked_at: 2026-05-28T213513Z
scope: L0 bundle-6 chapter #5 — book/src/L0/fem-libceed-operator-file.md (palace/fem/libceed/operator.cpp)
status: integrated
integrated_at: 2026-05-28T221238Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-016 (per-report position 4). NEW firm L0 file chapter fem-libceed-operator-file (bundle-6 #5; libCEED composite-operator wrapper + CeedOperatorFullAssemble COO→CSR @455-523 + CeedOperatorCoarsen @525-585). SUMMARY.md registered under L0 Part (L0 20→21). 2 fem-bilinearform-file.md forward references retired to live links (1 retroactive slice). OQ bundle-6-l0-libceed-operator-file-next-candidate resolved (ledger:2808). Retroactive-budget 1 (global 1, well below ≥4). Applied the repaired CYCLE.md content. Book build clean (exit 0)."
---

# CYCLE: L0 file — palace/fem/libceed/operator.{hpp,cpp}

## Summary

Authors L0 bundle-6 chapter #5: a reference note for `palace/fem/libceed/operator.{hpp,cpp}`,
the **libCEED composite-operator wrapper + matrix-materialization** file. This is the file
`book/src/L0/fem-bilinearform-file.md` forward-referenced as a deliberate plain-text
(no-link) target: `BilinearForm::FullAssemble` (`bilinearform.cpp:109-113`) is a thin forwarder to
`ceed::CeedOperatorFullAssemble`, whose body lives here (`operator.cpp:455-523`), and the
multigrid-hierarchy `Assemble` overload reuses `ceed::CeedOperatorCoarsen`
(`operator.cpp:525-585`, called from `bilinearform.cpp:174`).

The file declares three things in `namespace palace::ceed`: the `ceed::Operator` composite-operator
wrapper class (matrix-free apply over a per-thread vector of libCEED `CeedOperator`s), its
`SymmetricOperator` subclass (transpose ≡ forward), and the two free functions
`CeedOperatorFullAssemble` (COO→CSR matrix materialization) + `CeedOperatorCoarsen` (geometric-multigrid
coarse-operator construction reusing the fine-level quadrature data).

This chapter is the **producer of both the matrix-free `ceed::Operator` apply** that
`bilinearform.cpp:27-107` builds via `AddSubOperator`/`Finalize`, **and the assembled
`hypre::HypreCSRMatrix`** that `bilinearform.cpp:109-113` forwards to. It is the matrix-free side of
the PA/FA dual that `fem-bilinearform-file` introduces. A unit test
(`test/unit/test-libceed.cpp:284-343`) is cited as L0-equivalent evidence that full assembly matches
a reference MFEM sparse matrix to `1.0e-12 * MaxNorm` and that PA-apply matches the same reference.

Three proposed changes:
1. **New file** `book/src/L0/fem-libceed-operator-file.md` (full chapter below).
2. **`book/src/SUMMARY.md`** — register the new chapter under the L0 Part, after the
   `fem-bilinearform-file` row.
3. **`book/src/L0/fem-bilinearform-file.md`** — retire the deliberate plain-text forward reference
   to this file (convert to a live link now that the anchor exists), in two places: the
   `FullAssemble` prose (`fem-bilinearform-file.md:61-66`) and the Evidence row
   (`fem-bilinearform-file.md:158`).

## Proposed changes

```edit:book/src/L0/fem-libceed-operator-file.md
[old]:
[new]:
# File — `palace/fem/libceed/operator.{hpp,cpp}`

A reference note for the **libCEED composite-operator wrapper + matrix-materialization** file. Per
the class header comment (`palace/fem/libceed/operator.hpp:28-30`): *"Wrapper class for libCEED's
CeedOperator, supporting composite operator construction and application with multiple threads."*
This is the file that holds the concrete matrix-free local operator (`ceed::Operator`) that
[`fem-bilinearform-file`](./fem-bilinearform-file.md) builds up term-by-term via `AddSubOperator`,
**and** the two free functions that (i) materialize that operator into an assembled
`hypre::HypreCSRMatrix` (`CeedOperatorFullAssemble`) and (ii) coarsen it for the geometric-multigrid
hierarchy (`CeedOperatorCoarsen`). It is the matrix-free side of the partial-assembly /
full-assembly dual that `fem-bilinearform-file` introduces — `bilinearform.cpp:109-113`'s
`FullAssemble` is a thin forwarder to `ceed::CeedOperatorFullAssemble` (`operator.cpp:455-523`), and
the multigrid-hierarchy `Assemble` overload calls `ceed::CeedOperatorCoarsen`
(`operator.cpp:525-585`) from `bilinearform.cpp:174`.

The file declares, inside `namespace palace::ceed` (the header opens `palace::ceed` at
`operator.hpp:13,25`): the `Operator` class, its `SymmetricOperator` subclass, and two free
functions. It is **in scope** under the mesh / FE-space-construction directive (this is the
MFEM-equivalent FE-assembly backend). Per the single-rank reading rule
([`par-types-single-rank-reading`](./par-types-single-rank-reading.md)), the libCEED objects
(`Ceed`, `CeedOperator`, `CeedVector`, `CeedElemRestriction`, `CeedBasis`), the `HypreCSRMatrix` /
`hypre_CSRMatrix*` output machinery, and the per-thread `PalacePragmaOmp(parallel ...)` shells are
all read single-rank / single-thread: the assembled operator is independent of thread count
([`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)). **OMP / libCEED
threading flagged once here; not re-flagged per method.**

## At a glance — the wrapper class and two free functions

- **`ceed::Operator : public palace::Operator`** (`operator.hpp:32-65`) — a composite of per-thread
  libCEED operators. Holds `std::vector<CeedOperator> op, op_t` (forward + transpose composites, one
  per OMP thread), workspace `CeedVector` arrays `u, v`, an optional `dof_multiplicity` vector, and
  a `mutable Vector temp` workspace (`operator.hpp:35-38`). The constructor
  (`operator.cpp:17-41`) creates one empty `CeedOperatorCreateComposite` per thread; the
  destructor (`operator.cpp:44-58`) tears them down. `AddSubOperator`
  (`operator.cpp:60-87`) appends a sub-operator (and optionally its transpose) into the current
  thread's composite via `CeedOperatorCompositeAddSub`, after verifying the active-vector lengths
  match `(height, width)`. `Finalize` (`operator.cpp:89-101`) runs `CeedOperatorCheckReady`. The
  apply surface (`Mult` / `AddMult` / `MultTranspose` / `AddMultTranspose` / `AssembleDiagonal`,
  `operator.hpp:57-65`) is matrix-free.
- **`ceed::SymmetricOperator : public Operator`** (`operator.hpp:69-80`) — replaces `MultTranspose`
  with `Mult` and `AddMultTranspose` with `AddMult` (libCEED operators have no native transpose, so
  the symmetric case avoids building `op_t`). This is the class `BilinearForm::PartialAssemble`
  constructs for the square/symmetric case.
- **`CeedOperatorFullAssemble`** (`operator.hpp:82-83`, body `operator.cpp:455-523`) — materializes a
  `ceed::Operator` into an assembled `hypre::HypreCSRMatrix`.
- **`CeedOperatorCoarsen`** (`operator.hpp:86-88`, body `operator.cpp:525-585`) — constructs a
  coarse-level `ceed::Operator` from a fine-level one, reusing the fine operator's quadrature data.
  Header comment (`operator.hpp:84-86`): *"Only available for square, symmetric operators (same input
  and output spaces)."*

## Matrix-free apply — the composite over per-thread sub-operators

`ceed::Operator::Mult` (`operator.cpp:181-189`) is the matrix-free local-operator action: it zeros
`y`, then calls the file-local `CeedAddMult` helper (`operator.cpp:147-177`, anonymous namespace)
which loops the per-thread composites applying `CeedOperatorApplyAdd` into the output, and finally
scales by `dof_multiplicity` if present (`operator.cpp:185-188`). `AddMult` (`operator.cpp:191-211`)
accumulates without zeroing; with a multiplicity vector it routes through `temp` and an
`mfem::forall` elementwise multiply-add (`operator.cpp:200-208`). `MultTranspose` /
`AddMultTranspose` (`operator.cpp:214-240`) apply the transpose composite `op_t` (with `u`/`v`
workspaces swapped), pre-scaling by `dof_multiplicity` on the input side when present. `AddMult`
and `AddMultTranspose` both `MFEM_VERIFY(a == 1.0, ...)` — the libCEED apply does not support a
scalar coefficient (`operator.cpp:193,221`).

`AssembleDiagonal` (`operator.cpp:116-143`) extracts the operator diagonal via
`CeedOperatorLinearAssembleAddDiagonal` per thread — used by Jacobi-family preconditioners.

The `dof_multiplicity` scaling is the **load-bearing numerical content of the interpolation path**:
it is the reciprocal shared-dof count that `DiscreteLinearOperator::PartialAssemble` installs via
`SetDofMultiplicity` (`fem-bilinearform-file`'s multiplicity averaging) so that interpolation between
conforming spaces is well-defined at shared dofs. For a plain `BilinearForm` it is empty and the
apply is the bare composite.

## `CeedOperatorFullAssemble` — COO → CSR materialization with set/accumulate

`CeedOperatorFullAssemble(op, skip_zeros, set)` (`operator.cpp:455-523`) materializes the matrix-free
composite into an assembled `hypre::HypreCSRMatrix`, in three stages:

- **Per-thread COO assembly** (`operator.cpp:459-490`, OMP-parallel) — each thread assembles its own
  composite into a coordinate-format matrix via the file-local `CeedOperatorAssembleCOO`
  (`operator.cpp:262-316`): `CeedOperatorLinearAssembleSymbolic` builds the sparsity pattern,
  `CeedOperatorLinearAssemble` fills values, and `skip_zeros` filters out exact-zero entries on the
  host (`operator.cpp:276-314`). An **empty composite** (`nsub_ops == 0`,
  `operator.cpp:468-474`) short-circuits to a zero-nnz matrix. Each thread then converts its COO to
  CSR via `OperatorCOOtoCSR` (`operator.cpp:319-451`), which sorts by row then column, deduplicates
  column entries, and fills a `hypre::HypreCSRMatrix` — the `set` flag selects whether each CSR slot
  takes a single value (`d_A[k] = vals[perm[Jmap[k]]]`, `operator.cpp:406-410`) or the **sum** of
  duplicated COO entries (`operator.cpp:412-423`).
- **Cross-thread fold** (`operator.cpp:509-513`) — the per-thread CSR matrices are summed with
  `hypre_CSRMatrixAdd(1.0, mat, 1.0, loc_mat[id])` into a single matrix.
- **Set-mode duplicate scaling** (`operator.cpp:496-508,515-521`) — when `set == true` and there is
  more than one thread, the same dof can be written by multiple threads, so the fold would
  double-count. A companion all-ones matrix `b_mat` (`hypre_CSRMatrixSetConstantValues(*b_mat, 1.0)`)
  is summed in parallel to count how many threads contributed each nonzero, and the final values are
  divided by that count (`d_data[i] *= 1.0 / d_b_data[i]`, `operator.cpp:520`). For `set == false`
  (accumulate) the cross-thread sum is the intended behaviour and no scaling runs.

The **`set` vs accumulate axis is the load-bearing semantic** of this function (not a transparent
trick): `set == true` (used by `DiscreteLinearOperator::FullAssemble`, `bilinearform.hpp:122-131`)
makes shared-dof entries take a representative value; `set == false` (the default `BilinearForm`
path) sums them (weak-form term accumulation). The COO/CSR conversion, host zero-filtering, and OMP
per-thread assembly are transparent performance machinery
([`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)).

A unit test (`test/unit/test-libceed.cpp:284-343`, helper `TestCeedOperatorFullAssemble`) asserts
the assembled matrix matches a reference MFEM `BilinearForm` sparse matrix to within
`1.0e-12 * max(MaxNorm, 1.0)` (`test-libceed.cpp:298`), and `TestCeedOperator`
(`test-libceed.cpp:327-345`) checks PA-apply against the same reference — direct L0-equivalent
evidence that the **partial and full assembly compute the same operator** (the PA/FA dual collapses
at L1).

## `CeedOperatorCoarsen` — multigrid coarse-operator construction

`CeedOperatorCoarsen(op_fine, fespace_coarse)` (`operator.cpp:525-585`) builds the coarse-level
operator for the geometric-multigrid hierarchy. Its inner `SingleOperatorCoarsen` lambda
(`operator.cpp:528-548`) pulls the fine sub-operator's active basis and element topology, looks up
the coarse space's `CeedElemRestriction` + `CeedBasis` for that geometry
(`operator.cpp:537-542`, reusing `fespace_coarse.GetCeedGeomFactorData` /
`GetCeedElemRestriction` / `GetCeedBasis`), and calls libCEED's `CeedOperatorMultigridLevelCreate`
(`operator.cpp:543-545`) — which **reuses the fine-level quadrature data and quadrature function**
rather than re-assembling from scratch. The outer body (`operator.cpp:551-583`) constructs a
`SymmetricOperator` sized to the coarse space, then in an OMP-parallel region loops the fine
composite's sub-operators (`CeedOperatorCompositeGetSubList`, `operator.cpp:573-580`) coarsening
each into the coarse composite via `AddSubOperator`, and `Finalize`s.

This is the per-level coarsening that `BilinearForm::Assemble(FiniteElementSpaceHierarchy, ...)`
(`bilinearform.cpp:168-181`) calls when consecutive hierarchy levels share a mesh — the cheaper
quadrature-reuse path versus re-assembling. The square/symmetric restriction is why the result is a
`SymmetricOperator`.

## Notes for higher layers

- **The PA/FA dual collapses at L1; this file is the PA side + the FA materializer.** The
  matrix-free `ceed::Operator` apply (`Mult`/`AddMult`) and the assembled `HypreCSRMatrix`
  (`CeedOperatorFullAssemble`) compute the same local-operator action — the unit test
  (`test-libceed.cpp:284-345`) is the empirical witness. At L1 the FE-assembly operator is one map;
  the matrix-free-vs-assembled choice is a performance annotation, the same variant axis
  `fem-bilinearform-file` records.
- **`ceed::Operator` is the concrete realization of the integrator-fold.** `AddSubOperator`
  (`operator.cpp:60-87`) is the fold step — each weak-form term's libCEED sub-operator is composed
  into the running composite via `CeedOperatorCompositeAddSub`. At L2 this is the "sum of weak-form
  terms" algebra `fem-bilinearform-file` describes; this file is where the composition physically
  happens.
- **The `set`/accumulate axis on full assembly is load-bearing.** `set == true` (interpolation,
  shared-dof representative value) vs `set == false` (weak-form accumulation, sum) is an algebraic
  distinction in how duplicated nonzeros combine (`operator.cpp:406-423,496-521`), not a performance
  trick. At L1 it lifts as a variant axis on the FE-assembly-to-matrix map, tied to the
  `BilinearForm`-vs-`DiscreteLinearOperator` distinction.
- **`dof_multiplicity` scaling is the interpolation path's load-bearing numerical content.** The
  reciprocal shared-dof count applied in `Mult`/`AddMultTranspose` (`operator.cpp:185-188,200-208`)
  is what makes inter-space interpolation well-defined at conforming-space shared dofs. At L1 it is
  part of the `DiscreteLinearOperator` lift, not boilerplate.
- **`CeedOperatorCoarsen` is the per-level construction step of the multigrid-operator stack.** It
  lifts as the coarsening side of the geometric-multigrid V-cycle algebra (the apply side lives in
  `GeometricMultigridSolver`,
  [`preconditioner-classes-overview`](./preconditioner-classes-overview.md)); the quadrature-data
  reuse (`CeedOperatorMultigridLevelCreate`, `operator.cpp:543-545`) is a transparent performance
  optimization over re-assembly.
- **OMP per-thread composites and libCEED `Ceed`-per-thread are single-machine performance
  machinery.** Read single-rank / single-thread per
  [`par-types-single-rank-reading`](./par-types-single-rank-reading.md); the per-thread
  composite-build and cross-thread CSR fold (`operator.cpp:459-521`) are transparent tricks — the
  assembled operator and its action are independent of thread count.

## Referenced from

*Forward-declared. L1 work on the FE-assembly operator (the integrator-fold and PA/FA variant axis,
queued as FE-space material reaches the frontier) will reference this chapter.*

- [`L0/fem-bilinearform-file`](./fem-bilinearform-file.md) — the assembly entry-point file whose
  `PartialAssemble` builds the `ceed::Operator` (via `AddSubOperator`) and whose `FullAssemble`
  forwards to `CeedOperatorFullAssemble`; this chapter is its libCEED backend.
- [`L0/linalg-rap-file`](./linalg-rap-file.md) — the parallel-operator wrapper whose local operator
  `A` is one of these `ceed::Operator` (matrix-free) or the assembled `HypreCSRMatrix`.
- [`L0/par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the libCEED / Hypre /
  OMP single-rank-single-thread reading rule applied throughout.
- [`L0/transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the
  matrix-free-vs-assembled dual + OMP-parallel-assembly classification, and the `set`/accumulate
  load-bearing distinction.
- [`L0/preconditioner-classes-overview`](./preconditioner-classes-overview.md) — the
  `GeometricMultigridSolver` consuming the `CeedOperatorCoarsen` operator stack.

## Evidence (representative)

- `palace/fem/libceed/operator.hpp:1-96` — the header file (96 lines; `ceed::Operator` /
  `SymmetricOperator` / `CeedOperatorFullAssemble` / `CeedOperatorCoarsen`).
- `palace/fem/libceed/operator.hpp:13,25` — `namespace palace` / `namespace ceed` open.
- `palace/fem/libceed/operator.hpp:28-30` — class doc comment (composite operator construction +
  application with multiple threads; the authoritative reading).
- `palace/fem/libceed/operator.hpp:32-65` — `class Operator : public palace::Operator` body.
- `palace/fem/libceed/operator.hpp:35-38` — `std::vector<CeedOperator> op, op_t;` +
  `std::vector<CeedVector> u, v;` + `Vector dof_multiplicity;` + `mutable Vector temp;`.
- `palace/fem/libceed/operator.hpp:48` — `void AddSubOperator(CeedOperator sub_op, CeedOperator sub_op_t = nullptr);`.
- `palace/fem/libceed/operator.hpp:50,54` — `void Finalize();` + `void SetDofMultiplicity(Vector &&mult);`.
- `palace/fem/libceed/operator.hpp:57-65` — `AssembleDiagonal` / `Mult` / `AddMult` /
  `MultTranspose` / `AddMultTranspose` overrides.
- `palace/fem/libceed/operator.hpp:69-80` — `class SymmetricOperator : public Operator` (transpose ≡ forward).
- `palace/fem/libceed/operator.hpp:82-83` — `CeedOperatorFullAssemble(const Operator &op, bool skip_zeros, bool set)` decl.
- `palace/fem/libceed/operator.hpp:84-88` — `CeedOperatorCoarsen` decl + comment ("Only available for square, symmetric operators").
- `palace/fem/libceed/operator.cpp:1-588` — the source file (588 lines).
- `palace/fem/libceed/operator.cpp:14` — `namespace palace::ceed` open.
- `palace/fem/libceed/operator.cpp:17-41` — `Operator::Operator(int h, int w)`: per-thread
  `CeedOperatorCreateComposite` + `CeedVectorCreate` under `PalacePragmaOmp(parallel ...)`.
- `palace/fem/libceed/operator.cpp:44-58` — `Operator::~Operator()` (per-thread destroy).
- `palace/fem/libceed/operator.cpp:60-87` — `Operator::AddSubOperator`: active-vector-length verify
  (66-72) + `CeedOperatorCompositeAddSub` into `op[id]` (73) + optional transpose into `op_t[id]` (76-86).
- `palace/fem/libceed/operator.cpp:89-101` — `Operator::Finalize` (`CeedOperatorCheckReady` per thread).
- `palace/fem/libceed/operator.cpp:103-114` — `Operator::DestroyAssemblyData`.
- `palace/fem/libceed/operator.cpp:116-143` — `Operator::AssembleDiagonal` (`CeedOperatorLinearAssembleAddDiagonal`).
- `palace/fem/libceed/operator.cpp:147-177` — anonymous-namespace `CeedAddMult` helper (per-thread
  `CeedOperatorApplyAdd` loop).
- `palace/fem/libceed/operator.cpp:181-189` — `Operator::Mult` (zero `y`, `CeedAddMult`, optional
  `*= dof_multiplicity`).
- `palace/fem/libceed/operator.cpp:191-211` — `Operator::AddMult` (`a==1.0` verify; multiplicity path
  via `temp` + `mfem::forall`).
- `palace/fem/libceed/operator.cpp:214-240` — `Operator::MultTranspose` / `AddMultTranspose` (transpose
  composite `op_t`, `u`/`v` swapped; input-side multiplicity pre-scale).
- `palace/fem/libceed/operator.cpp:244-316` — anonymous-namespace `CeedInternalCalloc`/`Free` +
  `CeedOperatorAssembleCOO` (symbolic + value assembly + host zero-filter at 276-314).
- `palace/fem/libceed/operator.cpp:319-451` — anonymous-namespace `OperatorCOOtoCSR`: row/col sort +
  dedup (327-371), CSR fill with `set ? single-value : sum` (404-423), device-copy branch (435-447).
- `palace/fem/libceed/operator.cpp:455-523` — `CeedOperatorFullAssemble`: per-thread COO+CSR assembly
  (459-490, empty short-circuit 468-474), set-mode all-ones `b_mat` count (496-508), cross-thread
  `hypre_CSRMatrixAdd` value fold (509-513), set-mode reciprocal duplicate-scaling (515-521).
- `palace/fem/libceed/operator.cpp:525-585` — `CeedOperatorCoarsen`: `SingleOperatorCoarsen` lambda
  (528-548) with `CeedOperatorMultigridLevelCreate` (543-545), `SymmetricOperator` coarse target
  (551-552), per-sub-op coarsening loop (565-581), `Finalize` (583).
- `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble` forwards to
  `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`.
- `palace/fem/bilinearform.cpp:168-181` — multigrid-hierarchy loop calling `ceed::CeedOperatorCoarsen`
  (174) when consecutive levels share a mesh, else `PartialAssemble`.
- `test/unit/test-libceed.cpp:284-298` — `TestCeedOperatorFullAssemble` asserts assembled-vs-reference
  matrix diff `< 1.0e-12 * max(MaxNorm, 1.0)` (the PA/FA equivalence witness).
- `test/unit/test-libceed.cpp:327-345` — `TestCeedOperator` runs PA-apply (`TestCeedOperatorMult`) +
  full-assemble (`TestCeedOperatorFullAssemble`) against the same MFEM reference form.
```

```edit:book/src/SUMMARY.md
[old]: - [File — palace/fem/bilinearform.{hpp,cpp}](./L0/fem-bilinearform-file.md)
[new]: - [File — palace/fem/bilinearform.{hpp,cpp}](./L0/fem-bilinearform-file.md)
- [File — palace/fem/libceed/operator.{hpp,cpp}](./L0/fem-libceed-operator-file.md)
```

```edit:book/src/L0/fem-bilinearform-file.md
[old]: - **`FullAssemble`** (`bilinearform.cpp:109-113`) is a thin forwarder: it delegates to
  `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)` (the actual matrix-materialization lives in
  `palace/fem/libceed/operator.cpp`, the not-yet-authored bundle-6 #5 candidate — see Open questions
  for the bundle ranking; plain-text reference, no link target until that chapter lands),
  returning a `hypre::HypreCSRMatrix`. The header overloads (`bilinearform.hpp:72-84`) chain
  partial-then-full and supply the `set` default.
[new]: - **`FullAssemble`** (`bilinearform.cpp:109-113`) is a thin forwarder: it delegates to
  `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)` (the actual matrix-materialization lives in
  [`fem-libceed-operator-file`](./fem-libceed-operator-file.md), the libCEED composite-operator
  backend), returning a `hypre::HypreCSRMatrix`. The header overloads (`bilinearform.hpp:72-84`)
  chain partial-then-full and supply the `set` default.
```

```edit:book/src/L0/fem-bilinearform-file.md
[old]: - `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)`.
[new]: - `palace/fem/bilinearform.cpp:109-113` — `BilinearForm::FullAssemble`: forwards to `ceed::CeedOperatorFullAssemble(op, skip_zeros, set)` (body in [`fem-libceed-operator-file`](./fem-libceed-operator-file.md)).
```

## Supporting evidence

All citations below were self-verified with codemap `read_range` against `palace/fem/libceed/operator.{hpp,cpp}`, `palace/fem/bilinearform.cpp`, and `test/unit/test-libceed.cpp` during this dispatch (per the cycle-015 producer-citation self-verification bullet):

- **File structure** (`get_file_subtree`): `namespace palace::ceed` opens at `operator.cpp:14`,
  spans to `:587`. Function boundaries confirmed: `Operator` ctor `17-42`, dtor `44-58`,
  `AddSubOperator` `60-87`, `Finalize` `89-101`, `DestroyAssemblyData` `103-114`,
  `AssembleDiagonal` `116-143`, anon-ns (`CeedAddMult`) `145-180`, `Mult` `182-190`, `AddMult`
  `192-212`, `MultTranspose` `214-218`, `AddMultTranspose` `220-240`, anon-ns
  (`CeedOperatorAssembleCOO` / `OperatorCOOtoCSR`) `242-453`, `CeedOperatorFullAssemble` `455-523`,
  `CeedOperatorCoarsen` `525-585`. (Subtree gives function-def spans; prose cites tightened
  sub-ranges all read-verified.)
- **Header** (`operator.hpp:1-96`): class doc comment at `28-30`; `Operator` body `32-65`; members
  `35-38`; `SymmetricOperator` `69-80`; `CeedOperatorFullAssemble` decl `82-83`; `CeedOperatorCoarsen`
  decl + comment `84-88`. Read-verified.
- **`set`/accumulate load-bearing distinction**: `OperatorCOOtoCSR` fill lambda
  (`operator.cpp:404-423`) — `set` → `d_A[k] = vals_array[d_perm[d_Jmap[k]]]`; else → summed loop.
  Cross-thread set-mode duplicate scaling read-verified at `operator.cpp:496-521`. Matches the
  `set=true` default in `DiscreteLinearOperator::FullAssemble` (`bilinearform.hpp:122-131`, per
  `fem-bilinearform-file`).
- **`CeedOperatorCoarsen` quadrature reuse**: `CeedOperatorMultigridLevelCreate`
  read-verified at `operator.cpp:543-545`; `SymmetricOperator` coarse target at `551-552`.
- **Cross-reference call sites** (`search_text` + `read_range`): `BilinearForm::FullAssemble` →
  `ceed::CeedOperatorFullAssemble` at `bilinearform.cpp:112`; hierarchy `Assemble` →
  `ceed::CeedOperatorCoarsen` at `bilinearform.cpp:174`.
- **Unit test (L0-equivalent evidence)**: `test/unit/test-libceed.cpp:298` asserts
  `mat_diff->MaxNorm() < 1.0e-12 * std::max(mat_ref.MaxNorm(), 1.0)`; `TestCeedOperator`
  (`:327-345`) runs both PA-apply and FA against the same reference MFEM form. Read-verified.
- **Concept/convention link targets** all exist under `book/src/L0/`:
  `par-types-single-rank-reading.md`, `transparent-vs-load-bearing-tricks.md`,
  `preconditioner-classes-overview.md`, `fem-bilinearform-file.md`, `linalg-rap-file.md`.

## Open questions / caveats

- **`OperatorCOOtoCSR` is a large pure-host routine (`operator.cpp:319-451`).** I summarized it as
  "sort by row then column, dedup, fill CSR" and cited the load-bearing `set`-branch. The Thrust
  `TODO` comment (`operator.cpp:277`) and the device-copy branch (`operator.cpp:435-447`) are
  transparent performance machinery; I did not over-detail the perm/Jmap bookkeeping since it is L0
  CSR-construction plumbing, not algebra. If a future L1/L2 author needs the COO→CSR dedup as its
  own concept, it could be split out — flagged, not forced.
- **`bilinearform.cpp:153-201` line ranges** are cited as `168-181` here for the coarsen loop
  specifically (the sub-range I read-verified); `fem-bilinearform-file` cites the whole overload as
  `153-201`. Both are correct at their respective granularities — no contradiction, the narrower
  range is the coarsen-reuse `if` block.
- **No `concepts/` page touched.** This chapter cites only existing L0 convention/file pages; no new
  cross-cutting concept emerged that warranted a `concepts/` entry (the `set`/accumulate axis is a
  per-file load-bearing note, not yet a recurring cross-file primitive).
- Closes OQ `bundle-6-l0-libceed-operator-file-next-candidate`.
