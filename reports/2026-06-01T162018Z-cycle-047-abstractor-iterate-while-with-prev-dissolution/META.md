---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T000000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T000000Z
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

# META: verification of "L4>L3 theme sketch — iterate-while-with-prev-dissolution"

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: 37 of 38 citations in-bounds; the sole flag is `cg.md:441-446 [OOB]` (file is 165 lines). This is **not a drift defect** — both `441-446` mentions are explicitly framed as *historical-provenance prose* ("Re-anchored from the firm L4 cap's historical `cg.md:441-446` citation, which predates the cycle-009 corpus reduction…", CYCLE.md:206; mirrored CYCLE.md:273), not as live claims. The CRITICAL re-anchor verification (the inherited-stale `cg.md` ranges → current ranges) passes: I read the current on-disk `cg.md` (165 lines, reduced) and confirmed each re-anchored range says what the report claims:
- `cg.md:100-108` — the `iterate_while_with_prev s1 s0.beta …` call site. **Correct** (line 100 is the call; 102-103 the prev-threaded steady closure; 105 the trajectory readout).
- `cg.md:52-108` — the `cg_first_step` (52-67) / `cg_steady_step` (69-84) bootstrap/steady pair + `cg_solve` (86-106). **Correct.**
- `cg.md:102-103` — `(\(s, beta_prev) -> … cg_steady_step opA eps beta_prev s …)`: the `beta_prev`-as-`prev`-parameter pattern. **Correct** (the predicate-on-carry-only it is paired with is at line 101, one line above the cited range — a 1-line under-inclusion, mild but the cited lines do exhibit the `prev`-parameter half of the claim).
- `cg.md:124` — cited (Condition 4, CYCLE.md:166) as "CG v0.5's outer initial-convergence test". **Anchor imprecision:** line 124 is *prose describing* the initial-convergence test inside the "Equivalence to v0.4" enumeration ("1. **Initial convergence.** Both forms test `sqrt|beta_0| < eps`…"); the actual outer test *code* is at `cg.md:92` (`if sqrt (abs s0.beta) < eps then`). The citation points at a faithful description, not the construct itself — a soft mis-pin, downgraded from fail because the descriptive line is in-range and on-topic.

The new-chapter L4-LHS / strawman citations were spot-checked against disk: `iterate-while-with-prev.md:182-198` (firm §"Lowers to" L3 form) ✓, `:200`/`:223` (re-anchor targets) ✓, Law 1 `:129-135` ✓, Law 2 `:137-147` ✓; `l4_calculus.md:150-184` (§3.7 header at 150) ✓, `:186-213` (§3.8 header at 186) ✓; `krylov-step-typed-wrapper-dissolution.md:74-89` (Form-B-in-L3) ✓, `:150-154` (rough-in sig) ✓, `:202-213` (cycle-002 audit) ✓. The `iterate-while.md:123-133` Law-1 citation: the report's own citecheck note (CYCLE.md:270) correctly characterizes the `[DRIFT]` flag as a literal-token mismatch on the word "Law 1" (the range carries "1. **Demand-driven trajectory pruning**", which is Law 1's content) — confirmed.

