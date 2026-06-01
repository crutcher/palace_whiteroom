---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T19:20:20Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T19:35:00Z
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

# META: verification of "Combinator refactor — `linear_combination` family (replace-and-propagate)"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` over the whole report returns `31 ok, 0 failing` (all bounds-clean, paths hygienic). I then `--anchor`-checked the load-bearing pinpoints: the four `<<<OLD>>>` enacted-edit anchors (verified byte-exact + unique, see cross-reference-integrity below), `L2/linear_combination.md:19-20` ("does not replace"), `:316-345` (§Evidence "Self-verified"), `:176-178` (IEEE non-law deferral), `L2-L1/...:139-167` (pinned summation-order table), `L3/axpy.md:58` (no obstruction), `L4/krylov-step.md:67` + `L4/chebyshev.md:203` — all OK. Two pinpoint drifts surfaced, both in supporting/Pattern-instances prose (NOT in the enacted edits): (1) `L2/index.md:33` cited twice (Summary §:23, Pattern-instances §:55) for the "leaf-vs-fold realization RATIFIED (keep leaf-floor (b)), batch-12 meta-phase" text — `--anchor 'leaf-floor'` lands at line **28** (-5), and the quoted sentence in fact lives at line 28 (and a heading variant at line 45); line 33 is the bare `**Firm at L2**` header. (2) `L4-L3/krylov-step-typed-wrapper-dissolution.md:67` (b.4, §:284) for "renders the L3 body let-chain with `axpy` by name" — `--anchor 'axpy'` lands at line **68** (+1). The claims themselves are true (the text exists at the corrected lines); these are off-by-pinpoint, warning-tier. Note the report's frontmatter `status: pending` and the `## Proposed changes` self-summary are coherent with the four enacted `edit:` blocks.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (it modifies existing surface — the firm `L2/linear_combination.md` text) AND it is anchored to the 2026-06-01 vocabulary-shift redirect's combinator-as-entry mandate plus the unchanged cycle-018 evidence (signature/laws/L0 anchors are explicitly carried over, not re-asserted). The four edits change framing/role ("does not replace" → "the entry for this family"; leaves → "specialization notes") with the substantive algebra untouched. Not a pure rotation-claim-without-surface; the surface change IS the deliverable.

**rotation-quality — pass.** The enacted change (a) is an in-layer **role inversion**, not a cross-layer rotation, so the strict L_{n+1}/L_n compactness test is applied to the combinator-as-entry move: it makes the L2 surface strictly more abstract/compact (one variadic fold entry subsumes four mirrored arity chapters as notes — state/structure hiding, coarser substitution). This is the redirect's intended in-layer combinator consolidation, the opposite of a 1:1 rename. The (c) KEEP verdict on `linear-combination-fold-specialization` is correctly justified as a genuine translation (unbounded variadic fold → bounded fused-kernel family with a de-fusion at the arity-4 boundary + a source-grounded `γ==0` fall-through), NOT identity-in-named-terms — confirmed against the theme body (the arity-dispatch §:61-101 and the pinned summation-order table §:139-167 are real translation content no in-line note could carry). The contrast against the eight thin `*-body-identity`/`*-leaf-identity` smell themes is sound.

**variant-axis-coverage — pass.** The combinator's variant axes (arity = the unification axis; output-aliasing; element-type/scalar-promotion) are carried unchanged from the firm cycle-018 entry and are not re-opened by this refactor pass. The over-unification guard (do-NOT-merge `inner_product`, different codomain/combining-step) is explicitly preserved and is the subject of edit A4. No hidden branch introduced.

**cross-reference-integrity — pass.** All four `<<<OLD>>>` anchors verified byte-exact AND unique against `book/src/L2/linear_combination.md` (occurrences=1 each via exact-string match) — the build-readiness fence/anchor gate (`proposed-changes-fence-encloses-full-body-guard`) passes: four balanced `edit:` fences, each enclosing a complete OLD/NEW/END triple, no firm body authored outside a fence (this report enacts only surface edits, not a new firm chapter). Edit A4's NEW text introduces a live link `[`inner_product`](./inner_product.md)` and references its §"Sibling fold" — `inner_product.md` exists and DOES carry §"Sibling fold: linear_combination is not subsumed" (line 401) with the symmetric note already present, so the reciprocal cross-reference resolves and is not a dangling forward-ref. All (b.2) demotion-target theme files (4× `L3-L2/*-body-identity`, 4× `L2-L1/*-leaf-identity`) and all (b.4) L4-propagation files exist on disk. Verified-absence claims confirmed: `book/src/L3/linear_combination.md` does not exist; `grep -rl linear_combination book/src/L3/` returns no hits.

