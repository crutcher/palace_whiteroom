---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T233500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T234500Z
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

# META: verification of CYCLE — Synthesis Wave-2 `data-algebra` library def bodies

## Critique

This report is the Wave-2 implementation-VIEW rendering of the Synthesis `data-algebra`
library: it renders the synthesized code form of 13 firm L4 data-algebra operators
(+1 roadmap_goal stub note) as a single `new:book/src/synthesis/data-algebra.md`
proposed-changes block. The chapter is a `navigational-container` (`status: stub`,
no `rank:`), `reference`-class links only. The dominant critic obligation here is
**fidelity** of the rendered def bodies to their authoritative L4 chapters; I
spot-checked 6 renderings against the on-disk L4 sources.

### Checks run

**citation-validity — pass.** The report's claims are sourced to the authoritative
L4 chapters under `book/src/L4/` and they all exist on disk (verified the full set:
`linear_combination`, `inner_product`, `dot`, `nrm2`, `fe_assemble`,
`mk_matrix_free_operator`, `eliminate_bc`, `assemble_frequency_operator`,
`gram_reduce`, `domain_energy_reduce`, `eigenfreq_qfactor_reduce`,
`sparameter_reduce`, `waveguide_mode_reduce`, `sharding-decompose-reduce`), plus the
concept homes (`concepts/dofset.md`, `concepts/WaveguideModeTable.md`), the
kernel-API node (`L1-L0/fe-assemble-libceed-boundary-obstruction.md`), the L2
contraction chain (`L2/matrix-free-operator-apply.md`), and the L4 doc-group intro
(`L4/data-algebra-combinators-intro.md`). This is an implementation-VIEW chapter
that re-cites the L4 chapters, not L0, per the directive — appropriate; no L0
pinpoint drift to adjudicate. **Fidelity spot-checks (all pass):**
- `linear_combination`: rendered body `foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs`
  + the four `where`-local arity aliases — exact match to `L4/linear_combination.md:88-89`
  signature/body and the §"Arity specializations" equations (`:122-125`).
- `inner_product`: rendered `reduce (+) zero (zipWith kernel x y)` + `inner_product_M`
  pre-apply + plain≡M=I — exact match to `L4/inner_product.md:85-90`; the
  real/complex conjugation kernel table is faithfully rendered inline (`L4/inner_product.md:109-113`).
- `nrm2`: `sqrt (abs (inner_product x x))` — matches the chapter's `√ ∘ abs ∘ inner_product`
  consumer form (`L4/inner_product.md:213`); the load-bearing `abs` non-negativity guard preserved.
- `eliminate_bc`: the RHS-side `b − K·x_bc` rendered as `linear_combination [(1, b), (-1, y)]` —
  exact match to `L4/eliminate_bc.md` §Signature; both verbs and the `DiagPolicy` pin matched.
- `assemble_frequency_operator`: `linear_combination [(1,K),(1i*omega,C),(-(omega^2),M),(1,A2 omega)]` —
  exact match to `A(ω) = K + iω·C − ω²·M + A2(ω)` (`L4/assemble_frequency_operator.md:21-25`).
- `gram_reduce` / `eigenfreq_qfactor_reduce` / `waveguide_mode_reduce`: diagonal-vs-offdiag
  (`matrix_weighted_norm` / `bilinear_form`), the `f = Re ω` / `Q = ω/κ` with `κ=0 ⇒ Q=∞`
  guard, and the `Bz = curl(Et)/(iω)` propagating-mode `Maybe` arm all match their chapters.

**surface-or-evidence — pass (feature-surface-adapted reading).** This is the
Synthesis implementation-VIEW kind, not a refinement-shaped proposal: it asserts no
new per-op algebraic claim; each rendered def links back to its authoritative L4
chapter (USE+LINK, don't restate — correct). The composition is supported (every
rendered def resolves to a real L4 chapter; the down-links exist). **Record-definition
sub-check:** `FrequencyOperatorFamily[N]` is named in `assemble_frequency_operator`'s
signature and is given an in-chapter inline record def (single-consumer case — correct
home). `DofSet[N]` / `DiagPolicy` and `WaveguideModeTable`/`WaveguideModeRow` are
rendered as cluster blocks with their authoritative concept-page homes linked (correct).
`DomainData` is named in `domain_energy_reduce`'s `# Returns` but deliberately NOT
defined here — the report links it to its authoritative home
`feature/energy-fields.L4.md §Record definition` and flags OQ
`record-DomainData-needs-definition-home` as the open routing — this is the
"explicitly flagged in Open questions" carve-out, so it is NOT a record-definition gap.

