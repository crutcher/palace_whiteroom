---
agent: lowering-verifier
invoked_at: 2026-05-28T233000Z
scope: L2>L1 theme audit — linear-combination-fold-specialization
status: pending
inputs:
  - reports/2026-05-28T231508Z-abstractor-l2-l1-linear-combination-theme/CYCLE.md (the theme under audit)
  - palace/linalg/vector.cpp:695-775 (AXPY / AXPBY / AXPBYPCZ free-function bodies — self-read_range)
  - palace/linalg/vector.hpp:300-320 (the three free-function template decls; arity ceiling)
  - palace/linalg/nleps.cpp:338-346 (γ=1 iterated-chain witness)
  - palace/models/romoperator.cpp:184-191 (γ=1 iterated-chain witness, two-per-step)
  - palace/models/timeoperator.cpp:214-219 (γ=0 fall-through witness)
  - reports/2026-05-28T231026Z-harvester-linear-combination-L2/CYCLE.md (the L2 LHS laws 2/5/6/7)
---

# CYCLE: Audit linear-combination-fold-specialization (L2>L1)

## Summary

Audited the abstractor's L2>L1 lowering theme `linear-combination-fold-specialization`
(landed `firm`), which narrates how the L2 variadic fold `linear_combination` lowers into
the four fixed-arity L1 BLAS-1 leaves (scal / axpy / axpby / axpbypcz) via an
arity-dispatch fusion-selection rule, with an arity-≥4 iterated `γ=1` accumulate-fold
fall-back, plus a load-bearing-numerical summation-order table. **Verdict:
fully-supported.** Every L1 RHS primitive is real and each arity→primitive mapping is
semantically faithful to the L0 bodies I independently `read_range`-confirmed. The
arity-3→arity-2 `γ==0` fall-through is grounded exactly at `vector.cpp:749-751`
(self-read). The summation-order bit-divergence claim is **verified-sound** in substance
(the two arity-3 branches genuinely run distinct rounding schedules: the `γ==0` branch is
a single fused two-term pass `add(α,x,β,y,z)`; the `γ≠0` else-branch materializes
`α·x + γ·z` into `z` in one pass and then folds `β·y` in a *separate later* pass via
`z.Add(β,y)` — confirmed at `:751`, `:755`, `:756`). **One wording imprecision** in the
prose at theme `:200` overstates the γ==0 branch as summing "all three contributions in
one strided pass" — it sums **two** (`α·x + β·y`); the third `γ·z` term is dropped because
γ==0. The summation-order *table* (`:196`) states this correctly ("single fused pass
`add(α, x, β, y, z)`"). I propose a one-word fix; the underlying numerical claim is sound,
so this is not a status reduction. One forward-dependency caveat for the integrator: the
LHS anchor `book/src/L2/linear_combination.md` is a same-cycle harvester sibling
proposed-change not yet on disk; the link strands unless the harvester report is
integrated together with (or before) this theme.

## Per-citation audit

### `vector.cpp:702-712` — AXPY(double, const Vector &, Vector &)
- **Theme claim**: `α==1.0` fast-path `y += x` (FMA-free add) else `y.Add(α, x)`
  (`y ← y + α·x`); the arity-2-coeff-1 (`axpy`) leaf's pinned order.
- **Found** (self-read `:700-714`): function signature at `:702`, body `:703-712`:
  `if (alpha == 1.0) { y += x; } else { y.Add(alpha, x); }`. Exactly as claimed.
- **Verdict**: supports.
- **Notes**: range `:702-712` captures signature + full body; the `template <>` line is
  `:701` (one line above) — the body content is fully inside the cited range. No drift.

### `vector.cpp:726-730` — AXPBY(double, const Vector &, double, Vector &)
- **Theme claim**: `→ add(alpha, x, beta, y, y)`: single fused aligned in-place
  linear-combine (one strided pass, fewest roundings).
- **Found** (self-read `:725-730`): signature `:726`, `{` `:727`, `add(alpha, x, beta, y, y);`
  at `:729`, `}` `:730`. Exactly as claimed.
- **Verdict**: supports.
- **Notes**: `add(...)` confirmed at `:729` via `search_text`. The body range `:726-730`
  is accurate.

### `vector.cpp:745-758` — real-real AXPBYPCZ (the load-bearing range)
- **Theme claim**: branches on γ:
  `if (gamma == 0.0) { add(alpha, x, beta, y, z); }` (`:749-751`, arity-3→arity-2 collapse
  / law-5 witness) `else { AXPBY(alpha, x, gamma, z); z.Add(beta, y); }` (`:753-756`,
  general arity-3 two-pass split).
- **Found** (self-read `:745-757` + `search_text`):
  - `if (gamma == 0.0)` at `:749`, `{` `:750`, `add(alpha, x, beta, y, z);` at `:751`,
    `}` `:752`. → theme's `:749-751` is **exact**.
  - `else` `:753`, `{` `:754`, `AXPBY(alpha, x, gamma, z);` at `:755`, `z.Add(beta, y);`
    at `:756`. → theme's `:753-756` is the **enclosing else-block range** (brace at :753
    through the two statement lines :755-756); accurate as an enclosing range, though the
    two *statements* are precisely `:755-756`.
