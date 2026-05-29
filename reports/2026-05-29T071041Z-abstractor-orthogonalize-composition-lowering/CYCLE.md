---
agent: abstractor
invoked_at: 2026-05-29T07:20:26Z
scope: L2>L1 theme sketch — orthogonalize-composition-lowering
status: pending
integrated_at: 2026-05-29T1130Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-022 report 6/9 (wave-1). Applied clean — NEW firm L2>L1 theme orthogonalize-composition-lowering (gs_orthog MGS/CGS/CGS2 variant-dispatch rotation; CITES dot-mutation-rotation Sub-pattern D). The repairer relocated the reverse-direction caveat-bullet OUT of the chapter fence (high→low compliant). L2>L1 firm 3→4; SUMMARY-registered. retroactive-budget 0; build clean. See reports/cycle-022-integrator-staging/STAGING.md row 6 + reports/2026-05-29T1130Z-integrator-finalize-cycle-022/CYCLE.md."
inputs:
  - book/src/L2/orthogonalize.md (firm L2 composition, cycle-019)
  - book/src/L1/orthogonalize.md (firm L1 leaf, cycle-012)
  - book/src/L1/dot.md, book/src/L1/axpy.md (firm L1 leaves)
  - book/src/L1-L0/dot-mutation-rotation.md §Sub-pattern D (cycle-021, the unfused LocalDot+GlobalSum surface — REUSED, not re-derived)
  - book/src/L1-L0/orthogonalize-mutation-rotation.md (firm L1>L0 leaf lowering, audited cycle-014)
  - book/src/L2-L1/{linear-combination-fold-specialization.md, inner-product-fold-specialization.md} (sibling L2>L1 themes — structural precedent)
  - palace/linalg/orthog.hpp:18-89, iterative.cpp:308-325, romoperator.cpp:51-66, 631-646, test/unit/test-orthog.cpp:99-160
  - OQ orthogonalize-composition-lowering-l2-l1-theme + orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d
---

# CYCLE: L2>L1 theme sketch — orthogonalize-composition-lowering

## Summary

