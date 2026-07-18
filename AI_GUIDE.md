# Use the Companion as an AI-Guided Practice Session

You have already read the book. This repository should now behave less like another book and more like a patient technical product coach.

Open or attach the repository in an AI coding agent, then say:

> Guide me through Chapter 2.

Repository-native shortcuts are also included:

- **Codex skill:** `$pm-mts-guide Chapter 2`
- **Claude Code command:** `/pm-mts 2`

Add a mode and context when useful: `$pm-mts-guide apply Chapter 8 to checkout recovery` or `/pm-mts 13 demonstrate`.

That is enough. The repository tells the agent to bring the example into the conversation, run safe local checks for you, explain the results, and interview you through the related product record. Add a goal when you have one:

> Guide me through Chapter 5. I want to decide whether our “most popular” report is misleading.

## What the agent should do—not ask you to do

| Old companion behavior | AI-first behavior |
| --- | --- |
| “Open `request.json`.” | Reconstruct the request in chat, annotate it, and cite the source afterward. |
| “Run this command.” | Run the safe no-key check, display the useful output, and explain what it proves. |
| “Fill in this worksheet.” | Ask one question at a time, give feedback, and maintain the draft in chat. |
| “Read these five files.” | Read the bounded sources silently and synthesize the relevant teaching object. |
| “Here is the right answer.” | Ask for a prediction, compare it with evidence, and challenge one assumption. |
| “The check passed.” | Translate the pass into product meaning and state the evidence boundary. |

If an agent falls back to file navigation or terminal homework, say:

> Keep the conversation as the interface. Render the artifact here, run safe repository checks yourself, and ask me only for product judgment or context you cannot infer.

## Three session modes

### Demonstrate the book example

Use this when you want the book’s abstract idea to become concrete.

> Demonstrate Chapter 13. Show one evaluation case at a time, ask for my release judgment, run the supplied evaluator, and walk me through the result.

The agent should render the cases and outputs, not send you away to JSONL files.

### Apply it to my product

Use this when you want a completed decision artifact rather than a blank worksheet.

> Apply Chapter 8 to our checkout recovery flow. Interview me one question at a time, challenge missing states, and build the Flow-to-Acceptance Record in this chat.

The agent should keep facts, interpretations, unknowns, and specialist questions separate. It should give feedback after each meaningful answer and render the completed draft at the end.

### Run a bounded experiment

Use this after you understand the supplied example.

> Experiment with Chapter 2. Help me predict what breaks if `request_id` is missing, make the change in a temporary copy, run the narrow check, show the diff and output, then restore the original state.

The agent should make one reversible change at a time. It should ask before installing anything, using credentials, contacting an external service, editing shared state, or performing a destructive action.

## Ready-to-use chapter prompts

### Chapter 2: API contract

> Guide me through Chapter 2 in demonstrate mode. Reconstruct the fictional host, method, path, request, and three response states directly in chat. Ask me what the interface should do for one state. Run the supplied contract validator yourself, show the salient output, and explain what the result does and does not prove. Then offer to interview me through an API State Worksheet for one action in my product.

### Chapter 5: SQL

> Guide me through Chapter 5 in demonstrate mode. Render the exact product query and a compact result table here. Explain grain, numerator, denominator, joins, filters, ordering, and limitation in plain language. Run the bounded SQLite exercise yourself and walk me through its output. Then ask for one product question I want to translate into query logic.

### Chapter 6: analytics

> Guide me through Chapter 6. Render one valid and one invalid event in chat, ask me to predict which is usable, run the tracking validator, and connect every failure to a product or measurement consequence. Then interview me through a tracking plan one decision at a time.

### Chapter 13: AI evaluation

> Guide me through Chapter 13. Render one held-out case and both candidate outputs at a time. Ask whether each version should pass, fail, or abstain. Run the evaluator yourself, explain why the release gate differs from an average score, and help me draft a scorecard for my capability.

### Any workbook chapter

> Apply Chapter [NUMBER] to [BOUNDED PRODUCT SITUATION]. Treat the workbook template as your internal schema. Ask one high-leverage question at a time, reflect my answer, give specific feedback, and update the draft in chat. Keep facts, interpretations, decisions, unknowns, and specialist questions separate. Before finalising, challenge one assumption. End with the complete record, unresolved questions, evidence boundary, reviewers, and next action.

## The learning loop

Every useful session follows the same compact loop:

1. **See:** the agent renders a real teaching object in chat.
2. **Predict:** you make a product judgment before the result is explained.
3. **Verify:** the agent runs a safe check or compares preserved evidence.
4. **Interpret:** you distinguish what the evidence proves from what remains unknown.
5. **Apply:** the agent interviews you and drafts the relevant record.
6. **Challenge:** together you test one counterexample or failure state.
7. **Transfer:** you leave with one decision, artifact, and next action.

## More AI-first techniques built into the repo

- **Adaptive routing:** the agent chooses demonstrate, apply, or experiment based on your goal instead of making you navigate a syllabus.
- **Progressive disclosure:** it shows one request, case, flow state, or worksheet section at a time rather than dumping every source file.
- **Prediction before reveal:** you practise judgment instead of passively accepting the supplied answer.
- **Executable evidence:** safe deterministic checks become live evidence receipts in the conversation, with their limitations attached.
- **Counterexample coaching:** the agent pressure-tests the draft with a failure case, rival explanation, or disconfirming question.
- **Teach-back:** you explain the product meaning in your own words so the agent can correct reasoning, not just terminology.
- **Evidence ledger:** facts, interpretations, unknowns, decisions, and specialist-owned questions stay visibly separate as the session evolves.
- **Artifact synthesis:** the agent produces the completed record in chat; writing a file is optional, not the definition of completion.
- **Session checkpoints:** long exercises end each stage with what changed, what remains uncertain, and where to resume.
- **Fictional fallback:** when you cannot share work context, the agent can demonstrate with supplied synthetic fixtures without pressuring you to expose confidential material.

## What a complete session should leave behind

You should finish with a decision or learning question, a rendered example, a prediction you made, executed evidence where available, a completed or advanced product record, specific feedback, one challenged assumption, an evidence boundary, and a next action.

Never paste employer code, credentials, customer data, or confidential artifacts into this repository or an AI tool. Use fictional or approved data and follow your organisation’s policies.
