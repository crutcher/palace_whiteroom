---
agent: harvester
invoked_at: 2026-06-03T15:09:23Z
scope: L1 operator: port_projection
status: pending
integrated_at: 2026-06-03T154500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean from the report's `new:` block (staging row 5/5, LAST). Firm L1 port_projection (per-port linear functional <s,E>; OWN-verb verdict — NOT a bilinear-form specialization (s is a covector) and NOT a dot (unconjugated dual contraction); port-kind THE load-bearing variant axis; firm-on-positive-structure on 2 positive sites + unit-tested kernel; in-chapter ## Record definition for single-consumer Covector[N]). Firms sparameter_reduce gate-b (reduce verb STAYS rough-in, 2nd gate = dedicated reduction test). CLOSED the count-coordination 28->29 main / 35->36 grand (cycle-final L1 tally; .cpp->.hpp citation-extension fix + nested-fence->indented-code + SUMMARY 8->2-space repairs all held). Build clean."
inputs:
  - dispatch D5 cycle-077 (this dispatch)
  - OQ sparameter-reduce-l1-port-projection-home (c075 D1)
  - book/src/L4/sparameter_reduce.md (the L4 reduction folding this projection; gate-b)
  - witness 1 (lumped): palace/models/lumpedportoperator.cpp:283-294 (LumpedPortData::GetSParameter)
  - witness 2 (wave): palace/models/waveportoperator.cpp:780-793 (WavePortData::GetSParameter)
  - book/src/L1/bilinear-form.md (the candidate-subsume verb — the load-bearing question)
  - book/src/L1/dot.md (the co-spatial reduction sibling; tdot unconjugated-bilinear variant)
---

# CYCLE: Formalize port_projection at L1

## Summary

The per-port field-onto-port-mode projection `sᵢ·E` that `book/src/L4/sparameter_reduce.md`
folds (its gate-b) has no firm L1 home (OQ `sparameter-reduce-l1-port-projection-home`,
c075 D1). I investigated the **load-bearing question** — is this a specialization of the
existing `bilinear-form` (a left-fixed partial-application at the port covector `sᵢ`), or its
own verb? — and resolved it to **its OWN verb**. Both witnesses build the projection from an
**assembled `mfem::LinearForm`** (a covector / linear functional in the FE dual space, not an
`Operator`/matrix-weight) applied to the field by the MFEM dual pairing
`LinearForm::operator*(Vector) = Σᵢ sᵢ Eᵢ` (an **unconjugated real** contraction). This is
neither the two-vector matrix-weighted `xᴴ M y` of `bilinear-form` nor the co-spatial
Hermitian reduction `dot`: it is a *fixed-covector linear functional* applied to one field
argument. I author the standalone firm `book/src/L1/port_projection.md` and add its dep-map
row to `book/src/L1/index.md` (Operator-application-&-assembly grouping). **VERDICT (for the
later coupled re-check): `port_projection` IS a live slug.** The `sparameter_reduce` gate-b
is now satisfiable by this firm chapter + the `project` down-link; I do **not** re-anchor
`sparameter_reduce` or the sparameters column here (the double-gated coupled-column pass is a
later cycle — NOTED). Resolves OQ `sparameter-reduce-l1-port-projection-home`.

## The load-bearing question — verdict and warrant

**Verdict: `port_projection` is its OWN verb, NOT a `bilinear-form` specialization and NOT a
`dot` specialization.** Therefore `sparameter_reduce`'s gate-b is satisfied by a NEW firm
chapter (this one) + a `project` down-link, NOT by a note under `bilinear-form`.

Warrant (structural, read off the two witnesses + the assembly site):

1. **The port mode `s` is an assembled covector, not an operator.** `s` is
   `mutable std::unique_ptr<mfem::LinearForm>` (`palace/models/lumpedportoperator.hpp:51`),
   assembled by `InitializeLinearForms` from a `VectorFEBoundaryLFIntegrator` over the port
   boundary attributes (`:162-196`). A `LinearForm` is an element of the **FE dual space**
   (a covector), not an `Operator`/`ComplexOperator` matrix-weight. `bilinear-form`'s
   signature is `(x, M: LinearOperator[M,N], y) -> Scalar = xᴴ M y` — a **two-vector**
   reduction through a runtime linear-operator weight (`bilinear-form.md:62-94`). Modelling
   `s·E` as `bilinear_form(s, I, E)` would mint a fake identity weight AND a fake second
   vector and would attach the wrong (conjugate-linear, Hermitian-symmetric) algebra; it
   does not represent the assembled-covector + dual-pairing structure. So it does NOT cleanly
   factor through `bilinear-form`.

