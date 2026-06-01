---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T213000Z
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
repaired_at: 2026-06-01T214500Z
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

# META: verification of "Re-anchor jacobi-smoother (both edges) + divfree-projector-body-identity (L3>L2) — DEMOTE; KEEP divfree-projector-leaf-identity (L2>L1)"

## Critique

### Checks run

**citation-validity — pass.** The four load-bearing L0 anchors all verified mechanically via `citecheck.py --anchor` against on-disk `reference/palace/`: `jacobi.cpp:38` (`DI[i] * X[i]` → `[ok] :38`), `divfree.cpp:185` (`AddMult` → `[ok] :185`), `divfree.cpp:180-181` (`AddMult` → `[ok] :180,:181`), `divfree.cpp:155-187` (`Mult` → `[ok]` at `[155,162,163,167,175,180,181,185]`). The report-wide `--scan` returned `7 ok, 0 failing`. The §Discipline prose-correction claim — that the §Context "Downward" bullet (L3/jacobi-smoother.md:31) cited the `Y[i] = DI[i] * X[i]` kernel form but lacked the line anchor, and D4 added `jacobi.cpp:38` — is accurate: line 31's `[old]` has no anchor, the `[new]` adds it, and the same anchor is already cited at lines 73/143/158 of the same file, so the value is internally consistent and L0-verified. The report carries no `verified_against:` YAML block, so that sub-check is not applicable.

**surface-or-evidence — pass.** This is a pure structural refactor (theme-file deletion + in-line-note re-anchoring under the 2026-06-01 VOCABULARY-SHIFT REDIRECT), not a refinement-shaped proposal asserting a new rotation. The deletions are justified by the cycle-050 D8 verify-body audit (DEMOTE-OK verdicts) and the degeneracy claim (identity-in-named-terms across the edge). The one rotation NOT deleted — the KEPT `divfree-projector-leaf-identity` step-4 `Grad->AddMult` fusion — retains its surface and evidence untouched (file, SUMMARY line, L2-L1 index row 27 with `:185`/`:180-181` anchors, working-notes bullet 62 all confirmed present and unedited on disk).

**rotation-quality — pass (applies to the demotion-degeneracy judgments, not a new rotation).** The three deleted edges are correctly classified as degenerate identity-in-named-terms lowerings (no vocabulary shift across the edge: same signature, same laws, same variant profile at both layers — the §1d smell the redirect names), which is exactly the case the redirect directs to demote. The KEPT edge is correctly preserved as a genuine rotation: the L2 de-fused `apply_linop(P.Grad,ψ) ▷ axpy` RE-FUSES into the L1 fused `Grad->AddMult(ψ,y,1.0)` — a real translation across the L2↔L1 vocabulary boundary, not a rename. The keep/demote split is sound.

**variant-axis-coverage — pass.** No new variant-axis branching is introduced; the in-line notes preserve the existing variant profiles verbatim (jacobi "two-orthogonal-plus-one-absorbed"; divfree element-type axis). The element-type (real/complex) axis for the KEPT divfree fusion is preserved with both anchors (`:185` real, `:180-181` complex). Not a new-axis-introducing report.

**cross-reference-integrity — pass.** Full inbound-link inventory independently reproduced via `grep -rnE` over `book/src/`: the deleted-slug live links resolve to (i) SUMMARY 57/58/99 — handled §5; (ii) L3-L2/index.md 21/22 — handled §6; (iii) L2-L1/index.md 22 — handled §7; (iv) two refs inside the deleted file `jacobi-smoother-leaf-identity.md` (29/33) and one inside the deleted `jacobi-smoother-body-identity.md` (36) — vanish with the files; (v) the one LIVE link inside the KEPT `divfree-projector-leaf-identity.md:36` — handled §7b. No dangling live link remains after application. All `[old]` anchor strings were verified to match on-disk content exactly (frontmatter + §Context + §"Lowers to" blocks in both L3 entries; both L2 entries; both index files; SUMMARY). The L3/divfree-projector.md frontmatter+§Context-block+§"Lowers to"-block triple correctly captures all four on-disk body-identity references (line 6, lines 92+106 within one §Context block, line 476). Relative paths from L3 (`../L2-L1/divfree-projector-leaf-identity.md`, `../L2/divfree-projector.md`) resolve on disk. Build-readiness fence guard: 40 fence markers / 20 balanced blocks (3 delete + 17 edit), even parity, no nested fences inside payloads — not a firm-body-inside-fence report; no fence-truncation defect.

