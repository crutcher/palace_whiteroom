---
agent: combinator-miner
invoked_at: 2026-05-28T231046Z
scope: Pattern proposal — inner-product reduce-to-scalar fold (inner_product at L2), sibling to linear_combination
status: integrated
integrated_at: 2026-05-29T030000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-018 finalize — inner_product rough-in dep-map row added to L2/index.md (conjugation-convention-axis fold-sibling of linear_combination; >=3-instance bar met: dot/tdot/bilinear-form); forward-ref to ./inner_product.md kept PLAIN-TEXT (no dead link); OQ inner-product-fold-sibling-candidate answered, harvester-formalization + conjugation-pinning follow-ups via OQ inner-product-harvester-formalization-and-conjugation-pinning. L2 rough-in cohort = inner_product (was linear_combination)."
---

# CYCLE: Combinator candidate — inner-product-fold

## Summary

Palace's "reduce two conforming vectors to a scalar" surface — `LocalDot`/`Dot`
for real and complex vectors, `TransposeDot` for the unconjugated complex form,
and the matrix-weighted `Dot(comm, x, A, y)` (= `xᴴ A y`) — is a **single
reduce-to-scalar fold** parameterised over a per-element kernel:
`inner_product :: (Tensor[N], Tensor[N]) -> Scalar`, semantically
`foldl (+) 0 (zipWith kernel x y)`. This is the **sibling fold** the cycle-017
`linear_combination` proposal deliberately held out (OQ
`inner-product-fold-sibling-candidate`): `linear_combination` reduces a
(scalar, tensor) term-list to a **`Tensor[N]`** under the additive-fold
homomorphism; `inner_product` reduces two equal-shape tensors to a **`Scalar`**
under a multiply-then-sum reduction. They share NO laws — `inner_product`
carries symmetry / Hermitian-symmetry / conjugate-linearity / positive-semi-
definiteness, which have no analogue in `linear_combination`, and conversely
`linear_combination`'s concatenation/arity homomorphism has no analogue here.
Keeping them separate is exactly the "algebra of folds, not one mega-combinator"
nuance the human and methodology requested.

The ≥3-instance soft bar **is met** counting genuine kernel/weighting members:
real dot, complex Hermitian dot, complex unconjugated `tdot`, and the
M-weighted bilinear form `xᴴ M y` (whose `M = I` case IS plain `dot`). I
therefore **emit a rough-in dep-map row** for `inner_product` at
`book/src/L2/index.md`, sibling to `linear_combination`. Two axes are recorded
as **variant axes, NOT separate operators**: the **conjugation-convention** axis
(real-symmetric / complex-Hermitian-conjugate-first-arg / complex-unconjugated)
and the **weighting** axis (plain `M = I` vs M-weighted `xᴴ M y`). The M-weighting
unification of the `bilinear-form` + `matrix-weighted-norm` L1 cohort is noted
as upside but flagged "do not over-reach" — `matrix-weighted-norm` adds an outer
`√` and an SPD precondition, so it is a *composition over* `inner_product`, not
an instance *of* it.

**The L1 leaves stay.** `dot`/`tdot` (firm) and `bilinear-form`/
`matrix-weighted-norm` (rough-in) correctly mirror Palace's distinct L0 C++
symbols for the L1>L0 mutation rotation. `inner_product` is the L2 form they
fuse *up* into, not a replacement.

## Pattern instances

