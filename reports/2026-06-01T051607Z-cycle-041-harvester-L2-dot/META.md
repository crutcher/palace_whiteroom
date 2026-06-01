---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T053000Z
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
repaired_at: 2026-06-01T054500Z
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

# META: verification of "Formalize dot at L2" (L2 thin-identity-floor entry)

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: **15 ok, 0 failing** (bounds + path hygiene clean). Ran `--anchor` on every load-bearing pinpoint in the Evidence list — all 10 cleared mechanically: `vector.hpp:110-113` (`Dot` at :111-113), `:242-244` (`LocalDot` at :243-244), `:247-253` (`GlobalSum` at :251); `vector.cpp:263-267` (`Dot` :263, `0.0` :266), `:269-274` (`TransposeDot` :269), `:665-672` (`hypre_SeqVectorInnerProd` :671, `MFEM_ASSERT` :668), `:674-685` (`LocalDot` :674/:678/:682-683); `test/unit/test-vector.cpp:206-207` (`WithinRel` :207). Meaning-read via codemap `read_range` (with the `+1` over-read drift guard applied to each range) confirms every claim: the `ComplexVector::Dot` body returns `{Re*Re + Im*Im, (this==&y)?0.0:...}` (the Hermitian kernel + the self-dot imag-elision at :266); `TransposeDot` is the unconjugated form (:269-274); real `LocalDot` is the single `hypre_SeqVectorInnerProd` strided pass guarded by `MFEM_ASSERT(x.Size()==y.Size())` (:668); complex `LocalDot` is the four-real-dot lift into `(Re,Im)` with the `&x==&y` fast path; the `Dot` template (:247-253) is `Mpi::GlobalSum ∘ LocalDot`. The Evidence list is fully supported. **The warning is a single off-by-one in a NARRATIVE pinpoint outside the formal Evidence list:** §"Conjugation convention" (CYCLE.md ~:154-156) cites "comment at `palace/linalg/vector.hpp:246`" for the free-function conjugation comment `linalg::Dot(comm, x, y) = yᴴ x`. The actual comment line is **`:245`** (`// Calculate the parallel inner product yᴴ x or yᵀ x.`); line **246** is `template <typename VecType>`. The behavior is correctly covered by the formal range `:247-253` in the Evidence list, so this is a cosmetic prose drift, not an evidentiary gap — but it is a real, citecheck-confirmable `[DRIFT -1]` and should read `:245`.

**surface-or-evidence — pass.** Not a refinement of an existing operator — this is a `new:` L2 floor chapter (`book/src/L2/dot.md`). The proposal creates surface and carries its evidence (transitive through the firm L1 leaf + direct L0 anchors). The "thin identity-in-form floor" framing is the retroactive-evidence-allowed shape; there is no pure-rotation-claim-without-surface concern.

**rotation-quality — pass (with the sanctioned-thin-floor caveat).** The L2→L1 rotation is explicitly declared **identity-in-form on the primitive** (value-thread-isomorphic), not a compaction — and that is correct and sanctioned here, not a rotation-quality failure: per "Identity-lowerings still require both L levels" the entry exists for **floor presence** under the firm L3 `dot` leaf, with the genuine fusion-rotation content (de-fusion of the Hypre strided kernel / four-real-dot lift / local-then-collective two-step) correctly DEFERRED to the fold-parent `inner_product` §"Fusion note". This is the documented identity-floor pattern, not a renaming-only defect. The fold-vs-leaf separation is the real structural content and it is handled correctly (see cross-reference-integrity). Marked pass because the report does not overclaim a compaction it does not perform — it explicitly labels the rotation as identity-in-form and routes the de-fusion to the parent.

**variant-axis-coverage — pass.** The two variant axes (element-type real|complex; conjugation-convention hermitian|unconjugated for complex) are both covered with per-axis L0 kernel citations, and the per-element-kernel table enumerates all three (real `dot`, complex `dot`, complex `tdot`). The weight-presence axis (`M=I` vs general `M`) is **explicitly scoped out** to the separate fold-parent member `bilinear-form` — a clean scope-out, not a hidden branch. The `tdot` member's API-only evidentiary status is disclosed as a member-level caveat. No hidden branches.

