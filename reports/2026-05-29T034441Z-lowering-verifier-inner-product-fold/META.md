---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T041500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T043000Z
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

# META: verification of "Audit inner-product-fold-specialization"

## Critique

### Checks run

**citation-validity — warning.** THE CRUX of this audit. I independently `read_range`-verified
the contested `operator.cpp` anchors via BOTH the direct file `Read` and the `palace-codemap`
`read_range` (the two read paths agree exactly — no tool-numbering skew, which is itself worth
recording given the cycle-019/020 line-offset-drift signal). Ground truth (both paths):

| content | actual line |
|---|---|
| `// For SPD B, xᴴ B x is real.` (SPD comment) | **612** |
| `MFEM_ASSERT(dot.real() > 0.0 && ...)` (SPD assertion) | **616** (single line; `:615` is `std::complex<double> dot = Dot(comm, Bx, x);`) |
| real-`Operator` `ComplexVector Ax(A.Height());` | **624** |
| `ComplexOperator` `ComplexVector Ax(A.Height());` | **634** |

The verifier's *source* reads are all correct — every Palace L0 range it audited
(`vector.cpp:263-274`, `:664-685`; `vector.hpp:240-262`; `operator.cpp:598-617`,
`:621-628`, `:631-638`; `iterative.cpp:395`; `boundarymodeoperator.cpp:85,90`;
`nleps.cpp:487,492`; the `TransposeDot` zero-call-sites) reproduces faithfully against my
independent reads (`get_call_sites TransposeDot` → `[]` confirms zero callers exactly). The
math (the conjugate-pair re-order `xᴴ y = conj(yᴴ x)`, the `Dot`/`TransposeDot` sign tables,
the four-real-LocalDot tree) is sound per-line.