Counted as genuine fold members (distinct per-element kernel or distinct
weighting), all self-verified via codemap `read_range` this invocation. **Four
genuine kernel/weighting members** (Instances 1–4: real dot, complex Hermitian
dot, complex unconjugated `tdot`, M-weighted bilinear form) — well clear of the
≥3 bar — plus **one consumer-law witness** (Instance 5, `CheckDot`), which is NOT
a sixth kernel member but a runtime check of Instances 2/4's PSD law (see its
entry below and §"Why these are instances, not axes"). The four kernel/weighting
members are NOT the same operator wearing different hats (see §"Why these are
instances, not axes" below for the discipline on conjugation vs. genuine-instance).

- **Instance 1 — real dot** (`x[i]·y[i]`, returns real): `linalg::LocalDot(Vector, Vector)` at `palace/linalg/vector.cpp:665-672` (via Hypre `hypre_SeqVectorInnerProd`); also `mfem::Vector::operator*`. L1 home: `book/src/L1/dot.md:16` (`dot`, real element-type row).
- **Instance 2 — complex Hermitian dot** (`conj(x[i])·y[i]`, returns complex): `ComplexVector::Dot` at `palace/linalg/vector.cpp:263-267` and `linalg::LocalDot(ComplexVector, ComplexVector)` at `palace/linalg/vector.cpp:674-685`. L1 home: `book/src/L1/dot.md:34` (complex Hermitian row). Conjugation-convention = `hermitian`.
- **Instance 3 — complex unconjugated `tdot`** (`x[i]·y[i]`, returns complex, NOT PSD): `ComplexVector::TransposeDot` at `palace/linalg/vector.cpp:269-274`. L1 home: `book/src/L1/dot.md:35` (the `tdot` row). Conjugation-convention = `unconjugated`. **Distinct laws** (dot.md:71-75: symmetric not Hermitian, NOT positive-semi-definite — `tdot((1,i),(1,i)) = 0` with nonzero argument).
- **Instance 4 — M-weighted (matrix-weighted) inner product** (`xᴴ M y`): `linalg::Dot(comm, x, A, y)` at `palace/linalg/operator.cpp:621-639` (two overloads — real `Operator` weight at `:621-628`, complex `ComplexOperator` weight at `:630-639`). L1 home: `book/src/L1/bilinear-form.md` (rough-in). The `M = I` case IS Instance 2 — direct evidence: the L0 body is `A.Mult(x, Ax); return Dot(comm, Ax, y)`, i.e. apply-then-plain-dot, so plain `dot` is the `M = I` reduction. (Precise per overload: the complex `ComplexOperator` weight at `:630-639` is literally that single `A.Mult(x, Ax)`; the real `Operator` weight at `:621-628` splits the apply into `A.Mult(x.Real(), Ax.Real()); A.Mult(x.Imag(), Ax.Imag())` because `A` is real but `x` is a `ComplexVector` — the element-type axis covers this, and the apply-then-plain-dot characterization holds for both.)
- **Instance 5 (live call-site, the CheckDot breakdown-guard application)** — the inner-product fold consumed under a positive-real guard: `CheckDot` at `palace/linalg/iterative.cpp:22-32` asserts `isfinite(dot) && dot.real() >= 0.0` on the result of `dot`/`bilinear-form`, used at CG/GMRES breakdown checks (`iterative.cpp:396, 410, 445, 461, 569, 584, 643, 757, 763, 822`). This is NOT a separate fold — it is the **PSD law of Instance 2/4 being checked at runtime** (`β = ⟨Br, r⟩ ≥ 0` requires the Hermitian/SPD form). I count it as a pattern instance of *the fold's PSD law being load-bearing in the wild*, not as a sixth kernel; it grounds why the conjugation-convention axis is semantically load-bearing (only the Hermitian member supports the guard).

### Why these are instances, not axes (the over-unification discipline)

The dispatch correctly warns the conjugation-convention is an *axis*, not a set
of separate operators — and I keep it that way: Instances 1/2/3 collapse to ONE
`inner_product` operator with a `conjugation-convention` variant axis (exactly as
`book/src/L1/dot.md:89-96` already treats element-type and conjugation as the two
orthogonal axes of `dot`/`tdot`). The ≥3-instance bar for *proposing the L2
combinator at all* is met by the genuinely-distinct **reduction shapes** that
the L2 fold must subsume: (real ⊕ complex-Hermitian ⊕ complex-unconjugated)
kernel members PLUS the weighting member (`xᴴ M y`). What makes this a real L2
combinator rather than "just `dot` again" is that the **M-weighted form is a
genuinely different reduction** (it threads an operator application through the
left argument) that Palace exposes as a *separate L0 symbol* and the artifact
already hosts as a *separate L1 operator* (`bilinear-form`) — yet it is the same
multiply-conjugate-sum fold with `M = I` specialised away. The L2 layer is where
that "`dot` is `bilinear-form` at `M = I`" relationship becomes statable as one
operator.

## Proposed combinator

- **Slug**: `inner-product` (file `inner_product`)

- **Layer**: **L2** (fusion-rotation layer).

  Rationale — why L2, not adjacent layers (parallels the cycle-017
  `linear_combination` layer argument, since `inner_product` is its sibling fold):

  - **Not L1.** L1 must mirror Palace's distinct L0 symbols one-to-one: `dot`
    and `tdot` are firm L1 leaves (`book/src/L1/dot.md`), `bilinear-form` is an
    L1 rough-in (`book/src/L1/bilinear-form.md`). The L1>L0 mutation rotation
    rewrites each into its receiver-vs-argument / workspace idiom (the
    `ComplexVector::Dot` receiver asymmetry; the `Dot(comm,x,A,y)` internal
    `Ax` workspace). Those leaves are load-bearing for that rotation;
    `inner_product` is the form they fuse *up* into, not a replacement.
  - **L2 is exactly the fusion-rotation layer** (`book/src/L2/index.md:1-18`):
    the M-weighted `Dot(comm, x, A, y)` fuses an operator-apply and a dot into a
    single workspace-threaded pass; unfolding it to `dot(apply_linop(M, x), y)`
    and recognising plain `dot` as the `M = I` case is precisely the L2
    fusion rotation. The L2 overlay vocabulary even lists `dot` explicitly
    (`book/src/L2/index.md:17`). `inner_product` is the canonical L2 name the
    `dot`/`tdot`/`bilinear-form` cohort dissolves into.
  - **Not L4.** L4 is the graph-evaluation calculus of higher-order combinators
    + state monads (`iterate_while`, `solve-monad`). `inner_product` is a pure
    data-parallel reduction with no control flow, no monadic state threading, no
    convergence predicate — same classification as `linear_combination` at L2
    (cycle-017 §Proposed combinator). It belongs with the tensor algebra, the
    layer that already hosts `dot` in its vocabulary.

  This places `inner_product` at the **same layer as `linear_combination`** —
  the two folds sit side by side at L2, which is the intended "small algebra of
  folds" shape.

- **Signature sketch** (best guess; harvester firms up):

  ```text
  inner_product :: (x: Tensor[N], y: Tensor[N]) -> Scalar
  inner_product x y = foldl (+) zero (zipWith kernel x y)
    where kernel depends on the conjugation-convention axis:
      real-symmetric        : kernel a b = a * b
      complex-hermitian     : kernel a b = conj a * b      -- conjugate-linear in 1st arg
      complex-unconjugated  : kernel a b = a * b           -- the `tdot` member
  ```

  M-weighted member (the `bilinear-form` instance) as a thin composition over the plain fold:

  ```text
  inner_product_M :: (x: Tensor[N], M: LinearOperator[N,N], y: Tensor[N]) -> Scalar
  inner_product_M x M y = inner_product x (apply_linop M y)      -- xᴴ M y
  inner_product x y      = inner_product_M x I y                 -- the M = I specialization
  ```

  Shape contract (bunsen-style, named axes):
  - `x` — `Tensor[N]` — read-only.
  - `y` — `Tensor[N]` — read-only; `x` and `y` share length axis `N` and element type.
  - result — `Scalar` — element type follows the conjugation-convention/element-type table (real → real; complex → complex, per `book/src/L1/dot.md:31-35`).

- **Algebraic intuition** (the laws that make this a DIFFERENT fold from `linear_combination`):

  - **Bi-/sesqui-linearity**: linear in the second argument; linear (real) or
    conjugate-linear (complex Hermitian) in the first
    (`book/src/L1/dot.md:57-67`). This is the fold's defining structure — `dot`
    distributes over `linear_combination` in each argument:
    `inner_product(linear_combination [(aᵢ,xᵢ)], y) = Σ conj(aᵢ)·inner_product(xᵢ, y)`
    (Hermitian) — i.e. the two folds compose via a distributivity law, which is
    the cleanest evidence they are distinct-but-related siblings, not one
    operator.
  - **Symmetry / Hermitian symmetry**: `inner_product(x,y) = inner_product(y,x)`
    (real); `= conj(inner_product(y,x))` (Hermitian)
    (`book/src/L1/dot.md:57, 65`). `tdot` member: symmetric, not Hermitian.
  - **Positive semi-definiteness at `y = x`**: `inner_product(x,x) ≥ 0` (real /
    Hermitian), `= 0` iff `x = 0` (`book/src/L1/dot.md:60, 68`); confirmed by
    the self-dot fast path returning imaginary part exactly `0.0`
    (`palace/linalg/vector.cpp:266, 678`). **The `tdot` member breaks this** —
    `tdot(x,x) ∈ ℂ`, can be 0 for nonzero `x` (`book/src/L1/dot.md:71-75`). This
    is precisely why conjugation-convention is a load-bearing axis and why
    `CheckDot` (`iterative.cpp:22-32`) only guards the Hermitian/SPD member.
  - **Identity element / zero**: `inner_product(0, y) = inner_product(x, 0) = 0`
    (`book/src/L1/dot.md:61, 69`). There is no multiplicative identity (it is a
    reduction to a scalar, not a closed binary op on `Tensor[N]`).
  - **Permutation/associativity — EXACT-ARITHMETIC ONLY (IEEE caveat)**: the
    summation reduction-tree is non-associative in IEEE-754; load-bearing
    exactly as for `dot` (`book/src/L1/dot.md:45, 79`) and `linear_combination`
    (cycle-017). The fold's left-to-right order is the canonical L2 naming order;
    bit-identical reproduction of an L0 site requires the L2>L1 theme to record
    that site's pinned reduction tree (Hypre + MPI tree-reduce).
  - **Distinctness from `linear_combination`**: NO concatenation/arity
    homomorphism (it is binary in two whole tensors, not a fold over a
    variadic term-list); result is `Scalar` not `Tensor[N]`. This is the precise
    "different fold" content of OQ `inner-product-fold-sibling-candidate`.

- **Variant axes** (for harvester; all orthogonal):

  1. **Conjugation-convention** — `real-symmetric` | `complex-hermitian`
     (conjugate-first-arg, the default) | `complex-unconjugated` (the `tdot`
     member). At L0: `LocalDot(Vector,…)` / `ComplexVector::Dot` /
     `ComplexVector::TransposeDot`. This is the dispatch's "orthogonal axis, not
     separate operators" — recorded as an axis. The PSD law holds only on the
     first two; the `unconjugated` cell drops it (mirrors the existing
     `dot`/`tdot` split at `book/src/L1/dot.md:94`).
  2. **Element-type** — `real` | `complex` (the real member has no conjugation
     sub-axis; the conjugation axis only ranges over the complex members).
     Mirrors `book/src/L1/dot.md:93`.
  3. **Weighting** — `plain` (`M = I`) | `M-weighted` (`xᴴ M y`). At L0: `Dot(comm,x,y)`
     vs `Dot(comm,x,A,y)` (`operator.cpp:621-639`). The M-weighted cell threads
     an `apply_linop(M, ·)` through the first argument BEFORE the reduction; the
     plain cell is `M = I`. **Do-not-over-reach note**: the SPD-norm operator
     `matrix-weighted-norm` (`√(xᴴ B x)`, `book/src/L1/matrix-weighted-norm.md`)
     is NOT a cell of this axis — it is `√ ∘ inner_product_M` at `y = x` with an
     SPD precondition. It is a *composition over* `inner_product`, recorded as a
     consumer, not absorbed as an instance (keeps the fold pure and avoids
     dragging the SPD precondition into the inner-product algebra).
  4. **MPI collective** (L0 detail, not an L2 axis) — `LocalDot` (single-rank)
     vs `Dot` (= `LocalDot` + `Mpi::GlobalSum`). Single-rank is in scope; the
     collective folds into the L2>L1 / L1>L0 lowering, NOT an L2 variant axis
     (per `book/src/L1/dot.md:47`).

## Proposed changes

```edit:book/src/L2/index.md
| `inner_product` (chapter `./inner_product.md` to be authored by harvester) | `(Tensor[N], Tensor[N]) -> Scalar` (≡ `foldl (+) zero (zipWith kernel x y)`); M-weighted member `inner_product_M(x, M, y) = xᴴ M y` (shorthand — exact conjugation/arg-order convention to be pinned by harvester; Palace documents `Dot(comm,x,A,y)` as `yᴴ A x`, body `(Ax)ᴴ y = xᴴ Aᴴ y` — see caveat 7), plain ≡ `M = I` | L1 leaves it fuses up from: `dot`, `tdot` (firm), `bilinear-form` (rough-in, the M-weighted member). L2-composition for the weighted member: `apply_linop` (M applied to first arg). Concepts: `dot` (cross-cutting prose). **Sibling fold (do NOT merge):** `linear_combination` (reduce-to-`Tensor[N]`; different laws, no shared concatenation/PSD structure). Consumer (NOT an instance): `matrix-weighted-norm` = `√ ∘ inner_product_M` at `y=x`, SPD `B`. | `(rough-in, proposed-by: combinator-miner:2026-05-28T231046Z)` |
```

Append the row to the L2 operator dep-map table, **after the `linear_combination`
row at `book/src/L2/index.md:25`** (the cycle-017 rough-in row; a parallel
cycle-018 harvester is firming that same row — integrator should append the
`inner_product` row after whatever firmness state the `linear_combination` row
settles into, NOT replace it). Use a **plain-text forward-reference** for the
`./inner_product.md` chapter name (NOT a live markdown link), per the cycle-017
build-break lesson (mdbook-linkcheck2 rejects links to not-yet-authored
chapters) — the row above already uses the plain-text "(chapter
`./inner_product.md` to be authored by harvester)" form, matching how the
`linear_combination` row was de-linked at integration.