**cross-reference-integrity — pass.** All 14 referenced artifact targets resolve on disk (`L2/inner_product.md`, `L3/dot.md`, `L1/dot.md`, `L2/index.md`, `L2/{linear_combination,krylov-step,orthogonalize,gram,deflate}.md`, `L1/bilinear-form.md`, `concepts/dot.md`, `L3-L2/krylov-step-body-identity.md`, `L1-L0/dot-mutation-rotation.md`, `SUMMARY.md`). Cited sub-sections exist: `L2/index.md` §"Fold-cohort boundary" (:75), `inner_product.md` §"Conjugation convention (pinned)" (:46), §"Fusion note", §Signature (:104), §"tdot" (:267); `krylov-step-body-identity.md` §"Applicability conditions" point 3 (:89, and the seven-primitive statement at point 3 explicitly includes `dot`). The fold-parent is **CITED, not MERGED** — the report repeatedly carries the do-NOT-merge / codomain-fold distinction, the leaf-of relationship matches `inner_product`'s actual §Signature recovery (`dot(x,y) = inner_product x y`), and the index already carries the matching §"Fold-cohort boundary" note. Integration anchors resolve: the `edit:L2/index.md` block anchors on the verbatim `orthogonalize` dep-map row (:54) and prepends the new `dot` row (no pre-existing `dot` row → no conflict); the `edit:SUMMARY.md` anchors on the `inner_product` L2 line (:50). Build-readiness: forward-references to the D4-authored L2>L1 / L3>L2 `dot` themes are kept as plain prose, not live links — correct.

**edge-label-fidelity — pass.** The entry is an L2 operator chapter, not a lowering theme; it carries no `L_{n+1}→L_n` edge label. Where it discusses adjacent edges (L2→L1 identity-in-form; L3→L2 deferred to the D4 theme) the prose matches the edge named. Not applicable in the failing sense; pass.

