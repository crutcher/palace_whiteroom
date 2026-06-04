---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T211945Z
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
  rank-invariant: pass
  reachability: pass
repaired_at: 2026-06-04T213000Z
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
  rank-invariant: not-needed
  reachability: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of D6 — P1 high-fan-out vocabulary-frontier edge-typing + stale-edge false-positive audit

## Critique

### Checks run

**citation-validity — warning.** Mechanical scan: `citecheck.py --scan` = 24 ok / 1 failing of 25 citations. The single failure is `graded_stack_lint.py:328-380` cited in the Finding-1 "Root cause" paragraph WITHOUT its `tools/graded-stack-lint/` path prefix (citecheck resolves against `reference/` + `book/src`, so the bare filename does not resolve). The same range is cited correctly with full path in §Supporting evidence. The line numbers themselves are correct (`derive_rank` does begin at `:328`). A second, finer issue: the `:328-380` END bound over-extends — `derive_rank` ends at `:361` (verified: `build_graph` begins at `:364`), so `:328-380` spills ~19 lines into the next function. The load-bearing claim (the priority ordering `rank: > firmness: > status: > prose`) IS within `:328-361`, so the claim is fully supported; only the range bound is loose. Both issues are tool-source-citation hygiene, not substantive — but they are real `warning`-grade citation imprecisions. Every other load-bearing pinpoint was confirmed by direct read: the linter `read_status_line:310-326` blob-scan, all 15 frontier §Status lines, the L4/index `:32`/`:58`/`:101` cells, and `solve_family.md:154`.

**surface-or-evidence — pass.** This is a pure edge-typing + rank-token migration (scheme §4(a)), explicitly framed as "NOT a promotion" — the surface change (frontmatter `rank:`/`edges:`) is backed by reading each node's own current `## Status` + `## Dependencies` on disk. Record-definition sub-check: the signatures touched (the `:101` gram_reduce cell names `Matrix[m,m]`; `domain_energy_reduce` names `DomainOpMap`) carry their definition homes already — `DomainOpMap` has an in-chapter `## Record definition` section (visible in the `:97` dep-map cell "Input record: `DomainOpMap` (defined in-chapter §Record definition)"); D6 introduces NO new record name. Pass.

**rotation-quality — pass (not applicable to the typing/audit kind).** D6 asserts no algebraic/structural rotation; it types existing edges and re-anchors stale narration. The check no-ops, analogous to the stub/feature-surface no-op.

**variant-axis-coverage — pass.** D6 PRESERVES and in several cases RE-STATES the `variant_axes:` blocks (L2/nrm2, L3/dot, L3/inner_product, L3/normalize, L4/domain_energy_reduce, L2/eigsolve) verbatim from the existing chapters. No variant axis is hidden or dropped; the typing pass adds edges around the unchanged axis blocks.

**cross-reference-integrity — pass.** The `depends-on` edges all resolve to real on-disk nodes (verified the constituent claims against each `## Dependencies` section — e.g. L1/eigsolve's `ksp_solve`+`apply_linop`, L1/normalize's `nrm2`+`scal`). The `reference:` edges include several L1>L0 / L2>L1 theme slugs (`apply-linop-mutation-rotation`, `linear-combination-fold-specialization`, etc.) whose on-disk existence D6 EXPLICITLY flags for integrator verification in §Open-questions — and per graded-stack semantics a `reference` edge constrains nothing (a missing reference target is a soft warning, not a hard `linkcheck2` break, because these are frontmatter slugs not rendered `[link]`s). D6 correctly notes `linear-combination-fold-specialization` "does not yet exist". This is honest disclosure of non-blocking references, not a defect. Pass.

**edge-label-fidelity — pass.** The graded-stack typed edges (`depends-on` / `reference`) match the prose in each edit's parenthetical justification, and the direct-vs-transitive discipline is applied consistently (verified L1/eigsolve excludes the transitive BLAS-1 leaves the §Dependencies section marks transitive).

**plan-kind-consistency — pass.** Declared kind is "Audit residue (primary) + Consistency drift (secondary)" with an edge-typing proposed-changes payload — the content shape matches (a frontier-typing pass + a root-caused audit finding + three index/narrative re-anchors routed to this L4-area owner).

**skill-uptake-survey — pass (telemetry).** The report's shape (citation-grounded edge-typing + a linter root-cause) implies `verify-citation-range`/`establish-negative-finding-exhaustiveness` could apply; D6 does not name a skill invocation, but this check is non-blocking surface telemetry only.

