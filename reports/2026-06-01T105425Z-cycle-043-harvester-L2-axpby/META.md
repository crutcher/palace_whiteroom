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

# META: verification of "Formalize axpby at L2" (cycle-043 D4, L2 floor)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` clears all 13 citations (`13 ok, 0 failing`). The five load-bearing L0 anchors were each adjudicated with `--anchor AXPBY` (reference-relative paths): `vector.hpp:130-131` (anchor at :131), `vector.hpp:309-311` (:311), `vector.cpp:726-730` (:727), `:732-737` (:733,:736), `:739-743` (:740,:742) — all `1 ok`. The meaning-read confirms every load-bearing claim exactly: `vector.cpp:726-730` real-real → `add(alpha, x, beta, y, y)` (the 5-arg single-aligned in-place linear-combine, the arity-2 fusion-note witness); `:732-737` complex-complex → `y.AXPBY(alpha, x, beta)` member form; `:739-743` real-scalar-on-complex → `y.AXPBY(alpha, x, beta)` member form with implicit promotion; `vector.hpp:130` carries the comment `// In-place addition (*this) = alpha * x + beta * (*this).` + the member decl; `vector.hpp:309` carries `// Addition y = alpha * x + beta * y.` + the free-function template decl. The "no L0 constant-folding branches inside the AXPBY family" claim is verified (all three AXPBY bodies are single delegations) and the contrast with `axpy`'s real-path `if (alpha == 1.0)` fast-path (`vector.cpp:702`) is accurate. No `+1-drift`. No `verified_against:` block in this report, so that sub-check is not applicable.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme; this is a `new:` floor-presence entry for `book/src/L2/axpby.md` plus an `edit:` row in `L2/index.md` and a `SUMMARY.md` wiring line. New-surface authoring with full evidence apparatus — the refinement-surface vs retroactive-evidence fork does not bind on a net-new chapter.

