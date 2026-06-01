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
  argument; `d` (the direction) is a *member* workspace (`chebyshev.hpp:44` —
  `mutable VecType d, r;`; `:43` is the explanatory comment). Both are written
  every step and carry no value across
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
- `palace/linalg/chebyshev.cpp:190-220` — `ChebyshevSmoother<OperType>::Mult2`
  (4th-kind, signature-to-close; corrected from `:188-220`, whose start was the
  prior `SetOperator` close brace — the signature is `:190`, opening brace `:191`,
  close `:220`): the `pc_it` outer sweep, the `initial_guess` branch, the in-place
  `y += d` / `y = 0.0`, the scribbled `r` / `d`, the `ApplyOrder0` / `ApplyOrderK`
  diagonal-scaled passes.
- `palace/linalg/chebyshev.cpp:261-293` —
  `ChebyshevSmoother1stKind<OperType>::Mult2`: identical scaffold, 1st-kind
  scalars.
- `palace/linalg/chebyshev.hpp:44` — `mutable VecType d, r;` (the two scribbled
  workspaces; `d` is a member, `r` is passed; corrected from `:43`, which is the
  explanatory comment).

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
(`palace/linalg/chebyshev.cpp:102-110, :147-155`) but are dead code under the
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
- `palace/linalg/chebyshev.cpp:169-188` — 4th-kind `SetOperator` (corrected from
  `:169-186`, which undershot the close brace `:188`, missing `this->width`@187):
  capture `A`, `AssembleDiagonal(dinv); dinv.Reciprocal()`, `lambda_max = sf_max *
  GetLambdaMax(...)`, `MFEM_VERIFY(lambda_max > 0.0, …)`.
- `palace/linalg/chebyshev.cpp:232-258` — 1st-kind `SetOperator` (corrected from
  `:232-259`, one past the close brace `:258`): same scaffold + `sf_min` default,
  `theta`, `delta`.
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
- `palace/linalg/chebyshev.cpp:161-188` — 4th-kind ctor + `SetOperator`
  (`SetOperator` close brace is `:188`; corrected from `:161-186`).
- `palace/linalg/chebyshev.cpp:190-220` — 4th-kind `Mult2` (signature-to-close;
  corrected from `:188-220`, whose start was the prior fn close brace — sig `:190`,
  brace `:191`): in-place `y`, `r`, `d`; `ApplyOrder0` / `ApplyOrderK`
  diagonal-scaled passes.
- `palace/linalg/chebyshev.cpp:223-258` — 1st-kind ctor + `SetOperator`
  (`sf_min` default, `theta`, `delta`; `SetOperator` close brace is `:258`,
  corrected from `:223-259`).
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2`.
- `palace/linalg/chebyshev.cpp:295-299` — element-type instantiations.
- `palace/linalg/chebyshev.hpp:30-44` — 4th-kind member layout (`mutable VecType
  d, r;` is `:44`, `:43` the explanatory comment; `dinv`, `lambda_max`, `sf_max`;
  corrected from `:30-43`).
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

Lowering-verifier audit (cycle-014, verdict **CONFIRMS-WITH-REFINEMENT** — no
semantic defect; firm status retained):

```yaml
verified_against:
  - citation: palace/linalg/chebyshev.cpp:190-220
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind Mult2 signature-to-close; corrected from :188-220 (start was prior fn close brace; sig is :190, brace :191)
  - citation: palace/linalg/chebyshev.cpp:261-293
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
  - citation: palace/linalg/chebyshev.cpp:169-188
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind SetOperator; corrected from :169-186 (end undershot close @188)
  - citation: palace/linalg/chebyshev.cpp:232-258
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 1st-kind SetOperator; corrected from :232-259 (end was 1 past close @258)
  - citation: palace/linalg/chebyshev.cpp:13-27
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: GetLambdaMax real(:18 true)/complex(:27 A.IsReal()); DinvA=Dinv*A
  - citation: palace/linalg/chebyshev.cpp:183-184
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: 4th-kind MFEM_VERIFY(lambda_max>0) setup precondition (1st-kind :250-251)
  - citation: palace/linalg/chebyshev.hpp:44
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: mutable VecType d, r (member d, passed r); corrected from :43 (:43 is the explanatory comment, member is :44)
  - citation: palace/linalg/chebyshev.hpp:50-76
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: Mult resize-forward + Mult2 decl + MultTranspose2 symmetry alias
  - citation: palace/linalg/chebyshev.cpp:295-299
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: both-kind x both-element-type instantiations
  - citation: palace/linalg/distrelaxation.cpp:36
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: B_G->SetInitialGuess(false) per-call initial_guess control (exact line 36)
  - citation: palace/linalg/chebyshev.cpp:102-110,147-155
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules); first-kernel start tightened from :101-110 to :102-110 (:101 is the close brace of the non-transpose if-branch; the dead else-block is :102-110) (cycle-040 D3); second-kernel range tightened from :150-159 to :147-155 (cycle-035 D1)
```

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

- **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:102-110,
  :147-155` define conjugate-`dinv` transpose elementwise kernels that are
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
