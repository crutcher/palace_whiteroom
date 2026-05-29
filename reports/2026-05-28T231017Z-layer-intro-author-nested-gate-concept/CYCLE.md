---
agent: layer-intro-author
invoked_at: 2026-05-28T231017Z
scope: concepts/nested-constructed-operator-gate page authorship (OQ prong a)
status: integrated
integrated_at: 2026-05-29T030000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-018 finalize — concepts/nested-constructed-operator-gate.md authored (new concept page; inbound link from divfree-projector-mutation-rotation + outbound link to constructed-operator-factory) + SUMMARY register; prong (a) of OQ nested-constructed-operator-gate-concept-and-divfree-correction (resolved). +1 concept page."
---

# CYCLE: concepts/nested-constructed-operator-gate

## Summary

Author a new cross-cutting concept page `book/src/concepts/nested-constructed-operator-gate.md`
naming the structural shape **a constructed-operator gate whose closure carries
one or more further constructed-operator gates as sub-fields** (gate-carrying-gate),
plus its SUMMARY.md registration under the concepts Part.

The ≥2-firm-instance bar is cleared (cycle-017 cross-layer-cross-cutter audit,
critic VERIFIED-SOUND): `eigsolve` (firm, cycle-011 `8bb16b7`) carries TWO nested
gates (`E.linear : Solver[A]`, `E.projector : Maybe DivFreeSolver`); `divfree-projector`
(firm, cycle-016 `b54ea1c`) carries ONE (`P.ksp : Solver[P.M]`). The page encodes:
the structural shape; the **cross-layer fidelity rule** (the inner gate's iteration
stays interior to its OWN lowering theme and does not leak into the outer theme — at
the outer theme's resolution the inner gate is an opaque action); the two firm
instances with citations; the latent `ksp_solve` preconditioner site; the
**transitive-nesting** observation (`eigsolve ⊃ divfree ⊃ ksp`, three-deep); and the
sibling relationship to `constructed-operator-factory` (factory = the materialisation
site of a gate; nested-gate = the composition of gates).

This is a **documentation/fidelity** concept (how nested themes delegate), not a new
evaluation primitive — per the cross-cutter's concept-vs-combinator boundary, the
concept page is the right first home; combinator-mining defers until/unless the
nesting needs calculus-level support.

Addresses OQ `nested-constructed-operator-gate-concept-and-divfree-correction`
**prong a**. Prong b (the divfree-theme "first" / "no other op" correction) is a
separate cycle-018 lifter/harvester dispatch (out of my authority — surfaced in Open
questions, not enacted here).

## Proposed changes

### 1. New concept page (create file)

```edit:book/src/concepts/nested-constructed-operator-gate.md
[old]: <new file — no prior content>
[new]: # nested-constructed-operator-gate

A layer-pattern concept naming the structural shape in which a
[`constructed-operator`](./constructed-operators.md) gate's closure carries **one or
more further constructed-operator gates as sub-fields**. The outer gate's per-call
body invokes the inner gate(s) as opaque operator actions; the inner gate's own
iteration is never spelled out at the outer gate's resolution. This is the
*composition-of-gates* counterpart to [`constructed-operator-factory`](./constructed-operator-factory.md)
(which names the *construction* site of a single gate).

## Background

A *constructed-operator gate* (see [`constructed-operators`](./constructed-operators.md)
and [`solver-as-operator`](./solver-as-operator.md)) is a value materialised at
construction — an opaque handle that internalises one or more variant axes and is
invoked through a uniform operator interface. The basic shape is one gate over raw
operators and tensors: e.g. `chebyshev-smoother`'s closure carries `op.A :
LinearOperator[N, N]`, a **raw** operator (`book/src/L1/chebyshev-smoother.md:58`),
not a gate.

The *nested* shape is one level up: the closure's sub-field is **itself a gate**
(`Solver[A]`, `DivFreeSolver`, …), not a raw operator. The distinguishing test:

- **raw-operator field** → not nesting. `op.A : LinearOperator[N, N]`
  (`chebyshev-smoother`), `apply_linop`'s operand argument. The field is applied as a
  matrix-vector product; there is no inner solve loop.
- **gate field** → nesting. `E.linear : Solver[A]` (`eigsolve`), `P.ksp : Solver[P.M]`
  (`divfree-projector`). The field is itself a construction-bound solver carrying its
  own iteration, preconditioner, tolerances, and variant absorption.

The pattern is structural to the whole constructed-operator family — a solver
absorbs a preconditioner, an eigensolver absorbs an inner linear solver, a projector
absorbs an inner H1 solve — and it is load-bearing across the eigenmode pipeline (see
the transitive-nesting note below), which is why it earns a named concept rather than
ad-hoc per-instance prose.

## The cross-layer fidelity rule

The reason this shape needs a name is a **lowering discipline**: when an L_{n}>L_{n-1}
mutation-rotation theme lowers the outer gate, the inner gate's iteration **stays
interior to the inner gate's OWN lowering theme** and does not leak into the outer
theme. At the outer theme's resolution the inner gate is an **opaque action**:

- `divfree-projector`'s `ksp->Mult(rhs, psi)` is the opaque `K⁻¹` action; its CG
  iteration is interior to [`ksp_solve`](./ksp_solve.md) and does not appear in the
  divfree theme (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`).
