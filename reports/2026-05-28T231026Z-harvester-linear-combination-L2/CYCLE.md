---
agent: harvester
invoked_at: 2026-05-28T231026Z
scope: L2 operator: linear_combination
status: integrated
integrated_at: 2026-05-29T030000Z
integration_commit: 19b53b4
integration_notes: "cycle-018 finalize — firm L2 operator linear_combination authored (chapter + L2/index dep-map flip rough-in->firm + SUMMARY register); arity-axis unification of the BLAS-1 scalar-weighted-sum cohort; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification; OQ linear-combination-harvester-formalization resolved. L2 firm 2->3."
inputs:
  - reports/2026-05-28T223022Z-combinator-miner-linear-combination-fold/CYCLE.md (the rough-in proposal; integrated cycle-017 commit 80db8d6)
  - book/src/L2/index.md (rough-in dep-map row at :25)
  - book/src/L1/{scal,axpy,axpby,axpbypcz}.md (the four firm fixed-arity leaves)
  - book/src/concepts/scalar-promotion.md (element-type-axis sibling unification)
  - scaffolding/decisions/axpby-as-primitive.md (fused-leaf decision; L1 leaf-vs-decompose only)
  - book/src/L2/chebyshev-iteration.md (L2 chapter-format precedent; firm-without-dedicated-test precedent)
  - OQ blas1-variadic-linear-combination-fold-unification (HUMAN-RAISED; constructive prong)
  - OQ linear-combination-harvester-formalization (this dispatch closes it)
  - OQ inner-product-fold-sibling-candidate (the dot-distinction forward-ref)
---

# CYCLE: Formalize linear_combination at L2

## Summary

The L2 combinator `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]` is the arity-family unification of Palace's BLAS-1 scalar-weighted-vector-sum cohort: the four firm L1 leaves `scal` / `axpy` / `axpby` / `axpbypcz` are its arity-1/2/2/3 fixed-arity specializations. Semantically it is the fold `foldl (\acc (a,t) -> acc + a·t) zeros pairs`. The cycle-017 combinator-miner proposed it (constructive prong (b) of the human-raised OQ `blas1-variadic-linear-combination-fold-unification`) and landed the rough-in dep-map row; the rough-in cleared the ≥3-instance bar (four operator definitions + six representative live call sites). This invocation firms it: full signature with shape contract, the four specialization identities as derived laws, the algebraic-law set (empty-list identity, concatenation-homomorphism — the law that makes the arities one operator —, multilinearity, coefficient-scaling, zero-coefficient term-drop mapping to the Palace `γ==0` branch), the permutation exact-arithmetic law paired with its IEEE non-associative-reduction non-law, the output-aliasing variant axis (orthogonal to arity), the single-aligned-pass fusion note, and the `dot`-distinction. I land it `firm`: the structure is a fold over firm L1 leaves, every law is a syntactic identity or a standard linear-combination fact, and the specialization identities are grounded by direct source-transcription including the in-source arity-collapse evidence at `vector.cpp:749-751`. **Empirical-match caveat (not a status reduction)**: there is NO dedicated unit test exercising the linear-combination free functions — the `test-vector.cpp` "Vector Sum" tests exercise `linalg::Sum` (a reduce-to-scalar, distinct from this fold). The firm-without-dedicated-test bar follows the `chebyshev-iteration` precedent (source-transcription confidence). Closes OQ `linear-combination-harvester-formalization`.

## Proposed changes

```edit:book/src/L2/linear_combination.md
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
correctly keeps each as a leaf (fuse, don't decompose). `linear_combination` is the
form the four leaves fuse *up* into at L2; it does not replace them.

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
linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]
linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros N) pairs
```

Shape contract (bunsen-style; named axes):

- `pairs` — `[(Scalar, Tensor[N])]` — a finite list of (coefficient, term) pairs.
  Order is the fold's evaluation order (see § "Algebraic laws", permutation
  law/non-law pair).
- each `tᵢ` — `Tensor[N]` — **shape precondition**: all terms share one length axis
  `N` (`all tᵢ : Tensor[N]`). This is the aligned-fusion-kernels precondition — every
  term shares the length axis the single aligned pass strides over.
