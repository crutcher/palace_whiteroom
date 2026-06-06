---
agent: layer-intro-author
invoked_at: 2026-06-06T185234Z
scope: relocate named-shape-groups general rule out of linear_combination entries to l4_calculus.md §1.2.1
status: pending
integrated_at: 2026-06-06T211500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-115 D3. DIRECT USER DIRECTIVE 2026-06-06. Applied clean (staging row 2). PROSE-ONLY trim of the general named-shape-groups rule/rationale/migration-note out of book/src/{L4,L3,L2}/linear_combination.md, leaving each to USE the notation + LINK to design/l4_calculus.md sec 1.2.1. NO l4_calculus.md edit (critic verified 1.2.1/1.2.2/4.1 already carry the complete rule). Reachability-neutral (HELD 133), rank_violations HELD 0. sec 1.2.1 anchor-links all resolve; no KaTeX/table breakage. Build EXIT 0, no build-repair. Promoted OQ named-shape-groups-general-rule-restatement-cohort-extent (27 files / 3 tiers, now governed by the forthcoming semantic-consolidation USER DIRECTIVE). citecheck 10 ok/16 AMBIG (ALL in the cohort-inventory FINDING prose, NONE backs an applied change; non-blocking)."
---

# CYCLE: named-shape-groups notation relocation (linear_combination entries → §1.2.1)

## Summary

DIRECT USER DIRECTIVE (2026-06-06): "the directive about the named tensor shape
groups (and the general syntax and rules) should not live in the
linear_combination entry; they should live at the level where the shape semantics
are described."

The general named-shape-groups notation rule (`Tensor[(S: ...)]` binding /
`Tensor[$S]` use, the rank-agnostic congruence rule, the `Tensor[N]`-as-rank-1
anti-pattern rationale, the "earlier rendering" migration note) is GENERAL
calculus-notation. Its authoritative home is **already complete** in
`book/src/design/l4_calculus.md` §1.2.1 / §1.2.2 / §4.1. I **verified those
sections carry the complete rule** (see §Verification) — **nothing needs to be
added there before relocating**; no rule is lost.

I then TRIM the general rule/rationale/migration-note OUT of the three named
`linear_combination` entries (L4/L3/L2), leaving each to (a) USE the notation in
its own shape contract and (b) LINK to §1.2.1 for the general rule. Each entry
KEEPS its OWN shape facts (signature, congruent over one group `S`,
element-local at every position of `S`, result shares `S`).

This dispatch is scoped to the user-named `linear_combination` entries. The same
restatement pattern recurs across ~27 cohort files — I REPORT that extent as a
FINDING (§Cohort-wide extent) for the user/meta-phase to decide on a cohort-wide
sweep, without sweeping it here.

## Verification — §1.2.1/§1.2.2/§4.1 is the complete home (nothing lost)

Read `book/src/design/l4_calculus.md`:

- **§1.2.1 Named shape groups** (`:62-74`) — carries: the `(S: ...)` binding
  semantics ("a name to a contiguous run of axes without committing to rank");
  the **binding-vs-use rule** (`:66` "A group is bound exactly once… every later
  occurrence… is a use, written with a `$` sigil: `$S`"); the `$` back-reference
  rationale; the partial-run form `Tensor[(S: a, ...), b]`; the
  whole-congruent-signature example (`:70`); the rank-wildcard `...` semantics
  (`:72`); and the **"Why this exists — the `Tensor[N]`-as-same-shape
  anti-pattern"** paragraph (`:74`) which states verbatim the directive the L4
  entry restates: *"Do not reach for a bare concrete axis like `Tensor[N]` to
  mean 'same shape as the other operand' — `Tensor[N]` denotes a rank-1 tensor of
  length `N` and silently pins the operands to one dimension. When the intent is
  congruence-of-unknown-rank, write `Tensor[(S: ...)]`… reserve `Tensor[N]` for
  genuinely rank-1 vectors."*
- **§1.2.2 Operator shapes — domain and range groups** (`:76-84`) — the
  `LinOp[(R: ...), (D: ...)]` domain/range two-group form, range-first
  convention, square/endomorphic `LinOp[(S: ...), $S]`, and the L1/L0
  keep-`Tensor[N]`-rank-1 note (`:84`). (Not used by `linear_combination`, which
  is domain≡range element-local; present and complete for the cohort.)
- **§4.1 Shape contracts on primitives** (`:303`) — the primitive-level rule:
  *"Where only a partial run of axes must agree across operands of unknown rank,
  name it with a shape group (§1.2.1) and reuse the name: every occurrence of a
  group `S` in a signature must resolve to one congruent axis-run… A named group
  is the rank-agnostic same-shape contract; a bare concrete axis (`Tensor[N]`) is
  not — it is a rank-1 commitment."*

**Conclusion:** every general-rule sentence the `linear_combination` entries
restate — the binding-vs-use rule, the `$` sigil, the `Tensor[N]`-is-rank-1
anti-pattern, the "reuse of `S` asserts congruence" rule, the
congruence-of-unknown-rank directive — is ALREADY present in §1.2.1 + §4.1. The
"earlier `Tensor[N]` rendering accidentally read as a single length axis"
migration note is a transient artifact of the c111 notation rollout and has no
authoritative home need at all (it documents a past edit, not a rule). So **no
addition to `l4_calculus.md` is required**; the relocation is pure trimming.

## Keep-vs-relocate judgment (per entry)

The line drawn (per the dispatch's judgment-call instruction — err toward keeping
the entry self-contained for its OWN shape but pointing to §1.2.1 for the
convention):

| Phrase in the entry | KEEP / RELOCATE | rationale |
|---|---|---|
| signature `:: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]` | KEEP | the op's own algebra |
| "all terms are *congruent*, sharing one shape group `S`" | KEEP | this op's own shape fact |
| "the combination is element-local at every position of `S`" | KEEP | this op's own shape fact |
| "result … same shape group `S` / `Tensor[$S]`" | KEEP | this op's own shape fact |
| "of arbitrary, unknown rank" | KEEP (concise) | states THIS op admits any rank — its own contract |
| "the name `S` carries the same-shape contract" | **RELOCATE** | general rule (== §4.1) |
| "reuse of `S` across the signature asserts congruence" | **RELOCATE** | general binding/use rule (== §1.2.1 `:66`) |
| "`S` is **not** pinned to rank-1 / NOT rank-1" | KEEP (trimmed to a parenthetical) | the op-specific consequence; the *general* anti-pattern teaching goes, the op's own "admits any rank" stays |
| "The earlier `Tensor[N]` rendering accidentally read as a single length axis; `(S: ...)` states the congruence-of-unknown-rank intent directly." | **RELOCATE (delete)** | the general anti-pattern directive + a past-edit migration note; lives in §1.2.1 `:74` |

Net: each entry retains a self-contained statement of ITS shape ("terms congruent
over one group `S` of arbitrary/unknown rank; element-local at every position of
`S`; result shares `S`"), with the existing §1.2.1 link in the "Shape contract"
preamble carrying the general convention. The general TEACHING (why `(S:...)`
beats `Tensor[N]`, binding-vs-use, the migration note) is removed.

## Proposed changes

### 1. `book/src/L4/linear_combination.md` — trim the over-stated shape-precondition bullet

The bullet at `:97-102` restates the general rule (`carries the same-shape
contract`) AND the anti-pattern migration directive. Trim to linear_combination's
OWN shape fact. The §1.2.1 link is already present in the "Shape contract"
preamble at `:90-91` (untouched).

```edit:book/src/L4/linear_combination.md
[old]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary, unknown rank (the name `S` carries the
  same-shape contract; `S` is **not** pinned to rank-1 — the combination is
  element-local at every position of `S`, see §"Algebraic laws"). The earlier
  `Tensor[N]` rendering accidentally read as a single length axis; `(S: ...)` states
  the congruence-of-unknown-rank intent directly.
[new]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary, unknown rank; the combination is
  element-local at every position of `S` (see §"Algebraic laws"). (The named-shape-group
  convention — binding `(S: ...)` vs use `$S`, and why a group beats a bare `Tensor[N]`
  — is the general calculus rule in [`l4_calculus`](../design/l4_calculus.md) §1.2.1,
  linked above.)
```

### 2. `book/src/L3/linear_combination.md` — trim the same-shape-contract / congruence-assertion restatement

The bullet at `:47` restates the general rule ("The name `S` carries the
same-shape contract; reuse of `S` across the signature asserts congruence"). Trim
to the op's own shape fact. The §1.2.1 link is already in the "Shape contract"
preamble at `:44` (untouched).

```edit:book/src/L3/linear_combination.md
[old]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*, sharing one shape group `S` of arbitrary (unknown) rank — NOT rank-1; the combination is element-local at every position of `S`. The name `S` carries the same-shape contract; reuse of `S` across the signature asserts congruence.
[new]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*, sharing one shape group `S` of arbitrary (unknown) rank; the combination is element-local at every position of `S`. (The general named-shape-group convention is in [`l4_calculus`](../design/l4_calculus.md) §1.2.1, linked above.)
```

### 3. `book/src/L2/linear_combination.md` — trim the same-shape-contract restatement (keep the fusion-precondition, which IS this op's own fact)

The bullet at `:82-86` restates the general rule ("The name `S` carries the
same-shape contract") AND adds an op-specific fact (the aligned-fusion-kernels
precondition — every term shares the shape the single aligned pass strides over).
The fusion-precondition is linear_combination's OWN shape consequence (KEEP); the
general "carries the same-shape contract" restatement goes. The §1.2.1 link is
already in the "Shape contract" preamble at `:77` (untouched).

```edit:book/src/L2/linear_combination.md
[old]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary (unknown) rank — NOT rank-1; the combination
  is element-local at every position of `S`. The name `S` carries the same-shape contract,
  and is also the aligned-fusion-kernels precondition — every term shares the shape the
  single aligned pass strides over.
[new]:
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary (unknown) rank; the combination
  is element-local at every position of `S`. This congruence is also the
  aligned-fusion-kernels precondition — every term shares the shape the
  single aligned pass strides over. (The general named-shape-group convention is in
  [`l4_calculus`](../design/l4_calculus.md) §1.2.1, linked above.)
```

## Anchor-link verification

All three entries point to `[`l4_calculus`](../design/l4_calculus.md) §1.2.1` in
their "Shape contract" preamble (L4 `:90-91`, L3 `:44`, L2 `:77`) — those links
are UNTOUCHED by the edits above, and `book/src/design/l4_calculus.md` §1.2.1
exists (verified, `:62`). The edits add no new link targets (the L4 edit's
parenthetical reuses the same `../design/l4_calculus.md` relative path already
resolving elsewhere in the file). `linkcheck2` impact: none — no link added or
removed resolves to a missing file; the relative path `../design/l4_calculus.md`
is the existing, working one. (Note: §-anchor fragments are not appended to the
link URLs in these entries — they cite "§1.2.1" in prose, link to the file — so
there is no fragment-anchor to break.)

## Cohort-wide extent (FINDING — NOT swept this dispatch)

The dispatch instructed: do the three named `linear_combination` entries; REPORT
the cohort-wide extent rather than sweep it. Grep over `book/src/L*/` +
`book/src/concepts/` for the general-rule restatement markers
(`carries the same-shape contract`, `NOT rank-1`, `not rank-1`, the
`earlier `Tensor[N]`` migration note, `accidentally read as`,
`congruence-of-unknown-rank`) returns **27 files**. They split into THREE tiers
by how much general rule they restate:

**Tier A — full general-rule restatement (the user-named target tier; relocate):**
- `book/src/L4/linear_combination.md:99-102` — the heaviest: same-shape-contract +
  rank-1 pin + the `Tensor[N]` migration note. (Handled above.)
- `book/src/L3/linear_combination.md:47` — "carries the same-shape contract; reuse
  of `S` … asserts congruence". (Handled above.)
- `book/src/L2/linear_combination.md:83-84` — "carries the same-shape contract".
  (Handled above.)

**Tier B — mid-weight: cites the general rule via a "named shape groups per
§1.2.1" link inside the bullet (already mostly relocated — they LINK, but still
carry a "NOT rank-1" general echo):**
- `book/src/L2/nrm2.md:77`, `book/src/L3/nrm2.md:59` — "of arbitrary unknown rank
  (NOT rank-1; named shape groups per [`l4_calculus`] §1.2.1)".
- `book/src/L2-L1/linear-combination-fold-specialization.md:35` — same form.
- `book/src/L3/blas1-intro.md:20` — same form (a group-intro page — its job is
  orientation, the §1.2.1 link is appropriate there; the "NOT rank-1" echo is the
  only relocatable bit).
- `book/src/concepts/elementwise-product.md:9,18` — concept page; `:18` links
  §1.2.1, `:9` carries a "NOT rank-1" echo in the base-primitive line.

**Tier C — light: a bare "(arbitrary, unknown rank — NOT rank-1)" parenthetical,
no binding/use rule, no migration note (the largest group; borderline — the
"NOT rank-1" is a general echo but it is one parenthetical clause, arguably part
of stating the op admits any rank):**
- `book/src/L2/`: axpy.md:43, axpby.md:45, axpbypcz.md:48, scal.md:43, dot.md:38,
  normalize.md:52, reciprocal.md:38,102, elementwise_product.md:41,97,
  inner_product.md:166, gram.md:56.
- `book/src/L3/`: dot.md:49, inner_product.md:114, normalize.md:23,42,
  reciprocal.md:21,40, elementwise_product.md:41.
- `book/src/L4/`: dot.md:56,85, inner_product.md:20,101, nrm2.md:78,
  sparameter_reduce.md:100.

**Recommendation for the user/meta-phase (NOT enacted here):** Tier A is the
user's explicit target and is relocated above. Tier B is *already* doing the
right thing (it links §1.2.1) — a light pass could drop the residual "NOT rank-1"
echo but it is low-value. **Tier C is a judgment call**: the bare "(arbitrary,
unknown rank — NOT rank-1)" parenthetical is short enough to read as part of each
op's own shape statement ("this op admits any rank, and specifically is not pinned
to rank-1"), NOT as the general teaching the user objected to. My read: Tier C is
**below the relocation bar** — it states a per-op shape fact concisely and does
not restate the binding/use rule, anti-pattern rationale, or migration note. If
the user wants strict uniformity (only §1.2.1 may even mention rank-1), a
cohort-wide Tier-C trim is a separate, mechanical, ~25-line sweep — best dispatched
as a single batched relocation pass, not folded into this scoped dispatch. I
recommend a meta-phase decision on whether Tier C clears the bar before sweeping.

## Open questions / caveats

- **Tier-C bar (above).** Does the bare "(arbitrary, unknown rank — NOT rank-1)"
  parenthetical count as "the general rule living in the entry" (relocate) or as
  "the op stating its own shape concisely" (keep)? My judgment: keep. Flagged for
  meta-phase to ratify the bar before any cohort-wide sweep, so the principle's
  reach is decided once rather than per-entry.
- **Tier-B residual echo.** Tier-B entries already LINK §1.2.1 inside the bullet
  (the relocation target shape) but still carry a "NOT rank-1" echo. Whether to
  drop that echo is the same Tier-C judgment; bundling Tier B + Tier C into one
  decision is cleanest.
- **Migration-note class.** The "earlier `Tensor[N]` rendering accidentally read
  as…" note (unique to `L4/linear_combination.md`) is a *past-edit* artifact, not
  a rule — it has no authoritative home and is simply deleted (not relocated). If
  other entries carry analogous "earlier rendering" notes from the c111 rollout
  they should likewise be deleted, not homed; the grep found none beyond the L4
  entry.
- **No `l4_calculus.md` edit needed.** §1.2.1/§1.2.2/§4.1 verified complete; the
  relocation is pure trimming. (If a future Tier-C/B sweep wants a single
  canonical sentence to point every entry at, §4.1 `:303` already is that
  sentence — no new prose required there either.)
