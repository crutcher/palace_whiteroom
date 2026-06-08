---
layer: L1
operator: eigenvalue-untransform
firmness: firm
depends_on: []
variant_axes:
  - evp-degree (linear-EVP `ω = √μ` (μ = -λ² = ω², the squared eigenvalue) | quadratic-EVP `ω = λ/i` (λ = iω)) — THE load-bearing axis; selects which inverse map recovers ω. The L0 selector is the structural predicate `!C && !has_A2` (no damping operator AND no nonlinear A2 ⇒ linear; otherwise quadratic), NOT a literal `ProblemType` read
  - element-type (the eigenvalue and ω are both `std::complex<double>`; the map is complex-valued — the eigenfrequency `f = Re ω` projection is the consumer's, not this primitive's)
---

# eigenvalue-untransform

The L1 **eigenvalue→ω un-transform primitive**: the per-mode scalar map that recovers the
physical angular frequency `ω` from the raw eigenvalue the eigensolver returns, inverting the
problem-specific spectral transformation the eigensolver solved under,

    ω = untransform(degree, eigenvalue)
      = √μ        when degree = linear-EVP     (μ = -λ² = ω², the squared eigenvalue)
      = λ / i     when degree = quadratic-EVP  (λ = iω)

`eigenvalue-untransform` is the **second per-mode scalar building block** that the L4 eigenmode
reduction [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) folds: the
`untransform : EvpDegree -> Complex -> Complex` map the combinator applies to each eigenvalue
before taking `f = Re ω` (`eigenfreq_qfactor_reduce.md:73,80-81`). It is the sibling of the firm
[`participation_ratio`](./participation_ratio.md) (the κ-participation half) — together the
two firm the **structure side** of that combinator: this entry is the eigenvalue
un-transform gate, `participation_ratio` is the `½X|I|²/E` energy-ratio gate.

## Context

L1 re-expresses Palace's source operations as pure functions (`L1/index.md:1-3`). The eigensolver
returns each converged eigenvalue in the coordinates of whatever spectral transformation it solved
under — the **squared** angular frequency `μ = ω²` for the symmetric linear generalized EVP, or the
**imaginary-scaled** `λ = iω` for the quadratic (damped / nonlinear) polynomial EVP. The readout
loop un-transforms each eigenvalue back to the physical `ω` with a two-way branch before any
downstream measurement (`eigensolver.cpp:430-439`). `eigenvalue-untransform` names that branch as
one pure scalar function.

The operator is defined **in L1 vocabulary** (high→low discipline): its semantics, signature, and
laws are stated in terms of the eigenvalue scalar it maps and the EVP-degree it is keyed on — NOT
in terms of the L0 C++ readout loop. The forward narration of how this L1 map rewrites into the
Palace source branch is the §"Downward to L0" section.

This is **not** a BLAS-1 reduction or an `apply_linop` sibling — there is no tensor operand and no
length axis; it is a **scalar→scalar post-solve readout map**, the eigenmode-output-product
counterpart of [`participation_ratio`](./participation_ratio.md) (the other scalar readout map the
same L4 verb folds). It is the elementary algebraic atom that recovers `ω` the way `participation_ratio`
is the elementary atom that forms the κ/EPR ratio — both consume opaque scalars the eigensolver /
energy reductions produced and live above no tensor.

## Record definition

This primitive's signature names one selector type, **`EvpDegree`** — the binary EVP-degree axis
`linear-EVP | quadratic-EVP`. It is **single-consumer at L1** (only this primitive keys on it as a
standalone axis), so it is defined here rather than on a concept page:

| field/value | type | meaning |
|---|---|---|
| `linear-EVP` | `EvpDegree` | the symmetric generalized EVP `K x = μ M x` solving for `μ = ω²` (no damping operator `C`, no nonlinear `A2`); recovered by `ω = √μ` |
| `quadratic-EVP` | `EvpDegree` | the polynomial / damped EVP solving for `λ = iω` (a damping operator `C` is present, or a nonlinear `A2(ω)` term is interpolated); recovered by `ω = λ/i` |

