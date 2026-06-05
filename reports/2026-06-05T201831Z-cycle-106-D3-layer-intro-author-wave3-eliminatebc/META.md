---
verifies: ./CYCLE.md
critiqued_at: 2026-06-05T21:42:00Z
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

# META: verification of L4/eliminate_bc WAVE-3 typed-edge migration + DofSet record-page prose retarget

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck --scan` on the report (`4 ok, 0 failing`: bounds + path hygiene clean on all reference-resolved cites). Anchor-checked the two load-bearing prose pinpoints in Edit 2's retargeted §Record-definition: `palace/linalg/rap.cpp:45-46 --anchor dbc_tdof_list` → `[ok]` (anchor at line 45). The second pinpoint, `palace/fem/multigrid.hpp:99-100`, initially `[NOANC]` for `SetEssentialTrueDofs` — but that was a wrong anchor guess on my part: the prose claims the dof list is "**built by `essential_dofs`**" there, not that `SetEssentialTrueDofs` literally appears. On-disk `Read` of `multigrid.hpp:99-100` shows `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` — the exact materialization site; `--anchor GetEssentialTrueDofs` → `[ok]` at line 99. The citation is faithful. (Per the batch-33 sharpening, the "correct" reading came from `citecheck --anchor` + on-disk `Read`, never `read_range`.) Both Edit-2 prose pinpoints are in the *unchanged tail* carried verbatim from `[old]` to `[new]`, so they are pre-existing and sound. No `verified_against:` block in this report (n/a sub-check).

**surface-or-evidence — pass.** This report makes no new operator algebra (`eliminate_bc` is already `firm`); it is a pure frontmatter typed-edge migration + a coupled stale-prose retarget. The record-definition sub-check is the load-bearing one here: the chapter signature names `DofSet[N]` and `DiagPolicy`. `DofSet[N]` has a definition home — the migration ADDS the `uses-record depends-on → concepts/dofset` edge AND Edit 2 retargets the §Record-definition prose onto the existing `book/src/concepts/dofset.md` (verified `rank: firm`, `kind: record`, carries the cited `indices : Set<TrueDofIndex>` field + L0 backing). `DiagPolicy` is single-use-shaped (named by both verbs only in this chapter) and is defined inline as the two-valued `DIAG_ONE | DIAG_ZERO` enum — a correct in-chapter home for the single-consumer case. No record described only by use.

**rotation-quality — pass (not applicable to this report-kind).** No algebraic/structural/reduction rotation is asserted by this dispatch. The substantive L4>L3 rotation lives in the linked `bc-elimination-post-composition-dissolution` theme (already firm, not authored here); this report only records the rotation *direction* in-line per high→low discipline and migrates frontmatter. No rotation to grade.

**variant-axis-coverage — pass.** The chapter carries three variant axes (`diagonal-policy`, `trial-test-coincidence`, `bc-data-homogeneity`); the migration preserves the `variant_axes:` block verbatim across the frontmatter fold (confirmed unchanged in the `[old]`→`[new]` diff). No axis is dropped or hidden by the edge-typing; the axes themselves are fully scoped in the existing chapter body (laws 3/4/7, the square/rectangular reject, the homogeneous/inhomogeneous split). No new branch introduced.

**cross-reference-integrity — pass (load-bearing for this report).** The retargeted dofset prose link `[`DofSet`](../concepts/dofset.md)` resolves: `book/src/concepts/dofset.md` exists (case-exact: `DofSet.md` is ABSENT, `dofset.md` PRESENT — confirms the stale-prose claim that `concepts/DofSet.md` does not exist). All edge targets in the new `edges:` block resolve on disk: `L4/linear_combination`, `L1/apply_linop`, `concepts/dofset`, `L4-L3/bc-elimination-post-composition-dissolution`, `L4/fe_assemble`, `L1/essential_dofs`, `concepts/state-stratification`, `concepts/black-box-vs-accelerated-kernels`, `concepts/constructed-operators` — all OK. `eliminate_bc` and `dofset` are both wired into `SUMMARY.md` (lines 62 and 311). The proposed `edges:` YAML round-trips (`yaml.safe_load` OK; 4 depends-on, 5 reference) — build-safe frontmatter. Rank invariant holds: all four `depends-on` targets are `firm` (linear_combination, apply_linop, dissolution theme, dofset all `rank/firmness: firm`), so the `firm` entry rests only on `firm` — consistent with the report's `RANK VIOLATIONS: none`.

**edge-label-fidelity — pass.** The two flagged `reference` classifications are faithful, not edge-dropping. (1) `L4/fe_assemble → reference`: the chapter prose §Dependencies (lines 266–269) + separability law 8 (lines 215–220) establish `eliminate_bc` consumes `K` as an opaque assembled `LinearOperator[N,N]`, NOT `fe_assemble`'s term-list machinery — the dependency is on the *value*, post-composition position, so `reference` is correct (a blocking `folds` edge would be the over-claim). (2) `L1/essential_dofs → reference`: prose §Dependencies "Cross-refs (produces/operates-on, NOT dependencies)" (lines 288–292) — `essential_dofs` PRODUCES the `DofSet[N]` operand; the actual blocking dependency on that operand is captured by the separate `uses-record depends-on → concepts/dofset` edge, so routing the *producer* as `reference` is correct (it is not a construction input `eliminate_bc` blocks on). The two `depends-on` (`folds`) edges are likewise faithful: `linear_combination` is the literal RHS-side body `linear_combination [(1,b),(-1,y)]` (signature line 84), `apply_linop` is the `K·x_bc` operator action (line 83). No edge-direction or layer mislabel.

**plan-kind-consistency — pass.** Declared kind is a typed-edge migration (scheme conformance) + a coupled stale-prose fix — the content matches exactly (frontmatter fold + one prose retarget, no algebra). The faithful-path-or-finding discipline is correctly applied: routing the unreachable-dofset gap as a FINDING (`oq: bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue`) rather than forcing an unfaithful `column→eliminate_bc` edge is the correct c104-D2 discipline — installing only the genuinely-faithful second half of the path (`eliminate_bc →uses-record→ dofset`) and leaving the first half (`column →composes→ eliminate_bc`) to a producer/meta plausibility judgment. The report honestly reports `reachable from roots: 81 UNCHANGED` rather than claiming a rescue it did not earn. Dispatch write-authority respected: edit applied-then-reverted, emitted only as proposed-changes blocks (no `book/` mutation in this phase).

**skill-uptake-survey — pass (telemetry).** The report's shape (typed-edge migration under the graded-stack scheme) implies the graded-stack linter; the report invokes it (`tools/graded-stack-lint/graded_stack_lint.py --show-inbound`) and pastes verbatim pre/post output, which is the expected uptake. No missing skill reference surfaced.

### Issues found

None. All 8 checks pass.

- The single point worth recording (not an issue, a confirmation): the `multigrid.hpp:99-100` prose pinpoint anchors on `GetEssentialTrueDofs` (the materialization call), not `SetEssentialTrueDofs`; the prose claim ("built by `essential_dofs`") is faithful to what is at those lines. This pinpoint is pre-existing (carried verbatim from `[old]` into Edit 2's `[new]` tail), not introduced by this dispatch.
- The stale-prose claim is fully verified: `book/src/concepts/DofSet.md` is absent, `book/src/concepts/dofset.md` is present at `rank: firm` with the cited `indices : Set<TrueDofIndex>` field — so the retarget corrects a real dangling reference and drops a now-satisfied `record-DofSet-needs-definition-home` flag (the obligation is genuinely met).
