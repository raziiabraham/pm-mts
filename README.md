# PM MTS Companion

The public companion to *PM Is Now Another Member of Technical Staff* by Razii Abraham.

Start with a product question—not Python. You can inspect every core teaching artifact directly on GitHub, ask an AI coding agent to guide you, or run the optional checks when you want evidence that the supplied examples still behave as described.

## Choose what you want to understand

| I want to… | Start here | Setup |
| --- | --- | --- |
| Understand an API as a product contract | [See the host, method, request, responses, and UI decisions](companion/api/README.md) | None |
| Understand what a product SQL query actually does | [Read the exact SQL, result, and interpretation boundary](companion/sql/sakila/README.md) | None to read; SQLite to run |
| Compare two AI feature versions | [Inspect the cases, rubric, results, and release decision](companion/ai_evaluation/README.md) | None to read; Python is optional |
| Turn one book chapter into an exercise | [Use the chapter-by-chapter companion map](COMPANION_MAP.md) | None |
| Let an AI coding agent guide me | [Copy a ready-made agent prompt](AI_GUIDE.md) | Clone or download the repository |
| Work without code or a terminal | [Download the 55-page workbook](PM-MTS-Workbook.pdf) | None |

## Three ways to use the companion

### 1. Browse it on GitHub

Open any linked Markdown, JSON, SQL, or worksheet file in your browser. This is enough to learn from the API contract, SQL query, evaluation examples, calibration record, templates, and figures. You do not need Python merely to understand the material.

### 2. Ask an AI coding agent to guide you

Clone or download the repository, open the complete `pm-mts` folder in any coding agent that can read local files, and paste this:

> I am reading Chapter 2 of *PM Is Now Another Member of Technical Staff*. Read `AGENTS.md`, `AI_GUIDE.md`, and `COMPANION_MAP.md`. Start with the visible product artifact, not a command. Explain the product question in plain language, show me the files in the order I should inspect them, ask me to predict the expected behavior, and only then offer to run an optional check. Do not change files unless I ask to experiment.

Change the chapter number to match what you are reading. The agent-specific guide includes ready-made prompts for APIs, SQL, AI evaluation, and choosing a path.

### 3. Run an optional evidence check

The small Python and shell programs are not the lesson. They are deterministic checks behind the lesson: they confirm that the supplied request/response examples, SQL results, event cases, and evaluation decisions remain internally consistent.

If you want to run them, first clone the repository:

```sh
git clone https://github.com/raziiabraham/pm-mts.git
cd pm-mts
```

Then follow the single exercise command shown in its README, or run every self-contained check:

```sh
./scripts/validate_companion.sh
```

The no-key path uses Python 3.11+, SQLite 3.40+, and a POSIX-compatible shell. It needs no model API key, cloud account, package installation, production credential, or customer data.

## What is included

| Area | What readers can inspect or do |
| --- | --- |
| `companion/templates/` | Complete 26 reusable, chapter-aligned product records |
| `companion/api/` | Read a complete fictional API contract: host, method, path, request, success, validation failure, and provider failure |
| `companion/sql/` | Read and optionally run the book’s exact SQL against the open-licensed Sakila dataset |
| `companion/analytics/` | Inspect a tracking plan and valid and invalid event envelopes |
| `companion/ai_evaluation/` | Compare two constructed AI-output versions against held-out cases and a release gate |
| `companion/calibration/` | Trace one preserved failure through diagnosis, change, regression evidence, and release |
| `companion/repo_orientation/` | Inspect the public Noted repository at the cited commit and find a documented-versus-implemented contract mismatch |
| `companion/feedback_instrument/` | Inspect a synthetic labelled-feedback dataset and its edge cases |
| `companion/figures/` | Print, reuse, or inspect every book diagram as PDF, PNG, and SVG files |

## Downloadable materials

- [55-page printable workbook](PM-MTS-Workbook.pdf)
- [All 24 printable book figures](PM-MTS-Printable-Figures.pdf)
- [Editable workbook in Markdown](companion/pm_mts_workbook.md)
- [Individual templates](companion/templates/)
- [Latest complete companion package](https://github.com/raziiabraham/pm-mts/releases/latest)

## Reading paths

1. **Quick path:** Chapters 1, 8, 13, 16, and 20. Add Chapter 15 if the product itself contains an agent.
2. **Chapter path:** use the mapped worksheet after each chapter.
3. **Capstone path:** begin with one evidence row in Chapter 18 and carry it through prototype and delivery in Chapters 19–20.

The [companion map](COMPANION_MAP.md) links every chapter to its relevant worksheet or runnable artifact.

## What a passing check proves

A green check proves only the named assertions about the supplied teaching fixture. It does not prove that a production API, query, AI feature, or product decision is correct. The reader—and the relevant specialists—remain responsible for interpretation, evidence, permissions, and real-world verification.

## Data boundary

Named companies and people in constructed runnable fixtures are fictional, and all feedback reviews are synthetic. Chapter 5 vendors the open-licensed generated Sakila sample data. Chapter 17 intentionally inspects the author’s public Noted repository at a cited commit. This repository contains no employer code, credentials, customer data, or confidential artifacts.

Copyright © 2026 Razii Abraham. All rights reserved.
