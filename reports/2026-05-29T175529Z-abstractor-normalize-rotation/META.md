---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T18:40:00Z
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
repaired_at: 2026-05-29T18:55:00Z
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

# META: verification of CYCLE "L1>L0 theme sketch — normalize-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass (LOAD-BEARING; mechanically verified).** `citecheck --scan` on the report returns `43 ok, 0 failing (43 citations checked)`, matching the report's self-reported 43/0 claim exactly — bounds and path-hygiene clean. I then ran `--anchor` spot-checks on every load-bearing pinpoint and they all land exactly on the cited line with no drift:
- `vector.hpp:266` `Norml2` → 266; `:267` `MFEM_ASSERT` → 267; `:268` `1.0 / norm` → 268; `:269` `return norm` → 269.
- `iterative.cpp:631` `Norml2` → 631; `:632` `1.0 / Hj` → 632; `:811` `1.0 / Hj` → 811.
- `operator.cpp:660-661` `SetRandom(comm, u)` → 660; `:664` `A.Mult(u, v)` → 664; `:673` `l = Normalize` → 673; `:676` `res = std::abs(l - l0)` → 676.
- `nleps.cpp:610` `Norml2(GetComm(), v)` → 610; `:611` `1.0 / scale` → 611; `:617` `v2 / scale` → 617.
- `iterative.cpp:636-639` `PlaneRotation` → [636,638,639]; `operator.hpp:377-384`, `operator.cpp:599-619` in-range.
I read the actual source for the meaning-checks (not just WHERE): `vector.hpp:262-270` is verbatim the four-step `Norml2 → MFEM_ASSERT → x *= 1.0/norm → return norm`; `iterative.cpp:629-640` confirms the norm feeds BOTH the Hessenberg sub-diagonal `Hj[j+1]` AND the rescale divisor AND the downstream Givens plane-rotation least-squares; `operator.cpp:656-681` confirms `l = Normalize` IS the eigenvalue estimate consumed by `res = |l-l0|/l0` and the renormalised `u` carries into `A.Mult(u, v)`; `nleps.cpp:609-617` confirms the `// Update the invariant pair with normalization` comment and that `scale` is reused at `:617` to rescale companion `v2`. The report's claim that **vector.hpp is NOT affected by the codemap brace drift** is correct — on-disk `citecheck` (line-map authoritative) and the Read tool agree on all anchors; the only nuance is the `Normalize` literal anchors at the header-comment line 262 + def line 264 (both inside the cited 262-270 range), which the report itself correctly notes.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that adds genuine surface: a new L1>L0 theme file (`normalize-mutation-rotation.md`), an index.md row, and a SUMMARY entry. As an L1>L0 lowering theme it is itself the rotation surface (not a pure rotation_claim backfill against an existing operator). The justification is `structural` throughout, resting on the positive L0 source `vector.hpp:262-270` plus the two inherited firm sibling sub-themes. Not a pure-rotation-claim-without-surface situation. Pass.

**rotation-quality — pass.** The rotation is the in-place→pure-functional mutation rotation: the L1 form hides the destination buffer (three distinct values — prior `x`, unit `û`, scalar `β` — where L0 has one overwritten receiver), the MPI collective, and the reciprocal-vs-divide trick, and it lifts the returned norm to a first-class `result.0` rather than a side output. This is state-hiding / threaded-state compression, not a renaming or 1:1 map. The distinguishing abstraction is Sub-pattern C: the L1 pair `(β, û)` captures what a bare `scal(1/nrm2(x), x)` composition discards (the intermediate norm), and the report evidences that this is load-bearing via three independent consumer shapes. The reuse of sibling sub-themes (A = nrm2-mutation-rotation, B = scal-mutation-rotation Sub-pattern A) is correct and non-duplicating: I confirmed `nrm2-mutation-rotation.md:36-58,110-142` carries the `sqrt∘abs∘Dot` chain + the `MPI_Allreduce` single-rank no-op + the `std::abs` load-bearing-defensive classification, and `scal-mutation-rotation.md:48-49,55-58` names this exact `Normalize` site (and `:61-62` the second GMRES path). The theme inherits rather than restates — exactly the cycle-026 `matrix-weighted-norm-mutation-rotation` precedent (verified: that theme reuses apply-linop A + dot A at its `:11-12,68-86`). Sub-pattern C's load-bearing claim is well-evidenced — all three consumers genuinely consume the norm AFTER the rescale (GMRES `Hj[j+1]` → Hessenberg + Givens; power-iter `l` → convergence test; NEP `scale` reused at `:617` for the companion `v2`). The `MFEM_ASSERT(norm > 0.0)` partiality classification is correct: it is distinct in kind from the inner `nrm2` `std::abs` (which runs on `dot(x,x)` before, and is a no-op in exact arithmetic) — this assert is the run-time witness of the `x ≠ 0` domain restriction, the one semantic addition over the total `nrm2`/`scal` leaves, positively anchored to `vector.hpp:267`.

