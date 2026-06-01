---
layer: L2
operator: reciprocal
firmness: firm
lowers_to:
  - book/src/L1/reciprocal.md (identity-in-form; no firm `L2-L1/reciprocal-elementwise-identity` theme yet — the only fusion content is the transparent `s = 1/|z|²` factoring of the complex closed form, not a multi-op kernel fusion; in-line below at "Lowers to")
lifts_from:
  - book/src/L1/reciprocal.md (value-thread-isomorphic; same signature shape; whole-tensor elementwise leaf primitive, no kernel fusion to unfold)
variant_axes:
  - element-type (real / complex; collapsed to a single parameterised operator)
fold_parent: NONE (standalone elementwise leaf; NOT a member of inner_product or linear_combination — the leaf-vs-fold fork does not apply)
---

# reciprocal

Elementwise **multiplicative-inverse** as a base tensor-algebra primitive at L2 — the
**fusion-rotation** rendering of `y[i] = 1/x[i]`. Consumes a tensor `x`; produces a fresh
tensor of the same length axis whose every element is the field-multiplicative-inverse of
the corresponding input element. `reciprocal` is a **standalone elementwise leaf** at L2
with **no fold-parent** — unlike [`dot`](./dot.md) (a leaf-of [`inner_product`](./inner_product.md))
and [`scal`](./scal.md) (an arity-1 member-of [`linear_combination`](./linear_combination.md)),
`reciprocal` is not a member of any L2 fold (it neither reduces over the length axis to a
scalar nor sums scalar-weighted terms; it is a *nonlinear* elementwise self-map). Companion
to L1 [`reciprocal`](../L1/reciprocal.md) (the mutation-lifted form of the same
`Vector::Reciprocal()` / `ComplexVector::Reciprocal()` member-method pair) and L3
[`reciprocal`](../L3/reciprocal.md) (the iteration-rotation rendering); the rotation
L1 ↔ L2 is identity-in-form because `reciprocal` is a leaf field operation with no kernel
fusion to unfold. The elementwise leaf that, composed with `assemble_diagonal` (its L1 form
[`assemble-diagonal`](../L1/assemble-diagonal.md); no L2 floor yet), produces the inverse
diagonal `D⁻¹` consumed by the diagonal-preconditioner-apply chain (Jacobi, Chebyshev).

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." `reciprocal` at L2 is the base
elementwise-multiplicative-inverse primitive in that vocabulary — a single field operation
acting pointwise over the length axis `N`, with no control flow, no monadic state
threading, no reduction, and no convergence predicate.

This is a thin **floor presence** entry, authored under the 2026-05-31 foundation-first
directive `l2-floor-under-l3-blas1-cohort`. Its purpose is floor *presence*: the firm L3
[`reciprocal`](../L3/reciprocal.md) (the iteration-rotation rendering, cycle-038, consumed
inside the diagonal-preconditioner-apply chain) and the firm L1
[`reciprocal`](../L1/reciprocal.md) (the mutation-rotation leaf) sandwich a layer at which
`reciprocal` had no chapter. The L2 entry fills it so the lowering chain L3 → L2 → L1 has a
present chapter at every adjacent edge, and the L3 leaf can lower to an adjacent
same-named L2 parent rather than non-adjacently to L1.

`reciprocal` is **defined in L2 vocabulary** here (high→low discipline, CLAUDE.md
§Methodology invariants "Layers are defined high→low"): the signature, semantics, and
algebraic laws are stated at the L2 fusion-rotation resolution. The two adjacent rotations
— how the L2 form lowers to L1 and how the L3 form lowers to L2 — are narrated by the
separate lowering themes (the D10 dispatches this cycle); this chapter does not define
`reciprocal` in terms of L1 primitives. The L1 entry [`L1/reciprocal`](../L1/reciprocal.md)
is authoritative on every factual claim about the Palace surface (the
receiver-self-overwriting `Reciprocal()` member-method idiom, the complex `z̄/|z|²` kernel,
the four consumer call sites, the no-zero-guard policy, the complete L0 evidence list); this
L2 entry adds **fusion-rotation framing** and does not duplicate those details.

## No fold-parent (standalone leaf; the leaf-vs-fold fork does not apply)

