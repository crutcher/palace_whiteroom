---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T070102Z
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
repaired_at: 2026-06-04T070312Z
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

# META: verification of "Audit bilinear-form (firmability dischargeability probe)"

## Critique

### Checks run

**citation-validity — warning.** All five load-bearing L0 anchors were verified verbatim on disk (`awk` line-print + `citecheck`):
- `palace/linalg/operator.cpp:621-639` — real-A overload `621-629` (`A.Mult(x.Real(),...)` + `A.Mult(x.Imag(),...)` then `return Dot(comm, Ax, y)`), complex-A overload `631-638` (`A.Mult(x, Ax)` then `return Dot(comm, Ax, y)`). EXACT.
- `palace/linalg/operator.hpp:385-394` — the `yᴴ A x` comment is at line **386** (real-A block) and **391** (complex-A block); decls at 388-389 (real-A `const Operator &A`) and 393-394 (complex-A `const ComplexOperator &A`); line 385 is the blank/boundary line. The report's claim "comment at line 386 ... decl 388-389 ... decl 393-394 ... `:385` start is the blank boundary" is CORRECT and `:385-394` legitimately spans the full overload pair. (Codemap `read_range` reported these one line low — it dropped blank line 385 — but on-disk `awk` and `citecheck --anchor 'bilinear form'` both place the comment at 386/391; the authoritative line-map confirms the report, exactly the cycle-024 off-by-one trap the role-spec warns against.)
- `palace/models/boundarymodeoperator.cpp:85` — `linalg::Dot(comm, et, *Bttr, et)` Hermitian `y=x` witness. EXACT.
- `palace/models/boundarymodeoperator.cpp:90` — `linalg::Dot(comm, en, Atn, et)` with `Atn` a `ComplexWrapperOperator` over a HypreParMatrix (non-Hermitian, `en`≠`et`). EXACT.

The 2-call-site count is on-disk-accurate (`grep` for the 4-arg matrix-weighted signature in `palace/` non-test returns exactly the two `boundarymodeoperator.cpp:85/90` sites; all other `linalg::Dot` hits are 3-arg). The no-test claim is accurate (`test/unit/` carries only 3-arg `Dot`; no `*bilinear*` test file). Constituent firmness confirmed: `dot.md:100` firm (laws 6/7 present at `:65-66`), `apply_linop.md:87` firm (laws 1/5/6 at `:50,54,55`), `matrix-weighted-norm.md:110` firm c091 (discharges the same 4-arg gate as redundant under the escape). The `verified_against:` YAML round-trips clean (`yaml.safe_load` → 9 entries; verdicts 8×supports + 1×partially-supports; no leading-quote `note:` violation). **The one defect:** at CYCLE.md:369 the Open-questions self-note labels the referent as **`matrix-weighted-norm.md:251-257`**, but that file is only 212 lines (`citecheck --scan` → `[OOB]`); the paragraph it describes ("the `bilinear-form` half remains open", which the report's own prose locates "in the bilinear-form Dependencies §") is at **`bilinear-form.md:251-257`** — a misattributed filename producing an out-of-bounds range. The bare `(:251-257)` at CYCLE.md:117 (per-citation-audit context, implicitly the subject chapter) does land correctly in bilinear-form.md, so the verdict does not rest on the misattribution, but the explicit wrong-file citation at :369 is a concrete citation error.

**surface-or-evidence — pass.** This is a lowering-verifier dischargeability audit: it modifies surface (a `verified_against:` block + a §Status narrowing) with full evidence backing. I independently read laws 1-8 in `book/src/L1/bilinear-form.md:182-220` to adjudicate the escape's applicability (the report's crux claim). Laws 1-3 (conj-linear in `x`, linear in `y`, linear in `M`) are direct syntactic compositions of `dot` laws 7/8 + `apply_linop` laws 1/5/6; laws 4-5 are zero-coefficient corollaries; law 6 is the definitional identity-weight specialisation `bf(x,I,y)=dot(x,y)`. None carries inner-product-axiom (norm) theorem content — they are read-offs, not theorems. This is the load-bearing distinction from `matrix-weighted-norm`, whose gating laws WERE norm-axiom theorems (triangle/Cauchy–Schwarz/parallelogram) needing two probes; bilinear-form carries none of those. Law 7 (Hermitian-`M` symmetry) is a premise-guarded conditional identity — the matrix-weighted analogue of `dot` law 6 — with BOTH branches positively witnessed on disk (Hermitian `Bttr` `:85`, non-Hermitian `Atn` `:90`); the witnesses genuinely exercise the symmetry-conditional path (one branch where `Mᴴ=M` holds, one where it fails). Law 8 (PSD at `y=x` for SPD `M`) is the sole law with positivity content, but it is (i) premise-guarded (M SPD), (ii) inherited for the SPD diagonal from the firm `matrix-weighted-norm` sibling (c091), and (iii) positively witnessed by the genuine `y=x` form `Dot(comm, et, *Bttr, et)` at `:85`. The dispatch's pointed question — whether the "un-surfaced real-M-real-y" shape is NEEDED for law 8 / Cauchy–Schwarz-at-`y=x` — resolves NO: law 8 is stated for the complex `xᴴMx` form and is witnessed for it by `Bttr`; the real-`M`-real-`y` `xᵀMy` shape is a separate (unsurfaced) variant and is not the carrier of law 8's positivity. No law smuggles inner-product-axiom content the escape does not cover. The escape is genuinely applicable; the DISCHARGE is sound.

