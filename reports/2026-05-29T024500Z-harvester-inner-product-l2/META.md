---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T024827Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T025200Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize inner_product at L2" (harvester, stub→firm)

## Critique

### Checks run

**citation-validity — warning.** I independently re-read every load-bearing Palace
range via `palace-codemap read_range` / `search_text` (not trusting the report's
self-verification log). The conjugation self-consistency claim — Palace = `yᴴ x`
(arg-2 conjugated) across docs AND kernel bodies — verifies:
- `vector.cpp:263-267` `ComplexVector::Dot` body `{Re(x)Re(y)+Im(x)Im(y),
  Im(x)Re(y)−Re(x)Im(y)}` = `x·conj(y) = yᴴ x` (arg-2 `y` conjugated). Confirmed
  by direct expansion `(xr+i·xi)(yr−i·yi) = (xr·yr+xi·yi) + i·(xi·yr−xr·yi)`.
- `vector.cpp:269-274` `TransposeDot` is the same real part with **negated** imag
  cross-term + the `this==&y` `2·Im·Re` fast path. Confirmed (the report's
  one-sign distinction is exact).
- `vector.cpp:664-672` real `LocalDot` (single Hypre `hypre_SeqVectorInnerProd`,
  `MFEM_ASSERT(x.Size()==y.Size())` at `:667`) and `vector.cpp:674-685` complex
  `LocalDot` (four-real-dot lift, `&x==&y` imag=0 at `:679`). Confirmed.
- Doc strings: `vector.hpp:109` (`yᴴ x or yᵀ x`), `vector.hpp:242` and `:246`
  (`LocalDot`/free-function `Dot`, `yᴴ x or yᵀ x`), `operator.hpp:386` and `:391`
  (`yᴴ A x`). All confirmed on-line.
- Weighted free-function `operator.cpp:621-628` (real `Operator`): builds `Ax=A·x`
  then `Dot(comm, Ax, y) = yᴴ A x` (arg-2 `y` conjugated). `:631-638`
  (`ComplexOperator`) confirmed as the sibling overload.
- M-weighted call sites `boundarymodeoperator.cpp:85` (`linalg::Dot(comm, et,
  *Bttr, et)`, Poynting power, diagonal) and `:90` (`linalg::Dot(comm, en, Atn,
  et)`, cross-coupling, off-diagonal). Both confirmed on-line.
- `iterative.cpp:395` `beta = linalg::Dot(comm, z, r)` confirmed. `nleps.cpp:487`
  (`c,c`) and `:492` (`v,v`) confirmed.
- `tdot` zero-call-sites: `search_text TransposeDot` returns exactly two hits —
  `vector.hpp:112` (decl), `vector.cpp:269` (def). Zero callers confirmed.
- Test `test/unit/test-vector.cpp:206-207` (`double dot = vec1 * vec2;
  CHECK_THAT(dot, WithinRel(32.0))`) confirmed.
The cross-claim "the contradiction is Palace-vs-L1-entry, not Palace-internal" is
verified faithful — Palace's docs and bodies agree at `yᴴ x` with no internal
disagreement. The warning is for one **citation-range imprecision** (issue 1
below): the SPD-realness anchor `operator.cpp:614-616` cites the assertion (which
is at `:615-616`) but the report's prose attributes the "For SPD B, xᴴ B x is
real" comment to that range — the comment is actually at `:611`, three lines
outside the cited window. The assertion itself is in range; the construct is
correct; only the comment co-location is off by a few lines.

**surface-or-evidence — pass.** This is a surface-changing proposal (stub→firm
full rewrite + dep-map flip + SUMMARY de-stub), not a pure rotation_claim, so the
refinement-surface bar is met by construction. The defining fold-law
(split-additivity / length-concatenation-homomorphism `(length-concat,++) →
(Scalar,+)`, §"Algebraic laws" law 2) is grounded in the shape precondition
`MFEM_ASSERT(x.Size()==y.Size())` (`vector.cpp:667`) and the tiling/blocking trick
it licenses. The M-weighted member `xᴴ M y` is grounded in `operator.cpp:621-628`
+ `operator.hpp:386,391` and the verified Hermitian/SPD assertion
`operator.cpp:615-616`. The PSD-at-diagonal law (law 5) is double-anchored: the
`&x==&y` imag=0 elision (`vector.cpp:266,679`) and the SPD-realness assertion.