- each `aᵢ` — `Scalar` — element type one shared `T ∈ {real, complex}` across all
  scalars and all terms, with the `real ⊑ complex` scalar-promotion lattice inherited
  unchanged from [`concepts/scalar-promotion`](../concepts/scalar-promotion.md)
  (promote all-or-none across the scalar list).
- result — `Tensor[N]` — same length axis `N`; `zeros[N]` on the empty list.

The four fixed-arity specializations (the L1 leaves as derived identities):

```text
scal(α, x)                 = linear_combination [(α, x)]
axpy(α, x, y)              = linear_combination [(α, x), (1, y)]      -- second coeff fixed to 1
axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]
axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]
```

The L2 form differs from the L1 leaves in **resolution**, along the arity axis: L1
sees four distinct fixed-arity operators (mirroring Palace's four L0 symbols); L2 sees
one variadic fold whose list length recovers each fixed arity. The element-type /
scalar-promotion sub-axis is identical to the L1 leaves' (inherited, not re-derived).

## Semantics

`linear_combination` accumulates a running tensor sum: starting from the zero tensor
of axis `N`, it folds left over the term list, adding each scaled term `aᵢ·tᵢ` into
the accumulator. The result is the tensor `Σᵢ aᵢ·tᵢ` (the linear combination of the
terms with the paired coefficients).

It is **pure / out-of-place** at L2: it consumes the coefficient/term list and produces
a fresh tensor; no destination buffer appears in the signature. The L0 in-place idioms
(the receiver-mutating / output-arg forms where one term's tensor aliases the output
buffer) are an L2>L1 (and onward L1>L0) lowering concern, captured by the
output-aliasing variant axis below — not by the L2 algebra.

Each accumulate step is element-local and reduction-free in the length axis `N` (every
output element `result[i] = Σⱼ aⱼ·tⱼ[i]` depends only on element `i` of each term).
The fold's sequencing is over the **term list**, not over `N` — there is no
cross-element communication and no MPI collective (terms are rank-local; ranks own
disjoint slices of `N`). Contrast `dot` / `nrm2`, which reduce over `N` and do carry an
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

1. **Empty-list identity (the fold's seed).** `linear_combination [] = zeros[N]` —
   the additive identity of `Tensor[N]`. This is the fold's initial accumulator.

2. **Concatenation-homomorphism (the defining law).**
   `linear_combination (a ++ b) = linear_combination a + linear_combination b`,
   where `+` on the right is element-wise tensor addition. **This is the law that
   makes the four arities one operator**: `axpbypcz`'s 3-term list is the
   concatenation of an `axpby` 2-term list and a `scal` 1-term list, so
   `linear_combination [(α,x),(β,y),(γ,z)] = linear_combination [(α,x),(β,y)] +
   linear_combination [(γ,z)]` = `axpby(α,x,β,y) + scal(γ,z)`. It is a monoid
   homomorphism from `([(Scalar,Tensor[N])], ++, [])` to `(Tensor[N], +, zeros)`,
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
  lowering theme (forthcoming; not authored here — see § "Dependencies" forward-ref).

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

- L1 fixed-arity specializations (the fold's leaves, recovered at each list length):
  [`scal`](../L1/scal.md) (arity 1), [`axpy`](../L1/axpy.md) (arity 2, second coeff 1),
  [`axpby`](../L1/axpby.md) (arity 2), [`axpbypcz`](../L1/axpbypcz.md) (arity 3). These
  stay firm L1 leaves — `linear_combination` is the form they fuse up into, not a
  replacement; the `axpby-as-primitive` decision keeps them as leaves.
- Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md) — the element-type
  axis (`real ⊑ complex`), the concept-page-level sibling of this arity-axis unification;
  inherited unchanged, including its open upstream dependency (closure depends on the L1
  calculus adopting the `real ⊑ complex` lattice — OQ `scalar-promotion-typing-rule`, not
  yet committed; `concepts/scalar-promotion.md:49`).
- Sibling fold (do **NOT** merge): `dot` (reduce-to-scalar inner product) — see
  § "Sibling fold". Tracked as the candidate `inner_product` L2 fold under OQ
  `inner-product-fold-sibling-candidate`.
- L2>L1 lowering theme (forthcoming; abstractor work, not authored here): an
  `L2-L1/linear-combination-fold-specialization` theme will narrate how the variadic
  L2 fold lowers into the fixed-arity L1 leaves (list-length dispatch: 1 → `scal`,
  2 → `axpy`/`axpby`, 3 → `axpbypcz`; longer lists → left-fold of `axpbypcz`-into-output
  chains), and will record which L0 summation order each lowered call pins (the
  load-bearing content of the permutation non-law). Forward-reference only — that chapter
  does not yet exist.

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

**Fusion order (an L0 implementation detail, NOT an L2 variant axis)**: single aligned
pass (`add(α, x, β, y, z)`) vs multi-call split (`AXPBY(…); z.Add(…)`) — transparent for
value, load-bearing for bit-reproduction. This is the L2>L1>L0 realization of the fold's
seed-and-accumulate; recorded in the lowering theme, not as an L2 axis.

## Fusion note

The single aligned pass over compatible-shape operands — the MFEM `add(α, x, β, y, z)`
5-arg in-place linear-combine (`palace/linalg/vector.cpp:726-730` for the `AXPBY`
real-real path; `:749-751` for the `AXPBYPCZ` `γ==0` fast-path) — is the
**transparent-performance-trick implementation** of the fold: one strided pass computing
`Σᵢ aᵢ·tᵢ[i]` per element rather than the unfused seed-then-accumulate chain. It computes
the same value as the unfused fold modulo IEEE-754 summation order (the load-bearing
permutation non-law above). The precondition for the aligned pass is exactly the
signature's shape precondition `all tᵢ : Tensor[N]` (every term shares the length axis
the pass strides over). L2 de-fuses the aligned pass into the fold's
seed-and-accumulate and records the fusion as this one note.

## Sibling fold: dot is not subsumed

`dot :: (Tensor[N], Tensor[N]) -> Scalar` is a **different** fold —
`foldl (+) 0 (zipWith (·) x y)` (conjugation-weighted in the Hermitian complex case) — a
**reduce-to-scalar** inner product, NOT a scalar-weighted **tensor** sum. Its result type
is `Scalar`, not `Tensor[N]`; it reduces over the length axis `N` (and carries an MPI
collective), whereas `linear_combination` is element-local in `N` and folds over the
term list. Its laws are symmetry / Hermitian-symmetry / positive-semi-definiteness, which
have no analogue here. The target is a small **algebra of folds** — a tensor-producing
linear-combination fold AND a scalar-producing inner-product fold — not one
mega-combinator. A sibling `inner_product` L2 fold capturing `dot` / `tdot` as
conjugation-convention variants is a separate candidate, tracked under OQ
`inner-product-fold-sibling-candidate` (the axis there is conjugation-convention, not
arity). It is deliberately NOT merged into `linear_combination`.

## Status

`firm` — the structure is a fold over four firm L1 leaves; the signature is the
arity-axis unification (the structural sibling of the element-type unification carried by
`concepts/scalar-promotion`, whose own closure depends on the L1 calculus adopting the
`real ⊑ complex` scalar lattice — OQ `scalar-promotion-typing-rule`, not yet committed —
inherited here as a dependency, not as a settled axis); every algebraic law is either a
syntactic identity
(empty-list seed, concatenation, specialization identities) or a standard
linear-combination fact (multilinearity, coefficient-scaling, zero-term-drop), with the
zero-coefficient term-drop directly transcribed from the in-source arity-collapse at
`palace/linalg/vector.cpp:749-751`; the permutation law is paired with its explicit
IEEE non-law per the load-bearing-numerical-trick discipline. The combinator-miner
rough-in cleared the ≥3-instance bar (four operator definitions + six representative
live call sites).

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
> precedent (source-transcription confidence + integration coverage), ratified for that
> entry cycle-012.

## L2 vs L1 distinction

- **L1**: four distinct fixed-arity operators (`scal` / `axpy` / `axpby` / `axpbypcz`),
  mirroring Palace's four L0 C++ symbols one-to-one; each a leaf primitive whose
  one-to-one shape is load-bearing for the L1>L0 mutation rotation. The arity is fixed
  per operator; the term list is below L1 resolution.
- **L2**: one variadic fold `linear_combination` over a `[(Scalar, Tensor[N])]` term
  list; the four fixed arities are recovered as list-length specializations (law 6); the
  family's distinct fixed-arity call shapes (a kernel-fusion / call-shape choice) are
  unfolded into the canonical multi-term combination; the single aligned pass is de-fused
  into the fold's seed-and-accumulate (the fusion note). The arity axis — over which L1
  has four operators — is the axis this single L2 operator unifies.

## Evidence

- `palace/linalg/vector.cpp:749-751` — the `γ == 0` branch in real-real `AXPBYPCZ`:
  `if (gamma == 0.0) { add(alpha, x, beta, y, z); }`. The in-source arity-collapse — the
  arity-3 op dropping its third term and calling the arity-2 `add` directly. Exact
  algebraic content of law 5 (zero-coefficient term-drop). **Self-verified via `read_range`.**
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, Vector, double, Vector)` →
  `add(alpha, x, beta, y, y)` (the MFEM 5-arg single aligned in-place linear-combine; the
  fusion-note witness for the arity-2 case). **Self-verified.**
- `palace/linalg/vector.cpp:702-712` — `AXPY(double, Vector, Vector)` with the `α == 1.0`
  fast-path (`y += x` else `y.Add(alpha, x)`) — the arity-2-coeff-1 (`axpy`) leaf.
  **Self-verified.**
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=(std::complex<double>)`,
  the arity-1 (`scal`) site, with the `si == 0.0` real fast-path branch at `:207-211`
  (the internal scalar-promotion site). **Self-verified.**
