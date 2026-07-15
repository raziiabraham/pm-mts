# *PM Is Now Another Member of Technical Staff* Workbook

These worksheets turn the book's operating chain into reusable artifacts:

`signal -> evidence -> decision -> specification -> system behavior -> review -> release -> measurement -> learning`

Use one real, bounded problem across the workbook where possible. Link every artifact to its source evidence and successor rather than copying context manually. Delete fields that do not apply, but do not silently skip a risk or ownership question: record why it is not relevant.

The templates are decision aids, not mandatory process. Adapt them to the team's domain, risk, tools, and governance. They do not replace engineering, security, data, design, legal, accessibility, or behavioral-science review.

## How to Use This Workbook

Choose one of three modes:

1. **Quick path:** Chapters 1, 8, 13, 15, and 20. Map your participation boundary, expose one flow, define an AI quality bar, create portable context, and carry one slice through delivery.
2. **Chapter path:** complete the mapped worksheet after each chapter. Reuse the same product problem where the fit is natural.
3. **Capstone path:** begin with one Assumption and Evidence Map, then complete only the artifacts required to carry that claim through prototype, implementation, review, release, and learning.

The PDF is designed for printing and handwriting. The Markdown files remain the editable source for teams that prefer to complete the records digitally.

## Chapter-to-Workbook Map

| Chapter | Exercise | Workbook record |
| --- | --- | --- |
| 1 | Map your technical floor | Technical Floor Map |
| 2 | Turn a user story into an API conversation | API State Worksheet |
| 3 | Turn a feature idea into a release path | Feature Release Path Record |
| 4 | Rewrite and hand off an image requirement | Image Requirement Record |
| 5 | Turn a product question into SQL thinking | Product Data Question Record |
| 6 | Write a tracking plan | Tracking Plan |
| 7 | Design an experiment before results exist | Experiment Pre-Registration Card |
| 8 | Expose ambiguity in a flow | Flow-to-Acceptance Record |
| 9 | Audit one screen and one reusable component | Design Audit and Component Contract |
| 10 | Diagnose one target behavior twice | Behavior Intervention Card |
| 11 | Map the problem shape | Evidence Card and API State Worksheet |
| 12 | Compare solution shapes | AI Solution-Fit Decision Record |
| 13 | Design an AI evaluation system | AI Evaluation Scorecard |
| 14 | Design a calibration loop | Prompt Evaluation Table, AI Calibration Record, and Ship Decision Record |
| 15 | Create a portable context brief | Portable Context Brief |
| 16 | Build a repo orientation map | Repository Orientation Map |
| 17 | Create an assumption and evidence map | Assumption and Evidence Map |
| 18 | Write a prototype contract | Prototype Contract |
| 19 | Design a product instrument | Product Instrument Design Record and Productionization Memo |
| 20 | Take one slice through delivery | End-to-End Delivery Slice Record, PR Review Checklist, and Ship Decision Record |

## Artifact Index

The assembled workbook contains 25 reusable records. Some chapters use more than one record because the exercise crosses product, technical, or release boundaries. Reusing a record is intentional: the operating chain should carry evidence forward rather than duplicate it.



---

# Technical Floor Map

## Product Area and Promise

- Product area:
- User or operational actor:
- Product promise: what should they be able to trust?
- Decision this map should improve:

## System Behavior Behind the Promise

| State, system, data, or integration | Why the promise depends on it | Current evidence/source | Important unknown |
| --- | --- | --- | --- |
|  |  |  |  |

## Participation Level

| Level | What I can do today | Evidence or example | Gap | Next safe practice |
| --- | --- | --- | --- | --- |
| Ask |  |  |  |  |
| Inspect |  |  |  |  |
| Prototype |  |  |  |  |
| Contribute |  |  |  |  |

## Ownership Boundary

| Decision or activity | My role | Accountable owner or specialist | When to involve them | Handoff evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Thirty-Day Practice Plan

| Week | One action that follows the work further | Person or artifact needed | Evidence of progress |
| --- | --- | --- | --- |
| Week 1 |  |  |  |
| Week 2 |  |  |  |
| Week 3 |  |  |  |
| Week 4 |  |  |  |

## Reflection

- Where should I stop and ask for deeper expertise?
- What became clearer because I moved closer to the system?
- What will I inspect again after the next release?



