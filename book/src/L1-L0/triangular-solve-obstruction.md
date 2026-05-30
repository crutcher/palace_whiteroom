# triangular-solve-obstruction

The L1>L0 obstruction theme documenting that the general **sparse / dense
triangular-solve** primitive (`trsv` / `trsm` / `SpTrSV` / `TriangularSolve`) has
**no positive Palace source site**. Where triangular solves occur in Palace,
they occur **only inside opaque library calls** — HYPRE-internal Gauss-Seidel /
SSOR relaxation sweeps selected by integer config flags, and forward/back
substitution inside external direct-solver factorizations (MUMPS / SuperLU /
STRUMPACK). Palace-authored smoothers are deliberately GS-free
(Jacobi + Chebyshev only; the Chebyshev choice over Gauss-Seidel cites
Adams et al. 2003 explicitly). This is the concrete L0 evidence behind the
L3 index's `:7` "certain triangular solves" obstruction note.

**Obstruction-flavoured theme** — claim-free documentation, no constructive
L1 form. Follows the cycle-004 [`minres-iteration`](./minres-iteration.md) and
[`bicgstab-iteration`](./bicgstab-iteration.md) precedents (negative anchors
only, `justification kind: obstruction`).

## Slug

`triangular-solve-obstruction`

## L1 form (LHS)

**Empty — no constructive L1 form is proposed.**

A general triangular-solve primitive would have the literature signature

    trsv :: (R: Triangular[N, N], s: Tensor[N]) -> Tensor[N]
    trsv(R, s) = the unique y with  R · y = s   (R triangular, non-singular)

