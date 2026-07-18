# Chapter 5: Read a Product Question in SQL

You do not need Python or a database setup to begin. Start with the product question, read the exact SQL, and inspect the supplied result. Run SQLite only when you want to reproduce or change the query.

## Product question

> Which frequently rented films may be constrained by the number of inventory copies available?

Rental count alone is misleading because a title with more copies has more opportunities to be rented. This query compares recorded rentals with available inventory copies.

## Exact SQL from the exercise

```sql
WITH film_performance AS (
    SELECT
        f.film_id,
        f.title,
        COUNT(DISTINCT i.inventory_id) AS inventory_copies,
        COUNT(r.rental_id) AS recorded_rentals
    FROM film AS f
    JOIN inventory AS i
        ON i.film_id = f.film_id
    LEFT JOIN rental AS r
        ON r.inventory_id = i.inventory_id
    GROUP BY f.film_id, f.title
)
SELECT
    title,
    inventory_copies,
    recorded_rentals,
    ROUND(1.0 * recorded_rentals / inventory_copies, 2)
        AS rentals_per_copy
FROM film_performance
WHERE inventory_copies >= 4
ORDER BY rentals_per_copy DESC, recorded_rentals DESC, title
LIMIT 5;
```

[Open the SQL file](queries/film_demand_per_copy.sql)

## How to read the syntax

| SQL | Product meaning |
| --- | --- |
| `WITH film_performance AS (...)` | Build one intermediate table at film level before ranking it |
| `JOIN inventory` | Keep films that have physical inventory copies |
| `LEFT JOIN rental` | Preserve inventory copies even when no rental is recorded |
| `COUNT(DISTINCT i.inventory_id)` | Count available copies without multiplying them through the rental join |
| `COUNT(r.rental_id)` | Count recorded rental transactions |
| `GROUP BY f.film_id, f.title` | Produce one row per film |
| `recorded_rentals / inventory_copies` | Normalize demand by opportunity to rent |
| `WHERE inventory_copies >= 4` | Avoid ranking films from a very small copy base |
| `ORDER BY ... LIMIT 5` | Show the five highest diagnostic ratios |

The output grain is **one film**. The denominator is **distinct inventory copies**, not customers, stores, days, or rental opportunities.

## Supplied result

| title | inventory copies | recorded rentals | rentals per copy |
| --- | ---: | ---: | ---: |
| LOVE SUICIDES | 4 | 20 | 5.00 |
| SEATTLE EXPECATIONS | 5 | 24 | 4.80 |
| BACKLASH UNDEFEATED | 4 | 19 | 4.75 |
| HANGING DEEP | 4 | 19 | 4.75 |
| HANDICAP BOONDOCK | 6 | 28 | 4.67 |

[Open the captured result](results/film_demand_per_copy.expected)

## What the result does—and does not—say

The result identifies films with many recorded rentals relative to their inventory copies. It can help a team choose which titles deserve a closer availability investigation.

It does **not** prove unmet demand or a causal inventory shortage. The dataset does not record failed searches, unavailable-title attempts, copy downtime, waiting lists, or the time each copy was eligible to rent. `SEATTLE EXPECATIONS` is intentionally spelled as it appears in the source data.

Before changing the SQL, state:

1. the decision you want to support;
2. the output grain;
3. the numerator and denominator;
4. the required join path;
5. the filter or time boundary; and
6. what the result still cannot prove.

Use the [Product Data Question Record](../../templates/product_data_question.md) to apply the method to your own product question.

## Optional: reproduce the query with SQLite

This lab vendors the open-licensed generated Sakila data from the [jOOQ/sakila](https://github.com/jOOQ/sakila) repository. No Docker, database server, account, or network connection is required after cloning.

From the repository root, create the local database:

```sh
./companion/sql/sakila/load_sakila.sh
```

The loader verifies 599 customers, 1,000 films, 4,581 inventory copies, 16,044 rentals, 16,049 payments, and two stores.

Then print the product question, exact SQL, actual result, and interpretation boundary:

```sh
./companion/sql/sakila/run_product_query.sh
```

To run every concrete SQL example printed in Chapter 5 and compare its output with the book’s tables:

```sh
./companion/sql/sakila/run_chapter_examples.sh
```

## AI coding-agent experiment

After you understand the supplied query, ask an agent:

> Using the loaded Sakila SQLite database, propose one query that tests a different explanation for an availability problem. Before writing SQL, state the product question, decision, metric, output grain, denominator, join path, and one limitation. Wait for my approval. Then run the query and return the exact SQL and actual result. Do not change the upstream schema or data.

Review whether the SQL answers the stated question, whether a join multiplies rows, and whether the result supports the claimed decision. A syntactically valid query can still be product-wrong.

## Data provenance and licence

The files in `upstream/` come from jOOQ/sakila commit `e089a5b1ec9af0df7a9c6a5d47d49fa1736a4e84`. The source repository is licensed under BSD 2-Clause. Original notices remain in the SQL files and `LICENSE-jooq-sakila`.
