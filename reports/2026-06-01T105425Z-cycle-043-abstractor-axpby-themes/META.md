---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T112623Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "TWO adjacent thin-identity lowering themes for axpby — L2>L1 `axpby-leaf-identity` + L3>L2 `axpby-body-identity`"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the report returns `10 ok, 0 failing`. All load-bearing pinpoints verified with the tool as the authoritative line-map: `krylov-step-body-identity.md:97 --anchor 'axpby'` → ok (line 97 is the seven-primitive list, `axpby` named explicitly, framed L3-native-by-signature-shape — matches the report's structural justification exactly); `linear_combination.md:70 --anchor 'axpby'` → ok (line 70 is precisely the `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` row); `L1/axpby.md:16-18` (anchor `axpby` ok), `:42-53`/`:56-60`/`:72-77`/`:90-99` all in bounds (file has 99 lines). The focus-flagged L3 ranges all verify in bounds against the 152-line `L3/axpby.md`: `:30-32` (signature), `:51-65` (semantics + iteration-rotation marker — confirms "no iteration view, no sequential obstruction"), `:63-65` (the leaf-not-step-body marker), `:67-88` (the nine algebraic laws + four non-laws), `:103-110` (the two variant axes), `:116-120` (the §"Lowers to" the report flags as stale — confirmed: line 118 records straight-to-L1 lowering predating the L2 floor, so the staleness claim is accurate). Read-confirmed: the L1 and L3 entries each carry exactly **9** numbered laws and **4** "do not hold" non-laws, matching the report's "nine laws / four non-laws" assertion. No `verified_against:` YAML block is present (the report uses prose `## Verified-against` sections), so that round-trip sub-check is N/A. The `../../../scaffolding/decisions/axpby-as-primitive.md` relative link resolves to disk and is well-precedented (identical form at `L2/scal.md:49`, `L2/linear_combination.md:18`). One cosmetic imprecision (see Issues): the L2>L1 rewrite-table parenthetical enumeration at report line 147 lists "two identities" where laws 2/3/4 are three identities — but the headline count "nine" is correct, so this does not affect validity.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme — both proposals are `new:` lowering-theme chapters (plus two index `edit:` rows + two SUMMARY rows). New-surface authoring with full §Verified-against evidence chains on both sides; not a pure rotation-claim-without-surface shape. Passes.

**rotation-quality — pass.** Both themes claim **identity-in-form** rotations, explicitly, and justify them. This is the legitimate identity case (not a disguised renaming-only fail): the report does NOT claim the edges make the higher form more compact — it claims value-thread-isomorphism on a leaf primitive that is L3-native/L2-native by signature shape, with the genuine fusion-rotation work explicitly **deferred to the fold-parent** `linear-combination-fold-specialization` (L2>L1) or absent entirely (L3>L2, no element loop). The non-degeneracy is correctly surfaced: the arity-2 fused pass IS a two-term sum, so the summation-order non-law is non-degenerate (distinguished from the arity-1 `scal-fold-specialization` which is bit-exact) — this is a real, cited distinction, not a 1:1 mapping dressed up. The "no wrapper to rotate" framing for the L3>L2 edge (no `(op,K,s)`→`IterState`, no outer-loop dissolution) is the correct degenerate-maximal identity case versus the sibling `krylov-step-body-identity`. Passes.

**variant-axis-coverage — pass.** The two variant axes (element-type real|complex + scalar-promotion sub-axis) are explicitly covered and stated to be absorbed at construction at both layers (report L2>L1 rewrite-table row; L1/L3 `:72-77`/`:103-110` confirm the two-axis profile). The output-aliasing variant axis is explicitly scoped OUT to the fold-parent (`linear_combination.md` §Variant-axes axis 1) and to the L1>L0 mutation rotation — a clean explicit scope-out, not a hidden branch. The arity dispatch is explicitly the fold-parent's, not the leaf's. No hidden branch. Passes.

**cross-reference-integrity — warning.** All `[link]` targets resolve EXCEPT `book/src/L2/axpby.md`, which does not yet exist on disk — but this is by-design: it is the wave-1 D4 co-land that the dispatch states applies serially ahead of these themes (the report flags this explicitly in §Verified-against and §Open-questions). The sibling slugs (`dot-leaf-identity`, `scal-fold-specialization`, `dot-body-identity`, `scal-body-identity`, `krylov-step-body-identity`, `linear-combination-fold-specialization`) all resolve; the `axpby-leaf-identity` ↔ `axpby-body-identity` cross-links co-land. Fence parity is clean (12 fences = 6 balanced `new:`/`edit:` blocks; inner code is 4-space-indented, NO nested fences — the truncation defect is structurally avoided; the firm-body-inside-fence guard passes, both `## Status` + Signature + laws + Evidence sit inside their fences). **The warning is a registration-incompleteness:** both `L2-L1/index.md` and `L3-L2/index.md` carry TWO registration sites per theme — a top **index table** (rows where every existing sibling appears) AND a §"Vocabulary cohort" **bullet list**. The report's two index `edit:` blocks add ONLY the bullet-list item (matching the `scal-fold-specialization` / `scal-body-identity` bullet anchors at L2-L1:46 / L3-L2:35); no table-row edit is proposed for either index (grep confirms zero pipe-form rows in the report). The new themes would therefore land in the cohort bullet lists but be MISSING from the index tables where all 9+ siblings are listed. This is a structural-consistency gap, not a build-breaker (the table is markdown, not linkcheck-enforced).

**edge-label-fidelity — pass.** `axpby-leaf-identity` is labeled L2>L1 and its prose narrates the L2 leaf → L1 leaf rewrite forward (high→low), with LHS = L2, RHS = L1 throughout (§"L2 form (LHS)" / §"L1 form (RHS)" / §"The rewrite (L2 → L1)"). `axpby-body-identity` is labeled L3>L2 and narrates L3 → L2 forward (§"L3 form (LHS)" / §"L2 form (RHS)" / §"The rewrite (L3 → L2)"). Both edges narrate the exact labeled edge in the high→low direction; the reverse-direction lifting notes are correctly quarantined to §"Open questions / caveats" working-notes per the high→low discipline. No edge-label/prose mismatch. Passes.

**plan-kind-consistency — pass.** Declared kind is `firm` on both themes; content shape matches — identity-in-form edges between firm/firming endpoints, full §Verified-against chains, no rough-in placeholders, no speculative operators (both §"Speculative operators" sections correctly state "None"). The `firm` status is appropriate: the L1/L3 endpoints are firm (cycle-003/011), the L2 endpoint is firming-this-cycle (D4 co-land), and the rotation is the identity by construction. The design-presupposition note (leaf-floor (b) realization) is correctly framed as "not a status reduction." Consistent.

**skill-uptake-survey — pass (telemetry).** The report references its self-verification via `tools/citecheck/citecheck.py --anchor` on the `krylov-step-body-identity.md:97` anchor and `linear_combination.md:70` (§Supporting evidence). The relevant skill family (`verify-citation-range` / citecheck mechanical realization, `verify-rotation-citation`, `propose-rotation`) is implicitly exercised. No missing-skill-invocation gap surfaced.

### Issues found

1. **[cross-reference-integrity — warning] Index-table registration omitted for both new themes.** `book/src/L2-L1/index.md` and `book/src/L3-L2/index.md` each have a top index table (L2-L1 lines 11-26; L3-L2 lines 13-24) where every sibling theme is registered as a table row, in addition to the §"Vocabulary cohort" bullet list. The report's `edit:book/src/L2-L1/index.md` and `edit:book/src/L3-L2/index.md` blocks (CYCLE.md lines 596-604) add only the bullet-list item, not a table row. After integration, `axpby-leaf-identity` and `axpby-body-identity` will appear in the cohort bullet lists but be absent from the index tables — a registration-consistency gap versus every existing sibling. Severity: low/cosmetic (markdown table, not linkcheck-enforced; does not break the build), but it is a real per-index inconsistency. Candidate repair: add the matching table row to each index (mirroring the `scal-fold-specialization` table row at L2-L1:15 and the `scal-body-identity` table row at L3-L2:17).

2. **[citation-validity — cosmetic] L2>L1 rewrite-table parenthetical undercounts the law breakdown.** CYCLE.md line 147 enumerates the nine laws as "(subsumption / two identities / bilinearity / two distributions / scalar absorption / chained-collapse)" — that breakdown sums to 8, and "two identities" should be "three identities" (laws 2/3/4 are identity-in-α, identity-in-β, identity-in-both, per `L1/axpby.md:43-45` and `L3/axpby.md:72-74`). The headline count "nine algebraic laws" is correct and the L1/L3 sources confirm exactly nine, so this does not affect citation validity — it is a prose-breakdown imprecision only. Severity: cosmetic. Candidate repair: "two identities" → "three identities" in the parenthetical at line 147.

3. **[informational, not a defect] `book/src/L2/axpby.md` LHS endpoint not yet on disk.** Both themes' LHS/RHS reference `book/src/L2/axpby.md`, which does not exist at critique time. The report states it co-lands via the wave-1 D4 harvester, applied serially ahead of these themes. This is the standard co-land sequencing and is documented in §Verified-against and §Open-questions; flagged for the integrator's serial-ordering awareness, not as a report defect. If D4 does not land (or lands the fold-only realization), both themes' LHS would not resolve and the design-presupposition note (Applicability condition 1/2) becomes load-bearing — but that contingency is already surfaced for the batch-12 meta-phase OQ `dot-l2-leaf-floor-vs-fold-only-design`.

---
repaired_at: 2026-06-01T120000Z
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

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity — warning): Index-table registration omitted — both `L2-L1/index.md` and `L3-L2/index.md` carry TWO registration sites per theme (a top index TABLE row + a §"Vocabulary cohort" BULLET), and the report's two index `edit:` blocks added only the cohort bullet, leaving the new themes absent from the index tables where all 9+ siblings appear.
  - **Decision**: repaired.
  - **Action**: Read both index files on-disk to confirm the dual-registration structure and the exact sibling row format. Added one table-row `edit:` block per index to `reports/<id>/CYCLE.md` §Proposed-changes (preceding each existing cohort-bullet `edit:` block):
    - `edit:book/src/L2-L1/index.md` — a `[axpby-leaf-identity](./axpby-leaf-identity.md)` pipe-form row mirroring the `scal-fold-specialization` row (L2-L1:15) exactly: 4-column `| theme | L2 anchor | L1 anchor | status *(notes)* |`. Paired with its `scal-fold-specialization` sibling row so the integrator inserts it after the existing `scal-fold-specialization` table row.
    - `edit:book/src/L3-L2/index.md` — a `[`axpby-body-identity`](./axpby-body-identity.md)` pipe-form row mirroring the `scal-body-identity` row (L3-L2:17) exactly: 5-column `| Theme | LHS (L3) | RHS (L2) | Justification kind | Status |`. Paired with its `scal-body-identity` sibling row for the same sibling-anchored insertion.
  - The added rows are **D7's OWN rows only** — they register the two themes in the index tables. They do NOT touch the consolidated firm running-count tallies / cohort-growth-log totals in either Part's §"Working Notes" (D2 owns the consolidated tally this cycle, per the report's COUNT-OWNERSHIP open-question). Both new themes now land in BOTH the index table AND the cohort bullet list, matching every existing sibling and keeping D2's table-row-enumerating tally consistent.

- **Finding** (citation-validity — cosmetic): CYCLE.md:147 L2>L1 rewrite-table parenthetical undercounts the nine-law breakdown — "two identities" should be "three identities" (laws 2/3/4 are identity-in-α, identity-in-β, identity-in-both, per `L1/axpby.md:43-45` / `L3/axpby.md:72-74`); the breakdown otherwise summed to 8 against the correct headline count of 9.
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"The rewrite (L2 → L1)" table, line 147 — "two identities" → "three identities". Pure prose-breakdown correction; the headline count "nine" was already correct and is unchanged.

### Unrepairable findings

None. Both flagged findings were mechanical/surgical (one missing-registration-site mirror of an existing sibling row format; one cosmetic count correction). No substantive authoring required — the table-row content is a transcription of the report's own already-authored cohort-bullet prose into the sibling table format. The one informational note (the `book/src/L2/axpby.md` D4 co-land sequencing) is not a defect — it is standard wave-2 serial-ordering, already surfaced for the integrator.

## Suggested resolution

`ready`. Notes for the integrator:
- Apply D4 (`book/src/L2/axpby.md` harvester) serially ahead of this report, per the documented wave-2 co-land sequencing — both themes' L2 LHS/RHS endpoint depends on it.
- The two new index `edit:book/src/L2-L1/index.md` / `edit:book/src/L3-L2/index.md` table-row blocks insert after the existing `scal-fold-specialization` / `scal-body-identity` table rows (sibling-anchored, mirroring how the cohort-bullet edits are anchored).
- Do NOT increment the consolidated firm-count tallies in either Part's §"Working Notes" from this report — D2 owns those this cycle (report COUNT-OWNERSHIP OQ). The integrator reconciles the absolute counts (L2-L1: 15 firm + 1 pc → 16 firm + 1 with `axpby-leaf-identity`; L3-L2: 10 firm → 11 firm with `axpby-body-identity`) when D2's tally lands.
