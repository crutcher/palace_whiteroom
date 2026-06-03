---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T052418Z
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
repaired_at: 2026-06-03T054800Z
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

# META: verification of "Combinator candidate — sparameter_reduce"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` reports 26/26 citations in-bounds with clean path-hygiene (no out-of-range, no malformed paths). The bounds layer is clean. However, the *anchor* (pinpoint) layer carries drift, which the dispatch scope pre-flagged and D6 (the coupled harvester) already corrected on-disk. I re-read the load-bearing `MeasureSParameter` body (`postoperator.cpp:1246-1309`) and the two projection kernels and confirm D6's corrections against the source. D1's pinpoints into `postoperator.cpp` are systematically shifted by ~+2 lines relative to disk (the function body grew; D1's numbers predate D6's re-pin). The drifts are sub-anchors of in-bounds ranges, so they pass the mechanical bounds scan but mis-locate the named tokens. The projection-kernel citations (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`) and all book-side cross-references verify exactly. Marked `warning` (not `fail`) because every drifted pinpoint is a sub-line offset inside a correctly-bounded range pointing at the right structure, and D6 already holds the corrected line-map — the repairer can harmonize D1's dep-map row + §Pattern-instances/§Supporting-evidence pinpoints to D6's on-disk numbers.

**surface-or-evidence — pass.** This is a combinator-miner proposal that DOES modify surface (it adds a real `book/src/L4/index.md` dep-map row + a cohort-prose addition) AND carries the rotation/structural claim (the linear-projection reduce-to-matrix fold) backed by the positive `MeasureSParameter` witness + two `GetSParameter` kernels + unit-test evidence for the projection kernel. It is not a pure stranded rotation_claim. The over-unification analysis (the do-NOT-merge-with-`gram_reduce` guard) is grounded in the on-disk `gram_reduce.md:178-189` c074 D6 closed-negative probe, which I read and which explicitly scopes S-parameters out as "a per-column port-mode LINEAR PROJECTION ... NOT symmetric-Gram ... author their OWN reduction verb." The sibling framing (linear-projection vs bilinear Gram, same `Matrix[p,p]` shape) is faithful to that source.

**rotation-quality — pass.** The proposal asserts a structural reduction: scattered C++ (two structurally-identical port loops in `MeasureSParameter` + two cached `GetSParameter` projections) collapses to ONE per-ω `matrix_from_columns` reduction with the port-kind difference absorbed into a `PortMode` + `scale` closure. This is genuine state-hiding / threaded-assembly compression (the two-phase project-then-postscale C++ becomes a single declarative fold), not a 1:1 rename. The L4 form is strictly more compact/equational than the L0 loop body. Passes.

**variant-axis-coverage — pass.** The proposal enumerates the variant axes explicitly: port-kind (lumped | wave, the load-bearing axis, whole-model XOR per the `postoperator.cpp` mixing guard), scaling-presence (generalized-S via `|R|>0` resistive guard; de-embed via `d_offset≠0`, with the absent case identified as the scale-axis identity element), and element-type (complex, pinned). The single-excitation-per-port precondition is correctly scoped as a precondition, not a hidden branch. No hidden combinations. The `|R|>0` guard and `d_offset=0` identity case are both anchored to real source lines (verified the `if (std::abs(data.R) > 0.0)` guard on disk).

**cross-reference-integrity — pass.** All cross-references resolve: `gram_reduce.md`, `inner_product.md`, `linear_combination.md`, `frequency_sweep.md`, `black-box-vs-accelerated-kernels.md` all exist on disk; `feature/driven.L4.md` exists and lines 55/97-99/157 carry the cited forward-references verbatim. The one live link in the proposed dep-map row — `[`sparameter_reduce`](./sparameter_reduce.md)` — points at a file that does NOT exist as of D1 alone, BUT is authored this same cycle by the coupled D6 harvester (`reports/...-harvester-sparameter-reduce-chapter/CYCLE.md`, a `create:book/src/L4/sparameter_reduce.md` block). Per the integrator-coupling framing, the live link is VALID given D6 lands same-cycle. D1 itself is fully aware of this and supplies the correct integrator guidance (sequence the chapter create before/with the row, or downgrade to plain text per the `rough-in-forward-reference-must-be-plain-text-not-live-link` friction-ledger entry). This is a coupling to flag for the integrator, NOT a defect. See Issue 2.

