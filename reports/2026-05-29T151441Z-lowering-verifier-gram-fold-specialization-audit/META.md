---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T15:32:25Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T16:05:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Audit gram-fold-specialization" (lowering-verifier audit, cycle-025 dispatch 7)

## Critique

### Checks run

**citation-validity — pass.** This is the load-bearing axis for an audit report and I re-ran it
mechanically rather than re-reading by hand. `citecheck.py --scan` on the CYCLE.md reports **53 ok,
3 failing — but all 3 failures are `[AMBIG]` (bare-basename) hits, NOT bounds failures**:
`dot.md:43`, `dot.md:49` (basename matches `L1/dot.md`, `L3/dot.md`, `concepts/dot.md`), and
`operator.cpp:621-638` (matches `linalg/operator.cpp` + `fem/libceed/operator.cpp`). These are
prose shorthand that the report *also* writes in full-path form elsewhere (e.g. the §dispatch and
Verified-against blocks use `book/src/L1/dot.md:43` and `palace/linalg/operator.cpp:621-638`), so
the canonical citation exists and resolves; the bare forms are a readability convenience, not
missing/out-of-range citations. **Every full-path range is in bounds.** I then ran the three
load-bearing `--anchor` spot-checks the dispatch named, all against `reference/palace/`:
  - `palace/linalg/nleps.cpp:529 --anchor 'linalg::Dot(GetComm(), X[i], X[j])'` → **OK**, anchor at
    529. The headline XHX cell body is exact, and `search_text`-confirmed sole occurrence.
  - `palace/linalg/vector.cpp:668 --anchor 'MFEM_ASSERT(x.Size() == y.Size()'` → **OK** at 668;
    `palace/linalg/vector.cpp:667` with the same anchor → **`[DRIFT] +1, suggested :668`** (`:667`
    is `static hypre::HypreVector X, Y;`). The tool — the authoritative line-map — confirms the
    report's `:667→:668` finding with the corrected line in hand. Real.
  - `palace/linalg/nleps.cpp:614 --anchor 'X.resize(k + 1)'` → **OK** at 614; `:613` → `eigs[k] =
    eig;`. Confirms the `:613-619 → :614-619` enclosing-range looseness (off-by-one at the low
    boundary; in-bounds, value-faithful). Real.
  I additionally `--show`-read `vector.cpp:263-266` (conjugation kernel `Re=xr·yr+xi·yi`,
  `Im=xi·yr−xr·yi` = `x·conj(y)=yᴴx`, arg-2 conjugated) and `nleps.cpp:524-535` (build loop +
  complex LU-solve consumer) and `:515-518` (k==0 early-return) — all match the report verbatim. The
  conjugation chain `nleps.cpp:529 → vector.cpp:265-266 → dot.md:43` resolves and the no-op re-order
  identity `X[j]ᴴX[i] = X[j]ᴴX[i]` is sound. Both reported anchor-precision findings are real; both
  are anchor-precision, not content contradictions. Pass.

**surface-or-evidence — pass.** This is a lowering-verifier AUDIT, not a refinement of operator/theme
surface. The proposed changes are (1) an additive `verified_against:` evidence block (13 citations
with per-citation verdicts), (2) a bounded inherited-citation correction (`:667→:668` at two
in-theme lines), and (3) an optional precise-range refinement. This is the canonical
retroactive-evidence-backfill shape the check explicitly allows. No new rotation_claim, no surface
rewrite. Pass.

