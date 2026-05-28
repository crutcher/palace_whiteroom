---
layer: L3
operator: dot
firmness: firm
lowers_to:
  - book/src/L1/dot.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - (none) — `dot` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict)
variant_axes:
  - element-type (real / complex)
  - conjugation-convention (hermitian / unconjugated `tdot` — complex element-type only)
---

# dot

Whole-tensor inner-product reduction at L3: `α = ⟨x, y⟩`. The canonical BLAS-1 reduction primitive rendered as an L3 field operation; the workhorse of Krylov coefficient computation and orthogonalization at the iteration-rotation layer. Identity-in-form lowering to L1 [`dot`](../L1/dot.md); the rotation work is at the surrounding wrapper (the `krylov-step` body), not on the primitive itself.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `dot` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N], y: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3 just as it is at L1.

This entry is a **layer-coherence anchor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L1 form — the rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding context (the iteration view at L3 vs. the mutation-rotation view at L1) differs. The L3 entry exists because each layer is coherent within itself: a reader navigating L3 (whose index at `book/src/L3/index.md:13` advertises `dot` as a field operation in L3 vocabulary) cannot be required to reach down to L1 to find the primitive.

The companion concept page [`concepts/dot`](../concepts/dot.md) carries the BLAS-1 heritage framing and the cross-cutting prose treatment; the L1 entry [`L1/dot`](../L1/dot.md) is authoritative on every factual claim about the Palace surface. This L3 entry adds **iteration-rotation framing** to those — it names `dot` as an L3-native whole-tensor reduction consumed inside the surrounding `krylov-step` body — but does not duplicate algebraic-law content; the laws hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain.

The L1 conjugation convention (first-argument-conjugation for complex Hermitian `dot`, `⟨x, y⟩ = xᴴ y`) carries through unchanged at L3. The L0 free-function asymmetry — `linalg::Dot(comm, x, y) = yᴴ x` per `vector.cpp:674-685`, conjugating the second argument — is documented at `book/src/L1/dot.md:43, 104-105` and is L1>L0 lowering content, not L3 content.

## Signature

```text
dot   :: Tensor[N] -> Tensor[N] -> Scalar
tdot  :: Tensor[N] -> Tensor[N] -> Scalar     -- complex-only variant
```

Two operators in one chapter because they share the entire reduction skeleton (sum over `N`) and differ only by the per-element kernel. The L3 signature is identical to the L1 signature; only the surrounding layer's vocabulary differs.

Shape contract (positional values; bunsen-style named axes; no element loop exposed at L3):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument; the first (conjugated, for Hermitian variant) argument in the Hermitian inner product `xᴴ y`.
- **`y`** — `Tensor[N]` — read-only whole-tensor argument; the second (linear) argument in the Hermitian inner product.
- **result** — `Scalar` — element type follows the L1 rule (real `dot` → real; complex `dot` → complex; complex `tdot` → complex; see [`L1/dot`](../L1/dot.md) §Signature for the full element-type → return-type table).
- `x` and `y` must share the length axis `N` and the element type.

Per-element kernel by element-type (inherited from L1; reproduced for L3 reader coherence):

| element type | `dot(x, y)` returns | per-element kernel |
|---|---|---|
| `real`    | `real`    | `x[i] * y[i]` |
| `complex` | `complex` | `conj(x[i]) * y[i]` *(Hermitian, conjugate-linear in first arg)* |
| `complex` (via `tdot`) | `complex` | `x[i] * y[i]` *(unconjugated bilinear)* |

