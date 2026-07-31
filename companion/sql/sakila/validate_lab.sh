#!/bin/sh
# Standalone regression for the Sakila SQL lab.
#
# Chapter 5 moved to the Noted cohort, so this is no longer the book's
# Chapter 5 contract and is deliberately NOT wired into
# scripts/validate_companion.sh. It keeps the lab verifiable for readers who
# work through it as general SQL practice.
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
work=$(mktemp -d)
database="$work/sakila.db"
actual="$work/film_demand_per_copy.actual"
trap 'rm -rf "$work"' EXIT HUP INT TERM

"$here/load_sakila.sh" "$database" >/dev/null

# Every query shape the lab teaches, checked for syntax and schema
# compatibility; the detailed output is not the contract here.
sqlite3 "$database" < "$here/lab_validation.sql" >/dev/null

# The worked rentals-per-copy investigation is deterministic, so compare it
# byte for byte.
sqlite3 -header -list -separator '|' "$database" \
    < "$here/queries/film_demand_per_copy.sql" > "$actual"
diff -u "$here/results/film_demand_per_copy.expected" "$actual"

printf '%s\n' 'Sakila lab load, queries, and captured result passed.'
