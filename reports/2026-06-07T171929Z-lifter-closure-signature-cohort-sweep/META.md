---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T180000Z
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

# META: verification of "Re-anchor closure-signature non-compliant cohort to §1.3.1 + 2 stale-token fixes"

## Critique

### Checks run

**citation-validity — pass.** Every edit's `[old]` string was verified to exist verbatim AND uniquely on disk (multi-line blocks confirmed via `perl -0777` literal-block match; inline-backtick forms via `grep -c`). The two distinct old-strings flagged for collision risk — `assemble_frequency_operator.md:99` (the two-line code block `assemble_frequency_operator\n      :: ... -> LinearOperator[N, N]`) vs `:293` (the inline-backtick `\`assemble_frequency_operator :: ... -> LinearOperator[N, N]\`,` with trailing comma) — are each unique literal matches (1 each); the integrator will NOT mis-apply. The 2 stale-token grounds are accurate: `mk_matrix_free_operator.md` carries `status: firm` / `rank: firm` (on lines :5-6, report's verification note says ":4-5" — a benign ±1 prose-pointer drift in a non-claim-backing verification note, no impact), and `boundary-mode.L4.md` carries `rank: firm` (on :6, report says ":5" — same benign ±1). `citecheck --scan` reports 3 `[AMBIG]` results (`assemble_frequency_operator.md:103-105`, `fe_assemble.md:71`, `fe_assemble.md:77`) — these are bare-basename collision-hygiene nits on the report's prose *discussion* references (the `L4/` vs `L1/` basenames collide); they are NOT bounds drift, and all edit-blocks themselves use full `book/src/L4/...` paths and are unambiguous in context. Sub-warning observation only.

**surface-or-evidence — pass.** This is a pure-rewrite notation-fidelity sweep + two maturity-token corrections, not a new rotation/refinement claim — so the "surface + rotation_claim OR retroactive-evidence" gate is satisfied trivially (it modifies surface text; the supporting evidence is the on-disk frontmatter of the described nodes + the §1.2.2/§1.3.1 sanction, all cited). Record-definition sub-check: no NEW record is named; the records appearing in the re-spelled signatures (`FrequencyOperatorFamily[N]`, `WeakFormTerm`, `DofSet[N]`) are pre-existing with definition homes (in-chapter §Signature record block / firm L1 chapter / OQ-routed concept home), merely carried through with the codomain re-spelled. No gap.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted. Every edit is a notation conformance with identical semantics (the operator-value codomain meaning is unchanged; no signature SHAPE changed, no LHS/RHS shifted, no decomposition altered) — the report states this explicitly and correctly.

**variant-axis-coverage — pass.** The one in-play scope axis — closure-signature (§1.3.1) compliance cohort vs the plain operator-VALUE flat-vector (§1.2.2) rendering cohort — is explicitly enumerated and bounded: the closure-returning / high-order codomains are swept; the plain `K/C/M : LinearOperator[N, N]` record fields (`assemble_frequency_operator.md:103-105`), the plain result-lines (`:121`/`:137`), and `fe_assemble.md:77` (`result — LinearOperator[N, N]`) are deliberately left, routed to the META-owned `closure-signature-l4-constructor-restatement-compliance-cohort-sweep` OQ. No hidden branch.

