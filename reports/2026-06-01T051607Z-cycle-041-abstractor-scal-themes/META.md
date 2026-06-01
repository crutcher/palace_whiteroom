---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T053000Z
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
---

# META: verification of "TWO adjacent thin-identity lowering themes for `scal` — `scal-fold-specialization` (L2>L1) + `scal-body-identity` (L3>L2)"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` over the full report: `10 ok, 0 failing`. Anchor-checked the three load-bearing L0 pinpoints: `vector.cpp:203-227 --anchor 'operator*='` → ok (anchor :203 in range); `vector.hpp:262-270 --anchor 'Normalize'` → ok (:262,:264 in range); `vector.hpp:98-99 --anchor 'operator*='` → ok (:99 in range). I then Read `vector.cpp:200-227` directly to adjudicate the report's `207-211` sub-pinpoint: the source has `if (si == 0.0) { Real() *= sr; Imag() *= sr; }` spanning lines 207-211 exactly, and the general complex `forall_switch` kernel at 212-225 — both sub-pinpoints in the report are correct as written. (A naïve `--anchor 'imag'` returns a `[DRIFT -1]` to line 206 because `s.imag()` is *read* at 206, one line above the branch the report actually cites; this is NOT a drift in the report's claim — the report cites the branch body region 207-211, which is correct. Flagging here so the repairer does not "fix" a correct pinpoint.) The `linear_combination.md:68` cite resolves into the fenced specialization-identity block containing `scal(α, x) = linear_combination [(α, x)]` (verified by Read). The `krylov-step-body-identity.md:97` cite resolves to the point-3 applicability condition that names `scal` among the seven L1 primitives as L3-native by signature shape (verified). No `verified_against:` YAML block in this report (the `## Verified-against` sections are prose, not a fenced YAML payload), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Both proposals are `new:` files (new theme entries), not refinements of existing surface. They add surface (two new lowering-theme chapters + index/SUMMARY rows) AND carry evidence (firm-endpoint anchors on both L-levels + fold-parent + krylov-step mirror + transitive L0). Not a pure rotation_claim; not a pure retroactive backfill. The new-entry shape clears this check.

**rotation-quality — pass (correctly framed as identity-in-form, with explicit non-rotation justification).** Both themes assert identity-in-form rotations, NOT compaction rotations. This is the right call and is well-justified: `scal` is a BLAS-1 leaf with signature `Scalar -> Tensor[N] -> Tensor[N]` textually identical across L1/L2/L3, no kernel fusion to unfold and no iteration view to dissolve. The report does not dress these up as compaction rotations — it explicitly states "no abstraction is imposed and none is removed" and routes the genuine rotation content to the *adjacent fold-parent / wrapper siblings* (the four fold-selection mechanisms — arity dispatch, two-sub-selection, arity-3→2 fall-through, pinned-summation-order — collapse to nothing at arity 1; the `(op,K,s)`→`IterState` consolidation + outer-loop dissolution have no analog for a leaf). The arity-1-degenerate-shadow framing is correct: `scal(α,x) = linear_combination [(α,x)]` is `linear_combination.md` law 6 at the singleton case (verified at the cited block). The value-exact AND bit-exact claim is correct and distinct from the L1 entry's law-4 fusion caveat: L1/scal.md:57 notes `scal(α, scal(β, x))` vs `scal(α·β, x)` may differ at bit-level under *fusion of two scal calls* — but the report's bit-exact claim concerns the *single arity-1 row* (one term, one rounding per element = the same single operation at both layers), which is genuinely bit-exact. No contradiction. Per the critic guidance, identity-in-form / threaded-state-trivial cases are pass, not fail — and these are correctly NOT claimed as rotations-that-compact.

**variant-axis-coverage — pass.** The variant axes for `scal` (element-type real/complex; real-α-against-complex-x scalar promotion) are explicitly addressed: `scal-fold-specialization` applicability condition 2 names the shared-element-type axis and the `s.imag()==0.0` promotion branch, routing it to `concepts/scalar-promotion` and marking it "absorbed at construction at L1/L2; not a distinct lowering sub-pattern." The arity axis (the only axis the fold-parent dispatches on) is explicitly scoped to "exactly 1" (condition 1). No hidden branches — the complex/real kernel split is named and located (`vector.cpp:207-211` vs `212-225`) and correctly classified as a complex-scalar-shape specialization absorbed below the layer, consistent with L1/scal.md:34.

