# Chapter 13: compare two resolver versions

This deterministic lab models the entity-resolution gate described in Chapter 13. Every company and page is fictional.

Files:

- `dataset.jsonl`: five held-out cases, candidate pages, labelled behavior, and severity;
- `outputs_v1.jsonl`: a name-led resolver that forces answers;
- `outputs_v2.jsonl`: a context-aware resolver that can abstain;
- `rubric.json`: observable hard and semantic criteria; and
- `expected_comparison.json`: the release decision this fixture should reproduce.

Run:

```sh
python3 companion/ai_evaluation/evaluate.py
```

The script checks schema and candidate integrity, scores exact expected behavior, applies the critical-case gate, and confirms the expected two-version comparison. It does not call a model. Readers can change an output and rerun the evaluator to see why aggregate quality must not hide a critical identity error.
