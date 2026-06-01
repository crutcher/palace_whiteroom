---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T064500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T065200Z
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

# META: verification of "L2>L1 + L3>L2 thin-identity theme sketches — the elementwise pair (reciprocal + elementwise_product)"

## Critique

### Checks run

**citation-validity — warning.** `citecheck.py --scan` reports **16 ok / 0 failing** on all machine-parseable citations in the report; the four load-bearing pinpoints I re-anchored all clear: `krylov-step-body-identity.md:97` (anchor `L3-native`) `[ok]`; the prose pinpoints `L3/reciprocal.md:131` (anchor `no interposed` confirmed @131 within 125-135) and `L3/elementwise_product.md:149` are correct — my first `--anchor 'Lowers'` pass appeared to drift to the `## Lowers to` header at :129/:147, but the report references the *body* line (:131/:149), which is exactly right. The `book/src/L3/index.md:41` cohort-audit pinpoint is internally consistent with the artifact's own convention: the firm `reciprocal`/`elementwise_product` L3 rows themselves cite `book/src/L3/index.md:41` as the (A)-identity-in-form verdict home, so the report inherits the established self-citation anchor (NOT a fresh drift). All four L0 anchors (`vector.cpp:248-261`, `:257-259`, `vector.hpp:20`, `operator.cpp:478-487`, `:545-568`) are full-path, in-range, `[ok]`. No `verified_against:` YAML block is emitted (abstractor report, not a lowering-verifier audit), so that sub-check is N/A. The **warning** (not pass) is driven by the §Verified-against provenance lines (CYCLE.md:246-247, 720-721) that assert a file `book/src/L2-L1/reciprocal-elementwise-product-mutation-rotation.md` as the head of an "L2>L1 → L1>L0" chain — **no such L2-L1 file exists on disk** (the real firm theme lives only at `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`). As prose-provenance this is a soft citation defect; as a live link (see cross-reference-integrity) it is hard.

**surface-or-evidence — pass.** All four entries are `new:` files (net-new L2>L1 / L3>L2 theme chapters), not refinements of existing operator/theme text, so the refinement-surface-vs-retroactive-evidence gate does not bind. Each carries full rotation evidence (§"The rewrite" mapping table + §"Justification kind" structural+empirical-match + §Verified-against). Not a pure-rotation-claim-without-surface case.

**rotation-quality — pass.** The four edges assert pure *identity-in-form* rotations, and the report is scrupulous that these are the **degenerate-maximal** case of the identity property (total + bijective on a single leaf binding), explicitly justified by the methodology invariant **Identity-lowerings still require both L levels** — i.e. an identity edge is a *required* layer-coherence artifact, not a renaming masquerading as a rotation. The report does NOT overclaim compaction (it correctly states the L2/L1 and L3/L2 forms are value-thread-isomorphic, and locates the substantive rotation at the L1>L0 mutation-rotation). This is the sanctioned identity-lowering shape (precedents `scal-body-identity`, `dot-leaf-identity`); pass.

**variant-axis-coverage — pass.** Each theme enumerates its variant axes and carries them identically across the edge: `reciprocal` — single element-type axis (real `1/x[i]` / complex `z̄/|z|²`); `elementwise_product` — element-type axis + conjugation sub-axis (`ā ⊙ b` via `MultHermitianTranspose`). No hidden branch: the conjugate-variant consumer-duplicate dead-code caveat (CYCLE.md:698-704) is explicitly surfaced and scoped (live canonical `MultHermitianTranspose` vs. dead `jacobi.cpp` `Apply<Transpose=true>`), with the identity mapping the live axis. The fold-parent question (a potential hidden axis) is exhaustively scoped out as fold-free / fork-independent.

