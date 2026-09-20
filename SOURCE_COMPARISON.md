# Source Comparison

The canonical source comparison maps Old `recovered-source/grimchess-mobile/src/` to Current `src/src/`.

| Status | Count |
|---|---:|
| BYTE-IDENTICAL | 29 |
| MODIFIED | 5 |
| ADDED in Current | 1 |
| REMOVED from Current | 0 |

Modified files: `App.tsx`, `simulator/BenchmarkSuite.ts`, `simulator/IntegrityGuards.ts`, `simulator/StockfishAdapter.ts`, and `simulator/paradox/PredictionMap.ts`. The Current-only file is `forensics/ForensicTrace.ts`.

Every row with old/current SHA-256 values is in [`results/source/source_comparison.json`](results/source/source_comparison.json). “BYTE-IDENTICAL” means the compared files’ bytes matched; it does not prove identical runtime execution or identical build output.
