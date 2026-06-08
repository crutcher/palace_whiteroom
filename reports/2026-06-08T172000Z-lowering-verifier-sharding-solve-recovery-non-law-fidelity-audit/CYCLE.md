---
agent: lowering-verifier
invoked_at: 2026-06-08T172000Z
scope: L4 roadmap_goal SOLVE-case NON-LAW fidelity audit — sharding-solve-recovery-non-law-fidelity-audit
status: pending
integrated_at: 2026-06-08T173000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: >
  Applied cycle-140 (batch-45 MIDDLE 2/3) as the sole report. Audit-class FULLY-SUPPORTED;
  the 9-entry `verified_against:` block landed as a separate ```yaml fence after the existing
  c139 block in book/src/L4/sharding-decompose-reduce.md (both round-trip clean; NO chapter
  body line touched). Node STAYS rank-0 roadmap_goal; the 3 solve roots stay reference-class
  (no depends-on); DIRECTIVE-1 MPI cited-not-lifted. cargo make book EXIT 0, ZERO build-repairs;
  step-5c KaTeX `$`-sigil assertion PASS (0 class="katex" inside any <pre>); step-5b graded-stack
  both block-conditions PASS (rank_violations 0; no newly-orphaned node; all counts HELD EXACTLY
  vs c139). DISCHARGES OQ sharding-decompose-reduce-solve-case-recovery-strictly-weaker-than-reduce-case
  (routed to the batch-45 meta for CLOSE-RESOLVE at :2234).
inputs:
  - book/src/L4/sharding-decompose-reduce.md (the c139 D3 SOLVE-generalization extension under audit)
  - book/src/L4/domain_energy_reduce.md:147-152,172-178 (the Σ pᵢ=1 config-conditional NON-law model the SOLVE non-law mirrors)
  - book/src/L4/inner_product.md:154-157 ; linear_combination.md:146-151 (the standing firm reduce-case homomorphism laws)
  - book/src/L4/ksp_solve.md ; fold_solve.md ; krylov-step.md (the 3 firm solve roots, reference-class)
  - reference/palace/palace/utils/geodata.cpp ; linalg/rap.{hpp,cpp} ; models/romoperator.cpp (the DIRECTIVE-1 deferred mechanism + no-native-DD confirmation)
---

# CYCLE: Audit sharding-solve-recovery-non-law-fidelity

## Summary

This is an AUDIT-CLASS fidelity check (no new chapter content authored) of the cycle-139 D3
extension to the rank-0 `roadmap_goal` chapter `book/src/L4/sharding-decompose-reduce.md`, which
generalized the sharding-as-decomposition MATH from the REDUCE case to the per-sub-domain SOLVE
case (the additive-Schwarz decomposition-abstraction). I audited whether the SOLVE-case recovery
is framed as a config-conditional NON-LAW that is STRICTLY WEAKER than the reduce case, and whether
any over-strong "exact-recovery" claim leaked. **Top-level verdict: FULLY-SUPPORTED.** The chapter's
SOLVE framing is faithful: the reduce case rides a standing firm concatenation-homomorphism law
(exact, free) while the solve case explicitly carries NO analogous free law — exact ONLY for a
block-diagonal operator, approximate (additive-Schwarz preconditioner) for a coupled operator,
partition-of-unity-weighted for overlapping blocks — mirrored on `domain_energy_reduce`'s
`Σ pᵢ = 1` config-conditional non-law. The 3 new solve roots are `reference:`-class ONLY (no
`depends-on`), all 3 confirmed `rank: firm` on-disk, so no rank violation is manufactured. Every
MPI-path mention stays in the deferred-future / Evidence framing (DIRECTIVE-1: cited, not lifted).
The node STAYS rank-0 `roadmap_goal` (no flip). One minor under-qualified-path nuance (the bare
`romoperator.cpp:586` omits the `models/` dir prefix) is recorded as a caveat, not forced. This
audit discharges OQ `sharding-decompose-reduce-solve-case-recovery-strictly-weaker-than-reduce-case`.
I touched NO chapter body line, so the c139 KaTeX-fence recurrence guard is moot for my deliverable.

## Per-citation audit

- **Citation**: `book/src/L4/sharding-decompose-reduce.md:103-113,244-267` (the SOLVE recovery framing — the §"crucial asymmetry" callout + the §"Laws that explicitly do NOT hold" SOLVE bullet)
  - **Theme claim**: SOLVE-case recovery is STRICTLY WEAKER than the reduce case; exact only for block-diagonal, approximate additive-Schwarz for coupled, p.o.u.-weighted for overlapping; no false exact-recovery claim.
  - **Found**: L103-113 states explicitly "The solve case has **NO analogous free law**: `solve (A|_b, rhs|_b)` per block recovers the exact global `solve(A, rhs)` ONLY when `A` is **block-diagonal**... For a general coupled global operator, the bare restrict/solve/compose is an **APPROXIMATE** recovery — precisely the additive-Schwarz PRECONDITIONER, a convergent OUTER ITERATION, not a one-shot identity." L244-267 carries the matching config-conditional NON-law with the two explicit failure modes (inter-block coupling ⇒ approximation; overlapping blocks ⇒ p.o.u. weighting), and explicitly states "The abstraction makes NO exact-solve claim for a coupled operator" and "The bare abstraction makes NO partition-of-unity claim." It cites `domain_energy_reduce.md:172-178` as the model.
  - **Verdict**: supports
  - **Notes**: The framing is faithfully STRICTLY-WEAKER. No "exact recovery" claim leaked for the general/coupled case; the only exact claim is gated on block-diagonal structure. The mirroring on `domain_energy_reduce`'s `Σ pᵢ = 1` is correct (verified anchor below).

- **Citation**: `book/src/L4/sharding-decompose-reduce.md:184-221` (the speculative algebraic laws)
  - **Theme claim**: laws are framed as DERIVED-from-firm-law INTENT, not asserted proven; only the reduce case rides a standing firm law; the solve case carries no analogous free law.
  - **Found**: L186-188 frames the section "These are the laws the abstraction WOULD carry; they are stated as the target shape, NOT as established claims." Law 1 (reduce homomorphic recovery, L190-197) is "intended to be a DIRECT consequence of the firm concatenation-homomorphism" citing `inner_product.md:154-157`, `linear_combination.md:146-151`, `domain_energy_reduce.md:147-152`. Law 5 (SOLVE-case recovery, L212-221) is titled "CONFIG-CONDITIONAL — intended, NOT free" and states "it is NOT a free standing law — it is gated on the operator's block structure" and "For a coupled operator the equality becomes an APPROXIMATION (additive-Schwarz preconditioner)." Law 4 (L207-211) correctly isolates the part the solve case DOES share (per-block map-independence) from the part it does NOT (recovery, law 5).
  - **Verdict**: supports
  - **Notes**: Clean separation of the shared map-independence (firm-anchored to `domain_energy_reduce.md:147-152`) from the un-shared recovery (config-conditional). No solve-case free law is claimed.

- **Citation**: `book/src/L4/sharding-decompose-reduce.md:6-14` (frontmatter `edges:`)
  - **Theme claim**: the 3 new solve roots are `reference:`-class ONLY (no `depends-on`).
  - **Found**: the frontmatter `edges:` block has a single `reference:` key (L7) listing all roots including `L4/ksp_solve`, `L4/fold_solve`, `L4/krylov-step` (L12-14). There is NO `depends-on:` key anywhere in the frontmatter. `grep depends-on` returns 6 hits, ALL in prose explicitly DISCLAIMING the edge (L35, 272, 273, 348, 350, 357) — none is an actual edge.
  - **Verdict**: supports
  - **Notes**: All 3 solve roots confirmed `rank: firm` on disk (`ksp_solve`, `fold_solve`, `krylov-step`). A `depends-on` from this rank-0 node to a rank-3 firm node would manufacture `rank(firm)=3 > rank(roadmap_goal)=0` — a RED rank-violation. None exists. The graded-stack rank linter constrains only `depends-on` edges, so the `reference` roots carry no rank constraint.

- **Citation**: `book/src/L4/domain_energy_reduce.md:172-178`
  - **Theme claim**: the `Σ pᵢ = 1` config-conditional partition-coverage NON-law is the exact model the SOLVE exact-recovery NON-law mirrors.
  - **Found**: L172-178 reads "**`Σ pᵢ = 1` is CONFIG-CONDITIONAL, NOT an unconditional identity (D4 flag #3).** The participations sum to one ONLY when the configured domain set **partitions the field's support**... overlapping... double-counting... The verb makes NO partition claim; the `partition-coverage` variant axis records the precondition." This is precisely the overlap-double-count / partial-under-count model the SOLVE non-law (chapter L257-264) mirrors.
  - **Verdict**: supports
  - **Notes**: anchor exact; the SOLVE p.o.u. non-law (`Σ χ_b = 1` over overlaps) is the correct solve-side analog.

- **Citation**: `book/src/L4/inner_product.md:154-157`
  - **Theme claim**: firm split-additivity / shape-concatenation monoid-homomorphism — the standing firm law the REDUCE case (law 1) rides.
  - **Found**: L154-157 is the "Split-additivity / shape-concatenation-homomorphism (the defining law)": `inner_product (x₁ ++ x₂) (y₁ ++ y₂) = inner_product x₁ y₁ + inner_product x₂ y₂`, "A monoid homomorphism from `(shape-concatenated tensors, ++)` to `(Scalar, +)`".
  - **Verdict**: supports
  - **Notes**: anchor exact; this is a firm standing law the reduce-case recovery legitimately rides.

- **Citation**: `book/src/L4/linear_combination.md:146-151`
  - **Theme claim**: firm concatenation-homomorphism — the reduce-to-tensor recovery law.
  - **Found**: L146-151 "Concatenation-homomorphism (the defining law)": `linear_combination (a ++ b) = linear_combination a + linear_combination b`, "A monoid homomorphism from `([(Scalar,Tensor[(S: ...)])], ++, [])` to `(Tensor[$S], +, zeros)`".
  - **Verdict**: supports
  - **Notes**: anchor exact.

- **Citation**: `reference/palace/palace/utils/geodata.cpp:262,3239,3242` (DIRECTIVE-1 mesh-partitioning mechanism)
  - **Theme claim**: the MPI mesh-partitioning mechanism is cited in deferred-future framing, NOT lifted.
  - **Found**: `:262` = `Partition(IoData&, unique_ptr<Mesh>, MPI_Comm)` (citecheck --anchor ok); `:3239` = METIS `GeneratePartitioning` (citecheck --anchor ok); `:3242` = "partitioning mesh into N subdomains" (citecheck --anchor ok). In the chapter these appear ONLY under §"Accreting working context" (L294-309) and §Evidence (L398-407), both explicitly DEFERRED-MECHANISM / "cited, NOT lifted (DIRECTIVE-1)".
  - **Verdict**: supports
  - **Notes**: DIRECTIVE-1 honored — no MPI lift; all anchors verify on-disk.

- **Citation**: `reference/palace/palace/linalg/rap.hpp:24,rap.cpp:116-126` (DIRECTIVE-1 RAP parallel-assembly mechanism)
  - **Theme claim**: the `ParOperator` / RAP Galerkin triple product is cited as eventual realization path, NOT lifted.
  - **Found**: `rap.hpp:24` = `class ParOperator : public Operator` (citecheck --anchor ok); `rap.cpp:116-126` = the `R·A·P` Galerkin triple-product (`hypre_ParCSRMatrixRAPKT`, citecheck --anchor ok). In the chapter under §"Accreting working context" L300-305 + §Evidence L405-407, framed as "the eventual operator-restriction-and-compose mechanism", DEFERRED.
  - **Verdict**: supports
  - **Notes**: DIRECTIVE-1 honored.

- **Citation**: `reference/palace/palace/models/romoperator.cpp:586` (the no-native-DD-preconditioner confirmation)
  - **Theme claim**: Palace ships NO native additive-Schwarz / DD preconditioner — the only `overlap` site is the wave-port ROM check — so the solve-generalization is a genuine abstraction sketch, not a lift.
  - **Found**: `grep -ril schwarz reference/palace/palace/` returns ZERO files — confirms no native Schwarz/DD preconditioner. `romoperator.cpp:586` "ports don't have any overlap" is confirmed content. BUT: the chapter cites the bare filename `romoperator.cpp:586` (L326, L394-395) — the file actually lives at `palace/models/romoperator.cpp`, so the bare path omits the `models/` directory prefix.
  - **Verdict**: partially-supports
  - **Notes**: the CLAIM (no native DD preconditioner; genuine abstraction) is FULLY confirmed and is the load-bearing assertion. The defect is purely cosmetic path under-qualification (bare filename vs `models/romoperator.cpp`). The bare path is unambiguous (only one `romoperator.cpp` in the tree) and the content checks. Recorded as a caveat below, NOT a forced fix — it is in-prose Evidence text, not a `verified_against:` anchor, and does not affect the audit verdict.

## Applicability conditions

- **Condition**: SOLVE exact-recovery holds ONLY for a block-diagonal operator (chapter law 5, L212-221; NON-law L244-256).
  - **Verifiable**: Yes — this is a stated mathematical precondition (zero inter-block coupling ⇒ disjoint concatenation recovers the exact global solve). The chapter frames it as a config-conditional gate, not an unconditional identity. Internally consistent with the additive-Schwarz reading.
  - **Found counter-example?**: No. The framing is correct: a coupled operator (the generic FE-assembled system where neighbouring elements share dofs) is explicitly stated NOT to satisfy it (L250-252), which is the standard additive-Schwarz result.

- **Condition**: Overlapping blocks require a partition-of-unity weighting `Σ χ_b = 1` (chapter NON-law L257-267).
  - **Verifiable**: Yes — the solve-side analog of `domain_energy_reduce`'s `Σ pᵢ = 1` (verified anchor `:172-178`). The chapter states `compose_partition` "is written to CARRY the p.o.u. weighting as its config parameter precisely so the non-law is explicit at the combinator boundary, not hidden" (L266-267) — a faithful, non-papering-over disclosure.
  - **Found counter-example?**: No.

- **Condition**: Per-block sub-solves are independent / embarrassingly parallel (chapter law 4, L207-211).
  - **Verifiable**: Yes — this is the part the solve case DOES share with the reduce case (map-independence, anchored to `domain_energy_reduce.md:147-152`). Correctly isolated from the recovery question.
  - **Found counter-example?**: No.

## Algebraic laws (if cited)

- **Law**: Reduce-case homomorphic recovery over a partition (law 1, L190-197) — `subdomain_reduce reduce P field = reduce field`.
  - **Holds on operators?**: Yes, as a DERIVED consequence of the firm concatenation-homomorphism. Verified the cited firm laws are exact: `inner_product.md:154-157` (split-additivity), `linear_combination.md:146-151` (concatenation-homomorphism), `domain_energy_reduce.md:147-152` (map-independence). A partition is a `++`-decomposition and the firm verbs are monoid homomorphisms over `++`, so the recovery is the existing homomorphism applied to the blocks — no new reduction algebra. The chapter correctly frames this as INTENT (target shape), not asserted-proven (rank-0 node).

- **Law**: SOLVE-case recovery (law 5, L212-221) — `subdomain_solve solve P A rhs = solve A rhs`.
  - **Holds on operators?**: ONLY for block-diagonal `A` (config-conditional), as stated. There is NO analogous free standing law (correctly NOT claimed): the firm solve verbs (`ksp_solve`/`fold_solve`/`krylov-step`) carry no concatenation-homomorphism over an operator's index partition (a solve is not a monoid homomorphism over operator-block concatenation for a coupled operator — the off-block-diagonal coupling breaks it). The chapter's STRICTLY-WEAKER framing is mathematically faithful: it does not claim a free solve law where none exists, and correctly reduces the coupled case to an approximate additive-Schwarz preconditioner (an outer iteration, itself one of the firm `fold_solve`/`krylov-step` drivers at the OUTER level, L253-256).

## Proposed changes

Append the audit's `verified_against:` correspondence block to the chapter. This is the ONLY
proposed change — no chapter body line is touched (the c139 KaTeX-fence guard is therefore moot:
no signature/pseudocode line is edited; the real pseudocode blocks at L45-58 / L69-86 are already
inside ` ```text ` fences, verified). The block round-trips clean under
`python3 -c "import yaml; yaml.safe_load(...)"` (no leading-quote scalar of either kind; the one
colon-space defect — `reference: ONLY` — was rephrased to `the reference edge-class ONLY` before
shipping). It is appended AFTER the existing c139 `verified_against:` block (the two blocks
coexist; the c139 block records the authoring self-verification, this block records the
independent SOLVE-case NON-LAW fidelity audit).

