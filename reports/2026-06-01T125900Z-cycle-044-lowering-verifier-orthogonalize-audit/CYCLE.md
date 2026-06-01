---
agent: lowering-verifier
invoked_at: 2026-06-01T125900Z
scope: L3 operator audit — orthogonalize (partial-obstruction, c040 deferred verified_against audit)
status: pending
inputs:
  - book/src/L3/orthogonalize.md
  - palace/linalg/orthog.hpp:18-23,41-53,57-89 (MGS / CGS / CGS2 bodies + header contract)
  - palace/linalg/iterative.cpp:308-325,630-632,809-811 (OrthogonalizeIteration dispatch + GMRES/FGMRES consumers)
  - test/unit/test-orthog.cpp:99-120,123-160,234 (empty-prefix, parametric real, complex)
  - book/src/concepts/sequential-obstruction.md:22,37-48 (MGS-as-sequential-obstruction)
  - book/src/concepts/variant-absorption.md:131 (gs_orthog absorption)
  - book/src/L2/orthogonalize.md, book/src/L1/orthogonalize.md (firm sibling forecasts)
integrated_at: 2026-06-01T150500Z
integration_commit: d88f7b6
integration_notes: "cycle-044 batch integration; D4 lowering-verifier (deferred-from-c040 audit) — appended 24-row verified_against block to L3/orthogonalize.md (all supports), status stays partial-obstruction NO FLIP; re-pointed §Dependencies / §L3-vs-L2-distinction / lowers_to frontmatter onto the live ../L3-L2/orthogonalize-variant-split.md link for the substantive loop-rotation half (D3's target landed first, links resolved on apply); retroactive per-slice=1 (global=1, under ≥4 block); applied clean; see reports/2026-06-01T150500Z-integrator-finalize-cycle-44/CYCLE.md + cycle-044 STAGING row 3."
---

# CYCLE: Audit orthogonalize (L3 partial-obstruction)

## Summary

Audited the firm L3 `orthogonalize` entry (`book/src/L3/orthogonalize.md`, the third
`partial-obstruction` L3 row, cycle-040) against its cited L0 evidence and its firm L1/L2/concept
cross-references — the `verified_against:` audit deferred since c040. **Top-level verdict:
fully-supported.** Every load-bearing claim was independently confirmed against the on-disk
`reference/` source (NOT the codemap, per the `codemap-read-range-plus-one-drift` guard) and
cross-checked with `tools/citecheck/citecheck.py --anchor`. All 24 audited anchors return
`supports` with **zero drift** — `citecheck` reports `OK` on every bounds check and every anchor
probe. The variant-split structural claim (MGS = sequential-obstruction; CGS/CGS2 lift) is
faithful to the source: the MGS `j`-loop interleaves `dot`/`GlobalSum`/`w.Add` in the *same*
iteration (`orthog.hpp:49/:50/:51`, the `w.Add` feeding the next `dot`), while CGS takes all `m`
dots against the *original* `w` before a single batched `GlobalSum` (`:66-70`), and the CGS2
`refine` branch (`:75-88`) is the non-fusible second pass. The `partial-obstruction` status is the
honest verdict — **no contradiction found; status unchanged.** I propose (1) the fenced
`verified_against:` YAML append (24 rows) and (2) the §Downward / §L3-vs-L2 reconciliation pointing
at D3's new substantive `L3-L2/orthogonalize-variant-split.md` theme (D3 flagged the now-stale
"no L3-L2 theme file" prose), keeping the per-step body-identity in-line note accurate.

## Per-citation audit

### L0 — orthog.hpp (the variant bodies; read in full, 93 lines)

