---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T112000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T113000Z
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

# META: verification of "Formalize eigsolve at L3" (L3 eigsolve partial-obstruction backfill)

## Critique

### Checks run

**citation-validity — warning.** I spot-checked every load-bearing citation verbatim against Palace source via the `palace-codemap` `read_range` / `search_text` tools (this batch carries live inline-anchor-drift friction). The **enclosing range citations are all correct** — `arpack.cpp:562-590` (`ApplyOp` body), `:263-402` (RCI loop), `:579-581` (shift-invert branch), `:572-575` (no-transform branch); `slepc.cpp:687-709` (`Solve`), `:1847-1876` (`__pc_apply_EPS`), `:1801-1827` (shell matvecs), `:379-394` (`SetShiftInvert`), `:711-716` (`GetEigenvalue`), `:671-685` (`Customize`). The boundary/anchor structural claims are faithful to source: `EPSSolve(eps)` at `slepc.cpp:694` ✓, `naupd` at `arpack.cpp:318` ✓, `iparam[6] = sinvert ? 3 : 1` at `:273` ✓, `which::largest_magnitude` at `:278` ✓, `STPRECOND`/`STSINVERT` at `:384`/`:388` ✓, `return l * gamma` at `:715` ✓, `EPSSetTarget(eps, sigma/gamma)` at `:674` ✓, `STSetMatMode(...ST_MATMODE_SHELL)` at `:391` ✓, `x1.Set(px, n, false)` at `:570` ✓, `y1.Get(py, n, false)` at `:589` ✓, both `opInv = &ksp` bindings at `arpack.cpp:193` / `slepc.cpp:366` (both inside their cited `:191-194` / `:364-367` ranges) ✓. However **five single-statement spot citations are off-by-one** (the inline-anchor-drift signature) — see Issues 1–5. In every case the *enclosing range* the report also gives is correct, so no claim is ungrounded, but the precise line pointers are wrong and would mislead a reader/auditor jumping straight to the cited line. Net: not a fail (every claim has a real, in-range supporting anchor), but a warning for the drifted spot anchors.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (it refines the cycle-023 `stub` at `book/src/L3/eigsolve.md` in place). It modifies surface (replaces the entire stub body with a full `partial-obstruction` chapter: Signature, Semantics, Algebraic laws, Status, Evidence) AND carries the rotation/lift evidence (the §"Lifts from" / §"Lowers to" identity-in-form rotation against the firm L2 body, plus positive-source body anchors). It is not a pure rotation_claim without surface. Pass.

**rotation-quality — pass (identity-lowering backfill kind).** The report does NOT assert a compaction rotation across the L3↔L2 edge; it asserts the body is **identity-in-form** to the firm L2 `apply_shift_invert` composition, with the only surface adjustment being that L3 renders the (un-liftable) eigen-iteration loop as an explicit obstruction marker where L2 names the fold by role. Per the CLAUDE.md invariant "Identity-lowerings still require both L levels," this layer-coherence backfill is a legitimate report-kind that is explicitly NOT required to be a strictly-more-compact rotation — the recognized verdict is identity-in-form + an in-line non-adjacent-identity annotation, matching the `chebyshev` and `krylov-step` precedents (both verified: `book/src/L3/chebyshev.md` frontmatter `lowers_to:` "no L3-L2 theme file — in-line annotation"; `:438-474` §Status/§Downward). The "added information" of the rotation is real (the explicit `sequential-obstruction` marker + the value-threaded whole-tensor body rendering), so this is not a renaming-only 1:1 mapping presented as a compaction. Pass for the identity-lowering report-kind.

**variant-axis-coverage — pass.** The entry enumerates five variant axes (spectral-transformation, problem-type, backend-orchestration, element-type, scaling) in both the frontmatter and §"Variant axes", matching the firm L2 entry's profile. Three are opened at the body surface, two are collapsed/informational, and each is either covered with a source witness or explicitly scoped out (element-type "complex only — inherited"; the `nonlinear`/NEP problem-type sub-case is named and routed to the existing `apply_nonlinear_pencil` operand). The backend-orchestration axis (arpack-rci vs slepc-st-shell) is the load-bearing one and both branches are witnessed at distinct source sites. No hidden branches. Pass.

