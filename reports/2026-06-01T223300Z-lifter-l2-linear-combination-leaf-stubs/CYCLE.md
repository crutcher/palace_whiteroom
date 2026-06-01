---
agent: lifter
invoked_at: 2026-06-01T223300Z
scope: L2 linear_combination-family leaf reduce-to-stub — scal / axpy / axpby / axpbypcz
status: pending
integrated_at: 2026-06-02T010000Z
integration_commit: 9633c134b333932b31f2823c558398fafdaa9750
integration_notes: "cycle-052 D1 — applied clean (full-file overwrite reduce-to-stub for 4 L2 linear_combination leaves; old 365–449-line bodies removed, unique L0 anchors retained); no build-repair needed; refactor pass COMPLETE."
inputs:
  - book/src/L2/scal.md
  - book/src/L2/axpy.md
  - book/src/L2/axpby.md
  - book/src/L2/axpbypcz.md
  - book/src/L2/linear_combination.md
  - skills/deleted-slug-inbound-live-link-sweep/SKILL.md
---

# CYCLE: Re-anchor (reduce-to-stub) the four L2 linear_combination leaf chapters

## Summary

Under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, the L2 entry for the BLAS-1
scalar-weighted-sum family is the firm fold-combinator
[`linear_combination`](../../book/src/L2/linear_combination.md) (cycle-018; already
re-anchored cycle-050 to carry the §"Arity specializations" notes for the four members).
The four standalone L2 leaf chapters `scal` / `axpy` / `axpby` / `axpbypcz` (365 / 406 /
437 / 449 lines) are the **retired rectangular pattern**: full firm bodies duplicating the
combinator's semantics, algebraic-laws, fusion-note, and variant-axis prose, each framed as
a "same-named L2 floor mirrored beside the combinator" — exactly the floor the redirect
supersedes ("a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern", `book/src/L2/linear_combination.md:27-28`).

