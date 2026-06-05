---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T061500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T063000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of concepts library index + dependency-map refresh

## Critique

### Checks run

**citation-validity — warning.** This is intro / dep-map content (no Palace source claims), so the check is light: the
report's load-bearing factual assertions are about repository state (deleted corpus, decommissioned roles, on-disk page
set), all of which I verified directly (`book/src/spec/` does not exist; the orchestrator/`prompts/` provenance is gone
per CLAUDE.md §Repository status). Those check out. The one defect is a **numeric drift**: the report repeatedly says
"**53** on-disk concept pages" / "53 index-table concept links" (CYCLE.md Summary lines 32-34, line 639, Open-questions
line 673). The `book/src/concepts/` directory holds 53 *files*, but two of them are infra (`index.md`,
`dependency-map.md`); the actual concept-*page* count — and the §Index table row count — is **51**. The framing
"the 53 on-disk concept files" is technically true of files but is used interchangeably with "the 53 ... concept pages"
and "53 index-table concept links," which is off by two. Not a build or link problem, but a load-bearing count stated
wrong in the document's own self-description.

**surface-or-evidence — pass.** The stripped content is genuinely dead pre-redirect framing, verified against current
repo state: the `concept_writes mode=create` / orchestrator auto-maintain prose, the `prompts/synthesizer.md` /
`prompts/planner.md` provenance, the `grep -l ... book/src/spec/slices/*.md` recipe, the `:::planned` forward-projection
machinery keyed on roadmap slice slugs, and the `../spec/slices/X.md` format-example links all reference artifacts that
no longer exist (`prompts/` and `book/src/spec/` are both deleted). None of it is load-bearing current process. This is
a legitimate dead-framing strip plus a re-derivation, not a refinement masquerading as a backfill.

**rotation-quality — pass (not applicable to concepts-index / dep-map kind).** No algebraic/structural rotation is
asserted; this is library-index + dependency-graph maintenance.

**variant-axis-coverage — pass (not applicable).** No operator with orthogonal variant axes is in scope.

**cross-reference-integrity — warning (load-bearing for this kind).** Strong on the headline claims, one real
inconsistency:
- All **51** §Index-table concept links resolve to existing on-disk files (verified each `./<name>.md`).
- The `gmres` / `plane-rotation-stream` / `orthogonalization` distinction **holds**: each exists as a real
  `book/src/concepts/<name>.md` page (distinct from the deleted slice slugs of the same name) — confirmed by reading
  each page head.
- The removed-node claims are correct: none of `allreduce_sum` / `copy` / `zero` / `extract-diagonal` /
  `spectrum-estimate` / `iterate_while` / `orthogonalize_column` / `axpby` has a `concepts/` page (removal justified).
