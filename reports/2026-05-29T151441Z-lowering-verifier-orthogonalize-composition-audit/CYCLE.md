---
agent: lowering-verifier
invoked_at: 2026-05-29T151855Z
scope: L2>L1 theme audit — orthogonalize-composition-lowering (three-way delegation boundary)
status: integrated
integrated_at: 2026-05-29T17:15:00Z
integration_commit: 210e622
integration_notes: "cycle-025 finalize (first primary cycle of meta-batch-7). VERDICT-ONLY audit — NO artifact mutation, NO new verified_against: rows. Verdict cleanly-partitioned: the three-way delegation boundary (stage-selection [this theme] ⟂ Sub-pattern D inner-product unfusing ⟂ orthogonalize-mutation-rotation in-place w.Add) is cleanly partitioned across the L2>L1 theme + its two L1>L0 delegatees; the cycle-023/024 18-entry verified_against block already covers the delegation-boundary dimension, so appending would duplicate (report proposed None). OQ orthogonalize-composition-lowering-three-way-delegation-boundary-audit RESOLVED (the 4th/last slug on open-questions.md:327 — the WHOLE :327 line is now retirement/unification-ready for meta-phase). 1 NEW optional-cleanup OQ: orthogonalize-composition-lowering-stale-good-direction-34-parenthetical-trim. Build-relevant: no (only open-questions.md appended)."
inputs:
  - book/src/L2-L1/orthogonalize-composition-lowering.md
  - book/src/L1-L0/dot-mutation-rotation.md §Sub-pattern D (:146-187)
  - book/src/L1-L0/orthogonalize-mutation-rotation.md
  - palace/linalg/orthog.hpp:18-90 (header-only; orthog.cpp does not exist)
  - palace/linalg/iterative.cpp:305-326 (OrthogonalizeIteration dispatch)
  - palace/models/romoperator.cpp:51-66 (ROM OrthogonalizeColumn dispatch)
---

# CYCLE: Audit orthogonalize-composition-lowering (three-way delegation boundary)

## Summary

I audited the firm L2>L1 theme `orthogonalize-composition-lowering` against the **specific
question of the three-way delegation boundary**: whether the three distinct concerns that all
touch Palace's Gram-Schmidt machinery — (1) **stage-selection** owned by THIS theme, (2)
**inner-product collective unfusing** owned by `dot-mutation-rotation` §Sub-pattern D, and (3)
**in-place `w.Add` candidate-buffer rebinding** owned by `orthogonalize-mutation-rotation` —
are cleanly partitioned with no overlapping claims and no contradictory characterizations of
the same source range. **Top-level verdict: fully-supported / cleanly-partitioned.** The three
themes do cite an overlapping set of `orthog.hpp` source ranges (`:41-53`, `:57-74`, `:75-88`,
`:35`), but each cites them for a **disjoint facet** of the same code — collective-shape /
pass-count (this theme), the `LocalDot`+`GlobalSum` hook unfusing (Sub-pattern D), and the
in-place `w` overwrite + raw-`H` write (the L1>L0 theme). The three facets are mutually
consistent (no contradiction) and the load-bearing content of each is not re-derived in the
others — the delegation is explicit in prose and the cross-references resolve. The cycle-023
17-citation `verified_against:` audit (now grown to 18 entries via this theme's own producer
self-verification, `audited_at: 2026-05-29T092943Z`) **stands and is not duplicated** by this
pass — this audit confirms the *delegation-boundary* dimension that the existing block's final
three cross-theme entries already assert, and adds no new `verified_against:` rows (no edit to
the theme is proposed). All anchors re-confirmed clean via `tools/citecheck --anchor` and
`--scan` (0 failing across all three themes, 100 citations total).

## Per-citation audit

The theme's full 38-citation `verified_against:` + prose citation set scans clean
(`citecheck --scan`: 38 ok / 0 failing). I focused the per-citation audit on the **boundary-
critical anchors** — the source ranges that are shared across the three themes, since those are
the only places a duplication or contradiction could hide.