---

# API State Worksheet

## Product Promise

- User story:
- User action that starts the flow:
- Object/resource whose state changes:
- Decision this worksheet must clarify:

## Actors and Contract

| Actor/system | Request or event | Authentication/permission | Response or state change |
| --- | --- | --- | --- |
|  |  |  |  |

## Request

- Method/operation:
- Endpoint or contract reference:
- Required fields:
- Optional fields:
- Idempotency/retry identifier:
- Sensitive fields and handling boundary:

## State Map

| System state/status | User meaning | UI state/copy | Internal action | Support visibility | Event/metric |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Failure and Recovery

| Failure | How detected | Safe retry? | User recovery | Owner/escalation |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Asynchronous Behavior

- Webhook/callback events:
- Source of truth:
- Late event behavior:
- Duplicate event behavior:
- Missing/out-of-order event reconciliation:

## Acceptance and Verification

- Contract tests:
- Happy-path product check:
- Error/recovery checks:
- Security/logging checks:
- Analytics checks:
- Open engineering/security questions:



---

# Feature Release Path Record

## Objective and Slice

- User problem:
- Intended outcome:
- Smallest buildable version:
- Explicitly excluded:
- Evidence supporting this slice:

## Delivery Path

| Stage | Product question | Artifact, environment, or check | Owner | Exit evidence |
| --- | --- | --- | --- | --- |
| Brief and acceptance |  |  |  |  |
| Local implementation |  |  |  |  |
| Automated checks |  |  |  |  |
| Review |  |  |  |  |
| Preview or staging |  |  |  |  |
| UAT |  |  |  |  |
| Deployment |  |  |  |  |
| User exposure |  |  |  |  |
| Measurement |  |  |  |  |

## Release Control

- Feature flag or cohort:
- Rollout stages:
- Pause condition:
- Rollback or disable method:
- Support and on-call visibility:
- Data or migration reversibility:

## Product Verification

| Scenario | Expected behavior | Where tested | Result/evidence | Owner/status |
| --- | --- | --- | --- | --- |
| Happy path |  |  |  |  |
| Validation failure |  |  |  |  |
| Dependency failure |  |  |  |  |
| Permission or role boundary |  |  |  |  |
| Retry, duplicate, or recovery |  |  |  |  |

## Learning Contract

- Primary outcome:
- Guardrail:
- Event, query, or dashboard:
- Review date:
- Continue, revise, pause, or stop rule:
- Questions still requiring engineering, design, data, security, or operational judgment:



---

# Image Requirement Record

## User Job and Asset Role

- Product surface:
- User job:
- Why the image matters to trust, comprehension, or conversion:
- Asset owner and rights source:

## Input Contract

| Decision | Requirement | User-facing reason | Validation or fallback |
| --- | --- | --- | --- |
| Accepted formats |  |  |  |
| Minimum dimensions |  |  |  |
| Maximum file size |  |  |  |
| Aspect ratio and crop |  |  |  |
| Metadata retained |  |  |  |
| Privacy or rights boundary |  |  |  |

## Upload, Processing, and Storage

- Upload path and authorization:
- Original storage policy:
- Processing states:
- Generated variants:
- Retry and duplicate behavior:
- Retention and deletion:
- Failure ownership:

## Delivery Contract

| Context | Variant or transformation | Delivery path | Performance target | Fallback |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## User-Visible States

| State | Trigger | Interface behavior and copy | Recovery | Event/evidence |
| --- | --- | --- | --- | --- |
| Idle |  |  |  |  |
| Uploading |  |  |  |  |
| Processing |  |  |  |  |
| Ready |  |  |  |  |
| Failed |  |  |  |  |
| Missing or unavailable |  |  |  |  |

## Acceptance and Tradeoffs

- Required quality:
- Performance and cost guardrails:
- Accessibility requirement:
- Analytics or operational evidence:
- Open infrastructure or security decisions:
- What the requirement deliberately leaves to engineering/design judgment:

## AI Coding-Agent Handoff

- Observed user problem:
- Smallest prototype slice needed to learn:
- Explicit non-goals:
- Assumptions the agent must surface:
- Tests, diff, screenshots, and other evidence to return:
- Human review gates before production architecture or deployment:



---

# Product Data Question Record

## Question, Hypothesis, and Decision

- Product question:
- Hypothesis:
- Decision that could change:
- Evidence that would challenge the hypothesis:

## Metric and Grain

- Metric or comparison:
- Object being counted, summed, or compared:
- One row in the intended result represents:
- Time window and time zone:
- Cohort or eligibility:

## Source and Relationships

| Table, collection, event, or dashboard | Relevant fields | Relationship/key | Source-of-truth concern |
| --- | --- | --- | --- |
|  |  |  |  |

## Query Plan

- Filters:
- Joins, lookups, or embedded paths:
- Grouping:
- Aggregation:
- Missing, duplicate, or late data behavior:

```text
Write SQL, MongoDB syntax, or a pseudo-query here.



```

## Validation and Limits

| Check | Expected result | Actual evidence | Disposition |
| --- | --- | --- | --- |
| Row-count or grain check |  |  |  |
| Duplicate check |  |  |  |
| Null/missing-data check |  |  |  |
| Dashboard or source comparison |  |  |  |
| Sample-record inspection |  |  |  |

- What this analysis supports:
- What it cannot establish:
- Data or statistical specialist review needed:
- Next question:



---

# Tracking Plan

## Product Decision

- Feature/journey:
- Assumption or decision:
- Primary outcome:
- Guardrails:
- Owner:

## Event Contract

| Event | Exact firing condition | Actor | Object | Required properties | Identity/time rule | Decision supported |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Property Dictionary

| Property | Type | Allowed values/source | Required? | Sensitive? | Meaning/version |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Metric Definitions

| Metric | Numerator | Denominator | Unit/grain | Window/time zone | Exclusions | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Governance and QA

- Schema/version:
- Expected volume:
- Duplicate policy:
- Late event policy:
- Consent/retention/access constraints:
- Development validation:
- Production validation and alert:
- Backfill/reprocessing rule:
- Retirement rule:



---

# Experiment Pre-Registration Card

## Decision

- Decision this experiment informs:
- Why a randomized experiment is appropriate:
- Decision deadline and reversibility:

## Hypothesis and Mechanism

- Target population:
- Product change:
- Expected behavior:
- Why the change should cause it:

## Design

- Randomization unit:
- Eligibility:
- Trigger condition and counterfactual logic:
- First possible treatment exposure:
- Estimand and analysis population:
- Exclusions:
- Bucketing moment:
- Stable assignment method:
- Traffic allocation:
- Control:
- Variant(s):
- Contamination/interference risk:

## Measurement

- Primary metric and exact definition:
- Numerator, denominator, and metric grain:
- Baseline and source:
- Minimum effect worth acting on, absolute and relative:
- Operational floors:
- Treatment-effect guardrails and harm margins:
- Supporting metrics:
- Required events/properties:

## Analysis Plan

- Statistical method and assumptions:
- Alpha/interval level and sidedness:
- Power and required sample for primary metric:
- Power or interval requirement for guardrails:
- Stopping rule and expected duration:
- Prespecified segments:
- Multiple-comparison treatment:
- Missing data/outlier policy:

## Validity Checks

- Exposure logging:
- Sample-ratio mismatch:
- Pre-exposure balance diagnostics and interpretation:
- Instrumentation QA:
- Reasons to invalidate:
- Legitimate reasons for replication or follow-up:

## Evidence Rule

- Supported benefit if:
- Supported harm if:
- Inconclusive if:
- Invalid if:

## Product Decision Rule

- Ship if:
- Iterate if:
- Stop if:
- Roll back/avoid rollout if:
- Ship cautiously under uncertainty if:
- Language required when evidence and product action differ:

## Sign-Off

- Product:
- Data/statistics:
- Engineering:
- Design/research:
- Date locked before results:



---

# Flow-to-Acceptance Record

## Scope and Operational Claim

- Product journey/object:
- User or operational problem:
- Start condition:
- End condition:
- In-scope implementation boundary:
- Explicitly deferred boundary and manual fallback:
- Source evidence and domain reviewers:

## Actors and Ownership

| Actor/system | Role in the flow | Actions allowed | Evidence produced | Handoff owner |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Current State and Intended State

