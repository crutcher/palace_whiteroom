---
slug: establish-negative-finding-exhaustiveness
promoted_at: cycle-030 meta-phase (batch-8) / 2026-05-30
promoted_from: scaffolding/skill-candidates.md (c028 critic)
addresses: the negative-localization-with-routing shape (an "Palace does NOT expose X" finding that routes a methodology decision — obstruction-theme target vs. perpetually-blocked-pending-anchor)
status: promoted
---

# establish-negative-finding-exhaustiveness

A producer- and critic-facing skill for **negative-localization-with-routing** reports — dispatches whose entire deliverable is "Palace has NO standalone X primitive, therefore route the OQ leaf to obstruction (or to opaque-library-ownership, etc.) rather than leaving it BLOCKED pending an L1 anchor that does not exist."

The load-bearing claim is a **negative** ("zero hits"), which is exactly the shape that needs an exhaustiveness standard: a negative finding routes a real methodology decision, so a sloppy or term-narrow search that *missed* a positive hit would mis-route. This skill crystallizes the bar.

## When to invoke

- **Producer (harvester / abstractor / cross-layer-cross-cutter on a "does Palace expose X?" dispatch):** to establish the negative-localization finding strong enough to license routing to obstruction.
- **Critic (surface-or-evidence + citation-validity):** to re-verify the producer's exhaustiveness when the report's load-bearing claim is an absence.
- **Lowering-verifier (auditing an obstruction theme):** to confirm the negative anchors are exhaustive and structurally well-grounded.

## Why

Across the unimplemented-stub / opaque-library obstruction family — `minres` and `bicgstab` (cycle-004 enum-only-stub obstructions), the `eigsolve` opaque-library partial-obstruction (cycle-024), the cycle-028 `trsv` negative-localization, and the cycle-029 `triangular-solve-obstruction` opaque-library-ownership obstruction — the same "absence-of-X routes a methodology decision" shape recurs. The c028 `harvester-trsv-l1-localization` dispatch was the exemplar: its entire deliverable was "Palace has NO standalone `trsv`, therefore route the L3-inventory-gap leaf to obstruction rather than `BLOCKED-pending-L1-anchor`." It did the work well by hand (two stated codemap searches with explicit terms, plus an implicit accounting that every residual `triangular` token in the tree is a known non-`trsv` red herring), and a critic re-running the searches reproduced zero-hit and confirmed all 8 `triangular` mentions are accounted-for. But there was no skill naming the bar, and the same shape recurs each cycle.

Companion to `verify-citation-range` (which verifies positive pinpoints); this one sets the bar for the **absence** claim.

## Procedure

To establish a negative finding strong enough to route a methodology decision:

1. **State the search terms explicitly,** including casing/synonym variants of the target symbol. Example for `trsv`: `trsv|trsm|TriSolve|TriangularSolve|SpTrSV` + the broadened bare-stem case-insensitive sweep `triangular`.
2. **Run the searches against the in-scope tree** (Palace source under `reference/palace/palace/`, NOT vendored upstream MFEM/SLEPc/Hypre) and record the hit count. Prefer `mcp__palace-codemap__search_text` for the in-scope filter; fall back to `grep -rn` if the codemap is unavailable.
3. **Account for every residual hit** of the broadened sweep — classify each as either:
   - **a genuine hit** (the negative finding *fails*; the producer's premise was wrong; route as positive-anchor instead), OR
   - **a named non-target** (a red herring / different-family object — e.g. `triangular` in `triangular_mesh.cpp`, or HYPRE-internal relax-type enum strings).

   No token may be hand-waved. The classification per residual hit goes in the report's evidence section.
4. **Confirm the relevant public-API surface positively** to show the absence is structural, not a search miss. Example: enumerate `densematrix.hpp`'s exported functions to show `trsv` is not among them, even though `gemv`/`Mult`/`Invert` etc. are. This is the "we know what Palace DOES expose in this header, and X is not it" complement to the searches.
5. **Critic re-runs steps 1+3+4** (and reproduces the producer's stated searches + the broadened sweep + the positive-API enumeration). The negative finding is established only when steps (3) and (4) leave NO unexplained token AND the critic independently confirms the count.

The negative finding's strength rests on the **conjunction**: search-exhaustive AND every-residual-accounted-for AND positive-API-confirmed-absent AND critic-reproduced. A single unexplained residual `triangular`-token leaves a one-token hole through which the negative claim leaks.

## Output shape

The report's §Localization or §Negative-anchors section should carry:

- A "Searches run" list: each `(query, scope, hit-count)`.
- A "Residual tokens accounted-for" table: each residual hit, with its file + line + a one-line "red-herring because ..." classification.
- A "Positive API surface" enumeration: the relevant header's exported functions (or other positive-API-shape evidence) showing X is structurally absent.
- The routing decision: `route as obstruction-theme target` / `route as opaque-library-ownership` / `route as enum-only-stub` / etc., with the matching CLAUDE.md / friction-ledger / OQ slug.

The critic's §Citation-validity / §Surface-or-evidence paragraph should EXPLICITLY note the negative finding was independently re-verified (search re-run + residual count match + positive-API spot-check).

## Anti-patterns

- **Do not** establish a negative finding from a single narrow search (e.g. `grep -n trsv palace/` and stop). A negative claim that routes a methodology decision needs the broadened-sweep + residual-accounting + positive-API conjunction.
- **Do not** treat "I searched and got zero hits" as licensing without accounting for the broadened-sweep residuals. The c028 trsv dispatch had 8 `triangular`-token residuals; each was a real source-tree token that needed a red-herring classification. Skipping that step would have left a hole.
- **Do not** include vendored upstream (`reference/palace/mfem-extras/`, `reference/palace/extern/`) in the search scope unless the routing decision is specifically about upstream. The negative finding is about Palace's own surface, not the vendored libraries it consumes.
- **Do not** chain this skill with `verify-citation-range`'s drift-detection (`citecheck --anchor`) — that tool answers "WHERE is this positive citation" mechanically, but it has no answer for "is X absent from the tree" (that's a search exhaustiveness question, not an anchor question). The two skills are complements, not stages of the same procedure.

## Precedents

- **Cycle-004**: `minres-iteration` + `bicgstab-iteration` obstruction themes — enum-only-stub sub-kind; established the obstruction-theme category but without a written exhaustiveness procedure.
- **Cycle-024**: `eigsolve` L3 partial-obstruction (opaque-library-ownership sub-kind avant-la-lettre; the SLEPc EPS solver loop is library-opaque).
- **Cycle-028 D7 (`harvester-trsv-l1-localization`)**: the exemplar — explicit search terms, broadened-sweep, all 8 `triangular` residuals classified, positive-API confirmation (`densematrix.hpp` enumeration). Routed to L1>L0 obstruction-theme follow-up.
- **Cycle-029 D3 (`abstractor-triangular-solve-obstruction`)**: the routed follow-up — the FIRST opaque-library-ownership L1>L0 obstruction theme (HYPRE-internal relax-type enum strings + external direct-solver wrappers as negative anchors); citable home for the resolved-by-obstruction `trsv` leaf.
- **Cycle-030 meta-phase (batch-8)**: codified this skill from the cycle-028 critic's skill-candidate filing. The companion sub-kind refinement (`opaque-library-ownership` vs. `enum-only-stub`) is codified in CLAUDE.md §Methodology invariants + the abstractor role-spec.