The L0 selector is **not** a stored enum field — it is the structural predicate `!C && !has_A2`
read off the operator family at solve time: `C = space_op.GetDampingMatrix(...)` and
`has_A2 = (A2 != nullptr)` (`eigensolver.cpp:41,52-53`); the branch tests `if (!C && !has_A2)`
(`:430`). `EvpDegree` is the L1 abstraction of that predicate (linear ⟺ both absent). It is
**distinct from `ProblemType`**: the L4 verb's signature names the upstream `ProblemType` selector
(the six-member `enum class ProblemType : char`, defined as a cross-cutting record on
[`config-record`](../concepts/config-record.md):61-77, `palace/utils/labels.hpp:18-26`), but the
eigenvalue un-transform is keyed on the narrower derived EVP-degree, not the full `ProblemType` —
`EIGENMODE` problems can be either linear or quadratic depending on whether damping/nonlinear terms
are configured. `ProblemType` is cross-referenced (not redefined here); `EvpDegree` is the
in-chapter single-consumer selector this primitive actually branches on.

## Signature

    -- the eigenvalue→ω un-transform: recover the physical angular frequency from the raw eigenvalue
    eigenvalue_untransform :: EvpDegree        -- degree     : selects the inverse spectral map (linear | quadratic)
                           -> Complex          -- eigenvalue : the raw eigenvalue the eigensolver returned (μ or λ)
                           -> Complex          -- omega      : the physical angular frequency ω
    eigenvalue_untransform Linear    mu  = sqrt mu       -- μ = -λ² = ω²   (linear EVP)
    eigenvalue_untransform Quadratic lam = lam / i       -- λ = iω         (quadratic EVP)

Shape contract (bunsen-style; named axes):

- `degree : EvpDegree` — the EVP-degree selector (`linear-EVP | quadratic-EVP`). Read-only.
  Selects the inverse map. The L0 realization derives it from the operator family
  (`!C && !has_A2 ⇒ linear`, `eigensolver.cpp:430`).
- `eigenvalue : Complex` — the raw eigenvalue the eigensolver returned (`std::complex<double> omega
  = eigen->GetEigenvalue(i)`, `eigensolver.cpp:427`): the squared frequency `μ` in the linear case,
  the imaginary-scaled `λ` in the quadratic case. Read-only.
- result `omega : Complex` — the physical angular frequency `ω`. The eigenfrequency `f = Re ω` is
  the **consumer's** projection (the L4 verb / the postprocess `freq_re`), not part of this map.

The shape contract makes structural what is conventional in the C++ readout loop: each branch is one
closed-form scalar inverse of the spectral transformation the corresponding EVP class solved under.
There is no tensor operand and no reduction — the un-transform is a pure per-eigenvalue scalar map.

## Semantics

`eigenvalue_untransform degree eigenvalue` returns the physical angular frequency `ω` by applying
the inverse of the spectral transformation under which the eigensolver returned the eigenvalue:

- **Linear EVP** (`degree = linear-EVP`): the symmetric generalized problem `K x = μ M x` solves for
  `μ = -λ² = ω²`, the squared angular frequency; un-transform by the principal square root
  `ω = √μ` (`eigensolver.cpp:431-433`).
- **Quadratic EVP** (`degree = quadratic-EVP`): the damped / polynomial problem solves for the
  eigenvalue `λ = iω`; un-transform by dividing out the imaginary unit `ω = λ/i = -iλ`
  (`eigensolver.cpp:436-438`).

It is a pure scalar function — no state, no effect, no tensor. The map is total over the complex
plane in both branches (`std::sqrt` of a complex is the principal branch; `/ 1i` is exact complex
division), so there is no edge-case guard inside this primitive.

The operator's structural payoff: the eigensolver's per-mode `ω`-recovery — written as an inline
two-way branch in the readout loop, with the selector derived structurally from the presence of the
damping/nonlinear operators — is ONE scalar map keyed on the EVP-degree. The difference between the
two arms (square-root vs imaginary-division) is the **evp-degree** variant axis; the map is uniform
in structure (a per-eigenvalue closed-form inverse). The `f = Re ω` projection, the `B = -1/(iω)∇×E`
field recovery, and the Q-factor are all **downstream consumers** of the un-transformed `ω`, NOT part
of this primitive.

## Algebraic laws

