# cycle-037

**2026-05-31** — 3 reports applied clean — thirty-second consecutive cycle under split integrator — **FIRST PRIMARY CYCLE OF META-BATCH-11** (3:1 cadence; cycles 037/038/039; **the batch-11 meta-phase fires AFTER cycle-039 finalize, NOT this cycle**; cycle counter does NOT reset across batch boundaries) — **FIRST OPUS-PLANNER CYCLE** (all agents set to Opus 4.8, user directive 2026-05-31, commit `d3ee5dc`; the cycle-planner haiku→opus escalation surfaced as a batch-10 meta-phase ASK is now enacted as part of the blanket upgrade) — NO crash this cycle.

## Summary

Substantive frontier-broadening cycle: **2 firm L3 identity-in-form backfills** closing the **diagonal-preconditioner-apply chain at L3** + **1 additive `verified_against:` audit**. 3 of 3 dispatched-ready reports applied clean (3/3 staging rows == dispatched-ready — the cycle-018 staging-completeness gap did NOT recur for the **EIGHTEENTH** consecutive cycle); zero deferrals, zero rejections, zero build-repairs.

## Headlines

- **HEADLINE 1 — L3 firm 9 → 11 (+2), the diagonal-preconditioner-apply chain at L3.**
  - `book/src/L3/assemble-diagonal.md` NEW firm L3 entry (**10th firm L3 operator**) — the operator-to-data `A -> diag(A)` introspection primitive; **square** `N×N` precondition; sibling of `apply_linop` on the operator-to-data side (opaque-operator gate). Identity-in-form backfill per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**; enacts the **first** of the six **(A)** firm candidates of the cycle-036 D2 L3-cohort-growth audit verdict at `book/src/L3/index.md:39` ("structurally identical to the firm `apply_linop` opaque-operator-gate precedent"). The exact-vs-approximate caveat is absorbed as a representation-aware L1>L0 non-law. Substantive rotation is the L1>L0 `assemble-diagonal-mutation-rotation`. SUMMARY-registered (inserted between `apply_linop` and `axpy`) + L3-index dep-map row added; citecheck `--scan` clean (15 ok / 0 failing).
  - `book/src/L3/jacobi-smoother.md` NEW firm L3 entry (**11th firm L3 operator**) — the **thinnest** constructed-operator gate; apply is one whole-tensor elementwise product `op.dinv ⊙ x = (ω·D⁻¹) ⊙ x` — no operator-apply, no reduction, no sweep, no convergence test, **NO obstruction** at L3 (the sharpest contrast with the `ksp_solve`/`eigsolve` outer-loop obstructions and `chebyshev`/`eigsolve` `partial-obstruction`s). The **sixth and final (A)** firm candidate of the same c036 D2 audit verdict. Identity-in-form backfill per the same invariant; the substantive rotation is the L1>L0 leaf-mutation `elementwise_product → forall_switch` captured by `reciprocal-elementwise-product-mutation-rotation` sub-pattern B + `jacobi-smoother-mutation-rotation`. SUMMARY-registered (inserted between `scal` and `chebyshev`) + L3-index dep-map row added; citecheck `--scan` clean (15 ok / 0 failing).
- **HEADLINE 2 — `verified_against:` audit on the firm L1>L0 reciprocal/elementwise-product theme.**
  - `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` received a **19-row `verified_against:` YAML block** appended at end-of-file (all `supports`; top-level verdict fully-supported; NO body edits — the theme stays `firm`). Adds the machine-readable lowering-verifier channel-format audit record that was missing on disk (`grep -c '^verified_against:'` → 0 before, → 1 after) alongside the pre-existing prose `## Verified-against` section (complementary, not duplicative). The audit re-confirms (second independent confirmation) the 3 pre-existing c034 D1 dead-code-status OQs without duplicating them.
- **HEADLINE 3 (PROCESS) — `cycle-planner-stale-priorities-line-recruitment` did NOT recur (first clean planner cycle post-escalation).**
  - The escalating planner-staleness friction (recurrence 1/2/3 across batch-10 cycles 034/035/036) did **not** recur this cycle. The opus cycle-planner ran the deeper deliverable-presence check and **all 3 dispatches were genuinely-open frontier work** (2 missing L3 files + 1 missing `verified_against:` block on disk). This is the **first clean planner cycle since the haiku→opus escalation** (enacted as part of the user 2026-05-31 blanket Opus-4.8 model upgrade). The batch-11 meta-phase (post-cycle-039) will confirm whether the escalation closed the friction structurally — one clean cycle is encouraging but needs a 2-of-3 batch-11 confirmation before the friction is marked addressed.

## Gate results (aggregated across 3 staging rows)

