---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T053000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-05-30T060000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of lifter incremental-least-squares-composition-lowering prose-currency rework

## Critique

### Checks run

**citation-validity — pass.** No new `path:lo-hi` citations are introduced. The single new link target — `book/src/L1-L0/ls-update-column-mutation-rotation.md` — is path-only (no line range), so `tools/citecheck/citecheck.py` line-map adjudication is N/A. Cross-checked the four "supporting evidence" assertions: `book/src/L1-L0/ls-update-column-mutation-rotation.md` exists on disk (49766 bytes, matching the report's claim); `scaffolding/open-questions.md:388` is the Closed-index entry for `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` (verified verbatim); `:403`/`:404` Closed-index entries for the c029 partial-resolution + c030 forthcoming-firm closures also verified verbatim. The report's note that the OPEN-side mention moved from `:766` (pre-batch-8 meta) to `:805` (post-unification) is verified — `scaffolding/open-questions.md:805` carries the active OPEN-side line. No `verified_against:` YAML block is being emitted (this is a prose-rework, not an audit), so the round-trip sub-check is N/A.

**surface-or-evidence — pass.** This is surface-modifying (chapter text editing: 5 edit blocks against `book/src/L2-L1/incremental-least-squares-composition-lowering.md`). All edits are prose hygiene + live-link-upgrade + bullet-removal of OBE historical-judgment records — no algebraic claims or new vocabulary added. The "rotation_claim without surface" failure mode is N/A.

**rotation-quality — pass.** N/A to a prose-currency rework. The chapter's fan-down rule, dispatch rule, reduction-path table, applicability conditions, and verified-against block are explicitly unchanged. The report calls this out: "vocabulary stays firm; this is pure hygiene/prose-currency."

**variant-axis-coverage — pass.** N/A — no operator/theme variant-axis content is being added or rewritten. The chapter's existing `op.variant` × `op.basis_kind` axis coverage is untouched.

**cross-reference-integrity — warning.** Live-link target exists (verified on disk). The 3 plain-text→live-link upgrades (`../L1-L0/ls-update-column-mutation-rotation.md` in edits a1/a3 + the (b)-introduced `../L1/ls-update-column.md`, `../concepts/givens_generate.md`, `../concepts/givens_apply.md`, `../L1/back_solve.md`) all resolve to on-disk files. The 6 `edit:` proposed-changes fences are all balanced (even fence parity, 12 markers verified at report-internal lines :46/:58/:62/:75/:81/:96/:102/:121/:133/:172/:176/:188 — 6 open + 6 close pairs); each `[old]` block was verified unique-in-target (`grep -c` returns 1 for each load-bearing anchor: "own lowering onto the L0", "L1>L0 boundary deferred", "The one remaining plain-text", "Firm-promotion judgment record", "OQ \`incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor\`"). The warning is for one stranded-cross-reference concern: the surviving "General `trsv` remains BLOCKED" bullet (kept by edit (c)) contains the line-pointer `scaffolding/open-questions.md:24,:498` — the report acknowledges (at its §Open-questions caveat 3) that `:498` was NOT verified this dispatch and may be post-batch-8-meta-stale, but does not fix it. This is a known-not-fixed stranded reference inside the surviving bullet that this dispatch is recording for future cleanup; flagged as warning rather than fail because the report is explicit about leaving it alone.

**edge-label-fidelity — pass.** N/A to a prose-rework; no edge labels are added or modified. The chapter remains L2>L1 throughout; the (a3) live-link upgrade preserves the existing "L1>L0 theme" phrasing for the linked target.

**plan-kind-consistency — warning.** Declared kind matches content shape — a `lifter` doing bounded prose-currency on a firm L2>L1 theme is in-scope (no new operators authored, no signatures changed, lifter discipline respected per CYCLE.md §"Lifter scope boundary respected"). The warning is for a real overlap/sequencing concern in the proposed-changes block: edit **(a2)** at report lines 62-75 declares `[old]` = bullet 2's body (lines :458-467 in the target chapter) with `[new]:` empty, AND edit **(c)** at report lines 133-172 declares an `[old]` that ENCLOSES the same bullet 2 (from `## Open questions / caveats` through bullet 1 AND bullet 2's full body). If the integrator applies the 5 edit blocks serially in declaration order, (a2) removes bullet 2 first, then (c)'s `[old]` will not match the on-disk file (bullet 2 is no longer there). The report itself flags this at its line 77 ("bullet (a2) is fully removed as part of item (c) below ... routing-described 'live-link upgrade + drop forthcoming' is subsumed by the bullet's removal"), which signals the dispatcher's intent that (a2) be skipped / treated as documentary, but the edit block is STILL emitted as a real `edit:` fence the integrator will try to apply. Mark as warning (not fail) because the intent is explicit; flag for the repairer/integrator as a real apply-time hazard.