- **Citation**: `palace/linalg/orthog.hpp:35`
  - **Theme claim**: `IdentityInnerProduct::operator()` returns `LocalDot(x, y)` at `:35` — the
    Sub-pattern D pointer; the theme explicitly notes "(NOT :34 — line 34 is the brace)".
  - **Found**: `read_range` `:32-35` shows the `operator()` body `{ ... return LocalDot(x, y); }`
    with the `return LocalDot(x, y)` on line 35. `citecheck --anchor LocalDot` → `ok` at line 35.
  - **Verdict**: supports
  - **Notes**: This is the anchor cycle-024 fixed (`:34→:35`) in the *cited* theme
    (`dot-mutation-rotation`). I confirmed the fix is applied in `dot-mutation-rotation.md` at
    BOTH the prose (line 160, `orthog.hpp:35`) AND its `verified_against:` block (line 404,
    `citation: palace/linalg/orthog.hpp:35`). The L2>L1 theme under audit cites the *enclosing*
    `:29-36` range and pins `:35` in prose — consistent, no residual `:34` drift anywhere.

- **Citation**: `palace/linalg/orthog.hpp:41-53` (MGS body) — **SHARED by all three themes**
  - **Theme claim** (this theme): the `[dot, axpy] × m` interleaved **sequence** — `dot` at
    `:49`, `Mpi::GlobalSum(1, &H[j])` at `:50`, `w.Add(-H[j], V[j])` at `:51`, all in one
    `j`-loop → `m` reductions of size 1 (the collective-shape / pass-count facet).
  - **Found**: `read_range` `:39-52` confirms `OrthogonalizeColumnMGS` def at `:41`, the single
    `for` loop, `H[j] = dot_op(w, V[j])` at `:49`, `Mpi::GlobalSum(1, &H[j], comm)` at `:50`,
    `w.Add(-H[j], V[j])` at `:51`. `citecheck --anchor` clean on `:41`/`:49`/`:50`/`:51`.
  - **Verdict**: supports
  - **Notes**: The `orthogonalize-mutation-rotation` L1>L0 theme cites the same `:41-53` but for
    the **in-place `w.Add` = `w^(j)` intermediate** facet (buffer-rebinding); Sub-pattern D cites
    the overlapping `:46-52` for the **`LocalDot`+`Mpi::GlobalSum(1,&H[j])` hook** facet. The
    three characterizations are mutually consistent (same loop, three disjoint readings) — see
    §Applicability conditions boundary analysis below. No contradiction.

- **Citation**: `palace/linalg/orthog.hpp:57-74` (CGS body) — **SHARED by all three themes**
  - **Theme claim** (this theme): `[dot × m]` then `[axpy × m]` separated; `m==0` early return
    at `:62`, one `Mpi::GlobalSum(m, H, comm)` at `:70` → 1 reduction of size `m`; dots mutually
    independent (the pass-count facet).
  - **Found**: `read_range` `:53-71` confirms `OrthogonalizeColumnCGS` def at `:57`,
    `if (m == 0) { return; }` at `:62`, the `m`-local-dot loop `:66-69`, `Mpi::GlobalSum(m, H,
    comm)` at `:70`, the `m`-`w.Add` loop `:71-74`. `citecheck --anchor` clean on `:62`/`:70`.
  - **Verdict**: supports
  - **Notes**: L1>L0 theme cites `:57-74` for the two-phase in-place split + the `m==0`
    empty-basis law; Sub-pattern D cites `:66-70` for the batched-collective unfusing. Disjoint
    facets. The theme's prose `verified_against:` row uses `:57-74`; the body-section heading
    uses `:55-89` (line 307) — see Open questions (a benign enclosing-vs-precise range
    co-existence within one theme, not a boundary defect).