- **Citation**: `palace/linalg/orthog.hpp:18-23`
  - **Theme claim**: header scope contract — orthogonalises against a basis set using modified or
    classical Gram-Schmidt; "Assumes that the input vectors are normalized, but does not normalize
    the output vectors!" (`:22`).
  - **Found**: lines 18-23 are exactly that comment block; `:22` is verbatim the no-normalize
    sentence. `citecheck --anchor 'does not normalize'` → `OK` at `:22`.
  - **Verdict**: supports.
  - **Notes**: this is the load-bearing boundary justifying that the `{ residual, coeffs }` record
    stops at the un-normalised residual (`nrm2`/`scal` are caller's). Confirmed downstream at the
    consumer sites below.

- **Citation**: `palace/linalg/orthog.hpp:41-53` (and the loop body `:46-52`)
  - **Theme claim**: `OrthogonalizeColumnMGS`; the per-`j` loop
    `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])` with `dot` and
    `w.Add` in the **same** `j`-loop iteration, the `w.Add` feeding the next iteration's `dot` — the
    MGS sequential-obstruction witness (`[dot, axpy] × m`, `m` reductions of size 1).
  - **Found**: function opens `:41`, `for` opens `:46`, `H[j] = dot_op(w, V[j])` at `:49`,
    `Mpi::GlobalSum(1, &H[j], comm)` at `:50`, `w.Add(-H[j], V[j])` at `:51`, loop closes `:52`,
    function closes `:53`. The `w.Add` mutates `w` in place each iteration; the next iteration's
    `dot_op(w, V[j])` reads the mutated `w`. Exactly the loop-carried candidate the entry asserts.
  - **Verdict**: supports.
  - **Notes**: the entry cites the loop as `:46-52` (the `for` span) and the dot is at `:49`. Both
    are internally consistent; the `:46-52` range correctly bounds the loop. No drift.

- **Citation**: `palace/linalg/orthog.hpp:57-89` (CGS body, with sub-anchors `:62-64`, `:66-69`,
  `:70`, `:71-74`, `:75-88`)
  - **Theme claim**: `OrthogonalizeColumnCGS`; empty-basis early return (`m == 0`, `:62-64`); `m`
    batched local dots into `H` against the **original** `w` (`:66-69`); single `Mpi::GlobalSum(m,
    H, comm)` (`:70`); `m` batched `w.Add`s (`:71-74`); `refine` branch (`:75-88`) accumulating
    `H[j] += dH[j]` (the CGS2 `[CGS] × 2` second pass). Dots-against-original-`w` is the witness
    that CGS/CGS2 lift (basis index is a reduction axis).
  - **Found**: function opens `:57`; `if (m == 0) { return; }` at `:62-65` (the entry's `:62-64`
    captures the `if`+`return` lines; the closing `}` is at `:65`, in-bounds of the cited body —
    minor: the early-return *statement* is `:62-64`, accurate as the witness); the first dot loop
    `for ... H[j] = dot_op(w, V[j]);` at `:66-69` reads the **un-mutated** `w` (no `w.Add` inside
    this loop — the structural difference from MGS); `Mpi::GlobalSum(m, H, comm)` at `:70`; the
    `w.Add` loop at `:71-74`; the `if (refine)` branch `:75-88` computes `dH` against the
    once-projected `w` (`:80`), batched-sums (`:82`), then `H[j] += dH[j]; w.Add(-dH[j], V[j])`
    (`:85-86`). All confirmed.
  - **Verdict**: supports.
  - **Notes**: the load-bearing structural distinction — CGS dots read the original `w`, MGS dots
    read the progressively-subtracted `w` — is exactly as the entry claims. This is the source root
    of the variant-split lift verdict.

### L0 — iterative.cpp (dispatch + consumers)

- **Citation**: `palace/linalg/iterative.cpp:308-325` (and `:313-323`, `:321-322`)
  - **Theme claim**: `OrthogonalizeIteration` runtime variant dispatch — `switch (type)` over
    `MGS/CGS/CGS2` (`:313-323`), `CGS2 = OrthogonalizeColumnCGS(..., true)` (`:321-322`); variant
    bound at construction, dispatched once, against leading `j + 1` columns.
  - **Found**: function `:308-325`; comment "Orthogonalize w against the leading j + 1 columns"
    `:312`; `switch (type)` `:313`; `case MGS` → `OrthogonalizeColumnMGS(..., j + 1)` `:315-317`;
    `case CGS` `:318-320`; `case CGS2` → `OrthogonalizeColumnCGS(..., j + 1, true)` `:321-322`.
    The `true` is the `refine` flag — confirming CGS2 = refined CGS.
  - **Verdict**: supports.
  - **Notes**: the L3 `case op.variant` rendering maps 1:1 to this `switch`. The variant is
    inspected once per call (per column), but the *variant choice* is solver-construction-bound
    (`gs_orthog` field) — the entry's "inspected exactly once at dispatch, never re-branched per
    column within the orthogonalization body" is accurate (the body of each Column* function does
    not re-branch on variant).

