# Companion repository

This directory is the runnable practice surface for *PM Is Now Another Member of Technical Staff*. It is intentionally small: readers inspect bounded product artifacts, run deterministic checks, and then use the workbook to make decisions. It is not a production application or a coding curriculum.

## Runtime promise

The no-key path requires only:

- Python 3.11 or later;
- SQLite 3.40 or later; and
- a POSIX-compatible shell.

No cloud account, model API key, production credential, package installation, or customer data is required. The Python validators use only the standard library. Illustrative model prompts can be inspected without calling a model.

Run the complete companion check from the repository root:

```sh
./scripts/validate_companion.sh
```

The command exits non-zero if a fixture no longer matches the manuscript's promised behavior. Expected summary:

```text
Chapter 2 API contract validation passed.
Chapter 5 representative SQL examples passed.
Chapter 6 tracking validation passed.
Chapter 13 evaluation passed: v1 2/5; v2 5/5.
Chapter 14 calibration record validation passed.
Chapter 16 repo-orientation validation passed: documented 5 MB; implemented 3 MB.
HarborCart dataset validation passed: 17 reviews, aligned labels, required edge cases present.
Companion validation passed.
```

## Chapter map

| Chapter | Artifact | Reader action | Verification |
| --- | --- | --- | --- |
| 2 | `api/` | Compare one request with success, validation, and provider-failure responses; map each state to product behavior | `python3 companion/api/validate_contract.py` |
| 5 | `sql/` | Run representative SQL and compare deterministic output | `./companion/sql/validate_chapter_05.sh` |
| 6 | `analytics/` | Inspect a tracking plan and test valid and invalid event envelopes | `python3 companion/analytics/validate_tracking.py` |
| 7 | `experiments/chapter_07_statistical_interpretation_lab.md` | Interpret supplied experimental outputs and challenge validity | Worksheet; no calculator or external service required |
| 13 | `ai_evaluation/` | Compare two resolver versions against a held-out constructed set and severity-aware gates | `python3 companion/ai_evaluation/evaluate.py` |
| 14 | `calibration/` | Inspect a filled failure-to-change-to-regression record tied to the Chapter 13 cases | `python3 companion/calibration/validate_record.py` |
| 16 | `repo_orientation/` | Find a contradiction between product documentation and implemented validation, then compare with the expected orientation record | `python3 companion/repo_orientation/validate_task.py` |
| 19 | `feedback_instrument/` | Inspect a synthetic labelled feedback set containing abstention and difficult language cases | `python3 companion/feedback_instrument/validate_dataset.py` |
| All | `figures/` | Reuse or inspect every book diagram as an individual PNG or scalable SVG; consult the manifest for captions and alt text | Checked during release packaging |
| All | `templates/` and `pm_mts_workbook.md` | Apply 25 chapter-aligned records to one bounded product problem | `./scripts/assemble_workbook.sh` |
| All | `PM-MTS-Workbook.pdf` | Print or annotate the standalone 52-page A4 workbook | Verified in the publication release pipeline |

## Data and rights boundary

All named companies and people in runnable fixtures are fictional. The feedback reviews are synthetic. No Heatseeker customer data, Meta creative, Tokopedia review text, Qlip material, Shipper operational data, employer code, or GoPractice content appears here.

## Maintenance rule

When a chapter changes an artifact field, expected state, or term, update the corresponding fixture and validator in the same revision. A passing manuscript audit does not substitute for this companion check.
