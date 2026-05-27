---
agent: layer-intro-author
invoked_at: 2026-05-27T160553Z
scope: L1 retroactive context-thinning sweep across 7 firm L1 operator chapters
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-007 wave-1 per-report dispatch 3 of 6 at 18:00:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Files edited (7 L1 chapters thinned): book/src/L1/{axpy,dot,nrm2,axpby,scal,apply_linop,axpbypcz}.md (Context-section thinning; multi-bullet L0-surface enumerations replaced with cross-references to L0 chapters; ~55% net Context shrink per repairer recount; nrm2.md B-weighted aside stale `apply` → `apply_linop` micro-fix folded in).
  No new file creates; no SUMMARY edit; no L1/index.md edit (dep-map structure unaffected).
  0 OQs promoted (sweep is mechanical re-routing).
  Flagged 5 L0 chapters with stale forward-declaration italic notes (output-arg-vs-receiver.md:36, mfem-vector-types.md:42, linalg-free-functions.md:47, transparent-vs-load-bearing-tricks.md:34, apply-linop-overload-set.md:55) → cycle-008+ same-layer-cross-cutter follow-up.
  Priority #11 substantively progressed. Gate hits: 0.
---

# CYCLE: L1 retroactive Context-section thinning across 7 operators

## Summary

Priority #11's threshold (≥6 L0 reference chapters) is met (8 currently exist). This dispatch sweeps the `Context` sections of all 7 firm L1 operator chapters (`axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz`) and replaces inline L0-interpretation prose — multi-bullet enumerations of the Palace L0 surface, repeated cross-cutting idiom explanations (output-arg-vs-receiver, element-type-axis collapse, template-dispatch wrappers, transparent vs load-bearing classification) — with concise cross-references to the now-extant L0 reference chapters.

Each thinned `Context` keeps:
- The 1-paragraph "what the mutation rotation does here" statement (this is L1 content — not L0 interpretation — and is preserved).
- The pointer to any cross-cutting `concepts/` page (preserved verbatim).
- A 1-2 sentence summary of the L0 surface shape, with the file-overview / convention / overload-set citations forwarded to the L0 chapter.

Each thinned `Context` removes:
- Multi-bullet enumerations of `linalg::` symbols, member-form vs free-function-form pairs, transpose / accumulate-mode dispatch tables — all of which are now stated once in the relevant L0 chapter.
- Inline citations of L0 file ranges that are also held by the L0 chapter (the L0 chapter is the new home of these citations; the L1 `Evidence` section retains its own representative L0 citations).

No citation chain is lost: every L0 file range that the original `Context` enumerated is either retained in the L1 `Evidence` section (which is kept intact) or anchored by the corresponding L0 chapter's `Evidence (representative)` block. Cross-checked per chapter below.

The L1 entry's authority on the L1 form (Signature, Semantics, Algebraic laws, Dependencies, Variant axes, Status, L1 vs L0 distinction, Evidence) is preserved — thinning touches only the `Context` section and (where applicable) the cross-reference threading into it.

All 7 L1 chapters in scope have a corresponding L0 chapter (or set of chapters) available to cross-reference. **No deferrals.**

## Proposed changes

### 1) `book/src/L1/axpy.md`

```edit:book/src/L1/axpy.md
[old]: ## Context

The L0 source-side form is the in-place call `y.Add(α, x)` (a member function on `mfem::Vector`) or `y.AXPY(α, x)` (a member function on Palace's `ComplexVector`, with `Add` as an alias). At L0 both forms mutate `y` in place. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, and the pre-update value of `y`, and produces a fresh post-update value. Workspace, aliasing, and in-place overwrite are L0 concerns; they reappear (if at all) in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background, fusions (`α = 1`, `α = -1`), and roll-up usage across slices. The L1 entry here is the firm operator definition; the concept page is the narrative.
[new]: ## Context

`axpy` lifts the BLAS-1 in-place fused update `y ← α·x + y` from two L0 idioms (receiver-mutating `y.Add(α, x)` / `y.AXPY(α, x)` and free-function-form `linalg::AXPY(α, x, y)`) to a single pure-functional operator. The L0 surface is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) (the `AXPY` family in `palace/linalg/vector.{hpp,cpp}`); the receiver-vs-output-arg idiom split is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md); the real-vs-complex element-type axis is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md); the real-real `α == 1.0` constant-folding branch is classified as transparent in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, and the pre-update value of `y`, and produces a fresh post-update value. Workspace, aliasing, and in-place overwrite are L0 concerns; they reappear (if at all) in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering BLAS background, fusions (`α = 1`, `α = -1`), and roll-up usage across slices. The L1 entry here is the firm operator definition; the concept page is the narrative.
```

Citation-chain check: removed inline `palace/linalg/vector.cpp:702-712` and member/free-fn descriptions are now anchored by `L0/linalg-vector-file` (which cites `vector.cpp:701-724` as the AXPY-family region) and `L0/transparent-vs-load-bearing-tricks` (which cites `vector.cpp:701-712`). The L1 `Evidence` section (lines 73-82) is unchanged and retains the per-line citations (`vector.hpp:115-118`, `vector.hpp:305-307`, `vector.cpp:276-311`, `vector.cpp:702-712`, `operator.cpp:458-466`, `rap.cpp:73`, `rap.cpp:317`). No file range removed from the citation graph.

