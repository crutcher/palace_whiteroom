---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T05:26:08Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T06:05:00Z
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

# META: verification of cycle-075 D2 — sparameters output-product feature column (cohort OWNER)

## Critique

This report is a FEATURE-SURFACE composition-root (output-product leaf column, `status: seed`) PLUS a cohort-owner consolidated `feature/index.md` matrix + `# Feature surfaces` SUMMARY.md block for BOTH new output-product columns. The 8 checks were run with the feature-surface adaptations (rotation-quality + variant-axis-coverage no-op; surface-or-evidence and cross-reference-integrity adapted/load-bearing per the composition-root kind).

### Checks run

**citation-validity — fail.** Mechanical scan is clean at the range level: `citecheck --scan` returns 6 ok / 0 failing on CYCLE.md and 13/13, 13/13, 12/12 on the three staged sibling chapters; every enclosing range (`postoperator.cpp:1246-1309`, `lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`, the `:1141`/`:1239` projection caches) is correct and the three load-bearing symbol anchors (`MeasureSParameter`, both `GetSParameter`) resolve. HOWEVER, the **interior pinpoint lines are systematically drifted low by 1–3 lines** against ground truth (read directly from `reference/palace/palace/models/postoperator.cpp` and the two port-operator files this dispatch). This is a real `fail`: the report's *prose* attaches specific line numbers to specific statements, and those line numbers point at the wrong line (a comment or the preceding statement) in nearly every interior case. Crucially, CYCLE.md:118 **hand-asserts a self-clearance** — "I re-`read_range`'d `:1246-1309` directly this dispatch and cite the lines I observed: self-reflection at `:1272`/`:1296`, lumped scale `:1276-1279` ... confirmed by direct read" — but the direct read does NOT confirm those lines; the drift family is D2's own, not (only) D1's. This is the `producer-citation-drift-verify-not-self-invoked` friction pattern with an added self-clearance overclaim.

**surface-or-evidence — pass (feature-surface adaptation).** Per the adapted rule, a composition-root's evidence is the L0 driver/reduction range + the constituent down-links, NOT a new per-op algebraic claim. The L0 `MeasureSParameter` reduction range is cited, the `driven` upstream column resolves on-disk, and the `sparameter_reduce` constituent (forward-referenced) is a real same-cycle-landing chapter. The composition (S = `sparameter_reduce` over the driven driver's per-ω family) is supported by the cited source. The L4/L1 chapters correctly disclaim per-op algebra ("carries the compositional claim only"). Pass.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature chapter rotates nothing; it recomposes already-firm vocabulary outward. Formal no-op per the role-spec adaptation.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The port-kind (lumped | wave) and scaling-presence (generalized-S / de-embed) axes live in the constituent `sparameter_reduce` op (the harvester chapter carries them as `variant_axes`), not in the feature column. The feature chapter correctly absorbs them by reference ("absorbed into the reduction; does not surface as a new feature-level combinator"). No hidden branch at the feature level. Formal no-op.

