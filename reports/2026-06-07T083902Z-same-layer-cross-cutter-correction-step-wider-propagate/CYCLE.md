---
agent: same-layer-cross-cutter
invoked_at: 2026-06-07T083902Z
scope: cycle-123 D3 — correction_step wider replace-and-propagate (confirm-propagation-or-record-closure-rationale)
status: pending
integrated_at: 2026-06-07T083902Z
integration_commit: e79fb8c
integration_notes: "Applied clean (D3, PURE OBSERVATION — no book/ edit, no ## Proposed changes). Closed 2 OQs (correction-step-wider-replace-and-propagate-set-l1-and-feature-column c122 + correction-step-replace-and-propagate-scope c121 transitive) + promoted NEW OQ correction-step-l4-reference-edge-adds-to-reference-only-reachable-liveness-evidence (the candidate L4 correction_step reference down-link as COMPLEMENTARY reference-only-reachable meta-evidence; NOT enacted this cycle). Feeds the batch-39 meta reference-edge-liveness adjudication (complementary to the D2 depends-on flip). Batch-39 BATCH-CLOSING finalize."
---

# CYCLE: L2 observation — correction_step wider propagation reaches the L1 smoother + GMG columns as a DOWNWARD annotation, not a depends-on edge

## Summary

Comparing the firm `L2/correction_step` combinator (`y + B·(x − A·y)`) against the three
routed wider-propagation consumers — `L1/multigrid-relaxation-smoother`, the GMG V-cycle
feature column (`feature/geometric-multigrid-preconditioner.{L4,L1}.md`), and the
distributive-relaxation L1 form (which lives *inside* `multigrid-relaxation-smoother`) — I
confirm the c121-miner's read: **every one of these sites is a genuine structural
`correction_step` instance** (the primary leg `y + B(x−Ay)`, and the auxiliary/coarse-grid
leg as the law-6 conjugated `B = T·B'·Tᵀ` with `T=G` / `T=P`). BUT the propagation cannot be
realized as a `depends-on` *edge* at the L1 sites: `correction_step` is an **L2** combinator
and `multigrid-relaxation-smoother` / the GMG-L1 column are **L1** entries — an L1 form is
defined in L1 vocabulary and cannot depend UP on an L2 abstraction (CLAUDE.md §"Layers are
defined high→low"; the well-foundedness invariant is a *rank* order, but the
layer-vocabulary-direction rule independently forbids an L1→L2 definitional edge). So the
correct resolution is **(b) record the closure rationale** for the L1 sites (the relationship
is a *downward annotation* — "this L1 sweep body lowers from / is the L1 realization of the
L2 `correction_step` with B = …"), and **(a) a real unification opportunity** for the **GMG
L4 column** (L4 *may* reference an L2 combinator — worth a `reference`-class down-link so the
V-cycle prose names `correction_step` as the per-sweep body it composes). This is the
replace-and-propagate (not mine-and-strand) integrity check landing as: the combinator
ALREADY names all four call sites in its own Specializations/§Semantics (no strand), and the
back-direction wiring is a downward annotation at L1 + a candidate L4 reference edge.

## Observation kind

**Shared sub-pattern** (the four sites reach for the same `correction_step` primitive) — but
the actionable surface is a **layer-direction-constrained reference-wiring** observation: the
unification is already DONE in the combinator's outward-facing roster; what remains is the
inbound back-links, which are constrained by the L1-can't-depend-up-on-L2 rule.

## Specific finding

The c122 D3 harvester routed three sites here (OQ
`correction-step-wider-replace-and-propagate-set-l1-and-feature-column`). Per-site verdict:

**1. `L1/multigrid-relaxation-smoother` — primary leg + conjugated auxiliary leg. → (b) DOWNWARD ANNOTATION, NOT an edge.**

The `Mult2` body (`distrelaxation.cpp:101-119`, verified via codemap read_range) is:

- primary leg `:104` `// y = y + B (x - A y)` then `B->Mult2(x, y, r)` — this IS
  `correction_step A B x y` (the B-slot = the primary Chebyshev point smoother).
- auxiliary leg `:108-117` `// y = y + G B_G Gᵀ (x - A y)` — residual `A->Mult(y,r);
  AXPBY(1.0,x,-1.0,r)` (`:109-110`), restrict `RealMultTranspose(*G,r,x_G)` (`:111`),
  ess-pin (`:112-115`), inner-relax `B_G->Mult2(x_G,y_G,r_G)` (`:116`), prolong-add
  `RealAddMult(*G,y_G,y)` (`:117`) — this IS `correction_step A (G·B_G·Gᵀ) x y` (law 6,
  conjugated `B = T·B'·Tᵀ` with `T = G`).

So the L1 smoother's per-sweep body is a *sequential composition of two `correction_step`
instances*. BUT `correction_step` is `L2/correction_step` (`layer: L2`, `rank: firm`) and
`multigrid-relaxation-smoother` is `layer: L1` (`rank: firm`). An L1 entry **must not**
`depends-on` an L2 combinator:
  - CLAUDE.md §"Layers are defined high→low; lifting notes go in working notes": an L_n
    operator entry's Semantics/Signature live in L_n vocabulary; defining it via *higher*-layer
    abstraction is a layer-direction violation.
  - The graded-stack well-foundedness invariant `rank(u) ≤ rank(v)` is about the maturity
    rank, not the L-layer; but the L-layer direction is an independent constraint. (Note: the
    L1 smoother already correctly `depends-on`s the firm L1 primitives `apply_linop` + `axpby`
    — the SAME two primitives `correction_step` decomposes into — so the L1 form is already
    well-grounded in L1 vocabulary; it does not NEED the L2 combinator to be defined.)

Faithful resolution: a **downward annotation** in the L1 smoother (prose + the existing
"Downward to lower layer" idiom), e.g. a one-line note in §Algebraic laws or §Context: "Each
per-sweep leg is the L1 realization of the L2 [`correction_step`](../L2/correction_step.md)
combinator — the primary leg with `B` = the primary point smoother, the auxiliary leg with
the law-6 conjugated `B = G·B_G·Gᵀ`." This is a `reference`-class navigational back-link
(downward-pointing prose), **not** a `depends-on` edge in the frontmatter `edges:` block. It
makes the relationship reviewable without inverting the layer direction.

**2. The distributive-relaxation L1 form. → SAME as #1 (it has no separate chapter).**

The dispatch banner lists "the distributive-relaxation L1 form" as a third site, but there is
no separate `L1/*distrelax*` chapter (confirmed by the planner's `ls` — not found);
distributive relaxation IS the `multigrid-relaxation-smoother` body (the auxiliary leg above).
So site #2 is subsumed by site #1 — one downward annotation covers both legs.

**3. The GMG V-cycle feature column (`feature/geometric-multigrid-preconditioner.{L4,L1}`). → (a) UNIFICATION OPPORTUNITY at L4; (b) downward annotation at L1.**

The V-cycle body (`gmg.cpp:172-205`, verified) per non-coarse level `l`:
  - pre-smooth `B[l]->Mult2(X[l], Y[l], R[l])` (`:184`) — `correction_step` (B = level smoother);
  - residual `A[l]->Mult(Y,R); AXPBY(1.0,X,-1.0,R)` (`:187-188`); restrict
    `RealMultTranspose(*P[l-1],R,X[l-1])` (`:191`); recurse `VCycle(l-1)` (`:196`); prolong-add
    `RealMult(*P[l-1],Y[l-1],R); Y[l] += R` (`:199-200`) — the coarse-grid correction is
    `correction_step A (P·B'·Pᵀ) x y` (law 6, conjugated `B = T·B'·Tᵀ` with `T = P`, `B'` =
    the recursive V-cycle);
  - post-smooth `B[l]->MultTranspose2(X,Y,R)` (`:204`) — `correction_step` (transposed B).

So the V-cycle is a **pre-smooth ▷ coarse-grid-correction ▷ post-smooth chain of three
`correction_step` instances**, exactly as the `correction_step` §"Conjugated preconditioner"
section already states (it cites `gmg.cpp:189-200` with `T = P`).

- **GMG-L1 column** (`level: L1`): same layer-direction constraint as #1 → **downward
  annotation** (its `vcycle` pseudo-code already uses `presmooth`/`postsmooth`/`axpby` — add a
  one-line note that each smooth step + the coarse-grid correction is the L2 `correction_step`
  with the named `B`). NOT a depends-on edge.
- **GMG-L4 column** (`level: L4`): L4 **CAN** reference an L2 combinator (downward in BOTH
  rank and L-layer). The L4 column's `vcycle` already spells `presmooth`/`residual`/
  `prolong_add`/`postsmooth` inline — this is the one site where naming `correction_step` as
  the composed per-sweep body is a *genuine reference-edge candidate* (a `reference`-class
  down-link `feature/geometric-multigrid-preconditioner.L4 → L2/correction_step`, kind
  `references`/`composes-step`). This would make the L4 V-cycle prose say "each smooth +
  coarse-grid correction is a [`correction_step`](../L2/correction_step.md)" rather than
  re-spelling the residual-correction skeleton — the conciseness-driven combinator-primary
  payoff. **This is the one true unification edge to flag for follow-up.**

**Over-unification guards — all respected (verified against the combinator's own §guards):**
the bare `B·X` preconditioner apply, the Krylov shift-invert `(K−σM)⁻¹Mv`, and the libCEED
`GᵀBᵀDBG` quadrature contraction are correctly EXCLUDED — none of the three routed sites is
one of those; every site has the full `x − A·y` residual + add-back skeleton. The
`divfree-projector` borderline (A=I / no external x) is also correctly out and not among the
routed set.

## Recommendation

ONE observation, three follow-up candidates (none enacted here — I surface; harvester /
combinator-miner / layer-intro-author enact):

1. **(L4 reference edge — the real unification follow-up) Dispatch `combinator-miner` or
   `layer-intro-author` to add a `reference`-class down-link** from
   `feature/geometric-multigrid-preconditioner.L4.md` → `L2/correction_step`, and reword the
   L4 `vcycle` pseudo-code prose so pre-smooth / coarse-grid-correction / post-smooth each
   NAME `correction_step` (with the conjugated `B = P·B'·Pᵀ` for the coarse-grid leg). This is
   the replace-and-propagate completion at the one site where the layer direction permits an
   edge — and it is the combinator-primary conciseness win.

2. **(L1 downward annotations — closure rationale, NOT edges) Dispatch `harvester` (or fold
   into a layer-intro-author pass)** to add a one-line *downward annotation* (prose +
   `reference`-class navigational link, NOT a `depends-on` edge) to BOTH `L1/multigrid-relaxation-smoother`
   and `feature/geometric-multigrid-preconditioner.L1.md`, naming each per-sweep leg as the L1
   realization of `L2/correction_step` with its `B`-slot. Explicitly RECORD that no
   `depends-on` edge is created (L1 cannot depend up on L2) — the relationship is downward.

3. **(No new combinator; no strand) CONFIRM the replace-and-propagate is complete on the
   outward face:** `L2/correction_step` already names all four call sites (gmg /
   distrelaxation / chebyshev / jacobi) in its §Semantics + §Specializations + §Evidence — so
   this is NOT mine-and-strand. The only residual work is the inbound back-links (items 1-2).
   Close OQ `correction-step-wider-replace-and-propagate-set-l1-and-feature-column` with this
   verdict: propagation reaches all consumers; the wiring is 1 L4 reference edge + 2 L1
   downward annotations, constrained by the layer direction.

## Supporting evidence

- `book/src/L2/correction_step.md` — the combinator (firm); §"Conjugated preconditioner"
  (the law-6 `B = T·B'·Tᵀ`, T=G distrelaxation / T=P coarse-grid), §Specializations (Jacobi /
  Chebyshev / Distributive-coarse-grid), §"Over-unification guards", §Evidence (names
  `gmg.cpp:176/184-188/189-200`, `distrelaxation.cpp:104/108-117`, `chebyshev.cpp:193/264`,
  `jacobi.cpp:90-93`). The outward roster is already complete.
- `book/src/L1/multigrid-relaxation-smoother.md` — `layer: L1`, `rank: firm`; §Signature
  (`y := y + B(x−A·y)` primary, `y := y + G·B_G·Gᵀ(x−A·y)` auxiliary), `depends-on`
  `apply_linop` + `axpby` (the same primitives `correction_step` decomposes into). `grep -c
  correction_step` = 0 (no back-link yet).
- `book/src/feature/geometric-multigrid-preconditioner.L1.md` — `level: L1`; the `vcycle`
  pseudo-code (presmooth / `axpby` residual / restrict / recurse / prolong-add / postsmooth).
  `grep -c correction_step` = 0.
- `book/src/feature/geometric-multigrid-preconditioner.L4.md` — `level: L4`; the `vcycle`
  combinator pseudo-code (presmooth / residual / restrict / recurse / prolong_add /
  postsmooth) — the L4 site where a `reference`-class `correction_step` down-link is the real
  edge candidate.
- `reference/palace/palace/linalg/gmg.cpp:172-205` (codemap read_range, verified) —
  `VCycle`: pre-smooth `B[l]->Mult2` (:184), residual `A[l]->Mult; AXPBY(1.0,X,-1.0,R)`
  (:187-188), restrict `RealMultTranspose(*P[l-1],R,X[l-1])` (:191), recurse `VCycle(l-1)`
  (:196), prolong-add `RealMult(*P[l-1],Y[l-1],R); Y[l] += R` (:199-200), post-smooth
  `B[l]->MultTranspose2` (:204). The verbatim contract comment "compute Y <- Y + B (X - A Y)"
  at :176.
- `reference/palace/palace/linalg/distrelaxation.cpp:101-119` (codemap read_range, verified) —
  `Mult2`: sweep loop (:102), primary `// y = y + B (x - A y)` + `B->Mult2(x,y,r)` (:104-106),
  auxiliary `// y = y + G B_G Gᵀ (x - A y)` + `A->Mult(y,r); AXPBY(1.0,x,-1.0,r)` (:108-110),
  restrict `RealMultTranspose(*G,r,x_G)` (:111), ess-pin (:112-115), inner-relax
  `B_G->Mult2(x_G,y_G,r_G)` (:116), prolong-add `RealAddMult(*G,y_G,y)` (:117).

## Open questions / caveats

- **The L4 reference edge adds to the reference-edge-liveness evidence corpus the batch-39
  meta is adjudicating.** A `feature/...L4 → L2/correction_step` `reference`-class edge is the
  SAME edge shape (navigational, free, NOT traversed by the depends-on-only GC) as the
  combinator-primary / DIRECTIVE-3 / GMG cross-links the c122 finalize flagged. If the L4
  follow-up edge lands, `L2/correction_step` (currently a STRONGER reference-only-reachable
  node per the c123 plan's RE-recheck) gains *another* reference-only inbound edge — it does
  NOT become depends-on-reachable. Surface this to the meta: the correction_step
  back-propagation is a clean instance of "a faithful combinator reference produces a
  reference-only-reachable node", reinforcing the scheme question (a `reference`-to-reachable
  liveness rule would make `correction_step` show reachable; the current GC keeps it STRONGER).
  This is intentional evidence, not a defect.

- **Should item-1 (the L4 edge) be a `reference` or could the L4 column genuinely `depends-on`
  `correction_step`?** Judgment call for the enacting agent: the GMG L4 column's *blocking*
  composition is already via `preconditioning-framework` + the V-cycle structure + the
  smoother/prolongation constituents; `correction_step` is the *per-sweep body shape* the
  V-cycle composes, which reads more like a `reference` (navigational "this is the step we
  iterate") than a build-blocking dep. I lean `reference` (matches how the L4 column already
  types its `L3/chebyshev` / `L2/jacobi-smoother` iteration-views as `reference`), but the
  combinator-miner/layer-intro-author should confirm against the OWN-COMPOSITION rule. If
  `depends-on`, the well-foundedness check is firm(L4) ≤ firm(L2 correction_step) — holds.

- **Is the L1 downward-annotation the right mechanism, or should the L1 smoother's L1>L0 /
  L1→L2 *lifting* note carry it?** The combinator's own §"L2 vs lower-layer distinction"
  already states "There is no L1 `correction_step` primitive — the body is realized
  per-smoother". The cleanest framing: the L1 smoother gets a downward navigational note, and
  the *upward* lift relationship (this L1 body lifts to the L2 combinator) lives in working
  notes / the L1→L2 direction — consistent with "Reverse-direction notes live in working
  notes, NOT formal chapter content". The enacting agent should keep the L1 chapter edit to a
  bare navigational back-link (downward prose), not an upward-lift narrative.

- **No new friction pattern.** This is a textbook combinator-primary replace-and-propagate
  completing correctly, with the layer-direction rule doing exactly its job (preventing an
  L1→L2 inversion). Nothing warrants a friction-ledger entry beyond the already-flagged
  reference-edge-liveness scheme question.
