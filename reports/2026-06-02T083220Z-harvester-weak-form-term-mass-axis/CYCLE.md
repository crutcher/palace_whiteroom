---
agent: harvester
invoked_at: 2026-06-02T083220Z
scope: L1 operator: weak_form_term (Identity/mass axis-point grounding, in-place)
status: pending
integrated_at: 2026-06-02T103000Z
integration_commit: 4d621d1
integration_notes: "Applied clean by integrator-per-report (D1) at 2026-06-02T085600Z; finalized cycle-062. In-place x3 grounding of the Identity/mass variant-axis point 2-of-4 -> 3-of-4 (VectorFEMassIntegrator @ spaceoperator.cpp:278); NO count change, status stays firm. All 3 edit: anchors matched after a leading-whitespace correction. citecheck --scan 23 ok / 0 failing. Critic/repairer off-by-one finding repaired report-side pre-integration, never reached the artifact. Build clean (cargo make book exit 0)."
inputs:
  - book/src/L1/weak_form_term.md (firm entry, c061 D1)
  - cycle-062 dispatch D1 scope (ground the Identity/mass differential-operator axis point as a specialization note in-place)
  - palace/models/spaceoperator.cpp (GetMassMatrix + AddIntegrators VectorFEMassIntegrator fold)
  - palace/fem/integrator.hpp (MassIntegrator / VectorFEMassIntegrator wrapper declarations)
---

# CYCLE: Ground the Identity/mass axis point of weak_form_term at L1 (in-place)

## Summary
The firm L1 `weak_form_term` entry (c061 D1) carries a four-point **differential-operator** variant axis
(`Gradient | Identity | Curl | Divergence`), of which two points were GROUNDED by in-scope solver-K witnesses
(Gradient/electrostatic, Curl/magnetostatic) and two were named **pending-pull siblings** (Identity/mass,
Divergence/div-div). This dispatch GROUNDS the **Identity/mass** axis point in-place: the mass term is concretely
pulled by `SpaceOperator::GetMassMatrix` (`palace/models/spaceoperator.cpp:438`), which folds a
`VectorFEMassIntegrator` term via `AddIntegrators` (`a.AddDomainIntegrator<VectorFEMassIntegrator>(*f)`,
`palace/models/spaceoperator.cpp:278`) — the SAME `BilinearForm`-fold as the c061 curl-curl pull, differing only
in the integrator slot. The Identity term is `(Q, I)`: the identity differential operator (`𝒟u = u`, no
derivative), with mass coefficient `*f`. This is an **in-place axis-point grounding** (combinator-primary per the
2026-06-01 redirect §1: the term abstraction is the entry; the differential-operator variants are specialization
notes under it) — NOT a new mirrored entry, NO new chapter, NO new dep-map row, NO SUMMARY line. The variant axis
is now **3-grounded-of-4** (Divergence/div-div remains the only pending-pull sibling — unchanged, no in-scope
solver-K witness). The term-abstraction-level algebraic laws are witness-independent and unaffected.

## Proposed changes