- **Verdict**: supports.
- **Notes**: this is the keystone citation. Both branch ranges land. The `γ==0` branch IS
  a single fused two-term pass; the `else` branch IS a genuine two-pass split (an
  AXPBY-into-z that itself is `add(α,x,γ,z,z)`, then a separate `z.Add(β,y)`). The
  semantic substance of the bit-divergence claim is fully grounded here. (See
  "Algebraic laws" below for the precise reconciliation.)

### `vector.hpp:305-316` — AXPY/AXPBY/AXPBYPCZ free-function template decls
- **Theme claim**: the bounded-arity surface; ceiling at `AXPBYPCZ` (no arity-4 fused
  kernel `AXPBYPCZPDW`).
- **Found** (self-read `:300-320`): `// Addition y += alpha * x.` + `AXPY` decl
  (`:304-306`); `// Addition y = alpha * x + beta * y.` + `AXPBY` (`:308-310`);
  `// Addition z = alpha * x + beta * y + gamma * z.` + `AXPBYPCZ` (`:312-316`). The next
  declaration is `Sqrt` (`:318` onward) — no arity-4 linear-combine. Ceiling confirmed.
- **Verdict**: supports.
- **Notes**: the cited `:305-316` band brackets all three decls + their `// Addition`
  comments; the AXPY comment line is `:304` (one above the band start), but the three
  decls themselves are inside `:305-316`. The arity-ceiling-at-3 claim is sound.

### `nleps.cpp:343-344` — γ=1 iterated-chain witness (eigenvector synthesis)
- **Theme claim**: `AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())`
  + the `.imag()` line; `z=0.0` seed at `:340`; accumulate-into running `z`.
- **Found** (self-read `:338-346`): `z = 0.0;` at `:340`; `for (int j = 0; j < k; j++)`
  `:341`; `AXPBYPCZ(..., 1.0, z.Real())` at `:343`, `AXPBYPCZ(..., 1.0, z.Imag())` `:344`.
- **Verdict**: supports.
- **Notes**: the `γ=1` accumulate-into-output shape is exactly present; seed/loop
  structure matches the theme's `accumulate2` narrative. Self-verified.

### `romoperator.cpp:188-189` — γ=1 iterated-chain witness (ROM reconstruction)
- **Theme claim**: `AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())`
  + `.Imag()`; same accumulate-two-terms-into-`u` `γ=1` shape.
- **Found** (self-read `:184-191`): `for (... j += 2)` `:184`; `if (j + 1 < n)` `:186`;
  `AXPBYPCZ(..., 1.0, u.Real())` `:188`, `AXPBYPCZ(..., 1.0, u.Imag())` `:189`; `else`
  `:190` (the odd-tail branch the theme posits as `accumulate2 acc [(β,y)] = axpy(...)`).