`reciprocal` is a **standalone elementwise leaf** at L2 with **no fold-parent**. This is the
structural distinction from its BLAS-1-floor cohort siblings [`dot`](./dot.md) and
[`scal`](./scal.md):

- [`dot`](./dot.md) is the conjugation-axis **leaf-of** the reduce-to-`Scalar` fold
  [`inner_product`](./inner_product.md) (it folds the length axis to a scalar).
- [`scal`](./scal.md) is the arity-1 **member-of** the reduce-to-`Tensor[N]` fold
  [`linear_combination`](./linear_combination.md) (it is the arity-1 scalar-weighted-sum
  term).
- `reciprocal` (this entry) is **neither**. It is a *nonlinear* elementwise self-map
  `Tensor[N] -> Tensor[N]` (`1/(a+b) ≠ 1/a + 1/b` — the defining non-linearity that
  distinguishes it from the linear `linear_combination` leaves). It does not reduce over the
  length axis (so it is not an `inner_product` member) and it is not a scalar-weighted-sum
  term (so it is not a `linear_combination` member). No L2 fold subsumes it.

**Consequence — design-finality.** The **leaf-vs-fold design fork** under batch-12
meta-phase adjudication (`book/src/L2/index.md` §"Working Notes",
`dot-l2-leaf-floor-vs-fold-only-design`) concerns whether the per-leaf L2 floors `dot` /
`scal` should be same-named standalone chapters (the **(b)** reading) or whether the L2
surface should be the fold-parents only with no per-leaf floor (the **(a)** reading). **That
fork does not apply to `reciprocal`**: there is no fold-parent for the (a) reading to
re-anchor this leaf into. `reciprocal`'s L2 floor is **design-final** regardless of the
meta-phase adjudication — it can only ever be a same-named standalone leaf, because no
`inner_product` / `linear_combination` fold-parent subsumes a nonlinear elementwise
self-map. The closest elementwise siblings are `elementwise_product` (the binary Hadamard
multiply — an L2-floor candidate not yet authored, referenced here as plain text) and the
forthcoming `normalize` composite; `reciprocal` shares the *elementwise leaf* shape with
them but composes neither.

## Signature

    reciprocal :: Tensor[N] -> Tensor[N]
    reciprocal x = (\i -> 1 / x[i])   for i in [0, N)

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no
destination buffer):

- **`x`** — `Tensor[N]` — the input tensor with a single length axis `N`. Read-only at L2
  (the L2 form is pure / out-of-place; the L0 receiver self-overwrite is reintroduced only
  at the L1>L0 lowering).
- **result** — `Tensor[N]` — same axis `N` as `x`; **same element type** as `x`. Every
  output element equals the field-multiplicative-inverse of the corresponding input element.
  The result element type **tracks** the input element type (real `x` → real result; complex
  `x` → complex result) — unlike [`nrm2`](./nrm2.md), which collapses both to a real-valued
  result. `reciprocal` is a self-map on the vector type's element field.

The L2 signature is **identical in shape to the L1 signature** modulo notation; the rotation
L2 → L1 is identity-in-form on the primitive (there is no kernel fusion the L2 layer un-does
beyond the transparent `s = 1/|z|²` intermediate factoring — see § "Fusion note").

**Precondition (partiality).** `reciprocal(x)` is defined only at indices `i` where
`x[i] ≠ 0`. The L0 source carries **no zero-guard** (the complex body computes
`s = 1.0 / (XR[i]² + XI[i]²)` unconditionally at `palace/linalg/vector.cpp:257`; the real
upstream `mfem::Vector::Reciprocal()` divides without runtime check). At L2 the operator is
**partial**: undefined wherever `x[i] = 0`; the no-zero-guard policy lifts as a precondition
on the input (callers must ensure `x[i] ≠ 0 ∀ i`), recorded in the same form as
[`scal`](./scal.md)'s inverse-law non-zero requirement and L1 `normalize`'s `x ≠ 0`
precondition. Consumer call sites preclude zero by precondition (the Jacobi/Chebyshev
consumers require `diag(A) > 0`, the SPD assumption) or by construction (the FE-assembly
`test_multiplicity` is `≥ 1` per active dof). The partiality is the L2 reflection of the L0
no-zero-guard policy; it is **not** a variant axis.

## Semantics