2. **The pairing is the unconjugated real dual contraction, not the Hermitian `dot`.**
   `(*s) * E.Real()` is MFEM's `LinearForm::operator*(const Vector&) = Σᵢ sᵢ Eᵢ` — a real
   sum-of-products, **no conjugation**, between a fixed covector `s` and the real components
   of `E`. `dot` (complex) is conjugate-linear/Hermitian in its first argument
   (`conj(x)·y`, `book/src/L1/dot.md` lines 34, 63-68); the closer co-spatial kin `tdot` is
   the unconjugated *bilinear* form on **two vectors in the same space**
   (`book/src/L1/dot.md` lines 71-75). `port_projection`
   is neither a Hermitian nor a co-spatial-two-vector reduction: it is a **single fixed
   functional applied to one field**, where the functional is pre-assembled at port-setup
   time and the field is the runtime argument. The wave case makes the non-`dot` shape
   unmistakable (point 3).

3. **The wave case is a 2×2 real recombination of TWO distinct functionals — not any single
   inner product.** `WavePortData::GetSParameter` (`waveportoperator.cpp:780-793`) computes
   the complex result from two distinct assembled functionals `port_sr`, `port_si`
   (`waveportoperator.hpp:101`) applied to the real and imag parts of (the transferred)
   field: `Re = −(port_sr·Eᵣ) − (port_si·Eᵢ)`, `Im = −(port_sr·Eᵢ) + (port_si·Eᵣ)`
   (`:789-790`). This is `(port_sr + i·port_si)·(Eᵣ + i·Eᵢ)` — a complex linear functional
   `s = sr + i·si` applied to a complex field — realized as four real pairings. It is NOT
   `xᴴ M y` for any `M`, and NOT a Hermitian/bilinear `dot` of two co-spatial vectors. It is
   exactly a complex-covector dual pairing. This forces the OWN-verb verdict.

Conclusion: `port_projection` is the L1 home of the **assembled-linear-form dual pairing**
(covector applied to field) — a genuinely distinct primitive from both the matrix-weighted
two-vector `bilinear-form` and the co-spatial-vector `dot`/`tdot`. Authored standalone, firm.

## Proposed changes

