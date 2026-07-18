# Guidance for AI Coding Agents

This repository is the educational companion to *PM Is Now Another Member of Technical Staff*. The reader may be new to terminals, Git, Python, SQL, APIs, repositories, or coding agents.

Your job is to help the reader understand and apply a product concept. Running code is optional verification, not the default experience.

## Orient before acting

1. Read `README.md`, `AI_GUIDE.md`, and the relevant row in `COMPANION_MAP.md`.
2. Identify the chapter, the reader’s product question, and whether they want to browse, complete a worksheet, or experiment.
3. Open only the bounded files linked from that row. Do not scan the entire repository unless the reader asks for a broader audit.
4. Start with the human-readable artifact. Never lead with Python, installation, or a validation command.

## First-response contract

For a guided exercise, your first response should contain:

1. **Product question:** one sentence describing what the exercise helps decide.
2. **Artifact:** the first file to inspect and why it matters.
3. **Inspection order:** no more than four files.
4. **Reader prediction:** one question the reader should answer before seeing the supplied result.
5. **Optional verification:** name the command only after explaining what it would and would not prove.

Explain unfamiliar terms in plain language. Keep the reader responsible for interpretation and decisions.

## Artifact-first routes

- **Chapter 2 / API:** begin with `companion/api/README.md`. Show the explicit fictional host, HTTP method, path, request, success response, validation response, and provider-failure response. Help the reader derive interface states before offering `validate_contract.py`.
- **Chapter 5 / SQL:** begin with the exact query embedded in `companion/sql/sakila/README.md`, then inspect `queries/film_demand_per_copy.sql`. Explain the question, grain, denominator, join path, result, and limitation before offering SQLite commands.
- **Chapter 6 / analytics:** begin with the product decision and `tracking_plan.json`, then compare valid and invalid event envelopes before offering the validator.
- **Chapter 13 / AI evaluation:** begin with one held-out case, the rubric, and both outputs. Ask for a pass/fail/abstain prediction before offering the evaluator.
- **Chapter 14 / calibration:** begin with the preserved failure and version chain in `filled_record.json`, not the validator.
- **Chapter 17 / repository orientation:** begin with the product question and inspection map. Treat repository evidence as implementation evidence, not complete product truth.
- **Optional feedback lab:** begin with the decision, synthetic reviews, and label boundary before offering the dataset check.
- **Workbook chapters:** interview the reader one section at a time. Do not silently fill blank fields or invent facts.

## Running and editing

1. Work from the repository root and show the exact command before execution.
2. Run the narrow exercise check before the complete suite.
3. Translate a pass or failure into product meaning and its evidence boundary. A green check proves only the named deterministic assertions.
4. Do not edit fixtures, validators, templates, expected outputs, or upstream data unless the reader explicitly asks to experiment.
5. For experiments, suggest a Git branch or copied file first, ask the reader to predict the result, make one bounded change, and show the diff afterward.
6. Do not “fix” an expected result merely to make a check pass. Determine whether the artifact, expectation, or experiment changed.

## Safety boundary

- Do not add dependencies, contact external services, use network access, or request an API key for the supplied no-key path.
- Never introduce employer code, credentials, customer data, or confidential artifacts.
- State when specialist review, access, or organisation policy is required.
- Do not imply that completing an exercise transfers engineering, design, data, security, legal, or operational ownership to the reader.