`reciprocal` at L2 is a single base tensor-algebra field operation: a value-threaded
transformation `x -> y` where `y[i] = 1/x[i]` for every element index `i ∈ [0, N)`. The
operator is **element-local** (every output element depends on exactly one input element),
**reduction-free** (no cross-element communication), and **rank-local** (no MPI collective
at any layer; ranks own disjoint slices of `N` and apply the reciprocation independently —
contrast `dot` / `nrm2`, which reduce over `N` and do carry an MPI collective).

It is **pure / out-of-place** at L2: it consumes the prior value of `x` and produces a fresh
tensor; no destination buffer appears in the signature. The L0 in-place receiver-mutating
idiom (`x.Reciprocal()` overwriting `*this`) is an L2>L1 (and onward L1>L0) lowering concern,
captured by the output-aliasing direction of the lowering themes — not by the L2 algebra.

**Element-type semantics.** For real `x`, the reciprocal is the field-multiplicative-inverse
`1/x[i]` in `ℝ`. For complex `x`, the reciprocal is `1/z = z̄/|z|²` in `ℂ` — the closed-form
complex multiplicative-inverse `1/(a + bi) = (a − bi)/(a² + b²)`. The complex closed-form
decomposition is recorded as a law (law 5 below), not as a variant — the same elementwise
map in both fields. The L0 complex kernel realises `1/z = z̄/|z|²` via the intermediate
squared modulus `s = 1/|z|²` (`palace/linalg/vector.cpp:257-259`); the intermediate is a
transparent factoring of the closed form, not an L2 sub-operator (see § "Fusion note").

## Fusion note

`reciprocal` is a **leaf, with no multi-operation kernel fusion to unfold.** L2 is the layer
where kernel fusion across multiple algebraic operations is unfolded into composition.
`reciprocal` is a single elementwise multiplicative-inverse pass, not a fused composite of
distinct algebraic operations — so there is **no de-fusion treatment** for L2 to perform: the
L0 form is *already* the unfolded single-pass elementwise reciprocation.

The one intra-element factoring the complex kernel exhibits is the reuse of the intermediate
scalar `s = 1/(XR[i]² + XI[i]²) = 1/|z|²`, computed once per element and applied to both real
and imaginary components (`XR[i] *= s; XI[i] *= -s`, `palace/linalg/vector.cpp:257-259`). This
is a **transparent performance trick** — algebraically `(a − bi)/(a² + b²)` factors as
`a·s − i·b·s` with `s = 1/(a²+b²)`, exactly what the kernel computes; recomputing `1/(a²+b²)`
for each component would give the identical value. Per CLAUDE.md "transparent performance
tricks… algebraically equivalent to their unfolded form: the L1 form is the unfolded form,
the trick gets a one-line note", the L2 form is the closed-form `z̄/|z|²` and the `s` reuse is
this one note. It is **not** a load-bearing numerical trick (no non-associative reduction, no
mixed-precision intermediate, no determinism claim — a single deterministic division and two
multiplies per element). The L2>L1 lowering theme is where the in-place receiver overwrite and
the `forall_switch` host/device dispatch reappear; the `s`-reuse factoring is recorded here as
the single transparent note and otherwise `reciprocal` is treated as the base primitive it is.

## Algebraic laws

