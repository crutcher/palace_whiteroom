---
agent: abstractor
invoked_at: 2026-05-28T14:47:19Z
scope: L1>L0 + L2>L1 theme sketches — chebyshev-smoother-mutation-rotation + chebyshev-iteration-fusion
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: a4d7495
integration_notes: "cycle-013 finalize. 2 firm themes landed: chebyshev-smoother-mutation-rotation (L1>L0; 4 sub-patterns + transpose-alias sub-rule) + chebyshev-iteration-fusion (L2>L1; FIRST real chapter under the previously-skeleton L2-L1 Part — index ## Theme list placeholder displaced). Both SUMMARY-registered. Clean run (as-repaired element-kernel citations)."
inputs:
  - book/src/L1/chebyshev-smoother.md (firm L1 operator)
  - book/src/L2/chebyshev-iteration.md (firm L2 operator)
  - palace/linalg/chebyshev.cpp:13-78 (GetLambdaMax, ApplyOp, ApplyOrder0/K kernels)
  - palace/linalg/chebyshev.cpp:161-220 (4th-kind ctor / SetOperator / Mult2)
  - palace/linalg/chebyshev.cpp:223-293 (1st-kind ctor / SetOperator / Mult2)
  - palace/linalg/chebyshev.hpp:30-114 (member layout, Mult/MultTranspose forwarding)
  - book/src/L1-L0/axpby-mutation-rotation.md (L1>L0 structural precedent)
  - book/src/L1-L0/eigsolve-mutation-rotation.md (partly-constructive precedent)
---

# CYCLE: L1>L0 + L2>L1 theme sketches — chebyshev (two themes, one invocation pair)

## Summary

Two chebyshev lowering themes, both narrated high→low. **(1)
`chebyshev-smoother-mutation-rotation`** (L1>L0): the pure-functional L1 action
`y' = chebyshev_smoother(op, x, y, initial_guess)` lowers into Palace's
in-place `ChebyshevSmoother::Mult2(x, y, r)` /
`ChebyshevSmoother1stKind::Mult2(x, y, r)` member calls — the destination `y` is
overwritten in place, the residual workspace `r` and member direction workspace
`d` are scribbled, and `op`'s closure fields lower into the construction-bound
`SetOperator` step (captures `A`, assembles+reciprocates `dinv`, computes the
spectral scalars via `GetLambdaMax → linalg::SpectralNorm`). Justification is
**structural** (output-arg mutation re-binding + workspace erasure) with the
diagonal-scaling `dinv` coupling and the two-class polynomial-kind variant axis
folded into the constructed-operator closure. **(2)
`chebyshev-iteration-fusion`** (L2>L1): the L2 explicit `order`-step three-term
recurrence (one `apply_linop` + `axpby` + `scal` + `elementwise_product` chain
per degree) **fuses upward** into the L1 closed-form polynomial action
`p_order(D⁻¹ A)·r` named as a single matrix-free smoother step — the per-degree
direction/residual/accumulator updates collapse into one closed-form polynomial
call whose coefficients `op.scalars` generates. Justification **algebraic**
(the recurrence *is* the matrix-free evaluation of the polynomial; the L1↔L2
identity is law 1 of the L2 entry). Both themes are **firm** — every form is a
syntactic identity on fully-specified source (no literature inference, no
negative-anchor reconstruction). The L2>L1 theme is the first chapter under the
previously-empty `book/src/L2-L1/` Part.

## Proposed changes

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
# chebyshev-smoother-mutation-rotation

The mutation rotation for the fixed-degree Chebyshev polynomial smoother action.
Lowers the pure L1 form [`chebyshev_smoother`](../L1/chebyshev-smoother.md) —
`y' = chebyshev_smoother(op, x, y, initial_guess) = y + p_order(D⁻¹ A)·(x − A·y)`
[repeated `pc_it` times] — into Palace's in-place L0 `Mult2` member-call family on
the two `ChebyshevSmoother` / `ChebyshevSmoother1stKind` template classes, plus
the construction-bound `SetOperator` setup that materialises the L1 closure
fields. Narrated forward: the L1 pure action dissolves into the L0
output-argument mutation idiom (writes through `y`, scribbles workspaces `r`, `d`)
over a construction-bound spectral-scalar capture.

## Slug

`chebyshev-smoother-mutation-rotation`

## L1 form (LHS)

The pure-functional smoother action consumes the prior `y` and produces a fresh
post-smoothing accumulator value over an opaque constructed closure `op`
(`ChebSmoother[N]`, carrying `(A, dinv, order, pc_it, scalars)`):

    y_new = chebyshev_smoother(op, x, y_old, initial_guess)
          = y_old + p_order(D⁻¹ A)·(x − A·y_old)        -- repeated op.pc_it times

