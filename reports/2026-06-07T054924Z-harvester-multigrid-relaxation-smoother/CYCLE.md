---
agent: harvester
invoked_at: 2026-06-07T060000Z
scope: L1 operator: multigrid-relaxation-smoother
status: pending
inputs:
  - cycle-121 dispatch plan D3 (reports/2026-06-07T054924Z-cycle-planner-cycle-121/CYCLE.md)
  - kernel-api surface: book/src/L1-L0/triangular-solve-obstruction.md (retained obstruction-kind; role-label kernel-api added + sub-kind clarified bare obstruction → opaque-library-ownership)
  - DIRECTIVE-3 kernel-API/impl distinction (CLAUDE.md §Methodology-invariants; memory project_kernel_api_impl_distinction)
  - L0 source: palace/linalg/distrelaxation.{cpp,hpp} (all ranges on-disk verified)
  - firm constituents: L1/chebyshev-smoother, L1/apply_linop, L1/axpby, L1/interpolator
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean. L1/multigrid-relaxation-smoother FIRM (kernel-impl); triangular-solve obstruction gained kernel-api role-label. Made LIVE intra-cycle by D1's depends-on."
---

# CYCLE: Formalize multigrid-relaxation-smoother at L1

## Summary

Authors the **`multigrid-relaxation-smoother`** kernel-IMPLEMENTATION node — the
constructive, in-our-semantics realization of the multigrid relaxation slot that
the general GS-SSOR / sparse-triangular relaxation kernel-API
(`triangular-solve-obstruction`) names but does not realize in Palace. Palace's
realization is the **Hiptmair distributive relaxation smoother**
(`DistRelaxationSmoother`, `palace/linalg/distrelaxation.{cpp,hpp}`): a pure
relaxation action that applies a point-smoother `B` in the **primary**
(Nedelec/H(curl)) space and a second point-smoother `B_G` in the **auxiliary**
(gradient) space reached through the de-Rham discrete-gradient interpolator `G`,
threading the residual `x − A·y` between them across a fixed `pc_it` sweep count.
It composes entirely from firm L1 primitives — `chebyshev-smoother` (the point
smoothers `B`, `B_G`), `apply_linop` + `axpby` (the residual `r = x − A·y`),
and `interpolator` (the discrete gradient `G` and its transpose `Gᵀ`). It is
linked `realizes-kernel-api` (`reference`-class, free) to the KEPT
`triangular-solve-obstruction` kernel-api theme: a reviewer reads the opaque
GS-SSOR contract (a) AND this from-our-primitives realization (b) and checks they
match. The status is **firm** on the firm-on-positive-structure escape (every law
is a syntactic identity on fully-read positive source — the
`chebyshev-smoother` / `jacobi-smoother` multigrid-integration-coverage-only
precedent), with the **sequential-obstruction on the outer `pc_it` relaxation
sweep** documented as a non-law (the recurrence is the L3-iteration concern; the
GS triangular sweep the kernel-api would use is itself the witnessed
non-removable sweep Palace deliberately replaced with Chebyshev, per
`chebyshev.hpp:82` Adams 2003).

## Proposed changes