The eight laws that hold at L1 (per `book/src/L1/reciprocal.md` §"Algebraic laws") hold
**unchanged** at L2 — the rotation L2 ↔ L1 is identity-in-form on the operator's body and
signature, so the properties of the elementwise multiplicative-inverse map transport without
modification. Reproduced so the L2 reader does not have to reach to L1. They are stated where
the relevant elements are nonzero (the operator's precondition); the partiality is recorded
once (§ Signature) and not re-stated per law. Absences are deliberate and inherited.

1. **Involution (where defined)**: `reciprocal(reciprocal(x)) = x`, provided every
   `x[i] ≠ 0` (so the intermediate vector also has no zero entries). The composition of the
   multiplicative-inverse with itself is the identity on the multiplicative group of the
   element field (`ℝ*` or `ℂ*`). Witnessed by the closed-form `1/(1/z) = z` from the complex
   body's `(a−bi)/(a²+b²)` formula.
2. **Multiplicative-inverse identity (per element)**: `x[i] · reciprocal(x)[i] = 1` for every
   `i` where `x[i] ≠ 0`. The defining identity of the multiplicative inverse, applied
   pointwise. Composed with the `elementwise_product` primitive it yields the all-ones vector:
   `elementwise_product(x, reciprocal(x)) = 𝟙`.
3. **Scalar-factor distribution**: `reciprocal(scal(α, x)) = scal(1/α, reciprocal(x))` for any
   nonzero scalar `α`. The reciprocal of a uniformly-scaled vector is the inverse-scaled
   reciprocal — pointwise `1/(α·x[i]) = (1/α)·(1/x[i])`. This is the law that makes
   `reciprocal` compose cleanly with [`scal`](./scal.md):
   `(reciprocal ∘ scal(α)) = (scal(1/α) ∘ reciprocal)`.
4. **Multiplicative-distributivity (over the elementwise product)**:
   `reciprocal(elementwise_product(x, y)) = elementwise_product(reciprocal(x), reciprocal(y))`
   for `x[i], y[i] ≠ 0` everywhere. The reciprocal of an elementwise product is the
   elementwise product of reciprocals — pointwise `1/(x[i]·y[i]) = (1/x[i])·(1/y[i])`.
5. **Complex closed-form (complex element-type only)**: for complex `x`,
   `reciprocal(x)[i] = conj(x[i]) / |x[i]|²` where `|·|²` is the squared modulus. Equivalently
   `1/(a + bi) = (a − bi)/(a² + b²)`. The L0 kernel realises it verbatim
   (`palace/linalg/vector.cpp:257-259`).
6. **Conjugate–reciprocal commutation (complex)**: `reciprocal(conj(x)) = conj(reciprocal(x))`
   for complex `x ≠ 0`. The complex conjugate commutes with the reciprocal:
   `1/conj(z) = conj(1/z)`. Pointwise consequence of law 5.
7. **Identity on the all-ones input**: `reciprocal(𝟙) = 𝟙` where `𝟙` is the all-ones vector
   of axis `N`. Pointwise `1/1 = 1`. The fixed point of the operator.
8. **Negation factor**: `reciprocal(scal(−1, x)) = scal(−1, reciprocal(x))` for nonzero `x`.
   Pointwise `1/(−x[i]) = −(1/x[i])`. Special case of law 3 with `α = −1`.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Total definedness**: the operator is **partial** — `reciprocal(0)` is undefined (division
  by zero). The L0 kernel produces `NaN` / `±∞` rather than a clean error. Recorded as a
  precondition on the input (§ Signature) rather than an algebraic law that fails.
- **Linearity in `x`**: `reciprocal(x + y) ≠ reciprocal(x) + reciprocal(y)` in general.
  `1/(a+b)` is not `1/a + 1/b` — the reciprocal is a **nonlinear** elementwise map. This is the
  defining feature distinguishing it from the linear BLAS-1 leaves
  ([`scal`](./scal.md), `axpy`, `axpby`, `axpbypcz`) at L2 — and the structural reason
  `reciprocal` is **not** a member of the `linear_combination` fold (the fold's members are the
  linear scalar-weighted-sum arities; a nonlinear self-map is not a fold member).
- **Bit-level involution under finite precision**: law 1 holds exactly in `ℝ` / `ℂ` but is
  approximate at IEEE-754 — a round-trip `1/(1/x[i])` rounds twice and may differ from `x[i]`
  by a few ULPs. Transparent-trick consideration; not load-bearing for the Jacobi/Chebyshev
  consumers (which use the *intermediate* `D⁻¹` directly, never round-trip).
- **Bit-level distributivity under finite precision**: laws 3, 4 hold exactly in `ℝ` / `ℂ` but
  the two sides round differently in IEEE-754. Algebraically equal, bit-pattern not.
  Transparent-trick; not load-bearing.
- **Closed-form unification of real and complex**: law 5 is recorded in complex-specific form
  because the complex kernel realises `1/z = z̄/|z|²` as a non-trivial
  `s = 1/(XR²+XI²); XR *= s; XI *= -s` decomposition (`palace/linalg/vector.cpp:257-259`); it
  degenerates to the trivial `1/x` in `ℝ` but is not stated in unified form (the unified
  statement would erase the non-trivial complex decomposition the kernel realises).

The law set and non-law set are **inherited unchanged** from L1; the L2 rendering introduces
no new laws or non-laws. This is what makes the L2>L1 hop identity-in-form on the primitive's
signature: not only does the signature transport unchanged, the entire algebraic profile
transports unchanged.

## Dependencies

**Same-layer (L2)**: none. `reciprocal` is a **leaf elementwise primitive** at L2 just as it
is at L1 and L3 — element-local, reduction-free, single-tensor argument, no cross-element
coupling, no decomposition into other L2 primitives. Its sub-operation is scalar reciprocation
(`1/x` in the element field), below the L2 layer's resolution (a deterministic IEEE-754
primitive for both real and complex). The intermediate scalar `s = 1/|z|²` in the complex
body is a transparent factoring of the closed form `z̄/|z|²`; it does not surface as an L2
sub-operator.

