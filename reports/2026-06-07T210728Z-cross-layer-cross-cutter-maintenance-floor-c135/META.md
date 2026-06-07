---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T21:16:19Z
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
repaired_at: 2026-06-07T21:24:00Z
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

# META: verification of cross-layer maintenance-floor c135 clean-bill + batch-43-meta tee-up

## Critique

This is an **audit-class maintenance-floor report** — a standing-hygiene clean-bill with NO `book/` mutation and a batch-43-meta tee-up findings section. It proposes no new operator/theme/lowering surface, asserts no new algebraic claim, and carries no proposed-changes block. Per the critic role-spec, the producer-content-shape checks (surface-or-evidence, rotation-quality, variant-axis-coverage, edge-label-fidelity, plan-kind-consistency) no-op for this shape; the load-bearing checks are citation-validity (does the reported linter disposition + each cited line hold) and cross-reference-integrity (do the cited nodes/edges resolve on disk). Both graded-stack additions (rank-invariant, reachability) are likewise audit-class: the report's whole job IS to confirm them, and they were independently re-verified below.

### Checks run

**citation-validity — warning.** The headline linter disposition holds **exactly**. Re-running `python3 tools/graded-stack-lint/graded_stack_lint.py --json` reproduces `files=386, typed=325, untyped=61, roots=45, reachable=163, reference_reachable=247, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51` and `rank_histogram.roadmap_goal=4` — byte-for-byte the report's numbers and the `log/cycle-134.md:17` re-baseline (cited; the `files=385`→`386` supersession line is present at that location). The `detritus_reference_reachable_re11_cohort=72` figure is also reproduced. Every other cited line resolves and supports its claim: `book/src/L4/sharding-decompose-reduce.md:4` (`rank: roadmap_goal`), `:6-12` (`reference:`-only edges, no `depends-on` block), `:28-35` / `:169-171` / `:185-214` (claim-free FUTURE-DIRECTION discipline; MPI mechanics cited-but-NOT-lifted); `book/src/L1/dorfler_mark.md:69-79` (single-rank reading, OQ `dorfler-cross-rank-bisection-distributed-note-deferred`); the semantic-surface drift grep on `book/src/semantics/index.md` returns 0 matches (clean — no `design/l4_calculus` / `book/src/design` / `REPORT.md` / `spec/slices` residue). The **one imprecision** that lowers this to `warning` (see Issue 1): the report characterizes the new sharding node as sitting in "the EXPECTED RE11-§2g deliberate-reference-only-reachable landing class" and states `detritus_reference_reachable_re11_cohort=72` "accounts for the cohort" — but the linter actually files the node in `true_detritus` (51) and `detritus_no_typed_edges_pre_p1_artifact` (104), and does NOT place it in the 72-member reference-reachable cohort. The substantive conclusions the report draws from this framing (the +1 climb is fully accounted; the escalate-guard does not fire) are nonetheless **independently correct** — the climb IS the single new node, confirmed against `log/cycle-134.md:17`, and `rank_violations=0`/`unresolved=0` held — so this is a label/bucketing imprecision, not a false conclusion.

**surface-or-evidence — pass.** Not applicable to the audit/observation kind: the report proposes no surface modification and makes no rotation_claim. It is a clean-bill audit residue with a meta tee-up; no record is named-in-signature requiring a definition home. No-op.

**rotation-quality — pass.** Not applicable to the audit-class report: no algebraic/structural/reduction rotation is asserted. The sharding node it *audits* is a rank-0 roadmap_goal claim-free sketch (which itself makes no rotation claim). No-op.

**variant-axis-coverage — pass.** Not applicable: no operator/theme with variant axes is proposed. No-op.

