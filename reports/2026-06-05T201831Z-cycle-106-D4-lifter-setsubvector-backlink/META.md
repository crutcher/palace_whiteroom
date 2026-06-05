---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T20:55:00Z
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
overall_status: ready
---

# META: verification of "Re-anchor concepts/set_subvector_zero frontmatter (doubly-stale back-link)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim in the report is cited and I confirmed each against on-disk state. (1) "L1/set_subvector_zero landed c104/c105, firm, 24662 bytes": confirmed — `book/src/L1/set_subvector_zero.md` exists at 24662 bytes, `rank: firm`, `operator: set_subvector_zero` (lines 1-4). (2) "concepts/dofset.md already lists concepts/set_subvector_zero": confirmed — `concepts/dofset.md:18` carries `- concepts/set_subvector_zero` in its `reference:` block. (3) The current doubly-stale `reference: []` with the false comment: confirmed at `concepts/set_subvector_zero.md:1-6`. (4) The pre-change linter line `0 rank violation(s), 163 detritus, 77 untyped`: reproduced exactly. All citations point to real, in-range locations; the report cites Palace-source-adjacent book-artifact lines (not C++ pinpoints), so no `citecheck --anchor` C++ line-map adjudication was needed. No `read_range` was used as a source-of-truth anywhere — all verification was direct on-disk `Read`.

**surface-or-evidence — pass.** This is not a refinement-shaped proposal touching operator/theme semantics; it is a pure frontmatter `edges:` de-stale (navigation surface), explicitly scoped as a bounded prose-correction of a factually-false comment, with the page body untouched. The report frames it as evidence-grounded correction (disk state contradicts the old comment), which is the allowed retroactive-evidence/back-link shape. Record-definition sub-check: the page names no new record in a signature requiring a definition home (it is itself a concept/pointer page for an already-defined primitive); no gap.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted — this is a frontmatter link fix. The `L3 lift` / `L3 tensor-field form` prose already in the page is untouched.

**variant-axis-coverage — pass (not applicable).** No orthogonal variant axes are engaged by a frontmatter back-link.

**cross-reference-integrity — pass (load-bearing here, verified).** Both new `reference` targets resolve on-disk: `L1/set_subvector_zero` → `book/src/L1/set_subvector_zero.md` (exists) and `concepts/dofset` → `book/src/concepts/dofset.md` (exists). I independently applied the proposed edit to a scratch copy, re-ran the graded-stack linter, and got `0 rank violations, 164 detritus, 76 untyped` with NO UNRESOLVED edge involving either slug — matching the report's post-change figures exactly, then restored the file (git diff clean). The reciprocal claim is correct: `dofset.md:18` already points to this page, and (a stronger confirmation than the report itself notes) `L1/set_subvector_zero.md:21` ALSO already lists `concepts/set_subvector_zero`, so the L1↔concept edge becomes bidirectional too. The `[old]` block matched the file byte-for-byte (the scratch apply asserted the match), so the integrator's edit will apply cleanly. No firm-body-inside-fence concern (no firm-chapter authoring here).

**edge-label-fidelity — pass.** The edges carry no L_{n+1}→L_n directional label; they are navigational `reference` edges and the prose discusses exactly those edges. The `reference` (not `depends-on`) kind is correct: both are navigational see-also pointers (concept page → its authoritative L1 home; reciprocal record-page link), constraining neither rank nor liveness — the textbook `reference` semantics. Bare-slug form matches the scheme/sibling convention: `concepts/axpy.md` and `concepts/apply_linop.md` both use bare slugs (`L1/axpy`, `concepts/constructed-operators`) in `reference:` block sequences; the report correctly overrode the dispatch prompt's suggested `book/src/...` form per the prompt's own deferral to the on-disk scheme.

**plan-kind-consistency — pass.** Declared as a lifter re-anchor (frontmatter de-stale / back-link). Content shape matches exactly: a single `edit:` block confined to the `edges:` frontmatter, no prose change, no placeholder content. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The report's shape (frontmatter edge resolution + linter self-verification) does not strongly imply a dedicated skill; the lifter performed the natural verification (scratch-apply + linter re-run + restore) inline. No skill omission worth flagging.

### Issues found

None. All claims independently verified on-disk and via the graded-stack linter (pre-change `163/77` and post-change `164/76` both reproduced exactly; both new `reference` slugs resolve; no rank violation introduced; `[old]` block matches the file). The report's caveat is accurate and appropriately scoped: a `reference` edge does NOT create reachability (reachability is computed over `depends-on`), so this fix correctly does not claim to rescue the `set_subvector_zero` / `L1/set_subvector_zero` / `dofset` cluster from detritus — it honestly routes that higher-fan-out reachability question to a separate item rather than silently assuming it closed. The `+1 detritus` is correctly explained as the now-typed (formerly edgeless/skipped) page joining the counted-detritus set, not a node becoming newly unreachable. The report's own self-correction note (the earlier "163 unchanged" draft figure was wrong; measured is 164) is honest and the measured figure is the one I reproduced.

All 8 checks pass — clean report; `overall_status: ready` set per the batch-23 all-pass convention (no repairer will run).
