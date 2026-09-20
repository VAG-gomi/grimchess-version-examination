# Engine Comparison

The dedicated engine comparison selects source paths containing `engine`, `StockfishAdapter`, `Stockfish`, `PredictionMap`, or `paradox`. It reports 13 byte-identical files and 2 modified files.

The modified engine-relevant files are:

- `src/simulator/StockfishAdapter.ts`
- `src/simulator/paradox/PredictionMap.ts`

The exact old/current hashes and sizes are in [`results/engine/engine_comparison.json`](results/engine/engine_comparison.json). Stockfish JS/WASM assets are separately inventoried in each APK record. No claim is made here about UCI semantic equivalence, candidate-generation correctness, or runtime causality without controlled execution evidence.
