# HarborCart Feedback Instrument Lab

This is an original Chapter 19 companion. HarborCart is fictional. Every review and label is synthetic; no customer, app-store, employer, or course dataset is reproduced.

## Files

- `reviews.jsonl`: 17 synthetic mobile-app reviews.
- `labels.jsonl`: expected topics, categories, sentiment, abstention, review, and escalation behavior.
- `validate_dataset.py`: checks identifiers, splits, aligned labels, and edge-case coverage.

## Exercise

1. Define the recurring product decision and out-of-scope complaints.
2. Develop an extraction prompt on the `development` split.
3. Compare output with the labelled expectations.
4. Change one prompt or taxonomy rule at a time.
5. Evaluate the selected version on the held-out `test` split.
6. Report relevance, coverage, redundancy, sentiment, abstention, category mapping, escalation, and review demand separately.
7. Write a stop, improve, productionize, or pivot decision.

The labels are teaching expectations, not universal truth. Readers may challenge one by recording the reason; they should not tune the prompt on the held-out split and still call it unseen evaluation.

## Validate

```sh
python3 companion/feedback_instrument/validate_dataset.py
```

No API key, production credential, or paid service is required. The rows can be evaluated manually or with a provider selected under the reader's own data and security policy.
