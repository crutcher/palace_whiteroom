---
layer: L2
operator: inner_product
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/bilinear-form
    - L1/apply_linop
    - target: L2-L1/inner-product-fold-specialization
      kind: lowers-to             # UPGRADED from reference: faithful L2>L1 lowering theme edge (does NOT flip reachable yet — L2/inner_product is itself unreachable)
  reference:
    - L2/linear_combination
    - concepts/dot
---

# inner_product

**`inner_product` is the L2 entry for the reduce-to-scalar inner-product family**
— the combinator IS the inner product at this layer. The conjugation /
element-type / weight specializations Palace exposes — the Hermitian `dot`, the
unconjugated bilinear `tdot`, the matrix-weighted `xᴴ M y` (`inner_product_M`) — are
**specialization notes under this entry** (§"Specializations"), not separate
co-equal chapters: they are this one **reduce-to-scalar fold** over the shape group `S`
read at fixed axis-values. The fusion-rotation form: Palace's distinct reduction
call shapes (`ComplexVector::Dot` / `TransposeDot`, `linalg::LocalDot` over real and
complex, `linalg::Dot(comm,x,A,y)` for the weighted member — each a Hypre-kernel +
MPI-tree-reduce fusion choice) are unfolded into the canonical
`foldl (+) zero (zipWith kernel x y)`, with the pinned reduction tree de-fused into
the fold's seed-and-accumulate.

> **Vocabulary-shift redirect (2026-06-01) — combinator-as-entry inversion.** This
> entry was authored cycle-019 under the retired mine-and-strand regime, which stated
> `inner_product` was "the form they fuse *up* into, not a replacement" and stood it
> *beside* same-named L2 leaf chapters (`L2/dot`). Per the redirect (replace-and-
> propagate, not mine-and-strand; `METHODOLOGY-REDIRECT.md` §4-§5), the combinator is
> now the **layer's primary entry** and the members are specialization notes under it.
> The standalone `L2/dot.md` leaf-floor is collapsed into a §"Specializations" note
> (cycle-050 enactment — see combinator-miner refactor-pass report); the degenerate
> `L3-L2/dot-body-identity` + `L2-L1/dot-leaf-identity` identity-in-named-terms theme
> files were deleted at cycle-051, their identity-in-form content absorbed into the
> combinator homes (they were vocabulary-failed-to-shift smells, not translations). The
> combinator propagates **up** to a new `L3/inner_product` entry
> (cycle-050) through which the L3 leaf cohort re-expresses, rather than each L3 leaf
> re-deriving a base form. `nrm2` is **not** a member — it is a `√ ∘ abs ∘
> inner_product` **consumer** (§"Consumer (NOT an instance)").

## Context

At L1, the inner-product leaves mirror Palace's L0 reduction surface: `dot`/`tdot`
share [`dot`](../L1/dot.md) (the conjugation axis at one chapter), and the
M-weighted reduction is the separate leaf [`bilinear-form`](../L1/bilinear-form.md).
Those leaves stay firm at **L1** (the mutation-rotation layer, where each mirrors one
Palace L0 call surface one-to-one). **At L2, `inner_product` is the entry** — it does
not stand beside same-named L2 leaf chapters; the conjugation / weight specializations
are read off it at fixed axis-values (§"Specializations"). The L1→L2 step IS the
vocabulary shift the redirect calls for: L1's three separate call-shaped leaves become
one L2 fold parameterized by the conjugation/element-type/weight axes.

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
reduction over the shape group `S`, with no control-flow, no monadic state threading, and
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
inner_product   :: (x: Tensor[(S: ...)], y: Tensor[S]) -> Scalar
inner_product_M :: (x: Tensor[(S: ...)], M: LinOp[(S: ...), (S: ...)], y: Tensor[S]) -> Scalar