No element loop is exposed at L3 — the reduction over `i ∈ [0, N)` is a single semantic step in the L3 calculus. This is what makes `dot` L3-native by signature shape (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Whole-tensor reduction: `dot(x, y) = Σ_{i ∈ [0, N)} kernel(x[i], y[i])` with the per-element kernel from the table above. At L3 this is rendered as a single semantic step — the reduction is **one node in the iteration-rotation calculus**, not a loop.

Conjugation convention (complex `dot`): conjugate-linear in the **first** argument, linear in the second. This matches the standard mathematical Hermitian inner product `⟨x, y⟩ = xᴴ y`. Inherited unchanged from [`L1/dot`](../L1/dot.md) §Semantics.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense — floating-point summation is non-associative, so different reduction trees produce different bit-level results. Inherited unchanged from L1 as a non-law (see §Algebraic laws below). The trade-offs reappear in the L1>L0 lowering (`apply-linop-mutation-rotation` sister-theme structure; not applicable here because `dot` is a reduction, not a destination-bearing op).

The MPI collective is **not** in the L3 signature — single-rank is in scope per CLAUDE.md §Scope; MPI ranks are read as their single-rank equivalents. The reduction at L3 is a single step; the local-then-collective two-step reappears only in the L1>L0 lowering at L1. L3 sees a global reduction in one step; the lift from L1 to L3 does not introduce or remove MPI structure.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `dot`'s iteration view is the reduction over the length axis `N`. **The reduction lifts as a whole-tensor operation** — the signature `Tensor[N] -> Tensor[N] -> Scalar` exposes no element loop, and the reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded non-law, not a structural element of the L3 form). There is **no sequential obstruction** for `dot` — the reduction over independent length-axis indices is a parallel operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point implementation choice, not an algebraic obstruction at L3.

`dot` is **consumed inside** larger L3 forms — most notably the `krylov-step` body (per `book/src/L3/krylov-step.md` §Semantics, the iterate-and-scalar update sub-composition; the L3 form at `book/src/L3-L2/krylov-step-body-identity.md:30-37` shows `dot` in the per-step let-chain). At L3 `dot` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body provides, not what `dot` itself contributes.

## Algebraic laws

The L3 algebraic laws are **inherited unchanged from L1** because the L3 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `dot` and `tdot` holds at L3 with the same statement, and every L1 non-law remains a non-law at L3. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

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
9. **Positive semi-definite at `y = x`**: `dot(x, x) ∈ ℝ` and `dot(x, x) ≥ 0`, with equality iff `x = 0` (in exact arithmetic).
10. **Zero in either argument**: `dot(0, y) = dot(x, 0) = 0`.

**For `tdot` over complex element-type (unconjugated bilinear form):**

11. **Symmetry**: `tdot(x, y) = tdot(y, x)`.
12. **Bilinearity in each argument** (analogue of laws 2–3 with no conjugation).
13. **Not positive semi-definite**: `tdot(x, x) ∈ ℂ` in general; in particular `tdot(x, x) = 0` does **not** imply `x = 0` (e.g. `x = (1, i)` gives `tdot(x, x) = 1·1 + i·i = 0`). Recorded as the explicit absence: `tdot` is the indefinite form Palace exposes for algorithms that require it, distinct from `dot`.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Associativity of the reduction-tree** in floating point — different summation orders give different bit-level results. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra". The mathematical law `(a + b) + c = a + (b + c)` holds in ℝ / ℂ but not in IEEE-754.
- **Strictness of Cauchy–Schwarz in floating point**: `|dot(x, y)|² ≤ dot(x, x) · dot(y, y)` holds mathematically but can fail by ULP-level amounts due to summation ordering.
- **Distributivity over vector-multiplication structure**: not applicable — `dot` is not a binary operator on vectors closing back to vectors; it's a reduction to a scalar.

## Dependencies

**Same-layer (L3)**: none. `dot` is a leaf reduction at L3 — alongside [`nrm2`](./nrm2.md) it is one of the two BLAS-1 reduction floor primitives at the iteration-rotation layer. Its sub-operations are scalar multiplication, scalar conjugation (complex case only), and scalar addition — all at or below the L3 layer's resolution.

**Consumers (L3)**: [`krylov-step`](./krylov-step.md) — the per-step body's iterate-and-scalar-update sub-composition `krylov_update` consumes `dot` for scalar-stratum updates (CG's `α = dot(r, z) / dot(Ap, p)`; GMRES's orthogonalization coefficients `dot(v_i, w)`; per `book/src/L3-L2/krylov-step-body-identity.md:30-37`).

**Cross-cutting concepts**:

- [`dot`](../concepts/dot.md) — the cross-cutting concept page with BLAS-1 heritage framing.

**L1 anchor**: [`L1/dot`](../L1/dot.md) (firm cycle-002) — the L1 entry is authoritative on the Palace surface details, the receiver-vs-argument asymmetry on the L0 method form, the self-dot fast path (`&y == this`), and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1:

1. **element-type** (`real` | `complex`) — at L0 these are separate functions / overloads; at L1 / L3 they collapse to one operator parameterised by element type, with the Hermitian-vs-bilinear distinction handled by the per-element kernel.
2. **conjugation convention** (complex element-type only): `hermitian` (the default `dot`) | `unconjugated` (the separate operator `tdot`). At L1 / L3 these are distinct operators (sharing only the reduction skeleton), because the algebraic laws differ — `dot` is positive semi-definite at `y = x`, `tdot` is not.

No new variant axes introduced at L3. No axes merged or split. The L1 conjugation-convention axis is preserved as the `dot` vs `tdot` distinction; the L1 element-type axis is preserved as element-type parameterization of a single operator.

## Status

`firm` — L3 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); algebraic laws inherited unchanged; variant-axis profile inherited unchanged at two axes. The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification). Harvested cycle-011 wave-1 as part of the BLAS-1 reduction cohort backfill (sibling dispatch to `apply_linop`, the axpy cohort, and `scal` at L3).

