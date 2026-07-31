# Chapter 13: Compare Two AI Feature Versions

This deterministic lab models the entity-resolution gate described in Chapter 13. Every company and page is fictional.

Product question:

> Which resolver version, if either, is safe enough to release against the defined cases and critical-failure gate?

Files:

- `dataset.jsonl`: five held-out cases, candidate pages, labelled behavior, and severity;
- `outputs_v1.jsonl`: a name-led resolver that forces answers;
- `outputs_v2.jsonl`: a context-aware resolver that can abstain;
- `rubric.json`: observable hard and semantic criteria; and
- `expected_comparison.json`: the release decision this fixture should reproduce.

## Read before running

Open one row from [`dataset.jsonl`](dataset.jsonl), find the same case in both output files, and use [`rubric.json`](rubric.json) to predict whether each version should pass, fail, or abstain.

The supplied comparison is:

| Version | Cases passed | Critical failures | Release decision |
| --- | ---: | ---: | --- |
| v1 | 2 of 5 | 2 | Do not release |
| v2 | 5 of 5 | 0 | Release against this bounded gate |

The important distinction is not merely the average. Version 1 forces answers in cases where a wrong entity or forced match creates a critical product error. Version 2 earns the bounded release decision partly by knowing when to abstain.

Use the [AI Evaluation Scorecard](../templates/ai_evaluation_scorecard.md) to define tasks, severity, rubric levels, ownership, and release gates for another capability.

## Optional verification

Run:

```sh
python3 companion/ai_evaluation/evaluate.py
```

The script checks schema and candidate integrity, scores exact expected behavior, applies the critical-case gate, and confirms the expected comparison. It does not call a model or prove that either version generalizes beyond the five constructed cases.

If you experiment, predict the release impact before changing one output, then rerun the evaluator and inspect the diff.
