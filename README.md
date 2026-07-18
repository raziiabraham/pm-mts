# PM MTS Companion

The AI-guided practice companion to *PM Is Now Another Member of Technical Staff* by Razii Abraham.

You have done the reading. Now let the repository respond.

Open or attach this repository in an AI coding agent and say:

> Guide me through Chapter 2.

Or use the repository-native invocation for your agent:

- **Codex:** `$pm-mts-guide Chapter 2`
- **Claude Code:** `/pm-mts 2`

The agent should reconstruct the API request and responses in the conversation, ask for your product judgment, run the safe contract check itself, explain the output, then interview you through an API State Worksheet. You should not have to hunt through files, copy terminal commands, or fill in a blank workbook alone.

For another chapter, change the number. For your own product, add one sentence of context:

> Apply Chapter 8 to our checkout recovery flow. Interview me one question at a time and challenge missing states.

See [AI_GUIDE.md](AI_GUIDE.md) for demonstration, application, and experiment prompts, including compact command examples.

## What happens in an AI-guided session

1. **The example appears in chat.** The agent reads bounded repository sources and renders the relevant request, query, event, flow, evaluation case, or decision table.
2. **You make a prediction or judgment.** The agent asks one useful question before explaining the supplied result.
3. **The agent runs safe checks.** When a no-key fixture exists, the agent executes it, shows the salient output, and explains what it proves.
4. **You apply the technique.** The agent interviews you one question at a time, gives specific feedback, and maintains the workbook record in the conversation.
5. **The result gets challenged.** The agent tests one failure state, counterexample, or unsupported assumption.
6. **You leave with an artifact.** The completed draft, unresolved questions, evidence boundary, reviewers, and next action are rendered in chat. Saving a file is optional.

Repository files remain available for provenance, deeper inspection, reproducible evidence, and reuse. They are not the default user interface.

## Choose a practice session

| I want to practise… | Say this | What the agent brings into chat |
| --- | --- | --- |
| API product states | “Guide me through Chapter 2.” | Host, method, path, request, responses, UI decisions, and a live contract check |
| SQL product reasoning | “Guide me through Chapter 5.” | Exact query, result table, grain and denominator walkthrough, and a live SQLite run |
| Product analytics | “Guide me through Chapter 6.” | Tracking decision, valid and invalid events, validator output, and a guided tracking plan |
| Experiment judgment | “Guide me through Chapter 7.” | Decision rule, result scenarios, interpretation feedback, and a pre-registration draft |
| AI evaluation | “Guide me through Chapter 13.” | Held-out cases, candidate outputs, release gate, evaluator output, and a scorecard draft |
| AI calibration | “Guide me through Chapter 14.” | Preserved failure, version chain, regression logic, check output, and a calibration record |
| Agent design | “Guide me through Chapter 15.” | Goal, tools, memory, budgets, stops, authority, challenges, and an agent charter |
| Repository orientation | “Guide me through Chapter 17.” | Inspection map, classified findings, contradictions, unknowns, and a bounded check when available |
| Any chapter | “Apply Chapter N to [situation].” | A progressive interview, feedback, completed record, evidence boundary, and next action |

The [Companion Map](COMPANION_MAP.md) covers all 20 chapters. The quick path remains Chapters 1, 8, 13, 16, and 20; add Chapter 15 when the product itself contains an agent. The capstone path begins with one evidence row in Chapter 18 and carries it through prototype and delivery in Chapters 19–20.

## Three modes

- **Demonstrate:** reconstruct a supplied example, execute its bounded evidence, and explain the product meaning.
- **Apply:** interview you and produce the relevant decision artifact in chat.
- **Experiment:** record a prediction, make one reversible change, show the diff, run the narrow check, and compare the result.

If you do not choose, the agent starts with a demonstration and then offers to apply the technique to your product.

## What is included

| Area | Source material and executable evidence |
| --- | --- |
| `companion/chapters/` | Conversation routes for every chapter |
| `companion/templates/` | 26 chapter-aligned schemas used by guided interviews |
| `companion/api/` | A complete fictional API contract and deterministic validator |
| `companion/sql/` | The book’s exact SQL and open-licensed Sakila dataset |
| `companion/analytics/` | Tracking plan, valid and invalid event envelopes, and validator |
| `companion/ai_evaluation/` | Two constructed AI-output versions, held-out cases, rubric, and evaluator |
| `companion/calibration/` | A preserved failure, diagnosis, change, regression evidence, and release chain |
| `companion/repo_orientation/` | A bounded public-repository orientation exercise |
| `companion/feedback_instrument/` | A synthetic labelled-feedback dataset with edge cases |
| `companion/figures/` | Every book diagram as PDF, PNG, and SVG |

## If your agent does not have the repository yet

Give it the repository URL—`https://github.com/raziiabraham/pm-mts`—or use your agent’s GitHub/open-folder flow. Ask the agent to obtain or open the repository for you. Manual clone and download options remain in [GETTING_STARTED.md](GETTING_STARTED.md) as a fallback, not the default lesson.

The supplied path needs no model API key, cloud account, production credential, or customer data. A terminal-capable agent can run the checks with Python 3.11+, SQLite 3.40+, and a POSIX-compatible shell.

## Manual and maintainer verification

If you intentionally want to reproduce every check yourself:

```sh
./scripts/validate_companion.sh
```

This is an evidence and maintenance path, not the reader’s starting point.

## Downloadable materials

- [55-page printable workbook](PM-MTS-Workbook.pdf)
- [All 24 printable book figures](PM-MTS-Printable-Figures.pdf)
- [Editable workbook source](companion/pm_mts_workbook.md)
- [Individual template schemas](companion/templates/)
- [Latest complete companion package](https://github.com/raziiabraham/pm-mts/releases/latest)

## Evidence and data boundary

A green check proves only the named assertions about the supplied teaching fixture. It does not prove that a production API, query, AI feature, or product decision is correct. The reader and relevant specialists remain responsible for interpretation, evidence, permissions, and real-world verification.

Named companies and people in constructed runnable fixtures are fictional, and all feedback reviews are synthetic. Chapter 5 vendors the open-licensed generated Sakila sample data. Chapter 17 intentionally inspects the author’s public Noted repository at a cited commit. This repository contains no employer code, credentials, customer data, or confidential artifacts.

Copyright © 2026 Razii Abraham. All rights reserved.
