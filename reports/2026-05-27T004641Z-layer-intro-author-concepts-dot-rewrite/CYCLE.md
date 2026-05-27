---
agent: layer-intro-author
invoked_at: 2026-05-27T00:46:41Z
scope: rewrite book/src/concepts/dot.md to align with L1/dot.md
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. concepts/dot.md whole-file rewrite + L1/dot.md:17 softening edit. Closes 4 open questions.
inputs:
  - .claude/agents/layer-intro-author.md (broadened scope, cycle-003)
  - book/src/concepts/dot.md (current; to be rewritten)
  - book/src/L1/dot.md (authoritative L1 operator entry)
  - reports/2026-05-27T001116Z-same-layer-cross-cutter-dot-concept-contradictions/CYCLE.md (cross-cutter trigger)
  - reference/palace/palace/linalg/vector.hpp:100-260 (re-verified Dot/TransposeDot/LocalDot/Dot declarations)
  - reference/palace/palace/linalg/vector.cpp:130-280 (re-verified body of vector.cpp:142-178 is NOT dot — it's Get/operator=/SetBlocks)
  - reference/palace/palace/linalg/vector.cpp:263-274 (re-verified ComplexVector::Dot and TransposeDot bodies)
  - reference/palace/palace/linalg/vector.cpp:665-685 (re-verified linalg::LocalDot real and complex)
  - `grep -rn 'Dotc' reference/palace/` (zero results — re-verified non-existence)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: artifact_landed
    rationale: Used to directly re-verify every citation in the rewritten concept page against `reference/palace/palace/linalg/vector.{hpp,cpp}`. The cross-cutter's claim that `vector.cpp:142-178` does not contain dot content was confirmed by reading the range (Get/operator=/SetBlocks). The L1 entry's citations (`vector.hpp:110-113`, `vector.hpp:242-253`, `vector.cpp:263-267`, `vector.cpp:269-274`, `vector.cpp:665-685`) were each independently re-read; all are accurate. The rewritten concept page cites only the verified ranges.
  - skill: classify-variant-axis
    triggered: true
    decision: explained_non_applicable
    rationale: This is a concept-page reconciliation, not an operator-promotion. Variant axes are documented in the L1 entry (`element-type`, `conjugation-convention`) and the concept page intentionally points to the L1 entry rather than re-listing them.
  - skill: cross-cutter-corpus-grep
    triggered: true
    decision: artifact_landed
    rationale: Used to re-verify the non-existence of `linalg::Dotc`: `grep -rn 'Dotc' reference/palace/` returns zero matches. The rewritten concept page omits every reference to the invented symbol and explicitly names `ComplexVector::Dot` (Hermitian) and `ComplexVector::TransposeDot` (unconjugated bilinear) per the source.
---

# REPORT: Rewrite concepts/dot.md

## Summary

Whole-file rewrite of `book/src/concepts/dot.md` to fix the three contradictions surfaced by the cycle-003 cross-cutter (`reports/2026-05-27T001116Z-same-layer-cross-cutter-dot-concept-contradictions/`):

1. **Return type.** Old page claimed `ComplexVector::Dot` returns *real*. Source returns `std::complex<double>` (`palace/linalg/vector.hpp:111`, body at `vector.cpp:263-267`). Rewrite states the correct element-type rule: real element-type → real return; complex element-type → complex return.
2. **Hallucinated symbol `linalg::Dotc`.** Old page named a non-existent symbol and inverted the conjugation polarity between `Dot` and `TransposeDot`. `grep -rn 'Dotc' reference/palace/` returns zero hits. Rewrite removes every reference to `Dotc` and correctly maps `ComplexVector::Dot` → Hermitian (`yᴴ x`), `ComplexVector::TransposeDot` → unconjugated bilinear (`yᵀ x`), matching the header comment at `palace/linalg/vector.hpp:110`.
3. **Bogus source range `vector.cpp:142-178`.** That range was directly re-read and contains `ComplexVector::Get` device-host dispatch, `operator=(std::complex<double>)`, and the start of `SetBlocks` — no dot content. The "projection definition" referenced in the old page does not exist as a Palace function. Rewrite replaces the bogus cite with the verified ranges from the L1 entry (`vector.cpp:263-267` for `Dot`, `vector.cpp:269-274` for `TransposeDot`).

The rewrite also restructures the page per the layer-intro-author discipline for concepts/ pages (cycle-003 spec broadening): the concept page is the narrative cross-cutting pointer; the L1 entry (`book/src/L1/dot.md`) is authoritative. The page preserves the salvageable BLAS-heritage framing (the old "Background" section's tie to BLAS-1 `ddot`/`zdotc` naming), drops the wrong "real-projected" rationalisation, and adds explicit forwarding text directing readers to `L1/dot.md` for laws, evidence, and variant axes.

Secondary edit proposed: small softening of the back-pointer warning at `book/src/L1/dot.md:17`. The current L1 text reads `Note: the concept page predates this entry and contains an inaccuracy (it claims ComplexVector::Dot returns a real scalar — it returns std::complex<double>); the L1 entry is authoritative.` Once `concepts/dot.md` is corrected, the inline warning is redundant and confusing. The proposed edit deletes the warning while keeping the authoritative-pointer statement.

New concept-page word-count: ~310 words of prose (excluding code blocks and citations). Within the layer-intro-author discipline's "under 200 words for the prose" guidance for layer intros, slightly relaxed here because a concept page must carry its own one-line semantics, BLAS context, and the explicit list of slice-usages; the bulk is still pointer-and-narrative, not operator algebra.

## Proposed changes

````edit:book/src/concepts/dot.md
[old]: # dot

Base primitive: `α ← ⟨x, y⟩` — inner product of two conforming vectors. For real spaces, `α = Σ x[i] · y[i]`; for complex, `α = Σ x̄[i] · y[i]` (conjugate-linear in the first argument by Palace convention; check the slice's L0 citations for the exact convention in use).

## Contract

- Reads both operands; writes none.
- **Reduction.** In a distributed setting, `dot` carries a load-bearing MPI collective (typically `MPI_Allreduce` on a partial sum). The collective is implicit at L2 — slices that care about its cost or scheduling state that explicitly.
- **Associativity.** Floating-point summation order is non-associative; different reduction trees give different bit-level results. When this matters (deterministic builds, bit-reproducibility) the slice flags it as a load-bearing numerical claim.

## Role in higher-layer rotations

`dot` is the workhorse of orthogonalisation and convergence tests. MGS uses one `dot` per basis vector; CGS uses `j+1` `dot`s as a batch (one collective); CGS2 doubles that. `nrm2(x) = √dot(x, x)`.

## Palace mapping

- `linalg::Dot` and `linalg::Dotc` in `palace/linalg/vector.{hpp,cpp}`.
- The complex-conjugate version is `Dotc`; the un-conjugated bilinear version is `Dot`.

## Concept: `dot`

Inner product of two vectors: `⟨x, y⟩` (returns a scalar).

## Background

BLAS-1 `ddot` / `zdotc`. The complex case is subtle: the canonical BLAS
Hermitian inner product `⟨x, y⟩ = x^H y` returns a complex scalar.
Palace's `Vector::Dot` and `ComplexVector::Dot` both return a **real**
scalar — for the real case the natural definition, for the complex
case the real-projected form `Re⟨x, y⟩` (suitable when the recurrence
requires only the SPD form, as in CG).

This projection is a deliberate API choice, not a primitive deficiency:
Krylov recurrences for SPD or self-adjoint problems use only the real
form; recurrences that require the full complex inner product (e.g.,
GMRES residual-norm computations on complex iterates) compose multiple
dot calls. See
[palace/linalg/vector.cpp:142-178](../../../reference/palace/linalg/vector.cpp#L142-L178)
for the projection definition.

## Signature (canonical)

```
dot(x, y) → ℝ                    // real-projected for complex case
```

## Variant axes

- **Scalar field**: absorbed at the contract level (return type is
  always real). The complex case projects via `std::real`.
- **Conjugation convention**: Palace fixes `Re x^H y` for complex; other
  libraries may expose both `cdotc` and `cdotu`. Out of scope here.

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [gmres](../spec/slices/gmres.md) — orthogonalization coefficients
  `⟨v_i, w⟩` (CGS/MGS), at the L2 unfolding of `orthogonalize`.
[new]: # dot

Cross-cutting concept page for the inner-product reduction primitive. The
authoritative operator definition (signatures, algebraic laws, variant
axes, evidence) lives at [`L1/dot`](../L1/dot.md); this page is the
narrative pointer plus the BLAS-heritage framing.

## One-line semantics

`α = dot(x, y) = Σ_i kernel(x[i], y[i])` — a pure reduction of two
conforming vectors to a scalar. The per-element kernel depends on the
element type and on the conjugation convention; see the [L1
entry](../L1/dot.md) for the full element-type → return-type table.

## Background: BLAS-1 heritage

Palace's dot family inherits its shape from BLAS-1 `ddot` / `zdotc` /
`zdotu`. The real case is the textbook bilinear form `Σ x[i] · y[i]`;
the complex case has two distinct flavours, which Palace exposes as
separate methods:

- **`ComplexVector::Dot`** (`palace/linalg/vector.hpp:111`) — the
  Hermitian sesquilinear inner product `yᴴ x`, conjugate-linear in the
  argument `y` and linear in the receiver `*this`. Returns
  `std::complex<double>`. Body at `palace/linalg/vector.cpp:263-267`.
  Analogous to BLAS-1 `zdotc`.
- **`ComplexVector::TransposeDot`** (`palace/linalg/vector.hpp:112`) —
  the unconjugated bilinear form `yᵀ x`. Returns
  `std::complex<double>`. Body at `palace/linalg/vector.cpp:269-274`.
  Analogous to BLAS-1 `zdotu`. Method-form only; there is no free
  function `linalg::TransposeDot`.

The header comment at `palace/linalg/vector.hpp:110` summarises both:
"Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex
vectors."

The real case is `mfem::Vector::operator*(const Vector &) → double` and
the parallel free function `linalg::Dot(MPI_Comm, x, y)` template
(`palace/linalg/vector.hpp:247-253`) which dispatches `LocalDot` plus
`Mpi::GlobalSum` (a Palace wrapper over `MPI_Allreduce`). The real `LocalDot` is at
`palace/linalg/vector.cpp:665-672`; the complex `LocalDot` is at
`palace/linalg/vector.cpp:674-685`.

## Return type — the L1 element-type rule

| element type | `dot(x, y)` returns | per-element kernel | Palace mapping |
|---|---|---|---|
| `real`    | `real`    | `x[i] * y[i]`       | `mfem::Vector::operator*`, `linalg::Dot<Vector>` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian)* | `ComplexVector::Dot`, `linalg::Dot<ComplexVector>` |
| `complex` (`tdot`) | `complex` | `x[i] * y[i]` *(unconjugated)* | `ComplexVector::TransposeDot` (method only) |

The complex case returns a complex scalar, not a real one. The
"real-projection" view (e.g. `std::real(dot(x, x))`, `std::abs(dot(x, y))`)
arises only at call sites that know algebraically the result must be
real (CG's `β = ⟨r, z⟩` for SPD problems) or that want a norm
(`palace/linalg/nleps.cpp:487` uses `std::abs(linalg::Dot(...))`). That
projection is caller-side, not built into `dot`.

## Caveats and load-bearing facts

- **MPI reduction.** The free function `linalg::Dot` carries an
  `MPI_Allreduce` over the partial sums. Out of scope for single-rank
  builds per CLAUDE.md "Scope"; recorded in the L1>L0 lowering.
- **Reduction non-associativity.** Floating-point summation order is
  non-associative; different reduction trees give different bit-level
  results. Load-bearing for deterministic builds; see the L1 entry's
  "Semantics" section for the algebraic claim.
- **Self-dot fast path.** When `&x == &y`, the imaginary part is zero
  exactly (Hermitian case) and the code elides the cancellation
  (`vector.cpp:266`, `vector.cpp:678`). Transparent performance trick.

## Slices that use this primitive

- [cg](../spec/slices/cg.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [gmres](../spec/slices/gmres.md) — orthogonalization coefficients
  `⟨v_i, w⟩` (CGS/MGS), at the L2 unfolding of `orthogonalize`.

## See also

- [`L1/dot`](../L1/dot.md) — authoritative operator entry: full
  signatures, algebraic laws, variant axes, complete L0 evidence list.
  **If this page and the L1 entry disagree on any factual claim about
  the Palace surface, the L1 entry wins.**
````

```edit:book/src/L1/dot.md
[old]: A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page predates this entry and contains an inaccuracy (it claims `ComplexVector::Dot` returns a real scalar — it returns `std::complex<double>`); the L1 entry is authoritative.
[new]: A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative pointer plus BLAS-1 heritage framing. The L1 entry is authoritative on every factual claim about the Palace surface.
```

## Supporting evidence

Citations re-verified directly from `reference/palace/`:

- **`palace/linalg/vector.hpp:110-113`** — header comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` declares `std::complex<double> Dot(...)` and `std::complex<double> TransposeDot(...)`. *Verified by direct read; refutes old concept page's "returns a real scalar" claim and its `Dot`/`Dotc` symbol naming.*
- **`palace/linalg/vector.cpp:263-267`** — `ComplexVector::Dot` body. Real part `Real()·y.Real() + Imag()·y.Imag()`; imag part `(this == &y) ? 0.0 : (Imag()·y.Real() - Real()·y.Imag())`. *Verified; this is the Hermitian kernel `yᴴ x`.*
- **`palace/linalg/vector.cpp:269-274`** — `ComplexVector::TransposeDot` body. Real part `Real()·y.Real() - Imag()·y.Imag()`; imag part with self-dot fast path. *Verified; this is the unconjugated bilinear kernel `yᵀ x`.*
- **`palace/linalg/vector.cpp:142-178`** — re-read directly. Contains: (a) tail of `ComplexVector::Get` device-host pointer dispatch (lines 130-163); (b) `ComplexVector::operator=(std::complex<double> s)` (lines 165-170); (c) start of `void ComplexVector::SetBlocks(...)` (lines 172-178). **No dot, projection, or inner-product code anywhere in this range.** *Refutes old concept page's `vector.cpp:142-178` citation outright; range removed from rewritten page.*
- **`palace/linalg/vector.hpp:242-244`** — `linalg::LocalDot` declarations for real and complex inputs.
- **`palace/linalg/vector.hpp:247-253`** — free-function `linalg::Dot` template (`LocalDot` + `Mpi::GlobalSum`).
- **`palace/linalg/vector.cpp:665-672`** — real `LocalDot` via Hypre's `hypre_SeqVectorInnerProd`.
- **`palace/linalg/vector.cpp:674-685`** — complex `LocalDot`: four real `LocalDot` calls combined; self-dot fast path returns imag = 0 exactly.
- **`grep -rn 'Dotc' reference/palace/`** — zero matches. *Refutes old concept page's `linalg::Dotc` symbol; removed from rewrite.*

Cross-references in the rewritten concept page:

- Forwarding link to `../L1/dot.md` (authoritative) — three occurrences (header, semantics, "See also").
- Preserved slice-usage links: `../spec/slices/cg.md`, `../spec/slices/gmres.md`.

## Open questions / caveats

1. **Sweep concepts/ for analogous pre-layered-era contamination.** Cross-cutter open-question (3) and integration-note (4) flagged that other concept pages may have the same pattern (hallucinated symbols, stale citations, wrong return-type framings written from BLAS API memory rather than Palace source). This rewrite handles only `concepts/dot.md`; an audit pass over `book/src/concepts/` would be a candidate dispatch for cycle-005. Not in scope here.

2. **Slice-link targets exist but are unverified for layered-era accuracy.** The rewritten page preserves links to `../spec/slices/cg.md` and `../spec/slices/gmres.md`. These are pre-layered-era slice documents (Phase 1 corpus, see CLAUDE.md "Layout"). They are kept because (a) the cross-cutter's diff did not flag them and (b) the layer-intro-author discipline says preserve valid prose. Whether the linked slice files themselves accurately describe `dot` usage at L2/L3 is a separate audit that would belong to a same-layer-cross-cutter on those slice pages.

3. **Secondary edit on `L1/dot.md:17` is in-scope per cross-cutter open-question (4).** The cross-cutter explicitly recommended the cycle-004 REPORT propose the back-pointer edit "as part of the diff for the integrator to apply." Done above. If the integrator decides the rewrite of `concepts/dot.md` and the back-pointer softening should land in separate cycles for atomicity, both edits are independent and either can be deferred.

4. **`tdot` is named in the L1 entry but `ComplexVector::TransposeDot` is method-form only.** The concept page rewrite states this fact explicitly ("Method-form only; there is no free function `linalg::TransposeDot`.") to prevent the same hallucination from recurring. If a future surface adds `linalg::TransposeDot`, both the concept page and the L1 entry will need updating.

5. **Word-count discipline.** Layer-intro-author spec target is "under 200 words for the prose" (for layer intros). Concept pages may need slightly more (one-line semantics + BLAS heritage + return-type table + caveats + slice index = ~310 words here). Flagging as a possible role-spec refinement for meta-phase: the 200-word target was written for layer intros where the dep-map carries the structure; concept pages have no dep-map and carry their own structure inline. Not a blocker; just a friction point worth recording.