**rank-invariant — pass.** The headline honesty audit (brief claim a) HOLDS: all 15 typed nodes read `firm` on disk this cycle, verified directly at the cited §Status lines — `L1/dot:100`, `L1/normalize:99`, `L1/matrix-weighted-norm:110`, `L2/inner_product:449`, `L2/linear_combination:318`, `L2/nrm2:82`, `L3/dot:80`, `L1/eigsolve:167`, `L2/eigsolve:155`, etc. D6 promoted nothing; `rank: firm` is a typing of the genuine on-disk maturity. The `domain_energy_reduce` depends-on edges rest on `participation_ratio` (c077 firm) + `matrix-weighted-norm` (c091 firm) — `rank(3) ≤ min(3,3)` holds. The one genuine residual (`solve_family -> solve-family-map-dissolution`, firm-above-rough-in-tcb) is correctly identified as a real rank-gap and routed OUT of scope to D7, not papered over.

**reachability — pass.** All typed nodes are high-fan-out vocabulary leaves reachable from the feature-surface roots over `depends-on` edges (they are the most-depended-on frontier by construction). No orphaning introduced.

### Brief-directed spot-checks (all CONFIRMED)

- **(a) rank tokens honest / typing-not-promotion** — CONFIRMED. All 15 nodes `firm` on disk (verified per-line above). No promotion.
- **(b) edges direct-only, deliberately classified** — CONFIRMED. L1/eigsolve uses `ksp_solve`+`apply_linop` only (transitive BLAS-1 leaves excluded per `eigsolve.md:138`); L1/normalize uses `nrm2`+`scal` only (subsumption siblings excluded per `normalize.md:65`). The `lowers_to`/`lifts_from` identity-views are classified `reference` with a sound rationale (avoids importing the `L3/eigsolve` `partial-obstruction` rank onto the firm `L2/eigsolve`).
- **(c) linter root-cause CORRECT — the campaign headline** — CONFIRMED, this is a REAL defect. `read_status_line` (`graded_stack_lint.py:310-326`) does `blob = " ".join(lines[i+1:i+6]).lower()` (a 5-line join, `:319`) then scans tokens in the order `("partly-constructive", "rough-in (test-coverage-bounded)", "rough-in", "roadmap_goal", "obstruction", "partial-obstruction", "stub", "firm")` (`:320-322`) returning the FIRST match. `rough-in` (and `rough-in (test-coverage-bounded)`, and `stub`) precede `firm` in the scan order, and the scan is over a 5-line blob — so any §Status paragraph that LEADS with `` `firm` `` but mentions a rough-in/stub provenance/disclaimer within 5 lines is mis-read. Confirmed the trip on the cited witnesses: `L1/normalize:99` ("rough-in note"), `L2/inner_product:449` ("firm/rough-in L1 leaves" — substring in the first blob line), `L1/matrix-weighted-norm:110` ("promoted from `rough-in (test-coverage-bounded)`"), `L1/eigsolve:167` (same provenance phrase). ADDITIONAL trip cases the report did not enumerate but which its `rank:` typing also clears: `L2/nrm2:82` ("firm — consumer-stub" trips `stub`) and `L3/dot:80` ("firm — specialization-stub" trips `stub`) — both firm, both mis-readable by the same fallback. `derive_rank:337-343` confirms an explicit `rank:` token (or `firmness:`) is read BEFORE the prose fallback, so the typed `rank: firm` clears these by construction. The root-cause is sound and the campaign thesis ("typed `rank:` routes around the heuristic") is validated.
- **(d) L4/index count arithmetic** — CONFIRMED. The chapter dep-map carries 19 non-anchor chapter rows (iteration group 4 firm at `:87-90`; data-algebra group 10 rows at `:96-105` = 9 firm + gram_reduce rough-in at `:101`; outer-driver caps eigsolve/fold_solve/frequency_sweep/ksp_solve/solve_family = 5 firm at `:113-121`), i.e. 18 firm + 1 rough-in = the "18 + 4 outer-driver" `:32` header (the 4 = the `solve-monad` vocabulary anchors counted separately). Firming gram_reduce → 19 firm, exactly D6's 18→19. The `:58` "Rough-in at L4 (0)" was a pre-existing optimistic stale (gram_reduce sat at rough-in-tcb at `:101`); D6's J3 edit makes it true and is the honest correction.
- **(e) solve_family.md:154 re-anchor faithful** — CONFIRMED. The on-disk `:154` Column-gate note does assert all three stale claims D6 cites: (i) gram_reduce folds "plain-`rough-in` matrix-weighted-norm", (ii) the c080 "NO-GO-HELD … firm-on-positive-structure escape INAPPLICABLE", (iii) "Those columns stay `status: seed` this cycle". All three are genuinely overturned: `matrix-weighted-norm:110` is firm (promoted c091, the batch-28 meta-phase GO explicitly overturning the c080 NO-GO), and gram_reduce/bilinear-form firm via the in-flight D1/D3 reports D6 correctly cites as inputs. The re-anchor is accurate.

