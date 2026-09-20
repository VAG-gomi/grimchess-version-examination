# Computation scripts

`compare_pinned.py` is the deterministic comparison implementation used for the current result set. It reads two local clones at the pinned commits documented in [`inputs/PINNED_INPUTS.json`](../inputs/PINNED_INPUTS.json), inventories APK ZIP entries, compares canonical source files, and emits JSON result records. It does not write to either input repository.

The script uses SHA-256 for extracted APK entries and source files, records exact paths and sizes, and uses Git object hashes only where explicitly documented. Its current environment paths are `/home/ubuntu/comparison-current` and `/home/ubuntu/comparison-old`; a future rerun should update those paths or parameterize them before execution.
