---
verifies: ./CYCLE.md
critiqued_at: 2026-06-07T212600Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T213200Z
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

# META: verification of "L4 index — `sharding-decompose-reduce` roadmap_goal dep-map row"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim carries a verifiable pointer and every one checked out on disk. The precedent `mk_matrix_free_operator` rank-0 row is at `book/src/L4/index.md:119` exactly as cited (confirmed: rank-0 row, `Reference (free, navigational — NOT rank-constrained)` deps cell, `lowers-to` via a `reference`-class relationship, status cell `roadmap_goal (rank 0; …)` closing with "Rank-0 nodes do not bump the firm count"). The new chapter's frontmatter (`rank: roadmap_goal` / `status: roadmap_goal` / `edges.reference: [domain_energy_reduce, inner_product, linear_combination, gram_reduce, L2/gram]`, `sharding-decompose-reduce.md:4-12`), its signature `subdomain_reduce :: (Tensor[(Sb: ...)] -> r) -> Partition -> Tensor[(S: ...)] -> r` (`:48-54`), the `mconcat ∘ map …` framing (`:57`), and the `reference`-only / no-`depends-on` / `rank_violations=0`-preserved reasoning (`:227-231`) all match the report's transcription. SUMMARY placement `nrm2 → sharding-decompose-reduce → sparameter_reduce` confirmed at `SUMMARY.md:81-83`. The index-row signature cell matches the owning chapter's signature verbatim.

**surface-or-evidence — pass (mostly N/A).** Not a refinement-shaped proposal: this is a navigational/index touch (a dep-map row mirroring an already-landed chapter), making no new operator/theme algebraic claim and modifying no operator surface, so the refinement surface-or-evidence machinery no-ops. The record-definition sub-check also no-ops: the signature names `Partition`, `IndexBlock`, and the shape-group families `(S: ...)`/`(Sb: ...)`, but these are defined in the owning chapter `sharding-decompose-reduce.md` (the index row is a navigational mirror, not the definition home), and the chapter is a claim-free `roadmap_goal` that explicitly flags its forms as speculative target-shape. No undefined-record gap introduced by this index row.

**rotation-quality — pass (N/A).** A navigational dep-map row asserts no algebraic/structural rotation of its own. The chapter it indexes is a `roadmap_goal` (rank 0) which, like a `stub`, makes no resolution claim — the rotation check no-ops for both. Marked pass, not applicable to a navigational/roadmap_goal index touch.

**variant-axis-coverage — pass (N/A).** No variant axes are introduced or scoped by a navigational index row; any axes live in the owning chapter. Not applicable to this report kind.

**cross-reference-integrity — FAIL.** All five `reference` targets in the new row resolve on disk (`L4/domain_energy_reduce.md`, `L4/inner_product.md`, `L4/linear_combination.md`, `L4/gram_reduce.md`, `L2/gram.md` — all present), the down-links and the chapter self-link resolve, and the edit anchors (`nrm2` row at `index.md:120`, start of `sparameter_reduce` row at `index.md:121`) are each unique. BUT the proposed new row's **signature cell contains an unescaped, table-breaking `|`**: the body `\`subdomain_reduce reduce P field = mconcat [reduce (restrict_to_block b field) | b <- blocks P]\`` carries the Haskell list-comprehension pipe `|` *inside* an inline code span, written **bare**. In GFM / pulldown-cmark (mdBook's parser) a `|` inside a code span within a table cell is STILL parsed as a column delimiter unless escaped `\|` — the backtick protection does not extend across table-cell pipe-splitting. Mechanically confirmed: the proposed row splits into **7** pipe-delimited cells vs. the table's 6-column shape (`mk_matrix_free_operator` precedent row = 6 pipes; this row = 7), the spurious break falling between `…(restrict_to_block b field) ` and ` b <- blocks P]`. This will render a malformed/misaligned row (extra column) and is a build-readiness defect. The repo's own convention is unambiguous and already in this same file: `index.md:130` (`EigStatus = Converged \| PartialConverged Int \| MaxIterReached \| LinearSolveFailed`) and `index.md:135` (`Outcome = Continue \| Done Bool`) escape every in-code-span table-cell pipe as `\|`. The new row must do the same: `mconcat [reduce (restrict_to_block b field) \| b <- blocks P]`.

**edge-label-fidelity — pass.** The row's "Lowers-to" cell discusses the reduction case lowering to the firm reduce verbs' existing L3 forms by the standing homomorphism — consistent with the chapter and with the row's own framing; no mismatched edge label.

**plan-kind-consistency — pass.** Declared kind is a navigational-index touch landing a `roadmap_goal` row; content shape matches — claim-free, `reference`-class-only, status cell `roadmap_goal (rank 0; …)`, no `depends-on` edge, no firm-count bump. The status token correctly reflects rank 0 and the row introduces no rank constraint. Verified `rank_violations=0` holds at the current baseline (`tools/graded-stack-lint/graded_stack_lint.py` → "RESULT: 0 rank violation(s)"), and since the index page is a `kind: navigational-container (layer index)` (`index.md:2-10`, `reference`-edges-only, no `rank:`) the row adds no `depends-on` edge — the dispatch's invariant (a) holds.