### Wave-sequencing note (NOT a defect)

On disk RIGHT NOW `bilinear-form.md:323` and `gram_reduce.md:228` still read `rough-in` — they are flipped to firm by D1 (Wave 1) and D3 (Wave 2) THIS cycle, which D6 (Wave 3) reads from the cited D1/D3 reports rather than from disk. This is the documented wave structure (D6's inputs list D1/D3 reports explicitly); the integrator applies D1→D3→D6 in order, after which the post-cascade state D6 narrates is on disk. Flagged here only so the integrator confirms the apply-order; it is correct dispatch sequencing, not a citation error.

### Issues found

1. **citation-validity (warning) — bare tool-path citation.** Finding 1 "Root cause" paragraph (CYCLE.md §Specific finding, the `derive_rank` line) cites `graded_stack_lint.py:328-380` without the `tools/graded-stack-lint/` prefix; citecheck reports `[MISS]`. The full-path form appears correctly in §Supporting evidence. Fix: prefix the path. Severity: low (hygiene; claim supported).

2. **citation-validity (warning) — range over-extension.** The same `derive_rank` citation `:328-380` overshoots the function's actual end at `:361` (`build_graph` starts `:364`), spilling ~19 lines into the next function. The cited claim (priority ordering) lies within `:328-361`, so the claim holds; only the range bound is loose. Fix: tighten to `:328-361` (or `:328-343` for the precise priority-cascade lines). Severity: low.

Both issues are confined to ONE citation (the `derive_rank` pinpoint) and are non-substantive — the root-cause finding, the rank honesty, the arithmetic, and the re-anchor fidelity are all sound. No surface/rotation/rank/reachability defects.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, warning): bare tool-path citation.** The `derive_rank` pinpoint in the Finding-1 "Root cause" paragraph (CYCLE.md §Specific finding) was cited as bare `graded_stack_lint.py:328-380`, missing the `tools/graded-stack-lint/` path prefix (citecheck `[MISS]`).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §Specific finding (Finding 1 "Root cause" paragraph) — rewrote the citation to the full-path form `tools/graded-stack-lint/graded_stack_lint.py:328-361`, matching the full-path form already used in §Supporting evidence. In scope per repairer authority "citation line range off by a small offset / trivially-supported missing citation hygiene".

- **Finding 2 (citation-validity, warning): range over-extension.** The same `derive_rank` citation `:328-380` overshot the function's actual end; `build_graph` begins at `:364`.
  - **Decision**: repaired.
  - **Action**: verified the true function span on disk — `derive_rank` is `tools/graded-stack-lint/graded_stack_lint.py:328-361` (lines 362-363 blank; `build_graph` opens at 364). The load-bearing priority-ordering logic the claim rests on is the `tok = fm.get("rank") or fm.get("firmness")` cascade falling through to `read_status_line` last, at `:336-343` — squarely within `:328-361`. Tightened the range in BOTH occurrences (the Finding-1 paragraph AND the §Supporting evidence line, which carried the same loose `:328-380` bound) to `:328-361`. Re-ran `citecheck.py --scan`: 25 ok / 0 failing (both `graded_stack_lint.py` citations now resolve, in bounds).

### Unrepairable findings

None. Both warning findings were mechanical citation-hygiene fixes (path prefix + range tightening) on a single tool-source citation; the underlying claim (the `read_status_line` blob-scan / token-priority bug) is correct and confirmed by the critic, and was not altered.

## Suggested resolution

`ready`. All eight critic checks plus the two graded-stack checks were `pass` save the single `citation-validity: warning`, now `repaired`. No follow-up agent. Integrator note: the report is a Wave-3 (D6) member — apply D1→D3→D6 in cycle order per the critic's wave-sequencing note (the post-cascade state D6 narrates lands on disk only after D1/D3 apply); this is correct dispatch sequencing, not a defect.
