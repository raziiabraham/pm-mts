---
name: pm-mts
description: Turn a PM MTS book chapter into an interactive, chat-native practice session. Use when a reader asks to guide, demonstrate, apply, practise, or experiment with a chapter or workbook technique.
argument-hint: "[chapter] [demonstrate|apply|experiment] [optional product context]"
---

# Guide a PM MTS practice session

The reader invoked `/pm-mts $ARGUMENTS`.

Read `AGENTS.md`, `COMPANION_MAP.md`, and the matching `companion/chapters/NN.md` guide. Interpret the first chapter number in the arguments. Infer **demonstrate**, **apply**, or **experiment** from the remaining text. If no chapter is present, ask one short question about the product decision or skill the reader wants to practise, then recommend one chapter.

Keep the conversation as the interface:

1. Render the relevant artifact directly in chat; do not tell the reader to open files.
2. Ask one prediction or product-judgment question at a time.
3. Run safe, local, no-key repository checks yourself and show the salient output.
4. Interview through workbook schemas progressively and give specific feedback.
5. Separate facts, interpretations, decisions, unknowns, and specialist-owned questions.
6. Challenge one assumption before finalising.
7. End with the completed or advanced artifact, evidence boundary, unresolved questions, reviewers, and next action.

Follow every safety and evidence rule in `AGENTS.md`. Ask before installing dependencies, using credentials, contacting external services, changing shared state, or making destructive edits.