**skill-uptake-survey — pass.** Report explicitly cites the relevant skill in §Discipline notes: `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (with target-on-disk verification recorded before the upgrade). Report also notes that `citecheck --anchor` calls are not needed (no `path:lo-hi` cites added/modified) — correct invocation discipline. Skill citation is present and matches the actions taken.

### Issues found

- **Edit-block overlap: (a2) and (c) both delete bullet 2 of §Open-questions** [CYCLE.md §"Proposed changes" (a2) at report lines 62-75 vs (c) at report lines 133-172; severity: medium]. The (a2) `edit:` fence declares an `[old]` = bullet 2 body, `[new]:` empty — a pure deletion. The (c) `edit:` fence declares an `[old]` that opens at the `## Open questions / caveats` header and includes bullet 1 + bullet 2 together, with `[new]:` keeping only the General-`trsv` bullet at the head. Applied serially in declaration order, (a2) deletes bullet 2 first, then (c)'s `[old]` text will not match the on-disk file (bullet 2 is no longer present), causing an apply-time failure. The report acknowledges the overlap (line 77 "subsumed by ... bullet's removal") but emits BOTH edit fences anyway. Repair candidate: drop the (a2) edit fence entirely (the routing description can stay as documentary prose) so the (c) edit fence is the sole carrier of the deletion.

- **Surviving bullet carries an un-verified stale line-pointer** [CYCLE.md §Open-questions caveat 3 at report lines 213-214 vs target chapter :471 / surviving "General `trsv`" bullet referencing `scaffolding/open-questions.md:24,:498`; severity: low]. The (c) `[new]` text preserves the existing `:498` line-pointer inside the surviving bullet. The report is explicit that `:498` was NOT verified this dispatch and may be post-batch-8-meta-stale. This is a known-untouched stranded cross-reference inside the post-edit surface. Not blocking (the report flags it for a future bounded sweep); flagged as a candidate cleanup if the repairer wants to verify mechanically without scope expansion.

- **Out-of-scope "forthcoming" mentions at chapter lines :113, :275, :299, :305 are deferred to a follow-on c032 candidate** [CYCLE.md §Discipline notes at report line 200 + §Open-questions caveat 1 at report lines 211-212; severity: informational]. Verified via `grep -n "forthcoming"` against the target chapter: lines 113, 275, 299 carry "forthcoming `ls_update_column` L1>L0 theme" framings of the same now-firm theme that the in-scope :85/:466/:480 sites reference; line 305 carries "firm-or-forthcoming-firm vocabulary" in the §Speculative-L1-operators boilerplate. The c030 routing explicitly named only the three slug-spelled-out :85/:466/:480 sites, so the deferral is correctly scoped — the lifter is honouring bounded discipline rather than expanding scope ad hoc. The report flags this as a candidate `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` plan candidate. This is the textbook bounded-scope behaviour; not a defect, but worth surfacing so the repair/integration phase doesn't itself try to expand scope. Additionally lines 15 and 203 carry "forthcoming L2>L1 theme" framings that are quoted-historical-reference to the L2 entry's deferred-non-law text — those are NOT obsolete (the L2 entry's :278-285 still uses that phrasing as historical-record) and would be inappropriate to touch even in the follow-on sweep. The follow-on c032 candidate should scope to lines 113/275/299/305 only.

- **(b) edit replacement text drops the explicit reviewer-revert-option judgment** [CYCLE.md §(b) at report lines 102-121; severity: low]. The original :429-438 §Status paragraph carries the explicit "If a reviewer judges the opaque-leaf forward-ref should still hold the theme at `rough-in` until `ls_update_column` lands, the only change is the `## Status` value (the body is unaffected)" framing that records the firm-promotion judgment's reversibility. The (b) `[new]` text compacts this to a present-tense firm-resolution statement without preserving the reviewer-revert affordance. With `ls_update_column` now firm on disk c029 the reviewer-revert path is moot (no plain-text forward-ref left to gate on), so the deletion is materially correct — but is essentially a permanent erasure of the historical-judgment record. Not a defect (the report's own logic is sound — the judgment is overtaken by events) but worth flagging because the §Status paragraph is the only chapter location carrying the historical record of why the c028 promotion was made (the (c) edit also removes the bullet-1 carrier of the same record). Combined effect: the c028 firm-promotion judgment record is fully erased from the chapter. Git log preserves it; if the methodology requires in-chapter retention of firm-promotion judgments, this is a candidate concern. Flag for repair/integrator awareness only.

## Repair

### Fixes attempted