**rotation-quality — pass.** The dispatch asked me to confirm the matrix specialization
GENERALIZES rather than DUPLICATES the sibling scalar `inner-product-fold-specialization`. I read
the sibling §"The dispatch rewrite" (`:92-136`): the scalar theme dispatches a *single* leaf via
three orthogonal keys (conjugation / element-type / weight). The gram theme inherits those three
keys pointwise and adds genuinely matrix-specific content with **no scalar analogue**: the
double-loop cartesian materialization over two basis index axes (`k²` cells), the
symmetry-exploitation triangle-mirror transparent note, the `k²`-independent-per-cell-tree (vs
fused-GEMM) structural fact, and the Hermitian-symmetry interaction `G[j,i]=conj(G[i,j])`. Different
L2 LHS (`Scalar` vs `Matrix[k,k]`), different result rank, different consumer (`deflate` Gram-solve
vs Krylov coefficients). This is a strict generalization (the scalar theme is the `k=1` degeneration),
not a 1:1 renaming. The report's GENERALIZES-not-DUPLICATES verdict is correct. Pass.

**variant-axis-coverage — pass.** The gram operator's variant axes (hook ∈ {canonical Hermitian,
B-weighted}; single-set vs cross-Gram `gram2`; element-type real/complex) are each addressed by the
audit: the report walks the dispatch table covering the canonical-Hermitian arm (NLEPS, fully
exercised), the B-weighted arm (scoped as `bilinear-form` rough-in, structurally firm but not
NLEPS-exercised — explicitly scoped, not hidden), the cross-Gram `gram2` (a two-index-set
degeneration, dispatch-identical), and the real-vs-complex element-type split. The `tdot`
unconjugated arm is explicitly flagged as type-API-surface-only (zero call sites) — scoped, not
hidden. No hidden branches. Pass.

**cross-reference-integrity — pass.** I confirmed the theme is wired into `book/src/SUMMARY.md:57`
and the `book/src/L2-L1/index.md:17` theme-list row (both present and naming the slug). All `[link]`
references in the audited theme resolve (`../L2/gram.md`, `./inner-product-fold-specialization.md`,
`../L1/dot.md`, `../L1/bilinear-form.md`, `../L2/inner_product.md` all exist). The
build-readiness fence guard does NOT apply: this is an audit report whose proposed-changes are a
small `verified_against:` YAML block + two one-line citation corrections — no `firm`-chapter body is
being authored, so the cycle-019 fence-truncation defect is structurally impossible here (the
report uses the `~~~`-stands-for-backtick convention and explicitly says "emit as triple-backticks",
which the integrator handles at apply time). I note one mechanical caveat for the integrator below
(the nested-fence inside the `edit:` block) but it is not a cross-reference failure. Pass.

**edge-label-fidelity — pass.** The theme carries the L2>L1 edge label. The report's prose discusses
exactly that edge throughout — the L2 all-pairs fold (`gram`) lowering into the L1 per-cell leaf grid
(`dot`/`bilinear-form`), narrated forward L2→L1 per the high→low discipline. The reverse-direction
lifting note is correctly quarantined to §Open questions / working notes, not the edge narration. No
edge mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit with verdict
**fully-supported**, no status change (theme stays `firm`). The content shape matches: per-citation
verdicts, applicability-condition walk, law-by-law check, forward-reference-closure confirmation,
and an additive evidence block. The two anchor-precision findings are correctly classified as
precision matters (NOT contradictions → NOT a status reduction), consistent with the
fully-supported verdict. The audit does not over-claim (it does not mark the theme `firm` on the
strength of the constructive sub-parts; the firmness rests on the positive Gram-build site + the
firm sibling, as the theme already states). Kind matches content. Pass.

**skill-uptake-survey — pass.** The report explicitly invokes the mechanical citecheck realization
(`tools/citecheck/citecheck.py --anchor/--show/--scan`) per the cycle-024 `verify-citation-range`
extension, and references its lowering-verifier role-spec lints by name
(`lifter-scope-content-correction-boundary`, `audit-report-inherited-miscitation-lint`). The
skill surface implied by an audit shape (citation-range verification) is referenced and used. Pass.

### Issues found

No blocking issues. The audit is well-grounded; both of its anchor-precision findings independently
reproduce under the citecheck tool. The items below are the report's own findings (corroborated) plus
minor integrator-routing notes — none reduces the theme's firm status or blocks the additive
evidence block.

