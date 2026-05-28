---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T14:56:39Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: warning
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-28T15:10:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: unrepairable
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: combinator-miner
---

# META: verification of "Formalize chebyshev at L3 and L4"

## Critique

### Checks run

**citation-validity — pass.** Every claim carries a pointer and the sampled
pointers are in-range and accurate. Verified via codemap `read_range` against the
live Palace tree:

- `palace/linalg/chebyshev.cpp:191-220` (4th-kind `Mult2`) — exact match: the
  `for (int it = 0; it < pc_it; it++)` outer sweep, the
  `initial_guess || it > 0` branch with `r = x; y = 0.0` degenerate path,
  `ApplyOrder0(4.0/(3.0*lambda_max), …)`, the `k`-loop with `y += d`,
  `ApplyOp(*A, d, r, -1.0)`, `sd = (2k-1)/(2k+3)`, `sr = (8k+4)/((2k+3)·λ_max)`,
  `ApplyOrderK`, trailing `y += d`. Transcription is faithful.
- `palace/linalg/chebyshev.cpp:261-293` (1st-kind `Mult2`) — exact match:
  identical sweep scaffold, `ApplyOrder0(1.0/theta, …)`, `rhop = delta/theta`,
  `rho = 1.0/(2.0*theta/delta - rhop)`, `sd = rho*rhop`, `sr = 2.0*rho/delta`,
  `rhop = rho`. The "variant-invariant body sequence" (law 5) is genuinely
  witnessed by the identical scaffold across the two bodies.
- `palace/linalg/chebyshev.hpp:14-23` — the 4th-kind class doc comment carrying
  the Phillips & Fischer arXiv:2210.03179v1 (2022) reference is at lines 18-20,
  in-range; class decl follows. Accurate.
- `palace/linalg/chebyshev.hpp:72-75` — the `MultTranspose2(...) { Mult2(x, y, r);
  // Assumes operator symmetry }` alias body. Minor offset: the alias spans lines
  73-76 (line 72 is blank in the read), but lines 73-75 (`void MultTranspose2`,
  `{`, `Mult2(x,y,r)`) ARE within the cited 72-75 range, so the symmetry-alias
  claim (law 3 / law 4 witness) is in-range.
- `palace/linalg/chebyshev.hpp:80-114` — the 1st-kind class doc (Adams et al. JCP
  2003) + decl + `double theta, delta, sf_max, sf_min;` (member at line 105). All
  in-range and accurate.
- `palace/linalg/chebyshev.hpp:37` — `// Inverse diagonal scaling … (real-valued
  for now)` at line 37, `VecType dinv;` at 38. The "dinv real-valued even for
  complex A" element-type note is grounded.
- Slice ranges `book/src/spec/slices/chebyshev.md:229-285` (§L3) and `:287-439`
  (§L4) — confirmed: §L3 begins at line 229, §L4 at 287; file is 439 lines.
- Strawman `§2` (line 84), `§3.7` (line 150), `§3.8` (line 186) — all in-range.
- The "Phillips & Fischer 2022 §2" usage is consistent with the sibling L2 entry
  and slice §L3 (line 276) — used identically as a literature anchor for the
  recurrence's numerical-stability motivation, NOT as a positive-source
  substitute for the body (see surface-or-evidence). All sampled citations pass.

**surface-or-evidence — pass.** This is a forward-frontier harvest authoring two
NEW operator entries (L3 + L4), not a refinement of existing surface — so the
refinement-shaped surface+rotation_claim gate is not the governing case. The
body's algebraic content is grounded in positive Palace source
(`chebyshev.cpp:191-220, :261-293`); the literature anchor (Phillips & Fischer
2022 §2) is correctly used only to justify the *non-removability* of the
sequential obstruction, not to assert a positive constructive claim. This is
proper anchor usage (anchor for obstruction-rationale, positive-source for the
body), distinct from a load-bearing positive-source substitute. Pass.