- **Citation**: `palace/linalg/iterative.cpp:630-632` (GMRES) and `:809-811` (FGMRES)
  - **Theme claim**: Arnoldi consumer — `OrthogonalizeIteration(...)` immediately followed by
    `Norml2` (sub-diagonal) and `scal` (normalisation), confirming normalisation is the caller's,
    outside the operator.
  - **Found**: GMRES — `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` `:630`;
    `Hj[j + 1] = linalg::Norml2(comm, w)` `:631`; `w *= 1.0 / Hj[j + 1]` `:632`. FGMRES —
    identical at `:809/:810/:811`. The `w *= 1.0/...` is the scalar-multiply (`scal`) the prose
    names.
  - **Verdict**: supports.
  - **Notes**: confirms the no-output-normalisation boundary (`orthog.hpp:22`) is honoured at both
    consumer sites — the caller does the `Norml2` + `scal`. `nrm2`/`scal` are correctly excluded
    from the operator's dependency set.

### L0-equivalent — test-orthog.cpp

- **Citation**: `test/unit/test-orthog.cpp:99-120`
  - **Theme claim**: empty-prefix edge — all three variants leave `w` unchanged (`m = 0` identity,
    law 3).
  - **Found**: `TEST_CASE("OrthogonalizeColumn - Real Empty")` `:99`; all three variants `GENERATE`d
    `:101-103`; `orthogonalize_fn(..., V, w, H, 0)` with empty `V` `:117`; `CHECK_THAT(w,
    RangeEquals(w_orig))` `:120`.
  - **Verdict**: supports.

- **Citation**: `test/unit/test-orthog.cpp:123-160`
  - **Theme claim**: parametric real — all three variants zero the per-rank component and pass
    `⟨residual, V[i]⟩ ≈ 0` to `1e-12` (law 1, substitutability witness); assertion `CHECK_THAT(dot,
    WithinAbs(0.0, 1e-12))` at line 158 inside the check loop (leading comment `:154`, `for` opens
    `:155`, body `:155-159`); TEST_CASE closes 160.
  - **Found**: `TEST_CASE(... Real 1)` `:123`; three variants `:125-127`; `CHECK_THAT(w[mpi_rank],
    WithinAbs(0.0, 1e-12))` (per-rank zero) `:152`; comment "Check full orthogonalization" `:154`;
    `for (int i = 0; i < mpi_size; i++)` `:155`; `auto dot = linalg::Dot(...)` `:157`;
    `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` `:158`; loop closes `:159`; TEST_CASE closes `:160`.
    `citecheck --anchor 'WithinAbs(0.0, 1e-12)'` → `OK` at `:158`.
  - **Verdict**: supports.
  - **Notes**: the entry's pinpoint description of the assertion location (`:158`) and the loop
    structure (`:154`/`:155`/`:155-159`) is exactly correct — a notably precise prior anchor.

- **Citation**: `test/unit/test-orthog.cpp:234`
  - **Theme claim**: complex parametrisation (element-type axis).
  - **Found**: `TEST_CASE("OrthogonalizeColumn Parameterized - Complex 1")` `:234`, three variants
    `:236-238`. `citecheck --anchor 'Complex 1'` → `OK` at `:234`.
  - **Verdict**: supports.

### Intra-book — concept + sibling cross-references

- **Citation**: `book/src/concepts/sequential-obstruction.md:37-48`
  - **Theme claim**: canonical MGS-as-sequential-obstruction structural argument; the
    `(I − V[m-1] V[m-1]ᴴ) ⋯ (I − V[0] V[0]ᴴ) w` projector composition.
  - **Found**: §"Example: MGS as sequential-obstruction" `:37`; CGS bullet `:41`
    (`H = Vᴴ w` then `w ← w − V H`, parallel); MGS bullet `:42` (the exact projector composition
    `(I − V[m−1]...) ⋯ (I − V[0]...) w`, left-to-right serial); "MGS therefore has no global
    tensor-field form" `:44`. Matches the entry verbatim in structure.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/sequential-obstruction.md:22`
  - **Theme claim**: MGS example classifying CGS as the parallel-reduction alternative exposed as
    the `gs_orthog` variant.
  - **Found**: `:22` — "CGS is the parallel-reduction alternative; the choice is exposed as the
    `gs_orthog` variant." Verbatim.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/variant-absorption.md:131` — supports (gs_orthog absorbed at all
  three levels under residual-axis disclosure; Householder scoped out). In-bounds, anchor consistent.
