---
agent: harvester
invoked_at: 2026-05-29T024500Z
scope: L2 operator: inner_product
status: integrated
integrated_at: 2026-05-29T08:10:00Z
integration_commit: efb8a0b
integration_notes: "cycle-019 finalize. HEADLINE. inner_product PROMOTED rough-in→firm (reduce-to-Scalar fold (x,y) -> Scalar ≡ foldl (+) zero (zipWith kernel x y) unifying dot/tdot/bilinear-form along conjugation-convention/element-type/weight-presence axes; conjugation PINNED arg-1 xᴴ y with §reconciliation vs Palace arg-2 yᴴ x; 7 laws incl. IEEE reduction-tree non-law; sibling linear_combination NOT subsumed; consumer nrm2/matrix-weighted-norm = √∘inner_product). L2/index :26 row rough-in→firm flip (orthogonalize row :27 untouched); SUMMARY :40 de-stub. L2 firm contributes to 3→5; rough-in cohort → 0. retroactive-budget 0; clean build."
inputs:
  - reports/2026-05-29T023000Z-combinator-miner-parametric-family/CYCLE.md (wave-1 parametric-family characterization; fold-law + axis taxonomy + two caveats)
  - book/src/L2/inner_product.md (the cycle-018-rough-in / cycle-019-stub being firmed)
  - book/src/L2/index.md (dep-map row 26 — rough-in → firm flip)
  - book/src/L2/linear_combination.md (structural precedent: L1-leaves → L2-fold harvest, cycle-018)
  - book/src/L1/dot.md (the dot/tdot leaves; arg-1-conjugated L1 convention at :34,:43)
  - book/src/L1/bilinear-form.md (the M-weighted leaf; arg-1-conjugated `xᴴ M y` convention at :19,:63; conjugation-anchor resolution at :50-53)
  - OQ inner-product-harvester-formalization-and-conjugation-pinning (highest-fan-out head item)
  - Self-verified Palace ranges: vector.cpp:263-274, :664-685, :700-712; vector.hpp:105-120, :240-262; operator.cpp:598-617, :621-638; operator.hpp:384-396; boundarymodeoperator.cpp:82-92; iterative.cpp:393-406; nleps.cpp:485-493; test/unit/test-vector.cpp:204-212
---

# CYCLE: Formalize inner_product at L2

## Summary

Promote the L2 `inner_product` stub (cycle-018 rough-in dep-map row; cycle-019 stub home `book/src/L2/inner_product.md`) to a **firm** L2 entry. `inner_product` is the reduce-to-`Scalar` fold `(Tensor[N], Tensor[N]) -> Scalar ≡ foldl (+) zero (zipWith kernel x y)`, the **conjugation-convention / element-type / weight-presence** sibling family of the BLAS-1 reduction cohort, unifying the L1 leaves `dot` (Hermitian), `tdot` (unconjugated bilinear), and the M-weighted member realized by `bilinear-form` (`xᴴ M y`). It is the structural sibling of the already-firm `linear_combination` (cycle-018) but a **different fold** (reduce-to-`Scalar`, not reduce-to-`Tensor[N]`) and must not be merged with it; nor does it subsume `nrm2` / `matrix-weighted-norm`, which are `√ ∘ inner_product` consumers at the diagonal. The two wave-1 combinator-miner caveats are handled in-entry: (1) the **conjugation convention is PINNED** — `inner_product(x, y) = xᴴ y` (conjugate-linear in **arg-1**), reconciled against Palace's source/doc `Dot(comm, x, y) = yᴴ x` (arg-2 conjugated) as the deliberate, self-consistent L1 mutation-rotation re-order that both `dot.md` and `bilinear-form.md` already adopt; (2) `tdot`'s **zero-call-site / type-API-surface-only** status is flagged, with positive anchors leaning on `dot` + the M-weighted bilinear form (both have call sites). The fold-law is split-additivity / length-concatenation-homomorphism `(length-concat, ++) → (Scalar, +)`.

## Proposed changes

```edit:book/src/L2/inner_product.md
[full rewrite — stub → firm; see "Operator content" below for the file body]
```

```edit:book/src/L2/index.md
[flip dep-map row 26 from rough-in to firm — replace the existing `inner_product` row]
```

Replace the current row (`book/src/L2/index.md:26`):