**cross-reference-integrity — fail.** Build-readiness fence guard passes (16 fences = 8 balanced pairs, even parity; every `## Status` + Signature + rewrite table sits INSIDE its `new:`/`edit:` fence — no firm-body-outside-fence defect). SUMMARY surgical-insert anchors resolve (`dot-body-identity` @SUMMARY:43 and `dot-leaf-identity` @SUMMARY:70 both present for the insert). All named slug endpoints exist on disk (L1/L3 `reciprocal`+`elementwise_product`, the dot/scal/krylov templates, both index dep-maps, `scal-fold-specialization`, `nrm2-fold-specialization`, concept `elementwise-product.md`). **However, two of the four new chapters carry a dead live-link:** inside `book/src/L2-L1/reciprocal-leaf-identity.md` (CYCLE.md:135) and `book/src/L2-L1/elementwise-product-leaf-identity.md` (CYCLE.md:601), the substantive-rotation reference is written `[...](./reciprocal-elementwise-product-mutation-rotation.md)`. Because both authored chapters live in `book/src/L2-L1/`, the `./` relative link resolves to `book/src/L2-L1/reciprocal-elementwise-product-mutation-rotation.md` — **which does not exist** (the firm theme is at `book/src/L1-L0/…`). This is a hard `linkcheck2` build error in both files. The L3>L2 body-identity siblings reference the same target correctly via `../L1-L0/…` (and the two index dep-maps + SUMMARY entries are clean). The slug-spelling split is internally consistent and does NOT contribute to this fail (see plan-kind-consistency).

**edge-label-fidelity — pass.** Each chapter's declared edge matches its prose throughout: the two L2>L1 leaf-identity themes narrate L2 (LHS) → L1 (RHS) forward, high→low; the two L3>L2 body-identity themes narrate L3 (LHS) → L2 (RHS) forward. The §"The rewrite (L2 → L1)" / "(L3 → L2)" headers, the mapping-table column order, and the §"L_n form (LHS/RHS)" labels are all consistent with the slug's edge. No L_{n+1}/L_n inversion anywhere. The "Lowers to" / lifting-direction notes are correctly quarantined to §Open-questions working-notes per the high→low layer-definition discipline.

