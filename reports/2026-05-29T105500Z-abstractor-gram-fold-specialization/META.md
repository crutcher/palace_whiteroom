---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T113000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T114500Z
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

# META: verification of "L2>L1 theme sketch — gram-fold-specialization"

## Critique

### Checks run

**citation-validity — pass.** Self-verified the load-bearing L0 anchors against the live Palace
tree via `palace-codemap` `read_range` / `search_text`:
- `palace/linalg/nleps.cpp:524-531` — confirmed `Eigen::MatrixXcd SS(k, k);` at `:524` then the
  nested `for (int i...) { for (int j...) { SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]); } }`,
  cell body exactly at `:529`. `search_text linalg::Dot\(GetComm\(\), X` over `nleps.cpp` returns
  **exactly one** hit (line 529) — the report's "sole literal Gram-build site" and "exactly one
  occurrence" claims are correct.
- `:515-518` (k==0 early-return), `:520-523` (coord extraction `x2(j) = b2(j) - linalg::Dot(...,
  x1, X[j])`), `:532-535` (the `S = eig_opInv*I - H`, `SS = -S.fullPivLu().solve(SS)`, `x2 =
  SS.fullPivLu().solve(x2)`, `MatVecMult` consumer), `:561-569` (residual-deflation second
  consumer, `rr2(j) = linalg::Dot(..., vv, X[j])` at `:568`), `:613-619` (basis growth
  `X.resize(k+1); X[k]=v; ... k++`), `:354-362` (Jarlebring/Koskela/Mele 2018 + SLEPc-NEP
  minimality-index-1 + Effenberger 2013) — **all verified in-range and content-accurate.**
- `vector.hpp:248` free-function `Dot(comm, x, y)` → `LocalDot(x, y)`; `vector.cpp:263-266`
  `ComplexVector::Dot` body computes `Re = xr·yr + xi·yi`, `Im = xi·yr − xr·yi` = `x·conj(y) =
  yᴴx` (**arg-2 conjugated**) — the conjugation-handedness chain the whole theme rests on is
  verified correct.
Two **cosmetic off-by-one over-extensions** (in-range, no claim drift): (i) `vector.cpp:263-267`
cited for `ComplexVector::Dot` — the body closes at `:266`, `:267` is blank; (ii) `vector.cpp:664-672`
cited for the real `LocalDot` single-Hypre-pass — the function decl is `:665`, `:664` is the blank
line after the preceding `}`. Both include one adjacent non-load-bearing line; the complex
four-real-dot `:674-685` is exact. Artifact anchors into `L2/gram.md` (`:42-50`, `:73-85`,
`:117-122`, `:124-126`, `:130-135`, `:153-156`, `:158-164`, `:166-176`, `:178-182`, `:197-202`,
`:213-216`, `:242-246`) all spot-checked and content-accurate, including the forward-reference at
`:242-246` this theme closes. Net: pass — no fabricated or out-of-range citation; the two issues are
boundary-trim cosmetics for the repairer's optional tidy.

**surface-or-evidence — pass.** This is a `new:` L2>L1 theme chapter (new surface), not a
refinement of an existing operator/theme. It carries a full proposed-changes block authoring the
chapter text plus two append-only edits to shared index files. The refinement-shape rule (surface
+ rotation_claim, or retroactive-evidence-backfill) is satisfied by new-surface authorship with
its own evidence base; not a pure rotation_claim. Applicable and passes.

**rotation-quality — pass.** The asserted rotation is a genuine L2→L1 lowering: one L2
matrix-valued fold `gram dot X = Matrix (\i j -> dot X[j] X[i])` re-fuses **downward** into a `k×k`
grid of L1 per-cell `dot`/`bilinear_form` leaves materialized by the `:525-531` double loop. The
L2 form is strictly more compact/abstract (a single all-pairs fold with one hook field) than the
L1 form (an explicit nested-loop materialization of `k²` scalar invocations). The matrix-specific
structural content — double-loop materialization of the all-pairs definition law + the "select the
leaf once, apply k² times" uniform-dispatch simplification — is real abstraction collapse, not a
1:1 rename. Pass.

**variant-axis-coverage — pass.** The orthogonal axes are explicitly enumerated and each is
covered or scoped: (1) **conjugation/hook** — canonical Hermitian `dot` vs unconjugated `tdot`
(the latter flagged structurally-firm-but-behaviorally-unexercised: `TransposeDot` has zero call
sites; correctly scoped as a known caveat, not a hidden branch); (2) **element-type** real vs
complex (real → single Hypre pass; complex → four-real-dot, the NLEPS case) — both covered; (3)
**weight** canonical `XᴴX` vs B-weighted `XᴴBX` via `bilinear_form` (the rough-in arm, explicitly
scoped as L1-rough-in-not-gating); (4) **single-set vs cross-Gram** (`gram` vs `gram2`) — handled
as a two-index-set degeneration. The symmetry-exploitation triangle-mirror is correctly classified
as a transparent-perf-trick non-axis (consistent with `L2/gram.md:213-216`), and basis cardinality
`k` as the fold parameter (non-axis). No hidden branch. Pass.