The closure `op` is itself the value produced by a pure *setup* sub-action of
`(A, sf_max[, sf_min], order, pc_it, variant)` modulo the opaque
`spectrum_estimate(A, dinv)` (see [`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md)
§Signature). At L1 there is no destination buffer, no workspace ownership, and no
runtime kind tag — the polynomial-kind (4th / 1st) and element-type (real /
complex) variants are absorbed into the closure (see Applicability conditions).

## L0 form (RHS)

The rewrite splits into a **construction site** (the `SetOperator` step that
materialises the closure fields) and an **application site** (the `Mult2` /
`Mult` family that realises the per-call action by in-place mutation). Two L0
classes carry the polynomial-kind variant; the application scaffold is identical
across them and across the `Mult` / `MultTranspose` / `Mult2` / `MultTranspose2`
forwarding chain.

### Sub-pattern A — application via in-place `Mult2(x, y, r)`

    void ChebyshevSmoother<OperType>::Mult2(const VecType &x, VecType &y, VecType &r) const
    {
      for (int it = 0; it < pc_it; it++)
      {
        if (this->initial_guess || it > 0) {
          ApplyOp(*A, y, r);                 // r = A·y
          linalg::AXPBY(1.0, x, -1.0, r);    // r = x − A·y
        } else {
          r = x;  y = 0.0;                    // degenerate-absorption branch
        }
        ApplyOrder0(4.0/(3.0*lambda_max), dinv, r, d);   // d = α₀·(dinv ⊙ r)
        for (int k = 1; k < order; k++) {
          y += d;                            // accumulate into destination
          ApplyOp(*A, d, r, -1.0);           // r −= A·d
          /* sd, sr closed forms */
          ApplyOrderK(sd, sr, dinv, r, d);   // d = sd·d + sr·(dinv ⊙ r)
        }
        y += d;                              // final accumulate
      }
    }

The L1 *value* `y_new` is the L0 `y` after `Mult2` returns. The crucial L0 facts
the L1 form erases:

- **Destination-arg mutation.** `y` is the output argument; `y += d` and
  `y = 0.0` write through it in place. The L1 form takes the prior `y` as a value
  and returns a fresh one. (Same output-arg idiom as
  [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) and
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md), one level up: the
  destination is named in the call's argument list, not on the LHS.)
- **Two scribbled workspaces.** `r` (the residual) is a *passed* workspace
  argument; `d` (the direction) is a *member* workspace (`chebyshev.hpp:43` —
  `mutable VecType d, r;`). Both are written every step and carry no value across
  calls. At L1 they vanish — the smoother is a single value-producing action.
- **Construction-bound spectral scalars.** `lambda_max` (4th-kind) /
  `theta`, `delta` (1st-kind) are read from member fields set once at
  `SetOperator`; they are `op.scalars`' captured state at L1.
- **Diagonal-scaling coupling (`dinv`).** Every `ApplyOrder0` / `ApplyOrderK`
  pass reads the member `dinv` (`chebyshev.cpp:69-78, :114-123`); the `D⁻¹`
  action `dinv ⊙ r` is fused into the elementwise kernel at L0 (de-fusion is the
  *L2* concern — see the sibling [`chebyshev-iteration-fusion`](../L2-L1/chebyshev-iteration-fusion.md);
  here at L1>L0 the `dinv` coupling is just a closure field `op.dinv` read by the
  opaque polynomial action).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer `y`; erase the workspace arguments `r`, `d`; the closure
fields are the construction-bound members. The polynomial *body* is below L1
resolution (it is the L2 form), so this theme treats `Mult2`'s inner recurrence
as the opaque realisation of the L1 `p_order(D⁻¹ A)·(·)` action and does NOT
re-derive the per-degree coefficients (those are the L2>L1 theme's concern).

Citations:
- `palace/linalg/chebyshev.cpp:188-220` — `ChebyshevSmoother<OperType>::Mult2`
  (4th-kind): the `pc_it` outer sweep, the `initial_guess` branch, the in-place
  `y += d` / `y = 0.0`, the scribbled `r` / `d`, the `ApplyOrder0` / `ApplyOrderK`
  diagonal-scaled passes.
- `palace/linalg/chebyshev.cpp:261-293` —
  `ChebyshevSmoother1stKind<OperType>::Mult2`: identical scaffold, 1st-kind
  scalars.
- `palace/linalg/chebyshev.hpp:43` — `mutable VecType d, r;` (the two scribbled
  workspaces; `d` is a member, `r` is passed).

### Sub-pattern B — entry-point forwarding (`Mult` → `Mult2`; resize-on-demand)

    void Mult(const VecType &x, VecType &y) const override {
      if (r.Size() != y.Size()) { r.SetSize(y.Size()); r.UseDevice(true); }
      Mult2(x, y, r);
    }

The public `Solver` entry point `Mult(x, y)` lazily resizes the *member* `r`
workspace to match `y`, then forwards to `Mult2(x, y, r)` (sub-pattern A). The
resize-on-demand is a transparent workspace-management trick: it ensures the
member workspace conforms before the in-place sweep. At L1 the smoother action
has no notion of a member workspace — the resize and the `Mult` / `Mult2` split
both vanish into the single `chebyshev_smoother` action.

Justification kind: **structural** — the `Mult`/`Mult2` split is an L0 workspace-
ownership convention (passed-`r` vs. member-`r`), not an algebraic distinction.
The L1 form has one action; the two L0 entry points are the resize-wrapper and
the passed-workspace kernel of the same action.

Citations:
- `palace/linalg/chebyshev.hpp:50-58` — `Mult` resizes member `r`, forwards to
  `Mult2`.
- `palace/linalg/chebyshev.hpp:71` — `Mult2` pure-virtual override decl.

### Sub-pattern C — transpose aliasing under operator symmetry

    void MultTranspose2(const VecType &x, VecType &y, VecType &r) const override {
      Mult2(x, y, r);  // Assumes operator symmetry
    }

`MultTranspose2` forwards verbatim to `Mult2`. For the in-scope SPD `A` the
smoother is its own transpose. This realises L1 algebraic law 3
(`chebyshev_smoother_transpose(op, …) = chebyshev_smoother(op, …)`,
[`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md) §Algebraic laws). The
complex conjugate-`dinv` transpose kernels exist
(`palace/linalg/chebyshev.cpp:101-110, :150-159`) but are dead code under the
symmetric wiring — recognition rules for *potential* transpose sites, not
observed ones (see Open questions).

