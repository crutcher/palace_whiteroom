---
edges:
  reference:
    - concepts/eigsolve
    - concepts/dot
    - concepts/nrm2
    - concepts/scal
    - concepts/ksp_solve
    - concepts/apply_linop
    - L4/eigsolve
    - L4/ksp_solve
    - L4/fe_assemble
    - L4/fold_solve
    - L3/inner_product
    - L3/linear_combination
    - concepts/sequential-obstruction
    - concepts/scope-out-obstruction
---

# black-box vs accelerated kernels

Cross-cutting **classification-vocabulary** concept page. It names the test the
stack applies, at the bottom (L0/L1), to decide whether an opaque or
special-cased operator **rises** through the layers as a first-class verb or is
**stopped low** in favour of a more general combinator. This is methodology
vocabulary, not an operator: it has no signature or algebraic laws of its own.
The canonical instances it cites — [`eigsolve`](./eigsolve.md),
[`dot`](./dot.md), [`nrm2`](./nrm2.md), [`scal`](./scal.md) — carry their own
authoritative L_n entries; if this page and any L_n entry disagree on a factual
claim about a specific operator, the L_n entry wins.

The page exists because the [vocabulary-shift redirect](../semantics/index.md)
and the **L4-is-the-backend-lowering-target** framing both
turn on the same question — *which operators belong at L4?* — and the answer is
**not** "the ones that don't decompose". It is a three-way judgment about
**abstraction value**.

## One-line statement

Whether a bottom-of-stack operator rises is decided by **abstraction value**,
not by whether it decomposes:

- **no clean decomposition + clean surface** → it is a **black-box kernel** and
  **rises** (opaque body, clean signature) — a first-class primitive, *not* a
  failure;
- **decomposes + literature-standard + simplifies downstream algorithms** → it
  is a **kept named abstraction** and **rises** (its kernel tied below; its
  parent combinator rises too — a permitted dual);
- **decomposes + exists solely for speed + no standalone abstraction value** →
  it is an **accelerated kernel** and is **stopped low** (the general combinator
  rises in its place).

## The discriminating test is judgment, not "does it decompose"

The naive test — *if the operator decomposes into a combinator application,
stop it low; otherwise raise it* — is **wrong**, and the blanket
leaf-collapse that applied it was an over-correction. The decompose-or-not test
alone cannot separate case (2) from case (3): both decompose. The deciding
factor is **abstraction value** — does the named form simplify the description
of downstream algorithms and tie them back to the literature? That is a
per-operator judgment call, made low (where the operator lives), recorded with
its disposition.

## The three dispositions

### 1. Black-box kernel — rises

*Opaque body, clean surface.*

A tensor operation with **no easy decomposition but a clean operation surface**
(signature + semantics), typically carrying a lot of **non-local iterative
value exploration** inside an opaque body. Declaring an operator a black-box
kernel is **permitted when it is necessary to lift the operator through the
layers and there is no straightforward decomposition** — it is a first-class
L4 citizen, *not* a failure or an obstruction. Its clean surface rises to L4;
its body stays opaque, and the **external backend supplies the
implementation** (the backend has its own eigensolver / Krylov solver / ODE
stepper and wants the clean surface, not our decomposition — this is the
**L4-is-the-backend-lowering-target** principle).

Canonical instance: [`eigsolve`](./eigsolve.md) — the SLEPc/ARPACK
generalized-eigenproblem iteration, lifted as a clean-surface verb
([`L4/eigsolve`](../L4/eigsolve.md)) over an opaque `EigSolver[problem]` body.
Sibling black-box kernels:

- [`ksp_solve`](./ksp_solve.md) — the Krylov linear solve, an opaque
  construction-bound `KSP` value behind a clean per-call surface
  ([`L4/ksp_solve`](../L4/ksp_solve.md));
- the **per-element libCEED quadrature leaf** `A(space, ·)` inside
  [`fe_assemble`](../L4/fe_assemble.md) — the element-local→global
  assembly map (restriction + basis-apply + quadrature contraction), an
  upstream-owned (libCEED) opaque kernel that the assemble fold folds over
  *without cracking open*; it rises as an opaque-surface **input** to the
  risen assemble combinator;
