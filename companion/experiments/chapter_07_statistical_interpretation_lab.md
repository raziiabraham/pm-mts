# Chapter 7 Statistical Interpretation Lab

This companion lab practices interpretation, not independent statistical sign-off. The values are constructed teaching data adapted from the author's original “Online product experimentation” course page. Use a qualified statistician or experimentation specialist for consequential decisions and verify that the chosen method matches assignment, exposure, metric grain, missingness, stopping, and dependence.

## Lab A: proportion metric

### Scenario

A team tests a personalization quiz for new users who reach the fourth onboarding step. The primary metric is Day 1 retention among all triggered and assigned users. The team said before launch that a 10% relative lift from a 37.4% baseline—3.74 percentage points—would be worth acting on.

The constructed result is:

| Group | Retained on Day 1 | Triggered and assigned users | Day 1 retention | Onboarding completion |
|---|---:|---:|---:|---:|
| Control | `998` | `2,648` | `37.69%` | `91%` |
| Variant | `1,123` | `2,697` | `41.64%` | `89%` |

Using a two-sided large-sample comparison of the two retention proportions:

- absolute difference: `+3.95` percentage points;
- 95% confidence interval for the absolute difference: `+1.33` to `+6.57` percentage points;
- relative lift estimate: `+10.48%`;
- the absolute-difference interval expressed relative to the control rate: approximately `+3.53%` to `+17.43%`; and
- two-sided p-value: approximately `0.0032`.

The completion rates clear an 80% operational floor, but the variant is 2 percentage points below control. Completion numerators, denominators, a prespecified harm margin, and its interval are not supplied. The floor alone therefore cannot establish that the guardrail is safe.

### Interpretation tasks

1. Verify that the randomization unit, trigger condition, and retention denominator match the claim.
2. Explain why `+10.48%` relative and `+3.95` percentage points absolute describe the same point estimate in different units.
3. Compare the confidence interval with zero and with the `+3.74` percentage-point minimum effect worth acting on.
4. Explain why this result supports a positive retention effect but does not rule out a true effect smaller than the decision-relevant target.
5. State what completion data and non-inferiority rule are needed before calling the guardrail safe.
6. List at least three validity checks that could overturn the interpretation.
7. Identify which segments were prespecified for decisions and which are exploratory.

### Example evidence language

> For new users who reached the prespecified onboarding trigger, assignment to Variant B increased observed Day 1 retention by 3.95 percentage points, or 10.48% relative to control. The two-sided 95% interval for the absolute effect was 1.33 to 6.57 percentage points. This supports a positive effect, although the interval includes effects smaller than the 3.74-point minimum worth acting on. Both completion rates exceeded the operational floor, but the supplied data do not rule out unacceptable treatment-related harm. The evidence conclusion and rollout decision therefore remain conditional on guardrail and validity checks.

## Lab B: continuous metric

### Scenario

The original course exercise used average basket size per transaction. That metric can condition on a post-treatment event: users must purchase before they produce a basket. A randomized product experiment should prefer an outcome such as revenue per randomized eligible user, or analyze purchase incidence and basket value as separate parts of the mechanism.

For this revised teaching calculation, assume the metric is **revenue per randomized eligible user** and that each count is an independent user. The planning inputs are:

- baseline mean: `$16.89` per user;
- baseline standard deviation: `$46.03`;
- minimum effect worth acting on and design target: `+$3.00` per user;
- two-sided alpha: `0.05`;
- target power: `80%`;
- equal allocation; and
- illustrative normal-approximation output: approximately `3,696` independent users per variant.

The constructed result summary is:

| Group | Mean | Standard deviation | Independent users |
|---|---:|---:|---:|
| Control | `$16.89` | `$46.03` | `4,988` |
| Variant | `$20.82` | `$60.35` | `4,995` |

A two-sided Welch comparison calculated from those summary values gives:

- estimated difference: `+$3.93` per user;
- 95% confidence interval: `+$1.82` to `+$6.04`; and
- two-sided p-value: approximately `0.00026`, reported as `p < 0.001`.

### Interpretation tasks

1. Confirm that the counts really represent independent randomized users, not transactions or repeated observations.
2. Explain why transaction-level basket size can change because treatment changes who purchases, not only how much purchasers spend.
3. Ask whether skew, heavy tails, outliers, or clustered assignment require another method.
4. Compare the `$3.93` point estimate and `$1.82` to `$6.04` interval with zero and the `$3.00` minimum effect worth acting on.
5. Explain why the result supports a positive effect but does not rule out a true effect smaller than `$3.00`.
6. Explain why the p-value alone cannot determine product significance or guardrail safety.
7. State what would have to be justified before using a one-sided test instead.

## Validity checklist for both labs

- Assignment unit matches the product mechanism.
- Eligibility, trigger, exposure, estimand, numerator, and denominator are explicit.
- Allocation and sample-ratio checks pass.
- Metric grain matches the analysis unit.
- Missing and duplicate observations are understood.
- Fixed-horizon or sequential stopping rule was prespecified.
- Primary metric, decision segments, and multiplicity treatment were prespecified.
- Operational floors and treatment-effect harm margins are analyzed separately.
- Estimate, interval, minimum effect worth acting on, and guardrails are reported together.
- Time trends and supporting metrics are used as diagnostics, not post-hoc votes.
- Result language stays within the tested population, period, experience, and assumptions.
- A qualified reviewer confirms the method for a consequential decision.

## Reader deliverable

For each lab, produce a one-paragraph decision note with five labelled parts:

1. **Estimand, observed estimate, and interval**
2. **Prespecified criterion and guardrails**
3. **Validity conditions**
4. **Evidence label: supported benefit, supported harm, inconclusive, or invalid**
5. **Product decision and remaining uncertainty**