Justification kind: **algebraic** — the law `transpose = id` (SPD symmetry)
justifies the aliasing; recognition is by the `MultTranspose2 → Mult2` forward.

Citations:
- `palace/linalg/chebyshev.hpp:60-68` — `MultTranspose` resizes member `r`,
  forwards to `MultTranspose2`.
- `palace/linalg/chebyshev.hpp:73-76` — `MultTranspose2(x, y, r) { Mult2(x, y, r); }`
  ("Assumes operator symmetry").

### Sub-pattern D — construction site (`SetOperator`): closure-field materialisation

    void ChebyshevSmoother<OperType>::SetOperator(const OperType &op) {
      A = &op;
      d.SetSize(op.Height());  dinv.SetSize(op.Height());
      d.UseDevice(true);  dinv.UseDevice(true);
      op.AssembleDiagonal(dinv);  dinv.Reciprocal();    // dinv = 1 / diag(A)
      lambda_max = sf_max * GetLambdaMax(comm, *A, dinv);
      MFEM_VERIFY(lambda_max > 0.0, "…zero maximum eigenvalue…");
      this->height = op.Height();  this->width = op.Width();
    }

The L1 closure `op = ChebSmoother[N]` is the value `SetOperator` materialises:

- `op.A` ← the captured operator pointer `A = &op` (read-only thereafter).
- `op.dinv` ← `AssembleDiagonal(dinv); dinv.Reciprocal()` — assemble `diag(A)`
  into `dinv`, then reciprocate elementwise to `1 / diag(A)`. **Real-valued even
  for complex `A`** (`chebyshev.hpp:37` / `:106` — `// real-valued for now`).
  This is the **diagonal-scaling coupling**: `op.dinv` is the closure field that
  the per-call polynomial action reads as `D⁻¹`.
- `op.scalars`' captured state ← `lambda_max = sf_max * GetLambdaMax(...)`
  (4th-kind); 1st-kind additionally computes `lambda_min = sf_min * lambda_max`,
  `theta = ½(λ_max+λ_min)`, `delta = ½(λ_max−λ_min)`, with the optimised
  `sf_min` default `1.69 / (order^1.68 + 2.11·order + 1.98)` when non-positive
  (Phillips & Fischer 2022 eq. 2.24, `chebyshev.cpp:244-247`).
- `spectrum_estimate(A, dinv)` ← `GetLambdaMax(comm, *A, dinv)` →
  builds `DinvA = Dinv·A` and returns `linalg::SpectralNorm(comm, DinvA,
  hermitian)`; the **real** overload passes literal `true`
  (`chebyshev.cpp:13-18`), the **complex** overload passes `A.IsReal()`
  (`:20-27`); Hermitian for in-scope SPD-real wiring. This is the opaque setup
  sub-action of the L1 form (not part of the per-call mutation; see Open
  questions on its own L1 candidacy).

Justification kind: **structural** — `SetOperator` is the constructed-operator-
gate construction step (same family as the
[`ksp-solve`](./ksp-solve-mutation-rotation.md) /
[`eigsolve`](./eigsolve-mutation-rotation.md) setup sites): the L1 closure is a
pure function of the setup inputs modulo the opaque `spectrum_estimate`.

Citations:
- `palace/linalg/chebyshev.cpp:169-186` — 4th-kind `SetOperator`: capture `A`,
  `AssembleDiagonal(dinv); dinv.Reciprocal()`, `lambda_max = sf_max *
  GetLambdaMax(...)`, `MFEM_VERIFY(lambda_max > 0.0, …)`.
- `palace/linalg/chebyshev.cpp:232-259` — 1st-kind `SetOperator`: same scaffold
  + `sf_min` default, `theta`, `delta`.
- `palace/linalg/chebyshev.cpp:13-27` — `GetLambdaMax` (real + complex
  overloads): `DinvA = Dinv·A`; `linalg::SpectralNorm(comm, DinvA, hermitian)`.
