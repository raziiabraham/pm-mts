# PM MTS Companion

Companion materials for *PM Is Now Another Member of Technical Staff* by Razii Abraham.

This repository gives readers a printable workbook, editable templates, bounded technical exercises, sample datasets, and deterministic checks that require no API key or cloud account.

## Start here: clone the companion

The primary way to use this companion is to clone it to your computer, open the folder in an AI coding agent, and ask the agent to guide you through the exercise for the chapter you are reading.

### 1. Clone the repository

Open a terminal and run:

```sh
git clone https://github.com/raziiabraham/pm-mts.git
cd pm-mts
```

Cloning means making a local copy that you and your coding agent can inspect safely. If you prefer a graphical interface, use **GitHub Desktop → File → Clone repository**, enter `raziiabraham/pm-mts`, and choose a local folder.

### 2. Open the cloned `pm-mts` folder in your AI coding agent

Use any local coding agent that can read files and run terminal commands. Start with a prompt such as:

> I am reading Chapter 2 of *PM Is Now Another Member of Technical Staff*. Read `README.md`, `AGENTS.md`, and `companion/api/README.md`. Do not change any files yet. Explain the exercise in plain language, show me the files in the order I should inspect them, run the Chapter 2 validator, and translate the result for a product manager who is new to Python.

The agent should explain each command before running it. A passing validator confirms only that the supplied teaching fixture matches its expected contract; it is not evidence that a production system is correct.

### 3. Follow the chapter exercise

See [Getting Started](GETTING_STARTED.md) for screenshots-free, step-by-step instructions, including the exact Chapter 2 Python command, Windows alternatives, expected output, and troubleshooting.

## Prefer the workbook without local setup?

- [Download the 52-page printable workbook](PM-MTS-Workbook.pdf)
- [Download all 25 printable diagrams](PM-MTS-Printable-Figures.pdf)
- [Edit the workbook in Markdown](companion/pm_mts_workbook.md)
- [Browse the individual templates](companion/templates/)
- [Browse individual printable figure PDFs](companion/figures/pdf/)
- [Download the latest complete companion package](https://github.com/raziiabraham/pm-mts/releases/latest)

## What is included

| Area | What readers can do |
| --- | --- |
| `companion/templates/` | Complete 25 reusable, chapter-aligned product records |
| `companion/api/` | Inspect and validate request, success, validation-error, and provider-error states |
| `companion/sql/` | Run representative SQL against deterministic sample data |
| `companion/analytics/` | Inspect a tracking plan and validate event envelopes |
| `companion/ai_evaluation/` | Compare two AI-output versions against a held-out constructed set |
| `companion/calibration/` | Trace a failure through change and regression evidence |
| `companion/repo_orientation/` | Find a contradiction between product documentation and implementation |
| `companion/feedback_instrument/` | Inspect a synthetic labelled-feedback dataset and edge cases |
| `companion/figures/` | Print, reuse, or inspect every book diagram as PDF, PNG, and SVG files |

## Run every no-key check

Requirements:

- Python 3.11 or later
- SQLite 3.40 or later
- A POSIX-compatible shell

From the repository root:

```sh
./scripts/validate_companion.sh
```

No model API key, cloud account, production credential, package installation, or customer data is required. The Python validators use only the standard library.

## Workbook paths

Choose one mode:

1. **Quick path:** Chapters 1, 8, 13, 15, and 20.
2. **Chapter path:** complete the mapped worksheet after each chapter.
3. **Capstone path:** carry one evidence-backed claim through prototype, implementation, review, release, and learning.

The PDF is designed for printing and handwriting. The Markdown source and individual templates support digital editing and team adaptation.

## Data boundary

All named companies and people in runnable fixtures are fictional, and all feedback reviews are synthetic. The repository contains no Heatseeker customer data, Meta creative, Tokopedia review text, Qlip material, Shipper operational data, employer code, or GoPractice content.

## About the title

`pm-mts` is the short companion-repository name for *PM Is Now Another Member of Technical Staff*.

Copyright © 2026 Razii Abraham. All rights reserved.
