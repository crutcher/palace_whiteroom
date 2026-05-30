---
agent: lifter
invoked_at: 2026-05-30T050100Z
scope: L2>L1 theme prose-currency rework — incremental-least-squares-composition-lowering (4-item batch)
status: pending
inputs:
  - book/src/L2-L1/incremental-least-squares-composition-lowering.md
  - book/src/L1-L0/ls-update-column-mutation-rotation.md (target of live-link upgrade; verified on-disk firm c030)
  - book/src/L1/ls-update-column.md (L1 leaf, firm c029; cited in §Status compaction)
  - book/src/L1/back_solve.md (L1 leaf, firm c027; cited in §Status compaction)
  - scaffolding/open-questions.md (OQ closure confirmed at :388 Closed index)
integrated_at: 2026-05-30T051734Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean (cycle-031 D5). 5 prose-currency edits to L2-L1/incremental-least-squares-composition-lowering.md (3 plain-text→live-link upgrades dropping "forthcoming", §Status compaction, §Open-questions cleanup; -33 lines net 591→558). Theme stays firm — structural decomposition unchanged. New OPEN OQ filed: incremental-ls-composition-lowering-residual-forthcoming-mentions-c032 covering 4 residual mentions at :114/:276/:300/:306 bounded out of this dispatch.
---

# CYCLE: prose-currency rework — incremental-least-squares-composition-lowering

## Summary

