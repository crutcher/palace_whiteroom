---
verifies: ../REPORT.md
critiqued_at: 2026-06-04T201500Z
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

# META: verification of CYCLE — graded-stack-scheme (P0-A)

## Critique

This report's deliverable is a NEW normative-but-non-authoritative methodology/convention page
(`book/src/methodology/graded-stack-scheme.md`) + a one-row SUMMARY wiring edit. It is NOT a
subject-DAG operator entry, theme, or feature-surface chapter — it is a methodology page that the
spec itself (`METHODOLOGY-GRADED-STACK.md` §2d) places OUTSIDE the subject DAG. Per the same logic
that no-ops the checklist for a `stub` / concept narrative page, the citation/surface/rotation/
variant-axis checks largely no-op here; the load-bearing checks are faithfulness to the
authoritative spec, internal consistency of the maturity→ladder table, parseability of the `edges:`
grammar, cross-reference integrity, and honest surfacing of the flagged P1-cost decision-fork.

### Checks run

**citation-validity — pass.** The report's citations are of two kinds and both check out. (1) The
spec-section pointers into `METHODOLOGY-GRADED-STACK.md` (§1a/§1f, §2a–§2d, §3, §4, §5, §8, §9) all
resolve to real sections that say what the report attributes to them — verified §1a (ladder),
§1b/§1f (well-foundedness + 2.5 sub-rank + obstruction-as-separate-kind), §2a (root set), §2c
(OWN-COMPOSITION falls out of the root marker), §2d (methodology pages outside the DAG), §3 (typed-
edge minimal binary + ignored `kind:`), §8 (lowering-verifier "theme ≤ min(endpoints)"), §9 (book
methodology update instructions). (2) The on-disk grounding citations in §Supporting evidence: every
cited file exists — `book/src/feature/{eigenmode,capacitance}.L4.md`, `book/src/concepts/{dot,
config-record}.md`, `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, `book/src/L1/index.md`
(the dep-map table at :107-144 is present and its "Dependencies" cells do mix slugs + prose
qualifiers + explicit non-dependencies, corroborating the "not parseable" claim). The on-disk counts
are independently reproduced: 357 `.md` files; 104 carry `firmness:`/`status:` (so 253 without); 10
carry `depends_on:` frontmatter; 54 carry `lowers_to:`/`lifts_from:`. All four counts match the
report exactly. No `verified_against:` block is emitted (not a lowering-verifier audit), so that
sub-check is inapplicable.

**surface-or-evidence — pass (no-op for methodology-page kind).** This page proposes no change to an
existing operator/theme surface and asserts no per-op algebraic/rotation claim — it is a convention
page. The record-definition sub-check is inapplicable and the report correctly says so in Open
questions (line 394-396): no operator signature names an undefined record; the only record-shaped
constructs introduced (`edges:`, `rank:`, the obstruction triple) are the page's OWN scheme objects,
defined in-place in §1/§2/§3 with fields, meaning, and surface form. Nothing is described only by use.

**rotation-quality — pass (not applicable to methodology-page kind).** The page rotates no L_n→L_{n+1}
representation; it documents an authoring convention. Mark pass by the same no-op rule that applies to
concept/stub pages.

**variant-axis-coverage — pass (not applicable to methodology-page kind).** No operator with orthogonal
variant axes is in scope. (As an aside, the page itself handles the one place a reader might expect a
hidden branch — the two surface forms of an edge, bare-string vs `{target:, kind:}` mapping — by
explicitly stating both are interchangeable and a bare string is read as `{target: <string>}`; that is
covered, not hidden.)

**cross-reference-integrity — pass.** The SUMMARY edit's `[old]` anchor block (CYCLE.md:345-347) matches
the live `book/src/SUMMARY.md:4-6` byte-for-byte (`# Methodology` / Overview / Goal & Flow), so the edit
will apply. The new page slug `book/src/methodology/graded-stack-scheme.md` sits in a real directory
(`book/src/methodology/` exists with `overview.md` + `goal-flow.md`). The forward/back links resolve as
designed: `goal-flow.md` exists and DOES carry the "if this contradicts a source, the source wins"
non-authoritative convention the report claims to mirror (goal-flow.md:3,11 confirmed); `resolution-
ladder.md` (D3's deliverable) is correctly NOT yet on disk, and the report handles this by anchoring its
SUMMARY edit on the stable `goal-flow.md` row and documenting the D3-coordination ordering in an
integrator note (CYCLE.md:355-361) — the parallel-safe "distinct rows under the same section" case. The
spec doc `METHODOLOGY-GRADED-STACK.md` exists. No dangling reference found.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried by this report.

**plan-kind-consistency — pass.** The declared kind is a methodology/convention page (the layer-intro-
author's book-methodology-page responsibility, `METHODOLOGY-GRADED-STACK.md` §8/§9). The content shape
matches: a normative authoring contract with a NON-AUTHORITATIVE banner, a ladder-mapping table, an
edges grammar, a root-marker spec, a migration mapping, and an authoring checklist. No firm-operator
apparatus is mis-applied; no rough-in placeholders masquerade as firm claims. The page correctly
carries NO `rank:`/`edges:` frontmatter itself (it is outside the DAG per §2d) and says so.

**skill-uptake-survey — pass (telemetry only).** No existing skill is squarely implied by "author the
canonical machine-readable graded-stack scheme page" — this is a one-off campaign deliverable (P0-A)
authored against the fresh spec, not a recurring procedure with a SKILL.md. The report references the
spec sections and the relevant CLAUDE.md conventions directly. No uptake gap to surface.

### Faithfulness + internal-consistency findings (the load-bearing checks for this kind)

I ran the five directed checks the dispatch called out. All clear; details below so the integrator can
see the verification was substantive, not nominal.

1. **Faithfulness to `METHODOLOGY-GRADED-STACK.md` (no contradiction of §1/§2/§3) — clean.** The ladder
   `roadmap_goal=0 < stub=1 < rough-in=2 < firm=3` (CYCLE.md:91) reproduces spec §1a exactly. The
   well-foundedness consequence "a firm node's every depends-on dep must be firm" (table row, :102 sub-
   rule :110-116) reproduces §1b's `rank(u) ≤ rank(v)` and its §1f "firm cannot rest on 2.5". The root
   set (5 drivers + boundary-mode + lifecycle spine-ROOT + 5 output products, :192-194) matches §2a; the
   `seed`-as-root-marker-NOT-a-ladder-rung and the `feature_root: seed` / `rank:` split (:198-210) mirror
   §2a's "seed does not collapse into the resolution ladder." The OWN-COMPOSITION-from-root-marker logic
   (:166-168, :206-210) mirrors §2c. The minimal-binary edge typing + ignored `kind:` (:139-188) mirrors
   §3. The methodology-page-outside-the-DAG self-exclusion (:66-70) mirrors §2d. No statement contradicts
   the authoritative doc.

2. **Maturity→ladder table internal consistency — clean.** Every live status value is mapped: `firm`,
   `partly-constructive` (2.5), `rough-in (test-coverage-bounded)` (2.5), `rough-in` (2), `stub` (1),
   `roadmap_goal` (0), `obstruction`/`partial-obstruction` (separate kind), and `seed` (parallel axis,
   not a ladder value). This is the full live vocabulary set (cross-checked against CLAUDE.md's status
   tiers). The 2.5 sub-rank rule (:110-116) is stated with the correct load-bearing consequence (firm
   cannot rest on 2.5; a 2.5 node may rest on 2.5 or firm). Obstruction is handled as a separate rankable
   kind with an explicit encoding triple, consistent with §1f.

3. **`edges:` grammar well-defined + parseable — clean.** I round-tripped all three proposed YAML forms
   through `yaml.safe_load`: the plain `depends-on`/`reference` block (:146-153), the mixed bare-string +
   `{target:, kind:}` mapping form (:176-182), and the obstruction triple (:126-130). All parse. The
   mixed list parses to `[dict, str]` exactly as the page asserts a linter must accept ("a linter treats
   a bare string as `{target: <string>}`", :184-185) — so D2's parser contract is unambiguous and the
   dual surface form is well-specified. The slug-resolution rule (repo-relative, no `book/src/` prefix,
   no `.md` suffix, :185-188) is concrete.

4. **Cross-reference integrity with D3's resolution-ladder page — clean.** Covered under the
   cross-reference-integrity check above: the report correctly does NOT depend on D3 having landed, anchors
   on the stable row, and names the intended final ordering (overview → goal-flow → resolution-ladder →
   graded-stack-scheme) in both the SUMMARY integrator note and the report Summary. The division of labor
   is clean — this page is the "how-to-write-it", resolution-ladder.md is the reader-facing "why".

5. **Migration-mapping completeness + honest decision-fork — clean and notably well-handled.** All three
   current representations are covered in the §4 table: (a) `depends_on:` frontmatter (10 files, the count
   I reproduced), (b) prose `## Dependencies` + index dep-map tables (the un-parseable bulk), (c) feature
   `composes:`/`l0_ground_truth:` frontmatter (24 files). The `lowers_to:`/`lifts_from:` frontmatter (54
   files, count reproduced) is explicitly folded into (a). The P1-cost decision-fork is surfaced HONESTLY,
   not silently pre-decided: §4 presents three options (a/b/c) with cost/loss tradeoffs, states a
   recommendation WITH rationale, explicitly flags that recommendation as "materially raises P1's cost",
   offers a bounded (a)-incremental compromise, and routes the call to the batch-30 meta-phase / human via
   a named OQ (`graded-stack-edge-home-fork-p1-cost`, :405-412). This is exactly the "flag, don't pre-
   decide" behavior the dispatch asked to verify.

### Issues found

No blocking issues. No warnings. Two non-blocking observations recorded for the integrator and the
batch-30 meta-phase — neither is a defect in this report (each is already self-flagged by the report in
Open questions), recorded here only so the downstream reader sees the critic confirmed they are honestly
surfaced rather than buried:

- **(observation, not a defect) `obstruction_resolution` is a scheme addition beyond the letter of the
  spec.** CYCLE.md:126-137 introduces `rank: obstruction` + `obstruction_kind:` + `obstruction_resolution:`
  as the concrete frontmatter encoding of "obstruction is a kind that is itself rankable." The spec §1f
  asserts the *concept* ("a kind that is itself rankable") but does NOT fix a frontmatter spelling. The
  report flags this honestly as its own addition (Open questions, :419-424) and routes the spelling choice
  to D2/batch-30. This is faithful (it does not contradict §1f — it concretizes it) and correctly framed as
  the authoring contract's prerogative. No action needed from this report; D2's parser and this page must
  stay in sync on the spelling, which the OQ already requests.

- **(observation, not a defect) the index-page / concept-page node-status carve-out is deferred, correctly.**
  §5 (:290-305) leaves "is an `L_n/index.md` itself a DAG node, and which `concepts/` pages are in-DAG vs
  outside-DAG" to a P1 sub-task + OQ (`graded-stack-index-and-concept-node-status`, :397-404) rather than
  forcing a one-pass answer. This is consistent with §2d (methodology/narrative pages outside the DAG;
  record-definition concept pages inside it) and the dispatch's explicit allowance not to force it. The
  carve-out is principled and the boundary criterion (record-definition pages are the `record` Kind) is
  stated.

All 8 checks pass; the four directed faithfulness/consistency/parseability/migration verifications are
clean; the page does not contradict the authoritative spec. Setting `overall_status: ready` per the
all-pass clean-report rule (no repairer will run).