**cross-reference-integrity — pass.** All cross-referenced firm artifact files exist: `book/src/L1/scal.md`, `book/src/L3/scal.md`, `book/src/L2/linear_combination.md`, `book/src/L2-L1/linear-combination-fold-specialization.md`, `book/src/L3-L2/krylov-step-body-identity.md`, `book/src/L1-L0/scal-mutation-rotation.md`, `book/src/L2/index.md`, `book/src/concepts/scalar-promotion.md`, `scaffolding/decisions/axpby-as-primitive.md`. The insertion-anchor rows all exist as cited: L2-L1/index.md:14 (`linear-combination-fold-specialization` anchor row), L3-L2/index.md:14 (`ksp-solve-outer-driver` anchor row), SUMMARY.md:43 + :61. The `L2/index.md` §"Fold-cohort boundary" reference resolves (line 75, "load-bearing, do NOT merge"). The only forward reference is `book/src/L2/scal.md`, which does NOT yet exist — but this is the wave-1 D3 floor entry explicitly declared to "land at integration alongside these themes" (standard co-land pattern stated in frontmatter inputs + §Summary). Build-readiness fence guard: fence enumeration gives 12 markers / 6 balanced pairs (66-279, 281-527, 533-536, 543-546, 553-556, 558-561), even parity; both `new:` firm-bodies enclose their `## Status` INSIDE the fence (244-256 within 66-279; 487-507 within 281-527); the L2/L3 form blocks use 4-space indented code, not nested triple-backtick fences, so no nested-fence truncation risk. The firm-body-outside-fence defect is absent.

**edge-label-fidelity — pass.** `scal-fold-specialization` is labeled L2>L1 and the prose narrates exactly the L2-floor-LHS → L1-leaf-RHS edge (forward, high→low): "## L2 form (LHS)", "## L1 form (RHS)", "## The fusion-selection rewrite (L2 → L1)". `scal-body-identity` is labeled L3>L2 and narrates exactly the L3-whole-tensor-LHS → L2-floor-RHS edge: "## L3 form (LHS)", "## L2 form (RHS)", rewrite shown as `scal α x (L3) ⇒ scal α x (L2)`. Both narrate FORWARD per the high→low layer-definition discipline; reverse-direction (lift) notes are correctly quarantined to §"Open questions / caveats" working-notes, NOT in the chapter body. The L3-L2/index row and L2-L1/index row each carry the correct edge endpoints. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Both entries declare `## Status: firm` and the content matches: identity-in-form lowering edges between firm endpoints on both L-levels (L1 cycle-004, L3 cycle-011, L2 cycle-041-D3 co-landing), no rough-in placeholders, no speculative operators ("## Speculative L1/L3 operators: None" in both). The `firm` claim is justified by the firm-on-both-endpoints + the identity-in-form structure (no constructive sub-part, no negative-anchor reconstruction). The justification-kind declarations (`structural` dominant + secondary `algebraic`/`empirical-match`) are coherent with the identity-in-form shape. Classification is correct: these are firm themes, not rough-ins or partly-constructive.

**skill-uptake-survey — pass.** The report references its `citecheck --anchor` self-verification of L0 anchors (§Supporting evidence, "self-verified 2026-06-01 (citecheck `--anchor`...)") — the `verify-citation-range` mechanical realization. The shape (identity-in-form lowering theme) does not strongly imply a dedicated authoring skill beyond what is referenced. Telemetry-only; non-blocking.

### Issues found

No blocking issues. Two non-blocking notes for the repairer/integrator:

1. **(Non-issue, anti-repair flag) — `vector.cpp:207-211` is correct; do NOT "fix" to 206-210.** A mechanical `citecheck --anchor 'imag'` on this range returns `[DRIFT -1]` pointing at line 206, because `s.imag()` is *read* at line 206. But the report cites 207-211 for "the `si == 0.0` two-real-call promotion branch" — and the branch body `if (si == 0.0) { Real() *= sr; Imag() *= sr; }` is exactly lines 207-211 (verified by direct Read of `reference/palace/palace/linalg/vector.cpp:200-227`). The pinpoint is accurate. Flagging so an automated drift-sweep does not regress a correct citation. Severity: none (informational).

2. **Forward reference `book/src/L2/scal.md` does not yet exist on disk** (`reports/.../CYCLE.md` §Summary, §Proposed-changes link targets, frontmatter inputs). This is the co-landing wave-1 D3 floor entry, explicitly declared to land at integration alongside these two themes. Both themes link to it as a live `[scal](../L2/scal.md)` link. This is correct per the stated co-land pattern AND required for `linkcheck2` to pass — the integrator must apply D3 (`L2/scal.md`) in the same cycle as these themes, or the live links break the build. Severity: low (cross-dispatch ordering constraint, not a defect in this report). Surfaced as an integrator sequencing note, not a repair item.