```
| [`inner_product`](./inner_product.md) (stub — harvester to firm) | `(Tensor[N], Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (shorthand — exact conjugation/arg-order convention to be pinned by harvester; Palace documents `Dot(comm,x,A,y)` as `yᴴ A x`, body `(Ax)ᴴ y = xᴴ Aᴴ y` — see caveat 7), plain ≡ `M = I` | L1 leaves it fuses up from: `dot`, `tdot` (firm), `bilinear-form` (rough-in, the M-weighted member). L2-composition for the weighted member: `apply_linop` (M applied to first arg). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; different laws, no shared concatenation/PSD structure). Consumer (NOT an instance): `matrix-weighted-norm` = `√ ∘ inner_product_M` at `y=x`, SPD `B`. | `(rough-in, proposed-by: combinator-miner:2026-05-28T231046Z)` |
```

with:

```
| [`inner_product`](./inner_product.md) | `(x: Tensor[N], y: Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (arg-1-conjugated convention, pinned — matches the L1 `dot`/`bilinear-form` leaves; Palace's free-function `Dot(comm,x,y) = yᴴ x` conjugates arg-2, the deliberate L1 re-order — see entry §"Conjugation convention (pinned)"); plain ≡ `M = I` | L1 leaves it fuses up from: `dot` (Hermitian), `tdot` (unconjugated; firm but type-API-surface only — zero Palace call sites), `bilinear-form` (M-weighted member, rough-in). L2-composition for the weighted member: `apply_linop` (M applied to the linear/arg-1 operand). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; folds the term axis, keeps `N`; different homomorphism). Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`. | `firm` (harvested cycle-019; promoted from rough-in proposed-by combinator-miner:2026-05-28T231046Z; family-mode characterized combinator-miner:2026-05-29T023000Z; conjugation pinned per OQ inner-product-harvester-formalization-and-conjugation-pinning) |
```

```edit:book/src/SUMMARY.md
[de-stub the L2 chapter entry: replace `- [inner_product (stub)](./L2/inner_product.md)` with `- [inner_product](./L2/inner_product.md)`]
```

## Operator content

The full file body written into `book/src/L2/inner_product.md`:

---

# inner_product

The conjugation-convention-family unification of the BLAS-1 reduce-to-scalar
inner-product cohort: the L1 leaves [`dot`](../L1/dot.md) (Hermitian),
`tdot` (the unconjugated bilinear variant, co-defined in [`dot`](../L1/dot.md)),
and the matrix-weighted member [`bilinear-form`](../L1/bilinear-form.md)
(`xᴴ M y`) are the conjugation / element-type / weight-presence specializations
of a single **reduce-to-scalar fold** over the length axis. The fusion-rotation
form: Palace's distinct reduction call shapes (`ComplexVector::Dot` /
`TransposeDot`, `linalg::LocalDot` over real and complex, `linalg::Dot(comm,x,A,y)`
for the weighted member — each a Hypre-kernel + MPI-tree-reduce fusion choice) are
unfolded into the canonical `foldl (+) zero (zipWith kernel x y)`, with the pinned
reduction tree de-fused into the fold's seed-and-accumulate.

## Context

At L1, the inner-product leaves mirror Palace's L0 reduction surface: `dot`/`tdot`
share [`dot`](../L1/dot.md) (the conjugation axis at one chapter), and the
M-weighted reduction is the separate leaf [`bilinear-form`](../L1/bilinear-form.md).
Those leaves stay firm L1 — `inner_product` is the form they fuse *up* into at L2;
it does not replace them.

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Batched specialized BLAS
calls are written as compositions of base primitives… Kernel fusion across multiple
algebraic operations is unfolded into composition." Palace exposes the reduction as a
family of fused kernels (the real path is one Hypre `hypre_SeqVectorInnerProd`; the
complex path composes four real local dots into a `(Re, Im)` scalar; the weighted path
pre-applies `M` then reduces) and a local-then-collective two-step
(`LocalDot` ∘ `Mpi::GlobalSum`). Unfolding that family of fused reduction shapes into
the one canonical fold is the L2 rotation along the **conjugation-convention** axis —
the structural sibling of the **arity** axis unified by
[`linear_combination`](./linear_combination.md) and the **element-type** axis carried
at the concept-page level by [`dot`](../concepts/dot.md). The conjugation convention is
pinned in § "Conjugation convention (pinned)" below.

This is an L2 fold, not an L4 combinator: `inner_product` is a pure value-producing
reduction over the length axis, with no control-flow, no monadic state threading, and
no convergence predicate. It is a data-parallel reduction (the per-element kernel is
embarrassingly parallel; only the final sum communicates), not iteration-structural
(contrast L4 `iterate_while`, which threads state through a stopping predicate). It
belongs with the tensor algebra at L2.

The sibling reduction `linear_combination` is a **different** fold — see
§ "Sibling fold: linear_combination is not subsumed".

## Conjugation convention (pinned)

`inner_product` is **conjugate-linear in arg-1, linear in arg-2** (the standard
mathematical Hermitian inner product):

$$ \text{inner\_product}(x, y) = x^{\mathsf H} y = \textstyle\sum_{i} \overline{x_i}\, y_i $$

and the M-weighted member conjugates the arg-1 (M-applied) operand:

$$ \text{inner\_product\_M}(x, M, y) = x^{\mathsf H} M y . $$

This is the convention the L1 leaves it fuses up from already adopt
([`dot`](../L1/dot.md) §Semantics, "conjugate-linear in the **first** argument";
[`bilinear-form`](../L1/bilinear-form.md) §Signature, `bilinear_form(x, M, y) = xᴴ M y`).
The L2 entry inherits it unchanged so the fold and its leaves agree.

**Reconciliation against the Palace source — the deliberate L1 re-order.** Palace's
L0 surface pins the **opposite** operand: the free-function and its kernels conjugate
**arg-2** (the second operand), not arg-1.

- Doc strings say `yᴴ x`: `palace/linalg/vector.hpp:109` (`ComplexVector::Dot`,
  `// Vector dot product (yᴴ x) or indefinite dot product (yᵀ x)`),
  `palace/linalg/vector.hpp:242` / `:246` (`LocalDot` / free-function `Dot`,
  `// Calculate the … inner product yᴴ x or yᵀ x`), `palace/linalg/operator.hpp:386`
  (weighted, `// Compute the bilinear form inner product yᴴ A x`).
- The kernel bodies **agree with the docs** (no Palace-internal contradiction —
  contra the combinator-miner's wording of a "contradiction", which is between Palace
  and the L1 entry, not within Palace): `ComplexVector::Dot(y)` body
  (`palace/linalg/vector.cpp:263-267`) returns
  `{Re(x)·Re(y)+Im(x)·Im(y), Im(x)·Re(y)−Re(x)·Im(y)} = x·\overline{y} = y^{\mathsf H} x`
  (the imaginary cross-term sign is `+Im(x)Re(y)−Re(x)Im(y)`, i.e. arg-2 `y` is the
  conjugated operand). The local complex fold
  (`palace/linalg/vector.cpp:674-685`) has the same `Im = LocalDot(xi,yr)−LocalDot(xr,yi)`
  sign — again arg-2 conjugated. The weighted free-function
  (`palace/linalg/operator.cpp:621-628`) builds `Ax = A·x` then returns
  `Dot(comm, Ax, y) = y^{\mathsf H}(Ax) = y^{\mathsf H} A x` — arg-2 `y` conjugated.

