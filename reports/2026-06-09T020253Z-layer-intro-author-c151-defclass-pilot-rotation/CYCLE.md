---
agent: layer-intro-author
invoked_at: 2026-06-09T020253Z
scope: c151 D2 FINALIZATION-residue de-bulk PILOT — concepts/rotation.md
status: pending
integrated_at: 2026-06-09T022600Z
integration_commit: 0ce6aeda93e7f5dc1475416bfea7b75358bff4aa
integration_notes: |
  Applied clean as the cycle-151 (batch-50 OPENER) D/E/F FINALIZATION-residue de-bulk PILOT.
  book/src/concepts/rotation.md de-bulked on disk by the producer per the FINALIZATION de-bulk
  convention; integrator-per-report STAGED + ran per-report safety-net gates only (did NOT
  re-apply). Words 2455 → 1859 (−24%); 0 source citations (methodology concept page); graded-stack
  baseline HELD EXACTLY; no inbound anchor broken (all 14 inbound refs file-level). 8/8 critic
  checks PASS, no repairer ran. cargo make book EXIT 0; step-5b tripwire + step-5c KaTeX + step-5d
  frontmatter-leak assertions all PASS; ZERO build-repairs. The strip-vs-lift de-dup judgment
  (report (b)7) flagged for parent bar-confirmation for c152/c153 scale-out (critic verified
  lossless — not a blocker).
---

# CYCLE: concepts/rotation.md de-bulk PILOT (D/E/F residue campaign)

## Summary

Applied `finalization-debulk` (incl. the meta-150 concept-page `## Origin`/`## Working Notes`/`## Critic's role` STRIP rule + the E-class directive-date rephrase rule) to `book/src/concepts/rotation.md` — the cleanest pure-process-narrative pilot target. Edited the file directly (de-bulk convention). The page is a **methodology concept page** with NO `rank:`/`firmness:` frontmatter and NO `## Status` section, so there was **no sole-rank-carrier token at risk** and **no source citation** (no `palace/…:N-M` ranges — methodology pages cite no source). Result: a clean static concept statement of what a *rotation* IS, stripped of all slice-era process accounting.

- Words: **2455 → 1859 (−596, −24%)**.
- Source citations (`palace/…:N-M`): **0 → 0** (none present; methodology page).
- Live cross-references preserved: frontmatter `reference:` edges (`constructed-operators`, `variant-absorption`, `apply_BA`) UNTOUCHED; body backtick cross-ref `book/src/concepts/constructed-operators.md` preserved (1→1).
- Inbound-anchor check: **no inbound link targets any section anchor** of rotation.md anywhere in `book/src` — all 14 inbound references are file-level (`./rotation.md` / `rotation.md`). Removing sections broke nothing.
- Graded-stack lint baseline: **HELD EXACTLY** (`files=392, typed=331, untyped=61, rank_violations=0, unresolved=0, promotion_frontier=11, detritus=123, true_detritus=51`).
- A/B/C/D/E/F residue in the file post-edit: **all 0** (no `## Origin`/`## Working Notes`/`## Critic's role`/`## Context`, no `cycle-N`/`meta-review`/`Synthesizer`/`Critic`/`Meta-Critic`, no `2026-MM-DD`, no `prompts/`·`schemas/`·`rotation_claim.json`, no `CLAUDE.md` pointer).
- Fences balanced (8), no `$`-sigil (KaTeX rule N/A).

## The strip-vs-lift pattern (THE PILOT DELIVERABLE — guides c152/c153 scale-out)

### (a) STRIPPED WHOLESALE (pure process framing, no load-bearing static fact)

1. **`## Critic's role`** — referenced the DELETED `prompts/critic.md`; described retired-orchestrator verdict mechanics (`revise` / `labored_rotation_push_back_candidate` / `push_back_suggestion`). Pure process. The *underlying static criterion* ("when no criterion holds, the rotation is a renaming; respond by merge-or-redesign") was already stated in the kept `## If none of (1)/(2)/(3) hold` section, so nothing was lost.
2. **`## Origin`** — pure process provenance ("Codified during the 2026-05-24 meta-review enactment, in response to cycle 3 … `be11242` … See `meta-reviews/2026-05-24.md`"). Deleted entirely. (Note: the link it carried pointed at a `meta-reviews/` carve-out page, but it was pure process provenance, not a semantic coupling — safe to drop per skill SAFETY "MAY drop a link that pointed only at a process artifact"; the meta-review page retains its own inbound graph independently.)
3. **`## Working Notes`** — forward-process speculation ("Watch the next 3 cycles … If genuine rotations are being rejected, soften the framing … Subsequent meta-reviews should check …"). Deleted entirely — states nothing true *now*.

### (b) MIXED — stripped process framing, LIFTED/KEPT the static fact

