---
layer: L4
operator: inner_product
firmness: firm
edges:
  depends-on:
    - L3/inner_product
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/dot
variant_axes:
  - conjugation-convention (hermitian dot / unconjugated tdot — complex element-type only; the family's namesake unification axis)
  - element-type (real / complex)
  - weight-presence (M = I plain / general-or-SPD M pre-applied — the inner_product_M / bilinear_form member)
---

# inner_product

The L4 **reduce-to-scalar inner-product combinator**: a whole-tensor reduction
`α = ⟨x, y⟩` over the shape group `S` (arbitrary unknown rank), lifted to the top of the stack as a
**feature-surface verb the backend wants**. This is the BLAS-1 *combinator* (the
general reduce-to-scalar fold parameterized by the conjugation / element-type /
weight axes) that **rises to L4 regardless**, per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless". Its **kept named abstractions** — the
Hermitian [`dot`](../concepts/dot.md) and the 2-norm consumer `nrm2` (case 2,
literature-standard verbs that aid downstream algorithm clarity, e.g. `dot(p, Ap)`
in a CG description) — **rise alongside it as named verbs, a permitted dual**
(the general combinator vs. the literature-standard specialization downstream
algorithms reference by name); they are next-pull candidates noted below, NOT
authored this cycle. The L4 form re-expresses **through** the firm L3
[`inner_product`](../L3/inner_product.md) reduction (replace-and-propagate, not a
rectangular mirror); the conjugation / element-type / weight specializations are
**notes** under it (§"Specializations").

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`) and the
**backend-lowering target** (project memory `project_l4_is_backend_lowering_target`):
the feature surface whose semantics match the external GPU-tensor backend. The
inner product is a primitive the backend supplies directly, so the L4 surface must
name it as a verb so every in-scope feature (assemble AND solve) can be written at
L4 against the backend's verb set. `inner_product` is the **data-algebra half** of
the L4 vocabulary alongside its sibling [`linear_combination`](./linear_combination.md):
the half the iteration-structural combinators *consume* in their step bodies (the
CG `α`/`β` coefficients and GMRES orthogonalization coefficients inside
[`krylov_step`](./krylov_step.md)'s body are `inner_product` let-bindings).

`inner_product` is **not** an iteration-structural combinator like
[`iterate_while`](./iterate_while.md) / [`solve_family`](./solve_family.md) /
[`fold_solve`](./fold_solve.md). Those thread a `SimState` carry through a stopping
predicate or schedule; `inner_product` is a **pure value-producing data-parallel
reduction** over the shape group `S` — no control-flow, no monadic `Solve` effect,
no convergence predicate, no carry. (The per-element kernel is embarrassingly
parallel; only the final sum communicates — and the MPI collective is out of scope
per CLAUDE.md §Scope, ranks read as single-rank equivalents.)

The VOCABULARY-SHIFT REDIRECT + L4-is-the-backend-lowering-target framing
(memory `project_blackbox_vs_accelerated_kernels`,
`project_l4_is_backend_lowering_target`) set the admission test: L4 is the
feature surface, and the data-algebra combinators are feature-surface verbs the
backend wants, so they rise regardless of carrying iteration structure.

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../semantics/index.md`](../semantics/index.md). `inner_product` is a pure
whole-tensor reduction over the shape group `S`; its L4 rendering uses the strawman's term/type BNF (§1) with
no reduction-rule extension (a `reduce`/`zipWith` fold in the existing vocabulary).
Pseudo-language is Haskell `::` signatures inside a `text` fence per the L4/L3
notation invariant.

## Signature

```text
-- entry point: the reduce-to-scalar inner-product combinator
-- a pure reduction over the shape group S; no Solve monad, no carry
inner_product   :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar
inner_product_M :: Tensor[(S: ...)] -> LinOp[$S, $S] -> Tensor[$S] -> Scalar

inner_product   x y   = reduce (+) zero (zipWith kernel x y)   -- kernel from the table below
inner_product_M x M y = inner_product (apply_linop M x) y      -- weighted ≡ pre-apply M to arg-1, then plain
inner_product   x y   = inner_product_M x I y                  -- plain ≡ M = I
```

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../semantics/index.md) §1.2.1; identical to the firm L3 signature — the
L4 form is value-thread-isomorphic to it, §"Downward to L3"):

