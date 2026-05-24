# Test linkages

This directory accumulates the **source → test** mapping for Palace.

Palace's tests live in a parallel topic-keyed tree (`reference/palace/test/unit/test-<topic>.cpp`, also `reference/palace/test/examples/`), **not** alongside the source they exercise. Discovering and recording the linkages is itself work — this is where it accumulates.

## When to write here

- An Explorer (or session author) has discovered which tests exercise a given source file or symbol.
- Linkage is non-obvious: a test name doesn't directly imply its source coverage, or one test exercises symbols from multiple source files.
- A test pins a semantic claim the source alone doesn't make obvious — a load-bearing trick visible by what the test fails under, an invariant the test holds but the source doesn't state.

## File shape

One file per source area, named after the area (not the test file). Examples:

```
scaffolding/test-linkages/cg-solver.md       # tests touching CG-related source
scaffolding/test-linkages/vector.md          # tests touching linalg/vector.cpp
scaffolding/test-linkages/fe-assembly.md     # tests touching FE assembly
```

Within each file, suggested content (free-form — refine from use):

- **Source file(s) covered** — `palace/linalg/<file>.cpp` etc.
- **Test file** — `test/unit/test-<topic>.cpp`.
- **Test names** with brief notes on what each pins (mutation pattern, algebraic equivalence, load-bearing-trick evidence, boundary case).
- **Coverage gaps** — what the tests don't exercise (escalation candidates for execution grounding, Phase 7).

## Known topic-keyed test files (initial inventory)

For a starting orientation; not exhaustive linkage information, just a directory listing of tests with naming-pattern hints. **Linkages are not asserted until verified** — i.e., a test's name implies a likely topic, not a guaranteed source-file coverage.

```
test/unit/test-2d-submesh.cpp            # submesh extraction
test/unit/test-basesolver.cpp            # drivers/basesolver.cpp
test/unit/test-boundarymodeoperator.cpp  # boundary-mode operators
test/unit/test-coefficient.cpp           # coefficient evaluation
test/unit/test-config.cpp                # config schema
test/unit/test-constants.cpp             # physical/numerical constants
test/unit/test-domainpostoperator.cpp    # post-processing operators
test/unit/test-geodata.cpp               # geometric data
test/unit/test-libceed.cpp               # libCEED integration (large — ~1500 lines)
test/unit/test-lumpedportintegration.cpp # lumped port integration
test/unit/test-materialoperator.cpp      # material operators
test/unit/test-memoryreporting.cpp       # memory reporting
test/unit/test-nondimensionalize.cpp     # non-dimensionalization
test/unit/test-orthog.cpp                # orthogonalization
test/unit/test-postoperator.cpp          # post-processing
test/unit/test-postoperatorcsv.cpp       # post-processing CSV output
test/unit/test-rap.cpp                   # RAP (restriction–A–prolongation) operators
test/unit/test-romoperator.cpp           # reduced-order model operators
test/unit/test-schema.cpp                # config schema validation
test/unit/test-strattonchu.cpp           # Stratton–Chu boundary conditions
test/unit/test-tablecsv.cpp              # table CSV output
test/unit/test-vector.cpp                # vector operations
```

`test/examples/` holds end-to-end example-driven tests against the configurations in `examples/`.

## Status

Currently empty (no per-area linkage files yet). First entries land as the agent loop runs, or as session work surfaces them.