This dispatch REDUCES each of the four to a **specialization-stub** (information-non-lossy;
NOT a full delete — the file is KEPT so all inbound links stay live by construction). Each
stub keeps `## Status: firm` (it is a firm specialization pointer up to the combinator),
carries (a) the one-line "arity-`N` specialization of `linear_combination`" with a live link
up to the combinator entry + its §"Arity specializations" note, (b) the operator's UNIQUE L0
citation anchors (those the combinator's Evidence section does NOT already carry) + its one
output-aliasing / element-type variant-axis row (the aliasing axis recorded as the FOLD's),
and (c) DEFERS all semantics / algebraic-laws / fusion prose up to `linear_combination`. The
duplicated body is deleted. This completes the rectangular-residue removal for the L2
`linear_combination` family.

## Proposed changes

Each block below is a **full-file-overwrite** of its target chapter (the entire block body
IS the new file content, frontmatter through §Evidence — the integrator applies it via
`Edit` full-replace, not an anchor swap, so the old duplicated firm body is fully replaced).
The inner signature samples are rendered as 4-space-indented code blocks (not nested fences)
per the flat-CommonMark fence discipline, so each `edit:` fence stays balanced.

```edit:book/src/L2/scal.md
---
layer: L2
operator: scal
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-1 member — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/scal.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-α-against-complex-x)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# scal

**`scal` is the arity-1 specialization of
[`linear_combination`](./linear_combination.md)** — the L2 entry for the BLAS-1
scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The family speaks
through the combinator at L2 and above; `scal(α, x) = linear_combination [(α, x)]` (the
single-term list), recorded as the arity-1 readout label in
[`linear_combination` §"Arity specializations"](./linear_combination.md). All
semantics, the algebraic laws (the arity-1 shadow of the combinator's multilinearity /
coefficient-scaling laws), the fusion note (the degenerate single-term seed-and-accumulate),
and the variant-axis treatment are the combinator's — **deferred to
[`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-1 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row so the family's per-arity L0 navigation stays resolvable
from a real file. The L1 leaf [`scal`](../L1/scal.md) stays firm (it carries the
load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md)).

## Signature

    scal :: Scalar -> Tensor[N] -> Tensor[N]
    scal α x = α·x = linear_combination [(α, x)]

Arity-1 instance of the combinator's
`linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`
(`linear_combination.md` §Signature). The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `α`
  against complex `x` via the internal `si == 0.0` branch at `vector.cpp:207-211`. Inherited
  from the combinator's element-type axis; absorbed at construction, not in the positional
  signature.
- **output-aliasing** (in-place `x *= α` vs fresh-output) is the **FOLD's** variant axis
  (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; at L2 this
  specialization is pure / out-of-place, aliasing being an L2>L1 lowering concern.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect: a same-named base-form floor mirrored beside the combinator was the retired
rectangular pattern ([`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence). The L0 anchors UNIQUE to the
arity-1 readout label (those the combinator's Evidence does not already carry; retained here
so they stay navigable):

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)`
  declaration with comment `Scale all entries by s.` (the arity-1 L0 symbol).
- `palace/linalg/vector.cpp:207-211` — the `if (si == 0.0)` real fast-path branch inside
  `ComplexVector::operator*=` (`vector.cpp:203-227`, the arity-1 site the combinator
  Evidence carries) — the internal scalar-promotion site (real-into-complex), the L0 anchor
  for the scalar-promotion sub-axis.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template
  (`auto norm = Norml2(comm, x); … x *= 1.0 / norm; return norm;`) — the fused `nrm2 + scal`
  construct that the firm L2 [`normalize`](./normalize.md) composite factors as
  `scal(1/nrm2(x), x)`; the arity-1 `scal` site in the wild.

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor` + `--show`,
2026-06-01. The shared arity-1 site `vector.cpp:203-227` and `iterative.cpp:632` are in the
combinator's Evidence.)
```

```edit:book/src/L2/axpy.md
---
layer: L2
operator: axpy
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-2 member, second coefficient fixed to 1 — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpy.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpby-mutation-rotation` sub-pattern A, the β=1 specialization)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-α-against-complex-x)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpy

**`axpy` is the arity-2 specialization of
[`linear_combination`](./linear_combination.md)** with the **second coefficient fixed to
1** — the L2 entry for the BLAS-1 scalar-weighted-sum family (vocabulary-shift redirect
2026-06-01). The family speaks through the combinator at L2 and above;
`axpy(α, x, y) = linear_combination [(α, x), (1, y)]`, recorded as the arity-2 readout label
in [`linear_combination` §"Arity specializations"](./linear_combination.md). The fixed-1
`y`-coefficient is exactly what distinguishes `axpy` from the free-second-coefficient
`axpby` at the same arity. All semantics, the algebraic laws (the arity-2 shadow of the
combinator's concatenation-homomorphism / multilinearity laws), the fusion note (the
two-term single-aligned pass), and the variant-axis treatment are the combinator's —
**deferred to [`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-2 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpy`](../L1/axpy.md) stays firm (it carries
the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A).

## Signature

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y = linear_combination [(α, x), (1, y)]

Arity-2 instance (second coeff fixed 1) of the combinator's
`linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`
(`linear_combination.md` §Signature). The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `α`
  against complex `x, y` via the real-α-on-complex-vector forwarding overload at
  `vector.cpp:714-718`. Inherited from the combinator's element-type axis; absorbed at
  construction.
- **output-aliasing** (in-place `y ← α·x + y` vs fresh-output) is the **FOLD's** variant
  axis (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; at L2 this
  specialization is pure / out-of-place.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect (a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern — [`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:702-712`
real-real `AXPY` site with the `α == 1.0` fast-path and the `vector.hpp:305-307` decl are
carried there). The L0 anchors UNIQUE to the arity-2 readout label (retained here so they
stay navigable):

- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` (and `Add` / `Subtract`
  aliases) member declaration, comment `In-place addition (*this) += alpha * x.`
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels (`YR[i] += ar·XR[i] − ai·XI[i]`).
- `palace/linalg/vector.cpp:714-718` — `AXPY(double, ComplexVector, ComplexVector)`, the
  real-α-on-complex-vector forwarding overload (the scalar-promotion sub-axis L0 anchor).
- `palace/linalg/vector.cpp:720-724` — `AXPY(std::complex<double>, ComplexVector,
  ComplexVector)`, the complex-α overload forwarding to the member `ComplexVector::AXPY`.

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
```

```edit:book/src/L2/axpby.md
---
layer: L2
operator: axpby
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-2 member, general second coefficient — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpby.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpby-mutation-rotation`)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-(α,β)-against-complex-vectors)
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpby

**`axpby` is the arity-2 specialization of
[`linear_combination`](./linear_combination.md)** (general second coefficient) — the L2
entry for the BLAS-1 scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The
family speaks through the combinator at L2 and above;
`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`, recorded as the arity-2 readout
label in [`linear_combination` §"Arity specializations"](./linear_combination.md). The free
second coefficient `β` is what distinguishes `axpby` from the fixed-1 `axpy` at the same
arity. All semantics, the algebraic laws (the arity-2 shadow of the combinator's
concatenation-homomorphism / multilinearity / coefficient-scaling laws — the per-op
bilinearity is the multilinearity law read at list-length 2), the fusion note (the fused
`α·x + β·y` single-aligned `add(α,x,β,y,y)` pass), and the variant-axis treatment are the
combinator's — **deferred to [`linear_combination`](./linear_combination.md), not
re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-2 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpby`](../L1/axpby.md) stays firm (it
carries the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)).

## Signature

    axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpby α x β y = α·x + β·y = linear_combination [(α, x), (β, y)]

Arity-2 instance (general second coeff) of the combinator's
`linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`
(`linear_combination.md` §Signature). The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real `(α, β)`
  against complex `x, y` (promote all-or-none) via the real-scalar-on-complex-vector overload
  at `vector.cpp:739-743`. Inherited from the combinator's element-type axis; absorbed at
  construction.
- **output-aliasing** (in-place `y ← α·x + β·y` vs fresh-output) is the **FOLD's** variant
  axis (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; at L2 this
  specialization is pure / out-of-place.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect (a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern — [`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:726-730`
real-real `AXPBY` → MFEM `add(α,x,β,y,y)` fusion-pass site and the `vector.hpp:309-311` decl
are carried there). The L0 anchors UNIQUE to the arity-2 (general) readout label (retained
here so they stay navigable):

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member declaration, comment
  `In-place addition (*this) = alpha * x + beta * (*this).` (the receiver-mutating member
  form).
- `palace/linalg/vector.cpp:732-737` — complex-complex specialisation
  `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)`:
  delegates to the member form `y.AXPBY(alpha, x, beta)`.
- `palace/linalg/vector.cpp:739-743` — real-scalar-on-complex-vector specialisation
  `AXPBY(double, ComplexVector, double, ComplexVector)`: also delegates to the member form
  (implicit scalar promotion; the scalar-promotion sub-axis L0 anchor).

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
```

```edit:book/src/L2/axpbypcz.md
---
layer: L2
operator: axpbypcz
firmness: firm
specialization_of:
  - book/src/L2/linear_combination.md (arity-3 member — the L2 family entry; see its §"Arity specializations")
lowers_to:
  - book/src/L1/axpbypcz.md (identity-in-form; the L1 leaf carries the load-bearing one-to-one L0-symbol shape; L1>L0 in-place form is `axpbypcz-mutation-rotation`)
variant_axes:
  - element-type (real / complex; scalar-promotion sub-axis real-(α,β,γ)-against-complex-(x,y,z))
  - output-aliasing (the FOLD's axis — see linear_combination §Variant axes)
---

# axpbypcz

**`axpbypcz` is the arity-3 specialization of
[`linear_combination`](./linear_combination.md)** — the L2 entry for the BLAS-1
scalar-weighted-sum family (vocabulary-shift redirect 2026-06-01). The family speaks through
the combinator at L2 and above;
`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`, recorded as the
arity-3 readout label in
[`linear_combination` §"Arity specializations"](./linear_combination.md). It is the maximal
fixed-arity L0 symbol — combinations of more than three terms are open-coded in Palace as
iterated `axpbypcz`-into-output (the `γ=1` accumulate sites), which the variadic combinator
abstracts. All semantics, the algebraic laws (the arity-3 shadow of the combinator's
concatenation-homomorphism / multilinearity laws — the per-op trilinearity is the
multilinearity law read at list-length 3; the `γ==0` subsumption of `axpby` is the
combinator's zero-coefficient term-drop law 5, the exact algebraic content of the in-source
`γ==0` branch at `vector.cpp:749-751`), the fusion note (the arity-3 single-aligned pass /
`γ==0` arity-collapse), and the variant-axis treatment are the combinator's — **deferred to
[`linear_combination`](./linear_combination.md), not re-authored here**.

This chapter is retained as a **specialization-stub** (not a standalone L2 floor): the
arity-3 readout label for the bounded-arity L0 call shape, holding the operator's unique L0
anchors and its variant-axis row. The L1 leaf [`axpbypcz`](../L1/axpbypcz.md) stays firm (it
carries the load-bearing one-to-one L0-symbol shape for the L1>L0 mutation rotation
[`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)).

