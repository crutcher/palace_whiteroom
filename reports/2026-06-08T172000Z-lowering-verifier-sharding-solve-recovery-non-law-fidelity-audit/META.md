---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T184500Z
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

# META: verification of "Audit sharding-solve-recovery-non-law-fidelity"

## Critique

### Checks run

**citation-validity — pass.** This is an audit-class report; the load-bearing pinpoints are the firm reduce-case law anchors the SOLVE NON-LAW framing leans on, plus the DIRECTIVE-1 mechanism cites and the no-native-DD confirmation. I re-derived all on disk: `inner_product.md:154-157` (Split-additivity / shape-concatenation-homomorphism), `linear_combination.md:146-151` (Concatenation-homomorphism), `domain_energy_reduce.md:147-152` (map-independence fold law), and `domain_energy_reduce.md:172-178` (`Σ pᵢ = 1` config-conditional NON-law) all resolve EXACTLY to the cited content, confirmed both by `sed` extraction and by `citecheck.py --anchor` (all `[ok]`, anchors in-range). The chapter ranges the audit cites — `sharding-decompose-reduce.md:103-113` (the "crucial asymmetry" callout), `:184-221` (the speculative-laws section with law 1 reduce-recovery vs law 5 CONFIG-CONDITIONAL solve-recovery), `:244-267` (the NON-law block), `:6-14` (the frontmatter `edges:`) — all resolve and say what the audit says they say. The Palace anchors `geodata.cpp:262,3239,3242`, `rap.hpp:24` / `rap.cpp:116-126`, and `romoperator.cpp:586` ("ports don't have any overlap") all verify on-disk; `grep -ril schwarz reference/palace/palace/` returns zero (exit 1, no matches), confirming the no-native-DD claim. The proposed `verified_against:` 9-entry block round-trips clean under `yaml.safe_load` (no leading-`'`/`"`-scalar defect; the `reference: ONLY` colon-space hazard was pre-rephrased to `the reference edge-class ONLY`, confirmed in the shipped block). The one recorded path nuance — bare `romoperator.cpp:586` omitting the `models/` prefix at chapter L326/L395 — is real but assessed below-bar (see Issues).

**surface-or-evidence — pass.** Audit-class (lowering-verifier fidelity check), not a refinement-shaped proposal: it modifies no operator/theme surface text. Its single book mutation is a `verified_against:` correspondence-block append (pure retroactive evidence backfill), which is the allowed shape. No record/struct is newly named in a signature here (the chapter under audit is the surface; the audit only attests to it), so the record-definition sub-check no-ops. Pass.

**rotation-quality — pass (not applicable to audit-class).** No algebraic/structural/reduction rotation is asserted by the audit itself; it attests to the fidelity of an existing roadmap_goal chapter's speculative framing. No-op.

**variant-axis-coverage — pass (not applicable to audit-class).** The audit asserts no operator with orthogonal variant axes. Note in passing: the chapter's own block-diagonal / coupled / overlapping cases ARE the solve-recovery variant axis, and the audit correctly verified each is explicitly scoped (block-diagonal exact, coupled approximate-Schwarz, overlapping p.o.u.-weighted) with no hidden branch — but that is the audited content's axis coverage, not the report's, and the audit found it clean.

**cross-reference-integrity — pass.** The block-append target `book/src/L4/sharding-decompose-reduce.md` exists; the existing c139 `verified_against:` block is at L416, so the new block appends after it (the audit correctly states the two blocks coexist). All cross-referenced chapters exist on disk (`inner_product`, `linear_combination`, `domain_energy_reduce`, `ksp_solve`, `fold_solve`, `krylov-step`). The OQ discharge `sharding-decompose-reduce-solve-case-recovery-strictly-weaker-than-reduce-case` is well-formed and routed to planner/meta-phase for closure. The rank-invariant sub-claim checks out: frontmatter `edges:` carries a single `reference:` key listing the 3 solve roots and NO `depends-on:` key, and all 3 roots are `rank: firm` on-disk — so no `rank(firm)=3 > rank(roadmap_goal)=0` violation is manufactured (a `reference`-class edge constrains nothing). Reachability is intact (the node is a roadmap_goal, rank 0, pulled-by its sharding-math intent; reference edges to firm roots).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this audit; the `reference`-class root edges are navigational and the audit discusses them correctly as non-blocking. No-op / pass.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit (verdict FULLY-SUPPORTED) and the content shape matches: per-citation audit table, applicability conditions, algebraic-laws review, a `verified_against:` correspondence block, and an explicit no-promotion / stays-rank-0 disposition. No firm-claim or rough-in placeholder mismatch. The per-citation `romoperator.cpp:586` row is honestly graded `partially-supports` (content confirmed, path under-qualified) rather than over-claimed `supports`, which is consistent and correct.

**skill-uptake-survey — pass.** The report's shape implies the citation-verification skills, and it references them by name and invocation: `citecheck.py --anchor` is cited as run on the Palace anchors (all `[ok]`), and the `yaml.safe_load` round-trip is cited as run on the `verified_against:` block with the colon-space defect rephrased pre-ship. Telemetry present.

### Issues found

- **Minor (below-bar, correctly self-recorded): bare `romoperator.cpp:586` path under-qualification.** At chapter `sharding-decompose-reduce.md:326` and `:395`, the no-native-DD evidence cites the bare filename `romoperator.cpp:586`, omitting the `models/` directory prefix (the file is at `reference/palace/palace/models/romoperator.cpp`). The `verified_against:` block entry for this citation USES the fully-qualified path, so the block-append itself carries no defect — the under-qualification is purely in the pre-existing in-prose Evidence text of the chapter under audit, which this audit does not edit. Assessed genuinely below the forced-fix bar: (a) the path is unambiguous — a single `romoperator.cpp` exists in the tree (confirmed; no sibling); (b) the content resolves (`:586` = "ports don't have any overlap", confirmed) and the load-bearing claim (no native Schwarz/DD preconditioner) is fully verified via the zero-result `grep -ril schwarz`; (c) it is in-prose Evidence text, not a load-bearing `verified_against:` anchor; (d) audit-class forced-fix scope is at-most-one-line stale-token, and this is under-qualified, not stale. The report correctly grades the citation `partially-supports`, records the caveat in §Open questions, and leaves the optional one-line qualification to a land-clean lifter's discretion rather than forcing it. No repair warranted; this does not gate citation-validity (resolution and claim-support both hold).

  (One trivial transcription nuance, non-blocking: the report twice writes the in-prose sites as "L394-395"; the second bare citation is on L395 only. The line is within the cited span and the finding is unaffected.)

All 8 checks pass. The `verified_against:` block round-trips clean, every load-bearing anchor resolves exactly (citecheck `--anchor` `[ok]`), the rank-invariant / reference-class disposition is correct, the OQ discharge is well-formed, and the single recorded caveat is genuinely below-bar and honestly graded. No warning or fail finding; `overall_status: ready` set on the all-pass path.
