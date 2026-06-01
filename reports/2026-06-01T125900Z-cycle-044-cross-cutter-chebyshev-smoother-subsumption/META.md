---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T133000Z
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
repaired_at: 2026-06-01T134500Z
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

# META: verification of chebyshev-smoother-L3-subsumed-by-firm-chebyshev (cycle-044 D2)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan`: 8 ok, 11 `[AMBIG]`. Every one of
the 11 "failures" is a bare-basename ambiguity (`chebyshev.md` resolves to both
`book/src/L3/chebyshev.md` and `book/src/L4/chebyshev.md`; `index.md` resolves to 16 files),
NOT a bounds/path error. The report's prose disambiguates each in context ("L3 `chebyshev.md:415-420`",
"the firm L3 `chebyshev` entry"), so these are not genuine wrong-target citations — but the
scanner cannot mechanically resolve them, so I mark `warning` rather than `pass`. I hand-verified
every load-bearing pinpoint by reading the actual targets:
- Title "the iteration-rotation rendering of the **Chebyshev smoother**" — confirmed verbatim at `book/src/L3/chebyshev.md:16-17`.
- Law 2 linear-preconditioner-form (`:299-304`), Law 3 symmetry alias (`:305-309`, prose cites `:306-309`), Law 5 variant-invariant body (`:316-324`), Law 6 body identity-in-form incl. L1 `chebyshev-smoother` (`:325-331`) — all confirmed.
- Variant axes §1 polynomial-kind absorption + both-class citations (`:415-420`; axis 2 ends `:425`, so the report's `:415-425` span is correct) — confirmed.
- Evidence block (`:496-508` bodies; `:509-511` 4th-kind decl; `:514-516` 1st-kind decl; `:509-516` umbrella) — confirmed.
- L1 sibling references `chebyshev.md:404-405` and `:91` — both confirmed as L1 `chebyshev-smoother` links.
- L3 index `index.md:30` (chebyshev dep-map row), `:48` (c036 D2 (B)-candidate with "requires a subsumption check first" caveat), `:55` (§Working-notes first partial-obstruction record) — all three confirmed at the cited lines.
- Palace source: codemap `search_text "class Chebyshev"` returns EXACTLY two hits — `ChebyshevSmoother` `chebyshev.hpp:23`, `ChebyshevSmoother1stKind` `:86`; both `public Solver<OperType>`; symmetry alias `MultTranspose2 → Mult2` at `:72-75`; class doc Phillips & Fischer at `:15-19`. All confirmed via `read_range`.
No bounds drift, no wrong-target, no fabricated line. The warning is purely the bare-basename hygiene lint.

**surface-or-evidence — pass.** This is a NEGATIVE-result OBSERVATION (subsumption check), not a
refinement of an existing operator/theme — no surface is modified and the report explicitly carries
**no proposed-changes block**. The check is load-bearing here in the inverse sense the dispatch asked:
is the NO-LAND verdict evidence-backed? It is. The "no new surface" conclusion is the correct output
because the firm L3 `chebyshev` entry already carries every claim a standalone `chebyshev-smoother`
L3 row would (title naming the smoother, Law 2/3 preconditioner role, Law 5/6 variant + body identity,
Variant axes §1 polynomial-kind absorption with both class decls cited). A standalone row would be a
duplicate, not a missed-coverage gap. Verdict sound.

**rotation-quality — pass (not applicable).** No rotation is asserted; the report's whole point is
that the iteration rotation already exists (firm L3 `chebyshev`, `partial-obstruction`, c013) and no
second rotation is warranted. No 1:1 renaming is proposed as a rotation. N/A to a subsumption observation.

**variant-axis-coverage — pass.** The one variant axis at issue — polynomial-kind
(`Chebyshev-4th | Chebyshev-1st`) — is exactly the axis the report shows is already absorbed at firm
L3 `chebyshev` (Variant axes §1 `:415-420`, Law 5 `:316-324`). The two Palace classes are the two
axis values; both are cited; neither is a hidden branch. The element-type axis (real/complex) is
likewise covered by the firm entry (`:421-425`). No uncovered combination.

**cross-reference-integrity — pass.** All four sibling chapter links resolve on disk:
`book/src/L1/chebyshev-smoother.md`, `book/src/L2/chebyshev-iteration.md`, `book/src/L4/chebyshev.md`,
`book/src/L3/chebyshev.md` all exist (`ls` confirmed). The L3 dep-map row for `chebyshev` is present
at `index.md:30` and the c036 D2 (B)-candidate / working-note lines (`:48`, `:55`) resolve as cited.
No `firm`-body-inside-fence guard applies (no proposed-changes fence; read-only audit).

**edge-label-fidelity — pass.** The report discusses the L3↔L1 relationship (L1-slug name vs L3-slug
name for one operator) and the transitive L3>L2∘L2>L1 body identity; the prose matches the edges it
names (e.g. Law 6 is correctly described as a body-level transitive identity, not a loop-level one).
No mislabeled edge.

**plan-kind-consistency — pass.** Declared shape is a NEGATIVE-result coverage-gap OBSERVATION from
`cross-layer-cross-cutter`; content matches — one observation, a verdict (SUBSUMED/NO-LAND), a
recommendation to close the candidate, no artifact mutation, no proposed-changes block. Frontmatter
`status: pending` is the pre-critique default. The "Observation kind" section explicitly self-classifies
as NEGATIVE result. Consistent.

**skill-uptake-survey — pass.** The report states its Palace pinpoints were "verified via codemap this
dispatch" (the MCP-first-localization expectation for the C++ tree) and the work is exactly the
`subsumption check` the c036 D2 audit deferred. No dedicated subsumption-check skill exists to cite;
the implied procedure (search_text for the class surface, confirm both variant-axis values already
cited at the firm entry, confirm the smoother-role laws present) is followed in substance. Telemetry-only;
no gap.

### Issues found

1. **citation-validity (minor, mechanical) — bare-basename citations throughout `CYCLE.md` §Specific finding / §Supporting evidence.** The report cites the L3/L4 chebyshev entry and the various `index.md` files by bare basename (`chebyshev.md:415-420`, `index.md:48`, etc.) rather than full path. `citecheck --scan` flags all 11 as `[AMBIG]` because `chebyshev.md` matches both `book/src/L3/` and `book/src/L4/`, and `index.md` matches 16 files. The prose disambiguates each by layer-prefix, and I hand-verified every target resolves to the intended firm L3 entry / L3 index at the cited lines — so no citation is wrong, only under-qualified. Severity: low (hygiene). Candidate repair: qualify the load-bearing basenames with their `book/src/L3/` path (the §Supporting-evidence block already uses full paths; the inline §Specific-finding pinpoints are the ones flagged).

No substantive issues. The SUBSUMED / NO-LAND verdict is sound and fully evidence-backed:
exactly two `class Chebyshev*` exist in Palace (`chebyshev.hpp:23`, `:86`), both are the polynomial-kind
variant axis already absorbed at firm L3 `chebyshev` (Variant axes §1 + Law 5, both class decls cited at
`:509-516`); the smoother-as-preconditioner role is already Law 2/3; the firm entry's title literally names
"the iteration-rotation rendering of the Chebyshev smoother"; and the c036 D2 caveat explicitly demanded this
subsumption check, which resolves subsumed. Closing the candidate with no land and no proposed-changes is the
correct conclusion, not a missed-coverage gap.

## Repair

### Fixes attempted

- **Finding**: citation-validity (warning) — bare-basename artifact citations in §Specific finding (`chebyshev.md:…`, `index.md:…`) trip `citecheck --scan` as `[AMBIG]` because `chebyshev.md` resolves to both `book/src/L3/` and `book/src/L4/` and `index.md` resolves to 16 files. Not bounds/wrong-target errors (critic hand-verified every target); purely path-under-qualification hygiene.
  - **Decision**: repaired
  - **Action**: Added the `book/src/L3/` path prefix to every bare-basename artifact citation. In §Specific finding: `chebyshev.md:415-420`, `:316-324`, `:509-511`, `:514-516`, `:496-508`, `:299-304`, `:16-17`, `:404-405`, `:91`, `:325-331`, and `index.md:55`. Also qualified the two same-class bare basenames outside §Specific finding for full lint closure: the resolution-note string in §Recommendation (`chebyshev.md:509-516`, which the planner is told to copy into `priorities.md`) and the §Open-questions reference (`index.md:48`). The §Supporting-evidence block already used full paths and was untouched. The Palace L0 cites (`palace/linalg/chebyshev.{hpp,cpp}:…`, relative to `reference/`) were already correctly qualified.
  - **Verification**: `citecheck --scan` on the repaired CYCLE.md now reports `20 ok, 0 failing` (was 8 ok / 11 AMBIG). No bounds change, no target change — the line ranges and resolved files are identical to what the critic hand-verified; only the path prefix was added.

The other seven checks were `pass` with no flagged issue (no surface/rotation/variant/x-ref/edge/plan-kind/skill defect), so no repair was needed for them.

### Unrepairable findings

None. The single warning was mechanical path-qualification, fully within repair authority. No substantive authoring, no artifact mutation, no content decision was involved.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- This is a **read-only observation report — there is NO proposed-changes block and NO `book/` mutation**. The integrator-per-report pass should apply nothing to `book/`; the only artifact-adjacent action is the candidate-closure recorded below.
- **The verdict closes the `chebyshev-smoother` L3 (B)-candidate (SUBSUMED / NO-LAND).** The integrator should record the candidate closure in `scaffolding/priorities.md`, retiring the c036 D2 (B)-substantive `chebyshev-smoother` candidate with the report's resolution note: subsumed by firm L3 `chebyshev` (c013); `chebyshev-smoother` is the L1-slug name for the same operator whose L3 iteration-rotation rendering is L3 `chebyshev`; Palace `ChebyshevSmoother` / `ChebyshevSmoother1stKind` are the polynomial-kind variant axis already absorbed at L3 (cited `book/src/L3/chebyshev.md:509-516`). The c036 D2 caveat at `book/src/L3/index.md:48` ("requires a subsumption check first") is the trigger this dispatch resolves.
- This is a clean negative result that **removes** a candidate from the batch-13 substantive-L3 frontier rather than adding work — useful input for the cycle-planner's next-cohort selection. No follow-up harvester/abstractor/lifter dispatch is spawned.