- `palace/linalg/chebyshev.cpp:161-167` / `:223-230` — the two ctors:
  `MFEM_VERIFY(order > 0, …)`.

## Applicability conditions

The rewrite preserves semantics when:

1. **No aliasing between `x`, `y`, `r`, `d`.** `Mult2` reads `y` (residual) and
   writes `y` (accumulate), reads `r` and writes `r`, reads `d` and writes `d`.
   The L1 form takes the pre-call `y` as a value and owns no workspaces, so the
   lowering must guarantee `r`, `d` are distinct buffers from `x`, `y` and from
   each other. (Palace's `Mult` allocates the member `r` distinct from caller
   `y`; `d` is a distinct member. Inherited applicability condition shape from
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md).)
2. **No observer of prior `y` after the call.** `Mult2` destroys the prior `y`
   (`y = 0.0` on the no-guess first sweep, or `y += d` accumulation). If a
   downstream op reads `y_old`, the rewrite is invalid; at L1 `y_old` is still in
   scope. Upheld by lexical sequencing at every consumer site.
3. **Closure immutability across calls.** `op` (`A`, `dinv`, `order`, `pc_it`,
   spectral scalars) is set once at `SetOperator` and read-only across `Mult2`
   calls. `initial_guess` is the only per-call control input — a `Bool`
   argument at L1, the member `this->initial_guess` at L0 (set per-consumer via
   `SetInitialGuess`, e.g. `palace/linalg/distrelaxation.cpp:36`).
4. **Polynomial-kind variant is a setup-time class choice, not a runtime tag.**
   `ChebyshevSmoother` (4th-kind) and `ChebyshevSmoother1stKind` are distinct L0
   types; the consumer (`gmg.cpp:52-59`) chooses one at construction per the
   `cheby_4th_kind` config. At L1 both collapse to one operator parameterised by
   `op.scalars` — the kind is the closure's identity, NOT a per-call branch.
5. **Element-type conformance.** `<Operator>` (real) and `<ComplexOperator>`
   (complex) are both instantiated (`chebyshev.cpp:295-299`). The action is
   identical; only the underlying `apply_linop` and elementwise dispatch on
   element type. `dinv` is real-valued even for complex `A`.
6. **SPD operator (for the transpose-aliasing sub-pattern C).** The
   `MultTranspose2 → Mult2` alias requires operator symmetry; under a
   non-symmetric `A` the conjugate-transpose kernels would be needed (dead code
   currently).
7. **Single-machine scope.** The `comm` / `MPI_Comm` argument and the `Par*`
   spectral-norm machinery (`GetLambdaMax → SpectralNorm`) are read as their
   single-rank equivalents; MPI distribution is out of scope (flagged once).

## Justification kind

- **Sub-pattern A** (application) — `structural`. Output-arg `y` re-bind +
  workspace `r`, `d` erasure.
- **Sub-pattern B** (`Mult`→`Mult2` forwarding) — `structural`. Workspace-
  ownership convention split.
- **Sub-pattern C** (transpose aliasing) — `algebraic`. SPD-symmetry law
  `transpose = id` (L1 law 3).
- **Sub-pattern D** (construction) — `structural`. Constructed-operator-gate
  closure materialisation; pure-of-inputs modulo opaque `spectrum_estimate`.

The theme as a whole is `structural` with one algebraic sub-rule (C). A
`lowering-verifier` audit in a later cycle should confirm the four sub-patterns
match the L0 corpus exhaustively (both kinds, both element types, the consumer
forwarding sites).

## Speculative L1 operators

