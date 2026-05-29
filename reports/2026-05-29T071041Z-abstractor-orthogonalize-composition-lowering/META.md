---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T07:27:00Z
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
repaired_at: 2026-05-29T07:41:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L2>L1 theme sketch — orthogonalize-composition-lowering"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing pinpoint was re-verified line-exact via
`palace-codemap` `read_range` + `search_text`. All confirmed: `IdentityInnerProduct`'s
`return LocalDot(x, y)` at `orthog.hpp:35` (report says `:35` — correct; note the cited
Sub-pattern D body in `dot-mutation-rotation.md:160,183` says `:34`, off by one, but that is a
pre-existing drift in the *other* file, not a defect in THIS report's claim); MGS def at
`:41`, `H[j] = dot_op(w, V[j])` at `:49`, `Mpi::GlobalSum(1, &H[j], comm)` at `:50`,
`w.Add(-H[j], V[j])` at `:51`; CGS def at `:57`, `if (m == 0)` at `:62`,
`Mpi::GlobalSum(m, H, comm)` at `:70`; CGS2 `if (refine)` at `:75`, `H[j] += dH[j]` at `:85`,
block range `:75-88` (function closes `:89`). Dispatch sites verified:
`OrthogonalizeIteration` at `iterative.cpp:308-325` with CGS2 = `OrthogonalizeColumnCGS(...,
true)` exactly at `:322`; ROM `OrthogonalizeColumn` at `romoperator.cpp:51-66` threading
`dot_op`; B-weighted `W.InnerProduct(x, y, r.Real())` at `romoperator.cpp:636`; GMRES consumer
`iterative.cpp:630-632` (`OrthogonalizeIteration` + `Norml2` + `*= 1.0/Hj[j+1]`). Test
pinpoints verified: empty-prefix `TEST_CASE` at `test-orthog.cpp:99`, the orthogonality
assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at `:158`, weighted-real-1 `TEST_CASE` at
`:276`, weighted-complex-1 at `:333`. The cited Sub-pattern D range
`dot-mutation-rotation.md:146-187` is in-range and on-point (the unfused `LocalDot` + batched
`Mpi::GlobalSum` surface is literally there, lines 146-187). All in-range, all real.

**surface-or-evidence — pass.** This is a NEW theme (a fresh `new:` proposed-changes block
authoring the full L2>L1 chapter), not a refinement of an existing operator/theme, so the
surface-modification + rotation_claim test applies in the new-theme reading: the report carries
both the new surface (the chapter body) and the L0/L2/L1 evidence backing every claim. Not a
pure-rotation_claim-without-surface entry; the surface IS the chapter. Pass.

**rotation-quality — pass.** The lowering content is genuinely a rotation, not a re-derivation
of L2 semantics. The L2>L1 work is the **per-variant `[dot, axpy]` sequence selection** (Face 2)
plus the identity-in-value specialization onto the opaque leaf (Face 1) — the L_n (L1) form is
made strictly more concrete/expanded (the de-fused primitive sequences with pinned pass-count
and collective shape) than the L_{n+1} (L2) named-composition form, which is the correct
direction for a lowering (the L2 is the more-abstract form; lowering expands it). The
MGS/CGS/CGS2 dispatch reads as L2 entry law 4 (variant agreement) + law 5
(idempotence-as-CGS2) instantiated as a lowering rule, NOT re-stated as L2 semantics: the
report explicitly delegates orthogonality/loss-free-decomposition restatement back to the L2
entry and confines itself to stage-selection. The Sub-pattern D reuse is correct and verified:
`dot-mutation-rotation.md:146-187` does contain the exact unfused `LocalDot` + batched
`Mpi::GlobalSum` surface being cited (header struct `orthog.hpp:29-36`, the batched CGS
collective `Mpi::GlobalSum(m, H, comm)`, the MGS per-`j` interleave), so the "cited, not
re-derived" claim holds — the theme does not duplicate that L1>L0 inner-product chain.

**variant-axis-coverage — pass.** Two orthogonal axes are present and both are handled. The
`gs_orthog ∈ {MGS, CGS, CGS2}` axis is exhaustively covered (each variant gets its own
`[dot, axpy]` sequence, collective shape, and source-witnessed body in the
§"Collective-shape recording" table). The `dot`-hook axis (`canonical ⟨·,·⟩` → `B-weighted`)
is covered as a closure substitution invariant on the lowering shape (applicability condition 5,
cited to L2 law 7 + `romoperator.cpp:636`). The element-type (real/complex) sub-axis is noted
as absorbed by `op.dot`. Householder is explicitly scoped out with a cited rationale (no L0
path; unimplemented-component policy). No hidden branches.

**cross-reference-integrity — pass (build-readiness guard clears).** All `[link]` targets
resolve to existing files: `L2/orthogonalize.md`, `L1/orthogonalize.md`, `L1/dot.md`,
`L1/axpy.md`, `L1-L0/dot-mutation-rotation.md`, `L1-L0/orthogonalize-mutation-rotation.md`, and
the two sibling `L2-L1/{linear-combination,inner-product}-fold-specialization.md` all exist.
The `edit:book/src/L2-L1/index.md` dep-map row anchors correctly (its `old` matches index.md
line 15, the inner-product-fold-specialization row, and the new orthogonalize row is appended
after). The `edit:book/src/SUMMARY.md` block anchors correctly (matches SUMMARY.md line 51, new
entry follows). **Firm-body-inside-fence guard: CLEAR.** Fence enumeration on CYCLE.md gives 14
` ``` ` markers (even parity); the `new:` block opens at line 47 and closes at line 464 with
four properly-paired nested ` ```text ` blocks inside (78-85, 107-111, 128-134, 157-175); the
two `edit:` blocks (466-469, 471-474) are balanced. All firm apparatus — `## L2 form (LHS)`
(72), `## L1 form (RHS)` (97), `## Justification kind` (307), `## Verified-against` (339), and
`## Status` (406) — sits INSIDE the `new:` fence. This is NOT the cycle-019 fence-truncation
defect. The forward-reference from the L2 entry (`L2/orthogonalize.md:275-279`, "forthcoming…
that chapter does not yet exist") is now satisfied by this same proposed-changes batch (live
link is OK — file created in the batch).

**edge-label-fidelity — warning.** The chapter is correctly narrated FORWARD (L2→L1)
throughout the body: the LHS is the L2 `orthogonalize` named composition (§"L2 form (LHS)"),
the RHS is the L1 two-face form (§"L1 form (RHS)"), and §"The variant-dispatch rewrite
(L2 → L1)" plus the dispatch-rule prose all read L2→L1. The edge labels in the dep-map row
(`L2/orthogonalize` → `L1/orthogonalize` + `L1/dot` + `L1/axpy`) are correct. **The one
deviation:** the chapter's own `## Open questions / caveats` first bullet (CYCLE.md lines
428-437, INSIDE the `new:` fence — i.e. inside the published mdBook chapter) is a substantial
**reverse-direction (L1→L2 lift) note**. The bullet self-labels "working notes only — NOT in
the high→low chapter body," but it physically IS in the chapter body that mdBook will publish.
Per the CLAUDE.md "Layers are defined high→low; lifting notes go in working notes" invariant,
reverse-direction lifting notes belong in `scaffolding/`, per-report supporting docs, or the OQ
ledger — NOT in the formal chapter content. The report already has a report-level
`## Open questions / caveats` (lines 508-520, OUTSIDE the fence) which is the correct home.
Flagged `warning` (not `fail`): the directional core of the theme is clean L2→L1; only this
single caveat-bullet leaks reverse-direction prose into the published chapter.

