---
agent: cycle-planner
invoked_at: 2026-06-02T191346Z
scope: cycle-067 dispatch plan
status: pending
---

# Cycle 067 dispatch plan

## Goals selected this cycle

Cycle-067 is the LEAD primary cycle of meta-batch-21, reshaped by the four 2026-06-02 user directives.
Two threads run in parallel: (1) the unambiguous clean LEAD — finish the FE-space sub-spine **tail
cleanup** (D1 `lifter`, two on-disk-verified replace-and-propagate/live-link upgrades); (2) **OPEN the
batch-21 frontier** decided by directive 1 — the **FE-assembly/FE-space cohort → L4 lift** — with a
cheap warrant-first **observation-only survey** (D2 `cross-layer-cross-cutter`) that classifies the 8
stranded-at-L1 cohort members by the directive-2 three-way black-box/accelerated/named-abstraction test
and scopes the L4 `assemble`-fold combinator + opaque-leaf wrapping for the c068 landings. The two light
directive-driven concept/methodology pieces ride this cycle: the directive-2 **black-box/accelerated
concepts page** (D3) — which feeds D2's classification vocabulary — and the directive-4 **Methodology
GOAL+FLOW v1 seed** (D4) for an early user review window. The heavy directive-3 mdBook reorg is
deliberately NOT in c067 (directive 3 reserves it as its own structural wave); it is appended to the
plan as a c068/c069-or-meta-phase candidate.

## Dispatches

