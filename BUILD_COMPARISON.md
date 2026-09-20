# Build Comparison

Build comparison covers Gradle, Capacitor, package manifests, lockfiles, TypeScript configuration, Vite configuration, and Android settings. The evidence archives use different path layouts: Old keeps the mobile project under `recovered-source/grimchess-mobile/`, while Current separates `src/`, `src/android/`, and `build-config/`.

The computed result therefore records path additions/removals as archive-layout changes when the corresponding file bytes match. Canonical build files such as `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `vite.config.ts`, `tsconfig.json`, `capacitor.config.ts`, and Android Gradle settings are present with matching byte content where the corresponding evidence files were compared.

This does not prove that dependencies were installed identically, that generated assets were identical, or that either archive reproduces the exact historical signing process.
