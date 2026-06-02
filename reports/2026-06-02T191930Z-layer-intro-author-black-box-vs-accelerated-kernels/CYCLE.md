---
agent: layer-intro-author
invoked_at: 2026-06-02T191930Z
scope: concepts/black-box-vs-accelerated-kernels (NEW concept page) + SUMMARY.md alpha-wire
status: pending
integrated_at: 2026-06-02T193833Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-067 D3 — applied clean. NEW concepts/black-box-vs-accelerated-kernels.md (directive-2 classification-vocabulary page) + SUMMARY.md concepts-list alpha-insert between axpy and dot (LOCAL alpha head-cluster — GLOBAL re-sort + by-kind grouping is the batch-21 meta-phase reorg). Applied the repairer-fixed body (both L4-is-the-backend-lowering-target refs plain-text per repair option-b). 3 OQs promoted. Build-relevant; cargo make book exit 0; page renders. Staging row: cycle-067-integrator-staging/STAGING.md."
---

# CYCLE: concepts/black-box-vs-accelerated-kernels

## Summary

Authors the NEW cross-cutting concept page `book/src/concepts/black-box-vs-accelerated-kernels.md`
(canonical slug `black-box-vs-accelerated-kernels`; verified-ABSENT this cycle) and wires it into the
`SUMMARY.md` concepts list in ALPHA position (directive-3 active-immediately: between `axpy` and
`build-time-vs-run-time-stratification`).

The page is the **classification-vocabulary home** for the directive-2 three-way disposition of
opaque / special-cased / named-abstraction operators at the bottom of the stack — the shared vocabulary
that D2's survey and the batch-21 lift dispatches consume. It is synthesized FROM the project memory
`project_blackbox_vs_accelerated_kernels` + the `scaffolding/priorities.md` directive-2 banner (NOT a fresh
derivation), per the dispatch spec.

This is a concept (vocabulary/structure) page: it states one-line semantics + the discriminating test +
the three dispositions, forwards all algebraic detail to the canonical-instance chapters, and does NOT
restate operator laws (the L_n entries win on any factual disagreement). All cross-references are live
links to chapters verified present on disk; no new L0 source-line ranges are emitted (so the close-brace
on-disk-END discipline has no source-range targets in this dispatch — the one source pinpoint forwarded in
prose, the libCEED `A(space, ·)` leaf, is cited only by reference to `L1/fe_assemble`, which carries the
verified `palace/fem/bilinearform.cpp` anchors itself).

## Proposed changes

```edit:book/src/concepts/black-box-vs-accelerated-kernels.md
[old]:
[new]:
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

The page exists because the [vocabulary-shift redirect](../design/l4_calculus.md)
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
stop it low; otherwise raise it* — is **wrong**, and the 2026-06-01 blanket
leaf-collapse that applied it was an over-correction. The decompose-or-not test
alone cannot separate case (2) from case (3): both decompose. The deciding
factor is **abstraction value** — does the named form simplify the description
of downstream algorithms and tie them back to the literature? That is a
per-operator judgment call, made low (where the operator lives), recorded with
its disposition.

## The three dispositions

### 1. Black-box kernel — rises (opaque body, clean surface)

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
  [`fe_assemble`](../L1/fe_assemble.md) — the element-local→global
  assembly map (restriction + basis-apply + quadrature contraction), an
  upstream-owned (libCEED) opaque kernel that the assemble fold folds over
  *without cracking open*; it rises as an opaque-surface **input** to the
  assemble combinator;
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

### 2. Kept named abstraction — rises (decomposes, but earns its name)

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

### 3. Accelerated kernel — stopped low (decomposes, only for speed)

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
- [`fe_assemble`](../L1/fe_assemble.md) — the assemble fold (combinator,
  rises) over the libCEED quadrature leaf (black-box kernel, rises as input).
- [`sequential-obstruction`](./sequential-obstruction.md),
  [`scope-out-obstruction`](./scope-out-obstruction.md) — the negative filings
  that case (1) positively reframes (where the surface is genuinely clean).
```

```edit:book/src/SUMMARY.md
[old]:  - [axpy](./concepts/axpy.md)
  - [dot](./concepts/dot.md)
[new]:  - [axpy](./concepts/axpy.md)
  - [black-box vs accelerated kernels — methodology concept](./concepts/black-box-vs-accelerated-kernels.md)
  - [dot](./concepts/dot.md)
```

## Supporting evidence

- **Synthesis sources** (per dispatch spec — NOT a fresh derivation):
  - project memory `project_blackbox_vs_accelerated_kernels` (the three-way
    disposition, the keep-and-rise refinement for `dot`/`nrm2`, the
    combinators-rise-regardless rule, the FE-cohort→L4 fold-vs-leaf split).
  - `scaffolding/priorities.md` directive-2 banner (active-head item 4).