**D1 — `lifter` — `fe-space-sub-spine-tail-cleanup` (the LEAD; clean closes; LOW-MEDIUM fan-out).**
Scope: two on-disk-verified tail cleanups in `book/src/L1/`:
(a) `eliminate_essential_bc.md:56,68` — upgrade the `dofs: DofSet[N]` typed parameter to a live
`[essential_dofs](./essential_dofs.md)` cross-ref (replace-and-propagate, same class as the c065
`fe_space` opaque-parameter pass; `essential_dofs.md` is firm on disk). ALSO judge `eliminate_rhs.md`
(`:55,57,79-81` discuss the essential gather/scatter via `restrict_essential`/`set_essential` masking
and already cross-ref `fe_space`) — add an `essential_dofs` cross-ref ONLY if the essential-dof set is
named as a typed object there (the masking-projection framing may not warrant a link; lifter judgment —
do NOT manufacture a link where the text uses masking projections, not the dof set).
(b) `fe_space.md:39` + `:149` — upgrade the two "forward-reference until on disk" notes for
`fe-space-construction-rotation` to live `[fe-space-construction-rotation](../L1-L0/fe-space-construction-rotation.md)`
links (the theme is firm on disk; skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`).
All entries stay `firm` (surgical cross-ref/link upgrades, no status flips → no index-cell touch).
**Close-brace discipline:** D1 changes no `path:lo-hi` END lines (pure prose cross-ref edits); if it
touches any citation END, confirm by direct on-disk `Read`, NOT `citecheck --anchor` (recurrence-6).
deps: none.
rationale: active-head item 1 (the LEAD); closes the open FE-space front residue (the 3 batch-20-migrated
follow-ons). Integrator-signals c066 explicitly suggested both as small targeted lifter touches.

**D2 — `cross-layer-cross-cutter` — `fe-cohort-l4-lift-survey` (THE BATCH-21 FRONTIER OPENER;
observation-ONLY, authors nothing to `book/`; HIGH fan-out).**
Scope: the 8 firm-L1 FE-assembly + FE-space cohort entries (`fe_assemble`, `fe_space`, `fe_collection`,
`essential_dofs`, `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`,
`assemble_frequency_operator`) are stranded at L1 with ZERO presence above L1 (verified-ABSENT from
`book/src/L4/` this cycle) — the real deliverable hole directive 1 names (L4 is the outward
backend-lowering target; must be COMPLETE over the in-scope feature set). Warrant-first survey:
(i) classify each member by the directive-2 THREE-WAY test (black-box-rises / accelerated-stopped-low /
named-abstraction-keep-and-rise);
(ii) scope the **L4 `assemble`-fold combinator** shape — `fe_assemble` is literally a
concatenation-homomorphism `foldr` over the weak-form term list (`fe_assemble.md:60-61`:
`fe_assemble(space, terms) = foldr (\t acc -> A(space, t) + acc) zero terms`), the natural L4 combinator
— + the **opaque per-element libCEED quadrature leaf** as a black-box-kernel `readonly` L4 input
(the `integ->Assemble` sites `palace/fem/bilinearform.cpp:75,95`, the `PartialAssemble` boundary
`:112`, and `CeedOperatorFullAssemble` `palace/fem/libceed/operator.cpp:455` — codemap-localized this
cycle; these are LOCALIZATION HINTS — the producer on-disk-confirms any cited line, esp. END/close-brace
lines, NOT via `citecheck --anchor`). These are already filed `obstruction (opaque-library-ownership)`
at L1>L0; the survey POSITIVELY reframes them as a black-box kernel rising to L4 as an opaque input —
the SAME opaque-leaf-wrapping pattern `fold_solve`/`eigsolve` already use at L4;
(iii) decide which members rise as L4 vocabulary (the assemble fold) vs which are opaque L4 construction
INPUTS (`fe_space`/`fe_collection`/`essential_dofs` may be opaque construction inputs, not combinators)
vs intermediate L2/L3 identity-skip (the cycle-012 non-adjacent in-line rotation convention — L4 is the
destination regardless; intermediate rungs may legitimately be identity);
(iv) fan-out-rank the resulting per-member L4 dispatches for c068.
**Anti-mirror NOTE (directive 1, load-bearing):** the NO-L2 warrants (`fe_assemble` c063,
`weak_form_term`, `L2/fe_assemble`) bar only the L1→L2 rectangular MIRROR — they do NOT close the
upward-to-L4 question. Do NOT read "no L2 mirror" as "upward climb done." The STOP-PROPOSING entries bar
L2 forms, NOT L4 forms.
Also surface the directive-1 "re-examine no-L4-by-design" question as a sub-finding: `book/src/L4/index.md:66`
asserts the 13-of-18 BLAS-1/elementwise/smoother L3 ops are no-L4-by-design — judge per-case under
directive 2 (base tensor primitives in L3 global-tensor-field form may be the backend-target form, while
`linear_combination`/`inner_product` combinators + the kept `dot`/`nrm2` abstractions DO rise to L4).
This is a survey sub-observation, not a c067 landing.
Cite the `disciplined-cross-pipeline-combinator-mining-gate` skill where a fold/combinator shape surfaces.
deps: none (observation-only; references D3's classification but does not require it to land — see overlap).
rationale: active-head item 3, retargeted L2/L3→L4 by directive 1; the cheap warrant-first first step that
opens THE batch-21 frontier without forcing any landing. Authors nothing to `book/` — the per-member L4
landings open c068 from this survey's fan-out ranking.

**D3 — `layer-intro-author` — `black-box-vs-accelerated-kernels-concept-page` (NEW concept page;
MEDIUM fan-out; directive-2 enactment).**
Scope: author `book/src/concepts/black-box-vs-accelerated-kernels.md` (canonical slug
`black-box-vs-accelerated-kernels`; verified-ABSENT this cycle) capturing the directive-2 three-way
disposition: (1) no-decomposition + clean surface → **rises (black-box kernel)** — first-class primitive,
NOT a failure; body opaque, external backend supplies impl; canonical `eigsolve`, also `ksp_solve` / the
per-element libCEED quadrature leaf inside `fe_assemble` / `fold_solve`'s `ode->Step`; the POSITIVE reframe
of the negative `obstruction (opaque-library-ownership)` filing (distinct from an unimplemented enum-only
Palace stub, which stays a true obstruction); (2) decomposes + literature-standard + aids downstream
simplification → **keep-and-rise (named abstraction)** — confirmed keeps `dot`/`nrm2`, kernel tied below,
parent combinator rises too (a permitted genuinely-distinct dual); (3) decomposes + solely-for-speed +
no abstraction value → **stopped-low (accelerated kernel)** — combinator rises in its place;
`axpy`/`axpby`/`axpbypcz`/`scal` family the per-case candidate over `linear_combination`. State the test
is JUDGMENT (abstraction value), not just "does it decompose"; `linear_combination`/`inner_product`
combinators rise to L4 regardless. Synthesize FROM project memory `project_blackbox_vs_accelerated_kernels`
+ the priorities.md directive-2 banner (NOT a fresh derivation); cite canonical-instance chapters
(`L4/eigsolve`, `concepts/eigsolve`, `concepts/dot`, `concepts/nrm2`, `concepts/scal`, `L1/fe_assemble`).
Wire into `SUMMARY.md` concepts list in ALPHA position (directive 3 active-immediately:
`black-box-vs-accelerated-kernels` sorts between `axpy` and `build-time-vs-run-time-stratification`).
**Close-brace discipline:** any cited source END line confirmed on-disk, not `--anchor`.
deps: none.
rationale: active-head item 4; directive-2 enactment; the shared classification vocabulary D2's survey
+ all batch-21 lift dispatches consume.

**D4 — `layer-intro-author` — `methodology-goal-flow-chapter-v1-seed` (NEW methodology chapter v1;
MEDIUM fan-out; directive-4 enactment).**
Scope: seed the reader-facing **Methodology GOAL+FLOW chapter** under `book/src/methodology/`
(`book/src/methodology/` exists with only `overview.md`; the GOAL+FLOW chapter is ABSENT). Author
`book/src/methodology/goal-flow.md` (or `goal.md` + `flow.md`; author's structural judgment — single
chapter preferred for v1) with a GOAL section (the integrated view of what the book's goals ARE — the
L4→L0 impedance-matching stack, L4 as the outward backend-lowering feature surface, the layered
representational/vocabulary shifts) + a FLOW section (how they are met — the 5-phase primary cycle +
every-3rd meta-phase cadence, warrant-first/anti-mirror/replace-and-propagate discipline, the
solver-test-load). **NON-AUTHORITATIVE — load-bearing:** a synthesized descriptive MIRROR, NOT a
directive source; explicit non-authoritative / synthesized-view / review-point header MANDATORY;
synthesized FROM CLAUDE.md / `METHODOLOGY-REDIRECT.md` / memory / `priorities.md` + the emergent state;
if it contradicts a source the source wins + this chapter is corrected. Wire into `SUMMARY.md` under the
existing `# Methodology` Part (line 4-5), after `overview.md`. Note in the chapter that ownership
transfers to meta-phase post-seed (refreshes each batch).
deps: none.
rationale: active-head item 5; directive-4 enactment; v1 seeded early in batch-21 (directive-4 v1-timing:
the goal-understanding is rich now with the three 2026-06-02 directives) for an earlier-than-c069 user
review window. Meta-phase adopts + maintains thereafter.

## Overlap analysis

Pairwise (4 dispatches, 6 pairs):

- **D1 ↔ D2:** D1 edits `book/src/L1/eliminate_essential_bc.md` + `fe_space.md` (+ maybe `eliminate_rhs.md`);
  D2 authors nothing (observation-only) and only READS the 8 cohort entries. No shared write region.
  **NON-OVERLAPPING → parallel.**
- **D1 ↔ D3:** D1 edits `book/src/L1/*`; D3 creates `book/src/concepts/black-box-vs-accelerated-kernels.md`
  + appends one `SUMMARY.md` concepts-list row (alpha position). No shared file. **NON-OVERLAPPING → parallel.**
- **D1 ↔ D4:** D1 edits `book/src/L1/*`; D4 creates `book/src/methodology/goal-flow.md` + appends one
  `SUMMARY.md` Methodology-Part row. No shared file. **NON-OVERLAPPING → parallel.**
- **D2 ↔ D3:** D2 is observation-only (writes only its report); D3 authors the concept page. D2's survey
  REFERENCES the directive-2 three-way classification D3 codifies, but both synthesize the SAME source
  (project memory `project_blackbox_vs_accelerated_kernels` + the priorities banner) — neither depends on
  the other's output landing (D2 cites the directive, not D3's page; the report integrates after both).
  No shared write region. **NON-OVERLAPPING → parallel.**
