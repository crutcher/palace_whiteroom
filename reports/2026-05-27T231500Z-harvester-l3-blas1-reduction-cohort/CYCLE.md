---
agent: harvester
invoked_at: 2026-05-27T23:15:00Z
scope: L3 operators: dot + nrm2 (BLAS-1 reduction cohort backfill)
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: 8bb16b7
integration_notes: cycle-011 wave-1 pass 3; second cohort-bundle harvester landing; 2 firm L3 entries (dot + nrm2 with nrm2(x) = √dot(x,x) same-layer L3 dependency); 4 proposed-changes applied cleanly; 0 safety-net gate hits; 1 new OQ promoted (concepts-nrm2-stability-claim-correction); proposed sibling OQ l3-l1-identity-in-form-annotation-policy-formalization merged into existing cycle-010 OQ l3-l1-directory-naming-structure-policy per integrator policy-merge discretion; cumulative in-line identity-rotation count reaches 6 (revisit threshold)
inputs:
  - book/src/L1/dot.md (firm L1; cycle-002)
  - book/src/L1/nrm2.md (firm L1; cycle-003)
  - book/src/L3/krylov-step.md (firm L3; cycle-010; precedent template)
  - book/src/L3/index.md (L3 vocabulary inventory; advertises dot, nrm2 as field operations)
  - book/src/L3-L2/krylov-step-body-identity.md (firm; identity-in-form rationale §"Applicability conditions" point 3)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (firm; renders dot/nrm2 in L3 let-chain)
  - book/src/L2/krylov-step.md (firm L2; cycle-005)
  - book/src/concepts/dot.md (concept page)
  - book/src/concepts/nrm2.md (concept page)
  - reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md (cycle-010 audit; HIGH CONFIDENCE backfill for this cohort)
  - CLAUDE.md §Methodology invariants — "Identity-lowerings still require both L levels" (cycle-009 codification)
sister_dispatches:
  - cycle-011 wave-1 #1: harvester on book/src/L3/apply_linop.md
  - cycle-011 wave-1 #2: harvester on book/src/L3/{axpy,axpby,axpbypcz}.md
  - cycle-011 wave-1 #4: harvester on book/src/L3/scal.md
---

# CYCLE: Formalize dot + nrm2 at L3 (BLAS-1 reduction cohort)

## Summary

Author two firm L3 entries — `dot` and `nrm2` — both backfilled per CLAUDE.md §Methodology invariants **"Identity-lowerings still require both L levels"** (codified cycle-009 meta-phase; first enacted cycle-010 wave-1 for `krylov-step`). Both operators are leaf primitives whose L3 form is **value-thread-isomorphic** to their L1 form — each operates as a whole-tensor reduction with no element loop exposed at any layer of the chain. The L3 entry exists for **layer-coherence reasons** (a reader navigating L3 must find these primitives defined in L3 vocabulary; the L3 index already advertises them as field operations at line 13). The L3>L1 rotation is identity-in-form on the primitive's signature; the rotation work is at the surrounding `krylov-step` wrapper, captured by `book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" point 3. No L3-L1 lowering theme is created — the identity-in-form annotation lives in-line at each L3 entry (precedent: cycle-010 `L3/krylov-step.md`; no L3-L1/ directory exists). Together with sibling dispatches #1 (apply_linop), #2 (axpy cohort), #4 (scal), this closes the L3 vocabulary gap identified by the cycle-010 audit's HIGH CONFIDENCE recommendation.

## Proposed changes

```edit:book/src/L3/dot.md
[create new file — full content in "Operator content (dot)" below]
```

```edit:book/src/L3/nrm2.md
[create new file — full content in "Operator content (nrm2)" below]
```

```edit:book/src/L3/index.md
[append 2 rows to the operator dep-map table; add a Working Notes bullet recording the cohort backfill]
```

```edit:book/src/SUMMARY.md
[insert 2 chapter entries under the L3 Part, after `- [krylov-step](./L3/krylov-step.md)`]
```

---

## Operator content (dot)

The complete content of `book/src/L3/dot.md`:

````markdown
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
````

---

## Operator content (nrm2)

The complete content of `book/src/L3/nrm2.md`:

````markdown
---
layer: L3
operator: nrm2
firmness: firm
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - (none) — `nrm2` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict)
variant_axes:
  - element-type (real / complex; collapsed to single operator at L3 — result is always real)
---

# nrm2

