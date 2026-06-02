---
agent: same-layer-cross-cutter
invoked_at: 2026-06-01T23:57:19Z
scope: L2 cross-cut — solver capacitance/inductance reduction is a K-weighted variant of firm L2 `gram`
status: pending
integrated_at: 2026-06-02T010500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-053 D2 — APPLIED clean. Landed 2 solver witnesses (capacitance electrostaticsolver.cpp:111-137 + inductance magnetostaticsolver.cpp:110-152) onto book/src/L2/gram.md B-weighted axis + relaxed the witness-less caveat + 3 Evidence rows; gram stays FIRM (coverage strengthening, NO count delta, NOT a new operator). Confirms the c052-D6 capacitance-reduction-may-be-gram-variant hypothesis. Witness anchors codemap-RESOLVED byte-exact. 3 OQs promoted incl. the deferred solver-postprocess-reduction-consumes-gram-distinct-dispatch. Build exit 0; gram.md edits in-place."
---

# CYCLE: L2 observation — capacitance/inductance reduction IS `gram` with the weighted-hook axis (no new operator)

## Summary
The solver capacitance (electrostatic, `electrostaticsolver.cpp:111-137`) and inductance
(magnetostatic, `magnetostaticsolver.cpp:110-152`) reductions compute, cell-by-cell,
`Xⱼᴴ K Xᵢ` over the full all-pairs of a small column set `X` (the per-terminal field
solutions), with `K` an **assembled FE mass matrix** (`M_elec` = ε-weighted
`VectorFEMassIntegrator`, `M_mag` = μ⁻¹-weighted mass integrator). This is **exactly** the
firm L2 [`gram`](../../book/src/L2/gram.md) all-pairs fold under its **already-documented
`B`-weighted hook variant axis** (`gram.md:197-202`, the `inner_product_M` hook giving
`G = XᴴBX`). The planner's "`XᴴKX` shape" `K` IS the `B` of `gram`'s existing weighted
hook — the assembled mass matrix is the concrete SPD weight. **It is NOT a new operator.**
The reduction is cleanly describable in existing L2 vocabulary; the only gap is that the
existing `B`-weighted axis is documented but **witness-less** (NLEPS uses the canonical
unweighted hook), and these two solver sites are its **first concrete Palace witnesses**.
I propose a small clean variant-axis-witness landing (a proposed-changes block adding the
two witnesses to the existing axis), per the redirect's "advance a layer when cleanly
describable in existing shared vocabulary."

## Observation kind
**Variant-axis coverage gap** — the solver capacitance/inductance reduction is the existing
firm L2 `gram` operator exercised on its already-documented-but-witness-less `B`-weighted
hook axis (axis: `I` → `B`/`K` weight matrix). Not a redundancy (it is the *same* operator,
correctly), not a unification candidate (nothing to unify — it already subsumes), not a new
operator.

## Specific finding

**The cell body is `gram2`'s weighted hook, verbatim.** Both solver loops pin
`Y := K · X[i]` once per outer index `i` (`electrostaticsolver.cpp:118`
`M_elec->Mult(V_gf, D_gf)`; `magnetostaticsolver.cpp:129` `M_mag->Mult(A_gf, H_gf)`), then
sweep the inner `j`:
- elec cell: `C(i,j) = linalg::Dot(V[j], M_elec·V[i]) = V[j]ᴴ M_elec V[i]`
  (`electrostaticsolver.cpp:126`),
- mag cell: `M(i,j) = linalg::Dot(A[j], M_mag·A[i]) / (Iᵢ Iⱼ) = A[j]ᴴ M_mag A[i] / (Iᵢ Iⱼ)`
  (`magnetostaticsolver.cpp:138`).