inner_product   x y   = foldl (+) zero (zipWith kernel x y)   -- kernel from the table below
inner_product_M x M y = inner_product (apply_linop M x) y     -- weighted ≡ pre-apply M to arg-1, then plain
inner_product   x y   = inner_product_M x I y                 -- plain ≡ M = I
```

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1):

- `x` — `Tensor[(S: ...)]` — read-only; the **conjugated** (arg-1) operand (see § "Conjugation
  convention (pinned)").
- `y` — `Tensor[S]` — read-only; the **linear** (arg-2) operand.
- `M` (weighted member) — `LinOp[(S: ...), (S: ...)]` — read-only; the matrix-weight (a
  square / endomorphic operator, domain ≡ range = `S`, §1.2.2), pre-applied to `x` (the
  linear-operator type is the opaque
  [`apply_linop`](../L1/apply_linop.md) interface). For the off-diagonal cross-coupling
  use the codomain of `M` matches the shape group `S` of `y`; the diagonal
  (`y = x`, SPD `M`) is the norm-squared consumed downstream.
- result — `Scalar` — element type per the rule below; `zero` (the additive identity of
  the scalar field) on the empty tensor.
- `x` and `y` share one shape group `S` (arbitrary unknown rank, NOT rank-1) and one element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes):

| element type | operator | per-element `kernel(x[idx], y[idx])` | form |
|---|---|---|---|
| `real`    | `inner_product` | `x[idx] · y[idx]`             | bilinear symmetric (conjugation is a no-op) |
| `complex` | `inner_product` | `conj(x[idx]) · y[idx]`      | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot`          | `x[idx] · y[idx]`            | unconjugated bilinear (see § "tdot") |

## Specializations (the members, as notes under the combinator)

The members are **not separate L2 chapters** — they are this fold read at fixed
axis-values. Each row is the combinator with one axis pinned; there is no co-equal
`L2/dot` / `L2/bilinear-form` floor beside this entry (the standalone `L2/dot.md` is
collapsed into this note per the 2026-06-01 redirect; `bilinear-form` never had a
standalone L2 chapter — it lives only as the L1 leaf and as the weighted member here):

```text
dot(x, y)              = inner_product x y                          -- Hermitian (complex) / symmetric (real); conjugated kernel, M = I
tdot(x, y)             = inner_product x y  with unconjugated kernel -- complex-only specialization, see § "tdot"
bilinear_form(x, M, y) = inner_product_M x M y                      -- M-weighted member: weight axis = general M
```

- **`dot`** — the conjugation axis at value *Hermitian* (complex) / *symmetric* (real),
  with `M = I`. This is the workhorse specialization (CG coefficients, orthogonalization,
  NLEPS). Its L1 leaf [`dot`](../L1/dot.md) stays firm; at L2 there is no separate `dot`
  entry — it is this note.
- **`tdot`** — the conjugation axis at value *unconjugated bilinear* (complex-only). Co-
  defined with `dot` at L1; carried here with the type-API-surface-only caveat (§"tdot").
- **`bilinear_form`** — the weight axis at value *general / SPD `M`* (`inner_product_M`),
  realized as the pre-application `inner_product (apply_linop M x) y`. Its L1 leaf is
  [`bilinear-form`](../L1/bilinear-form.md) (firm, promoted cycle-095).

The L2 entry differs from the L1 leaves in **resolution**, along the
conjugation-convention / weight-presence axes: L1 sees `dot`/`tdot` (the conjugation
axis at one chapter) and `bilinear-form` (the separate M-weighted chapter); L2 sees one
fold whose `kernel` and optional pre-`apply_linop M` recover each member as a note. The
element-type sub-axis is identical to the leaves' (inherited, not re-derived).

## Semantics

`inner_product` reduces the two tensors to a scalar: starting from the additive identity
`zero`, it folds the per-element products `kernel(x[idx], y[idx])` over the shape group `S`.
The result is `Σ_idx kernel(x[idx], y[idx])` over every position `idx` of `S` — the (Hermitian / bilinear / M-weighted) inner product
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

The fold **reduces over the shape group `S`** and therefore carries an **MPI collective**
in the L0 realization (`LocalDot` ∘ `Mpi::GlobalSum`, `palace/linalg/vector.hpp:247-253`).
The collective is **not** in the L2 signature (single-rank scope; ranks read as their
single-rank equivalents). This is the structural opposite of
[`linear_combination`](./linear_combination.md), which is element-local over `S` and folds
over the *term list* (no collective) — see § "Sibling fold".

The self-inner-product fast path `&x == &y` (`palace/linalg/vector.cpp:266` returning
imaginary part `0.0` for the Hermitian form; `:272-273` returning `2·Im·Re` for `tdot`)
is a transparent performance trick at L2 — algebraically `xᴴ x` is exactly real, so
eliding the cancellation is equivalent. It disappears in the L2>L1 lowering.

## Algebraic laws

The laws below hold; absences are deliberate.

**Defining fold law (this is what makes the cohort one family):**