- **Citation**: `palace/linalg/orthog.hpp:75-88` (CGS2 / `if (refine)` block) — **SHARED by all three**
  - **Theme claim** (this theme): `[CGS] × 2`; `if (refine)` at `:75`, `H[j] += dH[j]`
    accumulate at `:85`, second `Mpi::GlobalSum(m, dH.data(), comm)` → 2 reductions of size `m`;
    second pass non-fusible.
  - **Found**: `read_range` `:75-88` confirms `if (refine)` at `:75`, the `dH` scratch, second
    local-dot loop, `Mpi::GlobalSum(m, dH.data(), comm)`, and the `H[j] += dH[j]; w.Add(-dH[j],
    V[j])` loop with `H[j] += dH[j]` at `:85`. `citecheck --anchor` clean on `:75`/`:85`.
  - **Verdict**: supports
  - **Notes**: The CGS2 non-fusibility (idempotence-as-law-5 read as lowering) is THIS theme's
    algebraic content; the L1>L0 theme cites `:75-88` for the in-place doubled-`w.Add` mechanics
    + the `H_returned = H + dH` accumulate. Consistent: this theme owns *why* two passes (law 5),
    the L1>L0 theme owns *how* the second pass mutates the buffers. No overlap of claim.

- **Citation**: `palace/linalg/iterative.cpp:308-325` / `:322` (OrthogonalizeIteration dispatch) — **SHARED**
  - **Theme claim** (this theme): the runtime variant dispatch `switch (type)` over MGS/CGS/CGS2;
    CGS2 = `OrthogonalizeColumnCGS(..., true)` at `:322`; variant bound + dispatched once.
  - **Found**: `read_range` `:305-326` confirms `OrthogonalizeIteration` with `switch (type)`,
    three cases, CGS2 = `...(comm, V, w, Hj, j + 1, true)` at `:322`, forwards `j + 1` as `m`.
    `citecheck --anchor` clean.
  - **Verdict**: supports
  - **Notes**: The L1>L0 theme cites the same dispatch (`:307-325`) for the **runtime variant
    selection** (which loop structure). This theme cites it for the same purpose (the dispatch
    site of the stage-selection). This is the ONE place where the two themes' citation purposes
    are nearest — but it is NOT a duplication-defect: a dispatch `switch` is legitimately the
    grounding for *both* "the L1 leaf inspects variant once" (L1>L0) AND "the L2 dispatch tag
    flows through to the per-variant sequence" (L2>L1). Both readings are correct and
    complementary; neither re-derives the other's content. See boundary analysis condition 1.

- **Citation**: `palace/models/romoperator.cpp:51-66` (ROM OrthogonalizeColumn) — **SHARED**
  - **Theme claim** (this theme): ROM sibling dispatch; threads the `dot_op` hook through all 3
    cases; CGS2 = `refine=true` at `:65`.
  - **Found**: `read_range` `:51-66` confirms `OrthogonalizeColumn` switch, all three cases pass
    `dot_op`, CGS2 = `OrthogonalizeColumnCGS(..., true, dot_op)` at `:65`, forwards `j` (not
    `j+1`). `citecheck --anchor` clean.
  - **Verdict**: supports
  - **Notes**: Identical complementary-citation situation to the `iterative.cpp` dispatch. Both
    themes cite it; this theme for the second stage-selection dispatch surface + the `dot_op`
    hook threading, the L1>L0 theme for the `j`-vs-`j+1` column-count + hook. Disjoint facets.

- **Citation**: `palace/models/romoperator.cpp:636` (B-weighted hook)
  - **Theme claim**: `W.InnerProduct(x, y, r.Real())` at `:636` — the B-weighted `op.dot`
    substitution (L2 law-7 hook-invariance witness).
  - **Found**: `citecheck --anchor InnerProduct` → ok at `:636` (within cited `:631-646`).
  - **Verdict**: supports
  - **Notes**: This is THIS theme's exclusive concern (inner-product-hook variant axis on the
    composition shape); Sub-pattern D owns the *unweighted* identity-hook realisation. The
    B-weighted substitution is correctly delegated as "same `dot` substitution through the
    identical composition" — not re-derived in Sub-pattern D. Clean.

- **Citation**: consumer sites `iterative.cpp:630-632`, `:809-811`, `romoperator.cpp:224-226`
  - **Theme claim**: each consumer follows the dispatch with its own `Norml2` + `scal` —
    normalisation is NOT a dependency of this lowering (applicability condition 2).
  - **Found**: `citecheck --anchor Norml2` → ok on all three ranges.
  - **Verdict**: supports
  - **Notes**: The L1>L0 theme cites `iterative.cpp:629-632` / `:808-811` for the SAME
    "normalisation is the caller's" point (its applicability condition 3) AND for "no observer of
    prior `w`" (its condition 1). This is a legitimately-shared *negative* fact (the lowering
    stops at the un-normalised residual) that BOTH layers must state at their own boundary; it is
    a shared contract, not a duplicated derivation. Clean.