**Fold-parent**: **NONE**. Unlike [`dot`](./dot.md) (leaf-of [`inner_product`](./inner_product.md))
and [`scal`](./scal.md) (arity-1 member-of [`linear_combination`](./linear_combination.md)),
`reciprocal` is a **standalone elementwise leaf with no fold-parent** — it is a nonlinear
self-map, not a reduction term. The leaf-vs-fold design fork (`book/src/L2/index.md`
§"Working Notes") does not apply to this floor (see § "No fold-parent" above).

**Sibling on the elementwise-primitives axis (not dependency)**:

- `elementwise_product` — the binary elementwise multiply (`(x, y) -> x ⊙ y`); an L2-floor
  candidate not yet authored, referenced here as plain text. The two together — `reciprocal`
  and `elementwise_product` — complete the diagonal-preconditioner-apply chain
  `assemble_diagonal → reciprocal → elementwise_product` named at L1
  [`assemble-diagonal`](../L1/assemble-diagonal.md) §Dependencies. `elementwise_product` is a
  *sibling* elementwise leaf (also fold-parent-free), not a dependency of `reciprocal`.

**Consumers (L2)** (cross-reference, not reverse-dependencies) — the
diagonal-preconditioner-apply fan-out:

- [`krylov-step`](./krylov-step.md) — the Jacobi / Chebyshev smoother setup chain
  `dinv = reciprocal(assemble_diagonal(A))` feeds the per-step preconditioner-apply the
  kernel folds (`palace/linalg/jacobi.cpp:80`; `palace/linalg/chebyshev.cpp:178, :241`). The
  damping fold `dinv *= omega` (`palace/linalg/jacobi.cpp:92`) is the only post-`reciprocal`
  step; the apply itself is `(ω·D⁻¹) ⊙ x` (one whole-tensor `elementwise_product`).
- FE-assembly multiplicity averaging — `test_multiplicity.Reciprocal()` at
  `palace/fem/bilinearform.cpp:278`, converting the per-true-dof contribution count `c[i]`
  into the averaging weight `1/c[i]` for `SetDofMultiplicity`. A non-preconditioner consumer
  of the same elementwise-reciprocal primitive.

**L1 anchor**: [`L1/reciprocal`](../L1/reciprocal.md) (firm) — authoritative on the Palace
surface (the real `mfem::Vector::Reciprocal()` upstream-MFEM alias and the complex
`ComplexVector::Reciprocal()` kernel, the four consumer call sites, the no-zero-guard policy,
the complete L0 evidence list). This L2 entry does not duplicate those details; the L2>L1
rotation is identity-in-form on the primitive itself.

## Variant axes

`reciprocal` has **one orthogonal variant axis at L2** — the same framing as L1
(`book/src/L1/reciprocal.md` §"Variant axes") and L3, transported unchanged.

- **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L2.
  The L0 source splits into two parallel hierarchies — real `mfem::Vector::Reciprocal()`
  (upstream MFEM, consumed via the `using Vector = mfem::Vector` alias at
  `palace/linalg/vector.hpp:20`; element-wise `1/x[i]` in `ℝ`) and complex
  `ComplexVector::Reciprocal()` (Palace-defined at `palace/linalg/vector.cpp:248-261`;
  element-wise `1/z = z̄/|z|²` in `ℂ`). At L2 these collapse to one operator parameterised by
  element type; the result element type matches the input element type (law 5 records the
  complex closed form as a law, not a variant).