None. Both L1 anchors are already firm
([`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md)). The setup sub-action
`spectrum_estimate` (the `SpectralNorm` power-iteration sibling) is an
*existing open L1 candidate* in the residual-cohort open question
(`scaffolding/open-questions.md`, `matrix-weighted-norm-and-bilinear-form`), not
a new rough-in proposed here — this theme treats it as opaque.

## Verified-against

L0 evidence ranges (all verified via `palace-codemap` read_range this cycle):

- `palace/linalg/chebyshev.cpp:13-27` — `GetLambdaMax` (real literal-`true` /
  complex `A.IsReal()`); `DinvA = Dinv·A`; `linalg::SpectralNorm`.
- `palace/linalg/chebyshev.cpp:161-186` — 4th-kind ctor + `SetOperator`.
- `palace/linalg/chebyshev.cpp:188-220` — 4th-kind `Mult2` (in-place `y`, `r`,
  `d`; `ApplyOrder0` / `ApplyOrderK` diagonal-scaled passes).
- `palace/linalg/chebyshev.cpp:223-259` — 1st-kind ctor + `SetOperator`
  (`sf_min` default, `theta`, `delta`).
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2`.
- `palace/linalg/chebyshev.cpp:295-299` — element-type instantiations.
- `palace/linalg/chebyshev.hpp:30-43` — 4th-kind member layout (`mutable VecType
  d, r;`, `dinv`, `lambda_max`, `sf_max`).
- `palace/linalg/chebyshev.hpp:50-76` — `Mult` / `MultTranspose` resize-forward;
  `Mult2` / `MultTranspose2` (symmetry alias).
- `palace/linalg/chebyshev.hpp:80-114` — 1st-kind doc + member layout
  (`theta, delta, sf_max, sf_min`).
- `palace/linalg/gmg.cpp:52-59` — consumer: per-level kind choice via
  `cheby_4th_kind`.
- `palace/linalg/distrelaxation.cpp:21-36` — consumer:
  `B_G->SetInitialGuess(false)` (per-call `initial_guess` control).

L1 anchor:

- `book/src/L1/chebyshev-smoother.md` — the firm L1 operator all sub-patterns
  lower from.

## Status

`firm` — every sub-pattern is a syntactic identity on fully-specified Palace
source (verified via codemap read_range this cycle): the output-arg mutation
re-binding (A), the workspace-ownership forwarding split (B), the SPD-symmetry
transpose alias (C, = L1 law 3), and the closure-field construction (D) all read
straight off the source with no literature inference and no negative-anchor
reconstruction. The L1 anchor is itself firm (cycle-012 ratified). The opaque
`spectrum_estimate` setup sub-action is treated as a closure field, not
re-derived, so it imposes no constructive caveat on this theme. A
`lowering-verifier` exhaustiveness audit (both kinds × both element types ×
consumer forwarding sites) is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:101-110,
  :150-159` define conjugate-`dinv` transpose elementwise kernels that are
  unreachable under the symmetric `MultTranspose2 → Mult2` wiring. They are
  recognition rules for *potential* non-symmetric sites, not observed ones —
  same defined-not-used status as the
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) `ComplexVector::Subtract`
  forms. Flag for the `lowering-verifier`.
- **`spectrum_estimate` L1 candidacy.** Whether the `GetLambdaMax → SpectralNorm`
  power-iteration sub-action should be firmed as its own L1 operator is the
  open `matrix-weighted-norm-and-bilinear-form` residual-cohort question; this
  theme treats it as opaque. (Lifting note — reverse direction: an L0
  power-iteration loop would lift to a `spectrum_estimate` L1 op; recorded here
  in working notes, not in the formal chapter.)
- The `MFEM_VERIFY(lambda_max > 0.0, …)` guard is a setup-time precondition (the
  spectral estimate must be positive), not a per-call error condition — distinct
  from the `eigsolve` `LinearSolveFailed` partly-constructive sub-part. No
  partly-constructive caveat applies here.
```

```edit:book/src/L2-L1/chebyshev-iteration-fusion.md
# chebyshev-iteration-fusion

The fusion rotation for the Chebyshev polynomial smoother. Lowers the L2 explicit
`order`-step three-term recurrence [`chebyshev-iteration`](../L2/chebyshev-iteration.md)
into the L1 closed-form polynomial action [`chebyshev-smoother`](../L1/chebyshev-smoother.md):
the per-degree direction / residual / accumulator updates **fuse** into a single
closed-form matrix-free polynomial-action call `y + p_order(D⁻¹ A)·(x − A·y)`
whose coefficients the variant scalar generator produces. Narrated forward: the L2
recurrence collapses (fuses) upward into one named polynomial step at L1.

## Slug

`chebyshev-iteration-fusion`

## L2 form (LHS)

The L2 form is the explicit degree-`order` three-term polynomial recurrence,
built from named L1 leaf primitives, threaded by the variant scalar generator
(`palace/linalg/chebyshev.cpp:188-220` 4th-kind, `:261-293` 1st-kind; the L2
unfolding in [`chebyshev-iteration`](../L2/chebyshev-iteration.md) §Semantics):

```text
sweep(op, x, y, first):
  r = if first && not initial_guess
        then x                                       -- with y := 0
        else axpby(1, x, -1, apply_linop(op.A, y))   -- r = x − A·y
  (α₀, st) = op.scalars(0, op.scalar_init)
  d        = scal(α₀, elementwise_product(op.dinv, r))   -- d = α₀·(dinv ⊙ r)
  for k in 1 .. op.order - 1:
    y           = axpy(1, d, y)                          -- y += d
    r           = axpby(1, r, -1, apply_linop(op.A, d))  -- r −= A·d
    (sd, sr, st) = op.scalars(k, st)
    t           = elementwise_product(op.dinv, r)        -- dinv ⊙ r
    d           = axpby(sd, d, sr, t)                    -- d = sd·d + sr·t
  y = axpy(1, d, y)                                      -- final accumulate
  in y
```

The full L2 action is `sweep` iterated `op.pc_it` times. Each line is a
composition of L1 leaf primitives: one `apply_linop` per residual update and per
direction-image; `axpy` / `axpby` for residual / accumulate / direction updates;
`scal` for the initial direction; `elementwise_product` for the `D⁻¹` action; and
the scalar generator `op.scalars(k, st)` producing `(α₀ | (sd, sr))` and the next
scalar state (4th-kind stateless closed form; 1st-kind `ρ`-threaded).

## L1 form (RHS)

The L1 form names the same polynomial as **one closed-form action** — the
matrix-free evaluation of `p_order(D⁻¹ A)`, applied without exposing the
per-degree recurrence body ([`chebyshev-smoother`](../L1/chebyshev-smoother.md)):

    y_new = chebyshev_smoother(op, x, y_old, initial_guess)
          = y_old + p_order(D⁻¹ A)·(x − A·y_old)        -- repeated op.pc_it times

At L1 the order-`order` recurrence is **below the layer's resolution**: L1 sees a
single closed-form smoother step `y + p_order(D⁻¹ A)·r`, where `p_order` is the
Chebyshev residual-correction polynomial determined by `op.scalars`. The L2
`sweep` body — the `α₀`/`sd_k`/`sr_k`-parameterised direction/residual/accumulate
updates — is fused away into the opaque polynomial action.

## The fusion (L2 → L1)

The lowering is a **resolution collapse**, not an algebraic transformation of the
value: the L2 recurrence *is* the matrix-free evaluation of the L1 polynomial, so
the two compute the same value (modulo floating-point reassociation —
[`chebyshev-iteration`](../L2/chebyshev-iteration.md) law 1). The fusion folds
two distinct structures upward:

1. **Per-degree-step fusion (the primary fusion).** The L2 `order`-step loop —
   each degree `k` performing an `apply_linop` + `axpby` (residual) + a
   `scal`/`axpby` over an `elementwise_product` (direction) + an `axpy`
   (accumulate) — collapses into the single L1 token `p_order(D⁻¹ A)·(·)`. The
   `order` distinct iterations and their ~4 primitive calls each become one
   closed-form polynomial-action name. **This is the fusion**: the explicit
   recurrence's per-degree work is fused into one polynomial-action call whose
   degree and coefficients are closure fields, exactly as the L1 entry's
   §Semantics states ("never materialised as an explicit operator … applied
   matrix-free via a fixed-degree recurrence whose closed-form coefficients
   `op.scalars` generates").
2. **Element-kernel fusion (the secondary, transparent fusion).** Within each L2
   step, the `scal` / `elementwise_product` / `axpby` chain over `dinv` is
   *already* realised in the L0 source as the single element-fused kernels
   `ApplyOrder0` (`d ← sr·dinv·r`) and `ApplyOrderK` (`d ← sd·d + sr·dinv·r`,
   `palace/linalg/chebyshev.cpp:68-78, :112-123`). The L2 entry de-fuses these
   into the base composition and records them as transparent (L2 law 3); the L1
   form re-absorbs them — they are part of the opaque polynomial action. At
   L2>L1 these are *inside* the fused polynomial token, so they need no separate
   treatment here beyond the note that L1 does not see them.

The two scalar generators (4th-kind stateless closed form; 1st-kind `ρ`-threaded)
both fuse into the same `op.scalars` closure field — the **polynomial-kind variant
axis** is absorbed identically at L1 and L2 (it is the closure's identity, not a
runtime branch; L2 law 2 — the primitive *sequence* is variant-invariant).

## Applicability conditions

The fusion preserves the L1 value when:

1. **No bit-exactness promise across fusion choices.** The L2→L1 fusion treats
   the recurrence and the closed-form action as the same algebra at different
   resolution; a fused-FMA element kernel is NOT bit-identical to the unfused
   `scal` + `elementwise_product` + `axpby` chain (L2 non-law). The fusion is
   transparent for *algorithmic correctness* and load-bearing for *bit
   reproduction* (Phillips & Fischer 2022 §3; the standard Palace smoother
   assumption). The lowering is valid under the algorithmic-correctness reading.
2. **Sequentiality is preserved inside the fused token.** The L2 `k`-recurrence
   is genuinely sequential (`d_{k+1}` depends on `r_{k+1}` depends on `d_k`; L2
   non-law) and the monomial-sum expansion is numerically unstable for the
   operative `order` range. The L1 polynomial token does NOT license reordering
   or monomial re-expansion — it names *this* recurrence's value, computed by
   *this* stable three-term scheme. (This sequential obstruction is what blocks
   an L3 global-tensor-field form;
   [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md).)
3. **`pc_it`-sweep sequentiality.** Each L2 sweep recomputes `r = x − A·y` from
   the post-previous-sweep `y`; sweeps do not commute with a cached residual. The
   L1 form preserves this by repeating the polynomial action `pc_it` times over
   the recomputed residual (L1 §Signature "repeated op.pc_it times").
4. **Variant + element-type conformance.** Polynomial-kind (4th / 1st) is the
   `op.scalars` closure identity at both layers; element-type (real / complex) is
   dispatched at the primitive level at L2 and inside the opaque action at L1.
   The fusion holds for all four combinations (the primitive sequence is
   variant-invariant — L2 law 2).

## Justification kind

`algebraic` — the core identity is "the explicit three-term recurrence *is* the
matrix-free evaluation of `p_order(D⁻¹ A)`" (L2 law 1: `chebyshev_iteration(op,
x, y, ig) = chebyshev_smoother(op, x, y, ig)` modulo floating-point
reassociation). The fusion is the algebraic fact that the polynomial action and
its three-term realisation are the same value at different resolution. A
**reduction-chain** flavour is present in the per-step structure (the `order`-step
small-step recurrence reduces to one closed-form action), but the governing
justification is the algebraic recurrence↔polynomial identity, so the theme is
classified `algebraic`. The element-kernel sub-fusion (point 2 of §The fusion) is
a transparent-performance-trick fusion (L2 law 3) nested inside.

## Speculative L1 operators

None. Both anchors are firm
([`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md),
[`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md), both cycle-012
ratified). The L1 leaf primitives the L2 form composes
([`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md),
[`axpby`](../L1/axpby.md), [`scal`](../L1/scal.md)) and the
[`elementwise-product`](../concepts/elementwise-product.md) concept are all
already-firm vocabulary; this theme proposes no new operators.

