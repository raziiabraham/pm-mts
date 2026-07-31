# Chapter 14: Follow a Failure Through Calibration

Product question:

> Does the proposed change address the preserved failure without losing the evidence, regression boundary, or release decision behind it?

Start with [`filled_record.json`](filled_record.json). It carries the constructed `domain` failure from Chapter 13 through diagnosis, a bounded resolver change, regression comparison, release decision, and remaining limits.

Before running anything, identify the observed failure, earliest plausible failing layer, smallest credible change, regression cases, and evidence that would trigger reversion. Then use the [Prompt Evaluation Table](../templates/prompt_evaluation_table.md) and [AI Calibration Record](../templates/ai_calibration_record.md) for your own bounded case.

## Optional verification

Run:

```sh
python3 companion/calibration/validate_record.py
```

The validator cross-checks the record against the Chapter 13 dataset and supplied version outputs. This prevents the teaching narrative from drifting away from its preserved case; it does not prove that the proposed change is safe in production.
