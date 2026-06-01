---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T20:09:19Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T20:30:00Z
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

# META: verification of cycle-050 D4 — DEMOTE elementwise_product degenerate theme pair to in-line notes

## Critique

### Checks run

**citation-validity — pass.** The two load-bearing L0 anchors were re-verified mechanically via
`tools/citecheck/citecheck.py --anchor`: `palace/linalg/operator.cpp:478-487 --anchor 'Mult'` →
`[ok]` (anchor at line 479, in range); `palace/linalg/operator.cpp:545-568 --anchor
'MultHermitianTranspose'` → `[ok]` (anchor at line 548, in range). These are exactly the
load-bearing-fact anchors the dispatch flagged for preservation, and both are present verbatim in
the receiving operator entries' §Evidence (`L2/elementwise_product.md:453-467`,
`L3/elementwise_product.md:176-178`) — confirmed on-disk. The report makes **no new L0 claim** in the
in-line notes (it points at existing evidence), so citation-validity is satisfied. The report's
internal artifact pinpoints (`L3-L2/...:120`, `L2-L1/...:104`, the `:6`/`:28`/`:149`/`:151` L3 edit
targets, the `:300-306`/`:387` L2 edit targets) all resolve to the exact on-disk content I read. No
`verified_against:` YAML block is emitted by this report (it is a demotion, not a lowering-verifier
audit), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a structural-demotion refinement, not a rotation_claim. It
modifies surface (operator-entry prose + frontmatter + index rows + SUMMARY) and the framing is pure
relocation of an existing identity-in-form fact (the themes' content is folded in-line; no new
algebraic content authored). The dispatch is explicitly a redirect-mandated DEMOTE, which is allowed
surface modification with the supporting "degenerate identity-in-named-terms" justification carried in
both theme bodies (`body-identity.md:120`, `leaf-identity.md:104-105`, re-read and confirmed). Not a
bare rotation_claim.

**rotation-quality — pass (degenerate, by design).** The check normally rejects 1:1 / identity
mappings as non-rotations — but here that is precisely the point: the report's thesis is that both
edges ARE degenerate identity-in-named-terms maps (total bijective identity on a single binding) and
therefore should NOT carry dedicated theme files under the 2026-06-01 redirect. I independently
confirmed the degeneracy by reading both deleted themes: signature, all ten algebraic laws, and both
variant axes (element-type + conjugation sub-axis) are textually identical across each edge; the
rewrite tables (`body-identity.md:104-121`, `leaf-identity.md:91-105`) are explicit total-bijective
identities. The deletion is correct; the surviving substantive rotation (L1>L0
`reciprocal-elementwise-product-mutation-rotation` sub-pattern B) is correctly retained as the chain's
real rotation. Pass.

**variant-axis-coverage — pass.** The operator has two orthogonal variant axes (element-type
real|complex; conjugation sub-axis on the complex side). Both in-line demotion notes (L3 §"Lowers to"
new-string `:89`; L2 §"Lowers to" new-string `:149-165`) explicitly carry "both variant axes:
element-type + conjugation sub-axis" and the conjugate `MultHermitianTranspose` anchor. No axis is
dropped or hidden in the demotion. Pass.

**cross-reference-integrity — warning.** All edit old-strings match on-disk exactly (verified by
`grep` for each of §2a/§2b/§2c on `L3/elementwise_product.md`, §3a/§3b/§3c on `L2/elementwise_product.md`,
the two SUMMARY lines, the two index rows, and the `normalize-leaf-identity.md` line). All inbound-link
targets resolve. The de-link strategy keeps `linkcheck2` green. Three sub-issues raise this to warning
(detailed below): (1) the §5a/§5b `[old]` strings are row-PREFIX substrings, not full rows — substring
replacement preserves the row tail, which is the intended de-link-the-slug-cell behavior, but it is
fragile to integrator semantics; (2) the D7 coordination dependency on `normalize-leaf-identity.md:12`
is a genuine cross-dispatch ordering risk the report itself flags; (3) the §4 SUMMARY edits replace a
list line with an empty `[new]`, leaving a blank line (tolerated by mdBook; tidy-up is D7 territory).
Build-readiness fence guard: 26 fences = 13 balanced pairs, even parity, every edit/delete block opens
and closes cleanly — no fence-truncation defect, no firm-body-outside-fence concern (this report
authors no firm chapter body).

**edge-label-fidelity — pass.** The report carries two edge labels (L3>L2 and L2>L1). The L3-entry
edits discuss the L3>L2 edge; the L2-entry edits discuss the L2>L1 edge. No edge/prose mismatch. The
non-adjacent L3>L1 transitive identity is correctly handled by composition (not a new directory),
consistent with the in-line non-adjacent convention.

**plan-kind-consistency — pass.** Declared shape is a lifter re-anchor/demotion (refactor-pass
enactment). Content matches: deletions + in-line folds + de-links + explicit defer-to-D7 of tallies.
No firm-operator-with-rough-in-placeholders mismatch. The one bounded prose-correction (stale
`-fusion` forward-reference) is recorded and is within lifter authority (see issue 4).