Note: this report does **not** create `book/src/L2/inner_product.md`. That is
harvester's job (formalization). Combinator-miner only adds the dep-map rough-in
row.

Suggested companion (integrator may apply or defer to harvester): the L2
"Working Notes" section could gain a provenance bullet mirroring the
`krylov-step` / `linear_combination` precedent:
- **Pattern provenance** (combinator-miner:2026-05-28T231046Z): the
  reduce-to-scalar inner-product fold sibling to `linear_combination`. Members:
  `dot` (real + complex-Hermitian), `tdot` (complex-unconjugated),
  `bilinear-form` (M-weighted). Conjugation-convention and weighting are variant
  axes, not separate operators. `matrix-weighted-norm` is a consumer
  (`√ ∘ inner_product_M`), not an instance. Closes OQ
  `inner-product-fold-sibling-candidate`; completes the "algebra of folds"
  (tensor-producing `linear_combination` + scalar-producing `inner_product`).

## Supporting evidence

All Palace ranges self-verified via codemap `read_range` / `search_text` /
`get_symbol_def` this invocation:

- `palace/linalg/vector.cpp:263-274` — `ComplexVector::Dot` (Hermitian, `&y==this` imag-0 fast path) and `ComplexVector::TransposeDot` (unconjugated, `&y==this → 2·Imag·Real`). **Verified** (exact match to `book/src/L1/dot.md:112-113`).
- `palace/linalg/vector.cpp:665-685` — `linalg::LocalDot(Vector,Vector)` (real, via `hypre_SeqVectorInnerProd`) and `LocalDot(ComplexVector,ComplexVector)` (four real LocalDot calls + self-dot imag-0 fast path). **Verified**.
- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot`/`TransposeDot` decls + comment "Vector dot product (yᴴ x) or indefinite dot product (yᵀ x)"; `operator*` aliased to `Dot`. **Verified**.
- `palace/linalg/vector.hpp:242-253` — `linalg::LocalDot` decls (real + complex) + the `Dot(comm, x, y)` template (`LocalDot` + `Mpi::GlobalSum`). **Verified**.
- `palace/linalg/operator.cpp:621-639` — `Dot(comm, x, A, y)` (real `Operator` weight) and `Dot(comm, x, ComplexOperator, y)` (complex weight): both `A.Mult(x, Ax); return Dot(comm, Ax, y)` — direct evidence the M-weighted fold is `apply-then-plain-dot`, i.e. plain `dot` is the `M = I` case. **Verified**.
- `palace/linalg/operator.hpp:386-394` — `Dot(comm,x,A,y)` overload decls + comments "Compute the bilinear form inner product yᴴ A x". **Verified**.
- `palace/linalg/operator.cpp:599-619` — `Norml2(comm, x, B, Bx)` (real + complex): `B.Mult(x,Bx); dot = Dot(comm,Bx,x); return sqrt(dot)` — direct evidence `matrix-weighted-norm` is `√ ∘ inner_product_M` at `y=x` with an `MFEM_ASSERT(dot > 0)` SPD guard, hence a **consumer**, not an instance. **Verified**.
- `palace/linalg/operator.hpp:372-384` — `Norml2`/`Normalize` weighted-norm decls. **Verified**.
- `palace/linalg/iterative.cpp:22-32` — `CheckDot` template pair: `MFEM_ASSERT(isfinite(dot) && dot >= 0.0, …)` (real) and `… && dot.real() >= 0.0` (complex). **Verified** — the runtime PSD guard on the Hermitian/SPD inner-product member.
- `palace/linalg/iterative.cpp:396,410,445,461,569,584,643,757,763,822` — `CheckDot(...)` call sites in CG/GMRES/FGMRES (`(Br,r)`, `(Ap,p)`, residual-norm guards). **Verified** via `search_text` (12 hits total, the 2 decls + 10 call sites).

Artifact citations (read this invocation):
- `book/src/L1/dot.md` — the firm `dot`/`tdot` leaves: full signatures (`:16-17`), element-type/conjugation table (`:31-35`), laws (`:55-81`), variant axes (`:89-96`). Authoritative on the conjugation-convention and PSD facts cited above.
- `book/src/concepts/dot.md` — BLAS-1 heritage framing (`zdotc`/`zdotu`/`ddot`); the cross-cutting prose home for `inner_product`'s narrative.
- `book/src/L1/bilinear-form.md:17-53` — the M-weighted `xᴴ M y` L1 rough-in (Instance 4); its `bilinear_form(x, I, y) = dot(x, y)` specialization law is the direct `M = I` evidence.
- `book/src/L1/matrix-weighted-norm.md:13, 18-19, 33-37` — the SPD `√(xᴴ B x)` operator; cited as a **consumer** (`√ ∘ inner_product_M`), with its own SPD-precondition / outer-√ structure that keeps it OUT of the inner-product fold.
- `book/src/L2/index.md:17, 22-25` — L2 charter (`dot` in overlay vocabulary) + dep-map (rough-in row target; `linear_combination` row at `:25` is the sibling/append-anchor).
- `reports/2026-05-28T223022Z-combinator-miner-linear-combination-fold/CYCLE.md` §Open questions 1 + §Summary — the cycle-017 dot-distinction that spawned this proposal.
- `scaffolding/open-questions.md` §`inner-product-fold-sibling-candidate` (the OQ this dispatch addresses) + §`blas1-variadic-linear-combination-fold-unification` (the parent "algebra of folds, not mega-combinator" nuance) + §`matrix-weighted-norm-and-bilinear-form-l1-rough-ins` (the M-weighting cohort context).

Tests exercising the pattern (L0-equivalent):
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*` (`double dot = vec1 * vec2; CHECK_THAT(dot, WithinRel(32.0))`) — cited transitively via `book/src/L1/dot.md:118`; the empirical-match anchor for Instance 1. Harvester should pull the concrete assertion (and any complex-dot / bilinear-form test, if surfaced) to anchor the laws as `empirical_match` per `feedback_tests_as_semantic_supplement`.
- `test/unit/test-orthog.cpp:157,219-220,271,313-315,373-376` — `linalg::Dot` as the orthogonalisation-coefficient primitive (cited via `book/src/L1/dot.md:119`); live evidence the Hermitian member is the workhorse of the Krylov/orthogonalisation surface.

