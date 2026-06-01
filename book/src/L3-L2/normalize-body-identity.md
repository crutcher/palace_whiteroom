# normalize-body-identity

The L3>L2 lowering theme for the fused vector-normalisation composite `normalize`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `normalize` is a fused whole-tensor
composite, not a step body, so the L3 [`normalize`](../L3/normalize.md) whole-tensor form lowers into the
L2 [`normalize`](../L2/normalize.md) floor form by the identity on the composite itself. There is no
`(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform (the two surface adjustments
the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper);
`normalize` has no wrapper. The body IS the identity. This is the **fused-composite** analogue of the
leaf-primitive [`reciprocal-body-identity`](./reciprocal-body-identity.md) and
[`scal-body-identity`](./scal-body-identity.md), and — like those, and unlike the fold-member BLAS-1 leaves
— **fold-parent-free**: there is no fold-parent at L2 for the composite's fusion content to belong to. The
one structural difference from the standalone-leaf siblings is that `normalize` carries genuine same-layer
L2 dependencies (`nrm2` + `scal`, cited as `consumes`) — it is a *composite*, not a leaf — but the body
edge is identity nonetheless because the law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`
is the same at L3 and L2.

## Slug

`normalize-body-identity`

## Context

The `normalize` lowering relationships span three adjacent layers, all identity-in-form because `normalize`
is a fused whole-tensor composite with no iteration view and no genuine kernel fusion:

- **L3 form** ([`L3/normalize`](../L3/normalize.md), firm cycle-039) — the whole-tensor fused composite
  `normalize :: Tensor[N] -> (Scalar, Tensor[N])`, the iteration-rotation rendering. Carries **no iteration
  view** (fused leaf composite, not a step body) and **no sequential obstruction** (the norm sub-step is
  the parallel `nrm2` reduction, the rescale sub-step is the embarrassingly-parallel `scal`). Partial at
  `x = 0`. The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/normalize`](../L2/normalize.md), firm cycle-043 D9) — the fusion-rotation floor: the
  fused `nrm2 ∘ scal` composite. **No fold-parent** (a fused composite whose codomain `(Scalar, Tensor[N])`
  is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), with two genuine same-layer constituent floors
  cited as `consumes`. The RHS of this theme.
- **L2>L1 form** ([`L2-L1/normalize-leaf-identity`](../L2-L1/normalize-leaf-identity.md), firm cycle-043
  D10) — the onward edge into the L1 operator; also identity-in-form.

This theme is the **fused-composite counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and a direct sibling of
[`reciprocal-body-identity`](./reciprocal-body-identity.md) and
[`scal-body-identity`](./scal-body-identity.md) (cycle-041/042). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its point-3
applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives as L3-native
by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at L2. This is what
makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step." `normalize` is the
**fused-composite** realization of the same classification: its signature
`Tensor[N] -> (Scalar, Tensor[N])` exposes no per-element loop (the norm reduction is the `nrm2` consumer's
single semantic step; the rescale is element-local), so it is L3-native by the identical signature criterion
— the body is the identity, **and there is no wrapper at all** — `normalize` is not a step body, so the two
wrapper adjustments the `krylov-step` theme carries have no analog here. The one difference from the
standalone-*leaf* siblings (`reciprocal-body-identity`, `scal-body-identity`): `normalize` is a *composite*
with two genuine same-layer constituents (`nrm2` + `scal`), not a single leaf — but a composite with no
fold-parent, so the fork-independence is preserved and the body edge is still the identity.

The firm L3 entry (`book/src/L3/normalize.md:27,131` §"Downward"/"Lowers to") currently records its lowering
as direct L3>L1 identity-in-form ("no interposed L2 entry and no `L3-L2`/`L3-L1` theme file") via the
non-adjacent in-line convention, because no L2 `normalize` chapter existed. With the L2 `normalize` floor now
present (D9), this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's §"Lowers to" had to
skip — so the L3 composite lowers to an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants
**Identity-lowerings still require both L levels**) rather than non-adjacently to L1. (The L3 entry's
§27/§131 notes go stale once the D9 floor + this theme land; the re-anchor is a downstream-consistency touch
routed to the c044 sweep — see §Open questions.)

## L3 form (LHS)

The L3 whole-tensor form ([`L3/normalize`](../L3/normalize.md) §Signature, firm cycle-039):

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (β, x/β)   where  β = nrm2 x,  β > 0

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `x : Tensor[N]` a single
length axis, read-only at L3; result `(β, û)` with `β = nrm2(x)` the norm (always real, positive) and
`û = scal(1/β, x)` the unit vector (same axis, same element type). The defining factorisation is law 6:
`normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. Partial at `x = 0` (the precondition `x ≠ 0`, recorded
once). The operator carries **no iteration view** (fused leaf composite, not a step body) and **no
sequential obstruction** (the norm sub-step is the parallel `nrm2` reduction — clean at L3; the rescale
sub-step is the embarrassingly-parallel element-local `scal`). No L4 wrapper machinery applies (fused leaf
composites appear inside L4 operator bodies as let-bindings, not first-class L4 typed-wrapper anchors — the
cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 / operator-to-data cohort).

