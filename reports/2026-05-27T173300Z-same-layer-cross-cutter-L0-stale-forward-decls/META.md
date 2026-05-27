---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T18:30:00Z
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

# META: verification of "L0 observation — 5 stale forward-declaration italic notes"

## Critique

### Checks run

**citation-validity** — pass. Spot-checked every cited line in the 5 L0 chapters: each italic note exists at the claimed line (`output-arg-vs-receiver.md:36`, `mfem-vector-types.md:42`, `linalg-free-functions.md:47`, `transparent-vs-load-bearing-tricks.md:34`, `apply-linop-overload-set.md:55`). The cited L1 back-reference targets at `:7` all match — confirmed for `axpy.md`, `axpby.md`, `axpbypcz.md`, `scal.md`, `dot.md`, `nrm2.md`, `apply_linop.md`, and `ksp_solve.md`. The new `L1/ksp_solve` back-reference claim is well-grounded: `ksp_solve.md:7` cites `L0/apply-linop-overload-set` in the Context paragraph and `ksp_solve.md:137` cites it again in the Evidence section, exactly as the dispatch claims. The 5th change's pre-existing 6-bullet list at `apply-linop-overload-set.md:57-62` matches the reproduced text in Change 5 verbatim. The cycle-007 sweep report citation (`reports/2026-05-27T160553Z-layer-intro-author-L1-context-thinning-sweep/CYCLE.md:244`) resolves to the cross-reference coverage matrix as described.

**surface-or-evidence** — pass. This is a housekeeping dispatch removing stale italic prophecy notes; 4 of 5 edits are pure deletions of obsolete annotations, and the 5th adds a single backlink bullet that documents an already-wired cross-reference (`L1/ksp_solve.md` already cites `L0/apply-linop-overload-set` at two locations, but the bullet list in the L0 chapter omits it). No new claims or content beyond making the L0 chapters' `Referenced from` blocks accurate. Not refinement-shaped — no rotation or proposal beyond cleanup.

**rotation-quality** — pass (not applicable to housekeeping dispatch). No algebraic, structural, or reduction rotation is asserted; the dispatch is observation-kind "redundancy (degenerate)" and proposes only deletion + one missed-backlink bullet. The cross-cutter role spec accommodates this shape.

**variant-axis-coverage** — pass. The dispatch enumerates all 5 stale italic notes and accounts for the asymmetry between the 4 "convention" chapters (identical italic text) and the 1 "overload-set" chapter (variant italic text + missing-bullet remediation). The exhaustiveness is verified against the cycle-007 sweep's L0-reference list at line 240 of the sweep report (8 L0 chapters total; 2 KSP-internal chapters `ksp-factory-file` and `kspsolver-base-class` correctly excluded because they have no analogous forward-decl notes — they were authored after the cycle-006 sweep was planned).

**cross-reference-integrity** — pass. I independently grepped `book/src/L1/*.md` for each of the 5 L0 chapter slugs and the back-reference matrix in the dispatch matches reality exactly: `output-arg-vs-receiver` ← 5 L1 ops, `mfem-vector-types` ← 7, `linalg-free-functions` ← 6 (no `apply_linop`, deliberate per cycle-007 OQ #4), `transparent-vs-load-bearing-tricks` ← 7, `apply-linop-overload-set` ← 2 (`apply_linop` and `ksp_solve`). The deliberate `apply_linop` omission from `linalg-free-functions` matches the cycle-007 sweep matrix at line 251. The new bullet's link target `../L1/ksp_solve.md` resolves (file exists; matches the chapter authored in cycle-006).

**edge-label-fidelity** — pass (not applicable). This is a same-layer observation (L0 housekeeping), not a lowering-edge proposal. No edge label is asserted.

**plan-kind-consistency** — pass. The same-layer-cross-cutter role spec normally constrains to "one observation per invocation," but the cycle-008 planner (`reports/2026-05-27T180000Z-cycle-planner-cycle-008/CYCLE.md:25`) explicitly authorized this as bundlable: "Bundlable into one short dispatch. Housekeeping." The 5 edits are all the same observation kind (redundancy / degenerate stale-prophecy) over a closed cohort, not 5 distinct cross-cuts. The bundling is therefore planner-sanctioned and consistent with the dispatch's frontmatter scope description. Frontmatter `status: pending` is correct (pre-integration).

**skill-uptake-survey** — pass. The dispatch implicitly applies the `verify-citation-range` skill discipline (every cited line was independently checkable and resolved). No mandatory skill is missing: `classify-variant-axis` would be misapplied here (housekeeping, not new operator/theme); `plan-sideways-concept-emission` not relevant (no new concepts proposed). The dispatch explicitly defers a candidate "Referenced from status convention" with reasonable rationale (5-instance pattern; wait for recurrence before promoting to skill-candidate). Observation-only telemetry; no blocking issue.

### Issues found

None blocking. Two minor observations recorded for transparency:

1. **Minor — line-range expressions in Supporting evidence are slightly broader than strictly needed** (`book/src/L0/output-arg-vs-receiver.md:34-42` covers the heading + italic + 5 bullets; the dispatch only modifies lines 35-36 conceptually). Severity: trivial. The wider range still resolves and supports the claim. Not a citation error — citation framing convention preference only.

2. **Minor — the "Open questions / caveats" item asserting mdBook will rebuild cleanly is unverified** (Open Questions section, item 4). This is a prediction, not a load-bearing claim — the integrator-finalize phase will run `cargo make book` and surface any breakage. The link target `../L1/ksp_solve.md` does exist (verified), so the prediction is well-grounded; flagging only because the dispatch states it as fact rather than expectation. Severity: trivial.

The "Referenced from status convention" deferral judgment (Recommendation paragraph 2; Open Questions item 3) is reasonable. Five instances of the same staleness pattern is enough to notice but not enough to mechanize — the cost of a convention (template change across every L0 chapter authored going forward) is currently larger than the cost of the manual cleanup. The dispatch's "wait for cycle-009+ recurrence" trigger is well-calibrated; no skill-candidate filing warranted.
