---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T07:27:19Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T07:30:07Z
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

# META: verification of "Audit axpbypcz-mutation-rotation (enact callsite corrections + firm)"

## Critique

### Checks run

**citation-validity — pass.** I independently re-verified every load-bearing citation against `reference/` Palace source via `palace-codemap` `read_range` and `tools/citecheck/citecheck.py` (bounds + anchor), not transcribing from the report. The three gate reclassifications all hold:
- `slepc.cpp:1986` — `read_range` shows `ctx->y1.AXPBYPCZ(ctx->gamma/ctx->sigma, ctx->y2, -ctx->gamma/ctx->sigma, ctx->x1, 0.0)`. The 5th (γ) slot is a literal `0.0`; `-gamma/sigma` occupies the 4th (β) slot. The cycle-021 "γ≠0 runtime" reading was wrong; **γ=0 is correct.** `citecheck --anchor "AXPBYPCZ"` lands line-exact at 1986. (Note: the statement wraps onto line 1987 where the `0.0` literally sits; citing the statement-start line 1986 is the established convention and is fine.)
- `nleps.cpp:343-344` — `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())` + `.Imag()` sibling at 344. `.Real()`/`.Imag()` are real `Vector` halves, scalars `double`, γ=1.0 → real-real free-fn → **sub-pattern A** (D→A confirmed). `citecheck --anchor "X[j].Real()"` lands at 343.
- `romoperator.cpp:188-189` — `linalg::AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())` + `.Imag()` sibling. `V` is `const std::vector<Vector>&` (sig at 178-180, in-bounds), `u.Real()` a real `Vector` half, γ=1.0 → real-real **sub-pattern A** (D→A confirmed). The odd-`n` AXPY companion at 193-194 (`linalg::AXPY(y(j).real(), V[j], u.Real())`, anchor lands at 193) corroborates `V`'s real-`Vector` element type.

Correction-6 range independently confirmed: `read_range` of `vector.cpp:400-432` shows `if (gamma == 0.0)` at 402, the closing `}` of the γ==0 outer block at **427**, `else` at 428, `{` at 429. So **402-427 is the exact γ==0 block** and the cycle-021 draft's `402-429` would over-cover into the `else`/γ≠0-open lines — the report's correction is right. The decl/body/kernel backbone all land verbatim: member decl `vector.hpp:133-136`, static decl `vector.hpp:144-146`, free-fn decl `vector.hpp:313-316`, outer trampoline `vector.cpp:381-386` (delegates at 385), static body `388-455`, real-real `745-758` (γ==0 fast-path `add(...,z)` at 751, γ≠0 split at 755-756), complex-complex `760-765`, real-on-complex `767-772`, and the MFEM `add(alpha,x,beta,y,y)` at 729. `citecheck` confirms all 23 report citations in-bounds (0 OOB) and anchor-confirms the make-or-break pinpoints (402 `gamma == 0.0`, 729, 751, 1986). The corpus census (`search_text "AXPBYPCZ\("`) reproduces the report's 13-site enumeration exactly: timeoperator{139,217,273}, arpack{772,787}, nleps{343,344,471,676,693}, slepc{1986}, romoperator{188,189}; remaining hits are decls/internal delegations (vector.hpp{134,144,315}, vector.cpp{381,385,388,746,761,764,768,771}), correctly excluded.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (rough-in→firm flip of an existing theme). The proposal both modifies surface (the full chapter text is rewritten with corrections 1-6 applied + a fresh `## Status` flip to firm) AND backfills retroactive evidence (the appended `verified_against:` block). Both halves of the disjunction are satisfied; not a pure rotation_claim. Pass.

**rotation-quality — pass.** Not the primary axis for a lowering-theme audit, but the theme does assert the mutation rotation L1→L0: the pure functional `axpbypcz(α,x,β,y,γ,z_old)` (no destination buffer) is the strictly-more-abstract form, and the L0 forms are the in-place receiver/output-arg kernels with state threaded through `z`. The γ==0 sub-rule additionally compresses to the more-abstract `axpby` form by law #1. This is genuine state-hiding / threaded-state compression, not a 1:1 rename. Pass.

**variant-axis-coverage — pass.** The orthogonal axes are exhaustively covered: element-type/dispatch shape (4 sub-patterns A real-real / B complex free-fn / C complex member / D real-on-complex) and the γ==0 vs γ≠0 control-flow branch. The corpus census makes the coverage exact rather than illustrative: every one of the 13 sites is classified; B and D are explicitly scoped as defined-not-used recognition rules (positively-cited overloads with a census showing zero callers); the inner imaginary-scalar fast-paths (`ai==0&&bi==0`, `gi==0`) are explicitly classified as transparent performance specialisations, not separate sub-patterns. No hidden branches — the static-body `read_range` (388-455) shows exactly the outer γ==0 branch and the two inner imaginary-scalar branches the report describes. Pass.

