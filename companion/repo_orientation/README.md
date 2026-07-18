# Chapter 17: inspect a real repository

You are orienting to the author-owned Noted repository at the same commit inspected for Chapter 17:

```sh
git clone https://github.com/avidx-app/noted-main.git
git -C noted-main checkout 985ad957b0131cddd3fd5d16a432150651c90b99
```

Product question:

> What happens when a user adds a cover image, and which upload limit should the interface communicate?

Inspect the repository, then write down:

1. files inspected;
2. verified product behavior;
3. one contradiction;
4. one question the repository cannot answer; and
5. the decision that should follow.

Compare your result with `expected_orientation.json`. Pass the cloned repository path to:

```sh
python3 companion/repo_orientation/validate_task.py /path/to/noted-main
```

The script verifies that the real files still contain the 25 MB product-contract mismatch described in the chapter: product surfaces describe a limit, storage code models a cumulative quota, and the upload client omits the identity the server-side gate needs to enforce it. The script does not decide the intended policy; that unresolved decision is the product finding.