- **Finding**: Edit-block overlap — (a2) and (c) both delete §Open-questions bullet 2 ("`ls_update_column` column-streaming leaf NOT harvested this dispatch"); serial application of both fences would fail because edit (c) encloses the bullet (a2) pure-deletes.
  - **Decision**: repaired
  - **Action**: Dropped the entire (a2) `edit:` fence from `reports/2026-05-30T050100Z-lifter-incremental-ls-prose-currency-rework/CYCLE.md` §"Proposed changes" §(a2). Replaced the §(a2) heading block (formerly an edit fence + post-fence note) with a single explanatory paragraph stating that the c030-routed `:466` mention is the in-bullet-2 mention, and bullet 2 is removed in toto by edit (c), so no separate fence is needed (and emitting one would conflict with (c) at apply time). The fence count drops from 6 to 5; surviving fences are (a1) :85, (a3) :480, (b) §Status :429-438, (c) first-fence (bullets 1+2 deletion, General-`trsv`-bullet preserved-with-`:537`-substitution), (c) second-fence (bullet 3 deletion). Verified each surviving `[old]` is unique-in-target via `grep -c` on the five load-bearing anchors ("own lowering onto the L0 in-place", "L1>L0 boundary deferred", "The one remaining plain-text forward-reference", "Firm-promotion judgment record", "incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor") — all return 1. Fence parity verified: 5 edit-open + 5 close = 10 markers, even. Edits are mutually disjoint and apply cleanly in any serial order.
  - **Rationale**: Mechanical overlap fix per the role-spec "trivial cross-reference fix" / "Methodology-level concerns the critic flagged for meta-phase attention" boundary — the report's own prose at line 77 already states that (a2) is "subsumed by item (c)"; the repair just makes the proposed-changes section honour that statement by dropping the redundant fence. No content authoring required; no substantive judgment. The two surviving (c) fences are the sole carriers of the `:466` resolution (via whole-bullet deletion).

- **Finding**: Cross-reference-integrity — the surviving "General `trsv`" bullet preserves a `scaffolding/open-questions.md:498` line-pointer flagged as possibly post-batch-8-meta-stale; CYCLE.md §Open-questions caveat 3 explicitly noted the line was not verified.
  - **Decision**: repaired
  - **Action**: Verified `:498` is stale on disk: `scaffolding/open-questions.md:498` is blank, sitting inside the cycle-020 `firm-chapter-body-authored-outside-proposed-changes-fenced-block` intake entry (unrelated to `trsv`). Searched the OQ ledger for the active `trsv` BLOCKED entry: it now lives at `scaffolding/open-questions.md:537` (post-batch-8-meta unification moved it). The `:24` companion line still references correctly (the resolved-cycle-028 `l3-vocabulary-inventory-gap` parent plan item). Updated edit (c)'s first-fence `[new]` text in CYCLE.md from `scaffolding/open-questions.md:24,:498` to `scaffolding/open-questions.md:24,:537`. Also updated CYCLE.md §Open-questions caveat 3 to record the repair (not-edited → REPAIRED, `:498 → :537`, with the on-disk verification rationale).
  - **Rationale**: Mechanical stale-line-pointer re-anchor — the critic asked to "verify the `:498` reference on disk; if stale, correct it; if fine, note so." On-disk verification confirmed staleness; the correct anchor is `:537`; the substitution is a single 3-digit literal change in (c)'s `[new]` text. No content authoring; no scope expansion (the bullet itself is not re-written, only its line pointer). Per the role-spec "Citation line range off by a small offset (a few lines slip)" repair authority — this is the larger-offset analog produced by a global OQ-ledger compaction, but the principle is identical: the producer's pointer is mechanically off-by-a-known-amount and the correct value is single-lookup verifiable.

### Unrepairable findings

None. Both warnings were mechanically repairable in scope; no findings require substantive authoring or contradict existing artifact content. The two informational/low-severity issues raised by the critic that were NOT formal warnings (out-of-scope "forthcoming" mentions at chapter lines 113/275/299/305 deferred to a c032 candidate; (b) edit dropping the reviewer-revert-option judgment) are flagged-for-awareness only and explicitly out-of-scope per the report's own bounded discipline — no repair action taken on either, none warranted.

## Suggested resolution

`ready` — the per-report integrator may apply the 5 surviving edit fences in declaration order. All `[old]` anchors are unique-in-target on disk; all `[new]` substitutions preserve fence parity. The `:498 → :537` re-anchor inside edit (c)'s first-fence `[new]` is the only line-pointer change relative to the on-disk text and corrects a known-stale (post-batch-8-meta) pointer to the active OQ-ledger location. No build-time hazards expected (this is a prose-rework with no new code, no new YAML, no dep-map row changes, no SUMMARY entry). The c032 follow-on "forthcoming" mentions at chapter lines 113/275/299/305 remain a separately-routable plan candidate; not blocking this cycle's integration.
