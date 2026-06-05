---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T073500Z
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

# META: verification of "typed `edges:` + reconciled typed graph for the concepts/ infra pair"

## Critique

This is a graded-stack P1 WAVE-2 infra-typing dispatch (cycle-103 D4): it types
`concepts/index.md` + `concepts/dependency-map.md` as `kind: navigational-container`
(reference-only, no `rank:`) and re-derives the dependency-map's Mermaid graph against
the WAVE-1 per-page typing. It is not a per-operator entry, a lowering theme, nor a
feature-surface composition root — it is a navigational-container / derived-view typing
pass, so several checks no-op by shape (noted per-check).

### Checks run

**citation-validity — pass.** The report's load-bearing pointers were spot-checked
against source. Scheme authority: `graded-stack-scheme.md` §2 (depends-on blocking vs
reference free) verified at `:101-115`; the §5 concept-page two-sub-case carve-out
(narrative/methodology = outside-DAG no `rank:`; record = DAG node) verified at the cited
`:244-252` region; §4(b) "authoritative edges move to per-chapter `edges:`; prose dep-map
becomes a derived view" verified at `:183`. The WAVE-1 sibling claims were verified
directly: D7 (`…071904Z-…-dofset-record-home`) does CREATE `concepts/dofset.md` with
`rank: firm` + `kind: record` and owns the SUMMARY.md concepts-row wiring (alpha between
`derived-view-hoisting` and `dot` — the exact position the report claims for its own index
table row, no overlap); D5 (`…072032Z-…-container-pages`) does flag `concepts/index` as the
alignment point and adopts the `kind: navigational-container` + reference-only + no-`rank:`
convention this report mirrors. No claim lacks support. No `verified_against:` block is
emitted by this report, so that sub-check is inapplicable.

**surface-or-evidence — pass.** This modifies surface (the two infra pages' frontmatter +
the dependency-map prose/graph) and its evidence is the per-page `edges:` blocks of the
WAVE-1 siblings it mirrors, which is the correct evidence shape for a derived-view
re-derivation (the map is explicitly a mirror of authoritative per-page frontmatter, not an
independent claim). The dependency-map re-derivation is faithful to the per-page edges:
each `-.->|ref| dofset` edge added (`state-stratification`, `build-time-vs-run-time-stratification`)
matches D7's dofset-page `reference:` block, which lists exactly those two concept consumers;
the `eliminate-bc-consumers` alias edge corresponds to D7's L1/L4 eliminate verb-pair
consumers and is documented as an alias label, not a file target. Record-definition sub-check:
the report NAMES the `dofset` record but does not define it — definition lives in D7's
`concepts/dofset.md` (a record-definition concept page, the ≥2-consumer home), which this
report merely references; that is the "already defined elsewhere and merely referenced here"
case, correctly NOT flagged.

**rotation-quality — pass (not applicable to this report-kind).** No algebraic/structural
rotation is asserted; this is an edge-typing / navigational-container reconciliation pass.
No-op.

**variant-axis-coverage — pass (not applicable).** The infra pages carry no orthogonal
variant axes. No-op.

**cross-reference-integrity — pass (LOAD-BEARING for this kind, verified mechanically).**
The 54-entry `reference:` block in `concepts/index.md` was checked target-by-target against
on-disk `book/src/concepts/*.md`: all resolve EXCEPT `dofset` (the single absent target),
which lands via D7's CREATE this same cycle. `concepts/dependency-map` (a self-reference)
and all 51 other concept pages exist. Every Mermaid node in the re-derived graph is an
on-disk concept page; the two non-file nodes (`krylov-step-record` → alias for `krylov`;
`eliminate-bc-consumers` → alias for the L1/L4 verb-pair) are explicitly documented as alias
labels in the prose, not links. All three `[old]` edit anchors were verified to match the
current file content byte-for-byte (the index H1, the `derived-view-hoisting | dot` table
rows, and the four dependency-map Mermaid blocks + edge-convention paragraph + records
paragraph). No `depends-on` edge is emitted on either infra page, so no rank-constraint or
dangling-blocking edge is created. The `dofset` member link and the `[dofset](./dofset.md)`
prose link are the ONLY cross-references whose target is not yet on disk — they resolve only
once D7's CREATE lands. See Issues for the integrator-ordering dependency.

