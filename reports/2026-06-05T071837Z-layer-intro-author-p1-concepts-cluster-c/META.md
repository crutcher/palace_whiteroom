---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T000000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: warning
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T073500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of concepts/ cluster C typed-edge frontmatter (12 pages)

## Critique

### Checks run

**citation-validity (pass).** This is a typed-edge frontmatter dispatch, not a claim-bearing
authoring pass: each proposed change prepends an `edges:` YAML block and re-emits the existing
`# Title` line — it asserts no new algebraic/structural claim that would need a source pinpoint.
The load-bearing "citations" here are the edge targets and the two flagged body-citation
characterizations. I confirmed the givens_* body citations the report describes are exactly as
characterized: `givens_apply.md:23` carries `palace/linalg/gmres.cpp:ApplyPlaneRotation` and
`givens_generate.md:23` carries `:GeneratePlaneRotation`, both bare-file `reference/palace/...`
pointers with no line range — correctly read as L0 body source-pointers inside the page, not
book-DAG edges. No `verified_against:` block is emitted, so that sub-check no-ops. All three
sampled `edges:` blocks (gmres / givens / black-box-vs-accelerated-kernels) round-trip through
`yaml.safe_load` cleanly.

**surface-or-evidence (pass).** Not a refinement of an operator/theme surface and carries no
rotation_claim — it is pure typed-edge frontmatter, the graded-stack P1 campaign shape. The
record-definition sub-check applies but finds no gap: none of the 12 pages defines a `{ field:
type }` data shape / named record (they are narrative-pointer + obstruction-classification +
disposition-test meta-pages), so no page needs a `## Record definition` home. The report correctly
notes that were any a record-definition page it would take a `depends-on (kind: cites-evidence)`
edge to its L0 struct — none occurred.

**rotation-quality (pass).** No-op: no algebraic/structural/reduction rotation is asserted. Typed
frontmatter recomposes no representation. Not applicable to a typed-edge frontmatter report.

**variant-axis-coverage (pass).** No-op: these pages carry no orthogonal variant axes; the dispatch
emits edges only. Not applicable to this report kind.

**cross-reference-integrity (pass — load-bearing for this report, exercised in full).** Every one of
the proposed `reference` edge targets was checked on disk: all ~37 distinct slugs across the 12
blocks resolve to an existing `book/src/<slug>.md` (L_n homes, L1/lowering pages, and concepts/
siblings all present; I also confirmed the two evidence-list-only mentions `L1/apply_linop.md` and
`L2/inner_product.md` exist). Zero dangling targets, so the `linkcheck2`/build-readiness guard is
satisfied. The 12 `[old]` anchors each match the live first line of their target file byte-for-byte
(e.g. `# concept: orthogonalization`, `# \`givens_apply\``, `# black-box vs accelerated kernels`),
so each edit will apply. The flagged `incremental-least-squares` repoint is verified: the prose
line 35 does name `givens-rotation`, `concepts/givens-rotation.md` does NOT exist, and
`concepts/givens.md` (the repoint target) DOES — the dispatch correctly typed the edge to the
existing slug and avoided introducing a dangling link.

**edge-label-fidelity (warning).** The all-`reference` / no-`depends-on` typing is the correct call
for these pages on the merits: a narrative-pointer concept page does not *rest on* (rank-constrain
or get constrained by) the entry it points at — the rank flows the other way and is carried by the
pointed-at entry's own `depends-on` block. The obstruction/disposition four
(`sequential-obstruction`, `scope-out-obstruction`, `negative-result-slice`,
`black-box-vs-accelerated-kernels`) as `reference`-only substrate (reference TARGETS of
obstruction-status entries, never `depends-on` supports) is also the right disposition. The
**warning** is for a real divergence the report itself surfaces (caveat 2): the authoring contract
in `graded-stack-scheme.md` §6 step 4 (and the scheme-page banner at line 15) states a
"methodology / process / narrative-concept page carries **no** `rank:`/`edges:`" — yet this dispatch
emits an `edges:` block (omitting only `rank:`) on all 12. The producer justifies this by reading
the HARD-gate-new "any node must be typed" + the dispatch's "type their own down-edges" as
overriding for concept *pages* (vs. the scheme/ladder methodology pages), explicitly flags it as an
open ambiguity, and defers the binding choice to the meta-phase. This is a scheme-vs-dispatch
convention question, not an internal contradiction of the report, and the producer characterizes it
accurately and reversibly — hence warning, not fail.

**plan-kind-consistency (pass).** Content shape matches the declared kind: typed-edge frontmatter
only, every `[new]` block is `---\nedges:\n  reference:\n  ...\n---\n` followed by the preserved
title line. No claim mutation, no rank token, no status-line edits — consistent with a graded-stack
P1 typed-edge dispatch. The "no `rank:` on a non-DAG meta-page" decision is correctly scoped to the
node-status convention and is internally consistent across all 12.

**skill-uptake-survey (pass, telemetry).** The dispatch shape (whole-artifact edge-typing) is the
graded-stack P1 campaign; the relevant procedure is the scheme's §6 authoring checklist, which the
report cites and follows. No dedicated edge-typing skill exists to reference; nothing missing.

### Issues found

