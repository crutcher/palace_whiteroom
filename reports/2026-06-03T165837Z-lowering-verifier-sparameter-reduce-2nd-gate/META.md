---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T18:42:00Z
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
repaired_at: 2026-06-03T19:05:00Z
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

# META: verification of "Audit sparameter_reduce — 2nd gate (test-coverage) discharge"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` over the full report (31 citations: 30 ok, 1 out-of-bounds) plus `--anchor` probes on the load-bearing pinpoints. Three drifts surfaced, all small but all in load-bearing positions:
- **`postoperatorcsv.cpp:214` is off by one.** The `dim[k].S = data.S; // NONE` line — the *entire source-side basis for the dimensionless-S invariant claim*, cited as `:214` at CYCLE.md lines 38, 124-127, 246, and in the `verified_against:` citation (line 308) and its note (line 311) — actually sits at **`:213`** (on-disk Read confirms: `:213` is `dim[k].S = data.S;  // NONE`; `:214` is blank). The `--anchor 'data.S'` probe reports `[DRIFT] -1 → :213`. This is the single most load-bearing anchor in the audit (it is the source-witness for the "Scattering always non-dim" test corroboration), so its drift matters.
- **test-postoperator.cpp non-dim assertions off by one in the BODY prose.** CYCLE.md line 104 cites `CHECK_THAT(std::abs(c.S), WithinRel(std::abs(ndc.S)))` at `:194` and `arg` at `:195`. On-disk these are at **`:195`** (`abs`) and **`:196`** (`arg`) — line `:194` is actually `arg(c.P)`. The `--anchor 'std::abs(c.S)':194` probe reports `[DRIFT] +1 → :195`. NOTE the partial self-consistency: the `verified_against:` YAML note (line 307) gets these RIGHT (`|S| :195 non-dim ... arg(S) :196`), and the dim-side anchors `:228` / `:229-230` are correct everywhere. So the drift is confined to the body-prose non-dim citations; the proposed-changes block's own non-dim citation (CYCLE.md line 243, "`:194-195` non-dim") inherits the same off-by-one and should read `:195-196`.
- **`port_projection.md:1-355` is out of bounds.** The file has **354** lines; the `verified_against:` citation (CYCLE.md line 312) ranges `:1-355`. `citecheck --scan` flags `[OOB]`. The three pinpoint sub-anchors in that same note (`:61-64`, `:219-221`, `:343-345`) are all correct and in-range (verified on-disk: `:61-64` states "That reduction's gate-b ... is satisfied by this entry"); only the whole-file `:1-355` upper bound overshoots by one.

Everything else in the citation surface verified clean: `MeasureSParameter` def at `:1246` (`--anchor [ok]`), `vi.S.real` self-term `:1275` (`[ok]`), `check_port_data` `:189` (`[ok]`), `lumped_port_vi` `:266` / `wave_port_vi` `:271` (`[ok]`), dim-side test assertions `:228-230` (on-disk confirmed). The `verified_against:` YAML block round-trips under `yaml.safe_load` (no leading-quote scalar defect; all `note:` values begin with prose). The report's *self-correction* of the dispatch citation error holds: `test-postoperatorcsv.cpp:22-138` asserts only on `port-V.csv` (grep confirms zero `port-S` hits; lines 80/126/210/253/293/385 are all `port-V.csv`), and the only `port-S.csv` content in the test tree is the synthetic literal at `test-basesolver.cpp:40` — so the `does-not-support` verdict for the S-reduction-output claim is correctly drawn, not a critic disagreement.

**surface-or-evidence — pass.** This is a lowering-verifier audit producing a `verified_against:` evidence block plus a status refinement on an existing verb — squarely retroactive-evidence-backfill shape, which is allowed. It modifies surface (the `## Status` section of `sparameter_reduce.md`) and carries the rotation/evidence audit, so it is not a pure rotation_claim. Record-definition sub-check: the verb's signature names `PortMode`, `Matrix[p,p]`, and the `(Int, Tensor[N])` family element — these are L4 calculus shape types already established in the L4 layer / index dep-map, not newly-introduced result records demanding an in-chapter definition home; the chapter references them by use against already-firm constituent chapters (`port_projection`, `gram_reduce`, `frequency_sweep`). No undefined signature-named record is introduced by this audit.

