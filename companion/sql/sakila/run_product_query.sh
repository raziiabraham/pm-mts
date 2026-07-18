#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
database="$here/sakila.db"
query="$here/queries/film_demand_per_copy.sql"

if [ ! -f "$database" ]; then
    "$here/load_sakila.sh" "$database"
    printf '\n'
fi

printf '%s\n' 'Product question:'
printf '%s\n' 'Which frequently rented films may be constrained by inventory supply?'
printf '\n%s\n' 'Query:'
sed -n '1,200p' "$query"
printf '\n%s\n' 'Result from the loaded Sakila database:'
sqlite3 -header -column "$database" < "$query"
printf '\n%s\n' 'Interpretation boundary:'
printf '%s\n' 'Rentals per copy is a diagnostic proxy. It does not observe failed searches, unavailable-title attempts, copy downtime, or causal demand.'