- **D2 ↔ D4:** D2 observation-only; D4 authors methodology. No shared file. **NON-OVERLAPPING → parallel.**
- **D3 ↔ D4:** both are `layer-intro-author` and both append ONE row to `SUMMARY.md` — but to DISTINCT,
  anchor-distinct regions (D3 → concepts list ~line 217+, alpha position; D4 → `# Methodology` Part line
  4-5, after `overview.md`). Distinct `SUMMARY.md` rows in non-adjacent regions are append-distinct, NOT
  a shared-region rewrite — per the Discipline "two dispatches that append distinct rows to the same table
  are NOT overlapping at the operational level → parallel." The per-report integrator serializes the two
  `SUMMARY.md` inserts cleanly (anchor-distinct). **NON-OVERLAPPING (append-distinct) → parallel; minor
  same-file conflict is integrator-handled per the conflict-tolerance philosophy.**

No two dispatches modify the same operator entry or rewrite the same theme body. No dispatch names an
operator slug another dispatch authors (D3's concept-page slug + D4's methodology slug are both new and
distinct; D2 references neither as a forward-link — it reports). **No count-ownership/dual-registration
partition is needed this cycle** — no two dispatches co-write a consolidated layer-index tally (D1 flips
no statuses; D2 authors nothing; D3/D4 touch concepts/methodology, not a counted layer index). The
retired rectangular-floor count-ownership machinery is correctly not invoked.

