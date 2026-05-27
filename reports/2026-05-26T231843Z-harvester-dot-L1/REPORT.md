---
agent: harvester
invoked_at: 2026-05-26T23:18:43Z
scope: L1 operator: dot
status: integrated
integrated_at: 2026-05-26T23:51:01Z
integration_commit: TBD-cycle-002
integration_notes: |
  Applied as-is per repaired META.md (overall_status: ready). All three proposed-changes blocks landed:
  (1) created book/src/L1/dot.md (~80 lines, firm L1 operator entry);
  (2) appended dot dep-map row to book/src/L1/index.md;
  (3) applied SUMMARY.md targeted insertion (single-line append-after axpy under L1 Part, per repairer-rewritten block).
  Two unrepairable findings (concept-page contradictions for ComplexVector::Dot return type, linalg::Dotc non-existence, inverted Dot/TransposeDot conjugation roles) promoted to open-questions ledger as `concepts-dot-return-type-correction` and `concepts-dot-dotc-and-inverted-conjugation`; routed to same-layer-cross-cutter.
  Build: cargo make book clean (88s; pre-existing katex warnings unchanged).
inputs:
  - book/src/concepts/dot.md (existing concept page; partially inaccurate — see "Open questions / caveats")
  - book/src/L1/axpy.md (format reference from pilot-1)
  - book/src/L1/index.md (dep-map to update)
  - reference/palace/palace/linalg/vector.hpp (Dot, TransposeDot, LocalDot, linalg::Dot declarations)
  - reference/palace/palace/linalg/vector.cpp (Dot, TransposeDot, LocalDot definitions)
  - reference/palace/test/unit/test-vector.cpp (real-vector dot via operator*)
  - reference/palace/test/unit/test-orthog.cpp (linalg::Dot used in MGS/CGS orthogonalization)
  - reference/palace/palace/linalg/iterative.cpp (CG using linalg::Dot for β and α-denom)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading source ranges; skill invocation deferred to critic-phase per pilot-1 axpy precedent.
  - skill: classify-variant-axis
    triggered: true
    decision: explained_non_applicable
    rationale: Two variant axes (element-type, conjugation-convention) plus an explicit "no third axis" closure landed in the Variant axes section directly; skill telemetry recorded post-hoc by repairer.
  - skill: verify-refinement-surface
    triggered: true
    decision: explained_non_applicable
    rationale: Three proposed-changes blocks (new L1/dot.md, L1/index.md dep-map row, SUMMARY.md TOC entry) — surface well-formedness verified by inspection; skill invocation deferred.
---

# REPORT: Formalize dot at L1

## Summary

Formalizes `dot` — the inner-product reduction `α ← ⟨x, y⟩` — as a firm L1 operator. The rough-in lives only as the cross-cutting concept page `book/src/concepts/dot.md` and as informal mention in the L1 index; no L1 chapter file exists yet. The Palace L0 surface has three distinct entry points (`Vector::operator*` / `mfem::Vector` inner-product → `double`; `ComplexVector::Dot` → `std::complex<double>` (the Hermitian form `yᴴx`); `ComplexVector::TransposeDot` → `std::complex<double>` (the unconjugated form `xᵀy`)), plus the parallel wrappers `linalg::LocalDot` and `linalg::Dot`. The L1 entry collapses these to two operators: a real `dot` and a complex `dot` (conjugate-linear in the first argument), with `tdot` as a separate variant for the bilinear-symmetric form. Distributed reduction (MPI Allreduce) is folded back into a single L1 reduction step; the explicit MPI collective is an L1>L0 lowering concern. The concept page's claim that "`Vector::Dot` and `ComplexVector::Dot` both return a real scalar" is **factually wrong** — `ComplexVector::Dot` returns `std::complex<double>` — and this report supersedes that claim, with the integrator-time correction to the concept page noted as an Open Question (out of scope for harvester per "one operator per invocation").

## Proposed changes

````edit:book/src/L1/dot.md
# dot

Mutation-free vector inner-product reduction: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive at L1; the workhorse of Krylov coefficient computation and orthogonalisation.

## Context

The L0 source-side forms are:

- `mfem::Vector::operator*(const Vector &)` — real inner product, returns `double`. Used at `palace/linalg/vector.cpp:265` inside `ComplexVector::Dot` building blocks. Visible on real vectors as the test-vector.cpp idiom `double dot = vec1 * vec2;` (`test/unit/test-vector.cpp:206-207`).
- `ComplexVector::Dot(const ComplexVector &y) const` — returns `std::complex<double>` per the header comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` at `palace/linalg/vector.hpp:110-113`. The implementation (`palace/linalg/vector.cpp:263-267`) computes `(this)·conj(y)` blocks, which algebraically equals `yᴴ · x` — i.e., conjugate-linear in `y` (the *argument*) and linear in `*this` (the *receiver*).
- `ComplexVector::TransposeDot(const ComplexVector &y) const` — returns `std::complex<double>` for the unconjugated bilinear form `xᵀ y` (`palace/linalg/vector.cpp:269-274`).
- `linalg::LocalDot(...)` — local-rank inner product, real (`palace/linalg/vector.cpp:665-672`, dispatched to Hypre's `hypre_SeqVectorInnerProd`) or complex (`palace/linalg/vector.cpp:674-685`).
- `linalg::Dot(MPI_Comm, x, y)` — global inner product = `LocalDot` followed by `MPI_Allreduce` (`palace/linalg/vector.hpp:247-253`).

At L0, the in-place destination for `dot` is the return register / a stack scalar. There is no destination buffer to write through. The distinction the mutation rotation is doing here is therefore not about buffer ownership but about **reduction order and collective topology**: the L0 form bakes in a specific tree (the Hypre reduction kernel + MPI_Allreduce); the L1 form treats the reduction as a single semantic step.

A cross-cutting prose treatment lives at [`concepts/dot`](../concepts/dot.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page predates this entry and contains an inaccuracy (it claims `ComplexVector::Dot` returns a real scalar — it returns `std::complex<double>`); the L1 entry is authoritative.

## Signature

```
dot   :: (x: Tensor[N], y: Tensor[N]) -> Scalar
tdot  :: (x: Tensor[N], y: Tensor[N]) -> Scalar     -- complex-only variant
```

Two operators in one chapter because they share the entire reduction skeleton (sum over `N`) and differ only by the per-element kernel.

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only.
- `y` — `Tensor[N]` — read-only.
- result — `Scalar` — element type follows the rule below.
- `x` and `y` must share the length axis `N` and element type.

Element-type rule:

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

The "real-projected" reading from `concepts/dot.md` (`Re⟨x,y⟩`) is **not** what Palace's `ComplexVector::Dot` returns. The real-projection only enters at the call site when callers take `std::abs(linalg::Dot(...))` (e.g. `palace/linalg/nleps.cpp:487` for a norm) or `std::real(...)` (in algorithms that know the form must be real, like CG's `β = ⟨r, z⟩` for SPD `B`). Those projections are caller-side L1 forms (`abs` and `re`), not part of `dot` itself.

## Semantics

Reduction: `dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])` with the per-element kernel from the table above.

Conjugation convention (complex `dot`): conjugate-linear in the **first** argument, linear in the second. This matches the standard mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y`. *Note* on the C++ surface: `ComplexVector::Dot` is a method on `*this`, so the receiver is the linear argument and the call argument is the conjugated one (`(*this).Dot(y) = yᴴ · (*this)`). At L1 this asymmetry between method-form (`receiver.Dot(arg)`) and free-function-form (`linalg::Dot(comm, x, y)`) is erased — the L1 signature names the conjugated argument first.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense: floating-point summation is non-associative, so different reduction trees produce different bit-level results. Palace's L0 implementation pins a specific tree (Hypre per-rank kernel + MPI tree-reduce); a different tree gives a different scalar at the bit level even though all are valid implementations of the L1 operator. This is recorded here, not erased.

The MPI collective is **not** in the L1 signature. Single-rank is in scope (`CLAUDE.md` "Scope"); MPI ranks are read as their single-rank equivalents. The reduction at L1 is a single step; the L1>L0 lowering theme is where the local-then-collective two-step reappears (and where bit-deterministic-reduction-order trade-offs are recorded).

The self-dot optimisation `&x == &y` (e.g. `palace/linalg/vector.cpp:266` returning imaginary part `0.0` directly for the Hermitian form; `palace/linalg/vector.cpp:272-273` returning `2 * Imag·Real` for `TransposeDot`) is a transparent performance trick at L1 — algebraically `xᴴ x` always has zero imaginary part exactly, so eliding the cancellation is equivalent. It disappears in the L1>L0 lowering.