**cross-reference-integrity — warning.** Most links resolve: `L3/chebyshev.md`, `L3/krylov-step.md`, `L3/ksp_solve.md`, `L3/apply_linop.md`, `L2/eigsolve.md`, `L1/eigsolve.md`, `L4/iterate-while.md`, `L1/apply_nonlinear_pencil.md`, and all six cited concept pages (`sequential-obstruction`, `tensor-field-lift`, `constructed-operators`, `solver-as-operator`, `variant-absorption`, `solve-monad`) all EXIST. The dep-map row insert into `L3/index.md` and the SUMMARY insert are well-formed. **But the report contains six live markdown links to `../L4/eigsolve.md`, which does NOT exist** (lines 44, 59, 103, 197, 228, 239 of CYCLE.md). A live `[eigsolve](../L4/eigsolve.md)` link to a missing file is a hard `linkcheck2` build error per the friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — even though the surrounding prose correctly and repeatedly frames the L4 entry as "not yet authored / future dispatch." See Issue 6. Build-readiness guard (firm-body-inside-fence): N/A-as-fail and PASS — the entry is `partial-obstruction` not `firm`, and regardless the `## Status` + Signature + Algebraic-laws + Evidence apparatus is fully ENCLOSED inside the `edit:book/src/L3/eigsolve.md` fence (line 25 open → line 263 close; `## Status` at line 214 is inside). Fence enumeration: 12 backtick fences, even parity, three properly-nested `text` code fences inside the chapter fence; the post-fence "## Operator content" (line 276+) is an explicitly-labeled summary recap, not body authored outside the fence. This is NOT the cycle-019 fence-truncation defect. The warning is solely for the dead L4 links.