```new:book/src/L1/port_projection.md
---
layer: L1
operator: port_projection
firmness: firm
lowers_to: []
lifts_from: []
depends_on: []
variant_axes:
  - port-kind
  - precision-mode
  - parallel-wrapper
---

# port_projection

Mutation-free **linear-functional projection of a field onto a port mode**:
`α = ⟨s, E⟩`, the dual pairing of a fixed pre-assembled port-mode covector `s`
(an element of the finite-element dual space) with a field `E`. The
field-onto-port-mode projection that the S-parameter reduction folds — the
**covector / linear-functional** primitive at L1, distinct from the
matrix-weighted two-vector [`bilinear-form`](./bilinear-form.md) (`xᴴ M y`) and
the co-spatial-vector Hermitian reduction [`dot`](./dot.md) (`⟨x, y⟩`).

## Context

`port_projection` lifts Palace's two port-S-parameter projection kernels —
`LumpedPortData::GetSParameter` (`palace/models/lumpedportoperator.cpp:283-294`)
and `WavePortData::GetSParameter` (`palace/models/waveportoperator.cpp:780-793`)
— to a single pure-functional dual-pairing operator. Both kernels apply a fixed
**assembled `mfem::LinearForm`** (a covector in the FE dual space) to the field
via MFEM's `LinearForm::operator*(const Vector&)`, the dual contraction
`⟨s, x⟩ = Σᵢ sᵢ xᵢ` (an **unconjugated real** sum-of-products). The covector is
built once at port setup (`LumpedPortData::InitializeLinearForms`,
`palace/models/lumpedportoperator.cpp:162-196`, from a
`VectorFEBoundaryLFIntegrator` over the port boundary attributes) and held fixed;
`E` is the runtime field argument. This is the structural reason `port_projection`
is **its own verb** and not a specialization of a co-spatial inner product:

- It is **not** [`bilinear-form`](./bilinear-form.md): that operator is the
  two-vector matrix-weighted reduction `xᴴ M y` with `M` a runtime
  `LinearOperator[M, N]`. A port mode `s` is a covector, not an operator;
  re-expressing `⟨s, E⟩` as `bilinear_form(s, I, E)` would invent both a fake
  identity weight and a fake second vector, and would attach the wrong
  (conjugate-linear, Hermitian-symmetric) algebra. The covector is **fixed at
  assembly time**, which `bilinear-form`'s two-runtime-vector signature does not
  model.
- It is **not** [`dot`](./dot.md): `dot` is the Hermitian (conjugate-linear in
  the first argument) reduction of two co-spatial vectors; `tdot` is its
  unconjugated *bilinear* sibling, still on two co-spatial vectors.
  `port_projection` is a single fixed functional applied to one field. The wave
  case (a complex covector `port_sr + i·port_si` realized as four real pairings,
  see *Semantics*) is unmistakably a covector dual pairing, not any co-spatial
  inner product.

The mathematical primitive is the **dual pairing** `V* × V → 𝕜` (covector applied
to vector). At L0 the covector is a concrete assembled `mfem::LinearForm` and the
pairing is `LinearForm::operator*`; the assembled-covector construction itself is
an FE-assembly concern (the boundary linear form), upstream of this operator's
runtime application.

`port_projection` is the per-port projection kernel that the L4 driven
output-product reduction [`sparameter_reduce`](../L4/sparameter_reduce.md) folds
(its `project sᵢ E = sᵢ·E` step). That reduction's gate-b — "the per-port
projection has no firm L1 home" — is satisfied by this entry.

## Signature

    port_projection :: (s: Covector[N], E: Tensor[N]) -> Scalar
    port_projection(s, E) = ⟨s, E⟩ = Σ_{i ∈ [0, N)} s[i] · E[i]

Shape contract (bunsen-style, named axes):

- `s` — `Covector[N]` — read-only. A fixed element of the FE **dual** space over
  the length axis `N` (concretely an assembled `mfem::LinearForm` on the port
  Nédélec space). Pre-assembled at port setup; not a runtime-varying argument in
  the way `E` is. Element type is `real` (lumped `s`; wave `port_sr`, `port_si`
  each separately real — the complex port mode is `port_sr + i·port_si`).
- `E` — `Tensor[N]` — read-only. The field being projected; axis `N` matches the
  covector's domain (the port FE space). Element type `real` or `complex`.
- result — `Scalar` — element type follows the rule below.

Element-type rule:

| `s` element type | `E` element type | result | realization |
|---|---|---|---|
| `real` | `real` | `real` | `⟨s, E⟩` (one real pairing) |
| `real` | `complex` | `complex` | `⟨s, Eᵣ⟩ + i·⟨s, Eᵢ⟩` (lumped) |
| `complex` (`= sr + i·si`) | `complex` | `complex` | the 2×2 real recombination (wave) |

The covector pairing is **unconjugated** (a real dual contraction `Σᵢ sᵢ Eᵢ`); the
complex result is assembled from real pairings on the real/imaginary field
components, NOT by a Hermitian per-element kernel (the distinction from `dot`).

`Covector[N]` is the FE dual-space element type — the type of an assembled linear
functional. It is collapsed at L1 to "a fixed linear functional over the space of
axis `N`"; its assembly (boundary integrator, attribute marker, mode coefficient)
is an FE-assembly concern, not part of this operator's runtime signature.

## Record definition

`Covector[N]` is the only record this signature names. It is used by **only this
operator** at present (single consumer) → defined here, in-chapter:

| field (conceptual) | type | meaning | stratum |
|---|---|---|---|
| coefficients | `Tensor[N]` (real) | the assembled per-DOF functional weights `s[i]` | **construction-time** (assembled once at port setup) |
| domain axis | axis `N` | the FE space the functional acts on (the port Nédélec space) | construction-time |

At L1 `Covector[N]` is a fixed linear functional: a read-only vector of dual-space
coefficients paired with a domain axis. The backing C++ object is an assembled
`mfem::LinearForm` (`palace/models/lumpedportoperator.hpp:51` `s`;
`palace/models/waveportoperator.hpp:101` `port_sr`, `port_si`), built by the port
operator's `InitializeLinearForms` from a boundary LF integrator
(`palace/models/lumpedportoperator.cpp:162-196`). The **construction** of the
covector (which integrator, which boundary attributes, which mode coefficient) is
an FE-assembly concern upstream of `port_projection`; this operator consumes the
covector as an already-assembled construction-time constant and only applies it to
the run-time field `E`. (If a second consumer of an assembled FE covector surfaces,
this should be promoted to a `concepts/covector.md` record-definition page; flagged
in Open questions as a watch, not yet owed.)

## Semantics

`port_projection(s, E)` returns the dual pairing `⟨s, E⟩ = Σᵢ sᵢ Eᵢ` — the value
of the fixed linear functional `s` at the field `E`. It is **linear in `E`** and
**linear in `s`** (a bilinear pairing between the dual space and the primal space),
with **no conjugation** of either argument. The L1 form is pure functional: same
`s`, same `E`, same return value.

**Lumped realization** (`palace/models/lumpedportoperator.cpp:285-293`): a single
real covector `s` is paired with the real and imaginary parts of `E` separately to
form the complex result `⟨s, Eᵣ⟩ + i·⟨s, Eᵢ⟩` (the imaginary part is taken only
when `E.HasImag()`; otherwise the result is the pure-real `⟨s, Eᵣ⟩`).

**Wave realization** (`palace/models/waveportoperator.cpp:782-792`): the port mode
is a **complex** covector `s = port_sr + i·port_si` (two assembled real
functionals), and the result is the complex dual pairing `⟨s, E⟩` of the complex
covector with the complex field, written out as the 2×2 real recombination
`Re = −(port_sr·Eᵣ) − (port_si·Eᵢ)`, `Im = −(port_sr·Eᵢ) + (port_si·Eᵣ)`
(`:789-790`). The leading sign realizes `(E × H_inc⋆)·n = E·(−n × H_inc⋆)`
(`:782-783`): the port-mode covector absorbs the `−n × H_inc⋆` so the body is a
plain projection of `E`. This is unconjugated complex-bilinear (`(sr+i·si)(Eᵣ+i·Eᵢ)`),
NOT the Hermitian `conj(s)·E`, which is the structural reason this is not `dot`.

**The complex result is assembled from real pairings**, not from a complex
per-element kernel: the underlying contraction `LinearForm::operator*` is always
real; complexity enters by combining real pairings on the real/imag components.
This is the load-bearing distinction from [`dot`](./dot.md) (whose complex form is
a Hermitian per-element kernel `conj(x[i])·y[i]`) and from
[`bilinear-form`](./bilinear-form.md) (a two-vector matrix-weighted form).

**Reduction-tree non-associativity is load-bearing** in the same CLAUDE.md sense
as [`dot`](./dot.md): the underlying scalar contraction `Σᵢ sᵢ Eᵢ` is the same
non-associative IEEE-754 floating-point summation. Mathematical laws hold exactly;
floating-point realisations are approximate under reduction-order changes.

**The MPI collective is not in the L1 signature** (single-rank scope per CLAUDE.md).
Both L0 kernels close with `Mpi::GlobalSum(1, &dot, ...)`
(`lumpedportoperator.cpp:292`, `waveportoperator.cpp:791`); at L1 the collective is
folded into the L1>L0 lowering (see *L1 vs L0 distinction*).

## Algebraic laws

The laws below hold; absences are deliberate. Every law is a syntactic identity on
the dual-pairing fold, read off the two `GetSParameter` bodies.

**Bilinear-pairing laws (general `s`, general `E`):**

1. **Linearity in `E`**: `port_projection(s, α·E₁ + E₂) =
   α·port_projection(s, E₁) + port_projection(s, E₂)`. The pairing is linear in
   the field — directly from `Σᵢ sᵢ (α·E₁ᵢ + E₂ᵢ)`. **No conjugation of `α`**
   (contrast `dot`'s conjugate-linearity in its first argument). This is the
   load-bearing law: `port_projection` is **linear** in `E`, which is why
   [`sparameter_reduce`](../L4/sparameter_reduce.md) is a per-column *linear
   projection* and not a bilinear Gram.
2. **Linearity in `s`**: `port_projection(α·s₁ + s₂, E) =
   α·port_projection(s₁, E) + port_projection(s₂, E)`. The pairing is linear in
   the covector (also unconjugated). Witnessed concretely by the wave covector
   composition `s = port_sr + i·port_si`
   (`palace/models/waveportoperator.cpp:789-790`): the complex covector's pairing
   is the `i`-linear combination of its two real-covector pairings.
3. **Zero in either argument**: `port_projection(0, E) = port_projection(s, 0) =
   0`. Follows from laws 1 and 2 with zero coefficients.

**Component-decomposition law (complex field, real covector — the lumped case):**

4. **Real/imag splitting**: for a real covector `s` and complex field
   `E = Eᵣ + i·Eᵢ`, `port_projection(s, E) = port_projection(s, Eᵣ) +
   i·port_projection(s, Eᵢ)`. The complex result is assembled from two real
   pairings (`palace/models/lumpedportoperator.cpp:287-290`), not a Hermitian
   kernel. This is the explicit "complex from real pairings" statement.

**Laws that explicitly do not hold:**

- **Conjugate-linearity (Hermitian symmetry)**: `port_projection` is **not**
  conjugate-linear in either argument and has no Hermitian symmetry. There is no
  conjugation in the dual contraction `Σᵢ sᵢ Eᵢ` (the wave realization is
  `(sr+i·si)(Eᵣ+i·Eᵢ)`, not `conj(sr+i·si)(Eᵣ+i·Eᵢ)`). This is the explicit
  absence distinguishing `port_projection` from [`dot`](./dot.md).
- **Positive semi-definiteness at `E = s`**: not meaningful — `s` (a covector) and
  `E` (a vector) live in dual spaces; there is no `port_projection(s, s)` self-form
  in the same sense as `dot(x, x)` or `bilinear_form(x, M, x)`. No PSD/Cauchy–Schwarz
  structure is claimed.
- **Symmetry under argument swap**: not applicable — the two arguments inhabit dual
  spaces (`Covector[N]` vs `Tensor[N]`); they are not interchangeable.
- **Associativity of the underlying reduction in floating point**: inherited from
  the scalar contraction; different summation orders give different bit-level
  results (load-bearing, see *Semantics*).

## Dependencies

None at L1. `port_projection` is a **leaf primitive** — the dual-pairing kernel.
Its sub-operations are scalar multiplication and scalar addition (the real
contraction `Σᵢ sᵢ Eᵢ`), all at or below the L1 layer's resolution. The covector
`s` is supplied as an already-assembled construction-time constant; the assembly
itself (boundary linear form) is an FE-assembly concern upstream of this operator,
not an L1 dependency of the runtime application.

It is the per-port projection kernel folded by the L4 reduction
[`sparameter_reduce`](../L4/sparameter_reduce.md) (`project sᵢ E = sᵢ·E`); that is
an upward consumer, not a dependency.

## Variant axes

`port_projection` has three orthogonal variant axes at L1:

- **port-kind**: `lumped` | `wave`. THE load-bearing axis. The two kinds differ in
  the covector's assembly and element-type: lumped uses a single real covector `s`
  paired with the real/imag field parts (`lumpedportoperator.cpp:285-290`); wave
  uses a **complex** covector `port_sr + i·port_si` realized as a 2×2 real
  recombination (`waveportoperator.cpp:789-790`). At L1 both collapse to the one
  dual-pairing operator `⟨s, E⟩` parameterised by the covector's element type; the
  port-kind distinction is in *which covector is assembled*, an FE-assembly concern.
  This is the same axis [`sparameter_reduce`](../L4/sparameter_reduce.md) carries at
  L4 (absorbed into its `PortMode` closure).
- **precision-mode**: the working precision of the underlying contraction. Palace
  exposes one precision (`double`); the axis is recorded for parallel structure with
  the BLAS-1 cohort.
- **parallel-wrapper**: at L0 the field's FE space may be MPI-distributed and the
  kernel closes with `Mpi::GlobalSum`; per CLAUDE.md single-rank scope, distributed
  forms are read as their single-rank equivalents at L1. The axis is recorded so the
  L1>L0 lowering correctly reintroduces the collective.

Collapsed (absorbed) axes:

- **covector element-type**: `real` (lumped `s`) | `complex` (wave
  `port_sr + i·port_si`). At L0 these are different field members assembled
  separately; at L1 they collapse to one operator parameterised by the covector
  element type (folded into the *port-kind* axis above and the element-type rule in
  *Signature*).

## Applicability conditions

- `s` must be a linear functional (a covector) over the same FE space as `E`'s
  length axis `N`. Nonlinear functionals are not meaningful for the dual pairing.
- The covector `s` is assembled once (construction-time) over the port boundary;
  `port_projection` applies it to the run-time field `E`. The operator does not
  perform the assembly.
- The element types of `s` and `E` must be compatible per the table in *Signature*
  (a real covector pairs with real or complex fields; a complex covector requires a
  complex field — the wave case `MFEM_VERIFY(E.HasImag())`,
  `palace/models/waveportoperator.cpp:784-786`).
- No SPD / symmetry / positive-definiteness requirement — the pairing is a plain
  bilinear dual contraction with no self-form.

## Status

`firm` — **firm-on-positive-structure**. The signature is read directly off two
positive Palace source sites (`palace/models/lumpedportoperator.cpp:283-294` and
`palace/models/waveportoperator.cpp:780-793`), and every algebraic law is a
syntactic identity on the dual-pairing fold (linearity in each argument,
real/imag splitting, the explicit non-Hermitian / non-symmetric absences). The
covector's assembled-`mfem::LinearForm` realization is positively witnessed
(`palace/models/lumpedportoperator.cpp:162-196`, `:51`;
`palace/models/waveportoperator.hpp:101`).

The **no-dedicated-test caveat is non-gating** here, following the
`apply_linop` / `jacobi-smoother` / `elementwise_product` precedent (firm-on-
positive-structure laws are syntactic identities that a missing unit test does not
gate). The projection *kernel* `GetSParameter` is in fact unit-tested
(`test/unit/test-lumpedportintegration.cpp:367,720`,
`test/unit/test-romoperator.cpp:603`) — these exercise `port_projection`'s
realization directly at the call boundary, raising confidence on the contraction
itself; the laws here are syntactic and need no further test. (The *reduction-level*
assembly that consumes this projection — `MeasureSParameter` — is integration-tested
only; that test-gating lands on [`sparameter_reduce`](../L4/sparameter_reduce.md),
not on this leaf kernel.)

## L1 vs L0 distinction

- **L0**: two model-method kernels. `LumpedPortData::GetSParameter`
  (`palace/models/lumpedportoperator.cpp:283-294`) re-assembles the covector lazily
  (`InitializeLinearForms`), forms `std::complex<double> dot((*s)·E.Real(), 0.0)`,
  conditionally sets the imaginary part `(*s)·E.Imag()` when `E.HasImag()`, then
  `Mpi::GlobalSum`. `WavePortData::GetSParameter`
  (`palace/models/waveportoperator.cpp:780-793`) transfers `E` onto the port space,
  forms the complex result from the two real covectors `port_sr`, `port_si` via the
  2×2 recombination, then `Mpi::GlobalSum`. The pairing operator is MFEM's
  `LinearForm::operator*(const Vector&)`. The covector is a mutable lazily-assembled
  `unique_ptr<mfem::LinearForm>`; the MPI collective is baked in.
- **L1**: pure functional dual pairing `α = port_projection(s, E) = ⟨s, E⟩`. No MPI
  collective in the signature (folded into the L1>L0 lowering). No lazy-assembly
  side effect — the covector is a value supplied to the operator. Covector
  element-type (real lumped / complex wave) is variant-absorbed (one operator
  parameterised by element type). The port-kind distinction (which covector is
  assembled, the leading-sign / transfer details) is an FE-assembly + L1>L0 lowering
  concern, not an L1 branch.

The L1>L0 lowering (narrated forward L1→L0, a future theme or in-line note on the
S-parameter rotation) reintroduces: the lazy covector assembly, the complex-from-
real-pairings expansion (lumped two-pairing / wave four-pairing 2×2), the wave
field transfer onto the port space, and the `Mpi::GlobalSum` collective. This entry
does not author that lowering theme (out of harvester scope; noted in Open
questions / the coupled-column re-check).

## Evidence

- `palace/models/lumpedportoperator.cpp:283-294` — `LumpedPortData::GetSParameter`
  (def `:283`, body `:285-293`, closes `:294`): the lumped projection
  `dot = (*s)·E.Real() [+ i·(*s)·E.Imag()]` — the single-real-covector dual pairing.
  Verified on-disk: `:294` is the closing `}`.
- `palace/models/lumpedportoperator.hpp:51` — `mutable std::unique_ptr<mfem::LinearForm> s, v;`
  — the covector `s` is an assembled `LinearForm` (FE dual-space element), not an
  `Operator`. The structural basis for the OWN-verb verdict.
- `palace/models/lumpedportoperator.cpp:162-196` — `LumpedPortData::InitializeLinearForms`:
  `s` is assembled from a `VectorFEBoundaryLFIntegrator(fb)` over the port boundary
  attribute marker (`:191-195`), confirming `s` is a boundary linear functional
  built at port setup.
- `palace/models/waveportoperator.cpp:780-793` — `WavePortData::GetSParameter`
  (def `:780`, body `:782-792`, closes `:793`): the wave projection
  `(E × H_inc⋆)·n = E·(−n × H_inc⋆)` (comment `:782-783`), realized as the 2×2 real
  recombination of `port_sr`, `port_si` against `port_E->Real()`/`Imag()`
  (`:789-790`); `MFEM_VERIFY(E.HasImag())` guard `:784-786`. Verified on-disk: `:793`
  is the closing `}`.
- `palace/models/waveportoperator.hpp:101` — `std::unique_ptr<mfem::LinearForm> port_sr, port_si;`
  — the wave port mode is a **complex** covector `port_sr + i·port_si` (two assembled
  real `LinearForm`s). Confirms the complex-covector / non-Hermitian shape.
- `test/unit/test-lumpedportintegration.cpp:367` + `:720` —
  `std::complex<double> s_param = port_1.GetSParameter(...)`: dedicated unit tests
  exercising the lumped projection kernel directly (L0-equivalent semantic evidence).
- `test/unit/test-romoperator.cpp:603` — `auto S = port_data.GetSParameter(E)`:
  the projection kernel exercised in the ROM-operator test.
- `book/src/L4/sparameter_reduce.md:86,197-202,255-259` — the L4 driven reduction
  that folds this projection (`project sᵢ E = sᵢ·E`) and whose gate-b
  (`sparameter-reduce-l1-port-projection-home`) this entry satisfies.
- `book/src/L1/bilinear-form.md:62-94` — the candidate-subsume verb (`xᴴ M y`,
  matrix-weighted two-vector); the load-bearing question resolved NON-MATCH (a
  covector is not an `Operator`).
- `book/src/L1/dot.md` lines 34, 63-75 — the co-spatial Hermitian reduction sibling
  (`conj(x)·y`) and its unconjugated bilinear variant `tdot`; resolved NON-MATCH
  (a covector dual pairing is not a co-spatial inner product).
- `book/src/L1/index.md` — dep-map this entry adds a row to.
- `scaffolding/open-questions.md` §`sparameter-reduce-l1-port-projection-home`
  (c075 D1) — the OQ this harvest resolves.
```