1. **[CORROBORATED — route to siblings, do NOT block this report] Inherited `vector.cpp:667 → :668`
   carry-forward drift.** The audited theme cites `palace/linalg/vector.cpp:667` for the
   `MFEM_ASSERT(x.Size() == y.Size())` aligned-pass precondition at two sites
   (`gram-fold-specialization.md:60` and `:240`); the assert is at `:668` (`:667` is `static
   hypre::HypreVector X, Y;`). Confirmed via `citecheck --anchor` (`[DRIFT] +1, suggested :668`). I
   independently `grep`-confirmed the report's claimed cohort scope: the same `:667` drift is present
   in `book/src/L2/inner_product.md:360`, `book/src/L2-L1/inner-product-fold-specialization.md:59` and
   `:260`, in addition to this theme's `:60`/`:240`. Notably `book/src/L1-L0/dot-mutation-rotation.md:269`
   already cites the **correct** `:668` — corroborating that this is a localized carry-forward in the
   inner-product/gram cohort, not a tree-wide error. **This is a finding the integrator should route
   to the sibling/parent files (a follow-up `lifter`/`repairer` sweep or carry-forward correction),
   NOT a defect that blocks THIS report** — the report correctly proposes the two in-theme fixes and
   recommends (not actions) the cross-file sweep, staying inside dispatch-phase write discipline. Where:
   CYCLE.md §"vector.cpp:667 — the aligned-pass precondition" (lines 124-129), Proposed change (2)
   (lines 297-312), Open questions (lines 351-356). Severity: low (anchor precision; construct exists
   and claim is correct at the right line).

2. **[CORROBORATED — non-blocking] Enclosing-range looseness `nleps.cpp:613-619 → :614-619`.**
   `:613` is `eigs[k] = eig;` (related but distinct); the basis-growth constructs the theme cites
   (`X.resize`, `X[k]=v`, `H.conservativeResizeLike`, `H(k,k)=eig`, `k++`) all fall within `:614-619`.
   Confirmed via `--anchor 'X.resize(k + 1)'` at 614 and `--show :613`. In-bounds and value-faithful;
   the report classifies it as a precise-range refinement (verdict `partially-supports` in the
   evidence block), not a contradiction. Where: CYCLE.md §"nleps.cpp:613-619" (lines 91-96),
   Proposed change (3) (lines 314-319). Severity: low (cosmetic range tightening).

3. **[CORROBORATED] Forward-reference closure is real; one text residual remains.** The
   `gram.md:242-246` content forward-reference names four content pieces; I read `gram.md:160-246`
   and confirm the theme delivers all four (cell-dispatch, symmetry note, per-cell reduction tree,
   the `nleps.cpp:524-531` loop). The report's closure verdict is sound. **Residual the report
   correctly flags:** the `gram.md` prose still literally says "(forthcoming)" at `:176` and
   "(forthcoming; abstractor work — not authored here)" at `:242-246` — a *text* refresh (name
   `gram-fold-specialization`, drop "forthcoming"), correctly routed as a follow-up to
   layer-intro-author/lifter (not actioned here, since `gram.md` is not this dispatch's file and
   editing it would breach dispatch-phase write discipline). Where: CYCLE.md §"Forward-reference
   closure" (lines 184-210), Open questions (lines 341-349). Severity: informational (a tracked
   follow-up, not a defect in this report).

4. **[scope confirmation — proposed changes are additive/surgical] `verified_against:` block scope.**
   The 13-citation block is purely additive (append-at-end), the `:667→:668` correction is two
   surgical one-line replacements within this theme, and the range refinement is optional. I confirm
   the scope is additive/surgical with no surface rewrite, no status change, no rotation claim — the
   audit does not author content. One mechanical note for the integrator (NOT a content issue): the
   Proposed-change (1) `edit:` block contains a nested `~~~yaml` fence standing in for the inner code
   fence (the report flags this explicitly at lines 235-236, "emit as triple-backticks"). The
   integrator should apply the inner block as a real triple-backtick `yaml` fence; this is the
   known nested-fence handling (cf. the cycle-024
   `convert-nested-fences-to-indented-code-in-proposed-changes-block` repair skill), surfaced here so
   the integrator does not paste the `~~~` literally. Where: CYCLE.md Proposed changes (lines 230-319).
   Severity: low (mechanical apply-time handling).