**variant-axis-coverage — pass.** The sole variant axis is element-type (real | complex), and the report covers it by inheritance: `Norml2` collapses the norm output to real in both cases, `x *= 1.0/norm` dispatches to the matching `operator*=` (including the complex-path `imag(s)==0.0` real-into-complex promotion, inherited from scal Sub-pattern B — verified at `scal-mutation-rotation.md:64-83`). No constant-folding axis (the divisor `1.0/norm` is a runtime value, never `0`/`1`/`-1` since `norm > 0`). The orthogonal B-weighted axis (`normalize_B`) is **explicitly scoped out**, not a hidden branch: it is recorded as a rough-in note with two concrete gating reasons — (a) no fused Palace `Normalize`-with-`B` site exists (the sole `Normalize` overload at `vector.hpp:264` takes no `B`; the `:262` header comment is aspirational), and (b) its `matrix-weighted-norm` constituent is `rough-in (test-coverage-bounded)` (verified at `book/src/L1/matrix-weighted-norm.md:110`). Both gates are upstream and the promotion condition is stated. This is a correct explicit scope-out, with a precedent-grounded promotion trigger.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `nrm2-mutation-rotation.md`, `scal-mutation-rotation.md`, `matrix-weighted-norm-mutation-rotation.md`, `L1/normalize.md`, `L1/nrm2.md`, `L1/scal.md`, `L1/matrix-weighted-norm.md` all exist. The `new:` target `normalize-mutation-rotation.md` does NOT pre-exist (correct for a `new:` block). Build-readiness guard: the firm body is FULLY ENCLOSED inside the `new:` fence — fence enumeration via `grep -n '```'` shows exactly 6 triple-backtick lines = 3 balanced pairs (new 25→430, edit-index 432→435, edit-SUMMARY 437→441), even parity, and the `## Status` apparatus (line 408) sits at line 408 INSIDE the 25-430 fence. The body uses 4-space-indented code blocks (not nested triple-backtick fences), so there is no nested-fence truncation hazard — the cycle-019 firm-body-outside-fence defect is absent. The `edit:book/src/L1-L0/index.md` anchor row is an EXACT byte-match against the current index.md line 30 (verified via diff), and the `edit:book/src/SUMMARY.md` block inserts between the existing consecutive `matrix-weighted-norm` (104) / `lu-solve` (105) rows — both edit blocks are cleanly anchored and the integrator can apply them surgically.

**edge-label-fidelity — pass.** The theme carries the implicit L1>L0 edge label (it is in the `L1-L0/` directory and the prose narrates forward from the L1 LHS to the L0 RHS throughout — "Lowers the pure L1 form ... into Palace's L0 free-function template"). The high→low direction is correct per the "Layers are defined high→low" invariant: LHS is L1, RHS is L0, prose narrates the rewrite forward. No mislabelled edge.

**plan-kind-consistency — pass.** Declared `firm` and the content shape matches: positive-source-anchored four-step expansion, no rough-in placeholders in the firm claim, three sub-patterns each with a justification kind, a positively-anchored guard classification, and a `## Status` block that correctly argues `firm` rather than `partly-constructive` (no negative-anchor reconstruction, no literature inference, no speculative operator — the one non-syntactic ingredient, partiality, is read straight off `vector.hpp:267`). The `normalize_B` rough-in note is correctly fenced OUT of the firm claim. The "Speculative L1 operators: None" declaration is consistent — the theme proposes no new L1 vocabulary. Classification matches content.

**skill-uptake-survey — pass.** The report references the relevant skills for its shape: `verify-citation-range` / `tools/citecheck/citecheck.py --anchor` (the citation self-verification, exercised in the Verified-against block), `classify-variant-axis` (cited in the Variant axes section), and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (named in the integrator-follow-up flag for `book/src/L1/normalize.md:104`). Telemetry present; no blocking.

### Issues found

No fail-level or warning-level issues. The report is a clean, mechanically-verified firm L1>L0 theme. Two low-severity observations (informational, not defects — repairer may ignore):

1. **Minor citation-range looseness (low severity)** — In the `new:` block body (CYCLE.md §"Speculative L1 operators", line ~313) and Verified-against, the matrix-weighted-norm *reduction* is cited as `palace/linalg/operator.cpp:599-619`, whereas the matrix-weighted-norm theme/L1-entry use `:600-619` / `:600-607`. The report's `:599-619` is one line wider at the start (599 vs 600). citecheck confirms `:599-619` is in-range and valid (it is a span citation, not a pinpoint), so this is NOT a drift/fail — just a slightly looser boundary than the canonical sibling citation. Harmless; flagged only for consistency.

