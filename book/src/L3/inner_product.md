---
layer: L3
operator: inner_product
rank: firm
edges:
  depends-on:
    - L2/inner_product
    - L3/apply_linop
  reference:
    - L4/inner_product
    - L2-L1/inner-product-fold-specialization
    - concepts/dot
variant_axes:
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only; the family's namesake unification axis)
  - element-type (real / complex)
  - weight-presence (M = I plain / general-or-SPD M pre-applied — the `bilinear_form` member)
---

# inner_product

**`inner_product` is the L3 entry for the reduce-to-scalar inner-product family** —
the combinator IS the inner product at the iteration-rotation layer, rendered as a
whole-tensor reduce-to-scalar field reduction `α = ⟨x, y⟩`. The conjugation /
element-type / weight specializations Palace exposes — the Hermitian `dot`, the
unconjugated bilinear `tdot`, the matrix-weighted `xᴴ M y` (`inner_product_M`) — are
**specialization notes under this entry** (§"Specializations"), not separate co-equal
L3 chapters: they are this one reduce-to-scalar field reduction over the shape group `S`
read at fixed axis-values. **There is no sequential obstruction** — the reduction over
all independent positions of the shape group `S` is a parallel operation in exact arithmetic; the pinned
L0 reduction tree is a floating-point implementation choice (a recorded non-law),
deferred to the L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme, not an algebraic obstruction at L3.

> **Combinator-as-entry (vocabulary-shift redirect).** Per the
> vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md` §4-§5; CLAUDE.md
> §Methodology invariants ⟢), the L3 leaf cohort re-expresses through this combinator
> (`dot` = the Hermitian specialization; `nrm2` = the `√ ∘ abs ∘ inner_product`
> **consumer** at `y=x`, NOT a member) rather than each L3 leaf re-deriving the base form,
> mirroring the L2 combinator-as-entry inversion (the combinator IS the L2 entry; commit `92327f7`).

## Context

L3 is the **iteration-rotation** layer (`book/src/L3/index.md` §Semantics): global
tensor-field operations expressed as `state' = f(state, params)`, with sequential
obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md).
`inner_product` at L3 is a whole-tensor reduction — its signature
`Tensor[(S: ...)] -> Tensor[$S] -> Scalar` exposes no element loop; the reduction over the
shape group `S` is a single semantic step at L3, just as the L2 fold is a single
algebraic step at the fusion-rotation layer.

**At L3, `inner_product` is the entry** — it does not stand beside same-named L3 leaf
chapters; the conjugation / element-type / weight specializations are read off it at
fixed axis-values (§"Specializations"). This mirrors the L2 inversion: the upward
reference [`L2/inner_product`](../L2/inner_product.md) is the fusion-rotation combinator
(one fold parameterized by the conjugation/element-type/weight axes); this L3 entry is
its **iteration-rotation rendering** — the same reduce-to-scalar reduction, now read as
a single field-operation node in the L3 calculus.