**rotation-quality — pass.** Not a rotation claim — this is a within-L1 firmability audit (no L_{n+1}→L_n representational shift is asserted). No-op for this report kind.

**variant-axis-coverage — pass.** The four declared variant axes (precision-mode, output-arg-pattern, M-symmetry-property, parallel-wrapper) are each addressed in the chapter and re-examined by the probe; the M-symmetry-property axis (the only material one) has two on-disk witnesses (one per branch). The report explicitly treats the unsurfaced real-`M`-real-`y` element-type combination as scoped-out (not surfaced by Palace), which is the correct disposition — no hidden branch.

**cross-reference-integrity — pass.** All cross-references resolve: `book/src/L1/dot.md`, `apply_linop.md`, `matrix-weighted-norm.md` exist and carry the asserted firm status; the constituent law-line ranges are in-range. The whole-book `grep -rln 'bilinear-form'` residue is enumerated (not edited) for the future cascade-wave lifter, correctly out of this single-file scope. (The `:251-257` filename misattribution at :369 is logged under citation-validity, not here, since the slug/link itself resolves.)

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (within-L1 audit referencing the L1>L0 lowering only as a preview, which the chapter and report frame correctly as a lowering PREVIEW, not a reverse-direction definition).

**plan-kind-consistency — pass.** Declared kind is an audit/dischargeability probe; content matches. Critically, the proposed-changes does NOT flip the frontmatter `firmness: rough-in` (verified: no edit block targets frontmatter; both `edit:` blocks target `book/src/L1/bilinear-form.md` body) and the Edit-2 replacement text retains the `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` token; the firm flip + `gram_reduce` re-judgment + 4-feature-column unblock + cross-reference re-anchor are all explicitly deferred to a separately-gated `bilinear-form-firm-flip-and-cascade-wave` (c093/batch-30 candidate). Edit-2's replace range `:323-335` lands exactly on the §Status gate paragraph (rough-in token through gate item 1), preserving the cycle-010 repair-note `:336-346` outside the range. No cascade / `gram_reduce` / feature-column / L1>L0-theme edits are enacted. The 9-entry `verified_against:` YAML parses.

**skill-uptake-survey — pass.** The probe invokes `citecheck` (anchor + scan) for the no-drift duty and `python3 -c "import yaml..."` for the YAML round-trip — the procedural tooling the report's shape implies. Telemetry-only; no blocking.

### Issues found