**The warning is on the verifier's characterization of the *theme's current state*, not on its
source reads.** The report repeatedly asserts the theme "says `:611`" for the SPD comment and
frames the `:611`→`:612` correction as one of "four inline-anchor drifts" (Summary; §operator.cpp
audit lines 122-139; Proposed-changes `audit_caveat`; Carry-forward item 3; OQ). **This is false
against the artifact as it stands.** The string `:611` appears NOWHERE in
`book/src/L2-L1/inner-product-fold-specialization.md`; the theme's §Verified-against block (line
372) already pins the SPD comment to `:612` — which is the correct value. So the verifier (a) is
right about ground truth (`:612`), but (b) mis-states what the theme currently asserts, turning a
no-op ("the theme is already correct here") into a phantom "drift" the integrator/lifter would be
told to "fix." The task framing's premise — that the verifier "directly contradicts what the
cycle-019 repairer pinned (`:611`)" — does not hold against the current file: whatever a prior
state pinned, the file now says `:612`, so there is no live contradiction to resolve; the
verifier is shadow-boxing a stale state. Net: 2 of the 4 claimed drifts are genuine, 1 is partial,
1 is a phantom. Hence `warning` (the soundness is intact but a follow-up consumer acting on the
report's drift list would touch an already-correct anchor).

**surface-or-evidence — pass.** Audit shape (read-only verification emitting a `verified_against:`
append; no operator/theme surface mutation). The three dispatch-arm verifications (conjugation
key via `Dot`/`TransposeDot`, element-type key via real/complex `LocalDot`, weight key via
weighted `Dot`), the conjugate-pair re-order soundness, and the summation-order table are each
backed by a verified L0 range. Retroactive-evidence-backfill framing is correct for an audit.

**rotation-quality — pass.** The audit correctly assesses that the L2→L1 lowering preserves
semantics: the L2 reduce-to-scalar `inner_product` fold lowers into three L1 leaf specializations
via a value-bearing dispatch; the re-order rule is value-bearing exactly where claimed (full
complex value, non-Hermitian off-diagonal — the `boundarymodeoperator.cpp:90` `Atn` witness) and
re-order-invisible where the value is real (CG `:395`, Poynting diagonal `:85`, abs-norms
`:487,492`). The compaction (state-free fold → pinned-tree leaves) is a genuine rotation, assessed
correctly.

**variant-axis-coverage — pass (not applicable to audit-shape).** The verifier nonetheless
exercised the relevant axes: real-vs-complex element type, Hermitian-vs-unconjugated kernel,
weighted-vs-unweighted, diagonal-vs-off-diagonal, Hermitian-vs-non-Hermitian weight — each with a
concrete witness or a no-counter-example finding. Applicability conditions 1-5 each carry a
verified witness.

**cross-reference-integrity — pass.** The proposed `verified_against:` block is a fenced
` ```yaml ` block (cycle-003 discipline) nested inside an `edit:` directive proposed as an append
(not a direct write) — well-formed. Slugs referenced (`dot`, `bilinear-form`, `inner_product`,
`mutable-workspace-pattern`, `matrix-weighted-norm`) resolve. The friction/precedent references
(`lifter-scope-content-correction-boundary`, the cycle-012 SLEPc-NEP `:387`→`:383` precedent,
`apply-linop-lowering-verifier-audit-cohort`) are coherent. One nit: the report's audited range
`operator.cpp:598-617` is one line narrower than the theme's own `:598-618` (line 369); both
enclose the content (618 = `return std::sqrt(dot.real());`), so this is cosmetic, not an error.

**edge-label-fidelity — pass.** Edge label L2>L1; the prose narrates the L2 `inner_product` fold
lowering forward into the L1 `dot`/`tdot`/`bilinear_form` leaves throughout. Direction-of-definition
is clean (the verifier itself confirms the reverse/lifting note is quarantined to working-note
§"Open questions / caveats"). No edge mislabel.

**plan-kind-consistency — pass.** Declared shape is an audit (`verdict: fully-supported` +
`status_recommendation: keep firm`). Content matches: read-only verification, no status change, no
content rewrite, only a metadata append + carry-forward corrections. The `partially-supports`
verdict on the `operator.cpp:598-617` row inside the yaml block is internally consistent with the
"semantic content fully supported, anchors drifted" framing.

**skill-uptake-survey — warning.** The report's shape (audit of cited ranges + an inherited
line-offset-drift finding) squarely implies `verify-citation-range` (extended cycle-012 with the
"Audit-report / inherited-citation sub-case" section — exactly this situation) and
`verify-rotation-citation`. The verdict-table / yaml-block discipline implies the
audit-emission convention. The report describes the read-range methodology in detail but does not
name any skill invocation. Pure telemetry (non-blocking) — but the inherited-anchor-drift sub-case
is precisely the one `verify-citation-range` was extended to cover, and applying its "compare the
report's claimed anchor against BOTH the source AND the current artifact state" step would have
caught the phantom `:611` drift before it reached the carry-forward list.

### Issues found

1. **Phantom `:611`→`:612` SPD-comment "drift" — citation-validity, severity: medium.**
   (CYCLE.md Summary line 33-39; §operator.cpp audit lines 122-139; Proposed-changes yaml
   `operator.cpp:598-617` note line 291 + `audit_caveat` line 322; Carry-forward item 3 line 334;
   OQ line 356-361.) The report asserts the theme pins the SPD comment to `:611` and that this
   drifted to `:612`. Independently verified: the theme file
   `book/src/L2-L1/inner-product-fold-specialization.md` line 372 **already says `:612`**, and
   `:611` appears nowhere in the file. Ground truth is `:612`. So this anchor is **already correct
   in the artifact** — there is no drift to carry forward. The report's repeated "theme/repairer
   says `:611`" is a misstatement of the current artifact state. A consumer (lifter/integrator)
   acting on the report's drift list would re-touch an already-correct line. The correct finding is
   "SPD comment `:612` — verified, no change." (The `status_recommendation` and `coverage_verdict`
   are unaffected; this is a defect in the carry-forward/caveat list, not the verdict.)

2. **Genuine `Ax` inline-anchor drifts — citation-validity, severity: low (the finding is
   correct; flagged for the repairer to act on, not as a report defect).** Theme line 142
   (`operator.cpp:623,632`) and line 363 (`:623`) pin the real-`Operator` `Ax` allocation to
   `:623` and the `ComplexOperator` one to `:632`. Ground truth: `:624` and `:634` respectively
   (line 623 = `{`, 624 = `ComplexVector Ax(A.Height());`; line 633 = `{`, 634 = the complex
   `Ax`). The verifier's correction is RIGHT here. These two are the substantive, actionable part
   of the carry-forward.

3. **Partial SPD-assertion range drift — citation-validity, severity: low.** Theme line 371 pins
   the SPD assertion to `:615-616`. Ground truth: the assertion is a **single line at `:616`**;
   line 615 is `std::complex<double> dot = Dot(comm, Bx, x);` (the preceding statement, not the
   assertion). The verifier's `:615-616`→`:616` correction is correct. Minor (the range over-
   covers by one adjacent code line; it does not point at wrong content), but the verifier's
   characterization is accurate.

4. **Self-dot fast-path anchor `:679`→`:678` — citation-validity, severity: trivial (self-flagged,
   correct).** (§vector.cpp audit lines 78-84; yaml note line 275.) Theme line 355 cites the
   complex `LocalDot` imag=0 self-dot return at `:679`; ground truth places the `{... , 0.0}`
   return at `:678` (inside the `if (&x == &y)` branch spanning `:676-679`). The verifier correctly
   notes this is within the fast-path span. Within tolerance; surfaced accurately.

5. **Dispatch-key-1 over-claim acknowledged but left in the yaml note — surface-or-evidence /
   accuracy, severity: trivial.** (§vector.cpp audit lines 60-66; yaml note line 267; OQ line
   363-370.) The theme's "the ONLY per-element difference is the sign of the imaginary cross-term"
   is imprecise — `TransposeDot` flips BOTH the real-part sign (`Re·Re − Im·Im` vs `Dot`'s `+`)
   AND the imag sign (verified `vector.cpp:271-273`). The verifier catches this correctly and
   correctly judges the *net* characterization (`x·conj(y)` vs `x·y`) sound and the §Summation-
   order-table reduction-tree reading correct. Properly scoped as non-blocking prose nuance.

6. **No skill invocation named — skill-uptake-survey, severity: trivial (telemetry).** The audit
   does not reference `verify-citation-range` / `verify-rotation-citation`, despite the inherited-
   anchor-drift sub-case being exactly what `verify-citation-range` was extended (cycle-012) to
   cover. Surfaces as telemetry; not blocking. Had the skill's "compare claimed anchor vs current
   artifact state" step been applied, issue #1 (the phantom `:611` drift) would have been caught.

### Tiebreaker verdict (per task instruction)

Independent reads (direct `Read` of `reference/palace/palace/linalg/operator.cpp:595-644` AND
`palace-codemap read_range` — the two agree exactly) establish ground truth:
**SPD comment = `:612`; SPD assertion = single line `:616`; real-`Operator` `Ax` = `:624`;
`ComplexOperator` `Ax` = `:634`.** Against the *current* theme file: the SPD comment is already
correct (`:612`); the `Ax` anchors (`:623`/`:632`) and the assertion range (`:615-616`) are the
genuine drifts. The verifier is right on ground truth across the board but mischaracterizes the
SPD-comment anchor as a live drift when the artifact already carries the correct value — there is
**no live `:611` in the theme**, so no contradiction with the cycle-019 repairer survives in the
committed file.

## Repair

### Fixes attempted

- **Finding**: Phantom `:611`→`:612` SPD-comment "drift" (critic issue #1, citation-validity,
  medium). The report's `verified_against:` block (`operator.cpp:598-617` note + `audit_caveat`),
  Summary, §operator.cpp audit, Carry-forward item 3, and OQ all assert the theme pins the SPD
  comment to `:611` and that this drifted to `:612`. The live theme already says `:612`; `:611`
  appears nowhere in `book/src/L2-L1/inner-product-fold-specialization.md`.
  - **Decision**: repaired.
  - **Action**: Independently re-verified the live theme via `grep` — `:611` absent (exit 1),
    `:612` present at theme line 372. Then dropped the phantom item from every place the report
    asserted it, surgically (no content authoring; the verifier's own ground-truth reads stand):
    - `verified_against:` yaml `operator.cpp:598-617` note (CYCLE.md §Proposed-changes) — rewrote
      to "SPD comment at :612 (theme ALREADY pins :612 — verified, no change); SPD assertion single
      line at :616 (narrow to :616)".
    - `audit_caveat` (CYCLE.md §Proposed-changes) — re-listed the three GENUINE drifts (Ax
      :623→:624, :632→:634; SPD assert range :615-616→:616) and parenthesized the SPD comment as
      already-`:612`.
    - Carry-forward list (CYCLE.md) — removed the phantom item 3 (SPD comment), renumbered the SPD
      assertion to item 3, added a note that `:611` is nowhere in the committed theme.
    - OQ `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` (CYCLE.md) — changed
      "four inline anchors" → "three"; dropped the SPD-comment row; noted the phantom.
    - Summary + §operator.cpp audit block (CYCLE.md) — corrected "theme/repairer says `:611`" to
      reflect that the theme already pins `:612`; reframed the verdict to one genuine drift (the
      SPD assertion range) on the `:598-617` citation.
  - The fenced ` ```yaml ` block format (and the enclosing `edit:` fence) is preserved unchanged.

- **Finding**: Three GENUINE inline-anchor drifts (critic issues #2, #3) — `Ax` `:623`→`:624`,
  `:632`→`:634`, SPD assertion range `:615-616`→`:616`.
  - **Decision**: repaired (kept; confirmed they remain the audit's actual findings).
  - **Action**: These are the verifier's correct findings and the substantive carry-forward; left
    intact in the `verified_against:` block (the two `Ax` `supports` rows with INLINE-drift notes,
    and the `operator.cpp:598-617` `partially-supports` row now narrowing the SPD assertion to
    `:616`), the `audit_caveat`, and the Carry-forward list (now items 1-3). No content change to
    these — only the phantom was removed around them.

### Unrepairable findings

None. The only actionable defect was the phantom `:611`→`:612` SPD-comment "drift", which is a
mechanical mischaracterization removable surgically (no substantive authoring — the verifier's
source reads and the three genuine corrections all stand). Critic issues #4 (self-dot `:679`→`:678`,
self-flagged within tolerance), #5 (dispatch-key-1 prose nuance, correctly scoped non-blocking by
the verifier), and #6 (no skill named — telemetry) are trivial / telemetry and require no repair.

## Suggested resolution

`ready`. Notes for the integrator:

- The `verified_against:` yaml append now records the audit's actual findings: `coverage_verdict:
  fully-supported`, `status_recommendation: keep firm`, and exactly three genuine inline-anchor
  drifts as the `audit_caveat`. No status change to the theme.
- The carry-forward citation corrections are now **three** (not four): `Ax` `:623`→`:624`,
  `:632`→`:634`, and the SPD-assertion range `:615-616`→`:616` (narrow to the single line `:616`).
  These are bounded, evidenced lifter/integrator-carry-forward touches; they do not block applying
  the metadata append. The SPD comment requires NO touch — the live theme already pins `:612`.
- The OQ `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` is the home for the
  three remaining anchor corrections.
