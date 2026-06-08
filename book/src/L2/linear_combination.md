---
layer: L2
operator: linear_combination
rank: firm
edges:
  depends-on:
    - L1/scal
    - L1/axpy
    - L1/axpby
    - L1/axpbypcz
    - target: L2-L1/linear-combination-fold-specialization
      kind: lowers-to             # UPGRADED from reference: the L2>L1 lowering theme this variadic fold lowers through (reachability-bearing)
  reference:
    - concepts/scalar-promotion
    - L2/inner_product
---

# linear_combination

The arity-family unification of the BLAS-1 scalar-weighted-vector-sum cohort:
the four L1 fixed-arity leaves [`scal`](../L1/scal.md), [`axpy`](../L1/axpy.md),
[`axpby`](../L1/axpby.md), [`axpbypcz`](../L1/axpbypcz.md) are the arity-1/2/2/3
specializations of a single variadic **fold** over a list of (scalar, tensor)
terms. The fusion-rotation form: Palace's distinct fixed-arity call shapes
(`operator*=` / `AXPY` / `AXPBY` / `AXPBYPCZ`, each a one-aligned-pass kernel-fusion
choice over its operands) are unfolded into the canonical multi-term linear
combination, with the single aligned pass de-fused into the fold's seed-and-accumulate.

## Context