**skill-uptake-survey — warning (non-blocking).** The report references `citecheck --anchor` usage
(citation re-verification) — good. But the dispatch shape (a demotion that DE-LINKS rather than removes
dead inbound links to keep the build green) is exactly the situation the
`proposed-changes-fence-encloses-full-body-guard` / link-hygiene skill family addresses, and the
inverse of `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. No skill is cited for the
de-link decision. Pure telemetry surface — not blocking.

### Issues found

**Issue 1 — §5a/§5b de-link old-strings are row-PREFIX substrings, not whole rows (cross-reference-integrity, low-medium).**
`L3-L2/index.md:24` and `L2-L1/index.md:26` are long multi-cell table rows. The report's `[old]`
captures only the leading cell(s) — for §5a up to `...§Signature`, for §5b up to `...D3 floor)` — and
the `[new]` likewise stops there, dropping the row tail (`— the whole-tensor binary field operation...`
for 5a; the L1 cell + justification + status cells for 5b). On-disk, both rows continue well past the
captured prefix. This is *intentional* (de-link the slug cell only, preserve the rest of the row for
D7's removal pass) and is SAFE under substring-replacement semantics — the `[old]` prefix is a unique
substring of its line, so the integrator replaces just the prefix and the tail survives intact,
yielding a coherent de-linked row. The risk: if the integrator interprets an `edit:` block as a
whole-line/whole-row replacement rather than a substring replacement, the row tail would be truncated.
Flagging for the integrator to confirm substring semantics; no content defect.

**Issue 2 — D7 coordination on `normalize-leaf-identity.md:12` is a real cross-dispatch ordering risk (cross-reference-integrity, medium).**
The dispatch context states D6 is deleting `normalize-leaf-identity.md` (it is itself a cycle-050
demotion candidate, and the report's own §"Open questions" flags it). D4 edits that file at `:12` to
de-link the dead `elementwise-product-leaf-identity` reference. If D6 deletes
`normalize-leaf-identity.md` before D4's §5c edit is applied, the §5c edit targets a non-existent file
(integrator must drop §5c); if D6 deletes it after, D4's edit is harmless but wasted. Either ordering
is benign for build-greenness PROVIDED the integrator is aware. The report flags the D7 row-removal
dependency in §"Open questions" but does NOT explicitly call out the D6-deletes-the-same-file collision
on §5c — it frames `normalize-leaf-identity.md` only as a future demotion candidate, not as a
this-batch deletion target. This under-states the coordination risk relative to the dispatch context.
Recommend the integrator sequence D4's §5c conditional on `normalize-leaf-identity.md` still existing.

**Issue 3 — §4 SUMMARY edits leave blank lines (cross-reference-integrity, low / cosmetic).**
Both SUMMARY edits replace a `- [slug](...)` list item with an empty `[new]:`, producing a blank line
where the entry was. mdBook's SUMMARY parser tolerates blank lines between list items, so the build
stays green, but the consolidated SUMMARY tidy-up (collapsing the blank) is left implicitly to D7.
Acceptable given tallies are deferred; noting for completeness.

**Issue 4 — bounded prose-correction (stale `-fusion` forward-reference) is justified and in-scope (no defect; verification recorded).**
The dispatch flagged the removal of a "stale/contradictory `-fusion` forward-reference" for scrutiny.
I confirmed on-disk: `L2/elementwise_product.md:300-306` carries a "Lowering themes (forthcoming —
plain-text forward-reference, files do not yet exist)" block naming `L2-L1/elementwise-product-fusion`
and asserting "files do not yet exist" — while the actual L2>L1 theme on disk was
`elementwise-product-leaf-identity.md` (the `-leaf-identity` slug, which DID exist). So the L2 prose
was simultaneously (a) forward-referencing a `-fusion` slug that never existed and (b) claiming no
L2>L1 theme existed when a `-leaf-identity` one did. The contradiction is real and on-disk. The
report's §3b replacement of that block with the demotion record is a bounded correction of a
drifted/contradictory forward-reference — within lifter authority, not substantive re-authoring (no
signature/law/decomposition change). Pass; recorded as the report's one bounded prose-correction.

**Issue 5 — slug asymmetry correctly respected (no defect; verification recorded).**
The dispatch flagged risk of the chapter slug being "normalized." Verified: every reference uses the
exact on-disk names — theme slugs hyphenated (`elementwise-product-body-identity`,
`elementwise-product-leaf-identity`), operator chapters underscore (`elementwise_product.md`). No
chapter slug was hyphenated. The delete targets, edit targets, SUMMARY lines, and index rows all use
the correct on-disk spelling (cross-checked against `grep` output). Pass.

**Issue 6 — deleted themes confirmed genuinely degenerate (no defect; verification recorded).**
Read both deleted theme files in full. `body-identity.md` rewrite table (`:104-121`) and
`leaf-identity.md` rewrite table (`:91-105`) are explicit total-bijective identities; signature, ten
laws, and both variant axes are textually identical across each edge; both bodies self-describe the
mapping as "total and bijective on a single binding / the leaf — the degenerate maximal case of the
identity-in-form property." Both are correctly classified degenerate and correctly slated for deletion
under the 2026-06-01 redirect. The one load-bearing fact (the identity-in-form relationship + the
deferral of the substantive rotation to L1>L0 sub-pattern B) is preserved in both in-line notes. Pass.

## Repair

### Fixes attempted

- **Finding (Issue 2, medium — cross-reference-integrity)**: §5c edits
  `book/src/L2-L1/normalize-leaf-identity.md:12`, but the sibling D6 dispatch
  (`reports/2026-06-01T195100Z-lifter-demote-normalize`) DELETES that whole file this cycle; the report
  under-states this (frames the file as a future candidate, not a this-cycle deletion target).
  - **Decision**: repaired.
  - **Action**: DROPPED the §5c `edit:` block targeting `normalize-leaf-identity.md` (CYCLE.md §5c).
    Confirmed D6 deletes the file (`delete:book/src/L2-L1/normalize-leaf-identity.md`, D6 CYCLE.md:48),
    so the inbound de-link is moot — no surviving line to de-link, no `linkcheck2` exposure from this
    report. Replaced the §5c block with a repairer note recording the drop + the D6 deletion +
    the integrator-ordering hazard it avoids. Also updated the §5 section intro and the §"Discipline
    notes" build-safety paragraph (which listed `normalize-leaf-identity.md:12` as one of three
    de-link targets) to two de-links, with the third explicitly recorded as dropped.

- **Finding (Issue 1, low-medium — cross-reference-integrity)**: §5a/§5b de-link `[old]` strings are
  row-PREFIX substrings, not whole rows — safe under substring replacement but fragile if the
  integrator treats `edit:` as whole-row replacement.
  - **Decision**: repaired.
  - **Action**: rewrote the §5a (`L3-L2/index.md:24`) and §5b (`L2-L1/index.md:26`) `[old]`/`[new]`
    strings to be the **whole row** (full line), so the edit applies cleanly under both substring and
    whole-line integrator semantics. Only the leading slug cell changes (live link → plain
    inline-code + DEMOTED marker); the remainder of each row is byte-identical, preserved verbatim from
    the on-disk file. Added a one-line note above each block stating the anchors are whole-row. Verified
    both whole-row `[old]` strings are byte-exact and unique (count 1) against the on-disk index files
    via `grep -cF`.

- **Finding (Issue 3, cosmetic — cross-reference-integrity)**: §4 SUMMARY edits leave blank lines
  (mdBook-tolerant).
  - **Decision**: not-needed (note-only).
  - **Rationale**: mdBook's SUMMARY parser tolerates blank lines between list items, so the build stays
    green; collapsing the blanks is part of D7/finalize's consolidated SUMMARY tidy-up. No defect to
    repair; left as-is per the critic's "D7/finalize can absorb."

### Verification of all remaining edit anchors

Re-verified every surviving `[old]` anchor byte-exact + unique against the on-disk files via `grep -cF`:
- §1 deletes — both target files exist on disk.
- §2a / §2b / §2c (`L3/elementwise_product.md`) — each `[old]` opener occurs exactly once.
- §3a / §3b / §3c (`L2/elementwise_product.md`) — each `[old]` opener occurs exactly once.
- §4 SUMMARY (both theme lines) — each occurs exactly once.
- §5a / §5b (now whole-row index rows) — each occurs exactly once.

### Unrepairable findings

None. The two cross-reference-integrity findings the critic raised (Issue 1, Issue 2) were both
mechanical and within repair authority (drop a moot in-batch-deleted-file edit; widen two de-link
anchors to whole-row). The substantive content of the report (degenerate-theme deletion, in-line
demotion folds, slug-asymmetry, L0-anchor preservation, the bounded `-fusion` prose-correction) was
confirmed clean by the critic and is untouched. The skill-uptake-survey warning is pure non-blocking
telemetry (no skill cited for the de-link decision) — not a defect.

## Suggested resolution

`ready`. Notes for the integrator:
- §5c was dropped because the sibling **D6** dispatch deletes `book/src/L2-L1/normalize-leaf-identity.md`
  this cycle. The D6 deletion subsumes the de-link; no D4 action against that file remains.
- §5a/§5b are now **whole-row** edits (only the leading slug cell changes); they apply correctly under
  either substring or whole-line `edit:` semantics. D7 still owns the consolidated index-row removal +
  cohort-tally decrement (enumerated in CYCLE.md §"Discipline notes").
- The §4 SUMMARY blank lines are mdBook-tolerant; the consolidated SUMMARY tidy is D7/finalize work.