Whole-tensor Euclidean-norm reduction at L3: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive rendered as an L3 field operation; the workhorse of residual-norm convergence tests, basis-vector normalization, and Arnoldi sub-diagonal coefficients at the iteration-rotation layer. Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the rotation work is at the surrounding wrapper (the `krylov-step` body or the outer convergence-test consumer), not on the primitive itself.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `nrm2` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3 just as it is at L1.

This entry is a **layer-coherence anchor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L1 form — the rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding context (the iteration view at L3 vs. the mutation-rotation view at L1) differs. The L3 entry exists because each layer is coherent within itself: a reader navigating L3 (whose index at `book/src/L3/index.md:13` advertises `nrm2` as a field operation in L3 vocabulary) cannot be required to reach down to L1 to find the primitive.

The companion concept page [`concepts/nrm2`](../concepts/nrm2.md) carries the BLAS-1 heritage framing; the L1 entry [`L1/nrm2`](../L1/nrm2.md) is authoritative on every factual claim about the Palace surface (in particular: Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`, not the BLAS scaled-summation algorithm — the concept page's claim to the contrary is noted as a correction-pending item at `book/src/L1/nrm2.md:11`). This L3 entry adds **iteration-rotation framing** to those — it names `nrm2` as an L3-native whole-tensor reduction consumed inside the surrounding `krylov-step` body's convergence-test readout and Arnoldi sub-diagonal computation — but does not duplicate algebraic-law content; the laws hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator (per the L1 entry's boundary documentation at `book/src/L1/nrm2.md:13`); it is a separate L1 operator candidate (the operator-weighted energy norm, depending on both `dot` and `apply_linop`; tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1). At L3 the same boundary holds — `nrm2` is the unweighted Euclidean reduction; the energy-norm primitive is a separate forthcoming L3 candidate.

## Signature

```text
nrm2 :: Tensor[N] -> Scalar
nrm2(x) = √⟨x, x⟩
```

The L3 signature is identical to the L1 signature; only the surrounding layer's vocabulary differs.

Shape contract (positional value; bunsen-style named axis; no element loop exposed at L3):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument.
- **result** — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L3 operator (in contrast to `dot`, where the result element-type tracks the input). It follows from the L1 fact that `dot(x, x)` is a non-negative real scalar for both real (L1 dot law 4) and complex (L1 dot law 9) inputs.

No element loop is exposed at L3 — the reduction over `i ∈ [0, N)` is a single semantic step in the L3 calculus. This is what makes `nrm2` L3-native by signature shape (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Whole-tensor reduction with defining identity: `nrm2(x) = √dot(x, x)`. This is the principal (non-negative) square root of the Hermitian self-inner-product. At L3 the reduction is rendered as a single semantic step — one node in the iteration-rotation calculus.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-dot `dot(x, x)` for complex `x` is `Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²`, which is real and non-negative element-wise. Inherited unchanged from [`L1/nrm2`](../L1/nrm2.md) §Semantics.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from `dot`. The square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is entirely the underlying `dot`'s. Recorded as a non-law (see §Algebraic laws below).

The MPI collective is **not** in the L3 signature — single-rank is in scope per CLAUDE.md §Scope. The reduction at L3 is a single step; the local-then-collective two-step reappears only in the L1>L0 lowering at L1.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `nrm2`'s iteration view is the reduction over the length axis `N`. **The reduction lifts as a whole-tensor operation** — the signature `Tensor[N] -> Scalar` exposes no element loop, and the reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded non-law, not a structural element of the L3 form). There is **no sequential obstruction** for `nrm2` — the reduction over independent length-axis indices is a parallel operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point implementation choice, not an algebraic obstruction at L3.

`nrm2` is **consumed inside** larger L3 forms in two distinct roles:

1. **Convergence-test readout in `outputs`** — per `book/src/L3/krylov-step.md` §Semantics, the per-step body's `derived_views K' op` projection typically produces `outputs.residual_norm = sqrt(abs K'.β)` (CG's residual norm, computed via `dot` and inferred via the recurrence) or `outputs.residual_norm = nrm2(K'.r)` (recompute-from-residual variants). The surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` against the convergence predicate; `nrm2` is a leaf reduction consumed by this projection.
2. **Arnoldi sub-diagonal coefficient** — `H[j+1, j] = nrm2(w)` after orthogonalization (per `palace/linalg/iterative.cpp:631, 810`, the Arnoldi loop's basis-vector normalization). Consumed inside the `op.orthog` closure at the L3 form; surfaces as a scalar field of `K'` in the iterate-and-scalar update.

At L3 `nrm2` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body or outer convergence-test consumer provides, not what `nrm2` itself contributes.

## Algebraic laws

The L3 algebraic laws are **inherited unchanged from L1** because the L3 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `nrm2` holds at L3 with the same statement, and every L1 non-law remains a non-law at L3. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

The laws below hold for both real and complex element-types of `x`:

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). The absolute value is necessary on both sign and complex phase.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `dot`): `|dot(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterizes norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-dot identity**: `nrm2(x)² = dot(x, x)` (real and complex) — the defining identity, restated. The structural link to `dot` is preserved unchanged at L3.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside `dot` (same load-bearing caveat as the `dot` operator).
- **Bit-determinism across reduction trees**: same load-bearing caveat as `dot` — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realizations are exact modulo summation-order noise.
- **Multiplicativity over the cross-element kernel**: not applicable — `nrm2` is a reduction, not a binary algebra on vectors.

## Dependencies

**Same-layer (L3)**: [`dot`](./dot.md) — `nrm2(x) = √dot(x, x)`. The dependency is direct and complete: the L0 source defines `Norml2` as a one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`, and the L3 form preserves this composition by Law 8. The outer `sqrt` and `abs` are scalar operations below the L3 layer's resolution (deterministic IEEE-754 primitives operating on a single scalar produced by `dot`). The dependency on `dot` is the **only** L3 dependency; `nrm2` is otherwise a leaf at L3.

The fact that `nrm2` factors so cleanly through `dot` is exactly the kind of compositional structure the L3 layer is meant to expose at the field-operation level; the L0 form makes the composition syntactically explicit (one line of source at `palace/linalg/vector.hpp:255-260`), and the L3 form preserves the algebraic identity by inheritance.

**Consumers (L3)**: [`krylov-step`](./krylov-step.md) — the per-step body's `derived_views K' op` projection consumes `nrm2` for the residual-norm readout (CG, MINRES) and the Arnoldi sub-diagonal scalar (GMRES). The convergence-test consumer at the surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` per the [`convergence-test`](../concepts/convergence-test.md) discipline.

**Cross-cutting concepts**:

- [`nrm2`](../concepts/nrm2.md) — the cross-cutting concept page with BLAS-1 heritage framing.
- [`dot`](../concepts/dot.md) — referenced transitively through the defining identity `nrm2(x) = √dot(x, x)`.
- [`convergence-test`](../concepts/convergence-test.md) — the consuming context at the outer `iterate_while_L3` loop.

**L1 anchor**: [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) — the L1 entry is authoritative on the Palace surface details, the one-line `linalg::Norml2` template definition, the relationship to the B-weighted overload (separately tracked), and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

1. **element-type** (`real` | `complex`) — at L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 / L3 these **collapse to a single operator** with the same signature `Tensor[N] -> Scalar(real)`, because the result is real-valued regardless of input element type (the Hermitian self-dot is real per `dot` law 4 / 9), and the defining identity `nrm2(x) = √dot(x, x)` is shared across element types.

This is a stronger collapse than `dot`'s element-type axis: `dot` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not.

No other variant axes at L3:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (the operator-weighted energy norm) tracked as [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1 (rough-in cycle-010 wave-1). The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0).
- **Stability variants**: BLAS-style scaled-summation `nrm2` is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x, x⟩` form. Not a variant axis of the L3 operator.

## Status

`firm` — L3 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); algebraic laws inherited unchanged; variant-axis profile inherited unchanged at one axis. The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification). Harvested cycle-011 wave-1 as part of the BLAS-1 reduction cohort backfill (sibling dispatch to `apply_linop`, the axpy cohort, `dot`, and `scal` at L3).

## Lowers to

L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body or outer convergence-test consumer, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `nrm2` lives at the L1 entry's evidence section (`book/src/L1/nrm2.md` §Evidence) — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` is the one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`; the `std::abs` outer guard is a load-bearing defensive non-negativity check against floating-point round-off pushing the sum slightly negative; the inner `Dot` carries the MPI_Allreduce. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.

## Lifts from

`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"). At L4, `nrm2` appears inside larger composed entries (e.g., `book/src/L4/krylov-step.md` §Semantics body — `outputs.residual_norm` computed via `nrm2` or via the recurrence shortcut) as a let-binding consuming the L3-native primitive surface; it carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), the defining identity `nrm2(x) = √dot(x, x)`, the B-weighted-overload boundary, and the complete L0 evidence list (`vector.hpp:255-260`, `vector.hpp:262-270`, `operator.hpp:372-374`, `operator.cpp:600-619`, etc.).
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — the dependency anchor; provides laws 4 / 9 (Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positivity depend.
- [`book/src/L3/dot.md`](./dot.md) (firm cycle-011, sibling dispatch) — the L3 dependency anchor; the defining identity `nrm2(x) = √dot(x, x)` is L3-internal.
- [`book/src/L3/index.md`](./index.md) line 13 — the L3 vocabulary inventory explicitly names `nrm2` as an L3 field operation. This L3 entry closes the inventory-vs-content gap noted by the cycle-010 audit.
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics — the consuming context at L3; the per-step body's `derived_views` projection consumes `nrm2` for residual-norm readout; the `op.orthog` closure consumes `nrm2` for Arnoldi sub-diagonal coefficients.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the load-bearing statement that the seven L1 primitives (including `nrm2`) are L3-native by signature shape. This is the structural justification for the L3>L1 identity-in-form rotation.
- [`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — the L3 body let-chain renders `nrm2` as an L3-native primitive call identical in shape to its L1 signature.
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; the BLAS-1 heritage framing. (Note: the concept page's stability claim ("Palace uses scaled summation") is incorrect per the L1 entry's correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES iterative solvers using `linalg::Norml2` for: initial right-hand-side norm `β = ‖b‖`, true residual norm `‖r‖`, and Arnoldi sub-diagonal coefficients `H[j+1,j] = ‖w‖`. Direct evidence `nrm2` is the convergence-test and Arnoldi-orthogonalization primitive, inherited transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement", inherited transitively. (Path relative to `reference/palace/`.)
- Cycle-010 audit at [`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`](../../../reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md) §"Per-candidate verdict" (2) — HIGH CONFIDENCE backfill recommendation for the BLAS-1 cohort at L3, including `nrm2`. This entry is the enactment.

## L3 vs L1 distinction

- **L1**: pure functional reduction `α = nrm2(x)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature; the MPI collective is folded into the L1>L0 lowering. The B-weighted overload is factored out as a separate L1 operator (`matrix-weighted-norm` rough-in). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8.
- **L3**: whole-tensor reduction `α = nrm2(x)` rendered as an L3 field operation. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body's `derived_views` projection, or the Arnoldi sub-diagonal in `op.orthog`) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `nrm2` itself is consumed as a leaf reduction with no iteration view of its own. The signature is identical to L1; the rotation is at the surrounding wrapper, not on the primitive.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `nrm2` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**.
````

---

## Dep-map and SUMMARY updates

### `book/src/L3/index.md` — append rows to operator dep-map

Append two rows (after the existing `krylov-step` row, lines 19-21) to the dep-map table:

```markdown
| [`dot`](./dot.md) | `Tensor[N] -> Tensor[N] -> Scalar` (real `dot` → real, complex `dot` → complex; complex `tdot` → complex; per-element kernel parameterized by element-type and conjugation-convention). | (leaf reduction at L3; consumed by `krylov-step`). Concepts: `dot`. | L1 [`dot`](../L1/dot.md) (identity-in-form on the primitive's signature; rotation work is at the consuming `krylov-step` body wrapper, captured by `book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" point 3). No L3-L1 theme file — identity-in-form annotation lives in-line. | `firm` (harvested cycle-011T231500Z; identity-lowering backfill per CLAUDE.md §Methodology invariants — supersedes cycle-006 "no L3 row needed" verdict for the BLAS-1 cohort) |
| [`nrm2`](./nrm2.md) | `Tensor[N] -> Scalar` (always real-valued; element-type axis collapses to single operator). | L3: [`dot`](./dot.md) via the defining identity `nrm2(x) = √dot(x, x)`. Concepts: `nrm2`, `convergence-test` (consumer-side). | L1 [`nrm2`](../L1/nrm2.md) (identity-in-form on the primitive's signature; rotation work is at the consuming `krylov-step` body wrapper / outer convergence-test consumer, captured by `book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" point 3). No L3-L1 theme file — identity-in-form annotation lives in-line. | `firm` (harvested cycle-011T231500Z; identity-lowering backfill per CLAUDE.md §Methodology invariants) |
```

Also update the Working Notes section (after line 28) to add:

```markdown
- **Cycle-011 wave-1: BLAS-1 cohort backfill in flight** (`apply_linop`, `dot`, `nrm2`, `axpy`/`axpby`/`axpbypcz`, `scal` — sibling harvester dispatches). Each entry is a layer-coherence anchor per **Identity-lowerings still require both L levels**; the L3 form is value-thread-isomorphic to the L1 form for all leaf primitives. The rotation work for the cohort lives at the consuming `krylov-step` body wrapper, captured by `book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" point 3. No `book/src/L3-L1/` theme directory is created — the identity-in-form annotation lives in-line at each L3 entry (precedent: cycle-010 `L3/krylov-step.md`).
```

### `book/src/SUMMARY.md` — add chapter entries

Insert two chapter entries under the L3 Part, after the existing `krylov-step` entry (line 19):

```markdown
- [dot](./L3/dot.md)
- [nrm2](./L3/nrm2.md)
```

Resulting L3 Part block:

```markdown
# L3 — Global Tensor-Field Operations
- [Overview](./L3/index.md)
- [krylov-step](./L3/krylov-step.md)
- [dot](./L3/dot.md)
- [nrm2](./L3/nrm2.md)
```

Sibling dispatches (#1 apply_linop, #2 axpy cohort, #4 scal) will add their own entries under this Part; the integrator-finalize is expected to reconcile the ordering across wave-1 if conflicts arise.

---

## Supporting evidence

**Files read for this dispatch:**

- `/home/crutcher/git/palace_whiteroom/book/src/L3/krylov-step.md` (precedent template; cycle-010 wave-1)
- `/home/crutcher/git/palace_whiteroom/book/src/L1/dot.md` (firm L1; authoritative source)
- `/home/crutcher/git/palace_whiteroom/book/src/L1/nrm2.md` (firm L1; authoritative source)
- `/home/crutcher/git/palace_whiteroom/book/src/L3/index.md` (vocabulary inventory; advertises dot/nrm2 at line 13)
- `/home/crutcher/git/palace_whiteroom/book/src/L3-L2/krylov-step-body-identity.md` (firm L3-L2 theme; §"Applicability conditions" point 3 is the load-bearing structural justification)
- `/home/crutcher/git/palace_whiteroom/book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm L4-L3 theme; renders dot/nrm2 in L3 let-chain identically to L1)
- `/home/crutcher/git/palace_whiteroom/book/src/L2/krylov-step.md` (firm L2; cross-reference for consuming context)
- `/home/crutcher/git/palace_whiteroom/book/src/concepts/dot.md` (concept page; BLAS-1 heritage framing)
- `/home/crutcher/git/palace_whiteroom/book/src/concepts/nrm2.md` (concept page; BLAS-1 heritage framing)
- `/home/crutcher/git/palace_whiteroom/book/src/L1/index.md` (L1 vocabulary cohort; dep-map shape reference)
- `/home/crutcher/git/palace_whiteroom/book/src/SUMMARY.md` (current Part structure)
- `/home/crutcher/git/palace_whiteroom/reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` (HIGH CONFIDENCE backfill recommendation)

**Key supporting passages:**

- `book/src/L3-L2/krylov-step-body-identity.md:97` — "The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are firm post-cycle-004; each operates on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." — the load-bearing structural statement that justifies the L3>L1 identity-in-form rotation for `dot` and `nrm2`.
- `book/src/L3/index.md:13` — "Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)" — the inventory line that this backfill closes for `dot` and `nrm2`.
- `book/src/L1/nrm2.md:11` — "Note: the concept page claims Palace uses 'scaled summation (BLAS nrm2 algorithm) to avoid overflow/underflow'. This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`." — the L1 correction-pending note carried forward into the L3 entry's §Context.
- `book/src/L1/dot.md:43, 104-105` — the documented L0/L1 conjugation-convention asymmetry (L0 free-function `linalg::Dot(comm, x, y) = yᴴ x` vs. L1/L3 first-arg-conjugation convention). Carried forward unchanged at L3.
- CLAUDE.md §Methodology invariants — **Identity-lowerings still require both L levels** — the codification (cycle-009) that justifies the L3 entries existing at all despite identity-in-form rotation.

## Open questions / caveats

1. **No L3-L1 lowering theme directory.** The two L3 entries record the identity-in-form L3>L1 rotation in-line (in §"Lowers to") rather than creating a separate `book/src/L3-L1/dot-identity.md` / `nrm2-identity.md` theme. This follows the cycle-010 `L3/krylov-step.md` precedent (also records its lowering in-line). The cycle-010 audit's open question (#1) — "L3-L1 lowering theme directory does not exist" — remains open; the cycle-011 wave-1 sibling dispatches are collectively setting the in-line-annotation precedent across the cohort. The cycle-011+ planner or meta-phase may want to formalize this as a policy decision (in-line annotation vs. dedicated `L3-L1/` themes). Surfacing as: **OQ candidate: `l3-l1-identity-in-form-annotation-policy-formalization`** — formalize whether identity-in-form L3>L1 rotations are recorded in-line at the L3 entry (current cycle-011 wave-1 convention) or as dedicated `book/src/L3-L1/` theme files. The wave-1 cohort sets the in-line precedent; meta-phase or layer-intro-author should bless or refine.

2. **Concept page `concepts/nrm2.md` carries an incorrect stability claim.** Per `book/src/L1/nrm2.md:11`, the concept page states "Palace uses scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow" — but `linalg::Norml2` actually computes the naive `√⟨x, x⟩`. The L1 entry flags this as correction-pending; the L3 entry repeats the flag in §Context. **Out of scope for this harvester dispatch** (would require editing `book/src/concepts/nrm2.md`, which is a layer-intro-author / cross-cutter concern, not harvester). Surfacing as: **OQ candidate: `concepts-nrm2-stability-claim-correction`** — `book/src/concepts/nrm2.md:8-9` claims Palace uses BLAS scaled-summation for `nrm2`, but `linalg::Norml2` computes the naive `√⟨x, x⟩` (per the firm L1 entry's correction note at `book/src/L1/nrm2.md:11`). Layer-intro-author / cross-cutter should correct.

3. **Wave-1 coordination with sibling dispatches.** This dispatch produces L3 entries for `dot` and `nrm2`. Sibling #2 (axpy cohort) will produce L3 entries for `axpy`, `axpby`, `axpbypcz`. Sibling #1 (apply_linop) will produce an L3 entry for `apply_linop`. Sibling #4 (scal) will produce an L3 entry for `scal`. **Each sibling will edit `book/src/L3/index.md` to add its own dep-map rows and `book/src/SUMMARY.md` to add its own chapter entries.** The integrator-per-report applies sibling reports serially, so the per-cycle staging should naturally serialize the edits — but the integrator may need to merge the Working Notes bullet that this dispatch and the sibling dispatches all propose (the "Cycle-011 wave-1: BLAS-1 cohort backfill in flight" addition). The merge is mechanical; surfacing here for integrator awareness.

4. **No L4 entries proposed for `dot` or `nrm2`.** Per the cycle-010 audit verdict (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"), leaf primitives are not first-class L4 vocabulary; they appear inside L4 entries (like `book/src/L4/krylov-step.md`) as let-bindings. This dispatch honors that verdict and does not propose L4 entries.

5. **The MPI collective is not in the L3 signature.** This dispatch follows the L1 convention (single-rank is in scope per CLAUDE.md §Scope; MPI collectives appear only in lowering themes). The L3 form sees a single-step whole-tensor reduction; the local-then-collective two-step reappears at L1>L0. **No change from L1 in this regard** — verified consistent with `book/src/L3/krylov-step.md` §Semantics and the upstream L4-L3 / L3-L2 themes.

6. **No new variant axes introduced at L3.** Both `dot` and `nrm2` preserve their L1 variant-axis profiles unchanged (`dot`: 2 axes; `nrm2`: 1 axis). The variant-axis count is closed at L1 and inherited; no L3-specific axis appears.

7. **Tests-as-semantic-supplement citations are transitive.** This dispatch cites `test/unit/test-vector.cpp:206-207` (for `dot`) and `test/unit/test-vector.cpp:209-211` (for `nrm2`) transitively through the L1 entries. Direct test re-verification was not done — the L1 entries' citations are taken as authoritative per the firm-status carried forward.

8. **L3 entries do not duplicate L0 evidence lists.** Each L3 entry cites the L1 entry for the complete L0 evidence list and selectively cites Palace source ranges only where the L3 consuming context is direct (e.g., `palace/linalg/iterative.cpp:631, 810` for `nrm2`'s Arnoldi sub-diagonal usage). This avoids duplication while preserving citation-grounded traceability per CLAUDE.md §Methodology invariants.
