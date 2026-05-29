---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T100000Z
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
repaired_at: 2026-05-29T103000Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Audit orthogonalize-composition-lowering"

## Critique

### Checks run

**citation-validity — pass.** This is the load-bearing check for a confirming audit, and it
holds. I independently re-read the cited L0 source via `palace-codemap` `read_range` and ran
`tools/citecheck/citecheck.py` anchor-drift checks on a spread of the 17 `verified_against`
citations. Every anchor the auditor asserts lands where claimed: `orthog.hpp:35` =
`return LocalDot(x, y);` `[ok]` (line 34 is the brace `{`, confirming the auditor's `:35`-not-`:34`
directive); MGS `:49` dot `[ok]`, `:51` `w.Add` (read directly), GlobalSum-1 `:50` (read
directly); CGS `:62` `if (m == 0)` `[ok]`, `:70` `Mpi::GlobalSum(m, H, comm)` `[ok]`, `:75`
`if (refine)`, `:85` `H[j] += dH[j]` `[ok]`; dispatch `iterative.cpp:322` CGS2 `j + 1, true` `[ok]`;
B-weighted hook `romoperator.cpp:636` `return W.InnerProduct(x, y, r.Real());` `[ok]`. Every range
in the proposed `verified_against` block bounds-checks in-range (orthog.hpp ranges ≤ `:89`;
iterative.cpp/romoperator.cpp/test-orthog.cpp/book ranges all `[ok]`). The carry-forward is
**real and correctly diagnosed**: `dot-mutation-rotation.md:160` writes `(orthog.hpp:34)` and
`:183` writes `return LocalDot(x, y)` at `:34`; citecheck flags `palace/linalg/orthog.hpp:34`
with anchor `return LocalDot(x, y);` as `[DRIFT] anchor at line 35, +1 outside range, suggested
:35` — a genuine stale citation in the OTHER file, while the audited theme correctly uses `:35`
(its lines 161, 302). One spotted self-inconsistency in the report's *non-payload* prose (see
Issues #1): the "Supporting evidence" line cites `orthog.hpp:1-95` while the same line says the
file is 93 lines — `--scan` flagged this as the lone OOB of 33 citations. It is outside the
`verified_against` payload (the artifact-bound block is clean) and does not change the verdict.

**surface-or-evidence — pass.** This is a pure retroactive evidence-backfill: a confirming audit
appending a `verified_against:` block to a firm theme, with no modification to the theme's
operator/theme surface (Signature / laws / prose are untouched). That is the allowed
"retroactive evidence" shape — not a surfaceless rotation_claim. The audit found no defect in the
audited theme and explicitly keeps status `firm`.