No other variant axes — `reciprocal` is unconditionally pure, element-local, reduction-free,
and rank-local across all variants, with no constant-folding fast paths in the L0 kernels.

Non-axes (recorded for disambiguation, inherited from L1):

- **zero-guard policy**: there is **no** zero-guarded vs. unguarded variant — the L0 source
  unconditionally divides; the partiality `reciprocal(0) = undefined` is recorded as a
  precondition on the input, not a variant axis. A speculative `safe_reciprocal(x, ε)`
  (threshold-guarded) is a separate L1 candidate / open question, not a variant of this
  operator.
- **in-place vs. out-of-place**: the L0 source is in-place receiver self-overwrite only (no
  two-arg `Reciprocal(x, y)` overload, no `linalg::Reciprocal` free function); the L2 form is
  unconditionally out-of-place (pure functional). The in-place/out-of-place choice is an
  L1>L0 mutation-rotation concern, not an L2 axis.
- **complex `s = 1/|z|²` intermediate**: a transparent factoring of the closed form (§ "Fusion
  note"), not a variant axis; the `mfem::forall_switch` host/device dispatch
  (`palace/linalg/vector.cpp:253-260`) is a transparent execution-model choice that disappears
  at L1 / L2 / L3.

The variant-axis count matches the L1 and L3 entries exactly (one orthogonal axis:
element-type). No new axes introduced by the L2 rendering; no axes merged or split.

## Status

`firm` — the L2 form is value-thread-isomorphic to the firm L1 leaf
[`L1/reciprocal`](../L1/reciprocal.md) (identity-in-form rotation on the primitive); every
algebraic law is a standard elementwise-multiplicative-inverse fact inherited unchanged, with
the complex closed-form (law 5) and the involution (law 1) directly confirmed by the in-source
`s = 1/(XR²+XI²); XR *= s; XI *= -s` kernel (`palace/linalg/vector.cpp:257-259`), the
nonlinearity / partiality / IEEE-754 caveats catalogued explicitly as non-laws, and the single
orthogonal variant axis (element-type) inherited from L1.

**Firm-on-positive-structure**: every law is a syntactic identity on the fully-present positive
complex-elementwise kernel body (`palace/linalg/vector.cpp:248-261`, read in full) and the
upstream-aliased real method — not a literature-inferred convergence claim — so the absence of
a dedicated `Reciprocal` unit test under `reference/palace/test/unit/` does not gate firm (the
`apply_linop` / `dot` / `scal` / `assemble-diagonal` firm-on-positive-structure situation, not
the `eigsolve`-convergence-semantics situation). Behaviour is exercised indirectly through the
integration coverage of the four consumer sites (Jacobi `palace/linalg/jacobi.cpp:80`;
Chebyshev `:178, :241`; bilinearform `:278`).

This is a **thin floor entry** authored under the 2026-05-31 foundation-first directive
`l2-floor-under-l3-blas1-cohort`: its purpose is floor *presence* so the firm L3
[`reciprocal`](../L3/reciprocal.md) leaf (cycle-038) rests on an adjacent same-named L2 parent
(per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**)
rather than skipping a layer to L1. No fusion structure unique to the leaf — beyond the
transparent `s = 1/|z|²` factoring the L1 entry already records — was found; the entry stays a
thin floor.

**Design-final on the leaf-vs-fold fork.** Unlike its cohort siblings `dot` / `scal` — whose
floor-vs-fold realization is under batch-12 meta-phase adjudication
(`dot-l2-leaf-floor-vs-fold-only-design`, `book/src/L2/index.md:91`) — `reciprocal` has **no
fold-parent** for the (a) fold-only reading to re-anchor it into. Its L2 floor is therefore a
same-named standalone leaf regardless of the meta-phase decision; this entry is stable on that
axis (see § "No fold-parent").

## Lowers to

L2 `reciprocal` lowers to L1 [`reciprocal`](../L1/reciprocal.md) via an **identity-in-form**
rotation: the signature `Tensor[N] -> Tensor[N]` is textually identical at both layers; the
body is the same elementwise multiplicative-inverse field operation; the eight algebraic laws,
the non-law set (partiality, nonlinearity, IEEE-754 caveats), and the single-orthogonal-axis
variant profile (element-type) all transport unchanged. The only fusion content is the
transparent `s = 1/|z|²` factoring of the complex closed form (§ "Fusion note") — not a
multi-operation kernel fusion to de-fuse — so the rotation carries no algebraic novelty.

No firm `L2-L1/reciprocal-elementwise-identity` theme file yet exists (the D10 dispatch this
cycle authors the L2>L1 lowering theme for `reciprocal`); this entry captures the identity
rotation **in-line**, following the L3 `reciprocal` and L2 `scal` backfill precedents for
in-line identity-rotation annotation (per the cycle-012 meta-phase non-adjacent-identity
convention — lowering directories are per-adjacent-edge only). The substantive rotation in the
chain is the firm L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
theme — it lowers the L1 pure-functional form into Palace's L0 in-place receiver-self-overwrite
`Reciprocal()` member-method pair (the real upstream `mfem::Vector::Reciprocal()`, the complex
`ComplexVector::Reciprocal()` kernel `s = 1/(XR²+XI²); XR *= s; XI *= -s`, the `forall_switch`
host/device dispatch, and the no-zero-guard policy). The L2>L1 hop is by contrast a
layer-coherence rotation (each layer is coherent within itself), not an algebraic one.

## Lifts from

L1 `reciprocal` lifts to this L2 entry via the **value-thread-isomorphic** identity rotation:
the L1 form's signature has no kernel fusion exposed, no destination buffer, no MPI collective,
no reduction — exactly the properties that make it L2-native by construction as a base
tensor-algebra elementwise primitive. **This L2 entry exists for layer-coherence reasons** — a
reader navigating L2 must find `reciprocal` defined in L2 vocabulary as the base
elementwise-multiplicative-inverse primitive, not have to reach down to L1 (or up to L3) to
recover the field-operation shape.

The cycle-041 BLAS-1-floor entries [`dot`](./dot.md), [`nrm2`](./nrm2.md), [`scal`](./scal.md)
are the freshest structural precedents on the same `l2-floor-under-l3-blas1-cohort` directive:
identity-in-form rotation on the primitive's signature, thin floor presence, methodology
invariant enacted. `reciprocal` is the **fold-parent-free** member of the broader floor effort
(the elementwise self-map, distinct from the fold-leaf `dot`/`scal` and the fold-consumer
`nrm2`); this dispatch closes its L2 entry.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's
signature); all L0 evidence is transitive through the firm L1 leaf. Direct citations relevant
to this L2 entry (paths relative to `reference/palace/`; L0 ranges self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation, 2026-06-01):