**cross-reference-integrity — pass.** All eight referenced book files exist (`L2/gram.md`,
`L2-L1/inner-product-fold-specialization.md`, `L1/dot.md`, `L1/bilinear-form.md`,
`L2/inner_product.md`, `L2-L1/index.md`, `SUMMARY.md`, `L2/index.md`). The new slug
`gram-fold-specialization` is wired into both `SUMMARY.md` (append after line 56,
orthogonalize entry) and `L2-L1/index.md` theme table (append after line 16, orthogonalize row) —
both edits verified accurate against current file state (4 existing index rows; SUMMARY Part
structure at lines 51-57). The in-chapter `[link]`s (`../L2/gram.md`, `../L1/dot.md`,
`../L1/bilinear-form.md`, `./inner-product-fold-specialization.md`, `../L2/inner_product.md`) all
resolve to existing files. **Build-readiness / firm-body-inside-fence guard:** the firm-claimed
theme body is fully ENCLOSED in the `new:` fence — fence opens at CYCLE.md line 39
(`` ````new:... ``), closes at line 515 (`` ```` ``); the chapter's `## Status` (line 424),
`## The dispatch rewrite`, `## Justification kind`, `## Verified-against`, and all firm apparatus
sit INSIDE the fence (39-515). Fence enumeration: outer 4-backtick pair balanced (39/515, 517/526,
528/537); the four nested 3-backtick `text` fences (77/84, 109/116, 136/140, 200/203) are balanced
and correctly nested inside the higher-backtick-count outer fence. The two `$$` display-math blocks
(lines 93-94 spanning, line 192 inline) are balanced pairs (4 `$$` markers = 2 pairs). No
cycle-019 fence-truncation signature. Pass.

**edge-label-fidelity — pass.** Edge label is L2>L1 throughout. The prose narrates exactly that
edge: L2 `gram` fold (LHS) lowering forward into L1 per-cell `dot`/`bilinear_form` leaves (RHS).
Direction is consistently high→low; no L4/L3 or mis-stated adjacent edge. The non-adjacent identity
relationships are not invoked. Pass.

**plan-kind-consistency — pass.** Declared kind is `firm` L2>L1 theme. Content shape matches: the
dispatch rule IS the `gram` all-pairs definition law (`L2/gram` law 1, verified at
`gram.md:117-122`) read as a lowering, composed pointwise with the **already-firm** sibling
`inner-product-fold-specialization`. No rough-in placeholders in the rewrite body; the two carried
caveats (`tdot` unexercised-but-structurally-firm; `bilinear-form` rough-in-at-L1) are correctly
scoped as non-status-reducing on the theme, with the firmness resting on read-direct positive
evidence (`nleps.cpp:524-531`/`:529`) + firm-sibling composition, no negative-anchor
reconstruction. The "Coverage caveat (not a status reduction)" framing for the single-Gram-build
site is consistent with the codified status tiers. Firm classification is appropriate. Pass.

**skill-uptake-survey — pass (telemetry).** The report invokes the right procedural disciplines:
`verify-citation-range` producer-self-verification is named in §Verified-against (and the live
codemap self-verification is evidenced by the `search_text` hit-count claims, which I confirmed).
The classify-variant-axis discipline is exercised in the explicit axis enumeration + the
transparent-trick-vs-axis classification. No skill-shape is implied-but-absent. Surfaces clean.

### Issues found

1. **Citation boundary over-extension (cosmetic, low severity)** — §Verified-against /
   §Per-cell summation-order recording, CYCLE.md:397-398 and :260. `vector.cpp:263-267` for
   `ComplexVector::Dot` extends one line past the body (closes at `:266`; `:267` blank);
   `vector.cpp:664-672` for the real `LocalDot` single-Hypre-pass leads with one blank line (decl
   at `:665`; `:664` blank). Both are in-range and carry no claim drift — the complex four-real-dot
   `:674-685` is exact. Candidate for a boundary trim only; does not affect any claim.

2. **`dot.md:43` convention anchor is one line below the convention statement (cosmetic, low
   severity)** — §L1 form (RHS), CYCLE.md:125. The arg-1-conjugated `⟨x,y⟩ = xᴴ y` convention is
   stated at `dot.md:42` (the §Semantics "Conjugation convention" line); `:43` is the adjacent
   C++-surface note ("`(*this).Dot(y) = yᴴ·(*this)`"). The cited anchor lands in the right region
   and the claim is accurate; the precise line is `:42-43`. Trivial.

