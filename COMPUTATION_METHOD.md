# Computation Method

The comparison uses deterministic local processing over clones checked out to the pinned commits. APKs are read as ZIP archives without modification. Each entry is represented by path, uncompressed size, and SHA-256. Source files are compared by canonical relative path, byte size, and SHA-256. Build and engine subsets are selected by documented filename/path rules.

Statuses are `BYTE-IDENTICAL`, `ADDED`, `REMOVED`, or `MODIFIED`. `BYTE-IDENTICAL` is stronger than same filename. `CONTENT-EQUIVALENT` and `FUNCTIONALLY-SIMILAR` are not assigned by this computation.

The algorithm is implemented in [`scripts/compare_pinned.py`](scripts/compare_pinned.py). Run it with explicit `--current-repo PATH` and `--old-repo PATH` arguments; both clones must be checked out to the exact commits in `inputs/PINNED_INPUTS.json`. Generated build outputs are not included as source evidence.

Limitations include no APK decompilation-to-source proof, no semantic JavaScript equivalence analysis, no runtime device execution, and no causal inference.