- **Verdict**: supports — **stronger than the theme states**. This witness shows the
  literal `j += 2` two-terms-per-step chunking AND the `if (j+1 < n) ... else` odd-tail
  guard that exactly mirrors the theme's `accumulate2` two-cases definition (`:129-131`).
  The greedy-two-per-step chunking is not merely posited; it is open-coded in Palace here.
- **Notes**: Self-verified.

### `timeoperator.cpp:217` — γ=0 fall-through witness (RK stage)
- **Theme claim**: `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` (`γ=0`, collapses to
  `k2 ← RHS2 + dt·k1`).
- **Found** (self-read `:214-219`): `// k2 = rhs2 + dt k1` comment `:216`;
  `linalg::AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2);` at `:217`. The literal `0.0` γ and the
  comment confirm the value `k2 ← RHS2 + dt·k1` (γ·z dropped).
- **Verdict**: supports.
- **Notes**: Self-verified. Clean live witness of the arity-3→arity-2 fall-through.

### `book/src/L2/linear_combination.md` — L2 LHS anchor (live link)
- **Theme claim**: firm L2 fold; laws 2/5/6/7 + IEEE non-law are the selection rule +
  summation-order deferral source.
- **Found**: file does NOT exist on disk yet — it is the same-cycle harvester sibling's
  proposed-change (`reports/2026-05-28T231026Z-harvester-linear-combination-L2/CYCLE.md`,
  proposed `edit:book/src/L2/linear_combination.md`). I verified the laws against the
  harvester report directly: law 2 (concatenation-homomorphism, harvester `:140-147`),
  law 5 (zero-coefficient term-drop → γ==0 branch, `:163-166`), law 6 (specialization
  identities, `:173-179`), law 7 (permutation EXACT-ARITHMETIC, `:181-182`) + IEEE non-law
  (`:189-190`). All four laws exist as the theme describes, and the harvester explicitly
  defers the summation-order recording to THIS theme (harvester `:228-232`).
- **Verdict**: supports (pending integration order).
- **Notes**: forward-dependency, NOT a citation error. See Open questions.

## Applicability conditions

1. **Shared length axis (aligned-pass precondition).** As stated: `all tᵢ : Tensor[N]`.
   - **Verifiable**: yes — it is the L2 signature precondition and the precondition the
     5-arg fused kernel `add(α,x,β,y,z)` requires (strides one length axis). Consistent
     with the L0 bodies (all operate on same-sized `Vector`s).
   - **Counter-example?**: N/A within the BLAS-1 cohort (the precondition always holds).

2. **Arity ceiling at 3.** As stated: no `AXPBYPCZPDW`; arity ≥ 4 lowers to a sequence.
   - **Verifiable**: yes — confirmed at `vector.hpp:305-316` (family stops at AXPBYPCZ).
   - **Counter-example?**: no. Self-verified the hpp decl band.

3. **Selection is value-preserving; summation-order is not free.** As stated.
   - **Verifiable**: value-preservation follows from L2 laws 6+2 (audited against harvester
     report); the order-pinning is the table below. Both readings (algorithmic-correctness
     unconditional; bit-reproduction order-gated) are the standard load-bearing-vs-
     transparent split per CLAUDE.md. Sound.
   - **Counter-example?**: no.

4. **Arity-3→arity-2 fall-through requires literal-zero γ.** As stated: the `γ == 0.0`
   test is a runtime branch, non-zero-but-tiny γ stays `axpbypcz` two-pass.
   - **Verifiable**: yes — the L0 test is literally `if (gamma == 0.0)` at `:749`
     (self-read), an exact floating-point equality test. A tiny-but-nonzero γ does take
     the `else`. Exactly grounded.
   - **Counter-example?**: no.

5. **Element-type / scalar-promotion conformance.** As stated: real or complex overload;
   complex delegates to MFEM member ops `y.AXPBY(...)` / `z.AXPBYPCZ(...)`
   (`vector.cpp:732-744, :760-769`).
   - **Verifiable**: partially — I self-read `:731-744` (complex AXPBY overloads delegate
     to `y.AXPBY(...)`) and `:760-769` (complex AXPBYPCZ overloads delegate to
     `z.AXPBYPCZ(...)`). The delegation IS present and the cited ranges are accurate. The
     claim that the complex member ops use "the same operand order as the real path" is an
     MFEM-internal property (the member-op rounding schedule is upstream); I cannot confirm
     it from Palace source. Recorded as an open question (upstream-behavior dependency).
   - **Counter-example?**: none found; the operand-order-parity sub-claim is unverifiable
     from Palace source (MFEM upstream).

