---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T000000Z
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
repaired_at: 2026-06-01T000000Z
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

# META: verification of cycle-043 abstractor `axpy` thin-identity themes (`axpy-leaf-identity` L2>L1 + `axpy-body-identity` L3>L2)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` returns `11 ok, 0 failing`. Every load-bearing pinpoint was adjudicated by the tool, not hand-asserted: the L0 anchors all resolve and `--anchor`-confirm (`vector.cpp:702-712` anchor `AXPY`@702 + `1.0`@704; `:276-311` `AXPY`@276-281; `vector.hpp:115-118` `AXPY`@116-118; `:305-307` `AXPY`@307; the scalar-promotion forwarding overload `vector.cpp:714-718` `AXPY`@715,717). The two cross-layer load-bearing anchors are correct in both bounds AND meaning: `L2/linear_combination.md:69` reads verbatim `axpy(α, x, y) = linear_combination [(α, x), (1, y)]  -- second coeff fixed to 1` (exactly the fold-membership claim, including the fixed-1 second coefficient), and `krylov-step-body-identity.md:97` (anchor `L3-native`@97) names the seven BLAS-1 primitives — `axpy` among them — as "L3-native because its signature has no per-element loop visible," which is precisely the structural justification the report leans on. Spot-checked L1/L3 pinpoints (`L1/axpy.md:16-18,77-83`; `L3/axpy.md:30-32,112-116`) are in-range and on-anchor. No `verified_against:` YAML block is present (the report uses a prose §Verified-against section, not a fenced YAML payload), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Both proposals are `new:` theme files (not refinements of existing operator/theme surface), each carrying full structural surface (signature, rewrite table, applicability conditions, justification kind, verified-against) plus rotation evidence. This is new-theme authoring, not a pure rotation_claim backfill; the surface-or-evidence gate is satisfied by construction. The one `edit:` touches (index rows + SUMMARY) are registration surface for the new files.

**rotation-quality — pass (identity-in-form, correctly typed).** These are deliberately identity-in-form edges, NOT compaction rotations, and the report does not over-claim a rotation that isn't there. The standard rotation-quality bar ("strictly more compact / more abstract") is the bar for a *claimed* rotation; an identity-in-form edge is the legitimate degenerate case explicitly licensed by the CLAUDE.md "Identity-lowerings still require both L levels" invariant. The report justifies the identity correctly on both edges: (L2>L1) the leaf carries no leaf-unique fusion because all fusion — arity-dispatch, `axpy`-vs-`axpby` sub-selection, pinned summation-order — is the fold-parent `linear-combination-fold-specialization`'s job, so the leaf's own edge is a no-op; (L3>L2) the body is identity-in-form with *no wrapper to rotate* because `axpy` is a leaf field operation, not a step body — explicitly contrasted with the sibling `krylov-step-body-identity`'s two wrapper adjustments (`(op,K,s)`→`IterState` consolidation + outer-loop dissolution), neither of which has an `axpy` analog. The mapping tables are total-and-bijective on the leaf. This is the "1:1 mapping = fail" carve-out done right: the report does not dress a renaming up as a rotation; it correctly classifies the edge as identity and defers the genuine fusion rotation to the named fold-parent. Pass.

**variant-axis-coverage — pass.** The report identifies the variant axes (element-type real/complex; the real-`α`-against-complex scalar-promotion sub-axis via `concepts/scalar-promotion` + the `vector.cpp:714-718` forwarding overload) and explicitly scopes them as inherited-unchanged from the firm L1 leaf, absorbed at construction, "not a distinct lowering sub-pattern" (Applicability condition 4 in the L2>L1 theme). The output-aliasing axis is named as the fold's axis, deferred to the fold-parent. No hidden branch: the `α == 1.0` fast-path is correctly called out as a transparent constant-folding trick already erased at L1, not a load-bearing variant. The fixed-1 `y`-coefficient (the load-bearing distinction from `axpby`) is preserved across both edges and stated in the mapping tables.

**cross-reference-integrity — pass.** Every `[link]` target resolves on disk: `L1/axpy.md`, `L3/axpy.md`, `L2/linear_combination.md`, `L2-L1/scal-fold-specialization.md`, `L3-L2/scal-body-identity.md`, `L2-L1/dot-leaf-identity.md`, `L3-L2/dot-body-identity.md`, `L1-L0/axpby-mutation-rotation.md`, `L2-L1/linear-combination-fold-specialization.md`, `L3-L2/krylov-step-body-identity.md`, `concepts/scalar-promotion.md`, all three index files, and `scaffolding/decisions/axpby-as-primitive.md` all present. `L2/axpy.md` is referenced as the LHS/RHS endpoint but is correctly absent on disk (co-lands this cycle as wave-1 D3) — the report flags this serial-sequencing dependency explicitly in frontmatter, §Verified-against, and §Open-questions; the two new files cross-link each other and both will exist post-integration. The index/SUMMARY insertion anchors all exist exactly as the `edit:` blocks expect (`dot-leaf-identity` row @L2-L1/index:17; `scal-body-identity` row @L3-L2/index:17; SUMMARY lines 43-44 and 80-81 contiguous). Build-readiness fence guard: not a firm-operator-body case (these are themes, not L_n operator entries with `## Status`+Signature+Algebraic-laws+Evidence apparatus); the firm-body-inside-fence concern does not apply, and the fence enumeration (below) confirms balanced parity regardless.