```edit:book/src/L1/index.md
| [`assemble_frequency_operator`](./assemble_frequency_operator.md) | `(fam: FrequencyOperatorFamily[N], ω: Scalar) → LinearOperator[N, N]` (i.e. `A(ω) = K + iω·C − ω²·M + A2(ω)`) | [`linear_combination`](../L2/linear_combination.md) (the fold this specializes — operator-operand corner of the operand-category axis, NOT a new fold); `apply_linop` (operands + result are opaque square operators) | `firm` (driven per-ω system-operator assembly; **operator-operand specialization of `linear_combination`** — replace-and-propagate, 2026-06-01 anti-mirror; L0: `palace/drivers/drivensolver.cpp:91-93,175,176-177,180` + `palace/models/spaceoperator.cpp:521-528` + `palace/linalg/rap.cpp:764-787`; L1>L0: [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md); harvested cycle-062; firm-on-positive-structure, no-dedicated-test caveat non-gating; **affine modulo A2** (A2 is an ω-dependent operand carrying coeff 1, not an ω-dependent coefficient); **single-pipeline-by-design** (driven only — transient bakes excitation into the captured op, electro/magnetostatic capture a single fixed K, eigenmode opaque — no 2nd-pipeline discharge owed); sharpens the `map_solve` scope boundary (`book/src/L4/solve_family.md`)) |
| [`port_projection`](./port_projection.md) | `(s: Covector[N], E: Tensor[N]) → Scalar` (i.e. `⟨s, E⟩ = Σᵢ sᵢ Eᵢ`, the field-onto-port-mode linear functional) | (leaf; dual pairing of an assembled FE covector `s` with a field `E`; NOT a `bilinear-form` specialization — `s` is a covector, not an `Operator` — and NOT a `dot` — unconjugated dual contraction, not a co-spatial Hermitian inner product) | `firm` (port-mode linear-functional projection; the `sparameter_reduce` gate-b L1 home; L0: lumped `palace/models/lumpedportoperator.cpp:283-294` + wave `palace/models/waveportoperator.cpp:780-793`; covector assembled `palace/models/lumpedportoperator.cpp:162-196` + decl `palace/models/lumpedportoperator.hpp:51` / `palace/models/waveportoperator.hpp:101`; harvested cycle-077; firm-on-positive-structure, kernel unit-tested `test/unit/test-lumpedportintegration.cpp:367,720` + `test/unit/test-romoperator.cpp:603`; port-kind THE load-bearing variant axis (lumped real covector / wave complex `port_sr+i·port_si`); resolves OQ `sparameter-reduce-l1-port-projection-home`) |
| **Constructed-operator gates** | | | |
```

