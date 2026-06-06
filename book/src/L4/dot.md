---
layer: L4
operator: dot
firmness: firm
edges:
  depends-on:
    - target: L4/inner_product
      kind: specializes
    - L3/dot
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/dot
variant_axes:
  - conjugation-convention (hermitian dot / unconjugated tdot — complex element-type only; value-bearing for complex vectors)
  - element-type (real / complex)
---

# dot

The L4 **Hermitian/symmetric inner-product verb**: `α = ⟨x, y⟩`, the named unit a
CG/GMRES description wants written as `dot(p, Ap)` rather than an inlined
`inner_product` application. `dot` is one of the **kept named abstractions** that
**rises to L4 as a named verb** per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2 "Kept named abstraction — rises": it decomposes into a simple combinator
application (it IS the [`inner_product`](./inner_product.md) reduction at `M = I`
with the Hermitian/symmetric kernel), **but** its simple named definition is
literature-standard and aids the simplification of downstream algorithms and their
tie-back to the literature. It is **not removed** just because its kernel is
replaceable — it earns its place as a first-class named verb, **and its parent
combinator [`inner_product`](./inner_product.md) rises too** (a permitted
genuinely-distinct dual: the general combinator vs. the literature-standard
specialization downstream algorithms reference by name).

The L4 form re-expresses **through** the firm L4 combinator
[`inner_product`](./inner_product.md) (replace-and-propagate, NOT a re-derived
fold) and is value-thread-isomorphic to the firm L3 named abstraction
[`L3/dot`](../L3/dot.md).

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`) and the
**backend-lowering target** (project memory `project_l4_is_backend_lowering_target`):
the feature surface whose semantics match the external GPU-tensor backend. `dot` is
the named verb every Krylov / eigen solver description reuses at the feature surface
(the CG `α`/`β` coefficients `dot(r, z)` / `dot(Ap, p)`; the GMRES orthogonalization
coefficients `dot(v_i, w)`) — so the L4 surface names it as a verb even though it
decomposes, because the named form is what makes a solver description readable and
tied to the literature. It is the **named-specialization half** of the L4 data-algebra:
the general combinator [`inner_product`](./inner_product.md) is the reduce-to-scalar
fold; `dot` is the literature-standard verb a downstream algorithm spells by name.

`dot` carries **no first-class L4 calculus structure of its own** (no `Solve` monad,
no iteration carry, no convergence predicate) — like its parent combinator it is a
**pure value-producing data-parallel reduction** over the shape group `S`
(arbitrary unknown rank, NOT rank-1). It rises
as a **feature-surface verb the backend wants**, not because it carries iteration
structure.

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../design/l4_calculus.md`](../design/l4_calculus.md). `dot` adds **no reduction-rule
extension** — it is the [`inner_product`](./inner_product.md) reduction read at the
fixed `M = I` weight with the Hermitian/symmetric kernel. Pseudo-language is Haskell
`::` signatures inside a `text` fence per the L4/L3 notation invariant.

## Signature

    -- the Hermitian/symmetric inner-product verb: inner_product at M = I
    dot  :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar
    tdot :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar     -- unconjugated complex-only co-variant

    dot  x y = inner_product x y                        -- Hermitian (complex) / symmetric (real); M = I
    tdot x y = inner_product x y  with unconjugated kernel   -- complex-only conjugation-axis value

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1; identical to the L4 combinator
[`inner_product`](./inner_product.md) §Signature read at `M = I`, and to the firm L3
signature — the L4 verb is value-thread-isomorphic to both):

- `x` — `Tensor[(S: ...)]` — read-only; the **conjugated** (arg-1) operand in `xᴴ y`.
- `y` — `Tensor[$S]` — read-only; the **linear** (arg-2) operand.
- result — `Scalar` — element type per the kernel table below; `zero` on the empty tensor.
- `x` and `y` share one shape group `S` (arbitrary unknown rank, NOT rank-1) and one
  element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes; inherited unchanged from
the combinator [`inner_product`](./inner_product.md) and the firm L3 reduction):