where `R` may be sparse (the Gauss-Seidel / SOR / ILU smoother kernel acting
on the length-`N` field) or dense (the BLAS-2 `TRSV` / `TRSM` substitution).
This signature is recorded here only for naming reference; **no L1 operator
of this shape exists in the artifact, and none is proposed by this theme**
(the alternative — a constructed primitive with no positive source site — is
out of policy per CLAUDE.md §Scope "Unimplemented Palace components are NOT
direct implementation targets"). The closest related leaves the artifact DOES
firm are:

- [`back_solve`](../L1/back_solve.md) (firm c027) — the **small-dense**
  upper-triangular GMRES / FGMRES restart-correction back-substitution
  (coordinate-space, dimension `j+1` ≤ `max_dim`, no collective). It is the
  *small-dense-triangular* sibling of [`lu_solve`](../L1/lu_solve.md), NOT a
  general `trsv`. The general `trsv` would act on the length-`N` field; this
  leaf does not.
- [`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md) L1>L0
  theme (cycle-029 dispatch-1, sibling theme landed in the same cycle as this
  one) — the rotation of the `back_solve` leaf into its L0 in-place
  back-substitution loop. Cross-referenced here only to make the sibling
  distinction concrete; that theme also covers only the GMRES/FGMRES
  restart-correction case, NOT a general `trsv`.

## L0 form (RHS)

**Empty — no Palace site authors a general triangular-solve.**

The L0 anchor is the **absence** of any standalone triangular-solve API,
combined with the **opaque-library-ownership** of every actual triangular
substitution that occurs in a Palace run. Three categories of negative anchor
ground the obstruction:

### (a) No standalone triangular-solve API in the small-dense utility module

The full public API of the small-dense matrix utility module is five
functions, **none of them a triangular solve and none of them a factorization**:

    // densematrix.hpp:24-36
    mfem::DenseMatrix MatrixSqrt(const mfem::DenseMatrix &M);            // :24
    mfem::DenseTensor MatrixSqrt(const mfem::DenseTensor &T);            // :26
    mfem::DenseMatrix MatrixPow(const mfem::DenseMatrix &M, double p);   // :28
    mfem::DenseTensor MatrixPow(const mfem::DenseTensor &T, double p);   // :30
    double            SingularValueMax(const mfem::DenseMatrix &M);      // :32
    double            SingularValueMin(const mfem::DenseMatrix &M);      // :34
    mfem::DenseTensor Mult(const mfem::DenseTensor &A,
                           const mfem::DenseTensor &B);                  // :36

There is no `LU`/`Cholesky`/`Solve`/`trsv`/`TriangularSolve` in the module
(`densematrix.cpp` grep for `Factor|LU|Cholesky|GETRS|trsv|TriangularSolve|Solve`
returned nothing). The module does dense matrix functions (sqrt/pow via
eigen-decomposition) and products, **never a triangular substitution**.

A separate exhaustive whole-tree codemap text search for
`trsv|trsm|TriSolve|TriangularSolve|SpTrSV` returned **zero hits anywhere in
Palace**. A repo-wide grep for any GS / SOR / ILU / IC smoother class
(`class …(GaussSeidel|SOR|ILU|IncompleteLU|IC0|Cholesky)…Smoother`) likewise
returned **zero hits** — no Palace-authored GS / SOR / ILU / IC smoother
class exists.

### (b) Where triangular solves occur — only inside opaque library calls

**(b1) HYPRE-internal Gauss-Seidel / SSOR relaxation sweeps.** The only
Gauss-Seidel / SOR relaxation in a Palace run is selected by an integer config
flag passed into the opaque HYPRE library. The actual forward/back substitution
sweeps live inside HYPRE; Palace authors **no** triangular substitution here:

    // amg.cpp:19
    int relax_type = 8;  // 8 = l1-symm. GS, 13 = l1-GS, 18 = l1-Jacobi, 16 = Chebyshev
    if (mfem::Device::Allows(mfem::Backend::DEVICE_MASK))
    {
      // Modify options for GPU-supported features.
      agg_levels = 0;
      relax_type = 18;                                                    // :24  GPU: GS -> Jacobi
    }
    ...
    HYPRE_BoomerAMGSetRelaxType(*this, relax_type);                       // :29

    // ams.cpp:162
    int relax_type = 2;  // 2 = l1-SSOR, 4 = trunc. l1-SSOR, 1 = l1-Jacobi, 16 = Chebyshev
    ...
    HYPRE_AMSSetSmoothingOptions(ams, relax_type, ams_smooth_it,          // :173
                                 weight, omega);
    ...
    // ams.cpp:158  (AMG sub-relax inside AMS)
    int amg_relax_type = 18;  // 3 = GS, 6 = symm. GS, 8 = l1-symm. GS, 13 = l1-GS,
                              // 18 = l1-Jacobi, 16 = Chebyshev
    ...
    // ams.cpp:179  (coarse-grid relax)
    int coarse_relax_type = 9;  // Default, l1-symm. GS, 9 = Gaussian elimination

These integer enums select one of HYPRE's internal relaxation kernels. The
triangular substitution that a GS / SOR / SSOR sweep performs is opaque-
library-owned — Palace ships a comment listing the available enum codes and a
single setter call. The GPU branch at `amg.cpp:24` flipping `relax_type` from
`8` (l1-symm. GS) to `18` (l1-Jacobi) is itself negative-anchor evidence: the
GS triangular sweep is sequential and GPU-hostile, so Palace's GPU default is
the diagonal-only Jacobi smoother instead.

**(b2) Palace-authored smoothers are GS-free.** The Palace-native smoother
cohort contains **no** triangular relaxation:

    // jacobi.hpp:19
    template <typename OperType>
    class JacobiSmoother : public Solver<OperType>     // diagonal-only

    // chebyshev.hpp:23
    template <typename OperType>
    class ChebyshevSmoother : public Solver<OperType>  // matrix-free polynomial

    // chebyshev.hpp:82  (immediately above the ChebyshevSmoother1stKind class)
    // Reference: Adams et al., Parallel multigrid smoothing: polynomial
    //            versus Gauss–Seidel, JCP (2003).

The Chebyshev citation is load-bearing for this obstruction: Palace explicitly
adopts polynomial smoothing **in place of** Gauss-Seidel — the GS triangular
sweep is a recognized non-liftable, non-parallelizable kernel that Palace
engineered around. Combined with the GPU GS→Jacobi flip at `amg.cpp:24`, this
is direct evidence that the absence of a Palace-authored triangular solve is
**deliberate**, not accidental.

**(b3) Direct-solver factorizations are external-library wrappers.** The full
LU / Cholesky factorizations whose forward/back substitution *is* a triangular
solve live entirely inside external libraries; Palace only wraps them:

    // strumpack.hpp:18-21
    // A wrapper for the STRUMPACK direct solver package.
    template <typename OperType>
    class StrumpackSolverBase : public StrumpackSolverType  // wraps mfem::STRUMPACKSolver

    // superlu.hpp:22
    class SuperLUSolver : public mfem::Solver

    // mumps.hpp:21
    class MumpsSolver : public mfem::MUMPSSolver

The triangular substitutions inside these factorizations are owned by
STRUMPACK / SuperLU / MUMPS (and ultimately out of scope as opaque-library
kernels per CLAUDE.md §Target system — "cite Palace source, not vendored
upstream"). Palace authors the wrapper class declarations; the substitution
itself is opaque-library-owned.

### (c) Red herring: the "block lower-triangular preconditioner" is NOT a scalar triangular solve

`palace/linalg/blockprecond.hpp:16-29` defines `BlockDiagonalPreconditioner`
with an optional lower off-diagonal `L10`, applied as a 2×2 **block** forward
substitution:

    // blockprecond.hpp:16-29
    // Block lower-triangular preconditioner for a 2-block system:
    //
    //   P = [P0      0 ]
    //       [L10    P1 ]
    //
    // where P0 and P1 are sub-solvers for the diagonal blocks, and L10 is
    // the lower off-diagonal operator (not owned). When L10 is null, this
    // reduces to a block-diagonal preconditioner.
    //
    // Application (forward solve of P z = r):
    //   z0 = P0^{-1} r0
    //   z1 = P1^{-1} (r1 - L10 z0)

The "forward solve" here applies the diagonal sub-solvers `P0` and `P1` to
**whole blocks** — it is block-structured Gaussian elimination at the 2-block
level, not an element-wise triangular substitution against matrix entries.
The same block-triangular concept appears at `modeeigensolver.cpp:448` and
`modeeigensolver.hpp:245`. This is a **red herring** for the `trsv`
obstruction (it should not be conflated with a triangular-solve primitive)
and is documented here as a non-example so a future search for "triangular"
in Palace does not falsely conclude the obstruction is filled by it.

## Applicability conditions

This is an obstruction theme; the "applicability" question is the *boundary
of the obstruction* — when does the negative finding apply?

1. **The general triangular-solve operator** (sparse or dense; acting on the
   length-`N` field; the BLAS-2 `TRSV` / `TRSM` shape, or the
   `sparse_triangular_solve` / GS / SOR / ILU smoother kernel shape) — **no
   positive Palace source site**. Obstruction applies. Do not author a firm
   L1 operator for this shape.
2. **The small-dense upper-triangular GMRES / FGMRES restart-correction
   back-substitution** (coordinate-space, dimension `j+1` ≤ `max_dim`, no
   collective) — has a positive Palace source site and is firm at L1
   ([`back_solve`](../L1/back_solve.md), cycle-027). Obstruction does **not**
   apply. The two are siblings on the "triangular solve" axis, split by the
   dense-small-coordinate vs sparse-large-field representation/cost
   distinction (the same split that separates [`lu_solve`](../L1/lu_solve.md)
   from [`ksp_solve`](../L1/ksp_solve.md) on the broader "solve a linear
   system" axis).
3. **A 2×2 block forward solve where the off-diagonal `L10` is an opaque
   linear operator** (`blockprecond.hpp:16-29`) — applies sub-solvers to
   whole blocks; not a scalar triangular substitution. Obstruction does not
   apply, but only because this is not a triangular-solve primitive at all
   (red herring, recorded so the absence is not mistakenly filled by it).
4. **Triangular sweeps inside HYPRE / STRUMPACK / SuperLU / MUMPS internal
   kernels** — the substitution exists in the running process but is owned by
   the external library. Obstruction applies on the Palace side (no
   Palace-authored kernel); the external-library kernel is out of scope per
   CLAUDE.md §Target system.

The obstruction is **load-bearing** (not incidental): Palace's deliberate
adoption of polynomial Chebyshev smoothing over Gauss-Seidel
(`chebyshev.hpp:82` citing Adams et al. 2003) and the GPU AMG default flip
from GS to Jacobi (`amg.cpp:24`) document an engineering choice to avoid the
triangular sweep, motivated by its non-parallelizability. Were a downstream
overlay to *want* a triangular solve for a tensor backend, it would face the
same obstruction Palace did and would, by construction, choose a polynomial
or Jacobi alternative — exactly the substitution Palace has already made.

## Justification kind

`obstruction` — **negative-result theme**. The L1 form for a general
triangular-solve operator is *recognised* (literature-standard `trsv` shape)
and the L0 anchor in Palace is **empty for it**; the substitution exists in
Palace runs only inside opaque library calls. The theme exists as
**citation-grounded documentation** that the general `trsv` primitive has no
home in Palace, not as an active lowering rule. Follows the cycle-004
[`minres-iteration`](./minres-iteration.md) and
[`bicgstab-iteration`](./bicgstab-iteration.md) precedents in form (negative
anchors only, no constructive L1 operator promoted).

The structural distinction from those two precedents: MINRES / BiCGStab are
**enum-only stubs** (`KrylovSolver::MINRES` / `KrylovSolver::BICGSTAB` declared
in the config enum and routed to `MFEM_ABORT` at `ksp.cpp:53-57`) — a user
can name them in JSON, but every call aborts. The `trsv` obstruction has **no
analogous user-facing token** to abort on — Palace does not expose a config
knob for "use a triangular solve" because there is no triangular-solve
primitive at all. The obstruction is on the *implementation surface*, not on
the *user-facing configuration surface*.

## Speculative L1 operators

**None proposed.** Per the CLAUDE.md §Scope policy on unimplemented Palace
components — "do not target the unimplemented functionality for filling in"
— this theme proposes no constructive L1 operator. A literature-anchored
`trsv` form *may* later inform higher abstractions if it would simplify an
L2 / L4 combinator, but no current upstream consumer would be simplified by
promoting it: the consumers Palace uses (HYPRE relaxation, external
factorizations, polynomial smoothing) do not factor through a `trsv` leaf in
the artifact. The harvester should **not** promote a speculative `trsv`
operator on the basis of this theme.

## Related

The same negative result (the absence of a Palace-authored general
triangular-solve primitive) is **also** recorded by the Phase 1 slice
[`sparse_triangular_solve`](../spec/slices/sparse_triangular_solve.md)
(registered at `book/src/SUMMARY.md:146`), which the cycle-013+ corpus-
reduction policy classifies as an **annotated-and-retained negative-result
slice** (a "the slice IS the artifact" case, per its reduction-status
header). That slice is the **canonical instance** of two concept pages:

- [`scope-out-obstruction`](../concepts/scope-out-obstruction.md) §"Canonical
  instance" (`:68`) — the L0→L1 scope-out obstruction (Palace forwards
  sparse-direct solves into MFEM / SuperLU_DIST / STRUMPACK / MUMPS opaquely;
  no Palace-level triangular-solve form to lift).
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) §"Sub-kind:
  out-of-scope-obstruction" (`:53`) — the out-of-scope sub-kind distinguished
  from genuine L2→L3 sequential obstruction.

This L1>L0 theme and the Phase 1 slice carry **overlapping L0 anchors**
(four shared sites — `superlu.hpp`, `strumpack.hpp`, `mumps.hpp`,
`blockprecond.hpp` red-herring); the relationship is:

- The **slice** is the Phase-1-era canonical-instance record (the original
  dissection that produced the negative result, plus the wrapper-level
  carry-through into `apply_linop` / `ksp_solve`).
- This **L1>L0 theme** is the layered-artifact home for the negative result
  in the post-structural-redirect cohort, sitting alongside
  [`minres-iteration`](./minres-iteration.md) and
  [`bicgstab-iteration`](./bicgstab-iteration.md) as the third obstruction-
  flavoured L1>L0 theme. It additionally records the engineered-absence
  evidence (Adams-2003 + GPU GS→Jacobi flip) that postdates the slice.

The two records cross-link rather than supersede; the slice's reduction
status remains **annotated-and-retained** and is not closed by this theme.
See the §"Open questions / caveats" entry on Phase-1-slice-reduction
candidacy below for the follow-up.

## Verified-against

L0 evidence ranges (all are **absence** / **negative-anchor** citations; this
is by design for an obstruction theme):

- `palace/linalg/densematrix.hpp:24-36` — the full small-dense matrix utility
  API; no triangular solve, no factorization. The absence of `LU`/`Cholesky`/
  `Solve`/`trsv` in the module is the absence anchor.
- `palace/linalg/amg.cpp:19` — `int relax_type = 8;  // 8 = l1-symm. GS, 13
  = l1-GS, 18 = l1-Jacobi, 16 = Chebyshev` — the config-flag enumeration that
  selects HYPRE's internal GS / Jacobi / Chebyshev relaxation kernel.
- `palace/linalg/amg.cpp:24` — `relax_type = 18;` (the GPU branch flipping
  from GS to l1-Jacobi) — load-bearing negative anchor: the GS triangular
  sweep is GPU-hostile, so Palace's GPU default avoids it.
- `palace/linalg/amg.cpp:29` — `HYPRE_BoomerAMGSetRelaxType(*this,
  relax_type);` — the setter call handing the enum to opaque HYPRE.
- `palace/linalg/ams.cpp:158` — `int amg_relax_type = 18;` — AMS internal
  AMG sub-relax type (l1-Jacobi default).
- `palace/linalg/ams.cpp:162` — `int relax_type = 2;  // 2 = l1-SSOR, 4 =
  trunc. l1-SSOR, 1 = l1-Jacobi, 16 = Chebyshev` — the AMS smoother config
  enumeration that selects HYPRE's internal SSOR / Jacobi / Chebyshev
  relaxation.
- `palace/linalg/ams.cpp:173` — `HYPRE_AMSSetSmoothingOptions(ams,
  relax_type, ams_smooth_it, weight, omega);` — the setter call handing the
  enum to opaque HYPRE-AMS.
- `palace/linalg/ams.cpp:179` — `int coarse_relax_type = 9;  // Default,
  l1-symm. GS, 9 = Gaussian elimination` — coarse-grid relaxation choice; the
  default `9` selects Gaussian elimination (HYPRE-internal direct solve), not
  a Palace-authored triangular kernel.
- `palace/linalg/jacobi.hpp:19` — `class JacobiSmoother` — the Palace-native
  diagonal-only smoother; no triangular sweep.
- `palace/linalg/chebyshev.hpp:23` — `class ChebyshevSmoother` — the
  Palace-native polynomial smoother; no triangular sweep.
- `palace/linalg/chebyshev.hpp:82` — `// Reference: Adams et al., Parallel
  multigrid smoothing: polynomial versus Gauss-Seidel, JCP (2003).` — the
  load-bearing citation documenting Palace's deliberate choice of polynomial
  smoothing over Gauss-Seidel.
- `palace/linalg/strumpack.hpp:18` — `// A wrapper for the STRUMPACK direct
  solver package.`; `palace/linalg/strumpack.hpp:21` — `class
  StrumpackSolverBase` — external-library wrapper; the triangular
  substitution inside the factorization is opaque to Palace.
- `palace/linalg/superlu.hpp:22` — `class SuperLUSolver : public mfem::Solver`
  — external-library wrapper.
- `palace/linalg/mumps.hpp:21` — `class MumpsSolver : public mfem::MUMPSSolver`
  — external-library wrapper.
- `palace/linalg/blockprecond.hpp:16-29` — `// Block lower-triangular
  preconditioner for a 2-block system: …  Application (forward solve of
  P z = r): z0 = P0^{-1} r0; z1 = P1^{-1} (r1 - L10 z0)` — the red-herring
  non-example: a 2×2 BLOCK forward solve applying sub-solvers to whole blocks,
  NOT a scalar triangular substitution.

Two exhaustive whole-tree zero-hit codemap text searches (cycle-028
harvester, critic-reproduced):

- `trsv|trsm|TriSolve|TriangularSolve|SpTrSV` — **zero hits anywhere in the
  Palace tree** (the negative finding's primary basis).
- `class …(GaussSeidel|SOR|ILU|IncompleteLU|IC0|Cholesky)…Smoother` — **zero
  hits** (no Palace-authored GS / SOR / ILU / IC smoother class exists).

Sibling firm L1 evidence (positive — used to make the sibling distinction
concrete, NOT to anchor this obstruction):

- [`book/src/L1/back_solve.md`](../L1/back_solve.md) — the firm c027
  small-dense upper-triangular GMRES / FGMRES restart-correction
  back-substitution; the **one** triangular-system component Palace DOES
  implement. Coordinate-space dense, dimension `j+1` ≤ `max_dim`, no
  collective. Distinct from a general `trsv` (which would act on the
  length-`N` field).
- [`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md)
  (cycle-029 dispatch-1; sibling theme landed in the same cycle as this one).
  The L1>L0 rotation of `back_solve` into its L0 in-place back-substitution
  loop; also small-dense only, not a general `trsv`.

    verified_against:
      - citation: reference/palace/palace/linalg/densematrix.hpp:24-36
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: full small-dense matrix utility API (MatrixSqrt/MatrixPow/SingularValue*/Mult); no triangular solve, no factorization; in-range bound zero-drift.
      - citation: reference/palace/palace/linalg/amg.cpp:19
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: HYPRE BoomerAMG relax_type enum comment "8 = l1-symm. GS, 13 = l1-GS, 18 = l1-Jacobi, 16 = Chebyshev"; the triangular substitution is HYPRE-internal; citecheck --anchor 'l1-symm. GS' zero-drift.
      - citation: reference/palace/palace/linalg/amg.cpp:24
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "GPU branch `relax_type = 18;` flipping from GS (8) to l1-Jacobi — load-bearing: documents that GS is GPU-hostile, justifying the Palace-engineered avoidance; citecheck --anchor 'relax_type = 18' zero-drift."
      - citation: reference/palace/palace/linalg/amg.cpp:29
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`HYPRE_BoomerAMGSetRelaxType(*this, relax_type);` — the setter handing the enum to opaque HYPRE; citecheck --anchor 'HYPRE_BoomerAMGSetRelaxType' zero-drift."
      - citation: reference/palace/palace/linalg/ams.cpp:158
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "AMS internal `int amg_relax_type = 18;` (l1-Jacobi default); citecheck --anchor 'amg_relax_type' zero-drift."
      - citation: reference/palace/palace/linalg/ams.cpp:162
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: HYPRE AMS smoother relax_type enum comment "2 = l1-SSOR, 4 = trunc. l1-SSOR, 1 = l1-Jacobi, 16 = Chebyshev"; the SSOR triangular substitution is HYPRE-AMS-internal; citecheck --anchor 'l1-SSOR' zero-drift.
      - citation: reference/palace/palace/linalg/ams.cpp:173
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`HYPRE_AMSSetSmoothingOptions(ams, relax_type, ams_smooth_it, weight, omega);` — the setter handing the enum to opaque HYPRE-AMS; citecheck --anchor 'HYPRE_AMSSetSmoothingOptions' zero-drift."
      - citation: reference/palace/palace/linalg/ams.cpp:179
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`int coarse_relax_type = 9;  // Default, l1-symm. GS, 9 = Gaussian elimination` — coarse-grid relax default (HYPRE-internal Gaussian elimination, not Palace-authored); citecheck --anchor 'coarse_relax_type' zero-drift."
      - citation: reference/palace/palace/linalg/jacobi.hpp:19
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`class JacobiSmoother` — Palace-native diagonal-only smoother (no triangular sweep); citecheck --anchor 'JacobiSmoother' zero-drift (re-anchored from the c028 report's `:15` after off-by-4 drift)."
      - citation: reference/palace/palace/linalg/chebyshev.hpp:23
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`class ChebyshevSmoother` — Palace-native polynomial smoother (no triangular sweep); citecheck --anchor 'ChebyshevSmoother' zero-drift."
      - citation: reference/palace/palace/linalg/chebyshev.hpp:82
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "Adams et al. 2003 citation comment 'polynomial versus Gauss-Seidel' — load-bearing: documents Palace's deliberate choice of polynomial smoothing over GS; citecheck --anchor 'polynomial versus Gauss' zero-drift."
      - citation: reference/palace/palace/linalg/strumpack.hpp:18
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "wrapper-class comment '// A wrapper for the STRUMPACK direct solver package.' — external-library wrapper; triangular substitution opaque to Palace; citecheck --anchor 'STRUMPACK' zero-drift."
      - citation: reference/palace/palace/linalg/strumpack.hpp:21
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`class StrumpackSolverBase` declaration — external-library wrapper; citecheck --anchor 'StrumpackSolverBase' zero-drift."
      - citation: reference/palace/palace/linalg/superlu.hpp:22
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`class SuperLUSolver : public mfem::Solver` — external-library wrapper; citecheck --anchor 'SuperLUSolver' zero-drift."
      - citation: reference/palace/palace/linalg/mumps.hpp:21
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: "`class MumpsSolver : public mfem::MUMPSSolver` — external-library wrapper; citecheck --anchor 'MumpsSolver' zero-drift."
      - citation: reference/palace/palace/linalg/blockprecond.hpp:16-29
        verdict: negative-anchor
        audited_at: 2026-05-29T234506Z
        note: 'red-herring non-example — 2x2 BLOCK forward solve "z0 = P0^{-1} r0; z1 = P1^{-1}(r1 - L10 z0)" applying sub-solvers to whole blocks, NOT a scalar triangular substitution; citecheck --anchor "Block lower-triangular" zero-drift (anchor at line 16 within range 16-29).'
      - citation: book/src/L3/index.md:7
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: the L3 Context paragraph that names "certain triangular solves" as canonical L3 obstructions; this L1>L0 theme is the concrete L0 evidence behind that note.
      - citation: book/src/L1/back_solve.md
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: firm c027 small-dense GMRES/FGMRES restart-correction back-substitution — the sibling distinction (NOT a general trsv; coordinate-space, dimension j+1 ≤ max_dim).
      - citation: book/src/L1-L0/minres-iteration.md
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: cycle-004 obstruction-theme precedent (MFEM_ABORT-anchored); justification-kind/structure followed.
      - citation: book/src/L1-L0/bicgstab-iteration.md
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: cycle-004 obstruction-theme precedent (MFEM_ABORT-anchored, with verified_against negative-anchor YAML); YAML shape followed.
      - citation: book/src/spec/slices/sparse_triangular_solve.md
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: Phase 1 negative-result slice covering the same triangular-solve absence (canonical-instance home for `scope-out-obstruction` and `sequential-obstruction` out-of-scope sub-kind); registered at `book/src/SUMMARY.md:146`; overlapping L0 anchors (superlu / strumpack / mumps / blockprecond red-herring). Annotated-and-retained per cycle-013+ corpus-reduction policy; cross-linked, not superseded, by this L1>L0 theme.
      - citation: book/src/concepts/scope-out-obstruction.md:68
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: concept page §"Canonical instance" line cites the `sparse_triangular_solve` slice as the L0→L1 scope-out obstruction canonical instance; this L1>L0 theme is the layered-artifact partner record.
      - citation: book/src/concepts/sequential-obstruction.md:53
        verdict: positive-cross-reference
        audited_at: 2026-05-29T234506Z
        note: concept page §"Sub-kind: out-of-scope-obstruction" line distinguishes the out-of-scope sub-kind from genuine L2→L3 sequential obstruction; the `sparse_triangular_solve` slice is the canonical instance and this L1>L0 theme cross-links it.

## Status

`obstruction` — claim-free documentation of the absence of a general
triangular-solve primitive in Palace, with negative anchors. **Not
`rough-in`** (no constructive L1 form is proposed and none should be —
per CLAUDE.md §Scope, unimplemented Palace components are not direct
implementation targets) and **not `firm`** (there is no positive L0 anchor
to firm against; obstruction is the terminal status). Mirrors the
[`minres-iteration`](./minres-iteration.md) /
[`bicgstab-iteration`](./bicgstab-iteration.md) cycle-004 precedents.

Resolves the `trsv` leaf of OQ `l3-vocabulary-inventory-gap`
(`scaffolding/open-questions.md`) as **resolved-by-obstruction** rather than
perpetually BLOCKED: the L3 index's `:7` "certain triangular solves" line now
has a citable concrete L0-evidence home in this theme, and the absence of any
Palace-authored `trsv` is documented with negative anchors. Does **not**
close the entry by promoting a `trsv` L1 operator (the obstruction is the
*resolution*, not a precursor to a constructive entry).

Open follow-up for layer-intro-author (out of this dispatch's scope): the
L3 index's `:7` line may want a back-reference to this theme file once it
lands, paralleling the `eigsolve` partial-obstruction cross-reference at
`:31`/`:45`. Not blocking for this theme.