**plan-kind-consistency — pass.** Declared kind is four `firm` identity-lowering themes; content shape matches (full §Status `firm` with §Signature, mapping table, §Justification kind, §Verified-against, no rough-in placeholders, no speculative operators). The underscore-vs-hyphen filename split (`elementwise_product-body-identity.md` underscore matching operator chapters; `elementwise-product-leaf-identity.md` hyphen matching the L2>L1 theme-slug convention; concept page `elementwise-product.md` hyphen) is **internally consistent** — every live cross-link, dep-map row, and SUMMARY registration uses the spelling matching its target filename, and all resolve on disk. Correctly self-flagged (OQ #2, theme-4 §Filename-convention note) as a meta-phase normalization signal, NOT a build defect — concur: it is a naming-hygiene surface for the meta-phase, not a critic-blocking issue.

**skill-uptake-survey — pass (telemetry).** The report invokes `tools/citecheck/citecheck.py --anchor`/`--scan` for L0 anchor self-verification (the cycle-024 mechanical citation discipline) and names the copied templates (`dot-leaf-identity`, `scal-body-identity`, `dot-body-identity`). The relevant identity-lowering skills are exercised by precedent-copy. No skill omission implied by the shape.

### Issues found

1. **[cross-reference-integrity / build-blocking] Dead `./` link to the L1>L0 mutation-rotation in BOTH leaf-identity themes.** `book/src/L2-L1/reciprocal-leaf-identity.md` §"L2 form (LHS)" (CYCLE.md:135) and `book/src/L2-L1/elementwise-product-leaf-identity.md` §"L2 form (LHS)" (CYCLE.md:601) both write the substantive-rotation reference as `[`reciprocal-elementwise-product-mutation-rotation`](./reciprocal-elementwise-product-mutation-rotation.md)`. Since both chapters live in `book/src/L2-L1/`, `./` resolves to `book/src/L2-L1/reciprocal-elementwise-product-mutation-rotation.md`, which does not exist — the firm theme is at `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`. Hard `linkcheck2` failure in two files. Correct relative path from an `L2-L1/` chapter is `../L1-L0/reciprocal-elementwise-product-mutation-rotation.md`. Severity: high (breaks the build). Note: the L3>L2 body-identity siblings reference the same target via the correct `../L1-L0/…` path, so the fix is a mechanical `./` → `../L1-L0/` correction in exactly these two spots.

2. **[citation-validity / provenance] §Verified-against asserts a non-existent `L2-L1/…mutation-rotation.md` file.** In both leaf-identity §Verified-against blocks (CYCLE.md:246-247 and 720-721) the chain is written `book/src/L2-L1/reciprocal-elementwise-product-mutation-rotation.md → book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md (firm)`. No `L2-L1/` file of that name exists; the firm theme exists only at `L1-L0/`. The intended meaning is presumably "this L2>L1 leaf-identity edge composes with the L1>L0 substantive rotation," but as written it names a file that is not on disk. Severity: low-medium (prose provenance, not a live link, so not build-blocking — but it asserts a path that does not resolve and reads as a real-file citation). Repair: drop the spurious `L2-L1/...` line and keep the `L1-L0/...` firm reference, or reword to "this L2>L1 edge → the firm L1>L0 `…/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`".

3. **[naming-hygiene / non-blocking, correctly self-flagged] `elementwise_product` family slug-spelling split.** Underscore (`elementwise_product-body-identity.md`, operator chapters) vs. hyphen (`elementwise-product-leaf-identity.md`, L2>L1 theme + concept page) now gives the same leaf two sibling-theme spellings. Every link resolves on disk and the split is internally consistent within each layer's convention, so this is NOT a defect — it is a meta-phase normalization signal, already surfaced in OQ #2 and the theme-4 §Filename-convention note. Recorded here only to confirm the critic concurs with the "flag for meta-phase, do not block" disposition. No repair required this cycle.

4. **[scope confirmation, no action] Count-ownership cleanly deferred.** The report appends only its four theme rows (2 to L2-L1/index, 2 to L3-L2/index), four SUMMARY registrations, and four bodies, and explicitly does NOT touch the consolidated §"Vocabulary cohort" firm tallies (CYCLE.md:1107-1120, OQ #1), deferring them to D11 to avoid `parallel-blind-shared-index-count-divergence`. This is the correct count-ownership partition; no tally assertion to verify. Confirmed no stray absolute-count edit leaked into the dep-map rows.

---

## Repair

### Fixes attempted

- **Finding 1 — [cross-reference-integrity / build-blocking] Dead `./` link to the L1>L0 mutation-rotation in BOTH leaf-identity themes.**
  - **Decision**: repaired
  - **Action**: Mechanical `./` → `../L1-L0/` correction on the two live-links. `book/src/L2-L1/reciprocal-leaf-identity.md` §"L2 form (LHS)" (CYCLE.md:135) and `book/src/L2-L1/elementwise-product-leaf-identity.md` §"L2 form (LHS)" (CYCLE.md:601). Both now read `[…](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)`, which resolves from an `L2-L1/` chapter to the on-disk firm theme `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (verified present, 48784 bytes). The link text is unchanged; only the relative path was corrected. This matches the path the L3>L2 body-identity siblings already use, and removes the hard `linkcheck2` break in both files. In scope per repair authority "Trivial cross-reference fix (broken `[link]` to a renamed/relocated file)".

- **Finding 2 — [citation-validity / provenance] §Verified-against asserts a non-existent `L2-L1/…mutation-rotation.md` file.**
  - **Decision**: repaired
  - **Action**: In both §Verified-against blocks (CYCLE.md:246-247 → now :247, and :720-721 → now :721) the spurious head line `book/src/L2-L1/reciprocal-elementwise-product-mutation-rotation.md →` was dropped and the entry reworded to "this L2>L1 leaf-identity edge composes with the firm L1>L0 `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) — …". The provenance now names only the file that exists on disk; the intended "L2>L1 edge composes with L1>L0 substantive rotation" meaning is preserved. Mechanical prose-path correction, no substantive content authored. Post-fix grep confirms zero remaining `L2-L1/…mutation-rotation.md` references in the report (all 7 references resolve to `L1-L0/` or `../L1-L0/`).

- **Finding 3 — [naming-hygiene / non-blocking, self-flagged] `elementwise_product` family slug-spelling split.**
  - **Decision**: not-needed
  - Per the dispatch note and the critic, the underscore/hyphen split is internally consistent (every link resolves on disk) and is a meta-phase normalization signal, not a defect. No repair this cycle.

- **Finding 4 — [scope confirmation] Count-ownership cleanly deferred.**
  - **Decision**: not-needed (no action requested by critic).

### Unrepairable findings

None. Both flagged findings (the build-blocking cross-reference fail and the provenance warning) were mechanical path corrections within repair authority.

## Suggested resolution

`ready`. The two build-blocking `./` live-links are corrected to `../L1-L0/…`, resolving to the on-disk firm theme, so `linkcheck2` will pass. The §Verified-against provenance no longer names a non-existent `L2-L1/` file. No substantive content was touched; the slug-spelling split remains correctly flagged for meta-phase normalization (OQ #2), and the count-ownership tallies remain deferred to D11 as intended. Integrator may apply.
