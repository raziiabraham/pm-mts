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
Chapter 5 Sakila load, book queries, and captured result passed.
Chapter 6 tracking validation passed.
Chapter 13 evaluation passed: v1 2/5; v2 5/5.
Chapter 14 calibration record validation passed.
Chapter 17 repo-orientation check skipped: clone Noted beside pm-mts or set NOTED_REPO_PATH to include it.
HarborCart dataset validation passed: 17 reviews, aligned labels, required edge cases present.
Companion validation passed.
```

## Chapter map

| Chapter | Artifact | Reader action | Verification |
| --- | --- | --- | --- |
| 2 | `api/` | Compare one request with success, validation, and provider-failure responses; map each state to product behavior | `python3 companion/api/validate_contract.py` |
| 5 | `sql/sakila/` | Load the real generated Sakila SQLite data, print the book's product-first query and actual result, then run an agent-assisted follow-up query | `./companion/sql/validate_chapter_05.sh` |
| 6 | `analytics/` | Inspect a tracking plan and test valid and invalid event envelopes | `python3 companion/analytics/validate_tracking.py` |
| 7 | `experiments/chapter_07_statistical_interpretation_lab.md` | Interpret supplied experimental outputs and challenge validity | Worksheet; no calculator or external service required |
| 13 | `ai_evaluation/` | Compare two resolver versions against a held-out constructed set and severity-aware gates | `python3 companion/ai_evaluation/evaluate.py` |
| 14 | `calibration/` | Inspect a filled failure-to-change-to-regression record tied to the Chapter 13 cases | `python3 companion/calibration/validate_record.py` |
| 17 | `repo_orientation/` | Inspect the public Noted repository at the cited commit and record a documented-versus-implemented storage-contract contradiction | `python3 companion/repo_orientation/validate_task.py /path/to/noted-main` |
| Companion lab | `feedback_instrument/` and `app_reviews_product_instrument.md` | Work through the optional app-review-to-product-instrument chapter and inspect its synthetic labelled feedback set | `python3 companion/feedback_instrument/validate_dataset.py` |
| All | `figures/` | Reuse or inspect all 24 book figures as individual PDF, PNG, or scalable SVG files; consult the manifest for captions and alt text | Checked during release packaging |
| All | `templates/` and `pm_mts_workbook.md` | Apply 26 chapter-aligned records to one bounded product problem | `./scripts/assemble_workbook.sh` |
| All | `../PM-MTS-Workbook.pdf` | Print or annotate the standalone 55-page A4 workbook | Verified in the publication release pipeline |

## Data and rights boundary

Named companies and people in the constructed runnable fixtures are fictional, and the feedback reviews are synthetic. Chapter 5 is the stated exception: it vendors the open-licensed generated Sakila SQLite sample data and retains its provenance and licence notices. No Heatseeker customer data, Meta creative, Tokopedia review text, Qlip material, Shipper operational data, employer code, or GoPractice content appears here.

## Maintenance rule

When a chapter or companion lab changes an artifact field, expected state, or term, update the corresponding fixture and validator in the same revision. A passing manuscript audit does not substitute for this companion check.
