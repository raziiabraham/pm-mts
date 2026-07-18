#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

python3 "$root/scripts/validate_guidance.py"
python3 "$root/companion/api/validate_contract.py"
"$root/companion/sql/validate_chapter_05.sh"
python3 "$root/companion/analytics/validate_tracking.py"
python3 "$root/companion/ai_evaluation/evaluate.py"
python3 "$root/companion/calibration/validate_record.py"
noted_repo=${NOTED_REPO_PATH:-"$root/../noted-main"}
if [ -d "$noted_repo" ]; then
    python3 "$root/companion/repo_orientation/validate_task.py" "$noted_repo"
else
    printf '%s\n' 'Chapter 17 repo-orientation check skipped: clone Noted beside pm-mts or set NOTED_REPO_PATH to include it.'
fi
python3 "$root/companion/feedback_instrument/validate_dataset.py"

printf '%s\n' 'Companion validation passed.'