**cross-reference-integrity — warning (load-bearing for this kind).** All down-links in the staged bodies resolve on-disk (`driven.L4/L1`, `frequency_sweep`, `ksp_solve` L4/L1, `gram_reduce`, `bilinear-form`) and every asserted constituent maturity matches on-disk (`driven.L4` = seed ✓; `frequency_sweep` = firm ✓; `gram_reduce` = rough-in(test-coverage-bounded) ✓; `bilinear-form` = rough-in ✓; the `sparameter_reduce` harvester chapter = `firmness: rough-in` ✓). The two `[old]` anchor blocks (index matrix rows + SUMMARY triples) match on-disk verbatim, so the edits apply cleanly. Matrix placement is correct under `*output products*` alongside capacitance/inductance (c074), and alpha order `capacitance < eigenfrequency-qfactor < inductance < sparameters` is correct. Within-column ordering is high→low (L4→L1→L0) in both the matrix and the SUMMARY block — the deliberate FEATURE-SURFACE exception, correctly applied. The `warning` (not pass) is for TWO build-ordering couplings that are real same-cycle hazards, both surfaced by D2 but worth the integrator's explicit attention: (a) the consolidated SUMMARY/index block references D4's `eigenfrequency-qfactor.{L4,L1,L0}.md`, which are NOT yet on disk (staged only in D4's report dir) — a SUMMARY row to a missing file is a hard mdBook break; D2 correctly carries the apply-order note (D4 before D2) + a fallback (omit the 3 eigenfrequency SUMMARY rows + defang the index row to plain-text); and (b) the `sparameter_reduce` plain-text refs depend on D6 (harvester) landing `book/src/L4/sparameter_reduce.md` for the upgrade (see issues). Neither is a defect in D2 — both are correctly handled — but the cross-reference graph is only build-safe under the stated apply order, so `warning` flags the dependency for the integrator rather than `pass`.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (feature columns link DOWN to constituents and across to the producing driver column, not via lowering-edge labels). The L1-vs-L4 prose discusses the correct pair. The L0 "Lifts to" points up to L1/L4 correctly. Pass.

**plan-kind-consistency — pass.** All three chapters declare `kind: feature-surface` / `status: seed` (uniform token, no `(exemplar)`/`(composition-root)` qualifier — correct per the batch-22 codification). The content shape matches: composition-root prose, constituent down-link tables, no new per-op algebraic claim. The `seed` token is justified (a composed constituent, `sparameter_reduce`, is rough-in; a feature column promotes past seed only when all constituents firm). Consistent.

**skill-uptake-survey — pass (telemetry only).** D2 explicitly names the relevant skills it expects the repairer/integrator to invoke: `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (for the `sparameter_reduce` ref upgrade) and the "Integration may materialize implied components as stubs" directive (with the ≥2-converging-reference bar evidenced: D1 dep-map row + 3 chapters + the `driven.L4.md:55,98,157` forward-refs — all verified present on-disk). Skill awareness is well-surfaced.

### Issues found

1. **[citation-validity / fail] Systematic interior-pinpoint drift (1–3 lines low) across all three staged chapters + CYCLE.md evidence.** Ground-truth lines (read directly this dispatch):
   - lumped self-reflection `vi.S.real(vi.S.real() - 1.0)` is at **1275** (D2 cites `:1272` in `sparameters.L0.md:50`/`sparameters.L1.md:37`/CYCLE.md:117, and the range `:1271-1272` in `sparameters.L0.md:32` — the real write is 1275, drift −3);
   - wave self-reflection is at **1297** (D2 cites `:1296` in L0:32/L1:37/CYCLE.md:117; and range `:1295-1296` in L0:32 — drift −1/−2);
   - driving-port index `drive_port_idx = measurement_cache.ex_idx` is at **1263** (D2 cites `:1261` in L0:32, L0:41, L4:43, CYCLE.md:117 — drift −2);
   - lumped generalized-S `vi.S *= std::sqrt(...)` is at **1280** (block 1277-1281); D2 cites range `:1276-1279` (L0:35, L1:38, CYCLE.md:117) which STOPS at 1279, BEFORE the `sqrt` write at 1280 — the cited range misses the statement it names;
   - the non-mixed-port guard `return;` is at **1259** (guard `if(...)` 1256-1257, `return` 1259, block 1256-1260); D2 cites `:1254-1258` (L0:37, CYCLE.md:117) — that range is the comment 1253-1255 + the `if` open, and EXCLUDES the `return` at 1259;
   - the wave de-embed `vi.S *= std::exp(...)` IS in range: actual 1301-1302, D2 cites `:1299-1303` (loose but covers it) — OK;
   - lumped projection interior: `(*s) * E.Real()` is at **287** (D2 cites `:286`, which is `InitializeLinearForms`), `dot.imag(...)` at **290** (D2 cites `:288-289`, the `if` header), `Mpi::GlobalSum` at **292** (D2 cites `:291`) — all in `sparameters.L0.md:28` / `sparameters.L1.md:36` — drift −1/−2;
   - wave projection interior: `Transfer(...)` at **787-788** (D2 cites `:786-787`), complex `dot` at **789-790** (D2 cites `:788-790`, 788 is the imag Transfer), `Mpi::GlobalSum` at **791** (correct) — `sparameters.L0.md:30` / `sparameters.L1.md:36` — drift −1.
   Locations to repair: `sparameters.L0.md` lines 28, 30, 32, 35, 36, 37, 41, 50; `sparameters.L1.md` lines 36, 37, 38, 60 (range `:1272-1303` → should be `:1275-1302`); `sparameters.L4.md` line 43 (`:1261` → `:1263`); CYCLE.md lines 117–118 (the evidence section + the self-clearance sentence). The enclosing ranges (`:1246-1309`, `:283-294`, `:780-793`, `:1141`, `:1239`) are all correct and need no change. Severity: medium — every range bounds-checks OK so the build is unaffected, but the prose attaches wrong line numbers to named statements, which is precisely what citation-validity guards.

2. **[citation-validity / fail-supporting] Self-clearance overclaim in CYCLE.md:118.** D2 writes that it cross-checked D1's drifted lines, re-read `:1246-1309` directly, and cites "the lines I observed ... confirmed by direct read." The observed lines (`:1272`/`:1296`/`:1276-1279`) do NOT match the direct read (1275/1297/1280). This is the `producer-citation-drift-verify-not-self-invoked` pattern with the aggravating factor that the producer asserted a manual verification that the tool/source contradicts. The repairer should both correct the lines AND soften/remove the "confirmed by direct read" assertion. (Telemetry: this is a candidate recurrence data point for the friction-ledger entry — a producer hand-asserting an off-by-N as correct, which `--anchor` would have settled.)

3. **[cross-reference-integrity / warning — UPGRADEABLE, not a defect] `sparameter_reduce` plain-text refs are now upgradeable to live links.** At D2's dispatch time `book/src/L4/sparameter_reduce.md` did not exist, so the 3 chapters correctly reference `sparameter_reduce` as plain-text *(rough-in; no anchor yet)* per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention (build-SAFE). VERIFIED THIS DISPATCH: the sibling D6 harvester (`reports/2026-06-03T045739Z-harvester-sparameter-reduce-chapter/CYCLE.md:46`) carries a `create:book/src/L4/sparameter_reduce.md` block (`firmness: rough-in`) landing the chapter THIS cycle. Therefore, once D6 applies, the plain-text refs CAN be upgraded to `../L4/sparameter_reduce.md` live links via `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. Plain-text occurrences for the repairer/integrator to upgrade (post-D6): `sparameters.L4.md` lines 17, 31-33 (composition comment), 39, 51, 54, 61 (down-link table), 67; `sparameters.L1.md` lines 39, 50; `sparameters.L0.md` lines 28, 37, 46. The upgrade is conditional on D6's chapter being on disk at apply time (today it is MISSING on disk — it lands same-cycle). D2 itself flags this in dependency-note #1 and OQ `sparameters-down-link-stub-upgrade-when-sparameter-reduce-lands`, but frames it as a *stub-materialization* action (D2 was apparently unaware D6 authors the full chapter); the repair is simpler than D2 anticipated — no stub needed, the real chapter lands. Severity: low (hygiene; better end-state, not a build blocker).

4. **[cross-reference-integrity / warning — build-ordering, handled] D4 `eigenfrequency-qfactor.*` apply-order dependency.** The consolidated SUMMARY block (CYCLE.md:101-103) and index matrix row (CYCLE.md:59) reference `eigenfrequency-qfactor.{L4,L1,L0}.md`, which are MISSING on disk (staged only in `reports/2026-06-03T045739Z-layer-intro-author-eigenfrequency-qfactor-output/`, and that report DEFERS its own index/SUMMARY rows to D2 — confirmed at its CYCLE.md:70-79). A SUMMARY row to a missing file is a hard mdBook break. D2 correctly carries dependency-note #2 (apply D4 before D2) + a complete fallback (omit the 3 eigenfrequency SUMMARY rows + defang the index row to plain-text; the sparameters rows are independent and unaffected). No defect in D2 — flagged so the integrator honors the apply order or the fallback. Severity: low (correctly handled; surfaced for integrator attention).

5. **[observation, non-blocking] Output-product cohort approaching by-kind nesting threshold.** With the consolidated block applied, the output-product cohort reaches 4 columns (capacitance / eigenfrequency-qfactor / inductance / sparameters) in a still-flat `feature/index.md` matrix + flat SUMMARY list. D2 already files OQ `feature-part-by-kind-nesting-output-product-cohort-grouping` (carried from c074 D2) flagging this for the meta-phase structural-reorg wave. No action for this cycle; noted as confirmation the OQ is live.

---

## Repair

All findings were mechanical/surgical and within repair authority. The two flagged checks (citation-validity FAIL, cross-reference-integrity warning) are both `repaired`; the FAIL clears to pass now that the interior pinpoints are corrected against directly-read source.

### Fixes attempted

- **Finding 1 — citation-validity FAIL: systematic interior-pinpoint drift (1–3 lines low) across the 3 staged chapters + CYCLE.md evidence.**
  - **Decision:** repaired.
  - **Action:** Hand-read the actual source ranges via palace-codemap `read_range` (brace-boundary discipline): `postoperator.cpp:1246-1309` (`MeasureSParameter`), `lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`, plus `:1141`/`:1239`. Corrected every drifted pinpoint to ground truth, harmonized to D6's verified line-map: self-reflection write lumped `:1272→:1275` (block `:1271-1272→:1273-1276`) / wave `:1296→:1297` (block `:1295-1296→:1295-1298`); `drive_port_idx = ex_idx` `:1261→:1263`; lumped generalized-S sqrt range `:1276-1279→:1278-1281` (write `:1280`); non-mixed-port guard `:1254-1258→:1256-1260` (`return` `:1259`); wave de-embed `:1299-1303→:1299-1302`; lumped projection `(*s)*E.Real()` `:286→:287`, imag `:288-289→:290`, `GlobalSum` `:291→:292` (range `:286-289→:287-290`); wave Transfer `:786-787→:787-788`, complex dot `:788-790→:789-790` (range `:787-790→:789-790`); `GetLumpedPortOp()` loop `:1266→:1267`; L1 down-link range `:1272-1303→:1275-1302`; L4 `ex_idx` `:1261→:1263`. Files: `sparameters.L0.md` (§composition steps 2/3/4/5, §inputs/outputs, §status), `sparameters.L1.md` (§composition step 2, down-link table), `sparameters.L4.md` (§inputs/outputs), `CYCLE.md` (§Supporting evidence L0 citations). The enclosing ranges (`:1246-1309`, `:283-294`, `:780-793`, `:1141`, `:1239`) were correct and left unchanged.
  - **Sub-fix (CYCLE.md:118 false self-clearance).** The producer prose hand-asserted "confirmed by direct read" for lines the direct read contradicts (`producer-citation-drift-verify-not-self-invoked` + self-clearance overclaim). Rewrote the parenthetical into an honest repair note: drops the false self-clearance, records that the interior pinpoints drifted and were re-read + corrected, and notes they now harmonize with D6's chapter. Mechanical truth-correction, no new content authored.

- **Finding 2 — cross-reference-integrity: `sparameter_reduce` plain-text → live-link upgrade.**
  - **Decision:** repaired.
  - **Action:** D6 (harvester) authors the real `book/src/L4/sparameter_reduce.md` (rough-in) this cycle (verified in `reports/2026-06-03T045739Z-harvester-sparameter-reduce-chapter/CYCLE.md`). Upgraded all plain-text `` `sparameter_reduce` *(rough-in; no anchor yet)* `` prose/table references to live links `[`sparameter_reduce`](../L4/sparameter_reduce.md)` per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` — in `sparameters.L0.md` (3), `sparameters.L1.md` (3 prose/table), `sparameters.L4.md` (7 prose/table + frontmatter `composes:` wording). Code-block path comments (the `── L4/sparameter_reduce` composition-block comment and the `sparameters = sparameter_reduce ... ∘ driven_family` formula) were left as code (not markdown links, not linkcheck targets). Updated CYCLE.md dependency-note #1 + note #3 to reflect: D6 authors the real chapter (no stub needed), refs upgraded, apply-order D6-before-D2, with a plain-text-downgrade fallback if D6 fails to land. The live link is build-validated only at finalize after D6 lands, so it is safe.

- **Finding 3 — D4 `eigenfrequency-qfactor.*` batch-ordering dependency.**
  - **Decision:** not-needed (already complete in D2).
  - **Action:** Confirmed CYCLE.md dependency-note #2 already carries the complete coupling: per-report apply order D4-before-D2 + a complete fallback (omit the 3 eigenfrequency SUMMARY rows + defang the index matrix row to plain-text; sparameters rows independent/unaffected). The critic concurred (issue #4: "No defect in D2"). No edit required.

### Unrepairable findings

None. All flagged findings were mechanical (pinpoint correction against directly-read source, plain-text→live-link upgrade, false-self-clearance truth-correction) — no substantive authoring required.

## Suggested resolution

`ready`. Notes for the integrator:
- **Apply order is load-bearing:** D6 (harvester `book/src/L4/sparameter_reduce.md`) AND D4 (`feature/eigenfrequency-qfactor.{L4,L1,L0}.md`) must both apply BEFORE D2. The 3 sparameters chapters now carry live links to `../L4/sparameter_reduce.md`, and D2's consolidated SUMMARY/index block references the D4 eigenfrequency files — both resolve only under that order. The build validates at finalize, so the live links are safe once D6+D4 land.
- **Fallbacks (only if a dependency fails to land):** downgrade the `sparameter_reduce` live links back to plain-text (CYCLE.md note #1); omit the 3 eigenfrequency SUMMARY rows + defang the index row (CYCLE.md note #2).
- The interior pinpoints across all 3 chapters + CYCLE.md now match D6's verified line-map; a finalize-time `citecheck --anchor` on the three primary symbols (`MeasureSParameter`, both `GetSParameter`) remains green (anchors unchanged).
