---
agent: lifter
invoked_at: 2026-06-03T041103Z
integrated_at: 2026-06-03T044543Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-074 D4. Applied clean — pure plain-text->live-link re-anchor of lifecycle.L4 (:37 prose + :59 dep-map cell + :64 §Status clause): the 3 plain-text forward-refs (eigenmode/driven/transient, now on disk after c073) -> live [name.L4](./name.L4.md) links; 'forthcoming/not yet authored' qualifiers dropped; the spine ROOT's 5-branch dispatch (problem_type) navigation now fully live-linked. No source-range change (main.cpp switch citations byte-identical). D5 boundary honored (mid-paragraph trailing-clause edit disjoint from D5's head-token edit). citecheck 3 ok/0 fail. retroactive 0. cargo make book exit 0, all 5 driver live-links resolve."
scope: feature-surface SPINE ROOT live-link re-anchor — lifecycle.L4 → driven/transient/eigenmode columns
status: pending
inputs:
  - book/src/feature/lifecycle.L4.md
  - book/src/feature/eigenmode.L4.md
  - book/src/feature/driven.L4.md
  - book/src/feature/transient.L4.md
---

# CYCLE: Re-anchor lifecycle.L4 forthcoming-refs to on-disk driver columns

## Summary
The lifecycle ROOT feature column (`book/src/feature/lifecycle.L4.md`) was authored c072 as the spine-ROOT meta-feature, when only `electrostatic` and `magnetostatic` driver columns existed. It forward-references the other three driver branches — eigenmode, driven, transient — as plain-text "forthcoming feature columns (not yet authored)". Those three columns landed c073: all of `book/src/feature/{driven,transient,eigenmode}.{L4,L1,L0}.md` are now on disk (verified, all 9 files present). This is a pure live-link re-anchor (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`): the three forthcoming plain-text refs become live links to the now-on-disk `.L4` columns and the "forthcoming / not yet authored / plain-text" qualifiers are dropped, at three loci (:37 prose, :59 dep-map row, :64 §Status clause). Structure and narrative are unchanged — only the vocabulary of the forward-references is firmed up. The §Status TOKEN (`seed (composition-root)`) at the head of :64 is explicitly LEFT for D5 (sequenced after this dispatch); only the "forthcoming, plain-text" CLAUSE inside that paragraph is edited.

## Proposed changes

```edit:book/src/feature/lifecycle.L4.md
[old]: 2. **Dispatch the per-driver specialization** — `dispatch (problem_type cfg)` selects ONE per-driver feature column by `ProblemType`. This is the **specialization seam**: the lifecycle root composes the *feature column*, and each column is itself a full composition root one level down. On disk this cycle: [`electrostatic.L4`](./electrostatic.L4.md) (the `ELECTROSTATIC` branch) and [`magnetostatic.L4`](./magnetostatic.L4.md) (the `MAGNETOSTATIC` branch). The other three branches — eigenmode, driven, transient — are forthcoming feature columns (not yet authored). L0: the `switch (iodata.problem.type)` (`palace/main.cpp:257-280`): `ELECTROSTATIC` `:267`, `MAGNETOSTATIC` `:270`, `EIGENMODE` `:264`, `DRIVEN` `:261`, `TRANSIENT` `:273`, `BOUNDARYMODE` `:276`.
[new]: 2. **Dispatch the per-driver specialization** — `dispatch (problem_type cfg)` selects ONE per-driver feature column by `ProblemType`. This is the **specialization seam**: the lifecycle root composes the *feature column*, and each column is itself a full composition root one level down. On disk this cycle: [`electrostatic.L4`](./electrostatic.L4.md) (the `ELECTROSTATIC` branch), [`magnetostatic.L4`](./magnetostatic.L4.md) (the `MAGNETOSTATIC` branch), [`eigenmode.L4`](./eigenmode.L4.md) (the `EIGENMODE` branch), [`driven.L4`](./driven.L4.md) (the `DRIVEN` branch), and [`transient.L4`](./transient.L4.md) (the `TRANSIENT` branch). L0: the `switch (iodata.problem.type)` (`palace/main.cpp:257-280`): `ELECTROSTATIC` `:267`, `MAGNETOSTATIC` `:270`, `EIGENMODE` `:264`, `DRIVEN` `:261`, `TRANSIENT` `:273`, `BOUNDARYMODE` `:276`.
```

```edit:book/src/feature/lifecycle.L4.md
[old]: | dispatch → eigenmode / driven / transient columns | eigenmode.L4 / driven.L4 / transient.L4 *(forthcoming — not yet authored)* | not yet authored | `palace/main.cpp:264, 261, 273` |
[new]: | dispatch → eigenmode / driven / transient columns | [eigenmode.L4](./eigenmode.L4.md) / [driven.L4](./driven.L4.md) / [transient.L4](./transient.L4.md) | on disk | `palace/main.cpp:264, 261, 273` |
```

```edit:book/src/feature/lifecycle.L4.md
[old]: stage (2) dispatches over the per-driver feature columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md) on disk; eigenmode/driven/transient forthcoming, plain-text).
[new]: stage (2) dispatches over the per-driver feature columns ([`electrostatic.L4`](./electrostatic.L4.md), [`magnetostatic.L4`](./magnetostatic.L4.md), [`eigenmode.L4`](./eigenmode.L4.md), [`driven.L4`](./driven.L4.md), [`transient.L4`](./transient.L4.md) — all five on disk, live-linked).
```

## Discipline notes
- **Pure re-anchor, structure preserved.** All three edits replace plain-text forward-references with live `[name.L4](./name.L4.md)` links and drop the "forthcoming / not yet authored / plain-text" qualifiers. No prose claim, no L0 citation, no decomposition was changed. The high→low direction is untouched (the chapter remains the L4 composition-root, narrating composition of the driver columns DOWN). Skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` is the governing procedure; all 9 target files (`{driven,transient,eigenmode}.{L4,L1,L0}.md`) verified present on disk before linking, with the three `.L4` files being the link targets.
- **D5 boundary respected.** Locus :64 begins with the §Status TOKEN `` `seed (composition-root)` ``, which is D5's deliverable. My edit at :64 targets ONLY the trailing parenthetical clause "(...; eigenmode/driven/transient forthcoming, plain-text)" deep inside the paragraph body; the `old_string` anchor does not include the token, and the token is unchanged.
- **Link-target form note.** The dep-map row (:59) previously carried a single combined cell "eigenmode.L4 / driven.L4 / transient.L4"; I rendered all three as separate live links within the cell and replaced the right-hand "not yet authored" column-cell with "on disk". The L0 citation cell (`palace/main.cpp:264, 261, 273`) is unchanged.

## Supporting evidence
- `book/src/feature/lifecycle.L4.md:37,59,64` — the three forthcoming-ref loci (read verbatim this dispatch).
- `book/src/feature/{eigenmode,driven,transient}.L4.md` — the three now-on-disk link targets (landed c073; `ls` confirmed present, sizes 12767/12443/10656 bytes respectively).
- `book/src/feature/{eigenmode,driven,transient}.{L1,L0}.md` — confirmed present (the full 3-level columns landed c073); only the `.L4` files are linked from lifecycle.L4 per the spine-reads-top-down convention.

## Open questions / caveats
- None. The targets are firm-on-disk full columns; the re-anchor is mechanical. No abstractor reread is warranted (no signature shift, no decomposition change).
- The boundarymode branch (`:276` in the `switch`) is still not a feature column on disk — it remains correctly un-linked in the prose (it is named only in the L0 `switch` enumeration, not claimed as an on-disk column). No change needed; flagging only so a future spine-coverage sweep notes wave-port/boundary-mode is the remaining un-authored driver-dispatch branch (consistent with the FEATURE-SURFACE SPINE scope list).
