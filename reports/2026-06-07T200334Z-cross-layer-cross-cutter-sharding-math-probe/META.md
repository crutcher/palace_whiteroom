---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T203500Z
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

# META: verification of "Cross-layer observation — sharding-MATH non-destabilization probe (vertical / cross-layer arm)"

## Critique

### Checks run

**citation-validity — pass.** Mechanical scan clean: `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returned `23 ok, 0 failing (23 citations checked)` (bounds + path-hygiene). I then anchor-verified every load-bearing pinpoint by direct on-disk Read (NOT via codemap `read_range`, per the c105 sharpening):
- **Dörfler source** (`reference/palace/palace/utils/dorfler.cpp`, cited by the report as `palace/utils/dorfler.cpp` relative to `reference/`): `:14-171` `ComputeDorflerThreshold` (function spans exactly 14-171); `:20,28,36` single-rank pivot (line 20 `std::sort`, 28 `std::partial_sum`, 36 `std::lower_bound` — exact); `:58-63` the "if a given processor has lots of low error elements" comment (exact); `:66-67` `Mpi::GlobalMin`/`GlobalMax` (exact); `:107-108` `GlobalSum`-reduced stopping criteria (exact); `:163` tie-break `error_threshold = min_threshold` (exact); `:64-67` single-rank degeneration `min == max == error_threshold` (lines 64-65 init both to `error_threshold`, 66-67 the no-op-at-single-rank collectives — claim well-supported); `:125,127` the break/exit conditions (exact). The report's bisection-loop range `:100-158` is a one-line-early START (the `for` is 101-158; line 100 is the `constexpr int max_it = 100;` context line immediately above) — a trivial inclusive-of-preceding-context range, not a misleading drift, and the loop genuinely ends at 158. Noted, not flagged.
- **`domain_energy_reduce` precedent** (`book/src/L4/domain_energy_reduce.md`, 424 lines): `:72-85` per-domain restricted-reduce signature (the signature + `restricted_energy` where-clause, exact); `:85,153-160` composes `inner_product`/`apply`/`participation_ratio` (line 85 `inner_product field (m apply field)`; laws 2-3 at 153-160 — exact); `:147-152` the map-independence / concatenation-homomorphism fold law (law 1, exact); `:172-178` partition-of-unity = config-conditional NON-law, incl. the contrast phrase "a true partition-of-unity reduction where the sum-to-one is structural" at `:177-178` (exact). The report's rendered signature `DomainOpMap -> Field -> Scalar -> [DomainData]` matches source lines 73-76 verbatim.
- **Boundary/supporting**: `book/src/L1/dorfler_mark.md` (410 lines) `:209-214` no-reduction-order non-law (exact, and confirms the report's "multi-rank analog" framing), `:325-336` *Downward to L0* deferred-distributed-concern (exact — independently states the same math/mechanism split). `book/src/L0/par-types-single-rank-reading.md` (125 lines) `:47-56` the single-rank collective-reading rule (`GlobalSum`/`GlobalMin`/`GlobalMax`/`Broadcast`/`Allgather` → identity, exact). OQ `:1790-1793` and `:1942`, priorities `:32-33,43,47-50` all resolve to the cited content. All ranges in-bounds. No `verified_against:` block in this report (not a lowering-verifier audit), so that sub-check is N/A.

**surface-or-evidence — pass (audit-class, no surface mutation).** This is an audit/observation report proposing NO book mutation (stated explicitly at CYCLE.md §"Open questions / caveats" final bullet and §Recommendation). There is no refinement-shaped proposal to a book operator/theme, so the surface-AND-rotation-evidence requirement does not bind; the report's evidence shape is the correct one for an audit-class verdict (cited source + cited firm-precedent backing a CLEAR/NO-CLEAR disposition). Record-definition sub-check: the report NAMES records/types (`DomainOpMap`, `DomainData`, the `M_idx` restriction operator) but does so by REFERENCE to the already-firm `domain_energy_reduce` chapter (which carries / routes their definition homes — `DomainData` via OQ `record-DomainData-needs-definition-home`, `DomainOpMap` via that chapter's §Record definition). The report introduces no new signature-named record of its own, so the obligation does not attach here. Pass.

**rotation-quality — pass (N/A to audit-class).** The report asserts no algebraic/structural/reduction rotation as a proposed book edit; it AUDITS whether a (deferred, speculative) decomposition-reduce abstraction could be expressed without destabilizing the spine, and lands the disposition as a recommendation for a future `roadmap_goal`-class WAVE-2 sketch. No L_{n+1}/L_n compactness claim is being made here. Marked pass, not applicable to audit-class observation report.

**variant-axis-coverage — pass (N/A to audit-class).** No operator/theme with orthogonal variant axes is being proposed. The report does correctly surface the load-bearing precondition AXIS it inherits from the precedent — partition-vs-overlap (partition-of-unity as a config-conditional precondition, CYCLE.md §"Open questions" 3rd bullet) — and flags that the future WAVE-2 sketch must carry it honestly. That is axis-aware, not an uncovered hidden branch. Marked pass, not applicable.

**cross-reference-integrity — pass.** All cited book chapters exist on disk at the claimed paths (`book/src/L4/domain_energy_reduce.md`, `book/src/L1/dorfler_mark.md`, `book/src/L0/par-types-single-rank-reading.md`) and the named firm roots the recommendation would wire to by `reference`-class edge (`domain_energy_reduce`, `inner_product`, `linear_combination`, `gram_reduce`, `apply_linop`, `participation_ratio`) are real spine nodes. The OQ slug `dorfler-cross-rank-bisection-distributed-note-deferred` resolves to the cited OQ block. The graded-stack reasoning (rank-0 `roadmap_goal` resting on `reference`-class edges introduces no `depends-on` that could violate `rank(u) ≤ rank(v)`; reachability and `rank_violations=0` preserved by construction) is internally sound and consistent with `METHODOLOGY-GRADED-STACK.md` / `book/src/methodology/resolution-ladder.md` as cited.

**edge-label-fidelity — pass.** The report's vertical framing (Finding 3) discusses the L4→L3→L2→L1 lowering direction it claims to examine, and correctly argues a `map`-over-domain-index combinator adds at the top without inverting any existing per-primitive vertical rotation. The edge discussion matches the arm it is labelled for (the "vertical / cross-layer arm"); the lateral per-combinator-closure question is explicitly deferred to the D2 same-layer arm and not mis-claimed here.

**plan-kind-consistency — pass.** Declared kind is audit / cross-layer observation (frontmatter `agent: cross-layer-cross-cutter`, §"Observation kind" = "Coverage gap (deferred-future kind) + Audit residue"). Content shape matches: a CLEAR/NO-CLEAR verdict with cited evidence and a deferred-handoff recommendation, NO book mutation. The split verdict (NO-CLEAR for the Dörfler candidate, CLEAR for the general decomposition-reduce abstraction, contingent on D2) is internally consistent — the two halves do not contradict (one is "this specific MPI-collective candidate generalizes to nothing"; the other is "a different, already-firm precedent shows the general shape is non-destabilizing"). The HARD-GATE boundary is honored: `linalg/rap.{hpp,cpp}`, `utils/geodata.{cpp,hpp}`, `utils/communication.hpp`, and the Dörfler cross-rank bisection itself are all cited as deferred-mechanism-ONLY and explicitly marked "NOT lifted" (CYCLE.md §"HARD-GATE boundary honored and stated"), satisfying the DIRECTIVE-1 boundary the dispatch demanded.

**skill-uptake-survey — pass (telemetry).** No skill is strongly implied for an audit-class non-destabilization probe; the report leans on the codemap-confirmed planner fact and direct source re-reading, which is appropriate. The `verify-citation-range`/`citecheck` discipline is a critic-side tool, not a producer obligation here. No gap surfaced.

### Issues found

None blocking. One cosmetic, non-blocking observation (NOT a citation-validity fault):

- **(cosmetic) CYCLE.md §"Finding 1" / §"Supporting evidence": bisection-loop range cited as `dorfler.cpp:100-158`.** The `for` loop body is lines 101-158; line 100 is the `constexpr int max_it = 100;` context line directly above. This is a one-line-early inclusive-of-context start on a range bound, the loop end (158) is exact, and the claim the range supports (the bisection loop is an MPI-collective-driven scalar reconciliation) is fully borne out by the cited interior anchors (`:103` midpoint, `:107-108` `GlobalSum` stopping, `:125,127` break). Not a drift worth a warning; recorded only for completeness. Notably the report's own pinpoints here are MORE accurate than the OQ note it supersedes (OQ `:1793` carried `:67-68` for `GlobalMin`/`GlobalMax`; the report correctly cites `:66-67`).

All 8 checks pass; the report is a clean audit-class observation with verified citations, an honored HARD-GATE boundary, and an internally consistent split verdict. Setting `overall_status: ready`.