## Algebraic laws (cited)

- **Law 6 specialization identities** (scal/axpy/axpby/axpbypcz = `linear_combination [...]`)
  — gives arity-1/2/3 dispatch. **Holds on operators?** Yes. Each L1 leaf's value equals
  the fold over its fixed-length term list; verified against the L1 leaf definitions in the
  theme (`:93-96`) and the harvester law 6 (`:173-179`). The RHS primitives are real
  (all four L1 `.md` files exist on disk).
- **Law 2 concatenation-homomorphism** — licenses arity-≥4 split into iterated chain.
  **Holds on operators?** Yes. `linear_combination (a ++ b) = linear_combination a +
  linear_combination b` is the monoid homomorphism from `([(Scalar,Tensor[N])], ++, [])`
  to `(Tensor[N], +, zeros)`; folding a long list = running accumulate of fixed-arity
  chunks. The `γ=1` accumulate-into shape is the open-coded realization (witnessed at
  nleps `:343-344` / romoperator `:188-189`, both self-read). Sound.
- **Law 5 zero-coefficient term-drop** — the arity-3→arity-2 fall-through. **Holds on
  operators?** Yes, and uniquely it is grounded by *direct source transcription* of the
  in-source `γ==0` branch (`:749-751`, self-read), not just algebra. Strongest-grounded law.
- **Law 7 permutation EXACT-ARITHMETIC** + IEEE non-law — the order-agnostic-for-value /
  order-pinned-for-bits split. **Holds on operators?** The exact-arithmetic law holds
  (real-number associativity/commutativity); the IEEE non-law correctly states it does NOT
  hold bit-for-bit. This is the foundation of the summation-order table. Sound.

### Summation-order bit-divergence claim (the load-bearing-numerical keystone)

The theme claims (`:199-202`) the two arity-3 branches do NOT agree bit-for-bit. I audited
this against the self-read L0 body:

- **γ==0 branch** (`:751`): `add(α, x, β, y, z)` — ONE fused pass; per element
  `z[i] = α·x[i] + β·y[i]` (two products, one sum-rounding). **Two-term** sum.
- **γ≠0 else branch** (`:755-756`): `AXPBY(α, x, γ, z)` = `add(α, x, γ, z, z)` →
  `z[i] = α·x[i] + γ·z[i]` (one pass, partial-sum rounded into z[i]); THEN `z.Add(β, y)`
  → `z[i] = z[i] + β·y[i]` (a SECOND, LATER pass; a second sum-rounding on the
  already-rounded partial). **Three-term** sum, computed as `(α·x + γ·z) + β·y` with an
  intermediate materialization.

**Verdict: verified-sound in substance.** The else-branch genuinely uses a distinct
rounding schedule (an intermediate rounding of `α·x + γ·z` before `β·y` is folded in),
whereas a single fused three-term pass would round once. The claim that bit-for-bit
divergence exists between a fused single-pass three-term sum and the two-pass split is
correct, and the operand/pass structure is exactly grounded at `:751`/`:755`/`:756`.

**One wording imprecision (NOT a soundness defect).** The prose at theme `:200` says the
γ==0 branch "sums **all three** contributions in one strided pass." When γ==0 the third
term `γ·z` is dropped — the γ==0 branch sums **two** contributions (`α·x + β·y`). The
divergence the theme is really pointing at is between (a) the γ==0 *two-term* fused pass
and (b) the γ≠0 *three-term* two-pass split — these compute different VALUES anyway
(γ==0 vs γ≠0 are different inputs), so the bit-for-bit comparison is most precisely framed
as: *for the same three-term value, the fused-vs-split rounding schedules differ*, which
is what the table rows actually encode. The table itself (`:196`) is correct
("single fused pass `add(α, x, β, y, z)`" — two-term). Recommend tightening the prose; see
Proposed changes. The numerical content is sound; this is a one-word over-statement in the
narration, not in the verified table.