- `palace/linalg/vector.hpp:305-316` — the free-function template decls `AXPY`
  (`:305-307`, comment `Addition y += alpha * x.`), `AXPBY` (`:309-311`, comment
  `Addition y = alpha * x + beta * y.`), `AXPBYPCZ` (`:313-316`, comment
  `Addition z = alpha * x + beta * y + gamma * z.`). The bounded-arity surface the fold
  unifies. **Self-verified.**
- `palace/linalg/nleps.cpp:343-344` — `AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(),
  X[j].Imag(), 1.0, z.Real())` and the `.imag()` line: the `γ=1` fold-into-output
  (output-aliasing variant axis, accumulate-into form). **Self-verified.**
- `palace/models/romoperator.cpp:188-189` — `AXPBYPCZ(y(j).real(), V[j], y(j+1).real(),
  V[j+1], 1.0, u.Real())` and `u.Imag()`: ROM solution reconstruction, the same
  accumulate-two-terms-into-output `γ=1` shape (multi-term combination open-coded as
  iterated arity-3 fold). **Self-verified.**
- `palace/models/timeoperator.cpp:217` — `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)`: RK
  time-integrator stage, the `γ=0` collapse to the arity-2 `axpby` (`k2 ← RHS2 + dt·k1`);
  live witness of law 5. **Self-verified.**
