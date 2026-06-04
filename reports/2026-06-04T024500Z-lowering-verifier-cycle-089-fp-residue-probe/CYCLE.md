---
agent: lowering-verifier
invoked_at: 2026-06-04T024701Z
scope: L1 verb FP-residue law-confidence probe — matrix-weighted-norm (FP-side analog of cycle-088 structure-side norm-axiom discharge)
status: integrated
integrated_at: 2026-06-04T030135Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-089 D1 (LEAD). FP-residue DISCHARGE: the two FP sub-claims at book/src/L1/matrix-weighted-norm.md:69-70 inherit cleanly from firm constituents dot+apply_linop through a deterministic IEEE-754 outer √ over disjoint accumulators (the nrm2 precedent) — NO composition-specific FP property. §Status gate-(c) narrowed; a SECOND verified_against: YAML block appended (file now carries TWO blocks, both parse, 12 entries total). With BOTH math sides now discharged (structure-side c088 + FP-side c089), the SOLE remaining law-confidence driver is gate (a): the untested 4-arg SPD-weighted overload Norml2(comm,x,B,Bx) √-entry-point test. The verb DELIBERATELY STAYS rough-in (test-coverage-bounded); the firm flip + its ~30-file cascade is a separately-gated future wave. Touched book/src/L1/matrix-weighted-norm.md only. matrix-weighted-norm-firm-flip-and-cascade-wave queued as a RECOMMENDED batch-29 LEAD candidate (OQ). Repair FIRED on this report: a false 'zero Norml2 references' phrasing was caught + narrowed to 'SPD-weighted 4-arg overload' before landing (a citation-precision catch); complex-branch Dot :615 pinpoint added. Build clean (cargo make book + linkcheck2 exit 0, ~94s). Zero gate hits."
inputs:
  - book/src/L1/matrix-weighted-norm.md (the verb under probe; FP sub-claims at :69-70)
  - book/src/L1/dot.md (firm constituent; FP non-laws :79-80)
  - book/src/L1/apply_linop.md (firm constituent; FP non-laws :62-63)
  - book/src/L1/nrm2.md (firmness precedent; sqrt(dot) firm with inherited FP caveats :38,:60-61)
  - palace/linalg/operator.cpp:599-619 (the Norml2(comm,x,B,Bx) √-overload entry point)
---

# CYCLE: Audit matrix-weighted-norm — FP-residue law-confidence probe (cycle-089 D1)

## Summary

