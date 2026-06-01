---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T064500Z
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
---

# META: verification of "Formalize reciprocal at L2" (cycle-042 D2)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` reports 14 ok / 0 failing on the whole CYCLE.md (bounds + path hygiene clean). All load-bearing pinpoints anchor-verified mechanically: `vector.cpp:248-261` (anchor `Reciprocal` @ :248), `:257-259` (anchor `XR` @ :257-258), `jacobi.cpp:80`/`:16` (anchors `Reciprocal`/`SPD`), `chebyshev.cpp:178`/`:241` (anchor `Reciprocal`), `bilinearform.cpp:278` (anchor `Reciprocal`), `vector.hpp:20`/`:107`/`:108` (anchors `mfem::Vector`/`reciprocal`/`Reciprocal`) — all `[ok]`. I read the complex kernel body (`vector.cpp:248-261`) directly: it is exactly `const auto s = 1.0 / (XR[i]*XR[i] + XI[i]*XI[i]); XR[i] *= s; XI[i] *= -s;` inside a `forall_switch` loop, with no zero-guard — confirming the meaning of the load-bearing claims (the `s = 1/|z|²` reuse realizes `z̄/|z|²`, law 5 and law 1 witnessed in-source, the no-zero-guard partiality). No `verified_against:` block present, so that sub-check is not applicable. No drift found.

**surface-or-evidence — pass.** This is a `new:` floor entry (`book/src/L2/reciprocal.md`), not a refinement of an existing operator/theme, plus an additive dep-map row and a SUMMARY registration — not a pure rotation_claim against existing surface. The refinement-shaped-proposal gate does not bind; the report creates new surface with its evidence inline.

**rotation-quality — pass (in the floor sense).** The report does NOT assert a substantive algebraic/structural rotation — it asserts an explicit **identity-in-form** floor (value-thread-isomorphic to L1), which is exactly the methodology-sanctioned shape for an `l2-floor-under-l3-blas1-cohort` entry (per **Identity-lowerings still require both L levels**). The renaming-only/1:1-mapping fail-trigger is aimed at proposals that *claim* a rotation while delivering an identity; here the identity is the declared, justified content (floor presence so the L3 leaf rests on an adjacent same-named L2 parent rather than skipping a layer). The single fusion candidate (the `s = 1/|z|²` intermediate) is correctly classified as a transparent factoring of the closed form, not a multi-op kernel fusion — matching the kernel I read. The thin-identity-floor justification is sound.

**variant-axis-coverage — pass.** One orthogonal variant axis (element-type real/complex), collapsed to a single parameterised operator, matching L1 and L3 exactly. Three non-axes are explicitly scoped out with reasons (zero-guard policy → precondition not axis; in-place/out-of-place → L1>L0 concern; `s`-intermediate + `forall_switch` host/device → transparent execution-model choice). No hidden branches: the real path (`mfem::Vector::Reciprocal` via the `:20` alias) and the complex path (`ComplexVector::Reciprocal` at `:248-261`) are both enumerated and unified under the element-type axis.

**cross-reference-integrity — pass.** All live `[link]` targets resolve on disk: `L1/reciprocal.md`, `L3/reciprocal.md`, `L2/dot.md`, `L2/scal.md`, `L2/nrm2.md`, `L2/index.md`, `L2/krylov-step.md`, `L2/inner_product.md`, `L2/linear_combination.md`, `L1/assemble-diagonal.md`, `L1-L0/reciprocal-elementwise-product-mutation-rotation.md`. Forward-references to not-yet-existing slugs (`elementwise_product`, the `L2-L1/reciprocal-*-identity` theme) are correctly left as **plain text**, not live links, per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention. Build-readiness fence guard: `grep -n '```'` shows 6 fences = 3 balanced blocks, even parity, no nested fences; the firm apparatus (`## Status` §349, `## Signature` §124, `## Algebraic laws` §201, `## Evidence` §423) all sit INSIDE the `new:book/src/L2/reciprocal.md` fence (lines 32–501) — no firm-body-outside-fence defect. The `:90`/`:91`/`:92` index.md anchors the report cites for the count tally and the leaf-vs-fold fork are accurate against the on-disk index.