Stripping the `/(IᵢIⱼ)` (and elec's `/Vᵢ²` with `Vᵢ≡1`) post-Gram cell-scaling, each cell is
exactly `inner_product_M(X[j], K, X[i]) = X[j]ᴴ K X[i]` — the firm L2 weighted-inner-product
member (`book/src/L2/inner_product.md:129-133,169` `inner_product_M x M y = inner_product (apply_linop M
x) y`; `bilinear-form` leaf). That is precisely a **`gram` cell** read through `gram`'s
`B`-weighted hook (`gram.md:197-202`: "the `B`-weighted hook (`inner_product_M`) gives the
weighted Gram `G = XᴴBX`"), with column `j` (the column index) the conjugated operand —
`gram`'s pinned arg-1-conjugated convention (`gram.md:73-85`), real here so symmetric.

**Three structural matches confirm same-operator (not coincidence):**
1. **Weight is the same *kind* of object as `B`.** `M_elec`/`M_mag` are assembled
   `BilinearForm::PartialAssemble()` FE **mass matrices** (`domainpostoperator.cpp:38-39`
   ε-weighted `VectorFEMassIntegrator`; `:53-64` μ⁻¹-weighted mass integrator) — SPD
   operators, the identical category as the SLEPc/ROM `inner_product_M` mass-matrix weight
   `gram.md:197-202` already names. `K = M_elec` is `B`, concretely.
2. **All-pairs over a small column set `X`.** `V` / `A` are `std::vector<Vector>` of
   per-terminal/per-port field solutions; the double `for i { for j }` over `V.size()` /
   `A.size()` (`electrostaticsolver.cpp:112,124`; `magnetostaticsolver.cpp:123,135`) is the
   `gram` all-pairs index sweep, `k = #terminals`. This is the **single-set `gram dot X`**
   form (`X` against itself), `k×k`.
3. **Symmetry-exploitation is `gram`'s documented transparent perf-trick, present verbatim.**
   Both loops compute only the upper triangle (`j = i+1 ..`) and copy the lower
   (`electrostaticsolver.cpp:131-137` "Copy lower triangle"; `magnetostaticsolver.cpp:144-150`)
   — exactly the "compute upper triangle + conjugate-mirror" one-line transparent note
   `gram.md:180-182,213` already classifies as NOT a variant axis. (Aside: NLEPS's own
   `nleps.cpp:525-531` does *not* exploit symmetry — so these solver sites are also the
   first Palace witness of the symmetry-exploited *lowering* of the same fold, a footnote
   for the L2>L1 `gram-fold-specialization` theme, not for the L2 entry.)

**What is NOT part of `gram`** (correctly outside the fold, so it does not motivate a new
operator): the energy-formulation post-Gram cell normalization — elec `/Vᵢ²` (with `Vᵢ≡1`,
`electrostaticsolver.cpp:114`), mag `/(IᵢIⱼ)` (`magnetostaticsolver.cpp:126,138`) — and the
`Cm`/`Mm` "Maxwell capacitance/inductance" off-diagonal-sign remix
(`electrostaticsolver.cpp:127-129`; `magnetostaticsolver.cpp:139-141`), and the final
in-place `C.Invert()` / `M.Invert()` (`electrostaticsolver.cpp:138-139`;
`magnetostaticsolver.cpp:151-152`). These are downstream small-dense post-processing on the
weighted Gram, not the Gram build. They belong to a *solver post-processing* description that
**consumes** `gram` (the same consumer-vs-constituent split `gram.md:236-241` draws for
`deflate`), not inside `gram`.

**Conclusion on the three planner questions:**
- *Same operation as firm `gram`?* — **Yes**, it is `gram` with `dot := inner_product_M[K]`
  (the weighted hook) instead of the canonical Hermitian hook. The `XᴴKX` shape is `gram`'s
  `XᴴBX`.
- *Variant-axis extension or distinct operator?* — **Variant-axis extension** on the
  **existing** weight-matrix hook axis (`gram.md` variant axis 1). NOT a new operator.
- *Does `gram.md:197-202` `B`-hook already cover it?* — **Yes, semantically** — the `XᴴBX`
  form is exactly this. The only deficiency is **witness coverage**: that axis currently
  cites no concrete Palace site (NLEPS uses the canonical hook; the coverage caveat
  `gram.md:266-281` explicitly notes the *unweighted* `XᴴX` build has exactly one site and
  the weighted form none). These two solver sites are the first witnesses of the `B`-weighted
  axis. A small variant-axis-**witness** addition is warranted (not a new axis row — the axis
  exists).

## Recommendation
**Land the small clean variant-axis-witness extension to `book/src/L2/gram.md`** (proposed-changes
block below). This is the "advance a layer when cleanly describable in existing vocabulary"
move: the solver reduction needs no new spine vocabulary, so the spine advances by recording
the two first witnesses of the already-documented `B`-weighted axis and noting the
single-set/symmetry-exploited specialization they exhibit. It also tightens the coverage
caveat (the weighted form now HAS Palace witnesses).

Do **not** dispatch a harvester for a new operator — there is none. The downstream
capacitance/inductance post-processing (the `/Vᵢ²`, `/(IᵢIⱼ)` scaling, `Cm`/`Mm` sign-remix,
in-place invert) is a separate *solver-postprocess-reduction* description that **consumes**
`gram`; if the planner wants that captured, it is a distinct future dispatch (a thin
solver-postprocess entry or an L2 note), NOT a modification of `gram`. Recorded as an OQ below.

## Proposed changes

```proposed-changes
FILE: book/src/L2/gram.md

# Edit 1 — add the two solver witnesses + single-set/symmetry-exploited note to the
# `dot` hook variant axis (the existing `B`-weighted member). Replaces the axis-1 bullet
# body at gram.md:197-202.

OLD:
1. **`dot` hook** ∈ {`canonical Hermitian ⟨·,·⟩`, `B-weighted`} — the same hook axis the sibling
   [`orthogonalize`](./orthogonalize.md) carries (`orthogonalize.md`:67-71). The canonical
   Hermitian hook gives `G = XᴴX`; the `B`-weighted hook (`inner_product_M`) gives the weighted
   Gram `G = XᴴBX` (the mass-matrix / SPD-weighted overlap used by Rayleigh-Ritz / Galerkin
   projection). NLEPS uses the canonical hook (`linalg::Dot`, `palace/linalg/nleps.cpp:529`).
   Orthogonal to the others; conjugation lives entirely in the hook.

NEW:
1. **`dot` hook** ∈ {`canonical Hermitian ⟨·,·⟩`, `B-weighted`} — the same hook axis the sibling
   [`orthogonalize`](./orthogonalize.md) carries (`orthogonalize.md`:67-71). The canonical
   Hermitian hook gives `G = XᴴX`; the `B`-weighted hook (`inner_product_M`) gives the weighted
   Gram `G = XᴴBX` (the mass-matrix / SPD-weighted overlap used by Rayleigh-Ritz / Galerkin
   projection). NLEPS uses the canonical hook (`linalg::Dot`, `palace/linalg/nleps.cpp:529`).
   Orthogonal to the others; conjugation lives entirely in the hook. **The `B`-weighted member
   has two concrete Palace witnesses** — the electrostatic capacitance and magnetostatic
   inductance energy reductions, each an all-pairs weighted Gram `G[i,j] = Xⱼᴴ K Xᵢ` over a
   small per-terminal field-solution set `X` with `K` an **assembled FE mass matrix** (the
   SPD instance of the `B`-weight): the capacitance build
   `C(i,j) = linalg::Dot(V[j], M_elec·V[i]) = V[j]ᴴ M_elec V[i]`
   (`palace/drivers/electrostaticsolver.cpp:111-137`, `M_elec` = ε-weighted
   `VectorFEMassIntegrator`, `palace/models/domainpostoperator.cpp:30-41`), and the inductance
   build `M(i,j) = A[j]ᴴ M_mag A[i]` (`palace/drivers/magnetostaticsolver.cpp:110-152`,
   `M_mag` = μ⁻¹-weighted mass integrator, `palace/models/domainpostoperator.cpp:43-66`). Both
   are the **single-set `gram dot X`** form (axis 2) and **exploit Hermitian symmetry in the
   lowering** (compute the upper triangle `j = i+1..`, copy the lower —
   `electrostaticsolver.cpp:131-137`, `magnetostaticsolver.cpp:144-150`; the transparent
   perf-trick non-axis below, here actually taken, unlike NLEPS's full-`k²` build at
   `nleps.cpp:525-531`). The energy-formulation post-Gram cell scaling (`/Vᵢ²` with `Vᵢ≡1`;
   `/(IᵢIⱼ)`) and the `Cm`/`Mm` capacitance/inductance sign-remix + final in-place invert are
   **downstream consumers** of this weighted Gram, not part of the fold (the consumer-vs-
   constituent split, as for `deflate`).

# Edit 2 — relax the coverage caveat's "weighted form has no Palace witness" implication.
# Append a sentence to the coverage-caveat blockquote (after the existing text ending
# "...minimality index 1) — the standard-scheme anchor for the oblique-Galerkin deflation
# Gram." is in Evidence; the caveat blockquote is gram.md:266-281). Insert before the final
# "**Promotion of the caveat to closed**..." sentence.

OLD:
> single-algorithm concentration is the same posture as `inner_product`'s `tdot`-member coverage
> caveat — recorded at the operator's coverage granularity, not a firmness gate. **Promotion of

NEW:
> single-algorithm concentration is the same posture as `inner_product`'s `tdot`-member coverage
> caveat — recorded at the operator's coverage granularity, not a firmness gate. The caveat scopes
> the **unweighted `XᴴX`** build (one site, `nleps.cpp:524-531`); the **`B`-weighted `XᴴKX`**
> member by contrast now has **two** concrete witnesses (the capacitance/inductance energy
> reductions, variant-axis 1 above), so the weighted axis is no longer witness-less. **Promotion of

# Edit 3 — add the two witness sites to the Evidence list (append after the
# romoperator.cpp:757-765 non-instance bullet, gram.md:324-328).

OLD:
- `palace/models/romoperator.cpp:757-765` — the ROM small-dense solves `RHSr =
  Ar.ldlt().solve(RHSr)` / `Ar.selfadjointView<...>().ldlt().solve(...)` /
  `Ar.fullPivHouseholderQr().solve(...)`: a *non-instance* — small-dense solve on a reduced
  operator `Ar`, NOT an explicit `XᴴX` Gram build (the coverage caveat's "no second Gram-build
  site" evidence). **Self-verified.**

NEW:
- `palace/models/romoperator.cpp:757-765` — the ROM small-dense solves `RHSr =
  Ar.ldlt().solve(RHSr)` / `Ar.selfadjointView<...>().ldlt().solve(...)` /
  `Ar.fullPivHouseholderQr().solve(...)`: a *non-instance* — small-dense solve on a reduced
  operator `Ar`, NOT an explicit `XᴴX` Gram build (the coverage caveat's "no second Gram-build
  site" evidence). **Self-verified.**
- `palace/drivers/electrostaticsolver.cpp:111-137` — **first `B`-weighted `gram` witness
  (capacitance).** The double-loop `C(i,j) = linalg::Dot(V[j], D_gf)` with `D_gf = M_elec·V[i]`
  pinned once per outer `i` (`:118`), inner sweep `:124-130`, symmetry copy `:131-137`. Cell
  `C(i,j) = V[j]ᴴ M_elec V[i] = inner_product_M(V[j], M_elec, V[i])` — the single-set weighted
  Gram. Palace's own comment names the shape: `// (Vⱼᵀ K Vᵢ)` (`:122`). Self-verified via
  `read_range`.
- `palace/drivers/magnetostaticsolver.cpp:110-152` — **second `B`-weighted `gram` witness
  (inductance).** Structurally identical: `M(i,j) = linalg::Dot(A[j], H_gf)/(Iᵢ Iⱼ)` with
  `H_gf = M_mag·A[i]` (`:129`), inner sweep `:135-141`, symmetry copy `:144-150`. Cell
  `M(i,j) = A[j]ᴴ M_mag A[i]` (pre-`/(IᵢIⱼ)`) `= inner_product_M(A[j], M_mag, A[i])`. Palace
  comment `// (Aⱼᵀ K Aᵢ)` (`:134`). Self-verified.
- `palace/models/domainpostoperator.cpp:30-66` — the weight matrices' construction: `M_elec`
  = `BilinearForm + VectorFEMassIntegrator(ε)` `PartialAssemble()` (`:38-39`); `M_mag` =
  μ⁻¹-weighted mass integrator `PartialAssemble()` (`:53-64`). Establishes `K` is an assembled
  SPD FE mass matrix — the concrete `B`-weight. Self-verified.
```

## Supporting evidence

Book entries (read this invocation):
- `book/src/L2/gram.md` (full) — the firm all-pairs fold; variant-axis 1 `dot` hook
  ∈ {Hermitian, B-weighted} at `:197-202`; the `XᴴBX` weighted form `:200`; pinned
  arg-1-conjugated convention `:73-85`; symmetry-exploitation transparent non-axis
  `:180-182,213`; single-set vs cross-Gram axis 2 `:204-207`; consumer-vs-constituent split
  (deflate) `:236-241`; coverage caveat `:266-281` ("weighted form, none" — the gap these
  witnesses fill).
- `book/src/L2/inner_product.md` — the weighted member `inner_product_M x M y = inner_product
  (apply_linop M x) y` `:129-133,169`; M-weighted leaf `bilinear-form` `:36,80,178-180`;
  arg-1 (M-applied) conjugation `book/src/L2/inner_product.md:74-80`.

Palace source (`read_range`-verified, paths relative to `reference/`):
- `palace/drivers/electrostaticsolver.cpp:111-137` — capacitance reduction (the witness).
- `palace/drivers/magnetostaticsolver.cpp:110-152` — inductance reduction (the witness).
- `palace/models/domainpostoperator.cpp:28-66` — `M_elec`/`M_mag` mass-matrix construction
  (the SPD `K`/`B` weight).
- `palace/linalg/nleps.cpp:524-531` — the existing canonical-hook `gram` witness (contrast:
  full-`k²`, unweighted).

## Open questions / caveats

1. **Solver-postprocess consumer is uncaptured (NOT a `gram` concern).** The energy-formulation
   post-Gram steps — cell scaling `/Vᵢ²` (`Vᵢ≡1`) and `/(IᵢIⱼ)`, the `Cm`/`Mm`
   off-diagonal-sign Maxwell-capacitance remix (`electrostaticsolver.cpp:127-129`;
   `magnetostaticsolver.cpp:139-141`), and the final in-place `C.Invert()`/`M.Invert()`
   (`:138-139`/`:151-152`) — together form a **small-dense capacitance/inductance reduction**
   that *consumes* the weighted Gram. Worth a future thin entry or note (a
   `terminal-reduction` / `capacitance-matrix` L2 consumer description), but it is a
   **distinct dispatch**, not part of `gram`. Surfaced for the planner; do NOT fold into
   `gram`. (If the planner judges it too thin / too solver-specific to lift, defer — per the
   redirect, solvers advance the spine only when cleanly describable; this post-step is
   arguably solver-domain bookkeeping, not shared spine vocabulary.)

2. **`linalg::Dot<Vector>` here is the REAL path** (`V_gf`/`A_gf` are `.Real()` grid
   functions — `electrostaticsolver.cpp:115`, `magnetostaticsolver.cpp:127`), so the
   conjugation convention is vacuous (`Vᴴ = Vᵀ`, matching Palace's `// (Vⱼᵀ K Vᵢ)` literal
   transpose notation). The `gram` arg-1-conjugated convention still applies *formally*
   (column `j` is the conjugated operand) and is convention-invariant here. No conflict; noted
   so a later complex-field driven/transient analog (where the convention bites) is not
   surprised. The weighted member's own conjugation lands on the M-applied operand
   (`book/src/L2/inner_product.md:74-80`, `(Mx)ᴴ y`); since `K` is symmetric-real here this is invisible.

3. **`read_range`-verification scope.** I `read_range`-verified the two solver windows and the
   weight-matrix construction this invocation; I did NOT re-run `tools/citecheck`. The
   integrator's per-report safety-net should bounds-check the four new Palace citations before
   landing Edit 3 (standard).

4. **Cross-set (`gram2`) is NOT exercised here.** Both witnesses are single-set `gram dot X`
   (axis 2's single-set member); they do not witness the cross-Gram `gram2 dot X Y`. So this
   landing strengthens the `B`-weighted axis (axis 1) and the single-set member (axis 2), but
   not the cross member. No change implied for the cross-Gram coverage.
