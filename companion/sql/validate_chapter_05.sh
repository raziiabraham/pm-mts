#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
work=$(mktemp -d)
database="$work/sakila.db"
actual="$work/film_demand_per_copy.actual"
trap 'rm -rf "$work"' EXIT HUP INT TERM

"$here/sakila/load_sakila.sh" "$database" >/dev/null

# Execute every query shape printed in Chapter 5 against the real Sakila
# schema. The detailed output is discarded here because syntax and schema
# compatibility are the regression contract for these examples.
sqlite3 "$database" < "$here/chapter_05_validation.sql" >/dev/null

# The worked product investigation has a stronger contract: the book prints
# these exact rows, so compare the deterministic output byte for byte.
sqlite3 -header -list -separator '|' "$database" \
    < "$here/sakila/queries/film_demand_per_copy.sql" > "$actual"
diff -u "$here/sakila/results/film_demand_per_copy.expected" "$actual"

printf '%s\n' 'Chapter 5 Sakila load, book queries, and captured result passed.'