- **Canonical-instance chapters cited** (all verified present on disk this
  cycle — live links, no plain-text-defer needed):
  - `book/src/L4/eigsolve.md`, `book/src/concepts/eigsolve.md` (case 1 canonical).
  - `book/src/concepts/dot.md`, `book/src/concepts/nrm2.md` (case 2 keeps).
  - `book/src/concepts/scal.md` (case 3 family candidate).
  - `book/src/L1/fe_assemble.md` (FE fold + libCEED leaf; the §"Role in the
    fold" / `A(space, ·)` opaque-leaf framing at its lines 79-81, 171-176 is
    the source of the quadrature-leaf-as-black-box-kernel claim — that chapter
    carries the verified `palace/fem/bilinearform.cpp:67-70` / `:87-90`
    anchors, which this page forwards to rather than re-citing).
  - `book/src/L4/ksp_solve.md`, `book/src/concepts/ksp_solve.md`,
    `book/src/L4/fold_solve.md` (sibling case-1 black-box kernels).
  - `book/src/L3/linear_combination.md`, `book/src/L3/inner_product.md` (the
    combinators that rise regardless).
- **SUMMARY alpha placement verified**: `black-box-vs-accelerated-kernels`
  sorts after `axpy` (line 221) and before
  `build-time-vs-run-time-stratification` (line 248 in the current file). The
  concepts list is NOT globally alpha-sorted (it is roughly insertion-ordered
  with a small alpha-sorted BLAS-1 cluster `apply_linop`/`axpy`/`dot`/`nrm2`/
  `scal` at its head); the directive-3 alpha target lands the new page inside
  that head cluster, immediately after `axpy`. See Open questions for the note
  on the `build-time-...` page's current non-adjacent position.

## Open questions / caveats

- **Directive-3 alpha-position interpretation.** The dispatch spec says the new
  page "sorts between `axpy` and `build-time-vs-run-time-stratification`". In
  the current `SUMMARY.md` concepts list these two are NOT adjacent
  (`build-time-vs-run-time-stratification` is at line 248, far below the
  `axpy`/`dot`/`nrm2`/`scal` head cluster at lines 221-224). The list is only
  *locally* alpha-sorted (the head BLAS-1 cluster), not globally. I placed the
  new page **immediately after `axpy`** (the in-cluster alpha position),
  matching the literal "between axpy and build-time-..." span and the
  active-head BLAS-1 cluster it conceptually belongs to. If directive-3 intends
  a *global* alphabetical re-sort of the whole concepts list, that is a larger
  reorg (the meta-phase's one-time concepts-list alpha reorg per the
  `mdbook-subchapter-grouping-and-alpha-api` directive) and is OUT of this
  single-page dispatch's scope — flagging so the integrator/meta-phase can
  decide whether the head-cluster insert is the intended interim or whether the
  global re-sort should subsume it.
- **`L4/fe_assemble.md` is absent on disk.** The FE-cohort→L4 lift (assemble
  fold rises as combinator; quadrature leaf rises as opaque input) is described
  in this page via the **L1** chapter [`L1/fe_assemble`](../L1/fe_assemble.md)
  (which exists and carries the opaque-leaf framing). I did NOT live-link an
  `L4/fe_assemble.md` (it would be a `linkcheck2` build error per the
  `rough-in-rows-must-be-plain-text-when-anchor-missing` convention). When the
  FE-cohort L4 lift lands (a batch-21+ harvester item), the See-also and the
  case-1 sibling list here should gain the `L4/fe_assemble` live link. Recorded
  as a forward-reference, not a defect.
- **No new L0 source ranges emitted** — so the recurrence-6 close-brace
  on-disk-END discipline has no source-range targets in this dispatch. The one
  source pinpoint the prose leans on (the libCEED `A(space, ·)` leaf at
  `palace/fem/bilinearform.cpp:67-70` / `:87-90`) is owned and verified by
  `L1/fe_assemble`, not re-cited here; this page forwards to that chapter per
  the concept-page discipline (do not re-cite the L_n entry's anchors).
- **`ksp_solve` as black-box kernel vs. its existing L4 chapter.** This page
  classifies `ksp_solve` as a case-1 black-box kernel. `L4/ksp_solve.md`
  already exists as a clean-surface verb, consistent with that classification.
  No contradiction; noting it because `ksp_solve` also has a rich internal
  Krylov decomposition (krylov-step) at lower layers — the case-1 classification
  is about the *L4 surface* (opaque solver value), not a claim that the Krylov
  iteration is indecomposable below. If D2's survey or a future cross-cutter
  reads this as "ksp_solve has no decomposition", that would be a misreading —
  the page says no clean decomposition *at the surface the backend consumes*.