**edge-label-fidelity — pass.** Both edges are labeled and narrated in the correct forward (high→low) direction. `axpy-leaf-identity` is labeled L2>L1 and its prose narrates L2 LHS → L1 RHS (§"The rewrite (L2 → L1)", LHS=`L2/axpy`, RHS=`L1/axpy`). `axpy-body-identity` is labeled L3>L2 and narrates L3 LHS → L2 RHS (§"The rewrite (L3 → L2)", LHS=`L3/axpy`, RHS=`L2/axpy`). No edge-label/prose mismatch. The transitive non-adjacent L3>L1 identity is correctly handled in-line (composed from the two adjacent edges) per the CLAUDE.md non-adjacent-in-line convention, with no spurious `L3-L1/` directory. Directionality (LHS=L_{n+1}, RHS=L_n) is consistent throughout both files, frontmatter, and index rows.

**plan-kind-consistency — pass.** Declared kind is `firm` theme for both edges, and the content shape matches: identity edge between firm/firming endpoints, no speculative operator, no negative-anchor reconstruction, no literature inference, no rough-in placeholders. The `firm` claim rests on two firm/firming endpoints (L1 cycle-002 firm; L3 cycle-011 firm; L2 firming-this-cycle D3) and a total-bijective identity mapping. The "Design-presupposition note (not a status reduction)" is correctly framed: the leaf-vs-fold fork is *resolved keep-(b)* (batch-12 meta-phase per the c042 audit), so presupposing the same-named L2 floor is sound, not a hidden rough-in. The `firm`-on-positive-structure rationale is consistent with the firm-theme tier.

**skill-uptake-survey — pass (telemetry).** The report references mechanical-skill invocation appropriately: `tools/citecheck/citecheck.py --anchor` self-verification of all L0 anchors is named in frontmatter, §Verified-against, and §Supporting-evidence. The slug-convention and identity-edge shape are abstractor-template work (mirroring the firm `scal`/`dot` arity-family precedents, cited). No skill is conspicuously implied-but-unreferenced. Surfaced, not blocking.

### Issues found

No blocking or warning issues found. All eight checks pass. Observations for the integrator (none are defects):

1. **`L2/axpy.md` co-lands (serial-sequencing dependency, NOT a defect).** Both new themes name `book/src/L2/axpy.md` as an endpoint; it is absent on disk now and lands this cycle as wave-1 D3. The report flags this in frontmatter, §Verified-against, §Open-questions, and the Applicability conditions. The integrator must apply D3 (`L2/axpy`) before — or in the same staging pass as — these two themes so the `../L2/axpy.md` links resolve at build time. The report's wave-2-applies-after-D3 instruction is explicit and correct.

