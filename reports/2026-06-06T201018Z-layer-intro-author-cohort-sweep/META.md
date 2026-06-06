---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T203413Z
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

# META: verification of the named-shape-groups restatement-cohort relocation sweep (cycle-116 D2)

## Critique

### Checks run

**citation-validity** — pass. This is a relocation/consolidation sweep that makes no new
claims; the only "citations" it carries are the §1.2.1 / §1.2.2 / §4.1 back-links to the moved
surface and the rewritten `index.md:NNN` strawman line-refs. I verified the surface sections
the report claims as the relocation home all exist at the cited lines in
`book/src/semantics/index.md`: §0.1 Active-management discipline (`:24`), §1.2.1 Named shape
groups (`:73`), §1.2.2 (`:87`), §4.1 Shape contracts on primitives (`:297`/`:314`, carrying the
authoritative "a named group is the rank-agnostic same-shape contract; a bare concrete axis
`Tensor[N]` is **not** — it is a rank-1 commitment" sentence). The L4 strawman line-refs
rewritten from `l4_calculus.md:NNN` → `index.md:NNN` are a verbatim 1:1 filename substitution on
content D1 moved unchanged; I confirmed e.g. `index.md:418` resolves to the `run_lbm` bounded-loop
region (`book/src/semantics/index.md:416-420`) that the chebyshev §6.5-step-5 ref relies on.

**surface-or-evidence** — pass. Not a refinement-shaped per-operator proposal; it is the canonical
**pure consolidation / relocation** disposition under the SEMANTIC-CONSOLIDATION directive
(USE+LINK-don't-restate). The "evidence" is the surface home + the resolving back-links, which I
verified present. No record-definition obligation is triggered (no new signature-named record).

**rotation-quality** — pass (not applicable). The sweep asserts no algebraic/structural rotation;
it relocates general teaching out of functional-unit entries. No rotation claim to grade.

**variant-axis-coverage** — pass (not applicable). No operator variant axes are in scope; this is
prose-trim only, frontmatter (`edges:`/`rank:`) untouched.

**cross-reference-integrity** — pass, and load-bearing for this sweep. The sweep's whole value is
that the trimmed entries still resolve to the surface home. I re-ran `cargo make book` → **EXIT 0**
("Build Done in 94.66 seconds"); linkcheck2 0.12.0 ran with no broken-link/does-not-exist errors
(those are hard non-zero-exit failures). I independently confirmed both gates: `grep -rn
'l4_calculus\.md' book/src` → 0; `grep -rln 'NOT rank-1\|not rank-1\|carries the same-shape
contract\|accidentally read as' book/src` → 0. The 56 remaining `l4_calculus` occurrences are all
the intentional link-TEXT form `[`l4_calculus`](../semantics/index.md)` (a `grep -v` of that exact
form yields zero non-conforming refs) — correct, matching the c115-D3 convention. Every one of the
5 Tier-B and 19 Tier-C files retains ≥1 resolving `semantics/index.md` back-link (verified
per-file), so no entry was left ungrounded.

**edge-label-fidelity** — pass. The relevant fidelity axis here is the semantic-consolidation
discipline: a restatement-at-functional-unit-scope must be resolved by **relocation-to-surface +
back-link**, NOT deletion-without-pointer. I confirmed this is exactly what happened — every
trimmed entry keeps the op's own concise shape fact AND a §1.2.1 back-link. The
`concepts/elementwise-product.md:9` base-primitive line, which previously had no on-line link, was
correctly given one (`see §Contract / [`l4_calculus`](../semantics/index.md) §1.2.1`) rather than
left dangling.

**plan-kind-consistency** — pass. Content shape (mechanical/surgical prose trim, verify-not-redo,
no frontmatter mutation) matches the declared dispatch kind.

**skill-uptake-survey** — pass. No skill is strongly implied for a prose-relocation sweep; the
report's own grep+build gate is the appropriate self-verification. Telemetry only, non-blocking.

### Faithfulness spot-checks (the load-bearing question for this sweep)

I spot-read the actual edited lines across both tiers to confirm the trim removed only the
general "NOT rank-1 / named shape groups per" echo and preserved each op's genuine own shape fact
(no over-trim of a real per-op precondition):

- Tier B: `L2/nrm2.md:77` (operand is one shape group `S` of arbitrary unknown rank + §1.2.1 link),
  `L3/blas1-intro.md:20`, `L2-L1/linear-combination-fold-specialization.md:35` (keeps the
  `all tᵢ : Tensor[(S: ...)]` aligned-pass precondition), `concepts/elementwise-product.md:9,18`
  (keeps congruence + back-link added). All faithful.
- Tier C: `L2/axpy.md:43`, `L2/gram.md:56` (the `, NOT rank-1-pinned —` → ` —` special pattern —
  keeps "shape-generic over a congruent shape group `S`"), `L2/reciprocal.md:38,102`,
  `L2/normalize.md:52`, `L2/inner_product.md:166`, `L2/elementwise_product.md:41,97`,
  `L3/reciprocal.md:21,40`, `L3/elementwise_product.md:41`, `L4/dot.md:56,85`,
  `L4/inner_product.md:20,101`, `L4/nrm2.md:78`, `L4/sparameter_reduce.md:100`. All retain the
  op's "arbitrary, unknown rank" / shape-group-`S` fact; only the general echo removed.

No file lost its §1.2.1 grounding (per-file back-link count verified for all 24 files).

### Issues found

**None.** Both declared gates reproduce cleanly (`l4_calculus.md` prose-ref grep → 0; echo-marker
grep → 0; `cargo make book` → EXIT 0 with no broken-link errors). The trim is faithful across the
Tier-B and Tier-C spot-checks — each entry keeps its own concise shape fact and a resolving
surface back-link; the only general-rule echoes were removed, exactly per the
USE+LINK-don't-restate discipline. The relocation-to-surface (not deletion-without-pointer)
resolution holds. The build warnings surfaced by `cargo make book` (`[k]`, `[j+1]`,
`[0..k, 0..k]` "potential incomplete link" + unclosed-HTML-tag WARNs) are pre-existing, in files
this dispatch did not touch, and non-fatal — correctly characterized in the report.

Note (non-issue, telemetry): the rewritten `index.md:NNN` inline-code line-refs in
`L4/iterate-while.md` / `ksp_solve.md` / `chebyshev.md` / `index.md` are bare-basename citations
(not markdown links, so build-neutral) that carry the same surface-disambiguation reliance as the
old `l4_calculus.md:NNN` form they replaced — they read correctly in context (each section also
names the full `book/src/semantics/index.md` path), so this is a faithful 1:1 substitution, not a
regression. Flagged only as a future-cleanup observation, not a defect of this sweep.

All 8 checks pass; this is a clean report.