| Step | Current behavior | Failure/cost | Intended behavior | Product/system affected |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Object States and Transitions

| From state | Trigger/action | Evidence required | To state | Custodian/owner | Invalid-transition behavior |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Event and Audit Contract

- Stable object identifier:
- Actor and authorization evidence:
- Event and server timestamps:
- Location/device/application context:
- Transition-specific fields:
- Idempotency or duplicate rule:
- History and support visibility:
- SLA clock: starts, stops, pauses, and source timestamp:

## Negative and Recovery Paths

| Scenario | Detection | User/operator feedback | System behavior | Manual fallback/escalation | Owner |
| --- | --- | --- | --- | --- | --- |
| Duplicate action |  |  |  |  |  |
| Offline or timeout |  |  |  |  |  |
| Missing/invalid evidence |  |  |  |  |  |
| Out-of-order event |  |  |  |  |  |
| Disputed handoff |  |  |  |  |  |

## Acceptance and Verification

| ID | Given/when/then product behavior | UI/state check | API/data check | Event/analytics check | Owner/status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Open Decisions

| Decision/question | Risk if unresolved | Decision owner | Due point | Resolution/source |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |



---

# Design Audit and Remediation Record

## Scope

- Product surface/journey:
- Users and tasks:
- Platforms/viewports:
- Audit methods:
- Design-system/version reference:
- Reviewers/date:

## Findings

| ID | Screen/component/state | Finding and evidence | User impact | Severity | Existing pattern/token | Remediation | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## State Coverage

| Component/flow | Default | Loading | Empty | Error/recovery | Disabled | Success | Responsive | Keyboard/assistive tech |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Reuse Decision

- Existing component/pattern:
- Reuse, extend, or create:
- Product reason:
- Accessibility and interaction review:
- Code/design parity check:
- Maintainer/ownership decision:

## Prioritization

- Critical before release:
- Next product slice:
- Design-system backlog:
- Accepted debt and expiry/review date:



---

# Design-System Component Contract

## Purpose and Decision

- Component/pattern:
- User intent supported:
- Product surfaces and frequency:
- Existing system options reviewed:
- Decision: reuse, extend, or create:
- Why composition is or is not sufficient:
- Design owner / engineering owner:

## Anatomy and Content

| Element | Required/optional | Content rule | Interaction/semantic role | Truncation/absence behavior |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## API, Variants, and States

| Prop/variant/state | Allowed values | Default | User-visible behavior | Invalid combination prevented? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Cover default, hover where relevant, pressed, focus, disabled, loading, empty, error, and success states. Delete states that genuinely do not apply and record why.

## Token Contract

| Decision | Semantic token | Component token, if justified | Raw value prohibited? | Figma variable/style | Code reference |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Responsive and Compositional Behavior

- Supported widths/platforms:
- Minimum touch target:
- Reflow/wrapping rule:
- Long content/localization rule:
- Nested action rule:
- Performance or rendering constraint:

## Accessibility Contract

- Native semantic element/role:
- Accessible name and description:
- Keyboard order and activation:
- Visible focus behavior:
- Error/status announcement:
- Contrast and non-color cues:
- Reduced-motion/zoom/text-resize behavior:
- Assistive-technology verification:

## Figma-to-Code Parity

| Contract area | Figma source/status | Code source/status | Verification | Drift owner/date |
| --- | --- | --- | --- | --- |
| Variants and states |  |  |  |  |
| Tokens |  |  |  |  |
| Responsive behavior |  |  |  |  |
| Accessibility |  |  |  |  |
| Product usage |  |  |  |  |

## Tests, Release, and Maintenance

- Unit/interaction tests:
- Visual regression stories:
- Keyboard/accessibility checks:
- Product acceptance criteria:
- Documentation and examples:
- Version/release path:
- Adoption or migration plan:
- Deprecated alternatives and removal date:
- Exceptions, owner, and review date:



---

# Behavior Intervention Card

## Target Behavior and Context

- Specific observable behavior:
- User/audience and journey step:
- Decision risk: low, medium, or high:
- Current baseline or qualitative frequency:
- Why this behavior should create user value:

## Evidence Ladder

| Level | Claim | Evidence/source | Confidence and limitation |
| --- | --- | --- | --- |
| Observation |  |  |  |
| Behavioral diagnosis |  |  |  |
| Intervention hypothesis |  |  |  |
| Outcome evidence |  |  |  |

