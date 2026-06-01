---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T213141Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T214500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of cycle-051 D2 — inner_product/dot family demotion

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` clears the report at 20 ok / 0 failing. I re-verified every load-bearing on-disk anchor by hand against the current tree: `L3/inner_product.md:148-152` (§Specializations `dot`+`tdot` bullets — confirmed; the `dot` bullet is the Hermitian/`M=I` specialization, the `tdot` bullet carries the type-API-surface-only caveat), `L3/inner_product.md:363-385` (§"Downward to L2" pre-built home — confirmed, names the `dot-body-identity` demotion provenance), `L1/dot.md:43` (anchor "Conjugation convention", `⟨x,y⟩ = xᴴ y`, conjugate-linear arg-1 — confirmed), `L1/dot.md:104-105` (the L0/L1 layer bullets — confirmed), and `vector.cpp:674-685` (the `yᴴ x` complex re-order, carried verbatim as an inherited-transitive citation, not re-localized — consistent with high→low). All 16 `[old]:` blocks across the eight target files (`L3/dot.md` ×6, `L3/inner_product.md` ×2, `L2/inner_product.md` ×2, `L3/index.md` ×2, `divfree-projector-*` ×4, `SUMMARY.md` ×2, `L3-L2/index.md` ×2, `L2-L1/index.md` ×2) match on-disk byte-exactly. No `verified_against:` block in this report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (re-expresses an existing firm L3 operator + deletes two existing themes). It modifies surface (the `L3/dot.md` body + frontmatter + four surviving files) and the evidence is the pre-existing firm combinator homes + the KEPT fold-specialization theme — the change *routes* to existing rotation evidence rather than asserting new rotation claims. The two deletions are backed by the genuine-degeneracy argument (verified below). Not a bare rotation_claim; passes.

**rotation-quality — pass.** The two deleted themes are genuinely degenerate. I read `L3-L2/dot-body-identity.md` in full: its entire content is "the L3>L2 body edge is the identity… the iteration rotation is already complete at the signature level… fusion content carried by the fold-parent." That is the §1d vocabulary-failed-to-shift smell the redirect names — no rotation, a 1:1 named-term restatement. `L2-L1/dot-leaf-identity.md` likewise only *defers* to `inner-product-fold-specialization`. Deleting them and routing through the combinator (the genuine reduce-to-scalar abstraction) + the KEPT fold-specialization (the genuine conjugation/weight/re-order translation) is a correct compaction, not a rename. The re-expression makes `L3/dot` strictly more abstract (it speaks *through* the combinator instead of re-deriving the base form).

**variant-axis-coverage — pass.** The two variant axes (element-type real/complex; conjugation-convention hermitian/unconjugated `tdot`) are preserved in the unedited §Signature kernel table (line 50, `tdot` unconjugated bilinear) and §"Variant axes" (lines 119-121), and explicitly carried in the frontmatter `variant_axes:` block (unchanged). The `tdot` API-surface-only evidentiary caveat is routed to the combinator homes (not dropped). No hidden branch.

**edge-label-fidelity — pass.** The report's edges are L3>L2 (the demoted `dot-body-identity` + the new §"Downward to L2 (through inner_product)") and L2>L1 (the KEPT `inner-product-fold-specialization`). The prose discusses exactly those edges; the new header's parenthetical "(through inner_product)" correctly names the combinator routing. The transitive L3>L1 identity is annotated in-line per the cycle-012 non-adjacent convention, correctly labeled.

**plan-kind-consistency — pass.** Declared shape is a lifter re-anchor (theme demotion + leaf re-expression + defensive de-link). Content matches: structural rewrite, no new authored content, deferred tally to D5. Consistent.

**skill-uptake-survey — warning.** The report performs the proposed-changes fence-parity discipline (50 fence lines, even, all blocks well-formed) and a deleted-slug inbound-link census, but does not name-invoke `proposed-changes-fence-encloses-full-body-guard` or the `verify-citation-range` mechanical realization despite doing the equivalent work by hand. Pure telemetry; non-blocking.

**cross-reference-integrity — fail.** Two findings, both on the defensive-de-link / cross-dispatch-dangler reasoning (the report's stated special-attention area). See Issues 1 and 2. The intra-D2 surface is clean (all D2-owned old_strings match, fences balanced, the new L3/dot relative links all resolve, SUMMARY/index row removals target real lines), and the *deferral* reasoning for the axpy/axpby/axpbypcz/jacobi families is sound — those slugs genuinely die with their D1/D4 delete-target files. The failure is specifically that the two files D2 *chose to edit* (`divfree-projector-*`) are misanalyzed.

### Issues found

**Issue 1 — D2 edits `divfree-projector-body-identity.md`, but that file is DELETED by the sibling D4 dispatch (cross-dispatch edit collision; D2's "surviving file" premise is false). Severity: high (build-readiness / apply-ordering).**
Location: CYCLE.md §(c) edits at lines 243-255 ("Defensive de-link of inbound LIVE links in surviving cross-dispatch files"); the framing at §Discipline-notes line 330 ("The two surviving firm cross-dispatch files… both survive (firm; not demotion targets)").
The sibling report `reports/2026-06-01T210700Z-lifter-jacobi-divfree-demotion/CYCLE.md` (D4) carries ` ```delete:book/src/L3-L2/divfree-projector-body-identity.md ` (its §1, line 36) and re-anchors the `L3/divfree-projector.md` body to an in-line note. So `divfree-projector-body-identity.md` does NOT survive — it is a D4 delete target. D2's two edits to it (the `[old]:` blocks at report lines 245 and 252) are therefore on a doomed file: harmless-but-moot if applied D2-then-D4, or a per-report apply failure if applied D4-then-D2 (the `old_string` won't match a deleted file). This is exactly the cross-dispatch edit-conflict D2 says it is avoiding for the axpy/jacobi files — but D2's premise ("both survive") is factually wrong for this one. The D3 sibling (`lifter-nrm2-consumer-demotion`) correctly flags this same collision in its OQ-2; D2 does not. Net effect on the artifact is benign (the file is deleted either way, so no dangling link results), but the report's reasoning is unsound on a file it actively edits, and integrator serial-ordering is required to avoid an apply failure.

**Issue 2 — three-way same-paragraph collision on the KEPT `divfree-projector-leaf-identity.md` (D2 + D3 + D4 all touch it); D2 leaves the `nrm2-leaf-identity` live link it does not own, and does not flag the collision. Severity: medium (build-readiness / apply-ordering).**
Location: CYCLE.md §(c) edits at lines 257-276 (three edits to `divfree-projector-leaf-identity.md`), specifically the line-266 paragraph `([dot-leaf-identity] / [nrm2-leaf-identity] / …)`.
`divfree-projector-leaf-identity.md` is KEPT (D4 explicitly preserves it; plan line 130 "KEEP `divfree-projector-leaf-identity` (L2>L1) reachable"), so D2's de-link of the `dot-leaf-identity` live link there is correct and necessary. However: (a) the same line-266 paragraph also carries a live link to `nrm2-leaf-identity.md`, which is a D3 delete target — D2's edit converts only the `dot-leaf-identity` link and leaves the `nrm2-leaf-identity` link live; D3 separately de-links it (D3 §(c), and D3's OQ-2 flags the collision). Both D2 and D3 edit the identical line-266 paragraph, requiring careful integrator serialization or one edit's `old_string` will fail to match after the other applies. D2 does not surface this collision (its Open-questions section only discusses the axpy/jacobi *deferred* slugs, not the divfree *edited* ones). (b) D2's line-19/22 edits to this same file also overlap D4's edits to it (D4 re-anchors the `dot-body-identity` cross-reference at its line 36). The KEPT file is touched by three dispatches in the same regions; the report's discipline note (line 330) frames divfree as cleanly D2-owned, which understates the collision surface.

**Issue 3 — header-anchor mismatch between D2's prose reference and the actual `L3/inner_product.md` header. Severity: low (cosmetic / navigation).**
Location: CYCLE.md §(b) new content, repeated references to `L3/inner_product.md` §"Downward to L2" (e.g. report lines 110, 95).
D2's new prose names the combinator's section as §"Downward to L2" and the new L3/dot section as §"Downward to L2 (through inner_product)". The on-disk `L3/inner_product.md` header is exactly `## Downward to L2` (confirmed at line 366) — so the reference is correct. But note these are prose section-name references, not live `#anchor` links, so there is no link-resolution risk; flagging only that the two same-named sections (one in `inner_product.md`, one newly created in `dot.md` with a parenthetical) could confuse a future grep-by-header. Non-blocking.

**Non-issues confirmed (special-attention items that passed):**
- high→low discipline: the re-expressed `L3/dot` defines `dot` in L3 vocabulary *through* the same-layer `inner_product` combinator; the `lowers_to:` frontmatter correctly moves from the old non-adjacent `L1/dot.md` pointer to the adjacent `L2/inner_product.md`; no L1/L0 base-form re-derivation is reintroduced (the old §"Lowers to" L0-evidence re-derivation is removed, routed to the L1 leaf + L1>L0). Confirmed pass.
- load-bearing-fact preservation: the value-bearing conjugation (`xᴴ y`, `yᴴ x` L0 re-order), the `tdot` unconjugated variant (§Signature kernel table line 50, laws 11-13), the IEEE-754 reduction-tree non-law (§Semantics line 60, §Algebraic-laws line 98, §"Iteration-rotation marker" line 66), and the no-sequential-obstruction claim (line 66) are all preserved in unedited sections and/or routed to the KEPT `inner-product-fold-specialization` theme. Confirmed pass.
- the substantive conjugation/weight translation is correctly routed to the KEPT `L2-L1/inner-product-fold-specialization.md` (not deleted, not duplicated). Confirmed pass.
- deleted-theme degeneracy: both `dot-body-identity` and `dot-leaf-identity` are genuine vocabulary-failed-to-shift smells. Confirmed pass.
- D2's *deferral* of the axpy/axpby/axpbypcz/jacobi-family inbound links is sound: those referencing files (`axpby-body-identity`, `axpy/axpby/axpbypcz-leaf-identity`, `jacobi-smoother-leaf-identity`) are all confirmed delete targets of D1 (`lifter-linear-combination-family-demotion`) and D4 (`lifter-jacobi-divfree-demotion`), so their live links to D2's deleted slugs die with the files. The integrator-ordering caveat D2 raises for these is the correct disposition.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, HIGH — cross-reference-integrity)**: D2 carried two proposed-changes edits to `book/src/L3-L2/divfree-projector-body-identity.md` on the false premise that it is a "surviving cross-dispatch file"; that file is DELETED by sibling D4 this cycle.
  - **Decision**: repaired.
  - **Action**: Dropped both `edit:book/src/L3-L2/divfree-projector-body-identity.md` blocks from CYCLE.md §(c) (the line-19 and the cohort-sibling edits). Corrected the false premise in four places: §inputs frontmatter (split the combined input line into a KEPT `divfree-projector-leaf-identity` line and a separate "DELETED by D4 — no D2 edit, repair-dropped" line for `divfree-projector-body-identity`); §Summary (the de-link sentence); §(c) header prose (now states D4 deletes the file, the inbound link dies with it, no D2 edit needed); §Discipline-notes line 330 (replaced the "both survive" framing with the corrected per-file disposition). Verified on-disk: D4 (`reports/2026-06-01T210700Z-lifter-jacobi-divfree-demotion/CYCLE.md` §1) carries `delete:book/src/L3-L2/divfree-projector-body-identity.md`. Net artifact effect is benign (file deleted either way) but the report's reasoning + the apply-ordering hazard are now correct.

- **Finding (Issue 2, MEDIUM — cross-reference-integrity)**: the KEPT `divfree-projector-leaf-identity.md` is co-edited by D2/D3/D4; D2 did not surface the collision.
  - **Decision**: repaired.
  - **Action**: KEPT all three of D2's edits to `divfree-projector-leaf-identity.md` (lines 19, 22, 266) — this file SURVIVES (D4 preserves it), so the live link to D2's deleted `dot-leaf-identity` would genuinely dangle; the de-links are necessary. Verified all three D2 `old_string`s match the on-disk file byte-exactly and uniquely (`grep -Fc` = 1 each). Verified the co-edit substring geometry against the sibling reports: D2 line 19 (D2-only), D4 line 36 (`body-identity` re-anchor, D4-only) — non-colliding distinct lines; **line 266 collides** — D2 drops the `dot-leaf-identity` live link and D3 (`lifter-nrm2-consumer-demotion`) drops the `nrm2-leaf-identity` live link from the same paragraph, with D2's `old_string` a substring of D3's 3-line `old_string`. Added an explicit 3-way co-edit flag to §(c) header prose and a dedicated Open-questions bullet directing the integrator to serialize the two line-266 edits (apply one, re-derive the other's `old_string`). Updated the supporting-evidence census line to match.

- **Finding (Issue 3, LOW — cosmetic)**: same-named-section grep ambiguity between `inner_product.md` §"Downward to L2" and the new `dot.md` §"Downward to L2 (through inner_product)".
  - **Decision**: not-needed (note only).
  - **Rationale**: the critic confirmed these are prose section-name references, not live `#anchor` links — no link-resolution risk. Cosmetic navigation note only; no edit applied. The parenthetical disambiguator already present on the `dot.md` header is sufficient.

### Unrepairable findings

None. Both substantive findings (Issues 1 and 2) were mechanical cross-reference / apply-ordering corrections within repair authority: dropping moot edits to a file another dispatch deletes, and surfacing a co-edit collision the report omitted. No substantive authoring, no content decisions, no artifact mutation. The skill-uptake-survey warning is pure telemetry (non-blocking, the critic already noted it as such).

## Suggested resolution

`ready` for the integrator, with one serial-ordering note carried into the report's Open questions: when applying D2/D3/D4 against `book/src/L2-L1/divfree-projector-leaf-identity.md` (KEPT), the two line-266 edits (D2's `dot-leaf-identity` de-link, D3's `nrm2-leaf-identity` de-link) hit the same paragraph and one's `old_string` is a substring of the other's — apply one, then re-derive the second's `old_string` against the post-edit text. D4's line-36 edit and D2's line-19 edit are non-colliding. The `divfree-projector-body-identity.md` file is a D4 delete target — no D2 edit touches it, so no ordering concern there (it is deleted, its inbound `dot-body-identity` link dies with it). All remaining D2 edits verified byte-exact + unique against on-disk; proposed-changes fence parity holds (46 fences = 23 open + 23 close).