- `eigsolve`'s ten `opInv->Mult(b, x)` call sites are each the opaque inner-solve
  action; each "rewrites by the firm `ksp-solve-mutation-rotation` theme"
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`, the **core sub-pattern** of
  the eigsolve theme) — the inner solve's body is NOT re-narrated inside the eigsolve
  theme.

This is the "composed-not-inherited" remark at `book/src/L1/eigsolve.md:140`: the
outer gate *composes against* the inner gate (delegating to its theme) rather than
*inheriting* its body (re-spelling the iteration). The fidelity claim is that the
outer theme is faithful precisely **because** it treats the inner gate opaquely — the
nested iteration is the inner theme's concern, and the lowering of the whole is the
**composition** of the two adjacent-edge themes, not a single flattened rewrite. A
theme that re-spelled the inner iteration would double-count the rotation and lose the
single-point-of-truth for the inner gate.

## Firm instances

Two FIRM L1 operators exhibit the gate-carrying-gate shape; a third site is latent.

- **`eigsolve`** (firm structure; cycle-011, `8bb16b7`) — **two** nested gates. The
  closure `E` binds `E.linear : Solver[A]` (the inner Krylov solver invoked per
  RCI / shell-matrix callback for spectral-transformation modes) and `E.projector :
  Maybe DivFreeSolver[ComplexVector]` (the optional divergence-free projector)
  (`book/src/L1/eigsolve.md:60`). The L1 entry already names the shape in prose: "the
  first L1 operator to compose two layers of constructed-operator absorption"
  (`book/src/L1/eigsolve.md:136`) and "structurally the same nesting pattern …
  composed-not-inherited" (`book/src/L1/eigsolve.md:140`). The theme's **core
  sub-pattern B** lowers each of the ten `opInv->Mult` inner-solve call sites through
  the firm [`ksp_solve`](./ksp_solve.md) theme
  (`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258`). The eigsolve theme is
  `firm (structural)`; its `LinearSolveFailed` sub-part is a *separate*
  partly-constructive status concern about a discarded convergence status, **not**
  about the gate-nesting structure — the nesting (sub-pattern B) is itself firm and
  source-anchored, so `eigsolve` is a clean FIRM instance of this shape independent of
  that caveat.

- **`divfree-projector`** (firm; cycle-016, `b54ea1c`) — **one** nested gate. The
  closure `P` binds `P.ksp : Solver[P.M]` (a CG solver bound to the ε-weighted H1
  mass-like operator `P.M` as both operator and preconditioner target), materialised
  at construction (`book/src/L1-L0/divfree-projector-mutation-rotation.md:193-198`).
  Its per-call `ksp->Mult(rhs, psi)` is the opaque inner H1 solve
  (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113`,
  `book/src/L1/divfree-projector.md`).

**Transitive nesting (three-deep).** `E.projector : Maybe DivFreeSolver` means the
`divfree-projector` gate is *itself* a sub-field of the `eigsolve` closure — so the
two instances are not merely parallel, they are transitively nested:

    eigsolve  ⊃  divfree-projector  ⊃  ksp_solve
      (E)            (E.projector)         (P.ksp)

The eigsolve outer loop carries a divfree projector, which carries its own inner CG
solve. The fidelity rule applies at each edge: the eigsolve theme treats `E.projector`
opaquely; the divfree theme treats `P.ksp` opaquely. This three-deep transitivity is
direct evidence the pattern is load-bearing across the eigenmode pipeline, not
incidental.