## Competing Diagnosis

| Lens | Plausible barrier | Supporting evidence | Contradicting evidence | What would discriminate it? |
| --- | --- | --- | --- | --- |
| Fogg: motivation |  |  |  |  |
| Fogg: ability |  |  |  |  |
| Fogg: prompt |  |  |  |  |
| COM-B: capability |  |  |  |  |
| COM-B: opportunity |  |  |  |  |
| COM-B: motivation |  |  |  |  |

## Intervention Contract

- Change proposed:
- Mechanism expected to change:
- User control: skip, revise, undo, or opt out:
- Safe default/fallback:
- Explanation and transparency:
- Accessibility and inclusion:
- Privacy/data collected, purpose, retention, and permission:
- Risk of manipulation, exclusion, or narrowing choice:

## Evidence Plan

| Evidence type | Metric/method | Segment/cohort | Decision threshold or interpretation rule | Owner |
| --- | --- | --- | --- | --- |
| Mechanism |  |  |  |  |
| Activation/outcome |  |  |  |  |
| Qualitative |  |  |  |  |
| System performance |  |  |  |  |
| Longer-term directional signal |  |  |  |  |

### Low-Traffic Plan

- Stable usability task and audience:
- Interviews/session review:
- Release-cohort comparison and caveats:
- Minimum repeated evidence before expanding:
- Claims this design cannot support:

## Guardrails and Reversal

| Potential harm/failure | Guardrail signal | Stop/revise condition | Response owner |
| --- | --- | --- | --- |
|  |  |  |  |

- Evidence that would reverse the diagnosis:
- Rollback or safe-disable path:
- Decision date and result:
- What the team learned next:



---

# Evidence Card

- Evidence ID:
- Date observed:
- Owner:
- Decision or opportunity:

## Source

- Source type:
- Source link or durable reference:
- Population/context:
- Collection method and period:
- Consent/confidentiality constraints:

## Observation

State what was seen, heard, or measured without interpretation.

## Interpretation

State the current explanation and plausible alternatives.

## Strength and Limits

- Confidence:
- What this evidence supports:
- What it does not support:
- Known bias, missing context, or data-quality issue:

## Decision Link

- Assumption affected:
- Decision changed or informed:
- Artifact/ticket link:

## Next Test

- Smallest useful next question:
- Method:
- Evidence that would increase confidence:
- Evidence that would reverse the current interpretation:



---

# AI Solution-Fit Decision Record

## Problem Without Technology

- Intended user and decision moment:
- Current behavior and missing capability:
- Approved data/content/tool asset:
- Consequence if the output is wrong:
- Required user control and fallback:
- Evidence/source links:

## Problem Shape

| Question | Evidence | Constraint/unknown |
| --- | --- | --- |
| Which behavior must be exact? |  |  |
| Which output may vary safely? |  |  |
| Which interpretation creates value? |  |  |
| What labels or ground truth exist? |  |  |
| Which source must ground output? |  |  |
| What should the system refuse or abstain from? |  |  |

## Option Comparison

| Dimension | No build/manual | Assisted workflow | Deterministic software | Predictive ML | Generative AI | Hybrid | Buy/integrate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| User value |  |  |  |  |  |  |  |
| Required data/labels |  |  |  |  |  |  |  |
| Grounding/provenance |  |  |  |  |  |  |  |
| Acceptable variability |  |  |  |  |  |  |  |
| Failure consequence |  |  |  |  |  |  |  |
| User control/fallback |  |  |  |  |  |  |  |
| Cost/latency |  |  |  |  |  |  |  |
| Team readiness/maintenance |  |  |  |  |  |  |  |
| Smallest meaningful test |  |  |  |  |  |  |  |

## Responsibility Boundary

| Responsibility | Deterministic code | Retrieval/provider | Predictive/generative component | UI/user | Human/domain owner |
| --- | --- | --- | --- | --- | --- |
| Eligibility and permissions |  |  |  |  |  |
| Context construction |  |  |  |  |  |
| Interpretation/generation |  |  |  |  |  |
| Validation/abstention |  |  |  |  |  |
| Storage/provenance |  |  |  |  |  |
| Monitoring/escalation |  |  |  |  |  |