**cross-reference-integrity — pass (including the firm-body-inside-fence build-readiness guard).** All `[link]` references resolve: `../L1/axpbypcz.md`, `../L1/axpby.md`, `../L1/axpy.md`, sibling `axpby-mutation-rotation.md` all exist; the chapter is wired into `SUMMARY.md:75`; the index.md edit targets the real dep-map row 19 (verbatim match to the current rough-in row). L1/axpbypcz law #1 and the "Laws that explicitly do not hold" IEEE-order non-law the report cites both exist in the anchor.
  Build-readiness fence guard (special attention this cycle): I enumerated fences with `grep -n '\`\`\`'` → markers at 141 (`edit:axpbypcz...`), 464 (`yaml`), 554, 555, 557 (`edit:index`), 560 — **6 markers, even parity.** The intended pairing is 141↔555 (the `edit:` chapter fence) enclosing a nested 464↔554 (`yaml` verified_against) block, then 557↔560 (the index.md row). The full firm apparatus sits INSIDE the chapter fence: `## Status` (line 445), the lowering rule + 4 sub-patterns + γ==0 sub-rule (143-443), and the `verified_against:` yaml (464-554) are all between the `edit:` open (141) and close (555). None of the firm body is authored as the report's own top-level sections (the report's own Summary/Per-citation-audit sections at 19-130 are separate from the in-fence chapter). This is NOT the cycle-019 fence-truncation defect. Crucially, this nested-fence shape (`edit:` → nested `yaml` → `\`\`\`` → `\`\`\``) is **byte-for-byte the same structure** the cycle-021 sibling report (`...axpby-axpbypcz-firm/CYCLE.md` lines 171/174/212/213) used, which integrated cleanly — the landed `axpby-mutation-rotation.md` contains the resulting fenced yaml block (lines 173-211). So the integrator's `edit:`-parser is known to handle this nesting. Pass. (See Issues — a low-severity hardening note on the bare adjacent `\`\`\``/`\`\`\`` at 554-555 vs. the sibling's `## Verified-against`-header framing.)

**edge-label-fidelity — pass.** The edge is L1>L0 (`axpbypcz-mutation-rotation`). The chapter's `## L1 form (LHS)` / `## L0 form (RHS)` headers, the "Lowers the pure L1 form ... into Palace's L0 ... forms" framing, and the forward narration (L1 pure → L0 kernels) all discuss exactly the L1→L0 edge. OQ #5 explicitly affirms clean high→low direction-of-definition. No mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit proposing a firm flip; content shape matches. The `## Status` block carries no rough-in placeholders — it states the exhaustive census, the defined-not-used scoping for B/D, the live γ≠0 non-law, and explicitly disclaims any constructive sub-part (so `firm`, not `partly-constructive`, is the right tier: there is no negative-anchor reconstruction — B/D are positively-cited overloads with a zero-caller census). The single residual (MFEM `add` alias-safety) is correctly carried as an out-of-Palace-scope OQ, not a firm-blocker, consistent with CLAUDE.md's MFEM-resolves-upstream policy. Classification is sound. Pass.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report's shape implies two relevant skills: `verify-citation-range` (the audit re-reads/anchor-checks 23 citations — squarely its territory, including its "Audit-report / inherited-citation sub-case") and `proposed-changes-fence-encloses-full-body-guard` (the report explicitly self-applies the batch-5 fence-guard at lines 137-139). Neither skill is named by its slug. The report does reference its mechanical tooling (`palace-codemap` `read_range`/`search_text`, `tools/citecheck/citecheck.py`) thoroughly, so the underlying procedures were clearly followed — this is a naming/telemetry gap, not a substantive uptake gap. Pure presence check; surfaced, not blocking.

### Issues found

1. **(low / cosmetic-hardening; cross-reference-integrity) Bare adjacent close-fences at CYCLE.md:554-555 vs. the sibling's section-header framing.** The nested `verified_against:` yaml closes at 554 and the `edit:` chapter fence closes at 555 with two bare adjacent ` ``` ` lines and no intervening `## Verified-against` (or equivalent) section header preceding the `yaml` open at 464 — the yaml block is appended directly after the `## Status` prose (462) with only a blank line. The landed sibling `axpby-mutation-rotation.md` places its fenced yaml under an explicit `## Verified-against` header (line 152) with `## Status` AFTER it (line 226). Here the order is inverted (`## Status` at 445, then the headerless yaml at 464-554), so the firmed chapter will carry a fenced yaml block with no section header introducing it. This integrates fine (the structure matches the cycle-021 precedent that landed cleanly) and is purely a chapter-readability/consistency nit — the repairer may optionally insert a `## Verified-against` header before line 464 to match the sibling's shape. Not a build-readiness blocker.