- **Citation**: tests `test/unit/test-orthog.cpp:99-120`, `:123-160` (`:158`), `:276`, `:333`
  - **Theme claim**: empty-prefix identity (law 3) across all 3 variants; variant-agreement
    orthogonality `⟨residual, V[i]⟩ ≈ 0` to 1e-12 at `:158`; B-weighted variant witnesses.
  - **Found**: `citecheck --anchor` clean on the empty-prefix `Empty` boundary (`:99-120`) and
    `WithinAbs` (`:158`).
  - **Verdict**: supports
  - **Notes**: L1>L0 theme cites the same `:99-120` empty-basis edge for the `m==0` early-return
    witness. Shared test citation, complementary readings (law-3 across variants vs the
    `if (m==0) return;` L0 witness). Clean.

## Applicability conditions

The theme states 6 applicability conditions. The audit-relevant ones (those touching the
boundary) walk through cleanly:

- **Condition**: (1) Orthonormal basis precondition (`orthog.hpp:18-23`).
  - **Verifiable**: Yes — header text "Assumes that the input vectors are normalized, but does
    not normalize the output vectors!" confirmed at `:22` via `citecheck --anchor Assumes`. This
    is a SHARED contract with the L1>L0 theme's condition 3 (same header, same range). It is a
    shared *precondition*, correctly inherited by both layers — not a duplicated derivation.
  - **Found counter-example?**: No.

- **Condition**: (2) No output normalisation in this composition.
  - **Verifiable**: Yes — the three consumer sites (`iterative.cpp:630-632`, `:809-811`,
    `romoperator.cpp:224-226`) all do their own `Norml2`+`scal`; `nrm2`/`scal` correctly
    excluded as dependencies. Same boundary the L1>L0 theme draws (its condition 3).
  - **Found counter-example?**: No.

- **Condition**: (5) Inner-product hook is a `dot` substitution; "The hook's L0 realisation is
  the `InnerProductHelper` template, covered by Sub-pattern D."
  - **Verifiable**: Yes — this is the EXPLICIT delegation to boundary-2. The theme states the
    hook substitution leaves the lowering shape + collective-shape table invariant and points at
    Sub-pattern D for the L0 realisation rather than re-deriving it. Confirmed Sub-pattern D
    (`dot-mutation-rotation.md:146-187`) owns exactly that (the `IdentityInnerProduct` +
    `LocalDot` + batched `GlobalSum` unfusing).
  - **Found counter-example?**: No.

- **Condition**: (6) In-place candidate destruction; "the leaf's onward lowering to the in-place
  L0 buffer is the firm `orthogonalize-mutation-rotation` theme's applicability condition 1 (no
  observer of the prior `w` after the call) — **not re-derived here**."
  - **Verifiable**: Yes — this is the EXPLICIT delegation to boundary-3. Confirmed the L1>L0
    `orthogonalize-mutation-rotation` theme's condition 1 (line 161-166) owns exactly that
    no-observer-of-prior-`w` claim, and its conditions 4 (no aliasing) + 5 (single-rank collapse)
    own the in-place `w.Add` mechanics. The L2>L1 theme correctly stops at the L1 leaf.
  - **Found counter-example?**: No.

### Three-way delegation-boundary partition (the audit target)

The three concerns map onto disjoint owners with explicit hand-off prose at each seam:

| Concern | Owner theme | What it owns (the facet of the shared `orthog.hpp` code) | Hand-off prose |
|---|---|---|---|
| 1. Stage-selection | **THIS theme** (`orthogonalize-composition-lowering`, L2>L1) | which `[dot, axpy]` sequence per variant; pass-count + collective shape (`m×1` / `1×m` / `2×m`); the variant-dispatch rule (law 4) + CGS2-as-law-5 | owns §"The variant-dispatch rewrite", §"Collective-shape recording" |
| 2. Inner-product unfusing | `dot-mutation-rotation` §Sub-pattern D (L1>L0) | the unfused `LocalDot` (`:35`) + the hook-routed batched `Mpi::GlobalSum` collective; the unweighted-observable conjugation note | cited at §"Inner-product realisation — cite Sub-pattern D, do not re-derive" + condition 5 |
| 3. In-place `w.Add` | `orthogonalize-mutation-rotation` (L1>L0) | the in-place `w` overwrite = `w^(j)` rebinding; raw-`H`-pointer write; aliasing + no-prior-observer + single-rank-collapse mechanics | cited at Face-2 §, condition 6, §"Justification kind" |