**rotation-quality — pass (the load-bearing judgment).** The L2 fold is a genuine
fusion rotation, strictly more abstract than its L1 leaves: it collapses three L1
operators (`dot`, `tdot`, `bilinear-form`) AND Palace's family of fused kernel
shapes (real single Hypre pass / complex four-real-dot lift / weighted pre-apply +
local-then-collective two-step) into ONE canonical `foldl (+) zero (zipWith kernel
x y)`. State-hiding / branch-coarsening compression — not a 1:1 rename. On the
**crux** (is pinning arg-1 against Palace's own arg-2 convention sound, or does it
introduce inconsistency?): I judge it **sound and internally consistent**.
(i) The pinning is *internally consistent with its own leaves* — `dot.md:43`
("conjugate-linear in the **first** argument", kernel `conj(x[i])·y[i]` at `:34`)
and `bilinear-form.md:63` (`bilinear_form(x,M,y)=xᴴ M y`) already pin arg-1; the
L2 entry inheriting unchanged is exactly what keeps fold-and-leaves in agreement.
Pinning to arg-2 instead would have *introduced* an inconsistency with the leaves.
(ii) The value-level divergence is *not erased*: `xᴴ y = conj(yᴴ x)` is stated
explicitly, and the reconciliation onto the L0 call is forward-handed to the L2>L1
theme — the correct high→low disposition (reverse-direction reconciliation belongs
in the lowering, not the L_n entry). (iii) The report correctly *reframes* the
wave-1 combinator-miner's "contradiction" as representation-vs-Palace, which I
independently confirmed (Palace is self-consistent). (iv) High→low discipline is
respected: L2 vocabulary throughout, the lowering plain-text forward-referenced to
dispatch #2's `inner-product-fold-specialization`. The only residual risk (a
reader could mis-sign at the boundary because the representation convention differs
from ground truth) is mitigated by the dedicated §"Conjugation convention
(pinned)", the conjugate-pair identity, and the real-projection-invisibility note
(`iterative.cpp:395`, `nleps.cpp:487,492`). The L1 precedent is unanimous. PASS.

**variant-axis-coverage — pass.** All three orthogonal axes are classified:
conjugation (Hermitian `dot` / unconjugated `tdot`, the unification axis),
element-type (real single-Hypre-kernel / complex four-real-dot lift), weight-
presence (`M=I` / M-weighted via pre-`apply_linop`). Two correctly-scoped-out
non-axes are flagged: the diagonal `y=x` (a consumer entry point, not an axis) and
the reduction tree (an L0 detail / the IEEE non-law, not an L2 axis). The
`tdot` zero-call-site / type-API-surface-only status is explicitly flagged at
member granularity with a stated reason it does not gate the entry's `firm` status.
No hidden branches.

**cross-reference-integrity — pass.** Every live `[link]` in the operator body
resolves: `../L1/dot.md`, `../L1/bilinear-form.md`, `../L1/apply_linop.md`,
`../concepts/dot.md`, `./linear_combination.md`, `./chebyshev-iteration.md` — all
exist. The claimed reciprocal section `linear_combination.md` §"Sibling fold: dot
is not subsumed" exists (line 256) — the over-unification guard is genuinely
two-sided. The L2>L1 theme `inner-product-fold-specialization.md` exists (stub) in
`book/src/L2-L1/` and is correctly forward-referenced **plain-text** (not a live
link). The consumer slugs `nrm2` / `matrix-weighted-norm` are referenced **only as
plain-text backticked slugs**, never as live links — important, because
`matrix-weighted-norm` lives at `book/src/L1/matrix-weighted-norm.md`, NOT at L2;
a live `[matrix-weighted-norm](./...)` would have been a dead link. As written
there is no build break. The dep-map row-26 replacement text matches the current
`L2/index.md:26` row verbatim, and the SUMMARY de-stub target
(`- [inner_product (stub)](./L2/inner_product.md)`) matches `SUMMARY.md:40`.

**edge-label-fidelity — pass.** The single structural edge-label is the dep-map
row flip at `book/src/L2/index.md:26`; the proposed-changes block cites that exact
line and the surrounding prose discusses exactly that row (rough-in→firm). No
mismatched L_{n+1}→L_n edge label (the lowering edge is deferred to dispatch #2,
correctly not claimed here).