- `palace/linalg/iterative.cpp:632` — `w *= 1.0 / Hj[j + 1]`: GMRES Arnoldi
  basis-normalisation, the arity-1 (`scal`) leaf in the wild. **Self-verified.**
- Artifact cross-references (read this invocation): `book/src/L1/scal.md`,
  `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md` (the four firm
  leaves; signatures, laws, variant axes); `book/src/concepts/scalar-promotion.md` (the
  element-type-axis unification — the precedent for this arity-axis unification);
  `scaffolding/decisions/axpby-as-primitive.md` (the fused-leaf decision; governs L1
  leaf-vs-decompose only, does not preclude the L2 fold);
  `book/src/L2/chebyshev-iteration.md` (L2 chapter-format + firm-without-dedicated-test
  precedent).
- Provenance: combinator-miner:2026-05-28T223022Z
  (`reports/2026-05-28T223022Z-combinator-miner-linear-combination-fold/CYCLE.md`) —
  arity-family unification of the BLAS-1 scalar-weighted-sum cohort; constructive prong
  (b) of the human-raised OQ `blas1-variadic-linear-combination-fold-unification`.
```

```edit:book/src/L2/index.md
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, concept-page-level sibling of this arity-axis unification; inherited with its open upstream dependency — OQ `scalar-promotion-typing-rule`, not yet committed). Sibling fold (do NOT merge): `dot` (reduce-to-scalar inner product). | `firm` (harvested cycle-018; promoted from rough-in proposed-by combinator-miner:2026-05-28T223022Z; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification) |
```

```edit:book/src/SUMMARY.md
- [linear_combination](./L2/linear_combination.md)
```

Insert this chapter entry under the **`# L2 — Algebraic Decompositions`** Part, as the
last chapter after the `chebyshev-iteration` entry (currently `book/src/SUMMARY.md:38`),
before the blank line separating the L2 Part from the `# L2 > L1 — Lowering` Part. Anchor:

```
# L2 — Algebraic Decompositions
- [Overview](./L2/index.md)
- [krylov-step](./L2/krylov-step.md)
- [chebyshev-iteration](./L2/chebyshev-iteration.md)
- [linear_combination](./L2/linear_combination.md)   <- new entry here
```

## Operator content

(The full operator entry is the create-file proposed-change above for
`book/src/L2/linear_combination.md`. Sections, per the harvester contract:)

- **Slug + one-line**: `linear_combination` — the arity-family unification of the BLAS-1
  scalar-weighted-vector-sum cohort; the four L1 fixed-arity leaves are arity-1/2/2/3
  specializations of one variadic fold.
- **Signature** (shape contract; bunsen-style named axes):
  `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`, body
  `foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`. Precondition `all tᵢ : Tensor[N]`
  (shared length axis); element type one shared `T ∈ {real, complex}` with `real ⊑ complex`
  scalar promotion (all-or-none across the scalar list).
- **Semantics**: pure / out-of-place tensor sum `Σᵢ aᵢ·tᵢ`; element-local in `N`, folds
  over the term list (not over `N`); no MPI collective; arity-3 is Palace's L0 ceiling,
  >3-term combinations open-coded as iterated `γ=1`-accumulate.
- **Algebraic laws** (7 holding + 3 non-laws): empty-list identity; concatenation-
  homomorphism (the unifying law); multilinearity in the scalar list; coefficient-scaling;
  zero-coefficient term-drop (= the L0 `γ==0` branch); specialization identities (the four
  leaves derived); permutation-invariance EXACT-ARITHMETIC. Non-laws: permutation under
  IEEE-754 (load-bearing summation order — paired with the exact law), re-fold idempotence,
  bit-level fusion identity vs multi-pass.
- **Variant axis**: output-aliasing (in-place / one `tᵢ` aliases output) orthogonal to
  arity; element-type / scalar-promotion (inherited). Fusion order is an L0 detail, not an
  L2 axis.
- **Dependencies**: L1 `scal` / `axpy` / `axpby` / `axpbypcz` (leaves); concept
  `scalar-promotion`; forward-ref to the forthcoming `L2-L1` lowering theme (plain text,
  not a live link).
- **Status**: `firm` (with explicit empirical-match caveat: no dedicated unit test; firm
  on source-transcription per the `chebyshev-iteration` precedent).
- **Evidence**: the `γ==0` arity-collapse `vector.cpp:749-751`; the `AXPBY` fusion pass
  `:726-730`; `AXPY` `:702-712`; `scal` site `:203-227`; the free-function decls
  `vector.hpp:305-316`; the `γ=1` aliasing call sites `nleps.cpp:343-344` /
  `romoperator.cpp:188-189`; the `γ=0` collapse `timeoperator.cpp:217`; the `scal` live
  site `iterative.cpp:632`. All self-verified via codemap `read_range` this invocation.

## Supporting evidence

All Palace ranges self-verified via codemap `read_range` / `search_text` this invocation
(producer-citation-drift discipline — `verify-citation-range` producer-self-verification):

