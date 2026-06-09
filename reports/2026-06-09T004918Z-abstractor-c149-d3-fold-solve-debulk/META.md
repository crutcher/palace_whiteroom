---
verifies: ../CYCLE.md
critiqued_at: 2026-06-09T00:53:14Z
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

# META: verification of FINALIZATION de-bulk — fold_solve family (c149 D3)

## Critique

This is a **FINALIZATION de-bulk** report (skill `finalization-debulk`), not a content-authoring or
theme-sketch dispatch. It strips process/judgment accounting from 3 already-firm `fold_solve` chapters
and asserts five load-bearing CONSERVATION invariants (no citation lost / no rank-token lost /
load-bearing content preserved / graded-stack baseline held / 0 residue). The 8 standard critic checks
are applied to the *static finalized surface* the de-bulk produces; the conservation claims are
adjudicated mechanically against `git show HEAD:<file>` vs the working tree.

### Checks run

**citation-validity — pass.** All conservation citation claims verified mechanically. Source-token
diff (HEAD vs working) on `L4/fold_solve.md` drops EXACTLY the two claimed aggregate spans
`transientsolver.cpp:33-99` and `drivensolver.cpp:231-398` — nothing else dropped, nothing added
(unique source-cite tokens 20→18). The load-bearing sub-claim — that both dropped spans were
roll-up summaries living ONLY in the deleted `## Status` firm-promotion prose, with every constituent
pinpoint surviving — is CONFIRMED: the transient span's constituents (`:33,34,35,36,77,89,93,98,99`)
all survive in `## Evidence` (Fold witness 1) and §Algebraic-laws/§Specializations; the driven span's
constituents (`:73,231,241,242,243,244,384,389,398`) survive verbatim in `## Evidence` (Fold witness 2,
byte-identical block). No grounding source range is lost — only the two prose-narrative roll-up spans
went with the deleted promotion narrative (the skill-sanctioned KEEP outcome: pinpoints preserved,
deleted-prose summary spans are not separate grounding). `L3/fold_solve.md` and
`L3-L2/fold-solve-time-step-body.md`: 0 source tokens dropped (16/16 and 10/10 respectively). (Note:
the report's table reports 23/23 and 21/21 "unique cite-lines" — a broader occurrence count than the
unique-source-token measure I used; both measures agree that ZERO source ranges were lost, which is
the conservation invariant that matters.) No `verified_against:` block is proposed (consistent with the
de-bulk's own purpose of stripping such blocks), so the YAML round-trip sub-check no-ops.

**surface-or-evidence — pass.** This is not a refinement-shaped proposal (no new surface claim, no new
rotation_claim) — it is a finalization de-bulk of existing firm chapters, the static-state analog of
"retroactive evidence framing" (allowed). No record is newly named in a signature here; the
record-definition sub-check no-ops (the `OpParams`/`TimeState` records are referenced, not defined, and
have their existing definition homes). The de-bulk PRESERVES the evidence surface intact (verified
above) and only relocates the load-bearing Scope content from the deleted `## Status` into a new
`## Scope` section — evidence-preserving by construction.

**rotation-quality — pass (no-op for this kind).** A de-bulk asserts no algebraic/structural rotation
of its own; it re-expresses existing firm chapters as a static surface. The chapters' underlying
rotations (the L4 fold combinator, the L3 partial-obstruction iteration view, the L3>L2 sweep erasure)
are untouched. Not applicable to a finalization-de-bulk report.

**variant-axis-coverage — pass.** The `schedule-source` variant axis (`fixed-list | state-generated`;
transient / SweepAdaptive / AMR) is the load-bearing content the conservation check requires survive,
and it DOES survive in full across all 3 files (L4 frontmatter `variant_axes` intact, L4 §Variant-axes
+ §Scope, L3 §Variant-axes axis-1, L3-L2 §Scope). The genuine unsettled sub-decision (whether the
state-generated greedy form warrants its own chapter) survives as a static "is unsettled" note in all
3 files, with the batch-18/OQ-slug bookkeeping correctly stripped. No variant combination was hidden
or dropped by the de-bulk.

**cross-reference-integrity — pass.** The one retargeted cross-ref (L3 Evidence pointer to the L4 cap,
`§Status` → `§Scope`) resolves: `L4/fold_solve.md` now carries exactly one `## Scope` section (the
relocated target), and the `## Status` it previously pointed at is gone — so the retarget is necessary
and correct (a stale `§Status` ref would now dangle). All four `../L4/fold_solve.md` links in L3
resolve to the existing file. No `firm`-body-inside-fence guard applies (direct-edit de-bulk, no
proposed-changes fence). Internal `.md` link counts are conserved (10/15/10 per the report, no links
lost).

**edge-label-fidelity — pass.** No edge label is introduced or altered; the de-bulk makes no graph
mutation (the report explicitly states no SUMMARY/dep-map registration, no node/edge move). The
`depends-on`/`reference` edges in the L4 frontmatter are untouched (verified: frontmatter unchanged).
Not applicable beyond confirming no edge prose drifted.

**plan-kind-consistency — pass.** The declared kind (FINALIZATION de-bulk, direct-edit book wave) matches
the content shape exactly: in-place edits, no proposed-changes fence, no graph mutation, conservation-
asserting. The three rank/status tokens are handled per the FINALIZATION directive: `L4/fold_solve`
`rank: firm` in frontmatter ⇒ `## Status` promotion-prose correctly DELETED (firmness lives in
frontmatter); `L3/fold_solve` non-firm ⇒ `## Status` `partial-obstruction` leading token correctly
PRESERVED; `L3-L2/fold-solve-time-step-body` no-frontmatter ⇒ `## Status` `firm` leading token is the
SOLE rank carrier and was correctly NOT touched (verified: git diff shows no change to the Status token
line). All three handled correctly.

**skill-uptake-survey — pass.** The report explicitly references its driving skill (`finalization-debulk`)
and the exemplar (`L4/krylov_step.md`), and applies the skill's KEEP/STRIP/LIFT model by name (Scope
LIFT, pinpoint-KEEP, process-STRIP). Skill uptake is surfaced.

