---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T203057Z
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

# META: verification of cycle-106 D5 unresolved-`depends-on`-target reclassification

## Critique

### Checks run

**citation-validity — pass.** The report's load-bearing citations are (i) linter line-refs into `tools/graded-stack-lint/graded_stack_lint.py` and (ii) on-disk book-slug existence. I verified every cited linter line directly on disk: `:211` = the `bm` block-mapping regex `^(\S[^:]*):\s*(.+)$` (the misparse trigger); `:208-218` = the surrounding block-mapping-item branch; `:431` = `derive_rank` reading `firmness:`; `:317-324` = `normalize_target`'s paren-strip + `:lo-hi`→None exclusion; `:519-543` = the legacy-key→`depends-on` migration (`depends_on`/`lowers_to`/`lifts_from`/`lifts_to`/`consumes`); `:614-615` = `rank: None`→warn-not-fail. All exact. `citecheck --scan` emits 3 `[MISS]` on `graded_stack_lint.py:{211,431,519-543}`, but those are `tools/` paths, which citecheck does not search (its roots are `reference/*` + `book/src`) — they are NOT Palace-source claims and I confirmed them by direct Read against the tool. No `±1` drift was asserted by the report, and none is asserted here. No `verified_against:` YAML block is present. No genuine citation failure.

**surface-or-evidence — pass.** This is a frontmatter edge-migration report (legacy `depends_on:`/`lowers_to:`/… → typed `edges:`), not a refinement that mutates operator/theme algebraic surface — `firmness:` is preserved verbatim on all 18 hosts, no rank claim changes, no algebraic-law text is touched (the `## Lowers to` / `## Downward to` body prose is explicitly left untouched). The record-definition sub-check does not trigger: no proposed chapter introduces a signature naming a new record. Evidence shape is appropriate (mechanical-cause diagnosis + per-target existence sweep).

**rotation-quality — pass (not applicable to this report-kind).** No algebraic/structural/reduction rotation is asserted; the work is edge-frontmatter re-encoding. No-op.

**variant-axis-coverage — pass.** No variant axes are introduced or altered; `variant_axes:` blocks are preserved on every host (each `[new]` block ends with the host's existing `variant_axes:` key intact). No hidden branches.

**cross-reference-integrity — pass (load-bearing here, verified exhaustively).** I ran an on-disk existence sweep of all 36 distinct re-encoded edge targets — every one resolves (`book/src/<slug>.md` present). The two missing-`L_n/`-prefix fixes are correct on-disk slugs and correctly disambiguated: `apply_linop`/`axpy` exist at `L1/`, `L2/`, `L3/`, and `concepts/`; the report fixes the `L1/eliminate_rhs` deps to `L1/apply_linop` / `L1/axpy`, the same-layer L1 homes — the right choice for an L1 operator depending on L1 vocabulary. Bare-string edge targets (`L3/dot`, `L4/eigsolve`, etc.) normalize cleanly via `normalize_target`. The two prose-as-slug strikes are genuinely prose with no recoverable head slug (case 12 `lowers_to:` = "the per-mode scalar maps …"; case 18 = "the per-port port-mode linear functional sᵢ·E …") and are correctly STRUCK rather than invented as stubs; case 12's mid-prose named L1 homes are routed to `reference` (not fabricated as lowering endpoints).

**edge-label-fidelity — pass (spot-checked across several files).** The `depends-on` vs `reference` reclassifications are faithful. (6) `L3/divfree-projector`: the lowering endpoint `L2/divfree-projector` is `depends-on`; the kept firm theme `L2-L1/divfree-projector-leaf-identity` is routed `reference` — correct, it sits one edge further down (it is the L2 floor's lowering, a downstream see-also, not a blocking constituent of the L3 entry's own composition). (13) `L4/fe_assemble` / (10),(11),(14)–(17): concept disposition/framing pages (`black-box-vs-accelerated-kernels`, `dot`, `nrm2`, `scalar-promotion`, `state-stratification`) and the `L4/index` container → `reference`; I confirmed `L4/index` carries `kind: navigational-container` + an explicit "not a DAG node: no rank" banner, so a blocking `depends-on` on it would never be legitimate — `reference` is exactly right. The lowering-endpoint keys (`lowers_to`/`lifts_from`/`lifts_to`/`lowers_from`) → `depends-on` matches the linter's own §migration semantics (a lowering edge is blocking on both endpoints, `:526-535`). No mislabeled edge.

**plan-kind-consistency — pass (WAVE-3 exclusion honored).** The 18 edited files are enumerated from the `edit:` blocks; NONE is among the 5 WAVE-3 chapters (`L4/ksp_solve`, `L4/krylov-step`, `L4/solve_family`, `L4/fold_solve`, `L4/eliminate_bc`). Note the report edits `L2/ksp_solve` (case 3) and `L4/dot`/`L4/inner_product`/etc. — all distinct from the WAVE-3 set; `L4/solve_family` is explicitly left untouched and its residual unresolved target is handed to D3 with a concrete suggested `edges:` block. The report's declared kind (mechanical lazy-tail edge-migration) matches content shape: no rough-in placeholders, no algebraic authoring. The linter-reader-bug (`graded-stack-lint-block-mapping-misparse-on-legacy-edge-prose-colon`) is correctly routed as an Open-questions finding rather than a tool-code edit — the boundary is right (layer-intro-author authors frontmatter, not `tools/` code), and the migration legitimately eliminates the trigger for these 18 files while flagging that un-migrated `:`-bearing legacy items elsewhere will reproduce it.

**skill-uptake-survey — pass.** No directly-matching skill for typed-edge migration; the report references the scheme (§2/§4/§5/§(e)) and the linter mechanics in lieu of a procedure. Telemetry-only; non-blocking.

### Issues found

No blocking or warning issues. The report is mechanically faithful: all 36 re-encoded targets resolve on disk, the two missing-prefix fixes are correct same-layer slugs, the prose-as-slug strikes are genuine prose (correctly struck, not stubbed), the `depends-on`/`reference` split is defensible per the scheme (lowering endpoints + folded vocabulary blocking; concept-framing pages + the navigational container + the one-edge-further kept theme as `reference`), the WAVE-3 exclusion is honored with `L4/solve_family` deferred to D3, and the linter-reader-bug is routed as a finding at the correct author-vs-tool-code boundary. All cited linter line-refs verified exact.

(Non-blocking telemetry, not a defect: case (12) routes the two firm L1 scalar-map homes `L1/eigenvalue-untransform` / `L1/participation_ratio` to `reference` rather than `depends-on`. The report's rationale — the struck `lowers_to:` was prose with no clean lowering endpoint, and these are named body-references — is reasonable, and `reference` is the conservative choice (it cannot induce a false rank violation). The constituent-edge rank-constraint is thereby not asserted for these two, which is consistent with the report's own narrative-reference framing. No action required.)
