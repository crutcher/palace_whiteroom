---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T040000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T041500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L1>L0 theme dot-mutation-rotation (stub → firm)

## Critique

### Checks run

**citation-validity — warning.** Every claim in the report carries a pointer, and I independently
re-read every cited L0 range via `palace-codemap read_range` / `search_text` (not trusting the
report's "self-verified" tags). The overwhelming majority are line-exact: `ComplexVector::Dot`
body `vector.cpp:263-267` (incl. the `this==&y` imag=`0.0` fast path at `:266`); `TransposeDot`
`vector.cpp:269-274` (the `2·Im·Re` self-dot branch at `:272-273`); the real leaf
`vector.cpp:665-672`; the complex leaf `vector.cpp:674-685`; the `linalg::Dot` template
`vector.hpp:246-253` (doc-comment `// … parallel inner product yᴴ x or yᵀ x` at `:246`, body
`LocalDot` + `Mpi::GlobalSum` at `:248-253`); the `LocalDot` decls `vector.hpp:242-244`; the
method decls + `operator*` alias `vector.hpp:110-113`; `Mpi::GlobalSum`
`communication.hpp:266-270` → `GlobalOp` → `MPI_Allreduce(MPI_IN_PLACE, …, MPI_SUM, comm)`
`communication.hpp:246-249`; CG `beta = linalg::Dot(comm, z, r)` at `iterative.cpp:395`; the test
`test/unit/test-vector.cpp:206-207` (`double dot = vec1 * vec2; … WithinRel(32.0)`); the
`Norml2` diagonal case `vector.hpp:256-260`; the `nleps.cpp:487` `std::abs(linalg::Dot(...))`
witness; the M-weighted boundary-marker overload `operator.cpp:621-638`. `search_text TransposeDot`
returns exactly the definition (`vector.cpp:269`) and one declaration (`vector.hpp:112`) — zero
call sites, as claimed. **Two off-by-one inline-anchor drifts** are the reason this is `warning`
not `pass` — see Issues 1 and 2. The recurring cycle-020 inline-anchor-drift pattern flagged in
the dispatch is real here.

**surface-or-evidence — pass.** This is a stub→firm promotion that adds the full theme surface
(three RHS sub-patterns with verbatim L0 bodies, the conjugate-pair re-order rule, the variant
axes, status `firm`) — it is not a pure rotation_claim. The load-bearing surface content (the
conjugation asymmetry: Palace `yᴴ x` arg-2 vs L1 `xᴴ y` arg-1, the identity
`xᴴ y = conj(yᴴ x)`, the operand-swap / outer-conj recovery rules) is grounded in directly-read
evidence: `ComplexVector::Dot` body returns `x·conj(y) = yᴴ x` (arg-2 `y` conjugated, `:265-266`),
the complex `LocalDot` has the matching arg-2-conjugated cross-term sign
`Im = LocalDot(xi,yr) − LocalDot(xr,yi)` (`:684`), and the three doc-strings (`vector.hpp:110`,
`:242`, `:246`) all read `yᴴ x`. The report's central claim "docs and bodies agree — no
Palace-internal contradiction; the asymmetry is between Palace's `yᴴ x` and the L1 `xᴴ y`" **holds**
on the read evidence. The re-order-invisible witnesses (CG `iterative.cpp:395`, `nleps.cpp:487`,
`Norml2` `vector.hpp:256-260`) all check out.

**rotation-quality — pass.** The narration is forward high→low (LHS = L1 `dot`, RHS = L0 source),
honoring the layers-defined-high→low invariant; the reverse-direction lift note is correctly
quarantined to the §Open questions working-notes, not the chapter body. The lowering is a genuine
expansion-of-hidden-structure rotation: one pure L1 reduction step expands into the L0
local-then-collective two-step (`Mpi::GlobalSum ∘ LocalDot`) that the L1 signature hides, plus the
conjugate-pair re-handing. This is state/collective-topology hiding compression in the L1→L0
direction (equivalently, the L1 form is strictly more abstract than the L0 surface), not a 1:1
rename. Pass.

**variant-axis-coverage — pass.** Two orthogonal axes are declared and each combination covered:
element-type {real | complex} (real leaf sub-pattern C `vector.cpp:665-672`; complex leaves
sub-patterns B/A `vector.cpp:263-267` / `:674-685`) and conjugation {hermitian `dot` |
unconjugated `tdot`} for complex only (`ComplexVector::Dot` vs `ComplexVector::TransposeDot`). The
`tdot` arm is explicitly scoped as "type-API-surface-only" with the zero-call-sites evidence
(`search_text` verified) rather than hidden — a behavioral caveat, correctly not a status
reduction. No hidden branches. Matches `classify-variant-axis`. Pass.

**cross-reference-integrity — pass.** All `[link]` targets resolve: `../L1/dot.md`,
`./nrm2-mutation-rotation.md`, `./axpby-mutation-rotation.md`, `./axpbypcz-mutation-rotation.md`,
`../L2-L1/inner-product-fold-specialization.md` all exist. The cited §"The conjugate-pair
re-order" and §"Summation-order recording" sections of the L2>L1 sibling exist
(`inner-product-fold-specialization.md:158`, `:222`) and carry the same `xᴴ y = conj(yᴴ x)`
identity — the consistency citation is accurate. The forward-ref claim "nrm2 already cites this
theme forward" is verified (`nrm2-mutation-rotation.md:49-50` links `[dot-mutation-rotation]`).
The L1/dot.md anchor lines cited (`:33-35`, `:43`, `:45`, `:49`, `:89-96`) all land on the
claimed content. OQ `l1-l0-dot-lowering-asymmetry` and `dot-reduction-tree-determinism-survey`
both exist in the ledger. Pass.

**edge-label-fidelity — pass.** The edge label throughout is L1>L0; the prose, the LHS/RHS framing,
the §Justification-kind, and the dep-map row all discuss exactly the L1→L0 edge. No L2 content
leaks in except as a correctly-attributed consistency citation to the adjacent L2>L1 theme. Pass.

**plan-kind-consistency — pass.** Declared kind is a `firm` theme promotion from `stub`. The
current chapter is a genuine `stub` (verified: `status: stub`, claim-free, "Implied by"
provenance) so stub→firm is the correct transition. The proposed content shape matches `firm`:
exhaustive cited RHS bodies, applicability conditions, variant-axis exhaustion, a positively-
anchored value-level identity (no negative-anchor reconstruction, no speculative operator), and
the report correctly argues `firm` over `partly-constructive`. The proposed-changes are well-formed:
(i) full `edit:` of the chapter, (ii) dep-map row appended to `L1-L0/index.md` after the verbatim-
quoted existing nrm2 row, (iii) SUMMARY de-stub. No rough-in placeholders in a firm entry. Pass.

**skill-uptake-survey — pass.** The report references `verify-citation-range` (self-verification,
§Verified-against) and `classify-variant-axis` (§Variant axes); both skills exist under `skills/`.
The shape (rotation theme) would also admit `verify-rotation-citation` / `propose-rotation`, not
invoked, but the two referenced cover the citation + variant dimensions. Telemetry only; pass.

### Issues found

**Issue 1 — inline-anchor drift: `MFEM_ASSERT` cited at `:667`, actually at `:668`.**
Location: `CYCLE.md` §Proposed-changes Sub-pattern C citation list (chapter line "with the
aligned-pass precondition `MFEM_ASSERT(x.Size() == y.Size())` (`:667`)"), the §Applicability
condition 2 (`palace/linalg/vector.cpp:667`), §Verified-against (`MFEM_ASSERT(x.Size()==y.Size())`
at `:667`), and the §Theme-prose Sub-pattern C (`:667`). I read `vector.cpp`: line 665 =
`double LocalDot(const Vector &x, const Vector &y)`, 666 = `{`, 667 = `static hypre::HypreVector X, Y;`,
**668 = `MFEM_ASSERT(x.Size() == y.Size(), "Size mismatch for vector inner product!");`**. The
enclosing `:665-672` range is correct; only the pinpoint `:667` is off by one (should be `:668`).
Severity: low (the enclosing range is right, claim content is correct), but it recurs 4× in the
report so the fix touches multiple sites.

**Issue 2 — inline-anchor drift: complex-leaf self-dot imag=`0.0` cited at `:679`, actually at `:678`.**
Location: `CYCLE.md` §Proposed-changes Sub-pattern C citation list ("the `&x==&y` self-dot fast
path returning imag = `0.0` (`:679`)"), §Verified-against (same, `:679`), and §Theme-prose
Self-dot fast path ("the complex `LocalDot` returns imag `0.0` (`vector.cpp:679`)"). I read the
`vector.cpp:674-682` block: 674 = `std::complex<double> LocalDot(const ComplexVector &x, …)`,
675 = `{`, 676 = `if (&x == &y)`, 677 = `{`, **678 = `return {LocalDot(x.Real(), y.Real()) + LocalDot(x.Imag(), y.Imag()), 0.0};`**,
679 = `}`, 680 = `else`. The imag=`0.0` self-dot return is at `:678`, not `:679`. Corroborating:
the firm sibling `book/src/L1/dot.md:68` already pins this exact line as `vector.cpp:678`, so this
report drifted from the established anchor. The enclosing `:674-685` range is correct; only the
pinpoint is off by one (should be `:678`). Severity: low; recurs 2×.

**Issue 3 (informational, not a defect) — `Dot` template range `:246-253` vs sibling's `:247-253`.**
Location: report cites the `linalg::Dot` template as `vector.hpp:246-253` throughout; the firm
`L1/dot.md:111` cites it as `:247-253`. I read `vector.hpp`: `:246` is the doc-comment
`// Calculate the parallel inner product yᴴ x or yᵀ x`, `:247` is `template <typename VecType>`,
body through `:253`. The report's `:246-253` is the *more* inclusive/precise range (it captures
the load-bearing `yᴴ x` doc-comment the report relies on for the asymmetry claim). This is not an
error — flagged only so the repairer does not "correct" it toward the sibling's narrower range.
No action needed.

**Issue 4 (informational) — proposed dep-map edit reproduces the existing nrm2 row verbatim.**
Location: `CYCLE.md` `edit:book/src/L1-L0/index.md` block. The block quotes the existing
`L1-L0/index.md:27` nrm2 row exactly and appends the new dot row beneath it; this is the standard
"insert-after" framing, not a duplicate-row hazard (verified: no pre-existing dot row in
`index.md`). The SUMMARY de-stub targets the existing `SUMMARY.md:82`
`- [dot-mutation-rotation (stub)](...)` in place (drop ` (stub)`, path unchanged) — an in-place
de-stub, not a duplicate append, as required. No defect; recorded so the integrator applies the
index edit as an append-after-nrm2 and the SUMMARY edit as an in-place suffix-drop.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: inline-anchor drift — `MFEM_ASSERT(x.Size() == y.Size())` cited at `:667`,
  actually at `:668` (enclosing `:665-672` correct; sibling `dot.md:68` context + the recurring
  cycle-020 inline-anchor-drift pattern).
  - **Decision**: repaired
  - **Action**: Verified via `mcp__palace-codemap__read_range palace/linalg/vector.cpp:665-685`:
    line 667 = `static hypre::HypreVector X, Y;`, **line 668 = `MFEM_ASSERT(x.Size() == y.Size(),
    "Size mismatch for vector inner product!");`** — confirms `:668`. Rewrote the pinpoint `:667`
    → `:668` at **all 5 occurrences** in `CYCLE.md` (the critic noted "4×"; a 5th instance in
    §Verified-against carried the same drift, fixed for consistency): §L0-form Sub-pattern A leaf
    list (line 81), §Theme-prose Sub-pattern C (line 241), §Proposed-changes Sub-pattern C
    Citations (line 252), §Applicability condition 2 (line 341), §Verified-against (line 393). The
    enclosing `:665-672` range is left intact everywhere. Mechanical pinpoint correction.

- **Finding (Issue 2)**: inline-anchor drift — complex-leaf self-dot `imag = 0.0` return cited at
  `:679`, actually at `:678` (enclosing `:674-685` correct; sibling `dot.md:68` already pins
  `:678`).
  - **Decision**: repaired
  - **Action**: Verified via the same codemap read: line 676 = `if (&x == &y)`, **line 678 =
    `return {LocalDot(x.Real(), y.Real()) + LocalDot(x.Imag(), y.Imag()), 0.0};`**, line 679 = `}`
    — confirms `:678`. Rewrote `:679` → `:678` at **all 3 occurrences** (the critic noted "2×"; a
    3rd instance in §Theme-prose Self-dot fast path carried the same drift, fixed for consistency):
    §Theme-prose Self-dot fast path (line 111, the `vector.cpp:679` long form), §Proposed-changes
    Sub-pattern C Citations (line 255), §Verified-against (line 397). The enclosing `:674-685`
    range is left intact everywhere. Mechanical pinpoint correction.

- **Finding (Issue 3, informational — NOT a defect)**: `Dot` template range `:246-253` vs sibling's
  `:247-253`.
  - **Decision**: not-needed
  - **Rationale**: The critic explicitly flagged this as the *more* precise range (captures the
    load-bearing `yᴴ x` doc-comment at `:246` the asymmetry claim rests on) — not an error. Left
    untouched; all 4 `:246-253` sites preserved (verified post-edit). No "correction" toward the
    sibling's narrower range, per the critic's directive.

- **Finding (Issue 4, informational — NOT a defect)**: dep-map insert-after-nrm2 framing + SUMMARY
  in-place de-stub at `:82`.
  - **Decision**: not-needed
  - **Rationale**: Correctly framed (insert-after, not duplicate-row; in-place suffix-drop). No
    edit; recorded for the integrator's application semantics only.

### Unrepairable findings

None. Both citation-validity drifts were off-by-one pinpoint corrections within already-correct
enclosing ranges, independently confirmed against the L0 source via codemap `read_range`. No
substantive authoring was required.

## Suggested resolution

`ready`. Both inline-anchor drifts are repaired (all 8 occurrences across the two findings: 5×
`:667`→`:668`, 3× `:679`→`:678`), each verified against `palace/linalg/vector.cpp` and aligned with
the firm sibling `book/src/L1/dot.md` anchors. The citation-validity `warning` is fully resolved at
the mechanical level; the report's claim content was always correct (enclosing ranges right).
Integrator notes: apply the `L1-L0/index.md` edit as an append-after the verbatim-quoted nrm2 row
(`:27`), and the `SUMMARY.md` edit as an in-place ` (stub)`-suffix drop at the existing
`dot-mutation-rotation` row (~`:82`, path unchanged) — this is the stub→firm de-stub. No follow-up
agent required.