**cross-reference-integrity — pass.** Verified against on-disk state: `eliminate_bc.md:83-84` is already the bracketed compliant `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]` and is NOT edited (read-only consult, confirmed). The `L4/index.md` TABLE rows `:110` / `:114` / `:115` are already bracketed `LinOp[(S: ...), $S]` and are NOT in the edit set (confirmed by reading them); `:119` (`mk_matrix_free_operator`, already bracketed `Op[Tensor[(N: ...)] → ...]`) is likewise untouched. Only the OPAQUE narrative rows `:61` / `:62` are moved — D1's "eliminate_bc is OUT" ruling is respected (only the opaque narrative side moves to agree with the canonical bracketed chapter/TABLE form). The new `LinOp[...]` spellings are correct per `semantics/index.md:88-95` (§1.2.2): `LinOp[(N: ...), $N]` is the valid square/endomorphic calculus rendering (binds one group, uses it for range) of the opaque `LinearOperator[N, N]`, axis `N` preserved; and the index `:61` new form `LinOp[(S: ...), $S] -> LinOp[$S, $S]` matches `eliminate_bc.md:84` exactly (input binds `S`, result back-references `$S`). All edited rows keep their existing `[link]` targets unchanged.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is asserted or changed. The `fe_assemble.md` frontmatter `constructs-via` edge stays `reference`-class (`kind: constructs-via`); only its inline-comment stale `roadmap_goal` wording is corrected to `firm (c127)` — the edge class/structure is unchanged, confirmed by reading the old-string (the `kind: constructs-via` line is untouched; only the trailing comment prose differs).

**plan-kind-consistency — pass.** The declared kind (lifter pure-rewrite fidelity sweep + 2 bounded evidenced maturity-token corrections, NO frontmatter status/rank/edge change) matches the content shape exactly: all edits are prose/signature-text re-spellings or maturity-token corrections backed by on-disk frontmatter, no DAG-node rank moves, consistent with the planner's "NO RE fires" note.

**skill-uptake-survey — pass.** No skill is implied beyond the §1.2.2/§1.3.1 conformance the report already performs by hand; the USE+LINK-to-semantics discipline is honored (no convention RE-statement added). No telemetry gap.

### Issues found

No warning- or fail-level issues. Two sub-threshold observations recorded for telemetry only (neither blocks):

1. **(info) `citecheck --scan` `[AMBIG]` basename-collision nits** — three prose-discussion references (`assemble_frequency_operator.md:103-105`, `fe_assemble.md:71`, `fe_assemble.md:77`, in CYCLE.md §Bounded-scope / §Open-questions) use a bare basename that collides between `book/src/L4/` and `book/src/L1/`. These are out-of-scope *discussion* pointers, not edit-block paths or new L0 claims, and are unambiguous in context (the report is plainly discussing the L4 chapters). The edit-blocks themselves all use full `book/src/L4/...` paths. No bounds drift; not a citation-validity defect.

2. **(info) ±1 verification-note pointers** — the report's on-disk verification notes cite `mk_matrix_free_operator.md:4-5` (actual `status: firm`/`rank: firm` on :5-6) and `boundary-mode.L4.md:5` (actual `rank: firm` on :6). These are descriptive verification notes, not claim-backing citations, and the underlying facts (both nodes genuinely `firm` on disk) are correct — so the stale-token corrections themselves are accurate. Off-by-one in the note text only.

**Dual-spelling scope-boundary assessment (per the dispatch's explicit ask): SOUND, not incoherent.** After the sweep, both target chapters carry a deliberate MIX — high-order/closure codomains in the `LinOp[(N: ...), $N]` calculus form, plain operator-VALUE record fields still in the rank-1 `LinearOperator[N, N]` form. This is a coherent scope boundary, not a half-finished edit: (a) the boundary tracks a real semantic distinction D1 pinned — the §1.3.1 closure-signature *compliance* question (high-order codomains hide their in/out arrow → re-spell) is genuinely separable from the §1.2.2 flat-vector→calculus *rendering* question (whether all operator-value spellings should additionally move to bracketed form); (b) the boundary is explicitly flagged to the META-owned `closure-signature-l4-constructor-restatement-compliance-cohort-sweep` OQ as the resolution home; (c) the mix is internally well-typed — both forms denote the same square operator on axis `N`, and §1.2.2 sanctions keeping the rank-1 form where it is faithful. A reader will notice the dual-spelling (the report says so), but it is a legible deferred-cohort boundary, not a contradiction. The chapter does not become incoherent.