**plan-kind-consistency — pass.** Declared `firm`; content shape matches. The firm apparatus (Signature, Semantics, Algebraic laws 1-13 + explicit non-laws, Variant axes, Evidence, Status) is all present and INSIDE the proposed-changes fence (§Status at CYCLE.md:304, inside the 46→392 block). The `firm` justification — value-thread-isomorphism to the firm L1 leaf + syntactic-identity laws inherited unchanged + the in-source `&x==&y` imag=0.0 confirmation of the PSD-at-diagonal law — is consistent with the "firm-on-positive-structure" escape (laws are sesquilinear/bilinear identities on fully-read source, so the missing dedicated `tdot` test does not gate firmness; only `tdot`'s behavioral weight is API-only, disclosed as a non-status-reducing caveat). No rough-in placeholders. The thin-floor `firm` is sound under both "Identity-lowerings still require both L levels" and the 2026-05-31 foundation-first directive.

**skill-uptake-survey — pass.** The report references its `tools/citecheck/citecheck.py --anchor` self-verification (Evidence preamble + §"Supporting evidence" L0-self-verification bullet) and the `convert-nested-fences-to-indented-code-in-proposed-changes-block` discipline (§"Supporting evidence" fence-parity self-check, realized as 4-space-indented signature samples). Skill telemetry present for the relevant procedures. Pure presence check; pass.

### Issues found

1. **[warning] Prose pinpoint off-by-one, `vector.hpp:246` → should be `:245`.** CYCLE.md §"Conjugation convention" (~line 154-156), inside the `new:book/src/L2/dot.md` body: "comment at `palace/linalg/vector.hpp:246`". The cited comment (`// Calculate the parallel inner product yᴴ x or yᵀ x.`) is on line **245**; line 246 is `template <typename VecType>`. citecheck-confirmable `[DRIFT -1]`. The behavior is independently covered by the formal Evidence range `:247-253`, so this is cosmetic (narrative pinpoint, not an Evidence-list entry) — but it is a real drift and the repairer can correct `:246` → `:245` mechanically. Severity: low.

2. **[note, not a defect] Downstream L3-entry consistency touch (already self-flagged).** The report's §"Open questions / caveats" correctly notes the firm L3 `dot` §"Lowers to" still records a non-adjacent in-line identity straight to L1, and that with this L2 floor present the L3 entry may want a light re-anchor to the adjacent L2 parent + the D4 L3>L2 theme. This is correctly scoped OUT of this dispatch and is not a defect in the L2 entry (the L2 floor is self-coherent). Recorded here only so the integrator/planner sees the carried-forward downstream touch.

3. **[note] Count-ownership respected — confirmed.** The `edit:L2/index.md` block prepends ONLY the `dot` dep-map row before the `orthogonalize` row; it does NOT touch the §"Vocabulary cohort" / "Firm at L2" tally (index.md:28-30), which D7 (layer-intro-author) owns this cycle. The §"Count-ownership note (mandatory)" states this explicitly. No `parallel-blind-shared-index-count-divergence` risk from this report. No action needed — flagged as a positive confirmation of the dispatch directive.

4. **[note] Leaf-vs-fold design fork.** The existence of `L2/dot` as a same-named leaf alongside the `inner_product` fold-parent is a sanctioned design choice under live meta-phase adjudication (not treated as a defect, per the dispatch framing). The report handles the fork conservatively and correctly — cites-not-merges, carries the do-NOT-merge note in body + dep-map row, and confines its fusion content to a single deferring note. If the meta-phase later adjudicates toward fold-only, this entry is cleanly reducible; nothing here pre-commits the fork.

---

## Repair

### Fixes attempted

- **Finding** (issue 1): Prose pinpoint claimed off-by-one — CYCLE.md §"Conjugation convention" cites `palace/linalg/vector.hpp:246` for the conjugation comment `linalg::Dot(comm, x, y) = yᴴ x`; critic asserted the comment is on `:245` and `:246` is `template <typename VecType>`, requesting a mechanical `:246` → `:245` tighten.
  - **Decision**: not-needed (no edit applied — the cited line is already correct on disk).
  - **Action**: NONE. Pre-edit on-disk verification (both vanilla `Read` of `reference/palace/palace/linalg/vector.hpp:243-253` AND a codemap `read_range` cross-check of `:244-248`) shows the comment `// Calculate the parallel inner product yᴴ x or yᵀ x.` is on **line 246** — exactly as CYCLE.md cites. The surrounding lines are: `:244` = `std::complex<double> LocalDot(...)`; `:245` = blank; `:246` = the comment; `:247` = `template <typename VecType>`. The critic's anchor read was itself shifted by **−1** (the comment is NOT on `:245`; `:245` is blank). Applying the requested `:246` → `:245` tighten would have **introduced** an off-by-one (re-pointing the citation at the blank line), corrupting a currently-correct anchor. Per repairer discipline ("verify on-disk before editing"; "mechanical and surgical only"), the correct mechanical action is to leave the citation untouched. The formal Evidence range `:247-253` is unaffected and correct (the critic concurred on that range).

- **Findings** (issues 2-4): notes, not defects — explicitly scoped out by the critic (downstream L3 re-anchor touch; count-ownership positive confirmation; leaf-vs-fold design fork). No repairer action; carried forward to integrator/planner as the critic recorded.

### Unrepairable findings

None. The single flagged warning required no repair because the artifact is already correct on disk; the warning rests on a critic-side −1 read drift, not a defect in the report. No substantive authoring was deferred.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- **The `citation-validity: warning` was a false positive.** CYCLE.md's `vector.hpp:246` pinpoint for the conjugation comment is correct as written (verified twice — `Read` + codemap `read_range`). No edit was applied; the citation should be integrated **unchanged**. Do NOT re-apply the critic's suggested `:246` → `:245` tighten — it would mis-point the anchor at a blank line.
- I did not override the critic's `checks: citation-validity: warning` value (out of repairer authority); the `repairs:` frontmatter records the outcome as `not-needed`, which is the accurate disposition.
- Carry-forward (issue 2): the firm L3 `dot` §"Lowers to" non-adjacent in-line identity-to-L1 may want a light re-anchor to the new adjacent L2 parent + the D4 L3>L2 theme once this floor lands. Self-flagged by the report; out of this dispatch's scope. A planner candidate, not an integration blocker.