- [`book/src/L1/reciprocal.md`](../L1/reciprocal.md) (firm) — the L1 entry whose signature,
  semantics (element-local, reduction-free, rank-local), eight algebraic laws, single variant
  axis (element-type), partiality precondition, and complete L0 evidence chain are transported
  unchanged to L2. The laws and non-laws cited above are reproduced from the L1 entry's
  §"Algebraic laws".
- [`book/src/L3/reciprocal.md`](../L3/reciprocal.md) (firm cycle-038) — the L3 leaf this floor
  goes under; the iteration-rotation rendering whose adjacent L2 parent this entry supplies.
- [`book/src/L2/dot.md`](./dot.md), [`book/src/L2/scal.md`](./scal.md) (firm cycle-041) — the
  BLAS-1-floor cohort siblings; the thin identity-in-form floor form, the firm-on-positive-
  structure status judgement, and the floor-presence framing are inherited from these. The
  do-NOT-merge fold-cohort boundary applies to *them* (leaf-of / member-of a fold); `reciprocal`
  is the fold-parent-free member.
- [`book/src/L2/index.md`](./index.md) §"Identity-in-form BLAS-1 floors" + §"Working Notes"
  (the `dot-l2-leaf-floor-vs-fold-only-design` fork) — the floor cohort framing; `reciprocal`'s
  no-fold-parent status places it outside the fork.