1. **Scheme-vs-dispatch convention divergence — `edges:` block on a non-DAG meta-page**
   (CYCLE.md Open-questions caveat 2; all 12 proposed blocks). `graded-stack-scheme.md` §6 step 4
   and the scheme-page banner (line 15) say a narrative-concept/meta page carries **no
   `rank:`/`edges:`**; this dispatch emits `edges:` (no `rank:`) on all 12. The producer flags it
   explicitly and defers to meta-phase. Severity: low/methodology — per the dispatch framing this is
   a divergence to NOTE for meta-phase cross-D unification (D1 reference-only-block convention vs D2
   no-frontmatter vs this typed-edges-no-rank convention), not a within-report defect, since the
   choice is scheme-ambiguous, self-disclosed, reversible, and strictly more information. The
   meta-phase should ratify one of: (a) concept meta-pages carry typed `edges:` + no `rank:` (this
   dispatch's choice), or (b) pure §2d treatment (no frontmatter at all), which would drop these 12
   blocks.

2. **Pre-existing prose/naming drift in `incremental-least-squares.md`** (CYCLE.md caveat 3;
   `incremental-least-squares.md:35`). Prose names `givens-rotation`, a slug with no backing file;
   the kernel pair lives at `concepts/givens.md` (+ `givens_apply`/`givens_generate`). Confirmed: the
   prose line exists, `concepts/givens-rotation.md` is absent, `concepts/givens.md` is present. The
   dispatch correctly typed the edge to `concepts/givens` (no dangling link introduced) and left the
   prose untouched as out-of-scope, flagging it as
   `incremental-least-squares-prose-names-nonexistent-givens-rotation-slug` for a future
   harvester/cross-cutter touch. Severity: low/pre-existing — not introduced by this report; correctly
   routed. Noted as a candidate for a follow-up prose fix, outside this dispatch's typed-edge scope.

No build-safety, anchor-mismatch, dangling-target, or YAML-validity issues were found.

## Repair

### Fixes attempted

- **Finding 1**: edge-label-fidelity WARNING — scheme-vs-dispatch convention divergence:
  `graded-stack-scheme.md` §6 step 4 / banner says a narrative-concept meta-page carries no
  `rank:`/`edges:`, yet this dispatch emits a `reference`-only `edges:` block (no `rank:`) on all
  12 pages.
  - **Decision**: not-needed (ACCEPT-AND-ROUTE — no repair edit applied).
  - **Rationale**: The critic confirmed the typing is correct ON THE MERITS — all-`reference` /
    no-`depends-on` / no-`rank:` is the right disposition for these narrative-pointer +
    obstruction-classification + disposition-test meta-pages (the rank flows the other way and is
    carried by the pointed-at entry's own `depends-on` block). The warning is purely the
    scheme-text divergence, which is **self-disclosed, reversible, scheme-ambiguous, and strictly
    more information** than the no-frontmatter alternative. This is the SAME node-status /
    concept-page-encoding convention question the meta-phase owns and will unify at batch close
    (D1 reference-only block, D2 no-frontmatter, D3 reference-only block). **Normalizing or
    stripping the `edges:` blocks here would pre-empt the scheme-level meta-phase decision** — out
    of repair authority. Confirmed the divergence is captured for routing in TWO places: (a) this
    report's own Open-questions caveats 1 & 2; and (b) the sibling D5 report
    `reports/2026-06-05T072504Z-layer-intro-author-p1-concepts-infra-reconcile/CYCLE.md`
    §"Node-status convention applied + divergence flagged (for batch-close meta-phase unify)",
    which records the exact D1+D3-write-block / D2-no-frontmatter split "for the meta-phase to
    unify the concept-PAGE encoding at batch close." The umbrella OQ
    `graded-stack-index-and-concept-node-status` is in the ledger and the batch-33 graded-stack
    typed-edge campaign (with its 7 P1 OQs) is the active plan LEAD that owns the unification.
    Routing is in place; no further action required.

- **Caveat (non-defect)**: pre-existing prose/naming drift in `incremental-least-squares.md:35`
  (prose names a non-existent `givens-rotation` slug).
  - **Decision**: not-needed (no repair edit applied).
  - **Rationale**: Verified `book/src/concepts/givens.md` (the repoint target) EXISTS and
    `book/src/concepts/givens-rotation.md` is ABSENT — the dispatch correctly typed the edge to
    the existing `concepts/givens` slug, so **no dangling edge was introduced** (build stays green
    under `linkcheck2`). The prose drift itself is **pre-existing** (the page predates the
    `givens`/`givens_apply`/`givens_generate` split), out of typed-edge scope, and already flagged
    by the producer as `incremental-least-squares-prose-names-nonexistent-givens-rotation-slug`
    for a future harvester/cross-cutter touch. A prose-body slug rewrite is page re-authoring not
    owned by this typed-edge dispatch — left flagged, not expanded into scope.

### Unrepairable findings

None. The single warning is a scheme-ambiguous convention divergence correctly deferred to the
meta-phase (not within-report defect, not repairable by mechanical edit — it requires a
scheme-level ratification the repairer must not pre-empt). It is already routed for batch-close
unification, so it does not block this report.

## Suggested resolution

`ready`. All eight critic checks are `pass` except the one `edge-label-fidelity` warning, which is
ACCEPT-AND-ROUTE: the typed-edge content is correct on the merits, build-safe (zero dangling
targets, all 12 anchors byte-match, YAML round-trips), and the only open item is a scheme-vs-dispatch
convention question already captured for meta-phase unification (this report's caveats + D5's
batch-close flag + the umbrella OQ under the batch-33 LEAD). Integrator note: apply the 12 `edges:`
blocks as-is; do NOT strip the `edges:` blocks or add `rank:` tokens — the concept-page encoding
convention is meta-phase-owned and will be ratified at batch close.
