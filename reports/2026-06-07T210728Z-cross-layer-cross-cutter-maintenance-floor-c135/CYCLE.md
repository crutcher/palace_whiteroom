---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-07T210728Z
scope: L-stack maintenance-floor standing hygiene + batch-43-meta tee-up — c135 (batch-43 BATCH-CLOSING)
status: pending
integrated_at: 2026-06-07T220000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean by integrator-per-report (staging row `maintenance-floor-c135`, status applied). Audit-class clean-bill report — NO book mutation (carries no `## Proposed changes`); touched only scaffolding/open-questions.md (append-only) promoting 4 batch-43-meta TEE-UP findings. Graded-stack disposition HELD EXACTLY vs c134 (`files=386, typed=325, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, promotion_frontier=11, detritus=123, true_detritus=51, roadmap_goal-bucket=4`). All per-report safety-net gates no-op (no proposed-changes). The 4 tee-ups (formal RE-disposition for the new node, exception-ledger re-baseline, DIRECTIVE-1 confirmation, hygiene-sweep cadence) are META-OWNED and carried verbatim into the batch-43 meta-phase tee-up.
---

# CYCLE: Cross-layer observation — maintenance-floor c135 clean-bill + batch-43-meta tee-up

## Summary

Standing maintenance-floor hygiene audit for c135 (batch-43 BATCH-CLOSING), run against the NEW c134 re-baselined disposition. **Clean-bill: the disposition HELDS EXACTLY, all hard invariants intact, no stale-token drift, DIRECTIVE-1 boundary held across the whole batch.** The graded-stack lint reports `files=386, typed=325, reachable=163, reference_reachable=247, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51, roadmap_goal-bucket=4` — identical to the c134 finalize-enacted re-baseline (c135 D1 was hygiene-only; no new node landed). The three `realizes-kernel-api` edges stay `reference`-class; the semantic surface has no stale path/anchor drift; the new `L4/sharding-decompose-reduce` node is the EXPECTED single detritus climb — a rank-0 roadmap_goal reference-**emitting** leaf (`reference`-edges-only out to firm roots, referenced by nothing, so filed in `true_detritus` / `no_typed_edges`; NOT a member of the reference-reached RE11 §2g cohort), with MPI cited-but-not-lifted — NOT an unexplained detritus climb. This report TEES UP — does not enact — the batch-43 meta-phase's three ownership items (the new node's formal RE-disposition, the exception-ledger re-baseline, the DIRECTIVE-1 confirmation).

## Observation kind

**Audit residue** (standing-hygiene clean-bill) + a batch-closing tee-up of meta-owned dispositions. No coverage gap, edge-label mismatch, consistency drift, or vocabulary mismatch surfaced.

## Specific finding

### (i) RE-set re-check — PASS

- **Lint disposition HELD exactly.** `python3 tools/graded-stack-lint/graded_stack_lint.py --json` reports `files=386, typed=325, untyped=61, roots=45, rank_violations=0, unresolved_depends_on_targets=0, promotion_frontier=11, reachable=163, reference_reachable=247, detritus=123, true_detritus=51`, rank-histogram `roadmap_goal=4`. This matches the c134 finalize-enacted re-baseline byte-for-byte (`log/cycle-134.md:17`). c135 D1 was hygiene-only — no new chapter, so the totals are stable c134→c135.
- **RE4 stays consumer-gated** — premise holds. No GMRES-variant feature column landed in c135 (no `feature/*gmres*` / GMRES-restart column exists on disk); the RE4 promotion condition (a named GMRES-variant consumer) remains unfired. Stays deferred.
- **RE11 §2g escalate-guard — does NOT fire; the +1 detritus is fully accounted.** The detritus climb 122 (c133) → 123 (c134, held at c135) is exactly the new `L4/sharding-decompose-reduce` node: a rank-0 `roadmap_goal` that **emits `reference`-class edges to the firm roots but is referenced BY nothing** — a reference-**emitting** leaf. The linter therefore files it in `true_detritus` (51) and `detritus_no_typed_edges_pre_p1_artifact` (104) under the hard (depends-on) GC sweep; it is **NOT** a member of the `detritus_reference_reachable_re11_cohort=72`, which counts nodes reference-**reached** FROM the roots (inbound reference paths), not reference-emitting leaves. The escalate-guard nonetheless correctly does not fire: the +1 climb is fully accounted as exactly this single new node (cross-confirmed at `log/cycle-134.md:17`), and the hard invariants held (`rank_violations=0`, `unresolved=0`). The node verified on disk:
  - `book/src/L4/sharding-decompose-reduce.md:4` — `rank: roadmap_goal`
  - `:6-12` — `edges: reference:` ONLY (`L4/domain_energy_reduce`, `L4/inner_product`, `L4/linear_combination`, `L4/gram_reduce`, `L2/gram`); NO `depends-on` block (a rank-0 → firm `depends-on` would manufacture a rank violation — correctly avoided).
  - `:28-35`, `:169-171` — explicit claim-free FUTURE-DIRECTION discipline; MPI/distributed mechanics cited as the deferred mechanism (`:188-204`) but NOT lifted (DIRECTIVE-1).

