# Agent Charter

## Product Job

- User and moment:
- Goal in one sentence:
- Evidence that proves the goal is met:
- Why a fixed pipeline is insufficient:
- Lowest useful autonomy level:

## Product Shape

| Decision or stage | Fixed application step, tool-using feature, or agent choice? | Why this shape? | Accountable owner |
| --- | --- | --- | --- |
|  |  |  |  |

## Loop and Stop Conditions

| Observe | Allowed next actions | Validation before action | Stop or escalation condition |
| --- | --- | --- | --- |
|  |  |  |  |

- Goal-reached stop:
- Step/time/token/cost budget stop:
- Repeated-tool-failure stop:
- Uncertainty that returns to the user:
- Behaviour when no safe next action exists:

## Tools and Connected Services

| Tool or server | Job and scope | Read-only or side-effecting | Permission and tenant boundary | Failure/duplicate behaviour | Confirmation or rollback |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Memory and Retrieval

| Information | Working, conversation, or durable memory? | Source and freshness | Retention/deletion | Who can inspect or correct it? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

- What must be retrieved fresh rather than remembered?
- What must never persist beyond the run?
- How is tenant isolation verified?

## Skills

| Skill | Trigger | Instructions/tools loaded | Version | Evaluation set | Rollback path |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Trajectory and Outcome Evaluation

- Required trajectory checks:
- Required final-output checks:
- Critical release blockers:
- Human-review and adjudication path:
- Trace fields a reviewer must be able to reconstruct:
- Cost, latency, privacy, security, and rights guardrails:

## Exposure and Earned Agency

- Current autonomy rung:
- Exposure boundary or feature flag:
- Fallback and disable path:
- Evidence required to widen agency:
- New failure surface created by the next rung:
- Evidence that would cause rollback or reduced autonomy:

## Riskiest Line

- The single riskiest decision in this charter:
- Why it is risky:
- Strongest harness control at that boundary:
