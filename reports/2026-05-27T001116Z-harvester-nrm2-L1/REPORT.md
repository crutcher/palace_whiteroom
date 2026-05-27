---
agent: harvester
invoked_at: 2026-05-27T00:11:16Z
scope: L1 operator: nrm2
status: pending
inputs:
  - book/src/concepts/nrm2.md (existing concept page; signature accurate, stability claim about scaled summation deserves caveat — see "Open questions / caveats")
  - book/src/L1/axpy.md (format reference from pilot-1)
  - book/src/L1/dot.md (format reference from cycle-002; firm L1 dot operator that nrm2 depends on)
  - book/src/L1/index.md (dep-map to update)
  - reports/2026-05-26T231843Z-harvester-dot-L1/REPORT.md (sister report; skill_uptake block format precedent)
  - reference/palace/palace/linalg/vector.hpp (linalg::Norml2 declaration at 255-260, linalg::Normalize at 263-270)
  - reference/palace/palace/linalg/operator.hpp (B-weighted Norml2 declaration at 374)
  - reference/palace/palace/linalg/operator.cpp (B-weighted Norml2 definitions at 600-619)
  - reference/palace/palace/linalg/iterative.cpp (CG/GMRES use of linalg::Norml2 at 408, 568, 578, 582, 631, 756, 762, 810)
  - reference/palace/palace/linalg/arpack.cpp (Arnoldi residual norms at 438, 442, 471, 609, 826)
  - reference/palace/palace/linalg/nleps.cpp (nonlinear-EVP residual norms at 114, 118, 147, 610, 820)
  - reference/palace/palace/linalg/slepc.cpp (SLEPc Arnoldi residual norms at 475, 479, 507, 834, 976, 1329, 1776)
  - reference/palace/palace/fem/errorindicator.hpp (ErrorIndicator::Norml2 wrapper at 43)
  - reference/palace/test/unit/test-vector.cpp (real-vector norm test at 209-211; sqrt(14) check)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading source ranges (vector.hpp:255-260 is the one-line definition; B-weighted variant at operator.cpp:600-619; representative use sites at iterative.cpp/arpack.cpp/nleps.cpp/slepc.cpp); skill invocation deferred to critic-phase per pilot-1 axpy and cycle-002 dot precedent.
  - skill: classify-variant-axis
    triggered: true
    decision: explained_non_applicable
    rationale: Single variant axis (element-type real|complex collapsing to one operator since the result is real either way) plus an explicit "no second axis at L1" closure (B-weighting is a related-but-separate operator, not a variant of nrm2); recorded directly in the Variant axes section.
  - skill: verify-refinement-surface
    triggered: true
    decision: explained_non_applicable
    rationale: Three proposed-changes blocks (new L1/nrm2.md, L1/index.md dep-map row append, SUMMARY.md targeted single-line append) — surface well-formedness verified by inspection; skill invocation deferred to critic-phase.
integrated_at: 2026-05-27T00:23:54Z
integration_commit: 9aa1c59
integration_notes: Applied as repaired (append-after dot row on L1/index.md; SUMMARY.md insertion auto-merged with sister axpby SUMMARY edit; both new chapter entries land after the dot line in dep-map row order).
---

# REPORT: Formalize nrm2 at L1

## Summary

Formalizes `nrm2` — the Euclidean vector norm `α ← ‖x‖₂ = √⟨x, x⟩` — as a firm L1 operator. The rough-in lives as the cross-cutting concept page `book/src/concepts/nrm2.md` and as a forward reference in cycle-002's `book/src/L1/dot.md` ("nrm2 (forthcoming; cycle-003) will depend on `dot` via `nrm2(x) = √dot(x, x)`"); no L1 chapter file exists yet. The Palace L0 surface is unusually clean here: the free function `linalg::Norml2(comm, x)` at `palace/linalg/vector.hpp:255-260` is a literal one-line `std::sqrt(std::abs(Dot(comm, x, x)))` over either real or complex `x` — the operator is fully expressed in terms of cycle-002's firm `dot`. The L1 entry collapses both element-type overloads to one operator with one signature (the result is real regardless of input element type, since the Hermitian self-dot `dot(x, x)` is real per cycle-002 dot.md law 9). The B-weighted variant `linalg::Norml2(comm, x, B, Bx)` at `operator.cpp:600-619` is **not** part of this operator — it is a separate higher-order construct (operator-weighted norm) and is recorded as a forward-reference for a future L1 entry. The concept page's stability claim about "scaled summation (BLAS `nrm2` algorithm)" overstates what Palace actually does — Palace's `linalg::Norml2` performs naive `√Σ |x[i]|²`, not the scaled BLAS algorithm — and this discrepancy is promoted to Open questions.

## Proposed changes

````edit:book/src/L1/nrm2.md
# nrm2

Mutation-free vector Euclidean-norm reduction: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive at L1; the workhorse of residual-norm convergence tests, basis-vector normalisation, and Arnoldi sub-diagonal coefficients.

## Context

The L0 source-side forms are:

- `linalg::Norml2(MPI_Comm comm, const VecType &x)` — free-function template at `palace/linalg/vector.hpp:255-260`. The entire definition is `return std::sqrt(std::abs(Dot(comm, x, x)));`. Specialised by `VecType ∈ {Vector, ComplexVector}` through the underlying `linalg::Dot` template; returns `double` in both cases (the `std::abs(std::complex<double>)` on the complex `dot(x, x)` extracts the modulus, which is the absolute value of the real part since the Hermitian self-dot has zero imaginary part exactly — see cycle-002 dot.md law 9).
- `mfem::Vector::Norml2()` — MFEM method-form on real vectors, no MPI. Direct evidence at `test/unit/test-vector.cpp:209-211` (`double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));`).
- `ErrorIndicator::Norml2(comm)` — a thin caller-side wrapper at `palace/fem/errorindicator.hpp:43` that forwards to `linalg::Norml2(comm, local)`. Not a separate operator — same L1 vocabulary.

At L0, the in-place destination for `nrm2` is the return register / a stack scalar; there is no destination buffer to write through. The L1 form is identical algebraically — the operator is naturally pure. What the mutation rotation does here is essentially nothing on the buffer side; the L1 entry exists to record the algebraic identity `nrm2(x) = √dot(x, x)`, the element-type unification (one operator at L1; two specialisations at L0), and the load-bearing numerical caveat (the reduction-tree non-associativity that propagates from `dot` is the same one).

