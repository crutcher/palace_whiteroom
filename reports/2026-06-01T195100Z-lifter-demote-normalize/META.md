---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T20:09:29Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T20:18:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Demote `normalize` degenerate theme pair to in-line notes"

## Critique

### Checks run

**citation-validity — pass.** The report introduces no new L0 citations; it restates the existing chain. The single load-bearing anchor `palace/linalg/vector.hpp:262-270` (`linalg::Normalize`) was re-verified mechanically: `citecheck.py "palace/linalg/vector.hpp:262-270" --anchor 'Normalize'` → `[ok]`, anchor at lines 262, 264 within range, resolved to `reference/palace/palace/linalg/vector.hpp`. (Note: the report's §Supporting-evidence and Discipline-note invocation cite the anchor without the `reference/` prefix Palace convention drops; the prefixed `reference/palace/linalg/vector.hpp:262-270` form does NOT resolve — `[MISS]` — but that is the standard citation convention (paths relative to `reference/`), and the bare-path form the report uses is the correct one. No drift.) The partiality `MFEM_ASSERT(norm > 0.0)` at `:267` and in-place rescale at `:268` referenced in the Discipline note fall inside the verified 262-270 range. The report carries no `verified_against:` YAML block, so that sub-check is not applicable.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (it modifies existing operator/theme surface): it deletes two theme chapters and rewrites the §"Lowers to" sections of two operator entries into in-line §"Downward to" notes. The surface change is paired with an explicit rotation-quality argument (the deleted edges are degenerate identity-in-named-terms lowerings under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, which is the prescribed demotion trigger). The evidence for "degenerate" is the deleted themes' own rewrite-mapping tables, confirmed below. Not a pure rotation_claim-without-surface.

**rotation-quality — pass (inverse application — demotion of a non-rotation).** This check normally asserts an L_{n+1} form is strictly more compact than L_n. Here the proposal's CLAIM is the converse: the two edges carry NO rotation (no vocabulary shift), so the dedicated theme chapters are unjustified and demote to in-line notes. I verified the claim against both deleted files. Every mapping row in `L3-L2/normalize-body-identity.md` §"The rewrite" (lines ~110-117) and `L2-L1/normalize-leaf-identity.md` §"The rewrite" (lines ~113-121) reads "Identity" — same signature, same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, same partiality `x ≠ 0`, same element-type axis, same `consumes: nrm2 + scal` with no fold-parent. The L3 and L2 forms are literally character-identical in the body row. This is a textbook degenerate identity-in-named-terms lowering; demotion is the correct disposition, not a fabricated rotation.

**variant-axis-coverage — pass.** `normalize` has one variant axis (element-type real/complex, collapsed to one parameterised operator). The notes preserve the "single element-type variant axis" statement at both layers and the demotion does not hide any branch. The fold-vs-leaf axis (the one place a hidden branch could lurk) is explicitly scoped: `normalize` is a fused composite with codomain `(Scalar, Tensor[N])`, neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`, hence fork-INDEPENDENT / no fold-parent — established at `book/src/L2/normalize.md:34-39,100-107` and `book/src/L3/normalize.md:88-93` per the report, and reflected in the preserved note prose. No hidden combinations.

**cross-reference-integrity — pass.** The complete inbound-reference set for the two deleted slugs was independently re-enumerated: `grep -rn "normalize-body-identity\|normalize-leaf-identity" book/src/` returns exactly the two self-referencing (deleted) files plus 5 non-deleted files — `L2-L1/index.md`, `L3/index.md`, `L3-L2/index.md`, `L3/normalize.md`, `SUMMARY.md`. The report edits all 5, and every occurrence within `L3/normalize.md` (lines 6, 27, 107, 131, 149, 150) is individually addressed by edits 2a/2b/2d/2c/2e — no missed live link. Every `[old]` string was confirmed present and unique in its target file (substring `[old]` blocks for L3/index.md step-7 and L3-L2/index.md step-5c both count==1). All preserved cross-layer link targets resolve on disk: `L1-L0/normalize-mutation-rotation.md`, `L1-L0/nrm2-mutation-rotation.md`, `L1-L0/scal-mutation-rotation.md`, `L1/normalize.md`, `L3/nrm2.md`, `L3/scal.md`. The two `delete:` targets and their SUMMARY.md links are removed together, so no dangling link survives. Fence parity is clean: 36 fences = 18 balanced pairs, all proposed-changes blocks correctly headed. (Build-readiness firm-body-inside-fence guard: not applicable — no firm chapter body is authored in this report; it is a demotion, not a new firm entry.)

**edge-label-fidelity — pass.** Two edges in play. The L3>L2 edit set (2a-2e, §5) consistently discusses the L3→L2 hop and titles the note §"Downward to L2"; the L2>L1 edit set (3a-3b, §6) consistently discusses the L2→L1 hop and titles the note §"Downward to L1". No edge-label/prose mismatch. The transitive L3>L1 identity is correctly framed as the in-line composition of the two adjacent edges (no fabricated `L3-L1/` directory), per the cycle-012 non-adjacent convention.

**plan-kind-consistency — pass.** Declared kind is a lifter demotion (re-anchor degenerate theme pair to in-line notes). Content shape matches exactly: two deletes, two operator-entry rewrites, three index re-anchors, two SUMMARY removals — no new firm authoring, no rough-in placeholders, no operator-semantics changes. The "pure demotion, no collapse" discipline (standalone entries persist, no fold-collapse) is consistent with `normalize` being fold-parent-free.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report invokes `citecheck.py --anchor` for the load-bearing anchor (good). However, this report's shape — removing live links to deleted chapters and re-anchoring 5 inbound files — is exactly what the `proposed-changes-fence-encloses-full-body-guard` and the inbound-reference re-enumeration discipline target, and the report does not name a skill for the systematic inbound-link enumeration (it does the grep manually and reports it, which is sound, just not skill-attributed). Pure presence surfacing, not a defect.

### Issues found

No blocking issues. The following are observations, ordered by salience:

1. **(informational, no severity) Citation-path prefix in Discipline note / Supporting-evidence.** The report writes the load-bearing anchor as `palace/linalg/vector.hpp:262-270` (correct per the paths-relative-to-`reference/` convention); the `reference/palace/...`-prefixed form does NOT resolve. The report uses the correct bare-path form, so this is a non-issue — flagged only so the repairer/integrator does not "helpfully" add a `reference/` prefix that would break the anchor. Location: CYCLE.md §"Discipline notes" / §"Supporting evidence" (the citecheck invocation line).

2. **(low) §Evidence 2e collapses two bullets into one — confirm intent.** Edit 2e's `[old]` spans both L3/normalize.md:149 (the L2-floor bullet, which mentions "via the `normalize-body-identity` theme") AND :150 (the standalone `normalize-body-identity` theme bullet). The `[new]` emits a single bullet (the rewritten L2-floor bullet). This is correct — the now-deleted-theme bullet (:150) must be removed and the :149 bullet must drop its theme reference — but the report's prose at §2e only narrates "remove the two deleted-theme bullets," which could read as removing BOTH and leaving zero. The actual edit correctly preserves an L2-floor bullet (and the separate L1-anchor bullet at :151 already covers the chain). Verified the resulting §Evidence still carries the `book/src/L1/normalize.md` anchor bullet and the `normalize-mutation-rotation` bullet. No content lost; just a prose/edit-granularity mismatch worth a glance. Location: CYCLE.md §2e.

3. **(informational) D6/D7 tally boundary is clean.** Confirmed the boundary is non-colliding: D6 removes the L3-L2 theme-row (5a) + cohort bullet (5b) + the design-fork trailing clause (5c), and the L2-L1 theme-row (6a) + cohort bullet (6b) + descriptive token in the historical cohort-growth log (6c) — and explicitly does NOT touch any consolidated firm-count integer (5d, 6d defer to D7). I confirmed the L3-L2 cohort header tally at `L3-L2/index.md:66` ("firm 15 → 17") and the L2-L1 historical figure at `:78` ("firm 15 → 19") are left intact by the report's edits — D6 only edits the descriptive token in the :78 entry (6c), not the integer. No D6/D7 collision; the deferral is correctly scoped. The report's own §"Open questions" enumerates the two decrements D7 owns.

4. **(informational) Pre-existing `L2/normalize.md:24` "c044 sweep" staleness correctly left out-of-scope.** Confirmed `L2/normalize.md:24` and `:151` and `:162` reference the c044 sweep / "§Open-questions in this report" and the L3 §27/§131 "no interposed L2 entry" staleness. This cross-reference predates D6 and is genuinely orthogonal to the theme demotion (it concerns whether the c044 sweep updated the L3 floor-presence notes, not the theme files). Leaving it is correct — it is not D6's to fix under one-operator-per-dispatch / bounded-demotion scope; the report flags it for the planner. Note: D6's edit 2b/2c DOES rewrite the L3 §27/§131 prose into the new §"Downward to L2" note, which incidentally removes the "no interposed L2 entry" phrasing from the L3 side — so after integration the L2:24/:151/:162 back-references to "§27/§131 ... no interposed L2 entry" may point at prose that no longer reads that way. This is downstream of the pre-existing staleness the report already flagged, not a new defect D6 introduces, but the integrator/planner should be aware the L2-side back-references are now doubly stale (the c044 sweep target moved). Location: CYCLE.md §"Open questions / caveats" bullet 2; artifact `book/src/L2/normalize.md:24,151,162`.

5. **(verified-clean) Constituent boundary held.** The CRITICAL boundary is intact: no `nrm2`/`scal` entry or theme appears in any `delete:`/`edit:` target (grep over the proposed-changes fence headers returned NONE). The in-line notes describe only the `normalize` COMPOSITE's lowering; the `consumes: nrm2 + scal` frontmatter, law-6 factorisation, and §Dependencies of the constituents are untouched. The combinator re-expression is correctly left as HELD cycle-051 fold-family work. No issue.

6. **(verified-clean) Load-bearing-fact preservation.** The `vector.hpp:262-270` Normalize anchor is preserved (it lives in both `normalize` entries' §Evidence, which the report does not edit beyond removing the deleted-theme bullets), and re-verified resolvable. The substantive L1>L0 `normalize-mutation-rotation` pointer is preserved in both new notes. No load-bearing fact dropped.

## Repair

### Fixes attempted

- **Finding (issue 2, low)**: §Evidence edit 2e's prose says "remove the two deleted-theme bullets" but the actual `[new]` correctly emits ONE rewritten bullet — a prose/edit-granularity mismatch (no content lost).
  - **Decision**: repaired.
  - **Action**: Rewrote the §2e narration in `reports/2026-06-01T195100Z-lifter-demote-normalize/CYCLE.md` §"2. `book/src/L3/normalize.md`" so the prose matches the single-bullet `[new]`: it now states the `[old]` block spans both bullets (:149 L2-floor + :150 standalone theme), the `[new]` emits a single rewritten L2-floor bullet (deleting :150, re-anchoring :149), and the separate L1-anchor bullet at :151 is untouched. Trivial wording fix; the edit body itself was already correct and was not changed.

- **Finding (issue 1, informational)**: the integrator should NOT add a `reference/` prefix to the bare-path `palace/linalg/vector.hpp:262-270` citation — the bare form is the resolvable convention; the prefixed form `[MISS]`es.
  - **Decision**: not-needed (no edit; integrator note).
  - **Rationale**: the report already uses the correct bare-path form. No defect to repair. Surfaced for the integrator below so the bare form is preserved.

- **Finding (issue 4, informational)**: D6's rewrite of the L3 §27/§131 prose into the new §"Downward to L2" note removes the "no interposed L2 entry" phrasing that the `L2/normalize.md:24/:151/:162` back-references point at, making those back-references doubly stale.
  - **Decision**: not-needed (no edit; planner/integrator note).
  - **Rationale**: the `:24/:151/:162` staleness is **pre-existing** (the c044-sweep target the report itself already flagged as out-of-scope) and lives in `book/src/L2/normalize.md`, which the artifact-touching is not D6's bounded-demotion scope to re-author. NOT a new defect D6 introduces. Surfaced for the planner below.

### Unrepairable findings

None. The skill-uptake-survey warning is telemetry-only (the report does its inbound-reference enumeration soundly via grep, just not skill-attributed) and non-blocking; no repair authority applies. All 8 critic checks pass.

## Suggested resolution

`overall_status: ready`. Notes for the integrator/planner:

- **Citation prefix (integrator)**: keep the load-bearing anchor as the bare `palace/linalg/vector.hpp:262-270` form — do NOT add a `reference/` prefix; the prefixed form does not resolve under the paths-relative-to-`reference/` convention.
- **Cross-dispatch ownership (integrator)**: D6 OWNS the two deletions (`book/src/L3-L2/normalize-body-identity.md`, `book/src/L2-L1/normalize-leaf-identity.md`) and the `L2-L1/index.md:69` cohort-bullet removal (6b). Confirmed intact and correct in CYCLE.md (`delete:` blocks at §1; the `:69` bullet `[old]→[new]:` empty at §6b). Sibling D3 (#6b) / D4 (§5c) edits targeting the now-deleted `normalize-leaf-identity.md` are being dropped in their own repairs (the file goes away); D7's duplicate removal of the `:69` bullet should be dropped (D6 owns it).
- **Tally boundary (D7)**: D6 correctly defers both consolidated firm-theme-count decrements (one per lowering layer) to D7 (§5d, §6d); D6 edits only row/bullet/descriptive-token content, never a count integer. Clean boundary.
- **Doubly-stale back-references (planner)**: after integration, `book/src/L2/normalize.md:24/:151/:162` back-references to the L3 §27/§131 "no interposed L2 entry" phrasing point at prose D6 rewrote — these are now doubly stale on top of the pre-existing c044-sweep staleness the report already flagged. Route a cleanup of the `L2/normalize.md` §Context/back-reference staleness to the planner (out of D6's bounded-demotion scope).
