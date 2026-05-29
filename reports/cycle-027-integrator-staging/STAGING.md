# cycle-027 integrator staging log

Per-report integration rows, append-only, newest LAST. integrator-finalize reads this to reconcile the cycle (rebuild, commit, push, cycle-end housekeeping).

---

## 2026-05-29T175529Z-abstractor-normalize-rotation
applied_at: 2026-05-29T19:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/normalize-mutation-rotation.md (created — new firm L1>L0 theme)
- book/src/L1-L0/index.md (edit — appended dep-map row after matrix-weighted-norm-mutation-rotation)
- book/src/SUMMARY.md (edit — inserted chapter entry between matrix-weighted-norm-mutation-rotation and lu-solve-mutation-rotation)
- book/src/L1/normalize.md (edit — live-link upgrade at §"L1 vs L0 distinction", line 104: plain-text ref → live link `[normalize-mutation-rotation](../L1-L0/normalize-mutation-rotation.md)`)
- scaffolding/open-questions.md (append — clause-scoped RESOLVED disposition on `normalize-mutation-rotation-l1-l0-theme`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 0 (scan clean — see Notes)
- SUMMARY.md chapter registration auto-fix: 0 (report proposed the SUMMARY edit itself)
- index-placeholder displacement auto-fix: 0 (index.md carried real rows, no placeholder)
- implied-component stub materialization: 0 (full firm theme authored, no stub needed)

Open questions promoted:
- normalize-mutation-rotation-l1-l0-theme (disposed RESOLVED — ENACTED; clause-scoped append, status-line not struck per append-only convention)

Build-relevant: yes

Notes:
- citecheck `--scan` on the report CYCLE.md: **43 ok, 0 failing (43 citations checked)** — matches the report's self-reported 43/0 and the critic's mechanically-verified 43/0 exactly. No MISS / AMBIG / OOB. (DRIFT is anchor-level, not surfaced by `--scan`; the critic already ran `--anchor` pinpoint spot-checks upstream — all landed exact, no drift.)
- All three proposed-changes blocks applied as-authored. The `new:` file body uses 4-space-indented code blocks (no nested triple-backtick fences) — no nested-fence truncation hazard; the full firm body landed intact. The two `edit:` anchors were exact-byte matches against the current index.md (matrix-weighted-norm row, was line 30) and SUMMARY.md (matrix-weighted-norm/lu-solve pair, was lines 104-105).
- **Integrator follow-up ENACTED (live-link upgrade):** the report (§Open questions, line 466) + critic (Note 2) flagged the plain-text ref at `book/src/L1/normalize.md:104` for upgrade now that the theme file exists on-disk. Applied the surgical upgrade per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (replaced the trailing parenthetical "...references it as plain text, not a live link" with the live link + "authored cycle-027"). No OQ-for-c028-follow-up needed — done inline.
- deferred integrated_at to finalize per role-spec (the consumed report's `integrated_at:` / `integration_commit:` frontmatter is finalize-only authority; not touched here).
- Standard `lowering-verifier` `verified_against:` audit (sole-overload + returned-norm consumer-cohort completeness) is the noted next-cycle follow-up, NOT a blocker / status reduction — recorded in the OQ disposition residual.

---

## 2026-05-29T175529Z-lifter-cycle026-hygiene-reanchors
applied_at: 2026-05-29T19:40:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/matrix-weighted-norm.md (edit ×3 — Correction 1 brace-drift `:601-606`→`:602-606` at the two body-quoting sites [law 8 + Composition note]; Correction 2 Category-4→Category-1 workspace relabel at the Context line)
- book/src/L0/linalg-operator-file.md (edit ×3 — Correction 2 at `:33` [Category-4→Category-1, the `operator.cpp:621-639` line] + Correction-2-residual at `:73` [Category-4→Category-1] and `:80` ["Categories 2 and 4"→"all Category 1"])
- book/src/concepts/givens.md (edit — Correction 3 source-cite `gmres.md`→`palace/linalg/iterative.cpp:634-640` with sub-range pinpoints)
- book/src/L1/bilinear-form.md (edit — Correction 4 `dot_bilinear` provenance-note refresh, false slug-discrepancy premise dropped)
- scaffolding/open-questions.md (append ×5 — clause-scoped RESOLVED dispositions on the four hygiene OQs + one NEW residual OQ `linalg-operator-file-category-mislabel-residual-lines-22-87`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 1 expected-AMBIG (non-blocking — see Notes); 27 ok / 1 AMBIG
- SUMMARY.md chapter registration auto-fix: 0 (no new files created)
- index-placeholder displacement auto-fix: 0 (no index rows touched)
- implied-component stub materialization: 0 (pure re-anchor pass; no forward-references to materialize)

Open questions promoted:
- matrix-weighted-norm-l1-entry-norml2-body-brace-boundary-drift-601-606 (disposed RESOLVED — ENACTED, Correction 1)
- bilinear-form-workspace-category-4-mislabel (disposed RESOLVED for named sites, Correction 2 + Correction-2-residual; one narrower residual split off)
- linalg-operator-file-category-mislabel-residual-lines-22-87 (NEW — opened for the two out-of-scope sites `:22`/`:87`, c028 follow-up)
- givens-concept-page-source-cite-staleness-gmres-md-should-be-iterative-cpp (disposed RESOLVED — ENACTED, Correction 3)
- bilinear-form-slug-name-coordination (residual disposed RESOLVED — ENACTED, Correction 4; companion plan candidate `bilinear-form-dot-bilinear-provenance-note-refresh` discharged)

Build-relevant: yes

Notes:
- All six surgical `[old]`/`[new]` edits applied verbatim, single-occurrence each. D1 (abstractor-normalize-rotation) did not touch any of these files; re-read each from disk before editing.
- citecheck `--scan` on the report CYCLE.md: **27 ok, 1 failing** — matches the repairer's verification (27/1) exactly. The single failure is the EXPECTED `[AMBIG] operator.cpp:621-639` inside the Correction-2 `[old]`/`[new]` payload that MUST match `linalg-operator-file.md:33`'s bare-basename convention verbatim (fully-qualifying the path inside the edit payload would break `[old]` applicability). This is a correct preserve-verbatim, NOT a citation defect — confirmed non-blocking by both dispatch instruction and the critic (META.md §critique note 3 / §repair Verification). Applied as-is, NOT path-qualified.
- Correction-2 + Correction-2-residual: after application, the four dispatch/critic-named sites in `linalg-operator-file.md` (`:33`/`:73`/`:80`) + `matrix-weighted-norm.md:9` are all internally consistent at "Category 1 — operator-composition workspace". TWO further same-file sites (`:22`/`:87`) carry the same wrong label but were OUT of the named scope; opened as the new residual OQ `linalg-operator-file-category-mislabel-residual-lines-22-87` for a c028 follow-up sweep (per dispatch instruction). Repairer deliberately did not widen into them.
- LOW non-blocking critic note (Issue 2): pre-existing stale section-name "Why this file pair matters" in `bilinear-form.md`'s Correction-4 surrounding-bullet tail (out-of-payload) — NOT corrected (outside the `[old]`/`[new]` payload + LOW); recorded as a note on the `bilinear-form-slug-name-coordination` OQ disposition, not a standalone OQ.
- deferred integrated_at to finalize per role-spec (the consumed report's `integrated_at:` / `integration_commit:` frontmatter is finalize-only authority; not touched here).

---

## 2026-05-29T175529Z-lowering-verifier-matrix-weighted-norm-audit
applied_at: 2026-05-29T20:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md (edit — appended additive `verified_against:` block, 19 entries, as a `~~~yaml` tilde-fenced block at EOF; NO content edit, NO status change — theme stays firm)
- scaffolding/open-questions.md (append — clause-scoped RESOLVED/AUDIT-CLOSED disposition under new slug `matrix-weighted-norm-mutation-rotation-lowering-verifier-audit-followup`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate to finalize per role-spec — this is dispatch 3 of the cycle; finalize sees the full staging log)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0 (theme on-disk; verified no pre-existing `verified_against:` YAML key — line 455 was a prose mention of the anticipated audit, not a key)
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 0 (scan clean — see Notes)
- SUMMARY.md chapter registration auto-fix: 0 (no new files created)
- index-placeholder displacement auto-fix: 0 (no index rows touched)
- implied-component stub materialization: 0 (audit-only; no forward-references to materialize)

Open questions promoted:
- matrix-weighted-norm-mutation-rotation-lowering-verifier-audit-followup (NEW slug, disposed RESOLVED — AUDIT-CLOSED for the theme; verdict fully-supported, no contradiction, no status reduction; residual `matrix-weighted-norm-mixed-element-type-variant` L1-ENTRY promotion gate migrates to the plan — the L1 entry `matrix-weighted-norm.md` stays `rough-in (test-coverage-bounded)`, and a firm lowering of a rough-in operator is legitimate per the `eigsolve-mutation-rotation` precedent)

Build-relevant: yes

Notes:
- Pure additive audit landing. Re-read the theme file from disk before editing: D1 (abstractor-normalize-rotation) created the SIBLING `normalize-mutation-rotation.md` and D2 (lifter-hygiene) touched `L1/matrix-weighted-norm.md` + `L0/linalg-operator-file.md` — NEITHER touched THIS theme file (`L1-L0/matrix-weighted-norm-mutation-rotation.md`, the cycle-026-landed theme). Confirmed no pre-existing frontmatter `verified_against:` key; the only `verified_against` token at line 455 was prose anticipating this very audit. The 19-entry block is appended cleanly after the §Status closing prose.
- Per the repairer's explicit note (META.md §repair finding 2 + §Suggested resolution): the inner `~~~yaml` tilde fence is intentional + integrator-ready (toggle-safe — the tilde fence does NOT cross-toggle the backtick `edit:` block; channel-conformant — the `cross-layer-cross-cutter` parser keys on the `verified_against:` leading text which survives the tilde form). Applied as a proper `~~~yaml … ~~~` fenced block at EOF; tilde fence NOT stripped.
- citecheck `--scan` on the report CYCLE.md: **48 ok, 0 failing (48 citations checked)** — matches the report's self-reported 48/0, the critic's mechanically-verified 48/0, and the dispatch instruction's expected 48/0 exactly. No MISS / AMBIG / OOB. (DRIFT is anchor-level, not surfaced by `--scan`; the critic already re-ran `--anchor` on every decisive pinpoint upstream — all landed line-exact, no drift; the theme-file `--scan` was 39/0.)
- deferred integrated_at to finalize per role-spec (the consumed report's `integrated_at:` / `integration_commit:` frontmatter is finalize-only authority; not touched here).
- For finalize: this is an audit `verified_against:` metadata append to `book/src/*.md` (Build-relevant: yes), so the rebuild will re-render the theme chapter with the new fenced-yaml block at EOF; the tilde-fenced yaml renders as a fenced code block (intended).

---

## 2026-05-29T175529Z-harvester-ls-update-column-l1
applied_at: 2026-05-29T20:30:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/back_solve.md (created — new firm L1 leaf; the GMRES/FGMRES restart-correction back-solve `(R: UpperTri, s) -> y`)
- book/src/L1/index.md (edit ×2 — appended dep-map row after the `nleps_eigenvalue_correction` row + cohort bullet after the `nleps_eigenvalue_correction` bullet, both using slug `back_solve`)
- book/src/SUMMARY.md (edit — inserted chapter entry `back_solve` under L1, after `nleps_eigenvalue_correction` and before the `# L1 > L0 — Lowering` Part header)
- scaffolding/open-questions.md (append ×2 — `ls-update-column-l1-leaf` RESOLVED resolved-on-arrival + NEW carry-forward OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate to finalize per role-spec — this is dispatch 4 of the cycle; finalize sees the full staging log)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0 (all three `edit:` anchors present + unique — `nleps_eigenvalue_correction` dep-map row at index.md:93, cohort bullet at :52, SUMMARY `nleps_eigenvalue_correction` at :84)
- variant-axis missing on multi-variant operator: 0 (three axes — element-type / basis-lift / restart-dim — all enumerated + resolved-as-absorbed; critic verified pass)
- bookkeeping incomplete: 0 (count-motif 20→21 bump deliberately DEFERRED to layer-intro/finalize per report scope — NOT a bookkeeping miss; the report's proposed-changes do not include the count edit and I did not invent one)
- citecheck bounds + path-hygiene lint: 0 (scan clean — see Notes)
- SUMMARY.md chapter registration auto-fix: 0 (report proposed the SUMMARY edit itself, using the correct `back_solve` slug)
- index-placeholder displacement auto-fix: 0 (index.md carried real rows, no placeholder)
- implied-component stub materialization: 0 (full firm leaf authored, no stub needed)

Open questions promoted:
- ls-update-column-l1-leaf (disposed RESOLVED — resolved-on-arrival; landed under renamed slug `back_solve`, NOT `ls_update_column`; the `ls_update_column` slug remains free for the still-un-harvested column-streaming leaf; the `trsv` L3-inventory gap stays OPEN)
- incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor (NEW — carry-forward for the c028 planner: dispatch-5 came back needs-revision, its terminal-back-solve refs need re-anchoring to the now-firm `back_solve` leaf; also gated on the still-un-harvested `ls_update_column` column-streaming leaf)

Build-relevant: yes

Notes:
- **`overall_status: ready` confirmed** (META.md:25). All three proposed-changes blocks applied as-authored (post-repair, using the renamed slug `back_solve`).
- **Slug collision re-confirmed collision-FREE before applying** (per dispatch instruction): grepped `book/src/L1/` + `book/src/SUMMARY.md` for `back_solve` → zero hits; `book/src/L1/back_solve.md` did NOT pre-exist; no `back_solve` slug or SUMMARY entry pre-existed. The repairer's no-collision precondition holds at integration time. (The slug `ls_update_column` is correctly NOT used for this leaf — it is reserved by the L2 entry `:412` + concept `:14` for the distinct still-un-harvested column-streaming step.)
- citecheck `--scan` on the report CYCLE.md: **43 ok, 0 failing (43 citations checked)** — matches the report's self-reported 43/0, the critic's mechanically-verified 43/0 (META.md:36), and the dispatch instruction's expected 43/0 exactly. No MISS / AMBIG / OOB. (DRIFT is anchor-level, not surfaced by `--scan`; the critic already ran `--anchor` pinpoint spot-checks on all 15 Palace citations upstream — all zero-drift; the off-page `trsv` cite drift was the repaired warning, re-pointed to `concepts/givens.md:29` which now resolves in-bounds.)
- The `new:back_solve.md` body uses 4-space-indented code blocks (Signature `:127-130`, the back-substitution L0 loop `:185-191`/`:425-426`, the §L1-vs-L0 GMRES loop) — NO nested triple-backtick fences — so no nested-fence truncation hazard; the full firm body (Signature, Semantics, six holding laws + four explicit non-laws, Dependencies, Variant-axes, Status, Evidence) landed intact inside the `new:` fence.
- Re-read all three target files from disk before editing. D1/D2/D3 (abstractor-normalize-rotation, lifter-hygiene, lowering-verifier-audit) did NOT touch `L1/back_solve.md` (new), `L1/index.md`, or `SUMMARY.md` — the two `edit:` anchors in `L1/index.md` (dep-map row at :93, cohort bullet at :52) and the SUMMARY insert anchor (:84) were exact-byte matches against the current on-disk state.
- **L1 firm count 20→21 motif NOT edited** (per report scope + dispatch instruction): `L1/index.md` §Vocabulary-cohort `**Firm (20)**` header (was line 31) is unchanged; the report deliberately emits only the dep-map row + cohort bullet, deferring the count-motif bump to layer-intro-author / finalize. Did NOT invent a count edit. **For finalize / layer-intro:** bump `**Firm (20)**` → `**Firm (21)**` (and the cohort lead-sentence enumeration of firm motifs if it individually lists the 21st).
- **Carry-forward for the c028 planner (per dispatch instruction):** cycle-027 dispatch-5 (`incremental-least-squares-composition-lowering` L2>L1 theme) returned `needs-revision` and is DEFERRED to batch-8/c028 — its terminal-back-solve references must re-anchor to this now-firm `back_solve` leaf (a c028 lifter promotion task, also gated on the still-un-harvested column-streaming `ls_update_column` leaf). Captured as the NEW OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`.
- deferred integrated_at to finalize per role-spec (the consumed report's `integrated_at:` / `integration_commit:` frontmatter is finalize-only authority; not touched here).

---

## 2026-05-29T175529Z-lifter-ksp-solve-materialise-iterate-cite-tightening
applied_at: 2026-05-29T20:55:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/ksp_solve.md (edit ×2 — Edit-1 §Dependencies `:123`: plain-text `incremental-least-squares` → live link `[`incremental-least-squares`](./incremental-least-squares.md)`, "queued"→"firm", correction-shape `K.y`→`V·y` / `Z·y`; Edit-2 §Semantics phase-3 `:83`: added live-link cross-reference resolving the `K.V · K.y` correction story to the firm operator's `back_solve` output)
- scaffolding/open-questions.md (append ×2 — clause-scoped RESOLVED/ENACTED disposition on `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening` + NEW c028 follow-up OQ `l2-incremental-least-squares-self-description-still-says-queued-after-firming`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate to finalize per role-spec — this is dispatch 6 of the cycle [the 5th and final ready per-report row; D5 deferred]; finalize sees the full staging log)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0 (no forward-edge — both ends are firm same-layer L2 entries; the cross-reference is consumer→producer, not a lowering edge)
- edge-label / prose mismatch: 0 (no L_{n+1}→L_n edge label — same-layer L2 consumer→producer link)
- H1 reuses page heading: 0 (no new file)
- append on missing slug: 0 (target `incremental-least-squares.md` on-disk firm; live link resolves)
- variant-axis missing on multi-variant operator: 0 (no variant-axis change — §Dependencies parenthetical broadens "GMRES" → "GMRES/FGMRES" running-QR, alignment with the file's existing solver-method axis, no hidden new branch)
- bookkeeping incomplete: 0
- citecheck bounds + path-hygiene lint: 0 (scan clean — see Notes)
- SUMMARY.md chapter registration auto-fix: 0 (no new files created)
- index-placeholder displacement auto-fix: 0 (no index rows touched)
- implied-component stub materialization: 0 (pure cite/cross-ref upgrade; target on-disk firm, NO forward-reference to materialize — the upgrade resolves an existing plain-text ref to a live link)

Open questions promoted:
- l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening (disposed RESOLVED — ENACTED; the gated cite-tightening is applied at both `:83` and `:123`; clause-scoped append per append-only convention, prior `:618`/`:910`/`:914` `status:` lines not struck)
- l2-incremental-least-squares-self-description-still-says-queued-after-firming (NEW — opened for the c028 producer-side symmetric staleness: `incremental-least-squares.md:13` still self-describes as "queued ... motif" despite `status: firm`; the dispatch-6 critic/repairer drive-by flag, confirmed at integration)

Build-relevant: yes

Notes:
- **`overall_status: ready` confirmed** (META.md:25). Both surgical `[old]`/`[new]` edits applied verbatim, single-occurrence each.
- Re-read `book/src/L2/ksp_solve.md` from disk before editing. D1 (abstractor-normalize-rotation), D2 (lifter-hygiene), D3 (lowering-verifier-audit), D4 (harvester-ls-update-column / `back_solve`) did NOT touch `book/src/L2/ksp_solve.md` — the two `[old]` anchors (§Dependencies line 123, §Semantics phase-3 line 83) were exact-byte matches against the current on-disk state.
- **Live-link target verified on-disk + firm:** `book/src/L2/incremental-least-squares.md` exists (33280 bytes), H1 `# incremental-least-squares` (line 1), §Status `firm` (line 378: ``firm` — the composition is a `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline…`). The relative link `./incremental-least-squares.md` resolves under linkcheck2.
- citecheck `--scan` on the report CYCLE.md: **4 ok, 0 failing (4 citations checked)** — matches the report's self-reported 4/0, the critic's mechanically-verified 4/0 (META.md §critique citation-validity), and the dispatch instruction's expected 4/0 exactly. No MISS / AMBIG / OOB. (The two `[new]` edits add only book-internal relative links — no new `path:lo-hi` pinpoint, so no `--anchor` run applies, per the report's §Discipline-notes. DRIFT is anchor-level, not surfaced by `--scan`.)
- **Producer-side symmetric staleness surfaced as NEW OQ (per dispatch instruction + critic note 3 / repairer §Surfaced open question):** the firm target `incremental-least-squares.md:13` still self-describes as "the queued second **named-composition** motif" — confirmed stale at integration (the entry is `status: firm` since cycle-026). Editing the producer entry is outside this report's one-operator scope (touches only `ksp_solve.md`) + out of per-report write-authority; opened as `l2-incremental-least-squares-self-description-still-says-queued-after-firming` for a c028 lifter follow-up (plan candidate `l2-incremental-least-squares-drop-queued-self-description`, low fan-out).
- deferred integrated_at to finalize per role-spec (the consumed report's `integrated_at:` / `integration_commit:` frontmatter is finalize-only authority; not touched here).
- For finalize: this is the **5th and final cycle-027 per-report row** (D1 abstractor-normalize-rotation, D2 lifter-hygiene, D3 lowering-verifier-audit, D4 harvester-`back_solve`, D6 this lifter cite-tightening). **D5 (`incremental-least-squares-composition-lowering` L2>L1 theme) returned `needs-revision` and is DEFERRED to batch-8/c028** — NOT integrated; see the carry-forward OQ `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` (D4 row above). Build-relevant: yes (the two `ksp_solve.md` edits touch `book/src/*.md`), so the rebuild re-renders the L2 ksp_solve chapter with the two new live links.

---