The firm L2 `orthogonalize` composition (`book/src/L2/orthogonalize.md`, cycle-019) names the
Gram-Schmidt orthogonalize-against-basis pattern as the canonical `project ▷ subtract`
pipeline, with the `gs_orthog ∈ {MGS, CGS, CGS2}` variant axis surfaced as the
**collective-shape residual axis** (the number/size of reductions: `m×1` / `1×m` / `2×m`).
This theme is the L2>L1 lowering carried forward from cycle-019 (it was blocked on the L2
anchor, now firm). It narrates FORWARD (L2→L1) how the named composition lowers into L1
vocabulary, with two faces of the L1 RHS: (1) the **fused face** — the opaque parameterised
L1 leaf [`orthogonalize`](../L1/orthogonalize.md) (firm, cycle-012), one-to-one with Palace's
single dispatch wrapper `OrthogonalizeIteration` / `OrthogonalizeColumn`; and (2) the
**de-fused face** — the `project` stage as a `dot`-fold and the `subtract` stage as an
`axpy`-fold, the explicit L1 primitives whose **per-variant batching and pass-count** is the
content L2 made visible. The lowering's load-bearing work is the **arity/pass-count dispatch**:
which `[dot, axpy]` sequence each variant pins (`[dot,axpy]×m` interleaved for MGS,
`[dot×m, reduce, axpy×m]` separated for CGS, `[CGS]×2` doubled for CGS2). Per the load-bearing
reuse instruction, the `project` stage's inner-product realisation **cites
[`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md) §Sub-pattern D** (the unfused
`LocalDot` + batched `Mpi::GlobalSum` surface, landed cycle-021) rather than re-deriving the
unfused chain; the `subtract` stage's residual update lowers to the L1 [`axpy`](../L1/axpy.md)
leaf and defers the L0 `w.Add` in-place mutation to the existing firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) L1>L0 theme.
The theme is `firm` (`algebraic` justification): the variant-dispatch IS the L2 entry's
already-firm variant-agreement + idempotence-as-CGS2 laws read as a lowering, over firm L1
vocabulary on both faces, with no speculative operator and no negative-anchor reconstruction.

## Proposed changes

```new:book/src/L2-L1/orthogonalize-composition-lowering.md
# orthogonalize-composition-lowering

The variant-dispatch rotation for Gram-Schmidt orthogonalize-against-basis. Lowers the firm
L2 named composition [`orthogonalize`](../L2/orthogonalize.md) — the `project ▷ subtract`
pipeline parameterised by `gs_orthog ∈ {MGS, CGS, CGS2}` — into its L1 form by **selecting,
per variant, the batching and pass-count of the constituent `dot` / `axpy` L1 primitives**.
Narrated forward: the one named L2 composition **fans down** into Palace's three distinct
loop-structures, and this theme records which `[dot, axpy]` sequence each variant pins
(MGS `[dot,axpy]×m` interleaved / CGS `[dot×m, reduce, axpy×m]` separated / CGS2 `[CGS]×2`
doubled) — the **collective-shape residual axis** the L2 entry made first-class. The L1 RHS
has two faces: the opaque parameterised leaf [`orthogonalize`](../L1/orthogonalize.md) (the
fused face, one-to-one with Palace's dispatch wrapper) and the explicit `dot`-fold ▷
`axpy`-fold (the de-fused face, the composition stages spelled out in L1 primitives). The
inner-product realisation is the firm [`dot`](../L1/dot.md) leaf whose unfused
`LocalDot` + batched `Mpi::GlobalSum` L0 surface is already covered by
[`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md) §Sub-pattern D — **cited, not
re-derived**. Sibling to [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
(the BLAS-1 arity-family fold) and [`inner-product-fold-specialization`](./inner-product-fold-specialization.md)
(the conjugation-convention fold): each is a one-L2-composition-fans-into-L1-vocabulary theme.

## Slug

`orthogonalize-composition-lowering`

## L2 form (LHS)

The L2 form is the named `project ▷ subtract` composition over a candidate `w` and a basis
prefix `V`, parameterised by the orthogonalisation variant and the inner-product hook
([`orthogonalize`](../L2/orthogonalize.md) §Signature, §Semantics):

```text
orthogonalize :: (op: OrthogOp, w: Tensor[N], V: Basis[N, m]) -> { residual: Tensor[N], coeffs: Tensor[m] }

orthogonalize op w V =
  let coeffs   = project  op.variant op.dot w V    -- the per-variant batched inner products
  let residual = subtract w coeffs V               -- w − Σ_j coeffs[j]·V[j]
  in { residual, coeffs }
```

where `op.variant : GSVariant ∈ {MGS, CGS, CGS2}` is inspected exactly once and `op.dot` is
the inner-product hook (canonical `⟨·,·⟩` or B-weighted). The composition is value-producing
and stateless: a fixed-size basis prefix folds into one residual-plus-coefficients pair, with
no convergence predicate (L2 entry §Context). At L2 the **interleaving** of `project` and
`subtract` — and the number/size of reductions inside `project` — is the **variant axis made
visible** (L2 entry §"L2 vs L1 distinction"); the value the composition computes is
variant-invariant in exact arithmetic (L2 entry law 4, variant agreement). The shape
precondition is `V` orthonormal under `op.dot` (caller's contract; L2 entry §Signature).

## L1 form (RHS)

The L1 form is two co-extensive faces of the same value, both firm. **Which face the lowering
targets is a resolution choice, not a value choice** — they compute the same
`{ residual, coeffs }`.

### Face 1 — the opaque parameterised leaf (the fused face)

The firm L1 leaf [`orthogonalize`](../L1/orthogonalize.md) (cycle-012), mirroring Palace's
single dispatch wrapper one-to-one ([`L1/orthogonalize`](../L1/orthogonalize.md) §Signature):

```text
orthogonalize :: (w: Tensor[N], V: Basis[N, m], variant: GSVariant) -> (w': Tensor[N], H: Tensor[m])
  -- H[j] = ⟨w_eff(j), V[j]⟩ ;  w' = w − Σ_j H[j]·V[j]
  -- w_eff(j) = w (CGS/CGS2)  |  progressively-updated w^(j) (MGS)
```

At L1 the `variant` is an **opaque parameter inspected once** and the per-variant collective
shape is recorded as a *property* (a variant-axis note), not as visible composition structure.
The L2 record `{ residual, coeffs }` is the same value-pair as the L1 leaf's tuple `(w', H)`
(L2 entry §Signature derived-specialization: `orthogonalize { variant, dot=⟨·,·⟩ } w V ==
let (w', H) = L1.orthogonalize w V variant in { residual = w', coeffs = H }`). The leaf's own
lowering onto the L0 in-place free functions is the firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) L1>L0 theme
(audited cycle-014) — **this theme stops at the L1 leaf and does not re-derive that L0 step.**

### Face 2 — the de-fused `dot`-fold ▷ `axpy`-fold (the spelled-out face)

The two composition stages spelled out in firm L1 primitives — the `project` stage as a fold
of [`dot`](../L1/dot.md) and the `subtract` stage as a fold of [`axpy`](../L1/axpy.md)
([`L1/dot`](../L1/dot.md) / [`L1/axpy`](../L1/axpy.md) §Signature):

```text
dot  :: (x: Tensor[N], y: Tensor[N])               -> Scalar      -- xᴴ y  (conjugate-linear arg-1)
axpy :: (α: Scalar, x: Tensor[N], y: Tensor[N])    -> Tensor[N]   -- α·x + y

-- project  fans into m applications of dot  (the per-variant batching is the variant axis)
-- subtract fans into m applications of axpy (the rank-1 update w ← w − coeffs[j]·V[j] = axpy(-coeffs[j], V[j], w))
```

At L1 the candidate's progressive update (MGS) or the all-against-original read (CGS) is below
the leaf's resolution; **Face 2 is the de-fusion of Face 1's variant body into the explicit
primitive sequence** — exactly what the L2 composition surfaces. The `op.dot` hook is a `dot`
substitution (canonical → B-weighted), not a structural change (L2 entry law 7). The inner
product's own L0 surface — the unfused `LocalDot` + (per-variant) batched `Mpi::GlobalSum` —
is **already covered by [`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md)
§Sub-pattern D** (cycle-021); see §"Inner-product realisation". The `axpy` residual update's
own L0 surface — the in-place `w.Add(-H[j], V[j])` overwrite — is covered by the firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) L1>L0 theme.

## The variant-dispatch rewrite (L2 → L1)

The lowering reads `op.variant` (the L2 dispatch tag, inspected exactly once) and emits the
matching L1 form. For Face 1 the rewrite is the **identity-in-value** specialization onto the
parameterised leaf; the variant tag flows straight through (`op.variant ↦ variant`). For
Face 2 the rewrite is the **per-variant `[dot, axpy]` sequence selection** — this is the
load-bearing content (the arity/pass-count dispatch the L2 entry made first-class). The
runtime dispatch site is `OrthogonalizeIteration` (`palace/linalg/iterative.cpp:308-325`,
`switch (type)` over `MGS / CGS / CGS2`) and the ROM sibling `OrthogonalizeColumn`
(`palace/models/romoperator.cpp:51-66`, threads the `dot_op` hook).

```text
orthogonalize op w V                                          -- Face 1 (opaque leaf)
  =  L1.orthogonalize w V op.variant                          -- variant flows through; { residual, coeffs } = (w', H)

orthogonalize { variant = MGS,  dot } w V                     -- Face 2 (de-fused), m = |V|
  =  foldl (\w^j j -> let h = dot (w^j) V[j]                  -- [dot, axpy] × m, INTERLEAVED
                      in axpy (-h) V[j] w^j)                   --   w^(j+1) = w^(j) − h·V[j], h gates the next dot
            w [0 .. m-1]                                       --   m reductions of size 1
            ⊕ coeffs[j] = h                                   --   (coeffs accumulated per j)

orthogonalize { variant = CGS,  dot } w V                     -- Face 2 (de-fused)
  =  let coeffs = [ dot w V[j] | j <- [0 .. m-1] ]            -- [dot × m], all against ORIGINAL w
     in subtract w coeffs V                                   -- THEN [axpy × m]; 1 reduction of size m

orthogonalize { variant = CGS2, dot } w V                     -- Face 2 (de-fused)
  =  let (w1, H1) = orthogonalize { variant = CGS, dot } w  V -- first CGS pass
         (w2, dH) = orthogonalize { variant = CGS, dot } w1 V -- second CGS pass on the once-orthogonalised w1
     in { residual = w2, coeffs = H1 + dH }                   -- [CGS] × 2; accumulate; 2 reductions of size m
```

The **dispatch rule** is: *read `op.variant`; for Face 2 emit the matching `[dot, axpy]`
sequence — interleaved-per-column (MGS), batched-separated (CGS), or doubled-CGS with
coefficient accumulation (CGS2)*. The three sequences compute the **same value** in exact
arithmetic (L2 entry law 4); they differ in **pass count and reduction shape**, which is the
load-bearing residual axis recorded in §"Collective-shape recording". The dispatch is the L2
entry's variant-agreement law (law 4) read as a lowering — at the value level it is one form;
the variant selects the sequencing.

### Why CGS2 is `[CGS] × 2`, not a fused single pass

CGS2 is the explicit re-application of the L2 entry's **idempotence law** (law 5): in exact
arithmetic `orthogonalize op residual V = { residual, coeffs = 0 }`, so the second CGS pass
would be a no-op; in finite precision it yields a small correction `dH` that recovers lost
orthogonality ("twice is enough", Kahan/Parlett). The second pass reads the
*once-orthogonalised* `w1` and is **not** algebraically fusible with the first (L2 entry
stage-fusion non-law) — fusing them would compute `dH` against the un-orthogonalised `w` and
destroy the re-orthogonalisation property. The lowering therefore emits two genuine `[dot×m,
reduce, axpy×m]` passes with `coeffs ← H1 + dH` accumulation, witnessed at the L0 `H[j] +=
dH[j]` accumulate (`palace/linalg/orthog.hpp:85`, inside the `if (refine)` block,
`orthog.hpp:75`). CGS2 is dispatched as the `refine = true` parametrisation of
`OrthogonalizeColumnCGS` (`palace/linalg/iterative.cpp:322`).

## Inner-product realisation — cite Sub-pattern D, do not re-derive

The `project` stage's per-column inner product is the firm L1 [`dot`](../L1/dot.md) leaf
(conjugate-linear arg-1; the `op.dot` hook is a `dot` substitution, L2 entry law 7). Its L0
surface — the **unfused `LocalDot` + (per-variant) batched `Mpi::GlobalSum`** — is **already
covered in full by [`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md) §Sub-pattern
D** (cycle-021, `book/src/L1-L0/dot-mutation-rotation.md:146-187`). Sub-pattern D records that
Palace's Gram-Schmidt routines do **not** call the fused `linalg::Dot` (Sub-pattern A); they
reach the same `yᴴ x` reduction through the `InnerProductHelper` template hook whose canonical
`IdentityInnerProduct::operator()` returns `LocalDot(x, y)` (`palace/linalg/orthog.hpp:35`),
and the routine itself applies `Mpi::GlobalSum` over the coefficient buffer — split across the
hook boundary so:

- **MGS** interleaves `w.Add(-H[j], V[j])` per `j` → `m` size-1 reductions (`Mpi::GlobalSum(1,
  &H[j], comm)` per column), and
- **CGS** batches the collective into one `Mpi::GlobalSum(m, H, comm)` across all `m`
  coefficients (`palace/linalg/orthog.hpp:70`; CGS2 = two such passes).

This is the **same per-variant collective-shape distinction** this theme records at the
arity/pass-count level (`m×1` / `1×m` / `2×m`) — Sub-pattern D is its L1>L0 leaf-level
realisation. **This theme does NOT re-derive the unfused LocalDot+GlobalSum chain**; it cites
Sub-pattern D as the inner-product realisation and confines itself to the L2>L1 stage-selection
content. (OQ `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d`
discharged on this side: the L2>L1 theme cites Sub-pattern D for `project`; the L1>L0
`orthogonalize-mutation-rotation` theme is the per-leaf in-place lowering that Sub-pattern D's
observability note already cross-links.)

The B-weighted hook (`op.dot = λ x y. W.InnerProduct(x, y, r)`, the SLEPc/ROM substitution,
`palace/models/romoperator.cpp:636`) is the same `dot` substitution through the identical
composition — the inner-product-hook variant axis, invariant on the lowering shape (L2 entry
law 7).

## Collective-shape recording — load-bearing-numerical residue

This is the **load-bearing residual axis the L2 entry surfaced and this theme pins per lowered
variant** (L2 entry §Semantics "collective-shape residual axis"; the variant-agreement-in-
floating-point non-law). The three variants compute the same value in exact arithmetic (L2
law 4) but pin different reduction trees and pass counts; bit-identical reproduction requires
matching the variant's shape. Read off the verified `orthog.hpp` bodies (the inner-product
collective itself is Sub-pattern D; this table records the **per-variant orchestration**):

| lowered variant | L0 body (verified) | `[dot, axpy]` sequence | collective shape |
|---|---|---|---|
| MGS  | `orthog.hpp:41-53` (`OrthogonalizeColumnMGS`) | `[dot, axpy] × m` interleaved — `dot` at `:49`, `Mpi::GlobalSum(1, &H[j])` at `:50`, `w.Add(-H[j], V[j])` at `:51`, all in one `j`-loop | **`m` reductions of size 1**; each gates the next dot (sequential — the L3 obstruction) |
| CGS  | `orthog.hpp:57-74` (`OrthogonalizeColumnCGS`, `refine=false`) | `[dot × m]` then `[axpy × m]` separated — `m` local dots against the original `w`, one `Mpi::GlobalSum(m, H, comm)` at `:70`, then `m` `w.Add`s | **1 reduction of size `m`**; dots mutually independent |
| CGS2 | `orthog.hpp:75-88` (`if (refine)` block, `:75`) | `[CGS] × 2` — second CGS pass into scratch `dH`, accumulate `H[j] += dH[j]` at `:85`, second `Mpi::GlobalSum(m, dH.data(), comm)` | **2 reductions of size `m`**; second pass non-fusible |

The MGS sequence is **column-order-non-commutative** at the bit level (the left-to-right
rank-1-projector composition does not commute — L2 entry column-order non-law); CGS/CGS2 are
column-order-invariant up to reduction-tree noise. The reduction tree *within* each `dot` is
the [`dot`](../L1/dot.md)-inherited non-associativity recorded in
[`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md) §"Reduction tree" — not re-stated
here. The MPI collective is folded to a local no-op under single-rank scope (CLAUDE.md
"Scope"); the **number and size** of `GlobalSum` calls is the recorded residual axis.

## Empty-prefix identity

The `m = 0` case (empty basis prefix) lowers to the identity for every variant:
`orthogonalize op w [] = { residual = w, coeffs = [] }`. At L1 (Face 1) this is the leaf's
empty-prefix identity law; at Face 2 it is the empty fold. The L0 witness is the
`if (m == 0) { return; }` early return in `OrthogonalizeColumnCGS` (`palace/linalg/orthog.hpp:62`)
and the zero-iteration MGS loop, exercised across all three variants at
`test/unit/test-orthog.cpp:99-120`. (L2 entry law 3.)

## Applicability conditions

The variant-dispatch lowering preserves the L2 value when:

1. **Orthonormal basis precondition.** `V` is orthonormal under `op.dot`
   (`⟨V[i], V[j]⟩ = δ_ij`). The composition does not enforce it; it is the caller's contract,
   inherited from the L2 entry (§Signature) and the L0 header (`palace/linalg/orthog.hpp:18-23`,
   "Assumes that the input vectors are normalized…"). Under this precondition all three
   variants compute the orthogonal projection `(I − V Vᴴ) w` in exact arithmetic.

2. **No output normalisation in this composition.** The lowered form stops at the
   **un-normalised** residual and the length-`m` coefficient vector. Every consumer follows
   the call with its own `Norml2` + `scal(1/‖residual‖)` (GMRES `iterative.cpp:630-632`,
   FGMRES `iterative.cpp:809-811`, ROM `romoperator.cpp:224-226`) — `nrm2` / `scal` are
   **not** dependencies of this lowering (L2 entry §Semantics; L0 header `orthog.hpp:18-23`).

3. **Variant selection is value-preserving; collective shape is not free.** The three `[dot,
   axpy]` sequences compute the same value in exact arithmetic (L2 law 4); bit-reproduction of
   a *specific* Palace call additionally requires matching that variant's collective shape and
   pass count (the §"Collective-shape recording" table). The lowering is valid under the
   **algorithmic-correctness** reading unconditionally, and under the **bit-reproduction**
   reading only when the variant's reduction shape is matched (the standard load-bearing-vs-
   transparent classification, CLAUDE.md §Optimization tricks — the three variants exist
   precisely because their finite-precision behaviour and MPI cost differ).

4. **CGS2 second pass non-fusible.** The CGS2 lowering MUST emit two genuine CGS passes with
   `coeffs ← H1 + dH` accumulation; fusing the passes destroys the re-orthogonalisation
   property (L2 entry stage-fusion non-law; the `H[j] += dH[j]` accumulate at
   `orthog.hpp:85`). The `refine` flag (`orthog.hpp:75`) is the exact L0 dispatch.

5. **Inner-product hook is a `dot` substitution.** `op.dot` (canonical → B-weighted) is a
   closure substitution leaving the lowering's shape and the §"Collective-shape recording"
   table invariant (L2 entry law 7); only the inner-product leaf's realisation differs and the
   orthogonality contract reads `⟨residual, V[i]⟩_B = 0`. The hook's L0 realisation is the
   `InnerProductHelper` template, covered by Sub-pattern D.

6. **In-place candidate destruction (Face 2 / leaf lowering).** The L0 forms overwrite `w` in
   place via `w.Add`; the lowering to the **L1 leaf** is value-faithful (the L1 leaf returns a
   fresh `w'`), and the leaf's onward lowering to the in-place L0 buffer is the firm
   [`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) theme's
   applicability condition 1 (no observer of the prior `w` after the call) — **not re-derived
   here**.

## Justification kind

`algebraic` — the variant-dispatch rule **is** the L2 entry's already-firm laws read as a
lowering: law 4 (variant agreement — the three `[dot, axpy]` sequences are one value) gives
the MGS/CGS dispatch directly, and law 5 (idempotence-on-the-residual) grounds the CGS2
`[CGS] × 2` second pass as an explicit re-application of the projector identity (the
`H[j] += dH[j]` accumulate, `orthog.hpp:85`). The Face-1 lowering (onto the opaque leaf) is the
**identity-in-value** specialization of the named composition onto the parameterised L1 leaf
(L2 entry §Signature derived-specialization). A **structural** flavour is present (the Face-2
de-fusion is the syntactic expansion of `project ▷ subtract` into `[dot, axpy]` sequences) and
a **reduction-chain** flavour is present in the MGS interleaved fold (each `axpy` gates the
next `dot`), but the governing justification is the algebraic variant-agreement +
idempotence-as-CGS2 identity, so the theme is classified `algebraic` (matching the sibling
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
`algebraic` classification — both are L2-laws-read-as-lowering). The per-variant collective
shape is the load-bearing-numerical residue recorded in §"Collective-shape recording"; the
inner-product fusion is delegated to Sub-pattern D.

## Speculative L1 operators

**None.** Both faces of the L1 RHS are firm:

- Face 1 — the L1 leaf [`orthogonalize`](../L1/orthogonalize.md) (firm, cycle-012).
- Face 2 — [`dot`](../L1/dot.md) (the `project` stage's inner product; firm post-cycle-002,
  the `op.dot` hook is a substitution) and [`axpy`](../L1/axpy.md) (the `subtract` stage's
  rank-1 update `w ← w − coeffs[j]·V[j] = axpy(-coeffs[j], V[j], w)`; firm post-cycle-002).

The LHS [`orthogonalize`](../L2/orthogonalize.md) is firm (cycle-019). This theme proposes no
new operators — it is the lowering edge between firm vocabulary on both sides. **Householder is
scoped out** (it threads a reflector sequence, fundamentally different state; Palace's L0 has
no Householder path — L2 entry §Variant axes; CLAUDE.md unimplemented-component policy).

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` read_range + `tools/citecheck/`
anchor-drift checks this invocation — producer-citation self-verification,
`verify-citation-range` producer-self-verification):

- `palace/linalg/orthog.hpp:18-23` — header scope contract: "Assumes that the input vectors
  are normalized, but does not normalize the output vectors!" — the no-output-normalisation
  contract (applicability condition 2). **Self-verified.**
- `palace/linalg/orthog.hpp:29-36` — `IdentityInnerProduct` / `InnerProductHelper`: the
  `op.dot` template hook; `return LocalDot(x, y)` at `:35`. The inner-product realisation
  pointer (Sub-pattern D). **Self-verified (anchor at :35).**
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`: the single interleaved `j`-loop;
  `H[j] = dot_op(w, V[j])` at `:49`, `Mpi::GlobalSum(1, &H[j], comm)` at `:50`,
  `w.Add(-H[j], V[j])` at `:51`. The MGS `[dot, axpy] × m` interleaved sequence (`m` size-1
  reductions). **Self-verified (def at :41; dot at :49; w.Add at :51).**
- `palace/linalg/orthog.hpp:55-89` — `OrthogonalizeColumnCGS`: empty-basis early return
  `if (m == 0)` at `:62`; `m` batched local dots; single `Mpi::GlobalSum(m, H, comm)` at `:70`;
  `m` batched `w.Add`s; the `if (refine)` block at `:75` with `H[j] += dH[j]` accumulate at
  `:85` and second `Mpi::GlobalSum`. The CGS `[dot×m, reduce, axpy×m]` and CGS2 `[CGS]×2`
  sequences. **Self-verified (def at :57; m==0 at :62; GlobalSum(m,H) at :70; refine at :75;
  accumulate at :85).**
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration`: the runtime variant
  dispatch (`switch (type)` over `MGS / CGS / CGS2`; `CGS2 = OrthogonalizeColumnCGS(..., true)`
  at `:322`); the variant is bound once and dispatched once, against the leading `j + 1`
  columns. **Self-verified (CGS2 `true` at :322).**
- `palace/models/romoperator.cpp:51-66` — the ROM `OrthogonalizeColumn` sibling dispatch:
  switches on `Orthogonalization`, forwards the `dot_op` hook (CGS2 = `refine=true`). The
  second dispatch surface. **Self-verified.**
- `palace/models/romoperator.cpp:631-646` — the B-weighted hook consumer: the lambda
  `[&W, &r](const Vector &x, const Vector &y){ return W.InnerProduct(x, y, r.Real()); }`
  (`W.InnerProduct` at `:636`) — the `op.dot` B-weighted substitution (inner-product-hook
  variant axis). **Self-verified (W.InnerProduct at :636).**
- `palace/linalg/iterative.cpp:630-632` — GMRES Arnoldi consumer: `OrthogonalizeIteration(...)`
  immediately followed by `Norml2` + `*= 1.0/Hj[j+1]` — normalisation is the caller's
  (applicability condition 2). **Self-verified.**
- `palace/linalg/iterative.cpp:809-811` — FGMRES Arnoldi consumer: identical dispatch +
  `Norml2` + `scal` sequence. **Self-verified.**
- `test/unit/test-orthog.cpp:99-120` — empty-prefix edge ("OrthogonalizeColumn - Real Empty"):
  all three variants leave `w` unchanged at `m = 0` (law 3, the empty-prefix identity).
  **Self-verified.**
- `test/unit/test-orthog.cpp:123-160` — parametric real test: all three variants pass
  `⟨residual, V[i]⟩ ≈ 0` to `1e-12` (the substitutability / variant-agreement witness; the
  `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at `:158`, inside the check loop `:154-159`).
  **Self-verified (WithinAbs assertion at :158).**
- `test/unit/test-orthog.cpp:276, 333` — weighted-real-1 (`:276`) / weighted-complex-1 (`:333`)
  parametrisations: the B-weighted `op.dot` variant axis witnesses. **Self-verified (TEST_CASE
  boundary lines).**

L2 / L1 / cross-theme anchors (firm on every side):

- `book/src/L2/orthogonalize.md` — the firm L2 named composition (LHS); its variant axis,
  laws 4 / 5 / 7, and collective-shape residual-axis disclosure are this theme's dispatch rule
  and load-bearing residue.
- `book/src/L1/orthogonalize.md` — the firm L1 leaf (Face 1 RHS); the opaque parameterised
  primitive this composition lowers into.
- `book/src/L1/dot.md`, `book/src/L1/axpy.md` — the firm L1 leaves the de-fused Face 2 composes
  (`project` = `dot`-fold, `subtract` = `axpy`-fold).
- `book/src/L1-L0/dot-mutation-rotation.md:146-187` — §Sub-pattern D (cycle-021): the unfused
  `LocalDot` + batched `Mpi::GlobalSum` inner-product surface — **cited as the `project`
  stage's L0 realisation, not re-derived** (the load-bearing reuse instruction).
- `book/src/L1-L0/orthogonalize-mutation-rotation.md` — the firm L1>L0 leaf lowering (audited
  cycle-014): how Face 1's leaf lowers to the in-place L0 free functions; this theme stops at
  the L1 leaf and defers the `w.Add` in-place step to it.
- `book/src/L2-L1/linear-combination-fold-specialization.md`,
  `book/src/L2-L1/inner-product-fold-specialization.md` — the sibling L2>L1 themes (structural
  precedent for a one-L2-composition-fans-into-L1-vocabulary theme).

## Status

`firm` — the L2 LHS is firm (cycle-019), both L1 RHS faces are firm (the leaf cycle-012; `dot`
+ `axpy` post-cycle-002), and the variant-dispatch rule IS the L2 entry's already-firm laws 4
(variant agreement) + 5 (idempotence-as-CGS2) read as a lowering, with the Face-1 lowering the
identity-in-value specialization onto the parameterised leaf. The three `[dot, axpy]` sequences
and their collective shapes (`m×1` / `1×m` / `2×m`) are read straight off the **self-verified**
`orthog.hpp` bodies (MGS `:41-53`, CGS `:57-74`, CGS2 `:75-88`), the dispatch wrappers are
read in full (`iterative.cpp:308-325`, `romoperator.cpp:51-66`), and all consumer call sites
are verified (`iterative.cpp:630, 809`; `romoperator.cpp:636`). The inner-product realisation
is delegated to the firm [`dot-mutation-rotation`](../L1-L0/dot-mutation-rotation.md)
§Sub-pattern D (no re-derivation), and the in-place `w.Add` step is delegated to the firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) L1>L0 theme.
No literature inference, no negative-anchor reconstruction, no speculative operator — so `firm`
(matching the sibling [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
and [`inner-product-fold-specialization`](./inner-product-fold-specialization.md) firmness
bar). A `lowering-verifier` audit attaching the `verified_against:` block (confirming the
per-variant sequence selection + collective-shape table against the L0 source, and the
Sub-pattern D delegation boundary) is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Sub-pattern D delegation boundary (for the lowering-verifier).** This theme deliberately
  does NOT re-derive the unfused `LocalDot` + `Mpi::GlobalSum` inner-product chain — it cites
  `dot-mutation-rotation` §Sub-pattern D (`:146-187`) as the `project` stage's L0 realisation.
  The audit should confirm the boundary is clean: the L2>L1 theme owns the **per-variant
  stage-selection** (which `[dot, axpy]` sequence, how many passes, collective shape); the
  L1>L0 Sub-pattern D owns the **inner-product collective unfusing** (LocalDot + batched
  GlobalSum); and the L1>L0 `orthogonalize-mutation-rotation` theme owns the **in-place `w.Add`
  candidate-buffer rebinding**. No content should be duplicated across the three.

- **OQ discharge.** This theme discharges OQ `orthogonalize-composition-lowering-l2-l1-theme`
  (the carry-forward from cycle-019, which was blocked on the L2 anchor — now firm). The
  companion OQ `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d` is
  discharged on the L2>L1 side here (the `project` stage cites Sub-pattern D); the L1>L0
  `orthogonalize-mutation-rotation` theme already cross-links Sub-pattern D via that theme's
  observability note (`dot-mutation-rotation.md:170-177`), so no edit to the L1>L0 theme is
  proposed by this dispatch (that would be a separate lifter/lowering-verifier scope).

- **No dedicated L1↔L2 equivalence test (inherited caveat, not a status reduction).** The
  variant-agreement substitutability is witnessed at the L0 level
  (`test/unit/test-orthog.cpp:123-160`, all three variants pass `⟨residual, V[i]⟩ ≈ 0`); a
  dedicated test asserting the de-fused Face-2 `[dot, axpy]` sequence reproduces the Face-1 leaf
  value would witness the lowering's value-preservation directly. The firm-without-dedicated-
  L1↔L2-test bar carries through from the sibling
  [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)
  (which records the same inherited caveat).
```

```edit:book/src/L2-L1/index.md
| [inner-product-fold-specialization](./inner-product-fold-specialization.md) | `L2/inner_product` (firm) | `L1/dot` (firm; `dot` + `tdot`) + `L1/bilinear-form` (rough-in, M-weighted member) | firm *(algebraic; conjugation-convention / element-type / weight dispatch + value-level `xᴴ y`↔`yᴴ x` conjugate-pair re-order + pinned reduction tree)* |
| [orthogonalize-composition-lowering](./orthogonalize-composition-lowering.md) | `L2/orthogonalize` (firm, cycle-019) | `L1/orthogonalize` (firm leaf) + `L1/dot` + `L1/axpy` (firm; `project`▷`subtract` de-fusion) | firm *(algebraic; MGS/CGS/CGS2 variant-dispatch = `[dot,axpy]` sequence selection; inner product cites `dot-mutation-rotation` Sub-pattern D; collective shape `m×1`/`1×m`/`2×m`)* |
```

```edit:book/src/SUMMARY.md
- [inner-product-fold-specialization](./L2-L1/inner-product-fold-specialization.md)
- [orthogonalize-composition-lowering](./L2-L1/orthogonalize-composition-lowering.md)
```

## Speculative operators proposed

**None.** This theme is a lowering edge between firm vocabulary on both sides:
- LHS: `L2/orthogonalize` (firm, cycle-019).
- RHS Face 1: `L1/orthogonalize` (firm leaf, cycle-012).
- RHS Face 2: `L1/dot` + `L1/axpy` (firm post-cycle-002).

No harvester promotion is required by this dispatch.

## Supporting evidence

- L2 LHS: `book/src/L2/orthogonalize.md` (firm composition; the `project ▷ subtract` form, the
  `gs_orthog ∈ {MGS, CGS, CGS2}` variant axis, laws 4 / 5 / 7, collective-shape residual axis).
- L1 RHS: `book/src/L1/orthogonalize.md` (Face 1 leaf), `book/src/L1/dot.md` +
  `book/src/L1/axpy.md` (Face 2 primitives).
- Reuse anchor (load-bearing instruction): `book/src/L1-L0/dot-mutation-rotation.md:146-187`
  (§Sub-pattern D — the unfused `LocalDot` + batched `Mpi::GlobalSum` inner-product surface;
  CITED, not re-derived).
- L0 source (self-verified via codemap + `tools/citecheck/` this invocation):
  `palace/linalg/orthog.hpp:18-89` (header-only inline GS free functions: MGS `:41-53`, CGS
  `:57-74`, CGS2 refine `:75-88`, hook `:29-36`, header contract `:18-23`),
  `palace/linalg/iterative.cpp:308-325` (`OrthogonalizeIteration` dispatch; CGS2 `true` at
  `:322`), `palace/models/romoperator.cpp:51-66` (ROM `OrthogonalizeColumn` sibling dispatch) +
  `:631-646` (B-weighted hook, `W.InnerProduct` at `:636`),
  `palace/linalg/iterative.cpp:630-632` + `:809-811` (GMRES/FGMRES consumers, caller's
  normalisation), `test/unit/test-orthog.cpp:99-120` (empty-prefix) + `:123-160` (variant
  agreement, `WithinAbs(0.0, 1e-12)` at `:158`) + `:276, 333` (B-weighted witnesses).
- Boundary anchors: `book/src/L1-L0/orthogonalize-mutation-rotation.md` (firm L1>L0 leaf
  lowering, audited cycle-014 — the in-place `w.Add` step deferred to it),
  `book/src/L2-L1/linear-combination-fold-specialization.md` +
  `book/src/L2-L1/inner-product-fold-specialization.md` (sibling structural precedent).

## Open questions / caveats

(See the in-fence §"Open questions / caveats" for the chapter-internal caveats. Report-level:)

- **Lifting note (reverse direction, working notes — relocated out of the chapter body per the
  high→low layer-definition discipline).** *[Repairer-relocated cycle-022: this reverse-direction
  L1→L2 lift observation was originally a first bullet inside the `new:` chapter fence; it is moved
  here to the report-level working-notes section because the CLAUDE.md "Layers are defined high→low;
  lifting notes go in working notes" invariant requires reverse-direction lift notes to live in
  working notes / supporting docs / the OQ ledger, NOT in the published chapter body. The formal
  chapter now narrates only L2 → L1.]* Lifting an L1 form *up* to the L2 composition is determinate
  on both faces: Face 1's leaf IS the composition with the variant as an opaque parameter (lift =
  name it `{ residual, coeffs }` and surface the variant as the visible batching axis); Face 2's
  `[dot, axpy]` sequence lifts to the `project ▷ subtract` composition by recognising the
  per-variant interleaving pattern (MGS interleaved / CGS separated / CGS2 doubled). The lift loses
  the pinned collective shape only in the sense that L2 records it as the disclosed residual axis
  rather than the executed reduction tree — the lift is value-faithful and shape-disclosing, not
  shape-erasing.
- The three-way delegation boundary (L2>L1 stage-selection ⟂ L1>L0 Sub-pattern D inner-product
  unfusing ⟂ L1>L0 `orthogonalize-mutation-rotation` in-place `w.Add` rebinding) is the key
  thing for the lowering-verifier to confirm is non-duplicative — flagged in the in-fence
  caveats and here.
- No edit to the existing L1>L0 `orthogonalize-mutation-rotation` theme is proposed by this
  dispatch (its Sub-pattern D cross-link already exists via the observability note at
  `dot-mutation-rotation.md:170-177`). If a future lifter pass wants to add an explicit
  reciprocal pointer FROM `orthogonalize-mutation-rotation` TO this new L2>L1 theme, that is a
  separate lifter scope.
