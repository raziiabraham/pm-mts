# Getting Started with the PM MTS Companion

You do not need to be a developer, install Python, or run a command to begin. Choose the lightest path that answers your question.

## Path 1: learn directly in your browser

Use this when you want to understand the artifact without local setup.

1. For APIs, open [Chapter 2: Read an API as a Product Contract](companion/api/README.md). It shows the host, HTTP method, path, request, three response states, and corresponding product decisions.
2. For SQL, open [Chapter 5: Read a Product Question in SQL](companion/sql/sakila/README.md). It shows the exact query, syntax explanation, captured result, and interpretation boundary.
3. For any chapter, open the [Chapter Guides](companion/chapters/README.md) and select the number you are reading.
4. For a printable path, open the [55-page workbook](PM-MTS-Workbook.pdf).

The Python and shell files are optional checks behind these examples. They are not prerequisites for reading them.

## Path 2: use an AI coding agent as your guide

Use this when you want the companion to respond to your questions, explain technical terms, or help adapt a worksheet.

### Get a local copy

Clone with a terminal:

```sh
git clone https://github.com/raziiabraham/pm-mts.git
cd pm-mts
```

Or use **GitHub Desktop → File → Clone repository**, enter `raziiabraham/pm-mts`, and choose a local folder. You may also use **Code → Download ZIP** on GitHub and unzip it.

### Open the complete folder

Open the cloned or unzipped `pm-mts` folder—not one individual file—in your AI coding agent. Then paste:

> Read `AGENTS.md`, `AI_GUIDE.md`, `COMPANION_MAP.md`, and the matching two-digit chapter guide—for example, `companion/chapters/02.md` for Chapter 2. I am reading Chapter [NUMBER]. Start with the product question and visible artifact, not a command. Explain the files in the order I should inspect them, ask me to predict the behavior or result, and only then offer an optional check. Do not change files unless I ask to experiment.

See [AI_GUIDE.md](AI_GUIDE.md) for specific API, SQL, AI-evaluation, and worksheet prompts.

## Path 3: reproduce or change an example

Use this after you understand the artifact and want to see how a bounded change affects the result.

| Chapter | Human-readable starting point | Optional command |
| --- | --- | --- |
| 2 | [API host, method, request, and responses](companion/api/README.md) | `python3 companion/api/validate_contract.py` |
| 5 | [Exact SQL, result, and limitation](companion/sql/sakila/README.md) | `./companion/sql/validate_chapter_05.sh` |
| 6 | [Tracking plan and event cases](companion/analytics/README.md) | `python3 companion/analytics/validate_tracking.py` |
| 13 | [Held-out cases, outputs, rubric, and release result](companion/ai_evaluation/README.md) | `python3 companion/ai_evaluation/evaluate.py` |
| 14 | [Preserved failure and calibration record](companion/calibration/README.md) | `python3 companion/calibration/validate_record.py` |
| 17 | [Public-repository inspection question](companion/repo_orientation/README.md) | `python3 companion/repo_orientation/validate_task.py /path/to/noted-main` |
| Optional lab | [Synthetic feedback instrument](companion/feedback_instrument/README.md) | `python3 companion/feedback_instrument/validate_dataset.py` |

On Windows, use `py` instead of `python3`. The Chapter 5 shell exercise is easiest in Git Bash or Windows Subsystem for Linux.

## The learning loop

For any path:

1. State the product question.
2. Inspect the visible artifact.
3. Predict the behavior, output, or failure.
4. Compare the supplied result with your prediction.
5. Run an optional check only if it adds useful evidence.
6. Explain what the result proves and what remains unknown.
7. Complete the related worksheet for one real, bounded problem.

## Run every self-contained check

If you intentionally want to validate the whole repository on macOS, Linux, or Git Bash:

```sh
./scripts/validate_companion.sh
```

The Chapter 17 repository exercise runs only when Noted is cloned beside this repository or supplied through `NOTED_REPO_PATH`.

## Troubleshooting

### “python3: command not found”

You can still use every browser-first and workbook path. Install Python only if you want to run the optional checks. On Windows, try `py --version`.

### “No such file or directory”

Your terminal is probably outside the repository root. Navigate to the folder containing `README.md`, `AGENTS.md`, `companion/`, and `scripts/`.

### A check fails after I edited a file

That may be the useful result. Inspect the diff and decide whether the artifact, expectation, or your experiment changed. Do not merely rewrite the expected answer to make the check green.

## Safety and data boundary

The supplied fixtures use fictional or synthetic data and require no model API key. Chapter 5 uses open-licensed generated Sakila data, and Chapter 17 explicitly inspects the author’s public Noted repository at a cited commit. Do not paste employer code, credentials, customer data, or confidential artifacts into this repository or an AI tool. Follow your organisation’s policies when adapting a template to real work.