4. **`## Context` → folded into a new `## Concept` intro.** The first paragraph (the *definition* of a rotation as an impedance-changing re-expression L_n→L_{n+1}, with the four per-edge impedance shifts) is **load-bearing semantic content** — LIFTED verbatim into the opening `## Concept` section. Stripped from it: the extraction provenance ("extracted during the 2026-05-24 meta-review, in response to cycle 3's friction … GMRES … the rotation collapsed to a renaming"), restated as a *static* definitional clarification of renaming-vs-rotation (no cycle attribution); the "Meta-Critic placed it there" process aside; and the `CLAUDE.md` *Output structure* process pointer (the layer-semantics fact survives in the inline prose).
5. **Date-tagged section headers — dropped the date parenthetical, KEPT the section** (E-class, meta-150 rule). Three section headers carried `(Added 2026-MM-DD meta-review #N after cycle K …)` parentheticals; the sections are load-bearing semantic content:
   - `## Carry-through: not every concept must rotate` — dropped `(Added 2026-05-24 meta-review #2, in response to user feedback …)`.
   - `## Renaming vs. coarser substitution — the algorithmic-substitution test` — dropped `(Added 2026-05-25 meta-review #13 after cycle 50 …)`.
   - `### Framework-tier slices and role-parametrized factories` — dropped `(added meta-23 after cycle 133 cg_preconditioning_framework L1→L2)`.
6. **Retired-orchestrator vocabulary scrubbed from KEPT sections** (the Synthesizer/Critic role names + `prompts/synthesizer.md`/`prompts/critic.md`/`schemas/rotation_claim.json` references). The *static criterion logic* was kept; only the "the Synthesizer applies this pre-emit / the Critic verifies via check #8 / per `schemas/rotation_claim.json`" process-mechanic wrappers were removed. Examples:
   - "`labored_rotation_push_back_candidate` in the Critic's verdict, with the `push_back_suggestion` naming the route" → removed (the merge/redesign responses are the kept static content).
   - "The Critic's check #8 (per `prompts/critic.md`) verifies …" / "the Synthesizer's pre-emit self-check (per `prompts/synthesizer.md`) requires …" → removed; the carry-through static rule kept.
   - `## Justification kinds` "Per `schemas/rotation_claim.json`:" → "A rotation's justification is one of:"; "the rotation_claim's justification" → "the rotation's justification"; "the to_form / from_form" → "the to-form / from-form".
7. **De-duplicated the two layered definitional clusters.** The page had grown TWO restatements of the same criteria — an earlier `## Context … ## What this is NOT` cluster AND a later `## Concept: rotation … ## Slices that use this methodology` cluster (a second authoring's `## Rotation-quality criteria` / `## Renaming vs. coarser substitution` / `## Carry-through` / `## Justification kinds`). Both are semantic, but they restated the same (a)/(b)/(c) criteria. Kept the richer first treatment as the body; preserved the compact rotation-claim phrasing of the criteria as a short `## Rotation-quality criteria (restated)` section (it adds the "named in the justification" framing) + the `## Justification kinds` + `## Slices that use this methodology` sections. No semantic criterion was dropped; the duplicate worked-counter-example (the `x ← x + α·p` → `axpy` renaming illustration) was the same point as the kept `### Worked counter-example: CG L1 → L2`, so the shorter duplicate was folded out. **Flag for scale-out judgment:** this de-dup was a *content* merge of two restatements, slightly beyond pure process-strip — I judged it in-scope because the duplication was itself an accreted-process artifact (two authorings layered without consolidation) and the SEMANTIC-CONSOLIDATION "define once" discipline applies. A more conservative scale-out could keep both clusters; I recommend the consolidation since no criterion is lost. **Noting it explicitly so the parent can confirm the bar.**

### Scale-out guidance (c152/c153)

- The **strip-wholesale set** is reliable: `## Critic's role` (always references deleted `prompts/`), `## Origin`, `## Working Notes` are process-record sections on concept pages → delete, *after* checking each for a buried coupling fact (per (b)4 — `## Context` first-paragraph definitions are the common LIFT case).
- The **`## Context` section is the high-risk LIFT case** — it routinely opens with the concept's actual definition (load-bearing) wrapped in extraction provenance (process). Lift the definition to `## Concept`, strip the provenance.
- **Date-tagged section headers** (`(Added 2026-MM-DD meta-review #N …)`) on *semantic* sections: drop the parenthetical, keep the section (meta-150 E-rule).
- **Retired-orchestrator vocabulary** (`prompts/`, `schemas/`, Synthesizer/Critic/Meta-Critic role names, `rotation_claim`, `push_back_suggestion`, check-#N) appears woven INTO semantic sections, not only in dedicated process sections — scrub the process-mechanic wrapper, keep the static rule it wrapped.
- **Inbound-anchor check is cheap and worth running per file:** `grep -rn '<slug>.md#' book/src` — for rotation.md it was empty (all inbound are file-level). If any inbound `#anchor` exists, do NOT rename/remove that anchor's section.

## Supporting evidence

- Inbound link survey: `grep -rln "concepts/rotation" book/src` → 14 files, all file-level links (`./rotation.md` / `rotation.md`); `grep -rn "rotation.md#"` → empty (no anchor-targeted inbound).
- `prompts/` and `schemas/` confirmed deleted (`ls` → No such file or directory; consistent with CLAUDE.md "decommissioned + DELETED pre-redirect orchestrator").
- Lint baseline before/after identical (see Summary).

## Open questions / caveats

- **Scale-out bar confirmation (flagged in (b)7):** I consolidated two layered definitional clusters that restated the same (a)/(b)/(c) criteria, judging the duplication an accreted-process artifact under the SEMANTIC-CONSOLIDATION "define once" discipline. This is a hair beyond pure process-strip. If the parent prefers the conservative bound (process-strip ONLY, leave content duplication), the c152/c153 dispatches should NOT replicate the de-dup — but I recommend keeping the consolidation, as no criterion was lost and the page reads as a single clean definition.
- No record-definition or named-shape-group obligations triggered (methodology concept page, no signatures naming records).
