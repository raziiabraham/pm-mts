# Chapter 6: tracking-plan fixture

`tracking_plan.json` is the tracking plan for Noted's proposed visible publish-review affordance—the feature Chapters 6 and 7 use as a teaching example—connecting seven events to the decision each one supports. `event_cases.jsonl` contains valid and invalid envelopes, including a missing `experiment_variant` that would make the change untestable, a document body smuggled in as a property, and an external-open event carrying an undeclared reader identifier.

Run:

```sh
python3 companion/analytics/validate_tracking.py
```

The point is not to memorize event syntax. It is to verify that an event has a stable trigger, required properties, ownership, and a decision it can inform—and to reject instrumentation that cannot support its claimed meaning.