```new:book/src/L1/multigrid-relaxation-smoother.md
---
layer: L1
operator: multigrid-relaxation-smoother
firmness: firm
# Graded-stack scheme: this L1 entry is the kernel-IMPLEMENTATION node (DIRECTIVE-3,
# 2026-06-07) — the constructive realization of the multigrid relaxation slot. It carries a
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
(2026-06-07; CLAUDE.md §Methodology-invariants "Kernel-API vs
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
[`divfree-projector`](./divfree-projector.md): the primary argument `op` is a
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
[`divfree-projector`](./divfree-projector.md) (`I − Grad(GᵀMG)⁻¹GᵀM`): both
consume the [`interpolator`](./interpolator.md)-produced discrete gradient `G`
and apply a sub-operation in the gradient space. The distinction:
`divfree-projector` performs an exact auxiliary *solve* `(GᵀMG)⁻¹`, while this
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
rank-1 dof-vector at L1, per `book/src/design/l4_calculus.md` §1.2.2 "reserve
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
  (auxiliary→primary→primary-transpose, `:121-152`) apply the legs in the
  REVERSED order with the transposed point smoothers `Bᵀ`, `B_Gᵀ`; the
  forward action is symmetric only if used as a forward+transpose pair (the
  SSOR-symmetric-sweep idiom). The single `Mult2` action alone is non-symmetric.

## Non-laws / load-bearing caveats

- **NL1 — outer `pc_it` relaxation-sweep is a witnessed sequential-obstruction.**
  The `for (int it = 0; it < pc_it; it++)` loop (`distrelaxation.cpp:103`)
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
  `divfree-projector` uses.
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
  sweep loop (`:103`), primary leg `y = y + B(x − A·y)` (`:104-106`,
  `SetInitialGuess(initial_guess || it > 0)` `:105`), auxiliary leg
  `y = y + G B_G Gᵀ(x − A·y)` (`:108-117`) — `A->Mult(y, r)` (`:109`),
  `linalg::AXPBY(1.0, x, -1.0, r)` (`:110`), `Gᵀ` transfer (`:111`),
  essential-dof pin (`:112-115`), `B_G` auxiliary relax (`:116`), `G` prolong-add
  (`:117`).
- `palace/linalg/distrelaxation.cpp:121-152` — `MultTranspose2`, the reversed-order
  transpose action (basis for the "not symmetric in general" non-law and the
  SSOR forward+transpose-pair idiom).

Kernel-api correspondence anchors (the opaque GS-SSOR contract this realizes,
from the kept `triangular-solve-obstruction` theme):

- `palace/linalg/chebyshev.hpp:82` — the Adams et al. 2003 polynomial-over-
  Gauss-Seidel citation: documents that Palace's relaxation is GS-free by design
  (the realized route avoids the triangular sweep the kernel-api names).
- `palace/linalg/amg.cpp:24` — the GPU GS→l1-Jacobi flip; corroborates that the
  GS triangular sweep is the non-removable kernel engineered around.

## Status

`firm` — **kernel-impl**. (DIRECTIVE-3 role-label: this node is the
kernel-IMPLEMENTATION — the constructive, in-our-semantics realization of the
multigrid relaxation slot; its kernel-API counterpart is the kept
[`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md), to
which it is linked by a `realizes-kernel-api` `reference`-class edge that
constrains neither rank nor liveness.)

Promoted firm on the **firm-on-positive-structure escape** (CLAUDE.md
§Methodology "rough-in (test-coverage-bounded)"): every algebraic law (1-5) is a
syntactic identity on the fully-read positive `Mult2` body
(`distrelaxation.cpp:101-119`) + ctor/`SetOperators`, so the absence of a
dedicated `test-distrelaxation.cpp` (multigrid-integration coverage only) does
not gate firm — the [`chebyshev-smoother`](./chebyshev-smoother.md) /
[`jacobi-smoother`](./jacobi-smoother.md) no-dedicated-test precedent. All four
`depends-on` constituents (`chebyshev-smoother`, `apply_linop`, `axpby`,
`interpolator`) are firm on disk, so the well-foundedness invariant
`rank(impl) ≤ min(rank(deps))` holds (firm ≤ firm). The `realizes-kernel-api`
edge to the obstruction theme does NOT enter the rank computation (it is
`reference`-class, free).

The **outer `pc_it` relaxation-sweep sequential-obstruction** (non-law NL1) is
documented as the L3-lift `partial-obstruction` finding (the body lifts; the
sweep loop does not — paralleling [`L3/chebyshev`](../L3/chebyshev.md)); it does
NOT gate the L1 firm status (at L1 the sweep is a pure `pc_it`-fold parameter).

L1>L0 lowering theme `multigrid-relaxation-smoother-mutation-rotation`
(named-not-authored; reintroduces the `Mult2(x, y, r)` output-arg mutation +
scratch vectors `x_G`/`y_G`/`r_G`/`r`).
```

```edit:book/src/L1-L0/triangular-solve-obstruction.md
## Status

