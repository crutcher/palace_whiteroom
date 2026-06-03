---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T164500Z
critic_version: 1
report_kind: feature-surface (output-product composition-root; cohort-owner of shared index + SUMMARY)
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T171500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of energy-fields output-product feature column (+ shared-surface cohort owner)

## Critique

This is a FEATURE-SURFACE composition-root report (output-product leaf column, `status: seed`),
so the adapted checks apply: rotation-quality and variant-axis-coverage are formal no-ops, the
surface-or-evidence shape is L0-driver-range + constituent down-links, and cross-reference-integrity
is load-bearing (the column's value IS its down-links + the cohort-owner shared-surface edits).

### Checks run

**citation-validity — pass.** Spot-verified the load-bearing L0 anchors on-disk via palace-codemap
`read_range`:
- `postoperator.cpp:1021` = `MeasureDomainFieldEnergy()` def signature ✓; `:1036` electric loop ✓,
  `:1038` `GetDomainElectricFieldEnergy` ✓, `:1039` participation ratio ✓, `:1040-1041` `DomainData`
  emit ✓.
- `:1055` `HasBGridFunction` guard ✓, `:1057` field `A?*A:*B` ✓, `:1058` total ✓, `:1061` magnetic
  loop ✓, `:1063` `GetDomainMagneticFieldEnergy` ✓, `:1064` ratio ✓, `:1065-1066` emit ✓.
- `domainpostoperator.cpp:255-275` = `GetDomainElectricFieldEnergy` body returning `0.5 * dot` ✓
  (the `½⟨E, M_idx E⟩` SPD form, `Mult` + `LocalDot` + imag + `GlobalSum` + `0.5*dot`).
- `postoperatorcsv.hpp:74-79` = `struct DomainData { int idx; double energy; double participation_ratio; };` ✓ exact.

The report's claimed catch of a uniform +1 codemap drift (citation self-verification §, CYCLE.md:692-696)
is CORRECT: the on-disk numbers the chapters use (loops `:1036`/`:1061`, ratios `:1039`/`:1064`,
emits `:1040-1041`/`:1065-1066`) are the true line-map — I confirmed them directly. The chapters
cite the corrected (on-disk) numbers throughout, so no drift survives into the artifact. The report
also correctly notes the magnetic-block guard tests the *total* `energy` (`std::abs(energy)`) not
`energy_i` — that is the source's own asymmetry (`:1064` reads `std::abs(energy) > 0.0`), faithfully
recorded rather than silently "fixed" (CYCLE.md:466-468). Citations point to real, in-range
locations.

**surface-or-evidence — pass.** Adapted form for feature-surface: the composition is supported by
(a) the L0 driver range `postoperator.cpp:1021-1077` (cited and verified) and (b) the constituent
down-links. The constituents' maturity claims are accurate on-disk: `participation_ratio.md` is
`firmness: firm` ✓; `matrix-weighted-norm.md` is `rough-in (test-coverage-bounded)` ✓. The `seed`
status is correctly justified — at least one composed constituent is non-firm (matrix-weighted-norm
rough-in + the freshly-minted `domain_energy_reduce` rough-in), and the chapter states the
"promote-past-seed only once ALL constituents firm" rule consistently across L4/L1/L0.
Record-definition sub-check: the `## Record definition` section for `Measurement::DomainData`
(energy-fields.L4.md) defines it in itself — fields + types + meaning table, stratum
(run-time/measurement, with `idx` mirroring construction-time config), and L0 source home
(`postoperatorcsv.hpp:74-79`) — and is correctly NOT duplicated at L1 (which links up to the single
home). This satisfies the record-definition obligation; the single-vs-cross-cutting judgment is
defensibly routed (OQ `record-DomainData-needs-definition-home` filed for the CSV-writer 2nd-consumer
case). On the verb-warrant question: the new `domain_energy_reduce` is defensibly justified (it
factors per-domain restriction + ratio into one fold over the firm `participation_ratio`, the rank-1
per-domain-table sibling of `eigenfreq_qfactor_reduce`, NOT a `gram_reduce` family-PAIR; the report
honors the c074 D6 do-NOT-over-unify guard) — but the report itself correctly flags this as
author-judgment needing a combinator-miner 2nd witness (OQ `domain_energy_reduce-l4-verb-needs-authoring`).
That is the right disposition; not a fail.

**rotation-quality — pass (not applicable to feature-surface kind).** A composition-root recomposes
already-firm/rough-in vocabulary outward; it asserts no new per-op algebraic/reduction rotation of
its own. Formal no-op.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The feature chapter has
no variant axes of its own. Note in passing: the report does explicitly cover the one variant it
touches — the electric/magnetic field-kind axis (the reduction "runs twice," with the E-only/H-only
`else` zero-`DomainData` branches witnessed at `:1044-1053`/`:1069-1078`) — so even under the
unadapted check there is no hidden branch.

**cross-reference-integrity — warning (LOAD-BEARING for this kind + cohort-owner).** The shared-surface
edits are mechanically sound: all five `[old]` anchors match the on-disk files exactly
(`feature/index.md` matrix lines 32-33 + 40-41, output-product.md lines 8 + 12, SUMMARY.md lines
13-14 + 35-36), all alpha positions are correct (energy-fields between eigenfrequency-qfactor and
inductance; boundary-mode alpha-FIRST before driven), and within-column high→low (L4→L1→L0) is
preserved in both SUMMARY blocks. The constituent up-links resolve on-disk
(`participation_ratio.md`, `matrix-weighted-norm.md`, `gram_reduce.md`, `eigenfreq_qfactor_reduce.md`
all exist). HOWEVER one finding (see Issue 1) blocks a clean pass: the chapter BODY uses live
Markdown links to `../L4/domain_energy_reduce.md`, a file that does NOT exist on disk, in 10 places —
which is a hard `linkcheck2` build-break under the `rough-in-forward-reference-must-be-plain-text-not-live-link`
convention, AND contradicts the report's own plain-text framing.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried (composition
roots link DOWN to constituents, not across a lowering edge). The "Lifts to" section in the L0
chapter narrates L0→L1/L4 lift direction consistently with its links.