**edge-label-fidelity — pass.** The two edge labels the entry carries (§"Lowers to" L2→L1, §"Lifts from" L1→L2) are discussed by prose that matches the exact edge: §"Lowers to" narrates the identity rotation downward to L1 and (forward) the substantive L1>L0 theme; §"Lifts from" narrates the value-thread-isomorphic upward identity. No mismatched edge label.

**plan-kind-consistency — pass.** Declared kind is a `firm` thin floor; the content shape matches — full Signature, eight algebraic laws with non-law catalogue, Status with firm-on-positive-structure justification, no rough-in placeholders. The firm judgement is anchored on the fully-present positive complex kernel (read in full) plus the upstream-aliased real method, with the missing-dedicated-test correctly handled by the firm-on-positive-structure escape (syntactic-identity laws, not convergence semantics) — consistent with the `dot`/`scal`/`assemble-diagonal` precedent. No-fold-parent / design-final framing is internally consistent.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` self-verification of all L0 anchors (the verify-citation-range mechanical realization) — the relevant skill for a citation-heavy floor harvest. Telemetry-only; no blocking.

### Issues found

No blocking or warning-level issues. The four focus areas adjudicated clean:

1. **Citation-validity (L0 anchors).** Verified mechanically (citecheck `--scan` + per-anchor `--anchor`) and by direct read of `vector.cpp:248-261`. The complex kernel, the `Reciprocal()` member, the four consumer sites, and the no-zero-guard policy are all supported. No +1-drift, no off-by-one.

2. **`firm` thin-identity-floor justification.** Sound. Value-thread-isomorphic to the firm L1 leaf; firm-on-positive-structure on a fully-present positive kernel body; missing-test correctly non-gating. Matches the cycle-041 `dot`/`scal` precedent.

3. **NO-fold-parent / design-final claim.** Correct. `reciprocal` is a nonlinear elementwise self-map (`1/(a+b) ≠ 1/a + 1/b`, law-7-adjacent non-law), so it neither reduces over the length axis (not an `inner_product` member) nor is a scalar-weighted-sum term (not a `linear_combination` member). The leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`, index.md:91) genuinely does not bind — there is no fold-parent to re-anchor into — so "design-final regardless of meta-phase adjudication" is a valid structural claim, not an overreach. The fork reference at index.md:91 is real and accurately characterized.

4. **Count-ownership (D11 owns the tally).** Respected. The `edit:book/src/L2/index.md` block (CYCLE.md:503–506) contains ONLY the `nrm2` anchor row (byte-identical md5 to the on-disk row, so the insert-after lands cleanly) plus the new `reciprocal` dep-map row — it does NOT touch the `:90` "firm 9 → 12" running tally or the §"Vocabulary cohort" / §"Identity-in-form BLAS-1 floors" bullet lists. The report's §Open-questions explicitly defers the consolidated count and the cohort-list additions to D11. SUMMARY.md edit inserts `reciprocal` between `nrm2` (on-disk :56) and `orthogonalize` (:57), matching the dep-map ordering. Body + own dep-map row + SUMMARY only — count-ownership partition honored.

5. **High→low discipline.** Honored. §Context explicitly states `reciprocal` is defined in L2 vocabulary; the two adjacent rotations are delegated to the separate lowering themes (D10); the chapter does not define the operator in terms of L1 primitives. The L1 entry is cited as authoritative-on-Palace-surface without re-defining the L2 operator downward.

6. **Fence parity.** Clean — 3 balanced blocks, even parity, no nested fences, firm apparatus enclosed.

Minor (non-blocking, informational, repairer may ignore): the entry forward-references `elementwise_product` and the L2>L1 `reciprocal` theme as plain text — both correct per convention; should an integrator-pass create an `elementwise_product` stub, the plain-text reference would become upgradeable, but that is downstream and out of this report's scope (the report flags it as such in §Open-questions).

---
repaired_at: 2026-06-01T070400Z
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