- retroactive-budget global: **0** (3 additive landings: 2 new-file identity-in-form backfills + 1 verified_against append; no surface mutation of any existing firm entry).
- staging-completeness: **3/3 rows == 3 dispatched-ready reports** — gap did NOT recur (18th consecutive cycle).
- path-hygiene / citecheck-AMBIG repair: **1** (D3 — the lowering-verifier integrator-per-report qualified 3 bare-basename `operator.cpp:NNN` note-text refs to `palace/linalg/operator.cpp:NNN` after citecheck `--scan` flagged AMBIG; the load-bearing `citation:` fields were already fully-qualified and clean; post-repair scan 42 ok / 0 failing).
- SUMMARY chapter-registration auto-fix: 0. index-placeholder displacement: 0. implied-component stub: 0. in-cycle live-link upgrade: 0. yaml-leading-quote: 0. proposed-changes fence-truncation: 0. citation-validity / cross-reference-integrity: 0.

## Build status

`cargo make book` exit 0 in ~90s. **Zero build-repairs.** The 2 NEW L3 chapters + SUMMARY entries + 2 L3-index dep-map rows + the L1>L0 verified_against append + the L3-index Working-Notes tally reconciliation are all SUMMARY-registered + link-clean + parse-clean. Only pre-existing KaTeX `Potential incomplete link` false-positives remain (`design/l4_calculus.md` + across-corpus template-in-prose warns in `krylov-step-body-identity`, the `chebyshev-iteration`/`sequential-obstruction` concept pages, the floquet/givens chapters, `L1/dot`, `L1/floquet-correction`) — NONE introduced by this cycle's files; linkcheck2 backend clean.

## Finalize reconciliation

- **L3-index running tally** at `book/src/L3/index.md` reconciled once for all c037 L3 landings: "9 firm + 2 `partial-obstruction`" → **"11 firm + 2 `partial-obstruction`"** (the consolidated D2-flagged count-bump superseding D1's narrower flag). A new Working-Notes bullet records the two diagonal-preconditioner-apply chain backfills.
- **roadmap.md** L3 line updated: 9 → 11 firm operators; appended the cycle-037 backfill note + the reciprocal/elementwise-product `verified_against:` audit note; flagged the 4 remaining (A) backfills (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) as the natural batch-11 L3 follow-frontier.

## Counts after cycle-037

L1 (**26 firm** / + 2 rough-in(test-coverage-bounded) + 6 rough-in(obstruction)) / L1>L0 (28 theme files = 24 firm + 2 rough-in + 1 partly-constructive + 3 obstruction) / L2 (9 firm + 1 partly-constructive + 0 stub) / L2>L1 (8 = 7 firm + 1 partly-constructive) / **L3 (11 firm +2: `assemble-diagonal` + `jacobi-smoother` / + 2 partial-obstruction)** / L4 (4 firm) / L0 (22 chapters). Concepts unchanged. Phase-1 removals stay 9/10.

## OQs

5 added (D1×3 — incl. the two firm-count-bump flags now reconciled; D2×4 net new — `jacobi-smoother-l4-no-entry-verdict-carried-by-analogy`, `l3-index-semantics-overlay-constructed-operator-gate-sub-family`, the count-bump flag, the audit-portion close). 1 partially-closed: `l3-cohort-growth-audit-c036-verdict` (assemble-diagonal + jacobi-smoother portions closed — 2 of 6 (A) firm backfills done; parent tracker carries the 4 remaining). 3 pre-existing c034 D1 OQs reconfirmed (second independent dead-code-status confirmation), unchanged.

## Next-cycle priorities

- **cycle-038 planner**: 4 remaining **(A)** firm L3 identity-in-form backfills — `reciprocal` (elementwise self-map) / `elementwise_product` (Hadamard binary) / `normalize` (fused `nrm2 + scal`) / `divfree-projector` (constructed-operator gate, like firm-L3 `ksp_solve`) — the natural batch-11 L3 follow-frontier under OQ `l3-cohort-growth-audit-c036-verdict`.
- **(B)** 3 substantive candidates (NOT quick backfills): `orthogonalize` (MGS sequential-obstruction; would be a third `partial-obstruction` row) / `chebyshev-smoother` (subsumption-check vs the firm L3 `chebyshev` row FIRST) / `apply_nonlinear_pencil` (fold into a future eigsolve-variant deepening, NOT a standalone L3 row).
- **(C) STOP-PROPOSING negative list** (7 operators disqualified by small-dense coordinate-space axis): `lu_solve` / `back_solve` / `ls-update-column` / the 4 NLEPS atoms. Any future planner proposal for these is STALE and should be rejected.
- **batch-11 meta-phase (post-cycle-039)**: confirm whether the opus-planner escalation closed `cycle-planner-stale-priorities-line-recruitment` (c037 = first clean planner cycle post-escalation; needs 2-of-3 batch-11 confirmation).

Written by `integrator-finalize` (split integrator-per-report×3 + finalize×1).