**plan-kind-consistency — pass.** The content shape is a feature-surface composition-root and lands
in its by-kind grouping (output-product, alpha-within-kind). The uniform `status: seed` token (no
`(composition-root)` qualifier) is correct per the codified convention. The driver-AGNOSTIC nature of
energy-fields (it breaks the 1:1 output-product↔driver cross-link convention) is correctly routed as
an OQ (`energy-fields-driver-agnostic-not-per-driver-stage3`) rather than forced into a single
reciprocal driver up-link — the right disposition.

**skill-uptake-survey — pass (telemetry only).** Not blocking. Observation: the
`proposed-changes-fence-encloses-full-body-guard` skill is N/A (the chapter bodies ARE inside their
`new:` fences — fence parity is balanced). The live-link-to-missing-target defect (Issue 1) is the
kind of thing the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill governs in reverse
(downgrade-live-link-when-target-absent); no skill was invoked for the forward-reference link
discipline, which would have caught Issue 1 at authoring time.

### Issues found

**Issue 1 (cross-reference-integrity, build-break risk + internal contradiction) — the column body
uses LIVE Markdown links to a non-existent file.** `book/src/feature/energy-fields.{L4,L1,L0}.md`
reference `[`domain_energy_reduce`](../L4/domain_energy_reduce.md)` as a live link in 10 places
(CYCLE.md:122, 161, 202, 233, 244, 266, 345, 375, 402, 499 — i.e. L4 body ×6, L1 body ×2, L0 body
×1, record-def ×1). The target `book/src/L4/domain_energy_reduce.md` does NOT exist on disk (verified:
the verb is freshly minted this cycle, no anchor file authored). A live link to a missing file is a
hard `linkcheck2` build error (friction-ledger `rough-in-forward-reference-must-be-plain-text-not-live-link`).
This also CONTRADICTS the report's own framing: CYCLE.md:88-89 states "the L4 chapter's down-link
uses plain-text per the rough-in-rows-must-be-plain-text convention since the anchor file does not
yet exist," and the constituent down-link tables (CYCLE.md:255 L4, and the L1/L0 tables) DO use
plain-text `domain_energy_reduce *(rough-in; no anchor yet)*` correctly — but the prose bodies do not.
Severity: build-break (would fail `cargo make book` linkcheck). Two resolution paths exist (the
repairer/integrator chooses): (a) demote all 10 body links to plain-text/inline-code per the
convention; OR (b) the integrator materializes a `domain_energy_reduce` STUB under the "Integration
may materialize implied components as stubs" directive — the bar is clearly met (10 converging
references + the OQ `domain_energy_reduce-l4-verb-needs-authoring`), which would make the links
resolve. Either is acceptable; the defect is that the report ships build-breaking links as-is.

