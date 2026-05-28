---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T220000Z
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
repaired_at: 2026-05-28T214634Z
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

# META: verification of "Re-anchor l4-krylov-step-cg-md-citation-sweep"

## Critique

### Checks run

**citation-validity — pass.** This is a pure citation re-anchor; the relevant verification is (i) the 6 edit-block OLD strings match disk byte-for-byte, (ii) the dangling source ranges genuinely dangle, and (iii) the live retained-stub anchors are genuinely in-range. All three confirmed against disk. The 6 OLD strings match `book/src/L4/krylov-step.md` exactly at lines 14, 82, 96, 133, 152, 170-171. `grep -n "cg\.md"` on the entry returns exactly the 8 mentions the report enumerated — 7 dangling-range lines (14/82/96/133/152/170/171) plus the bare-filename mention at 126 (correctly identified as a non-target). `book/src/spec/slices/cg.md` is confirmed `wc -l = 165`, so all four re-anchored ranges (`172-188`, `325-339`, `352-362`, `393-425`) are genuinely out-of-range. The retained Form-B stub anchors the report cites as LIVE are all in-range and verified: `cg_first_step` at stub line 52, `cg_steady_step` at line 69, the `iterate_while_with_prev` driver at lines 95-108, `forget_beta_prev` at line 129 — all ≤165. The out-of-scope co-citations the report leaves untouched are confirmed live: `arnoldi_step.md` (`wc -l = 302`, so `:185-188`/`:285-298` resolve) and `gmres.md` (`wc -l = 671`, so `:459-471`/`:471-489` resolve). The line-150→152 drift the report notes (cycle-015's OQ predicted line 150; actual is 152) is real and harmless — a 2-line Status-paragraph drift; the OLD string is matched on content, not line number.

**surface-or-evidence — pass.** Not a refinement proposal in the rotation_claim sense — this is a pure citation re-anchor with no claim/signature/law/variant-axis/status change, explicitly framed as retroactive-evidence-pointer hygiene (the lifted-evidence-provenance convention inherited verbatim from cycle-013/014/015). The historical `cg.md` range is preserved as parenthetical provenance in every block; the firm home the content was lifted into is named. This is exactly the allowed "pure retroactive evidence backfill" shape. The entry's `firm` status is unchanged and that is correct (verified: the firm homes do not contradict any signature/semantics/law/variant-axis the L4 entry asserts).

**rotation-quality — pass (not applicable to a citation-sweep).** No new algebraic/structural/reduction rotation is asserted. The pre-existing rotation claims in the entry (L4>L2 not-identity-in-form; L3>L2 identity-in-form-on-body; the Form-A/Form-B first-iteration-unrolling state-hiding) are untouched in substance — only the citation pointers anchoring them are re-pointed. No renaming-as-rotation risk.

**variant-axis-coverage — pass.** The six variant axes are inherited unchanged from L2 and are not touched by the sweep. The report explicitly scopes the gmres/arnoldi co-citations (which carry the GMRES/Arnoldi variant instances) out of a `cg.md`-only sweep, and leaves them live. No hidden branch introduced.

**cross-reference-integrity — warning.** All four NEW `[link]` targets the report introduces resolve from `book/src/L4/`: `../L3-L2/krylov-step-body-identity.md`, `../concepts/first-iteration-unrolling.md`, `../concepts/derived-view-hoisting.md`, `../L2/krylov-step.md` (all confirmed present on disk). The CRITICAL terminal-firm-home check (the cycle-015 failure mode — re-anchoring at relocated-dangle targets) was run on each destination and the report's self-verification is accurate:
  - **`L3-L2/krylov-step-body-identity.md` §Verified-against (line 125)** [Re-anchors 1, 4]: confirmed — line 125 carries the verbatim Claim-2 quote ("*…the identity in form: no unfolding, no global lift, no schema change.*", original slice line 360) in firm L3>L2 vocabulary; §Status line 154 is `firm`. The claim DOES live there in firm vocabulary.
  - **`concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" (lines 14-19)** [Re-anchor 3]: confirmed — the CG residual-norm hoisting worked example is held there in firm concept vocabulary; the page's internal `../spec/slices/cg.md` link at line 16 is a BARE filename (no range) that resolves. This is the only re-anchor pointing at a genuinely clean terminal firm home with no residual dangle.
  - **live `cg.md` stub retained material (`cg.md:27-141`)** [Re-anchors 2, 6-FormB, 5-FormB]: confirmed — the v0.5 Form-B derivation is RETAINED live in the 165-line stub, in-range.
  - **`L2/krylov-step.md` §Evidence (line 138)** [Re-anchors 5, 6-FormA]: confirmed — line 138 reads `cg.md:103-115` (CG L2 step body), `:172-188` (CG L4 cg_step), `:393-425` (CG L4 v0.5 split). The Form-A `cg_step` instance is registered there in the L2 narrative registry.

The reason this check is **warning, not pass**: two of the four re-anchor destinations (`L2/krylov-step.md:138` and `L3-L2/krylov-step-body-identity.md:125`) are NOT citation-clean terminal homes — they each carry their OWN dangling `cg.md` ranges (`L2:138` cites the out-of-range `:172-188`/`:393-425`; `L3-L2:125` cites the out-of-range `:341-362`). So a reader who follows the L4 pointer to the named section, then follows THAT section's provenance pointer, lands on a dangling range one hop down. The report is fully honest about this (Discipline notes bullet 3 CAVEATs both; Open-questions item 1 routes them). I assess the resolution as **SOUND, not a deferred dangle**, on three grounds: (a) the re-anchor points at the firm SECTION holding the claim in firm L2 / L3>L2 vocabulary — the content's authoritative home — not at the dangling range, which is the correct semantics for "where does this claim live"; (b) this is the exact established precedent — cycle-015's L3 sweep pointed its line-196 step-body pointer at `L2/krylov-step.md:138` with repairer endorsement (OQ-ledger RESOLUTION note at open-questions.md:2804 confirms "verified — carries the three CG step-body ranges; the repairer corrected this from the producer's transitive-dangling L4:170-171 target"), and the L4 entry's own §Evidence line 176 already declares L2 the transitive narrative anchor, so naming it is consistent with the entry's existing self-description; (c) the residuals are correctly routed — the `l2-krylov-step-cg-md-citation-sweep` OQ is already open in the ledger (open-questions.md:2793, a cycle-016 follow-up), and the report's proposed-new `l3-l2-body-identity-cg-md-citation-sweep` is genuinely absent from the ledger (grep confirms no existing slug), so opening it is the right routing, not a missed dangle. The warning records the multi-hop-to-dangle structural fact for the integrator's awareness; it is NOT a defect in the proposed re-anchors. (Contrast: had the report pointed at L4:170-171 itself — transitive-dangling within the same entry — that WOULD be the cycle-015 failure mode; the report explicitly does NOT do this, pointing instead one level out at the L2 registry.)

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge-label/prose mismatch. The re-anchors touch the L4 entry's own §Context / §Semantics / §Algebraic-laws / §Lowers-to (the L3>L2 row) / §Status / §Evidence prose; each re-anchor's named firm home matches the edge it discusses (Claim 1/2 body-identity → the L3>L2 theme; residual-norm hoisting → the derived-view-hoisting concept; Form A/B → the L2 registry + first-iteration-unrolling concept). Re-anchor 4's bounded future→past tense firm-up (line 133) correctly tracks the landed L3>L2 theme + cycle-010 L3 row, with the parallel future-tense clause at line 14 deliberately left (the report justifies the asymmetry — line 14's clause describes the L4>L3 transition, not made incoherent by the cg.md swap).

**plan-kind-consistency — pass.** Declared as a lifter pure citation re-anchor (`status: pending`, scope `L4 operator-entry re-anchor`). Content shape matches: 6 mechanical citation-pointer swaps preserving structure, no content authoring. The one bounded incidental edit (Re-anchor 4's future→past tense firm-up) is disclosed and justified as link/tense-hygiene forced by the same edit replacing the stale-anchored clause — within the lifter content-correction boundary, not a content/structure change. No rough-in placeholders in a firm-claimed entry; the entry stays firm and the report correctly does not touch the status line's `firm` token.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report's shape — citation-range re-anchor with explicit terminal-firm-home verification of each destination's in-range-ness — is precisely the `verify-citation-range` skill's domain (and its cycle-012 "Audit-report / inherited-citation sub-case" extension). The report's Discipline-notes bullet 3 invokes the discipline by name ("verify-citation-range producer-emit discipline") and performs the per-destination read-and-confirm, but does not cite a SKILL invocation in the `skill-selection` sense. The terminal-home check that the prompt flags as CRITICAL is exactly what a `verify-citation-range`-on-the-destination pass would surface; the report does it by hand. Pure presence telemetry — surfaces that the skill's procedure was followed in substance without an explicit invocation marker.

### Issues found

1. **[multi-hop-to-dangle, low severity] Two re-anchor destinations carry their own dangling `cg.md` provenance ranges.** Location: report §"Proposed changes" Re-anchors 5/6 (→ `L2/krylov-step.md:138`) and Re-anchors 1/4 (→ `L3-L2/krylov-step-body-identity.md:125`); flagged by the report itself in Discipline-notes bullet 3 + Open-questions item 1. `L2/krylov-step.md:138` cites out-of-range `cg.md:172-188`/`:393-425`; `L3-L2/krylov-step-body-identity.md:125` cites out-of-range `cg.md:341-362`. A reader following the L4 pointer → named section → that section's provenance pointer lands on a dangling range one hop down. NOT a defect in the proposed re-anchors (they point at the firm section, which holds the claim in firm vocabulary — the correct semantics, and the established cycle-015 precedent per OQ-ledger:2804). Recorded for integrator awareness; the residuals are correctly routed to sibling sweeps. No repair needed on THIS report's edits.

2. **[routing, informational] One residual sibling-sweep OQ is genuinely new; one is already filed.** Location: report §Open-questions item 1 + item 2. Verified against `scaffolding/open-questions.md`: `l2-krylov-step-cg-md-citation-sweep` is ALREADY open (ledger line 2793, a cycle-016 follow-up) — the report correctly recommends keeping it open. The report's proposed-new `l3-l2-body-identity-cg-md-citation-sweep` is genuinely ABSENT from the ledger (grep returns no existing slug) — opening it is correct routing, not a missed dangle. The `first-iteration-unrolling-cg-md-citation-sweep` possibility (report Open-questions item 2) is correctly flagged as unaudited-this-dispatch (the concept page was not opened) and out-of-scope; it may or may not exist depending on whether that page carries range-bearing `cg.md` pointers — a defensible scope boundary, not an omission.

3. **[telemetry, non-blocking] No explicit `verify-citation-range` skill-invocation marker** despite the report's terminal-firm-home check being squarely that skill's domain (and its cycle-012 inherited-citation sub-case). Location: report §Discipline notes bullet 3. The procedure is followed in substance (each destination read and confirmed in-range / firm); only the explicit invocation marker is absent. Surfaced as skill-uptake telemetry per the check's pure-presence nature; not a content defect.

4. **[scope note, no action] §Status roll-call "four slices' explicit L4 sections" count.** Location: Re-anchor 5 NEW text (line 152). The OLD enumerated four sections (cg:172-188, cg:393-425, gmres:459-471, arnoldi:285-298); the NEW text re-expresses the two CG sections as "CG L4 Form A … and L4-v0.5 Form B … lifted into the firm `L2/krylov-step.md` §Evidence registry … the Form B v0.5 derivation remains live in the reduced slice at cg.md:27-141" while keeping gmres/arnoldi ranges live. The "four slices" framing in the surrounding prose is preserved by the NEW text's parenthetical (still naming all four section sources). No undercount introduced; recorded for completeness only.

---

## Repair

### Fixes attempted

- **Finding** (cross-reference-integrity, warning — Issue 1): Two re-anchor destinations (`L2/krylov-step.md:138`, `L3-L2/krylov-step-body-identity.md:125`) carry their own dangling `cg.md` provenance ranges — the multi-hop-to-dangle structural fact.
  - **Decision**: not-needed.
  - **Rationale**: The critic assessed the producer's "point at the firm section" resolution as SOUND, not a deferred dangle, on the cycle-015 precedent (OQ-ledger RESOLUTION note at `open-questions.md:2804`). The re-anchors point at the firm SECTION holding the claim in firm L2 / L3>L2 vocabulary — the correct "where does this claim live" semantics — not at the dangling range. The critic explicitly states "No repair needed on THIS report's edits." The structural fact is recorded for integrator awareness only. No edit to the report's proposed-changes applies. The residuals are correctly routed to sibling sweeps (see the OQ finding below).

- **Finding** (cross-reference-integrity, informational — Issue 2 / Open-questions routing): The critic recommends a NEW OQ `l3-l2-body-identity-cg-md-citation-sweep` (grep-confirmed absent from the ledger) be captured so the integrator promotes it.
  - **Decision**: not-needed (already captured; verified not missing).
  - **Action / verification**: Confirmed `l3-l2-body-identity-cg-md-citation-sweep` is genuinely ABSENT from `scaffolding/open-questions.md` (grep returns no slug match). Confirmed `l4-krylov-step-cg-md-citation-sweep` (parent OQ) present at ledger line 2780 and `l2-krylov-step-cg-md-citation-sweep` already open at line 2793. The report's CYCLE.md §"Open questions / caveats" item 1 (line 101) ALREADY names the new slug and explicitly recommends "OPEN a NEW OQ `l3-l2-body-identity-cg-md-citation-sweep`" with its scope (the body-identity theme's own dangling `cg.md:341-362` provenance pointer + an out-of-scope `gmres.md` co-pointer) and routing (a separate lifter dispatch on a different file). This is the identical prose-recommendation shape the cycle-015 sibling used for its two follow-up OQs (`l4-`/`l2-krylov-step-cg-md-citation-sweep`), which integrator-per-report successfully parsed and promoted into structured ledger `slug:` entries (lines 2780/2793). The new OQ is therefore already in a promotable form; the prompt's conditional "add it surgically if missing" resolves to NOT-MISSING. No surgical edit to CYCLE.md required.

- **Finding** (skill-uptake-survey, warning — Issue 3): No explicit `verify-citation-range` skill-invocation marker despite the report's terminal-firm-home check being squarely that skill's domain.
  - **Decision**: not-needed.
  - **Rationale**: Pure presence telemetry per the check's own non-blocking nature — the critic confirms the procedure is followed in substance (each destination read and confirmed in-range / firm), only the explicit invocation marker is absent. Not a content defect; nothing to fix mechanically.

### Unrepairable findings

None. All flagged findings are informational / telemetry / already-captured; none require substantive authoring or exceed repair authority.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

1. **Promote the new OQ `l3-l2-body-identity-cg-md-citation-sweep`** from CYCLE.md §"Open questions / caveats" item 1 — it is genuinely new (grep-confirmed absent from the ledger) and named in the same promotable prose-recommendation form the cycle-015 siblings used. Keep the already-open `l2-krylov-step-cg-md-citation-sweep` (ledger line 2793) open.
2. **OQ `l4-krylov-step-cg-md-citation-sweep` (ledger line 2780) may be marked `answered`** with answer-link this CYCLE.md, contingent on the 6 re-anchor blocks landing — this dispatch addresses it in full for `book/src/L4/krylov-step.md` (all 7 dangling range-pointer lines re-anchored; the 1 bare-filename mention at line 126 correctly left untouched).
3. The two-hop-to-dangle structural fact (cross-reference-integrity warning) is recorded for awareness; it is NOT a defect in the re-anchors (they point at the firm section, the correct claim-home semantics, per the cycle-015 precedent). The residuals are routed to the sibling sweeps above.
