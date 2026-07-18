# Product Data Question Record

## Hands-on Sakila Lab

Use the same generated Sakila data as Chapter 5 before applying this record to your own product. From the cloned repository root, build the SQLite database:

```sh
./companion/sql/sakila/load_sakila.sh
```

The loader should verify 599 customers, 1,000 films, 4,581 inventory copies, 16,044 rentals, 16,049 payments, and two stores. Then make the companion print the product question, exact query, actual result, and interpretation boundary:

```sh
./companion/sql/sakila/run_product_query.sh
```

Do not treat running the query as the end of the exercise. Inspect the relationship path `film -> inventory -> rental`, confirm that one result row represents one film, and explain why recorded rentals divided by distinct inventory copies is more useful than rental count alone for this investigation.

Record one row exactly as the database returned it:

| title | inventory copies | recorded rentals | rentals per copy |
| --- | ---: | ---: | ---: |
|  |  |  |  |

- What possible availability problem does this result help investigate?
- What decision must **not** be made from this result alone?
- Which missing behavior would provide stronger evidence of unmet demand?

Now give an AI coding agent this bounded task:

> Using the loaded Sakila SQLite database, add one query that tests a different explanation for an availability problem. Before writing SQL, state the product question, decision, metric, grain, denominator, join path, and one limitation. Run the query and return the command, SQL, and actual result. Do not change the upstream schema or data.

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
