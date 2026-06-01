---
agent: cycle-planner
invoked_at: 2026-06-01T190828Z
scope: cycle-049 dispatch plan
status: pending
---

# Cycle 049 dispatch plan

## Goals selected this cycle

Cycle-049 is the FIRST primary cycle of meta-batch-15 and the FIRST cycle after the
2026-06-01 VOCABULARY-SHIFT REDIRECT. The lead frontier is the **REFACTOR PASS** (redirect
program item 1, highest priority, precedes all new forward-frontier work): collapse the
cycles-041–048 base-form leaf floors into **in-layer combinators**, propagate the combinator
**upward**, demote the thin `-body-identity`/`-leaf-identity` themes to in-line notes, and
re-audit every touched lowering under the translation/smell test.

The key on-disk finding from this cycle's survey reshapes how the refactor is scoped (see
§Survey findings): the two fold combinators **already exist** at L2 (`linear_combination`,
`inner_product`) — but they were authored under the OLD mine-and-strand regime where the
combinator is explicitly "the form the leaves fuse *up* into, **NOT a replacement**." The
refactor's first move is therefore to **invert that framing to combinator-as-entry**, not to
mine a new combinator. AND the combinator was **never propagated to L3** (there is no
`L3/linear_combination`/`L3/inner_product`; the L3 leaf entries reference `linear_combination`
zero times) — the canonical mine-and-strand drift the redirect (§5 of `METHODOLOGY-REDIRECT.md`)
names.

This cycle leads with the **two replace-and-propagate maps** (one per fold family,
combinator-miner per the redirect routing) which also enact the L2-entry inversion they own,
plus one **audit-first** dispatch producing the degenerate-theme demotion worklist. The bulk
enactment (collapsing 6 L2 leaf entries, authoring the 2 L3 combinators + re-expressing the L3
leaf cohort, demoting 12 themes, L4 propagation) is genuinely large, depends on the maps, and
is sequenced to cycle-050. This is the deliberate measured shape for a first refactor cycle:
map-then-enact, not big-bang.

## Survey findings (the refactor surface, on-disk-verified)

- `book/src/L2/linear_combination.md` (firm) and `book/src/L2/inner_product.md` (firm) **exist**,
  but each states it "does **not** replace the leaves" / is "the form they fuse *up* into, not
  a replacement" (`linear_combination.md:20,196-197`; `inner_product.md:21-22`). Under the
  redirect (§1d, §2 leaf-vs-fold reversal → fold/combinator-primary) this framing is exactly the
  drift to invert.
- The base-form leaves exist as **separate mirrored L2 entries**: `L2/{axpy,axpby,axpbypcz,scal,
  dot,nrm2}.md`, each a full chapter restating the same laws as L1/L3 under the (now-superseded)
  "Identity-lowerings still require both L levels" invariant.
- The thin degenerate lowerings exist: 6 `L3-L2/{axpy,axpby,axpbypcz,scal,dot,nrm2}-body-identity.md`
  + 6 `L2-L1/{...}-leaf-identity.md`. Each self-describes as "identity-in-form on the body, **no
  wrapper to rotate**" (e.g. `axpy-body-identity.md:3-14`) — the textbook degenerate
  identity-in-named-terms lowering the redirect §1d calls a smell.
- **NO `L3/linear_combination` or `L3/inner_product` exists.** `grep linear_combination book/src/L3/axpy.md`
  = 0 matches. The combinator was lifted once at L2 and never propagated up — mine-and-strand.
- The combinators' **own** lowering themes — `L2-L1/linear-combination-fold-specialization.md`
  (arity-dispatch + pinned summation order) and `L2-L1/inner-product-fold-specialization.md`
  (conjugation/element-type/weight dispatch + the `xᴴy`↔`yᴴx` re-order) — are **substantive
  translations, NOT degenerate**; they STAY (re-audited, not demoted).
- L4 entries referencing base forms (propagation targets for c050): `L4/krylov-step.md`,
  `L4/chebyshev.md`, and three L4>L3 themes.

## Dispatches