5. **[noted, not flagged — benign] Sibling range-style inconsistency.** The gram theme cites
   `ComplexVector::Dot` as `vector.cpp:263-266` (signature+return) while the sibling uses `:263-267`
   (including the closing brace); and `:664-672` (with leading blank) in §dispatch vs `:665-672`
   (tight) in Verified-against. All four ranges are in-bounds and capture the construct (confirmed in
   the `--scan`). This is style, not drift — the report itself notes it as a future
   same-layer-cross-cutter normalization opportunity, not a defect. No action. Severity: none.

## Repair

The critic graded all 8 checks `pass`. There are no warning/fail findings to repair. This pass is
therefore the two **mechanical normalizations** the role-spec authorizes on an otherwise-clean
audit report — a nested-fence encoding fix and a stale-frontmatter fix — plus accountability for the
two corroborated anchor-precision findings (both stay as the report already proposes; nothing
substantive to author). `overall_status: ready`.

### Fixes attempted

- **Finding (mechanical, IMPORTANT — critic issue 4 / nested-fence):** Proposed-change (1)'s `edit:`
  block carried a nested `~~~yaml … ~~~` stand-in for the `verified_against:` block plus a prose
  instruction ("emit as triple-backticks") that the integrator would have had to interpret.
  - **Decision**: repaired.
  - **Action**: `reports/<id>/CYCLE.md` §"Proposed changes (1)" (lines 232–298). Per the cycle-024
    `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill, option (b) — converted
    the nested `~~~yaml` fence to a **4-space-indented** code block inside the `edit:` block (deleted
    the `~~~yaml` open + `~~~` close, indented every `verified_against:` content line by 4 spaces,
    preserved every citation/verdict/note byte-for-byte). Replaced the "emit as triple-backticks"
    prose with an unambiguous apply instruction (`[append at end of file; emit the indented block
    below as a ```yaml ... ``` fenced block]`) so the integrator lands a real ` ```yaml ` fence in the
    chapter without interpreting a `~~~` literal. Re-verified fences: `grep -c '^\`\`\`'` = 4 (2
    `edit:` blocks × 2, all paired); `grep '^~~~'` = none. The `verified_against:` leading text the
    downstream `cross-layer-cross-cutter` parser keys on is preserved (skill §"Note on
    `verified_against:` YAML blocks").
  - **Consistency sub-fix (within the same edit, surgical):** the `verified_against:` block's last
    entry recorded `citation: palace/linalg/vector.cpp:667` / `verdict: does-not-support`. Since
    Proposed-change (2) corrects the in-theme citations to `:668`, an appended evidence entry citing
    the now-removed `:667` would be internally inconsistent with the landed chapter. Rewrote it to
    `citation: palace/linalg/vector.cpp:668` / `verdict: does-not-support-at-cited-line-667` — same
    drift record (still names the `:667` error and the `static hypre::HypreVector X, Y;` line at
    `:667`), now pointing at the correct line. Mechanical consistency, no new claim.

- **Finding (critic issue 1 — `vector.cpp:667 → :668` inherited drift):** the
  `MFEM_ASSERT(x.Size() == y.Size())` aligned-pass precondition is at `:668`, not `:667`
  (`:667` is `static hypre::HypreVector X, Y;`).
  - **Decision**: not-needed (the report already proposes the correct fix; I confirmed it intact).
  - **Action**: re-verified mechanically via `citecheck --anchor`: `:667` → `[DRIFT] +1, suggested
    :668`; `:668` → `[ok]`. Confirmed Proposed-change (2) (`CYCLE.md:306–309`) replaces
    `vector.cpp:667` → `:668` at the **in-theme** sites `gram-fold-specialization.md:60` and `:240` —
    intact and correct, no edit needed. **Integrator routing note:** this is a SHARED carry-forward —
    the same `:667` drift lives in the sibling/parent files `book/src/L2/inner_product.md:360` and
    `book/src/L2-L1/inner-product-fold-specialization.md:59,260`, which are OUT of this report's scope
    (NOT edited here). Route a sibling sweep (a follow-up `lifter`/`repairer` carry-forward
    correction); the report already recommends this at `CYCLE.md:311–315` and OQ `:351–356`.

- **Finding (critic issue 2 — enclosing-range looseness `nleps.cpp:613-619 → :614-619`):** `:613` is
  `eigs[k] = eig;`; the cited basis-growth constructs all fall within `:614-619`. In-bounds,
  value-faithful.
  - **Decision**: not-needed (the report records it as an optional precise-range refinement; kept as
    recorded).
  - **Action**: re-verified via `citecheck --anchor 'X.resize(k + 1)'` at `:614` → ok; `--show :613`
    → `eigs[k] = eig;`. Confirms the off-by-one at the low boundary. The report's Proposed-change (3)
    (`CYCLE.md:317–322`) leaves it as an optional tightening at integrator discretion and the
    `verified_against:` block records it `partially-supports` — consistent, left as recorded.

- **Finding (stale frontmatter `verifies: ../REPORT.md`):** present at META.md:2.
  - **Decision**: repaired.
  - **Action**: `reports/<id>/META.md` frontmatter line 2 — changed `verifies: ../REPORT.md` →
    `verifies: ../CYCLE.md` (the per-dispatch file is `CYCLE.md`, renamed from `REPORT.md` at
    cycle-004).

- **Note (critic issue 3 — `gram.md:176,242` "(forthcoming)" text residual):** the forward-reference
  *content* IS delivered by this theme (the report confirms all four content pieces close); only the
  `gram.md` prose still literally says "(forthcoming)". This is a text-refresh follow-up on a file
  OUT of this report's scope (`gram.md` is not this dispatch's file). NOT chased here. The report
  already routes it as the new small OQ
  `gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization` (`CYCLE.md:341–349`).