- `x` — `Tensor[(S: ...)]` — read-only; the **conjugated** (arg-1) operand in `xᴴ y`.
- `y` — `Tensor[$S]` — read-only; the **linear** (arg-2) operand.
- `M` (weighted member) — `LinOp[(S: ...), $S]` — read-only matrix-weight (a
  square / endomorphic operator, domain ≡ range = `S`, §1.2.2), pre-applied to `x`
  via the opaque [`apply_linop`](../L3/apply_linop.md) gate.
- result — `Scalar` — element type per the kernel table; `zero` on the empty tensor.
- `x` and `y` share one shape group `S` (arbitrary unknown rank) and one
  element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes; inherited unchanged from
the firm L3 reduction):

| element type | operator | per-element `kernel(x[idx], y[idx])` | form |
|---|---|---|---|
| `real`    | `inner_product` | `x[idx] · y[idx]`       | bilinear symmetric (conjugation a no-op) |
| `complex` | `inner_product` | `conj(x[idx]) · y[idx]` | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot`          | `x[idx] · y[idx]`       | unconjugated bilinear (specialization note) |

The convention is **conjugate-linear in arg-1, linear in arg-2** (the standard
Hermitian inner product `⟨x, y⟩ = xᴴ y`), inherited unchanged from the firm L3 /
L2 combinator. The L0 free-function asymmetry (Palace's `linalg::Dot` pins `yᴴ x`,
arg-2) is below-L3 lowering content carried by the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme — not L4 content; L4 sees the convention pinned at arg-1.

### Specializations (the members, tied below as notes)

The members are **not co-equal L4 chapters** — they are this reduction read at
fixed axis-values:

    dot(x, y)               = inner_product x y                          -- Hermitian (complex) / symmetric (real); M = I
    tdot(x, y)              = inner_product x y  with unconjugated kernel -- complex-only specialization
    bilinear_form(x, M, y)  = inner_product_M x M y                      -- M-weighted member: weight axis = general M

Per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2 (kept named abstraction — rises), `dot` and the `nrm2` consumer are
**literature-standard verbs that earn their name** (the named unit you want in
"`dot(p, Ap)`" / "residual `nrm2(r)`" rather than an inlined `inner_product`
application): they **rise to L4 alongside** this combinator as a permitted dual —
the general combinator vs. the named specializations downstream algorithms
reference. They have their own L4 homes ([`dot`](./dot.md), [`nrm2`](./nrm2.md)).
`tdot` is the unconjugated complex-only conjugation-axis value
(type-API-surface-only caveat: zero Palace call sites — declaration + definition
only). `bilinear_form` is the weighted member (`inner_product_M`).

## Algebraic laws

Carried up **unchanged** from the firm L3 [`inner_product`](../L3/inner_product.md)
(laws are statements about the value; the L4 form is value-thread-isomorphic to the
L3 reduction — §"Downward to L3"). Reproduced for L4 layer-coherence:

1. **Empty-tensor identity (reduction seed).** `inner_product` over an empty
   tensor is `zero`.

2. **Split-additivity / shape-concatenation-homomorphism (the defining law).**
   `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`
   (`++` concatenates the shape group `S`, `+` scalar addition). A monoid
   homomorphism from `(shape-concatenated tensors, ++)` to `(Scalar, +)` —
   collapsing the shape group `S`; this is what licenses parallel/blocked evaluation.

3. **Conjugate-linearity in arg-1, linearity in arg-2** (complex Hermitian member);
   the real member is bilinear (conjugation a no-op).

4. **Hermitian symmetry** (complex): `inner_product x y = conj(inner_product y x)`;
   real member reduces to plain symmetry.

5. **Positive semi-definiteness at the diagonal** (`y = x`): `inner_product x x ∈ ℝ`,
   `≥ 0`, with equality iff `x = 0` (exact arithmetic); SPD-`M` weighted form
   `inner_product_M x M x ∈ ℝ₊`. The law the `nrm2` consumer square-root rests on.

6. **Zero in either argument.** `inner_product 0 y = inner_product x 0 = zero`.

7. **Weighted-member specialization (derived).** `inner_product_M x I y =
   inner_product x y`; `inner_product_M x M y = inner_product (apply_linop M x) y`.

Laws that explicitly **do not** hold (all deferred to the lowering chain, NOT
restated as L4 laws):

- **Associativity of the reduction-tree under IEEE-754 (the load-bearing non-law).**
  Floating-point `(+)` is non-associative; bit-identical reproduction requires
  matching the pinned reduction tree — recorded by the L2>L1
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
  theme, not restated as an L4 law. At L4 the value is order-agnostic; the backend
  supplies its own reduction tree.
- **Cauchy–Schwarz strictness in floating point** — holds mathematically, can fail
  by ULP-level amounts due to summation ordering.
- **Positive-definiteness of `tdot`** — the unconjugated bilinear member is not PSD
  (law 5 is a Hermitian-member law only).

The L4 law set is **identical** to the L3 (and L2) combinator's set — structural,
because the rotation is identity-in-form and laws about the value are unchanged.

## Variant axes

1. **Conjugation convention** — `conj(x[idx])·y[idx]` (Hermitian `dot`) vs `x[idx]·y[idx]`
   (unconjugated `tdot`). The family's **namesake unification axis** (NOT a
   remaining variant); `tdot` is its second value (type-API-surface-only caveat).
2. **Element-type** — `real | complex`; the complex reduction is the real reduction
   lifted componentwise over `(Re, Im)` ([`dot`](../concepts/dot.md)).
3. **Weight presence** — `M = I` (plain) vs general / SPD `M` pre-applied to arg-1
   (`inner_product_M`, the `bilinear_form` member). The `tdot × weight` cell is
   scoped out (Palace exposes no unconjugated weighted member — no `tdot_M`).

**Diagonal degeneration (`y = x`) is NOT a variant axis — it is a consumer entry
point** (collapses to the norm-squared `nrm2`/`matrix_weighted_norm` consume; see
§"Consumer"). **Reduction tree is a below-L3 implementation detail, NOT an L4
variant axis** (the IEEE non-law); the backend owns it.

## Consumer (NOT an instance): nrm2 / matrix_weighted_norm

`nrm2` and `matrix_weighted_norm` are `√ ∘ abs ∘ inner_product` at the diagonal
(`y = x`) — **consumers** of this combinator's output, NOT reduction members:

    nrm2(x)                    = √ (abs (inner_product x x))   -- √ ∘ abs ∘ inner_product at y = x
    matrix_weighted_norm(x, B) = √ (inner_product_M x B x)     -- SPD B

The `√ ∘ abs` post-step is a downstream scalar map; the norm is not a reduction and
does not enter this entry's signature. Merging `nrm2` into `inner_product` would be
a category error (shape-group `S` homomorphism producing `⟨x, x⟩` vs the scalar map
`α ↦ √|α|` on that output). `nrm2` IS one of the **kept named abstractions** that
rises to L4 as a named verb (§"Specializations", case 2) — but as a *consumer*
verb, not a fold member; its do-NOT-merge boundary is the **over-unification
guard**, carried identically at L2/L3/L4. Law 5 (PSD at the diagonal) is exactly
what makes the consumer square-root well-defined.

## Downward to L3

The L4 `inner_product` combinator lowers to the firm L3
[`inner_product`](../L3/inner_product.md) as **identity-in-form on the body**: the
two forms are value-thread-isomorphic. Both layers see the same signatures, the
same `reduce (+) zero (zipWith kernel x y)` skeleton, the same seven algebraic
laws, the same deferred IEEE non-law, the same conjugation convention, and the same
variant-axis profile.

**There is no dedicated L4>L3 theme file** — the identity-in-form annotation lives
in-line here, per the non-adjacent-identity / in-line-marker convention
(CLAUDE.md §Methodology invariants "Identity rotations across non-adjacent layers
are annotated in-line"). This is the **same in-line-marker route**
[`eigsolve`](./eigsolve.md) and [`chebyshev`](./chebyshev.md) take to their L3
forms (`L4/index.md:39`/`:75`/`:81`): there is **no monadic wrapper, no `Solve`
monad, no state-stratification record, no convergence predicate, no outer driver**
to dissolve across the L4>L3 edge — `inner_product` is a pure value-producing
reduction at both layers, so the rotation is the identity on the combinator body.
An `L4-L3/inner-product-*-dissolution.md` would be a **degenerate
identity-in-named-terms theme** (the §1d smell — LHS and RHS the same named
combinator with no vocabulary shift), so it is correctly an in-line note.

The **substantive** rotation in the downward chain is the L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme (KEPT): the conjugation/element-type/weight dispatch, the
value-level `xᴴ y` ↔ `yᴴ x` re-order, and the per-call pinned reduction trees (the
load-bearing IEEE non-law content). The transitive L4>L3>L2>L1
identity-then-substantive chain composes this in-line L4>L3 identity with the firm
L3>L2 identity (the L3 entry's §"Downward to L2") and the substantive L2>L1
fusion-selection — annotated in-line per the per-adjacent-edge directory convention
(no `L4-L2`/`L4-L1` directory).

## Sibling combinator (do NOT merge)

The scalar-weighted-tensor-sum [`linear_combination`](./linear_combination.md)
is a **different** fold — scalar-weighted **tensor**
sum producing `Tensor[$S]`, NOT a reduce-to-scalar. Its concatenation-homomorphism
is over the *term list* to `(Tensor[$S], +)`; this combinator's is over the *shape
group `S`* to `(Scalar, +)`. Its combining step is scale-and-accumulate-over-the-term-
list; this combinator's is zip-and-reduce-over-`S`. The two are the small **algebra
of folds** at L4 — one tensor-producing, one scalar-producing — deliberately **NOT
merged** (the over-unification guard, symmetric in both entries; carried identically
at L2/L3/L4).

## Evidence

L2 / L3 endpoints (firm; the value-isomorphism this L4 entry rests on):

- `book/src/L3/inner_product.md` (firm) — the firm L3 reduction this L4
  entry re-expresses through: signature + kernel table (`:82-115`), conjugation
  convention (`:117-131`), the §"Specializations" notes (`:133-166`), the seven
  algebraic laws + deferred IEEE non-law (`:206-270`), the §"Downward to L2"
  identity-in-form note (`:363-387`), variant axes (`:294-317`), the `nrm2`
  do-NOT-merge consumer (`:319-337`), status + `tdot` caveat (`:339-361`).
- `book/src/L2/inner_product.md` (firm) — authoritative on the self-verified L0
  evidence list
  (`palace/linalg/vector.cpp:263-267` Hermitian kernel, `:269-274` `tdot`,
  `:664-685` real/complex reductions; `palace/linalg/operator.cpp:598-638`
  SPD-norm + weighted member; `palace/linalg/vector.hpp:247-253`
  local-then-collective; `test/unit/test-vector.cpp:206-207` real-dot value test),
  inherited transitively here.
- `book/src/L2-L1/inner-product-fold-specialization.md` (KEPT) —
  the substantive L2>L1 translation: conjugation/element-type/weight dispatch, the
  `xᴴ y` ↔ `yᴴ x` re-order, the per-call pinned reduction trees (the IEEE non-law
  home deferred there).

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` — the
  three-way disposition: §"The combinators rise regardless" (`:128-136`) names
  `inner_product` as the combinator that rises to L4 regardless; §2 "Kept named
  abstraction — rises" (`:88-109`) names `dot`/`nrm2` as the literature-standard
  named verbs that rise *alongside* it (the permitted dual).
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — the
  combinator-mining gate; this rise is **propagation of an already-firm mined
  combinator**, so the 4 gate points are satisfied by the firm L3 endpoint.
- `book/src/concepts/dot.md` — the BLAS-1 heritage / element-type cross-cutting
  framing.
- `book/src/semantics/index.md` — the strawman; adds no reduction rule (a
  `reduce`/`zipWith` fold in the existing vocabulary).