**edge-label-fidelity — pass.** The over-unification edge (the `sparameter_reduce` ↔ `gram_reduce` sibling relationship) is discussed in prose exactly as labeled: the proposal frames it as the linear-projection SIBLING (NOT a specialization / NOT a subsume) and the prose, dep-map row, and cohort note all consistently narrate "same `Matrix[p,p]` shape, DIFFERENT fold." The Lowers-to direction (L4 → identity-in-form on the body to the per-port linear functional, no dedicated L4>L3 theme, in-line-marker route) matches the `gram_reduce`/`inner_product`/`linear_combination` precedent and is narrated forward (high→low) per the layer-direction discipline. No label/prose mismatch.

**plan-kind-consistency — pass.** This is a combinator-miner proposal correctly NOT over-formalizing: it adds only the index dep-map row + cohort note + SUMMARY flag, and explicitly defers the full chapter to a harvester per the combinator-miner/harvester role split ("this report does **not** create `book/src/L4/sparameter_reduce.md` — that is the harvester's formalization job"). The declared `rough-in` status is well-warranted via the warrant-first §Status: structure is firm-on-positive-structure (single positive `MeasureSParameter` witness) but gated to `rough-in` by (1) reduction-level assembly being integration-level / test-unconfirmed (only the projection KERNEL is unit-tested) and (2) the per-port projection L1 home not yet being firm. The deliberate choice of plain `rough-in` over `rough-in (test-coverage-bounded)` is reasoned (both the L1 home is absent AND the laws are test-gated, so the test-coverage-bounded qualifier — which presumes a fully-anchored structure with only laws gated — does not fit). Content shape matches the declared kind.

**skill-uptake-survey — pass.** The report references its relevant skill invocations: `disciplined-cross-pipeline-combinator-mining-gate` (run as the single-witness probe, with the step-by-step disposition: single-pipeline driven, lumped-vs-wave is a variant axis not a 2nd pipeline), `verify-citation-range` via the codemap re-verification pass, and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (flagged for the harvester/repairer to upgrade the `driven.L4.md` forward-refs once the chapter lands). Telemetry present.

### Issues found

