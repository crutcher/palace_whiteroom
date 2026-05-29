---
agent: harvester
invoked_at: 2026-05-29T163011Z
scope: L1 operator: normalize (decision-first)
status: pending
inputs:
  - OQ normalize-as-fused-l1-primitive
  - OQ normalize-and-normalize-b-weighted-l1-candidates
  - plan item normalize-l1-primitive-harvest (scaffolding/priorities.md:54)
  - book/src/L1/scal.md (firm; flags this OQ in §Dependencies + §L1-vs-L0)
  - book/src/L1/nrm2.md (firm)
  - book/src/L1/matrix-weighted-norm.md (rough-in; the B-weighted norm)
  - book/src/L1-L0/scal-mutation-rotation.md (names the scal(1/nrm2) idiom + this OQ)
  - book/src/L2-L1/orthogonalize-composition-lowering.md (nrm2/scal normalize step)
  - Palace evidence: linalg::Normalize template + 5 consuming call sites
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-4). NEW firm L1 operator normalize :: Tensor[N] -> (Scalar, Tensor[N]) (decided YES; positive site linalg::Normalize, firm-on-positive-structure; nrm2+scal deps; normalize_B as in-chapter rough-in note). L1 firm 19→20. L1/index cohort bullet + dep-map row inserted (count-prose bump deferred to finalize → applied as Firm(19)→(20) at index.md:31). SUMMARY chapter registered. plan item normalize-l1-primitive-harvest COMPLETE; residual normalize-mutation-rotation L1>L0 theme forward-referenced (abstractor follow-up). Zero gate hits."

# CYCLE: Formalize normalize at L1

## Summary
The candidate is a fused L1 `normalize :: Tensor[N] -> (Scalar, Tensor[N])` — compute `β = ‖v‖₂`, rescale `v ← v/β`, **return BOTH** the norm and the normalized vector — plus a B-weighted sibling `normalize_B` using the energy norm `√(vᴴ B v)`. **Verdict: YES, promote to firm.** The decision is not marginal: Palace ships a *literal* `linalg::Normalize` free function (`palace/linalg/vector.hpp:262-270`) that is exactly this fused construct and **returns the norm** — so this is a firm-on-positive-structure harvest, not a speculative reconstruction. The returned-norm detail is load-bearing at three firm/near-firm consumers (GMRES Arnoldi stores it as the Hessenberg sub-diagonal entry; the spectral-radius power iteration *is* the returned norm; NEP deflation reuses it to scale a companion vector). The fused primitive collapses the recurring 2-op `nrm2 ∘ scal` idiom that the `scal`, `nrm2`, `orthogonalize` and `scal-mutation-rotation` entries already spell out by hand. The B-weighted sibling is recorded as a **rough-in note within the same chapter** (not a separate firm operator): Palace has the B-weighted `Norml2(comm, x, B, Bx)` reduction ([`matrix-weighted-norm`](../../book/src/L1/matrix-weighted-norm.md), rough-in) but **no** fused `Normalize`-with-B free function — the B-weighted normalize is always spelled inline (`scale = Norml2(comm, v); v *= 1/scale`, e.g. nleps.cpp:610-611 uses the *unweighted* norm there; the B-weighted reductions at arpack.cpp:438 / slepc.cpp:475 / nleps.cpp:114 are error-norm computations that do **not** rescale). So `normalize` lands firm; `normalize_B` lands as an in-chapter rough-in note inheriting `matrix-weighted-norm`'s test-coverage bound.

## Decision record

**Criterion** (CLAUDE.md "promote a speculative L1 operator to firm only when small AND when it simplifies the semantics of higher forms"): a fused `normalize` must (1) be small, (2) collapse a recurring multi-op idiom across ≥2 firm consumers, and (3) capture the load-bearing detail. All three are met, and additionally there is a **positive Palace source site** (which by itself qualifies under firm-on-positive-structure, independent of the simplification argument).

