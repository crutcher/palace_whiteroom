---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T00:30:00Z
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

# META: verification of "typed `edges:` for concepts/ cluster A (16 pages)"

## Critique

### Checks run

**citation-validity (pass).** This is a frontmatter-typing pass, so the load-bearing
citations are (a) the scheme-authority pointers and (b) the per-page home/use-site
anchors. Spot-checked the scheme anchors: `graded-stack-scheme.md:244-252` is indeed
the §5 concept-page two-sub-cases passage naming `concepts/dot.md` as a narrative
pointer "outside the subject DAG — no `rank:`"; the self-exclusion banner at `:13-17`
and the `depends-on`/`reference` binary at `:101-115` are in range and support the
claims made. The on-disk precedent at `L1/dot.md:1-9` is verified verbatim — `rank: firm`
with `edges: reference: [L1-L0/dot-mutation-rotation, concepts/dot]`, and `concepts/dot`
is a `reference` back-pointer, NOT a `depends-on`. The L0 prose citations (`iterative.cpp:669-706`,
`orthog.hpp:51-53`) are correctly left as prose, not promoted to edges (L0 ranges are not
book nodes). No claim lacks support.

**surface-or-evidence (pass).** Not a refinement of operator/theme surface text — it adds
`edges:` frontmatter only and mutates no prose, no Semantics/Laws/Signature. No
rotation_claim is needed. The record-definition sub-check is satisfied: the report
correctly determines none of the 16 pages is a record-definition page (the only concept
sub-case that is a DAG node), so no page needs a `rank:` or a record-definition home; this
is exactly the §5 narrative-pointer disposition.

**rotation-quality (pass — not applicable).** No algebraic/structural/reduction rotation is
asserted; a typed-edge frontmatter pass rotates nothing. No-op, as for the stub/feature-surface
kinds.

**variant-axis-coverage (pass — not applicable).** No operator variant axes are in scope; the
pass only types navigational edges. The report does carry one genuine judgment axis
(node-vs-non-node / `reference`-vs-`depends-on`) and resolves it uniformly with a stated
rationale per page, which is the right shape for this kind.

**cross-reference-integrity (pass — LOAD-BEARING for this kind, verified mechanically).**
Every one of the 16 target concept pages exists on disk and its `[old]` H1 anchor matches the
verbatim on-disk line 1 (checked all 16; e.g. `apply_BA` H1 is the long
``# Concept: `apply_BA` (preconditioner-side constructed operator)`` and matches). Every
`reference` edge target resolves: all `L1/{dot,nrm2,scal,axpy,apply_linop,axpby,axpbypcz,elementwise_product}.md`,
`L2/{krylov-step,inner_product,elementwise_product}.md`, `L4/preconditioning-framework.md`, and
all 12 cited `concepts/*` targets EXIST. The three homeless-primitive workarounds are correct:
`L1/trsv.md`, `L1/set_subvector_zero.md`, `L1/gemv_basis.md` are confirmed ABSENT, and the report
correctly does NOT emit edges to them — `trsv`/`set_subvector_zero` carry `reference: []` and
`gemv_basis` points only at the existing `concepts/orthogonalization`. Zero dangling edges. Edge
path style (bare slug, no `.md`) matches the on-disk precedent in `L1/dot.md`.

**edge-label-fidelity (pass).** The `reference`-vs-`depends-on` classification is correct per
the scheme. The scheme (`:97-115`) states `reference` is for "concept-narrative pointers" and
that classification must be deliberate, not defaulted. Verified the load-bearing symmetric-reference
argument against on-disk fact: L1 operator entries that mention their concept page (`L1/dot`,
`L1/apply_linop`) list it under `reference`, never `depends-on` — so a firm operator does not block
on its pointer page, and the concept→L1 down-edge is correctly the symmetric `reference`. The
all-`reference` outcome (zero `depends-on`) is the correct expected outcome for a pure-pointer
cluster, not an omission. The borderline pages (`apply_BA`, `two_operator_split`,
`complex-from-real-lift`, `finest-level-unwrap`) are each judged `reference` with a stated reason
(the genuine `depends-on` lives on the L4/constructed-operator chapter that carries its own typed
edges), which is consistent with the §3 OWN-COMPOSITION / root-edge rule.

**plan-kind-consistency (pass).** Declared kind is a graded-stack P1 typed-edge frontmatter pass.
Confirmed the content matches: every proposed-changes block is a pure `--- ... ---` prepend before
the existing H1; no operator entry is mutated, no prose is touched, no claim is added. The H1 is
reproduced verbatim as `[new]` so the diff is frontmatter-only. Matches the kind exactly.

**skill-uptake-survey (pass — telemetry).** No graded-stack-edge-typing skill exists to invoke; the
report leans directly on `graded-stack-scheme.md` §2/§5 as the authoring contract, which is the
right reference. A reusable "type-concept-page-edges / non-node-pointer-convention" procedure may be
a future skill candidate once D4/D5 settle the node-status convention, but its absence is not
blocking.

### Build-safety (verified)

- All 16 target pages have NO pre-existing frontmatter (line 1 is the H1 in every case), so a
  `--- ... ---` prepend is collision-free.
- Every proposed `edges:` block round-trips through `yaml.safe_load`, including the
  `reference: []` empty-list form and the multi-line trailing-`#`-comment continuations on
  `trsv`/`set_subvector_zero`/`gemv_basis` (the aligned comment lines parse as comments, not as
  malformed keys).
- Edits add/remove no body links, so the `linkcheck2` surface is unchanged. Edge targets are
  frontmatter metadata consumed by the graded-stack linters, not mdBook links, and all resolve.

### Issues found

None blocking. Two observations recorded as telemetry (not defects, and explicitly already
flagged by the report itself):

1. **Scheme item-4 tension (acknowledged, not a defect).** `graded-stack-scheme.md:267` (checklist
   item 4) says a narrative-concept page carries "**no** `rank:`/`edges:`", whereas the report
   emits `reference`-only `edges:` blocks. The report surfaces this exact tension in its
   Node-status convention section and in OQ `graded-stack-index-and-concept-node-status`, choosing
   the informative `reference`-only encoding over empty while noting the blocks are trivially
   droppable if the batch-close meta-phase prefers the strict zero-frontmatter reading. Because the
   blocks assert no `depends-on` (no rank/liveness claim), neither linter is misled under either
   reading, so this is a deferred convention choice, not an integrity defect. Routed correctly to the
   D4/D5 batch-close OQ.

2. **Latent coverage gap (correctly routed, out of this pass's scope).** `trsv`,
   `set_subvector_zero`, `gemv_basis` are real BLAS/vector primitives with no `L1/<name>.md` home.
   The report does not paper over this with a dangling edge — it flags
   `concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis` as an OQ for a harvester
   pass. This is the right disposition (a coverage finding, not a typing defect); concept pages are
   read-only toward their would-be homes in this pass.