**Issue 1 — citation-validity (warning): D1's `postoperator.cpp` pinpoints drifted ~+2 lines vs disk; the dep-map row carries a drifted range.** (`CYCLE.md` §Pattern-instances, §Supporting-evidence, and the §Proposed-changes dep-map row's last cell.) Verified on disk (`postoperator.cpp:1246-1309`):
  - `drive_port_idx = measurement_cache.ex_idx` — D1 cites `:1261`; on disk it is `:1263` (DRIFT +2). D6 corrected to `:1263`.
  - function close — D1 cites body `:1249-1307` / the dep-map row cites `postoperator.cpp:1141,1239,1246-1307`; on disk the function closes at `:1309` (body `1247-1308`). D6 corrected to `:1246-1309`.
  - lumped self-term — D1 `:1271-1274`; on disk the `if (idx == drive_port_idx) { vi.S.real(vi.S.real() - 1.0); }` block is `:1272-1275`.
  - lumped generalized-S scale — D1 `:1276-1280`; on disk the `if (std::abs(data.R) > 0.0)` block is `:1277-1280`.
  - wave self-term — D1 `:1296-1299`; on disk `:1294-1297`.
  - wave de-embed scale — D1 `:1301-1304`; on disk the two `vi.S *= std::exp(...)` lines are `:1300-1302`.
  - lumped/wave loop bounds — D1 `:1265-1284` / `:1286-1306`; on disk approximately `:1267-1286` / `:1287-1307`.
  Severity low: all are sub-line offsets inside in-bounds ranges, all point at the correct structure, and D6 already holds the corrected line-map. The repairer can harmonize D1's row + instance/evidence pinpoints to D6's on-disk numbers (the corrected set is enumerated in D6's CYCLE.md §Evidence). The `lumpedportoperator.cpp:283-294` and `waveportoperator.cpp:780-793` projection-kernel citations are EXACT — no correction needed there.

**Issue 2 — cross-reference-integrity (integrator coupling, NOT a defect): the dep-map row's live link `[`sparameter_reduce`](./sparameter_reduce.md)` resolves only because D6 authors the chapter this same cycle.** (`CYCLE.md` §Proposed-changes, first `edit:book/src/L4/index.md` block.) D1 alone proposes a live link to a file it does not create; the coupled D6 harvester (`reports/2026-06-03T045739Z-harvester-sparameter-reduce-chapter/CYCLE.md`) supplies the `create:book/src/L4/sparameter_reduce.md`. The pair MUST be applied together (chapter create before/with the row) or the link is a `linkcheck2` hard error. D1 itself documents this coupling and the fallback (downgrade the row's first cell to plain `` `sparameter_reduce` `` if the row is applied before the file exists). Flagged for the integrator as a coupled-pair sequencing requirement — not a content defect.

**Issue 3 — build-readiness (advisory): D1's SUMMARY.md insertion instruction cites literal line numbers (after line 47 `nrm2`, before line 48 `Outer-driver caps`) that will be stale by +1 if D3 lands first.** (`CYCLE.md` §Proposed-changes note, the SUMMARY.md flag.) D3 (`eigenfreq_qfactor_reduce`, `reports/2026-06-03T045739Z-combinator-miner-eigenfreq-qfactor-reduce/CYCLE.md`) ALSO inserts into `book/src/SUMMARY.md` and `book/src/L4/index.md` this cycle, prepending its bullet before `fe_assemble` (current SUMMARY line 43 / index line 96). That shifts every line below it by +1. D1's text anchors (`nrm2` line / the `Outer-driver caps` boundary) survive the shift, but the literal line numbers quoted in D1's prose become advisory/stale. NO anchor collision: D1 inserts at alpha position after `nrm2` (s > n, last data-algebra row before the Outer-driver group); D3 inserts between `dot` and `fe_assemble` (e... < f...) anchored on `fe_assemble` — distinct, non-adjacent alpha neighborhoods, confirmed against the on-disk SUMMARY (lines 40-48) and index (lines 95-105). Integrator should apply by text anchor, not the quoted line numbers; both reports correctly use tight alpha-neighbor anchoring to avoid mutual collision.

**Issue 4 — citation-validity (minor, advisory): the dep-map row's downward-content cite `postoperator.cpp:1141,1239,1246-1307` inherits the same close-line drift (should be `:1246-1309`).** (`CYCLE.md` §Proposed-changes, the dep-map row's 3rd cell "L1 the port-mode projection by identity-in-form...".) Same correction as Issue 1's function-close drift; the `:1141` and `:1239` projection-cache pinpoints are correct on disk (both are `vi.S = data.GetSParameter(*E)` sites). Bundle with Issue 1 for the repairer.

## Repair

### Fixes attempted