| element type | operator | per-element `kernel(x[idx], y[idx])` | form |
|---|---|---|---|
| `real`    | `dot`  | `x[idx] · y[idx]`       | bilinear symmetric (conjugation a no-op) |
| `complex` | `dot`  | `conj(x[idx]) · y[idx]` | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot` | `x[idx] · y[idx]`       | unconjugated bilinear (the conjugation-axis second value) |

The convention is **conjugate-linear in arg-1, linear in arg-2** (`⟨x, y⟩ = xᴴ y`),
inherited unchanged from the combinator. The conjugation choice is **value-bearing
for complex vectors** and is the one fact this verb foregrounds over the combinator's
general statement: `dot` is PSD-at-the-diagonal (`dot(x, x) ≥ 0`, law 5), `tdot` is
the indefinite form (`tdot(x, x) = 0` does not imply `x = 0`). The L0 free-function
asymmetry (Palace's `linalg::Dot(comm, x, y) = yᴴ x = conj(xᴴ y)`) is below-L3
lowering content carried by the KEPT L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme — not L4 content; L4 sees the convention pinned at arg-1.

## Algebraic laws

Carried up **unchanged** from the combinator [`inner_product`](./inner_product.md)
(laws are statements about the value; `dot` is the combinator at `M = I`, so each law
holds verbatim at this fixed weight). Reproduced for L4 layer-coherence:

1. **Empty-tensor identity.** `dot` over an empty tensor is `zero`.
2. **Split-additivity / shape-concatenation-homomorphism.**
   `dot (x₁ ++ x₂) (y₁ ++ y₂) = dot x₁ y₁ + dot x₂ y₂` (`++` concatenates the shape group
   `S`) — the monoid homomorphism that licenses parallel/blocked evaluation.
3. **Conjugate-linearity in arg-1, linearity in arg-2** (complex Hermitian); the real
   member is bilinear (conjugation a no-op).
4. **Hermitian symmetry** (complex): `dot x y = conj(dot y x)`; real reduces to plain
   symmetry.
5. **Positive semi-definiteness at the diagonal** (`y = x`): `dot x x ∈ ℝ`, `≥ 0`,
   `= 0` iff `x = 0` (exact arithmetic). **This is the law the
   [`nrm2`](./nrm2.md) consumer's square-root rests on.**
6. **Zero in either argument.** `dot 0 y = dot x 0 = zero`.

Laws that explicitly **do not** hold (deferred to the lowering chain, NOT restated as
L4 laws):

- **Associativity of the reduction-tree under IEEE-754** — floating-point `(+)` is
  non-associative; bit-identical reproduction requires matching the pinned reduction
  tree (the L2>L1
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
  theme). At L4 the value is order-agnostic; the backend supplies its own tree.
- **Cauchy–Schwarz strictness in floating point** — holds mathematically, can fail by
  ULP-level amounts.
- **Positive-definiteness of `tdot`** — the unconjugated co-variant is not PSD (law 5
  is Hermitian-member-only).

The L4 law set is **identical** to the combinator's (read at `M = I`) and to the L3 /
L2 / L1 leaf's — structural, because the rotation is identity-in-form and laws about
the value are unchanged.

## Variant axes

1. **Conjugation convention** — `conj(x[idx])·y[idx]` (Hermitian `dot`) vs `x[idx]·y[idx]`
   (unconjugated `tdot`). Value-bearing for complex vectors; `tdot` is the
   conjugation-axis second value (type-API-surface-only caveat: zero Palace call
   sites — declaration + definition only, inherited from the combinator / L3 leaf).
2. **Element-type** — `real | complex`; the complex reduction is the real reduction
   lifted componentwise over `(Re, Im)` ([`dot`](../concepts/dot.md)).

The **weight axis is pinned at `M = I`** for `dot` (that pinning is exactly what makes
`dot` the named specialization rather than the general combinator); the general-`M`
weighted member is `inner_product_M` / `bilinear_form`, a note under the combinator,
not under `dot`. **Diagonal degeneration (`y = x`) is NOT a variant axis of `dot` — it
is the entry point of the [`nrm2`](./nrm2.md) consumer** (the `√ ∘ abs` post-step on
`dot(x, x)`; see [`nrm2`](./nrm2.md)).

## Relationship to inner_product (the permitted dual — do NOT merge dot INTO the combinator)

`dot` and [`inner_product`](./inner_product.md) are a **permitted genuinely-distinct
dual** per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2: the general combinator vs. the literature-standard named specialization. They are
NOT merged in the over-unification sense (which would collapse a useful named verb into
a bare combinator application and lose the literature tie-back) — but `dot` IS defined
THROUGH the combinator (`dot x y = inner_product x y` at `M = I`), so the relationship
is "named specialization re-expressed through the rising combinator", the same shape the
combinator's own §"Specializations" records. The combinator
[`inner_product`](./inner_product.md) §"Specializations" already names this `dot` verb
as the Hermitian/symmetric specialization (`dot(x, y) = inner_product x y`); this chapter
is its first-class named-verb home.

## Downward to L3

The L4 `dot` verb lowers to the firm L3 [`dot`](../L3/dot.md) as **identity-in-form on
the body**: both forms are value-thread-isomorphic — the same `Tensor[(S: ...)] -> Tensor[$S] ->
Scalar` signature read at `M = I` with the Hermitian/symmetric kernel, the same six
algebraic laws, the same deferred IEEE non-law, the same conjugation convention pinned at
arg-1, the same `(dot, tdot)` conjugation-axis profile.

**There is no dedicated L4>L3 theme file** — the identity-in-form annotation lives in-line
here, per the cycle-012 non-adjacent-identity / in-line-marker convention (CLAUDE.md
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"). This is the **same in-line-marker route** the parent combinator
[`inner_product`](./inner_product.md) takes to its L3 form (and that
[`eigsolve`](./eigsolve.md)/[`chebyshev`](./chebyshev.md) take): there is **no monadic
wrapper, no `Solve` monad, no convergence predicate, no outer driver** to dissolve across
the L4>L3 edge — `dot` is a pure value-producing reduction at both layers, so the rotation
is the identity on the verb body. An `L4-L3/dot-*-dissolution.md` would be a **degenerate
identity-in-named-terms theme** (the §1d smell — LHS and RHS the same named verb with no
vocabulary shift), so it is correctly an in-line note.

The **substantive** rotation in the downward chain is the L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) theme
(KEPT, cycle-049 D2): the conjugation/element-type dispatch, the value-level `xᴴ y` ↔ `yᴴ x`
re-order (Palace's `linalg::Dot` pins arg-2), and the per-call pinned reduction trees (the
load-bearing IEEE non-law content). The transitive L4>L3>L2>L1 identity-then-substantive
chain composes this in-line L4>L3 identity with the firm L3>L2 identity (the L3 entry's
§"Downward to L2 (through inner_product)") and the substantive L2>L1 fold-specialization —
annotated in-line per the per-adjacent-edge directory convention (no `L4-L2`/`L4-L1`
directory).

## Status

`firm` — the L4 form is the calculus-level named verb re-expressing the combinator
[`inner_product`](./inner_product.md) (firm cycle-068 D3) at `M = I` with the
Hermitian/symmetric kernel, value-thread-isomorphic to the firm L3
[`dot`](../L3/dot.md) (firm cycle-011, specialization-stub cycle-052 D3): the same
`Tensor[(S: ...)] -> Tensor[$S] -> Scalar` reduction read at the plain-weight conjugation value,
identity-in-form across the L4>L3 edge (no monadic wrapper to dissolve — §"Downward to
L3"). The six algebraic laws are carried up unchanged (each a syntactic identity or a
standard inner-product fact, read at `M = I`); the IEEE-754 reduction-tree non-law is
deferred to the firm L2>L1 fold-specialization theme (NOT restated as an L4 law); the
conjugation convention is pinned at arg-1; the conjugation × element-type variant profile
is closed. It carries **no first-class L4 calculus structure of its own** (no `Solve`
monad, no iteration carry) — it rises as a **kept named abstraction / feature-surface verb
the backend wants** per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2, alongside the rising combinator (the permitted dual). The L0 anchors are **inherited
transitively through the firm L3/L2/L1 leaf** (self-verified at L2 cycle-019; the firm L1
[`dot`](../L1/dot.md) carries the complete L0 evidence list), not re-localized this pass.
The `tdot` co-variant carries the type-API-surface-only evidentiary caveat inherited from
L1/L2/L3 (zero Palace call sites; declaration + definition only) — not a status reduction
(the `dot` reduction structure is firm and behaviorally exercised; only `tdot`'s
behavioral weight is API-only). The empirical-match witness is the `test-vector.cpp:206-207`
real-dot value test (inherited transitively); the missing dedicated L4 test does not gate
firm because every L4 law is a syntactic identity carried up from the firm combinator /
leaf below (the firm-on-positive-structure / syntactic-identity escape, the same bar
[`inner_product`](./inner_product.md) cleared).

## Evidence

Combinator + L3/L1 endpoints (firm; the value-isomorphism this L4 named verb rests on):

- `book/src/L4/inner_product.md` (firm cycle-068 D3) — the L4 combinator this verb
  re-expresses through; §"Specializations" already names `dot(x, y) = inner_product x y`
  as the Hermitian/symmetric specialization, §2-keep dual.
- `book/src/L3/dot.md` (firm cycle-011; specialization-stub cycle-052 D3) — the firm L3
  named abstraction this verb is value-thread-isomorphic to: signature (`:43-44`), the
  conjugation variant-axis kernel table (`:56-60`), the consuming-context framing (`:72-76`),
  the §"Downward to L2 (through inner_product)" identity-in-form note (`:92-103`).
- `book/src/L1/dot.md` (firm cycle-002) — authoritative on Palace surface, signature,
  algebraic laws, variant axes, and the complete L0 evidence list (inherited transitively
  here): `palace/linalg/vector.hpp:110-113`, `palace/linalg/vector.cpp:263-274` (Hermitian
  kernel + `tdot`), `palace/linalg/vector.cpp:665-685` (real/complex reductions).
- `book/src/L2-L1/inner-product-fold-specialization.md` (KEPT; cycle-049 D2) — the
  substantive L2>L1 translation: conjugation/element-type dispatch + the `xᴴ y` ↔ `yᴴ x`
  re-order + per-call pinned reduction trees (the IEEE non-law home deferred there).

L0 transitive anchors (verified on-disk this dispatch via `citecheck --anchor`, not
re-localized — inherited through the firm leaves above):

- `palace/linalg/vector.cpp:263-267` — `linalg::Dot` (anchor confirmed at `:263`); the
  Hermitian reduction kernel. (Path relative to `reference/palace/`.)
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩`
  and the α-denominator `⟨z, p⟩`; the consuming context at L0 (the `dot(p, Ap)` /
  `dot(r, z)` named-verb use), inherited transitively. (Path relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:206-207` — the real-dot value test (the positive empirical
  witness), inherited transitively. (Path relative to `reference/palace/`.)

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) — §2 "Kept named
  abstraction — rises" (`:88-109`) names `dot` as a confirmed keep, the literature-standard
  named verb that rises to L4 alongside its parent combinator (the permitted dual).
- `book/src/concepts/dot.md` — the BLAS-1 heritage / element-type cross-cutting framing.
- `book/src/design/l4_calculus.md` — the strawman; `dot` adds no reduction rule (the
  combinator's `reduce`/`zipWith` fold read at `M = I`).

Provenance: harvester:2026-06-02T205715Z (cycle-069 D2) — the `l4-dot-nrm2-named-verb-rise`
plan-tag enactment; rises the kept named abstraction `dot` to L4 as a named verb through the
firm `L4/inner_product`, per directive-2 disposition-2 (keep-and-rise) and
`concepts/black-box-vs-accelerated-kernels.md` §2.