**edge-label-fidelity — pass.** Every edge label matches its prose: the jacobi/divfree `-body-identity` edges are discussed as L3>L2 throughout; `-leaf-identity` as L2>L1. The L3 divfree in-line note correctly distinguishes the L3>L2 demoted edge from the L2>L1 KEPT-fusion edge. The transitive L3>L1 in-line identity annotation is correctly framed as a non-adjacent composition (cycle-012 convention), not a directory edge.

**plan-kind-consistency — pass.** Declared shape (lifter re-anchor / theme demotion enacting D8 DEMOTE-OK verdicts) matches content: three `delete:` blocks + seventeen `edit:` blocks for re-anchoring, no new operator/theme authoring. The KEEP-vs-DEMOTE partition is explicit and consistently applied.

**skill-uptake-survey — warning (non-blocking, telemetry only).** The report's shape strongly implies two existing skills: `verify-citation-range` (the report DID use its mechanical `tools/citecheck/ --anchor`/`--scan` realization — invocation evidenced in §Supporting evidence and §Discipline), and `proposed-changes-fence-encloses-full-body-guard` (the fence-parity claim "40 balanced fences, 20 blocks" implies a fence-enumeration was run, but the skill is not named). The citecheck uptake is good; the fence-guard invocation is only implied by the count, not referenced. Pure presence survey — surfaces telemetry, does not block.

### Issues found

No blocking issues. The report is mechanically clean: all `[old]` anchors match on-disk content, all L0 citations verify, fence parity is balanced, the full inbound-link inventory is handled with no residual dangling live link, and the load-bearing KEEP + reachability constraint is satisfied. Minor observations below for the repairer/integrator record:

1. **(low — prose-accuracy nuance, not a defect) "reachable onward from the L2 floor" slightly overstates the L2-floor link.** Reports §4 / §Discipline state the KEPT fusion theme is "reachable onward from the L2 floor." Verified: `book/src/L2/divfree-projector.md` contains NO live link to `divfree-projector-leaf-identity` (it refers to "the L2>L1 lowering theme" only in descriptive prose). However, the reachability constraint is ACTUALLY satisfied by a more direct route the report also provides — the L3 entry's own in-line note carries a DIRECT live link `[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)` (report §4 block2 line 142, block3 line 190; relative path resolves on disk). So the load-bearing requirement (genuine rotation reachable from the L3 entry, not orphaned) is met; the "onward from the L2 floor" phrasing is the imprecise part. Location: report §4 `[new]` frontmatter block (line 96) and §Discipline "Reachability constraint satisfied" bullet (line 287). Severity low — the constraint holds via the direct L3→KEPT link regardless of the phrasing.

2. **(informational — serial-ordering coordination, not a D4 issue) L3-L2 cohort count narrative `17→13→11` is D4's local-scope view; D5 reconciles to FINAL 5.** D4 rewrites the L3-L2/index.md cohort-growth narrative (§6 line 61 edit) and the L2-L1/index.md split-note (§7 line 73 edit) to reflect only its own two L3>L2 demotions (`17→13→11`) plus the single `jacobi-smoother-leaf-identity` L2>L1 demotion. The on-disk file inventory confirms D4's local arithmetic (9 L3-L2 body-identity files − 2 = 7 thin remaining + 4 substantive = 11; remaining-7 enumeration `krylov-step/dot/nrm2/scal/axpy/axpby/axpbypcz` matches disk). D4 explicitly defers the consolidated cross-dispatch TALLY to D5 (§Discipline + §Open-questions caveat). Per the dispatch brief this is the intended D4-before-D5 serial dependency (D5's anchor is D4's `[new]`), so D4's intermediate `11` will be superseded by D5's FINAL `5`. Flagged only so the integrator preserves the D4→D5 ordering; not a defect in D4.

3. **(informational — skill telemetry) fence-parity guard invocation implied but not named.** See skill-uptake-survey above. The "40 balanced fences, 20 blocks" claim verified true, but `proposed-changes-fence-encloses-full-body-guard` is not referenced by name. No action required.

## Repair

### Fixes attempted

