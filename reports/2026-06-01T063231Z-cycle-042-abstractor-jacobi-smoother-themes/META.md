---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
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
repaired_at: 2026-06-01T071800Z
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

# META: verification of "TWO adjacent thin-identity lowering themes for jacobi-smoother"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` clears all 20 citations (20 ok, 0 failing: bounds + path-hygiene). Every load-bearing pinpoint anchor resolves mechanically: `jacobi.cpp:38` (`Y[i] = DI[i] * X[i]`), `:103` (`Apply(dinv, x, y)`), `:80` (`Reciprocal`), `:102` (`initial_guess`), `jacobi.hpp:43` (`Mult(x, y)`), `jacobi.cpp:52-60` and `:61-69` (complex forward / dead-code transpose branches), `:79-80` (setup chain), `ksp.cpp:198-200`, `errorestimator.cpp:75-77`, `krylov-step-body-identity.md:97` (`whole-tensor`). I read `reference/palace/palace/linalg/jacobi.cpp:28-107` directly: the dead-code transpose branch is the `else` of `if constexpr (!Transpose)` at :52, and the report's transcription of the negated off-diagonal terms (`YR[i] = DIR[i]·XR[i] + DII[i]·XI[i]`, `YI[i] = -DII[i]·XR[i] + DIR[i]·XI[i]`) matches source lines 66-67 exactly. The L1 signature pinpoint `L1/jacobi-smoother.md:56-59` is accurate (the `jacobi_smoother :: ...` signature + `op.dinv ⊙ x = (ω · diag(A)⁻¹) ⊙ x` body sit at :56-59). The ONE drift: the report cites `book/src/L3/index.md:39` (in both theme bodies' §Justification/§Verified-against and the L3-L2 index row) for the cycle-036 D2 audit verdict naming `jacobi-smoother` the "thinnest constructed-operator gate, one `elementwise_product`" classification — but `--anchor 'jacobi-smoother'` reports DRIFT (anchor at line 37, -2 outside range). The exact quoted phrase actually lives at `L3/index.md:46` (the "(A) Identity-in-form L3 backfill candidates — 6 firm" bullet); line 39 is the blank table-terminus. The cited content is fully real and ~7 lines away in the same file; the `:39` pinpoint is itself the artifact's OWN stale self-citation (the firm `L3/jacobi-smoother` entry, the cycle-037 landing note at `L3/index.md:58`, and the report all repeat `L3/index.md:39` — line 39 was presumably the verdict location before later rows were inserted above it). Warning, not fail: the classification is verifiable, only the pinpoint drifted, and the drift is inherited from upstream artifact text rather than introduced. No `verified_against:` YAML block is emitted (abstractor report), so the round-trip sub-check is N/A.

**surface-or-evidence — pass.** Both proposals are `new:` chapters (not refinements of existing operator/theme text), each authoring a thin-identity lowering theme between firm/firming endpoints. They are surface-creating with structural + empirical-match justification, not pure rotation_claims. Retroactive-evidence framing is correct (the identity is observational on three pre-existing firm chapters). Applicable and clean.

**rotation-quality — pass.** This is the load-bearing check for an identity-in-form report and it is handled correctly. Neither theme falsely asserts a compaction/abstraction rotation; both explicitly declare identity-in-form and justify WHY the rotation is degenerate: `jacobi-smoother` is the thinnest constructed-operator gate (one elementwise product `op.dinv ⊙ x`), with no wrapper to rotate (no `(op,K,s)`→`IterState` consolidation, no outer-loop dissolution), no kernel fusion to unfold, and no iteration view / sequential obstruction. The L2>L1 "negative fusion observation" framing is correct — the genuine L2 fusion-rotation observation is *negative* (no fused multi-operation kernel exists; the complex four-multiply at `jacobi.cpp:52-60` is a single componentwise ℂ product, not a fused composition of separable L2 primitives) — and the substantive rotation in the whole chain is correctly deferred to the L1>L0 leaf-mutation themes (`reciprocal-elementwise-product-mutation-rotation` sub-pattern B + `jacobi-smoother-mutation-rotation`). This is the sanctioned identity-lowering pattern (CLAUDE.md "Identity-lowerings still require both L levels"), matching the `scal-body-identity` / `dot-leaf-identity` precedents the report cites. Pass — the report does not mis-sell an identity as a rotation.

**variant-axis-coverage — pass.** The gate's variant axes (element-type real/complex `dinv`; damping-mode default-ω vs estimated-ω; operator-representation) are explicitly absorbed into the opaque `op` closure and transported unchanged across both edges; the report states the "two orthogonal + one absorbed" variant profile transports identity-in-form. The dead-code `Apply<Transpose=true>` Hermitian branch (`jacobi.cpp:61-69`) is correctly handled as a non-law / dead-code consumer branch noted by reference (no consumer instantiates `Apply<true>`; `MultTranspose` aliases `Mult` at `jacobi.hpp:43`), not as a hidden live variant. No hidden branches. Pass.