1. **Positive source site (decisive).** `linalg::Normalize` at `palace/linalg/vector.hpp:262-270`:

       template <typename VecType>
       inline auto Normalize(MPI_Comm comm, VecType &x)
       {
         auto norm = Norml2(comm, x);
         MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!");
         x *= 1.0 / norm;
         return norm;
       }

   This is `normalize` verbatim: it is the fused `nrm2` + `scal(1/nrm2, ·)` that **returns the norm**. Not a reconstruction — a read closure. This is the same firm-on-positive-structure footing as `apply_nonlinear_pencil` / `lu_solve` (laws are syntactic identities on positive source). Verified on-disk via `citecheck --anchor` (codemap `search_text` does not index the header; on-disk `reference/palace/` is authoritative, per dispatch instruction).

2. **Recurring 2-op idiom across firm consumers.** Both constituents are firm L1 leaves ([`nrm2`](../../book/src/L1/nrm2.md), [`scal`](../../book/src/L1/scal.md)). The `nrm2 ∘ scal` normalize step is currently spelled by hand in:
   - `book/src/L1/scal.md:65` — "`Normalize(x) = scal(1 / nrm2(x), x)` paired with the returned norm" (sibling-subsumption note).
   - `book/src/L1/scal.md:85` — "The fused `Normalize` construct factors at L1 as `scal(1/nrm2(x), x)`".
   - `book/src/L1-L0/scal-mutation-rotation.md:48-49,141-147` — sub-pattern A names the `x *= 1.0/norm` rescale inside `linalg::Normalize` and explicitly defers the fused-primitive decision to *this* OQ.
   - `book/src/L2-L1/orthogonalize-composition-lowering.md:229` — "`nrm2` / `scal`" as the basis-normalize step after Gram-Schmidt (FGMRES, ROM basis-extension sites).
   - `book/src/L2/orthogonalize.md:158` — `scal (1/‖residual‖)` normalisation with the sub-diagonal `H[m] = ‖residual‖`.

   That is ≥2 firm consumers (`scal`, `nrm2`, `orthogonalize` all firm) spelling the same 2-op idiom; the fused operator names it once.

