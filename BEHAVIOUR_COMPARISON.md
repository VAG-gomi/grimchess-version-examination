# Behaviour Comparison

## Status

This repository provides **computed structural evidence**, not a new behavioural experiment. It identifies changed source files and changed APK entries that may be relevant to behaviour.

## Relevance

`StockfishAdapter.ts` can affect engine command construction, response parsing, and move extraction. `PredictionMap.ts` can affect prediction/candidate handling. `IntegrityGuards.ts` can affect validation and error paths. These are functional-role observations from source location and content; they are not causal findings.

## Runtime forensic boundary

The Current F1 instrumentation and its runtime evidence remain in the Current forensic repository. A comparison result can generate a hypothesis, but the runtime file and a controlled reproduction are required before asserting causality.
