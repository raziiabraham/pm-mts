#!/bin/sh
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
actual=$(mktemp)
trap 'rm -f "$actual"' EXIT HUP INT TERM

sqlite3 ':memory:' < "$here/chapter_05_validation.sql" > "$actual"
diff -u "$here/chapter_05_validation.expected" "$actual"
printf '%s\n' 'Chapter 5 representative SQL examples passed.'
