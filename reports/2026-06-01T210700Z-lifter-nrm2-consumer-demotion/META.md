---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T214500Z
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
repaired_at: 2026-06-01T215500Z
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

# META: verification of "Re-anchor / consumer-demote nrm2" (cycle-051 D3)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` on the report: 9 ok / 1 "failing", where the single non-ok is `[AMBIG] index.md:73` — a bare basename in the §Supporting-evidence cross-report-split note (L2-L1/index.md:73), not a load-bearing claim pointer (it carries no `path/file.ext:lo-hi` form because it is contextual prose naming a line inside the index the report does not edit). The one load-bearing L0 citation reused in both in-line notes — `palace/linalg/vector.hpp:255-260` (`Norml2`) with the `:259` `std::sqrt(std::abs(Dot(...)))` body line — was confirmed mechanically: `--anchor Norml2` → `[ok] anchor at line(s) [257] within range 255-260`; `--anchor sqrt` on `:259` → `[ok] anchor at line(s) [259]`. Byte-exact. All other references are intra-book cross-references to surviving entries; the report's claim "all citations to surviving entries" holds. No `verified_against:` block is proposed by this report (the only one in scope lives inside the deleted `nrm2-body-identity.md`, which vanishes), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a structural-demotion / retroactive-reorganization report, not a refinement-shaped proposal asserting a new rotation. It deletes two degenerate identity-themes and relocates their (already-present) narration to in-line consumer notes. No new rotation_claim is asserted; the existing identity-in-form claims are preserved verbatim with their existing evidence. Allowed under the "pure retroactive evidence/reorganization" carve-out.

**rotation-quality — pass (with the explicit redirect-aligned finding that these are NON-rotations).** The two deleted themes are correctly diagnosed as degenerate identity-in-named-terms lowerings — the §1d "smell" the 2026-06-01 vocabulary-shift redirect names. Verified against the deleted files: `nrm2-body-identity.md` states "identity-in-form on the kernel ... value-thread-isomorphic ... no decomposition and no wrapper rotation ... the identity is total"; `nrm2-leaf-identity.md` mirrors this. These are 1:1 mappings (the only textual delta is the inner-reduction name `dot`-leaf ↔ `inner_product`-fold) with no compaction/abstraction gain — i.e. NOT rotations, which is precisely why the redirect demotes them. The check passes because the report's verdict (degenerate → demote in-line) is the correct rotation-quality judgment, not because a rotation is claimed.

**variant-axis-coverage — pass.** `nrm2` carries a single collapsed variant axis (element-type real/complex → always-real result via post-composed `abs`); the report preserves this framing in both notes ("the element-type axis is collapsed identically at both layers ... always-real result"). The B-weighted `Norml2` overload is correctly scoped out (it belongs to `matrix-weighted-norm`, per the surviving `L2/nrm2.md:35` boundary, which the report does not touch). No hidden branches.