**edge-label-fidelity — pass.** The (c) re-audit is labeled L2-L1 (`linear-combination-fold-specialization`) and the prose discusses exactly the L2-fold→L1-leaf edge; the (b.3) L3-propagation plan and the (b.4) L4 note are correctly labeled to their respective edges (L3>L2 collapse, L4/L3 base-form-by-name). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** The report cleanly separates ENACTED (a) from MAPPED-FOR-CYCLE-050 (b) from RE-AUDIT-VERDICT (c). Spot-verified the map/enactment boundary the dispatch flagged: the only artifact-mutating blocks are the four `edit:book/src/L2/linear_combination.md` triples; there is NO `edit:`/`new:`/`delete:` block touching the L2 leaf chapters, `L3/linear_combination.md`, or any `*-body-identity`/`*-leaf-identity` theme — those are all prose recommendations under (b), explicitly gated on cycle-050 + the D3 cohort audit. No map item is enacted prematurely. The `## Proposed changes` section correctly declares only the (a) edits and adds no dep-map rough-in row (deferring the L3-combinator file to a cycle-050 harvester per the one-pattern discipline). Scope-respect confirmed: D1 did NOT author any `edit:` against `book/src/L2/inner_product.md` (D2's scope) — its only `inner_product` contact is the reciprocal sibling-fold note INSIDE `linear_combination.md` (edit A4), as scoped.

**skill-uptake-survey — warning.** The report's shape (a proposed-changes block with byte-exact `<<<OLD>>>` anchors, the build-readiness gate the dispatch explicitly invokes) maps to the `proposed-changes-fence-encloses-full-body-guard` skill and the `verify-citation-range`/`tools/citecheck` procedure; a `combinator-as-entry` inversion under the redirect also implicates `propose-rotation`/`verify-rotation-citation`. The report does not name any skill invocation. Pure telemetry surfacing, non-blocking — the anchors and fences are in fact correct, so uptake would have been confirmatory rather than corrective.

### Issues found

1. **[citation-validity, warning] `L2/index.md:33` pinpoint drift (-5), cited twice.** Report §Summary (CYCLE.md:23) and §Pattern-instances (CYCLE.md:55) cite `book/src/L2/index.md:33` for the "leaf-vs-fold realization RATIFIED (keep leaf-floor (b)), batch-12 meta-phase" text. The quoted sentence is at **line 28** (full form) / line 45 (heading variant); line 33 is the bare `**Firm at L2**` section header. `citecheck --anchor 'leaf-floor'` suggests `:28`. Claim is true; pinpoint should be corrected to `:28` (or `:45`).

2. **[citation-validity, warning] `L4-L3/krylov-step-typed-wrapper-dissolution.md:67` pinpoint drift (+1).** Report §(b.4) (CYCLE.md:283-284) cites `:67` for "renders the L3 body let-chain with `axpy` by name". The `axpy`-by-name token is at line **68**. `citecheck --anchor 'axpy'` suggests `:68`. Minor; in a cycle-050-deferred propagation note, not in an enacted edit.

3. **[skill-uptake-survey, warning] No skill invocation referenced.** The report performs the exact procedures covered by `proposed-changes-fence-encloses-full-body-guard` (build-readiness anchor/fence parity, which the dispatch explicitly calls the gate) and `verify-citation-range`/`tools/citecheck`, but names no skill. Surfacing only — the underlying work is correct.

Note for the repairer: the two pinpoint drifts (issues 1, 2) are surgical line-number corrections (`:33`→`:28`, `:67`→`:68`) with the corrected lines confirmed by `--anchor`. The enacted edits, the build-readiness gate, the KEEP-verdict justification, the map/enactment boundary, and the inner_product non-touch all pass clean — no substantive content defect found.

## Repair

### Fixes attempted

- **Finding**: [citation-validity] `L2/index.md:33` pinpoint drift (-5), cited twice (CYCLE.md §Summary :23, §Pattern-instances :55) for the "leaf-vs-fold realization RATIFIED (keep leaf-floor (b)), batch-12 meta-phase" text.
  - **Decision**: repaired
  - **Action**: Independently verified by reading `book/src/L2/index.md` — the full "RATIFIED (keep leaf-floor (b)), batch-12 meta-phase" sentence is at line **28**; line 33 is the bare `**Firm at L2**` section header. Corrected both pinpoints `:33`→`:28` in `CYCLE.md` (Summary line and Pattern-instances bullet). The trailing `,112` in the Summary citation was left as-is (bounds-valid, not flagged).

- **Finding**: [citation-validity] `L4-L3/krylov-step-typed-wrapper-dissolution.md:67` pinpoint drift (+1) (CYCLE.md §(b.4) :284) for "renders the L3 body let-chain with `axpy` by name".
  - **Decision**: repaired
  - **Action**: Independently verified by reading `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — the `axpy`-by-name token (`krylov_update K_aux op w … composition of L3-native axpy / axpby / axpbypcz / dot / nrm2 / scal`) is at line **68**. Corrected `:67`→`:68` in `CYCLE.md` §(b.4). Also corrected the same `:67`→`:68` pinpoint in §Supporting evidence (CYCLE.md, the L4-base-form-by-name evidence bullet) for cross-section consistency, since it is the same citation.

- **Finding**: [skill-uptake-survey, warning] No skill invocation referenced.
  - **Decision**: not-needed
  - **Action**: Telemetry-only surfacing. The critic confirmed the underlying anchors and fences are correct, so uptake would have been confirmatory rather than corrective. No edit required.

### Unrepairable findings

None. Both citation-validity drifts were surgical line-number corrections with the corrected lines confirmed by direct file read; the skill-uptake-survey warning is non-blocking telemetry.

## Suggested resolution

`ready`. The two pinpoint drifts are repaired (both underlying claims were true; only the line numbers slipped). All four enacted `<<<OLD>>>` anchors remain byte-exact and untouched (build-readiness gate still passes). No substantive content defect; the integrator may apply the four L2-entry-inversion edits to `book/src/L2/linear_combination.md` as-is.