```edit:book/src/L4/sharding-decompose-reduce.md
[append at end of file, after the existing c139 verified_against block]
```yaml
verified_against:
  - citation: book/src/L4/sharding-decompose-reduce.md:103-113,244-267
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: SOLVE-case recovery framed STRICTLY WEAKER than reduce case — exact ONLY for block-diagonal, approximate additive-Schwarz preconditioner for coupled, partition-of-unity-weighted for overlapping; no false exact-recovery claim; mirrors domain_energy_reduce Sigma p=1 config-conditional NON-law
  - citation: book/src/L4/sharding-decompose-reduce.md:184-221
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: speculative laws framed as DERIVED-from-firm-law INTENT, not asserted proven; only reduce-case law 1 rides a standing firm law; solve-case law 5 explicitly CONFIG-CONDITIONAL (block-diagonal exact, coupled approximate) — no analogous free solve law claimed
  - citation: book/src/L4/sharding-decompose-reduce.md:6-14
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: 3 new solve roots (ksp_solve/fold_solve/krylov-step) under the reference edge-class ONLY in frontmatter edges; zero depends-on key; all 3 confirmed rank firm on-disk — no rank(firm)=3 > rank(roadmap_goal)=0 violation manufactured
  - citation: book/src/L4/domain_energy_reduce.md:172-178
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: Sigma p=1 config-conditional partition-coverage NON-law — the exact model the SOLVE exact-recovery NON-law mirrors (overlap double-count, partial under-count)
  - citation: book/src/L4/inner_product.md:154-157
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: firm split-additivity / shape-concatenation monoid-homomorphism — the standing firm law the REDUCE case (law 1) rides; verified anchor exact
  - citation: book/src/L4/linear_combination.md:146-151
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: firm concatenation-homomorphism (reduce-to-tensor recovery) — standing firm law for the reduce case; verified anchor exact
  - citation: reference/palace/palace/utils/geodata.cpp:262,3239,3242
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: DIRECTIVE-1 MPI mesh-partitioning mechanism (Partition / GeneratePartitioning / N-subdomain split) cited in deferred-future Evidence framing, NOT lifted; citecheck --anchor ok on all three
  - citation: reference/palace/palace/linalg/rap.hpp:24,rap.cpp:116-126
    verdict: supports
    audited_at: 2026-06-08T172000Z
    note: DIRECTIVE-1 ParOperator / RAP Galerkin triple-product parallel-assembly mechanism cited as deferred realization path, NOT lifted; citecheck --anchor ok
  - citation: reference/palace/palace/models/romoperator.cpp:586
    verdict: partially-supports
    audited_at: 2026-06-08T172000Z
    note: no-native-DD-preconditioner claim confirmed (no Schwarz anywhere in palace; only overlap site is the wave-port ROM check); chapter cites bare romoperator.cpp:586 omitting the models/ dir prefix — content correct, path under-qualified