### (ii) kernel-API/impl integrity — PASS

All three `realizes-kernel-api` edges stay `reference`-class (navigational, free; do NOT block, do NOT constrain rank, do NOT carry liveness):
- `book/src/L1/libceed-quadrature-kernel-impl.md:21-23` — `reference:` block, `kind: realizes-kernel-api` (libCEED element-quadrature kernel-api).
- `book/src/L3/eigsolve-impl.md:19-23` — `reference:` block, two `kind: realizes-kernel-api` edges (the L3 `eigsolve` kernel-api + the L4 cap sibling).
- `book/src/L1/multigrid-relaxation-smoother.md:24-26` — `reference:` block, `kind: realizes-kernel-api` (the kept `triangular-solve-obstruction` GS-SSOR kernel-api).

The impl nodes do NOT `depends-on` their opaque APIs; the correspondence is review-only per DIRECTIVE-3. No new linter edge-semantics required (the `kind:` label is documentation the linters ignore).

### (iii) semantic-surface liveness — PASS

`book/src/semantics/index.md` carries no stale path/anchor drift: no residual references to the pre-c116 `design/l4_calculus.md` home, `book/src/design`, `REPORT.md`, or the deleted `spec/slices` corpus (grep returns 0 matches). The cycle-116 relocation into the active semantic-management surface is clean.

### (iv) DIRECTIVE-1 boundary — HELD across the whole batch (133/134/135)

No MPI/distributed version was lifted in any batch-43 cycle:
- The batch-43 commits (`74d7357` c133 OPENER, `31b5e6b` c134 MIDDLE, c135 closing) lift only the **sharding-MATH decomposition-abstraction** as a `roadmap_goal` sketch — explicitly the MATH, not the message-passing.
- No book node carries a **blocking `depends-on`** edge onto the MPI-associated version. The grep hits for `ParOperator`/`rap.`/`communication.hpp`/`MPI_Comm`/`geodata Partition` are all (a) `reference:` CITATION targets to L0 source ranges, or (b) single-rank-read notes — none lift the distributed version into the spine.
- **The Dörfler cross-rank threshold-bisection stays DEFERRED** — `book/src/L1/dorfler_mark.md:69-79` reads the apparatus single-rank (DIRECTIVE-1), with the cross-rank reconciliation logged as a deferred distributed concern (OQ `dorfler-cross-rank-bisection-distributed-note-deferred`). Not lifted.

---

## BATCH-43-META TEE-UP (the deliverable — for the meta-phase firing after c135 finalize; NOT enacted here)

These are the meta-phase's to OWN and enact. Teed up with recommendation + rationale.

### TEE-UP 1 — formal RE-disposition of `L4/sharding-decompose-reduce` (meta owns; was deferred from c134-D2)