```edit:book/src/L1/index.md
- **`port_projection`** (firm; cycle-077) — the port-mode linear-functional projection `⟨s, E⟩`, the field-onto-port-mode dual pairing of an assembled FE covector with a field. The L1 home of the per-port projection folded by L4 [`sparameter_reduce`](../L4/sparameter_reduce.md) (its gate-b). Author-verdict: its OWN verb (NOT a `bilinear-form` specialization — `s` is a covector, not an operator; NOT a `dot` — unconjugated dual contraction). Resolves OQ `sparameter-reduce-l1-port-projection-home`.
```

```edit:book/src/SUMMARY.md
  - [port_projection](./L1/port_projection.md)
```

## Operator content

The full firm chapter body is inside the `new:book/src/L1/port_projection.md` fenced
block above. Summary of the apparatus:

- **Slug + one-line**: `port_projection` — the field-onto-port-mode linear-functional
  projection `α = ⟨s, E⟩`, the dual pairing of a fixed assembled FE covector `s` with a
  field `E`.
- **Signature**: `port_projection :: (s: Covector[N], E: Tensor[N]) -> Scalar` with the
  unconjugated dual contraction `Σᵢ sᵢ Eᵢ` and the port-kind / element-type table.
- **Record definition**: in-chapter `## Record definition` for `Covector[N]` (single
  consumer), backing C++ `mfem::LinearForm`.
