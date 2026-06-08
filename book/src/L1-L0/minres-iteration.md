# minres-iteration

The MINRES (Minimum Residual; Paige–Saunders 1975) Krylov iteration for
symmetric-indefinite linear systems. **Obstruction-flavoured theme** —
Palace exposes a `KrylovSolver::MINRES` enum tag but `MakeSolver` aborts
on it at runtime; there is no Palace-side L0 implementation to rewrite
into. The L1 form is sketched against the literature so that downstream
work has a hook, but the rewrite has no realised RHS in the Palace
corpus.

## Slug

`minres-iteration`

## L1 form (LHS)

The MINRES outer iteration is structurally identical to GMRES but with the
Arnoldi step specialised to a **symmetric Lanczos three-term recurrence**
(the upper-Hessenberg matrix collapses to a symmetric tridiagonal; the
orthogonalisation loop in the Arnoldi step is replaced by two `dot+axpy`
pairs against `V[j-1]` and `V[j]` only). The outer least-squares update
acts on a band of width 3 rather than a dense Hessenberg column, but the
running-QR / Givens-rotation structure of
[`incremental_least_squares`](../concepts/incremental_least_squares.md)
is reused unchanged.

Speculative L1 per-step form (rough-in operators below):

    -- state: (V_prev, V_curr, alpha_curr, beta_curr, qr_state, s_residual)
    -- input: A  : LinOp                  -- system operator (symmetric, possibly indefinite)
    --        B  : LinOp (optional, SPD)  -- left preconditioner (preserves symmetry only if SPD)
    state_next = lanczos_step(A, B, state)            -- 3-term recurrence
        |> three_term_recurrence_update                -- emit (alpha, beta_prev, beta_curr) band column
        |> givens_apply_with_residual_min              -- band-width 3 Givens cascade; |s| is the LS residual

The full MINRES iteration is the unfolded fixpoint
`fold(lanczos_step, init_state)` with `s_residual < tol · beta_0`
termination, identical in shape to the GMRES outer loop modulo
band-vs-Hessenberg width.

## L0 form (RHS)

**Empty — no Palace site.**

The L0 anchor for the theme is the *absence* at the dispatch site:

    // [palace/linalg/ksp.cpp:53-57]
    case KrylovSolver::MINRES:
    case KrylovSolver::BICGSTAB:
    case KrylovSolver::DEFAULT:
      MFEM_ABORT("Unexpected solver type for Krylov solver configuration!");
      break;

The factory enumerates MINRES alongside CG/GMRES/FGMRES but routes it to
`MFEM_ABORT`. The config-file enum (`utils/labels.hpp:108`) and the
JSON-string mapping (`utils/configfile.cpp:129`) likewise carry a
`"MINRES"` token; both are observable to a user but result in an
abort. There is no construction site, no `MinresSolver<OperType>` class
under `palace/linalg/`, and no test linkage.

Were MINRES to be added, two structural integrations would be possible:

1. **In-tree implementation under `palace/linalg/iterative.cpp`** — a
   `MinresSolver<OperType>` class with `Mult` shaped like the existing
   `GmresSolver::Mult` (`iterative.cpp:614-642`) but with the Arnoldi
   inner body replaced by the Lanczos three-term recurrence. The
   speculative L1 operators below presume this realisation.
2. **MFEM-substrate adoption** — wrap `mfem::MINRESSolver` via the
   wrapper pattern of `MakeWrapperSolver` (`ksp.cpp:103-`). In this
   reading, MFEM is the L0 substrate; the abstractor would re-target
   the theme against vendored MFEM source (not currently checked into
   `reference/`). See Open questions.

## Applicability conditions

If MINRES is added to Palace, the L1>L0 rewrite is valid when:

1. **System symmetry**. `A = Aᵀ` (real) or `A = Aᴴ` (complex Hermitian).
   Without symmetry the Lanczos three-term recurrence loses its
   orthogonality property and MINRES no longer minimises the residual
   over the Krylov subspace.
2. **Preconditioner SPD**. If `B` is supplied, it must be symmetric
   positive definite, otherwise the preconditioned operator `BA`
   (`B`-inner-product Lanczos) is not symmetric in the `B`-inner-product
   and the recurrence breaks. (Unlike GMRES, MINRES cannot accept
   indefinite preconditioning.)
3. **No mid-iteration restart**. Unlike GMRES, MINRES has no restart
   parameter — the three-term recurrence stores only `V_prev, V_curr`,
   so the basis-storage growth that motivates GMRES restarts is absent.
4. **Breakdown handling**. `beta_curr == 0` is hard breakdown (the
   Krylov subspace is `A`-invariant; the iterate is exact). Palace's
   `iterative.cpp` `CheckDot` pattern (`iterative.cpp:643`) is the
   structural analogue, were the kernel implemented.

## Justification kind

`obstruction` — the L1 form has a clean three-term-recurrence shape and
the rewrite *would* be `structural` (the lift from a Lanczos kernel into
the pure-functional form mirrors `arnoldi-step` exactly), but the L0
side is empty: Palace does not implement the solver. The theme records
this as a first-class negative result rather than synthesising an L1
form without a Palace anchor.

The closely-related affirmative theme would be `arnoldi-iteration` (GMRES
outer loop; not yet sketched); when it lands, MINRES becomes a thin
variant axis of it — the Lanczos recurrence is the symmetric
specialisation of Arnoldi, and the band-width-3 LS update is the
sparsified specialisation of the running QR. The variant absorption is
recorded for future use; firming it requires either a Palace
implementation or an explicit decision to treat MFEM as L0 substrate.

## Speculative L1 operators

- `lanczos_step` — rough-in. Sibling of the planned `arnoldi_step`
  operator (`concepts/dependency-map.md:68-72`, currently `:::planned`).
  See Speculative operators proposed section for signature sketch.
- `three_term_recurrence_update` — rough-in. The band-column emission
  step; produces a 3-entry slice of a symmetric tridiagonal `T_j` each
  iteration.
- `givens_apply_with_residual_min` — rough-in. The band-width-3
  specialisation of the running-QR step in
  [`incremental_least_squares`](../concepts/incremental_least_squares.md);
  the LS residual `|s|` falls out of the Givens cascade as for GMRES,
  but only the last 3 entries of `s` are touched per step.

## Evidence

L0 evidence ranges (all are *absence* citations; this is by design for
an obstruction theme):

- `palace/linalg/ksp.cpp:53-57` — `KrylovSolver::MINRES` enum case
  routed to `MFEM_ABORT`. **No construction**.
- `palace/utils/labels.hpp:104-112` — `KrylovSolver` enum definition;
  `MINRES` is item 3 of 6.
- `palace/utils/configfile.cpp:129` — JSON-string `"MINRES"` mapping;
  user-facing token exists, factory rejects.

No test linkage exists (no `test/unit/test-minres*` in
`reference/palace/test/`). No Palace site under `palace/linalg/`
implements a `MinresSolver`-shaped class.

Structural sibling (affirmative L1 evidence the rewrite would parallel):

- The Arnoldi inner-body kernel (`apply → orthog → norm → scal`; firm L0 home
  `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop)
  is the structural parent of the Lanczos three-term recurrence; one-line variant axis
  (`gs_orthog` → fixed-to-symmetric) collapses Arnoldi to Lanczos.
- `book/src/concepts/incremental_least_squares.md` — the running-QR
  pattern; MINRES is the band-3 specialisation.

## Status

`rough-in` — sketched as `obstruction` per the absence in Palace; the
three speculative L1 operators are flagged for harvester promotion only
if and when a Palace-side site materialises, or when an integrator
decision is made to widen L0 to include vendored MFEM.