**Latent site — `ksp_solve` preconditioner.** `ksp_solve`'s closure `K` binds a
preconditioner `M⁻¹` (`book/src/L1/ksp_solve.md:31`). Via [`solver-as-operator`](./solver-as-operator.md),
a preconditioner **is-an** operator and may itself be a `Solver`-typed handle (a
nested `ksp` used as a preconditioner). When `K.M⁻¹` is a `Solver`, `ksp_solve` is
*also* gate-carrying-gate. But the L1 `ksp_solve` entry types `M⁻¹` as a plain
`LinearOperator[N, N]` and the `ksp-solve-mutation-rotation` theme treats the
preconditioner opaquely, so this is a **latent** nesting site, not a confirmed firm
instance (no concrete Palace site where a `BaseKspSolver`'s preconditioner is itself a
`BaseKspSolver` has been verified against L0 source — flagged for a future harvester).
Chebyshev-as-preconditioner inside a Krylov method is a related but **weaker** nesting
(`book/src/L1/chebyshev-smoother.md:140`): chebyshev is a smoother-as-operator, not a
`Solver`-gate.

## Relationship to siblings

- [`constructed-operator-factory`](./constructed-operator-factory.md) — **the
  materialisation site** of a single gate (consumes a config record + context, returns
  a typed gate). This page is the **composition** counterpart: a gate whose closure
  *carries* another gate that some factory already materialised. The factory answers
  "where is a gate built?"; nested-gate answers "what happens when a gate's field is
  another gate?".
- [`solver-as-operator`](./solver-as-operator.md) — the type-level rotation that lets
  an inner gate appear as an operator-typed sub-field (`Solver<OperType>` IS-A
  `OperType`), which is precisely what makes the latent `ksp_solve` preconditioner
  site possible.
- [`constructed-operators`](./constructed-operators.md) / [`variant-absorption`](./variant-absorption.md)
  — the absorption motif each gate (inner and outer) realises.

## See also

- [`ksp_solve`](./ksp_solve.md) — the innermost gate in every instance here; the inner
  iteration's home theme.
- `book/src/L1-L0/eigsolve-mutation-rotation.md` §"Sub-pattern B" — the two-gate
  instance's lowering (delegates to `ksp-solve-mutation-rotation`).
- `book/src/L1-L0/divfree-projector-mutation-rotation.md` §"Sub-pattern A" / §"Sub-pattern C"
  — the one-gate instance's lowering + closure-field materialisation.
```

### 2. SUMMARY.md registration (concepts Part)

Register the new page as the final concepts entry, after `scalar-promotion`
(line 151) and before the blank line that closes the concepts Part. Plain-text-safe:
the target file is created by change (1) above, so the live link is firm.

```edit:book/src/SUMMARY.md
[old]:   - [scalar-promotion](./concepts/scalar-promotion.md)

# Design Artifacts
[new]:   - [scalar-promotion](./concepts/scalar-promotion.md)
  - [nested-constructed-operator-gate](./concepts/nested-constructed-operator-gate.md)

# Design Artifacts
```

## Supporting evidence

All citations self-verified via `Read` against the cited artifact lines (no
from-memory citations):

- `book/src/L1/eigsolve.md:60` — VERIFIED: `E` binds `linear : Solver[A]` … `projector
  : Maybe DivFreeSolver[ComplexVector]` (two nested gates) + `B : Maybe
  LinearOperator[N, N]`.
- `book/src/L1/eigsolve.md:136` — VERIFIED verbatim: "**This is the second L1 operator
  (after `ksp_solve` itself depending on `apply_linop`) whose primary dependency is
  itself a constructed-operator type**, making `eigsolve` the first L1 operator to
  compose two layers of constructed-operator absorption."
- `book/src/L1/eigsolve.md:140` — VERIFIED: "This is structurally the same nesting
  pattern as preconditioner application inside an iterative solver —
  composed-not-inherited."
- `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — VERIFIED: "### Sub-pattern B
  — inner-solve mutation-rotation … This is the **core sub-pattern** of the theme …
  ten `opInv->Mult(b, x)` call sites … Each `opInv->Mult(b, x)` rewrites by the firm
  `ksp-solve-mutation-rotation` theme." The "firm" attribution is at `:251` ("rewrites
  by the firm `ksp-solve-mutation-rotation` theme"); the theme header (`:1-16`) confirms
  the structured-opaque-primary-argument framing and lists the two nested sub-fields.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113` — VERIFIED:
  "**Inner solve is itself a constructed-operator gate.** `ksp->Mult(rhs, psi)` … Its
  CG iteration is interior to `ksp_solve` and does not leak into this theme; here it is
  the opaque `K⁻¹` action." (Note: this passage's "**first**" claim is the prong-b
  correction target — see Open questions.)
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:193-198` — VERIFIED: "`P.ksp`
  ← a CG solver bound to `P.M` … The inner constructed-operator gate; see `ksp_solve`."
