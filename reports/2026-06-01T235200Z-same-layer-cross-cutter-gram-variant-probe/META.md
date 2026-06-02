---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T00:03:15Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T00:18:00Z
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

# META: verification of "L2 observation — capacitance/inductance reduction IS `gram` with the weighted-hook axis"

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet`: 37 ok, 2 `[AMBIG]` (`inner_product.md:129-133`, `inner_product.md:74-80` — basename resolves to both `book/src/L2/` and `book/src/L3/`). Both ambiguous hits are in the prose §"Specific finding" / §"Supporting evidence", not in the proposed-changes block, and the intended target is unambiguously L2 from context (the report cites `inner_product.md` for the weighted-member law `inner_product_M`, which is the L2 entry). This is a cosmetic basename-vs-full-path lint, not a wrong-range. Beyond the scan I `read_range`-verified every load-bearing pinpoint via codemap: elec `electrostaticsolver.cpp:118` (`M_elec->Mult(V_gf, D_gf)`), `:122` (`// (Vⱼᵀ K Vᵢ) / (Vᵢ Vⱼ)`), `:126` (`C(i,j)=linalg::Dot(...)`), `:131-137` (lower-triangle copy); mag `magnetostaticsolver.cpp:129` (`M_mag->Mult`), `:134` (`// (Aⱼᵀ K Aᵢ) / (Iᵢ Iⱼ)`), `:138` (off-diag Dot with `/(I_inc[i]*I_inc[j])`), `:144-150` (copy); `domainpostoperator.cpp:38-39` (`M_elec = m.PartialAssemble()` over `VectorFEMassIntegrator(ε)`), `:53-64` (μ⁻¹ mass integrator → `M_mag`). All resolve in-range and the quoted comment/code tokens match the source byte-for-byte. The `// (Vⱼᵀ K Vᵢ)` and `// (Aⱼᵀ K Aᵢ)` Palace comments the report leans on as the shape-witness are real (the report quotes the leading fragment; the full comment line carries the `/ (Vᵢ Vⱼ)` energy-normalization tail).

**surface-or-evidence — pass.** Refinement-shaped (modifies existing surface — `book/src/L2/gram.md`). The proposed-changes block modifies surface (variant-axis-1 bullet body, coverage caveat, Evidence list) AND carries evidence (the two `read_range`-verified solver witnesses + the weight-matrix construction). This is the witness-backfill-into-existing-axis case: the rotation/operation identity it asserts (`solver reduction == gram on the B-weighted hook`) is evidence-backed, not a bare claim. Passes.

**rotation-quality — pass (not a new rotation; same-layer identity observation).** The report asserts no NEW algebraic rotation — it asserts that an L0 solver site is a *witness* of the EXISTING firm L2 `gram` operator's already-documented `B`-weighted hook. The load-bearing soundness question (is it genuinely the SAME operation?) verifies cleanly: the solver cell `C(i,j) = linalg::Dot(V_gf, D_gf)` where `D_gf = M_elec·V[i]` is exactly `V[j]ᴴ M_elec V[i] = inner_product_M(V[j], M_elec, V[i])`, the M-weighted inner product. `M_elec`/`M_mag` are `BilinearForm::PartialAssemble()` FE mass matrices (`VectorFEMassIntegrator(ε)` / μ⁻¹ mass integrator) — assembled SPD operators, the IDENTICAL category as the `B`-weight the existing `gram.md:197-202` hook already names (mass-matrix / SPD-weighted overlap). The double `for i { for j }` over the per-terminal field-solution set is the all-pairs single-set `gram dot X` index sweep, `k = #terminals`. This is genuinely the same operation — D2 is NOT conflating distinct operations; the landing direction is correct.

**variant-axis-coverage — pass.** This is the check the report most directly serves. The relevant axes on `gram` are (1) `dot` hook ∈ {Hermitian, B-weighted}, (2) single-set vs cross-Gram. The report correctly identifies the witnesses as exercising axis-1 `B`-weighted member + axis-2 single-set member, and explicitly scopes out the cross-Gram (`gram2`) member as NOT witnessed here (OQ 4). No hidden branch: the symmetry-exploitation (upper-triangle + lower-copy) is correctly classified as the existing transparent perf-trick NON-axis (`gram.md:178-182,213`), present verbatim in both solver loops (`:131-137` / `:144-150`) — verified in source. The boundary D2 draws (post-Gram `/Vᵢ²` / `/(IᵢIⱼ)` scaling, `Cm`/`Mm` sign-remix, in-place `Invert()` are downstream CONSUMERS, not part of the fold) is correct and well-motivated: I confirmed in source that the elec off-diagonal `C(i,j)` has NO inline division (the `/(Vᵢ Vⱼ)` lives only in the comment, vacuous since `Vᵢ≡1`), while the mag off-diagonal DOES divide inline by `/(I_inc[i]*I_inc[j])`. Both are post-Gram scalar scalings on a built Gram cell — folding them into `gram` would be wrong (they are energy-formulation / Maxwell-matrix bookkeeping, the same consumer-vs-constituent split `gram.md:236-241` draws for `deflate`). The boundary is correctly drawn.