## Lowers to

L3 `dot` lowers to L1 [`dot`](../L1/dot.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `dot` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `dot` lives at the L1 entry's evidence section (`book/src/L1/dot.md` §Evidence) — Palace's `linalg::Dot` template at `palace/linalg/vector.hpp:247-253` composes `LocalDot` with `Mpi::GlobalSum`; the Hypre per-rank reduction kernel at `vector.cpp:665-672` is the local kernel; the MPI_Allreduce is the collective. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.

## Lifts from

`dot` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"). At L4, `dot` appears inside larger composed entries (e.g., `book/src/L4/krylov-step.md` §Semantics) as a let-binding consuming the L3-native primitive surface; it carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), and the complete L0 evidence list (`vector.hpp:110-113`, `vector.hpp:242-253`, `vector.cpp:263-274`, `vector.cpp:665-685`, etc.).
- [`book/src/L3/index.md`](./index.md) line 13 — the L3 vocabulary inventory explicitly names `dot` as an L3 field operation. This L3 entry closes the inventory-vs-content gap noted by the cycle-010 audit.
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics — the consuming context at L3; the per-step body's iterate-and-scalar update sub-composition consumes `dot` for scalar-stratum updates.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the load-bearing statement that the seven L1 primitives (including `dot`) are L3-native by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." This is the structural justification for the L3>L1 identity-in-form rotation.
- [`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — the L3 body let-chain renders `dot` as an L3-native primitive call identical in shape to its L1 signature.
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; the BLAS-1 heritage framing.
- `palace/linalg/iterative.cpp:395, 404, 444, 460` — CG using `linalg::Dot` for `β = ⟨z, r⟩` and the α-denominator `⟨z, p⟩`; the consuming context for `dot` at L0, inherited transitively. (Path relative to `reference/palace/`.)
- `test/unit/test-orthog.cpp:157, 219-220, 271, 313-315, 373-376` — `linalg::Dot` used as the orthogonalization-coefficient primitive in MGS and CGS; L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement", inherited transitively. (Path relative to `reference/palace/`.)
- Cycle-010 audit at [`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`](../../../reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md) §"Per-candidate verdict" (2) — HIGH CONFIDENCE backfill recommendation for the BLAS-1 cohort at L3, including `dot`. This entry is the enactment.

## L3 vs L1 distinction

- **L1**: pure functional reduction `α = dot(x, y)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (a `dot` returns a scalar; there is no destination buffer to mutate); the MPI collective is folded into the L1>L0 lowering. The receiver-vs-argument asymmetry on the L0 method form is erased (the L1 signature names the conjugated argument first by convention). Reduction-tree non-associativity recorded as a load-bearing algebraic claim.
- **L3**: whole-tensor reduction `α = dot(x, y)` rendered as an L3 field operation. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `dot` itself is consumed as a leaf reduction with no iteration view of its own. The signature is identical to L1; the rotation is at the surrounding wrapper, not on the primitive.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `dot` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**.
