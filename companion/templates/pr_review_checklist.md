# Product and PR Review Checklist

## Context

- User problem and evidence:
- Ticket/spec/flow:
- PR/build/preview:
- Scope explicitly excluded:

## Diff Orientation

- Files and systems changed:
- Product states changed:
- Data/schema/API/event changes:
- Existing pattern or reference implementation followed:
- Unexpected or unrelated changes:

## Product Correctness

- Happy path matches acceptance criteria.
- Loading, empty, pending, error, permission, and recovery states are covered.
- Copy and interaction match the intended user context.
- Analytics events fire at the defined moment with valid properties.
- Feature flag, cohort, default, and fallback behavior are correct.
- AI output, if present, meets evaluation thresholds and routes failures safely.

## Technical and Operational Quality

- Required format/type/lint/build/test checks pass.
- Security, privacy, logging, and secrets boundaries are respected.
- Design-system and accessibility patterns are reused correctly.
- Retry, duplication, idempotency, and concurrency risks are handled where relevant.
- Migration, backward compatibility, performance, cost, and monitoring are addressed.
- Rollback/disable path exists and is understood.

## Verification Evidence

| Check | Command/scenario | Result | Reviewer |
| --- | --- | --- | --- |
|  |  |  |  |

## Review Disposition

- Robot/read-only review findings:
- Product review findings:
- Engineer/design/data/security findings:
- Must fix before merge:
- Follow-up backlog:
- Approved by/date:
