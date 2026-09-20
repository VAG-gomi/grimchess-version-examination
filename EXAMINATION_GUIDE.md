# Examination Guide

## Chapter 1 — What is GrimChess?

The pinned evidence describes GrimChess as an Android application built with a Capacitor/WebView mobile shell and a TypeScript/React application. Its recovered source contains a chess simulator, game/session state, UI components, a Stockfish JavaScript/WebAssembly engine integration, and simulator/paradox prediction systems. These statements are evidence-backed descriptions of the available source and APK contents, not claims about every historical version.

## Chapter 2 — Historical builds

The historical archive preserves four distinct APK evidence objects, `OLD-APK-001` through `OLD-APK-004`. Their order is **unknown**. The Current archive pins one F1 APK. An earlier hash is recorded separately because it is byte-identical to `OLD-APK-002`; provenance labels must not be collapsed merely because the bytes match.

## Chapter 3 — How to read this repository

Begin with `EVIDENCE_INDEX.md`, then use `FILE_NAVIGATION.md` to route questions to source files and result records. Use `COMPUTATION_METHOD.md` to understand how a result was produced. Treat `RESULTS.md` as a summary, not as replacement evidence.

## Chapter 4 — APK anatomy

An APK is a ZIP package containing a binary manifest, DEX files, resources, WebView assets, JavaScript, WebAssembly, and signing metadata. This examination compares ZIP entry paths, sizes, and SHA-256 values. A whole-APK hash difference alone is not a behaviour claim.

## Chapter 5 — Source architecture

The source comparison canonicalises the old mobile source root against the Current `src/src` root. It reports byte identity, additions, removals, and modifications, while retaining each side’s hash and path.

## Chapter 6 — Build system

The build examination compares Gradle, Capacitor, package, lockfile, TypeScript, and Vite configuration. Path relocation between the two evidence archives is reported as an archive-layout issue unless bytes differ.

## Chapter 7 — Engine architecture

The engine route is `StockfishAdapter.ts` → Stockfish JavaScript/WASM assets → UCI response parsing → simulator and paradox/prediction logic. The computed source results identify exact byte identity or modification; they do not prove runtime equivalence.

## Chapter 8 — Old versus Current

The source-level result is 29 byte-identical files, 1 Current-only file, and 5 modified files among the compared canonical source paths. The modified set includes `App.tsx`, `BenchmarkSuite.ts`, `IntegrityGuards.ts`, `StockfishAdapter.ts`, and `PredictionMap.ts`.

## Chapter 9 — Behaviour

This repository records computed differences and connects them to possible subsystem relevance. It does not perform a new device runtime experiment and does not convert any difference into a cause.

## Chapter 10 — Runtime forensic connection

The Current archive contains F1 observational instrumentation. Differences in `StockfishAdapter.ts`, `PredictionMap.ts`, and `IntegrityGuards.ts` are potentially relevant to the Current runtime investigation because of their functional roles, but causal linkage requires controlled runtime evidence.

## Chapter 11 — Unknowns

APK-to-source production identity, historical chronology, exact dependency resolution at each build, runtime execution equivalence, and causal explanations remain bounded or unknown.
