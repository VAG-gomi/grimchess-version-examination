# Architecture

The following map is grounded in recoverable source paths.

```text
UI
  └─ src/App.tsx
      └─ session and move state
          └─ src/simulator/ChessSimulator.ts
              └─ move processing and classification
                  └─ src/simulator/StockfishAdapter.ts
                      └─ public/stockfish/*.js + *.wasm
                          └─ UCI commands, responses, scores, bestmove
                              └─ simulator/paradox/PredictionMap.ts
                                  └─ contradiction / prediction result
                                      └─ UI state and forensic trace (Current)
```

| Component | Old evidence path | Current evidence path | Examination status |
|---|---|---|---|
| UI entry | `recovered-source/.../src/App.tsx` | `src/src/App.tsx` | Modified |
| Chess simulator | `.../src/simulator/ChessSimulator.ts` | `src/src/simulator/ChessSimulator.ts` | Byte-identical in computed source comparison |
| Engine adapter | `.../src/simulator/StockfishAdapter.ts` | `src/src/simulator/StockfishAdapter.ts` | Modified |
| Stockfish assets | `.../public/stockfish/` | `src/public/stockfish/` | Compare exact asset paths/hashes in the APK/source results |
| Prediction system | `.../src/simulator/paradox/PredictionMap.ts` | `src/src/simulator/paradox/PredictionMap.ts` | Modified |
| Current forensic trace | unavailable in Old source | `src/src/forensics/ForensicTrace.ts` | Current-only addition |