**cross-reference-integrity — pass.** All `[link]` targets on disk resolve: `L3/jacobi-smoother.md`, `L1/jacobi-smoother.md`, `L3-L2/scal-body-identity.md`, `L2-L1/dot-leaf-identity.md`, `krylov-step-body-identity.md`, `ksp-solve-outer-driver.md`, `reciprocal-elementwise-product-mutation-rotation.md`, `jacobi-smoother-mutation-rotation.md`, the three index files. The one not-yet-on-disk target is `L2/jacobi-smoother.md` — referenced via live link `[`L2/jacobi-smoother`](../L2/jacobi-smoother.md)` throughout — which is the **declared co-landing wave-1 D5 dependency** (the report's frontmatter + §Status state D5 applies before these themes via wave-2 serial sequencing). This is the correct presupposition shape, not a dangling reference: at integration the D5 floor lands first, so the live link resolves. (The forward-reference to a not-yet-existing L2 `elementwise_product`/`reciprocal` floor is correctly kept PLAIN-TEXT per the rough-in-forward-reference convention — the report explicitly notes "The forward-reference is plain-text (no live link — target file does not exist)".) Build-readiness fence guard: 16 fences = 8 balanced blocks, even parity; the two `new:` bodies use 4-space indented code for signatures (no nested triple-backtick fences), so no nested-fence truncation risk; `## Status` + Signature + laws all sit INSIDE the `new:` fences. The two SUMMARY.md registrations and the four index-row/bullet edits match the existing `scal-body-identity` / `dot-leaf-identity` column structure. Pass.

**edge-label-fidelity — pass.** `jacobi-smoother-body-identity` carries the L3>L2 label; its prose, §"L3 form (LHS)" / §"L2 form (RHS)" headers, and the rewrite table all discuss exactly the L3→L2 edge (LHS = L3 whole-tensor field op, RHS = L2 floor gate). `jacobi-smoother-leaf-identity` carries the L2>L1 label; its §"L2 form (LHS)" / §"L1 form (RHS)" headers and the rewrite table discuss exactly the L2→L1 edge. Both narrate FORWARD / high→low (L3→L2 and L2→L1 respectively), consistent with the CLAUDE.md "Layers are defined high→low" invariant; reverse-direction lifting notes are correctly quarantined to §Open-questions working notes, explicitly marked "NOT in this high→low chapter body". No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Both declared `firm`, and the content shape is firm: identity-in-form theme between firm endpoints (L3 cycle-037 firm; L1 firm; L2 firm-this-cycle D5), no rough-in placeholders, no speculative operator, no negative-anchor reconstruction, no obstruction. The status lines correctly distinguish the firm structural claim from the two non-status-reducing caveats (the fork-independence note and the no-L2-elementwise_product-floor-yet forward-reference), neither of which gates firmness. The classification matches the `scal-body-identity`/`dot-leaf-identity` firm precedents. Pass.

**skill-uptake-survey — pass (telemetry).** The report's shape implies the citation-verification skill family; it references self-verification via `tools/citecheck/citecheck.py --anchor` (the cycle-024 mechanical realization of `verify-citation-range`) in both theme §Verified-against blocks and the §Supporting-evidence `[ok]` ledger. No `proposed-changes-fence-encloses-full-body-guard` invocation is referenced, but the fence structure is clean on inspection. Adequate uptake surfaced.

### Issues found

1. **`L3/index.md:39` pinpoint drift (citation-validity, low severity).** In BOTH theme bodies and the L3-L2 index row, the report cites `book/src/L3/index.md:39` for the cycle-036 D2 audit verdict's "thinnest constructed-operator gate, one `elementwise_product`" classification of `jacobi-smoother`. The quoted phrase is actually at `L3/index.md:46` (the "(A) Identity-in-form L3 backfill candidates — 6 firm" Working-Notes bullet); line 39 is a blank table-terminus line. `citecheck --anchor 'jacobi-smoother'` confirms DRIFT (resolves to line 37, suggested correction in-file). Specific occurrences: §"Justification kind / Empirical-match (secondary)" and §"Verified-against / Cross-layer audit" of `jacobi-smoother-body-identity.md`; §Status of the same; the `edit:book/src/L3-L2/index.md` row's justification column ("cycle-036 D2 audit `L3/index.md:39`"). NOTE for the repairer: the artifact ITSELF carries the stale `:39` self-citation (`L3/jacobi-smoother.md`, the `L3/index.md:58` landing note, and the firm `L3/index.md:33` row all say `:39`), so this is an inherited drift, not an originated error; whether to correct to `:46` here while the upstream artifact still says `:39` is a repairer/integrator judgment call. The classification content is fully real and verifiable either way.

2. **(Not a defect — flagged for integrator sequencing awareness.)** `book/src/L2/jacobi-smoother.md` does not yet exist on disk; both themes live-link it. This is the declared wave-1 D5 co-landing dependency (frontmatter `inputs` + §Status), and the report explicitly relies on wave-2 serial sequencing applying D5 first. Confirmed correct presupposition shape (not a dangling link), but the integrator must apply D5 before these two themes or the live links will dead-link at `cargo make book`. Surfaced so it is not lost.

3. **(Observation, no action.) Slug-convention coherence is correct.** The chosen slugs `jacobi-smoother-leaf-identity` (L2>L1) and `jacobi-smoother-body-identity` (L3>L2) correctly track the precedent naming axis (`-body-identity` for L3>L2 matching `scal-body-identity`; `-leaf-identity` for L2>L1 matching `dot-leaf-identity`), and the report explicitly and correctly justifies `-leaf-identity` over `-fold-specialization` on the no-fold-parent ground. The fork-independence claim (jacobi-smoother is standalone, NOT a member of the `linear_combination`/`inner_product` fold cohort, so the cycle-041 `dot-l2-leaf-floor-vs-fold-only-design` leaf-vs-fold fork does not reach it) is internally consistent and matches the precedent index-table framing. No issue — recorded as a positive verification of the focus points.

## Repair

### Fixes attempted

- **Finding (issue 1): `L3/index.md:39` pinpoint drift (citation-validity warning).** The report cites `book/src/L3/index.md:39` for the cycle-036 D2 audit's "thinnest constructed-operator gate, one `elementwise_product`" classification of `jacobi-smoother`; the quoted phrase actually lives at `L3/index.md:46` (line 39 is a blank table-terminus).
  - **Decision: repaired.** This is a pure pinpoint off-by-offset — the cited content is real and the correct anchor is a small, mechanically-verifiable distance away. Within repair authority ("citation line range off by a small offset"). No content authored.
  - **Action.** Verified `:46` on-disk first (`book/src/L3/index.md:46` carries the exact phrase "`jacobi-smoother` (thinnest constructed-operator gate, one `elementwise_product`)" in the "(A) Identity-in-form L3 backfill candidates — 6 firm" Working-Notes bullet; line 39 confirmed blank table-terminus). Then tightened all FOUR `L3/index.md:39` occurrences in `CYCLE.md` to `:46`:
    - line 227 — §Surface/justification prose ("The cycle-036 D2 cross-layer-cross-cutter audit (`book/src/L3/index.md:46`) …").
    - line 263 — §Supporting-evidence "Cross-layer audit" `[ok]` ledger bullet.
    - line 305 — §plan-kind / status-justification prose ("classification (`L3/index.md:46`)").
    - line 633 — the `edit:book/src/L3-L2/index.md` theme-table row's justification column (secondary `empirical-match` cite).
  - Post-edit grep confirms zero `index.md:39` remain in `CYCLE.md`; all four now read `:46`.

### Inherited-drift note + follow-up routing

The `:39` pinpoint is **inherited from the artifact's OWN stale self-citation**, not originated by this report: the firm `book/src/L3/jacobi-smoother.md` §Status, the `L3/index.md:33` firm row, and the `L3/index.md:58` cycle-037 landing-note bullet all still repeat `L3/index.md:39` for this same verdict (line 39 was presumably the bullet's location before later Working-Notes rows were inserted above it, displacing it to :46). Tightening this report to `:46` makes the report correct but creates a local `:46`-vs-upstream-`:39` inconsistency until the artifact sites are swept.