**cross-reference-integrity — pass.** All `[link]`s resolve (`gram.md`, `orthogonalize.md`, `inner_product.md` all present in `book/src/L2/`). The proposed-changes anchors are byte-exact against the live `gram.md`: Edit 1 OLD == `gram.md:197-202` verbatim; Edit 2 OLD == `gram.md:277-278` verbatim (`> single-algorithm concentration is the same posture as ... not a firmness gate. **Promotion of`); Edit 3 OLD == `gram.md:324-328` verbatim (the `romoperator.cpp:757-765` non-instance bullet through `**Self-verified.**`). Fence parity: the single ` ```proposed-changes ` block opens at report line 114 and closes at line 202 — balanced, no nested fences. Not a firm-body-outside-fence case (this report does not author a firm chapter body; it edits an existing firm entry's bullets/Evidence). Build-readiness guard N/A (no new firm chapter). The caveat-relaxation (Edit 2) is internally consistent: I ran `search_text 'fullPivLu|Gram|deflat'` over `palace/**/*.cpp` — hits are ALL in `nleps.cpp`, confirming the existing caveat's "literal unweighted XᴴX appears at one site" claim stays TRUE (the solver sites build `XᴴKX` via `M_elec->Mult`+`Dot`, a different code shape that does NOT match that grep). The relaxation therefore narrows the caveat to the *unweighted* member (still exhaustive) and adds the *weighted* member's two witnesses — it does not contradict or undermine the original exhaustiveness claim.

**edge-label-fidelity — pass (not applicable).** Not a lowering-theme report; carries no L_{n+1}→L_n edge label. It is a same-layer (L2) observation + a witness-backfill into one L2 entry. The report correctly routes the symmetry-exploited-lowering footnote to the L2>L1 `gram-fold-specialization` theme rather than the L2 entry (report lines 68-71), which is the correct edge placement. No edge mislabel.

**plan-kind-consistency — pass.** Declared kind is an `observation` (same-layer-cross-cutter "variant-axis coverage gap") carrying a small clean variant-axis-witness landing. The content shape matches: it does NOT claim a new operator, does NOT dispatch a harvester, and the proposed-changes block adds witnesses + Evidence rows to an existing firm entry WITHOUT touching `## Status`. Count impact verified: the `gram` entry stays `firm` (no status line edited; Edits 1–3 touch variant-axis-1 body, the caveat blockquote, and the Evidence list only) — adding witnesses to a firm entry is a coverage strengthening, not a status/count change. The classification is honest.

**skill-uptake-survey — warning.** The report's shape (same-layer cross-cut with a variant-axis determination + a citation-bounded landing) implies two relevant skills: `classify-variant-axis` (the core determination "is this a new axis or an existing-axis witness?") and `verify-citation-range` / `tools/citecheck`. The report explicitly declines to re-run `tools/citecheck` (OQ 3, deferring bounds-check to the integrator safety-net) and does not reference `classify-variant-axis` by name. The variant-axis reasoning is nonetheless performed correctly and thoroughly by hand (the three structural-match criteria are exactly what `classify-variant-axis` would check), so this is telemetry-only, not a quality defect — surfaced per the pure-presence-check mandate.

### Issues found

1. **[low severity] citecheck `[AMBIG]` on bare `inner_product.md`** — `CYCLE.md` §"Specific finding" (line 47) and §"Supporting evidence" (line 213) cite `inner_product.md:129-133,169` / `inner_product.md:74-80` by basename; the basename resolves to both `book/src/L2/inner_product.md` and `book/src/L3/inner_product.md`. Intended target is L2 (unambiguous from context). Cosmetic; these are prose citations, NOT in the proposed-changes block, so they do not affect the landing. Repair would be to full-path them (`book/src/L2/inner_product.md`).

2. **[informational] no `tools/citecheck` self-run on the new Palace citations** — the report (OQ 3) explicitly defers the bounds-check of the four new Palace citations in Edit 3 to the integrator per-report safety-net. I independently `read_range`-verified all four (`electrostaticsolver.cpp:111-137`, `magnetostaticsolver.cpp:110-152`, `domainpostoperator.cpp:30-66`, and the `:38-39`/`:53-64` sub-anchors) and they resolve correctly — so the deferral carries no latent error, but it is the gap behind the skill-uptake-survey warning.