## L2 form (RHS)

The L2 floor form ([`L2/normalize`](../L2/normalize.md) §Signature, firm cycle-043 D9):

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (nrm2 x, scal (1 / nrm2 x) x)        -- law 6, the fused norm-then-rescale composite

The fused vector-normalisation composite in the fusion-rotation vocabulary — a **fused composite with NO
fold-parent** (codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`),
citing the two firm same-layer floors [`nrm2`](../L2/nrm2.md) (the norm, a consumer-of `inner_product`) and
[`scal`](../L2/scal.md) (the rescale, the arity-1 member-of `linear_combination`) as `consumes`. The
signature is **textually identical to the L3 form** modulo notation; the law-6 factorisation is the same
fused composition. The six algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic
laws — both inherit the L1 operator's six laws). There is **no fold-level fusion note** to carry (no
fold-parent) and **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the
norm pass from the rescale pass — the L2-genuine content is fusion-*naming*, not de-fusion); at L3 even the
reciprocal-vs-divide bit-difference drops below the whole-tensor resolution.

## The rewrite (L3 → L2)

The rewrite is the **identity on the fused composite's body**, with **no wrapper adjustment**:

    normalize x   (L3 whole-tensor fused composite)   ⇒   normalize x   (L2 fusion-rotation floor)

The body maps trivially — the same fused composition, same position, same dataflow, over the same two
constituents:

    | L3 form (`L3/normalize`)                          | L2 form (`L2/normalize`)                          | Mapping  |
    |---------------------------------------------------|---------------------------------------------------|----------|
    | `normalize x = (nrm2 x, scal (1/nrm2 x) x)` (whole-tensor fused composite; no iteration view) | `normalize x = (nrm2 x, scal (1/nrm2 x) x)` (fusion-rotation floor; NO fold-parent) | Identity. Same signature, same law-6 fused composition over the same two constituents (`nrm2` + `scal`). The only framing difference is documentary: L3 frames `normalize` as a whole-tensor fused composite in the iteration-rotation vocabulary; L2 frames the same operator as a fused `nrm2 ∘ scal` composition in the fusion-rotation vocabulary. No operational adjustment. |
    | partial: `x ≠ 0`                                  | partial: `x ≠ 0`                                  | Identity. Same partiality precondition (the `MFEM_ASSERT(norm > 0.0)`). |
    | algebraic laws 1–6                                | algebraic laws 1–6                                | Identity. Inherited unchanged across the chain. |
    | element-type variant axis                         | element-type variant axis                         | Identity. Real/complex collapsed; norm output always real, unit vector tracks input. |
    | consumes: `nrm2` + `scal` (NO fold-parent)        | consumes: `nrm2` + `scal` (NO fold-parent)        | Identity. The two same-layer constituents are cited unchanged across the edge; the composite has no fold-parent at either layer. |
    | no iteration view, no obstruction                 | no fold-parent, no genuine fusion                 | Identity. Nothing to rotate (composite, no loop) and nothing to de-fuse (no fold, no genuine kernel fusion — `linalg::Normalize` already separates the norm pass from the rescale pass). |

The mapping is total and bijective on the fused composite's body — the same single law-6 factorisation at
both layers, with the two constituent-floor citations preserved. This is the identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface adjustments
at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating into the L2
`IterState` record, and the L3 tail-recursive outer loop collapsing to the L2 outer-driver-by-role
reference. **Neither has an analog for `normalize`**: it is a single fused field-operation composite, not a
step body with an `(op, K, s)` carrier and an outer loop. This is the shape of
[`reciprocal-body-identity`](./reciprocal-body-identity.md) / [`scal-body-identity`](./scal-body-identity.md):
the body IS the identity, there is no wrapper, and there is no fold-parent to defer to — the one difference
being that `normalize` is a *composite* (two genuine same-layer constituents) rather than a single leaf, so
the constituent-floor citations (`nrm2` + `scal`) are carried across the edge unchanged.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `normalize` endpoints) when:

1. **`normalize` is treated as a fused composite over its two firm constituents, not decomposed further and
   not folded.** `normalize` decomposes into exactly its two L2/L3 constituents (`nrm2` + `scal`) by law 6;
   the constituents themselves are firm same-layer floors below `normalize`. It has **no fold-parent** (a
   fused composite, not a member of `inner_product` or `linear_combination`; D9 establishes this), so —
   unlike the fold-member BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for this
   theme's RHS (see §Status).

2. **The signature is whole-tensor at both layers** — `Tensor[N] -> (Scalar, Tensor[N])` with no
   per-element loop exposed at L2 and no iteration view at L3 (the norm reduction is the `nrm2` consumer's
   single semantic step; the rescale is element-local). This is the `krylov-step-body-identity` point-3
   condition applied to the fused `normalize` composite: its signature has no per-element loop visible, so
   it is L3-native by construction and the rotation is identity-in-form rather than a decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion, no genuine kernel fusion.**
   `normalize` carries exactly one reduction (the parallel `nrm2` norm) and one element-local map (the
   `scal` rescale); every element of the rescale is independent and the reduction is parallel in exact
   arithmetic. There is no outer loop, no carry trajectory, no recurrence — nothing for the L3 iteration
   rotation to have rotated and nothing for the L3>L2 lowering to dissolve. There is also no fold-parent and
   no genuine multi-operation kernel fusion (Palace's `linalg::Normalize` already separates the norm pass
   from the rescale pass — the only "fusion" is the *naming* of the composition, which is the same at L3 and
   L2). The load-bearing reduction-tree non-associativity (inherited from `nrm2`) is an L0 floating-point
   choice recorded as a non-law, not an L3 obstruction.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the composite's signature shape `Tensor[N] -> (Scalar, Tensor[N])` is
whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at L3. The
L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed; `normalize`
satisfies this *at L2 already* (its norm reduction is a single `nrm2`-consumer step, its rescale is
element-local `scal`), so the rotation is the identity. This is the same structural argument
`reciprocal-body-identity` / `scal-body-identity` make (and `krylov-step-body-identity` point-3 makes for
each primitive in the kernel body), here applied to a fused composite — and the law-6 factorisation is the
same at both layers, so the constituent-floor citations carry across the edge unchanged.

**Empirical-match (secondary)**: the L3 composite (firm cycle-039) and the L2 floor (firm cycle-043 D9) were
authored independently as value-thread-isomorphic to the same firm L1 operator (cycle-027), and they agree
on every law, the single variant axis (element-type), the non-law set, and the partiality precondition by
independent transcription. The cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit
(`book/src/L3/index.md:44`) classified `normalize` ("fused `nrm2 + scal`") as an **(A) identity-in-form**
backfill candidate; this theme's L3>L2 edge is the fused-composite realization of that audited
classification, now that the L2 floor entry exists for the rotation to target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/normalize`](../L3/normalize.md)) is firm (cycle-039), and the L2 RHS
([`L2/normalize`](../L2/normalize.md)) is firm (cycle-043 D9). No new L2 vocabulary is introduced. The two
constituent floors (`nrm2`, `scal`) already exist (firm cycle-041 D2/D3). `normalize` does not get its own
L4 typed-wrapper anchor (fused leaf composites appear inside L4 operator bodies as let-bindings — the
cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 / operator-to-data cohort), so there
is no upstream L4>L3 theme for `normalize` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor. The B-weighted sibling `normalize_B` is an L1-entry rough-in note
(defined-but-uncalled fused B-Normalize + `matrix-weighted-norm` test-coverage bound), NOT an L2/L3 candidate
— plain text here, not a live link, since no L2/L3 `normalize_B` chapter exists.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/normalize.md` (firm cycle-039) — the L3 whole-tensor form (LHS). Signature (:33-34),
  semantics (one reduction + one element-local map, no iteration view, no sequential obstruction), six
  algebraic laws (:70-75), the single element-type variant axis (:113-117), the §"Lowers to" currently
  recording direct L3>L1 identity via the non-adjacent convention (:131) — this theme supplies the
  now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open questions).
- `book/src/L2/normalize.md` (firm cycle-043 D9) — the L2 floor form (RHS). Identical signature and six
  laws; the fused `nrm2 ∘ scal` composite framing + the **fork-INDEPENDENT, NO fold-parent** /
  design-final determination + the thin-floor (no genuine fusion to unfold) reasoning. (Lands at this
  cycle's integration alongside this theme.)
- `book/src/L2/nrm2.md` + `book/src/L2/scal.md` (firm cycle-041 D2/D3) — the two same-layer constituent
  floors cited unchanged across the edge (`nrm2` the norm consumer-of `inner_product`, `scal` the rescale
  arity-1 member-of `linear_combination`).
- `book/src/L3-L2/reciprocal-body-identity.md` + `book/src/L3-L2/scal-body-identity.md` (firm cycle-042/041)
  — the direct sibling shapes: fold-free `-body-identity` edges, "no wrapper to rotate, the body IS the
  identity". The structure of this theme is inherited from them; the one difference is that `normalize` is a
  *composite* (two same-layer constituents) rather than a single leaf.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed by
  the firm `dot-body-identity` / `scal-body-identity` / `reciprocal-body-identity` themes that cite the same
  line).**

L0 evidence (transitive through the firm L1 operator; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template
  (`auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0/norm; return norm;`); the norm
  reduction (`:266`) and rescale (`:268`) are already separate passes (what makes this edge carry no
  genuine fusion to unfold). **Self-verified (anchor `Normalize` @262/264).** Inherited transitively; the
  body's edge is identity, no new L0 claim.
- `palace/linalg/vector.hpp:267` — `MFEM_ASSERT(norm > 0.0, ...)` — the partiality witness (`x ≠ 0`).
  **Self-verified (anchor `MFEM_ASSERT` @267).**
- `palace/linalg/vector.hpp:269` — `return norm;` — the load-bearing returned norm (`result.0`).
  **Self-verified (anchor `return norm` @269).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/normalize`](../L3/normalize.md)) is firm (cycle-039); the L2 RHS
