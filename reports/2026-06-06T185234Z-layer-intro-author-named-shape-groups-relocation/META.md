---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T191500Z
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
overall_status: ready
---

# META: verification of named-shape-groups notation relocation (linear_combination → §1.2.1)

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation was checked on disk. The three `[old]` blocks (L4 `linear_combination.md:97-102`, L3 `:47`, L2 `:82-86`) match the current file content **verbatim** — confirmed by direct Read of each. The home citations resolve and carry what the report claims: §1.2.1 (`l4_calculus.md:62-74`) carries the binding-vs-use rule and `$` sigil (`:64,:66`), the partial-run form (`:69`), and the "Why this exists — `Tensor[N]`-as-same-shape anti-pattern" paragraph (`:74`, verbatim the directive the entries restate); §1.2.2 (`:76-84`) carries `LinOp[(R: ...), (D: ...)]` domain/range and the L1/L0 keep-rank-1 note; §4.1 (`:303`) carries the primitive-level "A named group is the rank-agnostic same-shape contract; a bare concrete axis (`Tensor[N]`) is not — it is a rank-1 commitment." The cohort grep claim (27 files) reproduces exactly. No drift, no out-of-range pinpoint.

**surface-or-evidence — pass.** This is a surface-modifying refinement (trims to three operator entries) backed by an explicit content-preservation argument. The directive obligation here is the inverse of the usual one: the report must show that the removed text is *not lost*. I verified each removed sentence has a home: "carries the same-shape contract" → §4.1 `:303`; "reuse of `S` … asserts congruence" → §1.2.1 `:64` + §4.1 `:303`; the `$`-sigil binding-vs-use rule → §1.2.1 `:66`; the `Tensor[N]`-rank-1 anti-pattern teaching → §1.2.1 `:74`. The migration note ("earlier `Tensor[N]` rendering accidentally read as…") is correctly classified as a past-edit artifact (documents an edit, not a rule) and deleted rather than relocated — there is no rule to preserve, so no home is required. No record is named in any signature without a home (the only named type is the structural list `[(Scalar, Tensor[(S: ...)])]`, not a record). No unique content is lost.

**rotation-quality — pass (not applicable).** This is a prose-relocation refinement, not a layer rotation; no algebraic/structural/reduction claim is asserted or altered. The signatures (`[(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`) are untouched.

**variant-axis-coverage — pass (not applicable).** No variant axes are in play; this is a documentation trim. The op's own shape contract (congruent over one group `S`, element-local, result shares `S`) is preserved in all three `[new]` blocks.

**cross-reference-integrity — pass.** The §1.2.1 link in each "Shape contract" preamble (L4 `:90`, L3 `:44`, L2 `:77`) is present and untouched by the edits — confirmed by Read; the edits modify only the per-term shape-precondition bullet beneath it. The L4 `[new]` block re-uses the identical existing relative path `../design/l4_calculus.md`, so no new link target is introduced. As the report notes, the entries cite "§1.2.1" in prose and link the bare file (no fragment anchor), so there is no anchor fragment to break. `l4_calculus.md` §1.2.1 exists at `:62`. No `linkcheck2` exposure.

**edge-label-fidelity — pass.** Prose-only edits; no `edges:` frontmatter is touched. I confirmed each of the three files carries an `edges: depends-on:` block in frontmatter and that all three edit blocks operate strictly on body shape-contract bullets, well below the frontmatter. No edge label is asserted or altered.

**plan-kind-consistency — pass.** Declared as a scoped relocation refinement satisfying a direct user directive; content shape matches (three surgical edit blocks + a verification section + a cohort finding). No mis-classification.

**skill-uptake-survey — pass.** No skill is squarely implied by a prose-relocation-with-preservation-check; the report's own §Verification section performs the equivalent content-preservation audit by hand. Telemetry only; non-blocking.

### Issues found

No blocking issues. The directive is genuinely satisfied: after the trim, the general rule/syntax/anti-pattern teaching no longer lives in the `linear_combination` entries, the complete rule remains in §1.2.1/§1.2.2/§4.1, each entry retains its own shape contract (signature, congruence over `S`, element-locality, result shape) and its §1.2.1 link, and the L2 entry legitimately keeps its aligned-fusion-kernels precondition (the producer's `[new]` rephrases it to "This congruence is also the aligned-fusion-kernels precondition," which reads cleanly and remains the op's own consequence).

Two non-blocking observations (no severity; not repair candidates):

1. **Tier-C scoping is reasonable, not under-scoping.** The user named only `linear_combination`; scoping the dispatch to those three entries plus a cohort finding is defensible and matches the dispatch instruction. I spot-checked Tier C (`L2/axpy.md:43`, `L2/dot.md:38`) and Tier B (`L2/nrm2.md:77`) on disk: Tier C carries only a bare "(NOT rank-1)" parenthetical with no binding/use rule and no migration note, and Tier B already links §1.2.1 — both match the report's characterization. The producer's "Tier C is below the relocation bar pending meta-phase ratification" call is sound, and correctly routed to the meta-phase rather than silently swept or silently left. The 27-file extent reproduces exactly.

2. **Forward note for the integrator (not a defect):** the migration-note deletion is unique to the L4 entry; the report states the grep found no analogous "earlier rendering" notes elsewhere, which I did not exhaustively re-verify but is consistent with the marker grep. If a future Tier-B/C sweep is dispatched, §4.1 `:303` is already the single canonical pointer sentence, so no addition to `l4_calculus.md` is needed — the report's claim of "pure trim, nothing added to the home" holds.
