---
verifies: ./CYCLE.md
critiqued_at: 2026-05-28T145618Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-05-28T150412Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: unrepairable
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L0 bundle-6 candidates #2 / #3 — discovery + ranking"

## Critique

### Checks run

**citation-validity — warning.** All source ranges were re-verified against the Palace tree
via `palace-codemap`. The bulk are exact: `orthog.hpp` is confirmed 93 lines, header-only
(`list_files palace/linalg/orthog.*` returns only the `.hpp` — the report's "no `orthog.cpp`"
claim holds); `namespace palace::linalg` opens at line 15 ✓; `IdentityInnerProduct` struct
30-37 (report cites "line 30", the declaration line ✓); `OrthogonalizeColumnCGS` is exactly
57-89 ✓; `OrthogonalizeIteration` is exactly 308-325 in `iterative.cpp` and its body is a
`switch` over `MGS / CGS / CGS2` with `CGS2 = OrthogonalizeColumnCGS(..., true)` — the
`refine`-flag claim is source-faithful ✓; `rap.hpp` `ParOperator` 24-121 ✓,
`ComplexParOperator` 124-222 ✓; `rap.hpp`=252 + `rap.cpp`=979 = 1231 lines ✓. **The one
defect:** `OrthogonalizeColumnMGS` is cited as `orthog.hpp:39-55` in the proposed L0 chapter
(block A, lines 96 and 162) and in supporting evidence (line 196). The codemap reports the
function span as **41-53**, and the *already-firm* `book/src/L1/orthogonalize.md` cites it as
`orthog.hpp:41-53` with an explicit note "(Range covers the function-name line through the
closing brace at line 53.)"; the sibling cycle-013 wave-1 abstractor theme also uses 41-53.
The report's 39-55 over-ranges by ~2 lines on each side (39-40 = blank + template-decl head;
54-55 = blank + next template head) and drifts from the established authoritative range for the
same symbol. Functionally correct location, but a citation-range regression against the firm
entry it cross-links.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme. This is
new-surface authoring (a brand-new L0 file-overview chapter) plus a discovery/ranking
artifact. Every authored claim carries a citation pointer; no rotation_claim-without-surface
shape is present. Not applicable as a refinement check.