**rotation-quality — pass (identity-in-form, correctly framed as such).** The report does not assert a compacting algebraic rotation; it asserts the L2↔L1 rotation is **identity-in-form** (value-thread-isomorphic; whole-tensor in/out at both layers; the single fused `α·x + β·y` pass is the fold's arity-2 fusion note, deferred not unfolded). This is the sanctioned identity-lowering shape under CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — not a renaming masquerading as a rotation, because the entry's reason-to-exist is layer-coherence (a present adjacent L2 parent under the firm L3 leaf), explicitly stated. The "do NOT decompose into `scal ▷ axpy`" choice is correctly anchored to `scaffolding/decisions/axpby-as-primitive.md` and the bit-level fusion non-law. Pass.

**variant-axis-coverage — pass.** Two axes inherited from L1 (element-type real/complex; scalar-promotion real-(α,β)-on-complex as a sub-axis) are covered with L0 anchors (`vector.cpp:739-743` for the promotion overload; `vector.hpp:130-131` + `vector.cpp:726-730`/`:732-737` for the element-type specialisations). The **output-aliasing** axis is explicitly scoped OUT of the leaf and attributed to the fold-parent (`linear_combination.md` §"Variant axes" axis 1) — I confirmed that section exists in the fold-parent (lines 90/214/336), so the deferral lands on a real target, not a dangling reference. No hidden branches: the report affirmatively states there are no L0 constant-folding branches on α/β values (verified against source). Pass.

**cross-reference-integrity — pass.** All chapter links resolve from `book/src/L2/axpby.md`'s location (`../L1/axpby.md`, `../L3/axpby.md`, `./linear_combination.md`, `./scal.md`, `../concepts/scalar-promotion.md`, `../concepts/axpy.md`, `../L1-L0/axpby-mutation-rotation.md`, `../../../scaffolding/decisions/axpby-as-primitive.md` — all present on disk). The fold-parent deferral targets exist: `linear_combination.md` line 70 is exactly `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`; §"Fusion note" (line 243), §"Variant axes" (line 214), law 6 specialization identities (line 150) all present. Index §"Fold-cohort boundary" (line 100) and the `dot-l2-leaf-floor-vs-fold-only-design` working note exist; `index.md:17` carries the named vocabulary. **Build-readiness guard:** fence enumeration gives 8 backtick fences (lines 39/120/123/477/479/482/484/487) — even parity, the nested ```text``` signature fence (120–123) is balanced and fully enclosed within the `new:` block (39–477), no truncation risk. The full firm apparatus (`## Status`, `## Signature`, `## Algebraic laws`, `## Evidence`) sits INSIDE the `new:` fence — no firm-body-outside-fence defect. The `edit:` block re-quotes the on-disk `scal` row verbatim as its insertion anchor (byte-exact match to `index.md:70` confirmed) and the `SUMMARY.md` block re-quotes `- [scal](./L2/scal.md)` (byte-exact match to `SUMMARY.md:58` confirmed), so both insertions will land. Pass.

**edge-label-fidelity — pass.** The report's edges are L2↔L1 (lowers-to / lifts-from) and the L3↔L2 floor relationship; the prose discusses exactly those edges (L2 `axpby` lowers to L1 `axpby`; floors the firm L3 `axpby`). No mismatched edge label. Pass.

**plan-kind-consistency — pass.** Declared `firm` matches the content shape: canonical signature against three positively-cited L0 entry points, nine transported laws + the fold-specialization identity, four non-laws, full evidence chain. The `firm` justification is the **firm-on-positive-structure** escape (syntactic-identity laws on the small fully-present AXPBY closure; missing dedicated unit test does not gate) — correctly invoked per the `apply_linop` precedent, with the fold-parent carrying the matching empirical-match caveat. No rough-in placeholders inside a firm-claimed entry. Pass.

**skill-uptake-survey — pass.** The report references `citecheck.py --anchor` self-verification (§Supporting evidence) for the L0 anchors, the appropriate localization/verification telemetry for a floor entry. No further skill is implied by this shape (an identity-in-form floor with no rotation claim to classify). Pass.

### Issues found

No blocking or warning issues. The report is clean against all 8 checks. Minor observations (non-defects, surfaced for the repairer/integrator's awareness, NOT requiring action):

1. **`scaffolding/decisions/...` link reaches outside `book/src/` (cosmetic, precedent-consistent).** The chapter body links `../../../scaffolding/decisions/axpby-as-primitive.md` (`book/src/L2/axpby.md` §Context). The target exists on disk, but it is an out-of-book relative link; mdBook `linkcheck2` treats such links as external and does not hard-fail. The sibling `scal.md` floor (cycle-041 D3, the declared pattern source) uses the same construction, so this is precedent-consistent — flagged only for completeness, not a defect.

2. **`edit:`/`SUMMARY` blocks are anchor-quote-plus-insert, not standalone.** The `edit:book/src/L2/index.md` block (CYCLE.md:479–482) and `edit:book/src/SUMMARY.md` block (484–487) each lead with an exact re-quote of the existing `scal` row/line as the insertion anchor, followed by the new `axpby` row/line. Both anchors are byte-exact matches to the on-disk content (verified), so the insertions are well-formed. Noted so the integrator reads them as "insert-after-scal," not "replace."

3. **Self-declared scope deferrals are correctly out-of-scope (NOT defects).** (a) Count-ownership: the report deliberately does NOT touch the L2/index consolidated firm running-count tally (D2 owns it this cycle) — consistent with the count-ownership partition; the integrator should not increment the absolute firm count from this report. (b) `axpby` L3 staleness: `book/src/L3/axpby.md:6,101,118` do carry the stale "no L2 intermediate because the BLAS-1 primitives are L1 leaves not L2 compositions" framing (verified verbatim at those lines), now superseded by this L2 floor's existence; correctly surfaced as a cycle-044 re-anchor sweep item for the OQ ledger, not a defect of this report. (c) Forward-references `L2-L1/axpby-fusion` and `L3-L2/axpby-body-identity` are left plain-text (targets do not exist yet) per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — confirmed not rendered as live links anywhere in the body.

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
repaired_at: 2026-06-01T110000Z
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

## Repair

### Fixes attempted

The critic returned all 8 checks **pass** with **no blocking or warning issues**. There is no flagged defect to repair. The three items under "Issues found" are explicitly marked by the critic as non-defects surfaced for awareness only; each is informational and requires no repair action:

 - **Finding**: `scaffolding/decisions/...` link reaches outside `book/src/` (cosmetic).
   - **Decision**: not-needed.
   - **Rationale**: The critic confirmed the target exists on disk, `linkcheck2` treats out-of-book relative links as external (no hard-fail), and the sibling `scal.md` floor (cycle-041 D3, the declared pattern source) uses the identical construction. Precedent-consistent, not a defect — editing it would deviate from the established floor-entry pattern, which is a content decision outside repair authority.

 - **Finding**: `edit:`/`SUMMARY` blocks are anchor-quote-plus-insert, not standalone.
   - **Decision**: not-needed.
   - **Rationale**: The critic verified both anchors are byte-exact matches to on-disk content (`index.md:70` scal row; `SUMMARY.md:58` scal line), so both insert-after-scal edits are well-formed and will land. This is correct edit shape, noted only so the integrator reads them as inserts. No defect.

 - **Finding**: Self-declared scope deferrals (count→D2; axpby-L3-staleness→c044 OQ sweep; plain-text forward-refs `L2-L1/axpby-fusion`, `L3-L2/axpby-body-identity`).
   - **Decision**: not-needed.
   - **Rationale**: All three are correctly-scoped-out by the report and confirmed by the critic. Count-ownership respects the cycle-043 D2 partition; the L3 staleness re-anchor is a real cycle-044 follow-up the report properly routes to the OQ ledger rather than touching firm L3 content (substantive authoring, out of scope here AND out of repair scope); the plain-text forward-references follow the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention (targets do not yet exist on disk, so a live link would be a hard `linkcheck2` failure). Nothing to repair.

### Unrepairable findings

None. No finding required deferral; all observations are informational-no-defect.

## Suggested resolution

`ready`. Notes for the integrator:
- Apply the `new:book/src/L2/axpby.md` block and the two anchor-quote-plus-insert edits (`L2/index.md` insert-after-scal; `SUMMARY.md` insert-after-scal). Read both `edit:` blocks as insert-after, not replace.
- Do **not** increment the L2/index consolidated firm running-count tally from this report — count-ownership belongs to cycle-043 D2 per the partition.
- The `book/src/L3/axpby.md:6,101,118` stale "no L2 intermediate" framing is now superseded by this L2 floor; the report routes the re-anchor to the OQ ledger as a cycle-044 sweep item. Promote that OQ at integration; do not edit L3 here.
- The two forward-references (`L2-L1/axpby-fusion`, `L3-L2/axpby-body-identity`) are intentionally plain-text — their targets are not yet on disk. Do not upgrade them to live links.