## Signature

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z = linear_combination [(α, x), (β, y), (γ, z)]

Arity-3 instance of the combinator's
`linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`
(`linear_combination.md` §Signature). The element-type / scalar-promotion sub-axis is
inherited unchanged from the combinator.

## Variant axes

- **element-type** (`real` | `complex`), with the `real ⊑ complex` scalar-promotion
  sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)) — real
  `(α, β, γ)` against complex `(x, y, z)` (promote all-or-none) via the
  real-scalar-on-complex-vector specialisation at `vector.cpp:767-772`. Inherited from the
  combinator's element-type axis; absorbed at construction.
- **output-aliasing** (in-place `z ← α·x + β·y + γ·z` vs fresh-output) is the **FOLD's**
  variant axis (`linear_combination.md` §Variant axes, axis 1), orthogonal to arity; the
  `γ=1` accumulate-into sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) are the
  fold's aliasing case (carried in the combinator's Evidence). At L2 this specialization is
  pure / out-of-place.

## Status

`firm` — specialization-stub pointing at the firm combinator
[`linear_combination`](./linear_combination.md) (cycle-018). Reduced from a standalone L2
floor to a specialization note cycle-052 (batch-16 refactor) per the vocabulary-shift
redirect (a same-named base-form floor mirrored beside the combinator is the retired
rectangular pattern — [`linear_combination`](./linear_combination.md) §Context).

## Evidence

The semantics / laws / fusion-note evidence is the combinator's
([`linear_combination`](./linear_combination.md) §Evidence; the shared `vector.cpp:749-751`
`γ==0` arity-collapse branch, the `vector.hpp:313-316` decl, and the `nleps.cpp:343-344` /
`romoperator.cpp:188-189` / `timeoperator.cpp:217` `γ=1`/`γ=0` live sites are carried there).
The L0 anchors UNIQUE to the arity-3 readout label (retained here so they stay navigable):

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member declaration, comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, Vector, double, Vector, double,
  Vector)` real-real specialisation with the `γ == 0` branch: fast-path delegates to MFEM's
  `add(alpha, x, beta, y, z)` (`:749-751`, the arity-collapse the combinator carries);
  slow-path splits into `AXPBY(alpha, x, gamma, z); z.Add(beta, y)` (`:755-756`).
- `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(std::complex<double>, ComplexVector, …)`
  complex-complex specialisation: delegates to member
  `z.AXPBYPCZ(alpha, x, beta, y, gamma)`.
- `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, …)`
  real-scalar-on-complex-vector specialisation: also delegates to the member form (implicit
  scalar promotion; the scalar-promotion sub-axis L0 anchor).

(All anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01.)
```

## Discipline notes

- **Pure reduce-to-stub, not authorship.** The four stubs make no new content claims: every
  semantic / law / fusion statement is deferred up to the firm combinator
  `linear_combination` (cycle-018, re-anchored cycle-050 to carry the §"Arity
  specializations" notes for exactly these four members,
  `book/src/L2/linear_combination.md:74-99`). The four arity mappings I wrote into each stub
  (`scal`=arity-1, `axpy`=arity-2 second-coeff-1, `axpby`=arity-2 general, `axpbypcz`=arity-3)
  are verbatim the combinator's §"Arity specializations" block
  (`book/src/L2/linear_combination.md:81-84`)
  — no new decisions.
