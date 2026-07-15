#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

python3 "$root/companion/api/validate_contract.py"
"$root/companion/sql/validate_chapter_05.sh"
python3 "$root/companion/analytics/validate_tracking.py"
python3 "$root/companion/ai_evaluation/evaluate.py"
python3 "$root/companion/calibration/validate_record.py"
python3 "$root/companion/repo_orientation/validate_task.py"
python3 "$root/companion/feedback_instrument/validate_dataset.py"

printf '%s\n' 'Companion validation passed.'