**surface-or-evidence — pass.** This is a `new:` standalone L4>L3 theme (not a refinement of existing operator/theme text), explicitly framed as an **extraction + re-homing** of an already-firm form (the firm cap §"Lowers to" `:182-198` + the firm krylov-step sub-component `:74-89`). The new chapter IS the surface; the extraction provenance is fully cited. The two re-anchor `edit:` blocks modify existing surface (the cap's §"Lowers to" `:200` + §"L4 vs L3 distinction" `:223`) and are backed by the new chapter they point to. No bare rotation_claim without surface. Pass.

**rotation-quality — pass.** The L4→L3 forward rotation is genuine and strictly-dissolving, not a rename: the `Solve` monad → positional `sim` thread; the row-polymorphic `{state, prev, ...e}` record → positional tuple; the `prev` *closure parameter* → positional tuple slot; the `bootstrap_step` → non-recursive let-bound prefix; the demand-prunable `trajectory` → explicit accumulator (unpruned) or eliminated (pruned). The L4 form is strictly more abstract (typed records, monadic effect, closure-threaded prev, structural bootstrap-then-loop). The unpruned-ground / pruned-image framing is internally consistent and correctly states the pruned form is the §3.8 collapse-rule *image* of Law 2 (not a contradiction) — matching the parent theme's treatment at `krylov-step-typed-wrapper-dissolution.md:160-200`. The Law-1 degeneracy tie (`β = ()` ⇒ companion `iterate_while_L3`) is sound against cap Law 1 (`:129-135`). Pass.

**variant-axis-coverage — pass.** The combinator's two L4 variant axes (pure vs Solve-threaded; extras-carrying vs no-extras, per `iterate-while-with-prev.md:204-212`) are addressed: the trajectory-pruning axis is rendered as the explicit unpruned/pruned fork (§"L3 form (RHS)"), and the no-extras case is folded into the pruned form. The third potential axis (bootstrap-free) is correctly scoped out — this combinator *is* the carry-bootstrapped form, and the no-prev case is delegated to the companion theme via the Law-1 degeneracy. No hidden branch. Pass.

**cross-reference-integrity — warning.** Build-readiness: fence parity is even (12 backtick-fence lines = 6 proposed-change blocks; the new chapter's L3 forms use **4-space indented** code, not nested ` ``` ` fences, so there is NO fence-truncation defect). The full firm body — §Status (CYCLE.md:215), §L4 form, §L3 form, §Justification, §Verified-against, §L4 vs L3 distinction — is enclosed INSIDE the `new:` fence (lines 24–225). No firm-body-outside-fence defect. All concept/L4/L4-L3 cross-targets resolve on disk (`solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`, `sequential-obstruction`, `krylov-step`, `iterate-while`, `iterate-while-with-prev`, `gmres-`/`fgmres-inner-loop-…`, `arnoldi_step`) EXCEPT the same-cycle sibling **`L4-L3/iterate-while-dissolution.md` (D1), which is NOT on disk** — and the report links it as a **live link** in three places inside the new chapter body (§Context :29, §"Companion theme" :43, §Degeneracy :142, §"What this lowering does NOT cover" :153) AND inside BOTH re-anchor `edit:` blocks to the cap (`../L4-L3/iterate-while-dissolution.md` at CYCLE.md:230 and :236). Under `linkcheck2` a live link to a not-yet-on-disk file is a hard build error unless both reports' `new:` blocks land in the same `integrator-finalize` build. The report flags this dependency (CYCLE.md:278) and relies on the same-cycle carve-out of `rough-in-forward-reference-must-be-plain-text-not-live-link` — a legitimate cover, but it is an integrator co-wiring obligation, not a self-contained-buildable report; hence `warning`. The re-anchor `edit:` old-strings (cap `:200` paragraph beginning "As with [`iterate-while`]… not yet authored as a standalone…"; cap `:223` paragraph "Same effect-threading-and-demand-pruning-placement difference…") match disk verbatim. The L4/index.md dep-map re-anchor's old-string (`| [`iterate-while-with-prev`](./iterate-while-with-prev.md) |`) is unique and matches; the replacement row preserves the Signature/Concepts/Status cells and rewrites only the L3 cell (faithful). The L4-L3 index row and SUMMARY line both append after the `fgmres-inner-loop-iterate-while-migration` anchor (index:17, SUMMARY:17) — D1's `iterate-while-dissolution` rows ALSO append after the same anchor; the two are **distinct slugs** (`iterate-while-with-prev-dissolution` ≠ `iterate-while-dissolution`), so they are two distinct appended rows/lines, NOT a clobber — but this is a second integrator co-ordering obligation (apply both as appends, do not let one overwrite the other's anchor target). The report calls this out (CYCLE.md:245, :252).

**edge-label-fidelity — pass.** Every re-anchored edge points L4>L3 at the correct theme. The cap §"Lowers to" re-anchor (:200) and §"L4 vs L3 distinction" re-anchor (:223) both narrate the L4→L3 dissolution and link the new `iterate-while-with-prev-dissolution` chapter; the dep-map L3 cell (index :55 row) likewise. No L_{n+1}→L_n label mismatch with prose; the chapter's forward L4→L3 narration is consistent throughout. Pass.

**plan-kind-consistency — pass.** Declared `firm` (CYCLE.md:217), shape matches: exhaustively-cited extraction with stated justification (`structural` + secondary `reduction-chain`), no rough-in placeholders in the firm body, no speculative operator. The firm status is justified by the extraction-of-already-firm-form argument and is internally consistent with the parent firm artifacts. Pass.

**skill-uptake-survey — pass.** The report's shape (citation-heavy extraction + fence-bearing proposed-changes + on-disk re-anchor) implies `verify-citation-range` / `tools/citecheck` and the fence-parity guard; the report references citecheck self-verification (CYCLE.md:283) and the §Status/extraction provenance is well-formed. Telemetry only; non-blocking. Pass.

### Issues found

1. **`cg.md:124` anchor mis-pin (citation-validity, minor).** CYCLE.md:166 (Condition 4) cites `book/src/spec/slices/cg.md:124` for "CG v0.5's outer initial-convergence test", but line 124 is *prose describing* that test inside the "Equivalence to v0.4" enumeration; the actual outer-test code is at `cg.md:92` (`if sqrt (abs s0.beta) < eps then`). The construct cited is one of description, not definition. Severity: low (in-range, on-topic). Candidate repair: re-pin to `cg.md:92` (or `:89-106` for the whole `cg_solve` body) where the outer test is realized.

2. **`cg.md:102-103` 1-line under-inclusion (citation-validity, minor).** CYCLE.md:162 pairs "predicate-on-carry-only + `beta_prev`-as-`prev`-parameter" with `cg.md:102-103`, but the predicate-on-carry-only construct (`(\(s, _) -> s.it < config.max_it && not s.converged)`) is at `cg.md:101`, one line above the cited range; lines 102-103 carry only the `prev`-parameter half. Severity: low. Candidate repair: widen to `cg.md:101-103`.

3. **Stale historical `cg.md:441-446` carried as prose (citation-validity, informational).** Flagged OOB by citecheck (file is 165 lines). The report intentionally retains it twice (CYCLE.md:206, :273) as clearly-marked historical-provenance; this is acceptable under the inherited-citation convention but will perpetually trip a mechanical `--scan`. Severity: informational. No repair required; optionally annotate the line so future scans recognize it as a deliberate historical mention.

4. **Live-link to not-yet-on-disk same-cycle sibling `iterate-while-dissolution.md` (cross-reference-integrity, build-readiness).** The new chapter body (CYCLE.md:29, :43, :142, :153) AND both cap re-anchor `edit:` blocks (CYCLE.md:230, :236) link `../L4-L3/iterate-while-dissolution.md` as a live link; D1's file is not on disk. This is a hard `linkcheck2` error unless the integrator wires BOTH reports' `new:` blocks in a single finalize build. The report flags it (CYCLE.md:278) under the same-cycle carve-out. Severity: medium (integrator co-wiring obligation; not self-contained-buildable). Candidate handling: integrator must apply this report + D1 in the same finalize, OR (fallback) the links demote to plain-text per `rough-in-forward-reference-must-be-plain-text-not-live-link`.

5. **Shared `fgmres` append-anchor for L4-L3 index row + SUMMARY line (cross-reference-integrity, integrator-ordering).** Both this report's index row (CYCLE.md:247-250) and SUMMARY line (CYCLE.md:254-257) append after the `fgmres-inner-loop-iterate-while-migration` anchor, which D1 also targets. Distinct slugs (no clobber), but the integrator must apply both as additive appends, not anchor-replacements. The report calls this out (CYCLE.md:245, :252). Severity: low-medium (procedural). No content repair needed.

6. **"7 balanced fences" mis-count in report self-description (cosmetic).** The report (per the dispatch framing) claims 7 balanced fences; the CYCLE.md actually contains 12 fence-delimiter lines = **6** proposed-change blocks (1 `new:` + 5 `edit:`). Parity is even and there is no truncation defect, so this is cosmetic, but the self-reported count is wrong. Severity: cosmetic. Candidate repair: correct the count if it appears in any landed text (it does not appear in the proposed-changes payload, only in dispatch framing).

7. **`:202-213` audit cited for L4>L3 body-identity transport (rotation-quality, soft).** CYCLE.md:138 cites `krylov-step-typed-wrapper-dissolution.md:202-213` (the "Audit of cycle-002 identity-in-form claim") as establishing "the body-identity that licenses the [Law-2] transport" through the L4>L3 dissolution. That audit section establishes the **L2→L3** body identity-in-form; the L4>L3 value-thread-isomorphism argument in the parent theme is carried more directly at `:122-126`/`:198`. The cited range is supporting (it does establish body-identity), but is not the tightest anchor for the *L4>L3* transport specifically. Severity: low / soft. Candidate repair: add `:122-126` (or `:198`) as the primary transport anchor, keeping `:202-213` as the body-identity corroborant.

---

## Repair

### Fixes attempted

- **Finding 1a — `cg.md:124` anchor mis-pin (citation-validity).**
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Applicability conditions" Condition 4 (was CYCLE.md:166). Re-pinned the outer initial-convergence-test citation from `book/src/spec/slices/cg.md:124` (prose describing the test) to `book/src/spec/slices/cg.md:92` (the test *code* `if sqrt (abs s0.beta) < eps then`). Verified against current on-disk 165-line `cg.md`: line 92 holds the outer test; line 124 is the "Equivalence to v0.4" enumeration prose. Surgical anchor re-point — no content authored.

- **Finding 1b — `cg.md:102-103` 1-line under-inclusion (citation-validity).**
  - **Decision**: repaired.
  - **Action**: two sites widened from `cg.md:102-103` to `cg.md:101-103`, splitting the two halves of the paired claim. (i) CYCLE.md §"Applicability conditions" Condition 2 (was CYCLE.md:162) — now names `cg.md:101` (predicate-on-carry-only `(\(s, _) -> s.it < config.max_it && not s.converged)`) and `cg.md:102-103` (the `beta_prev`-as-`prev`-parameter half). (ii) CYCLE.md §"Verified-against" / slice-evidence line (was CYCLE.md:206) — same widening. Verified against disk: line 101 is the carry-only predicate, lines 102-103 the `prev`-parameter steady closure. Surgical range widening.

- **Finding 3 — stale historical `cg.md:441-446` carried as prose (citation-validity, informational).**
  - **Decision**: not-needed.
  - **Rationale**: critic confirmed both `441-446` mentions (CYCLE.md:206, :273) are explicitly framed as historical-provenance prose, not live claims. No repair required; the mechanical `--scan` OOB flag is a deliberate-historical-mention artifact, not a drift defect. Left as-is per critic guidance.

- **Finding 4 — live-link to not-yet-on-disk same-cycle sibling `iterate-while-dissolution.md` (cross-reference-integrity, build-readiness).**
  - **Decision**: repaired (recorded as integrator-ordering note; links KEPT, not defanged).
  - **Action**: confirmed the D1 sibling links are correctly-spelled relative paths that resolve once D1 lands: the live markdown links in both cap re-anchor `edit:` blocks (CYCLE.md:230, :236) use `../L4-L3/iterate-while-dissolution.md`, which resolves correctly from `book/src/L4/iterate-while-with-prev.md`; the new-chapter body references to D1 (§Context, §Degeneracy, §"What this lowering does NOT cover") are prose path text. **Links intentionally KEPT as live links** — defanging would needlessly lose correct cross-references. See INTEGRATOR-ORDERING NOTE below.
  - **Rationale for keeping**: `cargo make book` + `linkcheck2` runs ONCE at `integrator-finalize`, AFTER all per-report applies in the cycle. Both D1 (`iterate-while-dissolution`) and D2 (this report) `new:` blocks land before that single build, so D1's file is on disk by build time and every live link resolves. This is the standard pipeline behavior, so keeping the links is correct.

- **Finding 5 — shared `fgmres` append-anchor for L4-L3 index row + SUMMARY line (cross-reference-integrity, integrator-ordering).**
  - **Decision**: repaired (recorded as integrator-additive-append note).
  - **Action**: confirmed this report's L4-L3 index row (slug `iterate-while-with-prev-dissolution`, CYCLE.md:249) and SUMMARY line (CYCLE.md:256) are **distinct** from D1's (`iterate-while-dissolution`); both append additively after the same `fgmres-inner-loop-iterate-while-migration` anchor. No clobber — two distinct appended rows/lines. See INTEGRATOR-ADDITIVE-APPEND NOTE below.

- **Finding 6 — "7 balanced fences" mis-count in report self-description (cosmetic).**
  - **Decision**: not-needed.
  - **Rationale**: the count appears only in dispatch framing, not in any landed proposed-changes payload. Critic confirms fence parity is even (6 blocks, full body enclosed, no truncation defect). Cosmetic; no edit to landed text.

- **Finding 7 — `:202-213` audit cited for L4>L3 body-identity transport (rotation-quality, soft).**
  - **Decision**: not-needed (unrepairable-but-non-blocking).
  - **Rationale**: adding `:122-126`/`:198` as the tightest L4>L3 transport anchor is a content/anchor-selection judgement about which range most directly establishes the value-thread-isomorphism — that exceeds mechanical-repair authority (it is not a clearly-off-by-N slip; the cited `:202-213` does establish body-identity and is a valid supporting anchor). Critic rated it low/soft and did not invert the rotation-quality `pass`. Left for an optional future producer/lifter pass; not verdict-blocking.

### Unrepairable findings

None blocking. Finding 7 is a soft anchor-tightening suggestion (rotation-quality stayed `pass`); not routed to a follow-up agent.

### INTEGRATOR-ORDERING NOTE (finding 4)

Both D1 (`iterate-while-dissolution`) and D2 (this report) `new:` blocks must be applied before the finalize build — the default per-report-then-finalize pipeline already does this. The `iterate-while-dissolution.md` live links (in both cap re-anchor `edit:` blocks and the chapter body) resolve at the single `integrator-finalize` `linkcheck2`, NOT per-report. No defang needed. Link paths confirmed correctly spelled (`../L4-L3/iterate-while-dissolution.md` from the cap; `book/src/L4-L3/iterate-while-dissolution.md` prose in the new chapter).

### INTEGRATOR-ADDITIVE-APPEND NOTE (finding 5)

This report's L4-L3 index row and SUMMARY line (slug `iterate-while-with-prev-dissolution`) are distinct from D1's (`iterate-while-dissolution`); both append after the shared `fgmres-inner-loop-iterate-while-migration` anchor. Apply both as additive appends — do NOT let one report's edit overwrite the other's anchor target. Two distinct rows in `L4-L3/index.md`; two distinct lines under the L4>L3 Part in `SUMMARY.md`.

## Suggested resolution

`ready`. The two citation-validity warnings were mechanical anchor fixes (1a re-pin `cg.md:124`→`:92`; 1b widen `cg.md:102-103`→`:101-103` at two sites), all verified against the current on-disk 165-line `cg.md`. The cross-reference-integrity warning is an integration co-wiring obligation, not a content defect — the D1 sibling live links are correct and resolve at the single finalize build; recorded as integrator-ordering + additive-append notes rather than defanged. Content is sound per critic (surface, rotation, variant-axis, edge-label, plan-kind all pass). Integrator notes: apply this report together with D1 before the finalize build; treat both reports' index/SUMMARY rows as additive appends after the shared `fgmres` anchor.