3. **Load-bearing returned-norm detail.** The norm is RETURNED, not discarded, and downstream code consumes it at three independent sites — this is the detail that `nrm2 ∘ scal` as a bare composition *loses* (it would discard the intermediate):
   - **GMRES Arnoldi** (`palace/linalg/iterative.cpp:631-632`): `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` — the norm is **stored as the Hessenberg sub-diagonal entry** `Hj[j+1]` AND used to normalize `w`. Doubly load-bearing. Second identical path at `:811` (`:632`'s code is reached via the GMRES `Hj[j+1]` write at `:631`).
   - **Spectral-radius power iteration** (`palace/linalg/operator.cpp:661,673`): `Normalize(comm, u)` initial, then `l = Normalize(comm, u)` in the loop — the returned norm `l` **IS the dominant-eigenvalue estimate** driving the convergence test `res = std::abs(l - l0)/l0` (`:676`). Here the returned norm is the entire point; the normalized vector is the byproduct.
   - **NEP deflation basis growth** (`palace/linalg/nleps.cpp:610-611,617`): `const auto scale = linalg::Norml2(GetComm(), v); v *= 1.0 / scale;` then `H.col(k).head(k) = v2 / scale;` — the norm `scale` rescales BOTH `v` (the basis vector) AND `v2` (the coordinate companion). Doubly reused.

4. **Small + simplifies higher forms.** The operator is a 2-line body returning a pair. It simplifies the L2>L1 and L1>L0 normalize-step prose (one named operator instead of "`nrm2` then `scal`"), and it gives GMRES/Arnoldi basis-construction and power-iteration a single vocabulary item whose returned-scalar slot is exactly the Hessenberg-entry / eigenvalue-estimate consumer. The Arnoldi `krylov-step` (L2) and the `orthogonalize-composition-lowering` (L2>L1) both gain a cleaner spelling.

**OQ resolution.** Both `normalize-as-fused-l1-primitive` and `normalize-and-normalize-b-weighted-l1-candidates` resolve **decided-yes** for the unweighted `normalize` (firm) and **decided-yes-as-in-chapter-rough-in-note** for `normalize_B` (no fused Palace site; inherits `matrix-weighted-norm`'s test-coverage bound). Plan item `normalize-l1-primitive-harvest` (scaffolding/priorities.md:54) is completed by this dispatch.

## Proposed changes

```new:book/src/L1/normalize.md
# normalize

Mutation-lifted fused vector normalisation: compute `β = ‖x‖₂`, rescale `x ← x/β`, and **return both** `β` and the unit vector. The L1 lift of Palace's `linalg::Normalize` free function — the fused `nrm2` + `scal(1/nrm2, ·)` construct whose **returned norm** is load-bearing (Arnoldi Hessenberg sub-diagonal entry, spectral-radius eigenvalue estimate, deflation companion-vector scale).

## Context

`normalize` lifts the free-function template `linalg::Normalize(comm, x)` at `palace/linalg/vector.hpp:262-270` — which computes `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;` — to a single pure-functional fused operator. It is the **only** Palace `scal` use that returns its scalar (the norm), and the returned scalar is the reason this is a distinct named operator rather than a bare composition: many call sites consume `β` *after* the rescale (the Arnoldi sub-diagonal, the power-iteration eigenvalue estimate, the deflation companion-vector scale). A bare `scal(1/nrm2(x), x)` discards that intermediate; `normalize` retains it in the result.

The two constituents are firm L1 leaves: [`nrm2`](./nrm2.md) (`β = √⟨x,x⟩`) and [`scal`](./scal.md) (`x/β = scal(1/β, x)`). `normalize` is the fused pairing — it is to `nrm2`/`scal` what `axpy` is to `scal`/vector-add: a recognised composite that Palace ships as one symbol. Unlike `axpy`, which returns nothing, `normalize` carries one extra load-bearing output (the recovered norm), and that extra returned scalar is what justifies naming the fusion. The fusion is named at [`scal`](./scal.md) §Dependencies and §L1-vs-L0, and the rescale half is the sub-pattern A of [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md); this entry is the firm operator that consolidates them.

The element-type axis (real / complex, with a real-valued norm output regardless) is inherited from `nrm2` (the norm is always real) and `scal` (the rescale matches the input element type). No new variant axis is introduced by the fusion. The MPI collective folded inside `Norml2`'s inner `dot` is an L1>L0 concern, not part of this signature (single-rank is in scope per `CLAUDE.md`).

The B-weighted sibling `normalize_B` (rescale by the energy norm `√(xᴴ B x)`) is recorded below as a **rough-in note**, not a separate firm operator — Palace has the B-weighted reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (rough-in) but **no** fused `Normalize`-with-`B` free function; B-weighted normalisation is always spelled inline, and the only inline B-energy rescale sites use the *unweighted* norm.

## Signature

    normalize :: (x: Tensor[N]) -> (Scalar, Tensor[N])
    normalize(x) = (β, x/β)  where  β = nrm2(x),  β > 0

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only (the *prior* value). Element type real or complex.
- result.0 — `Scalar` — **always real-valued and positive** (`β = ‖x‖₂ > 0`), regardless of `x`'s element type (inherited from `nrm2`'s real-valued-output collapse).
- result.1 — `Tensor[N]` — the unit vector `x/β`, same axis `N` and same element type as `x`. Has unit norm: `nrm2(result.1) = 1` (in exact arithmetic).

Applicability precondition: `β > 0`, i.e. `x ≠ 0`. The L0 source asserts this directly (`MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!")` at `palace/linalg/vector.hpp:267`). `normalize` is **partial** — undefined on the zero vector. This is the one applicability condition distinguishing it from the (total) `nrm2` and `scal` leaves it composes.

## Semantics

Definitional: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. The norm is computed once and both returned and used as the rescale divisor — the fusion is the single-evaluation pairing, not a new arithmetic.

Reduction-tree non-associativity is **load-bearing**, inherited unchanged from the inner `nrm2` (hence from `dot`). The rescale `scal(1/β, ·)` is element-local and adds no reduction. The reciprocal-then-multiply (`1.0 / norm` then `x *= …`, rather than a per-element divide) is the L0 form; at L1 it is the algebraic `x/β`, and any reciprocal-vs-divide bit-difference is an L1>L0 transparent-trick note.

The **returned norm is the load-bearing output**. Three consumer shapes recur:
- The norm is captured into a separate structure and the unit vector is the working result (GMRES Arnoldi: `β` becomes the Hessenberg sub-diagonal `H[j+1,j]`, the unit `w` extends the Krylov basis — `palace/linalg/iterative.cpp:631-632`).
- The norm is the working result and the unit vector is the carrier for the next iteration (spectral-radius power iteration: `l = Normalize(comm, u)` returns the dominant-eigenvalue estimate, `u` is renormalised for the next `A·u` — `palace/linalg/operator.cpp:661` and `:673`).
- The norm rescales a *companion* quantity as well as `x` (NEP deflation: `scale` rescales both the basis vector `v` and its coordinate companion `v2 / scale` — `palace/linalg/nleps.cpp:610-611,617`; note this site uses the unweighted norm via an inline `Norml2` + `*=`, the same shape as `linalg::Normalize` but written out).

The operator is pure at L1: the prior `x` and the unit vector are distinct values, and `β` is a fresh scalar. The L0 source overwrites the receiver buffer in place and returns the norm by value; the L1>L0 lowering reintroduces the in-place rescale (it composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding).

## Algebraic laws

The laws below hold for `x ≠ 0` (the operator's domain); absences are deliberate. Write `normalize(x) = (β, û)` with `β = nrm2(x)` and `û = x/β`.

1. **Unit output**: `nrm2(û) = 1` (in exact arithmetic). The defining property — the second result has unit norm.
2. **Norm recovery**: `β = nrm2(x)`. The first result is exactly the input's norm; this is the projection `fst ∘ normalize = nrm2`.
3. **Reconstruction**: `scal(β, û) = x`, i.e. `β · (x/β) = x`. The pair `(β, û)` losslessly reconstructs `x` (the inverse of the `scal` law-8 round-trip, with `α = 1/β`). This is why `normalize` is information-preserving where a bare unit-vector projection would not be.
4. **Positive homogeneity collapse (scale invariance of the unit vector)**: for any scalar `α ≠ 0`, `snd(normalize(scal(α, x))) = scal(α/|α|, û)`. For real positive `α`: `snd(normalize(α·x)) = û` (the unit vector is invariant under positive rescaling of the input). For complex `α`: the unit vector picks up the phase `α/|α|`. Correspondingly `fst(normalize(scal(α, x))) = |α|·β` (positive homogeneity inherited from `nrm2`).
5. **Idempotence of the unit vector (up to the trivial norm)**: `normalize(û) = (1, û)`. Normalising an already-unit vector returns norm `1` and the same vector. Equivalently `snd ∘ normalize ∘ snd ∘ normalize = snd ∘ normalize` (the unit-vector projection is idempotent) and `fst(normalize(snd(normalize(x)))) = 1`.
6. **Factorisation (the defining decomposition)**: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. This is the L1 statement of the fusion — both components in terms of the firm leaves. It is the law a lowering theme or an L2 consumer rewrites against.

Laws that explicitly **do not** hold:

- **Totality**: `normalize` is undefined at `x = 0` (`β = 0`, division by zero; the L0 `MFEM_ASSERT(norm > 0.0)` fires). Unlike `nrm2(0) = 0` and `scal(α, 0) = 0` (both total), the fused operator is **partial**. This is the single semantic addition of the fusion over its constituents.
- **Additivity / linearity**: `normalize(x + y) ≠ (β_x + β_y, û_x + û_y)` in any form — the norm is sublinear (triangle inequality, from `nrm2`) and the unit vector is a nonlinear (projective) function of the input. The operator is **not** linear in `x`; it is positively-homogeneous-of-degree-zero in the unit-vector component (law 4) and degree-one in the norm component.
- **Bit-level fusion equivalence**: the L0 reciprocal-then-multiply (`x *= 1.0/norm`) and an idealised per-element divide (`x[i] /= norm`) may differ at the bit level in IEEE-754. The reciprocal form is Palace's actual L0 (`vector.hpp:268`); pinning it is an L1>L0 transparent-trick note, not an L1 law — the algebraic value `x/β` is the same.

## Dependencies

L1-internal dependencies (this is a fused composite, not a leaf):

- [`nrm2`](./nrm2.md) — the norm computation `β = √⟨x,x⟩` (result.0, and the rescale divisor).
- [`scal`](./scal.md) — the rescale `û = scal(1/β, x)` (result.1).

Subsumption / sibling relationships (not dependencies):
- `normalize` is the fused pairing flagged at `book/src/L1/scal.md:65,85` and `book/src/L1/nrm2.md` — those entries name the composition; this entry consolidates it as a firm operator with the returned-norm output made first-class.
- Bare `scal(1/nrm2(x), x)` (norm discarded) is the projection `snd ∘ normalize`. When a consumer needs only the unit vector and not the norm, the `scal ∘ nrm2` spelling is equivalent; `normalize` is preferred when the norm is consumed downstream (the load-bearing case).

Downstream consumers at L1/L2 (cross-reference, not reverse-dependencies):
- GMRES Arnoldi basis-normalisation `H[j+1,j] = β; w ← w/β` (`iterative.cpp:631-632, 811`) — the L2 `krylov-step` Arnoldi body.
- Spectral-radius power iteration (`palace/linalg/operator.cpp:661,673` via `linalg::Normalize`) — the returned norm is the eigenvalue estimate.
- NEP deflation-basis growth (`nleps.cpp:610-611,617`) — inline form; norm rescales basis + coordinate companion.
- Gram-Schmidt output normalisation in [`orthogonalize`](./orthogonalize.md) / [`orthogonalize-composition-lowering`](../L2-L1/orthogonalize-composition-lowering.md) — the `nrm2`/`scal` normalize step after orthogonalisation (FGMRES, ROM basis-extension).

## Variant axes

`normalize` inherits exactly the element-type axis of its constituents and adds none:

- **element-type**: `real` | `complex`. The `linalg::Normalize` template is `VecType`-generic (`mfem::Vector` real / `ComplexVector` complex); the inner `Norml2` returns a real scalar in both cases (per [`nrm2`](./nrm2.md)) and the `*= 1.0/norm` rescale dispatches to the matching `operator*=` (per [`scal`](./scal.md), including the `imag(s)==0.0` real-into-complex promotion). At L1 these collapse to one operator parameterised by element type; the norm output is real-valued in all variants.

No constant-folding axis (the rescale scalar `1/β` is a runtime value, never `0`/`1`/`-1` by construction since `β > 0`). No reduction-order variant beyond `nrm2`'s inherited one. The only non-trivial semantic axis relative to the leaves is the **partiality** at `x = 0`, which is uniform across element types.

### B-weighted sibling `normalize_B` — rough-in note (NOT a separate firm operator)

The energy-norm normalisation `(β_B, x/β_B)` with `β_B = √(xᴴ B x)` for SPD `B` is a *recognised* construct but lands here as a **rough-in note**, deliberately not a separate firm chapter, for two reasons:

1. **No fused Palace site.** Palace has no `linalg::Normalize`-with-`B` free function. The header comment at `palace/linalg/vector.hpp:262` ("Normalize the vector, possibly with respect to an SPD matrix B") is **aspirational/documentary** — the sole `Normalize` overload (`:264`) takes no `B`. The B-weighted reduction exists ([`matrix-weighted-norm`](./matrix-weighted-norm.md) = `linalg::Norml2(comm, x, B, Bx)`, `palace/linalg/operator.cpp:600-619`), but its call sites (`palace/linalg/arpack.cpp:438`, `palace/linalg/slepc.cpp:475`, `palace/linalg/nleps.cpp:114`) are **error-norm / eigenvector-norm computations that do not rescale** — they feed `GetError` / residual ratios, not an in-place normalise.
2. **Inherited test-coverage bound.** `normalize_B`'s norm component is `matrix-weighted-norm`, which is `rough-in (test-coverage-bounded)` (no dedicated test on the SPD-weighted overload — `book/src/L1/matrix-weighted-norm.md:108-110`, `book/src/L1/index.md:80`). A fused `normalize_B` cannot be firmer than its norm constituent.

If/when an inline B-weighted normalise site surfaces (a `scale = Norml2(comm, v, B, Bv); v *= 1/scale` pattern, distinct from the unweighted nleps.cpp:610-611), `normalize_B` promotes to a firm sibling with signature:

    normalize_B :: (x: Tensor[N], B: LinearOperator[N, N]) -> (Scalar, Tensor[N])
    normalize_B(x, B) = (β_B, x/β_B)  where  β_B = matrix_weighted_norm(x, B),  B SPD,  β_B > 0

Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until then it is tracked as a queued candidate inheriting the `matrix-weighted-norm` promotion gate, NOT a firm operator.

## Status

`firm` — firm-on-positive-structure (the `apply_nonlinear_pencil` / `lu_solve` precedent). The signature matches `linalg::Normalize` exactly; the body is a read closure (`vector.hpp:262-270`), not a literature reconstruction; the six algebraic laws are syntactic identities on that positive source plus the inherited `nrm2`/`scal` algebra (themselves firm). The absence of a dedicated `test-normalize` does not gate the laws — they are operator-algebra identities, not convergence claims (the `apply_nonlinear_pencil` cycle-021 / `chebyshev-smoother` cycle-012 no-dedicated-test precedent applies; the `eigsolve` rough-in framing does **not** bind, as `normalize`'s laws carry no literature-inferred semantics). The one semantic addition over the leaves — partiality at `x = 0` — is positively anchored by the L0 `MFEM_ASSERT`. The B-weighted sibling `normalize_B` is an in-chapter **rough-in note** (no fused Palace site + inherited `matrix-weighted-norm` test-coverage bound), not part of the firm claim.

## L1 vs L0 distinction

- **L0**: mutating free-function template `linalg::Normalize(comm, x)` (`palace/linalg/vector.hpp:262-270`). Computes `norm = Norml2(comm, x)`, asserts `norm > 0`, rescales the receiver in place `x *= 1.0/norm`, returns `norm` by value. Three consuming shapes inline the norm (Arnoldi Hessenberg `palace/linalg/iterative.cpp:631-632`, power-iteration eigenvalue estimate `palace/linalg/operator.cpp:661` and `:673`, NEP deflation companion-scale `palace/linalg/nleps.cpp:610-611,617`). The MPI collective is folded inside `Norml2`'s inner `Dot`.
- **L1**: pure functional `(β, û) = normalize(x)`. No destination buffer, no communicator, no in-place mutation. The returned norm is a first-class result component (not a side output). The in-place rescale, the reciprocal-vs-divide trick, the `MPI_Allreduce`, and the receiver overwrite are all L1>L0 lowering concerns — the lowering composes [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) (no-buffer reduction) with [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A (in-place rescale) plus a returned-scalar binding. (The L1>L0 `normalize-mutation-rotation` theme is not authored by this dispatch — see Open questions; this entry references it as plain text, not a live link.)

## Evidence

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template: `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!"); x *= 1.0 / norm; return norm;`. The positive source site — `normalize` verbatim, returning the norm. The rescale is line 268; the assert (partiality precondition) line 267; the `return norm` line 269. **Self-verified** (`citecheck --anchor 'Normalize'` → line 264 def; `--anchor 'return norm'` → 269; `--anchor '1.0 / norm'` → 268).
- `palace/linalg/iterative.cpp:631-632` — GMRES Arnoldi: `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` — the returned norm stored as the Hessenberg sub-diagonal entry AND used to normalize. The inline (un-fused) form of `normalize` with both outputs consumed. **Self-verified** (`--anchor 'Hj[j + 1] = linalg::Norml2'` → 631; `--anchor '1.0 / Hj'` → 632).
- `palace/linalg/iterative.cpp:811` — second analogous GMRES Arnoldi code path, identical `w *= 1.0 / Hj[j + 1];`. **Self-verified** (`--anchor 'Hj'` → 811).
- `palace/linalg/operator.cpp:660-661` — `SetRandom(comm, u); Normalize(comm, u);` — power-iteration initial normalisation (returned norm discarded on the seed). **Self-verified** (`--anchor 'SetRandom(comm, u)'` → 660).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` — the returned norm `l` IS the dominant-eigenvalue estimate, consumed by the convergence test. **Self-verified** (`--anchor 'l = Normalize'` → 673).
- `palace/linalg/operator.cpp:676` — `res = std::abs(l - l0) / l0;` — the convergence test consuming the returned norm `l` from `:673`. Direct evidence the returned scalar is load-bearing. **Self-verified** (`--anchor 'res = std::abs(l - l0)'` → 676).
- `palace/linalg/nleps.cpp:610-611` — NEP deflation-basis growth: `const auto scale = linalg::Norml2(GetComm(), v); v *= 1.0 / scale;` — inline unweighted normalise. **Self-verified** (`--anchor 'Norml2(GetComm(), v)'` → 610; `--anchor '1.0 / scale'` → 611).
- `palace/linalg/nleps.cpp:617` — `H.col(k).head(k) = v2 / scale;` — the returned norm `scale` reused to rescale the coordinate companion `v2`. Doubly-load-bearing returned-norm. **Self-verified** (`--anchor 'v2 / scale'` → 617).
- `palace/linalg/operator.cpp:600-607` — B-weighted `Norml2(comm, x, B, Bx)` (the `matrix-weighted-norm` reduction): `B.Mult(x, Bx); double dot = Dot(comm, Bx, x); ...; return std::sqrt(dot);`. Evidence the B-weighted *reduction* exists but is **not** fused into a `Normalize`-with-`B` (no rescale). **Self-verified** (`--anchor 'B.Mult(x, Bx)'` → 602).
- L1 anchors: `book/src/L1/nrm2.md` (firm; `β = √⟨x,x⟩`, real-valued output), `book/src/L1/scal.md` (firm; `û = scal(1/β, x)`, law 8 round-trip), `book/src/L1/matrix-weighted-norm.md` (rough-in; the `normalize_B` norm constituent), `book/src/L1-L0/scal-mutation-rotation.md:48-49,141-147` (sub-pattern A names the `Normalize` rescale + defers this decision to this OQ).

Test evidence (L0-equivalent semantic documentation):
- `palace/test/unit/test-orthog.cpp:193,208` — `V[0] *= 1 / v0_norm;` / `V[1] *= 1 / v1_norm;` on real `Vector`s, each immediately after a `CHECK_THAT(v*_norm, ...)` assertion on the norm. The textbook by-hand `normalize` (norm asserted, then rescale) on the real path — empirical-match for the fused operator's two-output shape (cited via `scal-mutation-rotation.md:183-186`, inherited).
```

```edit:book/src/L1/index.md
- [`scal`](./scal.md) — pure vector-scalar multiply; the fourth BLAS-1 floor primitive (sibling-subsumed by `axpby` β=0).
```
```edit:book/src/L1/index.md
- [`scal`](./scal.md) — pure vector-scalar multiply; the fourth BLAS-1 floor primitive (sibling-subsumed by `axpby` β=0).
- [`normalize`](./normalize.md) — fused vector normalisation `(β, x/β) = normalize(x)`; the L1 lift of Palace's `linalg::Normalize`, composing [`nrm2`](./nrm2.md) + [`scal`](./scal.md) and **returning the norm** as a first-class result (load-bearing: Arnoldi Hessenberg sub-diagonal entry, spectral-radius eigenvalue estimate, deflation companion-vector scale). Firm-on-positive-structure (`linalg::Normalize` is a read closure). Partial: undefined at `x = 0` (L0 `MFEM_ASSERT`). Carries an in-chapter **rough-in note** for the B-weighted sibling `normalize_B` (no fused Palace site; inherits `matrix-weighted-norm`'s test-coverage bound).
```

```edit:book/src/L1/index.md
| [`scal`](./scal.md) | `(α, x) → α·x` | (leaf; subsumed by `axpby` via β=0) | `firm` |
| [`normalize`](./normalize.md) | `(x: Tensor[N]) → (Scalar, Tensor[N])` (i.e. `(β, x/β)`, `β = ‖x‖₂ > 0`) | `nrm2`, `scal` | `firm` (fused-normalise; firm-on-positive-structure; L0: `palace/linalg/vector.hpp:262-270` `linalg::Normalize` + call sites `palace/linalg/iterative.cpp:631-632,811`, `palace/linalg/operator.cpp:661,673`, `palace/linalg/nleps.cpp:610-611,617`; harvested cycle-026; partial at `x=0`; B-weighted `normalize_B` in-chapter rough-in note) |
```

```edit:book/src/SUMMARY.md
- [scal](./L1/scal.md)
- [normalize](./L1/normalize.md)
```

## Operator content
The full firm `normalize.md` body is authored inside the `new:book/src/L1/normalize.md` proposed-changes block above. Key points: signature `normalize :: Tensor[N] -> (Scalar, Tensor[N])` returning `(β, x/β)`; six algebraic laws (unit output, norm recovery, reconstruction, scale-invariance, idempotence, factorisation); partiality at `x=0` as the single semantic addition over the `nrm2`/`scal` leaves; element-type the sole inherited variant axis; `firm` on firm-on-positive-structure grounds; `normalize_B` as an in-chapter rough-in note.

## Supporting evidence
- Positive site: `linalg::Normalize` template `palace/linalg/vector.hpp:262-270` (read closure, returns norm).
- Load-bearing returned-norm at three firm/near-firm consumers: GMRES Arnoldi `palace/linalg/iterative.cpp:631-632,811` (Hessenberg sub-diagonal), power iteration `palace/linalg/operator.cpp:661,673,676` (eigenvalue estimate), NEP deflation `palace/linalg/nleps.cpp:610-611,617` (companion-vector scale).
- Idiom-collapse witnesses (≥2 firm consumers spelling `nrm2 ∘ scal`): `book/src/L1/scal.md:65,85`, `book/src/L1-L0/scal-mutation-rotation.md:48-49,141-147`, `book/src/L2-L1/orthogonalize-composition-lowering.md:229`, `book/src/L2/orthogonalize.md:158`.
- B-weighted negative finding: no fused `Normalize`-with-`B`; the `Norml2(comm, x, B, Bx)` overload (`palace/linalg/operator.cpp:600-619`) is used only for error/eigenvector norms (`palace/linalg/arpack.cpp:438`, `palace/linalg/slepc.cpp:475`, `palace/linalg/nleps.cpp:114`), never an in-place B-rescale. Header comment `palace/linalg/vector.hpp:262` "possibly with respect to an SPD matrix B" is aspirational (no `B` overload exists).
- All load-bearing citations self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk `reference/palace/` (codemap does not index `vector.hpp`; on-disk is authoritative, per dispatch instruction).

## Open questions / caveats
- **L1>L0 `normalize-mutation-rotation` theme not authored** (out of one-operator-per-dispatch scope). It composes the firm [`nrm2-mutation-rotation`](../../book/src/L1-L0/nrm2-mutation-rotation.md) (no-buffer reduction) with the firm [`scal-mutation-rotation`](../../book/src/L1-L0/scal-mutation-rotation.md) sub-pattern A (in-place rescale) plus a returned-scalar binding and the partiality `MFEM_ASSERT`. This entry references it as plain text (the file does not yet exist — `linkcheck2` would hard-fail a live link). Recommend an abstractor dispatch; low novelty (it's the composition of two firm sister themes), so a stub-on-integration is also acceptable per the implied-component directive. Worth registering as an OQ residual under the now-resolved `normalize-l1-primitive-harvest`.
- **`normalize_B` promotion trigger**: an inline B-weighted normalise site (`scale = Norml2(comm, v, B, Bv); v *= 1/scale`) would promote the in-chapter rough-in note to a firm sibling. None surfaced in this dispatch (the B-weighted `Norml2` sites are error-norm computations). Gated additionally on `matrix-weighted-norm`'s own test-coverage promotion. Track as a queued candidate under the `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` OQ residuals.
- **L2 consumers may want to re-spell against `normalize`**: the L2 `krylov-step` Arnoldi body and `orthogonalize-composition-lowering` (L2>L1) currently spell the normalize step as "`nrm2` then `scal`"; a follow-up lifter/abstractor pass could re-anchor them to `normalize` now that it is firm (with the returned norm feeding the Hessenberg entry). Not in scope here; noted for the planner. (Layer-intro note: `book/src/L1/index.md` §"Vocabulary cohort" firm-count text says "Firm (19)" — this dispatch raises it to 20; the layer-intro-author should refresh that count + the motif prose, per role partition. Flagged, not edited.)
- **OQ resolution**: `normalize-as-fused-l1-primitive` and `normalize-and-normalize-b-weighted-l1-candidates` both resolve **decided-yes** (firm for `normalize`; in-chapter rough-in note for `normalize_B`). Plan item `normalize-l1-primitive-harvest` (scaffolding/priorities.md:54) completed.
