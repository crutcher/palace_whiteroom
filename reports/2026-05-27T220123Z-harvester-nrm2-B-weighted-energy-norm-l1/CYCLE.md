---
agent: harvester
invoked_at: 2026-05-27T220123Z
scope: L1 operator: nrm2_B-weighted-energy-norm (rough-in)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied via integrator-per-report pass 5 of cycle-010 (wave-2 #5). **Duplicate-resolution merge-and-rename verdict** — verified duplicate of wave-1 sibling pass 3 (matrix-weighted-norm) via 6 identity claims (same L0 anchor / closed-form / SPD precondition / dependencies / variant axis / callsite cohort). **No `book/` mutation**. Cycle-003 OQ `nrm2-B-weighted-energy-norm-harvest` partially-answered (`open` → `partially-answered`; `last_revisited: cycle-010`); priority #13 close routed via new OQ `priority-13-now-landed-as-matrix-weighted-norm` (status `routing`) per write-authority partition. **Friction-pattern signal at recurrence-1**: planner-side deduplication-by-L0-anchor; forwarded to cycle-012 meta-phase batch.
verdict: duplicate-of-sibling-wave-1-merge-and-rename
inputs:
  - reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md (wave-1 sibling — authoritative landing)
  - scaffolding/priorities.md #13 (nrm2_B-weighted-energy-norm-L1) and #17 (lower-layer-shared-vocabulary-priority; L1 cohort growth bullet)
  - scaffolding/open-questions.md slug `nrm2-B-weighted-energy-norm-harvest` (filed from `nrm2.md` boundary statement)
  - scaffolding/open-questions.md slug `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` (filed from L0 `linalg-operator-file` chapter)
  - book/src/L0/linalg-operator-file.md (lines 30-33, 73, 88 — L0 anchor naming `nrm2_weighted`)
  - book/src/L1/nrm2.md (line 13 — sibling-boundary statement referring to the energy-norm overload)
  - book/src/L1/index.md (line 51 — "Queued" line for `nrm2_B :: (x, B) → √(xᴴ B x)`)
  - palace/linalg/operator.hpp:372-374 (L0 declaration; SPD comment)
  - palace/linalg/operator.cpp:599-619 (L0 implementation; two element-type specializations)
---

# CYCLE: Resolve `nrm2_B-weighted-energy-norm` at L1 as duplicate of wave-1 `matrix-weighted-norm`

## Summary

**Verdict: case (c) merge-and-rename.** Per the planner's coordination warning, I read the wave-1 sibling dispatch report (`reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md`) and audited it against the planner-supplied target `nrm2_B-weighted-energy-norm`. The two dispatches name the **same L1 operator**:

- **Same L0 anchor**: both target `palace::linalg::Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx)` declared at `palace/linalg/operator.hpp:372-374`, implemented at `palace/linalg/operator.cpp:599-619` (two template specializations for `VecType ∈ {Vector, ComplexVector}`). There is exactly one such overload in the L0 surface (`grep -n "Norml2" palace/linalg/operator.hpp` returns line 374 only).
- **Same closed-form semantics**: `‖x‖_B = √(xᴴ B x)` for SPD `B`.
- **Same dependencies**: `dot` (firm cycle-002) + `apply_linop` (firm cycle-005).
- **Same SPD applicability condition** (with SPSD-seminorm caveat).
- **Same element-type variant axis** (real / complex collapses to one L1 operator).
- **Same algebraic-law set** (closed-form `√(xᴴ B x)` underwrites all 12 norm-induced-by-inner-product laws plus identity-collapse to `nrm2`).
- **Same M-orthonormalisation callsite cohort**: all three eigensolver backends (ARPACK / SLEPc / NLEPS) use this overload in `GetEigenvectorNorm` for the generalised eigenvalue problem.

The cycle-008 OQ list filed the target under **two distinct slugs** because the obstruction was observed at two distinct sites:

1. `nrm2-B-weighted-energy-norm-harvest` — filed from `book/src/L1/nrm2.md`'s sibling-boundary statement ("The B-weighted overload ... is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`"; cycle-003 era, line 13 of the firm entry).
2. `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` — filed from `book/src/L0/linalg-operator-file.md`'s enumeration of unharvested `linalg::` free functions (cycle-008 layer-intro-author dispatch).

The cycle-009 meta-phase carried both slugs forward into cycle-010 priorities #13 and #17 without recognising the duplication. **Both OQs name the same operator.** The wave-1 dispatch landed it as `matrix-weighted-norm`; this dispatch (wave-2 #5) does NOT produce a competing L1 entry under the `nrm2_B-weighted-energy-norm` slug.

## Proposed changes

This dispatch produces **no new L1 file** and **no `book/` mutations**. The only proposed changes are append-only OQ resolution notes for the integrator.

```edit:scaffolding/open-questions.md
[Resolve OQ `nrm2-B-weighted-energy-norm-harvest`]: mark as `partially-answered` (matching the wave-1 dispatch's planned resolution of `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`), with resolution note pointing to wave-1 landing `book/src/L1/matrix-weighted-norm.md` (rough-in, harvested cycle-010 wave-1). The energy-norm half is answered by the matrix-weighted-norm entry; the bilinear-form half is the remaining residual on the other OQ.

[Append new OQ entry (or merge into the existing `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` resolution)]:
  slug: nrm2-b-weighted-energy-norm-and-matrix-weighted-norm-duplicate-target
  filed_in_cycle: 010
  filed_by: harvester:2026-05-27T220123Z-harvester-nrm2-B-weighted-energy-norm-l1
  status: resolved
  resolution: |
    cycle-008 OQs `nrm2-B-weighted-energy-norm-harvest` (filed from nrm2.md boundary statement)
    and the energy-norm half of `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`
    (filed from linalg-operator-file L0 chapter) name the same operator at L1: the SPD
    operator-weighted Euclidean norm `‖x‖_B = √(xᴴ B x)` anchored at
    palace/linalg/operator.cpp:599-619.

    Both OQs were filed from distinct observation sites in different cycles, and the
    cycle-009 meta-phase promoted both to cycle-010 priorities (#13 and the L1 cohort
    growth bullet of #17). The cycle-010 wave-1 harvester dispatch landed the operator
    as `book/src/L1/matrix-weighted-norm.md` (rough-in). Wave-2 dispatch #5 verified
    the duplication.

    Naming axis resolution: the canonical L1 slug is `matrix-weighted-norm`. The
    candidate names `nrm2_B`, `nrm2_weighted`, `nrm2-B-weighted-energy-norm`,
    `energy-norm` are NOT separate operators — they are aliases / earlier candidate
    slugs for the same target. The L1 index line and L0 chapter prose may retain the
    `nrm2_B` / `nrm2_weighted` text as informational variants; an editorial sweep can
    align them (see new OQ `matrix-weighted-norm-naming-sweep` proposed by wave-1).
```

```edit:scaffolding/priorities.md
[Resolve priority #13]: mark `nrm2_B-weighted-energy-norm-L1` as `landed-as-matrix-weighted-norm` (cycle-010 wave-1 dispatch; rough-in). The priority is closed by the wave-1 dispatch; no separate wave-2 dispatch product is needed. Move to "Recently landed" section under cycle-010 entries with cross-reference to the wave-1 dispatch slug `2026-05-27T215334Z-harvester-matrix-weighted-norm-l1`.
```

No edits to `book/`. No edits to `book/src/L1/matrix-weighted-norm.md` (which is being authored by the wave-1 sibling — this dispatch must not race with it). No edits to `book/src/L1/index.md`, `book/src/SUMMARY.md`, or any L0 chapter — those are wave-1's scope.

## Operator content

Not authored in this dispatch. See `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` for the full operator content (signature, semantics, 12 algebraic laws + 5 non-laws, applicability conditions, composition note, dependencies, variant axes, status rationale, L1 vs L0 distinction, 17 evidence citations).

## Supporting evidence

The verdict-of-duplication rests on the following surface-level identity claims (each pinned to L0 source or to the wave-1 sibling report):

- **L0 declaration uniqueness**: `palace/linalg/operator.hpp:374` declares one `Norml2` template with the `(comm, x, B, Bx)` signature (`double Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx);`). The accompanying SPD comment is at line 372 ("Calculate the vector norm with respect to an SPD matrix B."). No second overload exists.
- **L0 implementation uniqueness**: `palace/linalg/operator.cpp:599-619` provides exactly two specializations of the same template (`Vector` and `ComplexVector`), both implementing the closed-form `√(xᴴ B x)` via `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)`. There is no second L0 entry point under any other name (`SpectralNorm` at `operator.hpp:398-401` is power-iteration, NOT the energy norm — separate operator candidate `power_iterate` already noted in OQ ledger).
- **Wave-1 sibling's claim**: the wave-1 dispatch report (lines 49-193 of its CYCLE.md) defines `matrix-weighted-norm` with signature `matrix_weighted_norm :: (x: Tensor[N], B: LinearOperator[N, N]) -> Scalar` and semantics `matrix_weighted_norm(x, B) = √(xᴴ B x)` for SPD `B`. The closed-form, applicability condition, dependencies, evidence pins, and callsite cohort match what `nrm2_B-weighted-energy-norm` would target.
- **`book/src/L1/index.md` line 51**: the "Queued" line is `nrm2_B :: (x, B) → √(xᴴ B x)` — pointing at the same closed-form. The slug `nrm2_B` is a candidate-name from the cycle-003-era `nrm2` harvester's boundary statement and is not anchored to a distinct operator.
- **`book/src/L1/nrm2.md` line 13**: the sibling-boundary statement says "The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator. ... It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`." Again — same L0 anchor, same closed-form, same dependencies. The "forthcoming" promise is fulfilled by the wave-1 `matrix-weighted-norm` landing.
- **`scaffolding/priorities.md` #13** literally reads: "depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest`." Identical dependency set to wave-1.
- **`scaffolding/priorities.md` #17 L1 cohort growth bullet** literally reads: "`matrix-weighted-norm` + `bilinear-form` L1 rough-ins (cycle-008 OQ carried forward)." Same operator, different slug.

The two OQ slugs were filed against the same operator from two different observation sites across two different cycles. The cycle-009 meta-phase's promotion of both to cycle-010 was an overcounting, not a discovery of two distinct targets.

## Open questions / caveats

1. **Naming-axis residual**. The L1 index `Queued` line (line 51) still uses `nrm2_B`; the L0 chapter `linalg-operator-file.md` prose (lines 30-33, 73, 88) still uses `nrm2_weighted`. Wave-1 already proposed updating the `Queued` line (to remove `nrm2_B` and add the bilinear-form residual). The L0 chapter's `nrm2_weighted` prose is editorial-sweep territory, already filed by wave-1 as new OQ `matrix-weighted-norm-naming-sweep`. **No new OQ needed from this dispatch.**

2. **Coordination with wave-1**. Wave-1's dispatch (`2026-05-27T215334Z-harvester-matrix-weighted-norm-l1`) is the authoritative cycle-010 landing for this operator. Wave-2 #5's role under the planner's case-(a)/(c) recommendation is to confirm the duplication and avoid producing a competing entry. The integrator should process wave-1 first (it has the proposed-changes block for the L1 file, the L1 index, and SUMMARY); wave-2 #5 contributes only OQ-resolution and priority-resolution notes that should be applied after the wave-1 landing.

3. **Should the integrator file a friction-ledger entry for OQ-duplicate-detection-across-cycles?** The pattern observed here is: cycle-N OQ filed at site A; cycle-N+5 OQ filed at site B; both name the same operator; cycle-N+6 meta-phase promotes both to next-cycle priorities without recognising the duplication; cycle-N+7 wave dispatches both, and the second dispatch discovers the overlap. Not a friction-ledger entry yet — recurrence-1; watch for repeat. Possible meta-phase improvement: deduplicate-by-L0-anchor in the OQ ledger as part of meta-phase aggregation. **Routed as a watch-item for cycle-012 meta-phase**, not a friction-ledger entry from this dispatch.

4. **The `apply_linop` evidence dependency check** is implicit in the verdict. The wave-1 dispatch cites `apply_linop` (firm cycle-005) as the L1 dependency for the `B · x` step. Priority #13 also cites `apply_linop`. The `nrm2.md` boundary statement also cites `apply_linop` ("the operator-application primitive `apply_linop`"). All three converge — no separate `apply` candidate-name to disambiguate.

5. **`bilinear-form` sibling is NOT a duplicate**. The cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` pairs two distinct operators: (a) the energy norm `‖x‖_B = √(xᴴ B x)` (this dispatch's resolved target) and (b) the operator-induced bilinear form `⟨x, y⟩_A = yᴴ A x` at L0 anchor `palace/linalg/operator.cpp:621-639` (`linalg::Dot(comm, x, A, y)`). These are **separate L0 declarations** (different L0 lines, different L0 signatures, different applicability conditions — `bilinear-form` does NOT require SPD `A`, accepts non-Hermitian, no outer `sqrt`). Wave-1 noted the bilinear-form half remains residual; this dispatch agrees — the OQ resolution should mark `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` as `partially-answered` with the bilinear-form half preserved.

6. **Does the `power_iterate` candidate-operator (SpectralNorm, `palace/linalg/operator.hpp:398-401`) belong on the same OQ?** No — `SpectralNorm` is power iteration with configurable tolerance, returning the dominant singular value. Distinct operator with distinct semantics; the cycle-008 OQ correctly named it as a separate rough-in target. Not in scope for this dispatch.

7. **Potential future planner enhancement**. When the cycle-planner promotes multi-target OQs to cycle priorities, it could check whether each target's L0 anchor (file + line range) is unique across the active priority list. The duplication here was preventable by such a check. Watch-item for cycle-012 meta-phase planner-role refinement.
