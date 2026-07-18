# Use the Companion with an AI Coding Agent

An AI coding agent should act as a patient guide through the companion—not as a command runner that hides the product reasoning. The repository contains instructions for the agent in `AGENTS.md`; this page gives you prompts and explains what a good session should feel like.

## Recommended first prompt

Open the complete `pm-mts` folder in your coding agent and paste:

> You are my guide for the *PM Is Now Another Member of Technical Staff* companion. Read `AGENTS.md`, `AI_GUIDE.md`, and `COMPANION_MAP.md`. I am reading Chapter [NUMBER], and my goal is [WHAT I WANT TO UNDERSTAND]. Start with the product question and visible artifact—not Python or a terminal command. Explain unfamiliar terms in plain language. Show me no more than four files in the order I should inspect them. Ask me to predict the behavior or result before revealing it. Offer an optional validator only after I understand the artifact, and explain exactly what a pass would and would not prove. Do not edit any file unless I explicitly ask to experiment.

You can use this with Codex, Claude Code, GitHub Copilot coding agent, Cursor, or another agent that can read a local repository. Agent features and file-instruction conventions vary, so explicitly asking it to read the three files above keeps the session portable.

## Prompt: help me choose a path

> Read `COMPANION_MAP.md`. Ask me two short questions: which part of the book I am reading, and whether I want to inspect an example, complete a worksheet, or run an experiment. Recommend one path only. Explain why it fits and open the first artifact. Do not run a command yet.

## Prompt: Chapter 2 API contract

> Guide me through Chapter 2. Read `companion/api/README.md` and its linked request and response examples. First show me the host, HTTP method, path, request body, and three response outcomes. Help me map each outcome to what the user sees, whether retry is safe, what operations can inspect, and what remains under user control. Do not start with the Python validator. Offer it only after I have made my own state map.

## Prompt: Chapter 5 SQL

> Guide me through Chapter 5. Read `companion/sql/sakila/README.md` and `companion/sql/sakila/queries/film_demand_per_copy.sql`. Show me the exact SQL first. Explain the product question, output grain, denominator, joins, filter, ordering, result, and one limitation. Ask me to change one assumption in plain language before proposing SQL. Run SQLite only if I ask to verify the query.

## Prompt: Chapter 13 AI evaluation

> Guide me through Chapter 13. Read `companion/ai_evaluation/README.md`, the five cases, rubric, and expected comparison. Show me one case at a time. Ask whether each version should pass, fail, or abstain before revealing the expected result. Explain why two critical failures block v1 even though it passes some cases. Run the evaluator only after we have discussed the release decision.

## Prompt: adapt a worksheet to my product

> Read the Chapter [NUMBER] row in `COMPANION_MAP.md` and the linked template. Interview me one section at a time. Keep verified facts, interpretations, unknowns, and decisions separate. Do not invent company facts or fill blank fields without asking me. At the end, show the completed draft, unresolved questions, required specialist review, and the next smallest action.

## What a good agent-guided session should produce

By the end, you should be able to explain:

1. the product question;
2. the artifact or evidence you inspected;
3. the result you predicted;
4. what the example or optional check established;
5. what remains unknown or requires a specialist; and
6. which decision or next action follows.

If the agent only runs a script and reports “passed,” ask it to restart from the product question. The check is evidence about the fixture; it is not the learning outcome.

## Safe experimentation

When you want to change a request, response, SQL query, rubric, or output:

1. ask the agent to create a branch or copy the file;
2. state the prediction before the edit;
3. make one bounded change;
4. inspect the diff;
5. run the narrow optional check; and
6. translate the failure or pass into product meaning.

Never paste employer code, credentials, customer data, or confidential artifacts into this repository or an AI tool. Use fictional or approved data and follow your organisation’s policies.