**edge-label-fidelity — pass.** The frontmatter declares `lifts_from: L2/eigsolve.md` and `lowers_to: L2/eigsolve.md`, and the prose discusses exactly the L3↔L2 edge throughout (§"Lifts from", §"Lowers to", §"L3 vs L2 distinction"). The §"L3 vs L4 distinction" correctly scopes the (absent) L3↔L4 edge as future. The non-adjacent-identity discussion correctly establishes that the body identity stops at L3↔L2 and does NOT extend transitively to L1 (because the L2↔L1 edge is non-identity) — I verified this against `L2/eigsolve.md:157` §Status ("The L2↔L1 rotation is **non-identity**") and §"Lowers from". No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is a harvester L3 operator entry landing status `partial-obstruction`. The content shape matches: a real operator definition with full Signature/Semantics/Algebraic-laws/Status/Evidence apparatus, no rough-in placeholders. The `partial-obstruction` status is correctly applied per the CLAUDE.md status-tier definition ("an operator whose per-step body lifts cleanly to a global tensor-field expression but whose loop structure does NOT lift … the status reflects the loop structure, not the body"): the body is documented identity-in-form + whole-tensor lifting (laws 1, 2, 4, 5 are syntactic identities on positive source), and the eigen-iteration loop is a witnessed `sequential-obstruction`. The report correctly distinguishes this from `firm` (loop doesn't lift), from full `obstruction` (operator IS implemented, body DOES lift), and from `rough-in (test-coverage-bounded)` (the §Status "Caveat" paragraph explicitly argues the body laws are syntactic identities on positive source, not test-gated convergence semantics — the firm-on-positive-structure escape). Status classification is sound. Pass.

**skill-uptake-survey — warning.** The report's shape (a refinement-surface operator entry + a rotation/lift claim + heavy citation verification) implies several relevant skills exist: `verify-citation-range`, `verify-refinement-surface`, `verify-rotation-citation`, `classify-variant-axis`. The Evidence section asserts "All citations self-verified against source this dispatch via codemap `get_symbol_def` + `read_range`" — which is the substance of `verify-citation-range` — but no skill is named by slug, and given the five off-by-one citation drifts that survived this self-verification, the self-verification was evidently not a line-exact pass. Pure telemetry surface (non-blocking): the verification *activity* is referenced but no skill invocation is cited, and the drift indicates the citation-range check did not catch the off-by-one anchors. Warning (surveyed, not blocking).

### Issues found

1. **Off-by-one: `opK->Mult(x1, z1)` no-transform branch.** CYCLE.md cites this at `arpack.cpp:572` (signature shape-contract §, line 93: "`K` (`palace/linalg/arpack.cpp:572` `opK->Mult(x1, z1)`)"; the `:572-575` range form recurs at lines 79-comment context / 205 / 245). **Actual line is 573** (`search_text` confirms `opK->Mult(x1, z1)` at `arpack.cpp:573`). The `:572-575` enclosing range is correct; only the implied `:572` start-of-statement pointer is wrong. Note the firm L2 entry got this right (`L2/eigsolve.md:99` cites `:573-575`). Severity: low (range valid; spot pointer drifted). Location: CYCLE.md §Signature line 93, §"Variant axes" line 205, §Evidence line 245.

2. **Off-by-one: `opM->Mult(x1, z1)` shift-invert branch.** CYCLE.md cites this at `arpack.cpp:580` in three places (§Signature line 93 `op.operand` "`opM->Mult(x1, z1)` (`palace/linalg/arpack.cpp:580`)"; §Dependencies line 181 "`palace/linalg/arpack.cpp:573, 580`"; §Dependencies line 182 "`opM->Mult(x1, z1)` (`palace/linalg/arpack.cpp:580`)"; §"Variant axes" line 211). **Actual line is 579** (`search_text` confirms `opM->Mult(x1, z1)` at `arpack.cpp:579`). The `:579-581` enclosing range used elsewhere (lines 19, 157, 245) is correct; the `:580` spot pointer is off by one. Severity: low. Location: CYCLE.md lines 93, 181, 182, 211.

3. **Off-by-one: ARPACK max-iteration `iparam[2] = arpack_it`.** CYCLE.md cites this at `arpack.cpp:269` (§Semantics line 119 "`iparam[2] = arpack_it` … (`palace/linalg/arpack.cpp:269`)"; §Evidence line 246 "max-iteration `iparam[2] = arpack_it` (`:269`)"). **Actual line is 270** (`search_text`: `iparam[2] = (a_int)arpack_it;` at `arpack.cpp:270`). Severity: low. Location: CYCLE.md lines 119, 246.

4. **Off-by-one: SLEPc `__pc_apply_EPS` `FromPetscVec(x, ctx->x1)`.** CYCLE.md cites this at `slepc.cpp:1856` (§Signature line 96 "SLEPc: `FromPetscVec(x, ctx->x1)`, `palace/linalg/slepc.cpp:1856`"; §Evidence line 248 "`FromPetscVec(x, ctx->x1)` (`:1856`)"). **Actual line is 1857** (`search_text`; line 1856 is the blank line preceding it). The `:1847-1876` enclosing range is correct. Severity: low. Location: CYCLE.md lines 96, 248.

5. **Off-by-one: SLEPc `__pc_apply_EPS` `ToPetscVec(ctx->y1, y)`.** CYCLE.md cites this at `slepc.cpp:1872` (§Signature line 97 "SLEPc: `ToPetscVec(ctx->y1, y)`, `palace/linalg/slepc.cpp:1872`"; §Evidence line 248 "`ToPetscVec(ctx->y1, y)` (`:1872`)"). **Actual line is 1873** (`search_text`). The enclosing range is correct. Severity: low. Location: CYCLE.md lines 97, 248. (Note: the in-range anchors I confirmed exact in this same body — `opInv->Mult` at `:1858`, `opProj->Mult` at `:1870`, un-scale `:1861`/`:1865`, A0/A1 `:1809-1810`/`:1824-1825` — are all correct, so the drift is isolated to the `FromPetscVec`/`ToPetscVec` boundary calls in this body.)

6. **Live markdown links to a non-existent `../L4/eigsolve.md` (build-breaker).** CYCLE.md links `[eigsolve](../L4/eigsolve.md)` as a live link in six places (lines 44, 59, 103, 197, 228, 239) while the prose at each site correctly states the L4 entry is unauthored / future. `book/src/L4/eigsolve.md` does NOT exist (verified by directory listing). A live link to a missing file is a hard `linkcheck2` failure per the friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link` convention; the forward-reference must be plain text, OR the integrator may materialize an `L4/eigsolve.md` stub per the "Integration may materialize implied components as stubs" directive (this L4 target is clearly-implied: ≥2 converging references here plus the L1/L2 `solve-monad`-surface anchors). The L4-target is genuinely speculative (no firm L4 exists), so plain-text-defer is the conservative fallback; stub-creation is the directive-preferred path if the integrator judges the convergence sufficient. Severity: medium (would break `cargo make book` linkcheck as-is). Location: CYCLE.md lines 44, 59, 103, 197, 228, 239.

7. **SUMMARY.md insert is a label change, not an addition (context note for the integrator).** The current SUMMARY.md line is `- [eigsolve (stub)](./L3/eigsolve.md)` (line 31); the report's `edit:book/src/SUMMARY.md` block supplies `- [eigsolve](./L3/eigsolve.md)` (drops the `(stub)` marker now that the entry is `partial-obstruction`). The proposed-changes block shows only the desired new line without the old→new pairing, so a naive append would duplicate the entry rather than replace the stub-labeled one. Not a content defect — the intent is clear and correct — but the integrator must perform a surgical *replace* of the existing line, not an insert. Severity: low (integration-mechanics note). Location: CYCLE.md §"Proposed changes" lines 272-274 vs `book/src/SUMMARY.md:31`.

---

## Repair

### Fixes attempted

**1. Off-by-one: `opK->Mult(x1, z1)` no-transform branch (`citation-validity`).**
- **Decision**: repaired.
- **Action**: CYCLE.md §Signature line 93 — corrected the single-statement spot pointer `arpack.cpp:572` → `:573`. Verified via codemap `read_range arpack.cpp:569-590`: `opK->Mult(x1, z1)` is at line 573 (matches the firm L2 entry's `:573-575` citation). The two other locations the critic listed (§"Variant axes" line 205, §Evidence line 245) use the *range* form `:572-575`, which the critic confirmed correct — left untouched.

**2. Off-by-one: `opM->Mult(x1, z1)` shift-invert branch (`citation-validity`).**
- **Decision**: repaired.
- **Action**: CYCLE.md §Signature line 93, §Dependencies line 181 (the `opInv->Mult` call-site list `:573, 580`), and §Dependencies line 182 — corrected the spot pointer `arpack.cpp:580` → `:579` in all three. Verified via codemap `read_range arpack.cpp:569-590`: `opM->Mult(x1, z1)` is at line 579. §"Variant axes" line 211 (critic-listed) uses only range forms — no `:580` spot pointer present, no change needed. (Note: the `:573` in line 181's `opInv->Mult` list was NOT flagged by the critic and is left as-is — outside the flagged findings; altering it would be a content judgment beyond repair scope.)

**3. Off-by-one: ARPACK max-iteration `iparam[2] = arpack_it` (`citation-validity`).**
- **Decision**: repaired.
- **Action**: CYCLE.md §Semantics line 119 and §Evidence line 246 — corrected `arpack.cpp:269` → `:270`. Verified via codemap `read_range arpack.cpp:268-274`: `iparam[2] = (a_int)arpack_it;` is at line 270.

**4. Off-by-one: SLEPc `FromPetscVec(x, ctx->x1)` (`citation-validity`).**
- **Decision**: repaired.
- **Action**: CYCLE.md §Signature line 96 and §Evidence line 248 — corrected `slepc.cpp:1856` → `:1857`. Verified via codemap `read_range slepc.cpp:1855-1875`: line 1856 is blank, `FromPetscVec(x, ctx->x1)` is at line 1857. The §"Algebraic laws" line 157 sub-range form `:1856-1865` (a composition span the critic did not flag) is left untouched.

**5. Off-by-one: SLEPc `ToPetscVec(ctx->y1, y)` (`citation-validity`).**
- **Decision**: repaired.
- **Action**: CYCLE.md §Signature line 97 and §Evidence line 248 — corrected `slepc.cpp:1872` → `:1873`. Verified via codemap `read_range slepc.cpp:1855-1875`: line 1872 is blank, `ToPetscVec(ctx->y1, y)` is at line 1873.

**6. Live markdown links to non-existent `../L4/eigsolve.md` (build-breaker; `cross-reference-integrity`).**
- **Decision**: repaired.
- **Action**: Defanged all six live `[eigsolve](../L4/eigsolve.md)` links (CYCLE.md lines 44, 59, 103, 197, 228, 239) to PLAIN TEXT — replaced the markdown link with a plain code-span ``eigsolve`` plus a parenthetical "the `L4/eigsolve.md` chapter is not yet authored", per the friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link` convention. Confirmed zero remaining `](../L4/eigsolve.md)` live links via grep. The surrounding prose already framed the L4 entry as future/unauthored, so the defang is purely the link-markup removal — no content change. NOT creating an `L4/eigsolve.md` stub: per the critic's note and the "Integration may materialize implied components as stubs" directive, stub-creation is an integrator discretionary call (the L4 target is genuinely speculative — no firm L4 exists), and explicitly outside repair authority; plain-text-defer is the correct conservative repair.

**7. SUMMARY.md proposed-changes block is a label-replace, not an append (`cross-reference-integrity` / integration-mechanics).**
- **Decision**: repaired.
- **Action**: CYCLE.md §"Proposed changes" `edit:book/src/SUMMARY.md` block (lines 272-274) — rewrote the bare new-line form into an explicit OLD→NEW surgical replacement instruction (`OLD: - [eigsolve (stub)](./L3/eigsolve.md)` / `NEW: - [eigsolve](./L3/eigsolve.md)`), pinned to `book/src/SUMMARY.md:31`, with a "Replace (NOT append)" header. Verified the current SUMMARY.md:31 line is `- [eigsolve (stub)](./L3/eigsolve.md)`. This prevents the integrator from duplicating the entry instead of dropping the `(stub)` label.

### Unrepairable findings

None. All seven critic findings were mechanical/surgical (off-by-one anchor corrections, live-link defanging, proposed-changes-block mechanics) and were repaired in place. No substantive authoring was required; the report's content, surface, rotation evidence, variant-axis coverage, edge labels, and status classification all passed the critic untouched.

## Suggested resolution

`overall_status: ready`. The report is ready for `integrator-per-report`. Integration notes:

- The L3 `eigsolve` entry replaces the cycle-023 stub in place (`edit:book/src/L3/eigsolve.md`) and lands `partial-obstruction`.
- SUMMARY.md edit is a **surgical line replacement** at `book/src/SUMMARY.md:31` (drop `(stub)` label) — now encoded explicitly as OLD→NEW in the proposed-changes block. Do not append.
- The L3 `index.md` dep-map row insert (lines 266-267) carries the new `eigsolve` row; the existing plain-text `No firm L4 eigsolve` reference in that row has no live link (clean).
- All six L4-eigsolve forward-references are now plain text — no `L4/eigsolve.md` file is required for the build to pass. The integrator MAY (discretionary, per "Integration may materialize implied components as stubs") create an `L4/eigsolve.md` stub if it judges the convergence sufficient (the L1/L2 `solve-monad` anchors + this entry's repeated references), but this is optional and not required for `ready`.
- Open question `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` (cycle-021) is **confirmed** by this entry and can be closed; the report's Open-questions §1–§5 (pending L2>L1 theme, optional L3>L2 audit anchor, unauthored L4 surface, chain-closure note, L3 partial-obstruction count) are promotable to the OQ ledger by the integrator.