1. **Empty-tensor identity (the fold's seed).** `inner_product` over an empty tensor is
   `zero` (the additive identity of the scalar field) — the fold's initial accumulator.

2. **Split-additivity / shape-concatenation-homomorphism (the defining law).**
   `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`,
   where `++` concatenates the shape group `S` and `+` is scalar addition. The fold is
   a **monoid homomorphism from `(shape-concatenated tensors, ++)` to `(Scalar, +)`** —
   it collapses the shape group `S`. This is the inner-product analogue of
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
`x[idx] · y[idx]` (no conjugation), realized at L0 by
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

- L1 leaves the specializations rest on (each member is this fold at a fixed axis-value —
  see §"Specializations"): [`dot`](../L1/dot.md) (the Hermitian / symmetric member, and
  `tdot` the unconjugated member, co-defined there), [`bilinear-form`](../L1/bilinear-form.md)
  (the M-weighted member). These stay firm/rough-in **L1** leaves (the mutation-rotation
  layer, one per Palace L0 call surface); at **L2** `inner_product` is the single entry and
  they are specialization notes under it — there is no separate same-named L2 leaf chapter.
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

1. **Conjugation convention** — `kernel = conj(x[idx])·y[idx]` (Hermitian `dot`) vs
   `kernel = x[idx]·y[idx]` (unconjugated `tdot`). The ONLY per-element difference between
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
precondition (`x`, `y` share the shape group `S` — Palace's
`MFEM_ASSERT(x.Size() == y.Size())` at `palace/linalg/vector.cpp:668`). L2 de-fuses the
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
  `acc_scalar + kernel(x[idx], y[idx])` (**collapses** the shape group `S`);
  `linear_combination`'s step is `acc_vec + a·t` (**preserves** the shape group,
  accumulates over the *term* axis).
- **Different unifying homomorphism**: `inner_product`'s is
  **`(shape-concat, ++) → (Scalar, +)`** (collapses `S`); `linear_combination`'s is
  **`(term-list-concat, ++) → (Tensor[N], +)`** (collapses the term list, keeps `N`).
  They fold over **different axes**.
- **Different laws**: `inner_product` has Hermitian symmetry + PSD-at-diagonal (laws 4–5),
  which have no analogue for `linear_combination`; `linear_combination` has multilinearity
  in the scalar list, which has no analogue here.

The target is a small **algebra of fold combinators** — a scalar-producing inner-product
combinator (this entry) AND a tensor-producing linear-combination combinator (the D1
sibling entry) — each the **primary L2 entry for its family**, not one mega-combinator and
not a leaf-floor lattice. They are deliberately NOT merged. (`linear_combination` records
the reciprocal boundary at its own §"Sibling fold: dot is not subsumed" — that entry is
D1's refactor scope this batch; this note is the `inner_product`-side half of the
two-combinator boundary and is edited here only.)

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
(empty-tensor seed, shape-concatenation-homomorphism) or a standard sesquilinear/bilinear
fact (sesquilinearity, Hermitian symmetry, PSD-at-diagonal, zero-argument), with the
PSD-at-diagonal directly confirmed by the in-source `&x==&y` imag=0 elision
(`palace/linalg/vector.cpp:266,679`) and the SPD-realness assertion
(`palace/linalg/operator.cpp:615-616`, comment "For SPD B, xᴴ B x is real" at `:611`);
the reduction-tree associativity is paired as the
explicit IEEE non-law per the load-bearing-numerical-trick discipline. The
combinator-miner same-shape rough-in cleared the ≥3-instance bar (dot + tdot +
bilinear-form), and the parametric-family mode independently characterized the cohort
(combinator-miner:2026-05-29T023000Z) with the fold-law membership test + axis taxonomy.

**Combinator-as-entry inversion (combinator-miner refactor-pass, cycle-049, D2).** Under
the 2026-06-01 vocabulary-shift redirect this entry was inverted from mine-and-strand
(combinator beside same-named L2 leaf chapters) to **combinator-as-entry**: the lede,
§Context, §"Specializations" (formerly the §Signature "recovered as specializations"
block), and §Dependencies now state the combinator IS the L2 inner-product entry and the
members (`dot`/`tdot`/`bilinear_form`) are specialization notes under it. The standalone
`L2/dot.md` leaf-floor collapse + the `L3/inner_product` upward propagation are the
cycle-050 enactment (mapped in the refactor-pass report); the
`L3-L2/dot-body-identity` / `L2-L1/dot-leaf-identity` smell-theme files were deleted at
cycle-051 (their identity-in-form content absorbed into the combinator homes). The combinator's own substantive
lowering [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
is a GENUINE translation (conjugation/element-type/weight dispatch + the value-level
`xᴴ y` ↔ `yᴴ x` re-order) and is KEPT (re-audited cycle-049, D2).

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
- **L2**: one fold `inner_product` over `(Tensor[(S: ...)], Tensor[S])` with an optional pre-
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