## Proposed changes

### Edit 1 (RECOMMENDED — prose precision, not a status change)

The theme body prose at `:200` should not say the γ==0 branch sums "all three"
contributions. Propose:

```edit:book/src/L2-L1/linear-combination-fold-specialization.md
[at the "Summation-order recording" prose, currently theme CYCLE.md :199-202]
~~~text
The two arity-3 branches do **NOT** agree bit-for-bit (the L2 entry / axpbypcz.md
non-law): the `γ==0` fused branch sums its two surviving contributions (`α·x + β·y`) in
one strided pass, whereas the `γ≠0` branch computes `α·x + γ·z` first and folds `β·y` in
afterward, so for the same three-term value the partial-sum magnitudes — and hence the
IEEE-754 rounding — differ.
~~~
```

(The `~~~` here represents the triple-backtick `text` fence in the actual file. The only
change is "all three contributions in one strided pass" → "its two surviving
contributions (`α·x + β·y`) in one strided pass" and the framing "for the same three-term
value". This is a prose-precision fix; the summation-order *table* needs no change.)

### Edit 2 (verified_against metadata — append to the theme file)

```edit:book/src/L2-L1/linear-combination-fold-specialization.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/vector.cpp:702-712
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: AXPY α==1.0 fast-path vs y.Add(α,x); self-read_range confirmed
  - citation: palace/linalg/vector.cpp:726-730
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: AXPBY -> add(alpha,x,beta,y,y) single fused pass; add() at :729
  - citation: palace/linalg/vector.cpp:749-751
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: γ==0 branch -> add(alpha,x,beta,y,z); EXACT range (if at :749, add at :751); arity-3→arity-2 collapse / law-5 witness
  - citation: palace/linalg/vector.cpp:753-756
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: γ≠0 else-block; AXPBY(alpha,x,gamma,z) at :755 then z.Add(beta,y) at :756; two-pass split summation order — enclosing range accurate, statements precisely :755-756
  - citation: palace/linalg/vector.hpp:305-316
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: AXPY/AXPBY/AXPBYPCZ free-fn decls; arity ceiling at AXPBYPCZ confirmed (next decl is Sqrt)
  - citation: palace/linalg/nleps.cpp:343-344
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: γ=1 iterated-chain witness; z=0.0 seed at :340, loop over j
  - citation: palace/models/romoperator.cpp:188-189
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: γ=1 iterated-chain witness; j+=2 two-per-step + if(j+1<n)/else odd-tail open-codes the accumulate2 two-cases
  - citation: palace/models/timeoperator.cpp:217
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: γ=0 fall-through witness; AXPBYPCZ(1.0,RHS2,dt,k1,0.0,k2), comment confirms k2 ← RHS2 + dt·k1
  - citation: palace/linalg/vector.cpp:732-744
    verdict: partially-supports
    audited_at: 2026-05-28T233000Z
    note: complex AXPBY overloads delegate to y.AXPBY(...); delegation present, but "same operand order as real path" is an MFEM-internal (upstream) property not confirmable from Palace source
  - citation: palace/linalg/vector.cpp:760-769
    verdict: partially-supports
    audited_at: 2026-05-28T233000Z
    note: complex AXPBYPCZ overloads delegate to z.AXPBYPCZ(...); same upstream-order caveat as :732-744
  - citation: summation-order-bit-divergence-claim
    verdict: supports
    audited_at: 2026-05-28T233000Z
    note: load-bearing-numerical claim VERIFIED-SOUND — γ≠0 else-branch genuinely two-pass (intermediate rounding of α·x+γ·z before folding β·y) vs γ==0 single fused two-term pass; one prose over-statement ("all three") flagged for Edit 1, table is correct
~~~
```

(The `~~~` represents the triple-backtick `yaml` fence in the actual emitted edit.)

## Supporting evidence

Source files self-read via `palace-codemap` `read_range` + `search_text` this invocation
(line numbers independently confirmed, not transcribed from the artifact under audit):
- `palace/linalg/vector.cpp:695-775` (AXPY :701-712, AXPBY :725-730, AXPBYPCZ :745-757 +
  complex overloads :731-744, :758-769); `search_text` pinned `if (gamma == 0.0)` → :749,
  `add(alpha, x, beta, y, z)` → :751, `AXPBY(alpha, x, gamma, z)` → :755,
  `z.Add(beta, y)` → :756, `add(alpha, x, beta, y, y)` → :729.
- `palace/linalg/vector.hpp:300-320` (three free-fn decls + arity ceiling).
- `palace/linalg/nleps.cpp:338-346`; `palace/models/romoperator.cpp:184-191`;
  `palace/models/timeoperator.cpp:214-219` (the three live witnesses).
- `reports/2026-05-28T231026Z-harvester-linear-combination-L2/CYCLE.md` (laws 2/5/6/7 +
  IEEE non-law + the explicit summation-order deferral to this theme, harvester :228-232).
- On-disk anchor check: `book/src/L1/{scal,axpy,axpby,axpbypcz}.md` all exist;
  `book/src/L2-L1/{index.md,chebyshev-iteration-fusion.md}` exist;
  `book/src/L2/linear_combination.md` does NOT yet exist (harvester sibling proposed-change).

The MFEM `add(a,v1,b,v2,vout)` 5-arg free function and `Vector::Add(a,v)` member are
upstream symbols (not in the Palace tree; `get_symbol_def add` / `search_text "void add("`
returned no Palace hits) — consistent with the theme's identification of them as MFEM ops.

## Open questions / caveats

1. **LHS anchor is a same-cycle forward dependency (integration-order caveat, NOT a
   citation error).** `book/src/L2/linear_combination.md` is the harvester sibling's
   proposed-change, not yet on disk. The four laws this theme leans on were verified
   directly against the harvester report. The live link `../L2/linear_combination.md`
   strands unless the integrator applies the harvester report together with (or before)
   this theme. **Carry-forward for the integrator: integrate the two reports as a pair
   (harvester first).**

2. **Complex-path operand-order parity is an upstream (MFEM) property.** The theme's
   condition 5 claims the complex overloads (`vector.cpp:732-744`, `:760-769`) use "the
   same operand order as the real path." The DELEGATION is verified (the complex overloads
   call `y.AXPBY(...)` / `z.AXPBYPCZ(...)`); the rounding-schedule parity is internal to
   MFEM's `ComplexVector` member ops and not confirmable from Palace source. Per CLAUDE.md
   (cite Palace, log upstream as OQ): the bit-faithful summation-order table is fully
   verified ONLY for the real-real path. Recommend the theme scope its summation-order
   table to the real-real path explicitly (it largely does: `:188-189` "real-real path; the
   complex paths delegate to MFEM member ops with the same operand order") — but the
   "same operand order" sub-claim should carry an upstream-unverified marker.

3. **Directionality (high→low) is compliant.** The chapter body narrates L2 → L1 forward
   (the `⇒` fusion-selection rewrites, theme `:113-181`). The reverse-direction lifting
   note is correctly quarantined under `## Open questions / caveats` (`:335-344`) with the
   explicit marker "reverse direction, working notes only — NOT in the high→low chapter
   body." No direction-of-definition violation.

4. **No dedicated test witness (inherited caveat).** Confirmed against the harvester
   report (`:451-457`): no unit test exercises the BLAS-1 linear-combination free
   functions (`test-vector.cpp` "Vector Sum" exercises `linalg::Sum`, a reduce-to-scalar).
   The theme inherits the firm-without-dedicated-test bar from the chebyshev-iteration
   precedent. Not a status reduction; recorded as-is.

5. **`:753-756` vs `:755-756` range nuance.** The theme cites the else-block as `:753-756`
   (enclosing range, brace at :753) while the two statements are precisely `:755-756`. Both
   the enclosing range and the statement-precise range are defensible; I confirmed the
   enclosing range lands the right code. No correction needed — recorded for the
   integrator's awareness only.