1. **Misattributed filename → out-of-bounds citation.** CYCLE.md:369 (Open questions / caveats, the third bullet) cites the referent as `matrix-weighted-norm.md:251-257`, but that file has only 212 lines (`citecheck --scan` → `[OOB]`). The paragraph being described ("the `bilinear-form` half remains open", which the bullet's own prose places "in the bilinear-form Dependencies §") is at `book/src/L1/bilinear-form.md:251-257`. Severity: low — non-load-bearing (the verdict does not rest on it; the bare `(:251-257)` at CYCLE.md:117 correctly resolves to the subject chapter), but it is a concrete wrong-file citation. Repair: change `matrix-weighted-norm.md:251-257` → `bilinear-form.md:251-257` at CYCLE.md:369.

2. **(Non-blocking, telemetry) basename-only references in the per-citation prose.** `citecheck --scan` raised `[AMBIG]` on bare-basename prose mentions (`dot.md:65`, `apply_linop.md:50`, `operator.cpp:621-639`, `operator.hpp:385-394`, etc.) where the basename matches multiple files. These are prose shorthand in the audit narrative; the load-bearing `verified_against:` block and inputs list all use full `book/src/L1/...` / `palace/...` paths, so the ambiguity is cosmetic. Noting for completeness, not flagged as a defect.

### Verdict note for downstream

The DISCHARGE is sound on the merits — every L0 anchor verifies verbatim, the firm-on-positive-structure escape genuinely applies (laws 1-6 syntactic read-offs with no norm-axiom content; laws 7-8 premise-guarded with on-disk witnesses; law 8 positivity inherited from the firm c091 sibling), the redundant-gate argument holds (real-M-real-y is unsurfaced, the no-test route is genuinely absent, Cauchy–Schwarz-at-`y=x` is an inherited FP non-law), and the maturity token correctly stays `rough-in` with the cascade deferred. The only finding is the single misattributed-filename citation at CYCLE.md:369.

---

## Repair

### Fixes attempted

- **Finding**: Misattributed filename → out-of-bounds citation. CYCLE.md:369 cites `matrix-weighted-norm.md:251-257`, but that file is only 212 lines, so the range is OOB; the paragraph described ("the `bilinear-form` half remains open", in the bilinear-form Dependencies §) actually lives at `bilinear-form.md:251-257`. The critic also noted the bare `(:251-257)` at CYCLE.md:117.
  - **Decision**: repaired.
  - **Action**:
    - Verified on disk first: `matrix-weighted-norm.md` = 212 lines (so `:251-257` is genuinely OOB, not a different valid range); `book/src/L1/bilinear-form.md:251-257` confirmed to contain the intended content — the law-8 energy-norm clause `nrm2_B(x, B) = √bilinear_form(x, B, x)` when `B` is SPD, plus the literal "the `bilinear-form` half remains open" text.
    - Determined the misattribution lives **ONLY in prose narration**, NOT in the proposed-changes block. CYCLE.md:117 is in `## Per-citation audit`; CYCLE.md:369 is in `## Open questions / caveats`. The `## Proposed changes` block (Edit 1 `verified_against:` YAML at :215-258, Edit 2 §Status narrowing at :260-329) was grepped for `matrix-weighted-norm`/`:251-257` and contains only the CORRECT `matrix-weighted-norm.md:108-115` sibling §Status reference plus by-name sibling mentions — no OOB/misattributed range lands in the artifact. The fix is therefore cosmetic-but-correct (report-narration accuracy), not load-bearing for integration.
    - Edit at CYCLE.md §Per-citation-audit (line 117): `(`:251-257`)` → `(`bilinear-form.md:251-257`)`.
    - Edit at CYCLE.md §Open-questions-caveats (line 369): `**`matrix-weighted-norm.md:251-257` self-note ...` → `**`bilinear-form.md:251-257` self-note ...`.
    - Re-confirmed the `verified_against:` YAML still parses after edits (untouched by the fixes; 9 entries = 8 supports + 1 partially-supports, well-formed nested-fence block).

### Unrepairable findings

None. The single citation-validity finding was mechanical (filename correction to a verified-on-disk range) and is repaired.

## Suggested resolution

`ready`. The DISCHARGE verdict, the unflipped `rough-in` maturity token, and the deferred cascade recommendation are all untouched. The misattribution was prose-narration-only and did not affect the artifact-bound proposed-changes block; the fix corrects report accuracy. Integrator note: Edit 1 appends the 9-entry `verified_against:` block and Edit 2 narrows the §Status (`:323-335`) without flipping `firmness: rough-in` — the firm flip + cascade wave (`gram_reduce` re-judgment, 4-feature-column unblock, cross-reference re-anchor) remain deferred to the separately-gated `bilinear-form-firm-flip-and-cascade-wave` candidate.
