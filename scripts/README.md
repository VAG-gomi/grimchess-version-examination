# Computation scripts

`compare_pinned.py` is the deterministic comparison implementation used for the current result set. It reads two local clones at the pinned commits documented in [`inputs/PINNED_INPUTS.json`](../inputs/PINNED_INPUTS.json), inventories APK ZIP entries, compares canonical source files, and emits JSON result records. It does not write to either input repository.

Run it with explicit portable input paths:

```text
python3 scripts/compare_pinned.py --current-repo PATH --old-repo PATH [--out PATH]
```

`--out` defaults to a `GRIMCHESS-VERSION-EXAMINATION` directory in the current working directory. The script uses SHA-256 for extracted APK entries and source files, records exact paths and sizes, and uses Git object hashes only where explicitly documented.

The two evidence repositories are authoritative for their respective evidence, while this repository is derived. Publication is an owner-controlled action; publication does not mean the candidate error has been solved, and runtime causality has not yet been established. No comparison output should be treated as a causal runtime finding without the pending genuine Current F1 `runtime_forensic.jsonl` evidence.
