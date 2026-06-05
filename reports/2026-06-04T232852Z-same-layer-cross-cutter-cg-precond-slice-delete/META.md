---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T234500Z
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
overall_status: ready
---

# META: verification of "L4 observation — cg_preconditioning_framework slice is reachability-GC detritus" (cycle-097 D1)

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation in the report was confirmed against the live files. The firm-home line-ranges in the §1 coverage table resolve exactly: §Record definition (79–146), §Signature (148–216), §Capability typing (218–240), §Derived-view hoisting (242–264), §Algebraic laws (266–287), §Status absorption provenance (lines 335–337, verbatim "Source-of-truth absorbed from the `cg_preconditioning_framework` slice's §L4 / §L4-v0.2 / §L4-v0.3 …"). The L0 anchors the firm chapter re-cites (`palace/linalg/ksp.hpp:30-76`, `ksp.cpp:276-293`, `:296-310`, `:25-99`, `:125-235`) are present in the firm chapter's §Record-definition table and §Evidence. The slice's three retained-unique §L4 sections cited by the report at lines 308–426 / 428–485 / 487–548 land on the real headings (`## L4 — calculus form` @308, `## L4 v0.2 …` @428, `## L4 v0.3 …` @487) — the report uses the *current* accurate slice line numbers; the stale pre-insert numbers (293/413/472) live only in the slice's own banner, which explicitly flags itself as "pre-insert / section-relative" (slice line 16). No drift in the report. No `verified_against:` YAML block in this report (not a lowering-verifier audit), so the round-trip sub-check is N/A.

**surface-or-evidence — pass.** This is not a refinement-shaped proposal (no operator/theme surface is modified) — it is an absorb-and-delete plus 7 link repoints, a slice-reduction operation. The record-definition sub-check is satisfied positively: the records the slice named (`KspParams`/`PcParams`/`OpBinding`/`Ksp`/`Pc`/`Counters`/`BaseKspSolver`) all have a definition home — the firm chapter's in-chapter §Record definition section (lines 79–146, single-consumer, with the field/stratum/meaning/L0-home table). No signature-named record is left orphaned by the deletion. The proposal's evidence is the firm-home coverage + the inbound-link inventory, both verified.

**rotation-quality — pass (not applicable to a slice-deletion / cross-cut observation).** The report asserts no algebraic/structural rotation of its own; it relocates references onto an already-firm chapter. No-op per the deletion-kind shape (the prompt confirms rotation-quality is N/A here).

**variant-axis-coverage — pass (not applicable).** No new operator with variant axes is introduced. The firm target chapter already carries the variant-axis enumeration (krylov-method / pc-type / multigrid / scalar-field / op-pc_op-coincidence, lines 289–300); the repoints route to it. Nothing to cover or scope out.

**cross-reference-integrity — pass (LOAD-BEARING, fully verified).** The grep for inbound concept-page links reproduces the report's 7-page / 8-hit inventory exactly: `constructed-operator-factory.md:34`, `solver-as-operator.md:30`, `finest-level-unwrap.md:22`, `complex-from-real-lift.md:25` and `:31`, `counter-update.md:20`, `two_operator_split.md:26`, `build-time-vs-run-time-stratification.md:33`. Every proposed-changes `OLD:` block matches the on-disk text byte-for-byte (verified each of the 8 hits in place). The repoint target `../L4/preconditioning-framework.md` resolves from `concepts/` to the existing `book/src/L4/preconditioning-framework.md` (337 lines, status `firm`). The report correctly partitions the non-repointed inbound categories: `dependency-map.md` (≈22 aggregate Mermaid edges, lines 168–389 — confirmed present, correctly flagged as aggregate-map out-of-D1-scope + a dangling-node OQ), `SUMMARY.md`/`spec/index.md` (D5 single-owner), and `meta-reviews/*` + `rotation.md:136` (historical narrative, correctly left as-is). No inbound *markdown link* into the slice is left unrepointed — the linkcheck2-hard-error condition is fully covered.

**edge-label-fidelity — pass.** The deletion-safety claim (§3) carries the typed-edge framing: no `depends-on` blocking edge targets the slice. Verified independently — `grep` for any `target: …cg_preconditioning_framework` across all frontmatter edges blocks returns NONE, and the firm chapter's own `depends-on` targets are `L4/ksp_solve` + the `ksp.cpp:276-293` range (lines 7–11), not the slice. The 7 inbound concept-page mentions are all `## Used by` / `## Worked example` prose back-references (`reference`-class, free), consistent with the report's edge-classification claim. The prose discusses exactly the edge type it labels.

**plan-kind-consistency — pass.** Declared kind is a same-layer-cross-cutter *Redundancy* observation feeding a graded-stack P2 slice-deletion. Content shape matches: one redundancy finding (slice == superseded copy of the firm L4 chapter), three evidence sub-findings (firm-home coverage / inbound-link inventory / reachability-safety), a concrete proposed-changes block (7 repoints + 1 DELETE-FILE). No rough-in placeholders, no mis-classification.

**skill-uptake-survey — pass (telemetry only).** The report's shape implies the `phase-1-slice-reduction-audit` skill (concept-page-grep-before-reduction). The report performs exactly that procedure (the inbound grep in §2, the firm-home verification in §1) but does not name the skill by slug. Non-blocking surface note: the slice-reduction-audit procedure was executed in substance; an explicit skill citation would improve traceability but is not required.

### Issues found

No blocking or warning-level issues. Two non-blocking notes (informational, already correctly handled by the report — recorded for the integrator, NOT findings to repair):

1. **(info) Slice-internal line numbers vs slice banner.** The report cites the retained §L4 sections at 308–426 / 428–485 / 487–548 (current/accurate); the slice's *own* banner (slice lines 9–11) names 293–412 / 413–471 / 472–533 (pre-insert, banner-acknowledged as section-relative). No action needed — the report uses the correct numbers and the discrepancy is internal to the slice being deleted.

2. **(info) Two cross-cutting OQs surfaced by the report are correctly out-of-scope.** The dangling `dependency-map.md` Mermaid edges (§2) and the already-closed `l4-preconditioning-framework-promotion` OQ (§1) are flagged for follow-up, not parked — consistent with intake-channel discipline. The dependency-map node-label dangle is correctly judged a non-`linkcheck2`-hard-error (a Mermaid node label, not a markdown link), so it does not block the deletion. These route to the next cycle-planner / dependency-map maintainer, as the report states.

All 8 checks pass; the firm-home coverage is real and verified against the firm chapter, every inbound markdown link is repointed with an exact `OLD:` match to a resolving target, and the deletion is reachability-safe (no `depends-on` blocking edge anywhere). `overall_status: ready` (clean all-pass report; no repairer runs).
