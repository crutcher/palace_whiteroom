---
agent: lowering-verifier
invoked_at: 2026-05-28T19:33:06Z
scope: L1>L0 theme audit — orthogonalize-mutation-rotation
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: 73ecd3e
integration_notes: "cycle-014 position 2/8. Verdict CONFIRMS-WITH-REFINEMENT; theme UPHELD firm. Applied R1 anchor tighten (iterative.cpp:321-323→:322, CGS2 dispatch, critic-confirmed via get_call_sites) + verified_against YAML block (10 supports) to L1-L0/orthogonalize-mutation-rotation.md §Status. R2 cosmetic brace-extend NOT applied. Answers cycle-013 audit-request OQ; residual ROM-greedy-consumer condition-1 caveat surfaced as OQ orthogonalize-mutation-rotation-audit-confirmed-rom-consumer-residual. Build clean."
inputs:
  - book/src/L1-L0/orthogonalize-mutation-rotation.md
  - palace/linalg/orthog.hpp:41-89 (OrthogonalizeColumnMGS, OrthogonalizeColumnCGS + refine block)
  - palace/linalg/iterative.cpp:307-325 (OrthogonalizeIteration dispatch)
  - palace/linalg/iterative.cpp:620-633 (GMRES Arnoldi call site)
  - palace/linalg/iterative.cpp:806-812 (FGMRES Arnoldi call site)
  - palace/models/romoperator.cpp:51-66 (ROM OrthogonalizeColumn sibling dispatch)
  - palace/utils/labels.hpp:165-170 (enum class Orthogonalization)
  - test/unit/test-orthog.cpp:82-120 (dispatch wrapper + empty-basis TEST_CASE)
  - codemap get_call_sites: OrthogonalizeColumnMGS (3 sites), OrthogonalizeColumnCGS (6 sites)
---

# CYCLE: Audit orthogonalize-mutation-rotation

## Summary

Audited the cycle-013 `firm/structural` L1>L0 theme `orthogonalize-mutation-rotation`
against Palace source via `palace-codemap`, with independent `read_range` confirmation of
every cited range plus the recognition-set closure (`get_call_sites` + the enum
definition). **Verdict: CONFIRMS-WITH-REFINEMENT.** All three sub-pattern L0 forms (MGS
single interleaved loop, CGS split two-phase, CGS2 doubled two-phase) appear verbatim at
their cited ranges; the in-place `w` mutation + raw-`H` write + inner-product-reduction
semantics are faithfully rebound; the m×1 / 1×m / 2×m collective-shape distinction is read
directly off the bodies (not reconstructed); and the recognition set is provably exhaustive
(the `Orthogonalization` enum has exactly 3 variants, every production call flows through
one of two dispatch switches, CGS2 is the `refine=true` parametrization of CGS — no fourth
free function). The refinements are all anchor-precision items, NOT semantic defects: one
enclosing-range citation should be tightened to the precise line, the L1-form comment is
cited at a line that is correct under the codemap's `read_range`/`get_symbol_def` numbering
(the earlier cycle-013 critic line-drift was already repaired and re-verifies clean here),
and one applicability-condition cites a call site one line off. The `firm` status is
upheld.

## Per-citation audit

### Sub-pattern A — MGS

- **Citation**: `palace/linalg/orthog.hpp:41-53`
- **Theme claim**: `OrthogonalizeColumnMGS` is a single `j`-loop doing dot → `GlobalSum(1)`
  → in-place `w.Add(-H[j], V[j])`, interleaved so iter `j`'s `w.Add` is read by iter `j+1`'s
  dot; collective shape `m`×size-1.