## Open questions / caveats

1. **M-weighting unification scope — proposed as a variant AXIS, with `matrix-weighted-norm` explicitly held OUT.** I unify the *plain* and *M-weighted* inner products under one `inner_product` (weighting axis, `M = I` the plain case) because the L0 evidence is unambiguous (`Dot(comm,x,A,y)` literally is `apply-then-plain-dot`, `operator.cpp:621-639`) and the artifact already separates them as L1 operators (`dot` vs `bilinear-form`). I do **NOT** absorb `matrix-weighted-norm` — it adds an outer `√` and an SPD precondition, making it a *consumer composition* `√ ∘ inner_product_M|_{y=x}`, not a fold member. Recommend harvester keep this boundary: pulling SPD/√ into the inner-product algebra would pollute the fold's laws (the fold is defined for any `M`; the norm needs SPD). This is the "note but don't over-reach" the dispatch asked for. Whether the M-weighted member warrants its OWN L2 chapter vs. an axis-cell of `inner_product` is a harvester firm-up call (I lean: one chapter, weighting as an axis, mirroring how `dot.md` hosts `dot`+`tdot` in one chapter).

2. **Conjugation-convention is an AXIS, not separate operators — but `tdot`'s broken PSD law is load-bearing.** The three kernel members collapse to one operator with a conjugation-convention axis (mirroring `dot.md`'s existing axis treatment). The one subtlety harvester must preserve: the PSD law (and hence the `CheckDot` runtime guard, `iterative.cpp:22-32`) holds ONLY on the real/Hermitian cells, NOT the `unconjugated` (`tdot`) cell. So the axis is not law-preserving across all cells — the `tdot` cell drops PSD + Hermitian-symmetry. This is exactly how `dot.md:71-75, 94` already records it; the L2 entry should carry the same per-cell law caveat.