**rotation-quality — warning.** The L3 rotation is sound: the per-step body lifts
to whole-tensor field arithmetic (strictly more abstract than the L2/L0
element-fused `ApplyOrder0`/`ApplyOrderK` kernels — those are explicitly recorded
as transparent fusions below L3's level), while the surrounding loop structure is
honestly recorded as a `partial-obstruction`. That is a genuine rotation, not a
1:1 rename. **However**, the L4 rotation introduces two iteration combinators —
`forM_` (outer `pc_it`) and `foldM` (inner `k`) — that are NOT part of the
established firm L4 vocabulary and are NOT more compact than the existing
canonical primitive. The firm L4 layer already carries `iterate-while` and
`iterate-while-with-prev` (cycle-007), and `book/src/L4/iterate-while.md:7`
explicitly declares `iterate_while` the "canonical iteration primitive at L4"
that "every iterative algorithm in the spec (CG, GMRES, **Chebyshev**, Arnoldi,
…) reduces at L4 to". The strawman §6 (worked example, lines 414-418) maps a
bounded `for t_idx in 1..=k` loop to `iterate_while_pure` with a step-count
predicate — i.e., the strawman's own answer for bounded iteration is
`iterate_while_pure`, not `forM_`/`foldM`. The L4 chebyshev entry therefore
proposes a *parallel* iteration vocabulary that competes with, rather than reuses
or strictly refines, the layer's existing abstraction. This is the central
rotation/abstraction-quality concern. (Mitigating: `forM_`/`foldM` are not
freshly invented by this dispatch — they are promoted verbatim from the
cycle-001-era slice §L4, lines 289/325/396-397; see plan-kind-consistency. The
warning is that the promotion did not reconcile the slice's pre-redirect
combinators against the now-firm `iterate-while` family.)

**variant-axis-coverage — pass.** Both axes are explicitly enumerated and either
covered or scoped at both layers: (1) polynomial-kind (Chebyshev-4th /
Chebyshev-1st) absorbed at level (c) into `op.scalars`/`scalarInit` (L3) and the
distinct closure types `ChebOp E Unit` / `ChebOp E { rho_prev: E }` (L4); (2)
element-type (real/complex) dispatched at the primitive level, with the
real-valued-`dinv` and complex-transpose-dead-code caveats called out. The
non-axes are explicitly distinguished from axes: `order`/`pc_it` (construction
parameters, not selectors), `initial_guess` (a per-call `Bool` degenerate-case
absorption, with an explicit argument for NOT over-absorbing it into the closure
lattice — a correct application of variant-absorption discipline), and the
spectral-bound-estimation method (setup-side). No hidden branches: the body
genuinely does not branch on kind, confirmed against both `Mult2` source bodies.
Pass.

**cross-reference-integrity — warning.** All concept slugs resolve
(`sequential-obstruction`, `tensor-field-lift`, `elementwise-product`,
`variant-absorption`, `derived-view-hoisting`, `first-iteration-unrolling`,
`constructed-operators`, `chebyshev-iteration`, `state-stratification`,
`solve-monad` all exist under `book/src/concepts/`). All sibling operator slugs
resolve (`L1/chebyshev-smoother`, `L2/chebyshev-iteration`, `L3/krylov-step`,
`L4/krylov-step`, `L3/{apply_linop,axpy,axpby,axpbypcz,scal,dot,nrm2}`). The
warning is two-fold: (a) the L4 entry and both L4 index-edit instructions
reference `forM_` and `foldM` as L4 combinators, but **neither has an L4 row or a
concept page** — they are dangling vocabulary references at a layer that
otherwise anchors its iteration combinators (`iterate-while`,
`iterate-while-with-prev` are firm rows; `krylov-step`'s dep-map lists its L4-row
dependencies explicitly). The L4 chebyshev dep-map row asserts "L4 rows: none
consumed", which is internally consistent with the entry but leaves `forM_`/
`foldM` un-anchored and contradicts `iterate-while.md:7`'s claim that Chebyshev
reduces to `iterate_while`. (b) Minor: the L3 index-edit instruction says "after
the `scal` row, line 28", but in the current `book/src/L3/index.md` the `scal`
row is the *last* row of the dep-map at a line well past 28 (line 28 is the
`axpby` row); the integrator should place the new row after the actual last row,
not at line 28. The report does delegate exact positioning to the integrator, so
this is a low-severity drift, not a blocker.

**edge-label-fidelity — pass.** Every edge label matches its prose. The L3
entry's §Upward discusses the L4>L3 edge (typed-wrapper dissolution), §Downward
discusses the L3>L2 edge (body identity-in-form), and the "Non-adjacent identity"
block discusses the L3>L1 transitive composition (L3>L2 ∘ L2>L1) — each edge's
prose matches its label. The frontmatter `lowers_to`/`lifts_from` directions are
correct (L3 lowers to L2, lifts from L4). The L4 entry's "L4 > L3" /"L3 > L2"
blocks each narrate the correct edge. No L_{n+1}→L_n / prose mismatch found.

