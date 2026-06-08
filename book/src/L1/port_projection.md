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
(its `project sᵢ E = sᵢ·E` step) — this entry is that reduction's per-port projection
L1 home.

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
this should be promoted to a `concepts/covector.md` record-definition page.)

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
field transfer onto the port space, and the `Mpi::GlobalSum` collective.

## Evidence

- `palace/models/lumpedportoperator.cpp:283-294` — `LumpedPortData::GetSParameter`
  (def `:283`, body `:285-293`, closes `:294`): the lumped projection
  `dot = (*s)·E.Real() [+ i·(*s)·E.Imag()]` — the single-real-covector dual pairing.
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
  (`:789-790`); `MFEM_VERIFY(E.HasImag())` guard `:784-786`.
- `palace/models/waveportoperator.hpp:101` — `std::unique_ptr<mfem::LinearForm> port_sr, port_si;`
  — the wave port mode is a **complex** covector `port_sr + i·port_si` (two assembled
  real `LinearForm`s). Confirms the complex-covector / non-Hermitian shape.
- `test/unit/test-lumpedportintegration.cpp:367` + `:720` —
  `std::complex<double> s_param = port_1.GetSParameter(...)`: dedicated unit tests
  exercising the lumped projection kernel directly (L0-equivalent semantic evidence).
- `test/unit/test-romoperator.cpp:603` — `auto S = port_data.GetSParameter(E)`:
  the projection kernel exercised in the ROM-operator test.
- `book/src/L4/sparameter_reduce.md:86,197-202,255-259` — the L4 driven reduction
  that folds this projection (`project sᵢ E = sᵢ·E`); this entry is its per-port
  projection L1 home.
- `book/src/L1/bilinear-form.md:62-94` — the candidate-subsume verb (`xᴴ M y`,
  matrix-weighted two-vector); the load-bearing question resolved NON-MATCH (a
  covector is not an `Operator`).
- `book/src/L1/dot.md` lines 34, 63-75 — the co-spatial Hermitian reduction sibling
  (`conj(x)·y`) and its unconjugated bilinear variant `tdot`; resolved NON-MATCH
  (a covector dual pairing is not a co-spatial inner product).
- `book/src/L1/index.md` — dep-map this entry adds a row to.