([`L2/normalize`](../L2/normalize.md)) is firm (cycle-043 D9). The body is the identity rotation on a single
fused composite (the same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` at both layers,
with the two constituent-floor citations preserved); **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `normalize` is a fused composite, not a
step body) and **no fold-parent to defer fusion to** (codomain `(Scalar, Tensor[N])` is neither
reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), and **no genuine kernel fusion to unfold** (`linalg::Normalize`
already separates the norm pass from the rescale pass). The structural justification (whole-tensor signature,
no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition applied to the fused
composite; the empirical-match anchor is the firm L1/L2/L3 value-thread-isomorphic chain + the cycle-036
cross-layer (A) identity-in-form classification. The partiality non-law at `x = 0` (`vector.hpp:267`)
transports unchanged. No speculative operator, no negative-anchor reconstruction, no sequential obstruction.
The fused-composite counterpart of `krylov-step-body-identity`, a direct sibling of `reciprocal-body-identity`
/ `scal-body-identity`, additionally fold-free.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves. `normalize` has **no
> fold-parent** (a fused composite whose codomain is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`),
> so its L2 RHS can only ever be a same-named standalone composite citing its two constituents — neither the
> (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
> `scal-body-identity` (whose §Status carries a design-presupposition note), this theme's RHS is
> design-final; the identity claim does not depend on the fork's outcome — exactly like the cycle-042
> standalone-floor cohort, on a different basis (composite-with-no-fold-parent rather than
> standalone-leaf-with-no-fold-parent). The *constituents* `nrm2` / `scal` do ride the fork at their own
> floors; `normalize` cites them as consumed dependencies, never as a fold of which it is a member, so this
> composite's edge stands unchanged regardless.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).** Lifting the
  L2 floor composite *up* to the L3 whole-tensor form is the value-thread-isomorphic identity rotation: the
  L2 signature has no element loop exposed (the norm is a single `nrm2`-consumer reduction, the rescale is
  element-local `scal`), which is exactly what makes it L3-native by construction. No additional structure
  is required for the lift. This reverse-direction note lives here in working notes per the high→low
  layer-definition discipline; the formal chapter narrates only L3 → L2.

- **L3 `normalize` §27/§131 "no interposed L2 entry" goes STALE once the D9 floor + this theme land
  (downstream-consistency touch, route to c044 sweep — NOT corrected here).** The firm L3 entry
  `book/src/L3/normalize.md` records at line 27 ("**Downward** to L1 … with **no interposed L2 entry and no
  `L3-L2`/`L3-L1` theme file**") and line 131 ("The L2 layer hosts no standalone `normalize` entry … the
  L3>L1 hop is therefore direct") that there is no L2 `normalize`. The D9 floor + this theme supersede those
  notes — once landed, the L3 entry's downward rotation should re-anchor to a **direct L3>L2** hop onto the
  new floor (and this `normalize-body-identity` theme), not a layer-skipping L3>L1 hop (and the L3
  frontmatter `lowers_to: book/src/L1/normalize.md (… no L3-L2/L3-L1 theme)` likewise). Per
  one-operator/theme-per-dispatch discipline this is **NOT corrected in this dispatch**; routed to the c044
  sweep (the same OQ the D9 report flagged).

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this theme's
  L3>L2 identity ∘ the L2>L1 `normalize-leaf-identity` identity) is annotated in-line at the `normalize`
  entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated in-line,
  not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This theme + the co-dispatched
  `normalize-leaf-identity` compose to capture it.