### Conservation results (load-bearing, mechanically verified)

- **No citation lost — CONFIRMED.** L3: 16/16 source tokens, 0 dropped. L3-L2: 10/10, 0 dropped. L4:
  20→18, the 2 dropped being EXACTLY `transientsolver.cpp:33-99` + `drivensolver.cpp:231-398`. Both
  spans' constituent pinpoints (transient 33/34/35/36/77/89/93/98/99; driven 73/231/241/242/243/244/
  384/389/398) survive verbatim in `## Evidence`. **No grounding source range actually lost** — the L4
  dropped-aggregate-spans claim is TRUE.
- **No rank/status token lost — CONFIRMED (all three).** L4 `rank: firm` in frontmatter (Status-prose
  deletion correct); L3 `partial-obstruction` leading token preserved; L3-L2 `firm` sole-rank-carrier
  leading token untouched.
- **Load-bearing content preserved — CONFIRMED.** "Classification decision (load-bearing): ONE
  combinator — the §3.7 carry form covers both" survives verbatim (L4:127). Full `schedule-source`
  variant axis (fixed-list/state-generated; transient/SweepAdaptive/AMR) survives across all 3 files.
  The genuine unsettled sub-decision survives as a static "is unsettled" note; first-person "I did NOT
  force…" framing and batch-18/OQ-slug bookkeeping correctly stripped.
- **Graded-stack baseline HELD EXACTLY — CONFIRMED.** Re-ran `graded_stack_lint.py`: `files=392,
  typed=331, untyped=61, rank_violations=0, detritus=123, true_detritus=51, promotion_frontier=11`,
  no unresolved-depends-on warnings. Rank histogram `firm: 224, partial-obstruction: 4` unchanged.
- **0 residue tags per file — CONFIRMED.** The full process-tag scan (`batch-N|cycle-N|cNNN|OQ |I did
  NOT|this dispatch|self-verified|verified_against|reports/|firm-on-positive|gated on the cap|deferred
  to OQ`) over all 3 files returns 0 matches (EXIT 1).

### Issues found

None. All 8 standard checks pass and all 5 load-bearing conservation invariants are mechanically
confirmed. The report's central risk claim — that the two dropped L4 aggregate spans are roll-up
summaries whose constituent pinpoints all survive in `## Evidence` (no grounding lost) — is verified
true. The frontmatter-prose caveats the report itself flags (the "now twice-witnessed" `variant_axes`
phrase left intact as static axis-documentation, and the untouched scaffolding OQ-ledger entry) are
correct dispositions per the skill's KEEP rule and the scaffolding-is-process-workshop boundary; they
are not defects. Setting `overall_status: ready` (all-pass clean report; no repairer will run).