### D1 — combinator-miner — `refactor-pass-linear-combination-family` (LEAD)
- **agent**: `combinator-miner`
- **scope**: Author the replace-and-propagate map for the `linear_combination` family
  (`scal`/`axpy`/`axpby`/`axpbypcz`) AND enact the L2-entry inversion. (a) Invert
  `book/src/L2/linear_combination.md` from "the fold does NOT replace the leaves / the form they
  fuse up into" to **combinator-as-entry**: the combinator is the L2 layer's primary entry for
  this family; the four leaves become **specialization notes under it** (arity-1/2/2/3
  specialization identities, retained as notes, not as standalone mirrored chapters). (b) Author
  the authoritative replace-and-propagate map (in the report, for c050 enactment): which L2 leaf
  entries (`L2/{scal,axpy,axpby,axpbypcz}.md`) collapse into specialization notes; the 4
  `{axpy,axpby,axpbypcz,scal}-body-identity` (L3>L2) + 4 `-leaf-identity` (L2>L1) themes flagged
  degenerate-smell → demote-to-in-line; the **L3 propagation plan** (author `L3/linear_combination`
  as the L3 layer's combinator entry, re-express the L3 leaf cohort *through* it rather than as
  re-derived base form); the L4 propagation note (`krylov-step`/`chebyshev` express through the
  combinator). (c) Re-audit the `linear-combination-fold-specialization` L2>L1 lowering under the
  1c translation test — it is substantive (arity-dispatch + pinned summation order), so it reads
  as a genuine translation and **STAYS** (record the verdict). Leaf-collapse + L3-combinator
  authoring + theme-demotion enactment are c050 (do NOT enact them this cycle — they depend on
  this map AND the D3 worklist).
- **deps**: none (wave 1).
- **rationale**: Redirect program item 1 (highest priority); redirect §4 combinator-miner
  re-mandate (replace-and-propagate, not mine-and-strand). HIGH fan-out — the corrected shape is
  the foundation everything else rests on. The family is on-disk-identified; the deliverable is
  the framing inversion + the map, per the redirect routing (combinator-miner first).

### D2 — combinator-miner — `refactor-pass-inner-product-family`
- **agent**: `combinator-miner`
- **scope**: Same as D1 for the `inner_product` family. (a) Invert `book/src/L2/inner_product.md`
  to combinator-as-entry; the members (`dot`/`tdot` Hermitian/unconjugated, `bilinear-form`
  M-weighted) become specialization notes under it. (b) Map: collapse `L2/{dot,nrm2}.md` —
  **NOTE `nrm2` is a CONSUMER-of `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`), NOT a fold
  member**, so its treatment differs from `dot` (record whether `nrm2` becomes a consumer-note
  under the combinator or stays a thin standalone consumer entry — combinator-miner judgment,
  state the rationale); the `dot`/`nrm2` `-body-identity` (L3>L2) + `-leaf-identity` (L2>L1)
  themes degenerate-smell → demote-to-in-line; the L3-propagation plan for `L3/inner_product`.
  (c) Re-audit `inner-product-fold-specialization` (conjugation/element-type/weight dispatch +
  the `xᴴy`↔`yᴴx` value-level re-order) as a substantive translation — KEEP. Enacts the
  `inner_product` L2-entry inversion this cycle; leaf-collapse + L3 enactment → c050.
- **deps**: none (wave 1; non-overlapping with D1 — see Overlap analysis).
- **rationale**: Redirect program item 1; the second of the two named fold families
  (`dot`/`nrm2` → `inner_product`). HIGH fan-out. The `nrm2`-is-a-consumer nuance is the one
  genuine design judgment in this dispatch and must be made explicitly.