This is the SCOPED FP-side probe of `book/src/L1/matrix-weighted-norm.md` (the FP analog of
cycle-088's structure-side norm-axiom discharge). The single question: **can the two
floating-point sub-claims at `:69-70` be discharged to law-confidence WITHOUT a dedicated
√-entry-point test, by inheritance from the already-firm folded primitives (`dot`,
`apply_linop`), or does the `√(xᴴBx)` composition introduce a NEW floating-point property
that genuinely needs a positive test the corpus lacks?**

**Verdict: DISCHARGE.** Both FP sub-claims are redundant restatements of the firm constituents'
already-stated, already-firm FP non-laws, composed through a **deterministic IEEE-754 outer `√`**
(`operator.cpp:606`/`:618`) that introduces no new floating-point property. The dispositive
evidence is the **`nrm2` firmness precedent**: `nrm2 = √(dot(x,x))` is **firm** while carrying
the *same two* FP non-laws (strict-CS-in-FP, bit-determinism), precisely because its `√` is
deterministic and "`nrm2`'s non-determinism is entirely the `dot`'s" (`nrm2.md:38`).
`matrix-weighted-norm` is that exact shape with **one additional firm constituent** (`apply_linop`,
supplying `Bx`); its FP caveats are the **additive union** of two firm operators' FP caveats. No
composition-specific FP effect arises — `dot` and `apply_linop` share no intermediate accumulator
(`B.Mult(x,Bx)` fully materializes `Bx` at `:602` before `Dot(comm,Bx,x)` reads it at `:603`), so
there is no third error term emergent from the composition.

This DISCHARGE — combined with cycle-088's structure-side discharge of laws 4/6/7 — closes the
two remaining *law-confidence* drivers of the verb's `rough-in (test-coverage-bounded)` status.
**Per HARD CONSTRAINTS I do NOT flip the verb to firm and do NOT trigger the cascade.** The
proposed-changes block narrows §Status gate (c) to record the FP-side discharge and adds a
`verified_against:` block; the `## Status` token stays `rough-in (test-coverage-bounded)`. I
RECOMMEND queuing `matrix-weighted-norm-firm-flip-and-cascade-wave` as a batch-29 LEAD candidate
(see Open questions).

Top-level verdict: **partially-supported → FP-residue law-confidence DISCHARGED; verb stays
rough-in pending the separate gated firm-flip wave.**

## Per-citation audit

### Citation: book/src/L1/matrix-weighted-norm.md:69 (strict-Cauchy–Schwarz in FP)
- **Theme claim**: "law 6 can fail by ULP-level amounts due to the compound non-associativity
  (inner `dot` + inner `apply_linop`). Same caveat as `nrm2` plus an additional contribution from
  `apply_linop`."
- **Found (on disk, `:69`)**: text matches verbatim. The claim self-decomposes its error into
  exactly two named sources (`dot` non-associativity + `apply_linop` contribution).
- **Inheritance analysis**: `matrix-weighted-norm` law 6 (`:56`) is Cauchy–Schwarz in the
  *B-inner-product* `⟨x,y⟩_B := xᴴBy`, which is *computed as* `dot(apply_linop(B,x), y)`. Its FP
  realization is plain-`dot`-CS where the operands have first been mapped through `apply_linop`.
  The two and only two FP error sources are: (i) `dot`'s reduction non-associativity over the
  already-computed `Bx`/`By` (= `dot.md:80`'s strict-CS-in-FP non-law, applied to mapped
  operands), and (ii) the perturbation in `Bx`/`By` from `apply_linop`'s FP-linearity-strictness
  non-law (`apply_linop.md:63`) and representation non-determinism (`apply_linop.md:62`). There is
  no THIRD error term from the *act of composing* — the `√` is deterministic and monotone (preserves
  inequality direction exactly), and the buffers do not share accumulators. The text's "compound
  non-associativity (inner `dot` + inner `apply_linop`)" is literally the additive sum of two
  firm non-laws.
- **Verdict**: **supports** (DISCHARGE — inherited additively; no composition-specific property).
- **Notes**: The `nrm2` analog (`nrm2.md:60`) is firm with the identical strict-CS-in-FP caveat
  and no `apply_linop` term; `matrix-weighted-norm` adds exactly the one extra firm term.

### Citation: book/src/L1/matrix-weighted-norm.md:70 (bit-determinism across B-representations)
- **Theme claim**: "same load-bearing caveat as `apply_linop` — a sparse-matrix realisation of
  `B` and a matrix-free realisation of the same SPD operator produce results that agree
  mathematically but may differ at the bit level."
- **Found (on disk, `:70`)**: text matches verbatim; self-cites `apply_linop` as the source.
- **Inheritance analysis**: This is the *verbatim* `apply_linop.md:62` non-law ("Bit-determinism
  across operator representations": sparse-matrix vs matrix-free `A` differ at bit level), specialized
  to `A = B`. The `Bx`-divergence is `apply_linop`'s caveat; the subsequent `dot`-reduction order
  is `dot.md:79`'s caveat; the outer `√` is deterministic IEEE-754 (`matrix-weighted-norm.md:43`:
  "The outer `sqrt` is deterministic IEEE-754") — a deterministic monotone unary fn applied to a
  divergent value *preserves* divergence but *creates none*. Pure inheritance.
- **Verdict**: **supports** (DISCHARGE — verbatim inheritance from a firm constituent).
- **Notes**: `nrm2.md:61` carries the analogous "bit-determinism across reduction trees" caveat
  while firm — same precedent.

### Citation: palace/linalg/operator.cpp:599-619 (the √-overload entry point)
- **Theme claim**: the named entry point; real `√` at `:606`, complex `√(dot.real())` at `:618`.
- **Found (codemap read_range + citecheck --anchor, on-disk)**:
  - `:600-607` real specialization: `B.Mult(x, Bx); double dot = Dot(comm, Bx, x);
    MFEM_ASSERT(dot > 0.0, ...); return std::sqrt(dot);` — `√` confirmed at `:606`.
  - `:610-619` complex: `B.Mult(x.Real(), Bx.Real()); B.Mult(x.Imag(), Bx.Imag());
    std::complex<double> dot = Dot(comm, Bx, x); MFEM_ASSERT(...); return std::sqrt(dot.real());`
    — `√` confirmed at `:618`.
  - **Composition disjointness witnessed**: `B.Mult(x, Bx)` at `:602` fully writes `Bx` before
    `Dot(comm, Bx, x)` at `:603` reads it — the `apply_linop` stage and the `dot` stage share no
    intermediate accumulator, so no cross-stage FP error term can emerge. This is the mechanical
    basis for "additive, not emergent."
- **Verdict**: **supports**.
- **Notes**: `citecheck --anchor` confirmed `std::sqrt` at lines [606, 618] within 599-619; the
  individual `:606`/`:618` anchors confirmed exact on-disk (not codemap-only). Both √ are single
  unary IEEE-754 ops — correctly-rounded, deterministic, monotone.

### Citation: book/src/L1/dot.md:79-80 (firm constituent FP non-laws)
- **Theme claim (dependency)**: `dot` (firm, cycle-002) supplies the inner reduction; its FP
  caveats underwrite `matrix-weighted-norm:69-70`.
- **Found**: `dot.md:100` Status = `firm` "modulo the explicitly-recorded floating-point caveats".
  `:79` reduction-tree associativity non-law; `:80` "Sub-additivity / Cauchy–Schwarz strictness in
  floating point ... can fail by ULP-level amounts due to summation ordering."
- **Verdict**: **supports** (the inherited FP caveats are firm-grade and explicitly recorded).

### Citation: book/src/L1/apply_linop.md:62-63 (firm constituent FP non-laws)
- **Theme claim (dependency)**: `apply_linop` (firm, cycle-005) supplies `Bx`; its FP caveats
  underwrite `matrix-weighted-norm:69-70`.
- **Found**: `apply_linop.md:87` Status = `firm` "modulo the explicitly-recorded floating-point
  caveats". `:62` "Bit-determinism across operator representations" non-law (sparse vs matrix-free
  divergence — the `Bx`-divergence source for `:70`); `:63` FP-linearity-strictness non-law (the
  `Bx`-perturbation source for `:69`).
