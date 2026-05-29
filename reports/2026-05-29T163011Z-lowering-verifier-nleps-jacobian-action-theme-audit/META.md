---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T17:05:00Z
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
repaired_at: 2026-05-29T17:40:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Audit nleps-jacobian-action-mutation-rotation"

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Re-ran `tools/citecheck/citecheck.py --scan` on the
CYCLE.md: **53 ok, 0 failing** — matches the report's claim exactly (line 375). Then ran `--anchor`
spot-checks on every decisive pinpoint the audit scope names, all against on-disk
`reference/palace/`:
- `:664` `Identity(k, k) - H` → ok, line 664 (the `S = λI − H` block; codemap was `663`, +1).
- `:665` `S.fullPivLu().solve(v2)` → ok, line 665 (first solve `S⁻¹·v₂`).
- `:666` `MatVecMult(X, Sv2)` → ok, line 666.
- `:667` `S.fullPivLu().solve(Sv2)` → ok, line 667 (the double-`S⁻¹`/`S⁻²` signature).
- `:668` `opJ->AddMult(XSv2, w, 1.0)` → ok, line 668 (the `+T'` two-pencil term).
- `:669` `A->AddMult(XSSv2, w, -1.0)` → ok, line 669 (the `−T` two-pencil term).
- `:411` `divided difference` → ok, line 411 (the divided-difference-Jacobian comment).
- `:412` `std::sqrt` → ok, line 412 (`δ = √ε`).
All zero-drift, all in-range. The corrected on-disk numbers the audit asserts (`S`=664, `Sv2`=665,
`XSv2`=666, `XSSv2`=667) are confirmed correct on disk. Every one of the audit's per-citation
verdicts holds.

**surface-or-evidence — pass.** This is an AUDIT report whose proposed-change is purely additive
(a `verified_against:` metadata block), no surface edit and no status change — the
audit-report / retroactive-evidence-backfill case, allowed. Independently confirmed the
load-bearing semantic claims by reading `nleps.cpp:645-684` and `:408-415`: the divided-difference
`A2'` construction (`:650-654`: bumped `opA2p`, `denom = i·δ·|Im λ|`, `BuildParSumOperator({1/denom,
−1/denom}, {opA2p, A2n})`), the derivative pencil `{0,1,2λ,1}` (`:655-656`), the product-rule
`∂_λ S⁻¹ = −S⁻²` realized as the double sequential solve (`:665`→`:667`) plus the two-distinct-pencil
`AddMult` (`opJ` at `:668`, `A` at `:669`), and the `δ = √ε` constant at `:412` with the `:411`
"divided difference Jacobian" comment — all present verbatim, exactly as the audit characterizes the
A2' non-law and the product-rule structure. Also read `MatVecMult` (`:329-347`: `z = 0.0` then
per-`j` two `AXPBYPCZ` real/imag carriers) and deflation growth (`:606-619`: `scale = Norml2`,
`v *= 1.0/scale`, `X[k] = v`, no Gram-Schmidt) — both match. The audit's honest self-correction at
its line 138 (its first `'1.0 / linalg::Norml2'` anchor was a NOANC because the code splits the
expression) is accurate and does not affect the verdict.

**rotation-quality — pass (not the primary axis for an audit; verified anyway).** The theme under
audit is a lowering (L1→L0); the audit does not assert a new rotation, it verifies an existing firm
theme's lowering is supported. The theme's rotation (pure L1 `nleps_jacobian_action` → the
destination-buffer `w = J*v` block, hiding buffer reuse, `A2n` caching, value-pencil re-scoping) is
a genuine state-hiding / compression rotation, and the audit correctly leaves it firm.

**variant-axis-coverage — pass.** The audit walks all six applicability conditions and the variant
axes (deflation-present `k=0` vs `k>0` via the `:658` guard; complex-only element type; variadic-`k`;
single-rank scope). The `k=0` degeneration to the bare derivative-pencil apply is covered, and the
audit explicitly scopes out real-valued and distributed specializations (correctly excluded by the
theme). No hidden branches.