`obstruction (opaque-library-ownership)` — **kernel-api**. (DIRECTIVE-3
role-label, 2026-06-07: this theme is repositioned as the **kernel-API surface**
— the reviewable opaque contract the multigrid smoother slot calls. This edit
adds the `kernel-api` role-label AND clarifies the sub-kind from the prior bare
`obstruction` to `obstruction (opaque-library-ownership)` — it stays
obstruction-*kind* (NOT downgraded, NOT promoted to a constructive status); the
sub-kind is the accurate one because it genuinely IS the opaque
GS-SSOR / sparse-triangular relaxation boundary (HYPRE / external direct-solver
ownership), claim-free, with negative anchors. Its constructive
kernel-IMPLEMENTATION counterpart is
[`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md) (the
Hiptmair distributive smoother, firm c121), which `realizes-kernel-api` this
surface via a `reference`-class edge; `lowering-verifier` audits the
impl-realizes-API correspondence.)

Claim-free documentation of the absence of a general
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
```

```edit:book/src/L1/index.md
| [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` (L1>L0: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md), cycle-008) |
| [`multigrid-relaxation-smoother`](./multigrid-relaxation-smoother.md) | `(op: DistRelaxSmoother[N, M], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` (i.e. the Hiptmair distributive relaxation: `y + B(x−A·y)` primary leg, then `y + G·B_G·Gᵀ(x−A·y)` auxiliary-gradient leg, `pc_it` sweeps) | `chebyshev-smoother` (the primary `B` + auxiliary `B_G` point smoothers), `apply_linop` (matvec `A·y` + `Gᵀ`/`G` transfers), `axpby` (residual `x−A·y`), `interpolator` (the de-Rham discrete gradient `G`); references `set_subvector_zero` (auxiliary essential-dof pin) + `realizes-kernel-api` → [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) (reference-class, free) | `firm` (**kernel-impl**, DIRECTIVE-3 2026-06-07; the constructive in-our-semantics realization of the multigrid relaxation slot the GS-SSOR kernel-api `triangular-solve-obstruction` names; L0: `palace/linalg/distrelaxation.cpp:13-36` ctor, `:38-69` `SetOperators`, `:101-119` `Mult2` + hpp `:23-51`; harvested cycle-121; firm-on-positive-structure, no-dedicated-`test-distrelaxation.cpp` caveat non-gating per `chebyshev-smoother`/`jacobi-smoother` precedent; laws: single-sweep multiplicative decomposition, `pc_it`-fold, zero-residual fixed point, auxiliary-leg residual-linearity, initial-guess fast path; non-laws: outer `pc_it` sweep sequential-obstruction (L3 partial-obstruction, body-lifts/sweep-does-not), not-additive-between-spaces, not-symmetric-single-action; realizes the GS-free Chebyshev relaxation Palace engineered for the kernel-api triangular sweep) |
```

(Dep-map placement, repairer cycle-121: the new dep-map row is inserted into the
existing **Constructed-operator gates** by-kind group at its alpha position
(`multigrid-relaxation-smoother` sorts after `ksp_solve`, the current last row of
that group — the `ksp_solve` row above is the unchanged placement anchor and
makes the insert point unique). The bare new `| **Kernel-impl (smoother)** |`
by-kind sub-header is dropped: the kernel-impl-ness is carried in the status cell
role-label `**kernel-impl**`, not a new dep-map group, matching the
sensible-default chapter-kind placement used for SUMMARY.)

```edit:book/src/L1/index.md
- (empty as of cycle-010) — the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now **fully answered**: both halves landed in cycle-010 wave-1 as rough-ins and both are now **firm** — the [`matrix-weighted-norm`](./matrix-weighted-norm.md) half promoted cycle-091 (the batch-29 LEAD firm-flip-and-cascade wave) and the [`bilinear-form`](./bilinear-form.md) half promoted cycle-095 (this cycle's firm-flip-and-cascade wave, on the firm-on-positive-structure escape). The `SpectralNorm` (power-iteration) sibling remains the OQ's sole open residual; both L1>L0 lowering themes (`matrix-weighted-norm-mutation-rotation`, `bilinear-form-mutation-rotation`) are themselves firm.

**Kernel-impl (smoother) — DIRECTIVE-3 (2026-06-07):**

- [`multigrid-relaxation-smoother`](./multigrid-relaxation-smoother.md) — the constructive **kernel-IMPLEMENTATION** of the multigrid relaxation slot (Palace's Hiptmair distributive relaxation smoother, `DistRelaxationSmoother`). Realizes the general GS-SSOR / sparse-triangular relaxation **kernel-API** ([`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md), kept `obstruction (opaque-library-ownership)`, role-label kernel-api) via a `realizes-kernel-api` `reference`-class edge (free — NOT a `depends-on`, constrains neither rank nor liveness). Relaxes the operator `A` in the primary H(curl) space via a Chebyshev point smoother `B`, then corrects through the de-Rham discrete gradient `G` into the auxiliary (gradient) space via a second Chebyshev point smoother `B_G` — a GS-free realization (the route Palace engineered to avoid the non-parallelizable triangular sweep the kernel-api names, `chebyshev.hpp:82` Adams 2003). Composes the firm constituents `chebyshev-smoother` (`B`, `B_G`), `apply_linop` (`A·y`, `Gᵀ`, `G`), `axpby` (residual), `interpolator` (`G`). Firm on the firm-on-positive-structure escape (every law a syntactic identity on the fully-read `Mult2` body; multigrid-integration test coverage only, non-gating per `chebyshev-smoother`/`jacobi-smoother` precedent). The outer `pc_it` relaxation sweep is a witnessed sequential-obstruction (the L3 partial-obstruction concern — body lifts, sweep loop does not — paralleling `L3/chebyshev`); the multigrid V-cycle ([`L4/preconditioning-framework`](../L4/preconditioning-framework.md)) installs it as the per-level smoother. Harvested cycle-121 D3.
```

(Vocabulary-cohort anchor uniqueness, repairer cycle-121: the new
**Kernel-impl (smoother)** bullet block is anchored to follow the section's
existing final paragraph — the unique "(empty as of cycle-010)…" Queued-list
line — so it is appended at the TAIL of the `## Vocabulary cohort` section (after
the Queued sub-list, before `## Operator dep-map`), NOT inserted ambiguously at
the top against the `**Firm (33 main…**` sub-list that immediately follows the
heading. The leading line above is the unchanged on-disk placement anchor.)

```edit:book/src/SUMMARY.md
  - [ksp_solve](./L1/ksp_solve.md)
  - [multigrid-relaxation-smoother](./L1/multigrid-relaxation-smoother.md)
```

(SUMMARY.md placement, repairer cycle-121: the new chapter is filed into the
existing **Constructed-operator gates** by-kind sub-chapter group at its alpha
position — `multigrid-relaxation-smoother` sorts after `ksp_solve`, the current
last entry in that group — as a 2-space-indented nested entry matching the
group's other entries. This is the kernel-impl sensible-default chapter-kind
placement: the chapter self-identifies as "a constructed-operator gate at L1, in
the family of `chebyshev-smoother` and `divfree-projector`" (§Context), so no new
SUMMARY "Kernel-impl (smoother)" group header / intro page is introduced; the
`kernel-impl` role-label lives on the `## Status` line + the index cells, not the
SUMMARY grouping. The `ksp_solve` line above is the unchanged placement anchor.)

## Operator content

(Authored in full inside the `new:book/src/L1/multigrid-relaxation-smoother.md`
fenced block above — Signature, Record definition, Algebraic laws, Non-laws,
Dependencies, Evidence, Status all enclosed.)

## Supporting evidence

- **Kernel-API/impl distinction** — CLAUDE.md §Methodology-invariants "Kernel-API
  vs kernel-IMPLEMENTATION distinction" (DIRECTIVE-3, 2026-06-07); memory
  `project_kernel_api_impl_distinction`. This is the founding triangular-solve /
  GS-SSOR relaxation kernel named in that directive ("triangular-solve / GS-SSOR
  relaxation … impl behind the multigrid smoother, sequential-obstruction noted
  for the recurrence").
- **Kept kernel-api theme** — `book/src/L1-L0/triangular-solve-obstruction.md`
  (read in full): documents the opaque GS-SSOR / `trsv` relaxation contract with
  negative anchors. Role-labeled `kernel-api` in this dispatch's edit; the edit
  also clarifies the sub-kind from the prior bare `obstruction` on disk to
  `obstruction (opaque-library-ownership)` — stays obstruction-*kind* (NOT
  downgraded/deleted, NOT promoted to a constructive status).
- **L0 source** — `palace/linalg/distrelaxation.{cpp,hpp}`, all ranges on-disk
  verified via citecheck `--anchor` + direct `Read` (codemap `read_range` drifted
  +1 on the hpp class line and the cpp auxiliary-leg block; on-disk values used —
  `AXPBY` `:110` not codemap's `:113`; `class DistRelaxationSmoother` hpp `:30`
  not codemap's `:29`).
- **Firm constituents** (all firm on disk, well-foundedness firm/firm):
  `L1/chebyshev-smoother` (rank firm), `L1/apply_linop` (rank: firm),
  `L1/axpby` (rank: firm), `L1/interpolator` (rank: firm).
- **Structural precedents** — `L1/divfree-projector` (same de-Rham
  discrete-gradient `G` auxiliary-space pattern), `L3/chebyshev`
  (`partial-obstruction`: body-lifts / sweep-does-not, the model for NL1's L3
  finding), `L1/chebyshev-smoother` + `L1/jacobi-smoother` (firm-on-positive-
  structure / no-dedicated-test precedent).

## Open questions / caveats

- **`multigrid-relaxation-smoother-mutation-rotation` L1>L0 theme is
  named-not-authored.** The `Mult2(x, y, r)` output-arg mutation idiom + the four
  scratch vectors (`x_G`, `y_G`, `r_G`, `r`, `distrelaxation.hpp:50`) reintroduce
  at L0; the per-step decomposition is the firm sister themes
  (`apply-linop-mutation-rotation`, `axpby-mutation-rotation`) plus the
  Chebyshev-smoother + interpolator-apply legs. Flag for an abstractor dispatch.
- **L3 partial-obstruction row not authored this cycle.** The outer `pc_it`
  relaxation sweep is the witnessed sequential-obstruction (NL1); its formal home
  is an `L3/multigrid-relaxation-smoother.md` `partial-obstruction` row
  (body-lifts / sweep-does-not, paralleling `L3/chebyshev`). Out of this
  one-operator-at-L1 dispatch's scope; flag for the L3-iteration-views planner
  (DIRECTIVE-2 grounded-consumer item-4). The L1 firm status does NOT depend on
  it (at L1 the sweep is a pure `pc_it`-fold parameter).
- **`lowering-verifier` impl-realizes-API audit is a c122 candidate.** Per the
  planner caveat, the `realizes-kernel-api` correspondence (the opaque GS-SSOR
  contract vs this from-our-primitives Chebyshev realization) should be audited
  by `lowering-verifier` once the impl lands — not dispatched this cycle.
- **D1 coupling (forward-reference).** The geometric-multigrid preconditioner
  column (D1) forward-references this canonical slug
  `book/src/L1/multigrid-relaxation-smoother.md` (stated in both scopes); the
  per-report integrator wires the live link when both land. No file collision
  (D1 = `feature/*.{L4,L1}.md`; D3 = this `L1/` chapter + the `L1-L0/` theme
  status edit).
- **Index tally NOT touched.** This kernel-impl is registered as its own
  dep-map row + its own §Vocabulary-cohort "Kernel-impl (smoother)" sub-list
  bullet (both authored above, per the index-registration partition). It is a
  distinct *kind* (kernel-impl), NOT a "main-cohort firm operator", so the
  "33 main / 43 firm grand total" consolidated tally is deliberately left
  unchanged — flag for the integrator to confirm whether a separate kernel-impl
  count line is wanted (no count-owner for L1 was named this cycle; only one
  index-touching dispatch for the main cohort, so no parallel-blind tally
  divergence risk).
