# Getting Started with the PM MTS Companion

You do not need to be a developer to use this repository. The exercises are designed so that an AI coding agent can inspect the local files, explain unfamiliar terms, and run bounded checks while you remain responsible for the product interpretation.

## Choose a path

- **Agent-guided path:** clone the repository, open it in a local AI coding agent, and work through the chapter exercises. This is the recommended path.
- **Manual path:** clone or download the repository and copy the commands in this guide yourself.
- **Workbook-only path:** open [`PM-MTS-Workbook.pdf`](PM-MTS-Workbook.pdf) and complete the records without running code.

## Step 1: get a local copy

### Terminal method

Open Terminal on macOS/Linux or Git Bash/PowerShell on Windows:

```sh
git clone https://github.com/raziiabraham/pm-mts.git
cd pm-mts
```

The first command downloads a local copy. The second moves the terminal into that folder so later commands can find the companion files.

### GitHub Desktop method

1. Open GitHub Desktop.
2. Choose **File → Clone repository**.
3. Select the URL tab and enter `https://github.com/raziiabraham/pm-mts.git`.
4. Choose where to save it.
5. Open that local folder in your coding agent.

### Download-only method

On GitHub, choose **Code → Download ZIP**, unzip the file, and open the resulting `pm-mts` folder. This is enough for reading and running exercises, although cloning is better if you want future updates.

## Step 2: ask your coding agent to orient itself

Use this reusable prompt, replacing the chapter number and folder when needed:

> I am reading Chapter 2. Read `README.md`, `AGENTS.md`, and `companion/api/README.md`. Do not edit files yet. Explain the exercise and every unfamiliar term in plain language. Show me which files to inspect, run the validator, and explain what the result proves and does not prove.

The agent should work from the repository root—the folder containing `README.md`, `AGENTS.md`, `companion/`, and `scripts/`.

## Step 3: Chapter 2 example—run your first Python check

Chapter 2 uses a fictional API contract. The files show one request and three possible outcomes:

1. `companion/api/request.json` — what the product sends;
2. `companion/api/success.json` — a successful response;
3. `companion/api/validation_error.json` — input the service rejects; and
4. `companion/api/provider_error.json` — an upstream service failure.

The validator reads those files and checks whether they preserve the states and safety boundaries described in the chapter. It does not contact an API or change the files.

### macOS or Linux

From the `pm-mts` folder, run:

```sh
python3 companion/api/validate_contract.py
```

### Windows

From PowerShell or Windows Terminal, run:

```powershell
py companion\api\validate_contract.py
```

If `python3` works on your Windows installation, you may use the macOS/Linux form with forward slashes instead.

Expected output:

```text
Chapter 2 API contract validation passed.
```

In plain language, “passed” means the supplied JSON examples contain the expected correlation ID, allowed states, validation details, retry rules, and failure boundaries. It does not prove that a real production API behaves correctly.

## Chapter-by-chapter runnable checks

Run only the exercise for the chapter you are reading. Your coding agent can run the command and then explain the output.

| Chapter | Command on macOS/Linux | What it checks |
| --- | --- | --- |
| 2 | `python3 companion/api/validate_contract.py` | Request, success, validation-error, and provider-error states |
| 5 | `./companion/sql/validate_chapter_05.sh` | Representative SQL output against deterministic data |
| 6 | `python3 companion/analytics/validate_tracking.py` | Event names, triggers, required properties, ownership, and invalid cases |
| 13 | `python3 companion/ai_evaluation/evaluate.py` | Two resolver versions, held-out cases, critical errors, and release gates |
| 14 | `python3 companion/calibration/validate_record.py` | Whether a calibration record stays connected to its preserved failure and outputs |
| 16 | `python3 companion/repo_orientation/validate_task.py` | Whether the documented 5 MB limit conflicts with the implemented 3 MB limit |
| 19 | `python3 companion/feedback_instrument/validate_dataset.py` | Synthetic review IDs, labels, splits, and required edge cases |

On Windows, replace `python3` with `py` and `/` with `\`. The Chapter 5 shell exercise is easiest through Git Bash or Windows Subsystem for Linux.

To run every supported check on macOS/Linux or Git Bash:

```sh
./scripts/validate_companion.sh
```

## A useful learning loop

For each exercise:

1. Ask the agent to explain the product question before inspecting code.
2. Read the small input files yourself.
3. Predict what the validator should accept or reject.
4. Run the validator.
5. Ask what the result proves and what remains unknown.
6. If you want to experiment, create a Git branch or copy the file before changing it.
7. Complete the related workbook record using your own bounded product problem.

## Troubleshooting

### “python3: command not found”

Ask your coding agent to check whether Python is installed. On Windows, try `py --version`. On macOS/Linux, try `python3 --version`. The exercises require Python 3.11 or later.

### “No such file or directory”

Your terminal is probably outside the repository root. Run `pwd` on macOS/Linux or `Get-Location` in PowerShell, then navigate to the cloned `pm-mts` folder.

### “Permission denied” for a `.sh` file

Run it through the shell explicitly:

```sh
sh scripts/validate_companion.sh
```

### The validator fails after I edited a file

That is often the point of the exercise. Ask the agent to show the diff, explain which expectation changed, and help you decide whether the fixture, validator, or your edit is wrong. Do not simply change the expected answer to make the check green.

## Safety and data boundary

These exercises use fictional or synthetic data and do not require network access. Do not paste employer code, credentials, customer data, or confidential artifacts into this repository or an AI tool. Follow your organisation's policies when adapting a template to real work.
