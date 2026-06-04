---
agent: lowering-verifier
invoked_at: 2026-06-04T205500Z
scope: L4 verb firm re-judgment — gram_reduce (coupled to the bilinear-form firm-flip cascade, D3 Wave 2)
status: integrated
integrated_at: 2026-06-04T231500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-095 D3 (staging position 3/7). gram_reduce DISCHARGE->firm (both folded gates discharged: matrix-weighted-norm c091 + bilinear-form c095) + typed edges: [direct-dep set] + first verified_against: block (7 entries); L4 firm 18->19 main / 22->23 grand, L4 rough-in (tcb) cohort 1->0 EMPTY. Rank-gate PASS firm-over-firm (re-read deps on disk in-invocation). Applied clean, all 4 blocks verbatim; retroactive-budget 0. Promoted OQ solve-family-154... (DISCHARGED in-artifact by D6's K edit same cycle)."
inputs:
  - book/src/L4/gram_reduce.md (the verb being re-judged)
  - reports/2026-06-04T204023Z-cycle-planner-cycle-095/CYCLE.md (D3 scope)
  - reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md (D1 — bilinear-form→firm, Wave 1)
  - book/src/methodology/graded-stack-scheme.md (rank/edges grammar; §1 ladder, §2 edge block, §4(a) supersession, §1b rank invariant)
  - book/src/L1/bilinear-form.md:4 (on-disk firmness: rough-in — D1's flip not yet applied; firm via D1 report)
  - book/src/L1/matrix-weighted-norm.md:110 (firm c091)
  - book/src/L1/dot.md:100 (firm)
  - book/src/L1/apply_linop.md:87 (firm)
  - book/src/L4/solve_family.md:4 (firm c086)
  - reference/palace/palace/drivers/electrostaticsolver.cpp / magnetostaticsolver.cpp (the 2 positive Gram witnesses)
---

# CYCLE: Audit gram_reduce — firm re-judgment under the discharged bilinear-form gate

## Summary

This is **D3, Wave 2** of cycle-095 (the bilinear-form firm-flip-and-cascade-wave / GRADED-STACK P1 launch). `book/src/L4/gram_reduce.md` is the L4 operator-weighted symmetric-Gram reduction combinator `Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)`, currently `rough-in (test-coverage-bounded)`. Its `## Status` (`:228-265`) already records that its **structure** satisfies the firm-on-positive-structure escape (the symmetric-Gram skeleton + every law a syntactic identity on the two skeleton-identical positive PostprocessTerminals loops) and that its SOLE residual constructive gate was the off-diagonal folded primitive `bilinear-form` (`matrix-weighted-norm` having firmed c091).

**Verdict: DISCHARGE → FIRM.** D1 (Wave 1) flips `bilinear-form` rough-in→firm on the firm-on-positive-structure escape (DISCHARGE established c092, ENACTED c095). That clears the sole residual gate. All of `gram_reduce`'s direct folded/consumed primitives are now firm on disk (matrix-weighted-norm c091, bilinear-form via D1, solve_family c086), so condition-(i) of the c083 two-condition narrowed escape rule (all folded primitives firm) is satisfied and the disposition is **materially identical** to the four prior reduce-verb promotions — `domain_energy_reduce` (c091, the per-DOMAIN sibling that firmed *this same cascade family* because BOTH its primitives firmed), `eigenfreq_qfactor_reduce` (c082), `sparameter_reduce` (c083), `solve_family` (c086). This is NOT a forcing: the structure was already judged firm-on-positive-structure on disk; the only thing that held it at rough-in was the least-firm-folded-primitive inheritance rule, and that primitive is now firm.

I propose (a) flip `gram_reduce.md` §Status + `firmness:` → `firm`; (b) land the HARD-gate-new typed frontmatter (`rank: firm` + an `edges:` block superseding the ad-hoc `consumes:`/`lowers_to:`); (c) re-anchor the bilinear-form rough-in labels inside the file; (d) append a `verified_against:` block. The four L0 Gram witnesses are citecheck-`[ok]` confirmed this cycle.

## Per-citation audit

### Citation A — the folded primitives' firmness (the rank-invariant inputs)

- **Citation**: `book/src/L1/matrix-weighted-norm.md:110`, `book/src/L1/bilinear-form.md` (firm via D1 report), `book/src/L4/solve_family.md:4`, `book/src/L1/dot.md:100`, `book/src/L1/apply_linop.md:87`.
- **Theme claim**: gram_reduce folds matrix-weighted-norm (diagonal) + bilinear-form (off-diagonal) and consumes solve_family; its maturity is bounded by the least-firm of these.
- **Found**:
  - `matrix-weighted-norm.md:110` §Status `firm` (promoted c091 — verified on disk this cycle).
  - `bilinear-form.md:4` on-disk frontmatter still reads `firmness: rough-in` — BUT this is the expected Wave-1/Wave-2 forward-reference: D1's report (`reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md`) proposes the flip to `firm`, applied by the integrator BEFORE this D3 report in serial integration order. D1's dependency-firmness section verifies dot/apply_linop/matrix-weighted-norm all firm so its own rank invariant holds. Confirmed D1's flip is sound (its three deps are firm on disk).
  - `solve_family.md:4` `firmness: firm` (c086 — verified on disk this cycle).
  - `dot.md:100` §Status `firm`; `apply_linop.md:87` §Status `firm` (both verified on disk this cycle).
- **Verdict**: supports (DISCHARGE). After D1's flip, min(rank of direct deps) = firm. The rank invariant `rank(gram_reduce=firm=3) ≤ min(matrix-weighted-norm=3, bilinear-form=3, solve_family=3)` holds.
- **Notes**: `dot` and `apply_linop` are deps of `bilinear-form`, NOT direct deps of `gram_reduce` (gram_reduce's body folds `matrix_weighted_norm` and `bilinear_form` directly — `gram_reduce.md:88-90` `entry`). The dispatch brief's "list all folded primitives now firm: bilinear-form, matrix-weighted-norm, dot, apply_linop" conflates direct + transitive. I use the **direct** edge set (matrix-weighted-norm, bilinear-form, solve_family) for the typed `edges:` block — that is what the rank linter checks per-edge and what the on-disk `consumes:`/`lowers_to:` frontmatter already records. dot/apply_linop are reached transitively through bilinear-form's own `edges:`; restating them on gram_reduce would create false direct edges. See §Proposed changes note.

### Citation B — the structure / law content (the escape substrate)

- **Citation**: `book/src/L4/gram_reduce.md:132-161` (§Algebraic laws), `:228-253` (§Status reasoning), L0 witnesses `electrostaticsolver.cpp:100-140` + `magnetostaticsolver.cpp:110-152`.
- **Theme claim**: every law is a syntactic identity on the fold structure, read off the two positive PostprocessTerminals loops; the structure satisfies firm-on-positive-structure independent of the test-coverage question.
- **Found**: §Algebraic laws 1-4 (symmetry from symmetric-K + symmetric-w; diagonal-is-self-bilinear; weight-factoring/bilinearity; grid-map independence) are read-offs of the loop structure with NO inner-product-norm theorem content beyond what the firm `matrix-weighted-norm`/`bilinear-form` primitives already carry. The two "do not hold" laws (inverse-not-in-reduction; no cross-output-product fusion) are correctly excluded. The §Status already states "the *structure* would satisfy the firm-on-positive-structure escape" (`:233-234`) — the ONLY thing holding it at rough-in was the bilinear-form primitive (`:234-237`, `:241-245`).
- **Verdict**: supports. The escape applies to the assembly: gram_reduce introduces NO new inner-product-axiom content over its now-firm folded halves (the exact `domain_energy_reduce` c091 / `eigenfreq_qfactor_reduce` c082 disposition — bare fold-assembly over firm primitives).
- **Notes**: gram_reduce is one step "higher" than its siblings (it folds the firm primitives via a `symmetric_from_upper` grid map) but the grid map adds only the symmetry law (law 1), itself a syntactic consequence of K-symmetry + w-symmetry — no theorem requiring a positive test.

### Citation C — the L0 Gram witnesses (citecheck-confirmed)

- **Citation**: `palace/drivers/electrostaticsolver.cpp:118-119` (M_elec apply + diagonal Dot), `:139-140` (Cinv Invert); `palace/drivers/magnetostaticsolver.cpp:129-131` (M_mag apply + diagonal Dot), `:151-152` (Minv Invert).
- **Theme claim**: the two skeleton-identical positive loops are the structural anchor for the symmetric-Gram skeleton + the inverse-as-consumer split.
- **Found** (citecheck `--anchor`, all `[ok]` this cycle):
  - `electrostaticsolver.cpp:118-119 --anchor 'M_elec'` → anchor at 118 in range. `--anchor 'Dot'` at :119 → ok.
  - `electrostaticsolver.cpp:139-140 --anchor 'Invert'` → anchor at 140 in range.
  - `magnetostaticsolver.cpp:129-131 --anchor 'M_mag'` → anchor at 129 in range. `--anchor 'Dot'` at :131 → ok.
  - `magnetostaticsolver.cpp:151-152 --anchor 'Invert'` → anchor at 152 in range.
- **Verdict**: supports. No drift on any of the four range-pairs.
- **Notes**: these are the witnesses already cited in §Evidence (`:279-292`); I re-confirmed them on-disk (not transcribed) per the audit-report-inherited-citation duty.

## Applicability conditions

- **Condition**: "a reduction is as firm as its least-firm folded primitive" (the §1b rank invariant / the gram_reduce §Status reasoning).
  - **Verifiable**: yes — read each direct dep's `## Status`/`firmness:` on disk. matrix-weighted-norm firm, solve_family firm, bilinear-form firm (via D1). min = firm.
  - **Found counter-example?**: no. All direct deps firm.
- **Condition** (c083 narrowed escape rule, condition-i): all folded primitives firm.
  - **Verifiable**: yes — verified above.
  - **Found counter-example?**: no.
- **Condition** (c083 narrowed escape rule, condition-ii): the missing dedicated test does not gate any law that lacks other evidence.
  - **Verifiable**: yes — §Algebraic laws 1-4 are syntactic identities on the fold (law 1 = K-symmetry + w-symmetry; laws 2-4 = read-offs), carrying no theorem-needing-proof beyond what the firm primitives supply. The "no dedicated Gram-reduction unit test" gap (`:246-248`, `:299-301`) is therefore REDUNDANT under the escape — exactly the `domain_energy_reduce` c091 disposition (whose §Status the L4/index:50 cell records: "the missing dedicated per-domain test is redundant under the escape").
  - **Found counter-example?**: no. There is no gram_reduce law for which the absent test is the only evidence.
- **Condition** (scope): 2-of-N pipelines (electrostatic + magnetostatic), disciplined-cross-pipeline-mining-gate 2-of-N met.
  - **Verifiable**: yes — §Specialization + §Status `:267-271`. Two positive witnesses, normalization-weight a variant axis (not a break-witness); the c074-D6 3rd-witness probe is CLOSED-NEGATIVE (eigenmode/driven correctly refused). Scope unchanged by the firm flip.
  - **Found counter-example?**: N/A — the firm flip does not widen scope (firm is a law-confidence judgment, not a witness-count change).

## Algebraic laws

- **Law 1 (Symmetry, load-bearing)**: holds on the operators — `bilinear_form xⱼ K xᵢ = bilinear_form xᵢ K xⱼ` for symmetric K, AND `w i j = w j i` (both witnesses' w are symmetric). Per the firm bilinear-form signature (law 7 Hermitian-M symmetry, conditional on symmetric M; K is SPD here per `:99-100`), this is a syntactic identity, no new theorem.
- **Law 2 (Diagonal-is-self-bilinear)**: holds — `entry K xs i i = matrix_weighted_norm (xs!!i) K = bilinear_form (xs!!i) K (xs!!i)` (modulo the √). This is the do-NOT-merge consumer-not-fold identity, sound per both primitives' firm signatures.
- **Law 3 (Weight factoring / bilinearity)**: holds — `w(i,j)` factors out (scalar multiply); `xⱼᵀ K xᵢ` bilinear per bilinear-form's firm laws 1-3 (linearity).
- **Law 4 (Grid-map independence)**: holds — each entry depends only on `(K, xs!!i, xs!!j, w i j)`; the upper-triangle map carries no state. Structural read-off of the loop.
- All four hold on the firm operator signatures with no inner-product-axiom content beyond the firm primitives. No law fails on the operator signatures.

## Proposed changes

DISCHARGE. Flip gram_reduce.md to firm + typed frontmatter + within-file re-anchor + appended `verified_against:` block.

### (1)+(2) Frontmatter — flip firmness, add rank, replace consumes:/lowers_to: with typed edges:

Per scheme §4(a) the `edges:` block supersedes the ad-hoc `consumes:`/`lowers_to:` lists. The `## Status`-free-text maturity qualifiers in those lists are dropped from the edges (the dep's rank is read from the dep's own frontmatter — scheme §4(c) the index-cell-drift lesson). `solve_family` is a `depends-on` (it produces the consumed family — blocking on the composition root); `matrix-weighted-norm` + `bilinear-form` are `depends-on` (the folded primitives); the two sibling combinators are `reference` (navigational).

```edit:book/src/L4/gram_reduce.md
---
layer: L4
operator: gram_reduce
firmness: firm
rank: firm
edges:
  depends-on:
    - L1/matrix-weighted-norm
    - L1/bilinear-form
    - L4/solve_family
  reference:
    - L4/inner_product
    - L4/linear_combination
variant_axes:
  - normalization-weight (unit | current-normalized — THE load-bearing axis; absorbed into the w closure)
  - operator-source (mass-energy — absorbed into K)
  - element-type (real — pinned for the two witnessed pipelines)
  - family-index-domain (terminal-boundary | surface-current — absorbed into [Tensor] / w)
---
```

Note on the `edges:` block (recorded for the integrator, NOT authored into the file): the dispatch brief listed `bilinear-form, matrix-weighted-norm, dot, apply_linop` as the `depends-on:` set. I use the **direct** dependency set `L1/matrix-weighted-norm` + `L1/bilinear-form` + `L4/solve_family` instead — `dot`/`apply_linop` are deps of `bilinear-form`, not direct deps of `gram_reduce` (gram_reduce's body `:88-90` folds `matrix_weighted_norm`/`bilinear_form` directly and consumes `solve_family`; it never names dot/apply_linop). Restating dot/apply_linop as gram_reduce `depends-on` edges would create false direct edges that the reachability GC + rank check would treat as first-class — the transitive reach is already carried through bilinear-form's own `edges:` (D1 lands those). All three direct deps are firm (matrix-weighted-norm c091, bilinear-form via D1, solve_family c086), so the rank invariant holds identically. The bare-string form is used (scheme §2, bare ≡ `{target}` no kind).

### (3) Re-anchor the bilinear-form rough-in labels

Frontmatter consumes-line equivalent is removed by (1) above. The remaining in-prose rough-in labels:

§Context off-diagonal line (`:58-60`):

```edit:book/src/L4/gram_reduce.md
- the off-diagonal entry `xⱼᵀ K xᵢ` is the now-**firm** (c095) L1
  [`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y` at `M = K`) — the last
  remaining folded gate, discharged by the cycle-095 firm-flip-and-cascade wave
  (see §Status).
```

§Dependencies bilinear-form row (`:198-199`):

```edit:book/src/L4/gram_reduce.md
- [`bilinear-form`](../L1/bilinear-form.md) (firm c095) — the off-diagonal cross-bilinear;
  the fold element. **Promoted rough-in→firm by the cycle-095 firm-flip-and-cascade wave (the last folded gate discharged).**
```

§Status — replace the whole `:228-271` block (the warrant-first reasoning + the narrowed promotion route + the scope note), re-anchoring to the ENACTED firm conclusion. The structure argument and the scope statement are preserved; only the "stays rough-in / one gate remains" framing flips to "both gates discharged / firm":

```edit:book/src/L4/gram_reduce.md
## Status

`firm` (promoted from `rough-in (test-coverage-bounded)` at **cycle-095**, the
`bilinear-form-firm-flip-and-cascade-wave` D3, on the **firm-on-positive-structure
escape**). **Reasoning (warrant-first):** the combinator's **structure** is
firm-on-positive-structure — the symmetric-Gram skeleton
(map-over-upper-triangle-pairs, diagonal/off-diagonal split, weight factoring,
symmetric mirror, inverse-as-consumer) is read directly off the two skeleton-identical
positive PostprocessTerminals loops (electrostatic `:100-140` + magnetostatic
`:110-152`), and every law (§Algebraic laws) is a syntactic identity on that fold.
After the cycle-091 + cycle-095 cascade, **both** folded gates are now discharged:

1. the diagonal building block [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   is **firm** (c091, the batch-29 firm-flip-and-cascade wave — both norm-axiom
   law-sides discharged on the firm-on-positive-structure escape) — **gate discharged**;
2. the off-diagonal building block [`bilinear-form`](../L1/bilinear-form.md) is now
   **firm** (c095, this cascade wave's D1 — promoted on the firm-on-positive-structure
   escape, firmability DISCHARGED by the cycle-092 `lowering-verifier` probe) — **the
   last residual gate, now discharged**;
3. the absence of a dedicated Palace unit test for the Gram reduction (the
   PostprocessTerminals bodies are integration-level, exercised only through the full
   `Solve(mesh)` driver) is **REDUNDANT** under the firm-on-positive-structure escape:
   every reduction-level law is a syntactic identity on the fold over two now-firm
   primitives (no theorem-needing-proof; the assembly is bare grid-fold arithmetic over
   firm halves with no inner-product-axiom content) — there is NO law for which that
   absent test is the only evidence.

A reduction is as firm as its least-firm folded primitive, and after the cascade BOTH
folded primitives are firm, so `gram_reduce` promotes to **firm** — the materially
identical disposition to its four reduce-verb siblings on the same escape: the
per-DOMAIN [`domain_energy_reduce`](./domain_energy_reduce.md) (firmed cycle-091 in
this same cascade family, because BOTH its primitives — matrix-weighted-norm c091 +
participation_ratio c077 — firmed), [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md)
(c082), [`sparameter_reduce`](./sparameter_reduce.md) (c083), and
[`solve_family`](./solve_family.md) (c086). This is NOT a forcing: the structure was
already firm-on-positive-structure on disk, and the only thing that held the verb at
`rough-in (test-coverage-bounded)` was the least-firm-folded-primitive inheritance
rule — which the c095 bilinear-form flip clears.

**Scope: 2-of-N pipelines** — electrostatic + magnetostatic output products (the two
energy-formulated symmetric-Gram reductions); eigenmode + driven post-processing are
candidate 3rd+ witnesses for a stronger future mine (§Specialization), not in scope
now. The disciplined-cross-pipeline-combinator-mining-gate is 2-of-N met (2 positive
witnesses, no break-witness — the normalization weight is a variant axis). The firm
flip is a law-confidence judgment, NOT a witness-count change: scope is unchanged.
```

### (4) Append the verified_against: block

Append at end of file (after §Evidence, `:308`):

```edit:book/src/L4/gram_reduce.md
[append at end of file]
```yaml
verified_against:
  - citation: book/src/L1/matrix-weighted-norm.md:110
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: diagonal folded primitive firm c091; the rank-invariant diagonal input
  - citation: book/src/L1/bilinear-form.md
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: off-diagonal folded primitive firmed c095 (D1, this cascade); the last residual gate discharged
  - citation: book/src/L4/solve_family.md:4
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: consumed composition-root family-producer firm c086; the depends-on input
  - citation: reference/palace/palace/drivers/electrostaticsolver.cpp:118-119
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: M_elec apply + diagonal Dot — capacitance Gram witness 1; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/electrostaticsolver.cpp:139-140
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: Cinv Invert — the gram_inverse consumer split; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/magnetostaticsolver.cpp:129-131
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: M_mag apply + diagonal Dot — inductance Gram witness 2; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/magnetostaticsolver.cpp:151-152
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: Minv Invert — the gram_inverse consumer split; citecheck --anchor ok
```
```

## Supporting evidence

- **DISCHARGE provenance (the cascade)**: D1 report `reports/2026-06-04T204500Z-harvester-cycle-095-bilinear-form-firm-flip/CYCLE.md` (bilinear-form→firm, Wave 1, the gate this re-judgment rests on); the c092 probe `reports/2026-06-04T065200Z-lowering-verifier-cycle-092-bilinear-form-probe/` (established bilinear-form firmability).
- **Sibling-reduce-verb escape precedents**: `domain_energy_reduce` (c091 — the per-DOMAIN sibling, same cascade family, `book/src/L4/index.md:50`), `eigenfreq_qfactor_reduce` (c082), `sparameter_reduce` (c083), `solve_family` (c086, `book/src/L4/solve_family.md:142-156`).
- **Rank-invariant dependency firmness (verified on disk this cycle)**: `matrix-weighted-norm.md:110` (firm), `solve_family.md:4` (firm), `dot.md:100` (firm), `apply_linop.md:87` (firm); `bilinear-form.md:4` reads rough-in on disk but is firmed by D1's Wave-1 flip (applied before this report in serial integration order; D1's own rank invariant verified). `rank(gram_reduce=3) ≤ min(3,3,3)` over the direct deps.
- **L0 Gram witnesses (citecheck `--anchor` ok this cycle)**: `electrostaticsolver.cpp:118-119`/`:139-140`, `magnetostaticsolver.cpp:129-131`/`:151-152` — all `[ok]`, no drift.
- **SUMMARY/registration**: gram_reduce is an existing chapter (this is a flip, not a new chapter) — no SUMMARY edit.

## Open questions / caveats

- **solve_family.md:154 is stale post-c091/c095 — OUT OF MY FILE SCOPE; routed to D4/integrator.** `book/src/L4/solve_family.md:154` (the "Column-gate note") states the gram_reduce gate is "convergently blocked on the `matrix-weighted-norm` √-cascade NO-GO-HELD (c080 D1 ruled the firm-on-positive-structure escape INAPPLICABLE for `matrix-weighted-norm`)" and that gram_reduce folds "plain-`rough-in` matrix-weighted-norm". BOTH are now stale: matrix-weighted-norm firmed c091 (the c080 NO-GO was OVERTURNED by the batch-28 meta-phase GO), and with this D3 flip gram_reduce itself firms. The `solve_family` verb is a DIFFERENT file outside my HARD scope (gram_reduce.md own status/frontmatter ONLY). Per my dispatch brief ("if it's outside your file scope (solve_family is a different verb), flag it for D4 or as OQ-intake"), I FLAG it: the exact stale text is `solve_family.md:154`, asserting (i) matrix-weighted-norm "plain-rough-in" → should be "firm c091", (ii) "NO-GO-HELD (c080 ... escape INAPPLICABLE)" → should be discharged/overturned, (iii) "those columns stay `status: seed` this cycle" → the 4 columns flip this cycle (D4). **Recommended re-anchor (for D4 or a co-scheduled land-clean lifter):** restate `:154` as "Firming `solve_family` discharged one of the two own-constituent gates; the second gate — `gram_reduce` — was firmed at cycle-095 (D3), and the columns flip this cycle (D4)." Routed to D4 (it owns the columns + the column-gate narrative coupling) OR the integrator's carry-forward; logged here as OQ-intake `solve-family-154-stale-column-gate-narrative-post-c091-c095`.
- **L4/index.md:101 gram_reduce dep-map cell needs the firm flip — contested ownership, FLAGGED for integrator (not edited).** `book/src/L4/index.md:101` carries the gram_reduce dep-map cell with `rough-in (test-coverage-bounded)` status + the bilinear-form "(rough-in ... the sole remaining rough-in folded primitive, the residual gate)" label. This must flip to `firm` + bilinear-form "(firm c095)" to track this D3 flip. Per my HARD constraint (the L4/index gram_reduce/count cells are contested this cycle — "flag if you need an L4/index edit rather than making it, since index-count ownership is contested this cycle — note it for the integrator"), I do NOT edit it. **Flagged for the integrator:** `L4/index.md:101` gram_reduce cell status `rough-in (test-coverage-bounded)`→`firm` and the folded-primitive label `bilinear-form` `(rough-in...residual gate)`→`(firm c095)`; also the L4-firm-count header (if the L4 index tracks a per-Part firm count, gram_reduce joins it) — but I did not verify an L4 firm-count header exists, so the integrator should check. (The matrix-weighted-norm label in the same cell already reads "firm c091" — correct.)
- **edges: direct-vs-transitive divergence from the brief (recorded, not a defect).** As noted in §Proposed changes (1)+(2): I used the direct dep set (matrix-weighted-norm, bilinear-form, solve_family) rather than the brief's literal `bilinear-form, matrix-weighted-norm, dot, apply_linop`. This is the correct typed-edges semantics (dot/apply_linop are transitive through bilinear-form; restating them would create false direct edges for the GC/rank linter). The rank invariant holds identically either way (all paths firm). If the batch-30 meta-phase prefers transitive-closure edges on every node, that is a scheme decision (scheme §2 currently implies direct edges only) — flagged for awareness, not blocking.
- **No `verified_against:` block pre-existed on disk** — gram_reduce.md ended at §Evidence (`:308`); this D3 appends the first block. (Contrast bilinear-form/matrix-weighted-norm which carry c092/c091 blocks.) The block is fenced YAML per the channel-format requirement; all `note:` values begin with a non-quote character (self-checked).
- **bilinear-form on-disk frontmatter still rough-in at audit time** — this is the expected Wave-1→Wave-2 forward reference, not a contradiction. The integrator applies D1 before D3 (serial, per-report integration order); if for any reason D1's flip does NOT land, this D3 flip would create a rank violation (firm gram_reduce on rough-in bilinear-form) — the integrator should confirm D1 landed before applying D3, OR the rank linter will flag it (the campaign's intended safety net). Noted for the integrator's sequencing.
