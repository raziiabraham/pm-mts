# Chapter 5: Read a Product Question in SQL

You do not need Python or a database setup to begin. Start with the product question, read the exact SQL, and inspect the supplied result. Run SQLite only when you want to reproduce or change the query.

This lab is not a tour of SQL syntax. It is **one investigation** against **one stated hypothesis**, and the hypothesis does not survive its first query.

## Product question

> Publishing is flat while the AI coworker is plainly busy. Which users are active in the product without ever publishing, and what important signals are absent from the database?

Write the hypothesis down before you run anything, because the point of the investigation is to find out whether it holds:

> **Working hypothesis.** Publishing is low because users are not engaged enough with the product. If that is true, the investment is engagement.

## What the product records

Noted is a workspace where people write documents, attach files, chat with an AI coworker beside their work, and configure Squad agents that take instructions from a document. Publishing is the moment private work becomes a page someone else can read.

| Table | Rows | Grain | Watch out for |
| --- | ---: | --- | --- |
| `users` | 50 | one person | **Derived.** Noted's product schema has no users table; identity lives in the auth provider. A real team would have to assemble this too. |
| `documents` | 243 | one document | `is_published` is the outcome the investigation is about |
| `files` | 55 | one attached file | carries both a single `documentId` and an optional `documentIds` array |
| `coworker_messages` | 50 | **one user, not one message** | a running count bucket; per-message grain exists only in `events` |
| `squad_agents` | 9 | one configured agent | Noted's second promise |
| `ai_settings` | 50 | one person | |
| `user_storage` | 50 | one person | cumulative, not per-file |
| `events` | 2,932 | one observed event | the analytics stream, which does **not** reconcile with the tables |

Two of these will bite anyone who skims. `coworker_messages` holds one row per *user* carrying a total, so joining it to `documents` and summing looks reasonable and silently multiplies. And the event stream delivers only about 79–85% of what the product tables recorded, on purpose — see [`PROVENANCE.md`](PROVENANCE.md).

## Exact SQL from the exercise

Fifteen queries build the argument; this is the one that ends it. It asks whether the engaged users are, in fact, the ones who never publish:

```sql
SELECT COUNT(*) AS engaged_users_never_published
FROM coworker_messages AS m
WHERE m.message_count >= 20
  AND NOT EXISTS (
      SELECT 1
      FROM documents AS d
      WHERE d.user_id = m.user_id
        AND d.is_published = 1
  );
```

[Open the full runnable file](queries/chapter_5_examples.sql)

## How to read the syntax

| SQL | Product meaning |
| --- | --- |
| `FROM coworker_messages AS m` | Start from the per-user count bucket, so the grain is one person |
| `m.message_count >= 20` | Define "engaged" as something countable rather than arguable |
| `NOT EXISTS (...)` | Absence is the question: users with **no** published document |
| `d.user_id = m.user_id` | Correlate the subquery to the user on the outer row |
| `d.is_published = 1` | The specific outcome whose absence matters |
| `COUNT(*)` | One number, because the hypothesis is a yes or no |

The output grain is **one user**. Note what this query deliberately avoids: joining `documents` to `coworker_messages` and aggregating, which would multiply each user's message total by their document count.

## Supplied result

```text
engaged_users_never_published
-----------------------------
27
```

Twenty-seven of fifty users have sent at least twenty coworker messages and have never published anything. Set against the totals the earlier queries print — 50 users, 2,895 coworker messages, 243 documents, and only 35 of them published — the working hypothesis is dead. These people are not disengaged. They are using the product heavily and stopping at exactly the step that delivers its promise.

That reverses the investment: the constraint is at publishing, not at engagement, and a quarter spent on onboarding nudges would have been spent on the wrong problem.

## What the result does—and does not—say

It locates *where* users stop. It does **not** say why.

The database records no reason for not publishing. There is no field for hesitation, no record of a user opening the publish control and abandoning it, no permissions confusion, no draft-quality judgment, and no record of work published somewhere else instead. Absence of a row is not evidence of a motive.

The rows are also synthetic: fifty users expanded from a fixed seed by Noted's own seeder, and the cohort was built to contain the patterns this chapter investigates. Every result is therefore **reproducible rather than discovered**, and none of these figures is a production measurement.

Before changing the SQL, state:

1. the decision you want to support;
2. the output grain;
3. the numerator and denominator;
4. the required join path;
5. the filter or time boundary; and
6. what the result still cannot prove.

Use the [Product Data Question Record](../../templates/product_data_question.md) to apply the method to your own product question.

## Optional: reproduce the investigation with SQLite

No Convex deployment, account, or network connection is required after cloning. From the repository root:

```sh
./companion/sql/noted/run_chapter_examples.sh
```

The script builds `noted.db` from the vendored seed on first run, then prints every Chapter 5 query with its actual result, in the order the chapter asks them. Building the database alone:

```sh
python3 companion/sql/noted/load_noted.py
```

Expect `users=50  documents=243  files=55  coworker_messages=50  squad_agents=9  ai_settings=50  user_storage=50  events=2932`.

The queries in `queries/` are generated from the chapter itself by `scripts/sync_chapter_5_examples.py`, so what prints here is what the book prints. To confirm nothing has drifted:

```sh
./companion/sql/validate_chapter_05.sh
```

Expected output:

```text
Chapter 5 Noted cohort load, book queries, and captured results passed.
```

That compares the whole transcript byte for byte against [`results/chapter_5_examples.expected`](results/chapter_5_examples.expected). It proves the supplied teaching files are internally consistent. It does not prove anything about a production system.

## AI coding-agent experiment

After you understand the investigation, ask an agent:

> Using the loaded Noted SQLite database, add one query that tests a different explanation for the publishing gap. Before writing SQL, state the product question, decision, metric, grain, denominator, join path, and one limitation. Run the query and return the command, SQL, and actual result. Do not change the upstream schema or data.

Then check its work the way you would check your own: is the grain what it claims, is the denominator the right one, and does the result support the decision or merely accompany it?

## Data provenance and licence

The cohort is synthetic and vendored, with its seeds, generators, and the one deliberate edit to the seeder output recorded in [`PROVENANCE.md`](PROVENANCE.md). That file also explains why the event stream does not reconcile with the product tables, and why the persona labels and the behavior sometimes disagree.

The superseded Sakila lab remains under [`../sakila/`](../sakila/) as standalone SQL practice on a larger open-licensed dataset.