3. **L2>L1 lowering theme needed (abstractor work, not mine).** Once harvester formalizes `inner_product` at L2, an `L2-L1/inner-product-fold-specialization` theme should narrate the lowering: conjugation-convention → `dot`/`tdot` dispatch; weighting axis → `apply_linop(M,·)` then `dot` (or the fused `bilinear-form` leaf); the reduction-tree pin (Hypre + MPI) is the load-bearing numerical content. Parallels the `L2-L1/linear-combination-fold-specialization` theme the cycle-017 report flagged. Not authored here.

4. **Parallel-dispatch collision risk on the L2 dep-map.** A cycle-018 harvester is firming the `linear_combination` row (`reports/2026-05-28T231026Z-harvester-linear-combination-L2/`) at `book/src/L2/index.md:25` THIS cycle. My append-anchor is "after the `linear_combination` row" regardless of its settled firmness — integrator should sequence so my `inner_product` row lands after the harvester's `linear_combination` edit (per-report serialization makes this natural; flagging so the integrator does not treat the two edits as conflicting). My row does NOT touch the `linear_combination` row.

5. **Self-verify note on tests.** The `test/unit/test-vector.cpp` complex-dot and any `bilinear-form` value-check assertions were not re-read this invocation (Instance-1 real-dot assertion cited transitively via `dot.md:118`). Harvester should pull the concrete per-member assertions to anchor the laws as `empirical_match` rather than purely algebraic claims.