- [`fold_solve`](../L4/fold_solve.md)'s per-step `ode->Step` — the opaque
  transient time-step leaf folded by the outer time-marching combinator.

**Positive reframe.** A black-box kernel is the *positive* reading of what the
artifact otherwise files negatively as `obstruction (opaque-library-ownership)`
/ `sequential-obstruction`. For the backend-lowering purpose the opaque
library boundary is exactly what we *want* to preserve, so the same fact that
reads as an obstruction at L3 reads as a clean black-box primitive at L4. This
reframe is **distinct from an unimplemented enum-only Palace stub**
(`obstruction (enum-only-stub)`): a stub names functionality Palace does *not*
implement and stays a true obstruction — there is no clean surface to rise.
A black-box kernel is implemented (by the external library) with a genuinely
clean surface; an enum-only stub is not implemented at all.

### 2. Kept named abstraction — rises

*Decomposes, but earns its name.*

A named operator that **does** decompose into a simple combinator application,
**but** whose simple named definition is **well-studied / literature-standard
and aids the simplification of other algorithms and their tie-back to the
literature**. Do **not** remove such an abstraction just because it has a
replaceable kernel. It earns its place as a first-class named verb that rises
(to L4), with any accelerated kernel tied below it — **and its parent
combinator rises too**, a permitted genuinely-distinct dual (the general
combinator vs. the literature-standard specialization that downstream
algorithms reference by name).

Confirmed keeps:

- [`dot`](./dot.md) — the inner product, the named unit you want in
  "`dot(p, Ap)`" in a CG/GMRES description rather than an inlined
  `inner_product` application;
- [`nrm2`](./nrm2.md) — the 2-norm, the named unit you want in
  "residual `nrm2(r)`".

Both rise as named abstractions; the general combinator
[`inner_product`](../L3/inner_product.md) rises alongside them.

### 3. Accelerated kernel — stopped low

*Decomposes, only for speed.*

A named operator that exists **solely to speed up a common operation that
*does* have a clean decomposition** — a performance-fused special case of a
general combinator, with **no standalone abstraction value**. Disposition:
**identify it low** (at L1/L0 where the fused call lives), **tie it to the
harvested abstract combinator, and prevent it from rising** — the combinator
rises and is applied in its place. A *pure* accelerated kernel correctly gets
**no** L2/L3/L4 chapter; the combinator does.

Per-case candidate family (judged operator-by-operator, leaning toward fusion):
the [`scal`](./scal.md) / `axpy` / `axpby` / `axpbypcz` fused-update routines
over the general combinator [`linear_combination`](../L3/linear_combination.md).
These are named BLAS routines that lean toward fusion; the per-case judgment is
whether the named form aids downstream algorithm clarity / literature tie-back
(if not → stop low, the combinator rises in its place).

## The combinators rise regardless

Whichever disposition a special-cased operator lands in, the general
combinators it specializes — [`linear_combination`](../L3/linear_combination.md)
and [`inner_product`](../L3/inner_product.md) — **rise to L4 regardless**. They
are feature-surface verbs the backend wants. In case (2) they rise *alongside*
the kept named abstraction (the dual); in case (3) they rise *in place of* the
stopped-low accelerated kernel. (Both combinators currently stop at L3 and are
queued to rise to L4 — see the L3 entries.)

## See also

- [`eigsolve`](./eigsolve.md) — canonical black-box kernel (case 1).
- [`dot`](./dot.md), [`nrm2`](./nrm2.md) — kept named abstractions (case 2).
- [`scal`](./scal.md) — accelerated-kernel-family candidate (case 3).
- [`fe_assemble`](../L4/fe_assemble.md) — the assemble fold (combinator,
  rises) over the libCEED quadrature leaf (black-box kernel, rises as input).
- [`sequential-obstruction`](./sequential-obstruction.md),
  [`scope-out-obstruction`](./scope-out-obstruction.md) — the negative filings
  that case (1) positively reframes (where the surface is genuinely clean).