2. **(low / skill-uptake; non-blocking) Relevant skills not referenced by slug.** `verify-citation-range` and `proposed-changes-fence-encloses-full-body-guard` are both implied by the report's shape (23-citation re-audit; explicit self-application of the fence guard) but are not named. The procedures were demonstrably followed via the underlying tooling (`citecheck`, `read_range`, the fence-enclosure note at 137-139); this is a telemetry/naming gap only.

3. **(informational, not a defect; citation-validity) slepc.cpp γ-slot literal physically sits on line 1987.** The `slepc.cpp:1986` citation points at the statement-start line; the `0.0` γ literal is on the wrapped continuation line 1987. The pinpoint is correct under the cite-the-statement-start convention and `citecheck --anchor "AXPBYPCZ"` confirms 1986, so this is not drift — noted only so a future reader auditing the literal does not expect to find `0.0` on 1986 alone.

---

## Repair

### Fixes attempted

- **Finding 1** (cross-reference-integrity / cosmetic-hardening): the firmed chapter's fenced `verified_against:` yaml block had no `## Verified-against` section header introducing it — appended directly after the `## Status` prose with only a blank line, where the landed cycle-021 sibling `axpby-mutation-rotation.md` places its yaml under an explicit `## Verified-against` header.
  - **Decision**: repaired.
  - **Action**: Inserted a `## Verified-against` section header inside the `edit:` fence, immediately before the nested ```yaml verified_against:``` open. Edit applied to `reports/<id>/CYCLE.md` proposed-changes block `edit:book/src/L1-L0/axpbypcz-mutation-rotation.md` (between the `## Status` prose and the yaml fence). This is a surgical one-line insertion that matches the sibling's `## Verified-against`-header framing verbatim (sibling `axpby-mutation-rotation.md:152`). Verified the fix is mechanical-only: the `## Status`-before-`## Verified-against` ordering is left as-authored (the critic confirmed the inverted order "integrates fine"; reordering would be substantive restructuring, out of repair scope). Fence parity re-checked: 6 markers, even (141 `edit:` ↔ 557 close enclosing nested 466 `yaml` ↔ 556, then 559 `edit:index` ↔ 562) — the header is a non-fence line inside the `edit:` fence, so it lands in the firmed chapter and does not perturb the integrator's `edit:`-parser pairing.

- **Finding 2** (skill-uptake-survey / telemetry, non-blocking): `verify-citation-range` and `proposed-changes-fence-encloses-full-body-guard` skills were followed-in-substance (23-citation re-audit via `citecheck`/`read_range`; explicit self-application of the fence guard at CYCLE.md:137-139) but not named by slug.
  - **Decision**: not-needed (record-only).
  - **Rationale**: Naming/telemetry gap only — the underlying procedures were demonstrably executed (the report cites `tools/citecheck/citecheck.py`, `palace-codemap read_range`/`search_text`, and the fence-enclosure note). Adding skill-slug labels to an integrated-pending report is not a mechanical correctness fix and would edit substantive narrative; per the critic this is a pure presence/telemetry check, non-blocking. No edit. (Recurrence already surfaced in the critic's telemetry channel; no new skill-candidate warranted from a single instance.)

- **Finding 3** (citation-validity / informational): the slepc γ-literal `0.0` physically wraps onto continuation line 1987; the `slepc.cpp:1986` pinpoint cites the statement-start line per the established cite-the-statement-start convention.
  - **Decision**: not-needed (record-only).
  - **Rationale**: Explicitly not a defect — `citecheck --anchor "AXPBYPCZ"` confirms 1986 line-exact and the convention is to cite the statement-start line. The report itself already documents the wrap (META critique line 23, CYCLE.md sub-pattern-C citation note). No edit.

### Unrepairable findings

None. The sole actionable finding (1) was mechanically repairable in-place; findings 2 and 3 are telemetry/informational record-only items, not repair targets.

## Suggested resolution

`ready`. All 7 substantive checks passed at critique; the lone `warning` (skill-uptake-survey) is telemetry-only and non-blocking. The one cosmetic-hardening finding (missing `## Verified-against` header) is now repaired in-place to match the landed sibling's shape, with fence parity preserved.

Notes for the integrator:
- This is a well-evidenced rough-in→firm flip closing the BLAS-1 L1>L0 floor **7/8 → 8/8** (`blas1-l1-l0-lowering-theme-gap`); the floor OQ can be marked closed (CYCLE.md Open-questions #2).
- The proposed-changes block carries two `edit:` fences: the full firmed chapter `book/src/L1-L0/axpbypcz-mutation-rotation.md` (now with the `## Verified-against` header inside the fence) and the `book/src/L1-L0/index.md` dep-map row-19 firm-flip. Both target verbatim-matching current content per the critic's cross-reference-integrity pass.
- Residual OQs to promote: MFEM `add(α,x,β,y,z)` alias-safety (out-of-Palace-scope, not a firm-blocker; CYCLE.md OQ #3) and the sibling-theme naming nuance `axpby-theme-covers-axpy-family-naming` (CYCLE.md OQ #4, untouched by this dispatch).