```edit:book/src/L1/weak_form_term.md
<<<SEARCH (Variant axes — differential-operator block)
  **Grounded variant points (pulled by an in-scope
  solver-K witness):**
  - `Gradient` — the **electrostatic** stiffness term `(ε, ∇)`, witnessed
    `palace/models/laplaceoperator.cpp:191-192` (`fe_assemble`'s single-term witness).
  - `Curl` — the **magnetostatic** stiffness term `(μ⁻¹, ∇×)`, witnessed
    `palace/models/curlcurloperator.cpp:179-181` (this cycle's pull).
  **Pending-pull sibling variant points (named axis points, NOT yet authored — await their own pipeline pull):**
  - `Identity` (mass) — `Mass`/`VectorFEMass`-realized `(Q, I)` term. The **most-likely next pull**: mass terms
    appear pervasively across the eigenmode/driven/transient pipelines (`VectorFEMassIntegrator` consumer sites
    at `palace/models/spaceoperator.cpp:278`, `palace/models/modeeigensolver.cpp:62`,
    `palace/models/domainpostoperator.cpp:38`, `palace/models/romoperator.cpp:424`). Awaits a pipeline pull that
    NEEDS a mass-term solver-K/M witness (not speculatively authored here per the redirect's pull-only clean-gate).
  - `Divergence` (div-div) — `DivDivIntegrator`-realized `(Q, ∇·)` term. **No in-scope solver-K witness** in the
=== REPLACE
  **Grounded variant points (pulled by an in-scope
  solver-K/M witness — 3 of 4):**
  - `Gradient` — the **electrostatic** stiffness term `(ε, ∇)`, witnessed
    `palace/models/laplaceoperator.cpp:191-192` (`fe_assemble`'s single-term witness).
  - `Curl` — the **magnetostatic** stiffness term `(μ⁻¹, ∇×)`, witnessed
    `palace/models/curlcurloperator.cpp:179-181` (c061's pull).
  - `Identity` — the **mass** term `(Q, I)` — the identity differential operator (`𝒟u = u`, **no derivative**),
    realizing the L² pairing `a(u, v) = (Q u, v)`. Witnessed by `SpaceOperator::GetMassMatrix`
    (`palace/models/spaceoperator.cpp:438`), whose `AddIntegrators` fold (`palace/models/spaceoperator.cpp:260`)
    appends `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f)` (`palace/models/spaceoperator.cpp:278`) with the
    mass coefficient `*f`. This is the **SAME `BilinearForm`-fold** as the Gradient/Curl witnesses — an
    integrator-slot-only difference (here `VectorFEMassIntegrator` over a vector-FE/Nedelec space; the
    coefficient still rides the variant-invariant base-class slot `palace/fem/integrator.hpp:39-42`). The mass
    term is heavily multi-witness (eigenmode/driven/transient/ROM/postprocess) — additional consumer sites at
    `palace/models/modeeigensolver.cpp:62`, `palace/models/domainpostoperator.cpp:38`,
    `palace/models/romoperator.cpp:424`. (Grounded c062.)
  **Pending-pull sibling variant point (named axis point, NOT yet authored — awaits its own pipeline pull):**
  - `Divergence` (div-div) — `DivDivIntegrator`-realized `(Q, ∇·)` term. **No in-scope solver-K witness** in the
>>> END
```

```edit:book/src/L1/weak_form_term.md
<<<SEARCH (Evidence — Identity-variant lines)
- `palace/fem/integrator.hpp:68-69` — `MassIntegrator`: `a(u, v) = (Q u, v)` for H1 / vector-`(H1)ᵈ` — the
  `Identity` differential-operator variant (pending-pull sibling).
- `palace/fem/integrator.hpp:79-80` — `VectorFEMassIntegrator`: `a(u, v) = (Q u, v)` for vector finite elements
  — the vector-FE realization of the `Identity` variant.
=== REPLACE
- `palace/fem/integrator.hpp:68-69` — `MassIntegrator`: `a(u, v) = (Q u, v)` for H1 / vector-`(H1)ᵈ` — the
  `Identity` differential-operator variant (grounded c062; identity operator, no derivative).
- `palace/fem/integrator.hpp:79-80` — `VectorFEMassIntegrator`: `a(u, v) = (Q u, v)` for vector finite elements
  — the vector-FE realization of the `Identity` variant (the integrator the mass witness instantiates).
- `palace/models/spaceoperator.cpp:434-460` — `SpaceOperator::GetMassMatrix`: the **mass witness** (c062's
  grounding). Builds the mass coefficient `fr` (`AddRealMassCoefficients(1.0, fr)`) then assembles via
  `AssembleOperator(GetNDSpace(), nullptr, &fr, ...)` (`:459`), which routes through `AddIntegrators`
  (`palace/models/spaceoperator.cpp:260`) appending
  `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f)` (`palace/models/spaceoperator.cpp:278`) — the term `(Q, I)`,
  the identity differential operator (`𝒟u = u`). The SAME `BilinearForm`-fold as the electrostatic/magnetostatic
  witnesses, differing ONLY in the integrator slot. Grounds the `Identity` variant point — the differential-operator
  variant axis is now **3 of 4 grounded** (only `Divergence`/div-div remains pending-pull).
>>> END
```