**skill-uptake-survey — pass.** No skill is specifically implied by a one-row navigational index touch; nothing to flag. Telemetry note only.

### Issues found

1. **`cross-reference-integrity` / build-readiness — FAIL — unescaped table-cell pipe in the proposed new row.** `reports/2026-06-07T210728Z-layer-intro-author-l4-index-sharding-row/CYCLE.md` §Proposed changes, the `[new]` block, the `sharding-decompose-reduce` row (CYCLE.md:26), signature cell: the inline code span `\`subdomain_reduce reduce P field = mconcat [reduce (restrict_to_block b field) | b <- blocks P]\`` contains a bare `|` (the list-comprehension generator bar). In GFM table parsing this is read as a column delimiter, splitting the row into 7 cells against the table's 6-column shape and producing a malformed render. Fix: escape as `\|` (matching the established same-file convention at `index.md:130` and `index.md:135`), i.e. `… [reduce (restrict_to_block b field) \| b <- blocks P]`. Severity: high (breaks the table render / build-readiness); surgical (single-character escape). Note for the repairer: the SAME bare-pipe code span also appears earlier in the row's prose framing — `\`subdomain_reduce = mconcat ∘ map (reduce ∘ restrict_to_block) ∘ blocks\`` uses `∘` (no pipe, fine), so only the list-comprehension occurrence needs escaping; scan the full cell for any other `|` inside backticks before applying.

### Confirmations (dispatch-requested checks that PASSED)

- (a) **No `depends-on` edge added.** The row lists firm reduce roots under `Reference (free, navigational — NOT rank-constrained)` only; the index page is a navigational container with `reference`-edges-only and no `rank:`. `rank_violations=0` confirmed via `graded-stack-lint` (RESULT: 0 rank violations). ✓
- (b) **Precedent `mk_matrix_free_operator` at `index.md:119` exists**, is a rank-0 `roadmap_goal` row, and the new row matches its format (5-column shape, `Reference (free, navigational — NOT rank-constrained)` deps cell, `reference`-class lowers-to, status cell `roadmap_goal (rank 0; …)` closing "Rank-0 nodes do not bump the firm count"). ✓
- (c) **Alpha-position correct**: `nr` < `sh` < `sp`; SUMMARY agrees at `SUMMARY.md:81-83`; edit inserts between `index.md:120` (`nrm2`) and `index.md:121` (`sparameter_reduce`). ✓
- (d) **No KaTeX `$`-sigil leak**: scanned the proposed row — no bare `$`; signatures/math are in inline code spans / Unicode (`∘`, `++`, `⊑`). ✓
- (e) **Status cell correctly reflects `roadmap_goal` (rank 0)** and does NOT bump any firm count (the cell states so explicitly; the §Vocabulary-cohort "Firm at L4" prose tally is untouched). ✓

## Repair

### Fixes attempted

- **Finding**: `cross-reference-integrity` / build-readiness FAIL — the proposed new `sharding-decompose-reduce` row's signature cell carries a bare, unescaped list-comprehension pipe `|` inside an inline code span (`mconcat [reduce (restrict_to_block b field) | b <- blocks P]`). GFM/pulldown-cmark splits the row into 7 cells vs the table's 6-column shape; backtick protection does not cross table-cell pipe-splitting → malformed render / build defect.
  - **Decision**: repaired
  - **Action**: escaped the in-code-span pipe to `\|` in `CYCLE.md:26`, the `[new]` proposed-changes block for `edit:book/src/L4/index.md` → `mconcat [reduce (restrict_to_block b field) \| b <- blocks P]`. This matches the established same-file convention (`index.md:130`, `index.md:135`). Scanned the full cell: the other in-backtick framing span uses `∘` (no pipe), and `++` / `⊑` carry no pipe — the list-comprehension bar was the sole occurrence, so no other escapes were needed. Single-character mechanical fix; no content change.

### Unrepairable findings

None. The sole fail was a surgical single-character escape, fully within repair authority (in-code-span table-cell pipe escape, an established same-file convention). All other checks passed at critique.

## Suggested resolution

`ready` — the one fail finding is repaired (table-cell pipe escaped to `\|`, matching `index.md:130`/`:135`); all other 7 checks passed at critique. Integrator note: this is a navigational/index-only touch (one `roadmap_goal` dep-map row mirroring the c134-landed `sharding-decompose-reduce.md`), introduces no `depends-on` edge, and preserves `rank_violations=0`. Worth a quick `cargo make book` confirmation that the L4 index table renders with the correct 6-column shape after applying the row.