**rotation-quality — pass.** Not the primary shape of this report (it is an audit, not a rotation proposal). The underlying lowering it audits is the L4 → per-port-projection-plus-scalar-maps fold; the report does not assert a new rotation, it confirms the existing one's evidence. No renaming-only or 1:1 mapping is asserted as a rotation.

**variant-axis-coverage — pass.** The lumped-vs-wave port-kind axis is explicitly and correctly handled: the audit verifies both port loops (`postoperator.cpp:1267-1286` lumped, `:1287-1307` wave), both `GetSParameter` kernels, and confirms the test invariant runs over BOTH `lumped_port_vi` (`:266`) and `wave_port_vi` (`:271`). The scaling-presence axis (generalized-S guarded `|R|>0`; de-embed identity at `d_offset=0`) is enumerated under §Applicability conditions with the identity-element cases noted as source-witnessed-only. No hidden branch.

**cross-reference-integrity — pass.** All edit-target anchors resolve: `sparameter_reduce.md` has `## Status` at `:238` (the replace anchor), `sparameters.L1.md:8` carries the exact `composes:` `bilinear-form` line the report proposes to repoint, and `L4/index.md:104` is the dep-map row the report flags for carry-forward. The proposed-changes fence parity is clean: `grep -n '```'` yields 6 fence markers — outer `edit:` block (`:225`→`:321`) properly encloses a nested ` ```yaml ` block (`:290`→`:320`), then a second `edit:` block (`:346`→`:351`); even parity, balanced nesting. Build-readiness guard (firm-body-inside-fence): not triggered — the claimed status is `rough-in (test-coverage-bounded)`, NOT `firm`, and the full refreshed Status body + `verified_against:` block sit INSIDE the fence regardless. Down-link `port_projection.md` resolves and its on-disk `firmness: firm` matches the report's maturity claim.

**edge-label-fidelity — pass.** No mislabeled cross-layer edge. The report consistently discusses the L4 `sparameter_reduce` verb, its L1 constituent home (`port_projection`), and the L0 source/test evidence; the gate-b discharge is correctly attributed to the L1 `port_projection` entry. The §"Direction-of-definition" self-check (CYCLE.md OQ 4) confirms forward narration.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit; content is an evidence audit with a status-refinement UNBLOCK (not enactment). The verdict (`rough-in` → `rough-in (test-coverage-bounded)`, NOT `firm`) is consistent with the partly-witnessed evidence: output invariant witnessed, assembly fold not test-exercised — exactly the `test-coverage-bounded` qualifier per the codified `eigsolve` / `matrix-weighted-norm` precedent. No firm-claim with rough-in placeholders.

**skill-uptake-survey — pass.** The report explicitly invokes `tools/citecheck/citecheck.py --anchor`/`--scan` and `palace-codemap read_range` for the citation re-confirmation (CYCLE.md lines 51-54, 70, 360-382), and references the `proposed-changes-fence-encloses-full-body-guard` fence-parity discipline (line 222). The batch-24 decision-(e) route (cite existing postprocess tests as L0-equivalent) is the methodological warrant cited. Telemetry positive.

### Issues found

1. **`postoperatorcsv.cpp:214` → should be `:213`** (severity: moderate — load-bearing anchor). CYCLE.md lines 38, 124-127, 246, 308, 311. The `dim[k].S = data.S; // NONE` line is at `:213`; `:214` is blank. This is the source-witness for the dimensionless-S test corroboration, so the off-by-one is on the audit's central new anchor. Appears in both the body prose AND the `verified_against:` citation+note. Mechanical fix.