## Decision

- Selected system shape and why:
- Rejected alternatives and evidence:
- Assumptions to test:
- Evaluation set required before release:
- Cost/latency boundary:
- Failure, fallback, and rollback:
- Privacy/security/rights review:
- Approvers/date:



---

# AI Evaluation Scorecard

## Capability and Release

- Capability/version:
- Model/prompt/tool/retrieval configuration:
- Intended users and task:
- Decision: prototype, internal test, pilot, expand, pause, or retire:

## Evaluation Set

- Dataset/version:
- Source and consent:
- Representative slices:
- Edge/adversarial cases:
- Leakage check:
- Known coverage gaps:

## Criteria

| Criterion | Definition | Evaluator | Scale/threshold | Critical failure? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Results

| Slice | Sample | Criterion results | Critical failures | Comparison to baseline |
| --- | ---: | --- | ---: | --- |
|  |  |  |  |  |

## Evaluator Quality

- Human reviewer calibration:
- Model-judge agreement with humans:
- Disagreement review:
- Deterministic-check coverage:

## Failure Taxonomy

| Failure type | Count/rate | Severity | Likely layer | Owner | Regression case added? |
| --- | ---: | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Product and Risk Signals

- Task success/behavior metric:
- User feedback:
- Safety/privacy/fairness concerns:
- Latency and cost:
- Escalation/fallback behavior:

## Decision Record

- Thresholds met/not met:
- Accepted residual risks:
- Required changes:
- Rollout boundary:
- Monitoring and recalibration trigger:
- Approvers/date:



---

# Prompt Evaluation Table

## Capability

- Task and intended user value:
- Dataset/version:
- Model/tool/retrieval configuration:
- Baseline prompt/version:
- Candidate prompt/version:
- Evaluators and calibration date:

## Case-Level Comparison

| Case ID | Input/slice | Expected qualities | Baseline output/result | Candidate output/result | Criterion scores | Preferred | Failure tags | Reviewer note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Aggregate Results

| Criterion/slice | Baseline | Candidate | Threshold | Delta | Confidence/limits |
| --- | ---: | ---: | ---: | ---: | --- |
|  |  |  |  |  |  |

## Regression and Risk Review

- Critical failures introduced:
- Previously failing cases fixed:
- Disagreements requiring adjudication:
- Cost/latency change:
- Safety/privacy change:
- Dataset leakage or overfitting concern:

## Decision

- Adopt, revise, reject, or run further test:
- Evidence supporting decision:
- Residual risk:
- New regression cases:
- Version/release boundary:



---

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



---

# Portable Context Brief

## Objective

- User or business problem:
- Desired decision or outcome:
- Why this matters now:

## Evidence

| Source | Observation | What it supports | Confidence/limits |
| --- | --- | --- | --- |
|  |  |  |  |

## Scope

- Included:
- Excluded:
- Smallest useful slice:

## Product Behavior

- Entry condition:
- Happy path:
- Loading/pending states:
- Error and recovery states:
- Permissions and roles:
- Data created, read, changed, or deleted:

## Relevant Surfaces

- Ticket/spec:
- Flow/design:
- Repository files or modules:
- Existing implementation precedent:
- API/schema/event documentation:

## Constraints and Ownership

- Security/privacy/compliance:
- Design-system/accessibility:
- Performance/cost:
- Decisions the agent or contributor may make:
- Decisions requiring human owner approval:

## Expected Output

- Artifact or change requested:
- Required explanation:
- Files or systems that must not change:

## Verification

- Product checks:
- Automated checks:
- Data/event checks:
- Reviewers:
- Rollout/rollback expectations:

## Open Questions

-



---

# Repository Orientation Map

## Product Promise and Entry Point

- Product flow:
- User promise:
- User or system entry point:
- Read-only orientation prompt or task:

## Rules and Reading Order

| Priority | File, document, or instruction | What it governs | Verified date |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Product-to-Repository Map

| Product behavior or state | Route/component/service/data | File reference | Tests/checks | Event/flag | Owner/reviewer |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Delivery Surfaces

- Local run path:
- Preview or staging path:
- CI and required checks:
- Feature-flag location:
- Analytics convention:
- Related tickets, specs, decisions, and pull requests:

## Evidence Classification

| Claim | Verified fact, inference, contradiction, or unknown | Evidence | Consequence or next check |
| --- | --- | --- | --- |
|  |  |  |  |

## Orientation Boundary

### What the repository proves

-

### What the repository cannot answer

-

### Human context required

-

## Next Safe Action

- Smallest useful inspection, prototype, or change:
- Files or systems that must not change:
- Required reviewers:
- Verification before implementation:



---

# Assumption and Evidence Map

## Product Bet and Original Signal

- Product bet or decision:
- Original observation:
- Observation type:
- Source and date:
- Current confidence and limits:

## Artifact Lineage

| Sequence | Artifact or conversation | Claim inherited | Claim changed or added | Evidence link |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Assumption Inventory

| Assumption | Type | Uncertainty (1-5) | Consequence (1-5) | Priority | Current evidence |
| --- | --- | ---: | ---: | ---: | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |

## Evidence Plan for the Top Assumptions

| Assumption | Question | Evidence method | Population/source | Decision threshold | Owner/date |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Evidence Update

| Evidence item | Evidence for | Evidence against | Limit or alternative explanation | Confidence change |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Decision

- Proceed, revise, narrow, pivot, stop, or investigate:
- Reason:
- Rejected alternatives:
- Next artifact or test:
- Evidence that would reverse this decision:



---

# Prototype Contract

## Learning Question

- Decision the prototype informs:
- Riskiest assumption:
- What must be learned now:

## Audience and Scenario

- Participant/user:
- Context and task:
- Starting information:
- Success behavior:

## Fidelity

- Interaction fidelity:
- Content/data realism:
- AI-output realism:
- Visual/design-system fidelity:
- Technical integration fidelity:
- What is intentionally simulated:

## Evidence Plan

- Method:
- Observable behaviors:
- Questions/prompts:
- Instrumentation:
- Sample and recruiting limits:
- Evidence that supports the assumption:
- Evidence that weakens or rejects it:

## Boundaries

- Not safe or appropriate for:
- Privacy/security constraints:
- Claims stakeholders must not infer:
- Parts that cannot be reused as production code/content:

## Stop Rule and Next Decision

- Stop when:
- Proceed if:
- Revise if:
- Abandon if:
- Owner and review date:



---

# Product Instrument Design Record

## Decision and Input Boundary

- Recurring product decision:
- Intended users:
- Manual workflow today:
- Input source and owner:
- Permission, consent, rights, and retention boundary:
- No-output or abstention condition:

## Structured Output

| Field | Type/allowed values | Meaning | Evidence/provenance | Missing behavior |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Pipeline

| Stage | Input | Output | Quality question | Failure route | Owner |
| --- | --- | --- | --- | --- | --- |
| Scope and collection |  |  |  |  |  |
| Ingestion and identity |  |  |  |  |  |
| Extraction |  |  |  |  |  |
| Taxonomy or mapping |  |  |  |  |  |
| Evaluation |  |  |  |  |  |
| Aggregation |  |  |  |  |  |
| Presentation |  |  |  |  |  |

## Evaluation Slice

| Case | Input shape | Expected output or no-output | Risk/severity | Reviewer/result |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 - no-output case |  |  |  |  |

## Error Taxonomy and Review

| Error type | Detection | User/decision consequence | Human-review route | Correction path |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Decision Surface

- Questions the dashboard, report, or export must answer:
- Required slices and filters:
- Observation versus inference treatment:
- Source and uncertainty display:
- User correction or challenge path:

## Product Gate

| Decision | Criteria | Evidence | Owner/date |
| --- | --- | --- | --- |
| Stop |  |  |  |
| Improve prototype |  |  |  |
| Productionize |  |  |  |
| Pivot |  |  |  |



---

# Product Instrument Productionization Memo

## Decision

- Instrument/capability:
- Decision requested:
- Users and decisions supported:
- Current proof-of-concept boundary:
- Recommended next state:

## Input and Rights

- Data sources and owners:
- Consent/license/terms basis:
- Sensitive-data classification:
- Retention and deletion:
- Deduplication/identity/provenance:
- Prohibited uses:

## Pipeline

