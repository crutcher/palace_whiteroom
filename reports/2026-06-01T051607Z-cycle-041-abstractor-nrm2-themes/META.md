---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T054523Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T055210Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L2>L1 + L3>L2 thin-identity nrm2 lowering themes (D5, wave-2)"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` returns `4 ok, 0 failing`; the four L0/source citations all resolve in-range and pass path hygiene. I confirmed the load-bearing pinpoints with `--anchor`: the L0 anchor `palace/linalg/vector.hpp:255-260` carries the body line `std::sqrt(std::abs(Dot(...)))` at line 259 (in range — no +1 drift); the B-weighted-overload boundary cites `palace/linalg/operator.cpp:600-619` (Norml2 at 600/610) and `operator.hpp:372-374` (Norml2 at 374), both OK; the cross-artifact pinpoint `book/src/L3-L2/krylov-step-body-identity.md:97` resolves to point-3 ("seven L1 primitives") exactly at line 97. I hand-verified the L1/nrm2 pinpoints the L2>L1 body cites: law 8 at `:53`, deps-abs/√-below-resolution at `:66`, variant-axes at `:74`, semantics-abs-guard at `:36` — all accurate. The warning is NOT a line-drift; it is the section-anchor imprecision flagged under cross-reference-integrity below (the `§"Fold-cohort boundary"` reference). No `verified_against:` block is emitted (deferred to a lowering-verifier per the report's own §"Open questions"), so the YAML round-trip sub-check is not applicable. The single co-land source (`book/src/L2/nrm2.md`) is not on disk yet — expected (see cross-reference-integrity).

**surface-or-evidence — pass.** Both proposals are NEW theme chapters (`new`/`edit` blocks creating `nrm2-fold-specialization.md` and `nrm2-body-identity.md`), not refinements of existing operator/theme text, so the refinement-surface gate is structurally satisfied: each carries its full surface (the theme body) plus the rotation framing and L0/artifact evidence inline. Not a pure rotation_claim-without-surface case.

**rotation-quality — pass.** These are declared thin-identity (identity-in-form) lowering themes, and the methodology invariant "Identity-lowerings still require both L levels" makes a 1:1 identity edge first-class rather than a rotation-quality failure — a renaming-only mapping is a fail ONLY when a *non-identity* rotation is claimed. Here the report does not over-claim a compaction; it explicitly states the rotation is identity-in-form on the primitive's signature, and isolates the one substantive structural fact each theme records (L2>L1: the resolution drop of the `√`/`abs` scalar post-steps and the abs-guard preserved-as-claim→absorbed-by-non-negativity transition; L3>L2: the inner-reduction-name change `dot` leaf → `inner_product` fold at the diagonal, no wrapper rotation). The framing is honest about being a leaf-identity, and the load-bearing `std::abs` guard is correctly handled as a preserved algebraic claim at L2 (not silently dropped). Pass.

**variant-axis-coverage — pass.** The only orthogonal axis for `nrm2` is element-type (real | complex), and both themes explicitly state it collapses to a single always-real operator at every layer, citing `L1/nrm2 §"Variant axes"` (`:74`) and `L3/nrm2 §Variant axes` (confirmed at `:113`). The B-weighted overload `√(xᴴ B x)` is correctly scoped OUT as a *different operator* (`matrix-weighted-norm` rough-in, separate forthcoming theme), with its L0 boundary anchors named. No hidden branch: there is exactly one L1 `nrm2` leaf and no dispatch family.

**cross-reference-integrity — warning.** Every named slug and `[link]` target I checked resolves on disk: `L1/nrm2`, `L3/nrm2`, `L1-L0/nrm2-mutation-rotation`, `L3-L2/krylov-step-body-identity`, `L2-L1/inner-product-fold-specialization`, `L1/dot`, `L1/matrix-weighted-norm`, `L2/inner_product`, `L2/krylov-step`, `L3-L2/ksp-solve-outer-driver`, both index files, and both SUMMARY sections — all present. The proposed index rows match each table's column arity (L2-L1 is 4-col `theme | L2 anchor | L1 anchor | status`; L3-L2 is 5-col `Theme | LHS | RHS | Justification | Status`); both SUMMARY insertions target existing Parts. The one referenced file NOT on disk is `book/src/L2/nrm2.md` — but that is the wave-1 D2 harvester body co-landing at the same integration (declared in frontmatter `inputs`; the D2 report dir `reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/` exists), the standard co-land pattern, not a dangling reference. The warning is a section-anchor imprecision: both bodies reference `[L2/inner_product](../L2/inner_product.md) §"Fold-cohort boundary"` (L2>L1 body line 47; L3>L2 body line 368), but `inner_product.md` has no heading by that name — the do-NOT-merge consumer discipline lives in its `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` section (`:390`), with a passing "fold-cohort" mention at `:221`. The cited content fully supports the consumer-not-fold-member claim, and prose §-references aren't linkcheck-resolved, so this won't break the build — but the named section title is wrong and should be corrected to the actual heading.

