# File Navigation

| Question | Read first | Then read | What it can answer |
|---|---|---|---|
| What is GrimChess? | `EXAMINATION_GUIDE.md` | `ARCHITECTURE.md` | Evidence-backed system overview |
| Which file controls the engine? | Current `src/src/simulator/StockfishAdapter.ts` | `ENGINE_COMPARISON.md` | Engine adapter changes and hashes |
| Where is Stockfish? | Current `src/public/stockfish/` or Old `recovered-source/.../public/stockfish/` | APK inventory | JS/WASM asset locations |
| Where is candidate/prediction logic? | `src/src/simulator/paradox/PredictionMap.ts` | `results/engine/engine_comparison.json` | Exact source modification record |
| Where is the Android build configured? | `src/android/app/build.gradle` and `build-config/` | `BUILD_COMPARISON.md` | Build inputs and layout differences |
| Which files changed? | `SOURCE_COMPARISON.md` | `results/source/source_comparison.json` | Byte-level source statuses |
| Which APKs are preserved? | `EVIDENCE_INDEX.md` | pinned evidence repositories | APK IDs, hashes, and provenance |
| What is unproven? | `LIMITATIONS.md` | `PROVENANCE.md` | Boundaries against overinterpretation |
