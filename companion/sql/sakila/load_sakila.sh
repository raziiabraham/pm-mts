#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
database=${1:-"$here/sakila.db"}
schema="$here/upstream/sqlite-sakila-schema.sql"
data="$here/upstream/sqlite-sakila-insert-data.sql"

if ! command -v sqlite3 >/dev/null 2>&1; then
    printf '%s\n' 'SQLite is required. Install SQLite 3.40 or later, then rerun this command.' >&2
    exit 1
fi

rm -f "$database"
sqlite3 "$database" < "$schema"
sqlite3 "$database" < "$data"

counts=$(sqlite3 -separator '|' "$database" "
SELECT
    (SELECT COUNT(*) FROM customer),
    (SELECT COUNT(*) FROM film),
    (SELECT COUNT(*) FROM inventory),
    (SELECT COUNT(*) FROM rental),
    (SELECT COUNT(*) FROM payment),
    (SELECT COUNT(*) FROM store);
")

expected='599|1000|4581|16044|16049|2'
if [ "$counts" != "$expected" ]; then
    printf 'Unexpected Sakila row counts: %s\n' "$counts" >&2
    exit 1
fi

printf 'Loaded Sakila into %s\n' "$database"
printf '%s\n' 'Verified: 599 customers, 1,000 films, 4,581 inventory copies, 16,044 rentals, 16,049 payments, and 2 stores.'