2. **Integrator follow-up correctly flagged (informational)** — The report (§"Open questions / caveats", line 466) flags that `book/src/L1/normalize.md:104` currently references this theme as PLAIN TEXT ("...references it as plain text, not a live link") and that the integrator MAY upgrade it to a live link `[normalize-mutation-rotation](../L1-L0/normalize-mutation-rotation.md)` now that the theme lands, per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. I confirmed line 104 of the L1 entry carries exactly that plain-text deferral. This is correctly scoped to the integrator's Phase 5 (a cross-reference upgrade in a file outside this dispatch's write-authority), NOT to this dispatch or the repairer. Noted here so the integrator does not miss it — and so it is NOT mistaken for an in-report cross-reference-integrity defect (the plain-text reference was the correct convention at cycle-026 authoring time, when the theme did not yet exist).

## Repair

### Fixes attempted

The critic graded all 8 checks `pass` with no fail- or warning-level findings — only two low-severity informational observations, both of which the critic itself flagged as "not defects" / "repairer may ignore". Nothing in the report requires a mechanical or surgical fix, so every check records `not-needed`.

- **Finding**: citation-validity — `pass` (citecheck 43 ok / 0 failing; all `--anchor` pinpoints land exactly; no drift).
  - **Decision**: not-needed. No missing citation, no off-by-N range, no path-hygiene defect to repair.
- **Finding**: surface-or-evidence — `pass` (the theme is itself the L1>L0 rotation surface, `structural` throughout).
  - **Decision**: not-needed.
- **Finding**: rotation-quality — `pass` (genuine state-hiding / threaded-state compression; Sub-pattern C returned-norm load-bearing claim well-evidenced).
  - **Decision**: not-needed.
- **Finding**: variant-axis-coverage — `pass` (sole element-type axis covered by inheritance; `normalize_B` explicitly scoped out with stated gates).
  - **Decision**: not-needed.
- **Finding**: cross-reference-integrity — `pass` (all `[link]` targets resolve; `new:` target correctly does not pre-exist; fence parity even — 3 balanced pairs; both `edit:` blocks exact-anchored).
  - **Decision**: not-needed. No broken-link or fence-truncation repair to apply.
- **Finding**: edge-label-fidelity — `pass` (implicit L1>L0 edge, high→low direction correct, prose narrates L1 LHS → L0 RHS forward).
  - **Decision**: not-needed. No edge-label rewrite needed.
- **Finding**: plan-kind-consistency — `pass` (declared `firm`; content matches; `firm`-vs-`partly-constructive` argument correct; no SIDEWAYS auto-rewrite trigger, "Speculative L1 operators: None").
  - **Decision**: not-needed.
- **Finding**: skill-uptake-survey — `pass` (relevant skills referenced for the shape; telemetry present).
  - **Decision**: not-needed.

**Low-severity informational notes (not findings; no repair):**

- **Note 1 — loose `operator.cpp:599-619` vs canonical `:600-619` span**. Per instruction, left as-is. citecheck confirms `:599-619` is a valid in-range *span* citation (not a pinpoint), and both spans bracket the same matrix-weighted-norm reduction body. A one-line start-boundary widening on a valid span is not a drift/fail and is below the repair bar — tightening it would be a cosmetic edit, not a correctness fix.
- **Note 2 — plain-text ref at `book/src/L1/normalize.md:104`**. This is an integrator/Phase-5 cross-reference upgrade in a file OUTSIDE this report's write-authority (the repairer does not modify `book/`). Not touched here. Carried to the integrator under *Suggested resolution* below.

**Stale-frontmatter touch (mechanical, in repair authority):** corrected `verifies: ../REPORT.md` → `verifies: ../CYCLE.md` in this META.md frontmatter (legacy `REPORT.md`→`CYCLE.md` rename, cycle-004). Pure pointer fix; no content change.

### Unrepairable findings

None. No finding exceeded repair authority — there were no fail/warning findings at all.

## Suggested resolution

`overall_status: ready`. The report is a clean, mechanically-verified firm L1>L0 theme with all 8 checks passing; it can be applied as-is.

Notes for the integrator:
- **Apply the three proposed-changes blocks as-authored**: the `new:book/src/L1-L0/normalize-mutation-rotation.md` file, the `edit:book/src/L1-L0/index.md` anchor-row append, and the `edit:book/src/SUMMARY.md` insertion (between the `matrix-weighted-norm-mutation-rotation` and `lu-solve-mutation-rotation` rows). The critic verified all anchors are exact-byte and fence parity is even.
- **Phase-5 follow-up (live-link upgrade)**: now that `normalize-mutation-rotation.md` lands, upgrade the plain-text reference at `book/src/L1/normalize.md:104` to a live link `[normalize-mutation-rotation](../L1-L0/normalize-mutation-rotation.md)` per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. This is the integrator's call (a cross-reference upgrade in a file outside this dispatch's write-authority), flagged by both the report (§Open questions, line 466) and the critic (Note 2).
- **OQ closure**: the report resolves OQ `normalize-mutation-rotation-l1-l0-theme` (theme now authored) — promote the closure when the report integrates.
- The standard `lowering-verifier` follow-up (confirming the `linalg::Normalize` template is the sole fused-normalise overload and the returned-norm consumer cohort is complete) is a normal next-cycle audit, not a blocker — no status reduction implied.
