# Companion Practice Surface

This directory contains the bounded examples, worksheets, datasets, and optional checks used by *PM Is Now Another Member of Technical Staff*. It is not a production application or a coding curriculum.

If you are a reader, begin with the repository [README](../README.md), [one of the 20 chapter guides](chapters/README.md), [Companion Map](../COMPANION_MAP.md), or [AI Agent Guide](../AI_GUIDE.md). Do not start by running every script.

## Artifact-first map

| Chapter | Inspect first | Product question | Optional verification |
| --- | --- | --- | --- |
| 2 | [`api/README.md`](api/README.md) | What request, response, failure, and control states make the API behavior complete? | `python3 companion/api/validate_contract.py` |
| 5 | [`sql/sakila/README.md`](sql/sakila/README.md) | What does the exact SQL measure, at what grain, and what can the result not prove? | `./companion/sql/validate_chapter_05.sh` |
| 6 | [`analytics/README.md`](analytics/README.md) | Can the event contract support the product decision it claims to inform? | `python3 companion/analytics/validate_tracking.py` |
| 7 | [`experiments/chapter_07_statistical_interpretation_lab.md`](experiments/chapter_07_statistical_interpretation_lab.md) | What decision rule should exist before the result arrives? | Worksheet |
| 13 | [`ai_evaluation/README.md`](ai_evaluation/README.md) | Which cases and failures determine whether an AI capability may ship? | `python3 companion/ai_evaluation/evaluate.py` |
| 14 | [`calibration/README.md`](calibration/README.md) | Does a proposed change remain connected to the preserved failure and regression evidence? | `python3 companion/calibration/validate_record.py` |
| 17 | [`repo_orientation/README.md`](repo_orientation/README.md) | What does the repository prove, contradict, and leave unresolved? | Optional public-repo check |
| Optional lab | [`feedback_instrument/README.md`](feedback_instrument/README.md) | Can synthetic reviews become a bounded, evaluated product instrument? | `python3 companion/feedback_instrument/validate_dataset.py` |
| All | [`templates/`](templates/) and [`pm_mts_workbook.md`](pm_mts_workbook.md) | How does the reader apply the chapter to one bounded product problem? | `./scripts/assemble_workbook.sh` |

## Why Python still exists here

The Python files are small deterministic verifiers. They check that teaching fixtures remain internally consistent as the repository evolves. They do not teach the chapter by themselves, call a model, contact a production service, or establish that a real system is correct.

The intended order is:

1. understand the product question;
2. inspect the human-readable artifact;
3. predict the result;
4. optionally run the narrow check; and
5. translate the output into a decision and evidence boundary.

## Complete no-key verification

Maintainers and readers who intentionally want to check every self-contained fixture can run:

```sh
./scripts/validate_companion.sh
```

Expected summary:

```text
Chapter 2 API contract validation passed.
Chapter 5 Sakila load, book queries, and captured result passed.
Chapter 6 tracking validation passed.
Chapter 13 evaluation passed: v1 2/5; v2 5/5.
Chapter 14 calibration record validation passed.
Chapter 17 repo-orientation check skipped: clone Noted beside pm-mts or set NOTED_REPO_PATH to include it.
HarborCart dataset validation passed: 17 reviews, aligned labels, required edge cases present.
Companion validation passed.
```

The no-key path requires Python 3.11+, SQLite 3.40+, and a POSIX-compatible shell. It needs no cloud account, model API key, package installation, production credential, or customer data.

## Data and rights boundary

Named companies and people in constructed runnable fixtures are fictional, and feedback reviews are synthetic. Chapter 5 vendors the open-licensed generated Sakila SQLite data with its provenance and licence notices. Chapter 17 intentionally inspects the author’s public Noted repository at a cited commit. No employer code, credentials, customer data, or confidential artifacts belong here.

## Maintenance rule

When an artifact field, expected state, or book term changes, update its fixture, human-readable README, and verifier in the same revision. A passing script does not substitute for checking that the reader-facing explanation still matches the book.