So **Palace = `yᴴ x` (arg-2 conjugated); the L1/L2 representation = `xᴴ y`
(arg-1 conjugated)**. The two are complex conjugates of each other
(`xᴴ y = \overline{y^{\mathsf H} x}`). The re-order is the **intentional L1
mutation-rotation choice** recorded at [`dot`](../L1/dot.md) §Semantics — the L1 form
erases the method `receiver.Dot(arg)` / free-function `Dot(comm,x,y)` asymmetry and
fixes arg-1 as the conjugated operand "by convention". It is **not** a defect: the
`bilinear-form` entry independently verified the L0 source is self-consistent and
retracted an earlier draft's alleged comment-vs-implementation disagreement
([`bilinear-form`](../L1/bilinear-form.md):50-53; OQ
`bilinear-form-conjugation-convention-anchor`). The L2 entry pins arg-1 to stay
consistent with both leaves; the **value-level effect of the re-order** (Palace's
`yᴴ x` vs the representation's `xᴴ y`) is a conjugation that the L2>L1 lowering theme
records explicitly when it maps the L2 fold onto the L0 call (forward-reference only —
`inner-product-fold-specialization`, not authored here).

For algorithms that take a real projection (`std::real`, `std::abs`) of the result —
e.g. CG's `β = ⟨r, z⟩` for SPD `B` (`palace/linalg/iterative.cpp:395`), or norms via
`std::abs(linalg::Dot(...))` (`palace/linalg/nleps.cpp:487,492`) — the re-order is
invisible (the projection of a value and of its conjugate agree), which is why the
two conventions coexist harmlessly in the Palace call sites.

## Signature

```text
inner_product   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
inner_product_M :: (x: Tensor[N], M: LinearOperator[N, N], y: Tensor[N]) -> Scalar

inner_product   x y   = foldl (+) zero (zipWith kernel x y)   -- kernel from the table below
inner_product_M x M y = inner_product (apply_linop M x) y     -- weighted ≡ pre-apply M to arg-1, then plain
inner_product   x y   = inner_product_M x I y                 -- plain ≡ M = I
```

Shape contract (bunsen-style; named axes):

- `x` — `Tensor[N]` — read-only; the **conjugated** (arg-1) operand (see § "Conjugation
  convention (pinned)").
- `y` — `Tensor[N]` — read-only; the **linear** (arg-2) operand.
- `M` (weighted member) — `LinearOperator[N, N]` — read-only; the matrix-weight,
  pre-applied to `x` (the linear-operator type is the opaque
  [`apply_linop`](../L1/apply_linop.md) interface). For the off-diagonal cross-coupling
  use the codomain of `M` matches the length axis of `y`; the diagonal
  (`y = x`, SPD `M`) is the norm-squared consumed downstream.
- result — `Scalar` — element type per the rule below; `zero` (the additive identity of
  the scalar field) on the empty length axis.
- `x` and `y` share one length axis `N` and one element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes):

| element type | operator | per-element `kernel(x[i], y[i])` | form |
|---|---|---|---|
| `real`    | `inner_product` | `x[i] · y[i]`             | bilinear symmetric (conjugation is a no-op) |
| `complex` | `inner_product` | `conj(x[i]) · y[i]`      | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot`          | `x[i] · y[i]`            | unconjugated bilinear (see § "tdot") |

The three L1 leaves recovered as specializations along the family axes:

```text
dot(x, y)              = inner_product x y                       -- Hermitian (complex) / symmetric (real)
tdot(x, y)             = inner_product x y  with unconjugated kernel  -- complex-only, see § "tdot"
bilinear_form(x, M, y) = inner_product_M x M y                   -- M-weighted member
```

The L2 form differs from the L1 leaves in **resolution**, along the
conjugation-convention / weight-presence axes: L1 sees `dot`/`tdot` (the conjugation
axis at one chapter) and `bilinear-form` (the separate M-weighted chapter); L2 sees one
fold whose `kernel` and optional pre-`apply_linop M` recover each leaf. The element-type
sub-axis is identical to the leaves' (inherited, not re-derived).

## Semantics

`inner_product` reduces the two tensors to a scalar: starting from the additive identity
`zero`, it folds the per-element products `kernel(x[i], y[i])` over the length axis `N`.
The result is `Σᵢ kernel(xᵢ, yᵢ)` — the (Hermitian / bilinear / M-weighted) inner product
of `x` and `y`.

The complex fold is the **real fold lifted componentwise over `(Re, Im)`**: the complex
local reduction is four real reductions combined into a `(Re, Im)` scalar
(`palace/linalg/vector.cpp:674-685`):
`Re = LocalDot(xr,yr)+LocalDot(xi,yi)`, `Im = LocalDot(xi,yr)−LocalDot(xr,yi)`. The real
member has no imaginary track (`palace/linalg/vector.cpp:664-672`, a single Hypre
`hypre_SeqVectorInnerProd`). This is the element-type axis; the conjugation axis is the
sign of the `Im` cross-term (negate it and you get `tdot`'s kernel — see § "tdot").

It is **pure** at L2: it consumes `x`, `y` (and `M`) and produces a fresh scalar; there
is no destination buffer (the L0 in-place destination is the return register / a stack
scalar). The weighted member's internal workspace `Ax` (the `A.Mult` scratch buffer at
`palace/linalg/operator.cpp:623-627`) is an L2>L1 lowering concern, not L2 algebra — at
L2 the weighted member is the clean composition `inner_product (apply_linop M x) y`.

The fold **reduces over the length axis `N`** and therefore carries an **MPI collective**
in the L0 realization (`LocalDot` ∘ `Mpi::GlobalSum`, `palace/linalg/vector.hpp:247-253`).
The collective is **not** in the L2 signature (single-rank scope; ranks read as their
single-rank equivalents). This is the structural opposite of
[`linear_combination`](./linear_combination.md), which is element-local in `N` and folds
over the *term list* (no collective) — see § "Sibling fold".

The self-inner-product fast path `&x == &y` (`palace/linalg/vector.cpp:266` returning
imaginary part `0.0` for the Hermitian form; `:272-273` returning `2·Im·Re` for `tdot`)
is a transparent performance trick at L2 — algebraically `xᴴ x` is exactly real, so
eliding the cancellation is equivalent. It disappears in the L2>L1 lowering.

## Algebraic laws

The laws below hold; absences are deliberate.

**Defining fold law (this is what makes the cohort one family):**

1. **Empty-axis identity (the fold's seed).** `inner_product` over a zero-length axis is
   `zero` (the additive identity of the scalar field) — the fold's initial accumulator.

2. **Split-additivity / length-concatenation-homomorphism (the defining law).**
   `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`,
   where `++` concatenates along the length axis and `+` is scalar addition. The fold is
   a **monoid homomorphism from `(length-concatenated tensors, ++)` to `(Scalar, +)`** —
   it collapses the length axis. This is the inner-product analogue of
   `linear_combination`'s concatenation-homomorphism, and it is exactly what licenses
   tiling / blocking of the reduction (the transparent HPC trick the L2 fold absorbs).
   It holds for every member; the weighted member inherits it at **whole-vector
   granularity** — `inner_product_M(x, M, y) = inner_product (apply_linop M x) y` is one
   fold over the M-applied operand, so the per-block split-law for `inner_product_M`
   holds only when `M` is block-diagonal w.r.t. the split (the general weighted case is
   stated at whole-vector level, not per-block — see § "Variant axes" and caveat).

**Sesquilinearity / bilinearity (uniform across members):**

3. **Conjugate-linearity in arg-1, linearity in arg-2** (complex Hermitian member):
   `inner_product (α·x₁ + x₂) y = conj(α)·inner_product x₁ y + inner_product x₂ y`;
   `inner_product x (α·y₁ + y₂) = α·inner_product x y₁ + inner_product x y₂`. The real
   member is bilinear (conjugation a no-op): linear in each argument. (Generalizes
   [`dot`](../L1/dot.md) laws 2–3 (real) / 7–8 (complex).)

4. **Hermitian symmetry** (complex member): `inner_product x y = conj(inner_product y x)`.
   For the real member this reduces to plain **symmetry** `inner_product x y =
   inner_product y x`. (Generalizes [`dot`](../L1/dot.md) law 1 / law 6.)

5. **Positive semi-definiteness at the diagonal** (`y = x`): `inner_product x x ∈ ℝ`
   and `inner_product x x ≥ 0`, with equality iff `x = 0` (exact arithmetic). For the
   weighted member with SPD `M`, `inner_product_M x M x ∈ ℝ₊`. This is the law
   `nrm2` / `matrix-weighted-norm` square-root (those are `√ ∘ inner_product` at `y=x` —
   see § "Consumer"); it is **confirmed by the implementation** returning imaginary part
   `0.0` exactly when `&x == &y` (`palace/linalg/vector.cpp:266`,
   `palace/linalg/vector.cpp:679`) and by the SPD-norm assertion
   `dot.real() > 0 && |dot.imag()| < 1e-9·dot.real()`
   (`palace/linalg/operator.cpp:611-616`, comment "For SPD B, xᴴ B x is real" at
   `:611`, assertion at `:615-616`).

6. **Zero in either argument.** `inner_product 0 y = inner_product x 0 = zero`.
   (Generalizes [`dot`](../L1/dot.md) law 5 / law 10.)

7. **Weighted-member specialization (derived).** `inner_product_M x I y = inner_product x y`
   (plain ≡ `M = I`), and `inner_product_M x M y = inner_product (apply_linop M x) y`
   (weighted ≡ pre-apply `M` to arg-1, then plain). The conjugation lands on the M-applied
   operand: `inner_product_M x M y = (Mx)ᴴ y = xᴴ Mᴴ y` for the value, pinned to
   `xᴴ M y` in the representation per § "Conjugation convention (pinned)". (Matches
   [`bilinear-form`](../L1/bilinear-form.md) §"Specialisation to `dot`".)

Laws that explicitly **do not** hold:

- **Associativity of the reduction-tree under IEEE-754 (the load-bearing non-law).**
  The fold's combining `(+)` is floating-point non-associative: different summation
  orders (different reduction trees) give different bit-level results. Palace pins a
  specific tree (Hypre per-rank kernel + MPI tree-reduce). Per CLAUDE.md "load-bearing
  numerical tricks… non-associative reduction orderings… preserve as explicit algebraic
  claims", this is recorded, not erased: **the L2 fold is order-agnostic for value, but
  bit-identical reproduction of an L0 reduction requires matching that reduction's pinned
  tree.** Which tree a given lowered call pins is recorded by the L2>L1 lowering theme
  (forthcoming — see § "Dependencies"). (Same discipline as
  [`linear_combination`](./linear_combination.md)'s permutation non-law and
  [`dot`](../L1/dot.md) §Semantics.)

- **Cauchy–Schwarz strictness in floating point.** `|inner_product x y|² ≤
  inner_product x x · inner_product y y` holds mathematically but can fail by ULP-level
  amounts due to summation ordering; orthogonalization heuristics that depend on it
  tightly must guard. (From [`dot`](../L1/dot.md) non-laws.)

- **Positive-definiteness of `tdot`.** The unconjugated bilinear member is **not** PSD:
  `tdot x x ∈ ℂ` in general, and `tdot x x = 0` does not imply `x = 0` (e.g.
  `x = (1, i)` gives `1·1 + i·i = 0`). Law 5 is a Hermitian-member law only. (From
  [`dot`](../L1/dot.md) law 13.)

- **Subsumption of `linear_combination`.** No fold-merge law: `inner_product` and
  `linear_combination` fold over different axes into different result types — see
  § "Sibling fold". No bridge identity is claimed.

## tdot — the unconjugated member (type-API-surface only)

`tdot` is the unconjugated-bilinear value of the conjugation axis: kernel
`x[i] · y[i]` (no conjugation), realized at L0 by
`ComplexVector::TransposeDot` (`palace/linalg/vector.cpp:269-274`), which differs from
`Dot` only in the sign of the imaginary cross-terms. It is co-defined with `dot` at
[`dot`](../L1/dot.md) (a firm L1 operator) and is a legitimate axis value of this family
(the unconjugated bilinear form Palace exposes for algorithms that require it).

**Evidentiary caveat (not a status reduction).** `TransposeDot` has **zero call sites**
in the Palace tree — `search_text TransposeDot` over `palace/**` returns exactly the
declaration (`palace/linalg/vector.hpp:112`) and the definition
(`palace/linalg/vector.cpp:269`), no callers. Its evidentiary weight as a family member
is **type-API-surface-only**, not behavioral. The firm-up therefore leans its positive
behavioral anchors on `dot` (Hermitian — numerous CG/orthogonalization/NLEPS call sites)
and the M-weighted `bilinear-form` (Poynting-power and cross-coupling call sites), both
of which are exercised; `tdot` is carried as the complete-the-conjugation-axis member
with this caveat recorded (the same posture as `bilinear-form`'s narrow-coverage note).
This caveat is at the **member** granularity and does not gate the entry's `firm` status:
the *fold structure* is firm (the conjugation axis is one of three, and the other two are
exercised), and `tdot` is a defined kernel differing from `dot` by one sign — the
structural claim it is a family member is firm; only its *behavioral* weight is API-only.

## Dependencies

- L1 leaves it fuses up from (recovered as family-axis specializations):
  [`dot`](../L1/dot.md) (the Hermitian / symmetric member, and `tdot` the unconjugated
  member, co-defined there), [`bilinear-form`](../L1/bilinear-form.md) (the M-weighted
  member). These stay firm/rough-in L1 leaves — `inner_product` is the form they fuse up
  into, not a replacement.
- L2-composition (weighted member): [`apply_linop`](../L1/apply_linop.md) — `M` applied
  to the linear (arg-1) operand before the plain fold (`inner_product_M x M y =
  inner_product (apply_linop M x) y`).
- Concepts: [`dot`](../concepts/dot.md) — the cross-cutting prose / BLAS-1-heritage
  framing for the inner-product reduction; the element-type axis (`real`/`complex`) is
  carried there.
- Sibling fold (do **NOT** merge): [`linear_combination`](./linear_combination.md)
  (reduce-to-`Tensor[N]`) — see § "Sibling fold".
- L2>L1 lowering theme (forthcoming; abstractor work — cycle-019 dispatch #2, not
  authored here): `inner-product-fold-specialization` will narrate how the L2 fold lowers
  into the L1 leaves (conjugation/weight dispatch: Hermitian → `dot`, unconjugated →
  `tdot`, weighted → `bilinear-form`; element-type → real Hypre kernel vs complex
  four-real-dot lift), where the value-level conjugation re-order (`xᴴ y` ↔ `yᴴ x`)
  reappears, and which L0 reduction tree each lowered call pins (the load-bearing content
  of the IEEE non-law). Forward-reference only — that chapter exists as a stub.

## Variant axes

`inner_product` has the following variant axes; the **conjugation-convention** axis is
the one this operator unifies (it is NOT a remaining variant — it is the unification
axis), so the remaining axes are orthogonal to it:

1. **Conjugation convention** — `kernel = conj(x[i])·y[i]` (Hermitian `dot`) vs
   `kernel = x[i]·y[i]` (unconjugated `tdot`). The ONLY per-element difference between
   `Dot` (`palace/linalg/vector.cpp:263-267`) and `TransposeDot`
   (`palace/linalg/vector.cpp:269-274`) is the sign of the imaginary cross-terms. This is
   the unification axis (the family's namesake); `tdot` is its second value, carried with
   the zero-call-site caveat above.
2. **Element-type** — `real | complex`. At L0 these are separate kernels (real via a
   single Hypre `hypre_SeqVectorInnerProd`, `palace/linalg/vector.cpp:664-672`; complex
   via four real local dots lifted into `(Re, Im)`, `palace/linalg/vector.cpp:674-685`).
   At L2 one fold parameterized by element type; the complex fold is the real fold lifted
   componentwise. (Concept-page sibling axis to `linear_combination`'s `scalar-promotion`;
   carried at [`dot`](../concepts/dot.md).)
3. **Weight presence** — `M = I` (plain `inner_product`) vs general / SPD `M` pre-applied
   to arg-1 (`inner_product_M`, the [`bilinear-form`](../L1/bilinear-form.md) member). At
   L0: `linalg::Dot(comm,x,y)` vs `linalg::Dot(comm,x,A,y)`
   (`palace/linalg/operator.cpp:621-638`). Orthogonal to conjugation: the weighted member
   is itself conjugate-linear in its (M-applied) arg-1.

**Diagonal degeneration (`y = x`) is NOT a variant axis — it is a consumer entry point.**
`y = x` collapses the fold to the norm-squared (consumed by `nrm2` /
`matrix-weighted-norm`, which compose a `√` post-step) and triggers the `&x == &y`
self-inner-product fast path (transparent trick, `palace/linalg/vector.cpp:266,272-273`).
The fast path is an L0 implementation detail, NOT an L2 axis.

**Reduction tree (an L0 implementation detail, NOT an L2 variant axis)**: the pinned
Hypre per-rank kernel + MPI tree-reduce vs any other valid tree — transparent for value,
load-bearing for bit-reproduction (the IEEE non-law). Recorded in the lowering theme, not
as an L2 axis.

## Fusion note

The fused reduction kernels — the single Hypre `hypre_SeqVectorInnerProd` strided pass
(`palace/linalg/vector.cpp:664-672`, real) and the four-real-local-dot composition into a
`(Re, Im)` scalar (`palace/linalg/vector.cpp:674-685`, complex), plus the
local-then-collective two-step `LocalDot ∘ Mpi::GlobalSum`
(`palace/linalg/vector.hpp:247-253`) — are the **transparent-performance-trick
implementation** of the fold: a strided per-element-kernel pass followed by a pinned-tree
sum, rather than the unfused seed-then-accumulate chain. They compute the same value as
the unfused fold modulo IEEE-754 summation order (the load-bearing reduction-tree
non-law). The precondition for the strided pass is exactly the signature's shape
precondition (`x`, `y` share the length axis `N` — Palace's
`MFEM_ASSERT(x.Size() == y.Size())` at `palace/linalg/vector.cpp:667`). L2 de-fuses the
fused reduction into the fold's seed-and-accumulate and records the fusion as this one
note.

## Sibling fold: linear_combination is not subsumed

[`linear_combination`](./linear_combination.md)`:: [(Scalar, Tensor[N])] -> Tensor[N]` is
a **different** fold — `foldl (\acc (a,t) -> acc + a·t) zeros pairs` — a **reduce-to-
tensor** scalar-weighted sum, NOT a reduce-to-scalar inner product. The boundary
(the same one `linear_combination` draws from its side):

- **Different result type**: `inner_product :: … -> Scalar`;
  `linear_combination :: … -> Tensor[N]`.
- **Different combining step**: `inner_product`'s step is
  `acc_scalar + kernel(x[i], y[i])` (**collapses** the length axis `N`);
  `linear_combination`'s step is `acc_vec + a·t` (**preserves** the length axis,
  accumulates over the *term* axis).
- **Different unifying homomorphism**: `inner_product`'s is
  **`(length-concat, ++) → (Scalar, +)`** (collapses `N`); `linear_combination`'s is
  **`(term-list-concat, ++) → (Tensor[N], +)`** (collapses the term list, keeps `N`).
  They fold over **different axes**.
- **Different laws**: `inner_product` has Hermitian symmetry + PSD-at-diagonal (laws 4–5),
  which have no analogue for `linear_combination`; `linear_combination` has multilinearity
  in the scalar list, which has no analogue here.

The target is a small **algebra of folds** — a scalar-producing inner-product fold AND a
tensor-producing linear-combination fold — not one mega-combinator. They are deliberately
NOT merged. (`linear_combination` records the reciprocal boundary at
[`linear_combination`](./linear_combination.md) §"Sibling fold: dot is not subsumed".)

## Consumer (NOT an instance): nrm2 / matrix-weighted-norm

`nrm2` and `matrix-weighted-norm` are `√ ∘ inner_product` at the diagonal (`y = x`), NOT
fold members:

- `nrm2(x) = √ inner_product x x` — `palace/linalg/vector.hpp:256-260`
  (`Norml2(comm, x) = √|Dot(comm, x, x)|`).
- `matrix-weighted-norm(x, B) = √ inner_product_M x B x` for SPD `B` —
  `palace/linalg/operator.cpp:598-617` (`Norml2(comm, x, B, Bx) = √ Dot(comm, Bx, x)`,
  with the SPD-realness assertion confirming law 5).

The `√` post-step is a downstream composition; the norm is not a fold and does not enter
this entry's signature. (Law 5 — PSD at the diagonal — is exactly the property that makes
the square-root well-defined; this is the family's downstream closure, recorded to show
the boundary, not to claim subsumption.)

## Status

`firm` — the structure is a reduce-to-scalar fold over three firm/rough-in L1 leaves
(`dot`, `tdot`, `bilinear-form`); the signature is the conjugation-convention-axis
unification (the structural sibling of the arity-axis unification carried by
`linear_combination`); the conjugation convention is pinned (arg-1 conjugated, matching
both L1 leaves) and reconciled against the Palace `yᴴ x` source as the deliberate,
self-consistent L1 re-order. Every algebraic law is either the defining fold law
(empty-axis seed, length-concatenation-homomorphism) or a standard sesquilinear/bilinear
fact (sesquilinearity, Hermitian symmetry, PSD-at-diagonal, zero-argument), with the
PSD-at-diagonal directly confirmed by the in-source `&x==&y` imag=0 elision
(`palace/linalg/vector.cpp:266,679`) and the SPD-realness assertion
(`palace/linalg/operator.cpp:615-616`, comment "For SPD B, xᴴ B x is real" at `:611`);
the reduction-tree associativity is paired as the
explicit IEEE non-law per the load-bearing-numerical-trick discipline. The
combinator-miner same-shape rough-in cleared the ≥3-instance bar (dot + tdot +
bilinear-form), and the parametric-family mode independently characterized the cohort
(combinator-miner:2026-05-29T023000Z) with the fold-law membership test + axis taxonomy.

> **Member-level caveat (not a status reduction).** `tdot` is carried as the unconjugated
> conjugation-axis value with a **type-API-surface-only** evidentiary note: it has zero
> Palace call sites (declaration + definition only). The fold *structure* is firm and the
> other two axis values (`dot`, weighted) are behaviorally exercised; only `tdot`'s
> behavioral weight is API-only. See § "tdot".
>
> **Empirical-match caveat (not a status reduction).** The real-vector inner product has a
> direct unit test (`test/unit/test-vector.cpp:206-207`: `double dot = vec1 * vec2;
> CHECK_THAT(dot, WithinRel(32.0))` for `1·4+2·5+3·6=32`). The complex/Hermitian and
> M-weighted members have no dedicated value-asserting unit test; they are grounded by
> direct source-transcription (the `Dot`/`TransposeDot`/`LocalDot` kernels, the weighted
> free-function, the SPD-realness assertion) plus the verified live call sites
> (CG coefficients `iterative.cpp:395`; NLEPS norms `nleps.cpp:487,492`; Poynting power +
> cross-coupling `boundarymodeoperator.cpp:85,90`). The firm-without-full-test bar follows
> the [`chebyshev-iteration`](./chebyshev-iteration.md) /
> [`linear_combination`](./linear_combination.md) precedent (source-transcription
> confidence + integration coverage).

## L2 vs L1 distinction

- **L1**: `dot`/`tdot` at one chapter (the conjugation axis below L1 resolution is the
  per-element kernel; the two are distinct operators because their laws differ — `dot` is
  PSD-at-diagonal, `tdot` is not) plus the separate `bilinear-form` chapter (the M-weighted
  reduction); each mirrors Palace's L0 reduction surface. The conjugation and weight axes
  are fixed per L1 operator.
- **L2**: one fold `inner_product` over `(Tensor[N], Tensor[N])` with an optional pre-
  `apply_linop M`; the conjugation value, element type, and weight presence are recovered
  as specializations; the family of fused reduction kernels (a kernel-fusion choice) is
  unfolded into the canonical `foldl (+) zero (zipWith kernel x y)`; the pinned reduction
  tree is de-fused into the fold's seed-and-accumulate (the fusion note). The
  conjugation-convention axis — over which L1 has `dot`/`tdot` — is the axis this single
  L2 operator unifies.

## Evidence

- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body: `Re = Re(x)Re(y)+Im(x)Im(y)`,
  `Im = Im(x)Re(y)−Re(x)Im(y)` (with `this==&y` imag=0 fast path) = `x·conj(y) = yᴴ x`.
  The Hermitian kernel + the arg-2-conjugated Palace convention. **Self-verified via
  `read_range`.**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: same real part,
  **negated** imaginary cross-term (with `this==&y` returning `2·Im·Re`). The unconjugated
  `tdot` kernel — differs from `Dot` only in the imag sign. **Self-verified.**
- `palace/linalg/vector.cpp:664-672` — `LocalDot(Vector, Vector)` via a single Hypre
  `hypre_SeqVectorInnerProd`, with `MFEM_ASSERT(x.Size()==y.Size())` at `:667`. The real
  member's fused kernel + the shape precondition. **Self-verified.**
- `palace/linalg/vector.cpp:674-685` — `LocalDot(ComplexVector, ComplexVector)`: four real
  `LocalDot`s combined into `(Re, Im)`, with the `&x==&y` self-dot fast path returning
  imag=0 at `:679`. The element-type axis (complex = real fold lifted) + law-5 confirmation.
  **Self-verified.**
- `palace/linalg/vector.hpp:109` — `ComplexVector::Dot` decl, comment
  `// Vector dot product (yᴴ x) or indefinite dot product (yᵀ x)`. The documented arg-2
  conjugation convention. **Self-verified.**
- `palace/linalg/vector.hpp:112` — `TransposeDot` declaration (the only declaration; zero
  callers). **Self-verified.**
- `palace/linalg/vector.hpp:242,246` — `LocalDot` / `Dot` free-function comments
  `// Calculate the … inner product yᴴ x or yᵀ x`. **Self-verified.**
- `palace/linalg/vector.hpp:247-253` — `Dot(comm, x, y) = Mpi::GlobalSum ∘ LocalDot`
  template (the reduction's local-then-collective two-step). **Self-verified.**
- `palace/linalg/operator.cpp:621-628` — `Dot(comm, x, A, y)` (real `Operator` weight):
  builds `Ax = A·x` then `Dot(comm, Ax, y) = yᴴ A x`. The M-weighted member; the weight axis
  + the M-applied-operand conjugation. **Self-verified.**
- `palace/linalg/operator.cpp:631-638` — `Dot(comm, x, A, y)` (`ComplexOperator` weight),
  the element-type-of-weight sibling overload. **Self-verified.**
- `palace/linalg/operator.cpp:598-617` — `Norml2(comm, x, B, Bx)` real + complex: the
  B-weighted norm `√ Dot(comm, Bx, x)`, with the SPD-realness assertion
  (`dot.real() > 0 && |dot.imag()| < 1e-9·dot.real()`) at `:615-616` and the comment
  "For SPD B, xᴴ B x is real" at `:611`. The `matrix-weighted-norm` consumer +
  law-5 confirmation. **Self-verified.**
- `palace/linalg/operator.hpp:386,391` — the two weighted `Dot(comm, x, A, y)` declarations,
  comment `// Compute the bilinear form inner product yᴴ A x`. **Self-verified.**
- `palace/linalg/iterative.cpp:395` — `beta = linalg::Dot(comm, z, r)`: CG's
  preconditioned `(Br, r)` coefficient, the workhorse live call site of the Hermitian
  member. **Self-verified.**
- `palace/linalg/nleps.cpp:487,492` — `std::sqrt(std::abs(linalg::Dot(GetComm(), c, c)) …)`
  and the `v,v` line: NLEPS normalization, live `inner_product`-at-diagonal sites
  confirming the complex form returns complex. **Self-verified.**
- `palace/models/boundarymodeoperator.cpp:85` — `linalg::Dot(comm, et, *Bttr, et)`: Poynting
  power (M-weighted, diagonal `y=x`); `:90` — `linalg::Dot(comm, en, Atn, et)`: cross-coupling
  (M-weighted, off-diagonal). The two live M-weighted call sites. **Self-verified.**
- `test/unit/test-vector.cpp:206-207` — real-vector dot `double dot = vec1 * vec2;
  CHECK_THAT(dot, WithinRel(32.0))` (`1·4+2·5+3·6=32`). Direct value-asserting test for the
  real member. **Self-verified.**
- Artifact cross-references (read this invocation): `book/src/L1/dot.md` (the `dot`/`tdot`
  leaves + arg-1-conjugated L1 convention at `:34,:43`), `book/src/L1/bilinear-form.md`
  (the M-weighted leaf, `xᴴ M y` at `:19,:63`, conjugation-anchor resolution at `:50-53`),
  `book/src/L2/linear_combination.md` (the sibling fold + harvest-format precedent),
  `book/src/L2/index.md` (the dep-map row being flipped),
  `book/src/L2/chebyshev-iteration.md` (firm-without-full-test precedent).
- Provenance: combinator-miner:2026-05-28T231046Z (cycle-018 same-shape rough-in row);
  combinator-miner:2026-05-29T023000Z
  (`reports/2026-05-29T023000Z-combinator-miner-parametric-family/CYCLE.md` — parametric-
  family mode characterization: fold-law membership test, four-axis taxonomy, the
  conjugation-convention contradiction + `tdot`-uncalled caveats this entry resolves).

---

## Supporting evidence

Self-verification log (every Palace range read this invocation via
`mcp__palace-codemap__read_range` / `search_text`, confirming the cited construct sits on
the asserted line):

- `vector.cpp:263-274` — `ComplexVector::Dot` (`:263-267`) and `TransposeDot` (`:269-274`)
  bodies; the imag-cross-term sign distinguishes them; `Dot` body = `x·conj(y) = yᴴ x`
  (Palace arg-2-conjugated). Confirmed.
- `vector.cpp:664-685` — `LocalDot(Vector)` (`:664-672`, single Hypre InnerProd,
  `MFEM_ASSERT` at `:667`) and `LocalDot(ComplexVector)` (`:674-685`, four-real-dot lift,
  self-dot imag=0 at `:679`). Confirmed.
- `vector.cpp:700-712` — `AXPY` (read for context on the surrounding free-function block;
  not cited in-entry). Confirmed adjacent.
- `vector.hpp:105-120` — `Dot`/`TransposeDot`/`operator*` decls + `yᴴ x` comment at `:109`,
  `TransposeDot` decl at `:112`. Confirmed.
- `vector.hpp:240-262` — `LocalDot` decls + `yᴴ x` comment (`:242`), free-function `Dot`
  (`:246-253`), `Norml2` (`:256-260`). Confirmed.
- `operator.cpp:598-617` — `Norml2(…, B, Bx)` real (`:598-606`) + complex (`:608-617`);
  "For SPD B" comment at `:611`, SPD-realness assertion `:615-616`. Confirmed.
- `operator.cpp:621-638` — weighted `Dot(comm, x, A, y)` real-`Operator` (`:621-628`) +
  `ComplexOperator` (`:631-638`) overloads. Confirmed.
- `operator.hpp:384-396` — weighted `Dot` decls + `yᴴ A x` comments (`:386,:391`). Confirmed.
- `boundarymodeoperator.cpp:82-92` — `linalg::Dot(comm, et, *Bttr, et)` at `:85`,
  `linalg::Dot(comm, en, Atn, et)` at `:90`. Confirmed (corrects the miner's `:85,:90` —
  both verified on-line).
- `iterative.cpp:393-406` — `beta = linalg::Dot(comm, z, r)` at `:395`. Confirmed.
- `nleps.cpp:485-493` — `std::abs(linalg::Dot(GetComm(), c, c))` at `:487`, `(v, v)` at
  `:492`. Confirmed.
- `test/unit/test-vector.cpp:204-212` — real dot test at `:206-207`. Confirmed (path is
  `test/unit/`, not `palace/test/unit/`).
- `search_text TransposeDot` over `palace/**` → exactly two hits (`vector.hpp:112` decl,
  `vector.cpp:269` def). Confirms zero call sites — caveat 2. Confirmed.

Conjugation reconciliation (caveat 1, the headline must-resolve):

- **Palace convention** = `Dot(comm, x, y) = yᴴ x` (arg-2 conjugated), consistent across
  doc strings (`vector.hpp:109,242,246`; `operator.hpp:386,391`) AND kernel bodies
  (`vector.cpp:263-267,674-685`; `operator.cpp:621-628`). There is **no Palace-internal
  contradiction** — I corrected the combinator-miner's framing: the contradiction is
  between Palace's `yᴴ x` and the L1 `dot.md` entry's `xᴴ y`, not within Palace.
- **L1/L2 representation convention** = `xᴴ y` (arg-1 conjugated), the deliberate L1
  mutation-rotation re-order recorded at `dot.md:34,43` and `bilinear-form.md:19,63`. Both
  L1 leaves already adopt it; `bilinear-form.md:50-53` independently verified the L0 source
  is self-consistent and retracted an earlier alleged-disagreement gating reason.
- **Decision**: the L2 `inner_product` entry **pins arg-1-conjugated** (`xᴴ y`,
  `xᴴ M y`) to stay consistent with both leaves it fuses up from; the value-level
  conjugation between Palace's `yᴴ x` and the representation's `xᴴ y` (they are complex
  conjugates) is documented in § "Conjugation convention (pinned)" and handed to the
  L2>L1 lowering theme to map onto the L0 call. This is internally consistent and does NOT
  require an `unclear` mark — the convention is cleanly pinned and the prior L1 precedent
  is unanimous.

## Open questions

- **`tdot` member status — carried `firm`-member with type-API-only behavioral weight.**
  Per the combinator-miner caveat 2, I kept `tdot` as a full conjugation-axis member
  (matching `dot.md`, which treats it as a co-defined firm operator) with the explicit
  zero-call-site caveat, rather than demoting it to a documented-but-not-instantiated axis
  value. The entry's overall status is `firm` (the fold structure + two exercised axis
  values), with `tdot`'s behavioral weight flagged at member granularity. If a later audit
  prefers the demote-to-axis-value posture, that is a member-level refinement, not an
  entry-level status change. Tracked under OQ `inner-product-fold-sibling-candidate` (can
  now be closed/migrated — the sibling fold is firm) and the `tdot`-coverage note shared
  with `bilinear-form`'s narrow-coverage OQ.
- **OQ `inner-product-harvester-formalization-and-conjugation-pinning` is resolved by this
  entry** (conjugation pinned arg-1; reconciliation documented; `tdot` flagged). Recommend
  the integrator close/migrate it. The sibling-candidate OQ
  `inner-product-fold-sibling-candidate` is likewise resolvable (the fold is now firm).
- **L2>L1 lowering theme is dispatch #2's job** (`inner-product-fold-specialization`,
  currently a stub). This entry forward-references it plain-text and hands it: (a) the
  conjugation/weight dispatch (Hermitian→`dot`, unconjugated→`tdot`, weighted→
  `bilinear-form`); (b) the element-type dispatch (real Hypre kernel vs complex
  four-real-dot lift); (c) the value-level conjugation re-order `xᴴ y ↔ yᴴ x` to map onto
  the L0 call; (d) which L0 reduction tree each lowered call pins (the IEEE non-law's
  load-bearing content). Not authored here per the layers-high→low discipline.
- **Weighted split-additivity is whole-vector general only.** Law 2 (split-additivity)
  holds elementwise/per-block for the plain/conjugate members; for `inner_product_M` the
  per-block split requires `M` block-diagonal w.r.t. the split. I stated the law at
  whole-vector granularity for the weighted member to avoid over-claiming a per-block
  tiling law (combinator-miner caveat 4). No further action needed; recorded in § "Algebraic
  laws" law 2 and § "Variant axes".
- **Layer-intro refresh (note for layer-intro-author, not actioned here):** the L2
  `index.md` §"Semantics (overlay)" primitive list (`axpy, dot, matvec, gemv, trsv, scal,
  nrm2`) predates the L2 fold cohort; once `inner_product` + `linear_combination` are both
  firm, the overlay could note the two reduce-to-X fold siblings as first-class L2 forms.
  Out of harvester scope.
- **`bilinear-form` is still rough-in at L1** (narrow variant-axis coverage). `inner_product`
  fuses it up as the M-weighted member but does not depend on its promotion — the M-weighted
  member's structure is firm at L2 (the composition `inner_product (apply_linop M x) y` is
  clean). The rough-in status of the L1 leaf does not gate the L2 entry's `firm` status (the
  L2 fold is firm in its decomposition; the leaf's coverage caveat lives at L1).
