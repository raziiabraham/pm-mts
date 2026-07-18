# Companion Map

This is the routing table used by the AI guide. You do not need to navigate it during a session: invoke `$pm-mts-guide Chapter N`, `/pm-mts N`, or say “Guide me through Chapter N.” The agent selects one row, renders the relevant artifact in chat, runs safe evidence, and guides the application.

## The five-chapter quick path

| Chapter | Product question | Agent route | Executed evidence |
| --- | --- | --- | --- |
| 1 | How close should I work to this product’s technical behavior? | [Chapter 1 guide](companion/chapters/01.md) | None |
| 8 | Which actors, states, handoffs, and failures are still ambiguous? | [Chapter 8 guide](companion/chapters/08.md) | None |
| 13 | What does “good” mean for this AI capability, and what blocks release? | [Chapter 13 guide](companion/chapters/13.md) | Optional evaluation check |
| 16 | What context does an agent or teammate need to do bounded work? | [Chapter 16 guide](companion/chapters/16.md) | None |
| 20 | What evidence makes this change ready—or not ready—to ship? | [Chapter 20 guide](companion/chapters/20.md) | None |

Add Chapter 15 when the product itself contains an agentic capability.

## All chapters

| Chapter | Exercise | Agent route and source contract | Evidence path |
| --- | --- | --- | --- |
| 1 | Map your technical floor | [Chapter 1 guide](companion/chapters/01.md) | Reflection |
| 2 | Turn a user story into an API conversation | [Chapter 2 guide](companion/chapters/02.md) | Optional contract check |
| 3 | Turn a feature idea into a release path | [Chapter 3 guide](companion/chapters/03.md) | Team review |
| 4 | Rewrite and hand off an image requirement | [Chapter 4 guide](companion/chapters/04.md) | Specialist review |
| 5 | Turn a product question into SQL thinking | [Chapter 5 guide](companion/chapters/05.md) | Optional SQLite run |
| 6 | Write a tracking plan | [Chapter 6 guide](companion/chapters/06.md) | Optional event check |
| 7 | Design an experiment before results exist | [Chapter 7 guide](companion/chapters/07.md) | Interpretation lab |
| 8 | Expose ambiguity in a flow | [Chapter 8 guide](companion/chapters/08.md) | Team review |
| 9 | Audit one screen and reusable component | [Chapter 9 guide](companion/chapters/09.md) | Design and implementation review |
| 10 | Diagnose one target behavior twice | [Chapter 10 guide](companion/chapters/10.md) | Evidence plan |
| 11 | Map the problem shape | [Chapter 11 guide](companion/chapters/11.md) | Evidence review |
| 12 | Compare solution shapes | [Chapter 12 guide](companion/chapters/12.md) | Cross-functional review |
| 13 | Design an AI evaluation system | [Chapter 13 guide](companion/chapters/13.md) | Optional version comparison |
| 14 | Design a calibration loop | [Chapter 14 guide](companion/chapters/14.md) | Optional record check |
| 15 | Write an agent charter | [Chapter 15 guide](companion/chapters/15.md) | Risk and specialist review |
| 16 | Create a portable context brief | [Chapter 16 guide](companion/chapters/16.md) | Product and technical verification |
| 17 | Build a repository orientation map | [Chapter 17 guide](companion/chapters/17.md) | Optional public-repo check |
| 18 | Create an assumption and evidence map | [Chapter 18 guide](companion/chapters/18.md) | Evidence review |
| 19 | Write a prototype contract | [Chapter 19 guide](companion/chapters/19.md) | Optional dataset check |
| 20 | Take one slice through delivery | [Chapter 20 guide](companion/chapters/20.md) | Delivery evidence |
| Optional lab | Turn app reviews into a product instrument | [App-review lab](companion/feedback_instrument/README.md), [Product Instrument Design](companion/templates/product_instrument_design.md), and [Productionization Memo](companion/templates/productionization_memo.md) | Optional dataset check |

## How the agent uses one row

1. State the product question in plain language.
2. Read the linked sources silently and render the first useful object in chat.
3. Ask the reader to predict or judge one behavior.
4. Run the narrow safe check itself when one exists and show the salient result.
5. Explain what the evidence proves and what it cannot prove.
6. Interview the reader through the related record one question at a time, with feedback.
7. Challenge one assumption and finish with the draft, evidence boundary, and next action.

For prompt and interaction patterns, see [AI_GUIDE.md](AI_GUIDE.md).