## Algebraic laws

The laws below hold; absences are deliberate.

**For `dot` over real element-type (bilinear symmetric form):**

1. **Symmetry**: `dot(x, y) = dot(y, x)`.
2. **Bilinearity (left)**: `dot(α·x₁ + x₂, y) = α·dot(x₁, y) + dot(x₂, y)`.
3. **Bilinearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`. (Follows from 1 + 2.)
4. **Positive semi-definite at `y = x`**: `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic).
5. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `dot` over complex element-type (Hermitian sesquilinear form, conjugate-linear in first arg):**

6. **Hermitian symmetry**: `dot(x, y) = conj(dot(y, x))`.
7. **Conjugate-linearity (left)**: `dot(α·x₁ + x₂, y) = conj(α)·dot(x₁, y) + dot(x₂, y)`.
8. **Linearity (right)**: `dot(x, α·y₁ + y₂) = α·dot(x, y₁) + dot(x, y₂)`.
9. **Positive semi-definite at `y = x`**: `dot(x, x) ∈ ℝ` and `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic). Confirmed by the implementation returning imaginary part `0.0` exactly when `&x == &y` (`palace/linalg/vector.cpp:266`, `palace/linalg/vector.cpp:678`).
10. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `tdot` over complex element-type (unconjugated bilinear form):**

11. **Symmetry**: `tdot(x, y) = tdot(y, x)`.
12. **Bilinearity in each argument** (analogue of laws 2–3 with no conjugation).
13. **Not positive semi-definite**: `tdot(x, x) ∈ ℂ` in general; in particular `tdot(x, x) = 0` does **not** imply `x = 0` (e.g. `x = (1, i)` gives `tdot(x, x) = 1·1 + i·i = 0`). Recorded as the explicit absence: `tdot` is the indefinite form Palace exposes for algorithms that require it, distinct from `dot`.

Laws that explicitly **do not** hold across both `dot` and `tdot`:

- **Associativity of the reduction-tree** in floating point: different summation orders give different bit-level results. Load-bearing (see Semantics). The mathematical law `(a + b) + c = a + (b + c)` holds in ℝ / ℂ but not in IEEE-754.
- **Sub-additivity / Cauchy–Schwarz strictness in floating point**: `|dot(x, y)|² ≤ dot(x, x) · dot(y, y)` holds mathematically but can fail by ULP-level amounts due to summation ordering; algorithms that depend on it tightly (e.g. some MGS reorthogonalisation heuristics) must guard.
- **Distributivity over vector-multiplication structure**: not applicable — `dot` is not a binary operator on vectors closing back to vectors; it's a reduction to a scalar.

## Dependencies

None at L1. `dot` is a leaf primitive — alongside `axpy`, it is one of the two BLAS-1 floor primitives. Its sub-operations are scalar multiplication, scalar conjugation (complex case only), and scalar addition, all at or below the L1 layer's resolution.

`nrm2` (forthcoming; cycle-003) will depend on `dot` via `nrm2(x) = √dot(x, x)` for real, and `nrm2(x) = √re(dot(x, x))` (equivalent to `√dot(x, x)` since law 9 guarantees the result is real) for complex.

## Variant axes

`dot` has two orthogonal variant axes at L1:

- **element-type**: `real` | `complex`. At L0 these are separate functions / overloads (real via `mfem::Vector::operator*` and `linalg::LocalDot(Vector, Vector)` at `vector.cpp:665-672`; complex via `ComplexVector::Dot` at `vector.cpp:263-267` and `linalg::LocalDot(ComplexVector, ComplexVector)` at `vector.cpp:674-685`). At L1 these collapse to one operator parameterised by element type, with the Hermitian-vs-bilinear distinction handled by the per-element kernel.
- **conjugation convention** (complex element-type only): `hermitian` (the default `dot`) | `unconjugated` (the separate operator `tdot`). At L0: `ComplexVector::Dot` vs `ComplexVector::TransposeDot`. At L1 these are distinct operators (sharing only the reduction skeleton), because the algebraic laws differ — `dot` is positive semi-definite at `y = x`, `tdot` is not.

No other variant axes — the reduction is unconditionally exhaustive over the length axis `N`, with no masking or strided variants in the Palace surface.

## Status

`firm` — signatures are canonical, evidence is direct from the Palace source, and the algebraic laws listed are standard sesquilinear/bilinear facts modulo the explicitly-recorded floating-point caveats.

## L1 vs L0 distinction

- **L0**: free-function `linalg::Dot(MPI_Comm, x, y)` (does a local kernel + MPI_Allreduce), method-form `(*this).Dot(arg)` (no MPI), or `mfem::Vector::operator*` (real, no MPI). The receiver-vs-argument asymmetry on the method form determines which side is conjugated. Reduction tree is pinned (Hypre + MPI). Self-dot is a branched fast path.
- **L1**: pure functional reduction `α = dot(x, y)`. No MPI collective in the signature (folded into the L1>L0 lowering). No receiver-vs-argument asymmetry (first argument is by convention the conjugated one). Reduction-tree non-associativity recorded as a load-bearing algebraic claim, not a separate operator.

## Evidence

- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot` declaration with comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.` and `TransposeDot` alongside; `operator*` aliased to `Dot`.
- `palace/linalg/vector.hpp:242-244` — `linalg::LocalDot` declarations for both real and complex inputs.
- `palace/linalg/vector.hpp:247-253` — `linalg::Dot` template, `LocalDot` + `Mpi::GlobalSum`.
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body: real part `(Real()·y.Real()) + (Imag()·y.Imag())`, imag part `(Imag()·y.Real()) - (Real()·y.Imag())` (with `&y == this` fast path returning imag = 0 directly).
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: real part `(Real()·y.Real()) - (Imag()·y.Imag())`, imag part `(Imag()·y.Real()) + (Real()·y.Imag())` (with `&y == this` fast path returning `2·(Imag()·y.Real())`).
- `palace/linalg/vector.cpp:665-672` — `linalg::LocalDot(Vector, Vector)` via Hypre's `hypre_SeqVectorInnerProd`.
- `palace/linalg/vector.cpp:674-685` — `linalg::LocalDot(ComplexVector, ComplexVector)`: combines four real `LocalDot` calls, with self-dot fast path returning imag = 0.
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`.
- `palace/linalg/nleps.cpp:487, 492, 522, 529, 543, 568, 575, 675` — nonlinear-EVP code using `std::abs(linalg::Dot(...))` and `std::sqrt(std::abs(...))`, confirming the complex case returns complex.
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 * vec2; CHECK_THAT(dot, WithinRel(32.0));`. Direct evidence the real form returns `double`.
- `test/unit/test-orthog.cpp:157, 219-220, 271, 313-315, 373-376` — `linalg::Dot` used as the orthogonalisation-coefficient primitive in MGS and CGS.
````

````edit:book/src/L1/index.md
# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:
- `x.Add(α, y)` → `x_{k+1} = x_k + α·y`
- `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention)
- Iterative loop mutating iterate in place → functional unfold `state_{k+1} = step(state_k)`
- Reused workspace `tmp` → omitted (the COW backend handles allocation)

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style).

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |

## Working Notes

- L1 is what `abstractor` produces in early bottom-up sweeps (L0 → L1).
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content.
````

````append-after:book/src/SUMMARY.md
# Anchor line (must exist in SUMMARY.md, under the "L1 — Mutation-Lifted Forms" Part):
- [axpy](./L1/axpy.md)

# Insert immediately after the anchor line above:
- [dot](./L1/dot.md)
````

(Integrator hint: this is a targeted insertion, NOT a full-file replacement. `SUMMARY.md` is ~115 lines covering many Parts; only the single new line `- [dot](./L1/dot.md)` should be added, positioned directly after the existing `- [axpy](./L1/axpy.md)` line under the "L1 — Mutation-Lifted Forms" Part heading. All other content in `SUMMARY.md` must be preserved verbatim.)

## Operator content

See the `book/src/L1/dot.md` content in the proposed-changes block above.

## Supporting evidence

- L0 source-side citations: every claim in the operator entry is cited to a `(file:start-end)` range in `reference/palace/`.
- Test citations: `test/unit/test-vector.cpp:206-207` (real dot returns `double`); `test/unit/test-orthog.cpp` (multiple sites, `linalg::Dot` used for orthogonalization coefficients).
- Use-site citations confirm `linalg::Dot` is a leaf primitive consumed by CG (`iterative.cpp:395, 404, 444, 460`), nonlinear EVP (`nleps.cpp:487, 492, 522, 529, 543, 568, 575, 675`), electrostatic / magnetostatic driver capacitance / inductance assembly (`electrostaticsolver.cpp:119, 126`; `magnetostaticsolver.cpp:131, 138`), post-operator (`postoperator.cpp:1759, 1760, 1795, 1796`), and ROM operator tests (`test/unit/test-romoperator.cpp:497, 502`).
- Cross-reference to the existing concept page `book/src/concepts/dot.md` — the L1 entry now supersedes its return-type claim. The concept page should be updated by a future invocation (out of scope here; one operator per invocation).
- No prior REPORT references for `dot` exist — this is the first formal pass.