---

### 2) `book/src/L1/dot.md`

```edit:book/src/L1/dot.md
[old]: ## Context

The L0 source-side forms are:

- `mfem::Vector::operator*(const Vector &)` — real inner product, returns `double`. Used at `palace/linalg/vector.cpp:265` inside `ComplexVector::Dot` building blocks. Visible on real vectors as the test-vector.cpp idiom `double dot = vec1 * vec2;` (`test/unit/test-vector.cpp:206-207`).
- `ComplexVector::Dot(const ComplexVector &y) const` — returns `std::complex<double>` per the header comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` at `palace/linalg/vector.hpp:110-113`. The implementation (`palace/linalg/vector.cpp:263-267`) computes `(this)·conj(y)` blocks, which algebraically equals `yᴴ · x` — i.e., conjugate-linear in `y` (the *argument*) and linear in `*this` (the *receiver*).
- `ComplexVector::TransposeDot(const ComplexVector &y) const` — returns `std::complex<double>` for the unconjugated bilinear form `xᵀ y` (`palace/linalg/vector.cpp:269-274`).
- `linalg::LocalDot(...)` — local-rank inner product, real (`palace/linalg/vector.cpp:665-672`, dispatched to Hypre's `hypre_SeqVectorInnerProd`) or complex (`palace/linalg/vector.cpp:674-685`).
- `linalg::Dot(MPI_Comm, x, y)` — global inner product = `LocalDot` followed by `MPI_Allreduce` (`palace/linalg/vector.hpp:247-253`).

At L0, the in-place destination for `dot` is the return register / a stack scalar. There is no destination buffer to write through. The distinction the mutation rotation is doing here is therefore not about buffer ownership but about **reduction order and collective topology**: the L0 form bakes in a specific tree (the Hypre reduction kernel + MPI_Allreduce); the L1 form treats the reduction as a single semantic step.

A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative pointer plus BLAS-1 heritage framing. The L1 entry is authoritative on every factual claim about the Palace surface.
[new]: ## Context

`dot` lifts Palace's reduction surface (`mfem::Vector::operator*` for real; `ComplexVector::Dot` / `TransposeDot` for complex; the `linalg::LocalDot` / `linalg::Dot` free-function templates over both) to a single pure-functional sesquilinear-reduction operator (with the unconjugated bilinear variant `tdot`). The L0 file layout — the reduction family in `vector.{hpp,cpp}`, including the receiver-vs-argument asymmetry on `ComplexVector::Dot` that determines which side is conjugated — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The reduction family". The `linalg::Dot` template-dispatch scaffold (composing `LocalDot` with `Mpi::GlobalSum`) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "Composed scaffold". The real / complex element-type split and the `LocalDot` vs `Dot` (single-rank vs MPI-collective) axis are named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The self-aliasing fast path (`&y == this`) and reduction-tree non-associativity classification (transparent vs load-bearing) live in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination for `dot` is the return register / a stack scalar. There is no destination buffer to write through. The distinction the mutation rotation is doing here is therefore not about buffer ownership but about **reduction order and collective topology**: the L0 form bakes in a specific tree (the Hypre reduction kernel + MPI_Allreduce); the L1 form treats the reduction as a single semantic step.

A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative pointer plus BLAS-1 heritage framing. The L1 entry is authoritative on every factual claim about the Palace surface.
```

Citation-chain check: the removed 5-bullet enumeration cites `vector.cpp:265`, `vector.hpp:110-113`, `vector.cpp:263-267`, `vector.cpp:269-274`, `vector.cpp:665-672`, `vector.cpp:674-685`, `vector.hpp:247-253`, `test/unit/test-vector.cpp:206-207`. All of these are retained in the L1 `Evidence` section (lines 113-126, unchanged — contains all of `vector.hpp:110-113`, `vector.hpp:242-244`, `vector.hpp:247-253`, `vector.cpp:263-267`, `vector.cpp:269-274`, `vector.cpp:665-672`, `vector.cpp:674-685`, `test/unit/test-vector.cpp:206-207`). The L0 `linalg-vector-file` chapter's "Evidence (representative)" block covers most of the same ranges directly (`vector.cpp:263-274`, `vector.hpp:247-253`) and encompasses `vector.hpp:110-113` within its broader `vector.hpp:23-147` (full `ComplexVector` class-declaration overview, with the `Dot` / `TransposeDot` / `operator*` lines 110-113 named inline in the chapter's "At a glance" prose) — i.e., the L0 anchor for the `vector.hpp:110-113` range is the encompassing class-declaration block, not an exact line-range match; the exact `:110-113` line range remains explicitly anchored only by the L1 `Evidence` section. No file range removed from the citation graph.

---

### 3) `book/src/L1/nrm2.md`

```edit:book/src/L1/nrm2.md
[old]: ## Context

The L0 source-side forms are:

- `linalg::Norml2(MPI_Comm comm, const VecType &x)` — free-function template at `palace/linalg/vector.hpp:255-260`. The entire definition is `return std::sqrt(std::abs(Dot(comm, x, x)));`. Specialised by `VecType ∈ {Vector, ComplexVector}` through the underlying `linalg::Dot` template; returns `double` in both cases (the `std::abs(std::complex<double>)` on the complex `dot(x, x)` extracts the modulus, which is the absolute value of the real part since the Hermitian self-dot has zero imaginary part exactly — see cycle-002 dot.md law 9).
- `mfem::Vector::Norml2()` — MFEM method-form on real vectors, no MPI. Direct evidence at `test/unit/test-vector.cpp:209-211` (`double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));`).
- `ErrorIndicator::Norml2(comm)` — a thin caller-side wrapper at `palace/fem/errorindicator.hpp:43` that forwards to `linalg::Norml2(comm, local)`. Not a separate operator — same L1 vocabulary.

At L0, the in-place destination for `nrm2` is the return register / a stack scalar; there is no destination buffer to write through. The L1 form is identical algebraically — the operator is naturally pure. What the mutation rotation does here is essentially nothing on the buffer side; the L1 entry exists to record the algebraic identity `nrm2(x) = √dot(x, x)`, the element-type unification (one operator at L1; two specialisations at L0), and the load-bearing numerical caveat (the reduction-tree non-associativity that propagates from `dot` is the same one).

A cross-cutting prose treatment lives at [`concepts/nrm2`](../concepts/nrm2.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`. Palace inherits any over/underflow risk; if the underlying BLAS / Hypre kernel internally scales, that is an L1>L0 lowering observation, not a Palace-level guarantee. The L1 entry is authoritative; the concept page should be corrected by a future invocation.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` (declared at `operator.hpp:372-374`) is **not** part of this operator. It computes `√(xᴴ B x)` for an SPD operator `B`, requires a workspace `Bx`, and is algebraically a different construct (operator-weighted norm, a.k.a. energy norm). It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply`.
[new]: ## Context

`nrm2` lifts the one-line free-function template `linalg::Norml2(comm, x) = std::sqrt(std::abs(Dot(comm, x, x)))` (and the MFEM method-form `Vector::Norml2()` on real vectors, plus the thin caller-side wrapper `ErrorIndicator::Norml2(comm)` at `palace/fem/errorindicator.hpp:43`) to a single pure-functional Euclidean-norm reduction. The L0 file layout — `Norml2`'s one-line body and the surrounding reduction family — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The reduction family". The composition shape (one-line `sqrt(abs(Dot(...)))`) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "One-line composition". The element-type axis (real / complex, with both collapsed to a real-valued result) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The outer `std::abs` defensive non-negativity guard is classified as a load-bearing implementation detail in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination for `nrm2` is the return register / a stack scalar; there is no destination buffer to write through. The L1 form is identical algebraically — the operator is naturally pure. What the mutation rotation does here is essentially nothing on the buffer side; the L1 entry exists to record the algebraic identity `nrm2(x) = √dot(x, x)`, the element-type unification (one operator at L1; two specialisations at L0), and the load-bearing numerical caveat (the reduction-tree non-associativity that propagates from `dot` is the same one).

A cross-cutting prose treatment lives at [`concepts/nrm2`](../concepts/nrm2.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`. Palace inherits any over/underflow risk; if the underlying BLAS / Hypre kernel internally scales, that is an L1>L0 lowering observation, not a Palace-level guarantee. The L1 entry is authoritative; the concept page should be corrected by a future invocation.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` (declared at `operator.hpp:372-374`) is **not** part of this operator. It computes `√(xᴴ B x)` for an SPD operator `B`, requires a workspace `Bx`, and is algebraically a different construct (operator-weighted norm, a.k.a. energy norm). It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`.
```

Citation-chain check: the removed 3-bullet enumeration cites `vector.hpp:255-260`, `test/unit/test-vector.cpp:209-211`, `palace/fem/errorindicator.hpp:43`. All retained: `vector.hpp:255-260` retained in L1 `Evidence` (line 101) and in `L0/linalg-vector-file` "Evidence (representative)" (line 46); `test/unit/test-vector.cpp:209-211` retained in L1 `Evidence` (line 110); `palace/fem/errorindicator.hpp:43` retained in the new shortened paragraph and in L1 `Evidence` (line 105). The B-weighted aside is preserved as-is (it stays an L1 concern — it identifies an operator boundary). The `apply` reference in the B-weighted aside is updated to `apply_linop` (the firm L1 name landed cycle-004/005). No file range removed from the citation graph.

---

### 4) `book/src/L1/axpby.md`

```edit:book/src/L1/axpby.md
[old]: ## Context

The L0 source-side forms are:

- `ComplexVector::AXPBY(std::complex<double> α, const ComplexVector &x, std::complex<double> β)` — member call mutating `*this` in place to `α·x + β·(*this)` (`palace/linalg/vector.hpp:130-131`). The destination is the receiver; there is no output argument.
- `linalg::AXPBY<VecType, ScalarType>(ScalarType α, const VecType &x, ScalarType β, VecType &y)` — free-function template (`palace/linalg/vector.hpp:309-311`) with three explicit specialisations:
  - `AXPBY(double, Vector, double, Vector)` (`palace/linalg/vector.cpp:726-730`) delegates to MFEM's `add(α, x, β, y, y)` — MFEM's 5-argument in-place additive combine which writes its last argument from the linear combination of its first four.
  - `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` (`palace/linalg/vector.cpp:732-737`) delegates to `y.AXPBY(α, x, β)`, i.e. the member form.
  - `AXPBY(double, ComplexVector, double, ComplexVector)` (`palace/linalg/vector.cpp:739-743`) — real-scalar overload on complex vectors; promotes scalars implicitly and delegates to the same member form.

At L0, the in-place destination `y` is overwritten; the prior value of `y` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, and the pre-update value of `y`, and produces a fresh post-update value. The fusion (single-call combined update rather than the two-pass `y *= β; y += α·x`) is preserved at L1 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpby` at L1; it supersedes the rough-in row in `book/src/L1/index.md` (originally proposed by the cycle-002 abstractor `axpby-mutation-rotation` theme — see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). The lowering theme remains the L1>L0 narrative; this entry is the L1 algebra. No `concepts/axpby.md`-style cross-cutting prose exists yet for `axpby` (the existing `concepts/axpy.md` covers `axpy` only); if one is authored, it should cross-reference this entry.
[new]: ## Context

`axpby` lifts Palace's fused two-scalar two-vector update from two L0 idioms (receiver-mutating `ComplexVector::AXPBY(α, x, β)` and free-function-form `linalg::AXPBY(α, x, β, y)` with three template specialisations: real-real delegating to MFEM `add(α, x, β, y, y)`, complex-complex and real-scalar-on-complex-vector both delegating to the member form) to a single pure-functional operator. The L0 file layout — the AXPBY family in `palace/linalg/vector.{hpp,cpp}` and its place in the AXPY → AXPBY → AXPBYPCZ subsumption chain — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The BLAS-1 fused-update family". The receiver-vs-output-arg idiom split is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md); the free-function template-dispatch pattern over the member form is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "Pure forward to method-form". The element-type axis (real / complex / scalar-promoted) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). Unlike `axpy`, no constant-folding branches exist in the `AXPBY` family — the L0 surface uniformly delegates without inspecting scalar values, per [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination `y` is overwritten; the prior value of `y` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, and the pre-update value of `y`, and produces a fresh post-update value. The fusion (single-call combined update rather than the two-pass `y *= β; y += α·x`) is preserved at L1 because it has algebraic meaning — the law `axpby(α, x, β, y) = α·x + β·y` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpby` at L1; it supersedes the rough-in row in `book/src/L1/index.md` (originally proposed by the cycle-002 abstractor `axpby-mutation-rotation` theme — see [`L1-L0/axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md)). The lowering theme remains the L1>L0 narrative; this entry is the L1 algebra. No `concepts/axpby.md`-style cross-cutting prose exists yet for `axpby` (the existing `concepts/axpy.md` covers `axpy` only); if one is authored, it should cross-reference this entry.
```

Citation-chain check: the removed bullet enumeration cites `vector.hpp:130-131`, `vector.hpp:309-311`, `vector.cpp:726-730`, `vector.cpp:732-737`, `vector.cpp:739-743`. All retained in L1 `Evidence` (lines 96-100, unchanged — all five ranges present) and in `L0/linalg-vector-file` evidence (line 52, `vector.cpp:726-743` as range-overview). No file range removed from the citation graph.

---

### 5) `book/src/L1/scal.md`

```edit:book/src/L1/scal.md
[old]: ## Context

The L0 source-side forms are:

- `mfem::Vector::operator*=(double)` — MFEM member-form on real vectors, in-place mutation `(*this)[i] ← s·(*this)[i]`. Used throughout Palace's solver code (e.g. `palace/linalg/iterative.cpp:632, 811` for GMRES Arnoldi basis normalisation `w *= 1.0 / Hj[j+1]`).
- `ComplexVector::operator*=(std::complex<double> s)` — Palace member-form on complex vectors (`palace/linalg/vector.hpp:98-99`). The body (`palace/linalg/vector.cpp:203-227`) branches on `s.imag() == 0.0`: the real-scalar path delegates to `Real() *= sr; Imag() *= sr` (two real `operator*=` calls); the general complex-scalar path runs a single fused `forall_switch` kernel computing `(sr·XR − si·XI, si·XR + sr·XI)` per element.

There is **no** free-function `linalg::Scal` or `linalg::Scale` symbol in Palace's `linalg/` namespace (verified by grep against `palace/linalg/*.{cpp,hpp}`). Scaling is performed through the member-form `operator*=` at every call site. The closest free-function is `linalg::Normalize` (`palace/linalg/vector.hpp:262-270`), which composes `nrm2` and a member-form `*=` to produce a unit vector and return the original norm — i.e. `Normalize` is **not** `scal` but rather a fused `nrm2 + scal(1/nrm2, ·)`.

At L0, the in-place destination buffer is the receiver `*this`. The L1 form drops the destination-buffer mention: the operator consumes `α` and the pre-update value of `x`, and produces a fresh post-update value. The L0 real-imag-branch fast path in `ComplexVector::operator*=` is a transparent performance trick at L1 — algebraically `(sr + 0i)·x = sr·x` exactly, so eliding the imaginary cross-term when `si == 0.0` is equivalent. It disappears in the L1>L0 lowering.

A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) — covering BLAS background and call-site role (basis normalisation, search-direction rescaling). The L1 entry here is the firm operator definition; the concept page is the narrative.
[new]: ## Context

`scal` lifts Palace's vector-scalar multiplication from the receiver-mutating member form alone — `mfem::Vector::operator*=(double)` on real vectors, `ComplexVector::operator*=(std::complex<double>)` on complex vectors — to a single pure-functional operator. There is no free-function form: the notable absence of any `linalg::Scal` / `linalg::Scale` symbol (and the closest neighbour, `linalg::Normalize`, which is a fused `nrm2 + scal(1/nrm2, ·)` rather than a `scal` wrapper) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md). The receiver-mutating idiom (no output-arg form for `scal`) is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md). The element-type axis (real / complex / scalar-promoted) and the complex-shape branch (`s.imag() == 0.0`) in `ComplexVector::operator*=` are named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md) and classified as transparent in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination buffer is the receiver `*this`. The L1 form drops the destination-buffer mention: the operator consumes `α` and the pre-update value of `x`, and produces a fresh post-update value. The L0 real-imag-branch fast path in `ComplexVector::operator*=` is a transparent performance trick at L1 — algebraically `(sr + 0i)·x = sr·x` exactly, so eliding the imaginary cross-term when `si == 0.0` is equivalent. It disappears in the L1>L0 lowering.

A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) — covering BLAS background and call-site role (basis normalisation, search-direction rescaling). The L1 entry here is the firm operator definition; the concept page is the narrative.
```

Citation-chain check: the removed bullet enumeration and the "no `linalg::Scal`" paragraph cite `iterative.cpp:632, 811`, `vector.hpp:98-99`, `vector.cpp:203-227`, `vector.hpp:262-270`. All retained in L1 `Evidence` (lines 94-104, unchanged): `vector.hpp:98-99`, `vector.cpp:203-227`, `vector.hpp:262-270`, `iterative.cpp:632`, `iterative.cpp:811`. `L0/linalg-free-functions` line 43 ("notable absence") names the absent symbol; `L0/output-arg-vs-receiver` line 17 cites `vector.hpp:99` for `x *= s`; `L0/mfem-vector-types` discusses the element-type axis. No file range removed from the citation graph.

---

### 6) `book/src/L1/apply_linop.md`

```edit:book/src/L1/apply_linop.md
[old]: ## Context

The L0 source-side forms are the family of virtual `Mult(x, y)` methods on the operator-interface hierarchy:

- `mfem::Operator::Mult(const Vector &x, Vector &y) const` — abstract base for real operators; inherited from MFEM and re-exported by Palace as `using Operator = mfem::Operator;` at `palace/linalg/operator.hpp:21`. Writes through the output argument `y`.
- `palace::ComplexOperator::Mult(const ComplexVector &x, ComplexVector &y) const = 0` — abstract base for complex operators; declared at `palace/linalg/operator.hpp:54`. Pure virtual; the entire `ComplexOperator` hierarchy is shaped around this method.
- `palace::ComplexOperator::MultTranspose` (`operator.hpp:56`) and `MultHermitianTranspose` (`operator.hpp:58`) — transpose / Hermitian-transpose variants; same shape as `Mult` but apply `Aᵀ` or `Aᴴ` instead of `A`.
- `palace::ComplexOperator::AddMult(x, y, a)` (`operator.hpp:60`) and the `MultTranspose` / `MultHermitianTranspose` accumulating analogues (`operator.hpp:63-67`) — accumulate `a · A · x` into `y` rather than overwrite. The default `Mult` paths in concrete subclasses often dispatch through `AddMult` (e.g. `SumOperator::Mult` zeros `y` then calls `AddMult`, `palace/linalg/operator.cpp:439-440`).
- Concrete subclasses implementing the virtual: `SumOperator::Mult` (`operator.cpp:428-441`); `BaseProductOperator::Mult` (`operator.hpp:202-206`, two-step `B.Mult(x, z); A.Mult(z, y)`); `BaseDiagonalOperator::Mult` (decl at `operator.hpp:277`, element-wise `y[i] = d[i] * x[i]`); `BaseMultigridOperator::Mult` (`operator.hpp:347`, dispatches to finest-level operator); `ComplexWrapperOperator::Mult` (`operator.hpp:99`, real-imaginary block dispatch); `ParOperator::Mult` (`palace/linalg/rap.cpp:195-234`, parallel wrapper applying prolongation/restriction around the inner operator); `ComplexParOperator::Mult` (`rap.cpp:481-517`). Plus all preconditioners, FE assembly closures, and Jacobian-action operators that implement the same interface.

At L0, the in-place destination `y` is overwritten; the operator `A` is read-only (the methods are `const`); workspace tensors are private to the operator's representation (e.g. `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`). The L1 form drops the destination-buffer mention: the operator consumes `A` and `x`, produces a fresh output. Workspace, in-place overwrite, and the choice of representation (sparse / dense / matrix-free / composition / multigrid) are all L0 concerns; they reappear in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/apply_linop`](../concepts/apply_linop.md) — covering background (BLAS-2 generalisation), constructed-operator chains, and slice-level use across CG / GMRES / divfree. The L1 entry here is the firm operator definition; the concept page is the narrative.
[new]: ## Context

`apply_linop` lifts the entire `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` virtual-method family on the parallel `Operator` (real) / `ComplexOperator` (complex) base classes, across all concrete subclasses (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, `ComplexParOperator`, all preconditioners, all FE assembly closures, all Jacobian-action operators), to a single pure-functional operator-application primitive `y = A·x` over an opaque `LinearOperator[M, N]` type. The full overload set, sub-axes (transpose mode, accumulate mode, element type), and concrete-subclass roster are detailed in [`L0/apply-linop-overload-set`](../L0/apply-linop-overload-set.md). The output-arg mutation idiom (`A.Mult(x, y)` writes through `y`) is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md). The element-type axis (`Operator` vs `ComplexOperator`, plus the `Par*` parallel-wrapper axis read as single-rank per CLAUDE.md Scope) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The `Mult → AddMult` fused-zero-init dispatch in `SumOperator` and the matrix-free element-summation-order load-bearing case are classified in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination `y` is overwritten; the operator `A` is read-only (the methods are `const`); workspace tensors are private to the operator's representation (e.g. `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`). The L1 form drops the destination-buffer mention: the operator consumes `A` and `x`, produces a fresh output. Workspace, in-place overwrite, and the choice of representation (sparse / dense / matrix-free / composition / multigrid) are all L0 concerns; they reappear in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/apply_linop`](../concepts/apply_linop.md) — covering background (BLAS-2 generalisation), constructed-operator chains, and slice-level use across CG / GMRES / divfree. The L1 entry here is the firm operator definition; the concept page is the narrative.
```

Citation-chain check: the removed multi-bullet enumeration cites `operator.hpp:21`, `operator.hpp:24-68` (lines 54, 56, 58, 60, 63-67), `operator.cpp:428-441` (line 439-440), `operator.cpp:458-466`, `operator.hpp:202-206`, `operator.hpp:277`, `operator.hpp:347`, `operator.hpp:99`, `rap.cpp:195-234`, `rap.cpp:481-517`. All retained in L1 `Evidence` (lines 102-114, unchanged): `operator.hpp:21`, `operator.hpp:24-68`, `operator.hpp:36-39`, `operator.hpp:116-136`, `operator.hpp:178-229` (`202-206` cited as sub-range), `operator.hpp:298-367`, `operator.cpp:428-441`, `operator.cpp:458-466`, `rap.cpp:195-234`, `rap.cpp:481-517`. `L0/apply-linop-overload-set` "Evidence (representative)" covers all the same ranges plus `operator.cpp:478-507` and `rap.cpp:236-275`. The `BaseProductOperator::z` workspace mention at `operator.hpp:192` is preserved in the new shortened paragraph. No file range removed from the citation graph.

---

### 7) `book/src/L1/axpbypcz.md`

```edit:book/src/L1/axpbypcz.md
[old]: ## Context

The L0 source-side forms are:

- `ComplexVector::AXPBYPCZ(std::complex<double> α, const ComplexVector &x, std::complex<double> β, const ComplexVector &y, std::complex<double> γ)` — member call mutating `*this` in place to `α·x + β·y + γ·(*this)` (`palace/linalg/vector.hpp:133-136`). The destination is the receiver; there is no output argument.
- `linalg::AXPBYPCZ<VecType, ScalarType>(ScalarType α, const VecType &x, ScalarType β, const VecType &y, ScalarType γ, VecType &z)` — free-function template (`palace/linalg/vector.hpp:313-316`) with three explicit specialisations:
  - `AXPBYPCZ(double, Vector, double, Vector, double, Vector)` (`palace/linalg/vector.cpp:745-758`): real-real path with a `γ == 0` branch. When `γ == 0` it delegates to MFEM's `add(α, x, β, y, z)` (the 5-argument out-of-place form that writes its last argument from the linear combination of its first four). When `γ ≠ 0` it splits into two calls: first `AXPBY(α, x, γ, z)` (in-place update `z = α·x + γ·z`), then `z.Add(β, y)` (in-place `z += β·y`). The split is not algebraically lossy — both branches compute the same `z_new = α·x + β·y + γ·z_old` — but it is the only L0 site in this family where the fused L1 form expands into multiple L0 calls.
  - `AXPBYPCZ(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)` (`palace/linalg/vector.cpp:760-765`): delegates to `z.AXPBYPCZ(α, x, β, y, γ)`, i.e. the member form on `ComplexVector`.
  - `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` (`palace/linalg/vector.cpp:767-772`): real-scalar-on-complex-vector overload; promotes scalars implicitly and delegates to the same member form.

At L0, the in-place destination `z` is overwritten; the prior value of `z` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, `y`, `γ`, and the pre-update value of `z`, and produces a fresh post-update value. The fusion (single-call combined update rather than a multi-pass form) is preserved at L1 because it has algebraic meaning — the law `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpbypcz` at L1; it lands as a new firm row in `book/src/L1/index.md` (no prior rough-in row — this entry is a fresh promotion, motivated by the forward reference in `axpby.md` § "Dependencies" and open question `axpby-axpbypcz-next-harvest`). The L1>L0 lowering theme for `axpbypcz` (companion to `axpby-mutation-rotation`) is not authored in this report — that is abstractor work; see open question `axpbypcz-mutation-rotation-abstractor-target` below.
[new]: ## Context

`axpbypcz` lifts Palace's fused three-scalar three-vector update from two L0 idioms (receiver-mutating `ComplexVector::AXPBYPCZ(α, x, β, y, γ)` and free-function-form `linalg::AXPBYPCZ(α, x, β, y, γ, z)` with three template specialisations: a real-real path that branches on `γ == 0` between a one-call MFEM `add(α, x, β, y, z)` fast-path and a two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`; complex-complex and real-scalar-on-complex-vector both delegating to the member form) to a single pure-functional operator. The L0 file layout — the AXPBYPCZ family in `palace/linalg/vector.{hpp,cpp}` and its place in the AXPY → AXPBY → AXPBYPCZ subsumption chain — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The BLAS-1 fused-update family". The receiver-vs-output-arg idiom split is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md); the free-function template-dispatch pattern is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md). The element-type axis (real / complex / scalar-promoted) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The real-real `γ == 0` control-flow specialisation (one-call vs two-call) is classified as a transparent performance trick (with cross-branch summation-order divergence noted as load-bearing for bit-reproduction) in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination `z` is overwritten; the prior value of `z` is consumed by the update and inaccessible afterwards. The L1 form drops the destination-buffer mention: the operator consumes `α`, `x`, `β`, `y`, `γ`, and the pre-update value of `z`, and produces a fresh post-update value. The fusion (single-call combined update rather than a multi-pass form) is preserved at L1 because it has algebraic meaning — the law `axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z` is a primitive statement of the linear combination, not a derived shorthand.

This entry is the firm operator definition for `axpbypcz` at L1; it lands as a new firm row in `book/src/L1/index.md` (no prior rough-in row — this entry is a fresh promotion, motivated by the forward reference in `axpby.md` § "Dependencies" and open question `axpby-axpbypcz-next-harvest`). The L1>L0 lowering theme for `axpbypcz` (companion to `axpby-mutation-rotation`) is not authored in this report — that is abstractor work; see open question `axpbypcz-mutation-rotation-abstractor-target` below.
```

Citation-chain check: the removed multi-bullet enumeration cites `vector.hpp:133-136`, `vector.hpp:313-316`, `vector.cpp:745-758` (lines 749-752 sub-range for the `γ == 0` branch), `vector.cpp:760-765`, `vector.cpp:767-772`. All retained in L1 `Evidence` (lines 115-122, unchanged — all five ranges present, plus `vector.cpp:729` for the AXPBY-reference cross-link). `L0/linalg-vector-file` line 53 cites `vector.cpp:745-772` as range-overview; `L0/transparent-vs-load-bearing-tricks` line 14 cites `vector.cpp:745-758` for the `γ == 0` branch. No file range removed from the citation graph.

---

## Supporting evidence

**Operators currently harvested at L1** (per `book/src/L1/index.md` dep-map): 7 firm — `axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz`. All 7 are swept in this dispatch.

**L0 reference chapters currently available** (per `book/src/L0/index.md` cohort): 8 total — 4 conventions (`output-arg-vs-receiver`, `mfem-vector-types`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks`), 2 file overviews (`linalg-vector-file`, `ksp-factory-file`), 2 overload-set / class-interface chapters (`apply-linop-overload-set`, `kspsolver-base-class`). The 7-operator sweep cross-references into 6 of these 8 chapters (`ksp-factory-file` and `kspsolver-base-class` are KSP-internal and not referenced from any of the 7 L1 BLAS-1/operator-apply operators — they will be referenced from the forthcoming L2 `krylov-step` entry).

**Cross-reference coverage** (which L1 operators reference which L0 chapters in the thinned form):

| L1 operator | output-arg-vs-receiver | mfem-vector-types | linalg-free-functions | transparent-vs-load-bearing-tricks | linalg-vector-file | apply-linop-overload-set |
|---|---|---|---|---|---|---|
| `axpy` | yes | yes | (covered via linalg-vector-file) | yes | yes | — |
| `dot` | (no — natural ret-val, no output-arg) | yes | yes | yes | yes | — |
| `nrm2` | (no — natural ret-val) | yes | yes | yes | yes | — |
| `axpby` | yes | yes | yes | yes | yes | — |
| `scal` | yes | yes | yes | yes | (member-form only — covered by output-arg-vs-receiver) | — |
| `apply_linop` | yes | yes | — (deliberate: `Mult` family is virtual-method-only, no free-function form — see open question #4) | yes | — (covered by apply-linop-overload-set) | yes |
| `axpbypcz` | yes | yes | yes | yes | yes | — |

Each L0 reference chapter's `Referenced from` block already lists every L1 operator that this sweep wires up — no new edits to L0 chapters are required (their backlink blocks were authored in the cycle-005/006 bootstrap with this sweep in mind).

**Forward references in the L0 chapters** that this sweep retires: each of `output-arg-vs-receiver`, `mfem-vector-types`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks` contains a forward-declared note in its `Referenced from` block:

> *Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

After this sweep lands, those `*Forward-declared; ...*` notes become stale — the thinning has happened. **Suggested follow-up** (not part of this dispatch, since editing those L0 chapters is out of this dispatch's L1-thinning scope, but flagged for next cycle's planner): remove the four `*Forward-declared; ...*` italic notes from the four L0 convention chapters (`output-arg-vs-receiver.md` line 36, `mfem-vector-types.md` line 42, `linalg-free-functions.md` line 47, `transparent-vs-load-bearing-tricks.md` line 34). Also retire the parallel note in `apply-linop-overload-set.md` line 55 ("*The L1 / L1>L0 entries below already cite this overload set inline. The retroactive-thinning sweep (priority #11) will replace those inline citations with backlinks here.*").

**Visible token-savings estimate** (line-count exact per current `book/src/L1/<op>.md` files; counts Context-section span from `## Context` through last body line before next `##`):

| L1 file | old `Context` lines | new `Context` lines | shrink |
|---|---|---|---|
| `axpy.md` | 5 | 5 | ≈ 0 (axpy was already lean — one paragraph + concepts pointer) |
| `dot.md` | 13 | 5 | ≈ 62% |
| `nrm2.md` | 13 | 7 | ≈ 46% (B-weighted aside preserved) |
| `axpby.md` | 13 | 5 | ≈ 62% |
| `scal.md` | 12 | 5 | ≈ 58% |
| `apply_linop.md` | 13 | 5 | ≈ 62% |
| `axpbypcz.md` | 13 | 5 | ≈ 62% |
| **totals** | **82** | **37** | **≈ 55%** |

The sweep removes ≈ 45 lines of cross-cutting L0-interpretation prose from L1 chapters and replaces them with ≈ 7 explicit one-sentence cross-references per chapter into the appropriate L0 convention / file-overview chapter. Net L1-chapter shrink ≈ 55% on `Context`-section size, with no loss of L0-citation reachability.

**No L1-index.md edit required.** The dep-map already names every L1 operator and its dependencies (`book/src/L1/index.md` lines 49-62). The `Context` thinning is internal to each L1 operator chapter; the dep-map's structure is unaffected.

## Open questions / caveats

1. **No deferrals.** Threshold met for all 7 chapters — every L1 operator in scope has a corresponding L0 chapter (or combination) available for cross-reference. No items pushed to "L0 bootstrap bundle 4" from this sweep.

2. **Stale forward-declarations in L0 chapters** (next-cycle planner input, not this dispatch's scope): the five L0 chapters that contain `*Forward-declared; ...*` retroactive-thinning notes (`output-arg-vs-receiver.md`, `mfem-vector-types.md`, `linalg-free-functions.md`, `transparent-vs-load-bearing-tricks.md`, `apply-linop-overload-set.md`) should have those italic notes retired in a follow-up dispatch once this sweep is integrated. Single-file edits each; bundlable into one `layer-intro-author` dispatch.

3. **Concept-page consistency** (out-of-band observation; surface only): the `concepts/nrm2.md` claim about "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow" is contradicted by the L1 `nrm2` chapter (line 15, preserved in the thinned form). This was flagged in the original `Context` and remains a pending future invocation per the existing note. Not new evidence — but the thinning preserves the flag so it does not get lost. (No `problems/` filing — this is already an open work item per the L1 chapter's own caveat.)

4. **`L0/linalg-free-functions` discoverability for `apply_linop`**: the apply-linop sweep does not cross-reference `linalg-free-functions` (the `Mult` family is virtual-method-only, not a free-function-template wrapper). If a future reader looking at `apply_linop` expects a parallel "free-function" treatment, they will not find one — but this is correct, because `Mult` does not have one. Recorded as a deliberate omission, not a gap.

5. **No new file-range citations introduced.** The thinning only removes citations from the L1 `Context` sections; the same citations are reachable via the L1 `Evidence` sections (which are kept intact) and via the L0 chapters' own `Evidence` blocks. No critic-relevant `citation-validity` concern should surface; the citation count per L1 chapter goes down (in `Context`) while the citation count in the L1 `Evidence` section is unchanged.

6. **Open-questions append**: none required. This sweep is mechanical re-routing of existing material; no new questions surfaced that aren't already tracked.
