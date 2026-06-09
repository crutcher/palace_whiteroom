---
layer: L1
operator: multigrid-relaxation-smoother
firmness: firm
# Graded-stack scheme: this L1 entry is the kernel-IMPLEMENTATION node (DIRECTIVE-3) —
# the constructive realization of the multigrid relaxation slot. It carries a
# normal rank/status (firm on the firm-on-positive-structure escape) and the `## Status`
# role-label `kernel-impl`. The `realizes-kernel-api` edge to the KEPT
# `triangular-solve-obstruction` theme is `reference`-class (navigational, free): the impl
# does NOT depend-on the opaque API, so that edge constrains neither rank nor liveness.
# The blocking `depends-on` edges below are to its from-our-firm-primitives constituents
# (all firm on disk → well-foundedness firm/firm holds).
rank: firm
edges:
  depends-on:
    - target: L1/chebyshev-smoother    # the primary + auxiliary point smoothers B, B_G
      kind: uses
    - target: L1/apply_linop           # the matvec A·y (residual) and Gᵀ·r / G·y_G transfers
      kind: uses
    - target: L1/axpby                 # the residual combine r = 1·x − 1·(A·y)
      kind: uses
    - target: L1/interpolator          # the de-Rham discrete-gradient G (and its transpose Gᵀ)
      kind: uses
  reference:
    - target: L1-L0/triangular-solve-obstruction
      kind: realizes-kernel-api        # DIRECTIVE-3: the kept opaque GS-SSOR kernel-api this impl realizes (free, NOT depends-on)
    - L1/set_subvector_zero            # the essential-dof pin on the auxiliary residual x_G (consumed-by, not a spine dep)
    - concepts/sequential-obstruction  # the outer pc_it relaxation-sweep recurrence (documented non-law)
    - L4/preconditioning-framework     # the multigrid V-cycle consumer that installs this as per-level smoother
    - L2/correction_step               # DOWNWARD annotation: each per-sweep leg (primary B; auxiliary conjugated G·B_G·Gᵀ) is the L1 realization of the L2 correction_step combinator. NOT a depends-on (L1 cannot depend UP on L2); reference-class navigational.
---

# multigrid-relaxation-smoother