**cross-reference-integrity — pass.** All cited nodes resolve on disk. The three `realizes-kernel-api` edges are confirmed `reference`-class: `book/src/L1/libceed-quadrature-kernel-impl.md` (`reference:` block, `kind: realizes-kernel-api` → `L1-L0/fe-assemble-libceed-boundary-obstruction`), `book/src/L3/eigsolve-impl.md` (`reference:` block, two `kind: realizes-kernel-api` edges → `L3/eigsolve` + `L4/eigsolve`), `book/src/L1/multigrid-relaxation-smoother.md` (`reference:` block, `kind: realizes-kernel-api` → `L1-L0/triangular-solve-obstruction`). None sit in a `depends-on` block; the linter's `unresolved_depends_on_targets=0` confirms no dangling edges. The sharding node's `reference:` edges all resolve (the linter records it as an inbound reference source to `L2/gram` and its other four firm targets).

**edge-label-fidelity — pass.** Not applicable: the report carries no L_{n+1}→L_n edge label whose prose direction could mismatch. The kernel-API edges it audits are `realizes-kernel-api` correspondences (review-only, direction-agnostic), and the prose discusses exactly those. No-op.

**plan-kind-consistency — pass.** The declared kind (audit-class maintenance-floor clean-bill + batch-43-meta tee-up) matches the content shape exactly: standing-hygiene re-checks (lint disposition, kernel-edge integrity, semantic-surface liveness, DIRECTIVE-1 boundary) followed by four explicitly meta-owned, NOT-enacted tee-up items. The "Recommendation" section correctly defers all four to the meta-phase by write-authority partition — no enactment leaks into this audit dispatch. Consistent.

**skill-uptake-survey — pass.** The report's shape (mechanical lint-disposition re-check + on-disk edge verification) is precisely what the audit performs in-line; it correctly invokes `graded_stack_lint.py --json` as the authoritative disposition source. No unreferenced skill is implied by the shape. Telemetry-only; no blocking.

