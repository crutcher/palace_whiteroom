---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T232600Z
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
repaired_at: 2026-05-28T233200Z
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

# META: verification of lifter divfree-projector "first"/"no-other-op" nesting-gate claim correction

## Critique

### Checks run

**citation-validity — pass.** Every emitted citation in the two proposed-changes
blocks was read against its source line this critique. (1) `book/src/L1/eigsolve.md:60`
— line 60 IS the `E` shape-contract bullet; it binds `linear : Solver[A]` AND
`projector : Maybe DivFreeSolver[ComplexVector]`, and the prose explicitly states
`projector` is the divergence-free projector itself. Two nested gates on the
asserted line, `E.projector` = the DivFreeSolver. CONFIRMED. (2)
`book/src/L1/eigsolve.md:136` — contains verbatim "making `eigsolve` the first L1
operator to compose two layers of constructed-operator absorption." CONFIRMED. (3)
`book/src/L1/eigsolve.md:140` — contains "composed-not-inherited" and "the **second
constructed-operator gate at L1**". CONFIRMED. (4)
`book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — `:213` opens "### Sub-pattern
B — inner-solve mutation-rotation", labeled "the **core sub-pattern** of the theme",
ten `opInv->Mult(b, x)` call sites enumerated (ARPACK 4 + NLEPS 1 + SLEPc 5),
each delegated to the firm `ksp-solve-mutation-rotation` theme; range closes within
`:258`. CONFIRMED. The two `[old]` blocks (`:108-113` sub-pattern A bullet, `:457-464`
Open-questions item) match the current divfree theme content byte-for-byte at those
lines. The provenance fact `8bb16b7` (cycle-011 eigsolve) predates `b54ea1c` (cycle-016
divfree) is declared inherited (not independently re-run), which is honest framing.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (edits to an
existing firm L1>L0 theme). It modifies surface (the two flagged passages in
`divfree-projector-mutation-rotation.md`) and the evidence is the firm artifact
content + a VERIFIED-SOUND cross-cutter audit — exactly the bounded
L0-evidence-driven prose-correction case in `.claude/agents/lifter.md` §Discipline.
The corrected claims are ACCURATE per the read-against-source verification above:
eigsolve genuinely IS a prior (cycle-011) and richer (two-gate) gate-carrying-gate
instance, so divfree is genuinely NOT the first. The correction does not introduce a
new inaccuracy on the load-bearing axis (this was the primary focus and it holds).
See the one terminological-imprecision observation under Issues found — it is a
clarity item, not an accuracy defect, and is inherited verbatim from the audit.

**rotation-quality — pass (not the operative axis for this report).** No new
algebraic/structural rotation is asserted. The proposal is a content-correction of
cross-theme provenance framing; it does not touch the LHS (L1 form) or RHS (L0 form)
of the divfree rotation, nor invert the high→low direction. The existing rotation
(L1 `P` apply → L0 four-step `DivFreeSolver::Mult`) is preserved untouched. No
renaming-masquerading-as-rotation to flag. Inapplicable-by-shape → pass.

**variant-axis-coverage — pass.** No variant axis is opened or closed by this
correction. The divfree theme's sub-patterns A–D, justification kinds, and
applicability conditions are explicitly preserved per §Discipline notes; the edit is
confined to the two false-uniqueness passages. The "two gates vs one gate" distinction
the new prose draws (eigsolve's `E.linear`+`E.projector` vs divfree's `P.ksp`) is a
faithful description of the existing closure shapes, not a new axis requiring coverage.

**cross-reference-integrity — warning.** All intra-theme links resolve:
`../L1/ksp_solve.md`, `./eigsolve-mutation-rotation.md`, `../L1/eigsolve.md` all exist
on disk. The one open item: both proposed blocks link
`../concepts/nested-constructed-operator-gate.md`, which does **not exist on disk
yet** — it is authored this same cycle by the parallel prong-a layer-intro-author
dispatch (`reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/CYCLE.md`,
confirmed: that report's proposed-changes carry a `[new]` block creating exactly
`book/src/concepts/nested-constructed-operator-gate.md`). This is a real same-cycle
co-dependency, not a phantom reference, and the report flags it explicitly with the
"exists at build time" rationale. It is marked `warning` (not `pass`) because it
encodes an **integration-ordering dependency**: if this report is integrated while
the prong-a report is deferred/rejected, the link dangles and `cargo make book`
linkcheck fails. Surfaced for the integrator's batch-ordering attention.

**edge-label-fidelity — pass.** The report carries the L1>L0 edge label
(divfree-projector-mutation-rotation is an L1>L0 theme) and the prose discusses
exactly that edge — and the cross-theme references it adds (eigsolve-mutation-rotation
at L1>L0; eigsolve.md / ksp_solve.md at L1) are all at consistent layers. No
edge-label/prose mismatch. The "transitively three-deep (eigsolve ⊃ divfree ⊃ ksp)"
chain is a within-L1 gate-nesting statement, not a cross-edge claim, and is correctly
framed as such.

**plan-kind-consistency — pass.** Declared kind is a bounded lifter content-correction
("re-anchor an existing theme to firmed-up vocabulary / fix a factually-wrong claim,
not re-architect"). The content shape matches: two surgical passage edits, no
decomposition/signature/sub-pattern/rotation change, append-only-after-`integrated_at`
discipline correctly invoked (the theme landed cycle-016, frontmatter already set; this
is the scoped-correction-dispatch the cross-cutter follow-up #1 routed). No re-architecting
leaked in. Consistent.

**skill-uptake-survey — pass.** The report's shape (self-verify every emitted citation
against source before emitting) is the `verify-citation-range` skill's territory, and the
report does perform per-citation read-against-source self-verification in §"Citation
self-verification" (four citations, each with READ + CONFIRMED note). It does not name
the skill by slug, but the procedure is executed; this is telemetry, not blocking.

### Issues found

1. **`nested-constructed-operator-gate.md` is a same-cycle forward reference —
   integration-ordering dependency.** (`book/src/L1-L0/divfree-projector-mutation-rotation.md`
   proposed blocks #1 `:108-113→new` and #2 `:457-464→new`; both add a live
   `[nested-constructed-operator-gate](../concepts/nested-constructed-operator-gate.md)`
   link.) Severity: low-medium. The target file does not exist on disk at critique
   time; it is created by the parallel prong-a dispatch
   (`2026-05-28T231017Z-layer-intro-author-nested-gate-concept`). The reference is real
   and intentional (both prongs route to the same OQ
   `nested-constructed-operator-gate-concept-and-divfree-correction`), and the report
   documents the dependency. The risk is purely ordering: if prong-a is not integrated
   in the same cycle, `cargo make book` linkcheck will fail on a dangling link. Candidate
   for repair = none needed at the report level (the link is correct); the integrator
   must co-apply or order prong-a first.

2. **Terminological imprecision: "the THIRD L1>L0 mutation-rotation" counts gates,
   not themes.** (`book/src/L1-L0/divfree-projector-mutation-rotation.md` proposed block
   #1 new text: "Divfree is the **third** L1>L0 mutation-rotation exhibiting the
   gate-carrying-gate shape (one gate), after eigsolve's two"; and block #2 "Divfree is
   the **third** instance (one gate)".) Severity: low (cosmetic clarity, NOT an accuracy
   defect). The "three-deep / third" count is along the **gate** axis (eigsolve
   contributes gates at positions 1 and 2 via `E.linear` + `E.projector`; divfree's
   `P.ksp` is gate 3), made explicit by the "(one gate) … after eigsolve's two" and
   "transitively three-deep (eigsolve ⊃ divfree ⊃ ksp)" parentheticals. But the noun
   phrase "the THIRD L1>L0 **mutation-rotation**" reads as a theme/operator count, and
   by *theme* count divfree is the SECOND gate-carrying theme (eigsolve theme, then
   divfree theme), not the third. Two readers could disagree on whether "third" means
   "third theme" or "third gate." Mitigating: this exact phrasing is inherited verbatim
   from the VERIFIED-SOUND cross-cutter audit
   (`2026-05-28T220000Z-cross-layer-cross-cutter-closure-nesting-gate/CYCLE.md:36`
   "divfree is the **third** L1>L0 mutation-rotation exhibiting gate-carrying-gate"), so
   the lifter faithfully tracked its source rather than inventing. A one-clause tightening
   (e.g. "the third gate-carrying instance — the second such theme, carrying the third
   nested gate") would remove the ambiguity. Optional repair; does not block.

3. **`eigsolve.md:140` cited for "composed-not-inherited"; "second constructed-operator
   gate at L1" also lives there.** (`divfree-...md` proposed block #2 cites
   `book/src/L1/eigsolve.md:140` after the "composed-not-inherited" attribution.) Not an
   error — verified `:140` carries both "composed-not-inherited" and "the **second
   constructed-operator gate at L1**, after `ksp_solve`." Noting only that the
   eigsolve-internal phrase "second constructed-operator gate at L1" (a different,
   operator-level count) sits one line away from the divfree "third gate" framing; a
   reader cross-navigating could conflate the two counts. This compounds issue #2's
   clarity concern but introduces no factual error. Severity: trivial / informational.

### Phase-boundary note

`git status --short` shows ZERO `book/` mutations during the dispatch phase — only
untracked `reports/` directories (the cycle-018 dispatch outputs). The dispatch
correctly produced proposed-changes blocks, not direct artifact edits. Phase boundary
clean.

---

## Repair

### Fixes attempted

- **Finding (issue 2, low / cross-reference-integrity-adjacent clarity)**: terminological
  imprecision — the noun phrase "the THIRD L1>L0 **mutation-rotation**" reads as a
  theme/operator count, but the count is along the **gate** axis (eigsolve contributes
  gates 1+2 via `E.linear`+`E.projector`; divfree's `P.ksp` is gate 3). By *theme* count
  divfree is the SECOND gate-carrying theme, so "third" is countable two ways.
  - **Decision**: repaired.
  - **Action**: tightened the two `[new]`-text passages in `reports/<id>/CYCLE.md`
    proposed-changes (block #1 = sub-pattern A bullet, current `:108-113→new`; block #2 =
    Open-questions item, current `:457-464→new`) to disambiguate gates-vs-themes. Both now
    read "the **second** gate-carrying [L1>L0] theme (after eigsolve), carrying the
    **third** nested gate overall (after eigsolve's two, `E.linear`+`E.projector`)" rather
    than the bare "third L1>L0 mutation-rotation / third instance". This is purely a
    wording tightening of new prose the report itself authors — no `[old]` block touched,
    surgical boundary preserved, no change to the load-bearing accuracy axis (eigsolve
    remains the prior richer instance; divfree remains genuinely not-the-first). Within
    repairer authority (mechanical wording disambiguation of a count the report already
    states two ways via the existing parentheticals; not substantive re-authoring).

- **Finding (issue 1, warning — cross-reference-integrity, integration-ordering)**: both
  proposed blocks link `../concepts/nested-constructed-operator-gate.md`, created THIS
  cycle by the parallel prong-a layer-intro-author dispatch
  (`reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/`); the target does
  not exist on disk at critique time.
  - **Decision**: not-needed (link is correct; do NOT change it — recorded for the
    integrator below).
  - **Rationale**: this is NOT a content defect — the link is intentional and correct, both
    prongs route to the same OQ
    `nested-constructed-operator-gate-concept-and-divfree-correction`. The only risk is
    integration ordering: if this report is applied while prong-a is deferred/rejected, the
    link dangles and `cargo make book` linkcheck fails. Changing the link (e.g. stubbing it
    out) would be substantive content authoring and would degrade the correct final state —
    out of repairer scope. Surfaced for the integrator under "Suggested resolution".

- **Finding (issue 3, trivial / informational)**: the eigsolve-internal phrase "second
  constructed-operator gate at L1" lives one line from the cited `:140`
  "composed-not-inherited", and an operator-level "second" count sits near the divfree
  "third" framing — a cross-navigating reader could conflate the two counts.
  - **Decision**: not-needed.
  - **Rationale**: the critic flagged this as trivial/informational with no factual error;
    the citation `:140` is verified-accurate for "composed-not-inherited". The issue-2
    repair (explicit "gate-carrying **theme**" vs "nested **gate** overall" wording) already
    reduces the conflation risk by naming the axis on the divfree side. No further edit
    needed.

### Unrepairable findings

None. The one warning (issue 1) is an integration-ordering dependency, not an
unrepairable content finding — the link is correct and must be preserved; routing is to the
integrator (batch ordering), not to a follow-up authoring agent. No `follow_up_agent`.

## Suggested resolution

`overall_status: ready`. Two notes for the integrator:

1. **INTEGRATION-ORDERING DEPENDENCY (load-bearing).** Both proposed-changes blocks in this
   report add a live link to `book/src/concepts/nested-constructed-operator-gate.md`, which
   is created by the parallel prong-a report
   `reports/2026-05-28T231017Z-layer-intro-author-nested-gate-concept/` (its `[new]` block).
   **`integrator-per-report` MUST apply the nested-gate concept-page report BEFORE or
   together with this divfree-correction report** so the link resolves at
   `cargo make book` linkcheck. If prong-a is deferred or rejected, do NOT apply this report
   in isolation — the link would dangle and the build would fail. The link is correct; do
   not alter it.

2. **OQ housekeeping (routing, not a blocker).** Per the report's §Open questions, the OQ
   `closure-nesting-constructed-gate-carrying-constructed-gate` should be marked ANSWERED
   (its "does not recur" premise is refuted by the eigsolve precedent), and the OQ
   `nested-constructed-operator-gate-concept-and-divfree-correction` prong-b is addressed by
   this report. Both are `integrator-per-report` open-questions-ledger authority.
