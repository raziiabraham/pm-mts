#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
database="$here/sakila.db"
queries="$here/queries/chapter_5_examples.sql"

if [ ! -f "$database" ]; then
    "$here/load_sakila.sh" "$database"
    printf '\n'
fi

cd "$here"
sqlite3 "$database" < "$queries"