**rank-invariant (graded-stack add'l) — pass.** Re-verified mechanically: `rank_violations=0`. The new sharding node is `rank: roadmap_goal` (rank 0) with NO `depends-on` block — it `reference`s firm (rank-3) roots, which constrains nothing (a rank-0 node may reference any rank freely; a `depends-on` from rank-0→rank-3 would manufacture a violation and is correctly avoided). The report's reasoning on this point is sound.

**reachability (graded-stack add'l) — pass.** Re-verified: the node is a claim-free `roadmap_goal`, so the citation/surface/rotation checks no-op per the rank-0 carve-out; it carries the banner + intent + `pulled_by` + reference-edge wiring and is on disk under `book/src/L4/`. The DIRECTIVE-1 boundary (no MPI-associated version lifted across batch-43) was independently confirmed: the MPI tokens in book files are all `reference`-class L0 citations / single-rank-read notes, none a blocking `depends-on` onto an MPI node; `unresolved_depends_on_targets=0` and no new MPI chapter landed.

### Issues found

**Issue 1 — RE11-§2g cohort mis-attribution for the sharding node (CYCLE.md §Specific finding (i), "RE11 §2g escalate-guard" bullet; and §Supporting evidence). Severity: low (characterization imprecision; conclusions unaffected).** The report states the new `L4/sharding-decompose-reduce` node is "the EXPECTED RE11-§2g deliberate-reference-only-reachable landing class" and that "`detritus_reference_reachable_re11_cohort=72` accounts for the cohort." The linter actually files this node in `true_detritus` (51) and `detritus_no_typed_edges_pre_p1_artifact` (104), and it is NOT a member of the 72-node `detritus_reference_reachable_re11_cohort`. The mechanism: the RE11 §2g `reference_reachable` cohort counts nodes reachable FROM the roots via inbound reference paths; the sharding node *emits* `reference` edges to firm roots but nothing references IT, so it is a reference-emitting leaf — true_detritus under the hard (depends-on) GC sweep, not a reference-REACHED cohort member. The downstream conclusions are still correct (the detritus +1 climb 122→123 IS exactly this new node, cross-confirmed at `log/cycle-134.md:17`; the escalate-guard does not fire because `rank_violations=0`/`unresolved=0` held), so this is a bucket-label slip, not a false clean-bill. It is also directly relevant to TEE-UP 1 (the meta's formal RE-disposition): the meta should decide the node's disposition knowing the linter currently classifies it as `true_detritus` / `no_typed_edges`, NOT as an RE11-§2g `reference_reachable` cohort member — the "match to RE11 §2g" recommendation rests on a cohort the linter does not (yet) count it in. Worth surfacing so the meta's RE-disposition is made against the linter's actual bucketing.

**Issue 2 — minor: `L4/sharding-decompose-reduce` also appears in `promotion_frontier` (11). Severity: informational.** The node is listed in the lint's `promotion_frontier` (alongside the deflate/NLEPS/eigsolve-impl/lanczos cohort). The report's promotion-path prose (`:169-171`, TEE-UP 1) correctly describes the roadmap_goal→real-rank promotion trigger, so this is consistent rather than contradictory; noting it only because the report's §(i) enumeration of the disposition does not mention the node's promotion-frontier membership, which the meta may want visible when ratifying its RE-disposition.

No fail-level issues. No `book/` mutation to vet. The clean-bill's substantive conclusions (disposition held, three kernel-API edges `reference`-class, sharding node a by-design reference-only rank-0 roadmap_goal, DIRECTIVE-1 held across the batch, four tee-ups correctly meta-owned and not enacted) are all independently confirmed.

## Repair

### Fixes attempted

- **Finding (Issue 1 — citation-validity warning)**: The report characterized the new `L4/sharding-decompose-reduce` node as sitting in "the EXPECTED RE11-§2g deliberate-reference-only-reachable landing class" and cited `detritus_reference_reachable_re11_cohort=72` as "accounting for the cohort," but the linter actually files the node in `true_detritus` (51) / `detritus_no_typed_edges_pre_p1_artifact` (104) — it is a reference-**emitting** leaf (outbound `reference` edges to firm roots, referenced by nothing), NOT a member of the 72-node reference-**reached** cohort. The TEE-UP 1 "match to RE11 §2g" recommendation rested on a cohort the node is not counted in.
  - **Decision**: repaired
  - **Action**: Surgical characterization-accuracy correction in four places in `CYCLE.md` (no substantive content change):
    - §Summary — restated the node as a reference-**emitting** leaf filed in `true_detritus` / `no_typed_edges`, NOT a member of the reference-reached RE11 §2g cohort.
    - §Specific finding (i), "RE11 §2g escalate-guard" bullet — replaced the cohort-membership characterization with the correct bucketing (`true_detritus`/`no_typed_edges`; the 72-cohort counts reference-**reached** nodes, not reference-emitting leaves); preserved the (independently-correct) escalate-guard-does-not-fire conclusion via the +1-climb / hard-invariants accounting.
    - §TEE-UP 1 — reframed the question and recommendation: the node is NOT auto-covered by the existing reference-reached RE11 §2g cohort, so the meta must make an explicit disposition — EXTEND §2g to cover reference-emitting `roadmap_goal` leaves, OR mint a fresh RE12; kept it meta-owned (no RE enacted) and added the explicit instruction to make the disposition against the linter's actual bucketing.
    - §Open questions / caveats — updated the TEE-UP 1 caveat line to match.

### Unrepairable findings

None. The single warning was a mechanical bucket-LABEL slip; the substantive conclusions (clean-bill on the hard invariants, escalate-guard correctly not firing, the four meta-owned tee-ups) were already correct and are preserved. Issue 2 was informational-only (no critic action requested).

## Suggested resolution

`ready` for the integrator. The report carries no `book/` mutation (audit-class clean-bill); nothing to apply to the artifact. Note for the integrator/meta: TEE-UP 1 now correctly tees up an OPEN RE-disposition decision (extend §2g vs mint RE12) for the batch-43 meta — the node is a reference-emitting `roadmap_goal` leaf that the existing reference-reached RE11 §2g cohort does not mechanically absorb.