| Stage | Input/output contract | Implementation | Quality check | Failure route | Owner |
| --- | --- | --- | --- | --- | --- |
| Ingestion |  |  |  |  |  |
| Extraction |  |  |  |  |  |
| Taxonomy |  |  |  |  |  |
| Mapping |  |  |  |  |  |
| Aggregation |  |  |  |  |  |
| Presentation/export |  |  |  |  |  |

## Evaluation and Monitoring

- Evaluation dataset/version:
- Human review and calibration:
- Accuracy/quality dimensions:
- Slice and edge-case coverage:
- Release thresholds:
- Drift/data-quality alerts:
- Feedback and correction path:

## Architecture and Operations

- Build versus buy decision:
- Model/prompt/tool versions:
- Latency/throughput target:
- Cost model and budget guardrail:
- Reliability/SLO/fallback:
- Observability and audit log:
- Security/threat review:
- Support/runbook/on-call ownership:

## Rollout

- Internal/pilot/general-availability stages:
- Feature flag and cohort:
- User disclosure/explanation:
- Rollback/kill switch:
- Measurement and review date:

## Open Risks and Sign-Off

| Risk | Likelihood/impact | Mitigation | Owner | Due/status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

- Product:
- Engineering:
- Data/AI:
- Security/privacy/legal:
- Operations/support:



---

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



---

# Ship Decision Record

## Change

- User problem and intended outcome:
- Scope included/excluded:
- Ticket/spec:
- Branch/PR/build:
- Owners:

## Evidence and Acceptance

- Evidence supporting the decision:
- Required product behavior:
- Known limitations:
- Rejected alternatives:

## Verification Record

| Check | Result/evidence | Owner | Status |
| --- | --- | --- | --- |
| Happy path |  |  |  |
| Error/recovery paths |  |  |  |
| Permissions/data behavior |  |  |  |
| Accessibility/design system |  |  |  |
| Type/lint/build/tests |  |  |  |
| Event and metric behavior |  |  |  |
| AI evaluation, if applicable |  |  |  |
| Robot/read-only review |  |  |  |
| Human review |  |  |  |
| Preview/staging |  |  |  |

## Risk and Controls

- Security/privacy/compliance sign-off:
- Feature flag/target cohort:
- Rollout stages:
- Guardrails and failure signals:
- Rollback/disable method:
- On-call/support visibility:

## Release and GTM

- Release owner/date:
- Internal communication:
- Customer communication:
- Documentation/training:

## Measurement and Learning

- Primary outcome:
- Guardrails:
- Dashboard/query:
- Review window:
- Continue/revise/pause rule:
- Result and next decision:



---

# End-to-End Delivery Slice Record

## Pressure-Tested Brief

- User signal and source:
- Problem and intended outcome:
- Smallest useful slice:
- Expected behavior and acceptance:
- Exclusions and unresolved questions:
- Success and guardrail signals:

## Planning Path

- Manual work, direct edit, prototype, or agent-assisted implementation:
- Why this path fits the risk and uncertainty:
- Repository precedents and rules:
- Files/systems likely to change:
- Files/systems explicitly protected:
- Required human owners and reviewers:

## Implementation and Verification

| Evidence | Result or link | Issue found | Disposition/owner |
| --- | --- | --- | --- |
| Local product QA |  |  |  |
| Type/lint/build/tests |  |  |  |
| Robot or read-only review |  |  |  |
| Human technical review |  |  |  |
| Product/design/data review |  |  |  |
| Preview or staging |  |  |  |
| Retest after review changes |  |  |  |

## Exposure and GTM

- Deployment date/build:
- Feature flag and eligible cohort:
- Rollout stages:
- Customer/internal communication:
- Support and documentation:
- Pause, rollback, or kill-switch owner:

## Boundary Memo

| Boundary | Included now | Deferred/manual fallback | Risk and owner |
| --- | --- | --- | --- |
| Product behavior |  |  |  |
| Data and instrumentation |  |  |  |
| Reliability/operations |  |  |  |
| Security/privacy/compliance |  |  |  |
| AI/model behavior, if applicable |  |  |  |

## Learning Record

- How will we know it worked?
- How will we know it caused harm?
- How will we know the team can maintain it?
- Measurement window and decision date:
- Continue, revise, pause, roll back, or stop rule:
- Result and next operating-loop decision:

