---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T21:31:20Z
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
repaired_at: 2026-06-01T22:05:00Z
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

# META: verification of cycle-051 D1 — linear_combination family demotion + L3-leaf re-expression

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` over the report reports 27 ok / 0 failing. The three load-bearing L0 anchors were `--anchor`-confirmed AND read in source: `vector.cpp:702-712` (`AXPY`, anchor at 702) carries the `if (alpha == 1.0) { y += x; } else { y.Add(alpha, x); }` fast-path at 704-706; `vector.cpp:745-758` (`AXPBYPCZ`, anchor at 746) carries the `if (gamma == 0.0) { add(alpha, x, beta, y, z); }` branch at 749-751; `vector.cpp:726-730` (`AXPBY`, anchor `add` at 729) carries the single aligned `add(alpha, x, beta, y, y)` pass. The report's frontmatter `verifies: ../REPORT.md` is the standard stub (the report file is `CYCLE.md`); not a content defect. No `verified_against:` block in this report — the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a refactor/demotion report, not a refinement of a single operator. It modifies surface (deletes 8 themes, re-expresses 4 leaves, de-links 3 kept gates, corrects 1 stale-tense passage) and is backed by the cycle-049 replace-and-propagate map + the deleted themes' own degenerate self-descriptions (verified below) + the redirect directive. The deletions are the "translation not rename" enactment, not a bare rotation_claim. Pass.

**rotation-quality — pass.** The substantive rotation (arity-dispatch fusion-selection + pinned summation order) is correctly NOT claimed in the re-expressed leaves — it is explicitly deferred to the KEPT `L2-L1/linear-combination-fold-specialization` theme (firm, `L2-L1/index.md:14`), which the leaves now reference as their lowering home. The demotion targets are genuine degenerate identity-in-named-terms lowerings: I confirmed each deleted theme self-describes as such — `scal-body-identity.md:9` "The body IS the identity", `axpy-body-identity.md:9` "The body IS the identity. `axpy` ... no wrapper", `axpbypcz-leaf-identity.md:7,139` "value-thread-isomorphic ... All fusion content is the fold-parent's". The re-expression makes the leaves MORE abstract (arity-N specializations of one combinator) rather than 1:1 renames. Pass.

**variant-axis-coverage — pass.** The load-bearing variant facts are preserved in the re-expressed leaves and re-homed correctly: AXPY `α==1.0` fast-path cited at `vector.cpp:702-712` in `L3/axpy.md` §"Lowers to" new-text; AXPBYPCZ `γ==0` arity-collapse cited at `vector.cpp:745-758` incl. `:749-751` in `L3/axpbypcz.md`; AXPBY aligned `add(α,x,β,y,y)` pass cited at `vector.cpp:726-730` in `L3/axpby.md`. None of the three load-bearing branches was dropped in the framing swap. The output-aliasing variant axis is explicitly attributed to the fold-parent (correct per the combinator home). Pass.

**cross-reference-integrity — FAIL.** A surviving file carries SIX live links to deleted slugs that the report does NOT touch. `book/src/L3/index.md` rows 24/25/26 each carry TWO live links (in the "Lowers via" column and the "Downward" column) to `../L3-L2/axpy-body-identity.md`, `axpby-body-identity.md`, `axpbypcz-body-identity.md` — none re-pointed, none de-linked. When the 8 themes are deleted (change (a)), these become hard `linkcheck2` build errors. I enumerated all live links to the 8 deleted slugs from surviving files: the 4 `L3/{scal,axpy,axpby,axpbypcz}.md` leaves (handled (b)), `L3/linear_combination.md:111` (handled (e)), the 3 divfree/jacobi gates (handled (c)) — and `L3/index.md` (UNHANDLED). The leaf↔body cross-links among the 8 deleted files self-resolve (those files vanish). This is the cycle-019-class build-breakage defect: a `delete` whose inbound-live-link sweep missed one surviving table. Severity HIGH (build-breaking).

**edge-label-fidelity — pass.** The L3>L2 / L2>L1 edge labels in the re-expressed leaves and the (c)/(e) de-links discuss the matching edges. The "Downward to L2" identity edge is correctly cited at `L3/linear_combination.md:107-113` (verified present), and the transitive L3>L1 in-line annotation correctly invokes the cycle-012 non-adjacent convention. No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared shape is a demotion+re-expression refactor (lifter). Content matches: 8 deletes, 4 in-place re-expressions through a kept combinator, defensive de-links, own-row SUMMARY/dep-map removal with tally deferred to D5. The re-expressed leaves stay `firm` (their bodies are unchanged; only the lowering route re-anchors) — consistent. Pass.

**skill-uptake-survey — warning.** The report invokes `tools/citecheck/ --anchor` for the two new L0 anchors (good). However, this report is a multi-file DELETE with inbound-live-link cleanup — exactly the shape the `proposed-changes-fence-encloses-full-body-guard` neighborhood and a "deleted-slug inbound-live-link sweep" procedure target. No skill exists for the inbound-link sweep, and the report's own de-link reasoning (c)/(e) was done ad-hoc and missed `L3/index.md`. The miss is itself evidence a checklist-style sweep skill would have caught it. Surfaced as telemetry, non-blocking.

### Issues found

1. **[HIGH / build-breaking] `book/src/L3/index.md` retains 6 live links to deleted slugs — not handled by the report.** `L3/index.md:24` (×2: `axpy-body-identity`), `:25` (×2: `axpby-body-identity`), `:26` (×2: `axpbypcz-body-identity`) link to `../L3-L2/*-body-identity.md`. Change (a) deletes those files; these become `linkcheck2` errors. The report touches `L3/index.md` only as a citation source (`:11-14`), never as an edit target. Fix path: re-point each to `../L3-L2/` combinator route (or `[`linear_combination`](../L3/linear_combination.md)` §"Downward to L2") consistent with the (b) leaf re-expressions, OR plain-text de-link per the (c) pattern. This is the load-bearing defect for D1.

2. **[MEDIUM / markdown-rendering] L3-L2 dep-map row deletion leaves a blank line mid-table.** Change (d)'s `book/src/L3-L2/index.md` edit replaces rows 17-20 (old_string, verified contiguous and exact) with an empty new_string (a single blank line). A blank line terminates a GFM table — rows 21+ (`jacobi-smoother-body-identity` onward) would split into a second table or render as literal pipes. Old_string matches exactly; the issue is the empty replacement. Fix: replace with nothing (zero blank lines) so rows 16 and 21 abut, preserving one continuous table.

3. **[LOW / stale-but-non-breaking] `L3-L2/index.md:37-41` "Lowering themes" bullet list references deleted slugs as code-spans.** Lines 37 (`axpy-body-identity`), 38 (`axpby-body-identity`), 39 (`axpbypcz-body-identity`), 41 (`scal-body-identity`) are backticked code-span references (not live links), so non-breaking, but they describe themes that no longer exist after (a). The report does not touch them. Recommend folding into the demotion note or removing, ideally in the same pass (or explicitly deferring to D5 alongside the tally — but the report does not mention them at all).

4. **[LOW / stale-but-non-breaking] `jacobi-smoother-body-identity.md` retains 4 code-span references to `scal-body-identity` after the 2 live links are de-linked.** Change (c) correctly de-links the two LIVE links (lines 12, 40 — both old_strings verified present and exact). Four further code-span / path references remain: `:126`, `:173`, `:211` (in an Evidence/Dependencies path list: `book/src/L3-L2/scal-body-identity.md (cycle-041 D6 firm)`), `:265`. Non-breaking; stale. Same disposition recommendation as issue 3.

5. **[LOW / acceptable-as-scoped, confirm] Residual future-tense phrasing in `L3/linear_combination.md` left for a bounded follow-up.** The report (§(e), Discipline notes, Open questions) applies only the build-breaking `:111` live-link fix + tense correction, and explicitly defers the other future-tense passages (§"Arity specializations" `:50-61` "still exist firm as of this cycle ... collapse ... is cycle-051 (gated)", §Context `:26`, §Status `:150`, §Dependencies `:117`, §Lifts-from `:154`, §Evidence `:162`). I verified `:61` and `:117` do carry the stale "is cycle-051 (gated)" / "their re-expression ... is cycle-051" phrasing. These are prose, not live links, so they do NOT break the build — deferring them is acceptable as scoped. The report's own caveat (Open questions bullet 2) correctly notes "stand firm" remains TRUE post-D1 (the leaves are re-expressed, not deleted), so no contradiction is introduced — only the scheduling tense is stale. Acceptable to defer; flag for D5/integrator awareness so the deferral is a conscious choice, not a silent miss. NOTE these deferred touches do not interact with issue 1: `L3/index.md` is a different file and IS build-breaking.

### Anchor/fence mechanical confirmations (for the repairer)

- Report fence parity: 72 fence markers = 36 balanced pairs (report's "36 balanced fences" claim confirmed; includes the 8 single-pair `delete:` fences).
- SUMMARY.md (d) old_strings: L3-L2 block matches lines 51-57 exactly; L2-L1 block matches lines 92-98 exactly. Both correctly preserve the non-demoted neighbors (`nrm2-body-identity`, `ksp-solve-outer-driver`, `jacobi-smoother-body-identity`; `inner-product-fold-specialization`, `dot-leaf-identity`, `nrm2-leaf-identity`).
- L2-L1/index.md (d) old_string matches rows 15-20 contiguously; new_string correctly re-emits rows 16-17 (kept `inner-product-fold-specialization` + `dot-leaf-identity`), dropping 15/18/19/20. Row 14 (`linear-combination-fold-specialization`, KEPT) untouched. Correct.
- L3-L2/index.md (d) old_string matches rows 17-20 exactly (table rows; verified the `[`slug`](./slug.md)` link form). See issue 2 re: the empty replacement.
- (c) de-link old_strings: `jacobi-smoother-body-identity.md` edit-1 (line 12 block) and edit-2 (line 39-40 block) both present and exact; `divfree-projector-body-identity.md` and `divfree-projector-leaf-identity.md` old_strings present and exact.
- (e) `L3/linear_combination.md:111` old_string present and exact; the `:107-113` "Downward to L2" pre-built home and `:50-61` "Arity specializations" both verified present (the absorption targets exist as the report claims).
- 8 deleted theme files all present on disk (correct pre-integration state); kept files (`L2-L1/linear-combination-fold-specialization.md`, `L3/linear_combination.md`, `L2/linear_combination.md`) all present.
- `L3/scal.md` carries NO references to `scal-body-identity`/`scal-leaf-identity` (report claim confirmed — no per-leaf dead-link cleanup needed there beyond frontmatter/Context/Lowers-to/Lifts-from, which (b.1) handles).

## Repair

### Fixes attempted

- **Finding 1 (cross-reference-integrity, FAIL, build-breaking)**: `book/src/L3/index.md` rows 24/25/26 retained SIX live links to the deleted `axpy-body-identity` / `axpby-body-identity` / `axpbypcz-body-identity` slugs (two per row — §Dependencies column + §"Lowers to" column), unhandled by the report.
  - **Decision**: repaired.
  - **Action**: added a new proposed-changes section **(f)** to `CYCLE.md` (inserted before `## Discipline notes`) with three `edit:book/src/L3/index.md` blocks. Each re-points its row's two live links from the deleted `*-body-identity.md` slug to the combinator route — the [`linear_combination`](./linear_combination.md) §"Downward to L2" identity-in-form edge (no per-leaf body-identity theme) + the KEPT L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme — mirroring exactly how D1's (b) leaf edits re-expressed the leaves. Each `[old]` row was confirmed byte-exact against on-disk `L3/index.md` (rows 24/25/26). The status cell gains a "re-expressed cycle-051 D1 through the `linear_combination` combinator" provenance clause. The `scal` row (row 30) carries no `scal-body-identity` link (it links L1 `scal` directly via the in-line identity-in-form note) — verified, so no change there, consistent with the report's own §59 note.
  - **Inbound-link sweep re-run** (the sweep the report missed): `grep -rE` over `book/src/` for all live `[..](..)` links to the 8 deleted slugs confirms the complete inbound set is now covered — `L3/index.md` rows 24/25/26 (now (f)); the 4 leaf prose links `L3/axpy.md:97,:114` / `axpby.md:101,:118` / `axpbypcz.md:106,:125` (all inside the report's (b.2)/(b.3)/(b.4) `[old]` blocks); `L3/linear_combination.md:111` ((e)); the 3 gate files ((c)); and the leaf↔body cross-links AMONG the 8 deleted files (self-resolve when both endpoints vanish). No surviving file retains a live link to a deleted slug after all blocks apply.

- **Finding 2 (markdown, MEDIUM)**: the (d) `book/src/L3-L2/index.md` deletion of rows 17–20 used an empty `[new]` that would leave a table-breaking blank line (terminating the GFM table mid-stream, splitting rows 21+ into a broken second table).
  - **Decision**: repaired.
  - **Action**: rewrote the (d) `L3-L2/index.md` block to use the proven kept-neighbor-re-emit pattern (the same shape the report's own L2-L1/index.md (d) edit uses): `[old]` now spans rows 16–20 (the KEPT `ksp-solve-outer-driver` row 16 + the four deleted `*-body-identity` rows 17–20); `[new]` re-emits ONLY row 16. Result: rows 16 and 21 (`jacobi-smoother-body-identity`) abut with no intervening blank line — one continuous table. Row 16 text confirmed byte-exact against on-disk `L3-L2/index.md:16`; rows 16–21 verified all `|`-prefixed table rows (contiguous, 6 of 6).

- **Finding 3 (LOW, residual future-tense phrasing in `L3/linear_combination.md`)**: deferral ruled acceptable by the critic (prose-only, non-build-breaking).
  - **Decision**: not-needed (left as-is per the critic's ruling).
  - **Rationale**: these are tense-only touches in a firm, pre-built combinator home D1 is otherwise not authoring; they break no link (the only live-link error in that file, `:111`, is fixed by the report's own (e)). The report's Open-questions bullet 2 correctly notes "stand firm" remains TRUE post-D1, so no contradiction is introduced — only scheduling tense is stale. Flagged for the integrator/D5 awareness as a conscious deferral, consistent with the critic's disposition.

### Build-readiness verification

- `tools/citecheck/citecheck.py --scan CYCLE.md --quiet` → 27 ok, 0 failing (exit 0). The new (f) block introduced no new `path:lo-hi` citations.
- Fence parity: 78 fence markers = 39 balanced `edit:`/`delete:` pairs (was 36; +3 pairs from the three new (f) `edit:` blocks). No nested fences inside any block.
- Anchor uniqueness: each (f) `[old]` row's distinctive Dependencies-cell fragment (`via \`${slug}-body-identity\`(..); concepts:`) matches exactly once in `L3/index.md`; the (d) `[old]` ksp-solve-outer-driver row 16 fragment matches exactly once in `L3-L2/index.md`.
- The load-bearing facts (AXPY `α==1.0` fast-path `vector.cpp:702-712`, AXPBYPCZ `γ==0` `:745-758`, AXPBY aligned-pass `:726-730`) and the high→low re-expression were NOT touched — only the L3/index.md row links re-pointed and the L3-L2/index.md deletion block reshaped.

### Unrepairable findings

None. Both build-breaking findings (the L3/index.md live-link FAIL and the L3-L2/index.md table termination) were mechanical and surgical — re-pointing stale links to the combinator route D1 already established for its own leaves, and reshaping a deletion block to the kept-neighbor-re-emit pattern already used elsewhere in the same report. No substantive authoring was required.

## Suggested resolution

`overall_status: ready`. Both build-breaking defects are fixed; `cross-reference-integrity` is now satisfied across the full inbound-live-link set, and the L3-L2/index.md table stays contiguous. Integrator notes:
- The skill-uptake-survey `warning` (critic): this report was a multi-file DELETE whose inbound-live-link sweep was done ad-hoc and missed `L3/index.md`. The miss is exactly the shape a "deleted-slug inbound-live-link sweep" checklist skill would catch. Recorded below as a skill candidate.
- The LOW residual future-tense phrasing in `L3/linear_combination.md` (§"Arity specializations" `:50-61`, §Context `:26`, §Status `:150`, §Dependencies `:117`, §Lifts-from `:154`, §Evidence `:162`) is deferred-by-design; D5/integrator may fold it into the indexes tally pass or a batch-16 micro-sweep.
