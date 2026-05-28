---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: warning
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T00:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: unrepairable
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of L3 scal harvester report

## Critique

### Checks run

**citation-validity** — pass. Every claim in the report carries a citation pointer (file:lines or theme:section). Spot-checked load-bearing citations: `book/src/L1/scal.md` (verified — 100-line firm L1 entry; signature, semantics, 9 laws, 2 variant axes including scalar-promotion sub-axis all confirmed as inherited content); `book/src/L3/krylov-step.md` (verified firm L3 precedent with 6-field frontmatter and identity-in-form backfill rationale); `book/src/L3/index.md:13` (verified — line 12 reads "Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)"; `scal` is NOT named here, which the report correctly flags in Open Question #5); `book/src/L3-L2/krylov-step-body-identity.md:97` (verified — exact quote "The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal`) are firm post-cycle-004..."); `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:68` (verified — line 68 renders `krylov_update` body let-binding citing the BLAS-1 primitives including `scal`); `palace/linalg/vector.cpp:203-227` and `:207-211` (cited transitively from L1 entry, which directly verifies them); `palace/linalg/vector.hpp:262-270` (verified — `Normalize` template at line 264; range covers the body). Cross-layer-cross-cutter audit report exists and contains the cited HIGH CONFIDENCE recommendation at lines 47-49. All citations in range.

**surface-or-evidence** — pass. This is a refinement-shaped proposal (creating a new L3 entry where one did not exist; not a rotation_claim modification of existing surface). The proposal modifies surface (new `book/src/L3/scal.md` file, new row in `book/src/L3/index.md`, new SUMMARY.md entry) and is accompanied by a structural rotation_claim (identity-in-form L3 → L1). The pair (surface change + rotation claim) is properly formed.

**rotation-quality** — warning. The proposal asserts an explicit "identity-in-form" rotation L3 → L1. By the strict rotation-quality bar in §Checks, a renaming-only or 1:1 mapping is FAIL ("not a rotation"). The report repeatedly frames the L3 form as "value-thread-isomorphic" / "identical in body and signature" to L1 (e.g. §Lifts from line 159: "the L1 form's signature has no element loop exposed, no destination buffer, no MPI collective, no iteration view"; §L3 vs L1 distinction line 188: "the L3 form is identical in body and signature to L1"). This is by design — the cycle-009 methodology invariant **Identity-lowerings still require both L levels** *requires* an entry at the lower layer even when the rotation is trivial — and the report explicitly cites that invariant as load-bearing for its existence. The wave-1 `krylov-step` L3 backfill (cycle-010) is the structural precedent and passed prior critique with the same shape. **Not a failure on policy grounds** (the invariant overrides the strict rotation-quality bar for identity-lowering backfills). Marked **warning** because the rotation does NOT make the L_{n+1} form more compact/abstract/equational — it is by stipulation a layer-coherence anchor, not a compactifying rotation. The critic flags this for the integrator's attention so the rotation-quality telemetry does not silently drift on this category of backfill.

**variant-axis-coverage** — pass. The L1 entry has two variant axes — `element-type` (real/complex) and `scalar-promotion` (sub-axis on the complex element-type, real `α` against complex `x`). The proposal's frontmatter lists both axes; §Variant axes (lines 138-147) covers both with the same content as L1, marks the `scalar-promotion` sub-axis as inherited unchanged, and explicitly states (line 145) that `scal` has no L0 constant-folding branches on `α` (distinguishing it from `axpy` and aligning with `axpby`). The "absorbed at construction time" framing and the "no other variant axes" close-out are consistent. No hidden branches.

**cross-reference-integrity** — warning. Most `[link]` references resolve correctly: `../L1/scal.md`, `../L4/krylov-step.md`, `../L3/krylov-step.md`, `../concepts/scalar-promotion.md`, `../concepts/scal.md`, `../concepts/sequential-obstruction.md`, `../L1-L0/`, `book/src/L3-L2/krylov-step-body-identity.md`, `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` all verified present. **HOWEVER**, the proposed `book/src/L3/scal.md` references three sibling L3 files that do not yet exist on disk:
  1. §Dependencies > "Sibling subsumption" line 127: `[axpby](./axpby.md)` — resolves to `book/src/L3/axpby.md`, NOT PRESENT (only `book/src/L3/krylov-step.md` currently exists in `book/src/L3/`).
  2. §Dependencies > "Sibling subsumption" line 128: `[nrm2](./nrm2.md)` — resolves to `book/src/L3/nrm2.md`, NOT PRESENT.
  3. §Dependencies > "Downstream consumers" lines 132-133: `[krylov-step](./krylov-step.md)` — this one DOES resolve (krylov-step.md exists).

  The report acknowledges this situation in §"Supporting evidence" lines 301-303 ("Wave-1 sibling dispatch awareness") and §"Open questions / caveats" #2 (sibling dispatch coordination on L3 index.md). The expectation is that wave-1 sibling dispatches #1 (`apply_linop`), #2 (`axpy/axpby/axpbypcz`), and #3 (`dot/nrm2`) will land alongside this dispatch and produce the missing sibling files. Marked **warning** rather than fail because the links are coordinated cross-dispatch (not unprompted dangling refs), but the integrator must verify the sibling dispatches actually land their target files before applying this dispatch's links — if sibling dispatches #2 or #3 fail or defer, the `./axpby.md` / `./nrm2.md` links will be broken in the merged book.

**edge-label-fidelity** — pass. The proposal's stated edges are L3 → L1 (Lowers to) and L1 → L3 (Lifts from); both sections (lines 153-161) discuss exactly those edges. The L3 vs L1 distinction section (lines 185-190) reinforces the L3 ↔ L1 framing. No L4 wrapper-dissolution claim is made; the report correctly notes (line 74) that `scal` does NOT have an L4 entry per the cross-layer-cross-cutter audit's "L4 candidate (CONFIRMED-NOT-NEEDED)" verdict. No L3>L2 edge is asserted for `scal` itself (which is correct — `scal` is a leaf primitive, not a composition). Edge labels and prose are consistent.

**plan-kind-consistency** — pass. The proposal declares `firmness: firm` in the frontmatter (consistent with the L1 entry's firmness, the wave-1 `krylov-step` L3 backfill precedent, and the methodology invariant's intent — identity-lowering backfills inherit the firmness of the source entry). The §Status section (lines 149-151) elaborates: signature is canonical (matches BLAS-1 `dscal` / `zscal`), evidence is direct from L1, 9 algebraic laws are standard scalar-vector-multiplication facts. No rough-in placeholders, no speculative content, no missing semantics. Content shape (full operator definition with signature, semantics, 9 laws, dependencies, variants, evidence, distinction-from-adjacent-layer) matches "firm operator entry" shape.

**skill-uptake-survey** — warning. The report includes a §"Supporting evidence" subsection "MCP codemap tool usage" (line 306) that explicitly states no MCP codemap tools were invoked, with the rationale that "the L3 entry is value-thread-isomorphic to L1 by construction (identity-in-form rotation)" and "no fresh L0 line-range verification was needed for the rotation to L3." This is reasonable for an identity-lowering backfill. **HOWEVER**, the report makes NO reference to skill invocations from the available skills bank — neither `verify-citation-range` (despite citing many file:line ranges), `verify-refinement-surface` (despite being a refinement-shaped proposal), `classify-variant-axis` (despite involving two variant axes), nor `skill-selection`. The proposal's shape — citation-heavy, refinement-shaped, variant-axis-bearing — implies several relevant skills exist. The pure-presence check fails: zero skill mentions. Marked warning per the §Checks discipline ("surfaces telemetry, not blocking"). The wave-1 `krylov-step` L3 backfill (cycle-010 precedent) may have set the same pattern; meta-phase should aggregate.

### Issues found

1. **(rotation-quality — warning)** §Summary line 23, §Lifts from line 159, §L3 vs L1 distinction line 188 — the proposal explicitly asserts "identity-in-form" / "value-thread-isomorphic" / "identical in body and signature" rotation, which by strict §Checks rotation-quality discipline would be a fail. The harvester correctly invokes the cycle-009 methodology invariant **Identity-lowerings still require both L levels** to justify the entry's existence; this is the right policy mapping. Flagged as warning for telemetry purposes (so cycle-012 meta-phase can audit whether the identity-lowering-backfill cohort is silently warping rotation-quality pass-rates). No content fix indicated; this is a policy-tier signal, not a content defect.

2. **(cross-reference-integrity — warning, sibling-dispatch coordination)** Proposed `book/src/L3/scal.md`:
   - Line 127 references `[axpby](./axpby.md)` — target `book/src/L3/axpby.md` does not exist on disk; expected to land via sibling wave-1 dispatch #2.
   - Line 128 references `[nrm2](./nrm2.md)` — target `book/src/L3/nrm2.md` does not exist on disk; expected to land via sibling wave-1 dispatch #3.
   - The integrator's per-report serial application order (#1, #2, #3, #4 = this scal dispatch) determines whether these links are valid at any intermediate book-build. If wave-1 dispatch #2 or #3 fails/defers, the integrator must either (a) reorder application so this dispatch lands AFTER the missing siblings land, or (b) downgrade the sibling-subsumption note's links to plain text pending the sibling dispatches' arrival, or (c) reject this dispatch.

3. **(cross-reference-integrity — minor, no `L3-L1/` directory)** The proposal repeatedly refers to a hypothetical `book/src/L3-L1/` directory (e.g., §Lowers to line 155, §Open questions #1 line 310) that does not exist on disk. The report correctly notes the OQ `l3-l1-directory-naming-structure-policy` tracks the broader policy question and follows the wave-1 `krylov-step` precedent of capturing the identity rotation in-line at the L3 entry. The reference is hypothetical and properly framed. Not a broken link — the path is named as not-yet-existing — but this pattern recurs 4+ times across the BLAS-1 cohort and should be tracked as an upstream policy decision needed (Open Question #1 already does so).

4. **(L3 index `Semantics (overlay)` inventory gap — Open Question #5)** §Open questions #5 (line 318) self-identifies: the L3 index's `Semantics (overlay)` prose lists only "matvec, axpy, dot, nrm2 as field operations" — `scal` is implied by the BLAS-1 cohort reading but not literally named. The dispatch does NOT update the prose, only adds the dep-map row. This is properly flagged for a future layer-intro-author refresh dispatch; not a content defect of THIS dispatch, but a forwarded inconsistency.

5. **(skill-uptake-survey — warning, telemetry)** The report's §"Supporting evidence" / "MCP codemap tool usage" explanation is reasonable for the codemap-tool dimension. But the report makes zero reference to skill invocation (`verify-citation-range`, `verify-refinement-surface`, `classify-variant-axis`, `skill-selection`). The proposal's shape implies these are relevant. Pure presence-check signal; surfaces telemetry rather than blocks.

6. **(content-quality observation, not blocking)** §"Lowers to" line 155 mentions "no firm `scal-mutation-rotation` theme yet exists" and §"Open questions / caveats" #4 (line 316) repeats this as a forwarded watch-list item. This correctly acknowledges that the L3 → L1 → L0 chain reaches firm coverage only down to L1; the L1 → L0 hop is currently informal. Not a defect of THIS dispatch but a coverage gap properly forwarded. The integrator may want to surface this to cycle-012+ planner per the established pattern (analogous to `axpby-mutation-rotation` / `axpbypcz-mutation-rotation` having landed).

7. **(content quality, no fix needed)** The 9 algebraic laws in §Algebraic laws (lines 98-106) match the L1 entry's 9 laws exactly (Identity, Absorption×2, Composition, Distributivity×2, Negation, Inverse, Field-commutativity). The 5 "do not hold" cases (Idempotence, Commutativity-in-argument-positions, Distributivity-over-vector-products, Bit-level-equivalence-under-fusion, Step-composition-/outer-loop-lift) are inherited and properly contextualised — the fifth one (step composition / outer-loop lift) is novel-at-L3 and correctly framed as "structural, not a non-law in the usual sense" (line 114), with a forward-compare to `krylov-step`'s L3 entry that DOES have step-body structure. Faithful inheritance with appropriate L3-specific additions.

8. **(content quality, no fix needed)** §Iteration-rotation marker (lines 88-92) correctly identifies `scal`'s iteration view as "degenerate" — `scal` is a leaf primitive, not a step body, so the operator carries no iteration view of its own. This is the right framing for a BLAS-1 leaf primitive at L3 and aligns with `krylov-step`'s L3 entry where the iteration-rotation marker IS substantive (the body lifts as whole-tensor; outer loop does not lift).

9. **(content quality, no fix needed)** Frontmatter convention (6-field YAML; `lowers_to`, `lifts_from`, `variant_axes`) matches the wave-1 `krylov-step` L3 backfill precedent. Open Question #6 forwards the convention-codification question to cycle-012 meta-phase appropriately.

## Repair

### Fixes attempted

- **Finding**: rotation-quality warning — identity-in-form rotation flagged for telemetry per the identity-lowerings-both-levels methodology invariant.
  - **Decision**: unrepairable (methodology-compliance signal, not a content defect).
  - **Rationale**: The harvester correctly invokes the cycle-009 methodology invariant **Identity-lowerings still require both L levels** as load-bearing for the entry's existence. The warning is intentional telemetry for cycle-012 meta-phase aggregation across the identity-lowering-backfill cohort. No content fix is appropriate — repairing would mean either fabricating a non-identity rotation (substantive authoring; out of scope) or deleting the L3 entry (contradicts the methodology invariant).

- **Finding**: cross-reference-integrity warning — sibling L3 references `[axpby](./axpby.md)` and `[nrm2](./nrm2.md)` resolve to files that do not yet exist on disk; expected to land via wave-1 sibling dispatches #2 and #3.
  - **Decision**: repaired.
  - **Action**: Rephrased sibling-L3 forward references in CYCLE.md §Dependencies > "Sibling subsumption" (lines 127-128) to remove the `[axpby](./axpby.md)` and `[nrm2](./nrm2.md)` link forms. The prose now reads "once the sibling `axpby` entry lands (wave-1 dispatch #2 — `book/src/L3/axpby.md`), it will also be a leaf whole-tensor primitive" and analogously for `nrm2`. This makes the references safe under any integration ordering: if siblings #2 / #3 fail or defer, this dispatch's prose still composes correctly (the file paths are named as future-pointing, not linked). The third `./krylov-step.md` link in §Downstream consumers is preserved because the target exists. The L3 index dep-map row's `axpby β=0` reference is plain text (no link) so it required no change.
  - **Rationale**: This is the mechanical-fix shape per the critic's explicit guidance ("Could optionally rephrase as forward-pointing prose ('once axpby/nrm2 L3 entries land...') for safety"). Surgical edit; no content authoring.

- **Finding**: skill-uptake-survey warning — telemetry on skill-invocation patterns for cycle-012 meta-phase aggregation.
  - **Decision**: unrepairable (pure-presence telemetry; not a content defect).
  - **Rationale**: The harvester's choice not to invoke `verify-citation-range` / `verify-refinement-surface` / `classify-variant-axis` is reasonable for an identity-in-form backfill that transitively inherits L1's citation chain. The warning is methodological-pattern signal, not a content fix — meta-phase will aggregate this across the identity-lowering-backfill cohort.

- **Finding**: L3 index `Semantics (overlay)` inventory does not name `scal` (issue #4 in Critique).
  - **Decision**: not-needed (already covered by Open Question #5 in CYCLE.md and forwarded for a future layer-intro-author refresh dispatch).
  - **Rationale**: The report self-identifies this gap and properly forwards it via Open Question #5; no repair authority needed. The integrator-finalize will surface OQ #5 to cycle-012+ planner per established pattern.

### Unrepairable findings

- **rotation-quality warning** (identity-lowering methodology compliance): routed to cycle-012 meta-phase via the standard telemetry mechanism (no agent assignment needed; aggregated automatically).
- **skill-uptake-survey warning** (skill-invocation telemetry): routed to cycle-012 meta-phase for cohort-level pattern review.

Both warnings are policy-tier signals that the critic explicitly identified as non-blocking, so no follow-up agent dispatch is required.

## Suggested resolution

**`pass-after-repair`** — the report is ready for integrator-per-report application. The cross-reference-integrity fix removes the only mechanically-fixable issue; the two remaining warnings are methodological-telemetry signals (rotation-quality, skill-uptake-survey) that the critic explicitly flagged as non-blocking and that cycle-012 meta-phase will aggregate.

Integrator notes:
- The CYCLE.md edits at lines 127-128 (§Dependencies > "Sibling subsumption") now refer to `book/src/L3/axpby.md` and `book/src/L3/nrm2.md` as future-pointing prose rather than active links. If wave-1 sibling dispatches #2 and #3 land successfully in the same integration cycle, a follow-up integrator-finalize cleanup (or a future cohort refresh dispatch) may want to restore the `[name](./path)` link forms.
- Open Question #5 (L3 index `Semantics (overlay)` does not name `scal`) is forwarded as documented; integrator should ensure it lands in the OQ ledger.
- The four wave-1 BLAS-1 cohort dispatches share the same identity-in-form rotation rationale; aggregating their rotation-quality warnings is the cycle-012 meta-phase agenda item.
