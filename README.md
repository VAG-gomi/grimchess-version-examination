# GrimChess Version Examination

This is a **derived analytical and educational repository** for understanding GrimChess across a pinned Current forensic archive and a pinned historical forensic archive. It does not replace either evidence repository, does not modify either input, and does not claim that every computed difference caused a behavioural change.

## Start here

1. Read [`EXAMINATION_GUIDE.md`](EXAMINATION_GUIDE.md).
2. Read [`EVIDENCE_INDEX.md`](EVIDENCE_INDEX.md) and [`FILE_NAVIGATION.md`](FILE_NAVIGATION.md).
3. Read [`GRIMCHESS_TIMELINE.md`](GRIMCHESS_TIMELINE.md) for what can and cannot be dated.
4. Read [`ARCHITECTURE.md`](ARCHITECTURE.md) to understand the application flow.
5. Read [`APK_COMPARISON.md`](APK_COMPARISON.md), [`SOURCE_COMPARISON.md`](SOURCE_COMPARISON.md), and [`ENGINE_COMPARISON.md`](ENGINE_COMPARISON.md).
6. Read [`BEHAVIOUR_COMPARISON.md`](BEHAVIOUR_COMPARISON.md) and [`LIMITATIONS.md`](LIMITATIONS.md) before interpreting results.

## Three-repository evidence chain

The project uses three repositories with separate responsibilities:

1. [`grimchess-f1-forensic`](https://github.com/VAG-gomi/grimchess-f1-forensic/tree/f7cd9a89e8c4f6366c7ed7a778ae3acf0b89e180) is the authoritative Current-version forensic evidence repository, including Current F1 runtime instrumentation.
2. [`grimchess-old-forensic`](https://github.com/VAG-gomi/grimchess-old-forensic/tree/6fbdc09a604ecb373981e1f4b2787b56a86076b4) is the authoritative historical forensic evidence repository for the preserved Old APKs and recovered historical source/build evidence.
3. This `grimchess-version-examination` repository is derived: it records methods, comparisons, and educational analysis computed from pinned inputs from the two authoritative evidence repositories.

The evidence chain is **Current forensic evidence + Old forensic evidence → derived examination and comparison results**. The genuine Current F1 `runtime_forensic.jsonl` evidence is still pending; no derived result in this repository should be read as a substitute for that runtime evidence.

## Source-of-truth repositories

- [Current forensic archive](https://github.com/VAG-gomi/grimchess-f1-forensic/tree/f7cd9a89e8c4f6366c7ed7a778ae3acf0b89e180)
- [Historical forensic archive](https://github.com/VAG-gomi/grimchess-old-forensic/tree/6fbdc09a604ecb373981e1f4b2787b56a86076b4)

All conclusions in this repository are derived results. The immutable inputs and method are recorded in [`COMPARISON_MANIFEST.json`](COMPARISON_MANIFEST.json).

## Release-readiness boundary

The two evidence repositories are authoritative for their respective evidence; this examination repository is derived. Publication is an owner-controlled action. Publication does not mean the candidate error has been solved, and runtime causality has not yet been established. Source, APK, and comparison differences must not be presented as causal findings without supporting runtime evidence.