## Verified-against

L0 evidence ranges (verified via `palace-codemap` read_range this cycle):

- `palace/linalg/chebyshev.cpp:188-220` — 4th-kind `Mult2`: the `order`-step
  recurrence (`ApplyOrder0`, the `k`-loop with `sd`/`sr` closed forms,
  `ApplyOrderK`, the `y += d` accumulates) that L2 makes explicit and L1 fuses.
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2`: same scaffold, the
  `ρ`-threaded scalars.
- `palace/linalg/chebyshev.cpp:68-78` — `ApplyOrder0` (real overload; the
  element-fused initial-direction kernel `d ← sr·dinv·r`; secondary fusion).
- `palace/linalg/chebyshev.cpp:112-123` — `ApplyOrderK` (real overload; the
  element-fused direction-recurrence kernel `d ← sd·d + sr·dinv·r`; secondary
  fusion).

L1 / L2 anchors:

- `book/src/L1/chebyshev-smoother.md` — the firm L1 closed-form action (RHS).
- `book/src/L2/chebyshev-iteration.md` — the firm L2 explicit recurrence (LHS);
  its law 1 is this theme's core identity.

## Status

`firm` — the L2→L1 fusion is the L2 entry's already-firm law 1 (the recurrence
*is* the polynomial action), read as a lowering. Both anchors are firm
(cycle-012 ratified); the fusion is a syntactic resolution-collapse with no
literature inference and no negative-anchor reconstruction. The per-step and
element-kernel structure both read straight off the source. This is the first
chapter under the `book/src/L2-L1/` Part; a `lowering-verifier` audit confirming
the fusion against the L0 source (both kinds) is the standard follow-up, not a
status reduction.

## Open questions / caveats

- **L3 sequential obstruction (downward context, not this theme's concern).** The
  L2 `k`-recurrence and `pc_it`-sweep sequentiality block a global-tensor-field
  L3 form — recorded in [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md)
  non-laws and [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md).
  The cycle-013 wave-1 harvester's L3 chebyshev row treats this; this L2>L1
  theme does not depend on it.
- **Lifting note (reverse direction, working notes only).** Lifting an L1
  polynomial-action token *up* to the L2 explicit recurrence requires knowing the
  `op.scalars` generator (which closed-form / `ρ`-threaded family) and the
  `order` — both are closure fields, so the lift is determinate given the
  closure. This reverse-direction note lives here in working notes, not in the
  formal high→low chapter.
- **Bit-reproduction caveat.** The fusion is transparent only under the
  algorithmic-correctness reading; bit-exact reproduction against any other
  polynomial-evaluation scheme does not hold (L2 non-law). Not a status
  reduction — it is the standard load-bearing-vs-transparent classification, and
  Palace itself uses the fused kernels.
```