**edge-label-fidelity — pass.** Both themes narrate forward (high→low) and the prose matches the edge label. L2>L1 (`nrm2-fold-specialization`): the rewrite block shows `√(abs(inner_product x x))` [L2] → `√dot(x, x)` [L1], LHS=L2, RHS=L1, prose narrates the L2 form re-fusing onto the L1 leaf. L3>L2 (`nrm2-body-identity`): the rewrite block shows `√dot(x, x)` [L3] → `√(abs(inner_product x x))` [L2], LHS=L3, RHS=L2, prose narrates the L3 whole-tensor norm dissolving into the L2 fusion composition. The `√ ∘ inner_product` at `y=x` consumer framing is carried correctly and identically through both edges (nrm2 = CONSUMER of inner_product, NOT a fold member), grounded in `inner-product-fold-specialization.md:154-156` which names nrm2 as exactly that consumer entry "downstream of this lowering, not a dispatch within it." No edge-direction mismatch.

**plan-kind-consistency — pass.** Both entries are declared `firm` thin-identity lowering themes, and the content shape matches: each is a complete theme body (LHS form, RHS form, the rewrite, applicability conditions, justification kind, status) with no rough-in placeholders, no unfilled sections, no constructive sub-part. The `firm` claim is justified — both endpoints are firm vocabulary (L1 cycle-003 / L3 cycle-011 / L2 co-landing this cycle), the rotation is identity-in-form on positively-anchored fully-specified source. The deferred `verified_against:` block is correctly framed as corroboration, not a promotion gate (consistent with the partly-constructive vs firm distinction). The proposed-changes fences are balanced (6 pairs, 12 backtick-fence lines, even parity; nested code-block forms use 4-space indentation, no nested `text` fences) — the fence-truncation defect does not apply; the conversion-to-indent was done correctly.

**skill-uptake-survey — pass (telemetry).** The shape implies `propose-rotation` / `verify-rotation-citation` could apply; the report does not name an explicit skill invocation, but it grounds its rotation framing in the precedent themes and the methodology invariants (Identity-lowerings, the BLAS-1-leaf cohort, the high→low discipline) and does its own L0 self-verification. Pure presence check, non-blocking — surfaced for telemetry only.

### Issues found

1. **(citation-validity / cross-reference-integrity — low) Wrong section-anchor name `§"Fold-cohort boundary"`.** Both theme bodies — `nrm2-fold-specialization.md` intro (CYCLE.md line 47) and `nrm2-body-identity.md` §"L2 form (RHS)" (CYCLE.md line 368) — cite `[L2/inner_product](../L2/inner_product.md) §"Fold-cohort boundary"` for the consumer-not-fold-member boundary. No heading by that name exists in `book/src/L2/inner_product.md`; the supporting content is in `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` (`:390`) (with a passing "fold-cohort" mention inside law 5 at `:221`). The claim is fully supported; only the named section title is incorrect. Candidate repair: change the two `§"Fold-cohort boundary"` references to `§"Consumer (NOT an instance)"`. Non-build-breaking (prose §-reference, not a resolved `#anchor`).

2. **(naming tension — informational, NOT a defect; flagged for the meta-phase) L2>L1 slug `nrm2-fold-specialization` names a consumer-not-fold-member relationship.** The slug is carried for sibling-naming continuity with the BLAS-1 reduce-to-scalar cohort (`inner-product-fold-specialization`, `linear-combination-fold-specialization`), but `nrm2` is a CONSUMER of the `inner_product` fold, not a fold member, and there is no L1 family to "specialize" into (single leaf). The report itself records this tension in its body (intro + §"The rewrite" point 1) and in §"Open questions" with a `Defer`. This is a sibling case to D4's `dot-leaf-identity` rename consideration; it is a candidate rename follow-up (e.g. `nrm2-norm-consumer-identity`), not a hard defect — the body content is slug-agnostic and the slug resolves cleanly in SUMMARY/index. Surfaced for the meta-phase / a future lowering-verifier audit.

