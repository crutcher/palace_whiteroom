---
agent: combinator-miner
invoked_at: 2026-06-03T165837Z
scope: Distinct-verb-vs-inline confirm probe for domain_energy_reduce (D4; observation-only)
status: integrated
integrated_at: 2026-06-03T210000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-079 (batch-25 position 1). Observation-only confirm-probe; verdict DISTINCT-VERB-WARRANTED (the per-domain numerator is itself a domain-restricted SPD energy reduction, so domain_energy_reduce does NOT collapse into a participation_ratio fold-inline / gram_reduce). NO book/ mutation. Verdict already consumed by D3 (which authored the verb file). Closes OQ domain_energy_reduce-distinct-verb-vs-inline-confirm-probe (verdict-provenance marker only)."
---

# CYCLE: Combinator candidate — domain_energy_reduce (distinct-verb confirm probe)

## Summary

This is the D4 observation-only probe answering: does the per-domain field-energy table
reduction (`MeasureDomainFieldEnergy`) warrant a DISTINCT L4 verb `domain_energy_reduce`, or
does it COLLAPSE into a bare `participation_ratio` fold inlinable directly into the
`energy-fields` feature column? **Verdict: DISTINCT-VERB-WARRANTED.** The per-domain reduction
is a genuine 4th reduce-shape in the L4 algebra-of-folds family — a **rank-1 per-domain scalar
TABLE** reduction that folds TWO L1 primitives per domain (the domain-RESTRICTED energy form
`½⟨field, M_i field⟩` AND the participation ratio `energy_i / e_total`) over a config-driven
domain-attribute index set, producing `[DomainData]` rows. It does NOT collapse to a bare
`participation_ratio` fold because the per-domain numerator energy `energy_i` is itself a
non-trivial domain-restricted SPD energy reduction (the load-bearing content), not a
pre-computed scalar handed to the ratio. It does NOT collapse into `gram_reduce` (no family-PAIR
grid / `symmetric_from_upper`; the c074 D6 do-NOT-over-unify guard, already honored in the
column). It is the per-domain-table sibling of the per-mode-table `eigenfreq_qfactor_reduce`,
which itself was minted as a distinct verb on the same rank-1-table-vs-rank-2-Gram reasoning.
The redirect's abstraction-value test is MET: minting the verb gives the energy-fields column a
navigable L4 home for its reduction shape and matches the established naming pattern (one
reduce-verb per output-product column), rather than stranding the reduction as inline column
prose. → **D3 (Wave 2 / harvester) mints `book/src/L4/domain_energy_reduce.md`.**

## Pattern instances

The per-domain energy-table reduction recurs as TWO structurally-identical instances within one
method (the electric and magnetic field passes), each a distinct per-domain fold:

- **Instance 1 — per-domain ELECTRIC field-energy table.**
  `palace/models/postoperator.cpp:1036-1042` (`MeasureDomainFieldEnergy`, the
  `for (const auto &[idx, data] : dom_post_op.M_i)` electric loop): each domain `idx` →
  `energy_i = GetDomainElectricFieldEnergy(idx, field)`, `participation_ratio = |energy_i| > 0 ?
  energy_i / energy : 0.0`, emit `DomainData{idx, energy_i, participation_ratio}`. Numerator
  energy form: `domainpostoperator.cpp:255-275` (`GetDomainElectricFieldEnergy` — `½⟨E, M_i E⟩`
  via `M_i->Mult(E.Real(), D)` + `LocalDot`, plus the imag-part accumulation).

- **Instance 2 — per-domain MAGNETIC field-energy table.**
  `palace/models/postoperator.cpp:1061-1066` (the magnetic loop, same shape with `B`/`A`
  for `E`/`V`): each domain `idx` → `energy_i = GetDomainMagneticFieldEnergy(idx, field)`,
  `participation_ratio = |energy| > 0 ? energy_i / energy : 0.0`, emit `DomainData{idx, energy_i,
  participation_ratio}`. Numerator energy form: `domainpostoperator.cpp:277-298`
  (`GetDomainMagneticFieldEnergy` — `½⟨B, M_i B⟩`, identical shape to the electric form with the
  magnetic mass operator).