**rotation-quality — pass.** No L_{n+1}→L_n rotation is asserted by this report. The L0 chapter
documents source-level algebra and explicitly *defers* the lowering ("the in-place `w` overwrite
is L0-internal ... the L1 form returns a fresh orthogonal residual"; "the three variants become
L1's single runtime variant axis") to the L1 entry / the L1>L0 theme rather than performing the
rotation itself. Correct discipline for an L0 reference note (high→low, source-faithful at L0).
Not applicable as a rotation check.

**variant-axis-coverage — pass.** The orthogonalization surface has a clear variant axis
(`MGS | CGS | CGS2`). The chapter covers all three explicitly (§"The two variants and what each
buys" enumerates MGS, CGS, and CGS2=`refine=true`), maps them onto the two routines plus the
`refine` flag, and correctly identifies that the runtime *selection* over the axis lives in the
sibling `iterative.cpp` (`OrthogonalizeIteration`), not in this header. The `IdentityInnerProduct`
default (inner-product policy axis) is also named and scoped as "absorbed at L1". No hidden
branch. Source confirms exactly three switch cases.

**cross-reference-integrity — pass.** Every `[link]` target resolves on disk:
`L1/orthogonalize.md`, `concepts/orthogonalization.md`, `concepts/gemv_basis.md`,
`L0/linalg-iterative-file.md`, `L0/par-types-single-rank-reading.md`,
`L0/output-arg-vs-receiver.md`, `L0/transparent-vs-load-bearing-tricks.md`,
`L0/apply-linop-overload-set.md` all exist. The index.md edit (B) `[old]` anchor reproduces the
current `book/src/L0/index.md:27` line verbatim — it will match. (The SUMMARY.md anchor is a
separate, flagged issue — see plan-kind-consistency / Issues.)

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this report (it is an L0
file-overview, not a lowering theme). The "Notes for higher layers" section gestures upward to L1
but does not assert a specific edge it then mis-describes. Not applicable.

**plan-kind-consistency — warning.** The dispatch scope is
`L0-bundle-6-candidates-discovery-and-ranking` (a discovery/ranking kind). The report delivers
the discovery+ranking deliverable cleanly (citation-pressure survey of 28/25 `linalg/` files, a
ranked table, an OQ-promotion block). However it *also* authored a complete, firm-shaped L0
chapter for `linalg-orthog-file` (block A, ~90 lines of prose + Evidence) plus index + SUMMARY
registration — i.e. discovery turned into authoring within the same dispatch. The report
justifies this as "small + ready + already line-range-mapped by the firm L1 entry" and explicitly
held back the larger #2 `linalg-rap-file` for a dedicated cycle-014 dispatch. This is a defensible
in-scope-creep (the file is genuinely 93 lines and the ranges were pre-verified by an existing
firm entry), and it is consistent with the project's accumulate-surface posture — but it is a
kind-boundary stretch worth flagging: a "discovery/ranking" dispatch produced a firm-content
proposed-changes block that the integrator must now safety-gate as authored content, not as a
ranking note. The content shape (firm L0 file-overview) does match what it claims to be, so this is
warning, not fail.

**skill-uptake-survey — pass.** Localization used `palace-codemap` (`list_files`) per the
MCP-first directive — surfaced in Summary and Supporting evidence. The SUMMARY.md registration
note (block C) explicitly references the `summary-md-surgical-insert` skill as the fallback for the
anchor mismatch — appropriate skill uptake for the registration shape. No missing-skill telemetry.

### Issues found

1. **MGS citation range over-ranges and drifts from the firm entry** — `CYCLE.md` block (A)
   lines 96 & 162, and Supporting evidence line 196: `OrthogonalizeColumnMGS` cited as
   `orthog.hpp:39-55`. Codemap span is **41-53**; the already-firm `book/src/L1/orthogonalize.md`
   and the sibling cycle-013 wave-1 `orthogonalize-mutation-rotation` theme both cite **41-53**.
   Severity: low-moderate. Correct symbol/location, but an out-of-range citation and an internal
   inconsistency with the firm cross-linked entry. Candidate repair: change `39-55` → `41-53` in
   all three sites (the CGS sibling 57-89 is already exact, so this aligns the pair).

2. **SUMMARY.md edit (C) `[old]` anchor does not match the artifact** — `CYCLE.md` block (C)
   lines 178-180. The `[old]` text is `  - [File — linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)`
   but the actual `book/src/SUMMARY.md:78` reads
   `- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)` (note the
   `palace/` path prefix and the leading single-dash indentation). The proposed `[new]` entry text
   `[File — linalg/orthog.hpp]` likewise omits the `palace/` prefix that every other L0 `File —`
   SUMMARY entry carries (`palace/linalg/vector...`, `palace/linalg/operator...`, etc.). Severity:
   moderate (the proposed edit as literally written will not apply, and if forced would introduce
   a naming-convention inconsistency). Mitigating: the report self-flagged this exact risk in its
   Integrator note (lines 183-187) and pointed at `summary-md-surgical-insert`. Candidate repair:
   correct the `[old]` anchor to the verbatim line 78 and the `[new]` title to
   `[File — palace/linalg/orthog.hpp]`.

3. **Discovery dispatch authored firm L0 content (kind stretch)** — `CYCLE.md` block (A), the
   whole `linalg-orthog-file.md` proposed-changes block. The dispatch scope is discovery/ranking;
   the firm-content chapter is an in-scope expansion the report argues for explicitly. Severity:
   low (informational). No repair needed if the integrator accepts the authored chapter on its own
   merits; flagged so the integrator treats block (A) as authored content requiring the
   author-content safety net, distinct from the ranking deliverable.

4. **Overlap with cycle-013 wave-1 `orthogonalize-mutation-rotation` (same source file)** —
   informational, NOT a conflict. The wave-1 abstractor report
   (`reports/2026-05-28T0915Z-abstractor-orthogonalize-mutation-rotation-l1-l0-theme/`) authors
   `book/src/L1-L0/orthogonalize-mutation-rotation.md` and cites the same `orthog.hpp`; this report
   authors `book/src/L0/linalg-orthog-file.md`. The two target **different artifact files in
   different Parts** (L0 file-overview vs L1>L0 theme) — no file collision. Both append one
   `SUMMARY.md` entry (in different SUMMARY sections), so the integrator should apply them with
   independent surgical inserts. The content split is clean (L0 = per-variant source algebra; L1>L0
   = the mutation rotation). One latent inconsistency to watch: this report's MGS range (39-55)
   disagrees with the wave-1 theme's MGS range (41-53) for the same symbol — issue #1 resolves
   this in this report's favor of the established 41-53.

5. **"L0 chapter count is 18" housekeeping claim unverified here** — `CYCLE.md` lines 243 & (OQ
   block). The current `book/src/L0/index.md` carries 17 `- [` bullets including Convention/
   sub-section headers, so the post-#3 "18" is an integrator-finalize roadmap number, not a
   load-bearing content claim. Severity: trivial; flagged only so finalize re-derives the count
   rather than trusting it.

## Repair

### Fixes attempted

- **Finding**: citation-validity warning — `OrthogonalizeColumnMGS` cited as `orthog.hpp:39-55`,
  over-ranging the true `41-53` span (firm `L1/orthogonalize.md` + wave-1 theme both cite 41-53).
  - **Decision**: repaired
  - **Action**: Verified the symbol span via `palace-codemap get_symbol_def OrthogonalizeColumnMGS`
    → `palace/linalg/orthog.hpp:41-53`. Corrected `39-55` → `41-53` at all three sites the critic
    identified: CYCLE.md block (A) §"At a glance" bullet, block (A) Evidence line, and the
    Supporting-evidence `orthog.hpp symbols` line. The CGS sibling (57-89) was already exact; the
    pair is now aligned, and the citation matches the firm cross-linked entry.

- **Finding**: cross-reference-integrity / Issue #2 — SUMMARY.md edit (C) `[old]` anchor and
  `[new]` title omit the `palace/` path prefix and use wrong indentation, so the block would not
  apply cleanly (self-flagged by the report's integrator note).
  - **Decision**: repaired
  - **Action**: Verified `book/src/SUMMARY.md:78` reads
    `- [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)` (single-dash
    indent, `palace/` prefix). Rewrote block (C): `[old]` anchor now matches line 78 verbatim;
    `[new]` carries the existing iterative entry plus
    `- [File — palace/linalg/orthog.hpp](./L0/linalg-orthog-file.md)` with the `palace/` prefix
    matching every sibling `File —` L0 entry. The block now applies cleanly via plain surgical
    insert (the `summary-md-surgical-insert` fallback note remains valid but is no longer required).

- **Finding**: plan-kind-consistency warning / Issue #3 — discovery/ranking dispatch also authored
  a full firm L0 bundle chapter for `linalg-orthog-file` (block A, 93-line header).
  - **Decision**: unrepairable (no edit — informational routing)
  - **Rationale**: Stripping or rewriting the authored chapter would be a content decision, outside
    repair authority. The critic deemed the authoring defensible (small file, ranges pre-verified by
    the firm L1 entry, consistent with accumulate-surface posture). No mechanical fix applies; this
    is an integrator safety-gating concern, routed below.

- **Finding**: Issue #4 — overlap with cycle-013 wave-1 `orthogonalize-mutation-rotation` (same
  `orthog.hpp` source file).
  - **Decision**: not-needed
  - **Rationale**: Critic confirmed no collision — the two reports target different artifact files
    in different Parts (L0 file-overview vs L1>L0 theme). The MGS-range disagreement that was the
    one latent inconsistency is now resolved in favor of 41-53 by the citation-validity repair
    above. Routed to integrator awareness for apply-ordering (both append one SUMMARY.md entry in
    different sections — independent surgical inserts).

### Unrepairable findings

- **Discovery dispatch authored firm L0 content (plan-kind stretch)** — the integrator should
  safety-gate the authored L0 bundle chapter (block A, `book/src/L0/linalg-orthog-file.md`) as
  in-scope authored content (discovery→authoring stretch, defensible per the critic), applying the
  author-content safety net rather than treating block (A) as a mere ranking note. The blocking
  follow-up is integrator handling, not a re-dispatch, so `follow_up_agent: null`.

## Suggested resolution

`ready`. Notes for the integrator:

- Block (A) is authored firm L0 content despite the discovery/ranking dispatch kind — apply the
  author-content safety net, not the ranking-note path. The stretch is defensible (93-line
  header-only file, ranges pre-verified by the firm `L1/orthogonalize` entry).
- **Apply-ordering awareness**: this report cites the SAME `orthog.hpp` file as the cycle-013 wave-1
  `orthogonalize-mutation-rotation` L1>L0 theme. The critic confirmed NO collision (different target
  files, different Parts; both append independent SUMMARY.md entries in different sections). The MGS
  citation range is now consistent (41-53) across both reports after this repair.
- Both blocks (B) index.md and (C) SUMMARY.md now match the artifact verbatim and apply cleanly.
- The "L0 chapter count is 18" OQ housekeeping number is an integrator-finalize roadmap figure
  (Issue #5) — re-derive at finalize rather than trusting it.