This entry adds **iteration-rotation framing** to the combinator: it names
`inner_product` as an L3-native whole-tensor reduction consumed inside larger L3 forms
(most notably the [`krylov_step`](./krylov_step.md) body — CG's `α`/`β` coefficients,
GMRES orthogonalization coefficients — per the L3 `dot` consumption already recorded at
`book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" point 3). It
does not duplicate the combinator's algebraic-law derivations or its L0 evidence list —
those are authoritative at [`L2/inner_product`](../L2/inner_product.md) (firm); the laws hold uniformly across L1 / L2 / L3 because the body is
identity-in-form across the chain (§"Downward to L2").

This L3 field reduction is data-parallel, not iteration-structural: it is a pure
value-producing reduction over the shape group `S` with no control-flow, no monadic state
threading, and no convergence predicate (the per-element kernel is embarrassingly
parallel; only the final sum communicates — contrast L4 `iterate_while`, which threads
state through a stopping predicate). It lifts to [`L4/inner_product`](../L4/inner_product.md)
(firm) **identity-in-form on the body** — the L4 calculus combinator is
value-thread-isomorphic to this L3 reduction, with no dedicated L4>L3 theme file (the
eigsolve/chebyshev in-line-marker route), precisely because there is no monadic
state-threading or convergence predicate to dissolve across the edge. Under the
vocabulary-shift redirect the combinator IS
first-class L4 vocabulary that rises to the feature surface as a named verb. The
combinator also appears inside other L4 composed entries (e.g.
`book/src/L4/krylov_step.md` §Semantics) as a let-binding.

## Signature

```text
inner_product   :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar
inner_product_M :: Tensor[(S: ...)] -> LinOp[$S, $S] -> Tensor[$S] -> Scalar

inner_product   x y   = reduce (+) zero (zipWith kernel x y)   -- kernel from the table below
inner_product_M x M y = inner_product (apply_linop M x) y      -- weighted ≡ pre-apply M to arg-1, then plain
inner_product   x y   = inner_product_M x I y                  -- plain ≡ M = I
```

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../semantics/index.md) §1.2.1; no element loop exposed at L3):

- **`x`** — `Tensor[(S: ...)]` — read-only whole-tensor argument; the **conjugated** (arg-1)
  operand in the Hermitian inner product `xᴴ y` (see §"Conjugation convention").
- **`y`** — `Tensor[$S]` — read-only whole-tensor argument; the **linear** (arg-2) operand.
- **`M`** (weighted member) — `LinOp[(S: ...), $S]` — read-only; the matrix-weight (a
  square / endomorphic operator, domain ≡ range = `S`, §1.2.2),
  pre-applied to `x` via the opaque [`apply_linop`](./apply_linop.md) gate. The diagonal
  (`y = x`, SPD `M`) is the M-weighted norm-squared consumed downstream.
- **result** — `Scalar` — element type per the rule below; `zero` (the additive identity
  of the scalar field) on the empty tensor.
- `x` and `y` share one shape group `S` (arbitrary unknown rank) and one element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes; inherited from the L2 combinator,
reproduced for L3-reader coherence):

| element type | operator | per-element `kernel(x[idx], y[idx])` | form |
|---|---|---|---|
| `real`    | `inner_product` | `x[idx] · y[idx]`        | bilinear symmetric (conjugation is a no-op) |
| `complex` | `inner_product` | `conj(x[idx]) · y[idx]`  | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot`          | `x[idx] · y[idx]`        | unconjugated bilinear (see §"Specializations") |

No element loop is exposed at L3 — the reduction over every position `idx` of `S` is a single semantic
step in the L3 calculus. This is what makes `inner_product` L3-native by signature shape
(the same property that makes `dot`/`nrm2` L3-native, per
`book/src/L3-L2/krylov-step-body-identity.md:97`).

## Conjugation convention (pinned)

`inner_product` is **conjugate-linear in arg-1, linear in arg-2** (the standard
mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y = Σ_idx conj(x[idx])·y[idx]`), and the
M-weighted member conjugates the arg-1 (M-applied) operand: `inner_product_M(x, M, y) =
xᴴ M y`. This is inherited unchanged from the upward reference
[`L2/inner_product`](../L2/inner_product.md) §"Conjugation convention (pinned)" (which
pins arg-1 to agree with both L1 leaves). The L0 free-function asymmetry — Palace's
`linalg::Dot` pins the **opposite** operand (`yᴴ x`, arg-2 conjugated) — is the deliberate,
self-consistent L1 mutation-rotation re-order; the value-level effect (`xᴴ y` ↔ `yᴴ x`,
complex conjugates of each other) is **L1>L0 / L2>L1 lowering content**, not L3 content.
The genuine translation that carries the re-order is the KEPT
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
(§"Downward to L2"). L3 sees the convention pinned at arg-1
and a single-step whole-tensor reduction.

## Specializations

The members are **not separate L3 chapters** — they are this field reduction read at
fixed axis-values. Each is the combinator with one axis pinned; there is no co-equal
`L3/dot` / `L3/bilinear_form` floor beside this entry as a *member-of-the-fold*
(the firm L3 `dot` leaf is the Hermitian specialization re-expressed through this
combinator, a specialization note pointing here; `bilinear_form`
has no standalone L3 entry, it lives as the weighted member here):

```text
dot(x, y)              = inner_product x y                          -- Hermitian (complex) / symmetric (real); conjugated kernel, M = I
tdot(x, y)             = inner_product x y  with unconjugated kernel -- complex-only specialization
bilinear_form(x, M, y) = inner_product_M x M y                      -- M-weighted member: weight axis = general M
```

- **`dot`** — the conjugation axis at value *Hermitian* (complex) / *symmetric* (real),
  with `M = I`. The workhorse specialization (CG coefficients, orthogonalization, NLEPS).
  `dot` at L3 IS this specialization (no standalone leaf chapter — the residual
  `L3/dot` specialization-stub was eliminated, its conjugation
  variant-axis + krylov_step consuming context folded into this section). The kept named
  L4 verb [`L4/dot`](../L4/dot.md) re-expresses through this combinator.
- **`tdot`** — the conjugation axis at value *unconjugated bilinear* (complex-only).
  Co-defined with `dot` (no standalone L3 chapter); carried with the type-API-surface-only
  evidentiary caveat (zero Palace call sites — declaration + definition only) inherited
  from the L2 combinator §"tdot".
- **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. It has no standalone
  L3 chapter (its L1 leaf `bilinear_form` is firm — an identity-in-form L3 backfill candidate like
  its `matrix_weighted_norm` cohort-sibling; see `book/src/L3/index.md`); at L3 it is
  this weighted-member note.

The L3 entry differs from the L3 `dot`/`nrm2` leaves in **role**: the leaves mirror one
Palace L0 reduction surface each; this combinator is the single field-reduction node the
leaves re-express through. The element-type and conjugation sub-axes are identical to the
leaves' (inherited, not re-derived).

## Semantics

`inner_product` reduces the two tensors to a scalar: `inner_product(x, y) =
Σ_idx kernel(x[idx], y[idx])` over every position `idx` of the shape group `S`, with the per-element kernel from the table above.
At L3 this is rendered as a single semantic step — the reduction is **one node in the
iteration-rotation calculus**, not a loop.

The complex reduction is the **real reduction lifted componentwise over `(Re, Im)`** (the
element-type axis); the conjugation axis is the sign of the imaginary cross-term (negate
it to get `tdot`'s kernel). This is inherited unchanged from the L2 combinator §Semantics
(authoritative); the L3 form adds no decomposition — it adds the iteration-rotation framing
that names `inner_product` as an L3-native whole-tensor reduction.

The weighted member's internal workspace (the `M`-apply scratch buffer) is an L2>L1 /
L1>L0 lowering concern, not L3 algebra — at L3 the weighted member is the clean
composition `inner_product (apply_linop M x) y`.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `inner_product`'s iteration view is the reduction
over the shape group `S`. **The reduction lifts as a whole-tensor operation** — the
signature `Tensor[(S: ...)] -> Tensor[$S] -> Scalar` exposes no element loop, and the
reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded
non-law, not a structural element of the L3 form). **There is NO sequential obstruction**
for `inner_product` — the reduction over all independent positions of the shape group `S` is a parallel
operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point
implementation choice, not an algebraic obstruction at L3. This places `inner_product` at
the **obstruction-free end** of the L3 obstruction-profile spectrum
(`book/src/L3/index.md` §Semantics-overlay), alongside the leaf reductions `dot`/`nrm2` it
unifies. The MPI collective is **not** in the L3 signature (single-rank in scope per
CLAUDE.md §Scope; ranks read as their single-rank equivalents); the local-then-collective
two-step reappears only in the L1>L0 lowering.

`inner_product` is **consumed inside** larger L3 forms — most notably the
[`krylov_step`](./krylov_step.md) body (CG's `α = ⟨r, z⟩ / ⟨Ap, p⟩`; GMRES
orthogonalization coefficients), where it appears as a per-step let-binding. At L3 it is a
leaf reduction; the iteration view is what the surrounding `krylov_step` body provides.

## Algebraic laws

The L3 laws are **inherited unchanged from the L2 combinator** because the L3 form is
value-thread-isomorphic to the L2 reduction (§"Downward to L2"). They are reproduced here
so the L3 reader does not have to reach up to L2; [`L2/inner_product`](../L2/inner_product.md)
§"Algebraic laws" is authoritative.

**Defining reduction law (this is what makes the cohort one family):**

1. **Empty-tensor identity (the reduction's seed).** `inner_product` over an empty
   tensor is `zero` (the additive identity of the scalar field).

2. **Split-additivity / shape-concatenation-homomorphism (the defining law).**
   `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`,
   where `++` concatenates the shape group `S` and `+` is scalar addition. The reduction
   is a **monoid homomorphism from `(shape-concatenated tensors, ++)` to `(Scalar, +)`** —
   it collapses the shape group `S`. This is what licenses parallel/blocked evaluation of the
   reduction (the property underlying the no-obstruction verdict). The weighted member
   inherits it at whole-vector granularity (per-block only when `M` is block-diagonal
   w.r.t. the split).

**Sesquilinearity / bilinearity (uniform across members):**

3. **Conjugate-linearity in arg-1, linearity in arg-2** (complex Hermitian member):
   `inner_product (α·x₁ + x₂) y = conj(α)·inner_product x₁ y + inner_product x₂ y`;
   `inner_product x (α·y₁ + y₂) = α·inner_product x y₁ + inner_product x y₂`. The real
   member is bilinear (conjugation a no-op).

4. **Hermitian symmetry** (complex member): `inner_product x y = conj(inner_product y x)`;
   for the real member this reduces to plain **symmetry** `inner_product x y =
   inner_product y x`.

5. **Positive semi-definiteness at the diagonal** (`y = x`): `inner_product x x ∈ ℝ` and
   `inner_product x x ≥ 0`, with equality iff `x = 0` (exact arithmetic); for the weighted
   member with SPD `M`, `inner_product_M x M x ∈ ℝ₊`. This is the law the `nrm2` /
   `matrix_weighted_norm` **consumer** square-root rests on (§"Consumer"); it is confirmed
   by the L0 source (`&x == &y` imag=0 elision; SPD-realness assertion) cited at the L2
   combinator §"Algebraic laws".

6. **Zero in either argument.** `inner_product 0 y = inner_product x 0 = zero`.

7. **Weighted-member specialization (derived).** `inner_product_M x I y = inner_product x y`
   (plain ≡ `M = I`); `inner_product_M x M y = inner_product (apply_linop M x) y`.

Laws that explicitly **do not** hold:

- **Associativity of the reduction-tree under IEEE-754 (the load-bearing non-law).** The
  combining `(+)` is floating-point non-associative: different reduction trees give
  different bit-level results. This is a **load-bearing numerical trick** per CLAUDE.md
  §"Optimization tricks vs. base algebra" — recorded, not erased. **The L3 reduction is
  order-agnostic for value (hence no sequential obstruction), but bit-identical
  reproduction of an L0 reduction requires matching that reduction's pinned tree.** Which
  tree each lowered call pins is recorded by the L2>L1
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
  (the genuine translation, not restated here). This
  is exactly the distinction the no-obstruction verdict turns on: the *value* lifts to a
  parallel whole-tensor reduction; only the *pinned tree* is an L0 non-law.

- **Cauchy–Schwarz strictness in floating point.** `|inner_product x y|² ≤
  inner_product x x · inner_product y y` holds mathematically but can fail by ULP-level
  amounts due to summation ordering.

- **Positive-definiteness of `tdot`.** The unconjugated bilinear member is **not** PSD:
  `tdot x x ∈ ℂ` in general, and `tdot x x = 0` does not imply `x = 0` (e.g. `x = (1, i)`
  gives `0`). Law 5 is a Hermitian-member law only.

## Dependencies

- **Same-layer (L3)** — for the weighted member only: [`apply_linop`](./apply_linop.md)
  (the opaque `M`-apply gate pre-applied to arg-1: `inner_product_M x M y =
  inner_product (apply_linop M x) y`). The plain/Hermitian/unconjugated members have no
  same-layer L3 dependency (the per-element kernel and the shape-group `S` reduction are at or
  below the L3 layer's resolution).
- **Consumers (L3)**: [`krylov_step`](./krylov_step.md) (CG/GMRES coefficients). The
  do-NOT-merge consumers [`nrm2`](#consumer-nrm2-and-matrix-weighted-norm) / `matrix_weighted_norm` are
  `√ ∘ abs ∘ inner_product` at `y=x` — see §"Consumer (NOT an instance)".
- **Upward reference (L2)**: [`L2/inner_product`](../L2/inner_product.md) (firm) — authoritative on the algebraic laws,
  the conjugation reconciliation, and the L0 evidence list. The L3 form is identity-in-form
  to the L2 reduction (§"Downward to L2").
- **L2>L1 lowering theme** (the genuine translation; KEPT):
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) —
  carries the conjugation/element-type/weight dispatch, the `xᴴ y` ↔ `yᴴ x` re-order, and
  the per-call pinned reduction trees (the load-bearing IEEE non-law content). Referenced,
  not restated.
- **Concepts**: [`dot`](../concepts/dot.md) — the BLAS-1-heritage / cross-cutting prose
  framing for the inner-product reduction; the element-type axis is carried there.

## Variant axes

`inner_product` has three variant axes; the **conjugation-convention** axis is the one
this combinator unifies (NOT a remaining variant — it is the unification axis), inherited
unchanged from the L2 combinator §"Variant axes":

1. **Conjugation convention** — `kernel = conj(x[idx])·y[idx]` (Hermitian `dot`) vs
   `kernel = x[idx]·y[idx]` (unconjugated `tdot`). The family's namesake unification axis;
   `tdot` is its second value (type-API-surface-only caveat).
2. **Element-type** — `real | complex`. At L3 one reduction parameterized by element type;
   the complex reduction is the real reduction lifted componentwise. (Concept-page-carried
   at [`dot`](../concepts/dot.md).)
3. **Weight presence** — `M = I` (plain) vs general / SPD `M` pre-applied to arg-1
   (`inner_product_M`, the `bilinear_form` member). Orthogonal to conjugation, **but the
   `tdot × weight` cell is scoped out**: Palace exposes no unconjugated weighted member
   (`inner_product_M` conjugates arg-1; `tdot` is type-API-surface-only with zero call
   sites), so the weight axis interacts only with the Hermitian/real conjugation values —
   there is no `tdot_M`.

**Diagonal degeneration (`y = x`) is NOT a variant axis — it is a consumer entry point**
(collapses the reduction to the norm-squared consumed by `nrm2`/`matrix_weighted_norm`;
§"Consumer"). **Reduction tree is an L0 implementation detail, NOT an L3 variant axis** —
transparent for value, load-bearing for bit-reproduction (the IEEE non-law); recorded in
the L2>L1 lowering theme.

## Consumer: nrm2 and matrix_weighted_norm

`nrm2` and `matrix_weighted_norm` are `√ ∘ abs ∘ inner_product` at the diagonal (`y = x`),
**NOT fold/reduction members** — they are **consumers** of this combinator's output:

```text
nrm2(x)                  = √ (abs (inner_product x x))         -- √ ∘ abs ∘ inner_product at y = x
matrix_weighted_norm(x, B) = √ (inner_product_M x B x)        -- SPD B
```

The `√ ∘ abs` post-step is a downstream scalar map; the norm is not a reduction and does
not enter this entry's signature. Merging `nrm2` into `inner_product` would be a category
error — `inner_product` is the shape-group `S` homomorphism producing `⟨x, x⟩`; `nrm2` is the
scalar map `α ↦ √|α|` applied to that output. `nrm2` at L3 IS this consumer (no standalone
leaf chapter — the residual `L3/nrm2` consumer-stub was eliminated, the
load-bearing `std::abs` defensive guard + the Arnoldi-sub-diagonal / residual-norm consuming
context folded into this section; do-NOT-merge boundary preserved — `nrm2` is the
`√∘abs∘inner_product` consumer, NOT a fold member). The kept named L4 verb
[`L4/nrm2`](../L4/nrm2.md) consumes this combinator at the diagonal. Law 5 (PSD at the
diagonal) is exactly the property that
makes the consumer square-root well-defined; this section records the boundary, not a
subsumption.

## Caveats

> **Member-level caveat (not a status reduction; inherited from L2).** `tdot` is carried
> as the unconjugated conjugation-axis value with a type-API-surface-only evidentiary note
> (zero Palace call sites — declaration + definition only). The reduction *structure* is
> firm and the other two axis values (`dot`, weighted) are behaviorally exercised; only
> `tdot`'s behavioral weight is API-only.

## Downward to L2

L3 `inner_product` lowers to L2 [`inner_product`](../L2/inner_product.md) as
**identity-in-form on the body** — the L3 reduction is value-thread-isomorphic to the L2
reduction (the same `reduce (+) zero (zipWith kernel x y)` skeleton; the L3 layer's
iteration-rotation framing names it a single field-reduction node, the L2 layer's
fusion-rotation framing names it the canonical fold the fused kernels unfold into; the
*value thread is identical*). There is **no L3-L2 theme file** — the identity-in-form
annotation lives in-line here, per the non-adjacent-identity convention (CLAUDE.md
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"; precedent `book/src/L3/krylov_step.md`, and this entry's own §"Specializations"
absorbing the former `L3/dot` leaf's "Downward to L2 (through inner_product)" framing). This section is the **home** the degenerate
`dot-body-identity` L3>L2 identity-in-named-terms theme was demoted into ("L3>L2 is identity-in-named-terms — no rotation;
`dot` is the Hermitian specialization of the `inner_product` combinator at both layers";
the `L3-L2/dot-body-identity.md` file was deleted, its identity-in-form content absorbed
here).

Transitively (L3>L2 identity ∘ L2>L1 substantive), the L3 form lowers to the L1 leaves
through the L2 combinator: the **genuine** translation is the L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
(KEPT) — the conjugation/element-type/weight dispatch + the value-level
`xᴴ y` ↔ `yᴴ x` re-order + the per-call pinned reduction trees (the load-bearing IEEE
non-law content). No `book/src/L3-L1/` directory — the non-adjacent identity-rotation
annotation is in-line per the same convention.

## Evidence

The L3 form is value-thread-isomorphic to the L2 combinator; **all L0 evidence is inherited
transitively through the firm L2 entry** and is **not
re-localized at L3** per the high→low layer-definition discipline. Direct citations relevant
to this L3 entry:

- [`book/src/L2/inner_product.md`](../L2/inner_product.md) (firm; combinator-as-entry, commit `92327f7`) — the upward reference; authoritative
  on the signature, algebraic laws (inherited unchanged at L3), conjugation reconciliation,
  variant axes, and the complete L0 evidence list (`palace/linalg/vector.cpp:263-267`
  Hermitian kernel, `:269-274` `tdot`, `:664-672` real reduction / `:674-685` complex reduction; `palace/linalg/operator.cpp:598-617`
  SPD-norm + realness assertion, `:621-638` weighted member; `palace/linalg/vector.hpp:247-253`
  local-then-collective; `test/unit/test-vector.cpp:206-207` real-dot value test).
- [`book/src/L3/index.md`](./index.md) §Semantics line 12 — the L3 vocabulary inventory
  names the reductions (`dot`, `nrm2`) as field operations; this combinator is the entry
  they re-express through. Line 15 §Semantics-overlay obstruction-profile spectrum — the
  obstruction-free end this entry sits at.
- [§"Specializations"](#specializations) — the
  Hermitian/unconjugated `dot` specialization (the residual standalone `L3/dot` leaf,
  firm, was eliminated; its conjugation variant-axis +
  no-sequential-obstruction verdict + krylov_step consuming context are folded here).
- [§"Consumer (NOT an instance)"](#consumer-nrm2-and-matrix-weighted-norm) — the
  `√ ∘ abs ∘ inner_product` consumer `nrm2` (the residual standalone `L3/nrm2` leaf, firm
  was eliminated; do-NOT-merge boundary preserved — NOT a member).
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md)
  — the KEPT genuine L2>L1 translation; the pinned-tree IEEE non-law + conjugation re-order
  home (referenced, not restated).
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md)
  §"Applicability conditions" point 3 — the structural justification that the reduction
  primitives are L3-native by signature shape (no per-element loop visible), which licenses
  the identity-in-form L3>L2 rotation.
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the BLAS-1 heritage / cross-cutting
  framing; the element-type axis.

## L3 vs L2 distinction

- **L2**: one fusion-rotation fold `inner_product` over `(Tensor[(S: ...)], Tensor[$S])` with an
  optional pre-`apply_linop M`; the family of fused reduction kernels (a kernel-fusion
  choice) is unfolded into the canonical `foldl (+) zero (zipWith kernel x y)`; the pinned
  reduction tree is de-fused into the fold's seed-and-accumulate. The combinator IS the L2
  entry.
- **L3**: the same reduce-to-scalar reduction rendered as a single whole-tensor
  field-operation node in the iteration-rotation calculus — no element loop, no sequential
  obstruction (parallel-clean in exact arithmetic), consumed inside larger L3 forms
  (`krylov_step`). The combinator IS the L3 entry; the conjugation/element-type/weight
  specializations are notes under it.

The two layers' entries are **value-thread-isomorphic** on the reduction itself. The L3
entry exists for layer-coherence (each layer is coherent within itself; a reader at L3
must find `inner_product` defined in L3 vocabulary) and as the combinator the L3 leaf
cohort re-expresses through — per CLAUDE.md §Methodology invariants ⟢ (the combinator is
the entry, members are specialization notes) + "Identity-lowerings still require both L
levels".
