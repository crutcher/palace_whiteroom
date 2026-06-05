---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T234500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-04T235500Z
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

# META: verification of "L1 observation — divfree-slice-detritus-GC" (cycle-097 D2)

## Critique

### Checks run

**citation-validity — warning.** `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returns `25 ok, 15 failing`. All 15 "failing" hits are non-drift: 14 `[AMBIG]` (the report writes bare basenames — `divfree-projector.md:122-135`, `ksp_solve.md:131`, `apply_linop.md:43` — where 3-5 same-named files exist across layers) and 1 `[MISS]` on `slices/divfree.md:24-100` (the slice being deleted; a book-artifact path, not a `reference/` range, quoted verbatim from the on-disk footer link). None is a `[DRIFT ±N]`. I hand-confirmed the load-bearing pinpoints resolve: the firm-home L1 entry `book/src/L1/divfree-projector.md` carries the positive L0 cites the report's table asserts (`divfree.cpp:155-187` 4-step apply at lines 122-135; `divfree.cpp:175` step-3 ksp solve at 128-129; `divfree.hpp:28-31`; `mixedvecgrad.cpp:202`), and the Palace source `divfree.cpp:175` is exactly `ksp->Mult(rhs, psi)` (192-line file, range in-bounds). The warning is path-hygiene (bare basenames invite ambiguity once a reader leaves the report's L1 framing), not a wrong claim — flagged so the repairer can decide whether to disambiguate the report's internal cross-refs to full paths. No `verified_against:` block in this report, so that sub-check no-ops.

**surface-or-evidence — pass.** This is a deletion/detritus-GC report, not a refinement of an operator/theme surface. The "absorb" half is asserted to be a no-op, and I verified that claim against the firm home (see cross-reference-integrity): every load-bearing fact the slice states is positively L0-anchored in `L1/divfree-projector.md`, so there is no unabsorbed surface to back. The record-definition sub-check is N/A — the report proposes no chapter with a signature naming a record.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted; this is a slice deletion + three pointer re-anchors. No-op for this report kind.

**variant-axis-coverage — pass (not applicable).** A deletion has no variant axes. The divfree projector's own variant axes (real/complex, 1-arg/2-arg `Mult`) live in the firm `L1/divfree-projector.md`, out of this report's scope. No-op.

**cross-reference-integrity — LOAD-BEARING, pass.** This is the decisive check for a deletion: any unrepointed inbound markdown link to the deleted file is a `linkcheck2` hard error. I ran the full inbound sweep `grep -rn "slices/divfree" book/src/ scaffolding/` and `grep -rn "divfree.md" book/src/`. The complete live-artifact inbound set is exactly: `L1/ksp_solve.md:131`, `L1/ksp_solve.md:143`, `L1/divfree-projector.md:326`, `SUMMARY.md:295`, `spec/index.md:18`. The report's changes 1-3 re-anchor the three `L1/` pointers; SUMMARY.md:295 + spec/index.md:18 are correctly attributed to dispatch D5 and explicitly flagged (Open questions) as a same-cycle co-landing requirement. The only other hits are `book/src/meta-reviews/2026-05-24-*.md` and `scaffolding/cycle-record.jsonl` — I confirmed these are PROSE mentions, NOT `[text](path)` markdown links (the `grep -E '\]\(.*divfree'` over the meta-reviews returns empty), so they are frozen history that does not trip linkcheck2. No inbound link is missed. I further confirmed the report's three negative-grep claims independently: `book/src/concepts/` has ZERO slice links (exit 1), `L1/eigsolve.md`/`L0/eigensolver-wrapper.md` have ZERO (exit 1), and no `depends-on` edge targets the slice (exit 1) — confirming reachability-GC clearance. The three proposed `Replace:` blocks match the on-disk text byte-for-byte (verified ksp_solve.md:131/:143 and divfree-projector.md:325-327).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a same-layer (L1) cross-cut deletion. No-op.

**plan-kind-consistency — pass.** Declared shape is a `same-layer-cross-cutter` redundancy observation driving a detritus-GC deletion (graded-stack P2 slice-deletion). The content matches: a redundancy finding (slice ≡ firm entry), an absorb-is-no-op verification, an inbound-link sweep, and four mechanical proposed-changes (3 re-anchors + 1 delete). No firm-operator apparatus is claimed; no mis-classification.

**skill-uptake-survey — pass.** The slice-deletion shape implies `skills/phase-1-slice-reduction-audit` (concept-page-grep before recommending reduction). The report does not name the skill by slug, but it performs the skill's core procedure inline (the `grep book/src/concepts/` for slice links is exactly the audit's concept-page-grep, run and reported). Pure telemetry surface, non-blocking; noting the missing explicit slug reference for the uptake record.

### Issues found

1. **citation-validity / path-hygiene (CYCLE.md §Specific-finding-1 table + §Supporting-evidence) — minor.** The report's internal book cross-references are written as bare basenames (`divfree-projector.md:122-135`, `ksp_solve.md:131`, `apply_linop.md:43`, `ksp_solve.md:34`) that citecheck flags `[AMBIG]` because the same basename exists at 3-5 layers. The report's prose framing (L1 firm homes) disambiguates them for a reader in context, and I verified they resolve to the L1 files, but the load-bearing table would be more robust as full paths (`book/src/L1/divfree-projector.md:122-135` etc.). Candidate for mechanical disambiguation; does not affect the deletion's correctness.

2. **citation-validity (CYCLE.md §Supporting-evidence, slice self-cite `slices/divfree.md:24-100`, `:142-216`) — informational, self-resolving.** citecheck flags `[MISS]` on the slice path because it searches under `reference/` first; this is a book-artifact path (the file being deleted), present on disk. Not a defect — flagged only so the repairer does not mistake the `[MISS]` for a broken Palace citation.

3. **No load-bearing defect found in the deletion itself.** The three claims the dispatch foregrounded are all confirmed: (a) the firm homes carry the positive L0 (sampled `divfree.cpp:175 = ksp->Mult(rhs, psi)`, plus the 4-step apply / sign / construction ranges present in `L1/divfree-projector.md`); (b) exactly 3 inbound `L1/` prose pointers + 2 D5-owned SUMMARY/index rows + 0 concept-page links — the inbound set is complete with no missed link; (c) no `depends-on` blocking edge targets the slice. The D5 co-landing dependency (SUMMARY.md:295 + spec/index.md:18 must be removed in the same cycle or the delete leaves two dangling linkcheck2 errors) is correctly identified and flagged by the report itself — recording it here as the one hard integration constraint the integrator-finalize build gate must enforce.

## Repair

### Fixes attempted

- **Finding**: citation-validity (warning) — citecheck reports 14 `[AMBIG]` (bare basenames like `divfree-projector.md:122-135`, `ksp_solve.md:131`, `apply_linop.md:43` where same-named files exist across 3-5 layers) + 1 `[MISS]` on the slice's own to-be-deleted path. No `[DRIFT ±N]`; every citation is substantively correct, just under-qualified.
  - **Decision**: repaired
  - **Action**: Disambiguated the report's internal book cross-references to full `book/src/<layer>/<file>` paths in the analysis/evidence sections only — the §Specific-finding-1 table right column (8 `divfree-projector.md` / `ksp_solve.md` cells), the §1 deliberately-dropped-content bullet (`divfree-projector.md:244-265`/`:1-9`/`:267-277` → `book/src/L1/divfree-projector.md:…`), the §2 inbound-pointer list (`L1/ksp_solve.md:131`/`:143`, `L1/divfree-projector.md:325-327` → full paths), the §3 concept-page prose (`apply_linop.md:43`, `ksp_solve.md:34`, `nested-constructed-operator-gate.md:…`, `dependency-map.md:153` → `book/src/concepts/…` and `book/src/L1-L0/…`), and the §Supporting-evidence firm-home line. **The four proposed-change `Replace:`/`With:` code blocks were NOT touched** — they are byte-for-byte on-disk artifact text that must match for the integrator to apply them; the `(../spec/slices/divfree.md)` markdown link inside the `Replace:` block is verbatim slice-link text, not a citation to qualify. Re-ran `tools/citecheck/citecheck.py --scan CYCLE.md`: AMBIG dropped 14 → 1, zero new DRIFT introduced.
  - **Residual (benign, intentionally left)**: (i) one `[AMBIG] ksp_solve.md:131` survives inside a **verbatim grep-output transcript** at the §Supporting-evidence grep-set bullet (a quoted recap of what the shell command printed, NOT a cross-ref to resolve — qualifying it would misrepresent the recorded output); (ii) the `[MISS] slices/divfree.md:24-100` is the **deletion target's own path** (a book-artifact path, present on disk, being removed by change 4 — a no-op the critic already flagged as self-resolving). Both are non-drift and non-load-bearing.

### Unrepairable findings

None. The only flagged finding was path-hygiene, fully addressed by mechanical full-path disambiguation. The 7 other checks passed.

### Integration constraint (confirmed, NOT a repairable defect)

The critic and the report both flag a hard sequencing constraint: the slice deletion (proposed-change 4) **must co-land with D5's removal of `book/src/SUMMARY.md:295` + `book/src/spec/index.md:18`**, or the delete leaves two dangling `linkcheck2` errors at the finalize rebuild. This is a **correct integrator sequencing note, not a defect this report can fix** — D5 is dispatched this same cycle, and `integrator-per-report` applies all ready reports before `integrator-finalize` runs `cargo make book`. Recording (not "fixing") it here so the integrator enforces the co-landing at the build gate. Out of repair authority (cross-report sequencing belongs to the integrator).

## Suggested resolution

`ready`. The citation-validity warning was path-hygiene only (no DRIFT, every claim substantively correct against the verified firm home `book/src/L1/divfree-projector.md`) and is now resolved by full-path disambiguation of the report's internal cross-refs; the two residual citecheck hits are benign (a verbatim grep transcript + the deletion target's own path). Integrator note: apply this report's four mechanical proposed-changes (3 re-anchors + 1 delete) **in the same cycle as D5's SUMMARY/index row removals** so the finalize `cargo make book` linkcheck2 sees no dangling slice link.