### Unrepairable findings

None. No warning/fail finding from the critic; the two corroborated anchor-precision findings are
already correctly proposed by the report (in-theme fix + optional refinement), and the cross-file
carry-forward + `gram.md` text-refresh are correctly scoped as out-of-this-report follow-ups, not
defects in this report.

## Suggested resolution

`ready`. Notes for the integrator:

1. **Apply Proposed-change (1) as a real ` ```yaml ` fence.** The block is rendered 4-space-indented
   inside the `edit:` block (mis-toggle-proof); land it in
   `book/src/L2-L1/gram-fold-specialization.md` as a triple-backtick `yaml` fenced
   `verified_against:` block appended at end of file (the channel-format requirement
   `lowering-verifier-yaml-in-prose-channel-format`).
2. **Apply Proposed-change (2) in-theme** (`gram-fold-specialization.md:60` and `:240`,
   `vector.cpp:667` → `:668`). Then **route a sibling carry-forward sweep** (follow-up
   `lifter`/`repairer`) for the SAME `:667 → :668` drift in `book/src/L2/inner_product.md:360` and
   `book/src/L2-L1/inner-product-fold-specialization.md:59,260` — out of this report's scope, so not
   fixed here.
3. **Proposed-change (3)** (`nleps.cpp:613-619` → `:614-619`) is optional; integrator discretion.
4. **Follow-up text-refresh:** the `gram.md:176,242` "(forthcoming)" prose should be refreshed to
   name `gram-fold-specialization` (a `layer-intro-author`/`lifter` cross-reference refresh; tracked
   as OQ `gram-md-forward-ref-text-refresh-to-name-gram-fold-specialization`). Content is already
   closed; this is text-only and does not gate the theme's `firm` status.
5. No status change: the theme stays `firm`; both anchor-precision findings are precision matters,
   not contradictions.