- **Citation**: `book/src/L2/orthogonalize.md:133-134` and `:290-292` — supports (the L2 forecast of
  the L3 MGS sequential-obstruction / CGS-CGS2-lift split, and the L2 reading as collective-shape
  residual axis + MGS column-order non-commutativity non-law). In-bounds.
- **Citation**: `book/src/L1/orthogonalize.md:200-203` — supports (the L1-leaf forecast that the MGS
  sequential-obstruction is an L3 property of the variant, not an L1 contract distinction).
  In-bounds.

## Applicability conditions

- **Condition**: input basis `V` is orthonormal (`⟨V[i], V[j]⟩ = δ_ij`); the operator does not
  enforce it.
  - **Verifiable**: yes — the L0 header (`orthog.hpp:18-23`) states the assumption ("Assumes that
    the input vectors are normalized"); neither `OrthogonalizeColumnMGS` nor `OrthogonalizeColumnCGS`
    contains an orthonormality check (read in full).
  - **Found counter-example?**: no.

- **Condition**: `m = 0` (empty basis) is the identity for every variant.
  - **Verifiable**: yes — CGS early-returns at `orthog.hpp:62-64`; MGS's `for` loop with `m = 0`
    executes zero iterations (trivially identity); test `:99-120` asserts `w` unchanged across all
    three variants.
  - **Found counter-example?**: no.

- **Condition**: normalisation is NOT part of the operator (caller does `nrm2` + `scal`).
  - **Verifiable**: yes — header `:22` + both consumer sites `:630-632`/`:809-811` perform the
    `Norml2`+`scal` *after* the call.
  - **Found counter-example?**: no.

- **Condition**: the variant is inspected once (no per-column re-branch); the lift verdict splits on
  `gs_orthog`.
  - **Verifiable**: yes — `OrthogonalizeIteration`'s `switch (type)` (`:313-323`) selects one
    Column* function; each Column* body is variant-free (no `switch`/`if` on variant inside).
  - **Found counter-example?**: no.

## Algebraic laws

- **Law 1 (Orthogonality, exact)**: `op.dot(residual, V[i]) = 0`. Holds — witnessed empirically
  across all three variants at `test-orthog.cpp:158` (`WithinAbs(0.0, 1e-12)`), under canonical and
  B-weighted `op.dot`. Source-consistent.
- **Law 2 (Loss-free decomposition)**: `w = residual + Σ coeffs[j]·V[j]` (exact, orthonormal V).
  Holds by construction of the projector composition — the `H[j]`/`w.Add` updates accumulate exactly
  this decomposition. Consistent with both bodies.
- **Law 3 (Empty-prefix identity)**: holds — `orthog.hpp:62-64` + test `:99-120`.
- **Law 4 (Variant agreement, exact)**: holds in exact arithmetic — MGS/CGS/CGS2 compute the same
  projection; diverge only in finite precision (correctly recorded as a non-law below).
- **Law 5 (Per-step body identity across L3↔L2↔L1)**: holds — the per-step `dot`+`axpy` body is
  whole-tensor by signature shape; the L0 `H[j] = dot_op(...)` / `w.Add(-H[j], V[j])` maps to the L2
  `project`/`subtract` stages. Body-level only; does NOT erase the MGS loop obstruction. Correct.
- **Law 6 (CGS/CGS2 global-lift)**: holds — the CGS body (`:66-74`) takes all dots against the
  original `w` then batches the subtraction; this is exactly `coeffs = Vᴴw`, `residual = w − V·coeffs`.
  The basis index is a reduction/broadcast axis. CGS2 = `[CGS] × 2` via the `refine` branch
  (`:75-88`). Source-confirmed.
- **Law 7 (dot-hook invariance)**: holds — `dot_op` is a template parameter (`InnerProductW`,
  default `IdentityInnerProduct`); the body shape and the MGS/CGS structural split are independent of
  the hook. The B-weighted hook is a closure substitution. Confirmed at `orthog.hpp:39-43,55-59`.

**Non-laws (all confirmed as genuine non-laws):**
- MGS loop lift to a single tensor-field op — **does NOT hold** (the `w.Add` at `:51` feeds the next
  `dot` at `:49`; genuinely serial in `j`). This is the source of the `partial-obstruction` status.
- Variant agreement in floating point — does not hold (load-bearing; the motivation for the variant
  axis). Inherited from L1/L2.
- Column-order commutativity under MGS — does not hold (the left-to-right projector composition does
  not commute; CGS/CGS2 are column-order-invariant up to reduction noise). Consistent with the
  source loop structure.
- Reduction-tree associativity (fp), stage-fusion across the CGS2 pass boundary, bit-level
  linearity/idempotence — all correctly recorded as non-laws; the CGS2 non-fusibility is confirmed
  at `:80` (the second-pass `dH` reads the once-projected `w`, not the original).

## Proposed changes

### Change 1 — append the fenced `verified_against:` YAML block

The block was parse-verified with `python3 -c "import yaml; yaml.safe_load(...)"` (24 rows, clean
parse). Every `note:` value's first non-whitespace character is a non-quote character (the
`codemap-read-range-plus-one-drift` and `verified-against-note-no-leading-quote-of-either-kind`
guards both satisfied). All anchors `citecheck`-confirmed `OK` against on-disk source.

