# SIZE PLAN

Target: git history about 2-3 GB, no Git LFS, one commit (and push) per phase.

## Rules
| What | Where |
|---|---|
| Documents, PDFs, spreadsheets, text/code, small images (normally < 10 MB, never > 50 MB) | committed in the phase folder |
| Videos, bulky image/media folders, decks > 100 MB, any file > 50 MB | one release zip per phase (`phase-...` tag), split below 2 GB per asset |
| Duplicates / backup snapshots | dropped; the dated main-tree copy is kept |
| Legal, finance, email, third-party PII, credentials | excluded (EXCLUSIONS.md) |

## Status by phase
See the table at the end of this file (updated after each phase push).

| Phase folder | Files in folder | MiB in folder | Release asset(s) |
|---|---:|---:|---|
| 2020-04 Origin and first applications | 29 | 25.5 | phase-2020-04.zip (897.6 MiB) |
| 2020-07 NUS GRIP Run 4 | 110 | 315.6 | phase-2020-07.zip (93.7 MiB) + phase-2020-07-videos.zip (636.4 MiB) |
| 2021-H1 NUS GRIP Run 5 and spin-out | 186 | 512.2 | phase-2021-H1-part1.zip (1.86 GiB) + part2 (235.6 MiB) |
| 2021-H2 Singapore company - patents and accelerators | 88 | 223.2 | phase-2021-H2.zip (548.4 MiB) |
| 2022 Singapore accelerators - SMU ACE Panasonic | 139 | 286.6 | phase-2022.zip (728.3 MiB) |
| 2023 Panasonic DTC and Hong Kong discovery | 135 | 261.9 | phase-2023.zip (249.8 MiB) |
| 2024 Hong Kong and Quebec - data platform | 333 | 593.7 | phase-2024.zip (1.03 GiB) |
| 2025 Global version - HK Canada Japan | 48 | 48.4 | phase-2025.zip (181.8 MiB, 69 files) |
| 2026 Agency model and wind-down | 49 | 49.2 | phase-2026.zip (172.9 MiB, 18 files) |

Status 2026-10-04: all phases (2020-04 to 2026) built and pushed (1,117 files, 2,316.3 MiB in the phase folders; releases listed above). Files are counted by the folder they sit in: later builds also add older-dated documents to earlier phase folders (e.g. the 2025 and 2026 builds added 2021-2024 documents found in their working folders).
Note: 2021-H1 alone holds ~20 investment-deck versions of 25-47 MB each (~607 MiB of git-eligible files before folders). To stay inside the 2-3 GB git target, the later phases should commit decks as PDF and move the original .pptx of each deck version into the phase release zip.