### Notes on focused-attention items (dispatch directive)

- **Count-ownership (item 4): clean.** The report touches only its two theme files, two index theme-list rows (one each, after the named anchor rows), and two SUMMARY registrations. It explicitly defers all consolidated tallies (L2-L1/index §"Vocabulary cohort" firm-list, §"Working Notes" cohort-growth log) to D7, stated in three places (§Summary COUNT-OWNERSHIP, two per-index insertion notes, §Count-ownership note). No tally mutation in the proposed changes — verified by inspecting the `edit:` blocks (they carry only the single new row each, with the anchor row reproduced unchanged for placement context).
- **`linear_combination` cited as fold-parent not merged (item 3): clean.** Every reference frames `scal` as "arity-1 member of the `linear_combination` fold, cited as fold-parent but NOT merged," tied to the load-bearing `L2/index.md` §"Fold-cohort boundary" do-NOT-merge note (verified present at L2/index.md:75). No merge is proposed.
- **Design-fork OQ (item 5): captured.** The leaf-vs-fold realization fork is recorded as cross-CYCLE OQ `scal-leaf-vs-linear-combination-fold-realization-fork` (status open; trigger: batch-12 meta-phase fork verdict) in both theme §Status blocks and the report §Open-questions, with the conditional re-anchoring consequence spelled out for each theme.
- **Fence parity (item 6): clean.** 6 balanced fenced blocks, even marker parity, both firm bodies enclose `## Status` inside the fence, no nested triple-backtick fences (4-space indented code used for form blocks).

---
repaired_at: 2026-06-01T054740Z
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

## Repair

### Fixes attempted

All 8 critic checks returned `pass` with no blocking issues. No repairable defects. Two critic non-blocking notes adjudicated as informational-no-defect; the directive-keyword verification the dispatch requested was performed and found correct (no fix needed).

- **Finding**: (Non-issue, anti-repair flag) `vector.cpp:207-211` cites the `si == 0.0` two-real-call promotion branch correctly; a mechanical `citecheck --anchor 'imag'` reports a spurious `[DRIFT -1]` to line 206 because `s.imag()` is *read* one line above the cited branch body.
  - **Decision**: not-needed (informational; explicit anti-repair).
  - **Action**: None. Confirmed I did NOT run any drift-sweep against this range and did NOT regress the pinpoint to :206. The critic's direct Read of `reference/palace/palace/linalg/vector.cpp:200-227` establishes the branch body `if (si == 0.0) { Real() *= sr; Imag() *= sr; }` spans 207-211 exactly. Leaving the citation as written.

- **Finding**: Forward reference `book/src/L2/scal.md` does not yet exist on disk; it is the wave-1 D3 floor entry declared to co-land at integration.
  - **Decision**: not-needed (cross-dispatch sequencing constraint, not a defect in this report).
  - **Action**: None. This is the standard co-land pattern — `L2/scal.md` lands from wave-1 D3 in the same cycle. Surfaced to the integrator as a sequencing note (below), not a repair item. The live `[scal](../L2/scal.md)` links in both themes are correct provided D3 co-lands; the integrator must apply both in the same cycle for `linkcheck2` to pass.

- **Finding (dispatch-requested verification)**: Confirm the two scal theme files use `new:` (creation), not `edit:`.
  - **Decision**: not-needed (verified correct).
  - **Action**: Inspected the proposed-changes directive fences. `book/src/L2-L1/scal-fold-specialization.md` (CYCLE.md:66) and `book/src/L3-L2/scal-body-identity.md` (CYCLE.md:281) both carry `new:` directives. The only `edit:` blocks (CYCLE.md:533, :543, :553, :558) target the two index theme-list rows and the two SUMMARY registrations — the standard insertion pattern. No keyword fix required.

### Unrepairable findings

None. No findings exceed repair authority; there were no defects to defer.

## Suggested resolution

`ready`. Integrator notes:

1. **Co-land sequencing (load-bearing for build):** apply wave-1 D3 (`book/src/L2/scal.md`) in the SAME cycle as these two themes. Both themes carry live `[scal](../L2/scal.md)` links; without the D3 floor entry on disk, `linkcheck2` fails. This is the only ordering constraint.
2. **Anti-repair preserved:** `vector.cpp:207-211` is a correct pinpoint. Do not let any automated drift-sweep regress it to :206 (the `s.imag()` read at :206 is one line above the cited branch body).
3. **Count-ownership:** the report defers all consolidated tallies (L2-L1/index §"Vocabulary cohort" firm-list, §"Working Notes" cohort-growth log) to D7 — no tally mutation is present in its proposed changes. The D3-count-ownership partition holds.