## Repair

### Fixes attempted

No critic findings to repair — all 8 checks returned `pass` with no warning/fail-level issues. Recorded as informational-no-defect; no per-finding repair was required. The single critic "Minor" note (plain-text forward-reference to `elementwise_product` / the L2>L1 theme) is correct-per-convention and explicitly out of this report's scope; nothing to fix.

**Cross-report consistency check (directed):** verified whether the firm `book/src/L3/reciprocal.md` (cycle-038 backfill) asserts that no interposed L2 entry exists — parallel to the elementwise_product case.

 - **Finding**: `book/src/L3/reciprocal.md` asserts "**no interposed L2 entry**" in five load-bearing locations — frontmatter `lowers_to:` (L3/reciprocal.md:5-6), §Context "Downward to L1" prose (:25), §"Lowers to" (:131, :133), and the related-entries note (:150). It states the L3>L1 hop is "**direct**" and that "the L2 layer hosts no standalone `reciprocal` entry." Once this cycle-042 L2 floor (`new:book/src/L2/reciprocal.md`) lands, those five assertions become stale/contradictory — the L3 leaf will then rest on an adjacent same-named L2 identity-in-form parent, so the chain is L3>L2>L1, not a direct L3>L1 hop.
 - **Decision**: unrepairable (defer to follow-up; does NOT block this report).
 - **Rationale**: The contradiction lives in the **artifact** (`book/src/L3/reciprocal.md`), which the repairer must not modify (write-authority partition + "Modify the artifact (book/, concepts/) directly" is explicitly out of scope). It is also **not** a trivial one-line reconciliation: it spans frontmatter + two full prose sections + a related-entries note, and the fix is a substantive re-framing (the "direct L3>L1 hop / no L2 entry" claim becomes "L3>L2 identity-in-form ∘ L2>L1 identity," with the new L2 floor as the interposed parent) — that is authoring, not a mechanical surgical edit. The L2-floor report under repair is itself clean; this is a downstream consequence of it landing, correctly routed as a lifter touch (the dispatch note + the cycle-042 abstractor themes already flag the stale L3 §Lowers-to). Recorded as a follow-up OQ rather than fixed here.

### Unrepairable findings

- **Stale "no interposed L2 entry" assertions in `book/src/L3/reciprocal.md` (×5 sites: :5-6, :25, :131, :133, :150).** Becomes contradictory once `book/src/L2/reciprocal.md` lands. Follow-up: a **lifter** touch on `book/src/L3/reciprocal.md` to re-anchor the L3>L1 "direct hop / no L2 entry" framing to the L3>L2>L1 chain (L3>L2 identity-in-form ∘ L2>L1 identity), updating the `lowers_to:` frontmatter, §"Downward to L1", §"Lowers to", and the related-entries note. This sits alongside the abstractor-flagged stale L3 §Lowers-to. Routed as an OQ for the integrator to promote, not blocking integration of this cycle-042 L2 floor (the L2 floor is independently sound; the L3 staleness is a known, methodology-sanctioned consequence of the layer-coherence backfill chain catching up — same shape as the cycle-041 `dot`/`scal` and the elementwise_product L2-floor landings).

## Suggested resolution

`ready` — apply the L2-floor report as-is; it is clean on all 8 checks and creates correct new surface (`book/src/L2/reciprocal.md` + its own dep-map row + SUMMARY registration; count tally correctly deferred to D11 per count-ownership).

Integrator note (non-blocking): when this L2 floor lands, the firm `book/src/L3/reciprocal.md` will carry five now-stale "no interposed L2 entry / direct L3>L1 hop" assertions (frontmatter :5-6, §Context :25, §"Lowers to" :131/:133, related-entries :150). Promote a follow-up OQ for a **lifter** re-anchor of `book/src/L3/reciprocal.md` to the L3>L2>L1 chain (consolidate with the abstractor's already-flagged stale L3 §Lowers-to so a single lifter dispatch closes both). Same reconciliation shape the `dot`/`scal`/elementwise_product L2-floor landings carried.
