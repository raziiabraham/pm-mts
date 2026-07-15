#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ALLOWED_SPLITS = {"development", "test"}
ALLOWED_SENTIMENTS = {"positive", "neutral", "negative"}


def load_jsonl(name):
    rows = []
    with (ROOT / name).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise SystemExit(f"{name}:{line_number}: invalid JSON: {error}")
    return rows


reviews = load_jsonl("reviews.jsonl")
labels = load_jsonl("labels.jsonl")
review_ids = [row["review_id"] for row in reviews]
label_ids = [row["review_id"] for row in labels]

assert len(reviews) == 17, "expected 17 synthetic reviews"
assert len(review_ids) == len(set(review_ids)), "duplicate review_id in reviews"
assert len(label_ids) == len(set(label_ids)), "duplicate review_id in labels"
assert set(review_ids) == set(label_ids), "reviews and labels must have identical IDs"
assert {row["split"] for row in reviews} == ALLOWED_SPLITS, "both splits are required"
assert all(row["text"].strip() for row in reviews), "review text must not be blank"

for row in labels:
    topics = row["expected_topics"]
    categories = row["expected_categories"]
    sentiments = row["expected_sentiments"]
    assert len(topics) == len(categories) == len(sentiments), f"unaligned labels: {row['review_id']}"
    assert all(value in ALLOWED_SENTIMENTS for value in sentiments), f"unknown sentiment: {row['review_id']}"
    assert row["expected_abstain"] == (len(topics) == 0), f"abstention mismatch: {row['review_id']}"

assert any(row["expected_abstain"] for row in labels), "need abstention examples"
assert any(row["needs_review"] for row in labels), "need human-review examples"
assert any(row["escalate"] for row in labels), "need escalation examples"
assert any(len(row["expected_topics"]) > 1 for row in labels), "need multi-topic examples"
assert ALLOWED_SENTIMENTS.issubset({value for row in labels for value in row["expected_sentiments"]}), "need all sentiment labels"

print("HarborCart dataset validation passed: 17 reviews, aligned labels, required edge cases present.")