**rotation-quality — pass (not the audited object; the audited theme's rotation re-confirmed).**
The audit itself asserts no new rotation; it verifies an existing firm L2>L1 rotation. The
underlying rotation is genuine and strictly more compact at L2: the one named `orthogonalize`
composition fans down into three distinct L0 loop structures (MGS interleaved `m×1` / CGS
separated `1×m` / CGS2 doubled `2×m`), with the variant axis and collective shape hidden as
properties at L2 — state-hiding / coarser dispatch, not a 1:1 rename. The auditor's law-4/5/7
read-as-lowering analysis is faithful. Pass.

**variant-axis-coverage — pass.** The orthogonalize operator carries two orthogonal variant axes
(the GS variant {MGS, CGS, CGS2} and the inner-product hook {canonical, B-weighted}). The audit
verifies all three GS variants against their L0 bodies (MGS `:41-53`, CGS `:57-74`, CGS2
`:75-88`) AND both hook positions (canonical `IdentityInnerProduct` `:35`; B-weighted
`W.InnerProduct` `:636`), and confirms Householder is explicitly scoped out (no L0 path). No
hidden branch. Pass.

**cross-reference-integrity — pass (build-readiness guard satisfied).** I enumerated fences in
CYCLE.md (`grep -n '```'`): exactly 4 markers (even parity) — `:162` opens the
`edit:book/src/L2-L1/orthogonalize-composition-lowering.md` block, `:164` opens the nested
` ```yaml `, `:242` closes the yaml, `:243` closes the edit block. Balanced nested fences. The
build-readiness guard is satisfied: the proposed change is an **append-only fenced yaml INSIDE
the edit fence** — there is no `## Status` flip and no firm-body authored outside the fence. The
theme stays `firm` and already carried that status, so the cycle-019 fence-truncation defect
signature (firm-claimed body sitting outside the proposed-changes fence) does NOT apply here. All
cross-references resolve: every cross-theme file the block names exists on disk
(`L2/orthogonalize.md`, `L1/{orthogonalize,dot,axpy}.md`,
`L1-L0/{dot-mutation-rotation,orthogonalize-mutation-rotation}.md`, the two sibling L2>L1
themes), the target theme is wired into `SUMMARY.md:54`, the append is additive (no pre-existing
`verified_against:` yaml key in the theme), and the two friction-ledger slugs the carry-forward
cites (`audit-report-inherited-miscitation-lint`, `lifter-scope-content-correction-boundary`) are
real ledger entries. Pass.

**edge-label-fidelity — pass.** The theme is an L2>L1 lowering and the audit's prose discusses
exactly that edge (the `orthogonalize` L2 composition fanning down into L1 `[dot, axpy]`
sequences). No reverse-direction (L1→L2 lift) content was introduced — the append is a forward
verification block, and the auditor was attentive to the high→low invariant (it stops at the L1
leaf and defers the L0 `w.Add` step to the L1>L0 theme, never re-deriving downward content into
the L2>L1 theme). Pass.

**plan-kind-consistency — pass.** Declared shape is a lowering-verifier confirming audit
(verdict fully-supported, theme stays firm, append `verified_against` block). The content matches
exactly: per-citation audit table, applicability-condition verification, delegation-boundary
partition analysis, and a single append-only proposed change. No rough-in placeholders, no
status downgrade, no authored content. Consistent.

**skill-uptake-survey — pass (telemetry only).** The report references its skill uptake
explicitly: `verify-citation-range` (producer/audit-report self-verification sub-case),
`tools/citecheck/` mechanical anchor-drift confirmation (24 anchors), and the carry-forward
routing cites `audit-report-inherited-miscitation-lint` / `lifter-scope-content-correction-boundary`.
This is the expected skill set for a lowering-verifier audit and is surfaced. Non-blocking.

### Issues found

**Issue #1 — `orthog.hpp:1-95` OOB in Supporting-evidence prose (file is 93 lines).**
Location: `CYCLE.md` §"Supporting evidence", line 261 — "`reference/palace/palace/linalg/orthog.hpp:1-95`
(full file, 93 lines ...)". The range overshoots the file by 2 lines, and the same sentence
self-reports the correct length (93). `--scan` flagged this as the single OOB of 33 extracted
citations. Severity: **low / cosmetic.** It is in the report's descriptive prose (what was read),
NOT in the `verified_against` payload that lands in the artifact — every range in the proposed
block is in-bounds. Candidate fix: `:1-95` → `:1-93` (or drop the range, keep "full file").

**Issue #2 (informational, not a defect in this report) — confirmed stale carry-forward in
`dot-mutation-rotation.md`.** Location: cross-referenced file `book/src/L1-L0/dot-mutation-rotation.md:160`
("`orthog.hpp:34`") and `:183` ("`return LocalDot(x, y)` at `:34`"). Independently confirmed via
read + citecheck `[DRIFT → :35]`: the token is at `:35` (line 34 is `{`). This is a genuine
stale `:34` in the OTHER theme; the audited theme correctly uses `:35`. The report already
diagnoses and routes this accurately as a carry-forward (out of this dispatch's edit scope). I
flag it here only to confirm the auditor's finding is real and to keep it visible for the next
pass that owns `dot-mutation-rotation` — it is not a defect of the report under critique. No
action required of this report.

**No blocking issues.** This is a clean confirming audit. The single in-report blemish (Issue #1)
is a cosmetic prose-range typo outside the artifact payload; the carry-forward (Issue #2) is a
correctly-routed finding about a different file.

---

## Repair

All 8 critic checks returned `pass`. The two non-blocking issues map to: one mechanical
cosmetic fix (Issue #1, applied) and one record-only carry-forward about a different file
(Issue #2). No substantive authoring required; no artifact mutation. `overall_status: ready`.

### Fixes attempted

- **Finding**: Issue #1 — `orthog.hpp:1-95` OOB in Supporting-evidence prose (file is 93 lines);
  `--scan` flagged it as the lone OOB of 33 citations, outside the `verified_against` payload.
  - **Decision**: repaired.
  - **Action**: `CYCLE.md` §"Supporting evidence" (line 261) — rewrote the range
    `reference/palace/palace/linalg/orthog.hpp:1-95` → `:1-93`. The fix is in scope per repair
    authority "citation line range off by a small offset" (a +2 overshoot in descriptive prose,
    not a content decision). The same sentence already self-reports the correct length (93), so
    the surgical edit is unambiguous and authors no content.
  - **Verification**: codemap `read_range` confirms line 93 (`#endif`) is the last line (no 94/95);
    `wc -l` = 93; `citecheck "…:1-95"` = `[OOB ] range 1-95 out of bounds (file has 93 lines)`,
    `citecheck "…:1-93"` = `[ok ]`. Post-fix `citecheck --scan CYCLE.md` = **33 ok, 0 failing**
    (the lone OOB is gone). Fence parity unchanged (4 markers, even).

- **Finding**: Issue #2 — confirmed stale `orthog.hpp:34` for `return LocalDot(x, y)` in the
  cross-referenced file `book/src/L1-L0/dot-mutation-rotation.md:160,183` (token is at `:35`;
  line 34 is the brace `{`). Already diagnosed + routed by the report as a carry-forward.
  - **Decision**: not-needed (record-only; not a defect of this report's file).
  - **Rationale**: the drift lives in `dot-mutation-rotation.md`, a *different* artifact file —
    outside both this report's audit/edit scope and the repairer's "do not modify the artifact
    (book/, concepts/) directly" boundary. The audited theme correctly uses `:35` throughout
    (its lines 161, 302), and the report already routes the fix via
    `audit-report-inherited-miscitation-lint` / `lifter-scope-content-correction-boundary`. I
    independently re-confirmed the finding (codemap: line 34 = `{`, line 35 = `return LocalDot(x, y);`;
    citecheck `:34` = `[DRIFT] → suggested :35`, `:35` = `[ok]`) but applied no edit. No change
    needed in this report's CYCLE.md (its carry-forward prose mentions `:34` only descriptively,
    paired with the correct `:35`).

### Unrepairable findings

None. (Issue #1 repaired; Issue #2 is a correctly-routed carry-forward about a different file,
not an unrepairable finding in this report.)

## Suggested resolution

`ready` — all 8 checks pass and the lone cosmetic blemish is fixed. Notes for the integrator:

- The proposed `verified_against:` append-only block (CYCLE.md `:162-243`) is artifact-clean and
  bounds-checked; the theme stays `firm`. Safe to apply as-is.
- **Carry-forward to route (not this report's edit)**: `book/src/L1-L0/dot-mutation-rotation.md`
  cites stale `orthog.hpp:34` at lines **160** and **183** for `return LocalDot(x, y)` — should
  be `:35`. Confirmed via codemap + citecheck `[DRIFT → :35]`. This is a one-token mechanical
  fix for a future `lifter`/`lowering-verifier` pass that owns `dot-mutation-rotation` (or an
  integrator-touch if that file is edited this cycle). Keep visible in the plan/OQ ledger; it is
  out of this dispatch's scope and out of the repairer's artifact-write boundary.
