# Getting Started with the AI-Guided Companion

The shortest path is a conversation, not a setup checklist.

## 1. Give an AI coding agent the repository

Open the `pm-mts` repository with an agent that can read files and use a terminal. If it is not already local, give the agent this URL and ask it to obtain or open the repository:

`https://github.com/raziiabraham/pm-mts`

Use the agent’s GitHub, repository, or open-folder flow when available. You do not need to learn Git before starting the lesson.

## 2. Ask for a chapter

> Guide me through Chapter 2.

You can also invoke the bundled entry point directly:

- **Codex:** `$pm-mts-guide Chapter 2`
- **Claude Code:** `/pm-mts 2`

The agent reads the repository instructions automatically. It should render the relevant artifact in chat, ask for a prediction or decision, run safe local checks itself, interpret the output, and offer to guide you through the related workbook record.

Useful variations:

- “Demonstrate Chapter 5 and walk me through the live SQL result.”
- “Apply Chapter 8 to our checkout recovery flow.”
- “Experiment with Chapter 13 by changing one output in a temporary copy.”
- “I am not sure where to start. Ask me one question and recommend a chapter.”

## 3. Keep the conversation as the interface

If the agent only gives you file paths or commands, say:

> Render the artifact here, run safe repository checks yourself, show me the salient output, and interview me one question at a time.

A good session should not require you to switch repeatedly between chat, files, a terminal, and a blank worksheet.

## 4. Bring a bounded product situation—or use the fictional example

For application mode, share only the context needed to make the decision. The agent will ask one question at a time, reflect your answer, give feedback, and maintain the draft in chat.

Do not paste employer code, credentials, customer data, or confidential material. If real context cannot be shared, ask the agent to continue with the repository’s fictional or synthetic example.

## What the agent may run automatically

The repository includes safe, local, no-key checks for the API contract, Sakila SQL, analytics events, AI evaluation, calibration record, and synthetic feedback dataset. The agent can run the narrow relevant check and show its output as an execution receipt.

It should ask before installing dependencies, using credentials, contacting external services, changing shared or production state, or making a destructive edit.

## Manual fallback

If your agent cannot obtain the repository, clone it yourself:

```sh
git clone https://github.com/raziiabraham/pm-mts.git
cd pm-mts
```

You can also use **GitHub Desktop → File → Clone repository**, or **Code → Download ZIP** on GitHub. Open the complete `pm-mts` folder in the agent, not an individual file.

If you intentionally want to reproduce every self-contained check by hand:

```sh
./scripts/validate_companion.sh
```

On Windows, use `py` instead of `python3`; the Chapter 5 shell exercise is easiest in Git Bash or Windows Subsystem for Linux. Python 3.11+ and SQLite 3.40+ are needed only for execution, not for chat-rendered walkthroughs.

## Troubleshooting

### The agent tells me to open files

Ask it to follow `AGENTS.md` and keep the conversation as the interface. File links are provenance, not the default teaching step.

### The agent tells me to run a command

Ask it to run the narrow safe check itself. If it lacks terminal access, it should explain that limitation and use the preserved expected result, clearly labelled as supplied rather than executed.

### The agent dumps the entire workbook

Ask for progressive interview mode: one high-leverage question, brief feedback, and one updated section at a time.

### A check fails after an experiment

That may be the useful result. Ask the agent to show the diff, explain which assertion changed, and distinguish a fixture mismatch from a product insight. Do not rewrite the expected result merely to make the check green.

## Where the sources live

The [Companion Map](COMPANION_MAP.md) routes all 20 chapters. [AI_GUIDE.md](AI_GUIDE.md) contains ready-to-use prompts and the complete interaction model. The [chapter guides](companion/chapters/README.md) define the bounded sources, interview output, and evidence boundary for each session.
