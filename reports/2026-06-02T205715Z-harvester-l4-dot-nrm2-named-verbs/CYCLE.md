---
agent: harvester
invoked_at: 2026-06-02T205715Z
scope: L4 operator: dot + nrm2 (paired named-verb cohort)
status: integrated
integrated_at: 2026-06-02T222500Z
integration_commit: PLACEHOLDER_SHA_CYCLE069
integration_notes: |
  Applied by integrator-per-report (staging row D2, applied_at 2026-06-02T214500Z); finalized by integrator-finalize cycle-069.
  dot + nrm2 PROMOTED FIRM L4 (the two kept named abstractions rise as feature-surface verbs — dot = L4/inner_product at M=I; nrm2 = L4/inner_product-at-diagonal CONSUMER under √∘abs, NOT a fold member; black-box-vs-accelerated-kernels case 2; the c068 D3 next-pull verbs). New book/src/L4/dot.md + book/src/L4/nrm2.md. D2 SOLE L4/index count-owner: tally (10+4)→(13+4) unconditional (incorporating D1's assemble_frequency_operator) + §Active-frontier prose + 2 rows/bullets + SUMMARY inserts. Build-relevant: cargo make book exit 0; both pages render. 1 OQ promoted (l3-dot-nrm2-stale-no-l4-entry-lines-need-reanchor, c070+ follow-on). Zero gate hits.
inputs:
  - reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md §D2 (dispatch spec; plan-tag l4-dot-nrm2-named-verb-rise)
  - book/src/L4/inner_product.md (firm cycle-068 D3 — the combinator dot/nrm2 re-express THROUGH; §"Specializations" + §"Consumer (NOT an instance)" already name both as the next-pull named verbs)
  - book/src/L4/linear_combination.md (firm cycle-068 D3 — the sibling named-verb-style L4 rise precedent: combinator-rises + members-as-notes)
  - book/src/L3/dot.md (firm; the kept named abstraction below — specialization-stub, M=I Hermitian/symmetric specialization of L3/inner_product)
  - book/src/L3/nrm2.md (firm; the kept named abstraction below — consumer-stub, √∘abs∘inner_product at the diagonal, NOT a fold member)
  - book/src/concepts/black-box-vs-accelerated-kernels.md §2 (cycle-067 D3 — disposition-2 keep-and-rise; names dot/nrm2 as confirmed keeps that rise as named verbs alongside the combinator)
  - reports/.../cycle-069 D1 assemble_frequency_operator (sibling dispatch; I count its landing into the consolidated tally, do NOT author it)
---

# CYCLE: Formalize dot + nrm2 at L4 (paired named-verb cohort)

## Summary

This dispatch (D2 of cycle-069) authors the **paired named-verb cohort** `book/src/L4/dot.md` + `book/src/L4/nrm2.md` — the two **kept named abstractions** rising to L4 as named verbs through the now-firm `L4/inner_product` (c068 D3), per directive-2 disposition-2 ("keep-and-rise": literature-standard named abstractions that decompose but aid downstream algorithm clarity — the named units a CG/GMRES description wants as `dot(p, Ap)` / residual `nrm2(r)` rather than inlined `inner_product` applications). Both are **thin re-expressions THROUGH `L4/inner_product`** (replace-and-propagate, not re-derived): `dot` = the Hermitian/symmetric `inner_product` at `M = I`; `nrm2` = `√ ∘ abs ∘ inner_product` at the diagonal `y = x` — a **consumer** of `inner_product`, NOT a fold member (the do-NOT-merge over-unification guard, carried identically at L2/L3/L4). The firm L3 forms (`L3/dot.md` specialization-stub, `L3/nrm2.md` consumer-stub) were verified on disk first; their carve-out framing (`dot` specialization / `nrm2` consumer, NOT merged into the combinator) is preserved verbatim at L4. The combinator `L4/inner_product` is cross-referenced as the **permitted dual** (general combinator vs. literature-standard named specialization). Both land **firm** (firm-on-positive-structure / syntactic-identity escape — every law is a read-off identity carried up from the firm combinator + the firm L3/L1 leaves below). Both L4 slugs were verified ABSENT before authoring.

As **sole `L4/index.md` consolidated-count owner this cycle**, I also reconcile the firm tally + §Active-frontier prose to incorporate D1's `assemble_frequency_operator` (landing this same cycle) plus my two named verbs, counting each from the linked chapters' `## Status` lines per the c057-meta guard.

## Proposed changes

```new:book/src/L4/dot.md
---
layer: L4
operator: dot
firmness: firm
consumes:
  - book/src/L4/inner_product.md (the firm L4 reduce-to-scalar inner-product combinator this named verb re-expresses THROUGH; dot IS inner_product at M = I with the Hermitian/symmetric kernel — replace-and-propagate, NOT a re-derived fold)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§2 "Kept named abstraction — rises": dot is a confirmed keep — the literature-standard named unit downstream algorithms reference by name, rising to L4 as a named verb alongside the general combinator, a permitted dual)
  - book/src/L3/dot.md (the firm L3 named abstraction below; the value-thread-isomorphic image — identity-in-form on the body)
  - book/src/concepts/dot.md (the BLAS-1-heritage / element-type cross-cutting framing)
lowers_to:
  - book/src/L3/dot.md (identity-in-form on the body — the L4 named verb is value-thread-isomorphic to the firm L3 specialization-stub; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the inner_product/eigsolve/chebyshev in-line-marker route — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
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
**pure value-producing data-parallel reduction** over the length axis `N`. It rises
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
    dot  :: Tensor[N] -> Tensor[N] -> Scalar
    tdot :: Tensor[N] -> Tensor[N] -> Scalar     -- unconjugated complex-only co-variant

    dot  x y = inner_product x y                        -- Hermitian (complex) / symmetric (real); M = I
    tdot x y = inner_product x y  with unconjugated kernel   -- complex-only conjugation-axis value

Shape contract (bunsen-style; named axes; identical to the L4 combinator
[`inner_product`](./inner_product.md) §Signature read at `M = I`, and to the firm L3
signature — the L4 verb is value-thread-isomorphic to both):

- `x` — `Tensor[N]` — read-only; the **conjugated** (arg-1) operand in `xᴴ y`.
- `y` — `Tensor[N]` — read-only; the **linear** (arg-2) operand.
- result — `Scalar` — element type per the kernel table below; `zero` on the empty axis.
- `x` and `y` share one length axis `N` and one element type `T ∈ {real, complex}`.

Per-element kernel (the conjugation × element-type axes; inherited unchanged from
the combinator [`inner_product`](./inner_product.md) and the firm L3 reduction):

| element type | operator | per-element `kernel(x[i], y[i])` | form |
|---|---|---|---|
| `real`    | `dot`  | `x[i] · y[i]`       | bilinear symmetric (conjugation a no-op) |
| `complex` | `dot`  | `conj(x[i]) · y[i]` | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot` | `x[i] · y[i]`       | unconjugated bilinear (the conjugation-axis second value) |

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

1. **Empty-axis identity.** `dot` over a zero-length axis is `zero`.
2. **Split-additivity / length-concatenation-homomorphism.**
   `dot (x₁ ++ x₂) (y₁ ++ y₂) = dot x₁ y₁ + dot x₂ y₂` — the monoid homomorphism that
   licenses parallel/blocked evaluation.
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

1. **Conjugation convention** — `conj(x[i])·y[i]` (Hermitian `dot`) vs `x[i]·y[i]`
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
the body**: both forms are value-thread-isomorphic — the same `Tensor[N] -> Tensor[N] ->
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
`Tensor[N] -> Tensor[N] -> Scalar` reduction read at the plain-weight conjugation value,
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
```

```new:book/src/L4/nrm2.md
---
layer: L4
operator: nrm2
firmness: firm
consumes:
  - book/src/L4/inner_product.md (the firm L4 reduce-to-scalar inner-product combinator nrm2 CONSUMES at the diagonal y = x; nrm2 = √ ∘ abs ∘ inner_product — a CONSUMER of the fold's output, NOT a fold member, the do-NOT-merge over-unification guard)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§2 "Kept named abstraction — rises": nrm2 is a confirmed keep — the 2-norm, the named unit downstream algorithms reference by name as residual nrm2(r), rising to L4 as a named verb)
  - book/src/L3/nrm2.md (the firm L3 named abstraction below; the value-thread-isomorphic image — identity-in-form on the body)
  - book/src/concepts/nrm2.md (the BLAS-1-heritage cross-cutting framing)
lowers_to:
  - book/src/L3/nrm2.md (identity-in-form on the body — the L4 named verb is value-thread-isomorphic to the firm L3 consumer-stub; NO dedicated L4>L3 theme file, in-line §"Downward to L3", the inner_product/eigsolve/chebyshev in-line-marker route — there is no monadic wrapper / Solve-monad / convergence predicate to dissolve)
variant_axes:
  - element-type (real / complex; collapsed to a single operator — result is always real-valued and non-negative)
---

# nrm2

The L4 **Euclidean-norm verb**: `α = ‖x‖₂ = √⟨x, x⟩`, the named unit a Krylov / eigen
solver description wants written as residual `nrm2(r)` rather than an inlined
`√(inner_product r r)`. `nrm2` is one of the **kept named abstractions** that **rises
to L4 as a named verb** per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§2 "Kept named abstraction — rises": it decomposes into a simple combinator
application (`√ ∘ abs ∘ inner_product` at the diagonal `y = x`), **but** its named
definition is literature-standard and aids downstream algorithm clarity and
literature tie-back — it is **not removed** just because its kernel is replaceable.

**`nrm2` is a CONSUMER of [`inner_product`](./inner_product.md), NOT a fold member**
(the do-NOT-merge over-unification guard, carried identically at L2/L3/L4). It
post-composes two scalar maps — the defensive `abs`, then `√` — onto the combinator's
**scalar output**; it does not itself fold over the length axis. Merging `nrm2` into
[`inner_product`](./inner_product.md) would be a category error (a length-axis
homomorphism producing `⟨x, x⟩` vs. the scalar map `α ↦ √|α|` on that output). It
rises as a **consumer verb** alongside the combinator (the permitted dual), not as one
of its members.

The L4 form re-expresses **through** the firm L4 combinator
[`inner_product`](./inner_product.md) at the diagonal (NOT a re-derived fold) and is
value-thread-isomorphic to the firm L3 named abstraction [`L3/nrm2`](../L3/nrm2.md).

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`) and the
**backend-lowering target** (project memory `project_l4_is_backend_lowering_target`):
the feature surface whose semantics match the external GPU-tensor backend. `nrm2` is
the named verb every Krylov / eigen solver description reuses at the feature surface in
two distinct roles: the **residual-norm convergence readout** (`outputs.residual_norm =
nrm2(r)` in the recompute-from-residual variants) and the **Arnoldi sub-diagonal
coefficient** (`H[j+1, j] = nrm2(w)` after orthogonalization). The L4 surface names it
as a verb even though it decomposes, because the named form is what makes a convergence
test or an Arnoldi step readable and tied to the literature.