- [`book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
  (firm) — the substantive L1>L0 rotation in the chain, which reintroduces the L0
  receiver-self-overwrite mutation, the complex kernel decomposition, and the no-zero-guard
  policy that the L2 entry abstracts away.

**Transitive L0 evidence (via the L1 entry; load-bearing citations re-verified on-disk for
this dispatch with `tools/citecheck/citecheck.py --anchor`, not duplicated in detail)**:

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;` — the real-vector alias;
  `Vector::Reciprocal()` resolves into upstream `mfem::Vector::Reciprocal()` (the
  real-element-type case). **Self-verified (anchor `mfem::Vector` at :20).**
- `palace/linalg/vector.hpp:107-108` — doc comment `// Set all entries to their reciprocal.`
  (:107) and `void Reciprocal();` (:108) — the complex `ComplexVector::Reciprocal()`
  declaration. **Self-verified (anchor `reciprocal` at :107, `Reciprocal` at :108).**
- `palace/linalg/vector.cpp:248-261` — `ComplexVector::Reciprocal()` definition (the
  `forall_switch` element-loop computing `s = 1.0 / (XR[i]² + XI[i]²); XR[i] *= s; XI[i] *= -s`
  at `:257-259`) — realises the complex closed form `1/z = z̄/|z|²`; witnesses laws 1, 5 and the
  no-zero-guard policy. **Self-verified (anchor `Reciprocal` at :248, `XR` at :257-258).**
- `palace/linalg/jacobi.cpp:80` — consumer: `dinv.Reciprocal();` inside
  `JacobiSmoother::SetOperator`, immediately after `op.AssembleDiagonal(dinv)`. The principal
  downstream consumer; the `assemble_diagonal → reciprocal → elementwise_product` chain's
  reciprocal step. **Self-verified (anchor `Reciprocal` at :80).**
- `palace/linalg/jacobi.cpp:16` — comment `// Assumes A SPD (diag(A) > 0) ...` — the
  operator-class-level Jacobi consumer precondition (`diag(A) > 0` ⇒ no zero entry in `dinv`)
  enforcing the L2 `x[i] ≠ 0` precondition. **Self-verified (anchor `SPD` at :16).**
- `palace/linalg/chebyshev.cpp:178` — consumer: `dinv.Reciprocal();` inside
  `ChebyshevSmoother::SetOperator` (4th-kind); `:241` — inside
  `ChebyshevSmoother1stKind::SetOperator` (1st-kind). Same chain. **Self-verified (anchor
  `Reciprocal` at :178, :241).**
- `palace/fem/bilinearform.cpp:278` — consumer: `test_multiplicity.Reciprocal();` — FE-assembly
  multiplicity-averaging step (a non-preconditioner consumer of the same elementwise-reciprocal
  primitive). **Self-verified (anchor `Reciprocal` at :278).**
- *Negative anchor*: no dedicated `Reciprocal` test under `reference/palace/test/unit/`. Per the
  firm-on-positive-structure precedent (`apply_linop`, `dot`, `scal`, `assemble-diagonal`, the
  BLAS-1 leaves), the firm judgement does not require a dedicated test — every law is a syntactic
  identity on the positive complex-elementwise kernel body.

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `x_new = reciprocal(x_old)`. Frames the
  operator as the pure-functional image of the L0 receiver-self-overwriting `Reciprocal()`
  member-method idiom; emphasises the *mutation rotation* against the source (the
  receiver-mutation drop, the no-zero-guard partiality, the complex `s = 1/|z|²` factoring).
- **L2**: base tensor-algebra field operation. `y = reciprocal(x)`. Frames the operator as a
  leaf primitive in the fusion-rotation layer's base vocabulary — a **standalone elementwise
  leaf with no fold-parent** (distinct from the fold-leaf `dot`/`scal`); emphasises that there
  is no kernel fusion to unfold (the only fusion note is the transparent `s = 1/|z|²`
  intermediate factoring). The L2 form is **identical in body and signature to L1** — the
  framing differs (mutation rotation at L1 vs fusion rotation at L2), but no operational
  adjustment occurs.

The two layers' entries are value-thread-isomorphic on the primitive itself, sharing signature,
algebraic laws (eight), non-laws (partiality, nonlinearity, IEEE-754 caveats), the single
variant axis (element-type), and the cited L0 evidence (transitive). The L2 entry exists for
floor presence — so the L3 [`reciprocal`](../L3/reciprocal.md) leaf has an adjacent same-named
L2 parent.
