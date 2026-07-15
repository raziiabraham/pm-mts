# Chapter 6: tracking-plan fixture

`tracking_plan.json` connects three fictional onboarding events to product questions and decisions. `event_cases.jsonl` contains valid and invalid envelopes.

Run:

```sh
python3 companion/analytics/validate_tracking.py
```

The point is not to memorize event syntax. It is to verify that an event has a stable trigger, required properties, ownership, and a decision it can inform—and to reject instrumentation that cannot support its claimed meaning.