**Issue 2 (cross-reference-integrity, minor stale prose) — `output-product.md` cohort-summary line
not updated for the 2nd rank-1 verb.** `book/src/feature/output-product.md:5` reads "The cohort spans
**three reduction shapes**, one reduction verb each." Edit 4 adds the energy-fields bullet (correctly,
as the per-domain sibling within the *same* rank-1 scalar-table shape — so "three reduction shapes"
stays accurate), but "**one reduction verb each**" becomes inaccurate: the rank-1 scalar-table shape
now carries TWO verbs (`eigenfreq_qfactor_reduce` per-mode + `domain_energy_reduce` per-domain). The
report does not touch line 5. Severity: minor (stale count-prose, not a broken link). Note the
parallel prose in `feature/index.md:46` ("three reduction shapes, one reduction verb each") is also
left stale by the same omission — Edit 2 updates the bullet list + the "All three → All five" tally
but not the "one reduction verb each" clause.

**Issue 3 (informational, not a defect) — boundary-mode SUMMARY/matrix links point at files D2
authors this cycle.** Edits 1 + 5 add `boundary-mode.{L4,L1,L0}` rows to the index matrix and SUMMARY
on D2's behalf (cohort-owner duty), but those 3 files do not exist on disk yet (D2's column authoring
creates them). This is the documented cohort-owner / parallel-blind-shared-index coordination pattern
(c074/c075 precedent) and is correct BY DESIGN — flagged only so the integrator confirms D2's
boundary-mode report lands in the SAME integration batch; if D2 does not land, the boundary-mode
matrix/SUMMARY rows would be dangling links (a linkcheck break). This is an integration-ordering
dependency, not a defect in THIS report. (The energy-fields rows this report owns DO have their 3
files authored in this same report's proposed-changes, so they are self-consistent.)

## Repair

### Fixes attempted

- **Finding 1 (warning, cross-reference-integrity — the load-bearing fix): dead live-links to an unauthored verb.** The L4/L1/L0 chapter bodies used live Markdown links `[`domain_energy_reduce`](../L4/domain_energy_reduce.md)` in 10 places, but `book/src/L4/domain_energy_reduce.md` does NOT exist on disk (the verb was minted as a `rough-in` forward-reference this cycle, not authored). A live link to a missing file is a hard `linkcheck2` build break (friction `rough-in-forward-reference-must-be-plain-text-not-live-link`); it also internally contradicted the report's own plain-text framing (CYCLE.md:88-89) and the constituent down-link tables (which already correctly used plain-text).
  - **Decision: repaired.** Mechanical/surgical — the convention's build-safe fallback (demote-to-plain-text), no content authored.
  - **Action:** Demoted all 10 chapter-body live-link occurrences of `[`domain_energy_reduce`](../L4/domain_energy_reduce.md)` to plain-text code-spans `` `domain_energy_reduce` `` (CYCLE.md:122, 161, 202, 233, 244, 266, 345, 375, 402, 499 — L4 body ×6, L1 body ×2, L0 body ×1, record-def ×1). The surrounding prose describing what the verb does is left intact; only the link form changed. Verified file absence on disk (`book/src/L4/` holds only `eigenfreq_qfactor_reduce.md` / `gram_reduce.md` / `sparameter_reduce.md`). The 3 remaining `domain_energy_reduce.md` mentions (CYCLE.md:87 supporting-evidence code-span, :107 YAML `composes:` frontmatter value, :623 OQ code-span) are NOT Markdown links and are build-safe — left as-is. This clears the build break.
  - **Follow-up note:** authoring the full `book/src/L4/domain_energy_reduce.md` `rough-in` verb (so these references can be re-upgraded to live links per the on-disk→live-link upgrade discipline) is a clean LATER-cycle plan item for a harvester / combinator-miner — and is exactly the 2nd-witness verb-warrant probe the report already flagged (OQ `domain_energy_reduce-l4-verb-needs-authoring`, CYCLE.md:617-630). Not done here (would be substantive authoring, out of repair scope). At that point the integrator's stub-materialization directive is also an option, but plain-text is the correct build-safe state for now.

- **Finding 2 (minor, stale prose): "one reduction verb each".** Both `book/src/feature/output-product.md:5` ("The cohort spans **three reduction shapes**, one reduction verb each") and `book/src/feature/index.md:46` ("The **output-product cohort** spans **three reduction shapes**, one reduction verb each") carry stale "one reduction verb each" prose — the rank-1 per-element scalar-table shape now carries 2 verbs (`eigenfreq_qfactor_reduce` per-mode + `domain_energy_reduce` per-domain). NOTE: the "three reduction shapes" count itself stays accurate (energy-fields is a sibling WITHIN the existing rank-1 scalar-table shape, not a 4th shape) — only the "one reduction verb each" clause is stale.
  - **Decision: not-needed (flagged for integrator).** Verified on-disk: neither line 5 of `output-product.md` nor line 46 of `index.md` appears in any `[old]` anchor of this report's proposed-changes blocks (Edit 2's anchors begin at the eigenfrequency-qfactor bullet + the "All three → All five" tally; Edit 4's anchors are `output-product.md:8` and `:12`). The stale clauses live in EXISTING on-disk file content NOT edited by this report. The repairer's authority is in-place edits to CYCLE.md / co-located report docs only; it does not write `book/`, and the clause is not present in a proposed-changes `[old]` block to surgically amend. Per the critic's own instruction ("if the stale prose is in an existing on-disk file NOT edited by this report, flag it for the integrator instead of editing out-of-scope"), this is flagged for the integrator (below) rather than repaired.

- **Finding 3 (informational): boundary-mode index/SUMMARY rows point at D2-authored files (cohort-owner pattern).** Not a defect, no action — documented integration-ordering dependency (see Suggested resolution).

### Unrepairable findings

None block a clean build. Finding 2 is a `not-needed`-routed minor stale-prose touch deferred to the integrator (it is a 2-clause in-place edit to existing on-disk files, mechanically trivial but outside the repairer's write-partition); it does NOT gate `ready` because it is cosmetic count-prose, not a build break or a content error. No `unrepairable` (substantive-authoring) findings.

## Suggested resolution

`overall_status: ready`. The single load-bearing build-break (Finding 1, dead live-links to the unauthored `domain_energy_reduce` verb) is repaired — all 10 chapter-body links demoted to build-safe plain-text code-spans, which clears the `linkcheck2` break. All other checks pass or no-op.

Two carry-along notes for the integrator (neither gates `ready`):

1. **Finding 2 — stale "one reduction verb each" (minor, out of repairer write-scope).** When applying this report, also make the trivial in-place edit to the two existing on-disk files NOT in this report's proposed-changes:
   - `book/src/feature/output-product.md:5` — change "one reduction verb each" to reflect the rank-1 shape now carrying two verbs (`eigenfreq_qfactor_reduce` per-mode + `domain_energy_reduce` per-domain). Keep "three reduction shapes" (still accurate — energy-fields is a sibling within the rank-1 shape).
   - `book/src/feature/index.md:46` — same clause, same fix.

2. **Finding 3 — integration-ordering dependency (by design).** Edits 1 + 5 add `boundary-mode.{L4,L1,L0}` rows to `feature/index.md` matrix + `SUMMARY.md` on D2's behalf (the cohort-owner / parallel-blind-shared-index pattern, c074/c075 precedent). Those 3 boundary-mode files are authored by D2's report, NOT this one. Confirm D2's boundary-mode report lands in the SAME integration batch; otherwise those rows become dangling links (a `linkcheck2` break). The energy-fields rows this report owns DO have their 3 files authored in this same report's proposed-changes, so the energy-fields surface is self-consistent regardless.

3. **Later-cycle plan item (informational).** Author `book/src/L4/domain_energy_reduce.md` (`rough-in`) via a harvester / combinator-miner, then re-upgrade the 10 demoted plain-text references back to live links — the 2nd-witness verb-warrant probe already filed as OQ `domain_energy_reduce-l4-verb-needs-authoring`.