- **Verdict**: **supports**.

### Citation: book/src/L1/nrm2.md:38 (dispositive firmness precedent)
- **Theme claim (precedent)**: `nrm2 = √(dot(x,x))` is the structural precedent for a
  deterministic-`√`-over-reduction verb being firm with inherited FP caveats.
- **Found**: `nrm2.md` Status = `firm`. `:38` "The square root itself is a deterministic IEEE-754
  operation (correctly rounded), so `nrm2`'s non-determinism is **entirely** the `dot`'s." `:60`
  strict-CS-in-FP non-law (same as `dot`); `:61` bit-determinism non-law (same as `dot`).
- **Verdict**: **supports** (this is the load-bearing precedent — a firm verb of identical FP
  shape, lacking only the `apply_linop` term that is itself firm).

## Applicability conditions

The probe does not re-audit the verb's SPD/Hermitian/square applicability conditions (those are
the *structure-side*, discharged cycle-088). The FP probe's only applicability condition is:

- **Condition**: the two folded primitives are firm "modulo explicitly-recorded FP caveats".
  - **Verifiable**: yes — `dot.md:100` firm, `apply_linop.md:87` firm, both citecheck-confirmed.
  - **Found counter-example?**: no.
- **Condition**: the outer `√` is deterministic (so it contributes no FP non-determinism).
  - **Verifiable**: yes — `operator.cpp:606`/`:618` are single `std::sqrt` unary ops (IEEE-754
    correctly-rounded); `matrix-weighted-norm.md:43` and `nrm2.md:38` both state this explicitly.
  - **Found counter-example?**: no.
- **Condition**: the two FP error sources (`dot` reduction-order, `apply_linop` `Bx` perturbation)
  are *additive*, not coupled through a shared accumulator.
  - **Verifiable**: yes — `operator.cpp:602-603` materializes `Bx` fully before `dot` reads it.
  - **Found counter-example?**: no.

