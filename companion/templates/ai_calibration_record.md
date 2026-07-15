# AI Calibration Record

## Observed Failure

- Capability/version:
- User-visible failure and consequence:
- System/business consequence:
- Detection source: user report, event, trace, human review, judge, or regression:
- Severity and affected cohort:
- Preserved case/evidence location:

## Version Chain

| Layer | Current version/configuration | Evidence captured? |
| --- | --- | --- |
| Input/context construction |  |  |
| Retrieval/provider/index |  |  |
| Entity resolution/ranking |  |  |
| Prompt/model/sampling |  |  |
| Tool and output schema |  |  |
| Evaluator/rubric/judge |  |  |
| Application/exposure |  |  |

## Diagnosis

| Candidate layer | Supporting evidence | Contradicting evidence | How to discriminate |
| --- | --- | --- | --- |
| Input/context |  |  |  |
| Retrieval/provider |  |  |  |
| Identity/ranking |  |  |  |
| Prompt/orchestration |  |  |  |
| Model capability |  |  |  |
| Evaluation |  |  |  |
| UI/workflow |  |  |  |
| Policy/strategy |  |  |  |

## Bounded Change

- Diagnosed component:
- Smallest credible change:
- Expected mechanism:
- Layers deliberately unchanged:
- Cost/latency/privacy impact:
- New failure risk:

## Comparison Plan

| Case group | Cases/version | Required behavior | Critical regression | Evaluator |
| --- | --- | --- | --- | --- |
| Preserved failures |  |  |  |  |
| Normal regression |  |  |  |  |
| Boundary/high risk |  |  |  |  |
| Held out/novel |  |  |  |  |
| Repeated-run stability |  |  |  |  |

## Release and Production Learning

- Evaluation result and limits:
- Adopt, revise, reject, or investigate:
- Exposure boundary/feature flag:
- Fallback/rollback:
- Production sampling mix:
- Events/traces/qualitative evidence:
- Judge-to-human calibration check:
- Review owner/date:
- Evidence that would reverse the diagnosis:
- New regression cases and next decision:
