# Guidance for AI coding agents

This is the educational companion to *PM Is Now Another Member of Technical Staff*. The reader may be new to terminals, Git, Python, SQL, APIs, or coding agents.

When helping a reader:

1. Identify the chapter and product question before running anything.
2. Read the relevant `companion/<area>/README.md` and inspect only the bounded files needed for that exercise.
3. Explain unfamiliar terms and each command in plain language before execution.
4. Work from the repository root and show the exact command used.
5. Do not edit fixtures, validators, templates, or expected outputs unless the reader explicitly asks to experiment.
6. If the reader wants to experiment, suggest a Git branch or copied file first, then show the diff afterward.
7. Run the narrow chapter validator before the complete validation suite.
8. Translate a pass or failure into its product meaning and evidence boundary. A green check proves only the named deterministic assertions.
9. Do not add dependencies, contact external services, use network access, or request an API key for the supplied no-key path.
10. Never introduce employer code, credentials, customer data, or confidential artifacts.

For Chapter 2, begin with `companion/api/request.json`, then inspect the success, validation-error, and provider-error responses before running `python3 companion/api/validate_contract.py` (or `py companion\api\validate_contract.py` on Windows).
