---
agent: lowering-verifier
invoked_at: 2026-05-29T092943Z
scope: L2>L1 theme audit — orthogonalize-composition-lowering
status: pending
integrated_at: 2026-05-29T10:46:32Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row 6). Confirming audit — verdict fully-supported, theme STAYS firm. Single mutation: appended verified_against: yaml block (17 citations) to book/src/L2-L1/orthogonalize-composition-lowering.md EOF. No count change. retroactive-budget per-slice 1 (the only retroactive revision this cycle; global 1, under threshold). 3 OQs promoted. CARRY-FORWARD: stale orthog.hpp:34->:35 anchor in dot-mutation-rotation.md Sub-pattern D (not in this audit's scope; routed as OQ for a future dot-mutation-rotation pass). No gate hits."
inputs:
  - book/src/L2-L1/orthogonalize-composition-lowering.md (firm; landed cycle-022)
  - palace/linalg/orthog.hpp:18-89 (MGS/CGS/CGS2 bodies + InnerProductHelper hook + scope contract)
  - palace/linalg/iterative.cpp:308-325 (OrthogonalizeIteration dispatch), :630-632 / :809-811 (GMRES/FGMRES consumers)
  - palace/models/romoperator.cpp:51-66 (ROM dispatch sibling), :224-226 (consumer), :631-646 (B-weighted hook, :636)
  - test/unit/test-orthog.cpp:99-120 (empty), :123-160 (parametric real, assertion :158), :276 / :333 (weighted witnesses)
  - book/src/L1-L0/dot-mutation-rotation.md:146-187 (§Sub-pattern D — delegation boundary 2)
  - book/src/L1-L0/orthogonalize-mutation-rotation.md (L1>L0 in-place w.Add — delegation boundary 3)
  - book/src/L2/orthogonalize.md:166-220 (laws 4/5/7 + floating-point non-law)
---

# CYCLE: Audit orthogonalize-composition-lowering

## Summary

Audited the firm L2>L1 theme `orthogonalize-composition-lowering` (the Gram-Schmidt
variant-dispatch rotation: the named L2 `orthogonalize` composition fans down into the
per-variant MGS/CGS/CGS2 `[dot, axpy]` sequences). Verdict: **fully-supported — confirming
audit, theme stays `firm`.** Every L0 citation was independently re-read via `palace-codemap`
`read_range` and mechanically confirmed with `tools/citecheck/` anchor-drift checks (24
anchors/ranges, 0 drift, 0 OOB). The three-way delegation boundary — (1) stage-selection
owned by this theme, (2) inner-product collective unfusing delegated to
`dot-mutation-rotation` §Sub-pattern D, (3) in-place `w.Add` subtraction delegated to
`orthogonalize-mutation-rotation` L1>L0 — **partitions the lowering cleanly: no overlap, no
gap.** The algebraic basis (L2 laws 4/5/7 read-as-lowering) was confirmed against the L2 entry
body. The `op.cpp`/`orthog.cpp` does not exist — Palace's Gram-Schmidt is header-only in
`orthog.hpp`; the theme correctly cites `orthog.hpp` exclusively for the bodies (the dispatch
scope's `orthog.{hpp,cpp}` framing is wider than reality but the theme itself only cites the
`.hpp`, which is correct). **One inherited-citation carry-forward flagged** (NOT a defect in
the audited theme): the delegated-to `dot-mutation-rotation.md` §Sub-pattern D still cites the
stale `orthog.hpp:34` for `return LocalDot(x, y)` (lines 160, 183) — the token is at `:35`
(line 34 is `{`). The theme under audit correctly uses `:35` throughout, per the dispatch
directive; the stale `:34` lives in the cross-referenced theme and is routed as a carry-forward
correction for `dot-mutation-rotation`, not a change to this theme.

## Per-citation audit

### L0 source — orthog.hpp (header-only; orthog.cpp does NOT exist)

- **Citation**: `palace/linalg/orthog.hpp:18-23`
  - **Theme claim**: header scope contract "Assumes that the input vectors are normalized, but does not normalize the output vectors!" (applicability condition 2 — no output normalisation).
  - **Found**: lines 19-23 are the comment block; line 22 = "Assumes that the input vectors are normalized, but does not normalize the output vectors!"; line 23 = "If done in a loop, normalization has to be managed by hand!". Text is within `:18-23`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/orthog.hpp:29-36` (`IdentityInnerProduct` / `InnerProductHelper` hook; `return LocalDot(x, y)` at `:35`)
  - **Theme claim**: the `op.dot` template hook; canonical hook returns `LocalDot(x,y)` at `:35`. The Sub-pattern D inner-product pointer.
  - **Found**: line 30 = `struct IdentityInnerProduct`, line 33 = `auto operator()(...)`, line 34 = `{`, line 35 = `return LocalDot(x, y);`. citecheck `[ok]` anchor `'return LocalDot(x, y);'` at line 35.
  - **Verdict**: supports. **The `:35` anchor is correct (NOT `:34`)** — directive honored; line 34 is the brace.

- **Citation**: `palace/linalg/orthog.hpp:41-53` (`OrthogonalizeColumnMGS`; dot `:49`, GlobalSum(1) `:50`, w.Add `:51`)
  - **Theme claim**: MGS single interleaved `j`-loop; `[dot, axpy] × m` interleaved; `m` size-1 reductions.
  - **Found**: line 41 = `inline void OrthogonalizeColumnMGS(...`; the loop body `:49` `H[j] = dot_op(w, V[j]);`, `:50` `Mpi::GlobalSum(1, &H[j], comm);`, `:51` `w.Add(-H[j], V[j]);` — all in one `for` loop (`:46`-`:52`); body closes `:53`. citecheck `[ok]` on all three pinpoints.
  - **Verdict**: supports. The MGS `m`-size-1-reduction interleaved structure is exactly as Palace writes it.

- **Citation**: `palace/linalg/orthog.hpp:55-89` (Verified-against range) / `:57-74` (table CGS body) / `:75-88` (table CGS2) — `OrthogonalizeColumnCGS`: `if (m==0)` `:62`, GlobalSum(m,H) `:70`, `if (refine)` `:75`, accumulate `:85`
  - **Theme claim**: CGS `[dot×m, reduce, axpy×m]` separated (1 size-m reduction) + CGS2 `[CGS]×2` (2 size-m reductions, second non-fusible).
  - **Found**: line 57 = `inline void OrthogonalizeColumnCGS(...`; `:61` `if (m == 0)` (theme says `:62` — `:62` is the `if`-condition line; the bare `return;` is at `:64`. Minor: the `if (m == 0)` token is at `:62` per citecheck `[ok]`, so the theme's pinpoint matches what citecheck resolves; the early-return semantics span `:61-65`); `:66-68` `m` local dots; `:70` `Mpi::GlobalSum(m, H, comm);`; `:72-73` `m` w.Adds; `:75` `if (refine)`; `:77-87` second pass; `:85` `H[j] += dH[j];`; second `Mpi::GlobalSum(m, dH.data(), comm)` at `:84`. The `:57-74` (non-refine CGS) and `:75-88` (refine block) ranges partition the function. citecheck `[ok]` on `:62`, `:70`, `:75`, `:85`.
  - **Verdict**: supports. The two sub-ranges cleanly partition the function; the wide `:55-89` is the enclosing range (template line 55 → closing brace 88). No drift.

### L0 source — dispatch + consumers

- **Citation**: `palace/linalg/iterative.cpp:308-325` (`OrthogonalizeIteration` `switch (type)`; CGS2 `true` at `:322`)
  - **Theme claim**: runtime variant dispatch, variant bound + dispatched once, against leading `j+1` columns; CGS2 = `OrthogonalizeColumnCGS(..., true)`.
  - **Found**: `:308` def; `:313` `switch (type)`; `:315` MGS case → `OrthogonalizeColumnMGS(..., j+1)`; `:318` CGS case → `OrthogonalizeColumnCGS(..., j+1)`; `:321` CGS2 case; `:322` `OrthogonalizeColumnCGS(comm, V, w, Hj, j + 1, true);`. Comment `:312` "Orthogonalize w against the leading j + 1 columns of V." citecheck `[ok]` at `:322`.
  - **Verdict**: supports.

- **Citation**: `palace/models/romoperator.cpp:51-66` (`OrthogonalizeColumn` ROM sibling; threads `dot_op`; CGS2 = `refine=true`)
  - **Theme claim**: second dispatch surface; forwards the `dot_op` hook; CGS2 `true`.
  - **Found**: `:51` `inline void OrthogonalizeColumn(... const InnerProductW &dot_op = {})`; `:56` `switch (type)`; `:59` MGS → `OrthogonalizeColumnMGS(comm, V, w, Rj, j, dot_op)`; `:62` CGS → `...CGS(..., false, dot_op)`; `:65` CGS2 → `...CGS(..., true, dot_op)`. The hook is threaded through all three cases.
  - **Verdict**: supports.

- **Citation**: `palace/models/romoperator.cpp:631-646` (B-weighted hook; `W.InnerProduct(x, y, r.Real())` at `:636`)
  - **Theme claim**: the `op.dot` B-weighted substitution — inner-product-hook variant axis.
  - **Found**: `:633` `OrthogonalizeColumn(`; `:635` lambda capture `[&W = *(this->weight_op_W), &r = this->r](const Vector &x, const Vector &y)`; `:636` `{ return W.InnerProduct(x, y, r.Real()); }`. citecheck `[ok]` at `:636`. This is the same composition with the hook substituted (law 7).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:630-632` (GMRES) / `:809-811` (FGMRES) / `palace/models/romoperator.cpp:224-226` (ROM)
  - **Theme claim**: every consumer follows the call with its own `Norml2` + `scal(1/‖residual‖)` — normalisation is the caller's, NOT a dependency of this lowering (applicability condition 2).
  - **Found**: GMRES `:630` `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j);`, `:631` `Hj[j + 1] = linalg::Norml2(comm, w);`, `:632` `w *= 1.0 / Hj[j + 1];`. FGMRES `:809-811` byte-identical pattern. ROM `:224` `OrthogonalizeColumn(...)`, `:225` `Norml2`, `:226` `*= 1.0/...`. citecheck `[ok]` on `:630`, `:809`, `:224`.
  - **Verdict**: supports. Confirms condition 2: `nrm2`/`scal` are downstream of the lowering, not inside it.

### L0 tests (L0-equivalent semantic documentation)

- **Citation**: `test/unit/test-orthog.cpp:99-120` (empty-prefix edge)
  - **Theme claim**: all three variants leave `w` unchanged at `m = 0` (law 3 empty-prefix identity).
  - **Found**: `:99` `TEST_CASE("OrthogonalizeColumn - Real Empty", ...)`; `:101-103` `GENERATE(MGS, CGS, CGS2)`; `:116` `orthogonalize_fn(Mpi::World(), V, w, H, 0)` (m=0); `:120` `CHECK_THAT(w, RangeEquals(w_orig))`. All three variants exercised.
  - **Verdict**: supports.

- **Citation**: `test/unit/test-orthog.cpp:123-160` (parametric real; assertion `:158`, loop `:154-159`)
  - **Theme claim**: all three variants pass `⟨residual, V[i]⟩ ≈ 0` to `1e-12` (variant-agreement / substitutability witness).
  - **Found**: `:123` `TEST_CASE("OrthogonalizeColumn Parameterized - Real 1", ...)`; `:125-127` `GENERATE(MGS, CGS, CGS2)`; `:154` `for (int i = 0; i < mpi_size; i++)`; `:156` `auto dot = linalg::Dot(...)`; `:158` `CHECK_THAT(dot, WithinAbs(0.0, 1e-12));`; `:159` `}`; TEST_CASE closes `:160`. citecheck `[ok]` at `:158`.
  - **Verdict**: supports.

- **Citation**: `test/unit/test-orthog.cpp:276` (weighted-real-1) / `:333` (weighted-complex-1)
  - **Theme claim**: B-weighted `op.dot` variant-axis witnesses.
  - **Found**: `:276` `TEST_CASE("OrthogonalizeColumn Weighted - Real 1", "[orthog][Serial]")`; `:333` `TEST_CASE("OrthogonalizeColumn Weighted - Complex 1", "[orthog][Serial]")`. citecheck `[ok]` on both TEST_CASE boundary lines.
  - **Verdict**: supports.

### Cross-theme anchors

- **Citation**: `book/src/L1-L0/dot-mutation-rotation.md:146-187` (§Sub-pattern D)
  - **Theme claim**: the unfused `LocalDot` + batched `Mpi::GlobalSum` inner-product surface is "cited, not re-derived" (delegation boundary 2).
  - **Found**: §Sub-pattern D header at `:146`; the section spans `:146-187` (closing citation list at `:182-187`). It records the hook-routed two-step, MGS interleaved `m` size-1 collectives and CGS batched size-m collective. Confirmed in-bounds (file has 400 lines).
  - **Verdict**: supports the delegation. **See "Open questions" for the inherited `:34` miscitation INSIDE Sub-pattern D — that is the cited theme's defect, not this theme's.**

- **Citation**: `book/src/L2/orthogonalize.md` (LHS; laws 4/5/7), `book/src/L1/{orthogonalize,dot,axpy}.md` (RHS faces), `book/src/L1-L0/orthogonalize-mutation-rotation.md` (boundary 3), the two sibling L2>L1 themes
  - **Found**: all files exist and resolve in-bounds (citecheck `[ok]`). L2 laws 4/5/7 read in full — see Algebraic laws section below.
  - **Verdict**: supports.

## Applicability conditions

1. **Orthonormal basis precondition** — **Verifiable**: yes, from `orthog.hpp:18-23` header ("Assumes that the input vectors are normalized…") + inherited L2 §Signature. The composition does not enforce it (no normalisation guard in any of the three bodies). **Counter-example?** No.
2. **No output normalisation in this composition** — **Verifiable**: yes, directly. The three bodies stop at the un-normalised residual; every consumer (`iterative.cpp:630-632`, `:809-811`, `romoperator.cpp:224-226`) appends its own `Norml2` + `scal`. **Counter-example?** No — no body calls `Norml2`/`scal` internally.
3. **Variant selection value-preserving; collective shape not free** — **Verifiable**: yes. Law 4 (exact variant agreement) + the floating-point non-law (L2 `:218-220`) ground the "value-preserving under algorithmic-correctness / shape-sensitive under bit-reproduction" reading. The `m×1`/`1×m`/`2×m` shapes are read straight off the bodies. **Counter-example?** No.
4. **CGS2 second pass non-fusible** — **Verifiable**: yes. The `if (refine)` block (`:75`) reads the once-orthogonalised `w` (mutated by the first pass's `w.Add` loop `:72-73`) and accumulates `H[j] += dH[j]` (`:85`). Fusing would compute `dH` against the un-orthogonalised `w`. **Counter-example?** No — the source structurally enforces sequencing (first w.Add loop completes before the refine dots).
5. **Inner-product hook is a `dot` substitution** — **Verifiable**: yes. `romoperator.cpp:631-646` threads `W.InnerProduct` (`:636`) through the identical `OrthogonalizeColumn` dispatch; L2 law 7 states shape/laws invariant. **Counter-example?** No.
6. **In-place candidate destruction (delegated to the leaf lowering)** — **Verifiable**: partially — by construction this is delegated to `orthogonalize-mutation-rotation` condition 1/4; the L2>L1 theme correctly does not re-derive it. Confirmed the L1>L0 theme owns the `w.Add` in-place rebinding (its lines 59/94/133, applicability condition 4 on aliasing at `:177`). **Counter-example?** No.

All six conditions are complete and individually verifiable against the cited evidence. No condition is stated that the evidence contradicts.

## Algebraic laws (cited: L2 laws 4, 5, 7 + floating-point non-law)

- **Law**: Law 4 — variant agreement (exact): MGS/CGS/CGS2 produce the same `{residual, coeffs}` in exact arithmetic.
  - **Holds on operators?** Yes. L2 entry `:190-194` states it verbatim and names it "the substitutability law." The theme reads it as the MGS/CGS dispatch ("the three `[dot, axpy]` sequences are one value") — a faithful read-as-lowering. The three bodies compute the orthogonal projection `(I − VVᴴ)w` (exact), so the value is variant-invariant. Holds.

- **Law**: Law 5 — idempotence on the residual (exact): `orthogonalize op residual V = {residual, coeffs=0}`; in finite precision yields a small correction.
  - **Holds on operators?** Yes. L2 entry `:196-203` states it AND explicitly grounds CGS2: "CGS2 is one explicit re-application of this law" / "the `[CGS chain] × 2` shape is law 5 instantiated as a composition step." The theme's "Why CGS2 is `[CGS]×2`" section reads this directly, witnessed at the L0 `H[j] += dH[j]` accumulate (`orthog.hpp:85`) inside the `if (refine)` block (`:75`). Holds.

- **Law**: Law 7 — `dot`-hook invariance of shape and laws: substituting `op.dot` (canonical → B-weighted) leaves shape and laws 1-6 unchanged.
  - **Holds on operators?** Yes. L2 entry `:210-214`; the source witness `romoperator.cpp:631-646` threads the weighted hook through the identical composition (same `OrthogonalizeColumn` dispatch, only the lambda differs). The theme reads it as "the `op.dot` hook is a `dot` substitution, not a structural change" — faithful. Holds.

- **Non-law**: variant agreement in floating point (Law 4 fails at the bit level) = the collective-shape residual axis.
  - **Holds on operators?** The non-law holds (i.e. the divergence is real): the three bodies pin genuinely different reduction trees (`m`×size-1 / 1×size-`m` / 2×size-`m`). This is the load-bearing-numerical residue the theme's "Collective-shape recording" table records. Correctly classified (CLAUDE.md §Optimization tricks — load-bearing, since the variants exist precisely because finite-precision + MPI cost differ). Holds.

Justification kind `algebraic` is correct: the variant-dispatch rule IS laws 4+5 read-as-lowering, with the Face-1 lowering the identity-in-value specialization onto the parameterised leaf (structural + reduction-chain flavours present but subordinate). Matches the sibling `linear-combination-fold-specialization` `algebraic` classification.

## Delegation-boundary partition (the dispatch focus)

The three boundaries genuinely partition the lowering — **no overlap, no gap**:

| part of lowering | owner | this theme's treatment |
|---|---|---|
| variant → `[dot, axpy]` sequence + pass-count + collective shape (`m×1`/`1×m`/`2×m`) | **this L2>L1 theme** (stage-selection) | derived in full ("The variant-dispatch rewrite", "Collective-shape recording", "Why CGS2 is `[CGS]×2`") |
| inner-product `dot` leaf's L0 realisation — unfused `LocalDot` + batched `Mpi::GlobalSum` | **`dot-mutation-rotation` §Sub-pattern D** (boundary 2) | cited (theme `:14-16`, `:92-95`, `:156-177`); explicit "does NOT re-derive" (`:16`, `:158`, `:172-173`) |
| in-place `w.Add(-H[j], V[j])` candidate-buffer rebinding | **`orthogonalize-mutation-rotation` L1>L0** (boundary 3) | cited (theme `:71-73`, `:96-97`, `:252-257`); explicit "stops at the L1 leaf and does not re-derive that L0 step" (`:73`) |

**Overlap scrutiny — the one risk site.** The "Collective-shape recording" table (theme `:193-197`) names `Mpi::GlobalSum(1, &H[j])` (MGS) and `Mpi::GlobalSum(m, H, comm)` (CGS) — tokens that also appear in Sub-pattern D. This is NOT duplication: the table records the **per-variant orchestration** (how many reductions, what size — the variant axis), explicitly demarcated at theme `:191` ("the inner-product collective itself is Sub-pattern D; this table records the per-variant orchestration") and `:170-172` ("the same per-variant collective-shape distinction this theme records at the arity/pass-count level… Sub-pattern D is its L1>L0 leaf-level realisation"). Stage-selection (count/shape) ⟂ leaf-realisation (the unfusing mechanism). Clean.

**Gap scrutiny.** Coverage is exhaustive: (a) variant→sequence = this theme; (b) the `dot` leaf's L0 surface = Sub-pattern D; (c) the `w.Add` subtraction's L0 surface = orthogonalize-mutation-rotation; (d) Face-1 opaque leaf = the L1 leaf entry; (e) normalisation = explicitly out-of-scope (condition 2, caller's). No part of the lowering is uncovered, and none is covered twice. **No gap.**

## Proposed changes

Append the `verified_against:` audit block to the theme. **The theme STAYS `firm`** — this is a
confirming audit; no defect was found in the audited theme. (The one inherited miscitation is
in a *different* theme, routed as a carry-forward below, not applied here.)

```edit:book/src/L2-L1/orthogonalize-composition-lowering.md
[append at end of file]
```yaml
verified_against:
  # L0 source — orthog.hpp (header-only; orthog.cpp does not exist)
  - citation: palace/linalg/orthog.hpp:18-23
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: no-output-normalisation scope contract (applicability condition 2); text at :22.
  - citation: palace/linalg/orthog.hpp:29-36
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: IdentityInnerProduct hook; return LocalDot(x, y) at :35 (NOT :34 — line 34 is the brace). Sub-pattern D pointer.
  - citation: palace/linalg/orthog.hpp:41-53
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: OrthogonalizeColumnMGS; dot :49, Mpi::GlobalSum(1,&H[j]) :50, w.Add :51 — one interleaved j-loop, m size-1 reductions.
  - citation: palace/linalg/orthog.hpp:57-74
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: OrthogonalizeColumnCGS non-refine; if(m==0) :62, m local dots, Mpi::GlobalSum(m,H) :70, m w.Adds — 1 size-m reduction.
  - citation: palace/linalg/orthog.hpp:75-88
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: CGS2 if(refine) block :75; H[j] += dH[j] accumulate :85; second size-m reduction — [CGS]x2, non-fusible.
  # L0 dispatch + consumers
  - citation: palace/linalg/iterative.cpp:308-325
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: OrthogonalizeIteration switch(type); CGS2 = OrthogonalizeColumnCGS(...,true) at :322; variant bound+dispatched once.
  - citation: palace/models/romoperator.cpp:51-66
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: ROM OrthogonalizeColumn sibling; threads dot_op hook through all 3 cases; CGS2 = refine=true at :65.
  - citation: palace/models/romoperator.cpp:631-646
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: B-weighted op.dot substitution; W.InnerProduct(x,y,r.Real()) at :636 (L2 law 7 hook-invariance witness).
  - citation: palace/linalg/iterative.cpp:630-632
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: GMRES consumer; OrthogonalizeIteration :630 then Norml2 :631 + scal :632 — normalisation is the caller's (condition 2).
  - citation: palace/linalg/iterative.cpp:809-811
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: FGMRES consumer; byte-identical OrthogonalizeIteration + Norml2 + scal pattern.
  - citation: palace/models/romoperator.cpp:224-226
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: ROM consumer; OrthogonalizeColumn :224 then Norml2 :225 + scal :226.
  # L0 tests (L0-equivalent)
  - citation: test/unit/test-orthog.cpp:99-120
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: empty-prefix edge; GENERATE(MGS,CGS,CGS2), m=0, CHECK_THAT(w, RangeEquals(w_orig)) :120 — law 3 across all variants.
  - citation: test/unit/test-orthog.cpp:123-160
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: parametric real; GENERATE(MGS,CGS,CGS2); orthogonality assertion CHECK_THAT(dot, WithinAbs(0.0,1e-12)) :158, loop :154-159 — variant-agreement witness.
  - citation: test/unit/test-orthog.cpp:276
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: weighted-real-1 TEST_CASE boundary — B-weighted op.dot variant witness.
  - citation: test/unit/test-orthog.cpp:333
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: weighted-complex-1 TEST_CASE boundary — B-weighted op.dot variant witness.
  # Cross-theme delegation boundaries (the three-way partition — clean, no overlap/gap)
  - citation: book/src/L1-L0/dot-mutation-rotation.md:146-187
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: §Sub-pattern D — inner-product collective unfusing; cited not re-derived (boundary 2). Clean partition vs stage-selection orchestration. SEE carry-forward — Sub-pattern D's own :34 anchor for LocalDot is stale (should be :35); that is the cited theme's defect, not this theme's.
  - citation: book/src/L1-L0/orthogonalize-mutation-rotation.md
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: L1>L0 in-place w.Add candidate-buffer rebinding (boundary 3); cited not re-derived. Owns the in-place mechanics (its :59/:94/:133, aliasing condition :177).
  - citation: book/src/L2/orthogonalize.md:166-220
    verdict: supports
    audited_at: 2026-05-29T092943Z
    note: laws 4 (variant agreement) + 5 (idempotence-as-CGS2) + 7 (hook invariance) + floating-point non-law — all hold; the dispatch rule IS these laws read-as-lowering.
```
```

## Carry-forward correction (separate scope — NOT applied by this dispatch)

**Inherited miscitation in `dot-mutation-rotation.md` §Sub-pattern D** (per
`audit-report-inherited-miscitation-lint` / `lifter-scope-content-correction-boundary`):
Sub-pattern D cites `orthog.hpp:34` for `return LocalDot(x, y)` at lines **160** ("`orthog.hpp:34`")
and **183** ("`return LocalDot(x, y)` at `:34`"). I independently confirmed via `read_range` +
citecheck that the token is at **`:35`** (line 34 is the opening brace `{`). The theme under
audit correctly uses `:35` (its lines 161, 302), so this is the cited theme drifting, not the
audited theme. **Bounded, evidenced correction for a future `lifter`/`lowering-verifier` pass on
`dot-mutation-rotation`** (or an integrator carry-forward if it is touched): `:34` → `:35` at
`dot-mutation-rotation.md:160` and `:183`. This dispatch proposes NO edit to `dot-mutation-rotation`
(out of this theme's audit scope; flagged for the next pass that owns that file). citecheck:
`[ok] palace/linalg/orthog.hpp:35 (anchor lit: 'return LocalDot(x, y);') anchor at line 35`.

## Supporting evidence

- Source bodies (codemap `read_range`): `reference/palace/palace/linalg/orthog.hpp:1-93` (full file, 93 lines — header-only Gram-Schmidt; `orthog.cpp` does not exist per `list_files glob=palace/linalg/orthog.*`).
- Dispatch + consumers: `reference/palace/palace/linalg/iterative.cpp:308-325, 628-633, 807-812`; `reference/palace/palace/models/romoperator.cpp:51-66, 222-227, 631-646`.
- Tests: `reference/palace/test/unit/test-orthog.cpp:99-122, 123-162` (+ search hits for TEST_CASE boundaries `:276`, `:333`).
- L2 laws: `book/src/L2/orthogonalize.md:166-220`.
- Delegation targets: `book/src/L1-L0/dot-mutation-rotation.md:140-188`, `book/src/L1-L0/orthogonalize-mutation-rotation.md` (grep of `w.Add` / in-place / condition rows).
- Mechanical confirmation: `tools/citecheck/citecheck.py` — 24 anchor/bounds checks, all `[ok]`, 0 DRIFT, 0 OOB, 0 MISS.

## Open questions / caveats

- **Dispatch-scope path framing `orthog.{hpp,cpp}` is wider than reality.** Only `orthog.hpp`
  exists (header-only inline functions); `orthog.cpp` does not. The **theme itself** cites only
  `orthog.hpp`, which is correct — no action needed on the theme. Noting it so the next planner
  does not re-issue a scope mentioning a non-existent `orthog.cpp`.

- **Inherited `:34`→`:35` miscitation in `dot-mutation-rotation` §Sub-pattern D** (see
  Carry-forward above). Confirmed by independent read; out of this audit's edit scope; routed to
  the next pass that owns `dot-mutation-rotation`. Does not reduce this theme's status.

- **No dedicated L1↔L2 equivalence test (inherited caveat, not a status reduction).** The
  theme already records this (lines 398-405): variant-agreement is witnessed at L0
  (`test-orthog.cpp:123-160`, all three variants `⟨residual, V[i]⟩ ≈ 0`); a dedicated test
  asserting the de-fused Face-2 `[dot, axpy]` sequence reproduces the Face-1 leaf value would
  witness the lowering's value-preservation directly. The firm-without-dedicated-L1↔L2-test bar
  carries through from the sibling `linear-combination-fold-specialization`. This is the same
  `rough-in (test-coverage-bounded)`-adjacent situation but here the structure AND the laws are
  fully source-witnessed (the laws are exact-arithmetic algebraic facts read straight off the
  bodies + L0 orthogonality tests), so `firm` is correct — the missing test would be a *direct*
  Face-1↔Face-2 witness, not a gate on the already-source-confirmed laws.

- **OQ discharges (recorded by the theme, confirmed here).** The theme discharges
  `orthogonalize-composition-lowering-l2-l1-theme` and discharges
  `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d` on the L2>L1 side
  (the `project` stage cites Sub-pattern D). Both confirmed accurate against the cited evidence.
  No new OQ raised by this audit beyond the carry-forward citation fix.