- **Found**: `read_range :41-53` returns exactly the signature (`:41-43`), `MFEM_ASSERT`
  (`:45`), and the single `for (std::size_t j = 0; j < m; j++)` body containing
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])`. The
  `GlobalSum` is size-1 (`Mpi::GlobalSum(1, &H[j], comm)`); the loop carries the in-place
  `w` mutation across iterations.
- **Verdict**: **supports**.
- **Notes**: `get_symbol_def` confirms the function definition spans `:41-53` exactly. The
  interleaving claim (iter `j` writes `w`, iter `j+1` dots the updated `w`) is correct — the
  `w.Add` precedes the next iteration's `dot_op(w, ...)` in the same loop body.

### MGS comment citation

- **Citation**: `palace/linalg/orthog.hpp:48`
- **Theme claim**: line 48 is `// Global inner product: Note order is important for complex
  vectors.`
- **Found**: under the codemap `read_range`/`get_symbol_def` numbering (line 41 = the
  `inline void OrthogonalizeColumnMGS` signature), the comment falls at **:48**, immediately
  above `H[j] = dot_op(w, V[j])`. Confirmed by reading `:41-53`: the comment is the line
  before the dot.
- **Verdict**: **supports**.
- **Notes**: The cycle-013 critic flagged citation line-drift here and it was repaired; the
  repair re-verifies clean. (A naive whole-file read that collapses leading
  blank/comment/`#include` lines reports a few-line-lower offset — this is a read-tool
  alignment artifact, NOT a citation error. The authoritative `read_range`/`get_symbol_def`
  numbering matches the theme's cited line.)

### Sub-pattern B — CGS (refine=false path)

- **Citation**: `palace/linalg/orthog.hpp:57-74`
- **Theme claim**: `OrthogonalizeColumnCGS` has an `m == 0` early return, then phase-1
  `m`-local-dot loop against the original `w`, a single `Mpi::GlobalSum(m, H, comm)`, then a
  phase-2 `m`-`w.Add` loop; collective shape 1×size-`m`; the two-phase split is the absence
  of MGS interleaving; the early return is the empty-basis law.
- **Found**: `read_range :57-74` returns signature (`:57-59`, with the `bool refine = false`
  default param), `MFEM_ASSERT` (`:61`), `if (m == 0) { return; }` (`:62-65`), first
  `for`-loop `H[j] = dot_op(w, V[j])` (`:66-69`), `Mpi::GlobalSum(m, H, comm)` (`:70`),
  second `for`-loop `w.Add(-H[j], V[j])` (`:71-74`). All `m` dots are taken against the
  unmodified `w` before any `w.Add` — the per-`j` independence is real.
- **Verdict**: **supports**.
- **Notes**: `:57-74` is the refine=false portion; the function definition actually spans
  `:57-89` (`get_symbol_def`), with `:75-89` being the refine block (sub-pattern C). The
  theme's split of the single function into two citation ranges (B = `:57-74`, C = `:75-88`)
  is a faithful structural decomposition. The `GlobalSum(m, H, comm)` is a single size-`m`
  reduction — collective shape 1×size-`m` confirmed.

### Sub-pattern C — CGS2 (refine block)

- **Citation**: `palace/linalg/orthog.hpp:75-88` (theme body) / `:75-88` (verified-against
  list) — and the task-cited anchors `H[j] += dH[j]` at `:85`, signedness loop at `:78`.