**plan-kind-consistency — warning.** The L3 entry's declared status
`partial-obstruction` matches its content shape exactly (firm body lift + named,
cited loop-structure obstruction) — this is well-classified, and the report
correctly distinguishes it from the cycle-012 `partly-constructive` status (OQ 3).
The concern is the L4 entry's `firm` declaration. Its content is a faithful, clean
re-typing of the cycle-012 firm L1/L2 entries AND a verbatim promotion of the
cycle-001-era slice §L4 — but it carries an un-reconciled vocabulary choice
(`forM_`/`foldM` vs. the firm `iterate-while` family) that the report itself
flags as an open question for the lowering-verifier (OQ 1, "L4>L3 chebyshev theme
file (not authored)"). A `firm` L4 operator whose iteration combinators are
neither anchored as L4 rows nor reconciled with the layer's canonical primitive
sits closer to a rough-in-at-the-wrapper / firm-at-the-body shape than a
fully-firm entry. Whether to (i) re-express via `iterate-while_pure` with a
count predicate (strawman-conformant), (ii) promote `forM_`/`foldM` as firm L4
rows, or (iii) keep them and downgrade the entry's firmness, is a judgment call —
flagged for the repairer/integrator/lowering-verifier, not decided here.

**skill-uptake-survey — warning (telemetry only).** The report references
`skills/phase-1-slice-reduction-audit` for the slice-reduction follow-up (OQ 2),
which is appropriate. But this is a rotation- and variant-axis-heavy harvest, and
the report does not reference invocation of `verify-citation-range` (despite
citing many source ranges — though they do verify out), `verify-rotation-citation`
/ `propose-rotation` (despite asserting an L3 iteration rotation), or
`classify-variant-axis` (despite a two-axis enumeration at both layers). Pure
presence check; non-blocking telemetry that the available rotation/variant skills
were not surfaced in the report's procedure trail.

### Issues found

1. **[L4/chebyshev.md §Signature/§Semantics; L4 index-edits] — `forM_`/`foldM`
   are un-anchored L4 vocabulary that competes with the canonical `iterate-while`
   family. Severity: medium.** The firm L4 layer declares `iterate-while` the
   canonical iteration primitive and explicitly names Chebyshev as one of its
   consumers (`book/src/L4/iterate-while.md:7`). The strawman maps bounded loops
   to `iterate_while_pure` with a count predicate (`book/src/design/l4_calculus.md`
   §6, lines 414-418). The L4 chebyshev entry instead introduces `forM_` (outer)
   and `foldM` (inner) with no L4 row and no concept page, and its dep-map asserts
   "L4 rows: none consumed". This is the dominant cross-reference-integrity +
   rotation-quality + plan-kind-consistency concern. Note this is a faithful
   promotion of the cycle-001-era slice §L4 (`book/src/spec/slices/chebyshev.md:289,
   325, 396-397`), so it is not a fabrication — but the promotion did not
   reconcile the pre-redirect slice combinators against the now-firm
   `iterate-while`/`iterate-while-with-prev` vocabulary. Candidate repairs:
   re-express the bounded loops via `iterate_while_pure` with a step-count
   predicate (strawman-conformant + reuses canonical vocabulary), OR scope-note
   that `forM_`/`foldM` are proposed-as-rough-in L4 combinators pending their own
   rows, OR downgrade the L4 entry's `firm` status to reflect the unanchored
   wrapper.

2. **[L4/chebyshev.md §Status — `firm`] — firmness over-claims given issue 1.
   Severity: low-medium.** The entry is firm at the body (clean re-type of the
   cycle-012 firm L1/L2) but carries an unreconciled wrapper-vocabulary choice
   that the report's own OQ 1 leaves to the lowering-verifier. Consider whether
   `firm` is the right status for an entry whose iteration combinators are neither
   anchored nor reconciled, vs. a body-firm/wrapper-rough-in framing.

3. **[L3 index-edit instruction] — stale line reference. Severity: low.** The
   instruction places the new dep-map row "after the `scal` row, line 28", but in
   the current `book/src/L3/index.md` line 28 is the `axpby` row and `scal` is the
   *last* dep-map row at a higher line number. The new row should follow the
   actual last row. The report delegates exact positioning to the integrator, so
   this is drift rather than breakage.

4. **[chebyshev.hpp:72-75 citation] — one-line offset. Severity: trivial.** The
   `MultTranspose2 → Mult2` symmetry-alias body spans lines 73-76; line 72 is
   blank and line 76 is the closing brace. The cited range 72-75 still covers the
   load-bearing alias lines (73-75), so the law-3/law-4 witness is in-range; flagged
   only for precision.

### Notes on scrutiny items requested

- **(a) In-line non-adjacent identity convention — correctly applied.** The L3
  entry annotates the L3↔L1 identity IN-LINE (§Downward + the dedicated
  "Non-adjacent identity (in-line, no directory)" block + the dep-map +
  frontmatter `lowers_to` note) as the transitive composition of the two
  adjacent-edge identities (L3>L2 ∘ L2>L1), and explicitly creates **no**
  `L3-L2/`, `L3-L1/`, or `L4-L2/` directory. This conforms to the cycle-012
  meta-phase `l3-l1-inline-identity-rotation-convention` and the CLAUDE.md
  invariant. One framing nuance (not an error): the report cites
  `book/src/L3/krylov-step.md` §Downward as the precedent for in-line *adjacent*
  L3>L2 treatment, but krylov-step's L3>L2 edge actually HAS a dedicated theme
  file (`book/src/L3-L2/krylov-step-body-identity.md`); the cleaner in-line
  no-directory precedent is the BLAS-1 cohort (`book/src/L3/axpy.md`, `dot.md`,
  `nrm2.md`, `scal.md`), which the report does not cite. The chebyshev L3↔L1
  *transitive* (through-L2) case is a legitimate extension of the convention.

- **(b) L3 `partial-obstruction` status — correctly grounded.** The witnessed
  sequential obstruction (inner `k`-recurrence + outer `pc_it` sweep) is grounded
  in positive Palace source (both `Mult2` bodies), and Phillips & Fischer 2022 §2
  is used as a *literature anchor* for the recurrence's numerical-stability
  motivation (non-removability rationale), NOT as a load-bearing positive-source
  substitute for the body. The reference is one Palace itself cites
  (`chebyshev.hpp:18-20`, arXiv:2210.03179v1). The report correctly distinguishes
  `partial-obstruction` from the cycle-012 `partly-constructive` status (OQ 3).

- **(c) L4 strawman conformance — partial.** Haskell `::` signatures + TS-record
  braces in ```text fences + `$$` math display for the L3 body are used per the
  `krylov-step` precedent (the L4 entry correctly omits YAML frontmatter, matching
  `book/src/L4/krylov-step.md`; the L3 entry includes frontmatter, matching
  `book/src/L3/krylov-step.md`/`axpy.md`). The departure is the iteration
  combinators (issue 1): the strawman §6 + the firm `iterate-while` family are the
  canonical bounded-iteration vocabulary; `forM_`/`foldM` are not strawman-defined.

- **(d) Consistency with cycle-012 L1/L2 two-kinds treatment — confirmed.** The
  collapse of ChebyshevSmoother (4th-kind) and ChebyshevSmoother1stKind into one
  operator parameterised by `op.scalars`, with variant absorption at level (c) and
  a variant-invariant body, matches `book/src/L2/chebyshev-iteration.md` law 2 and
  §Variant axes verbatim. The L2 `sweep` body maps line-for-line to the L3 body as
  claimed (identity-in-form), and the L2 non-laws (step-reordering,
  polynomial-expansion, `pc_it`-non-commutativity) are exactly the obstructions the
  L3 entry inherits.

## Repair

### Fixes attempted

- **Finding (issue 4, citation-validity):** `chebyshev.hpp:72-75` flagged as a
  one-line offset (critic read the alias as spanning 73-76 with line 72 blank).
  - **Decision:** not-needed.
  - **Rationale:** Re-verified via `palace-codemap` `read_range` on
    `palace/linalg/chebyshev.hpp:70-78`. Line 72 = `void MultTranspose2(...)
    override`, 73 = `{`, 74 = `Mult2(x, y, r); // Assumes operator symmetry`, 75 =
    `}`. The cited `72-75` range covers the full alias **exactly** — no offset.
    The critic's "73-76 / blank line 72" reading was itself off by one. No edit.

- **Finding (issue 3, cross-reference-integrity (b) / plan-kind drift):** L3
  index-edit instruction says "after the `scal` row, line 28"; critic claimed line
  28 is the `axpby` row and `scal` is the last row at a higher line.
  - **Decision:** not-needed (verified against live file).
  - **Rationale:** Read live `book/src/L3/index.md`. Line 24 = `axpby` row; **line
    28 = the `scal` row, which IS the last dep-map row**. The report's "after the
    `scal` row, line 28" is correct against the current file; the critic's offset
    was the stale one. The L4 index-edit references ("`iterate-while-with-prev`
    row, line 51"; "Firm at L4 list line 36") also verify correct. No anchor edit
    needed.

- **Finding (issue 1, rotation-quality / cross-reference-integrity (a); CENTRAL):**
  L4 `chebyshev.md` introduces `forM_`/`foldM` iteration combinators that are
  un-anchored at L4 (no dep-map row, no concept page) and compete with the firm
  canonical `iterate-while` family — whose entry (`iterate-while.md:7`) declares
  itself canonical and explicitly names Chebyshev as a consumer.
  - **Decision:** unrepairable (the rotation-quality / cross-reference dangling part).
  - **Action (partial, mechanical safety):** downgraded the L4 entry from `firm` to
    `rough-in` ("firm at the body, rough-in at the wrapper") and recorded the
    un-anchored-vocabulary caveat in three places: `CYCLE.md` L4 §Status, the L4
    index-edit dep-map row (status `firm`→`rough-in`, dependency cell rewritten to
    flag "iteration combinators UNRECONCILED"), and the L4 "Firm at L4" cohort-list
    index-edit instruction (rewritten so chebyshev is NOT added to the firm cohort
    and the "Firm at L4 (3)" count is NOT bumped — added a "Rough-in at L4" note
    instead). Opened repairer OQ 6 routing the reconciliation.
  - **Rationale (why the core is unrepairable):** A faithful re-anchor would mean
    re-expressing the bounded `forM_ [1..pc_it]` and `foldM (innerStep) (r0,d0,st0)
    [1..order-1]` constructs — the latter threading a 3-tuple accumulator with
    embedded monadic `modifyY` side effects — in terms of `iterate_while_pure` /
    `iterate-while-with-prev` with step-count predicates. That requires re-deriving
    the wrapper's monadic body shape (accumulator state-record design, predicate
    formulation, effect interleaving), i.e. substantive authoring, not a mechanical
    name swap. Out of repair scope; escalated.

- **Finding (issue 2, plan-kind-consistency):** L4 entry `firm` status over-claims
  given issue 1.
  - **Decision:** repaired.
  - **Action:** status downgraded `firm` → `rough-in` in `CYCLE.md` L4 §Status (with
    a "wrapper caveat" explaining the body is firm and the wrapper-iteration
    vocabulary is the open part) and in the L4 index-edit dep-map row + cohort-list
    instruction. This is the mechanical, in-scope half of the central finding (a
    status correction that does not author content); the substantive re-anchoring is
    the unrepairable half above.

### Unrepairable findings

- **L4 chebyshev wrapper iteration vocabulary (`forM_`/`foldM`) un-reconciled
  against the firm `iterate-while` family.** Requires substantive re-authoring of
  the L4 wrapper's monadic iteration shape (or a justified second-vocabulary
  anchor). **Routed to `combinator-miner`** (alternatively `lifter`) — opened as
  `CYCLE.md` Open Question 6. The repairer's downgrade to `rough-in` prevents a
  `firm` L4 entry from asserting un-anchored competing vocabulary in the interim;
  the follow-up dispatch re-expresses or anchors the combinators, then re-firms.

## Suggested resolution

`needs-revision`. The L3 entry is clean and integrable as-is (`partial-obstruction`,
body identity-in-form in-line, well-cited — all critic checks on the L3 content
pass or are telemetry-only). The L4 entry is integrable **at `rough-in`** with the
wrapper caveat recorded. The integrator may apply both rows this cycle (the
`rough-in` L4 status honestly reflects the open part — accumulate-with-embedded-
friction). Follow-up for `combinator-miner` (OQ 6): re-express the L4 chebyshev
bounded loops via `iterate_while_pure` / `iterate-while-with-prev` with step-count
predicates (strawman §6 + `iterate-while.md:7` are the canonical target), OR anchor
`forM_`/`foldM` as their own firm L4 rows with a rationale for a second iteration
vocabulary; then drop the wrapper caveat and re-firm the L4 entry + index row +
move it into the "Firm at L4" cohort (bumping the count to 4). The
`iterate-while.md:7` "Chebyshev reduces to iterate_while" claim is the load-bearing
constraint the reconciliation must satisfy or explicitly amend.