**cross-reference-integrity — pass.** All 12 referenced theme/operator chapters resolve on disk
(the 5 sibling/cross themes, the 6 L1/L2 operator chapters, plus the L1 entry the theme lowers).
The build-readiness fence guard: the proposed-changes `edit:` block (lines 249-350) is a properly
nested fence — `edit:`(249) / `yaml`(251) open, `yaml`-close(349) / `edit`-close(350) — even parity
(4 fences), balanced nesting, and the explanatory note at 352-354 confirms the structure. This is an
ADDITIVE metadata block, not a firm-body authoring, so the firm-body-inside-fence guard does not
apply (no `## Status`/Signature/Algebraic-laws body is being authored here). No fence-truncation
defect.

**edge-label-fidelity — pass.** The theme is L1>L0 and the audit's prose discusses exactly that
edge: the §"Directionality check" (CYCLE.md:409-412) confirms forward L1→L0 narration with no
reverse-direction lift in the formal sections. No edge-label mismatch.

**plan-kind-consistency — pass.** Declared kind is an audit (lowering-verifier verdict
"fully-supported"); content shape matches — per-citation verdicts, applicability-condition walk,
algebraic-law check, additive `verified_against:` proposed-change, no status change. Correctly
classified as an audit, not a firm-authoring or rough-in.

**skill-uptake-survey — pass.** The audit references the mechanical citecheck realization of
`verify-citation-range` (the `--anchor`/`--scan` tooling) throughout, consistent with the cycle-024
role-spec wiring. The skill uptake is surfaced and appropriate for an audit's shape.

### Issues found

No blocking or warning issues. The audit is sound; all eight checks pass on independent
re-verification. Items recorded for the repairer/integrator as confirmations (not defects):

1. **Carry-forward correctly scoped (CONFIRMED, not a defect).** The audit's OQ1 (CYCLE.md:383-399)
   claims the L1 ENTRY `book/src/L1/nleps_jacobian_action.md` still carries the codemap `+1` drift on
   its deflation-block pinpoints, and that this is dispatch-1's (lifter's) re-anchor target this
   cycle — NOT a defect of the theme under audit. Independently confirmed: `citecheck --anchor`
   against the entry's pinpoints shows `:663→664`, `:664→665`, `:665→666`, `:666→667` all `[DRIFT +1]`
   (with the suggested corrected line in hand), while the wide ranges `:659-660` and `:661-662` read
   `[ok]` precisely because they enclose the off-by-one anchor — exactly as the audit describes. The
   entry passes `citecheck --scan` (33 ok / 0 failing) only because the single-line pinpoints happen
   to fall inside enclosing ranges or the scan tolerance; the `--anchor` probe is what exposes the
   pinpoint drift. This is correctly scoped as a carry-forward / independent confirmation of
   dispatch-1's target, NOT a finding against the theme under audit. The THEME itself uses the
   corrected on-disk numbers (`664`/`665`/`666`/`667`) throughout and is drift-free — confirmed.

2. **OQ disposition is NOT over-claimed as discharged.** The report states "OQ ledger disposition
   appended" (CYCLE.md:414) and the ledger entry
   (`scaffolding/open-questions.md:846`) is `status: Open — disposition pending integration`. The
   AUDIT WORK (theme verification) is fully discharged — verdict fully-supported, additive
   `verified_against:` block is the per-report proposed-change. The residual OPEN items are genuine
   carry-forwards (the L1-entry `+1` re-anchor, owned by dispatch-1; the standing cohort-wide
   test-coverage absence), each with an explicit action + trigger. The audit correctly does NOT
   assert it has closed those — it leaves them open with disposition pending integration. This is
   accurate framing, not a defect.

3. **Scope of the proposed change is purely additive (CONFIRMED).** The 24-entry `verified_against:`
   YAML block adds metadata only; no theme content edit, no status change. The theme stays `firm`.
   The block's per-line notes match the verified on-disk numbers. The note count (24 entries
   including the enclosing-range row + the `:177-181` closure-provenance row) is a superset of the
   "19 per-line L0 citations" headline figure — the headline counts the numbered per-line pinpoints;
   the YAML block additionally itemizes the enclosing `:649-669` range and the `:177-181`
   `SetExtraSystemMatrix` provenance citation. Not a discrepancy, but the integrator should be aware
   the "19" and "24" both refer to correct, distinct tallies (numbered pinpoints vs. total
   `verified_against:` rows).

---

## Repair