**edge-label-fidelity — pass.** The reconciliation logic is correct per the WAVE-1 typing
and the scheme. The load-bearing fact — a non-record concept page (narrative / methodology /
layer-pattern Kind) sits outside the subject DAG (scheme §5, verified) and emits ONLY
`reference` edges, so the c101 solid `-->` (depends-on) edges become `-.->|ref|` — is faithful
to scheme §5 and to the WAVE-1 D1/D3 finding (16 + 12 pages, all reference-only, 0 depends-on).
The record pages are correctly typed as DAG-node leaves whose only `depends-on` edges are
`kind: cites-evidence` to raw L0 source (off this concept-graph). Each re-typed sub-graph
preserves the c101 node/edge set exactly while flipping `-->` to `-.->|ref|`; the only
additions are the three new `dofset` edges (matching D7) and the two `config-record`/`dofset`
build-time edges. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind (navigational-container infra typing + derived-view
re-derivation) matches the content shape exactly: no `rank:`, reference-only `edges:`, prose
re-derivation of a derived mirror. No firm/rough-in placeholders, no mis-classification. The
rank-invariant check (graded-stack add-9) no-ops because neither infra page is a ranked node;
the reachability check (add-10) is the subject of a correctly-routed OQ rather than a defect
(see Issues).

**skill-uptake-survey — pass (telemetry).** No graded-stack-edge-typing skill is referenced;
the WAVE-1/WAVE-2 typed-edge campaign is meta-phase-driven against `graded-stack-scheme.md`
rather than a promoted skill, and the report cites the scheme + the linter source directly.
Non-blocking; surfaced only.

### Issues found

No blocking issues. Three items are surfaced as integration-context / telemetry (none is a
report defect):

1. **INTEGRATOR-ORDERING DEPENDENCY (cross-report integration risk — the key risk this cycle).**
   `CYCLE.md` §Proposed-changes (1) adds the `concepts/index.md` `reference:` block entry
   `- concepts/dofset` AND the `| [dofset](./dofset.md) | record |` member-table row, and
   §Proposed-changes (2) adds the `[`dofset`](./dofset.md)` prose link in the dependency-map
   records paragraph. All three resolve to `book/src/concepts/dofset.md`, which **does not yet
   exist on disk** — it is CREATED by sibling report D7
   (`…071904Z-layer-intro-author-dofset-record-home`) this same cycle. **D7's CREATE of
   `dofset.md` MUST be applied before (or in the same staging step as) this report's index
   row + dependency-map prose link, or the `[dofset](./dofset.md)` link dangles and
   `linkcheck2` hard-fails the build.** The report itself flags this prominently
   (§Supporting-evidence "Build-safety" and §Open-questions), so it is correctly disclosed —
   recorded here for the integrator-per-report serial ordering, not as a report fault. (The
   frontmatter `- concepts/dofset` `reference:` entry is frontmatter-stripped by mdBook so does
   not itself trip linkcheck2; the table-row + prose Markdown links are what require D7 first.)

2. **OQ `dependency-map-not-recognized-outside-dag-by-linter` — legitimate routing, NOT
   fixable here.** Verified against `tools/graded-stack-lint/graded_stack_lint.py:637-647`:
   `is_likely_outside_dag` matches `concepts/index` via the `("/index", "index")` suffix rule
   (so the index flips cleanly from untyped-WARNING to typed-outside-DAG), but
   `concepts/dependency-map` matches NONE of `OUTSIDE_DAG_PREFIXES`, the index suffixes, or
   `FEATURE_NON_COLUMN` — so once typed-and-unreachable it is reported as detritus (the report
   correctly notes this is cosmetic lint noise, not a rank-violation failure / exit-code trip).
   The fix (extend `is_likely_outside_dag` to honor `kind: navigational-container`) is a `tools/`
   edit, which is meta-phase write-authority — out of this dispatch's scope. Routing to
   meta-phase is correct; the report should NOT have fixed it here. Same gap class D5 flagged
   for the 23 group-intros (one fix resolves both).

3. **OQ `graded-stack-six-record-concept-pages-need-frontmatter` — legitimate routing.**
   Confirmed: `krylov`, `op-params`, `sim-state`, `step-outputs`, `prev-carry`, `solve-result`
   each currently start directly at their `# <Name>` H1 with no frontmatter (only `config-record`
   (D2) and `dofset` (D7) carry on-disk `rank:`+`edges:` this cycle). Their node-status is settled
   by scheme §5 (record ⇒ DAG node); only the on-disk frontmatter is pending. The report correctly
   does NOT author that frontmatter (those are six separate record pages, outside the infra-pair
   scope — a follow-on harvester/layer-intro-author tranche). The dependency-map prose now states
   this explicitly. Routing is appropriate; not a defect.

   (The report additionally surfaces the inherited `config-record-reachability-gap` and a
   prospective `dofset-reachability-needs-uses-record-edge` — both correctly scoped OUT, since
   feature-column `kind: uses-record depends-on` edges are not this report's pages. These are
   accurately characterized: under reachability GC a record reached only by `reference` from a
   root is unreachable garbage until a consuming column adds a blocking `depends-on`. No action
   for this report.)