## Algebraic laws (FP-side)

| Sub-claim (`matrix-weighted-norm.md`) | Inherits from | New FP property at composition? | Disposition |
|---|---|---|---|
| `:69` strict-Cauchy–Schwarz in FP | `dot.md:80` (over mapped operands) + `apply_linop.md:63` | **No** — deterministic `√`, disjoint accumulators | DISCHARGE |
| `:70` bit-determinism across B-reps | `apply_linop.md:62` (verbatim) + `dot.md:79` | **No** — `√` deterministic monotone, divergence preserved not created | DISCHARGE |

Both rows resolve to "no composition-specific FP property" → the FP residue is a redundant
restatement of firm constituents' caveats → DISCHARGE. This is the FP-side analog of the
firm-on-positive-structure escape: where the structure-side escape rests on exact-arithmetic
theorems over provably-SPD `B` (cycle-088), the FP-side rests on the firm constituents' FP
non-laws composed through a deterministic `√` — exactly the `nrm2` precedent.

## Proposed changes

Touches `book/src/L1/matrix-weighted-norm.md` ONLY. Two edits:
(1) narrow §Status gate (c) to record the FP-side DISCHARGE (leaving the `## Status` token
`rough-in (test-coverage-bounded)` UNCHANGED — the verb is NOT promoted; gate (a)'s √-entry-point
test stays the sole remaining driver);
(2) append a `verified_against:` YAML block recording the inheritance derivation.

The verb has NO frontmatter `status:` line (status lives in `## Status` prose only), so there is
no token to leave un-flipped beyond the prose — confirmed.

### Edit 1 — narrow §Status gate (c) FP-residue clause

```edit:book/src/L1/matrix-weighted-norm.md
[replace the trailing two sentences of gate (c), currently:]

What this discharge does **NOT** cover, and why the verb stays `rough-in (test-coverage-bounded)`: the **floating-point** sub-claims at "Laws that do not hold" `:69-70` — strict Cauchy–Schwarz failing by ULP-level amounts (compound `dot`+`apply_linop` non-associativity) and bit-determinism across operator representations of `B` — are numerical claims about the realized arithmetic, not exact-arithmetic theorems, and remain genuinely test-bounded (inherited from `dot` / `apply_linop`). Gate (a)'s √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`) also stays open: the corpus has ZERO `Norml2` references in `test/unit/` (verified cycle-088). So the structure-side of 4/6/7 is closed; the FP-side and the entry-point test are the residue keeping the verb at rough-in.

[with:]

The **floating-point** sub-claims at "Laws that do not hold" `:69-70` are now ALSO discharged to law-confidence by **inheritance** (cycle-089 FP-residue probe), the FP-side analog of the cycle-088 structure-side discharge: (i) strict Cauchy–Schwarz failing by ULP-level amounts is the **additive union** of `dot`'s strict-CS-in-FP non-law (`book/src/L1/dot.md:80`, firm) applied to the `apply_linop`-mapped operand `Bx` plus `apply_linop`'s FP-linearity-strictness non-law (`book/src/L1/apply_linop.md:63`, firm); (ii) bit-determinism across operator representations of `B` is the **verbatim inheritance** of `apply_linop`'s representation-non-determinism non-law (`book/src/L1/apply_linop.md:62`, firm) plus `dot`'s reduction-tree non-determinism (`book/src/L1/dot.md:79`). The outer `√` (`palace/linalg/operator.cpp:606` real, `:618` complex) is **deterministic IEEE-754** (correctly-rounded, monotone) and `B.Mult(x,Bx)` fully materialises `Bx` (`:602`) before `Dot(comm,Bx,x)` reads it (`:603`), so the two error sources are additive across disjoint accumulators and the composition introduces **NO new floating-point property**. This is exactly the `nrm2` firmness precedent (`book/src/L1/nrm2.md:38`: "the square root itself is a deterministic IEEE-754 operation ... so `nrm2`'s non-determinism is entirely the `dot`'s"; `nrm2` is **firm** carrying the same two FP non-laws), extended by one additional **firm** constituent (`apply_linop`). With the FP-side now discharged, the **sole** remaining driver of `rough-in (test-coverage-bounded)` is gate (a)'s direct √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`): the corpus has ZERO references to the **SPD-weighted 4-arg overload** `Norml2(comm,x,B,Bx)` in `test/unit/` (the only `Norml2` hits are the unweighted 2-arg `linalg::Norml2(comm,x)` and the `mfem::Vector::Norml2()` method form — a different operator, `nrm2`; verified cycle-089). The structure-side (laws 4/6/7, cycle-088) and the FP-side (laws `:69-70`, cycle-089) are both closed; **only the entry-point test remains**. The combined discharge LICENSES — but does not itself enact — a future full-firm flip of the verb; that flip plus its ~30-file cascade is a separately-gated wave (recommended batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`, see the cycle-089 D1 probe report).
```

### Edit 2 — append `verified_against:` block

The verb already carries one `verified_against:` block (the cycle-080 + cycle-088 entries at
`:145-171`). Append the cycle-089 FP-residue entries as a SECOND fenced YAML block immediately
after the existing one (downstream `cross-layer-cross-cutter` extracts all fenced `verified_against:`
blocks; a second block is well-formed). The block is parse-validated (`python3 -c "import yaml;
yaml.safe_load(...)"` → PARSE OK, 6 entries; no `note:` begins with a quote character of either
kind).