## Open questions / caveats

1. **Concept-page correction needed**. `book/src/concepts/dot.md` claims `ComplexVector::Dot` returns a real scalar (`α ← ⟨x, y⟩` real-projected). This is factually wrong: the C++ implementation (`palace/linalg/vector.cpp:263-267`) returns `std::complex<double>`. The real-projection happens at *call sites* via `std::real(...)` or `std::abs(...)`, not inside `Dot`. Fixing the concept page is out of harvester's scope (one operator per invocation, and concept-page edits are not in this role's write authority partition). Recommend a follow-up plan item; cycle-planner could route it to a same-layer-cross-cutter or a layer-intro-author who maintains concept pages.

2. **`Dotc` does not exist in Palace**. The concept page mentions `linalg::Dotc` but a full-tree grep finds zero occurrences of `Dotc` in `reference/palace/`. The unconjugated complex form is `ComplexVector::TransposeDot` (method-form only — no free-function `linalg::TransposeDot` either). The free-function `linalg::Dot` is conjugated for complex inputs. The L1 entry uses `tdot` as the L1 slug for the unconjugated variant; if a future invocation prefers a different L1 name (e.g. `dot_t` or `bilinear_dot`), this can be renamed without semantic change.

3. **L1>L0 lowering note**: when the lowering theme for `dot` gets authored, it must record both (a) the local-kernel + MPI_Allreduce two-step (single-rank-equivalent though it is per scope) and (b) the receiver-vs-argument conjugation asymmetry on the method form `(*this).Dot(arg) = argᴴ · (*this)` vs the free-function form `linalg::Dot(comm, x, y) = xᴴ y` (which conjugates the first argument). This sign-of-which-arg-is-conjugated trap is exactly the kind of friction an abstractor pass should catch — flag in the L1>L0 lowering, not here.

4. **Reduction-tree determinism**: classified the reduction order as a load-bearing numerical claim (CLAUDE.md "Optimization tricks vs. base algebra"). Whether Palace claims bit-determinism for any of its dot uses (e.g. CG convergence test, eigenvalue residual norm) is not surveyed in this report; flag for combinator-miner or cross-cutter if it becomes relevant.

5. **No layer-intro refresh needed yet**. The L1 Part overview is small and just needed a new row in the dep-map. If the dep-map grows past ~6 rows or if firm operators start to cluster into families, a layer-intro-author refresh becomes worthwhile.

6. **HARNESS-FRICTION drive-by observation**: this harvester invocation attempted to use the Write tool per the dispatcher's note that `subagent-file-write-blocked-general-purpose` is empirically resolved for opus subagents. The Write was nonetheless blocked with `Subagents should return findings as text, not write report files. Include this content in your final response instead.` Recommend the dispatcher / meta-phase re-verify the friction-ledger status and either (a) re-open that entry, or (b) update the harvester role definition to make returning REPORT.md inline the canonical contract. Either way the parent main session can paste this content into the intended file path.

---

## Parent-session annotation (persisted via embed-and-persist skill)

This REPORT.md was persisted by the parent session because the harvester subagent's `Write` call to a `*REPORT.md` target was intercepted by a content-pattern filter ("Do NOT Write report/summary/findings/analysis .md files. Return findings directly as your final assistant message."). Body content above is the harvester's substantive output verbatim. Updated finding: custom `.claude/agents/<name>.md` definitions DO resolve via `Agent(subagent_type=<name>)`, but the harness enforces a content-pattern filter that blocks subagent Writes targeting filenames matching `report|summary|findings|analysis`. The embed-and-persist skill remains operationally required. Meta-phase should rename/update friction-ledger entry `subagent-file-write-blocked-general-purpose` to reflect that the block is content-pattern-based, not agent-type-based.