- **Instance 3 (the per-domain energy form itself, folded TWICE — the load-bearing inner fold).**
  `palace/models/domainpostoperator.cpp:255-275` and `:277-298` — `GetDomain{Electric,
  Magnetic}FieldEnergy(idx, ...)` are each a domain-RESTRICTED `½⟨field, M_i field⟩` SPD energy
  (the `matrix-weighted-norm` squared radicand with `B = M_i`, the operator restricted to ONE
  domain attribute). This restricted-energy reduction is what makes `domain_energy_reduce` more
  than a bare `participation_ratio` fold: the numerator is a per-domain TENSOR reduction, not a
  pre-reduced scalar.

(3 structural instances: 2 table passes + the doubly-folded restricted-energy inner reduction.
The 2 table passes alone clear the parametric-family ≥2-siblings-with-a-stateable-law bar, with
the field-kind {electric, magnetic} as the variant axis. Same-shape mode also fires: the two
passes are the same reduction shape modulo the field-kind operator.)

## Proposed combinator (CONFIRM of the already-forward-referenced slug)

This probe does NOT propose a new slug — it CONFIRMS the slug `domain_energy_reduce` already
forward-referenced by the energy-fields column should be minted as a real verb file (vs. inlined).

- **Slug**: `domain_energy_reduce` (already the canonical forward-ref in
  `book/src/feature/energy-fields.L4.md:8,48,62,134,156`)
- **Layer**: **L4** (with rationale below — NOT inline-in-column, NOT L1/L2).
- **Reduce-shape class**: the **reduce-to-scalar-TABLE** member of the L4 algebra-of-folds family
  (`inner_product` reduce-to-scalar · `linear_combination` reduce-to-tensor · `gram_reduce`
  reduce-to-matrix · `eigenfreq_qfactor_reduce` reduce-to-per-mode-table). `domain_energy_reduce`
  is the **reduce-to-per-DOMAIN-table** sibling — same rank-1-table shape as
  `eigenfreq_qfactor_reduce`, indexed by configured domain attribute instead of mode.

- **Signature sketch** (harvester firms up; matches the column's stage-2 prose at
  `energy-fields.L4.md:62-76`):

      -- per-domain field-energy table reduction over a config-driven domain-attribute set
      domain_energy_reduce :: DomainOpMap          -- the {idx -> M_idx} domain-restricted energy operators
                           -> Field                -- the solution field (V/E electric, A/B magnetic)
                           -> Scalar               -- e_total: the whole-domain energy (the shared denominator)
                           -> [DomainData]         -- per domain: { idx, energy_i, p_i }
      domain_energy_reduce doms field e_total =
        [ let energy_i = domain_energy M_idx field            -- ½⟨field, M_idx field⟩  (matrix-weighted-norm radicand, domain-restricted)
              p_i      = if abs energy_i > 0 then participation_ratio energy_i e_total else 0
          in  DomainData { idx, energy_i, p_i }
        | (idx, M_idx) <- doms ]                              -- map over configured domains (no inter-domain state)

- **Algebraic intuition**:
  - **Per-domain map independence** (list homomorphism over the domain set): each row depends only
    on `(idx, M_idx, field, e_total)`; no inter-domain accumulator threads — embarrassingly
    parallel over domains. The C++ loop carries no cross-domain state (`postoperator.cpp:1036`,
    `:1061`).
  - **Shared-denominator invariance**: every row divides the SAME whole-domain `e_total`
    (`energy` set once at `:1034` / `:1059`) — the `participation_ratio` denominator-shared law
    (`participation_ratio.md` law 3) lifted to the table level.
  - **Identity element / empty fold**: empty domain set → empty table (`[]`).
  - **Restricted-energy additivity (partial)**: when the configured domains partition the full
    domain and `M = Σ M_idx`, `Σ energy_i = e_total` and `Σ p_i = 1` (the participations sum to
    unity). NON-partition configs (overlapping or sub-covering domain attributes) do NOT sum to 1
    — this is a property of the CONFIG, not the reduction, and is the per-domain-table analog of
    the `gram_reduce` weight axis (harvester to state as a conditional law).