**plan-kind-consistency — pass.** Declared kind is a `firm` L2 operator promoted
from `stub`; content shape matches — full Signature / Semantics / Algebraic-laws /
Variant-axes / Status, no rough-in placeholders left in the firm body. The
`tdot` type-API-surface-only and the no-dedicated-complex-test caveats are
correctly carried as **member-level** caveats explicitly stated as "not a status
reduction", consistent with the `partly-constructive`-adjacent / `firm`-with-caveat
precedents (`chebyshev-iteration`, `linear_combination`). The three proposed-change
blocks (full rewrite + dep-map flip + SUMMARY de-stub) are well-formed and mutually
consistent.

**skill-uptake-survey — warning.** The report's shape implies several relevant
skills: `verify-citation-range` (it self-verified ~14 ranges), `verify-rotation-
citation` / `propose-rotation` (it asserts a fusion rotation), `classify-variant-
axis` (it classifies a 3-axis family), and `find-tests-for-region` (it located the
real-dot unit test). The report carries the substance of all of these in its
self-verification log and the per-axis taxonomy, but **does not name any skill
invocation**. Pure-telemetry surface (non-blocking): the harvester appears to have
performed the equivalent procedures inline rather than via the named skills, or
omitted recording the invocation. Surfaced for the meta-phase skill-uptake signal.

### Issues found

1. **Citation-range imprecision — SPD-realness comment off-by-three.** Severity:
   low (warning). Location: CYCLE.md §"Algebraic laws" law 5 (line ~280) and
   §"Evidence" (`operator.cpp:614-616`, line ~542) and §"Status" first caveat
   (line ~470). The cited range `operator.cpp:614-616` captures the assertion
   `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real())`
   (actually at `:615-616`) but the prose attributes the comment "For SPD B, xᴴ B
   x is real" to that range; the comment is at `operator.cpp:611`, three lines
   above the cited window. The construct is correct and the assertion is in range —
   only the cited line span should extend to `:611-616` (or the comment attribution
   should be dropped) to be exact.

2. **Self-verification log line-span vs in-entry citation mismatch (cosmetic).**
   Severity: low (warning). Location: "Supporting evidence" self-verification log
   (line ~590) cites `operator.cpp:598-618` for `Norml2(…,B,Bx)` and the SPD
   assertion; the real-`Operator` `Norml2` begins at `:600` and the complex
   overload's "For SPD B" comment is at `:611`. The wide `598-618` window is
   defensible as "the Norml2 weighted-overload block", but pairs with issue 1 — the
   in-entry §"Consumer" cite `operator.cpp:598-618` for `Norml2(comm, x, B, Bx)`
   transcribes the body as `√ Dot(comm, Bx, x)`, which matches `:613-617`. No
   factual error; the span is just looser than necessary.

3. **`matrix-weighted-norm` is an L1 slug referenced in an L2 entry (latent
   layer-placement note, not an error here).** Severity: informational. Location:
   CYCLE.md §"Consumer (NOT an instance): nrm2 / matrix-weighted-norm" (line ~443)
   and dep-map replacement row (line ~42). The entry names `matrix-weighted-norm`
   as a consumer; the only `matrix-weighted-norm` artifact is
   `book/src/L1/matrix-weighted-norm.md` (there is no L2 one). The report correctly
   keeps every such reference **plain-text** (no dead link), so this is NOT a
   build-break and NOT a cross-reference failure. Flagged only so a downstream pass
   knows the consumer named here is the L1 operator (an L2→L1 plain-text consumer
   pointer), should anyone later try to upgrade it to a live link — that link would
   need to target `../L1/matrix-weighted-norm.md`, not a same-layer path.

4. **Skill invocations not named.** Severity: low (warning, telemetry only).
   Location: whole report — no §invoked-skills / no inline skill-invocation
   markers despite citation-range verification, rotation assertion, variant-axis
   classification, and test localization all being performed. Non-blocking; surfaced
   for the meta-phase skill-uptake survey.

No fail-severity issues. The conjugation-pinning crux — the make-or-break judgment
— is sound: the arg-1 pinning is internally consistent with both L1 leaves, the
value-level `xᴴ y ↔ yᴴ x` divergence is explicitly recorded and forward-handed to
the lowering rather than silently absorbed, and the Palace-self-consistency claim
is independently verified. The two citation-range nits are surgical (extend a span
/ drop a three-line-off comment attribution); the skill and layer-placement items
are telemetry.