- **Finding (Issue 1 + Issue 4): citation-validity warning** — D1's `postoperator.cpp` `MeasureSParameter` interior pinpoints drifted ~+2 lines vs disk (pass `citecheck --scan` bounds but mis-locate the named tokens). The dep-map row's downward-content cite carried the same close-line drift.
  - **Decision**: repaired.
  - **Action**: Hand-Read `palace/models/postoperator.cpp:1246-1309` (the full `MeasureSParameter` body) + `:1139-1143` / `:1237-1241` (the two `vi.S = data.GetSParameter(*E)` cache sites) via the codemap to confirm the on-disk line-map before editing. Harmonized every drifted pinpoint to D6's verified numbers across `CYCLE.md` §Pattern-instances (Instance 1), §Algebraic-intuition (the `|R|>0` scale-skip cite), the §Proposed-changes dep-map row (3rd cell downward-content cite + 4th cell status warrant), §Supporting-evidence, and §Status-warrant:
    - `drive_port_idx`: `:1261` → `:1263`
    - function body / close range: `:1249-1307` / `1246-1307` → `:1247-1308` (body) / `:1246-1309` (def→close)
    - lumped self-term: `:1271-1274` → `:1272-1275`
    - lumped generalized-S scale: `:1276-1280` → `:1277-1280`
    - wave self-term: `:1296-1299` → `:1294-1297`
    - wave de-embed scale: `:1301-1304` → `:1300-1302`
    - lumped loop bounds: `:1265-1284` → `:1267-1286`
    - wave loop bounds: `:1286-1306` → `:1287-1307`
    - downward-content cite: `postoperator.cpp:1141,1239,1246-1307` → `...,1246-1309`
  - **Untouched (confirmed exact on disk)**: the projection-kernel cites `lumpedportoperator.cpp:283-294` + `waveportoperator.cpp:780-793` (per scope, EXACT — do not touch); the cache pinpoints `:1141` / `:1239`; the precondition guards `:1255-1259` / `:1257`; the eigensolver/Q-factor cross-cite `postoperator.cpp:1174-1217` (cited from `gram_reduce.md`, not part of the drifted MeasureSParameter set).

- **Finding (Issue 2): dep-map live link `[sparameter_reduce](./sparameter_reduce.md)` resolves only because D6 authors the chapter same-cycle.**
  - **Decision**: not-needed (coupling, not a defect — explicitly per the critic and the dispatch note). Left the live link in place; it is a coupled-pair the integrator sequences (D6's `create:book/src/L4/sparameter_reduce.md` before/with D1's row). D1 already documents the plain-text fallback. No repair authority action.

- **Finding (Issue 3): SUMMARY.md insertion instruction cites literal line numbers that go stale +1 if D3 lands first.**
  - **Decision**: not-needed (advisory; no collision). D1's text anchors (`nrm2` row / `Outer-driver caps` boundary) survive the shift; the literal line numbers are integrator-guidance prose, applied by text anchor. Critic confirmed no alpha-neighbor collision with D3 (D1 anchors on `nrm2`, D3 on `fe_assemble`). No edit needed.

### Unrepairable findings

None. The sole flagged finding (citation-validity warning) was a mechanical pinpoint drift with a fully on-disk-verified corrected line-map (cross-confirmed by hand-Read this pass) — squarely within repair authority (citation line range off by a small offset). All other checks passed at critique.

## Suggested resolution

`ready`. Notes for the integrator:
- **Coupled-pair sequencing (Issue 2)**: apply D6's `create:book/src/L4/sparameter_reduce.md` before (or atomically with) D1's `book/src/L4/index.md` dep-map row, so the `[sparameter_reduce](./sparameter_reduce.md)` live link resolves. If for any reason the row lands before the file, downgrade the row's first cell to plain `` `sparameter_reduce` `` per the `rough-in-forward-reference-must-be-plain-text-not-live-link` friction-ledger entry (D1 documents this fallback).
- **Apply SUMMARY.md / index inserts by TEXT ANCHOR, not the quoted literal line numbers (Issue 3)** — D3 (`eigenfreq_qfactor_reduce`) inserts into the same two files this cycle and shifts lines by +1; the quoted numbers in D1's prose are advisory. D1 anchors at alpha position after `nrm2` (data-algebra group, before the Outer-driver group); no collision with D3's `fe_assemble`-anchored insert.
- All L0 pinpoints now match D6's verified on-disk line-map (re-confirmed by hand-Read this repair pass).