```edit:book/src/L1-L0/index.md
| [eigsolve-mutation-rotation](./eigsolve-mutation-rotation.md) | `L1/eigsolve` (rough-in) | `palace/linalg/{arpack,slepc,nleps}.cpp`, `palace/linalg/eps.hpp` | firm *(structural; partly-constructive on LinearSolveFailed)* |
| [chebyshev-smoother-mutation-rotation](./chebyshev-smoother-mutation-rotation.md) | `L1/chebyshev-smoother` (firm) | `palace/linalg/chebyshev.{hpp,cpp}` | firm *(structural; algebraic transpose-alias sub-rule)* |
```

```edit:book/src/L2-L1/index.md
## Theme list

| theme | L2 anchor | L1 anchor | status |
|---|---|---|---|
| [chebyshev-iteration-fusion](./chebyshev-iteration-fusion.md) | `L2/chebyshev-iteration` (firm) | `L1/chebyshev-smoother` (firm) | firm *(algebraic; recurrence↔polynomial fusion)* |
```

**Integrator note (repairer, cycle-013):** the `L2-L1/index.md` edit above is a
**REPLACEMENT** of the Phase-B placeholder, not an append. The current
`L2-L1/index.md` has a fenced placeholder between `## Theme list` and
`## Working Notes`:

```
## Theme list

​```
(empty — Phase B skeleton.)
​```

## Working Notes
```