- **Variant axes**:
  - **field-kind** {electric `½⟨E, M_i E⟩` | magnetic `½⟨B, M_i B⟩`} — THE load-bearing axis; the
    reduction runs twice, once per field, producing `domain_E_field_energy_i` /
    `domain_H_field_energy_i`. Absorbed into the `DomainOpMap` + `Field` arguments (the operator
    and the field differ; the fold is uniform).
  - **element-type** (complex field, real energy — the `E.HasImag()` imag-part accumulation at
    `domainpostoperator.cpp:267-271`; the energy reduction is real-valued).
  - **field-absent degenerate pass** — when a solver has no E (or no B) grid function, the loop
    emits all-zero `DomainData{idx, 0, 0}` rows (`postoperator.cpp:1048-1052` / `:1073-1077`).
    A degenerate variant, not a separate fold.

### Why DISTINCT-VERB and not COLLAPSE (the abstraction-value reasoning — the redirect's test)

The redirect's bar is judgment about abstraction value, NOT "does it decompose." Three collapse
candidates were tested; all REFUSED:

1. **Collapse to a bare `participation_ratio` fold (the inline candidate) — REFUSED.** A bare
   participation fold would be `map (\e -> participation_ratio e e_total) energies` over a
   PRE-COMPUTED `energies` list. But the per-domain numerator `energy_i` is NOT pre-computed —
   it is a domain-RESTRICTED SPD energy reduction `½⟨field, M_i field⟩` (`GetDomain*FieldEnergy`,
   `domainpostoperator.cpp:255-298`), a non-trivial tensor reduction over a per-domain operator
   `M_i`. `domain_energy_reduce` folds TWO L1 primitives per row (the `matrix-weighted-norm`-
   squared domain-restricted energy AND the `participation_ratio` quotient); `participation_ratio`
   is only the second, post-energy step. Inlining would strand the load-bearing restricted-energy
   reduction as anonymous column prose with no navigable L4 home. The `participation_ratio.md`
   entry ITSELF explicitly disclaims the energy reduction as out-of-scope ("the numerator-energy
   ... computations BELOW the quotient are deliberately out of this primitive's scope ... separate
   energy-reduction vocabulary, named not authored", `participation_ratio.md:188-191`) — that
   named-not-authored energy-reduction vocabulary IS `domain_energy_reduce`. The bare-fold collapse
   would re-violate exactly the scope boundary `participation_ratio` was firmed to respect.

2. **Collapse into `gram_reduce` — REFUSED (already settled, c074 D6).** No family-PAIR
   `xⱼᵀ K xᵢ` bilinear grid, no `symmetric_from_upper`. The upstream is a SINGLE solution field,
   not a solution family; the index domain is the config domain-attribute set, not a family-pair
   product. This is the rank-1-table-vs-rank-2-Gram distinction the `gram_reduce` §Specialization
   already records as CLOSED-NEGATIVE (`gram_reduce.md:178-189`) and the energy-fields column
   already honors (`energy-fields.L4.md:123-141`).

3. **Collapse into `eigenfreq_qfactor_reduce` — REFUSED (sibling, not subsume).** Both are rank-1
   scalar-table reductions, BUT the index domain differs (per-MODE vs per-DOMAIN), the upstream
   differs (eigenpair family vs single field + domain-op map), and the folded primitives differ
   (eigenvalue-untransform + κ-ratio vs domain-restricted-energy + participation-ratio).
   `eigenfreq_qfactor_reduce` was ITSELF minted as a distinct verb (c074) on precisely this
   "same rank-1-table shape, different upstream/index/folded-primitives ⇒ own verb per
   output-product column" reasoning. Minting `domain_energy_reduce` is the CONSISTENT application
   of the established naming pattern (one reduce-verb per output-product column), not a new
   precedent. The two are siblings in the algebra-of-folds family, each its own verb.

**Net abstraction value (the mint clears the redirect bar):** the verb (a) gives the energy-fields
output-product column a navigable L4 reduction home (matching the 1-reduce-verb-per-column pattern
already set by `gram_reduce` for capacitance/inductance, `eigenfreq_qfactor_reduce` for
eigenfrequency-Q, `sparameter_reduce` for S-params); (b) names the doubly-folded
restricted-energy + participation structure as ONE reduction shape (the field-kind variant axis
unifies the electric and magnetic passes — without the verb they are two inline loops); (c)
completes the L4 algebra-of-folds family with its 5th member (reduce-to-per-domain-table). It is
NOT degenerate-identity-in-named-terms (it folds two distinct primitives over a config-driven
index), so it is not the redirect's smell-to-inline case.

## Layer placement rationale (why L4, not inline / L1 / L2)

- **Not inline-in-column.** The column (`energy-fields.L4.md`) is a composition-ROOT: it COMPOSES
  vocabulary and links DOWN, it does not DEFINE per-op algebra (CLAUDE.md §Feature-surface spine:
  "It does not introduce new per-op algebra"). The reduction's fold structure + laws are per-op
  algebra and belong in a verb file the column down-links to — exactly as the column ALREADY
  treats it (`energy-fields.L4.md:156` lists `domain_energy_reduce *(rough-in; no anchor yet)*`
  as a constituent down-link). Inlining would make the column define algebra, the anti-pattern.
- **Not L1.** It is a reduction-COMBINATOR (a fold over a config-driven set, parameterized by the
  domain-op map and folding two L1 primitives) — the same layer-placement reasoning as its four
  algebra-of-folds siblings, all at L4 (one layer above the L1 primitives they fold). The L1
  primitives it folds (`matrix-weighted-norm`, `participation_ratio`) already exist; the fold OVER
  them is L4.
- **Not L2/L3.** No iteration-rotation or fusion-rotation content — it is a pure value-producing
  reduction with no `Solve` monad, no carry, no loop recurrence (a post-processing readout, like
  the eigenmode `(f,Q)` readout). It lowers identity-in-form on the body to the L1 fold (the
  in-line-marker route, no dedicated L4>L3 theme — matching `gram_reduce.md:213-223` and
  `eigenfreq_qfactor_reduce.md` lowering disposition).

## Proposed changes

**NONE to `book/` from this dispatch.** This is an observation-only confirm probe. The slug
`domain_energy_reduce` is ALREADY forward-referenced in `book/src/feature/energy-fields.L4.md`
(at `:8,48,62,134,156`, the canonical down-link `domain_energy_reduce *(rough-in; no anchor
yet)*`) — the dep-map rough-in row already stands for it. No new rough-in row is needed; the
verb file authoring is D3/harvester's Wave-2 job, conditioned on this DISTINCT-VERB-WARRANTED
verdict.

(Per role-spec: combinator-miner emits a dep-map rough-in row only when the slug is NOT yet
referenced. Here the column already carries the rough-in down-link, so the only output is this
verdict + the harvester-firming notes above.)

## Supporting evidence

All L0 citations self-verified on-disk this dispatch via palace-codemap `read_range` /
`get_symbol_def` against `reference/palace/`.

- **`MeasureDomainFieldEnergy`** — `palace/models/postoperator.cpp:1021-1099` (the method;
  electric per-domain loop `:1036-1042`, magnetic `:1061-1066`, totals `:1034/:1059`,
  field-absent degenerate passes `:1048-1052/:1073-1077`). The participation guard asymmetry
  noted: electric uses `std::abs(energy_i) > 0.0` (`:1039`), magnetic uses `std::abs(energy) >
  0.0` (`:1064`) — see Open questions.
- **Per-domain energy form** — `palace/models/domainpostoperator.cpp:255-275`
  (`GetDomainElectricFieldEnergy` — `½⟨E, M_i E⟩`, `M_i->Mult` + `LocalDot` + imag-part accum +
  `0.5 * dot`), `:277-298` (`GetDomainMagneticFieldEnergy` — same shape, magnetic operator).
- **L4 reduce-shape siblings tested for collapse** —
  `book/src/L4/gram_reduce.md` (reduce-to-matrix; §Specialization `:178-189` records the
  eigenmode/driven 3rd-witness probe CLOSED-NEGATIVE — the rank-1-vs-rank-2 precedent),
  `book/src/L4/eigenfreq_qfactor_reduce.md` (reduce-to-per-mode-table; `:36-41` records its OWN
  mint on the rank-1-table-not-Gram reasoning — the consistent-precedent for this verdict),
  `book/src/L4/sparameter_reduce.md` (the per-output-product reduce-verb naming pattern).
- **Firm `participation_ratio` L1 primitive** — `book/src/L1/participation_ratio.md` (firm c077);
  `:188-191` explicitly names the numerator-energy reduction as out-of-scope "separate
  energy-reduction vocabulary, named not authored" — the named-not-authored vocabulary that
  `domain_energy_reduce` IS (the collapse-1 refutation).
- **The energy-fields column carrying the forward-ref** —
  `book/src/feature/energy-fields.L4.md:8,48,62-76,134,156` (the canonical
  `domain_energy_reduce` down-link, the column's stage-2 reduction prose, the
  rank-1-not-Gram §"Why distinct" section the column already states).
- **No dedicated unit test** exercises `MeasureDomainFieldEnergy` (the body is integration-level
  under the full `Solve(mesh)` driver; no `reference/palace/test/unit/` coverage) — consistent
  with the column's `seed` status and `participation_ratio`'s firm-on-positive-structure
  no-test-gate precedent. The verb will land `rough-in` (its folded `matrix-weighted-norm`
  energy form is itself `rough-in (test-coverage-bounded)`).

## Open questions / caveats

- **`domain_energy_reduce` should land `rough-in`, NOT `firm`** when D3 authors it: its folded
  domain-restricted energy form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)`
  primitive (per `energy-fields.L4.md:157`), so the reduction inherits reduced maturity — the
  same gating `gram_reduce` carries (`gram_reduce.md:227-248`). The energy-fields column stays
  `seed` until the verb AND its energy form firm. Flagging so D3 does not over-promote.
- **Participation-guard asymmetry (drive-by, source-level).** The electric pass guards on
  `std::abs(energy_i) > 0.0` (the NUMERATOR, `postoperator.cpp:1039`) while the magnetic pass
  guards on `std::abs(energy) > 0.0` (the DENOMINATOR/total, `:1064`). Both avoid the same `0/0`,
  but the predicates differ: electric zeroes `p_i` when the per-domain energy is zero; magnetic
  zeroes `p_i` when the TOTAL is zero. For the L4 verb the harvester should pick ONE total-guard
  (`if e_total > 0` is the cleaner uniform form, matching `participation_ratio`'s consumer-side
  totality handling) and note the two C++ sites' guard divergence as a transparent
  realization detail, NOT bake the asymmetry into the verb. (Likely a Palace inconsistency, not
  load-bearing — both produce `p_i = 0` in the degenerate case — but the harvester should make
  the call explicitly.) Not filed to `problems/` (below the ~1/15 bar; it is a benign
  zeroing-predicate divergence, not a semantic bug).
- **`DomainOpMap` record / `dom_post_op.M_i` definition home.** The verb's first argument is the
  `{idx -> M_idx}` domain-restricted-operator map (`dom_post_op.M_i`,
  `postoperator.cpp:1028-1029`). Per the record-definition obligation, the harvester should either
  define it in-chapter (single-consumer) or note `record-DomainOpMap-needs-definition-home` if a
  2nd consumer surfaces. (The `DomainData` RESULT record already has a definition home in the
  column at `energy-fields.L4.md:83-106` with the cross-cutter re-check OQ
  `record-DomainData-needs-definition-home` already open.)
- **Restricted-energy additivity law is config-conditional.** `Σ p_i = 1` holds ONLY when the
  configured domains partition the full domain (`Σ M_idx = M`). The harvester should state this
  as a CONDITIONAL law (partition precondition), not an unconditional one — overlapping/
  sub-covering domain configs are valid and do NOT sum to unity. This is the per-domain analog of
  the `gram_reduce` weight-symmetry precondition.