**The shared-source-range question (the only place a defect could hide):** all three themes cite
`orthog.hpp:41-53` / `:57-74` / `:75-88` and the two dispatch switches. This is **expected and
correct, not a duplication defect** — a single ~50-line header-only routine legitimately grounds
three distinct layer-boundary claims:
- the **collective-shape / pass-count** reading (this theme) — *which sequence, how many reductions*;
- the **inner-product-collective** reading (Sub-pattern D) — *how the `yᴴx` reduction is split across the hook boundary*;
- the **buffer-mutation** reading (the L1>L0 theme) — *how `(w', H)` materialises as in-place `w` + raw `H`*.

I cross-read all three characterizations of each shared range against the source and found them
**mutually consistent**: e.g. for MGS `:49-51`, the three readings ("interleaved `[dot,axpy]`,
`m` size-1 reductions" / "`LocalDot`+`GlobalSum(1)` hook" / "`w.Add` = `w^(j)` intermediate")
describe the same three lines from three angles with **no contradictory claim** about what the
code does. The load-bearing derivation of each facet lives in exactly one theme; the other two
cite (not re-derive). **Found counter-example? No — the boundary is cleanly partitioned.**

## Algebraic laws (if cited)

- **Law**: L2 law 4 (variant agreement — the three `[dot, axpy]` sequences are one value in exact
  arithmetic).
  - **Holds on operators?**: Yes. The dispatch rule IS this law read as a lowering; the three
    `orthog.hpp` bodies compute `(I − V Vᴴ)w` (modulo finite-precision residue) — confirmed
    structurally + witnessed by `test-orthog.cpp:123-160` (`⟨residual,V[i]⟩ ≈ 0` to 1e-12 across
    all three variants, `WithinAbs` at `:158`).
- **Law**: L2 law 5 (idempotence-on-residual) → CGS2 = `[CGS] × 2`.
  - **Holds on operators?**: Yes. The `if (refine)` second pass (`:75-88`) is the explicit
    re-application; `H[j] += dH[j]` at `:85` is the accumulate. The non-fusibility (second pass
    reads once-orthogonalised `w1`) is correctly stated as a non-law. Consistent with the L1>L0
    theme's Sub-pattern C algebraic justification.
- **Law**: L2 law 7 (inner-product-hook invariance).
  - **Holds on operators?**: Yes. The `op.dot` closure substitution (identity `LocalDot` →
    B-weighted `W.InnerProduct`, `romoperator.cpp:636`) leaves the composition shape and the
    collective-shape table invariant — the hook is a `dot`-leaf substitution, structurally
    transparent. Confirmed against both dispatch sites threading `dot_op`.

## Proposed changes

**None.** The theme is `firm`, fully cited, and the three-way delegation boundary is cleanly
partitioned. The existing `verified_against:` block (18 entries, `audited_at:
2026-05-29T092943Z`, producer self-verification + the cycle-023-equivalent retroactive set)
**already asserts the delegation-boundary dimension** in its final three cross-theme entries
(`dot-mutation-rotation.md:146-187` "boundary 2", `orthogonalize-mutation-rotation.md` "boundary
3", `L2/orthogonalize.md:166-220` laws). This audit **confirms those three entries stand** and
adds no new rows — appending a fresh `verified_against:` block would DUPLICATE the existing one
(the scope explicitly warned against re-doing the cycle-023 audit). The boundary verdict is
recorded here in the report; no theme mutation is warranted.

(For completeness, were a row to be added it would read — but is NOT proposed, to avoid the
duplication the scope cautioned against:
`citation: <three-way-boundary>, verdict: supports, note: cleanly-partitioned, no overlap/gap`.)

## Supporting evidence

Source / test / theme files consulted (all via `palace-codemap read_range` + `tools/citecheck`):

- `palace/linalg/orthog.hpp:25-90` — read in full: `IdentityInnerProduct` (`:30-36`, `LocalDot`
  at `:35`), `OrthogonalizeColumnMGS` (`:41-53`), `OrthogonalizeColumnCGS` (`:57-89`, incl. the
  `if (refine)` CGS2 block `:75-88`, `H[j] += dH[j]` at `:85`).
- `palace/linalg/iterative.cpp:305-326` — `OrthogonalizeIteration` dispatch (`switch (type)`,
  CGS2 `...,true` at `:322`, forwards `j+1`).
- `palace/models/romoperator.cpp:51-66` — ROM `OrthogonalizeColumn` dispatch (threads `dot_op`,
  CGS2 `...,true,dot_op` at `:65`, forwards `j`).
- `book/src/L1-L0/dot-mutation-rotation.md:146-187` — §Sub-pattern D (boundary-2 owner);
  confirmed its `:35` anchor fix (cycle-024) applied at prose line 160 + `verified_against:`
  line 404.
- `book/src/L1-L0/orthogonalize-mutation-rotation.md` (full) — boundary-3 owner; its conditions
  1/4/5 own the in-place `w.Add` mechanics; cycle-014 audit `firm` upheld.
- `tools/citecheck/citecheck.py --anchor` on 19 boundary anchors (all `ok`, 0 drift) and
  `--scan` on all three themes (38 / 41 / 21 citations, 0 failing = 100 total).

## Open questions / caveats

- **OQ `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` — DISCHARGED.**
  Verdict: **cleanly-partitioned**. The three concerns (stage-selection / inner-product unfusing
  / in-place `w.Add`) own disjoint facets of the shared `orthog.hpp` routine; the shared
  source-range citations are complementary layer-boundary readings, not duplicated derivations,
  and no characterization contradicts another. No theme mutation proposed.

- **Benign enclosing-vs-precise range co-existence WITHIN this theme (not a boundary defect, not
  proposed for change).** The theme cites the CGS body at TWO slightly different ranges in
  different sections: the body-section heading + collective table use `orthog.hpp:55-89` (line
  307) / `:57-74` (line 196) and the `verified_against:` block uses `:57-74` (`:75-88` split out
  for CGS2). `citecheck --scan` passes on all of them (each is in-bounds and the `OrthogonalizeColumnCGS`
  def begins at `:57`, the `if (refine)` block at `:75`, function closes `:89`). This is the
  same enclosing-vs-precise pattern the `verify-citation-range` audit-sub-case flags for
  reconciliation; here both forms are correct and consistent (the `:55-89` is the
  whole-function-incl-CGS2 enclosing range, the `:57-74`+`:75-88` pair is the precise
  non-refine/refine split). Recording for transparency per the "reconcile two-range citations
  before asserting no-drift" discipline — I reconciled them and they agree; no drift, no fix
  needed.

- **Carry-forward already recorded by the producer (no new action).** The theme's
  `verified_against:` note on `dot-mutation-rotation.md:146-187` states "Sub-pattern D's own :34
  anchor for LocalDot is stale (should be :35); that is the cited theme's defect, not this
  theme's." I independently confirmed this carry-forward is **already resolved** — cycle-024
  fixed `dot-mutation-rotation` Sub-pattern D from `:34→:35` at both its prose (line 160) and its
  `verified_against:` block (line 404). So the producer's caveat is now **stale-in-the-good-
  direction** (the referenced defect is fixed). No edit needed; flagging only so a future reader
  does not chase a defect that no longer exists. (If a lifter touches this theme for an unrelated
  reason, the note's parenthetical could be trimmed, but that is below the bar for a dispatch.)

- **Inherited caveat (not a status reduction).** No dedicated L1↔L2 equivalence test asserting
  the de-fused Face-2 `[dot, axpy]` sequence reproduces the Face-1 leaf value; variant-agreement
  is witnessed at L0 (`test-orthog.cpp:123-160`). This carries through from the sibling
  `linear-combination-fold-specialization` and does not gate `firm` (the laws are L2-firm read as
  lowering, not test-gated structure). Unchanged by this audit.
