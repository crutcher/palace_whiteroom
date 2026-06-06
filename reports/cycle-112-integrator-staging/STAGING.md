# cycle-112 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative
apply-order record (NOT the `applied_at` timestamps). integrator-finalize reconciles from this log.

---

## 2026-06-06T165604Z-layer-intro-author-L3-orthogonalize-nrm2-typing
applied_at: 2026-06-06T171234Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/orthogonalize.md (frontmatter migrate: legacy layer/firmness/lifts_from/lowers_to → `rank: partial-obstruction` + `obstruction_resolution: firm` + typed `edges:` block; `variant_axes:` 3 entries preserved verbatim)
- book/src/L3/nrm2.md (frontmatter migrate: legacy layer/firmness/lowers_to/lifts_from → `rank: firm` + typed `edges:` block; `variant_axes:` 1 entry preserved verbatim)

Gate hits:
- rank-well-foundedness: 0 (linter `rank_violations` HELD 0; orthog=partial-obstruction deps L2/orthogonalize firm + L3/dot firm + L3/axpy typed-no-rank(vacuous) + L3-L2/orthogonalize-variant-split untyped(vacuous); nrm2=firm deps L1/nrm2 firm + L2/nrm2 firm + L3/dot firm — firm-rests-on-firm holds)
- edge-label/prose-mismatch: 0 (kind: tokens lowers-to/composes faithful; critic's edge-label-fidelity warning was a mis-stated-PRECEDENT-in-rationale, repaired pre-integration, edges themselves sound)
- YAML round-trip: 0 (both files parse via yaml.safe_load; rank token + edges depends-on/reference keys + variant_axes all present)
- SUMMARY-registration: 0 (both chapters pre-exist + are registered; frontmatter-only, no new slug, no SUMMARY edit needed)
- forward-edge-without-surface: 0 (all 16 edge targets verified on-disk by critic; cross-reference-integrity pass)
- citecheck (bounds): 0 failing — `--scan` reports "no citations found" (frontmatter-only typing dispatch; report cites book-relative chapter prose lines, not reference/ source ranges). No MISS/AMBIG/OOB.

Open questions promoted:
- re2-shadows-orthogonalize-variant-split-theme
- lazy-tail-untyped-no-decrement-for-legacy-edged-files
- obstruction-resolution-firm-linter-keying-untested

Build-relevant: yes (touches book/src/L3/*.md — but frontmatter-only; mdBook renders body unchanged. finalize: rebuild to confirm no breakage)

Notes: D1 LEAD of batch-36 graded-stack lazy-tail typing. Graded-stack linter on the landed-so-far
tree (this report's 2 files applied onto clean baseline): files=355, typed=295, untyped=60 (HELD,
per F1), reachable=123 (baseline 122 → +1), rank_violations=0 (HELD), detritus=136 (baseline 137 → −1),
partial-obstruction histogram 3→4. The +1 reachable / −1 detritus is the FAITHFUL `L2/nrm2` ground
(D1 Finding F2: the genuine adjacent-layer `L3/nrm2 → L2/nrm2` lowers-to depends-on edge from
already-reachable `L3/nrm2` grounds the previously-unreachable `L2/nrm2`; RE5 transitive-grounding
mechanism, NOT a manufactured flip). `L3/orthogonalize` HELD GARBAGE (RE2 honored — only outbound
edges authored, no forced inbound depender; verified [GARBAGE*] in linter output). The
`L3/orthogonalize → L3-L2/orthogonalize-variant-split` rescue edge is structurally-correct-but-latent
(F3): rides RE2, rescued only when a faithful reachable L3-iteration-view consumer lands → OQ
`re2-shadows-orthogonalize-variant-split-theme`. Deferred integrated_at to finalize per role-spec.
First per-report integrator in cycle-112 (created this STAGING.md). No sibling landings observed on
disk this invocation.

---
## 2026-06-06T165604Z-layer-intro-author-L3-scal-linear-combination-typing
applied_at: 2026-06-06T172730Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/scal.md (frontmatter migrate: legacy firmness/lowers_to/lifts_from → `rank: firm` + typed `edges:` block [depends-on: L2/linear_combination; reference: L3/linear_combination, L1/scal, L2-L1/linear-combination-fold-specialization]; `variant_axes:` 2 entries preserved verbatim)
- book/src/L3/linear_combination.md (frontmatter migrate: legacy firmness/lowers_to/lifts_from → `rank: firm` + typed `edges:` block [depends-on: L2/linear_combination; reference: L4/linear_combination, L2-L1/linear-combination-fold-specialization]; `variant_axes:` 5 entries preserved verbatim)

Gate hits:
- rank-well-foundedness: 0 (both `rank: firm` rest on `L2/linear_combination` which is `rank: firm` on-disk — firm-rests-on-firm holds; linter `rank_violations` HELD 0)
- edge-label/prose-mismatch: 0 (bare-slug surface form mirrors typed sibling `L3/dot`; depends-on = the adjacent L2 op, reference = up-edges + non-adjacent L1 identity + lowering theme; faithful per producer's per-file edge derivation, critic edge-label-fidelity PASS)
- YAML round-trip: 0 (both parse via yaml.safe_load; rank token + edges.depends-on/reference + variant_axes all present and correct)
- SUMMARY-registration: 0 (both chapters pre-exist + are registered; frontmatter-only, no new slug, no SUMMARY edit needed)
- forward-edge-without-surface: 0 (all edge targets resolve: L2/linear_combination, L3/linear_combination, L1/scal, L4/linear_combination, L2-L1/linear-combination-fold-specialization all on-disk; linter unresolved_depends_on_targets HELD 0)
- citecheck (bounds): AMBIG/MISS hits are book-relative chapter-prose pointers (scal.md:16, linear_combination.md:152, etc.) + a linter tool-source pointer (graded_stack_lint.py:518-547) — NOT reference/ source-range claim citations. Same class as D1's frontmatter-only-typing-dispatch note. Advisory, NOT a citation defect in the landed artifact; non-blocking.

Open questions promoted:
- L3-scal-reachable-via-normalize-grounding
- linter-legacy-shim-line-citation-527-532-not-546-547

Build-relevant: yes (touches book/src/L3/*.md — frontmatter-only; mdBook renders body unchanged. finalize: rebuild to confirm no breakage)

Notes: D2 of batch-36, extends the LEAD. FRONTMATTER-ONLY. ZERO standalone delta exactly as the
producer predicted: these two files already carried legacy `lowers_to`/`lifts_from` and were thus
shim-counted as typed before the edit, so `untyped` HOLDS (not 60→58) — a representation upgrade
(legacy fields → canonical `edges:` + explicit `rank:` token), not a typed-count change. Graded-stack
linter on the CUMULATIVE landed tree (D1's 2 files + D2's 2 files, all applied): files=355, typed=295,
untyped=60 (HELD), roots=36, reachable=123 (= D1's cumulative figure; D2 adds +0), rank_violations=0
(HELD), unresolved_depends_on_targets=0 (HELD), detritus=136. L3/scal verified NOT in untyped + still
in detritus [GARBAGE*] (GROUND-candidate per OQ L3-scal-reachable-via-normalize-grounding — NOT
force-flipped); L3/linear_combination verified reachable (via L4/linear_combination). On-disk state I
directly observed this invocation: both files were at baseline legacy frontmatter before my edits
(matched the report's [old] blocks exactly), and D1's staging row + D1's reachable=123 are reflected in
the cumulative linter run above (the 123 figure already includes D1's L2/nrm2 ground). Deferred
integrated_at to finalize per role-spec.

---