- **Algebraic laws**: linearity in `E` (load-bearing — the linear-projection basis for
  `sparameter_reduce`), linearity in `s`, zero-annihilation, real/imag splitting; explicit
  absences (no conjugate-linearity/Hermitian symmetry, no PSD self-form, no argument-swap
  symmetry, FP non-associativity).
- **Dependencies**: leaf (none at L1).
- **Status**: `firm` (firm-on-positive-structure; kernel unit-tested; no-dedicated-test
  caveat non-gating per `apply_linop`/`jacobi-smoother`/`elementwise_product`).
- **Evidence**: both `GetSParameter` bodies + the covector-assembly sites + the two
  unit-test witnesses + the `sparameter_reduce` gate-b + the two NON-MATCH siblings.

**Index-registration partition (this dispatch):** I write (1) my dep-map TABLE row and (2)
my §Vocabulary-cohort BULLET (both above). The dispatch prompt names no count-owner and I am
not the consolidated-tally owner; the firm grand-total tally / growth-log update is **DEFERRED**
to the cycle's index-count owner (the running-count prose in `book/src/L1/index.md:31`
must increment 34→35 main-cohort-plus-sub-spines; I do not author the absolute total to avoid
the parallel-blind divergence — D4 also touches this index this cycle). SUMMARY.md registration
of my new chapter (the `new:book/src/SUMMARY.md` edit above, placed in alpha position under the
L1 Part's "Operator application & assembly" sub-grouping) is mine.

## Supporting evidence

- The load-bearing question is resolved structurally (see §"The load-bearing question" above):
  `s` / `port_sr` / `port_si` are `mfem::LinearForm` (covectors), confirmed at
  `palace/models/lumpedportoperator.hpp:51` and `palace/models/waveportoperator.hpp:101`;
  the assembly is a boundary linear form (`lumpedportoperator.cpp:162-196`). A covector is
  not the `Operator`/`LinearOperator[M,N]` matrix-weight that `bilinear-form` requires, and
  the unconjugated dual contraction is not the Hermitian co-spatial `dot`. OWN verb.
- All four primary L0 citations self-verified on-disk this dispatch: `citecheck --anchor`
  on the lumped `GetSParameter` (`:283-294`, anchor `GetSParameter`, `[ok]`), and direct
  on-disk `Read` of both function END lines (lumped `:294` `}`, wave `:793` `}`) per the
  FE-source END-drift caveat — the `--anchor` check confirms the anchor is in-range but not
  the upper bound, so the END lines were read directly.

## Open questions / caveats

- **COUPLED-COLUMN RE-CHECK (NOTED, not done here):** `book/src/L4/sparameter_reduce.md`
  gate-b is now satisfiable — `port_projection` is a live firm L1 slug. A later **coupled**
  pass should: (i) repoint `sparameter_reduce`'s "no firm L1 home" caveat
  (`sparameter_reduce.md:197-202,255-259`) to a live down-link `[port_projection](../L1/port_projection.md)`,
  (ii) re-evaluate whether closing gate-b alone (gate-a, the reduction-assembly test, still
  open) lets `sparameter_reduce` refine `rough-in` → `rough-in (test-coverage-bounded)`, and
  (iii) check the sparameters feature column's down-links. Per dispatch scope this is the
  double-gated coupled-column pass for a later cycle — I did NOT re-anchor `sparameter_reduce`
  or the sparameters column here.
- **L1>L0 lowering theme not authored** (out of harvester scope). The S-parameter projection
  rotation — lazy covector assembly, complex-from-real-pairings expansion, wave field
  transfer, `Mpi::GlobalSum` — wants either a dedicated `L1-L0` theme or an in-line note on
  an S-parameter rotation. Flagging `port-projection-l1-l0-rotation-home` as a follow-up plan
  candidate (low priority; the kernel laws are syntactic and the lowering is mechanical).
- **`Covector[N]` record-definition watch:** defined in-chapter (single consumer). If a
  second consumer of an assembled FE covector surfaces (e.g. a future `port_voltage` /
  `port_current` verb folding `(*v)·E` — the sibling `v` linear form at
  `lumpedportoperator.hpp:51`, `GetVoltage`/`GetCurrent` use the same dual-pairing shape),
  promote to `concepts/covector.md`. Flagging `assembled-fe-covector-record-definition-home`
  as a watch (not yet owed at the ≥2-consumer bar).
- **Sibling port functionals (`GetVoltage`, `GetCurrent`) are the same shape:** the lumped
  `(*v)·E` voltage projection (`lumpedportoperator.cpp:296-...`) is structurally identical
  (a different assembled covector `v`, same dual pairing). They are candidate future
  consumers of `port_projection` (or a shared covector-projection verb). Noted, not authored
  (one operator per invocation).