- **Repairer does NOT touch `book/`** (write-authority partition), so the upstream sweep is out of scope here.
- **Recorded a follow-up OQ** `l3-index-39-stale-self-citation-sweep-to-46` as item 5 of the report's top-level §"Open questions / caveats" block (for `integrator-per-report` to promote to `scaffolding/open-questions.md`). The OQ names the three upstream artifact sites and routes the `:39`→`:46` sweep to a future lifter / layer-intro-author L3-index-refresh pass (co-schedulable with any `L3/jacobi-smoother` re-anchor). This keeps THIS report correct and tracks the broader sweep rather than losing it.

### Unrepairable findings

None. The only warning finding (issue 1) was mechanically repairable. Issues 2 and 3 are critic observations explicitly marked "not a defect" / "no action" — no repair needed (issue 2 is integrator sequencing awareness, carried in the report frontmatter + §Status already; issue 3 is a positive verification). All other checks passed at critique.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- The single citation warning is repaired in-place (4 pinpoints `:39`→`:46`, verified on-disk).
- **Sequencing (issue 2, not a defect but load-bearing):** apply the wave-1 D5 `book/src/L2/jacobi-smoother.md` floor BEFORE these two themes, or the live links `[`L2/jacobi-smoother`](../L2/jacobi-smoother.md)` in both theme bodies will dead-link at `cargo make book`. The report relies on wave-2 serial sequencing for this.
- **Promote the new OQ** `l3-index-39-stale-self-citation-sweep-to-46` (report §Open-questions item 5) so the inherited upstream `:39`→`:46` sweep (`L3/jacobi-smoother.md`, `L3/index.md:33`, `L3/index.md:58`) is tracked for a future lifter / layer-intro-author pass.
- Count-ownership (report §Open-questions item 1) is correctly deferred to D11 (the +1 L3>L2 and +1 L2>L1 firm-count tallies) — no repairer action.