Apply the edit by replacing the placeholder fence (the three-line
` ``` ` / `(empty — Phase B skeleton.)` / ` ``` ` block) with the `## Theme list`
header + table above, so the rendered page shows only the table — NOT both the
placeholder and the table. (`chebyshev-iteration-fusion` is the first chapter
under the previously-empty L2-L1 Part.)

## SUMMARY.md registration (repairer-added, cycle-013)

Both new chapter files MUST be registered in `book/src/SUMMARY.md` or they are
orphaned from mdBook nav (the dispatch omitted these; surgical inserts added by
the repairer per the `summary-md-surgical-insert` skill — literal-string anchors,
not byte offsets; re-read SUMMARY.md fresh just before each Edit).

L1>L0 chapter — append after the last sibling theme row under the
`# L1 > L0 — Lowering` Part (anchor on the `minres-iteration` row):

```edit:book/src/SUMMARY.md
- [minres-iteration](./L1-L0/minres-iteration.md)
- [chebyshev-smoother-mutation-rotation](./L1-L0/chebyshev-smoother-mutation-rotation.md)
```

L2>L1 chapter — append after the `Overview` row under the `# L2 > L1 — Lowering`
Part (the L2-L1 `Overview` row is the only existing entry; this is the first
chapter; anchor on the L2-L1 `Overview` row, which is unique to that Part):

```edit:book/src/SUMMARY.md
# L2 > L1 — Lowering
- [Overview](./L2-L1/index.md)
- [chebyshev-iteration-fusion](./L2-L1/chebyshev-iteration-fusion.md)
```

## Speculative operators proposed

None. All four anchors are already-firm vocabulary (L1 `chebyshev-smoother`, L2
`chebyshev-iteration`, both ratified cycle-012; plus the firm L1 leaf primitives
`apply_linop`, `axpy`, `axpby`, `scal` and the `elementwise-product` concept).
Both themes are pure lowering descriptions over existing firm operators — no
rough-in operators to hand off to harvester. The one *existing* open candidate
(`spectrum_estimate`, the `SpectralNorm` power-iteration sibling) is already
tracked in the `matrix-weighted-norm-and-bilinear-form` residual-cohort open
question and is treated as opaque by the L1>L0 theme; it is not re-proposed here.

## Supporting evidence

All Palace ranges below were verified via `palace-codemap` `read_range` during
this dispatch:

- `palace/linalg/chebyshev.cpp:13-27` — `GetLambdaMax` overloads (`SpectralNorm`,
  real literal-`true` / complex `A.IsReal()` Hermitian flag).
- `palace/linalg/chebyshev.cpp:55-78` — `ApplyOp` non-accumulating + `ApplyOrder0`.
- `palace/linalg/chebyshev.cpp:80-123` — `ApplyOp` accumulating overload +
  `ApplyOrderK`.
- `palace/linalg/chebyshev.cpp:161-220` — 4th-kind ctor / `SetOperator` / `Mult2`.
- `palace/linalg/chebyshev.cpp:223-293` — 1st-kind ctor / `SetOperator` / `Mult2`.
- `palace/linalg/chebyshev.hpp:30-114` — both class member layouts +
  `Mult`/`MultTranspose`/`Mult2`/`MultTranspose2` forwarding (symmetry alias).
- L1 anchor `book/src/L1/chebyshev-smoother.md` (firm), L2 anchor
  `book/src/L2/chebyshev-iteration.md` (firm) — read in full for vocabulary
  consistency.
- Structural precedents `book/src/L1-L0/axpby-mutation-rotation.md` (sub-pattern
  shape, applicability-condition shape) and
  `book/src/L1-L0/eigsolve-mutation-rotation.md` (partly-constructive precedent —
  determined not to apply here).

## Open questions / caveats (cross-theme)

- **Dead-code complex transpose kernels** (`chebyshev.cpp:101-110, :150-159`):
  defined-not-used under symmetric wiring; recognition rules for potential
  non-symmetric sites. Flag for `lowering-verifier` (L1>L0 theme sub-pattern C).
- **`spectrum_estimate` opacity**: both themes treat the `GetLambdaMax →
  SpectralNorm` setup sub-action as opaque; its L1 firming is the open
  `matrix-weighted-norm-and-bilinear-form` cohort question, not in scope here.
- **MPI single-rank reduction**: the `comm` / `MPI_Comm` argument and `Par*`
  spectral-norm machinery are read single-rank (flagged once per scope policy).
- **Lowering-verifier follow-ups** (both themes, standard, not status
  reductions): (a) L1>L0 — confirm the four sub-patterns match the L0 corpus
  exhaustively across both kinds × both element types × consumer forwarding
  sites; (b) L2>L1 — confirm the per-degree-step fusion against both `Mult2`
  bodies.
- **No partly-constructive sub-part** in either theme: every form is a syntactic
  identity on fully-specified source. The `eigsolve` `LinearSolveFailed`
  partly-constructive precedent was examined and determined not to apply (the
  `MFEM_VERIFY(lambda_max > 0.0)` guard is a setup-time precondition, not a
  reconstructed-from-negative-anchors error condition).
```