```
```

**Optional one-line caveat fix (NOT forced — integrator/lifter discretion).** The bare in-prose
citations `romoperator.cpp:586` at chapter L326 and L394-395 could be qualified to
`models/romoperator.cpp:586` for path-precision. This is a cosmetic under-qualification, not a
defect that affects any claim (the file is unique in the tree; the content is confirmed). I do
NOT force it; recorded here and in §Open questions for a land-clean lifter's discretion.

## Supporting evidence

- `book/src/L4/sharding-decompose-reduce.md` — the chapter under audit (read in full on disk this dispatch).
- `book/src/L4/domain_energy_reduce.md:147-152,172-178` — the map-independence fold law + the `Σ pᵢ = 1` config-conditional partition-coverage NON-law (the model the SOLVE non-law mirrors); both anchors verified exact.
- `book/src/L4/inner_product.md:154-157`, `book/src/L4/linear_combination.md:146-151` — the standing firm reduce-case concatenation/split homomorphism laws; both anchors verified exact.
- `book/src/L4/ksp_solve.md`, `book/src/L4/fold_solve.md`, `book/src/L4/krylov-step.md` — all 3 confirmed `rank: firm` (frontmatter grep); the `reference`-class solve roots.
- `reference/palace/palace/utils/geodata.cpp:262,3239,3242`, `reference/palace/palace/linalg/rap.{hpp:24,cpp:116-126}` — DIRECTIVE-1 deferred mechanism; all verified via `tools/citecheck/citecheck.py --anchor` (all `[ok]`).
- `reference/palace/palace/models/romoperator.cpp:586` — the wave-port ROM overlap check; `grep -ril schwarz reference/palace/palace/` returns ZERO — confirms no native DD preconditioner.

## Open questions / caveats

- **DISCHARGE: OQ `sharding-decompose-reduce-solve-case-recovery-strictly-weaker-than-reduce-case`.**
  This audit confirms the SOLVE-case recovery is framed STRICTLY WEAKER than the reduce case (no
  false exact-recovery claim leaked; the config-conditional block-diagonal/p.o.u. NON-law is
  carried explicitly, mirroring `domain_energy_reduce`'s `Σ pᵢ = 1`). The OQ is DISCHARGED. Route
  to the planner/meta-phase to close it on integration.
- **STAYS DEFERRED: OQ `sharding-decompose-reduce-...solve-generalization-promotion-pull`.** The
  node correctly STAYS rank-0 `roadmap_goal` (no maturity/rank flip). No real single-machine-valid
  domain-decomposition-preconditioner consumer is in flight this cycle; the promotion-pull OQ
  stays deferred per the chapter's §Status (L354-358) and §Accreting-context (L319-324). This
  audit does NOT promote.
- **CAVEAT (cosmetic, not forced): bare `romoperator.cpp:586` path.** The chapter's two in-prose
  citations of the no-native-DD evidence (`romoperator.cpp:586`, L326 + L394-395) omit the
  `models/` directory prefix — the file is at `palace/models/romoperator.cpp`. The claim is fully
  confirmed and the bare path is unambiguous (single `romoperator.cpp` in the tree); this is a
  path under-qualification, not a content defect. Recorded for a land-clean lifter's discretion;
  I do NOT force the edit (audit-class: at-most-one-line stale-token fix, and this is not stale,
  merely under-qualified — below the forced-fix bar).
- **No DIRECTIVE-1 leak found.** Every MPI-path mention (`geodata.cpp` partitioning, `rap.*`
  ParOperator/RAP, the MPI collectives leg) stays in the §"Accreting working context — deferred
  MECHANISM" / §Evidence "cited, NOT lifted" framing. No MPI form was lifted into a claim.
- **c139 KaTeX recurrence guard: moot.** I touched NO chapter body line. The fence-check confirmed
  the only `$S`-sigil line outside a ` ```text ` fence (L137) is inside an inline backtick code
  span within a nested bullet-list continuation (4-space = list nesting, NOT a code block) —
  backtick code spans are not KaTeX-parsed, so no collision. The real pseudocode signature blocks
  (L45-58 `restrict_to_block`/`subdomain_reduce`; L69-86 `restrict_op_to_block`/`subdomain_solve`)
  are correctly inside ` ```text ` fences.
