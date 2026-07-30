# Product Data Question Record

## Hands-on Noted Cohort Lab

Use the same fifty-user Noted cohort as Chapter 5 before applying this record to your own product. From the cloned repository root, build the SQLite database:

```sh
python companion/sql/noted/load_noted.py
```

The loader should report users=50, documents=243, files=55, coworker_messages=50, squad_agents=9, ai_settings=50, user_storage=50, and events=2892. The cohort is synthetic and generated from a fixed seed, so its numbers are reproducible rather than discovered; `companion/sql/noted/PROVENANCE.md` records where the rows come from and what they deliberately do not reconcile. Then make the companion print each of the chapter's questions beside the rows its query actually returned:

```sh
./companion/sql/noted/run_chapter_examples.sh
```

Do not treat running the queries as the end of the exercise. Inspect the relationship path `users -> documents -> files`: one user holds many documents, and one document holds many files.

Then find the printed result that joins `cohort_power_01` to both `documents` and `coworker_messages`. That account is one user row with thirteen documents and a single message-count row, so the join repeats the count once per document and `SUM(message_count)` reports 806 messages instead of the 62 the account actually sent. Every join key is correct and no warning appears. Write down how you would have caught a thirteen-times overstatement before quoting it in a review.

Now record the published-rate result exactly as the database returned it. Raw counts make the two groups look equivalent—seventeen published documents against sixteen—so the fourth column is the same evidence divided by the group it came from:

| persona | users | published | published per user | % of drafts published |
| --- | ---: | ---: | ---: | ---: |
| power_users |  |  |  |  |
| casual_users |  |  |  |  |

- Which roadmap decision would the raw counts of seventeen and sixteen have supported that the per-user rate does not?
- What decision must **not** be made from this result alone?
- Which missing record would provide stronger evidence about when the publishing gap opened?

Now give an AI coding agent this bounded task:

> Using the loaded Noted SQLite database, add one query that tests a different explanation for the publishing gap. Before writing SQL, state the product question, decision, metric, grain, denominator, join path, and one limitation. Run the query and return the command, SQL, and actual result. Do not change the upstream schema or data.

Capture the agent-assisted run rather than accepting a proposed query that was never executed:

- Command used:
- Query file created or changed:
- Actual result returned:
- Grain and denominator verified:
- Join-duplication risk checked:
- Interpretation and limitation:

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