At L1, the four scalar-weighted-sum leaves mirror Palace's distinct L0 C++ symbols
one-to-one — that one-to-one shape is load-bearing for the L1>L0 mutation rotation,
which rewrites *each fixed-arity symbol* into its receiver-mutating / output-arg
idiom. The `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps the fused scalar-vector update whole at L1 (fuse, don't decompose) — that decision
governs the L1>L0 mutation rotation, where each fixed-arity symbol mirrors one L0 C++ call
one-to-one. **At L2, `linear_combination` is the entry for this family** (vocabulary-shift
redirect 2026-06-01, `CLAUDE.md` §Methodology invariants): the four arity forms `scal` /
`axpy` / `axpby` / `axpbypcz` are **specialization notes under the combinator** (§"Arity
specializations"), not standalone mirrored L2 chapters. Under the redirect, a same-named
base-form floor mirrored beside the combinator is the retired rectangular pattern. The L1
leaves remain firm (the L1>L0 one-to-one shape is load-bearing there); what changes is L2's
*entry* — the family speaks through the combinator at L2 and above.

L2 is exactly the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion
across multiple algebraic operations is unfolded into composition… Batched specialized
BLAS calls are written as compositions of base primitives." Palace's choice to expose
four distinct fixed-arity entry points (rather than one variadic one) is a
kernel-fusion / call-shape choice — each entry point fuses its 1/2/3 scalar-vector
products into a single aligned pass over the operands. Unfolding that family of
fixed-arity call shapes into the one variadic multi-term fold is precisely the L2
rotation along the **arity** axis — the structural sibling of the **element-type**
axis unified at the concept-page level by
[`concepts/scalar-promotion`](../concepts/scalar-promotion.md) (whose own closure
depends on the L1 calculus formally adopting the `real ⊑ complex` scalar lattice,
tracked under OQ `scalar-promotion-typing-rule` and not yet committed).

This is an L2 fold, not an L4 combinator: `linear_combination` is a pure
value-producing reduction over a term list, with no control-flow, no monadic state
threading, and no convergence predicate. It is data-parallel, not iteration-structural
(contrast L4 `iterate_while`, which threads state through a stopping predicate). It
belongs with the tensor algebra at L2.

The sibling reduction `dot` is a **different** fold — see § "Sibling fold: dot is not
subsumed".

## Signature

```text
linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]
linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs
```

Shape contract (bunsen-style; named shape groups per [`l4_calculus`](../semantics/index.md) §1.2.1):

- `pairs` — `[(Scalar, Tensor[(S: ...)])]` — a finite list of (coefficient, term) pairs.
  Order is the fold's evaluation order (see § "Algebraic laws", permutation
  law/non-law pair).
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary (unknown) rank; the combination
  is element-local at every position of `S`. This congruence is also the
  aligned-fusion-kernels precondition — every term shares the shape the
  single aligned pass strides over. (The general named-shape-group convention is in
  [`l4_calculus`](../semantics/index.md) §1.2.1, linked above.)
- each `aᵢ` — `Scalar` — element type one shared `T ∈ {real, complex}` across all
  scalars and all terms, with the `real ⊑ complex` scalar-promotion lattice inherited
  unchanged from [`concepts/scalar-promotion`](../concepts/scalar-promotion.md)
  (promote all-or-none across the scalar list).
- result — `Tensor[$S]` — same shape group `S`; `zeros[$S]` on the empty list.

### Arity specializations

The four arity forms are list-length specializations of the combinator — **specialization
notes, not standalone L2 chapters** (vocabulary-shift redirect). Each is the combinator at a
fixed term-list length:

```text
scal(α, x)                 = linear_combination [(α, x)]              -- arity 1
axpy(α, x, y)              = linear_combination [(α, x), (1, y)]      -- arity 2, second coeff fixed to 1
axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]      -- arity 2, general
axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)] -- arity 3
```

**Per-arity unique L0 surface** (the bounded-arity L0 call shapes each readout label names;
the combinator's generic free-function-surface anchors `vector.hpp:305-316` do not pinpoint
these at the per-arity resolution):

| Arity | Readout | Unique L0 anchors (paths relative to `reference/palace/`) |
|---|---|---|
| 1 | `scal(α,x)` | `linalg/vector.hpp:98-99` (`ComplexVector::operator*=` decl, "Scale all entries by s."); `linalg/vector.cpp:203-227` (`operator*=` def) incl. `:207-211` (`si==0.0` real fast-path / scalar-promotion site); `linalg/vector.hpp:262-270` (`linalg::Normalize` fused `nrm2+scal` consumer). Receiver-mutating `*=` member idiom — the only family member NOT a free function. |
| 2 (coeff-1) | `axpy(α,x,y)` | `linalg/vector.hpp:115-118` (`ComplexVector::AXPY` + `Add`/`Subtract` aliases decl); `linalg/vector.cpp:276-311` (`ComplexVector::AXPY` def + element-wise kernels); `linalg/vector.cpp:714-718` (real-α-on-complex forwarding overload — scalar-promotion sub-axis); `linalg/vector.cpp:720-724` (complex-α overload → member `ComplexVector::AXPY`). |
| 2 (general) | `axpby(α,x,β,y)` | `linalg/vector.hpp:130-131` (`ComplexVector::AXPBY` member decl, receiver-mutating); `linalg/vector.cpp:732-737` (complex-complex specialisation → member); `linalg/vector.cpp:739-743` (real-scalar-on-complex promotion site). |
| 3 | `axpbypcz(α,x,β,y,γ,z)` | `linalg/vector.hpp:133-136` (`ComplexVector::AXPBYPCZ` member decl); `linalg/vector.cpp:745-758` (real-real, incl. the `γ==0` arity-collapse fast-path `:749-751` → `add(α,x,β,y,z)` — the exact algebraic content of law 5, and the `γ≠0` split `:755-756`); `linalg/vector.cpp:760-765` (complex-complex → member); `linalg/vector.cpp:767-772` (real-scalar-on-complex promotion site). |

These names remain useful as *readout labels* for the bounded-arity L0 call shapes (the
L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
fusion-selection theme picks the maximal fused L0 leaf per list-length). They are NOT
separate L2 operators with their own algebra — every law below is the combinator's; the
per-arity facts (`axpby` bilinearity, `axpbypcz` trilinearity, etc.) are the multilinearity
law (law 3) read at a fixed list length. The L1 leaf chapters (`book/src/L1/{scal,axpy,axpby,axpbypcz}.md`)
stay firm — they carry the L1>L0 one-to-one symbol shape; the *L2* family entry is this
combinator.

The L2 form differs from the L1 leaves in **resolution**, along the arity axis: L1
sees four distinct fixed-arity operators (mirroring Palace's four L0 symbols); L2 sees
one variadic fold whose list length recovers each fixed arity. The element-type /
scalar-promotion sub-axis is identical to the L1 leaves' (inherited, not re-derived).

## Semantics

`linear_combination` accumulates a running tensor sum: starting from the zero tensor
of shape group `S`, it folds left over the term list, adding each scaled term `aᵢ·tᵢ` into
the accumulator. The result is the tensor `Σᵢ aᵢ·tᵢ` (the linear combination of the
terms with the paired coefficients).

It is **pure / out-of-place** at L2: it consumes the coefficient/term list and produces
a fresh tensor; no destination buffer appears in the signature. The L0 in-place idioms
(the receiver-mutating / output-arg forms where one term's tensor aliases the output
buffer) are an L2>L1 (and onward L1>L0) lowering concern, captured by the
output-aliasing variant axis below — not by the L2 algebra.

Each accumulate step is element-local and reduction-free over `S` (every
output position `result[idx] = Σⱼ aⱼ·tⱼ[idx]` for every multi-index `idx` of `S`
depends only on position `idx` of each term).
The fold's sequencing is over the **term list**, not over `S` — there is no
cross-element communication and no MPI collective (terms are rank-local; ranks own
disjoint slices of `S`). Contrast `dot` / `nrm2`, which reduce over `S` and do carry an
MPI collective.

Palace's L0 surface stops at arity 3 (`AXPBYPCZ`; there is no `AXPBYPCZPDW`).
Combinations of more than three terms are realized in Palace as **iterated**
`axpbypcz`-into-output with the aliased coefficient fixed to 1 (the `γ=1` accumulation
sites — `nleps.cpp:343-344`, `romoperator.cpp:188-189` — accumulate two more terms per
loop step into the running sum). The variadic `linear_combination` is therefore the L2
abstraction that the bounded-arity L0 family approximates; per CLAUDE.md
("the literature-anchored / higher form may inform extensions Palace hasn't implemented"),
the variadic form may later let an L4 combinator express n-term
basis-reconstruction (ROM / eigenvector synthesis) directly, which Palace open-codes as
accumulation loops. This is the correct generalization direction, not scope creep.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Empty-list identity (the fold's seed).** `linear_combination [] = zeros[$S]` —
   the additive identity of `Tensor[$S]`. This is the fold's initial accumulator.

2. **Concatenation-homomorphism (the defining law).**
   `linear_combination (a ++ b) = linear_combination a + linear_combination b`,
   where `+` on the right is element-wise tensor addition. **This is the law that
   makes the four arities one operator**: `axpbypcz`'s 3-term list is the
   concatenation of an `axpby` 2-term list and a `scal` 1-term list, so
   `linear_combination [(α,x),(β,y),(γ,z)] = linear_combination [(α,x),(β,y)] +
   linear_combination [(γ,z)]` = `axpby(α,x,β,y) + scal(γ,z)`. It is a monoid
   homomorphism from `([(Scalar,Tensor[(S: ...)])], ++, [])` to `(Tensor[$S], +, zeros)`,
   and it directly generalizes the per-operator distribution laws already recorded
   (axpby.md laws 6–7; axpbypcz.md laws 8–10).

3. **Multilinearity in the scalar list.** `linear_combination` is linear separately
   in each coefficient `aᵢ` with all other terms held fixed:
   `linear_combination ((a₁+a₂, t):rest) = a₁·t + a₂·t + linear_combination rest`,
   and (combined with law 2) `linear_combination` is a multilinear function of the
   coefficient tuple. This is the variadic generalization of axpby.md law 5
   (bilinearity in `(α,β)`) and axpbypcz.md law 7 (trilinearity in `(α,β,γ)`).

4. **Coefficient-scaling / scalar absorption.**
   `linear_combination ((κ·a, t):rest) = linear_combination ((a, κ·t):rest)` — each
   coefficient absorbs into its paired term. Generalizes scal.md law 4, axpby.md law 8,
   axpbypcz.md law 11.

5. **Zero-coefficient term-drop.**
   `linear_combination ((0, t):rest) = linear_combination rest` for any term `t` — a
   term with zero coefficient drops from the combination (its contribution is the zero
   tensor by scal.md law 2). This generalizes the per-op identity laws (axpby.md laws
   2–3; axpbypcz.md laws 3–5) and is the **exact algebraic content of the L0 `γ==0`
   branch** at `palace/linalg/vector.cpp:749-751`: when `γ == 0` the real-real
   `AXPBYPCZ` calls `add(α, x, β, y, z)` directly — dropping the `γ·z` term and
   collapsing the arity-3 fold to the arity-2 `axpby`. This is direct source evidence
   that the family is one fold parameterized by arity.

6. **Specialization identities (derived).** Each L1 leaf is the fixed-arity instance:
   `scal(α,x) = linear_combination [(α,x)]`; `axpy(α,x,y) = linear_combination
   [(α,x),(1,y)]`; `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`;
   `axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`. These follow from
   law 2 (concatenation) plus the L1 leaves' own definitions; the subsumption chain
   `scal ≺ axpy ≺ axpby ≺ axpbypcz` recorded across the L1 entries (axpby.md law 1,
   axpbypcz.md laws 1–2) is the bounded-arity shadow of the concatenation law.

7. **Permutation-invariance — EXACT-ARITHMETIC LAW.** In exact arithmetic,
   `linear_combination` is invariant under permutation of the term list:
   `linear_combination (permute pairs) = linear_combination pairs` (tensor addition is
   commutative and associative over an exact field). The `foldl` left-to-right order
   is the **canonical** order this L2 form names.

Laws that explicitly **do not** hold:

- **Permutation-invariance under IEEE-754 (paired non-law).** The exact-arithmetic
  permutation law (law 7) does **NOT** hold bit-for-bit in floating-point: the
  summation order is a **load-bearing numerical concern** (per CLAUDE.md
  "load-bearing numerical tricks… non-associative reduction orderings… preserve as
  explicit algebraic claims"). Different reduction orderings give different bit-level
  results when the partial-sum magnitudes differ enough to lose precision in one
  ordering. The per-op entries already record this as an explicit non-law (axpby.md
  "Floating-point associativity of the summation"; axpbypcz.md notes the two L0
  branches — fused `add(α,x,β,y,z)` vs the split `AXPBY(α,x,γ,z); z.Add(β,y)` — do not
  match each other bit-for-bit). **The L2 algebra is order-agnostic for value, but
  bit-identical reproduction of any L0 call requires matching that call's pinned
  summation order**; which order a given lowered call pins is recorded by the L2>L1
  lowering theme [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md).

- **Idempotence of re-folding.** `linear_combination` over a singleton list is `scal`,
  which is not idempotent in general (scal.md non-law); there is no fold-level
  idempotence to claim.

- **Bit-level fusion identity against the multi-pass form.**
  `linear_combination [(α,x),(β,y),(γ,z)]` computed as one fused pass is not
  bit-identical to the three-pass `scal(α,x) + scal(β,y) + scal(γ,z)` chain (the
  multi-pass form rounds more times). Mathematically equal; the L0 fusion choice is
  load-bearing for bit-reproduction, transparent for value (axpbypcz.md "Fusion identity
  with three separate scal+add passes" non-law, generalized to arbitrary arity).

## Dependencies

- L1 fixed-arity specializations (the family members, recovered at each list length):
  [`scal`](../L1/scal.md) (arity 1), [`axpy`](../L1/axpy.md) (arity 2, second coeff 1),
  [`axpby`](../L1/axpby.md) (arity 2), [`axpbypcz`](../L1/axpbypcz.md) (arity 3). These
  stay firm **L1** leaves (the L1>L0 one-to-one symbol shape is load-bearing for the
  mutation rotation; `axpby-as-primitive` keeps them fused there). **At L2 and above the
  family speaks through this combinator** — there are no separate L2
  `scal`/`axpy`/`axpby`/`axpbypcz` chapters; their unique L0 anchors are folded into
  §"Arity specializations" above.
- Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md) — the element-type
  axis (`real ⊑ complex`), the concept-page-level sibling of this arity-axis unification;
  inherited unchanged, including its open upstream dependency (closure depends on the L1
  calculus adopting the `real ⊑ complex` lattice — OQ `scalar-promotion-typing-rule`, not
  yet committed; `concepts/scalar-promotion.md:49`).
- Sibling fold (do **NOT** merge): `dot` (reduce-to-scalar inner product) — see
  § "Sibling fold". Tracked as the candidate `inner_product` L2 fold under OQ
  `inner-product-fold-sibling-candidate`.
- L2>L1 lowering theme:
  [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
  narrates how the variadic L2 fold lowers into the fixed-arity L1 leaves (list-length
  dispatch: 1 → `scal`, 2 → `axpy`/`axpby`, 3 → `axpbypcz`; longer lists → left-fold of
  `axpbypcz`-into-output chains), and records which L0 summation order each lowered call pins
  (the load-bearing content of the permutation non-law).

## Variant axes

`linear_combination` has the following variant axes; the **arity** axis is the one this
operator unifies (it is NOT a remaining variant — it is the unification axis), so the
remaining axes are orthogonal to it:

1. **Output aliasing (in-place vs out-of-place)** — the in-place forms (`y ← α·x + β·y`,
   `z ← α·x + β·y + γ·z`) are the case where one term's tensor `tᵢ` **aliases the output
   buffer**. This is orthogonal to arity: every arity ≥ 1 has both an aliasing form (the
   receiver-mutating / output-arg L0 idioms) and a fresh-output form. The `γ=1`
   accumulation call sites are the aliasing case where the aliased term's coefficient is
   1 (accumulate-into): `palace/linalg/nleps.cpp:343-344`
   (`AXPBYPCZ(…, 1.0, z.Real())` / `z.Imag()`) and `palace/models/romoperator.cpp:188-189`
   (`AXPBYPCZ(…, 1.0, u.Real())` / `u.Imag()`). At L2 the fold is pure / out-of-place;
   aliasing is an L2>L1 lowering concern, NOT an arity axis.
2. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion
   sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)). Inherited
   unchanged from the L1 leaves; promote all-or-none across the scalar list. Note: this
   sub-axis is unified at the concept-page level, but its closure depends on the L1
   calculus formally adopting the `real ⊑ complex` scalar lattice — an upstream dependency
   tracked under OQ `scalar-promotion-typing-rule` and not yet committed
   (`concepts/scalar-promotion.md:49`); the inheritance here carries that dependency
   unchanged.
3. **Operand-category** — `tensor-operand | operator-operand`. The fold's operand monoid
   is parametric: the original cohort is the **tensor-operand** corner (the BLAS-1
   `scal`/`axpy`/`axpby`/`axpbypcz` family, operand monoid = tensor-addition +
   scalar-tensor-scaling). The **operator-operand** corner is the same fold over
   `LinearOperator[N, N]` operands under operator-addition + scalar-operator-scaling —
   witnessed by Palace's `BuildParSumOperator` (`palace/linalg/rap.cpp:764-787`,
   `sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` for `coeff[i] != 0`), the
   operator-domain scalar-weighted sum. The driven pipeline's per-ω system-operator
   assembly `A(ω) = K + iω·C − ω²·M + A2(ω)` is the L1 operator-operand specialization
   [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (arity-4 instance,
   affine-in-ω scalar weights). The zero-coefficient term-drop law
   (law 5) holds verbatim at this corner — `BuildParSumOperator`'s `coeff[i] != 0`
   guard IS the operator-domain `γ==0` arity-collapse. The operand category is a variant of
   the one fold, NOT a mirrored `operator_linear_combination` chapter.

**Fusion order (an L0 implementation detail, NOT an L2 variant axis)**: single aligned
pass (`add(α, x, β, y, z)`) vs multi-call split (`AXPBY(…); z.Add(…)`) — transparent for
value, load-bearing for bit-reproduction. This is the L2>L1>L0 realization of the fold's
seed-and-accumulate; recorded in the lowering theme, not as an L2 axis.

## Fusion note

The single aligned pass over compatible-shape operands — the MFEM `add(α, x, β, y, z)`
5-arg in-place linear-combine (`palace/linalg/vector.cpp:726-730` for the `AXPBY`
real-real path; `:749-751` for the `AXPBYPCZ` `γ==0` fast-path) — is the
**transparent-performance-trick implementation** of the fold: one strided pass computing
`Σᵢ aᵢ·tᵢ[idx]` per position `idx` rather than the unfused seed-then-accumulate chain. It computes
the same value as the unfused fold modulo IEEE-754 summation order (the load-bearing
permutation non-law above). The precondition for the aligned pass is exactly the
signature's shape precondition `all tᵢ : Tensor[(S: ...)]` (every term is congruent over the
shape group `S` the pass strides over). L2 de-fuses the aligned pass into the fold's
seed-and-accumulate and records the fusion as this one note.

## Sibling fold: dot is not subsumed

`dot :: (Tensor[(S: ...)], Tensor[$S]) -> Scalar` is a **different** fold —
`foldl (+) 0 (zipWith (·) x y)` (conjugation-weighted in the Hermitian complex case) — a
**reduce-to-scalar** inner product, NOT a scalar-weighted **tensor** sum. Its result type
is `Scalar`, not `Tensor[$S]`; it reduces over the shape group `S` (and carries an MPI
collective), whereas `linear_combination` is element-local over `S` and folds over the
term list. Its laws are symmetry / Hermitian-symmetry / positive-semi-definiteness, which
have no analogue here. The target is a small **algebra of folds** — a tensor-producing
linear-combination fold AND a scalar-producing inner-product fold — not one
mega-combinator. The sibling [`inner_product`](./inner_product.md) L2 fold captures `dot` /
`tdot` as conjugation-convention variants (the axis there is conjugation-convention, not
arity). It is deliberately **NOT merged** into `linear_combination`: same operand shape
`(Tensor[(S: ...)], Tensor[$S])`-ish, but a different codomain (`Scalar` vs `Tensor[$S]`) and a
different combining step (zip-and-reduce-over-`S` vs scale-and-accumulate-over-the-term-list).
The do-NOT-merge boundary is load-bearing and symmetric — recorded here and in
[`inner_product`](./inner_product.md) §"Sibling fold". The two are the small algebra of
folds (one tensor-producing, one scalar-producing), not one mega-combinator.

> **Empirical-match caveat (not a status reduction).** There is **no dedicated unit
> test** exercising the BLAS-1 linear-combination free functions — searches for
> `AXPY` / `AXPBY` / `AXPBYPCZ` and the member `.AXPBY(` / `.AXPBYPCZ(` / `operator*=`
> forms in `test/unit/test-vector.cpp` returned zero hits; the `test-vector.cpp`
> "Vector Sum" tests (`:17`, `:42`, `:76`) exercise `linalg::Sum` (a reduce-to-scalar
> MPI-collective, the `dot`/`nrm2`-family fold), which is a **different** fold and not a
> witness for the specialization identities. The specialization identities are instead
> grounded by direct source-transcription (the `γ==0` arity-collapse branch
> `vector.cpp:749-751`; the `AXPBY` real-real fusion pass `:726-730`; the free-function
> decls `vector.hpp:305-316`) plus the verified live call sites. The
> firm-without-dedicated-test bar follows the [`chebyshev-iteration`](./chebyshev-iteration.md)
> precedent (source-transcription confidence + integration coverage).

## L2 vs L1 distinction

- **L1**: four distinct fixed-arity operators (`scal` / `axpy` / `axpby` / `axpbypcz`),
  mirroring Palace's four L0 C++ symbols one-to-one; each a leaf primitive whose
  one-to-one shape is load-bearing for the L1>L0 mutation rotation. The arity is fixed
  per operator; the term list is below L1 resolution.
- **L2**: one variadic fold `linear_combination` over a `[(Scalar, Tensor[(S: ...)])]` term
  list; the four fixed arities are recovered as list-length specializations (law 6); the
  family's distinct fixed-arity call shapes (a kernel-fusion / call-shape choice) are
  unfolded into the canonical multi-term combination; the single aligned pass is de-fused
  into the fold's seed-and-accumulate (the fusion note). The arity axis — over which L1
  has four operators — is the axis this single L2 operator unifies.

## Evidence

- `palace/linalg/vector.cpp:749-751` — the `γ == 0` branch in real-real `AXPBYPCZ`:
  `if (gamma == 0.0) { add(alpha, x, beta, y, z); }`. The in-source arity-collapse — the
  arity-3 op dropping its third term and calling the arity-2 `add` directly. Exact
  algebraic content of law 5 (zero-coefficient term-drop).
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` →
  `add(alpha, x, beta, y, y)` (the MFEM 5-arg single aligned in-place linear-combine; the
  fusion-note witness for the arity-2 case).
- `palace/linalg/vector.cpp:702-712` — `AXPY(double, Vector, Vector)` with the `α == 1.0`
  fast-path (`y += x` else `y.Add(alpha, x)`) — the arity-2-coeff-1 (`axpy`) leaf.
 
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=(std::complex<double>)`,
  the arity-1 (`scal`) site, with the `si == 0.0` real fast-path branch at `:207-211`
  (the internal scalar-promotion site).
- `palace/linalg/vector.hpp:305-316` — the free-function template decls `AXPY`
  (`:305-307`, comment `Addition y += alpha * x.`), `AXPBY` (`:309-311`, comment
  `Addition y = alpha * x + beta * y.`), `AXPBYPCZ` (`:313-316`, comment
  `Addition z = alpha * x + beta * y + gamma * z.`). The bounded-arity surface the fold
  unifies.
- `palace/linalg/nleps.cpp:343-344` — `AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(),
  X[j].Imag(), 1.0, z.Real())` and the `.imag()` line: the `γ=1` fold-into-output
  (output-aliasing variant axis, accumulate-into form).
- `palace/models/romoperator.cpp:188-189` — `AXPBYPCZ(y(j).real(), V[j], y(j+1).real(),
  V[j+1], 1.0, u.Real())` and `u.Imag()`: ROM solution reconstruction, the same
  accumulate-two-terms-into-output `γ=1` shape (multi-term combination open-coded as
  iterated arity-3 fold).
- `palace/models/timeoperator.cpp:217` — `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)`: RK
  time-integrator stage, the `γ=0` collapse to the arity-2 `axpby` (`k2 ← RHS2 + dt·k1`);
  live witness of law 5.
- `palace/linalg/iterative.cpp:632` — `w *= 1.0 / Hj[j + 1]`: GMRES Arnoldi
  basis-normalisation, the arity-1 (`scal`) leaf in the wild.
- Artifact cross-references: `book/src/L1/scal.md`,
  `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md` (the four firm
  leaves; signatures, laws, variant axes); `book/src/concepts/scalar-promotion.md` (the
  element-type-axis unification — the precedent for this arity-axis unification);
  `scaffolding/decisions/axpby-as-primitive.md` (the fused-leaf decision; governs L1
  leaf-vs-decompose only, does not preclude the L2 fold);
  `book/src/L2/chebyshev-iteration.md` (L2 chapter-format + firm-without-dedicated-test
  precedent).
