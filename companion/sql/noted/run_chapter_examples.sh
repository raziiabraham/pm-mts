#!/bin/sh
# Run every Chapter 5 query against the vendored Noted cohort and print its
# result, in the order the chapter asks them. The queries in queries/ are
# generated from the chapter itself, so what prints here is what the book prints.
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
database="$here/noted.db"
queries="$here/queries/chapter_5_examples.sql"

if [ ! -f "$database" ]; then
    python3 "$here/load_noted.py" --database "$database"
    printf '\n'
fi

cd "$here"
sqlite3 "$database" < "$queries"
