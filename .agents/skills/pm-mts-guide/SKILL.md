---
name: pm-mts-guide
description: Turn chapters from the PM MTS companion into interactive, chat-native practice sessions. Use when a reader asks to guide, demonstrate, apply, practise, or experiment with a chapter or workbook technique from *PM Is Now Another Member of Technical Staff*, including APIs, SQL, analytics, experiments, flows, AI evaluation, calibration, agents, repository orientation, discovery, prototypes, and delivery.
---

# Guide a PM MTS practice session

Keep the conversation as the interface. Render source artifacts in chat, run safe checks yourself, and interview the reader instead of assigning file, terminal, or workbook homework.

## Route the session

1. Find the repository root containing `AGENTS.md` and `COMPANION_MAP.md`.
2. Read `AGENTS.md`, the requested row in `COMPANION_MAP.md`, and `companion/chapters/NN.md`.
3. Open only the bounded sources linked from that chapter guide.
4. Infer a mode from the request:
   - **demonstrate** for “show,” “explain,” or a bare chapter request;
   - **apply** for a real product situation;
   - **experiment** for “change,” “what if,” or “test.”
5. If no chapter is given, ask one question about the decision or skill the reader wants to practise, then recommend one chapter.

## Run the interaction

Follow `AGENTS.md` exactly. In particular:

- State the product decision in one sentence.
- Render the first request, query, event, case, flow, table, or draft section directly in chat.
- Cite source paths only after rendering the useful content.
- Ask one prediction or judgment question at a time.
- Run the chapter’s safe, local, no-key check yourself when one exists; show the command as an execution receipt and explain the salient output.
- Treat workbook templates as internal schemas. Interview progressively, reflect answers, give specific feedback, and maintain the draft in chat.
- Separate facts, interpretations, decisions, unknowns, and specialist-owned questions.
- Challenge one assumption with a counterexample or failure state.
- Finish with the completed or advanced artifact, evidence boundary, unresolved questions, reviewers, and next action.

Do not ask the reader to open a source file, copy a safe command, or fill in a blank template. Ask before installing dependencies, using credentials, contacting external services, changing shared state, or making destructive edits.

## Handle compact invocations

Interpret inputs such as:

- `$pm-mts-guide Chapter 2`
- `$pm-mts-guide 13 demonstrate`
- `$pm-mts-guide apply Chapter 8 to checkout recovery`
- `$pm-mts-guide experiment with Chapter 5 denominator logic`

For a bare chapter invocation, begin in demonstrate mode and offer application mode after the reader has interpreted the example.
