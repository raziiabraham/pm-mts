# Companion Map

Use this page when you know the chapter you are reading but do not know which companion file matters. Start with one row only. The companion is designed to support the book, not to become another syllabus.

## The five-chapter quick path

| Chapter | Product question | Start with | Optional check |
| --- | --- | --- | --- |
| 1 | How close should I work to this product’s technical behavior? | [Technical Floor Map](companion/templates/technical_floor_map.md) | None |
| 8 | Which actors, states, handoffs, and failures are still ambiguous? | [Flow-to-Acceptance Record](companion/templates/flow_to_acceptance.md) | None |
| 13 | What does “good” mean for this AI capability, and what blocks release? | [AI evaluation lab](companion/ai_evaluation/README.md) | `python3 companion/ai_evaluation/evaluate.py` |
| 16 | What context does an agent or teammate need to do bounded work? | [Portable Context Brief](companion/templates/context_brief.md) | None |
| 20 | What evidence makes this change ready—or not ready—to ship? | [End-to-End Delivery Slice](companion/templates/delivery_slice_record.md) | None |

Add Chapter 15 when the product itself contains an agentic capability.

## All chapters

| Chapter | Exercise | Start with | Runnable artifact |
| --- | --- | --- | --- |
| 1 | Map your technical floor | [Technical Floor Map](companion/templates/technical_floor_map.md) | — |
| 2 | Turn a user story into an API conversation | [API contract](companion/api/README.md) and [API State Worksheet](companion/templates/api_state_worksheet.md) | Optional contract check |
| 3 | Turn a feature idea into a release path | [Feature Release Path Record](companion/templates/release_path_record.md) | — |
| 4 | Rewrite and hand off an image requirement | [Image Requirement Record](companion/templates/image_requirement_record.md) | — |
| 5 | Turn a product question into SQL thinking | [SQL query and result](companion/sql/sakila/README.md) and [Product Data Question Record](companion/templates/product_data_question.md) | Optional SQLite run |
| 6 | Write a tracking plan | [Tracking-plan fixture](companion/analytics/README.md) and [Tracking Plan](companion/templates/tracking_plan.md) | Optional event check |
| 7 | Design an experiment before results exist | [Experiment interpretation lab](companion/experiments/chapter_07_statistical_interpretation_lab.md) and [Experiment Card](companion/templates/experiment_card.md) | Worksheet |
| 8 | Expose ambiguity in a flow | [Flow-to-Acceptance Record](companion/templates/flow_to_acceptance.md) | — |
| 9 | Audit one screen and reusable component | [Design Audit](companion/templates/design_audit.md) and [Component Contract](companion/templates/component_contract.md) | — |
| 10 | Diagnose one target behavior twice | [Behavior Intervention Card](companion/templates/behavior_intervention_card.md) | — |
| 11 | Map the problem shape | [Evidence Card](companion/templates/evidence_card.md) and [API State Worksheet](companion/templates/api_state_worksheet.md) | — |
| 12 | Compare solution shapes | [AI Solution-Fit Decision Record](companion/templates/ai_solution_fit_decision.md) | — |
| 13 | Design an AI evaluation system | [AI evaluation lab](companion/ai_evaluation/README.md) and [AI Evaluation Scorecard](companion/templates/ai_evaluation_scorecard.md) | Optional version comparison |
| 14 | Design a calibration loop | [Calibration case](companion/calibration/README.md), [Prompt Evaluation Table](companion/templates/prompt_evaluation_table.md), and [AI Calibration Record](companion/templates/ai_calibration_record.md) | Optional record check |
| 15 | Write an agent charter | [Agent Charter](companion/templates/agent_charter.md) | — |
| 16 | Create a portable context brief | [Portable Context Brief](companion/templates/context_brief.md) | — |
| 17 | Build a repository orientation map | [Noted repository exercise](companion/repo_orientation/README.md) and [Repository Orientation Map](companion/templates/repo_orientation_map.md) | Optional public-repo check |
| 18 | Create an assumption and evidence map | [Assumption and Evidence Map](companion/templates/assumption_evidence_map.md) | — |
| 19 | Write a prototype contract | [Prototype Contract](companion/templates/prototype_contract.md) | — |
| 20 | Take one slice through delivery | [Delivery Slice](companion/templates/delivery_slice_record.md), [PR Review Checklist](companion/templates/pr_review_checklist.md), and [Ship Decision Record](companion/templates/ship_decision_record.md) | — |
| Optional lab | Turn app reviews into a product instrument | [App-review lab](companion/feedback_instrument/README.md), [Product Instrument Design](companion/templates/product_instrument_design.md), and [Productionization Memo](companion/templates/productionization_memo.md) | Optional dataset check |

## How to use one row

1. State the product question in your own words.
2. Inspect the linked example or worksheet before running anything.
3. Predict what you expect to find.
4. Use the optional check only when it helps test that prediction.
5. Record what the artifact proves, what it does not prove, and the next decision.
6. Adapt the worksheet to one real, bounded product problem without adding confidential data to this repository or an AI tool.

If you are using an AI coding agent, open [AI_GUIDE.md](AI_GUIDE.md) and choose a prompt for the same chapter.