## Repair

### Fixes attempted

- **Finding 1 [citation-validity, low]**: `operator.cpp:614-616` cited for the SPD-realness
  law-5 anchor, but the comment "For SPD B, xᴴ B x is real" is at `:611` (3 lines outside the
  cited window); the assertion `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9
  * dot.real())` is at `:615-616`.
  - **Decision**: repaired.
  - **Action**: re-verified the source via `mcp__palace-codemap__read_range` on
    `palace/linalg/operator.cpp:598-638` — confirmed comment at `:611`, `dot = Dot(comm, Bx, x)`
    at `:614`, assertion at `:615-616`, complex `Norml2` overload closing at `:617`. Corrected
    all three in-entry occurrences of the imprecise span:
    - §"Conjugation convention (pinned)" → §"Algebraic laws" law 5 (CYCLE.md ~line 280):
      `operator.cpp:614-616` → `operator.cpp:611-616, comment ... at :611, assertion at :615-616`.
    - §"Status" first paragraph (CYCLE.md ~line 472): `operator.cpp:614-616` →
      `operator.cpp:615-616, comment ... at :611`.
    - §"Evidence" `Norml2` entry (CYCLE.md ~line 542): assertion attribution `:614-616` →
      `:615-616` and comment-at-`:611`.

- **Finding 2 [citation-validity, cosmetic]**: the wide `operator.cpp:598-618` self-verification
  / consumer window includes a trailing blank line (`:618`); the weighted `Norml2` overload
  block ends at `:617`.
  - **Decision**: repaired (trivial tightening — drop the trailing blank line).
  - **Action**: tightened `operator.cpp:598-618` → `598-617` at the three sites that used it
    (§"Consumer" CYCLE.md ~line 452; §"Evidence" CYCLE.md ~line 542; §"Supporting evidence"
    self-verification log CYCLE.md ~line 593) plus the frontmatter `inputs:` self-verified-ranges
    manifest (CYCLE.md line 14). Annotated the self-verification-log entry with the real/complex
    sub-spans (`:598-606` real, `:608-617` complex).

- **Finding 3 [info]**: `matrix-weighted-norm` is an L1 slug (`book/src/L1/matrix-weighted-norm.md`)
  referenced plain-text in this L2 entry; no dead link.
  - **Decision**: not-needed. The reference is correctly kept plain-text (no live link, no build
    break). Per the critic's note this is a latent layer-placement flag for any *future*
    link-upgrade pass (which would target `../L1/matrix-weighted-norm.md`), not a defect now.
    Leaving plain-text as-is; nothing to repair.

- **Finding 4 [skill-uptake, telemetry]**: no named skill invocations despite citation-range
  verification / rotation assertion / variant-axis classification / test localization being
  performed inline.
  - **Decision**: not-needed. Pure meta-phase skill-uptake telemetry; non-blocking and outside
    repair authority (recording a skill invocation post-hoc would be fabricating provenance).
    Left for the meta-phase skill-uptake survey.

### Unrepairable findings

None. All four critic findings were either mechanical citation-range corrections (findings 1, 2 —
repaired) or non-actionable telemetry / latent-note items (findings 3, 4 — not-needed). The
conjugation-pinning crux passed as sound; no substantive authoring was required.

## Suggested resolution

`overall_status: ready`. The two citation-range fixes are surgical (verified against source via
`read_range` before editing); the surface, rotation (including the headline conjugation-pinning
crux), variant-axis, cross-reference, edge-label, and plan-kind checks all passed. Integrator
notes:
- The entry resolves OQ `inner-product-harvester-formalization-and-conjugation-pinning` and
  `inner-product-fold-sibling-candidate` (both flagged resolvable in CYCLE.md §"Open questions");
  close/migrate at integration.
- The L2>L1 lowering theme `inner-product-fold-specialization` is forward-referenced plain-text
  and remains a stub (dispatch #2's job) — no link-upgrade needed here.
- Finding 3's latent note: should any later pass live-link `matrix-weighted-norm`, the target is
  `../L1/matrix-weighted-norm.md` (L1, not same-layer).