**rotation-quality — pass (not applicable to the implementation-VIEW / synthesis kind).**
The chapter rotates nothing — it recomposes already-firm L4 vocabulary into the
synthesized code form (the implementation VIEW, analogous to the feature-surface
no-op). No L_{n+1}→L_n rotation claim is asserted.

**variant-axis-coverage — pass (not applicable).** The synthesis rendering has no
variant axes of its own; the axes live in the constituent L4 ops it renders. The
report correctly leaves them on the L4 chapters and renders the closed-form bodies.

**cross-reference-integrity — warning.** Two findings (one navigational, one
build-readiness). (1) The link targets that resolve cleanly: all `../L4/<op>.md`
down-links and the two `../concepts/` cluster-type links exist. `synthesis/types.md`
and `synthesis/index.md` (linked in the intro + frontmatter `edges.reference`) do
NOT exist on disk yet — but they are sibling Wave-2 dispatches this same cycle (the
shell + the `types` library), and the report explicitly documents the merge ordering
(apply the shell `new:` first; this body merges onto it). This is the standard
same-cycle-sibling forward-link situation, acceptable for staged application — noted,
not a fail. (2) **The load-bearing finding — nested-fence truncation hazard.** The
proposed-changes block opens at CYCLE.md:27 with a 3-backtick ` ```new:... ` fence,
and the rendered file body inside it contains 12 nested 3-backtick ` ```text ` code
fences. The first inner fence-closer (CYCLE.md:93, intended to close the inner
`linear_combination` `text` block) will be read by a naive fence-parser as closing
the OUTER `new:` block — truncating the applied file at `linear_combination` and
discarding the other 12 defs. This is the cycle-019 fence-truncation defect class
(friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` family;
here the inverse — body fully INSIDE the fence but the fence is not escaped against
its own nested fences). The report's §"Open questions / merge mechanics" describes
the CONTENT merge (frontmatter no-op match) but describes NO fence-escaping mechanism
(e.g. a 4-backtick ` ````new: ` outer fence enclosing 3-backtick inner fences). The
firm-body-inside-fence guard's firm-trigger does not strictly fire (this is a
`stub`/`navigational-container`, not a `firm` claim), so this is a `warning` not a
`fail`, but it is a real build-readiness hazard the integrator must handle (re-fence
the outer block to 4 backticks on apply) or the chapter lands truncated.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; the relationship
asserted is `reference`-class implementation-VIEW links to the L4 surface, and the
prose discusses exactly those. The `realizes-kernel-api` correspondence is correctly
described as recorded on the L4 chapters, not re-asserted here.

**plan-kind-consistency — pass.** Declared kind is the Synthesis implementation-VIEW
rendering (`navigational-container`, `status: stub`); the content shape matches —
rendered code-form def bodies with code-doc, no new algebraic claims, `reference`-class
links only. The DIRECTIVE-3 dual-surface is rendered correctly and NOT conflated:
`fe_assemble` renders the opaque libCEED kernel-API leaf as `#extern assemble_term`
after its type signature (matching `L4/fe_assemble.md:72` opaque-input discipline),
while `mk_matrix_free_operator` renders the constructive kernel-impl as the inline
five-stage contraction chain `Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (matching
`L4/mk_matrix_free_operator.md:69-73` + the `Op[τ_in → τ_out]` operator-VALUE codomain
per semantics §1.3.1). `sharding-decompose-reduce` is rendered as a rank-0 roadmap_goal
prose stub note (NOT a filled def), matching the on-disk chapter's claim-free status
and its intended `subdomain_reduce = reduce ∘ restrict-to-block` combinator — the
DIRECTIVE-1 boundary is preserved. No `depends-on` edge is manufactured (frontmatter
`edges` carries only `reference:`) — verified.

**skill-uptake-survey — pass.** No skill invocation is strictly implied for an
implementation-VIEW rendering pass; the report references the governing conventions
(CLAUDE.md §"The SYNTHESIS section", semantics §1.2.1/§1.3.1, the KaTeX `$`-sigil-fence
memory) directly. Telemetry only; non-blocking.

### Issues found

1. **(cross-reference-integrity, build-readiness, severity: medium)** — CYCLE.md:27
   (proposed-changes block) — the outer ` ```new:book/src/synthesis/data-algebra.md `
   fence is 3-backtick and encloses 12 nested 3-backtick ` ```text ` code fences;
   the first inner closer at CYCLE.md:93 will truncate the applied file at the
   `linear_combination` def under a naive fence-parser (cycle-019 fence-truncation
   defect class). The report's merge-mechanics note covers content-merge ordering but
   describes no fence-escaping mechanism (outer fence should be 4-backtick
   ` ````new: ` to enclose the 3-backtick inner fences). Repair candidate: re-fence
   the outer proposed-changes block to 4 backticks.

2. **(cross-reference-integrity, same-cycle sibling forward-link, severity: low /
   informational)** — CYCLE.md:53-54, 61 — `synthesis/types.md` and `synthesis/index.md`
   are linked (intro + frontmatter `edges.reference`) but do not exist on disk; they
   are sibling Wave-2 dispatches this cycle. The report documents the staged
   apply-the-shell-first ordering. Not a defect in this report — surfaced so the
   integrator confirms the sibling shell/`types` dispatches land in the same cycle so
   the links resolve at `linkcheck2` time.

3. **(fidelity, informational, severity: none)** — the synthesized helper names
   (`restrict_essential`/`set_essential`, `conj_if_complex`, `apply_chain`/
   `element_restrict[_T]`/`basis_apply[_T]`/`quad_point_contract`, `mask_to`/
   `scatter_essential`/`mkOp`) are rendering glue spelling the L4 prose, not claims
   about named spine verbs — the report flags this clearly and routes the
   `lowering-verifier` to audit body-shape correspondence, not exact spelling. No
   action needed; recorded for the downstream lowering-verifier audit.

## Repair

### Fixes attempted

- **Finding**: (cross-reference-integrity, build-readiness) — the outer
  ` ```new:book/src/synthesis/data-algebra.md ` proposed-changes fence (CYCLE.md:27)
  is 3-backtick and encloses 15 nested 3-backtick ` ```text ` code fences; the first
  inner closer would truncate the applied file at the `linear_combination` def under
  a naive fence-parser (cycle-019 fence-truncation defect class).
  - **Decision**: repaired.
  - **Action**: re-fenced the OUTER `new:` block to 4 backticks at both boundaries —
    opener CYCLE.md:27 (` ````new:book/src/synthesis/data-algebra.md `) and closer
    CYCLE.md:491 (` ```` `). The 15 nested 3-backtick ` ```text ` fences are now
    unambiguously contained; a fence-parser scanning for the outer terminator skips
    all 3-backtick lines and stops only at the 4-backtick closer. This is the
    established safe pattern (4-backtick outer fence around 3-backtick inner fences).
    Verified balance: exactly two 4-backtick lines (27, 491) bracketing 30 pure
    3-backtick lines (15 openers + 15 closers, even/balanced).

- **Finding**: (cross-reference-integrity, same-cycle sibling forward-link, severity:
  low / informational) — `synthesis/types.md` + `synthesis/index.md` linked but not
  yet on disk; sibling Wave-2 dispatches this cycle.
  - **Decision**: not-needed.
  - **Rationale**: the critic explicitly marked this informational, not a defect in
    this report — it is the standard same-cycle-sibling staged-apply situation the
    report documents (apply the shell `new:` first). No repair-authority action; the
    integrator confirms the sibling dispatches land in-cycle so links resolve at
    `linkcheck2` time. Not the gating finding for the `warning`.

- **Finding**: (fidelity, informational, severity: none) — synthesized helper-name
  glue.
  - **Decision**: not-needed.
  - **Rationale**: critic marked "no action needed"; flagged glue for the downstream
    `lowering-verifier` audit, not a repairable defect.

### Unrepairable findings

None. The single load-bearing warning (the nested-fence truncation hazard) is a
mechanical, surgical re-fencing — squarely within repair authority and now applied.
The two remaining findings were informational (not-needed), not unrepairable.

## Suggested resolution

`ready`. The cross-reference-integrity `warning` was driven by the build-readiness
fence hazard, which is now fixed by the 4-backtick re-fencing — the chapter will
apply in full (all 13 firm defs + 1 roadmap_goal note) rather than truncating at
`linear_combination`. Integrator note: this is a staged same-cycle apply — apply the
sibling shell (`2026-06-07T230500Z-layer-intro-author-synthesis-section-shell`) and
the `types` library dispatch in the same cycle so `synthesis/index.md` /
`synthesis/types.md` and `concepts/dofset.md` / `concepts/WaveguideModeTable.md` links
resolve at `linkcheck2` time. The frontmatter `edges` carries only `reference:` — no
`depends-on` edge is manufactured, so no rank/liveness constraint on any firm node.