All eight critic checks `pass` on independent re-verification — no warning/fail finding to
substantively repair. Two mechanical/surgical hygiene fixes were applied (neither overrides a
critic check); both are build-safety / channel-format, not content authoring. `overall_status:
ready`.

### Fixes attempted

- **Finding** (build-safety, surfaced by the dispatch prompt + cross-reference-integrity check note): the proposed-changes `edit:` block (CYCLE.md:249–350) nested a literal ```` ```yaml ```` fence (open at :251, close at :349) directly inside the flush-left ```` ```edit: ```` block. Under flat CommonMark fence-toggle parsing (how `integrator-per-report` extracts the block), the inner ```` ```yaml ```` would have closed the outer `edit:` block early at :251, capturing only the `[append at end of file]` marker and stranding the entire 24-row `verified_against:` payload outside the apply boundary — the exact `convert-nested-fences-to-indented-code-in-proposed-changes-block` mis-toggle defect. (The critic read the fences as "even parity (4 fences), balanced nesting" — correct as a *count*, but flat toggle-parsing does not respect nesting, so the count being even does not make the extraction safe.)
  - **Decision**: repaired.
  - **Action** (`reports/<id>/CYCLE.md` §"Proposed changes", the `edit:` block at :249): applied the skill's option (b) — 4-space-indented the entire inner payload (the ```` ```yaml ```` open line, all 24 `verified_against:` rows, and the ```` ``` ```` close line) so the inner fence is captured as literal block *content* rather than a toggle. Post-edit fence audit: exactly 2 flush-left toggle fences (`edit:` open :249, close :350 — clean parity for the single block); the ```` ```yaml ````/```` ``` ```` markers now sit at 4-space indent (:251/:349) inside the captured content. The integrator strips the 4-space indent on apply and appends the resulting standalone ```` ```yaml ```` fenced block at end-of-file, producing exactly the landed-sibling form (`book/src/L1-L0/dot-mutation-rotation.md:402–420`). Not a single character of the YAML content changed — only the fence *mechanism* (fence-delimited → indent-wrapped). Verified the target chapter `book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md` exists with no pre-existing `verified_against:` block, so the append is genuinely additive and idempotent-safe.

- **Finding** (stale report-pointer): META.md frontmatter carried `verifies: ../REPORT.md`, the pre-rename filename (CYCLE.md replaced REPORT.md at cycle-004).
  - **Decision**: repaired.
  - **Action** (`reports/<id>/META.md` frontmatter line 2): `verifies: ../REPORT.md` → `verifies: ../CYCLE.md`.

### Unrepairable findings

None. No critic finding was warning/fail; the audit is sound and the verdict (`fully-supported`)
is fully supported. The three integrator-facing items the critic recorded are explicit
**confirmations, not defects**, and need no repair:
1. The L1-ENTRY `+1` codemap drift is correctly scoped as dispatch-1's (lifter's) re-anchor target
   this same cycle — a carry-forward cross-check, NOT a defect of the theme under audit (the THEME
   uses corrected on-disk numbers and is drift-free).
2. The OQ disposition is honestly framed as `Open — disposition pending integration`; the audit
   work itself is discharged and does not over-claim closure of the residual carry-forwards.
3. The "19 per-line citations" headline and "24-entry `verified_against:` block" are two correct,
   distinct tallies (numbered pinpoints vs. total rows, the block additionally itemizing the
   enclosing `:649-669` range + the `:177-181` closure-provenance citation) — no discrepancy.

## Suggested resolution

`ready` — clean for `integrator-per-report`. Notes for the integrator:
- The proposed change is purely additive: append the (now indent-wrapped) ```` ```yaml ````
  `verified_against:` block to `book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md` at
  end-of-file, after the existing `## Verified-against` prose section. Strip the 4-space indent on
  apply so the landed file carries a flush-left ```` ```yaml ```` fence (channel-format requirement
  for the `cross-layer-cross-cutter` parser, which keys on the `verified_against:` leading text).
  No status change — the theme stays `firm`.
- The L1-entry `+1` drift (entry's `:663→664`, `:664→665`, `:666→667`, with comment/pencil ranges
  `:659-660→660-661`, `:661-662→662-663`) is **dispatch-1's (lifter's) scope this cycle**, not part
  of this report's proposed-changes — do not apply it here; it lands via the lifter's per-report
  dispatch.