2. **test-postoperator.cpp non-dim assertions off by one in body prose** (severity: low). CYCLE.md line 104: `std::abs(c.S)` cited `:194` should be `:195`; `arg` cited `:195` should be `:196`. Also CYCLE.md line 243 (inside the proposed `## Status` replacement) cites "`:194-195` non-dim" — should be `:195-196`. The `verified_against:` YAML note (line 307) already has these correct (`:195` / `:196`), as does the dim-side everywhere, so the fix is to align the body/Status prose to the (correct) YAML.

3. **`port_projection.md:1-355` out of bounds** (severity: low). CYCLE.md line 312 (`verified_against:` citation). File has 354 lines; range overshoots to `:1-355`. Should be `:1-354`. The three sub-anchors in the same note are correct and in-range.

All three are mechanical line-number corrections; none undermines a verdict (the gate-b discharge against firm `port_projection.md`, the `partially-supports` test verdict, the `does-not-support` CSV self-correction, and the `rough-in (test-coverage-bounded)` promotion are all independently confirmed against source/disk). The corrections should propagate into the proposed-changes `edit:` block so the artifact lands with the right line numbers.

---

## Repair

### Fixes attempted

- **Finding 1**: `postoperatorcsv.cpp:214` → `:213` — the `dim[k].S = data.S; // NONE` source-witness for the dimensionless-S invariant (line 214 is blank). Load-bearing anchor; appears in body prose AND the `verified_against:` YAML block + note.
  - **Decision**: repaired
  - **Action**: Verified on disk (`postoperatorcsv.cpp:213` = `dim[k].S = data.S;  // NONE`; `:214` is blank). Corrected all 5 occurrences in `CYCLE.md`: body-prose §Summary, §Per-citation-audit Found, the proposed `## Status` block (inside the `edit:` fence so the artifact lands correct), the `verified_against:` YAML `citation:` line, and §Supporting-evidence. The YAML note text references the loop range `(:200-226)` which is unchanged and correct.

- **Finding 2**: `test-postoperator.cpp` non-dim assertion prose off-by-one — `std::abs(c.S)` `:194`→`:195`, `arg` `:195`→`:196`. The `verified_against:` YAML note already had these correct; align prose to YAML.
  - **Decision**: repaired
  - **Action**: Verified on disk (`:195` = `std::abs(c.S)`, `:196` = `std::arg(c.S)`; `:194` = `arg(c.P)`). Corrected the §Per-citation-audit body prose (`:194`/`:195` → `:195`/`:196`) and the proposed `## Status` block range `:194-195` → `:195-196` (inside the `edit:` fence). The YAML note (`|S| :195 / arg(S) :196`) was already correct and left as-is; prose now aligns.

- **Finding 3**: `port_projection.md:1-355` out of bounds → `:1-354` (file has 354 lines). Sub-anchors in the note (`:61-64`, `:219-221`, `:343-345`) are correct.
  - **Decision**: repaired
  - **Action**: Verified on disk (`wc -l` = 354). Corrected the `verified_against:` YAML `citation:` whole-file range to `:1-354`. The three in-range pinpoint sub-anchors in the same note are untouched.

### Unrepairable findings

None. All three citation-validity drifts were mechanical line-number corrections within repair authority (off-by-one offsets and a one-line out-of-bounds upper bound), and all corrections were propagated into the proposed-changes `edit:` blocks so the integrator lands correct anchors. The 7 other checks passed.

## Suggested resolution

`ready`. Notes for the integrator: the two carry-forward items the report flags remain open by design and are NOT repairer-resolvable (they are deliberate one-theme-per-invocation deferrals, not defects):
- OQ 1 — `book/src/L4/index.md:104` dep-map status refresh (`rough-in` → `rough-in (test-coverage-bounded)`, drop the stale gate-b clause) — an integrator carry-forward.
- OQ 2 — `sparameters.L1.md:39,60,64` prose down-link repoint from `bilinear-form` to the now-firm `port_projection` — flagged for a follow-up `layer-intro-author` / `lifter` pass; the `composes:` frontmatter repoint is already in the report's second `edit:` block.

The proposed-changes fence parity (6 markers, balanced nested `yaml` block) was confirmed clean by the critic and is unaffected by these line-number edits.
