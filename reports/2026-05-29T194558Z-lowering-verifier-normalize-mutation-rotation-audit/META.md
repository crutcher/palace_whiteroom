---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T20:15:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T20:42:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Audit normalize-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan book/src/L1-L0/normalize-mutation-rotation.md --quiet` → `42 ok, 0 failing, exit 0`, matching the auditor's claim exactly (CYCLE.md:26, :371-372). Ran `--anchor` probes on every load-bearing pinpoint the audit relies on: `vector.hpp:262-270 --anchor 'MFEM_ASSERT'` → 267; `vector.hpp:267 --anchor 'MFEM_ASSERT'` → 267; `iterative.cpp:631-632 --anchor 'Hj[j + 1] = linalg::Norml2'` → 631; `operator.hpp:377-384 --anchor 'Normalize(MPI_Comm comm, VecType &x, const Operator &B'` → 378. All land exactly where the report says. The two contested F3 anchors are mechanically settled by the tool (see F3 below): `iterative.cpp:810-811 --anchor 'Hj[j + 1] = linalg::Norml2'` → **810** and `iterative.cpp:811 --anchor 'w *= 1.0 / Hj'` → **811** — the tool confirms the `Hj[j+1]=Norml2` half is at 810, not 811, so the auditor's `:811`→`:810-811` parity nudge is correct and not an off-by-one hallucination. The auditor's "zero codemap drift" claim is sound: every per-citation row carries a verdict and the load-bearing rows are anchor-confirmed. The `verified_against:` payload in Edit 1 is a well-formed YAML list with correct `verdict:` vocabulary (`supports` / `partially-supports` / `does-not-support`).

**surface-or-evidence — pass.** This is a lowering-verifier audit (audit-kind, not a refinement). It modifies no operator/theme surface; its deliverable is the `verified_against:` evidence-backfill block plus two proposed refinements that are explicitly GATED (CYCLE.md:234-235, :328-334, :396-399 — "this audit proposes, it does not apply"). The retroactive-evidence-backfill framing is the allowed shape for this kind. F1, although a `does-not-support` finding, is correctly NOT enacted in-place: it spans two files (theme + L1 entry) and touches note *substance*, so the auditor routes it to a follow-up abstractor/lifter (CYCLE.md:328-334) — correct lowering-verifier discipline (audit only, no authoring). Confirmed against the write-authority partition: a verifier appends `verified_against:` and proposes; it does not author content.

**rotation-quality — pass (not the primary check for an audit, but the underlying rotation is sound).** The audited theme asserts a structural mutation rotation: the pure L1 pair `(β, û) = normalize(x)` lowers to the L0 in-place `linalg::Normalize(comm, x)` (four-step composition reduction→guard→rescale→return). This is state-hiding / returned-value compression (the L1 form carries no destination buffer; the L0 form reintroduces the in-place receiver overwrite), not a 1:1 rename — the L1 form is strictly more abstract (three distinct values vs. one mutated buffer + returned scalar). The auditor confirms the factorisation law `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` holds on the L0 body (CYCLE.md:213-216). Genuine rotation.

**variant-axis-coverage — pass.** The audited theme has one variant axis (element-type real|complex), inherited wholesale from the `nrm2`/`scal` leaves and explicitly collapsed (theme lines 304-313; CYCLE.md:193-198 Condition 3). The auditor verifies the axis is absorbed by inherited sub-themes and flags no hidden branch. The one non-trivial semantic axis (partiality at x=0) is correctly classified as a guard, not a variant axis. No hidden combination.

**cross-reference-integrity — warning.** All seven cross-referenced artifact targets resolve on disk (`book/src/L1/normalize.md`, `nrm2.md`, `scal.md`, `matrix-weighted-norm.md`, and the three sibling `L1-L0/*-mutation-rotation.md` themes — all present). The audited theme is `firm` (Status line 383-399) but this is an audit, not a fresh firm-body author, so the firm-body-inside-fence guard applies to the *proposed-changes block fence parity* rather than to a chapter body. Fence enumeration of CYCLE.md (`grep -n '\`\`\`'`) yields 6 fences with even parity: Edit 1 opens ` ```edit: ` (L239), opens a nested ` ```yaml ` (L241), closes the yaml (L307), closes the edit (L308); Edit 2 opens ` ```edit: ` (L315) and closes (L326). The `verified_against:` body IS enclosed inside the fence (correct — not the cycle-019 outside-fence defect). HOWEVER: Edit 1 nests a same-style triple-backtick ` ```yaml ` fence **inside** the ` ```edit: ` proposed-changes fence — the exact nested-fence pattern the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` repairer skill exists to defuse, because a naive markdown/integrator parse can truncate the edit block at the first inner ` ``` ` (L307) and silently drop the closing edit fence (L308). The sibling theme `matrix-weighted-norm-mutation-rotation.md:460` deliberately rendered its own `verified_against:` block with **tilde fences (`~~~yaml`)** precisely to avoid this hazard. This is the warning: the Edit 1 payload should be re-fenced (tilde outer or inner, or indented-code) before the integrator parses it. Issue I1 below.

**edge-label-fidelity — pass.** The theme carries the L1>L0 edge label; the audit prose discusses exactly that edge (L1 `normalize` → L0 `linalg::Normalize`). The auditor's "direction-of-definition: clean" note (CYCLE.md:393-395) independently confirms forward (high→low) narration with no reverse-direction lift prose. No edge mismatch.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit; content shape matches — per-citation verdict table, applicability-condition re-verification, algebraic-law re-check, a `verified_against:` deliverable, and gated refinements. The frontmatter `status: pending` (line 5) is the pre-repair value (the repairer/overall_status owns the final state). No mis-classification. (Minor: frontmatter `verifies:` is implied by co-location; the report itself is internally consistent on its audit-kind self-description.)

**skill-uptake-survey — pass.** The audit references the relevant skills it exercised: `verify-citation-range` (implicitly via the citecheck `--anchor`/`--scan` mechanical realization, CYCLE.md:26, :371-372), and the verdict shape follows the sibling-theme `verified_against:` convention. The F1 routing to a follow-up abstractor and F3 citation re-anchor are the right downstream skill targets (`upgrade-plain-text-ref-to-live-link`-adjacent re-anchor / abstractor authoring). Telemetry surfaced; not blocking.

### Issues found

**I1 (cross-reference-integrity, build-readiness, repairable) — nested same-style triple-backtick fence in Edit 1.** `reports/.../CYCLE.md:239-308` (Edit 1 proposed-changes block). The `verified_against:` YAML payload is wrapped in a ` ```yaml ` fence (L241, closing L307) nested inside the ` ```edit:book/src/L1-L0/normalize-mutation-rotation.md ` fence (L239, closing L308). Same-style backtick nesting risks integrator/markdown truncation at the inner close (L307), dropping the outer edit close (L308). Severity: medium — fence parity is even and the body is correctly enclosed, so it is not the cycle-019 outside-fence defect, but the nesting is a known truncation hazard. Fix path: the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill, or mirror the sibling `matrix-weighted-norm-mutation-rotation.md:460` `~~~yaml` tilde-fence convention. Candidate for repair.

**I2 (assessment of whether F1 should block — it should NOT) — does-not-support lands on a non-firm note; firm status correctly unaffected.** The auditor's central judgment call holds. F1 is a `does-not-support` verdict on `operator.hpp:377-384`'s *characterization* (CYCLE.md:160-176, :299-302). I independently confirmed the substance: `sed -n '377,384p' operator.hpp` shows a genuine fused `inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)` (def at line 378, body reduction→guard→rescale→return identical to the unweighted `vector.hpp:264`), and `grep` for 4-arg `Normalize(` callsites across `reference/palace/palace/` returns **zero** — so the function is defined-but-uncalled, exactly as the auditor states (CYCLE.md:42, :367-370). The theme's prose "Palace has **no** `linalg::Normalize`-with-`B` free function" (theme lines 283-284) is therefore factually wrong; the defensible claim is "exists but uncalled." CRITICALLY, this `does-not-support` lands ONLY on the `normalize_B` rough-in NOTE (theme lines 274-301), which the theme's own Status line (lines 397-399) and Speculative-L1-operators section (lines 274-280) explicitly scope OUT of the firm claim ("not part of this theme's firm claim"). The firm claim is the *unweighted* `linalg::Normalize(comm, x)` lowering, whose 14 supporting citations all verdict `supports`/`partially-supports`. So the reasoning "firm status unaffected" is sound: a does-not-support on an explicitly-non-firm in-chapter note does not gate the firm core. F1 should NOT block; it is a correctness refinement to a rough-in note. (Corroborating: the sibling `matrix-weighted-norm-mutation-rotation.md:478-481` already records `operator.hpp:377-384` as its OWN Sub-pattern C consumer with verdict `supports` — confirming the range is the weighted theme's consumer, exactly the boundary the `normalize` theme cites; the contradiction is purely in the `normalize` theme's "does not exist" phrasing, not in the citation.)

**I3 (F3 confirmed correct — minor, repairable) — `:811`→`:810-811` parity nudge is mechanically validated.** `book/src/L1-L0/normalize-mutation-rotation.md:137, :174, :341` cite the second GMRES path as `iterative.cpp:811`, but describe the full two-line `Hj[j+1]=Norml2; w*=1.0/Hj[j+1]` shape, whose `Hj[j+1]=Norml2` half is at line 810 (`--anchor` → 810), with `:811` covering only the rescale. The first path is correctly cited `631-632`; the second should be `810-811` for parity. This is a citation-precision refinement, in-bounds, non-blocking. Note the audited theme's own Verified-against row (theme line 342) currently self-justifies the second path as "cited inherited via `scal-mutation-rotation.md:61-62`" rather than anchor-verified — Edit 2 (CYCLE.md:322-325) correctly upgrades this to an `--anchor`-audited 810-811 row. Candidate for repair (mechanical re-anchor, 3 occurrences).

**I4 (F2 — observation, no edit forced, correctly handled).** `nleps.cpp` carries additional companion-scale instances beyond the cited `610-611,617`. Verified at `488-494, 544-545, 697-698, 738-739`: each is a shared `norm` rescaling a vector and its `*2` companion (the Sub-pattern C shape). The auditor records this as a resolved Open question with no forced edit (CYCLE.md:376-384), which is correct since the theme characterizes the cohort as "illustrative." Minor nuance, not a defect: several of these extras compute the norm via inline `std::sqrt(std::abs(Dot(...)) + v2.squaredNorm())` (a *combined* v⊕v2 norm) rather than a bare `linalg::Norml2(v)` — i.e. the companion is folded into the norm, not just rescaled by it. This is a slightly richer shape than the cited `610-611,617` (where `scale = Norml2(v)` then `v2/scale`); a future abstractor enriching the cohort should distinguish "norm-of-v rescales companion" from "norm-of-(v⊕v2) normalizes both." Does not affect the "no fourth shape that discards-vs-consumes" claim. No action required for this report.

## Repair

### Fixes attempted

- **Finding I1** (cross-reference-integrity, warning): nested same-style triple-backtick fence in Edit 1 — the `verified_against:` YAML payload was wrapped in a ` ```yaml ` fence (CYCLE.md:241, closing :307) nested inside the ` ```edit: ` proposed-changes fence (:239, closing :308). Same-style backtick nesting is the cycle-024 truncation hazard (a naive parse closes the `edit:` block at the inner ` ``` ` and drops the outer close).
  - **Decision**: repaired.
  - **Action**: re-fenced the inner `verified_against:` payload from backtick to tilde, mirroring the sibling-theme convention `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:460` (`~~~yaml`). Applied two surgical edits to `reports/.../CYCLE.md`: line 241 ` ```yaml ` → `~~~yaml`; line 307 inner-closing ` ``` ` → `~~~`. The outer `edit:` fence stays backticks (open :239, close :308). Post-edit fence enumeration: Edit 1 = ` ```edit: ` (239) / `~~~yaml` (241) / `~~~` (307) / ` ``` ` (308); Edit 2 = ` ```edit: ` (315) / ` ``` ` (326). No same-style backtick nesting remains; a backtick-only scan now correctly closes the Edit-1 block at 308 with the full payload enclosed. This is the `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill realized via the tilde-fence variant (the sibling's chosen form for this exact `verified_against:` shape).

- **Finding I3** (F3, repairable): `:811`→`:810-811` line-range parity nudge for the second GMRES Arnoldi path.
  - **Decision**: repaired (within report scope) / routed-for-application (artifact scope).
  - **Action**: the three `:811` occurrences the critic flags live in the **artifact** (`book/src/L1-L0/normalize-mutation-rotation.md:137,174,341`), which is outside repairer write-authority (only the integrator writes `book/`). The report already delivers the F3 correction correctly as a **gated Edit 2** (CYCLE.md:310-326): it quotes the as-found `:811` on the "replace" side and supplies the corrected `:810-811` on the "with" side for all three occurrences, plus the `verified_against:` `partially-supports` row (CYCLE.md:259) carrying the remediation note. I mechanically re-validated the range before recording repaired: `--anchor 'Hj[j + 1] = linalg::Norml2' iterative.cpp:810-811` → 810 and `--anchor 'w *= 1.0 / Hj' iterative.cpp:810-811` → 811 — confirming `:810` carries the `Hj[j+1]=Norml2` half and `:811` the rescale, so Edit 2's `:810-811` is correct. No edit needed inside the report (the fix is authored as a gated edit); the integrator applies it to the theme file at integration. The audit's diagnostic rows (CYCLE.md:92-93, :259) intentionally preserve the as-found `:811` — editing them would desync the verdict from what it audits, so they are left verbatim.

- **Finding I2** (F1, central judgment): does-not-support on `operator.hpp:377-384` lands only on the `normalize_B` rough-in NOTE, which the theme's own Status line scopes OUT of the firm claim; firm status correctly unaffected. The auditor gated F1 to a follow-up abstractor (CYCLE.md:328-334), not enacted in-place — correct lowering-verifier discipline (audit-only, spans two files + touches note substance).
  - **Decision**: not-needed (no repair; the critic confirmed the judgment sound and explicitly directed leaving it gated).

- **Finding I4** (F2): cohort is "illustrative"; no edit forced; resolved as a closed OQ.
  - **Decision**: not-needed (no action; correctly handled by the auditor).

### Unrepairable findings

None. The one warning (I1) was a mechanical fence-fix within repair authority; I3's report-side artifact is already correctly authored as a gated edit and mechanically re-validated; I2/I4 are correctly-gated/no-action items that the critic affirmed need no enactment.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

1. **Edit 1** now uses a tilde-fenced (`~~~yaml`) inner `verified_against:` payload inside the backtick `edit:` block — parse the `edit:` block on its backtick boundaries (open :239 / close :308); the tilde inner block carries the full YAML list. Append it to the end of `book/src/L1-L0/normalize-mutation-rotation.md` (matches the sibling `matrix-weighted-norm-mutation-rotation.md:460` rendering, where the integrated artifact carries the `~~~yaml` block directly).
2. **Edit 2** (F3, mechanical) is in-scope to apply: re-cite the second GMRES path `:811` → `:810-811` at theme lines 137, 174, 341 (range mechanically re-validated by the repairer: `:810`=`Hj[j+1]=Norml2`, `:811`=rescale). This is the artifact-side application of finding I3.
3. **Edit 3 (F1)** is correctly GATED — do NOT apply it here; route to a follow-up abstractor/lifter dispatch (it corrects substantive `normalize_B`-note phrasing across the theme + `book/src/L1/normalize.md`, exceeding integrator-per-report's mechanical-application bar). The firm `## Status` stays `firm` — F1 is on the non-firm note only. OQ `normalize-mutation-rotation-lowering-verifier-audit` is RESOLVED by this dispatch; the F1 follow-up may be tracked as a fresh plan item (precision-fix to the `normalize_B` rough-in note).