- **Information-non-lossy retention.** Each stub RETAINS the operator's UNIQUE L0 anchors —
  the per-arity L0 symbol decls/defs/promotion-overloads that the combinator's Evidence
  section does NOT already carry — plus the one output-aliasing/element-type variant row. The
  combinator's Evidence carries the SHARED sites (`vector.cpp:749-751`, `:726-730`,
  `:702-712`, `:203-227`, `vector.hpp:305-316`, `nleps.cpp:343-344`,
  `romoperator.cpp:188-189`, `timeoperator.cpp:217`, `iterative.cpp:632`); I verified each
  retained anchor is NOT redundant with that set before keeping it, and explicitly named the
  shared sites in each stub's §Evidence as "carried there" so the navigation is complete
  without duplication.
- **scal-unique anchors preserved exactly as the dispatch directed.** `vector.hpp:98-99`
  (decl), `vector.hpp:262-270` (`linalg::Normalize`), `vector.cpp:207-211` (the `si == 0.0`
  scalar-promotion branch) are retained. `vector.cpp:203-227` is the combinator's (the arity-1
  `operator*=` site), so I did NOT re-list it as scal-unique — I named it as the parent range
  of the retained `:207-211` sub-anchor and noted it is in the combinator's Evidence.
- **Output-aliasing recorded as the FOLD's axis** (not a per-leaf axis), per each former
  leaf's own framing and `linear_combination.md` §Variant axes axis 1 — preserved in the
  reduced variant-row.
- **Status kept `firm`** on all four (the stub is a firm specialization pointer, per the
  dispatch directive (c)).