```edit:book/src/L3/orthogonalize.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/orthog.hpp:18-23
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: header scope contract; modified-or-classical Gram-Schmidt against a basis set
  - citation: palace/linalg/orthog.hpp:22
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: the no-output-normalisation contract sentence -- citecheck anchor "does not normalize" OK at :22
  - citation: palace/linalg/orthog.hpp:41-53
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: OrthogonalizeColumnMGS; dot+GlobalSum+w.Add interleaved in the SAME j-loop iteration (:49/:50/:51) -- the MGS sequential-obstruction source witness
  - citation: palace/linalg/orthog.hpp:46-52
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: the MGS j-loop body; w.Add(:51) feeds the next iteration dot(:49) -- loop-carried candidate
  - citation: palace/linalg/orthog.hpp:57-89
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: OrthogonalizeColumnCGS; m dots-against-original-w then single GlobalSum then m w.Add -- the lifting half; refine branch is the CGS2 second pass
  - citation: palace/linalg/orthog.hpp:62-64
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: CGS empty-basis early return (m == 0) -- law 3 source
  - citation: palace/linalg/orthog.hpp:66-69
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: m batched local dots into H against the original w (not progressively-subtracted) -- the basis index is a reduction axis
  - citation: palace/linalg/orthog.hpp:70
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: single Mpi::GlobalSum(m, H, comm) -- one reduction of size m, the batched CGS reduction
  - citation: palace/linalg/orthog.hpp:71-74
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: m batched w.Add subtractions -- the w - V H matvec
  - citation: palace/linalg/orthog.hpp:75-88
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: CGS refine branch; dH against once-projected w then H[j] += dH[j] -- the CGS2 [CGS] x 2 non-fusible second pass
  - citation: palace/linalg/iterative.cpp:308-325
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: OrthogonalizeIteration dispatcher; orthogonalizes against leading j+1 columns
  - citation: palace/linalg/iterative.cpp:313-323
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: switch(type) over MGS/CGS/CGS2 -- the L3 case op.variant; inspected once at dispatch
  - citation: palace/linalg/iterative.cpp:321-322
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: CGS2 = OrthogonalizeColumnCGS(..., true) -- the refine=true CGS2 binding
  - citation: palace/linalg/iterative.cpp:630-632
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: GMRES consumer; OrthogonalizeIteration(:630) then Norml2(:631) then w *= 1/Hj (scal, :632) -- normalisation is the caller's, outside the operator
  - citation: palace/linalg/iterative.cpp:809-811
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: FGMRES consumer; identical OrthogonalizeIteration + Norml2 + scal sequence
  - citation: test/unit/test-orthog.cpp:99-120
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: empty-prefix edge; all three variants GENERATE'd, w unchanged (RangeEquals) at :120 -- law 3 empirical
  - citation: test/unit/test-orthog.cpp:123-160
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: parametric real; per-rank component zeroed (:152) and orthogonality loop (comment :154, for :155, body :155-159) asserting WithinAbs(0.0,1e-12) at :158 -- law 1 substitutability witness across MGS/CGS/CGS2
  - citation: test/unit/test-orthog.cpp:234
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: complex parametrisation TEST_CASE -- element-type axis coverage
  - citation: book/src/concepts/sequential-obstruction.md:37-48
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: canonical MGS-as-sequential-obstruction argument; the (I - V[m-1]...) ... (I - V[0]...) w projector composition matches the entry
  - citation: book/src/concepts/sequential-obstruction.md:22
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: MGS example classifying CGS as the parallel-reduction alternative exposed as the gs_orthog variant
  - citation: book/src/concepts/variant-absorption.md:131
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: gs_orthog axis absorbed at all three levels under residual-axis disclosure; Householder scoped out
  - citation: book/src/L2/orthogonalize.md:133-134
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: L2 forecast of the L3 MGS sequential-obstruction / CGS-CGS2-lift split
  - citation: book/src/L2/orthogonalize.md:290-292
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: L2 reading of the lift split as the collective-shape residual axis + MGS column-order non-commutativity non-law
  - citation: book/src/L1/orthogonalize.md:200-203
    verdict: supports
    audited_at: 2026-06-01T125900Z
    note: L1 leaf forecast that the MGS sequential-obstruction is an L3 property of the variant, not an L1 contract distinction
```
```

### Change 2 — reconcile the now-stale §Dependencies "substantive rotation" prose (line 408)

D3 (cycle-044) authored a SUBSTANTIVE L3>L2 theme `book/src/L3-L2/orthogonalize-variant-split.md`
(the loop-erasure / variant-split half is substantive, not identity, so it warrants a dedicated
theme — the cycle-012 non-adjacent-identity convention covers identity edges only). The current
prose says "no `L3-L2/` theme file", which is now false. Update it to point at the new theme for the
substantive variant-split rotation while keeping the **per-step body**-identity in-line note
accurate (the body identity remains in-line; the *variant-split loop rotation* is the substantive
theme).

This edit assumes D3's `orthogonalize-variant-split.md` lands in the same cycle (the integrator
applies D1 → D3 → D4 per the plan's same-file/dependency sequencing). If for any reason D3 does NOT
land this cycle, the integrator must demote the live link to plain text per
`rough-in-forward-reference-must-be-plain-text-not-live-link` — see Open questions.

```edit:book/src/L3/orthogonalize.md
[replace lines 402-408]
The **substantive** rotation is downward in two places. At L1>L0 the in-place `w` overwrite
(`w.Add(-H[j], V[j])`), the raw-pointer `H` write, and the per-variant collective shape are
narrated forward from L1 to L0 by the firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) theme (and the
L2>L1 [`orthogonalize-composition-lowering`](../L2-L1/orthogonalize-composition-lowering.md)
theme narrates the L2 composition into the L1 leaf). At L3>L2 the **per-step `dot`+`axpy` body** is
identity-in-form (annotated in-line above, per the cycle-012 non-adjacent-identity convention), but
the **variant-split loop rotation** — the MGS `jloop` tail recursion collapsing into the L2
per-variant sequencing, and the CGS/CGS2 batched-arm straight-line statements collapsing into the
L2 collective-shape residual axis — is **substantive** and is narrated forward from L3 to L2 by the
[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md) theme (cycle-044). The
L3>L2 edge therefore carries both an in-line body-identity note (the per-step body) and a dedicated
theme (the loop-structure variant split).
```

### Change 3 — reconcile the §L3 vs L2 distinction closing prose (line 479-483)

The §"L3 vs L2 distinction" closing sentence (lines 479-483) repeats the now-stale "No `L3-L2/`
theme file" claim. Update it to the same effect: the **body** identity-in-form lives in-line; the
**loop-structure variant split** is the substantive `orthogonalize-variant-split` theme.

```edit:book/src/L3/orthogonalize.md
[replace lines 479-483]
The L3>L2 hop erases the explicit iteration view (the `jloop` tail recursion / the batched-arm
straight-line statements collapse to L2's per-variant sequencing) and leaves the **per-step body**
identity-in-form. The body identity-in-form annotation lives in-line here (per the cycle-012
meta-phase non-adjacent-identity convention; precedent `book/src/L3/chebyshev.md`,
`book/src/L3/eigsolve.md`); the **substantive loop-structure variant split** (which is NOT an
identity rotation — the MGS `jloop`/CGS-batched-arm collapse is a real rewrite) is the dedicated
[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md) L3>L2 theme (cycle-044, the
first substantive — non-identity — `L3-L2/` theme).
```

### Change 4 — frontmatter `lowers_to:` reconciliation (line 8)

The `lowers_to:` frontmatter (line 8) also asserts "no L3-L2 theme file". Update it to name the new
substantive theme while keeping the body-identity note accurate.

```edit:book/src/L3/orthogonalize.md
[replace line 8]
  - book/src/L2/orthogonalize.md (per-step `dot`+`axpy` body identity-in-form, annotated in-line per cycle-012; the SUBSTANTIVE loop-structure variant split — MGS `jloop`/CGS-batched-arm collapse into the L2 per-variant sequencing — is the dedicated `orthogonalize-variant-split` L3>L2 theme, cycle-044)
```

> Note: Changes 2/3/4 are co-located correctness fixes on the entry under audit (a reconciliation
> of a cross-reference D3 flagged as stale), within the lowering-verifier "co-located correctness
> fix" scope. They are emitted as proposed-changes for the integrator to apply (NOT applied here) —
> the dispatch instruction confirms this routing.

## Supporting evidence

Files consulted (all on-disk `reference/` / `book/`, NOT codemap — `codemap-read-range-plus-one-drift`
guard in force; `tools/citecheck/citecheck.py --anchor` is the no-drift adjudicator):

- `reference/palace/palace/linalg/orthog.hpp` (read in full, 93 lines) — the MGS/CGS/CGS2 bodies.
- `reference/palace/palace/linalg/iterative.cpp:305-325, 625-639, 804-818` — dispatch + consumers.
- `reference/palace/test/unit/test-orthog.cpp:95-164, 228-241` — the parametric + empty + complex
  cases.
- `book/src/concepts/sequential-obstruction.md:20-48` — the MGS structural argument.
- `book/src/L3/orthogonalize.md` (the audited entry).
- `book/src/L3-L2/` directory listing — confirmed the 14 existing themes are all `*-body-identity.md`
  / driver themes; `orthogonalize-variant-split.md` is NOT yet on disk (D3 wave-2 sibling, applied at
  integration).
- `tools/citecheck/citecheck.py` — 24 bounds checks + 13 anchor probes, all `OK`, zero drift.

## Open questions / caveats

- **D3 dependency for the live link (Changes 2/3/4).** The §Downward reconciliation introduces a
  live markdown link `[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md)`. The
  target does **not** exist on disk at audit time — it is D3 (cycle-044)'s proposed-changes output, a
  wave-2 sibling. The integrator applies D1 → D3 → D4 per the plan's same-file sequencing, so by the
  time Change 2/3/4 lands the target should exist and `linkcheck2` will pass. **Carry-forward for the
  integrator:** if D3's theme does NOT land this cycle (rejected / deferred), demote the three live
  links to plain text per `rough-in-forward-reference-must-be-plain-text-not-live-link`, OR sequence
  Change 2/3/4 strictly after D3's file-creation edit. I cannot verify the target exists; flagging the
  ordering dependency explicitly.
- **D1 same-file overlap.** D1 (cycle-044) also re-anchored this entry's audit-block citations
  (`:NN` drift) and may have touched §Lowers-to. I authored Changes 2/3/4 against the **current
  on-disk c040 state** (last commit `26b58f6`); my line-number targets (8, 402-408, 479-483) are
  c040 line numbers. If D1's edits shift those line numbers, the integrator must re-resolve the edit
  anchors by matching the quoted `old`-text (the replaced prose blocks are quoted in full in each
  edit), not by absolute line number. The `verified_against:` append (Change 1) is line-number-
  independent (appends at EOF) and unaffected.
- **Status unchanged — no contradiction found.** The `partial-obstruction` status is the honest
  verdict (MGS loop is a genuine sequential-obstruction; CGS/CGS2 lift). I did NOT flip it.
- **`:62-64` vs `:62-65` minor boundary.** The CGS empty-basis `if (m == 0) { return; }` spans
  `:62-65` (the closing `}` at `:65`); the entry/audit cite `:62-64` for the early-return *statement*
  (`if`+`return`+`}` open). Both are in-bounds witnesses of the same construct; I recorded `:62-64`
  as the entry states (the `return` is at `:64`). Not a drift — flagging only for completeness.
- **No firm L4 `orthogonalize`.** Inherited open item (Arnoldi-step-monad target unauthored); not in
  this audit's scope. Already flagged in the entry's own §Open-questions; no new action.