### D3 — cross-layer-cross-cutter — `refactor-pass-degenerate-lowering-audit` (AUDIT-FIRST)
- **agent**: `cross-layer-cross-cutter`
- **scope**: Observation-only re-audit (no `book/` mutation) of the full thin-theme cohort
  against the redirect 1c/1d translation/smell test. For the **12 leaf themes**
  (`L3-L2/{axpy,axpby,axpbypcz,scal,dot,nrm2}-body-identity.md` +
  `L2-L1/{...}-leaf-identity.md`): confirm each is a degenerate identity-in-named-terms lowering
  (the smell — each self-describes "no wrapper to rotate / identity on the body"), and classify
  the resolution per 1d: (i) demote-to-in-line note vs (ii) absorb-into-combinator-specialization
  -note. For the **NON-leaf substantive themes** confirm they are GENUINE translations that STAY:
  `krylov-step-body-identity` (real wrapper rotation — `(op,K,s)`→`IterState` + outer-loop
  dissolution), `orthogonalize-variant-split`, the four substantive L3>L2 erasure themes
  (`ksp-solve-outer-driver`, `chebyshev-nested-recurrence`, `eigsolve-opaque-eigen-iteration`,
  plus `orthogonalize-variant-split`), and the two `*-fold-specialization` L2>L1 themes (the
  combinators' own substantive lowerings). Produce the **demotion worklist** (which theme files
  delete/inline, which stay) that the c050 abstractor/lifter enactment consumes. Cross-reference
  the D1/D2 maps for the family-specific demotion calls (forward-reference only — D1/D2 are
  wave-1 siblings; this audit is the cohort-wide cross-check that the per-family maps are
  consistent and complete).
- **deps**: none operationally (observation-only; reads the same files D1/D2 read but writes no
  `book/`); see Overlap analysis for why this is parallel-safe with D1/D2.
- **rationale**: Redirect §3 ("re-audit every lowering touched under 1c/1d"). MEDIUM fan-out —
  organizes the theme-demotion enactment into a single worklist so c050 doesn't re-derive the
  classification per-theme. Audit-first framing (per the cycle-planner discipline bullet:
  cross-cutting cohort question → prefer audit-first over reflexive harvest) is correct here:
  the question "which of these 12+ themes are degenerate-smell vs genuine-translation" is a
  cohort-boundary classification, exactly the cross-layer-cross-cutter's job.

## Overlap analysis

Pairwise:

- **D1 ↔ D2**: NON-overlapping. D1 modifies `book/src/L2/linear_combination.md` (+ produces a map
  for the `scal`/`axpy`/`axpby`/`axpbypcz` family); D2 modifies `book/src/L2/inner_product.md` (+
  maps the `dot`/`nrm2` family). Disjoint file sets, disjoint operator families. The two
  combinators are explicit do-NOT-merge siblings (each entry's §"Sibling fold" cross-references
  the other, but neither dispatch rewrites the other's chapter). The only shared touch-point is
  the reciprocal §"Sibling fold" cross-reference paragraph in each combinator — but each dispatch
  edits **its own** entry's paragraph (D1 edits `linear_combination.md`'s "dot is not subsumed"
  note; D2 edits `inner_product.md`'s "linear_combination is not subsumed" note). PARALLEL.
- **D1 ↔ D3**: NON-overlapping at the artifact level. D3 is observation-only (writes no `book/`).
  D3 reads the same `L3-L2/*-body-identity.md` / `L2-L1/*-leaf-identity.md` files that D1's map
  *references* (forward-references for c050 enactment), but D1 does NOT mutate those theme files
  this cycle (the demotion is c050 enactment). No write-write or write-read conflict. PARALLEL.
- **D2 ↔ D3**: same as D1↔D3. D3 observation-only; D2 mutates only `inner_product.md`. PARALLEL.

No dispatch modifies the same operator entry or rewrites the same theme body as another. No
shared running-count / consolidated index tally is co-written: the L2/index, L3-L2/index,
L2-L1/index `firm`-count tallies are **NOT touched this cycle** (the leaf entries are not
collapsed and the themes are not demoted until c050; the c049 dispatches mutate only the two
combinator chapter bodies + produce maps/worklists). The count-ownership / dual-registration
partition is therefore **not triggered** this cycle (it applies only where ≥2 dispatches co-write
one index; here zero index tallies are written). This is consistent with the redirect's note that
the rectangular-floor count machinery is retired-as-a-target and useful only where genuine
co-writes occur.

No canonical-slug forward-reference coordination is needed: D1/D2 reference EXISTING slugs
(`linear_combination`, `inner_product`, and the existing leaf/theme files); no dispatch authors a
new not-yet-existing slug that a sibling references this cycle. (The new `L3/linear_combination` /
`L3/inner_product` slugs are c050 deliverables, named in the D1/D2 maps but not authored this
cycle, so no cross-report slug-divergence risk fires.)

## Sequencing schedule

**Single wave (all parallel).** D1, D2, D3 are mutually non-overlapping (Overlap analysis above):
two disjoint-file combinator-entry inversions + one observation-only audit. All three run in
wave 1.

- **Wave 1 (parallel)**: D1 (combinator-miner, `linear_combination` family), D2 (combinator-miner,
  `inner_product` family), D3 (cross-layer-cross-cutter, degenerate-lowering audit).

Then the standard per-dispatch pipeline: 3 critics (parallel) → repairers as needed (parallel) →
`integrator-per-report` ×3 (serial) → ONE `integrator-finalize` (rebuild + commit + push). No
inter-wave book rebuild; one finalize at cycle end.

## Deliverable-presence verification

Per the mandatory pre-dispatch four-step check (paste-inline-evidence). All three dispatches are
either open-by-construction (the framing-inversion of an entry under a brand-new directive is not
a re-proposal of landed work) or verified below.

### D1 — `book/src/L2/linear_combination.md` (combinator-entry inversion)
1. **File existence**: `ls -la book/src/L2/linear_combination.md` →
   `-rw-rw-r-- 1 crutcher crutcher 23042 May 28 16:36 book/src/L2/linear_combination.md` (EXISTS).
2. **Maturity / already-discharged**: `grep -m1 "^## Status" book/src/L2/linear_combination.md` →
   `## Status` line present; entry is `firm`. The proposed dispatch is NOT a no-op: the entry is
   firm under the OLD "does NOT replace the leaves" framing (`linear_combination.md:20,196-197`);
   D1's deliverable is the **framing inversion to combinator-as-entry** under the 2026-06-01
   redirect — a new directive issued AFTER this entry was authored (2026-05-28). Open by the
   redirect.
3. **OQ-ledger RESOLVED-grep**: `grep -i -E "refactor|combinator.*collapse|vocabulary-shift"
   scaffolding/open-questions.md` → no RESOLVED/CLOSED entry for a refactor-pass /
   combinator-collapse slug (the only matches are the batch-unification headers; no
   `refactor-pass-linear-combination-family ... RESOLVED`). The refactor pass is fresh intake from
   the 2026-06-01 redirect; nothing closed.
4. **Structural block**: none. The redirect explicitly mandates this work (§2 leaf-vs-fold
   reversal → fold/combinator-primary; §3 refactor pass; §4 combinator-miner replace-and-propagate)
   and routes it `combinator-miner` first. No blocking methodology gate. NOT on the STOP-PROPOSING
   negative list (`linear_combination` ≠ `lu_solve`/`back_solve`/`ls-update-column`/NLEPS-atoms/
   `apply_nonlinear_pencil`).

### D2 — `book/src/L2/inner_product.md` (combinator-entry inversion)
1. **File existence**: `ls -la book/src/L2/inner_product.md` →
   `-rw-rw-r-- 1 crutcher crutcher 33181 May 29 10:04 book/src/L2/inner_product.md` (EXISTS).
2. **Maturity / already-discharged**: `grep -m1 "^## Status" book/src/L2/inner_product.md` →
   `## Status` present; `firm` under the OLD "fuse up into, not a replacement" framing
   (`inner_product.md:21-22`). NOT a no-op — D2's deliverable is the redirect-mandated inversion.
   Open by the redirect (entry authored 2026-05-29, redirect issued 2026-06-01).
3. **OQ-ledger RESOLVED-grep**: same as D1 — no `refactor-pass-inner-product-family ... RESOLVED`
   entry. Fresh intake.
4. **Structural block**: none (redirect-mandated). NOT on the STOP-PROPOSING list.

### D3 — degenerate-lowering audit (observation-only; no named-artifact deliverable to pre-check)
- D3 produces an observation/worklist, mutates no `book/` artifact, and authors no new slug.
  Open by construction (a fresh cross-cutting audit under a brand-new directive, no prior-cycle
  history). The audit targets — the 12 leaf themes — are verified present:
  `ls book/src/L3-L2/{axpy,axpby,axpbypcz,scal,dot,nrm2}-body-identity.md` → all 6 present;
  `ls book/src/L2-L1/{axpy,axpby,axpbypcz,scal,dot,nrm2}-leaf-identity.md` → all 6 present.
  The audit reads existing files; there is no risk of re-proposing landed work (no prior
  degenerate-lowering audit exists — this is the first under the redirect).

**STOP-PROPOSING negative-list check (all picks)**: none of `linear_combination`, `inner_product`,
`axpy`/`axpby`/`axpbypcz`/`scal`/`dot`/`nrm2` (leaves or themes) appears on the negative list
(`lu_solve`, `back_solve`, `ls-update-column`, the 4 NLEPS atoms) and none is `apply_nonlinear_pencil`
(HELD). Clear.

## Open questions / caveats

- **Cycle-049 is map-led, not enactment-heavy.** Only 3 dispatches, and the only `book/` mutations
  this cycle are the two combinator-entry framing inversions (D1/D2). The visible artifact delta
  is small relative to the refactor's total scope; this is intentional for a first refactor cycle
  (the redirect routes combinator-miner FIRST to lay out the replace-and-propagate plan before
  harvester/abstractor/lifter enact). The bulk delta lands c050. If the orchestrator/meta-phase
  prefers more enactment in c049, the cleanest add would be a wave-2 `harvester` collapsing ONE
  L2 leaf family slice into specialization notes once D1's map lands — but I have deliberately NOT
  scheduled it, because the leaf-collapse design (do the leaves become inline notes in the
  combinator chapter, separate stub chapters, or deleted-with-redirect?) is precisely what D1/D2's
  maps must decide first; enacting before the map risks a re-do. Flagging for the orchestrator's
  discretion.

- **`nrm2`-is-a-consumer-not-member is the one genuine design fork in this cycle.** `nrm2` is
  `√ ∘ abs ∘ inner_product` at `y=x` (a consumer), not a fold member. Whether it collapses into
  an `inner_product` consumer-note or stays a thin standalone consumer entry is a D2 judgment call
  I have left to the combinator-miner (with a mandate to state the rationale). If D2 and D3
  disagree on `nrm2`'s disposition, that surfaces as an integrator wave-conflict signal next cycle
  — acceptable per the conflict-tolerance philosophy (mark parallel when in doubt).

- **The `*-fold-specialization` themes must NOT be swept up in the demotion.** Both D1/D2 and D3
  are instructed that `linear-combination-fold-specialization` and `inner-product-fold-specialization`
  are SUBSTANTIVE translations (arity-dispatch / conjugation-dispatch), not degenerate smells —
  they STAY. This is the one place a careless "demote all the thin themes" reading could destroy
  load-bearing content (the pinned-summation-order / `xᴴy`↔`yᴴx` re-order facts live in those
  themes). Both the D1/D2 scopes and the D3 scope call this out explicitly. Critics should verify
  these two themes are NOT on any demotion worklist.

- **Methodology-adjustment candidate for the batch-15 meta-phase (fires after c051), not yet in any
  ledger.** The refactor pass needs a settled convention for **what a collapsed leaf becomes**:
  (a) an in-line specialization note inside the combinator chapter, (b) a thin stub chapter
  redirecting to the combinator, or (c) a deleted chapter with the SUMMARY.md row removed. D1/D2
  will each make a per-family call this cycle; if they diverge, the meta-phase should ratify ONE
  convention cohort-wide (analogous to the batch-12 leaf-vs-fold-fork ratification, but now in the
  opposite — combinator-primary — direction). I have noted this here rather than appending a fresh
  plan candidate because the convention can't be chosen until D1/D2 surface the options from the
  actual collapse work. Surfacing for the next meta-phase.

- **No `apply_nonlinear_pencil` / NLEPS / direct-solver work touched** — STOP-PROPOSING list and
  HELD items untouched, consistent with the refactor-pass-first ordering (those are forward-frontier
  candidates, which the redirect explicitly subordinates to the refactor pass).