## Sequencing schedule

**Single wave — all 4 dispatches parallel (wave 1).** D1/D2/D3/D4 are mutually non-overlapping (no
forward-reference dependency: D2 authors nothing so no sibling needs its slug; D3/D4 create new pages
neither D1 nor D2 links). No dispatch references a not-yet-landed sibling slug, so no wave-2 ordering is
needed. The single `integrator-finalize` runs once at cycle end (per the one-finalize-per-cycle rule);
the per-report integrators serialize the writes (D1's L1 edits, D3's concept page + SUMMARY row, D4's
methodology page + SUMMARY row; D2 has no artifact write).

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence check (friction `cycle-planner-stale-priorities-line-recruitment`,
`escalating`). Pasted literal command output:

**D1 (a) — `eliminate_essential_bc.md` DofSet→essential_dofs (verify-PRESENT target + verify link target firm):**
```
$ grep -n 'DofSet\|essential_dofs\|dofs:' book/src/L1/eliminate_essential_bc.md
56:eliminate_essential_bc :: (K: LinearOperator[N, N], dofs: DofSet[N], policy: DiagPolicy)
68:- `dofs` — `DofSet[N]` — the essential (Dirichlet) true-dof index set, a subset of `0..N` over the
$ ls -la book/src/L1/essential_dofs.md   # link target exists + firm
-rw-rw-r-- 1 ... 11459 ... book/src/L1/essential_dofs.md
$ grep -m1 'status:' book/src/L1/essential_dofs.md  -> status: firm
```
`DofSet[N]` confirmed present at `:56,:68`; link target `essential_dofs.md` firm on disk. **OPEN — recruit.**

**D1 (b) — `fe_space.md` forward-ref→live-link (verify-PRESENT forward-ref notes + theme on disk):**
```
$ grep -n 'forward-reference until on disk\|Forward-reference until' book/src/L1/fe_space.md
39:theme `fe-space-construction-rotation` (authored cycle-064 D3; forward-reference until on disk).
149:extraction (... ). (Forward-reference until that theme is on disk.)
$ ls book/src/L1-L0/fe-space-construction-rotation.md   # link target exists
book/src/L1-L0/fe-space-construction-rotation.md (present; firm per c064 D3 + c066 finalize)
```
Forward-ref notes present at `:39,:149`; theme on disk. **OPEN — recruit.** (Integrator-signals c066
flagged this exact `fe_space.md:39/:149` plain-text→live-link upgrade as a suggested next dispatch.)

**D2 — FE-cohort→L4 lift survey (verify-ABSENT: cohort has zero L4 presence; open-by-construction survey):**
```
$ ls book/src/L4/
chebyshev.md  eigsolve.md  fold_solve.md  index.md  iterate-while.md
iterate-while-with-prev.md  krylov-step.md  ksp_solve.md  solve_family.md
```
No `fe_assemble.md` / `fe_space.md` / `fe_collection.md` / `essential_dofs.md` / `weak_form_term.md` /
`eliminate_*.md` / `assemble_frequency_operator.md` in `book/src/L4/` — the cohort is ABSENT above L1.
All 8 cohort members verified `firm` at L1:
```
$ for f in fe_assemble fe_space fe_collection essential_dofs weak_form_term \
    eliminate_essential_bc eliminate_rhs assemble_frequency_operator; do
    grep -m1 -iE 'status:|firmness:' book/src/L1/$f.md; done
fe_assemble: firmness: firm     fe_space: status: firm     fe_collection: status: firm
essential_dofs: status: firm    weak_form_term: firmness: firm
eliminate_essential_bc: firmness: firm   eliminate_rhs: firmness: firm
assemble_frequency_operator: firmness: firm
```
**OPEN by construction** (observation-only survey opening a new frontier; no prior-cycle L4-cohort history).
Structural gate: NOT on the STOP-PROPOSING list — that list bars L2 MIRRORS (`L2/fe_assemble`,
`weak_form_term` L2 floor), explicitly NOT L4 forms (directive 1, re-confirmed). **Recruit.**

**D3 — black-box/accelerated concept page (verify-ABSENT):**
```
$ ls book/src/concepts/ | grep -iE 'black|accel|opaque|kernel'
(no matches)
```
No black-box / accelerated / opaque-kernel concept page on disk. **OPEN — recruit** (fresh, open by
construction; directive-2 enactment).

