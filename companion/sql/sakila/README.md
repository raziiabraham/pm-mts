# Sakila hands-on lab

This lab uses the real generated Sakila sample data from the [jOOQ/sakila](https://github.com/jOOQ/sakila) repository, not the miniature fictional fixture previously used by the companion. The vendored SQLite port keeps the exercise runnable without Docker, a database server, an account, or a network connection after cloning this repository.

From the repository root, load the database:

```sh
./companion/sql/sakila/load_sakila.sh
```

The loader creates `companion/sql/sakila/sakila.db` and verifies these source row counts: 599 customers, 1,000 films, 4,581 inventory copies, 16,044 rentals, 16,049 payments, and two stores.

Then print the product question, exact SQL, actual result, and interpretation boundary:

```sh
./companion/sql/sakila/run_product_query.sh
```

To run every concrete SQL example printed in Chapter 5 and compare the terminal output with Tables 5.1–5.8:

```sh
./companion/sql/sakila/run_chapter_examples.sh
```

The generic `SELECT ... FROM ... WHERE ...` syntax template and the MongoDB translation are not included because they are not executable Sakila SQLite queries.

The worked question asks which frequently rented films may be constrained by inventory supply. It divides recorded rentals by inventory copies so that a heavily stocked title is not ranked only because it has more copies. This remains a diagnostic proxy: the dataset does not record failed searches, unavailable-title attempts, copy downtime, or causal demand.

The source spelling `SEATTLE EXPECATIONS` is intentionally preserved because it is what the generated dataset contains. Do not silently clean source data while claiming to reproduce a query result.

## AI coding-agent prompt

After the supplied query runs, give an AI coding agent this bounded task:

> Using the loaded Sakila SQLite database, add one query that tests a different explanation for an availability problem. Before writing SQL, state the product question, decision, metric, grain, denominator, join path, and one limitation. Run the query and return the command, SQL, and actual result. Do not change the upstream schema or data.

Review the agent's SQL before accepting the result. Confirm the table relationships, the unit represented by each output row, whether a join multiplies records, and whether the result actually bears on the stated decision.

## Data provenance and licence

The files in `upstream/` were copied from jOOQ/sakila commit `e089a5b1ec9af0df7a9c6a5d47d49fa1736a4e84`. The root repository is licensed under BSD 2-Clause. The SQLite source headers also credit DB Software Laboratory and describe the original Sakila database developed by Mike Hillyer for the MySQL documentation team. The original notices are retained in the SQL files, and `LICENSE-jooq-sakila` is included beside them.
