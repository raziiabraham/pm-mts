# Chapter 2: request, response, and failure states

The fictional Briefly service accepts a website URL and returns a public-context draft that a user may edit. Inspect `request.json` and the three response files. For each response, identify what the interface should show, what may be retried, and what must remain under user control.

Run:

```sh
python3 companion/api/validate_contract.py
```

The validator checks the contract's stable correlation ID, allowed states, validation detail, retry policy, and absence of a generated context payload in failure responses.