Constructive **kernel-implementation** of the multigrid relaxation slot: a
pure-functional relaxation action
`y' = multigrid_relaxation_smoother(op, x, y, initial_guess)` realizing the
**Hiptmair distributive relaxation smoother**. It is the in-our-semantics
realization that the general GS-SSOR / sparse-triangular relaxation kernel-API
([`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md))
names but Palace deliberately does not author as a triangular sweep. Instead of a
Gauss-Seidel forward/back substitution, the relaxation is built from a
**primary-space point smoother** plus an **auxiliary-space (gradient) correction**
threaded through the de-Rham discrete gradient — every piece a firm L1 primitive.

## Context

This node is the **`kernel-impl`** half of the DIRECTIVE-3 kernel-API/impl pair
(CLAUDE.md §Methodology-invariants "Kernel-API vs
kernel-IMPLEMENTATION distinction"). The **kernel-api** half is the kept
[`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) theme
(`obstruction (opaque-library-ownership)`), which documents the opaque contract:
a general sparse-triangular relaxation sweep
(`trsv` / `SpTrSV` / GS / SOR / SSOR) over the length-`N` field is the
*kernel the multigrid smoother slot calls*, but **no positive Palace source site
authors it** — the only GS/SSOR sweeps in a Palace run live inside HYPRE, selected
by an integer enum (`amg.cpp:19`, `ams.cpp:162`). This impl node does NOT
`depends-on` that opaque API; it `realizes-kernel-api` it (a `reference`-class
correspondence, reviewed by `lowering-verifier`, that constrains neither rank nor
liveness). A reviewer reads BOTH and confirms they match.

The relaxation slot has a *positive* Palace realization that this node lifts: the
`DistRelaxationSmoother<OperType>` class
(`palace/linalg/distrelaxation.cpp:13-36` ctor, `:38-69` `SetOperators`,
`:101-119` `Mult2`, header `palace/linalg/distrelaxation.hpp:23-30`). Per the
header comment it is the **Hiptmair distributive relaxation smoother** (Hiptmair,
*Multigrid method for Maxwell's equations*, SIAM J. Numer. Anal. 1998,
`distrelaxation.hpp:23-28`): a smoother for H(curl) problems that relaxes the
operator `A` in the primary Nedelec space AND its projection
`A_G = GᵀAG` into the auxiliary (scalar-potential / gradient) space, where `G` is
the discrete gradient. The two point-smoothers `B`, `B_G` are
`ChebyshevSmoother` instances (`distrelaxation.cpp:21-34`) — so the realized
relaxation is **GS-free by construction**, exactly the engineered-around choice
the kernel-api theme documents (Adams 2003 polynomial-over-Gauss-Seidel,
`chebyshev.hpp:82`).

This is a **constructed-operator gate** at L1, in the family of
[`chebyshev-smoother`](./chebyshev-smoother.md) and
[`divfree_projector`](./divfree_projector.md): the primary argument `op` is a
structured opaque value built once at setup (the ctor + `SetOperators` step),
carrying the captured operators `A` / `A_G`, the discrete gradient `G`, the
auxiliary essential-dof set, the two point-smoother closures, and the fixed
sweep count `pc_it`. The L1 signature is variant-free; the 4th-kind vs 1st-kind
Chebyshev choice (`distrelaxation.cpp:20-34`) is absorbed into the closure's
point smoothers, exactly as `chebyshev-smoother` absorbs it into its own
`scalars` generator. The output-arg mutation idiom of the L0 `Mult2(x, y, r)`
(writes through `y`, scribbles `r`, `x_G`, `y_G`, `r_G`) is an L0 concern
reintroduced in the forthcoming L1>L0 lowering theme, not in the L1 signature.

The de-Rham structural pattern — relax in the primary space, correct through the
discrete gradient `G` into an auxiliary space — is the SAME shape as
[`divfree_projector`](./divfree_projector.md) (`I − Grad(GᵀMG)⁻¹GᵀM`): both
consume the [`interpolator`](./interpolator.md)-produced discrete gradient `G`
and apply a sub-operation in the gradient space. The distinction:
`divfree_projector` performs an exact auxiliary *solve* `(GᵀMG)⁻¹`, while this
smoother performs an inexact auxiliary *relaxation* `B_G` (a fixed-degree
Chebyshev sweep, not a solve to convergence).

## Signature

```text
multigrid_relaxation_smoother
  :: (op: DistRelaxSmoother[N, M], x: Tensor[N], y: Tensor[N], initial_guess: Bool)
     -> Tensor[N]

multigrid_relaxation_smoother(op, x, y, initial_guess) =
  iterate op.pc_it times, threading y:
    y := y + B   (x − A·y)            -- primary-space relaxation
    y := y + G · B_G · Gᵀ (x − A·y)   -- auxiliary-space (gradient) correction
```

Shape contract (bunsen-style; named axes — `Tensor[N]` is the genuinely-flat
rank-1 dof-vector at L1, per `book/src/semantics/index.md` §1.2.1 "reserve
`Tensor[N]` for genuinely-flat rank-1 dof-vectors at L1/L0"):

- `op` — `DistRelaxSmoother[N, M]` — the constructed distributive-smoother
  closure. `N` = primary (H(curl)/Nedelec) true-dof count; `M` = auxiliary
  (H1/gradient) true-dof count. Bound at setup; immutable across calls. See
  §Record definition for the fields.
- `x` — `Tensor[N]` — the right-hand-side / residual-source field in the primary
  space (the smoother's `b`). Read-only.
- `y` — `Tensor[N]` — the input iterate in the primary space (the current
  approximate solution being relaxed). Read-only in the pure form (the L0
  threads it as the in-place accumulator).
- `initial_guess` — `Bool` — when `false`, the first primary sweep treats the
  input `y` as zero (`B->SetInitialGuess(false)`, `distrelaxation.cpp:105`), a
  one-matvec saving on the leading residual; when `true`, the residual
  `x − A·y` is formed from the supplied `y`. A degenerate-case flag, not an
  algebraic-law variant.
- result — `Tensor[N]` — the relaxed iterate in the primary space.

The two relaxation legs per sweep (`distrelaxation.cpp:104-117`):

1. **Primary leg** (`:104-106`): `y := y + B (x − A·y)`. The point smoother `B`
   is applied to the primary operator `A`; with the input-guess flag set to
   `op.initial_guess || it > 0` (`:105`) so only the very first sweep may skip
   the leading residual.
2. **Auxiliary leg** (`:108-117`): form the primary residual `r = x − A·y`
   (`A->Mult(y, r)` `:109`, then `linalg::AXPBY(1.0, x, -1.0, r)` `:110`);
   restrict it to the auxiliary space `x_G = Gᵀ r` (`:111`); pin the auxiliary
   essential dofs to zero (`:112-115`); relax in the auxiliary space
   `y_G = B_G x_G` (`:116`); prolong the correction back and add
   `y := y + G y_G` (`:117`).

**Downward annotation (L1 → L2 navigational, NOT a dependency).** Both legs are
the L1 realization of the L2 [`correction_step`](../L2/correction_step.md)
combinator `y + B·(x − A·y)` (firm) with a different `B`-slot: the primary
leg is `correction_step A B x y` (B = the primary point smoother); the auxiliary
leg is `correction_step A (G·B_G·Gᵀ) x y` — the **conjugated** preconditioner
`B = T·B'·Tᵀ` with `T = G` (correction_step law 6, the de-Rham auxiliary-space
specialization). The two-leg sequence is multiplicative (the auxiliary leg reads
the post-primary residual; law 1 above). This is a **downward annotation only** —
NO `depends-on` edge to `correction_step` is created (an L1 form cannot depend UP
on an L2 abstraction, CLAUDE.md §"Layers are defined high→low"); this smoother is
already correctly grounded in the firm L1 primitives `apply_linop` + `axpby` that
`correction_step` itself decomposes into. The link is the combinator-primary
navigational back-reference.

## Record definition

`DistRelaxSmoother[N, M]` is used by **only this operator** (single consumer), so
it is defined in-chapter (the record-definition obligation, CLAUDE.md §Methodology
"Records/structs get a definition home"). It is the L1 reflection of the
`DistRelaxationSmoother<OperType>` private member set
(`palace/linalg/distrelaxation.hpp:34-51`):

    {
      A      : LinearOperator[N, N],   -- captured primary system operator (SetOperators, distrelaxation.cpp:49; hpp field :42)
      A_G    : LinearOperator[M, M],   -- the auxiliary projection GᵀAG (SetOperators, :50; hpp field :42)
      G      : LinOp[(N), (M)],        -- the de-Rham discrete gradient (ctor arg, distrelaxation.cpp:17; hpp field :39; produced by `interpolator`)
      B      : ChebSmoother[N],        -- primary-space point smoother closure (ctor, :23/:30; hpp field :46)
      B_G    : ChebSmoother[M],        -- auxiliary-space point smoother closure (ctor, :25/:32; hpp field :47; initial-guess pinned false, :35)
      ess_G  : DofSet[M],              -- auxiliary essential/Dirichlet true-dof set (SetOperators, :61 GetEssentialTrueDofs; hpp field dbc_tdof_list_G :43)
      pc_it  : Nat                     -- relaxation sweep count (ctor smooth_it, :17; hpp field :36)
    }

Strata:

- **Construction-time** (bound once at ctor + `SetOperators`, immutable across
  applies): `A`, `A_G`, `G`, `B`, `B_G`, `ess_G`, `pc_it`. `A` / `A_G` /
  `ess_G` are bound in `SetOperators` (`distrelaxation.cpp:49-50,61`); `G`, `B`,
  `B_G`, `pc_it` are bound in the ctor (`:13-36`).
- **Run-time**: none of the record fields. The L0 scratch vectors
  `x_G, y_G, r_G, r` (`distrelaxation.hpp:50`) are per-call mutable workspace,
  NOT part of the L1 record (they are the L0 mutation idiom reintroduced by the
  L1>L0 theme).

The backing C++ struct is the `DistRelaxationSmoother<OperType>` private section
(`palace/linalg/distrelaxation.hpp:34-51`); the `ChebSmoother[·]` element type of
`B` / `B_G` is the `chebyshev-smoother` record
([`chebyshev-smoother`](./chebyshev-smoother.md) §Record / Signature). The
`LinOp[(N), (M)]` discrete gradient `G` is the
[`interpolator`](./interpolator.md)-produced de-Rham grid-transfer operator
(Grad edge, H1→ND).

## Algebraic laws

Only laws that hold are stated; each is a syntactic identity on the fully-read
positive `Mult2` body (`distrelaxation.cpp:101-119`).

1. **Single-sweep decomposition** (`pc_it = 1`, `initial_guess = true`):
   `multigrid_relaxation_smoother(op, x, y, true)`
   `= (y + B(x − A·y)) + G·B_G·Gᵀ(x − A·(y + B(x − A·y)))`.
   The auxiliary leg's residual is formed AFTER the primary leg updates `y`
   (`A->Mult(y, r)` at `:109` reads the just-updated `y`) — the two legs do not
   commute; this is a **multiplicative** (Gauss-Seidel-between-spaces) composition,
   not additive Schwarz. (Holds: read directly from the ordered body.)
2. **Sweep iteration** (`pc_it = k`): the action is the `k`-fold self-composition
   of the single-sweep map with `initial_guess` forced `true` on sweeps `it > 0`
   (`distrelaxation.cpp:105`, `B->SetInitialGuess(this->initial_guess || it > 0)`).
   Each sweep reads the previous sweep's output `y` — a recurrence (see non-law NL1).
3. **Zero-residual fixed point**: if `A·y = x` and `Gᵀ(x − A·y) = 0` then
   `multigrid_relaxation_smoother(op, x, y, true) = y`. (Holds: both relaxation
   legs apply their smoother to a zero argument, and `B`, `B_G` are linear in
   their residual argument, so a zero residual yields a zero correction.)
4. **Auxiliary-leg linearity in the residual**: the correction
   `G·B_G·Gᵀ·r` is linear in the primary residual `r = x − A·y`. (Holds: `Gᵀ`,
   `B_G`, `G` are each linear maps — `interpolator`-produced `G` is linear
   (`interpolator` law "produced-op linearity"); `chebyshev-smoother`'s action
   is linear in its residual; the essential-dof pin `set_subvector_zero`
   (`:112-115`) is a linear projector `Z_ess`.)
5. **Initial-guess fast path** (`initial_guess = false`, first sweep): the
   leading primary residual is taken against `y = 0` rather than the supplied
   `y` (`B->SetInitialGuess(false)` at the first sweep, `:105`), saving one
   `A·y` matvec. The *result* equals the `initial_guess = true` action applied
   to `y = 0`. (Holds: `SetInitialGuess(false)` is the documented
   zero-iterate-skip of the point smoother, see
   [`chebyshev-smoother`](./chebyshev-smoother.md).)

Laws that do **NOT** hold (stated to bound the operator):

- **NOT additive between the two spaces.** The auxiliary leg reads the residual
  AFTER the primary leg's update (law 1), so the smoother is a multiplicative
  (sequential primary-then-auxiliary) composition, not `(I + B)·… + G B_G Gᵀ`
  applied to the same residual. Conflating the two changes the operator.
- **NOT symmetric in general.** `Mult2` (primary→auxiliary,
  `distrelaxation.cpp:101-119`) and `MultTranspose2`
  (auxiliary→primary→primary-transpose, `:121-151`) apply the legs in the
  REVERSED order with the transposed point smoothers `Bᵀ`, `B_Gᵀ`; the
  forward action is symmetric only if used as a forward+transpose pair (the
  SSOR-symmetric-sweep idiom). The single `Mult2` action alone is non-symmetric.

## Non-laws / load-bearing caveats

- **NL1 — outer `pc_it` relaxation-sweep is a witnessed sequential-obstruction.**
  The `for (int it = 0; it < pc_it; it++)` loop (`distrelaxation.cpp:102`)
  threads `y` across sweeps: each sweep reads the previous sweep's residual
  `x − A·y` (`:106`/`:109`). This is a genuine sequential recurrence — the loop
  does NOT lift to a single global tensor-field expression (the L3-iteration
  concern, [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md)).
  At L1 the sweep is a pure `pc_it`-fold parameter (law 2); the
  non-removability is the L3 lift's `partial-obstruction` finding (the BODY lifts;
  the SWEEP loop does not), to be recorded when this smoother's L3 row is
  authored — paralleling [`L3/chebyshev`](../L3/chebyshev.md). This is the
  sequential-obstruction the dispatch banner calls out.
- **NL2 — the kernel-api triangular sweep is the deeper non-removable kernel.**
  The general GS-SSOR / `trsv` relaxation the kernel-api
  ([`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md))
  names IS a sequential forward/back substitution that is non-parallelizable —
  the very reason Palace replaced it with Chebyshev point smoothers
  (`chebyshev.hpp:82` Adams 2003; GPU GS→Jacobi flip `amg.cpp:24`). This impl
  realizes the relaxation *without* that triangular sweep — the
  `realizes-kernel-api` correspondence is "what the opaque GS-SSOR contract
  computes, this from-our-primitives composition computes by a GS-free route."
- **NL3 — multigrid-integration test coverage only.** There is no dedicated
  `test-distrelaxation.cpp`; coverage is via the geometric-multigrid V-cycle
  integration path. Per the firm-on-positive-structure escape (CLAUDE.md
  §Methodology), the missing dedicated test does not gate firm because every law
  is a syntactic identity on fully-read positive source (the
  `chebyshev-smoother` / `jacobi-smoother` no-dedicated-test precedent).

## Dependencies

- [`chebyshev-smoother`](./chebyshev-smoother.md) (firm) — the primary point
  smoother `B` and the auxiliary point smoother `B_G`
  (`distrelaxation.cpp:21-34`). Both are `ChebyshevSmoother` /
  `ChebyshevSmoother1stKind` closures; the 4th-/1st-kind variant is absorbed
  there.
- [`apply_linop`](./apply_linop.md) (firm) — the primary matvec `A·y`
  (`distrelaxation.cpp:109`) forming the residual, and the discrete-gradient
  transfers `Gᵀ·r` (`:111`) / `G·y_G` (`:117`).
- [`axpby`](./axpby.md) (firm) — the residual combine `r = 1·x − 1·(A·y)`
  (`linalg::AXPBY(1.0, x, -1.0, r)`, `distrelaxation.cpp:110`).
- [`interpolator`](./interpolator.md) (firm) — produces the de-Rham discrete
  gradient `G` (the Grad edge, H1→ND) consumed at `Gᵀ` (`:111`) and `G`
  (`:117`); `G` is the ctor argument (`distrelaxation.cpp:17`).

References (NOT spine dependencies):

- [`set_subvector_zero`](./set_subvector_zero.md) — the auxiliary essential-dof
  pin `Z_ess · x_G` (`linalg::SetSubVector(x_G, *dbc_tdof_list_G, 0.0)`,
  `distrelaxation.cpp:112-115`); consumed-by, the same essential-dof-pin atom
  `divfree_projector` uses.
- [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) —
  the `realizes-kernel-api` target (the opaque GS-SSOR kernel-api this impl
  realizes; `reference`-class, free).
- [`L4/preconditioning-framework`](../L4/preconditioning-framework.md) — the
  multigrid V-cycle that installs this as a per-level smoother (consumed-by).

## Evidence

All ranges on-disk verified (citecheck `--anchor` + direct `Read`; the codemap
`read_range` drifted +1 on `distrelaxation.hpp` and the `.cpp` auxiliary-leg
lines — on-disk values used):

- `palace/linalg/distrelaxation.hpp:23-30` — the header class declaration with
  the Hiptmair-distributive-relaxation comment (`:23-28`,
  "Hiptmair distributive relaxation smoother applying smoothers to both the
  operator in the primary space as well as its projection into an auxiliary
  space. Reference: Hiptmair … SIAM J. Numer. Anal. (1998)") and the
  `class DistRelaxationSmoother : public Solver<OperType>` line (`:30`).
- `palace/linalg/distrelaxation.hpp:34-51` — the private member set backing the
  `DistRelaxSmoother[N, M]` record: `pc_it` (`:36`), `G` (`:39`), `A`/`A_G`
  (`:42`), `dbc_tdof_list_G` (`:43`), `B`/`B_G` (`:46`/`:47`), scratch vectors
  (`:50`).
- `palace/linalg/distrelaxation.cpp:13-36` — the ctor: template head (`:13`),
  signature with `comm, G, smooth_it, cheby_*` args (`:14-18`), the
  4th-kind/1st-kind ChebyshevSmoother fold for `B`, `B_G` (`:21-34`),
  `B_G->SetInitialGuess(false)` (`:35`).
- `palace/linalg/distrelaxation.cpp:38-69` — `SetOperators`: the size assert
  (`:46-48`), `A = &op` / `A_G = &op_G` capture (`:49-50`), the auxiliary
  essential-dof set `dbc_tdof_list_G = PtAP_G->GetEssentialTrueDofs()` (`:61`),
  and `B->SetOperator(op)` / `B_G->SetOperator(op_G)` (`:64-65`).
- `palace/linalg/distrelaxation.cpp:101-119` — `Mult2`, the relaxation action:
  sweep loop (`:102`), primary leg `y = y + B(x − A·y)` (`:104-106`,
  `SetInitialGuess(initial_guess || it > 0)` `:105`), auxiliary leg
  `y = y + G B_G Gᵀ(x − A·y)` (`:108-117`) — `A->Mult(y, r)` (`:109`),
  `linalg::AXPBY(1.0, x, -1.0, r)` (`:110`), `Gᵀ` transfer (`:111`),
  essential-dof pin (`:112-115`), `B_G` auxiliary relax (`:116`), `G` prolong-add
  (`:117`).
- `palace/linalg/distrelaxation.cpp:121-151` — `MultTranspose2`, the reversed-order
  transpose action (basis for the "not symmetric in general" non-law and the
  SSOR forward+transpose-pair idiom).

Kernel-api correspondence anchors (the opaque GS-SSOR contract this realizes,
from the kept `triangular-solve-obstruction` theme):

- `palace/linalg/chebyshev.hpp:82` — the Adams et al. 2003 polynomial-over-
  Gauss-Seidel citation: documents that Palace's relaxation is GS-free by design
  (the realized route avoids the triangular sweep the kernel-api names).
- `palace/linalg/amg.cpp:24` — the GPU GS→l1-Jacobi flip; corroborates that the
  GS triangular sweep is the non-removable kernel engineered around.