3. **(scope note — informational, no action) The nrm2 L2 floor's existence rides the open `l2-floor-under-l3-blas1-cohort` design fork.** The report correctly flags (both themes' §"Open questions") that the existence of the L2 `nrm2` floor — the LHS of the L2>L1 theme / the RHS of the L3>L2 theme — depends on the unresolved meta-phase decision on whether BLAS-1 leaves should get L2 floors. If that fork resolves against L2 floors, the L2>L1 theme dissolves and the L3>L2 theme re-homes as a non-adjacent in-line identity note at `L3/nrm2`. This is captured-not-resolved per dispatch instruction; no action in this dispatch. Noted here so the integrator sees the design-fork dependency is acknowledged.

4. **(co-land dependency — informational, no action) RHS/LHS `book/src/L2/nrm2.md` is not yet on disk.** Both themes reference the L2 `nrm2` floor body, which co-lands at integration from the wave-1 D2 harvester report (`reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/CYCLE.md`, dir confirmed present). Standard co-land pattern declared in frontmatter; the integrator must apply D2 before/with D5 so the `../L2/nrm2.md` links resolve at build. Not a report defect — surfaced so integration ordering is explicit.

## Repair

### Fixes attempted

1. **Finding** (citation-validity / cross-reference-integrity, low): Both theme bodies cite a non-existent section-anchor `§"Fold-cohort boundary"` of `book/src/L2/inner_product.md`; the supporting heading is `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` (`:390`).
   - **Decision**: repaired
   - **Action**: Verified on-disk (`grep -n "^#"` → the only consumer/fold-cohort heading is `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` at `book/src/L2/inner_product.md:390`; no `Fold-cohort boundary` heading exists). Corrected both occurrences of the named section title to `§"Consumer (NOT an instance)"`:
     - CYCLE.md `nrm2-fold-specialization.md` intro (former line 47).
     - CYCLE.md `nrm2-body-identity.md` §"L2 form (RHS)" (former line 368-369).
     The cited content fully supports the consumer-not-fold-member claim; only the named title was wrong. Mechanical title-substitution, non-build-breaking (prose §-reference, not a resolved `#anchor`).

2. **Finding** (directive-keyword, repairer-instruction item 2): The two NEW theme files used `edit:` directives instead of `new:`.
   - **Decision**: repaired
   - **Action**: Confirmed via `ls` that neither `book/src/L2-L1/nrm2-fold-specialization.md` nor `book/src/L3-L2/nrm2-body-identity.md` exists on disk (NEW creations, consistent with the critic's read that both are new theme chapters). Changed the two proposed-changes fence directives from `edit:` to `new:`:
     - ` ```edit:book/src/L2-L1/nrm2-fold-specialization.md ` → ` ```new:... `
     - ` ```edit:book/src/L3-L2/nrm2-body-identity.md ` → ` ```new:... `
     The four remaining `edit:` blocks (`L2-L1/index.md`, `L3-L2/index.md`, two `SUMMARY.md` insertions) target existing files and were left unchanged (verified present on disk).

### Unrepairable findings

None. The remaining critique items (2/3/4) are informational / meta-phase signal, not defects:
- Item 2 (`-fold-specialization` slug-vs-consumer-framing naming tension) — surfaced for the meta-phase / a future lowering-verifier rename audit; the body is slug-agnostic and resolves cleanly in SUMMARY/index. No fix in repair scope.
- Item 3 (the L2 `nrm2` floor's existence rides the open `l2-floor-under-l3-blas1-cohort` design fork) — captured-not-resolved per dispatch instruction; design-fork dependency, not a repairable defect.
- Item 4 (co-land dependency: `book/src/L2/nrm2.md` not yet on disk) — standard wave-1 D2 co-land pattern; integration-ordering note, not a report defect.

## Suggested resolution

`ready`. Both flagged warnings are repaired (section-anchor title corrected in both bodies; `new:` directive keyword applied to the two NEW theme files). Integrator notes:
- **Co-land ordering**: apply the wave-1 D2 harvester report (`reports/2026-06-01T051607Z-cycle-041-harvester-L2-nrm2/`) before/with this report so the `../L2/nrm2.md` links resolve at build (both new theme bodies + index rows reference the L2 `nrm2` floor body).
- The `l2-floor-under-l3-blas1-cohort` design fork (informational item 3) and the slug-rename consideration (item 2) are meta-phase signal — promote to the OQ ledger / priorities as the integrator-per-report sees fit; no blocking action.