A cross-cutting prose treatment lives at [`concepts/nrm2`](../concepts/nrm2.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`. Palace inherits any over/underflow risk; if the underlying BLAS / Hypre kernel internally scales, that is an L1>L0 lowering observation, not a Palace-level guarantee. The L1 entry is authoritative; the concept page should be corrected by a future invocation.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` (declared at `operator.hpp:372-374`) is **not** part of this operator. It computes `√(xᴴ B x)` for an SPD operator `B`, requires a workspace `Bx`, and is algebraically a different construct (operator-weighted norm, a.k.a. energy norm). It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply`.

## Signature

```
nrm2 :: (x: Tensor[N]) -> Scalar
nrm2(x) = √⟨x, x⟩
```

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only.
- result — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L1 operator (in contrast to `dot`, where the result element-type tracks the input). It follows from the fact that `dot(x, x)` is a non-negative real scalar for both real (law 4 of L1 dot) and complex (law 9 of L1 dot) inputs.

## Semantics

Definitional: `nrm2(x) = √dot(x, x)`. This is the principal (non-negative) square root of the Hermitian self-inner-product.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-dot `dot(x, x)` for complex `x` is `Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²`, which is real and non-negative element-wise — so the L0 implementation's outer `std::abs(...)` before `std::sqrt` is a defensive guard against floating-point round-off pushing the sum slightly negative, **not** a semantic projection. Algebraically `nrm2(x) = √dot(x, x)` for both element types.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from `dot`. The square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is entirely the `dot`'s.

The MPI collective is **not** in the L1 signature. The `linalg::Norml2(comm, x)` form folds a `MPI_Allreduce` inside the inner `dot`; single-rank is in scope (per `CLAUDE.md` "Scope"), so the L1 reduction is a single semantic step. The L1>L0 lowering reintroduces the local-then-collective two-step (and inherits the bit-deterministic-reduction-order trade-offs already recorded for `dot`).

## Algebraic laws

The laws below hold for both real and complex element-types of `x`; absences are deliberate.

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). Note the `|α|` — the absolute value is necessary on both sign and complex phase; the norm strips both.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `dot`): `|dot(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterises norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-dot identity**: `nrm2(x)² = dot(x, x)` (real and complex) — the defining identity, restated. Used directly by Palace at `palace/linalg/vector.hpp:259` and indirectly anywhere CG-style algorithms reuse `dot(r, r)` instead of recomputing `nrm2(r)²`.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold:

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside `dot` (same load-bearing caveat as the `dot` operator). Algorithms that depend on the strict inequality (e.g. orthogonality-loss detection in MGS reorthogonalisation) must guard.
- **Bit-determinism across reduction trees**: same load-bearing caveat as `dot` — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realisations are exact modulo summation-order noise.
- **Multiplicativity over the cross-element kernel**: `nrm2(x ⊙ y) ≠ nrm2(x) · nrm2(y)` in general (where `⊙` is the hypothetical element-wise product). Not applicable — `nrm2` is a reduction, not a binary algebra on vectors.

## Dependencies

- [`dot`](./dot.md) (firm, cycle-002) — `nrm2(x) = √dot(x, x)`. The dependency is direct and complete: the L0 source defines `Norml2` as a one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`. At L1 this is the **only** L1 operator that `nrm2` depends on; the outer `sqrt` and `abs` are scalar operations below the L1 layer's resolution (deterministic IEEE-754 primitives).

Not a leaf — but only one level removed. The fact that `nrm2` factors so cleanly through `dot` is exactly the kind of compositional structure the L1 layer is meant to expose; the L0 form makes the composition syntactically explicit (one line of source), and the L1 form names it as the defining identity (algebraic law 8).

## Variant axes

`nrm2` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. At L0 these are template specialisations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 these **collapse to a single operator** with the same signature `(x: Tensor[N]) → Scalar(real)`, because:
  - The result is real-valued regardless of input element type (the Hermitian self-dot is real).
  - The defining identity `nrm2(x) = √dot(x, x)` is shared across element types; the element-type dispatch is entirely absorbed by `dot`.
  - All ten algebraic laws hold uniformly across both element types.

  This is a stronger collapse than `dot`'s element-type axis: `dot` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not.

No other variant axes at L1:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (operator-weighted norm, `‖x‖_B = √(xᴴ B x)`) with its own L1 entry forthcoming. The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0 even though it's pure at L1).
- **Stability variants**: BLAS-style scaled-summation `nrm2` (which avoids overflow/underflow at the cost of extra arithmetic) is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x,x⟩` form. If scaling matters for a specific algorithm, that is a caller-side concern (no Palace use site is known to scale before calling `Norml2`); not a variant axis of the L1 operator.

## Status

`firm` — signature is canonical and tightly constrained by the one-line L0 definition, evidence is direct from `palace/linalg/vector.hpp:255-260`, and the algebraic laws listed are standard properties of the Euclidean norm induced by a Hermitian inner product (modulo the explicitly-recorded floating-point caveats inherited from `dot`).

## L1 vs L0 distinction

- **L0**: free-function `linalg::Norml2(MPI_Comm, x)` (does `Dot` + `MPI_Allreduce` + `std::abs` + `std::sqrt`), method-form `Vector::Norml2()` (real, no MPI), or wrapper `ErrorIndicator::Norml2(comm)`. The B-weighted overload `Norml2(comm, x, B, Bx)` is a separately-named operator at L0 sharing the same symbol via overloading. The `std::abs` outer guard is present to defend against round-off-induced sub-zero `dot(x,x)` values.
- **L1**: pure functional reduction `α = nrm2(x)`. No MPI collective in the signature, no method-form / wrapper / overload distinction. The B-weighted overload is **factored out** as a separate L1 operator (forthcoming). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8; the `std::abs` defensive guard is recognised as a floating-point implementation detail and disappears at L1 (the algebraic claim that `dot(x, x)` is non-negative real subsumes it).

## Evidence

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template, which uses `Norml2` then scales `x *= 1.0 / norm` and asserts `norm > 0.0`. Confirms `nrm2` returns a positive real used as a divisor.
- `palace/linalg/operator.hpp:372-374` — declaration of the B-weighted overload `Norml2(comm, x, B, Bx) → double`. Recorded here to mark the boundary; not part of this operator's definition.
- `palace/linalg/operator.cpp:600-619` — definitions of the B-weighted overload for both `Vector` and `ComplexVector`. The complex case asserts `dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real()` then returns `std::sqrt(dot.real())` — confirming that `xᴴ B x` is expected to be real for SPD `B`. Recorded as boundary evidence.
- `palace/fem/errorindicator.hpp:43` — `ErrorIndicator::Norml2(comm) const { return linalg::Norml2(comm, local); }` — a transparent wrapper.
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES iterative solvers using `linalg::Norml2` for: initial right-hand-side norm `β = ‖b‖` (l.408, 578, 582, 762), true residual norm `‖r‖` (l.568, 756), and Arnoldi sub-diagonal coefficients `H[j+1,j] = ‖w‖` (l.631, 810). Direct evidence `nrm2` is the convergence-test and Arnoldi-orthogonalisation primitive.
- `palace/linalg/arpack.cpp:438, 442, 471, 609, 826` — ARPACK Arnoldi residual norm computations: B-weighted form at l.438 (separate operator), plain form at l.442; residual relative norm at l.471; final residual norms at l.609 and l.826.
- `palace/linalg/nleps.cpp:114, 118, 147, 610, 820` — nonlinear-EVP residual norms; B-weighted at l.114; plain at l.118; relative residual at l.147 (`GetResidualNorm(...) / linalg::Norml2(comm, x1)`); scale-extraction for normalisation at l.610; final residual norm at l.820.
- `palace/linalg/slepc.cpp:475, 479, 507, 834, 976, 1329, 1776` — SLEPc Arnoldi residual norms (B-weighted and plain), confirming `nrm2` is the primary residual-norm primitive across all three eigensolver backends (ARPACK, SLEPc, NLEPS).
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. Confirms `nrm2((1,2,3)) = √14` and confirms the return type is `double` (real) for real inputs. L0-equivalent semantic documentation per CLAUDE.md "Tests as semantic supplement".
- Cycle-002 firm `dot` entry at `book/src/L1/dot.md` — provides laws 4 and 9 (Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positivity depend.
````

````append-after:book/src/L1/index.md
[Targeted dep-map row append, NOT a full-file replacement. Cycle-003 dispatch 2 — the sister `axpby` harvester (`reports/2026-05-27T001116Z-harvester-axpby-L1/REPORT.md`) — also edits this file via a row-replacement (rough-in → firm) on the existing `axpby` row; the integrator must apply both edits.

Anchor line (must exist in `book/src/L1/index.md` under the "## Operator dep-map" table; this is the cycle-002 firm `dot` row):

| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |

Insert immediately after the anchor line above:

| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |

No other rows or sections in `book/src/L1/index.md` should change. This mirrors the cycle-002 `dot` harvester's SUMMARY.md append-after convention; the sister `axpby` harvester's row-replacement edit on the `axpby` rough-in row is independent and non-overlapping with this append.]
````

````append-after:book/src/SUMMARY.md
# Anchor line (must exist in SUMMARY.md, under the "L1 — Mutation-Lifted Forms" Part):
- [dot](./L1/dot.md)

# Insert immediately after the anchor line above:
- [nrm2](./L1/nrm2.md)
````

(Integrator hint: this is a targeted insertion, NOT a full-file replacement. `SUMMARY.md` covers many Parts; only the single new line `- [nrm2](./L1/nrm2.md)` should be added, positioned directly after the existing `- [dot](./L1/dot.md)` line under the "L1 — Mutation-Lifted Forms" Part heading. All other content in `SUMMARY.md` must be preserved verbatim. This mirrors cycle-002's `dot` SUMMARY block convention.)

## Operator content

See the `book/src/L1/nrm2.md` content in the proposed-changes block above. Key decisions:

- **Signature**: `nrm2 :: (x: Tensor[N]) -> Scalar` with the strong claim that the result is **always real** regardless of input element type (collapses the element-type axis at L1 in a way that `dot` does not).
- **Defining identity**: `nrm2(x) = √dot(x, x)`. The L0 source is a literal one-line composition; the L1 entry promotes the identity to algebraic law 8.
- **Algebraic laws stated**: 10 holding (non-negativity, positive-definite, positive homogeneity with `|α|`, triangle, reverse triangle, Cauchy–Schwarz, parallelogram identity, self-dot identity, zero argument, phase invariance) and 4 explicitly-not-holding (linearity, strict Cauchy–Schwarz in float, bit-determinism, kernel multiplicativity).
- **One variant axis**: element-type (collapsing to a single operator). B-weighting is a separate forthcoming operator, not a variant. BLAS-style scaled-summation stability is not present in Palace and not a variant axis.
- **One L1 dependency**: `dot` (firm, cycle-002).

## Supporting evidence

- L0 source-side citations: every claim in the operator entry is cited to a `(file:start-end)` range in `reference/palace/`. The defining one-line definition at `vector.hpp:255-260` is the load-bearing citation.
- Test citation: `test/unit/test-vector.cpp:209-211` directly verifies `nrm2((1,2,3)) = √14` and confirms the real-input return type is `double`. L0-equivalent semantic documentation.
- Use-site citations confirm `nrm2` is the primary residual-norm and basis-normalisation primitive across all of Palace's iterative solver corpus: CG / GMRES (`iterative.cpp`, 8 sites), ARPACK eigensolver (`arpack.cpp`, 5 non-comment sites), SLEPc eigensolver (`slepc.cpp`, 7 non-comment sites), NLEPS (`nleps.cpp`, 5 sites), and the error indicator (`errorindicator.hpp`, 1 wrapper site).
- Cross-reference to the existing concept page `book/src/concepts/nrm2.md` — the L1 entry supersedes its (incorrect) stability claim; see Open question 1.
- Cross-reference to cycle-002 firm `dot` entry `book/src/L1/dot.md` — provides the algebraic facts (laws 4 and 9 — Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positive-definiteness depend.
- Sister cycle-002 harvester report `reports/2026-05-26T231843Z-harvester-dot-L1/REPORT.md` — format precedent for the `skill_uptake:` frontmatter block and the SUMMARY.md `append-after:` convention.

## Open questions / caveats

1. **Concept-page correction needed (stability claim)**. `book/src/concepts/nrm2.md:9` claims "production implementations use scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow when `|x[i]|` spans a wide range. A naïve `√Σ x[i]²` is not equivalent." This sets reader expectations that Palace's `Norml2` is scaled — but `palace/linalg/vector.hpp:255-260` shows Palace is precisely the naïve `√⟨x,x⟩` form (one line, no scaling). Either: (a) Palace's `dot` kernel ultimately bottoms out in a Hypre / BLAS routine that scales internally (worth verifying — this would be an L1>L0 lowering observation, not a Palace-source-level guarantee), or (b) Palace is simply naïve and the concept page is wrong. Fixing the concept page is out of harvester's scope (one operator per invocation, and concept-page edits are not in this role's write authority partition). Recommend a follow-up plan item; cycle-planner could route to same-layer-cross-cutter for source-and-concept reconciliation, or to layer-intro-author if concept pages fall under that authority.

2. **B-weighted norm is a separate L1 operator (forthcoming)**. The L0 surface uses overloading: `linalg::Norml2(comm, x)` (this operator) and `linalg::Norml2(comm, x, B, Bx)` (operator-weighted norm `‖x‖_B = √(xᴴ B x)`). At L1 these are distinct: the second requires an `apply`-style operator-application primitive (not yet in the L1 dep-map), an SPD precondition on `B`, and a workspace `Bx` (which is pure at L1 but load-bearing at L0). Recommend cycle-planner queue a `nrm2_B` or `energy_norm` harvester invocation once `apply` (matrix-vector multiplication) is firm at L1.

3. **`std::abs` outer guard at `vector.hpp:259`**. The L0 expression `std::sqrt(std::abs(Dot(comm, x, x)))` wraps `std::abs` around the inner `dot(x, x)`. For real inputs, `dot(x, x)` is `Σ x[i]²` (non-negative in exact arithmetic; can be slightly negative only by round-off when many terms are summed with cancellation, which is not expected for a sum of squares but defensible). For complex inputs, `std::abs(std::complex<double>)` computes the modulus `√(re² + im²)` — but the Hermitian self-dot has `im = 0` exactly (law 9 of L1 dot), so `std::abs` reduces to `|re| = re` (since `re ≥ 0`). At L1 the `std::abs` is recognised as a defensive guard against floating-point sub-zero round-off and is **not** a semantic projection. This is recorded in the operator content but flagged here in case the cross-cutter or critic wants to verify the round-off-only-defensive interpretation against e.g. mixed-precision contexts where the sum might overflow / underflow before reaching `std::abs`.

4. **L1>L0 lowering theme**: when authored, the lowering theme for `nrm2` should: (a) record the `Dot` + `MPI_Allreduce` + `sqrt` chain (inheriting the dot lowering's MPI-collective theme); (b) record the `std::abs` defensive guard against round-off-induced sub-zero `dot(x, x)`; (c) record the method-form `Vector::Norml2()` vs free-function `linalg::Norml2(comm, x)` vs wrapper `ErrorIndicator::Norml2(comm)` surface as transparent caller-side conveniences; (d) record the B-weighted overload's existence as a separate-but-overloaded symbol at L0 with a different L1 referent.

5. **No layer-intro refresh needed yet**. The L1 Part overview is small and just needs a new row in the dep-map (proposed in the edit block above). The dep-map now has 4 entries (3 firm: `axpy`, `dot`, `nrm2`; 1 rough-in: `axpby`); if it grows past ~6 rows or if firm operators start to cluster into families (BLAS-1 vs higher-level Krylov fragments), a layer-intro-author refresh becomes worthwhile.

6. **No HARNESS-FRICTION recurrence**. Per dispatcher instructions, this report was Edit-ed into a pre-created skeleton REPORT.md by the harvester subagent — the `subagent-file-write-blocked-general-purpose` friction is `resolved-with-narrowing` (blocks `Write` on `*REPORT.md`-named files but `Edit` works against pre-created skeletons). The pattern worked cleanly here; no new friction observed.