- **Theme claim**: the `if (refine)` block allocates `dH` scratch, runs a second
  `m`-local-dot loop against the once-orthogonalised `w`, a second
  `Mpi::GlobalSum(m, dH.data(), comm)`, then a fused accumulate-and-update loop
  `H[j] += dH[j]; w.Add(-dH[j], V[j])`; collective shape 2×size-`m`; not algebraically
  fusible (reads the first pass's output).
- **Found**: `read_range :75-89` returns `if (refine)` (`:75`), `std::vector<ScalarType>
  dH(m)` (`:77`), the signedness loop `for (int j = 0; j < m; j++)` (`:78`), second dot loop
  body `dH[j] = dot_op(w, V[j])` (`:80`), `Mpi::GlobalSum(m, dH.data(), comm)` (`:82`),
  accumulate loop `for (std::size_t j ...)` (`:83`), `H[j] += dH[j]` (`:85`),
  `w.Add(-dH[j], V[j])` (`:86`). The function closing brace is at `:89`.
- **Verdict**: **supports**.
- **Notes**: All task-cited fine-grained anchors land exactly: `H[j] += dH[j]` IS at **:85**
  and the `for (int j ...)` signedness loop IS at **:78**. The accumulate-into-caller's-`H`
  (`H[j] += dH[j]`, so returned coefficients = `H + dH`) is real and grounds the `algebraic`
  justification kind. The theme's body cites the C range as `:75-88`; the actual block runs
  `:75-89` (the `:89` is the function-closing brace `}`). Minor: extending the C range to
  `:75-89` would include the closing brace — a one-line tightening, not a defect (the
  load-bearing content `:75-87` is fully inside the cited `:75-88`).

### Dispatch wrapper (OrthogonalizeIteration)

- **Citation**: `palace/linalg/iterative.cpp:307-325`; CGS2 line cited as `:321-323`.
- **Theme claim**: `OrthogonalizeIteration` `switch`es over MGS/CGS/CGS2, forwards `j + 1`
  as `m`, and `CGS2 = OrthogonalizeColumnCGS(comm, V, w, Hj, j + 1, true)`.
- **Found**: `read_range :307-325` returns the template wrapper: signature (`:307-310`),
  comment "Orthogonalize w against the leading j + 1 columns of V." (`:312`), the `switch`
  (`:313`) with `MGS → OrthogonalizeColumnMGS(comm, V, w, Hj, j + 1)` (`:316`), `CGS →
  OrthogonalizeColumnCGS(..., j + 1)` (`:319`), `CGS2 → OrthogonalizeColumnCGS(..., j + 1,
  true)` (**:322**). All three forward `j + 1`.
- **Verdict**: **supports** (with anchor-precision refinement).
- **Notes**: The precise CGS2 line is **:322**, not the enclosing `:321-323`. The
  enclosing-range cite is correct-but-loose; tighten to `:322` for the no-drift assertion.

### GMRES Arnoldi call site

- **Citation**: `palace/linalg/iterative.cpp:629-632` (theme) / `:630` (dispatch),
  `:631-632` (normalise), `:622` (distinct candidate slot).
- **Theme claim**: `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` followed by
  `Hj[j+1] = Norml2(comm, w); w *= 1.0/Hj[j+1]` — confirms normalisation is the caller's
  (condition 3) and the candidate `w = V[j+1]` is a distinct slot (condition 4).
- **Found**: `read_range :620-633`: `VecType &w = V[j + 1]` (**:622**), `ScalarType *Hj =
  H.data() + j * (max_dim + 1)` (`:628`), `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj,
  j)` (**:630**), `Hj[j + 1] = linalg::Norml2(comm, w)` (**:631**), `w *= 1.0 / Hj[j + 1]`
  (**:632**).
- **Verdict**: **supports**. All sub-anchors (`:622`, `:630`, `:631-632`) land exactly.

### FGMRES Arnoldi call site

- **Citation**: `palace/linalg/iterative.cpp:808-811`.
- **Theme claim**: second consumer of the dispatch wrapper, same dispatch→normalise pattern.
- **Found**: `read_range :806-812`: `ScalarType *Hj = H.data() + j * (max_dim + 1)`
  (`:808`), `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` (**:809**), `Hj[j + 1] =
  linalg::Norml2(comm, w)` (**:810**), `w *= 1.0 / Hj[j + 1]` (**:811**).
- **Verdict**: **supports**. The cited range `:808-811` is exact.

### ROM sibling dispatch

- **Citation**: `palace/models/romoperator.cpp:51-66`.
- **Theme claim**: `OrthogonalizeColumn` sibling dispatch forwards `j` (not `j + 1`) and
  threads the `dot_op` hook (B-weighted inner-product consumer; third call-site family).
- **Found**: `read_range :51-66`: signature with `const InnerProductW &dot_op = {}`
  (`:51-53`), comment "Orthogonalize w against the leading j columns of V." (`:55`),
  `switch` with `MGS → ...(comm, V, w, Rj, j, dot_op)` (`:59`), `CGS → ...(comm, V, w, Rj,
  j, false, dot_op)` (`:62`), `CGS2 → ...(comm, V, w, Rj, j, true, dot_op)` (`:65`). Forwards
  `j` and the `dot_op` hook — confirmed.
- **Verdict**: **supports**.

### Empty-basis test

- **Citation**: `test/unit/test-orthog.cpp:99-120`.
- **Theme claim**: empty-basis edge — all three variants leave `w` unchanged at `m = 0`
  (sub-pattern B's `if (m == 0) return;` + the MGS/CGS2 zero-iteration loops both witness law
  3).
- **Found**: `read_range :99-120`: `TEST_CASE("OrthogonalizeColumn - Real Empty", ...)`
  (`:99`), `GENERATE(orthogonalize_wrapper(MGS), ...(CGS), ...(CGS2))` (`:101-103`), empty
  `std::vector<Vector> V{}` (`:107`), `orthogonalize_fn(Mpi::World(), V, w, H, 0)` (`:118`),
  `CHECK_THAT(w, RangeEquals(w_orig))` (`:120`).
- **Verdict**: **supports**. The test exercises all three variants at `m = 0` and asserts
  `w` unchanged — direct L0-equivalent witness of the empty-basis identity law.

## Applicability conditions

1. **No observer of prior `w` after the call.** Verifiable from `iterative.cpp:630-632`
   (GMRES) and `:809-811` (FGMRES): the only post-orthogonalise reads of `w` are
   `Norml2(comm, w)` and `w *= 1/Hj[j+1]`, both consuming `w'`. No counter-example among the
   two production call families. The ROM site (`romoperator.cpp:51-66`) is the dispatch
   wrapper, not a consumer; the consumer-side discard would need a separate audit of the ROM
   greedy loop, but the theme's claim is scoped to GMRES/FGMRES and holds there.
   **Counter-example found? No (in audited scope).**
2. **Caller owns/sizes the `H` buffer.** Verifiable: `ScalarType *Hj = H.data() + j *
   (max_dim + 1)` at `iterative.cpp:628` / `:808` shows the caller computes the Hessenberg-
   column slice pointer; the `MFEM_ASSERT(m <= V.size())` (orthog.hpp:45/:61) guards the `V`
   read only, not the `H` write — exactly as the theme states. **Counter-example? No.**
3. **Basis normalised; output not.** Verifiable from the header contract
   (`orthog.hpp:21-22`: "Assumes that the input vectors are normalized, but does not
   normalize the output vectors!") + the caller's `Norml2`/`*=` at `:631-632` / `:810-811`.
   **Counter-example? No.** (Note the theme cites the header contract as `:18-23`; the actual
   prose runs `:18-23` in codemap numbering — confirmed in the full read.)
4. **No aliasing in `w.Add(-h, V[j])`.** Verifiable: `VecType &w = V[j + 1]`
   (`iterative.cpp:622`) — the candidate is slot `j+1`, the orthogonalised columns are
   `0..j`, so `w` does not alias any read `V[j]`. **Counter-example? No.**
5. **Single-rank collapse of MPI reduction.** Per CLAUDE.md (MPI out of scope, `GlobalSum`
   collapses to a local sum). The collective shape (m×1 / 1×m / 2×m) is recorded as a
   per-sub-pattern property that does not change the lowered value. Verifiable directly from
   the `Mpi::GlobalSum` call counts/sizes read off the three bodies. **Counter-example? N/A
   (out of scope, flagged once as required).**

All five conditions are verifiable from the cited evidence and no counter-example surfaced
in the audited scope.

## Algebraic laws (cited)

- **CGS2 accumulate law `H_returned = H + dH`** (sub-pattern C, `algebraic` justification).
  **Holds on operators?** Yes. `orthog.hpp:85` is literally `H[j] += dH[j]` — the caller's
  `H` slot accumulates the second-pass correction `dH[j]`, so on return `H` holds the full
  projection `H + dH`. The `dH` is a transient `std::vector<ScalarType>` (`:77`) not exposed
  at L1, matching the L1 form returning only the summed `H`. The "twice is enough"
  re-application reads the once-orthogonalised `w` (`dH[j] = dot_op(w, V[j])` at `:80`, after
  the phase-2 `w.Add` loop at `:71-74`), so it is genuinely a second pass — not algebraically
  fusible with the first under floating-point (the idempotence law that exact arithmetic
  would collapse). The signature `OrthogonalizeColumnCGS(..., bool refine, ...)` carries the
  CGS↔CGS2 selector, so the law is realised by the same operator under the `refine=true`
  parametrization — consistent with the dispatch (`iterative.cpp:322`: `CGS2 = ...(true)`).
- **Empty-basis identity law `orthogonalize(w, [], variant) = (w, [])`** (sub-pattern B,
  `structural`). **Holds on operators?** Yes. CGS's `if (m == 0) { return; }`
  (`orthog.hpp:62-65`) is an explicit early return leaving `w` untouched; MGS and the CGS2
  refine block both have `for (... j < m ...)` loops that execute zero iterations at `m = 0`.
  The unit test (`test-orthog.cpp:99-120`) asserts all three variants leave `w` unchanged —
  empirical confirmation across the variant axis.

## Recognition-set closure (exhaustiveness)

The theme asserts the MGS/CGS/CGS2 recognition set is exhaustive. **Re-verified and
confirmed closed:**

- `enum class Orthogonalization : char { MGS, CGS, CGS2 }` (`palace/utils/labels.hpp:165-170`)
  — exactly three variants, no fourth.
- `get_call_sites(OrthogonalizeColumnMGS)` → 3 sites: `iterative.cpp:316`,
  `romoperator.cpp:59`, `test-orthog.cpp:87`.
- `get_call_sites(OrthogonalizeColumnCGS)` → 6 sites: `iterative.cpp:319`,
  `iterative.cpp:322`, `romoperator.cpp:62`, `romoperator.cpp:65`, `test-orthog.cpp:90`,
  `test-orthog.cpp:93`.
- Total 3 MGS + 6 CGS = matches the cycle-013 critic count exactly.
- Every non-test site is inside one of the two production dispatch switches:
  `OrthogonalizeIteration` (`iterative.cpp:316/319/322`) and `OrthogonalizeColumn`
  (`romoperator.cpp:59/62/65`). The three test sites (`test-orthog.cpp:87/90/93`) are inside
  the test harness's own `orthogonalize_wrapper` switch (`test-orthog.cpp:84-94`). No free
  function is called outside a 3-way dispatch switch.
- CGS2 is NOT a separate free function — it is `OrthogonalizeColumnCGS(..., refine=true)`.
  The theme correctly characterises it as the doubled parametrization of CGS.

Conclusion: the recognition set is provably complete; there is no unaccounted L0 variant.

## Reduction-ordering / collective-shape characterisation

The theme characterises the m×1 (MGS) / 1×m (CGS) / 2×m (CGS2) reduction shapes as
load-bearing. **Confirmed correct and correctly classified:**

- MGS: `Mpi::GlobalSum(1, &H[j], comm)` inside the loop (`orthog.hpp:49`) → `m` reductions
  of size 1.
- CGS: `Mpi::GlobalSum(m, H, comm)` once (`orthog.hpp:70`) → 1 reduction of size `m`.
- CGS2: CGS's single size-`m` plus a second `Mpi::GlobalSum(m, dH.data(), comm)`
  (`orthog.hpp:82`) → 2 reductions of size `m`.

The shapes are read directly off the bodies (no reconstruction). They are correctly framed
as a load-bearing collective-shape / numerical-stability property (interleaved sequential
dependency for MGS vs. batched independence for CGS vs. the doubled stabilising pass for
CGS2) that does NOT change the single-rank lowered value but DOES distinguish the three L0
loop structures and their parallel cost models — a faithful application of the "load-bearing
numerical tricks" classification (CLAUDE.md §Optimization tricks vs. base algebra). This is
the theme's stated load-bearing axis and it holds.

## Proposed changes

The audit is **CONFIRMS-WITH-REFINEMENT**. The `firm` status is upheld; the refinements are
anchor-precision tightenings (no semantic defect). A follow-up `lifter`/`abstractor`
dispatch should apply the two precision tightenings and append the `verified_against:`
block. **Do NOT mutate `book/` in this audit dispatch.**

Refinements (anchor precision; route to a cycle-014/015 follow-up dispatch):
- **R1** — In sub-pattern C's dispatch citation, tighten `iterative.cpp:321-323` to the
  precise line **`iterative.cpp:322`** (`CGS2 = OrthogonalizeColumnCGS(comm, V, w, Hj, j + 1,
  true)`). The enclosing range is correct-but-loose.
- **R2** — Optionally extend sub-pattern C's body-citation `orthog.hpp:75-88` to `:75-89` to
  include the function-closing brace (or leave as-is; the load-bearing content `:75-87` is
  fully inside `:75-88`). Cosmetic; not required for correctness.

Append (after the follow-up applies R1; emitted as a fenced YAML block inside the theme):

```edit:book/src/L1-L0/orthogonalize-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/orthog.hpp:41-53
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: OrthogonalizeColumnMGS single interleaved loop; def spans 41-53 per get_symbol_def
  - citation: palace/linalg/orthog.hpp:48
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: complex-order comment; cycle-013 line-drift repaired, re-verifies clean
  - citation: palace/linalg/orthog.hpp:57-74
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: CGS refine=false; m==0 early return at 62-65, single GlobalSum(m) at 70
  - citation: palace/linalg/orthog.hpp:75-88
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: CGS2 refine block; H[j]+=dH[j] at 85, signedness loop at 78, 2x GlobalSum(m)
  - citation: palace/linalg/iterative.cpp:307-325
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: OrthogonalizeIteration dispatch; CGS2=...(true) precise line is 322 (R1)
  - citation: palace/linalg/iterative.cpp:629-632
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: GMRES Arnoldi; w=V[j+1] at 622, dispatch 630, normalise 631-632
  - citation: palace/linalg/iterative.cpp:808-811
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: FGMRES Arnoldi; same dispatch-then-normalise pattern, exact
  - citation: palace/models/romoperator.cpp:51-66
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: ROM sibling dispatch; forwards j (not j+1) and threads dot_op hook
  - citation: palace/utils/labels.hpp:165-170
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: enum Orthogonalization {MGS,CGS,CGS2} — recognition set provably exhaustive
  - citation: test/unit/test-orthog.cpp:99-120
    verdict: supports
    audited_at: 2026-05-28T19:33:06Z
    note: empty-basis edge; all 3 variants leave w unchanged at m=0
~~~
```

(The `~~~` triple-tilde represents the triple-backtick fence in the actual file; emit as
triple-backticks.)

## Supporting evidence

Files consulted (all via `palace-codemap`, paths relative to `reference/palace/`):
- `palace/linalg/orthog.hpp:1-95` (full header read), then precise re-reads `:41-53`,
  `:57-74`, `:75-89` — the three free-function bodies.
- `palace/linalg/iterative.cpp:307-325` (dispatch), `:620-633` (GMRES), `:806-812` (FGMRES).
- `palace/models/romoperator.cpp:51-66` (ROM sibling dispatch).
- `palace/utils/labels.hpp:165-170` (`enum class Orthogonalization`).
- `test/unit/test-orthog.cpp:82-98` (test-harness dispatch wrapper), `:99-120` (empty-basis
  TEST_CASE).
- `get_symbol_def(OrthogonalizeColumnMGS)` → `orthog.hpp:41-53`;
  `get_symbol_def(OrthogonalizeColumnCGS)` → `orthog.hpp:57-89`.
- `get_call_sites(OrthogonalizeColumnMGS)` → 3 sites; `get_call_sites(OrthogonalizeColumnCGS)`
  → 6 sites (recognition-set closure).
- `search_text("enum class Orthogonalization")` → `labels.hpp:165`.

## Open questions / caveats

- **Direction-of-definition: clean.** The theme narrates the rewrite forward (L1 LHS → L0
  RHS): "Lowers the pure L1 form ... into Palace's ... L0 free functions." No reverse-lift
  narration in the formal content. No high→low violation.
- **Applicability condition 1 (no prior-`w` observer) audited only for GMRES/FGMRES.** The
  theme scopes its lexical proof to those two sites (`iterative.cpp:630-632` / `:809-811`).
  The ROM consumer (the greedy-sampling loop that calls `romoperator.cpp:OrthogonalizeColumn`)
  was NOT audited for prior-`w` discard — `romoperator.cpp:51-66` is the dispatch wrapper, not
  the consumer. This is not a defect in the theme (its claim is scoped to GMRES/FGMRES), but a
  future audit of the ROM greedy loop could extend condition-1 coverage to the third call
  family. Logged here as an audit-scope caveat, not a refutation.
- **`read_range` vs whole-file line numbering.** A whole-file `read_range :1-95` returns text
  offset by a few lines relative to `get_symbol_def`/targeted `read_range` (the tool appears
  to collapse leading license/`#include` lines in the bulk read). The AUTHORITATIVE numbering
  is `get_symbol_def` + targeted `read_range`, which agrees with the theme's citations. This
  is the same alignment artifact that produced the cycle-013 critic's apparent "line-drift"
  finding; the repaired citations are correct under the authoritative numbering. Flagged so a
  future auditor does not re-open a phantom drift: prefer `get_symbol_def` bounds + targeted
  `read_range` over bulk reads for this header.
- **No `book/` mutation performed** (audit-only dispatch, per scope). R1/R2 + the
  `verified_against:` block are proposed for a follow-up dispatch.