**plan-kind-consistency — pass.** Declared kind is `firm` (theme). The content shape matches:
the LHS is firm (L2 `orthogonalize`, cycle-019, verified `Status: firm`), both L1 RHS faces are
firm (the leaf cycle-012; `dot`/`axpy` post-cycle-002), the variant-dispatch rule is grounded
in the L2 entry's already-firm laws 4/5/7, no speculative operator is proposed (§"Speculative
L1 operators": None), and no negative-anchor reconstruction is present. No rough-in placeholders
anywhere in the firm body. The `algebraic` justification kind matches the sibling
`linear-combination-fold-specialization` precedent (verified: that sibling is also `algebraic`,
line 212, and carries the same firm-without-dedicated-L1↔L2-test caveat at lines 306-310, so
the report's firmness-bar and structural-precedent claims are corroborated).

**skill-uptake-survey — pass.** The report references `verify-citation-range`
(producer-self-verification sub-case) for the self-verified `Verified-against` block, and
`classify-variant-axis` is implicitly satisfied (the L2 entry it builds on uses the
classify-variant-axis output contract). For a firm-theme proposed-changes block whose shape
implies the fence-guard skill, note the producer is not the consumer of
`proposed-changes-fence-encloses-full-body-guard` (that is the critic's skill) — pure presence
check, non-blocking.

### Issues found

1. **Reverse-direction lifting note inside the published chapter** (severity: low/medium;
   `edit:book/src/L2-L1/orthogonalize-composition-lowering.md` via CYCLE.md lines 428-437, the
   chapter's `## Open questions / caveats` first bullet). The "Lifting note (reverse
   direction…)" bullet is a real L1→L2 lift discussion that sits inside the `new:` fence and
   will therefore publish as part of the formal mdBook chapter. The CLAUDE.md high→low invariant
   ("Layers are defined high→low; lifting notes go in working notes") requires reverse-direction
   notes to live in `scaffolding/` / supporting docs / the OQ ledger, not the chapter. Candidate
   repair: relocate the bullet's content out of the in-fence chapter section into the
   report-level `## Open questions / caveats` (already present, lines 508-520, outside the
   fence) or a supporting doc, leaving the in-fence section either dropped or reduced to the
   genuinely chapter-internal caveats (the Sub-pattern D delegation boundary, the OQ discharge,
   the no-dedicated-test caveat — all of which are forward-facing and chapter-appropriate). The
   bullet's own self-label ("working notes only") signals the producer knew the intent; the
   placement (inside the published-chapter fence) is the defect.

2. **Sub-pattern D anchor off-by-one is in the cited file, not this report** (severity:
   informational; not a defect in THIS report). This report cites Sub-pattern D's
   `return LocalDot(x, y)` correctly at `orthog.hpp:35`; the Sub-pattern D body in
   `dot-mutation-rotation.md` (lines 160, 183) cites the same line as `:34`. The true line is
   `:35` (verified). The report under critique is correct; the drift is in the upstream
   `dot-mutation-rotation.md` and is out of scope for this dispatch (noting it only so the
   repairer/integrator does not "fix" this report's correct `:35` to match the neighbor's stale
   `:34`). No action required on this report.

---

## Repair

### Fixes attempted

- **Finding**: edge-label-fidelity warning — the chapter's own in-fence `## Open questions /
  caveats` first bullet (CYCLE.md ~428-437, INSIDE the `new:` proposed-changes fence) is a
  substantial reverse-direction (L1→L2 lift) note that would publish as part of the formal mdBook
  chapter, violating the CLAUDE.md "Layers are defined high→low; lifting notes go in working notes"
  invariant. The chapter's directional core is otherwise clean L2→L1; only this one caveat-bullet
  leaked reverse-direction prose into the published chapter.
- **Decision**: repaired.
- **Action**: Surgical relocation — cut the reverse-direction lift bullet out of the in-fence
  chapter `## Open questions / caveats` (CYCLE.md `new:book/src/L2-L1/orthogonalize-composition-lowering.md`
  §Open questions / caveats) and pasted it into the report-level (OUTSIDE-fence)
  §Open questions / caveats (CYCLE.md, the report-tail section after `## Supporting evidence`),
  marked with a `[Repairer-relocated cycle-022: …]` provenance note explaining the move and the
  governing invariant. The substantive lift content is preserved verbatim. The three remaining
  in-fence bullets (Sub-pattern D delegation boundary, OQ discharge, no-dedicated-L1↔L2-test
  caveat) are all forward-facing/chapter-internal and were left in place — the in-fence section
  now opens coherently with the Sub-pattern D bullet. The high→low forward narration L2→L1
  (§"L2 form (LHS)", §"L1 form (RHS)", §"The variant-dispatch rewrite (L2 → L1)") is untouched.
- **Verification**: Fence parity re-checked after the edit — 14 ` ``` ` markers (even, unchanged
  from the critic's pre-repair count). The `new:` block opens at line 47 and closes at line 453
  (shrank from 464 by the 11 removed lines); all four nested ` ```text ` blocks (78/85, 107/111,
  128/134, 157/175) and both `edit:` blocks (now 455/458, 460/463) remain balanced. No fence was
  disturbed by either edit.

The other seven checks were `pass` from the critic — `not-needed`. (The informational
Sub-pattern D off-by-one note in the critic's Issues #2 is in the upstream `dot-mutation-rotation.md`,
NOT this report; per the critic's explicit instruction this report's correct `:35` was left as-is
— no action.)

### Unrepairable findings

None. The sole substantive finding was a mechanical in-fence→out-of-fence relocation within
repair authority (surgical cut/paste of a self-labeled working note to its correct home; no
content authoring, no artifact mutation).

## Suggested resolution

`ready`. Notes for the integrator:

- The chapter body that will publish (`book/src/L2-L1/orthogonalize-composition-lowering.md`) is
  now strictly high→low: the in-fence §Open questions / caveats carries only chapter-appropriate
  forward-facing caveats; the reverse-direction lift observation lives in the report-level
  working-notes section and is NOT part of the proposed-changes block, so it will not land in the
  artifact.
- Per the critic's Issues #2 (informational): do NOT "fix" this report's `orthog.hpp:35`
  Sub-pattern D anchor to match the stale `:34` in `dot-mutation-rotation.md` — `:35` is the
  verified-correct line; the drift is in the neighbor file, out of this report's scope.
