#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
work=$(mktemp -d)
database="$work/noted.db"
actual="$work/chapter_5_examples.actual"
trap 'rm -rf "$work"' EXIT HUP INT TERM

# Build the cohort from the vendored seed into a scratch database rather than
# reusing companion/sql/noted/noted.db, so the check cannot pass against a
# database someone has edited by hand. No Convex deployment, no network.
python3 "$here/noted/load_noted.py" --database "$database" >/dev/null

# Chapter 5 prints these exact rows, so the contract is byte-for-byte over the
# whole transcript, not merely that the SQL parses. queries/chapter_5_examples.sql
# is generated from the chapter by scripts/sync_chapter_5_examples.py, so a query
# edited in the book and a result captured here cannot drift apart unnoticed.
sqlite3 "$database" < "$here/noted/queries/chapter_5_examples.sql" > "$actual"
diff -u "$here/noted/results/chapter_5_examples.expected" "$actual"

printf '%s\n' 'Chapter 5 Noted cohort load, book queries, and captured results passed.'
