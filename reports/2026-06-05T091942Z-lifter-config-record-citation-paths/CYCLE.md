---
agent: lifter
invoked_at: 2026-06-05T09:19:42Z
scope: concepts/config-record citation-path basename hygiene — disambiguate bare `main.cpp` citations
status: integrated
integrated_at: 2026-06-05T100000Z
integration_commit: 7417836
integration_notes: |
  Applied clean (cycle-105 D3, batch-33 position 3/3, BATCH-CLOSING). Disambiguated 4 bare `main.cpp:NNN` citations to `palace/main.cpp:NNN` across 3 edit blocks in concepts/config-record.md (§driver-selector :257-281, §Signatures :231 + :259, *Solver ctor :262-280). Pure citation-path firm-up; no claim/structure/edge/frontmatter change; the citations sit in prose/inline-code spans (not markdown links) so build-safe. Resolves the c103/c104-carried config-record main.cpp AMBIG residue — citecheck now 31 ok / 0 failing on the file. RE-READ off disk first (D1 had edited a different region — frontmatter back-ref + §Per-driver paragraph); no overlap. Build EXIT 0.
inputs:
  - book/src/concepts/config-record.md
  - palace/main.cpp:229-283 (codemap read_range, confirmed)
---

# CYCLE: Re-anchor config-record `main.cpp` citation paths

## Summary
The `config-record.md` record-definition page cites `palace/main.cpp` at several
points; the c104 critic flagged a citecheck `[AMBIG]` because the bare basename
`main.cpp` resolves to **two** files (`reference/palace/palace/main.cpp` and
`reference/palace/test/unit/main.cpp`). Two citations already carry the
disambiguating `palace/main.cpp` prefix (lines 50, 96); three sites still use the
bare `main.cpp:NNN` form (line 97 `main.cpp:257-281`, line 134 `main.cpp:231` and
`main.cpp:259`, line 137 `main.cpp:262-280`). This is a **pure citation-format
firm-up**: every bare `main.cpp:NNN` is repointed to `palace/main.cpp:NNN`. No
claim, structure, typed-edge, or line number changes — every range was
re-confirmed against source and is drift-free.

## Verification (citecheck + codemap read_range, on-disk)
All ranges read via codemap `read_range palace/main.cpp:229-283` and checked with
`tools/citecheck/citecheck.py`:

- `main.cpp:231` → `IoData iodata(argv[1], false);` at line 231. `[ok]` for
  `palace/main.cpp:231 --anchor IoData`. No drift.
- `main.cpp:259` → `switch (iodata.problem.type)` at line 259. Bare form returns
  `[AMBIG] main.cpp:259 — basename matches 2 files`; `palace/main.cpp:259
  --anchor 'problem.type'` resolves `[ok]`. No drift.
- `main.cpp:257-281` → the `const auto solver = [&]() -> std::unique_ptr<BaseSolver>`
  lambda opens at 257 and closes `}();` at 281. `[ok]` for
  `palace/main.cpp:257-281 --anchor BaseSolver`. No drift.
- `main.cpp:262-280` → the six `case ProblemType::…: return std::make_unique<…Solver>`
  branches (first `DrivenSolver` at 262, last `BoundaryModeSolver` continuation at
  280). `[ok]` for `palace/main.cpp:262-280 --anchor DrivenSolver`. No drift.

Confirmed disambiguation: bare `main.cpp:259` → `[AMBIG]`; `palace/main.cpp:259`
→ `[ok]`. The fix is exactly the prefix.

## Proposed changes

```edit:book/src/concepts/config-record.md
[old]: `palace/main.cpp:259` (the 6-branch dispatch; the lambda constructing the
`BaseSolver` spans `main.cpp:257-281`). The enum is
[new]: `palace/main.cpp:259` (the 6-branch dispatch; the lambda constructing the
`BaseSolver` spans `palace/main.cpp:257-281`). The enum is
```

```edit:book/src/concepts/config-record.md
[old]: - the spine-ROOT lifecycle column — `IoData iodata(argv[1], false)`
  (`main.cpp:231`) and the `problem.type` dispatch (`main.cpp:259`).
[new]: - the spine-ROOT lifecycle column — `IoData iodata(argv[1], false)`
  (`palace/main.cpp:231`) and the `problem.type` dispatch (`palace/main.cpp:259`).
```

```edit:book/src/concepts/config-record.md
[old]: - `BaseSolver` and every `*Solver` ctor take `iodata` (`main.cpp:262-280`).
[new]: - `BaseSolver` and every `*Solver` ctor take `iodata` (`palace/main.cpp:262-280`).
```

## Discipline notes
- Pure citation-path firm-up within the lifter mandate (vocabulary/path firm-up;
  structure + claims unchanged). No typed edge, frontmatter, status, or
  schema/table content touched — the `## Status`/`rank: firm` line and the
  `edges:` block are untouched.
- All four citation texts sit in **prose / inline-code spans**, not markdown
  link targets, so the change is build-safe (`linkcheck2` is unaffected — these
  are not `[...](...)` links). The only markdown links in the file point at the
  sibling concept page (`./build-time-vs-run-time-stratification.md`), which is
  not touched.
- Lines 50 (`palace/main.cpp:231`) and 96 (`palace/main.cpp:259`) already carry
  the full path; left as-is. The three remaining bare sites (lines 97, 134×2, 137)
  are the only edits.

## Supporting evidence
- `book/src/concepts/config-record.md` — the four bare-citation sites (lines 97,
  134, 137).
- `palace/main.cpp:229-283` — codemap `read_range`, all four ranges confirmed
  on-disk with no drift.
- `tools/citecheck/citecheck.py` runs (above) confirming bare→`[AMBIG]`,
  `palace/`-prefixed→`[ok]`.

## Open questions / caveats
None. The disambiguation is mechanical and the line numbers are confirmed exact.