- **The build-green claim holds**: the only surviving `../spec/slices/` references (index.md:42-43 slice links,
  index.md:53 grep prose) sit inside the Edit-A `[old]` block being removed, AND they live inside a fenced ```markdown
  code-example (linkcheck does not follow links inside fenced blocks) — which is why the build is already green.
- **The defect — a dangling `reciprocal` node.** The new "Primitives + algorithms" sub-graph contains
  `chebyshev-iteration --> reciprocal` (CYCLE.md line 525) and lists `reciprocal` among the bare leaf primitives
  (line 531). There is **no `book/src/concepts/reciprocal.md`** — `reciprocal` exists only as L1/L2/L3 *operator*
  chapters. This violates the dep-map's own restated invariant ("Dependency map of the concept pages in
  `book/src/concepts/`", line 204; "Every node is an on-disk concept page", line 502; "Every node below corresponds to
  an on-disk page", line 219). Critically, it is **the exact situation the report removed `axpby` for** ("`axpby`
  (concept page is at L2/L3 not concepts/)", line 654) — so the re-derivation applied its own dangling-node rule
  asymmetrically: it caught `axpby` but kept `reciprocal`. Not a build break (Mermaid labels aren't link targets), but a
  genuine cross-reference / consistency defect in the freshly re-derived graph.
- A second, milder item: the `krylov-step-record` node (CYCLE.md line 569) has no page of that name; the report
  explicitly flags it as a readability alias for the on-disk `krylov` page (lines 572-576). Acknowledged in-report, so
  lower-severity, but it is a second node whose label does not map to a file under the same stated invariant.

**edge-label-fidelity — pass.** The opportunistic `depends-on` (solid `-->`) vs `reference` (`-.->|ref|`) typing is a
light pass scoped correctly: the report explicitly disclaims it is NOT the meta-phase-owned graded-stack full typing
campaign (CYCLE.md lines 33-34, 216, 668-672). The typed edges I spot-checked are sensible (record pages as `ref`
leaves of the layer patterns that thread them). No edge-direction overreach into the authoritative campaign.

**plan-kind-consistency — pass.** Content shape matches the concepts-index / dep-map maintenance kind: dead-framing
strip + Mermaid re-derivation + light edge typing, all expressed as `edit:` proposed-changes blocks against the two
infra files. No mis-classification (this is not a firm operator / theme entry).

**skill-uptake-survey — pass (telemetry).** No skill invocation is referenced. This refresh's shape (dead-framing strip
+ graph re-derivation) does not strongly imply an existing skill; surfacing only — not blocking.

### Issues found

1. **Dangling `reciprocal` node in the re-derived graph** — `book/src/concepts/dependency-map.md` (new "Primitives +
   algorithms" sub-graph, CYCLE.md lines 525 + 531). `reciprocal` is referenced as a graph node and listed as a bare
   leaf primitive, but no `concepts/reciprocal.md` exists (it is an L1/L2/L3 operator chapter). This contradicts the
   dep-map's restated "every node is an on-disk concept page" invariant (lines 204, 502, 519, 219) and is the identical
   situation the report removed `axpby` for (line 654). Severity: medium (the report's own consistency rule, applied
   asymmetrically; build stays green but the graph self-description is false for this node). Candidate repair: remove the
   `reciprocal` node + its edge and drop it from the bare-leaf list, OR add an explicit "operator-chapter, not a concept
   page" annotation as was done for the `krylov-step-record` alias.

2. **Duplicate `## Methodology concepts (cross-layer)` heading post-integration** —
   `book/src/concepts/dependency-map.md`. The original `## Methodology concepts (cross-layer)` section + its Mermaid
   graph (on-disk lines 20-61) is NOT inside any `[old]` block, so it survives untouched. The new Edit-B (CYCLE.md
   lines 578-587) emits a SECOND `## Methodology concepts (cross-layer)` heading (graph-less, pointing "above" to the
   surviving one). Post-integration the file has two identically-titled sections. The "above" cross-reference is
   coherent (the real graph does survive above), and the report deliberately avoids duplicating the graph itself
   (lines 580-582) — but the duplicate heading is a structural smell (confusing for a reader; potential anchor
   collision). Severity: low/medium. Candidate repair: rename the new graph-less section (e.g. "Methodology concepts —
   see above") or fold its prose into the surviving section.

3. **Off-by-two count in self-description** — `book/src/concepts/index.md` / `dependency-map.md` framing and CYCLE.md
   Summary. "53 concept pages / 53 index-table links" should be "51" (53 files − `index.md` − `dependency-map.md`); the
   §Index table has 51 rows. Severity: low (cosmetic / accuracy of the document's own self-count; no link or build
   impact). Candidate repair: replace the "53 ... pages/links" phrasings with the file-vs-page-correct count, or qualify
   as "53 files (51 concept pages)".

## Repair

### Fixes attempted

- **Finding 1 — Dangling `reciprocal` node in the re-derived "Primitives + algorithms" graph** (cross-reference-integrity, medium).
  - **Decision**: repaired.
  - **Action**: In CYCLE.md Edit-B (`book/src/concepts/dependency-map.md`, the new "Primitives + algorithms" sub-graph) removed the `chebyshev-iteration --> reciprocal` edge and dropped `reciprocal` from the bare-leaf primitive list — consistent with how `axpby` / `allreduce_sum` / `copy` / `zero` / `extract-diagonal` / `spectrum-estimate` were handled. Added `reciprocal` to the Supporting-evidence "removed nodes" list (`reciprocal` (operator chapter is at L1/L2/L3 not concepts/)), and removed the stray `reciprocal` from the Supporting-evidence on-disk-pages enumeration (line 640) where it was listed as an existing page — it is not (`book/src/concepts/reciprocal.md` does not exist). The surviving `chebyshev --> reciprocal` at CYCLE.md line 377 is INSIDE an `[old]` block (the original L2 graph being deleted) and is correctly left untouched.
  - **Re-derivation check**: re-ran the full new-graph node set against `ls book/src/concepts/*.md`. After removing `reciprocal`, the only remaining non-file node is `krylov-step-record`, which is the in-report-acknowledged readability alias for the on-disk `krylov` page (CYCLE.md lines 572-576) — the critic ranked this lower-severity/acknowledged and did NOT list it among the findings to repair, so it is left as-is. No other dangling non-concept-page node survives.

- **Finding 2 — Duplicate `## Methodology concepts (cross-layer)` heading post-integration** (cross-reference-integrity / structure, low/medium).
  - **Decision**: repaired.
  - **Action**: Confirmed on-disk that the original `## Methodology concepts (cross-layer)` section (dependency-map.md lines 20-56) carries the authoritative methodology Mermaid graph + bullet list and is NOT inside any `[old]` block, so it survives integration. Edit-B's `[new]` emitted a second graph-less section of the same title. Renamed Edit-B's section heading to `## L4 calculus + feature spine (tracked elsewhere)` and rewrote its lead sentence to point UP to the surviving `## Methodology concepts (cross-layer)` section, so post-integration there is exactly ONE `## Methodology concepts (cross-layer)` heading (the surviving original). The genuinely-new content (L4-calculus design-artifact pointer + feature-spine note) is preserved under the renamed heading. This is the cleaner structure: the real graph + bullets live in one place, the new prose is no longer titled to collide.

- **Finding 3 — Off-by-two count in self-description** (citation-validity, low).
  - **Decision**: repaired.
  - **Action**: Corrected the count wherever it conflated FILES with concept-pages / index-table rows. CYCLE.md Summary (line 32): "53 on-disk concept files" → "51 on-disk concept pages — 53 files minus the two infra files `index.md` + `dependency-map.md`". Supporting evidence (line 638): "53 files ..." → "51 concept pages (53 files ... minus the two infra files ...; the §Index table's 51 rows are in sync ...)". Open-questions caveat (line 673): "in sync with the 53 on-disk pages" → "its 51 rows are already in sync with the 51 on-disk concept pages". The raw 53-FILE count is retained (correctly, parenthetically) as the denominator; the page/row count is now stated as 51 throughout.

### Unrepairable findings

None. All three critic findings were mechanical / surgical (node + edge removal from a proposed Mermaid block, a heading rename to break a title collision, a numeric self-count correction) and were applied in-place to CYCLE.md proposed-changes. No substantive authoring was required; the dead-framing strip and the overall re-derivation the critic judged sound were preserved untouched.

## Suggested resolution

`ready`. The report's two `warning` checks (citation-validity numeric drift; cross-reference-integrity dangling node + duplicate heading) are fully resolved by mechanical edits to the proposed-changes; the other six checks passed. Note for the integrator: the Supporting-evidence on-disk enumeration remains illustrative rather than exhaustive (it omits a couple of real pages such as `gmres` / `build-time-vs-run-time-stratification`) — pre-existing, not a count claim, and not flagged by the critic; left as-is to stay within repair authority. The proposed Mermaid graphs now contain exactly one non-file node (`krylov-step-record`, the documented `krylov` alias), which the report annotates in-line.
