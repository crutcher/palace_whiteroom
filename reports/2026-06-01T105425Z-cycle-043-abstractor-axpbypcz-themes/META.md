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
---

# META: verification of "axpbypcz adjacent thin-identity lowering themes (L2>L1 + L3>L2)"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` over the full CYCLE.md: 13 citations, 13 OK, 0 failing (bounds + path-hygiene clean). The four load-bearing L0 pinpoints all confirmed with `--anchor`: `vector.cpp:745-758` (anchor `AXPBYPCZ` @746, in range), `vector.cpp:749-751` (anchor `add` @751, in range — the report's claimed @751 is exact), `vector.cpp:755-756` (anchor `AXPBY` @755, in range — the γ!=0 slow-path two-call split), and `vector.hpp:313-316` (anchor `AXPBYPCZ` @315, in range). The fold-parent section anchors verified by Read: `L2/linear_combination.md` line 214 is `## Variant axes` and line 243 is `## Fusion note` — both match the report's claims. The `krylov-step-body-identity.md:97` anchor is correct: line 97 carries the point-3 applicability condition naming the seven L1 primitives (`apply_linop`, `axpy`, `axpby`, **`axpbypcz`**, `dot`, `nrm2`, `scal`) as L3-native by signature shape — the exact claim the report leans on. The L3/axpbypcz staleness lines (`:106,125`) verified: line 125 carries the literal "does not pass through L2 because `axpbypcz` is an L1 leaf" prose, line 106 carries "no L2 intermediate is required" — both correctly identified as stale-this-cycle and correctly deferred to cycle-044 (not authored here). No `verified_against:` YAML block is emitted (the report uses a §Verified-against prose section, not a fenced YAML payload), so the YAML round-trip sub-check is N/A.

**surface-or-evidence — pass.** Both proposals are `new:` chapters (new theme surfaces), not refinements of existing operator/theme text — the refinement-shaped-proposal precondition does not fire. Each new theme carries its own structural rotation_claim (identity-in-form) plus a §Verified-against evidence section. Not a pure rotation-claim-without-surface case; not applicable as a refinement backfill. The two `edit:` blocks (index rows, SUMMARY) are additive registrations of the new surfaces, not modifications to existing claims.

**rotation-quality — pass (with an inherent-shape note, not a defect).** Both themes assert an **identity-in-form** rotation, explicitly. Under the project's "Identity-lowerings still require both L levels" invariant, an identity-in-form edge between two value-thread-isomorphic same-named leaves is a *legitimate, named* rotation kind — it is NOT the "renaming-only / 1:1 mapping = fail" case the check targets, because the report does not claim compaction/abstraction-gain; it claims and demonstrates that the leaf's own edge is the no-op WHILE the actual L2-layer fusion work (single-aligned `add(α,x,β,y,z)` pass + `γ==0` arity-collapse + pinned summation order) is correctly *deferred to the fold-parent* `linear-combination-fold-specialization`. The report is careful and explicit about this deferral (§"The rewrite", §"The one note (fusion deferral)", Applicability condition 3). This matches the firm precedents `dot-leaf-identity` and `scal-body-identity` exactly. The "fail" branch (a renaming masquerading as a rotation) does not apply: the report does not assert a rotation gain it cannot back; it asserts identity and routes the real rotation elsewhere with citations.

**variant-axis-coverage — pass.** The variant axes are handled explicitly and consistently: the output-aliasing in-place/out-of-place axis is repeatedly and correctly scoped to the **fold-parent** (`linear_combination` §Variant axes @214), NOT leaf-specific — "this floor is uniformly pure" (both themes). The two leaf-level variant axes (element-type + scalar-promotion sub-axis) are named and stated to be inherited identity-in-form (L2>L1 theme §"The rewrite" row 5, Applicability condition 2). No hidden branch: the `γ==0` control-flow branch is explicitly identified as L1>L0 / fold-parent territory, not a hidden leaf variant. Scoped-out combinations are stated, not silently dropped.

**cross-reference-integrity — pass.** Every referenced artifact file resolves on disk: `L1/axpbypcz.md`, `L3/axpbypcz.md`, `L2/linear_combination.md`, `L2/scal.md`, `L1-L0/axpbypcz-mutation-rotation.md`, `L2-L1/dot-leaf-identity.md`, `L2-L1/scal-fold-specialization.md`, `L2-L1/linear-combination-fold-specialization.md`, `L3-L2/scal-body-identity.md`, `L3-L2/krylov-step-body-identity.md`, both index files, SUMMARY.md, and `scaffolding/decisions/axpby-as-primitive.md`. The one **expected** non-resolving reference is `L2/axpbypcz.md` (the D5 co-landing floor) — the report explicitly presupposes D5 co-lands and flags wave-2 serial sequencing (apply D5 before these themes); this is a known cross-report dependency, not a dangling link. All insertion anchors verified exact: L2-L1 row inserts between `scal-fold-specialization` (@15) and `inner-product-fold-specialization` (@16); L3-L2 row inserts between `scal-body-identity` (@17) and `assemble-diagonal-body-identity` (@18); SUMMARY inserts after the scal rows at @46 (L3-L2 Part) and @78 (L2-L1 Part) — all four match the report's line claims. Fence parity: 10 fences = 5 balanced `new:`/`edit:` blocks (no nested `text` fences inside; the L-form pseudocode is indented-code, not nested-fenced), so the firm-body-inside-fence guard is satisfied — every firm-claimed body (`## Status`, signature, laws, evidence) sits INSIDE its `new:` fence.