6. **No CYCLE.md write-filter block encountered** (per the role-spec instruction to surface filter blocks as an Open question). The report wrote to `reports/<id>/CYCLE.md` without incident.

7. **M-weighted conjugation/argument-order convention is NOT pinned here — harvester must firm it (caveat-note, rough-in).** This report uniformly writes the M-weighted member as the shorthand `xᴴ M y`. That shorthand does NOT exactly reconcile with the Palace-documented convention: the decl comment at `operator.hpp:386-394` documents `Dot(comm, x, A, y)` as the bilinear form **`yᴴ A x`**, and the body `A.Mult(x, Ax); return Dot(comm, Ax, y)` (`operator.cpp:621-639`) computes `dot(Ax, y) = (Ax)ᴴ y = xᴴ Aᴴ y` under the Hermitian-conjugate-first-arg `dot` convention. So which argument is conjugated and the exact `Aᴴ`-vs-`A` placement is a load-bearing conjugation-convention detail — precisely the kind this report elevates as load-bearing for plain `dot`. Treat every `xᴴ M y` in this report as a placeholder shorthand, NOT a pinned convention. Harvester should pin the exact form against the `operator.hpp:386-394` comment (`yᴴ A x`) and the `(Ax)ᴴ y` body algebra, and should inherit the resolution recorded for the related L0-comment-vs-implementation subtlety in `book/src/L1/bilinear-form.md` Status / OQ `bilinear-form-conjugation-convention-anchor` rather than introduce a fresh framing. Does not affect the rough-in verdict (the fold structure and the `M = I ⟹ plain dot` relationship are unchanged regardless of which argument carries the conjugate).
