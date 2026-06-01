---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T133000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T134500Z
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

# META: verification of "Audit orthogonalize (L3 partial-obstruction)"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the report returns 33 ok / 0 failing.
I spot-checked the load-bearing pinpoints via `--anchor` and Read, all confirming the report's
structural claims against on-disk source: (a) the MGS interleave — `dot_op` at `orthog.hpp:49`,
`Mpi::GlobalSum` at `:50`, `w.Add(-H[j], V[j])` at `:51`, all inside the same `j`-loop opened at
`:46`, with `w.Add` mutating `w` in place so the next iteration's `dot_op(w, V[j])` reads the
subtracted `w` (loop-carried serial — the obstruction witness); (b) CGS dots-against-original — the
`:66-69` loop reads the un-mutated `w` (no `w.Add` inside), then a single `GlobalSum(m, H, comm)` at
`:70` and a batched `w.Add` loop `:71-74`, with the `refine`/CGS2 second pass `:75-88` reading the
once-projected `w` at `:80` (`dH[j] = dot_op(w, V[j])`); (c) the no-output-normalisation boundary —
`orthog.hpp:22` "does not normalize the output vectors" anchor OK, honoured at GMRES
`iterative.cpp:630/:631/:632` (`OrthogonalizeIteration` → `Norml2` → `w *= 1.0/Hj[j+1]`) and FGMRES
`:809-811`; (d) `test-orthog.cpp:158` `WithinAbs(0.0, 1e-12)` anchor OK, `:234` `Complex 1` anchor
OK. The proposed `verified_against:` block (24 rows) round-trips under `yaml.safe_load` and NO
`note:` value begins with `'` or `"` (the `verified-against-note-no-leading-quote-of-either-kind`
guard is satisfied; every note opens with prose). The minor `:62-64` vs `:62-65` boundary the report
self-flags is in-bounds and not a drift (the `return` is at `:64`, the closing `}` at `:65`). No
citation issues.

**surface-or-evidence — pass.** This is a lowering-verifier audit: primarily a retroactive
evidence backfill (the `verified_against:` block) plus co-located correctness fixes (Changes 2/3/4
reconcile a stale cross-reference). The retroactive-evidence framing is explicit and the surface
edits modify the entry's own prose with cited justification. Within scope.

**rotation-quality — pass.** The audit does not assert a NEW rotation; it confirms the existing
partial-obstruction verdict (MGS loop = sequential-obstruction, non-lifting; CGS/CGS2 lift because
the basis index is a batched reduction axis). The substantive variant-split rotation it points at
(`orthogonalize-variant-split` theme, D3) is genuinely a loop-structure rewrite (MGS `j`-recurrence
→ L2 per-variant sequencing; CGS batched-arm → L2 collective-shape residual axis), not a 1:1
rename. The body-identity is correctly kept separate (in-line note) from the substantive loop
rotation (dedicated theme). Consistent.

**variant-axis-coverage — pass.** All three `gs_orthog` variants (MGS/CGS/CGS2) plus the dot-hook
axis (canonical / B-weighted) and element-type axis (real/complex) are addressed; the lift verdict
explicitly SPLITS on `gs_orthog` and is invariant under the dot-hook and element-type axes (Law 7,
test `:234`). No hidden branch — the `OrthogonalizeIteration` `switch(type)` at
`iterative.cpp:313-323` is the complete dispatch and each Column* body is variant-free.

