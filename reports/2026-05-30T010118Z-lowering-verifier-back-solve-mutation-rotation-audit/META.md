---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T01:30:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-30T02:00:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "Audit back-solve-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan reports/.../CYCLE.md --quiet` and got `43 ok, 0 failing (43 citations checked)`; also ran `--scan book/src/L1-L0/back-solve-mutation-rotation.md --quiet` to validate the upstream target — `33 ok, 0 failing`. Spot-anchored the two load-bearing pinpoints `palace/linalg/iterative.cpp:653` and `:832` with `--anchor 'for (int i = j'` — both zero-drift. The auditor's per-citation table (lines 65-244) walks all 22 L0 anchors with `--anchor`-style narration and reproduces the citecheck output verbatim at lines 342-364. The diff-based refutation of the brace-placement narrative is itself a verification act: I reproduced `diff <(sed -n '653,660p' iterative.cpp) <(sed -n '832,839p' iterative.cpp)` and got exit-0 / zero output, mechanically confirming the auditor's "byte-for-byte identical" claim. The L1-leaf cross-anchor tightenings (`:78`→`:77-78`, `:218-221`→`:217-221`) are correct — I read the L1 leaf at the relevant ranges and confirm `back_solve` name is on `:77` (the auditor's call) and law-5 header `5. Empty / single-column boundary.` is on `:217` (the auditor's call). The `:466-540` "correct-as-is" call is also correct — `:466` is the opening ` ```yaml ` fence and `:467` is `verified_against:`.

**surface-or-evidence — pass.** This is an audit report (lowering-verifier role), not a refinement-shape proposal. The proposal is exclusively a `verified_against:` evidence-backfill block appended to the theme, plus two routed follow-ups (narrative repair, anchor-precision tightening) — no operator/theme surface is modified by this dispatch. The retroactive-evidence framing is appropriate. The "partially-supports + firm stays" verdict is the correct scoping: Finding A is a defect in **explanatory prose** that justifies a `partially-supports` row for the FGMRES outer-loop citation but does NOT undermine the firm-status rationale (firm-on-positive-structure; laws are syntactic identities on positive source). Indeed, the byte-identical reading **strengthens** law-6 (basis-lift independence) relative to the "+1 line-shift" narrative the theme currently carries, so a status reduction would be a regression. Lowering-verifier's audit-only discipline (UNBLOCK but do not ENACT) is correctly observed — the narrative repair is routed as OQ `back-solve-mutation-rotation-subpattern-b-narrative-repair` for a future lifter/abstractor dispatch.

**rotation-quality — pass (n/a).** No new rotation is proposed. The theme's existing structural rotation (in-place RHS overwrite of `back_solve(R, s) = s'`) is reaffirmed but not modified.

**variant-axis-coverage — pass.** The audit explicitly addresses the GMRES/FGMRES axis pair (Sub-pattern A vs B), the LEFT/RIGHT preconditioning branch axis (cited at `:662-668` LEFT vs `:669-678` RIGHT in Per-citation §:666), the ScalarType element-type axis (applicability-condition 5), and the restart-dimension `j+1` size axis (condition 6 + the empty-cycle / single-column boundary). No hidden branches surface; the auditor explicitly walks the LEFT/RIGHT split at `:666` and the V/Z basis split at `:843` to verify both branches consume the post-back-solve `s[0..j]`, grounding law-6 across all combinations.

**cross-reference-integrity — fail.** The proposed-changes block at lines 372-466 contains a **nested code-fence defect** that is the cycle-024 friction-ledger pattern `firm-chapter-body-authored-outside-proposed-changes-fence` / `convert-nested-fences-to-indented-code-in-proposed-changes-block`. The structure is:

```
372: ```edit:book/src/L1-L0/back-solve-mutation-rotation.md
375:   ```yaml
465:   ```
466: ```
```

Under CommonMark, an inner triple-backtick fence inside an outer triple-backtick fence closes the **outer** fence on first match. Line 465's ` ``` ` closes the `edit:` block at line 372, and line 466's ` ``` ` then opens a *new* unclosed code block (or — depending on the integrator's proposed-changes parser — the entire YAML payload is silently truncated). The auditor's parenthetical at lines 468-472 explicitly acknowledges the nested-fence structure ("the inner `` ```yaml `` ... `` ``` `` is the YAML fence the downstream parser consumes; the outer `` ```edit:… `` ... `` ``` `` is this audit's proposed-changes channel") but **does not apply the cycle-024 repair convention**: nested fences inside a proposed-changes block must be rewritten as indented (4-space) code, or use a different fence backtick count for one of the layers. As shipped, the 89-row `verified_against:` payload (the entire substantive proposal) will not reliably land at integration. Total fence count is 6 (even parity), so a naive fence-balance check passes, but the **semantic intent** of nesting is broken. This is precisely the build-readiness defect the `proposed-changes-fence-encloses-full-body-guard` skill was crystallized to catch.