**cross-reference-integrity — pass.** Full inbound-link sweep confirms the report catches every live markdown link to the two deleted slugs: SUMMARY.md ×2 (directive d), L3-L2/index.md:15 + L2-L1/index.md:21 dep-map rows (directive d), and divfree-projector-body-identity.md:231 + divfree-projector-leaf-identity.md:266 (directive c). The remaining matches are (i) bare-code-span mentions at L2/index.md:118/121 — verified NOT live links (the `](...)` grep returns no match for the `nrm2-*-identity` tokens on those lines; they are backtick code-spans inside historical-narrative bullets) so they do not break `linkcheck2`; and (ii) two self-references inside `nrm2-body-identity.md` itself (:130, :207) which vanish with the file. Every `[old]` block was checked byte-for-byte against on-disk state and matches: L3/nrm2.md:128-130, L2/nrm2.md:6 (frontmatter), :124, :128, the two divfree `[old]` paragraphs (:230-232 / :265-267 — line-broken identically), SUMMARY.md:53-55 / :97-99, and both index dep-map rows + cohort bullets. Build-readiness fence guard: 28 fences, even parity, all 14 `edit:`/`delete:` blocks open+close cleanly; the in-line note bodies use 4-space indented-code for the `nrm2(x) = √...` identity (no nested ` ``` ` fences), so there is no fence-truncation risk and no firm-body-outside-fence defect (these are notes-on-existing-entries, not new firm chapters).

**edge-label-fidelity — pass.** Both new notes are titled and narrated for the exact edge they carry: §"Downward to L2" on `L3/nrm2.md` discusses the L3→L2 hop; §"Downward to L1" on `L2/nrm2.md` discusses the L2→L1 hop. The direction discipline is high→low throughout (no reverse-lift prose in the formal entries). The frontmatter `lowers_to:` edit and the §"Lifts from" re-anchor both correctly redirect their deleted-theme cross-references to the in-line notes without changing the edge.

**plan-kind-consistency — pass.** Declared kind is a lifter consumer-demotion / re-anchor (structural). Content matches: deletions + in-line note relocation + de-links + own-row removal, with the tally explicitly deferred to D5. No firm/rough-in mis-classification; nothing is authored as new content (the report explicitly states "no content decision made").

**skill-uptake-survey — pass (telemetry).** The report references the relevant mechanical procedure: citation self-verification via `tools/citecheck/citecheck.py --anchor` (Discipline note + Supporting-evidence), and the inbound-link sweep via `grep`. The `proposed-changes-fence-encloses-full-body-guard` shape is implicitly satisfied (no firm body outside a fence). No skill invocation is missing for this report's shape.

### Issues found

No blocking issues. The do-NOT-merge CONSUMER boundary — the critical check for this report — is honored correctly: the report does NOT fold `nrm2` into `inner_product` and does NOT touch `inner_product`, `L1/nrm2`, or any fold entry; both new in-line notes record the boundary explicitly ("`nrm2` is a CONSUMER of `inner_product`, not a fold member ... Merging `nrm2` into `inner_product` would be a category error"), and the demotion lands ON the `nrm2` entries themselves. The `std::abs` load-bearing guard is preserved as an explicit claim in both notes; the `vector.hpp:255-260` Norml2 anchor is byte-exact.

Two minor / non-blocking observations, surfaced for the repairer and integrator (neither requires a fix to land this report):

1. **(non-blocking; for integrator — D3/D4 serial-ordering collision on the two `divfree-projector-*` files).** Severity: low (procedural, correctly self-flagged by the report's OQ-2). Directive (c) has D3 de-link the `nrm2-*` cohort-sibling live links inside `book/src/L3-L2/divfree-projector-body-identity.md` (:231) and `book/src/L2-L1/divfree-projector-leaf-identity.md` (:266) — both of which are D4's OWN files. D4 (divfree-projector demotion) is reported to DELETE `divfree-projector-body-identity.md` and KEEP+edit `divfree-projector-leaf-identity.md`. Concrete consequence for the integrator's serial application: (a) D3's edit to `divfree-projector-body-identity.md` is MOOT if D4 deletes that file wholesale — the integrator should drop D3's edit to it (no-op against a deleted target); (b) D3's edit to `divfree-projector-leaf-identity.md` (the KEPT file) and D4's edits to the same file both target the cohort-sibling paragraph region — the integrator must apply both narrow edits and confirm they do not overlap the same lines (D3 drops only the `nrm2-leaf-identity` live link at :266; D4's edits are reported elsewhere in that file). This is exactly the collision the report flags; recording it here so the integrator sequences accordingly. The report's `[old]` text for both divfree edits matches on-disk byte-for-byte as of this critique, so D3's edits are independently applicable if D4 has not yet run.

2. **(non-blocking; deferred-to-D5 historical narrative — confirmed acceptable).** Severity: trivial. The report's OQ-1 cites L2/index.md "lines 118/121/123" as still naming the deleted slugs as firm. Verified on-disk: the deleted-slug mentions are bare backtick code-spans at :118 and :121 (the `](...)` link-pattern grep returns no match for the `nrm2-*-identity` tokens), inside append-only historical cohort-growth-log narrative — NOT live links, so they do not break `linkcheck2`. (The :123 reference in the OQ is approximate; the substance is unchanged.) Editing append-only historical narrative is out of D3's scope, and the redirect-honesty annotation is correctly deferred to D5's consolidated tally. Acceptable as-is for this report. Note also the surviving `L2-L1/index.md:73` cohort-growth-log line still reads "`nrm2-leaf-identity` STAYS" — the report's §Supporting-evidence correctly explains this c050-log "STAYS" meant "stays NOT-merged-into-the-fold" (which the consumer-demotion honors), and flags the running-count refresh at :73 to D5 in OQ-1(ii). This is consistent; the count/narrative reconciliation is properly D5's.

## Repair

D3 was essentially clean — all 8 critic checks `pass`, the critical do-NOT-merge CONSUMER boundary honored, `std::abs` guard preserved, `vector.hpp:255-260` Norml2 anchor byte-exact, deleted themes genuinely degenerate, fences balanced. The two non-blocking observations the critic surfaced both touched the `cross-reference-integrity` finding's directive-(c) de-link edits; both are now resolved mechanically.

### Fixes attempted

- **Finding**: (D3/D4 serial-ordering collision, part a) D3's de-link edit to `book/src/L3-L2/divfree-projector-body-identity.md` is MOOT — sibling D4 (`…lifter-jacobi-divfree-demotion`) DELETES that file wholesale this cycle (`delete:` at D4 report `:36`).
  - **Decision**: repaired
  - **Action**: Dropped D3's `edit:book/src/L3-L2/divfree-projector-body-identity.md` block from CYCLE.md §(c). Replaced with an in-place repair note explaining the drop; updated the §(c) header, the inputs-frontmatter line, and OQ-2 to record it. The link dies with the deleted file, so de-linking it serially against a deleted target would be a no-op / collision. Verified D4 deletes the file (D4 CYCLE.md `:36`).

- **Finding**: (D3/D4 serial-ordering collision, part b) Verify D3's de-link of the `nrm2-leaf-identity` live link inside the D4-KEPT `book/src/L2-L1/divfree-projector-leaf-identity.md` targets a distinct substring from D2's and D4's co-edits on the same file.
  - **Decision**: repaired
  - **Action**: On verification the file is a **3-way co-edit** and D3's ORIGINAL full-cohort-tuple `[old]`/`[new]` did **NOT** target a distinct substring from D2's — D2 (`…lifter-inner-product-dot-demotion`, 3rd block) and D3 BOTH rewrite the same on-disk cohort-tuple line `:266` (`([dot-leaf-identity] / [nrm2-leaf-identity] / [scal-leaf-identity])`), with conflicting `[new]` (D2 keeps `nrm2-` live; D3 keeps `dot-` live). D4's edit to this file is the `:36` `divfree-projector-body-identity` re-anchor — a genuinely distinct line, no overlap. **Repair**: narrowed D3's `divfree-projector-leaf-identity.md` edit from the full-tuple block to the unique single substring `[`nrm2-leaf-identity`](./nrm2-leaf-identity.md)` (confirmed exactly 1 occurrence in the file via grep), so D2's narrow `dot-leaf-identity` de-link and D3's narrow `nrm2-leaf-identity` de-link compose **order-independently** to the correct final state (both de-linked, `scal-leaf-identity` left live). Added an in-place CYCLE.md repair note + integrator flag, updated OQ-2. **Integrator flag**: D2's edit must likewise be repaired to a narrow `dot-leaf-identity`-only substring for full order-independence (D2's repair is the D2 repairer's responsibility; flagged here for the integrator to confirm at apply time).

- **Finding**: (deferred narrative, acceptable) `L2/index.md:118/121/123` historical cohort-log code-spans naming deleted slugs as firm.
  - **Decision**: not-needed
  - **Action**: None. These are bare backtick code-spans (not live `[...](...)` links), inside append-only historical narrative — non-blocking for `linkcheck2`, and editing append-only historical narrative is out of D3's scope. Correctly deferred to D5's consolidated tally per D3's OQ-1. The surviving `L2-L1/index.md:73` "`nrm2-leaf-identity` STAYS" code-span is the same situation (also a bare code-span, also D5's reconciliation). Note only, no fix.

### Unrepairable findings

None. Both flagged observations were mechanical (drop a moot edit; narrow an overlapping edit to a distinct substring) and within repair authority. No substantive authoring, no content decisions.

## Suggested resolution

`ready`. Notes for the integrator:
- This file (`book/src/L2-L1/divfree-projector-leaf-identity.md`) is a **3-way co-edit** across D2 / D3 / D4 this cycle. Apply all three as narrow substring replacements:
  - **D4**: re-anchor the `divfree-projector-body-identity` live link at on-disk `:36` (distinct line).
  - **D2**: de-link the `dot-leaf-identity` token on `:266`.
  - **D3** (this report, repaired): de-link the `nrm2-leaf-identity` token on `:266`.
  D2 and D3 both touch `:266` on disjoint tokens; confirm D2's repaired form is a narrow `dot-leaf-identity`-only substring (the D2 repairer's edit) before applying so the pair composes order-independently.
- D3's edit to `book/src/L3-L2/divfree-projector-body-identity.md` has been **removed** — D4 deletes that file; do not re-introduce a de-link there.
- The remaining D3 edits (`L3/nrm2.md`, `L2/nrm2.md` ×3, `SUMMARY.md` ×2, `L3-L2/index.md` ×2, `L2-L1/index.md` ×2) were re-verified byte-exact against on-disk this repair phase and apply cleanly.
- The `L2/index.md:118/121/123` + `L2-L1/index.md:73` historical-narrative count/slug refreshes remain D5's (OQ-1) — bare code-spans, non-blocking.