**The question (meta's to formally resolve):** the new node is a reference-**emitting** leaf — the linter files it in `true_detritus` (51) / `detritus_no_typed_edges_pre_p1_artifact` (104), NOT in the reference-**reached** `detritus_reference_reachable_re11_cohort=72`. So it is **NOT auto-covered** by the existing RE11 §2g disposition (which enumerates reference-reached nodes). The meta must therefore decide: should the RE11 §2g disposition be **EXTENDED to cover reference-emitting `roadmap_goal` leaves** (so this node and future gated-exploration sketches fall under one widened §2g class), OR should this be **ratified as a fresh RE (RE12)** for the reference-emitting-leaf gated-exploration case?

**Recommendation: EXTEND the RE11 §2g disposition to cover reference-emitting `roadmap_goal` leaves** (rather than minting a free-standing fresh RE with novel semantics), with this rationale:
- The node is **closely related** to the existing RE11 cohort members in INTENT: a claim-free `roadmap_goal` deliberately wired to the feature-root set via `reference`-class edges ONLY, and therefore detritus under the hard-reachability (depends-on) GC sweep by design. The DIFFERENCE the meta must reckon with is direction: the RE11 §2g cohort counts reference-**reached** nodes, whereas this node is a reference-**emitting** leaf (nothing references IT), so it lands in `true_detritus` / `no_typed_edges` instead of the §2g cohort — it is NOT mechanically a member of the 72.
- It is a **gated-exploration `roadmap_goal` landing** — the batch-43 (C) directive's authorized exploratory future-direction. RE11 §2g already exists to hold "deliberately-reference-only, not hard-reachable, escalate-guard-suppressed" nodes; widening it to also cover the reference-emitting-leaf variant keeps a single coherent disposition rather than fragmenting it.
- It carries the standard `roadmap_goal` promotion path: it joins the hard-reachable DAG (and leaves the detritus bucket) IF/WHEN a real `depends-on` consumer pulls it to a non-zero rank — the same promotion trigger the RE11 cohort members carry. No distinct promotion semantics warrant a distinct RE.
- **Caveat for the meta:** if the meta prefers per-front RE granularity for tracking the (C)-gate exploration distinctly, a fresh RE12 (reference-emitting-leaf gated-exploration class, pointing back to the RE11 mechanism) is acceptable — but the underlying disposition is the same escalate-guard-suppressed roadmap_goal behavior, and the recommendation is to widen §2g rather than fragment. Either way the meta's RE-disposition should be made against the linter's ACTUAL bucketing (`true_detritus` / `no_typed_edges`), NOT against an assumed membership in the reference-reached 72-cohort.

### TEE-UP 2 — re-baseline the exception ledger to the c134 disposition (meta owns the ledger edit)

**Finding for the meta:** `scaffolding/graded-stack-baseline-exceptions.md` is currently the **CLOSED c094→c096 burn-down record** — it carries NO live disposition-snapshot line (no `files=` token; grep returns 0). The authoritative post-landing re-baseline was already **finalize-ENACTED at c134** and lives in `log/cycle-134.md:17` (the `files=385` → `files=386` supersession is recorded there, NOT in the exceptions ledger).

**Recommendation:** the meta should record/affirm the authoritative live disposition as **`files=386, typed=325, reachable=163, reference_reachable=247, rank_violations=0, unresolved=0, promotion_frontier=11, detritus=123, true_detritus=51, roadmap_goal-bucket=4`** (the c133 `files=385` snapshot SUPERSEDED). Because the closed ledger holds no snapshot line, the meta's choice is between (a) leaving the live snapshot in the integrator-signals / cycle-record + log trail (current arrangement; the ledger stays a closed historical record) and (b) re-opening the ledger with a fresh live-disposition banner for the batch-43 sharding-MATH exploration. **Recommend (a)** — the burn-down ledger correctly reads as a closed historical record with 0 tracked open exceptions; the live disposition belongs in the per-cycle signal trail, and the new node is a `roadmap_goal` (not a rank-violation exception), so it does not belong in a rank-violation exception ledger at all. If the meta wants a durable home for the sharding-MATH exploration provenance, the node's own `pulled_by` + `## Accreting working context` already carry it (`L4/sharding-decompose-reduce.md:21-23,185-214`).

### TEE-UP 3 — DIRECTIVE-1 boundary held (meta confirmation)

**Confirmed for the meta:** DIRECTIVE-1 (MPI/sharding = deferred future direction, NOT active work) HELD across the entire batch-43 (cycles 133/134/135). No MPI-associated version lifted; the sharding-MATH landed as a non-destabilizing `roadmap_goal` reference-only node; the Dörfler cross-rank bisection stays deferred. The hard non-destabilization gate (c133 WAVE-1 probe, both arms CLEAR) was respected through to batch close. The meta can ratify the (C)-gate exploration as having stayed within the DIRECTIVE-1 / spine-non-destabilization envelope.

### TEE-UP 4 — methodology observation: every-cycle full-hygiene audit weight vs steady-state need

**Observation worth the meta's attention.** The maintenance-floor full-hygiene audit (lint run + kernel-edge integrity + semantic-surface drift + DIRECTIVE-1 boundary + RE-set re-check) has now run as a dedicated dispatch every cycle of batch-43, and across that batch it returned a clean-bill every time — with the ONLY delta being the single expected c134 sharding-node landing (forecast and confirmed). The hard invariants (`rank_violations=0`, `unresolved=0`) have held `c123..c135`. **The signal:** with the in-scope spine L4-COMPLETE (batch-42) and the forward frontier now a gated exploratory direction, the full per-cycle hygiene sweep may be **heavier than a steady-state artifact needs**. Recommendation for the meta to weigh: consider moving the full-hygiene sweep to a **per-batch (meta-cadence) cadence** with a **lightweight per-cycle tripwire** (just the two hard invariants `rank_violations`/`unresolved` + the detritus-count escalate-guard from the lint `--json`, which is one command) as the every-cycle floor. This is a methodology-weight observation, not a defect — the audit IS valuable; the question is its cadence now that the artifact is in maintenance. (Note this composes with the batch-43 §CENTRAL-ASK posture: as the (C) sharding-MATH gate is exploratory-only, the steady-state floor is the dominant ongoing cost.)

---

## Recommendation

**Defer to the batch-43 meta-phase** — all four tee-up items are meta-owned by partition (formal RE-disposition, exception-ledger policy, DIRECTIVE-1 ratification, methodology-cadence). This dispatch is audit-class clean-bill; no follow-up specialized dispatch is warranted. No `book/` mutation needed (no stale token surfaced).

## Supporting evidence

- `tools/graded-stack-lint/graded_stack_lint.py --json` — c135 disposition (matches c134 re-baseline).
- `book/src/L4/sharding-decompose-reduce.md:4-12,28-35,169-171,185-214` — the new node: `rank: roadmap_goal`, `reference`-edges-only, MPI cited-not-lifted.
- `book/src/L1/libceed-quadrature-kernel-impl.md:21-23`, `book/src/L3/eigsolve-impl.md:19-23`, `book/src/L1/multigrid-relaxation-smoother.md:24-26` — three `realizes-kernel-api` `reference`-class edges.
- `book/src/semantics/index.md` — no stale path/anchor drift (grep clean).
- `book/src/L1/dorfler_mark.md:69-79` — Dörfler cross-rank bisection deferred (DIRECTIVE-1, OQ `dorfler-cross-rank-bisection-distributed-note-deferred`).
- `log/cycle-134.md:17` — the authoritative c134-enacted re-baseline (`files=385`→`386` supersession).
- `scaffolding/graded-stack-baseline-exceptions.md` — closed c094→c096 burn-down record, 0 tracked open, no live disposition snapshot line.

## Open questions / caveats

- TEE-UP 1's recommendation (EXTEND RE11 §2g to cover reference-emitting `roadmap_goal` leaves rather than mint a fresh RE) is the cross-cutter's read; the formal ratification is the meta's authority. The node is NOT auto-covered by the existing RE11 §2g reference-reached cohort (72) — the linter files it in `true_detritus` / `no_typed_edges` as a reference-emitting leaf — so the meta must make an explicit disposition (widen §2g, or mint RE12); the existing cohort does not silently absorb it.
- TEE-UP 2 recommends leaving the exceptions ledger as a closed historical record (the live disposition lives in the signal trail); if the meta prefers a durable ledger home for the sharding-MATH exploration provenance, the node's own `pulled_by` / accreting-context already carry it.
- TEE-UP 4 is a cadence observation, not a defect — the every-cycle full sweep returned clean all batch; the meta weighs whether a per-batch sweep + per-cycle two-invariant tripwire is the right steady-state floor.