**D4 — methodology GOAL+FLOW v1 (verify-ABSENT chapter; dir exists):**
```
$ ls -la book/src/methodology/
overview.md   (only)
$ grep -n -i 'methodolog' book/src/SUMMARY.md
4:# Methodology
5:- [Overview](./methodology/overview.md)
```
`book/src/methodology/` carries only `overview.md`; no GOAL+FLOW chapter. **OPEN — recruit** (fresh, open
by construction; directive-4 v1-seed).

**OQ-ledger RESOLVED-grep (none of the recruits is a closed-and-stale line):** the c066 integrator-signals
list both D1 targets as live suggested-next-dispatches (`eliminate-star-dofset-cross-ref-to-essential-dofs`,
`fe-space-construction-rotation-forward-ref-live-link-upgrade` — needs-more, not resolved). D2/D3/D4 are
fresh directive enactments (the directives postdate the batch-20 meta-phase). No recruit matches a
RESOLVED/CLOSED slug.

All four checks pass for all four dispatches; none on the STOP-PROPOSING list; framings correct
(D2 audit-first/observation-only; D1 surgical-lifter; D3/D4 fresh-authoring). The directive-3 mdBook reorg
is correctly NOT recruited (sequenced to its own structural wave per directive 3).

## Open questions / caveats

- **D1 `eliminate_rhs` sub-judgment is left to the lifter.** `eliminate_rhs.md` already cross-refs
  `fe_space` and frames the essential-dof handling as masking projections (`restrict_essential` /
  `set_essential`), NOT as a typed `DofSet[N]` object — so an `essential_dofs` cross-ref there may NOT be
  warranted (manufacturing a link where the text uses masking projections would be over-linking). The
  active-head line (a) named both `eliminate_*`; I have scoped D1 to upgrade `eliminate_essential_bc`'s
  explicit `DofSet[N]` (clearly warranted) and to JUDGE `eliminate_rhs` (link only if the dof set is named
  as a typed object). Flagging for the human in case the intent was a forced link on both.

- **D2 survey is the warrant-first OPENER, not the landing.** Per directive 1 the FE-cohort→L4 lift is THE
  frontier, but it is large (8 members + the assemble-fold combinator + the opaque-leaf wrapping + the
  no-L4-by-design re-examination). c067 opens it with the cheap observation-only survey (tail cleanup is
  light, so opening the frontier this cycle is the right call per the planner brief); the per-member L4
  landings open c068 from D2's fan-out ranking. If D2's classification surfaces a member that does NOT
  cleanly rise to L4 (e.g. a pure construction input better left as an opaque L4 parameter), that is a
  spine finding recorded in the survey, not a forced land — consistent with the redirect's clean-gate.

- **Directive-3 mdBook reorg sequencing (flagged for the batch-21 meta-phase / human).** I appended it as
  plan item 7 sequenced to a dedicated structural wave at c068/c069 OR routed to the batch-21 meta-phase
  (post-c069) for the one-time reorg + role-spec codification. Directive 3 is active-immediately via the
  orchestrator per-dispatch prompts (new SUMMARY entries inside the right kind group; dep-map rows in
  alpha position) — so D3/D4's new SUMMARY rows this cycle should land in alpha position (D3 concepts-list)
  / inside the Methodology Part (D4) per that directive. The full structural regroup is NOT a c067
  forward-frontier item. **Decision recorded: c067 does NOT dispatch the reorg.**

- **Methodology chapter ownership transfer.** D4 seeds v1; directive 4 makes meta-phase the owner
  thereafter. The batch-21 meta-phase (post-c069) must (i) adopt + refresh the chapter, (ii) codify the
  maintenance target into `.claude/agents/meta-phase.md` (a `.claude/agents/` edit → session restart). I
  flag this so the meta-phase picks it up; the c067 D4 seed carries the explicit non-authoritative header.

- **Cap usage:** 4 dispatches (well under the 12 cap). The active head plus the four directives did not
  fill more slots cleanly this cycle — the heavy frontier work (per-member L4 landings) is correctly
  deferred to c068 behind the D2 survey warrant, and the reorg is deferred to its own wave. Fewer is fine
  per Discipline.

- **`fe_space_hierarchy` (active-head item 2) intentionally NOT recruited.** It is pull-gated MEDIUM-LOW
  (the geometric-multigrid consumer pull is not concrete this cycle), and the directive-1 FE-cohort→L4 lift
  is the higher-fan-out frontier. It stays the standing next FE-space-sub-spine pick; recruit when a
  multigrid consumer pulls it or as the sub-spine's natural completion. Not stale, just lower-priority.