```edit:book/src/L1/weak_form_term.md
<<<SEARCH (Status — witness-count framing)
one witness
could be coincidence; two witnesses differing in EXACTLY the integrator slot establish the variant axis).
=== REPLACE
one witness
could be coincidence; multiple witnesses differing in EXACTLY the integrator slot establish the variant axis).
The differential-operator variant axis is now **3-of-4 grounded** by in-scope solver-K/M witnesses
(`Gradient`/electrostatic, `Curl`/magnetostatic, `Identity`/mass — the last grounded c062 at
`palace/models/spaceoperator.cpp:278`,`:438`); only `Divergence`/div-div remains a named pending-pull sibling
(no in-scope witness). The grounding is an in-place specialization note under the term abstraction
(combinator-primary per the 2026-06-01 redirect §1), not a new mirrored entry; the term-abstraction-level
algebraic laws are witness-independent and unchanged.
>>> END
```

## Operator content (the grounded axis-point note, as written into the file)

**Slug + one-line:** `weak_form_term` — the immutable `(coefficient, differential-operator)` pair naming one
weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)` (entry unchanged; this dispatch grounds one axis point of its
primary variant axis in-place).

**Axis point grounded:** `Identity` (mass) on the **differential-operator** variant axis. The identity
differential operator `𝒟u = u` (no derivative) realizes the L² mass pairing `a(u, v) = (Q u, v)`.

**Signature (unchanged):**

    weak_form_term :: { coefficient: MaterialCoefficient, diff_op: DifferentialOperator } -> WeakFormTerm
    data DifferentialOperator = Gradient | Identity | Curl | Divergence

The `Identity` constructor of the `DifferentialOperator` enum is now grounded by an in-scope witness — its
specialization is `weak_form_term { coefficient = Q (mass coeff), diff_op = Identity }`, realizing `(Q u, v)`.

**Semantics (axis-point-specific):** the `Identity` term carries the identity differential operator — `𝒟u = u`,
applied to both trial and test functions, so the pairing degenerates to the `Q`-weighted `L²(Ω)` mass inner
product `(Q u, v)_Ω`. It is well-formed over any FE space (H1 or vector-FE); the witnessed pull
(`GetMassMatrix`) realizes it over the Nedelec/vector-FE space via `VectorFEMassIntegrator`. All four
term-abstraction algebraic laws (coefficient-linearity, coefficient-additivity, variant-discreteness,
symmetry-for-symmetric-Q) hold for the `Identity` point unchanged — they are witness-independent pair-constructor
laws.

**Algebraic laws:** unchanged (term-abstraction-level, witness-independent). The mass-term grounding does NOT add
or remove any law; it only moves the `Identity` enum constructor from "named pending-pull sibling" to "grounded
specialization with an L0 witness."

**Dependencies:** unchanged — `weak_form_term` remains an L1 leaf (inert pair constructor) consumed by
`fe_assemble`.

**Status:** `firm` (unchanged). Variant axis now **3-grounded-of-4**.

**Evidence (new for this grounding):**
- `palace/models/spaceoperator.cpp:278` — `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f);` — the mass-term
  instantiation; integrator `VectorFEMassIntegrator`, coefficient `*f` (mass coeff). [citecheck ok]
- `palace/models/spaceoperator.cpp:438` — `SpaceOperator::GetMassMatrix` signature — the mass-term fold site.
  [citecheck ok]
- `palace/models/spaceoperator.cpp:260` — `AddIntegrators` — the fold function the mass-term instantiation lives
  in (reached from `GetMassMatrix` via `AssembleOperator`, `:459`). [citecheck ok]
- `palace/fem/integrator.hpp:79-80` — `VectorFEMassIntegrator` wrapper: `a(u, v) = (Q u, v)` for vector FE (the
  realized bilinear form; comment `:78`, class decl `:79` — the cited `:79-80` range encloses the class decl).
- `palace/fem/integrator.hpp:68-69` — `MassIntegrator` wrapper: `a(u, v) = (Q u, v)` for H1 / vector-`(H1)ᵈ`
  (comment `:68`, class decl `:69`).

## Supporting evidence

Verified via `palace-codemap` `read_range` + `tools/citecheck/citecheck.py --anchor` (on-disk source-of-truth):

- `spaceoperator.cpp:278` `--anchor VectorFEMassIntegrator` → `[ok]` (anchor at 278).
- `spaceoperator.cpp:438` `--anchor GetMassMatrix` → `[ok]` (anchor at 438).
- `spaceoperator.cpp:260` `--anchor AddIntegrators` → `[ok]` (anchor at 260).
- `read_range spaceoperator.cpp:270-285` confirms the `AddIntegrators` else-branch:
  `a.AddDomainIntegrator<VectorFEMassIntegrator>(*f);` on `:278`.
- `read_range spaceoperator.cpp:436-470` confirms `GetMassMatrix` builds mass coeff `fr`
  (`AddRealMassCoefficients(1.0, fr)`) and assembles via `AssembleOperator(GetNDSpace(), nullptr, &fr, ...)`
  (`:459`).
- `read_range palace/fem/integrator.hpp:66-82` confirms the `MassIntegrator` (`a(u, v) = (Q u, v)` for H1 / vector-`(H1)ᵈ`,
  comment `:68`) and `VectorFEMassIntegrator` (`a(u, v) = (Q u, v)` for vector FE, comment `:79`) declarations.
  The existing `:68-69` / `:79-80` two-line range citations correctly bracket comment + class decl (`MassIntegrator`
  class at `:69`, `VectorFEMassIntegrator` class at `:79` — both inside the cited ranges; the `VectorFEMass`
  comment is at `:78`).

Note on the `CurlCurlMassIntegrator` combined branch (`spaceoperator.cpp:264`): when BOTH `df` (curl coeff) and
`f` (mass coeff) are present, Palace fuses them into a single `CurlCurlMassIntegrator` term (the curl-curl-PLUS-mass
sum operator). The pure-mass `VectorFEMassIntegrator` branch (`:278`) is taken when only `f` is present — which is
exactly the `GetMassMatrix` case (it passes `nullptr` for the `df` curl slot, `:459`). The fused branch is a
distinct (additive-sum) term not in scope here; the pure-mass branch is the clean `Identity`/`(Q, I)` witness.

## Open questions / caveats

- The mass term has the largest multi-witness footprint of any axis point (eigenmode/driven/transient/ROM/
  postprocess all consume it). This dispatch grounds it from the `GetMassMatrix` pure-mass site; the other
  consumer sites (`modeeigensolver.cpp:62`, `domainpostoperator.cpp:38`, `romoperator.cpp:424`) are named as
  additional witnesses but not individually re-verified line-by-line this dispatch (the `GetMassMatrix` site is
  the canonical pure-`(Q, I)` witness; the others are corroborating, and several route through the same
  `AddIntegrators` fold). A future pipeline pull (e.g. the eigenmode M-matrix) that NEEDS the mass term will
  re-anchor its own site — no gap is created by not exhaustively verifying them here.
- `Divergence`/div-div remains the sole pending-pull sibling — unchanged from c061. Codemap search over
  `palace/models/*.cpp` returns no `DivDivIntegrator` instantiation among the model operator K-builds; its
  absence stays recorded as a possible spine-coverage finding (the wrapper exists at
  `palace/fem/integrator.hpp:122-123` but no in-scope solver needs it), not a gap to fill speculatively.
- No intro refresh needed: this is an in-place axis-point grounding within an existing firm chapter; the L1 Part
  intro / dep-map already lists `weak_form_term` as firm with a differential-operator variant axis.
- No new dep-map row, no SUMMARY line, no new lowering theme — the entry already exists and its downward-lowering
  surface (`fe-operator-assemble-mutation-rotation` + `fe-assemble-libceed-boundary-obstruction`) already covers
  the mass term's realization (the `VectorFEMassIntegrator` `make_unique`/`push_back` build-up and its libCEED
  kernel are the same boundary as the other variants).