- `vector.cpp:749-751` — `if (gamma == 0.0) { add(alpha, x, beta, y, z); }` (verified; law-5 / term-drop witness).
- `vector.cpp:726-730` — `AXPBY(double,…)` → `add(alpha, x, beta, y, y)` (verified; fusion-note witness).
- `vector.cpp:702-712` — `AXPY(double,…)` with `α == 1.0` fast path (verified).
- `vector.cpp:203-227` — `ComplexVector::operator*=` with `si == 0.0` branch at `:207-211` (verified; `scal` arity-1 site).
- `vector.hpp:305-316` — `AXPY`/`AXPBY`/`AXPBYPCZ` free-function template decls with their `// Addition …` comments (verified).
- `nleps.cpp:343-344` — `AXPBYPCZ(…, 1.0, z.Real())` / `z.Imag()` (verified; `γ=1` aliasing).
- `romoperator.cpp:188-189` — `AXPBYPCZ(…, 1.0, u.Real())` / `u.Imag()` (verified; `γ=1` aliasing).
- `timeoperator.cpp:217` — `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` (verified; `γ=0` collapse).
- `iterative.cpp:632` — `w *= 1.0 / Hj[j + 1]` (verified; `scal` arity-1 live site).
- `search_text` for `AXPBYPCZ|AXPBY|AXPY` and `.AXPBY(`/`.AXPBYPCZ(`/`operator*=`/`y.Add(`
  in `test/unit/test-vector.cpp` → **zero hits** (confirms the no-dedicated-test caveat).
- `test/unit/test-vector.cpp:17,42,76` "Vector Sum" tests read — they exercise
  `linalg::Sum` (reduce-to-scalar), NOT the linear-combination free functions (confirms
  they are NOT empirical-match witnesses for the specialization identities).

## Open questions / caveats

1. **No empirical-match test witness for the specialization identities (caveat, not a
   blocker).** Confirmed by direct search: no unit test exercises the BLAS-1
   linear-combination free functions. The entry lands `firm` on source-transcription per
   the `chebyshev-iteration` firm-without-dedicated-test precedent, with the caveat stated
   in the Status block. This realizes the cycle-017 combinator-miner's "Self-verify note"
   (caveat 5): the harvester confirmed there are no per-arity value-check assertions to
   anchor the concatenation law as an `empirical_match` — the `test-vector.cpp` Vector-Sum
   tests are a *different* fold (`linalg::Sum`). If a future cycle adds dedicated
   linear-combination tests (or locates integration coverage that pins the per-arity
   values), the caveat upgrades to a clean `empirical_match`. NOT a status reduction.

2. **L2>L1 lowering theme is needed (abstractor work, not this dispatch).** An
   `L2-L1/linear-combination-fold-specialization` theme should narrate the list-length
   arity-dispatch (1 → `scal`, 2 → `axpy`/`axpby`, 3 → `axpbypcz`; longer → left-fold of
   `axpbypcz`-into-output chains) and record which L0 summation order each lowered call
   pins (the load-bearing content of the permutation IEEE non-law). Referenced in the
   entry as a plain-text forward-reference only (no live link — the chapter does not yet
   exist). Closes OQ-adjacent to `linear-combination-harvester-formalization`; the theme
   itself is a new abstractor target.

3. **`inner_product` sibling fold (forward-ref, deliberately out of scope).** The
   `dot`-distinction §note points at OQ `inner-product-fold-sibling-candidate`. A future
   combinator-miner invocation should mine the inner-product fold as a separate parametric
   family (axis: conjugation-convention `dot`/`tdot`, not arity). Plain-text reference;
   not authored here.

4. **L2 layer-intro refresh (note for layer-intro-author, not this dispatch).** The L2
   `index.md` "Working Notes" gained a `linear_combination` dep-map row; the
   combinator-miner suggested a provenance bullet mirroring the `krylov-step` precedent
   (`index.md` Working Notes). I do not author the intro (layer-intro-author's domain) — flagging
   that a provenance bullet for the arity-family unification could be added to the L2
   Working Notes on a future intro pass.

5. **Variadic generalization beyond arity 3 is upside, not scope creep.** Palace's L0
   ceiling is `AXPBYPCZ` (arity 3); >3-term combinations are open-coded as iterated
   `γ=1`-accumulate loops (`nleps.cpp:343-344`, `romoperator.cpp:188-189`). The variadic
   `linear_combination` is the L2 abstraction those loops approximate; per CLAUDE.md it may
   later let an L4 combinator express n-term basis-reconstruction (ROM / eigenvector
   synthesis) directly. Recorded in the Semantics section as the correct generalization
   direction.
