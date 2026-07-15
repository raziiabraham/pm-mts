# Chapter 16: toy repo-orientation task

You are orienting to a fictional Noted cover-image feature.

Product question:

> What happens when a user adds a cover image, and which upload limit should the interface communicate?

Inspect the files under `toy_repo/`, then write down:

1. files inspected;
2. verified product behavior;
3. one contradiction;
4. one question the repository cannot answer; and
5. the decision that should follow.

Compare your result with `expected_orientation.json`. Run:

```sh
python3 companion/repo_orientation/validate_task.py
```

The script proves that the contradiction is present. It does not decide which limit is correct; the absence of that rationale is the product finding.