- **Inner code samples rendered 4-space-indented**, not nested fences, per the flat-CommonMark
  fence discipline (friction-ledger
  `firm-chapter-body-authored-outside-proposed-changes-fence` recurrence-2 / skill
  `convert-nested-fences-to-indented-code-in-proposed-changes-block`). Each `` ```edit `` fence
  encloses the full reduced body (frontmatter through §Evidence) as a **full-file-overwrite**
  (no `[old]`/`[new]` anchor markers — the block body is the complete new file content, so
  the integrator full-replaces rather than anchor-swaps and the old duplicated firm body is
  removed in full); no apparatus is stranded outside.
- **Citation self-verification** (skill `verify-citation-range` / `tools/citecheck`): all 16
  retained L0 anchors run through `citecheck --anchor` against on-disk
  `reference/palace/palace/linalg/vector.{hpp,cpp}`, 2026-06-01 — all `[ok]`. The one
  `[DRIFT]` on `vector.cpp:207-211 --anchor 'imag'` was spurious (citecheck matched
  `si = s.imag()` at the line-206 comment); `--show` confirmed `:207-211` IS the `if (si ==
  0.0)` real fast-path branch exactly as the prior body described — anchor token, not range,
  was the mismatch.

## Supporting evidence

- **Re-anchor target** (firm combinator the family speaks through):
  `book/src/L2/linear_combination.md` — §Context lines 21-29 (the redirect: combinator is the
  L2 family entry; same-named floor mirrored beside it is the retired rectangular pattern),
  §"Arity specializations" lines 74-99 (the four mappings), §Dependencies lines 219-223 (the
  cycle-050 replace-and-propagate map naming the scheduled collapse of these four chapters
  into the specialization notes), §Evidence lines 346-383 (the shared L0 anchor set).
- **Replace-and-propagate provenance**: `book/src/L2/linear_combination.md:222-223` points at
  `reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md`
  (the cycle-050 combinator-miner refactor pass that scheduled this leaf collapse).
- **Convention**: batch-15-ratified `collapsed-leaf-disposition-convention-cohort-wide`
  (REDUCE-TO-STUB, information-non-lossy).
- **Zero-dangling verification** (skill `deleted-slug-inbound-live-link-sweep`, used as a
  VERIFICATION gate, NOT a de-link sweep — no file deleted): see §Open questions for the full
  inbound-link enumeration result. Reduce-to-stub keeps all four files on disk, so every
  inbound live link (`SUMMARY.md:60-63`; `orthogonalize-variant-split.md:260` →
  `../L2/axpy.md`; `concepts/tensor-field-lift.md:30` → `axpy.md`; the many `./scal.md` /
  `./axpy.md` etc. same-dir links from `reciprocal`/`normalize`/`divfree-projector`/
  `elementwise_product`/`jacobi-smoother`/`index.md`) stays LIVE by construction.

## Open questions / caveats

- **Inbound-link sweep result (zero dangling, by construction).** Per the
  `deleted-slug-inbound-live-link-sweep` procedure run as a verification gate: enumerated all
  inbound LIVE markdown links to the four slugs. Hits — `SUMMARY.md:60-63` (the four TOC
  rows); `book/src/L3-L2/orthogonalize-variant-split.md:260` (`](../L2/axpy.md)`);
  `book/src/concepts/tensor-field-lift.md:30` (`](axpy.md)`); and the dense same-directory
  `](./scal.md)` / `](./axpy.md)` / `](./axpby.md)` / `](./axpbypcz.md)` links from
  `book/src/L2/{reciprocal,normalize,divfree-projector,elementwise_product,jacobi-smoother,index}.md`.
  Because this is REDUCE-TO-STUB (files KEPT), **zero of these dangle** — no `delete:` fence is
  emitted. Confirmed clean: 4 slugs, all inbound links resolve to retained files, 0 residual.
- **Stale line-pinpoint references into the deleted scal body (LOW-tier narrative residual,
  NOT build-breaking, NOT my scope).** `book/src/L2/normalize.md:11`, `:111`, `:141`, `:164`
  carry the prose/code-span reference `book/src/L2/scal.md:223-228` pointing at the former
  scal §Dependencies "Sibling subsumption" note (`Normalize(x) = scal(1/nrm2(x), x)`), which
  the reduction deletes. These are **bare code-span path references** (no `](...)` markdown
  link), so they are stale-but-NOT-breaking per the inbound-sweep skill's Tiers (linkcheck2
  does not check prose code-spans). I did NOT touch `normalize.md` (it is outside this
  dispatch's four-file scope and the count-owner D4 owns consolidated narrative). Flagging for
  a count-owner / micro-sweep follow-up: re-point those four pinpoints at the combinator's
  closing-of-that-OQ home or drop the line-range. Not a re-architecture — a bounded narrative
  re-anchor for a later pass.
- **`index.md` dep-map + consolidated narrative explicitly left to D4** (the count-owner) per
  the dispatch directive — `index.md` carries `](./scal.md)` etc. rows (lines 78-84, 121) and
  the "Fold-cohort boundary" / leaf-vs-fold working-notes that this redirect supersedes; those
  are D4's to reconcile, not this dispatch's. The frontmatter `fold_parent:` keys I replaced
  with `specialization_of:` are local to the four files; if D4's index narrative keys off the
  old `fold_parent` field name, that is a coordination point (flagged here, not resolved).
- **No signature/notation shift.** The combinator signature
  (`[(Scalar, Tensor[N])] -> Tensor[N]`) and the arity mappings are unchanged from the
  cycle-050 re-anchor; the lift stayed pure rewriting (high→low preserved: each stub's LHS is
  the L2 arity form, deferring to the L2 combinator, lowering to the L1 leaf). No abstractor
  reread needed.