2. **L3/axpy staleness routed to c044 (NOT a defect, correctly scoped out).** `L3/axpy.md` §"Lowers to" (`:5-6` frontmatter, `:112-116`) currently asserts a direct L3>L1 identity with "no L2 intermediate"; once the L2 floor + `axpy-body-identity` land, this goes stale and should re-anchor L1→L2. The report correctly defers this to the c044 L3-re-anchor sweep (one-theme-per-invocation discipline; out of this dispatch's scope; tracks with the same `L3/scal.md` staleness from cycle-041). Confirmed as a deliberate scope-out, not an omission.

3. **Count-ownership cleanly partitioned to D2 (correct, NOT a defect).** The proposed changes are exactly: two `new:` theme bodies, two single dep-map ROWS (one each in L2-L1/index + L3-L2/index), and two SUMMARY registrations. Both index `edit:` blocks carry explicit integrator notes NOT to touch the §"Vocabulary cohort" running tallies or §"Working Notes" cohort-growth/coverage-gap counts (`l3-l2-rotation-theme-coverage-gap 10-of-18`) — those are D2's (layer-intro-author) this cycle. This matches the D3-count-ownership partition convention; no tally double-write risk.

4. **Slug convention (`-leaf-identity` / `-body-identity`) is the RATIFIED batch-12 convention, applied correctly.** Matches the firm `dot-leaf-identity` / `dot-body-identity` and `scal-body-identity` precedents. The report notes the L2>L1 `axpy` edge uses `-leaf-identity` even though it is a fold-member, correctly distinguishing an identity-leaf-lowering from a fold→leaf dispatch (same as the `dot-leaf-identity` precedent, also a fold-member). The cohort-hygiene note (D1's pending `scal`/`nrm2` rename will make the L2>L1 BLAS-1-floor-edge cohort slug-uniform) is forward-looking awareness, not a blocker.

5. **Fence parity confirmed.** 12 `^```` lines = 6 balanced proposed-changes blocks (2 `new:` + 4 `edit:`), each open/close paired (53-338, 340-603, 605-608, 616-619, 626-630, 632-636). No nested code fences inside the `new:` bodies (headings are markdown `##`, code snippets are indented, not re-fenced), so no nested-fence-truncation risk; the firm-body-outside-fence defect class does not apply (theme files, not firm operator entries).

---

## Repair

### Fixes attempted

The critic returned all eight checks `pass` with no blocking or warning findings. There is no defect to repair. The repair pass performed only the explicit cross-check the dispatch instruction requested (index TABLE-row completeness — the omission the sibling D7 axpby report exhibited), plus a confirmation of the five self-flagged integrator observations as non-defects.

- **Finding (dispatch cross-check)**: Did D6 add BOTH the dep-map/theme-list TABLE rows AND any cohort bullets for its axpy themes in `L2-L1/index.md` + `L3-L2/index.md` — or did it repeat the D7 omission (cohort bullets only, table rows missing)?
  - **Decision**: not-needed (verified present and correctly formatted; no repair required).
  - **Action**: none. **Cross-check result — D6 did NOT repeat the D7 omission.** The CYCLE.md carries both index TABLE-row `edit:` blocks:
    - `edit:book/src/L2-L1/index.md` (CYCLE.md:605-608) inserts the `axpy-leaf-identity` row into the 4-column `| theme | L2 anchor | L1 anchor | status |` Theme-list table, immediately after the `dot-leaf-identity` anchor row (verified live at `book/src/L2-L1/index.md:17`). Column count and `|`-delimited format match the sibling rows exactly.
    - `edit:book/src/L3-L2/index.md` (CYCLE.md:616-619) inserts the `axpy-body-identity` row into the 5-column `| Theme | LHS (L3) | RHS (L2) | Justification kind | Status |` Theme-list table, immediately after the `scal-body-identity` anchor row (verified live at `book/src/L3-L2/index.md:17`, reproduced verbatim as insertion context). Column count and format match.
  - **Note on cohort bullets**: D6 correctly did NOT add the §"Vocabulary cohort" bullets or touch the §"Working Notes" tallies. Both index `edit:` blocks carry explicit integrator notes (CYCLE.md:610-614, 621-624) deferring the cohort-bullet / running-tally writes to D2 (layer-intro-author) per the ratified D3-count-ownership partition for this cycle. This is correct partitioning, not an omission — the opposite shape from the D7 defect (which dropped the load-bearing table rows). No row needs to be synthesized.

- **Finding (integrator observations 1–5, all self-flagged by the report and the critic as non-defects)**:
  - **Decision**: not-needed for all five.
  - **Confirmation**: (1) `L2/axpy.md` co-lands as wave-1 D3 — serial-sequencing dependency, explicitly flagged; the integrator must stage D3 before/with these two themes so `../L2/axpy.md` links resolve. Not a repairable defect (it is a sequencing instruction, already stated correctly). (2) `L3/axpy.md` §"Lowers to" staleness routed to the c044 L3-re-anchor sweep — a deliberate, correctly-scoped deferral (one-theme-per-invocation; out of this dispatch's write-scope; tracks with the same `L3/scal.md` staleness from cycle-041). Authoring the re-anchor here would be substantive content outside repair authority AND would touch a file outside this report's scope. (3) Count-ownership cleanly partitioned to D2 — confirmed above; no tally double-write risk. (4) Slug convention `-leaf-identity` / `-body-identity` is the ratified batch-12 convention, applied correctly (matching `dot-leaf-identity` / `scal-body-identity`). (5) Fence parity confirmed (6 balanced blocks); no nested-fence-truncation risk.

### Unrepairable findings

None. No finding exceeds repair authority because no finding is a defect: all eight checks pass, the dispatch cross-check confirms the table rows are present and correctly formatted, and the five integrator observations are correctly-handled non-defects (sequencing dependency + a correctly-scoped c044 deferral + a correct count-ownership partition + a ratified slug choice + confirmed fence parity).

## Suggested resolution

`ready`. Notes for the integrator:

- **Stage D3 (`book/src/L2/axpy.md`) before or in the same staging pass as these two themes.** Both new theme files reference `../L2/axpy.md` as an endpoint; that file co-lands this cycle as wave-1 D3. Applying these themes before D3 would leave a dead `../L2/axpy.md` link at build time. The report's wave-2-applies-after-D3 instruction is explicit and correct.
- **Do NOT write the §"Vocabulary cohort" bullets or §"Working Notes" cohort/coverage tallies for these two themes here** — they are D2's (layer-intro-author) this cycle per the count-ownership partition. The two index `edit:` blocks insert ONLY the single Theme-list TABLE rows (plus the two SUMMARY registrations). This is the inverse of the D7 axpby shape; here the table rows ARE present and the cohort bullets are the correctly-deferred part.
- **L3/axpy staleness is c044's, not this cycle's.** The `L3/axpy.md` §"Lowers to" re-anchor (L1→L2, once the L2 floor + `axpy-body-identity` land) is routed to the c044 L3-re-anchor sweep alongside the equivalent `L3/scal.md` staleness — do not attempt it in this integration.