Bounded prose-rework pass folding four cycle-030-routed items into ONE chapter-touch on `book/src/L2-L1/incremental-least-squares-composition-lowering.md`. Three `ls_update_column-mutation-rotation` plain-text mentions are upgraded to live links AND have their adjacent stale "forthcoming" framing dropped (target file landed firm at `book/src/L1-L0/ls-update-column-mutation-rotation.md` cycle-030 D1). The §Status historical paragraph (c027 deferred-draft vs c028 firm-promotion judgment, then 3 cycles stale) is compacted to current state. Three §Open-questions entries (c027/c028-authored historical judgments, all superseded by c029/c030 leaf-landings + this dispatch's live-link upgrades) are removed. The chapter structure is unchanged; vocabulary stays firm; this is pure hygiene/prose-currency.

## Line-range mapping (c030-reported vs on-disk authoritative)

All c030-reported line numbers verified exactly against on-disk content:

| c030-reported | on-disk verified | content |
|---|---|---|
| `:85` | `:85` (exact) | `forthcoming \`ls_update_column-mutation-rotation\` theme; **this theme stops...` |
| `:466` | `:466` (exact) | `per-column loop body \`iterative.cpp:634-642\`, with its own forthcoming \`ls_update_column-mutation-rotation\`` |
| `:480` | `:480` (exact) | `\`ls_update_column-mutation-rotation\` L1>L0 theme; the \`lowering-verifier\` audit should confirm this` |
| `:429-438` | `:429-438` (exact) | §Status historical paragraph "The one remaining plain-text forward-reference..." through "...NOT this theme's back-solve target." |
| `:448-456` | `:447-456` (bullet header at `:447`, body `:448-456`) | OQ bullet "Firm-promotion judgment record (the one non-mechanical decision)" |
| `:458-467` | `:458-467` (exact) | OQ bullet "`ls_update_column` column-streaming leaf NOT harvested this dispatch (lifter-scope decision)" |
| `:495-499` | `:491-499` (bullet header at `:491`, body `:492-499`) | OQ bullet "OQ ...RESOLVED by this dispatch" (c027 D5 closure record) |

No drift. The c030 routing description gave bullet-body line ranges for the two OQ bullets at 447 and 491; the on-disk bullet headers sit one line above. Edits are applied at full-bullet granularity (header + body) so the `- ` markers are preserved/removed coherently.

## Verification — live-link target is on disk

`book/src/L1-L0/ls-update-column-mutation-rotation.md` confirmed on disk (49766 bytes, 813 lines), header `# ls-update-column-mutation-rotation`, status firm (cycle-030 D1; landed end-to-end GMRES restart-cycle L1>L0 cohort). Relative path from this chapter (`book/src/L2-L1/...`) to the target (`book/src/L1-L0/...`) is `../L1-L0/ls-update-column-mutation-rotation.md`. Confirmed correct.

Open-questions ledger: the c027-deferred OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` is in the Closed index at `scaffolding/open-questions.md:388` (RESOLVED c028 D1). The bullet at chapter `:491-499` referencing it as still-OPEN-and-resolved-by-this-dispatch is stale historical record.

## Proposed changes

### (a1) Line :85 — first plain-text `ls_update_column-mutation-rotation` mention + adjacent "forthcoming"

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: own lowering onto the L0 in-place free functions — the four `*PlaneRotation` calls at
`iterative.cpp:634-642` writing `Hj`, `cs`, `sn`, `s` in place — is the **L1>L0** concern of the
forthcoming `ls_update_column-mutation-rotation` theme; **this theme stops at the L1 leaf and does not
re-derive that L0 in-place step** (the same boundary the sibling draws at the L1 `orthogonalize`
leaf). The [`ls_update_column`](../L1/ls-update-column.md) column-streaming leaf is **firm**
[new]: own lowering onto the L0 in-place free functions — the four `*PlaneRotation` calls at
`iterative.cpp:634-642` writing `Hj`, `cs`, `sn`, `s` in place — is the **L1>L0** concern of the firm
[`ls_update_column-mutation-rotation`](../L1-L0/ls-update-column-mutation-rotation.md) theme
(cycle-030); **this theme stops at the L1 leaf and does not re-derive that L0 in-place step** (the
same boundary the sibling draws at the L1 `orthogonalize` leaf). The
[`ls_update_column`](../L1/ls-update-column.md) column-streaming leaf is **firm**
```

### (a2) Line :466 — subsumed by edit (c); no separate edit fence

The c030-routed `:466` plain-text `ls_update_column-mutation-rotation` mention lives inside §Open-questions bullet 2 ("`ls_update_column` column-streaming leaf NOT harvested this dispatch"), which is fully removed by edit (c) below as a c028-historical-judgment bullet overtaken by c029/c030 events (the leaf IS firm on disk c029 and its L1>L0 theme is firm on disk c030). The routing-described "live-link upgrade + drop forthcoming" at `:466` is therefore eliminated by the bullet's whole-removal — no separate in-place rewrite is needed (and emitting one would conflict with edit (c) at apply time: serial application of two edits that both touch the same bullet would fail). Recorded here so the routing is transparent; the edit-block carrier of the `:466` resolution is edit (c).

### (a3) Line :480 — third plain-text mention + adjacent "forthcoming"

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: - **L1>L0 boundary deferred.** This theme stops at the L1 leaves and does NOT re-derive the L0 in-place
  running-QR mechanics (the four `*PlaneRotation` writes to `Hj`/`cs`/`sn`/`s`) or the back-solve
  in-place `s[0..j]` overwrite (the firm `back_solve` leaf's own L1>L0 concern) or the `x.Add`
  reconstruction (a `linear_combination` concern). The per-column in-place step is the forthcoming
  `ls_update_column-mutation-rotation` L1>L0 theme; the `lowering-verifier` audit should confirm this
  boundary is clean (no duplication of the L0 in-place step across this L2>L1 theme and the leaf L1>L0
  themes).
[new]: - **L1>L0 boundary deferred.** This theme stops at the L1 leaves and does NOT re-derive the L0 in-place
  running-QR mechanics (the four `*PlaneRotation` writes to `Hj`/`cs`/`sn`/`s`) or the back-solve
  in-place `s[0..j]` overwrite (the firm `back_solve` leaf's own L1>L0 concern) or the `x.Add`
  reconstruction (a `linear_combination` concern). The per-column in-place step is the firm
  [`ls_update_column-mutation-rotation`](../L1-L0/ls-update-column-mutation-rotation.md) L1>L0 theme
  (cycle-030); the `lowering-verifier` audit should confirm this boundary is clean (no duplication of
  the L0 in-place step across this L2>L1 theme and the leaf L1>L0 themes).
```

### (b) §Status historical paragraph :429-438 — compact 3-cycle-stale c027↔c028 judgment record

The c027-deferred-draft vs c028-firm-promotion historical reasoning is no longer load-bearing: as of c029/c030 BOTH the `ls_update_column` L1 leaf AND its L1>L0 theme are firm on disk. The paragraph is compacted to a present-tense statement of the firm-vocabulary resolution.

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: The one remaining plain-text forward-reference — the opaque **Face-1** `ls_update_column`
column-streaming leaf — does **not** gate firmness: Face 1 and Face 2 are co-extensive presentations
of the same value ("a resolution choice, not a value choice"), and Face 2 (the de-fused scalar Givens
sequence) is fully firm, so the theme's fan-down value is firm independent of the opaque-leaf face
being on disk. (This is the one judgment that distinguishes this promotion from the deferred draft's
`rough-in`, where the back-solve target was an unanchored general `trsv` forward-ref AND Face-1 was
treated as the sole value-carrier; the re-anchor resolves the back-solve target to the firm
`back_solve` leaf, which is what unblocks `firm` — see the report's §Open questions for the explicit
judgment record.) The general `trsv` is a distinct, separately-blocked L3-inventory operator
(`scaffolding/open-questions.md:24`), NOT this theme's back-solve target.
[new]: Both Face-1 and Face-2 of the L1 RHS resolve to firm vocabulary on disk: the opaque Face-1
[`ls_update_column`](../L1/ls-update-column.md) column-streaming leaf (firm cycle-029,
firm-on-positive-structure) and the de-fused Face-2 scalar Givens kernel pair
([`givens_generate`](../concepts/givens_generate.md) /
[`givens_apply`](../concepts/givens_apply.md)) are co-extensive presentations of the same value, and
the terminal back-solve target is the firm L1 [`back_solve`](../L1/back_solve.md) leaf (cycle-027).
The general `trsv` is a distinct, separately-blocked L3-inventory operator
(`scaffolding/open-questions.md:24`), NOT this theme's back-solve target.
```

### (c) §Open-questions superseded historical-judgment entries — remove three obsolete bullets

Three bullets are c027/c028-authored historical-judgment records, all superseded by c029/c030 leaf-landings:

- **Bullet 1 (lines :447-456, "Firm-promotion judgment record"):** records the c028 promotion-judgment that Face-1 could be opaque-with-firm-by-co-extensiveness. With Face-1 (`ls_update_column`) now firm on disk c029, the judgment is moot — no reviewer can "judge the opaque-leaf forward-ref should still hold the theme at `rough-in`" because there is no forward-ref left.
- **Bullet 2 (lines :458-467, "`ls_update_column` column-streaming leaf NOT harvested this dispatch"):** records the c028 lifter-scope decision NOT to harvest the leaf. The leaf was harvested cycle-029 (firm) and its L1>L0 theme landed cycle-030 (firm). The decision is overtaken by events.
- **Bullet 3 (lines :491-499, "OQ ... RESOLVED by this dispatch"):** records the c028 closure of OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`. That OQ is in the Closed index at `scaffolding/open-questions.md:388` (RESOLVED c028 D1) and the stale `:766` line reference in the bullet is no longer accurate (post-batch-8 meta-phase unification renumbered the open-side mention to `:805`, but more importantly, it's already Closed). The closure record is duplicate of the Closed index.

Surviving bullets are the three forward-looking ones — General `trsv` BLOCKED (`:469-474`), L1>L0 boundary deferred (`:476-482` — edited above per (a3)), L3 sequential-obstruction forecast (`:484-489`).

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: ## Open questions / caveats

- **Firm-promotion judgment record (the one non-mechanical decision).** The deferred c027 D5 draft was
  `rough-in`, gated on the Face-1 `ls_update_column` leaf not being on disk. That leaf is **still not on
  disk**. The promotion to `firm` rests on the judgment that the opaque Face-1 leaf is co-extensive
  with the **firm de-fused Face 2** (the scalar Givens kernel pair) — the theme's fan-down value is
  carried by Face 2 + the now-firm `back_solve` leaf + firm `linear_combination`, so the opaque-leaf
  forward-reference is an alternative presentation, not a value-gate. This matches the sibling
  `orthogonalize-composition-lowering` reasoning where the fan-down rule IS the L2 entry's firm laws
  read as a lowering. If a reviewer judges the opaque-leaf forward-ref should still hold the theme at
  `rough-in` until `ls_update_column` lands, the only change is the `## Status` value (the body is
  unaffected) — flagged here as the explicit judgment so the integrator/critic can confirm or revert.

- **`ls_update_column` column-streaming leaf NOT harvested this dispatch (lifter-scope decision).** The
  distinct, still-un-harvested Face-1 leaf — the per-column running-QR update `ls_update_column(K, j,
  h_new) → K'` (`concepts/incremental-least-squares.md:14`), distinct from the terminal `back_solve` —
  was offered as an optional harvest "only if clean and small". **Decision: NOT harvested.** Harvesting
  a new L1 operator is harvester scope, not lifter scope (a lifter does pure structural re-anchoring,
  not authoring new operators — CLAUDE.md §What you DO NOT do); it is also not required to tighten this
  fan-down (Face 2 already carries the firm de-fused value). Left as a plain-text forward note;
  **flagged for a follow-on harvester** (a small L1 column-streaming leaf whose L0 site is the
  per-column loop body `iterative.cpp:634-642`, with its own forthcoming `ls_update_column-mutation-rotation`
  L1>L0 theme). Suggested plan entry under the `l2-named-composition-lifts` / `back_solve` cohort.

- **General `trsv` remains BLOCKED — not closed by this theme.** The terminal-back-solve target is the
  specific `back_solve` leaf, NOT the general `trsv` / `sparse_triangular_solve` (the Gauss-Seidel /
  ILU smoother kernel on the length-`N` field, no positive L0 anchor, `scaffolding/open-questions.md:24,:498`). The
  re-anchor explicitly demotes the general-`trsv` mention to a forward note and does not claim it
  exists; the `trsv` L3-inventory gap stays open (likely obstruction-theme target). Recorded so the
  `trsv` gap is not falsely treated as touched by this firm theme.
[new]: ## Open questions / caveats

- **General `trsv` remains BLOCKED — not closed by this theme.** The terminal-back-solve target is the
  specific `back_solve` leaf, NOT the general `trsv` / `sparse_triangular_solve` (the Gauss-Seidel /
  ILU smoother kernel on the length-`N` field, no positive L0 anchor, `scaffolding/open-questions.md:24,:537`). The
  re-anchor explicitly demotes the general-`trsv` mention to a forward note and does not claim it
  exists; the `trsv` L3-inventory gap stays open (likely obstruction-theme target). Recorded so the
  `trsv` gap is not falsely treated as touched by this firm theme.
```

(This single edit removes BOTH the "Firm-promotion judgment record" bullet AND the "`ls_update_column` column-streaming leaf NOT harvested this dispatch" bullet — bullets 1 and 2 — while preserving the "General `trsv` remains BLOCKED" bullet at the head of the surviving list. Item (a2) above is subsumed by this edit since bullet 2 is the carrier of the `:466` plain-text mention.)

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[old]: - **OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`
  (`scaffolding/open-questions.md:766`) — RESOLVED by this dispatch.** The c027 D5 deferral is closed: the theme is
  re-anchored to the firm `back_solve` leaf, the `trsv`↔`back_solve` naming reconciled (option (a) from
  the c027 repairer's META: re-point at `back_solve`, demote general `trsv` to a forward note), the
  `ls_update_column` harvest decided (deferred to a follow-on harvester, recorded above), and the theme
  promoted `rough-in → firm`. *Meta-phase action:* migrate the OQ to Closed (answer-link
  `book/src/L2-L1/incremental-least-squares-composition-lowering.md`, status `firm`); the residual
  `ls_update_column`-column-streaming-leaf harvest is a fresh plan candidate (small L1 leaf, follow-on
  harvester), distinct from the now-resolved re-anchor.

[new]: 
```

(Bullet 3 — the OQ-RESOLVED record — fully removed; the OQ closure is recorded authoritatively at `scaffolding/open-questions.md:388` (Closed index).)

## Discipline notes

**Bounded prose-currency rework, no structural change.** The chapter stays firm; the LHS/RHS, the fan-down rule, the reduction-path table, the applicability conditions, the §Verified-against block, and the surviving forward-looking caveats (general-`trsv`-still-blocked, L1>L0-boundary-deferred, L3-sequential-obstruction-forecast) are all untouched. The four edits are: (a1) one in-§L1-form-Face-1 prose paragraph adjusted to firm-pointer + dropped-stale-"forthcoming", (a3) one in-§Open-questions L1>L0-boundary-deferred bullet adjusted to firm-pointer + dropped-stale-"forthcoming", (b) one §Status paragraph compacted from historical judgment to present-tense firm-resolution statement, (c) three §Open-questions historical-judgment bullets removed (their content is overtaken by c029/c030 events and/or duplicated in the OQ Closed index). Item (a2) is subsumed by item (c) — the `:466` mention sits inside bullet 2 of the §Open-questions section, which is removed as a whole.

**Live-link upgrade authority:** per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`, the target file `book/src/L1-L0/ls-update-column-mutation-rotation.md` is verified on disk before the upgrade is proposed. The plain-text-when-anchor-missing convention is honoured in reverse — when the anchor lands, the plain text upgrades.

**Lifter scope boundary respected.** No new operators authored; no signatures changed; no L1 leaf newly cited that wasn't already cited (`ls_update_column` is already firm-cited at lines 87-90, 307-310 elsewhere in the chapter). No re-anchoring of existing citations to different line ranges (no `citecheck --anchor` calls needed — no `path:lo-hi` cites are emitted or modified by these edits; all changes are prose-level inside-the-chapter words). The single new link target (`../L1-L0/ls-update-column-mutation-rotation.md`) is a chapter-relative path with no line range, so the citecheck path-hygiene applies trivially (target exists, no drift possible).

**Out-of-scope "forthcoming" mentions noted:** four additional "forthcoming" mentions exist in this chapter that refer to the same now-firm `ls_update_column` L1>L0 theme via slightly different framings ("forthcoming `ls_update_column` L1>L0 theme" at lines 113, 275, 299, and "firm-or-forthcoming-firm vocabulary" at line 305). These were NOT in the c030-routed scope (the routing named exactly the three slug-spelled-out sites at :85, :466, :480). Per the bounded discipline I do NOT touch them in this dispatch. They are recorded in §Open questions below as a candidate follow-on bounded prose pass.

## Supporting evidence

- Cycle-030 routing description (D3): three `ls_update_column-mutation-rotation` plain-text mentions at `:85`, `:466`, `:480`; §Status historical paragraph at `:429-438`; §Open-questions entries at `:448-456`, `:458-467`, `:495-499`. All line ranges verified exactly on disk in this dispatch.
- `book/src/L1-L0/ls-update-column-mutation-rotation.md` — exists on disk (49766 bytes, 813 lines), header `# ls-update-column-mutation-rotation`, status firm cycle-030 D1. Confirms the live-link upgrade target.
- `scaffolding/open-questions.md:388` — Closed-index record of OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` (RESOLVED c028 D1). Confirms the historical OQ-resolution bullet (chapter `:491-499`) is duplicate-of-Closed-index and removable.
- `scaffolding/open-questions.md:404` — Closed-index record of `ls-update-column-mutation-rotation-l1l0-theme-forthcoming-c029` (RESOLVED c030 D1, "GMRES restart-cycle L1>L0 cohort COMPLETE"). Confirms the firm L1>L0 theme landing this dispatch is upgrading the plain-text refs to.
- `scaffolding/open-questions.md:403` — Closed-index record of `ls-update-column-l2-l1-theme-plain-text-ref-upgrade-to-live-link-c029` (RESOLVED-PARTIAL c030 D6, "3 of 6 mechanical plain-text refs upgraded; the 3 sibling `ls_update_column-mutation-rotation` mentions with adjacent stale 'forthcoming' framing routed to c031"). Confirms this dispatch's scope is exactly the three c031-routed completions.

## Open questions / caveats

- **Out-of-scope `forthcoming \`ls_update_column\` L1>L0 theme` mentions at chapter lines 113, 275, 299, 305.** Four further "forthcoming"-framed references to the same now-firm L1>L0 theme exist in this chapter under a different (non-slug-spelled-out) framing. Not in the c030-routed scope; left untouched per the bounded discipline. Candidate for a small follow-on prose pass — uniformly drop the four "forthcoming" qualifiers (the theme is firm). Suggested plan candidate `incremental-ls-composition-lowering-residual-forthcoming-mentions-c032` (low priority, single-chapter, prose-only). Not blocking.
- **OQ stale line-pointer `scaffolding/open-questions.md:766` inside the removed bullet at :491-499.** The line pointer is post-batch-8-meta-stale (the post-unification new pointer is `:805` for the OPEN-side mention, `:388` for the Closed-index entry). Bullet removal eliminates the stale pointer; no separate fix needed.
- **OQ stale line-pointer `scaffolding/open-questions.md:498` inside the surviving "General `trsv`" bullet at :471 — REPAIRED in repair phase (`:498 → :537`).** Repair-phase mechanical re-anchor: on-disk verification confirmed `scaffolding/open-questions.md:498` is blank (sits inside the cycle-020 `firm-chapter-body-authored-outside-proposed-changes-fenced-block` intake entry; unrelated to `trsv`). The active `trsv` BLOCKED entry lives at `scaffolding/open-questions.md:537` post-batch-8-meta unification. Edit (c)'s `[new]` text has been updated to use `:24,:537` (the `:24` resolved-cycle-028 entry still refers correctly to the closed parent `l3-vocabulary-inventory-gap` plan item). Mechanical re-anchor only — no scope expansion.