- **Finding 1 (low — prose-accuracy)**: "reachable onward from the L2 floor" overstates the L2-floor link (`L2/divfree-projector.md` carries no live link to the KEPT `divfree-projector-leaf-identity` theme — only descriptive prose). The reachability constraint actually holds via the DIRECT L3→KEPT-theme live link the report itself provides.
  - **Decision**: repaired (filed under `cross-reference-integrity` — the affected claim is about which link satisfies the reachability constraint).
  - **Action**: corrected the phrasing in all three occurrences in `reports/<id>/CYCLE.md`:
    - §4 block2 (the `L3/divfree-projector.md` frontmatter `[new]`): "reachable onward from the L2 floor" → "reachable directly from this L3 entry via the live link above (the L2 floor entry itself carries no live link to the KEPT theme, only descriptive prose)".
    - §4 block3 (the §Context "Downward" `[new]`): "reachable onward from the L2 floor, not orphaned" → "reachable directly from this L3 entry via the live link above (not via the L2 floor, which carries no live link to the KEPT theme), so not orphaned".
    - §Discipline "Reachability constraint satisfied" bullet: rewrote to state reachability is provided by the direct L3→KEPT-theme link, with the L2 floor explicitly noted as carrying only descriptive prose (no live link).
  - **Note**: these are surgical phrasing corrections to the report's *prose-about-reachability*, not to the proposed-changes' `[new]` artifact payloads' load-bearing content — wait, two of the three edits DO touch `[new]` payloads (§4 block2/block3). They are still mechanical/surgical: the corrected phrasing replaces an imprecise descriptive clause with an accurate one describing the SAME live link the block already emits (the `[`divfree-projector-leaf-identity`](../L2-L1/divfree-projector-leaf-identity.md)` link is unchanged in both blocks). No new claim, citation, or rotation is authored; the demotion/keep structure and all anchors are untouched.

- **Finding 2 (informational — serial-ordering)**: D4's `17→13→11` L3-L2 cohort count is its local-scope view; D5 reconciles to FINAL 5.
  - **Decision**: not-needed (no fix; integrator note only).
  - **Rationale**: D4's local intermediate count is correct for its own two L3>L2 demotions and was a necessary intermediate; the report explicitly defers the consolidated cross-dispatch TALLY to D5 (§Discipline + §Open-questions caveat). Preserving it as-is is correct. See "Suggested resolution" for the integrator-ordering note.

- **Finding 3 (informational — skill telemetry)**: `proposed-changes-fence-encloses-full-body-guard` invocation implied by the "40 balanced fences, 20 blocks" count but not named.
  - **Decision**: not-needed (telemetry only; no action required per critic).

### Unrepairable findings

None. All three critic observations were low/informational; the one prose-accuracy finding was a surgical phrasing correction within repair authority (trivial cross-reference / reachability-claim accuracy fix — the live link itself was already correct, only the descriptive clause naming the wrong route was imprecise).

### Cross-dispatch coordination (for the repair record, not a D4 fix)

- Sibling D2 and D3 each authored de-link edits to `book/src/L3-L2/divfree-projector-body-identity.md` — the file D4 DELETES. Those sibling edits are being dropped in their own repairs; D4's deletion of that file is correct and stays.
- D4's §7b edit to the KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md` (the `:36`-area re-anchor) targets the lines-35-37 sibling-pointer prose ("mostly-identity-in-form ... sibling of the L3>L2 [`divfree-projector-body-identity`]..."), verified on disk at lines 35-36. This is a distinct substring from any D2/D3 edit to the same file, so the serial 3-way apply succeeds for whichever sibling edits to this file survive their own repairs. D4's `[old]` substring confirmed present on disk.

## Suggested resolution

`ready`. D4 is the cleanest dispatch this cycle: 7 pass + 1 non-blocking telemetry warning, the load-bearing KEEP + reachability constraint is satisfied (now with accurate phrasing after the finding-1 fix), all L0 anchors verified, fences balanced, deleted edges genuinely degenerate.

Integrator notes:
- **Preserve the D4-before-D5 serial dependency.** D4's `17→13→11` L3-L2 cohort count and its single `jacobi-smoother-leaf-identity` L2>L1 demotion are intermediate; D5's anchor is D4's `[new]`, and D5 owns the consolidated cross-dispatch TALLY reconciling to FINAL 5. Apply D4 before D5.
- **D4 DELETES `book/src/L3-L2/divfree-projector-body-identity.md`.** Sibling D2/D3 edits to that same (deleted) file are being dropped in their own repairs; the deletion stands.