Every law is a **syntactic identity on the per-eigenvalue scalar map**, read off the two positive
branches of the readout loop.

1. **Branch definition.** `eigenvalue_untransform Linear μ = √μ` and
   `eigenvalue_untransform Quadratic λ = λ/i` — the two literal closed forms (`:433`, `:438`).
2. **Inverse-of-the-transform round-trip.** Each branch is the inverse of the spectral map the
   eigensolver solved under: linear `ω = √(ω²)` recovers `ω` (principal branch, for `Re ω ≥ 0`);
   quadratic `ω = (iω)/i` recovers `ω` exactly. The un-transform composed with the forward transform
   is the identity on the principal domain.
3. **Linear-branch square-root homogeneity.** `√(k²·μ) = k·√μ` for `k > 0` — the scale factor pulls
   through the principal square root (the property that makes the `μ = ω²` recovery scale-correct
   under nondimensionalization).
4. **Quadratic-branch C-linearity.** `eigenvalue_untransform Quadratic (a·λ) = a · eigenvalue_untransform
   Quadratic λ` — division by `i` is `ℂ`-linear, so the quadratic arm commutes with complex scaling
   (the property that makes the nondimensional↔dimensional `λ`-rescaling pass through the un-transform).
5. **Element-type purity.** Both arms map `Complex → Complex` with no real/imag coupling beyond the
   closed-form scalar operation; the eigenfrequency `f = Re ω` real projection is applied by the
   consumer AFTER this map, not inside it.

Laws that explicitly **do not** hold:

- **No cross-branch identity.** The linear and quadratic arms are NOT the same function — `√μ ≠ μ/i`
  in general. The evp-degree axis is load-bearing (it selects genuinely different inverse maps), not
  a transparent variant. Picking the wrong arm silently returns a wrong frequency.
- **Not a reduction, not element-wise over a tensor.** The operand is a single already-extracted
  scalar eigenvalue; there is no length axis, no sum, no tensor (contrast [`dot`](./dot.md) /
  [`nrm2`](./nrm2.md), which DO reduce; contrast [`reciprocal`](./reciprocal.md), which maps
  element-wise over a tensor). This is a scalar→scalar map, the per-mode counterpart of
  [`participation_ratio`](./participation_ratio.md).
- **Square-root branch non-totality of the inverse-uniqueness, NOT of the function.** `√μ` is total
  (principal branch always returns), but the round-trip law (2) holds only on the principal domain
  `Re ω ≥ 0`; the eigensolver's target shift makes this the physical domain, so the readout never
  hits the ambiguous case — a precondition on the consumer, not a partiality of this map.

## Downward to L0

`eigenvalue_untransform` lowers by **identity-in-form on the scalar branch** to the eigensolver
readout loop's un-transform — each arm is the literal C++ scalar operation this primitive names
(`omega = std::sqrt(omega)` for the linear arm, `omega /= 1i` for the quadratic arm). There is no
intervening reshape: the L1 scalar map IS the C++ branch. The substantive downward content is the
**EVP-degree selector derivation** — the L0 branch keys on `!C && !has_A2` (the structural predicate
that `C = GetDampingMatrix(...)` is null AND no nonlinear `A2` was interpolated), which the L1
`EvpDegree` axis abstracts; that derivation reads the operator family assembled upstream
(`eigensolver.cpp:41,52-53`), a separate construction step, NOT part of this scalar map. No dedicated
L1>L0 theme file is authored: the rotation is the bare-scalar-branch identity (the
[`participation_ratio`](./participation_ratio.md) / [`reciprocal`](./reciprocal.md) in-line-marker
route); this entry records the rotation direction in-line per high→low discipline.

The un-transformed `ω` feeds three downstream consumers, all separate steps NOT part of this map: the
eigenfrequency projection `f = Re ω` (the L4 verb / postprocess `freq_re`), the magnetic-field
recovery `B = -1/(iω)∇×E` (`eigensolver.cpp:449`), and the Floquet B-correction scale `1/ω`
(`:454`). Those are named here as the consumers, not authored.

## No L2 entry (by warrant)