```edit:book/src/L1/matrix-weighted-norm.md
[append at end of file, after the existing verified_against block's closing fence:]

**FP-residue law-confidence DISCHARGE (cycle-089 D1 probe)** — the floating-point sub-claims at
`:69-70` inherit additively from the firm constituents `dot` / `apply_linop` through a deterministic
outer `√`; no composition-specific FP property remains (the `nrm2` firmness precedent extended by
one firm constituent). The verb stays `rough-in (test-coverage-bounded)` pending ONLY gate (a)'s
√-entry-point test.

~~~yaml
verified_against:
  - citation: book/src/L1/matrix-weighted-norm.md:69
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: cycle-089 FP-residue probe DISCHARGE of the strict-Cauchy-Schwarz-in-FP sub-claim; the ULP-failure mode is the additive union of dot's CS-strictness non-law (book/src/L1/dot.md:80, firm) over the apply_linop-mapped operand Bx plus apply_linop's FP-linearity-strictness non-law (book/src/L1/apply_linop.md:63, firm); the outer sqrt at operator.cpp:606/618 is deterministic IEEE-754 and introduces no new error term; exactly the nrm2 firmness precedent (nrm2.md:38/60) extended by one firm constituent, no composition-specific FP property
  - citation: book/src/L1/matrix-weighted-norm.md:70
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: cycle-089 FP-residue probe DISCHARGE of the bit-determinism-across-B-representations sub-claim; verbatim inheritance of apply_linop's representation-non-determinism non-law (book/src/L1/apply_linop.md:62, firm sparse-vs-matrix-free divergence) plus dot's reduction-tree non-determinism (book/src/L1/dot.md:79); deterministic monotone sqrt preserves but does not create divergence; no composition-specific FP property
  - citation: book/src/L1/dot.md:79-80
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: firm constituent FP caveats inherited - :79 reduction-tree associativity non-law, :80 strict-Cauchy-Schwarz-in-FP ULP non-law; dot is firm (dot.md:100) modulo these explicitly-recorded FP caveats
  - citation: book/src/L1/apply_linop.md:62-63
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: firm constituent FP caveats inherited - :62 bit-determinism-across-operator-representations non-law (Bx divergence source), :63 FP-linearity-strictness non-law; apply_linop is firm (apply_linop.md:87) modulo these explicitly-recorded FP caveats
  - citation: book/src/L1/nrm2.md:38
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: dispositive firmness precedent - nrm2 = sqrt(dot(x,x)) is FIRM carrying the same two FP non-laws (nrm2.md:60 strict-CS, nrm2.md:61 bit-determinism) because the sqrt is deterministic IEEE-754 and nrm2's non-determinism is entirely dot's; matrix-weighted-norm is the same shape with one added firm constituent apply_linop
  - citation: palace/linalg/operator.cpp:599-619
    verdict: supports
    audited_at: 2026-06-04T024701Z
    note: outer sqrt entry points confirmed deterministic-IEEE-754 unary ops - :606 return std::sqrt(dot) real, :618 return std::sqrt(dot.real()) complex; the radicand dot=Dot(comm,Bx,x) at :603/:615 fully materializes Bx before the reduction (B.Mult completes before Dot reads), so dot and apply_linop share no intermediate accumulator and the composition adds no third FP error term
~~~
```

## Supporting evidence

- `palace/linalg/operator.cpp:599-619` — the `Norml2(comm,x,B,Bx)` √-overload (codemap read_range
  + citecheck `--anchor 'std::sqrt'` → lines [606, 618]; individual `:606`/`:618` confirmed exact
  on-disk). The radicand-before-√ ordering at `:602-603` is the disjoint-accumulator witness.
- `book/src/L1/dot.md:79-80` (FP non-laws), `:100` (firm Status) — firm constituent #1.
- `book/src/L1/apply_linop.md:62-63` (FP non-laws), `:87` (firm Status) — firm constituent #2.
- `book/src/L1/nrm2.md:38,:60-61` — the dispositive firmness precedent (firm `√(dot)` verb with
  identical inherited FP caveats).
- `book/src/L1/matrix-weighted-norm.md:43` — "The outer `sqrt` is deterministic IEEE-754" (the
  verb's own statement of the determinism that makes the inheritance clean).
- cycle-088 structure-side discharge (the existing `verified_against:` block `:159-170`) — the
  companion half; together they close both law-confidence drivers.

## Open questions / caveats

- **RECOMMENDED batch-29 LEAD candidate: `matrix-weighted-norm-firm-flip-and-cascade-wave`.** With
  the structure-side (cycle-088) and FP-side (cycle-089, this probe) law-confidence both discharged,
  the verb's `rough-in (test-coverage-bounded)` rests on a SINGLE remaining driver: gate (a)'s
  direct √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`), which the corpus lacks (ZERO references
  to the SPD-weighted 4-arg overload `Norml2(comm,x,B,Bx)` in `test/unit/` — the 7 extant `Norml2`
  hits are all the unweighted 2-arg `linalg::Norml2(comm,x)` or the `mfem::Vector::Norml2()` method
  form, a different operator; verified cycle-089). **Judgment for the planner:** gate (a) is a *test*-coverage gate, but
  the firm-on-positive-structure escape (CLAUDE.md §Methodology invariants, the `apply_linop` /
  `eigenfreq_qfactor_reduce` / `sparameter_reduce` / `solve_family` precedents) MAY now apply — the
  laws are inner-product-space theorems on provably-SPD `B` (structure-side, exact-arithmetic) plus
  FP non-laws inherited from firm constituents (FP-side); the missing test does not gate
  *syntactic-identity / inherited* laws. A firm-flip wave should (i) re-judge gate (a) against the
  escape now that BOTH law-sides are discharged, and (ii) if it flips, carry the ~30-file cascade
  (the verb is referenced widely — `nrm2`, the three eigensolver backends ARPACK/SLEPc/NLEPS, the
  L0 chapters, the bilinear-form sibling, plus every maturity-token co-mention). **This probe does
  NOT flip and does NOT trigger the cascade — per HARD CONSTRAINTS.** Recommend the wave run a
  whole-`book/src/` cross-reference grep of the old `rough-in (test-coverage-bounded)` token on
  `matrix-weighted-norm` co-mentions before flipping (firm-promotion coupled re-anchor guard).
- **Directionality**: not applicable — this is an L1-verb audit, not a lowering-theme directionality
  check. The verb narrates own-layer (L1) semantics; no high→low directionality concern.
- **Out-of-scope-for-this-probe**: I did not re-audit the verb's structure-side laws (cycle-088),
  the SPD construction provenance (`eigensolver.cpp:205-213`, `spaceoperator.cpp:530-537`, already in
  the existing block), nor gate (a)'s test question (that is the firm-flip wave's call). This probe's
  scope is strictly the `:69-70` FP sub-claims.
- **No new stale-reference residue introduced**: the proposed edits touch §Status prose + append a
  `verified_against:` block within the verb's own file; the `## Status` token is UNCHANGED, so no
  cross-file maturity-token re-anchor is owed by this probe (the firm-flip wave owns that grep).