`nrm2` carries **no first-class L4 calculus structure of its own** (no `Solve` monad,
no iteration carry, no convergence predicate) — it is a pure value-producing scalar map
on a pure value-producing reduction. It rises as a **feature-surface verb the backend
wants**, not because it carries iteration structure.

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../design/l4_calculus.md`](../design/l4_calculus.md). `nrm2` adds **no reduction-rule
extension** — it is the [`inner_product`](./inner_product.md) reduction at the diagonal
`y = x` post-composed with the `√ ∘ abs` scalar map. Pseudo-language is Haskell `::`
signatures inside a `text` fence per the L4/L3 notation invariant.

## Signature

    -- the Euclidean-norm verb: √ ∘ abs ∘ inner_product at the diagonal y = x
    nrm2 :: Tensor[N] -> Scalar

    nrm2 x = sqrt (abs (inner_product x x))   -- √ ∘ abs ∘ inner_product at y = x

Shape contract (bunsen-style; named axes; identical to the firm L3 / L1 signature —
the L4 verb is value-thread-isomorphic to both):

- `x` — `Tensor[N]` — read-only; the single operand.
- result — `Scalar` — **always real-valued and non-negative** (`nrm2 x ≥ 0`),
  regardless of `x`'s element type; `zero` on the empty axis (`inner_product` seeds
  `zero`, `√ (abs zero) = zero`).

The result is always real even for a complex `x`, because the diagonal
`inner_product x x` is real-and-non-negative by law 5 (PSD at the diagonal) of the
combinator, and `√ ∘ abs` maps it to a non-negative real.

### The `abs` defensive guard (load-bearing scalar-map detail)

The defining identity is `nrm2 x = √ (inner_product x x)`; the `abs` is a **load-bearing
defensive non-negativity guard** against floating-point round-off pushing the reduction
sum slightly negative on a numerically-zero vector (it strips a sign that round-off could
have flipped, buying domain-safety for `√` — no NaN). It is a no-op in exact arithmetic
(law 5 guarantees `inner_product x x ≥ 0`) but load-bearing in floating point. The full
classification lives at the L1>L0
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
guard — classification"; at L4 it is preserved as an explicit part of the scalar map
(the L0 source is the one-line `std::sqrt(std::abs(Dot(comm, x, x)))`).

## Algebraic laws

`nrm2` is a **scalar map on the combinator's diagonal output**, so its laws are the
square-root norm-axioms over the PSD diagonal, NOT the fold's homomorphism laws (the
do-NOT-merge boundary at the law level — `nrm2` does NOT inherit split-additivity,
because `√` is not additive). The laws that hold:

1. **Non-negativity.** `nrm2 x ≥ 0` (real-valued); `= 0` iff `x = 0` (exact arithmetic,
   from combinator law 5 PSD-at-the-diagonal + `√` monotone). The `abs` guard makes the
   non-negativity hold defensively in floating point too.
2. **Empty-axis identity.** `nrm2` over a zero-length axis is `zero` (`√ (abs zero)`).
3. **Absolute homogeneity (the norm-scaling law).** `nrm2 (scal α x) = |α| · nrm2 x`
   for a scalar `α` — follows from combinator multilinearity at the diagonal
   (`inner_product (αx) (αx) = |α|² ⟨x, x⟩`) and `√`.
4. **Triangle inequality.** `nrm2 (x + y) ≤ nrm2 x + nrm2 y` (the norm axiom; the
   `inner_product` Cauchy–Schwarz fact under the square-root).
5. **Defining-identity / diagonal-consume.** `nrm2 x = √ (abs (inner_product x x))` —
   the `√ ∘ abs ∘ inner_product` composition at `y = x`; this is the law that ties the
   consumer verb to the rising combinator.

Laws that explicitly **do not** hold (deferred / category-distinct, NOT restated):

- **Split-additivity / length-concatenation-homomorphism does NOT hold for `nrm2`.**
  `nrm2 (x₁ ++ x₂) ≠ nrm2 x₁ + nrm2 x₂` in general (it is `√(nrm2 x₁² + nrm2 x₂²)`) —
  `√` is not additive. This is exactly **why `nrm2` is a consumer, not a fold member**:
  the homomorphism is a property of [`inner_product`](./inner_product.md)'s reduction,
  lost under the post-composed `√`.
- **Reduction-tree associativity under IEEE-754** — the inner `inner_product x x`
  carries the same load-bearing non-law as the combinator (pinned reduction tree for
  bit-reproduction; deferred to the L2>L1 fold-specialization theme). The outer `abs`/`√`
  scalar map is order-independent.

## Variant axes

1. **Element-type** — `real | complex`, **collapsed to a single operator** at L4 (as at
   L3): the result is always real-valued and non-negative regardless of `x`'s element
   type (the diagonal `inner_product x x` is real by combinator law 5). No conjugation
   variant axis surfaces at the `nrm2` verb level (it is absorbed into the diagonal
   consume — `inner_product x x` is Hermitian-self).

The **B-weighted overload** `linalg::Norml2(comm, x, B, Bx) = √(inner_product_M x B x)`
for SPD `B` is **NOT part of this operator** — it is the `matrix-weighted-norm` consumer
of the combinator's weighted member `inner_product_M` (tracked rough-in at L1
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), L1-promotion-gated). `nrm2`
pins the weight at `M = I` through the plain `inner_product` (the same pinning that makes
`dot` the plain-weight named specialization).

## Relationship to inner_product (CONSUMER, NOT a fold member — the do-NOT-merge guard)

`nrm2` **consumes** [`inner_product`](./inner_product.md)'s scalar output at the diagonal
and post-composes `√ ∘ abs`; it is **NOT a member of the fold cohort** and does **NOT**
merge into the combinator. This is the **over-unification guard**, carried identically at
L2/L3/L4: the combinator [`inner_product`](./inner_product.md) §"Consumer (NOT an
instance)" lists `nrm2` as a consumer; the L4 frontmatter lists `inner_product` under
`consumes`, never as a fold `nrm2` instantiates. Combinator law 5 (PSD at the diagonal)
is exactly what makes the consumer square-root well-defined. `nrm2` rises as a kept named
abstraction (the **permitted dual** — a consumer verb alongside the general combinator),
distinct from [`dot`](./dot.md), which is a *specialization* of the same combinator (at
`M = I`) rather than a consumer of its output.

## Downward to L3

The L4 `nrm2` verb lowers to the firm L3 [`nrm2`](../L3/nrm2.md) as **identity-in-form on
the body**: both forms are value-thread-isomorphic — the same `Tensor[N] -> Scalar`
signature, the same `√ (abs (inner_product x x))` skeleton (L3 writes the defining
identity through the same-layer `dot(x, x)` leaf; both denote the same Hermitian
self-inner-product value at the diagonal), the same five laws, the same do-NOT-merge
consumer carve-out, the same load-bearing `abs` defensive guard.

**There is no dedicated L4>L3 theme file** — the identity-in-form annotation lives in-line
here, per the cycle-012 non-adjacent-identity / in-line-marker convention (CLAUDE.md
§Methodology invariants "Identity rotations across non-adjacent layers are annotated
in-line"). This is the **same in-line-marker route** the combinator
[`inner_product`](./inner_product.md) and the sibling named verb [`dot`](./dot.md) take to
their L3 forms (and that [`eigsolve`](./eigsolve.md)/[`chebyshev`](./chebyshev.md) take):
there is **no monadic wrapper, no `Solve` monad, no convergence predicate, no outer
driver** to dissolve across the L4>L3 edge — `nrm2` is a pure value-producing scalar map
on a pure reduction at both layers, so the rotation is the identity on the verb body. An
`L4-L3/nrm2-*-dissolution.md` would be a **degenerate identity-in-named-terms theme** (the
§1d smell), so it is correctly an in-line note.

The **substantive** content in the downward chain is (a) the L1>L0
[`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) — the four-stage L0 chain
`linalg::Norml2` → `std::sqrt(std::abs(Dot(comm, x, x)))` and the full `abs`-guard
classification — and (b) the inner reduction's L2>L1
[`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
(the pinned reduction tree the `inner_product x x` inherits). The transitive
L4>L3>L2>L1 identity-then-substantive chain composes this in-line L4>L3 identity with the
firm L3>L2 identity (the L3 entry's §"Downward to L2 (consumer identity-in-form)") and the
substantive L1>L0 rotation — annotated in-line per the per-adjacent-edge directory
convention (no `L4-L2`/`L4-L1` directory).

## Status

`firm` — the L4 form is the calculus-level named verb re-expressing the diagonal consume
of the combinator [`inner_product`](./inner_product.md) (firm cycle-068 D3) under the
`√ ∘ abs` scalar map, value-thread-isomorphic to the firm L3 [`nrm2`](../L3/nrm2.md) (firm
cycle-011, consumer-stub cycle-052 D3): the same `Tensor[N] -> Scalar` `√(abs(inner_product
x x))` skeleton, identity-in-form across the L4>L3 edge (no monadic wrapper to dissolve —
§"Downward to L3"). The five algebraic laws are the square-root norm-axioms over the PSD
diagonal (each a syntactic identity or a standard norm fact); the homomorphism non-law is
the **defining reason `nrm2` is a consumer, not a fold member**; the inner reduction-tree
IEEE non-law is deferred to the firm L2>L1 fold-specialization theme (NOT restated as an
L4 law); the `abs` defensive guard is preserved as an explicit part of the scalar map; the
element-type axis is collapsed (result always real). It carries **no first-class L4
calculus structure of its own** (no `Solve` monad, no iteration carry) — it rises as a
**kept named abstraction / feature-surface verb the backend wants** per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2,
alongside the rising combinator (the permitted dual; as a *consumer* verb, the do-NOT-merge
boundary the over-unification guard). The L0 anchors are **inherited transitively through
the firm L3/L1 leaf** (the firm L1 [`nrm2`](../L1/nrm2.md) carries the complete L0 evidence
list; the `vector.hpp:255-260` `Norml2` one-line composition was re-verified on disk at the
L3 entry this batch), not re-localized this pass. The empirical-match witness is the
`test-vector.cpp:209-211` `Norml2` value test (`norm = √14` for `(1,2,3)`, inherited
transitively); the missing dedicated L4 test does not gate firm because every L4 law is a
syntactic identity / standard norm fact carried up from the firm combinator / leaf below
(the firm-on-positive-structure / syntactic-identity escape, the same bar
[`inner_product`](./inner_product.md) cleared).

## Evidence

Combinator + L3/L1 endpoints (firm; the value-isomorphism this L4 named verb rests on):

- `book/src/L4/inner_product.md` (firm cycle-068 D3) — the L4 combinator this verb
  consumes; §"Consumer (NOT an instance): nrm2 / matrix-weighted-norm" already records
  `nrm2(x) = √ (abs (inner_product x x))` at the diagonal as a consumer, NOT a member, with
  combinator law 5 (PSD) as the well-definedness witness.
- `book/src/L3/nrm2.md` (firm cycle-011; consumer-stub cycle-052 D3) — the firm L3 named
  abstraction this verb is value-thread-isomorphic to: signature + defining identity
  (`:33-34`), the consuming-context roles (`:42-52`), the `std::abs` defensive-guard note
  (`:58-68`), the §"Downward to L2 (consumer identity-in-form)" note (`:95-127`); its L0
  anchor `palace/linalg/vector.hpp:255-260` re-verified on-disk at `:128-132` this batch.
- `book/src/L1/nrm2.md` (firm cycle-003) — authoritative on Palace surface, signature,
  algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list (inherited transitively):
  `palace/linalg/vector.hpp:255-260`, `palace/linalg/vector.hpp:262-270`,
  `palace/linalg/operator.cpp:600-619`.
- `book/src/L1-L0/nrm2-mutation-rotation.md` (firm) — the four-stage L0 chain and the full
  `std::abs` defensive-guard classification (the substantive downward content home).
- `book/src/L4/dot.md` (this cycle, sibling) — the sibling named verb (`nrm2(x) = √dot(x, x)`
  is the L3-internal defining identity; both rise through the same combinator as the
  permitted dual).

L0 transitive anchors (verified on-disk this dispatch via `citecheck --anchor`, not
re-localized — inherited through the firm leaves above):

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template (anchor confirmed at
  `:257`); body line `:259` is `return std::sqrt(std::abs(Dot(comm, x, x)));` — the one-line
  `√ ∘ abs ∘ inner_product` composition. (Path relative to `reference/palace/`.)
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES using
  `linalg::Norml2` for the initial RHS norm, the true residual norm, and the Arnoldi
  sub-diagonal coefficients (the residual `nrm2(r)` / `H[j+1,j] = nrm2(w)` named-verb use),
  inherited transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — the `Norml2` value test (`norm = √14` for `(1,2,3)`),
  the positive empirical witness, inherited transitively. (Path relative to `reference/palace/`.)

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) — §2 "Kept named
  abstraction — rises" (`:88-109`) names `nrm2` as a confirmed keep, the 2-norm named verb
  (`residual nrm2(r)`) that rises to L4 alongside the rising combinator (the permitted dual).
- `book/src/concepts/nrm2.md` — the BLAS-1 heritage cross-cutting framing. (Note: its
  scaled-summation stability claim is incorrect per the L1 correction-pending note at
  `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
- `book/src/design/l4_calculus.md` — the strawman; `nrm2` adds no reduction rule (the
  combinator's diagonal consume + a `√ ∘ abs` scalar map).

Provenance: harvester:2026-06-02T205715Z (cycle-069 D2) — the `l4-dot-nrm2-named-verb-rise`
plan-tag enactment; rises the kept named abstraction `nrm2` to L4 as a named *consumer* verb
through the firm `L4/inner_product`, per directive-2 disposition-2 (keep-and-rise) and
`concepts/black-box-vs-accelerated-kernels.md` §2 (the do-NOT-merge over-unification guard
preserved: consumer, not fold member).
```

### `book/src/L4/index.md` — three artifacts (my OWN 2 dep-map ROWS + 2 §Vocabulary-cohort BULLETs in alpha position; + the consolidated firm TALLY + frontier prose, which I own as sole count-owner this cycle, incorporating D1's `assemble_frequency_operator`)

The dep-map rows and cohort bullets are inserted in alpha position; D1 adds its OWN `assemble_frequency_operator` row/bullet (I count it, do not author it). The four edits below are the consolidated-tally bump (block 1), the two cohort bullets (blocks 2–3, alpha position), and the two dep-map rows (blocks 4–5, alpha position).

**Block 1 — consolidated firm tally (the count-owner edit):**

```edit:book/src/L4/index.md
**Firm at L4 (10 + 4 outer-driver)** — three firm chapters landed cycle-068 (the FE-cohort→L4 frontier opener + the two BLAS-1 data-algebra combinators): the assemble-fold combinator [`fe_assemble`](./fe_assemble.md) (D1), and the two general data-algebra combinators [`linear_combination`](./linear_combination.md) + [`inner_product`](./inner_product.md) (D3) — the BLAS-1 combinators that rise to L4 regardless as feature-surface verbs the backend wants (`concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"; L4>L3 identity-in-form on the body, the `eigsolve`/`chebyshev` in-line-marker route — no dedicated theme files). Before them `fold_solve` joined the firm cohort cycle-058 (the SECOND solver-driven firm L4 combinator after `solve_family`'s rough-in): the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, the fixed-degree polynomial smoother, the two iterative-solve outer-driver **caps** (`ksp_solve`, `eigsolve`; cycle-048), and the state-threaded **fold** outer-driver `fold_solve` (cycle-058); plus the four `solve-monad` outer-driver vocabulary anchors. The two solver-driven combinators `solve_family` (independent **MAP** over an RHS family) and `fold_solve` (state-threaded **FOLD** over a time/sweep schedule) are the two children of the strawman §3.7 [`iterate-while`](./iterate-while.md) family — a map is the degenerate fold whose step ignores the accumulator — per the batch-17 two-combinator MAP/FOLD ratification; there is **no third parent abstraction** above them (the §3.7 `iterate_while` family IS the shared parent):
```

with:

```text
**Firm at L4 (13 + 4 outer-driver)** — cycle-069 (batch-21 final) landed three more firm chapters, counted from each linked chapter's `## Status` line (c057-meta guard, not from index cells): the driven per-ω **assemble** operator [`assemble_frequency_operator`](./assemble_frequency_operator.md) (D1 — the operator-operand specialization riding [`linear_combination`](./linear_combination.md)'s operator-operand corner, the driven pipeline's ASSEMBLE half reaching L4), and the two **kept named verbs** [`dot`](./dot.md) + [`nrm2`](./nrm2.md) (D2 — the literature-standard named abstractions rising through [`inner_product`](./inner_product.md) per `concepts/black-box-vs-accelerated-kernels.md` §2: `dot` the Hermitian/symmetric specialization at `M = I`, `nrm2` the `√∘abs∘inner_product` diagonal **consumer**, NOT a fold member — the do-NOT-merge over-unification guard; both L4>L3 identity-in-form on the body, the in-line-marker route, no dedicated theme files). Before them, cycle-068 landed the FE-cohort→L4 frontier opener [`fe_assemble`](./fe_assemble.md) (D1) + the two general data-algebra combinators [`linear_combination`](./linear_combination.md) + [`inner_product`](./inner_product.md) (D3) — the BLAS-1 combinators that rise to L4 regardless as feature-surface verbs the backend wants (`concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"; L4>L3 identity-in-form on the body, the `eigsolve`/`chebyshev` in-line-marker route — no dedicated theme files). Before them `fold_solve` joined the firm cohort cycle-058 (the SECOND solver-driven firm L4 combinator after `solve_family`'s rough-in): the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, the fixed-degree polynomial smoother, the two iterative-solve outer-driver **caps** (`ksp_solve`, `eigsolve`; cycle-048), and the state-threaded **fold** outer-driver `fold_solve` (cycle-058); plus the four `solve-monad` outer-driver vocabulary anchors. The two solver-driven combinators `solve_family` (independent **MAP** over an RHS family) and `fold_solve` (state-threaded **FOLD** over a time/sweep schedule) are the two children of the strawman §3.7 [`iterate-while`](./iterate-while.md) family — a map is the degenerate fold whose step ignores the accumulator — per the batch-17 two-combinator MAP/FOLD ratification; there is **no third parent abstraction** above them (the §3.7 `iterate_while` family IS the shared parent):
```

**Block 2 — `dot` cohort bullet (alpha position: after `chebyshev`, before `eigsolve`):** insert the new bullet immediately after the `chebyshev` cohort bullet (line 38) and before the `ksp_solve` bullet. Alpha order in the cohort list places `dot` after `chebyshev`. Anchor on the end of the `chebyshev` bullet:

```edit:book/src/L4/index.md
The fixed-count-vs-convergence distinction lives in the predicate, not the combinator.
- [`ksp_solve`](./ksp_solve.md) — the `Solve`-monadic outer-driver **cap** for preconditioned Krylov solves:
```

with (inserting the `dot` bullet between):

```text
The fixed-count-vs-convergence distinction lives in the predicate, not the combinator.
- [`dot`](./dot.md) — the **Hermitian/symmetric inner-product verb** `α = ⟨x, y⟩`; one of the **kept named abstractions** (directive-2 disposition-2 keep-and-rise) risen to L4 as a named verb — the literature-standard unit a CG/GMRES description wants as `dot(p, Ap)` / `dot(r, z)` rather than an inlined application. Re-expresses through the firm [`inner_product`](./inner_product.md) combinator at `M = I` with the Hermitian/symmetric kernel (a **specialization** of the combinator; identity-in-form on the body to [`L3/dot`](../L3/dot.md); no dedicated L4>L3 theme — the in-line-marker route). The conjugation × element-type variant profile is value-bearing for complex vectors (`tdot` the unconjugated co-variant, type-API-surface-only). Rises **alongside** the combinator as the permitted dual (general combinator vs. named specialization), `concepts/black-box-vs-accelerated-kernels.md` §2.
- [`ksp_solve`](./ksp_solve.md) — the `Solve`-monadic outer-driver **cap** for preconditioned Krylov solves:
```

**Block 3 — `nrm2` cohort bullet (alpha position: after `linear_combination`, before `solve_family`):** insert immediately after the `linear_combination` cohort bullet (line 40) and before the `eigsolve` bullet. Alpha order places `nrm2` after `linear_combination`. Anchor on the end of the `linear_combination` bullet:

```edit:book/src/L4/index.md
The next-pull operator-operand consumer is the driven [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (c069, GATED on this entry). Sibling of [`inner_product`](./inner_product.md) — the tensor-producing half of the L4 algebra of folds (do-NOT-merge over-unification guard).
- [`eigsolve`](./eigsolve.md) — the `Solve`-monadic outer-driver **cap** for the generalized eigenproblem:
```

with (inserting the `nrm2` bullet between):

```text
The next-pull operator-operand consumer is the driven [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (c069, GATED on this entry). Sibling of [`inner_product`](./inner_product.md) — the tensor-producing half of the L4 algebra of folds (do-NOT-merge over-unification guard).
- [`nrm2`](./nrm2.md) — the **Euclidean-norm verb** `α = ‖x‖₂ = √⟨x, x⟩`; one of the **kept named abstractions** (directive-2 disposition-2 keep-and-rise) risen to L4 as a named verb — the literature-standard unit a solver description wants as residual `nrm2(r)` / the Arnoldi sub-diagonal `H[j+1,j] = nrm2(w)`. A **CONSUMER** of the [`inner_product`](./inner_product.md) combinator (`√ ∘ abs ∘ inner_product` at the diagonal `y = x`), **NOT a fold member** — the do-NOT-merge over-unification guard (split-additivity is lost under `√`, the defining reason it is a consumer). Identity-in-form on the body to [`L3/nrm2`](../L3/nrm2.md) (no dedicated L4>L3 theme — the in-line-marker route); the `abs` defensive guard preserved as an explicit scalar-map detail; element-type collapsed (result always real ≥ 0). Rises alongside the combinator as the permitted dual, `concepts/black-box-vs-accelerated-kernels.md` §2.
- [`eigsolve`](./eigsolve.md) — the `Solve`-monadic outer-driver **cap** for the generalized eigenproblem:
```

**Block 4 — `dot` dep-map row (alpha position: after the `chebyshev` dep-map row at index line 81, before the `solve_loop` row at :82).** Anchor on the end of the `chebyshev` row + the start of `solve_loop`. (The `chebyshev` row text is long; the unique anchor is the `solve_loop` row's leading text — the new `dot` row is inserted immediately before it.)

```edit:book/src/L4/index.md
| `solve_loop` | `solve_loop :: OpParams -> Inputs -> Solve ()`; entry `solve op inp = execState (solve_loop op inp) initial_state`. Outer driver: tail-recurses `do { o <- restart_cycle op inp; unless (done o) (solve_loop op inp) }` (`one_cycle` for non-restarted solvers) until the returned `Outcome` says stop. | Concepts: `solve-monad`, `state-stratification`, `convergence-test`. L4 rows: `restart_cycle` (the per-cycle body it recurses on); `Outcome` (its termination signal); sits *above* [`iterate-while`](./iterate-while.md) (the inner kernel-fold `restart_cycle` runs). | L3 explicit `iterate_while_L3` outer tail-recursion + positional `(K, s)` threading per [`L3/ksp_solve`](../L3/ksp_solve.md):142 (the `Solve` monad dissolves; `do`/`unless` ↦ the predicate's read of `s.converged`). L4>L3 theme rides the `L4/ksp_solve` cap (cycle-048). | `firm` (outer-driver vocabulary anchor; cycle-047 — specified from [`solve-monad`](../concepts/solve-monad.md) §Shape + strawman §§3.6–3.7; first-two consumers [`L3/ksp_solve`](../L3/ksp_solve.md), [`L3/eigsolve`](../L3/eigsolve.md); per-operator laws ride the forthcoming `L4/ksp_solve` cap) |
```

with (inserting the `dot` row before `solve_loop`):

```text
| [`dot`](./dot.md) | `dot :: Tensor[N] -> Tensor[N] -> Scalar`; `tdot :: Tensor[N] -> Tensor[N] -> Scalar` (unconjugated complex-only). `dot x y = inner_product x y` at `M = I` with the Hermitian/symmetric kernel (`xᴴ y`, conjugate-linear in arg-1). The kept named inner-product verb a CG/GMRES description spells `dot(p, Ap)`. Pure value-producing reduction — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (§2 kept-named-abstraction rises), `dot` (element-type / BLAS-1 heritage). L4 rows: re-expresses through [`inner_product`](./inner_product.md) at `M = I` (the parent combinator, the permitted dual; `dot` is its Hermitian/symmetric **specialization**). | L3 [`dot`](../L3/dot.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the `inner_product`/`eigsolve`/`chebyshev` in-line-marker route); substantive translation is the L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) (conjugation dispatch + the `xᴴ y` ↔ `yᴴ x` re-order + pinned reduction trees). | `firm` (cycle-069 D2 — risen from firm [`L3/dot`](../L3/dot.md) through firm [`inner_product`](./inner_product.md); the kept named abstraction that rises to L4 as a named verb alongside the combinator, `concepts/black-box-vs-accelerated-kernels.md` §2; laws carried up unchanged / syntactic-identity escape; `tdot` type-API-surface-only caveat inherited) |
| `solve_loop` | `solve_loop :: OpParams -> Inputs -> Solve ()`; entry `solve op inp = execState (solve_loop op inp) initial_state`. Outer driver: tail-recurses `do { o <- restart_cycle op inp; unless (done o) (solve_loop op inp) }` (`one_cycle` for non-restarted solvers) until the returned `Outcome` says stop. | Concepts: `solve-monad`, `state-stratification`, `convergence-test`. L4 rows: `restart_cycle` (the per-cycle body it recurses on); `Outcome` (its termination signal); sits *above* [`iterate-while`](./iterate-while.md) (the inner kernel-fold `restart_cycle` runs). | L3 explicit `iterate_while_L3` outer tail-recursion + positional `(K, s)` threading per [`L3/ksp_solve`](../L3/ksp_solve.md):142 (the `Solve` monad dissolves; `do`/`unless` ↦ the predicate's read of `s.converged`). L4>L3 theme rides the `L4/ksp_solve` cap (cycle-048). | `firm` (outer-driver vocabulary anchor; cycle-047 — specified from [`solve-monad`](../concepts/solve-monad.md) §Shape + strawman §§3.6–3.7; first-two consumers [`L3/ksp_solve`](../L3/ksp_solve.md), [`L3/eigsolve`](../L3/eigsolve.md); per-operator laws ride the forthcoming `L4/ksp_solve` cap) |
```

**Block 5 — `nrm2` dep-map row (alpha position: after the `linear_combination` dep-map row at index :87, before the `eigsolve` row at :88).** Anchor on the end of the `linear_combination` row + the start of `eigsolve` (the unique anchor is the `eigsolve` row's leading text — the new `nrm2` row is inserted immediately before it):

```edit:book/src/L4/index.md
| [`eigsolve`](./eigsolve.md) | `eigsolve :: OpParams -> Inputs -> EigState`; entry `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`. The `Solve`-monadic outer-driver cap for the generalized eigenproblem — a **role-naming `EigOutcome`-wrapper over an opaque-library obstruction marker** (the eigen-iteration is library-owned; the cap names `eigen_iterate` by role and marks the `sequential-obstruction`, NOT a `solve_loop`/`restart_cycle` tail-recursion). | Concepts: `solve-monad`, `state-stratification`, `sequential-obstruction` (the load-bearing opaque-library obstruction), `tensor-field-lift`, `variant-absorption`, `constructed-operators`, `solver-as-operator`, `convergence-test`. L4 rows: `solve_loop` (specialised to a single opaque step + classification), `Outcome` (extended to `EigOutcome`), `EigOutcome` (the richer sum it produces); [`ksp_solve`](./ksp_solve.md) (sibling cap + inner solver `op.inv`); `restart_cycle` / [`iterate-while`](./iterate-while.md) by role-contrast only (the absent Palace-loop analogs). | L3 [`eigsolve`](../L3/eigsolve.md) (`partial-obstruction`) via an **in-line marker-erasure** (NO dedicated L4>L3 theme — the eigen-iteration is opaque-library-owned, marked-not-rendered at both layers; the `Solve`/`EigOutcome` wrapper erases, the obstruction marker is preserved; parallel to `chebyshev`'s in-line-by-design L4>L3). | `firm` (harvested cycle-048 R3; the L4 driver-half cap over the `partial-obstruction` L3 eigsolve, consuming the cycle-047 outer-driver vocabulary anchor under the opaque-library constraint; closes the `eigsolve` half of OQ `l4-ksp-solve-eigsolve-caps-gated-on-solve-monad-outer-driver-vocabulary`; re-anchors the seven stale `L3/eigsolve` §Upward "no L4 cap" assertions) |
```

with (inserting the `nrm2` row before `eigsolve`):

```text
| [`nrm2`](./nrm2.md) | `nrm2 :: Tensor[N] -> Scalar`; `nrm2 x = sqrt (abs (inner_product x x))`. The kept named 2-norm verb `‖x‖₂ = √⟨x, x⟩` — `√ ∘ abs ∘ inner_product` at the diagonal `y = x`. A **CONSUMER** of the combinator, NOT a fold member (split-additivity lost under `√` — the do-NOT-merge guard). Result always real ≥ 0. Pure value-producing scalar map on a pure reduction — no `Solve` monad / carry / predicate. | Concepts: `black-box-vs-accelerated-kernels` (§2 kept-named-abstraction rises), `nrm2` (BLAS-1 heritage). L4 rows: **consumes** [`inner_product`](./inner_product.md) at the diagonal (the permitted dual — `nrm2` is a consumer verb, NOT a member; combinator law 5 PSD-at-diagonal is the √ well-definedness witness); sibling named verb [`dot`](./dot.md). | L3 [`nrm2`](../L3/nrm2.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3 theme** — in-line §"Downward to L3", the in-line-marker route); substantive downward content is the L1>L0 [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) (the four-stage chain + the `abs`-guard classification) + the inner reduction's L2>L1 fold-specialization. | `firm` (cycle-069 D2 — risen from firm [`L3/nrm2`](../L3/nrm2.md) as the diagonal consumer of firm [`inner_product`](./inner_product.md); the kept named abstraction that rises to L4 as a named consumer verb, `concepts/black-box-vs-accelerated-kernels.md` §2; the five norm laws are syntactic identities / standard norm facts / syntactic-identity escape; the `abs` defensive guard preserved) |
| [`eigsolve`](./eigsolve.md) | `eigsolve :: OpParams -> Inputs -> EigState`; entry `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`. The `Solve`-monadic outer-driver cap for the generalized eigenproblem — a **role-naming `EigOutcome`-wrapper over an opaque-library obstruction marker** (the eigen-iteration is library-owned; the cap names `eigen_iterate` by role and marks the `sequential-obstruction`, NOT a `solve_loop`/`restart_cycle` tail-recursion). | Concepts: `solve-monad`, `state-stratification`, `sequential-obstruction` (the load-bearing opaque-library obstruction), `tensor-field-lift`, `variant-absorption`, `constructed-operators`, `solver-as-operator`, `convergence-test`. L4 rows: `solve_loop` (specialised to a single opaque step + classification), `Outcome` (extended to `EigOutcome`), `EigOutcome` (the richer sum it produces); [`ksp_solve`](./ksp_solve.md) (sibling cap + inner solver `op.inv`); `restart_cycle` / [`iterate-while`](./iterate-while.md) by role-contrast only (the absent Palace-loop analogs). | L3 [`eigsolve`](../L3/eigsolve.md) (`partial-obstruction`) via an **in-line marker-erasure** (NO dedicated L4>L3 theme — the eigen-iteration is opaque-library-owned, marked-not-rendered at both layers; the `Solve`/`EigOutcome` wrapper erases, the obstruction marker is preserved; parallel to `chebyshev`'s in-line-by-design L4>L3). | `firm` (harvested cycle-048 R3; the L4 driver-half cap over the `partial-obstruction` L3 eigsolve, consuming the cycle-047 outer-driver vocabulary anchor under the opaque-library constraint; closes the `eigsolve` half of OQ `l4-ksp-solve-eigsolve-caps-gated-on-solve-monad-outer-driver-vocabulary`; re-anchors the seven stale `L3/eigsolve` §Upward "no L4 cap" assertions) |
```

```edit:book/src/SUMMARY.md
- [linear_combination](./L4/linear_combination.md)
- [eigsolve](./L4/eigsolve.md)
```

with (inserting `dot` and `nrm2` in alpha position within the L4 group — the current SUMMARY L4 list is insertion-ordered, not alpha; per directive-3 the by-kind alpha-within-group reorg is a deferred meta-phase pass, so I insert the two new chapters at a stable, link-resolving position after the data-algebra combinators they re-express through, leaving the global reorg to the meta-phase):

```text
- [linear_combination](./L4/linear_combination.md)
- [dot](./L4/dot.md)
- [nrm2](./L4/nrm2.md)
- [eigsolve](./L4/eigsolve.md)
```

## Operator content

The two firm chapter bodies are authored in full **inside the `new:` fenced blocks above** (the complete `## Status` + Signature + Semantics + Algebraic-laws + Variant-axes + Downward-to-L3 + Evidence apparatus is enclosed in each block; inner code samples are rendered as 4-space-indented blocks, not nested ` ``` ` fences, per the fence-parity guard). Summary of each:

- **`dot`** (`book/src/L4/dot.md`, status `firm`) — `dot :: Tensor[N] -> Tensor[N] -> Scalar`, the Hermitian/symmetric inner-product verb `= inner_product x y` at `M = I`. A **specialization** of the firm combinator `L4/inner_product` (re-expressed THROUGH it, not re-derived), value-thread-isomorphic to firm `L3/dot`. Six algebraic laws carried up unchanged (empty-axis, split-additivity, conjugate-linearity, Hermitian symmetry, PSD-at-diagonal — the law `nrm2` rests on, zero-in-either-argument); conjugation × element-type variant profile (`tdot` the type-API-surface-only co-variant). Identity-in-form L4>L3, in-line-marker route (no theme file).

- **`nrm2`** (`book/src/L4/nrm2.md`, status `firm`) — `nrm2 :: Tensor[N] -> Scalar`, the Euclidean-norm verb `= √(abs(inner_product x x))` at the diagonal `y = x`. A **CONSUMER** of the firm combinator `L4/inner_product`, **NOT a fold member** (the do-NOT-merge over-unification guard — split-additivity is lost under `√`, the defining reason it is a consumer). Five laws (non-negativity, empty-axis, absolute homogeneity, triangle inequality, defining-identity); the homomorphism explicitly does NOT hold; the `abs` defensive guard preserved as an explicit scalar-map detail; element-type collapsed (result always real ≥ 0). Identity-in-form L4>L3, in-line-marker route (no theme file).

## Supporting evidence

- **Combinator the verbs re-express through (firm c068 D3):** `book/src/L4/inner_product.md` — its §"Specializations" (`:117-138`) already names `dot(x, y) = inner_product x y` as the Hermitian/symmetric specialization and `nrm2`/`matrix-weighted-norm` as the §"Consumer (NOT an instance)" (`:203-218`) consumers (the do-NOT-merge boundary). This dispatch lands the first-class named-verb homes those notes point at.
- **Sibling named-verb-style L4 rise precedent (firm c068 D3):** `book/src/L4/linear_combination.md` — the combinator-rises + members-as-notes + identity-in-form-L4>L3 + firm-on-positive-structure-escape shape, followed verbatim here.
- **Firm L3 named abstractions below (verified on disk this dispatch):** `book/src/L3/dot.md` (specialization-stub, `M = I` Hermitian/symmetric specialization of the L3 combinator) + `book/src/L3/nrm2.md` (consumer-stub, `√∘abs∘inner_product` at the diagonal, NOT a fold member). Both `firm`; their carve-out framing preserved verbatim at L4.
- **Disposition source:** `book/src/concepts/black-box-vs-accelerated-kernels.md` §2 "Kept named abstraction — rises" (`:88-109`) — names `dot` (`:102-104`) and `nrm2` (`:105-106`) as confirmed keeps that rise to L4 as named verbs alongside the rising combinator (the permitted dual). §"The combinators rise regardless" (`:128-136`) confirms the combinator rises in all cases.
- **L0 transitive anchors (citecheck `--anchor` confirmed on disk this dispatch):** `palace/linalg/vector.cpp:263-267` (`Dot`, anchor at `:263`); `palace/linalg/vector.hpp:255-260` (`Norml2`, anchor at `:257`; body `:259` = `std::sqrt(std::abs(Dot(comm, x, x)))`). Both inherited transitively through the firm L3/L1 leaves (the `L4/inner_product` precedent of NOT re-localizing L0).
- **Count basis (c057-meta guard):** firm L4 chapters counted from each linked chapter's `## Status` line on disk this dispatch — 10 firm before this cycle (chebyshev, eigsolve, fe_assemble, fold_solve, inner_product, iterate-while, iterate-while-with-prev, krylov-step, ksp_solve, linear_combination), `solve_family` rough-in, 4 outer-driver anchors. With D1's `assemble_frequency_operator` (firm standalone L4 chapter, `firmness: firm` — +1) + my `dot` + `nrm2` (+2), the firm tally is **13 + 4 outer-driver**. (Repairer note c069: D1 confirmed firm at critique-time — the prior `12 + 4` conditional fallback is struck; D1 must integrate before D2 so the `./assemble_frequency_operator.md` L4-relative target in the tally resolves on disk.)

## Open questions / caveats

- **D1 `assemble_frequency_operator` count + integration order (RESOLVED at critique-time; repairer-confirmed c069):** D1 landed `assemble_frequency_operator` as a standalone firm L4 chapter (`book/src/L4/assemble_frequency_operator.md`, `firmness: firm` — confirmed by the critic against D1's sibling report), so the unconditional **`13 + 4 outer-driver`** count is correct and the prior `12 + 4` conditional fallback has been **struck** from the tally edit (block 1), the count-basis bullet, and here. The tally edit (block 1) links the slug as `./assemble_frequency_operator.md` (L4-relative — the new firm D1 chapter, NOT the old `../L1/` path). **Integration-ordering requirement: D1 must be applied before D2** so the `./assemble_frequency_operator.md` target is on disk when D2's index edit lands (else `linkcheck2` breaks). I do NOT author D1's row/bullet — D1 owns those; the tally prose links its chapter by the planner's canonical slug `assemble_frequency_operator`.
- **dot/nrm2 paired-cohort vs split — RESOLVED as a clean pair (no split warranted).** The planner flagged that either verb might carry non-trivial distinct content warranting a follow-on split. On authoring: both are thin re-expressions through the single firm `L4/inner_product` (one a specialization at `M = I`, one a diagonal consumer under `√ ∘ abs`), each fitting one chapter cleanly; the pairing is justified (two named verbs over one combinator, not two combinators). **No split needed.** The genuine distinction between them — `dot` is a *specialization* of the combinator, `nrm2` is a *consumer* of its output (the do-NOT-merge boundary) — is captured by their distinct §"Relationship to inner_product" sections, not by splitting the dispatch.
- **SUMMARY.md / dep-map alpha-position vs the deferred directive-3 reorg.** The L4 SUMMARY group and the index dep-map table are currently insertion-ordered, NOT alphabetized (the directive-3 by-kind sub-chapter grouping + global alpha re-sort is a deferred meta-phase structural pass, OQ `concepts-list-global-alpha-resort-vs-local-cluster-insert`). I inserted the two new SUMMARY entries + two dep-map rows at stable link-resolving positions (after the data-algebra combinators they re-express through) rather than forcing a partial alpha-sort that would conflict with the meta-phase's one-time reorg. The §Vocabulary-cohort BULLETs ARE placed in alpha position within the cohort list per the dispatch spec (`dot` after `chebyshev`; `nrm2` after `linear_combination`). Flagged so the integrator does not read the non-alpha dep-map/SUMMARY insert as a positioning defect.
- **Staleness pointers on firm L3 dot/nrm2 (out of this dispatch's scope — D-cohort note).** `L3/dot.md:7-8` + `:107-110` and `L3/nrm2.md:7-8` + `:135-139` still assert "no L4 entry — leaf primitives are not first-class L4 vocabulary (cycle-010 audit verdict)." With this dispatch's `L4/dot` + `L4/nrm2` on disk those lines are now **stale** (the same staleness class D3 this cycle re-anchors for `L3/linear_combination`/`L3/inner_product`). This is OUT of my write-scope (one-operator-per-dispatch; the L3 entries are not mine to edit) — flagged for a follow-on thin lifter re-anchor pass (the `eigsolve`/c068 D3 precedent routine). Recommend the batch-21 meta-phase or a c070 lifter pick this up; the trigger is now firm (the L4 entries the L3 lines deny are on disk). Layer-intro-author note: the `L3/index.md` BLAS-1 cohort framing ("no-L4-by-design") may also need the same per-case correction `L4/index.md:71` already carries.