`eigenvalue-untransform` is a bare per-mode scalar branch (two closed-form
inverses keyed on a binary axis). An L2 mirror would be an identity-in-named-terms re-statement — the
degenerate-mirror smell the vocabulary-shift redirect names; there is no fusion content,
no iteration, no base-primitive composition to unfold at L2. It stops at L1 as a leaf (the
[`participation_ratio`](./participation_ratio.md) / [`reciprocal`](./reciprocal.md) NO-L2 precedent).
The downstream `f = Re ω` / `B = -1/(iω)∇×E` consumers are separate readout steps with their own homes,
not L2 reshapes of this map.

## Relationship to `eigenfreq_qfactor_reduce`

This entry is **gate-(a)** of the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)
combinator — the eigenvalue un-transform's firm L1 home, completing the κ-participation +
un-transform pair ([`participation_ratio`](./participation_ratio.md) is the κ half). That combinator's
promotion is **double-gated** and remains `rough-in (test-coverage-bounded)` until gate-(b) (a
dedicated eigenpair→`(f,Q)` assembly test, or a lowering-verifier law-confidence pass) is addressed.

## Evidence

- **Eigenvalue un-transform (the positive site):** `palace/drivers/eigensolver.cpp:424` (the
  `for (int i = 0; i < num_conv; i++)` readout loop start), `:427`
  (`std::complex<double> omega = eigen->GetEigenvalue(i)` — the raw eigenvalue extraction),
  `:430` (`if (!C && !has_A2)` — the EVP-degree selector predicate), `:431-433`
  (`// Linear EVP has eigenvalue μ = -λ² = ω².` + `omega = std::sqrt(omega)` — the linear arm),
  `:435-438` (`// Quadratic EVP solves for eigenvalue λ = iω.` + `omega /= 1i` — the quadratic arm).
- **EVP-degree selector operators (the construction the predicate reads):**
  `palace/drivers/eigensolver.cpp:41` (`auto C = space_op.GetDampingMatrix<ComplexOperator>(...)`),
  `:52-53` (`auto A2 = funcA2(target); bool has_A2 = (A2 != nullptr);`).
- **Downstream consumers of the un-transformed ω (separate steps, NOT this map):**
  `palace/drivers/eigensolver.cpp:449` (`B *= -1.0 / (1i * omega)` — the `B = -1/(iω)∇×E` field
  recovery), `:454` (`floquet_corr->AddMult(E, B, 1.0 / omega)` — the Floquet B-correction scale),
  `:457-458` (`post_op.MeasureAndPrintAll(i, E, B, omega, ...)` — the per-mode measure that takes
  `f = Re ω`).
- **L4 fold consumer:** `book/src/L4/eigenfreq_qfactor_reduce.md:51-53` (the
  `ω = √μ` / `ω = λ/i` per-mode un-transform the combinator folds), `:68,73,80-81` (the
  `ProblemType -> ... untransform ptype lambda` signature + the `untransform Linear/Quadratic`
  branch), `:195-198` (the §Status naming the eigenvalue-un-transform L1 entry as gate-(a)). This
  entry IS that un-transform L1 home.
- **Sibling (the κ-participation half):** `book/src/L1/participation_ratio.md` (the `½X|I|²/E`
  energy-ratio half of the same L4 verb; this entry is its eigenvalue-un-transform sibling, the two
  together firming the structure side of `eigenfreq_qfactor_reduce`).
- **`ProblemType` record home (cross-cutting, cross-referenced not redefined):**
  `book/src/concepts/config-record.md:61-77` (the `enum class ProblemType : char` six-member
  definition, `palace/utils/labels.hpp:18-26`). The L1 selector `EvpDegree` is the narrower
  derived axis (the in-chapter single-consumer §Record definition), distinct from `ProblemType`.
- **Sibling-primitive grounding:** `book/src/L1/reciprocal.md` (the bare-scalar-map NO-L2 precedent
  for a non-reducing scalar primitive), `book/src/L1/nrm2.md` (the elementary `√·` analog).
- **No dedicated test** exercises the eigenmode readout un-transform (the `eigensolver.cpp` readout
  loop is integration-level under the eigenmode `Solve(mesh)` driver; no `reference/palace/test/unit/`
  coverage) — non-gating for the syntactic-identity scalar laws (firm-on-positive-structure).