3. **[informational] minor anchor-comment-fragment phrasing** — Edit 3's Evidence bullets quote Palace's comment as `// (Vⱼᵀ K Vᵢ)` / `// (Aⱼᵀ K Aᵢ)`; the actual source comment lines are `// (Vⱼᵀ K Vᵢ) / (Vᵢ Vⱼ)` and `// (Aⱼᵀ K Aᵢ) / (Iᵢ Iⱼ)` (the report quotes the leading fragment, which is the shape-relevant part). Not an error — the quoted fragment is verbatim-present and the omitted tail is exactly the post-Gram normalization the report explicitly scopes out as a consumer. Noted only for completeness; no repair required.

No high/medium-severity issues. The load-bearing variant-axis-identity claim is sound, the boundary is correctly drawn, the count impact is correctly assessed (stays firm), and the proposed-changes anchors are byte-exact and fence-balanced.

## Repair

### Fixes attempted

- **Finding**: [low] citecheck `[AMBIG]` on bare `inner_product.md` basenames in prose (§"Specific finding" line 47, §"Supporting evidence" line 215, and a third occurrence at line 246) — basename resolves to both `book/src/L2/inner_product.md` and `book/src/L3/inner_product.md`.
  - **Decision**: repaired.
  - **Action**: Full-pathed the three bare `inner_product.md` prose citations to `book/src/L2/inner_product.md` in `CYCLE.md` (line 47 `:129-133,169`; line 215 `:74-80`; line 246 `:74-80`). These are prose-only citations, NOT in the proposed-changes block, so the landing is unaffected — this is a cosmetic basename→full-path tightening (trivial cross-reference fix within repair authority). Re-ran `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet`: now **39 ok, 0 failing** (the prior 2 `[AMBIG]` resolved; count dropped because the duplicate-basename ambiguity collapsed to canonical full paths).

- **Finding**: [informational] no `tools/citecheck` self-run on the new Palace citations (OQ 3 deferred the bounds-check of Edit 3's four Palace anchors to the integrator per-report safety-net).
  - **Decision**: not-needed.
  - **Rationale**: The critic independently `read_range`-verified all four new Palace citations (`electrostaticsolver.cpp:111-137`, `magnetostaticsolver.cpp:110-152`, `domainpostoperator.cpp:30-66` + sub-anchors) and confirmed no latent error. The deferral is honest and carries no defect; the integrator safety-net will re-confirm at apply-time. No repair action required.

- **Finding**: [informational] Edit 3 Evidence bullets quote the leading fragment of the Palace comments (`// (Vⱼᵀ K Vᵢ)` / `// (Aⱼᵀ K Aᵢ)`), omitting the `/ (Vᵢ Vⱼ)` / `/ (Iᵢ Iⱼ)` normalization tail.
  - **Decision**: not-needed.
  - **Rationale**: Not an error — the quoted fragment is verbatim-present and the omitted tail is exactly the post-Gram normalization the report explicitly scopes out as a downstream consumer. The boundary is intentional and correct; no repair.

- **Finding**: skill-uptake-survey — warning (report performs the `classify-variant-axis` reasoning correctly by hand without naming the skill; declines an explicit `tools/citecheck` self-run).
  - **Decision**: not-needed.
  - **Rationale**: Telemetry-only per the pure-presence-check mandate — the variant-axis determination is performed correctly and thoroughly (the three structural-match criteria are exactly what `classify-variant-axis` checks). No quality defect; nothing to repair.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Notes for the integrator:

- D2's proposed-changes block edits `book/src/L2/gram.md`: adds the 2 solver witnesses (`electrostaticsolver.cpp:111-137`, `magnetostaticsolver.cpp:110-152`) to the weighted (`B`-weighted hook) variant axis, relaxes the witness-less coverage caveat (narrows it to the *unweighted* member, which stays exhaustive — the `nleps.cpp`-only `fullPivLu` grep confirms the unweighted claim still holds), and appends 3 Evidence rows. The `gram` entry **stays firm — no `## Status` edit, no count delta** (witness-backfill into an existing firm entry is a coverage strengthening, not a status change).
- All three proposed-changes OLD anchors are byte-exact (Edit 1 == `:197-202`, Edit 2 == `:277-278`, Edit 3 == `:324-328`); fence parity is balanced (single `proposed-changes` block).
- **Promote as an OQ**: the separate solver-postprocess reduction that *consumes* `gram` — the `/Vᵢ²` scaling (elec) / `/(IᵢIⱼ)` scaling (mag) + `Cm`/`Mm` sign-remix + in-place `Invert()` — is correctly flagged as a distinct future dispatch (downstream consumer, NOT folded into the `gram` fold). It should be carried as an open question, not landed in this report.