**edge-label-fidelity — pass.** Theme 1 is labeled L2>L1 and its prose discusses exactly the L2 `axpbypcz` leaf → L1 `axpbypcz` leaf edge (LHS = L2 §"L2 form", RHS = L1 §"L1 form", rewrite narrated L2→L1). Theme 2 is labeled L3>L2 and its prose discusses exactly the L3 `axpbypcz` whole-tensor form → L2 floor leaf edge (LHS = L3, RHS = L2, rewrite `axpbypcz (L3) ⇒ axpbypcz (L2)`). Both narrate strictly high→low, consistent with the layer-definition discipline; the reverse-direction (lifting) notes are correctly quarantined into §"Open questions / caveats" as working-notes, NOT in the chapter bodies. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Both entries declare `firm` and carry firm-shaped content (full Signature, the rewrite mapping table, Applicability conditions, Justification kind, Verified-against, Status). No rough-in placeholders, no TODO bodies, no stub markers. The `firm` claim rests on two firm/firming endpoints (L1 firm cycle-003; L3 firm cycle-011; L2 firming D5 this cycle) and an identity-by-construction argument — consistent with the firm precedents. The one transient dependency (L2 RHS firming this cycle) is disclosed in both Status blocks, which is the correct handling, not a mis-classification.

**skill-uptake-survey — pass.** The report references the relevant skills its shape implies: `tools/citecheck/citecheck.py --anchor` self-verification (named in §Verified-against and §Supporting evidence, with the @746/@751/@315 anchors), and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (correctly cited as a noted-not-enacted integrator option for the D5 forward-reference, since cross-report edits are outside dispatch authority). Telemetry present; nothing blocking.

### Issues found

No blocking issues. The report is clean across all 8 checks. Minor, non-blocking observations for the repairer/integrator to be aware of (none require a fix):

1. **(Informational, not a defect) Cross-report dependency on D5.** `book/src/L2/axpbypcz.md` (the L2 floor, both themes' load-bearing endpoint — Theme 1's LHS, Theme 2's RHS) does not yet exist on disk; it co-lands from wave-1 D5 this cycle. The report discloses this explicitly and flags the required serial-sequencing constraint (integrator must apply D5 before these two themes, and before D2's count consolidation). This is correct handling of a known co-land, surfaced for the integrator's sequencing — not a dangling cross-reference to repair. If D5 fails to land, both themes' `firm` Status (which asserts "L2 RHS firming this cycle") and the L2>L1 / L3>L2 links would dangle; the integrator's per-report gate should confirm D5 landed first.

2. **(Informational, count-ownership respected) No tally mutation.** Per the dispatch's count-ownership partition, the report's two `edit:` blocks insert ONLY the two new theme-list rows (one per index) plus two SUMMARY entries; it does NOT touch the consolidated firm running-count tallies (`L2-L1/index.md:63` "15 firm + 1 partly-constructive"; `L3-L2/index.md:48` "firm 5 → 10"), the §Vocabulary-cohort bullets, or the `l3-l2-rotation-theme-coverage-gap` progress line. This is correct — D2 owns the consolidation. Verified: no `edit:` block in the report targets those count lines. The report flags the D2 reconciliation boundary clearly (§Open questions D2 count-ownership boundary).

3. **(Informational, slug convention) `-leaf-identity` / `-body-identity` slugs ratified.** The report uses `-leaf-identity` (L2>L1) and `-body-identity` (L3>L2) per the cycle-042 uniform convention, deliberately NOT the cycle-041 `scal`/`nrm2` `-fold-specialization` outliers, even though `axpbypcz` IS a fold-member. The report's rationale (align with the cycle-042 cohort; record fold-membership in the body, not the slug; `dot-leaf-identity` precedent is also a fold-member edge using `-leaf-identity`) is internally consistent and matches the dispatch ratification. Slugs verified against the SUMMARY/index insertion targets. Surfaced for any later meta-phase slug-normalization pass, as the report notes.

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
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