**cross-reference-integrity — warning.** All resolved cross-references check out: the two existing
live-link theme targets `orthogonalize-mutation-rotation.md` and
`orthogonalize-composition-lowering.md` exist on disk; all intra-book citation ranges (L2:133-134,
:290-292; L1:200-203; sequential-obstruction:22,:37-48; variant-absorption:131) are in-range. The
edit-target line numbers resolve precisely against the current on-disk c040 state: line 8
(`lowers_to:` "no L3-L2 theme file"), lines 402-408 ("The L3>L2 edge is identity-in-form... no
`L3-L2/` theme file"), and lines 479-483 ("No `L3-L2/` theme file — ...") all match the quoted
`old`-text. The warning is the **single dangling live link**: Changes 2/3/4 introduce
`[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md)` whose target does NOT
exist on disk (D3's co-land output). This is a sequencing dependency, not a defect — the report
flags it explicitly with a correct carry-forward (apply after D3, or demote to plain text per
`rough-in-forward-reference-must-be-plain-text-not-live-link`). Surfaced as a warning so the
integrator does not lose the ordering constraint at apply time.

**edge-label-fidelity — pass.** The edges discussed match their labels throughout: the L3>L2 edge
prose discusses exactly the L3→L2 hop (body identity + variant-split loop rotation); the L1>L0 and
L2>L1 references in Change 2 correctly name their respective edges; the `verified_against:` rows tag
L0 / L0-equivalent (test) / intra-book citations correctly.

**plan-kind-consistency — pass.** Declared kind is an L3 operator audit. The status correctly stays
`partial-obstruction` — the report finds NO contradiction and does NOT silently flip the status
(explicitly noted in §Open-questions). The top-level verdict `fully-supported` is justified: all 24
anchors return `supports` with zero drift, independently confirmed here. The content shape (per-
citation audit + applicability conditions + algebraic laws + non-laws + `verified_against:` append)
matches a lowering-verifier audit exactly.

**skill-uptake-survey — pass.** The report references the relevant procedures: `citecheck.py
--anchor` (the `verify-citation-range` mechanical realization), the `codemap-read-range-plus-one-drift`
guard (on-disk reads, not codemap), the `verified-against-note-no-leading-quote-of-either-kind` YAML
guard, and the `rough-in-forward-reference-must-be-plain-text-not-live-link` fallback for the
dangling link. Telemetry present.

### Issues found

1. **[warning] Dangling live link pending D3 co-land** — `book/src/L3/orthogonalize.md` Changes
   2/3/4 (report §Proposed changes, edit blocks at report lines 359-374, 382-392, 399-402) introduce
   a live markdown link to `../L3-L2/orthogonalize-variant-split.md`, which is NOT on disk at audit
   time (confirmed: `ls` returns "No such file or directory"). If D3 lands first (per the plan's
   D1→D3→D4 sequencing) the link resolves and `linkcheck2` passes; if D3 is rejected/deferred, the
   three live links must be demoted to plain text or Change 2/3/4 deferred. The report flags this
   correctly in §Open-questions — recorded here so the integrator carries the ordering constraint.
   Severity: low (sequencing, not content).

2. **[informational, not a defect] D1 same-file line-number overlap** — D1 (cycle-044) also
   re-anchors this entry's audit-block citations and may touch §Lowers-to. The report's edit targets
   (lines 8, 402-408, 479-483) are c040 line numbers; if D1 shifts them, the integrator must
   re-resolve by the quoted `old`-text (which each edit block supplies in full) rather than absolute
   line number. Verified the `old`-text quotes match the current on-disk state exactly, so text-
   anchored re-resolution is reliable. Change 1 (EOF append) is line-number-independent. No genuine
   overlap defect — the edits target disjoint regions (D1: audit-block citations / §Lowers-to prose
   vs. D4: the `lowers_to:` frontmatter "no L3-L2 theme file" clause) and are text-anchored.
   Integrator should apply with text-match, not line number.

3. **[informational] Change-2 preamble line-reference** — the Change-2 prose preamble cites "line
   408" for the stale sentence while the edit block replaces "lines 402-408". Consistent (line 408
   is the load-bearing "no `L3-L2/` theme file" sentence inside the 402-408 block); noted only for
   completeness, no action.

### Fence parity

Report fence count = 10 (even). Change 1 carries a nested ```yaml``` (report lines 243-341) inside
the ```edit:``` fence (241-342) — balanced nested pair. Changes 2/3/4 are single edit-fence pairs
(359/374, 382/392, 399/402), all balanced. The `## Status: partial-obstruction` apparatus is NOT
re-authored in a proposed-changes block (this is an evidence-append + prose-reconciliation audit,
not a firm-body author), so the firm-body-inside-fence guard is not triggered. No fence defect.

## Repair

### Fixes attempted

- **Finding**: [warning] Dangling live link pending D3 co-land — Changes 2/3/4 introduce a live
  markdown link to `../L3-L2/orthogonalize-variant-split.md`, which is not on disk at audit time.
  - **Decision**: not-needed (informational-no-defect).
  - **Rationale**: This is a sequencing dependency, not a content defect. The link target
    (`book/src/L3-L2/orthogonalize-variant-split.md`) co-lands from D3 this same cycle; the
    integrator applies D1→D3→D4, so by the time D4's link is written the target exists on disk and
    `linkcheck2` passes. The report already flags this explicitly in §Open-questions with the
    correct carry-forward fallback (demote to plain text per
    `rough-in-forward-reference-must-be-plain-text-not-live-link` if D3 does not land). Repairing
    would require either authoring the missing D3 theme file (substantive authoring — out of repair
    scope) or pre-emptively demoting a link the report intentionally left live pending co-land
    (which would override the report's correct sequencing-aware design, not fix a defect). Neither
    is a mechanical surgical fix; the sequencing is handled correctly by integration ordering. No
    edit applied.

- **Finding**: [informational, not a defect] D1 same-file line-number overlap — D1 (cycle-044) also
  re-anchors this entry; the report's c040 line-number edit targets may shift.
  - **Decision**: not-needed (informational-no-defect).
  - **Rationale**: The critic confirmed the edits target disjoint, text-anchored regions (D1: audit-
    block citations / §Lowers-to prose vs. D4: the `lowers_to:` "no L3-L2 theme file" clause) and
    that every `old`-text quote matches current on-disk state exactly. Text-anchored re-resolution
    is reliable; this is an apply-time note for the integrator, not a repairable defect.

- **Finding**: [informational] Change-2 preamble line-reference ("line 408" vs. edit block "lines
  402-408").
  - **Decision**: not-needed.
  - **Rationale**: The critic confirms these are consistent (line 408 is the load-bearing sentence
    inside the 402-408 block). Noted for completeness; no action.

### Unrepairable findings

None. The single warning is a sequencing dependency resolved by integration application order, not
an unrepairable content defect. No follow-up agent required.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

1. **Enforce D1→D3→D4 application order this cycle.** D4 (this report) introduces a live link to
   `../L3-L2/orthogonalize-variant-split.md` whose target is D3's co-land output. Applying D3 before
   D4 makes the link resolve and `linkcheck2` pass.
2. **Fallback if D3 does not land** (rejected/deferred): demote the three live links in Changes
   2/3/4 to plain text per `rough-in-forward-reference-must-be-plain-text-not-live-link`, or defer
   Changes 2/3/4. The report flags this in §Open-questions.
3. **Apply by text-match, not absolute line number.** D1 may shift this entry's line numbers; the
   edit blocks supply full `old`-text quotes that match current on-disk state (critic-verified), so
   text-anchored resolution is reliable. Change 1 is an EOF append (line-number-independent).