**edge-label-fidelity — pass.** The proposal carries no edge-label; the report frontmatter scope says "L1>L0 theme audit — back-solve-mutation-rotation" and the prose throughout discusses the L1>L0 edge (L1 `back_solve` leaf lowering into L0 `iterative.cpp:652-660` / `:831-840`). No mismatch.

**plan-kind-consistency — pass.** This is declared as a lowering-verifier audit (no `kind:` frontmatter field, but the scope frame + `proposed changes = verified_against block + routed follow-ups` matches the audit shape exactly). The content shape is consistent: per-citation table → applicability conditions → algebraic laws → named findings → proposed verified_against block → routed follow-ups. Audit-only discipline is observed (no surface authoring, no operator promotion, the narrative repair is routed not enacted). The `partially-supports` overall verdict is internally consistent with one Finding A `partially-supports` row plus three Finding B precision-tightening notes plus 21 zero-drift `supports` rows.

**skill-uptake-survey — warning.** The auditor invokes `tools/citecheck/citecheck.py --anchor` 27 times (correctly addressing the producer-citation-drift friction) and references the cycle-024 mechanical-check invariant. However, the auditor does NOT invoke or reference the cycle-021 `proposed-changes-fence-encloses-full-body-guard` skill or the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill — both of which would have flagged the cross-reference-integrity defect above before the report shipped. Lowering-verifier role spec does cite the verify-citation-range skill (invoked) and the partly-constructive-promotion-checklist skill (not applicable — no promotion proposed). Pure surface check — not blocking on its own — but the nested-fence defect would have been self-caught had the proposed-changes-fence-guard skill been invoked. The auditor's parenthetical acknowledgment of the nesting (lines 468-472) shows awareness of the convention but stops short of applying it.

### Issues found