The critic returned all 8 checks PASS with no blocking issues. The repair pass was driven by the
dispatch-level cross-check (same shape as the D7 finding): verify D8 registered each new theme at
**both** index registration sites — (a) the §"Theme list" TABLE row AND (b) the §"Vocabulary cohort"
per-theme bullet — in `L2-L1/index.md` and `L3-L2/index.md`.

- **Finding**: D8 registered the two new themes at the §"Theme list" TABLE rows in both index files
  (the two `edit:` blocks), but did NOT register the corresponding §"Vocabulary cohort" per-theme
  bullets — the report mis-assigned its OWN per-theme cohort bullets to D2 under the count-ownership
  partition (CYCLE.md §"Open questions / caveats" D2-count-ownership-boundary; §"Supporting evidence"
  count-ownership line). This is the same registration-site omission shape as the D7 report (which
  inversely omitted the table rows). The §"Vocabulary cohort" sub-lists are **per-theme registration
  entries** — one bullet per theme, parallel to the table rows (e.g. `dot-leaf-identity` /
  `nrm2-fold-specialization` / `scal-fold-specialization` each carry their own bullet at
  `L2-L1/index.md:44-46`; `dot-body-identity` / `nrm2-body-identity` / `scal-body-identity` at
  `L3-L2/index.md:33-35`) — distinct from the **consolidated running-count tally** ("15 firm + 1
  partly-constructive"; "firm 5 → 10") and the sub-cohort-header count prose, which D2 legitimately
  owns. A new theme needs BOTH a table row AND its own cohort bullet; D2 owns only the tally numbers.
  - **Decision**: repaired.
  - **Action**: Extended each of the report's two index `edit:` blocks with a second INSERT — D8's
    OWN §"Vocabulary cohort" per-theme bullet, matching the sibling format and placed immediately
    after its arity-sibling `scal` bullet (where the table row also lands). Specifically:
    - `reports/.../CYCLE.md` → `### L2/index.md dep-map row` `edit:book/src/L2-L1/index.md` block:
      added the `axpbypcz-leaf-identity` cohort bullet after the `scal-fold-specialization` bullet
      (the cycle-041 FOLD-PARENTED BLAS-1-floor sub-list), mirroring the `scal-fold-specialization`
      bullet shape (arity-3-analogue framing, fusion-deferred-to-fold-parent, non-laws-preserved,
      slug/fork notes).
    - `reports/.../CYCLE.md` → `### L3/index.md dep-map row — N/A ...` `edit:book/src/L3-L2/index.md`
      block: added the `axpbypcz-body-identity` cohort bullet after the `scal-body-identity` bullet
      (the cycle-041 FOLD-PARENTED BLAS-1-leaf body-edge sub-list), mirroring the `scal-body-identity`
      bullet shape (body-is-identity / no-wrapper-to-rotate / arity-3-fold-member-counterpart).
    - Each new INSERT is explicitly scoped in-block as D8's OWN per-theme bullet and explicitly NOT
      the consolidated tally / coverage-gap progress prose (which stays D2's), preserving the
      count-ownership partition. The repair is purely mechanical-surgical (per-theme registration-site
      completion, matching enumerable sibling format) — no substantive authoring; the bullet text
      restates the theme's own already-authored rotation_claim.

All other checks: `not-needed` (critic PASS, no defect; nothing to repair). The L2/axpbypcz endpoint
co-lands from D5 (integrator serial-sequencing, disclosed in the report — not a repair item); the L3
`axpbypcz.md:106,125` staleness is correctly deferred to cycle-044 (substantive refresh, out of
repair authority — not flagged by the critic as a defect anyway).

### Unrepairable findings

None. The single actionable finding (missing §Vocabulary-cohort registration bullets) was mechanically
repairable and repaired in-place in the report.

## Suggested resolution

`ready`. Notes for the integrator:

- The report now carries the COMPLETE registration set for both new themes: per index file, a
  §"Theme list" table row AND a §"Vocabulary cohort" per-theme bullet (4 inserts total across the two
  index `edit:` blocks, 2 per file), plus the two SUMMARY.md entries.
- **Count-ownership preserved.** None of the repair inserts touch the consolidated firm running-count
  tallies (`L2-L1/index.md:63` "15 firm + 1 partly-constructive"; `L3-L2/index.md:48` "firm 5 → 10"),
  the sub-cohort-header count prose, or the `l3-l2-rotation-theme-coverage-gap` "10-of-18" progress
  line — those remain D2's to reconcile. Apply D5 (the L2 floor) + these two themes BEFORE D2's count
  consolidation, per the report's serial-sequencing flag.
- The cohort bullets were placed in the **cycle-041 FOLD-PARENTED** sub-lists (alongside the `scal`
  arity-sibling), since `axpbypcz` IS a fold-member of `linear_combination` (arity-3). If D2's
  consolidation reorganizes cohort sub-headers (e.g. adds a cycle-043 sub-group), the bullets can be
  moved with the rest — they are correctly content-tagged either way.
