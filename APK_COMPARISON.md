# APK Comparison

The complete per-entry records are in [`results/apk/current_vs_old_apk_pairs.json`](results/apk/current_vs_old_apk_pairs.json). The Current reference is `CURRENT-F1` with SHA-256 `77f33dc3a825c02a59d65c011b52956b85d081b01008ea82c7ef1c6b34b209dc`.

| Pair | Byte-identical entries | Added | Removed | Modified |
|---|---:|---:|---:|---:|
| Current F1 vs OLD-APK-001 | 22 | 291 | 256 | 183 |
| Current F1 vs OLD-APK-002 | 86 | 404 | 404 | 6 |
| Current F1 vs OLD-APK-003 | 86 | 404 | 404 | 6 |
| Current F1 vs OLD-APK-004 | 86 | 404 | 404 | 6 |

For `OLD-APK-002` through `OLD-APK-004`, the six common modified entries are the binary manifest, signature manifest metadata, embedded `assets/public/index.html`, two DEX files, and `resources.arsc`. The 404 additions/removals are largely packaging/signing/container-entry differences. This is an entry-level classification, not a claim that the six modified entries are all behavioural.

`OLD-APK-001` has a different package identity and much larger entry-level divergence; it must not be treated as a minor rebuild of the other three without further evidence.
