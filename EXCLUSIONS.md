# EXCLUSIONS

This repository is the venture timeline of Ambient Systems (private). Everything in the working archive is included **except** the categories below. Excluded material stays in Ivan Damnjanovic's private OneDrive records. This file deliberately names no third parties.

| Category | Why | Rows | GB | Where it is kept |
|---|---|---:|---:|---|
| Legal, finance and email (contracts, agreements, NDAs/LoIs/MoUs, corporate/statutory filings, bank and KYC, purchases/receipts/invoices/quotes, email printouts and mailbox exports) | Legal and financial records | 112 | 0.28 | Records/40 Legacy entities (41 SG, 42 CA, 43 QC); mailbox exports in Records/20/28 |
| Third-party personal data (other people's CVs and profiles, contact lists, investor databases, cohort lists, team-detail forms, evaluator lists, comment exports) | Privacy | 72 | 0.07 | Contacts were consolidated into a private, unshared contact record. The source copies and third-party CVs were deleted |
| Credentials (password store; files containing shared passwords; signature specimen) | Security | 4 | 0.0 | Private only. Move to a password manager |
| Duplicates and backup snapshots | Redundant | 139 | 6.06 | Original copy published once |

Pre-publication review (2026-10-02) was resolved item by item: own application forms, brochures and venture documents stay in (personal phone number redacted); anything showing or naming third parties, third-party published works and licensed stock was removed. Identity documents (passport/ID/permit scans) are never included.

[redacted]

Company milestones that rest on excluded records (incorporation, the company name appeal, programme agreements, strike-off) appear in TIMELINE.md as event-only entries without the underlying document.

## Large videos
Videos over 50 MB were fetched separately (direct download) and are published as release assets (phase-2020-04, phase-2020-07-videos, phase-2021-H1), not in git.

## Added during the 2020-07 build
- Signed GRIP assignment cover forms (Assignment 1-3 "cc-Signed"): carry a signature - kept in OneDrive.
- GRIP Run 4 FDR mentor notes and Zoom chat feedback: name third-party mentors/participants - kept in OneDrive.
- 00 Templates / ICON PACK and Infograpia Templates: licensed third-party stock packs, no venture content - kept in OneDrive.
- MVP Studio Prototyping.mp4 (308 MB) and 2020-11-08 Ambient.mp4 (70 MB): backfilled into the phase-2020-07-videos release asset.

## CVs (ruling 2026-10-02)
All CVs/resumes - including Ivan Damnjanovic's own - are excluded from the repository and releases. The source CV files were removed from the OneDrive venture tree.

## Pre-publication review resolution (2026-10-02)
Removed from the repository (kept in OneDrive):
- Third-party published works: research papers, textbook chapters, vendor/industry reports, product web pages, market-data printouts, library guides, infographic/template packs.
- Other GRIP teams' factsheets and Lift-Off booklets (Runs 1-5), screenshots of other teams' presentations and Zoom galleries.
- A GRIP evaluation sheet whose cell comments name programme evaluators.
- A workshop screenshot showing a consultant's name and phone number.

## Added during the 2021-H1 build
- Patent attorney specification/figure drafts and patent-office search reports: legal - backed up to Records/40 (41, From venture archive), not in the repo. The as-filed application form (inventor/applicant personal details) and invention-disclosure forms stay in OneDrive.
- GRIP pitch-training slides and recordings by external trainers, a pitch-practice recording showing other participants, Zoom screenshots with other people, and other teams' Run 5 factsheets.
- Third-party material: competitor benchmark folder, competitor logos and stock icon sets, licensed stock photo libraries, slide-template packs, vendor/corporate-secretary decks, third-party flyers, directories and annual reports, business-development partner brochures, competitor UI screenshots, prior-art research, legal templates and example models.
- Email printouts (application confirmations/feedback) - kept in OneDrive.
- Another startup's pitch material - kept in OneDrive.
- Duplicate folders (re-filed GRIP Run 4 deliverables, Run 5 marketing copies, notebook checkpoints, repeated business-plan and application files).

## Withheld for privacy (public snapshot only)

The orphan branch `public-snapshot` is built from this archive with additional paths removed. They remain in the private repository but are not published. Reasons are grouped without naming individuals:

| Group | Why withheld |
|---|---|
| CRM and sales exports | Screenshots of contact databases with third-party emails and phone numbers |
| Technical user manuals and engineering summaries | Embedded network credentials, cloud API keys, and operational passwords |
| Standard operating procedures and end-user guides | Author names, vendor contacts, and credential examples |
| Accelerator and university application PDFs | Personal contact details, demographic answers, and CV-style pages |
| Team roster forms, LLP booklets, and social calendars | Other participants' names, photos, and schedules |
| Selected business plans and charter documents | Co-founder, shareholder, and advisor personal details |
| Programme photo grids and infosheets | Other cohort members visible in screenshots |
| Corrupt or template-only workshop decks | Unreliable files plus third-party programme staff imagery |

The machine-readable path list lives in `_private-tooling/scripts/public_snapshot_excludes.txt`. Snapshot preparation also drops files that still match automated third-party contact scans.

## CI verification allowlists (false positives)

GitHub Actions runs `export_public_snapshot_tree.sh` and `verify_round5.py --gate` on pull requests. Residual regex hits that are not personal data are documented in `_private-tooling/scripts/verify_allowlist.txt`:

- **DOB-shaped strings** in CSV/XLSX demo and sensor logs, root timeline/readme files, and GRIP pitch-deck revision dates (operational dates, not birth dates).
- **Email addresses** on published company decks (`@ambientsystems.ai`, `@ambientsystems.sg`) and programme portals (NUS GRIP, EnterpriseSG, Y Combinator, EFL, IPI TechInnovation operator).

Ivan Damnjanovic’s business address `ivan@ambientsystems.ai` is intentionally retained on public materials.

Additional snapshot-only withholds (2026-10 follow-up): all eight SMU ACE Panasonic platform SOP documents under `2022-04-28 Engineering Documentation/User Manuals (2022)/` (operational steps with author and vendor contact context), and the Singrow prototype launcher script `ABsystem_autorun.sh` (environment and service account hints). The `ABsystem/` application folder was already withheld; the autorun script is withheld separately so the public tree does not ship deployment glue tied to private credentials.

## Added during the 2025 and 2026 builds
- Own application forms (2025) stay in with personal fields redacted (home address, phone numbers, demographic and income answers).
[redacted]
- A company registry business profile and a government R&D survey return: corporate records - moved to Records/40 (41, From venture archive).
- Finance and admin playbooks (accounting process, annual close and filing, chart of accounts, group financial statements): finance records - kept in OneDrive.
- Platform code snapshot (2026-03-13): published with the web API key value redacted.
- OneDrive archive admin notes (folder guide, merge log, "moved" pointer stubs): not venture material.
- Founder CV and profile printouts found in the 2026 folders: excluded under the CV ruling.
- Byte-identical copies in the March 2026 final backup (design screenshots, hackathon video) and repeated logo files: the original copy is published once.