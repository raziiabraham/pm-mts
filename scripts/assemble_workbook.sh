#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
output="$root/companion/pm_mts_workbook.md"
tmp="$output.tmp"

files='companion/templates/00_workbook_intro.md
companion/templates/technical_floor_map.md
companion/templates/api_state_worksheet.md
companion/templates/release_path_record.md
companion/templates/image_requirement_record.md
companion/templates/product_data_question.md
companion/templates/tracking_plan.md
companion/templates/experiment_card.md
companion/templates/flow_to_acceptance.md
companion/templates/design_audit.md
companion/templates/component_contract.md
companion/templates/behavior_intervention_card.md
companion/templates/evidence_card.md
companion/templates/ai_solution_fit_decision.md
companion/templates/ai_evaluation_scorecard.md
companion/templates/prompt_evaluation_table.md
companion/templates/ai_calibration_record.md
companion/templates/context_brief.md
companion/templates/repo_orientation_map.md
companion/templates/assumption_evidence_map.md
companion/templates/prototype_contract.md
companion/templates/product_instrument_design.md
companion/templates/productionization_memo.md
companion/templates/pr_review_checklist.md
companion/templates/ship_decision_record.md
companion/templates/delivery_slice_record.md'

: > "$tmp"
for relative in $files; do
  path="$root/$relative"
  if [ ! -f "$path" ]; then
    printf 'Missing workbook component: %s\n' "$relative" >&2
    exit 1
  fi
  if [ -s "$tmp" ]; then
    printf '\n\n---\n\n' >> "$tmp"
  fi
  sed 's/[[:space:]]*$//' "$path" >> "$tmp"
  printf '\n' >> "$tmp"
done

mv "$tmp" "$output"
printf '%s\n' "$output"
