# Chapter 6: Read a Tracking Plan as a Product Contract

Product question:

> Can these events support the product decision they claim to inform, or do they merely record activity?

Start with [`tracking_plan.json`](tracking_plan.json). It connects three fictional onboarding events to product questions, decisions, triggers, required properties, and ownership. Then inspect [`event_cases.jsonl`](event_cases.jsonl) and predict which envelopes should be accepted or rejected.

The point is not to memorize event syntax. It is to verify that an event has a stable trigger, required properties, ownership, and a decision it can inform—and to reject instrumentation that cannot support its claimed meaning.

Use the [Tracking Plan worksheet](../templates/tracking_plan.md) to apply the method to one real product decision.

## Optional verification

After making your predictions, run:

Run:

```sh
python3 companion/analytics/validate_tracking.py
```

The check proves only that the supplied event cases match the fixture’s declared contract. It does not prove that production instrumentation fires correctly or supports a causal claim.