3. **No structural, surface, rotation, edge, variant, or kind defect found.** The load-bearing
   finding — `linalg::Dot(comm, a, b) = bᴴa` (arg-2 conjugated), so `SS(i,j) = linalg::Dot(comm,
   X[i], X[j]) = X[j]ᴴ X[i] = inner_product(X[j], X[i])`, making the conjugate-pair re-order a
   **no-op as Palace writes it** but **observable under loop-index transpose / operand swap** — is
   verified correct against the source chain (`vector.hpp:248` → `vector.cpp:264-266`) and is
   correctly framed as a load-bearing claim (the off-diagonal complex cells feed the
   `fullPivLu().solve` at `nleps.cpp:533-534`, consumed by value). No speculative operators
   promoted; both sides are existing vocabulary (LHS `gram` firm; RHS `dot`/`tdot` firm +
   `bilinear-form` rough-in), correctly recorded as `Speculative L1 operators: None`. The shared
   `L2-L1/index.md` + `SUMMARY.md` edits are append-only and verifiably distinct from the parallel
   `deflate-composition-lowering` (gram builds the matrix; deflate solves it — different rows,
   no collision), with explicit integrator coordination notes.

---

## Repair

### Fixes attempted

- **Finding 1 — Citation boundary over-extension (cosmetic, low severity).**
  - **Decision**: repaired.
  - **Action**: trimmed the two non-load-bearing adjacent lines off both cited `vector.cpp`
    ranges, in all four occurrences in CYCLE.md. Verified the exact boundaries via
    `palace-codemap read_range` against the live tree before editing:
    - `ComplexVector::Dot` — decl `:263`, `{` `:264`, return spans `:265-266`, closing `}` `:266`;
      `:267` is blank. Corrected `vector.cpp:263-267` → `vector.cpp:263-266` at CYCLE.md §"The
      per-cell conjugate-pair re-order" (the L0-surface citation), §Justification-kind (the
      value-level-identity verification citation), and §Verified-against (the L0-evidence-range
      bullet).
    - `LocalDot` (real single-Hypre-pass) — `:664` blank, decl `:665`, body `:666-671`, closing
      `}` `:672`. Corrected `vector.cpp:664-672` → `vector.cpp:665-672` at CYCLE.md §"The dispatch
      rewrite" (element-type-key bullet) and §"Per-cell summation-order recording" (the real-Gram
      reduction-tree table row).
    These are pure boundary trims — no claim text changed; both ranges were already in-range with
    no claim drift (the critic confirmed). The complex four-real-dot `:674-685` was already exact
    and is untouched.

- **Finding 2 — `dot.md:43` convention anchor one line below the convention statement (cosmetic,
  low severity).**
  - **Decision**: not-needed.
  - **Rationale**: re-read the live `book/src/L1/dot.md` — line `:42` is blank; the full
    conjugation-convention statement (`⟨x, y⟩ = xᴴ y`) AND the C++-surface note
    (`(*this).Dot(y) = yᴴ·(*this)`) are both on line `:43`. The CYCLE.md citation
    `[dot](../L1/dot.md):43` therefore already lands exactly on the convention statement. The
    critic's read placed the statement at `:42` and the note at `:43`, but against current file
    state the cited `:43` is correct as written. No edit applied (a "correction" to `:42-43` would
    have introduced the blank line `:42`).

- **Finding 3 — No structural/surface/rotation/edge/variant/kind defect.**
  - **Decision**: not-needed (informational pass note from the critic, not a defect).

### Unrepairable findings

None. Both flagged findings were cosmetic and in-range; finding 1 was a trivial boundary trim
(repaired), finding 2 was already-correct as cited (not-needed).

## Suggested resolution

`ready`. All 8 critic checks pass; the only two findings were low-severity cosmetic
citation-boundary nitpicks. Finding 1's boundary over-extensions are trimmed in-place (four
occurrences); finding 2 required no change (the cited `dot.md:43` already lands on the convention
statement in the live file). No substantive authoring, no contradictions, no deferred work.

Integrator notes (carried from the report, not repair actions): (a) this theme closes the
`book/src/L2/gram.md:242-246` forward-reference — a lifter / layer-intro-author cross-reference
refresh naming `gram-fold-specialization` is the standard follow-up; (b) surface the new OQ
`gram-percell-dot-vs-fused-matmul-tree-loadbearing`; (c) the `book/src/L2-L1/index.md` +
`book/src/SUMMARY.md` appends are append-only and explicitly non-colliding with the parallel
`deflate-composition-lowering` abstractor (gram row vs deflate row) — apply both.