1. **(CYCLE.md:372-466) Nested triple-backtick fences in proposed-changes block — build-readiness defect.** The ` ```edit:book/src/... ` outer fence at :372 contains a ` ```yaml ` inner fence at :375. Under CommonMark, the first ` ``` ` close at :465 terminates the OUTER `edit:` block (not the inner `yaml`), and the stray ` ``` ` at :466 opens a new unclosed code block. Either:
   - the integrator parses the edit and gets an empty / truncated YAML payload (the entire 89-row `verified_against:` proposal silently drops), OR
   - the integrator's tolerant parser DTRT but the rendered mdBook (after the YAML lands in the theme, where it is correctly a single-level ` ```yaml ` fence) is fine while THIS REPORT's rendering carries a broken trailing code block.
   
   Severity: **fail** (load-bearing — this is the entire substantive proposal). The cycle-024 friction-ledger pattern requires the inner nested content to be rewritten as 4-space indented code OR to use a different backtick count for one of the fences (e.g., outer ` ````edit:... ` four-backtick / inner ` ```yaml ` three-backtick). The auditor's parenthetical at :468-472 acknowledges the nesting structure but did not apply the cycle-024 repair convention. The `proposed-changes-fence-encloses-full-body-guard` skill (cycle-021) and the `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill (cycle-024) directly address this case.

2. **(CYCLE.md:333) Finding B repair text contradicts itself.** Finding B (lines 322-333) describes three off-by-one anchor imprecisions and concludes "Repair: bulk-edit the L1 cross-anchor list to use `:77-78`, `:217-221`, `:466-540` (the third was already correct as a range; only the first two need tightening)." This is internally consistent. However, the Finding B opening text at :329 says "`:466-540` → confirm as `:466-540` (correct as the full fenced block; `verified_against:` keyword is at :467 inside the :466 fence)" — confirming the third anchor is correct. The proposed bulk-edit then lists `:466-540` as one of the three to "use", which is benign (it's a no-op for that one), but a reader could misread it as "all three need tightening." Severity: **warning** (low — cosmetic prose ambiguity in the repair instruction; the substance is correct). Repair-only-the-first-two phrasing would be clearer.

3. **(CYCLE.md:108-109, 304-321) Theme self-contradiction surfaced but routed (rather than enacted).** The auditor correctly identifies that `book/src/L1-L0/back-solve-mutation-rotation.md` is internally self-contradictory: at theme :203 the FGMRES code-block annotation says `// :833 opening brace on its own line`, while at theme :219-229 the "Brace placement / line shift" bullet attributes the line offset to GMRES putting `{` at the end of the for line. Both cannot be true. The audit also notes that the L1 leaf at `:225-226` has the correct "line-for-line identical" phrasing — so the theme contradicts BOTH its own annotation AND the L1 leaf it cites as authority. The auditor's routing of this as a narrative-only follow-up (OQ `back-solve-mutation-rotation-subpattern-b-narrative-repair`) is the correct discipline call per lowering-verifier role spec (audit-only; UNBLOCK but do not ENACT). However, the contradiction is **not just narrative housekeeping** — the theme actively misrepresents the source as having a brace-style difference that doesn't exist, which would mislead any downstream lifter/abstractor reading the theme as authoritative. This intensifies the priority of the routed follow-up (it should be near the top of the cycle-030 plan candidates, not low-priority "cosmetic" as currently framed at :490). Severity: **warning** (correctness of routing is fine; severity framing is under-stated).

4. **(CYCLE.md:370 + :468-472) Parenthetical "downstream parser parses by fence" claim is unverified.** Lines 468-472 assert that "downstream `cross-layer-cross-cutter` parses by fence" as justification for the nested ` ```yaml ` inside the ` ```edit: ` outer fence. This is an unanchored claim about an unnamed downstream parser's behavior; no test-linkage, no role-spec citation, no integrator-finalize parser code reference. Combined with Issue 1, this suggests the auditor knew the nested fence was load-bearing for downstream consumption but did not validate the integrator's actual parsing behavior (or substitute a known-safe encoding per the cycle-024 skill). Severity: **warning** (the assertion itself is plausibly correct — themes DO carry top-level ` ```yaml verified_against ` blocks elsewhere — but the nested-fence-inside-proposed-changes-block encoding is not the same problem, and the conflation is the bug).

5. **(CYCLE.md frontmatter line 6: `status: pending`)** The report's frontmatter `status: pending` is in keeping with pre-critic norms, but the post-finding-A flow (per-citation `partially-supports` on `:832`, audit overall `partially-supports`) is not reflected in any frontmatter field. The critic/repairer pipeline will set `overall_status` in META.md (not CYCLE.md), so this is in scope of the repairer/integrator handoff and not a critic concern; noted for context, not as an issue.

## Repair

### Fixes attempted

- **Finding**: Issue 1 — Nested triple-backtick fences in proposed-changes block (CYCLE.md:372-466). Inner ` ```yaml ` at :375 + closing ` ``` ` at :465 mis-toggles the outer ` ```edit: ` at :372 under CommonMark, risking silent truncation of the 89-row `verified_against:` payload at integration. Severity: fail / load-bearing.
  - **Decision**: repaired.
  - **Action**: Applied skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` option (b) — removed the inner ` ```yaml `/` ``` ` fence pair (old CYCLE.md:375 + :465) and prefixed every YAML content line with 4 spaces (CommonMark indented-code form). All 89 rows of `verified_against:` payload preserved byte-for-byte (content unchanged: keys, citation paths, verdicts, audited_at timestamps, notes — only the indentation mechanism changed from fence-delimited to indent-delimited). Added an explicit `NOTE TO INTEGRATOR` line inside the block + an updated trailing parenthetical (replacing the previous "nested-yaml" parenthetical at old :468-472) instructing the integrator to re-fence the payload as a top-level ` ```yaml … ``` ` block when materialised in the target chapter file (channel-format requirement: `cross-layer-cross-cutter` parses chapter by fence — the chapter file's TOP-LEVEL `verified_against:` fence is unaffected by this repair; only the report's proposed-changes block encoding changes). Post-edit fence audit: line-leading ` ``` ` count is 4 (was 6), pairing into exactly 2 closed blocks (`:341-364` citecheck output + `:372-466` edit:), each well-formed, no nesting. The `verified_against:` payload's data integrity preserved end-to-end; the only thing that changed is the wire encoding from the report to the integrator's apply step.
  - **File touched**: `reports/2026-05-30T010118Z-lowering-verifier-back-solve-mutation-rotation-audit/CYCLE.md` (lines 372-472 → 372-468 in the repaired file).

- **Finding**: Issue 2 — Finding B repair text cosmetic ambiguity (CYCLE.md:333). The bulk-edit line lists `:466-540` alongside `:77-78` and `:217-221` even though `:466-540` is already correct as a range. Severity: warning / cosmetic.
  - **Decision**: not-needed.
  - **Rationale**: Critic flagged as optional / low-severity cosmetic prose ambiguity; the substance of the repair instruction is correct (the parenthetical immediately following clarifies that only the first two need tightening). Per task framing, this is explicitly marked "optional". Leaving as-is to keep repair surface surgical and avoid touching authored content.

- **Finding**: Issue 3 — Theme self-contradiction at back-solve-mutation-rotation.md:203 vs :219-229 (CYCLE.md:108-109, 304-321). Critic notes the auditor under-stated severity but routed the narrative repair correctly as an OQ.
  - **Decision**: not-needed.
  - **Rationale**: Per task framing, the auditor's audit-only discipline is correct (lowering-verifier UNBLOCKs but does not ENACT). The narrative repair of the theme is a c031 follow-up (a future lifter/abstractor pass); leaving the routed OQ intact. NOTE: the cycle-030 dispatch-4 abstractor (ls-update-column-mutation-rotation) independently flagged the sibling brace error — so the pattern is independently surfaced and queued. Not in scope of THIS repair.

- **Finding**: Issue 4 — Unverified "downstream parser parses by fence" parenthetical (CYCLE.md:370 + :468-472). Severity: warning / optional tightening.
  - **Decision**: repaired (incidentally, as part of Issue 1's repair).
  - **Action**: The original parenthetical at old :468-472 (conflating the report-side nested-fence encoding with the chapter-side top-level `verified_against:` fence consumption) has been replaced by a tighter parenthetical (new CYCLE.md:468) that distinguishes the two: the report-side proposed-changes block uses 4-space-indented code to avoid mis-toggling, while the chapter-side `verified_against:` lands as a top-level ` ```yaml … ``` ` block that the `cross-layer-cross-cutter` parses by fence. The conflation Issue 4 identified is dissolved by the indented-code encoding (the report's encoding choice is now decoupled from the chapter's fence requirement); this also addresses the warning incidentally.

- **Finding**: skill-uptake-survey warning — proposed-changes-fence skills not invoked at production time.
  - **Decision**: repaired.
  - **Action**: The Issue 1 repair above is a direct application of skill `convert-nested-fences-to-indented-code-in-proposed-changes-block` (cycle-024) and aligns with the detection guard `proposed-changes-fence-encloses-full-body-guard` (cycle-021). Skill uptake is now reflected in the repaired report: the new in-block NOTE and the new trailing parenthetical both cite the skill by name. This is telemetry-fix (the defect is repaired and the skill invocation is now visible in the artifact); the **production-time** uptake gap (the auditor did not invoke the skills at producer time) is real but is a methodology signal for the meta-phase, not a per-report repair concern.

### Unrepairable findings

None. The single load-bearing finding (Issue 1, cross-reference-integrity fail) was repairable via the cycle-024 promoted skill; the three warning findings are either repaired-incidentally (Issue 4), correctly-routed-not-mine (Issue 3), or optional-cosmetic-deferred (Issue 2). No follow-up agent required for the report itself; the routed OQ for theme narrative repair remains the auditor's correct routing and is queued in the cycle-030 OQ ledger as `back-solve-mutation-rotation-subpattern-b-narrative-repair` for a future lifter/abstractor.

## Suggested resolution

`ready` — the load-bearing nested-fence defect is repaired (the 89-row `verified_against:` payload now sits cleanly inside a single, well-formed ` ```edit: ` proposed-changes block). The integrator-per-report should:

1. Apply the proposed `verified_against:` payload to `book/src/L1-L0/back-solve-mutation-rotation.md` per the `NOTE TO INTEGRATOR` inside the block — re-fence the 4-space-indented YAML as a top-level ` ```yaml … ``` ` block in the chapter file (strip leading 4 spaces per line of payload; preserve content byte-for-byte).
2. File OQ `back-solve-mutation-rotation-subpattern-b-narrative-repair` (per auditor's routing; the narrative repair is c031 follow-up scope, NOT this cycle's integrator).
3. Optionally pick up the three L1 cross-anchor precision tightenings (Finding B: `:78` → `:77-78`, `:218-221` → `:217-221`; the `:466-540` entry is already correct) as a small repair-pass while applying. Low priority; safe to defer.

The audit's overall verdict `partially-supports` is correctly scoped to the FGMRES Sub-pattern B narrative defect and does NOT block the firm landing of the theme — the firm status holds (laws are syntactic identities on positive source per the firm-on-positive-structure rationale).