- `book/src/L1/ksp_solve.md:31` — VERIFIED: "`K` additionally binds an optional
  preconditioner `M⁻¹` (also a `LinearOperator[N, N]`)" (latent gate-carrying-gate via
  `solver-as-operator`).
- `book/src/L1/chebyshev-smoother.md:58` — VERIFIED: "`op.A : LinearOperator[N, N]` —
  the captured SPD system operator" (RAW operator, negative case).
- `book/src/L1/chebyshev-smoother.md:140` — referenced by the cross-cutter for the
  "used as `B` preconditioner" weaker-nesting note; cited indirectly (chebyshev =
  smoother-as-operator, not a `Solver`-gate).
- `book/src/concepts/constructed-operator-factory.md:1-42` — VERIFIED: the sibling
  concept (no frontmatter, starts with `# constructed-operator-factory`); the new page
  matches its format (title heading, `## Background`, `## See also`, relative-path
  `./concepts/*.md` links).
- `book/src/concepts/solver-as-operator.md:1-12` — VERIFIED: `Solver<OperType>` IS-A
  `OperType` rotation; supports the latent-site reasoning.
- Provenance: cross-cutter report cites `git log` — `8bb16b7` (cycle-011, eigsolve
  theme) predates `b54ea1c` (cycle-016, divfree theme) by five cycles. Not
  independently re-run; inherited from the VERIFIED-SOUND audit.

Format/structure: the page matches `constructed-operator-factory.md` (no YAML
frontmatter — concept pages start directly with `# <slug>`; `## Background` +
`## See also` sections; relative `./<slug>.md` links within `concepts/`). It does NOT
restate the operators' algebraic laws (those live in the L1 entries); it forwards
citations to the L1 entries and themes per role-spec concept-page discipline.

## Open questions / caveats

- **Prong b is NOT enacted here** (out of authority). The divfree theme's three
  "first" / "no other current L1 op" claims
  (`book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113` "the first L1>L0
  mutation-rotation whose closure carries another constructed-operator gate";
  `:457-464` "the first such case … shared with no other current L1 op"; OQ-ledger
  `:2897`) are inaccurate against `eigsolve` (firm, five cycles earlier). These need a
  scoped cycle-018 **lifter/harvester** correction dispatch on the divfree theme
  (append-only after `integrated_at:`) to cite `eigsolve-mutation-rotation` sub-pattern
  B as the prior, richer (two-gate) instance and re-point the in-line note at this new
  concept page once it lands. The new page already states `eigsolve` is the prior
  instance, so it does not propagate the "first" error — but the divfree theme still
  carries it until prong b runs.

- **`ksp_solve` preconditioner-as-`Solver` listed as LATENT, not firm.** I did not
  confirm a concrete Palace L0 site where a `BaseKspSolver`'s preconditioner is itself
  a `BaseKspSolver` (the cross-cutter explicitly did not either). The page lists it as
  a latent site with that caveat; a future harvester should confirm before promoting it
  to a firm instance. If confirmed, the page's "Latent site" paragraph should be
  promoted into the "Firm instances" list.

- **Concept vs combinator boundary (flagged, not pre-decided).** The page is a
  documentation/fidelity convention (how nested themes delegate), not a new evaluation
  primitive. If a later cycle finds the nesting needs explicit calculus-level support
  (e.g. an L4 `withInnerSolver` bracket), re-route to `combinator-miner`. The page does
  not foreclose that.

- **Eigsolve theme `firm (structural)` vs `partly-constructive` `LinearSolveFailed`.** I
  confirmed (per the cross-cutter's resolution-disposition note + the theme's
  sub-pattern B text at `:213-258` and the L1 entry's §3 / §Signature callout) that the
  nesting sub-pattern is firm and source-anchored; the partly-constructive caveat is
  about the discarded inner-solve convergence status (`LinearSolveFailed`), a separate
  status concern, NOT the gate-nesting structure. The page cites `eigsolve` as a clean
  FIRM instance of the nesting shape on that basis and states the distinction
  explicitly so a reader does not mistake the `LinearSolveFailed` caveat for a caveat on
  the nesting.

- **OQ `nested-constructed-operator-gate-concept-and-divfree-correction` prong a is the
  deliverable of this report;** prong b + the OQ ANSWER of the refuted
  `closure-nesting-constructed-gate-carrying-constructed-gate` premise are integrator /
  separate-dispatch concerns surfaced here for routing.
